# Episode 7, round 3: craft review (motion design, visual design, A/V sync)

Evidence: `review/` pack (metrics.json 19:32, newer than final.mp4 19:30). I read report.md, all 13 contact sheets and 18 full-resolution keyframes (kf 03, 05, 06, 10, 13, 16, 17, 19, 20, 22, 24, 26, 28, 30, 32, 34, 37, 40). I also pulled 28 extra frames with ffmpeg at 0:24.6, 0:25.6, 1:00.5, 1:01.5, 1:56.0, 1:56.6, 1:57.4, 2:20.6, 2:21.6, 2:24.3–2:28.6 (six frames), 2:33.8, 2:34.3, 2:42.6, 2:43.4 and 3:50.6–3:52.3 (eight frames), and measured audio RMS across 1:54.4–1:56.0. I recomputed the numbers and checked LLMZip on arXiv.

```
EPISODE: 007 — "How Much Information Is in a Letter?"
IDEA: A character costs log2(1/p) yes/no questions, so the average (entropy) depends on predictability, not alphabet size, and once you use the text before it, English carries about 1 bit per character, not 4.75.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.6   AFTER CEILING: 8.6 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none
FINAL: 8.6   PASS: no
```

## FACTS

| Claim | Status | Source / check |
|---|---|---|
| 27 symbols (A–Z plus space) | Verified | Shannon 1951 p. 56 |
| Five halvings take 27 to 1; ideal log2 27 = 4.75 | Verified | 4.7549 recomputed |
| "About one" bit per character (Shannon) | Verified | Shannon 1951 p. 50 |
| Nothing compresses below the true entropy on average | Verified | source-coding theorem |
| 3.75 extra (79%) | Verified | 3.75 / 4.75 = 0.789 |
| E is 130× as common as Z | Verified | data.json E_over_Z = 130.3 (Brown) |
| Space, E, T, A, O are 48% of text | Verified | top5_share = 0.4834 |
| E: 3.3 doublings | Verified | log2(1/0.1031) = 3.277 |
| Z: 1 in 1,260, needs 10.3 | Verified | 1/p = 1263; log2 = 10.30 |
| p·2^k = 1, so k = log2(1/p) | Verified | algebra |
| H1 = 4.11 bits (Brown) | Verified | data.json |
| 4.11 is "four times" ≈1 | Verified | arithmetic |
| After Q: U 98%; H = 0.16 | Verified | data.json after_Q (0.9814, 0.156) |
| After TH: E 68%, about half a question, H = 1.7 | Verified | 0.683; log2(1/0.683) = 0.549; 1.667 |
| All two-letter contexts: 2.81 | Verified (producer data, consistent) | data.json H_given_2_prev = 2.8105 |
| 79 of 102 first guesses; the passage | Verified | Shannon 1951 p. 56 |
| Guess-count entropy 1.42 | Verified | recomputed from counts 79,8,3,2,2,3,1×5 → 1.4223 |
| A better guesser can only lower it | Verified | Shannon §5–6 upper-bound argument |
| 0.6–1.3 bits at N = 100 | Verified | Shannon 1951 p. 64 |
| LLM, 2023, a book in 27 symbols: 0.84 bits/char | Verified | arXiv 2306.04050v2 §IV: "only 0.8426 bits/character" |
| Hidden char = Y, guessed first time | Verified | record line 3 |

No wrong or uncited empirical claims. The citations are on screen: Shannon (0:33–0:53 and 2:53–3:25), Brown Corpus (0:55–2:53) and Valmeekam et al. (3:26–3:35).

```
MECHANICS: runtime 3:52.4 · wpm 162 (speech) · max silence 1.95 s (2:20.3, planned prediction hold) · max static 3.13 s (3:42.3) · −14.0 LUFS / −2.1 dBTP · lead 0.0 s / trail 1.47 s · WER 2.1 % · 0 banned phrases · layout audit 0/204
```

## What I saw, beat by beat

- **0:00–0:13 Cold open.** The puzzle is concrete and the 27 tiles cascade in by 0:05. The question lands at 0:13, followed by a 1.9 s hold, and "The natural answer is 5" is a clean commit. The first frame (0:01) is still a row of empty dim boxes, which tells you little before the narration does.
- **0:13–0:29 Naive build.** The halving cuts and the 27→13→6→3→2→1 chain read well. At 0:24.6 the log₂27 build turns to soup: the copied "27" overlaps the chain's "27", a half-written "lo" glyph appears, and at 0:25.6 the flying 27 crosses the word "character". The settled line at 0:28.7 sits about 200 px right of centre, from x≈660 to 1665.
- **0:31–0:53 Chart entrance and fail.** The tiles drop onto a baseline and the columns rise together to 4.75. This is the best entrance in the series so far. The hatched "3.75 extra (79%)" overlay with its double arrow is a clear, measured failure.
- **0:55–1:09 Widths and re-sort.** The real widths appear with "10.3%" and "0.08%" labels, but the spoken "130 times" never appears on screen. The re-sort at 1:00.5–1:01.5 shows columns sliding through one another with black gaps between them. It reads as shuffling, not sorting.
- **1:11–1:43 Doubling strips and derivation.** This is excellent, and the derivation is what makes it 3b1b-grade. Each p·2ᵏ=1 → 2ᵏ=1/p → k=log₂(1/p) step lands on its own words. The chart behind is "dimmed", but its letter labels (E T A O I N S R H L D), the % ticks, and the full-strength yellow 4.75 line and label stay at full brightness (kf 13, 16, 17). That leaves three bright zones competing with the strips. "1 in 1260" (1:22.6) has no on-screen counterpart.
- **1:43–2:09 Skyline, area, pour.** The cost morph and "×32 wide" inset are good. The inset at 1:49–1:53 abuts the main axis at 100% with no gap or frame, so X J Q Z read as columns past 100% (kf 19). The pour is a real proof: the area becomes the height and is copied into "= 4.11 bits". The intermediate frame at 1:56.6 is floating fragments for about 1 s, which is acceptable.
- **2:18–2:51 Context.** The "? bits" slot fixes the round-2 stale-H problem. U widens at 2:25.5 on "98 times out of 100", but the **98% brace arrives at about 2:28.0, 3.7 s after "98" (2:24.3)**. While it flies to the axis title (2:25.5–2:26.5), the purple Q crosses the columns and the "100%" tick label. From 2:31 to 2:53 the y-axis still runs 0–10 while every quantity on screen is ≤ 2.81 (kf 28), so about 70% of the plot area is dead and the 0.16 / 1.67 / 2.81 differences are squeezed into the bottom 100 px.
- **2:51–3:35 Payoff.** Shannon's real record with a reading cursor and a live tally is memorable. "Treat each guess count as a symbol" (3:05) is the one conceptual leap the video does not earn. Nothing says *why* the guess counts carry the passage's information (Shannon's "identical twin" can rebuild the text from them), so the 1.42 arrives as an assertion. In row 3, "11 5" (kf 32, 34) reads as "115". The number line and the LLM marker slide are clean.
- **3:35–3:52 Landing.** THE OTHER DAY flies into the cold-open row and Y lands in the ? box. This exactly re-sees the first frame, which is the strongest landing in the series. Composition: from 3:39 to 3:45 the row sits in the upper third with the lower two-thirds empty (kf 37). The series ident cross-fades in at 3:51.6 and the file ends at 3:52.4, a 0.8 s flash that cannot be read. It also steals the last beat from the reframe image.

## Sync check

Deictics land within ±2 s everywhere except the "98" label, which is late by about 3.7 s, although the U widening it describes is on time. One spoken number is never shown ("130 times") and one is shown only as a sliver ("1 in 1260"). None of these triggers the sync cap.

## Audio

Measured: 162 wpm and on-target loudness, and every pause ≥ 0.9 s sits on a beat boundary. ASR dropped "questions" in "the average number of questions" (1:54.8). RMS shows 0.6 s of decaying energy (1:54.9–1:55.5) before the planned 0.2 s pause, so the word is probably swallowed or trailing off. ASR heard "pores" for "pours", "why" for "Y" and "cue" for "Q", which are homophones and acceptable.

## FIXES (highest impact first)

1. [3:05–3:12][Clarity] Turning guess counts into 1.42 is asserted, not earned. Before "Treat each guess count as a symbol", add about 5 s: "An identical twin with the same predictor could rebuild the passage from these counts alone." Visually, flash the counts row bright while the letters dim to 15% for 1.5 s, then fly the counts into the skyline. Trim 2–3 s elsewhere (fix 9) to keep the runtime under 3:55.
2. [2:31–2:53][Visual] The y-axis stays 0–10 while all data is ≤ 2.81, so the plot is about 70% empty (kf 28). Right after U flattens (about 2:31), animate the axis to 0–5 (ticks 0, 1, 2, 3, 4, 5) with the 4.11 reference riding along. The 0.16 / 1.67 / 2.81 levels and the ≈1 band then get about twice the vertical separation.
3. [1:11–1:43][Visual] The dimmed chart still has full-opacity letter labels, % ticks and a full yellow 4.75 line and label (kf 13, 16, 17). Set those to 30% with the chart, keeping only the E column and its "E" label bright as the strip's referent. Restore all of them at "Now give each character its own cost" (1:43).
4. [2:24.3–2:28.0][Sync] Make the 98% brace grow with U's widening (start about 2:25.0, done by "out of a hundred", 2:26.1), not 3.7 s after "98".
5. [1:00–1:02][Motion] The re-sort leaves black gaps and columns pass through each other (1:00.5, 1:01.5). Animate the sort as a contiguous reorder: interpolate each column's left edge from the old cumulative position to the new one, so the columns tile [0, 100%] with no gaps in every frame, over 1.5 s with smooth easing.
6. [0:24.6–0:28.7][Motion and Visual] The log₂27 build is glyph soup (27 over 27, a partial "lo", and the 27 crossing "character"), and the final line is 200 px off centre. Write "log₂" first, then TransformFromCopy the chain's 27 along an arc *below* the chain into its slot, then TransformMatchingTex "5" → "≈ 4.75". End by shifting the whole "questions per character log₂27 ≈ 4.75" group so it is centred at x = 0.
7. [1:49–1:55][Visual] The inset reads as columns beyond 100% (kf 19). Leave a 0.35-unit gap after the main axis, give the inset its own thin grey baseline and frame, and draw a dashed grey leader from the last four hairline columns (X J Q Z) to the inset.
8. [3:51.6–3:52.4][Motion] The 0.8 s ident flash is unreadable and cuts off the landing image. Drop the end-card cross-fade and hold the final landing frame (THE OTHER DAY Y, "1 guess" above the dimmed "5 questions") to the end, or move the ident to the optional ≤ 1.5 s slot after the stakes beat (§6).
9. [3:39–3:45][Visual] The landing row sits in the upper third with an empty lower two-thirds for 6 s (kf 37). Bring the dimmed tile row, the chain and "5 questions" back on "a single yes-or-no question" (3:43), not on "Splitting" (3:45.4). Alternatively, centre the row vertically and move it to y = 1.35 when the tiles return.
10. [1:54.8][Audio] "questions" in "the average number of questions" is swallowed: ASR misses it and the energy decays over 0.6 s. Regenerate the line with the pause *before* "Pour" lengthened to 0.35 s, and confirm that WER drops the delete.
11. [0:55–0:58][Clarity / Sync] "130 times as often" is not on screen. Grow a small "×130" in blue between the 10.3% and 0.08% labels on "130".
12. [1:22.6–1:25][Clarity / Sync] "1 in 1260" is not on screen. Label the Z strip's starting sliver "1/1260" (blue, Text ≥ 26) and fade it out as the counter starts.
13. [3:00–3:35][Visual] In row 3, "11 5" reads as "115" (kf 32, 34). Widen the two-digit cells to 0.42 or add a 0.06-unit extra gap after a two-digit count.
14. [2:25.5–2:26.5][Motion] The flying Q crosses the columns and the "100%" tick label. Route it through the right gutter (x > 6.0) and down to the axis title.

REACHES 9 IF ALL FIXED: yes. Nothing structural is missing. The episode has a real hook with a commit, a measured failure (3.75 extra, 79%), one picture (doubling strip → log₂(1/p) → area → pour) that turns into the formula, a sourced payoff with honest limits (easy cases vs 2.81, 1.42 as an upper estimate), and a landing that re-sees the first frame. Fixes 1–4 move Clarity and Visual to 9. Fixes 4–6 and 8 move Motion to 9. Fix 10 moves Audio to about 9. That gives a weighted score of about 9.0–9.1.

KEEP:
- The doubling strips with live counters, deriving p·2ᵏ=1 → k=log₂(1/p) step by step on the spoken words.
- The "pour": skyline area → full-width slabs → level line → copied into H, reused for after-Q and after-TH with the "? bits" slot.
- Shannon's own record (cursor and tally) → guess skyline → bits line → the landing where THE OTHER DAY flies into the cold-open row and Y fills the ? box.
