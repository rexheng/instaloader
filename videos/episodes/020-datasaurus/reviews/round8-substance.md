EPISODE: 020 — "A Dinosaur Hiding in Your Summary Statistics"  (round 8, substance / science-and-story editor)
IDEA: Two means, two SDs and a correlation pin down exactly one ellipse (a centre, a box, and a touch point that lies on the best-fit line), so any shape with that ellipse (a dinosaur, a star, Anscombe's four sets) has the same five numbers and the same line, and only a plot shows the shape.
SCORES: Hook 9 · Clarity 9 · Visual 8.5 · Motion 9 · Audio 9 · Concision 8.5 · Originality 9
WEIGHTED: 8.9 (887.5 / 100 = 8.875)   AFTER CEILING: 8.9 (lowest 8.5 + 2 = 10.5, so the ceiling does not bind)
CAPS: none. I recomputed every spoken and on-screen number and all are correct. All four citations check out on publisher or primary pages. There are 0 banned phrases or patterns. Every mechanical stat is in range, and the layout audit reports 0 issues in 222 checks.
FINAL: 8.9   PASS: no

Evidence used: the review/ pack. Its metrics.json (21:34) is newer than final.mp4 (21:32). I read report.md, all 12 contact sheets, and 14 full-resolution keyframes (kf_01, 07, 08, 12, 17, 19, 23, 26, 32, 33, 35, 38, 39, 40). I also extracted frames at 0:20.3, 0:34.6, 0:35.2, 0:35.8, 1:39.0, 2:27.6, 2:28.2, 2:38.6, 2:39.4, 2:40.2, 2:51.0, 2:55.0, 3:02.8 and 3:03.6. I read transcript.txt, transcript_words.tsv (1:33–1:51), narration.txt, script.md and facts.md. I recomputed the statistics with numpy from datasaurus_dozen.tsv (all 13 sets) and anscombe.csv (all 4 sets).

FACTS:
- Dinosaur: n = 142, x̄ 54.26, ȳ 47.83, s_x 16.76, s_y 26.93, r −0.06 | Verified | numpy gives 54.2633, 47.8323, 16.7651, 26.9354 and −0.0645 (sample SDs, first two decimals as published). All 13 Dozen sets truncate to the same five values.
- "Drawn by Alberto Cairo", shown on screen as "Datasaurus: Alberto Cairo, 2016 · The Functional Art" | Verified | The Autodesk Research page says "Albert[o] Cairo created the Datasaurus" and links his Aug 2016 Functional Art post.
- "In a review of 703 physiology papers, 86% used bar graphs … only 13% showed the points", on screen "Weissgerber et al., 2015 · PLOS Biology" | Verified | PLOS Biol 13(4): e1002128 (journals.plos.org, PubMed 25901488): n = 703; "85.6% of papers included at least one bar graph"; "13.4% … at least one univariate scatterplot". The "± 1 SD" tag correctly marks our convention (most of the reviewed bar graphs used ± SE).
- Version-one star: 0/5 match, readout 50.00 / 50.00 / 20.51 / 20.50 / 0.00, "the y spread shrank by almost a quarter" | Verified | 26.935 → 20.509 is −23.9 %; s_x is +22.4 % (facts #4, consistent with the frames at 0:51–0:59).
- Balance point, box, "Many ellipses touch all four walls. The correlation, r, picks one." | Verified | Centred ellipses inscribed in the box [x̄ ± s_x] × [ȳ ± s_y] form a one-parameter family. The 1-SD covariance ellipse touches the right wall at ȳ + r·s_y (its support in direction (1, 0) is attained at μ + (s_x, r s_y)).
- "Go one standard deviation right. On average, the cloud rises r times ess why. That's the best-fit line, through the middle of every slice of the ellipse." | Verified | The midpoint of a vertical chord at x is ȳ + r(s_y/s_x)(x − x̄), which is the OLS line of y on x. At the wall the chord collapses to the touch point. The simulated r = 0.50 band is tagged "simulated", and the touch height 47.83 + 0.5·26.94 = 61.30 is correct.
- "For the dinosaur, it's just below the middle" | Verified | 47.832 − 0.0645·26.935 = 46.10, which is 1.74 below the centre.
- Fixed star, "All five match now, to every decimal place" | Verified | facts #10: differences ≤ 3e-14. The slide, stretch and tip map keeps the other moments (I re-derived the tip map in facts #9).
- "Add a sixth number, the median of y. Our star misses it by six." (46.02 vs 52.16) | Verified | 46.0256 vs 52.1617 is a gap of 6.14.
- Matejka & Fitzmaurice, 2017, CHI: a search that keeps the five fixed while it nudges points toward a target; "12 shapes" | Verified | Autodesk page and CHI 2017 (doi:10.1145/3025453.3025912): simulated annealing, statistics held to two decimals, the Datasaurus turned into 12 target shapes.
- On-screen medians: circle 51.02, star 50.11, bullseye 47.38 (shown mid-transition as 47.71 at 2:29), X 39.87, stripes 50.47; "each one has … a different median" | Verified | numpy gives 51.025, 50.111, 47.383, 39.876 and 50.474, which truncate to the on-screen values. All 12 differ from 46.02.
- Anscombe 1973, eleven points; all four sets share x̄ 9.00, ȳ 7.50, s_x 3.32, s_y 2.03, r 0.82; "a trend, a curve, an outlier, one point doing all the work" | Verified | anscombe.csv gives r 0.8164 / 0.8162 / 0.8163 / 0.8165 and s_y 2.0316 / 2.0317 / 2.0304 / 2.0306. Set IV has a single point at x = 19. The citation The American Statistician 27(1):17–21 checks out (JSTOR 2682899).
- slope = r s_y / s_x; Anscombe's touch point at 7.50 + 0.82·2.03 = 9.16 | Verified | OLS b = cov/s_x² = r s_y/s_x. polyfit on set I gives 0.5001 = 0.8164·2.0316/3.3166.
- Landing "slope minus point one", on screen (−0.06 × 26.93)/16.76 ≈ −0.10 | Verified | That is −0.0964 from the displayed values and −0.1036 unrounded. polyfit on dino gives −0.1036, intercept 53.45.
- "Most of those papers used a bar graph, which draws only two." | Verified | 85.6 % is "most". A bar plus error bar encodes one mean and one spread number. The squeezed 1-SD ellipse is exactly ȳ ± s_y.

MECHANICS: runtime 3:24.7 · wpm 150 (speech time; 136 overall; median sentence 173) · max silence 2.37 s (0:10.3–0:12.7, the planned commit hold) · max static 2.73 s · −14.1 LUFS / −1.7 dBTP · leading 0.00 s, trailing 1.94 s · WER 2.4 % (only spelled-symbol and homophone differences: "oh"/"zero", "ess why"/"S-Y", "dinosaur's"/"dinosaurs") · 0 banned phrases · deictics 12/12 landed · 0 black frames · layout audit 0 issues

TRANSCRIPT / SLOP: I checked for every §4 phrase and pattern and found 0.
- The four questions (0:06, 0:37, 1:00, 1:49) each stand alone, so there is no question chain. The cold-open question has two clauses but is one prompt.
- There are no fake reveals, no "it turns out", no empty superlatives and no recap ending. "A trend, a curve, an outlier, and one point doing all the work" is concrete, not an adjective triplet.
- The hook lands at 0:00–0:10, with the puzzle on frame 1 (kf_01) and a 2.4 s commit hold.
- The landing reuses the cold-open frame (kf_35: "your guess", "your line", the same readout) and resolves both halves of the question. Five numbers do fix the line; they cannot draw the cloud.
- Every round-7 substance fix is in this cut:
  - The "now" column and the = marks are dimmed during the r = 0.50 what-if (kf_17, kf_19).
  - The narration says "r times ess why".
  - The narration says "slice of the ellipse".
  - B9b is slowed to 0.80 with a pause.
  - The tautology and the Anscombe redundancy are cut.
  - The x̄, s_x and r rows step back on "only two" (kf_39).
  - The "± 1 SD" tag is on screen.

BEAT MAP vs §6:
- Cold open 0:00–0:12.
- Reveal and stakes 0:12–0:37.
- Naive build and measured fail 0:37–1:00: 0/5, with −24 % in s_y.
- Insight 1:00–1:45: the ellipse built from the numbers.
- Replay, prediction pause and fix 1:46–2:07.
- Honest limit 2:07–2:12: the median misses by 6.
- Payoff 2:12–3:03: Matejka & Fitzmaurice, then Anscombe.
- Landing 3:03–3:24.
The structure is complete. The only §6 deviation is that the formula slope = r s_y/s_x emerges in the payoff (2:49–2:53), not in the insight beat where its picture was built (1:22–1:37).

WHAT HOLDS IT BELOW 9 (with evidence):
- Visual and Motion, the dozen-to-Anscombe rescale (2:38.6–2:40.2). The tick numbers cross-fade to Anscombe's 4/8/12 and 4–10 about 0.8 s before the data moves. In the frame at 2:39.4, the Dozen's stripes, the dinosaur's box and ellipse, and the bright "x̄ = 54.26" readout all sit under axis numbers that place them at x ≈ 5–15, y ≈ 4–11. For about a second the plotted data is labelled with the wrong scale. The relation between old and new coordinates is cross-faded, not transformed.
- Visual, the single-panel to quartet hand-off (2:54.6–2:55.4). In the frame at 2:55.0, Anscombe I's old 4–12 axes ghost under panel I's new 0–20 axes. The ellipse and the points sit outside the new panel: one point is below its x-axis at about (264, 695) px, and another is left of it. Two coordinate systems share one frame.
- Visual, a doubled label (2:50.6–2:51.4). In the frame at 2:51.0, the bright "r s_y" climbing to the numerator has a 20 % source copy of itself 70 px below, so the label reads twice.
- Visual, the stakes hand-off (0:34.6–0:35.8). In the frame at 0:35.2, "13% / showed po…" is being written while "± 1 SD", the error bar, the bar and "86% used bars" are still at about 40 %. Three label blocks stack within 70 px, over a visible error bar.
- Concision and structure, the second derivation (2:44.4–2:53.4). "Same rule: ess ex across, r times ess why up. So the slope is the rise over the run." applies the B9b rule again to Anscombe I, because slope = r s_y / s_x was never written when the run and rise were first drawn (1:22–1:31, kf_17/kf_19 show "s_x" and "r s_y" on the run and rise with no formula). Writing the formula there puts it in the insight beat, where §6 wants it, and lets Anscombe be a 15 s payoff instead of a 26 s re-teach.
- Audio nit, not scored down. The longest run without a breath is 6.3 s (0:25.1–0:31.3), and it carries 703 and 86 % back to back. That is the busiest 20 s for numbers. I cannot hear the track, and the transcript renders every number correctly, so I make no deduction.
- Clarity nit, not scored down. "Say r is point five" (1:20.2) comes with no reason, though the reason (−0.06 is too flat to see a rise) is the whole point of the what-if.
- Hook nit, not scored down. The title says "dinosaur", which pre-announces the 0:19 reveal. The commit still works, because it asks for a shape and a tilt, not a guess.

FIXES (highest impact first):
1. [2:38.6–2:40.2][Visual/Motion] The axis numbers swap to Anscombe's scale before the data moves, so the Dozen's stripes and the "x̄ = 54.26" readout sit under 4–12 ticks (frame 2:39.4). Fade the 131 non-Anscombe points and the dinosaur's box and ellipse first (0.4 s). Then put the 11 points' travel, the box and ellipse retarget, and the tick-number swap in one AnimationGroup with the same rate_func, so the ticks move with the data. Never show new tick numbers next to old-scale data. This fix lifts Visual.
2. [2:54.6–2:55.4][Visual] At 2:55.0, Anscombe I's old 4–12 axes ghost under the new 0–20 panel, and a point sits below the panel's x-axis. Transform the old axes and ticks into panel I's axes in the same animation that moves the 11 points, ellipse and line, as the 3:03 hand-off already does with ReplacementTransform on the axes. Alternatively, fully fade the old axes (≤ 0.3 s) before anything moves.
3. [1:29.3–1:31.3 and 2:44.4–2:53.4][Concision/Clarity] Build "slope = r s_y / s_x" in B9b on "That's the best-fit line" (1:29.3). Use the same carry() moves that now run at 2:49–2:53: r s_y from the rise label to the numerator, s_x from the run label to the denominator, placed top right over the plot's empty upper-right area and held through 1:41. Let it dim to 40 % and stay in the corner until Anscombe. Then replace B20 and B21 ("Same rule: ess ex across, r times ess why up. So the slope is the rise over the run.") with "Same rule, same line." Keep the 0.82 flight to the touch dot, draw the line through it as the formula flags, and cut the run, rise and label rebuild at 2:45–2:53. This saves about 7 s, and the formula emerges from its picture in the insight beat (§6), not in the payoff.
4. [2:50.6–2:51.4][Visual] A dim 20 % duplicate "r s_y" sits under the bright copy as it climbs (frame 2:51.0). If fix 3 is not taken, move the label itself (Transform into the numerator slot) instead of TransformFromCopy with the source at 20 %, or fade the source to 0 within 0.2 s of the copy leaving. If fix 3 is taken, apply the same rule to the B9b build.
5. [0:34.6–0:35.8][Visual] "13% showed points" writes in over the fading "± 1 SD", bar and error bar (frame 0:35.2). Finish the FadeOut of the bar, error bar, "± 1 SD" and "86% used bars" in 0.4 s starting on "Only" (0:34.2), and start Write("13% / showed points") on "showed" (about 0:35.5), so the two label sets never share a frame.
6. [0:25.1–0:31.3][Audio] The 6.3 s breathless run carries 703 and 86 %. Add [pause 0.3] after "physiology papers," and set B2's voice speed to 0.80, so each number gets its own beat. Fix 3 pays for the time.
7. [1:20.2][Clarity, optional] Change "Say r is point five." to "Too flat to see. Say r is point five." (+4 words, about 1.2 s; fix 3 pays for it). The what-if then has a stated reason, and the later "For the dinosaur, it's just below the middle" lands as a return.
8. [Title][Hook, optional] If curriculum.json allows it, use a title that does not pre-announce the 0:19 reveal (for example "What Five Numbers Can't See"). This is not needed for 9.

REACHES 9 IF ALL FIXED: yes. Fixes 1, 2, 4 and 5 remove the four transition frames where the picture contradicts itself or doubles up, which lifts Visual to 9. Fix 3 removes the one re-taught beat and moves the formula to where its picture is built, which lifts Concision to 9 and holds Clarity at 9. The weighted score then becomes (9 × 100) / 100 = 9.0. No structural change is needed. The misconception commit, the measured failure, the one-picture insight, the "how would you fix it?" iteration, the honest limit (the median), the sourced payoff and the cold-open callback are all present, and every claim is correct.

KEEP:
- The five-numbers-are-one-ellipse picture: centre, then the SD box, then r picking one ellipse, then the touch point reached by the simulated slice average and the shrinking chords (1:04–1:41). It is mathematically exact and it is the episode's original contribution.
- The StuffMadeHere arc: the naive star at 0/5 with −24 % s_y, the red ellipse replayed against the yellow one, slide, stretch and tip to 5/5, then the median missing by 6 (0:45–2:12), with a live readout throughout.
- The landing on the cold-open frame: the dashed "your line" overwritten by the exact yellow line, "your cloud was wrong", the ellipse squeezed into the ± 1 SD error bar, and the two numbers a bar keeps (3:03–3:24).
