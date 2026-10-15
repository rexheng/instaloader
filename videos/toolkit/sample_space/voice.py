"""Narration voice for Sample Space.

Kokoro-82M (ONNX, "timestamped" export from onnx-community) driven by the misaki
G2P that Kokoro was trained with.  Everything runs locally on CPU.

Public API
----------
    synth(text) -> (wav_path, duration_s)
    synthesize(text) -> Speech      # .wav_path .duration .words .sentences .find()

Features
    * content-hash cache in $SAMPLE_SPACE_HOME/tts (default ~/.cache/sample_space/tts),
      safe for many concurrent processes (per-key file lock + atomic rename);
    * per-sentence synthesis (Kokoro's context is 510 phonemes) with a natural
      pause between sentences; very long sentences are split at clause boundaries;
    * inline pauses:  "... and then [pause] the answer"  or  "[pause 1.2]";
    * pronunciation overrides (PRONUNCIATIONS below, or per call) given either as a
      plain-English respelling ("R squared") or as IPA between slashes ("/kˈAmˌinz/");
    * loudness normalised to -16 LUFS integrated with a -2 dBFS peak ceiling;
    * word-level timestamps from Kokoro's own duration predictor (no ASR needed).

CLI
    python -m sample_space "Some text."                  # synth, print path + words
    python -m sample_space --file script.txt --out a.wav
"""
from __future__ import annotations

import contextlib
import fcntl
import hashlib
import json
import logging
import os
import re
import tempfile
import threading
from dataclasses import asdict, dataclass, field
from pathlib import Path

import numpy as np

log = logging.getLogger("sample_space.voice")

# --------------------------------------------------------------------------- config
SAMPLE_RATE = 24_000
FRAME_SAMPLES = 600                    # one Kokoro duration unit = 600 samples = 25 ms
HOME = Path(os.environ.get("SAMPLE_SPACE_HOME", Path.home() / ".cache" / "sample_space"))
MODEL_DIR = Path(os.environ.get("SS_KOKORO_DIR", HOME / "models" / "kokoro"))
MODEL_FILE = os.environ.get("SS_KOKORO_MODEL", "model.onnx")    # fp32 = best quality
CACHE_DIR = HOME / "tts"

DEFAULT_VOICE = os.environ.get("SS_VOICE", "af_heart")
DEFAULT_SPEED = float(os.environ.get("SS_VOICE_SPEED", "0.78"))   # ~150-162 wpm (BAR 140-165)
TARGET_LUFS = -16.0
PEAK_CEILING_DB = -2.0
SENTENCE_PAUSE = 0.38                  # seconds of silence between sentences
CLAUSE_PAUSE = 0.12                    # between pieces of an over-long sentence
DEFAULT_INLINE_PAUSE = 0.6             # "[pause]" without a number
MAX_PHONEMES = 500                     # Kokoro limit is 510 incl. padding
PIPELINE_VERSION = "ss-tts-1"          # bump to invalidate every cached clip

# Pronunciation overrides: key (matched case-sensitively, as a whole token) ->
# a respelling in plain words, or IPA in misaki's phoneme alphabet between slashes.
# Keys keep their written form for word-timestamp lookup (beat.until("R²") works).
PRONUNCIATIONS: dict[str, str] = {
    "PCA": "P C A",
    "SVD": "S V D",
    "OLS": "O L S",
    "MLE": "M L E",
    "MCMC": "M C M C",
    "ROC": "R O C",
    "AUC": "A U C",
    "GDP": "G D P",
    "i.i.d.": "I I D",
    "iid": "I I D",
    "k-means": "kay means",
    "k-NN": "kay nearest neighbors",
    "kNN": "kay nearest neighbors",
    "t-SNE": "tee snee",
    "UMAP": "you map",
    "R²": "R squared",
    "R^2": "R squared",
    "χ²": "chi squared",
    "p-value": "P value",
    "p-values": "P values",
    "p-hacking": "P hacking",
    "LaTeX": "lah tek",
    "NumPy": "num pie",
    "SciPy": "sigh pie",
    "PyTorch": "pie torch",
    "SQL": "sequel",
    "e.g.": "for example",
    "i.e.": "that is",
    "vs.": "versus",
    "etc.": "et cetera",
    "≈": "approximately",
    "σ": "sigma",
    "μ": "mu",
    "Kokoro": "/kəkˈɔɹO/",
}

_ABBREVIATIONS = {"e.g.", "i.e.", "etc.", "vs.", "dr.", "mr.", "mrs.", "ms.", "prof.",
                  "st.", "fig.", "approx.", "no.", "eq.", "cf.", "al.", "jr.", "sr."}
_PAUSE_RE = re.compile(r"\[pause(?:\s*[:= ]\s*([0-9]*\.?[0-9]+)\s*s?)?\]", re.I)


# --------------------------------------------------------------------------- data
@dataclass
class Word:
    text: str
    start: float
    end: float


@dataclass
class Speech:
    text: str
    wav_path: str
    duration: float
    words: list[Word] = field(default_factory=list)
    sentences: list[dict] = field(default_factory=list)
    voice: str = DEFAULT_VOICE
    speed: float = DEFAULT_SPEED

    def __iter__(self):                       # allows: wav, dur = synthesize(text)
        yield self.wav_path
        yield self.duration

    def find(self, phrase: str, occurrence: int = 1, after: float = -1.0) -> Word | None:
        """Locate a word or phrase (case/punctuation-insensitive). Returns a Word whose
        start/end span the whole phrase, or None.  `occurrence` is 1-based and counts
        only matches that start after `after` seconds."""
        target = [_norm(t) for t in phrase.split() if _norm(t)]
        if not target:
            return None
        normed = [_norm(w.text) for w in self.words]
        seen = 0
        for i in range(len(normed) - len(target) + 1):
            if normed[i:i + len(target)] == target and self.words[i].start > after:
                seen += 1
                if seen == occurrence:
                    return Word(phrase, self.words[i].start, self.words[i + len(target) - 1].end)
        # fallback: prefix match on single words ("flip" matches "flipped")
        if len(target) == 1:
            seen = 0
            for w, n in zip(self.words, normed):
                if n.startswith(target[0]) and w.start > after:
                    seen += 1
                    if seen == occurrence:
                        return Word(phrase, w.start, w.end)
        return None

    def to_json(self) -> dict:
        d = asdict(self)
        d["words"] = [asdict(w) for w in self.words]
        return d


def _norm(s: str) -> str:
    return re.sub(r"[^0-9a-z²³]+", "", s.lower())


# --------------------------------------------------------------------------- engine
class _Engine:
    """Lazily-loaded singleton holding the ONNX session, voices and G2P."""

    _lock = threading.Lock()
    _inst: "_Engine | None" = None

    @classmethod
    def get(cls) -> "_Engine":
        with cls._lock:
            if cls._inst is None:
                cls._inst = cls()
            return cls._inst

    def __init__(self):
        import onnxruntime as ort
        from misaki import en, espeak

        model = MODEL_DIR / MODEL_FILE
        if not model.exists():
            raise FileNotFoundError(
                f"Kokoro model not found at {model}. Run videos/toolkit/setup.sh first.")
        self.vocab = json.loads((MODEL_DIR / "tokenizer.json").read_text())["model"]["vocab"]
        so = ort.SessionOptions()
        so.intra_op_num_threads = int(os.environ.get("SS_TTS_THREADS", "2"))
        so.inter_op_num_threads = 1
        so.log_severity_level = 3
        self.sess = ort.InferenceSession(str(model), so, providers=["CPUExecutionProvider"])
        self.g2p = en.G2P(trf=False, british=False, fallback=espeak.EspeakFallback(british=False))
        self.voices: dict[str, np.ndarray] = {}
        self._respell_cache: dict[str, str] = {}

    def voice(self, name: str) -> np.ndarray:
        if name not in self.voices:
            path = MODEL_DIR / "voices" / f"{name}.bin"
            if not path.exists():
                raise FileNotFoundError(f"voice {name!r} not found in {path.parent}; "
                                        f"setup.sh downloads af_heart and a few others")
            self.voices[name] = np.fromfile(path, dtype=np.float32).reshape(-1, 1, 256)
        return self.voices[name]

    def respell_ipa(self, respelling: str) -> str:
        if respelling.startswith("/") and respelling.endswith("/"):
            return respelling.strip("/")
        if respelling not in self._respell_cache:
            ps, _ = self.g2p(respelling)
            self._respell_cache[respelling] = ps.strip()
        return self._respell_cache[respelling]

    def phonemize(self, sentence: str, overrides: dict[str, str]):
        text = _apply_overrides(sentence, overrides, self.respell_ipa)
        _, tokens = self.g2p(text)
        return tokens

    def infer(self, ids: list[int], voice: str, speed: float):
        ref = self.voice(voice)[min(len(ids) - 1, 509)]
        wav, dur = self.sess.run(None, dict(
            input_ids=np.array([[0, *ids, 0]], dtype=np.int64),
            style=ref.astype(np.float32),
            speed=np.array([speed], dtype=np.float32)))
        frames = np.clip(np.round(dur[0]), 1, None).astype(int)
        return wav[0].astype(np.float32), frames


def _apply_overrides(sentence: str, overrides: dict[str, str], to_ipa) -> str:
    """Rewrite override keys into misaki link syntax:  [R²](/ˈɑɹ skwˈɛɹd/)."""
    if not overrides:
        return sentence
    keys = sorted(overrides, key=len, reverse=True)
    pat = re.compile(r"(?<![\w\[])(" + "|".join(re.escape(k) for k in keys) + r")(?![\w\]])")

    def sub(m):
        ipa = to_ipa(overrides[m.group(1)])
        return f"[{m.group(1)}](/{ipa}/)"
    return pat.sub(sub, sentence)


def _override_signature(sentence: str, overrides: dict[str, str]) -> str:
    """Cheap, G2P-free representation of the overrides that affect a sentence (cache key)."""
    if not overrides:
        return sentence
    return _apply_overrides(sentence, overrides, lambda r: r)


# --------------------------------------------------------------------------- text
def split_segments(text: str) -> list[tuple[str, float]]:
    """Split narration into [(sentence, pause_after_s)], honouring [pause x] markers."""
    text = re.sub(r"\s+", " ", text.strip())
    chunks: list[tuple[str, float]] = []
    pos = 0
    for m in _PAUSE_RE.finditer(text):
        chunks.append((text[pos:m.start()], float(m.group(1)) if m.group(1) else DEFAULT_INLINE_PAUSE))
        pos = m.end()
    chunks.append((text[pos:], 0.0))
    out: list[tuple[str, float]] = []
    for chunk, pause in chunks:
        sents = split_sentences(chunk)
        if not sents:
            if out and pause:
                out[-1] = (out[-1][0], out[-1][1] + pause)
            continue
        out.extend((s, SENTENCE_PAUSE) for s in sents[:-1])
        out.append((sents[-1], pause))
    # a sentence followed by more text but no explicit pause still gets a natural gap
    return [(s, p if p or i == len(out) - 1 else SENTENCE_PAUSE) for i, (s, p) in enumerate(out)]


def split_sentences(text: str) -> list[str]:
    text = text.strip()
    if not text:
        return []
    sents, start = [], 0
    for m in re.finditer(r"[.!?…]+['\")”’\]]*\s+", text):
        before = text[start:m.end()].strip()
        last_word = before.split()[-1].lower() if before.split() else ""
        if last_word in _ABBREVIATIONS or re.fullmatch(r"[a-z]\.", last_word):
            continue
        nxt = text[m.end():m.end() + 1]
        if nxt and nxt.islower():
            continue
        sents.append(before)
        start = m.end()
    tail = text[start:].strip()
    if tail:
        sents.append(tail)
    return sents


# --------------------------------------------------------------------------- audio
def _trim(wav: np.ndarray, thresh_db: float = -42.0, pad_start=0.03, pad_end=0.09):
    """Trim leading/trailing silence. Returns (trimmed, samples_cut_at_start)."""
    win = int(0.01 * SAMPLE_RATE)
    n = len(wav) // win
    if n < 3:
        return wav, 0
    rms = np.sqrt(np.mean(wav[: n * win].reshape(n, win) ** 2, axis=1) + 1e-12)
    loud = np.where(20 * np.log10(rms / (rms.max() + 1e-12)) > thresh_db)[0]
    if len(loud) == 0:
        return wav, 0
    a = max(0, loud[0] * win - int(pad_start * SAMPLE_RATE))
    b = min(len(wav), (loud[-1] + 1) * win + int(pad_end * SAMPLE_RATE))
    return wav[a:b], a


def _limit(x: np.ndarray, ceiling_db: float = PEAK_CEILING_DB, release_ms: float = 80.0) -> np.ndarray:
    """Look-ahead peak limiter (5 ms attack, smooth release); only touches rare peaks."""
    from scipy.ndimage import minimum_filter1d, uniform_filter1d
    ceiling = 10 ** (ceiling_db / 20)
    blk = SAMPLE_RATE // 1000                     # 1 ms blocks
    n = int(np.ceil(len(x) / blk))
    peak = np.pad(np.abs(x), (0, n * blk - len(x))).reshape(n, blk).max(axis=1)
    raw = np.minimum(1.0, ceiling / np.maximum(peak, 1e-9))
    if raw.min() >= 1.0:
        return x
    need = minimum_filter1d(raw, size=11)         # gain is already down 5 ms before a peak
    g = np.empty(n)
    cur, a = 1.0, 1.0 - np.exp(-1.0 / release_ms)
    for i in range(n):                            # ~1e4 iterations per 10 s: cheap
        cur = min(need[i], cur + (1.0 - cur) * a)
        g[i] = cur
    g = uniform_filter1d(g, 5)                    # soften the attack ramp (stays <= raw)
    step = np.repeat(g, blk)[: len(x)]
    smooth = np.interp(np.arange(len(x)), np.arange(n) * blk + blk / 2, g)
    return (x * np.minimum(step, smooth)).astype(np.float32)


def normalize_loudness(x: np.ndarray, target_lufs: float = TARGET_LUFS) -> tuple[np.ndarray, float, float]:
    import pyloudnorm as pyln
    meter = pyln.Meter(SAMPLE_RATE)
    padded = x if len(x) > SAMPLE_RATE else np.pad(x, (0, SAMPLE_RATE - len(x)))
    lufs = float(meter.integrated_loudness(padded))
    if not np.isfinite(lufs):
        return x, lufs, 0.0
    gain_db = target_lufs - lufs
    y = x * (10 ** (gain_db / 20))
    return _limit(y), lufs, gain_db


# --------------------------------------------------------------------------- synth
def _word_times(tokens, vocab, frames: np.ndarray) -> tuple[list[int], list[Word]]:
    """Build model input ids and word timings (Kokoro's join_timestamps logic)."""
    ids: list[int] = []
    spans = []                               # (token, first_idx, n_ids, has_space)
    for t in tokens:
        ps = t.phonemes or ""
        tid = [vocab[c] for c in ps if c in vocab]
        first = len(ids)
        ids.extend(tid)
        space = bool(t.whitespace)
        if space:
            ids.append(vocab[" "])
        spans.append((t, first, len(tid), space))
    words: list[Word] = []
    if len(frames) < 3:
        return ids, words
    right = 2 * max(0, int(frames[0]) - 3)   # half-frames
    for t, first, n, space in spans:
        i = first + 1                        # +1 for the BOS pad in `frames`
        j = i + n
        if j > len(frames) - 1:
            break
        tok = int(frames[i:j].sum())
        sp = int(frames[j]) if space and j < len(frames) - 1 else 0
        left = right + 2 * tok + sp
        if n and re.search(r"\w", t.text):
            words.append(Word(t.text, right / 80.0, left / 80.0))
        right = left + sp
    return ids, words


def _split_long(engine: _Engine, sentence: str, overrides) -> list[str]:
    """Split a sentence whose phoneme string exceeds the model context."""
    tokens = engine.phonemize(sentence, overrides)
    n = sum(len(t.phonemes or "") + bool(t.whitespace) for t in tokens)
    if n <= MAX_PHONEMES:
        return [sentence]
    parts = re.split(r"(?<=[,;:—–])\s+", sentence)
    if len(parts) == 1:
        words = sentence.split()
        mid = len(words) // 2
        parts = [" ".join(words[:mid]), " ".join(words[mid:])]
    pieces, cur = [], ""
    for p in parts:
        cand = f"{cur} {p}".strip()
        if cur and len(cand) > len(sentence) / max(2, round(n / MAX_PHONEMES + 0.5)) * 1.1:
            pieces.append(cur)
            cur = p
        else:
            cur = cand
    if cur:
        pieces.append(cur)
    out = []
    for p in pieces:
        out.extend(_split_long(engine, p, overrides) if p != sentence else [p])
    return out


def _cache_key(segments, voice, speed, overrides) -> str:
    payload = json.dumps({
        "v": PIPELINE_VERSION, "model": MODEL_FILE, "voice": voice, "speed": round(speed, 4),
        "lufs": TARGET_LUFS, "segs": [(_override_signature(s, overrides), round(p, 3)) for s, p in segments],
    }, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(payload.encode()).hexdigest()[:24]


@contextlib.contextmanager
def _file_lock(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as fh:
        fcntl.flock(fh, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(fh, fcntl.LOCK_UN)


def synthesize(text: str, voice: str | None = None, speed: float | None = None,
               overrides: dict[str, str] | None = None, cache: bool = True) -> Speech:
    """Synthesize narration text -> Speech (cached).  See module docstring."""
    voice = voice or DEFAULT_VOICE
    speed = float(speed or DEFAULT_SPEED)
    ov = dict(PRONUNCIATIONS)
    if overrides:
        ov.update(overrides)
    segments = split_segments(text)
    if not segments:
        raise ValueError("empty narration text")
    key = _cache_key(segments, voice, speed, ov)
    wav_path = CACHE_DIR / key[:2] / f"{key}.wav"
    meta_path = wav_path.with_suffix(".json")

    def load():
        m = json.loads(meta_path.read_text())
        return Speech(text=m["text"], wav_path=str(wav_path), duration=m["duration"],
                      words=[Word(**w) for w in m["words"]], sentences=m["sentences"],
                      voice=m["voice"], speed=m["speed"])

    if cache and wav_path.exists() and meta_path.exists():
        return load()
    with _file_lock(wav_path.with_suffix(".lock")):
        if cache and wav_path.exists() and meta_path.exists():
            return load()
        speech = _render(text, segments, voice, speed, ov, wav_path)
        tmp = meta_path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(speech.to_json(), ensure_ascii=False, indent=1))
        os.replace(tmp, meta_path)
        return speech


def _render(text, segments, voice, speed, ov, wav_path: Path) -> Speech:
    import soundfile as sf
    eng = _Engine.get()
    pieces: list[np.ndarray] = []
    words: list[Word] = []
    sentences = []
    t = 0.0
    for sent, pause in segments:
        subs = _split_long(eng, sent, ov)
        for k, sub in enumerate(subs):
            tokens = eng.phonemize(sub, ov)
            ids, wtimes = _word_times(tokens, eng.vocab, np.zeros(0))
            if not ids:
                continue
            audio, frames = eng.infer(ids, voice, speed)
            _, wtimes = _word_times(tokens, eng.vocab, frames)
            audio, cut = _trim(audio)
            off = t - cut / SAMPLE_RATE
            dur = len(audio) / SAMPLE_RATE
            for w in wtimes:
                words.append(Word(w.text, round(max(t, w.start + off), 3),
                                  round(min(t + dur, max(w.end + off, w.start + off)), 3)))
            sentences.append({"text": sub, "start": round(t, 3), "end": round(t + dur, 3)})
            pieces.append(audio)
            t += dur
            gap = pause if k == len(subs) - 1 else CLAUSE_PAUSE
            if gap > 0:
                pieces.append(np.zeros(int(gap * SAMPLE_RATE), dtype=np.float32))
                t += gap
    audio = np.concatenate(pieces) if pieces else np.zeros(SAMPLE_RATE // 2, dtype=np.float32)
    audio, lufs_in, gain = normalize_loudness(audio)
    wav_path.parent.mkdir(parents=True, exist_ok=True)
    tmp = wav_path.with_name(wav_path.stem + ".tmp.wav")
    sf.write(tmp, np.clip(audio, -1, 1), SAMPLE_RATE, subtype="PCM_16")
    os.replace(tmp, wav_path)
    log.info("tts %s: %.2fs, in %.1f LUFS, gain %+.1f dB", wav_path.name, len(audio) / SAMPLE_RATE, lufs_in, gain)
    return Speech(text=text, wav_path=str(wav_path), duration=round(len(audio) / SAMPLE_RATE, 3),
                  words=words, sentences=sentences, voice=voice, speed=speed)


def synth(text: str, **kw) -> tuple[str, float]:
    """synth(text) -> (wav_path, duration_s).  kwargs: voice, speed, overrides."""
    s = synthesize(text, **kw)
    return s.wav_path, s.duration


def estimate_duration(text: str, wpm: float = 160.0) -> float:
    """Rough planning estimate without running TTS (af_heart @0.78 speaks ~160 wpm)."""
    n = len(re.findall(r"[\w'’-]+", _PAUSE_RE.sub("", text)))
    pauses = sum(float(m.group(1) or DEFAULT_INLINE_PAUSE) for m in _PAUSE_RE.finditer(text))
    return n / wpm * 60 + pauses + SENTENCE_PAUSE * max(0, len(split_sentences(text)) - 1)


# --------------------------------------------------------------------------- CLI
def _main(argv=None):
    import argparse
    import shutil
    ap = argparse.ArgumentParser(description="Synthesize Sample Space narration (Kokoro).")
    ap.add_argument("text", nargs="?", help="text to speak")
    ap.add_argument("--file", help="read text from a file instead")
    ap.add_argument("--out", help="copy the resulting wav here")
    ap.add_argument("--voice", default=None)
    ap.add_argument("--speed", type=float, default=None)
    ap.add_argument("--json", action="store_true", help="print full JSON (words, sentences)")
    a = ap.parse_args(argv)
    text = Path(a.file).read_text() if a.file else a.text
    if not text:
        ap.error("give text or --file")
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    s = synthesize(text, voice=a.voice, speed=a.speed)
    if a.out:
        shutil.copyfile(s.wav_path, a.out)
    if a.json:
        print(json.dumps(s.to_json(), ensure_ascii=False, indent=1))
    else:
        print(f"{s.wav_path}\t{s.duration:.2f}s")
        print(" ".join(f"{w.text}@{w.start:.2f}" for w in s.words))


if __name__ == "__main__":
    _main()
