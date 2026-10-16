# Episode 006, round 1, craft critic (visual design / motion / sync emphasis)

Evidence used: `review/` pack (metrics.json 00:01 is newer than final.mp4 23:59, so I reused it): report.md, all 13 contact sheets, keyframes kf_01, kf_04, kf_08, kf_10, kf_12, kf_15, kf_19, kf_23, kf_27, kf_30, kf_40 at full resolution, plus my own frames from ffmpeg at 0:45.5, 0:47.0, 1:10.8, 1:13.0, 1:43.0, 2:07.0, 2:16.0–2:18.2 (cropped), 2:19.0, 2:39.0, 2:41.0, 2:46.5, 3:23.0, 3:41.0 and 3:51.0. I also read transcript.txt and transcript_words.tsv, narration.txt, script.md, facts.md and the relevant parts of scene.py. I recomputed every number independently: Eulerian numbers / 52! for the uniform count, B-D Theorem 1 for the riffled pmf, and a 200k-deck Monte Carlo for the top card.

```
EPISODE: 006 — "Seven Shuffles: When a Deck Suddenly Becomes Random"
IDEA: A riffled deck's chance depends only on its number of rising sequences; each riffle halves the gap between that count and a random deck's while the random spread stays fixed, so the deck is near-perfectly detectable for four riffles and then falls off a cliff around seven, even though the top card already looks random after four.
SCORES: Hook 8.5 · Clarity 8 · Visual 8 · Motion 8 · Audio 8 · Concision 7 · Originality 8.5
WEIGHTED: 8.0 (8.03)   AFTER CEILING: 8.0 (ceiling = 7 + 2 = 9, not binding)
CAPS: none
FINAL: 8.0   PASS: no
```

## FACTS
| Claim | Verdict | Source / my check |
|---|---|---|
| GSR model: binomial cut, drop proportional to packet size | Verified | Bayer & Diaconis 1992, p. 294 |
| One riffle leaves two rising sequences; R ≤ 2^k after k riffles | Verified | B-D §2–3; cut-crosses-once argument holds |
| Example deck R = 2, 4, 8, 14 (labelled "one simulated deck (GSR model)") | Verified (seeded, labelled simulated) | decks.json |
| Top card after 4 riffles: card 1 is on top 1 time in 15 | Verified | my MC 0.0650 (1 in 15.4) |
| Judging by the top card gives 52.4 % | Verified | TV 0.0475 → 52.4 % (MC agrees within noise) |
| Uniform mean R = 26.5; P(R ≤ 16) = 1 in 2.1 million | Verified | Eulerian: 4.666e-7 = 1 in 2,143,307 |
| Wrong about once in 4 million games; 99.99998 % | Verified | ½·4.666e-7 = 1 in 4.29 M |
| Same count → same chance; 3.5×10⁻⁶⁰ and 1.2×10⁻⁶⁸ | Verified | C(54,52)/2^208 = 3.479e-60; 1/52! = 1.240e-68 |
| d = 1.00 (k ≤ 4), 0.92, 0.61, 0.33, 0.17 | Verified | exact: 0.9237, 0.6135, 0.3341, 0.1672; B-D Table 1 |
| At k = 6: catch 78 %, flag 17 %; accuracy = ½ + ½ d | Verified | P(r ≤ 24) = 0.7824, U(r ≤ 24) = 0.1688 |
| Gap 12.4 → 6.89 → 3.55 → 1.79; spread → 2.1 | Verified | exact means 14.099, 19.605, 22.948, 24.710; sd at k=4: 1.08, at k=7: 2.08, uniform 2.10 |
| gap × 2^k → 230 = 52·53/12; 2^k ≈ 110 → k ≈ 6.8 | Verified (heuristic, tagged "(gap = spread rule)") | log₂(229.67/2.1016) = 6.77 |
| Cliff near (3/2) log₂ n | Verified | B-D abstract; Aldous 1983 |
| "Aldous, then Bayer and Diaconis, proved it: for 52 cards seven riffles is the first count…" | Verified, but the wording blurs credit | The 52-card exact count is Bayer–Diaconis's; Aldous gave the asymptotics (fix 12) |
| Trefethen & Trefethen 2000: with an information measure there is no cliff; 5–6 shuffles do a reasonable job | Verified (abstract and press paraphrase) | Proc. R. Soc. A 456:2561 |
| Many Markov chains show a cutoff | Verified | Diaconis 1996, PNAS 93:1659 |
| Landing: 66.7 % after 7 riffles; ten riffles to get under 52.4 % (54.3 % after 9, 52.1 % after 10) | Verified | ½(1 + d) |
| Gilbert 1955 · Reeds 1981 | Verified as credited by B-D; the on-screen citation has no venue | fix 12 |

No wrong, fabricated or misattributed claims, so no fact caps.

## MECHANICS
runtime 3:53.9 · 155 wpm on speech time (573 words) · max internal silence 1.98 s (0:13.2, the planned prediction hold) · leading 0.00 s / trailing 1.89 s · max static 3.23 s (2:41.6) · −14.0 LUFS / −1.9 dBTP · no black frames · WER 1.4 % · banned phrases 0 · layout audit 0 issues. **No mechanical caps.** Runtime sits 6 s inside the 4:00 limit, which matters for Concision.

## Transcript and sync
- No §4 banned phrases or patterns. There is one honest question and then a planned 1.5 s hold, at 1:54.5–1:58.8.
- Hook: the prediction is asked at 0:06.7 ("how often could you tell which?") and the options at 0:10.2–0:15.1, with the "?" hopping 50 → 75 → 100 on each number (sheet 1). The commit lands at about 0:13, just past the 0:12 anchor.
- Deictic references land within ±2 s throughout. "Blue is a perfect shuffle. Purple is 4 riffles" (1:44.9–1:47.8): the blue bell is grown by 1:47. "The red area" at 1:48.4: red fill at 1:49. "Right now it's one" at 1:53: the d = 1.00 dot. "point nine two" at 1:59–2:01. "Guess riffled wherever purple is higher" at 2:03.6: the zones appear by 2:05. "spread … about two" at 2:23–2:26: "spread 2.1" appears at 2:25. "That's the cliff" at 2:36: the curve draws through the dots at 2:37. "like the top card" at 3:27: the grey top-card curve at 3:29.
- Prosody: "Gap times two to the k levels off near 230" is heard as "two to the K levels, off near 230" (2:36.3–2:43.9). "Levels" has been a noun in this episode since 1:01, so the line is a garden path. Separately, "the distance halves too" is heard as "halves two" (2:34.5), in a sentence surrounded by numbers.
- "Aldous" transcribed as "all does" matches the intended ALL-dus pronunciation, so this is not a defect.

## Contact sheets (flipbook read)
- 0:00–0:15: strong concrete open. Two decks as bar profiles, the left one riffles (0:03–0:05) and the right one jumps to random (0:05–0:07), then the meter and the "?" appear. In kf_01 the frame's bottom 40 % is empty until 0:09.
- 0:13–0:23 (stakes): "Any simulation that mixes by random steps faces this question" plays over a picture that carries no new information for about 8 s (sheets 1–2, frames 0:13–0:21 look identical). The only change is a grey dashed diagonal at 0:22.
- 0:24–0:44 (naive build): good. The deck shrinks to the corner, its top card's copy flies into its bar (kf_04, the white bar at card 11), "1 in 15" turns red, and the meter fills to 52.4 %. Each motion encodes origin.
- 0:45–1:34 (fail and rising sequences): the best stretch. The riffle visibly interleaves two packets (0:49–0:55), yellow traces join the two sequences, the level view drops bars to their sequence index, and a cut line rings each level. The ceilings ≤ 4, ≤ 8, ≤ 16 match the counts. The two decks return side by side with the 16-line (kf_10), and the needle jumps to 99.99998 % (kf_12). Weak point: at 1:11 the "2"/"4" and "≤ 2² = 4" glyphs morph through garbled shapes, and at 1:13 skewed trace lines cross the whole deck mid-riffle. That moment is informative but busy.
- 1:35–1:48 (one chart): the equal-chance demo (1:39–1:41) works. Then "pile each deck onto its count" (1:42–1:47) squeezes each deck into a square labelled "1 deck", which sits at about 0.03 on a "chance" axis (kf_15). That y-position means nothing, and the jump from one deck to the full distribution happens with no narration.
- 1:49–2:17 (insight): the red area, the gap bracket and the d-plot are coherent. Slides to 5 and 6 riffles, zones, purple and blue areas flying into `½(0.78) + ½(1 − 0.17)` (2:07–2:13), and the second line at 2:15. Then the payoff of the derivation, `accuracy = ½ + ½ d`, is never held. My frames at 2:16.0, 2:17.0, 2:17.6 and 2:18.2 show it forming at full opacity at about 2:17.4 and already dimmed to 30 % by 2:18.2. scene.py dims it inside the same `slide_to(7)` call (`e3.animate.set_opacity(0.3)`), and it fades out at 2:19.6. The rule requires ≥ 2 s + 0.4 s × 5 terms = 4 s.
- 2:19–2:37 (mechanism): the spread hops laid along the gap (5.9 spreads at 4 riffles, 0.85 at 7) are a lovely, original picture. But it is the second replay of 4 → 7 riffles in 20 s.
- 2:37–3:01 (equation): built in place from the gap row, 230 and the spread label, which is good. But it runs through four equation states in about 20 s. `gap ≈ 230/2^k = 2.1` uses "=" to mean "set equal to the spread", which reads as a false identity (kf_27). While the narration says "the gap meets the spread" (2:42–2:48), the "spread 2.1" label in the chart is dimmed to near-invisibility (frame 2:46.5). The frame then carries six groups: two rows, the chart, the d-plot, the equation and a citation.
- 3:01–3:32 (payoff): a clean full-width distance curve with cited values and an honest "information yardstick" note. At 3:23.0 the Diaconis 1996 and Trefethen 2000 citations crossfade in the same spot, giving about 0.8 s of overlapping garbled text (`FadeOut(tref), FadeIn(dia)` run together). The "top card only" against "whole deck" curves (3:29) make a strong closing image.
- 3:32–3:53 (landing): the opening deck returns in level view with the meter at 99.99998 %. Riffles 5–10 take the meter down to 52.1 %, landing next to the "top card 52.4 %" ghost. This is the third showing of the 5 → 6 → 7 progression. The counters morph through garbled glyphs at 3:41 ("¿ riffles", "2ɕ", "9▒%") and at 3:51 ("ʝ0 riffles", "2ꞩ"). The last line does reframe the opening well.

## Keyframes against §5
- Safe area and spacing: no violations found. The rightmost text, "∼ n²" and the fraction (kf_30), ends at about x = 1800 px, inside 1824. Citations sit at y ≈ −2.97, above the −3.2 caption zone.
- Type: primary labels and ticks are large enough. The ghost label "top card 52.4%" mixes Text and `MathTex(font_size=MATH_SMALL-4)`, so the digits are about 22 px cap height against about 26 px for the words (crop of kf_08). That is below the 24 px tick minimum and visibly mismatched.
- Palette: disciplined and consistent. Purple is riffled, blue is perfect, yellow is rising sequences (counts, caps, gap, 230), red is the giveaway (excess, d, meter fill). No colour is reused with a second meaning.
- Hierarchy: good from 0:24 to 2:17. It gets crowded at 1:19–1:34 (nine text items, still legible) and at 2:39–2:48 (six groups).

## FIXES (highest impact first)
1. **[1:58–2:37, 3:03–3:11, 3:32–3:53][Concision]** The 5 → 6 → 7 riffle progression is shown three times: the histogram slides (1:58–2:17), the rewind-and-replay (2:29–2:37) and the landing (3:40–3:45). The d values are also read off the curve at 3:05–3:11. → Cut the rewind at 2:29. Keep the chart at k = 7, lay the 0.85-spread hop there, and show the k = 4 comparison by keeping a dim ghost of the 1:55 bracket ("12.4 = 5.9 spreads") instead of sliding back. In the landing, play riffles 5–7 at about 1.0 s each without re-splitting the levels, so the needle and the level count only tick. Delete "Seven belongs to this yardstick." (3:11.7, about 2 s). Target runtime ≤ 3:30.
2. **[2:16.9–2:19.6][Motion/Clarity]** `accuracy = ½ + ½ d`, the conclusion of the accuracy derivation, is at full opacity for under 1 s and then dims (scene.py, the "A seventh riffle" beat: `e3.animate.set_opacity(0.3)` inside the slide to 7). → End the "Accuracy is a half plus…" beat with the e3 transform, then hold e3 at full opacity for ≥ 3 s with `d` in red flashing together with the red area (add `[pause 1.0]` after "the red area"). Start the seventh-riffle slide only after that hold, and dim e3 at the start of "Meanwhile".
3. **[1:42–1:48][Clarity]** "Pile each deck onto its count" turns one deck into a square labelled "1 deck" at chance ≈ 0.03 (kf_15), then a full distribution appears with no bridge. "Chance" also changes meaning from per-deck (3.5×10⁻⁶⁰) to per-count. → Narrate "Do this for every possible deck, weighted by its chance." Drop 4–5 more small purple and blue squares (other decks) into the 13–16 and 24–29 columns before the bars grow. Put the "1 deck" squares on the axis as tokens rather than on the chance scale, and relabel the y-axis "chance of this count".
4. **[2:36.3–2:43.9][Audio/Clarity]** "Gap times two to the k levels off near two hundred thirty" is a garden path, since "levels" is a noun in this episode and whisper inserts "K levels, off". → Replace it with "Multiply each gap by two to the k, and it settles near two hundred thirty."
5. **[2:41–3:01][Motion/Clarity]** Four equation states arrive in about 20 s, and `gap ≈ 230/2^k = 2.1` misuses "=". → Write `gap ≈ 230/2^k` first. Then fly the blue "2.1" in under the words "set gap = spread", so the line becomes `230/2^k ≈ 2.1`. Hold each state ≥ 3 s (2 s + 0.4 s per term) before transforming. Spend the 6–8 s saved by fix 1 here.
6. **[2:41–2:48][Visual/Sync]** While the narration says "the gap meets the spread", the chart's "spread 2.1" label and bracket are dimmed to about 15 % (frame 2:46.5), so the referent of the blue 2.1 is not visible. → Keep the spread bracket and label at full opacity and `Indicate` them as their copy flies into the equation. Dim the gap and ×2^k rows to 30 % instead.
7. **[3:22.6–3:23.4][Visual]** The citation crossfade overlaps "Diaconis, 1996 · PNAS" and "Trefethen & Trefethen, 2000" in the same spot (frame 3:23.0). → Use `Succession(FadeOut(tref, run_time=0.3), FadeIn(dia, run_time=0.4))`, and apply the same pattern to every citation swap (1:35, 3:01, 3:13).
8. **[1:11, 2:19, 2:39, 3:41, 3:51][Motion]** Counters (riffle count, rising-sequence count, meter %, gap label copies) change by glyph-to-glyph morphing and show garbled intermediates ("¿ riffles", "2ɕ", "9▒%", the "1.79" blob at 2:19). → Swap counters with `FadeTransform` plus a 0.15-unit vertical shift (old moves up and out, new comes in from below) over 0.35 s, or use `DecimalNumber` with `ChangeDecimalToValue` for the meter. For copies flying into the rows, move a whole `.copy()` with `animate.move_to` and `FadeTransform` only on arrival.
9. **[0:15–0:23][Hook/Motion]** The stakes line is generic, and the picture adds no information for about 8 s. → Make the motion carry the line. On "mixes by random steps", replay the left deck's four riffles fast (0.35 s each) with a step counter "1 2 3 4" above it. On "stopped too early", freeze it with a purple "stop here?" tag. On "remembers where it started", draw the dashed sorted profile (already built) 2 s earlier than now.
10. **[0:00–0:09][Visual]** The cold open uses only the top 55 % of the frame (kf_01, content between y ≈ 180 and 670 px). → Centre the two decks vertically (shift down about 0.8 units) for 0:00–0:08, and shift them up 0.8 as the meter draws at 0:08.
11. **[0:45–3:53][Visual]** The ghost label "top card 52.4%" mixes Text and smaller MathTex digits (about 22 px cap, below the 24 px minimum). → In `Meter.ghost` (scene.py ≈ l.255), set the % to the same size as the words: `MathTex(..., font_size=MATH_SMALL)`, or render the whole label as one `text(...)` at SMALL.
12. **[3:01–3:10, 0:49–1:34][Clarity]** "Aldous, then Bayer and Diaconis, proved it: for fifty-two cards…" credits the exact 52-card count to Aldous as well. The Gilbert/Reeds citation also has no venue. → Change to "Aldous proved the three-halves law; Bayer and Diaconis computed it exactly: for fifty-two cards, seven riffles…". Change the citation to "Gilbert, 1955 · Bell Labs memo · Reeds, 1981 · unpubl."
13. **[2:34.5][Audio]** "the distance halves too" is heard as "halves two" among the numbers. → "the distance starts halving."
14. **[1:01–1:09][Clarity]** In the level view, bar height switches from card number to sequence index on four spoken words. → As the bars drop, leave their old tops as 25 %-opacity ticks for 1 s, and add a ≤ 4-word grey label next to the deck, "height = which sequence". Remove the label after riffle 2.

**REACHES 9 IF ALL FIXED: yes, narrowly.** Fixes 1–5 lift Concision to about 9 and Clarity and Motion to about 9, and fixes 6–11 take Visual to 9. Estimated 9.0 with Hook 9 · Clarity 9 · Visual 9 · Motion 9 · Audio 9 · Concision 9 · Originality 8.5. No structural change is needed: the hook, the failure beat (top card at 52.4 % against whole deck at 99.99998 %) and the one-picture insight are all present. The pass depends on actually cutting runtime to ≤ 3:30 and on letting the two derivations (accuracy, then 2^k ≈ 110) breathe. Without fix 1 the episode stays at about 8.5.

## KEEP
- The rising-sequence **level view** with the cut line ringing each level and the ≤ 2^k ceilings (1:02–1:16). This is the episode's memorable, original image.
- The **spread hops laid along the gap** (5.9 spreads → 0.85 spreads) feeding the cliff drawn through the d-dots. The mechanism is shown, not asserted.
- The **meter as the spine**: the same 50–100 % track from the cold open, the 52.4 % top-card ghost, the jump to 99.99998 %, and the landing needle stepping down to 52.1 % beside the ghost on "takes ten".
