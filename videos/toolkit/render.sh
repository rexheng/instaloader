#!/usr/bin/env bash
# render.sh — render one Manim scene through the shared, concurrency-limited queue,
# then master it (H.264 CRF 22 + AAC 160k, -14 LUFS / <= -1.5 dBTP).
#
#   videos/toolkit/render.sh [--preview] [--no-cache] <scene_file.py> <SceneClass> <out.mp4>
#
#   --preview   854x480 @15 fps, fast encode — for iterating on timing/layout (~6x faster)
#   --no-cache  disable Manim's partial-movie cache (use if a stale cache is suspected)
#
# Side effects next to <out.mp4>: narration.json / narration.txt (beat timings + warnings),
# <out>.srt subtitles.  Manim media/cache lives in $SAMPLE_SPACE_HOME/renders/<hash>
# (outside git; pruned after 24 h).
# Env: SS_RENDER_SLOTS (default nproc-1), SS_QUEUE_DIR, SAMPLE_SPACE_HOME, SS_MUSIC=<wav>.
set -euo pipefail

TOOLKIT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PREVIEW=0
NOCACHE=0
usage() { sed -n '2,15p' "$0" | sed 's/^# \{0,1\}//'; exit "${1:-2}"; }
while [[ $# -gt 0 && "$1" == --* ]]; do
  case "$1" in
    --preview) PREVIEW=1 ;;
    --no-cache) NOCACHE=1 ;;
    --help) usage 0 ;;
    *) echo "render.sh: unknown option $1" >&2; usage ;;
  esac
  shift
done
[[ $# -eq 3 ]] || usage
SCENE_FILE="$(realpath "$1")"
CLASS="$2"
OUT="$(realpath -m "$3")"
[[ -f "$SCENE_FILE" ]] || { echo "render.sh: no such scene file: $1" >&2; exit 2; }
grep -qE "^class[[:space:]]+${CLASS}\b" "$SCENE_FILE" || {
  echo "render.sh: class $CLASS not found in $SCENE_FILE" >&2; exit 2; }
mkdir -p "$(dirname "$OUT")"

SS_HOME="${SAMPLE_SPACE_HOME:-$HOME/.cache/sample_space}"
QUEUE_DIR="${SS_QUEUE_DIR:-/tmp/sample_space_render_slots}"
NPROC="$(nproc)"
SLOTS="${SS_RENDER_SLOTS:-$(( NPROC > 1 ? NPROC - 1 : 1 ))}"
mkdir -p "$QUEUE_DIR" "$SS_HOME/renders"
chmod 1777 "$QUEUE_DIR" 2>/dev/null || true

T0=$(date +%s.%N)
# ---------------------------------------------------------------- acquire a slot
SLOT=""
announced=0
while [[ -z "$SLOT" ]]; do
  for ((i = 0; i < SLOTS; i++)); do
    exec {FD}>>"$QUEUE_DIR/slot.$i.lock"
    if flock -n "$FD"; then
      SLOT=$i
      echo "pid=$$ scene=$SCENE_FILE:$CLASS since=$(date -Is)" > "$QUEUE_DIR/slot.$i.owner"
      break
    fi
    exec {FD}>&-
  done
  if [[ -z "$SLOT" ]]; then
    if [[ $announced -eq 0 ]]; then
      echo "render.sh: all $SLOTS render slots busy (see $QUEUE_DIR/slot.*.owner); queued…"
      announced=1
    fi
    sleep $(( 2 + RANDOM % 4 ))
  fi
done
T_SLOT=$(date +%s.%N)
echo "render.sh: slot $SLOT/$SLOTS acquired after $(awk "BEGIN{printf \"%.0f\", $T_SLOT - $T0}")s — rendering $CLASS"

# ---------------------------------------------------------------- per-video work dir
QUAL="final"; [[ $PREVIEW -eq 1 ]] && QUAL="preview"
KEY="$(printf '%s:%s:%s' "$SCENE_FILE" "$CLASS" "$QUAL" | sha1sum | cut -c1-16)"
WORK="$SS_HOME/renders/$KEY"
mkdir -p "$WORK"
exec {WFD}>>"$WORK/.lock"
flock "$WFD"                        # same scene rendered twice at once: serialize
touch "$WORK"
find "$SS_HOME/renders" -mindepth 1 -maxdepth 1 -type d -mmin +1440 \
  ! -name "$KEY" -exec rm -rf {} + 2>/dev/null || true
echo "$SCENE_FILE $CLASS $QUAL" > "$WORK/source.txt"
rm -f "$WORK/media/videos"/*/*/"$CLASS".{mp4,wav,srt} 2>/dev/null || true

MANIM_ARGS=(--config_file "$TOOLKIT/manim.cfg" --media_dir "$WORK/media" -o "$CLASS")
if [[ $PREVIEW -eq 1 ]]; then
  MANIM_ARGS+=(-r 854,480 --fps 15)
else
  MANIM_ARGS+=(-r 1920,1080 --fps 30)
fi
[[ $NOCACHE -eq 1 ]] && MANIM_ARGS+=(--disable_caching)

LOG="$WORK/render.log"
cd "$(dirname "$SCENE_FILE")"
set +e
COLUMNS=200 PYTHONPATH="$TOOLKIT${PYTHONPATH:+:$PYTHONPATH}" \
  SS_NARRATION_DIR="$(dirname "$OUT")" \
  manim render "${MANIM_ARGS[@]}" "$SCENE_FILE" "$CLASS" >"$LOG" 2>&1
RC=$?
set -e
T_MANIM=$(date +%s.%N)
grep -E "^\[sample_space\]" "$LOG" | sed 's/^/  /' || true
if [[ $RC -ne 0 ]]; then
  echo "render.sh: manim FAILED (exit $RC). Last lines of $LOG:" >&2
  grep -vE "^\s*$" "$LOG" | tail -n 60 >&2
  exit $RC
fi
RAW="$(find "$WORK/media/videos" -path '*partial_movie_files*' -prune -o -name "$CLASS.mp4" -print | head -n 1)"
[[ -n "$RAW" && -f "$RAW" ]] || { echo "render.sh: manim produced no $CLASS.mp4 (see $LOG)" >&2; exit 1; }
WAV="${RAW%.mp4}.wav"
SRT="${RAW%.mp4}.srt"

# ---------------------------------------------------------------- master
POST_ARGS=(--video "$RAW" --out "$OUT")
[[ -f "$WAV" ]] && POST_ARGS+=(--audio "$WAV")
[[ $PREVIEW -eq 1 ]] && POST_ARGS+=(--preview)
[[ -n "${SS_MUSIC:-}" ]] && POST_ARGS+=(--music "$SS_MUSIC")
PYTHONPATH="$TOOLKIT${PYTHONPATH:+:$PYTHONPATH}" python3 -m sample_space.postprocess "${POST_ARGS[@]}"
[[ -f "$SRT" ]] && cp "$SRT" "${OUT%.mp4}.srt"
T_END=$(date +%s.%N)

DUR="$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT")"
python3 - "$T0" "$T_SLOT" "$T_MANIM" "$T_END" "$DUR" "$OUT" "$QUAL" <<'PY'
import sys
t0, ts, tm, te, dur = map(float, sys.argv[1:6])
out, q = sys.argv[6], sys.argv[7]
work = te - ts
print(f"render.sh: done [{q}] {out}\n"
      f"  video {dur:.1f}s | queue wait {ts - t0:.0f}s | manim {tm - ts:.0f}s | master {te - tm:.0f}s | "
      f"wall {te - t0:.0f}s | {work / max(dur, 1e-6):.2f}s render per video-second")
PY
