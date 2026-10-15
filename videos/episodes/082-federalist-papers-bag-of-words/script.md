# 082 · The Boring Words That Unmasked an Author

**One idea:** a writer's habit shows up in how often they use dull function words, and asking
"how likely is this exact count under each writer" (Poisson likelihood ratio, multiplied
across words) turns those counts into odds of authorship.

Target runtime ~3:15 at ~150 wpm. All plotted data is real: my own word counts from the
Project Gutenberg text of *The Federalist* (`data_prep.py` -> `data.json`), labelled on screen
"counts: Project Gutenberg text".

## Palette (colour -> one meaning, whole episode)

| Colour | Meaning |
|---|---|
| RED | Hamilton: his name, his essays (dots), his expected counts (bars) |
| BLUE | Madison: his name, his essays, his expected counts, and evidence (odds) for Madison |
| INK (white) | the twelve disputed essays (author unknown) |
| YELLOW | focus: the word being counted, the dividing line, the changing term, the error counter |
| GRAY / DIM | axes, ticks, citations / dimmed context |

Red and blue are never the only cue: every row and bar set carries a name label.

## Beats

**1 · Cold open (0:00-0:12)** - twelve numbered essay cards; "Hamilton" red at left,
"Madison" blue at right; three word chips appear.
> Twelve of the Federalist Papers are disputed between Alexander Hamilton and James Madison.
> You may count one word to settle it. War, liberty, or upon. Pick one. [pause 1.5]

**2 · Stakes** - card 51 lifts; its line appears under it; a red line from "Hamilton 1804"
and a blue line from "Madison 1818" both point at it. Citation Adair 1944.
> Essay fifty-one is one of them: if men were angels, no government would be necessary.
> Hamilton's list, made public after his death in eighteen oh four, claimed it. Madison's
> list, in eighteen eighteen, claimed it too.

**3 · Naive build: bag of words** - the quote's words shuffle into a heap; rate = count /
words x 1000 is written from the heap.
> Start the obvious way. Shred each essay into a bag of words: forget the order, keep the
> counts, and divide by the length.

**4** - strip plot: 51 red dots (Hamilton row), 14 blue dots (Madison row), x = uses of the
word per 1,000 words. Header chip: "war".
> Sixty-five other essays have known authors: fifty-one by Hamilton, fourteen by Madison.
> Each dot is one essay, placed by how often it says war.

**5 · Fail, measured** - yellow dividing line slides; live counter "wrong: n of 65".
> Now slide a line to split them. Its best spot is the far edge, calling every essay
> Hamilton's, and that still gets fourteen wrong.

**6 · Cause named** - dots move to "liberty" rates; counter stays at 14. Essay 8's dot
flagged on the war strip (11 uses).
> Liberty does no better. Both words follow the topic. Essay eight, on hostilities between
> the states, says war eleven times. The essays on the courts say it once at most.

**7 · Iterate: upon** - dots glide to "upon" rates; line settles at 0.85; counter 14 -> 1.
> Now count upon. Every one of Hamilton's fifty-one essays uses it. Eleven of Madison's
> fourteen never do. The same line now makes one mistake. Upon carries no topic, so it
> follows the writer.

**8 · Second failure** - the twelve disputed cards drop as white dots: ten at zero, two
(50 and 54) right of the line.
> Drop in the twelve disputed essays. Ten land at zero. But fifty and fifty-four, with one
> and two uses, fall on Hamilton's side of the line.

**9 · Insight: likelihood, not sides** - dot 54 moves to a new chart; lambda = rate x length
built from the rates.
> A line only asks which side. Ask instead how likely this exact count is for each writer.
> Fifty-four runs about two thousand words. At Hamilton's rate, three point three per
> thousand, he'd average about six and a half uses. Madison would average about a third of one.

**10 · The picture + prediction pause** - Poisson bars for both writers, counts 0-12;
yellow marker at 2.
> Counts of a rare word follow a Poisson distribution, set by that average. Here are both
> writers' chances for every count, and here is two. Which writer does two favour? [pause 1.5]

**11 · Formula from the picture** - the two bars at 2 are lifted out, enlarged by the same
factor; ratio built from them: 0.045 / 0.028 ~ 1.6.
> Madison, barely. Two is high for him but low for Hamilton. The bars stand at four point
> five percent and two point eight percent. Their ratio, one point six to one, is the
> evidence, and here it is weak.

**12 · Multiply = add on a log scale** - essay 54's odds bar grows word by word on a
log axis (upon, by, on, to, there).
> So ask more words. By, on, to and there each give a ratio. If words are independent, the
> ratios multiply, so on a log scale their lengths add. For essay fifty-four, the product
> passes twenty million to one.

**13 · All twelve** - twelve bars, all on Madison's side; 55 short. Leave-one-out check.
> Do it for every essay. Tested on the sixty-five known essays, each held out in turn, it
> makes one mistake. All twelve disputed essays point to Madison, though fifty-five barely leans.

**14 · Payoff (real)** - citation Mosteller & Wallace, 1963 · JASA; markers "80 : 1" (55) and
"800 : 1" (56).
> Frederick Mosteller and David Wallace did this carefully in nineteen sixty-three: thirty
> words, and a model that lets words clump, which shrinks the odds. They gave all twelve to
> Madison. Their weakest case was also fifty-five, at about eighty to one. Next came
> fifty-six, at eight hundred.

**15 · Honest limit**
> Historians, led by Douglass Adair in nineteen forty-four, already leaned toward Madison.
> The counts added evidence that ignores meaning completely, which is why it hears habit
> and not argument.

**16 · Landing** - back to the twelve cards and the three chips; "upon" chip lights; under
card 51: "upon: 0".
> In fifty-one essays, Hamilton never once went without upon. The essay about angels never
> uses it at all.

## Sources
See facts.md. Mosteller & Wallace (1963) JASA 58(302):275-309; Mosteller & Wallace (1964)
*Inference and Disputed Authorship: The Federalist*; Adair (1944) WMQ 1(2):97-122;
Project Gutenberg eBook #18 (The Federalist Papers).
