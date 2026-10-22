EPISODE: 075 — "Mild Preferences, Segregated Towns"   (round 6, craft critic: visual design / motion / sync)
IDEA: In Schelling's model, households that demand only a third of their neighbors match still build a town where three quarters match, because each departure drops a content neighbor from 3/8 to 2/7, so a segregated map cannot tell you what its residents wanted.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.6 (8.55)   AFTER CEILING: 8.6 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none. (The end ident dissolves in over the still-visible board at 3:32.5–3:33.3. I read that as a transition, not a held overlap, and did not apply cap 7. It is fix 3.)
FINAL: 8.6   PASS: no

Evidence used: review/ pack (metrics.json 19:57 is newer than final.mp4 19:55), report.md, all 12 contact sheets, 15 keyframes (kf_02, 04, 08, 10, 14, 18, 22, 23, 26, 27, 30, 32, 35, 40), extra frames at 0:01.0, 0:12.3, 1:12.4, 1:50.0, 2:04.6, 2:28.8, 3:09.6 and 3:32.9, and 2 fps / 1 fps motion strips over 1:41–1:46 and 3:23.5–3:33.5. I also read the transcript, script.md, facts.md and sim_output.txt.

FACTS:
- Final town: 76 % / "three quarters" match | Verified | sim_output: share 0.7553
- Rule: content if same/occupied ≥ 1/3, empties not counted; "2 of 6 match" box | Verified | sim; boxed 3×3 at 0:22 shows 2 gold, 4 blue, 2 × (kf_04)
- "happy to be outnumbered two to one" | Verified | s/(s+d) ≥ 1/3 ⇔ d ≤ 2s
- Random start: half match, meter 50 % | Verified | 0.4992
- 238 unhappy at the start | Verified | ladder bars below 1/3: 23+15+23+11+23+76+67 = 238
- Round 1: 200 moves, 38 content by their turn | Verified | round1_breakdown {moved 200, content_before_turn 38, no_destination 0}
- Counter reads 74, not 0; 67 of them were content before round 1 | Verified | unhappy by state [238, 74, …]; "never unhappy at start: 67"
- Chain: B 3/8 → 2/7 after A leaves; C 3/8 → 2/7 after round 2 | Verified | verify_chain rows r0–r2; inset tiles in kf_14 and kf_18 match (2 gold of 7, the vacated square shown empty)
- "After round seven nobody wants to move" | Verified | moves per round 200, 72, 41, 16, 9, 2, 1 → 0 unhappy
- ¼ → 58 %, ⅓ → 76 % (same start) | Verified | 0.5787 / 0.7553
- "only shares up to 60 %" with ≤ 8 neighbors | Verified | the 14 values k/n ≤ 0.6 for n ≤ 8; bar x-positions in kf_23 measured linear to within 2 px (0→139 px, 0.6→1192 px)
- Bar counts 67 (2/7), 125 (3/8), 76 (¼); 238 − 76 − 67 = 95 | Verified | share_ladder; bar heights measured ≈ 1.69 px per household, consistent
- Schelling 1971, JMS: nearest satisfactory vacancy, 25–30 % vacancies, jump "from about 35 % to 50 %" | Verified | paper PDF p.155 via web search ("rapidly rising function of demands in the range from about 35% to 50%")
- "As Schelling argued … the map alone could not have told you" | Verified (paraphrase) | JMS 1971 abstract: inferences about individual motives "can usually not be drawn from aggregate patterns"
- Aaronson, Hartley & Mazumder 2021, AEJ: Economic Policy: HOLC maps increased racial segregation in later decades, through reduced credit access | Verified | abstract (doi 10.1257/pol.20190414)
- Rule-made town also at 76 % | Verified | zoned town share 0.7553

MECHANICS: runtime 3:33.8 · wpm 153 (speech time) · max silence 2.08 s (0:09.1 and 3:06.4, both planned prediction holds) · max static 3.8 s (2:56.4–3:00.2) · −14.0 LUFS / −1.8 dBTP · leading 0.00 s, trailing 1.65 s · banned phrases 0 · WER 0.4 %. Two sentences run above 200 wpm: 3:24.0 "Look again at the first town…" (215) and 1:48.4 "That whole town is one point on this chart" (208). The longest stretch without a ≥ 0.35 s breath is 14.7 s, from 3:08.5.

WHAT WORKS (why this sits near 9):
- The cold open is the finished town and a meter, with "? demanded" parked at 76 %. That marker is the viewer's naive guess drawn on the scale, and it slides to ⅓ on the reveal (0:09 → 0:12.3).
- The naive plan has a number: "plan predicts 0" against a live counter of 74 (0:58–1:03). Dimming the 67 never-movers (1:05–1:09, kf_10) is the clearest failure picture in the series.
- The domino replay uses the real tiles and the real moves. The fractions are built from the inset tiles and their states hold long enough to read (1:13–1:41, kf_14 and kf_18).
- The dot chart's x-axis morphs into the ladder's baseline (2:03–2:07, f_2-04.6), and the caret slide crosses exactly two bars (2:30–2:33). Motion carries the argument here.
- Deictic sync is clean: "these 238" counts up on the word (0:40–0:41), "this neighbor moved away" flies A out (1:21–1:23), "Its neighbor here" moves the box to C (1:33–1:35), "Only these two bars" (2:30) and "This one" boxes the right town (3:09).

FIXES (highest impact first):
1. [2:16–2:39][Clarity] The ladder never shows why the cascade fizzles at ¼. The 125 households at 3/8 that lose a match land on 2/7, which is content at ¼. Instead, the "lose one match" arrow fades out during the caret slide (2:29 → 2:33). The viewer gets only "238 → 95, that chain never starts", which covers the initial count, not the cascade. Exact change: keep the arrow through the slide. When the 2/7 bar turns grey, flash the arrowhead's target bar and swap the arrow label to "still content". Add 8 words to the last ladder line: "…and they're tall. A household at three eighths that loses a match is still content. Just ninety-five start unhappy…". Also replace the vague pronoun at 2:21 with "…is one lost match away from two sevenths." Pay for the words by merging 0:43–0:52 into "The obvious plan: move each one to a random empty square where it would be content, so the town stays mixed." (saves about 5 words).
2. [3:24.0–3:32.4][Audio] The landing line, the most important sentence, runs at 215 wpm. It comes straight after a 14.7 s run with no breath (3:08.5 onward). Exact change: put [pause 0.7] after "…through reduced credit." and [pause 0.5] after "Look again at the first town." Synthesize "As Schelling argued, whatever you guessed its people demanded, the map alone could not have told you." at speed 0.76 with [pause 0.3] after "demanded,". Slow 1:48.4 "That whole town is one point on this chart" the same way, with [pause 0.4] before it.
3. [3:32.4–3:33.8][Visual/Motion] The "Ω Sample Space / Episode 75" ident fades in while the landing board and meter are still at about 80 % (f_3-32.9). For half a second the title text sits over the tiles and the meter's "0%". The restored opening frame also gets only about 0.5 s after the last word before the dissolve. Exact change: hold the restored opening frame 1.2 s after "told you", fade it to 0 over 0.5 s, then fade the ident in on an empty background (sequential, not cross). Trailing silence stays ≤ 2 s if the ident hold drops to about 0.8 s.
4. [0:40–0:58][Visual] The RED "unhappy" rings on gold tiles read as orange and blend into the gold (kf_08, 0:44.3), so the 238 do not pop out as a set the way they do on blue tiles. Exact change: while the rings draw, dim content tiles to 55 % (the same move used at 1:05, but milder), and raise ring stroke from about 3 px to 5 px. Undim on "Round one".
5. [1:42.5–1:45.0][Motion] Rounds 2–7 run at about 0.4 s each. In the 2 fps strip the HUD shows "round 2 · moves 0", then "round 3 · unhappy 41 · moves 0", then "round 3 · 24 · 28". Round 2's 72 moves never settle on screen, so the moves row flickers stale values. Exact change: give each round ≥ 0.6 s with an ease-in-out on the meter, and let each round's final moves count land before the round number advances. Or hide the moves row for the fast run and keep only round, unhappy and meter. Stretch the [pause 1.4] to 2.4 s (paid for by the cut in fix 1).
6. [2:05–2:17][Visual] For about 12 s the ladder fills the left 64 % of the frame and the right third is empty (kf_23, 2:11.3). The bars also have no scale: only a y-title, with counts added later. Exact change: build the ladder centred (x-shift +1.6 units). When A's 3×3 enters at 2:17, slide the whole ladder left in 0.8 s, so the move reads as making room for the example.
7. [2:27–2:31][Visual] The prediction hold has about 14 labels in three competing clusters: counts plus the arrow, the two carets with fractions, and A's patch with 2/7 < 1/3 (f_2-28.8). Exact change: during the 1.5 s hold, dim A's patch, its formula and "lose one match" to 30 %, so the dashed ¼ outline with 76 and 67 is the one focal point. Restore them on "Only these two bars".
8. [1:51–2:03][Visual] The 30-town clouds render as grey smudges (38 % opacity, ±0.6 pp jitter, kf_22). The small PURPLE ¼ and ⅓ column marks sit just above the axis beside the "random mix" label and read as stray glyphs. Exact change: raise dot opacity to 60 % and reduce jitter to ±0.3 pp. Move the ¼ and ⅓ column marks below the x-axis tick row, or drop them, since the thumbnail labels already name the columns.
9. [0:22–0:27][Hook] The stakes sentence "We read real city maps the same way, guessing motives from patterns" plays over an unchanged frame (sheet 2, 0:23–0:27). It is the only abstract line in the first 30 s. Exact change: on "real city maps", dim the 3×3 inset and HUD to 30 % and pulse the board's frame once, so the sentence points at the town as a map. Keep the line.
10. [1:11.9][Audio] Whisper hears "Replay 1 corners": the singular is slurred into the next word. Exact change: re-synthesize as "Replay one corner." followed by [pause 0.3].

REACHES 9 IF ALL FIXED: yes. The structure is right: misconception-led cold open, a measured failure (74 against 0), a real-tile domino, the ladder as the single picture, an honest Schelling comparison, and a landing that restores the first frame. What separates this from 9 is execution: one missing causal link in the ladder (fix 1), a rushed landing line (fix 2), the ident dissolve (fix 3) and four focus and legibility issues (fixes 4–7). Fixes 1–5 would put Clarity, Audio, Visual and Motion at 9 and the weighted score at about 9.0.

KEEP:
- The "plan predicts 0" HUD against the live 74, and the dim-all-but-the-67 frame (0:58–1:09).
- The corner replay with the real moves and fractions built from tiles (1:13–1:41), and the axis-into-baseline morph (2:03–2:07).
- The two-town test with no visual tell, ending on the exact cold-open frame (2:54–3:32).
