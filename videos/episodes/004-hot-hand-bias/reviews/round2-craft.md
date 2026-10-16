# Episode 004: Round 2 review (craft critic: visual design · motion · A/V sync)

**Evidence.** `review/metrics.json` (16:21) is newer than `final.mp4` (16:19), so I used the existing pack in `review/` and did not generate a new one. I read:

- report.md, all 11 contact sheets, the transcript, narration.txt, script.md, facts.md and CHANGELOG.md.
- Full-resolution keyframes at 0:14.4, 0:22.3, 0:33.9, 1:08.7, 1:27.6, 1:37.4, 1:51.4, 1:56.1, 2:21.5, 2:36.7, 2:50.0 and 3:10.8.
- Extra frames I extracted with ffmpeg:
  - single frames at 0:00.3, 0:13.8, 0:55.3, 1:13.6, 1:15.0, 1:43.4, 1:49.0, 1:57.0, 2:26.5, 2:46.5, 3:05.6 and 3:09.6;
  - a 10 fps strip over 1:52.9–1:53.6 (the mirror flip);
  - a 2.5 fps strip over 3:07.0–3:10.8 (the ending).

I re-enumerated all 16 four-flip sequences myself and read the mirror-beat code in scene.py to explain one timing defect. I edited nothing except this file.

```
EPISODE: 004 — "The Hidden Bias That Hid the Hot Hand"
IDEA: Averaging the "share of heads after a heads" row by row gives every sequence one vote no matter how many flips it checked, so a fair coin reads 17/42, not 1/2. The mirror bias after tails doubles the gap, so the 1985 test's random-shooter baseline is −8, not 0, and Cornell's +4 is really +12.
SCORES: Hook 8.5 · Clarity 8 · Visual 8 · Motion 7.5 · Audio 8.5 · Concision 8.5 · Originality 8.5
WEIGHTED: 8.2 (815/100 = 8.15)   AFTER CEILING: 8.2 (lowest 7.5 + 2 = 9.5, so the ceiling does not bind)
CAPS: none
FINAL: 8.2   PASS: no
```

## FACTS

| Claim | Verdict | Source / check |
|---|---|---|
| 4 flips → 16 equally likely sequences | Verified | 2^4 |
| HHTH: checked flips 2, 3 → 1 of 2 heads ("1/2") | Verified | my enumeration |
| HHHT "checks three flips, two of them heads" (2/3) | Verified | enumeration |
| 2 rows (TTTH, TTTT) get no score; 14 are scored | Verified | enumeration |
| Dots: 0×6, ½×4, ⅔×1, 1×3; mean 17/42 = 40.476% ("about 40.5%") | Verified | my enumeration: 17/42 exactly |
| "reads cold by 9.5 points" | Verified | 50 − 40.48 = 9.52 |
| 24 checked flips: 12 H, 12 T ("exactly half") | Verified | Σh = 12, Σn = 24 |
| "12 heads crowd into 8 rows, 12 tails spread across 11" | Verified | my enumeration: 8 and 11 |
| After a tails, the heads share averages 25/42 | Verified | my enumeration: 25/42 over 14 rows |
| 17/42 − 25/42 = "gap of minus 19 points" (worded as a difference of averages) | Verified | −8/42 = −19.05 pts |
| GVT 1985, *Cognitive Psychology*; "a powerful and widely shared cognitive illusion" | Verified | GVT pp. 312–313 via Miller & Sanjurjo 2018 fn. 8 (and round 1) |
| 26 Cornell players, up to 100 shots each; 3 hits vs 3 misses | Verified | M&S 2018 §3.1 / Table 2 |
| Random shooter: 46% after 3 hits, 54% after 3 misses (n = 100) | Verified (consistent) | facts.md exact DP 0.4603 / 0.5397; matches M&S Fig. 1 and the −8 |
| "M&S 2018 put the gap at about minus 8 points" | Verified | M&S 2018 §3.2: "the expected difference (and the strength of the bias) is -8 percentage points" (my web check of the Wharton and Melbourne PDFs) |
| "Longer streaks grow the bias, longer records shrink it" | Verified | M&S abstract |
| Cornell 49% after 3 hits, 45% after 3 misses, +4 | Verified | M&S 2018 §3.1 |
| +4 − (−8) = "+12 points hot" | Verified | M&S 2018: "+12 percentage points higher" |
| M&S 2018 · *Econometrica* | Verified | 86(6):2019–2047 |

No wrong or uncited numbers. GVT's citation is on screen 0:21–0:33 and 2:07–2:55, and M&S's 2:25–2:55.

## MECHANICS

| Metric | Value |
|---|---|
| Runtime | 3:10.8 |
| Pace | 152 wpm (speech time) |
| Longest internal silence | 2.07 s (the planned prediction hold, 0:13.0–0:15.1) |
| Leading / trailing silence | 0.00 s / 1.75 s |
| Longest static stretch | 3.43 s (0:19.7–0:23.2) |
| Loudness | −14.1 LUFS / −2.2 dBTP |
| Black frames | 0 |
| WER | 1.1% (the only name diff is "Sanjorjo's", which is an acceptable rendering of the Spanish) |
| §4 banned phrases | 0 |

No mechanical caps.

## Sync audit (deictics vs visible, ±2 s)

All land except where noted.

| Time | Narration | What is on screen |
|---|---|---|
| 0:04.8 | "Here, one of the two" | rings at 0:05, "1/2" at 0:07 |
| 0:06.9 | "all 16 possible sequences" | ghost miniature at 0:09 |
| 0:10 | "average the shares" | axis at 0:11, "?" at 0:13 |
| 0:15 | "One half feels obvious" | dashed "the obvious guess" at 0:17 |
| 0:19 | "1985" | citation at 0:21 |
| 0:25 | "illusion" | quote at 0:27 |
| 0:27.6 | "Heads are hits" | letters morph at 0:29 |
| 0:43.2 | "This row checks three flips" | HHHT boxed at 0:45 |
| 0:49.4 | "Two rows never…" | TTTH/TTTT boxed at 0:51 |
| 0:54 | "Drop the other 14 scores" | dots fly 0:55–0:57 |
| 0:57–1:02 | "17 out of 42, about 40.5%" | live marker 47.2% → 40.5% |
| 1:05 | "reads cold by 9.5" | red arrow and label 1:06–1:08 |
| 1:11.6 | "Gather all 24" | tiles fly 1:13–1:16 |
| 1:30 / 1:33 | "this row's three heads" / "this lone tails" | HHHH box at 1:31, HTTT box at 1:35 |
| 1:36 / 1:39 | "8 rows" / "11" | outlines at 1:37 / 1:39 |
| 1:40.5 | "Line up the votes" | slide 1:41–1:43, 17/42 at 1:45 |
| 1:48 | "Pool the counts" | Σh/Σn 1:49–1:51 |
| 1:51.5 | "Tails crowd the same way" | flip at 1:53.3. **In sync but only 0.3 s long** (see Motion) |
| 1:56.8 | "25 out of 42" | label 1:57–1:59 |
| 2:01–2:05 | "minus 19" | arrow 2:03, label 2:05 |
| 2:13–2:17 | "after three hits / misses" | lane labels relabel 2:15 / 2:17 |
| 2:20 | "46 and 54" | cursors 2:21–2:23 |
| 2:27 | "minus 8" | gap axis 2:29 |
| 2:36–2:46 | "49%", "45", "plus 4" | values land 2:39, 2:41, 2:45 |
| 2:46.7 | "12 points hot" | brace 2:47–2:49 |
| 3:08.2 | "running hot" | the hot arrow is already drawn at 3:07.4, which is acceptable |

No sync cap. The one sentence with nothing new on screen is 2:30–2:36, "Longer streaks grow the bias and longer records shrink it…". It is not a deictic, so it is not a cap, but it is a clarity and motion gap (see below).

## Dimension notes (evidence)

### Hook 8.5
- The first frame (0:00.3) shows coins mid-flip, with no title.
- One worked example and the commit question "What do you get?" land at 0:12.0–0:13.2, followed by a 2.1 s hold on "?" over the share axis (0:13.8).
- The stakes and the GVT quote arrive by 0:27.
- The landing (2:57–3:09) rebuilds the cold-open frame and moves the reading from 1/2 to the 17/42 baseline. That resolves the opening exactly.
- What holds it under 9:
  - The question lands at 0:12–0:13 rather than inside 0:12.
  - The 0:27–0:43 stretch (hit/miss morph, hot/cold arrows, "test the test") still reads as setup. Tension rises again only at 0:43.

### Clarity 8
- The coin half is close to canonical: one concrete row, all 16 rows, a measured failure (−9.5 points), then pooled 12/24 vs one-vote-per-row 17/42 in the same strip.
- The round-1 hole (−8 asserted from nowhere) is now bridged by the new mirror beat: after-tails reads 25/42, the gap is −19, and it shrinks to −8 for Cornell's design.
- Two weak links remain:
  1. **The mirror is not visible as a mirror.** The flip that should show "after-tails is the after-heads strip with heads and tails swapped, reflected about 50%" plays in about 0.3 s (frames at 10 fps: 1:53.2 shows no lower strip, 1:53.3 is mid-flip, 1:53.5 is complete). The viewer sees a second strip pop in and must take "Tails crowd the same way" on trust. This is the one step that needs a rewatch, and a rewatch does not help because the motion is too fast at any viewing.
  2. **−19 (4 flips, streak 1) to −8 (100 shots, streak 3) is verbal only.** "Longer streaks grow the bias and longer records shrink it" plays over an unchanged gap axis (2:29–2:36, with a 3.1 s fully static stretch at 2:30.8–2:33.9). Two opposing effects are named and neither is shown. The 46/54 positions are likewise asserted, though cited.

### Visual 8
- **Palette.** The semantic palette is held for the whole runtime: yellow for heads/hits, grey for tails/misses, blue for the test and its reading, red for bias, purple for the real Cornell data, and ink for the assumption.
- **Round-1 fixes that worked:**
  - The cold-open composition is now centred (0:14.4, 0:22.3).
  - The hollow rings in the payoff are gone.
  - The axis relabel happens without a cross-fade (2:25–2:29).
- **The vote strip.** 1:37.4 and 1:51.4 are frames I would screenshot to teach from. On the 1:51.4 frame, Σhᵢ/Σnᵢ = 12/24 sits above (1/14)Σhᵢ/nᵢ = 17/42, each beside the strip it measures, with matching colours.
- **Defects:**
  1. **Payoff word load.** At 2:41–2:50 the prose on screen is the header (8 words) + "random shooter" + "bias" + "after 3 hits" + "after 3 misses" + "+12 points" + the two-line axis title (7 words + "percentage points"). That is about 25 prose words, plus two citations. §5 allows ≤ 12. The dim to 30% comes only at 2:51 (on "evidence").
  2. **Bottom-heavy mirror and payoff frames.** The top 43% (y 0–460 px) is empty from 1:53 to 2:05 (1:56.1 keyframe). The band y ≈ 130–460 px is empty from 2:07 to 2:45 (2:21.5, 2:36.7). The lanes, axis and labels are all packed into the lower half.
  3. **Coin overlaps.** In the 4×4 table the blue check rings overlap their neighbours' outlines (1:08.7: in HHHH, coin 2's ring cuts coins 1 and 3), so each row reads as a chain of interlocking circles. This is busy at the small size.
  4. **Small fraction.** The "every flip: ½ heads" caption (0:17–0:25, 0:22.3) uses a stacked ½ whose digits are about 20 px tall, below the 24 px floor.

### Motion 7.5
- **What works.** Objects persist and transform with meaning:
  - the scores fly down and become dots (0:55–0:57);
  - the ringed coins become tiles (1:13–1:16);
  - each row resizes to one vote (1:21–1:25);
  - the yellow segments slide onto the 40.5% marker (1:41–1:43);
  - the blue cursor is carried to the −8 marker (2:27–2:29);
  - the purple values fly into the +4 marker (2:43–2:45).
- **Defects:**
  1. **The mirror flip runs in about 0.3 s (1:53.2 → 1:53.5).** This is far below §5's 0.4 s floor for tracked motion and its 1–2.5 s range for transforms. It is also the one transform whose content *is* the argument (heads ↔ tails, reflected about 50%). Cause in scene.py: `UpdateFromAlphaFunc(lane_T, flip_step)` gets `run_time=beat.until("tails", 2, offset=-0.1)`, which leaves almost no time after the 0.6 s fade and 0.8 s rise.
  2. **Shatter transforms that read as debris.**
     - At 1:49.0, the 14 score fractions break into about 20 glyph fragments that scatter over the table before assembling Σhᵢ/Σnᵢ.
     - At 0:55.3, flying fraction copies sit on top of the neighbouring scores ("0//1", "0/2" doubled).
     - At 1:15.0, coin letters smear into tiles while "12/" is still being written next to tiles in flight.
     - At 1:57.0, the yellow segments blur into "25/42".
     Each lasts about 1 s, but together they are the least 3b1b-like moments in the video.
  3. **Static gap axis at 2:29–2:36** while two quantitative claims are spoken.
  4. **End card.** The end card cross-dissolves over the landing at 3:09.3 while "hot." is still sounding (it ends at 3:09.56). The final image is superimposed rather than held.

### Audio 8.5
- 152 wpm, −14.1 LUFS / −2.2 dBTP.
- Pauses vary by role (0.4–0.9 s between thoughts, 2.07 s prediction hold).
- "Sanjurjo's" is acceptable, and every deictic above lands within about 1.5 s.
- The cadence at 1:29.9–1:40.5 is one dense run ("…gets a whole one. Twelve heads crowd into eight rows. Twelve tails spread across eleven."). It has only 0.5–0.7 s gaps, at the densest visual moment.
- The last word is overlapped by the end-card dissolve.

### Concision 8.5
- 476 words in 3:10. Almost every sentence carries weight.
- Slack:
  - "That's the row average, one vote per row" (1:44.8) restates what the strip just showed.
  - "So look again at your guess" (2:55.6) is a soft pivot.
  - The hot/cold arrow beat (0:29–0:34) mostly repeats the cold open.

### Originality 8.5
- The one-vote-per-row strip and its mirror are a fresh, memorable way to see Miller–Sanjurjo. Most treatments stop at "the expected proportion is below p". No slop, and a specific voice.
- The topic itself is well covered elsewhere, and the payoff visuals (sliders, a brace) are standard.

## FIXES (highest impact first)

1. **[1:51.5–1:54.5][Motion + Clarity] The mirror flip lasts about 0.3 s, so the symmetry argument is invisible.**
   - In scene.py's `mirror` beat, start moving earlier. Overlap the `FadeOut(table…)` (0.6 s) with the tail of "…you get one half" (start it at `beat.wait_until("half")` in the previous beat).
   - Begin the rise on "Tails" (1:51.5).
   - Split the flip into two plays:
     1. `lane_T` copies down to the lower lane, unflipped, in 0.8 s.
     2. The flip about the dashed 50% line runs in 1.4 s with `smooth`. Pulse the dashed line as the mirror axis during it.
   - It must finish by "after a tails" (≈1:54.5). Set an explicit `run_time=1.4` and do not use `beat.until("tails", 2…)`.
   - Expected gain: Clarity +0.5, Motion +0.5.

2. **[2:29–2:36][Clarity + Motion] "Longer streaks grow the bias and longer records shrink it" plays over a static frame.**
   - On "Longer streaks", grow two dim (40%) blue ghost ticks on the gap axis at −1.0 and −3.1, labelled "1 in a row" and "2 in a row" (font 20), with the existing −8 marker labelled "3 in a row". These are the exact n = 100 values for 1- and 2-hit streaks in facts.md row 18 and the one-line DP in check_numbers.py.
   - On "longer records shrink it", slide all three ghosts 30% toward 0 and back (1.2 s). Alternatively, show "4 flips: −19" as an off-axis arrow at the left edge.
   - Fade the ghosts on "Cornell's". This removes the 3.1 s static stretch and makes −19 → −8 visible.

3. **[1:48.5–1:50.0, 0:54.5–0:57.0, 1:13–1:16, 1:56.8–1:58][Motion] Shatter transforms read as debris.**
   - **Σhᵢ/Σnᵢ (1:48.5).** First recolour or `Indicate` the 14 numerators in the table (0.4 s). Then `TransformFromCopy(VGroup(numerators), sum_h)` and `TransformFromCopy(VGroup(denominators), sum_n)` as two grouped moves of 0.9 s each, so each sum receives one group rather than 14 fragmenting fractions.
   - **Scores → dots (0:54.5).** First scale each fraction copy to a dot in place (0.3 s), then move the dots with `lag_ratio=0.06`, so no fraction copy ever sits on a neighbouring score.
   - **Coins → tiles (1:13).** `FadeOut` the H/T letters (0.2 s) before transforming circles into squares. Start `Write("12/24")` only after the last tile lands.
   - **"25/42" (1:57).** Use `TransformFromCopy` of a single merged yellow rectangle, not the 14 segments.

4. **[2:41–2:51][Visual] About 25 prose words on screen against a limit of 12.**
   - At 2:23 (once the lanes are relabelled), dim the header "· 26 players · up to 100 shots each" to 30%, keeping "Cornell, 1985" at full.
   - Shorten the gap-axis title to the single line "hits − misses gap (points)" (MathTex, true minus).
   - Dim the GVT citation to 30% once the M&S citation is on screen.
   - Target ≤ 14 prose words at 2:45.

5. **[1:53–2:05, 2:07–2:45][Visual] Frames are bottom-heavy, with the top 40% empty.**
   - **Mirror (1:53–2:05).** Shift the two lanes, the axis and the right-column labels up by 1.0 unit, so the group centres near y ≈ −0.3.
   - **Payoff (2:07–2:45).** Raise the lanes 0.6 so the header-to-lane gap is no larger than the lane-to-axis gap.
   - Keep the brace (2:47) clear of the header with ≥ 0.3 units between them.

6. **[3:09.3–3:10.8][Motion + Audio] The end card dissolves over the landing while "hot." is still being spoken.**
   - Hold the landing frame, with "→ hot" fully drawn, until 0.6 s after the last word (≈3:10.2).
   - Then fade it out in 0.4 s and show the ident for ≤ 1.0 s with no overlap. Or drop the ident and end on the landing frame.

7. **[0:43–1:51][Visual] The check rings overlap the adjacent coins in the table (1:08.7, 1:37.4).**
   - Shrink the table coins by 8%, or reduce the ring radius so it clears the neighbouring coin outline by ≥ 0.03 units.
   - Each coin should stay a separate shape. The table has about 40 px of spare right margin (1782 px vs the 1824 px safe edge), so a 4% wider pitch also fits.

8. **[0:00–0:13][Hook] The commit question lands at 0:12.0–0:13.2.**
   - Start the 16-sequence ghost miniature during "Here, one of the two is heads" (0:04.8), not on "Do that for all sixteen".
   - Cut the 0.12 s pauses after the first two sentences, so "What do you get?" ends by about 0:11.5 and the hold starts by 0:12.

9. **[1:29.9–1:40.5][Audio] The densest visual stretch is the narration's least punctuated run.**
   - In narration_text.py, raise the gaps after "a whole one." and after "across eleven." to 0.45 s. The box animations already wait on those words.

10. **[0:17–0:25][Visual] The stacked ½ in "every flip: ½ heads" is about 20 px tall.**
    - Use an inline `1/2` MathTex at font_size ≥ 36, with "1" in yellow and "2" in blue to match the cold-open fraction.

## REACHES 9 IF ALL FIXED

Yes, but narrowly, and only if fixes 1–3 are executed cleanly. No structural change is needed. The idea, the failure beat, the one picture (the vote strip) and the landing are all right.

Fixes 1–3 lift Clarity and Motion to 9. Fixes 4–7 lift Visual to 9. Fixes 8–9 lift Hook and Audio to 9. That gives about 8.9–9.0 weighted. With Concision and Originality at 8.5, there is no slack. If the mirror flip and the streak-length visual are only patched (made slower but still unreadable as a reflection), the episode will stall at about 8.6.

## KEEP
- The vote-strip sequence (1:13–1:51): pooled 12/24 above, one-vote-per-row 17/42 below, both read on the same axis, with the formulas beside the strips they measure.
- The continuous carry from the after-3-hits cursor to the −8 "random shooter" marker, with the axis relabelled in place (2:23–2:29), and the purple +12 brace from −8 to +4.
- The landing on the rebuilt cold-open frame, with "→ hot" drawn from the 17/42 baseline past 50% (3:05–3:09).
