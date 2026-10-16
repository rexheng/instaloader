# Episode 20, round 3 craft review (motion, visual design, sync)

Evidence: `review/` pack, generated 19:32 after `final.mp4` was written at 19:30, so it is current. I read report.md, metrics.json, transcript.txt, transcript_words.tsv and narration_diff.txt; all 12 contact sheets; keyframes kf_03, kf_08, kf_11, kf_13, kf_15, kf_18, kf_21, kf_24, kf_33, kf_34 and kf_36 at full resolution; and 18 extra frames I pulled with ffmpeg:
- single frames at 0:00.0, 1:52.0, 2:32.4, 2:33.0, 2:33.6, 2:44.3, 2:59.2, 3:00.9, 3:12.6, 3:16.6, 3:17.4, 3:18.3, 3:19.0, 3:23.5, 3:24.4, 3:25.0, 3:25.6 and the last frame;
- strips at 5 fps over 3:17.9–3:20.3 (quartet copies) and 3:23.9–3:26.3 (landing);
- a strip at 2 fps over 2:22.6–2:34.6 (the Dozen roll call).

I recomputed every number with Python from `datasaurus_dozen.tsv` and `anscombe.csv`. I also read script.md, facts.md, the CHANGELOG and both round-2 reviews.

```
EPISODE: 020 — "A Dinosaur Hiding in Your Summary Statistics"
IDEA: Two means, two SDs and a correlation fix exactly one ellipse (a centre, a box, and the height r·s_y where it
      touches the walls), so any shape with that ellipse shares the five numbers, and even the best-fit line; only a
      plot shows the shape.
SCORES: Hook 8.5 · Clarity 9 · Visual 8.5 · Motion 8.5 · Audio 9 · Concision 8.5 · Originality 8.5
WEIGHTED: 8.7 (8.675)   AFTER CEILING: 8.7 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none
FINAL: 8.7   PASS: no
FACTS:
  142 points in `dino` | Verified | datasaurus_dozen.tsv (142 rows)
  x̄ 54.26, ȳ 47.83, s_x 16.76, s_y 26.93, r −0.06 (first two decimals, as published) | Verified | recomputed 54.2633 / 47.8323 / 16.7651 / 26.9354 / −0.0645
  Datasaurus drawn by Alberto Cairo, 2016 · The Functional Art | Verified | Autodesk page acknowledgement; Cairo's 2016 post
  703 physiology papers, 86 % bar graphs, 13 % showed the points | Verified | Weissgerber et al. 2015, PLoS Biol 13(4) e1002128 (85.6 %, 13.4 %)
  Version 1 star: all five break; y spread shrinks "almost a quarter" | Verified | 26.935 → 20.509 = −23.9 %, our construction (facts #4)
  Ellipse inscribed in the ±1 SD box touches the right wall at ȳ + r·s_y | Verified | support function of the covariance ellipse
  "At −0.06 that's just below the middle" | Verified | 47.832 − 1.737 = 46.096
  Slide / stretch / shear fixes all five "to every decimal place" | Verified (derivation) | affine moves; facts #9–10
  Star median misses by six (46.02 vs 52.16) | Verified for dino 46.0256; star value from our construction | facts #11
  Matejka & Fitzmaurice 2017, CHI: perturb, bias toward shape, accept only if stats hold to 2 dp | Verified | CHI 2017 pp. 1290–1294
  Twelve shapes; same ellipse, different median | Verified | medians circle 51.03, star 50.11, bullseye 47.38, x 39.88, h_lines 50.47, dots 51.30; all five stats agree to 2 dp (truncated)
  Anscombe 1973, 11 points, r 0.82, five shared numbers | Verified | I–IV: 9.000, 7.50, 3.317, 2.03, 0.816
  OLS slope = cov/s_x² = r s_y/s_x ≈ 0.50 | Verified | 0.5001 (I); 0.82·2.03/3.32 = 0.501
  Landing: the guess line equals the line the five numbers force | Verified | slope −0.1036, through (x̄, ȳ)
MECHANICS: runtime 3:37.0 · 162 wpm (speech), 153 overall · max silence 1.96 s · max static 3.5 s (planned hold 1:37.6–1:41.1) · −14.1 LUFS / −2.0 dBTP
FIXES (highest impact first):
1. [3:24.4–3:35][Hook/Originality] The stakes beat (0:26–0:38: 86 % of papers draw a bar, 13 % show points) is
   never paid off. The episode answers "how much can five numbers hide?" but not "what does the bar graph you read
   on Monday hide?", so the real-world consequence ends at 0:38. Change: after "All that five numbers can draw."
   (3:30.5), insert "Eighty-six percent of those papers drew two of them." (≈2.3 s). On it, TransformFromCopy the
   yellow ellipse into the ȳ bar with its ±s_y error bar from 0:33 (same position and colour). Then
   "The dinosaur lived in everything they leave out." returns the points around the bar and ellipse together. The
   ending then re-sees both the cold open and the stakes.
2. [2:08.8–2:13.5][Motion] The nudge contradicts its own sentence. On "biased toward a target shape" the ringed tail
   point steps from (91.3, 41.5) to (94.0, 46.3), away from where the circle will be (kf_24, 2:11.1), and the dashed
   target circle is only drawn after the step (it first appears in the 2:13 frame). Change: draw the dashed circle
   on "Nudge" (2:08.8, 0.6 s Create). On "biased toward" (2:10.2), step the ringed point 5.5 units toward the
   nearest point on the circle, which is inward and left. It still breaks x̄ and s_x, so recompute and show ≠ as
   now. Undo on "keep the nudge only if" exactly as now. The motion then encodes both rules: bias, then rejection.
3. [2:57.5–2:59.6][Motion/Clarity] cov(x,y) → r s_x s_y is a glyph crossfade, with no matching parts for
   TransformMatchingTex. At 2:59.2 the ghost "cov(x,y)" sits under "r s_x s_y", and "covariance" is asserted
   rather than built. Change: on "The covariance is" write a side line under the fraction, "cov(x,y) = r s_x s_y".
   Build r, s_x and s_y by TransformFromCopy from the readout symbols at bottom right (Indicate each source for
   0.3 s first). Then ReplacementTransform that line's right side up into the numerator while the old numerator
   fades, flag it in yellow for ≤ 1 s, and fade the side line. Keep the strike-through of s_x as it is.
4. [3:18.0–3:19.4][Motion] The copies of the ellipse and line launch as a stacked train from panel I. At 3:18.3,
   four ellipses overlap inside panel I; at 3:19.0, five parallel lines hatch across panel I's points, which reads
   as a render smear for about 0.4 s. Change: give each copy `path_arc=-0.6` so it arcs above the panel row, and
   use LaggedStart with lag_ratio 0.5 and run_time 1.2, in the order ellipse II, III, IV, then line II, III, IV. No
   two copies should share a position in any frame.
5. [3:20.3–3:24.4][Visual] The quartet labels "an outlier" and "one point" sit about 0.2 units (≈28 px, frame
   3:23.5) above the readout row "s_x = 3.32 s_y = 2.03 r = 0.82", so they read as its column headers. The labels
   are also centred by bounding box, so "a curve" and "one point" sit about 5 px higher than "a trend" and
   "an outlier". Change: move the readout 0.35 units down (its x̄ row can share the citation's baseline at y ≈ −2.96;
   both stay above −3.2), or place it centred under panels II–III with buff ≥ 0.45 from the labels. Align all four
   labels on one baseline: `lab.align_to(ref_label, DOWN)` using a strut, or `Text` with the same `line_spacing`
   and the first label's baseline.
6. [2:45–2:53][Visual] For about 8 s the top-right 60 % of the frame is empty while the readout sits at bottom
   right (kf_33, 2:51.9), and the focal pair (the touch dot, r = 0.82) is split across the frame diagonally. Change:
   land the Anscombe readout at mid-right (centre y ≈ +0.6, level with the touch dot), so "r = 0.82" → touch dot is
   a short horizontal flight. On "Least squares" (2:51) slide the readout down to its current slot (0.8 s, smooth)
   to make room for "slope =". The move then means "make room for the derivation".
7. [3:24.5–3:25.3][Motion] The landing is a double exposure. In the 3:25.0 frame, the incoming "ȳ = 47.83" and
   "s_x = 16.76" overlay ghost panels III–IV at about 40 %, and the ghost "a trend" and "a curve" sit under the guess
   cloud. Change: run it in sequence with one continuous object. First fade out everything in the quartet except
   panel I's ellipse (3:24.2–3:24.7) while that ellipse grows. Then fade in the opening frame (3:24.7–3:25.3). The
   frame never empties (the ellipse is always there), and no text overlaps text.
8. [0:00–0:12.3][Hook] The commit prompt ends at 0:12.3, and "Picture the scatterplot and its best-fit line" is
   an open "imagine", not a commitment. Change: cut "five numbers:" from the first sentence (the five symbol slots
   are on screen from frame 1), saving ≈1.2 s, so the prompt ends by about 0:11. Then make it a commitment:
   "Picture the scatterplot, and sketch its best-fit line." Keep the 1.5 s hold. Fade in a faint grey "?" at the
   plot centre during the hold, so the static 3.3 s (0:10.9–0:14.2) is not empty axes.
9. [2:24.2–2:33.3][Concision] The roll call has four 1.6 s silences in a row (metrics: 2:24.2, 2:26.7, 2:29.1,
   2:31.6). Each shape lands in 0.5 s and is legible within about 0.8 s (2 fps strip), so the fourth silence drags.
   Change: set the bullseye and X pauses to [pause 1.2] and the stripes pause to [pause 0.9]. Keep the dots hold at
   1.5, since it leads into "Every one of them". This saves ≈1.2 s, and the cadence speeds up into the punchline.
10. [0:47–0:55][Visual] "first two decimals, as published" (kf_11) has a cap height of about 24 px, the floor for
    citations, and it disappears by 0:55, before the fail beat it qualifies is over. Change: `Text` font_size 20
    (MathTex 28), and hold it to 1:03, when the dinosaur returns.
REACHES 9 IF ALL FIXED: yes, narrowly.
  - Fixes 2, 3, 4 and 7 take Motion to 9; fixes 5, 6 and 10 take Visual to 9.
  - Fixes 1 and 8 take Hook to 9, and fix 1 is also the likeliest lift for Originality. Fix 9 takes Concision to 9.
  - That gives (15·9 + 25·9 + 15·9 + 15·9 + 10·9 + 10·9 + 10·8.5) / 100 = 8.95, or 9.0 if fix 1 lifts Originality.
  - No structural change is needed. The arc already runs misconception → commit → reveal → measured v1 fail (0/5)
    → one picture (the ellipse in its box) → three-move repair (0→2→4→5) → honest limit (median) → sourced
    Dozen/Anscombe → landing on the opening frame. What is left is finish work, plus the one narrative loose end
    (fix 1).
KEEP:
  - The ellipse assembled from the readout (1:05–1:31): means fly into the balance point, SDs grow the box, and r
    sets the touch dot; then the live r-sweep with the "r s_y" rise. This is the episode's thesis as one picture.
  - The live "dinosaur | now" readout with =/≠ and the k/5 counter, with the red live ellipse drifting off the
    yellow one on the replay (1:34–1:41) and closing in three verb-synced moves (1:41–1:53).
  - The frozen yellow geometry through the Dozen with a wandering live median (2:13–2:38), and the best-fit line
    grown through the touch point (3:09–3:11), which pays off over the viewer's dashed guess (3:29–3:31).
```

## Notes by step

**1. Script, read cold.** The idea fits in one sentence. The palette in script.md is followed in every frame I saw:
- YELLOW: the summary geometry.
- BLUE: the data.
- RED: a summary that has drifted.
- GREEN: matches, always with "=".
- Grey: context.

That is 4 hues, never red against green alone, and one background.

**2. Fact-check.** I recomputed every number on screen or in the narration (table above). I found nothing Wrong and nothing Unverifiable among the empirical claims, and every empirical claim has an on-screen citation bottom left:
- Cairo 0:23–0:26
- Weissgerber 0:26–0:39
- Matejka & Fitzmaurice 2:03–2:39
- Anscombe 2:41–3:24

The facts.md note on truncation versus rounding is correct: dino s_x is 16.7651, which rounds to 16.77, so "first two decimals" is the right convention.

**3. Mechanics.** All within the bar, so no mechanical cap applies:
- runtime 3:37.0
- 161.7 wpm on speech time
- longest internal silence 1.96 s (0:12.1–0:14.1, the planned commit hold)
- longest static stretch 3.5 s (1:37.6–1:41.1, the planned "how would you fix the star?" hold)
- −14.1 LUFS, −2.0 dBTP
- leading silence 0.0 s, trailing 1.85 s

**4. Transcript.**
- WER is 2.5 %, and every difference is number formatting ("oh" vs "zero", "s x" vs "sx").
- "Matejka", "Fitzmaurice", "Weissgerber" and "Anscombe" are all transcribed correctly.
- There are no §4 banned phrases. "Now replay version one" is an instruction about the picture, not signposting.
- The two questions (0:37.9 and 1:00.0) are 22 s apart, so they do not form a chain.
- The hook is the concrete numbers from frame 1, with the commit at 0:09.4–0:12.3.

**5. Flipbook and sync.** I checked each deictic against word timings:
- "Here are the real points" (0:19.5): the morph runs 0:20–0:23.
- "bar graphs" (0:31): the bar grows by 0:33.
- "error bar" (0:34): drawn at 0:35.
- "Raise it" (1:18.8): the sweep is under way by 1:21.
- "R times S-Y" (1:24): the label is on by 1:25.
- "watch the ellipse" (1:36): the red live ellipse is visible 1:37.
- Slide, stretch, tip (1:41.0, 1:42.9, 1:45.4): the counter reads 2/5 at 1:43, 4/5 at 1:45, and 5/5 by 1:49.
- "Nudge" (2:08.8): the ring appears at 2:09.
- Dozen nouns: the 2 fps strip shows each dataset landing 0.4–0.6 s before its noun (star 143.1 vs 143.7; bullseye 145.6 vs 146.0; X 148.1 vs 148.6; stripes 150.6 vs 151.0; dots 153.1 vs 153.6).
- "these five numbers" (3:15.9): the box goes round the readout at 3:16.6.
- "this ellipse" (3:26.3): the carried ellipse is pulsed.

The beats match §6:
- cold open 0:00–0:19
- stakes 0:19–0:38
- naive build and fail 0:38–1:00
- insight 1:00–1:53
- limit 1:53–1:58
- payoff 1:58–3:24
- landing 3:24–3:37

There are no hard cuts, and every scene change is a transform or a staggered fade. The only places continuity looks rough are the copy train (fix 4) and the landing double exposure (fix 7).

**6. Keyframes against §5.**
- Safe area holds. The readout's right-hand "≠" ends at about 1770 px, and the quartet's "x" at about 1812 px, both inside 1824 px.
- The citation baseline is about 955 px (y ≈ −2.96). The layout audit reports 0 issues in 237 checks, and I saw no settled overlap.
- Type:
  - readout cap height about 45 px;
  - tick labels about 30 px;
  - citations about 26 px;
  - the grey decimals note about 24 px, which is the floor (fix 10).
- Word load stays under 12 at every keyframe. The worst case is the quartet, with four 2-word labels plus a citation.
- Charts: axes are named x/y with ≤ 6 ticks. The Datasaurus is unitless, so I make no deduction.
- The guess cloud is labelled "your guess", and it is never presented as data.
- The two transitional glyph stacks (2:59.2 "cov" ghost, 3:12.6 doubled "3.32") last under 0.5 s and are not capped. The first is part of fix 3.
- I checked the real `dots` dataset, because the top-centre cluster looks smeared. It really spans y 82.8–94.2, so this is not a defect.

## Score rationale
- **Hook 8.5.**
  - For: concrete from frame 1 (axes, n = 142, five empty slots that fill on their spoken words). The guess cloud and "your line" voice the reasonable belief before it is broken at 0:20. The landing re-sees the opening exactly.
  - Against: the commit is an open "picture" that ends at 0:12.3. Tension plateaus after the median limit (1:58), because three demonstrations follow (search and Dozen, Anscombe, slope). The sourced stakes from 0:26 never come back (fix 1).
- **Clarity 9.** All numbers check, the assumptions are on screen ("first two decimals, as published"), and every source is correct. The ellipse rule is stated, drawn and reused as rise over run. The only soft spot is "covariance" being asserted at 2:57 (fix 3), which does not need a rewatch.
- **Visual 8.5.**
  - For: strict semantic palette, a consistent plot-left / readout-right grid for 2:39 of runtime, and dimming to about 30 % for context (kf_13, kf_15).
  - Against: the empty top-right during 2:45–2:53 (fix 6), quartet labels crowding the readout and off baseline (fix 5), and the decimals note at the size floor (fix 10).
- **Motion 8.5.**
  - For: nearly every motion carries a relation: guess → dinosaur, dinosaur → strip → bar, readout copies → centre and box, the live red geometry, three verb-synced affine moves, the Dozen under a frozen ellipse, panel I → quartet, and the carried ellipse at the landing.
  - Against: the nudge moves away from the target it is "biased toward" (fix 2), the cov crossfade (fix 3), the copy train (fix 4), and the double-exposure landing (fix 7).
- **Audio 9.** 162 wpm, loudness on target, intentional holds (0:12, 1:39, the roll call), and every deictic I checked lands within 0.6 s of its visual. The round-2 miss ("these five numbers") is fixed. I found no mispronunciation.
- **Concision 8.5.** Less than 10 % is removable. The slack is about 1.2 s of roll-call silence (fix 9) and about 1.2 s of B0 (fix 8). The 89 s payoff is long, but each part earns its place: the slope derivation is what makes the landing line work.
- **Originality 8.5.** Datasaurus and Anscombe are the most-shown examples in the field, which caps freshness. The "five numbers = one ellipse in a box" picture, the hand-built star repaired by slide, stretch and shear with a k/5 counter, and the guess line that turns out to be forced are all genuinely non-obvious. A 9 needs the ending to land on a consequence the viewer carries out of the video (fix 1).
