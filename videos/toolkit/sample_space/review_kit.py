"""Evidence pack for critics who can only look at images and read text.

    videos/toolkit/review_kit.sh <video.mp4> <outdir> [--narration narration.json|.txt]
                                 [--no-whisper] [--interval 2] [--max-keyframes 40]

Writes into <outdir>:
    report.md            summary: BAR mechanics with flags, sheets, keyframes, transcript, diffs
    metrics.json         every number in machine-readable form
    sheets/sheet_NN.png  contact sheets: one frame every 2 s, 3x3 tiles of 640x360, each stamped
                         with its time and the words spoken within +-1 s of it
    keyframes/kf_NN_<mm-ss.s>.png   full 1920x1080 frames at moments where the picture settles
    transcript.txt / transcript_words.tsv / transcript.json   Groq whisper-large-v3-turbo
    narration_diff.txt   word-level diff + WER against the intended narration
If no --narration is given, narration.json next to the video is used when present.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import sys
import time
from difflib import SequenceMatcher
from pathlib import Path

import numpy as np

TOOLKIT = Path(__file__).resolve().parent.parent
HOME = Path(os.environ.get("SAMPLE_SPACE_HOME", Path.home() / ".cache" / "sample_space"))
GROQ_URL = "https://api.groq.com/openai/v1/audio/transcriptions"
WHISPER_MODEL = "whisper-large-v3-turbo"

# BAR thresholds (videos/BAR.md §3 hard caps, §5 standards)
RUNTIME = (150.0, 240.0)
WPM = (140.0, 165.0)
WPM_CAP = (120.0, 180.0)
MAX_INTERNAL_SILENCE = 2.5
MAX_LEADING_SILENCE = 1.0
MAX_TRAILING_SILENCE = 2.0
STATIC_FLAG, STATIC_CAP = 4.0, 8.0
LUFS_TARGET, LUFS_TOL, LUFS_CAP_TOL = -14.0, 1.0, 3.0
TP_MAX, TP_CAP = -1.5, -1.0

FALLBACK_BANNED = [
    "in today's video", "let's dive in", "dive into", "delve", "it's important to note",
    "it's worth noting", "in conclusion", "in summary", "to sum up", "so to recap",
    "key takeaway", "game-changer", "unlock", "harness", "leverage", "the world of",
    "the realm of", "the landscape of", "buckle up", "without further ado", "let's get started",
    "imagine a world where", "picture this", "ever wondered", "have you ever wondered",
    "what if I told you", "here's the thing", "here's the kicker", "but here's the twist",
    "this is where X comes in", "enter: X", "plays a crucial role", "a testament to",
    "the power of", "the magic of", "navigate the complexities", "rich tapestry", "intricate",
    "journey", "seamless", "revolutionize", "cutting-edge", "mind-blowing", "incredible",
    "fascinating", "powerful tool", "data tells a story", "numbers don't lie", "simply put",
    "in a nutshell", "basically", "essentially", "stay tuned", "thanks for watching",
    "like and subscribe"]
PATTERNS = [  # (name, regex, allowed occurrences)
    ("'it's not just X, it's Y'", r"\bit'?s not (just|only)\b[^.?!]{1,80}?\bit'?s\b", 0),
    ("'X isn't just Y'", r"\b(isn'?t|aren'?t|wasn'?t) (just|only|merely)\b", 0),
    ("hedging 'in a sense'", r"\bin a sense\b", 0),
    ("hedging 'kind of/sort of'", r"(?<!what )(?<!this )(?<!that )(?<!the )(?<!any )\b(kind|sort) of\b", 0),
    ("signpost 'now let's look at'", r"\bnow let'?s (look|take a look)\b", 1),
    ("signpost 'let's break it down'", r"\blet'?s break (it|this) down\b", 1),
    ("signpost 'it turns out'", r"\bit turns out\b", 1),
    ("empty superlative 'beautiful/surprising'", r"\b(beautiful|surprising(ly)?|stunning|amazing)\b", 2),
]


# ----------------------------------------------------------------------------- utils
def sh(cmd: list[str], check=True) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, check=check)


def fmt_t(t: float) -> str:
    m, s = divmod(max(t, 0.0), 60)
    return f"{int(m)}:{s:04.1f}"


def probe(video: Path) -> dict:
    out = sh(["ffprobe", "-v", "error", "-print_format", "json", "-show_format", "-show_streams",
              str(video)]).stdout
    return json.loads(out)


def font(size: int, bold=False):
    from PIL import ImageFont
    for name in (("Inter:bold" if bold else "Inter"), "DejaVu Sans"):
        try:
            path = sh(["fc-match", "-f", "%{file}", name]).stdout.strip()
            if path:
                return ImageFont.truetype(path, size)
        except Exception:
            pass
    return ImageFont.load_default()


# ----------------------------------------------------------------------------- audio
def loudness(video: Path) -> dict:
    err = sh(["ffmpeg", "-hide_banner", "-nostats", "-i", str(video), "-map", "0:a:0",
              "-af", "ebur128=peak=true", "-f", "null", "-"], check=False).stderr
    s = err[err.rfind("Summary:"):]

    def grab(pat):
        m = re.search(pat, s)
        return float(m.group(1)) if m and m.group(1) not in ("-inf", "inf") else None
    return {"integrated_lufs": grab(r"I:\s+(-?[\d.]+|-inf) LUFS"),
            "lra_lu": grab(r"LRA:\s+(-?[\d.]+) LU"),
            "true_peak_dbtp": grab(r"True peak:\s+Peak:\s+(-?[\d.]+|-inf) dBFS")}


def silences(video: Path, duration: float, noise_db=-45, min_d=0.3) -> list[tuple[float, float]]:
    err = sh(["ffmpeg", "-hide_banner", "-nostats", "-i", str(video), "-map", "0:a:0", "-af",
              f"silencedetect=noise={noise_db}dB:d={min_d}", "-f", "null", "-"], check=False).stderr
    out, start = [], None
    for line in err.splitlines():
        m = re.search(r"silence_start: (-?[\d.]+)", line)
        if m:
            start = max(0.0, float(m.group(1)))
        m = re.search(r"silence_end: ([\d.]+)", line)
        if m and start is not None:
            out.append((start, float(m.group(1))))
            start = None
    if start is not None:
        out.append((start, duration))
    return out


# ----------------------------------------------------------------------------- video
def analyse_frames(video: Path, fps: float, w=320, h=180):
    """Stream low-res gray frames: per-frame changed-pixel counts, mean, std, thumbnails."""
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", str(video), "-vf",
                          f"scale={w}:{h}:flags=area,format=gray", "-f", "rawvideo", "-"],
                         stdout=subprocess.PIPE)
    size = w * h
    changed, still, means, stds, thumbs = [], [], [], [], []
    prev = anchor = None
    while True:
        buf = p.stdout.read(size)
        if len(buf) < size:
            break
        f = np.frombuffer(buf, np.uint8).reshape(h, w).astype(np.int16)
        changed.append(-1 if prev is None else int((np.abs(f - prev) > 6).sum()))
        # "fully static" = identical to the first frame of the current still run (so slow
        # fades that change little per frame still break the run)
        same = anchor is not None and int((np.abs(f - anchor) > 4).sum()) <= 2
        still.append(same)
        if not same:
            anchor = f
        means.append(float(f.mean()))
        stds.append(float(f.std()))
        thumbs.append(f.reshape(h // 2, 2, w // 2, 2).mean(axis=(1, 3)).astype(np.uint8))
        prev = f
    p.wait()
    return np.array(changed), np.array(still), np.array(means), np.array(stds), thumbs


def runs(mask: np.ndarray) -> list[tuple[int, int]]:
    """[start, end] index pairs (inclusive) of True runs."""
    out, s = [], None
    for i, v in enumerate(mask):
        if v and s is None:
            s = i
        elif not v and s is not None:
            out.append((s, i - 1))
            s = None
    if s is not None:
        out.append((s, len(mask) - 1))
    return out


def static_stretches(still, fps, min_s=0.25):
    still = still.copy()
    still[0] = False
    res = []
    for a, b in runs(still):
        f0 = a - 1                                   # frame a equals frame a-1
        dur = (b - f0 + 1) / fps
        if dur >= min_s:
            res.append((f0, b, dur))
    return res


def pick_keyframes(changed, thumbs, fps, stretches, n_frames, cap=40):
    # a frame a little before the end of each still run: eased fades change the first
    # frames of the next animation too little to break the run, so b itself can be blended
    cands = [b - max(2, (b - a) // 4) for (a, b, d) in stretches if d >= 0.3]
    cands.append(n_frames - 1)
    # continuous-motion coverage: add calmest frame in any 8 s window without a candidate
    cands = sorted(set(cands))
    filled = list(cands)
    edges = [0] + cands + [n_frames - 1]
    win = int(8 * fps)
    for lo, hi in zip(edges, edges[1:]):
        for s in range(lo + win // 2, hi - win // 2, win):
            seg = changed[s:s + win]
            if len(seg):
                filled.append(s + int(np.argmin(np.where(seg < 0, 1 << 30, seg))))
    cands = sorted(set(filled))
    sel: list[tuple[int, float]] = []
    for c in cands:
        if not sel:
            sel.append((c, 1e9))
            continue
        d = float((np.abs(thumbs[c].astype(np.int16) - thumbs[sel[-1][0]]) > 12).sum())
        if d < 8:                                   # < 8 of 14400 thumbnail pixels differ
            sel[-1] = (c, sel[-1][1])               # same picture, later = more complete
        else:
            sel.append((c, d))
    if len(sel) > cap:
        keep = {sel[0][0], sel[-1][0]}
        for c, _ in sorted(sel[1:-1], key=lambda x: -x[1])[:cap - 2]:
            keep.add(c)
        sel = [x for x in sel if x[0] in keep]
    return [c for c, _ in sel]


def extract_frames(video: Path, indices: list[int], outdir: Path, fps: float, prefix="kf"):
    outdir.mkdir(parents=True, exist_ok=True)
    for old in outdir.glob(f"{prefix}_*.png"):
        old.unlink()
    if not indices:
        return []
    expr = "+".join(f"eq(n\\,{i})" for i in indices)
    tmp = outdir / "_tmp"
    tmp.mkdir(exist_ok=True)
    sh(["ffmpeg", "-v", "error", "-y", "-i", str(video), "-vf", f"select='{expr}'",
        "-fps_mode", "passthrough", str(tmp / "f_%03d.png")])
    files = sorted(tmp.glob("f_*.png"))
    out = []
    for k, (i, f) in enumerate(zip(indices, files), 1):
        t = i / fps
        name = outdir / f"{prefix}_{k:02d}_{int(t // 60):02d}-{t % 60:04.1f}.png"
        f.rename(name)
        out.append((t, name))
    shutil.rmtree(tmp, ignore_errors=True)
    return out


def contact_sheets(video: Path, outdir: Path, duration: float, words, interval=2.0,
                   cols=3, rows=3, tw=640, th=360, fps: float | None = None, n_frames: int = 0):
    from PIL import Image, ImageDraw
    outdir.mkdir(parents=True, exist_ok=True)
    for old in outdir.glob("sheet_*.png"):
        old.unlink()
    tmp = outdir / "_tmp"
    shutil.rmtree(tmp, ignore_errors=True)
    tmp.mkdir()
    times = [float(t) for t in np.arange(interval / 2, duration, interval)]
    fps = fps or 30.0
    idx = [min(int(round(t * fps)), max(0, n_frames - 1)) for t in times]
    expr = "+".join(f"eq(n\\,{i})" for i in idx)
    sh(["ffmpeg", "-v", "error", "-y", "-i", str(video), "-vf",
        f"select='{expr}',scale={tw}:{th}:flags=lanczos", "-fps_mode", "passthrough",
        str(tmp / "t_%04d.png")])
    tiles = sorted(tmp.glob("t_*.png"))
    times = times[:len(tiles)]
    f_stamp, f_cap, f_head = font(22, bold=True), font(19), font(22, bold=True)
    cap_h, head_h, gap = 52, 44, 8
    per = cols * rows
    sheets = []
    n_sheets = math.ceil(len(tiles) / per)
    for s in range(n_sheets):
        chunk = list(zip(times, tiles))[s * per:(s + 1) * per]
        W = cols * tw + (cols + 1) * gap
        H = head_h + rows * (th + cap_h + gap) + gap
        sheet = Image.new("RGB", (W, H), (32, 34, 40))
        d = ImageDraw.Draw(sheet)
        d.text((gap, 10), f"{video.name}  ·  sheet {s + 1}/{n_sheets}  ·  {fmt_t(chunk[0][0])}"
               f"–{fmt_t(chunk[-1][0])}  ·  one frame every {interval:g}s; text under each frame ="
               f" words spoken within ±{interval / 2:g}s", fill=(220, 220, 220), font=f_head)
        for k, (t, path) in enumerate(chunk):
            r, c = divmod(k, cols)
            x = gap + c * (tw + gap)
            y = head_h + r * (th + cap_h + gap)
            sheet.paste(Image.open(path).convert("RGB"), (x, y))
            label = fmt_t(t)
            bw = d.textlength(label, font=f_stamp) + 16
            d.rectangle([x, y, x + bw, y + 32], fill=(0, 0, 0))
            d.text((x + 8, y + 4), label, fill=(255, 214, 90), font=f_stamp)
            spoken = " ".join(w["word"].strip() for w in words
                              if t - interval / 2 <= w["start"] < t + interval / 2)
            lines = _wrap(d, spoken or "—", f_cap, tw - 8)[:2]
            for li, line in enumerate(lines):
                d.text((x + 4, y + th + 4 + li * 23), line, fill=(200, 200, 200), font=f_cap)
        p = outdir / f"sheet_{s + 1:02d}.png"
        sheet.save(p, optimize=True)
        sheets.append((chunk[0][0], chunk[-1][0], p))
    shutil.rmtree(tmp, ignore_errors=True)
    return sheets


def _wrap(d, text, fnt, width):
    lines, cur = [], ""
    for w in text.split():
        cand = (cur + " " + w).strip()
        if d.textlength(cand, font=fnt) > width and cur:
            lines.append(cur)
            cur = w
        else:
            cur = cand
    if cur:
        lines.append(cur)
    if len(lines) > 2:
        lines = lines[:2]
        lines[1] = lines[1][:-1] + "…"
    return lines


# ----------------------------------------------------------------------------- whisper
def transcribe(video: Path, workdir: Path) -> dict | None:
    audio = workdir / "_audio.flac"
    sh(["ffmpeg", "-v", "error", "-y", "-i", str(video), "-map", "0:a:0", "-ac", "1", "-ar",
        "16000", str(audio)])
    digest = hashlib.sha256(audio.read_bytes()).hexdigest()[:24]
    cache = HOME / "whisper" / f"{digest}.json"
    if cache.exists():
        audio.unlink()
        return json.loads(cache.read_text())
    delay = 2
    for attempt in range(6):
        r = subprocess.run(["curl", "-sS", "-w", "\n%{http_code}", GROQ_URL,
                            "-F", f"model={WHISPER_MODEL}", "-F", f"file=@{audio}",
                            "-F", "response_format=verbose_json", "-F", "language=en",
                            "-F", "temperature=0",
                            "-F", "timestamp_granularities[]=word",
                            "-F", "timestamp_granularities[]=segment"],
                           capture_output=True, text=True)
        body, _, code = r.stdout.rpartition("\n")
        if code == "200":
            data = json.loads(body)
            cache.parent.mkdir(parents=True, exist_ok=True)
            cache.write_text(json.dumps(data))
            audio.unlink()
            return data
        sys.stderr.write(f"review_kit: whisper HTTP {code} (attempt {attempt + 1}): {body[:300]}\n")
        time.sleep(delay)
        delay *= 2
    audio.unlink()
    return None


# ----------------------------------------------------------------------------- text
_ONES = {"²": " squared", "³": " cubed", "%": " percent", "&": " and ", "+": " plus ",
         "=": " equals ", "×": " times ", "≈": " approximately "}


def _num_words(tok: str) -> str:
    from num2words import num2words
    try:
        if re.fullmatch(r"\d+(st|nd|rd|th)", tok):
            return num2words(int(re.sub(r"\D", "", tok)), to="ordinal")
        if re.fullmatch(r"(1[1-9]|20)\d\d", tok):       # years read as years
            return num2words(int(tok), to="year")
        if re.fullmatch(r"\d*\.\d+", tok):
            whole, frac = tok.split(".")
            w = num2words(int(whole)) if whole else ""
            return f"{w} point " + " ".join(num2words(int(c)) for c in frac)
        return num2words(int(tok))
    except Exception:
        return tok


def normalize_words(text: str, drop_and: bool = True) -> list[str]:
    t = text.lower().replace("’", "'")
    t = re.sub(r"\[pause[^\]]*\]", " ", t)
    t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)            # misaki link syntax
    t = re.sub(r"(?<=\d),(?=\d{3})", "", t)
    for k, v in _ONES.items():
        t = t.replace(k, v)
    t = re.sub(r"\d*\.\d+|\d+(st|nd|rd|th)?", lambda m: " " + _num_words(m.group(0)) + " ", t)
    t = re.sub(r"[-–—/]", " ", t)
    t = re.sub(r"[^a-z0-9' ]+", " ", t)
    words = [w.strip("'") for w in t.split()]
    return [w for w in words if w and not (drop_and and w == "and")]  # "and" in numbers varies


def load_narration(path: Path) -> tuple[str, list[dict]]:
    if path.suffix == ".json":
        d = json.loads(path.read_text())
        beats = d.get("beats", [])
        return " ".join(b["text"] for b in beats), d.get("warnings", [])
    text = re.sub(r"^\s*\[\d+:\d+(\.\d+)?\]\s*", "", path.read_text(), flags=re.M)
    return text, []


def diff_narration(script: str, words: list[dict]) -> tuple[float, list[str], int]:
    ref = normalize_words(script)
    hyp, hyp_t = [], []
    for w in words:
        for x in normalize_words(w["word"]):
            hyp.append(x)
            hyp_t.append(w["start"])
    sm = SequenceMatcher(a=ref, b=hyp, autojunk=False)
    errs, lines = 0, []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        errs += max(i2 - i1, j2 - j1)
        t = hyp_t[j1] if j1 < len(hyp_t) else (hyp_t[-1] if hyp_t else 0.0)
        lines.append(f"[{fmt_t(t)}] {op:8s} script: {' '.join(ref[i1:i2]) or '∅'!r:40s} "
                     f"heard: {' '.join(hyp[j1:j2]) or '∅'!r}")
    return errs / max(1, len(ref)), lines, len(ref)


def banned_list() -> list[str]:
    bar = TOOLKIT.parent / "BAR.md"
    if bar.exists():
        txt = bar.read_text()
        m = re.search(r"\*\*Banned phrases\*\*(.*?)\n\n", txt, re.S)
        if m:
            found = re.findall(r'"([^"]+)"', m.group(1))
            if len(found) > 10:
                return found
    return FALLBACK_BANNED


def phrase_regex(p: str) -> str:
    p = p.lower().replace("’", "'")
    parts = [re.escape(x) for x in re.split(r"\bX\b|\bx\b(?=\s|$)", p)] if " x " in f" {p} " else [re.escape(p)]
    body = r"\w+(?:\s+\w+){0,3}?".join(parts)
    body = body.replace("'", "'?")
    return r"(?<![\w-])" + body + r"(?![\w-])"


def scan_slop(text: str, times: list[float] | None = None, words: list[str] | None = None):
    """Return list of (label, match_text, time_or_None)."""
    low = text.lower().replace("’", "'")
    hits = []

    def when(pos):
        if times is None or words is None:
            return None
        n = len(low[:pos].split())
        return times[min(n, len(times) - 1)] if times else None
    for p in banned_list():
        for m in re.finditer(phrase_regex(p), low):
            hits.append((f'banned "{p}"', m.group(0), when(m.start()), True))
    for name, rx, allowed in PATTERNS:
        ms = list(re.finditer(rx, low))
        if len(ms) > allowed:
            for m in ms:
                hits.append((f"pattern {name} (allowed {allowed}x, found {len(ms)}x)", m.group(0),
                             when(m.start()), False))
    # rhetorical question chains: >= 2 consecutive sentences ending in '?'
    sents = re.split(r"(?<=[.!?])\s+", text.strip())
    for i in range(len(sents) - 1):
        if sents[i].endswith("?") and sents[i + 1].endswith("?"):
            pos = low.find(sents[i].lower()[:20])
            hits.append(("pattern rhetorical-question chain", f"{sents[i]} {sents[i + 1]}",
                         when(max(pos, 0)), False))
    return hits


# ----------------------------------------------------------------------------- main
def flag(ok: bool | None) -> str:
    return "—" if ok is None else ("ok" if ok else "**FLAG**")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("video", type=Path)
    ap.add_argument("outdir", type=Path)
    ap.add_argument("--narration", type=Path)
    ap.add_argument("--no-whisper", action="store_true")
    ap.add_argument("--interval", type=float, default=2.0)
    ap.add_argument("--max-keyframes", type=int, default=40)
    a = ap.parse_args(argv)
    video, out = a.video.resolve(), a.outdir.resolve()
    out.mkdir(parents=True, exist_ok=True)
    t_start = time.time()

    info = probe(video)
    vs = next(s for s in info["streams"] if s["codec_type"] == "video")
    aus = [s for s in info["streams"] if s["codec_type"] == "audio"]
    num, den = map(int, vs["r_frame_rate"].split("/"))
    fps = num / den
    duration = float(info["format"]["duration"])
    m: dict = {"file": str(video), "duration_s": round(duration, 3),
               "width": vs["width"], "height": vs["height"], "fps": round(fps, 3),
               "video_codec": vs["codec_name"], "pix_fmt": vs.get("pix_fmt"),
               "audio_codec": aus[0]["codec_name"] if aus else None,
               "audio_rate": int(aus[0]["sample_rate"]) if aus else None,
               "size_mb": round(int(info["format"]["size"]) / 1e6, 2)}
    flags: list[str] = []
    caps: list[str] = []

    # ---- audio
    sil = []
    if aus:
        m.update(loudness(video))
        sil = silences(video, duration)
    lead = sil[0][1] if sil and sil[0][0] <= 0.05 else 0.0
    trail = duration - sil[-1][0] if sil and sil[-1][1] >= duration - 0.05 else 0.0
    internal = [(s, e) for s, e in sil if s > 0.05 and e < duration - 0.05]
    longest_int = max([e - s for s, e in internal], default=0.0)
    m.update({"leading_silence_s": round(lead, 2), "trailing_silence_s": round(trail, 2),
              "longest_internal_silence_s": round(longest_int, 2),
              "silences_over_1_5s": [(round(s, 2), round(e, 2)) for s, e in internal if e - s > 1.5]})

    # ---- frames
    changed, still, means, stds, thumbs = analyse_frames(video, fps)
    nf = len(changed)
    stretches = static_stretches(still, fps)
    longest_static = max([d for _, _, d in stretches], default=0.0)
    long_static = [(round(a / fps, 2), round((b + 1) / fps, 2), round(d, 2))
                   for a, b, d in stretches if d >= 3.0]
    black = runs((means < 20) & (stds < 1.5))
    bg_level = float(np.median(means[stds < 1.5])) if (stds < 1.5).any() else None
    blank = runs(stds < 1.5)
    m.update({"frames": nf, "longest_static_s": round(longest_static, 2),
              "static_stretches_over_3s": long_static,
              "black_frame_runs": [(round(a / fps, 2), round((b + 1) / fps, 2)) for a, b in black],
              "blank_runs_over_0_5s": [(round(a / fps, 2), round((b + 1) / fps, 2))
                                       for a, b in blank if (b - a + 1) / fps > 0.5],
              "background_luma": bg_level})

    # ---- whisper
    words, segments, transcript_text = [], [], ""
    if aus and not a.no_whisper:
        tr = transcribe(video, out)
        if tr:
            (out / "transcript.json").write_text(json.dumps(tr, indent=1))
            words = tr.get("words", [])
            segments = tr.get("segments", [])
            transcript_text = tr.get("text", "").strip()
            (out / "transcript.txt").write_text("\n".join(
                f"[{fmt_t(s['start'])}–{fmt_t(s['end'])}] {s['text'].strip()}" for s in segments) + "\n")
            (out / "transcript_words.tsv").write_text("start\tend\tword\n" + "\n".join(
                f"{w['start']:.2f}\t{w['end']:.2f}\t{w['word'].strip()}" for w in words) + "\n")
        else:
            flags.append("whisper transcription failed (see stderr)")
    if words:
        n_words = sum(len(normalize_words(w["word"], drop_and=False)) or 1 for w in words)
        first, last = words[0]["start"], words[-1]["end"]
        span = max(1e-6, last - first)
        holds = sum(e - s for s, e in internal if s >= first and e <= last and e - s > 1.0)
        speech_s = max(1e-6, span - holds)
        m.update({"transcript_words": n_words, "first_word_s": first, "last_word_s": last,
                  "wpm_speech": round(60 * n_words / speech_s, 1),
                  "wpm_overall": round(60 * n_words / duration, 1),
                  "wpm_excluding_all_pauses": round(60 * n_words / max(
                      1e-6, span - sum(e - s for s, e in internal if s >= first and e <= last)), 1)})

    # ---- narration diff
    narration_path = a.narration or (video.parent / "narration.json"
                                     if (video.parent / "narration.json").exists() else None)
    scene_warnings, diff_lines, script = [], [], ""
    if narration_path and narration_path.exists():
        script, scene_warnings = load_narration(narration_path)
        if words:
            wer, diff_lines, nref = diff_narration(script, words)
            m.update({"narration_file": str(narration_path), "wer": round(wer, 4),
                      "narration_words": nref})
            (out / "narration_diff.txt").write_text(
                f"WER {wer:.1%} over {nref} script words (numbers spelled out, 'and' ignored)\n"
                f"script: {narration_path}\n\n" + ("\n".join(diff_lines) or "no differences") + "\n")

    # ---- slop scan
    word_times = [w["start"] for w in words]
    slop = []
    if transcript_text:
        slop += [("transcript",) + h for h in scan_slop(transcript_text, word_times,
                                                        [w["word"] for w in words])]
    if script:
        slop += [("script",) + h for h in scan_slop(script)]
    banned_hits = [h for h in slop if h[0] == ("transcript" if transcript_text else "script") and h[4]]
    m["banned_phrase_hits"] = len(banned_hits)
    m["slop_hits"] = [{"source": s, "rule": r, "text": t, "t": tt} for s, r, t, tt, _b in slop]

    # ---- flags vs BAR
    def chk(name, ok, msg, cap=None):
        if ok is False:
            flags.append(f"{name}: {msg}")
            if cap:
                caps.append(cap)
        return ok
    st = {}
    st["runtime"] = chk("runtime", RUNTIME[0] <= duration <= RUNTIME[1],
                        f"{fmt_t(duration)} outside 2:30–4:00", "cap 7 (runtime)")
    st["resolution"] = chk("resolution", (vs["width"], vs["height"]) == (1920, 1080) and abs(fps - 30) < 0.01,
                           f"{vs['width']}x{vs['height']}@{fps:g} (expected 1920x1080@30)")
    if "wpm_speech" in m:
        w = m["wpm_speech"]
        st["wpm"] = chk("pace", WPM[0] <= w <= WPM[1], f"{w:.0f} wpm outside 140–165",
                        "cap 7 (pace)" if not (WPM_CAP[0] <= m["wpm_overall"] <= WPM_CAP[1]) else None)
    st["lead"] = chk("leading silence", lead <= MAX_LEADING_SILENCE, f"{lead:.1f}s > 1 s") if aus else None
    st["trail"] = chk("trailing silence", trail <= MAX_TRAILING_SILENCE, f"{trail:.1f}s > 2 s") if aus else None
    st["internal"] = chk("dead air", longest_int <= MAX_INTERNAL_SILENCE,
                         f"{longest_int:.1f}s silence > 2.5 s", "cap 7 (dead air)") if aus else None
    st["static"] = chk("static frame", longest_static <= STATIC_FLAG,
                       f"{longest_static:.1f}s fully static (limit 4 s, cap at 8 s)",
                       "cap 7 (static ≥ 8 s)" if longest_static >= STATIC_CAP else None)
    if aus and m.get("integrated_lufs") is not None:
        i, tp = m["integrated_lufs"], m["true_peak_dbtp"]
        st["lufs"] = chk("loudness", abs(i - LUFS_TARGET) <= LUFS_TOL, f"{i:.1f} LUFS (target -14 ±1)",
                         "cap 7 (loudness)" if abs(i - LUFS_TARGET) > LUFS_CAP_TOL else None)
        st["tp"] = chk("true peak", tp is not None and tp <= TP_MAX, f"{tp} dBTP > -1.5",
                       "cap 7 (true peak)" if tp is not None and tp > TP_CAP else None)
    elif not aus:
        flags.append("no audio stream")
    st["black"] = chk("black frames", not black, f"{len(black)} run(s) of black frames", "cap 5 (black frames)")
    blank_long = [(a, b) for a, b in blank if (b - a + 1) / fps > 1.0 and a > 0]
    st["blank"] = chk("empty frames", not blank_long,
                      f"{len(blank_long)} stretch(es) > 1 s showing only the background")
    if banned_hits:
        n = len(banned_hits)
        chk("banned phrases", False, f"{n} banned phrase(s) in narration",
            "cap 6 (≥2 banned phrases)" if n >= 2 else "cap 8 (1 banned phrase)")
    if "wer" in m:
        st["wer"] = chk("transcript vs script", m["wer"] <= 0.08,
                        f"WER {m['wer']:.0%} — dropped/garbled words or mispronunciations (see diff)")
    if scene_warnings:
        flags.append(f"{len(scene_warnings)} scene warning(s) from NarratedScene (timing/layout)")

    # ---- images
    sheets = contact_sheets(video, out / "sheets", duration, words, a.interval, fps=fps,
                            n_frames=nf)
    kf_idx = pick_keyframes(changed, thumbs, fps, stretches, nf, a.max_keyframes)
    kfs = extract_frames(video, kf_idx, out / "keyframes", fps)
    m["contact_sheets"] = [str(p.relative_to(out)) for _, _, p in sheets]
    m["keyframes"] = [{"t": round(t, 2), "file": str(p.relative_to(out))} for t, p in kfs]
    m["flags"], m["implied_caps"] = flags, caps
    (out / "metrics.json").write_text(json.dumps(m, indent=1, ensure_ascii=False))

    # ---- report
    R = []
    R.append(f"# Review kit — `{video.name}`\n")
    R.append(f"Generated {time.strftime('%Y-%m-%d %H:%M')} by videos/toolkit/review_kit.sh. "
             f"Frames are evidence; numbers are measured, not judged.\n")
    R.append("## Mechanics (BAR §3 caps / §5 standards)\n")
    R.append("| metric | value | bar | status |\n|---|---|---|---|")
    R.append(f"| runtime | {fmt_t(duration)} ({duration:.1f}s) | 2:30–4:00 | {flag(st['runtime'])} |")
    R.append(f"| video | {vs['width']}x{vs['height']} @ {fps:g} fps, {vs['codec_name']}/{vs.get('pix_fmt')}, "
             f"{m['size_mb']} MB | 1920x1080 @ 30 | {flag(st['resolution'])} |")
    if "wpm_speech" in m:
        R.append(f"| pace | {m['wpm_speech']:.0f} wpm (speech time) · {m['wpm_overall']:.0f} overall · "
                 f"{m['wpm_excluding_all_pauses']:.0f} excl. all pauses; {m['transcript_words']} words | "
                 f"140–165 (cap <120/>180) | {flag(st['wpm'])} |")
    if aus:
        R.append(f"| loudness | {m.get('integrated_lufs')} LUFS, LRA {m.get('lra_lu')} LU | −14 ±1 | {flag(st.get('lufs'))} |")
        R.append(f"| true peak | {m.get('true_peak_dbtp')} dBTP | ≤ −1.5 | {flag(st.get('tp'))} |")
        R.append(f"| leading silence | {lead:.2f}s | ≤ 1 s | {flag(st['lead'])} |")
        R.append(f"| trailing silence | {trail:.2f}s | ≤ 2 s | {flag(st['trail'])} |")
        R.append(f"| longest internal silence | {longest_int:.2f}s | ≤ 2.5 s | {flag(st['internal'])} |")
    R.append(f"| longest fully static stretch | {longest_static:.2f}s | ≤ 4 s (cap ≥ 8 s) | {flag(st['static'])} |")
    R.append(f"| black frames | {len(black)} run(s) | none | {flag(st['black'])} |")
    R.append(f"| background-only stretches > 1 s | {len(blank_long)} | none | {flag(st['blank'])} |")
    if "wer" in m:
        R.append(f"| transcript vs script | WER {m['wer']:.1%} ({m['narration_words']} words) | ≲ 8 % | {flag(st['wer'])} |")
    R.append(f"| banned phrases (§4) | {len(banned_hits)} | 0 | {flag(not banned_hits)} |")
    R.append("")
    R.append("## Flags\n")
    R.append("\n".join(f"- {f}" for f in flags) if flags else "- none")
    if caps:
        R.append(f"\nImplied hard caps: {', '.join(sorted(set(caps)))}")
    R.append("")
    if sil:
        R.append("### Silences ≥ 0.3 s\n")
        R.append(", ".join(f"{fmt_t(s)}–{fmt_t(e)} ({e - s:.1f}s)" for s, e in sil) + "\n")
    if long_static:
        R.append("### Static stretches ≥ 3 s\n")
        R.append(", ".join(f"{fmt_t(s)}–{fmt_t(e)} ({d:.1f}s)" for s, e, d in long_static) + "\n")
    if slop:
        R.append("## Slop scan (BAR §4; check context — e.g. statistical 'power' is fine)\n")
        for src, rule, txt, tt, _b in slop:
            R.append(f"- [{src}{' @ ' + fmt_t(tt) if tt is not None else ''}] {rule}: “{txt}”")
        R.append("")
    if scene_warnings:
        R.append("## Scene warnings (NarratedScene timing / layout self-check)\n")
        R.append("\n".join(f"- [{fmt_t(w['t'])}] {w['msg']}" for w in scene_warnings) + "\n")
    R.append("## Contact sheets (one frame every %gs; words spoken ±%gs under each)\n" % (a.interval, a.interval / 2))
    for t0, t1, p in sheets:
        R.append(f"- `{p.relative_to(out)}` — {fmt_t(t0)}–{fmt_t(t1)}")
    R.append("\n## Keyframes (full resolution, frames where the picture settles)\n")
    for t, p in kfs:
        R.append(f"- `{p.relative_to(out)}` — {fmt_t(t)}")
    R.append("")
    if segments:
        R.append(f"## Transcript ({WHISPER_MODEL}, word timings in transcript_words.tsv)\n")
        R.append("```")
        R.extend(f"[{fmt_t(s['start'])}–{fmt_t(s['end'])}] {s['text'].strip()}" for s in segments)
        R.append("```\n")
    if diff_lines or "wer" in m:
        R.append(f"## Narration vs transcript (WER {m.get('wer', 0):.1%})\n")
        R.append("Differences (numbers spelled out, 'and' ignored). A technical term heard wrong "
                 "usually means it was mispronounced:\n")
        R.append("```")
        R.extend(diff_lines[:80] or ["no differences"])
        R.append("```\n")
    R.append(f"_review kit ran in {time.time() - t_start:.0f}s_\n")
    (out / "report.md").write_text("\n".join(R))
    print(f"review_kit: {out / 'report.md'}  ({len(sheets)} sheets, {len(kfs)} keyframes, "
          f"{len(flags)} flags)")
    for f in flags:
        print(f"  FLAG {f}")


if __name__ == "__main__":
    main()
