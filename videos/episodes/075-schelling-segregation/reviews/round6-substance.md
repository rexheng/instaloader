# Round 6 — substance review (science + story editor)

Evidence: `review/` pack (metrics.json 19:57 is newer than final.mp4 19:55, so it was used as is). I read report.md, all 12 contact sheets and 12 full-resolution keyframes (kf_01, 04, 08, 10, 14, 19, 21, 26, 27, 30, 33, 35, 40), plus transcript.txt, transcript_words.tsv, narration.json word timings, script.md, facts.md and sim_output.txt. I recomputed the numbers from sim_output.txt by hand and checked both citations by web search.

```
EPISODE: 075 — "Mild Preferences, Segregated Towns"
IDEA: In Schelling's model, households that demand only a third of their neighbors match still sort into a town where three quarters match, because each departure tips a neighbor who was content; so a segregated map cannot tell you what its people wanted.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8.5 · Motion 9 · Audio 8 · Concision 8.5 · Originality 8.5
WEIGHTED: 8.5 (852.5/100 = 8.53)   AFTER CEILING: 8.5 (lowest 8 + 2 = 10, so the ceiling does not bind)
CAPS: none (runtime 3:33.8 ok; 153 wpm ok; max silence 2.08 s; max static 3.8 s; −14.0 LUFS / −1.8 dBTP; 0 banned phrases; both empirical claims cited on screen ≥ 3 s; no overlap, clipping or typo in the keyframes)
FINAL: 8.5   PASS: no
```

## FACTS
| Claim | Verdict | Source / recomputation |
|---|---|---|
| Final town: on average ¾ of neighbors match, meter 76 % (0:00–0:06) | Verified | sim 0.7553. Narration says "three quarters", the screen rounds to 76 %. |
| ⅓ demand means "happy to be outnumbered two to one"; boxed example "2 of 6 match" (0:16–0:22) | Verified | s/(s+d) ≥ ⅓ ⇔ d ≤ 2s. kf_04 shows 2 gold, 4 blue and 2 × empties, so 2/6 = ⅓ is content at exactly the threshold. |
| Random start: half the neighbors match (0:35) | Verified | 0.4992 |
| 238 unhappy at start (0:40) | Verified | sum of the ladder bars below ⅓: 23+15+23+11+23+76+67 = 238 |
| Round 1: 200 moves, the other 38 content by their turn (0:53–0:58) | Verified | round-1 breakdown 200 / 38 / 0 |
| Counter reads 74 vs "plan predicts 0" (1:02) | Verified | unhappy after r1 = 74 |
| 67 of the 74 were content before round 1 and never moved (1:05–1:09) | Verified | "never unhappy at start: 67"; only households unhappy at the start of a round move |
| B: 3/8 ≥ ⅓, then 2/7 < ⅓ after A leaves (1:13–1:32) | Verified | chain r0 B (2,3,8), r1 B (2,2,7); 0.375 > 0.333 > 0.286. Inset tiles checked in kf_14 (2 gold of 7 occupied) |
| C: 3/8 after r1, 2/7 after r2 when B leaves (1:33–1:40) | Verified | chain r1 C (2,3,8), r2 C (2,2,7) |
| "After round seven, nobody wants to move" (1:44) | Verified | moves 200,72,41,16,9,2,1; unhappy after r7 = 0 (kf_19 HUD: round 7, moves 1, unhappy 0) |
| Same start at ¼ → 58 %; at ⅓ → 76 % (1:52–1:59) | Verified | 0.5787 and 0.7553; the 30-town means are 0.584 and 0.749 (dot clouds in kf_21 match) |
| Ladder: the shares k/n ≤ 0.6 with n ≤ 8; bar heights | Verified | I checked the 14 positions against the 0–60 % baseline in kf_26 (2/7 at x≈640, 3/8 at x≈797, ½ at x≈1015 px); the heights match the counts 67, 125, 256 |
| At ¼ only the 2/7 (67) and ¼ (76) bars change sides; 95 start unhappy (2:30–2:36) | Verified | 238 − 67 − 76 = 95; a share equal to the demand is content |
| "That chain never starts" at ¼ | Verified | "demand 1/4: chain households that ever move: []" |
| Schelling 1971 ran this model; his households moved to the nearest suitable square on emptier boards; his jump came between about ⅓ and ½ (2:39–2:54) | Verified | Schelling, *J. Math. Sociology* 1(2):143–186 (1971). The paper text (via search excerpts of the PDF) has "moves to the nearest vacant spot…", "25% to 30% vacancies allows fair freedom…", "rapidly rising function of demands in the range from about 35% to 50%" and "slight when the demand is for about one-third". The on-screen citation is correct. |
| Rule-placed town also at 76 % (2:54–3:13) | Verified | zoned town 0.7553, every household in its own colour's zone, nobody moves |
| 1930s federal lending maps increased racial segregation for decades, through reduced credit (3:13–3:24) | Verified | Aaronson, Hartley & Mazumder 2021, *AEJ: Economic Policy* 13(4):355–92, doi 10.1257/pol.20190414. Abstract (aeaweb.org): "increased racial segregation in later decades … through reduced credit access and subsequent disinvestment". The on-screen citation is correct, and "one study" is a fair hedge. |
| "As Schelling argued … the map alone could not have told you" (3:26) | Verified (paraphrase) | 1971 abstract: inferences about individual motives "can usually not be drawn from aggregate patterns" |

No factual or mathematical error found. No claim is unverifiable.

## MECHANICS
runtime 3:33.8 · wpm 153 (speech time; 139 overall) · max silence 2.08 s (0:09.1, the planned prediction hold) · max static 3.8 s (2:56.4) · −14.0 LUFS / −1.8 dBTP · leading 0.00 s / trailing 1.65 s · WER 0.4 % ("corner" heard as "corners" twice) · 0 banned phrases. Only 4 questions in the whole episode and never two in a row. One signpost ("To see why that happens", 2:02), which the rules allow once.

## What the evidence shows, beat by beat
- **0:00–0:32 hook.** It is strong. The finished town and a 76 % meter are on screen in frame 1 (kf_01), the "? demanded" marker pulses, and the 2 s hold leads to the reveal "Just a third". Then the "2 of 6" box turns the rule into a picture (kf_04). The stakes line ("We read real city maps the same way") is the episode's thesis in one sentence.
- **0:33–1:11 naive build and fail.** This is textbook Stuff Made Here. The rewind flies every tile home (0:33 sheet) and the meter drops from 76 to 50. The "plan predicts 0" row sits directly above the live count of 74 (kf_10). The 67 "never moved" households stay lit while everything else dims, so the cause ("Their neighbors did") is shown, not just asserted.
- **1:11–1:52 domino.** The inset is the best sequence in the film. The real tiles replay in step with the board, and the fraction is built from the tiles, with "?" shown while the state is pending (kf_14). There is one small gap: "corner" is the wrong word. The patch (rows 2–5, cols 11–15 of 40) is not a corner of the board (sheet 5, 1:13).
- **1:48–2:39 generalise and explain.** The town flies in as a dot. Then the x-axis morphs into the ladder baseline (sheet 7, 2:03→2:05), and the caret slides from ⅓ to ¼ while the count falls 238 → 95 (sheet 9). This is where the explanation is thinnest. At ⅓ the narration tells us the 3/8 rung is "one lost match away" from tipping (arrow, 2:25). At ¼ the arrow simply fades (2:31). The mechanism that actually kills the chain is never said: at ¼ a 3/8 household can lose a match and still stay, because 2/7 ≥ ¼. That is exactly why B and C never leave. As it stands, "that chain never starts" reads as following from a smaller starting count alone. The size of the cascade is also never measured: 238 → 341 total moves at ⅓, against 95 → 105 at ¼.
- **2:39–2:54 honest limits.** The episode handles its limit well. "Our jump" (¼–⅓) slides to "Schelling: 35–50%", and our dots dim under the hatch (kf_30), so the viewer is told that the exact location of the tipping point depends on the model.
- **2:54–3:13 the test.** This is the episode's most original idea, but it is not a blind test. The right-hand town is the seed-3 town itself, in the same orientation (compare kf_01 with kf_33). The viewer has watched it for about 90 s of screen time, so "Which one wanted a third?" can be answered by recognising it rather than by reading the map. That undercuts the very point the landing makes.
- **3:13–3:33 payoff and landing.** The HOLC sentence is accurate and cited. The return to the exact opening frame with "? demanded" (sheet 12, 3:29) is an excellent callback. The audio rushes it, though: only 0.30 s separates "Look again at the first town." from "As Schelling argued" (Kokoro timings; in whisper "As" starts at 205.74 s, before "town." ends at 205.76 s), so the last line starts while the frame is still reassembling. The kit puts this sentence at 215 wpm.

## FIXES (highest impact first)
1. **[2:30–2:39][Clarity] The ¼ side of the ladder explains the jump by the starting count only.** During the caret slide to ¼, keep the "lose one match" arrow instead of fading it. Re-draw it from the 3/8 count to the now-grey 2/7 bar and relabel it "lose one match → still content". Narrate this after "just ninety-five start unhappy": "and a household at three eighths can now lose a match and stay, so that chain never starts." That is correct (2/7 ≥ ¼, and B and C never move at ¼), and it turns "never starts" into the mechanism. Optionally add "341 moves" and "105 moves" under the ⅓ and ¼ thumbnail labels at 1:55 to measure the size of the cascade (sim: 200+72+41+16+9+2+1 = 341, and 105).
2. **[2:54–3:08][Clarity/Hook] The two-town test is not blind.** Rotate both towns 90° (or mirror them) in the test beat. The neighbor share and the texture do not change under rotation or reflection, so 76 % holds exactly. Then rotate ours back to the opening orientation as it grows into the landing frame on "Look again at the first town". This makes the visual line "the map alone could not have told you" literally true for the viewer.
3. **[3:23–3:33][Audio] The landing is rushed.** Insert [pause 1.0] after "Look again at the first town." so the reassembled opening frame with "? demanded" is seen in silence. Synthesize the last sentence at speed 0.80 (it is 215 wpm now). Lengthen the gap after "credit." from 0.4 s to [pause 0.7]. That adds about 1.6 s, for a runtime of about 3:35.4.
4. **[1:11.9 and 2:18][Clarity] "Replay one corner" and "our corner's chain" name a corner that is not there.** The highlighted patch sits mid-top of the board, and whisper hears the word as "corners". Change both to "block": "Replay one block." and "…the neighbor that started our block's chain…".
5. **[0:41–1:11][Visual] The RED unhappy rings on gold tiles read as orange outlines and blend into the gold (kf_08, 0:44).** Draw each ring with a 1 px background-colour gap between tile and ring and a 3 px RED stroke, so red separates from gold as clearly as it does from blue.
6. **[2:07–2:13][Concision] "With at most eight neighbors, these are the only shares up to sixty percent" spends 14 words on a caveat.** Replace it with "With at most eight neighbors, shares come in steps." The 0 % and 60 % end marks already show the crop. This also states why the bars matter: the demand crosses whole rungs.
7. **[3:13][Clarity] The HOLC sentence arrives with no link to the rule-made town.** Open it with "Real segregation has causes besides preference:" and keep the rest as written. The toy towns stay dimmed, so the toy rule is still not equated with the maps.
8. **[1:48–1:52][Audio] "That whole town is one point on this chart" runs at 208 wpm.** Synthesize it at speed 0.80.
9. **[3:32.5–3:33.8][Visual] The end card fades in over the still-fading town and meter, and "Sample Space" crosses the dimmed meter at 3:33.0.** Fade the town and meter out fully (0.4 s) before the card fades in.

**REACHES 9 IF ALL FIXED: yes, narrowly.** Fixes 1–2 lift Clarity to 9 and Hook to 9. Fix 3 with fix 8 lifts Audio to 8.5–9, and fixes 5 and 9 lift Visual to 9. With Originality still at 8.5 (the checkerboard-Schelling framing is well-trodden: Parable of the Polygons and countless classroom demos), the weighted score lands at about 8.95–9.0. No structural change is needed. The hook, the measured failure, the domino insight and the cited payoff are all present.

**KEEP**
- The measured failure: "plan predicts 0" directly above the live count of 74, with the 67 who never moved left lit (0:58–1:11).
- The corner/block replay: real tiles in step with the board, and each fraction built from its tiles with a "?" while the state is pending (1:13–1:41).
- The axis-to-ladder morph and the caret sliding ⅓ → ¼ with the count falling 238 → 95 (2:03–2:36), plus the exact return to the opening frame (3:24–3:31).
