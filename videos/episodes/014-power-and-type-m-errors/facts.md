# Episode 14 — facts and verification

All simulation numbers recomputed with numpy/scipy (normal model: each lab's estimate of the
standardized mean difference ~ Normal(D, SE), SE = sqrt(2/n), known sigma = 1, two-sided z-test
at alpha = 0.05, so "significant" means |estimate| > 1.96 SE). The video labels all of this "simulated".

| # | Claim (as narrated / shown) | Verification | Source |
|---|---|---|---|
| 1 | True effect 0.2 SD; 1,000 labs; 20 per group | Setup of the simulation (curriculum id 14). Not a claim about the world. | own simulation, seed 13 |
| 2 | SE = sqrt(2/20) = 0.316 ~ "point three two" | sqrt(0.1) = 0.3162 | exact |
| 3 | Wall = 1.96 x 0.316 = 0.62 | 0.6198 | exact |
| 4 | All 1,000 estimates average 0.20 | seed 13 mean = 0.2045 -> "point two oh" (2 s.f.) | simulation |
| 5 | 97 of 1,000 are significant | seed 13: 97; exact expectation 96.9 (power 0.0969) | simulation + exact |
| 6 | Printed (significant) average 0.69, ~3.5x truth | seed 13: 0.690 (ratio 3.45); exact expected signed mean ratio 3.47 | simulation + exact |
| 7 | Six significant results have the wrong sign | seed 13: 6 (exact expectation 4.8 of 97, Type S rate 4.9%) | simulation |
| 8 | Smallest printable positive effect 0.62 = ~3x the truth | 0.62/0.2 = 3.1 | exact |
| 9 | Walls cross the truth near 200 per group | 1.96*sqrt(2/n) = 0.2 at n = 192 | exact |
| 10 | n = 400: power 81%, printed average 12% too high | power 0.807; E[signed estimate given significant]/D = 1.120 | exact (normal model) |
| 11 | Planning from 0.69 with the standard 80%-power formula gives ~33 per group | n = 2((1.96+0.84)/0.69)^2 = 33.0 | exact |
| 12 | 33 per group against a true 0.2 gives 13% power | 0.128 | exact |
| 13 | Button et al. 2013 estimated median power of neuroscience studies at 21% (730 studies, 49 meta-analyses) | Read in the paper: "comprising data from 49 meta-analyses and 730 individual primary studies ... the median statistical power in neuroscience is 21%." | Button, Ioannidis, Mokrysz, Nosek, Flint, Robinson & Munafò (2013), "Power failure: why small sample size undermines the reliability of neuroscience", Nature Reviews Neuroscience 14:365-376 |
| 14 | In this picture, 21% power -> printed effects ~2.2x the truth | Under the normal model power fixes D/SE = 1.15; expected significant estimate / D = 2.18 (signed), 2.19 (absolute). Same for any D. Equivalent to n ~ 66 per group at D = 0.2. Stated as "in this picture" (a model consequence), not as a measured fact about neuroscience. | exact; relation also in Gelman & Carlin 2014 Fig. 2 |
| 15 | Gelman & Carlin named Type M (magnitude) and Type S (sign) errors | Paper abstract: "(a) the probability of an estimate being in the wrong direction (Type S [sign] error) and (b) the factor by which the magnitude of an effect might be overestimated (Type M [magnitude] error or exaggeration ratio)" | Gelman & Carlin (2014), "Beyond Power Calculations: Assessing Type S (Sign) and Type M (Magnitude) Errors", Perspectives on Psychological Science 9(6):641-651 |
| 16 | A 2007 study reported that the most attractive parents had 8 percentage points more girls among first-born children | Gelman & Carlin: "Of the first-born children of the parents in the most attractive category, 56% were girls, compared with 48% in the other groups ... estimated difference of 8 percentage points with a p value .015" (Kanazawa 2007, Add Health, n = 2,972) | Gelman & Carlin 2014, p. 4-5 |
| 17 | Walls for that study at +-6.5 points | "standard error of the difference was 3.3% ... would have to be more than 6.5 percentage points or less than -6.5". Recomputed: p = .015 -> z = 2.43 -> SE = 3.29 -> 1.96 SE = 6.45 | Gelman & Carlin 2014 |
| 18 | Known sex-ratio effects are about 1 point or less | "effects that have been found have been on the order of 1 percentage point"; authors "expect any true differences ... to be well under 1 percentage point" | Gelman & Carlin 2014 quoting Gelman & Weakliem 2009 |
| 19 | If the true effect were 0.1 point: significant estimate overstates 77x on average, 46% wrong sign | "there is a 46% chance it will have the wrong sign ... the estimated effect will be 77 times too high (the exaggeration ratio)" | Gelman & Carlin 2014 p. 5 |
| 20 | Using published (inflated) effect sizes to plan studies leads to underpowered studies | Gelman & Carlin: "past estimates will themselves tend to be overestimates (as also noted by Button et al., 2013)"; Button et al. discuss winner's curse in replication planning | both papers |

Notes / pitfalls handled
- Power is presented only as a property of a design for an assumed true effect (0.2); no post-hoc power.
- Exaggeration ratios are always quoted with their setup (n per group, true effect, normal model).
- "Printed average" = mean of the signed significant estimates (what a naive meta-analysis of the printed set would compute). Gelman & Carlin's exaggeration ratio uses |estimate|; at n = 20 that is 3.8 vs 3.5 signed; at 21% power both are 2.2.
