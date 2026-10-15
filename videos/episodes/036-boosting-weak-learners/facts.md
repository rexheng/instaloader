# Episode 36 — fact sheet

All numbers about the 40 points come from `sim.py` in this directory (seeded, deterministic,
re-run with `python sim.py`). They are **simulated** and labelled "simulated" on screen.

## Simulation (sim.py)

| Claim (script) | Value | Verification |
|---|---|---|
| 40 points, 20 blue (inside a hidden circle), 20 purple (outside) | disc of area 50 centred in a 10 x 10 square, radius sqrt(50/pi) = 3.99 | `make_train()`, seed 3 |
| Best single straight cut gets 26 of 40 right | best stump: x < 1.14 -> purple, else blue; weighted error 14/40 = 0.35 | `best_stump` over all axis-aligned cuts, both features, both signs |
| Guessing gets about 20 | expected 20 of 40 for a fair coin | arithmetic |
| Bagging: 100 cuts each trained on a bootstrap resample, majority vote -> 23 of 40 | 23/40; 12 of the first cut's 14 mistakes are also bagged-vote mistakes | `bagging(seed=500)` |
| The cuts pile up in a few places | 100 bagged cuts: 36 distinct thresholds; top five positions hold 44 of the 100 | Counter in sim.py |
| First cut's 14 mistakes | all 14 are purple points it calls blue | sim.py |
| Mistakes hold 0.35 of the weight, the rest 0.65 | uniform weights 1/40 | — |
| Multiply mistakes by e^alpha, the rest by e^-alpha, set equal -> alpha = 1/2 ln(0.65/0.35) = 0.3095 ~ 0.31 | AdaBoost update w <- w exp(-alpha y h(x)), alpha = 1/2 ln((1-eps)/eps) | Freund & Schapire 1997; computed |
| After the update the old cut has weighted error exactly 1/2 ("a coin flip") | 0.49999999999999983 | sim.py prints it; algebra: eps e^a = (1-eps) e^-a |
| Second cut: x < 5.79 -> blue, else purple; it "splits off the heavy purple points on the right" | 11 of the 14 heavy (misclassified) points have x > 5.79 | sim.py |
| alpha(eps=0.376) = 0.25 for cut 2; alpha = 0 at eps = 0.5 ("a coin flip gets no say") | formula | computed |
| By round 10, 34 right; from round 66 on, 40 of 40 every round | counts per round: 10->34, 47->40 first time, then 38-40 until 66, 40 from 66 to 100 | sim.py round table |
| 5,000 fresh points from the same simulation: vote of 100 cuts scores 78%, one cut scores 61% | 0.778 and 0.607 | `make_fresh(5000, seed=99)` |
| Error region: blocky boundary agrees with the true circle on 77% of the square | 0.773 on a 400x400 grid | consistent with 78% on fresh points |
| Mislabelled point is "chased" | flipping the label of the point at (4.35, 5.82) (inside the circle): its weight rises from 1/40 = 0.025 to a peak of 0.079 (about 3x average) during 100 rounds | sim.py (`noisy_track`) |

## Real-world anchors

| Claim | Verification | Source |
|---|---|---|
| Kearns & Valiant posed whether weak learnability equals strong learnability (1988; 1989) | Schapire (1990) p.197: "The notion of weak learnability was introduced by Kearns and Valiant (1988; 1989) who left open the question of whether the notions of strong and weak learnability are equivalent." | Schapire, R. E. (1990). The strength of weak learnability. *Machine Learning* 5(2):197-227 (PDF read) |
| Schapire 1990 proved the answer is yes | same abstract | same |
| AdaBoost, 1997 (journal version) | Freund, Y. & Schapire, R. E. (1997). A decision-theoretic generalization of on-line learning and an application to boosting. *J. Computer and System Sciences* 55(1):119-139. Conference version EuroCOLT 1995 | Princeton research portal; DOI 10.1006/jcss.1997.1504 |
| Viola & Jones 2001: each weak classifier = a single rectangle feature + a threshold (+ parity) | paper §3: "the weak learning algorithm is designed to select the single rectangle feature which best separates the positive and negative examples ... determines the optimal threshold" | Viola, P. & Jones, M. (2001). Rapid Object Detection using a Boosted Cascade of Simple Features. CVPR (PDF read) |
| Rectangle features compare sums of pixels in adjacent rectangles; base window 24x24 | §2 | same |
| "over 180,000" rectangle features | §2, §3: "there are over 180,000 rectangle features associated with each image sub-window" | same |
| 200 features: 95% detection, 1 false positive in 14,084 | §3.2: "a frontal face classifier constructed from 200 features yields a detection rate of 95% with a false positive rate of 1 in 14084" | same |
| First feature: eye region darker than nose/cheeks | §3.2 | same |
| With noisy labels, bagging beats boosting | Dietterich (2000): with substantial classification noise, bagging is much better than boosting | Dietterich, T. G. (2000). An experimental comparison of three methods for constructing ensembles of decision trees: bagging, boosting, and randomization. *Machine Learning* 40:139-157 |

## Cut / hedged
- Did not claim Viola-Jones "real-time" numbers in narration (15 fps on 700 MHz Pentium III is true per paper but cut for length).
- No claim that the 2001 detector is the first face detector; only that it used AdaBoost on single-feature threshold rules.
- The noisy-label claim from our simulation is only the mechanism (one point's weight grows); the accuracy claim is Dietterich's.
