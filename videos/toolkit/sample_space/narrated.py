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

After every play() and wait()/hold() the overlap audit (sample_space.overlap_audit) checks
the frame for text closer than 0.15 units to anything else or outside the safe area; the
findings are merged into time ranges, printed as ``[sample_space] WARNING overlap ...``
and stored in narration.json["layout_audit"].  Opt out with ``LAYOUT_AUDIT = False``;
exempt a deliberate overlap with ``self.allow_overlap(a, b, reason="...")``.
"""
from __future__ import annotations

import contextlib
import inspect
import json
import logging
import os
import time as _time
from pathlib import Path

import numpy as np
from manim import FadeIn, FadeOut, MovingCameraScene, Scene, Wait, config

from . import overlap_audit, style
from .voice import Speech, synthesize

log = logging.getLogger("sample_space")
if not log.handlers:
    _h = logging.StreamHandler()
    _h.setFormatter(logging.Formatter("[sample_space] %(levelname)s %(message)s"))
    log.addHandler(_h)
    log.setLevel(logging.INFO)
    log.propagate = False

TEXT_TYPES = overlap_audit.TEXT_TYPES


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
    LAYOUT_AUDIT = True                   # overlap audit after every play()/wait() (BAR §5)
    LAYOUT_CLEARANCE = style.MIN_GAP      # 0.15 units between text and anything else
    CHECK_LAYOUT = True                   # legacy switch; False also disables the audit

    # ------------------------------------------------------------------ lifecycle
    def setup(self):
        super().setup()
        style.apply_defaults()
        self.camera.background_color = style.BG
        self._beats: list[dict] = []
        self._warnings: list[dict] = []
        self._beat_index = 0
        self._audit = overlap_audit.AuditLog()
        self._audit_allowed: list[tuple] = []
        self._audit_excluded: list[tuple] = []
        self._wall_start = _time.perf_counter()

    def tear_down(self):
        try:
            self._finish_audit()
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
        if self.LAYOUT_AUDIT and self.CHECK_LAYOUT:
            held = len(args) == 1 and isinstance(args[0], Wait)
            self._run_audit(t0, r.time, held)

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
        # layout: the overlap audit runs after every play()/wait() (see _run_audit)

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
        """Audit the current frame now and warn about every issue (also runs by itself
        after each play()/wait() unless LAYOUT_AUDIT = False)."""
        issues = layout_issues(self)
        for i in issues:
            self._warn(self.time, f"{tag} layout: {i}")
        return issues

    def allow_overlap(self, a, b=None, reason: str = ""):
        """Declare a deliberate overlap so the audit stops reporting it.
            self.allow_overlap(label, axis_line, reason="label marks the crossing point")
        With one argument, `a` (and everything in it) is left out of the audit entirely.
        Give a reason: it is stored in narration.json for the critics."""
        if b is None:
            allow_overlap(a)
            self._audit_excluded.append((a, reason or "excluded (no reason given)"))
            return a
        self._audit_allowed.append((a, b, reason or "allowed (no reason given)"))
        return a

    # ------------------------------------------------------------------ overlap audit
    def _run_audit(self, t0: float, t1: float, held: bool) -> None:
        """Audit the frame after an animation (never raises into the render)."""
        log_ = getattr(self, "_audit", None)
        if log_ is None:
            return
        c0 = _time.perf_counter()
        try:
            issues = overlap_audit.audit(self.mobjects, camera=getattr(self.renderer, "camera", None),
                                         allowed_pairs=self._audit_allowed,
                                         clearance=self.LAYOUT_CLEARANCE)
            log_.update(issues, t0, t1, held)
        except Exception as e:                       # the audit must never break a render
            log_.errors += 1
            if log_.errors == 1:
                log.debug("overlap audit failed at t=%.2fs (%s: %s); skipping that check",
                          t1, type(e).__name__, e)
        finally:
            log_.seconds += _time.perf_counter() - c0

    def _finish_audit(self) -> None:
        log_ = getattr(self, "_audit", None)
        if log_ is None:
            return
        try:
            log_.close_all(self.time)
            found = log_.findings()
            live = [f for f in found if not f.issue.allowed]
            # every overlap / frame problem; the 25 tightest clearance findings
            ranked = overlap_audit.rank_findings(live)
            severe = [f for f in ranked if f.issue.kind != "clearance"]
            tight = [f for f in ranked if f.issue.kind == "clearance"][:25]
            sev = overlap_audit.SEVERITY
            for f in sorted(severe + tight, key=lambda f: (sev.get(f.issue.kind, 9), f.start)):
                log.warning("%s %s", f.issue.kind, overlap_audit.finding_line(f))
            more = len(live) - len(severe) - len(tight)
            if more:
                log.warning("clearance ... and %d more (smaller or shorter) in narration.json -> "
                            "layout_audit", more)
            self._audit_summary = self._audit_report(found)
        except Exception as e:
            log.debug("overlap audit summary failed (%s: %s)", type(e).__name__, e)
            self._audit_summary = None

    def _audit_report(self, found) -> dict:
        log_ = self._audit
        live = [f for f in found if not f.issue.allowed]
        counts = {k: sum(1 for f in live if f.issue.kind == k)
                  for k in ("overlap", "clearance", "safe-area", "caption-zone")}
        wall = _time.perf_counter() - getattr(self, "_wall_start", _time.perf_counter())
        return {
            "clearance": self.LAYOUT_CLEARANCE, "checks": log_.checks,
            "audit_seconds": round(log_.seconds, 3), "render_seconds": round(wall, 1),
            "errors": log_.errors, "count": len(live), "counts": counts,
            "issues": [overlap_audit.finding_dict(f) for f in live],
            "allowed": [overlap_audit.finding_dict(f) for f in found if f.issue.allowed],
            "excluded": [{"mobject": type(m).__name__, "reason": r}
                         for m, r in getattr(self, "_audit_excluded", [])],
        }

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
        audit = getattr(self, "_audit_summary", None)
        if not getattr(self, "_beats", None) and not getattr(self, "_warnings", None) and \
                not (audit and (audit["issues"] or audit["allowed"] or audit["errors"])):
            return
        out = self._narration_dir()
        out.mkdir(parents=True, exist_ok=True)
        total = float(self.time)
        data = {
            "scene": type(self).__name__, "episode": self.EPISODE, "title": self.TITLE,
            "video_duration": round(total, 3), "beats": self._beats, "warnings": self._warnings,
        }
        if audit is not None:
            data["layout_audit"] = audit
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
        if audit is not None:
            c = audit["counts"]
            log.info("layout audit: %d issue(s) (%d overlap, %d clearance < %.2f, %d safe-area, "
                     "%d caption-zone; %d allowed) in %d checks%s; audit %.1fs = %.1f%% of %.0fs render",
                     audit["count"], c["overlap"], c["clearance"], audit["clearance"],
                     c["safe-area"], c["caption-zone"], len(audit["allowed"]), audit["checks"],
                     f" ({audit['errors']} skipped after an internal error)" if audit["errors"] else "",
                     audit["audit_seconds"], 100 * audit["audit_seconds"] / max(audit["render_seconds"], 1e-6),
                     audit["render_seconds"])


class NarratedScene(NarrationMixin, Scene):
    pass


class NarratedMovingCameraScene(NarrationMixin, MovingCameraScene):
    pass


# ---------------------------------------------------------------------- layout check
def allow_overlap(m):
    """Leave a mobject (and its children) out of the overlap audit entirely.  Prefer
    scene.allow_overlap(a, b, reason=...) for one deliberate pair."""
    m.ss_allow_overlap = True
    return m


def layout_issues(scene, clearance: float | None = None) -> list[str]:
    """Overlap audit of the current frame (see sample_space.overlap_audit), as strings:
    text outside the safe area or in the caption zone, text within `clearance` (0.15) of
    other text or of any line, curve, dot or shape, text crossed by a panel's outline."""
    issues = overlap_audit.audit(
        scene.mobjects, camera=getattr(getattr(scene, "renderer", None), "camera", None),
        allowed_pairs=getattr(scene, "_audit_allowed", ()),
        clearance=clearance if clearance is not None else
        getattr(scene, "LAYOUT_CLEARANCE", style.MIN_GAP))
    return [f"{i.kind}: {i.describe()}" for i in issues if not i.allowed]
