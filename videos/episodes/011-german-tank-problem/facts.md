# Episode 11: facts and verification

All toy numbers come from one hand-picked **simulated** capture (on screen as "simulated")
of k = 5 serial numbers {8, 14, 22, 31, 89} from a factory of N = 100. They were checked
with numpy (`np.random.default_rng(11)`, 100,000 simulated captures of 5 from 1..100;
the scene uses 10,000 with the same seed and gives the same rounded figures).

| # | Claim (as spoken / shown) | Verification | Source |
|---|---|---|---|
| 1 | The average of 8, 14, 22, 31, 89 is 32.8. Doubled, that is 65.6, or "about sixty six" | Exact arithmetic: 164/5 = 32.8 | computed |
| 2 | 66 is below serial 89, which is already in hand, so the estimate is impossible | 65.6 < 89 | computed |
| 3 | Likelihood of this sample given N: 1/C(N,5) for N >= 89 and 0 below. It decreases in N, so it peaks at N = 89 = max (the MLE) | Standard result. Relative values: L(100)/L(89) = 0.551, L(120)/L(89) = 0.218 | Wikipedia "German tank problem"; Goodman 1952 JASA |
| 4 | Simulation: 2 x mean averages about 101, i.e. "centers near a hundred". It falls below the sample's own max in about 19% of captures ("about one in five") | numpy: mean 101.0, sd 25.3, P(2*mean < max) = 0.192 | simulated |
| 5 | The max never overshoots N. It averages about 84, "sixteen tanks short" | Exact E[max] = k(N+1)/(k+1) = 84.17. Simulated mean 84.17 | exact + simulated |
| 6 | Unseen numbers below 89: 89 - 5 = 84, spread over 5 gaps (1-7, 9-13, 15-21, 23-30, 32-88 = 7+5+7+8+57 = 84). Average gap 16.8 ("about seventeen") | Exact | computed |
| 7 | Estimate: 89 + 16.8 = 105.8 ("about a hundred and six"). Formula m + (m-k)/k = m(1 + 1/k) - 1 | Algebra: m + m/k - 1. This is the minimum-variance unbiased estimator | Wikipedia "German tank problem" (frequentist analysis); Goodman 1952 |
| 8 | Gap estimator on the simulation: averages 100, with "about a third less spread" than doubling the average | sd 16.56 (exact sqrt((N-k)(N+1)/(k(k+2))) = 16.56) vs 25.33, so 35% less | exact + simulated |
| 9 | The gap above the max is, on average, the same as the gaps below it | The k+1 gaps of a uniform sample without replacement are exchangeable | standard (order statistics) |
| 10 | August 1942: Allied intelligence estimated 1,550 German tanks a month, the serial-number analysis 327, and German records 342 | Table in Ruggles & Brodie (1947), reproduced in Simon (2023, arXiv 2301.00046, Table 1) and in Scientific American ("How Math Helped the Allies Win WWII"). Both cite Ruggles & Brodie | Ruggles, R. & Brodie, H. (1947). An Empirical Approach to Economic Intelligence in World War II. JASA 42(237):72-91, doi:10.1080/01621459.1947.10501915 |
| 11 | "Other months missed by more, by as much as forty percent" | Same table: June 1940 169 vs 122 (+39%); June 1941 244 vs 271 (-10%); Aug 1942 327 vs 342 (-4%) | same |
| 12 | The analysis used captured gearbox serial numbers. Gearbox numbers ran in unbroken sequences; chassis numbers came in blocks with gaps, which made them harder to use | Simon 2023, footnote 2: "Gearboxes on captured tanks ... unbroken sequence. Chassis serial numbers ... broken into blocks". Wikipedia: chassis and engine numbers were "more complicated" to use | Ruggles & Brodie 1947 via Simon 2023; Wikipedia |
| 13 | Ratio in the stakes beat ("more than four times too high") | 1550/342 = 4.5 | computed |

## Hedges and deliberate omissions
- The narration says the economists ran "this kind of serial number analysis" and does not claim they used exactly m(1+1/k) - 1. Their published method was more elaborate: several components, plus estimating monthly output from serial ranges.
- The often-quoted "246 vs 1,400 vs 245 per month" summary was cut. It comes through secondary sources (a 2006 newspaper column), and I could not trace it to the 1947 table. Only the three table rows are used.
- The toy factory (N = 100) and its capture are simulated, and the screen says so.
