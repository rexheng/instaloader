# Round 6 — craft critic (visual design, motion, A/V sync; all dimensions scored)

Evidence: `review/` pack (metrics.json 17:28, newer than final.mp4 17:26): report.md, all 12 contact sheets,
keyframes kf_01, 04, 08, 10, 12, 14, 16, 17, 19, 23, 27, 29, 31, 33, 35, 37, 39, 40 at full resolution, plus
extra ffmpeg frames at 0:20.6, 0:33.0, 0:35.5, 0:40.2, 1:12.6, 1:13.2, 2:40.0, 2:40.6, 2:41.2, 2:41.8, 2:47.5,
2:48.1, 2:54.6, 2:55.3, 3:12.8, 3:13.4, 3:30.0, 3:30.6, 3:30.9, 3:31.2, 3:31.5, 3:31.8. Transcript, script.md,
narration.txt, facts.md read. All Datasaurus and Anscombe statistics recomputed with numpy from the episode's
own data files.

```
EPISODE: 020 — "A Dinosaur Hiding in Your Summary Statistics"
IDEA: Two means, two SDs and a correlation pin down exactly one ellipse (centre, box, touch points on the
      best-fit line), so any shape with that ellipse — a dinosaur, a star, Anscombe's four sets — has the same
      five numbers and the same line; only a plot shows the shape.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8 · Originality 9
WEIGHTED: 8.5   AFTER CEILING: 8.5 (lowest 8 + 2 = 10, not binding)
CAPS: none
FINAL: 8.5   PASS: no
```

## FACTS
| Claim | Status | Source / check |
|---|---|---|
| Dinosaur: 142 points, x̄ 54.26, ȳ 47.83, s_x 16.76, s_y 26.93, r −0.06 | Verified | numpy on datasaurus_dozen.tsv: 54.263, 47.832, 16.765, 26.935, −0.0645 (first two decimals, labelled "first two decimals, as published") |
| Drawn by Alberto Cairo, 2016 · The Functional Art | Verified | Matejka & Fitzmaurice 2017 acknowledgements; Cairo's 2016 post |
| 703 physiology papers, 86% bar graphs, 13% showed points | Verified | Weissgerber et al. 2015, PLoS Biol 13(4):e1002128: n = 703, 85.6% bar graph, 13.4% univariate scatterplot |
| Version 1 star: centre moved, s_x grew, s_y shrank "almost a quarter" | Verified | on-screen 50.00/50.00/20.51/20.50/0.00; s_y −23.9% |
| Two means → point; two SDs → box; many inscribed ellipses; r picks one | Verified | 1-SD covariance ellipse touches x̄ ± s_x at ȳ ± r·s_y; inscribed family is one-parameter |
| "One SD right, on average r SDs up" = best-fit line through mid of every vertical slice | Verified | OLS of y on x: ŷ−ȳ = r(s_y/s_x)(x−x̄); chord midpoints of the ellipse lie on it |
| Fixed star matches all five "to every decimal place" | Verified (by construction) | facts.md #10; translate/scale/shear argument re-derived |
| Star median 52.16 vs 46.02, "misses it by six" | Verified | 6.14 |
| Matejka & Fitzmaurice 2017, CHI; 12 shapes from the dinosaur; same five numbers | Verified | Datasaurus Dozen = dino + 12; recomputed circle/star/bullseye/x_shape/h_lines all truncate to 54.26/47.83/16.76/26.93/−0.06 |
| Dozen medians 51.02, 50.11, 47.38, 39.87, 50.47 | Verified | numpy medians 51.025, 50.111, 47.383, 39.876, 50.474 |
| Anscombe 1973, 11 points, r 0.82, x̄ 9.00, ȳ 7.50, s_x 3.32, s_y 2.03 in all four | Verified | numpy: r 0.816–0.817, s_y 2.030–2.032; The American Statistician 27(1):17–21 |
| slope = r s_y / s_x; dinosaur −0.06×26.93/16.76 ≈ −0.10 | Verified | polyfit on dino: −0.1036 |
| "Most of those papers used a bar graph, which draws only two" | Verified | 85.6%; bar + error bar encodes ȳ and one spread number |

No wrong or fabricated claim found. Every empirical claim carries an on-screen citation.

## MECHANICS
runtime 3:34.5 · 150 wpm (speech time; 494 words) · max silence 2.09 s (planned commit hold, 0:12.9) ·
max static 3.40 s (2:49.7) · −14.0 LUFS / −1.6 dBTP · leading 0.00 s / trailing 1.92 s · WER 3.7% ·
0 banned phrases · layout audit 0 issues on settled frames.

Transcript scan: no §4 phrase; questions are single ("How much can five numbers hide?" 0:39, "So what exactly
do five numbers pin down?" 1:03, "How would you fix it?" 1:51), never chained. Hook: commit question ends 0:12.9.

## What I saw, beat by beat (flipbook)
- **0:00–0:15** Empty 0–100 axes, "n = 142", five blank slots that fill in yellow on their spoken words. Clean,
  but the first frame (kf_01) is an empty chart and an empty table; the question lands at 0:12.9, a hair past
  the 0:12 anchor. The commit is only about tilt, the half the viewer gets *right*.
- **0:15–0:27** Grey guess cloud and dashed "your line", then the cloud's own points travel into the dinosaur
  (0:19–0:21). Strong reveal; real motion carries real correspondence.
- **0:27–0:39** Dinosaur squeezes to a strip, bar to ȳ, error bar. At 0:35–0:39 (kf_08) the ±s_y whisker —
  the object being named "an error bar" — is drawn inside the column of 142 blue strip dots and is half
  occluded; the bar's translucent fill also sits over them. Weakest-read frame in the stakes beat.
- **0:41–1:03** Dashed star target, "dinosaur | now" readout with = / ≠ glyphs (red/green always paired with a
  glyph), live drift 0/5, red vs yellow mean ± SD crosses. Textbook Stuff-Made-Here fail-by-a-measured-amount.
- **1:05–1:47** The insight: cross → box (walls grow from arm tips, 1:15–1:17), two grey ghost ellipses, the
  yellow one, r sweep 0 → 0.80, dashed line, five vertical slices sliding to the wall and collapsing onto the
  touch point (1:33–1:36). This is the episode's best minute; the animation is the argument. But it is also
  the densest: 1:20–1:42 carries six steps in 22 s with the review kit's longest unbroken stretch (12.4 s from
  1:29.7), and the "what if" r = 0.80 ellipse is the same yellow as the dinosaur's real summary.
- **1:47–2:07** Replay v1 with a live red ellipse; prediction hold with the star dimmed; slide / stretch / shear
  each turn their rows green (1:55, 1:57, 2:03). Every move encodes exactly one number. Excellent.
- **2:07–2:39** Median row arrives red; Dozen roll call with the yellow ellipse unmoved and the median jumping.
  Each shape lands on its word (deictic sync verified).
- **2:39–3:14** Anscombe: 11 points travel out of the stripes; at 2:40.6 the Anscombe citation is already
  under the stripes on the 0–100 axes, and at 2:41.2 the axes have no tick labels while his readout is already
  in. Then 0.82 flies to the touch dot, s_x / r / s_y copies label run and rise, the line grows, slope formula
  assembled from the segments, quartet with ellipse and line copies. Correct and well built, but 35 s that
  partly re-teaches B9's rule and re-makes the Dozen's point.
- **3:12–3:34** Hand-off: at 3:13.4 the frame is a lone ellipse floating in an empty field next to
  "slope = r s_y/s_x", no axes, before the opening frame fades in around it. The landing itself is strong:
  dashed line Indicated, values fly into the formula, ≈ −0.10, ellipse squeezed into the ±s_y error bar
  (3:27–3:29, a superb image), dinosaur returns. During the bar's park (3:30.6–3:31.5) the bar slides across the
  cloud and line, and at 3:30.9 its left edge and fill cover the plot's "x" axis label (a moving pass, < 0.5 s;
  noted as a Visual deduction, not the cap-7 trigger, which I reserve for settled frames).

## Scores, with evidence
- **Hook 8.5.** Concrete numbers on screen from frame 1 and a genuine commit, then a dinosaur reveal that pays
  off; the landing re-sees the opening ("your line was exactly right… your cloud was wrong", 3:14–3:21). Held
  below 9: first frame is empty axes and blank slots (kf_01); commit ends 0:12.9; the explicit prediction
  (tilt) is the half the viewer gets right, while the wrong half (shape) is only asserted ("you probably
  pictured").
- **Clarity 8.5.** Concrete-first, every number checks, assumptions stated (two-decimal truncation on screen),
  honest limit (median). 1:20–1:42 needs a rewatch: six steps in 22 s, no breath for 12.4 s; "Correlation r
  means" at 1:23 is half-swallowed (the transcriber dropped "Correlation").
- **Visual 8.5.** Fixed palette rigorously held, red/green always with ≠/=, sizes and margins clean, one dark
  background, citations bottom-left. Deductions: occluded error bar 0:35–0:39; empty hand-off frame 3:13.4;
  bar crossing the "x" label 3:30.9; citation under the wrong dataset 2:40.6; yellow also used for the
  hypothetical r = 0.80 ellipse (1:27–1:38).
- **Motion 8.5.** Objects persist and transform (cloud→dino, dino→star, slices→touch point, ellipse→error bar,
  ellipse copies to the quartet). Static ≤ 3.4 s. Held below 9 by the two fade-based joins (2:39–2:42 Anscombe
  entry with vanishing ticks; 3:12–3:15 landing hand-off where the opening frame fades in instead of the
  quartet's axes transforming into it) and a slightly busy run of symbol flights 2:53–2:56.
- **Audio 8.5.** On-target loudness, 150 wpm, shaped pauses, all 12 deictics land. Letter-name strings run
  together: "one ess ex across, r ess why up" heard as "1sx… rsy" (2:53–2:55); "rise, over run" heard as
  "overrun" (3:00); "Correlation" swallowed (1:23); "one" held 0.62 s (0:48.6).
- **Concision 8.** ~500 words, little filler, but the Anscombe block (2:39–3:14) is the one slack beat: its
  "same five numbers, different shapes" was just shown with twelve shapes, and its rise/run rule was already
  shown at r = 0.80.
- **Originality 9.** The Datasaurus is familiar; reading the five numbers as one ellipse, fixing the star by
  slide/stretch/shear, and squeezing the ellipse into the bar graph's error bar are angles I have not seen
  taught this way.

## FIXES (highest impact first)
1. **[1:20–1:42][Clarity/Audio]** Six steps in 22 s, 12.4 s without a breath, "Correlation" swallowed.
   → Replace "Correlation r means one standard deviation…" with "Read r like this: one standard deviation to
   the right, on average r standard deviations up." Add `[pause 0.8]` after "standard deviations up" (hold the
   finished run + rise) and `[pause 0.8]` after "every vertical slice" (hold the five midpoints on the dashed
   line before they slide). Pay for it with fix 2.
2. **[2:39–3:02][Concision]** Anscombe block re-makes the Dozen's point and re-derives B9's rule over 23 s.
   → Merge B18–B20 into one sentence: "Anscombe made this point in 1973 with eleven points, and his line obeys
   the same rule: r ess why up for every ess ex across." Keep the 0.82 → touch dot flight, the run/rise build
   and "So the slope is rise over run" with its formula; drop "His correlation is point eight two, so the
   ellipse touches the right wall high up" as narration (the flight shows it). Saves ~8 s, which funds fix 1.
3. **[0:00–0:13][Hook]** Empty first frame; commit at 0:12.9 on the half the viewer gets right.
   → Show the five values already written at frame 0 (yellow), cut "Picture the cloud, and" so "Which way does
   its best-fit line tilt?" ends by ≈ 0:10; during the 1.5 s hold draw three faint grey candidate lines through
   (x̄, ȳ) — up, flat, down — so the commit is visible; at 0:15 two fade and the slight-down one becomes
   "your line". Keeps the landing's "your line was exactly right" literal.
4. **[0:33–0:39][Visual]** The ±s_y error bar named at 0:35 is buried in the 142 strip dots.
   → On "an average" dim the strip points to 30% (restore on "showed the points", 0:37), set the bar and error
   bar z-index above the points, error-bar stroke 4, fill opacity ≤ 0.15.
5. **[3:12.3–3:15][Motion/Visual]** Lone ellipse floats on an empty field (3:13.4) before the opening frame
   fades in.
   → Transform panel I's axes into the 0–100 axes (ReplacementTransform of axis lines, tick labels handed over
   with TransformMatchingTex) while the ellipse grows, so the ellipse always sits on axes; fade in only the
   guess cloud and labels.
6. **[3:30.6–3:31.5][Visual]** The parked bar slides across the cloud and line and covers the "x" axis label
   (3:30.9).
   → Do not translate it through the plot: FadeOut the in-plot bar (0.4 s) and FadeIn the parked bar at its
   final spot (0.4 s), or move the "x" label below the axis end for this beat and path the bar so its left edge
   stays ≥ 0.15 units right of the label.
7. **[2:53–3:01][Audio]** "1sx… rsy… overrun".
   → Respell "one ess ex across, r times ess why up", render that sentence at speed 0.78 with `[pause 0.3]`
   between the clauses; write "So the slope is the rise [pause 0.3] over the run."
8. **[2:40–2:42][Visual]** Anscombe citation appears under the stripes on 0–100 axes (2:40.6); axes show no
   ticks at 2:41.2 while his readout is already in.
   → Delay the citation FadeIn until his 11 points settle (≈ 2:42.0); crossfade old → new tick labels in place
   rather than removing them first.
9. **[1:23–1:41][Visual]** The hypothetical r = 0.80 ellipse uses the dinosaur's summary yellow.
   → Draw the "what if" ellipse, run, rise and dashed line at 60% opacity (or a dashed yellow stroke) while r ≠
   −0.06, returning to solid yellow when r sweeps back on "For the dinosaur".
10. **[0:48.6][Audio]** "Version one" holds "one" 0.62 s → regenerate the line, or say "The first version
    slides every point…".

REACHES 9 IF ALL FIXED: yes, narrowly. The structure (commit → reveal → stakes → measured fail → ellipse insight
→ fix by three moves → honest limit → real result → landing that re-sees the opening) is right; fixes 1–3 lift
Hook, Clarity and Concision to 9, and fixes 4–9 remove every Visual/Motion deduction I can cite. No structural
change needed.

KEEP:
- The slices sliding to the wall and collapsing onto the touch point (1:33–1:36), and the ellipse squeezed into
  the ±s_y error bar (3:27–3:29): the two frames that are the proof.
- Slide / stretch / shear fixing one row each with the live = / ≠ readout (1:53–2:05).
- The landing's split verdict, "Your line was exactly right… Your cloud was wrong", over the returned opening.
