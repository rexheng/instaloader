# Episode 6 — Seven Shuffles: When a Deck Suddenly Becomes Random

**Idea (one sentence):** A riffled deck's chance depends only on its count of rising sequences;
each riffle roughly halves the gap between that count and a random deck's while the random
deck's spread stays fixed, so the deck stays almost perfectly detectable for four riffles and
then falls off a cliff around seven, even though the top card already looks random after four.

Runtime ≈ 3:54 · ≈ 573 words · voice af_heart, speed 0.84.

## Palette (one meaning each, whole episode)

| Colour | Meaning |
|---|---|
| card ramp (slate → ink) | a card's number, 1 to 52 (the deck itself; neutral, not a hue). In card view bar height is also the card number; in level view bar height is the card's rising-sequence index |
| PURPLE | the riffled deck: its tag, its chance, its top-card histogram, its rising-sequence histogram, "say riffled", P |
| BLUE | the perfect shuffle: its tag, its chance, the 1-in-52 line, the bell, the spread bracket and its hops, "say perfect", U, "2.1", √(53/12), √((n+1)/12) |
| YELLOW | rising sequences: the caps/levels on the deck, the counts, the riffle-2 packet tint, the gap between centres, the gap × 2^k row, 230, 52·53/12, n(n+1)/12 |
| RED | what gives the deck away: purple-above-blue area (= distance d), the meter's edge over a coin flip, the distance curve, "whole deck" |
| INK / greys | text, axes, ticks, citations; the "top card only" curve (grey dashed); text grey is #A3AAB4 (7.7:1), GRAY #8B939E only for axes and lines |

## Data and model
- Gilbert–Shannon–Reeds (GSR) riffle model (Bayer & Diaconis 1992, p. 294).
- Every number is exact (rational arithmetic) from `sim.py` → `data.json`; example decks from
  `deck_pick.py` (seed 68, plus a second 4-riffle deck with 14 sequences, seed 10001) →
  `decks.json`. The example decks are labelled "one simulated deck (GSR model)" on screen.
- See `facts.md` for each claim and its source.

## Beats

### 1. Cold open (0:00–0:15, commit at 0:10–0:13)
> Heads, I riffle shuffle a sorted deck four times. Tails, a computer shuffles it perfectly.
> From the deck alone, how often could you tell which? Pick fifty, seventy five, or a hundred
> percent. *[pause 1.5]*

Visual: first frame is TWO sorted decks side by side (52 bars each, height and shade = card
number), "1"/"52" over the left deck's end cards, "top"/"bottom" under it. Purple tag *heads: 4
riffles* above the left deck; it riffles four times. Blue tag *tails: perfect shuffle* above the
right deck, which then jumps into a uniformly random order on "shuffles it perfectly". These are
the same two decks that return side by side in level view at 1:15 (14 vs 26 levels). The accuracy
meter draws (coin flip 50 % → always right 100 %); a "?" hops 50 → 75 → 100 % as each option is
spoken (tick label flags), then a 1.5 s hold.

### 2. Stakes (0:15–0:24)
> Any simulation that mixes by random steps faces this question: stopped too early, it still
> remembers where it started.

Visual: the heads tag flags on "mixes by random steps", the riffled deck on "stopped too early";
on "remembers where it started" a grey dashed diagonal (the sorted deck's profile) is drawn over it.

### 3. Naive build: the top card (0:24–0:45)
> The obvious check is the top card, the one you'd be dealt. Here's how often each card lands
> there after four riffles.

> Almost flat. Only the old top card stands out: one time in fifteen. Judging by the top card,
> you'd be right fifty two percent of the time. Four riffles look like plenty.

Visual: tags, "?" and the perfect deck leave; meter end labels dim to 40 % (they stay, dimmed,
whenever the meter is on screen). The riffled deck shrinks to the top right; its top card's copy
flies into its bar of a purple histogram (x: card number, y: chance on top %). Blue dashed
"perfect: 1 in 52". Only card 1's excess turns red, "1 in 15". Meter fills red to 52.4 %.

### 4. Fail: rising sequences (0:45–1:32)
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

> Call any deck with sixteen or fewer riffled, and you'd be wrong about once in four million
> games. The top card can't see this; it lives in the order between cards.

Visual: the top-card chart fades out (0.45 s) BEFORE the deck moves; the grey "top card 52.4 %"
ghost appears under the meter track. The deck re-sorts in the centre, cuts 26|26 and riffles
slowly (citation: Gilbert, 1955 · Reeds, 1981). Yellow traces join the two sequences; labels
"1, 2, 3, …, 26" and "27, 28, …, 52"; a yellow dot reads sequence 1 left to right.
**Level view** (level unit 0.55 → 0.5 → 0.32 → 0.2 as the levels double, so the deck is 1.2–3.4
units tall): every bar drops to the height of its sequence (two levels), yellow caps, a faint
shelf per level. On "cut" a dashed vertical cut line (21 | 31) with the label "cut"; on "crosses
each level once" yellow rings where it crosses each level and the right packet's bars tint
yellow. Riffle 2; the split: the four new levels alternate untinted / tinted (exact: L1-left,
L1-right, L2-left, L2-right), dashed ceiling "≤ 2² = 4". Riffle 3 (1.4 s + 0.8 s split): 8
(ceiling 8). Riffle 4: 14, ceiling "≤ 2⁴ = 16". Tag "one simulated deck (GSR model)". The deck
then moves to its cold-open place on the left and the perfect deck returns on the right in the
same level view: 26 levels, visibly almost twice as tall. "average 26.5"; the dashed 16-line
extends across both decks; "≤ 16: 1 in 2.1 million" under the perfect deck. On "sixteen or fewer
riffled" the region under the line tints; on "wrong about once in four million" the needle jumps
to 99.99998 %. The top card is boxed; all caps flash on "order between cards".

### 5. Insight: one chart (1:32–2:48)
> Bayer and Diaconis proved that in this model, decks with the same count are equally likely.
> *[pause 0.7]*

> So pile each deck onto its count. *[pause 0.4]*

> Blue is a perfect shuffle, purple is four riffles. The red area, purple above blue, is the
> distance from random. Right now it's one.

> How many more riffles to bring it below a half? *[pause 1.5]*

> A fifth riffle: point nine two. A sixth: point six one.

> Guess riffled wherever purple is higher. You catch seventy eight percent of riffled decks, but
> flag seventeen percent of perfect ones. Accuracy is a half plus half the difference: the red
> area.

> A seventh riffle: point three three.

> Meanwhile the gap between the centers roughly halved each riffle, while purple's spread settled
> to blue's: about two.

> While the gap spans several spreads, the distance stays near one. Once it's down to about one
> spread, the distance halves too. That's the cliff.

> Gap times two to the k levels off near two hundred thirty. *[pause 1.2]* So the gap meets the
> spread when two to the k is about a hundred and ten: just under seven. *[pause 0.8]*

> Both numbers come from the deck's size. *[pause 1.0]* For n cards, the gap grows like n
> squared, but the spread only like root n, so the cliff sits near three halves log base two of n.

Visual: the meter fades out before the citation *Bayer & Diaconis, 1992 · Ann. Appl. Probab.*
fades in. "chance 3.5 × 10⁻⁶⁰" under the riffled deck, "chance 1.2 × 10⁻⁶⁸" under the perfect
one; on "equally likely" the riffled deck rearranges into a different 14-sequence deck and "same
chance" appears. During the pause the labels leave and the chart's axes draw on their own. On
"pile each deck onto its count" each deck's 52 bars squeeze, in order, into one square on the
rising-sequence axis (x = 14 purple, x = 26 blue) under its count and a "1 deck" tag; then the
blue bars grow and the purple outline grows from its square. The "k riffles" tag rides above the
purple histogram (switching to the target count at the start of each slide). Red fills
purple-above-blue; a small distance-vs-riffles plot gets a dot at (4, 1.00) with "d = 1.00".
Prediction: the gap bracket (legs on the two centres) draws with "12.4" → row "gap: 12.4"; a dashed
line at d = ½, the "0.5" tick flags, 1.5 s hold. The purple histogram slides to 5 and 6 riffles;
gap and d labels are hidden during each slide and written at the whole count; the row grows
"→ 6.89 → 3.55". At k = 6 the row, bracket and "perfect" leave; shaded zones "say riffled"
(r ≤ 24) / "say perfect"; the purple area flies into `0.78`, the blue bars into `0.17`:
`accuracy = ½(0.78) + ½(1 − 0.17)`; on "a half plus" each term's copy slides down into a second
line `= ½ + ½(0.78 − 0.17)` (red area flashes) → on the seventh riffle the second line rises into
`accuracy = ½ + ½ d` (dims), row and bracket return, "→ 1.79". "(each step ≈ ÷2)"; blue spread
bracket "spread 2.1" (centre to one spread, where the bell is at 61 % of its peak).
**Mechanism, shown:** the chart slides back to 4 riffles (red dot climbs back to 1); blue
spread-long hops are laid along the gap: "5.9 spreads"; dots 1–3 appear at d = 1. On "once it's
down to about one spread" it slides forward to 7: the hops vanish one by one, the last is cut where
the gap ends, "0.85 spreads", the red dot falls to 0.33; dots 6 and 7 flash, dot 8 (0.17)
appears; the cliff is drawn through the dots.
**One equation, in place:** a "× 2^k ≈ 198 → 220 → 227 → 229 → 230" row is built from the gap
values; the rows dim to 30 %, then `gap ≈ 230/2^k = 2.1` is assembled from the gap bracket, the
230 and the spread label (copies fly on arcs, clear of the d-plot) during the pause and holds
≈ 3 s; on "about a hundred and ten" "gap" and "=" leave, 2^k arcs over, 2.1 arcs under: `2^k ≈ 230/2.1 ≈ 110`; `⇒ k ≈ 6.8` (dashed line at
6.77 on the d-plot) and holds. Then, with the chart dimmed: 230 → `52·53/12` (yellow) and 2.1 →
`√(53/12)` (blue) in a fraction, "≈ 110" kept; on "gap grows" 52 → n, 53 → n+1 in the numerator
("∼ n²"), on "spread only" 53 → n+1 under the root ("∼ √n", "≈ 110" leaves); on "three halves"
`k ≈ 6.8` becomes `k ≈ (3/2) log₂ n − 1.8`, grey "(gap = spread rule)" (the −1.8 is our
heuristic, not Bayer–Diaconis's constant).

### 6. Payoff (2:48–3:20)
> Aldous, then Bayer and Diaconis, proved it: for fifty two cards, seven riffles is the first
> count that brings the distance below a half.

> Seven belongs to this yardstick. Trefethen and Trefethen measured information instead: no
> cliff, and five or six shuffles do a reasonable job.

> Many Markov chains share this cliff, and samplers share the trap: one statistic can settle,
> like the top card, long before the whole chain has.

Visual: the chart and rows fade; the d-plot grows into the full distance curve (10 points, Table 1
values; y-title stays "distance d"); the equations stay top right. Citations *Aldous, 1983 ·
Séminaire de Probabilités XVII* and *Bayer & Diaconis, 1992 · Ann. Appl. Probab.*; values
0.92/0.61/0.33/0.17 by the dots, the k = 7 dot flags, the d = ½ line flags. Then *Trefethen &
Trefethen, 2000 · Proc. R. Soc. A* with a grey note "information yardstick: no cliff, 5–6
riffles" and a grey band over 5–6 riffles. Then *Diaconis, 1996 · PNAS*, the cliff flashes, and
the grey dashed "top card only" curve (0.71, 0.37, 0.12, 0.05 …) drops early beside the red cliff
labelled "whole deck".

### 7. Landing (3:20–3:45)
> Back to the coin flip. After four riffles you'd almost never be wrong, same as with an
> unshuffled deck.

> Three more riffles, *[pause 1.2]* and you'd be right only two times in three.

> Four riffles fool someone watching the top card. Fooling someone who counts sequences that well
> takes ten.

Visual: the opening deck returns in level view (14 levels, "one simulated deck"), meter at
99.99998 % with both end labels (40 %) and the grey "top card 52.4 %" ghost under the track.
Riffles 5, 6, 7 (each: riffle, then the levels re-split): the deck grows to 20, 23, 25 levels and
the meter falls 96.2 → 80.7 → 66.7 %. Ghost flags on "top card"; riffles 8–10 (≈ 1.1 s each, marks
kept): 58.4 → 54.3 → 52.1 %, the needle landing above the ghost before "takes ten"; ghost flashes
on "ten"; the landed frame holds, the scene fades fully, then the end card.

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
