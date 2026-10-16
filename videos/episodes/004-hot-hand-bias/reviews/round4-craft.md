# Episode 004, round 4 review (craft critic: visual design, motion, A/V sync)

## Evidence used

`review/metrics.json` (00:31) is newer than `final.mp4` (00:29), so I used the existing pack in `review/`.

What I read:
- BAR.md in full.
- report.md, all 11 contact sheets, and the transcript with word timings (transcript_words.tsv).
- script.md, narration.txt, facts.md, CHANGELOG.md, and the round-3 craft review.
- 15 full-resolution keyframes: 0:12.9, 0:21.0, 0:45.2, 1:03.7, 1:16.8, 1:38.7, 1:48.2, 1:49.9, 1:56.1, 2:13.8, 2:25.7, 2:39.3, 2:42.3, 2:55.3, 3:15.1.

Frames I extracted myself into /tmp/ep4r4:
- Single frames at 0:38.5, 0:39.5, 1:31.6, 1:32.2, 1:32.8, 1:44.5, 1:45.5, 1:46.3, 1:47.0, 1:47.6, 1:50.4, 1:51.0, 2:30.0, 2:31.0, 2:32.0, 2:34.3, 2:35.0, 2:36.0, 2:37.6, 2:38.4, 2:40.4, 2:47.8, 2:48.4, 3:00.6, 3:01.6, 3:02.4, 3:12.6, 3:13.4 and 3:14.0.
- Crops of the equation region at 1:47.2, 1:47.8, 1:48.6, 1:49.2, 1:49.6 and 1:50.2.

Other checks:
- I re-enumerated all 16 sequences myself. Results: 14 scored, mean 17/42; 12 H out of 24 checked; 8 rows contain a checked H and 11 a checked T; after-tails mean 25/42; gap −19.05 pts.
- An exact dynamic program for n = 100, k = 3 gives E[P̂(hit | 3 hits)] = 0.4603, which matches the 46% / 54% on screen.
- I measured text contrast from pixels in the keyframes.

I edited nothing except this file.

```
EPISODE: 004 — "The Hidden Bias That Hid the Hot Hand"
IDEA: Averaging "share of heads after a heads" row by row gives every sequence one vote however many flips it checked, so heads-after-heads (which crowd into few rows) are under-weighted and a fair coin reads 17/42; the mirror bias after tails makes a random shooter's after-hits − after-misses gap −8 for GVT's design, so Cornell's +4 is really +12.
SCORES: Hook 9 · Clarity 9 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.8 (875/100 = 8.75)   AFTER CEILING: 8.8 (lowest 8.5 + 2 = 10.5, does not bind)
CAPS: none
FINAL: 8.8   PASS: no
```

## Summary

Round 4 fixed every round-3 craft item I can check:
- The 40.5% marker is now shortened to the vote lane. At 1:16.8 its top stops below the "the obvious guess" label, and the pooled 12/24 strip reads only against the dashed 50% line.
- The streak flags are decoded by a "hits in a row" legend (2:35), and each flag rides its own tick.
- Blue "random" and purple "Cornell" column heads now label 46/54 and 49/45 (2:23, 2:42.3).
- The landing line is re-worded and paced: "A fifty percent shooter… who averages one half on this test… is already running hot."

The episode is now close. Every deictic lands, and the central picture (1:21–1:43) is teach-from-it quality. The remaining gap to 9 is concentrated in three places:
1. **The formula coda (1:44.5–1:50.1).** Two equations are born within 3.3 s and the pooled one is gone 2.3 s after it completes, which breaks two §5 equation rules. The frame at 1:48.2 is also the most cluttered in the episode.
2. **Grey text contrast.** Axis titles, ticks and citations measure 6.2–6.4 : 1, below §5's 7 : 1.
3. **Cold-open pace.** The densest instruction in the episode runs at 180 wpm.

All of these are fixable without structural change.

## FACTS

| Claim | Verdict | Source / check |
|---|---|---|
| 4 flips → 16 equally likely sequences | Verified | 2^4 |
| HHTH: checked flips 2 and 3, "one of the two is heads" | Verified | my enumeration |
| HHHT "checks three flips, and two of them are heads" | Verified | enumeration |
| TTTH and TTTT unscored; 14 scored; dots 0×6, ½×4, ⅔×1, 1×3 | Verified | enumeration; matches the dot plot at 1:03.7 |
| Mean 17/42 ≈ 40.5%; "reads cold by nine and a half points" | Verified | 17/42 = 0.4048; 50 − 40.48 = 9.52 |
| 24 checked flips: 12 H / 12 T, "exactly half" | Verified | Σh = 12, Σn = 24 |
| "Twelve heads crowd into eight rows; twelve tails spread across eleven" | Verified | enumeration: 8 and 11 |
| After tails 25/42 (mirror about ½); heads part ends at 59.5% | Verified | enumeration; geometry at 1:56.1 / 2:01 |
| Gap 17/42 − 25/42 = "minus nineteen points" | Verified | −8/42 = −19.05 pts |
| GVT 1985, *Cognitive Psychology*; "a powerful and widely shared cognitive illusion" | Verified | GVT pp. 312–313 as quoted in Miller & Sanjurjo 2018 fn. 8 (verified in rounds 1–3) |
| 26 Cornell players, up to 100 shots, from about 50%; 3 hits vs 3 misses | Verified | M&S 2018 §3.1, Table 2 |
| Random shooter 46% / 54% | Verified | my exact DP: 0.4603 / 0.5397 |
| M&S "puts the gap at about minus eight points" | Verified | M&S 2018 §3.2 ("expected difference … is −8 percentage points") |
| Longer streaks grow the bias, longer records shrink it (ghosts at −1.0, −3.1, −7.9; the 3-hit ghost at −0.7 for 1,000 shots) | Verified | M&S abstract; facts.md row 18 DP; positions at 2:37.6 / 2:39.3 match |
| Cornell 49% / 45%, +4; "twelve points hot" | Verified | M&S 2018 §3.1–3.2 ("+12 percentage points higher") |
| "Evidence for a hot hand in a gym, not proof it survives defenders" | Verified | M&S §3.1 (the design removed defensive pressure) and fn. 22 |
| M&S 2018 · *Econometrica* | Verified | 86(6):2019–2047 |

There are no wrong, fabricated or uncited claims. GVT is cited on screen 0:19–0:33 and 2:09–2:59; M&S is cited 2:24–2:59.

## MECHANICS

```
MECHANICS: runtime 3:15.1 · wpm 154 (speech time; 486 words) · max silence 2.07 s (planned prediction hold 0:11.7–0:13.8) · max static 3.87 s (same hold) · −14.0 LUFS / −2.1 dBTP
```

- Leading silence is 0.00 s and trailing silence 0.89 s.
- There are 0 black frames and 0 layout-audit issues.
- WER is 0.6%. The differences are a/one ×2 and "Sanjorjo's".
- The §4 phrase and pattern scan found nothing; there is one question in the whole narration.
- The second static stretch, 0:18.5–0:21.9, lasts 3.4 s.
- Per-10-s pace is 108–168 wpm everywhere except **0:00–0:10, which runs at 180 wpm** (30 words).
- No mechanical caps are triggered.

## Sync audit (deictic → visible, ±2 s; word times from transcript_words.tsv)

| Spoken | On screen | OK |
|---|---|---|
| "here, one of the two" 0:04.6 | rings at 0:05, 1/2 at 0:07 | yes |
| "all sixteen sequences" ~0:08 | compact 16-row ghost at 0:09 | yes |
| "What do you get?" 0:10.3–0:11.7 | "?" on the axis at 0:11; hold to 0:13.8 | yes |
| "In 1985" 0:17.1 | GVT citation at 0:19 | yes |
| "illusion" ~0:25.5 | quote at 0:25 | yes |
| "Heads are hits" 0:26.3 | hit/miss morph 0:27; axis title swaps to "shots/hits" | yes |
| "This row checks three flips" 0:41.8 | HHHT boxed by 0:43 | yes |
| "Two rows never…" 0:48.0 | TTTH/TTTT boxed at 0:49 | yes |
| "17 out of 42 … 40.5%" 0:56.9–1:00.9 | marker reads 49.1% at 0:57, settles at 40.5% by 0:59 | yes |
| "reads cold / nine" 1:04.3 / 1:05.3 | red arrow and "cold" at 1:05; "−9.5 points" at 1:07 | yes |
| "Gather all 24" ~1:10 | tiles fly 1:11; 12 at 1:13; 12/24 at 1:15 | yes |
| "This row's three heads" 1:28.3 | HHHH boxed at 1:29 | yes |
| "this lone tails" 1:31.5 | HTTT box drawing at 1:31.6, closed at 1:32.2 | yes |
| "eight rows" 1:35.2 / "eleven" 1:38.0 | yellow outlines at 1:35 / white outlines 1:37–1:39 | yes |
| "seventeen out of forty two" 1:41.4 | yellow lands on 40.5% at 1:41; 17/42 at 1:43 | yes |
| "Swap heads and tails" 1:51.7 | copy drops and recolours 1:52–1:53.5 | yes |
| "the strip flips over one half" 1:54.2–1:55.9 | half turn mid-way at 1:55 | yes |
| "twenty five" 1:59.3 | 25/42 at 2:01 | yes |
| "minus nineteen" 2:05.3 | red arrow at 2:05; "−19 points" at 2:07 | yes |
| "For a random shooter" 2:21.9 | blue "random" head at 2:23 | yes |
| "minus eight" 2:31.7 | relabel 2:31–2:33; "−8" at 2:33 | yes |
| "Longer streaks" 2:34.3 / "records" 2:37.2 / "isn't" 2:39.9 | ghosts out 2:34–2:35 / 1,000-shot ghost 2:37.6–2:39.3 / back 2:40.4 | yes |
| "plus 4" 2:49.0 | +4 marker at 2:49–2:51 | yes |
| "twelve points hot" ~2:52.5 | brace and "+12 points" at 2:53 | yes |
| "defenders" ~2:58.5 | "no defenders" tag at 2:57–2:59 | yes |
| "Seventeen out of forty two" ~3:04.5 | ghost rows at 3:05; 17/42 at 3:07 | yes |
| "running hot" 3:13–3:14.2 | dot at 3:12.6; arrow and "hot" by 3:13.4; held to 3:15.1 | yes |

Every deictic lands. The sync cap is not triggered.

## Dimension notes (evidence)

### Hook 9
- **0:00.** The first frame is four coins mid-flip. There is no title card.
- **0:10.3–0:11.7.** The question "What do you get?" is held for a 2.07 s prediction pause over a "?" on the axis (0:12.9). The viewer commits to ½ by 0:12, and that is exactly the likely-wrong answer the episode breaks.
- **0:17–0:26.** The GVT stakes arrive with an on-screen citation and the "cognitive illusion" quote.
- **3:02–3:15.** The landing rebuilds the cold-open frame, collapses the 16 rows onto 17/42 and draws "hot" to 50%. It resolves the opening exactly.
- **Nit.** The rule is delivered at 180 wpm (see Audio). The 0:26–0:37 hit/miss round trip is the one place the tension rests.

### Clarity 9
- **What works:**
  - one row, then 16 rows;
  - a measured failure (the live marker goes 50% → 40.5%, then "cold −9.5 points");
  - pooled 12/24 shown against one-vote 17/42 on the same axis;
  - the crowding made literal: HHHH's three heads squeezed into one vote at 1:29, HTTT's lone tails stretched to a whole vote at 1:32, outlines on 8 vs 11 rows;
  - a visible mirror (copy, recolour, half turn about 50%).
- **Round-3 confusions now gone:**
  - The marker no longer crosses the pooled strip (1:16.8, 1:38.7).
  - 46/54 are labelled "random" from the moment they appear (2:23).
  - The dot code is decoded by "hits in a row" (2:35).
- **Remaining (not enough to drop below 9):**
  - The mirror (1:50–1:56) leans on one sentence, "Tails crowd the same way", for its symmetry argument. It is correct and visible, but it is the step most viewers will replay.
  - The formula coda is too brief to read (see Motion). Clarity survives only because the 12/24 vs 17/42 strips already made the point.

### Visual 8.5
- **What works:**
  - The palette holds for the whole runtime: yellow = heads/hits, grey = tails/misses, blue = the test's reading, red = bias, purple = Cornell data, ink = assumption.
  - Type sizes pass. Ticks have about 30 px cap height and citations about 28 px (0:21.0).
  - The safe area is respected. The right column's "Cornell" ends at x ≈ 1797 px, inside the 1824 px limit (2:42.3).
  - 1:38.7 (vote strip with boxed rows), 2:55.3 (purple +12 brace over −8 → +4) and 3:15.1 (17/42 → hot) are frames people would screenshot.
- **Defects:**
  1. **1:44–1:50 is the most cluttered frame in the episode (1:48.2).** All of these sit on screen at full brightness at once: the 16-row table with 14 scores, the pooled strip and 12/24, "the obvious guess", the vote strip with its marker and 40.5%, and two stacked equations. There is no single focal point. The table was dimmed at 1:13–1:21 but returned to full brightness at 1:23 and stays there through 1:49.
  2. **The paired equations are typeset differently (1:48.2).** The pooled form uses inline `\sum_i` (textstyle) over a fraction bar. The row-average form uses a display Σ with *i* below. The two formulas are the contrast the beat exists for, yet their structures do not line up and their "=" signs sit at different x positions (1598 vs 1677 px).
  3. **Grey text is below the §5 7 : 1 text contrast.** Measured from pixels against the background (20,21,26):
     - axis title (150,152,166): 6.37 : 1 at 0:12.9;
     - tick labels: 6.31 : 1;
     - GVT citation: 6.15 : 1 at 0:21.0;
     - M&S citation: 6.30 : 1 at 2:55.3.

     The blue (7.42) and purple (7.75) labels pass.
  4. **Nit: the purple "Cornell, 1985" header sits over 2:21–2:41.** In that stretch only random-shooter (blue, M&S) content is on screen, and purple is declared as "real Cornell data". The header's hue claims the baseline as Cornell's for 20 s.

### Motion 8.5
- **What works:**
  - Meaning-carrying transforms throughout: scores shrink to dots and fall (0:53–0:57); the live marker slides to its balance point (0:57–0:59); the disc → tile pooling (1:11–1:15); every row resized to one vote (1:19–1:21); yellow slides onto 40.5% (1:41).
  - The 1.6 s half turn about 50% (1:54–1:56).
  - The after-hits cursor becomes the −8 marker as the axis is relabelled in place (2:31–2:33).
  - The ghost ticks now slide out of zero and hold (2:34–2:40).
  - The 49/45 flights arc into +4 (2:47.8–2:49).
- **Defects:**
  1. **The formula coda breaks two §5 equation rules (1:44.5–1:50.1).**
     - Σ hᵢ/nᵢ = 17/42 is born at about 1:44.5, the 1/14 joins at 1:45.5, and Σᵢhᵢ/Σᵢnᵢ = 12/24 is complete at 1:47.8. That is two new equations in 3.3 s, against "at most one new equation per 5 s".
     - The pooled equation is complete at 1:47.8 (crop sequence) and fades on "Tails" at 1:50.1, a hold of about 2.3 s. Four terms need ≥ 3.6 s (2 s + 0.4 s × 4).
     - This is the one moment where the picture becomes the formula, and it gets the least screen time in the insight beat.
  2. **A 3.4 s fully static frame at 0:18.5–0:21.9.** It sits under "a famous study ran this same check on basketball shots": the only change is the citation line. It is within the 4 s limit, but it is dead motion at the stakes beat, where the narration names an action ("ran this same check") the picture could show.
  3. **The payoff → landing transition is a dissolve, not a transform (3:00.3–3:02.2).** The payoff fades out over 0.5 s (3:00.6) and the cold-open frame fades in over 0.8 s (3:01.6–3:02.4). It sits at a beat boundary, so it is allowed. But the dashed zero line and the −8 "bias" marker die instead of becoming the landing's 50% line and 17/42 marker, which loses the last chance to show that the bias is what the test sees.

### Audio 8.5
- **What works:**
  - Every deictic lands within 1.5 s (table above).
  - The planned holds are intentional: the 2.07 s prediction hold (0:11.7–0:13.8), the 1.7 s breath before the landing (3:00.5–3:02.2), and 0.9–1.0 s around "Longer records shrink it" (2:35.7–2:36.7).
  - Loudness is exactly on target: −14.0 LUFS, −2.1 dBTP, LRA 2.2.
- **Defects:**
  1. **The cold open is the fastest window in the episode.** It runs at 180 wpm: 30 words in 0:00–0:10, with only a 0.4 s gap (0:04.2–0:04.6) between the rule ("After each heads, check the next flip") and its worked example. The viewer must parse the episode's procedure in about 2 s while arcs, rings, the 1/2, the axis and the 16-row ghost all arrive in 9 s.
  2. **Nit: "Sanjurjo's" is heard as "Sanjorjo's" (2:27.9).** The Spanish /u/ is not landing.

### Concision 8.5
- At 486 words and 3:15, under 10% is removable.
- **The one slack beat is 0:26–0:37.** The coins morph H/T → hit/miss and the axis title swaps, then on "a fair coin" (0:36) both morph back. The reverse transform adds no information, and "a fair coin" restates the cold open.
- "Subtract the two averages, and a fair coin shows a gap of minus nineteen points" (2:01–2:07) could lose about a second ("The gap between them is minus nineteen points"), because the red arrow already shows the subtraction.

### Originality 9
- The "one vote per row" strip, with three heads squeezed into one vote and a lone tails stretched to a whole one (1:29–1:32), is a non-obvious image of the Miller–Sanjurjo bias that viewers would remember and share.
- The "test the test on a fair coin" framing is a fresh build-fail-measure take on a famous paper.
- There is no slop in narration or visuals.

## Score computation
- Weighted = (9×15 + 9×25 + 8.5×15 + 8.5×15 + 8.5×10 + 8.5×10 + 9×10) / 100 = 875 / 100 = 8.75, reported as **8.8**.
- Ceiling: lowest 8.5 + 2 = 10.5, so it does not bind.
- Caps: none.
- **FINAL 8.8, FAIL.**

## FIXES (highest impact first)

1. **[1:43.7–1:51.5][Motion/Visual] The formula coda: two equations in 3.3 s, the pooled one held about 2.3 s (needs ≥ 3.6 s), and a cluttered frame at 1:48.2.**
   - On "That's one vote per row" (1:43.7), dim the table, both strips' labels and "the obvious guess" to 30%. The two strips and the right column become the only bright objects.
   - Keep the hᵢ/nᵢ flights and the 1/14 build on "one vote per row".
   - Add `[pause 0.8]` after "and you get one half." so the 12/24 → Σᵢhᵢ/Σᵢnᵢ restack starts no earlier than 5 s after the first equation's birth.
   - Hold both formulas ≥ 3.6 s after the pooled one completes: the fade on "Tails crowd" must start ≥ 1:51.4 in the re-timed master.
   - During the hold, flag the one difference (Σ inside the fraction vs Σ outside it) with a 0.8 s `Indicate` on each Σ, so the eye reads "ratio of sums" vs "average of ratios".
   - Expected effect: Motion +0.5 and Visual +0.25.
2. **[1:44.5–1:50][Visual] The paired equations have mismatched typography.**
   - Set both in `\displaystyle` at the same `font_size`: `\frac{\sum_i h_i}{\sum_i n_i}` and `\frac{1}{14}\sum_i \frac{h_i}{n_i}`.
   - Left-align them on a shared x, and align their "=" signs and right-hand fractions (12/24 over 17/42) on one vertical. The pair then reads as a comparison, not as two unrelated blocks.
3. **[0:00–0:12][Audio/Hook] The cold open runs at 180 wpm.**
   - In `narration_text.py`, change the `[pause 0.12]` after "check the next flip" to `[pause 0.45]`, and the one after "one of the two is heads" to `[pause 0.5]`.
   - Start the 16-row ghost deal-in only after "sixteen sequences" ends.
   - Cost: about +0.8 s. The question still ends by about 0:12.5, inside the 15 s hook window.
   - Expected effect: Audio +0.5.
4. **[whole episode][Visual] Grey text contrast is 6.15–6.37 : 1, below the §5 7 : 1 minimum.**
   - Lift the grey *text* token (axis titles, tick labels, citations, secondary labels) from about (150,152,166) to about #A6A9B5. That measures about 7.5 : 1 against (20,21,26).
   - Leave the grey tails tiles, axes and strokes as they are, so the tails/miss semantics do not change.
5. **[0:18.5–0:21.9][Motion] A 3.4 s static frame at the stakes beat.**
   - On "ran this same check" (about 0:19.5), re-trace the two blue arcs on the HHTH row (0.8 s, `Create` with `smooth`). The check the narration names is shown being run again.
   - Then on "basketball shots" (about 0:22.5), pulse the two blue rings once. This removes the dead stretch with motion that encodes the procedure.
6. **[0:26.3–0:37.3][Concision/Motion] The hit/miss morph and its reverse morph cost about 11 s for no new information.**
   - Keep the H/T letters. On "Heads are hits", write small grey "hit"/"miss" sublabels (Text 20) under each coin and the axis-title word swap. On "a fair coin", fade the sublabels out (no reverse morph).
   - Trim "So first, test the test on a shooter we know is random: a fair coin." to "So first, test the test on a shooter we know is random."
   - Also trim 2:01 to "The gap between them is minus nineteen points."
   - Saves about 2.5 s. Expected effect: Concision +0.5.
7. **[3:00.3–3:02.2][Motion] The payoff → landing transition is a dissolve.**
   - Keep the dashed zero line and the blue −8 marker alive.
   - `ReplacementTransform` the points axis back into the 0–100% share axis (the dashed line becomes the 50% "obvious guess"), and the −8 marker into the 17/42 marker. Fade only the brace, the +4, the column and the header.
   - The ghost rows then collapse onto a marker that is already there, and the bias visibly becomes "what this test sees".
8. **[2:09–2:41][Visual] Nit: the purple header sits over random-shooter content.**
   - Render "Cornell, 1985" in ink/white until the purple 49% / 45% arrive at 2:42, then recolour it purple (0.5 s).
   - Purple then means Cornell data only.
9. **[2:27.9][Audio] Nit: "Sanjurjo's" is heard as "Sanjorjo's".**
   - Respell it phonetically in the TTS string, e.g. "San-hoor-ho's", or add a Kokoro lexicon entry, so the Spanish /u/ lands. Re-check that the narration diff no longer flags it.

## REACHES 9 IF ALL FIXED
Yes, with no structural change:
- Fixes 1, 2 and 4 bring Visual to 9 (one focal point per frame, all §5 standards met).
- Fixes 1, 5 and 7 bring Motion to 9 (every equation readable, no dead stretches, the landing transforms).
- Fix 3 brings Audio to 9.
- Fix 6 brings Concision to 9.
- Hook, Clarity and Originality are already 9.
- Result: weighted 9.0, ceiling 11.0, no caps, **FINAL 9.0**.

The margin is thin. Fixes 1, 3 and 4 are the ones that must land.

## KEEP
1. **The one-vote strip (1:19–1:43).** Every row resized to one equal vote, HHHH's three heads squeezed into one, HTTT's lone tails stretched to a whole one, the 8/11 row outlines, and the yellow sliding onto 40.5%.
2. **"Test the test" with a live marker (0:53–1:07).** Scores fall as dots, the marker slides 50% → 40.5%, then "cold −9.5 points".
3. **The mirror-to-payoff chain (1:51–2:55).** The half turn about 50%, the after-hits cursor carried into the −8 marker with the axis relabelled in place, and the ending on the purple +12 brace. The landing then rebuilds the cold-open frame with 17/42 → "hot".
