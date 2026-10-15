# Episode 72: fact sheet

Primary sources, downloaded and read in full:
- **[SDW06]** Salganik, M. J., Dodds, P. S., & Watts, D. J. (2006). "Experimental Study of Inequality and Unpredictability in an Artificial Cultural Market." *Science* 311(5762), 854–856. doi:10.1126/science.1121066. PDF: pdodds.w3.uvm.edu/research/papers/years/2006/salganik2006a.pdf
- **[SOM]** Supporting Online Material for the paper: pdodds.w3.uvm.edu/research/papers/years/2006/salganik2006a_supp.pdf
- **[W07]** Watts, D. J. (2007, April 15). "Is Justin Timberlake a Product of Cumulative Advantage?" *New York Times Magazine* (Idea Lab).

## Real-world claims (narration and screen)

| # | Claim | Status | Source / check |
|---|---|---|---|
| 1 | "Lockdown" (by 52metro) ranked 26th of 48 in quality. Quality means market rank in the independent condition, so the narration says "listening alone, people ranked this song 26th". | Verified | [W07]: "The song 'Lockdown,' by 52metro, for example, ranked 26th out of 48 in quality; yet it was the No. 1 song in one social-influence world, and 40th in another." [SDW06] defines quality as market share or rank in the independent condition. |
| 2 | Lockdown finished first in one influence world and 40th in another. | Verified | [W07], quoted above. The other six worlds are **not reported**, and the screen says so. Which experiment this was is also not stated, so the narration does not say. |
| 3 | The market was copied into eight worlds, and listeners in them could see download counts. | Verified | [SDW06] p. 854: participants in the social influence condition "could also see how many times each song had been downloaded"; they were assigned to "one of eight 'worlds'". |
| 4 | Over 14,000 listeners (14,341), 48 songs by unknown bands, eight influence worlds and one independent world. | Verified | [SDW06] abstract (14,341) and p. 854 ("48 songs by different bands", "previously unknown songs from unknown bands"). [SOM]: Exp. 1 had 7,149 subjects and Exp. 2 had 7,192 (sum 14,341). |
| 5 | Allocation: about 700 people per influence world and about 1,400 in the independent world, in each experiment. | Verified | [SOM] "Experimental design": 20% independent and 10% per influence world, "about 700 subjects in each of the social influence worlds and about 1,400 in the independent condition." |
| 6 | Published in 2006 (the experiments ran Oct 2004 to Mar 2005). | Verified | [SDW06] *Science* 10 Feb 2006. [SOM] gives the dates. |
| 7 | "When songs were listed by download count" is Experiment 2: one column in descending order of popularity. | Verified | [SDW06] p. 854. |
| 8 | In Exp. 2, every influence world had a Gini coefficient more than twice the independent world's. Values read from Fig. 1B at 400 dpi: worlds ≈ 0.46, 0.51, 0.53, 0.45, 0.50, 0.50, 0.48, 0.56; independent ≈ 0.20 (read precision ±0.01). Smallest ratio is 0.45/0.20 = 2.25, and still over 2 at the worst-case reading (0.44/0.21 = 2.1). | Verified (figure read) | [SDW06] Fig. 1B. The screen shows "values read from Fig. 1B". |
| 9 | Gini coefficient: 0 means all songs have equal market share, 1 means maximum inequality. | Verified | [SDW06] Fig. 1 caption. |
| 10 | "The best songs rarely did poorly, and the worst rarely did well, but any other result was possible." | Verified (verbatim abstract) | [SDW06] abstract. |
| 11 | Participants were mostly teens and young adults recruited from one website (bolt.com). | Verified | [SDW06] p. 854: "recruited mostly from a teen-interest World Wide Web site". [SOM]: "a website popular with teens and young adults from the United States." The narration therefore calls real charts an extrapolation, as the curriculum's pitfall note asks. |
| 12 | Social influence increased both inequality and unpredictability. | Verified | [SDW06] abstract. Unpredictability U in Exp. 2 was ≈ 0.0126 (influence) vs ≈ 0.0038 (independent), read from Fig. 2B. This is not spoken; it backs the episode's thesis. |

## Simulated claims (labelled "simulated" on screen)

Model (`model.py`, deterministic, seed 3): 48 songs with qualities `q = linspace(1.0, 0.1, 48)`, song 1 best. Each world has 3,000 listeners, and each listener downloads exactly one song.
- **Quality-only market (s = 0):** P(pick i) ∝ q_i.
- **Counts-visible market (s = 1):** P(pick i) ∝ q_i·(d_i + 1), where d_i is the song's current download count in that world. This is the strip shown on screen: one blue block of width q, plus one block of the same width for each download.

This model is ours, a standard cumulative-advantage (Pólya-urn-type) model. It is not the paper's procedure: real participants could listen to and download several songs. The narration presents it as "simulated songs", and the formula is introduced as how our strip works.

Recomputed by `python3 model.py 3`:

| On screen / spoken | Value |
|---|---|
| Song 26's finishing ranks across 8 worlds, quality only | 24, 26, 24, 27, 25, 30, 28, 26 → range 24th–30th, spread **6** places |
| Same song, counts visible | 27, 12, 32, 24, 44, 32, 17, 40 → range 12th–44th, spread **32** places |
| Average spread (best minus worst finish) over all 48 songs, quality only → counts visible | 8.9 → 20.6, spoken as "nine places to twenty-one" |
| Robustness of the average spread across seeds 3, 11, 21 and 0–5 | 8.1–9.5 (quality only) vs 20.0–22.7 (counts visible): it always more than doubles |
| "Towers still lean toward better songs" | The winners in the 8 influence worlds are songs 4, 3, 1, 1, 4, 2, 7, 3 (all in the top 7 by quality), but they differ between worlds |
| Simulated Gini (not shown) | ≈ 0.28 quality-only vs ≈ 0.72 counts-visible. The direction matches the paper; the size is larger than in the real experiment, which is why no simulated Gini is shown |

Seed choice: seed 3 was picked because song 26's 8 outcomes show the effect clearly. Song 26 is less dramatic under other seeds (e.g. seed 11: spread 6 → 19). The headline average-spread number is reported because it does not depend on the seed.

## Mathematical claims

- With equal quality q, a song with 1 download has slice q·2 and a song with 0 downloads has slice q·1, so the first is **twice** as likely to be picked next. After 2 downloads to 0 it is q·3 against q·1, **three to one**. Exact.
- P(pick i) = q_i(d_i+1) / Σ_j q_j(d_j+1): the slice divided by the whole strip. This is the definition of the model.
- The x-position of rank r on the cold-open axis uses the same column grid as the quality-ordered bars (rank 1 / best song on the left).

## Cut or softened during fact-check

- "Top-5 quality song had only a 50% chance of a top-5 finish" ([W07]). This is verified but cut for time.
- Which world numbers Lockdown won or lost in is unknown, so the lanes are unlabelled and the six unreported worlds are marked "not reported".
- "Record labels bet on this every day" was cut because it is unsourced.
