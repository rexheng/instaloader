# Episode 44 — fact sheet

All "simulated" numbers come from the binormal model below, recomputed in numpy/scipy
(exact expectations; a sampled check with seed 1 gave ROC-AUC 0.993, AP 0.68, 435 TP / 2,773 FP).

| # | Claim (screen / narration) | Verification | Source |
|---|---|---|---|
| 1 | Dataset: 284,807 card transactions over two days (Sept 2013, European cardholders), 492 frauds (0.172%) | Kaggle / ULB dataset description; matches Papers-with-Code mirror | Dal Pozzolo, Caelen, Johnson & Bontempi, "Calibrating Probability with Undersampling for Unbalanced Classification", 2015 IEEE Symposium Series on Computational Intelligence (SSCI), pp. 159–166, Cape Town (IEEE Xplore doc 7376606). Data from Worldline–ULB MLG collaboration. |
| 2 | Honest = 284,807 − 492 = 284,315 | arithmetic | — |
| 3 | "Predict nothing" accuracy = 284,315 / 284,807 = 0.99827 → 99.8% | arithmetic | — |
| 4 | Waffle: one square ≈ 492 transactions → 578 honest squares + 1 fraud square (284,315/492 = 577.9); 578/579 = 0.99827 → 99.8% | arithmetic (honest:fraud ratio = 577.9 ≈ 578) | — |
| 5 | Simulated scores: honest ~ N(0,1), fraud ~ N(3.608,1). Threshold t = 2.326 gives TPR 0.900, FPR 0.010 | Φ⁻¹(0.99)=2.326, d = 2.326 + Φ⁻¹(0.90) = 3.608 | own simulation (labelled "simulated" on screen) |
| 6 | ROC-AUC of that model = Φ(d/√2) = 0.9946 → "point nine nine five" | closed form; sampled 0.993 | own simulation |
| 7 | At t: TP = 0.90 × 492 = 442.8 → 443; FP = 0.01 × 284,315 = 2,843.15 → 2,843 | arithmetic | own simulation |
| 8 | Precision = 442.8 / (442.8 + 2843.15) = 0.1348 → "thirteen percent" | arithmetic | — |
| 9 | False alarms per real fraud = 2843.15/442.8 = 6.42 = (0.01/0.90)·577.9 → "more than six" | arithmetic | — |
| 10 | Precision = 1 / (1 + (FPR/TPR)·(N/P)) — algebraic rearrangement of TP/(TP+FP) with TP = TPR·P, FP = FPR·N | algebra | — |
| 11 | ROC axes (TPR, FPR) are each normalised within one class, so ROC does not change with class ratio | Saito & Rehmsmeier: "The ROC plots are unchanged between balanced and imbalanced datasets"; "Only PRC changes with the ratio of positives and negatives." | Saito & Rehmsmeier 2015, PLoS ONE 10(3): e0118432 |
| 12 | Random-classifier PR baseline = P/(P+N) = 0.00173 → "point one seven percent", not 0.5 | Saito & Rehmsmeier baseline definition; arithmetic | same |
| 13 | Raise threshold to FPR 0.1% (t = 3.090): TPR = Φ(3.608 − 3.090) = 0.698 → "seventy percent"; TP 343, FP 284; precision 0.547 → "more than half" | scipy | own simulation |
| 14 | That simulated model's accuracy at t = 2.326 is (442.8 + 0.99·284,315)/284,807 = 0.9898 (not used on screen) | arithmetic | — |
| 15 | Literature review: of 33 binary SVM genome-wide studies with large imbalanced data sets, 22 used ROC, only 4 used PRC (3 used both) | quoted from paper's Results / Table 4 | Saito & Rehmsmeier 2015, PLoS ONE |
| 16 | ROC is not "wrong": it measures ranking quality independent of class ratio | consistent with paper and curriculum pitfall note | — |

Cut / not claimed: real models on this dataset often reach much higher AUPRC than our simulation;
the video never says the simulated model is a real model's performance — scores are labelled simulated,
class counts are real.
