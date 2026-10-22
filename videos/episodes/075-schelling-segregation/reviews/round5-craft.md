EPISODE: 075 — "Mild Preferences, Extreme Segregation" (on-file title: "Mild Preferences, Segregated Towns")
REVIEWER: craft critic (visual design, motion, A/V sync), review round 1, against final.mp4 of 2026-10-16 01:12
IDEA: In Schelling's model, households that demand only a third of their neighbors match still build a town where three quarters match, because each departure tips a neighbor who was content; so a segregated map cannot tell you what its people wanted.

SCORES: Hook 9 · Clarity 8.5 · Visual 8 · Motion 8.5 · Audio 8.5 · Concision 8 · Originality 9
WEIGHTED: 8.5   AFTER CEILING: 8.5 (lowest 8 + 2 = 10, does not bind)
CAPS: none. Checked and not triggered:
- Overlap: the 3:04.8–3:05.4 label cross-fade overlaps for about 0.5 s mid-animation. No held frame overlaps, and the layout audit found 0 issues in 231 settled frames. Listed as fix 4.
- Bullet slide: the 3-line grey block at 3:00–3:08 is not the main visual. Listed as fix 2.
- Citations: both empirical claims carry one on screen (Schelling @ 2:55, Aaronson et al. @ 3:29).
FINAL: 8.5   PASS: no

FACTS:
- 76 % final share ("three quarters") | Verified | sim_output.txt: 0.7553
- Random start: half match (50 %) | Verified | 0.4992
- 238 unhappy at the start, "about one in six" | Verified | 238/1440 = 16.5 %; ladder bars below ⅓ sum to 23+15+23+11+23+76+67 = 238
- Round 1: 200 moves, share 64 % | Verified | sim: moves [200, …], share 0.6441
- 74 unhappy after round 1, 67 of them content at the start | Verified | sim: "never unhappy at start: 67"
- Chain fractions 3/8 → 2/7 for B, C, D; 3/8 ≥ ⅓ and 2/7 < ⅓ | Verified | arithmetic + verify_chain()
- "2 of 6 match" (empties not counted); "outnumbered two to one" ⇔ ⅓ | Verified | arithmetic
- Round 7 is the last move, then 0 unhappy | Verified | moves per round 200, 72, 41, 16, 9, 2, 1
- ¼ → 58 %, ⅓ → 76 % for the same start | Verified | 0.5787 / 0.7553
- At ¼, 95 start unhappy (238 − 76 − 67) | Verified | arithmetic; ¼ is content because the rule is ≥
- Ladder counts 76 / 67 / 125 | Verified | share_ladder(init(3))
- Schelling 1971, J. Math. Sociology; households move to the nearest satisfactory vacancy; 25–30 % vacancies | Verified | JMS 1(2):143–186 pp. 154–155 (confirmed by web search: "moves to the nearest vacant spot")
- Schelling's jump between about a third and a half (35–50 %) | Verified | JMS 1971: "a rapidly rising function of demands in the range from about 35% to 50%" (confirmed by web search)
- "One study finds that 1930s federal lending maps increased racial segregation for decades … reduced credit in the areas marked in red" | Verified | Aaronson, Hartley & Mazumder 2021, AEJ: Economic Policy 13(4):355–392. The abstract reports increased segregation and lasting effects "through reduced credit access".
- "As Schelling argued … the map alone could not have told you" | Verified (paraphrase) | JMS 1971 abstract: "inferences about individual motives can usually not be drawn from aggregate patterns"

MECHANICS: runtime 3:50.4 · wpm 154 (speech time) · max silence 1.96 s (planned prediction holds @ 0:09.2 and 3:20.0) · max static 3.5 s (3:24.9–3:28.4) · −14.0 LUFS / −1.7 dBTP · leading 0.00 s, trailing 1.73 s · WER 0.4 % · 0 banned phrases. No mechanical cap triggered. The runtime is 9.6 s under the 4:00 limit.

WHAT WORKS (evidence)
- Hook @ 0:00–0:12. Frame 1 is the finished town. The meter is drawn at 76 %, the purple "? demanded" marker appears on "demand" @ 0:07–0:09, and a real 2.0 s hold follows (0:09.2–0:11.1) before "Just a third". The viewer commits to a likely-wrong guess by 0:11. This is the misconception-first opening, done properly.
- Measured failure @ 0:57–1:15. "plan predicts 0" sits directly under the live counter, which stops at 74. At 1:11 every content tile dims, leaving the 67 red rings ("67 content at the start"). This is the clearest Stuff-Made-Here beat in the series so far.
- Domino replay @ 1:15–1:49, with real tiles and real moves. The board's corner and the inset stay in step (kf 1:36.7, 1:44.4). The fraction copies come from the tiles, and the red 3×3 frame appears exactly when a household tips. Red means "unhappy" everywhere it appears (checked 1:19.6, 1:40.5, 2:35.3, 2:53.4), and gold in the numerator always means gold neighbors.
- Continuity: the town shrinks into the thumbnail that becomes the (33, 75) dot (2:01–2:03), the dot chart's x-axis morphs into the ladder baseline (2:17–2:21), and the ending returns to the exact opening frame (kf 3:48.9 vs 0:05.9).
- The two-town test @ 3:08–3:27 (two boards at 76 %, one from a preference and one from a rule, then a 1.5 s hold) is the memorable, shareable image the episode needed.

PROBLEMS (evidence)
- [2:27–2:53] The ladder frame is the most crowded in the episode. At 2:43 (kf 2:53.4, sheet 10) it holds 14 bars, the counts 76/67/125, the fractions ¼, 2/7, ⅓, 3/8, the ends 0 % and 60 %, the "lose one match" arrow, "unhappy 238", A's 3×3 patch with its inequality, two town thumbnails with "⅓ → 76 %" and "¼ → 58 %", the title and the axis title. That gives three competing focal regions: bars, patch and thumbnails. This is the one place a viewer needs a rewatch.
- [2:16–2:53] The ladder has no vertical quantity. The bars show household counts, but nothing on the vertical says so. Only three bars carry numbers, and the title "households by share" is the only hint (§5: every axis carries a quantity name).
- [3:00–3:08] (kf 3:07.7) Prose on screen: "Schelling's jump: 35–50%", "his rules: nearest square", "25–30% empty (ours: 10%)", the citation, "random mix" and both axis titles add up to about 22 words of prose (cap: 12). The three grey lines form a stacked text block. The grey 35–50 % band is drawn over our own dots, so for a moment the chart reads as our data inside Schelling's band.
- [1:44.8–1:45.2] The inequality "2/7 < 1/3" turns into "3/8 ≥ 1/3" by glyph morph in about 0.3 s. The frame at 1:45.0 shows mangled shapes: a broken "2", "7" merging into "8", and "<" folding into "≥". This is faster than the 0.4 s tracking floor, and the script itself promises "every digit change cross-fades in place, with no glyph morph."
- [3:04.8–3:05.4] "our jump" cross-fades into "Schelling's jump: 35–50%" in the same spot. For about 0.5 s the two labels are superimposed, and the bracket's left cap slides through "35–50%" (my crops at 3:04.8 and 3:05.0).
- [1:17–1:25] Salience. On "this gold household had 3 gold neighbors out of 8" the subject, B (the centre of the white 3×3), has no marker of its own. Neighbor A's thick red ring (kf 1:19.6) is the strongest element in the inset, so the eye lands on the wrong tile until "Then this neighbor moved away" (1:25.6).
- [2:00.5–2:03] "That whole town is one point on this chart" is spoken while the frame holds only the shrinking board on an empty field (my frame at 2:01.0). The axes appear at about 2:03, so "this chart" lands at the edge of the ±2 s window.
- [2:07.7–2:16] "Demand a quarter … fifty-eight percent. Demand a third …": neither the 25 % nor the 33 % column is highlighted, and the thumbnails have no visual link to their columns. The viewer has to find the columns alone.
- [1:03–1:07] "this counter would read zero": the counter gets no highlight on "this". The deictic relies on the viewer already watching the HUD.
- [3:15.3] "In the other," lasts about 0.57 s (my audio energy trace: 195.36–195.93 s), and whisper dropped "other" entirely. Kokoro rushed the clause, so the contrast word of the test is swallowed.
- [0:33–1:15] Composition. The HUD hugs the top right, which leaves the lower-right quadrant (about 40 % of the frame) empty for 40 s (kf 0:48.6, 1:13.3). [1:16–1:18] For 2 s the frame is mostly empty while the board parks and before the inset flies out (sheet 5, 1:17). Both are nitpicks.
- Concision. At 3:50 the episode is 10 s under the cap, with 12 beats. A few phrases restate what the picture already shows: "So most households are content." (0:40.8), "Round after round, the tipping spreads," (1:51) and "Seventy-six percent, the town we started with" (1:57, while the meter already reads 76 %).

FIXES (highest impact first):
1. [2:16–2:53][Visual/Clarity] The ladder frame is overloaded with three focal regions → fade both thumbnails and their "⅓ → 76 %" / "¼ → 58 %" labels to 0 on "sort" (2:16), and bring them back on the reverse morph (2:45). Move A's patch and its inequality to the vacated right column, vertically centred on the baseline. Show only the counts the narration speaks at each moment: 67 and 125 from 2:34, and 76 from 2:41.
2. [3:00–3:08][Visual] There are about 22 words of prose, and the band sits over our dots → replace "his rules: nearest square" and "25–30% empty (ours: 10%)" with one 5-word grey label, "nearest move · 30 % empty", under "Schelling's jump: 35–50%". While the band is shown, dim our dots and mean ticks to 35 % and give the band a hatched fill, so it reads as a different model and not as our data.
3. [1:44.8–1:45.2][Motion] There is a 0.3 s glyph morph with mangled shapes → replace the Transform with a per-glyph FadeTransform, or a fade-out then fade-in in place, at run_time ≥ 0.6 s, as the script specifies. Apply the same treatment to every inequality change in the replay (1:29–1:49).
4. [3:04.8–3:05.4][Visual/Motion] The labels overlap and the bracket cap crosses the text → first FadeOut "our jump" (0.3 s), then slide the bracket to 35–50 %, then Write "Schelling's jump: 35–50%" once the bracket has stopped. Keep ≥ 0.15 units between the bracket's left cap and the label throughout.
5. [1:17–1:25][Clarity/Visual] The subject household has no marker → on "this gold household" (1:17.4), give B a 4 px white inner outline, and keep A's red ring at 50 % opacity until "Then this neighbor moved away" (1:25.6), then bring it to full as A departs.
6. [2:00.5–2:03][A/V sync] "this chart" is spoken before the chart exists → start the axes' Create 1.5 s earlier so they are fully drawn by 2:01.0, with the thumbnail copy landing on the dot on "point" as now.
7. [2:07.7–2:16][Clarity] The spoken columns are not marked → on "a quarter" draw a thin grey leader from "¼ → 58 %" to the 25 % column and raise that column to full opacity while the other columns dim to 40 % (0.6 s). Repeat for ⅓ on "a third".
8. [2:16–2:53][Visual] The ladder's vertical is unnamed → add a grey label "households" at the left end above the baseline (Text ≥ 18), or one tick "100" with a short vertical scale line.
9. [1:03–1:07][A/V sync] Add an Indicate on the unhappy counter (scale 1.15, 0.8 s, RED) that lands on "this counter".
10. [3:15.3][Audio] "In the other" is swallowed → regenerate that beat with "In the second, nobody minds their neighbors at all." and a 0.25 s pause after "a third". Re-check that whisper now transcribes "second".
11. [Concision] Cut "So most households are content." (0:40.8), "Round after round, the tipping spreads," (1:51) and "Seventy-six percent, the town we started with" (1:57; the meter already shows it). This saves about 5 s and moves the runtime away from the 4:00 cap.
12. [0:33–1:15][Visual, nitpick] Centre the HUD block vertically against the board (move it down about 1.2 units) so the frame balances. At 1:16–1:18, start the inset flying out as the board parks instead of after it.

REACHES 9 IF ALL FIXED: yes, but only narrowly. Fixes 1–5 lift Visual to 9, Motion to 9 and Clarity to 9. Fixes 9–10 lift Audio to 9 and fix 11 lifts Concision to 8.5, which gives a weighted score of about 9.0. No structural change is needed: the hook, the failure beat and the visual insight are all present and strong. What remains is density control in the ladder and Schelling beats and the polish of a few transitions.

KEEP:
- The cold open and the exact-frame return: the finished town, the meter at 76 %, "? demanded", the 2 s hold, and the same frame at 3:43–3:50.
- The measured failure beat: "plan predicts 0" under the live counter stopping at 74, then dimming to the 67 that never moved.
- The two-town test (3:08–3:27): two boards at 76 %, one from a preference and one from a rule, with a hold before the reveal.
