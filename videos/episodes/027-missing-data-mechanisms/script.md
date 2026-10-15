# Episode 27 — When Missing Data Isn't Missing at Random

**Idea in one sentence:** Deleting or filling in blanks is only safe when the chance of a blank depends on
things you can see; when it depends on the missing value itself, the remaining data look fine and still lie.

## Palette (one hue, one meaning)

| Colour | Meaning |
|---|---|
| BLUE | an income that was answered (dots, the average of the answers, "income" in the formula) |
| PURPLE | a blank: people who skipped, the eraser's fog, the "blank" term, real nonresponse bars |
| GREEN | a filled-in value (imputed dots, the filled average) |
| RED | error: the gap between an estimate and the truth |
| YELLOW | the age slice, conditioning on age ("age" in the formula) |
| INK (dashed) | the truth (true average, true line) |
| GRAY | axes, labels, citations |

## Beats (target ~3:15, ~480 words)

**1. Cold open (0:00)** — scatter of 300 simulated people (age × income) on screen from frame 1.
> Three hundred people answer a survey about age and income. Ninety of them leave the income blank, so for them we know the age, but not the income.

90 dots turn purple and drop to a rug on the age axis.

> Drop the blanks and average the two hundred and ten answers. Is that too high, too low, or about right? [pause 1.5]

Blue average line + readout $33,590. Prediction hold.

**2. Reveal** — dashed truth line, red gap bracket, error readout.
> This survey is simulated, so we know the truth: thirty-nine thousand, two hundred and fifty. Deleting the blanks came in about fifty-seven hundred dollars low, and nothing in the remaining dots looks wrong.

**3. Stakes** — 10×10 waffle, 43 purple squares. Citation Bollinger et al., 2019.
> America's official income and poverty numbers come from a survey where, by twenty sixteen, forty-three percent of earnings went unreported.

**4. Naive build: three erasers**
> Whether deletion is safe depends on who skipped. So let's restore all ninety, and try three erasers.

Ticks rise back to true positions. Error resets.

> Eraser one flips a coin for each person, so its fog is even everywhere. The average of the rest misses by under five hundred dollars. Deletion works.

**5. Fail**
> Eraser two takes the young. Its fog is thick on the left and thin on the right. Now deletion comes in high, by about forty-six hundred dollars, because the survivors are too old, and older people here earn more.

**6. Insight**
> But look inside one slice of age. Here the fog is even, so within this slice, the eraser picked at random. Survivors in every slice are a fair sample, and a line through them lands on the true line.

> Fill each blank from that line, plus the usual scatter, and the error drops under two hundred dollars.

> In symbols, the chance of a blank, given age and income, equals the chance given age alone. Donald Rubin named this missing at random, in nineteen seventy six.

**7. Prediction 2**
> Eraser three takes high earners. Its fog thickens toward the top. This is the survey we started with. Will the same fix rescue it? [pause 1.5]

**8. Measured failure of the fix**
> Only halfway. Deletion was fifty-seven hundred low, and filling from the line still leaves twenty-eight hundred. Inside each slice, the top is erased, so the survivors' line sinks, and every fill lands on the sunken line.

> The chance of a blank now depends on income, the very number that is missing.

**9. Honest limit**
> And the remaining dots can't warn you. Molenberghs and colleagues proved that every not-at-random model has an at-random twin that fits the observed data just as well. Only outside information can tell them apart.

Two sets of fills toggle while the 210 answers stay frozen.

**10. Payoff** — real bars, Table 3 col. 1, men. Citation Bollinger et al., 2019 · JPE.
> Bollinger and colleagues had that outside information: Social Security earnings records, linked to the survey. Among men, more than a quarter of the bottom tenth left earnings unreported, under a fifth through the middle, and nearly a third of the top one percent. In the real survey, the eraser works both ends.

**11. Landing** — back to the opening frame; the 90 blanks rise to their true places, mostly top right.
> Back to our first survey. The two hundred and ten answers were never wrong. The bias was in why the other ninety left.

End card.

## Sources
- Rubin, D. B. (1976). Inference and missing data. *Biometrika* 63(3):581–592.
- Molenberghs, Beunckens, Sotto & Kenward (2008). *JRSS B* 70(2):371–388.
- Bollinger, Hirsch, Hokayem & Ziliak (2019). *Journal of Political Economy* 127(5):2143–2185.
- Simulation: `data.py` (see facts.md).
