# Facts check — episode 56

| Claim (screen / narration) | Verification | Source |
|---|---|---|
| 20 equally spaced looks at two-sided z = 1.96 under H0 give ≈ 25 % false positives | Monte Carlo, 2,000,000 Gaussian random walks: 0.248. Matches the 24.8 % value tabulated after Armitage et al. (1969) in secondary sources | sim.py (scratch) ; Armitage, McPherson & Rowe 1969 JRSS A 132(2):235–244 |
| 1 / 2 / 5 / 10 / 20 / 100 looks → 5.0 / 8.3 / 14.2 / 19.3 / 24.8 / 37.3 % | Monte Carlo (2 M walks): 0.0502, 0.0834, 0.1418, 0.1934, 0.2480, 0.3733. 14.2 % and 24.8 % confirmed in a secondary summary of the 1969 table; 10 looks "nearly 20 %" confirmed by James Lind Library on McPherson (1974). On screen rounded to 5, 8, 14, 19, 25, 37 | own simulation; jameslindlibrary.org |
| Treating 20 looks as independent would give 64 % | 1 − 0.95^20 = 0.6415 (not used in narration) | exact |
| Day 11's z is built mostly from day 10's data | cumulative data: day 11 contains days 1–10 (10/11 of visitors); corr(Z10, Z11) = √(10/11) = 0.953, simulated 0.9535 | exact + sim |
| Concrete dataset: 1,000 A/A tests, 10 % click rate both arms, 500 visitors/arm/day, 20 days, pooled two-proportion z-test | make_data.py seed 47 (seed chosen so the counts are representative of the 2 M-walk expectation: 249 vs 248 expected, 52 vs 50, 49 vs 50) | make_data.py, data.npz |
| 249 / 1000 stop with a "winner" under daily peeking | data.npz | simulated |
| 52 / 1000 outside ±1.96 at day 20 only | data.npz | simulated |
| first-crossing slices day 1 = 55 (≈ 5 %), day 2 = 30 (≈ 3 %), decreasing thereafter | data.npz; expected values from 2 M walks: 5.0 %, 3.3 %, 2.4 %, 1.9 %, … 0.41 % | simulated |
| Hero test: crosses z = 2.02 on day 7 (p = 0.043 → "point oh four"), ends day 20 at z = 0.70 | data.npz test #990; p = 2(1 − Φ(2.02)) = 0.0434 | simulated |
| O'Brien–Fleming boundary for 20 looks: c·√(20/k), c = 2.127 so total α = 0.05 | bisection on 1 M walks: c = 2.127 → day-20 boundary 2.13 (shown "2.13") | own computation; O'Brien & Fleming 1979 Biometrics 35(3):549–556 (shape c√(K/k)) |
| With the funnel, 49 / 1000 simulated tests stop with a winner (4.9 %) | data.npz | simulated |
| Armitage, McPherson & Rowe 1969 computed the inflation from repeated significance tests on accumulating (normal / binomial) data | Crossref: J. R. Stat. Soc. A 132(2):235, doi 10.2307/2343787; abstract: "probability that at some stage the test criterion is significant may be substantially greater than the nominal value" | crossref, jameslindlibrary.org |
| "Medical statisticians mapped this trap decades before A/B tests" | Armitage was a medical statistician (London School of Hygiene & Tropical Medicine); paper motivated by clinical trials; web A/B testing became common in the 2000s | James Lind Library |
| Johari, Koomen, Pekelis & Walsh 2017 KDD, with Optimizely, always-valid p-values robust to continuous monitoring | Crossref doi 10.1145/3097983.3097992: authors Johari, Koomen, Pekelis, Walsh; KDD '17 pp. 1517–1525. KDD talk abstract: always valid p-values "provably robust" to peeking; deployed by Optimizely. Pekelis employed / Johari advisor at Optimizely; Koomen co-founded Optimizely | crossref, videolectures.net, arXiv 1512.04922 |
| Always-valid p-values keep the false-positive rate ≤ 5 % for any monitoring schedule | Definition in Johari et al.: P(p_T ≤ α) ≤ α for any stopping time T | arXiv 1512.04922 |
| "Looking is harmless; stopping because of what you saw is what spends the budget" | Type I error only depends on the decision rule; looking without changing the stopping decision leaves the single-analysis rate unchanged (curriculum pitfall note) | standard |
