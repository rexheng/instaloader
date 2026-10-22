# Round 1 review: substance and story (science editor), independent pass

Evidence: the existing `review/` pack (metrics.json 00:01 is newer than final.mp4 23:59). I read report.md, all 13 contact sheets and 16 full-resolution keyframes (0:06.6, 0:47.9, 1:04.3, 1:12.1, 1:30.3, 1:37.0, 1:48.2, 2:09.6, 2:19.5, 2:35.7, 2:44.0, 2:56.3, 3:15.7, 3:32.6, 3:51.2, plus 2:41.8, 3:23.0, 3:43.6 and 3:44.4, which I extracted with ffmpeg). I also read script.md, narration.txt, the transcript, facts.md, sim.py and deck_pick.py.

I recomputed every number in my own exact-rational scripts:
- the Eulerian distribution of R for n = 52, and Bayer–Diaconis Theorem 1 for k = 1…10;
- the TV distances, means, sds and gaps, and the k = 6 decision set;
- the top-card law after k riffles, in closed form over the binomial packet boundaries.

I checked the citations by web search and read the Bayer–Diaconis text myself (JSTOR scan, Berkeley copy).

```
EPISODE: 006 — "Seven Shuffles: When a Deck Suddenly Becomes Random"
IDEA: A riffled deck's chance depends only on its count of rising sequences. Each riffle roughly halves the gap between that count and a random deck's, while the random deck's spread stays about 2. So the deck stays almost perfectly detectable for four riffles, even though its top card already looks random, and the distance falls off a cliff once the gap shrinks to about one spread, near seven riffles.
SCORES: Hook 8.5 · Clarity 8 · Visual 8 · Motion 8.5 · Audio 8.5 · Concision 7.5 · Originality 9
WEIGHTED: 8.3   AFTER CEILING: 8.3  (lowest 7.5 + 2 = 9.5, not binding)
CAPS: none
FINAL: 8.3   PASS: no
```

## FACTS

| Claim | Verdict | Source / check |
|---|---|---|
| GSR model: "cuts near the middle, then drops cards from each half in proportion to its size" (0:47) | Verified | Bayer & Diaconis 1992, p. 294: binomial cut; "cards drop from the left or right heaps with probability proportional to the number of cards in each heap"; model credited to Gilbert and Shannon (Gilbert 1955) and to Reeds (1981) |
| Top card after 4 riffles: "almost flat", old top card "one time in 15", label "1 in 15" (0:31–0:37) | Verified | exact P(card 1) = 6.49 % = 1 in 15.4. The rest of the histogram matches the plot: card 2 = 0.84 %, cards 51–52 = 0.84 % and 0.24 %, max other 1.985 %. Card 1 carries 96 % of the excess |
| "Judging by the top card, you'd be right 52 %"; ghost "top card 52.4 %" (0:38) | Verified | TV = 0.0475 → ½ + ½·TV = 52.37 % |
| One riffle leaves two rising sequences; a riffle at most doubles them; ≤ 2^k; "this deck has 14" (0:53–1:16) | Verified | The argument "the cut crosses each level once" is correct: each sequence is a prefix in one packet plus a suffix in the other. P(R > 16 after 4 riffles) = 0 exactly. The example deck is labelled simulated |
| Perfect shuffle "averages 26.5"; "16 or fewer once in 2 million"; "≤ 16: 1 in 2.1 million" (1:17) | Verified | (n+1)/2 = 26.5; P_U(R ≤ 16) = 4.666e-7 = 1 in 2,143,307 |
| "Wrong about once in 4 million games"; meter 99.99998 % (1:24–1:30) | Verified | ½ · 4.666e-7 = 1 in 4.29 M; accuracy 99.999977 % |
| Same count → equally likely (Bayer & Diaconis); "chance 3.5 × 10⁻⁶⁰", "1.2 × 10⁻⁶⁸" (1:35–1:41) | Verified | Thm 1: C(2^m + n − r, n)/2^{mn} = C(54,52)/2^208 = 3.479e-60; 1/52! = 1.240e-68 |
| Red area (purple above blue) = distance from random; "right now it's one" (1:48–1:53) | Verified | r is sufficient, so the TV of the r-laws equals the TV of the deck = 1 − 4.7e-7 |
| d = .92, .61, .33 after 5, 6, 7; .17 after 8 (1:58–2:35) | Verified | exact 0.9237, 0.6135, 0.3341, 0.1672 = B&D Table 1 |
| k = 6: "catch 78 % … flag 17 %"; accuracy = ½ + ½ × difference; on screen ½(0.78) + ½(1 − 0.17) (2:03–2:16) | Verified | A = {r ≤ 24}: P(A) = 0.7824, U(A) = 0.1688, difference = 0.6135 = d. The spoken apposition is ambiguous (see fix 3) |
| Gap 12.4 → 6.89 → 3.55 → 1.79, "roughly halved"; spread "about two", "spread 2.1" (2:19–2:26) | Verified | exact gaps 12.401, 6.895, 3.552, 1.790; sd_U = √(53/12) = 2.1016; purple sd 1.08 → 2.08. B&D p. 296 also says d "begins to decrease sharply by factors of 2 each time" |
| "5.9 spreads", "0.85 spreads"; once the gap is about one spread "the distance halves too" (2:27–2:36) | Verified | gap/sd = 5.90, 3.28, 1.69, 0.852, 0.427; d = 1, .92, .61, .33, .17, .085. A normal mean shift δ gives TV = 2Φ(δ/2) − 1, which is linear in small δ, so d halves as the gap halves |
| "Gap × 2^k levels off near 230"; row 198 → 220 → 227 → 229 → 230 (2:37) | Verified | exact 198.4, 220.6, 227.3, 229.1 → n(n+1)/12 = 229.67 |
| "2^k about 110: just under seven"; k ≈ 6.8 (2:43–2:47) | Verified | 229.67/2.1016 = 109.3; log₂ = 6.77 |
| Gap ∼ n², spread ∼ √n, "cliff near three halves log base two of n"; k ≈ (3/2)log₂n − 1.8 "(gap = spread rule)" (2:49–3:01) | Verified | gap ≈ n(n+1)/(12·2^k), sd = √((n+1)/12) → k ≈ (3/2)log₂n − log₂√12 = (3/2)log₂n − 1.79. This heuristic is the exact mechanism behind B&D Theorem 2: δ/2 = 2^{−c}/(4√3) reproduces their limit 1 − 2Φ(−2^{−c}/(4√3)). The −1.8 is correctly tagged as the episode's own rule |
| "Aldous, then Bayer and Diaconis, proved it: for 52 cards, seven riffles is the first count that brings the distance below a half" (3:01–3:11) | **Imprecise attribution** | 7 is from B&D's exact Table 1 (0.614 → 0.334). Aldous 1983 (Sém. Probab. XVII, LNM 986, 243–297) proved only an asymptotic result; B&D p. 296: "A partial version of Theorem 2 has been proved by very different arguments in Aldous (1983)". Aldous did not prove the 52-card statement that follows the colon. Not a fabrication, and Aldous does deserve credit for the (3/2)log₂n asymptotics (the Trefethens' abstract says "theorem of Aldous, Bayer and Diaconis"). Fix 4 |
| Trefethen & Trefethen 2000, Proc. R. Soc. A: "measured information instead: no cliff, and five or six shuffles do a reasonable job" (3:11–3:22) | Verified | 456:2561–2568. Abstract: with an entropy measure "there is no cutoff"; about log₂n (5.7 for n = 52) shuffles bring the information close to 0. Science News (Peterson): "five shuffles would do a reasonable job … six would make it practically certain" |
| "Many Markov chains share this cliff" — Diaconis 1996 · PNAS (3:22) | Verified | PNAS 93(4):1659–1664. Cutoffs are proven for shuffles and the Ehrenfest urn; the drunkard's walk has none, so "many" is right |
| Top-card-only distance curve 0.71, 0.37, 0.12, 0.05 … vs whole deck (3:27–3:33) | Verified | exact top-card TV for k = 1…4: 0.708, 0.371, 0.124, 0.048. It is the episode's own computation, but it sits next to the "Diaconis, 1996" citation (fix 8) |
| Landing: "two times in three" after 7; meter 96.2 → 80.7 → 66.7 → 58.4 → 54.3 → 52.1 %; "fooling someone who counts sequences that well takes ten" (3:40–3:52) | Verified | ½(1 + d_k): 96.19, 80.68, 66.70, 58.36, 54.27, 52.15 %. 52.15 % at k = 10 is the first value ≤ 52.37 % |

No wrong numbers and no fabricated sources. This is unusually clean work.

## MECHANICS

runtime 3:53.9 · 155 wpm on speech time (573 words) · max internal silence 1.98 s (0:13.2 planned commit hold; 1:56.9 planned prediction hold) · leading 0.00 s / trailing 1.89 s · max static 3.23 s (2:41.6) · −14.0 LUFS / −1.9 dBTP · 0 black frames · WER 1.4 %. The only transcript mismatches are homophones ("too/two", "blue's/blues") and "Aldous" heard as "all does", which is the correct pronunciation. No mechanical cap triggers, but the runtime is 6 s from the 4:00 cap and 54 s over the §6 template.

## TRANSCRIPT / SLOP SCAN

- No §4 banned phrases.
- No question chains: the only questions are 0:06 (followed by "Pick fifty…", which is an instruction) and 1:54.
- No "it turns out", no "not just X", no fake-reveal colons.
- "Four riffles look like plenty" (0:42) is the single dry line, and it works.
- Hook: two decks are on screen from frame 1, the question comes at 0:06–0:10, and the viewer commits at 0:10–0:15 (the "?" hops 50 → 75 → 100, then a 2.0 s hold). That lands inside the 15 s rule and just misses the 12 s "9" anchor.

## WHAT IS GENUINELY STRONG

The structure is the best part of the episode.
- The naive detector (the top card) "succeeds" in calling the deck random. That success is the failure, and its size is measured: 52.4 % on a live meter.
- The level view at 1:02–1:16 turns "rising sequences" from a definition into a picture. Bar height becomes sequence index, the cut line crosses each level once, and the ceiling ≤ 2^k rises with each riffle. A first-time viewer can see why the count at most doubles.
- The gap-vs-spread mechanism (2:19–2:36, with spread-long hops along the gap) is not hand-waving. It is the actual asymptotic mechanism of Bayer–Diaconis Theorem 2, which I checked.
- The landing replays the cold-open meter and resolves it exactly: 99.99998 → 66.7 → 52.1 %, against the 52.4 % ghost. The last line, "Four riffles fool someone watching the top card. Fooling someone who counts sequences that well takes ten", reframes the opening.

## WHY IT IS NOT A 9 (evidence)

1. **The insight section is overloaded, and the prediction payoff is interrupted.** From 1:35 to 3:01 (86 s) the viewer gets:
   - the B–D theorem;
   - the pile-up into histograms;
   - TV as the red area;
   - a prediction;
   - three d values;
   - an accuracy derivation (two equation lines);
   - the halving gap;
   - the spread;
   - hops;
   - a ×2^k row;
   - `gap ≈ 230/2^k = 2.1` → `2^k ≈ 110` → `k ≈ 6.8`;
   - `52·53/12 / √(53/12)`, then the n-generalisation, then `(3/2)log₂n − 1.8`.

   The prediction "How many more riffles to bring it below a half?" (1:54) is answered at 1:59 (.92) and 2:02 (.61). Then a 14 s accuracy detour (2:03–2:16) intervenes before the decisive ".33" at 2:17. The tension peak is spent on bookkeeping. The 2:36–3:01 algebra stacks three equation states in about 25 s (2:43, 2:47, 2:51, 2:55, 2:59 per the contact sheets). That breaks §5 "one new equation per 5 s" in spirit, and nobody re-derives (3/2)log₂n after one watch. This drives the Clarity 8 and the Concision 7.5.
2. **Concision.** At 3:54 the runtime is near the ceiling. About 10 % is compressible without losing the idea: the 230 → 110 → 6.8 → n-scaling chain (2:37–3:01) and the narrated walk-through of the accuracy formula. Each of those beats is correct but carries a second derivation.
3. **Ambiguous sentence at 2:13:** "Accuracy is a half plus half the difference: the red area." Heard aloud, the appositive can attach to "accuracy". The on-screen line ends at `½ + ½ d`, but the spoken sentence invites the wrong reading.
4. **Attribution at 3:01** (see FACTS): the colon pins the 52-card "seven" on Aldous.
5. **Jargon on screen:**
   - "one simulated deck (GSR model)" (1:17, 1:19–1:31, 3:35–3:53): "GSR" is never expanded or spoken.
   - "spread" is never said to be the standard deviation. The bracket goes from the centre to 1 sd (kf 2:35.7), so a viewer can easily read "spread 2.1" as the full width.
6. **Word load at 1:19–1:35** (kf 1:30.3) is about 20 prose words on screen at once, against the §5 limit of 12:
   - "4 riffles", "14 rising sequences", "perfect shuffle", "26 average 26.5";
   - "one simulated deck (GSR model)", "≤ 16: 1 in 2.1 million";
   - "coin flip", "always right", "top card 52.4 %", and the Gilbert/Reeds citation.

   On top of that, the faint yellow traces across the 26-level deck (kf 1:37.0) form a hatch with no focal point.
7. **Citation crossfade overlap at 3:23.0** (extracted frame): "Diaconis, 1996 · PNAS" fades in over "Trefethen & Trefethen, 2000 · Proc. R. Soc. A" in the same spot, and for a few frames the two read as garbled overlapping text. Transitional, so not capped, but visible.
8. **Stakes line (0:15–0:24):** "Any simulation that mixes by random steps faces this question" is abstract at second 15. The viewer has no picture of such a simulation until 3:22, and the visual is only a dashed diagonal over the deck (0:23). The stakes are correct but weak next to a 3b1b-style "why you should care".

## FIXES (highest impact first)

1. **[1:54–2:17][Hook/Clarity] The accuracy detour splits the prediction from its answer.**
   - Move the accuracy derivation to right after "Right now it's one" (about 1:53), done at k = 4, where it is trivial (P(A) = 1, U(A) ≈ 0 → accuracy ½ + ½·1). Or generalise it once with the zone shading, and tie it to the meter that the viewer already knows.
   - Then ask "How many more riffles to bring it below a half?", hold 1.5 s, and run 5 → 6 → 7 contiguously (".92 … .61 … .33") with no interruption, so the d = ½ line is crossed at the climax.
   - This restores the tension arc and removes the need for the second explanation at 2:03–2:16.
2. **[2:37–3:01][Concision/Clarity] Too many equation states.**
   - Collapse the 230 → 110 → 6.8 → n-scaling chain into one transform. Keep the row "gap × 2^k ≈ 230" and go straight to the dashed line at k ≈ 6.8 with one sentence: "Halve 230 until it's about 2: that takes just under seven."
   - Replace the `52·53/12 / √(53/12)` intermediate with a single `TransformMatchingTex` to `2^k ≈ n²/√n = n^{3/2}` → `k ≈ (3/2) log₂ n`, and keep "(gap = spread rule)".
   - Target: cut 10–12 s, so the runtime is about 3:40 or less, and no more than one new equation per 5 s.
3. **[2:13][Clarity] Fix the ambiguous apposition.** Change the narration to: "Accuracy is a half, plus half the difference — and the difference is the red area." Flash the red area exactly on "red area" (it currently flashes on "a half plus").
4. **[3:01–3:11][Clarity/correctness] Fix the attribution.** Change to: "Aldous proved the cliff sits near three halves log n. Bayer and Diaconis computed it exactly: for fifty-two cards, seven riffles is the first count below a half." Show the Aldous citation on the first clause and B&D on the second. The current line credits Aldous with the 52-card table, which B&D themselves call only a "partial version" of their Theorem 2.
5. **[1:17–1:31, 3:35–3:53][Visual/Clarity] Undefined "GSR" label.** Replace "one simulated deck (GSR model)" with "one simulated deck" and move "Gilbert–Shannon–Reeds model" into the citation line at 0:49 (which also restores Shannon, credited by B&D alongside Gilbert).
6. **[2:22–2:26][Clarity] "Spread" is undefined.** Label the bracket "spread (1 sd) 2.1", or say "…settled to blue's: one standard deviation, about two".
7. **[1:19–1:35][Visual] Word load and trace clutter (kf 1:30.3, 1:37.0).**
   - Drop "average 26.5" once it has been spoken (keep 26).
   - Dim the citation and the "top card 52.4 %" ghost to 25 % during this beat.
   - Fade the level traces on the perfect deck to 15 % opacity and keep only the caps, so the "14 vs 26 height" comparison is the single focal point.
   - Target: no more than 12 prose words on screen.
8. **[3:22–3:33][Clarity/sourcing] The top-card curve can be misread as Diaconis 1996's data.** Add a grey "computed (GSR model)" tag beside "top card only", so it is not read as coming from the citation next to it.
9. **[3:22.8–3:23.4][Visual] Crossfading citations overlap.** FadeOut "Trefethen & Trefethen, 2000" fully (0.4 s) before "Diaconis, 1996 · PNAS" fades in, or place the new citation one line higher.
10. **[0:15–0:24][Hook] Abstract stakes line.** Make it concrete in the same time. For example: "A computer that explores possibilities by random steps (a Monte Carlo sampler) has this problem too: stop too early and its answer still remembers where it started." Over it, show the sorted deck's dashed profile ghosting through the riffled deck, as now.

**REACHES 9 IF ALL FIXED: yes.**
- The facts are clean and the narrative skeleton is right (misconception → measured naive success-as-failure → one picture → mechanism → honest limit with Trefethen → MCMC consequence → landing that reframes the opening).
- What holds it below 9 is pacing and density in the insight section, not structure. Fixes 1–2 are the big ones: they should lift Clarity to 9, Concision to 8.5–9 and Hook to 9. Fixes 3–9 clear the remaining Clarity and Visual nitpicks.
- Without fixes 1 and 2, polish alone will not get past about 8.6.

**KEEP**
1. The top-card "success" as the naive failure, measured on the live meter (52.4 % ghost), and the landing that drives the needle down to 52.1 % against that ghost on "takes ten".
2. The level view with the cut line crossing each level once and the rising ≤ 2^k ceiling (1:02–1:16), which is the clearest picture of rising sequences I have seen.
3. The gap-vs-spread hops (5.9 spreads → 0.85 spreads) explaining the cliff, plus the honest Trefethen "this yardstick" caveat.
