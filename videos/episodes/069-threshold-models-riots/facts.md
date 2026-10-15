# Episode 69 — facts and verification

Primary source read in full (PDF): Mark Granovetter, "Threshold Models of Collective Behavior",
*American Journal of Sociology* 83(6), May 1978, pp. 1420–1443. doi:10.1086/226707.
Copy used: https://www.gwern.net/doc/sociology/1978-granovetter.pdf

| # | Claim (as narrated / shown) | Verification | Source |
|---|---|---|---|
| 1 | A threshold is "how many others must already be rioting before that person joins". | Granovetter's abstract: "the number or proportion of others who must make one decision before a given actor does so". | Granovetter 1978, abstract |
| 2 | Crowd A: 100 people with thresholds 0, 1, 2, …, 99 → everyone riots (equilibrium 100). | Paper p. 1424–25: "one individual with threshold 0, one with threshold 1 … up to … 99 … until all 100 people have joined. The equilibrium is 100." Recomputed: iteration r ← #{θ ≤ r} from r = 0 goes 0,1,2,…,100 and stops at 100. | Granovetter 1978 p.1424–25; sim.py |
| 3 | Crowd B: replace the threshold-1 person with a threshold-2 person → one rioter. | Paper p. 1425: "Remove the individual with threshold 1 and replace him by one with threshold 2 … the riot ends at that point, with one rioter." Recomputed: r goes 0 → 1, then #{θ ≤ 1} = 1, stop. | Granovetter 1978 p.1425; sim.py |
| 4 | Average thresholds: 49.5 (A) and 49.51 (B). | Exact: sum 0..99 = 4950 → 49.5; B sum = 4950 − 1 + 2 = 4951 → 49.51. | arithmetic |
| 5 | "Off by ninety-nine people." | 100 − 1 = 99. | arithmetic |
| 6 | Equilibrium = first point where the cumulative threshold count F(r) meets the line y = r (F(r) = r). | Paper p. 1426: "That limit is the point where the c.d.f. first crosses the 45° line from above. Algebraically … F(r) = r." | Granovetter 1978 p.1426, Fig. 1 |
| 7 | Crowd A's staircase F(r) = r + 1 sits one step above the line for every r < 100; crowd B has F(1) = 1. | Direct count. | sim.py |
| 8 | Normal thresholds, mean 25, N = 100: equilibrium creeps up to about six, then near a standard deviation of about 12.2 jumps to nearly 100. | Paper p. 1427 & Fig. 2: "Up until a critical point … the equilibrium number of rioters increases gradually to about six. Then after this point, approximately 12.2, the value … jumps to nearly 100". Recomputed (continuous, first root of 100·Φ((r−25)/σ) − r from 0): σ=10 → 0.8, σ=12 → 4.0, σ=12.2 → 5.5, critical σ = 12.22, σ=12.3 → 100.0, σ=15 → 100.0. On screen marked "recomputed". | Granovetter 1978 p.1427 Fig. 2; sim.py |
| 9 | The mean (25) never changes during that sweep. | By construction. | — |
| 10 | Newspaper quotes: "A crowd of radicals engaged in riotous behavior" / "A demented troublemaker broke a window while a group of solid citizens looked on." | Verbatim, paper p. 1425. | Granovetter 1978 p.1425 |
| 11 | "The two crowds are almost identical in composition" / hazardous to infer dispositions from outcomes. | Paper p. 1425 and abstract. | Granovetter 1978 |
| 12 | Honest limit: stylized model; says nothing about a specific real riot; thresholds are not directly observable. | Paper's own section "Issues of measurement, falsification, verification"; curriculum pitfall note. Stated as a limit, no number. | Granovetter 1978 |

Things deliberately cut: friendship-network results (true in the paper — modal outcome one rioter for the uniform crowd under most social-structure settings — but needs a weighted-proportion explanation that does not fit); 37% chance of no instigator under random sampling (true: 0.99^100 = 0.366) — cut for concision.
