EPISODE: 020 — "A Dinosaur Hiding in Your Summary Statistics"   (review round 4, substance / science-and-story editor)
IDEA: Two means, two SDs and a correlation fix exactly one ellipse (a centre, a box, and the height where the ellipse touches the box), so any shape built around that ellipse (a dinosaur, a star, Anscombe's four sets) has the same five numbers and the same best-fit line. Only a plot shows the shape.
SCORES: Hook 8.5 · Clarity 9 · Visual 8.5 · Motion 9 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.8 (8.75)   AFTER CEILING: 8.8 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none
FINAL: 8.8   PASS: no

Evidence used: review/ pack (metrics.json 23:13:41 is newer than final.mp4 23:11:23, so it was reused). I read report.md, all 13 contact sheets and keyframes kf_01, 05, 09, 14, 17, 19, 22, 30, 31, 34 and 38. I also extracted frames at 0:09.5, 0:34.5, 1:01.5, 1:09.0, 1:41.5, 2:29–2:33 (a 5-frame strip), 2:56.8, 3:35.0 and 3:41.5. Every number below was recomputed with numpy from datasaurus_dozen.tsv and anscombe.csv, and both stars were rebuilt from the construction in scene.py. Citations were checked by web search (PLOS Biology article page, Autodesk Research page, ResearchGate full text).

FACTS:
- Dinosaur n = 142; x̄ 54.26, ȳ 47.83, s_x 16.76, s_y 26.93, r −0.06 | Verified | numpy: 54.2633, 47.8323, 16.7651, 26.9354, −0.0645. These are the first two decimals, truncated, as published, and the on-screen note "first two decimals, as published" says so.
- All 13 Dozen sets share those five numbers to two decimals ("this same ellipse") | Verified | the truncated values are identical in all 13 sets; the spread is ≤ 0.010 on every statistic.
- "A different median" for every shape; star, bullseye, X, stripes and dots shown with 50.11, 47.38, 39.87, 50.47 and 51.29 against 46.02 | Verified | numpy medians: 50.1106, 47.3829, 39.8762, 50.4735, 51.2993; dino 46.0256.
- Version-one star: centre moved, x spread grew, y spread "shrank by almost a quarter"; shown 50.00 / 50.00 / 20.51 / 20.50 / 0.00 | Verified | rebuilt star: (50.000, 50.0007), s_x 20.513 (+22.4 %), s_y 20.509 (−23.9 %), r ≈ 0.
- Slide / stretch / shear fixes all five "to every decimal place" | Verified | rebuilt fixed star: differences from the dinosaur ≤ 7e−15.
- "Our star misses [the median] by six" | Verified | 52.1617 − 46.0256 = 6.14.
- Nudge illustration at 2:13 (x̄ → 54.22, s_x → 16.68, both ≠) | Verified | the point (91.28, 41.54) stepped 5.5 toward (54.27, 47.84) gives 54.2251, 47.8388, 16.6862, 26.9340, −0.0638.
- Ellipse geometry: box x̄ ± s_x by ȳ ± s_y; touch height ȳ + r s_y; at r = −0.06 "just below the middle" | Verified | derivation: the 1-SD covariance ellipse has horizontal support s_x, reached at (x̄ + s_x, ȳ + r s_y); 47.83 − 0.0645 × 26.94 = 46.10, which is 1.74 below the centre.
- "Correlation r means one SD right, on average r SDs up" | Verified (it is the regression reading of r, not its definition; "means" is loose but standard: Freedman, Pisani & Purves, ch. 10).
- OLS slope = cov/s_x², cov = r s_x s_y, so slope = r s_y/s_x, which is rise to the touch point over run to the wall | Verified | derivation; Anscombe I: 5.501/11.0 = 0.5001.
- Anscombe: 11 points per set, r = 0.82, s_x 3.32, s_y 2.03, x̄ 9.00, ȳ 7.50, shared by all four; slope "one half" | Verified | r 0.8164/0.8162/0.8163/0.8165; s_y 2.0316/2.0317/2.0304/2.0306; polyfit slopes 0.5001/0.5000/0.4997/0.4999; 0.82 × 2.03 / 3.32 = 0.501.
- Dinosaur best-fit line, "nearly flat" (dashed "your line") | Verified | r s_y/s_x = −0.1036; polyfit −0.1036, intercept 53.45.
- "Datasaurus: Alberto Cairo, 2016 · The Functional Art" | Verified | Cairo's Aug 2016 blog post; the Autodesk page credits him with the Datasaurus.
- Weissgerber et al., 2015 · PLOS Biology: 703 physiology papers, 86 % used bar graphs, 13 % showed the points | Verified | PLOS Biology 13(4):e1002128: n = 703; 85.6 % had ≥ 1 bar graph; 13.4 % had ≥ 1 univariate scatterplot.
- Matejka & Fitzmaurice, 2017 · CHI: a search that holds whatever statistics you choose; random nudges biased toward a target shape, kept only if the stats hold to two decimals; the Datasaurus is the starting set for the 12 shapes | Verified | Autodesk Research page ("biasing the random point movements toward a particular shape", "same to two decimal places", "12 shapes"); paper text ("datasaurus as the initial dataset"); the abstract says the method is agnostic to which statistics are held.
- Anscombe, 1973 · The American Statistician | Verified | 27(1):17–21.
No wrong, fabricated or uncited claims.

MECHANICS: runtime 3:42.3 · wpm 160 (speech time; 151 overall; 185 with all pauses removed) · max silence 1.96 s (the 1:40.8 prediction hold) · max static 2.97 s · −14.0 LUFS / −1.7 dBTP · leading silence 0.00 s, trailing 1.83 s · WER 3.1 % (the one inserted "those" at 3:34.0 lasts 20 ms in the word timings, so it is a whisper artifact, not a stutter) · banned phrases 0. I also searched by hand for every §4 pattern: no question chains (each question stands alone), no "it turns out", no fake reveals, no adjective triplets.

What works (the reason this is close): the cold open has numbers on screen in frame 1 and a commit by 0:11.5, with a 1.9 s hold over the "?". The stakes are real and sourced (0:25–0:37). Version one fails by a measured amount, shown live in red with ≠ (0:47–0:59). The insight is built from objects already on screen: dot, then cross, then box, then ellipse, with the r sweep at 1:17–1:31. The fix is SMH-style (slide, stretch, shear, with the counter going 2/5 → 4/5 → 5/5 at 1:45–1:53). An honest limit follows (the median misses by 6, 1:57). The roll call keeps the ellipse visibly fixed while the median wanders (2:25–2:37), and the slope is derived on Anscombe and confirmed on four panels. The landing reverses the opening: "Your line was exactly right… Your cloud was this ellipse." The ellipse squeezes into the ±s_y error bar (3:35–3:38), which pays off the stakes beat geometrically. The colour semantics hold all the way through (YELLOW summary, BLUE data, RED drift, GREEN =).

Why it is not yet a 9:
- Hook 8.5: the question is "Which way does their best-fit line tilt, and how steeply?" (0:08). The "how steeply" half is never answered with a number for the dinosaur. The slope −0.10 appears nowhere; the only computed slope is Anscombe's 0.50 (3:13). So "Your line was exactly right" (3:25) asserts a match the viewer never sees quantified. The narrator also supplies the guess for the viewer ("…is the reasonable guess", 0:13–0:18).
- Clarity 9 (nitpicks only): at 1:23 "So the touch point… sits r times s y above the center" follows from "on average r SDs up" only if the viewer sees that the touch point is where the best-fit line crosses the right wall. That link is said only at 3:08. The nudge demo (2:11–2:17) shows only a rejected step, never an accepted one, so "repeat it enough times" (2:19) asks the viewer to believe something is ever kept.
- Visual 8.5:
  - The digits 16.76 and 26.93 visibly smear into scribbles while morphing into the cross arms (frame 1:09.0).
  - The copied cov(x,y) passes through the numerator, giving a double-printed "cov(x, y)" (frame 2:56.8).
  - After the sweep returns to −0.06, "r s_y" labels a rise of about 25 px that you can barely see (kf 1:32.7).
  - The prediction hold (frame 1:41.5) still stacks 142 full-opacity star points, two ellipses, two dimmed boxes and four dots in one 4-unit area.
- Audio 8.5: loudness, pace and deictics check out. "this X" and "these stripes" land on their shapes (frames 2:30.0–2:33.0). But whisper heard 1:45.0–1:59.2 as one unpunctuated 14 s run ("…boxes match Then tip it… same height All five match now… But add a sixth number…"), so the four sentences there run together. Speed without pauses is 185 wpm.
- Concision 8.5: at 3:42 the episode sits at the top of the band.
  - B7–B8 (1:02–1:11) re-explain a centre dot and SD cross that have been on screen since 0:55–1:01.
  - The regression reading of r (1:16–1:28) and the cov/var derivation (2:50–3:10) explain the same fact twice, 90 s apart.

FIXES (highest impact first):
1. [3:25–3:29][Hook] Answer "how steeply" with a number so the ending resolves the opening exactly.
   - On "five numbers fix it", TransformFromCopy r, s_y and s_x from the readout into "slope = r s_y / s_x ≈ −0.10" (MathTex 40, YELLOW). Place it above-right of the dashed line, in the empty area x ∈ [1.0, 3.5], y ≈ 0.9 (screen units).
   - Hold it ≥ 2.8 s; it can ride under "Your cloud was this ellipse".
   - Narration: "Your line was exactly right: slope minus point one, fixed by five numbers." (+1 s)
   - Values check: −0.06 × 26.93 / 16.76 = −0.096 → −0.10; unrounded −0.1036.
   - Hook goes 8.5 → 9.
2. [1:16–1:31][Clarity] Make the touch point visibly the place where the best-fit line meets the wall, so the "So" is shown, not asserted.
   - Replace "So the touch point on the right wall sits r times s y above the center." with "That's where the best-fit line meets the right wall, r times s y above the center, and that's where the ellipse touches it."
   - During the 0 → 0.80 sweep, draw a thin YELLOW segment (stroke 2, 60 % opacity) from the centre through the live touch dot to the right wall. It is the same line that grows at 3:08 and 3:27.
   - Fade the segment with the run and rise at 1:32.6.
   - The 3:04–3:08 derivation then confirms something already seen.
3. [2:13–2:19][Clarity] Show one accepted nudge after the rejected one, so "repeat it enough times" is believable.
   - After the 5.5-unit step is undone (2:15), keep the ring and step the same point 0.3 units toward the circle centre.
   - Recomputed: the truncated readout stays 54.26 / 47.83 / 16.76 / 26.93 / −0.06, all =, while a 0.5 step already breaks x̄ and s_x.
   - Indicate the = column and leave the point where it landed.
   - Narration: insert "Tiny steps pass." after "…hold to two decimals." (about 1 s). Offset the time with fixes 5 and 10.
4. [1:09.0][Visual] The digit-to-arm morph smears 16.76 and 26.93 into scribbles.
   - Make the copies shrink and fade (FadeOut with scale 0.3) toward the arm ends while each arm Indicates.
   - Or TransformFromCopy each number into a small YELLOW dot at its arm tip, then GrowFromCenter the arm.
   - Do not morph glyph outlines into line segments.
5. [1:02–1:11][Concision] B7–B8 re-explain the cross drawn at 0:55–1:01. Merge them: "The averages mark the balance point; the standard deviations, a box one deviation out on each side." Saves about 3 s. Keep the flights of the four values onto the dot and arms.
6. [2:56.8][Visual] The copy of cov(x,y) leaves through the numerator, so two overlapping "cov(x, y)" glyph sets show.
   - First shift the copy straight down 0.7 units (0.4 s) before it travels to the side line.
   - Or build the side line's cov(x,y) with FadeIn(shift=DOWN) beside the numerator instead of copying it through.
7. [1:39.3–1:42.7][Visual] The prediction hold is cluttered.
   - Dim the star points to 40 % during "How would you fix the star? [pause 1.5]", together with the boxes already at 30 %.
   - Keep both ellipses and both centre dots at full opacity, then restore the points on "Slide".
8. [1:28.9–1:32.5][Visual] After the sweep returns to −0.06, "r s_y" labels an invisible 25 px rise. Transform the label into "r s_y ≈ −1.7" on "minus point oh six" (−0.0645 × 26.94 = −1.74), so "just below the middle" has a number. Or fade the label there.
9. [1:45–1:59][Audio] The four sentences run together. Add [pause 0.35] after "the boxes match." and [pause 0.4] after "at the same height." Lengthen the pause before "But add a sixth number" from 0.8 to 1.0 s. That costs about 1 s; take it from fix 10.
10. [2:50–3:10][Concision] Once fix 2 is in, the derivation only needs to confirm. Shorten it to "Least squares sets the slope to the covariance over the x variance. The covariance is r times s x times s y, so one s x cancels: rise over run, through that touch point." Keep the strike-through animation. Saves about 3 s.

REACHES 9 IF ALL FIXED: yes, narrowly. Fix 1 takes Hook to 9; fixes 4 and 6–8 take Visual to 9; fixes 5 and 10 take Concision to 9; fixes 2–3 make Clarity solid at 9 (possibly 9.5). That gives 9 × 15 + 9 × 25 + 9 × 15 + 9 × 15 + 8.5 × 10 + 9 × 10 + 9 × 10 = 8.95 → 9.0 even if Audio stays at 8.5. No structural change is needed. The hook, the failure beat, the visual insight and the reversing landing are all in place.
KEEP:
- The commit-then-reversal frame: the cloud and dashed "your line" at 0:13–0:18, paid off by "Your line was exactly right… Your cloud was this ellipse" at 3:25–3:31.
- Version one fails live in red with ≠ and a 0/5 counter, then is fixed by slide, stretch and shear, with the counter climbing to 5/5 (0:47–1:53).
- The landing's ellipse squeezing into exactly the ±s_y error bar on the ȳ bar (3:35–3:38), with the dinosaur returning around it.
