# Episode 4, round 7: substance review (science and story editor)

Evidence: `review/` pack. Its metrics.json (17:38) is newer than final.mp4 (17:36), so I used it as is. I read report.md, all 12 contact sheets, 11 full-resolution keyframes (0:13.5, 0:23.7, 1:00.6, 1:25.9, 1:46.5, 1:57.4, 2:04.8, 2:46.0, 3:11.1, 3:32.7, plus 0:51.9 via the sheet) and 8 frames I extracted myself (1:00.2, 1:00.6, 1:01.0, 1:01.4, 1:51.0, 2:03.0, 2:47.0, 3:21.0). I also read the transcript, the word timings around 1:40–1:56, narration.txt, script.md and facts.md.

I recomputed every number myself:
- Exhaustive enumeration over the 16 four-flip sequences, with exact fractions.
- 400,000 simulated 100-shot records at p = .5 for the k = 3 values.

I checked both citations against the Miller & Sanjurjo text (Wharton PDF, JSTOR excerpt) by web search.

```
EPISODE: 004 — "The Hidden Bias That Hid the Hot Hand"
IDEA: Averaging each short sequence's after-heads share gives every sequence one vote however many flips it checked; checked heads crowd into few sequences and get diluted, so a fair coin reads 17/42, not 1/2. The same bias puts a random shooter at −8 on the 1985 after-3-hits minus after-3-misses test, so Cornell's +4 is about 12 points hot.
SCORES: Hook 9 · Clarity 9 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.8   AFTER CEILING: 8.8 (lowest 8.5 + 2 = 10.5; does not bind)
CAPS: none
FINAL: 8.8   PASS: no
```

Working: 15·9 + 25·9 + 15·8.5 + 15·8.5 + 10·8.5 + 10·8.5 + 10·9 = 875, which gives 8.75 and rounds half-up to 8.8.

I checked every cap and none is triggered:
- Runtime is 3:32.7 and pace is 151 wpm over speech time.
- Loudness is −14.0 LUFS with a −1.9 dBTP true peak.
- The longest silence is 2.17 s, which is the planned prediction hold at 0:12.1–0:14.2.
- The longest static stretch is 3.6 s (3:08.4–3:12.0).
- There are 0 black frames, 0 banned phrases and 0 layout-audit issues.
- I found no typo or broken LaTeX in any frame I read.
- Both empirical sources are on screen whenever their numbers are.
- No number is wrong (see FACTS).

The "co." glyph at 1:01.0 is not a defect. Frames 1:00.6, 1:01.0 and 1:01.4 show the "cold" label being drawn by Write in its final place.

## FACTS

| Claim | Status | Check / source |
|---|---|---|
| 4 flips give 16 equally likely ways | Verified | 2^4 |
| HHTH: flips after a heads are H, T, so "one of the two is heads" = 1/2 | Verified | enumeration |
| HHHT "checks three flips and two are heads" (2/3) | Verified | enumeration |
| Two rows (TTTH, TTTT) get no score; 14 scored | Verified | enumeration |
| Score dots: six at 0, four at 1/2, one at 2/3, three at 1 | Verified | my enumeration gives the same sorted list |
| Average of the 14 scores = 17/42 = 40.48% | Verified | (3 + 2/3 + 2)/14 = 17/42 |
| "Reads cold by 9.5 points" | Verified | 50 − 40.48 = 9.52 |
| 24 checked flips, 12 H, 12 T; total/total = 1/2 | Verified | Σh = 12, Σn = 24 |
| "Twelve heads crowd into eight rows, twelve tails across eleven" | Verified | 8 rows hold a checked H, 11 a checked T |
| HHHH: three heads share one vote; HTTT: lone tails gets a whole one | Verified | n = 3 and n = 1 |
| Heads hold 5⅔ of 14 votes = 17/42; tails 8⅓ | Verified | Σhᵢ/nᵢ = 17/3 |
| (1/14) Σ hᵢ/nᵢ = 17/42 vs Σhᵢ/Σnᵢ = 12/24 | Verified | both evaluated |
| After tails the test reads 25/42 (59.5%), "strip flips over one half" | Verified | 14 rows, mean 25/42; H↔T symmetry |
| Gap 17/42 − 25/42 = "minus nineteen points" | Verified | −8/42 = −19.05 pts |
| GVT 1985, Cognitive Psychology; "a powerful and widely shared cognitive illusion" | Verified | Gilovich, Vallone & Tversky 1985, Cogn. Psych. 17(3):295–314; quote p. 313, as quoted in M&S 2018 §3 (web search, JSTOR excerpt) |
| 26 Cornell players, up to 100 shots, at a distance where they'd hit about half | Verified | M&S 2018 §3.1: "26 players from the Cornell University Mens' (14) and Womens' (12) basketball teams … shot 100 times at a distance from which … he/she would make around 50 percent" (Table 2: three players took fewer, so "up to") |
| Random shooter, n = 100, p = .5: after 3 hits ≈ 46%, after 3 misses ≈ 54% | Verified | my simulation: 46.02% / 53.94%; M&S Fig. 1 |
| "Miller and Sanjurjo's 2018 paper puts the gap at about minus eight points" | Verified | M&S §3.2: "the expected difference … is -8 percentage points"; my simulation −7.92 |
| Longer streaks grow the bias, longer records shrink it | Verified | M&S abstract; ghost ticks −1.0 / −3.1 / −7.9 consistent with my k = 1, 2, 3 runs |
| Cornell: 49% after 3 hits, 45% after 3 misses; study read +4 as no hot hand | Verified | M&S §3.1: ".49 when on a hit streak, versus .45 when on a miss streak … statistically indistinguishable from zero (p = .49)" |
| "Measured from minus eight, it's twelve points hot" | Verified | M&S §3.2: "+4 … is actually +12 percentage points higher than … a Bernoulli i.i.d. shooter" |
| Gym evidence, not proof it survives defenders | Verified (honest limit) | GVT's controlled task removed defensive pressure (M&S §3.1, fn. 22) |
| Miller & Sanjurjo 2018 · Econometrica | Verified | 86(6):2019–2047 |
| Landing: a 50% shooter whose rows average 1/2 is already running hot | Verified | its baseline is 17/42, so 1/2 is above it |

No claim is wrong, unverifiable or uncited.

One precision gap, which is not an error. "The study took that plus four to mean no hot hand" leaves out *why*: GVT's test found +4 not significantly different from zero (p = .49). A viewer could think GVT simply eyeballed +4 as small. See fix 4.

## MECHANICS
runtime 3:32.7 · wpm 151 (speech) · max silence 2.17 s (planned hold) · max static 3.6 s · −14.0 LUFS / −1.9 dBTP · leading 0.00 s / trailing 1.88 s · WER 0.8% (the three diffs are number formatting and "a"/"one")

## Transcript and story notes

**Hook (9).**
- The first frame is the coin row, and by 0:12 the viewer is asked "below, at, or above one half?" while three answers sit on the axis, followed by a 2.2 s hold. That makes the viewer commit to a likely-wrong prediction by 0:12.
- The stakes arrive at 0:18–0:26: the 1985 study and the "cognitive illusion" quote.
- The fail lands at 0:59 ("reads cold, by nine and a half points").
- The ending is HHTH with the formula, and "already running hot" re-reads the opening's "obvious guess". It resolves the opening exactly.
- What keeps it from 10: tension dips in the mirror beat (1:57–2:14). That beat is mechanical, and nothing new is at stake until "1985" at 2:15.

**Slop scan.**
- 0 banned phrases. "It turns out", "let's", rhetorical chains, triplets and fake reveals are all absent.
- 0:10 has one genuine question. "Evidence … not proof …" at 3:10 is a real contrast with content, not the banned "not just X" pattern.
- The four "seventeen out of forty two" repeats (0:57, 1:47, 3:20, plus "twenty five out of forty two" at 2:07) are each a new derivation or the landing callback. They are not filler.

**Clarity (9).**
- A viewer can rebuild 17/42 after one watch by counting votes. The one-vote-per-row strip (kf 1:25.9, 1:46.5) is the canonical picture for this, and the assumption (fair coin, every sequence equally likely) is stated on screen.
- 0:55.1–0:58.9: the narration says "seventeen out of forty two" while the screen shows only 40.5%, and at 0:57.0 the live readout is still at 43.9%. The fraction first appears at 1:47.
- 1:38.7–1:56.0 packs 5⅔, 14, 17/42 and two formulas into 17 s with 0.4–0.6 s gaps. This is the one transition likely to need a rewatch.

**Concision (8.5).**
- 498 words is at the top of the budget. "Score every row the same way." (0:44.6) adds no information, because the cascade shows it.
- 1:57–2:14 states the mirror twice: "reads high, twenty five out of forty two", then "subtract the averages … minus nineteen". This is acceptable, but it is the slack beat.

**Visual (8.5).**
- The palette is held all episode. Yellow means heads or a hit, grey tails or a miss, blue the test, red the bias and purple Cornell.
- 1:13–1:35 (kf 1:25.9) has five groups at full strength: the table, the pooled strip, Σh/Σn = 12/24, "the obvious guess" and the vote strip. There is no single focal point.
- 3:21.0 (extracted frame): during the landing flight the 16 ghost rows overlap one another, the dashed line and the half-faded "1/14 Σ". This is transient, but cluttered.

**Motion (8.5).**
- Objects persist and transform. The vote strip becomes the after-heads lane and is mirrored about 50% (2:03.0), and the percentage axis is relabelled as the difference axis.
- 1:51.0 (extracted): the 14 vote outlines double over the strip while they fly.
- At 2:43–2:46 the relabel from % to points hides a ×10 change of scale. Nothing on screen shows the 46–54 gap becoming the −8 arrow.

**Audio (8.5).**
- The pace and loudness are on target, all 7 deictics land, and whisper reproduces every technical term, including "Sanjurjo".
- The 1:38.7–1:56 run-on noted under Clarity is the main cadence issue.
- The cold open runs 12.1 s without a ≥0.35 s breath, using 0.12 s pauses (0:00–0:12).

**Originality (9).**
- The topic is well covered (NYT Upshot, Numberphile-style explainers), but the "checked heads crowd, so each heads gets a smaller vote" strip is a non-obvious and memorable image.
- The mirror flip about 50% turning −9.5 into −19 is also fresh.

## FIXES (highest impact first)
1. [0:55.1–1:07][Clarity] The narration says "seventeen out of forty two", but only "40.5%" is visible, and it reads 43.9% mid-slide at 0:57.0. When the marker settles (about 0:57.5), write a blue `MathTex(r"=\tfrac{17}{42}", font_size=36)` directly under the 40.5% readout, buff 0.15. Keep it with the readout through 1:07, and let it shorten with the marker at 1:05. The 1:47 "17/42" then reads as a confirmation, not a first sighting.
2. [1:38.7–1:56][Clarity/Audio] The lineup puts three numbers and two formulas into 17 s with 0.4–0.6 s gaps. In narration_text.py:
   - Add [pause 0.8] after "split their votes." and after "Line them up:".
   - Add [pause 1.0] after "That's seventeen out of forty two."
   - Hold 5⅔/14 = 17/42 complete for ≥ 3.2 s before it steps aside.
3. [1:18.4–1:35][Visual] Five groups compete at full strength (kf 1:25.9). On "Each row gets one vote", fade the table (except the row being named), the pooled strip, Σh/Σn = 12/24 and "the obvious guess" to 30%. Bring each back only when named: HHHH at 1:26.7, HTTT at 1:30 and the pooled formula on "ratio of totals" at 1:54.
4. [3:01.5–3:05.2][Clarity] "The study took that plus four to mean no hot hand" omits GVT's actual logic. Replace it with "The study found plus four, too close to zero to count, so no hot hand." (+3 words; fix 6 pays for them). Add a grey `Text("vs 0: p = .49", font_size=20)` under "49 − 45 = +4" for 2.5 s on "too close to zero". The +12 at 3:06 then visibly answers the study's own criterion: the baseline was wrong, not the arithmetic.
5. [2:43.5–2:46][Motion/Clarity] The %-to-points relabel hides a ×10 rescale. First draw a thin red bracket between the 46% and 54% cursors labelled "−8" (0.6 s). Then scale the bracket about the dashed line ×10 (2.0 s, smooth) until its left end sits on −8 of the new axis, cross-fading the tick labels while it scales. The bracket becomes the "bias" arrow.
6. [0:44.6–0:47.0][Concision] Cut "Score every row the same way." and let the scoring cascade run under a [pause 0.8]. This saves about 1.6 s and 5 words.
7. [1:50.5–1:51.5][Motion] The 14 vote outlines double over the strip in flight (frame 1:51.0). Use `lag_ratio=0.08` and leave the strip upward first, or fade each outline to 40% stroke as it lifts.
8. [3:20.0–3:22.0][Visual] The landing ghost rows pile onto one another and onto the dashed line in flight (frame 3:21.0). Fade the dashed line to 25% during the flight, and stagger the 14 rows (`lag_ratio=0.06`) so each lands in the sum before the next leaves.
9. [0:00–0:12][Audio] The cold open runs 12.1 s with 0.12 s pauses. Raise the pause after "check the next flip:" and after "one of the two is heads." to 0.35 s. The question hold stays at 1.6 s.

REACHES 9 IF ALL FIXED: yes. No structural change is needed. Every number and citation checks out, the hook commits the viewer by 0:12, there is a measured failure (−9.5) with a named cause, and the vote-strip insight is the right picture. The remaining deductions are a missing on-screen fraction, one over-dense formula beat, one cluttered stretch, one hidden rescale and the omitted significance logic. Fixes 1–5 move Visual, Motion, Audio and Concision from 8.5 to 9, which gives 9.0.

KEEP:
- The one-vote-per-row strip: the 3/3 slices shrinking against HTTT's whole vote (1:26–1:33), and the heads parts packing to exactly the 40.5% marker (1:43–1:47).
- The mirror: the after-heads strip flipping about the dashed 50% into the after-tails reading (2:01–2:07), which makes the −19 gap visible.
- The landing that answers the cold-open question on its own image (HHTH, 17/42 marker, "its rows average 1/2" → "hot").
