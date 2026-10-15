# 090 · Fact check

Every number spoken or shown, how it was checked, and where it comes from.

## Real-world claims

| Claim (as used) | Verified? | Source / note |
|---|---|---|
| Pew phone poll of "fifteen hundred" Americans | Yes | Pew 2012, *About the Study*: standard survey "conducted January 4-8, 2012 among 1,507 adults". |
| Lands within four points of the government on homeownership (63 vs 62), marriage (50 vs 54), citizenship (95 vs 92) | Yes | Pew 2012, Section 1 table "Demographic Profiles Match on Gender, Age but Not on Education" (standard survey vs US government survey). These three rows are "based on fully weighted data". Gaps 1, 4, 3. |
| Government: 27% volunteered last year; Pew poll: 55% | Yes | Pew 2012, Section 1 "Effects of Over-Representing Volunteers": "55% … did some type of volunteer work for or through an organization in the past year … compared with 27% … in the Current Population Survey". Benchmark = CPS September 2011 Volunteering Supplement (Pew, *Government Benchmarks*); BLS reports 26.8% for the year ending Sept 2011. Survey figures are weighted. |
| 28 points, "nearly ten times the margin of error" | Yes (arithmetic) | 55 − 27 = 28; Pew: standard survey MoE ±2.9 points (design-effect adjusted). 28 / 2.9 = 9.66. |
| "Pew traces the gap at least partly to who agreed to talk" | Yes | Pew: "the differences are likely, at least partly, a result of non-response bias. But the context in which the questions are asked could not be replicated exactly and may have contributed". "People who volunteer are more likely to agree to take part in surveys" (citing Abraham, Helms & Presser 2009, AJS). |
| 9% of households took part, down from 36% in 1997 | Yes | Pew 2012: "obtained interviews in just 9% of sampled households … response rates have declined steadily, from 36% in 1997". (AAPOR RR3.) |
| 39% of respondents had a college degree vs 28% of adults | Yes | Pew 2012 Section 1: "39% of respondents in the standard survey say they graduated from college. That compares with 28% of adults in the Current Population Survey." (Table note: these are weighted only for probability of selection, i.e. before demographic weighting.) |
| Graduates volunteer more | Yes | BLS 2011: bachelor's+ 42.4% vs HS grad 18.2%, < HS 9.8%, some college 29.5% (age 25+). |
| Pew's real poll was weighted on education, age, sex and race, and still said 55 | Yes | Pew *About the Study → Weighting*: raked to "gender, age, education, race, Hispanic origin and nativity, region, population density and telephone status"; 55% is "based on weighted data". |
| UNH 2016: weighted on age, sex and region but not education; Clinton +11; won by < 0.5 (0.4); with an education weight the poll matched the result | Yes | AAPOR 2017, §3.4: "The final University of New Hampshire (UNH) poll had Clinton leading in the Granite State by 11 points. She ultimately won by a razor thin 0.4-point margin … adjusted for age, gender and region but not education … 'When we include a weight for level of education, our predictions match the final number.' … that single modification would have removed essentially all of the error." |
| Reweighting Pew's poll to the CPS volunteer share: Republican share 41 → 39 | Yes | Pew 2012 Section 1: "the volunteer-weighted estimate of the Republican share is only two points lower than the standard weighting (39% vs. 41%)" (Republicans + leaners). |
| "The bias reaches only answers linked to answering" | Yes (paraphrase) | Pew: re-weighting "has very little impact on the survey estimates … political views"; significant changes only for behaviours linked to volunteering (talking with neighbours, contacting officials −5, church attendance −6, voting frequency). |
| Homes, marriage, citizenship "barely linked to who picks up" | Inference, stated as such in context | They match the benchmark after weighting, which implies little residual link between responding and these answers. Phrased as explanation of the match, not as a measured result. |

## Simulated numbers (labelled "simulated" on screen)

Model: two education columns. Population: graduates W = 0.28 (CPS share), volunteer rate 0.42
(BLS bachelor's+ 42.4%); everyone else 0.72, volunteer rate 0.21 (BLS < HS / HS / some-college
mix ≈ 21%). Volunteers answer k = 3.3 times as often as non-volunteers in every column; graduates
answer 1.24× as often as non-graduates (chosen so 39% of respondents are graduates, as in Pew).

Exact computation (python, `scratch`):

| Quantity | Value | Shown |
|---|---|---|
| true volunteer share 0.28·0.42 + 0.72·0.21 | 0.2688 | 27% |
| graduate-column height h₁ = 0.42k / (0.42k + 0.58) | 0.7050 | 70% |
| other-column height h₂ = 0.21k / (0.21k + 0.79) | 0.4673 | 47% |
| raw estimate 0.39·h₁ + 0.61·h₂ | 0.5600 | 56% |
| weighted estimate 0.28·h₁ + 0.72·h₂ | 0.5338 | 53% (0.28·0.70 + 0.72·0.47 = 0.534) |
| misses vs 27 | 29.1 → 26.5 | 29 → 26 (from displayed integers: 56−27, 53−27) |
| gaps inside columns | 70−42 = 28, 47−21 = 26 | "more than twenty-five points" |
| Monte Carlo check (2M people, seed 7) | raw 0.5595, weighted 0.5334, resp. graduates 39.0%; s.d. of a 1,507-person poll's weighted estimate 1.3 points | consistent |

Odds step (single column, p = 0.27):
- k = 2 → 0.27·2 / (0.27·2 + 0.73) = 0.4252 → "forty-three" (42.5 rounds to 43, shown as 43%).
- k needed for 55%: (0.55/0.45) / (0.27/0.73) = 3.30 → "about three point three".
- k = 3.3 → 0.5497 → 55%.

The model is an illustration of the mechanism, not an estimate of Pew's actual response
propensities; the narration says "simulated" and the screen says "simulated".
