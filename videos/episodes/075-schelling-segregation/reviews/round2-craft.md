# Review: Episode 75, round 2 (craft critic: visual design, motion, A/V sync)

**Evidence.** `review/metrics.json` (16:17) is newer than `final.mp4` (16:15), so I used the existing `review/` pack. I read:
- report.md and all 13 contact sheets.
- Full-resolution keyframes kf_03, 05, 08, 10, 13, 16, 23, 25, 26 and 27.
- 30 extra frames I pulled with ffmpeg: 1:26.0–1:27.6, 1:43.6–1:48.6, 2:00–2:02, 2:40, 2:42, 2:56.5, 3:03, 3:04, 3:05, 3:29–3:31, 3:44.5–3:47.5.
- A pixel map of the rung labels at 2:50.4.
- The transcript, word timings, script.md, facts.md, narration.txt, the CHANGELOG and the round-1 craft review.

```
EPISODE: 075 — "Mild Preferences, Segregated Towns"
IDEA: In Schelling's model, households that demand only a third of matching neighbours still build a 76 %-matching town, because each departure tips a neighbour who was content, so a segregated map alone cannot tell you what its people wanted.
SCORES: Hook 9 · Clarity 8.5 · Visual 8 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.6 (855/100 = 8.55)   AFTER CEILING: 8.6 (lowest 8 + 2 = 10, does not bind)
CAPS: Text overlapping another element → 7. Rung labels "¼" and "2/7" on the share ladder sit on the x-axis line, and the "7" crosses it (pixel map: glyph rows 745–763 cross the axis line at y = 757–759, x ≈ 727–733; the "4" of ¼ merges into the axis at x ≈ 600–612) @ 2:41–2:50
FINAL: 7.0   PASS: no
```

The cap comes from one mispositioned pair of labels. Fixing it is one line of code. Without the cap the episode sits at 8.6. Round 1 fixed a great deal, and the remaining gap to 9 is real but small.

## FACTS

| Claim | Verdict | Source / check |
|---|---|---|
| Final town: on average 76 % of neighbours match (0.755) | Verified | sim_output / facts #1 |
| Rule: stay if ≥ ⅓ of occupied neighbours match = "happy to be outnumbered two to one" | Verified | same ≥ (same+diff)/3 ⇔ diff ≤ 2·same. The boxed example at 0:20 shows 2 gold, 4 blue and 2 × empties, so "2 of 6" checks |
| Random start: half match; 238 unhappy ≈ 1 in 6 | Verified | 238/1440 = 16.5 % |
| Round 1: 200 moves, 64 %; 238 − 200 = 38 "fixed by neighbors' moves" | Verified | 200 + 38 + 0 = 238 |
| Counter reads 74; 67 of them were content before round 1 | Verified | 67 + 7 = 74; on screen at 1:11–1:15 (67 red rings, 7 turn grey) |
| Corner chain: 3/8 ≥ ⅓ → 2/7 < ⅓, for A→B, B→C and C→D | Verified | recounted tiles at 1:20.4 (B: 3 gold of 8), 1:31–1:35 (2 of 7), 1:41.7 (C: 3/8), 1:44.6 (C: 2 of 7 with the empty square), 1:48 (D) |
| Settles in round 7 at 76 % | Verified | sim |
| 30 towns per demand; same start at ¼ → 58 %, at ⅓ → 76 % | Verified | sim (0.579 / 0.755) |
| Share ladder: 14 values k/n ≤ 0.6; bars left of ⅓ sum to 238; ¼ (76) and 2/7 (67) are the only rungs in [¼, ⅓); 238 − 76 − 67 = 95 | Verified | 23 + 15 + 23 + 11 + 23 = 95, and 95 + 76 + 67 = 238. The bar heights at 2:38 are proportional to the counts (½ bar ≈ 310 px vs 0-bar ≈ 27 px, ratio 11.5 vs 256/23 = 11.1) |
| A at the start: 2 gold of 7; 2/7 < ⅓ but 2/7 ≥ ¼ | Verified | 0.286 vs 0.333 / 0.25; tiles at 2:38 |
| Schelling 1971 ran it by hand on a checkerboard; moved to the nearest satisfying square; 25–30 % vacancies; rapid rise between about 35 % and 50 % | Verified | Schelling 1971, *J. Math. Sociol.* 1(2):143–186, pp.154–159 as quoted in facts.md; the round-1 critic confirmed the passage independently |
| Quote: "inferences about individual motives can usually not be drawn from aggregate patterns" | Verified | 1971 abstract, verbatim |
| 1930s federal (HOLC) lending maps increased racial segregation for decades ("one study") | Verified | Aaronson, Hartley & Mazumder 2021, *AEJ: Economic Policy* 13(4):355–392; the abstract says "increased racial segregation in later decades" |
| Two towns both 76 % (0.7553 / 0.7554), one with zero demand | Verified (simulated, a toy) | sim.py `zoned_town`; the narration says "simulated", but the frame has no tag (fix 6) |

Both sources are cited on screen: Schelling at 2:53–3:15 and Aaronson et al. at 3:36–3:44, both bottom-left above y = −3.2 and both held more than 3 s. I found no wrong number.

## MECHANICS
runtime 3:52.9 · wpm 155 (speech) / 180 (excluding pauses) · max silence 1.97 s (0:09.9, the planned prediction hold) · max static 3.53 s (3:32.7) · −14.0 LUFS / −1.7 dBTP · leading 0.00 s / trailing 1.75 s · WER 0.0 % · banned phrases 0. No mechanical cap.

**Pattern sweep.**
- No question chains: each question stands alone (0:08, 0:28.8, 1:28.3, 2:19.3, 3:25.5).
- No "it turns out", fake reveals or recap ending.
- "That cuts both ways" is the only signpost-like line, and it is earned by the test that follows.

**Hook.** The question "How much matching do they demand?" lands at 0:08–0:11.8. The "? demanded" marker is parked at 76 %, which plants the wrong guess, and a 2 s hold follows. This is a commit by 0:12.

## What the frames show

**Works.**
- **Object continuity carries the argument.** Tiles fly back to their random start on "Rewind" (0:33–0:37), and the meter falls 76 → 62 → 50 with them. The dashed preview arc becomes a real move. Tiles fly into the numerator (1:20–1:23). The town shrinks into the thumbnail, then a copy becomes the chart dot on "point" (2:00–2:03.5). The thumbnail grows back into the exact opening frame (3:44–3:48), and the marker returns to "?".
- **Domino round 2 is fixed.** At 1:17 the board dims to about 30 % and the HUD fades. The inset is about 540 px wide. Each departure puts "?" in the relation and dims the old numbers in one move, so no stale inequality appears. The "?" lands at 1:29 on "Is it still content?", and A's departure starts on "away" (1:27.6).
- **The share ladder (2:21–2:50) is the episode's new one picture.** The demand line sweeps from ⅓ to ¼, two rungs flip from red to grey, and the counter reads 238 → 171 → 95. A's 2/7 flips from < to ≥.
- **The two-town test (3:15–3:44) is a genuine Veritasium move.** It has a prediction hold (3:27.6–3:29.6) and a reveal in which the zone lines draw on.
- **Deictics land within ±1 s.** I checked "these 238" (0:43.7, rings draw), "this counter" (1:05), "this gold household" (1:19), "this neighbor" (1:26.3 → departure at 1:27.6), "Its neighbor here" (1:37.6, box moves to C), "this chart" (2:03.5), "left of the line" (2:30), "This one" (3:29.6, box on the right town at 3:30) and "between about a third and a half" (the band sweeps 3:04–3:06).
- **Palette discipline holds across 3:53.** The six hues are blue/gold households, red for unhappy (always a ring or a count), purple for demand, ink for the outcome, and grey for context. There is no red/green pair, and the end-card Ω is now ink.

**Defects (with evidence).**
1. **Rung labels touch and cross the x-axis (2:41–2:50, kf_27, my 2:42 frame).** The "¼" label's denominator rests on the axis line. The "2/7" label's "7" crosses it and runs down to y ≈ 763, between the tick marks. The 2/7 label is also centred at x ≈ 731, exactly midway between the 2/7 bar (x ≈ 695) and the ⅓ bar (x ≈ 768), so its referent is ambiguous. This triggers cap 7.
2. **The ladder bars sit on a percent axis (2:21–2:50, kf_25/26/27).** The bars encode household counts, but the dimmed y-axis still reads 40/60/80/100 "neighbors matching (%)". The ½ bar (256 households) reads as "≈ 70 %" against it. The bars have no count scale or count labels: §5 requires every axis to carry a quantity name and unit. "but they're crowded" (2:43–2:45) asks the viewer to judge bar heights that have no numbers. The counter's 238 → 171 → 95 rescues the claim, but the picture alone does not.
3. **The general mechanism is still one step implicit (2:28–2:50).** The ladder shows which households start unhappy. The reason the cascade fails at ¼ is not drawn: a 3/8 household (the tallest left-side rung, 125) that loses one same-colour neighbour lands on 2/7, which is red at ⅓ and grey at ¼. The episode says this only for A ("that chain never starts"). The domino and the ladder are both on screen, but the arrow linking them (3/8 → 2/7) is missing. That is the line that would make the jump re-derivable.
4. **Round 3 is rushed (1:45.3–1:48.4).** D's "3/8 ≥ ⅓" is readable for about 1.1 s (1:45.3 → "?" by 1:46.5), and C's resolved "2/7 < ⅓" for about 0.8 s (1:44.4–1:45.2). §5 asks for ≥ 2 s + 0.4 s per term on an equation. The viewer cannot recount D's eight tiles before they change.
5. **Stale minimap (1:40–1:50).** The full-brightness focus box on the dimmed board still shows the after-round-1 patch, with B present and ringed. The inset meanwhile says "after round 2/3" and shows B's square empty (my 1:44.6 frame). The fix for this was half applied in round 2.
6. **The two-town frame has no "simulated" tag (3:15–3:44).** The narration says "simulated", but the frame does not. Every other town frame carries the grey tag.
7. **Label flight crosses a board (3:30.2–3:31.5).** "0 demanded" flies straight across the left town's tiles (sheet 12 at 3:31; my 3:30.5 frame), and "· placed by a rule" fades in before its noun arrives.
8. **The HUD column is ragged (0:58–1:16, kf_10).** "76% match", "unhappy 74", "plan predicts 0", "round 1" and "67 content at the start" each sit on a different horizontal anchor, with no common edge.
9. **Near-static stretch (2:52.3–2:55.5).** It runs under "ran this model by hand, on a checkerboard". Only the citation fades in; nothing on screen refers to "by hand" or "checkerboard".

## FIXES (highest impact first)
1. **[2:41–2:50][Visual] Rung labels sit on and cross the x-axis; the 2/7 label is equidistant from two bars.** Place each label with `label.next_to(bar, UP, buff=0.15)`, centred on its own bar's x: ¼ above the bar at x = 25, 2/7 above the bar at x = 28.6. Use `MathTex` font_size 30. If space is tight, lift both to a common y just above the taller of the two bars. This removes cap 7 and makes the final score about 8.6.
2. **[2:21–2:50][Visual + Clarity] Count bars are read against a % axis.**
   - When the ladder rises (2:22), fade the y tick labels 40/60/80/100 and the y title to 0, rather than 30 %.
   - Write the count above every red/grey rung that the narration names: "76" on ¼, "67" on 2/7, and "125" on 3/8 (see fix 3), in GRAY, `MathTex` 28.
   - Keep the caption "households at each share (start)" as the bar axis title.
   "but they're crowded" then points at visible numbers.
3. **[2:38–2:50][Clarity] Make the cascade step general, not anecdotal.**
   - At ⅓ (2:31–2:37), draw a curved GRAY arrow from the 3/8 rung to the 2/7 rung, labelled "lose one neighbor". The arrowhead lands on a red bar.
   - When the line slides to ¼, the 2/7 bar turns grey under the arrowhead.
   - Narration after "at two sevenths.": "Every household at three eighths is one departure away from it." That is about 2.5 s at 155 wpm.
   - Pay for the time with fix 8.
   The viewer can then re-derive why ⅓ cascades and ¼ does not. This is worth about Clarity +0.5 and Originality +0.
4. **[1:44.4–1:48.4][Motion] Round 3 is too fast to read.** Increase the `[pause 0.5]` before "In round three" to 1.0 s, so C's "2/7 < ⅓" holds at least 1.3 s. Then start the round-3 departure only after D's "3/8 ≥ ⅓" has been visible for 1.5 s: delay C's exit to the word "tips" (1:47.2) instead of about 1:46.4. This costs about 0.8 s.
5. **[1:40–1:50][Visual] Stale minimap.** Animate the 4×5 tiles inside the board's white focus box in the same `AnimationGroup` as the inset departures (B, then C, become empty squares). Alternatively, dim the focus box to the board's 30 % once the inset is up.
6. **[3:15–3:44][Visual] Two-town frame lacks "simulated".** Add the same GRAY "simulated" tag (Text 18) centred above the gap between the two towns at y ≈ 3.3, faded in with the cross-fade.
7. **[3:30.0–3:31.5][Motion] Label flies through the left board.** Give "0 demanded" a `path_arc` up and over (via y ≈ 3.4), or fade it out in the gap and fade it in above the left town. Start "· placed by a rule" only after "0 demanded" has landed, so the two arrive as one phrase.
8. **[2:50.6–2:57.2][Concision + Motion] Static stretch under a line with no visual.** Cut "by hand, on a checkerboard" so the line reads "In his 1971 paper, Thomas Schelling ran this model." This saves about 2 s, offsets fix 3 and removes the 3.2 s static stretch at 2:52.3. If you keep the words, show them: on "checkerboard", draw a 13×16 grey grid outline over the ⅓ thumbnail for 1.5 s.
9. **[0:58–1:16][Visual] Ragged HUD.** Right-align "unhappy N", "plan predicts 0", "round N" and the note to the meter's 100 % end (x ≈ 5.0). Put the numbers in one column so that "0" sits under "74".

**REACHES 9 IF ALL FIXED:** yes, narrowly.
- Fix 1 alone removes the cap and gives 8.6.
- Fixes 2 and 3 lift Clarity to 9 and Visual to about 8.5–9.
- Fixes 4, 5 and 7 lift Motion to 9.
- Fix 8 keeps the runtime under 4:00 and lifts Concision.
- The result is about 15·9 + 25·9 + 15·9 + 15·9 + 10·8.5 + 10·9 + 10·9 = 8.95–9.0.

No structural change is needed. The hook, the fail, the one picture, the payoff and the landing are all present and work.

**KEEP:**
- The cold open, with "? demanded" parked at 76 %, and the identical landing frame.
- The tile-built domino with "?" on each departure.
- The ⅓ → ¼ ladder sweep with its 238 → 171 → 95 counter, and the two-town blind test.
