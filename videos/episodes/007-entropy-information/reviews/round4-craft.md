# Episode 7, round 4: craft review (visual design, motion, A/V sync)

Evidence: the existing `review/` pack (metrics.json 23:28 is newer than final.mp4 23:26). I read report.md, narration_diff.txt, transcript.txt and transcript_words.tsv, all 13 contact sheets, and 12 full-resolution keyframes (kf 01, 03, 07, 13, 16, 17, 21, 23, 30, 34, plus the 0:09.5 and 2:52.6 frames). I also pulled extra frames with ffmpeg at 1:00.5, 1:53.0, 2:18.6, 2:19.2, 2:50.5–2:53.4 (a strip of 6), 3:28.8, 3:38.4, 3:39.5, 3:40.5 and 3:41.5. I recomputed the numbers from data.json and checked LLMZip's 0.8426 on arXiv (2306.04050v2).

```
EPISODE: 007 — "How Much Information Is in a Letter?"
IDEA: A character costs log2(1/p) yes/no questions, so information depends on predictability rather than alphabet size; averaged with the text that came before, English carries about 1 bit per character, not the 4.75 that halving the alphabet suggests.
SCORES: Hook 9 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.6 (862.5/100)   AFTER CEILING: 8.6 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none
FINAL: 8.6   PASS: no
```

## FACTS

| Claim | Status | Check |
|---|---|---|
| 27 symbols (A–Z + space) | Verified | Shannon 1951 p. 56 |
| Five halvings 27→1; ideal log2 27 ≈ 4.75 | Verified | 4.7549 (data.json H0) |
| Shannon: "about one" bit per character | Verified | Shannon 1951 p. 50 |
| No compressor beats the true figure on average | Verified | source-coding theorem |
| 3.75 extra (79%) | Verified | 3.75/4.75 = 0.789 |
| E is 130× as common as Z; 10.3% / 0.08% | Verified | E_over_Z = 130.3 (Brown) |
| Space, E, T, A, O ≈ half (48%) | Verified | top5_share = 0.4834 |
| E: 3.3 doublings; Z: 1 in 1260, 10.3 | Verified | log2(1/0.1031) = 3.28; 1/p = 1263, log2 = 10.30 |
| p·2^k = 1 ⇒ k = log2(1/p) | Verified | algebra |
| H1 = 4.11 bits (Brown) | Verified | 4.1111 |
| After Q: U 98%, H = 0.16 | Verified | 0.9814; 0.156 |
| After TH: E 68%, ≈ half a question, H = 1.7 | Verified | 0.683; 0.549; 1.667 |
| All two-letter contexts 2.81 | Verified | H_given_2_prev = 2.8105 |
| 79 of 102 first guesses | Verified | Shannon 1951 p. 56; record in data.json |
| Guess-count entropy ≈ 1.4 | Verified | recomputed from 79,8,3,2,2,3,1×5 → 1.4223 |
| Identical twin can rebuild text from counts | Verified | Shannon 1951 p. 55 |
| 0.6–1.3 bits at N = 100 | Verified | Shannon 1951 p. 64 |
| LLM 2023, new book, 27 symbols: 0.84 bits/char | Verified | arXiv 2306.04050v2 §IV: "only 0.8426 bits/character" |
| Hidden character = Y, first guess | Verified | record, line 3 |

No wrong, fabricated or uncited claims. Citations are on screen: Shannon (0:31–0:53, 2:55–3:28), Brown (0:51–2:53), Valmeekam et al. (3:29–3:38).

```
MECHANICS: runtime 3:54.6 · wpm 160 (speech) · max silence 1.96 s (0:08.3, planned prediction hold) · max static 3.63 s (closing hold 3:51.0) · −14.0 LUFS / −1.9 dBTP · lead 0.00 s / trail 1.24 s · WER 2.0 % · banned phrases 0 · layout audit 0/218
```

No mechanical cap triggers. Every WER item is a homophone or a number-format difference (Q/"cue", U/"you", Y/"why", pours/"pores", "a hundred"/"one hundred"), not a mispronunciation.

## Beat-by-beat (flipbook read)

- **0:00–0:10 Cold open.** The puzzle is fully on screen from frame 1 (kf 01): the purple "already read" row, the yellow ? slot, 27 blue tiles, and "26 letters + space". "questions per character ?" arrives at 0:04 and the question ends at 0:08.3, followed by a 1.9 s hold. Clean and centred. The top-to-bottom reading order is well built.
- **0:10–0:25 Naive build.** The halving cuts and the 27→13→6→3→2→1 chain read well. The log2 27 ≈ 4.75 line is now centred and assembled in order (kf 03). This is fixed since round 3.
- **0:27–0:53 Chart entrance and fail.** The tiles become column feet and the columns rise to 4.75. The hatched "3.75 extra (79%)" with its double arrow is a measured failure. E and Z are isolated, then go to real widths with 10.3% / 0.08% on leaders and "×130" on "hundred and thirty" (kf 07). All of this is strong.
- **0:55–1:05 Re-sort.** It is now gap-free (1:00.5 frame: every column tiles 0–100%). Each of the five gets its outline flash in turn (T at 1:01), and the 48% brace lands on "nearly half".
- **1:05–1:39 Doubling strips and derivation.** This is the best 35 s in the episode. The chart behind dims properly to 30% (kf 13), and each algebra step lands on its own clause. One weak point: the Z strip has no visible referent. Z's 1/1260 sliver is invisible by construction, and Z's hairline in the main chart is not brightened the way E's column is (kf 13). So "Z" in the strip comes from nowhere.
- **1:39–2:13 Skyline, area, pour, H.** The cost morph and the framed ×28 inset with leaders now read correctly (kf 16). The pour itself (1:52–1:54, frame 1:53.0) moves all 27 columns at once: slabs cross one another and stack in no legible order for about 1.5 s. After the pour, the stacked level is drawn with 27 black slab outlines (1:55–2:13, sheet 7). They read as hatching rather than one quantity.
- **2:13–2:53 Context.** The "? bits" slot, the axis zoom and the gutter route for Q/TH are all clean (kf 21, 23). At 2:18.6 the brace is already labelled **98%** while it spans only about 26% of the axis, so the label tells the truth about the end state and a lie about the frame. The completed ladder 4.11 > 2.81 > 1.67 > ≈1, the summary image of the whole context section, appears at 2:51.3 (in sync with "2.8" at 2:51.0). But it is fully assembled for only about 1.5 s before the cross-dissolve begins at 2:52.8.
- **2:53–2:55 Transition.** This is a plain cross-dissolve, with the record superimposed on the chart at 2:53.4. The four levels the viewer just built are thrown away, and 30 s later they reappear on the bits-per-character line as fresh markers (3:21). Only 1.42 flies in from its source. This is the largest continuity break in the video.
- **2:55–3:19 Shannon's record, twin, guess skyline.** The reading cursor and live green tally are memorable (kf 30). The twin beat (letters fade to 12%, counts remain, letters rebuild) makes the argument visually. The mini skyline's y-axis runs 0–7 while the poured level is 1.42 (kf 34), so about 75% of the plot is dead space.
- **3:19–3:38 Bits line.** The number line is clear, but its markers carry only numbers. 4.75, 4.11, 2.81 and 1.42 have no identity tag (frame 3:28.8), so the viewer has to recall which method each came from 30–90 s earlier. At 3:28.8 the Shannon and Valmeekam citations are superimposed mid-cross-fade, which leaves illegible text for about 0.5 s.
- **3:38–3:54 Landing.** THE OTHER DAY is lifted out of the record (good). From 3:39 to 3:43, though, it floats alone on an empty frame: first off-centre right (3:40.5 frame, x ≈ 955–1560 px, nothing else on screen), then letter-spaced with a white, unboxed Y (3:41.5). Only after that do the boxes and tiles fade in under it. When "the Y" is spoken (3:40.4), Y has no slot to land in. The re-seen cold-open frame from 3:43 is excellent and holds to the end.

## Sync check

The deictics land within ±2 s: "Z costs as much as E" → isolation at 0:49; "130" → ×130 at 0:53; "nearly half" → 48% at 1:03; "1 in 1260" → 1/1260 at 1:19; "4.11" → "= 4.11 bits" at 2:05; "U" → widening at 2:18; ".16" → 0.16 at 2:27; "long runs" → ? run at 2:41; "1.7" → 1.67 at 2:45; "2.8" → 2.81 at 2:51.3; "0.84" → marker at 3:35. "Shannon called that average the entropy" (1:55.6) → "average" becomes H at about 1:58.5, 3 s later, though "bits" arrives in step. No cap.

## Scoring rationale

- **Hook 9.** A concrete puzzle in frame 1, a question by 0:08, a 1.9 s hold, then "the natural answer is five", a likely-wrong number the viewer has just committed to. Tension rises through 4.75 → 4.11 → 0.16 / 1.67 → 1.42 → 0.84, and the ending re-sees the first frame exactly.
- **Clarity 8.5.** The core derivation is re-derivable after one watch: halving the probability, p·2^k = 1, area = average, pour = H. The one hard step, "half a question … the fractions add up" (2:34–2:44), is asserted, not shown. The four ? boxes at 2:41 put no number in any box, so nothing visibly adds up. The markers on the bits line (3:21–3:37) are untagged.
- **Visual 8.5.** The palette is semantic and consistent, hierarchy is good, and the layout audit is clean. Remaining issues: the empty, off-centre landing frames (3:39–3:43); the striped slab stacks (1:55–2:13, 2:45–2:53, 3:15–3:19); the mini skyline's dead space (3:13–3:19); the citation superimposition (3:28.8); and the dissolve soup (2:53.4). Each is minor, but together they exceed the "at most 2 minor issues" of an 8 and miss the 9 standard of one focal point in every frame.
- **Motion 8.5.** The doubling, the algebra, the re-sort and the U/E widenings are all meaningful transforms. Three moves fall short. The chart → record transition is a dissolve that discards built objects (2:53). The pour is simultaneous and illegible (1:52–1:54). The 98% / 68% labels are static while the widths they measure grow (2:17.6–2:20, 2:29–2:31).
- **Audio 8.5.** On target for loudness and pace, with intentional holds at 0:08, 1:29.6 and 2:15.8. The other inter-sentence gaps are a uniform 0.4–0.6 s for almost 4 minutes (report silence list), so beat boundaries such as 0:39.5, 1:37.7 and 3:37.4 get the same breath as mid-thought commas.
- **Concision 8.5.** At 608 words in 3:54.6 there is little slack, but "Q and th are the easy cases" (2:44.7–2:47.4) restates what the 2.81 line then shows. The context section is so dense that its summary frame gets only 1.5 s.
- **Originality 9.** Shannon's actual 1951 record with the identical-twin argument, the pour-the-skyline proof of entropy, and the landing on THE OTHER DAY are images a viewer would remember and share.

## FIXES (highest impact first)

1. **[2:34–2:44][Clarity]** "The fractions add up" is shown by four empty ? boxes. Use a real 4-character run from the record whose two-letter contexts are in Brown, e.g. the "HE␣O" of THE OTHER. Compute each character's cost log2(1/p(x | previous two)) with `data.py`'s conditional counts. On "long runs of letters", write each cost in yellow inside its ? box (e.g. "0.55" over E after TH). On "the fractions add up", TransformFromCopy the four numbers into a yellow sum under the run, "= N questions for 4 letters", with N computed. Without this, Clarity stays at 8.5.
2. **[2:51–2:55 and 3:19–3:22][Motion]** The finished context ladder dissolves after about 1.5 s, and its values are rebuilt from nowhere on the bits line 30 s later. Hold the completed ladder ≥ 2.2 s (2:51.3 → ≥ 2:53.5), paid for by fix 11. Then shrink the 4.11 / 2.81 level labels into small markers parked in the right gutter (x ≈ 6.0) while the chart fades. On "Shannon's tests" (3:19), fly them onto the bits-per-character line exactly as 1.42 already flies in. Replace the cross-dissolve at 2:52.8 with FadeOut of the chart (0.6 s, shift DOWN×0.3) followed by FadeIn of the record, so the two are never superimposed.
3. **[3:38.4–3:43][Visual/Motion]** The landing floats THE OTHER DAY alone, off-centre, with an unboxed Y. Keep the cold-open box row on screen through the fade: fade the record and line to 0, then bring the 12 purple boxes and the yellow ? box in at their cold-open positions at 3:38.0. Fly T,H,E,␣,O,T,H,E,R,␣,D,A straight from the record into the 12 boxes, and Y into the ? box, in one 1.5 s `TransformMatchingShapes`/LaggedStart (lag 0.05) that ends on "the Y" (3:40.4). Cut the intermediate centred and letter-spaced states, and flash the ? box yellow on "Y".
4. **[3:21–3:37][Clarity/Visual]** The bits-line markers carry numbers only. Add a 1–2-word grey tag under each value label (Text font_size ≥ 18, ticks size): 4.75 "halving", 4.11 "letter odds", 2.81 "2-letter context", 1.42 "the guesser". That is 7 words, within the 12-word cap. Keep 0.6–1.3 and LLM as they are.
5. **[2:17.6–2:20, 2:29–2:31][Motion]** The 98% and 68% labels are fixed text while their braces widen from about 10% / 7%. Make each label a `DecimalNumber` (0 decimals, "%" suffix) with an updater bound to the column's current width, so it reads 26% at 2:18.6 and lands on 98% as U finishes. Do the same for 68%.
6. **[1:51.8–1:54][Motion]** The pour moves all 27 columns at once, so slabs cross and the stacking order is illegible (frame 1:53.0). Stage it: pour the space column alone (0.8 s) into a full-width slab on the baseline, then E (0.6 s) on top of it, then the remaining 25 with LaggedStart (lag_ratio 0.04) in sorted order, each stacking on the previous top. Total about 2.5 s, still inside "Then pour the skyline flat, and its height is that average." Use the same staging for the after-Q, after-TH and guess-count pours.
7. **[1:55–2:13, 2:27, 2:45–2:53, 3:15–3:19][Visual]** Poured stacks are drawn with 27 black slab outlines that read as hatching. Set the slab stroke opacity to 0.2 (or stroke = fill colour) once a pour completes, keeping only the top edge, so the level reads as one block under its yellow line.
8. **[3:11–3:19][Visual]** The mini skyline's y-axis runs 0–7 for a final level of 1.42 (kf 34), leaving 75% dead plot. After the pour completes, zoom its y-axis to 0–2.5 (ticks 0, 1, 2), as the context beats already do, with the 1.42 line and its label riding along.
9. **[3:28.5–3:29.2][Visual]** The Shannon and Valmeekam citations are superimposed mid-fade (frame 3:28.8). Fade the Shannon citation out fully (0.4 s) before the Valmeekam citation fades in (0.4 s), or use `ReplacementTransform` with `run_time` 0.6 so the glyphs morph instead of overlapping.
10. **[0:39.5, 1:37.7, 2:52.0, 3:37.4][Audio]** Inter-sentence gaps are a uniform 0.4–0.6 s. Lengthen these four beat-boundary gaps to 0.9 s (fail, skyline, Shannon's experiment, landing) and trim intra-beat sentence gaps inside the 2:13–2:51 context beat to 0.3 s, which keeps the runtime under 3:58.
11. **[2:44.7–2:47.4][Concision]** Cut "Q and th are the easy cases." and say "But averaged over every two-letter context, it's still two point eight." That saves about 2.4 s; spend it on the ladder hold in fix 2.
12. **[1:17.7–1:22.6][Visual]** The Z strip has no visible referent. While the Z strip runs, raise Z's hairline column to full blue opacity with the white outline flash, and raise its axis letter to full ink, exactly as E is treated at 1:05.
13. **[1:45–1:53][Visual, nitpick]** The inset frame's right edge sits at x ≈ 6.47, just outside the 6.4 safe line. Shift the inset 0.1 left.

REACHES 9 IF ALL FIXED: yes, narrowly. Fixes 1 and 4 move Clarity to 9; 3, 4, 7, 8 and 9 move Visual to 9; 2, 5 and 6 move Motion to 9; and 10–11 lift Audio and Concision to 9. That gives a weighted 9.1, or 9.0 even if Audio stays at 8.5. No structural change is needed: the hook, the failure beat and the visual insight are all in place.

KEEP:
- The doubling strips with live yellow counters, and the one-clause-per-step derivation p·2^k = 1 → 2^k = 1/p → k = log2(1/p) (1:05–1:39).
- The skyline pour to H with the "? bits" slot reused for after-Q and after-TH, plus the axis zoom (1:45–2:51).
- Shannon's real record → identical twin → guess skyline → THE OTHER DAY landing back in the cold-open frame (2:55–3:54).
