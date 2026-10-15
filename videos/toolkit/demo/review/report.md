# Review kit — `demo.mp4`

Generated 2026-10-15 08:06 by videos/toolkit/review_kit.sh. Frames are evidence; numbers are measured, not judged.

## Mechanics (BAR §3 caps / §5 standards)

| metric | value | bar | status |
|---|---|---|---|
| runtime | 0:32.9 (32.9s) | 2:30–4:00 | **FLAG** |
| video | 1920x1080 @ 30 fps, h264/yuv420p, 1.23 MB | 1920x1080 @ 30 | ok |
| pace | 144 wpm (speech time) · 138 overall · 168 excl. all pauses; 76 words | 140–165 (cap <120/>180) | ok |
| loudness | -14.0 LUFS, LRA 1.8 LU | −14 ±1 | ok |
| true peak | -2.3 dBTP | ≤ −1.5 | ok |
| leading silence | 0.00s | ≤ 1 s | ok |
| trailing silence | 1.73s | ≤ 2 s | ok |
| longest internal silence | 0.51s | ≤ 2.5 s | ok |
| longest fully static stretch | 2.87s | ≤ 4 s (cap ≥ 8 s) | ok |
| black frames | 0 run(s) | none | ok |
| background-only stretches > 1 s | 0 | none | ok |
| transcript vs script | WER 1.4% (70 words) | ≲ 8 % | ok |
| banned phrases (§4) | 0 | 0 | ok |

## Flags

- runtime: 0:32.9 outside 2:30–4:00

Implied hard caps: cap 7 (runtime)

### Silences ≥ 0.3 s

0:02.2–0:02.7 (0.5s), 0:06.7–0:07.1 (0.5s), 0:10.3–0:10.7 (0.4s), 0:12.5–0:13.0 (0.5s), 0:14.0–0:14.3 (0.3s), 0:16.4–0:16.9 (0.5s), 0:21.2–0:21.7 (0.5s), 0:23.1–0:23.6 (0.5s), 0:26.1–0:26.5 (0.4s), 0:28.5–0:29.0 (0.5s), 0:31.2–0:32.9 (1.7s)

## Contact sheets (one frame every 2s; words spoken ±1s under each)

- `sheets/sheet_01.png` — 0:01.0–0:17.0
- `sheets/sheet_02.png` — 0:19.0–0:31.0

## Keyframes (full resolution, frames where the picture settles)

- `keyframes/kf_01_00-04.4.png` — 0:04.4
- `keyframes/kf_02_00-07.9.png` — 0:07.9
- `keyframes/kf_03_00-12.5.png` — 0:12.5
- `keyframes/kf_04_00-16.5.png` — 0:16.5
- `keyframes/kf_05_00-21.3.png` — 0:21.3
- `keyframes/kf_06_00-23.3.png` — 0:23.3
- `keyframes/kf_07_00-27.0.png` — 0:27.0
- `keyframes/kf_08_00-31.2.png` — 0:31.2
- `keyframes/kf_09_00-32.9.png` — 0:32.9

## Transcript (whisper-large-v3-turbo, word timings in transcript_words.tsv)

```
[0:00.0–0:02.7] Flip a fair coin 10 times.
[0:02.7–0:07.1] How likely is it that exactly seven of them land heads?
[0:07.1–0:12.1] 10 flips give 1,024 equally likely sequences.
[0:13.0–0:16.9] 100 and 20 of them have seven heads.
[0:16.9–0:21.9] So the chance is 120 out of 1,024, about 12%.
[0:23.6–0:26.4] Do that count for every number of heads
[0:26.4–0:29.0] and the chances form this hump.
[0:29.0–0:31.3] S7 sits on its right shoulder.
```

## Narration vs transcript (WER 1.4%)

Differences (numbers spelled out, 'and' ignored). A technical term heard wrong usually means it was mispronounced:

```
[0:29.0] insert   script: '∅'                                      heard: 's'
```

_review kit ran in 9s_
