# 052 facts and verification

Primary source read in full text (pages 1-10): Card, D. & Krueger, A. B. (1994). "Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania." *American Economic Review* 84(4): 772-793. PDF: https://davidcard.berkeley.edu/papers/njmin-aer.pdf

| # | Claim (narration / screen) | Verification | Source |
|---|---|---|---|
| 1 | NJ minimum wage rose from $4.25 to $5.05 on April 1, 1992 | Verified, first sentence of the abstract | C&K 1994 abstract |
| 2 | Pennsylvania's minimum stayed at $4.25 | Verified: PA was at the federal minimum, $4.25 since April 1, 1991 (C&K §I); "Pennsylvania (where the minimum wage was constant)" | C&K 1994 abstract, §I |
| 3 | The raise was +80 cents, about 19% | 0.80 / 4.25 = 0.188 -> 19% (computed) | arithmetic |
| 4 | "Textbook economics says ... should cut jobs" | Verified: "The prediction from conventional economic theory is unambiguous: a rise in the minimum wage leads perfectly competitive employers to cut employment (George J. Stigler, 1946)" | C&K 1994 p. 772 |
| 5 | Surveyed 410 fast-food restaurants: 331 NJ, 79 PA | Verified, Table 1 (wave 1 interviewed 410 = 331 + 79; 473 in frame) | C&K 1994 Table 1 |
| 6 | Survey once just before the raise, again ~8 months after | Verified: wave 1 Feb 15-Mar 4 1992; wave 2 Nov 5-Dec 31 1992 ("7-8 months after") | C&K 1994 Table 1, intro |
| 7 | FTE: part-timer counts as half a worker | Verified: "number of full-time workers [including managers] plus 0.5 times the number of part-time workers" | C&K 1994 §II, Table 3 notes |
| 8 | NJ FTE per store 20.44 before, 21.03 after; change +0.59 | Verified, Table 3 rows 1-3 col (ii) | C&K 1994 Table 3 |
| 9 | PA FTE per store 23.33 before, 21.17 after; change -2.16 | Verified, Table 3 col (i) | C&K 1994 Table 3 |
| 10 | NJ - PA after = -0.14; before = -2.89 | Verified, Table 3 col (iii) | C&K 1994 Table 3 |
| 11 | 1992 was a recession year in NJ | Verified: "the rise in the minimum wage occurred during a recession"; unemployment in NJ, PA, NY trended up 1991-93 | C&K 1994 intro, §III.A |
| 12 | Ghost NJ = 20.44 - 2.16 = 18.28 ("eighteen point three") | computed | arithmetic |
| 13 | DiD from rounded table means = 0.59 - (-2.16) = 2.75 = (-0.14) - (-2.89) | computed with python, both routes give 2.75 | arithmetic |
| 14 | Paper reports DiD 2.76 (SE 1.36), t = 2.03, about 13% | Verified, Table 3 row 3 col (iii) and §III.A text. 2.76 vs 2.75 is rounding of the unrounded group means; screen says "2.76 from unrounded means" | C&K 1994 Table 3 |
| 15 | 95% interval for 2.76 +/- 1.96 x 1.36 = [0.09, 5.43] | computed (shown as an interval bar, labelled ±1.96 SE) | arithmetic |
| 16 | "No sign that the higher wage cut jobs" | Verified: "We find no indication that the rise in the minimum wage reduced employment." | C&K 1994 abstract |
| 17 | Neumark & Wascher, payroll records, found a decline | Verified: "Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania: Comment", AER 90(5):1362-1396 (2000); payroll data for ~235 restaurants; NJ employment fell relative to PA (NBER w5224 abstract: ~4.6% relative decline) | nber.org/papers/w5224; AER 2000 |
| 18 | Card & Krueger reply with government (BLS ES-202) records, found no drop | Verified: "Minimum Wages and Employment: ... Reply", AER 90(5):1397-1420 (2000); NBER w6386: little or no effect of the NJ increase on fast-food employment | nber.org/papers/w6386 |
| 19 | C&K 1994 had a single pre-period survey, so no pre-trend check in that data | Verified from the design: one wave before (Feb-Mar 1992), one after. (Their within-NJ high-wage-store comparison is a different specification test.) | C&K 1994 Table 1, §III.A |
| 20 | Pre-trend panel | SIMULATED, labelled "simulated" on screen. Control y = 22 - 0.3t; treated y = 18 + 0.5t for t = -3..2, true effect 0. Ghost from t = 0 parallel to control: 18 - 0.3t. Reported "effect" at t = 2: 19.0 - 17.4 = 1.6 | constructed |

Not used (could not justify the words / time): Card's 2021 Nobel, Krueger's death (2019), John Snow 1855.
