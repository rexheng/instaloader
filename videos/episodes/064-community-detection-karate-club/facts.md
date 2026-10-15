# 064 · Fact sheet

All network numbers recomputed by `simulate.py` (networkx 3.7, unweighted graph) → `data.json`.

| # | Claim (as spoken / shown) | Verification | Source |
|---|---|---|---|
| 1 | 34 members, 78 friendships | `karate_club_graph()` has 34 nodes, 78 edges. Zachary: "Only 34 individuals are presented"; the club itself had 50–100 members, so we say "thirty four members", not "the whole club" | Zachary 1977, JAR 33(4):452–473; networkx |
| 2 | University karate club; observed early 1970s; split over lesson prices | Zachary: "observed for a period of three years, from 1970 to 1972"; conflict "between the club president, John A., and Mr. Hi over the price of karate lessons"; "formal separation of the club into two organizations" | Zachary 1977 (PDF, read via communicationcache.com mirror); UCINET dataset page |
| 3 | Mr. Hi = instructor; the other leader = club president | Zachary: John A. is "the club president"; Mr. Hi "the instructor". Member 1 = Mr. Hi, member 34 = John A. (UCINET) | Zachary 1977; UCINET page |
| 4 | Circles followed Mr. Hi, squares stayed with the president | networkx `club` attribute = club joined after the split: 17 "Mr. Hi", 17 "Officer". Matches Zachary Table 3 for the checked rows (3: Mr. Hi's; 9: Mr. Hi's; 10: Officers') | networkx docs; Zachary Table 3 |
| 5 | Cheapest cut = 1 line, isolating member 12 (one friend) | Stoer–Wagner global min cut = 1, side = {node 11} = member 12, degree 1 | computed |
| 6 | That split puts 16 on the wrong side | Best labelling of {12} vs 33 others: the 33-group = president's side → the 16 other Mr. Hi members are wrong (17 otherwise) | computed |
| 7 | 78 friendships → 156 ends | 2m = 156 | arithmetic |
| 8 | Chance of a random line landing inside group c = (d_c/2m)²; modularity Q = Σ e_c/m − Σ (d_c/2m)² | Configuration-model null; Newman–Girvan modularity (the (d_c/2m)² form is the standard large-m approximation used in the definition) | Newman & Girvan 2004 PRE 69, 026113; Newman 2006 PNAS |
| 9 | Cheap cut: chance 99 % inside, actual 99 % inside, Q = 0 | expected = (1/156)² + (155/156)² = 0.987; actual 77/78 = 0.987; Q = −0.00008 → shown "0.00" | computed |
| 10 | Newman's method's split: chance 50 %, actual 87 %, Q = 0.37 | leading-eigenvector sign split: groups of 16 and 18; ends 76 and 80; expected 0.237 + 0.263 = 0.500; inside 33 + 35 = 68 of 78 = 0.872; Q = 0.3715 | computed; method from Newman 2006 PNAS 103:8577 |
| 11 | Only member 9 on the wrong side | eigenvector split vs `club`: only node 8 (= member 9) differs. Newman 2006 reports this division coincides with the known *faction* split; Zachary lists member 9 in John's faction but in Mr. Hi's club, consistent with both | computed; Newman 2006; Zachary Table 3 |
| 12 | Zachary's own model also missed member 9 | Zachary: model "97% accurate in predicting club membership after the split"; Table 3 row 9 = the only Miss ("Person number 9 was a weak supporter of John but joined Mr. Hi's club after the split") | Zachary 1977 |
| 13 | Three weeks from his black-belt test; president's club switched styles; would restart at white belt | Zachary (quoted on UCINET page): "he was only three weeks away from a test for black belt (master status) when the split in the club occurred"; "he would have had to give up his rank and begin again in a new style of karate with a white (beginner's) belt, since the officers had decided to change the style of karate practiced in their new club" | Zachary 1977 |
| 14 | "Most of his friends backed the president" | member 9's neighbours: members 1, 3, 31, 33, 34 → 3 of 5 in the Officers' club | computed (networkx data) |
| 15 | Shuffled club keeps everyone's number of friends | `double_edge_swap`, 780 swaps (10 per edge), preserves every degree | computed (simulated) |
| 16 | Shuffled club still splits with Q ≈ 0.24 | representative shuffle (closest to the median): Q = 0.236 | simulated |
| 17 | 300 shuffles: best split never above 0.3; real club 0.37 far outside | best bisection found (30-restart local search) per shuffle: mean 0.237, min 0.203, max 0.290; no shuffle ≥ 0.37 | simulated, seed 64 |
| 18 | Random networks have modularity too | Guimerà, Sales-Pardo & Amaral show "random graphs and scale-free networks have modularity" from fluctuations, which "must be taken into consideration to define statistically significant modularity" | Guimerà et al. 2004, Phys. Rev. E 70, 025101(R) |

## Honest caveats kept off-screen (not claimed)
- The *exact* maximum-Q two-way split has Q = 0.3718 (vs 0.3715) and moves member 10 as well; we say "Newman's method" and show what that method returns, not "the optimum".
- Modularity of the true club split is 0.358, slightly below the found split: the algorithm's answer is not identical to history.
- Whether Q's null model is "the right" chance model is a modelling choice; we name it (rewire ends, keep degrees) on screen.
- Curriculum's resolution-limit beat (Fortunato & Barthélemy 2007) cut to keep one idea.
