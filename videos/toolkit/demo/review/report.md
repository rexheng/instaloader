# Review kit — `demo.mp4`

Generated 2026-10-22 12:00 by videos/toolkit/review_kit.sh. Frames are evidence; numbers are measured, not judged.

## Mechanics (BAR §3 caps / §5 standards)

| metric | value | bar | status |
|---|---|---|---|
| runtime | 0:29.5 (29.5s) | 2:30–4:00 | **FLAG** |
| video | 1920x1080 @ 30 fps, h264/yuv420p, 1.14 MB | 1920x1080 @ 30 | ok |
| pace | 159 wpm (speech time) · 152 overall · 186 excl. all pauses; 75 words | 140–165 (cap <120/>180) | ok |
| loudness | -14.0 LUFS, LRA 2.2 LU | −14 ±1 | ok |
| true peak | -2.1 dBTP | ≤ −1.5 | ok |
| leading silence | 0.00s | ≤ 1 s | ok |
| trailing silence | 1.84s | ≤ 2 s | ok |
| longest internal silence | 0.76s | ≤ 2.5 s | ok |
| longest fully static stretch | 2.67s | ≤ 4 s (cap ≥ 8 s) | ok |
| black frames | 0 run(s) | none | ok |
| background-only stretches > 1 s | 0 | none | ok |
| transcript vs script | WER 0.0% (70 words) | ≲ 8 % | ok |
| banned phrases (§4) | 0 | 0 | ok |

## Flags

- runtime: 0:29.5 outside 2:30–4:00

Implied hard caps: cap 7 (runtime)

### Silences ≥ 0.3 s

0:01.8–0:02.4 (0.6s), 0:05.9–0:06.7 (0.8s), 0:11.1–0:11.5 (0.4s), 0:14.1–0:14.6 (0.6s), 0:18.6–0:19.1 (0.5s), 0:20.4–0:21.1 (0.7s), 0:25.3–0:25.7 (0.4s), 0:27.7–0:29.5 (1.8s)

## Narration craft (PRODUCTION_GUIDE §13: the systemic 9-blockers)

Measured from narration.json (Kokoro's own word timings). Each line names the defect critics docked and the target that scored 9.

- **Budget:** 70 words in 0:29.5. Target ≤ 500 words, 3:15–3:35. 16 of 28 round-5/6 reviews docked Concision for length; 9 of the 10 episodes at ≥ 3:41 were told to cut, none at ≤ 3:37 was.
- **Pace between pauses:** voice speed 0.83; median sentence 184 wpm (episodes 165–178; number-dense sentences run faster), 0 sentence(s) above 200 wpm. 9 of 28 reviews called the delivery hurried; the Audio 9s were at the same 160–164 wpm, with planned pauses and no run-ons.
- **Cadence:** full stops 0.40 s median, beat turns 0.65 s; longest stretch without a ≥ 0.35 s breath 5.8 s at 0:14.7. Audio 9 went to episodes with 0.9–1.4 s after key results and every turn audibly longer than a full stop; flat 0.4 s gaps were called 'metronomic' (use CADENCE = "shaped" and [pause 1.0] after results).
- **Number load:** 9 spoken numbers; busiest 20 s from 0:01.0 has 5 different ones. Critics docked Clarity where 3+ new figures arrived inside ~20 s without a picture for each.
- **Glyph morphs:** 0 Transform(s) between different strings (render as glyph soup; 13 of 28 reviews docked one). Use swap() / carry() / live_number() / TransformMatchingTex.
- **Deictic sync:** 1 deictic words; 0 with no animation starting within −0.8…+0.4 s (Audio 9 required every one to land within ~0.6 s).

## Layout audit (automatic overlap check, BAR §5)

0 issue(s): 0 overlapping/touching, 0 closer than 0.15, 0 outside the safe area, 0 in the caption zone, 0 text(s) under the 24 px cap-height floor; 0 allowed by the producer. 26 frames checked (after every animation and hold).


## Contact sheets (one frame every 2s; words spoken ±1s under each)

- `sheets/sheet_01.png` — 0:01.0–0:17.0
- `sheets/sheet_02.png` — 0:19.0–0:29.0

## Keyframes (full resolution, frames where the picture settles)

- `keyframes/kf_01_00-03.9.png` — 0:03.9
- `keyframes/kf_02_00-07.3.png` — 0:07.3
- `keyframes/kf_03_00-11.1.png` — 0:11.1
- `keyframes/kf_04_00-14.4.png` — 0:14.4
- `keyframes/kf_05_00-18.7.png` — 0:18.7
- `keyframes/kf_06_00-20.8.png` — 0:20.8
- `keyframes/kf_07_00-25.6.png` — 0:25.6
- `keyframes/kf_08_00-27.9.png` — 0:27.9
- `keyframes/kf_09_00-29.5.png` — 0:29.5

## Transcript (whisper-large-v3-turbo, word timings in transcript_words.tsv)

```
[0:00.0–0:02.4] Flip a fair coin 10 times.
[0:02.4–0:06.6] How likely is it that exactly 7 of them land heads?
[0:06.6–0:11.5] 10 flips give 1,024 equally likely sequences.
[0:11.5–0:14.6] 120 of them have 7 heads.
[0:14.6–0:19.6] So the chance is 120 out of 1,024, about 12%.
[0:21.1–0:23.5] Do that count for every number of heads
[0:23.5–0:25.7] and the chances form this hump.
[0:25.7–0:27.8] 7 sits on its right shoulder.
```

## Narration vs transcript (WER 0.0%)

Differences (numbers spelled out, 'and' ignored). A technical term heard wrong usually means it was mispronounced:

```
no differences
```

_review kit ran in 20s_
