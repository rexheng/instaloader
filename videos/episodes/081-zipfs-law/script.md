# Episode 81: Why "The" Is Twice as Common as "Of"

**One idea:** a straight Zipf line can't tell you what caused it, because a monkey typing at random draws one too. When the number of possible words grows exponentially with length and each word's probability shrinks exponentially with length, the result is a power law.

**Data:**
- English: the Brown Corpus (1,013,319 word tokens in NLTK's copy, lower-cased, punctuation dropped).
- Monkey: a numpy simulation (seed 7) of the same number of words. It uses 26 equally likely letters, and after each letter the space bar ends the word with probability 1/5. It is labelled "simulated" on screen.
- `make_data.py` builds `data.json`.

## Palette (colour -> one meaning)

| Colour | Meaning (whole episode) |
|---|---|
| BLUE | English word counts (Brown Corpus) |
| PURPLE | the monkey's word counts (simulated random typing) |
| RED | the wrong guess: a flat line, slope 0 |
| GREEN | ×26: each extra letter makes 26 times as many possible words (rank axis) |
| YELLOW | ÷32.5: each extra letter makes a word 32.5 times rarer, and the slope that produces |
| GRAY / DIM / INK | axes, the 1/rank reference, citations / context / text and neutral highlight boxes |

## Narration (beat by beat)

**Cold open (0:00–0:13)**
1. In a million words of American English, "the" appears seventy thousand times, and "of", the runner-up, about half as often. *(two blue bars grow: 69,971 and 36,412)*
2. Now a monkey hits random keys until it has typed a million words. Do its counts fall off like this, or stay flat? [pause 1.5] *(purple stream of random letters; two sketch options: "falls" / "flat")*

**Stakes (0:13–0:30)**

3. Further down the English list, the counts keep falling, roughly as one over the rank. *(four more bars and a grey 1/rank curve)*
4. In nineteen forty nine, George Zipf read this curve as a law of human behaviour, the principle of least effort. If random typing draws it too, the curve can't be his evidence. *(citation: Zipf, 1949)*

**Naive build (0:30–1:05)**

5. So here is the whole English list: nearly fifty thousand different words, ranked by count. Stretch both axes so each tick is ten times the last. *(bars collapse into dots on log-log axes, and the full blue curve draws)*
6. On these axes, one over rank is a straight line with slope minus one. English hugs it. Fit the top thousand words, and the slope comes out minus point nine eight. *(dashed grey slope −1 line, fitted band, live readout −0.98)*
7. Our monkey hits the space bar one press in five, and otherwise any of twenty six letters, all equally likely. No letter is favoured, so the natural guess is that no word is either: a flat line, slope zero. *(rules card; red flat dashed line)*

**Fail (1:05–1:25)**

8. Here is what it actually typed. Its counts fall too. Fit the same top thousand ranks, and the slope is minus one point oh seven. *(purple staircase draws; a purple fit line pivots from the red guess down to −1.07)*
9. The flat guess misses by the entire slope, and random noise lands within a tenth of English.

**Insight (1:25–2:20)**

10. Look closely at the monkey's curve. It's a staircase. The top step is the twenty six one-letter words, all tied. The next holds six hundred and seventy six two-letter words. *(braces under the steps)*
11. Each extra letter multiplies the possible words by twenty six, so each step is twenty six times wider. *(green ×26 leg)*
12. Each extra letter also makes any single word rarer. The monkey must skip the space bar, four times in five, and then hit the right letter, one time in twenty six. Together, thirty two and a half times rarer. *(4/5 × 1/26 = 1/32.5, yellow ÷32.5 leg)*
13. Twenty six times wider, thirty two and a half times lower, at every step. What slope does that make? [pause 1.5]
14. Minus log thirty two and a half, over log twenty six. Minus one point oh seven, the slope we measured. *(slope formula built from the two legs; flag −1.07)*
15. The number of possible words grows exponentially with length. Each word's count shrinks exponentially. Put together, they make a power law, with no mind required. *(rank ∝ 26^L, count ∝ 32.5^−L ⟹ count ∝ rank^−1.07; the dashed line extends through every step)*

**Payoff (2:20–2:55)**

16. George Miller made this point with random typing in nineteen fifty seven. Wentian Li worked out the slope in nineteen ninety two. *(citations)*
17. The staircase is also where the monkey gives itself away. In twenty ten, Ferrer-i-Cancho and Elvevåg tested random texts statistically, and they did not match the rank curves of real ones. *(box around the 26-way tie vs English's smooth head; citation)*
18. A straight line on log axes is a test that both can pass.

**Landing (2:55–3:15)**

19. So, back to the top of the list. The monkey's most common word is tied with twenty five others. English has one word alone at the top, "the", nearly twice as common as "of". Chance drew the straight line for free. It did not draw that. *(the/of bars return beside 26 tiny tied purple bars at the same scale)*

## Sources
- Kučera, H. & Francis, W. N. (1967). *Computational Analysis of Present-Day American English*. Brown University Press. (Brown Corpus counts; recomputed from NLTK's copy.)
- Zipf, G. K. (1949). *Human Behavior and the Principle of Least Effort*. Addison-Wesley.
- Miller, G. A. (1957). Some effects of intermittent silence. *American Journal of Psychology* 70(2), 311–314.
- Li, W. (1992). Random texts exhibit Zipf's-law-like word frequency distribution. *IEEE Transactions on Information Theory* 38(6), 1842–1845.
- Ferrer-i-Cancho, R. & Elvevåg, B. (2010). Random texts do not exhibit the real Zipf's law-like rank distribution. *PLoS ONE* 5(3), e9411.
