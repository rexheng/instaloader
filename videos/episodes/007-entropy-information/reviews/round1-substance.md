# Episode 7, review round 1 (substance: science and story editor; all dimensions scored)

Note: this replaces an earlier round-1 file at this path, which reviewed an older cut. This review covers final.mp4 dated 2026-10-15 23:26.

**Evidence**
- I reused the existing `review/` pack because metrics.json (23:28) is newer than final.mp4 (23:26).
- I read report.md, narration_diff.txt, transcript.txt, the transcript_words.tsv timings for 1:58–2:14, and all 13 contact sheets.
- Full-resolution keyframes: kf_01, 03, 05, 07, 10, 15, 17, 20, 23, 28, 30, 33 and 40.
- Extra ffmpeg frames: 0:08.8, 1:29.0, 1:48.0, 2:25.5, 3:29.0, 3:36.5 and 3:40.0, plus a 0.1 s strip of the citation swap at 3:28.2–3:30.0.
- Documents: script.md, narration.txt, facts.md, data.json, and the CHANGELOG tail.

**Independent recomputation.** I downloaded the NLTK Brown corpus into my scratchpad and recounted it with my own script (not `data.py`), reduced to 27 symbols:
- n = 5,751,046 (data.json says 5,751,047, an off-by-one trailing space that changes nothing); 1,005,119 words
- H₁ = 4.1111; p(E) = 10.314 %; p(Z) = 0.0792 %; E/Z = 130.3; 1/p(Z) = 1263; log₂(1/p(Z)) = 10.30; log₂(1/p(E)) = 3.277
- top five (space, E, T, A, O) = 48.34 %
- H(X | 1 prev) = 3.381; H(X | 2 prev) = 2.8105
- after Q: n = 5,103, U = 98.14 %, cost 0.027, H = 0.156
- after TH: n = 134,673, E = 68.33 %, cost 0.549, H = 1.667
- inset heights: X 9.25, J 9.53, Q 10.14, Z 10.30

From Shannon's record:
- tally 79/8/3/2/2 and 8 above five
- plug-in entropy of the guess counts = 1.4223
- mean = 1.94 guesses per symbol

Arithmetic: log₂27 = 4.755; 3.75/4.75 = 78.9 %; 27¹⁰ ≈ 2.1 × 10¹⁴.

On-screen geometry, measured in pixels: space column 2.51 and E 3.26 (kf_15); the guess-skyline's 2nd-guess bar 3.65 vs 3.67 computed (kf_33). The ≈1 band spans 0.6–1.3 (kf_07).

**Citation checks (web)**
- LLMZip arXiv HTML v2: "The compression ratio for LLaMA with arithmetic coding is only 0.8426 bits/character". Table IV row M = 511 gives ρ_LLaMA+AC = 0.8426. Ref [7] is "Texas Folk-Lore Society, 1924; Project Gutenberg, May 25, 2023". The preprocessing "contained only lowercase …" letters and space (text8 style).
- Shannon 1951, Princeton mirror:
  - "the long range statistical effects (up to 100 letters) reduce the entropy to something of the order of one bit per letter"
  - "Out of 102 symbols the subject guessed right on the first guess 79 times"
  - the identical-twin passage
  - "If he is wrong, he is told so and asked to guess again"
  - 27-letter F₀–F₃ = 4.76 / 4.03 / 3.32 / 3.1

```
EPISODE: 007 — "How Much Information Is in a Letter?"
IDEA: A character costs log₂(1/p) yes/no questions, so its information depends on how
      predictable it is in context, not on the size of the alphabet; English drops from
      4.75 (halving) to 4.11 (frequencies) to ~1 bit (long context).
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.6 (127.5+212.5+127.5+127.5+85+85+90 = 855/100 = 8.55)   AFTER CEILING: 8.6 (8.5+2 = 10.5, not binding)
CAPS: none
FINAL: 8.6   PASS: no
```

**Why no caps**
- I found no wrong number, spoken or drawn.
- Every empirical claim has an on-screen citation: Shannon at 0:31–0:53 and 2:55–3:28, Brown at 0:51–2:53, LLMZip at 3:29–3:37 (held more than 3 s).
- The transcript has 0 banned phrases and no rhetorical-question chains.
- Mechanics are all inside the bar.
- The ending reframes the cold open rather than recapping.
- The two transient superimpositions (citations at 3:28.8–3:29.2, axis ticks at 2:25.5) last ≤ 0.5 s mid-transition. I treat them as fix items, not the overlap cap.

## FACTS

| Claim | Verdict | Source / check |
|---|---|---|
| 27 symbols (26 letters + space) | Verified | Shannon 1951 p. 56; on screen 0:00 |
| Halving: 27→13→6→3→2→1, five cuts | Verified | 2⁴ < 27 ≤ 2⁵ |
| "log base two of 27, about 4.75" (ideal) | Verified | 4.7549; Shannon F₀ = 4.76 |
| Shannon 1951 estimated "about one" | Verified | "of the order of one bit per letter" (BSTJ 30:50) |
| No compressor can beat the true figure on average | Verified | source-coding theorem (stated about the true rate, not the estimate) |
| Next-character guessing is how LMs are trained | Verified | standard next-token objective; LLMZip §I |
| "four of every five questions" / "3.75 extra (79%)" | Verified | 3.75/4.75 = 0.789 |
| E 130× as often as Z; 10.3 %, 0.08 % | Verified | my Brown recount: 130.3 |
| Space, E, T, A, O ≈ half (48 %) | Verified | 48.34 % |
| E ≈ a tenth; 3.3 doublings | Verified | log₂(1/0.1031) = 3.277 |
| Z 1 in 1,260, needs 10.3 | Verified | 1/p = 1263 (3 s.f.); 10.30 |
| p·2ᵏ = 1 ⇒ k = log₂(1/p) | Verified | re-derived; two legal steps shown |
| Area of the skyline = average; pour = Σ p log₂(1/p) | Verified | definition of expectation |
| H for English letters = 4.11 | Verified | Brown 4.1111 (Shannon's older table: 4.03), labelled Brown on screen |
| "four times Shannon's estimate" | Verified | 4.11 / ~1 |
| After Q: U 98 %, cost ≈ 0, average 0.16 | Verified | 98.14 %, 0.027, 0.156 |
| After TH: E two-thirds (68 %), ≈ half a question, average 1.7 | Verified | 68.33 %, 0.549, 1.667 |
| Fractions of a question are achievable by coding runs | Verified | block/arithmetic coding (Shannon 1948 §9; LLMZip uses AC) |
| All two-letter contexts: 2.8 | Verified | 2.8105 (my recount) |
| Subject guessed until right; 79 of 102 first guesses | Verified | Shannon 1951 pp. 55–56 (quoted above) |
| Identical twin can rebuild the text from the counts | Verified | Shannon 1951 p. 55 |
| Guess-count skyline pours to ≈ 1.4 bits | Verified | 1.4223 (my calculation from the record) |
| "A better guesser could only lower it" | Verified (in expectation) | majorisation + Schur-concavity of entropy; for one 102-symbol passage it is an expectation claim |
| With 100 letters of context, 0.6–1.3 bits | Verified | Shannon 1951 Fig. 4 / table at N = 100 |
| 2023 LM: 0.84 bits on the same 27 symbols, inside the range | Verified | LLMZip Table IV, M = 511: 0.8426 |
| "part of a **new** book" | Misleading (not counted as an error) | The book is J. F. Dobie, *Legends of Texas*, **1924**. Only its Gutenberg release (25 May 2023) is new. The authors' own wording is "recently released / recently published", but a viewer will hear "newly written". |
| Hidden character = Y of THE OTHER DAY, 1 guess | Verified | record line 3, count 1 |
| "Splitting the alphabet took five" | Verified | the chain on screen ends on Y at cut 5 |

MECHANICS: runtime 3:54.6 · wpm 160 (speech time; 156 overall) · max internal silence 1.96 s · lead 0.00 s / trail 1.24 s · max static 3.63 s (closing hold) · −14.0 LUFS / −1.9 dBTP · WER 2.0 % (only homophones: cue/Q, you/U, why/Y, pores/pours)

## What the scores rest on

- **Hook 8.5.**
  - For: the frame-one puzzle (hidden yellow ?, 27 tiles, "26 letters + space") is on screen at 0:00, the question ends at 0:08.5 with a 1.9 s hold (0:08.3–0:10.2), and "the natural answer is five" is voiced as the reasonable belief. Shannon's "about one" at 0:26 then creates a measured 79 % gap ("3.75 extra", 0:41), and the landing (3:40–3:54) resolves the exact opening frame: Y in the box, 1 guess vs 5.
  - Against: the opening says "You've read this English sentence", but the sentence is 12 unreadable boxes, so the deictic points at nothing (kf_01). The tension sags from 1:05 to 2:04. For 60 s of derivation the ≈1 target is dimmed to 30–40 % (kf_10, 1:07–1:37) and no gap is measured. The failure metric from 0:41 never comes back as a live number, so the viewer never watches the gap shrink (4.75 → 4.11 → 2.81 → ~1).
- **Clarity 8.5.**
  - For: concrete before abstract throughout. E and Z as real columns come first; the doubling strip with a live counter turns into p·2ᵏ = 1 and then k = log₂(1/p), one clause per step; area = average; the pour gives 4.11. Every number checks out, and the assumptions are stated ("ideal", runs of letters, the twin).
  - Against:
    1. 2:50–2:55 never says *why* Shannon switches from counting to a person. Counting longer contexts runs out of text (27¹⁰ ≈ 2×10¹⁴ contexts vs 5.75 M characters), which is the hinge of the payoff, and the viewer has to supply it.
    2. "part of a new book" (3:29) misdescribes a 1924 book.
    3. "Three point three doublings" (1:14) is the first fractional question, but the justification arrives 80 s later (2:34).
    4. At 2:18.6–2:21.0, U widens to 98 % while still at its unconditional height (≈5.4, sheet 8 at 2:19–2:23). The skyline's area visibly balloons just as the narration says the cost is collapsing.
    5. "Here they average one point seven" (2:42): "they" has no clear referent.
- **Visual 8.5.**
  - For: a semantic palette that holds (blue = probability, yellow = questions/bits, green = Shannon, purple = context), labelled axes with units, ≤ 4 hues per frame, a clean inset with a ×28 label (1:45), and real data.
  - Against:
    - At 3:28.8–3:29.2 the two citations superimpose and are unreadable (extracted strip).
    - At 2:25.5, mid-zoom, the ticks "10", "5" and "4" coexist with non-linear spacing.
    - On the final bits line (3:21–3:37), 2.81 is grey while 4.11 and 1.42 are yellow, although 2.81 is the same Σ p log₂(1/p) quantity. The palette meaning wobbles at the payoff.
    - The record frames (2:55–3:37) carry about 100 cells of letters plus digits, and the top 45 % of the frame sits dimmed for 26 s while the bits line works below it.
    - The "≈1" label sits at the band's top edge (≈1.25), not its middle (kf_07).
- **Motion 8.5.**
  - For: the tiles become chart columns, the columns re-sort without gaps, E's column becomes the strip, p and 2ᵏ come from their referents, and the pours reuse one visual mechanism three times. THE OTHER DAY flies back into the cold-open row.
  - Against:
    - Glyph-scramble morphs between unlike strings: "k"→"average" at 1:48 and the axis title "questions"→"bits" at 1:59 (sheet 7).
    - The chart→record change at 2:52–2:55 is a dissolve; nothing carries over.
    - The U width-then-height order at 2:18–2:22 (above).
- **Audio 8.5.**
  - For: 160 wpm, −14.0 LUFS, no clipping, deictics land within ±1 s ("Z costs as much as E" at 0:47.7 with E and Z isolated at 0:49; Q appears at 2:15 on "after a Q"; the tally reaches 79 on "seventy-nine" at 3:00).
  - Against, as the word timings show: "That" is stretched to 1.04 s (2:04.1–2:05.2) right after a compressed "four point one one" (0.74 s, 2:03.4). That reads as an odd, synthetic emphasis on the episode's key number.
- **Concision 8.5.** Fewer than 10 % of lines are removable, but the runtime of 3:54.6 sits 5 s under the hard limit and is 54 s over the §6 template. Candidates: "Common characters sit wide and low, rare ones narrow and tall" (1:41–1:45) describes what the skyline already shows. "Shannon measured this with a person, who read a passage one character at a time, guessing each next one until right" (2:52–3:00) could be tighter.
- **Originality 9.** Several elements are non-obvious and memorable: the doubling strip, the pour, Shannon's own motorcycle record and guess skyline, and the cold-open character turning out to be the Y in THE OTHER DAY. There is no slop. I found no banned phrase or pattern, and "sounds impossible" is earned by the run-of-letters picture.

## FIXES (highest impact first)

1. **[2:50–2:55][Clarity + Hook] Missing reason for the human experiment.**
   - Insert after "it's still two point eight": "Longer contexts need more text than any corpus holds, so Shannon used a predictor that already knows English: a person." (≈ 8 s)
   - On screen, beside the 2.81 level, a grey counter "contexts: 27² = 729 → 27¹⁰ ≈ 2×10¹⁴" next to "Brown: 5.75 M characters". Then cross-fade to the record.
   - This closes the one logical gap in the payoff.
2. **[3:27–3:37][Clarity/correctness] Correct "new book".**
   - Narration: "In twenty twenty-three, a language model compressing part of a book first put online after it was trained, in the same twenty-seven symbols, needed point eight four bits."
   - Add a small grey note under the LLM marker: "1924 book, online May 2023".
   - facts.md #30 already has the details.
3. **[0:41 → 2:05 → 2:47 → 3:35][Hook + Motion] Bring the failure metric back as a live gap.**
   - Keep a small yellow double arrow plus a DecimalNumber "extra" between the current level and Shannon's ≈1, the same reference that 0:41 uses.
   - Its values: 3.75 at 0:41, 3.11 when the pour lands at 4.11 (2:03), 1.81 at 2.81 (2:52), and 0.42 at 1.42 (3:16).
   - Keep the green band at full strength while the arrow is shown.
   - This removes the 1:05–2:04 sag and makes "measure, don't adjectivize" literal.
4. **[2:18.6–2:22][Clarity + Motion] U balloons before it collapses.** Animate U's height from 5.44 to 0.027 *during* the widening, on "U swallows the bar", with the 98 % brace parked at a fixed y above. Keep "its cost drops to almost nothing" on the flattened column, with a white outline flash.
5. **[3:28.8–3:29.2][Visual] Citations superimpose.** Use `Succession(FadeOut(shannon_cite, run_time=0.3), FadeIn(llmzip_cite, run_time=0.3))` so the two never coexist.
6. **[2:25.3–2:26.0][Visual] Ticks collide mid-zoom.** Fade the 0–11 ticks out completely (0.3 s), rescale the axis, then fade in 0, 2 and 4. Apply the same to the zoom-out at ≈2:29 and the zoom-in at ≈2:42.
7. **[3:21–3:37][Visual] Palette inconsistency on the bits line.** Draw 2.81 in yellow like 4.11 and 1.42, because all three are Σ p log₂(1/p) estimates. Keep grey only for 4.75, the abandoned halving price. Also recolour the 2.81 dashed level at 2:47–2:53 yellow at 60 %, or explicitly declare grey = "reference" in the palette and use it for 4.11 as well on the final line.
8. **[1:14][Clarity] Fractions arrive before they are justified.**
   - Say "Three point three *ideal* doublings".
   - At 2:34 tie back: "Half a question, like three point three doublings, sounds impossible, but a compressor asks about long runs of letters…"
9. **[2:03–2:05][Audio] Rushed key number, then a stretched "That".**
   - Re-synthesize "For English letters, it's four point one one." with a 0.3 s pause before the number.
   - Re-synthesize "That beats four point seven five" as one phrase so "That" is not held for 1 s.
   - Re-check the word timings: aim for "four point one one" ≥ 1.0 s and "That" ≤ 0.35 s.
10. **[1:41–1:45, 2:52–3:00][Concision] Pay for fix 1 and keep ≤ 3:58.**
    - Cut "Common characters sit wide and low, rare ones narrow and tall" (≈ 3.9 s). Trigger the inset on "the widths add up" instead.
    - Tighten "Shannon measured this with a person, who read a passage one character at a time, guessing each next one until right" to "His subject read a passage letter by letter, guessing each next one until right" (≈ −2 s).
11. **[2:42][Clarity] "Here they average one point seven"** → "After TH, the average is one point seven."
12. **[1:48, 1:59][Motion] Glyph-scramble morphs.** Use `FadeTransform` (or a cross-fade in place) between unlike strings ("k"→"average", "questions"→"bits"), and keep `TransformMatchingTex` only where tokens match.
13. **[0:00–0:04][Hook, nitpick] "this English sentence" points at blank boxes.** Change it to "You've read an English sentence up to one hidden character", or keep the letters' 9 % glint for the whole first sentence (≈ 3.5 s) instead of 0.6 s, so "this" has a referent.
14. **[0:31–0:53][Visual, nitpick]** Centre "≈1" on the band (y = 0.95), not on its top edge.

**REACHES 9 IF ALL FIXED: yes, narrowly.**
- Fixes 1–4 and 8 lift Clarity and Hook to 9. Fixes 3–7 and 12 lift Visual and Motion to 9. Fix 10 lifts Concision to 9.
- That gives (15×9 + 25×9 + 15×9 + 15×9 + 10×8.5 + 10×9 + 10×9)/100 = 8.95 → 9.0 even with Audio at 8.5.
- No structural change is needed: the misconception, the measured failure, the one-picture insight, the sourced payoff and the reframing landing are all in place.

**KEEP**
- The doubling strip with its live counter, turning clause by clause into p·2ᵏ = 1 → k = log₂(1/p), and the skyline-pour that makes "average" an area (1:05–2:05). It is the canonical picture for this idea.
- Reusing the pour for after-Q and after-TH with the "= ? bits" slot, and the honest 2.81 "all two-letter contexts" level.
- Shannon's actual motorcycle record → twin → guess skyline → bits line → landing on the Y of THE OTHER DAY in the cold-open row (1 guess vs 5).
