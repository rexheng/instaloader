# Facts — episode 19 (Metropolis MCMC)

All simulation numbers are reproduced by `sim_check.py` in this directory (numpy, seeds fixed).

## Target shape (simulated, used throughout)
p̃(x) = 3·exp(−(x−1.3)²/(2·0.55²)) + exp(−(x+1.7)²/(2·0.55²)), x ∈ [−4, 4].

| Claim | Verification | Source |
|---|---|---|
| Small hill is a third as tall as the big one | p̃(−1.7) = 1.000, p̃(1.3) = 3.000 (overlap < 1e-6) | sim_check.py |
| Z = total area ≈ 5.51 | exact 4·0.55·√(2π) = 5.5146; 100-point grid sum on [−4,4] = 5.5146 | sim_check.py |
| Small hill holds 25 % of the area | mass left of the valley (x = −0.328) = 24.96 % | sim_check.py |
| 50,000 Metropolis steps put ≈ 25 % of footprints on the small hill | Gaussian random-walk proposal σ = 1.5, seed 8, start x = 1.3: 25.0 %; seeds 7, 9 give 25.8 %, 24.5 % | sim_check.py (labelled "simulated" on screen) |
| About half of proposals accepted at σ = 1.5 | 46.8–47.2 % | sim_check.py |
| Tiny steps (σ = 0.05, 2,000 steps) never leave the big hill | 96 % accepted, range x ∈ [0.62, 3.16], 0 % on small hill | sim_check.py, seed 3 |
| Huge steps (σ = 25, 2,000 steps) are mostly refused | 5.7 % accepted | sim_check.py, seed 3 |
| 50,000 steps ≈ a few thousand independent draws | effective sample size (initial-positive autocorrelation sum) 3,480–3,930 across seeds 7–9 | sim_check.py |

## Grid cost
| Claim | Verification |
|---|---|
| 100 points per parameter → 100² = 10,000 for two parameters | arithmetic |
| ten parameters → 100¹⁰ = 10²⁰ evaluations | arithmetic |
| at 10⁹ evaluations/s, 10²⁰ takes over 3,000 years | 10¹¹ s / 3.156·10⁷ s/yr = 3,169 years |
| 224 disks in 2-D → 448 coordinates; grid 100⁴⁴⁸ = 10⁸⁹⁶ | arithmetic |

## Two-spot balance (exact expected flows, always propose the other spot)
Heights 3 and 1; acceptance tall→short = 1/3, short→tall = 1.
60/60 → tall loses 20, gains 60 → 100/20 → 86.7/33.3 → 91.1/28.9 → 89.6/30.4 → 90.1/29.9 → 90/30.
At 90/30: 90 × 1/3 = 30 = 30 × 1. Displayed populations are rounded to whole walkers (60, 100, 87, 91, 90, 90).
General: π(x)·min(1, h(y)/h(x)) = π(y)·min(1, h(x)/h(y)) holds iff π ∝ h (detailed balance with a symmetric proposal).

## Real-world anchor
| Claim | Verification | Source |
|---|---|---|
| 1953 paper "Equation of State Calculations by Fast Computing Machines", J. Chem. Phys. 21(6), 1087–1092 | read the scanned paper (received March 6, 1953; June 1953 issue) | doi:10.1063/1.1699114 |
| Authors: Nicholas Metropolis, Arianna W. Rosenbluth, Marshall N. Rosenbluth, Augusta H. Teller, Edward Teller; Los Alamos | paper header | same |
| Rule: if ΔE < 0 allow the move; if ΔE > 0 allow with probability exp(−ΔE/kT) — i.e. accept with the ratio of Boltzmann weights (heights) | paper p. 1088 | same |
| System: N = 224 particles (rigid spheres in two dimensions), 14 per row × 16 rows initial trigonal lattice | paper p. 1090, Fig. 2 | same |
| Run on the Los Alamos MANIAC; "a given point on the pressure curve was obtained in four to five hours of running" | paper p. 1091 | same |
| Paper names the step-size catch: "if too large, most moves will be forbidden, and if too small, the configuration will not change enough" | paper p. 1089 | same |
| Paper itself: "impractical to carry out a several hundred-dimensional integral by the usual numerical methods" | paper p. 1088 | same |
| Arianna Rosenbluth implemented the algorithm on MANIAC | Wikipedia "Arianna W. Rosenbluth", citing Gubernatis 2005 (Phys. Plasmas 12:057303) and M. N. Rosenbluth 2003 (AIP Conf. Proc. 690:22) | |
| W. K. Hastings generalized the method in 1970 | Biometrika 57(1):97–109, doi:10.1093/biomet/57.1.97 | Oxford Academic issue page |
