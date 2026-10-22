# Episode 8 — fact sheet

Every number below is recomputed by `data.py` (→ `data.json`) from the raw CSV in this
directory. "Bits" = log base 2. D(W‖V) = ∫ w(x) · log₂(w(x)/v(x)) dx.

**Reading order.** The last section, "Round-5 cut: what is said and shown now", lists every
claim of the current narration and screen. Earlier sections keep the verification history
(some quoted lines there, e.g. the cross-validation sentence and the 15 % ratio, are no longer
in the episode; their numbers stay correct).

## Data

| Claim (screen / narration) | Verification | Source |
|---|---|---|
| 272 eruptions of Old Faithful, timed in minutes | `faithful` has 272 rows; column `eruptions` = "Eruption time in mins" (range 1.6–5.1 min) | R `datasets::faithful` documentation (source: W. Härdle; refs Härdle 1991, *Smoothing Techniques with Implementation in S*, Springer; Azzalini & Bowman 1990, *Applied Statistics* 39:357–365). CSV: vincentarelbundock.github.io/Rdatasets/csv/datasets/faithful.csv |
| Two humps: short eruptions near 2 min, long ones near 4.3 min | Histogram (0.25-min bins from 1.5): 4, 47, 26, 15, 2, 3, 1, 6, 11, 19, 35, 38, 41, 20, 4 | data.py |
| "More than a third of all eruptions are short ones" | 97 of 272 (35.7 %) are under 3 min | data.py |
| The gap is nearly empty | 12 of 272 (4.4 %) between 2.5 and 3.5 min; none below 1.6 or above 5.1 | data.py |

**"The data's curve" (smoothed data).** P = maximum-likelihood mixture of two normals fitted
by EM: weights 0.348 / 0.652, means 2.019 / 4.273 min, SDs 0.236 / 0.437 min. At the EM
fixed point the mixture's mean and variance equal the sample mean and (1/n) variance exactly
(3.488 min, 1.139 min), which is why the data-first best bell is the ordinary
maximum-likelihood normal fit. The curve is labelled "data, smoothed" on screen.

**Sensitivity (narration and demonstration, beat 12).** The bell-first optimum lands on the
long hump (4.27 ± 0.40–0.50 min) for the 2-, 3- and 4-component normal mixtures (BIC 580.9 /
582.0 / 580.4) and for Gaussian kernel smoothing with bandwidth ≤ 0.25 min (leave-one-out
likelihood CV picks ≈ 0.10). Heavier smoothing fills the gap. **R's default** (`density()` uses
`bw.nrd0` = 0.9·min(sd, IQR/1.34)·n^(−1/5) = 0.9 · min(1.1414, 2.2915/1.34) · 272^(−0.2) =
**0.3348 min**, recomputed in data.py with R's type-7 quartiles) already tips it: D(bell ‖ data)
then has two local minima, a **wide one at 3.547 ± 0.991 min (0.567 bits, the global
minimum)** and a narrow one at 4.188 ± 0.615 min (0.598 bits); plain gradient descent started
from A stops at the wide one. (Round-1 substance critic computed the same 0.566 vs 0.598.)
Narration: "Smooth the data with R's default setting, and the gap fills enough that the best
bell-first fit comes out wide." On screen: the curve morphs into that kernel smoothing ("R's
default smoothing"); B stays as a faint reference and a *separate* fit starts from A and slides
(the stored gradient-descent path from A, 612 raw steps, D falling monotonically 1.69 → 0.567)
to "best bell-first fit: 3.55 ± 0.99 min". It is never called B (round-2 substance fix: a descent
started from B under this smoothing stops at the narrow local minimum 4.19 ± 0.62, so the morph
must start from A). (Bandwidths 0.30–0.33 give a wide local minimum that is not yet global; at
0.36 the only minimum is wide, 3.53 ± 1.02.)

**Which smoothing to trust (narration, beat 12): "Smoothing chosen by cross-validation keeps the
gap nearly empty, and the fit on one hump."** Leave-one-out likelihood cross-validation of the
Gaussian kernel bandwidth (grid 0.050–0.400 min in steps of 0.001, data.py) picks **h = 0.103
min** (LOO log-likelihood −270.8 vs −302.1 at R's default 0.335). That smoothing puts 5.5 % of its
mass in 2.5–3.5 min (raw data 4.4 %, R's default 9.8 %, the two-normal fit 3.2 %), and its best
bell-first fit is **4.275 ± 0.389 min (0.698 bits)**, reached by Nelder–Mead from A and from B
alike; on screen the fit slides there from the wide fit (gradient descent on that curve, 294
steps, monotone) and is labelled "best bell-first fit: 4.28 ± 0.39 min". Bandwidth scan
(best fit from A / from B): 0.10 → 4.28 ± 0.39 both; 0.15 → 4.27 ± 0.42 both; 0.20 → 4.27 ± 0.45
both; 0.25 → 4.26 ± 0.50 both; 0.30 → 3.59 ± 0.95 from A, 4.23 ± 0.55 from B; 0.335 → 3.55 ± 0.99 /
4.19 ± 0.62; 0.36 → 3.53 ± 1.02 both. The cross-validated curve's peak density is 0.62; the fit's
peak is 1.027 (drawn just above the 1.0 tick).

**Why the data is smoothed at all (footnote, beat 12).** Against the raw 272 points (the
empirical distribution, all mass on 272 points) every bell has D(bell ‖ data) = ∞: the bell puts
positive probability on the intervals between data points, where the empirical distribution
puts none, so the bell is not absolutely continuous with respect to it and the KL divergence is
infinite (standard measure-theoretic definition: KL(P‖Q) is finite only if P ≪ Q, i.e. dP/dQ
exists; with densities, w·log(w/v) blows up wherever w > 0 = v). On screen, in the citation slot: "With raw points, D(bell ‖ data) = ∞ for every bell". (Data first, the bell-dependent part −(1/n)Σ log q(xₙ) is finite, which is what
maximum likelihood minimises — Bishop eq. 1.119; not claimed on screen.)

## Numbers shown or spoken

| Claim | Value (data.py) | Spoken / shown |
|---|---|---|
| Bell A = closest bell with the data first = MLE normal | mean 3.4878, SD 1.1393 min (numerical minimisation of D(P‖N) from (3, 1) lands on the same point: 3.48778, 1.13927) | "three and a half minutes, give or take one point one"; 3.49 ± 1.14 |
| D(data ‖ A) | 0.762 bits | "point seven six bits" |
| Shifting or stretching A increases D(data ‖ bell) | closed form D = −h(P) + ln(σ√2π) + (Var_P + (m_P − μ)²)/(2σ²), in nats ÷ ln 2; strictly convex in (μ, log σ) with minimum at moments. On screen: shift μ by −0.8 min → 1.118 bits (shown 1.12); stretch σ ×1.8 → 1.111 bits (1.11); each flashed during a 0.5 s hold | live number on screen |
| D(A ‖ data) | 1.695 bits; ratio 1.695 / 0.762 = 2.22 | "one point seven bits … more than twice as far" |
| At 2.0 min: p = 0.588, q_A = 0.149 | q/p = 0.254; 4·q = 0.597 ≈ p; log₂(p/q) = 1.98 | "about a quarter as much … double q twice … about two" |
| Bell B = closest bell with the bell first | mean 4.2712, SD 0.4408 min (Nelder–Mead; grid search over μ∈[1,6], σ∈[0.1,3] agrees) | "settles on the long hump"; 4.27 ± 0.44 |
| B is less than half as wide as A | 0.4408 / 1.1393 = 0.387 | "less than half as wide" |
| At 2.0 min under B: q_B = 1.56·10⁻⁶ | log₂(p/q_B) = log₂(0.588 / 1.56·10⁻⁶) = 18.52 | "eighteen and a half doublings"; readout switches to scientific notation below 0.01, shows "q = 1.6×10⁻⁶" |
| D(data ‖ B) | 5.77 bits | "five point eight bits" |
| Peak of the data-first integrand for B | p·log₂(p/q_B) peaks at 10.98 bits/min near 1.97 min (drawn clipped at 2 with a "peak 11" tag) | on screen |
| D(B ‖ data) | 0.616 bits | "point six two" |
| Descent from A with the bell first ends at B | plain gradient descent on (μ, log σ) from A, 308 steps, D decreases monotonically 1.695 → 0.616 and stops at B | animation (path stored in data.json) |
| Other local minimum (not shown) | short hump: 2.020 ± 0.237, D = 1.519 bits (worse than B) | facts only |
| Bell A "imagines eruptions in the gap and out in the tails" | A puts 31.1 % of its mass in 2.5–3.5 min (smoothed data: 3.2 %; raw: 4.4 %) and 2.8 % outside 1–6 min, where the data has none; integrand q·log₂(q/p) is positive there | narration + shaded area |
| Of D(A ‖ data) = 1.695, 1.60 comes from 0–7 min (the plotted range) | remaining 0.09 from beyond the axis | number shown is the full integral |
| Bell B "almost never imagines a short eruption, so ignoring them costs it nothing" (beat 9: "Take bell B first. It almost never imagines…") | B puts 0.20 % of its mass below 3 min; the part of D(B ‖ data) from x < 3 min is −0.0005 bits | narration |
| Where A's 1.695 bits come from (bell first) | gap 2.5–3.5 min: 1.226; tails below 1 min and above 6 min: 0.324 + 0.165; refunds under the humps: −0.026 (1–2.5) and +0.005 (3.5–6) | shaded area |
| R's default smoothing (kernel bandwidth bw.nrd0 = 0.3348 min): best bell-first fit | 3.547 ± 0.991 min, D = 0.567 bits (global; narrow local minimum 4.188 ± 0.615 at 0.598 bits); gradient descent from A ends at the wide one | "comes out wide"; "best bell-first fit: 3.55 ± 0.99 min", morph started from A (beat 12) |
| Unweighted log₂(p/q_A) where the lower panel clips it at −1 | below −1 on [0, 1.461], [2.444, 3.588] and [5.229, 7] min; −45.4 at 0 min, minimum −6.18 at 2.84 min in the gap, −20.5 at 7 min | grey tags "↓ −45", "↓ −6.2", "↓ −20"; clipped stretches drawn faint (beat 6) |
| B keeps 15 % of the posterior's variance | The blue curve (standing in for the posterior) has SD 1.1393 min (= sample SD, the EM mixture keeps the moments); (σ_B/σ_post)² = (0.4408/1.1393)² = 0.1497; from the displayed values (0.44/1.14)² = 0.149 → 15 % | "Here, bell B keeps only fifteen percent of the posterior's variance"; "(0.44 / 1.14)² = 15%", 1.14 blue, 0.44 purple (beat 11) |
| ±1 SD brackets | Posterior (blue curve): 3.488 ∓ 1.139 → [2.349, 4.627] min, drawn blue on the blue curve at height 0.12 (low, under the curve; the curve's own heights there are 0.22 and 0.43); B: 4.271 ∓ 0.441 → [3.830, 4.712] min, drawn purple at height 0.78, above the blue crowns (0.590, 0.595) and below B's crown (0.905) | labelled 1.14 and 0.44 before they fly into the fraction (beat 11) |

## Real-world anchor and citations

| Claim | Verification | Source |
|---|---|---|
| KL divergence from Kullback and Leibler, 1951 | S. Kullback & R. A. Leibler, "On Information and Sufficiency", *Annals of Mathematical Statistics* 22(1): 79–86 (1951) | Encyclopedia of Mathematics entry "Kullback–Leibler information"; Project Euclid |
| "Every maximum-likelihood fit is the closest model by it" (data first) | Bishop (2006) §1.6.1, eq. 1.119: with training points the KL(p‖q) ≈ (1/N)Σ{−ln q(xₙ|θ) + ln p(xₙ)}, "minimizing this Kullback-Leibler divergence is equivalent to maximizing the likelihood function" | C. M. Bishop, *Pattern Recognition and Machine Learning*, Springer 2006, p. 57 (eq. 1.119) |
| "It's often described as a distance" but is not symmetric | Bishop §1.6.1: "it is not a symmetrical quantity, that is to say KL(p‖q) ≢ KL(q‖p)"; Blei et al. 2017 §2.2: "It is asymmetric … and nonnegative". (It also fails the triangle inequality; not claimed on screen.) | Bishop 2006; Blei et al. 2017 |
| "Maximum likelihood puts the data first, so its fits stretch over every hump. Variational inference approximates a Bayesian posterior with the model first, so it settles on one hump." (Bishop citation on screen, §10.1) | Bishop §10.1.2, Fig. 10.3: single Gaussian fitted to a two-Gaussian mixture by KL(p‖q) spans both modes; by KL(q‖p) it sits on one mode (panels b, c show two local minima). Text: "a variational treatment based on the minimization of KL(q‖p) will tend to find one of these modes. By contrast, if we were to minimize KL(p‖q), the resulting approximations would average across all of the modes" | Bishop 2006, pp. 468–469 |
| Variational inference minimizes KL(q‖p), the second argument being the exact **posterior** | Blei et al. eq. 1: q*(z) = argmin KL(q(z)‖p(z|x)). Round-1 fix: the on-screen legend used to read "D(model ‖ data) · variational inference", which was wrong (VI's target is the posterior p(z|x), not the data). It now reads "D(model ‖ posterior) · variational inference", the blue curve's tag turns from "data" into "posterior" before that row appears, and the narration says "Variational inference approximates a Bayesian posterior with the model first". Row 1 stays "D(data ‖ model) · maximum likelihood" (Bishop eq. 1.119). | Blei, Kucukelbir & McAuliffe, "Variational Inference: A Review for Statisticians", *J. American Statistical Association* 112(518): 859–877 (2017), arXiv:1601.00670 |
| "Variational inference generally underestimates posterior variance" (illustrated: B keeps 15 % of the blue curve's variance) | Blei et al. 2017 §1: "We do know that variational inference generally underestimates the variance of the posterior density; this is a consequence of its objective function." | Blei et al. 2017 |
| "a fast way to approximate Bayesian posteriors" | Blei et al. 2017 §1: VI approximates difficult-to-compute posterior densities and "tends to be faster than classical methods, such as Markov chain Monte Carlo sampling" | Blei et al. 2017 |

## Conventions

The episode never uses "forward/reverse" or "from/to" wording, because fields disagree on
which is which (Bishop calls KL(p‖q) the "reverse" divergence in the variational-inference
context, many ML texts call it "forward"). It names the order only by what goes first:
"with the data first" = D(data‖bell), "with the bell first" = D(bell‖data). The first
argument is the distribution whose samples are averaged over (the weight in the integral).

## Cut / not claimed

- No claim that KL is the only or most common fitting criterion.
- The 2-D posterior picture (Bishop Fig. 10.2) is not drawn. Round 1 said "Bishop's textbook
  draws this same picture"; that clause is cut (the viewer never saw Bishop's figure). Bishop
  is now cited only for the ML / VI behaviour it states in §1.6.1 and §10.1.2 (Fig. 10.3).
- The one-hump bell is called a "fit that settles on one hump", not a "jump" (round 1 used
  "the jump", which the viewer never saw).

## Round-2 review changes (verified)

| Claim (screen / narration) | Value / verification | Where |
|---|---|---|
| Cold-open bet "it stays at one. Or does it move to two, or three?" | 1 = bell A's own place; 2 and 3 are schematic narrow ghosts (drawn with B's width 0.44) on the short (2.02 min) and long (4.27 min) hump. Option 2 is a genuine candidate: the bell-first objective has a local minimum on the short hump, 2.020 ± 0.237 min at 1.519 bits, worse than B (0.616) | beat 1; answered in beat 10 ("moves to three", arrow 1 → 3) |
| "Where the bell rises above the data, the grey dips pay a little back" | The integrand p·log₂(p/q) is negative exactly where q > p; for A its negative part totals −0.175 bits of the 0.762 (deepest −0.186 bits/min at 3.51 min, under the "refund" tag) | beat 6 |
| Two bills kept side by side: at B data-first 5.77 vs bell-first 0.62; at A 0.76 vs 1.69 | data.json A/B fwd/rev | beats 8–10 |
| "As that bill drains, the other one swells" | Along the stored descent path A → B (121 resampled points): D(bell ‖ data) falls monotonically 1.695 → 0.616; D(data ‖ bell) rises monotonically 0.762 → 5.766; the peak of the data-first integrand on 0–7 min rises monotonically 1.16 → 10.98 (live "peak ≈" tag, shown only while the bill is clipped at 2.5) | beat 10 |
| "Smoothing chosen by cross-validation keeps the gap nearly empty, and the fit on one hump" | LOO likelihood CV bandwidth 0.103 min; gap mass 5.5 %; best bell-first fit 4.28 ± 0.39 (from A and from B) | beat 12; details above |
| Footnote "With raw points, D(bell ‖ data) = ∞ for every bell" | unchanged (see "Why the data is smoothed"); now typeset with the D-expression in math | beat 12 |


## Round-5 cut: what is said and shown now (verified)

| Claim (narration / screen) | Verification | Source |
|---|---|---|
| Cold open: "Data first, the closest bell is this one. Swap the order. If closeness is a distance, order can't matter: it stays at one. Or does it move to two, or three?" | A = data-first optimum (above). A distance (metric) is symmetric by definition, d(x, y) = d(y, x), so the belief voiced is exactly the symmetry axiom. Answer (beat 10): the bell-first optimum is B on the long hump (option 3); option 2 is a real but worse local minimum (2.020 ± 0.237 min, 1.519 bits vs B's 0.616) | metric axioms; data.json |
| Stakes: "Every maximum-likelihood fit shrinks it with the data first, and much of Bayesian machine learning shrinks it with the order flipped" | ML: minimising KL(empirical ‖ model) ⇔ maximising likelihood (Bishop 2006 eq. 1.119; strictly, the data-dependent part −(1/n)Σ log q(xₙ) of KL(true ‖ model), estimated from the sample). VI: q* = argmin KL(q(z) ‖ p(z∣x)), the model (approximation) first (Blei et al. 2017 eq. 1). "much of": Bayesian ML also uses MCMC, which minimises no KL; the claim is limited to the variational part (the on-screen tag says "variational inference"). Grey "variational inference" tag under D(bell ‖ data), Blei citation on screen | Bishop 2006 §1.6.1; Blei et al. 2017 §2 |
| Payoff legend: "D(data ‖ bell) maximum likelihood → A", "D(bell ‖ posterior) variational inference → B" | ML normal fit = A exactly (moments). B minimises D(bell ‖ curve); the curve is tagged "if this were a posterior" while row 2 is on screen, so → B is the VI answer for that hypothetical posterior. Bishop §10.1.2 / Fig. 10.3 for the general behaviour ("tends to find one of these modes") | Bishop 2006 pp. 468–469 |
| "In a real ad-conversion model, its average for one effect matched MCMC, but its spread was only a fifth as wide." (round-5 continuation: reworded so "MCMC" is not followed by a possessive, which whisper heard as "MCM cease") Screen: "MCMC 0.110 ± 0.020", "VI 0.110 ± 0.004", five VI spreads laid end to end across one MCMC spread | Giordano, Broderick & Jordan (2018), "Covariances, Robustness, and Variational Bayes", *JMLR* 19(51):1–49, §5.3 (logistic GLMM with random effects on a subsample of the 2014 Criteo Labs conversion-logs data). **Table 2** (posterior means): β₃ MCMC 0.110, MFVB 0.110 (MCMC std. err. 0.00028, 5000 effective draws). **Table 3** (posterior standard deviations): β₃ MCMC 0.020, LRVB 0.020, uncorrected MFVB 0.004 → 0.004 / 0.020 = 1/5. Text: "The uncorrected MFVB variance estimates of β are particularly inaccurate". Checked against the JMLR PDF (jmlr.org/papers/volume19/17-670/17-670.pdf) on 2026-10-22, and re-read again in the round-5 continuation: Table 2 row "β3 | 0.110 | 0.110 | 0.103 (MAP) | 0.00028 | 5000"; Table 3 row "β3 | 0.020 | 0.020 | 0.004" (MCMC, LRVB, uncorrected MFVB). "VI" on screen = the paper's uncorrected mean-field VB, i.e. plain variational inference. The authors note their data cleaning was for illustration, so the episode claims nothing about advertising itself | Giordano et al. 2018, Tables 2–3 (citation on screen: "Giordano, Broderick & Jordan, 2018 · JMLR, Tables 2–3") |
| Why VI's spread is too narrow is the same order effect | KL(q‖p) charges q for any mass where p is small, so q is pulled inside p; for a correlated posterior a factorised q fitted this way has the variance of the narrowest direction (Bishop §10.1.2, Fig. 10.2: "the variance … is controlled by the direction of smallest variance of p"); Blei et al. §5: underestimation "is a consequence of its objective function" | Bishop 2006 p. 467; Blei et al. 2017 |
| ±1 SD brackets during "underestimates posterior variance": "±1.14" (blue, on the curve) and "±0.44" (purple, on B) | brackets span mean ± SD: [2.349, 4.627] and [3.830, 4.712] min, so the label now states the half-length the bracket measures (round-5 substance fix 2) | data.json A_pm_sd, B_pm_sd |
| Honest limit: "Against raw points, every bell-first score is infinite" (272 blue ticks, one per eruption; "D(bell ‖ data) = ∞") | The empirical distribution puts all its mass on 272 points; a bell puts mass between them, where the empirical measure has none, so bell ≪ data fails and KL(bell ‖ data) = ∞ for every bell (data first, the bell-dependent part −(1/n)Σ log q(xₙ) stays finite, which is how maximum likelihood still ranks bells; not claimed) | measure-theoretic KL definition |
| "so the data must be smoothed. Smooth it more heavily, the gap partly fills" | Mass in the 2.5–3.5 min gap: two-normal fit (the curve used all episode) 3.2 %, raw data 4.4 %, R's default kernel smoothing (bw.nrd0 = 0.3348 min) 9.8 % | data.py |
| "and the best bell-first fit spreads wide, almost back to A"; label "best bell-first fit: 3.55 ± 0.99 min"; dashed A returns beside it | Under R's default smoothing the global minimum of D(bell ‖ data) is 3.547 ± 0.991 min (0.567 bits); A = 3.488 ± 1.139 min. The bell moves straight from B to that fit (an interpolation showing which bell is best, not a descent: a descent started *from B* would stop at the narrow local minimum 4.188 ± 0.615, see above). Tag "R's default smoothing"; citation "Silverman, 1986 · Density Estimation (R's default bandwidth)": R's `bw.nrd0` documentation calls its formula "Silverman's 'rule of thumb', Silverman (1986, page 48, eqn (3.31))" and `density()` uses it by default | data.json rdef; R `stats::bw.nrd0` docs |
| Landing: "Bell A never misses an eruption that happens. Bell B almost never imagines one that doesn't." with `D(data ‖ bell) → A` / `D(bell ‖ data) → B` and the yellow 1 / 3 | A covers both humps (A's density at every observed length is ≥ 0.089 per min, its lowest at 1.6 and 5.1 min); B puts 0.20 % of its mass below 3 min, where 35.7 % of eruptions are | data.json |
