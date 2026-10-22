# Round 8 review: substance (facts, story, clarity, concision, slop)

Critic: an independent science and story editor. I did not make this video. I recomputed every number, re-derived every formula, checked the citations on the web and scored every dimension.

Evidence used:
- The `review/` pack. metrics.json (19:14) is newer than final.mp4 (19:12), so I reused it rather than building a new one. From it I read report.md, transcript.txt, transcript_words.tsv and narration_diff.txt, plus narration.txt, script.md, facts.md and data.json.
- All 12 contact sheets.
- Full-resolution keyframes kf_04, 07, 13, 15, 18, 22, 24, 26, 28, 31, 32, 37 and 40.
- Frames I extracted myself:
  - 1:16.0–1:19.4 (six frames of the 2ᵏ = 1/p → k = log₂(1/p) step)
  - 2:12.3 (the run bill)
  - 2:20.9, 2:21.4, 2:22.6, 2:23.4 and 2:23.9 (the gap meter: it does reach 3.11, and the "3.10" on the sheet is a frame caught mid-count)
- An independent Brown recount with my own tokenizer (scratchpad `ep7r8/recount.py`, not `data.py`). It found N = 5,751,046, one fewer than `data.py` because of a trailing space. The other values:
  - H₁ = 4.1111, E/Z = 130.28, 1/p(Z) = 1263 (log₂ 10.30), top five = 48.34 %.
  - After Q: U 98.14 %, H 0.156. After TH: E 68.33 %, H 1.667.
  - ␣∣HE 0.6697 (cost 0.578), O∣E␣ 0.0720 (cost 3.796).
  - H(X∣1 prev) = 3.381, H(X∣2 prev) = 2.8105.
  - Every value matches data.json.
- Shannon's guess record, taken from data.json:
  - 102 symbols, 79 ones, 198 guesses in all.
  - −Σ q log₂ q = 1.4223 and log₂(102/8) = 3.672.
  - THE OTHER DAY → Y = 1 guess.
  - Product check on the run: 0.6833 × 0.6697 × 0.0720 = 0.0329, and log₂(1/0.0329) = 4.92. That is the same as 0.549 + 0.578 + 3.796.
- Web checks:
  - Shannon 1951: the princeton.edu PDF has "Out of 102 symbols the subject guessed right on the first guess 79 times". The archive.org listing confirms BSTJ 30(1), January 1951, pp. 50–64. arXiv:0911.2284 repeats "between 0.6 and 1.3 bits/letter over 100-letter long sequences".
  - LLMZip (arXiv 2306.04050v2, §IV and Table IV): "a recently released (May 25, 2023) book [7] under Project Gutenberg … only 0.8426 bits/character". The authors are Valmeekam, Narayanan, Kalathil, Chamberland and Shakkottai.

```
EPISODE: 007 — "How Much Information Is in a Letter?"
IDEA: A character costs log₂(1/p) yes/no questions, so the average cost (the area of a probability-wide, cost-tall skyline poured flat) is set by predictability, and it falls from the 4.75 that halving the alphabet suggests to about one bit once the guesser uses what came before.
SCORES: Hook 9 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 9 · Originality 9
WEIGHTED: 8.7   AFTER CEILING: 8.7 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none
FINAL: 8.7   PASS: no
```

Weighted = (15·9 + 25·8.5 + 15·8.5 + 15·8.5 + 10·8.5 + 10·9 + 10·9) / 100 = 867.5 / 100 = 8.7.

## FACTS

| Claim (spoken / shown) | Status | Source / my check |
|---|---|---|
| 26 letters + space = 27 symbols | Verified | Shannon 1951 p. 56 ("27 symbols") |
| Halving: 27 → 13 → 6 → 3 → 2 → 1, five cuts; Y isolated on the fifth | Verified | Arithmetic: 2⁴ < 27 ≤ 2⁵. kf_04 shows the chain ending on Y. |
| log₂ 27 ≈ 4.75, "the ideal" | Verified | 4.7549 |
| "In 1951, Claude Shannon put the true figure at about one" | Verified | Shannon 1951 p. 50: "of the order of one bit per letter" |
| "No compressor beats it on average" (it = the true figure) | Verified | Source-coding theorem; the floor is attached to the true rate, not to the estimate |
| "Guessing what comes next is how language models are trained" | Verified | Standard next-token objective; LLMZip §I. No on-screen citation, but this is a definition, not an empirical result. |
| "3.75 extra (79%)" | Verified | 4.75 − 1 = 3.75; 3.75 / 4.75 = 0.789 |
| E 10.3 %, Z 0.08 %, ×130 | Verified | Brown recount: 10.314 %, 0.0792 %, 130.3 |
| Space, E, T, A, O "nearly half" (48 %) | Verified | 48.34 % |
| E "near a tenth", 3.3 doublings | Verified | log₂(1/0.1031) = 3.277 |
| Z "one in 1260" needs 10.3 | Verified | 1/p = 1263, rounded to 3 s.f.; log₂ = 10.30 |
| p·2ᵏ = 1 → 2ᵏ = 1/p → k = log₂(1/p) | Verified | Each step is legal and shown on screen in turn (1:09–1:19) |
| Widths sum to 1, so area = average; the poured level | Verified | Definition of the expectation |
| H = 4.11 bits for English letters | Verified | Brown 4.1111, labelled Brown on screen. (Shannon's own older-table F₁ is 4.03.) |
| "Four times Shannon's estimate" | Verified | 4.11 / ≈1 |
| After Q, U 98 %; average 0.16 bits | Verified | 98.14 %; 0.156 |
| After TH, E is two thirds and costs about half a question; average 1.7 | Verified | 68.33 %; 0.549; 1.667 |
| Run E␣O: 0.5 + 0.6 + 3.8 = 4.9 → 5 questions; one at a time 1 + 1 + 4 = 6 | Verified | 0.549 + 0.578 + 3.796 = 4.92. This equals log₂(1/(0.683·0.670·0.072)); Shannon code ⌈4.92⌉ = 5; per-letter ceilings and Huffman depths give 6. |
| Average over every two-letter context: 2.8 (on screen 2.81, "1.81 extra") | Verified | 2.8105. The on-screen notation is loose (fix 3). |
| 27² = 729, 27¹⁰⁰ ≈ 10¹⁴³; Brown has 5.75 M characters | Verified | log₁₀ 27¹⁰⁰ = 143.14 |
| Subject guessed until right; 79 of 102 on the first guess | Verified | Shannon 1951 pp. 55–56 (web-checked) |
| An identical twin could rebuild the passage from the counts | Verified | Shannon 1951 p. 55 |
| Guess-count skyline: log₂(1/q) = 3.67 for the 2nd guess; pours to ≈ 1.42; "upper estimate"; "one passage, context 0–101" | Verified | 1.4223, recomputed from the record |
| "A better guesser could only lower it" | Verified | An ideal ranking majorises any other predictor's guess distribution, and entropy is Schur-concave |
| With 100 letters of context, 0.6–1.3 bits | Verified | Shannon 1951 p. 64 table, N = 100 column; corroborated by arXiv:0911.2284 |
| 2023 LLM, part of a 1924 book posted to Gutenberg after the model was trained, 0.84 bits; 27 symbols | Verified | LLMZip Table IV, 0.8426 (LLaMA-7B + arithmetic coding, text8-style 27-symbol preprocessing). The book was released 25 May 2023; LLaMA was released in Feb 2023. |
| The hidden character is the Y in "the other day"; one guess | Verified | Record, line 3: … D 1, A 1, Y 1 |
| Citations on screen | Verified | "Shannon, 1951 · Bell System Technical Journal"; "Letter counts: Brown Corpus (Francis & Kučera, 1964)"; "Valmeekam et al., 2023 · arXiv:2306.04050 (LLMZip), Table IV". All are correct. |

No claim is Wrong, Fabricated or Unverifiable.

## MECHANICS

runtime 3:34.3 · wpm 152 (speech time; 144 overall) · max silence 2.07 s (1:48.6, the planned Q prediction pause) · max static 3.30 s (3:31.0–3:34.3, end hold) · −14.1 LUFS / −1.8 dBTP · leading silence 0.00 s, trailing 0.83 s · 0 black frames · WER 1.0 % (the differences are numeral normalisation: "a hundred thirty" → "130" and so on) · 0 banned phrases. No mechanical cap triggers.

## Step notes

**1. Script, read cold.** The idea fits in one sentence (above). The arc follows §6 well:
- **Cold open (0:00–0:09):** the row ends in a ? box, the 27 tiles sit below, and the question is asked with a 2.0 s hold at 0:07.4.
- **Naive build (0:09–0:22):** "five", then log₂ 27 = 4.75.
- **Target (0:22):** Shannon's ≈1.
- **Fail (0:34–0:43):** "where do four of every five questions go?", 3.75 extra (79 %), and the cause is named: Z costs as much as E, at ×130 lower frequency.
- **Insight (0:43–1:47):** doubling strips, k = log₂(1/p), the skyline, the pour, then 4.11.
- **Context (1:47–2:28):** Q, then TH, then the run bill, then 2.81.
- **Payoff (2:28–3:18):** Shannon's person, 1.42, 0.6–1.3, LLM 0.84.
- **Landing (3:18–3:34):** back to frame one, now reading THE OTHER DA[Y], "1 guess" against "5 questions".

**2. Fact-check.** See the table: every number is reproduced, both web sources are confirmed and the formulas re-derive.

**3. Mechanics.** All within the bar (above).

**4. Transcript and slop.**
- None of the §4 phrases appear. A grep for "it turns out", "let's", "dive", "delve", "incredible", "fascinating", "journey", "basically", "essentially", "simply put", "the power of" and "picture this" returns 0.
- There are no rhetorical-question chains. "So where do four of every five questions go?", "What comes after a Q?" and "is it Y?" are each a single question.
- There are no "not just X" constructions and no lesson-list ending.
- One borderline colon reveal: "so Shannon used a predictor that knows English: a person" (2:29–2:33). It reveals content rather than pumping a fake mystery, so I do not count it, but it is the one line that sounds formulaic (fix 8).
- The ending reframes the cold open ("almost no letter arrives without a past"); it is not a recap.
- The hook lands by 0:07, and the likely-wrong answer "five" is voiced at 0:09.4.

**5. Contact sheets.**
- Narration and picture match within ±2 s throughout. Three examples:
  - "Z costs as much as E": E and Z are isolated on the one price line at 0:39.
  - "U swallows the bar": U widens under a 98 % brace at 1:55.
  - "these three": the three-column bill is up at 2:13–2:15.
- Objects persist from start to finish: the context row and the ? box, the tiles that become column feet, the chart that pours, the level lines and the number line markers.
- There are no hard cuts inside a beat.
- No slide frame appears. The densest frames are the run bill (2:11–2:19) and the payoff number line (3:09–3:18).

**6. Keyframes.**
- No text is clipped and nothing overlaps.
- Type is large, and LaTeX renders correctly: "Kučera", "␣", "log₂", "10¹⁴³".
- The palette holds (blue p, yellow questions and bits, green Shannon, purple context, grey abandoned or reference).
- Residual issues are in fixes 1, 3, 4 and 5.

## Dimension notes

- **Hook 9.** The concrete first frame and the prediction hold (0:07.4–0:09.4) are followed by a plausible wrong answer and a measured gap meter. The meter tightens across the whole video: 3.75 (0:35) → 3.11 (1:43) → 1.81 (2:25) → 0.42 (2:57) → inside the band (3:17). The landing re-sees frame one exactly (3:21–3:34). The one sag: the context section (1:47–2:20) runs on three local results (0.16, 1.67, the run) before the meter returns.
- **Clarity 8.5.** This is concrete before abstract, and every step of the k = log₂(1/p) derivation is shown and justified. Three spots still need a rewatch or mislead mildly:
  - (a) At 2:09–2:19 the run bill sits inside a "bits" chart whose ticks (5, 10), x-title ("share after TH") and 4.11 line do not belong to it, so the 3.8 reads as a height of about 7 bits (fix 1).
  - (b) "The fractions add up" is asserted. The viewer is never shown that the run's probability is the product of the three, so its log is the sum (fix 2).
  - (c) At 2:25 the slot reads "H = Σ p log₂(1/p) = 2.81 bits", but 2.81 is a context-weighted average of 729 such sums, a conditional entropy (fix 3).
- **Visual 8.5.** The semantic palette is clean and has a clear focal point in almost every frame (kf_07, kf_15, kf_31, kf_32 and kf_40 are teaching-grade). Deductions:
  - The bill drawn on foreign axes (kf_24, 2:16).
  - About 20 words of prose labels on the payoff number line at 3:13–3:18 (the "1924 book · on Gutenberg May 2023 · 27 symbols" note plus seven tags), against the 12-word limit.
  - The meter's hidden counter faintly visible as "0.48 extra" inside the TH stack (sheet 8, 2:21.0).
- **Motion 8.5.** The pours (1:27–1:31, 1:55–1:58, 2:51–2:55) and the 2 flying into log₂'s base (1:17.0–1:18.0) are proof-carrying motion. Deductions:
  - At 2:21–2:23 the meter re-grows from ≈1 to 4.11 to re-measure the 3.11 already shown at 1:43, then shrinks to 2.81: repeated motion with no new relation.
  - The count-sorting flight (2:49) is busy for 2 s, though it is ordered.
- **Audio 8.5.** Pace 152 wpm and loudness are on target. The deictics ("these counts" 2:47, "these three" 2:14) land on visible referents, and the pauses after results are planned (1.4 s after 4.11, 1.3 s after 0.16, 1.3 s after 79/102). Deductions:
  - An 11.1 s stretch without a breath of at least 0.35 s across 26 dense words at 2:04.6–2:16 ("Half a question … not six").
  - "one" held 0.50 s at 1:24.2 ("add to one,"), which can sound like odd emphasis.
  - Full stops are fairly uniform (median 0.38 s).
- **Concision 9.** There are 499 words, and every sentence does work. The repeats ("log base two of", "four point seven five", "half a question") are deliberate callbacks. The only slack is visual (the meter re-growth), not verbal.
- **Originality 9.** Pouring the skyline flat to turn area into average, applied three times to three different distributions, is a memorable image. Shannon's own passage, the identical twin and the post-training Gutenberg book are non-obvious, real material.

## FIXES (highest impact first)

1. **[2:08.5–2:16.3][Clarity/Visual] The run bill is drawn on the wrong axes.**
   - **Problem:** once the after-TH skyline leaves, the bill (E ␣ O, the context tags, 0.5 + 0.6 + 3.8 = 4.9 → 5, and 1 + 1 + 4 = 6) sits inside the chart. The y ticks 0/5/10 "bits", the x-title "share after TH", the 0–100 % ticks, the 4.11 reference and the ≈1 band all stay up, so 3.8 sits at the "7 bits" height, and "share after TH" mislabels the HE and E␣ costs.
   - **Change:** in the same animation that removes the TH skyline at 2:08.5, fade the axes, ticks, x-title, 4.11 line and band to 0 (keep the Brown citation). Bring them back with the TH pour on "After TH, it averages" (2:16.3).
   - No narration change.
2. **[2:11–2:15][Clarity] Show why fractions add.** No narration change.
   - On "the fractions add up", before "= 4.9", write a line beneath the bill (MathTex 36): `p(\text{run}) = 0.68 \times 0.67 \times 0.072 = 0.033`.
     - Make each factor a TransformFromCopy of its letter's share, in blue.
     - Then write `\log_2 \tfrac{1}{0.033} = 4.9`, with `log₂` in yellow, copied from the formula row's `k = log₂(1/p)` shape.
   - Let the existing "= 4.9" flash with it, so the run's cost visibly comes from the same k = log₂(1/p): the odds multiply, so the costs add.
   - If the space is too tight, put this line in place of the "1 + 1 + 4 = 6" row for 2 s, then restore that row on "not six".
3. **[2:24.5–2:28][Clarity] Label the 2.81 as an average of H's.**
   - When 2.81 is copied into the slot, write a grey `Text` 20 under "= 2.81 bits": "avg of 729 contexts' H".
   - Alternatively, TransformMatchingTex the slot's left side to `\bar H = \sum_c p(c)\,H(c)` for this value only, then back.
   - This keeps the on-screen equation literally true. Today the screen shows the single-distribution sum equalling a conditional entropy.
4. **[3:09–3:18][Visual] Payoff number line word load (about 20 words of prose against the 12 maximum).**
   - When the LLM note starts building on "book" (3:09), dim the tags "2-letter context", "no context", "halving" and "bits per character" to 30 %. Leave "person / 102 letters" and "0.6–1.3" bright, since the LLM's story is relative to those two.
   - Restore the tags with the landing fade.
5. **[2:21–2:24][Motion/Visual] The gap meter re-measures what it already showed.**
   - Instead of re-growing from ≈1 to 4.11 (reading 3.11) and then shrinking, grow it once from ≈1 straight to 2.81 on "every two-letter context", counting 0 → 1.81. The 4.11 reference stays as the comparison.
   - This also removes the faint "0.48 extra" readout visible inside the TH stack at 2:21.0.
   - It saves about 1.5 s of motion with no new information.
6. **[2:04.6–2:16][Audio] An 11.1 s breathless run of 26 words.**
   - In narration.json insert `[pause 0.3]` after "impossible," and `[pause 0.5]` after "the fractions add up". The second pause should land as "= 4.9" arrives (fix 2's product line).
   - Re-cue the bill to the new word times.
7. **[1:23.4–1:25][Audio] "one" is held 0.50 s at 1:24.2.** Change "The widths add to one, so the area is the average cost" to "The widths sum to one, so the area is the average cost". This moves the stress off a held function word, or else re-synthesise with "one" as the last word before a `[pause 0.3]`.
8. **[2:29–2:33][Originality] A colon reveal.** Change "so Shannon used a predictor that knows English: a person." to "so Shannon asked a person, a predictor that already knows English." Re-cue the yellow cursor lock and the purple row flash to "a person" at its new time.
9. **[3:30.5–3:34.3][Visual] Keep the Y tile highlighted.** The Y's blue highlight in the tile row drops when the chain steps back (3:31), so the last 3 s lose the link between "5 questions" and this Y. Keep the Y tile at full blue with its white outline to the end.

REACHES 9 IF ALL FIXED: yes.
- Fixes 1–3 lift Clarity to 9: the bill reads on its own, the run's cost comes from the formula already on screen, and every equation shown is literally true.
- Fixes 1, 4 and 5 lift Visual and Motion to 9.
- Fixes 6 and 7 lift Audio to 9.
- That gives (15·9 + 25·9 + 15·9 + 15·9 + 10·9 + 10·9 + 10·9) / 100 = 9.0.
- No structural change is needed: the hook, the failure beat and the visual insight are all present and correct.

KEEP:
- The poured skyline (area = average), reused for letters, after-Q, after-TH and the guess counts. It is the episode's proof, and it is what viewers will remember.
- The measured gap meter (3.75 → 3.11 → 1.81 → 0.42 → inside the band) and the landing that turns frame one into THE OTHER DA[Y], "1 guess" against "5 questions".
- The sourcing discipline: Brown counts, Shannon's own passage and twin argument, and the LLMZip book figure with its "1924 book · on Gutenberg May 2023 · 27 symbols" caveat. Every number in the episode reproduces.
