# 059 — Why Acquaintances Find You Jobs

**One idea:** a tie helps you only if it is willing to pass news on *and* reaches people you don't already know; closeness raises the first and destroys the second, so the most useful tie is a moderately weak one.

## Palette (colour → one meaning, whole episode)

| colour | meaning |
|---|---|
| INK (off-white) | people in Granovetter's survey; "you"; text |
| RED | the close-friends guess (the naive prediction) |
| BLUE | what you already know: your contacts, mutual friends, overlap share *s* |
| PURPLE | what is new to you: contacts outside your circle, news from there, 1 − *s* |
| GREEN | willingness to pass a tip on |
| YELLOW | help per tie (the product, LinkedIn's causal estimates) and focus |
| GRAY | axes, secondary labels, plain-correlation estimates |

Tie thickness = tie strength (thick = close friend, thin = acquaintance).

## Beats

| t (approx) | narration | picture |
|---|---|---|
| 0:00 cold open | Fifty-four people each got a job through someone they knew. Sort them by how often they saw that person back then. Which pile will be biggest? [pause 1.5] | 54 white dots in a block; three empty piles labelled often (twice a week or more), occasionally, rarely (once a year or less). Hold for the prediction. |
| 0:13 naive guess | Most of us would bet on the left pile. Close friends know us best, and they want to help. | A red dashed ghost pile rises over "often", labelled "close-friends guess". |
| 0:19 reveal | Mark Granovetter published this survey in nineteen seventy-three. Nine people saw their contact often. Thirty, occasionally. Fifteen, rarely. | Dots fall into piles on each number; counts appear; citation. |
| 0:31 fail measured | The close-friends pile holds nine of fifty-four, seventeen percent. His respondents kept correcting him: not a friend, an acquaintance. | 9/54 = 17% beside the ghost; the quote appears top. |
| 0:41 objection | A fair objection, which Granovetter printed in a footnote: most of us have far more acquaintances than close friends. Maybe they win on numbers alone. So split each pile into how many ties, times help per tie. | pile = number of ties × help per tie, built from the piles; "help per tie" boxed yellow. |
| 0:57 build | Take one person: you. Here are your close friends, and close friends tend to know each other. | Network: you, ring of 9 friends on thick blue edges, dim edges between friends. |
| 1:04 | Here's Sam, your best friend. Of Sam's ten other contacts, eight are already yours. | Sam's ten edges light up: 8 blue (mutual), 2 purple (new). Counts 8 and 2. |
| 1:12 | When a job opens in this circle, the news reaches you and Sam at the same moment. Sam's tip arrives as a rerun. | Pulse from a ring node reaches you and Sam together; Sam's packet arrives late, greyed: "already heard". |
| 1:21 | Now Ana, someone you see once a year. Of her ten contacts, you know one. The other nine live in a circle you never hear from, except through her. | Thin edge to Ana; her purple cluster; a job pulse spreads there and crosses only via Ana; "you" flashes purple: new. |
| 1:35 v2 overshoot | So are the weakest ties of all the best? A stranger shares none of your friends, so everything they hear is new to you, but they have no reason to tell you any of it. | A disconnected stranger node at the edge, all purple contacts, but no edge. |
| 1:47 insight | Call s the share of their contacts you already know: eight in ten for Sam, one in ten for Ana. As a toy assumption, say their willingness to pass a tip on grows with s. The share of their news that's new to you is one minus s. | s = 8/10 and 1/10 built from the counts; axes with a green rising line (willing) and a purple falling line (new). |
| 2:05 prediction | Help per tie is the product. Where does it peak? [pause 1.5] | Formula help per tie ∝ s × (1 − s) assembled from the two lines; hold. |
| 2:11 | Not at either end. Sam scores point one six, Ana point oh nine, and a friend with half your contacts in common scores point two five. Where exactly the peak sits depends on the toy assumption. | Yellow hump draws as the product; dots for Ana, the half-shared friend, Sam. |
| 2:25 payoff | In twenty twenty-two, researchers at LinkedIn, Harvard, Stanford and MIT tested this causally. Over five years, People You May Know randomly nudged more than twenty million people toward weaker or stronger new connections. | Toy axes morph into real axes; citation Rajkumar et al., 2022 · Science. |
| 2:40 | For each new connection, they measured the chance it led to a job at the contact's company. It rose with mutual friends, peaked around ten, then fell. | Yellow dots (IV estimates, 2015 wave, digitized) draw left to right; peak marked near 10. |
| 2:52 | Because the nudges were random and the count is per tie, sheer numbers can't explain it. Plain correlations in the same data pointed the other way, toward the strongest ties. In less digital industries, strong ties did help more. | Grey OLS dots rise beside the yellow hump; small note on industries. |
| 3:08 landing | Look back at the fifty-four. The biggest pile wasn't the rarest contacts either. It was the middle one: people close enough to think of you, and far enough to know something you don't. | The three piles return; the middle pile turns yellow. End card. |

## Sources

- Granovetter, M. S. (1973). The Strength of Weak Ties. *American Journal of Sociology* 78(6):1360–1380 (p. 1371 numbers; fn. 17 quote; fn. 18 objection).
- Rajkumar, K., Saint-Jacques, G., Bojinov, I., Brynjolfsson, E., Aral, S. (2022). A causal test of the strength of weak ties. *Science* 377(6612):1304–1310. doi:10.1126/science.abl4476 (Fig. 3B digitized: data/fig3b_digitized.json).
