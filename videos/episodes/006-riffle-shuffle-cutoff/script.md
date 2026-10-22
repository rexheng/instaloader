# Episode 6 — Seven Shuffles: When a Deck Suddenly Becomes Random

**Idea (one sentence):** A riffled deck's chance depends only on its count of rising sequences;
each riffle roughly halves the gap between that count and a random deck's while the random
deck's spread stays fixed, so the deck stays almost perfectly detectable for four riffles and
then falls off a cliff around seven, even though the top card already looks random after four.

Runtime ≈ 3:38 · ≈ 545 words · voice af_heart, speed 0.84.

## Palette (one meaning each, whole episode)

| Colour | Meaning |
|---|---|
| card ramp (slate → ink) | a card's number, 1 to 52 (the deck itself; neutral, not a hue). In card view bar height is also the card number; in level view bar height is the card's rising-sequence index |
| PURPLE | the riffled deck: its tag, its chance, its token and stack, its top-card histogram, its rising-sequence histogram, "say riffled", the step counter, P (0.65) |
| BLUE | the perfect shuffle: its tag, its chance, its token and stack, the 1-in-52 line, the bell, the spread bracket and its hops, "say perfect", U (0.32), "2.1", √((n+1)/12) |
| YELLOW | rising sequences: the caps/levels on the deck, the counts, the riffle-2 packet tint, the gap between centres (and its 4-riffle ghost), the gap × 2^k row, 230, n(n+1)/12 |
| RED | what gives the deck away: purple-above-blue area (= distance d), the meter's edge over a coin flip, the distance curve, "whole deck" |
| INK / greys | text, axes, ticks, citations; the "top card only" curve (grey dashed); text grey is #A3AAB4 (7.7:1), GRAY #8B939E only for axes and lines |

## Data and model
- Gilbert–Shannon–Reeds (GSR) riffle model (Bayer & Diaconis 1992, p. 294).
- Every number is exact (rational arithmetic) from `sim.py` → `data.json`; example decks from
  `deck_pick.py` (seed 68, plus a second 4-riffle deck with 14 sequences, seed 10001) →
  `decks.json`; the 40 + 40 decks that rain into the stacks from `pile.py` (seed 253) → `pile.json`.
  The example decks are labelled "one simulated deck", the stacks "40 simulated decks each".
- See `facts.md` for each claim and its source.

## Beats

### 1. Cold open (0:00–0:15, commit at 0:10–0:13)
> Heads, I riffle shuffle a sorted deck four times. Tails, a computer shuffles it perfectly.
> From the deck alone, how often could you tell which? Pick fifty, seventy five, or a hundred
> percent. *[pause 1.5]*

Visual: first frame is TWO sorted decks side by side (52 bars each, height and shade = card
number), centred vertically, "1"/"52" over the left deck's end cards, "top"/"bottom" under it.
Purple tag *heads: 4 riffles*; the left deck riffles four times. Blue tag *tails: perfect
shuffle*; the right deck jumps into a uniformly random order on "shuffles it perfectly". On "how
often" both decks rise 0.8 as the accuracy meter draws below them (coin flip 50 % → always right
100 %); a "?" hops 50 → 75 → 100 % as each option is spoken, then a 1.5 s hold.

### 2. Stakes (0:15–0:23)
> Monte Carlo samplers move by random steps, like these riffles. Stop them too early, and they
> still remember where they started.

Visual: on "random steps" the left deck re-sorts and replays its four riffles fast under a purple
counter "step 1 … step 4"; "step 4" flags on "Stop them too early"; on "remember where they started"
the sorted deck's profile (grey dashed diagonal) is drawn over it.

### 3. Naive build: the top card (0:23–0:43)
> The obvious check is the top card, the one you'd be dealt. Here's how often each card ends up
> there after four riffles.

> Almost flat. Only the old top card stands out: one time in fifteen. Judging by the top card,
> you'd be right fifty two percent of the time. Four riffles look like plenty.

Visual: as before (top card boxed; its copy flies into its bar of the purple histogram; blue
dashed "perfect: 1 in 52"; card 1's excess red, "1 in 15"; meter fills red to 52.4 %).

### 4. Fail: rising sequences (0:43–1:31)
> A guesser who sees the whole deck does far better. The model cuts near the middle, then drops
> cards from each half in proportion to its size.

> Each half stays in order, so one riffle leaves two rising sequences: runs of consecutive cards,
> reading left to right.

> Give each sequence its own level. The cut crosses each level once, so a riffle can at most
> split it in two.

> Three riffles, *[pause 0.8]* eight. Four riffles, *[pause 0.6]* at most sixteen; this deck has
> fourteen.

> A perfect shuffle averages twenty six and a half, and gives sixteen or fewer once in two million
> decks.

> Call sixteen or fewer riffled, and you'd be wrong about once in four million games. The top card
> can't see this; it lives in the order between cards.

Visual: the top-card chart fades before the deck moves; grey "top card 52.4%" ghost (one font
size) under the meter track. Slow riffle with the two-line citation *Gilbert–Shannon–Reeds model
· Gilbert, 1955 · Bell Labs; Reeds, 1981*. Yellow traces join the two sequences, "1, 2, 3, …, 26"
/ "27, 28, …, 52", a dot reads sequence 1. **Level view:** as the bars drop to their sequence's
level, their old tops stay behind for ~1 s as faint ticks and a grey "height = which sequence"
label appears (it leaves on riffle 3). Cut line, rings, right packet tinted; riffle 2 splits the
two levels into four (exact: L1-left, L1-right, L2-left, L2-right), ceiling "≤ 2² = 4"; riffle 3:
8; riffle 4: 14 under "≤ 2⁴ = 16". Counters and ceiling labels change by a short slide (old up and
out, new up and in), never a glyph morph; the faint shelf lines hide while cards fly. Tag "one
simulated deck". Side by side: the perfect deck returns with 26 levels (its shelves at 15 %, caps
kept), "average 26.5" (leaves once spoken, as the 16-line crosses), "≤ 16: 1 in 2.1 million"; the
citation and the top-card ghost dim to 25 % during this beat. On "wrong about once in four
million" the needle jumps to 99.99998 %; on "The top card can't see this" the top card is boxed
and the ghost returns to full; caps flash on "order between cards".

### 5. Insight (1:31–2:50)
> Bayer and Diaconis proved that in this model, decks with the same count are equally likely.
> *[pause 0.7]*

> So pile decks onto their counts, *[pause 0.6]* then every possible deck, weighted by its chance.

> The red area, purple above blue, is the distance from random. Right now it's one.

> How many more riffles to bring it below a half? *[pause 1.5]*

> A fifth riffle: point nine two. A sixth: point six one. A seventh: point three three.

> Guess riffled where purple is higher: you catch sixty five percent of riffled decks, and flag
> thirty two percent of perfect ones. Accuracy is a half, plus half the difference, and the
> difference is the red area.

> Each riffle roughly halved the gap, but blue's spread, its standard deviation, stays about two.
> While the gap spans several spreads, the distance stays near one. Within about one spread, it
> halves every riffle: that's the cliff.

> Multiply each gap by two to the k, and it settles near two hundred thirty. *[pause 1.2]*
> Divide that by two each riffle, and it reaches one spread after just under seven.

> For n cards, two hundred thirty grows like n squared, but the spread only like root n, so the
> cliff sits near three halves log base two of n.

Visual: meter leaves, then *Bayer & Diaconis, 1992 · Ann. Appl. Probab.* fades in. "chance 3.5 ×
10⁻⁶⁰" / "chance 1.2 × 10⁻⁶⁸"; on "equally likely" the riffled deck rearranges into another
14-sequence deck, "same chance"; in the pause each deck's 52 bars squeeze into one token.
**Pile:** the axes ("rising sequences" × "share of decks") draw; the two tokens drop onto 14 and
26; 39 more tokens of each colour rain into stacks ("40 simulated decks each", one token = 1/40);
on "every possible deck, weighted by its chance" the label leaves and the stacks become the exact bars (blue bars + outline, purple
outline); "4 riffles" rides above the purple histogram on the row above the axis title.
Red fills purple-above-blue on "red area"; the d-inset draws on "distance"; "d = 1.00" at 4.
Prediction: d = ½ line, "0.5" flags, 1.5 s hold, during which the yellow gap bracket (legs on the
two centres) draws and its bar flies up into "gap: 12.4". **Contiguous answer:** a 30 % ghost of
the 4-riffle bracket stays; purple slides to 5, 6, 7 riffles (the tag names the target, d hidden
mid-slide), each whole count adds its dot, "d = …" and the row value (the bracket's bar flies up
into "→ 6.89", "→ 3.55", "→ 1.79"); the ½ line flags when 0.33 lands below it.
**Accuracy at 7:** zones "say riffled" (r ≤ 25) / "say perfect"; the purple area in the zone flies
into 0.65, the blue area in the zone into 0.32: `accuracy = ½(0.65) + ½(1 − 0.32)`; copies slide
into `= ½ + ½(0.65 − 0.32)`; (0.65 − 0.32) flashes red on "the difference is", and on "red area"
the rest of line 1 leaves, then the difference shrinks into a red `d` while the two lines close
up into `accuracy = ½ + ½ d` under a fixed "accuracy =" (red area flashes), held ≥ 3.5 s; it
leaves when the spread bracket draws. **Mechanism, no rewind:** row flashes + "(each step ≈ ÷2)"; blue
"spread 2.1" bracket on the bell (centre to one sd); on "several spreads" the 4-riffle ghost
brightens and spread-long hops are laid along it, "5.9 spreads", dots 1–4 at d = 1; on "Within
about one spread" one hop on the 7-riffle gap, "0.85 spreads"; dots 6, 7 flash and dot 8 appears; the cliff
is drawn through the dots. **One equation line:** "× 2^k ≈ 198 → 220 → 227 → 229 → 230" from the
gap row; `gap ≈ 230/2^k` built from the bracket and the 230 (held ~3 s); on "one spread" the word
"gap" is replaced by the blue 2.1 flown from the spread label: `2.1 ≈ 230/2^k`; `⇒ k ≈ 6.8` and a
dashed line at 6.77 on the d-plot. For n: the chart dims; 230 → `n(n+1)/12` ("∼ n²" above it),
2.1 → `√((n+1)/12)` ("∼ √n"), `k ≈ 6.8` → `k ≈ (3/2) log₂ n − 1.8`, grey "(gap = spread rule)".

### 6. Payoff (2:50–3:17)
> Aldous proved that law. Bayer and Diaconis computed the exact curve: for fifty two cards, seven
> riffles is the first count below a half.

> Trefethen and Trefethen measured information instead: no cliff, and five or six shuffles do a
> reasonable job.

> Many Markov chains share this cliff, and samplers share the trap: one statistic can settle, like
> the top card, long before the whole chain has.

Visual: the d-plot grows into the full distance curve (Table 1 values), the equations stay top
right at 45 %. *Aldous, 1983 · Séminaire de Probabilités XVII* while `k ≈ (3/2) log₂ n − 1.8`
flashes; on "Bayer" it is replaced (fade out, then fade in — never crossfaded) by *Bayer &
Diaconis, 1992 · Ann. Appl. Probab.*; dots 9–10 on "exact curve"; values 0.92/0.61/0.33/0.17; the
k = 7 dot and the ½ line flag. Then *Trefethen & Trefethen, 2000 · Proc. R. Soc. A*, grey note
"information yardstick: no cliff, 5–6 riffles" and a grey band over 5–6. Then *Diaconis, 1996 ·
PNAS*, the cliff flashes, and the grey dashed "top card only (computed)" curve drops early beside
the red "whole deck".

### 7. Landing (3:17–3:38)
> Back to the coin flip. After four riffles you'd almost never be wrong, same as with an
> unshuffled deck.

> Three more riffles, *[pause 1.2]* and you'd be right only two times out of three.

> Four riffles fool someone watching the top card. Fooling someone who counts sequences that well
> takes ten.

Visual: the opening deck returns in level view (caps only, 14 levels, "one simulated deck"),
meter at 99.99998 % with the grey "top card 52.4%" ghost. Each riffle: cut, then the cards drop
straight onto the new levels while the counters tick by a slide and the needle steps to ½(1 + d):
96.2 → 80.7 → 66.7 %; the ghost flags on "top card"; riffles 8–10: 58.4 → 54.3 → 52.1 %, landing
beside the ghost before "takes ten"; ghost flashes on "ten"; the scene fades, then the end card.

## Sources
- Bayer, D. & Diaconis, P. (1992). Trailing the dovetail shuffle to its lair. *Annals of Applied
  Probability* 2(2), 294–313. doi:10.1214/aoap/1177005705 (Theorem 1, Table 1, §2).
- Aldous, D. (1983). Random walks on finite groups and rapidly mixing Markov chains. *Séminaire de
  Probabilités XVII*, Lecture Notes in Mathematics 986, 243–297.
- Gilbert, E. (1955). Theory of shuffling. Bell Laboratories technical memorandum; Reeds, J.
  (1981), unpublished manuscript (as credited by Bayer & Diaconis).
- Trefethen, L. N. & Trefethen, L. M. (2000). How many shuffles to randomize a deck of cards?
  *Proc. R. Soc. Lond. A* 456, 2561–2568.
- Diaconis, P. (1996). The cutoff phenomenon in finite Markov chains. *PNAS* 93(4), 1659–1664.
