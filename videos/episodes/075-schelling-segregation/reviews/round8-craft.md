# Round 8 — craft review (visual design, motion, audio/visual sync)

Evidence: the `review/` pack, used as is because metrics.json (23:58) is newer than final.mp4 (23:56). I read report.md, all 12 contact sheets and 16 full-resolution keyframes (kf_02, 04, 09, 11, 16, 18, 21, 26, 28, 30, 31, 33, 35, 38, plus kf_01 and kf_39 via the sheets). I also pulled extra frames with ffmpeg at 0:01.0–0:03.2, 1:39.6–1:41.4, 1:55.4–1:56.9, 2:44.6–2:46.2 (two passes, 0.2–0.4 s apart), 2:50.6–2:51.8, 3:19.0–3:20.8 and 3:28.5–3:30.8. I read transcript.txt, transcript_words.tsv, narration_diff.txt, script.md, facts.md, sim_output.txt and the round-7 craft review, which I used only to check whether its defects are still visible. I re-checked both citations by web search: the Schelling 1971 PDF (uzh.ch and uvm.edu copies) and the aeaweb.org abstract for Aaronson, Hartley & Mazumder.

```
EPISODE: 075 — "Mild Preferences, Segregated Towns"
IDEA: In Schelling's model, households that demand only a third of their neighbors match still sort into a town where three quarters match, because each departure drops a content 3/8 neighbor to 2/7 and tips it in turn; so a segregated map cannot tell you what its people wanted.
SCORES: Hook 9 · Clarity 9 · Visual 8.5 · Motion 9 · Audio 9 · Concision 9 · Originality 9
WEIGHTED: 8.9 (892.5/100 = 8.925)   AFTER CEILING: 8.9 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none (runtime 3:30.9; 153 wpm; max silence 2.09 s at 0:09.1 and 3:00.1, both planned prediction holds; max static 3.63 s at 0:03.9; −14.0 LUFS / −1.9 dBTP; 0 banned phrases; both empirical claims cited on screen ≥ 3 s; no settled-frame overlap, clipping, typo or broken LaTeX; layout audit 0 issues in 232 frames)
FINAL: 8.9   PASS: no
```

## FACTS
| Claim | Verdict | Source |
|---|---|---|
| Finished town: three quarters of neighbors match, meter 76 % (0:00–0:06) | Verified | sim_output: share 0.7553 |
| Demand ⅓, empties not counted, "happy to be outnumbered two to one"; boxed "2 of 6 match" (0:12–0:22, kf_04) | Verified | s/(s+d) ≥ ⅓ ⇔ d ≤ 2s; kf_04 shows 2 gold, 4 blue, 2 × marks |
| Random start: half match (0:36) | Verified | 0.4992 → 50 % |
| 238 unhappy at the start (0:40–0:43) | Verified | ladder rungs below ⅓: 23+15+23+11+23+76+67 = 238 |
| Round 1: 200 moves; "38 content by their turn" (0:52–0:58) | Verified | round-1 breakdown {moved 200, content_before_turn 38, no_destination 0} |
| Unhappy stalls at 74 against "plan predicts 0"; 67 of them content before round 1 (0:54–1:03) | Verified | unhappy by state [238, 74, …]; "never unhappy at start: 67" |
| B: 3/8 ≥ ⅓, then 2/7 < ⅓ after A leaves; C: 3/8, then 2/7 after round 2 (1:06–1:33) | Verified | chain rows r0–r2; the inset tiles in kf_16 and kf_18 match (2 gold of 7, the vacated square dark) |
| After round 7 nobody wants to move; moves 341 (1:36–1:39) | Verified | 200+72+41+16+9+2+1 = 341; unhappy by state ends at 0 |
| Same start at ¼ → 58 %, at ⅓ → 76 % (1:44–1:53) | Verified | 0.5787 / 0.7553; 30-town means 0.584 / 0.749 match the swarms in kf_21 |
| Ladder: bar positions linear in share; at ¼ only the ¼ (76) and 2/7 (67) bars flip; 95 start unhappy (1:57–2:26) | Verified | in kf_26, 0 % at x 138, 60 % at x 1190; ¼ bar at 578 → 0.251, ½ bar at 1016 → 0.500. 238 − 76 − 67 = 95 = 23+15+23+11+23 |
| At ¼ a 3/8 household that loses a match stays (2/7 ≥ ¼), "so that chain never starts" (2:26–2:33) | Verified | "demand 1/4: chain households that ever move: []" |
| Schelling 1971, J. Math. Sociology: nearest move, 25–30 % empty, jump "from about 35 % to 50 %" (2:33–2:49) | Verified | Schelling 1971 PDF: "a rapidly rising function of demands in the range from about 35% to 50%" |
| Aaronson, Hartley & Mazumder 2021, AEJ: Economic Policy: 1930s HOLC maps raised racial segregation for decades; the authors point to reduced credit (3:06–3:19) | Verified | aeaweb.org abstract, doi 10.1257/pol.20190414: "increased racial segregation in later decades … These results suggest … through reduced credit access" |
| The rule-placed town also matches 76 % (2:51–3:19) | Verified | zoned town share 0.7553 |
| "As Schelling argued … the map alone could not have told you" (3:22–3:29) | Verified (paraphrase) | 1971 abstract: inferences about individual motives "can usually not be drawn from aggregate patterns" |

No factual or mathematical error found.

## MECHANICS
runtime 3:30.9 · wpm 153 (speech; 137 overall) · max silence 2.09 s · max static 3.63 s · −14.0 LUFS / −1.9 dBTP · leading 0.00 s, trailing 1.77 s · WER 0.2 % (the only difference is "block's" heard as "blocks", a homophone) · 0 banned phrases · 0 glyph morphs · 13 of 13 deictics land within −0.8…+0.4 s.

## What the evidence shows (craft lens)
- **Round-7 defects are fixed.** The ladder's y title is now "households" (kf_26, kf_28), so the frame is under 12 prose words. The ½ bar carries "256" as a height anchor. Both test boards are at full strength by 2:50.6, before "Two simulated towns" at 2:49.7–2:51.5 (frame grid 2:50.6–2:51.8). The Schelling sentence is three sentences with breaths (silences 2:37.6, 2:41.7, 2:44.0). "Our jump" has a dotted drop to the ¼ column (kf_30).
- **Cold open (0:00–0:12).** Frame 1 is the finished town tagged "simulated". The meter bar is drawn at 76 % by 0:01 and the number is written by 0:02.0 (frame grid), so the figure is on screen before "three quarters" is spoken. "? demanded" lands on "these households" and holds through 2.1 s of silence (kf_02). The same marker slides to ⅓ on "Just a third": one object changes meaning.
- **Failure (0:33–1:05).** Tiles fly home and the meter falls 76 → 73 → 56 → 50 (sheet 2), a transform rather than a cut. RED rings draw while the count runs (104 at 0:41, 238 at 0:43, kf_09), and the content tiles dim so the 238 read as a set. In kf_11 "plan predicts 0" sits directly under "unhappy 74", while "round"/"moves" dim to about 35 % and the 7 grey rings separate from the 67 red ones. The failure is measured, and it is the focal point.
- **Domino (1:05–1:33).** The real tiles replay inside a 4×5 inset that flies out of the boxed block. Each fraction is built from tile copies (1:09: gold squares in flight toward the 3) and shows "?" while its state is pending (1:17, 1:21), and the relation flips only after the digits change (kf_16, kf_18).
- **Generalise and ladder (1:33–2:33).** The town shrinks into the thumbnail while the axes build (1:39.6–1:41.4), and a copy lands as the ⅓ dot. The dot chart's x-axis rises into the ladder baseline and the bars sprout left to right (1:55.4–1:56.9). The caret crosses exactly two bars, the count falls to 95, and A's formula flips to 2/7 ≥ ¼ with "lose one match / still content" (kf_28). The episode's one picture explains the jump, not just the starting count.
- **Test and landing (2:51–3:31).** The blind test (kf_33) assigns labels by travelling through the gap, the rule town's zone lines draw on (kf_35), both towns dim under the study (kf_38), and ours un-turns its quarter turn while it grows back into the opening position (3:19.6–3:20.8). The last frame is the first frame with "? demanded" (3:28.5–3:30.3). This rotation is the one spin that carries meaning: it undoes the disguise.

## Remaining defects (cited)
1. **Two focal points in the honest-limit beat (2:37–2:50, kf_30, kf_31).** The two town thumbnails and their "⅓ → 76%" / "¼ → 58%" labels stay at full saturation for the whole Schelling beat. At 2:48.7 (kf_31), our swarms dim to 30 % so the hatched 35–50 % band reads as his result. The brightest, most saturated objects in that frame are the two thumbnails at the right edge, though nothing in the narration refers to them after 1:53. The eye goes to the thumbnails, not the band.
2. **Orphaned bracket (2:41.7–2:45.8, kf_30).** The "our jump" tag fades on "nearest", but the bracket and its dotted drop stay on screen, unlabelled, for about 4 s. The tag lived about 2 s (2:39–2:41). When the bracket slides to 35–50 %, the viewer has to remember what it was, so the slide (our jump → his jump) loses half its meaning.
3. **The bracket skews during its slide and passes the rules labels (2:44.9–2:45.1).** In the frames at 2:44.9 and 2:45.1 the bracket's bar is visibly tilted, with the left tick lower than the right. That is the interpolation between two brackets of different geometry. Its left end passes within a few pixels of "25–30% empty", which only steps down a row afterwards (2:45.8). It lasts about 0.3 s, so this is a nitpick, but it is the one untidy move in the episode.
4. **The ladder is silently truncated (1:57–2:33, kf_26, kf_28).** The baseline ends at "60%". The bars shown sum to 1,019 households, so the 421 households above 60 % (5/8: 136, 3/4: 58, …) are not drawn, under a title that just says "households". The cut is harmless to the argument, but a careful viewer reads the right end as the end of the distribution.
5. **"76 67" crowding (2:17–2:33, kf_26, kf_28).** The two counts sit side by side about 20 px apart, at the §5 limit, and read as one string, "76 67". Nitpick.

## FIXES (highest impact first)
1. [2:37–2:50][Visual] The thumbnails compete with the Schelling band. On "His households" (2:38.2), dim both thumbnails and their "⅓ → 76%" / "¼ → 58%" labels to 35 %, using the same colour-not-opacity dim as the swarms. They leave with the chart at 2:50 anyway. The one focal point is then the bracket, and from 2:46.6 the band. This plus fix 2 moves Visual to 9.
2. [2:39–2:45.8][Visual/Motion] The bracket is unlabelled for 4 s. Shorten the tag from "our jump" to "ours" (1 word, which keeps the frame at 12 prose words with "nearest move", "25–30% empty", the axis titles and the 5-word citation), keep it on through "nearest … emptier", and fade it only as the bracket starts sliding on "There" (2:44.6), in the same move that brings in "Schelling: 35–50%". The slide then reads "ours → his".
3. [2:44.6–2:45.8][Motion] The bracket skews mid-slide and grazes "25–30% empty". Step the two rules labels down a row before the slide (move the 2:45.8 shift to 2:44.6), and build both brackets with the same function and identical tick heights. Then animate with `bracket.animate.move_to(...).stretch_to_fit_width(...)` instead of a Transform between differently shaped brackets, so the bar stays level.
4. [1:57–2:33][Clarity/Visual] Make the truncation visible: put a GRAY note "+421 above 60%" (Text 18) just right of the "60%" tick, or end the baseline with a short arrow, so the 1,019 bars shown are not read as all 1,440.
5. [2:17–2:33][Visual] Separate "76" from "67". Lift "76" so its baseline clears the top of the dashed ¼ outline by 0.15, leaving the two counts on different rows. Or keep one row and set ≥ 0.3 units between them.
6. [1:27.2–1:30.0][Sync] "our household leaves" refers to B after the subject outline has moved to C (1:24.5). On "our household", pulse B's red ring once (0.5 s) before B flies out, so the pronoun has a visible referent.

REACHES 9 IF ALL FIXED: yes. Fixes 1 and 2 alone lift Visual from 8.5 to 9, and the weighted score from 8.925 to 9.0 (900/100). The structure needs no change: a misconception cold open with a held prediction, a measured failure (74 against "plan predicts 0"), a real-tile domino with fractions built from tiles, the share ladder as the single picture with its mechanism on screen, an honest comparison with Schelling, a blind two-town test, and a landing on the exact first frame. What remains is hierarchy and transition polish in one 13-second beat.

KEEP:
- The "? demanded" marker: it slides from 76 % to ⅓ on "Just a third" (0:09–0:12) and returns to "?" on the restored first frame (3:22–3:31), after the un-turn that reveals the test town was ours.
- The "plan predicts 0" row against the live 74, with the dim-all-but-the-67 frame (0:54–1:05), and the real-tile domino with fractions built from tile copies (1:06–1:33).
- The town-to-dot flight and the x-axis-to-baseline morph (1:39–1:57), plus the caret crossing exactly two bars to "still content / 2/7 ≥ ¼" (2:17–2:33).
