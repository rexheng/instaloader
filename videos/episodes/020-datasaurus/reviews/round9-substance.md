EPISODE: 020 — "A Dinosaur Hiding in Your Summary Statistics"  (round 9, substance: science and story editor)
IDEA: Two means, two SDs and a correlation pin down exactly one ellipse (a centre, a box, and touch points that sit on the best-fit line), so any shape with that ellipse (a dinosaur, a star, the Datasaurus Dozen, Anscombe's four) has the same five numbers and the same line, and only a plot shows the shape.
SCORES: Hook 9 · Clarity 8.5 · Visual 8.5 · Motion 9 · Audio 9 · Concision 8.5 · Originality 9
WEIGHTED: 8.8 (135 + 212.5 + 127.5 + 135 + 90 + 85 + 90 = 875 / 100 = 8.75)   AFTER CEILING: 8.8 (lowest 8.5 + 2 = 10.5, so the ceiling does not bind)
CAPS: none. Every number I recomputed is correct. All four citations check out. The transcript has 0 banned phrases or patterns. Every mechanical stat is in range.
FINAL: 8.8   PASS: no

Evidence: I used the review/ pack, because metrics.json (23:03) is newer than final.mp4 (23:01).
- Read: report.md, narration_diff.txt, transcript.txt, all 12 contact sheets, narration.txt, script.md, facts.md, final.srt.
- Full-resolution keyframes: kf_01, 07, 09, 16, 18, 22, 25, 30, 32, 35, 38, 40.
- Extra frames I extracted with ffmpeg: 0:35.6, 1:34.6, 1:35.3, 2:42.3, 2:42.8, 2:43.2, 2:47.6, 2:52.6, 2:53.0, 2:53.4.
- Recomputed with numpy from the episode's datasaurus_dozen.tsv (all 13 sets) and anscombe.csv (all 4 sets). I also rebuilt the naive version-one star (outer radius 40, inner radius 0.45 R, 142 evenly spaced spots).
- Read scene.py's `fix` and the transition code. Interpolated frames are re-imposed onto the five numbers by `fix(lerp(A,B,a), lerp(sA,sB,a))`, so the "=" marks during the morphs are honest.
- Web-verified (Firecrawl): the Weissgerber et al. PLOS Biology page, and the Autodesk Research "Same Stats, Different Graphs" page plus the CHI 2017 listing.

FACTS:
- Dinosaur: n = 142, x̄ 54.26, ȳ 47.83, s_x 16.76, s_y 26.93, r −0.06 | Verified | numpy gives 54.2633, 47.8323, 16.7651, 26.9354, −0.0645, shown as the first two decimals, matching the on-screen note "first two decimals, as published". The Autodesk page lists the same values.
- "Drawn by Alberto Cairo", shown as "Datasaurus: Alberto Cairo, 2016 · The Functional Art" | Verified | The Autodesk page credits "Albert[o] Cairo" with creating the Datasaurus and links his Aug 2016 Functional Art post.
- "In a review of 703 physiology papers, 86% used bar graphs … Only 13% showed the points", cited as "Weissgerber et al., 2015 · PLOS Biology" | Verified | The PLOS Biol 13(4): e1002128 page: n = 703; "85.6% of papers included at least one bar graph"; "13.4% of articles included at least one univariate scatterplot". The "± 1 SD" tag discloses our convention (most bars in the review were ± SE).
- Version-one star: centre (50, 50), s_x 20.51, s_y 20.50, r 0.00; "the y spread shrank by almost a quarter" | Verified | My rebuild gives 50.00 / 50.00 / 20.51 / 20.51 / 0.00. 26.935 → 20.51 is −23.9 %, and s_x rises 22 %.
- "Many ellipses touch all four walls. The correlation, r, picks one." | Verified | Re-derived. A centred ellipse tangent to x̄ ± s_x and ȳ ± s_y has inverse shape matrix [[s_x², c], [c, s_y²]] with |c| < s_x s_y, which is a one-parameter family with c = r s_x s_y. It touches the right wall at ȳ + r s_y.
- "Go one SD right; on average the cloud rises r times s_y. That's the best-fit line, through the middle of every slice of the ellipse." | Verified | The OLS slope is cov / s_x² = r s_y / s_x. The midpoint of a vertical chord of the 1-SD ellipse is ȳ + r(s_y/s_x)(x − x̄). The r = 0.50 cloud is tagged "simulated", and its touch height is 47.83 + 0.5 · 26.94 = 61.30.
- "For the dinosaur, it's just below the middle" | Verified | 47.832 − 0.0645 · 26.935 = 46.10, which is 1.74 below the centre.
- "All five match now, to every decimal place" | Verified | The tip map w' = a u + b w with b = √((1−r_t²)/(1−r_s²)) and a = r_t − b r_s keeps var(w') = 1 and sets corr = r_t. I re-derived it.
- "Our star misses [the median of y] by six" | Verified | 52.16 − 46.02 = 6.14.
- Matejka & Fitzmaurice, 2017, CHI: a search that keeps the five fixed while nudging points toward a target; twelve shapes grown from the dinosaur | Verified | Autodesk page: random small moves are kept only if the statistics stay the same "to two decimal places" and the point moves closer to the target (simulated annealing); "we created 12 shapes to direct the dots towards". CHI 2017, Denver.
- On-screen medians: circle 51.02, bullseye 47.38, X 39.87, stripes 50.47 vs dino 46.02 | Verified | numpy gives 51.0250, 47.3829, 39.8762, 50.4735 and 46.0256. All twelve Dozen medians differ from 46.02.
- Anscombe 1973, eleven points; all four share x̄ 9.00, ȳ 7.50, s_x 3.32, s_y 2.03, r 0.82; "same line" | Verified | r is 0.8164 / 0.8162 / 0.8163 / 0.8165, s_y is 2.0316 / 2.0317 / 2.0304 / 2.0306, and slopes are 0.5001 / 0.5000 / 0.4997 / 0.4999. Set IV has a single point at x = 19. The American Statistician 27(1):17–21.
- Landing: slope = (−0.06 × 26.93) / 16.76 ≈ −0.10, "minus point one" | Verified | That is −0.0964 from the displayed values and −0.1036 unrounded. polyfit on dino gives −0.1036.
- "Most of those papers used a bar graph, which draws only two." | Verified | 85.6 % is "most". A bar plus one error bar encodes a mean and one spread number. The squeezed 1-SD ellipse is exactly ȳ ± s_y.
- Nit, not an error. "Five numbers fix it exactly" is true of the exact numbers. Across the 13 Dozen sets, which agree only to two decimals, the slope ranges from −0.097 to −0.112. No line on screen claims otherwise.

MECHANICS: runtime 3:22.3 · 150 wpm over speech time (134 overall; median sentence 173) · max silence 2.37 s (0:10.3–0:12.7, the planned commit hold) · max static 2.30 s · −14.1 LUFS / −1.6 dBTP
- Leading silence 0.00 s, trailing 1.94 s.
- WER 1.4 %. The only differences are spelled symbols ("oh" heard as zero, "ess why" heard as S-Y) and a possessive.
- 0 black frames. The layout audit reports 0 issues in 216 checks. Deictics landed 12 of 12.

TRANSCRIPT / SLOP:
- 0 §4 phrases.
- No question chains: the four questions at 0:06, 0:38, 1:02 and 1:54 each stand alone.
- No "it turns out", no fake colon reveals and no recap ending. "A trend, a curve, an outlier, and one point doing all the work" is concrete, not an adjective triplet.
- The hook is on frame 1 (kf_01: empty axes, "?", n = 142, the five values). The prediction prompt ends at 0:10.4, followed by a 2.4 s hold.
- The landing (3:01–3:20, kf_35, kf_38) re-uses the cold-open frame and resolves both halves of the prediction. The line was right (fixed by the five numbers); the cloud was wrong.

BEAT MAP vs §6:
- cold open 0:00–0:12
- reveal and stakes 0:12–0:38
- naive build and measured fail 0:38–1:02 (0/5; s_y −24 %)
- insight 1:02–1:50 (ellipse from the numbers; the slope formula now built here, at 1:34–1:36)
- replay, prediction pause and fix 1:50–2:12
- honest limit 2:12–2:18 (median off by 6)
- payoff 2:18–3:01 (Matejka & Fitzmaurice, then Anscombe)
- landing 3:01–3:20, then the end card

The structure is complete, and the round-8 complaint (formula emerging only in the payoff) is fixed.

WHAT HOLDS IT BELOW 9 (with evidence):
1. Clarity and Concision: the crux beat is overloaded, and its key link is never spoken (1:21.7–1:46).
   - In 24 s, B9b covers a what-if r, a simulated cloud, a slice average landing on the touch dot (1:29–1:33), the best-fit line, a formula assembled silently in a 1.1 s pause (frames 1:34.6 and 1:35.3 show the labels flying), five ellipse slices (1:36–1:40), the slices collapsing at the wall (1:40–1:42), and the return to the dinosaur.
   - The fact "the touch point lies on the best-fit line" is shown twice in 12 s: first by the slice average (the white dot turns into the touch dot at about 1:32), then by the slices shrinking at the wall.
   - The narration never says what the formula on screen says ("rise over run, r s_y over s_x"), and never states the conclusion the slices are there for ("so the line runs through the touch point").
   - From 2:48, "Same rule, same line" relies on the viewer having decoded all this. This is the one transition a first-time viewer needs to rewatch.
2. Clarity, story logic: the median beat points at the wrong fix (2:12–2:41).
   - "But add a sixth number: the median of y. Our star misses it by six." is followed by "Each one has this same ellipse, and a different median."
   - A viewer can leave with "so report the median too". The episode's own thesis, and its landing "everything they leave out", says no finite list of numbers is enough.
   - The cited paper says so directly. Its method is "agnostic to the particular statistical properties that are to remain constant", and the Autodesk page's boxplot example holds the median and quartiles fixed while the distributions differ.
   - One clause would close the gap. As cut now, the honest-limit beat slightly undercuts the payoff.
3. Clarity and Visual: a bare "0.82" is parked beside Anscombe's touch dot during a silent 1.2 s pause (frame 2:47.6). The dot sits at y = 9.16 on the 4–10 axis, so "0.82" next to it reads as a coordinate or a label for the dot. What it means is "r: the dot is 0.82 of the way up the half-box". Nothing on screen or in the narration says so.
4. Visual and Motion: transient coordinate clutter at two hand-offs.
   - About 2:42.5–2:43.3 (frame 2:42.8): the dinosaur's 0–100 tick numbers and Anscombe's 4–12 numbers are both near full opacity, stacked ("10" over "75", "8" over "50", "4" over "25"; the x-axis reads "0 4 25 8 50 … 100"). For roughly 0.8 s the plotted points carry two scales.
   - About 2:52.9–2:53.1 (frame 2:53.0): panel I's moving "20" sits on panel II's "0", and panel I's origin reads "00".
   - Both are mid-motion, so I apply no cap, but they are the only frames in the episode that would not survive a screenshot.

What is excellent and earns the 9s:
- The cold open commits the viewer by 0:10.
- The fail is measured on a live readout (0/5, then 1/5, 2/5, 4/5, 5/5 as slide, stretch and tip land at 2:00–2:08).
- The "five numbers = one ellipse" picture is genuinely the canonical way to see what Pearson summaries keep.
- The landing re-sees frame 1 exactly and ties the bar graph back to "only two" of the five.

FIXES (highest impact first):
1. [1:33–1:46][Clarity/Concision] Make the crux beat say what it shows, and drop the duplicated proof.
   - Replace "That's the best-fit line, [pause 1.1] through the middle of every slice of the ellipse. [pause 0.7] At the wall, the slices shrink to the touch point. [pause 0.4] For the dinosaur, it's just below the middle." with "That's the best-fit line: [pause 0.4] rise over run, r ess why over ess ex. [pause 0.8] For the dinosaur, the touch point sits just below the middle."
   - Time the build to the words: the s_x label drops into the denominator on "ess ex", and the r s_y copy flies to the numerator on "r ess why".
   - Cut the five-slice draw and slide (about 1:36–1:42). The slice average landing on the touch dot at 1:29–1:33 already proves the touch point is on the line.
   - This saves about 5 s and 8 words, puts the formula in speech as well as on screen, and lets "Same rule, same line" at 2:48 land on something the viewer heard. Clarity goes to 9 and Concision to 9.
2. [2:38–2:41][Clarity] Close the "just add the median" escape.
   - Change "Each one has this same ellipse, and a different median." to "Each one has this same ellipse. The same search can pin a median too." (Supported: Matejka & Fitzmaurice 2017 abstract, "agnostic to the particular statistical properties…", and the boxplot example, Fig. 7.)
   - Keep the live median row as is. The words now say the median is not a cure, which is what the landing claims.
3. [2:46.5–2:48.5][Clarity/Visual] Do not fly a bare "0.82" to the touch dot. Either:
   - (a) during the pause, draw Anscombe's rise from ȳ to the touch dot and fly "r = 0.82" from the readout to sit beside it as "r s_y" (the label the viewer learned at 1:31), or
   - (b) cut the flight and let "Same rule" draw the run and rise as now.
   Either way, nothing on the plot should read as a coordinate it isn't.
4. [2:42.5–2:43.3][Visual/Motion] Stop the two tick scales stacking (frame 2:42.8). Fade the 0–100 numbers fully out (0.3 s) before the 4–12 numbers fade in. Better: let the old numbers ride their ticks to their new positions and fade, as the 2:53 hand-off already does with ticks.
5. [2:52.8–2:53.2][Visual] Panel I's travelling "20" collides with panel II's "0", and panel I's origin shows a doubled "00" (frame 2:53.0). Start panel II's tick-number fade-in only after panel I's transform has passed 0.8, or fade panel I's old numbers out before the move starts.
6. [0:25–0:38][Clarity, nit] "Only thirteen percent showed the points" paraphrases "included at least one univariate scatterplot". It is accurate enough, but "showed their individual points" would match the study's measure exactly at no cost.

REACHES 9 IF ALL FIXED: yes.
- Fix 1 alone lifts Clarity and Concision to 9 (weighted 8.9).
- Fix 1 plus fixes 3–5 lift Visual to 9, giving a weighted score of about 9.0–9.1.
- Fix 2 removes the remaining story-logic doubt.
No structural change is needed: the hook, the measured failure, the one picture and the landing are all in place and correct.

KEEP:
- The cold-open frame and the landing that re-uses it. "Your line was right … Your cloud was wrong" resolves both halves of the opening question with the same axes, readout and dashed line.
- The live dinosaur / now readout with =/≠ marks through the version-one fail and the slide / stretch / tip fix. It is a measured, Stuff-Made-Here-grade failure and repair.
- The ellipse-in-the-box built from the numbers (1:05–1:21), and the closing squeeze of the ellipse into the ± s_y error bar ("which draws only two").
