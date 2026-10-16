# Episode 7, review round 2 (craft critic: visual design, motion, A/V sync)

**Evidence.** I used the existing `review/` pack, because metrics.json (15:25) is newer than final.mp4 (15:23). I read:
- report.md, narration_diff.txt and transcript.txt
- all 13 contact sheets
- keyframes kf_03, 05, 07, 10, 13, 16, 17, 18, 20, 24, 25, 26, 27, 30, 31, 32, 35 and 36
- extra ffmpeg frames at 0:00.2, 0:22.5, 0:40.0, 1:05.5 (as 66.0 s), 1:45.5, 1:51.5, 1:56.0, 2:15.5, 2:21.0, 3:19.0 and 3:42.5
- a crop sequence of the formula at 1:32.0, 1:33.0, 1:33.8, 1:34.4, 1:35.0, 1:35.6 and 1:36.4

I also read script.md, narration.txt, facts.md, CHANGELOG.md and round1-craft.md. I recomputed H₁, H(·|Q), H(·|TH), the guess-number entropy and the record tally from data.json. I checked LLMZip's 0.7101 figure against arXiv 2306.04050v2.

```
EPISODE: 007 — "How Much Information Is in a Letter?"
IDEA: A character costs log2(1/p) yes/no questions, so its information depends on how predictable it is; priced with what came before, English needs about one bit per character, not the 4.75 that halving the alphabet suggests.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.5 (847.5/100 = 8.475)   AFTER CEILING: 8.5 (lowest 8 + 2 = 10, not binding)
CAPS: none.
  Considered and not applied: (a) the stale H value in the equation over the after-Q and after-TH skylines (2:17–2:28, 2:29.5–2:38.5). The number is correct for the state it was computed on and is replaced on the pour, so it is a labelling defect, not a factual error. It is fix 1 and it costs Clarity and Visual. (b) The axis-title cross-fade double exposure at 2:21.0 lasts under 1 s and is a transition, so I did not apply the overlap cap.
FINAL: 8.5   PASS: no
FACTS:
- 27 symbols (26 letters + space) | Verified | Shannon 1951 p.56
- 5 halvings take 27→1; on-screen chain 27→13→6→3→2→1 with cuts N|O, U|V, X|Y, Z|␣, Y|Z ending on Y | Verified | frame 0:22.5, arithmetic
- log2 27 ≈ 4.75 | Verified | 4.7549
- Shannon 1951 estimated "about one" bit/char | Verified | BSTJ 30(1) p.50
- No compressor beats the true entropy rate on average | Verified | source-coding theorem
- Next-character guessing is how LMs are trained | Verified | standard autoregressive objective
- 3.75 extra = 79% | Verified | 3.75/4.75 = 0.789
- E ≈ 130× as frequent as Z | Verified | data.json E_over_Z = 130.28 (Brown)
- Space+E+T+A+O ≈ 48% | Verified | data.json top5_share = 0.4834
- E ≈ a tenth, 3.3 doublings | Verified | log2(1/0.1031) = 3.28
- Z is 1 in 1260, needs 10.3 | Verified | one_in_Z = 1263, log2 = 10.30
- p·2^k = 1 ⇒ k = log2(1/p) | Verified | algebra
- Area = average; pour height = Σ p log2(1/p) | Verified | expectation; slabs preserve area
- H(Brown, 27 symbols) = 4.11 bits | Verified | data.json H1 = 4.1111
- "Still four times Shannon's estimate" | Verified | 4.11/1
- After Q, U 98/100; H = 0.16 | Verified | recomputed H(·|Q) = 0.156
- After TH, E 68%, cost ≈ 0.55, H = 1.7 (1.67 on screen) | Verified | recomputed H(·|TH) = 1.667
- Record THERE IS NO REVERSE…THE OTHER DAY, 79/102 first guesses | Verified | Shannon 1951 p.56; data.json tally 79,8,3,2,2,3,1,1,1,1,1 (n=102)
- Guess-number skyline heights (1st 0.37, 2nd 3.67, 3rd/6th 5.09, 4th/5th 5.67, singles 6.67) and pour to 1.42 | Verified | recomputed −Σq log2 q = 1.4223; kf_31 heights match
- Better guesser could only lower it | Verified | Shannon 1951 upper-bound argument (facts #27)
- 0.6–1.3 bits/char at N = 100 | Verified | Shannon 1951 p.64
- LLM 0.71 bits/char on 27-symbol text | Verified | Valmeekam et al. 2023, arXiv:2306.04050v2, Table I, 0.7101 (LLaMA-7B + AC, text8)
- Hidden char is the Y of THE OTHER DAY, guessed first time | Verified | record line 3
MECHANICS: runtime 3:42.8 · wpm 161 (speech) · max silence 1.99 s · max static 3.6 s · −14.1 LUFS / −2.0 dBTP · leading 0.00 s / trailing 1.47 s · 0 banned phrases · WER 1.9 %
FIXES (highest impact first):
1. [2:17–2:28 and 2:29.5–2:38.5][Clarity/Visual] The equation keeps the previous context's answer while the new skyline is shown. "= 4.11 bits" sits over the after-Q skyline (kf_24 2:23.6, frame 2:21.0). "= 0.16 bits" sits over the after-TH skyline and the "share after TH" axis title for about 9 s (kf_26 2:32.5, kf_27 2:37.1). A paused frame reads "H after TH = 0.16", which is false. Fix: at each context change ("What comes after a Q?" 2:13.9 and "After TH" 2:29.3), TransformMatchingTex the right-hand side to "= ? bits", with a yellow "?". After each pour, TransformFromCopy the newborn level label (0.16 at about 2:28, 1.67 at about 2:38.5) into that slot. Optionally leave the previous value as a 30 % ghost in the right gutter so the drop 4.11 → 0.16 / 1.67 stays readable.
2. [1:33.8–1:35.6][Motion/Clarity] The complete `p·2^k = 1` is on screen for only about 0.6 s. It is complete at 1:33.8, and the rearrangement has started by 1:34.4. §5 asks for at least 2 s + 0.4 s per term (about 3.2 s). Mid-transform at 1:35.0 the glyphs pile up into an unreadable "k lo⊕σ p 1". Fix:
   - Add "[pause 1.2]" to the narration after "equals one", and hold the full equation for at least 2.5 s.
   - On "two to the k", Indicate the yellow doublings counters (3.3 and 10.3) so 2^k visibly is the counter.
   - Rearrange in two sequential 1 s moves, not one simultaneous TransformMatchingTex: first k drops out of the exponent along a path_arc while 2 becomes the log base, then p moves under the 1.
   - Keep k YELLOW in `k = log₂(1/p)`. It turns white at 1:35.6 (kf_16, kf_17), which breaks the declared palette (k = questions = yellow).
3. [1:11–1:37][Visual] The doubling-strip panel crowds the chart. The Z strip's bottom edge (y ≈ 413 px) is only about 12 px above the "questions" axis title (top ≈ 428 px, kf_16). That is below the 20 px (0.15 unit) minimum, and the title reads as a third strip row. While the strips are active, fade the axis title to 0 (the chart is already dimmed and unread), or raise the strip group 0.2 units. The context row has 26 px of headroom to the 54 px safe line.
4. [1:39–2:39][Visual] The top band is crammed:
   - The formula's numerator sits about 18 px under the context boxes (box bottom y ≈ 158 px, "1" top ≈ 176 px; kf_17, kf_20, kf_24).
   - Its p descender drops to y ≈ 318 px, level with the "10" tick (323 px), inside the plot's vertical range.
   - Meanwhile 30 % of the plot height above the bars is empty from 1:53 to 2:13 and from 2:27 to 2:39.

   Fix: scale the formula to 0.85 and raise the context row by 0.15 units. Or cap the y-axis at 10.5 and lower the plot top by 0.3 units so the formula clears the 10-tick by at least 0.15 units.
5. [2:21.0 and about 2:30][Visual/Motion] The x-axis title cross-fades as a double exposure: "share of text" and "share after Q" are overlaid in the same box (frame 2:21.0), and "after Q" → "after TH" does the same. Use TransformMatchingStrings, keep "share" in place and swap only the tail ("of text" → "after Q" → "after TH"), with the purple context letters flying in from the context row boxes.
6. [3:11.7–3:18][Motion/Sync] The narration starts on the language model at 3:11.7, but the LLM marker lands only at about 3:18 on "0.71". 3:13.9–3:17.5 is a 3.6 s static stretch in which only the citation changes. Bring the INK marker in on "a language model" (3:12.5) at the 4.75 end and slide it smoothly down the line to 0.71 over the phrase "compressing text…" (about 3 s). The motion then *is* the compression, and the static stretch disappears.
7. [2:52–3:03][Visual] Mini guess skyline (kf_31, kf_32):
   - The "share of guesses" axis has no 0 % / 100 % ticks, so it breaks the §5 rule that every axis carries a scale.
   - The labels "2nd" and "3rd+" sit about 15 px above the axis title.
   - The axis title ends 60 px from the Shannon citation on almost the same baseline, so the bottom-left is crowded.

   Fix: add 0 % and 100 % ticks, move the title down 0.15 units and right-align it to the axis end. Move the citation to the far left at y = −3.1 (it already is); then the title must clear it by at least 0.15 units vertically, or move the mini chart up 0.2.
8. [2:41–2:53][Visual] The record reveal uses only the top 45 % of the frame. The rows run y ≈ 120–480 px, with "first guess" at 545 px, and 350 px of empty frame lies below until 2:53 (kf_30). Centre the record block vertically during the reveal, with its centre at y ≈ +0.5 units, then animate it up by 1.2 units as the mini skyline enters at 2:53. The move then signals "now we compute from this".
9. [2:52.8][Audio] "Treat each guess number as a symbol" comes out as "guess's number" (narration_diff 2:53.4). The sibilant run slurs. Rewrite it as "Treat each guess count as a symbol".
10. [0:00–0:11][Hook] The first frame is 12 blank boxes and a "?" (frame 0:00.2). The tiles arrive only at 0:04–0:07, and "questions per character ?" at 0:09–0:11, so the full puzzle is not on screen until 0:11. Front-load it: tiles in by 0:03 on "one of twenty-six letters, or a space" (already spoken at 0:03–0:06), and the question line by 0:07 on "how many do you need". That gives the viewer 4 s plus the 2 s hold with the whole puzzle to commit on.
11. [3:22.5–3:25.4][Concision] "None of these numbers depends on what the words mean" is a semantic aside. It is backed only by the four markers flashing and does not feed the landing. Cut it, which saves about 3 s and moves the landing's reveal straight after "inside that range". If you keep it, show it: for example, the record dims to 10 % while the markers stay lit.
12. [0:44–0:51][Visual] The translucent yellow overlay mixes with the blue bars into a muddy grey-teal (kf_07), which is neither "probability" blue nor "questions" yellow. Use a 12–15 % yellow fill, or a yellow outline with 45° hatching, so the bars stay blue under it.
13. [0:59–1:50][Visual] Z-order of the baseline: the x-axis line is hidden under the five top-frequency columns, but drawn over all the others. It is visible only from x ≈ 925 px (kf_13, kf_17, frame 1:05.5). After the white-outline flash, call `bring_to_front(x_axis)`, or set the axis z_index above the columns.
REACHES 9 IF ALL FIXED: yes, narrowly. The structure is right and every round-1 cap and structural fix landed: the pour to the level line, guess counts → skyline → 1.42, braces that never cross the line, the band behind the bars, centred open and landing, and fixed record cells. What keeps it from 9 is execution at the seams: a stale answer on screen during both context beats (fix 1), the derivation's key equation held for 0.6 s (fix 2), and spacing and composition in the top band and on the mini chart (fixes 3, 4, 7). With fixes 1–7, Clarity, Visual and Motion reach 9. Fixes 9–11 lift Audio, Hook and Concision. The weighted score then reaches about 9.0, with no structural change needed.
KEEP:
- The pour (1:51–1:55): columns become full-width slabs of equal area and stack to 4.11, the level line is born on top, and the same move repeats for after-Q (0.16) and after-TH (1.67). This is the episode's "picture becomes the number" moment, and it is genuinely 3b1b-grade.
- The "what's still possible" doubling strips with the live yellow counter (1:11–1:27), which feed p·2^k = 1.
- Shannon's own record → first-guess tally → guess-number skyline → 1.42 on the bits-per-character line (2:41–3:11), and the landing: THE OTHER DAY flies into the cold-open row, the Y lands in the "?" box, then "1 guess" sits against the returning 27→1 chain and "5 questions" (3:26–3:41).
```

## Notes behind the scores

- **Hook 8.5.**
  - A concrete question by 0:11, then a 2.0 s prediction hold (0:11.4–0:13.4).
  - The natural "5" becomes the ideal 4.75, then Shannon's "about one" lands at 0:33. The stakes (compressors, LMs) are now paid off at 3:12 with the LLMZip marker, and the ending resolves the hidden character exactly.
  - Held below 9 because the first frame is abstract (blank boxes) and the full puzzle is not assembled until 0:11 (fix 10).
- **Clarity 8.5.**
  - log₂(1/p) is derived from a picture (the doubling strips), area = average is shown by the pour, and guess counts → bits is now visible. A viewer could re-derive most of it.
  - Deductions: the stale H values contradict the displayed skyline for about 9 s twice (fix 1), and the pivotal `p·2^k = 1` is readable for about 0.6 s (fix 2).
- **Visual 8.**
  - The palette is semantic and mostly held (blue p, yellow questions/bits, green Shannon, purple context, grey ghosts), and citations sit correctly. Round-1 problems are gone: the H line through 68 %, the opaque band and the record collisions (kf_30 is clean).
  - Remaining issues, more than the two minor ones allowed at 8:
    - spacing under 20 px between the strips and the axis title (kf_16) and on the mini chart (kf_31)
    - a crammed top band against an empty plot (kf_20, kf_27)
    - k changing colour
    - the title double exposure at 2:21
    - the muddy overlay (kf_07)
    - the baseline z-order
- **Motion 8.5.**
  - Objects persist and transform with meaning: tiles → columns (0:29–0:33), widths → probabilities (0:53–0:57), heights → log₂(1/p) (1:38–1:41), the pour, the stack rising back during the Q pause (2:15.5), U widening then flattening, guess counts flying into the skyline (2:53–2:57), 1.42 flying to the number line (3:05), and the record phrase flying into the cold-open row (3:27–3:31).
  - The only hard cut (2:39 → 2:41) is at a beat boundary. Deductions: equation hold and glyph pile-up (fix 2), the 3.6 s static LLM beat (fix 6) and the cross-fade (fix 5).
- **Audio 8.5.**
  - 161 wpm, −14.1 LUFS, −2.0 dBTP, max silence 1.99 s, trailing 1.47 s.
  - Deictics land within about 1 s:
    - "where do 4 of every 5" → overlay at 0:44.5
    - "Z costs as much as E" → isolation by 0:53
    - "U swallows the bar" → widening at 2:21
    - "pours flat" → pour at 2:57
    - "the Y at the end of the other day" → phrase fly-in at 3:27–3:29
  - Deduction: the "guess's number" slur (fix 9) and a slightly breathless 1:45–1:57 run (three sentences with 0.4–0.5 s gaps). "Q" is correctly voiced as "cue".
- **Concision 8.5.** 583 words in 3:43, almost all load-bearing. The one slack sentence is "None of these numbers depends on what the words mean" (fix 11).
- **Originality 9.** The hidden Y, isolated by the halving chain in the cold open and then guessed first time in Shannon's own 1951 record, is a memorable frame for entropy. The doubling strip and the pour are fresh, exact visual arguments.
