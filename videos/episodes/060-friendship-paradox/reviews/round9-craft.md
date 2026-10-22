# Round 9 — craft critic (visual design, motion, A/V sync; every dimension scored)

Evidence used:
- The `review/` pack. metrics.json (21:38) is newer than final.mp4 (21:36), so I used the existing pack and did not regenerate it.
- report.md, narration_diff.txt, metrics.json, transcript.txt and transcript_words.tsv, narration.txt, script.md, facts.md, CHANGELOG (round 8 section).
- All 12 contact sheets.
- Full-resolution keyframes kf_01, 05, 11, 14, 18, 20, 22, 26, 28, 31, 33, 34, 35, 37, 39 and 40.
- Extra strips I extracted with ffmpeg into the scratchpad (`r9c/`):
  - 2.5 fps: 0:19.6–0:22.8 (guess box), 0:59.6–1:03.2 (sort), 1:23.8–1:26.2 (divide step), 1:36.0–1:40.8 (distances to squares), 2:41.6–2:44.8 (635 reveal), 2:55.6–2:58.8 (Facebook to C&F), 3:04.6–3:08.2 (C&F hand-off), 3:26.4–3:30.4 (landing);
  - 10 fps: 1:38.4–1:39.6 (the squares being born).
- Web check of the PLoS ONE page for C&F (3.2 days self-report) and of Ugander et al. 2011 (92.7 %, 635), on top of the quotes logged in facts.md.
- I recomputed every network number from the degree list Betty 1, Sue 4, Alice 4, Jane 2, Dale 3, Pam 3, Carol 2, Tina 1, which matches the 10 edges drawn at kf_05.

```
EPISODE: 060 — "Why Your Friends Have More Friends Than You"
IDEA: Following a friendship lands on each girl once per friend she has, so the friend average is avg(k²)/μ = μ + σ²/μ (the cross term dies because the distances from the balance point sum to zero), which beats the person average whenever friend counts vary; that is why the friends that people name catch flu first.
SCORES: Hook 9 · Clarity 9 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 9 · Originality 9
WEIGHTED: 8.8 (135 + 225 + 127.5 + 127.5 + 85 + 90 + 90 = 880 / 100)   AFTER CEILING: 8.8 (lowest 8.5 + 2 = 10.5, does not bind)
CAPS: none. 0 banned phrases or patterns. Every empirical claim has an on-screen citation (Feld/Coleman, Ugander, C&F). Layout audit 0/214 and no overlap seen in any settled frame I read. Runtime, pace, silences, static stretches and loudness are all in range.
FINAL: 8.8   PASS: no
FACTS:
- 8 girls, 10 friendships, counts 1,4,4,2,3,3,2,1; μ = 20/8 = 2.5 | Verified | Feld 1991 AJS 96(6) Fig. 1 / Table 1 (Coleman 1961); recomputed
- "an Illinois high school" | Verified | Coleman's 10 northern-Illinois schools (facts.md: GESIS ZA1196, Brookings 2017)
- Ring: 16 tokens, 32/16 = 2.0 | Verified | computed; tagged "(hypothetical)"
- Real class: 20 tokens, 60/20 = 3.0; 15/5 and 58/19 shown as live partial counts; +0.5 = 20 % of 2.5 | Verified | computed
- Fulcrum 2.5 → (2.8 seen mid-move at 1:09) → 3.0 | Verified | the layer sums give 38/14, 52/18, 60/20
- Sue 4 × 4 = 16; Σk² = 60; Σk²÷8 / Σk÷8 = 7.5/2.5 = 3.0 | Verified | computed
- Distances ±1.5/±0.5; squares 2.25/0.25; σ² = 10/8 = 1.25 (population variance); square sides 84 px and 27 px = ¼ of the ruler lengths 325 px and 108 px (kf_18) | Verified | computed; measured
- 4² = (2.5 + 1.5)² = 2.5² + 1.5² + 2·2.5·1.5; avg(d) = 0 ⇒ avg(k²) = μ² + σ² = 6.25 + 1.25 = 7.5 | Verified | algebra
- μ + σ²/μ = 2.5 + 0.5 = 3.0; ring 2 + 0/2 = 2 | Verified | computed
- Facebook, May 2011: mean ≈ 190 friends; ⟨k²⟩/⟨k⟩ = 635; 445 > 2 × 190 | Verified | Ugander, Karrer, Backstrom & Marlow 2011, arXiv:1111.4503
- "a few had thousands"; 5,000 cap | Verified | Ugander et al. 2011
- 92.7 % (spoken "93 %") of users below their own friends' average | Verified | Ugander et al. 2011, "Degree correlations"
- Bars are drawn to scale: 190 → 64 px, 635 → 214 px on a 270 px per 800 axis (sheet 10) | Verified | measured
- C&F, Harvard, fall 2009: 319 random students, 425 named friends; fitted lead 13.9 d (95 % CI 9.9–16.6); self-reported 3.2 d (95 % CI 2.2–4.3) | Verified | Christakis & Fowler 2010, PLoS ONE 5(9) e12948
- In-chart arrow ≈ 14 days at the chart's own day scale (kf_37, 3.39 px per day on the sheet) | Verified | measured; the "logistic refit" is disclosed in the citation
- "Most of us are Betty": 5 of the 8 girls and 92.7 % of Facebook users are below their friends' average | Verified | Feld 1991 p. 1465; Ugander et al. 2011
MECHANICS: runtime 3:33.3 · wpm 156 (speech time; 141 overall; median sentence 172) · max silence 2.22 s (the planned "Pick one" hold at 0:12.1; the landing pause is 2.2 s) · max static 2.67 s · −14.0 LUFS / −2.1 dBTP · leading 0.00 s / trailing 1.70 s · WER 0.6 %
FIXES (highest impact first):
1. [1:38.6–1:40.0][Motion] The central variance move runs backwards and too fast.
   - The squares do not come from the distances. At 10 fps the eight squares grow out of points under the girls in about 0.3 s (1:38.7 dots, 1:39.0 full squares), which is under the 0.4 s floor for anything the viewer must track. Only after that (1:39.1–1:39.5) do copies of the PURPLE distance segments fall onto the squares' top edges. "Square it" (spoken 1:38.6–1:39.2) therefore shows squares appearing first and the distances arriving later, which is the reverse of the script's plan ("the segment drops to her square's top edge, the square grows down from it").
   - Change, in this order:
     - On "square" (1:38.6), drop the eight ¼-scaled distance copies first: 0.5 s, lag 0.05.
     - Then grow each square down from its copy, using that copy as the top edge (GrowFromEdge(UP) or a stretch from the edge): 0.8 s, smooth.
     - Then write the areas: 0.4 s.
     - Everything ends by about 1:40.5, inside the existing 1.6 s pause, so no re-timing is needed.
   - This is the one picture where "variance is the average squared distance" becomes visible. It needs to read as length → area.
2. [1:36.0–1:38.6, kf_18/kf_20][Visual/Clarity] The four distances are drawn on top of each other.
   - On the ruler they read as one continuous PURPLE line from 1 to 4, with "1.5 / 0.5 / 0.5 / 1.5" sitting over the tick endpoints. The 1.5 segment visibly contains the 0.5 segment, so the viewer never sees four separate lengths to square. The 10 fps strip shows that the dropping copies overlap too (1:39.1).
   - Change: draw each girl-pair's distance as its own segment in one of two lanes just above the ruler:
     - the ±0.5 distances at +0.10 above the ruler;
     - the ±1.5 distances at +0.24 above the ruler;
     - each label centred over its own segment, at least 0.15 clear of the 2.5 label.
   - Keep the ruler itself GRAY. Fix 1's copies then come from separate, unambiguous segments, and the signed relabel at 2:03 (−1.5 … +1.5) reads as four vectors that cancel.
3. [1:24.6–1:25.4][Motion] The step that turns a sum into an average flashes an empty numerator.
   - "Σk² ÷ 8" and "60 ÷ 8" fade out, the numerator is blank at 1:25.0 (sheet 5 and the 2.5 fps strip), and then "avg(k²)" and "7.5" fade in. The denominator does the same at 1:27–1:29.
   - That is the episode's "÷ 8 means average" moment, and it is told as a disappearance.
   - Change: use the toolkit's swap()/carry() so that "Σk² ÷ 8" shrinks into its slot while "avg(k²)" grows from the same centre (0.6 s, no frame without a numerator), and the same for 60÷8 → 7.5 and Σk÷8 → μ. Flash the "÷ 8" in BLUE as it is absorbed, for ≤ 1 s.
4. [2:56.4–2:57.2][Motion/Visual] The Facebook → C&F change passes through an empty frame while "Christakis and Fowler" is spoken.
   - At about 2:56.8 the whole frame is background (dip strip, frame 4).
   - On the way out, the YELLOW 635 and its outline fade through olive (2:56.4), which breaks the series' own "YELLOW never fades" rule.
   - Change: shrink the YELLOW elements out at full colour (shrink_out), and start the class FadeIn 0.3 s before the Facebook panel finishes leaving, so that every frame holds at least the network's nodes.
   - Better still, morph the BLUE "average user" bar down into the class's BLUE nodes (a BLUE → BLUE correspondence), so the cut becomes a transform.
5. [1:15.0–1:33.0][Visual] "4 × 4 = 16" (YELLOW, top) stays on screen for about 18 s.
   - It is relevant only on "sixteen" (1:15). Through the whole Σk²/Σk build it is a second YELLOW focal point competing with the equation (kf_14, sheet 5).
   - Change: on "adds k squared on top" (1:17.5), fly a copy of its 16 into the Σk² numerator (TransformFromCopy, 0.8 s), then shrink the label out. That also gives Σk² a visual referent, which BAR §5 asks for.
6. [0:00–0:10.7, 1:12–1:30][Audio] The delivery is fast between pauses.
   - The median sentence runs at 172 wpm, above the 140–165 natural band.
   - The cold open runs 10.7 s with no breath ≥ 0.35 s; only 0.3 s follows "every friendship between them" (0:04.4).
   - The derivation's 20 s window from 1:10.8 carries 6 different numbers.
   - Change:
     - add [pause 0.4] after "every friendship between them.";
     - set speed 0.78 (from 0.82) for "Sue holds four tokens, each worth four: sixteen." and "Now divide top and bottom by the eight girls …";
     - add [pause 0.4] after "sixteen."
   - This adds about 1.5 s, so the runtime stays under 3:35.
7. [3:01–3:04.4, kf_35][Visual] The C&F tokens crowd their rings.
   - Betty→Sue's "4" is about 10 px from Sue's YELLOW ring, and Jane→Dale's "3" is about 15 px from Dale's ring, both under the 20 px spacing standard.
   - Change: park each token at 45 % of the edge length measured from the receiver's centre (not tucked under the ring), and re-run the clearance assert against the thicker 0.08 rings.
8. [3:33.0–3:33.3][Visual, nitpick] The end card is still mid-fade on the last frame of the video at 3:33.0 (sheet 12).
   - Change: if the trailing-silence budget allows (it is 1.70 s against a 2 s limit), hold the finished card for 0.25 s.
REACHES 9 IF ALL FIXED: yes. Fixes 1–4 remove the remaining motion that does not encode a relation (Motion 9). Fixes 2, 4, 5 and 7 leave one focal point and clean spacing in every frame (Visual 9). Fix 6 brings the cadence into the natural band (Audio 9). That gives a weighted score of 9.0, and no structural change is needed.
KEEP: (1) the token-weighted beam, whose fulcrum slides from the BLUE 2.5 to the YELLOW 3.0 as each layer lands. (2) The cross term dying as the signed distances slide into a PURPLE 0 under the balance point, with the "+0.5 ?" target answered at 2:21. (3) The YELLOW-outline / BLUE / PURPLE friend bar carried from the class to Facebook (190 + 445 = 635) and into the silent landing that accounts for all three candidates (2.5 counts the girls, 3 counts the tokens, 4 is what Betty sees).
```

## Notes by dimension

**Hook 9.**
- Frame 0 already poses the question: the dimmed network and a YELLOW "?" (kf_01).
- By 0:09–0:11 the candidates 2.5 / 3 / 4 sit on the axis under drop lines, and "Pick one" is followed by a 2.2 s hold. The viewer commits by 0:12.
- The stakes line (0:14–0:20) is paid off exactly by the C&F beat, and the landing (3:25–3:31) returns to the cold-open frame and resolves every candidate.
- Nothing to change here.

**Clarity 9.**
- The episode goes concrete before abstract throughout: tokens, then the count, then the beam, then Σk²/Σk, then avg(k²)/μ.
- Its hardest step, why avg(k²) = μ² + σ², is shown rather than asserted. Sue's split, the boxed cross term, and the distances summing to 0 "because the beam balances" are all on screen (2:01–2:07).
- The honest limits are stated: the C&F lead shrinks from 13.9 to 3.2 days for self-reports, and the ring shows that zero spread gives no gap.
- The weak spot is visual, not logical. The overlapping distance segments and the squares that appear before their sides (fixes 1–2) are the one place a viewer has to take "average squared distance" on faith.

**Visual 8.5.**
- The palette is held all the way through: BLUE for people, YELLOW for tokens and the friend average, PURPLE for spread, GRAY for guess and axes, INK for highlights.
- Type sizes are generous and the safe area is respected (the "+0.5 ?" target at x ≈ 1780 px and σ² at 1808 px are both inside 1824 px).
- Below 9 because of:
  - the superimposed distances (kf_18);
  - the lingering "4 × 4 = 16" (1:15–1:33);
  - the empty frame at 2:56.8;
  - tight token clearances at 3:04.
- Each is minor, but together they exceed the "nothing to remove" bar.

**Motion 8.5.**
- Most moves carry meaning:
  - tokens travel both ways along the edges and read the count where they land;
  - the girls sort onto the beam on nested arcs with no collisions (strip 0:59.6–1:03.2, fixed since round 8);
  - the fulcrum slides as the layers land;
  - the numbers fly into the result rows;
  - the 635 outline grows on the word (2:42.9–2:44.0);
  - the landing plays three moves cleanly in the 2.2 s silence (3:28.0–3:30.0).
- Below 9 because of:
  - the squares-before-sides inversion in under 0.4 s (fix 1);
  - two fade-swaps on the divide step (fix 3);
  - the fade through empty at the C&F change (fix 4).

**Audio 8.5.**
- Sync is excellent:
  - "four on Sue, four on Alice, one on Betty" pulse as they are named;
  - 635 appears on its word;
  - "rose first" flashes the friends' curve;
  - the "+0.5 ?" target is answered on "exactly the extra half friend we measured".
- Loudness is exactly −14.0 LUFS and WER is 0.6 %.
- The deduction is for measured pace between pauses (median sentence 172 wpm; a 10.7 s breathless cold open), not for the voice itself.

**Concision 9.** 497 words, and every sentence carries a step or a number that is used later. The repeated "two and a half" is the episode's anchor, and each repeat points at a different object (bar, fulcrum, split, result).

**Originality 9.** The token-weighted beam is the memorable image: both averages appear as balance points of the same girls, with the cross term killed by the balance itself. The C&F illustration shows the real sampling design (random students name their friends) rather than a stock network graphic.
