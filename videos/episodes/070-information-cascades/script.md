# Episode 70: How Rational People Join the Wrong Crowd

**One idea:** once the public record leads by two, a rational person's private evidence can no longer change their choice, so every later choice adds nothing. The whole line's verdict rests on the first few draws and is wrong one time in five, however long the line gets.

## Palette (colour -> one meaning)

| Colour | Meaning |
|---|---|
| RED | urn A: red balls, "A" guesses, the A wall. In our run the true urn is B, so red is also the wrong answer and the error rates |
| BLUE | urn B: blue balls, "B" guesses, the B wall (the true urn) |
| YELLOW | focus: the person deciding now, the token, the term that is changing |
| GRAY / DIM | private, hidden or ignored information (an unseen ball, a ball nobody uses), axes |
| INK | text |

## Beats

| # | Beat | Narration | Picture |
|---|---|---|---|
| 0 | Cold open (0:00) | One of these two urns was picked in secret. A hundred people guess which, one at a time, out loud. How often is the hundredth guess wrong? [pause 1.5] | Urns A and B, a yellow "?" between them. A row of 100 dots is the line, and dot 100 turns yellow. |
| 1 | Setup | Urn A holds two red balls and one blue. Urn B holds two blue and one red. Each person draws one ball in private, puts it back, and hears every guess before theirs. So a single ball matches its urn two times in three. | Balls drop into the urns. A grey "private" ball appears under each person. 2/3 is built from urn B's balls. |
| 2 | Naive expectation and stakes | With all hundred balls in view, a simple majority would be wrong three times in ten thousand. The last person can't see the balls, only the ninety-nine guesses. Restaurants, bestsellers and stock tips work the same way: you see what people chose, not why. | Ball row reveals 67 blue and 33 red (simulated). "majority of 100 balls: wrong 0.03%". The balls hide again, and the row labels "guesses: public" and "balls: private" flag. |
| 3 | Naive run | Let's run it. Secretly, the urn is B. Person one draws red and says A. Person two draws red too, and says A. | Urn B is boxed and becomes the "true urn: B" tag. Four large people appear, each with a private ball bubble and a guess box. Each guess drops into the tape. |
| 4 | The flip | Person three draws blue. But those two A's each stand for a red ball, and two reds against one blue favour urn A. So she says A, and her blue ball never reaches the record. | The two A boxes become two red balls next to person 3's blue ball: "2 vs 1 → A". Her bubble greys out. |
| 5 | Copying | Person four sees the same two A's and does the same arithmetic. So does everyone after her. | Person 4 repeats it. The tape fills with red A's up to person 100. |
| 6 | The line | A hundred guesses of A, sitting on sixty-seven blue balls. | Ball row reveals 67 blue. |
| 7 | Fail, measured | Simulate a hundred thousand lines, and the hundredth person is wrong twenty percent of the time, more than six hundred times worse than the pooled balls. The cause is everyone after person two: each guess just repeats the record. | Bar chart. A live counter runs to 100,000 lines and the red bar settles at 20.0%. The pooled bar is a 0.03% sliver. In the tape, guesses 3 to 100 dim and 1 to 2 are boxed. |
| 8 | Insight: the token | So track the record as one token. Each guess that still reveals a ball moves it a step: left for red, right for blue, and a tie goes to your own ball. Two steps from the middle, no single ball can outweigh it, and the token locks. | A number line from −2 to +2 with a red wall (locked on A) and a blue wall (locked on B). The yellow token steps and locks. |
| 9 | Replay | Here, two reds locked it on A. Start over from the middle. Each step goes right two times in three. Take two steps. | The token replays the run: two left steps (tape guesses 1 and 2 flag) and it locks on A. It resets. Arrows get 2/3 and 1/3. |
| 10 | Two-step paths, plus a prediction | Blue, blue, four ninths: locked on B. Red, red, one ninth: locked on A. One of each, four ninths: back to the middle, and the race restarts. Does a longer line rescue her? [pause 1.2] | Three curved paths, each with its probability. Hold. |
| 11 | Formula from the picture | No. Only the first two paths ever end the race, so the wrong lock wins one ninth out of five ninths: one in five. For a line of ten people or ten million. | The loop dims. 1/9 ÷ (1/9 + 4/9) = 1/5 is built by TransformFromCopy from the path labels. |
| 12 | General case | For any ball accuracy p, the wrong share is q squared over q squared plus p squared, with q equal to one minus p. | The ninths morph into q² and p², and q = 1 − p appears. |
| 13 | Fix | The fix is one rule: announce your ball, not your guess. Every step counts again, the token never locks, and the hundredth person is back to three mistakes in ten thousand. | The walls dissolve and the token wanders freely. The live error number drops from 20% to 0.03%. |
| 14 | Payoff (real) | Anderson and Holt ran this game with real urns and cash prizes, six people a round. Where a cascade could form, one did in forty-one of fifty-six rounds, and thirteen of those locked onto the wrong urn. | A waffle of 56 rounds: 28 blue, 13 red, 15 outlined. Citation. |
| 15 | Honest limit | Their subjects weren't perfect copiers. In about a quarter of the cases where copying was optimal, people followed their own ball anyway, and each deviation put a real ball back into the record. | "26%" with a label. The 15 no-cascade rounds flag. |
| 16 | Landing | So look again at this row of a hundred A's. It sounds like a hundred votes. It holds two balls of evidence. | The tape of 100 red A's returns over the 67-blue ball row. All except the first two dim, and the first two are boxed. End card. |

## Sources
- Bikhchandani, Hirshleifer & Welch (1992), *J. Political Economy* 100(5):992–1026 (the model).
- Anderson & Holt (1997), *American Economic Review* 87(5):847–862 (the lab: 41 of 56, 13 reverse, 26%).
- All other numbers are exact calculations or simulation in `sim.py` (seeded).
