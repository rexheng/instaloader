# Episode 75, round 3: craft review (motion, visual design, A/V sync)

Evidence used: `review/` pack (metrics.json 21:49 is newer than final.mp4 21:47, so it was reused), all 14 contact sheets, 14 full-resolution keyframes (kf_03, 05, 08, 11, 14, 16, 20, 22, 26, 27, 32, 36 and others), plus 28 extra frames I pulled with ffmpeg at 0:00.3, 0:02.0, 0:34.3, 0:44, 0:52, 1:03.5, 1:17.5, 1:48–1:52.5 (every 0.5 s), 2:02.5, 2:04, 2:20, 2:25.5, 2:34.6, 2:35.5, 2:36.5, 2:55.0, 3:16, 3:17.5, 3:30 and 3:49 (`/tmp/claude-0/ep75r3/`). I also used transcript_words.tsv, script.md, facts.md and sim_output.txt, and checked Schelling 1971 p.159 against the online PDF.

```
EPISODE: 075 — "Mild Preferences, Segregated Towns"
IDEA: In Schelling's model, households that demand only a third of their neighbours match still produce a town where three quarters match, because each move away tips a neighbour who was content; so a segregated map cannot tell you what its residents wanted.
SCORES: Hook 9 · Clarity 9 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8 · Originality 9
WEIGHTED: 8.7 (135 + 225 + 127.5 + 127.5 + 85 + 80 + 90 = 870 / 100)   AFTER CEILING: 8.7 (lowest 8 + 2 = 10, does not bind)
CAPS: none. I checked these and none triggers:
  - overlap: the layout audit is 0/237. The only text-on-text contacts are in motion: ⅓ flies through "¼ → 58%" @ 2:35.5, and ghost dots cross the ladder title @ 2:55.0.
  - citations: Schelling is on screen 2:56–3:16 and Aaronson et al. 3:37–3:47, both ≥ 3 s.
  - banned phrases: 0.
  - mechanics: all in range.
FINAL: 8.7   PASS: no
```

## FACTS
| Claim | Verdict | Source |
|---|---|---|
| Final town 76 % match (0.7553); random start 50 % (0.4992) | Verified | sim_output.txt "share by state" |
| 238 unhappy at start, "about one in six" (16.5 %) | Verified | sim_output.txt; 238/1440 = 0.165 |
| Round 1: 200 moves, 64 %, 74 still unhappy, 67 of them content at the start; on screen "38 fixed by neighbors' moves" | Verified | sim_output.txt round-1 breakdown (200 + 38 = 238) |
| Chain A→B→C→D: 3/8 → 2/7 at each step, leaving in rounds 1–4 | Verified | sim_output.txt chain rows; I checked the inset tiles @ 1:31 and 1:45.9 square by square (2 gold of 7) |
| "after round seven, nobody wants to move" | Verified | moves per round 200, 72, 41, 16, 9, 2, 1; unhappy after round 7 = 0 |
| "2 of 6 match" example is content at ⅓ | Verified | 2/6 = ⅓, and the rule is ≥ |
| Demand ¼ → 58 % (same start); 30 towns per demand, 0–60 % | Verified | sim_output.txt (0.5787; means 0.500 … 0.965) |
| Ladder: 238 left of ⅓; rungs ¼ (76) and 2/7 (67); 95 at ¼ | Verified | share ladder sums to 23+15+23+11+23 = 95, and 95 + 76 + 67 = 238 |
| Schelling 1971 ran this model; nearest square; 25–30 % vacancies; jump "about 35 % to 50 %"; slight at about one third | Verified | Schelling 1971, JMS 1(2):143–186, pp.154–159 (PDF text: "rising function of demands in the range from about 35% to 50%", "slight when the demand is for about one-third") |
| Quote "inferences about individual motives can usually not be drawn from aggregate patterns" | Verified | Schelling 1971 abstract |
| HOLC maps cut credit and increased racial segregation for decades | Verified | Aaronson, Hartley & Mazumder 2021, AEJ: Economic Policy 13(4):355–392 |
| Two towns both 76 % (0.7553 vs 0.7554); left town "placed by a rule" | Verified (simulated, labelled) | sim_output.txt zoned town |

## MECHANICS
runtime 3:56.4 · 156 wpm (speech) · max silence 1.97 s (the planned prediction hold at 0:09.9) · max static 3.3 s (3:18.9) · −14.0 LUFS / −1.7 dBTP · leading silence 0.0 s, trailing 1.75 s · WER 0.4 %

## What I saw (flipbook notes)
- **Hook (0:00–0:12).** The finished town is on screen in frame 1. The meter shows 76 % before the narration says it. The PURPLE "? demanded" marker appears at 0:09, followed by a 2.0 s commit pause, and "Just a third" lands at 0:11.8. This is exact. The landing at 3:49–3:56 rebuilds this frame pixel for pixel. One nit: at 0:02.0 the meter reads "1 % match" while it counts up from 0. That implies the town once matched 0 %, but the true starting point, shown 30 s later, is 50 %.
- **Naive plan and failure (0:33–1:16).** The rewind sends every tile flying home (0:34.3), which is a meaningful transform. RED rings mark the 238. The real round-1 move is previewed as a dashed arc (0:52). The counter stops at 74 above "plan predicts 0", in a clean two-column HUD (kf_11). On "sixty-seven" the content tiles dim, which reads well. The "38 fixed by neighbors' moves" note (1:03–1:11) is never spoken and competes with "If the plan had worked, this counter would read zero".
- **Domino (1:16–1:52).** This is the best stretch of the episode. The board's corner and the inset stay in step, and tile copies fly into the numerators. The "?" state dims the stale fraction. D's 3/8 ≥ ⅓ holds about 2 s, the departure lands on "tips" (1:49.6–1:50.0), and 2/7 < ⅓ holds about 2 s into "Now run the whole town" (frames 1:48.0–1:52.5). The round-2 timing complaint is fixed. Deictics land: "this neighbor moved away" as A empties at about 1:28, and "Its neighbor here" as the box recentres on C at 1:37–1:39.
- **Cascade and chart (1:52–2:18).** The counter reaches 0 on "nobody". The town shrinks to a thumbnail and a copy becomes the dot at (33.3, 75.5) on "one point" (2:04–2:05.8). This is a strong correspondence.
- **Ladder (2:18–2:55).** The logic is now right: the counts are visible, the "lose one match" arrow runs from 3/8 to 2/7, the tick slides from ⅓ to ¼ and two rungs turn grey, 238 → 95, and A's inequality flips. The picture itself is the weakest frame in the film (see fix 1). The bars occupy only the band y ≈ 450–760 px, with the upper-left 40 % of the frame empty. There is no baseline, so short bars float on their tick stubs. The PURPLE demand marker is drawn *inside* the grey rung bar (kf_26 at x ≈ 768 px; kf_27 at x ≈ 637 px), so it reads as a purple sub-bar of households rather than a threshold.
- **Schelling (2:55–3:16).** The bracket slides from "our jump" to the 35–50 band exactly on "between about a third and a half", which is honest and well synced. The ladder-to-chart change at 2:55.0 is a muddy cross-dissolve: blurred dots appear over "households by share (simulat●d start)" and beside "unhappy 95". In the settled frame (kf_32) the band label "Schelling's jump: 35–50%" is crammed against the y-title "neighbors matching (%)" on a staggered baseline (x 708→745 px, y 75 vs 100 px), and the band fill is heavy.
- **Two-town test (3:16–3:47).** This is a memorable and original device. The labels travel above the boards and no longer cross them. In the settled frame (kf_36) the two headers sit on different baselines ("0 demanded" ≈ 135 px, "⅓ demanded" ≈ 155 px), and the left header is not centred over its board: it starts at x = 160 px while the board spans 193–795 px.
- **Audio.** Cadence is natural, and the pauses at 0:09.9 (2.0 s), 1:29.8 (1.7 s), 2:45.0 (1.6 s) and 3:28.1 (2.0 s) are planned prediction holds. One real prosody failure is the HOLC sentence. Whisper hears "federal lending maps from the 1930s**.** By cutting credit to the areas**,** they marked red, increased…" (3:36–3:47). The voice drops at "1930s" (3:40.5) and breaks for 0.3 s between "areas" and "they" (3:42.8–3:43.1). By ear, "they marked red" parses as the main clause, and the actual verb "increased" arrives 11 words after its subject. "aggregate" heard as "aggregating" @ 3:14 is a soft nit: facts.md says the TTS chose the adjective reading.

## FIXES (highest impact first)
1. **[2:22–2:55][Visual + Clarity] The insight picture is small, has no baseline, and its threshold marker reads as a purple bar.**
   - Draw a GRAY x-axis line under the bar bases (stroke 2, full ladder width) so that short rungs such as 1/8 and 1/6 (n = 11–23) no longer float.
   - Replace the purple tick inside the rung bar with a PURPLE upward caret (a triangle about 0.18 units tall) between the axis and the fraction row.
   - Outline the threshold rung's own bar with a PURPLE stroke of 3 instead of overlaying it, and slide the caret and outline together ⅓ → ¼.
   - Scale the ladder group by about 1.35 and shift it up about 0.8 units into the empty upper-left. The bars then span roughly y ∈ [−1.4, 1.9], and the title sits at y ≈ 2.6.
   - Set the count labels (67 / 125 / 76) to `MathTex` font_size 32 (currently ≈ 27 px).
   - Effect: Visual +0.5.
2. **[3:36–3:47][Audio + Clarity] HOLC sentence garden-paths by ear (see transcript punctuation at 3:40.5 and the 0.3 s break at 3:42.8).** Rewrite with the subject next to the verb: "In real cities, one study finds that 1930s federal lending maps increased racial segregation for decades. They cut off credit to the areas marked in red." Pulse the zone lines on "increased" and again on "credit". Effect: Audio +0.5, no time cost.
3. **[3:09–3:56][Concision] The thesis is stated three times in 45 s:** Schelling's quote (3:09–3:15), the two-town test (3:16–3:47) and the landing line (3:48–3:55).
   - Cut the quote sentence "He wrote that inferences … aggregate patterns." That saves about 6 s and brings the runtime to about 3:50.
   - Let the two-town test carry the idea, and keep the landing as the single statement.
   - To keep the source, put it in the landing: "Schelling's point: whatever you guessed its people demanded, the map alone could not have told you."
   - Effect: Concision +0.5.
4. **[2:54.6–2:56.0][Motion] The ladder→chart cross-dissolve shows ghost dots over the ladder title and over "unhappy 95" (frame 2:55.0).**
   - Reverse the 2:19 morph: the bars shrink to the axis over 0.6 s and the x-title transforms back to PURPLE "demanded (% of neighbors)".
   - Only then do the dot clouds, y-axis and baseline FadeIn over 0.6 s.
   - Never show both charts at more than 0 opacity at once.
5. **[2:35.3–2:36.0][Motion] The PURPLE ⅓ that builds A's "2/7 < ⅓" flies straight through the "¼ → 58%" label (frame 2:35.5 shows "1/31/4" overlapped).**
   - Start the copy from the ⅓ in "⅓ → 76%" (top-right), which is the closer source and carries the same meaning, instead of from the axis label.
   - Alternatively, keep the axis source and give the copy `path_arc=-1.2` so it rises above the lower thumbnail.
6. **[3:07–3:16][Visual] Two headers collide at the top-left (kf_32) and the band is heavy.**
   - Move "Schelling's jump: 35–50%" inside the band, centred, at y = 2.9 under the bracket.
   - Cut the band fill opacity to 0.18 so the 40 and 50 dot clouds keep full contrast.
7. **[3:31–3:47][Visual] Two-town headers are misaligned (kf_36).**
   - Set the bottom of each header `align_to` the same y (0.25 above the board tops).
   - Centre "0 demanded · placed by a rule" on the left board's x-centre, or split it into "0 demanded" above and a GRAY "placed by a rule" under the board beside "76% match".
8. **[1:03–1:11][Clarity] The unspoken note "38 fixed by neighbors' moves" competes with the narrated counter.**
   - Fade it in only after "It reads seventy-four" (≈ 1:08.5), at GRAY 60 %.
   - Alternatively, add a 2 s clause after "Round one takes two hundred moves": "thirty-eight more were fixed before their turn".
9. **[0:01–0:04][Motion] The meter counts up from 0 % ("1 % match" @ 0:02.0)**, which implies a 0 % state that never existed. Fill from 50 %: show a dim GRAY tick at 50, labelled later as "random mix" at 0:36, and animate to 76. Alternatively, draw the bar at 76 with the number written on.
10. **[1:17–1:51][Visual] The dimmed board fills about 42 % of the frame for 34 s while all the action is in the inset.**
    - Scale the board to 0.7 and move it to the left edge, keeping the white focus box.
    - Grow the inset from about 530 px to about 680 px, and move the formula 0.4 units right.
    - The tiles and fractions then read at phone size.

**REACHES 9 IF ALL FIXED:** yes, narrowly.
- Fixes 1, 6 and 7 raise Visual to 9.
- Fixes 4, 5 and 9 raise Motion to 9.
- Fix 2 raises Audio to 9.
- Fix 3 raises Concision to 8.5.
- The result is 15·9 + 25·9 + 15·9 + 15·9 + 10·9 + 10·8.5 + 10·9 = 895, which gives 9.0 (8.95).

No structural change is needed. The cold open, the measured failure, the domino picture, the honest limits beat and the two-town reframe are all present. What remains is finishing work on the ladder frame, the transitions, one sentence and the final 45 s.

**KEEP:**
- The domino replay (1:16–1:52): the board corner and the inset move in step with the real simulated moves, and tile copies become the numerators.
- The two-town blind test (3:16–3:47), which is the episode's shareable image.
- The opening frame with the "? demanded" marker, rebuilt exactly as the last frame (0:07 ↔ 3:53).
