# Episode 27 — fact sheet

Every number spoken or shown, how it was checked, and where it comes from.

## Simulated survey (on screen: "simulated")

All produced by `data.py` in this directory (run `python3 data.py`; seeds fixed).
300 people, age ~ U(20, 65), income ($ thousands) = 18 + 0.9·(age − 20) + N(0, 11), floored at 8.
Each eraser removes exactly 90 people (30 %), drawn without replacement with probability
proportional to a skip propensity (constant / logistic in age / logistic in income).

| Quantity | Value | Shown as | Spoken as |
|---|---|---|---|
| True mean income, all 300 | 39.25 k | $39,250 | "thirty-nine thousand, two hundred and fifty" |
| Eraser 1 (coin flip, MCAR): mean of the 210 answers | 38.79 k (err −0.46 k) | $38,790 / −$460 | "under five hundred dollars" |
| Eraser 2 (young skip, MAR): mean of answers | 43.87 k (err +4.62 k) | $43,870 / +$4,620 | "about forty-six hundred dollars" too high |
| Eraser 2, filled from survivors' line + residual noise | 39.42 k (err +0.17 k) | $39,420 / +$170 | "under two hundred dollars" |
| Eraser 3 (high earners skip, MNAR): mean of answers | 33.59 k (err −5.66 k) | $33,590 / −$5,660 | "about fifty-seven hundred" too low |
| Eraser 3, filled from survivors' line + residual noise | 36.42 k (err −2.83 k) | $36,420 / −$2,830 | "about twenty-eight hundred" low |
| Skip propensity ranges | MAR 0.01–0.89, MNAR 0.00–0.99; mean 0.30 each | fog opacity | — |

Arithmetic check on displayed values (all rounded to $10): 39,250 − 38,790 = 460; 43,870 − 39,250 = 4,620;
39,420 − 39,250 = 170; 39,250 − 33,590 = 5,660; 39,250 − 36,420 = 2,830.

Typicality (199 repeated erasures, same population, not cherry-picked): MCAR deletion error mean −0.03 k, sd 0.62 k
(the shown −0.46 k is a typical size); MAR deletion +4.45 ± 0.46 k, MAR fill +0.19 ± 0.63 k; MNAR deletion
−5.67 ± 0.30 k, MNAR fill −2.78 ± 0.48 k. So the shown run is representative.

Why the fix works under MAR: skip probability depends only on age, so within any age slice the survivors are a
random subsample; OLS of income on age fitted to survivors is unbiased for the population line, and filling
from it (plus residual noise) recovers the mean. Under MNAR the skip probability rises with income within each
age slice, so survivors sit low in every slice, the fitted line sinks (survivor line: intercept 1.17, slope
0.811 vs population −0.06, 0.896), and fills inherit the sink. (Verified numerically above.)

## Definitions / theory

- **"Missing at random" defined by Rubin (1976).** Rubin, D. B. (1976). Inference and missing data.
  *Biometrika* 63(3): 581–592, doi:10.2307/2335739. Abstract (Harvard DASH record): ignoring the process that
  causes missing data is appropriate when "the missing data are missing at random and the observed data are
  observed at random". Verified. On screen: "Rubin, 1976 · Biometrika". We say Rubin *named* missing at random;
  we do NOT claim he coined "MCAR"/"MNAR" (attribution of those labels is less clear).
- **Formula shown:** P(blank | age, income) = P(blank | age) — the MAR condition for this two-variable survey
  (missingness depends only on the observed covariate). Standard textbook statement (Little & Rubin,
  *Statistical Analysis with Missing Data*). The MNAR version shows ≠.
- **MAR vs MNAR cannot be told apart from observed data.** Molenberghs, G., Beunckens, C., Sotto, C. &
  Kenward, M. G. (2008). Every missingness not at random model has a missingness at random counterpart with
  equal fit. *JRSS Series B* 70(2): 371–388, doi:10.1111/j.1467-9868.2007.00640.x. Verified via IDEAS/RePEc and
  LSHTM repository. Spoken: "every not-at-random model has an at-random twin that fits the observed data just as
  well". On screen: "Molenberghs et al., 2008 · JRSS B".

## Real-world anchor

Bollinger, C. R., Hirsch, B. T., Hokayem, C. M. & Ziliak, J. P. (2019). Trouble in the Tails? What We Know about
Earnings Nonresponse 30 Years after Lillard, Smith, and Welch. *Journal of Political Economy* 127(5): 2143–2185
(verified on RePEc). Text read from IZA DP 11710 (2018 version).

- "by 2015 total (item and whole) nonresponse in the ASEC reached 43 percent" (main text, Fig. 1);
  Appendix A.2: "in survey year 2016 the total earnings nonresponse rate was 43 percent, with item nonresponse
  accounting for 24 percentage points and whole supplement nonresponse 19". Spoken: "by the twenty sixteen
  survey, forty-three percent of earnings went unreported" — Census fills these with a hot-deck imputation.
- The CPS ASEC is the source of the Census Bureau's official annual income and poverty estimates
  (census.gov, "Income in the United States" / "Poverty in the United States" reports). Spoken as "America's
  official income and poverty numbers come from a survey…".
- Linked CPS ASEC 2006–2011 to Social Security Administration Detailed Earnings Records (2005–2010 earnings).
  "The common assumption that earnings are missing at random is rejected. Nonresponse across the earnings
  distribution is U-shaped, highest in the left and right tails." (abstract)
- Bar chart = Table 3, column (1), men, nonresponse rate by DER earnings decile / top percentiles (decile
  dummies only, OLS, linkage-weighted): 26.7, 25.3, 21.7, 21.0, 18.9, 17.9, 17.8, 17.6, 18.5 (deciles 1–9),
  20.0 (pct 91–95), 19.9, 22.7, 25.2, 27.1, 32.0 (pct 96, 97, 98, 99, 100).
  Spoken: bottom tenth "more than a quarter" (26.7 %), middle "under a fifth" (deciles 5–9: 17.6–18.9 %),
  top one percent "nearly a third" (32.0 %). Labeled bars: 27 %, 19 % (median decile), 32 %.
  On screen: "Bollinger et al., 2019 · J. Political Economy".

## Cut / not claimed
- No claim about who coined "MCAR" or "MNAR".
- No claim about women's rates (U-shape is weaker for women; we say "among men").
- Multiple imputation's variance step is not covered (one idea only); the fill shown is a single stochastic
  regression imputation, described as "fill from that line, plus the usual scatter".
