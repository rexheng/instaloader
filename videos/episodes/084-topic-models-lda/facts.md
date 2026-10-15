# Episode 84: fact check

Every claim spoken or shown, how it was checked, and where it comes from.

| # | Claim (as used) | Verification | Source |
|---|---|---|---|
| 1 | Two programs (CTM and LDA) were fed the same ~8,000 New York Times articles | Chang et al. §4.1: "a collection of 8447 articles from the New York Times from the years 1987 to 2007". Both models (plus pLSI) were trained on this corpus and on 10,000 Wikipedia articles. The narration says "eight thousand"; the screen says 8,447 | Chang, Gerrish, Wang, Boyd-Graber & Blei (2009), "Reading Tea Leaves: How Humans Interpret Topic Models", NIPS 22, pp. 288–296 (read the PDF text directly) |
| 2 | CTM usually predicts held-out articles better than LDA | §4.2 / Table 1: "in most cases CTM performs best, followed by LDA" (predictive log likelihood on a held-out 20% of the documents) | Chang et al. 2009 |
| 3 | Held-out likelihood means hiding some articles and scoring how well the model predicts their words | §4.2: "we set aside 20% of the documents in each corpus as a test set and train on the remaining 80%"; predictive likelihood p(w_d \| D_train). The screen shows 20% | Chang et al. 2009 |
| 4 | CTM usually lost to LDA with human readers | §4.3, word intrusion: "In most cases LDA performs best. Although CTM gives better predictive results on held-out likelihood, it does not perform as well on human evaluations." Topic intrusion: "LDA and pLSI generally outperform CTM". The Discussion says traditional metrics "are, indeed, negatively correlated" with the human measures | Chang et al. 2009 |
| 5 | Word intrusion = a topic's top words plus one planted word that people must find | §3.1: five most probable words from a topic plus an intruder that has low probability in this topic and high probability in another; six words, shuffled | Chang et al. 2009 |
| 6 | The {committee, legislation, proposal, republican, taxis} topic; 7 of 8 readers picked "taxis" | Fig. 4 (NYT, 50-topic LDA) lists these words for a low-precision topic. Text: "'taxis' did not fit in with the other political words in the topic, as 87.5% of subjects chose 'taxis' as the intruder." Each job "was performed by 8 separate workers", and 87.5% = 7/8 | Chang et al. 2009 |
| 7 | So at most 1 in 8 found the planted word | Each subject picks one word. If 7/8 picked taxis, which is a topic word and not the intruder, at most 1/8 picked the true intruder (model precision ≤ 0.125) | Arithmetic from #6 |
| 8 | Political scientists use topic models to track what the Senate talks about, over 118,000 speeches | Abstract: "a new database of over 118,000 speeches (70,000,000 words) from the Congressional Record", U.S. Senate 1997–2004. The body gives 118,065 speeches and a K = 42 model. NOTE: their model gives each speech a single topic (not LDA), so the episode only says "topic models" | Quinn, Monroe, Colaresi, Crespin & Radev (2010), "How to Analyze Political Attention with Minimal Assumptions and Costs", American Journal of Political Science 54(1):209–228 (read the PDF text) |
| 9 | LDA is from Blei, Ng & Jordan, 2003; it gives every word its own topic, so a document is a mixture of topics | Standard. JMLR 3:993–1022 (2003). In the generative model each token has a topic assignment z, and each document has topic proportions θ_d ~ Dirichlet(α) | Blei, Ng & Jordan (2003), Journal of Machine Learning Research 3:993–1022 |
| 10 | The recolouring rule p(z = k) ∝ (n_dk + α)(n_kw + β)/(n_k + Vβ), with counts that leave out the current word | The collapsed Gibbs sampler for LDA. On screen it is attributed to Griffiths & Steyvers, because Blei et al. 2003 used variational inference | Griffiths & Steyvers (2004), "Finding scientific topics", PNAS 101(suppl. 1):5228–5235 |
| 11 | Topics are co-occurrence patterns, and the names and the number K are human choices | Follows from the model (no word meanings are input). Quinn et al.: "We decided on these labels" for the 42 clusters. Results depend on seed and K (LDA's posterior is multimodal, and Gibbs/variational runs from different inits differ) | Quinn et al. 2010; model definition |

## Toy simulation (all marked "simulated" on screen)

`sim.py` writes `sim.json` and is fully reproducible.

- **Corpus:** 6 speeches × 8 tokens = 48 tokens. Vocabulary: tax, budget, deficit (money words) and troops, war, army (war words).
  - Speeches 1–2 are all money words. Speeches 3–4 are all war words.
  - Speech 5 is 4 money + 4 war. Speech 6 is 3 money + 5 war.
- **k-means:** sklearn KMeans (k = 2, n_init = 20, seed 0) on word counts gives clusters {1, 2} and {3, 4, 5, 6}.
  - The 4 money tokens in speech 5 and the 3 in speech 6 get the war group, so **7 of 48** are wrong. Verified by running the script.
- **LDA:** collapsed Gibbs, K = 2, α = 0.5, β = 0.1, seed 135.
  - Wrong-group tokens per sweep: **24 → 13 → 8 → 3 → 2 → 0**, then 0 through sweep 20.
  - The random start has exactly 24/48 wrong.
  - Final mix: speech 5 = 4/8 blue (exactly half), speech 6 = 3/8 blue.
- **Probe:** the first "war" token of speech 5, at the random start, currently purple. With the probe's own token removed:
  - Speech 5's other 7 words are 5 blue and 2 purple.
  - The war column holds 6 blue and 3 purple.
  - Totals are 27 blue and 20 purple.
  - p(purple) ∝ (2 + 0.5)(3 + 0.1)/(20 + 0.6) = 0.3762; p(blue) ∝ (5.5)(6.1)/(27.6) = 1.2156.
  - Normalized, p(purple) = 0.236 (shown as 24%) and p(blue) = 0.764 (76%).
- **Topic colours:** blue is the topic that ends holding the money tokens (a pure relabelling; LDA topics have no inherent order).
