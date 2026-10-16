# Round 2 review: substance and story (science editor)

Evidence: the existing `review/` pack (metrics.json 19:39 is newer than final.mp4 19:37). I read report.md, all 13 contact sheets, 13 full-resolution keyframes (0:11.8, 0:39.8, 1:07.6, 1:16.0, 1:27.5, 1:39.2, 2:00.5, 2:12.4, 2:44.7, 2:53.2, 3:01.8, 3:24.6, 3:51.7) and extra frames I pulled with ffmpeg at 0:05.2, 1:09.8, 2:15.6, 2:41.2, 2:46.5, 2:47.3 and 3:50.8. I also read script.md, narration.txt, facts.md, CHANGELOG.md, the transcript and word timings, and the cold-open and pmf code in scene.py. Every number was recomputed independently from exact rationals in my own script. That covered the Eulerian numbers, Bayer–Diaconis Theorem 1 for k = 1…10, means, sds, TV, the k = 6 decision set and the top-card law after k riffles (closed form over packet boundaries). Citations were checked by web search, and the Bayer–Diaconis PDF text was read directly for the Aldous attribution.

```
EPISODE: 006 — "Seven Shuffles: When a Deck Suddenly Becomes Random"
IDEA: A riffled deck's chance depends only on its number of rising sequences. Each riffle roughly halves the gap between that count and a random deck's, while the random deck's spread stays fixed. So four riffles leave the deck almost perfectly detectable (even though its top card already looks random), and the distance falls off a cliff once the gap shrinks to about one spread, near seven riffles.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8 · Motion 8.5 · Audio 8.5 · Concision 8 · Originality 8.5
WEIGHTED: 8.4   AFTER CEILING: 8.4  (lowest 8 + 2 = 10, not binding)
CAPS: none
FINAL: 8.4   PASS: no
```

## FACTS

| Claim | Verdict | Source / check |
|---|---|---|
| GSR model: binomial cut near the middle, cards drop in proportion to packet size (0:51) | Verified | Bayer & Diaconis 1992, p. 294; Gilbert/Shannon and Reeds credited there |
| Top card after 4 riffles: old top card "one time in 15" (0:36), "1 in 15" label | Verified | exact P = 6.49 % = 1 in 15.4 |
| "Only the old top card still turns up too often" (0:36) | Imprecise | 23 of 52 cards sit above 1/52 (max 1.985 % vs 1.923 %); card 1 carries 96 % of the excess. Red slivers at about cards 5 and 47 are visible in the 0:39.8 frame. Not capped, but it is a fix |
| Top-card guesser right "52 %", ghost "top card 52.4 %" (0:41) | Verified | TV = 0.0475 → 52.37 % |
| One riffle → 2 rising sequences; ≤ 2^k after k riffles; "this deck has 14" (0:57–1:17) | Verified | P(R > 16 after 4 riffles) = 0 exactly; mean 14.10, sd 1.08; the deck is labeled simulated |
| Perfect shuffle averages 26.5; ≤ 16 "once in 2 million"; on screen "1 in 2.1 million" (1:17) | Verified | (n+1)/2; P = 4.666e-7 = 1 in 2,143,307 |
| "Wrong about once in 4 million games"; meter 99.99998 % (1:25) | Verified | ½ · 4.666e-7 = 1 in 4.29 M |
| Same count → equally likely (Bayer & Diaconis); "chance 3.5 × 10⁻⁶⁰", "1.2 × 10⁻⁶⁸" (1:35–1:42) | Verified | Thm 1: C(54,52)/2^208 = 3.48e-60; 1/52! = 1.24e-68 |
| Red area (purple above blue) = distance; "Here it's one" (1:48–1:53) | Verified | r is sufficient, so TV of the r-laws = TV of the deck = 1 − 4.7e-7 |
| d = 0.92, 0.61, 0.33 after 5, 6, 7 (1:58–2:17); 0.17 after 8 | Verified | exact 0.9237, 0.6135, 0.3341, 0.1672 = B&D Table 1 |
| k = 6: catch 78 % of riffled, flag 17 % of perfect; accuracy = ½ + ½ d (2:03–2:15) | Verified | A = {r ≤ 24}: P(A) = 0.7824, U(A) = 0.1688; ½ + ½ · 0.6135 = 80.7 % |
| Gap row 12.4 → 6.89 → 3.55 → 1.79, "roughly halved" (2:18) | Verified | 12.401, 6.895, 3.552, 1.790 (ratios 0.56, 0.52, 0.50) |
| Purple spread settles to blue's, "about two"; "spread 2.1" (2:22) | Verified | sd 1.08 → 2.08; √(53/12) = 2.102 |
| Gap × 2^k ≈ 198 → 220 → 227 → 229 → 230 (2:36) | Verified | 198.4, 220.6, 227.3, 229.1 → 52·53/12 = 229.67 |
| 2^k ≈ 230/2.1 ≈ 110 → k ≈ 6.8, "just under seven" (2:40) | Verified | 109.5; log₂ = 6.78 (exact sd: 6.77) |
| Gap ∼ n², spread ∼ √n → cliff near (3/2) log₂ n; k ≈ (3/2) log₂ n − 1.8 tagged as heuristic (2:47–2:58) | Verified | gap ≈ n(n+1)/(12·2^k); the −1.79 = log₂√12 is tagged "(gap = spread rule)" |
| "Aldous, then Bayer and Diaconis, proved it" (2:58) | Verified | B&D 1992 p. 295: "A partial version of Theorem 2 has been proved by very different arguments in Aldous (1983)"; Aldous, Sém. Probab. XVII, LNM 986, 243–297 (numdam) |
| 7 riffles = first count with d < ½ (3:03) | Verified | 0.614 → 0.334 |
| Trefethen & Trefethen 2000, Proc. R. Soc. A: information measure, "no cliff, five or six shuffles do a reasonable job" (3:09) | Verified | the preprint says "there is no cutoff", "~log₂ n … for n = 52, 5 shuffles"; Science News (2003) says "five … reasonable … six … practically certain" |
| "Many Markov chains show the same cliff" (3:19) | Verified | Diaconis 1996, PNAS 93(4):1659–1664 |
| Top-card-only distance curve 0.71, 0.37, 0.12, 0.05 (3:26) | Verified | recomputed 0.708, 0.371, 0.124, 0.0475 |
| Landing meter 96.2, 80.7, 66.7, 58.4, 54.3, 52.1 %; "two times in three"; "takes ten" (3:33–3:49) | Verified | ½(1 + TV_k); after 10 riffles 52.15 % ≤ 52.37 % (after 9 it is 54.3 %) |
| "Card rooms need to know how many riffles make this a coin flip" (0:15) | Unverifiable (motivation) | no source on screen; not a statistic, so not capped |

No wrong or fabricated claims. One line is imprecise ("only").

## MECHANICS
runtime 3:51.7 · 156 wpm (speech) · max silence 1.99 s (planned prediction hold at 1:56) · max static 3.1 s (2:59.5) · −14.0 LUFS / −1.9 dBTP · lead 0.00 s / trail 1.89 s · WER 2.3 % · 0 banned phrases. My own search of the transcript found no §4 patterns either: there are no question chains (the opener is one question plus "Pick …") and no "it turns out".

## Transcript and story notes
- **Hook.** The first frame is the sorted deck. The commit ("Pick fifty, seventy five, or a hundred percent") comes at 0:10–0:13, with the "?" hopping across the ticks and a 2.0 s hold. The answer is a likely-wrong 100 %. Tension rises as the top card says 52 % ("Four riffles look like plenty"), and then the whole deck says 99.99998 % at 1:29. A second prediction ("below a half?") is held at 1:56. The landing returns to the meter. This is the episode's strongest element.
- **Hook weakness.** There is only ever one deck in the cold open (scene.py cold open). The "tails: perfect shuffle" tag fades in while riffles 3–4 are still animating (frame 0:05.2), so the viewer cannot tell whether the bars on screen are the heads deck or the tails deck. "From the deck alone, how often could you tell which?" is asked over a deck the viewer cannot compare with anything.
- **Density.** 1:35–2:58 packs about ten steps into 83 s: theorem, piling, red area = d, prediction, accuracy formula, gap row, spread, cliff rule, ×2^k row, 2^k ≈ 110, then a second, symbolic derivation of the same location. The numbers are all right, but a first-time viewer will not re-derive this after one watch, and that is the gap to Clarity 9.
- **Asserted step.** "Every riffle can split each level in two" (1:08) is the doubling that drives the whole episode, and it is only asserted. The reason (the cut crosses each rising sequence at most once) is never shown.
- **Audio.** "runs of consecutive cards, read left to right" is heard as "red left to right" (transcript 1:02.5–1:05.5). In this episode red means "what gives the deck away", and nothing is red at that moment.

## FIXES (highest impact first)
1. **[1:35–2:58][Clarity/Concision]** The cliff location is derived twice: numerically (×2^k row → 230/2.1 → 110 → k ≈ 6.8, 2:36–2:47) and again symbolically after a chart-clearing crossfade (2:47–2:58). Merge them into one chain. Build `2^k ≈ 230/2.1` from the row, then transform 230 → `52·53/12` → `n(n+1)/12` and 2.1 → `√(53/12)` → `√((n+1)/12)` in place, landing on `k ≈ (3/2) log₂ n − 1.8 = 6.8 for n = 52`. Narration: "Gap times two to the k levels off near two hundred thirty, that is fifty two times fifty three over twelve, about n squared. The spread is root of fifty three over twelve, about root n. They meet near three halves log two n: six point eight riffles." This cuts about 6 s and one re-layout and gives the insight a single line of argument.
2. **[0:00–0:13][Hook/Clarity]** Show both coin outcomes. After the four riffles, slide the riffled deck left and deal a perfectly shuffled deck on the right, with the tags under each deck rather than across the top. Better still, use the same two decks that return side by side in level view at 1:19 (14 vs 26 levels), so the 1:19–1:29 reveal is literally the cold-open picture answered. The "tails" tag must not appear while riffles are animating (frame 0:05.2).
3. **[1:06–1:15][Clarity/Visual]** The doubling is asserted, and the level view is a thin strip (1:07.6 frame: the deck sits in y ≈ 590–710 px with the top 55 % of the frame empty, about 25 px per level). Double the level step for k ≤ 3 so the deck fills y ≈ 300–700 px. On riffle 2, draw the cut as a vertical dashed line through the source deck and tint each old level's left-packet and right-packet pieces differently before they interleave. Narration: "The cut crosses each level once, so a riffle can at most split it in two."
4. **[2:44–2:48][Motion/Visual]** `⇒ k ≈ 6.8` is at full opacity for only about 1.3 s (written by 2:46.0, already dimming at 2:47.3); §5 asks ≥ 2 s + 0.4 s/term ≈ 3 s. At 2:47.3, "distance d" morphs into "total variation distance, d" letter by letter over the half-faded histogram, which leaves garbled glyphs. Add `[pause 0.8]` after "just under seven", hold the line ≥ 3 s, finish fading the histogram before the d-plot grows, and FadeTransform the axis title as one unit. If fix 1 is applied, this transition disappears.
5. **[2:40.5–2:42][Visual/Motion]** In the copy-out frames, the copies sit on top of their sources (frame 2:41.2): "gap" over "gap:" reads "gapgap", 230 over 230 reads "2330", a loose "2.1" floats over "spread 2.1", and a partial "/?" is visible. Dim the source rows to 30 % first, then move each copy on a path arc that clears its source by ≥ 0.3 units before the target equation starts writing.
6. **[0:36–0:41][Clarity/correctness]** "Only the old top card still turns up too often" is literally false: 23 cards exceed 1/52, and red slivers at about cards 5 and 47 are visible in the 0:39.8 frame. Say "Only the old top card stands out: one time in fifteen", and color only card 1's excess red.
7. **[2:07–2:17][Visual]** The k = 6 frame (2:12.4) carries about 15 prose words plus a citation: gap row, accuracy equation, "chance", "say riffled", "say perfect", "6 riffles", "perfect", "distance d", axis titles. That is above the 12-word limit. Fade the gap row to 0 during the accuracy derivation (it returns at 2:18), and drop the "perfect" label while the zone labels are up.
8. **[1:59–2:17][Clarity]** During the slides, live values belong to non-integer riffle counts produced by clipped, renormalised interpolation (scene.py `rs_pmf` clips negative terms). Examples: bracket "11.4" at 1:59, "5.84" and dot "d = 0.86" at 2:01, "3.54" at 2:17. A viewer who pauses sees numbers that correspond to no deck. Hide the bracket label and dot value during each slide and write the integer-k value on arrival.
9. **[1:02–1:05][Audio]** "read left to right" is heard as "red". Change it to "runs of consecutive cards, reading left to right".
10. **[0:15–0:19][Hook]** "Card rooms need to know…" is an unsourced, generic stake. The episode's real payoff is MCMC, so lead with it: "Any simulation that mixes by random steps needs this number: stop early and it still remembers where it started." Then drop the card-room clause, which saves about 3 s.

**REACHES 9 IF ALL FIXED: yes, narrowly.** The structure is right and every number and citation checks out. What separates this from 9 is the density of the insight section and two moments where the explanation is asserted or visually ambiguous: the single-deck cold open and the doubling. Fixes 1–3 lift Clarity and Hook to 9. Fixes 4–7 lift Visual and Motion. If fix 1 is skipped, Concision stays at 8 and the episode tops out around 8.7.

**KEEP:**
- The coin-flip accuracy meter as the spine: commit at 0:10, top-card ghost at 52.4 %, 99.99998 % at 1:29, and the landing riffles 5–10 sliding to 52.1 % against the ghost ("Fooling someone who counts sequences that well takes ten"). It resolves the opening exactly.
- The areas-to-equation derivation at k = 6 (2:03–2:17): 0.78 and 0.17 fly out of the shaded zones into ½(0.78) + ½(1 − 0.17) → ½ + ½ d.
- The top-card-only vs whole-deck curves (3:26) as the honest MCMC consequence, plus the Trefethen "different yardstick" caveat.
