# Episode 006, round 6, craft critic (visual design / motion / sync emphasis)

Evidence: `review/` pack (metrics.json 23:54 is newer than final.mp4 23:52, so it was reused): report.md, all 12 contact sheets, 16 full-resolution keyframes (kf_02, 04, 09, 10, 13, 16, 19, 22, 26, 27, 29, 31, 32, 36, 38, 40), plus my own ffmpeg strips: 1:04.0–1:09.0 (counter slides), 1:59.5–2:12.8 cropped to the equation (accuracy build), 0:00, 0:24–0:26, 1:32.4–1:34.8 (squeeze into tokens), 3:19.6–3:20.8 (landing transition), 3:19.5–3:32.5 (landing counters). I read transcript.txt, narration.txt, script.md, facts.md and the CHANGELOG. I recomputed every number with exact Eulerian-number arithmetic and the B–D formula C(2^k+n−r, n)/2^(kn).

```
EPISODE: 006 — "Seven Shuffles: When a Deck Suddenly Becomes Random"
IDEA: A riffled deck's chance depends only on its number of rising sequences; each riffle halves the gap between that count and a random deck's while the random spread stays fixed, so the deck stays almost perfectly detectable for four riffles (even though the top card already looks random) and then falls off a cliff near seven.
SCORES: Hook 9 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.6 (8.625)   AFTER CEILING: 8.6 (ceiling 8.5 + 2 = 10.5, not binding)
CAPS: none
FINAL: 8.6   PASS: no
```

## FACTS
| Claim | Verdict | Source / my check |
|---|---|---|
| GSR model: cut near the middle, drop in proportion to packet size | Verified | Bayer & Diaconis 1992, p. 294 |
| One riffle leaves 2 rising sequences; ≤ 2^k after k riffles | Verified | cut-crosses-each-level-once argument; B–D §3 |
| Card 1 on top after 4 riffles 1 time in 15 | Verified | exact (1/16)Σ(j/16)^51 = 0.0649 (1 in 15.4) |
| Judging by top card: 52 % (52.4 %) | Verified | ½ + ½·TV(top card), TV ≈ 0.048 |
| 14-sequence deck chance 3.5×10⁻⁶⁰; perfect 1.2×10⁻⁶⁸ | Verified | C(54,52)/2^208 = 3.48e-60; 1/52! = 1.24e-68 |
| Same count → same chance (B–D) | Verified | B–D 1992 Theorem 1 |
| Perfect deck ≤ 16 sequences once in 2 (2.1) million | Verified | exact 4.666e-7 = 1 in 2,143,307 |
| Wrong once in 4 million games; 99.99998 % | Verified | ½·4.666e-7 = 1 in 4.29 M |
| d = 1.00, 0.92, 0.61, 0.33 at 4–7; 0.17, 0.085, 0.043 at 8–10 | Verified | exact 0.9237, 0.6135, 0.3341, 0.1672, 0.0854, 0.0429; B–D Table 1 |
| Zone at 7: catch 65 %, flag 32 %; accuracy = ½ + ½d | Verified | P = 0.6500, U = 0.3159 (r ≤ 25) |
| Gap 12.4 → 6.89 → 3.55 → 1.79; ×2^k → 198, 220, 227, 229 → 230 = n(n+1)/12 | Verified | exact means 14.099, 19.605, 22.948, 24.710; limit 229.67 |
| Spread (sd) 2.1 = √((n+1)/12) | Verified | 2.1016 |
| k ≈ 6.8 "just under 7"; (3/2)log₂n − 1.8 | Verified (heuristic, labelled "gap = spread rule") | log₂(229.67/2.10) = 6.77; ½log₂12 = 1.79 |
| Aldous (1983) proved the (3/2)log₂n law | Verified | Aldous 1983 Sém. Probab. XVII; credited so by B–D p. 296 and Trefethen² abstract |
| 7 riffles first below ½ for 52 cards | Verified | B–D Table 1 |
| Trefethen & Trefethen 2000: information measure, no cutoff, 5–6 shuffles | Verified | Proc. R. Soc. A 456:2561; abstract "no cutoff" |
| Many Markov chains show a sharp cutoff | Verified | Diaconis 1996 PNAS 93:1659 |
| Top-card-only distance curve 0.71, 0.37, 0.12, 0.048 … "(computed)" | Verified | labelled computed; consistent with my top-card calc at k = 4 |
| Landing: 7 riffles → right 2 times out of 3 (66.7 %); 10 riffles 52.1 % < top card 52.4 % | Verified | ½ + ½·0.3341 = 0.667; ½ + ½·0.0429 = 0.521 |

## MECHANICS
runtime 3:34.8 · 148 wpm (speech) · max silence 1.84 s (planned prediction hold) · max static 3.23 s (3:06.7) · −14.0 LUFS / −2.1 dBTP · lead 0.00 s / trail 1.77 s · 0 banned phrases · WER 1.0 % · layout audit 0 issues.

## What I saw (flipbook notes)
- **Cold open 0:00–0:15** is strong: two sorted decks on frame 1, purple/blue tags, the right deck jumps to random on "perfectly", the meter draws and "?" hops 50→75→100 on each spoken option (sheet 1, 0:09–0:13). Commit lands at 0:10–0:13.
- **Naive build 0:23–0:41**: the top-card bar chart with red excess at card 1, blue 1-in-52 line, meter needle at 52.4 % (kf_04, sheet 2–3). Clean, one focal point.
- **Fail 0:42–1:26**: the level view is the episode's signature image (kf_09); counter slides land on "Eight" (1:05.2) and "fourteen" (1:08.4) per my strip. Side by side 14 vs 26 with the 16-line (kf_13) and the needle jump to 99.99998 % on "four million" (1:21) are well synced.
- **Insight 1:26–2:50**: decks squeeze into tokens, tokens rain into stacks, stacks become exact bars, red = purple above blue, the bracket's bar flies into the gap row, areas fly into 0.65 / 0.32, the spread ruler sits beside the gap, hops are laid along it (5.9 vs 0.85 spreads), the cliff is drawn through the dots. This is real 3b1b grammar. Weak spots are the equation build (2:00–2:12) and the general-n substitutions (2:41–2:49), below.
- **Payoff 2:50–3:19**: Aldous / B–D / Trefethen / Diaconis citations swap in sequentially at bottom-left, each on its name. The "top card only (computed)" vs "whole deck" curves (kf_38) are a superb closing image.
- **Landing 3:20–3:33**: fade through black (3:20.4 is empty), the opening deck returns in level view, needle steps 99.99998 → 94.8 → … → 66.7 → 58.3 → 52.1 % beside the "top card 52.4 %" ghost. Resolves the opening exactly.

## FIXES (highest impact first)
1. **[1:59.5–2:12.8][Motion/Visual] accuracy equation build has three glyph-collision moments.** 2:01.5: the purple area copy morphs into "0.65" on top of "½(" (unreadable blob of glyphs for ~0.5 s). 2:08.5: the line-2 copies ("=", "½ +") fly up across line 1's "½(0.65", overlapping it. 2:11.4: line 1's tail has left, "½ + ½" sits stranded bottom-left of "accuracy =", and the 25 %-opacity "(0.65 − 0.32)" floats above it, detached from where `d` will land. **Change:** (a) reserve each slot first: write "accuracy = ½(   ) + ½(1 −    )" with invisible placeholders, then fly the area copies on an arc *above* the equation and `FadeTransform` into the slot only after they arrive; (b) give the line-2 copies `path_arc` downward (negative arc) so they never cross line 1; (c) do the collapse in place: fade line 1 except "accuracy =", move line 2 up into line 1's position in one `TransformMatchingTex`, *then* `ReplacementTransform` the parenthesised "(0.65 − 0.32)" into red `d` at its own position. During 2:00–2:12 dim the distance inset and the gap row to 35 % so the equation is the only focal point (both stay full-bright now, kf_26).
2. **[2:39–2:49][Clarity/Motion] general-n substitution: false intermediate and short holds.** 2:41–2:44 shows "2.1 ≈ n(n+1)/12 / 2^k ⇒ k ≈ 6.8" for ~3 s (sheet 9–10): a numeric 52-card LHS beside a general-n RHS and the 52-card answer, which is wrong for general n. The three changes (2:41, 2:44.5, 2:48) each hold ~3.5 s, under the §5 rule (2 s + 0.4 s × ~6 terms ≈ 4.4 s). **Change:** on "For n cards" fade "⇒ k ≈ 6.8" to 25 % first; swap 230 → n(n+1)/12 and 2.1 → √((n+1)/12) in one `TransformMatchingTex` (both under "∼ n²" / "∼ √n" tags, one flash each, staggered 0.6 s) so no mixed state exists; hold the general equation ≥ 4.5 s before `k ≈ (3/2)log₂n − 1.8` writes. If time is needed, take it from fix 6.
3. **[1:33–1:43][Clarity] sufficiency step is implied, not said.** "So pile decks onto their counts" and "The red area … is the distance from random" never say the count carries all the evidence, so a careful viewer asks "distance of the count or of the deck?" (needs a rewatch). **Change:** narration "Same count, same chance, so the count carries all the evidence. Pile decks onto their counts …" and "the red area … is the whole deck's distance from random"; on "all the evidence" put a 4-word grey label "count = all the evidence" under the axis title for 2.5 s.
4. **[1:51–2:19][Visual] unlabeled 30 % ghost bracket.** From 1:51 a dim yellow bracket spanning 14 → 26.5 hangs over the chart (kf_22, sheet 7–8) with no label for ~28 s; it only gains meaning at 2:21 when the hops are laid on it. **Change:** hide it at 1:51 and draw it back on "several spreads" (2:20) from the gap row's "12.4" (`TransformFromCopy`), or label it at its left leg "4 riffles: 12.4" in dim yellow, font 18 Text.
5. **[2:29–2:39][Visual] top-left stack is crowded.** Gap row, ×2^k row, "7 riffles" tag and "share of decks" title sit in ~1.7 units with ~25 px between the ×2^k row and the tag (kf_29); the ×2^k row also starts 60 px left of "gap:", so the two rows don't share a left edge. **Change:** left-align "×2^k ≈" under "gap:"; move the riffle tag off the axis-title column (fix 6), which opens ≥ 0.4 units between rows.
6. **[1:41–2:39][Visual] "k riffles" tag floats above the y-axis title.** "4 riffles" / "7 riffles" (kf_19, kf_22) sit stacked over "share of decks" and read as part of the axis title. **Change:** attach the tag to the purple histogram (`next_to(purple_peak, UR, buff=0.2)`) and let it ride with the slide; after 2:13 (7 is settled) dim it to 40 %.
7. **[1:32.8–1:33.6][Motion] squeeze into tokens scatters the yellow caps.** At 1:33.2 the 104 level caps fly loose above and around both decks while the bars compress, a confetti moment that carries no meaning. **Change:** `FadeOut` the caps (0.4 s) before the squeeze, or include them in the same `Transform` target so they collapse into the token with their bar.
8. **[3:03–3:10][Clarity/Visual] information yardstick drawn on the TV axis.** The grey band over 5–6 riffles (kf_36) sits on the d-curve, where d is still 0.92 / 0.61, so it reads as "the distance is fine at 5–6". **Change:** replace the band with a grey bracket *under the x-axis* at 5–6 labelled "information: enough" and keep the note "different yardstick: no cliff".
9. **[3:19.6–3:20.8][Motion] landing enters via fade through black.** The opening deck reappears after a ~0.8 s empty frame rather than by a transform, the one place the episode breaks its persistence grammar. **Change:** shrink the d-plot while the k = 4 dot flies to the meter needle and becomes it (needle at 99.99998 %), and fade the deck in under it, so the landing is visibly "this point on the curve".
10. **[0:20.0][Audio] "Stopped too early" is heard as "Stop too early"** (WER diff). The "-ped t" elides at speed. **Change:** "Halt them too early, and they still remember where they started," or slow that sentence to 0.80 speed.
11. **[1:22.3][Audio] 201 wpm on "The top card can't see this"** (report). This is the line that turns the episode. **Change:** speed 0.78 on that sentence and [pause 0.5] after "this" while the 14 / 26 counts flash.

REACHES 9 IF ALL FIXED: yes, narrowly. Fixes 1–2 lift Motion and Clarity to 9, fixes 3–6 lift Visual and Clarity to 9, fixes 10–11 lift Audio to 9 (Hook 9, Clarity 9, Visual 9, Motion 9, Audio 9, Concision 8.5, Originality 9 → 8.95). To clear 9.0 cleanly, Concision also needs a 9: the 2:12–2:50 stretch packs about 12 new numbers into 38 s. Fold the "×2^k ≈ 198 → 220 → 227 → 229 → 230" list into "Multiply each gap by two to the k: it settles near two hundred thirty", with only 198 and 230 visible and the middle values ticking in a live `DecimalNumber`. Nothing structural is missing.

KEEP:
- The level view (bars drop to their sequence's level, the cut crosses each level once, ceiling ≤ 2^k), which shows *why* rising sequences give the deck away.
- The cold-open meter that comes back three times with the "top card 52.4 %" ghost (0:10, 1:21, 3:20–3:33), so the ending re-sees the opening exactly.
- The closing "top card only (computed)" curve against the red "whole deck" cliff (3:15–3:20).
