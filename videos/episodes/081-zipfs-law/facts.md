# Facts: Episode 81 (Zipf's law)

Every number below was recomputed by `make_data.py`, which writes `data.json`. English data comes from NLTK's copy of the Brown Corpus (all 500 texts, tokens lower-cased, pure-punctuation tokens dropped). The monkey data is a numpy simulation (seed 7).

| # | Claim (as narrated or shown) | Verification | Source |
|---|---|---|---|
| 1 | "A million words of American English" | 1,013,319 word tokens after punctuation is removed. Kučera & Francis describe ~1,014,000 words of American English text printed in 1961 | Recomputed; Kučera & Francis 1967; Wikipedia "Brown Corpus" |
| 2 | "the" appears ~70,000 times (69,971 on screen) | 69,971, which is exactly the classic Kučera–Francis figure. It is 6.9% of tokens | Recomputed |
| 3 | "of" is runner-up, "about half as often" (36,412 on screen) | 36,412 (the classic list has 36,411). 36,412 / 69,971 = 0.52 | Recomputed |
| 4 | Bars for and/to/a/in: 28,853 / 26,158 / 23,195 / 21,337 | Recomputed | Recomputed |
| 5 | Counts fall "roughly as one over the rank" | rank × count stays within 89,700–107,000 for ranks 50–5,000. The head deviates: rank 4 is 1.5× the 1/r value, and the curve shows this honestly | Recomputed |
| 6 | Zipf (1949) read the curve as a law of human behaviour, the principle of least effort | The book is *Human Behavior and the Principle of Least Effort* (Addison-Wesley, 1949). Ferrer-i-Cancho & Elvevåg (2010) say Zipf's law was "originally thought to reveal principles of language functioning" | Zipf 1949; PLoS ONE 2010 intro |
| 7 | "nearly fifty thousand different words" | 49,796 case-folded types (Kučera–Francis report 50,406 distinct forms) | Recomputed |
| 8 | 1/rank is a straight line of slope −1 on log–log axes | log f = log C − log r | Math |
| 9 | English least-squares slope over ranks 1–1000 = −0.98 | −0.9790 (log10–log10 OLS) | Recomputed |
| 10 | Monkey rules: space ends a word 1 press in 5 (after each letter), 26 letters equally likely | Simulation definition, labelled "simulated" on screen. Empty words are not allowed, following Li's (1992) version | make_data.py |
| 11 | Monkey slope over ranks 1–1000 = −1.07 | −1.0722 | Recomputed |
| 12 | "within a tenth of English" | 1.0722 − 0.9790 = 0.093 | Arithmetic |
| 13 | 26 one-letter words, all tied (~7,800 each) | Expected 1,013,319 × 0.2 / 26 = 7,795. Simulated range is 7,608–8,016 | Recomputed |
| 14 | 676 two-letter words | 26² = 676. Expected count each is N·0.8·0.2/676 = 240 (simulated 202–289) | Math, simulation |
| 15 | Each step is 26× wider | Step L covers ranks 26+…+26^(L−1)+1 … 26+…+26^L. Its width is 26^L, so each step is 26× wider than the last. The geometric midpoints of steps 2 and 3 sit at ranks 137.7 and 3,580, a ratio of 26.0 | Math |
| 16 | Each extra letter makes a word 32.5× rarer: (4/5)·(1/26) = 1/32.5 | P(a given word of length L) = 0.2·0.8^(L−1)/26^L. The ratio between consecutive L is 0.8/26 = 1/32.5 | Math |
| 17 | Slope = −log 32.5 / log 26 = −1.07 | ln 32.5 / ln 26 = 3.4812 / 3.2581 = 1.0685 | Math. Li 1992 derives the general form, −log(M/(1−q))/log M |
| 18 | rank ∝ 26^L and count ∝ 32.5^−L give count ∝ rank^−1.07 | Eliminate L: L = log r / log 26, so f ∝ 32.5^(−log r/log 26) = r^(−log 32.5/log 26) | Math |
| 19 | Miller (1957) made the random-typing argument | G. A. Miller, "Some effects of intermittent silence," *Am. J. Psychology* 70(2):311–314. Ferrer-i-Cancho & Elvevåg cite it (ref. 5) as showing that random character sequences reproduce Zipf's law | AJP 1957; PLoS ONE 2010 |
| 20 | Wentian Li worked out the slope (1992) | W. Li, "Random texts exhibit Zipf's-law-like word frequency distribution," *IEEE Trans. Inf. Theory* 38(6):1842–1845. The abstract says the exponent is close to 1 and comes from the length-to-rank transformation of an exponential | IEEE TIT 1992 |
| 21 | Ferrer-i-Cancho & Elvevåg (2010): random texts did not match real rank curves under statistical tests | *PLoS ONE* 5(3):e9411. Using three statistical tests, they found the rank distributions of random texts inconsistent with real texts, including for equiprobable characters. They point out the "pronounced staircase" in random texts | PLoS ONE 2010 (PMC2834740) |
| 22 | "the" is "nearly twice as common as of" | 69,971 / 36,412 = 1.92 | Recomputed |
| 23 | The monkey's top word is tied with 25 others | The top 26 simulated words are the 26 one-letter words, with counts of 7,608–8,016. In expectation they are exactly equal | Recomputed |

**What was cut.** The hapax share (44% of English types appear once) is true, but it would introduce a second idea. Miller's 1965 "monkeys" preface is also left out: the episode cites only the 1957 paper.

**Hedges kept in the narration.** The narration says "roughly" one over rank, "about half", "nearly twice", and "a test both can pass". The landing says only that this monkey (equiprobable letters) cannot produce a single winner at the top. It does not claim that every random model fails.
