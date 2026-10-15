# Episode 68 — Why Behaviors Don't Spread Like Viruses

**One idea:** a habit needs to be heard from two friends, and only overlapping (clustered) friendships deliver the second signal, so the network that is fastest for a disease is the worst for a behavior.

## Palette (colour -> one meaning, whole episode)

| Colour | Meaning |
|---|---|
| YELLOW | has adopted (the habit / the disease has reached this person); signals travelling along ties |
| GREEN | a second signal: a friend shared by both starters (reinforcement) |
| BLUE | the clustered ring network (its label, its bar, its readout) |
| PURPLE | the randomly rewired network (its label, its bar, its readout) |
| INK / GRAY / DIM | text; axes and not-yet-adopted people; ties |

Never green vs red: green always comes with the number "2" / the word "both".

## Beats

| # | Time | Narration (as spoken) | On screen |
|---|---|---|---|
| 0 | 0:00 | Forty people, four friends each. On the left, your friends are your neighbours. On the right, the same eighty friendships, rewired at random. | Two 40-node rings build: ring lattice (k = 4) left, degree-preserving rewired copy right (chords). Header "40 people · 4 friends each". |
| 1 | 0:09 | You want a new habit, say a weekly run, to reach all forty. Which network do you start it in? [pause 1.5] | Seed slot pulses at the top of both rings; prediction hold. |
| 2 | 0:18 | The standard answer is the right one. Watts and Strogatz showed that a few random shortcuts let a disease spread much faster. | Right ring's long chords flash. Citation Watts & Strogatz, 1998 · Nature. |
| 3 | 0:27 | So treat the habit like a disease. Hearing about it from one friend is enough. | Rule in the middle: "adopt after 1 friend". |
| 4 | 0:33 | Plant it in one person on each side. Every round, anyone with an adopter for a friend adopts. | Round-by-round spread, live round and adopter counters. |
| 5 | 0:41 | The random network has everyone in four rounds. The ring of neighbours needs ten. | Counters: 4 rounds vs 10 rounds. |
| 6 | 0:48 | But nobody takes up running because one friend mentioned it once. Centola and Macy call a behaviour like this a complex contagion: you need to hear it from two friends. | Rule 1 -> 2 (flag). Citation Centola & Macy, 2007 · Am. J. Sociology. |
| 7 | 1:00 | Reset both networks, and plant it in two friends who know each other. | Rewind to gray; two adjacent seeds (Ann, Ben). |
| 8 | 1:05 | On the left, the habit marches around the ring, one person each way, every round. On the right, it never moves. Two out of forty. | Ring fills in 19 rounds; random counter stuck at 2 / 40. |
| 9 | 1:15 | Maybe that network was unlucky, so I simulated two thousand random rewirings. Not once did it reach all forty, and eight times in ten it never got past the first two. | 2,000 tally: "reached all 40: 0", "stuck at 2: 82%" (simulated). |
| 10 | 1:27 | Look at the starters' friends. On the left, these two people are friends with both of them. Each one hears it twice, and adopts. | Rings rewind and lift; the two shared friends and their four ties turn GREEN. |
| 11 | 1:36 | On the right, the starters' other friends are six different people. Six signals, and every one arrives alone. | Six single YELLOW ties fan out to six outlined nodes. |
| 12 | 1:43 | Count what Ann and Ben should share. Ben has three other friends. Each has about a three in thirty eight chance of also being one of Ann's three. Three times three over thirty eight: about a quarter of a person. | Formula built from the nodes: 3 (Ben's friends) × 3 (Ann's friends) / 38 (everyone else) ≈ 0.24. Left: "2". |
| 13 | 1:57 | With k friends each among N people, that is k minus one, squared, over N minus two. A bigger town only pushes it toward zero. The ring gives them two at any size. | TransformMatchingTex to (k-1)^2/(N-2); live N 40 -> 4000, value -> 0.002. |
| 14 | 2:10 | Now turn a dial from ring to random. Swap just four of the eighty ties, and the habit's average reach drops below half. Meanwhile, the disease gets faster. | Rings become the two ends of an x-axis; simulated curve; live dial readouts: habit reach 46%, disease 7.7 rounds. |
| 15 | 2:23 | In twenty ten, Damon Centola ran this as an experiment. Fifteen hundred and twenty eight volunteers got anonymous health buddies, wired into clustered or random networks. | Bars set up; citation Centola, 2010 · Science. |
| 16 | 2:34 | The behaviour was signing up for a health forum. It reached fifty four percent of people in the clustered networks, and thirty eight percent in the random ones, and it spread more than four times faster through the clusters. | Bars grow to 53.8 % and 38.3 %; "4.4x faster" tag. |
| 17 | 2:47 | A second buddy's signal made people significantly more likely to sign up. But some joined after one, so the random networks never froze like our model. And these were strangers in designed networks, not real friends. | GREEN "2nd signal: p < 0.001"; mini random ring (frozen at 2) labelled "strict model" beside the random bar. |
| 18 | 3:00 | So, back to the forty. For a rumour, plant it on the right. For a habit, pick the ring that looked slow: its friendships overlap, and overlap is where the second voice comes from. | Cold-open rings return; the shared-friend triangles glow GREEN along the filled ring. End card. |

## Sources
- Centola, D. (2010). The Spread of Behavior in an Online Social Network Experiment. *Science* 329(5996):1194–1197. doi:10.1126/science.1185231
- Centola, D. & Macy, M. (2007). Complex Contagions and the Weakness of Long Ties. *American Journal of Sociology* 113(3):702–734.
- Watts, D. J. & Strogatz, S. H. (1998). Collective dynamics of 'small-world' networks. *Nature* 393:440–442.
- All network numbers (4 vs 10 rounds, 19 rounds, 0 of 2,000, 82 %, 0.24/0.19, the dial curve) are from `sim.py` / `make_data.py` in this folder and are labelled "simulated" on screen.
