# Facts — Episode 21: When Every Part Says Yes but the Whole Says No

All department data are real (Berkeley, fall 1973). Nothing in this episode is simulated.

| # | Claim (as said / shown) | Verification | Source |
|---|---|---|---|
| 1 | Fall 1973 Berkeley graduate applicants: 8,442 men, 44% admitted; 4,321 women, 35% admitted (12,763 total) | Matches Wikipedia's table and Freedman–Pisani–Purves' textbook summary of the paper | Bickel, Hammel & O'Connell (1975), *Science* 187(4175):398–404, doi:10.1126/science.187.4175.398; Freedman, Pisani & Purves, *Statistics* ch. 2 (via math.upenn.edu/~kazdan notes); en.wikipedia.org/wiki/Simpson's_paradox |
| 2 | "A nine point gap is about ten standard errors wide" | Two-proportion z-test with p1=.44 (n=8442), p2=.35 (n=4321): z = 9.8. Using unrounded 44.3% / 34.6%: z ≈ 10.5. "About ten" holds either way | computed (numpy) |
| 3 | Six largest departments (applicants, % admitted), men / women: A 825 62% / 108 82%; B 560 63% / 25 68%; C 325 37% / 593 34%; D 417 33% / 375 35%; E 191 28% / 393 24%; F 373 6% / 341 7% | Same table in Freedman–Pisani–Purves and Wikipedia; admitted counts from R's `UCBAdmissions` (e.g. A men 512 of 825 = 62.1%, women 89 of 108 = 82.4%) | R datasets::UCBAdmissions doc (rdrr.io); Wikipedia |
| 4 | Women had the higher rate in 4 of the 6 (A, B, D, F); men led in C (36.9 vs 34.1, ~3 pts) and E (27.7 vs 23.9, ~4 pts) | recomputed from counts | computed |
| 5 | Pooled over the six: men 1198/2691 = 44.5% (shown "45"), women 557/1835 = 30.4% (shown "30") | recomputed; R doc states the same 44.5% / 30.4% | R UCBAdmissions doc |
| 6 | "Almost three quarters" of women's applications went to C, E, F | (593+393+341)/1835 = 72.3% | computed |
| 7 | Men's biggest steps are A and B: 51.5% of men applied to A or B (vs 7.2% of women) | (825+560)/2691; (108+25)/1835 | computed |
| 8 | Overall rate = Σ_d (n_d/N) r_d (weighted average of department rates, weights = application shares) | identity: Σ a_d / Σ n_d = Σ n_d r_d / N | algebra |
| 9 | Women's own department rates with the men's application mix: 52% overall, 7 points above men's 45% | Σ_d (n_d^M/2691) r_d^W = 0.516; 51.6 − 44.5 = 7.1 | computed |
| 10 | Bickel, Hammel & O'Connell (Science, 1975) analysed the full campus data and concluded the aggregate gap came from women applying to departments that were harder for anyone to enter; no pattern of discrimination by admissions committees; properly pooled data showed a small, statistically significant bias in favour of women | Wikipedia quotes the paper's "small but statistically significant bias in favor of women"; arXiv 2502.10161 quotes the paper's "no pattern of discrimination on the part of the admissions committee" and "proportion of women applicants tends to be high in departments that are hard to get into" | Science 187:398; arXiv:2502.10161 (Revisiting the Berkeley Admissions data) |
| 11 | Department labels A–F are anonymised in the original; the six-department table is a subset of the full data (101 departments/majors; ~85 analysed) | We say "six largest departments" and never claim they are the whole campus | Freedman et al.; Wikipedia |
| 12 | Causal framing: department is on the path sex → department choice → admission; conditioning on it isolates the committee (direct) path; the pooled gap is the total including where people applied | Pearl frames Bickel's analysis as estimating the direct effect by conditioning on the mediator (department choice) — as summarised in arXiv:2502.10161. We state it as a question-dependent choice, not a universal rule | Pearl & Mackenzie, *The Book of Why* (2018), via arXiv:2502.10161 |

Cut / not used:
- The "Berkeley was sued" story is a myth (Berkeley feared a suit; Bickel to the WSJ, via refsmmat.com). Not mentioned.
- The paper's "shunted by their socialization" closing line: could not retrieve primary text, so not quoted. The episode only poses the upstream question itself.
- Exact admitted totals (3,738 / 1,494) not verified from the primary source; not shown.
