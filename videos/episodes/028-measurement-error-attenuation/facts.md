# Episode 28: facts and verification

Simulation: `numpy.random.default_rng(79)`, n = 200 (re-run inline in `scene.py`, numbers below are exact outputs).
Model: true diastolic pressure T ~ N(80, 8²) mmHg; cuff error E ~ N(0, 6²); stroke risk (%) y = 5 + 0.1·(T − 80) + U, U ~ N(0, 0.6²).
Slopes are shown as "% risk per 10 mmHg". All plotted patient data are **simulated** and labelled so on screen.

| # | Claim (on screen / spoken) | Verification | Source |
|---|---|---|---|
| 1 | Fitted slope on true pressures ≈ 1 ("one point of risk per ten") | sample OLS slope = 1.015 (shown 1.02; spoken "about one") | simulation |
| 2 | True pressures spread about 8 either side of 80; cuff error spreads about 6 | sample SD(T) = 8.13, SD(E) = 6.04, mean(E) = −0.25 | simulation |
| 3 | Error averages to zero | mean(E) = −0.25 mmHg ("≈ 0") | simulation |
| 4 | Slope with one noisy reading falls to 0.64 | OLS slope on X = T + E: 0.636 | simulation |
| 5 | "More than a third of the effect is gone" (−37%) | 1 − 0.636/1.015 = 0.374 | simulation |
| 6 | Same-sized noise in the outcome leaves slope near one | slope of (y + E/5) on T = 1.013 | simulation; theory: error in y is uncorrelated with x, OLS unbiased |
| 7 | Readings around 95 (92–98) have true pressures averaging about 90 | 19 patients, mean reading 94.0, mean true 90.0. Theory: 80 + 0.64·15 = 89.6 | simulation; E[T∣X] = μ + λ(X − μ) for jointly normal T, E |
| 8 | Low column (62–68): mean reading 65.7, mean true 68.5 (pulled up toward middle) | simulation | simulation |
| 9 | 8² + 6² = 64 + 36 = 100; λ = 64/100 = 0.64 | arithmetic; Var(T + E) = Var T + Var E for independent T, E | standard |
| 10 | b_obs = λ · b_true with λ = σ_T²/(σ_T² + σ_E²) | plim of OLS slope: Cov(X,y)/Var X = b·σ_T²/(σ_T²+σ_E²) for classical error independent of T and U | Fuller (1987) *Measurement Error Models*; Hutcheon, Chiolero & Hanley (2010) BMJ 340:c2289 |
| 11 | Error spread 12: λ = 64/(64+144) = 64/208 = 0.308 "under a third"; simulated slope 0.30 | arithmetic; sample slope on T + 2E = 0.298 | simulation |
| 12 | Correlation of two independent readings estimates λ: r = 0.64 | Corr(T+E1, T+E2) = σ_T²/(σ_T²+σ_E²) when E1, E2 independent with equal variance; sample r = 0.637 | simulation; Spearman 1904 |
| 13 | Corrected slope 0.636/0.637 = 1.00, matching truth | 0.998 vs built-in 1.0 (sample true-data fit 1.015) | simulation |
| 14 | Spearman named this "attenuation" in 1904 and prescribed repeated measurement | Verified in text: errors' effect "is always in the direction of 'attenuating' the apparent correspondence"; "it appears necessary to make two or more independent series of observations of both p and q". Reprinted IJE 2010;39:1137. | C. Spearman (1904), "The Proof and Measurement of Association between Two Things", *American Journal of Psychology* 15(1):72–101, doi:10.2307/1412159 |
| 15 | MacMahon et al. 1990 pooled nine prospective studies, 420,000 people, blood pressure measured at baseline | Abstract: "nine major prospective observational studies: total 420,000 individuals, 843 strokes, and 4856 CHD events"; "uncorrected associations of DBP measured just at 'baseline'" | MacMahon S, Peto R, Cutler J, et al. *Lancet* 1990;335(8692):765–774, doi:10.1016/0140-6736(90)90878-9 (PubMed 1969518, abstract fetched via NCBI E-utilities) |
| 16 | Correcting for regression dilution made the associations with stroke and CHD about 60% stronger | Abstract: "These associations are about 60% greater than in previous uncorrected analyses." Shown as bars 1.0× vs 1.6× (normalised) | same |
| 17 | Limits: clean attenuation needs classical random error in one predictor; systematic error or several error-prone predictors can bias either way | Standard results (e.g. bias in other coefficients of a multiple regression can go either direction; differential/systematic error can inflate) | Hutcheon et al. 2010 BMJ; Fuller 1987; curriculum pitfall note |

Not claimed (cut because not verifiable from accessible text): the exact correction factor or remeasurement dataset MacMahon et al. used.
Note: Spearman's 1904 correction is for correlation coefficients (divide by the square root of the two reliabilities); the slope correction shown (divide by λ) is the regression-dilution form. The script says Spearman named the shrinkage and prescribed repeat measurement, which is what the text supports; it does not attribute the slope formula to him.
