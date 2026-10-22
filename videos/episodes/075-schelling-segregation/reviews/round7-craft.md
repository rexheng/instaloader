# Round 7 — craft review (visual design, motion, audio/visual sync)

Evidence: I used the `review/` pack as is, because metrics.json (21:56) is newer than final.mp4 (21:55). I read report.md, all 12 contact sheets, and 18 full-resolution keyframes (kf_01, 04, 08, 10, 14, 17, 19, 21, 23, 25, 26, 28, 30, 31, 33, 34, 37, 39, 40). I also read four 3 fps motion strips covering 1:10–1:14, 1:37.5–1:44.5, 1:43.5–1:49.5, 1:58–2:02, 2:51.5–2:54.5 and 3:21.5–3:25.5, and single frames at 2:52.0 and 3:23.4. I read transcript.txt, transcript_words.tsv, the narration.json beats and word timings, script.md, sim_output.txt and the round-6 reviews. Both citations were re-checked by web search.

```
EPISODE: 075 — "Mild Preferences, Segregated Towns"
IDEA: In Schelling's model, households that demand only a third of their neighbors match still sort into a town where three quarters match, because each departure drops a content 3/8 neighbor to 2/7 and tips it; so a segregated map cannot tell you what its people wanted.
SCORES: Hook 9 · Clarity 9 · Visual 8.5 · Motion 9 · Audio 9 · Concision 9 · Originality 9
WEIGHTED: 8.9 (892.5/100 = 8.925)   AFTER CEILING: 8.9 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none (runtime 3:34.5; 152 wpm; max silence 2.08 s at 0:09.1, a planned prediction hold; max static 3.8 s at 2:54.2; −14.0 LUFS / −1.9 dBTP; 0 banned phrases; both empirical claims cited on screen for ≥ 3 s; no overlap, clipping, typo or broken LaTeX in any keyframe; layout audit 0/229)
FINAL: 8.9   PASS: no
```

## FACTS
| Claim | Verdict | Source |
|---|---|---|
| Finished town: three quarters of neighbors match, meter 76 % (0:00–0:06) | Verified | sim_output: share 0.7553 |
| Demand ⅓, empty squares not counted, "happy to be outnumbered two to one"; boxed "2 of 6 match" (0:12–0:22) | Verified | s/(s+d) ≥ ⅓ ⇔ d ≤ 2s. kf_04 shows 2 gold, 4 blue and 2 × marks |
| Random start: half match (0:36) | Verified | 0.4992 |
| 238 unhappy at the start (0:40) | Verified | ladder rungs below ⅓: 23+15+23+11+23+76+67 = 238 |
| Round 1: 200 moves; the other 38 content by their turn (0:51–0:57) | Verified | round-1 breakdown {moved 200, content_before_turn 38} |
| Counter reads 74 against "plan predicts 0"; 67 of them content before round 1 (1:00–1:08) | Verified | unhappy by state [238, 74, …]; "never unhappy at start: 67"; 74 − 67 = 7, shown as grey rings in kf_10 |
| B: 3/8 ≥ ⅓, then 2/7 < ⅓ after A leaves; C: 3/8, then 2/7 after round 2 (1:11–1:38) | Verified | chain rows r0–r2; the inset tiles in kf_14 and kf_17 match (2 gold of 7, vacated square empty) |
| After round 7 nobody wants to move; moves 341 (1:41–1:44) | Verified | moves 200+72+41+16+9+2+1 = 341; unhappy 0 (kf_19) |
| Same start at ¼ → 58 %, at ⅓ → 76 % (1:49–1:58) | Verified | 0.5787 / 0.7553; the 30-town means 0.584 / 0.749 match the clouds in kf_21 |
| Ladder: rung positions and heights; at ¼ only the ¼ (76) and 2/7 (67) bars flip; 95 start unhappy (2:00–2:31) | Verified | I measured the bar x-positions in kf_23: 0 → 422 px, ⅛ → 641, ¼ → 861, 2/7 → 923, ⅓ → 1007 (1755 px per unit, linear). Height ratio 76/67 = 128/113 px. 238 − 143 = 95 |
| At ¼, a 3/8 household that loses a match (2/7 ≥ ¼) stays, "so that chain never starts" (2:31–2:37) | Verified | "demand 1/4: chain households that ever move: []" |
| Schelling 1971, J. Math. Sociology: nearest suitable vacancy, emptier boards, jump "from about 35 % to 50 %" (2:37–2:52) | Verified | the paper PDF (uvm.edu and uzh.ch copies): "a rapidly rising function of demands in the range from about 35% to 50%" |
| Aaronson, Hartley & Mazumder 2021, AEJ: Economic Policy: the 1930s HOLC maps increased racial segregation in later decades, through reduced credit (3:13–3:23) | Verified | aeaweb.org abstract, doi 10.1257/pol.20190414: "increased racial segregation in later decades … through reduced credit access" |
| Rule-placed town also 76 % (2:52–3:10) | Verified | zoned town share 0.7553 |
| "As Schelling argued … the map alone could not have told you" (3:26) | Verified (paraphrase) | 1971 abstract: inferences about individual motives "can usually not be drawn from aggregate patterns" |

No factual or mathematical error found.

## MECHANICS
runtime 3:34.5 · wpm 152 (speech; 138 overall) · max silence 2.08 s (0:09.1 and 3:03.8, both prediction holds) · max static 3.8 s (2:54.2–2:58.0) · −14.0 LUFS / −1.9 dBTP · leading 0.00 s, trailing 1.77 s · WER 0.2 % (the only miss is "block's" heard as "blocks", a homophone) · 0 banned phrases · 0 glyph morphs · 14 of 14 deictics landed.

## What the evidence shows (craft lens)
- **Cold open and hook (0:00–0:32).** Frame 1 is the finished town with the 76 % meter, plus a "simulated" tag (kf_01). "? demanded" appears on "these households" and holds through a 2.1 s silence, which is a real prediction prompt by 0:09. The marker then slides from 76 % to ⅓ on "Just a third". It is one object that changes meaning, the best possible reveal. On "real city maps" (0:23–0:27) the inset and meter dim and the board's frame pulses, so the stakes line now points at something.
- **Naive build and fail (0:33–1:10).** The rewind flies tiles home while the meter falls 76 → 73 → 56 → 50 (sheet 2). That is a transform, not a cut. The RED rings draw as "unhappy" counts up (104 at 0:41.0, 238 at 0:43), and the content tiles dim, so the 238 read as a set (kf_08). The red/gold confusion from round 6 is gone. The dashed arc previews a real move, "plan predicts 0" sits directly under the count, and the counter stops at 74. The dim-all-but-the-67 frame (kf_10) is the clearest failure picture in the series.
- **Domino (1:10–1:38).** The board parks left at 0.7 scale and the inset flies out of the boxed block (strip 1:10–1:14). The real tiles replay in step, and each fraction is built from the tiles with a "?" while its state is pending (kf_14, kf_17). The relation flips from ≥ to < only after the digits change. The state captions swap one after the other.
- **Cascade (1:37.5–1:44).** At 3 fps every round's counts settle before the round number advances (70 % → 76 %, unhappy 44 → 41 → 29 → 16 → 11 → 9 → 5 → 2 → 1 → 0). "After round seven" (1:41.1–1:42.8 by word timing) lands as the HUD reads round 7 and unhappy 0 (about 1:42.2).
- **Generalise (1:44–2:00).** A copy of the town shrinks into the ⅓ dot on "point" (strip 1:43.5–1:49.5). The clouds fade in only after it lands, and the ¼ town's dot arrives the same way. The x-axis rises into the ladder baseline and the bars sprout left to right on "sort … neighbors" (strip 1:58–2:02). Motion carries the argument here.
- **Ladder (2:00–2:37).** It is built centred and slides left when A's patch enters (kf_23 → kf_25). During the prediction the patch dims and the dashed ¼ outline is the focus (kf_26). The caret slides across exactly two bars, then "lose one match / still content" appears and A's formula flips to 2/7 ≥ ¼ (kf_28). The mechanism is now on screen, not just stated.
- **Honest limit (2:37–2:52).** The bracket slides from "our jump" to "Schelling: 35–50%", the hatch sweeps and our dots dim (kf_30, kf_31), so the citation is attached to its picture.
- **Test and landing (2:52–3:34).** The test is blind: ours is turned a quarter turn (kf_33), the labels wait unassigned in the gap, and the reveal moves them around the boards, never over them. In the landing everything else fades, ours turns back while it grows into the opening position (3:22.3–3:24.5, frame 3:23.4), and "? demanded" returns on the exact first frame (kf_39). The ending re-sees the cold open, and the rotation is the one place where a spin carries meaning: it undoes the disguise.

## Remaining defects (cited)
1. **Word load over the §5 limit (2:34.5–2:37.3, kf_28).** The frame carries 13 prose words: "households (simulated start)" (3), "lose one match" (3), "still content" (2), "unhappy" (1) and "share of neighbors matching" (4). The limit is 12. "(simulated start)" also repeats a tag the viewer has seen since 0:00, so it is removable.
2. **The chart-to-test transition dips through an empty frame while the narration starts (2:51.6–2:53.0).** In the frame at 2:52.0 both test boards are at about 5 % opacity on an otherwise empty background. "Two simulated towns" starts at 2:52.0, so the noun is spoken over a nearly blank frame for about 0.5 s, and they reach full strength only at about 2:52.8. A cut is the right choice here, because the blind test forbids carrying our thumbnail across. The timing is the problem.
3. **The ladder has no vertical scale (2:00–2:37).** "households (simulated start)" is a title without an axis. Heights become quantities only for the 3–4 rungs that carry counts (67, 76, 125). The tallest bar (½, 256 households) is never labelled, so the eye has no anchor for the right half.
4. **The "our jump" bracket floats (2:42–2:47, sheet 10).** It sits at the 95 % row, about 1.5 units above the two dots it is meant to join (58 % and 76 %), so it reads as a range on the x-axis rather than "these two dots". This is a nitpick, because the slide to 35–50 % reads well either way.
5. **Audio nitpick (2:41.6–2:52.0).** "His households moved to the nearest suitable square, on emptier boards, and there the jump came later, between about a third and a half." That is 26 words with no Kokoro gap longer than 0.31 s (narration.json), while the screen does three sequential things: "our jump" fades out, the bracket slides, the band sweeps. It is the episode's densest qualification, delivered in one breath.

## FIXES (highest impact first)
1. [2:00–2:37][Visual] 13 prose words on screen at 2:34.5 (kf_28). Change the ladder's y-title from "households (simulated start)" to "households", which brings it to 11 words. The board has carried "simulated" since frame 1, and the ladder is introduced as "the random start" in narration. Optionally merge the arrow label into one line, "lose one: still content". This restores the §5 word load and, on its own, moves Visual to 9 and the weighted score to 9.0.
2. [2:51.6–2:53.0][Visual/Sync] The test boards are at about 5 % at 2:52.0, when "Two simulated towns" starts. Keep the sequential cut (it protects the blind test), but start the boards' fade-in 0.4 s earlier, or delay the line by 0.4 s with [pause 0.4] before "Two". Then both boards are at ≥ 70 % when "Two" is spoken, and the near-empty frame lasts ≤ 0.3 s.
3. [2:00–2:37][Visual] The ladder heights have no scale. Add a GRAY count "256" (MathTex 32) above the ½ bar when the bars finish sprouting at 2:04, the same style as 67/125. Or draw a thin GRAY y-axis at the baseline's left end with one tick, "100". One anchor is enough; do not add more ticks.
4. [2:41.6–2:52.0][Audio] The honest-limit sentence runs in one breath. Insert [pause 0.4] after "on emptier boards," and synthesize that sentence at speed 0.80. Retime the "our jump" fade-out and bracket slide into that pause, so the band sweep alone rides "between about a third and a half". This adds about 0.8 s, for a runtime of about 3:35.3, still inside the 3:15–3:35 budget band if the next fix is applied.
5. [2:52.0–2:56.1][Concision] "Two simulated towns, both seventy-six percent" reads out the two "76% match" labels. Say "Two simulated towns." and pulse both "76% match" labels in silence for 0.6 s. That saves 3 words and about 0.9 s, which pays for fix 4.
6. [2:42–2:47][Visual] Move the "our jump" bracket down to just above the ⅓ cloud (y ≈ 80 % on the chart), with its ends over the ¼ and ⅓ columns. Or keep it where it is and drop two thin dotted GRAY lines from its ends to the ¼ and ⅓ dots, so it visibly joins our two towns. Slide it back to the top row when it becomes "Schelling: 35–50%".

REACHES 9 IF ALL FIXED: yes. Fix 1 alone reaches 9.0 (Visual 8.5 → 9, weighted 900/100). Fixes 2–4 move Visual, Motion and Audio from a borderline 9 to a secure one. The structure is right: a misconception cold open with a held prediction, a measured failure (74 against 0), a real-tile domino, the ladder as the single picture with its mechanism on screen, an honest Schelling comparison, a blind two-town test, and a landing on the exact first frame. Only execution nitpicks remain.

KEEP:
- The "? demanded" marker sliding from 76 % to ⅓ on "Just a third" (0:09–0:12), and its return to "?" on the restored first frame (3:26–3:33).
- The "plan predicts 0" HUD against the live 74, plus the dim-all-but-the-67 frame (0:57–1:09), and the real-tile domino with fractions built from tiles (1:11–1:38).
- The town-to-dot flight and the x-axis-to-baseline morph (1:45–2:02), the caret crossing exactly two bars to "still content / 2/7 ≥ ¼" (2:25–2:37), and the blind two-town test (2:52–3:10).
