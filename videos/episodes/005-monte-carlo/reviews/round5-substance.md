# Episode 5, round 1 review (substance: science and story editor)

Reviewer: independent substance critic. Evidence: `review/` pack (metrics.json 01:26 is newer than final.mp4 01:25, so the pack is current). I read report.md, all 14 contact sheets and keyframes kf_04, 06, 10, 17, 23, 25, 28, 30, 33, 35, 36, 38, 39. I also pulled extra frames at 2:01.5, 2:45.8, 2:46.5, 2:47.2, 3:16.6, 3:17.2, 3:33.2 and 3:33.8. I re-ran every number from `data.json` with independent code (lattice DP, Monte Carlo, closed forms) and checked the citations by web search.

```
EPISODE: 005 — "Why Random Darts Beat Grids in 100 Dimensions"
IDEA: An even grid of N points in d dimensions gets only N^(1/d) values per axis, so its error explodes with d. Each random dart is an independent coin flip with P(heads) = the answer, in any dimension, so the darts' error is σ/√N with no d in it.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8 · Originality 9
WEIGHTED: 8.5   AFTER CEILING: 8.5 (lowest 8 + 2 = 10, not binding)
CAPS: none
FINAL: 8.5   PASS: no
```

## FACTS (recomputed independently)

| Claim | Verdict | Check / source |
|---|---|---|
| 10^6 points on a grid in 100-D give 1 value per axis | Verified | floor(10^(6/100)) = floor(1.148) = 1 |
| 2^100 = 1,267,650,600,228,229,401,496,703,205,376 (on screen 0:19–0:21) | Verified | exact integer, 31 digits |
| The single grid point is the centre | Verified | midpoint rule with n = 1 → (½,…,½) |
| Quarter disc average = exactly ½ | Verified | r² = 2/π, πr²/4 = ½ |
| 10×10 grid: 52 of 100 inside, 2 points off | Verified | my count of midpoints with x²+y² ≤ 2/π = 52 |
| 100 darts: 44 inside, 6 points off (simulated, labelled) | Verified | `darts2d` recount = 44 |
| Half-volume ball in every d | Verified | my 200k-point MC at r_d² from data.json: 0.4996, 0.5006, 0.4995, 0.5007, 0.4991 (d = 3, 6, 10, 20, 100); d = 3 exact r = (3/π)^(1/3) = 0.985 |
| Values per axis 1000/100/10/3/1/1, points used 10^6/10^6/10^6/59,049/1/1 | Verified | floor(10^(6/d)); 4^10 > 10^6 |
| Grid errors 0.002, 0.001, 0.10, 2.4 points (d = 2, 3, 6, 10) | Verified | my own lattice DP: 0.50002, 0.499989, 0.501022, 0.524463 |
| d ≥ 20: centre inside the ball, grid says 1.000, 50 points off | Verified | d/4 = 5 ≤ r_20² = 6.63; 25 ≤ 33.30 |
| 2 values on 19 axes, 2^19 points, 18 points off | Verified | Σx² = (23+8k)/16 ≤ 6.6345 ⇔ k ≤ 10; P(Bin(19,½) ≤ 10) = 0.6762 → 17.6 |
| Darts "under a tenth of a point in every dimension" | Verified for the 6 runs shown (wording overgeneralises, fix 5) | errors 0.038, 0.013, 0.022, 0.028, 0.025, 0.004 |
| Grid's 100 points cast 10 shadows; 100 darts cast 100 | Verified | 10 distinct x-midpoints |
| Each axis gets N^(1/d) | Verified | n^d = N |
| 10^6 diagonal points: 57.7% inside, 7.7 ("eight") points off | Verified | 100t² ≤ 33.3015 ⇔ t ≤ 0.57707 |
| Gauges 1.20 > 0.64 (out), 31.8 < 33.3 (in) | Verified | 1.1957 vs 0.6366; 31.766 vs 33.302 (same cold-open dart; coordinates match) |
| One 0/1 flip misses its mean ½ by exactly ½ | Verified | definition |
| 300 runs: ±4.8 / ±4.8 pts (N = 100), ±2.6 / ±2.4 (N = 400) | Verified (simulated) | SDs 4.84, 4.80, 2.61, 2.35; theory 5.0 / 2.5 |
| 16 darts stray about 4 halves; N darts about √N halves; per dart ½/√N | Verified | SD of a sum of N i.i.d. ±½ = ½√N; divided by N |
| Any f: σ/√N, no d | Verified | standard MC standard error |
| Grid error ∝ N^(−2/d) for smooth f (Glasserman 2003 §1.1) | Verified (the law); passage attribution plausible, not reproduced online | product trapezoid/midpoint rule O(h²) = O(N^(−2/d)); course notes give the same rate and the d = 4 crossover; the Glasserman book exists (Springer, Applications of Mathematics 53, 2003/2004) |
| ½/√10^6 = 0.0005 = 0.05 points | Verified | arithmetic |
| Two runs in three land closer; all six did | Verified | P(\|Z\|<1) = 0.683; six errors all < 0.05 (0.683^6 = 0.10) |
| Bergstra & Bengio 2012: random search as good as grid search for neural nets, in a fraction of the time | Verified | JMLR 13:281–305 abstract: "as good or better within a small fraction of the computation time" |
| 9 grid trials test 3 values; 9 random trials test 9 | Verified | B&B 2012, Fig. 1 caption |
| Metropolis & Ulam 1949, JASA | Verified | JASA 44(247):335–341 |
| Option on 100 stocks is a 100-D average (Glasserman 2003) | Verified | pricing = expectation over 100 terminal prices |
| "Such averages are usually done with random points" | Weakly supported | M&U 1949 (on screen) supports the origin, not current practice; quasi-random points are also standard (fix 3) |
| Radius-1 ball in 30-D fills 2 parts in 10^14 | Verified | π^15/15!/2^30 = 2.04e−14 |
| Below 1/N darts "usually report zero" | Verified | crossing at d = 17.06; at the first integer below the line (d = 18), P(0 hits) = e^(−0.31) = 0.73; at d = 30 ≈ 1 |

No wrong or fabricated claims. No cap from the facts.

## MECHANICS

runtime 3:57.1 · wpm 163 (speech) / 156 overall · max silence 1.73 s (prediction hold, 0:11.3) · max static 3.23 s (3:04.3, prediction hold) · −14.0 LUFS / −2.0 dBTP · leading 0.00 s, trailing 1.80 s · WER 2.5% (only spelling and "a"/"one" swaps; "Bengio", "Ulam" and "d-th" heard correctly) · 0 banned phrases. No mechanical caps. Runtime sits 3 s under the 4:00 cap, so any addition must be paid for with a cut.

## Transcript audit (§4)

- Banned phrases: 0. Rhetorical-question chains: none; each of the three questions stands alone and two get a real hold.
- "Hold that thought" (0:36) is a stock filler, though not banned.
- "Darts do have a blind spot: tiny answers" (3:33) and "Darts win another way:" (1:59) are colon set-ups. Neither is a question-and-answer fake reveal, so I do not count them.
- No "it turns out", no recap ending. The last line, "a million coin flips, in any dimension", reframes the cold-open frame instead of listing lessons.
- Hook: question at 0:09, a 1.7 s hold, answer at 0:12.7. It lands before 0:15.

## Story and structure

- **Cold open (0:00–0:21): strong.** 100 parallel axes, "how many values does each input get?", then "One." The likely guess (10,000 = 10^6/100) is wrong by four orders of magnitude, so this is a real jolt. Weakness: the first 5 s are 100 grey lines and the abstract phrase "average a function". The concrete stake (an option on 100 stocks) only arrives at 0:21.5.
- **Open loop (0:34): good.** "How far off would a million of them land?" closes exactly at 3:08–3:11, with the answer flying onto the chart's dashed line.
- **Build/fail (0:38–1:36): textbook SMH.** The grid honestly wins in 2-D. The fixed-budget climb has an honest "points used" row and a budget-fair 2^19 rescue. Cost: the cold open already revealed that the 100-D grid is one point at the centre, so the climb confirms rather than surprises. Its new information is the size of the miss (50 points), which it shows well.
- **Insight (1:36–3:16): logically complete.** Shadows give N^(1/d). The diagonal kills the "more shadows" misreading. Gauges reduce one dart to one bit, the bits become coins, and identical 2-D/100-D histograms follow. The random walk derives √N, the ½ flies into the formula, ½ becomes σ, and the grid law stands beside it. Two gaps:
  1. **The ball's radius changes silently.** It is 0.80 in 2-D and 5.77 in 100-D, larger than the box's side. "The disc becomes a ball that always covers exactly half the box" (1:05) never says so. The 100-D gauge's "33.3" (kf_23, 2:08) appears from nowhere. At 3:36 "a radius-one ball fills 2 parts in 100 trillion" sits next to "the ball always covers half" with no reconciliation, and an attentive viewer will stumble here.
  2. **The two laws are not cashed in.** N^(−2/d) and N^(−1/2) tie at d = 4, which is exactly where the chart's purple and blue lines cross (between d = 3 and 6, visible 1:17–1:36). The episode puts the law beside the data but never connects them, and that connection is what would let a viewer re-derive the chart.
- **Payoff (3:16–3:50): strong and honest.** Bergstra & Bengio reuse the shadow device (3 vs 9 shadows). The limit beat shades from the exact crossing.
- **Landing (3:50–3:55):** returns to the cold-open frame flooded with blue, and the closing line re-sees it.

## Frame audit (§5)

- Settled frames are clean. The palette holds all episode long (PURPLE grid, BLUE darts, YELLOW d, RED miss) with no red/green coding. Inside vs outside uses filled vs hollow dots.
- Charts carry quantity names. Citations are bottom-left and held (Glasserman 0:23–0:26 and 2:55–2:59, M&U 0:27–0:34, B&B 3:19–3:33).
- Transitional defects seen in extracted frames:
  - **3:16.6:** the chart's two curves melt into "grid search"/"random search" through blob shapes, with glyph shards scattered over the d = 3, 6, 10 and 20 dots.
  - **2:47.2:** the formula slides down through the fading "N halves / if they never cancelled" label (√N over "they never").
  - **3:33.2:** the B&B squares and the limit chart's title and ticks overlap mid-dissolve.
- Each defect lasts under 1 s, so none triggers a cap.
- Terminology drift: "spread" (formula, 2:45–3:13), "typical miss" (chart, 3:15), "off by" (2-D), "error" (grid law, 2:55). Four names for one quantity.

## FIXES (highest impact first)

1. **[1:04.8–1:08.9, 2:03–2:09, 3:33–3:42][Clarity] Show the radius growing, and turn the limit beat into its consequence.**
   - B6 narration: "The disc becomes a ball, grown just enough to cover exactly half the box."
   - Add a GRAY row under "points used" (1:11 onward): "ball radius 0.80 0.98 1.40 1.82 2.58 5.77". It comes back with the chart at 3:15.
   - In the 100-D gauge write "< 33.3 = 5.77²" (2-D: "> 0.64 = 0.80²").
   - B19: "Keep the radius at one instead, and by thirty dimensions it fills two parts in a hundred trillion of the box."
   - This removes the "half vs 2×10⁻¹⁴" collision and ties the honest limit back to the main object.
2. **[0:00–0:05 and 0:21.5–0:25.3][Hook + Concision] Put the stake in the first sentence and delete the separate stakes sentence.**
   - Open with: "Your budget: a million evaluations to price an option on a hundred stocks, an average over a hundred inputs."
   - Show "e.g. an option on 100 stocks" and the Glasserman citation from 0:02, beside "d = 100 inputs".
   - Delete "Pricing an option on a hundred stocks is this kind of average." The viewer has a reason to care at 0:03 instead of 0:22, and about 3.5 s is freed.
3. **[2:51–2:59][Clarity] Cash in the two laws against the chart.**
   - After "has d in its exponent" add: "Set them equal: they tie at four dimensions, right where our two lines crossed."
   - On screen: "−2/d = −1/2 ⇔ d = 4" under the two laws (YELLOW d). Then, as the chart returns at 3:15, flash a YELLOW tick at d = 4 between the 3 and 6 columns where the purple and blue lines cross.
   - About 3.5 s, paid for by fix 2.
4. **[0:36.3–0:38.3, 1:32.5–1:35.6][Concision] Make room for fixes 1 and 3 without exceeding 4:00.**
   - Cut "Hold that thought." (≈1.3 s with its pause). The "off by ?" label already holds the question.
   - Shorten B9's second sentence to "The darts stay under a tenth of a point." (≈1 s).
   - Shorten B8 to "From twenty on, just the centre, which is inside the ball." The cold open already established the centre (≈1 s).
5. **[1:32.5–1:35.6][Clarity] "under a tenth of a point in every dimension" generalises six simulated runs.** A single run exceeds 0.1 point (2 SD) about 4.6% of the time. Either drop "in every dimension" (fix 4) or say "in all six dimensions we ran".
6. **[0:25.3–0:34.3][Clarity / sourcing] "Such averages are usually done with random points" is cited only to M&U 1949**, which supports the origin, not current practice.
   - Rephrase as "Since Metropolis and Ulam's 1949 paper, the standard tool has been random points, like this one."
   - Keep "Glasserman, 2003" on screen next to M&U through this sentence (two citation lines, bottom-left).
7. **[3:16.3–3:17.3][Motion] Replace the curve-to-word morph.** At 3:16.6 the curves melt into letter shards. Use `FadeTransform` (or fade out the curves while `TransformFromCopy` takes the chart legend words "grid"/"darts" into "grid search"/"random search"), so no frame shows broken glyphs.
8. **[2:46.6–2:47.6][Visual] Formula passes through a fading label.** At 2:47.2 √N overlaps "they never cancelled". Fade the walk group out completely (0.4 s) before moving the formula, or move the formula first and fade the walk after.
9. **[3:32.7–3:34.0][Visual] B&B → limit-chart dissolve overlaps two scenes.** At 3:33.2 the title "share of box inside a radius-1 ball" and the y-ticks sit over "grid search". Either do the script's promised transform (the squares' axes become the log chart's axes) or finish the B&B fade before writing the chart title.
10. **[2:45–3:15][Clarity] One name for one quantity.** Rename the formula's left side "typical miss" and the grid law's "error" to "grid's miss". Then "typical miss = ½/√N = 0.05 points" flies onto a chart line already labelled "typical miss", and both match the "off by" language of the 2-D beat.

**REACHES 9 IF ALL FIXED:** yes, narrowly.
- My estimate after the fixes: Hook 9 (stake in the first sentence), Clarity 9 (radius visible, d = 4 tie closes the loop between the law and the chart), Visual 9, Motion 9, Audio 8.5, Concision 8.5–9, Originality 9. That gives about 8.9–9.0.
- Fixes 1–3 carry the gain; without them the episode stays about 8.6.
- No structural change is needed: the skeleton follows §6, and the one insight picture (gauges → coins → histograms → walk → σ/√N) already exists.

**KEEP:**
- The 100-axis parallel-coordinates cold open ("grid values per input: ? → 1") and its return at 3:50, flooded with blue coin flips.
- The fixed-budget dimension climb with the honest "points used" row, the 2^19 rescue and the diagonal counterexample (57.7% inside with a million distinct values per axis).
- The gauges that collapse one dart's 2 or 100 coordinates into one 0/1 verdict (kf_23), feeding identical 2-D/100-D histograms and the random walk that derives √N (kf_28).
