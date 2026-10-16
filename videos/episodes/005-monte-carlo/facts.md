# Episode 5: fact sheet

Every number shown or spoken, how it was checked, and where it comes from. Computed values are
produced by `sim.py` (writes `data.json`, fixed seeds); simulated data is labelled "simulated" on screen.
Errors are given in **percentage points** (1 point = 0.01 of the box) everywhere on screen and in narration.

## Mathematics (recomputed)

| # | Claim (as narrated / shown) | Check | Status |
|---|---|---|---|
| 1 | A million points on an even grid in 100 dimensions gives **one** value per axis | n = floor(10^6^(1/100)) = floor(1.148) = 1 | Verified |
| 2 | Two values per input would take **2^100** points, a **31-digit** number | 2^100 = 1,267,650,600,228,229,401,496,703,205,376 (31 digits), printed by `sim.py` | Verified |
| 3 | The single grid point is **the centre** of the box | n = 1 midpoint per axis is (1/2, ..., 1/2) | Verified |
| 4 | The function (1 inside the quarter disc, 0 outside) has average = the disc's share of the square = exactly one half | radius r = √(2/π) = 0.7979; area πr²/4 = 1/2 | Verified (exact) |
| 5 | 10×10 grid: **52** of 100 midpoints inside, **two points off** (52/100 vs 50/100) | `sim.py` grid2d count = 52 | Verified |
| 6 | 100 random darts: **44** inside, **six points off** | `sim.py` darts2d: dart #1 is the cold-open 100-D dart's first two coordinates (outside), plus 99 darts from seed 9; count = 44; a typical miss for 100 darts is ±5 points (1 SD), so 6 is ordinary | Verified (simulated) |
| 7 | "The disc becomes a ball that always covers exactly half the box" | r_d solved so that P(ΣU_i² ≤ r_d²) = 1/2: d = 3 exact (r³ = 3/π, r = 0.985); d ≥ 4 by characteristic-function inversion of the exact CDF (residual < 1e-8), cross-checked with 10^6-point Monte Carlo (0.5003, 0.49999, 0.50004, 0.4992 at d = 6, 10, 20, 100). r = 0.798, 0.985, 1.403, 1.817, 2.576, 5.771 for d = 2, 3, 6, 10, 20, 100. The 3-D inset is the exact r = 0.985 eighth-ball centred on a cube corner, computed in 3-D (convex hull of the projected solid) | Verified |
| 8 | Grid values per axis at a million points: **1000, 100, 10, 3, 1, 1**; points used **10^6, 10^6, 10^6, 59,049, 1, 1** for d = 2, 3, 6, 10, 20, 100 | n = floor(10^6^(1/d)); points used n^d (4^10 = 1,048,576 exceeds the budget, so d = 10 uses 3^10 = 59,049) | Verified |
| 9 | Grid error (percentage points) at d = 2, 3, 6, 10: 0.002, 0.001, 0.10, 2.4 | exact lattice counts in `sim.py` (dynamic programming on integer sums of (2i+1)²): estimates 0.50002, 0.499989, 0.501022, 0.524463 | Verified |
| 10 | (shown) the grid's error line crosses above the darts' between d = 3 and d = 6 | grid 0.001 < darts 0.013 at d = 3; grid 0.10 > darts 0.022 at d = 6 | Verified |
| 11 | "From twenty dimensions on, just one" value per axis (floor(10^(6/d)) = 1 for every d ≥ 20, since 10^(6/20) = 1.995); the centre "sits inside the ball", so the grid says the ball **fills the whole box**, **fifty points off** | centre's squared distance from the corner = d/4 = 5 ≤ r_20² = 6.63 (and 25 ≤ 33.30 at d = 100); estimate 1.000 vs truth 0.5 | Verified |
| 12 | **Budget fairness.** "Even two values on nineteen of the axes, half a million points, is eighteen points off" (on screen: hollow dot at 17.6, "2^19 points · 18 points off" over "2 values on 19 axes"; the round-3 wording "the largest two-value grid that fits" misnamed it, since a true two-value grid needs 2^20 > 10^6) | The largest grid with two values per axis that fits the budget at d = 20: midpoints {1/4, 3/4} on 19 axes and the centre on the 20th = 2^19 = 524,288 points (2^20 = 1,048,576 > 10^6). With k coordinates at 3/4, Σx² = (23 + 8k)/16 ≤ 6.6345 ⇔ k ≤ 10, so the estimate is P(Bin(19, ½) ≤ 10) = 0.6762: 17.6 points off (`sim.py` "rescue20") | Verified (exact) |
| 13 | Darts (10^6 each, simulated) "stay **under a tenth of a point** in every dimension" | errors 0.038, 0.013, 0.022, 0.028, 0.025, 0.004 points; max 0.038 < 0.1 (the 0.1 tick flashes). This is a statement about the six simulated runs shown; 0.1 point is 2 SD, which a single run exceeds ~5% of the time | Verified (simulated, seed 2024) |
| 14 | "The grid's hundred points cast **only ten** shadows" on one axis; a hundred darts cast **a hundred** | 10 distinct x-midpoints; 100 continuous uniform draws are distinct with probability 1 (checked) | Verified |
| 15 | N grid points over d axes: **d-th root of N** values per axis (shown first as 100^(1/2) = 10) | n^d = N ⇒ n = N^(1/d) | Verified |
| 16 | "Each one lands inside with a chance equal to the answer, on its own, in two dimensions or a hundred. Their estimate is a share of heads in N coin flips." | A dart is uniform on the cube, so P(inside) = volume inside = the answer p, in any d; darts are drawn independently, so hits ~ Binomial(N, p) (p = 1/2 here in every d). A grid point is not random: it is inside or not with certainty, so its bits are neither independent draws nor fair coins | Verified (definition) |
| 16a | Gauges (on screen): the cold-open dart in 2-D "x1² + x2² = 1.20 > 0.64" -> outside -> 0; the same dart in 100-D "x1² + ... + x100² = 31.8 < 33.3" -> inside -> 1 | `data.json`: dart2d_sum_sq = 1.1957, r2[2] = 0.6366; dart100.sum_sq = 31.766, r2[100] = 33.302 (bar scales 0–2 and 0–40) | Verified |
| 16b | **Shadows alone are not the fix.** "A million points on the diagonal give every axis a million values, and still miss by eight points" (on screen: "10^6 points on the diagonal", "57.7% inside: 7.7 points off") | Points (t, ..., t), t = (i + ½)/10^6: every axis gets 10^6 distinct values; inside iff 100 t² ≤ r_100² = 33.30, i.e. t ≤ 0.5771, so the estimate is 0.577075, 7.7 points off (`sim.py` "diag100"; also checked by the round-2 substance critic: 0.577075). On screen the dashed INK level sits at t = 0.577 and the 26 drawn lines above it fade | Verified (exact) |
| 17 | "One flip is zero or one. Its average is a half, and every flip misses that by exactly a half." | For a 0/1 variable with p = ½: mean ½, |X − ½| = ½ always, so SD = ½ | Verified (exact) |
| 18 | 300 runs of 100 darts: spread **±4.8 points** in 2-D and **±4.8 points** in 100-D (SD 0.0485, 0.0481); with 400 darts **±2.6** and **±2.4 points** (0.0262, 0.0236). Run 1 of each is the experiment shown on screen (44/100 and 48/100) | `sim.py` hist (seed 5); theory √(p(1−p)/N) = 5.0 and 2.5 points | Verified (simulated) |
| 19 | Spread = **that half over the square root of N** | SD of a Binomial share = √(p(1−p)/N) = (1/2)/√N at p = 1/2; no d appears. Quadrupling N halves it (√4 = 2) | Verified (exact) |
| 19a | **Why root N (new).** "Each dart misses by a half, up or down at random, so the misses partly cancel: sixteen darts stray about four halves, not sixteen. N darts stray about root N halves; per dart, that's a half over the square root of N." On screen: 16 steps from darts 62–77 of the 2-D run (`data.json` darts2d.inside[61:77] = 1000010111110111: 10 inside, 6 outside), net +4 halves; the all-aligned staircase reaches 16 halves | Each miss X_i − ½ = ±½ with mean 0, independent; the sum of N has SD ½√N ("about √N halves"; for N = 16 that is 4 halves, and these 16 happen to land exactly at +4). If they never cancelled, N halves. The share's miss is the sum divided by N, i.e. the miss per dart: (½√N)/N = ½/√N | Verified (exact; the walk uses real simulated darts, labelled as the 2-D run) |
| 20 | "Any other function swaps that half for its own spread, sigma. The root N stays." | Monte Carlo standard error is σ_f/√n "for all dimensions d" (Glasserman 2003, §1.1.1, quoted below); for a yes/no f, σ_f = √(p(1−p)) ≤ ½ | Verified |
| 20a | **Grid's error law (new).** "A grid's error, even for smooth functions, has d in its exponent." On screen: "grid, smooth f: error ∝ N^(−2/d)", cited "Glasserman, 2003 · Monte Carlo Methods in Financial Engineering, §1.1" | Glasserman 2003, §1.1.1, p. 3: "the error in a product trapezoidal rule in d dimensions is O(n^{−2/d}) for twice continuously differentiable integrands; this degradation in convergence rate with increasing dimension is characteristic of all deterministic integration methods." The product midpoint rule (our grid) has the same h² = N^(−2/d) leading term (Euler–Maclaurin), so for a generic smooth f the error is proportional to N^(−2/d). It decays more slowly than the darts' N^(−1/2) once d > 4, consistent with the chart, where the grid wins at d = 3 and loses from d = 6. For our ball's yes/no function (not smooth) the grid does worse still: its error is set by the cells cut by the ball's surface | Verified (source read) |
| 21 | "So, back to our ball, with a million darts, in any dimension: how far off is a typical estimate? ... One half over a thousand: five hundredths of a point" | For our ball p = ½ exactly, so the SD is √(p(1−p)/N) = ½/√10^6 = 0.0005 = 0.05 percentage points (exact for this ball; for another yes/no answer p it would be smaller, √(p(1−p)) ≤ ½ — that general case is B16's σ). Answers the open question planted in B2 ("How far off would a million of them land?") | Verified |
| 22 | "Two runs in three land closer; all six of ours did." | P(|Z| < 1) = 0.683; all six simulated errors (#13) < 0.05 points (a ~10% event, 0.683^6 = 0.10, stated as what happened, not as a bound) | Verified |
| 23 | Radius-one ball: by **thirty dimensions** it fills **two parts in a hundred trillion** of the box | share = π^15/15! / 2^30 = 2.04 × 10^-14 | Verified |
| 24 | "Below this line, a million darts expect under one hit, so they usually report zero: off by the whole answer" (on screen: RED zone shaded only from the crossing d = 17.06 on; "darts report 0: / off by the whole answer") | expected hits = N·p < 1 ⇔ p < 10^-6; the share drops below 10^-6 after d = 17 (1.08e-6 at 17, 2.9e-7 at 18). P(0 hits) = (1−p)^N ≈ e^(−Np) > e^(−1) = 0.37 below the line, 0.75 at d = 18, and 1 − 2e-8 at d = 30, hence "usually"; reporting 0 is a 100% relative error | Verified |

## Real-world anchors

| # | Claim | Source | Status |
|---|---|---|---|
| 25 | "Pricing an option on a hundred stocks is exactly this kind of average" (on screen: "e.g. an option on 100 stocks", citation "Glasserman, 2003 · Monte Carlo Methods in Financial Engineering, Springer", held ≈4.5 s) | P. Glasserman, *Monte Carlo Methods in Financial Engineering*, Springer, Applications of Mathematics 53 (2003; © 2004 printing, LoC 2003050499), §1.1.1, p. 3: "the price of a derivative security can be usefully represented as an expected value. Valuing derivatives thus reduces to computing expectations. In many cases, if we were to write the relevant expectation as an integral, we would find that its dimension is large or even infinite." A basket option on 100 stocks is an expectation over 100 random terminal prices (100 normals → 100 uniforms), i.e. an average over [0,1]^100. Same page: "the standard error will still have the form σ_f/√n … In particular, the O(n^−1/2) convergence rate holds for all d. In contrast, the error in a product trapezoidal rule in d dimensions is O(n^−2/d)" — the episode's thesis | Verified (read in the book, pp. 1–3) |
| 26 | "Since Metropolis and Ulam's 1949 paper, such averages are usually done with random points" | N. Metropolis & S. Ulam, "The Monte Carlo Method", *Journal of the American Statistical Association* 44(247):335–341, Sept 1949 (JSTOR listing; PubMed 18139350). "Usually" (round 3 said "use random points", which overclaimed): deterministic quasi-random points (Sobol, Halton) are also used for such integrals, e.g. Paskov & Traub, "Faster Valuation of Financial Derivatives", *J. Portfolio Management* 22(1):113–123 (1995), whose abstract opens "Monte Carlo simulation is widely used to value complex financial instruments" | Verified |
| 27 | (Background, not narrated) Ulam's idea came in 1946 from asking the chance a Canfield solitaire comes out | R. Eckhardt, *Los Alamos Science* 15:131–141 (1987) | Verified |
| 28 | "In 2012, Bergstra and Bengio found that random search tuned neural networks as well as grid search, in a fraction of the time" | J. Bergstra & Y. Bengio, "Random Search for Hyper-Parameter Optimization", *JMLR* 13:281–305 (2012). Abstract: "Compared with neural networks configured by a pure grid search, we find that random search over the same domain is able to find models that are as good or better within a small fraction of the computation time." | Verified |
| 29 | "If one setting matters most, nine grid trials test three values of it; nine random trials test nine." | Same paper, Figure 1 caption: "With grid search, nine trials only test g(x) in three distinct places. With random search, all nine trials explore distinct values of g." The on-screen panel is redrawn after this figure (curve labelled "model score (schematic)"); the nine random points use seed 119736, chosen so their on-screen x-values are at least 0.06 apart (min gap 0.073; nine visibly distinct shadows) and uncorrelated with y (r = 0.00) | Verified |

## Round-1 critic claims and resolutions
- **"One SD presented as a ceiling" (both critics).** Correct. B9 now says "under a tenth of a point"
  (2 SD; true for all six runs), B16 says "a typical miss … two runs in three land under that typical
  miss; all six of ours did", and the dashed line is labelled "typical miss".
- **"N = 1,000,000 header over 400-dart histograms".** Correct. The header now stays "N = 400 darts per
  experiment" and dims with its histograms; 1,000,000 is substituted only inside the formula.
- **"Unstated assumption (½)/√N is the yes/no case; general error is σ_f/√N".** Correct. B13 shows the
  ½ as one yes/no dart's spread, B15 states that any other function swaps the ½ for its own σ (with the
  √N unchanged; Glasserman 2003 §1.1.1), and B16 asks about "a million yes-or-no darts".
- **"Closing line credits distinct projections, not coin flips".** Accepted: the landing now ends on
  "The darts never noticed the axes: a million coin flips, in any dimension."
- **"Budget fairness".** Added (#12): the fairest two-value grid at d = 20 is still 17.6 points off.

## Honest limits stated in the episode
- Plain darts' error is one dart's spread over √N in any dimension (½ over √N at most for a yes/no
  question; σ over √N in general), but a tiny answer (radius-one ball in 30-D) needs ~1/p darts before
  the first hit: the dimension can re-enter through p. The episode says so (B18).
- The grid compared is the plain even (tensor-product) midpoint grid, plus the largest two-value variant that fits the budget at
  d = 20. Smarter deterministic designs (sparse grids, quasi-Monte Carlo) exist; they are not claimed against.
- Pseudo-random numbers (NumPy PCG64) are used; true randomness is not required for this.

## Round-2 critic claims and resolutions
- **No factual errors were claimed** by either critic; all 25 claims were independently re-verified by them.
- **"Each one reports a single bit" also fits grid points (substance 1).** Accepted. The narration now states the
  mechanism: each dart lands inside with a chance equal to the answer, on its own (#16), and the gauges (#16a)
  show one dart's 2 or 100 coordinates collapsing to one bit.
- **"More shadows" misreading (substance 2).** Accepted, with the critic's 100-D construction (#16b): the diagonal
  gives every axis a million values and is still 7.7 points off. (A 2-D diagonal would prove nothing: 56/100.)
- **"One half over a thousand" exact only for p = ½ (substance 9).** Accepted: B17 now opens "Back to our ball",
  after B16 has said that any other function uses its own sigma (#21).
- **Glasserman citation format (substance 8).** "· Springer" added.
- **Random-search x-values merge (substance 11).** New seed (119736); on-screen x-values ≥ 0.06 apart, x and y uncorrelated (#29).
- **"100% off" switches units (substance 4).** The label now reads "darts report 0: / off by the whole answer" and the
  shaded zone starts at the crossing d = 17.06 (#24).

## Round-3 critic claims and resolutions
- **No factual errors were claimed** by either critic; both re-verified every number (the substance critic re-ran the
  seed-2024 million-dart simulation and reproduced all six hit counts).
- **"Use random points" overclaims (substance 6).** Accepted: "are usually done with random points" (#26).
- **"The largest two-value grid that fits" misnames the design (substance 7).** Accepted: "two values on nineteen of
  the axes", label "2 values on 19 axes" (#12).
- **√N asserted from one experiment (substance 1).** Accepted: the random-walk beat (#19a) derives it.
- **The two laws compared a count with an error (craft 2, substance 2).** Accepted: the grid side is now its error
  law, N^(−2/d) for smooth f, quoted from Glasserman §1.1 (#20a). The cell-width alternative was not used: at d = 20
  the formula 1/N^(1/d) gives 0.50 while the actual integer grid's cell is the whole box, which would have put two
  conflicting numbers on screen.
