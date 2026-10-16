# Review, round 1 (science and story editor): episode 003

```
EPISODE: 003 — "Randomness Looks Clumpier Than You Think"
IDEA: Pure chance leaves gaps, and the gaps force clumps, so a cluster is not evidence of aim. The honest test compares the whole count histogram with Poisson's prediction, and a pattern that is too even is the sign of a rule.
SCORES: Hook 8.5 · Clarity 7.5 · Visual 8 · Motion 8 · Audio 8 · Concision 8 · Originality 8
WEIGHTED: 8.0 (7.95)   AFTER CEILING: 8.0 (ceiling 7.5 + 2 = 9.5, not binding)
CAPS: Factual/mathematical error → 6: on-screen "0.39 × 576 ≈ 227" @ 1:19–2:05 (kf_12 @ 1:27.6; scene.py:366). 0.39 × 576 = 224.6. The 227 comes from 0.3933 × 576 = 226.6, but the screen states the false product.
FINAL: 6.0   PASS: no
```

## FACTS

| Claim | Status | Source / check |
|---|---|---|
| Each map has 537 hits on 576 squares (24×24) | Verified | sim_data.npz recount: A and B both 537 points |
| Map A lights up with 39 squares with ≥ 3 hits | Verified | recount A: 0..5+ = 222, 223, 92, 28, 9, 2 → 28+9+2 = 39 |
| Map B has none | Verified | recount B: 109, 397, 70, 0, 0, 0 |
| B's rule: no two hits closer than 4/5 square | Verified | min pairwise distance = 0.8005 squares |
| One bomb lands in a given square with chance 1/576; P(empty) = (1 − 1/576)^537 ≈ 0.39 | Verified | 0.39333 |
| "about 227 squares stay empty" (spoken) | Verified | 576 × 0.39333 = 226.6; 576·e^−λ = 226.7 |
| **On screen "0.39 × 576 ≈ 227" (1:19–2:05)** | **Wrong** | 0.39 × 576 = 224.64. The rounded factor gives 225, not 227 |
| "four in ten, with almost a bomb per square" | Verified | 39.3 %; λ = 0.932 |
| Map A has 222 empty squares | Verified | recount |
| The other 354 squares share the hits, about 1.5 each | Verified | 576 − 222 = 354; 537/354 = 1.517 |
| λ = 537/576 ≈ 0.93; P(0) ≈ e^−λ ≈ 0.39 | Verified | 0.9323; e^−0.9323 = 0.3937 |
| P(k) ≈ (537^k/k!)(1/576)^k e^−λ → λ^k e^−λ / k! | Verified (approximation) | binomial→Poisson. C(537,k) ≈ 537^k/k! and (575/576)^(537−k) ≈ e^−λ are used but never said |
| Purple bars 227, 211, 98.5, 30.6, 7.1, 1.6 | Verified | 576·Pois(0.9323) = 226.74, 211.39, 98.54, 30.62, 7.14, 1.57 |
| Map B: half the expected empty squares, a tower of single hits | Verified | 109/226.7 = 0.48; 397 vs 211 |
| 1944: Londoners claimed the flying bombs fell in clusters; quote "…tended to be grouped in clusters." | Verified | Clarke 1946 p. 481, quoted verbatim in Shaw & Shaw 2019 ("frequent assertions were made that the points of impact of the bombs tended to be grouped in clusters") |
| Precise aim would put factories at risk | Verified | Shaw & Shaw 2019: "if it could be accurately targeted at munitions factories it would also become a strategic threat to the war effort" |
| R. D. Clarke, an actuary, 1946, J. Inst. Actuaries 72:481 | Verified | Byline "R. D. Clarke, F.I.A., of the Prudential Assurance Company"; doi:10.1017/S0020268100035435 |
| 537 hits over 576 squares of south London; expected 226.74/211.39/98.54/30.62/7.14/1.57 vs actual 229/211/93/35/7/1 | Verified | Clarke 1946 table, reproduced in Shaw & Shaw 2019 |
| χ² test p = 0.88 | Verified | Clarke; recomputed χ² = 1.171, df = 4 → p = 0.883 |
| "…no support to the clustering hypothesis" | Verified (secondary) | Clarke 1946 per facts.md; consistent with Shaw & Shaw's summary |
| Clustering would show as extra empty squares and extra pile-ups | Verified | Clarke's stated alternative (excess of high and zero classes) |
| Aimed at London, but too loosely to choose a street | Verified (paraphrase) | Shaw & Shaw: V-1s "tended to fall short of the centre of London" |
| Over the whole county map more hits fell in the south; whole-county test p = 0.02 | Verified | Shaw & Shaw 2019, *Significance* 16(5):12–17: "skewed to the south", "the chi-squared test gives p=0.02" |

## MECHANICS

```
MECHANICS: runtime 3:22.6 · wpm 158 (speech) / 154 overall · max silence 1.98 s (0:10.1, planned prediction hold) · max static 3.97 s (3:14.0) · −14.0 LUFS / −2.0 dBTP
```
Leading silence 0.00 s, trailing 1.74 s, 0 black frames, WER 2.0 %, 0 banned phrases. No mechanical cap is triggered.

## Transcript and story notes

- **Hook (0:00–0:12):** strong. The first frame shows the two maps with live counters, the question "Which one is chance?" comes at 0:09, and a 1.9 s hold follows. Real stakes arrive by 0:24 (V-1s, factories). The landing at 3:12–3:21 returns to the exact cold-open frame, and "If you picked map B, you picked the one with a plan" resolves the opening.
- **Fail beat (0:43–1:00):** good StuffMadeHere structure. "Backwards." is followed by a measured failure ("39 false alarms") and a named cause ("expected chance to spread out evenly").
- **Sag (1:38–2:05):** about 27 s of symbol work beside a static map, and its key step is announced, not shown (e^−λ, see fix 2).
- **The v2 detector has no number:** "So the honest detector compares whole histograms" (2:04). Unlike v1, which gave a count, v2 gives no measured verdict for A or B. It is judged by eye, which is weak for an episode about eyes being fooled.
- **Slop scan:** no §4 phrases. "Backwards." is a one-word reveal but it carries content, so it is not counted. "Too even is the fingerprint of a rule" (2:19) is aphoristic and logically loose, because aim is also a rule and the next sentence says aim produces the opposite pattern.
- **Pronunciation:** "Poisson" is correct (whisper heard "Poisson"). "Clarke" is heard as "Clark", which is a homophone and fine. "too/two" is a homophone. Nothing is mispronounced.

## Contact-sheet and keyframe notes

- **Persistence:** good. The same Map A carries from 0:00 to 2:13; its cells shade, outline, fill and then become bars. The formula is assembled with TransformMatchingTex (1:47–1:57; a transient glyph scramble appears at 1:52.0 mid-morph, which is acceptable).
- **1:29–1:37:** the narration says "so many take two or more", but the highlighted squares are the red outlines of the 39 squares with 3+ hits. The 131 squares with 2+ hits are never shown.
- **1:23–2:13:** the declared YELLOW "empty" fill renders as a muddy olive brown (kf_12, kf_14, kf_24) and does not match the yellow "222 empty" label next to it.
- **2:09–2:19 (kf_24):** the 3/4/5+ bars are a few pixels tall, so the "39 targets" brace points at bars too small to see. The central comparison of the fix beat cannot be read from the chart.
- **1:59–2:05:** "Times 576" is never shown on screen, because the axis is in squares while the formula is P(k). "These purple bars" is spoken at 2:03.4, but the bars only start growing after 2:04.0 (axes are still empty at 2:04.0).
- **3:10.3–3:11.9:** the Shaw & Shaw citation and "whole county p = 0.02" are on screen for about 1.6 s before the cross-fade to the landing. That breaks the ≥ 3 s citation hold and the reading time, so the one non-Clarke empirical number is effectively unreadable.
- **3:01–3:11 schematic:** labelled "schematic" honestly, but it is thin. The payoff never shows a real map of real hits, even though Shaw & Shaw digitised all 887 London County V-1 locations.
- **Layout:** type sizes, margins and contrast are fine on all keyframes checked (0:15, 0:19.5, 0:34, 0:52.8, 1:02.4, 1:27.6, 1:35.7, 1:45.8, 1:52.5, 2:13.6, 2:59, 3:11.5, 3:22.5). No overlaps or clipping. Every chart axis is labelled.

## FIXES (highest impact first)

1. **[1:19–2:05][Clarity, removes cap 6]** The on-screen "0.39 × 576 ≈ 227" is arithmetically false (224.6). In scene.py:366, change `formula(r"0.39", r"\times", r"576", r"\approx", r"227")` to `0.393 × 576 ≈ 227` and the line above to `≈ 0.393`. The spoken "point three nine … about two hundred and twenty-seven" can stay.
2. **[1:38–1:45][Clarity]** e^−λ is announced, not derived. Add one transform chain under P(empty): `(1 − 1/576)^537` → `(1 − λ/537)^537` (TransformFromCopy of λ from the λ line) → `≈ e^{−λ}`, with a side-by-side check "0.3933 vs 0.3937". Narration (+5 s): "One over five seventy-six is lambda over five thirty-seven, and one minus a tiny slice, raised to a big power, is e to the minus lambda: point three nine three either way."
3. **[2:04–2:22][Clarity/Hook]** The v2 detector needs a measured verdict, as v1 had. After the bars settle, add a live `DecimalNumber` "fit to chance: p = 0.74" under Map A. When B slides in, morph it to "p < 10⁻⁵⁰" (recomputed: A χ² = 2.0, df 4, p = 0.74; B χ² = 271.7, p ≈ 1e−57). Narration: "Map A: p point seven four. Map B: p below ten to the minus fifty." This also sets up Clarke's p = 0.88 as the same number on real data.
4. **[2:09–2:19][Visual]** The tail bars are unreadable. Add a 4× zoom inset over k = 3–5+ (purple outline 39.3 vs blue 39), or count labels over those bars, so "39 targets in all" can be read off the chart.
5. **[1:29–1:37][Clarity/Visual]** "So many take two or more" is shown with the 3+ outlines. Outline the 131 squares with ≥ 2 hits in BLUE with a counter "131 squares with 2+", then fade it out, keeping RED for detector targets only.
6. **[3:10–3:12][Visual/Clarity]** "whole county p = 0.02" and the Shaw & Shaw citation are visible for about 1.6 s. Hold them ≥ 3 s (add a 1.5 s wait before the landing cross-fade, or let the citation persist until 3:14).
7. **[2:29–2:41][Originality/Hook]** The payoff on real data shows no real map. Shaw & Shaw digitised the LCC V-1 locations (887 hits). If the dataset is available, open the Clarke beat with the real dots over a 144 km² square (labelled "V-1 hits, LCC bomb damage maps"), gridded the same way as Maps A and B, before the histogram. This is the screenshot moment the episode lacks. If it is not available, say so in facts.md and keep the schematic.
8. **[2:19–2:22][Clarity]** "Too even is the fingerprint of a rule" over-generalises, since aim is also a rule and the next line says it does the opposite. Change it to "Too even is the fingerprint of a spacing rule."
9. **[1:59–2:05][Clarity/Audio sync]** Show "× 576" on screen: transform P(k) into "576 · P(k)" beside the y-axis "squares" as the bars grow. Start the purple bar growth on "Times" (1:59.5) so "these purple bars" (2:03.4) lands on visible bars.
10. **[1:23–2:13][Visual]** The YELLOW fill reads as olive brown. Raise the empty-cell fill opacity (or use a yellow 2 px cell outline plus 30 % fill) so it matches the yellow "222 empty" counter and the palette's single meaning for YELLOW.

REACHES 9 IF ALL FIXED: yes, narrowly. Fix 1 alone lifts the final to 8.0. Fixes 2–6 and 8–9 should bring Clarity to 8.5–9, Visual to 8.5 and Hook to 9. Getting Originality above 8 depends on fix 7 (a real map of the real hits), because the flying-bomb Poisson example is the canonical textbook case (Feller). The detector-with-39-false-alarms framing is the fresh part and must stay.

KEEP: (1) The cold open and landing on the same two maps, closing with "If you picked map B, you picked the one with a plan". (2) The naive ≥ 3-hit detector failing with a measured "39 false alarms", and "Those gaps force the clumps". (3) The honest-limits beat (aimed at London but too loosely to choose a street; one λ everywhere; whole county p = 0.02).
