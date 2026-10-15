# 037 · Fact sheet

Every number on screen or in the narration, how it was checked, and where it comes from. Simulation code: `data.py` (run `python3 data.py`).

## Simulated stage data (labelled "simulated data" on screen)
| Claim | Verification |
|---|---|
| 80 points: 40 purple in a disk r ≤ 1.0, 40 blue in a ring 1.5 ≤ r ≤ 2.3 | `make_points(seed=7)`; purple max r = 0.998, blue min r = 1.505 |
| 2-D perceptron (start line w=(0.6,0.8), b=0.3; seed 3) starts at 37 mistakes, still thrashing after 5,000 nudges (36 wrong at the end) | `perceptron(X, y, 5000, seed=3, w0=[0.6,0.8], b0=0.3)` |
| Its best moment: 22 of 80 wrong (at nudge 187) | same run, min of the mistake history |
| No straight line gets below 21 mistakes | brute force over 721 directions × every threshold in `data.py` → 21 |
| "Stops only at zero mistakes": the perceptron updates on any misclassified point, so it halts only when none remain; on non-separable data that never happens | definition of the algorithm |
| Lifted with z = x² + y²: purple z ≤ 0.996, blue z ≥ 2.266, so a level sheet at any c in (0.996, 2.266) separates them | `lift(X)` |
| 3-D perceptron from zero weights (seed 44): 8 nudges, 8 distinct points, mistakes 40, 34, 23, 8, 5, 18, 2, 0 | `perceptron(lift(X), y, 50, seed=44)` |
| Level sheet shown at c = 1.65 (perceptron's sheet is nearly level, c ≈ 1.65, tilt 0.1) | same run |
| z = c and z = x² + y² ⇒ x² + y² = c, a circle of radius √c | algebra |
| Perceptron weight = signed sum of nudged points: w = Σ yᵢ φ(pᵢ) (offset b = Σ yᵢ likewise), so the score w·φ(q)+b needs only φ(pᵢ)·φ(q) | perceptron update w ← w + yᵢ φ(pᵢ) from w = 0 (Aizerman et al. 1964 "potential function" form; also Cortes & Vapnik §4) |
| φ(a)·φ(b) = a₁b₁ + a₂b₂ + z_a z_b = a·b + ‖a‖²‖b‖² | algebra; numerically checked in `data.py` (`kernel check`) |
| Widest-margin sheet (hard-margin SVM, C = 10⁶, precomputed kernel above) has exactly 4 support vectors (2 purple, 2 blue), margins ±1.000 | `sklearn.svm.SVC(kernel="precomputed")`; identical to linear SVM on lifted coordinates. Boundary circle r = 1.29, gutters r = 1.01 and 1.52 |

## Real-world claims
| Claim | Status | Source |
|---|---|---|
| Rosenblatt's perceptron, 1958 | Verified | Rosenblatt, F. (1958) *Psychological Review* 65(6):386–408 (PubMed 13602029). The mistake-driven update shown is the standard textbook form of the perceptron rule |
| Boser, Guyon & Vapnik (1992) combined kernels with the maximum-margin ("optimal margin") separator; the classifier depends only on the closest training points | Verified | *A training algorithm for optimal margin classifiers*, COLT '92, pp. 144–152, doi:10.1145/130385.130401; Cortes & Vapnik 1995 p. 276 credit the interchange of operations (kernel) to Boser, Guyon & Vapnik 1992 |
| "Support vectors" | Verified | term used in Cortes & Vapnik 1995 (Boser et al. call them "supporting patterns") |
| US Postal Service digit database, 16 × 16 = 256 pixels, recorded from real mail | Verified | Cortes & Vapnik 1995, §6.2 ("7,300 training patterns and 2,000 test patterns. The resolution … 16 x 16 pixels"; "recorded from actual mail pieces") |
| Polynomial kernel (a·b + 1)^d, degrees 1–7 tried | Verified | Cortes & Vapnik 1995, eq. (39) and Table 2 ("the order of the polynomial ranged from 1 to 7") |
| Degree 1 (flat cut on pixels): 12.0 % raw test error; degree 7: 4.3 %; human performance 2.5 % | Verified | Cortes & Vapnik 1995, Table 2 and Table 1 (human: Bromley & Säckinger 1991). (Best degree was 6 at 4.2 %; we quote degree 7 because it is the 7-pixel-product space discussed) |
| "about sixteen trillion" coordinates for products of up to 7 of 256 pixels | Computed | number of distinct monomials of degree ≤ 7 in 256 variables = C(263, 7) = 15,932,831,090,241 ≈ 1.6 × 10¹³. Note: the paper's Table 2 lists "~1 × 10¹⁶", which matches 256⁷ ≈ 7.2 × 10¹⁶ ordered products; we use the exact distinct-monomial count |
| 256 multiplications per kernel evaluation | Computed | a·b over 256 pixels = 256 multiply–adds, then +1 and a 7th power (a few more multiplications) |
| "Two lab readings … normal means near the middle" | Illustrative analogy only; no empirical claim, no numbers |

## Things deliberately not claimed
- No claim that maximum margin guarantees the best accuracy (it is a regularization principle).
- No claim about RBF kernels / infinite-dimensional spaces (cut for one-idea focus).
