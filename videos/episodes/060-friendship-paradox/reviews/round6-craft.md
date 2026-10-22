# Round 6 — craft critic (visual design, motion, A/V sync; all dimensions scored)

Evidence: `review/` pack (metrics.json 08:49 is newer than final.mp4 08:47, so reused). Read: report.md, all 12
contact sheets, keyframes kf_01, 05, 10, 16, 19, 20, 23, 25, 27, 30, 34, 39 at full resolution, plus extra frames
extracted at 0:07.0, 0:21.8, 1:14.0, 1:37.0, 1:39.5, 2:09.5, 2:10.0, 2:16.0, 2:17.5, 2:21.5, 2:28.0, 3:14.0, 3:20.5,
and 2 fps strips over 2:08–2:20 and 2:23–2:35. Glyph heights measured in pixels on the 1080p keyframes.
Transcript, script.md, narration.txt and facts.md read. External checks: Ugander et al. arXiv:1111.4503 (quote
"the average Facebook user ... around 190 Facebook friends"; "The expected number of friends at the end of a
randomly chosen edge, ⟨k²⟩/⟨k⟩ = 635"), Christakis & Fowler 2010 PLoS ONE / PMC2939797 (13.9 days, 95% CI 9.9–16.6;
self-reported 3.2 days).

```
EPISODE: 060 — "Why Your Friends Have More Friends Than You"
IDEA: Following a friendship lands on each girl once per friend she has, so the friend average is avg(k²)/μ = μ + σ²/μ, larger than μ whenever friend counts vary — which is why random people's named friends get flu earlier.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 8.5
WEIGHTED: 8.4 (842.5/100)   AFTER CEILING: 8.4 (lowest 8 + 2 = 10, not binding)
CAPS: none (every empirical claim has an on-screen citation; no overflow/overlap in settled frames; 0 banned phrases; mechanics in range)
FINAL: 8.4   PASS: no
FACTS:
- 8 girls, 10 reciprocated friendships, counts 1,4,3,2,4,3,2,1; μ = 20/8 = 2.5 | Verified | Feld 1991 Table 1; recomputed from the edge list
- Ring: 16 tokens, 32/16 = 2.0 | Verified | computed
- 20 tokens sum to 60, friend average 3.0, +0.5 = 20 % | Verified | Feld 1991 ("Mean 3, for 20 friends")
- Token-layer fulcrum read-outs 2.7 (38/14), 2.9 (52/18), 3.0 (60/20) | Verified | computed
- Sue 4×4 = 16; Σk²/Σk → avg(k²)/μ = 7.5/2.5 | Verified | computed
- Distances 1.5/0.5, squares 2.25/0.25, σ² = 10/8 = 1.25 | Verified | computed
- 4² = 2.5² + 1.5² + 2·2.5·1.5 (6.25+2.25+7.5 = 16); Σd = 0 so cross terms vanish; avg(k²) = μ² + σ² = 7.5 | Verified | algebra
- μ + σ²/μ = 2.5 + 0.5 = 3.0; ring 2 + 0/2 = 2 | Verified | computed
- Landing: friends' averages Betty 4, Jane 3.5, Dale 3.33, Pam 3.33, Tina 2, Sue 2.75, Alice 3; five fewer, Sue and Alice more (Carol ties, unmentioned) | Verified | Feld 1991 p. 1465, recomputed
- "Illinois high school" (Marketville, Coleman 1961) | Verified | Feld 1991 Fig. 2 caption; facts.md
- Facebook 2011: ~190 friends; edge-end average 635; σ²/μ ≈ 445 > 2×190 | Verified | Ugander et al. 2011 arXiv:1111.4503 (quoted above)
- "A few users had thousands", 5,000 limit | Verified | Ugander et al. 2011
- C&F: Harvard 2009, 319 random students, 425 named friends, diagnosed-flu fitted lead 13.9 days, self-reported 3.2 days | Verified | Christakis & Fowler 2010 PLoS ONE 5(9) e12948
- Named friends more central (higher in-degree/betweenness) so infected sooner | Verified | C&F 2010 Results, Fig. 1 caption
- Fits are a logistic refit with shift held at 13.9 days (labelled "logistic refit") | Verified as disclosed | sim.py / facts.md
MECHANICS: runtime 3:33.3 · wpm 160 (speech time; 152 overall) · max silence 2.23 s (planned "Pick one" hold) · max static 2.60 s · −14.0 LUFS / −2.1 dBTP · lead 0.00 s / trail 1.81 s · WER 0.8 % ("divide" dropped by Whisper but spoken: RMS −14.7 dB over 1:24.5–1:25.1)
FIXES (highest impact first):
1. [2:09–2:19][Motion/Clarity] The algebra collapse changes state six times in ~9 s (2 fps strip): 2:09.0 7.5/2.5 row → 2:10.5 (μ²+σ²)/μ = (2.5²+1.25)/2.5 → 2:12.5 split → 2:14.5 μ²/μ boxed → 2:16.0 2.5²/2.5 boxed → 2:17.5 1.25/2.5 → 0.5. The seven-term (μ²+σ²)/μ row holds ~2 s against the §5 minimum of 2 s + 0.4 s/term ≈ 4.8 s, and this is the one transition a viewer will need to rewatch. Change: add a 1.2 s pause after "mu squared plus sigma squared" (2:11.6) so the rebuilt row holds ≥ 3.5 s; then do the three collapses (μ²/μ → μ, 2.5²/2.5 → 2.5, 1.25/2.5 → 0.5) in ONE TransformMatchingTex (run_time 1.5) on "Here that's two and a half plus a half", so the split row μ²/μ + σ²/μ = … holds ≥ 3 s before it collapses.
2. [2:22–2:27][Visual] kf_27 (2:26.1): beam + names + fulcra, distance line + labels, eight squares, ring thumbnail + "2 + 0/2 = 2", both bars + "+0.5 · 20%", the main row and the citation are all at full strength — seven groups, no focal point, while the narrator has already moved on to "In 2011, Facebook". Change: in the closing pause brighten only the main row μ + σ²/μ = 2.5 + 0.5 = 3.0 and the bars; leave the beam, squares and ring at 30 %, then clear them as Facebook starts.
3. [2:25.7–2:29.5][Sync/Motion] "In 2011, Facebook users averaged…" is spoken while the bars still read "average girl 2.5 / average friend 3.0" on a 0–4 axis, under a citation that already says "Ugander et al., 2011 … (Facebook, May 2011)" (f 2:28.0, sheet 9 at 2:27). The data and its source disagree for ~2.5 s. Change: swap the citation in the same AnimationGroup as the label change "average girl" → "average user" and the axis rescale, and start that group on "Facebook" (2:26.6) rather than after "users averaged".
4. [2:00–2:07][Visual] Highlight boxes still hug their glyphs: around "2μ·avg(d)" at 2:01.6 the "2" sits ~8 px and ")" ~6 px from the box (zoomed crop), against the 20 px (0.15 unit) spacing standard. Change: SurroundingRectangle(term, buff=0.15, corner_radius=0.08) for both cross-term boxes and the μ²/μ, 2.5²/2.5 cancel boxes (2:14–2:16).
5. [1:39–2:19][Clarity/Visual] "sides at 1/4 scale" is shown only 1:38–1:42 at ~24 px ascender height and then removed; afterwards the 0.6-unit squares sit under 2.4-unit distance segments with nothing saying why their sides differ. The area labels 2.25/0.25 (26 px) also leave for good at 1:43. Change: keep the tag at 40 % under the squares until the picture moves back at 2:19, as MathTex(r"\text{sides at }\tfrac14\text{ scale}", font_size=30); set distance labels and area labels to MathTex font_size 36.
6. [0:00–0:05][Hook] Frame 0 (kf_01) is eight dim circles and names with no edges, no number and an empty right half; the puzzle text arrives at 0:08–0:11. Change: open with the edges at 40 % and the "average girl / average friend ?" rows as 30 % ghosts in the right panel, so the first frame already poses the question; keep all existing beat timings.
7. [2:52–3:06][Originality] The Harvard payoff is narrated over a redrawn chart; the episode's own machine (tokens) is absent exactly where C&F's design *is* "follow one friendship". Change: on "Named friends have more friends" run a 3 s inset: eight BLUE dots labelled "random" each send one YELLOW token along an edge; the tokens pile on the two high-degree nodes; the pile then flies to the origin of the YELLOW curve. This is the single change most likely to lift Originality to 9.
8. [1:36.5–1:37.5][Motion] The distance-segment copies drop straight through the "1.5"/"0.5" labels (f 1:37.0 shows the purple copies striking the label tops). Change: dim the four labels to 40 % for the 0.6 s of the drop, or start the copies 0.3 units below the label row.
9. [3:18–3:25][Clarity] "Five have fewer… only Sue and Alice have more" accounts for 7 of 8; Carol (2 vs 2) is the only node with no label (f 3:20.5). Change: give Carol a GRAY "2" label on "Only Sue and Alice", so the tie is visible without narration.
10. [3:13–3:17][Visual] The self-reported arrow and its "self-reported:" label are GRAY, the hue declared for the naive guess and axes. Change: draw it in INK at 50 % opacity (it is the same measurement type as the INK 13.9-day arrow, only smaller).
11. [1:37.6–1:41.4, 3:16.8][Concision] "Two and a quarter at the ends, a quarter in the middle" restates the on-screen area labels, and "Back to the eight girls." restates the cut. Change: cut both sentences (about 4 s); let the squares' labels pop in time with "square it", and start the landing on "Seat by seat" as the class fades in.
REACHES 9 IF ALL FIXED: yes, narrowly, and only with every fix. Fixes 1, 4, 5, 8 lift Motion, Visual and Clarity to 9; fix 2 removes the last cluttered frame; fix 3 makes every deictic land, lifting Audio to 9; fix 6 lifts Hook to 9; fix 11 lifts Concision to 9. That alone is 895/100 ≈ 8.95, a borderline round. Fix 7 (tokens carried into the Harvard payoff) is required to move Originality to 9 and give a safe 9.0. No structural rewrite is needed: the hook, the measured failure, the beam proof, two cited payoffs with an honest limit, and the landing that re-sees the 0:11 frame are all in place.
KEEP: (1) The token-weighted balance beam whose YELLOW fulcrum slides 2.5 → 2.7 → 2.9 → 3.0 as layers land, then the signed distances merging into the 0 that kills the cross term (1:10–2:07). (2) The friend bar as a YELLOW outline filled BLUE to μ and PURPLE beyond, carried unchanged to Facebook (190 + 445 = 635). (3) The landing: the cold-open candidates return, Betty "sees four", and the bar grows to the ringed 3 (kf_39).
```

## Notes by dimension (evidence)

**Hook 8.5.** Question "How many friends does the average friend have? Pick one." at 0:08–0:11 with YELLOW candidates 2.5 / 3 / 4 and a 2.2 s hold (0:11.7–0:14.0): commitment by 0:12. Stakes in one sentence by 0:22. The ending re-sees the 0:11 frame and rings the 3. Deductions: frame 0 is near-empty (kf_01); tension sags across the 50 s algebra stretch 1:33–2:24, which has no open question on screen.

**Clarity 8.5.** Textbook-quality order: the naive guess is tested where it works (ring, 0:28–0:44), then fails by a measured +0.5 (0:44–0:57), and the cause (tokens pile on Sue and Alice) is named before any symbol. The cross-term cancellation is derived from the beam balancing, not asserted. Every number checks out. Deductions: the 2:09–2:19 collapse is too fast to follow on one watch (fix 1); the ¼-scale squares lose their explanation after 1:42 (fix 5).

**Visual 8.** Semantic palette is held across all 3:33 (BLUE person-once, YELLOW reached-by-friendship, PURPLE spread, INK emphasis), safe area respected (layout audit 0 issues, 194 checks; "Facebook's limit" right edge at x ≈ 1768 px, inside 1824). Deductions: the cluttered 2:23–2:27 summary frame (kf_27), tight boxes (2:01, 2:14–2:16), small secondary labels (beam names 26 px, area labels 26 px, scale tag ~24 px — at the tick-grade floor, below the 34 px label grade), GRAY reused for a data arrow at 3:13.

**Motion 8.5.** Most moves encode a relation: node counts fly into the girl bar (0:06–0:09), tokens travel along edges, the fulcrum slides as layers land, distances shrink into squares, signed labels merge into 0 and that 0 replaces avg(d), Facebook numbers fly into 190 + 445 = 635, the 13.9-day arrow is copied to the read-out and shrinks to 3.2 with a live number. Deductions: algebra pacing (fix 1), segment copies striking labels at 1:37, and the 2.5 s period at 2:26–2:29 where the Facebook beat runs over girl data.

**Audio 8.5.** 160 wpm, −14.0 LUFS, −2.1 dBTP, WER 0.8 %; pauses are placed (prediction holds at 0:11.7 and 2:35.9, 2.1 s closing pause at 2:24). Deictics land: "Sue holds four tokens" with the box at 1:17; "her distance" with d = k − μ at 1:51; "add to zero" with the signed labels at 2:03; "a few users" with the brace at 2:41. One deictic lags: "Facebook users" at 2:26.5 over girl bars until 2:29.5 (fix 3). Kokoro cadence remains slightly even on list sentences ("one, two, three, or four").

**Concision 8.5.** 509 words; nearly every sentence carries a step. Slack: "Back to the eight girls." (3:16.8) and the double statement "Measure each girl's distance … and square it. Two and a quarter at the ends, a quarter in the middle" partly duplicates the area labels.

**Originality 8.5.** The tokens-and-beam proof of avg(k²) = μ² + σ² by balance is a non-obvious, memorable image. Held back because Feld's eight girls and the Facebook 190/635 pair are the canonical examples (also Strogatz, NYT 2012), and the payoff does not reuse the token machine (fix 7).
