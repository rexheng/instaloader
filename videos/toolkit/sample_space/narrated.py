"""NarratedScene: Manim scenes driven by synthesized narration beats.

    from manim import *
    from sample_space import *

    class Episode(NarratedScene):
        EPISODE = 12
        TITLE = "Why averages lie"

        def construct(self):
            with self.narrate("A coin is flipped ten times.") as beat:
                self.play(Create(axes), run_time=beat.until("ten"))   # lands on "ten"
                self.play(FadeIn(dots), run_time=beat.remaining())
            # leaving the block waits for the audio to finish (+ BEAT_GAP)

Each beat's audio is added with ``self.add_sound`` at the beat's start time.  At the
end of the render the scene writes ``narration.json`` + ``narration.txt`` (beat start
times, word timings, timing/layout warnings) into $SS_NARRATION_DIR (set by render.sh
to the output directory) or next to the scene file.
"""
from __future__ import annotations

import contextlib
import inspect
import json
import logging
import os
from pathlib import Path

import numpy as np
from manim import (FadeIn, FadeOut, MathTex, MovingCameraScene, Scene, SingleStringMathTex,
                   Tex, Text, MarkupText, Paragraph, DecimalNumber, VMobject, config)

from . import style
from .voice import Speech, synthesize

log = logging.getLogger("sample_space")
if not log.handlers:
    _h = logging.StreamHandler()
    _h.setFormatter(logging.Formatter("[sample_space] %(levelname)s %(message)s"))
    log.addHandler(_h)
    log.setLevel(logging.INFO)
    log.propagate = False

TEXT_TYPES = (Text, MarkupText, Paragraph, MathTex, Tex, SingleStringMathTex, DecimalNumber)


class Beat:
    """Timing handle for one narrated beat (all values in seconds)."""

    def __init__(self, scene: "NarrationMixin", index: int, speech: Speech, start: float):
        self.scene, self.index, self.speech, self.start = scene, index, speech, start
        self.sync_notes: list[str] = []

    # -- basic timing
    @property
    def duration(self) -> float:
        return self.speech.duration

    @property
    def words(self):
        return self.speech.words

    def elapsed(self) -> float:
        return self.scene.time - self.start

    def _min(self) -> float:
        return 2.0 / config.frame_rate

    @staticmethod
    def _snap(seconds: float) -> float:
        """A run_time that renders exactly round(seconds*fps) frames (Manim renders
        ceil(run_time*fps) frames, so aim half a frame low to dodge float noise)."""
        fps = config.frame_rate
        return (max(1, round(seconds * fps)) - 0.5) / fps

    def remaining(self, min_time: float | None = None) -> float:
        """Seconds until the narration audio of this beat ends (>= 2 frames)."""
        return self._snap(max(self._min() if min_time is None else min_time,
                              self.duration - self.elapsed()))

    # -- word-triggered timing
    def time_of(self, phrase: str, occurrence: int = 1, end: bool = False) -> float:
        """Beat-relative time at which `phrase` starts (or ends) being spoken."""
        w = self.speech.find(phrase, occurrence)
        if w is None:
            spoken = " ".join(x.text for x in self.words)
            raise KeyError(f"beat {self.index}: {phrase!r} (occurrence {occurrence}) not in "
                           f"narration: {spoken!r}")
        return w.end if end else w.start

    def until(self, phrase: str, occurrence: int = 1, offset: float = 0.0, end: bool = False,
              min_time: float | None = None) -> float:
        """Seconds from *now* until `phrase` is spoken - use as a run_time so that the
        NEXT animation starts on that word.  offset<0 starts early (e.g. -0.15 so a
        highlight is already visible as the word lands)."""
        target = self.time_of(phrase, occurrence, end) + offset
        dt = target - self.elapsed()
        floor = self._min() if min_time is None else min_time
        if dt < floor - 0.3:
            self.sync_notes.append(f"beat {self.index}: animations reached {phrase!r} "
                                   f"{floor - dt:.2f}s after it was spoken - narration and "
                                   f"visuals out of sync; shorten the preceding animations")
        return self._snap(max(floor, dt))

    def until_end_of(self, phrase: str, occurrence: int = 1, offset: float = 0.0) -> float:
        return self.until(phrase, occurrence, offset, end=True)

    def wait_until(self, phrase: str, occurrence: int = 1, offset: float = 0.0) -> None:
        """Hold the frame until `phrase` is spoken."""
        target = self.time_of(phrase, occurrence) + offset
        dt = target - self.elapsed()
        if dt < -0.3:
            self.sync_notes.append(f"beat {self.index}: reached {phrase!r} {-dt:.2f}s after it "
                                   f"was spoken - shorten the preceding animations")
        self.scene.hold(dt)

    def wait_remaining(self) -> None:
        self.scene.hold(self.duration - self.elapsed())


class NarrationMixin:
    """Mix into any Scene subclass. See module docstring."""

    EPISODE: int | None = None
    TITLE: str | None = None
    VOICE: str | None = None              # default: sample_space.voice.DEFAULT_VOICE (af_heart)
    SPEED: float | None = None
    PRONUNCIATIONS: dict[str, str] = {}   # per-episode extra overrides
    BEAT_GAP = 0.35                       # breathing room after each beat (s)
    STATIC_WARN = 4.0                     # BAR: a fully static frame lasts <= 4 s
    CHECK_LAYOUT = True

    # ------------------------------------------------------------------ lifecycle
    def setup(self):
        super().setup()
        style.apply_defaults()
        self.camera.background_color = style.BG
        self._beats: list[dict] = []
        self._warnings: list[dict] = []
        self._beat_index = 0

    def tear_down(self):
        try:
            self._write_narration()
        finally:
            super().tear_down()

    def play(self, *args, **kwargs):
        """Scene.play, kept frame-accurate when Manim serves the clip from its cache.

        On a cache hit Manim advances scene time by the exact run_time, but the cached clip
        holds whole frames; over a long episode that drift (up to 1 frame per animation)
        would pull narration audio seconds ahead of the picture.  Re-sync it here."""
        r = self.renderer
        t0 = r.time
        super().play(*args, **kwargs)
        hashes = getattr(r, "animations_hashes", None)
        if r.skip_animations and hashes and hashes[-1] is not None:
            dt = 1.0 / self.camera.frame_rate
            try:
                frozen = self.is_current_animation_frozen_frame()
            except Exception:
                frozen = False
            n = int(self.duration / dt) if frozen else len(np.arange(0, self.duration, 1 / config.frame_rate))
            r.time = t0 + n * dt
        # video time is always a whole number of frames; drop accumulated float noise so
        # timings (and therefore cache hashes) are identical between cold and cached runs
        r.time = round(r.time * self.camera.frame_rate) / self.camera.frame_rate

    def add_audio(self, path: str, gain: float | None = None) -> None:
        """Cache-safe add_sound (use it for sound effects too).

        Manim drops sounds while `skip_animations` is set, and a partial-movie cache hit
        leaves it set until the next play(), so on re-renders every beat that follows a
        cached animation would silently lose its audio."""
        r = self.renderer
        hashes = getattr(r, "animations_hashes", None) or []
        cache_hit = r.skip_animations and hashes and hashes[-1] is not None
        if r.skip_animations and not cache_hit:
            return                                   # genuinely skipped (-n / sections)
        r.file_writer.add_sound(path, self.time, gain)

    def hold(self, seconds: float) -> None:
        """Frame-exact wait: shows the current frame for round(seconds*fps) frames."""
        fps = self.camera.frame_rate
        n = round(seconds * fps)
        if n < 1:
            return
        moving = (self.always_update_mobjects or self.updaters or
                  any(m.has_time_based_updater() for m in self.get_mobject_family_members()))
        # Manim renders int(d*fps) frames for a frozen wait but ceil(d*fps) when updaters run
        self.wait((n - 0.5) / fps if moving else (n + 0.5) / fps)

    # ------------------------------------------------------------------ narration
    @contextlib.contextmanager
    def narrate(self, text: str, *, voice: str | None = None, speed: float | None = None,
                gap: float | None = None, overrides: dict | None = None):
        """Speak `text` while the body of the with-block animates.  Yields a Beat."""
        ov = dict(self.PRONUNCIATIONS)
        if overrides:
            ov.update(overrides)
        speech = synthesize(text, voice=voice or self.VOICE, speed=speed or self.SPEED,
                            overrides=ov or None)
        idx = self._beat_index
        self._beat_index += 1
        start = self.time
        if idx == 0 and start > 1.0:
            self._warn(start, f"first narration starts at {start:.2f}s (BAR: leading silence <= 1 s)")
        self.add_audio(speech.wav_path)
        for s in speech.sentences:
            try:
                self.add_subcaption(s["text"], duration=s["end"] - s["start"], offset=s["start"])
            except Exception:                        # subcaptions are a nicety only
                pass
        beat = Beat(self, idx, speech, start)
        yield beat
        # ---- on normal exit: let the audio finish, then breathe
        elapsed = self.time - start
        g = self.BEAT_GAP if gap is None else gap
        left = speech.duration + g - elapsed
        if left >= 1.0 / config.frame_rate:
            if left > self.STATIC_WARN:
                self._warn(self.time, f"beat {idx}: holding a static frame for {left:.1f}s while "
                           f"narration finishes (BAR static limit 4 s) - add motion or split the beat")
            self.hold(left)
        elif elapsed > speech.duration + max(g, 0.5) + 0.5:
            self._warn(self.time, f"beat {idx}: animations ran {elapsed - speech.duration:.1f}s past "
                       f"the narration ({speech.duration:.1f}s) - silence gap")
        for n in beat.sync_notes:
            self._warn(start, n)
        self._beats.append({
            "index": idx, "start": round(start, 3), "duration": speech.duration,
            "end": round(start + speech.duration, 3), "text": text, "voice": speech.voice,
            "words": [{"w": w.text, "t": round(start + w.start, 3), "end": round(start + w.end, 3)}
                      for w in speech.words],
            "wav": speech.wav_path,
        })
        if self.CHECK_LAYOUT:
            for issue in layout_issues(self):
                self._warn(self.time, f"beat {idx} layout: {issue}")

    def say(self, text: str, **kw) -> Beat:
        """Narrate over whatever is on screen (no new animation)."""
        with self.narrate(text, **kw) as beat:
            pass
        return beat

    def narrate_play(self, text: str, *animations, **kw) -> None:
        """Narrate while playing `animations` stretched across the whole beat."""
        with self.narrate(text, **kw) as beat:
            self.play(*animations, run_time=beat.remaining())

    # ------------------------------------------------------------------ helpers
    def fade_out_all(self, *exclude, run_time: float = style.QUICK):
        """FadeOut everything on screen except `exclude` (a deliberate hard reset)."""
        mobs = [m for m in self.mobjects if m not in exclude]
        if mobs:
            self.play(*[FadeOut(m) for m in mobs], run_time=run_time)

    def end_card(self, hold: float = 0.8, run_time: float = 0.5):
        """Fade everything out and show the series card: 1.3 s, so that with the last beat's
        gap the trailing silence stays under BAR's 2 s."""
        card = style.end_card(self.EPISODE, self.TITLE)
        mobs = list(self.mobjects)
        anims = [FadeOut(m) for m in mobs] + [FadeIn(card, shift=0.1 * np.array([0, 1, 0]))]
        self.play(*anims, run_time=run_time)
        self.hold(hold)

    def check_layout(self, tag: str = "manual") -> list[str]:
        issues = layout_issues(self)
        for i in issues:
            self._warn(self.time, f"{tag} layout: {i}")
        return issues

    def _warn(self, t: float, msg: str):
        self._warnings.append({"t": round(t, 2), "msg": msg})
        log.warning("t=%.2fs %s", t, msg)

    # ------------------------------------------------------------------ output
    def _narration_dir(self) -> Path:
        d = os.environ.get("SS_NARRATION_DIR")
        if d:
            return Path(d)
        try:
            return Path(inspect.getfile(self.__class__)).resolve().parent
        except (TypeError, OSError):
            return Path.cwd()

    def _write_narration(self):
        if not getattr(self, "_beats", None) and not getattr(self, "_warnings", None):
            return
        out = self._narration_dir()
        out.mkdir(parents=True, exist_ok=True)
        total = float(self.time)
        data = {
            "scene": type(self).__name__, "episode": self.EPISODE, "title": self.TITLE,
            "video_duration": round(total, 3), "beats": self._beats, "warnings": self._warnings,
        }
        (out / "narration.json").write_text(json.dumps(data, ensure_ascii=False, indent=1))
        lines = []
        for b in self._beats:
            m, s = divmod(b["start"], 60)
            lines.append(f"[{int(m):02d}:{s:04.1f}] {b['text']}")
        (out / "narration.txt").write_text("\n\n".join(lines) + "\n")
        n_words = sum(len(b["words"]) for b in self._beats)
        speech = sum(b["duration"] for b in self._beats)
        log.info("narration: %d beats, %d words, %.1fs speech in %.1fs video (%.0f wpm overall), "
                 "%d warnings -> %s", len(self._beats), n_words, speech, total,
                 60 * n_words / max(total, 1e-6), len(self._warnings), out / "narration.json")


class NarratedScene(NarrationMixin, Scene):
    pass


class NarratedMovingCameraScene(NarrationMixin, MovingCameraScene):
    pass


# ---------------------------------------------------------------------- layout check
def _self_visible(x) -> bool:
    try:
        stroke = x.get_stroke_opacity() if x.get_stroke_width() > 0 else 0.0
        return len(x.points) > 0 and max(x.get_fill_opacity(), stroke) > 0.05
    except Exception:
        return len(getattr(x, "points", ())) > 0


def _visible(m: VMobject) -> bool:
    return any(_self_visible(x) for x in m.get_family())


def _collect(mobs, texts, shapes):
    for m in mobs:
        if getattr(m, "ss_allow_overlap", False):
            continue
        if isinstance(m, TEXT_TYPES):
            if _visible(m) and m.width > 0 and m.height > 0:
                texts.append(m)
            continue
        if isinstance(m, VMobject) and _self_visible(m):
            shapes.append(m)
        _collect(m.submobjects, texts, shapes)


def allow_overlap(m):
    """Exclude a mobject (and its children) from the automatic layout check."""
    m.ss_allow_overlap = True
    return m


def _name(m) -> str:
    if isinstance(m, (Text, MarkupText)):
        return f"Text({getattr(m, 'original_text', m.text)[:30]!r})"
    if isinstance(m, (MathTex, Tex, SingleStringMathTex)):
        return f"{type(m).__name__}({getattr(m, 'tex_string', '')[:30]!r})"
    if isinstance(m, DecimalNumber):
        return f"DecimalNumber({m.get_value():g})"
    return type(m).__name__


def layout_issues(scene, shrink: float = 0.03) -> list[str]:
    """Cheap static check of the current frame: text outside the BAR safe area, text
    overlapping text, and shapes cutting through text.  Bounding-box based, so treat
    hits as 'look at this frame', not gospel."""
    texts, shapes = [], []
    _collect(scene.mobjects, texts, shapes)
    issues = []
    boxes = []
    for t in texts:
        lo, hi = t.get_corner([-1, -1, 0]), t.get_corner([1, 1, 0])
        boxes.append((lo, hi))
        if lo[0] < -style.SAFE_X - 0.02 or hi[0] > style.SAFE_X + 0.02 or \
                lo[1] < style.SAFE_BOTTOM - 0.02 or hi[1] > style.SAFE_TOP + 0.02:
            issues.append(f"{_name(t)} outside safe area x[{lo[0]:.2f},{hi[0]:.2f}] "
                          f"y[{lo[1]:.2f},{hi[1]:.2f}]")
        elif lo[1] < style.CONTENT_BOTTOM - 0.02 and not getattr(t, "ss_caption_zone", False):
            issues.append(f"{_name(t)} reaches y={lo[1]:.2f}, below y=-3.2 (caption/player zone; "
                          f"BAR: nothing essential there)")
    # text vs text
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            (a0, a1), (b0, b1) = boxes[i], boxes[j]
            if texts[i] in texts[j].get_family() or texts[j] in texts[i].get_family():
                continue
            ox = min(a1[0], b1[0]) - max(a0[0], b0[0])
            oy = min(a1[1], b1[1]) - max(a0[1], b0[1])
            if ox > shrink and oy > shrink:
                issues.append(f"{_name(texts[i])} overlaps {_name(texts[j])}")
    # shapes through text
    for t, (lo, hi) in zip(texts, boxes):
        lo2, hi2 = lo + shrink, hi - shrink
        fam = set(map(id, t.get_family()))
        for s in shapes:
            if id(s) in fam:
                continue
            pts = s.points
            inside = np.all((pts[:, :2] > lo2[:2]) & (pts[:, :2] < hi2[:2]), axis=1)
            if inside.any():
                issues.append(f"{type(s).__name__} crosses {_name(t)}")
                break
    return issues
