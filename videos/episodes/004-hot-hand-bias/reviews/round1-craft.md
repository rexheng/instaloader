# Episode 004 — Round 1 review (craft critic: visual design · motion · A/V sync)

Evidence: review pack `review/` (metrics.json 12:20 is newer than final.mp4 12:19, so I reused it). I read report.md, all 11 contact sheets, and the full-resolution keyframes at 0:11.2, 0:33.1, 1:10.7, 1:23.1, 1:38.9, 1:42.4, 1:53.9, 2:00.0, 2:30.5 and 2:46.4. I also pulled extra frames with ffmpeg at 0:00.3, 0:47.0, 1:13.5, 1:47.0, 1:57.0, 2:17.5, 2:45.0 and 3:02.0. I read script.md, facts.md, narration.txt and the transcript, and re-enumerated all 16 sequences myself.

```
EPISODE: 004 — "The Hidden Bias That Hid the Hot Hand"
IDEA: When you average the "share of heads after a heads" row by row, every sequence gets one vote however many flips it checked, so a fair coin reads 17/42 instead of 1/2. The 1985 hot-hand test was graded against 0 when a random shooter scores −8, and measured from the right baseline, Cornell's +4 becomes +12.
SCORES: Hook 8.5 · Clarity 8 · Visual 8 · Motion 8 · Audio 8 · Concision 8 · Originality 8.5
WEIGHTED: 8.1   AFTER CEILING: 8.1 (lowest 8 + 2 = 10, so the ceiling does not bind)
CAPS: none
FINAL: 8.1   PASS: no
```

## FACTS
| Claim | Verdict | Source / check |
|---|---|---|
| 4 flips → 16 equally likely rows | Verified | 2^4 |
| HHTH: checked flips 2, 3 → 1 of 2 heads | Verified | enumeration |
| 2 rows (TTTH, TTTT) unscored; 14 scored | Verified | enumeration |
| HHHT checks 3 flips, 2 heads → 2/3 | Verified | enumeration |
| Scores 0×6, ½×4, ⅔×1, 1×3; mean 17/42 = 0.405 | Verified | my enumeration: 17/42 exactly |
| "reads cold by 9.5 points" | Verified | 50 − 40.48 = 9.52 |
| 24 checked flips, 12 H / 12 T | Verified | Σh = 12, Σn = 24 |
| 12 heads in 8 rows, 12 tails in 11 rows | Verified | enumeration; the 8 rows outlined at 1:42 are the right 8 |
| Vote strip at 1:38: 14 equal segments, each split h_i/n_i | Verified | I read every segment of the 1:38.9 keyframe against the table |
| GVT 1985, Cognitive Psychology; "a powerful and widely shared cognitive illusion" | Verified | GVT 1985 pp. 312–313 via Miller & Sanjurjo 2018 fn. 8 |
| 26 Cornell players, up to 100 shots each | Verified | M&S 2018 §3.1 / Table 2 (GVT Study 4) |
| 49% after 3 hits, 45% after 3 misses, +4 | Verified | M&S 2018 §3.1 |
| Random-shooter expected gap ≈ −8 pts (n = 100, streak 3) | Verified | M&S 2018 §3.2; facts.md simulation −7.88 |
| 1,000 shots: −0.75 (simulated) | Verified as labelled simulation | check_numbers.py |
| +4 − (−8) = +12 "points hot" | Verified | M&S 2018: "+12 percentage points higher" |
| Miller & Sanjurjo 2018 · Econometrica | Verified | Econometrica 86(6):2019–2047 |

No wrong numbers. Citations are on screen at 0:19–0:39 (GVT), 2:05–2:51 (GVT) and 2:23–2:51 (M&S).

## MECHANICS
runtime 3:06.3 · 153 wpm (speech time) · max internal silence 2.07 s (the planned prediction hold at 0:12.3) · leading 0.00 s / trailing 1.74 s · max static 3.37 s (2:18.5–2:21.8, the planned second prediction hold) · −14.0 LUFS / −2.1 dBTP · 0 black frames · WER 0.7% (both diffs are number formatting, not mispronunciations) · 0 banned phrases. No mechanical caps.

## Sync audit (deictics vs visible, ±2 s)
- 0:05.3 "Here, one of the two" → "1/2" assembles by 0:07. OK.
- 0:48.4 "This row checks three flips" → HHHT boxed at 0:49. OK.
- 0:59.6 "Drop the other 14 scores onto the line" → scores fly down at 1:01. OK.
- 1:11 "reads cold" → red arrow and "cold −9.5 points" at 1:12–1:13. OK.
- 1:35 "This row's three heads" → HHHH row plus its strip segment boxed at 1:35. OK. 1:38.5 "this lone tails" → HTTT plus its segment boxed at 1:39. OK. This is the best sync in the episode.
- 1:40.3 "eight rows" / 1:43 "eleven" → the outlines appear on cue (1:41, 1:45).
- 1:47 "Line up the votes" → the yellow segments slide left onto 0.405 (1:47–1:49). OK.
- 2:12 "after three hits" / 2:15 "after three misses" → rows build on cue.
- 2:25 "minus 8" → the blue marker slides 0 → −8 by 2:27. OK.
- 2:35 "49%" / 2:39 "45" / 2:41 "plus 4" / 2:45 "12 points hot" all land within 1 s.
- 3:03 "already running hot" → the "→ hot" arrow grows. OK.

No sync cap. Every deictic lands.

## Dimension notes (evidence)
- **Hook 8.5.** The first frame (0:00.3) shows coins flipping in, with no title card. The commit question "What do you get?" lands at 0:11.3–0:12.4, followed by a 2.1 s hold with a "?" over the line. The stakes ("famous study … called the hot hand an illusion") arrive by 0:26. The landing (2:53–3:06) returns to the exact cold-open frame and re-reads it, which is excellent. Two things hold it back. Tension sags at 0:27–0:44: about 17 s re-explain the procedure the viewer already ran in the cold open ("Heads are hits. After every hit, check the next shot…"), and only small "hot →" / "cold ←" arrows are added to a frame that is otherwise static. The opening 11 s are also four procedural sentences before the question.
- **Clarity 8.** The coin half is near-canonical: concrete row, all 16 rows, measured failure (−9.5), pooled 12/24 vs vote-weighted 17/42. The one transition a viewer cannot rebuild is 2:05–2:27. The video measured a one-sided quantity (share after a heads vs ½), then jumps to a two-sided difference (after 3 hits − after 3 misses) with streak length 3, and the baseline −8 is simply asserted. Nothing shows that the after-misses side is biased *upward* by the mirror argument, so the viewer cannot see why the gap baseline is negative, or why it is bigger than the one-sided bias. "Longer records shrink the bias" (2:28) is correct, but streak length 3 pulls the other way and is never mentioned.
- **Visual 8.** The palette is semantic and held all episode: yellow heads/hits, grey tails, blue test and its reading, red bias, purple real Cornell data. The vote strip (1:27–1:53) is a frame I would screenshot. Defects:
  1. The composition is left-weighted for most of the runtime. The axis spans x ≈ 135–1405 px, so the right ~500 px are empty from 0:08–1:49 and 2:53–3:06 (see 0:11.2, 0:33.1, 1:10.7, 3:02). In the cold open (0:00–0:08) the bottom 55% is also empty.
  2. Word load is over §5's 12-word limit in the stakes frame (0:27–0:39: quote 6 + legend + "the obvious guess" + 7-word axis title + citation ≈ 20 prose words) and in the payoff frame (2:41–2:51: 9 separate text blocks, about 30 words).
  3. Vestigial empty blue rings: at 2:35 and 2:39 the "?" vanishes from the ring and "49%" / "45%" appear beside it. That leaves two hollow blue circles (2:35–2:51) that mean nothing.
  4. The ghost label "1,000 shots: −0.75 (simulated)" (2:29–2:33) floats about 230 px above its marker, and the marker sits about 38 px from the dashed 0 line, so at a glance the label reads as attached to "the obvious guess".
  5. The "+12 points" brace (2:45–2:51) hangs about 290 px above the −8 line and the +4 dot it measures, with three labels between them.
  6. In the formula at 1:53 the "1/14" (one vote per row, the whole point) is tiny (cap ≈ 22 px) and white instead of carrying a colour that ties it to the equal-width segments.
- **Motion 8.** Insight motion is genuinely 3b1b-grade: checked coins fly out of the table into a 24-tile strip whose boundary lands on ½ (1:16–1:21). A copy regroups into 14 equal votes (1:25–1:29). The yellows slide left onto the blue 0.405 (1:47–1:49). The scores fly out of the table into Σ h_i/n_i (1:51). Weak points:
  1. 2:03–2:07: both strips and both formulas fade out, so the one picture is discarded instead of carried into the payoff (script.md promised they stay).
  2. 2:16.5–2:18: the share axis cross-fades into the gap axis. At 2:17.5 the old ticks (0.25, 0.75) and the "0.405 random shooter" ghost are visibly superimposed on −5 and +10, so the moment reads as a dissolve, not a transform. The random-shooter marker does not travel from 0.405 to its new meaning; it fades out and a new blue marker is born at 0.
  3. 0:27–0:44 is nearly static. The detector shows 0:19.0–0:22.3 fully static, and the rest adds only fades.
- **Audio 8.** Pace 153 wpm, loudness on target, every deictic lands. Cadence evidence: of 57 internal pauses ≥ 0.3 s, 51 are 0.4–0.5 s, one after almost every sentence (report.md silence list). That is a metronomic sentence-gap rhythm, not intentional pausing. Only the two prediction holds (2.1 s, 2.0 s) vary.
- **Concision 8.** 1:45.8–1:54.4 says "17 out of 42" twice in about 6 s ("heads hold 17 out of 42. Averaging the 14 row scores gives 17 out of 42"). 0:26.6–0:38.0 restates the cold-open procedure. Everything else earns its place.
- **Originality 8.5.** The equal-width "one vote per row" strip is a non-obvious, memorable image of the Miller–Sanjurjo mechanism, and the landing line reframes the opening. The topic itself is well trodden. What would lift this to 9 is making the strip legible at a glance, with the tiles currently about 25 px wide.

## FIXES (highest impact first)
1. **[2:05–2:27][Clarity] The −8 baseline is asserted, not seen.** Before the axis swap, spend about 8 s on the mirror while the 16-row table is still on screen. Add a second blue marker at 25/42 ≈ 0.595 labelled "after tails" and say "By the same logic, the share after a tails reads hot: twenty five out of forty two." Draw a red arrow from 0.595 down to 0.405 labelled "−19 points", the difference of the two averages (17/42 − 25/42 = −8/42). I verified 25/42 by enumeration. Note that the per-row mean of the difference, over the 12 rows where both are defined, is −1/3, so label it as a difference of averages. Then say "Cornell's test compares exactly these two, after streaks of three over a hundred shots, and there a random shooter's gap is about minus eight." This makes the sign and the mechanism of −8 visible. Add one clause noting that longer streaks push the bias up while longer records shrink it.
2. **[2:03–2:18][Motion] Carry the picture into the payoff instead of fading it.** Keep the vote strip and the blue 0.405 marker. Transform the 0–1 share axis into the gap axis with `ReplacementTransform` on the axis line, and fade the old tick labels out completely (the `FadeOut` must finish before the new `Write` starts, so there is no 2:17.5 overlap). Move the "random shooter" marker with its label, so blue visibly travels from "reads 0.405" to "reads −8". At minimum, sequence the tick swap so old and new labels never coexist.
3. **[2:35–2:51][Visual] Remove the hollow rings.** `Transform` each "?" ring into its percentage: the "49%" / "45%" `MathTex` should grow out of the ring (`ReplacementTransform(ring_q, pct)`), or fill the ring purple. Then drop the separate percentages so no empty circles remain.
4. **[2:41–2:51][Visual] Declutter the payoff frame.** Once they have been read, dim the citations and the "after 3 hits / after 3 misses" rows to 30% opacity. Replace the "the obvious guess" text on the gap axis with just the dashed 0 tick after 2:27. Move the "+12 points" brace down to sit directly above the axis (buff 0.25 above the −8 / +4 marks), with "bias" shifted below the arrow, so the brace touches what it measures.
5. **[0:26.6–0:44][Hook/Concision] Cut the procedure restatement.** Replace "Heads are hits. After every hit, check the next shot, and score the share that went in." with a single morph: transform the H/T coin faces into hit/miss glyphs while saying only "Heads are hits." That saves about 6 s. Then bring "A hot shooter should score above their usual rate…" in over the arrows. Target: the 16-row table on screen by 0:38 instead of 0:45.
6. **[1:45.8–1:57][Concision] Say "17 out of 42" once.** Change the narration to "Line up the votes, and heads hold seventeen out of forty two. That's the row average. Pool the counts first, and you get one half." Build the Σ h_i/n_i formula on "row average".
7. **[2:29–2:33][Visual] Fix the ghost marker.** Put the "1,000 shots: −0.75 (simulated)" label directly below the axis under its marker (buff 0.2, left-aligned to the marker), or drop the marker and show the shrink as the blue −8 marker sliding briefly toward 0 and back, labelled "1,000 shots (simulated)".
8. **[0:00–1:49, 2:53–3:06][Visual] Re-centre the composition.** Shift the coin row, axis and table group right by about 1.2 units (so the axis spans x ≈ −5.0…+4.6 instead of −6.1…+3.3) until the formulas need the right column at 1:51, or slide the whole group left only when the formulas arrive. In the cold open, start the coin row at y ≈ 0.8 and lower it to its slot as the axis draws.
9. **[1:51–2:03][Visual] Colour the vote weight.** Render "1/14" at the same font size as h_i/n_i and colour it to match the equal-width segment outlines. Flash the 14 segment outlines as the 1/14 is written (`TransformFromCopy(segment_outlines, one_over_14)`).
10. **[whole][Audio] Vary the sentence gaps.** In narration.json, set inter-sentence pauses to 0.2–0.3 s inside a thought (e.g. 0:42.4 "A fair coin." → "Four flips") and 0.7–0.9 s at beat ends (1:15.5, 1:58, 2:51), instead of a uniform 0.5 s.

REACHES 9 IF ALL FIXED: yes. The structure is right: cold-open prediction, measured failure (−9.5), a one-picture insight with the formula grown from it, a cited payoff, and a landing that re-reads the first frame. What keeps it at 8 is the unexplained −8 bridge (fix 1), the discarded picture and cross-fade at the axis swap (fix 2), and payoff-frame clutter (fixes 3–4). With those fixed, Clarity, Motion and Visual each move to about 9, and the weighted score clears 9.0.

KEEP:
- The one-vote-per-row strip sequence (1:16–1:53): 24 tiles → 14 equal votes → yellows slide onto 0.405. It is the proof.
- The landing (2:53–3:06): the exact cold-open frame returns, the row's ½ drops right of 17/42, and "→ hot" passes it.
- Deictic sync on "this row's three heads" / "this lone tails" (1:35, 1:39), with the table row and strip segment boxed together.
