# 048 — Storks Deliver Babies (p = 0.008)

**One idea:** a significant correlation can be produced entirely by a common cause; a causal diagram (DAG) tells you which variable to adjust for — block every back-door path.

## Palette (colour → one meaning, whole episode)
- **BLUE** — stork pairs (the suspected cause): x-axis, "storks" node and term, run of the slope triangle
- **PURPLE** — births (the outcome): y-axis, "births" node and term, rise of the slope triangle
- **YELLOW** — land area (the confounder): dot size/outline, "land area" node and term, its arrows
- **RED** — the spurious association: the naive line, the back-door path, the naive b and p
- INK — text, the adjusted line; GRAY — axes, country names, citations; DIM — dimmed context

## Beats (narration as spoken)

**0 · Cold open (0:00)** — Real scatter, red line, r and p.
Seventeen European countries, one dot each. Across, pairs of breeding storks. Up, babies born per year. The line climbs. The correlation, r, is point six two, and p is point oh oh eight. Is this a fluke? Commit to an answer. [pause 1.5]

**1 · Stakes** — dots flash; citation.
It's not a fluke. These are real counts, published in two thousand by Robert Matthews in the journal Teaching Statistics. His point: suspected links, like diet and cancer, often get their first test exactly this way.

**2 · Naive build** — slope triangle on the line, fraction built from its legs.
So take the line at its word. Ten thousand more stork pairs, and births rise by two hundred and eighty-eight thousand. That's twenty-nine babies per stork pair, per year. And if storks and births were unrelated, a correlation this strong would turn up only about once in a hundred and twenty-five tries.

**3 · The test** — dots grow to land area.
A causal claim should survive one test: compare countries of the same size. So let each dot's area show its country's land area.

**4 · Fail, cause named** — biggest dots labelled; two correlations.
The biggest dots ride high: Turkey, Germany, France. The small ones huddle near zero. Land area alone tracks births with a correlation of point nine two. It tracks storks too, at point five eight. Size is doing the work.

**5 · DAG** — scatter moves left; nodes come from the axis titles.
Draw that as arrows. Area points to births: more land, more people. Area points to storks: more land, more nests. The claim on trial is this dashed arrow, from storks to births.

**6 · Back door** — red path lights storks ← area → births.
Even if that arrow were missing, a path would still connect them: from storks, back through area, to births. That's a back door. It carries correlation, but no causation.

**7 · Formula from the picture** — each arrow into births becomes a term.
Every arrow into births becomes a term. Births equals a, plus b times storks, plus c times area. The number on trial is b.

**8 · Close the door, one country** — box on area; Turkey's two arrows.
To estimate b, close the back door: hold area fixed by subtracting what each country's size alone predicts. For Turkey, that's eighteen thousand stork pairs and one point three million births. Take them away, and Turkey slides down here.

**9 · Prediction pause**
Now the other sixteen. Will the line stay steep? [pause 1.5]

**10 · Result** — all dots slide; live slope 29 → 6; p 0.008 → 0.31.
It nearly flattens. b falls from twenty-nine babies per pair to six, and p climbs to point three one. With seventeen countries, six is indistinguishable from zero.

**11 · Payoff** — Pearl citation.
That's Judea Pearl's back-door rule: draw the diagram, then adjust for whatever blocks every back-door path.

**12 · Honest limit** — collider node.
But the diagram is an assumption, and no regression can draw it for you. Adjusting for everything isn't safe either: box a variable that two arrows point into, and you open a path instead of closing one.

**13 · Landing** — dots slide back to the opening plot; area arrows flagged.
So look at the opening plot again. The p-value was right: something real links storks and babies. It just has an arrow pointing at both.

## Sources (on screen)
- Matthews, 2000 · Teaching Statistics 22(2) — data, r, p, land-area suggestion
- Pearl, 2000 · Causality (Cambridge University Press) — back-door criterion
