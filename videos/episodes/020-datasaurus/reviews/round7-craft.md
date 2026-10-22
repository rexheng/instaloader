# Round 7: craft critic (visual design, motion, A/V sync; all dimensions scored)

Evidence: the `review/` pack (metrics.json 19:17 is newer than final.mp4 19:15, so I used it as is). I read
report.md, narration_diff.txt, all 12 contact sheets, and these full-resolution keyframes: kf_01, 05, 07, 15, 16, 17,
19, 23, 29, 30, 32, 35, 37, 39. I also extracted frames with ffmpeg: 0:19.0/19.6/20.2, 1:12.4–1:13.6 (4 frames),
1:25.0, 1:27.1, 1:27.5–1:31.4 (6 frames), 1:39.0–1:42.6 (4), 2:40.8–2:44.0 (5), 2:49.4–2:51.0 (4), 2:54.0–2:55.5
(4), 3:07.0–3:08.8 (4) and 3:24.6–3:26.8 (6), plus 3x crops of the s_x label at 1:25.0, 1:27.1 and 1:29.5. I read the
transcript, the word timings, script.md, narration.txt and facts.md. I recomputed every Datasaurus and Anscombe
statistic from the episode's own `datasaurus_dozen.tsv` and `anscombe.csv`. I also read the round-6 reviews to check
which fixes landed.

```
EPISODE: 020 — "A Dinosaur Hiding in Your Summary Statistics"
IDEA: Two means, two SDs and a correlation pin down exactly one ellipse (a centre, a box, and touch points that lie
      on the best-fit line), so any shape with that ellipse (a dinosaur, a star, Anscombe's four sets) has the same
      five numbers and the same line, and only a plot shows the shape.
SCORES: Hook 9 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 9 · Concision 8.5 · Originality 9
WEIGHTED: 8.7   AFTER CEILING: 8.7 (lowest 8.5 + 2 = 10.5, so the ceiling does not bind)
CAPS: none
FINAL: 8.7   PASS: no
```

## FACTS
| Claim | Status | Source / check |
|---|---|---|
| Dinosaur n = 142; x̄ 54.26, ȳ 47.83, s_x 16.76, s_y 26.93, r −0.06 | Verified | My recompute: 54.26327, 47.83225, 16.76514, 26.93540, −0.0645. Shown as the first two decimals, labelled on screen "first two decimals, as published" |
| Circle / star / bullseye / X / stripes share the five numbers | Verified (truncated) | circle 54.267/47.838/16.760/26.930, star 54.267/47.840/16.769/26.930, bullseye 54.269/47.831/16.769/26.936, x_shape 54.260/47.840/16.770/26.930, h_lines 54.261/47.830/16.766/26.940 (26.93988, which truncates to 26.93); all r between −0.062 and −0.069 |
| Their medians 51.02, 50.11, 47.38, 39.87, 50.47 vs the dinosaur's 46.02 | Verified | 51.025, 50.111, 47.383, 39.876, 50.474; dino 46.026 |
| "Drawn by Alberto Cairo", on screen as Cairo, 2016 · The Functional Art | Verified | Cairo's 2016 Datasaurus post; credited in the Matejka & Fitzmaurice acknowledgements |
| 703 physiology papers, 86% bar graphs, 13% showed the points | Verified | Weissgerber et al. 2015, PLOS Biology 13(4):e1002128: n = 703, 85.6% bar graphs, 13.4% univariate scatterplots (text checked by both round-6 critics; consistent with my own knowledge of the paper) |
| Version-one star: centre moved, x spread grew, y spread "shrank by almost a quarter" | Verified | On screen (50.00, 50.00), s_x 20.51, s_y 20.50: 26.935 to 20.509 is −23.9% |
| Two means give a point, two SDs a box, and r picks one of many inscribed ellipses; the touch point is at ȳ + r s_y | Verified | Re-derived: the support of the 1-SD covariance ellipse in direction (1, 0) is s_x, reached at (x̄ + s_x, ȳ + r s_y) |
| "One SD right, on average r SDs up" is the best-fit line through the middle of every vertical slice | Verified | The OLS line ŷ − ȳ = r(s_y/s_x)(x − x̄) is the locus of the ellipse's vertical-chord midpoints |
| "For the dinosaur, it's just below the middle" | Verified | 47.83 − 0.0645 × 26.94 = 46.10 |
| Slide, stretch and tip "keeping the box" match all five "to every decimal place" | Verified (by construction) | facts.md #9–10: a shear plus a 0.2% vertical rescale keeps both SDs; "keeping the box" now describes what the move actually does |
| Star median misses by "six" | Verified | 52.16 vs 46.02 = 6.14 |
| Matejka & Fitzmaurice 2017, CHI: a search that holds the five numbers fixed while nudging points toward a target; 12 shapes grown from the dinosaur | Verified | CHI 2017, doi:10.1145/3025453.3025912; the Dozen = dino + 12 |
| Anscombe 1973, 11 points; r 0.82, s_x 3.32, s_y 2.03, x̄ 9.00, ȳ 7.50 for all four | Verified | My recompute: I–IV r 0.816–0.817, s_x 3.317, s_y 2.030–2.032, x̄ 9.000, ȳ 7.500–7.501; The American Statistician 27(1):17–21 |
| slope = r s_y / s_x; for the dinosaur −0.06 × 26.93 / 16.76 ≈ −0.10, "slope minus point one" | Verified | Displayed values give −0.0964; unrounded r s_y/s_x = −0.1036; OLS on dino = −0.1036 |
| "A bar graph, which draws only two" | Verified | A bar plus one error bar encodes ȳ and one spread value; the squeezed ellipse has exactly the ±s_y vertical extent |

No claim is wrong or fabricated, and every empirical claim has an on-screen citation (Cairo, Weissgerber, Matejka &
Fitzmaurice, Anscombe).

## MECHANICS
runtime 3:29.1 · 152 wpm (speech time; 471 script words, 479 heard) · max silence 2.37 s (0:10.3–0:12.7, the planned
commit hold) · max static 2.77 s · −14.2 LUFS / −4.1 dBTP · leading 0.00 s / trailing 1.94 s · WER 2.6% · 0 banned
phrases · 12 of 12 deictics animated within the window · layout audit 0 issues in 227 checks.

Transcript sweep: no §4 phrase. The questions stand alone: "What shape is the cloud, and which way does its best-fit
line tilt?" (0:06–0:10, one question with two halves), "How much can five numbers hide?" (0:37), "So what exactly do
five numbers pin down?" (1:01) and "How would you fix it?" (1:52). There is no fake reveal and no recap ending.
"it turns out" and "let's break it down" do not occur. Round-6 mishearings are gone: "rise, over the run" is now heard
correctly (2:53–2:55), "SX across, R times SY up" is heard as letters rather than "1sx", and "Correlation" is no longer
swallowed. The hook lands with the commit at 0:10.5.

## Round-6 craft fixes: what landed
Landed: frame 1 is now the puzzle (five yellow values, a faint "?", n = 142) with three grey candidate lines during the
hold (0:09–0:12). B9 has its pauses and the simulated r = 0.80 cloud with an averaged slice. The what-if ellipse is at
60%. Anscombe is one sentence. The strip dims under the bar (0:29–0:35). The Anscombe citation now arrives with his
points (2:45). Panel I's axes transform into the opening axes (3:07). The parked bar fades out and back in rather than
sliding through the plot (3:25–3:26). "The first version" no longer holds on "one". **Not fully landed:** see fixes
1–3.

## What I saw, beat by beat
- **0:00–0:12** The puzzle is on screen from frame 1 (kf_01): grey axes, a faint "?", n = 142, and five yellow values
  that flag on their words. The three dashed candidate lines are drawn through the centre on "which way" (sheet 1,
  0:09–0:11) and held through a 2.4 s silence. It's a real commit on both halves, shape and tilt.
- **0:12–0:25** The grey guess cloud reads as "your guess". The up and down candidates fade, and the flat one becomes
  "your line" (0:17). The guess cloud's own points travel into the dinosaur (0:19.0–0:20.2) and turn blue. The
  correspondence is carried by motion, and the citation fades in on "drawn by". This is the episode's best 13 seconds.
- **0:25–0:37** The dinosaur collapses to a strip of its y-values with the x ticks dimmed (kf_05). This is meaningful:
  a bar graph throws away x. The bar to ȳ and the error bar are drawn over the 30% strip (0:31–0:33). On "showed the
  points" (0:35–0:37, kf_07) the points come back at full strength *over* the now-dimmed bar and error bar. The column
  then holds the bar, the whisker, 142 dots and two labels at once, with no single focal point.
- **0:37–1:01** The dashed star target appears, along with the "dinosaur | now" readout, = / ≠ glyphs, "matching 5/5 →
  0/5", and red vs yellow mean ± SD crosses (sheet 4). Stuff Made Here's "fail by a measured amount", done right.
- **1:01–1:21** The red cross rides back and turns yellow. The (x̄, ȳ) copies fly in, then the s_x and s_y copies.
  Around 1:12.4–1:13.4 the small s_x / s_y labels at the arm tips sit on the dimmed dinosaur for about 1 s (not
  doubled any more). The walls grow from the arm tips (1:15), the ghost ellipses appear on "Many" (1:17), and the
  yellow ellipse is drawn with its touch dots on "picks one" (1:21).
- **1:21–1:47** This is the insight, and the densest window: the simulated cloud, the run, the slice band, the
  converging slice points, the rise, the dashed line, five slices, the slices collapsing onto the touch point, and r
  sweeping back. Two craft defects sit here:
  - The slice band, the box's right wall, the rise and the touch dot are all in the same 20 px column at
    x = x̄ + s_x. From 1:28 to 1:31 the rise reads only as a slightly thicker part of the yellow wall, and the 12 white
    points converge onto a touch dot that was already drawn at 1:21 (extracted frames 1:27.5–1:31.4).
  - The rise carries no label while the narration says "rises R times a standard deviation" (1:27.9–1:30.1). The
    "r s_y" label arrives at 1:38.8, ten seconds later (kf_16 at 1:32.5 shows an unlabelled triangle; even s_x has
    left by then).

  At 1:42–1:47 (kf_17), with r back at −0.06, the solid run and the dashed best-fit line nearly coincide. The "r s_y"
  label points at a 1.7-unit rise you cannot see, and the right touch point becomes a knot of overlapping strokes.
  Elsewhere, the slices collapsing to the touch point (1:35–1:38) is the proof as animation, and it is excellent.
- **1:47–2:09** The dinosaur returns inside the ellipse. The v1 replay shows a live red centre, box and ellipse
  (kf_19). In the prediction hold the boxes fade out and the star dims to 40%. Slide, stretch and tip each turn their
  own rows green (sheet 7, 1:57, 1:59, 2:03–2:05). Every move encodes exactly one number. It's top-channel quality.
- **2:09–2:41** The median row arrives red, ≠ 52.16. The star walks back to the dinosaur, the five rows are boxed on
  "these" (2:23), and the points stream into the circle target. Each shape of the roll call lands on its own "this"
  (sheet 9). The ellipse stays put while the median jumps.
- **2:41–3:08** Anscombe. The readout and tick labels hand over by fade: at 2:42.4 the axes are unnumbered and there
  is no readout. At 2:43.2 his 11 points have arrived over the dimmed stripes, and the citation comes in with them
  (2:45). The 0.82 flies to the touch dot (2:47). The s_x, r and s_y copies label the run and rise, with the source
  dimmed and nothing doubled (2:49–2:51). Then the line grows. At 2:52.9 (kf_30) the readout jumps from mid-right to
  bottom-right, purely to make room for the formula. The slope terms climb out of their segments into r s_y / s_x
  (2:53–2:57). Ellipse and line copies go to the quartet, with tags and rings (kf_32).
- **3:08–3:29** The hand-off transforms panel I's axes into the 0–100 axes. A brief tickless frame (3:07.6) holds a
  lone ellipse and the formula, then the guess cloud and "your line" return. The yellow line grows onto the dashed
  guess, the dinosaur's values fly into the formula (kf_35, ≈ −0.10), and "your guess" is flagged. The ellipse is
  squeezed into the ±s_y error bar (3:21–3:23, the episode's signature image, kf_37). On "dinosaur" (3:24.7) the
  points re-form by 3:25.8, and the bar is parked beside the plot (kf_39). One focal point: the blue dinosaur. The end
  card runs 3:28.5–3:29.

## Scores, with evidence
- **Hook 9.** The first frame is the puzzle (kf_01). The viewer commits to both shape and tilt by 0:10.5, with three
  visible candidate lines. The reveal is at 0:19, and the landing re-sees the opening frame exactly ("Your line was
  right… Your cloud was wrong", 3:09–3:16). Small residue: the first 6 s are a static readout plus a faint "?", text-led
  rather than image-led. That's a nitpick.
- **Clarity 8.5.** It's concrete first, every number checks, the truncation convention is stated on screen, and the
  honest limit is the median. It is held below 9 by the central step at 1:27–1:31. "the cloud rises R times a
  standard deviation" doesn't say *which* SD, and the rise it refers to is unlabelled and sits on top of the box wall,
  so "on average… r s_y up" is not readable on first watch. The viewer is rescued only at 1:38.8 by "r times ess why".
  This is the one transition that needs a rewatch.
- **Visual 8.5.** The palette is held rigorously, red and green always come with ≠ / =, the citations sit bottom-left,
  sizes and margins are clean, and the landing frame has one focal point. Deductions:
  - (a) Wall, rise, band and touch dot share one column (1:28–1:31).
  - (b) A knot of strokes plus an orphan "r s_y" label at the touch point (kf_17, 1:42–1:47).
  - (c) The column muddle at 0:35–0:39 (kf_07): bar, whisker, dots and two labels, with no focal point.
  - (d) The s_x label's backing plate clips the surrounding simulated dots into half-moons (crops at 1:25.0, 1:27.1,
    1:29.5), which reads like a render nick.

  That is more than the 8-anchor's "at most 2 minor", though each one is small.
- **Motion 8.5.** Objects persist and transform throughout: cloud to dino, dino to strip, dino to star, slices to touch
  point, ellipse to error bar, panel I to opening axes. Static ≤ 2.8 s. Deductions:
  - The 1:28–1:30 convergence, the beat's key motion, plays out where it can't be seen (onto an existing dot on the
    wall).
  - The readout jump at 2:52.9 encodes nothing.
  - The tick and readout hand-over at 2:41.5–2:44 is fade-out then fade-in, leaving unnumbered axes and no readout for
    about 2 s.
- **Audio 9.** −14.2 LUFS, −4.1 dBTP, 152 wpm. There are shaped pauses after key results: 1.4 s after "picks one",
  1.6 s after "five numbers know", 1.3 s after "every decimal place". All 12 deictics land, and every round-6
  mishearing is fixed (WER 2.6%). Nothing citable remains beyond Kokoro's timbre, which I don't penalize as such.
- **Concision 8.5.** It's 471 words in 3:29, with almost nothing to cut sentence by sentence. The one slack beat
  remains the double demonstration: the Dozen roll call (2:26–2:41) and Anscombe's quartet (2:58–3:08) make the same
  "same five numbers, different shapes" point twice. Anscombe earns his place through the slope formula, but
  "All four of his datasets share these five numbers, so they share the ellipse and line" restates what the
  ellipse-and-line copies are already showing.
- **Originality 9.** Several pictures here I have not seen elsewhere, and they would be shared: the five numbers read
  as one ellipse, the star fixed by slide / stretch / tip one row at a time, the slices collapsing to the touch point,
  and the ellipse squeezed into the bar graph's error bar.

## FIXES (highest impact first)
1. **[1:27.5–1:31][Clarity/Visual/Motion]** The rise is drawn on top of the box's right wall, the slice band and
   touch dot share that column, and the averaged white point lands on a touch dot already there since 1:21. The key
   "on average, r SDs up" evidence is unreadable. Change it as follows:
   - At "Say r is point eight" (1:21.5), dim the SD box to 30% and hide the two touch dots until the averaged point
     arrives.
   - Draw the rise 0.15 units to the right of the wall (or the band 0.15 left of it) with stroke 6.
   - Let the average of the 12 slice points land as a *new* white dot at (x̄ + s_x, ȳ + r s_y) that turns yellow and
     becomes the touch dot.
   - Restore the box to full strength on "At the wall" (1:35).
2. **[1:27.9–1:30.1][Clarity/Audio sync]** "rises R times a standard deviation" doesn't name y's SD, and the rise has
   no label until 1:38.8. Change the narration to "On average, the cloud rises r times y's standard deviation." Write
   the "r s_y" label beside the rise on "r times" (≈1:27.9) and keep it through 1:38. On "r times ess why" at 1:38.6,
   flag that existing label instead of writing it. Keep the s_x label on the run until the slices start (1:33).
3. **[1:41–1:47][Visual]** At r = −0.06 the solid run overlaps the dashed best-fit line, and "r s_y" labels an
   invisible 1.7-unit rise (kf_17). As r sweeps back (1:41), fade out the run, the rise and the "r s_y" label. Keep
   only the dashed line, the centre and the two touch dots, and flag the right touch dot on "just below the middle".
4. **[0:35–0:39][Visual]** On "showed the points", the full-strength dots cover the dimmed bar and whisker (kf_07).
   On "Only thirteen percent", fade the bar and error bar to 0 (they return at 3:21 anyway). Let the 142 strip dots
   alone carry "13% showed points", then spring back to the dinosaur at 0:39.
5. **[2:41.5–2:44.5][Motion]** Tick labels and readout fade out before the new ones arrive, leaving unnumbered axes
   and no readout for about 2 s. Crossfade the tick labels in place (old to new in the same 0.8 s, each new number at
   its tick). Have the dinosaur's readout rows dim and slide right while Anscombe's rows build in place, so the panel
   is never empty.
6. **[2:52.9][Motion/Visual]** The readout jumps from mid-right to bottom-right only to make room for the formula.
   Place Anscombe's readout at its final bottom-right position when it first appears (≈2:44.5), so nothing moves
   without meaning.
7. **[1:25–1:31][Visual]** The s_x label's background plate clips the simulated dots into visible half-moons (crops at
   1:25.0, 1:27.1, 1:29.5). Remove the plate and move the label below the run, buff 0.2 under its midpoint, where the
   cloud is sparse. Or drop the plate's opacity to 0 and z-order the label above the dots.
8. **[2:58–3:03][Concision]** "All four of his datasets share these five numbers, so they share the ellipse and line"
   narrates what the copies already show. Cut it to "All four share his five numbers." (−6 words, ≈−1.5 s) and start
   the ellipse copies on "share".
9. **[3:07.4–3:08.2][Motion]** The hand-off frame shows tickless axes, a lone ellipse and a floating formula (frame
   3:07.6). Bring the 0–100 tick numbers in with the axis transform (same 1.5 s), not after it.

REACHES 9 IF ALL FIXED: yes. Fixes 1–3 make the one hard step readable and correctly labelled, which lifts Clarity to
9, Visual to 9 and Motion to 9. Fixes 4–7 remove the remaining visual and motion nits, and fix 8 lifts Concision to
about 9. With Hook, Audio and Originality at 9, the weighted score is about 9.0. No structural change is needed: the
commit, reveal, measured failure, single picture, three-move fix, honest limit, sourced payoff and callback landing
are all present and correct.

KEEP:
- The guess cloud's own points travelling into the dinosaur (0:19–0:21), and the landing that returns to that exact
  frame and grows the yellow line onto "your line".
- Slide / stretch / tip, each turning one readout row green (1:55–2:05), and the slices collapsing onto the touch
  point (1:35–1:38).
- The ellipse squeezed into the bar graph's ±s_y error bar (3:21–3:23), and the final frame where the blue dinosaur
  is the only full-strength object.
