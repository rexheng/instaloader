#!/usr/bin/env bash
# setup.sh — idempotent, non-interactive environment setup for Sample Space production.
#
#   videos/toolkit/setup.sh            # full setup (apt + pip + models + smoke test)
#   SS_SKIP_APT=1 videos/toolkit/setup.sh   # skip apt (e.g. no root)
#
# Installs: TeX Live pieces for Manim's MathTex/Tex (+dvisvgm, cm-super), CMU + Inter
# fonts, Pango/Cairo dev libs, espeak-ng (G2P fallback), sox, ffmpeg; Manim CE 0.22 and the
# scientific stack; Kokoro-82M TTS (ONNX, timestamped export) + misaki G2P + spaCy model.
# Models go to $SAMPLE_SPACE_HOME (default ~/.cache/sample_space), never into git.
# Safe to re-run: every step checks before it acts.
set -euo pipefail
export DEBIAN_FRONTEND=noninteractive

TOOLKIT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SS_HOME="${SAMPLE_SPACE_HOME:-$HOME/.cache/sample_space}"
MODEL_DIR="$SS_HOME/models/kokoro"
PY="${PYTHON:-python3}"
SUDO=""
[[ $EUID -ne 0 ]] && command -v sudo >/dev/null && SUDO="sudo -n"
log() { printf '\033[1;34m[setup]\033[0m %s\n' "$*"; }
retry() {   # retry <n> <cmd...>   (2/4/8/16 s backoff)
  local n=$1; shift; local d=2
  for ((i = 1; i <= n; i++)); do
    "$@" && return 0
    ((i < n)) && { log "retry $i/$n in ${d}s: $*"; sleep $d; d=$((d * 2)); }
  done
  return 1
}
T0=$(date +%s)

# ------------------------------------------------------------------ 1. apt packages
PYVER="$($PY -c 'import sys; print(f"{sys.version_info[0]}.{sys.version_info[1]}")')"
APT_PKGS=(
  texlive-latex-base texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended
  texlive-science preview-latex-style dvisvgm cm-super lmodern fonts-lmodern
  fonts-cmu fonts-inter fontconfig
  libpango1.0-dev libcairo2-dev pkg-config
  espeak-ng sox libsox-fmt-all ffmpeg curl ca-certificates
)
if [[ "${SS_SKIP_APT:-0}" != 1 ]]; then
  apt-cache show "python${PYVER}-dev" >/dev/null 2>&1 && APT_PKGS+=("python${PYVER}-dev")
  MISSING=()
  for p in "${APT_PKGS[@]}"; do
    dpkg-query -W -f='${Status}' "$p" 2>/dev/null | grep -q "install ok installed" || MISSING+=("$p")
  done
  if ((${#MISSING[@]})); then
    log "apt: installing ${#MISSING[@]} package(s): ${MISSING[*]}"
    retry 4 $SUDO apt-get update -qq
    retry 3 $SUDO apt-get install -y -q --no-install-recommends "${MISSING[@]}"
  else
    log "apt: all ${#APT_PKGS[@]} packages present"
  fi
fi

# ------------------------------------------------------------------ 2. python packages
PIP=($PY -m pip install -q --disable-pip-version-check --root-user-action=ignore)
$PY -m pip help install 2>/dev/null | grep -q -- "--break-system-packages" && PIP+=(--break-system-packages)
# Debian's bundled setuptools cannot build sdists on 3.13 (install_layout bug): bring a modern one.
if ! $PY -c 'import setuptools,sys; sys.exit(int(setuptools.__version__.split(".")[0]) < 70)' 2>/dev/null; then
  log "pip: upgrading pip/setuptools/wheel"
  retry 3 "${PIP[@]}" --ignore-installed -U pip setuptools wheel
  hash -r
  PIP=($PY -m pip install -q --disable-pip-version-check --root-user-action=ignore --break-system-packages)
fi
PY_PKGS=(
  "manim==0.22.0" "numpy>=2.1" "scipy>=1.14" "pandas>=2.2" "networkx>=3.3" "scikit-learn>=1.5"
  "matplotlib>=3.9" "soundfile>=0.12" "pyloudnorm>=0.1.1" "pillow>=10" "requests" "jinja2"
  "onnxruntime==1.29.0" "num2words==0.5.14" "spacy==3.8.16" "phonemizer-fork==3.3.2"
  "espeakng-loader==0.2.4" "addict" "regex"
)
if $PY - "${PY_PKGS[@]}" <<'PY' 2>/dev/null; then
import sys
from importlib.metadata import version, PackageNotFoundError
from packaging.requirements import Requirement
for spec in sys.argv[1:]:
    r = Requirement(spec)
    try:
        if not r.specifier.contains(version(r.name), prereleases=True):
            sys.exit(1)
    except PackageNotFoundError:
        sys.exit(1)
PY
  log "pip: core packages present"
else
  log "pip: installing ${#PY_PKGS[@]} packages"
  retry 3 "${PIP[@]}" "${PY_PKGS[@]}"
fi
# misaki (Kokoro's G2P) is pure Python but its metadata says <3.13; spaCy 3.8 works fine on 3.13.
if ! $PY -c 'import importlib.metadata as m; assert m.version("misaki") == "0.9.4"' 2>/dev/null; then
  log "pip: installing misaki 0.9.4 (G2P)"
  retry 3 "${PIP[@]}" --no-deps --ignore-requires-python "misaki==0.9.4"
fi
if ! $PY -c 'import spacy.util,sys; sys.exit(0 if spacy.util.is_package("en_core_web_sm") else 1)' 2>/dev/null; then
  log "pip: installing spaCy en_core_web_sm (POS tags for misaki)"
  WD="$(mktemp -d)"
  if retry 2 curl -fsSL -o "$WD/en_core_web_sm-3.8.0-py3-none-any.whl" \
      "https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl"; then
    :
  else
    log "GitHub release blocked; using the Hugging Face mirror (spaCy 3.7.1 model, compatible)"
    retry 3 curl -fsSL -o "$WD/en_core_web_sm-3.7.1-py3-none-any.whl" \
      "https://huggingface.co/spacy/en_core_web_sm/resolve/main/en_core_web_sm-any-py3-none-any.whl"
  fi
  "${PIP[@]}" --no-deps "$WD"/en_core_web_sm-*.whl
  rm -rf "$WD"
fi
# make `import sample_space` work everywhere (render.sh also sets PYTHONPATH itself)
SITE="$($PY -c 'import site; print(site.getsitepackages()[0])')"
if [[ -w "$SITE" ]]; then
  echo "$TOOLKIT" > "$SITE/sample_space_toolkit.pth"
fi

# ------------------------------------------------------------------ 3. Kokoro model
HF="https://huggingface.co/onnx-community/Kokoro-82M-v1.0-ONNX-timestamped/resolve/main"
VOICES=(af_heart af_bella am_michael am_fenrir bf_emma)
mkdir -p "$MODEL_DIR/voices"
fetch() {   # fetch <url> <dest> <expected-bytes|0>
  local url=$1 dest=$2 want=$3
  if [[ -f "$dest" ]] && { [[ $want == 0 ]] || [[ $(stat -c %s "$dest") == "$want" ]]; }; then return 0; fi
  log "download $(basename "$dest")"
  retry 4 curl -fsSL --retry 3 -o "$dest.part" "$url"
  if [[ $want != 0 && $(stat -c %s "$dest.part") != "$want" ]]; then
    echo "size mismatch for $dest" >&2; rm -f "$dest.part"; return 1
  fi
  mv "$dest.part" "$dest"
}
fetch "$HF/onnx/model.onnx" "$MODEL_DIR/model.onnx" 325532171
fetch "$HF/tokenizer.json" "$MODEL_DIR/tokenizer.json" 0
for v in "${VOICES[@]}"; do fetch "$HF/voices/$v.bin" "$MODEL_DIR/voices/$v.bin" 522240; done

# ------------------------------------------------------------------ 4. smoke test
log "smoke test: LaTeX, Pango fonts, TTS"
SMOKE="$(mktemp -d)"
(
  cd "$SMOKE"
  PYTHONPATH="$TOOLKIT" $PY - <<'PY'
import logging
from manim import MathTex, Text, config, logger
logger.setLevel("WARNING")
config.media_dir = "media"
MathTex(r"\hat{\beta} = (X^\top X)^{-1} X^\top y")          # latex + dvisvgm
Text("Sample Space", font="CMU Serif")                        # pango + fonts
import subprocess
fonts = subprocess.run(["fc-list", ":", "family"], capture_output=True, text=True).stdout
assert "CMU Serif" in fonts, "CMU Serif font missing"
from sample_space.voice import synthesize
s = synthesize("Sample Space is ready. The p-value is point oh three.")
assert s.duration > 1.0 and len(s.words) >= 6, s
print(f"[setup] TTS ok: {s.duration:.2f}s, {len(s.words)} timed words -> {s.wav_path}")
PY
)
rm -rf "$SMOKE"
if curl -fsS -m 20 -o /dev/null https://api.groq.com/openai/v1/models 2>/dev/null; then
  log "Groq API reachable (whisper transcription for review_kit.sh)"
else
  log "WARNING: api.groq.com not reachable — review_kit.sh will need --no-whisper"
fi
log "done in $(( $(date +%s) - T0 ))s. Models: $MODEL_DIR"
