#!/usr/bin/env bash
# review_kit.sh <video.mp4> <outdir> [--narration narration.json|txt] [--no-whisper]
#               [--interval 2] [--max-keyframes 40]
# Builds the critic evidence pack (report.md, metrics.json, contact sheets, full-res
# keyframes, whisper transcript, narration diff). See sample_space/review_kit.py.
set -euo pipefail
TOOLKIT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHONPATH="$TOOLKIT${PYTHONPATH:+:$PYTHONPATH}" exec python3 -m sample_space.review_kit "$@"
