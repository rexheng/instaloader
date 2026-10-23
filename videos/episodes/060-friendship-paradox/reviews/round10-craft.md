# Round 10 — craft critic (visual design, motion, A/V sync; every dimension scored)

Evidence used:
- The `review/` pack. metrics.json (23:33) is newer than final.mp4 (23:31), so I used it and did not regenerate.
- report.md, narration_diff.txt, transcript.txt, narration.txt, the round-9 CHANGELOG section, and round-9 craft review (to check which fixes landed).
- All 12 contact sheets.
- Full-resolution keyframes kf_01, 05, 08, 10, 13, 16, 18, 19, 22, 26, 28, 32, 35, 37, 39, 40.
- Extra strips I extracted with ffmpeg into my scratchpad: 2.5 fps 1:16–1:21 (the 16 flies into Σk²), 1:23–1:29.4 (divide pinch), 2:25.5–2:30.5 (ring beat), 3:23–3:28 (C&F to landing); 2 fps 1:34.5–1:42.5 (beam to distances); 5 fps 1:38.4–1:40.8 (sides then squares); 3 fps 1:59.5–2:03.5 (Sue's split to the general row) and 2:55.5–2:59.5 (Facebook to class); full-res crops at 2:00.6, 2:01.0, 2:01.4, 2:01.8, 2:02.2 and a full frame at 3:25.0.
- I recomputed every network number from the degree list Betty 1, Sue 4, Alice 4, Jane 2, Dale 3, Pam 3, Carol 2, Tina 1 (10 edges, as drawn at kf_05), and the C&F draw {Betty, Dale, Carol} → tokens 4, 4, 4, 2, 3, 1.

Round-9 craft fixes, checked on this master:
1. Squares: sides drop first (1:39.1–1:39.6), then grow down, then areas (1:40.5–1:41.5). **Fixed.**
2. Four distances in two lanes with end caps, labels over their own segments (kf_18). **Fixed.**
3. Divide step pinches in place with the ÷ 8s flashed; no frame without a numerator (strip 1:23–1:29). **Fixed.**
4. Facebook → class: the BLUE bar splits into the eight nodes, no empty frame (strip 2:55.5–2:59.5). **Fixed.**
5. "4 × 4 = 16": its 16 flies into Σk² at ~1:18.4 and the label leaves by 1:20 (strip). **Fixed.**
6. Cold-open breaths added (0:04.4 0.6 s, 0:08.0 0.8 s). **Partly** (median sentence still 170 wpm).
7. C&F tokens mid-edge, clear of rings (kf_35). **Fixed.**
8. End card held (kf_40). **Fixed.**

```
EPISODE: 060 — "Why Your Friends Have More Friends Than You"
IDEA: Sampling a person through a friendship lands on each girl once per friend she has, so the friend average is avg(k²)/μ = μ + σ²/μ (the cross term dies because distances from the balance point sum to zero), which exceeds the person average whenever friend counts vary — which is why the friends people name catch flu first.
SCORES: Hook 9 · Clarity 9 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 9 · Originality 9
WEIGHTED: 8.8 (135 + 225 + 127.5 + 127.5 + 85 + 90 + 90 = 880 / 100)   AFTER CEILING: 8.8 (lowest 8.5 + 2 = 10.5, does not bind)
CAPS: none. 0 banned phrases or patterns (I re-read the transcript: no question chains — "How many friends does the average friend have? Pick one." is a question plus an imperative; "Where does the extra half come from?" and the Facebook question stand alone). Every empirical claim carries an on-screen citation (Feld/Coleman 0:00–2:30, Ugander 2:31–2:58, C&F 2:59–3:24). Layout audit 0/218, and no overlap or clipping in any settled frame I read. Runtime, pace, silences, static stretches and loudness are in range.
FINAL: 8.8   PASS: no
FACTS:
- 8 girls, 10 friendships, counts 1,4,4,2,3,3,2,1; μ = 20/8 = 2.5 | Verified | Feld 1991 AJS 96(6) Fig. 1 (Coleman 1961); recomputed
- Ring: 16 tokens, 32/16 = 2.0, tagged "(hypothetical)" | Verified | computed (kf_08)
- Real class: 20 tokens, 60/20 = 3.0; partials 15/5, 58/19 consistent; +0.5 = 20 % of 2.5 | Verified | computed (kf_10, sheet 3)
- Fulcrum 2.5 → 2.7 (mid-slide, 1:09) → 3.0 | Verified | layer sums
- Sue 4 × 4 = 16; Σk² = 60; (60÷8)/(20÷8) = 7.5/2.5 = 3.0 | Verified | computed
- Distances ±1.5/±0.5; squares 2.25/0.25; σ² = 10/8 = 1.25 (population variance) | Verified | computed (kf_18)
- 4² = (2.5+1.5)² = 2.5² + 1.5² + 2·2.5·1.5; avg(d) = 0 ⇒ avg(k²) = μ² + σ² = 7.5 | Verified | algebra (kf_19, kf_22)
- μ + σ²/μ = 2.5 + 0.5 = 3.0; ring 2 + 0/2 = 2 | Verified | computed (kf_26, kf_28)
- Facebook May 2011: mean ≈ 190; friend-weighted mean 635; 190 + 445 = 635; 445 > 2 × 190 | Verified | Ugander, Karrer, Backstrom & Marlow 2011, arXiv:1111.4503
- 92.7 % (spoken "93 %") of users below their friends' average | Verified | Ugander et al. 2011
- C&F, Harvard 2009: 319 random students, 425 named friends; fitted lead 13.9 d; self-reported 3.2 d | Verified | Christakis & Fowler 2010, PLoS ONE 5(9) e12948
- C&F demo draw {Betty, Dale, Carol}: tokens 4,4,4,2,3,1 → 3.0 | Verified | computed (kf_35)
- "Most of us are Betty" | Verified as a fair per-person reading | 5 of 8 girls and 92.7 % of users below their friends' mean
MECHANICS: runtime 3:34.5 · wpm 153 (speech time; 138 overall; median sentence 170) · max silence 2.22 s (landing pause 3:29.0) · max static 3.5 s (0:53.1) · −14.0 LUFS / −2.1 dBTP · leading 0.00 s / trailing 1.80 s · WER 2.6 % (number formatting only)
FIXES (highest impact first):
1. [2:00.8–2:01.9][Motion] The generalisation step ("Every girl splits this way") passes through an equation with holes.
   - Full-res crops at 2:01.0 and 2:01.4 show only "=   +   + [2   ·]": Sue's 4², 2.5², 1.5², 2.5·1.5 have faded out and avg(k²), μ², σ², μ·avg(d) have not yet faded in (≈1.0 s of empty slots; also sheet 7 @2:01). This is the same disappear-then-reappear pattern that round 9 removed from the divide step, on the one line that turns Sue's arithmetic into the general law.
   - Change: use the same `pinch()` you built for the divide step, term by term, left to right with lag 0.15: 4² → avg(k²) (YELLOW), 2.5² → μ² (BLUE), 1.5² → σ² (PURPLE, and pulse the eight squares once as it lands, since σ² is their average), 2.5·1.5 → μ·avg(d) inside the box. Operators and the box stay put. No frame may lack a term; total ≈1.4 s, ending by 2:02.4 (before "Because the beam balances").
2. [3:24.6–3:25.6][Motion] The C&F chart → landing hand-off is the episode's last dip through a near-empty frame.
   - At 3:25.0 the full frame is the cold-open class at ~15 % opacity on black (my extracted frame; sheet 12 @3:25.0); at 3:24.6 the chart is already dimmed. Everywhere else the episode transforms between beats.
   - Change: play the 3:07 hand-off in reverse. The two curves shrink into the chart origin (0.6 s), the eight node rings fly out of the origin to their class positions in their C&F colours and relax to BLUE (0.8 s, lag 0.04), then friendships and names draw on and the "average girl / average friend" panel grows from its axis (0.6 s). Start at 3:24.3 so the class is fully opaque at "Betty looks" (3:25.7).
3. [2:06.5–2:30][Visual] The PURPLE "0" where the signed distances cancel sits inside the count axis's tick row.
   - kf_22 / kf_26: the ruler reads "1   2  0  3   4" — a 0 between 2 and 3 on an axis of friend counts. It is purple and slightly larger, but at a glance it is a mis-ordered tick label, and it survives dimmed into the ring beat (kf_28).
   - Change: when the signed copies meet at the balance point, morph them into "avg(d) = 0" in PURPLE, placed under "d = k − μ" at the right end of the ruler (x ≈ +4.3, y one line below, ≥ 0.15 clear of the σ² label). That label is then the visual referent for the boxed 2μ·avg(d) dying at 2:08, and the tick row stays 1, 2, 3, 4.
4. [2:09–2:22][Visual] Too many live layers while the main equation is the focal point.
   - kf_22 holds the lineup with names, the beam and fulcrum, four signed distances, the ruler, the "0", eight squares with their scale tag, σ² = 10/8 = 1.25, d = k − μ, avg(k²) = μ² + σ², the main fraction and the "+0.5 ?" target — 11 labelled groups at full opacity.
   - Change: on "So the average of k squared…" (2:08.4) dim the lineup, beam, ruler, distances and squares to 35 % (keep σ² = 1.25 and the "+0.5 ?" target at full), and restore them on "With no spread" (2:26.3) only as far as the ring beat needs. One focal point per frame.
5. [0:00–3:30][Audio] Cadence is still at the fast, even end.
   - Median sentence 170 wpm (above 165), full stops 0.39 s median with low variation (report §Narration craft), and the run from "The guess fell short…" to "…one on Betty" (0:51.1–0:59.6) is delivered as one breath group.
   - The runtime budget (3:34.5 of 3:35) blocks adding pauses, so make room: cut "Odds are, that includes you." (2:55.5–2:57.9, ≈2.4 s). It pre-empts the landing line "Most of us are Betty", which then lands harder.
   - Spend the 2.4 s: [pause 0.5] after "by half a friend" (0:53.6), [pause 0.4] after "unevenly", [pause 0.5] after "sixteen" (1:16.5, beyond the existing 0.6 if it reads clipped), and [pause 0.6] after "a cross term" (2:00.0) so fix 1's swap starts on a breath. Set CADENCE = "shaped".
6. [1:41.3–1:43.6][Visual, nitpick] The eight area labels zigzag on two rows ("2.25 2.25 0.25 0.25 …", sheet 6 @1:43) and read as noise for ~2 s before they fly to σ².
   - Change: one row, labels only under the first square of each pair (2.25 under Betty, 0.25 under Jane, 0.25 under Pam, 2.25 under Sue) with "×2" in GRAY after each; or shrink to MathTex 30 on one row at the squares' centres (each square pair is ≥ 108 px apart).
7. [2:25.9–2:29.5][Motion, nitpick] In the ring beat, "μ + σ²/μ = 2.5 + 0.5 = 3.0" fades out (2:25.9) and a fresh "μ + σ²/μ" fades in by the ring (2:27.5) before morphing to 2 + 0/2 = 2 (ring strip).
   - Change: TransformFromCopy the left side "μ + σ²/μ" of the existing equation down to the ring (0.8 s) instead of fading one out and another in.
REACHES 9 IF ALL FIXED: yes. Fixes 1, 2 and 7 remove the last transitions that disappear instead of transform (Motion 9). Fixes 3, 4 and 6 give every frame of the derivation one focal point and a clean axis (Visual 9). Fix 5 gives the narration audible structure inside the same runtime (Audio 9). That yields 9.0 weighted, with no structural change needed.
KEEP: (1) The token-weighted beam: the girls balance at the BLUE 2.5, the token layers slide the fulcrum to the YELLOW 3.0, and the same girls later carry the distances and squares. (2) The two-lane distance segments dropping as sides and growing into squares, then the signed distances sliding into the balance point to kill the cross term. (3) The BLUE / PURPLE / YELLOW-outlined friend bar carried from the class (2.5 + 0.5) to Facebook (190 + 445 = 635) and back into the silent landing where Betty sees 4.
```

## Notes by dimension

**Hook 9.** Frame 0 (kf_01) already poses the question with a YELLOW "?" beside dimmed "average girl / average friend". By 0:11 the candidates 2.5 / 3 / 4 are on the axis and "Pick one" is followed by a 2.0 s hold (0:12.8–0:14.8). The stakes line (0:14.8–0:21) is answered exactly by the C&F beat, and the landing (3:25–3:31) returns to the cold-open frame and resolves the three candidates (2.5 the girls, 3 the tokens, 4 what Betty sees). Nothing to change.

**Clarity 9.** Concrete before abstract all the way: ring check (works), real class (fails by +0.5 = 20 %), beam, Σk²/Σk, averages, variance as squares, Sue's split, the general identity, μ + σ²/μ, then the zero-spread check. Assumptions and limits are on screen (hypothetical ring; C&F lead shrinks from 13.9 to 3.2 days; "logistic refit" disclosed). Every number checks. The only place a viewer must take a step on faith is the 1 s gap at 2:01 where Sue's numbers become symbols (fix 1), which is a motion defect more than a logic gap.

**Visual 8.5.** The palette is disciplined (BLUE people / μ, YELLOW tokens / friend average, PURPLE spread, GRAY guess and axes, white highlights), type is generous, the safe area holds (the "+0.5 ?" target ends at x ≈ 1780 px, the C&F legend at 1808 px), every chart axis is named with a unit, and citations sit bottom-left. The round-9 issues (overlapping distances, the lingering 16, token clearances, the empty frame) are gone. What keeps it under 9: the "0" in the tick row (kf_22), the 11-layer frame during 2:09–2:22 where the equation should be the single focal point, and the zigzag area labels at 1:43.

**Motion 8.5.** Most moves now carry a relation: tokens travel both ways and read the count where they land; the girls sort onto the beam; the fulcrum slides as the layers land; the 16 flies into Σk² (1:18.4); the divide row pinches in place; the sides drop and the squares grow from them; signed distances slide into the balance point; the BLUE bar breaks into the class's nodes (2:58); the random students and named friends contract into the C&F origin (3:06–3:08). Three transitions still disappear and reappear rather than transform: the operator skeleton at 2:01 (fix 1), the fade through dark at 3:25 (fix 2) and the formula fade-out/fade-in at the ring (fix 7). The first is on the episode's key generalisation, so it costs the half point.

**Audio 8.5.** Sync is excellent: "four on Sue, four on Alice, one on Betty" pulse as named (0:57–1:00); the fulcrum reaches 3.0 on "balance at three" (1:11); the squares grow on "square it" (1:39); the ring appears on "With no spread" (2:26.3); 635 appears on its word (2:44–2:45); "rose first" lands as the friends' curve leads (3:13). Loudness is exactly −14.0 LUFS with −2.1 dBTP, and WER differences are number formatting only. The deduction is for measured cadence, not the voice itself: median sentence 170 wpm, full stops a uniform ~0.4 s, and 0:51–0:59 as one breath group.

**Concision 9.** 495 words, and nearly every sentence carries a step or a number that is used later. The repeated "two and a half" is the episode's anchor, and each repeat points at a different object. The one soft line is "Odds are, that includes you." (2:55.5), which pre-empts the landing; I recommend cutting it in fix 5 to fund the pauses, not because the episode is long.

**Originality 9.** The beam that balances the same eight girls twice — once by head count and once by tokens — is a memorable, teachable image, and killing the cross term "because the beam balances" ties the algebra to the picture. The C&F beat redraws the real sampling design rather than a stock network graphic.
