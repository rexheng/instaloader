# Round 1 review: substance and story (science editor)

Evidence: `review/` pack (metrics.json 13:36 is newer than final.mp4 13:34, so the existing pack was used). I read report.md, all 12 contact sheets and 12 full-resolution keyframes (0:12.0, 0:33.0, 1:05.2, 1:13.1, 1:27.9, 1:46.6, 1:51.9, 2:14.3, 2:30.6, 2:52.4, 3:10.9, 3:24.7). I also extracted extra frames: the d counter at 1:51.2–1:55.0 (it settles on 0.61, matching narration), plus 1:19.4, 2:29.4, 3:28.0, 3:29.6 and 3:30.4. I read script.md, narration.txt, facts.md, sim.py, deck_pick.py and the transcript. Every number was recomputed independently: Eulerian numbers from the closed form, the Bayer–Diaconis Theorem 1 pmf, and a 200k-deck forward GSR Monte Carlo of the top card. Citations were checked by web search, including the 1998 Trefethen draft text.

```
EPISODE: 006 — "Seven Shuffles: When a Deck Suddenly Becomes Random"
IDEA: A riffled deck's order is governed entirely by its count of rising sequences; each riffle roughly halves that count's gap to a random deck's while the random bell's spread stays fixed, so the deck stays almost perfectly detectable through four riffles and then drops off a cliff near seven, even though the top card looks random after four.
SCORES: Hook 8.5 · Clarity 8 · Visual 7.5 · Motion 8 · Audio 8.5 · Concision 8 · Originality 8.5
WEIGHTED: 8.1   AFTER CEILING: 8.1  (lowest 7.5 + 2 = 9.5, not binding)
CAPS: none
FINAL: 8.1   PASS: no
```

## FACTS

All numbers were recomputed independently in a scratch script (exact rationals for Eulerian numbers and Theorem 1; Monte Carlo for the top card).

| Claim | Verdict | Source / check |
|---|---|---|
| GSR model: binomial cut near the middle, cards drop in proportion to packet size (0:47) | Verified | Bayer & Diaconis 1992 p.294; Gilbert 1955 / Reeds 1981 as credited there |
| Top card after 4 riffles: old top card "one time in 15" (0:31) | Verified | exact 6.49% = 1 in 15.4; MC 0.0650. Note: 22 other cards also sit fractionally above 1/52 (max 1.985%), but card 1 carries 96% of the excess, so "only" is a fair simplification |
| Top-card guesser right "52%" (0:36), meter 52.4% | Verified | TV(top card) = 0.0475 → ½+½·0.0475 = 52.4% |
| One riffle → 2 rising sequences; 4 riffles → at most 16 (0:53–1:03) | Verified | a-shuffle has ≤ a rising sequences; P(R>16 \| 4 riffles) = 0 exactly |
| "This deck has 14" (1:05) | Verified (simulated) | seeded GSR deck, R = 2,4,8,14; exact mean 14.10. Not labelled "simulated" on screen |
| Perfect shuffle averages 26.5 (1:07) | Verified | (n+1)/2; sd √(53/12) = 2.10 |
| ≤16 sequences "once in 2 million decks" (1:11) | Verified | 4.666e-7 = 1 in 2,143,307 |
| Wrong "about once in 4 million games"; meter 99.99998% (1:17) | Verified | ½·4.666e-7 = 1 in 4.29 M; 99.999977% |
| Order's chance depends only on rising sequences (1:25) | Verified | B&D 1992 Thm 1: C(2^k+n−r, n)/2^{kn} |
| Red area = distance; accuracy = ½+½d (1:39–1:49) | Verified (asserted, not shown) | TV of R-distributions equals full TV since the likelihood ratio is a function of r; Bayes accuracy at 50/50 prior = ½(1+TV) |
| d = 0.92, 0.61, 0.33 after 5, 6, 7; 0.17 after 8 | Verified | recomputed 0.9237, 0.6135, 0.3341, 0.1672; B&D Table 1 |
| Gap 12, 7, 3.5, under 2 ("about half each time") | Verified | 12.401, 6.895, 3.552, 1.790 (ratios 0.56, 0.52, 0.50). On-screen "÷2" is stated as exact, but it is approximate |
| Bell spread "near two"; "2.1" | Verified | 2.1016 |
| Gap ≈ 230/2^k | Verified as large-k limit | gap·2^k = 198, 221, 227, 229, 229.6 → n(n+1)/12 = 229.67. At k=4 the formula gives 14.4 vs the actual 12.4 |
| 2^k ≈ 110 → "just under seven" | Verified | 229.67/2.10 = 109.3; log2 = 6.77 |
| Gap ~ n², spread ~ √n → cliff ~ (3/2)log2 n; on screen "k ≈ (3/2)log2 n − 1.8" | Verified | n²/(12·2^k) = √(n/12) → k = 1.5 log2 n − log2 √12 = 1.5 log2 n − 1.79; n=52 → 6.76 |
| "Bayer and Diaconis proved it in 1992" (2:36) | Verified, attribution incomplete | Ann. Appl. Probab. 2(2):294–313, doi:10.1214/aoap/1177005705 ("(3/2)log2 n + θ shuffles are necessary and sufficient"). Aldous (1983) had already shown the (3/2)log2 n asymptotics, and the Trefethens' own abstract calls it "a celebrated theorem of Aldous, Bayer and Diaconis". The "−1.8" on screen beside the B&D citation is the episode's heuristic, not B&D's constant (theirs puts d = ½ near 1.5 log2 n − 2.2) |
| 7 is first count with d < ½ (2:40) | Verified | 0.614 → 0.334 |
| Trefethen & Trefethen measured information, "no cliff", "five or six shuffles doing a reasonable job" | Verified | Proc. R. Soc. Lond. A 456:2561–2568 (2000). 1998 draft text: "there is no cutoff"; "3.52% of the information remains after five shuffles and 0.92% after six"; Science News (Peterson 2003): "five shuffles would do a reasonable job … six would make it practically certain" |
| Many Markov chains show the same cliff | Verified | Diaconis 1996, PNAS 93(4):1659–1664: chains "often" show a sharp cutoff (and the drunkard's walk does not, which matches "many") |
| Top-card-only distance 0.71, 0.37, 0.12, 0.05 (3:07 curve) | Verified | exact 0.708, 0.371, 0.124, 0.048 |
| Landing meter 96.2 → 80.7 → 66.7 → 58.4 → 54.3 → 52.1% | Verified | ½(1+TV_k) |
| "Right only two times in three" after 7 | Verified | 66.70% |
| "Fooling someone who counts sequences that well takes ten" | Verified | 52.15% after 10 vs 52.4% top-card after 4 (9 riffles = 54.3%) |

No wrong, fabricated or uncited empirical claim found. This is the cleanest fact sheet I have checked in this series.

## MECHANICS

runtime 3:31.7 · 157 wpm (speech time; 544 words) · max internal silence 1.98 s (0:09.7–0:11.7, the planned prediction hold) · max static 3.27 s (2:54.8) · −14.0 LUFS / −2.1 dBTP · leading 0.00 s / trailing 1.82 s · WER 1.5% · banned phrases 0 · banned patterns 0. Only one question is asked; the signposts are "So everything fits in one chart" and "That's the cliff" (both acceptable).

No mechanical caps triggered.

## Narrative read (story editor)

- **Hook (0:00–0:11): strong.** The first frame is the sorted deck. Heads/tails is a real decision game, and the viewer commits on a 50–100% meter with a "?" and a 2.0 s hold. The top-card beat then *confirms* the viewer's likely wrong belief: 52%, "Four riffles look like plenty". The reversal to 99.99998% at 1:19 is a Veritasium-grade misconception break.
- **Stakes (0:11–0:19): the weakest sentence in the script.** "Casinos and simulations both need to know how many riffles it takes" is wrong for simulations: simulations never riffle. The link to Markov chains does not arrive until 2:58, so a first-time viewer hears a non sequitur here.
- **Sag at 1:56–2:36.** Ten numbers and three scaling laws arrive in 40 s (12, 7, 3.5, 2, 2, 230, 2^k, 110, 7, n², √n, 3/2 log2 n). Each is correct, but the viewer is handed them rather than seeing them. The constant 230 is never shown to come from the gap row (12.4·16 = 198, which is *not* 230). n²/12 and √(n/12) at 2:27–2:33 are announced, not derived.
- **"accuracy = ½ + ½d" (1:47) is asserted.** It is the single bridge between the opening game and the distance curve, and it gets no picture (guess "riffled" wherever purple > blue: you win ½·P(A) + ½·(1−U(A)) = ½ + ½d).
- **Honest limit: excellent.** "Seven belongs to this yardstick" plus the Trefethen counterpoint is exactly the BAR §2 "honest limits" move.
- **Payoff is thin.** The data-science consequence ("one statistic can settle long before the whole chain does") gets a single sentence at 3:06–3:11 over the gray top-card curve, with no concrete MCMC instance such as a trace plot or a single-parameter R-hat. It is correct but abstract.
- **Landing works.** It returns to the meter, and the final line reframes the cold open, with the 10-riffle needle landing on the 52.4% top-card ghost. But riffles 8–10 run in about 2.5 s (3:27.5–3:30.0), and the needle-on-ghost coincidence is on screen for about 1 s before the end card fades over it (3:30.4 frame).

## Visual and motion notes (scored, not my main remit)

- **1:05–1:33 and 3:13–3:30: the rising-sequence traces are a tangle.** At 1:13.1 both decks show a mesh of near-horizontal yellow lines, and "14" vs "26" can only be read from the numerals, not from the picture. This is the episode's central object, and it is not readable as a shape.
- **1:35–2:27: the citation shares a baseline with the axis title.** "Bayer & Diaconis, 1992 · Ann. Appl. Probab." ends about 24 px before "rising sequences" on the same baseline (kf 1:51.9, 2:14.3), so it reads as one line.
- **Gray text contrast is low.** GRAY #8B939E on BG #14161B is 5.8:1, under the §5 7:1 text minimum. It is used for primary labels ("rising sequences", "card number", "chance", "information yardstick").
- **2:03 onward: "÷2" over each arrow is stated as exact.** The actual ratios are 0.56, 0.52 and 0.50.
- **Transient ghost overlaps.** Duplicate gap-row text at 2:19, doubled "spread 2.1" at 2:21 and doubled "2^k ≈ 230/" at 2:29 are visible for under 1 s. Not capped, but they look sloppy at full resolution.
- **Motion strengths.** The top card flies from the deck into its histogram bar. The 14/26 counters fly to the rising-sequence axis. The purple histogram slides through k while d counts down live. Equation terms come by TransformFromCopy from the gap row and the spread bracket. These are good.

## FIXES (highest impact first)

1. **[1:05–1:33, 3:13–3:30][Visual/Clarity] The rising-sequence traces cannot be read as 14 vs 26.** Redraw each rising sequence as its own horizontal row. Keep the bar positions, but lift every card's bar top onto a y-level equal to its sequence index (a "staircase" view), or tint each sequence with alternating light/dark yellow and thicken its line to 4 px. The 4-riffle deck then shows 14 long rows and the perfect deck 26 short ones, and the contrast is visible before the numerals appear. Optionally animate one riffle splitting a row into two (0:59 "can split each sequence in two") so the doubling is seen.
2. **[1:44–1:49][Clarity] "accuracy = ½ + ½d" is announced.** Before writing it, show the rule. Tint the bins where purple > blue with a bracket "guess: riffled", and the rest "guess: perfect". Show the two win rates as two short red/blue bars, then TransformFromCopy those into ½·P + ½·(1−U) → ½ + ½d. Add about 6 s of narration: "Say 'riffled' wherever purple is higher. You win half of the riffled games plus half of the perfect ones, which comes to a half plus half the red area."
3. **[2:15–2:36][Clarity] 230, n²/12 and √(n/12) arrive from nowhere.** (a) Show gap×2^k as a live product under the gap row: 198 → 221 → 227 → 229 → 230, so "230" visibly emerges from the data. (b) Give one sentence of why for each scaling: "the spread is a sum of 51 nearly independent up-or-down steps, so it grows like root n", and "230 is 52 times 53 over 12, so it grows like n squared" (write `230 = 52·53/12` on screen). Otherwise the payoff formula is a stated fact, not a derivation.
4. **[0:11–0:19][Hook/Clarity] The stakes line says simulations need riffles.** Replace it with: "Card rooms need the answer, and so does every simulation that shuffles by random steps: when is 'mixed' actually mixed?" Or cut "and simulations" and set up the Markov-chain payoff with a single word at 2:58 instead.
5. **[2:58–3:11][Clarity/Hook] The data-science payoff is one abstract sentence.** Make it concrete. Show a tiny MCMC trace for one statistic flattening early while a second statistic is still drifting (labelled "simulated"), or name the practice: "a sampler judged by one parameter's trace plot can look converged long before the joint distribution is". Keep the Diaconis 1996 citation, and add Assaf, Diaconis & Soundararajan 2011 (Ann. Appl. Probab.) if you state that partial statistics mix in about log2 n.
6. **[2:32–2:46][Clarity/Correctness] Attribution and constant.** Change the on-screen citation at 2:36 to "Aldous 1983; Bayer & Diaconis 1992 · Ann. Appl. Probab." and the narration to "Aldous, then Bayer and Diaconis, proved it". Add a gray "(our heuristic)" tag after "− 1.8", or move the B&D citation to the "(3/2)log₂ n" term only, so the −1.8 is not read as theirs.
7. **[3:27–3:31][Motion/Hook] The landing payoff is rushed and buried.** Give riffles 8–10 at least 0.8 s each. Hold the needle-on-ghost frame (52.1% under the 52.4% "top card" label) for 1.5 s with the ghost tick flashing once, and only then fade in the end card. Trim 1.5 s elsewhere to keep the runtime (for example "Start again from order." at 0:46, or "So everything fits in one chart." at 1:33).
8. **[1:49][Hook] The insight beat has no prediction pause.** After "d = 1.00", ask once, "How many more riffles to bring this below a half?", and hold 1.5 s on the empty distance plot before the fifth riffle. This re-commits the viewer to the title's "seven".
9. **[1:35–2:27][Visual] The citation runs into the axis title.** Move the citation to y = −3.0 at the left edge, below the axis-label row, or move "rising sequences" up 0.3 units under the axis, keeping ≥ 0.3 units between them.
10. **[2:03–2:27][Visual/Correctness] "÷2" is stated as exact.** Write "≈÷2" (or "×0.56, ×0.52, ×0.50"), matching the narration's "about half each time".
11. **[1:05][Correctness/§5] The example deck is a simulated draw but is not labelled.** Add a small gray tag "one simulated GSR deck" under the 4-riffle deck at 1:05, and again at 3:13.
12. **[whole episode][Visual] Gray labels are under the 7:1 text contrast.** Lighten GRAY for text labels to about #A3AAB4, which is ≈ 7.5:1 on #14161B. Keep the current gray for axes and ticks.
13. **[2:19, 2:21, 2:29][Visual] Ghost duplicates show during the transforms.** Fade the source copies to 0 within the same `play`, or use `ReplacementTransform`, so that no doubled text survives a frame.
14. **[2:03–2:05][Clarity] "The bell's spread stays near two" is trivially true.** The blue bell never changes. Say instead "and the riffled histogram's width settles to the same two", which is the claim the argument needs (1.08 → 1.77 → 2.01 → 2.08).

REACHES 9 IF ALL FIXED: yes, narrowly. There is no structural problem: hook, misconception, measured fail, one-chart insight, honest limit and landing are all present, and every number is correct. The gap to 9 is (a) the central visual (the trace tangle, fix 1) and (b) two asserted bridges (accuracy formula and scaling constants, fixes 2–3). Polish fixes alone (6–14) would not get there.

KEEP:
- The heads/tails detection game with the 50–100% accuracy meter and the gray "top card 52.4%" ghost. It turns total-variation distance into a stake the viewer feels, and the 10-riffle needle landing on the ghost is the right closing image.
- The top-card misconception beat (52%, "Four riffles look like plenty") followed by the 99.99998% reversal at 1:19.
- "Seven belongs to this yardstick" plus the Trefethen counterpoint. The honest limit is sourced correctly, so keep the citation exactly as is.
