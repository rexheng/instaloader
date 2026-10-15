# 064 · The Karate Club That Split in Two

**One idea:** a community is a group with *more links inside than chance would put there*. Measure the surplus over a shuffled baseline (modularity), and judge that score against shuffles too.

Target runtime ≈ 3:10 · ≈ 470 words · narrator af_heart @ 0.78

## Palette (colour → one meaning, whole episode)

| Colour | Meaning |
|---|---|
| BLUE | algorithm's group 1 (the side holding member 1, Mr. Hi) and its share of link ends |
| PURPLE | algorithm's group 2 (the other side) and its share of link ends |
| YELLOW | focus: the line being cut, and the surplus Q |
| RED | a member the algorithm put on the wrong side (ring) |
| GRAY | chance: the expected-by-chance bar/term, shuffled networks, axes |
| INK | actual counts, text |
| Shape (not colour) | ● circle = joined Mr. Hi's club · ■ square = stayed with the president's club |

Real outcome is carried by *shape*, the algorithm's answer by *colour*, so a mismatch is a circle in purple or a square in blue (plus a red ring) — never red vs green.

## Beats

**B1 · Cold open (0:00)** — network fades in node by node; "34 members · 78 friendships"; readout "wrong side: ?"; citation Zachary 1977.
> Seventy eight friendships among thirty four members of a university karate club. In the early nineteen seventies, a fight over lesson prices split this club in two. From these lines alone, how many people will an algorithm put on the wrong side? [pause 1.5]

**B2 · Naive rule** — caption "community detection: groups from links alone" → "rule 1: cut the fewest lines".
> Finding groups from links alone is called community detection. The obvious rule says a good split cuts as few friendships as possible.

**B3 · Naive build** — the one edge of member 12 turns yellow and is slashed; "lines cut: 1"; colours: 33 purple, member 12 blue.
> The cheapest cut in this network snips a single line. It separates member twelve, who has exactly one friend, from everyone else.

**B4 · Measured failure** — dots morph into circles/squares (real outcome); "Mr. Hi", "president" labels; red rings on 16 purple circles while the readout counts to 16.
> Now check it against history. Circles followed the instructor, Mr. Hi. Squares stayed with the club's president. Lumping thirty three people together puts sixteen of them on the wrong side.

**B5 · Cause named** — member 12's single line flagged; the rings clear.
> This rule rewards loners. Member twelve is cheap to cut only because he has one friend to lose. A fairer test asks whether a group holds more lines inside than chance would put there.

**B6 · Build chance** — network slides left; every line splits into two stubs; "156 link ends".
> So build chance. Keep each person's number of friends, cut every friendship in half, and rewire the loose ends at random. Seventy eight friendships make a hundred and fifty six ends.

**B7 · The picture** — the stubs fly to the top and left sides of a square, each side split blue/purple by ownership; a random sample point drops into the square; diagonal blocks = chance of landing inside; INK "inside" bar vs GRAY "chance" bar.
> Lay all the ends along this side, and again down this one. A random line picks one end from each, so it falls inside a group as often as that group's square covers. Member twelve owns one end, a speck. Everyone else owns the rest, so chance alone puts ninety nine percent of lines inside. The real count is also ninety nine percent.

**B8 · Formula from the picture** — the inside bar becomes Σ e_c/m, the diagonal blocks become Σ (d_c/2m)²; Q readout 0.00 (yellow).
> The score is the surplus, actual minus chance. Call it Q, for modularity. Here it is zero. In symbols, e sub c counts the lines inside group c, out of m, and d sub c counts its ends, out of two m.

**B9 · Fix** — the divider slides from 1/156 to 76/156 while the network recolours; chance bar falls to 0.50, inside 0.87, the yellow surplus grows to Q = 0.37; citation Newman 2006.
> Now let Newman's method hunt for the split with the biggest surplus. Chance now expects half the lines inside, but eighty seven percent are. Q is point three seven.

**B10 · Payoff (real)** — readout "wrong side: 1"; red ring on member 9; his five lines highlighted, three run to purple; citation Zachary 1977.
> Check history again. [pause] Only member nine is on the wrong side. Zachary's own model, in nineteen seventy seven, missed him too. Most of his friends backed the president, but he was three weeks from his black belt test, and the president's club was switching styles. Joining it meant starting over at white belt. He followed his belt.

**B11 · Second failure** — lines swing to random new endpoints (same degrees); colours re-split; Q readout falls to 0.24; label "shuffled club (simulated)".
> One warning before trusting that number. Shuffle the club, keeping the same people and the same number of friends each, but rewiring the lines at random. The hunt still finds two groups, with Q near point two four.

**B12 · Null model** — histogram of best-split Q over 300 shuffles (simulated); yellow line at the real club's 0.37; citation Guimerà, Sales-Pardo & Amaral 2004.
> Across three hundred shuffles, the best split never scored above point three. The real club, at point three seven, sits far outside them. Random networks have modularity too, so a Q means nothing until you compare it with shuffles.

**B13 · Landing** — lines swing back; the network returns to the opening frame, now coloured, "wrong side: 1".
> The algorithm put one person of thirty four on the wrong side. But it would have split a shuffled club just as confidently. What made this split real is that chance never came close.

## Sources
- Zachary, W. W. (1977). An information flow model for conflict and fission in small groups. *Journal of Anthropological Research* 33(4):452–473.
- Newman, M. E. J. & Girvan, M. (2004). Finding and evaluating community structure in networks. *Phys. Rev. E* 69, 026113 (definition of modularity).
- Newman, M. E. J. (2006). Modularity and community structure in networks. *PNAS* 103(23):8577–8582 (leading-eigenvector method; karate club example).
- Guimerà, R., Sales-Pardo, M. & Amaral, L. A. N. (2004). Modularity from fluctuations in random graphs and complex networks. *Phys. Rev. E* 70, 025101(R).
- Data: `networkx.karate_club_graph()` (unweighted, 34 nodes, 78 edges; `club` = club joined after the split). All numbers: `simulate.py` → `data.json`.
