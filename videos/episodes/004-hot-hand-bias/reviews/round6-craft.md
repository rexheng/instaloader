EPISODE: 004 — "The Hidden Bias That Hid the Hot Hand"
IDEA: If you average the "share of heads after a heads" row by row over short coin sequences, a fair coin reads below one half (17/42 for four flips), because every row gets one vote and checked heads crowd into few rows. The same bias puts a random shooter at −8 points on the 1985 hot-hand test, so Cornell's +4 is really +12.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.5 (847.5/100 = 8.475, rounded half-up)   AFTER CEILING: 8.5 (lowest 8 + 2 = 10, so the ceiling does not bind)
CAPS: none. Every cap was checked. Runtime 3:24, pace 152 wpm, −14.0 LUFS / −2.1 dBTP, max silence 2.06 s, max static 2.73 s, 0 black frames. The layout audit found 0 issues in 216 settled frames. 0 banned phrases, and both studies are cited on screen. No false intermediate equation appears: I stepped through 1:15.2–1:17.6 at 5 fps and 1:48.8–1:53.6 at 2.5 fps, and "=" joins each formula only once both sides exist. Two transient glyph-on-glyph moments occur mid-animation (2:56.9–2:57.2 and 0:04.9; see fixes 2 and 7). Each is a copy leaving its own source for under 0.4 s, not a settled overlap, so I score it under Motion instead of applying the cap-7 overlap rule. A stricter reading could cap it.
FINAL: 8.5   PASS: no
FACTS:
- 4 flips → 16 equally likely sequences | Verified | 2^4
- HHTH: the flips after a heads are H, T → 1/2 | Verified | enumeration
- HHHT checks 3 flips, 2 are heads (2/3) | Verified | enumeration
- TTTH and TTTT get no score; 14 rows are scored | Verified | enumeration
- Row scores 0×6, ½×4, ⅔×1, 1×3; the table at 0:53 matches cell by cell | Verified | enumeration (kf_14)
- Average = 17/42 ≈ 40.5%, so "cold by nine and a half points" (9.52) | Verified | (3+⅔+2)/14 = 17/42
- 24 checked flips, 12 H and 12 T, so pooled = ½ | Verified | Σhᵢ = 12, Σnᵢ = 24
- 12 heads in 8 rows, 12 tails in 11 rows | Verified | enumerated HHHH, HHHT, HHTH, HHTT, HTHH, THHH, THHT, TTHH / 11 rows with a checked T
- Vote strip: heads hold 17/3 of 14 votes = 17/42 | Verified | strip at 1:44 checked box by box
- After tails: 25/42 ≈ 59.5%; gap −8/42 = −19.05 pts | Verified | H↔T symmetry
- GVT 1985, Cognitive Psychology; "a powerful and widely shared cognitive illusion" | Verified | M&S 2018 quotes GVT pp. 312–313 (web check, Wharton PDF of the paper)
- 26 Cornell players, up to 100 shots, shot from where they would hit about half | Verified | M&S §3.1 / Table 2 (facts.md 15)
- Random shooter, n = 100, k = 3: 46% / 54%, gap −8 pts | Verified | M&S §3.2 ("−8 percentage points", confirmed by web search); exact DP in check_numbers.py
- Cornell 49% after 3 hits, 45% after 3 misses, +4 read as no hot hand | Verified | M&S §3.1
- Measured from −8, +4 is +12 points | Verified | arithmetic; M&S §3.2 states +12
- Bias grows with streak length and shrinks with record length; ghost ticks at −1.0, −3.1, −7.9 and −0.7 at 1,000 shots | Verified | M&S abstract; DP values in facts.md 18
- "evidence for a hot hand in a gym, not proof it survives defenders" | Verified (stated as a limit) | M&S §3.1, fn. 22
- M&S 2018, Econometrica | Verified | Econometrica 86(6):2019–2047
MECHANICS: runtime 3:24.0 · wpm 152 (speech time) · max silence 2.06 s (the planned prediction hold at 0:12.3–0:14.3) · max static 2.73 s · −14.0 LUFS / −2.1 dBTP · leading 0.00 s, trailing 1.32 s · WER 0.4%, where the only misses are "a" heard as "one" at 2:21 and 2:47 · "Sanjurjo's" is transcribed correctly

## Evidence read
I used the review/ pack, since metrics.json (09:04) is newer than final.mp4 (09:02). I read report.md, all 12 contact sheets, and 14 full-resolution keyframes: kf_04, 07, 10, 14, 16, 20, 21, 23, 26, 30, 33, 34, 36, 38 and 40. I also extracted 20 frames with ffmpeg at 0:04.6, 0:05.0, 0:05.4, 0:36.8, 0:37.3, 1:05.0, 1:14.3, 1:15.0, 1:21.0, 1:50.6, 1:51.2, 2:16.5, 2:17.2, 2:46.0, 2:47.5, 2:56.6, 2:57.0, 2:57.4, 3:12.0 and 3:14.0. On top of those I made fine-step crop tiles at 0:04.6–0:05.8, 1:15.2–1:17.6, 1:48.8–1:53.6 and 2:56.4–2:57.6. I also read the transcript, its word timings, the script, narration.txt and facts.md.

## Beat structure against §6
| Beat | Here | Verdict |
|---|---|---|
| Cold open | 0:00–0:14. The coins flip in at frame 1, then the "< ½ / = ½ / > ½" options and a 2.06 s hold | Strong. The prediction is explicit, but the viewer must parse three instructions in 12 s |
| Stakes | 0:14–0:27. GVT is cited and quoted, and H→hit morphs | Good |
| Naive build / fail | 0:33–1:08. The 16-row table, dots dropped onto the line, a live 50% → 40.5% marker, "cold −9.5 points" | Excellent SMH-style test-the-test |
| Insight | 1:08–1:56. Pooled strip vs one-vote strip, then the two formulas | The best minute of the episode |
| Mirror | 1:56–2:14. A half-turn about 50%, giving 25/42 and −19 | Meaningful motion |
| Payoff | 2:14–3:10. Cornell, M&S −8, ghost ticks, +12 brace, "no defenders" | Correct and cited, but 56 s long with three axis re-labellings in 24 s |
| Landing | 3:10–3:24. The cold-open frame returns with the formula and the 17/42 marker, then "hot" | Re-sees the opening. The closing line is subtle |

## Sync (deictics, ±2 s)
- "This row checks three flips" (0:42.1): HHHT is boxed at 0:43. ✓
- "Two rows never show a heads" (0:48.3): TTTH and TTTT are boxed at 0:49. ✓
- "Drop the other 14 scores onto the line" (0:53.2): dots are falling at 0:55. ✓
- "17 out of 42, about 40.5%" (0:56.4–1:01.4): the live readout is at 49.9% at 0:57 and 40.9% at 0:59, and lands on 40.5% at 1:01. ✓
- "reads cold by nine and a half" (1:02–1:08): "cold" is written at 1:05 and "−9.5 points" is up at 1:07. ✓
- "Gather all 24 checked flips" (1:10.4): tiles leave the table at 1:11. ✓
- "This row's three heads… this lone tails" (1:30.9–1:36): HHHH is boxed at 1:33 and HTTT at 1:35, each in both the table and the strip. ✓
- "Twelve heads crowd into eight rows. Twelve tails…" (1:36.7–1:41): 8 yellow boxes at 1:39, then 11 white boxes at 1:41. ✓
- "line them up… 17 out of 42" (1:44–1:47): the yellow slides and stops on 40.5%, and 17/42 appears at 1:47. ✓
- "Swap heads and tails, and the strip flips" (1:58.6–2:02.7): the copy is unchanged at 1:59, recoloured at 2:01 and flipped at 2:03. ✓
- "After three hits, versus after three misses" (2:25–2:28): rings mark the record. ✓
- "Longer records shrink it" (2:45.4): the 1,000-shot ghost is at −0.7 at 2:46–2:47.5. ✓
- "49 percent… 45" (2:49.5–2:56): the purple column fills at 2:51 and 2:53. ✓
- "Seventeen out of forty two" (3:13.3): the formula and marker are built by 3:15. ✓
- "running hot" (3:21–3:22.8): the arrow is drawn at 3:23. ✓

No miss over 2 s anywhere. A/V sync is the strongest craft area of this cut.

## Notes per dimension
- **Hook 8.5.** The first frame is concrete (0:00 coins flipping in) and the viewer commits by 0:12.3 with on-screen options (kf_04). But the prompt is three procedural instructions in 12 s: "check the next flip", "the shares", "average over all 16 sequences". A first-time viewer is still parsing the procedure when asked to commit. At 0:09 a 4×4 ghost deal of 64 tiny coins, at 60% opacity, is added on top. The ending does resolve the opening on its own image (3:15).
- **Clarity 8.5.** It is concrete first, and every number checks. Two gaps remain:
  - (a) "Fewer rows, fewer votes" (1:43) asks the viewer to infer the vote totals. The screen shows "12 heads · 8 rows / 12 tails · 11 rows" (kf_21), but never the votes those rows hold (5⅔ vs 8⅓ of 14). So the step from crowding to 17/42 is asserted, not shown, and the 17/42 at 1:47 arrives as a parked number.
  - (b) The payoff re-labels one axis three times in 24 s: 0–100% lanes at 2:19, a zoom to 40–60% at 2:23, then −10…+10 points at 2:41. It also introduces a simulated record (2:21–2:31) whose rings are never counted. The 46/54 then come from M&S, not from anything on screen.
- **Visual 8.** The palette is semantic and consistent: yellow is a hit, blue is the test, red is bias, purple is Cornell. Type is large, contrast is good, and the layout audit is clean. The deductions:
  - **1:37–1:44** (kf_20, kf_21): this is the frame that should have one focal point, and it has about eight competing groups. The 16-row table at full opacity, the boxes, the pooled strip, "the obvious guess", the vote strip, the 40.5% label and marker, the pooled formula and the two count lines all show at once. Neither the table nor the pooled strip dims until 1:45. The blue 40.5% marker and the dashed 50% line also cut through vote-strip tiles: the marker runs through box 6, HTHT, at x≈655.
  - **2:41–3:09** (kf_33, 34, 36): the chart spans x 137–1405, so its centre is at x≈771, while the title "Cornell, 1985" is centred on the frame at x=960. Once the right column fades (3:03), the right 27% of the frame is empty and the composition sits left-heavy.
  - **0:29 and 3:23** (kf_40): the "hot" arrows are ink. The declared palette gives ink to "the assumption" (the dashed guess), so the landing's key arrow borrows the colour of the thing it refutes.
  - **3:12–3:13**: the "sixteen rows return" ghost is barely visible. The coins are tiny and the ghost sits at about 10–15% opacity (frame 3:12.0), so the "on 'fair'" reference has nothing to land on.
  - Nitpick: the +4 marker carries a base dot (kf_36) but the −8 marker does not.
- **Motion 8.5.** Objects persist and transform with meaning throughout:
  - The table's discs become pooled tiles (1:11).
  - The rows are resized into equal votes (1:21–1:25).
  - The half-turn mirror runs about 50% (2:01–2:03).
  - The two lanes collapse into the difference axis (2:39–2:41).
  - The difference axis becomes the cold-open axis (3:10).

  These are the deductions:
  - **2:56.9–2:57.2**: the copies of 49% and 45% start on top of the originals, giving garbled "4949%" and "45%5%" glyphs for about 0.3 s. They then shrink to about 20 px text that crosses the empty plot (2:57.4) and vanishes into the +4 dot. The subtraction this motion should show (49 − 45) is never written.
  - **1:21**: regrouping tiles fly straight through the "40.5%" label and occlude it.
  - **1:50.6–1:51.2**: the 14 row ratios fly at about 20 px as scattered debris ("0/1", "1/2") across the dimmed pooled formula.
  - **0:04.9**: the yellow H copy doubles over the coin's H before it travels to "1".
- **Audio 8.5.** Loudness, pace and WER are all on target, and every deictic lands (see Sync). The one cited weakness is 1:36.7–1:53.1, which whisper heard as a single 16-second unpunctuated segment ("…across eleven Fewer rows fewer votes Line them up…"). That suggests the densest conceptual run is delivered with run-on, non-falling sentence-final prosody, even though the pause table shows 0.5–0.7 s gaps there.
- **Concision 8.5.** Less than 10% is removable. The slack is in the payoff (2:14–3:10, 56 s). The simulated record (2:21–2:31) teaches the ring rule a second time without a measured result, and the 40–60% zoom is used for only one slide.
- **Originality 9.** The one-vote strip (HHHH's three heads squeezed into one vote, HTTT's lone tails stretched to a whole one, 1:31–1:36) and the half-turn mirror are images a viewer would remember and re-draw. "Test the test" on a coin is a real SMH-style move.

FIXES (highest impact first):
1. [1:41–1:47][Clarity + Visual] Crowding to 17/42 is asserted, not shown, and the frame has no focal point.
   - On "Twelve heads crowd into eight rows", dim to 30%: the pooled strip, the pooled formula, "the obvious guess", and the 6 table rows without a checked head.
   - On "Twelve tails…", swap which rows are dimmed.
   - On "Fewer rows, fewer votes", write a live `DecimalNumber` vote count directly above each colour of the vote strip: yellow "5⅔ votes" over the heads slices, grey "8⅓ votes" over the tails slices, both Text ≥ 26.
   - On "line them up", carry the yellow "5⅔" into the numerator so "5⅔ / 14 = 17/42" appears before it TransformMatchingTex-es into 17/42.

   This makes 17/42 derivable on screen and gives the frame one focal point. Expected effect: Clarity +0.5, Visual +0.5.
2. [2:56.6–2:58][Motion] The 49%/45% flight garbles glyphs and then shrinks to debris. Replace it with:
   - TransformFromCopy of 49% and 45% into a MathTex "49 − 45" placed right of the +4 marker (copies offset 0.4 units down on frame 1, full size, 1.2 s, smooth);
   - then TransformMatchingTex "49 − 45" → "+4", with the marker growing from 0 as the "+4" lands.

   The subtraction becomes visible and the superposition goes away.
3. [2:41–3:09][Visual] The composition is left-heavy and the title is misaligned with the chart.
   - When the right column fades at 3:03, shift the whole number line group right by +1.4 units (1.0 s, smooth) so it centres on x = 0.
   - Alternatively, centre "Cornell, 1985" over the chart (x = −1.4) from 2:41 on.

   Then the brace, title and chart share one vertical axis.
4. [1:21][Motion] The regroup tiles occlude the "40.5%" label. Fade the label to 25% during the 1.5 s regroup and restore it on "however many flips it checked". Alternatively, route the tile paths below the vote lane, using `path_arc` so they stay under y of the label minus 0.3.
5. [3:11–3:14][Visual + Sync] The ghost of the sixteen rows on "fair" is nearly invisible. Bring it back at 60% opacity with coin radius ≥ 0.15, in the same compact 4×4 layout as 0:09, held 1.0 s before the rows fly into (1/14)Σhᵢ/nᵢ. The reference then lands on something visible.
6. [0:28–0:30, 3:21–3:23][Visual] The "hot" arrows are ink, which is the assumption colour.
   - Colour both blue, the test's reading, to match the shooter dot and the 17/42 marker.
   - Or declare a seventh role "verdict arrow" in the palette and use it consistently.

   Either way, the landing's key arrow stops borrowing the colour of the dashed guess.
7. [0:04.8–0:05.0, 1:50.6–1:51.4][Motion] Two more transient superpositions.
   - At 0:04.8–0:05.0, offset the H copy 0.25 units up on its first frame (or fade it in from 0 as it leaves) so no doubled "H" appears.
   - At 1:50.6–1:51.4, the 14 row ratios flying at about 20 px read as debris. Either fly them at their own table size (Text ≥ 26) in 2 staggered waves (`lag_ratio` 0.08), or fly one representative "3/3" while the other 13 fade.
8. [2:19–2:41][Clarity + Concision] Three axis re-labellings and an uncounted record crowd 24 s. Cut the 40–60% zoom and keep 0–100% for the lanes, since the 46/54 cursors are readable at that scale with labels. Then either:
   - give the record a payoff: count its ringed shots live and show "after 3 hits: 6/13 = 46%" (that this record happens to read 46% is itself the point; check that it does), or
   - cut the record and use the 10 s for a 1.5 s hold on the 46/54 picture.
9. [1:36.7–1:53][Audio] The densest conceptual run is heard as one sentence. Regenerate the TTS with sentence-final stops: split "Fewer rows, fewer votes." and "Line them up, and heads hold seventeen out of forty two." into separate clips, each followed by a 0.5 s gap. Add 0.3 s before "So the test takes".
10. [0:00–0:12][Hook] The prediction prompt is three procedures in 12 s. Cut "Average the shares over all sixteen sequences" to "Do this for every four-flip run and average." Show the 16 ghost rows at radius ≥ 0.15 (the 0:09 tiles are ≈ 0.12) and fade the big row to 40% while they deal, so the viewer looks at one thing when asked to commit.

REACHES 9 IF ALL FIXED: yes, narrowly. Fixes 1–6 are worth about +0.5 on Visual, Motion and Clarity, which lifts the weighted score to about 9.0. Fix 1 is essential: it is the one remaining step in the argument that is asserted rather than seen. No structural change is needed; the hook, fail, insight and landing are all in the right place.

KEEP:
1. The one-vote strip (1:21–1:47), with HHHH's three heads squeezed into one vote, HTTT's lone tails stretched to a whole one, and the yellow sliding onto 40.5%.
2. "Test the test": the live 50% → 40.5% marker and "cold −9.5 points" (0:53–1:08), then the half-turn mirror into −19 (2:01–2:14).
3. The landing on the cold-open frame with (1/14)Σhᵢ/nᵢ = 17/42 beside its marker (3:15–3:24), and the deictic sync throughout.
