# Episode 7, review round 1 (substance: science and story editor)

Evidence used: `review/` pack (metrics.json 11:10 is newer than final.mp4 11:08, so it was reused), report.md, all 11 contact sheets, 13 full-resolution keyframes (kf_02, 05, 10, 16, 20, 22, 28, 29, 32, 34 plus extracted frames at 0:27.0, 0:27.6, 0:28.2, 1:39.4, 1:45.0, 2:18.6–2:24.2, and crops at 2:23.6–2:26.4), transcript.txt, narration_diff.txt, script.md, facts.md, narration.txt, data.json, scene.py.
Independent checks: I downloaded the NLTK Brown corpus and recomputed every corpus number with my own script, re-derived every formula, and read Shannon (1951) from the Princeton mirror of the BSTJ scan.

```
EPISODE: 007 — "How Much Information Is in a Letter?"
IDEA: A character costs log2(1/p) yes/no questions, so the information in a letter depends on how predictable it is; with frequencies alone English costs 4.11 bits per character, and with context it falls to about one.
SCORES: Hook 8 · Clarity 7 · Visual 7.5 · Motion 8 · Audio 8 · Concision 8 · Originality 8
WEIGHTED: 7.7   AFTER CEILING: 7.7   (lowest 7 + 2 = 9, so the ceiling does not bind)
CAPS: Factual/mathematical error → 6 (@3:03.9–3:06.9, narration "Five questions is the price of a letter with no past" contradicts the episode's own result at 1:52–2:05, where a letter priced "as if nothing came before it" costs 4.11 bits, not 5)
      | Text overlapping another element → 7 (@2:23.6–2:25.8, the blue "68%" label is struck through by the moving yellow average line for about 2 s; briefly again at about 2:19.0, the "98%" label)
FINAL: 6.0   PASS: no
```

## FACTS

| Claim | Verdict | Source / my check |
|---|---|---|
| Alphabet is 26 letters + space = 27 symbols | Verified | Shannon 1951, p. 56: "an alphabet of 27 symbols, A, B, …, Z, space" |
| 5 halvings take 27 to 1 (chain 27→13→6→3→2→1) | Verified | 2^4 = 16 < 27 ≤ 32; the chain shown is one valid worst-case path |
| log2 27 ≈ 4.75 | Verified | 4.7549. Shannon's F0 for 27 letters = 4.76 (p. 54 table). Nit: "More exactly" presents the ideal fractional cost as the exact answer; a real equal-split tree averages 4.73 on Brown text and 4.81 on uniform text |
| Shannon 1951 estimated ≈ 1 bit per character | Verified | p. 50: "reduce the entropy to something of the order of one bit per letter". BSTJ 30(1):50–64, Jan 1951 |
| "That's the floor for any text compressor" | Verified with caveat | The true entropy rate is the floor (source coding theorem). Shannon's "≈1" is an estimate with a range of 0.6–1.3, and modern LLM coders already sit below 1.0 on 27-symbol text: LLaMA-7B gives 0.709 bits/char on text8 (Valmeekam et al., 2023, arXiv:2306.04050, "LLMZip"). Saying "about one is the floor" overstates things slightly; see fix 4 |
| Guessing the next token is how language models are trained | Verified | Standard autoregressive cross-entropy objective. It is never paid off later (fix 4) |
| "Four of every five questions" are excess | Verified | (4.755 − 1)/4.755 = 0.79 |
| E turns up 130× as often as Z | Verified (recomputed) | Brown, 27-symbol: p(E) = 0.10314, p(Z) = 0.000792, ratio 130.3; 5,751,047 chars, 1,005,119 words, matching facts.md exactly |
| Space, E, T, A, O ≈ half of text (48%) | Verified (recomputed) | 17.48 + 10.31 + 7.63 + 6.66 + 6.26 = 48.34% |
| E ≈ a tenth; 3.3 doublings | Verified | log2(1/0.10314) = 3.277 |
| Z = 1 in 1,260; needs 10.3 | Verified | 1/p = 1263.1 (rounded down to 1,260 when spoken, acceptable); log2 = 10.30 |
| p·2^k = 1 ⇒ k = log2(1/p) | Verified (re-derived) | Each ideal answer halves the remaining mass, so p's share doubles; it reaches 1 after log2(1/p) answers |
| Widths sum to 1, so area = average questions | Verified | E[log2(1/p)] = Σ p log2(1/p) |
| H for English letters = 4.11 bits | Verified (recomputed) | 4.1111 (Brown); labelled as Brown on screen. Shannon's own 27-letter F1 is 4.03 |
| "Still four times Shannon's estimate" | Verified | 4.11/1 |
| After Q, U 98 in 100; average 0.16 bits | Verified (recomputed) | 5,103 Q's; U = 98.14%; H(next ∣ Q) = 0.156 |
| After TH, E > 2/3; average 1.7 | Verified (recomputed) | 134,673 TH's; E = 68.33%; H = 1.667 |
| Experimental procedure (guess until right) | Verified | Shannon 1951 p. 55–56 |
| The on-screen record and its guess counts | Verified | Matches display (9), p. 56. My tally from data.json: 79 / 8 / 3 / 2 / 2 / 8 (>5), exactly as Shannon states |
| 79 of 102 right on the first guess | Verified | p. 56: "Out of 102 symbols the subject guessed right on the first guess 79 times" |
| With 100 letters of context, 0.6–1.3 bits/char | Verified | p. 64 table, column 100: Upper 1.3, Lower .6 |
| Human-guesser range; predictability, not meaning | Verified | p. 56 (text-type dependence); entropy is defined on probabilities only |
| The hidden character is the Y of "the other day", 1st guess | Verified | Record line 3: D 1, A 1, Y 1 |
| **"Five questions is the price of a letter with no past"** | **Wrong** | By the video's own derivation, a letter with no past costs H1 = 4.11 bits (1:52–2:05: "prices every character as if nothing came before it"). Five is the worst-case price of a letter you know *nothing* about, frequencies included. Cap 6 |
| Brown Corpus, Francis & Kučera, 1964 | Verified | CoRD/Helsinki and Wikipedia: compiled by W. N. Francis and H. Kučera, 1964 (rev. 1971, 1979) |

## MECHANICS

| Metric | Value | Status |
|---|---|---|
| Runtime | 3:12.6 | ok |
| Pace | 161 wpm (speech time), 502 words | ok |
| Longest internal silence | 1.96 s (2:07.1–2:09.1, planned prediction hold) | ok |
| Leading / trailing silence | 0.00 s / 1.74 s | ok |
| Longest static stretch | 3.53 s (2:00.3–2:03.8) | ok |
| Loudness | −14.0 LUFS integrated, −1.9 dBTP | ok |
| Banned phrases | 0 | ok |
| Script WER | 1.8% | ok |

No mechanical caps. The narration diff shows only number formatting and "Y"→"why" (correct homophone). No mispronounced technical terms.

## Transcript and story notes

- **Hook (0:00–0:13): strong.** The first frame is a hidden row with a yellow "?". The question lands at 0:06–0:11 and is followed by a 2.0 s hold. "The natural answer is five" is a believable wrong commitment. At 0:26–0:32 Shannon's "about one" is a real reversal, and "where do four of every five questions go?" (0:40) drives the middle. Two problems:
  1. **Ambiguous setup.** The 12 context boxes are grey and hidden. A careful viewer who reasons "I can't see anything before it" should answer about 4.1, not about 1. The answer only works if the guesser *has read* the past. The landing (THE OTHER DA flying in) shows that was the intent, but the cold open never says so.
  2. **Unpaid stake.** The stakes line promises language models (0:35–0:40), and they never come back.
- **Fail beat (0:40–0:55): good.** The 4/5 overlay, then E versus Z at equal height, then real widths. The failure is measured and the cause is named. The phrase "Cutting the alphabet in half prices every character alike" is a garden path: listeners parse "half prices" as a noun, and Whisper even punctuated it as "in half prices, every character".
- **Insight (0:55–2:05): the best part.** The E strip doubling against a live counter, p·2^k = 1 built from E's column, the skyline morph, and "widths add up to one, so area = average" are all solid 3b1b-grade moves. Weak spots:
  - Rare letters vanish (fix 7).
  - p is coloured yellow inside 1/p (fix 8).
  - "That makes k log base two of one over p" is missing a verb.
- **Context (2:05–2:27): very good.** Q→U is the right example and the H counter falls in sync with "falls to point one six" (2:18.6 shows 3.75, 2:19.4 shows 1.00, 2:20.2 shows 0.16). The TH step lags because the chart first resets to no context: E widens at about 2:24 for words spoken 2:21–2:24.
- **Payoff (2:27–2:56): real, correctly cited, honest limits.** But the jump from "79 of 102 first guesses" to "0.6–1.3 bits" is pure authority. The viewer is never shown how guesses become bits, even though the formula needed is already on screen. Applying H = Σ q log2(1/q) to the guess-count distribution in this record gives 1.42 bits/char (79, 8, 3, 2, 2, 3, 1, 1, 1, 1, 1 of 102; my computation). That is Shannon's own upper-bound construction (eq. 17, valid "whether or not the prediction is ideal").
- **Landing (2:56–3:12): structurally excellent.** The hidden character turns out to be Shannon's own Y, guessed first time, and the line about letters arriving with a past reframes the opening. It is undermined by one false sentence (cap 6).
- **Slop scan.** No banned phrases, no question chains, no recap ending. There is a mild verbal tic of three "X, not Y" antitheses: "split the probability, not the alphabet" (0:56), "a range from human guessers, not a constant" (2:50) and "predictability, not meaning" (2:54). Keep the first and rephrase one of the other two.

## Visual and motion notes (keyframes)

- **Palette is disciplined.** Blue is probability, yellow is questions/bits, green is Shannon, purple is context, grey is ghosts and citations. Colour stays consistent from the cold open through the landing. One violation: in `k = log2(1/p)` (1:31–1:47) and in `H = Σ p log2(1/p)` (1:47–2:27), the p in the denominator is yellow because the whole `\log_2\frac{1}{p}` substring is coloured yellow (scene.py lines 491–493, 517–520, 553–556).
- **Rare letters invisible (kf_22 @1:43.4).** The tallest visible column reaches about 7.5 (K). J, X, Q and Z (9.3–10.3 bits) are 1–2 px wide and effectively invisible except during the 1:39 yellow flash. The narration "rare ones narrow and tall" and the axis to 10 promise them.
- **Label overlap (crops @2:23.6–2:25.8).** The "68%" label rides the top of E's column while the yellow H line descends from 4.11 to 1.67, so the dashed line runs through the label for about 2 s. The same happens with "98%" at about 2:19.0. Cap 7.
- **Cluttered transition (@0:27.0–0:28.2).** The axes and the "questions / 10" label draw over the alphabet and the hidden row while the chain and "log2 27 ≈ 4.75" are still on screen. A stray yellow tick and grey dot sit at the left (about x 300, y 570 at 0:27.0). This lasts under 1.5 s, so it is a polish item, not a cap.
- **Typography passes §5.** Citations measure about 28 px cap height and sit above y = −3.2. Axes carry names: "questions"/"bits", and "share of text"/"share after Q". Ticks are at most 5. The record (kf_32) is legible. Nit: "11 5" under DRAMATICALLY reads as "115".
- **Continuity is a real strength.** The hidden row persists 0:00–2:27, tiles become columns, uniform widths become real widths, the columns re-sort, heights morph into the skyline, the chart is conditioned on context, and the record's characters fly into the cold-open row. There is one hard cut, at 2:27 on a beat boundary.

## FIXES (highest impact first)

1. **[3:03.9–3:06.9][Clarity] Removes cap 6.** "Five questions is the price of a letter with no past" contradicts the video's own 4.11.
   - Replace with: "Five questions is what a letter costs when you know nothing about it. In English, almost no letter arrives without a past."
   - Or, if you keep "no past", change the on-screen "5 questions" (scene.py line 820) and the narration to "4.11 bits" and bring back the grey/yellow markers from the payoff line.

2. **[2:21–2:27 and 2:17–2:20][Visual] Removes cap 7.** The "68%" and "98%" labels are struck by the moving H line.
   - In `pct_label` (scene.py lines 667ff.), anchor the call-out below the x-axis beside the column's tick letter (for example "E 68%" replacing the E tick label) instead of above the column top.
   - Or fade e68 in only after the final `morph(..., extra=[self.avg...])` finishes, at fixed y = 2.4 bits (above the final 1.67 line).
   - Then re-check frames 2:19.0 and 2:24.0 for any line–text contact.

3. **[2:41–2:50][Clarity] Show how guesses become bits instead of asserting 0.6–1.3.** This is the biggest remaining clarity gap and the most original payoff available.
   - After "79 of 102 came on the first guess", `TransformFromCopy` the guess counts into a small histogram of guess numbers (1: 79, 2: 8, 3: 3, …).
   - Copy `H = Σ p log2(1/p)` onto it and land on "≈ 1.4 bits". Recomputed from data.json: 1.42.
   - New line (about 14 words): "Treat the guess numbers as the new alphabet. The same formula gives about one point four bits."
   - Then keep "with a hundred letters of context, 0.6 to 1.3" as Shannon's full-sample result. State that this one passage gives an upper bound (Shannon eq. 17, p. 61).

4. **[0:32–0:40 and 2:41–2:56][Hook/Clarity] Pay off the language-model stake, or cut it, and soften "the floor".**
   - Change 0:32 to: "The true figure is the floor for any text compressor."
   - Add one payoff beat after Shannon's range, with an on-screen citation: "In 2023, a language model compressing the same 27-symbol English got 0.71 bits per character, inside Shannon's range." The citation is *Valmeekam et al., 2023 · arXiv (LLMZip)*: LLaMA-7B, text8, 0.709 bits/char. Mark it as a yellow marker on the 0–5 line inside the green band.
   - Runtime budget allows it (3:12 → about 3:25).
   - Otherwise, delete "and guessing what comes next is exactly how language models are trained."

5. **[0:00–0:11][Hook/Clarity] Disambiguate what the guesser knows.**
   - Add a dim purple "already read" label over the 12 hidden boxes.
   - Change the second line to: "You've read everything before it. With only yes-or-no questions, how many do you need per character, on average?"
   - This makes "about one" fair and makes the landing reveal land harder.

6. **[0:43–0:47][Audio/Clarity] Fix the garden path.** Replace "Cutting the alphabet in half prices every character alike" with "Halving the alphabet charges every character the same."

7. **[1:35–2:07][Visual] Make "rare ones narrow and tall" visible.**
   - Add a 10× zoom inset of the last 1.5% of the x-axis (Q, J, X, Z) above-right of the skyline, connected by a thin grey bracket.
   - Label the tallest column "Z 10.3" in yellow. Keep it while "rare ones narrow and tall" plays (1:38–1:41).
   - Do not fake the widths; the area meaning must hold.

8. **[1:31–2:27][Visual] Make p blue everywhere.**
   - Build f2/f3/f4 with `MathTex(..., r"\log_2", r"\frac{1}{", "p", "}")`, or use `substrings_to_isolate=["p"]`.
   - Colour the p in the denominator BLUE so it matches the palette's "every p" rule.

9. **[2:21–2:27][Motion] Remove the lag.**
   - Morph directly from the after-Q layout to the after-TH layout. Drop the intermediate return to no context (scene.py lines 640–643), or give it 0.4 s max.
   - Then E's widening and H falling land on "two thirds" and "one point seven" instead of about 1.5 s late.

10. **[0:26.8–0:28.4][Motion] Clean up the cut to the chart.**
    - FadeOut the chain and "log2 27 ≈ 4.75" (or `TransformFromCopy` the 4.75 into the dashed line's label) before the axes `Create`.
    - Remove the stray yellow tick and dot visible at the left at 0:27.0.

11. **[1:28.5–1:33][Audio] Add the missing verb.** "That makes k log base two of one over p" → "So k equals log base two of one over p."

12. **[0:21–0:26][Clarity] Say what 4.75 is.** "More exactly, it's log base two of twenty-seven" → "With perfect halving, the ideal is log base two of twenty-seven, about four point seven five."

13. **[2:49–2:56][Originality] Trim the "X, not Y" tic.** Rephrase one of the two antitheses, for example: "That's a range from human guessers, and it measures predictability; meaning never enters."

## REACHES 9 IF ALL FIXED

Yes, plausibly. The structure is already right: a commit-to-5 cold open, a measured failure, an insight picture that turns into the formula, a real cited payoff, and a landing that re-sees the first frame. Fixes 1–2 only lift the caps (to about 7.7). Fixes 3–5 are what move Clarity and Hook to 9: guesses turned into bits on screen, the language-model stake paid off with a real 2023 number, and a fair setup. Fixes 6–9 are what move Visual to 9. No structural rewrite is needed.

## KEEP

1. The landing: the hidden character is Shannon's own Y from "the other day", guessed on the first try. Keep the THE OTHER DA fly-in to the cold-open row.
2. The E "what's still possible" strip doubling against the live counter, then p·2^k = 1 built from E's column and the counter. This is the episode's visual proof.
3. Real Brown-corpus data throughout: the same chart re-weighted by Q→U (98%, 0.16 bits) and TH→E (68%, 1.67), with the H counter and dashed line moving in sync.
