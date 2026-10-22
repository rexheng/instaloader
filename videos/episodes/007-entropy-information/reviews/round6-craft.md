# Round 6 review: craft (visual design, motion, A/V sync)

Critic: independent; emphasis on visual design, motion craft and audio/visual sync. All dimensions scored.
Evidence: `review/` pack (metrics.json 07:01 is newer than final.mp4 06:54, so it was reused): report.md, all 14 contact sheets, 14 full-resolution keyframes (kf_01, 04, 07, 13, 16, 17, 23, 26, 27, 28, 31, 33, 35, 37). I also extracted these frames with ffmpeg: 0:36.5, 1:25.0, 1:40.0, 2:44.4–2:45.9 (gutter crop), 2:45.0, 3:10.0–3:12.0 (5-frame strip), 3:10.8, 3:21.5, 3:43.0 and 3:57.6. I re-ran ASR on 2:45–2:50 and 3:08–3:13.

```
EPISODE: 007 — "How Much Information Is in a Letter?"
IDEA: A character costs log2(1/p) yes/no questions, so the average (entropy) is the area of a probability-width / cost-height skyline poured flat, and it falls from 4.75 to about 1 bit as the guesser uses more of what came before.
SCORES: Hook 9 · Clarity 9 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.8   AFTER CEILING: 8.8 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none
FINAL: 8.8   PASS: no
```

## FACTS

| Claim | Status | Source / check |
|---|---|---|
| 27 symbols; 5 halvings 27→13→6→3→2→1 end on Y | Verified | arithmetic; on-screen cut positions N\|O, U\|V, X\|Y, Y\|Z, Z\|␣ give 13, 6, 3, 2, 1 (kf_04) |
| log2 27 ≈ 4.75 | Verified | 4.7549 |
| Shannon 1951: "about one" bit; 0.6–1.3 at 100 letters | Verified | Shannon 1951 BSTJ 30(1), p. 50 and p. 64 table (facts.md 5, 28) |
| 3.75 extra (79%) | Verified | 3.75/4.755 = 0.789 |
| E 10.3%, Z 0.08%, ×130 | Verified | 0.10314/0.000792 = 130.2 (Brown, data.py) |
| Space+E+T+A+O ≈ 48% | Verified (corpus) | facts.md 11 |
| E: 3.3 doublings; Z: 1/1260, 10.3 | Verified | log2(1/0.1031) = 3.28; log2 1263 = 10.30 |
| p·2^k = 1 ⇒ k = log2(1/p); average = Σ p log2(1/p) | Verified | re-derived |
| H1 = 4.11 (Brown) | Verified (corpus, independently recomputed in earlier rounds) | facts.md 17 |
| After Q: U 98%, H = 0.16; after TH: E 68%, 0.55, H = 1.67; two-letter avg 2.81 | Verified (corpus) | facts.md 19–21b |
| Run E R E ␣: 0.5+3.0+2.6+1.6 = 7.7 → 8 | Verified | sum 7.7; ceil 8 |
| 27² = 729; 27^100 ≈ 10^143; Brown 5.75 M chars | Verified | log10 27^100 = 143.1 |
| 79 of 102 first guesses; record (display 9) | Verified | Shannon p. 56; tally 79/8/3/2/2/3/1×5 sums to 102 |
| Guess-number entropy 1.42 (upper bound); log2(1/q) = 3.67 for 2nd | Verified | recomputed: 1.4223; log2(102/8) = 3.672 |
| LLMZip 0.84 bits/char on a book released on Gutenberg May 2023, 27 symbols | Verified | arXiv 2306.04050v2, §IV / Table IV: "only 0.8426 bits/character" (checked by web search this round) |
| "Twin" reconstructs passage from counts | Verified | Shannon 1951 p. 55 ("identical twin") |

## MECHANICS

runtime 3:57.7 · 157 wpm (speech time; 184 excluding pauses) · max internal silence 2.09 s (2:08.5, the planned Q prediction pause) · max static 3.5 s (end hold) · −14.1 LUFS / −2.2 dBTP · leading 0.0 s, trailing 1.04 s · 0 black frames · layout audit 0 issues · WER 1.7%.
ASR diffs checked: "longer"→"other" (2:47) and the missing "treat" (3:10.6) are segmentation artifacts. Re-transcribing the clips gives "longer contexts need more text…" and "Treat each guess count as a symbol". "pores"/"why" are homophones, not mispronunciations. No banned phrases or patterns found.

## What I saw (flipbook notes)

- **0:00–0:10** The context row, the yellow ? box and the 27 candidate tiles are all in frame 1. The question is spoken by 0:08 and held silent 2.0 s on "questions per character ?". The hook is clean.
- **0:10–0:23** The halving cuts close on **Y**, which plants the landing. log2 27 ≈ 4.75 is built in place from the chain's 27 (kf_04). Good.
- **0:24–0:52** The tiles become the feet of columns, then the uniform 4.75 skyline and the green ≈1 band. A hatched "3.75 extra (79%)" block follows, then E and Z isolated with 10.3% / ×130 / 0.08% (kf_07). The measured failure is on screen. Strong.
- **0:52–1:35** A gap-free re-sort, the doubling strips and the counter. The equation is built centre stage from E's column and the counter (1:21–1:33). Each algebra step lands on its own words.
- **1:35–2:07** Heights morph to log2(1/p), the ×28 inset, the skyline turns yellow on "area", then the **pour** (1:44–1:47) and the level born at 4.11. The live gap meter goes 3.75 → 3.11. This is the episode's signature image: the animation is the argument.
- **2:07–2:58** Context beats. The Q box turns purple and the value slot becomes "?". U swallows the bar; the axis re-fits; 0.16; TH; the E-outline at 0.55; the run box with costs; 1.67; the 2.81 average with 1.81 extra. Colour semantics hold throughout: blue = probability, yellow = questions/bits, green = Shannon, purple = context.
- **2:58–3:41** Shannon's record is revealed under a cursor with a green tally (kf_31, very good). The twin fade, the counts dropping into the guess skyline (3:10–3:12), the pour to ≤1.42, then the bits-per-character line with the LLM marker at 0.84.
- **3:41–3:57** THE OTHER DA rises into the boxes and Y lands in the ? box. The tiles and the 27→1 chain return dimmed. "1 guess" sits against "5 questions". It closes on the opening frame, re-seen.

## FIXES (highest impact first)

1. **[3:10.0–3:12.0][Motion/Visual] The count flight is unreadable.** All ~102 guess counts fly at once, in about 0.8 s, through the 30%-opacity passage text. At 3:10.8, numerals sit on top of the RATHER DRAMATICALLY row and a "1" lands on the "bits" axis label (extracted frame at 3:10.8). A viewer cannot track 102 objects, so the one transform that proves "the same skyline" reads as noise.
   - Before the flight, drop the record letters to 12%.
   - Fly by group: first all the 1s as one `AnimationGroup` (lag_ratio 0.02, run_time 1.2) into the 1st column, then the 2s, then the rest (run_time 0.8).
   - Route the paths below the record (`path_arc` ≤ 0.3, start by shifting DOWN 0.3).
   - Keep the axis title "bits" out of the paths: place it after the drop, or move it left of the axis.
   - Take the extra ~1.2 s from the existing 0.5 s pause at 3:09.8 plus a slower "Treat each guess count as a symbol" (narration pause 0.4 s after "symbol").

2. **[3:19–3:41][Visual/Clarity] The payoff number line's markers are unlabelled numbers.** 1.42 / 2.81 / 4.11 / 4.75 sit there for 22 s (kf_35, kf_37) with no identity, so the viewer has to remember what each number was. Meanwhile the dimmed record fills the top 45% of the frame and pushes the summary picture into the lower third. This should be the screenshot frame of the episode.
   - Add a grey 26-pt tag under each marker, below the axis numbers or as a second row: "halving" (4.75), "letter odds" (4.11), "2-letter context" (2.81), "human guesser" (1.42), "LLM" (0.84, already present).
   - Fade the record to 0 at 3:19 (it is not referenced again until 3:41, where it can fade back for the landing), then move the number line up to y ≈ 0.
   - Raise the "1924 book · on Gutenberg May 2023 · 27 symbols" note from ~24 px cap height to at least the 34 px primary-label size (`Text` ≥ 26), or shorten it to "book released after training" at that size.

3. **[2:28–2:31][Audio/sync] "like three point three doublings" names something no longer on screen.** The doubling strips left at 1:35, and nothing visible refers to 3.3 here (sheet 9, 2:29). Either:
   - cut the phrase: "Half a question sounds impossible, but a compressor…" (also saves ~1.5 s, which helps concision), or
   - on "three point three", ghost E's 3.3 strip/counter back above the chart at 40% for 1.5 s.

4. **[2:35–2:47][Visual] The run box and its costs crowd the equation, and two yellow results compete.**
   - The run costs "0.5 3.0 2.6 1.6" are ~30 px cap height and wedged under the box at top-right.
   - "7.7 → 8 questions" sits 90 px from the equation's "bits".
   - Both stay at full strength while the 1.67 level is born and copied (kf_27), so the frame has two yellow focal numbers.
   - Change: costs to `MathTex` font_size ≥ 36. On "After TH, the average", dim the run box, costs and total to 30% (or collapse the run back into the ? box then, instead of at "But averaged").

5. **[1:24.6–1:25.4][Motion] The 3.3 → 2^k copy scribbles over its source.** The copy morphs in place and produces a garbled "3,3" glyph overlapping the source "3.3" counter (extracted frame at 1:25.0). Lift the copy first (`copy.animate.shift(DOWN*0.4)`, 0.3 s), then `FadeTransform` it into 2^k along a short arc.

6. **[2:44.6–2:45.6][Motion] The 2.81 gutter label's copy overlaps its source, then crosses the 4.11 dashed line.** For a few frames the two "2.81" glyphs stack (gutter crop at 2:44.8), then the copy crosses the 4.11 line on its way up (2:45.4). Shift the copy left 0.4 before rising, or route it with `path_arc=-0.6` through the empty space left of the gutter labels.

7. **[1:38–1:42][Visual] The ×28 inset sits on the safe-area edge.** The frame's right edge is at x ≈ 6.46 units and its "10.3" label at x ≈ 6.39 (extracted frame at 1:40.0). "×28 wide" is ~24 px cap height. Shift the inset group left 0.15 and set the "×28 wide" label to `Text` ≥ 26 (or MathTex ≥ 36).

## REACHES 9 IF ALL FIXED: yes

Fixes 1, 2, 4, 5 and 6 lift Visual and Motion to 9. Fix 3 removes the only deictic miss (Audio 9) and trims slack (Concision toward 9). That gives 135 + 225 + 135 + 135 + 90 + 85..90 + 90, so 9.0–9.1. No structural change is needed: hook, measured failure, a visual insight that transforms into the formula, a sourced payoff and a landing that re-sees the opening are all in place.

## KEEP

1. The **pour**: the cost skyline collapsing into a flat level, born at 4.11 / 0.16 / 1.67 / 1.42. It is the same picture each time and it carries the whole argument.
2. The **persistent context row**: it carries the episode (purple Q / TH / THE OTHER DA), the halving chain plants Y at 0:17, and Y lands in the ? box at 3:43.
3. The **live gap meter** (3.75 → 3.11 → 1.81 → 0.42 extra) and Shannon's real record revealed under a cursor with the green 79/102 tally.
