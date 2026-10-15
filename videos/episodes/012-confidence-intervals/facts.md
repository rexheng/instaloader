# Facts — Episode 12 (confidence intervals)

| # | Claim (as narrated / shown) | Verification | Source |
|---|---|---|---|
| 1 | Survey scenario: a 95% CI for a mean "from 0.1 to 0.4"; statement "There is a 95% probability that the true mean lies between 0.1 and 0.4" | Read in the paper's Method section (statement 4, verbatim) | Hoekstra, Morey, Rouder & Wagenmakers (2014), *Psychon. Bull. Rev.* 21(5):1157–1164, doi:10.3758/s13423-013-0572-3 |
| 2 | "Twenty fourteen", "Hoekstra and colleagues" | Article metadata: vol. 21 issue 5, Oct 2014 (online Jan 2014); authors Hoekstra, Morey, Rouder, Wagenmakers | same |
| 3 | 118 psychology researchers; 59% ticked true | Table 1: Researchers (n = 118 after removing 2 incomplete responses from 120), statement 4 endorsed by 59%. Waffle shows 70/118 = 59.3% filled | Table 1 of the paper |
| 4 | "The survey's authors had written it as a false statement" | Paper: "all six statements were false"; statements 1–4 "assign probabilities to parameters or hypotheses, something that is not allowed within the frequentist framework" | same |
| 5 | Researchers endorsed on average ~3.5 of 6 false statements, about as many as first-year students who had not been taught inference | Means: first-years 3.51, masters 3.24, researchers 3.45; first-years "had not yet taken any class on inferential statistics" | same, Results + Method |
| 6 | Simulated world: μ = 0.25, σ = 0.13, n = 5 | Our choice; labelled "simulated" on screen (axis title + tag) | sim.py |
| 7 | z-interval x̄ ± 1.96 s/√5 covers 88% in the long run | Exact: P(|t₄| ≤ 1.96) = 0.8784; 10⁶ simulated runs: 0.8782 | sim.py (scipy.stats.t) |
| 8 | Displayed 100 runs: 88 hits / 12 misses; first 4 runs hit | Seed 4335 chosen so the displayed sample matches the long-run rates (88 and 95) and fits the axis; stated as "simulated" | sim.py |
| 9 | 11 of the 12 displayed misses are in the narrower half; over 10⁶ runs "nearly nine in ten misses come from the narrower half" | Long run: P(s below median ∣ miss) = 0.888 | sim.py |
| 10 | Fix: multiply by 2.78 instead of 1.96 | t₀.₉₇₅ with 4 df = 2.7764 → shown as 2.78; ratio 2.776/1.96 = 1.417 ("every bar stretches by the same factor") | scipy |
| 11 | With 2.78: 95 of the 100 displayed runs hit; 10⁶ runs: 95.0% | Exact coverage 0.95 by construction; 10⁶ sim: 0.9502; seed 4335 gives 95/100 | sim.py |
| 12 | Gosset, writing as "Student", 1908 | "The probable error of a mean", *Biometrika* 6(1):1–25; pseudonym because of Guinness policy. (Gosset derived the distribution; the modern t-quantile form was popularised later by Fisher — narration says "worked out the fix", which is accurate.) | Wikipedia "William Sealy Gosset"; MIT OCW reading list |
| 13 | Neyman's theory of confidence intervals, 1937 | "Outline of a theory of statistical estimation based on the classical theory of probability", *Phil. Trans. R. Soc. A* 236(767):333–380, doi:10.1098/rsta.1937.0005. (Neyman first used the term in 1934; the 1937 paper is the full theory, so the narration says "theory … from 1937", not "invented".) | Royal Society archive; ProofWiki |
| 14 | "The probability is one or zero" for a computed interval | Frequentist: μ is a fixed constant, 0.1 ≤ μ ≤ 0.4 is either true or false | Neyman 1937; Hoekstra et al. 2014 |
| 15 | A Bayesian credible interval does carry the "95% chance for this interval" reading, but only given a prior | Standard. The purple curve is the posterior for μ under the reference prior p(μ,σ) ∝ 1/σ: μ ∣ data ~ x̄ + (s/√5)·t₄, with x̄ = 0.25, s/√5 = 0.054 → 95% central mass is exactly 0.1 to 0.4 | Gelman et al., *Bayesian Data Analysis* ch. 3 (normal model, noninformative prior) |
| 16 | Coverage holds only under its assumptions (random sampling, model fits) | Standard; t-interval assumes iid normal data | — |

Not used (could not make fully precise in one line): the 3% of researchers who rejected all six statements (true: 3 researchers, 3%; cut for length).
