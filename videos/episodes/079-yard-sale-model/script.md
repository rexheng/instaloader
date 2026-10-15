# 079 — Fair Coin Flips, Wildly Unfair Outcomes

**One idea:** when every fair bet is a fixed *fraction* of what you have, losses compound
more than gains, (1 + f)(1 − f) = 1 − f², so a room of perfectly fair trades drains the
poorer half into a few towers unless something redistributes.

Narrator: af_heart, speed 0.84. Room data is simulated (`simulate.py`, seed 1), labelled
"simulated" on screen.

## Palette (colour → one meaning)

| Colour | Meaning |
|---|---|
| BLUE | money: the 500 bars, dollar values, the tree's dollar nodes, paths that end above $100 |
| YELLOW | the stake *f* and focus: the slice that changes hands, *f* in equations, the break-even wall |
| GREEN | a win (×1.2), always with its "×1.2" label |
| RED | a loss and the shrinkage it causes (×0.8, −4 %, 1 − f²), always labelled |
| PURPLE | redistribution (the 1 % shared each round) |
| INK / GRAY / DIM | text, axes and citations, dimmed context |

## Beats

**0 · Cold open (0:00–0:14)** — 500 equal blue bars, axis in dollars. One pair turns yellow;
a yellow $20 slice moves from loser to winner. Brace under the left half: "poorer half owns
$25,000" and a yellow "?".
> Five hundred people, a hundred dollars each. In every trade, a fair coin decides who pays a
> fifth of the poorer player's money. After a thousand trades each, how much will the poorer
> half own? *(1.5 s hold)*

**1 · Stakes (0:14–0:25)** — model name top-right; three more pairs trade; citation.
> This is the yard-sale model, a toy economy physicists use to ask whether inequality needs
> anyone to cheat. Here, nobody can.

**2 · Naive build (0:25–0:47)** — rule morphs to "stake = $10"; bars reset, sort, and run
1,000 rounds; live readout slides $25,000 → ≈ $7,000 and levels; a grey marker keeps the result.
> First, the version intuition expects. Every bet is a flat ten dollars. Sort the room from
> poorest to richest, and luck spreads it out. The poorer half slides from twenty-five thousand
> dollars to about seven thousand, then levels off, because wins and losses are the same size.

**3 · Fail (0:47–1:07)** — rule morphs back to "⅕ × poorer's wealth"; same coin, 1,000
rounds; the y-axis zooms out to $5,000; the left half of the room goes flat.
> Now put the yard-sale rule back. The stake is a fifth of the poorer player's money. Same fair
> coin, same thousand trades.
>
> The poorer half owns four cents. Two hundred and fifty people, four cents between them, while
> the richest five hold a third of all the money.
>
> The coin never changed. The stake did. A stake that scales with your wealth turns adding into
> multiplying.

**4 · Insight (1:07–2:05)** — room shrinks to the corner (kept, dimmed). One player: a
recombining tree 100 → 120 / 80 → 96. "1.2 × 0.8 = 0.96" is built from the edge labels, then
becomes (1 + f)(1 − f) = 1 − f². Then a win-share axis: the break-even wall at 55 %, the
fair-coin spread at 50 % for 100 trades; prediction hold; the tail fills, the spread narrows as
trades → 1,000 while "her average: $100" never moves.
> Follow one player who keeps ending up the poorer one. A win multiplies her money by one point
> two. A loss, by point eight. Win, then lose: ninety-six. Lose, then win: ninety-six again.
>
> Every win and loss pair costs her four percent. In symbols, one plus f, times one minus f, is
> one minus f squared.
>
> So winning half the time is not enough. To break even, she has to win just over fifty-five
> percent of her trades. A fair coin gives her fifty. After a hundred trades, what share of her
> possible paths end above a hundred dollars? *(1.5 s hold)*
>
> About fourteen percent. As trades pile up, the coin's spread narrows around fifty, while the
> wall stays at fifty-five. After a thousand trades, seven paths in ten thousand clear it. Her
> average is still exactly a hundred dollars, held up by those few enormous paths.

**5 · Back to the room (2:05–2:20)** — room returns; a $200 bar and a $2,000 bar trade:
20 % of hers, 2 % of his; 1 − 0.2² = 0.96 vs 1 − 0.02² = 0.9996.
> In the room, the poorer player always stakes a full fifth of her money. The richer one risks a
> smaller slice of his, so the drag hits whoever is behind hardest. The money does not vanish.
> It pools in the towers.

**6 · Payoff (2:20–2:58)** — purple "1 % shared each round" joins the rule; room re-runs, axis
zooms back in, readout climbs to ≈ $8,300. Fit claim + citation; then the honest limit.
> Stopping it takes redistribution. Each round, take one percent of everyone's money and share
> it equally. The poorer half climbs back above eight thousand dollars, and stays there.
>
> Bruce Boghosian's group at Tufts built redistribution, plus a small edge for the rich, into
> this model. It matched the shape of U.S. wealth across twenty-seven years of Federal Reserve
> surveys, with an average error under zero point one six percent.
>
> A good fit is not a cause. The model shows that chance plus proportional stakes is enough to
> build towers, not that every real fortune is luck.

**7 · Landing (2:58–3:10)** — the bars rewind to the opening row of equal $100 bars; flip
counter 250,000; "1 − f²" returns in red.
> Back in the room, a quarter of a million coin flips, and every one was fair. The unfairness was
> in the multiplying.

## Sources
- Chakraborti, A. (2002). Distributions of money in model markets of economy. *Int. J. Mod. Phys. C* 13(10), 1315–1321.
- Hayes, B. (2002). Follow the Money. *American Scientist* 90(5), 400–405 (names the yard-sale model).
- Boghosian, B. M. (2019). Is Inequality Inevitable? *Scientific American*, Nov 2019.
- Li, J., Boghosian, B. M. & Li, C. (2019). The Affine Wealth Model. *Physica A* 516, 423–442 (SCF, 27 years, average error < 0.16 %).
- Simulation: `simulate.py` (numpy, seed 1); exact binomial tails in facts.md.
