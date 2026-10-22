# Episode 3, review round 1 (craft critic: visual design, motion, A/V sync)

Evidence: I used the existing `review/` pack, because metrics.json (00:46) is newer than final.mp4 (00:43). I read report.md, all 13 contact sheets and these keyframes at full resolution: kf_01, 03, 05, 06, 07, 10, 14, 16, 18, 21, 22, 24, 26, 27, 28, 30, 31, 37 and 39. I also pulled extra frames with ffmpeg at 0:46.5, 0:53.5, 1:02.0, 1:54.5, 2:55.3 and 2:56.0. I measured citation cap height on kf_30 by pixel scan, read transcript_words.tsv for the ending, and read script.md, facts.md and narration.txt.

```
EPISODE: 003 — "Which Map Is Random?" (curriculum: "Randomness Looks Clumpier Than You Think")
IDEA: Pure chance leaves empty squares, so it must pile hits up elsewhere. Clumps alone are not evidence of aim; the honest test scores the whole count histogram against Poisson, and a pattern that is too even is the real fingerprint of a rule.
SCORES: Hook 8.5 · Clarity 8 · Visual 7.5 · Motion 8 · Audio 8 · Concision 7.5 · Originality 8
WEIGHTED: 7.95 → 8.0   AFTER CEILING: 8.0 (lowest 7.5 + 2 = 9.5, does not bind)
CAPS: none (no factual error found; every empirical claim carries an on-screen citation; mechanics all inside limits; the one layout-audit "allowed" overlap is internal to the typeset P(empty) equation; the 2:05.8 clearance and the 2:55.3 overlap below happen in motion, not on a held frame)
FINAL: 8.0   PASS: no
FACTS:
- Clarke 1946, J. Inst. Actuaries 72:481: 537 hits, 576 squares of 1/4 km², south London | Verified | Clarke 1946; Shaw & Shaw 2019
- Quote "...tended to be grouped in clusters." | Verified (Clarke p. 481, verbatim) | Clarke 1946
- Factories at risk if aim were precise | Verified (paraphrase) | Shaw & Shaw 2019, Significance 16(5)
- λ = 537/576 ≈ 0.93 (0.9323) | Verified | recomputed
- P(empty) = (1 − 1/576)^537 ≈ 0.3933; × 576 ≈ 227 (226.6) | Verified | recomputed
- e^−λ ≈ 0.3937 | Verified (0.39365) | recomputed
- Map A: 222 empty, 39 squares with 3+, 131 with 2+, 537/354 ≈ 1.5 | Verified against facts.md/sim.py counts (222, 223, 92, 28, 9, 2) | sim.py
- Poisson expectations 227, 211, 98.5, 30.6, 7.1, 1.6; "chance predicts 39" (39.33) | Verified | recomputed
- χ² terms 0.10+0.64+0.43+0.22+0.49+0.12 = 2.0 | Verified (sum 2.00) | recomputed from counts
- p = 0.74 (74.5% of 20,000 simulated maps ≥ 2.0; χ²₄ tail e^−1·2 = 0.736) | Verified | recomputed tail
- Map B misfit 271.7; 109 empty ≈ half of 227; 397 singles | Verified (B counts 109, 397, 70, 0, 0, 0) | recomputed
- Clarke table 229, 211, 93, 35, 7, 1; χ² = 1.17, p = 0.88 | Verified | Clarke 1946 (widely reproduced)
- "People expect chance to spread out evenly" | Verified | Falk & Konold 1997, Psych. Review 104(2):301–318
- North box 1.9 vs Clarke's area 3.7 hits/km² | Unverifiable by me (own count of Zenodo data, credited on screen as "our count · L. Shaw, 2025 · Zenodo"); plausible and honestly labelled
- "Aimed at London, too loosely to choose a street" | Verified in spirit (Shaw & Shaw on V-1 inaccuracy) | Shaw & Shaw 2019
MECHANICS: runtime 3:49.5 · wpm 161 (speech time; 186 excluding all pauses) · max silence 1.98 s (planned prediction hold, 0:09.8) · max static 3.57 s (0:45.1–0:48.7) · −14.0 LUFS / −1.8 dBTP
FIXES (highest impact first):
1. [1:41–2:09][Concision/Clarity/Audio] The P(2)→P(k) beat takes 28 s of glyph-by-glyph swaps (2:01 and 2:03 show "P(2)" and "537²" mid-swap). Whisper merged 1:48.2–2:02.7 into one run-on sentence ("...and the rest miss E to the minus lambda again 536 is almost 537 so for any k each two becomes a k"), which suggests the planned 0.6 s breath groups do not land. Compress it to about 16 s. Keep P(2) built from the picture as it is now. Then do one TransformMatchingTex in which all three "2"s become yellow "k"s at once (2!→k!, 537²→537^k, (1/576)²→(1/576)^k). Next, one transform folds 537^k·(1/576)^k into a purple λ^k. Cut the separate "537·536 ≈ 537²" side line and say it instead ("536 is close enough to 537"). Put a real 0.8 s silence before "Five thirty-six". The derivation is then shorter, rewatch-free and audibly separated.
2. [1:19–1:31, 2:17–2:25, 2:33–2:49][Visual] The 222 empty squares are filled solid saturated yellow, about 39% of map A (kf_10, kf_21, kf_22). It is the loudest thing on screen at 2:17–2:23, while the narration is about the histogram. The fill also comes back inside both thumbnails at 2:33–2:49 (kf_26, kf_27), where yellow no longer means "focus". Change the empty-square fill to YELLOW at 0.35 fill opacity with a thin yellow stroke during 1:19–1:31. When map A returns at 2:17, do not restore the fill, because the 0-bar now carries "empty". Draw the thumbnails with dots and frame only. Each of those frames then has one focal point.
3. [0:53, 1:21, 2:25][Clarity] "Gap" carries three meanings in one episode: the minimum spacing in B's rule ("rule: gap ≥ 4/5 square", kf_07), empty squares ("Those gaps force the clumps", 1:21), and observed−expected bar difference ("χ² = Σ gap²/chance", 2:25). Keep "gap" only for the bar difference. Retag B as "rule: spacing ≥ 4/5 square" (0:53, and again at 3:45 in the landing). Change the 1:21 line to "Those empty squares force the clumps."
4. [2:33–2:49][Visual/Clarity] The 20,000-map misfit histogram has no y-axis or quantity label (kf_26, kf_27), which breaks §5 "every axis carries a quantity name". The readout "χ² = ... = 271.7" at 2:45–2:49 does not name its map, while A's "p = 0.74" sits beside it at full strength (kf_27). Add a GRAY "maps" label at the top-left of the misfit axes (MathTex ≥ 26). Make the readout "χ²_A = 2.0" and then "χ²_B = 271.7", with the subscript coloured like each thumbnail's label.
5. [0:44.4–0:48.7][Motion] The episode's reveal ("I dropped every hit on map A at random, so all 39 targets are false alarms") plays over the longest static frame in the video, 3.57 s (frame at 0:46.5 is identical to 0:45). On "dropped every hit", clear A's dots and re-rain the same 537 positions in 1.5 s, with linear rate because it is time-like and the counter running 0→537. The proof is then shown, not asserted, and the static stretch disappears.
6. [2:54.6–2:56.0][Motion] When the histogram rises for the Clarke section, the aimed map's red outline bars are left behind and fade in place. At 2:55.3 they hang below the moved x-axis and cross the "hits per square" label (extracted frame). Either put the red bars in the same VGroup as the axes for the shift, or FadeOut them (0.4 s) before the chart moves.
7. [3:31–3:37][Visual] The two densities being compared sit at opposite ends of the panel. "north: 1.9 hits/km²" is a second header line about 115 px above its box, and "Clarke's area: 3.7 hits/km²" is about 600 px lower, under the rectangle (kf_37). Place "1.9 hits/km²" immediately right of the white box (buff 0.2) and "3.7 hits/km²" immediately right of the yellow rectangle, left-aligned in the same column, so the 2:1 ratio reads in one glance.
8. [2:32.5–2:36][Audio] "Pure-chance maps score worse three times in four" was transcribed as "three times than four", so the "in" is swallowed. Re-voice as "Three chance maps in four score worse" and put a 0.4 s pause before "p equals point seven four", which lands as the p label emerges.
9. [3:45.6–3:46.4][Audio] The closing line's second "picked" was transcribed as "pick" (0.24 s, 225.97–226.21), so the final payoff word probably loses its -ed into "the". Add a phoneme override or a 0.1 s gap after the second "picked", and re-check the transcript.
10. [0:17–0:24, 2:57–3:37][Visual] Citation cap height measures about 22–23 px (pixel scan of "R." on kf_30), under §5's 24 px minimum for citations. Raise the citation font size by about 10% (for example Text 18→20, or the Tex equivalent) and keep the y > −3.2 placement.
11. [1:01.2–1:03.5][Visual/Sync] On "Each bomb has a 1 in 576 chance" the right half of the frame is empty (frame at 1:02.0), and "1/576" arrives about 2 s after "Each bomb". Start the TransformFromCopy from the yellow square to "1/576" on "Each bomb".
12. [2:39–2:45][Visual] B's "109" label sits about 19 px above its bar, inside the purple 227 outline (kf_26), under the 0.15-unit clearance. Lift it to buff 0.2, or place it left of the bar.
REACHES 9 IF ALL FIXED: yes, narrowly, but only if 1–5 all land. The structure is right: hook and commit by 0:10, a measured failure (39 false alarms against 39.3 predicted), insight, honest fix, real data, limits, and a landing that rebuilds the cold open. What holds the score down is density and focus, not architecture. The middle minute (1:31–2:49) has a derivation, a χ² construction, a Monte Carlo null and map B in quick succession. Fix 1 buys the breathing room, and fixes 2–4 give each of those frames a single focal point. If fix 1 is skipped, Concision and Clarity stay at 7.5–8 and the episode cannot reach 9.
KEEP:
- The cold-open A/B maps, and the landing where Clarke's rectangle opens into map A's frame and B slides back in with the same yellow circles and the 39 red outlines (3:39–3:47). The ending re-sees the first frame exactly.
- The χ² built from the picture: the yellow gap slivers lift into their terms, fly into the readout (2:25–2:31), and A's marker then lands on the 20,000-map null (2:33–2:37).
- The aimed-map counterexample (red outline bars over the purple prediction, 2:49–2:55) followed by Clarke's real table, whose blue bars grow into the same outlines (3:07–3:19). Same chart, three datasets, one colour code.
```

## Notes by dimension

**Hook (8.5).** Both maps are on screen from frame 1, with the dots raining in. The binary question "Which one is chance?" comes at 0:08.7, and a 2 s hold with "A or B?" (0:09.8–0:11.8) makes the viewer commit. Most viewers will pick B, which is the misconception the episode needs. "Backwards." at 0:42.6 is a real turn. Tension sags during 1:31–2:09, a long derivation with no new stakes. The landing resolves the opening exactly.

**Clarity (8).** It is concrete before abstract, and every number checks out. P(empty) is computed on one specific square before λ is named, which is good 3b1b order. Deductions:
- "Gap" is overloaded (fix 3).
- "Each two becomes a k" is said faster than the glyphs can be read (fix 1).
- The p-value-by-simulation idea gets about 4 s (2:32.5–2:36) and leans on a chart with no y label (fix 4).

**Visual (7.5).** The palette is semantic and held for the whole episode: blue observed, purple chance, red flagged/aimed, yellow focus. Typography is consistent, and nothing is clipped or outside the safe area on held frames. Deductions:
- The yellow-fill dominance at 1:19–1:31 and 2:17–2:25, and in the thumbnails (fix 2).
- The unlabelled misfit axis (fix 4).
- The separated density labels (fix 7).
- Citations slightly under size (fix 10).
- The empty right half at 1:02 (fix 11).

The count shading on both maps under bright dots at 0:31–0:49 (kf_05, kf_06) is busy, B especially, but it is legible and semantically right.

**Motion (8).** Many transforms carry meaning:
- the hits counter flies into the exponent (1:07–1:09)
- "targets" lifts off and "false alarms" rises in (0:47–0:49)
- map cells fly into histogram bars (2:19)
- gap slivers become terms and then the readout (2:27–2:31)
- the London rectangle opens into map A (3:39)

Deductions:
- The static reveal at 0:45–0:48.7 (fix 5).
- The red bars left behind at 2:55.3 (fix 6).
- The aimed map is faded out rather than transformed into the London map at 2:55–2:57, which is acceptable at a beat boundary.
- The glyph-swap chain at 2:01–2:05 is too fast to track.

**Audio / sync (8).** Loudness, peak, leading/trailing silence and pace are all on target. The deictics land within ±1 s:
- "like this one" gets its red ring at 0:35
- "these purple bars" grows them at 2:11
- "39 targets and chance predicts 39" gets its brace at 2:22–2:23
- "Map B, half the expected empty squares" gets the yellow 109 bar at 2:39

Deductions: the run-on derivation delivery (fix 1) and two swallowed words (fixes 8, 9). The rate excluding pauses is 186 wpm, so the voice itself is fast and the pauses carry the pacing.

**Concision (7.5).** At 3:49.5 the episode is near the 4:00 ceiling and packs eleven beats. Little is padding, but the P(2)→P(k) chain and the "537·536 ≈ 537²" side line are a double explanation of one approximation. The stakes line repeats what the quote shows.

**Originality (8).** Clarke's flying bombs is the canonical textbook Poisson example, and A/B dot plots of "which is random" are a known demonstration. The fresh angles are the spacing-rule map B as the "too even" fingerprint, the simulated aimed map showing the opposite fingerprint, and the real V-1 data with the honest density limit. That earns an 8, but it is not yet a "share this" image.
