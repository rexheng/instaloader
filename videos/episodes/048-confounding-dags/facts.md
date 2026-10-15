# Episode 48 — facts and verification

All numbers recomputed by `check_numbers.py` (in this directory) from Table 1 of Matthews (2000).
Source PDF read in full: Matthews, R. (2000). "Storks Deliver Babies (p = 0.008)". *Teaching Statistics* 22(2): 36–38. doi:10.1111/1467-9639.00013 (copy at brixtonhealth.com/storksBabies.pdf).

| # | Claim (narration / screen) | Verification | Source |
|---|---|---|---|
| 1 | 17 European countries; stork breeding pairs vs births per year | Table 1 lists 17 countries with area (km²), storks (pairs), humans (10⁶), births (10³/yr). Storks 1980–1990 (Harbard, RSPB, pers. comm.); demographics Britannica Yearbook 1990. Data are real, not simulated. | Matthews 2000, Table 1 |
| 2 | r = 0.62, p = 0.008 | Recomputed: r = 0.6203, t = 3.063, df 15, two-sided p = 0.0079. Paper: r = 0.62, t = 3.06, p = 0.008. | Matthews 2000; check_numbers.py |
| 3 | "about once in a hundred and twenty-five" | Paper: "only a 1 in 125 chance of obtaining at least as impressive a value assuming the null hypothesis". 1/0.0079 = 127, so "about 1 in 125" is correct. Phrased as conditional on no relation, not as P(fluke). | Matthews 2000 p. 37 |
| 4 | Matthews' point that suspected diet–cancer links are investigated by the same kind of correlational study | Paper p. 36: "If one were approaching the question in the same way that many other links are investigated (e.g. suspected links between diet and cancer risk), one may well decide to carry out a correlational study". | Matthews 2000 |
| 5 | Naive slope: +10,000 pairs → +288 thousand births; ≈ 29 babies per pair per year | OLS births(10³) on storks: slope 0.02879 → 287.9 thousand per 10,000 pairs, 28.8 births per pair. | check_numbers.py |
| 6 | Land area vs births r = 0.92; land area vs storks r = 0.58 | 0.9225 and 0.5793. | check_numbers.py |
| 7 | Land area as the confounder | Matthews: "One candidate for a potential confounding variable is land area: readers are invited to investigate this possibility using the data in table 1." The DAG arrows (area → births, area → storks) are our stated assumption, shown as such. | Matthews 2000 p. 38 |
| 8 | births = a + b·storks + c·area; b on trial | Standard linear adjustment; coefficients a = −7.4, b = 0.00599, c = 0.00158 (births in 10³). | check_numbers.py |
| 9 | Turkey: size predicts ~18 thousand pairs and ~1.3 million births; residual (6.9k, 241k) | Linear fit of storks on area and births on area: 18,106 pairs; 1,335 thousand births. | check_numbers.py |
| 10 | Subtracting what size predicts from both axes and refitting gives b | Frisch–Waugh–Lovell theorem: slope of residuals = 5.99, identical to the multiple-regression b. | check_numbers.py |
| 11 | After adjustment b ≈ 6 babies per pair, p = 0.31 | b = 5.99 births/pair, p = 0.307 (df 14), 95% CI [−6.1, 18.1] includes 0 → "indistinguishable from zero with 17 countries". | check_numbers.py |
| 12 | Back-door rule: adjust for a set that blocks every back-door path (and contains no descendant of the cause) | Pearl's back-door criterion; first stated Pearl (1993, *Statistical Science*), textbook form in *Causality* (Cambridge University Press, 2000; 2nd ed. 2009), §3.3. | Pearl 2000 |
| 13 | A DAG is an assumption; regressions cannot draw it | Curriculum pitfall; Pearl's framework: a DAG encodes causal assumptions that data alone (correlations) cannot in general identify. | Pearl 2000 |
| 14 | Adjusting for a variable that two arrows point into (a collider) opens a path | Standard d-separation: conditioning on a collider unblocks the path through it. | Pearl 2000 |

Not used (checked and cut): the hormone-therapy observational vs. WHI-trial reversal. The discrepancy is partly attributed to timing/age of initiation (Hernán et al. 2008, *Epidemiology*), not purely confounding, so it would overstate the case.

Honest caveat known but not voiced (one idea per episode): without Turkey, r = 0.34, p = 0.20, so the raw correlation leans heavily on one country; this is consistent with the size story (Turkey is by far the largest country).
