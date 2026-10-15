# 076 — The Winning Strategy That Never Won a Single Game

**One idea:** in a game where both sides can score, your total is your *share* times the *pot*; Always Defect maximizes the share and shrinks every pot, Tit for Tat gives up the share (never above one half, so it can never win a match) and grows the pot, and the tournament adds up pots.

## Palette (colour -> one meaning)

| Colour | Meaning |
|---|---|
| GREEN | a *cooperate* move (always drawn with the letter C) |
| RED | a *defect* move (always drawn with the letter D) |
| BLUE | the row program's own points / its share of a pot |
| GRAY | the opponent's points; axes, secondary labels |
| YELLOW | focus: the entry or term being discussed, slips, highlights |
| INK | names and labels |

## Beats

| # | t | Narration | Visual |
|---|---|---|---|
| 1 | 0:00 | In nineteen eighty, Robert Axelrod pitted fifteen computer programs against each other. One of them never outscored a single opponent. Where did it finish? [pause 1.5] | A rank ladder of 15 slots (1st to 15th) on the right; on the left a card "opponents outscored" with a yellow 0. A yellow "?" marker beside the ladder. Prediction hold. |
| 2 | 0:12 | First. It was Tit for Tat, the simplest entry: cooperate on the first move, then copy whatever the other side did last. | Marker snaps to slot 1, card gains the name. Below, a two-row move strip: the opponent's moves, and Tit for Tat's moves, each linked by a diagonal arrow from the opponent's previous move. |
| 3 | 0:22 | Every match was two hundred rounds of the prisoner's dilemma. Both cooperate: three points each. Both defect: one each. Defect on a cooperator, and you take five while they get zero. | 2x2 payoff grid, cells fill on cue; your points BLUE, theirs GRAY. |
| 4 | 0:36 | Price wars and arms races have this shape. So how do you win a tournament without winning a match? | Payoff grid slides to the top-right corner and stays as reference. |
| 5 | 0:43 | Build the opposite: a program that can never lose. Always Defect never takes a zero, so no one can outscore it. | The "0" cell of the payoff grid is crossed for Always Defect. Two-row strip appears: Always Defect vs Tit for Tat. |
| 6 | 0:51 | Against Tit for Tat, it grabs five in round one. After that, Tit for Tat copies the defection, and both earn one point a round. Final score: two hundred and four to one ninety nine. A win. | Rounds play as coloured squares; live counters run to 204 vs 199; the payoff cell in use flashes. |
| 7 | 1:06 | Now a small simulated tournament with Axelrod's scoring. Four entries; everyone plays everyone, including its own twin. Grudger cooperates until you defect once, then never forgives. Suspicious Tit for Tat copies too, but opens with a defection. | 4x4 round-robin grid builds; the 204 and 199 fly in from the counters to their cells. Label "simulated". |
| 8 | 1:21 | Each cell is the row program's score, with its margin over the opponent underneath. | Cells fill (score in blue, margin in gray). |
| 9 | 1:27 | Always Defect's row: two wins, two ties, no losses. Tit for Tat's row: no wins at all. Now total the points. Always Defect, eight hundred and eight: last place. Tit for Tat, eighteen ninety nine: more than double. | Margins flagged per row; totals count up in the right column; ranks appear. |
| 10 | 1:42 | So redraw each match as a pot: everything both programs scored, with the row program's piece in blue. Always Defect holds at least half of every pot, but its pots are tiny, about two points a round. Tit for Tat's reach six. | Other rows leave; each cell's numbers turn into a stacked bar (blue = row share, gray = opponent); heights are points per round. |
| 11 | 1:58 | Your score is your share, times the pot. | Formula assembled from one bar: blue piece -> score, blue fraction -> share, whole bar -> pot. |
| 12 | 2:02 | Always Defect's share never drops below one half. Tit for Tat never defects first, so what can its share never rise above? [pause 1.5] | Brackets on the shares; prediction hold. |
| 13 | 2:11 | One half. It cannot win a match. But half of six is three points a round, while Always Defect's half of two is about one. | Two worked instances of the formula, each built from its bar. |
| 14 | 2:21 | A tournament adds share times pot over every opponent. Winning a match only maximizes the first factor. | Formula becomes the sum over opponents; "share" flagged. |
| 15 | 2:28 | Axelrod's real tournament agreed. Tit for Tat averaged five hundred and four points per match, about two and a half a round, and the top eight finishers never defected first. In a second tournament with over sixty entries, it won again. | Rank ladder returns; top 8 slots bracketed "never defected first"; "504 per match"; citation Axelrod 1980, JCR. |
| 16 | 2:44 | Its win depends on the field, and its weakness is mistakes. One slip, and two Tit for Tats echo it back and forth. Over a long, noisy match their pot falls from six a round to about four and a half. Generous Tit for Tat, which forgives about one defection in three, breaks the echo. | Strip: TFT vs TFT with one yellow slip, the echo; live "pot per round" 6 -> 4.5; second strip: GTFT forgives, row returns to green. Citations Axelrod 2012 JTB, Nowak & Sigmund 1992 Nature. |
| 17 | 3:05 | Zero matches won, first place. Tit for Tat never took the bigger share of a match. It won by making the matches bigger. | Return to the opening card (0) and ladder (1st), then the pot bars once more beside it. End card. |

## Sources
- Axelrod, R. (1980a). Effective choice in the Prisoner's Dilemma. *Journal of Conflict Resolution* 24(1):3–25.
- Axelrod, R. (1980b). More effective choice in the Prisoner's Dilemma. *Journal of Conflict Resolution* 24(3):379–403.
- Axelrod, R. (2012). Launching "The Evolution of Cooperation". *Journal of Theoretical Biology* 299:21–24.
- Nowak, M. A. & Sigmund, K. (1992). Tit for tat in heterogeneous populations. *Nature* 355:250–253.
- Rapoport, A., Seale, D. A. & Colman, A. M. (2015). Is Tit-for-Tat the answer? *PLoS ONE* 10(7):e0134128.
- Molander, P. (1985). The optimal level of generosity in a selfish, uncertain environment. *JCR* 29(4):611–618.
