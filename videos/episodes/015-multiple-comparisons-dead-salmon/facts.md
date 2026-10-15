# Episode 15 — fact sheet

Primary source read in full: Bennett, C. M., Baird, A. A., Miller, M. B., & Wolford, G. L. (2010).
"Neural Correlates of Interspecies Perspective Taking in the Post-Mortem Atlantic Salmon: An Argument
For Proper Multiple Comparisons Correction." *Journal of Serendipitous and Unexpected Results* 1(1):1–5.
(First presented as a poster, 15th Annual Meeting of the Organization for Human Brain Mapping, San
Francisco, June 2009.) Full text: mirror at uni-rostock.de (salmon-fMRI.pdf); poster at prefrontal.org.

| # | Claim (as spoken / shown) | Verification | Source |
|---|---|---|---|
| 1 | The salmon was dead when scanned | Methods: "One mature Atlantic Salmon (Salmo salar) … was not alive at the time of scanning." | Bennett et al. 2010, §2 |
| 2 | Each voxel gets its own test | "Voxelwise statistics … ordinary least-squares estimation of the general linear model" | §2 |
| 3 | "one time in a thousand" false-alarm rate per test | Results: "t(131) > 3.15, p(uncorrected) < 0.001". Recomputed: one-sided t crit for df 131 at p = 0.001 is 3.154 (scipy) | §3; sim.py |
| 4 | "A typical scan has about a hundred and thirty thousand voxels" | Abstract: "Across the 130,000 voxels in a typical fMRI volume the probability of at least one false positive is almost certain." | Abstract, §1, §4 |
| 5 | 2009, Craig Bennett's team "did this for real" | Poster OHBM June 2009; journal version 2010 | Improbable Research Ig Nobel page; paper |
| 6 | Shown 48 photos of people in social situations, asked what each person was feeling | "shown a series of photographs depicting human individuals in social situations … asked to determine which emotion the individual in the photo must have been experiencing … 12 blocks … 48 photos" | §2 |
| 7 | "A cluster in its brain lit up" / cluster in the brain cavity | "Several active voxels were observed in a cluster located within the salmon's brain cavity … 81 mm³" (a second, smaller one in the dorsal spinal column). Our on-screen cluster is a schematic, labelled "schematic" | §3, Fig. 1 |
| 8 | Real study threshold p < 0.001, clusters of at least three voxels | "p(uncorrected) < 0.001, 3 voxel extent threshold" | §3 |
| 9 | With FDR or family-wise correction: nothing | "Both of the additional contrasts controlling for multiple comparisons indicated that no significant voxels were present … even at the relaxed thresholds of FDR = 0.25 and FWER = 0.25." (FDR = Benjamini–Hochberg q = 0.05; FWER = Gaussian random field theory, 0.05) | §3 |
| 10 | In 2008 about one in four fMRI studies in NeuroImage skipped correction | "For the year 2008 only 74% of articles in the journal NeuroImage reported results from a general linear model analysis of fMRI data that utilized multiple comparisons correction (193/260 studies)." 67/260 = 25.8 % ≈ one in four | §1 |
| 11 | Ig Nobel Prize (on screen only) | 2012 Ig Nobel Neuroscience Prize to Bennett, Baird, Miller, Wolford | improbable.com/ig/winners (2012) |
| 12 | Gentler corrections such as the false discovery rate still account for the number of tests | Benjamini–Hochberg step-up compares the i-th smallest p to i·q/m; random-field FWER depends on search volume. Paper: "FDR is a less conservative approach relative to FWER methods" | Benjamini & Hochberg 1995, JRSS B 57:289–300; Bennett et al. §1 |

## Recomputed numbers (sim.py, exact unless stated)

| Shown / spoken | Value | Computation |
|---|---|---|
| 0.95 after 1 test, 0.9025 after 2 | 0.95, 0.9025 | 0.95^1, 0.95^2 |
| "Fourteen tests, and it's below a half" | 0.95^13 = 0.513, 0.95^14 = 0.488 | first m with 0.95^m < 0.5 is 14 |
| "A thousand, about five times ten to the minus twenty-three" | 0.95^1000 = 5.29e-23 | exact float |
| "thousand-voxel fish stays clean only thirty-seven percent of the time" at α = 0.001 | 0.999^1000 = 0.3677 (Monte Carlo 20 000 fish: 0.3666 clean) | |
| "three times ten to the minus fifty-seven" | 0.999^130000 = exp(−130.07) = 3.26e-57 | |
| "about a hundred and thirty are expected" | m·α = 130 000 × 0.001 = 130 | linearity of expectation (no independence needed) |
| Bonferroni: all m tests together take at most α | P(any) ≤ Σ α/m = α (union bound, no independence needed); for 1000 independent tests 1 − (1 − 0.00005)^1000 = 0.0488 | |
| "p less than five in a hundred thousand" | 0.05 / 1000 = 0.00005 | |
| Power, true signal z-mean 3 (one-sided z test) | P(Z > 1.645) = 0.912 → "ninety-one percent"; P(Z > 3.891) = 0.187 → "nineteen percent" | z crit = Φ⁻¹(0.95) = 1.645, Φ⁻¹(1 − 0.00005) = 3.891 |

## Simulated fish (labelled "simulated" on screen)
- 1000 voxels (silhouette on a 74 × 30 grid), each an independent N(0,1) test statistic, one-sided p = 1 − Φ(z).
- Seed 8 gives 51 hits at p < 0.05 (expected 50), 2 at p < 0.001 (expected 1.0), 0 at p < 0.00005
  (expected 0.05). The seed was picked from the seeds whose counts match these typical values, so the
  picture shows the typical outcome rather than a lucky or unlucky one; everything said about it
  is a count on screen, and expectations are stated from the formulas.
- Independence is an assumption of the (1 − α)^m picture and is said aloud ("for independent tests").
  Real voxels are spatially correlated (smoothing), which is why imaging uses random-field or FDR
  methods instead of plain Bonferroni (paper §4); the Bonferroni bound itself holds without independence.

## Careful wording
- The study is a deliberate demonstration of a statistical error, not a debunking of fMRI. The script
  says corrected analyses found nothing and that imagers use corrections; it never says fMRI is bogus.
- The cold-open cluster is a schematic of the reported brain-cavity cluster, labelled as such.
