# 084 · An Algorithm That Finds Topics Without Reading

**One idea:** a topic model never reads. It recolours each word by how much its document uses a topic times how much that topic uses the word, so its topics are just words that travel together. That is why the model that predicts text best is not the one people find most readable.

## Palette (colour → one meaning)

| Colour | Meaning |
|---|---|
| BLUE | topic / group 1 (ends up holding tax, budget, deficit) |
| PURPLE | topic / group 2 (ends up holding troops, war, army) |
| YELLOW | focus: the word, row or column being looked at, and the inequality sign under test |
| RED | a word in the wrong group (red ring, so never colour alone) |
| GRAY | an unassigned word, axes, secondary labels, citations |
| INK | text |

## Beats

| # | Time (approx.) | Narration | Screen |
|---|---|---|---|
| 0 Cold open | 0:00 | Two programs were fed the same eight thousand New York Times articles, and each sorted the words into topics. This one, CTM, predicts unseen articles better than this one, LDA. Will its topics also make more sense to people? [pause 1.5] | A grid of article pages, "8,447 NYT articles". The two names emerge from the pages. Row "predicts unseen articles: CTM > LDA" with a yellow ">", then row "makes sense to readers: CTM ? LDA". Citation: Chang et al. 2009 |
| 1 Stakes | 0:14 | Political scientists use topic models to track what the Senate talks about, across more than a hundred and eighteen thousand speeches. If the topics mean nothing, so does the measurement. | The page grid becomes a denser grid, "118,065 Senate speeches · 1997–2004". Citation: Quinn et al. 2010 |
| 2 Toy | 0:26 | So shrink the problem: six simulated speeches, eight words each, from a six-word vocabulary. Every dot is one word. A program that cannot read sees only this: which words share a speech. | The grid collapses into 6 rows; the word columns appear; 48 grey dots drop into the cells. Tag: "simulated" |
| 3 Naive | 0:41 | The obvious first try is k-means: cluster whole speeches into two groups. Speeches one and two land together, and so do three and four. | The right-hand "group" bars fill solid blue (rows 1–2) and purple (rows 3–4); the dots take their row's colour |
| 4 Fail | 0:50 | Speech five is half money words and half war words, but k-means has to give it a single group. So does speech six. Seven of the forty-eight words land in the wrong group, because the label belongs to the whole speech. | Rows 5–6 turn solid purple. Red rings appear on the 7 money dots there. Metric: words in wrong group = 7/48 |
| 5 Fix | 1:05 | Latent Dirichlet Allocation, from Blei, Ng and Jordan in two thousand and three, moves the label onto each word, so a speech can be a mix. Start by coloring every word at random. | Citation: Blei, Ng & Jordan 2003 · JMLR. The bars become "mix" bars. The dots get random colours, and the metric jumps to 24/48 |
| 6 Insight | 1:18 | Now recolor one word: this war, in speech five. Look along its row: of the other seven words, two are purple. Look down its column: of the twenty purple words, three are war. | Probe dot ringed yellow. Row highlight, and the 2 purple dots flag. Column highlight, and the 3 purple dots flag. All purple dots flag ("20") |
| 7 | 1:34 | Multiply those shares, with a small alpha and beta so no count is ever zero. Do the same for blue, and redraw the color with those odds. Purple gets only twenty four percent, because the colors are still noise. | The formula is built from the flagged dots: p(purple) ∝ (2+α)·(3+β)/(20+6β). The odds bar reads blue 76% / purple 24%. Citation: Griffiths & Steyvers 2004 · PNAS |
| 8 | 1:50 | In symbols: how much speech d uses topic k, times how much topic k uses word w. | The concrete numbers morph into n_dk, n_kw, n_k, V. Row and column highlights pulse with their terms |
| 9 Predict | 1:58 | Now do that to every word, sweep after sweep. Before it runs, predict speech five: one color, or a split. [pause 1.5] | Row 5 boxed in yellow; the sweep counter appears |
| 10 Run | 2:08 | Each recoloring makes the rows and columns a little less random, which sharpens the next one. Twenty four wrong words become thirteen, eight, three, two, then none. Speech five settles at exactly half and half, which k-means could never say. | Sweeps 1–5 land on the spoken numbers; the metric counts down and the mix bars update. The counter runs on to 20 with no change. Row 5's bar is flagged at 50/50 |
| 11 Meaning | 2:25 | Notice what the program never used: what any word means. Blue is only words that keep turning up together. Calling it money is our reading, and so is the choice of two topics. On real text, another random start can split the words differently, and so can another K. | Column headers copy down into "tax budget deficit" (blue) and "troops war army" (purple), with grey "“money”?" / "“war”?" labels and "K = 2" |
| 12 Payoff | 2:45 | So how do you choose? The usual score is held-out likelihood: hide some articles, and check how well the model predicts their words. Chang and colleagues added a test with human readers. | The page grid returns, 20% slides out and is labelled "held out". Citation: Chang et al. 2009 · NIPS |
| 13 | 2:58 | Show people a topic's top words with one planted intruder, and see if they can find it. For this New York Times topic, seven of eight readers picked taxis. But taxis was the model's own word, so at most one in eight found the plant. | Word chips "committee legislation proposal republican taxis + [planted]". Eight reader dots; 7 move to "taxis"; 7/8. Underline: "model's top word"; ≤ 1/8 |
| 14 | 3:15 | Across their tests, the correlated topic model usually beat LDA at predicting held-out text, and usually lost to it with readers. | The cold-open rows return; "?" turns into "<" |
| 15 Landing | 3:24 | So the answer to the opening question is no. A topic model finds words that travel together; deciding which of those patterns is a topic still takes a reader. | The yellow "<" is flagged, then the end card |

**Words:** ~500. **Target:** ~3:35.

## Sources (on screen)
- Chang, Gerrish, Wang, Boyd-Graber & Blei (2009). Reading Tea Leaves: How Humans Interpret Topic Models. NIPS 22.
- Quinn, Monroe, Colaresi, Crespin & Radev (2010). How to Analyze Political Attention with Minimal Assumptions and Costs. AJPS 54(1).
- Blei, Ng & Jordan (2003). Latent Dirichlet Allocation. JMLR 3.
- Griffiths & Steyvers (2004). Finding scientific topics. PNAS 101 (suppl. 1).
