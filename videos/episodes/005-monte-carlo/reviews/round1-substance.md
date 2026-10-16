# Episode 5, review round 1: substance (science and story editor)

Evidence: `review/` pack (metrics.json 12:28 is newer than final.mp4 12:26, so I reused it). I read report.md, all 12 contact sheets and 14 full-resolution keyframes (kf_01, 04, 05, 12, 14, 19, 22, 25, 28, 31, 34, 38, plus extracted frames at 0:50.0–0:52.4 (tiled), 1:08.5 (cube zoomed), 1:29.6, 2:36.6–2:38.2 (tiled), 2:44.0 and 3:24.0). I also read the transcript, the word timings, script.md, facts.md, narration.txt, sim.py and data.json. I recomputed every number independently (Python) and checked both citations by web search.

```
EPISODE: 005 — "Why Random Darts Beat Grids in 100 Dimensions"
IDEA: An even grid of N points in d dimensions gives each axis only N^(1/d) values, so at 20–100 inputs a million-point grid is one point and gets the answer 50 points wrong. Each random dart is a single in/out coin flip, so the darts' error is (1/2)/√N with no d in it.
SCORES: Hook 8 · Clarity 8 · Visual 8 · Motion 8 · Audio 8.5 · Concision 8 · Originality 8.5
WEIGHTED: 8.1   AFTER CEILING: 8.1   (lowest 8 + 2 = 10, not binding)
CAPS: none. Two transient overlaps (0:50.6–0:51.2 digit-glyph swarm over the "input 1" label; 2:36.8–2:37.4 cross-faded formulas on top of each other) each last < 1 s mid-transform. I did not treat them as a held-frame cap 7, but they must be fixed.
FINAL: 8.1   PASS: no
```

## FACTS

| Claim | Status | Source / my check |
|---|---|---|
| 10^6 grid in 100-D → 1 value per input | Verified | 10^(6/100) = 1.148 → floor 1 |
| Single grid point = centre of the box | Verified | midpoint rule with n = 1 is (½,…,½) |
| 2 values per input → 2^100 points, 31 digits; on-screen digits 1,267,650,600,228,229,401,496,703,205,376 | Verified | Python: 31 digits, string matches |
| Quarter disc share of the square = exactly ½ | Verified | r² = 2/π, πr²/4 = ½ |
| 10×10 grid: 52/100 inside, 0.52, "two points off" | Verified | recomputed midpoint count = 52 |
| 100 darts: 44 inside, "six points off"; dart #1 = cold-open dart, outside | Verified (simulated, labelled) | data.json; dart drawn at (0.62, 0.90) in 2-D matches the polyline's first two values at 0:33 |
| "Ball always covers exactly half the box" for d = 2…100 | Verified | r_d² from data.json; my own 400k-point MC gives 0.5002, 0.4997, 0.4993, 0.4996 at d = 6, 10, 20, 100 |
| Grid values per axis 1000, 100, 10, 3, 1, 1 | Verified | floor(10^(6/d)) (with 1e-9 guard at d = 3) |
| Grid errors 0.002, 0.001, 0.10, 2.4 points; 50 points at d = 20 and 100 | Verified | exact lattice DP in sim.py; centre's squared distance d/4 = 5 ≤ 6.63 (d = 20) and 25 ≤ 33.3 (d = 100), so estimate = 1.000 |
| Darts at 10^6: 0.038, 0.013, 0.022, 0.028, 0.025, 0.004 points; "within a twentieth of a point in every dimension"; "every blue dot came in under it" | Verified for the plotted seed, **misleading as a general statement** | 0.05 points is one SD. P(\|err\| < 1 SD) ≈ 0.68, so P(all six under it) ≈ 0.68^6 ≈ 10%. This is a lucky draw, but narration and the dashed line present it as a ceiling (1:31–1:35, 2:38–2:41) |
| N^(1/d) values per axis; 10^6^(1/20) ≈ 1.995 "fewer than two" | Verified | 10^0.3 = 1.9953 |
| 100 grid points cast 10 shadows; 100 darts cast 100 | Verified | |
| Histogram SDs 0.048/0.048 (N = 100) and 0.026/0.024 (N = 400); theory 0.05, 0.025 | Verified (simulated) | data.json hist; matches √(p(1−p)/N) |
| spread = (½)/√N; with N = 10^6 → 0.0005 = 0.05 points | Verified (for a yes/no answer at p = ½) | Bernoulli SD √(p(1−p)) = ½ at p = ½. The general-function assumption (σ_f/√N) is never stated |
| Radius-one ball at d = 30: 2 × 10^-14, "two parts in a hundred trillion" | Verified | π^15/15!/2^30 = 2.041e-14 |
| Curve crosses 1-in-a-million between d = 17 and 18 | Verified | 1.08e-6 (17), 3.1e-7 (18); on-screen crossing ≈ 17.2 |
| Metropolis & Ulam, 1949, *JASA*, published the Monte Carlo method | Verified | JASA 44(247):335–341, Sept 1949 (JSTOR/T&F, PubMed 18139350) |
| Bergstra & Bengio, 2012, *JMLR*: random search found neural nets "as good or better within a small fraction of the computation time" | Verified | JMLR 13:281–305, abstract (jmlr.org) |
| "Nine grid trials test three values of it; nine random trials test nine" | Verified | same paper, Fig. 1 caption; the redraw is labelled "schematic" |

No Wrong or fabricated claims. One claim is true but presented as more than it is (the SD shown as a ceiling), and one modelling assumption is unstated (the (½)/√N figure holds for a yes/no function; general functions scale as σ_f/√N).

## MECHANICS

```
MECHANICS: runtime 3:25.1 · wpm 156 (speech) · max silence 1.96 s (planned prediction hold at 0:10.7) · max static 3.0 s (0:41–0:44) · −14.0 LUFS / −2.0 dBTP
```
Leading silence 0.0 s, trailing 1.74 s, WER 3.4 %, 0 banned phrases, no rhetorical-question chains, no "not just X" patterns. "Darts do have a blind spot: tiny answers" is a mild colon reveal, and the only one. Bengio, Ulam and "d-th" were transcribed correctly, so pronunciation is fine. At 1:16 the ASR heard "a hundred in three" as "103" (the word "in" was deleted per narration_diff), so the TTS is swallowing that word.

## Story / structure (BAR §6)
- **Cold open (0:00–0:12): strong.** The puzzle is concrete and the likely-wrong prediction (most viewers divide and guess 10,000, or guess 10) is committed by 0:12, with the 1.7 s hold. "One." is a real jolt.
- **Stakes (0:23–0:35): weak.** "Yet such averages are routine" names no real problem. The first real-world anchor is Bergstra & Bengio at 2:43, so for 2½ minutes the viewer has no concrete reason to care about a 100-input average.
- **Naive build and fail (0:35–1:35): textbook SMH.** The grid *wins* in 2-D (0.02 vs 0.06, boxed at 1:01), then the measured collapse to 50 points off. This is the best part of the episode.
- **Insight (1:36–2:41).** Shadows → N^(1/d) → one bit per dart → histograms → formula from the brackets → prediction hold → back to the chart. The chain holds together and could be re-derived after one watch.
- **Payoff and limit (2:41–3:15).** The B&B redraw reuses the shadow device, which is a lovely callback. The limit (3:01–3:15) shows the number but never says *why* it is a blind spot: darts report 0, which is off by 100 % of the answer even though the absolute error is tiny.
- **Landing (3:15–3:23).** It returns to the cold-open frame, which is good. The last line, however, credits the darts' win to "a million values per axis". That is the shadow story, not the mechanism the episode proved (independent coin flips). A million points on the diagonal also give each axis a million values and would fail.

## FIXES (highest impact first)
1. **[1:31–1:35 and 2:33–2:41][Clarity] The SD is presented as a ceiling.** "The darts stay within a twentieth of a point in every dimension" and "Every blue dot came in under it" turn a one-SD typical miss (which about 1 in 3 runs exceeds; all six landing under it is a ~10 % draw) into a guarantee. Change B8's last sentence to "The darts stay under a tenth of a point in every dimension." Two SD is a robust claim and true for all six dots (max 0.038). Change B13's last sentence to "That's a typical miss; about two runs in three land inside it. All six of ours did." Keep the dashed line at 0.05 labelled "typical miss (1 SD)".
2. **[2:29–2:38][Clarity/Visual] The chart is mislabelled.** The header reads "N = 1,000,000 darts" directly above histograms whose brackets read ±0.026/±0.024 (N = 400 data). Read literally, the frame says million-dart estimates spread by 2.6 points. When N = 1,000,000 is substituted, dim both histograms to 30 % and move "N = 400 darts per experiment" onto them as their own label, or shrink them away before the substitution.
3. **[1:09–1:35][Clarity] Budget fairness is never addressed.** At d = 10 the grid uses 59,049 points, and at d = 20/100 it uses 1 of the million, while the darts use all 10^6. A sharp viewer objects "you threw away 999,999 points". Add a grey row "points used: 10^6 · 10^6 · 10^6 · 59,049 · 1 · 1" under "grid values per axis". Then add one clause to B8: "Even spending half a million points on two values for nineteen of the axes still leaves it eighteen points off." I checked this: 2^19 = 524,288 points at (¼, ¾) on 19 axes plus the centre value on one; P(Bin(19, ½) ≤ 10) = 0.676, so it is 17.6 points off.
4. **[3:01–3:15][Clarity] The honest limit never says why tiny answers hurt.** After "less than one hit", add: "So they report zero: off by the entire answer, even while the error is far under a twentieth of a point." Optionally add one dim on-screen line, "relative error → 100 %". In the same beat, state the hidden assumption in one clause: "a yes/no answer spreads at most a half per dart; a wilder function spreads more" (on screen: σ/√N with σ ≤ ½ for yes/no).
5. **[0:23–0:26][Hook] The stakes are abstract.** Replace "Yet such averages are routine." with one concrete, true instance on screen, for example "That's what pricing an option on a hundred stocks, or averaging a Bayesian model over a hundred parameters, asks for." A citation such as "Glasserman, 2003 · Monte Carlo Methods in Financial Engineering" (or similar) must be held ≥ 3 s.
6. **[0:00–0:12][Clarity/Hook] The parallel-coordinates encoding is never explained.** A viewer has to infer that each vertical line is one input from 0 to 1 and that a point is a zig-zag across them. "100 inputs, side by side" only appears at 2:01. Add a dim label "each line: one input, 0 to 1" from 0:01–0:06. At 0:33 change "a random point" to "one random point = one value per input".
7. **[3:15–3:23][Clarity/Hook] The closing line credits the wrong mechanism.** Keep the frame, and change the last sentence to "The darts never noticed the axes: a million coin flips, in any dimension." Or keep "a million" per axis and add "and each one is a fair coin flip". The callback should land on the coin-flip insight, not on distinct projections.
8. **[0:50.6–0:51.2][Motion/Visual] The count animation is a digit swarm.** About 52 copies of "5" and "2" swarm out of the dots and over the "input 1" label (tiled frames 0:50.0–0:52.4). Replace it with: Indicate the 52 filled dots (≤ 1 s), then one TransformFromCopy of the whole filled-dot VGroup into a single "52", or a DecimalNumber ticking 0→52 at the readout.
9. **[2:36.6–2:37.4][Motion/Visual] The formulas are cross-faded on top of each other.** "spread = 1/2 ⁄ 1000" and "spread = 0.0005 = 0.05 points" are both visible, overlapping, for about 0.6 s. Use TransformMatchingTex with "spread =" kept fixed, and the fraction morphing into "0.0005", then append "= 0.05 points".
10. **[0:53–1:01 and 2:13–2:38][Clarity] Units switch.** The narration says "two points off" while the screen says "off by 0.02". The histograms read ±0.048 while the chart reads "percentage points". Pick points throughout: "off by 2 points", "off by 6 points", "±4.8 points", "±2.6 points". This also prepares "0.05 points" at 2:37.
11. **[1:54.7–1:58.7][Concision] The per-axis count is said three times.** "A million points over twenty axes: fewer than two" repeats what the chart row showed at 1:21–1:23 ("1" at d = 20). Cut the sentence and the 1,000,000^(1/20) ≈ 1.995 label, and use the 4 s for fix 4.
12. **[1:05–1:11][Visual] The 3-D inset reads as a scribble.** The cabinet projection (P = x + 0.42z, y + 0.3z) makes the x–z and y–z arcs bulge outside the cube outline, as visible curls at the front-bottom-right and top-left corners (1:08.5 zoom), and the octant has no fill. Use an orthographic or isometric projection where the arcs stay inside the cube, and fill the octant face at the same 30 % grey as the 2-D disc so it reads as the same object grown.
13. **[2:13–2:38][Visual] The histograms have no vertical-axis meaning.** Add a dim "runs" label, or a single tick "300 runs", per BAR §5 ("every axis carries a quantity name").
14. **[1:16][Audio] "a hundred in three" loses "in".** Rewrite it as "a hundred values in three dimensions", or add a 0.15 s pause token after "hundred".
15. **[2:53–3:00][Visual] The "model score (schematic)" label is ambiguous.** It floats between the two panels and touches neither curve cleanly. Put one label above each curve, or a single label centred above both, with ≥ 0.15 units clearance.
16. **[1:36–1:38][Motion] There is a near-empty transition.** The chart fades out to an empty frame before the squares return. Keep the chart at 30 % and slide the squares in over it, or transform the d = 2 chart point into the squares, which is what the 2-D comparison is.

REACHES 9 IF ALL FIXED: yes, narrowly. The structure is right (prediction hook, a naive method that first wins and then fails by a measured 50 points, a one-picture insight, a sourced payoff, an honest limit and a callback ending). With fixes 1–7, Clarity and Hook move to 9. Fixes 8–16 move Visual and Motion to about 8.5–9. Reaching 9.0 also needs the concision cut, so that every remaining sentence carries weight.

KEEP:
- The 2-D build where the grid *wins* (0.02 vs 0.06, boxed at 1:01), followed by the measured collapse to "grid says 1.000, 50 points off". This is a real SMH failure beat.
- The single cold-open dart that persists: polyline (0:27) → 2-D dot (0:37) → ringed "outside → 0" against "inside → 1" in 100-D (2:05) → coin block → first histogram run.
- The shadow device used twice: grid points casting 10 shadows (1:41) and B&B's 3-vs-9 trials projected onto the score curve (2:55). Also the half-volume ball recalibrated per dimension so that the truth is ½ everywhere.
