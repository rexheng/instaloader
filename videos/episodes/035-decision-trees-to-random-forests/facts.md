# Episode 35 — fact check

Every number shown or spoken comes from `sim.py` (seeded; output in `sim_output.txt`). The data is simulated, and the screen says so.

## Simulation setup (labelled "simulated" on screen)
- The true rule: a point is gold if x₂ > 5 + 2.2·sin(0.75·x₁), with x uniform on [0,10]². The training set has 300 points (seed 1), and 15 % of labels are flipped at random. In this sample 47 of the 300 are mislabelled.
- "Wrong on new points" means the share of a 400×400 grid over the plane where the model's prediction differs from the true rule. That is the error rate on new points scored against the true rule (the Bayes boundary). It is not scored against noisy labels, which would add a constant 15 %.

## Numbers
| Claim | Value in sim | Verification |
|---|---|---|
| The tree sorts all 300 training points perfectly | training accuracy 1.0 (69 leaves, depth 13) | sim_output.txt |
| The single tree is wrong about 18 % (on screen 18.4 %) | 0.1843 | sim_output.txt |
| Random-forest trees are each wrong about 21 % | mean individual error 0.2147 over the 200 trees | sim_output.txt |
| 200 copies of the tree: 18.4 %, exactly as before | identical trees give an identical majority vote | follows by construction (scene uses literal copies) |
| A bootstrap leaves out about a third of the points | 36.3 % in the resample shown; theory (1−1/300)^300 = 36.7 % → 1/e ≈ 36.8 % | sim_output.txt |
| 200 bagged trees: 11.6 %, and no change after 50 trees | B=20: 12.3 %, B=50: 11.6 %, B=100: 11.6 %, B=150: 11.7 %, B=200: 11.6 % | sim_output.txt |
| Var(mean of B equicorrelated votes) = ρσ² + (1−ρ)σ²/B | exact identity. The B×B covariance matrix has σ² on the diagonal and ρσ² off it; mean of entries = [Bσ² + (B²−B)ρσ²]/B² | Hastie, Tibshirani & Friedman, ESL 2nd ed. (2009), eq. 15.1 |
| ρ = 1 gives σ² (copies gain nothing) | substitute ρ = 1 | algebra |
| Bagged trees: ρ ≈ 0.22, σ² ≈ 0.148, floor ≈ 0.032 | 40 simulated datasets × 100 trees, vote variance averaged over a 60×60 grid; ρ = 0.219 | sim_output.txt |
| Measured variance follows the formula curve | e.g. B=5: 0.0553 vs 0.0556; B=20: 0.0379 vs 0.0382; B=100: 0.0336 vs 0.0336. ρ is estimated from the same runs, so the check is on the curve's shape across B | sim_output.txt |
| Random-feature trees: ρ ≈ 0.17, σ² ≈ 0.152 (each tree a little worse), floor ≈ 0.026 | ρ = 0.170, σ² = 0.1523 | sim_output.txt |
| Random forest: wrong 9.9 % | 0.0992 at B = 200 | sim_output.txt |
| "At every split, look at only a random subset of the features; here one of the two" | sklearn max_features=1 of the 2 features | sim.py |

## Real-world anchor
- **Breiman (2001), "Random Forests", *Machine Learning* 45(1):5–32.** I read the text of the paper (stat.berkeley.edu/~breiman/randomforest2001.pdf). Theorem 1.2: as the number of trees grows, the generalization error converges almost surely, and "this result explains why random forests do not overfit as more trees are added, but produce a limiting value of the generalization error." The abstract says the generalization error "depends on the strength of the individual trees in the forest and the correlation between them." Theorem 2.3 gives PE* ≤ ρ̄(1−s²)/s². Also: "the randomness injected has to minimize the correlation ρ while maintaining strength." **Verified.** Breiman credits earlier random-split ideas (Amit & Geman 1997, Ho 1998, Dietterich 1998), so the narration says "the random forest fix" and does not call random feature selection Breiman's invention.
- **Bagging: Breiman (1996), "Bagging predictors", *Machine Learning* 24(2):123–140.** Verified as the standard citation.
- **ESL eq. 15.1:** Hastie, Tibshirani & Friedman, *The Elements of Statistical Learning*, 2nd ed., Springer 2009, §15.2: the variance of the average of B identically distributed variables with pairwise correlation ρ is ρσ² + (1−ρ)σ²/B. Verified (book text quoted in a web search; I also re-derived it, above).
- **Shotton et al. (2011), "Real-Time Human Pose Recognition in Parts from Single Depth Images", CVPR 2011, 1297–1304.** I read the PDF text. The paper uses a "deep randomized decision forest classifier", and "each tree is trained on a different set of randomly synthesized images", with split candidates randomly proposed. It classifies each pixel into 31 body parts. "Training 3 trees to depth 20 from 1 million images takes about a day on a 1000 core cluster." It runs at "under 5ms per frame (200 frames per second) on the Xbox" GPU. "The algorithm presented here forms a core component of the Kinect gaming platform." **Verified.** The narration says "three randomized trees, each trained on different random images, labelling every pixel of a frame in under five milliseconds."

## Stated limits
- Averaging reduces variance, not bias, and not the variance the trees share (ρσ²). The leftover red area is what most trees get wrong together. The narration says only that, and does not attribute it to bias alone.
- The variance formula assumes equal variance and equal pairwise correlation. The ρ and σ² shown are plane averages, which the sim computes as mean covariance / mean variance.
