# Episode 20, round 3 substance review (science and story editor)

## Evidence

I used the existing `review/` pack. metrics.json (19:32) is newer than final.mp4 (19:30), so it is current. I read:
- report.md, transcript.txt, transcript_words.tsv and narration_diff.txt;
- script.md and facts.md (narration.txt is in the transcript diff);
- all 12 contact sheets.

Full-resolution keyframes I read: kf_01 (0:03.2), kf_03 (0:19.4), kf_08 (0:37.7), kf_10 (0:44.1), kf_15 (1:24.3), kf_17 (1:34.0), kf_24 (2:11.1), kf_32 (2:42.9), kf_33 (2:51.9), kf_34 (3:15.7), kf_36 (3:19.8), kf_38 (3:28.7) and kf_40 (3:37.0).

I extracted extra frames with ffmpeg:
- single frames at 0:48.0, 1:40.0, 1:55.0, 2:18.0, 2:23.0, 2:23.6, 2:24.2, 2:59.5, 3:03.0, 3:17.5 and 3:24.5;
- a strip at 2.5 fps over 3:16.0–3:18.4 (the quartet hand-off);
- a strip at 1.5 fps over 0:26–0:30 (the stakes squeeze).

Numbers: I recomputed every Datasaurus and Anscombe statistic myself with numpy from `datasaurus_dozen.tsv` and `anscombe.csv`. That covers n, means, sample SDs, r, the y-median for all 13 sets, OLS slopes, and every Anscombe set.

Citations: I verified by web search (Firecrawl):
- Weissgerber et al. 2015, PLOS Biology page and PubMed: n = 703, 85.6 % had a bar graph, 13.4 % had a univariate scatterplot.
- Matejka & Fitzmaurice 2017, the Autodesk Research page and the CHI 2017 listing: simulated annealing, random perturbations biased toward a shape, a thank-you to Cairo for the Datasaurus.
- Anscombe 1973, *The American Statistician* 27(1):17–21 (JSTOR, T&F).

```
EPISODE: 020 — "A Dinosaur Hiding in Your Summary Statistics"
IDEA: Two means, two SDs and a correlation pin down exactly one ellipse (a centre, a box, and the height r·s_y
      where it touches the side walls), so every dataset with those five numbers, dinosaur, star or Anscombe's
      quartet, shares that ellipse and even its best-fit line; the shape lives only in what the numbers leave out.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8.5 · Motion 9 · Audio 8.5 · Concision 8.5 · Originality 8.5
WEIGHTED: 8.6 (8.575)   AFTER CEILING: 8.6 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none
  Checked and not triggered:
  - Fabrication or misattribution: none (all four citations verified).
  - Factual or math errors: none (see FACTS).
  - Banned phrases: 0. No question chains (single questions at 0:37.9, 1:00.0 and 1:37.6), no "it turns out", no
    fake reveals, no recap ending.
  - Every empirical claim is cited on screen: Cairo 0:23, Weissgerber 0:27, Matejka & Fitzmaurice 2:03,
    Anscombe 2:41.
  - Sync: deictics land. "this star" at 2:23.5: the star is landed at 2:23.6. "This bullseye" 2:26.0, "This X"
    2:28.6, "these dots" 2:33.6, "this same ellipse" 2:36.2 (ellipse flagged at 2:35).
  - Bullet slide: none. Text overflow or overlap: none in settled frames (layout audit 0 of 237).
  - Mechanics are all inside the bar.
FINAL: 8.6   PASS: no
FACTS:
  n = 142 (dino) | Verified | 142 rows in datasaurus_dozen.tsv
  x̄ 54.26, ȳ 47.83, s_x 16.76, s_y 26.93, r −0.06 | Verified (raw 54.2633 / 47.8323 / 16.7651 / 26.9354 / −0.0645;
    the shown values are truncated, as published; "first two decimals, as published" is on screen 0:47–0:52) |
    numpy; Autodesk page
  "A dinosaur drawn by Alberto Cairo" + "Datasaurus: Alberto Cairo, 2016 · The Functional Art" | Verified |
    Autodesk page ("Recently, Albert[o] Cairo created the Datasaurus…"; thefunctionalart.com/2016/08/…)
  "a review of 703 physiology papers, 86 % used bar graphs … only 13 % showed the points" | Verified (85.6 % had
    ≥1 bar graph; 13.4 % had ≥1 univariate scatterplot) | Weissgerber, Milic, Winham & Garovic 2015, PLoS Biol
    13(4) e1002128
  Version 1 star: all five lost; centre moved; x spread grew; y spread "shrank by almost a quarter" | Verified
    (50.00/50.00/20.51/20.50/0.00 on screen; s_y −23.9 %, s_x +22.4 %) | our construction; facts #4
  Averages = balance point; SDs = box ±1 SD | Verified | definition
  1-SD ellipse is inscribed in the box and touches the right wall at ȳ + r·s_y; r → 1 sends it to the corner |
    Verified (support function of Σ in direction (1,0) is s_x, attained at μ + (s_x, r s_y)) | re-derived
  "At minus point oh six, that's just below the middle" | Verified (47.832 − 0.0645·26.935 = 46.10, 1.74 below) |
    computed
  "That ellipse is everything the five numbers know" | Verified ((μ, Σ) ↔ 1-SD ellipse is one-to-one for |r| < 1) |
    re-derived
  Slide / stretch / shear each fix their own numbers; "all five match now, to every decimal place" | Verified
    (translation moves only means; scaling about the mean moves only SDs, r scale-invariant; the shear
    w' = a u + b w with a² + b² + 2ab r_s = 1 keeps var and sets r) | re-derived
  Median y: dino 46.02, our star 52.16, "misses it by six" | Verified (46.0256; Δ 6.14) | numpy; facts #11
  Matejka & Fitzmaurice 2017 (CHI): a search that holds chosen statistics; random nudges biased toward a target;
    kept only if the stats hold to 2 dp; dinosaur → circle | Verified | research.autodesk.com/publications/
    same-stats-different-graphs; CHI '17 pp. 1290–1294
  "twelve shapes"; star, bullseye, X, stripes, dots shown | Verified (13 sets in the TSV = dino + 12) | datasauRus
  "Every one of them has this same ellipse and a different median" | Verified (all 13 truncate to 54.26 / 47.83 /
    16.76 / 26.93 / −0.06; medians: star 50.11, bullseye 47.38, x_shape 39.87, h_lines 50.47, dots 51.29, circle
    51.02, all ≠ 46.02) | numpy
  Anscombe 1973, eleven points | Verified | Am. Stat. 27(1):17–21
  Anscombe r = 0.82; all four share x̄ 9.00, ȳ 7.50, s_x 3.32, s_y 2.03, r 0.82 | Verified (r 0.8162–0.8165;
    s_y 2.0304–2.0317) | numpy
  OLS slope = cov/s_x² = r s_x s_y / s_x² = r s_y / s_x; the line passes through the centre and the touch point;
    0.82·2.03/3.32 ≈ 0.50 | Verified (0.5001 unrounded; 0.5014 from the rounded display; OLS fits for I–IV:
    0.5001, 0.5000, 0.4997, 0.4999) | re-derived; numpy
  Landing: "the line you pictured was its line" (dashed guess line = the five-number OLS line, slope −0.104) |
    Verified (polyfit on dino: −0.1036, intercept 53.45) | numpy
MECHANICS: runtime 3:37.0 · wpm 162 (speech time), 153 overall · max silence 1.96 s (1:39.1, planned prediction
  hold) · max static 3.5 s (1:37.6–1:41.1, planned) · −14.1 LUFS / −2.0 dBTP · lead 0.00 s / trail 1.85 s ·
  WER 2.5 %
FIXES (highest impact first):
1. [1:19.3–1:27.4][Clarity] The r·s_y rule is asserted, not shown ("It always sits r times s y above the center").
   Everything downstream depends on it: the slope identity at 3:03–3:11 ("the rise to the touch point over the run
   to the wall") only reads the assertion back, so a viewer cannot re-derive why the line passes through the touch
   point.
   - Give the one-line reason the viewer already half-knows: correlation means "one SD right, r SDs up, on
     average". Replace the sentence with: "Correlation r means one standard deviation to the right, r standard
     deviations up. So the touch point on the right wall sits r times s y above the center."
   - Picture: during the existing sweep, start from the r = 0 ellipse (touch at the middle). Draw the run from the
     centre to the right wall as a thin YELLOW segment labelled s_x (the same object that returns at 3:05), then
     grow the rise r·s_y from its end.
   - This makes the 2:59–3:11 derivation a confirmation of something the viewer saw, not a second assertion.
2. [1:14.9–1:19.3][Clarity] "The correlation picks the one ellipse that touches all four walls" reads as "only one
   ellipse touches all four walls", which is false: a one-parameter family does.
   - Change it to "Many ellipses touch all four walls. The correlation picks one."
   - On "many", flash two GREY ghost ellipses (touch heights ±0.5·s_y, 40 % opacity, 0.8 s) inside the box. Fade
     them on "picks one".
3. [0:09.5–0:21.3 and 3:24.4–3:35.2][Hook] The commit is spoiled by the title. Anyone who clicked "A Dinosaur
   Hiding in Your Summary Statistics" knows the cloud guess is wrong, so the prediction carries no tension. The
   genuinely surprising half of the payoff is that the viewer's line guess was exactly right, and the narration
   leaves that implicit.
   - At 0:09.5, sharpen the prompt to one committable quantity: "Picture the scatterplot. Now draw its best-fit
     line: which way does it tilt, and how steeply?" Keep the 1.5 s hold.
   - At the landing, replace "The cloud you pictured at the start was this ellipse, and the line you pictured was
     its line." with "Your line was exactly right: five numbers fix it. Your cloud was this ellipse." Pulse the
     dashed line on "exactly right".
   - Keep "The dinosaur lived in everything they leave out."
   - This turns the ending into a reversal (right about the line, wrong about the shape) instead of a restatement.
4. [0:26.2–0:37.6 → 3:30][Hook/Payoff] The stakes beat (86 % of papers draw a bar, 13 % show points) is never paid
   off. After 0:38 the real-world consequence disappears, and the episode ends on a 1973 toy dataset rather than
   on the practice it indicted.
   - Insert after "All that five numbers can draw." (3:30.5): "A bar graph draws two." (about 1.3 s).
   - On it, TransformFromCopy the ellipse's centre and its vertical half-axis into the YELLOW ȳ bar and ±s_y error
     bar from 0:33, at the same position, for 1 s, then fade back before "The dinosaur lived…".
   - Net runtime change is about +1.5 s; cut the same from fix 8.
5. [1:37.6–1:41.1][Visual] At the prediction hold ("How would you fix the star?", frame 1:40.0) the two boxes,
   two ellipses and the star outline make five crossing yellow, red and blue curves. That is the moment the viewer
   must read "red is off-centre, wider, shorter".
   - During the hold, dim both boxes to 30 %.
   - Keep the two ellipses and the two centre dots at full opacity.
   - Restore the boxes on "Stretch it until the boxes match" (1:43.4).
6. [0:31.0–0:38.0][Visual] The "86%" beside the bar and the "13%" beside the points have no referent on screen, so
   a muted viewer, or anyone rewatching the frame, cannot tell what they count.
   - Change the labels to "86% used bars" and "13% showed points" (Text 26, grey, 3 words each, same anchors).
7. [3:16.6–3:17.2][Motion] In the quartet hand-off, the zoomed Anscombe axes (y 4–10) and panel I's new axes
   (y 0–15) are both visible for about 0.5 s (strip frame at 3:16.8), so two sets of tick labels overprint.
   - ReplacementTransform the zoomed axes into panel I's axes, so one set of ticks morphs.
   - Alternatively, finish the FadeOut of the old axes before panels II–IV begin to FadeIn.
8. [2:38.0–2:45.9 and 1:03.1–1:05.0][Concision] Two sentences restate what the picture already carries.
   - Trim "with 11 points and 5 numbers of his own" to "with eleven points of his own". The five readout symbols
     glide in on screen; the "five numbers" callback comes at 3:14.6.
   - Cut "Go back to the dinosaur." The points visibly return, and the next sentence names the dinosaur's balance
     point.
   - Saves about 3 s, which covers fix 4.
9. [2:24.2–2:34.8][Audio] The roll call uses four identical 1.6 s pauses, and almost every sentence boundary in
   the episode is exactly 0.5 s (44 of the 63 listed silences). The result is a metronomic, recognisably
   synthetic cadence.
   - Vary the roll-call pauses to 1.2 / 1.5 / 1.0 / 1.4 s.
   - Set sentence gaps by weight: 0.3 s inside a thought (for example, "Two averages, two standard deviations" →
     "and a correlation"), 0.7–0.9 s at beat boundaries (0:26.2, 1:00.0, 1:54.2, 2:38.0, 3:24.4).
10. [0:14.1–0:17.7][Clarity, nit] "A shapeless, roundish cloud" does not match the tall oval drawn (kf_03 @ 0:19.4,
    vertical spread about 1.6× the horizontal). Say "A shapeless oval cloud".
REACHES 9 IF ALL FIXED: yes, narrowly. Fixes 1–2 take Clarity to 9, fixes 3–4 take Hook to 9, fixes 5–6 take Visual
  to 9, fix 9 takes Audio to 9 and fix 8 takes Concision to 9. With Motion at 9 and Originality staying 8.5, the
  weighted score is (135 + 225 + 135 + 135 + 90 + 90 + 85)/100 = 8.95 → 9.0.
  Originality is the ceiling: the Datasaurus is among the most reproduced examples in data visualisation. The
  episode's fresh angle is the ellipse-in-a-box lens and the "your line was right" reversal (fix 3). Making that
  reversal explicit is the one change that could lift Originality to 9 and give margin above the threshold. No
  structural change is needed.
KEEP:
  - The ellipse-in-the-SD-box geometry, carried from the dinosaur (1:05) through the fixed star and the Dozen to
    the slope derivation (3:03–3:11), where the rise r·s_y and the run s_x fly from the fraction onto the picture.
    This is the episode's real insight.
  - The SMH loop on live data: version one fails by a measured amount (0/5, s_y −24 %), then slide / stretch /
    shear each turn their own rows green, and the sixth number (the median, off by six) shows where the fix still
    fails.
  - The landing that carries the ellipse home onto the opening frame and grows the yellow line over the dashed
    "your line".
```

## Notes behind the scores

- **Hook 8.5.** The first frame is concrete: empty axes, n = 142 and five empty slots. There is a prediction
  prompt with a 2.0 s hold (0:12.1–0:14.1), and the dinosaur reveals at 0:21. Tension rises through the failure
  at 0:51 (0/5) and the fix, and the ending returns to the opening frame exactly.
  - Deductions: the title gives away the reveal, so the commit is low-stakes; and the stakes beat (0:26–0:38) is
    never paid off.
- **Clarity 8.5.**
  - Every number checks out; I recomputed all of them independently. All four sources are correct. The
    truncation convention is disclosed on screen. The derivation 2:51–3:11 (cov/s_x² → r s_y/s_x → rise/run) is
    clean and built on the picture.
  - Deductions: the touch-point rule at 1:23.9 is asserted with "always", with no reason; "the one ellipse" at
    1:14.9 misstates uniqueness; and the ellipse's meaning in data terms is never said.
  - None of these is a factual error, so no cap applies.
- **Visual 8.5.**
  - The palette is semantic and held for 3:37: YELLOW summary, BLUE data, RED drifted, GREEN match, with every
    red and green paired with ≠ or =.
  - Citations sit bottom-left, and the readouts are aligned and legible.
  - Deductions: the busy prediction-hold frame (1:40), the referentless percentages (0:31–0:38), and the zoomed
    Anscombe axes having a different aspect from the quartet's (59.5 vs 89.5 px per unit at 2:42.9), which makes
    the slope-0.5 line look steeper than 0.5.
- **Motion 9.** The animation carries the argument. Points travel by minimum-travel assignment into each real
  dataset, the readout is computed live from the points, the nudge is acted out and rejected (2:09–2:16), each
  fix moves only its own rows, TransformMatchingTex runs cov → r s_x s_y → r s_y, and the rise and run fly onto
  the plot. The only blemish is the 0.5 s double-axes crossfade at 3:16.8.
- **Audio 8.5.**
  - Pace is 162 wpm on speech time, loudness and peak are on target, and the names Matejka, Fitzmaurice and
    Anscombe are heard correctly. "r times s y" is now unambiguous, and the deictics land.
  - Deduction: the uniform 0.5 s sentence gaps and the 4 × 1.6 s roll-call pauses make the cadence mechanical.
- **Concision 8.5.** At 3:37 this runs long for one idea. The Dozen gallery (2:21–2:38) and the quartet
  (3:14–3:24) make the same "same ellipse, different shape" point twice. The second earns its place only through
  the line, so I judge under 10 % removable.
- **Originality 8.5.** The subject is famous, but the lens is not: the inscribed 1-SD ellipse, the touch point at
  r·s_y and the regression line through it are textbook (Freedman–Pisani–Purves territory) but almost never shown
  in Datasaurus videos. No slop.
