# 093 · The Strange Bump at 20 Friends

**Idea (one sentence):** Patterns in platform data are co-written by the platform's code, and a friend-of-a-friend recommender writes directly into the numerator of clustering, so even a "law" like triangle closing can be partly manufactured (algorithmic confounding).

## Palette (colour -> one meaning)

| Colour | Meaning |
|---|---|
| BLUE | people, and friendships people make on their own |
| YELLOW | the platform's hand: the nudge to 20, the 5,000 cap, suggested friendships, the code's share |
| INK | text, numbers, the data box |
| GRAY / DIM | axes, existing friendships, possible-but-absent pairs, citations |

## Beats

**0 · Cold open (0:00)** — log-log friend-count curve (schematic) draws itself; gray ring around the kink.
> These are the friend counts of seven hundred and twenty one million Facebook users, in May twenty eleven. The curve falls smoothly, except for one small kink, near twenty friends. Is that kink about people, or about the website? [pause 1.5]

**1 · Reveal** — the kink flattens, then yellow arrows shove mass from below 20 into the bump; ring turns yellow; the 5,000 wall drops in yellow. Citation: Ugander et al. 2011.
> Facebook's own researchers explained it. The product pushed people with few friends to keep adding them, until they reached twenty. And the curve stops dead at five thousand, because Facebook capped friend lists there.

**2 · Stakes** — kink and wall flag; curve slides out.
> So the most basic statistic of the largest social network anyone had analyzed carries the platform's fingerprints. A kink is easy to spot. The dangerous case is a pattern that looks like a law of human behaviour.

**3 · Naive build: measure clustering** — one person, five friends; ten dashed pairs; two solid. Fraction built from the lines.
> Here is one person with five friends. Five friends make ten possible pairs, and two of those pairs are friends themselves. Two out of ten is this person's clustering.

**4 · General + real number** — denominator becomes k(k-1)/2; Facebook value appears. Citation.
> With k friends, the bottom is k times k minus one, over two. On Facebook, people with a hundred friends score point one four, about five times an instant messaging network studied in two thousand eight.

**5 · The naive reading** — a third friend-pair closes in blue; reading label.
> The textbook reading is that people close triangles: your friends meet, and become friends. So let's build people who never do that, and measure.

**6 · Setup + prediction** — two copies of 48 simulated people.
> Here are forty eight simulated people with sixty random friendships, copied twice. Each person adds one new friend. On the left, a stranger picked at random. On the right, a suggestion: a friend of a friend. Nobody on either side cares about triangles. Both start at point oh four. Where does each side end up? [pause 1.5]

**7 · Run + measured failure** — edges appear; live C counters.
> Random strangers reach point oh nine. The suggestions reach point four eight, more than five times as high. A theory of human triangle closing would fit the right side well, and the suggestion rule made every one of those triangles.

**8 · Insight** — back to the ego; one dashed pair turns yellow; numerator 2 -> 3, C 0.2 -> 0.3.
> The reason is in the fraction. A friend of a friend suggestion exists because of a shared friend, like this one. When it's accepted, her k stays the same, and the top goes up by one. The algorithm writes straight into the numerator.

**9 · Payoff** — data-generating diagram: people -> data <- platform; loop from theory. Citation Salganik 2018.
> Matthew Salganik calls this algorithmic confounding: the platform is part of the process that makes the data. Facebook does suggest friends of friends, through People You May Know. So when Facebook data confirm that triangles close, part of that confirmation was built into the system.

**10 · Honest limit** — the 0.14 bar with an unknown split point sliding; the yellow arrow switches off.
> From the traces alone, nobody can split point one four into people and code. To split it, you have to break the loop: switch the suggestions off for a random group, and see what's left.

**11 · Landing** — the cold-open curve returns with "people" (blue) and "code" (yellow) labels.
> The kink at twenty is the rare case where the code left a visible mark. Triangles leave none. Every curve from a platform has two authors: the people, and the code.

## Sources
- Ugander, Karrer, Backstrom & Marlow (2011), *The Anatomy of the Facebook Social Graph*, arXiv:1111.4503.
- Leskovec & Horvitz (2008), *Planetary-scale views on a large instant-messaging network*, WWW 2008.
- Salganik (2018), *Bit by Bit: Social Research in the Digital Age*, Princeton University Press, §2.3.
- Simulation: sim.py in this directory (see facts.md).
