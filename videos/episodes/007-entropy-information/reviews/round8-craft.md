# Round 8 review: craft (visual design, motion, A/V sync)

Critic: independent. My emphasis is visual design, motion craft and audio/visual sync, but I scored every dimension.

Evidence:
- I reused the `review/` pack, because metrics.json (19:14) is newer than final.mp4 (19:12).
- From it I read report.md, all 12 contact sheets, transcript.txt plus the word timings around 1:40–1:53 and 1:01–1:06, narration.txt, narration.json (beat starts, gaps and speeds), script.md, facts.md and CHANGELOG.md (round 7).
- Full-resolution keyframes read: kf_01, 04, 07, 09, 13, 15, 18, 20, 22, 24, 27, 29, 31, 32, 37, 40.
- Motion strips I extracted at 4 fps into /tmp/r8c: 0:51.5–0:55.5, 1:02.5–1:06.5 (Z counter, cropped), 1:16–1:20, 2:07.5–2:11.5, 2:58–3:02 and 3:18.5–3:22.5. I also took a 3 fps strip at 2:47–2:53 (the count flight).
- I re-checked LLMZip (arXiv 2306.04050v2, §IV) by web search: 0.8426 bits/character on the post-training Gutenberg book. I recomputed the key arithmetic from data.json.

```
EPISODE: 007 — "How Much Information Is in a Letter?"
IDEA: A character costs log2(1/p) yes/no questions, so the average (entropy) is the area of a skyline with width = probability and height = cost, poured flat, and it falls from 4.75 to about 1 bit as the guesser uses more of what came before.
SCORES: Hook 9 · Clarity 9 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 9 · Originality 9
WEIGHTED: 8.8   AFTER CEILING: 8.8 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none
FINAL: 8.8   PASS: no
```

## FACTS

| Claim | Status | Source / check |
|---|---|---|
| 27 symbols; five cuts 27→13→6→3→2→1 | Verified | arithmetic; the cut positions in kf_04 end on Y |
| log2 27 ≈ 4.75 | Verified | 4.7549 |
| Shannon 1951: "about one"; 0.6–1.3 bits with 100 letters of context | Verified | Shannon 1951, BSTJ 30(1), p. 50 and the p. 64 table (facts.md) |
| 3.75 extra (79%), "four of every five questions" | Verified | 3.75 / 4.755 = 0.789 |
| E 10.3%, Z 0.08%, ×130; Z "1 in 1260" needs 10.3 | Verified | data.json: E/Z = 130.3, 1/pZ = 1263 (1260 at 3 s.f.), log2 = 10.30 |
| Space, E, T, A, O ≈ 48% ("nearly half") | Verified | top5_share 0.4834 |
| E: 3.3 doublings | Verified | log2(1/0.1031) = 3.28 |
| p·2^k = 1 ⇒ k = log2(1/p); average = Σ p log2(1/p) | Verified | re-derived |
| H = 4.11 bits (Brown, 27 symbols) | Verified (corpus) | data.json H1 = 4.1111 |
| "four times Shannon's estimate" | Verified | 4.11 / ≈1 |
| After Q: U 98%, 0.16 bits | Verified (corpus) | facts.md / data.json after_Q |
| After TH: E 68%, about half a question, 1.67 ("1.7") | Verified (corpus) | 0.683 → 0.55 bits; H = 1.667 |
| Run E ␣ O: 0.5 + 0.6 + 3.8 = 4.9 → 5; one at a time 1 + 1 + 4 = 6 | Verified | run_after_TH |
| Average over all two-letter contexts 2.81 | Verified (corpus) | H_given_2_prev = 2.8105 |
| 27² = 729; 27¹⁰⁰ ≈ 10¹⁴³; Brown 5.75 M characters | Verified | 100·log10 27 = 143.1 |
| 79 of 102 first guesses; the record | Verified | Shannon p. 56 (facts.md, prior rounds' recount) |
| Guess-number entropy ≈ 1.42 (upper estimate); log2(1/q) = 3.67 | Verified | log2(102/8) = 3.672; 1.4223 (facts.md 26) |
| "A twin could rebuild the passage from these counts" | Verified | Shannon 1951, identical-twin argument |
| LLMZip 2023: 0.84 bits/char on a book posted to Gutenberg after training | Verified | arXiv 2306.04050v2 §IV / Table IV: 0.8426 (web search this round) |

## MECHANICS

| Measure | Value |
|---|---|
| Runtime | 3:34.3 |
| Pace | 152 wpm over speech time (144 overall); 499 narration words |
| Longest internal silence | 2.07 s at 1:48.6, the planned Q prediction hold |
| Lead / trail | 0.00 s / 0.83 s |
| Longest static stretch | 3.3 s (the closing hold) |
| Loudness | −14.1 LUFS / −1.8 dBTP |
| Other | WER 1.0 %; 0 black frames; 0 banned phrases; layout audit 0 issues; 0 glyph morphs flagged |

Narration notes:
- The whisper segment at 1:39.4–1:53.6 is a segmentation artefact. The word timings show "beats 4.75, but it's four times Shannon's estimate" intact.
- Beat-level pace from narration.json:
  - "The widths add to one, so the area is the average cost. Pour the skyline flat…" (1:23.4) runs at **178 wpm**, the fastest ordinary beat, on the episode's central idea.
  - "After TH, E takes two thirds…" (1:59.2) and "A better guesser could only lower it" (2:55.8) both run at 183 wpm.
- All 26 beat gaps are 0.42–0.46 s, including the act turn "…what came before. / What comes after a Q?". There, ffmpeg silencedetect measures only 0.56 s of silence (1:46.7–1:47.3).

## What I saw (flipbook)

- **0:00–0:22.** Frame one is the context row, the ? box and the 27 tiles (kf_01). The question is complete by 0:07.5, followed by a 1.9 s silent hold. Cuts, chain and `log2 27 ≈ 4.75` are built in place (kf_04, clean).
- **0:22–0:52.** The tiles become column feet, rise to 4.75, then the ≈1 band and the Shannon citation appear. The hatched "3.75 extra (79%)" follows. E and Z are isolated with real widths and ×130 (kf_07). The re-sort leads to the 48% brace. Everything lands on its words.
- **0:52–1:21.** Doubling strips (kf_09):
  - E's strip runs to 3.3, then Z's to 10.3.
  - The equation is built from E's column and the counter (kf_13), and the algebra steps land on their words.
  - The Z counter lags its spoken number: see defect 6.
- **1:21–1:47.** Heights morph to log2(1/p), the ×28 inset appears, and the formula is assembled (kf_15). Then the pour: a 4.11 level, average → H, "bits". The live meter goes 3.75 → 3.11 (kf_18). This is still the best passage in the series.
- **1:47–2:25.**
  - Q turns purple and the formula reads "= ? bits" (kf_20). U swallows the bar and the level pours to 0.16.
  - The TH skyline and its 68% brace follow, with E outlined at half a question (kf_22).
  - The run box widens into E ␣ O, and the bill appears with its context tags. The bracket slides TH → HE → E␣ (strip 2:07.5).
  - 1.67, then 2.81 with 1.81 extra.
- **2:25–2:47.** The contexts arithmetic appears alone (kf_27, one focal point). Shannon's record is revealed under a cursor, with the green tally running to 79/102 (kf_29, excellent).
- **2:47–2:58.**
  - The letters leave and the counts sort into their lanes. Nothing crosses a resting row (strip 2:47).
  - The guess skyline rises, then 3.67 appears on a leader (kf_31). It pours to ≈ 1.42 with the band over it and a context note (kf_32), then the 0.42 meter and "upper estimate".
- **2:58–3:18.** The bits-per-character line. The LLM marker is born from 1.42 and drops to 0.84 inside the band (kf_37).
- **3:18–3:34.** The line fades and the record returns. THE OTHER DA rises into the boxes, Y lands in the ? box, and frame one comes back with "1 guess" against "5 questions" (kf_40).

Colour semantics hold: blue is probability, yellow questions/bits, green Shannon's measurements, purple context, grey abandoned or reference. No slide-like frame appears. Every round-7 craft fix landed: the count flight, the label gaps, the centred chart, the live meter labels, the handover and the slower landing.

## Defects found (evidence)

1. **2:58.75–2:59.25, the payoff line appears whole in about 0.5 s (Motion).**
   - In strip 2:58.0, frame 5 (2:59.0) shows the axis stub and every marker and tag at about 15 %, and frame 6 (2:59.25) shows all of it complete.
   - That is roughly 12 text items born at once in under 0.5 s: the axis, ticks 0–5, the 4.75/4.11/2.81 values and triangles, four tags and the axis title. Only 1.42 travels.
   - This is the one diagram in the episode that is announced rather than built. It is also the summary of the whole argument.
2. **3:00.0, wrong referent (A/V sync).** On "With a hundred letters of context", the **2.81 "2-letter context"** triangle flashes white (strip 2:58.0, row 3, frame 1). The thing the sentence names is the 0.6–1.3 band, and the band is not drawn until 3:03 ("between point six and…", sheet 11).
3. **2:09.2–2:19.0, the run bill sits inside an empty chart (Visual).**
   - kf_24 shows the bill (letters, context tags, costs, sums) laid over the plotting area.
   - Behind it, the y ticks 10 and 5, the axis, the ≈1 band, the dashed 4.11 line, the 0–100 % ticks, "share after TH" and the Brown citation all stay at full strength, although nothing is plotted on them.
   - The arithmetic reads as if it were data on those axes. That is a second, empty focal structure.
4. **1:23.4–1:30.8, the crux is the fastest beat (Audio / Clarity).** "The widths add to one, so the area is the average cost. Pour the skyline flat, and its height is that average" runs at 178 wpm. The visual work in those 7 s is dense: the blue sweep, the ×28 inset, the formula assembled from referents, and the pour. This is the one transition a first-time viewer would rewind.
5. **Uniform beat gaps (Audio).** Every beat boundary in narration.json is 0.42–0.46 s. The biggest turn in the argument, "…ignores what came before. / What comes after a Q?" at 1:46.8, gets 0.56 s of silence, the same as an ordinary sentence. The landing turn at 3:18.6 gets 0.44 s.
6. **1:03.5–1:06.0, the Z counter lags its spoken number (A/V sync).** "ten point three" is spoken at 64.06–65.14 s. The counter reads 0.0 at 63.5, 2.4 at 64.0, 7.6 at 65.0 and 10.3 at 65.75 (cropped strip 1:02.5). The number is said about 1.7 s before it is shown, and the 1/1260 label fades out as the count starts.
7. **1:16.9–1:18.3, the "2" travels through the k and the "=" (Motion).** In the `2^k = 1/p → k = log2(1/p)` step (strip 1:16.0, frames 5–7), the 2 sits on top of the k, then on the "=" (one frame shows a fragment glyph), while "log" is half-written. The idea is right (the base travels to its subscript), but its path collides with other glyphs for about 0.75 s.
8. **3:09–3:19, word load (Visual).**
   - The note "1924 book · on Gutenberg May 2023 · 27 symbols" is 8 words in one block (the §5 limit is 7).
   - kf_37 also carries LLM, person, 102 letters, 2-letter context, no context, halving and bits per character, about 20 words of labels.
   - Everything is legible, but it is the densest frame in the episode.
9. **2:51–2:59, guess-chart composition (Visual, minor).**
   - In kf_31 the top 28 % of the frame is empty after the record leaves, and the chart is left of centre (axis spans x ≈ 340–1420 px, centre 880 px).
   - The 3rd+ columns rise to 5.1–6.7 bits above the top tick "5", with no tick to read them against.
10. **2:21–2:31 and 2:55–2:58, teal blend (Visual, nitpick).** The 30 % green band fill over the blue stack renders teal (kf_27, kf_32). A seventh apparent hue then sits in the middle of a bar stack and can read as a different category.
11. **3:18.5–3:19.0, a brief two-layer frame (Motion, nitpick).** The record ghost (about 20 %) fades in under the payoff line while the line is still at full strength (strip 3:18.5, frames 1–2). The changelog says the record comes back "only then".

## FIXES (highest impact first)

1. **[2:58.6–3:01.0][Motion] Build the payoff line instead of fading it in.**
   - Grow the axis left to right, 0 → 5, over 0.8 s.
   - Then drop the markers in story order, each with its value and tag and lag_ratio 0.35 at 0.5 s per marker: 4.75 "halving", 4.11 "no context", 2.81 "2-letter context".
   - Then fly the 1.42 in last, as now. The whole build fits 2:58.8–3:01.0. Fade the axis title in only after the last tag.
2. **[2:59.6–3:05.5][A/V sync] Put "a hundred letters of context" on the band.**
   - Remove the 2.81 flash.
   - On "hundred letters of context", grow the green band outward from 1.0 to 0.6–1.3. Write "0.6–1.3" on "point six and one point three".
   - If a contrast with the 2-letter marker is wanted, dim 2.81 to 40 % at the same moment rather than flashing it.
3. **[2:09.2–2:16.3][Visual] Step the empty chart back while the bill is up.**
   - Fade the axes, ticks, ≈1 band, 4.11 line, "share after TH" and the Brown citation to 25 % when the after-TH skyline leaves (2:09.2).
   - Bring them back to full strength on "After TH" (2:16.3), when the TH skyline returns to pour.
   - Alternative: lift the bill clear of the axes (top of bill at y ≈ 2.4, chart compressed below), so it never sits between the tick labels.
4. **[1:23.4–1:30.8][Audio] Slow the crux.**
   - Run this beat at speed 0.78 and add `[pause 0.6]` after "the area is the average cost."
   - Keep the pour cue on "Pour".
   - This costs about 1.2 s, which keeps runtime ≤ 3:36.
5. **[1:46.8, 2:25.1, 3:18.6][Audio] Shape the act turns.** Set the beat gap to 0.9 s at the three act boundaries: no context → context, two-letter → person, payoff → landing. Keep 0.44 s elsewhere. Take the 1.4 s from `BEAT_GAP` 0.44 → 0.40 on the other 23 boundaries, or accept a 3:36 runtime.
6. **[1:01.4–1:05.1][Motion/sync] Land Z's 10.3 on its word.**
   - Start the Z doubling run on "twelve" (≈ 62.3 s) with run_time 2.6 s, so the counter reaches 10.3 as "ten point three" begins (64.1 s).
   - Keep the "1/1260" label until the counter passes 1.0.
7. **[1:16.9–1:18.3][Motion] Route the travelling 2.**
   - In the TransformMatchingTex to `k = log2(1/p)`, give the "2" `path_arc ≈ −1.2` so it dips under the "=" into the subscript slot.
   - Write "log" only after the 2 lands (0.3 s later).
   - Nothing then overlaps mid-flight.
8. **[3:09–3:19][Visual] Trim the payoff frame's words.**
   - Shorten the note to "1924 book · Gutenberg, May 2023" (5 words) and move "27 symbols" to the citation line ("… Table IV · 27 symbols").
   - Dim "bits per character" to 40 % once the first marker lands.
9. **[2:51–2:59][Visual] Recentre and tick the guess chart.**
   - Shift the chart right by 0.6 units and up by 0.5 so the axis centre is at x ≈ 0.
   - Give the pre-pour axis ticks 0, 2, 4, 6, so the 3rd+ heights (5.1–6.7) can be read.
10. **[2:21–2:31, 2:55–2:58][Visual] Draw the ≈1 band over a stack without mixing colour.** Use the two green edge lines plus a 10 % fill, or keep the band behind a stack at 85 % opacity. The overlap then reads as green lines on blue, not as teal bars.
11. **[3:18.5–3:19.3][Motion] Delay the record's return by 0.4 s,** until the payoff line is below 30 %. Only the 1.42 marker then overlaps it, as intended.

## REACHES 9 IF ALL FIXED: yes

- Fixes 1, 3, 7, 8 and 11 lift Motion and Visual to 9. They cover the last place where a diagram is announced rather than built, and the last frames with a second, empty focal structure or an over-long block.
- Fixes 2 and 4–6 lift Audio to 9. Every spoken referent is then visible as it is named, the crux breathes, and the act turns are audibly longer than sentence breaks.
- That gives 135 + 225 + 135 + 135 + 90 + 90 + 90 = 9.0.
- No structural change is needed. The hook, the measured failure (3.75 extra), the picture that becomes the formula (the doubling strips leading to the skyline and the pour), the sourced payoff and the landing that re-sees frame one are all in place and correct.

## KEEP

1. **The pour.** The cost skyline collapses into a flat level (4.11, 0.16, 1.67, 1.42). It is the same picture every time, and it is the proof.
2. **The persistent context row.** It carries the cold open, Q, TH, the run box and the subject's reading, and the Y lands in the ? box in the closing frame (kf_40).
3. **Shannon's real record under a reading cursor** with the green 79/102 tally (kf_29), and the live gap meter that re-measures the opening failure at every level.
