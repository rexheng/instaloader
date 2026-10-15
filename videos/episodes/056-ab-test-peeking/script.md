# 056 — Why Checking Your A/B Test Early Breaks It

**One idea:** a p < 0.05 cutoff spends a 5 % false-positive budget once; checking every day and
stopping at the first "significant" result spends it twenty times, so identical buttons "win"
about a quarter of the time. Sequential boundaries spend the same 5 % deliberately across the looks.

## Palette (colour -> one meaning, whole episode)

| Colour | Meaning |
|---|---|
| BLUE | a simulated test's z-statistic path (data with no real difference) |
| RED | a false winner: a test that crossed a line and was stopped (always with a dot marker or a label) |
| YELLOW | the naive rule and its promise: the ±1.96 lines and the 5 % budget |
| GREEN | the corrected rule: the O'Brien–Fleming funnel and what it delivers (always labelled) |
| INK / GRAY / DIM | text / axes and secondary labels / context and paths after stopping |

## Narration (beat by beat)

| # | Beat | Narration | On screen |
|---|---|---|---|
| 1 | Cold open | These two sign-up buttons are identical. Same color, same words, and the same true click rate, ten percent. | Buttons A and B, "true click rate 10 %" under each, "=" between |
| 2 | Cold open | You run an A B test on them anyway. Every day for twenty days you check the p-value, and you stop the first time it drops below point oh five. | 20 look-dots light up; rule `p < 0.05 ⇒ stop` (yellow) |
| 3 | Prediction | How often does one of two identical buttons get declared the winner? [pause 1.5] | `P(a winner) = ?` |
| 4 | Stakes | Point oh five comes with a promise. When the buttons truly match, you get fooled in one test out of twenty, five percent. | `promised 5%` (yellow) |
| 5 | Naive build | That p-value comes from one number, z. It's the gap between the two click rates, divided by the noise you'd expect in that gap. | Buttons shrink to header; z formula built from the buttons; chart axes from the look-dots |
| 6 | | P below point oh five means z has escaped these two lines, at plus and minus one point nine six. | Yellow ±1.96 lines |
| 7 | | Here is one simulated test, with five hundred visitors per button each day. Day one, day two, still inside. | Blue path grows day by day |
| 8 | | On day seven, z pokes above the line. P is point oh four. You stop, and ship button B. | Red dot at day 7, `p = 0.04`, "stop: B wins" |
| 9 | | Had you kept going, this same test would have drifted back and finished day twenty inside the lines. No winner. | Dim continuation to day 20 (z = 0.70) |
| 10 | Fail | Now run a thousand of these tests, every one between identical buttons, and stop each one at its first crossing. | 1,000 simulated paths sweep; winners turn red; live counter |
| 11 | | Two hundred and forty nine of them crown a winner. That's twenty five percent, five times the promise. | Counter 24.9 % next to promised 5 % |
| 12 | | Check only once, on day twenty, and just fifty two land outside the lines. | Day-20 column: 52 dots, `one look 5.2%` |
| 13 | Cause | No single p-value lied. But every check is another chance to touch a line, and one touch is enough. | Red crossing dots flagged |
| 14 | Insight | Sort the winners by the day they first crossed. | Red dots fly into a stacked bar, one slice per day |
| 15 | | Day one takes about five percent. Day two adds three more. Later days add less and less, because day eleven's z is built mostly from day ten's visitors. | α₁, α₂ labels; slices shrink upward |
| 16 | | Stacked up, alpha one plus alpha two, all the way to alpha twenty, comes to twenty five percent. | `α₁ + α₂ + ⋯ + α₂₀ = 24.9%` built from the slices |
| 17 | Prediction | The promise allows five percent in total. How would you spend it across twenty looks? [pause 1.5] | Yellow 5 % budget line across the bar |
| 18 | | Spend almost nothing early. Make the lines very wide on the first days, and narrow them toward the end. This funnel is the O'Brien Fleming boundary, from clinical trials. | Yellow lines morph into green funnel; citation O'Brien & Fleming 1979 |
| 19 | | Run the same thousand tests again. Forty nine winners. Five percent, with twenty looks. | Re-sweep; second stacked bar grows to 4.9 %; formula `= 4.9%` |
| 20 | Price | The price is small. On day twenty, z must pass two point one three instead of one point nine six. | `2.13` vs `1.96` at day 20 |
| 21 | Payoff | Medical statisticians mapped this trap decades before A B tests. In nineteen sixty nine, Armitage, McPherson and Rowe calculated how fast it grows: five looks give fourteen percent, twenty give twenty five, a hundred give thirty seven. | Bar chart: looks → false-positive rate; citation |
| 22 | | In twenty seventeen, Johari and colleagues, working with the testing company Optimizely, built p-values that stay valid however often you look. | Green ≤ 5 % line across all look counts; citation |
| 23 | Landing | Looking is harmless. Stopping because of what you saw is what spends the budget. | Buttons return; 20 look-dots |
| 24 | | These two buttons never differed. They just got twenty chances to look like they did. | Day-7 dot red, "B wins" tag; end card |

## Sources
- Armitage, P., McPherson, C. K., Rowe, B. C. (1969). Repeated significance tests on accumulating data. *J. Royal Statistical Society A* 132(2):235–244. doi:10.2307/2343787
- O'Brien, P. C., Fleming, T. R. (1979). A multiple testing procedure for clinical trials. *Biometrics* 35(3):549–556. doi:10.2307/2530245
- Johari, R., Koomen, P., Pekelis, L., Walsh, D. (2017). Peeking at A/B tests: why it matters, and what to do about it. *KDD '17*, 1517–1525. doi:10.1145/3097983.3097992
- All test paths: simulated (make_data.py, seed 47), labelled "simulated" on screen.
