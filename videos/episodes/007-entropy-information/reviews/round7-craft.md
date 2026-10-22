# Round 7 review: craft (visual design, motion, A/V sync)

Critic: independent; my emphasis is visual design, motion craft and audio/visual sync, but I scored every dimension.

Evidence:
- I reused the `review/` pack, because metrics.json (17:48) is newer than final.mp4 (17:46). From it I read report.md, all 12 contact sheets, the transcript, narration.txt, script.md and facts.md.
- Full-resolution keyframes read: kf_01, 04, 07, 13, 14, 16, 19, 24, 25, 27, 29, 31, 32, 37, 40.
- Motion strips I extracted at 4 fps (`/tmp/r7c/strip_*.png`): 0:20.0, 0:23.5, 1:24.5, 1:27.0, 1:57.5, 2:24.0, 2:49.5, 2:51.5, 3:19.5 and 3:21.5. I also took a 2 fps strip at 0:46–0:52.
- I made a 2× crop of the mini-chart labels at 2:54.1.
- I recomputed the guess-record entropy from data.json and re-checked LLMZip Table IV (arXiv 2306.04050v2, 0.8426) by web search.

```
EPISODE: 007 — "How Much Information Is in a Letter?"
IDEA: A character costs log2(1/p) yes/no questions, so the average (entropy) is the area of a width = probability, height = cost skyline poured flat, and it falls from 4.75 to about 1 bit as the guesser uses more of what came before.
SCORES: Hook 9 · Clarity 9 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 9 · Originality 9
WEIGHTED: 8.8   AFTER CEILING: 8.8 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none
FINAL: 8.8   PASS: no
```

## FACTS

| Claim | Status | Source / check |
|---|---|---|
| 27 symbols; five cuts 27→13→6→3→2→1 end on Y | Verified | arithmetic; cut positions in kf_04 |
| log2 27 ≈ 4.75 | Verified | 4.7549 |
| Shannon 1951: "about one"; 0.6–1.3 bits with 100 letters of context | Verified | Shannon 1951, BSTJ 30(1), p. 50 and the p. 64 table (facts.md) |
| 3.75 extra (79%) | Verified | 3.75 / 4.755 = 0.789 |
| E 10.3%, Z 0.08%, ×130; Z "one in 1260", 10.3 doublings | Verified | data.json: 0.10314, 0.000792, ratio 130.3, 1/p = 1263, log2 = 10.30 |
| Space+E+T+A+O ≈ 48% ("nearly half") | Verified | top5_share 0.4834 |
| E: 3.3 doublings | Verified | log2(1/0.1031) = 3.28 |
| p·2^k = 1 ⇒ k = log2(1/p); average = Σ p log2(1/p) | Verified | re-derived |
| H = 4.11 bits (Brown, 27 symbols) | Verified (corpus) | data.json H1 = 4.111 |
| After Q: U 98%, 0.16 bits | Verified (corpus) | 0.9814; H = 0.156 |
| After TH: E 68% ("two thirds"), about half a question, H 1.67 ("1.7") | Verified (corpus) | 0.6833 → 0.549; H = 1.667 |
| Run E ␣ O: 0.5 + 0.6 + 3.8 = 4.9 → 5; one at a time 1 + 1 + 4 = 6 | Verified | 0.549, 0.578, 3.796 (sum 4.923); each rounds to the value shown, and the displayed sum is exact |
| Average over all two-letter contexts 2.81 | Verified (corpus) | H_given_2_prev = 2.810 |
| 27² = 729; 27^100 ≈ 10^143; Brown 5.75 M chars | Verified | log10 = 143.14; 5,751,047 |
| 79 of 102 first guesses; the record | Verified | Shannon p. 56; data.json record: 79/102, row lengths 38/30/34 match the text |
| Guess-number entropy ≈ 1.42 (an upper estimate); log2(1/q) = 3.67 for the 2nd guess | Verified | recomputed: 1.4223; log2(102/8) = 3.672 |
| "A twin … could rebuild the passage from these counts" | Verified | Shannon 1951 p. 55 (identical twin) |
| LLMZip, 2023: 0.84 bits/char on a book released on Gutenberg after training | Verified | arXiv 2306.04050v2, Table IV: 0.8426 (web search this round) |

## MECHANICS

| Measure | Value |
|---|---|
| Runtime | 3:34.2 |
| Pace | 152 wpm over speech time (143 overall); 496 narration words |
| Longest internal silence | 2.23 s at 1:49.5, the planned Q prediction hold |
| Lead / trail | 0.00 s / 0.88 s |
| Longest static stretch | 3.33 s (the closing hold) |
| Loudness | −14.0 LUFS / −2.1 dBTP |
| Other | WER 1.4 %; 0 black frames; 0 banned phrases; layout audit 0 issues |

Narration-craft flags I checked:
- Two sentences run above 200 wpm: "The hidden character from the start…" at 3:19.6 (208 wpm) and "A better guesser could only lower it" at 2:57.3 (203 wpm).
- The longest stretch without a breath is 11.5 s, the LLM sentence from 3:07.5 to 3:19.0.
- Transcript oddities are not mispronunciations. "why" for Y is a homophone. The garbled whisper segment at 1:40.6–1:54.1 is only a segmentation artifact: the word timings show "4.75, but it's four times Shannon's estimate" intact (100.5–105.4 s).

## What I saw (flipbook)

- **0:00–0:10.** The context row, the yellow ? box and the 27 tiles are all there in frame 1. The question lands by 0:07 and is followed by a 2.1 s silent hold on "questions per character ?". This is a strong hook.
- **0:10–0:22.** The cuts and the chain close on Y. `log2 27 ≈ 4.75` is built in place, and 5 swaps cleanly to 4.75 (0:20–0:22 strip, no glyph soup).
- **0:23–0:38.** The tiles fall on a wave into the feet of the columns, which are the same objects persisting, and the uniform 4.75 skyline rises. The ≈1 band and the Shannon citation follow, then the hatched "3.75 extra (79%)".
- **0:38–0:52.** E and Z are isolated with real widths, then 10.3% / ×130 / 0.08% (kf_07, clean). The re-sort follows, and the white outline steps ␣→E→T→A→O exactly on each spoken letter (0:46–0:50 strip), ending in the 48% cut.
- **0:52–1:21.** The doubling strips and counters (3.3, 10.3). The equation is built centre stage from E's column and the counter, and the algebra steps land on their words (kf_13, kf_14).
- **1:21–1:47.** Heights morph to log2(1/p), the ×28 inset appears, the skyline goes yellow on "area", then comes the pour and the 4.11 level, and average → H. The live meter goes 3.75 → 3.11. This is still the best passage in the series.
- **1:47–2:27.** The Q box turns purple, U swallows the bar and the level pours to 0.16. The TH skyline gets a 68% brace, then the run bill (kf_24, now clean and well placed). 1.67 arrives with the bill stepped back to 30% (kf_25: one focal number), then 2.81 with 1.81 extra (kf_27).
- **2:27–2:47.** The contexts arithmetic, Shannon's record revealed under a cursor while the context row reads along, and a green tally running to 79 / 102 (kf_29, excellent).
- **2:47–3:00.** The counts fly by guess number into the guess skyline, then the pour to ≈ 1.42, "upper estimate" and "0.42 extra".
- **3:00–3:19.** The tagged bits-per-character line, and the LLM marker drops to 0.84 inside the band (kf_37: this is the screenshot frame; the round-6 fix landed).
- **3:19–3:34.** THE OTHER DA steps under the boxes and rises in, Y lands in the ? box, and the 0:17 frame returns with "1 guess" against "5 questions" (kf_40). The opening frame is re-seen.

Colour semantics hold all the way through: blue is probability, yellow is questions/bits, green is Shannon's measurements, purple is context, grey is abandoned or reference. No frame is slide-like.

## Defects found (evidence)

1. **2:53–2:57, mini guess chart labels below the clearance minimum (Visual).** In the 2× crop of kf_31 (2:54.1), "1st" sits about 8 px above "share of guesses", and "2nd" and "3rd+" are about 8 px apart, so they read as one label. The §5 minimum is 20 px. The layout audit did not catch this.
2. **2:49.5–2:53.0, the count flight is better but still split-focus (Motion).**
   - The stream of 79 ones runs diagonally through the dimmed RATHER DRAMATICALLY row and its count row (strip 2:49.5, frames 4–5).
   - At 2:52.0 the last counts (17, 15, 11, 8) are still in the air over the third text row while "bits", "1st / 2nd 3rd+", "share of guesses" and `log2(1/q) =` are being written (strip 2:51.5, frame 3). Two things compete for the eye at the moment the narration says "the same skyline".
3. **2:51–2:59, composition (Visual).** The top half of the frame is the passage at about 12 % opacity (kf_31, kf_32). That is below the §5 floor for de-emphasised context (25–40 %), so it reads as neither present nor gone. The guess chart is a small panel in the lower-left 55 % of the frame, with its right third empty.
4. **2:24.0, the gap meter's label leads its arrow (Motion).** "3.11 extra" is already drawn at the 4.11 line while the arrow spans only about 1 → 2 (strip 2:24.0, frame 1); it reaches 4.11 a quarter-second later. The same pattern shows at 0:25: the "4.75" label rides at the top of bars still rising through about 2.5 (strip 0:23.5, frames 6–7).
5. **3:19.5–3:19.75, the payoff line leaves in about 0.25 s (Motion).** It is gone between consecutive 4 fps frames as the record snaps back, so in practice it is a hard cut out of the episode's best frame, on "The hidden character". It sits at a beat boundary, so it is allowed, but it is abrupt.
6. **3:19.6 and 2:57.3, rushed delivery (Audio).** The landing's first sentence runs at 208 wpm, the fastest line in the episode, exactly where the episode should breathe. "A better guesser could only lower it" runs at 203 wpm. The LLM sentence at 3:07.5–3:19.0 is 11.5 s with no breath: 27 words, a date, a book, Gutenberg, training and a number.
7. **2:53.0, the 2nd-guess column flashes olive (Visual, nitpick).** It is yellow over blue at partial opacity when 3.67 is copied, a seventh hue that appears nowhere else.

## FIXES (highest impact first)

1. **[2:49.5–2:53.0][Motion] De-conflict the count flight.**
   - Fade the passage letters *and* their count rows' non-flying digits to 0 before the flight starts. The record returns at 3:19 anyway.
   - Route every count straight down its own column of text (x fixed), then horizontally along y = −0.4 above the axis into its column. Nothing then crosses another row.
   - Delay "bits", "share of guesses", "1st/2nd/3rd+" and `log2(1/q) =` until 0.2 s after the last count lands. Take the 0.5 s needed from the 0.8 s pause after "symbol".
2. **[2:53–2:57][Visual] Fix the label clearances on the mini chart.**
   - Move "share of guesses" down 0.15 units, or move the category labels up 0.1.
   - Place "3rd+" centred under its own column group with ≥ 0.2 units between it and "2nd"; if the 2nd column is too narrow, put "2nd" and "3rd+" on leaders above the columns.
   - Add a 2.9 s frame to the layout audit's check list here: it currently misses this group.
3. **[2:51–2:59][Visual] Recompose the guess skyline.**
   - With the passage at 0 (fix 1), centre the chart: shift it up about 1.2 units and right so it is centred on x = 0.
   - Keep `log2(1/q) = 3.67` on a short grey leader to the 2nd column, so it cannot be read as the height of the tall tail columns.
   - Flash the 2nd column with the standard white outline plus brighter blue (the episode's own emphasis rule) instead of the yellow/blue olive blend.
4. **[3:19.6–3:23][Audio] Slow the landing.**
   - Insert `[pause 0.6]` after "inside that range." and split the first landing line: "The hidden character from the start [pause 0.3] is the Y in 'the other day'."
   - Run the landing paragraph at speed 0.78, or add `[pause 0.4]` after "one guess".
   - This also gives fix 5 its time.
5. **[3:19.5–3:20.3][Motion] Let the payoff line leave over 0.6–0.8 s.** Keep the 1.42 (person) marker for an extra 0.4 s and let it fade last as the record comes up, so the transition reads "person → that person's record", not a cut.
6. **[3:07.5–3:19.0][Audio/Clarity] Give the LLM sentence a breath.** "In twenty twenty-three, a language model compressed part of a book [pause 0.3] that reached Project Gutenberg after its training. [pause 0.4] It needed point eight four bits, inside that range." The note's three parts already land on "book / Gutenberg / training", so the cue words do not change.
7. **[2:24.0 and 0:24.5–0:25.3][Motion] Grow labels with the thing they measure.**
   - Gap meter: make the "N extra" label a live `DecimalNumber` attached to the arrow's midpoint, counting from 0 as the arrow grows.
   - Column rise: hold "4.75" off until the bars reach the dashed line, or attach it to the dashed line instead of the bar tops.

## REACHES 9 IF ALL FIXED: yes

- Fixes 1–3 and 7 lift Visual and Motion to 9, because the count flight and the mini chart are the last frames where §5 is breached and focus splits.
- Fixes 4–6 lift Audio to 9: the landing gets its breath and there are no more > 200 wpm or 11 s breathless runs.
- That gives 135 + 225 + 135 + 135 + 90 + 90 + 90 = 9.0.
- No structural change is needed. The hook, the measured failure, the visual insight that becomes the formula, the sourced payoff and the landing that re-sees the opening are all in place and correct.

## KEEP

1. The **pour**: the cost skyline collapsing into a flat level (4.11, 0.16, 1.67, 1.42). It is the same picture every time and it is the proof.
2. The **persistent context row**: it carries the cold open, Q, TH and the subject's reading, and the Y lands in the ? box in the closing frame (kf_40).
3. **Shannon's real record under a reading cursor** with the green 79 / 102 tally, and the tagged bits-per-character line with LLM at 0.84 (kf_29, kf_37).
