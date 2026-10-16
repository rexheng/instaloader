# Episode 20, review round 2 (substance: science and story editor)

**Evidence.** I used the `review/` pack, because metrics.json (13:34) is newer than final.mp4 (13:32). I read:
- report.md and all 12 contact sheets;
- transcript.txt, narration_diff.txt, script.md, narration.txt, facts.md and CHANGELOG.md.

Full-resolution keyframes I read: kf_01 (0:03.5), kf_04 (0:21.1), kf_05 (0:28.2), kf_09 (0:39.7), kf_11 (0:46.2), kf_14 (0:53.1), kf_18 (1:26.1), kf_20 (1:39.3), kf_24 (2:01.4), kf_29 (2:24.6), kf_35 (3:07.3) and kf_36 (3:16.7).

I extracted extra frames with ffmpeg at 1:08.6, 1:36.0, 2:38.8, 2:57.6, 2:58.4, 2:59.2, 3:00.8 and 3:09.0, plus a 3× crop of the s_x label at 3:06.0.

Numbers:
- I recomputed all 13 Datasaurus sets (means, SDs, r, y-median, OLS slope) and all 4 Anscombe sets with numpy from the episode's data files.
- I rebuilt the version-one star and the fixed star with scene.py's own `star_spots`, `match` and `fix`.

Citations: I checked Weissgerber et al. 2015 (PLOS Biology page) and Matejka & Fitzmaurice 2017 (Autodesk Research page) by web search and scrape.

```
EPISODE: 020 — "A Dinosaur Hiding in Your Summary Statistics"
IDEA: Two means, two SDs and a correlation fix exactly one ellipse (centre, box, side-wall touch height), so any shape with that ellipse (a dinosaur, a star, Anscombe's four sets) shares the five numbers and even the best-fit line; only a plot shows the shape.
SCORES: Hook 8 · Clarity 8.5 · Visual 8 · Motion 8.5 · Audio 8.5 · Concision 8 · Originality 8.5
WEIGHTED: 8.3   AFTER CEILING: 8.3 (lowest 8 + 2 = 10, not binding)
CAPS: Text overlapping another element → 7. At 3:00.8–3:08.5 (settled frame, kf_35 @ 3:07.3; 3× crop @ 3:06.0) the "s_x" run label sits on the yellow ellipse's lower arc. Its background patch erases about 25 px of the ellipse stroke, and its top edge is about 13 px (< 20 px) from the run segment.
  Checked and not triggered:
  - Banned phrases: 0. Banned patterns: no question chains (3 single questions at 0:40, 1:01, 1:36), no "it turns out", no recap ending.
  - Every empirical claim is cited on screen: Cairo 0:25, Weissgerber 0:29, Matejka & Fitzmaurice 2:05, Anscombe 2:37.
  - Factual errors: none (see FACTS).
  - Deictic misses: 1 ("these five numbers" @ 3:07–3:09, with no Anscombe numbers on screen), so the ≥ 2 sync cap does not apply.
  - Mechanics are all within limits.
FINAL: 7.0   PASS: no
FACTS:
  Dino n = 142 | Verified | datasaurus_dozen.tsv
  x̄ 54.26, ȳ 47.83, s_x 16.76, s_y 26.93, r −0.06 | Verified as truncated first two decimals (raw 54.2633, 47.8323, 16.7651, 26.9354, −0.0645); the "first two decimals, as published" note is on screen from 0:49 | numpy; Autodesk Research page
  "A dinosaur drawn by Alberto Cairo [2016]" | Verified | Autodesk page: "A special thanks to Alberto Cairo for creating the Datasaurus"; The Functional Art, Aug 2016
  "…with exactly these five numbers" (0:25) | Verified only under truncation (s_x 16.765 would round to 16.77, and the decimals note is not yet on screen); wording nit, not an error | numpy
  703 physiology papers; 86 % used bar graphs; 13 % showed the points | Verified (n = 703; 85.6 % had ≥ 1 bar graph; 13.4 % had ≥ 1 univariate scatterplot) | Weissgerber, Milic, Winham & Garovic 2015, PLoS Biol 13(4) e1002128
  Version-one star: 50.00, 50.00, 20.51, 20.50, 0.00; y spread −23.9 % ("almost a quarter"); x spread +22.4 % | Verified (rebuilt: 50.0000, 50.0001, 20.5133, 20.5089, −3.5e−17) | scene.py construction
  Means = balance point; SDs = box; the 1-SD ellipse touches the right wall at ȳ + r·s_y; r → 1 sends it to the corner; at r = −0.06 it sits 1.74 below centre (46.09) | Verified | support function of Σ; computed
  "That ellipse is everything the five numbers know" | Verified ((μ, Σ) ↔ 1-SD ellipse is one-to-one for |r| < 1) | derivation
  Slide, stretch and tip fix only their own numbers; fixed star matches "to every decimal place" | Verified (max |Δ| 2.8e−14) | rebuilt with scene.py fix()
  Median y: dino 46.02 vs fixed star 52.16, "misses it by six" | Verified (46.0256 vs 52.1617, Δ 6.14) | rebuilt
  Matejka & Fitzmaurice 2017, CHI: random nudges, biased toward a target shape, kept only if the stats hold to 2 dp; method works for any statistic; 12 shapes grown from the Datasaurus | Verified ("biasing the random point movements toward a particular shape"; "means, standard deviations, and correlations remain the same to two decimal places"; "we created 12 shapes to direct the dots towards") | research.autodesk.com/publications/same-stats-different-graphs; CHI '17 pp. 1290–1294, doi:10.1145/3025453.3025912
  "Every one of them has this same ellipse" | Verified (spread across all 13 sets ≤ 0.010 on every statistic) | numpy
  Anscombe 1973, 11 points, r 0.82; all four share the five numbers; trend / curve / outlier / one high-leverage point | Verified (r 0.8162–0.8165; s_y 2.0304–2.0317; s_x 3.3166) | Anscombe, Am. Stat. 27(1):17–21
  slope = cov/s_x² = r·s_y/s_x = 0.82 × 2.03 / 3.32 ≈ 0.50; the line passes through the centre and the touch point | Verified (0.5001 exact; 0.5014 from the shown roundings) | derivation; numpy
  Implied by sequence (1:53–2:35): the Matejka–Fitzmaurice search fixes the median miss | Misleading, not false. Their Dozen holds only the five numbers; y-medians range 32.50–51.30 across the 13 sets, 39.88 (X) to 51.30 (dots) among the shapes shown, vs dino 46.03 | numpy
MECHANICS: runtime 3:30.1 · wpm 159 (speech time) · max silence 1.98 s (1:38.2, planned) · max static 3.5 s (1:36.7–1:40.2, planned) · −14.0 LUFS / −1.6 dBTP · lead 0.00 s / trail 1.85 s
FIXES (highest impact first):
1. [3:00.8–3:08.5][Visual] The s_x run label overlaps the ellipse, and its background patch cuts the stroke (cap 7).
   - Delete the patch.
   - Put `s_x` (MathTex 40) below the left quarter of the run: `next_to(run.point_from_proportion(0.2), DOWN, buff=0.18)`. Check in code that its bounding box is ≥ 0.15 units from 200 sampled ellipse points.
   - If it still collides, zoom the Anscombe axes to x ∈ [4, 14] for this beat so the ellipse is larger.
   - Removes cap 7.
2. [1:16.7–1:30][Clarity] The episode never says how high the touch point sits, yet the derivation at 2:57.6 ("the rise to the touch point") silently assumes it is r·s_y.
   - Change B9 to: "The correlation sets how high the ellipse touches the side walls: r standard deviations above the centre."
   - On "r standard deviations", draw a thin yellow vertical segment from the centre line to the right touch dot, labelled `r\,s_y` (MathTex 36, buff 0.2), and keep it live through the sweep: 0.88·s_y up, then back to −0.06·s_y (just below).
   - At 2:59 the Anscombe rise segment is then a recognised object, and a viewer could re-derive the slope claim after one watch.
3. [1:53–2:35][Clarity/Story] The limit beat says our star misses the median, then introduces "a slower search that can hold any statistic". That implies the Datasaurus Dozen fixes the median, but it doesn't: their y-medians run 39.88 (X) to 51.30 (dots) among the shapes shown, against the dino's 46.02.
   - Make the honesty explicit and turn it into a payoff. Narration B16: "…a search that can hold whatever numbers you choose. They chose these five."
   - During B17, keep a grey live `med y` readout under the plot (MathTex 36, truncated like the others) that visibly jumps 50.11 → 47.38 → 39.88 → 50.47 → 51.30 as each shape lands, while the yellow ellipse stays still.
   - Add after "Every one of them has this same ellipse": "and a different median."
   - This also makes the cold-open lesson general: any finite list of numbers leaves shapes free.
4. [2:34.7–3:09][Clarity] Anscombe's five numbers are never shown, so three things land from nowhere:
   - 2.03 and 3.32 in "0.82 × 2.03 / 3.32" (3:05, white, though their symbols are yellow);
   - "these five numbers" (3:07.3–3:09), the episode's one deictic miss;
   - "share the ellipse".

   Fix:
   - When the Anscombe morph lands (2:39), write a compact yellow readout: "x̄ = 9.00, ȳ = 7.50" / "s_x = 3.32, s_y = 2.03" (MathTex 36), with r = 0.82 written on its word as now.
   - TransformFromCopy 0.82, 2.03 and 3.32 from it into the substitution, coloured yellow.
   - Indicate it on "these five numbers".
5. [0:00–0:15.8][Hook] The commit ("Picture the scatter plot and its best-fit line") ends at 0:13.8, against BAR's 0:12. The first frame is empty axes with "n = 142", which holds no tension. The title already says "dinosaur", so the reveal at 0:21 confirms rather than surprises.
   - Cut B0 to "A hundred and forty-two points. Five numbers: two averages, two standard deviations, and a correlation of minus point oh six. Picture the scatterplot, and its best-fit line." Drop "almost none", since the flat guess line already says it. That saves about 1.5 s and lands the commit by 0:12.
   - Keep the 1.5 s hold.
   - Make the line the stake the title can't spoil: hold the grey dashed line and add a one-word label "your line" so the landing (3:21) pays it off explicitly.
6. [2:01.4–2:13.3][Clarity/Motion] "A slower search" is an adjective where a measurement belongs, and the picture is static while "Nudge a point at random" is spoken (sheet 8, 2:09–2:11 identical).
   - Replace "used a slower search" with "ran two hundred thousand tiny nudges". This is verified: Autodesk page, "200,000 iterations of perturbations toward a 'circle' shape", which is the very target shown at 2:13.
   - Show a grey "nudges: 0 → 200,000" counter (MathTex 30) under the plot during the circle morph.
   - On "Nudge" (2:09.6), ring one point and step it; on "keep the nudge only if…" (2:13.5), Indicate the ellipse once.
7. [3:05–3:08.5][Visual] "≈ 0.50" reaches x ≈ 1862 px (6.68 units), beyond the 6.4-unit safe edge (1824 px).
   - Left-align the substitution under "slope =" with `next_to(slope_eq, DOWN, buff=0.5, aligned_edge=LEFT)`, or shift the equation block 0.5 units left.
   - Assert `get_right()[0] ≤ 6.2`.
8. [0:25.5–0:27.6][Clarity] "with exactly these five numbers" is exact only under truncation (s_x 16.765 rounds to 16.77), and the "first two decimals" note appears only at 0:49. Change "exactly" to "with these same five numbers", and save "every decimal place" for the fixed star (1:51), where it is literally true.
9. [0:31–0:40][Visual/Clarity] During the strip and bar, the x-axis still carries 0–100 ticks, but the strip is x compressed 0.12× toward x̄, so it reads as data at x ≈ 50–60. Dim the x ticks and the "x" label to 25 % for the strip and bar (0:31–0:40), and restore them as the dinosaur returns.
10. [1:53.3–1:56.9][Concision] "Those three moves only protect these five numbers." restates what the median row then shows. Merge it: "But add a sixth number, the median of y, and our star misses it by six." That saves about 3 s and funds fix 2's extra clause.
11. [3:16.6–3:18.6][Motion] The landing is a cross-dissolve through a near-empty frame while "The cloud you pictured" is spoken. Keep panel I's ellipse alive and ReplacementTransform it into the opening-plot ellipse (1.2 s), so "this ellipse" (3:19) refers to a carried object.
12. [2:38.5–2:39.5][Visual] Three of the 11 travelling Anscombe points pass through white or pale blue (frame @ 2:38.8), off the BLUE = data palette. Keep their fill BLUE throughout the morph.
REACHES 9 IF ALL FIXED: yes, narrowly.
  - Fix 1 removes the cap, which returns the episode to 8.3.
  - Fixes 2–4 and 8 lift Clarity to 9.
  - Fixes 1, 4, 7, 9 and 12 lift Visual to 9.
  - Fixes 6 and 11 lift Motion to 9.
  - Fix 5 lifts Hook to 9, and fix 10 lifts Concision to 8.5–9.
  - Weighted then lands around 8.9–9.0. Fix 3, the medians wandering under a fixed ellipse, is also the most likely lift for Originality, and the episode needs it to clear 9.
  - No structural change is required. The episode already has misconception → commit → reveal → measured v1 fail (0/5) → one picture (ellipse in a box) → three-move repair (0→2→4→5/5) → honest limit → sourced payoff → landing on the opening frame.
KEEP:
  - The ellipse assembled from the readout (1:06–1:30): balance point from the means, box from the SDs, touch point from r. It is exact, original and the episode's thesis.
  - The live "dinosaur | now" readout with =/≠ and the "matching k/5" counter through the fail and the slide-stretch-tip repair (0:47–1:53), plus the red live ellipse drifting off the yellow one on the replay (1:33–1:40).
  - The slope derivation that ends with the best-fit line growing through the touch point (2:45–3:07), paid off when the same line grows over the viewer's dashed guess (3:21–3:23).
```

## Notes on scoring

- **Hook 8.**
  - Concrete and number-first. The viewer is asked to picture the plot and the line, holds 1.9 s (0:13.9–0:15.8), and the ending re-sees the opening frame exactly (3:17–3:28).
  - Held below 9 because the commit lands at 0:13.8 (after 0:12), the first frame is empty axes, and the title gives away the dinosaur.
  - Tension rises through fail (0/5) and repair (5/5). It flattens after 1:53, when the question "how much can five numbers hide?" is answered and two demonstrations follow (the Dozen, then Anscombe).
- **Clarity 8.5.**
  - Every number checks out. Every source is real and correctly attributed. The ellipse picture is exact.
  - Deductions:
    - The touch height r·s_y is used at 2:57.6 but never established (1:16–1:30).
    - The median beat leads into a method whose outputs also miss the median, a misleading sequence (1:53–2:35).
    - Anscombe's numbers are substituted without ever being shown (3:05).
- **Visual 8.**
  - A strict semantic palette: yellow summary, blue data, red drift, green match, always paired with = and ≠. One background, correct citations bottom-left.
  - Deductions:
    - the s_x label overlapping the ellipse (3:00.8–3:08.5);
    - "≈ 0.50" outside the safe area (3:05–3:08.5);
    - a meaningless x-axis during the strip (0:31–0:40);
    - off-palette white points (2:38.8).
- **Motion 8.5.**
  - Objects persist and transform throughout: guess → dinosaur (0:21), dinosaur → strip → bar (0:31–0:37), readout copies into the centre dot (1:08), the live red geometry, the three verb-synced repair moves, the dozen with a frozen ellipse, panel I → quartet.
  - Deductions: a static picture under "Nudge a point at random" (2:09–2:13), and a cross-dissolve landing (3:16.6–3:18.6).
- **Audio 8.5.**
  - 159 wpm, −14.0 LUFS, −1.6 dBTP, WER 3.0 %. Names and terms are pronounced cleanly (Matejka, Fitzmaurice, "s x").
  - Deictics land ("this bullseye" 2:23 on the bullseye; "these dots" 2:31 on the dots), with one miss ("these five numbers" 3:07–3:09).
- **Concision 8.** Less than 10 % is removable: the "Those three moves only protect…" restatement (1:53–1:57), "almost none" (0:09.5), and some slack in the two back-to-back demonstration payoffs.
- **Originality 8.5.**
  - The Datasaurus and Anscombe are the most-shown examples in statistics teaching, which lowers the ceiling.
  - Three things lift it: the "five numbers = one ellipse in a box" framing, the hand-built affine star with a measured counter, and the guess line that turns out to be the line the five numbers force.
  - No slop in the transcript.
