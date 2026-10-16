# Review, round 1 (craft critic: visual design, motion, A/V sync; all dimensions scored)

Evidence: `review/` pack (metrics.json 11:31 is newer than final.mp4 11:29, so it was reused). I read report.md, all 11 contact sheets,
keyframes kf_03, kf_07, kf_09, kf_15, kf_17, kf_19 at full resolution, and extra frames I pulled at 0:12.0–0:15.2 (the "?" slide),
1:28.8, 1:47, 1:49.5, 1:52.5, 2:01, 2:07.5, 2:29.0, 2:47.0, 3:03.5 and 3:06.0. I also read the transcript, word timings, script.md, facts.md and scene.py (palette and font sizes).

```
EPISODE: 060 — "Why Your Friends Have More Friends Than You"
IDEA: Following a friendship lands on each person once per friend she has, so the average friend has Σk²/Σk = μ + σ²/μ friends, which is more than the average person whenever friend counts vary. Epidemiologists use this to see an outbreak early.
SCORES: Hook 8 · Clarity 8.5 · Visual 8 · Motion 8 · Audio 8 · Concision 8.5 · Originality 8
WEIGHTED: 8.2   AFTER CEILING: 8.2   (lowest 8 + 2 = 10, so the ceiling does not bind)
CAPS: none (all three empirical sources are cited on screen; overlaps happen only mid-transition; no banned phrases; mechanics are within the bar)
FINAL: 8.2   PASS: no
FACTS:
- 8 girls, 10 reciprocated ties, "Marketville", Coleman's data, names fictitious | Verified | Feld 1991 AJS 96(6) Fig. 1/Table 1 (quoted in facts.md; edge list reproduces Table 1)
- "late 1950s" | Verified | Coleman survey 1957–58 (cited on screen as Coleman, 1961)
- counts 1,4,4,2,3,3,2,1 → mean 2.5; friend average 60/20 = 3 | Verified | recomputed: Σk = 20, Σk² = 1+16+16+4+9+9+4+1 = 60
- +0.5 = 20% of 2.5 | Verified | arithmetic
- ring: 8 edges, 16 tokens, 32/16 = 2 = μ, σ² = 0 | Verified | arithmetic
- two girls at each count 1–4; token columns 2,4,6,8; fulcra at 2.5 and 3 | Verified | the beam is evenly spaced, so position is linear in count and the token-weighted centroid sits at count 3; I checked pixel positions (fulcrum x ≈ 622 px versus 623.5 predicted)
- Sue 4 × 4 = 16 | Verified | arithmetic
- Σk²/Σk = mean(k²)/mean(k) = (μ²+σ²)/μ = μ + σ²/μ; 2.5 + 1.25/2.5 = 3 | Verified | re-derived, population variance 7.5 − 6.25 = 1.25
- Facebook 2011: average ≈190 friends; friends average ≈635 | Verified | Ugander, Karrer, Backstrom & Marlow 2011, arXiv:1111.4503 (abstract page and secondary sources confirm 190/635)
- spread term 445 > 2 × 190 | Verified | 635 − 190 = 445 > 380
- "a few users had thousands of friends" | Verified | Ugander et al. (cap of 5,000; long tail)
- Harvard 2009, 319 random students, 425 named friends | Verified | Christakis & Fowler 2010, PLoS ONE 5(9):e12948
- friends 13.9 days ahead (fitted); self-reported 3.2 days | Verified | C&F 2010 abstract/results
- 5 of 8 have fewer friends than their friends' average; Sue and Alice have more | Verified | Feld 1991 p.1465; recomputed (Carol is equal)
MECHANICS: runtime 3:11.3 · 149 wpm · max silence 2.09 s (planned prediction pause, 0:15.8 and 2:15.6) · max static 3.63 s · −14.0 LUFS / −1.9 dBTP · lead 0.00 s / trail 1.73 s · WER 1.1%
FIXES (highest impact first):
1. [1:43–1:55][Clarity/Motion] The crucial step, mean(k²) → μ² + σ², is a symbol morph (TransformMatchingShapes, frames 1:47 → 1:49.5) with no picture behind it. The token-stack picture produced Σk²/Σk, but nothing on screen produces σ². This is where the "one picture becomes the formula" chain breaks. Fix: on the beam, draw PURPLE deviation bars from the 2.5 fulcrum to each girl (lengths −1.5, −1.5, −0.5, −0.5, +0.5, +0.5, +1.5, +1.5), square them into PURPLE squares (2.25, 2.25, 0.25, 0.25, 0.25, 0.25, 2.25, 2.25), and show their average 1.25 = σ². Then TransformFromCopy that 1.25 into the σ² term of μ² + σ², and the 2.5 fulcrum into μ². Narration: "mean of k squared is the mean squared, plus the average squared distance from the mean, the variance." Hold the equation at least 2 s + 0.4 s per term before the next morph.
2. [2:27–2:41][Clarity] The narration never says *why* friends catch flu earlier. "Put this to work" assumes the viewer bridges "more friends" to "more exposure, infected sooner". Fix: add one sentence before "They tracked flu…": "More friends means more ways to catch it, so the friends should get sick first." On screen, keep the YELLOW friend bar (now 635) and morph it into the "425 friends they named" label instead of hard-resetting.
3. [2:28–2:33][Motion/Visual] Hard reset: everything vanishes and for about 2 s the frame is a lone grey x-axis with no labels (frame 2:29.0) while "Christakis and Fowler put this to work at Harvard" plays. This is the weakest frame in the video. Fix: shrink the dimmed beam and Facebook bars to the upper-left corner (scale 0.35, opacity 0.3), or transform the BLUE "average user" bar into the BLUE "319 random students" label and the YELLOW friend bar into the YELLOW "425 friends they named" label. Build the axes at the same time (axes and title in ≤ 1.2 s), so the first new visible object arrives on "Christakis".
4. [2:11–2:27 and 0:59–1:13][Visual] Colour/referent mismatch. The equation "190 + 445 = 635" colours 190 BLUE (μ), but the 190 segment of the friend bar is YELLOW. The same happens at 1:05–2:05, where the bar's 2.5 base is YELLOW while μ in μ + σ²/μ is BLUE. BAR §5 asks each term to be coloured like its referent. Fix: draw the friend bar's base segment as a BLUE fill (μ) with a YELLOW outline around the whole bar, and keep the total label (3.0 / 635) YELLOW. The bar then reads literally as μ (blue) + σ²/μ (purple) = friend average (yellow outline).
5. [2:58–3:09][Clarity/Sync] The landing asserts "five have fewer friends than their own friends' average" with only white outlines as evidence (frame 3:03.5), so the viewer cannot check it. "Only Sue and Alice have more" gets only a slight scale-up (frame 3:06.0), much weaker than the five outlines. Fix: as each of the five is outlined, put a small YELLOW number beside her for her friends' average (Betty 4, Jane 3.5, Pam 3.3, Dale 3.3, Tina 2). On "Sue and Alice", outline them in INK with a thicker stroke (6 vs 4) and show their friends' averages (2.5, 3.25) in YELLOW. Keep each label ≤ 3 characters at Text ≥ 26 so word load stays under 12.
6. [0:12.7–0:16.0][Sync/Motion] The "?" slide lags the words. At 0:13.5 ("than") it still sits at x≈0.5 (the "fewer" side), at 14.6 s ("fewer") it is at x≈3.3 (the "more" side), and at 15.2 s ("same") it is at x≈1.6. Each option is shown about 0.6–0.9 s late, so the image contradicts the word. Fix: start the slide right of 2.5 on "More" (12.68 s), cross to the left on "fewer" (14.60 s) and land on the dashed line on "same" (15.22 s). Use 0.5 s smooth moves keyed to the word timings in transcript_words.tsv.
7. [0:00–0:03][Hook] The first frame (0:01) is almost empty: three tiny dots and a faint name. BAR §6 wants the concrete object in the first frame. Fix: have the full network already at 70% opacity at 0:00 and animate the edges in. Also bring the commit point earlier by cutting "Now ask" (ask "How many friends does the average friend have?" directly) so the prediction hold starts at about 0:13.
8. [1:13–2:05][Visual] The composition is left-heavy and bottom-heavy. The beam and stacks fill x∈[−6.2,−0.3], y∈[−1.8,0.5], leaving the upper-left third empty for 50 s (frames 1:30, 1:36), while the right column stacks bars, axis and a growing equation. Fix: raise the beam by 0.8 units and move the "4 × 4 = 16" label and fulcra with it, or run the equation chain under the bars at x∈[0.5,6.3] and centre the beam group vertically on y = −0.2.
9. [0:29–1:01][Visual] The "guess" label is Text font_size 24 in GRAY inside the dashed box (frame kf_09), below the 26 minimum for labels, and it crowds the right edge of the box next to "?". Fix: font_size 26 and place it left-aligned inside the box with buff 0.15.
10. [1:28.8][Motion] The "3.0" copy that flies from the bar label to the yellow fulcrum passes through the purple segment and sits on the axis for several frames (frame 1:28.8). Fix: path_arc −0.6 so it arcs left of the bar group, run_time ≥ 0.8 s.
11. [2:07.0–2:07.6][Visual] The Feld and Ugander citations crossfade in the same spot and are both legible at once (2:07 contact frame). Fix: FadeOut Feld first (0.3 s), then FadeIn Ugander.
12. [3:05–3:11][Hook/Landing] The final line ("you tend to land on someone who has many") is accurate, but it never returns to the viewer, so it misses the title's "you". Optional fix: "Follow any friendship, yours included, and you tend to land on someone who has many." Keep the end within 2 s of the last word.
REACHES 9 IF ALL FIXED: yes, plausibly. The structure is right: misconception, a ring where the guess works, measured failure (+0.5, 20%), the weighted-beam picture, a formula, a real prediction at Facebook scale, and a cited, honestly limited payoff. What keeps it at 8 is a craft gap at one point: the variance step is announced rather than shown (fix 1). Fixes 2–5 close the remaining clarity, continuity and colour-semantics gaps. With fixes 1–5 applied, I would expect Clarity 9, Visual 8.5–9 and Motion 9, which gives about 8.8–9.0.
KEEP:
- The tokens: two per friendship, each reading the count of the girl it lands on, with the live "sum of counts / tokens" counter going 32/16 → 60/20 and the YELLOW bar overshooting the dashed guess by a PURPLE +0.5 (0:41–1:07). This is the episode's proof, and it is excellent.
- The beam of numbered token stacks with BLUE 2.5 and YELLOW 3 fulcra, and "sum of counts" turning into Σk² (1:15–1:43).
- The redrawn C&F Fig. 3 curves on a shared sweeping calendar, with the fitted 13.9-day arrow and the self-reported 3.2-day caveat (2:33–2:57).
```

## Notes by dimension

**Hook 8.** There is a concrete real network (Feld/Coleman) and a stated number by 0:09. A three-way prediction is posed 0:12.7–0:15.8, followed by a 2.1 s hold. The stakes (flu surveillance) arrive by 0:27 and are paid off at 2:27. Deductions: the first frame is nearly empty (0:01), the commit point lands at 0:15.8 rather than ≤ 0:12, and the "?" choreography contradicts the spoken option (fix 6). Tension rises well through ring → fail → beam → Facebook prediction pause (2:13–2:18).

**Clarity 8.5.** Everything is concrete before abstract, every number checks, the sources are correct, and there is an honest limit (3.2 days self-reported). The ring control case ("no spread, no gap") is a strong touch. Deductions: the variance identity is asserted rather than shown (1:45–1:51), the infection mechanism is left implicit (2:27), and the landing's individual-level claim cannot be checked on screen (3:00).

**Visual 8.** One flat background; the palette is semantic and consistent (BLUE person-once, YELLOW reached-by-friendship, PURPLE spread, GRAY guess/axes). Axes carry names and units, citations are bottom-left above y = −3.2, and there are no persistent overlaps. Deductions: the friend bar's μ segment is YELLOW while μ is BLUE in the equation (1:05–2:27), the composition is unbalanced during the insight (1:15–2:05), the "guess" label is undersized, and the 2:29 frame is nearly empty. GRAY names measure 5.8:1 by the style file; that is acceptable for secondary labels, but it is the weakest contrast in the video.

**Motion 8.** Objects persist and transform: the network becomes a ring and back, girls glide onto the beam, tokens travel along edges and then into stacks, the counter labels become Σk²/Σk, numbers drop out of symbols, and the PURPLE 0.5 lands on the PURPLE bar. The static maximum is 3.6 s. Deductions: the variance step is a morph of glyphs with no geometric referent, there is a hard reset at 2:28, the "?" is mistimed, and the flying "3.0" crosses the bar at 1:28.8.

**Audio 8.** 149 wpm, −14.0 LUFS, −1.9 dBTP, WER 1.1%. Deictics mostly land: "4 on Sue, 4 on Alice, 1 on Betty" lights each stack (1:10–1:13); "rose first" flashes the curve (2:47); "13.9 days" brings the arrow (2:51); "319 random students" and "425 friends" labels appear as they are named. Deductions: the "?" lag on "more/fewer/same" and the weak emphasis on "Sue and Alice" (3:03). Cadence is measured and even, which is fine but not human-skilled.

**Concision 8.5.** 461 words, and almost every sentence pulls weight. The ring beat (0:33–0:50, about 17 s) earns its keep through the 2:03 callback. "Now ask" (0:09.8) and "Exactly the extra half friend we measured" (2:00), with the equation already showing 2.5 + 0.5, are the only soft spots.

**Originality 8.** The friendship paradox is a well-worn topic, but the tokens-as-weights balance beam is a fresh, memorable image. Using Feld's original eight girls, and pairing the formula with the real Harvard curves, goes beyond the standard telling. No slop phrases.
