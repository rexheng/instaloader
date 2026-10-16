# Review — Episode 75, round 1 (craft critic: visual design, motion, A/V sync)

Evidence: `review/` pack (metrics.json 11:28 is newer than final.mp4 11:25, so it was reused). I read report.md, all 12 contact sheets and 14 full-resolution keyframes (kf_02, 06, 09, 11, 16, 17, 21, 25, 26, 28, 33, 37, 38, 40), plus 25 extra frames I pulled with ffmpeg (0:00.0, 0:56.5–0:58.5, 1:18–1:26.5, 1:42–1:52, 2:03–2:05.5, 2:21.5–2:27.5, 2:40, 2:55–2:57.5, 3:16). I also read the transcript, script.md, facts.md and sim_output.txt.

```
EPISODE: 075 — "Mild Preferences, Extreme Segregation"
IDEA: In Schelling's model, households that need only a third of their neighbours to match still build a town where three quarters match, because each departure tips a neighbour that was content, so a segregated map cannot tell you what its people wanted.
SCORES: Hook 9 · Clarity 8 · Visual 7.5 · Motion 8 · Audio 8 · Concision 8.5 · Originality 8
WEIGHTED: 8.1   AFTER CEILING: 8.1   (lowest 7.5 + 2 = 9.5, so the ceiling does not bind)
CAPS: none
FINAL: 8.1   PASS: no
```

## FACTS
| Claim | Verdict | Source |
|---|---|---|
| Final town: 76 % of neighbours match (0.755) | Verified | sim_output.txt, state 7 |
| Rule: stay if at least ⅓ of neighbours match = "happy to be outnumbered two to one" | Verified | arithmetic; boxed example at 0:17–0:22 shows 2 of 6 (2 gold, 4 blue, 2 empty) |
| Random start: half match (0.499) | Verified | sim |
| 238 unhappy, "about one in six" (16.5 %) | Verified | sim |
| Round one: 200 moves, 64 % (0.644) | Verified | sim (38 became content before their turn, which the video never explains, see fix 9) |
| 74 still unhappy; most were content before round one and never moved (67 and 68 of 74) | Verified | sim |
| Corner chain A→B→C→D: 3/8 → 2/7 at each step; B leaves in round 2, C in round 3 | Verified | sim_output chain table; I recounted the on-screen tiles at 1:24, 1:29 and 1:43 |
| Settles at round 7, 76 % | Verified | unhappy by state [..., 1, 0] |
| 30 towns per demand from 0–60 %; same town at ¼ gives 58 %, at ⅓ gives 76 % | Verified | sim (0.579 / 0.755); dot at (33.3, 75.5) placed correctly at 2:06.8 |
| 2/7 < ⅓ and 2/7 ≥ ¼; at ¼ the chain never starts | Verified | arithmetic plus `verify_chain` ("chain households that ever move: []") |
| Schelling 1971 ran it by hand on a checkerboard; moves to the nearest satisfying square; 25–30 % vacancies; the jump comes at about 35–50 % | Verified (paper text as quoted in facts.md; web search confirms the "rapidly rising function" passage) | Schelling 1971, J. Math. Sociol. 1(2):143–186 |
| Quote: "inferences about individual motives can usually not be drawn from aggregate patterns" | Verified (abstract, verbatim) | Schelling 1971 |
| The HOLC 1930s maps increased racial segregation for decades | Verified (abstract: "increased racial segregation in later decades"; hedged as "one study") | Aaronson, Hartley & Mazumder 2021, AEJ: Economic Policy 13(4):355–392 |

Both empirical sources are cited on screen ("Schelling, 1971 · Journal of Mathematical Sociology" from 2:35 to 2:56; "Aaronson, Hartley & Mazumder, 2021 · AEJ: Economic Policy" from 3:08 to 3:16, each held well over 3 s, bottom left at about y = −3.0). I found no wrong numbers.

## MECHANICS
runtime 3:23.5 · wpm 157 (speech time; 184 excluding pauses) · max silence 1.97 s (0:09.6, the planned prediction hold) · max static 3.33 s (2:34.5 and 2:44.4) · −14.0 LUFS / −1.6 dBTP · leading 0.00 s / trailing 1.73 s · WER 0.4 % · banned phrases 0. No mechanical cap triggers.

Banned-pattern sweep: there are no question chains (every question stands alone: 0:07.7, 0:27.6, 1:26.7, 2:21.4), no "it turns out", no fake reveals, and no recap ending. The closing line reframes the cold open.

## What the frames show (craft notes)
- **Hook (0:00–0:31).** The town is on screen from frame 0. The "? demanded" marker sits at 76 % (0:09), which quietly plants the wrong guess. The 2.0 s hold is followed by "Just a third" as the marker slides down to ⅓ (0:11–0:13). This is a textbook misconception-first opening.
- **Persistent objects.** Tiles fly back to their starting squares on "Rewind" (0:32–0:35) and the meter falls 76 → 65 → 50 alongside them. The dashed preview arc (0:49–0:55) is a real move that later flies on the same arc. Tiles fly into the numerator "3" (1:20.5). The town shrinks into a thumbnail and the thumbnail becomes the chart dot (2:03–2:06). The thumbnail grows back into the full town for the landing (2:55–2:58). This is the best motion craft in the episode.
- **Deictic sync.** Pointing words land on what is visible: "these 238" (0:43, outlines draw in as the counter counts up); "this counter" (1:03); "this gold household" (1:17, the magnifier opens); "this neighbor moved away" (1:25, A flies out); "Its neighbor here" (1:36, the ring moves to C); "this chart" (2:05); "individual motives" / "aggregate patterns" (the box flashes on the x-axis title at 2:51 and on the thumbnails at 2:55). None of them misses.
- **Competing focal points in the core insight (1:15–1:50).** For 35 s the full-saturation 40×40 board, with 74 red outlines, fills the left 45 % of the frame and never moves. Meanwhile the actual argument plays out in a 390 × 310 px inset and a fraction in the lower right (kf_16, kf_17, kf_21). The eye goes to the biggest, busiest object, which is the wrong one. The board also disagrees with the inset: it stays in the after-round-1 state, and the dimmed HUD still reads "round 1" while the inset says "after round 2" (1:41) and "after round 3" (1:45).
- **Unhappy tiles lose their household colour.** A red outline over a darkened fill turns gold tiles olive and blue tiles slate (kf_09 at 0:48, kf_16 at 1:24). At 1:18.9 the narration says "three gold neighbors", but only two neighbours are bright gold. The third (A, at the right of the centre) is an olive square inside a red ring, the same olive as the dimmed context tiles around it. The viewer counts two.
- **Chart dot clouds (2:09–2:57).** Thirty translucent dots per column overlap into soft white blobs ("cotton balls" in kf_26), and no column has a mean marker. The ¼ and ⅓ columns read as smudges, not measurements.
- **Inset inside the plot area (2:23–2:33).** The 3×3 patch and "2/7 < ⅓" sit inside the axes at about (5–15 %, 75–85 %), where a viewer expects data, about 90 px from the ⅓ cluster (kf_28). The "1/3" copied from the thumbnail label also briefly leaves a doubled "⅓ ⅓ → 76%" at 2:25.
- **"random mix" straddles the edge of Schelling's band** (2:43–2:57, kf_33). Half the word sits on the band and half on the background.
- **Transition overlap at 2:03.** The chart's x-axis line draws across the still full-size town board for about 0.5 s (sheet_07 at 2:03, extra frame at 2:03.0).
- **Near-static payoff (2:32–2:57).** For 25 s the only changes are a citation fade, the grey band and two box flashes, and both static stretches at 3.3 s fall here. The Schelling band appears at 2:41, about 5 s before "between about a third and a half" (2:46.5–2:48.9).
- **Typography and safe area.** Everything passes. The y-title's top is at y ≈ 3.57 (limit 3.6), citations are at y ≈ −3.0, ticks are about 30 px, and labels are at least 34 px. The palette is semantic and consistent (blue/gold households, red for unhappy, purple for demand, ink for outcome, grey for context), with no red/green pairing. The one exception is the blue Ω on the end card, which reuses the colour that means "blue households".
- **Voice.** Sync is clean, but nearly every sentence ends in an identical 0.4–0.5 s gap (more than 45 of them in the silence list), with fast delivery inside phrases (184 wpm excluding pauses). The cadence is metronomic and does not mark beat boundaries (0:31.9, 1:14.7, 2:02.5 and 2:32.2 get the same 0.5 s as mid-thought joins).

## FIXES (highest impact first)
1. **[1:15–1:50][Visual + Motion]** The static full-brightness board competes with the inset that carries the argument. When "Replay one corner" starts, dim the board to 30 % opacity except the white focus box. Scale the magnified inset up by about 1.6× (to about 620 px wide) and centre it in the right half, with the fraction to its right. Remove or update the HUD "round 1" label so it matches the inset ("after round 2/3"). Expected effect: Visual +0.5, Motion +0.5.
2. **[2:21–2:32][Clarity + Originality]** "Why the jump?" is answered with a single household, so the step in the curve is never explained in general. Add one picture. Under the chart's x-axis, draw a number line from 0 to 0.5 with a tick for every possible neighbour fraction k/n (n ≤ 8). Slide the purple demand marker from ¼ to ⅓ and colour red the only two rungs it crosses, 2/8 and 2/7, while saying: "Between a quarter and a third, only two fractions change sides: two eighths and two sevenths. Our corner household was two sevenths." This turns the anecdote into the reason the curve is a step, and it is the memorable "one picture" the episode currently lacks. Expected effect: Clarity +0.5, Originality +0.5.
3. **[1:06–1:14][Clarity]** "Most of these … never moved" is asserted, not shown. When the counter reads 74, split the outlined tiles: keep red outlines on the 67 that were content at the start, fade the 7 others to grey, and add a grey label under the counter, "67 were content at the start". The failure's cause then becomes visible evidence rather than narration.
4. **[0:43–1:50, especially 1:16–1:22][Visual + Clarity]** Unhappy tiles turn olive or slate, so "three gold neighbors" shows only two gold. Keep the household's full fill colour on unhappy tiles and draw the red outline as an outer stroke (about 4 px, outside the tile). Use the dimmed-context tint only for tiles outside the focus neighbourhood.
5. **[2:09–2:57][Visual]** The dot clouds blur into blobs. Render each column as dots of radius 0.05 at 0.5 opacity with ±0.8 pp horizontal jitter, plus an ink horizontal tick at the column mean (58 at ¼, 75 at ⅓). Alternatively, use a mean dot with a min–max whisker and keep the 30 dots faint behind it.
6. **[2:23–2:33][Visual]** The patch and inequality sit inside the plot's data area. Move them to the right-hand column between the two thumbnails, at the same height as the "⅓ → 76%" label, and build the ⅓ from that label as now. Let the inequality's ⅓ → ¼ swap happen next to the ¼ thumbnail, so the comparison reads left to right.
7. **[2:32–2:57][Motion + Sync]** The payoff is near-static and the band arrives early. Do not show Schelling's band at 2:41. Sweep it in from 35 % to 50 % in step with "between about a third and a half" (2:46.5–2:48.9). On "nearest square … emptier boards" (2:39–2:44), show one tile in the ⅓ thumbnail hopping to its nearest acceptable square. That replaces both 3.3 s static stretches with motion that encodes the different rule.
8. **[whole episode][Audio]** The pauses are metronomic. Regenerate the narration with variable gaps: 0.15–0.25 s between sentences that continue one thought (0:38.4→0:40.0, 1:13.1→1:14.7, 2:17.6→2:21.4), 0.8–1.0 s at beat boundaries (0:31.9, 1:14.7, 2:02.5, 2:32.2, 3:15.0), and the prediction holds unchanged. Slightly lower the Kokoro speed inside long clauses so the within-phrase rate falls from 184 to about 165 wpm.
9. **[0:56–0:59][Clarity]** The video says 238 unhappy but "200 moves", and never explains the gap. Change the line to "Round one takes two hundred moves — thirty-eight households became content before their turn — and the matching share jumps to sixty-four percent." Or add a grey "38 no longer need to" under the counter as it ticks from 238.
10. **[2:03–2:05][Visual]** The x-axis line draws across the town board. Start the axes' Create only after the town has finished shrinking into its thumbnail slot, or draw the axes from the left edge so they never cross the board.
11. **[2:43–2:57][Visual]** "random mix" straddles the band edge. Move the label to the left end of the dashed line (x ≈ 3–15 %), above the line, with a buff of 0.15.
12. **[0:55–1:50][Visual]** "plan: 0" is cryptic. Replace it with "plan predicts 0" set directly under the red counter, so 74 and 0 are read as a pair.
13. **[0:17–0:22][Clarity]** The video never says that empty squares do not count. Under the 3×3 patch, label the two empties "empty: not counted" in grey for the 1.5 s hold. Without that, the 8 → 7 denominator change at 1:29 is left for the viewer to infer.
14. **[3:22–3:23][Visual]** The end-card Ω uses the "blue households" hue. Make it ink or grey so blue keeps one meaning for the whole episode.

REACHES 9 IF ALL FIXED: yes, narrowly. Fixes 1–8 lift Visual and Motion to about 9 and Clarity to about 9. Originality reaches 9 only through fix 2 (the fraction-ladder picture). The re-score would be about Hook 9, Clarity 9, Visual 9, Motion 9, Audio 8.5, Concision 9, Originality 9, giving a weighted score of about 9.0. Without fix 2 the episode stays at about 8.8: polish alone does not get it there, because it needs a general picture for why ⅓ tips and ¼ does not.

## KEEP
1. The cold open, with the "? demanded" marker parked at 76 % and the 2 s hold, and the landing that returns to the identical frame with the marker reset to "?".
2. The single-household domino told with real simulation tiles and fractions built from the tiles (3/8 ≥ ⅓ → "?" pause → 2/7 < ⅓), including the "?" placeholder that never shows a false inequality.
3. The object continuity: tiles flying back on "Rewind", the preview arc that becomes the real move, and thumbnail → chart dot → full town.
