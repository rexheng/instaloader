EPISODE: 020 — "A Dinosaur Hiding in Your Summary Statistics"  (round 7, substance / science-and-story editor)
IDEA: Two means, two SDs and a correlation pin down exactly one ellipse (a centre, a box, and a touch point that lies on the best-fit line), so any cloud with that ellipse, whether a dinosaur, a star or Anscombe's four sets, has the same five numbers and the same line, and only a plot shows the shape.
SCORES: Hook 9 · Clarity 8.5 · Visual 8.5 · Motion 9 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.7   AFTER CEILING: 8.7 (lowest 8.5 + 2 = 10.5, so the ceiling does not bind)
CAPS: none. Every spoken and on-screen number was recomputed and is correct. All four citations were verified against primary or publisher pages. There are 0 banned phrases or patterns. Every mechanical stat is in range, and the layout audit is clean (0 issues in 227 checks).
FINAL: 8.7   PASS: no

Evidence used: review/ pack (metrics.json 19:17, newer than final.mp4 19:15), report.md, all 12 contact sheets, and 14 full-resolution keyframes (kf_01, 07, 10, 14, 15, 17, 19, 23, 25, 29, 30, 32, 35, 38, 39). I also extracted extra frames at 0:30.6, 0:31.0, 0:34.8, 0:35.2, 1:11.5–1:14.8 (5-frame strip), 1:25, 1:29, 2:48.8, 2:54.9, 2:55.3 and 3:11.5. I read transcript.txt, narration.txt, script.md and facts.md, and independently recomputed the statistics with numpy from datasaurus_dozen.tsv, anscombe.csv and the star/fix functions in scene.py.

FACTS:
- Dinosaur n = 142; x̄ 54.26, ȳ 47.83, s_x 16.76, s_y 26.93, r −0.06 | Verified | numpy: 54.2633, 47.8323, 16.7651, 26.9354, −0.0645 (sample SDs; first two decimals, as published)
- "drawn by Alberto Cairo", on screen "Alberto Cairo, 2016 · The Functional Art" | Verified | Autodesk Research page ("Albert[o] Cairo created the Datasaurus dataset"); Cairo's Aug 2016 Functional Art post
- "review of 703 physiology papers, 86% used bar graphs … only 13% showed the points"; on screen "Weissgerber et al., 2015 · PLOS Biology" | Verified | PLOS Biol 13(4):e1002128: n = 703, top 25% of physiology journals; "85.6% of papers included at least one bar graph"; "13.4% … at least one univariate scatterplot"
- Version-one star: centre moves, x spread grows, "y spread shrank by almost a quarter"; on screen 50.00 / 50.00 / 20.51 / 20.50 / 0.00 | Verified | recomputed from scene.py star_spots(50,50,40,0.45,142): s_y −23.9 %, s_x +22.4 %
- Two means give the balance point, the two SDs give the box, and the 1-SD covariance ellipse is inscribed in the box, touching the right wall at ȳ + r·s_y | Verified | derivation: the support of (v−μ)ᵀΣ⁻¹(v−μ)=1 in direction (1,0) is s_x, attained at μ + (s_x, r s_y)
- "Many ellipses touch all four walls. The correlation picks one." | Verified | centred ellipses inscribed in a fixed box form a one-parameter family indexed by the touch height
- "One SD right, on average the cloud rises r times [s_y]"; the best-fit line passes through the midpoints of vertical chords of the ellipse, and through the touch point | Verified | the chord midpoint at x is ȳ + r(s_y/s_x)(x − x̄), which equals the OLS line
- Touch point "just below the middle" for the dinosaur | Verified | ȳ + r s_y = 46.10, which is 1.74 below 47.83
- Fixed star: "all five match now, to every decimal place" | Verified | recomputed differences ≤ 3.6e-14
- "add a sixth number, the median of y. Our star misses it by six" (46.02 vs 52.16) | Verified | numpy: 46.0256 vs 52.1617, a gap of 6.14
- Matejka & Fitzmaurice 2017 (CHI): a search that holds the five numbers while nudging points toward a target; "12 shapes" | Verified | Autodesk page: "12 shapes to direct the dots towards", "means, standard deviations, and correlations remain the same to two decimal places"; CHI 2017, doi:10.1145/3025453.3025912
- On-screen medians circle 51.02, star 50.11, bullseye 47.38, X 39.87, stripes 50.47; "each one has a different median" | Verified | numpy; all 12 differ from 46.02 (the closest are wide_lines 46.27 and slant_down 46.40)
- Anscombe 1973, eleven points; all four share x̄ 9.00, ȳ 7.50, s_x 3.32, s_y 2.03, r 0.82 | Verified | anscombe.csv: r 0.8164/0.8162/0.8163/0.8165, s_y 2.0316/2.0317/2.0304/2.0306; The American Statistician 27(1):17–21
- Anscombe touch point at 7.50 + 0.82·2.03 = 9.16 and box 5.68–12.32 × 5.47–9.53 (kf_29, kf_30) | Verified | measured against the tick positions
- slope = r s_y / s_x; landing "slope minus point one", on screen (−0.06 × 26.93)/16.76 ≈ −0.10 | Verified | −0.0964 from the displayed values; −0.1036 unrounded; polyfit(dino) −0.1036
- "Most of those papers used a bar graph, which draws only two" | Verified | 85.6 % is "most"; a bar plus error bar encodes a mean and one spread number (SD or SE)
- The simulated r = 0.80 cloud is labelled "simulated" (kf_14, kf_15) | Verified | facts #36; labelled on screen

MECHANICS: runtime 3:29.1 · wpm 152 (speech time; 137 overall) · max silence 2.37 s (0:10.3–0:12.7, the planned commit hold) · max static 2.77 s · −14.2 LUFS / −4.1 dBTP · leading 0.00 s / trailing 1.94 s · WER 2.6 % (only spelled-symbol and homophone differences) · 0 banned phrases · deictics 12/12 landed

TRANSCRIPT / SLOP: I checked for every §4 phrase and pattern and found 0. The four questions (0:06, 0:37, 1:00, 1:52) are each standalone, so there is no chain. "A trend, a curve, an outlier, and one point doing all the work" is a concrete list, not an abstract-adjective triplet. There are no fake reveals, no "it turns out" and no recap ending. The hook lands at 0:06–0:10 with an explicit two-part commit and a 2.4 s hold. The ending re-uses the cold-open frame ("your guess", "your line", kf_35) and resolves both halves of the question: the line was right, the cloud was wrong.

BEAT MAP vs §6:
- Cold open 0:00–0:12, with the puzzle on frame 1 (kf_01).
- Reveal and stakes 0:12–0:37.
- Naive build and fail 0:37–1:00, measured as 0/5 with −24 % in s_y (kf_10, sheet 4).
- Insight 1:00–1:49: the ellipse built from the numbers.
- Fail replay, prediction pause and fix 1:49–2:09.
- Honest limit 2:09–2:16: the median misses by 6.
- Payoff 2:16–3:08: Matejka & Fitzmaurice, then Anscombe.
- Landing 3:08–3:29.

The structure is complete and well ordered.

WHAT HOLDS IT BELOW 9 (with evidence):
- Clarity, the what-if readout contradicts the picture (1:21.5–1:41; kf_14, kf_15, sheet 5 at 1:23–1:29, sheet 6 at 1:31). A cloud tagged "simulated, r = 0.80" fills the plot, but the "now" column still reads r = −0.06 next to a full-strength green "=". The r row is dimmed, but the = glyph and "matching 5/5" are not. "now" is meant to describe the points on screen, and for 20 s it describes points that are not on screen. A first-time viewer is told two different correlations for the one cloud they are looking at.
- Clarity, an ambiguous SD (1:23.4–1:30.8). "Go one standard deviation right. On average, the cloud rises r times a standard deviation." The only SD just named is the horizontal one, so "a standard deviation" invites "r·s_x". The ambiguity is resolved only 8 s later by "r times ess why" at 1:38.6, and the review kit flags that phrase as a repeat of 2:50.3.
- Clarity, an over-general sentence (1:30.8–1:35.5). "That's the best-fit line, through the middle of every vertical slice" is true of the ellipse's chords, which are what is drawn at 1:33–1:35. For real data such as the dinosaur, the OLS line does not pass through the middle of every slice. One extra noun ("of the ellipse") makes the sentence exactly right.
- Visual, the landing frame is overloaded (3:24.5–3:29; kf_38, kf_39). The last frame has eight elements: blue dinosaur, 60 % ellipse, 60 % line, bar, error bar, "86% used bars", the five-row readout and the citation. The line "which draws only two" is not tied to the two readout rows by more than a brief flag, so the eye has no single landing point besides the dinosaur.
- Concision (2:40.8–3:08.9). The Anscombe block is a second instance of the Datasaurus Dozen point, which the narration concedes with "made the same point". It earns its place by deriving slope = r s_y/s_x, but "so they share the ellipse and line" (3:00.3–3:02.9) narrates what the four copied ellipses and lines already show. The B8 line "reach one deviation out on each side" (1:09–1:15.5) is tautological.
- Audio. The voice speed is 0.82–0.84 with a median sentence pace of 178 wpm, and the densest stretch (B9b, 1:21.5–1:44) has a 6.7 s run without a ≥ 0.35 s breath starting at 1:23.4 (report, Narration craft). That is the beat that most needs room. I cannot hear the audio, so I make no further deduction.
- Hook nit, not scored down. The title already says "dinosaur", so the 0:19 reveal is pre-announced. The commit still works, because the viewer is asked to picture a shape and a tilt, not to guess "dinosaur".

FIXES (highest impact first):
1. [1:21.5–1:42][Clarity/Visual] The "now" column says r = −0.06 with a bright green "=" while the on-screen cloud is labelled r = 0.80 (kf_14). On "Say r is point eight", fade the whole "now" column, all five =/≠ glyphs and "matching 5/5" to 25 % together with the dinosaur column's r row, so the only live r on screen is the yellow "r = 0.80" tag. Restore them on "For the dinosaur" as r sweeps back to −0.06. Keep the yellow 60 % geometry as it is. This removes the one contradictory frame in the episode (Clarity +0.25, Visual +0.25).
2. [1:25.9–1:30.8 and 1:35.5–1:40.8][Clarity/Concision] Change "On average, the cloud rises r times a standard deviation." to "On average, the cloud rises r times ess why." On "ess why", fly a copy of the s_y readout symbol to the rise as it grows, using the same carry() as B8. Then change "At the wall, the slices shrink to the touch point, r times ess why above the center." to "At the wall, the slices shrink to the touch point." This kills the ambiguity at first use, removes the kit's repeated phrase (1:38.6 / 2:50.3) and saves 6 words, about 2 s. Keep the "r s_y" label written beside the rise.
3. [1:30.8–1:35.5][Clarity] Change "That's the best-fit line, through the middle of every vertical slice." to "That's the best-fit line, through the middle of every slice of the ellipse." This adds 2 words, and the statement is then exactly true (chord midpoints of the 1-SD ellipse lie on the OLS line, facts #26) without implying that the dinosaur's own slices are centred on it.
4. [1:23.4–1:30.8][Audio] Add [pause 0.4] after "Go one standard deviation right." and set B9b's voice speed to 0.80. This breaks the 6.7 s breathless run, so the run and the rise each get their own beat while the band of 12 white points converges (1:27–1:29). Fix 2 pays for the time.
5. [2:57.2–3:08.9][Concision] Change "All four of his datasets share these five numbers, so they share the ellipse and line. [pause 0.5] A trend, a curve, an outlier, and one point doing all the work." to "All four of his datasets share these five numbers. [pause 0.5] A trend, a curve, an outlier, and one point doing all the work." Keep the ellipse and line copies arcing to panels IV, III and II, because they say "share the ellipse and line" without words. This saves about 2.5 s.
6. [1:08.9–1:15.5][Concision] Change "The two standard deviations reach one deviation out on each side, and draw a box." to "The two standard deviations reach out on each side, and draw a box." This drops the tautological "one deviation" and saves 2 words. The arm-lighting and wall-growing animation stays.
7. [3:20.0–3:29.0][Visual] On "which draws only two", fade the x̄, s_x and r readout rows to 30 % and leave ȳ and s_y at full strength until the end card. The two surviving rows are then literally the two numbers the parked bar draws, and the final frame reads as dinosaur, two numbers and bar, instead of eight competing elements (kf_39).
8. [0:31.5–0:37.0][Clarity] The error bar is drawn as ±1 s_y, while 77.6 % of the reviewed bar graphs showed ±SE (Weissgerber 2015). For n = 142, SE is about 12× narrower. Nothing said is wrong, but add a 26-pt grey tag "± 1 SD" beside the error bar's top cap at 0:33.0 (hold through 0:37). The picture then cannot be read as "the error bar these papers drew". Repeat the tag on the parked bar at 3:24.
9. [0:00–0:12][Hook, optional] If the series title is not locked, retitle the episode so it does not pre-announce the reveal, for example "What Five Numbers Can't See". The current title gives away the 0:19 payoff. This is a nitpick and is not needed for 9.

REACHES 9 IF ALL FIXED: yes, narrowly. Fixes 1–3 remove the only three places a careful viewer would stumble, which lifts Clarity to 9. Fixes 1 and 7 lift Visual to 9. Fixes 2, 5 and 6 cut about 6 s of words the screen already carries, which lifts Concision to 9. Fix 4 lifts Audio to 9. With Hook, Motion and Originality at 9, the weighted score is 9.0. No structural change is needed: the misconception commit, measured failure, one-picture insight, "how would you fix it?" iteration, honest limit (median), sourced payoff and cold-open callback are all present and all correct.

KEEP:
- The five-numbers-are-one-ellipse picture: box from the SDs, touch point on the best-fit line via the shrinking vertical chords (1:04–1:44). It is the episode's original contribution and it is mathematically exact.
- The StuffMadeHere arc: the naive star at 0/5 with −24 % s_y, a live red ellipse replayed against the yellow one, then slide, stretch and tip with the counter climbing to 5/5, then the median missing by 6 (0:45–2:16).
- The landing on the cold-open frame: the dashed "your line" overwritten by the exact yellow line, "your cloud was wrong", and the ellipse squeezed into the bar's error bar (3:08–3:24).
