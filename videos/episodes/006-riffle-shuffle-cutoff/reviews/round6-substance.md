# Episode 006, round 6: substance and story critic (science editor), independent pass

**Evidence.** I reused the existing `review/` pack, because metrics.json (23:54) is newer than final.mp4 (23:52). From it I read:
- report.md
- all 12 contact sheets
- full-resolution keyframes kf_01, 02, 04, 09, 13, 15, 19, 25, 27

I also extracted my own frames with ffmpeg:
- 2:30.6, 2:31.0 and 2:31.4 (the ×2^k row)
- 3:06.0
- 3:30.6 and 3:31.6 (the landing meter)
- a crop strip of the citation slot at 2:47.6–2:52.4, to time how long the Aldous citation stays on screen

I read transcript.txt, transcript_words.tsv, narration.txt, script.md and facts.md.

**Recomputation.** I recomputed every number with my own exact-rational scripts, independent of sim.py:
- the Eulerian distribution of R for n = 52
- Bayer–Diaconis Theorem 1 for k = 1…10, with the TV distance, mean, sd, gap, gap·2^k and gap/sd at each k
- the k = 7 decision set
- the closed-form top-card law after an a-shuffle, from the binomial packet boundaries

**Citations.** I checked every citation by web search: Trefethen PDF and Table 1, Aldous's Numdam record, the Bayer–Diaconis JSTOR copy, Diaconis 1996 on PubMed/PNAS, and Gelman & Rubin 1992 as a candidate source for fix 4.

```
EPISODE: 006 — "Seven Shuffles: When a Deck Suddenly Becomes Random"
IDEA: A riffled deck's chance depends only on how many rising sequences it has. Each riffle roughly halves the gap between that count and a random deck's, while the random deck's spread stays about 2, so the deck stays almost perfectly detectable for four riffles (even though its top card already looks random) and then falls off a cliff once the gap shrinks to about one spread, near seven riffles.
SCORES: Hook 8.5 · Clarity 8 · Visual 8 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.4 (8.35)   AFTER CEILING: 8.4 (lowest 8 + 2 = 10, not binding)
CAPS: none
FINAL: 8.4   PASS: no
```

## FACTS

| Claim | Verdict | Source / my check |
|---|---|---|
| GSR model: cut near the middle, cards drop from each half in proportion to its size (0:42–0:47) | Verified | Bayer & Diaconis 1992 p. 294; the model is credited to Gilbert (1955, Bell Labs memo, with Shannon) and Reeds (1981, unpublished). The on-screen citation matches |
| One riffle leaves 2 rising sequences, and a riffle at most doubles the count, so R ≤ 2^k (0:48–1:10) | Verified | The cut crosses each sequence once, so each sequence splits into at most two pieces. Exact P(R > 16 after 4) = 0 |
| "this deck has 14"; landing counts 20, 25, 28, 27, 29; "one simulated deck" (1:08, 3:21–3:33) | Verified (labelled simulated) | deck_pick seed. The typical count after 4 riffles is 14.10 ± 1.08 (exact) |
| Top card after 4 riffles: old top card "one time in 15" (0:30–0:34) | Verified (number) / imprecise (wording) | Exact P = 0.06490 = 1 in 15.4. But "**Only** the old top card stands out" is said over a chart where card 2 = 0.84 %, card 3 = 1.51 %, cards 50–52 = 1.51 %, 0.84 %, **0.24 %** visibly sit far under the 1-in-52 line. Those deficits are, by definition, the other half of the TV mass (0.0470 of 0.0475). See fix 3 |
| "Judge by it and you're right 52 % of the time"; ghost "top card 52.4 %" (0:34–0:41) | Verified | TV = 0.0475, so ½ + ½·TV = 52.37 % |
| 14-sequence deck "chance 3.5 × 10⁻⁶⁰"; perfect deck "1.2 × 10⁻⁶⁸" (1:31) | Verified | C(54,52)/16⁵² = 3.48e-60; 1/52! = 1.24e-68 |
| B–D proved that decks with the same count are equally likely (1:26–1:33) | Verified | B–D 1992 Theorem 1: P(π) = C(2^k + n − r, n)/2^{kn} |
| Perfect shuffle gives ≤ 16 "once in 2 million"; on screen "1 in 2.1 million" (1:11–1:16) | Verified | 4.666e-7 = 1 in 2,143,307 |
| "wrong once in 4 million games"; meter 99.99998 % (1:16–1:21) | Verified | ½·4.666e-7 = 1 in 4.29 M; accuracy 99.999977 % |
| Red area (purple above blue) = distance from random (1:40) | Verified | P_k depends on π only through r, so TV on permutations = TV on r = Σ max(0, p − u) |
| d after 5, 6, 7 = .92, .61, .33; d = 1.00 for 1–4; curve to 10 (1:49–1:57, 2:51) | Verified | exact 0.9237, 0.6135, 0.3341, 0.1672, 0.0854, 0.0429; matches B–D Table 1 |
| "catch 65 % of riffled decks, flag 32 % of perfect ones"; accuracy = ½(0.65) + ½(1 − 0.32) = ½ + ½d (1:57–2:13) | Verified | A = {r ≤ 25}: P(A) = 0.6500, U(A) = 0.3159; difference 0.3341 = d |
| gap 12.4 → 6.89 → 3.55 → 1.79 "roughly halves" (2:12–2:15) | Verified | exact 12.401, 6.895, 3.552, 1.790 (ratios 0.56, 0.52, 0.50) |
| Blue's spread (sd) "stays about 2" / "spread 2.1" (2:15–2:19) | Verified | √(53/12) = 2.1016 at every k |
| "5.9 spreads" at 4 riffles, "0.85 spreads" at 7 (2:21–2:26) | Verified | 12.401/2.1016 = 5.90; 1.790/2.1016 = 0.852 |
| "While the gap spans several spreads the distance stays near one; within one spread it halves every riffle" (2:19–2:27) | Verified | gap/sd 5.9, 3.3, 1.7, 0.85, 0.43 against d 1.00, 0.92, 0.61, 0.33, 0.17; two equal-sd normals give 2Φ(δ/2) − 1 ≈ the same values |
| gap·2^k ≈ 198 → 220 → 227 → 229 → 230 (2:27–2:32) | Verified | exact 198.4, 220.6, 227.3, 229.1, then 229.5, 229.6 → limit n(n+1)/12 = 229.67 |
| gap = spread ⇒ k ≈ 6.8, "just under 7"; dashed line at 6.77 (2:34–2:39) | Verified | log₂(229.67/2.1016) = 6.77 |
| 230 ~ n², spread ~ √n ⇒ k ≈ (3/2)log₂ n − 1.8 on screen (2:39–2:49) | Verified (screen) / imprecise (narration) | log₂√12 = 1.79 is correct. The narration "the cliff **sits near** three halves log base two of n" gives 8.55 at n = 52, which contradicts "just under seven" spoken 8 s earlier. "Grows like" is the true statement. See fix 2 |
| "Aldous proved that law" (2:49); Aldous, 1983 · Séminaire de Probabilités XVII on screen ≈ 3.4 s | Verified | Aldous, Sém. Probab. XVII, LNM 986, 243–297 (Numdam record). Aldous & Diaconis 1986 credit the (3/2)log₂ n asymptotics to Aldous (1983a); the Trefethens' abstract credits "Aldous, Bayer and Diaconis" |
| B–D computed the exact curve; for 52 cards 7 is the first below ½ (2:51–3:01) | Verified | B–D 1992, Ann. Appl. Probab. 2(2):294–313, Table 1: 0.614 at 6, 0.334 at 7 |
| Trefethen & Trefethen measured information: "no cliff; five or six shuffles do a reasonable job" (3:01–3:09) | Verified | Proc. R. Soc. Lond. A 456:2561–2568 (2000): "In the measure of information, evidently, the cut-off phenomenon is absent". Table 1: 27.27 bits remain after 4 shuffles, 7.95 after 5 and 2.07 after 6, out of 225.58 (3.5 % and 0.9 %). "Five or six" ≈ log₂ 52 = 5.7 |
| "Many Markov chains share this cliff" (3:10); Diaconis, 1996 · PNAS | Verified | PNAS 93(4):1659–1664, "The cutoff phenomenon in finite Markov chains" |
| "One statistic, like the top card, settles long before the whole chain"; grey "top card only (computed)" curve (3:14–3:20) | Verified (as computed demonstration) | My exact top-card TV is 0.708, 0.371, 0.124, 0.048, 0.020 for k = 1…5, which matches the plotted dots. The MCMC version of the trap is asserted, not sourced (fix 4) |
| Landing meter 96.2 → 80.7 → 66.7 → 58.4 → 54.3 → 52.1 %; "right only two times out of three"; "takes ten" (3:20–3:33) | Verified | ½(1 + d_k). 52.15 % at k = 10 is the first value ≤ 52.37 %. The "58.3 %" in the 3:31 sheet frame is the counter mid-tick; the settled value is 58.4 % |

There is no fabricated, misattributed or wrong number. The two imprecise wordings (0:30 "Only", 2:46 "sits near") do not trigger the cap-6 rule: the on-screen chart and the formula with −1.8 are both correct, and each spoken line has a true reading. Both still lose Clarity points.

## MECHANICS

```
runtime 3:34.8 · wpm 148 (speech) / 138 overall · max silence 1.84 s · leading 0.00 s / trailing 1.77 s · max static 3.23 s (3:06.7) · -14.0 LUFS / -2.1 dBTP · WER 1.0 % · 0 banned phrases
```

No mechanical cap triggers.

**Craft flags (no caps):**
- The sentence at 1:22.3 runs at 201 wpm.
- The longest run without a breath is 14.4 s (1:57.4–2:12).
- The busiest 20 s window (from 1:02) carries 7 distinct numbers.

**Transcript.**
- §4 scan finds no banned phrases, no "not just X", no question chains, no fake reveals.
- "that's the cliff" and "So pile decks…" are plain statements.
- Whisper heard "Aldus" and "Trafethen", which are both acceptable renderings of ALL-dus and truh-FETH-en.
- There are no dropped lines.

## Story read (cold)

**What works.**
- The hook is a real wager with a committed answer (0:10–0:13 "Pick 50, 75, or 100%").
- The naive detector (the top card) fails by a measured amount: 52.4 % against the truth of 99.99998 %, which arrives at 1:21.
- The landing re-runs the opening coin flip and ends on a line that reframes both detectors ("Fooling someone who counts sequences takes 10").
- That is Veritasium structure done properly.

**Where the tension sags.**
1. **The threshold is never motivated.** At 1:44 the question is "How many more riffles until it's below a half?", but nothing has yet said why ½ matters. The accuracy law (½ + ½d) arrives 25 s later and is never connected back. The connection is free and lovely: d = ½ is exactly the 75 % the viewer could have picked at 0:11. As cut, "seven" answers an arbitrary question.
2. **The payoff is thin on real-world stakes.** The data-science stake is one generic sentence at 0:13 ("Monte Carlo samplers…") and one at 3:12 ("samplers share the trap"). Both are asserted, with no real case. BAR §6 asks for a real data-science consequence.
3. **The mechanism beat (2:13–2:49) is shown, not explained, at one step.** The halving of the gap is read off data ("each step ≈ ÷2"). The viewer cannot re-derive *why* it halves. That is acceptable at 3 minutes, but it keeps Clarity below 9 together with items 1 above and fixes 2–3 below.

## FIXES (highest impact first)

1. **[2:11–2:13 and 1:44][Clarity + Hook] The ½ threshold is arbitrary on screen.**
   - Change: after "…and the difference is the red area." add: "So d below a half means right less than three times in four."
   - On screen: with `accuracy = ½ + ½d` still showing, swap d for a red ½ and let the line evaluate to `= 75%` for 2 s.
   - Optionally fade in a small grey "75 %" tick beside the d-plot's ½ line. Its referent is the hook's 75 % option.
   - Cost: +13 words. To hold the ≤ 500-word budget, cut "like these riffles" (0:17) and "instead" (3:03), and merge "You catch… You also flag…" into one sentence: "you catch sixty five percent of riffled decks and flag thirty two percent of perfect ones."
   - This makes "seven" the answer to the viewer's own 75 % pick.

2. **[2:44–2:49][Clarity] "The cliff sits near three halves log base two of n" gives 8.55 at n = 52.** That contradicts "just under seven" (2:37) and the on-screen −1.8.
   - Change: say "so the cliff grows like three halves log base two of n".
   - While `k ≈ (3/2)log₂ n − 1.8` holds, flash "n = 52: 8.6 − 1.8 = 6.8" in grey under it.

3. **[0:30–0:34][Clarity/correctness] "Only the old top card stands out" is spoken over bars that visibly sink far below 1-in-52.** Card 52 is at 0.24 %, card 2 at 0.84 %.
   - Change: "The old top card turns up too often: one time in fifteen."
   - Alternatively keep "stands out" and drop "Only".
   - The red marking on card 1's excess already matches this wording.

4. **[3:10–3:20, with 0:13–0:23][Hook/Payoff, BAR §6] Give the sampler trap one real, sourced case.**
   - Candidate (verified to exist): Gelman & Rubin (1992), "A single series from the Gibbs sampler provides a false sense of security", *Bayesian Statistics 4*. A single chain looked converged when it was not, which is why multiple-chain diagnostics exist.
   - Change: replace "and samplers share the trap" with "Gelman and Rubin caught a sampler in this trap: one chain looked settled long before it was".
   - On screen: "Gelman & Rubin, 1992 · Bayesian Statistics 4" for ≥ 3 s. Keep the grey top-card curve as the picture.
   - The producer must read the paper and state its example exactly in facts.md before using it.

5. **[3:01–3:09][Clarity/Motion] "No cliff" is asserted over a grey band, not shown.** Trefethen & Trefethen's Table 1 is real and small.
   - Change: draw the information remaining as a fraction of the deck's starting information, as a grey dashed curve on the same 0–10 riffle axis: 1, 0.77, 0.54, 0.31, 0.12, 0.035, 0.009, 0.002 for k = 0…7 (k = 0–7 from 225.58, 173.58, 121.58, 69.87, 27.27, 7.95, 2.07, 0.52 bits).
   - Label it "information left (Trefethen & Trefethen)".
   - It descends steadily from riffle 1 while the red curve sits flat at 1, which shows "no cliff" in one glance. Remove the 5–6 band.
   - This also breaks the 3.2 s static stretch at 3:06.7.

6. **[2:21–2:31][Visual] The insight frame is crowded.**
   - At 2:25 there are more than 12 prose words on screen: "gap", "(each step ≈ ÷2)", "7 riffles", "share of decks", "5.9 spreads", "0.85 spreads", "spread 2.1", "distance d", "rising sequences", "riffles" and the citation.
   - At 2:31 the purple "7 riffles" sits about 0.2 units under the new ×2^k row.
   - Change: on "that's the cliff" (2:27), dim "(each step ≈ ÷2)", the 5.9-spread hop ghost and "0.85 spreads" to 30 %. Move "7 riffles" to the chart's upper right, inside the axes, before the ×2^k row writes.

7. **[1:22.3–1:25.9][Audio] 201 wpm on "The top card can't see this: it lives in the order between cards."**
   - Change: put [pause 0.4] after "this" and render this sentence at speed 0.8.
   - The two counts (14 vs 26) flash on "this", so the pause also gives that flash room.

8. **[1:57.4–2:12][Audio] 14.4 s with no breath of ≥ 0.35 s through the accuracy derivation.**
   - Change: add [pause 0.5] after "perfect ones." (≈ 2:06.4), where the second number lands in the equation.

9. **[2:13–2:15][Clarity, optional, only if the budget allows after fix 1] Give the halving a cause in one clause.**
   - Change: "Four riffles act like one riffle into sixteen packets, so each riffle halves the gap."
   - Source: B–D §3, where k riffles equal one 2^k-shuffle and E[R] ≈ (n+1)/2 − n(n+1)/(12·2^k).
   - Skip this fix if it pushes the runtime past 3:40.

**REACHES 9 IF ALL FIXED:** yes, narrowly.
- Fixes 1–3 lift Clarity to 9: the threshold becomes the viewer's own 75 %, and both imprecise lines become exact.
- Fixes 1 and 4 lift Hook to 9: the ending resolves the opening options, and the payoff becomes a real case.
- Fixes 5–6 lift Visual and Motion to 9: shown rather than asserted, one focal point per frame.
- Fixes 7–8 lift Audio to 9.
- Result: 9 · 9 · 9 · 9 · 9 · 8.5 · 9 → 8.95 ≈ 9.0.
- No structural change is needed. The hook, the fail and the insight picture are all right.

**KEEP:**
1. The level view of rising sequences, with the cut-crosses-each-level-once argument and the ≤ 2^k ceiling (0:55–1:11).
2. The top-card detector against the whole-deck detector, with the 52.4 % ghost carried all the way to "Fooling someone who counts sequences takes 10" (0:34 → 3:33).
3. The accuracy law built from the zone areas (0.65 and 0.32 flying out of the histogram into `½ + ½d`) (1:57–2:13).
