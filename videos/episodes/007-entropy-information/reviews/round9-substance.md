# Round 9 review: substance (facts, story, clarity, concision, slop)

Critic: an independent science and story editor. I did not make this video. I recomputed every number, re-derived every formula, checked the citations on the web and scored every dimension.

## Evidence

**Review pack.** `review/metrics.json` (20:57) is newer than `final.mp4` (20:54), so I reused it rather than building a new one. From it I read:
- `report.md`, `transcript.txt`, `transcript_words.tsv` and `narration_diff.txt`
- `narration.txt`, `script.md`, `facts.md`, `data.json` and the round-8 CHANGELOG

**Frames.**
- All 12 contact sheets.
- Full-resolution keyframes kf_01, 04, 07, 14, 18, 24, 26, 29, 31, 32, 36 and 40.
- Frames I extracted myself:
  - 0:23.0
  - 1:37.0
  - 2:17.8, 2:19.0 (the bill exit and the TH pour)
  - 2:49.5 (the count flight)
  - 2:58.5
  - 3:08.5, 3:14.5, 3:16.0 (the LLM marker)
  - 3:21.5
  - 3:31.0

**Independent Brown recount.** I wrote my own tokenizer (scratchpad `ep7r9/recount.py`, not `data.py`). It found:
- N = 5,751,046 characters.
- H₁ = 4.1111. E 10.314 %, Z 0.0792 %, E/Z = 130.28, 1/p(Z) = 1263.
- Top five = 48.34 %.
- After Q: n = 5,103, U 98.14 %, H = 0.156.
- After TH: n = 134,673, E 68.33 %, H = 1.667.
- ␣∣HE 0.6697 and O∣E␣ 0.0720.
- H(X∣2 previous) = 2.8105.

Every value matches `data.json`.

**Shannon's record**, taken from `data.json`:
- 102 symbols, 79 ones, 198 guesses in all.
- Counter {1: 79, 2: 8, 3: 3, 4: 2, 5: 2, 6: 3, 7, 8, 11, 15, 17: 1 each}.
- −Σ q log₂ q = 1.4223 and log₂(102/8) = 3.672.
- The guess-chart column heights check: 0.37, 3.67, 5.09, 5.67, 5.67, 5.09, and 6.67 for each singleton.

**Run bill.**
- 0.683 × 0.670 × 0.072 = 0.03295 → 0.0329, and log₂(1/0.0329) = 4.926 → 4.93.
- 0.55 + 0.58 + 3.80 = 4.93. The exact sum is 0.549 + 0.578 + 3.796 = 4.923, and ⌈4.92⌉ = 5.
- One at a time, ⌈cost⌉ gives 1 + 1 + 4 = 6.

**Web checks.**
- Shannon 1951 (princeton.edu PDF): "Out of 102 symbols the subject guessed right on the first guess 79 times". In §6 the column-100 lower bound is ".6", and the upper bound of 1.3 is corroborated by M. Mahoney's summary "0.6 to 1.3 bpc".
- LLMZip (arXiv 2306.04050v2, §IV and Table IV): "The compression ratio for LLaMA with arithmetic coding is only 0.8426 bits/character". The table row is M = 511, N_c = 508,463, H_ub 0.8417, ρ 0.8426. The book was released on Gutenberg on 25 May 2023. The authors are Valmeekam, Narayanan, Kalathil, Chamberland and Shakkottai.

```
EPISODE: 007 — "How Much Information Is in a Letter?"
IDEA: A character costs log₂(1/p) yes/no questions, so the average cost (a probability-wide, cost-tall skyline poured flat) is set by predictability, and it falls from the 4.75 that halving the alphabet suggests to about one bit once the guesser uses what came before.
SCORES: Hook 9 · Clarity 9 · Visual 8.5 · Motion 9 · Audio 9 · Concision 9 · Originality 9
WEIGHTED: 8.9   AFTER CEILING: 8.9 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none
FINAL: 8.9   PASS: no
```

Weighted = (15·9 + 25·9 + 15·8.5 + 15·9 + 10·9 + 10·9 + 10·9) / 100 = 892.5 / 100 = 8.9.

## FACTS

| Claim (spoken / shown) | Status | Source / my check |
|---|---|---|
| 26 letters + space = 27 symbols | Verified | Shannon 1951 p. 56 |
| Halving: 27 → 13 → 6 → 3 → 2 → 1, five cuts, ends on Y | Verified | 2⁴ < 27 ≤ 2⁵. kf_04 shows the chain ending on Y. |
| "The ideal is log base two of 27: 4.75" | Verified | 4.7549 |
| Shannon 1951 put the true figure "at about one" | Verified | Shannon 1951 p. 50; band 0.6–1.3 at N = 100 (p. 64) |
| "No compressor beats it on average" (it = the true figure) | Verified | Source-coding theorem |
| "Guessing what comes next is how language models are trained" | Verified | The next-token objective. This is a definition, so no citation is needed. |
| "3.75 extra (79%)"; "four of every five questions" | Verified | 3.75 / 4.75 = 0.789 |
| E 10.3 %, Z 0.08 %, ×130 | Verified | My recount: 10.314 %, 0.0792 %, 130.3 |
| Space, E, T, A, O are "nearly half" (48 %) | Verified | 48.34 % |
| E "near a tenth"; 3.3 doublings | Verified | log₂(1/0.1031) = 3.277 |
| Z "one in 1260" needs 10.3 | Verified | 1/p = 1263 (3 s.f.); log₂ = 10.30 |
| p·2ᵏ = 1 → 2ᵏ = 1/p → k = log₂(1/p) | Verified | Each step is legal and shown in turn (1:09–1:19) |
| The widths add to 1, so area = average; the pour | Verified | Definition of the expectation |
| H = 4.11 bits for English letters (Brown, labelled) | Verified | 4.1111. Shannon's older-table F₁ is 4.03; the episode uses only the Brown value. |
| "Four times Shannon's estimate" | Verified | 4.11 / ≈1 |
| After Q: U 98 %, average 0.16 | Verified | 98.14 %; 0.156 |
| After TH: E is two thirds and costs "about half a question"; average 1.7 | Verified | 68.33 %; 0.549; 1.667 |
| Run E␣O: 0.683 × 0.670 × 0.072 = 0.0329; log₂(1/0.0329) = 4.93 = 0.55 + 0.58 + 3.80 → 5; one at a time 1 + 1 + 4 = 6 | Verified | Recomputed (above). The chain rule for a 2nd-order model; Shannon code ⌈4.92⌉ = 5. |
| Every two-letter context: 2.8 (screen 2.81, "H averaged over contexts", "1.81 extra") | Verified | 2.8105 (my own H(X∣2) recount) |
| 27² = 729; 27¹⁰⁰ ≈ 10¹⁴³; Brown has 5.75 M characters | Verified | log₁₀ 27¹⁰⁰ = 143.14 |
| "Hundred-letter contexts need more text than any corpus holds" | Verified | This holds even for typical strings, about 2^(100·H) ≥ 10³⁰, not only all 27¹⁰⁰ |
| The subject guesses until right; 79 of 102 on the first guess | Verified | Shannon 1951 pp. 55–56, web-checked |
| A twin could rebuild the passage from the counts | Verified | Shannon 1951 p. 55 ("identical twin") |
| Guess skyline log₂(1/q) = 3.67; pours to ≈ 1.42; "upper estimate"; "one passage, context 0–101" | Verified | 1.4223 recomputed. It is a plug-in estimate of Shannon's eq. 17 upper bound, honestly labelled. |
| "A better guesser could only lower it" | Verified | Ideal ranking majorises any other guesser's guess distribution, and entropy is Schur-concave (in expectation) |
| Shannon, 100 letters of context: 0.6–1.3 bits | Verified | Shannon 1951 §6 table, column 100 |
| 2023 LLM, part of a 1924 book posted to Gutenberg after training: 0.84 bits; 27 symbols | Verified | LLMZip Table IV, 0.8426 (LLaMA-7B + AC, text8-style preprocessing); Gutenberg 25 May 2023; LLaMA released Feb 2023 |
| The hidden character is the Y in "the other day"; one guess | Verified | Record line 3: … D 1, A 1, Y 1 |
| On-screen citations | Verified | "Shannon, 1951 · Bell System Technical Journal"; "Letter counts: Brown Corpus (Francis & Kučera, 1964)"; "Valmeekam et al., 2023 · arXiv:2306.04050 (LLMZip), Table IV · 27 symbols" |

No claim is Wrong, Fabricated or Unverifiable.

## MECHANICS

| Metric | Value |
|---|---|
| Runtime | 3:34.7 |
| Pace | 152 wpm over speech time (143 overall) |
| Longest internal silence | 2.01 s (0:07.4, the planned prediction hold) |
| Longest static stretch | 3.03 s (3:31.7, the end hold) |
| Loudness / true peak | −14.0 LUFS / −1.7 dBTP |
| Leading / trailing silence | 0.00 s / 0.56 s |
| Black frames | 0 |
| Narration vs transcript | WER 1.8 %. The differences are numeral normalisation plus the homophone "Y" → "why". |
| Banned phrases | 0 |
| Layout audit | 0 issues |

No mechanical cap triggers.

## Step notes

**1. Script, read cold.** The idea fits in one sentence (above), and the arc follows BAR §6:

| Beat | Time | What happens |
|---|---|---|
| Cold open | 0:00–0:09 | Row and ? box, the 27 tiles, the question, a 2.0 s hold |
| Naive build | 0:09–0:22 | Five cuts, then log₂ 27 = 4.75 |
| Target and stakes | 0:22–0:34 | Shannon's ≈1; compressors and language models |
| Fail | 0:34–0:43 | 3.75 extra (79 %); the cause named: Z priced like E at 1/130 the frequency |
| Insight | 0:43–1:47 | Doubling strips, k = log₂(1/p), the skyline and the pour, then 4.11 with the meter at 3.11 |
| Context | 1:48–2:26 | Q 0.16; TH 1.67; the run bill (why half a question is possible); 2.81 overall |
| Payoff | 2:27–3:18 | Shannon's person, 1.42 upper estimate, 0.6–1.3, LLM 0.84 |
| Landing | 3:19–3:34 | Frame one re-seen, THE OTHER DA[Y], "1 guess" against "5 questions" |

**2. Fact-check.** Every number reproduces (table above), both web sources check out, and every formula re-derives.

**3. Mechanics.** All within the bar.

**4. Transcript and slop.**
- I found none of the §4 phrases, no "not just X" constructions and no rhetorical-question chains:
  - "So where do four of every five questions go?", "What comes after a Q?" and "is it Y?" each stand alone.
  - "Is it a space, E, T, A or O?" is the strategy's own question, not rhetoric.
- The round-8 colon reveal ("…: a person") is gone.
- "Now make each character's cost its height" is an instruction with a visible referent, not signposting.
- The ending reframes the cold open rather than recapping it.
- The hook question is complete by 0:07.5, and the likely-wrong answer "five" lands at 0:09.4.

**5. Contact sheets.**
- Narration and picture match within ±2 s throughout. For example:
  - "E turns up 130 times as often" at 0:41: ×130 between the leaders.
  - "U swallows the bar" at 1:55: U widens under the 98 % brace.
  - "their costs add" at 2:13: the sum row builds.
  - "79 of 102" at 2:41: the tally reaches 79 / 102.
  - "point eight four" at 3:17: the marker sits at 0.84.
- Objects persist from start to finish: the context row, the tiles that become column feet, the poured stacks, the level lines and the number-line markers. There are no hard cuts inside a beat.
- Two staging problems appear in the flipbook and are confirmed at full resolution:
  - **(a) The LLM marker sits on 1.42.** At 3:08.6–3:15.7 the white "LLM ▼" sits directly above "1.42 ▼" for about 7 s (sheet 11 at 3:09, 3:11, 3:13 and 3:15; kf_36; my frame at 3:14.5). While the LLM sentence is spoken, the screen reads "LLM = 1.42".
  - **(b) The bill and the chart overlap.** At 2:17.5–2:21.5 the bill is still at full strength, then dims, while the chart's axes (ticks 0/5/10, ≈1, "share after TH") fade back in and the TH stack pours beneath it (my frames at 2:17.8 and 2:19.0).
    - "3.80" sits at the 5-bit tick, and the pouring columns' top edge passes about 20 px under "1 + 1 + 4".
    - For about 3 s this brings back the "bill on foreign axes" reading that round 8 removed.

**6. Keyframes.**
- No text is clipped, nothing overlaps, and the safe area is respected; the citations sit at y ≈ −2.96.
- LaTeX renders cleanly: "Kučera", "␣", "log₂", "10¹⁴³".
- The palette holds: blue p, yellow questions and bits, green Shannon, purple context, grey abandoned or reference, ink LLM.
- On the guess chart (kf_32, 2:55–2:58), the ≈1 band is only two 2 px green lines among thirteen dark slab separators. The 0.6 edge sits about 5 px from a separator, so the band does not read as a band under the "0.42 extra" meter.
- The run bill (kf_24) carries 14 numbers in four rows. It is built term by term on its words, so it does not read as a slide, but it is the densest frame in the episode.

## Dimension notes

- **Hook 9.**
  - The first frame is concrete, and the question plus a 2.0 s hold (0:07.4–0:09.4) are followed by the plausible wrong answer.
  - The measured gap meter then keeps tension rising: 3.75 (0:35) → 3.11 (1:43) → 1.81 (2:25) → 0.42 (2:57) → inside the band (3:17).
  - The landing re-sees frame one exactly (3:21–3:34).
  - The one sag is the stakes sentence at 0:27–0:33, which is asserted rather than shown. That is a nitpick.
- **Clarity 9.**
  - Every round-8 clarity item is fixed:
    - The run bill now shows the product and its log (2:11–2:15).
    - The bill no longer sits on axes while it is read (2:09–2:17).
    - 2.81 is labelled "H averaged over contexts" (kf_26).
  - The derivation is concrete-first, every algebra step is shown on its words, and every number checks.
  - Two residual nitpicks:
    - The 1.42 step (2:47–2:58) never says that the guess cost caps the text cost; "upper estimate" carries it alone (fix 4).
    - The "0.42 extra" meter followed by "A better guesser could only lower it" lets a viewer attribute the gap to Shannon's band to the guesser, when the gap is mostly short contexts and one 102-letter sample (fix 5).
  - The LLM-on-1.42 frame is scored under Visual.
- **Visual 8.5.** The palette and hierarchy are strong (kf_07, kf_18, kf_26, kf_29 and kf_40 are teaching-grade), but three minor issues remain, one more than the 8 anchor allows:
  - LLM ▼ over 1.42 ▼ for about 7 s (3:08.6–3:15.7).
  - The bill inside the re-entering chart for about 3 s (2:17.5–2:21.5).
  - A band that cannot be read on the guess chart (2:55–2:58).
- **Motion 9.**
  - The round-8 fixes hold:
    - The payoff line is built in story order (2:59–3:03).
    - The meter grows once to 2.81 (2:23–2:25).
    - The 2 dips under the "=" (1:16–1:18).
  - The pours (1:27–1:31, 1:55–1:58, 2:53–2:55) and the count sort (2:49–2:51, ordered bottom row first, f_2:49.5) carry the argument.
- **Audio 9.**
  - Pace is 152 wpm, loudness −14.0 LUFS and true peak −1.7 dBTP.
  - The act turns are about 0.8 s against 0.38 s ordinary gaps, and the results get 1.1–1.4 s holds: 4.11 at 1:38.8, 0.16 at 1:58.4 and 79 / 102 at 2:43.1.
  - Both deictics land.
  - I found no mispronounced term; "Y" heard as "why" is a homophone.
- **Concision 9.** There are 497 words. Each beat buys a distinct number on the path from 4.75 to 0.84, and the repeats ("log base two of", "four point seven five", "two to the k") are deliberate callbacks.
- **Originality 9.** The memorable image is pouring the skyline flat, used four times on four distributions. Shannon's own passage, the identical twin and the post-training Gutenberg book are real, non-obvious material.

## FIXES (highest impact first)

1. **[3:08.6–3:15.7][Visual] The LLM marker reads as "LLM = 1.42" for about 7 s.**
   - **Problem:** on "a language model" the white LLM ▼ is born from the person's triangle and parks directly above "1.42 ▼" until "needed" (kf_36; frame 3:14.5).
   - **Change:**
     - Birth it on its upper track but offset to x = 1.0 bits (over the band centre), with a grey "?" in the value row under it. The "1924 book · Gutenberg, May 2023" note builds above it as now.
     - On "point eight four" (3:15.7), slide it to 0.84 and swap "?" for "0.84".
   - **If the "born from the person" motion must stay:** start the slide left on "book" (3:10.4), so the stacked state lasts under 1 s and the marker waits over a "?" instead.
2. **[2:17.5–2:21.5][Visual/Clarity] The bill is read against the returning after-TH axes.**
   - **Problem:** on "After TH, it averages", the axes, ticks 0/5/10, ≈1 and "share after TH" fade in, and the TH stack pours under the still-bright bill. "3.80" sits on the 5-bit tick (frames 2:17.8 and 2:19.0).
   - **Change:** in the play that starts on "After" (2:17.5), FadeOut the four bill rows completely over 0.5 s. Keep only the run box, at 30 %, in the context row. Start the axes' fade-in and the TH pour 0.4 s later, so they land on "averages" (2:18.9).
   - No narration change.
3. **[2:55–2:58][Visual] Shannon's band cannot be read on the guess chart.**
   - **Problem:** the 0.6 and 1.3 edges are 2 px green lines among thirteen dark slab separators (kf_32).
   - **Change:**
     - Once the pour lands, step the separator strokes to 25 % opacity.
     - Draw the two band edges at 4 px, extended 0.25 units past both ends of the stack.
     - This keeps the no-teal rule (no fill), and the "0.42 extra" meter then visibly starts from the band.
4. **[2:56.0–2:58.5][Clarity] Say why 1.42 is an upper estimate.**
   - Change "A better guesser could only lower it." to "That caps the text; a better guesser could only lower it." (+3 words).
   - Land the grey "upper estimate" on "caps".
   - Rationale: the twin line gave reversibility; this sentence closes the loop, since sending the counts at 1.42 bits each and letting the twin rebuild the text means the text costs at most 1.42.
5. **[2:59–3:06][Clarity] Show why Shannon's band sits below 1.42.**
   - Change the note under the guess-chart level from "one passage, context 0–101" to "one passage · most letters < 100 context". Alternatively, change the narration to "Shannon's tests, giving every letter a hundred letters of context, put English…" (+1 word).
   - Either way, the step from 1.42 to the 0.6–1.3 band is attributed to context length, not only to guesser quality.
6. **[0:27–0:33][Hook, nitpick] Make the stakes visible.**
   - On "No compressor beats it", draw a thin yellow floor line at ≈1, labelled "floor (true figure)" in grey, under the band for 2 s.
   - The stakes sentence then points at something on screen instead of being purely spoken.

REACHES 9 IF ALL FIXED: yes.
- Fixes 1–3 lift Visual to 9.
- Fixes 4 and 5 make the payoff's hardest step re-derivable after one watch.
- That gives (15·9 + 25·9 + 15·9 + 15·9 + 10·9 + 10·9 + 10·9) / 100 = 9.0.
- No structural change is needed: the hook, the measured failure, the visual insight and the cited payoff are all in place, and every number is correct.

KEEP:
- The poured skyline (area = average), reused for letters, after-Q, after-TH and the guess counts. It is the episode's proof and its memorable image.
- The gap meter (3.75 → 3.11 → 1.81 → 0.42 → inside the band), and the landing that turns frame one into THE OTHER DA[Y], "1 guess" against "5 questions".
- The run bill's product-and-log line (0.683 × 0.670 × 0.072 = 0.0329, log₂(1/0.0329) = 4.93 = 0.55 + 0.58 + 3.80), and the sourcing discipline (Brown recount, Shannon's own record and twin argument, LLMZip's post-training book).
