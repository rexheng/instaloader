# Review, round 4 (craft critic: visual design, motion, A/V sync; every dimension scored)

**Evidence used**
- The existing `review/` pack. Its metrics.json (00:53) is newer than final.mp4 (00:51), so I reused it rather than regenerating.
- I read report.md, all 13 contact sheets, transcript.txt, transcript_words.tsv, narration_diff.txt, script.md, narration.txt, facts.md, the CHANGELOG and the round-3 craft review.
- Full-resolution keyframes read: kf_01 (0:00.3), kf_03 (0:07.9), kf_05 (0:32.4), kf_08 (0:52.9), kf_10 (1:13.3), kf_16 (1:44.2), kf_19 (2:04.8), kf_21 (2:13.1), kf_25 (2:23.3), kf_27 (2:29.4), kf_30 (2:47.4), kf_34 (3:14.8), kf_36 (3:24.1) and kf_38 (3:32.4).
- Extra frames I pulled with ffmpeg:
  - 1:03.4, 1:04.6 and 1:05.6 (the Sue, Alice and Betty pulses);
  - 1:55.0 and 1:55.4 (the 1.5 flight);
  - 1:56.6–1:57.8 (the bracket expansion);
  - 2:00.0–2:02.8 (the cross-term box);
  - 2:08.6–2:09.4 (avg(d) → 0);
  - 2:16.4–2:18.0 (the split and cancel);
  - 2:42.3 and 2:43.2 (the Facebook reveal).
- Pixel measurements: cap heights of the small labels, and the box-to-glyph gaps at 2:01.6 and 2:04.8.
- Sources: I re-checked Ugander et al. by direct quote from arXiv:1111.4503 ("⟨k²⟩/⟨k⟩ = 635"; n ≈ 721 million) and recomputed every network number from the edge list myself.

```
EPISODE: 060 — "Why Your Friends Have More Friends Than You"
IDEA: Following a friendship lands on each girl once per friend she has, so the average friend has Σk²/Σk = μ + σ²/μ friends (the cross terms vanish because the distances from the balance point sum to zero), which exceeds the average person whenever counts vary; the friends of random Harvard students caught a real flu outbreak early.
SCORES: Hook 8.5 · Clarity 9 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 8.5
WEIGHTED: 8.6 (862.5/100)   AFTER CEILING: 8.6 (lowest 8.5 + 2 = 10.5, does not bind)
CAPS: none. The layout audit is clean (0/198). No held overlap or clipping. The closest case: the cross-term boxes at 2:00–2:09 sit 4–9 px from their glyphs, under the 20 px §5 clearance but not overlapping, so it is a Visual deduction. 0 banned phrases. Every empirical claim has an on-screen citation. Runtime, pace and loudness are all in range.
FINAL: 8.6   PASS: no
FACTS:
- 8 girls, 10 reciprocated friendships, Marketville (Illinois), Coleman's data | Verified | Feld 1991 AJS 96(6) Fig. 1 / Table 1 (facts.md quotes); Coleman 1961
- counts 1,4,4,2,3,3,2,1 → μ = 20/8 = 2.5 | Verified | recomputed from the edge list
- 20 tokens, Σ = 60, 60/20 = 3.0; "half a friend too low", "20% more" | Verified | recomputed; 0.5/2.5 = 20 %
- ring: 16 tokens, 32/16 = 2.0, σ² = 0, "2 + 0/2 = 2" | Verified | recomputed
- "Sue holds four tokens, each worth four: sixteen" | Verified | 4 × 4
- ÷8 → 7.5/2.5; squares 2.25 ×4, 0.25 ×4 → σ² = 10/8 = 1.25 | Verified | recomputed (population variance)
- squares drawn at exactly ¼ of the beam scale | Verified | kf_16: a 1.5 distance is 324 px on the beam; its square side is 84 px (≈ 324/4)
- 4² = (2.5 + 1.5)² = 2.5² + 1.5² + 2·2.5·1.5 = 16 | Verified | 6.25 + 2.25 + 7.5
- avg(d) = 0 → avg(k²) = μ² + σ² = 7.5; μ + σ²/μ = 2.5 + 0.5 = 3.0 | Verified | algebra
- beam fulcra: 2.5 (girls) and 3 (tokens) placed exactly | Verified | kf_10 pixel positions: girl centroid 538 px, token-weighted centroid 646 px = the count-3 position
- Facebook 2011, ≈190 friends | Verified | arXiv:1111.4503 (2 × 68.7e9 / 721e6 = 190.6)
- tokens average ≈635 (⟨k²⟩/⟨k⟩) | Verified | arXiv:1111.4503, direct quote re-checked this round
- 190 + 445 = 635; "spread term more than twice the mean" | Verified | 445 > 380
- "a few users had thousands", 5,000 limit | Verified | Ugander et al. 2011 (facts.md quote)
- Harvard 2009; 319 random students; 425 named friends | Verified | C&F 2010 PLoS ONE e12948, Methods (verified in rounds 2–3 by direct quote)
- fitted lead 13.9 days; self-reported ≈3 (3.2 on screen) | Verified | C&F 2010 Abstract and Results
- "Friends sit closer to everyone else in the network" | Verified | C&F 2010, Fig. 1 caption (centrality rationale)
- friends' averages Betty 4, Jane 3.5, Pam 3.33, Dale 3.33, Tina 2; Sue 2.75, Alice 3; Carol equal | Verified | recomputed
- "land on a Sue four times as often as on a Betty" | Verified | 4/20 vs 1/20
MECHANICS: runtime 3:41.4 · 160 wpm (speech time; 164 wpm across the 1:06–2:28 insight) · max silence 2.23 s (planned hold 0:11.7–0:14.0) · max static 2.50 s · −14.0 LUFS / −2.1 dBTP · lead 0.00 s / trail 1.49 s · WER 1.5 % · 0 banned phrases
FIXES (highest impact first):
1. [1:06–2:30, 2:44–2:52][Visual] Annotation labels sit below the §5 label minimum (34 px cap height), measured on keyframes:
   - beam names "Betty … Alice": 26 px (kf_19);
   - signed distance labels "−1.5 … +1.5": 28 px (kf_21);
   - "a few users" and "Facebook's limit": about 25 px (kf_30);
   - the ring thumbnail's node digits: about 20 px (kf_27);
   - "square side = distance, drawn at 1/4 scale": 8 words in one block (limit 7) at about 24 px, with ¼ set in small digits (kf_16).
   Change: beam names to Text(font_size=24); the nodes are 108 px apart, so "Carol" still fits. Distance labels to MathTex(font_size=36). "a few users" to Text 26 and "Facebook's limit" to Text 22. Remove the digits from the 0.42× ring thumbnail; eight plain dots plus the PURPLE centre point carry "no spread". Replace the tag with MathTex(r"\text{squares at }\tfrac14\text{ scale}", font_size=34).
2. [2:00.0–2:09.5][Visual] Both highlight boxes hug their glyphs. At 2:01.6 the right edge of "2·2.5·1.5" is about 5 px from the "5" and about 9 px from the top. At 2:04.8 the "2μ·avg(d)" box leaves 4–5 px at the "2" and the ")". The 2:01 frame reads as if the box clips the 5. Change: SurroundingRectangle(term, buff=0.15, corner_radius=0.08) for both. Keep the round-3 resize-on-shrink, recomputed with the same buff.
3. [1:55.0, 2:16.6–2:17.4][Motion] Two crossings leave glyph soup in transit.
   - 1:55.0: the 1.5 copied from Sue's distance label flies straight through the left end of the σ² row, giving a "1•" smear beside σ².
   - 2:16.8: the denominator duplicates in place ("μμ", "2255").
   - 2:17.2: the old and new "1.25" overprint ("1l25").
   Change: route the 1.5 copy below the σ² row (path_arc=-0.6, or a two-leg move through a point 0.4 units under it). In the split, shift the duplicated denominators apart in the first frame of the transform (lag_ratio 0) rather than cross-fading on top of each other. Fade the old 1.25 out completely (0.25 s) before the new one fades in.
4. [2:12–2:24][Motion/Clarity] The algebra rows change about every 2 s:
   - 2:13: the main row returns;
   - 2:15: (μ²+σ²)/μ = (2.5²+1.25)/2.5;
   - 2:17: split;
   - 2:19: cancel;
   - 2:21: 2.5;
   - 2:23: 0.5.
   §5 asks for ≥ 2 s + 0.4 s per term, which is about 4.8 s for the seven-term (μ²+σ²)/μ row. Change: add a 0.8 s narration hold after "mu squared plus sigma squared" (2:16.1). Merge "cancel μ²/μ" and "2.5²/2.5 → 2.5" into one TransformMatchingTex. The (μ²+σ²)/μ row then holds about 3.5 s, and the numeric collapse happens once.
5. [2:27–2:30][Clarity/Visual] On "no gap" the bar panel snaps to 2.0 and 2.0, but the beam still shows the real fulcra (2.5, 3) and the main row still reads "μ + σ²/μ = 2.5 + 0.5 = 3.0" at full opacity (kf_27). Two datasets are on screen with nothing saying which bars belong to which. Change: during the dip, dim the beam group and the main row to 30 % and write a GRAY Text 24 "ring" left of the bars (next_to(bar_panel, LEFT, buff=0.25)). Restore both when the bars return to 2.5 and 3.0.
6. [1:51.0][Audio] Whisper hears "Split sus four": "Sue's" is slurred into "four" in the one sentence that names whose number is being split. Change: respell it in narration.json as "Split Sue's count, four, into the balance point…", or add a lexicon override "Sue's" → /suːz/ with a 0.12 s comma pause before "four". Re-check that Whisper returns "Sue's".
7. [0:55–1:00][Concision] "The guess was half a friend too low: friends average twenty percent more than girls" says the same gap twice, and the screen already shows "+0.5 · 20%" (kf_10). Change: "The guess was half a friend too low, twenty percent." That saves about 2 s.
8. [0:00–0:08][Hook] Frame 0 is eight empty, dim circles with no edges, counts or question, and the right half of the frame is empty (kf_01). The puzzle arrives at 0:08. Change: start with the edges drawn at 40 % and the "average girl" / "average friend ?" rows already present as 30 % ghosts in the right panel. The first frame then poses the question, and the existing brighten, count fly-in and "?" beats keep their timings.
9. [1:02.9–1:06.1][Motion/Sync] "Four on Sue, four on Alice, one on Betty" is shown only as a 1.3× scale pulse on small tokens (frames 1:03.4, 1:04.6, 1:05.6), which is easy to miss at phone size. Change: on each name, lift that girl's tokens 0.15 units toward her node and Indicate them (scale 1.5, YELLOW). Leave a small "4", "4", "1" count tag beside each node for 1.5 s. This also previews the landing tally.
10. [2:51–3:19][Originality/Clarity, structural] The Harvard payoff is told, not shown through the episode's own machine. Change: on "425 friends they named", show 8 BLUE dots ("random students") each sending one YELLOW token along an edge to a friend; the tokens pile up on the well-connected nodes. Then let the token pile become the YELLOW curve's origin. C&F's design is literally "follow one friendship", so the payoff becomes the token argument applied to a real outbreak (about 4 s, can reuse the token code).
REACHES 9 IF ALL FIXED: borderline. Fixes 1–5 lift Visual and Motion to 9, fix 6 lifts Audio to 9, fix 7 lifts Concision to 9 and fix 8 lifts Hook to 9. That gives 8.5 Originality and 9 everywhere else = 9.0 weighted (895/100 = 8.95), which only just rounds to a pass. A safe pass needs Originality to move as well: the topic and Feld's eight-girl example are canonical, so the non-obvious image has to come from fix 10. Tying C&F's sampling design to the token mechanism is what would make the payoff memorable rather than a citation. The structure itself is sound (number-commit hook, an easy case where the guess works, a measured +0.5 failure, a beam that becomes μ + σ²/μ, two cited payoffs with an honest limit, and a landing that re-sees the opening). No other structural change is needed.
KEEP: (1) The token-weighted balance beam with exactly placed fulcra (2.5 BLUE, 3 YELLOW), the distance segments that shrink into ¼-scale squares, and the signed distances merging into 0 under the balance point. That is the proof and the memorable image. (2) The friend bar as a YELLOW outline filled BLUE to μ and PURPLE beyond, carried unchanged to Facebook (190 + 445 = 635). (3) The landing: each girl's friends' average in YELLOW, then "Sue ■■■■ 4× / Betty ■ 1×" and "Betty looks at her one friend and sees four" (kf_36, kf_38).
```

## Notes by dimension

**Hook (8.5).**
- The question "How many friends does the average friend have?" ends at 0:11.0, and "Pick one" at 0:11.9. Three candidate drop lines (2.5, 3, 4; sheet 1 @ 0:11–0:15) are followed by a 2.2 s hold. That is a commit by 0:12.
- The stakes come at 0:14–0:22, with a "random" ring on Jane and a "named friend" arrow to Alice (sheet 2 @ 0:19–0:21).
- The landing re-sees the opening network with the answer filled in (sheet 12 @ 3:21–3:39).
- The second commit, the Facebook question with a 2.1 s hold at 2:40, re-raises tension at the general case.
- Held below 9 by an inert first frame (fix 8) and a title that already gives the direction.

**Clarity (9).** Round 3's gaps are closed:
- PURPLE d = k − μ is written beside the distance line (kf_19).
- Every beam node carries its name, so "Sue holds four tokens" and "Split Sue's four" point at a visible Sue (kf_16).
- The chain runs: tokens → Σk²/Σk → ÷8 → avg(k²)/μ → squares → σ² → Sue's split → cross term → avg(d) = 0 → μ² + σ² → μ + σ²/μ. A viewer could redo it on paper after one watch.
- Every number recomputes.
- The paradox is stated about averages, and the landing shows the 5 vs 2 split, so it is not overclaimed.

Two places cost a rewatch: the 2:27 mixed-data frame (fix 5) and the 2 s cadence of the algebra rows (fix 4). Neither is wrong, so 9 is held.

**Visual (8.5).**
- The palette stays semantic from start to finish: BLUE is counted once, YELLOW is reached by friendship, PURPLE is spread.
- Context dims to about 25 % rather than disappearing (kf_16, kf_19).
- Citations sit bottom-left at y ≈ −2.96. Nothing is in the caption band.
- Moving the beam up at about 1:50 is a clear improvement over round 3's crowded kf_25. The frame at 2:13 (kf_21) has one focal column on the right, with the picture on the left.

Deductions:
- undersized annotation labels in five places (fix 1);
- boxes hugging their glyphs (fix 2);
- the 2:27 mixed-data frame (fix 5).

The faint ghost under the friend bar at 1:13.3 (kf_10) is only visible after a contrast stretch, so I did not count it.

**Motion (8.5).** Almost every move carries a relation:
- counts fly into the μ bar (0:07);
- tokens ride their edges and read degrees (0:33, 0:47);
- the bar overshoots the dashed guess (0:55);
- the girls sort onto the beam, and the tokens stack (1:07–1:17);
- distances shrink into squares, and their labels fly into σ² (1:43–1:48);
- Sue's specific split becomes the general identity in place (2:01 → 2:03);
- the four signed labels merge into the PURPLE 0, which replaces avg(d), and the box shrinks (2:08.6–2:09.4);
- the ring's spread collapses to a point (2:27);
- the Facebook bars become the curve origins (2:52);
- the 13.9-day arrow is copied into the read-out, and the self-report copy shrinks to 3.2 (3:15–3:19).

Round 3's empty-axes stretch is gone: the axes build at 2:52 and the steps start by 2:55. Deductions: the transit glyph soup (fix 3), algebra rows changing faster than the §5 hold (fix 4), and a weak pulse on a key deictic (fix 9).

**Audio (8.5).**
- −14.0 LUFS and −2.1 dBTP. 160 wpm overall and 164 wpm in the insight. WER 1.5 %.
- The holds fall where the script plans them: 0:11.7, 2:28.3 and 2:40.1.
- The deictics land within ±1 s:
  - Sue's, Alice's and Betty's tokens pulse at 1:03.4, 1:04.6 and 1:05.6;
  - the box on "Sue holds four tokens" (1:19–1:21);
  - Σk² on "k squared on top" (1:25);
  - signs appear on "left and right distances" (2:07);
  - the ring thumbnail on "The ring" (2:25);
  - the dots slide on "A few users" (2:45);
  - the GRAY arrow shrinks on "shrank" (3:17–3:19);
  - Betty's outline on "So Betty" (3:34).
- "Thank you" at 3:40.8 is a Whisper hallucination over the silent end card (trailing silence is 1.49 s), not narration.
- Deduction: "Sue's four" is heard as "sus four" (fix 6).

**Concision (8.5).** At 3:41 the episode carries one idea plus two payoffs. The ring easy case (0:28–0:44) earns its place, because the ring callback at 2:25 uses it. The one slack beat is the gap stated twice at 0:55–1:00 (fix 7).

**Originality (8.5).** The token-weighted beam with a second fulcrum, the signed-distance cancellation drawn on the beam, the redrawn Harvard curves with a refit, and "you land on a Sue four times as often as on a Betty" are specific, with no slop. But Feld's eight girls and μ + σ²/μ are the canonical presentation of this topic, so the episode refines the standard lesson rather than changing how it is taught. Fix 10 is the route to 9.
