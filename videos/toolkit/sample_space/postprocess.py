"""Final mastering for a Manim render (called by render.sh).

    python -m sample_space.postprocess --video raw.mp4 [--audio raw.wav] --out final.mp4
        [--preview] [--music bed.wav --music-db -24]

* audio: 48 kHz stereo, padded/trimmed to the exact video length, gain to -14 LUFS
  integrated with a look-ahead limiter so true peak <= -1.5 dBTP (BAR §5), verified
  on the final AAC and iterated if the encoder overshoots;
* optional music bed (off by default) mixed `--music-db` under the voice and
  side-chain ducked by it;
* video: H.264 (libx264, CRF 22, preset slow, tune animation), yuv420p, +faststart,
  AAC 160 kb/s.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TARGET_LUFS = -14.0
TARGET_TP = -1.5


def run(cmd: list[str], capture: bool = True) -> str:
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if p.returncode != 0:
        sys.stderr.write(p.stderr[-4000:])
        raise SystemExit(f"command failed: {' '.join(cmd[:6])} ...")
    return p.stderr if capture else ""


def probe(path: Path) -> dict:
    out = subprocess.run(["ffprobe", "-v", "error", "-print_format", "json", "-show_format",
                          "-show_streams", str(path)], capture_output=True, text=True, check=True)
    return json.loads(out.stdout)


def measure(path: Path) -> tuple[float, float]:
    """(integrated LUFS, true peak dBTP) via ffmpeg's ebur128 scanner."""
    err = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-map", "0:a:0",
               "-af", "ebur128=peak=true", "-f", "null", "-"])
    summary = err[err.rfind("Summary:"):]
    i = float(re.search(r"I:\s+(-?[\d.]+|-inf) LUFS", summary).group(1))
    tp = re.search(r"True peak:\s+Peak:\s+(-?[\d.]+|-inf) dBFS", summary)
    return i, float(tp.group(1)) if tp else float("nan")


def master_audio(src: Path, duration: float, out_wav: Path, music: Path | None,
                 music_db: float, tmp: Path, limit_db: float) -> None:
    pre = tmp / "pre.wav"
    base = (f"aresample=48000:resampler=soxr,aformat=sample_fmts=fltp:channel_layouts=stereo,"
            f"apad=whole_dur={duration:.3f},atrim=0:{duration:.3f}")
    if music:
        # voice -> [v]; music looped, gain, ducked by voice; then mixed
        fc = (f"[0:a]{base},asplit=2[v][sc];"
              f"[1:a]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,"
              f"aloop=loop=-1:size=2e9,atrim=0:{duration:.3f},volume={music_db}dB,"
              f"afade=t=in:d=1.5,afade=t=out:st={max(0, duration - 2):.3f}:d=2[m];"
              f"[m][sc]sidechaincompress=threshold=0.02:ratio=6:attack=40:release=600[md];"
              f"[v][md]amix=inputs=2:normalize=0[out]")
        run(["ffmpeg", "-y", "-hide_banner", "-i", str(src), "-i", str(music),
             "-filter_complex", fc, "-map", "[out]", "-c:a", "pcm_f32le", str(pre)])
    else:
        run(["ffmpeg", "-y", "-hide_banner", "-i", str(src), "-map", "0:a:0", "-af", base,
             "-c:a", "pcm_f32le", str(pre)])
    lufs, _ = measure(pre)
    if lufs == float("-inf") or lufs < -70:
        shutil.copyfile(pre, out_wav)
        return
    gain = TARGET_LUFS - lufs
    lim = 10 ** (limit_db / 20)
    for _ in range(3):
        run(["ffmpeg", "-y", "-hide_banner", "-i", str(pre), "-af",
             f"volume={gain:.2f}dB,alimiter=limit={lim:.4f}:attack=5:release=60:level=0:latency=1",
             "-c:a", "pcm_f32le", str(out_wav)])
        got, _tp = measure(out_wav)
        if abs(got - TARGET_LUFS) <= 0.3:
            break
        gain += TARGET_LUFS - got


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--video", required=True, type=Path)
    ap.add_argument("--audio", type=Path, help="lossless narration mix (manim's .wav)")
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--preview", action="store_true")
    ap.add_argument("--music", type=Path)
    ap.add_argument("--music-db", type=float, default=-24.0)
    a = ap.parse_args(argv)

    info = probe(a.video)
    vstreams = [s for s in info["streams"] if s["codec_type"] == "video"]
    has_audio = any(s["codec_type"] == "audio" for s in info["streams"])
    duration = float(vstreams[0].get("duration") or info["format"]["duration"])
    a.out.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="ss_post_") as td:
        tmp = Path(td)
        video = tmp / "video.mp4"
        x264 = (["-preset", "veryfast", "-crf", "26"] if a.preview else
                ["-preset", "slow", "-tune", "animation", "-crf", "22"])
        run(["ffmpeg", "-y", "-hide_banner", "-i", str(a.video), "-map", "0:v:0", "-c:v", "libx264",
             *x264, "-pix_fmt", "yuv420p", "-an", str(video)])
        src = a.audio if (a.audio and a.audio.exists()) else (a.video if has_audio else None)
        final_tmp = tmp / "final.mp4"
        if src is None:
            run(["ffmpeg", "-y", "-hide_banner", "-i", str(video), "-c", "copy",
                 "-movflags", "+faststart", str(final_tmp)])
            print("postprocess: no audio track (no narration?)")
        else:
            limit_db = TARGET_TP - 0.6
            for attempt in range(4):
                wav = tmp / "master.wav"
                master_audio(src, duration, wav, a.music, a.music_db, tmp, limit_db)
                run(["ffmpeg", "-y", "-hide_banner", "-i", str(video), "-i", str(wav),
                     "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy", "-c:a", "aac",
                     "-b:a", "160k", "-ar", "48000", "-movflags", "+faststart", str(final_tmp)])
                lufs, tp = measure(final_tmp)
                if tp <= TARGET_TP or lufs < -70:
                    break
                limit_db -= (tp - TARGET_TP) + 0.3       # AAC overshoot: tighten and retry
            print(f"postprocess: audio {lufs:.1f} LUFS integrated, true peak {tp:.1f} dBTP "
                  f"(target {TARGET_LUFS:.0f} LUFS / <= {TARGET_TP} dBTP)")
        shutil.move(str(final_tmp), a.out)
    print(f"postprocess: wrote {a.out} ({duration:.1f}s)")


if __name__ == "__main__":
    main()
