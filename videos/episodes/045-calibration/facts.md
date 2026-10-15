# Episode 45 — facts and verification

All "simulated" numbers are reproduced by `python3 sim.py` (seed 45) in this directory.

## Real-world claims

| Claim (as said / shown) | Verification | Source |
|---|---|---|
| Guo, Pleiss, Sun & Weinberger, "On Calibration of Modern Neural Networks", ICML 2017 (PMLR 70) | Read the paper text (arXiv 1706.04599v2): header "Proceedings of the 34th International Conference on Machine Learning, Sydney, Australia, PMLR 70, 2017" | arxiv.org/abs/1706.04599 |
| Two networks on CIFAR-100 (32×32 colour photos, 100 categories): a 5-layer LeNet (design from 1998) and a 110-layer ResNet (2016) | Fig. 1 caption and §1: "compares a 5-layer LeNet (left) (LeCun et al., 1998) with a 110-layer ResNet (right) (He et al., 2016) on the CIFAR-100 dataset"; panel titles "LeNet (1998)", "ResNet (2016)". CIFAR-100 = 100 classes, 32×32 colour images (§5) | Guo et al. 2017, Fig. 1, §5 |
| LeNet right about 55 % of the time, ResNet about 69 % | Fig. 1: Error = 44.9 (LeNet), Error = 30.6 (ResNet) → accuracy 55.1 %, 69.4 % | Guo et al. 2017, Fig. 1 |
| "The old design's confidence was honest; the new one's was inflated" | §1: "The average confidence of LeNet closely matches its accuracy, while the average confidence of the ResNet is substantially higher than its accuracy … LeNet is well-calibrated" | Guo et al. 2017, §1 |
| LeNet-5 on CIFAR-100 calibration error 4.85 % (shown as 4.9 %) | Table 1, uncalibrated column, CIFAR-100 LeNet 5: 4.85 % (ECE, M = 15 bins) | Guo et al. 2017, Table 1 |
| ResNet-110 on CIFAR-100: calibration error 16.53 % ("sixteen and a half percent") | Table 1, uncalibrated, CIFAR-100 ResNet 110: 16.53 % | Guo et al. 2017, Table 1 |
| One temperature cut it to 1.26 % ("one point three") | Table 1, Temp. Scaling column, CIFAR-100 ResNet 110: 1.26 % | Guo et al. 2017, Table 1 |
| Temperature scaling does not change accuracy | §4.2: "Because the parameter T does not change the maximum of the softmax function, the class prediction ŷ′ remains unchanged. In other words, temperature scaling does not affect the model's accuracy." | Guo et al. 2017, §4.2 |
| T is fitted on held-out (validation) data | §4.2: "T is optimized with respect to NLL on the validation set." CIFAR splits 45k/5k/10k | Guo et al. 2017 |
| Calibration error definition = count-weighted average gap between confidence and accuracy over bins | Eq. (3): ECE = Σ_m (\|B_m\|/n)·\|acc(B_m) − conf(B_m)\| (Naeini et al. 2015) | Guo et al. 2017, Eq. 3 |
| Bigger capacity → worse calibration (motivates "smaller network" naive fix) | §3 / Fig. 2: "the ECE metric grows substantially with model capacity" | Guo et al. 2017, Fig. 2 |
| Pitfall: not every modern model is overconfident | Stated as "in their experiments"; SVHN and Reuters had ECE < 1 % (§5). Narration only claims results for the networks shown | Guo et al. 2017, §5 |
| Under distribution shift, calibration fitted on held-out data does not hold | Ovadia, Fertig, Ren, Nado, Sculley, Nowozin, Dillon, Lakshminarayanan & Snoek, "Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift", NeurIPS 2019. §4.2: "calibration on the i.i.d. validation dataset does not guarantee calibration under distributional shift"; abstract: "traditional post-hoc calibration does indeed fall short" | arxiv.org/abs/1906.02530 |
| Stakes: confidence decides when a car relies on other sensors / a diagnosis is passed to a doctor | Guo et al. §1 uses exactly these two examples (Bojarski et al. 2016; Jiang et al. 2012). Narrated as uses, not as a statistic | Guo et al. 2017, §1 |

## Simulated numbers (labelled "simulated" on screen)

Model: 10 classes; true label probabilities softmax(u), u = v + w, v ~ N(0, 2.9²), w ~ N(0, 1.5²) per class.
"Big network" reports softmax(2u) (over-sharpened, the kind of overconfidence Guo et al. report).
"Small network" sees only v and reports the exact calibrated E[softmax(v+w) | v] (Monte Carlo, 400 draws).
Test set 10 000 cases, validation set 5 000 cases, 10 equal-width confidence bins.

| Number on screen / spoken | Value from sim.py |
|---|---|
| Big network accuracy "sixty-nine percent" | 0.6915 (identical at every T, checked over T ∈ [1, 2.5] in 0.01 steps) |
| Example prediction's top probability "point eight four" | 0.843 (class 7, which is the true label) |
| Cases with confidence in (0.8, 0.9] "about thirteen hundred" | 1 317 |
| Mean stated confidence in that range | 0.854 |
| Fraction right in that range "sixty-three out of every hundred" | 0.626 |
| Big network calibration error "point one five" (all bins over-confident, so avg confidence − accuracy) | 0.1474 |
| Small network accuracy "fifty-four percent", calibration error "point oh one" | 0.5411, 0.0102 |
| Temperature fitted by NLL on validation set "about two" | T* = 1.97 (true sharpening factor 2.0) |
| Calibration error after temperature "point oh one" | 0.0096 |
| Simulated shift (inputs' informative part shrunk to 60 %), same T*: error "point one one", accuracy 58 % | 0.1089, 0.5811 |

Bins with fewer than 50 cases are drawn faint (opacity ∝ count) because their accuracy is noise.

## Cut / not claimed
- No claim about the accuracy of the ResNet specifically in its 90 % bin (not tabulated in the paper).
- Murphy & Winkler (1977) weather forecasters: not used (one idea per episode).
- No claim that all modern networks are miscalibrated.
