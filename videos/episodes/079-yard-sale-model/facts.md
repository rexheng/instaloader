# Episode 79 — fact sheet

All room numbers come from `simulate.py` (seeded, deterministic, N = 500, $100 each,
1,000 rounds, every agent trades once per round, fair coin, numpy). They are **simulated**
and labelled so on screen.

| # | Claim (as narrated / shown) | Verification | Source |
|---|---|---|---|
| 1 | Model rule: random pairs, a fair coin picks the winner, the stake is a fixed fraction of the *poorer* trader's wealth | Matches the standard definition, Δ = γ·min(wᵢ, wⱼ) | Wikipedia "Yard-sale model"; Boghosian, *Sci. Am.* Nov 2019 |
| 2 | Called the "yard-sale model" | Name from Brian Hayes, "Follow the Money", *American Scientist* 90(5):400–405, Sept–Oct 2002 | Wikipedia; Hayes 2002 |
| 3 | The poorer-trader rule is traced to Chakraborti 2002 | A. Chakraborti, "Distributions of money in model markets of economy", *Int. J. Mod. Phys. C* 13(10):1315–1321 (2002) | Wikipedia; Greenberg & Gao, arXiv 2309.12418 review |
| 4 | "Physicists use it" | Chakraborti (statistical physicist); the model belongs to econophysics kinetic-exchange models | as above |
| 5 | 500 people × $100 = $50,000; poorer half starts with $25,000 | arithmetic | — |
| 6 | Flat $10 bets: poorer half slides from $25,000 to about $7,000 and levels off | sim: $9,430 (r100), $8,040 (r200), $7,980 (r300), $7,340 (r500), $6,800 (r1000). Fixed-amount exchange relaxes toward an exponential (Boltzmann–Gibbs) distribution whose bottom-half share is ½ + ½ ln ½ ≈ 15.3 % (≈ $7,650); our $10 granularity gives slightly less | Dragulescu & Yakovenko 2000 (EPJ B) for the exponential limit; sim |
| 7 | Yard-sale rule, same coin, 1,000 trades each: poorer half owns four cents | sim seed 1: $0.037. Seeds 1–5: $0.037–$0.085, so "a few cents" is robust; screen shows the seed-1 value | sim |
| 8 | Richest five hold a third of all the money | sim seed 1: 33.0 % (seeds 1–5: 27–33 %) | sim |
| 9 | Tallest stack ≈ $4,870 (chart rescales to $5,000) | sim seed 1 | sim |
| 10 | Win ×1.2, loss ×0.8 when she stakes 1/5 of her own money; win-then-lose = lose-then-win = 96 | 100·1.2·0.8 = 96 | arithmetic |
| 11 | (1+f)(1−f) = 1 − f², f = 0.2 → 0.96 | algebra | — |
| 12 | Break-even needs just over 55 % wins | 1.2ᵏ·0.8ⁿ⁻ᵏ ≥ 1 ⇔ k/n ≥ ln 1.25 / ln 1.5 = 0.5503 | exact |
| 13 | After 100 trades, ≈ 14 % of paths end above $100 | P(Bin(100, ½) ≥ 56) = 0.1356 | scipy.stats.binom |
| 14 | After 1,000 trades, 7 paths in 10,000 | P(Bin(1000, ½) ≥ 551) = 0.000696 | scipy.stats.binom |
| 15 | Her average stays exactly $100 | E[factor] = ½(1.2) + ½(0.8) = 1 each trade, so E = 100 for any n | exact |
| 16 | Richer player risks a smaller fraction of his own wealth (f·w_poor/w_rich < f), so his pair cost 1 − g² is smaller | algebra on the rule | — |
| 17 | 1 % per-round redistribution (w ← 0.99 w + 0.01·mean) brings the poorer half back above $8,000 and holds | sim from the condensed state: $7,650 (r100), $8,920 (r200), $8,610 (r300), $8,880 (r500), $8,270 (r600). Independent runs from equality, 3,000 rounds, seeds 1–3: 16.9–17.4 % of the money ≈ $8,500 | sim |
| 18 | Boghosian's group (Tufts) added redistribution and wealth-attained advantage ("a small edge for the rich") and fitted U.S. data from the Survey of Consumer Finances over 27 years, average error < 0.16 % | Abstract: "compare the steady-state solutions … with data from the United States Survey of Consumer Finances over a time period of 27 years … average error less than 0.16%". Fits are to Lorenz curves (paper §II–IV). Model also allows negative wealth (affine shift) | Li, Boghosian & Li, "The Affine Wealth Model", *Physica A* 516:423–442 (2019), doi:10.1016/j.physa.2018.10.042; arXiv 1604.02370 |
| 19 | SCF is run by the Federal Reserve | SCF is the Federal Reserve Board's triennial survey | federalreserve.gov/econres/scfindex.htm |
| 20 | A quarter of a million coin flips | 250 pairs × 1,000 rounds = 250,000 | arithmetic |
| 21 | Honest limit: toy model; shows chance + proportional stakes suffices, not that real fortunes are pure luck | Boghosian, *Sci. Am.* 2019 ("x-ray … strip away the messiness"); curriculum pitfall | — |

Not used (could not verify precisely enough or off-idea): Sugarscape; specific Gini values of
real countries.
