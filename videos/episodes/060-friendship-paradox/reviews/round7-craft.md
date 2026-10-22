# Round 7 — craft critic (visual design, motion, A/V sync; every dimension scored)

Evidence used:
- The `review/` pack. metrics.json (18:00) is newer than final.mp4 (17:59), so I reused it rather than regenerating.
- report.md, all 12 contact sheets, and these keyframes at full resolution: kf_01, 05, 10, 12, 14, 17, 19, 22, 25, 27, 30, 32, 35, 37, 38, 39.
- Extra frames I extracted with ffmpeg into /tmp/r7craft060: 0:07.0, 0:21.5, 0:45.5, 1:45.0, 2:15.0, 2:27.0, 2:41.0, 3:01.0. I also made strips at 2.5 fps over 2:59.6–3:02.8 and at 5 fps over 2:40.2–2:41.8.
- Pixel checks: contrast of "sides at ¼ scale", and the colour of the dimmed YELLOW.
- Transcript, script.md, narration.txt, facts.md, and the round-6 reviews and CHANGELOG, so I could tell what is new in this cut.
- External check: ar5iv for arXiv:1111.4503 confirms "92.7% of users have less friends than the average friend count of their friends".
- I recomputed every number from the degree list 1, 4, 4, 2, 3, 3, 2, 1.

```
EPISODE: 060 — "Why Your Friends Have More Friends Than You"
IDEA: Following a friendship lands on each girl once per friend she has, so the friend average is avg(k²)/μ = μ + σ²/μ (the cross term dies because the distances from the balance point sum to zero), which beats the person average whenever counts vary — and that is why named friends catch flu first.
SCORES: Hook 8.5 · Clarity 9 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 9 · Originality 9
WEIGHTED: 8.7 (872.5/100)   AFTER CEILING: 8.7 (lowest 8.5 + 2 = 10.5, does not bind)
CAPS: none (0 banned phrases; every empirical claim cited on screen; no overlap/clipping in settled frames, layout audit 0/197; mechanics in range)
FINAL: 8.7   PASS: no
FACTS:
- 8 girls, 10 friendships, counts 1,4,4,2,3,3,2,1; μ = 20/8 = 2.5 | Verified | Feld 1991 AJS 96(6) Table 1; recomputed
- "an Illinois high school" (Marketville, Coleman 1961) | Verified | Feld 1991; facts.md (GESIS ZA1196)
- Ring: 16 tokens, 32/16 = 2.0 | Verified | computed (labelled hypothetical)
- Real class: 20 tokens, 60/20 = 3.0; +0.5 = 20 % | Verified | Feld 1991 ("mean of 3.0"); 0.5/2.5
- Live fulcrum 2.5 → 2.7 (38/14) → 2.9 (52/18) → 3.0 (60/20) | Verified | computed layer by layer
- Sue 4×4 = 16; Σk²/Σk → avg(k²)/μ = 7.5/2.5 | Verified | Σk² = 60
- Distances ±1.5/±0.5, squares 2.25/0.25, σ² = 10/8 = 1.25 | Verified | computed (population variance)
- 4² = 2.5² + 1.5² + 2·2.5·1.5 = 6.25 + 2.25 + 7.5 = 16; avg(d) = 0 ⇒ avg(k²) = μ² + σ² = 7.5 | Verified | algebra
- μ + σ²/μ = 2.5 + 0.5 = 3.0; ring 2 + 0/2 = 2 | Verified | computed
- Facebook 2011 ~190 friends; edge-end average ⟨k²⟩/⟨k⟩ = 635; 445 > 2×190 | Verified | Ugander et al. 2011 arXiv:1111.4503
- "a few had thousands", 5,000 limit | Verified | Ugander et al. 2011
- 92.7 % (spoken "93 %") had fewer friends than their friends' average | Verified | Ugander et al. 2011 (ar5iv text, quoted above)
- C&F Harvard 2009: 319 random, 425 named; fitted lead 13.9 d; self-reported 3.2 d | Verified | Christakis & Fowler 2010 PLoS ONE 5(9) e12948
- Fits = logistic refit with shift held at 13.9 d, disclosed "logistic refit" | Verified as disclosed | sim.py, facts.md
- "One possible draw" at 3:00 (3 on Sue, 3 on Alice, 1 Pam, 1 Carol) | Verified | consistent with edges; labelled as one draw
MECHANICS: runtime 3:29.5 · wpm 155 (speech time; 140 overall; median sentence 172) · max silence 2.22 s (planned "Pick one" hold) · max static 3.70 s (2:06.7–2:10.4) · −14.0 LUFS / −2.1 dBTP · lead 0.00 s / trail 1.91 s · WER 3.6 % (all number formatting/homophones)
FIXES (highest impact first):
1. [3:00.4–3:02.0][Motion] The C&F hand-off reads as the scene falling apart. In the 2.5 fps strip, the edges and count digits vanish first, then eight empty BLUE rings and loose tokens drift, then for ~0.8 s the frame holds only the floating labels "random" and "named friend" (f 3:01.2) and a lone x-axis line (f 3:01.6). Only after that does the chart appear. The intended correspondence (girls → BLUE curve origin, token pile → YELLOW origin) is invisible because the destination does not exist while they shrink. Change: draw the axes first, at 2:59.5, over 0.6 s and in the network's empty right half or behind it at 30 %. Then shrink the 8 nodes into the BLUE origin dot and the 8 tokens into the YELLOW origin dot in one 1.2 s move with path_arc, keeping each node's count digit until it has merged. No frame may show fewer than the axes plus the two labels.
2. [1:31–2:04, 3:09–3:20][Visual] Dimmed YELLOW stops reading as YELLOW and becomes a separate brown hue, which breaks the one-hue-one-meaning palette. Two places show it. The 3.0 fulcrum and the parked avg(k²)/μ row at 50 % (kf_17, kf_19) read khaki/brown. The raw friends' flu steps at 60 % (kf_37) measure RGB (159,128,68), an ochre clearly unlike the label's yellow. Change: never de-emphasise YELLOW by opacity. (a) During 1:31–2:17, fade the YELLOW 3.0 fulcrum out completely and restore it at 2:17 with the result row. (b) Keep the parked row at 100 % but scale it 0.8 and move it to the bottom edge. (c) For the C&F raw steps, keep full YELLOW at stroke_width 1.5, and give the fits stroke_width 4 dashed so the fit is the heavier mark.
3. [1:31–2:17][Hook/Clarity] For about 46 s of algebra there is no open question or target on screen. The bar panel and its PURPLE "+0.5" go to 0 at 1:31 (sheet 6) and return only at 2:19. This is the only sag in an otherwise rising episode. Change: keep a small PURPLE tag "+0.5 ?" at full strength at the top-right of the safe area (x ≈ 5.6, y ≈ 3.2) from 1:31 to 2:17. On "exactly the extra half friend we measured" (2:17), fly the result row's 0.5 into it and drop the "?". Optionally prefix 1:30.8 with the single question "Where does the extra half come from?" (one question only, so not a chain).
4. [2:40.4–2:41.6][Motion] In the 5 fps strip, the copies of 190, 445 and 635 fly straight down through the axis tick labels. "190" crosses the bar's bottom edge and "400"; "635" crosses "600/800". At 2:41.0 a 60 % "635" copy sits directly under the "635" label, reading as "635 / 635". Change: dim the tick labels to 30 % 0.5 s before the flight rather than during it. Route all three copies with path_arc = −0.6 out to the right of the 800 tick and back to the row. Keep them at 0 opacity until they clear the bar's lower edge by 0.3 units.
5. [2:14.5–2:16.5][Motion] The one-move collapse has baseline jitter: mid-move, "2.5" rides about 20 px above the "+0.5" (f 2:15.0, "= 2.5 +0.5  = 3.0" with uneven spacing). Change: typeset the target "μ + σ²/μ = 2.5 + 0.5 = 3.0" first. ReplacementTransform the surviving numerator 2.5 onto the target's 2.5 glyph (same TeX) and FadeOut the ² and the denominator in place. Do the 1.25/2.5 → 0.5 swap with TransformMatchingTex, so every glyph travels on the final baseline.
6. [1:43–1:55][Audio] The densest sentence, "Split Sue's count, four, into the balance point, two and a half, plus her distance, one and a half. Squaring gives two and a half squared…", carries five numbers in ~9 s. The kit's median sentence pace is 172 wpm against the 140–165 band, and the transcript runs 1:39.9–1:49.7 as one 9.8 s segment. Each flying glyph (Sue's 4 at 1:45, her 1.5 at 1:47) lands while the next number is already being spoken. Change: insert [pause 0.4] after "four" and after "two and a half", and start each glyph flight on its own word, so every number lands before the next one is spoken.
7. [3:10–3:20][Visual] The lead read-out "C&F fitted lead: 13.9 days ←" sits at the top-right (≈1330,100 px), about 700 px from the in-chart arrow it measures (≈860,598 px, kf_37). After the arc, nothing ties them together. Change: place the read-out block left-aligned at the arrow's x (≈ x = −1.0 units) just above the plot title, so the copied arrow travels straight up 2 units. Keep the self-reported row directly under it with tips aligned, as now.
8. [2:55–3:00][Visual/Clarity] "random" stays on Jane alone, yet at 3:00.5 every node wears the thick BLUE ring and every girl sends a token (kf_35). The label says one girl is random while the picture says all eight are. Change: on "Named friends", replace Jane's "random" with a caption under the network: "every girl names one friend" (Text 22, GRAY). Keep "named friend" in YELLOW at the pile.
9. [1:38–2:17][Visual] "sides at ¼ scale" is dimmed to a measured 2.4:1 contrast (kf_19), yet it is the only thing explaining why 1.5-long distances make 0.375-wide squares. Change: hold it at 70 % (≥ 4.5:1) until the picture moves back.
REACHES 9 IF ALL FIXED: yes, narrowly. Fixes 1, 4 and 5 lift Motion to 9. Fixes 2, 7, 8 and 9 lift Visual to 9. Fix 3 removes the mid-episode sag and lifts Hook to 9. Fix 6 lifts Audio to 9. That gives 9.0 weighted with the other dimensions unchanged. No structural change is needed. The misconception hook, the ring check, the measured +0.5 failure, the beam proof, two cited payoffs with an honest limit, and the landing on the 0:11 frame are all in place.
KEEP: (1) The token-weighted beam whose YELLOW fulcrum slides 2.5 → 2.7 → 2.9 → 3.0 as each layer lands, then the signed distances merging into the 0 that replaces avg(d) (1:06–2:03). (2) The friend bar as a YELLOW outline filled BLUE to μ and PURPLE beyond, carried unchanged to Facebook 190 + 445 = 635 (kf_32). (3) The landing: the cold-open candidates return, Betty's token lands on Sue reading 4, and the bar grows to the ringed 3 (kf_39).
```

## Notes by dimension (evidence)

**Hook 8.5.**
- Frame 0 (kf_01) already poses the question: the network plus ghost rows "average girl / average friend ?".
- The candidates 2.5 / 3 / 4 are up by 0:11 (kf_05), and "Pick one" is followed by a 2.2 s hold (0:12.1–0:14.3). The viewer commits by 0:12.
- The stakes sentence is done by 0:20.7, and the ending re-sees the 0:11 frame and rings the 3 (kf_39). Those meet the 9 anchor.
- Held at 8.5 for one reason: 1:31–2:17 is ~46 s of derivation with the measured gap removed from screen. That is the "slight sag midway" of the 8 anchor (fix 3).

**Clarity 9.**
- Concrete before abstract throughout. The guess is tested where it holds (ring, 0:27–0:42), then fails by a measured +0.5 · 20 % (0:53, sheet 3). The cause is named ("piled up unevenly") before any symbol.
- The beam turns Σk²/Σk into a balance point, and the read-outs are exact.
- The cross-term cancellation is derived from the balance condition, not asserted (1:55–2:03).
- Every number recomputes.
- The one step a viewer might replay is 1:55 → 1:57: Sue's specific expansion becomes the averaged identity in one swap. It is carried by "Every girl splits this way" with all nodes flashing, which is enough.

**Visual 8.5.**
- Clean dark ground, a consistent semantic palette (BLUE once-counted, YELLOW reached-by-friendship, PURPLE spread), and safe area held. "σ² = 10/8 = 1.25" ends at x ≈ 1808 px, inside 1824.
- No settled overlaps; labels are at 34 px or more.
- Deductions:
  - dimmed YELLOW turning brown, at 1:31–2:04 and 3:09–3:20 (fix 2);
  - the C&F read-out detached from its arrow (fix 7);
  - the single-"random" mislabel at 3:00 (fix 8);
  - the 2.4:1 explanatory tag (fix 9).
- kf_27 (2:23) is much improved over round 6: only the ring and its 2 + 0/2 = 2 are at full strength.

**Motion 8.5.**
- Almost every move encodes a relation:
  - counts fly from nodes into the girl bar (0:07);
  - tokens ride edges and read the count where they land;
  - the fulcrum slides as layers grow;
  - distances drop and shrink into squares;
  - the signed labels merge into a 0 that replaces avg(d);
  - the rebuilt row holds about 4 s before one collapse;
  - Facebook's source, label and axis change on one cue;
  - the 13.9-day arrow is copied and shrinks to 3.2 with a live number.
- Static stretches peak at 3.7 s.
- Deductions:
  - the C&F hand-off empties the frame (fix 1);
  - flight copies crash through tick labels and double "635" at 2:41 (fix 4);
  - baseline jitter in the 2:15 collapse (fix 5).

**Audio 8.5.**
- Measurements: −14.0 LUFS, −2.1 dBTP, 155 wpm on speech time, 0 banned phrases, WER 3.6 % (formatting only).
- Pauses are planned: the prediction holds at 0:12 and 2:36, and there are reading pauses at 1:36, 2:08 and 2:23.
- Deictics land:
  - "Sue holds four tokens" with the box (1:13);
  - "her distance" with d = k − μ (1:51);
  - "add to zero" with the signed labels (1:59);
  - "a few had thousands" with the brace (2:31);
  - "With no spread" with the ring thumbnail (2:21);
  - "sees four" with Betty's token (3:23).
- Deduction: the number-dense split sentence at 1:43–1:52 runs ahead of its glyph flights (fix 6). The median sentence pace is 172 wpm.

**Concision 9.**
- 494 words in 3:29. Every beat does work: the ring is needed for the "no spread, no gap" callback at 2:20, and the 93 % line pays off the title's "you".
- The nine repeats of "two and a half" are deliberate anchors, each tied to a visible 2.5.
- I could not name a sentence whose removal loses nothing.

**Originality 9.**
- The episode avoids the stock "Strogatz explainer" frame by making Σk²/Σk physical: a token-weighted balance beam whose fulcrum moves, then the cross-term killed by the beam's own balance.
- The token machine is now carried into C&F's sampling design at 3:00 ("one possible draw").
- Feld's eight girls and Facebook's 190/635 are canonical examples, but the image is the episode's own and memorable.
