# Round 7 review: substance (facts, story, clarity, concision, slop)

Critic: independent science and story editor. I recomputed every number, re-derived the formulas and checked both sources on the web. Every dimension is scored.

Evidence used:
- `review/` pack. metrics.json (17:48) is newer than final.mp4 (17:46), so I reused it.
- report.md, transcript.txt, transcript_words.tsv, narration_diff.txt, narration.txt, script.md, facts.md and data.json.
- All 12 contact sheets.
- Full-resolution keyframes kf_01, 04, 07, 13, 18, 24, 27, 29, 31, 32, 37 and 39.
- Frames I extracted at 0:24.4, 0:53.4, 2:14.4, 2:24.6, 2:50.4 and 3:20.4, plus a 5 fps strip of 2:49.6–2:52.0 (the count flight).
- An independent Brown recount with my own tokenizer (not `data.py`): N = 5,751,046 (1 fewer, a trailing space), H₁ 4.1111, E/Z 130.28, top-5 48.34%, Q→U 98.14% (H 0.156), TH→E 68.33% (H 1.667), ␣∣HE 0.578, O∣E␣ 3.796, H(X∣2 prev) 2.8105. All of these match data.json.
- Web checks:
  - Shannon 1951 (princeton.edu PDF): "something of the order of one bit per letter"; "Out of 102 symbols the subject guessed right on the first guess 79 times…"; the identical-twin sentence; the N = 100 column reads upper 1.3 and lower .6.
  - LLMZip (arXiv 2306.04050v2 §IV / Table IV): "only 0.8426 bits/character", on the Gutenberg book of 25 May 2023.

```
EPISODE: 007 — "How Much Information Is in a Letter?"
IDEA: A character costs log2(1/p) yes/no questions, so the average cost (entropy, the area of a probability-wide, cost-tall skyline poured flat) falls from the 4.75 that halving the alphabet suggests toward about one bit once the guesser uses what came before.
SCORES: Hook 9 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 9 · Originality 9
WEIGHTED: 8.7   AFTER CEILING: 8.7 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none
FINAL: 8.7   PASS: no
```

Weighted = (15·9 + 25·8.5 + 15·8.5 + 15·8.5 + 10·8.5 + 10·9 + 10·9) / 100 = 867.5 / 100 = 8.7.

## FACTS

| Claim | Status | Source / check |
|---|---|---|
| 27 symbols; five cuts take 27→13→6→3→2→1 and end on Y | Verified | 2⁴ < 27 ≤ 2⁵; cut positions in kf_04 |
| log₂27 ≈ 4.75 ("the ideal") | Verified | 4.7549 |
| Shannon 1951: true figure "about one" | Verified | BSTJ 30(1), p. 50, "of the order of one bit per letter" (web, this round) |
| No compressor beats it on average; LMs are trained on next-symbol prediction | Verified | source-coding theorem; standard objective |
| "Four of every five questions": 3.75 extra (79%) | Verified | 3.7549/4.7549 = 0.790 |
| Z costs as much as E (4.75 each under halving); E is 130× as frequent; 10.3% / 0.08% | Verified | my recount: 0.103137/0.000792 = 130.3 |
| Space, E, T, A, O are "nearly half" (48%) | Verified | 48.34% |
| E "near a tenth", 3.3 doublings; Z is 1 in 1260 and needs 10.3 | Verified | log₂(1/0.1031) = 3.28; 1/p = 1263; log₂ = 10.30 |
| p·2ᵏ = 1 ⇒ 2ᵏ = 1/p ⇒ k = log₂(1/p); average = Σ p log₂(1/p) = area (Σp = 1) | Verified | re-derived |
| H₁ = 4.11 bits for English letters (Brown, on screen) | Verified | recount 4.1111 (Shannon's own F₁ is 4.03 from older tables; the on-screen label is Brown, so this is fine) |
| "Four times Shannon's estimate" | Verified | 4.11 / ≈1 |
| After Q: U 98%; H = 0.16 | Verified | recount 0.9814; 0.156 |
| After TH: E two-thirds, ≈ half a question; average 1.7 | Verified | 0.6833; 0.549; 1.667 |
| Run E ␣ O after T H: 0.5 + 0.6 + 3.8 = 4.9 → 5; one at a time 1 + 1 + 4 = 6 | Verified | recount 0.549 + 0.578 + 3.796 = 4.923; ⌈4.923⌉ = 5 is a valid Shannon-code length for 3-letter blocks (Kraft holds); per-letter whole questions ≥ ⌈cost⌉ = 1, 1, 4. **Clarity caveat:** the costs are conditioned on TH, HE and E␣, and only TH is shown (fix 1) |
| Average over every two-letter context 2.8 | Verified | recount 2.8105 |
| 27² = 729; 27¹⁰⁰ ≈ 10¹⁴³; Brown 5.75 M characters | Verified | log₁₀ 27¹⁰⁰ = 143.14 |
| "Hundred-letter contexts need more text than any corpus holds" | Verified | literal count is 10¹⁴³; even at ~1 bit/char, ~10³⁰ plausible contexts far exceed any corpus |
| Subject guesses until right; 79 of 102 on the first guess | Verified | p. 56 (web); record tally 79/8/3/2/2/3/1/1/1/1/1 = 102 (data.json, re-counted) |
| A twin could rebuild the passage from the counts | Verified | p. 55, "identical twin" (web) |
| Guess-count skyline: log₂(1/q₂) = 3.67; pours to ≈ 1.42 (upper estimate) | Verified | log₂(102/8) = 3.672; −Σ q log₂ q = 1.4223 |
| "A better guesser could only lower it" | Verified (as a statement about the ideal predictor) | majorisation + Schur-concavity (facts #27) |
| N = 100: 0.6–1.3 bits | Verified | p. 64 table, column 100 (web) |
| LLMZip 2023: 0.84 bits/char on part of a book that reached Gutenberg after training, 27 symbols | Verified | arXiv 2306.04050v2 §IV, Table IV: 0.8426 (web, this round) |
| The hidden Y took Shannon's subject 1 guess; halving took 5 | Verified for this letter | record line 3, Y = 1; the chain at 0:13–0:21 |

No wrong, fabricated or misattributed claims. Every empirical claim has an on-screen citation:
- Shannon 1951 at 0:25–0:37 and 2:33–3:09.
- Brown at 0:41–2:31.
- Valmeekam et al. 2023 at 3:11–3:19.

## MECHANICS

```
runtime 3:34.2 · wpm 152 (speech time; 143 overall) · max silence 2.23 s (1:49.5, planned Q prediction hold) · max static 3.33 s (closing hold) · −14.0 LUFS / −2.1 dBTP
```

- Leading silence 0.00 s, trailing 0.88 s. No black frames. Layout audit: 0 issues in 218 checks. WER 1.4%.
- ASR diffs are benign. "a"→"one" is number formatting. The dropped "hundred" at 1:02.8 comes back as "1260". The inserted "zero" is "point six" written as 0.6. "Y"→"why" is a homophone.
- The 1:40–1:54 segment text looks garbled, but the word timings show every word was spoken: "That beats 4.75, but it's four times Shannon's estimate."
- No cap is triggered.
- Pace flags (report): 2 sentences run above 200 wpm.
  - 3:19.6, 208 wpm: the landing reveal, "The hidden character from the start is the Y…".
  - 2:57.3, 203 wpm: "A better guesser could only lower it."
- The longest stretch without a breath is 11.5 s, at 3:07.5 (the LLM sentence).

## TRANSCRIPT / SLOP

- 0 banned phrases.
- No "it's not just X" construction.
- No question chains. The questions at 0:07, 0:37, 1:49 and 3:26 each stand alone, and each gets an answer.
- No signposting, fake reveals or empty superlatives. The ending is not a recap.
- "split the probability, not the alphabet" and "five questions for these three, not six" are concrete contrasts, not the banned pattern.
- The voice stays noun-heavy and visual ("U swallows the bar", "Pour the skyline flat").

The hook works:
- The question is spoken by 0:07.5, followed by a 2.1 s hold.
- "The natural answer is five" commits the viewer at 0:10.
- The reversal ("about one") comes at 0:25.
- The landing puts the Y in the ? box (3:23), which re-sees frame one exactly.

The cut from 607 to 496 words removed slack without losing a step. I can no longer find a sentence whose removal costs nothing, so Concision gets 9.

## STORY / CLARITY NOTES (what still stalls a careful viewer)

1. **2:11–2:20: the run's bill contradicts the chart it sits on.** The bill reads E 0.5, ␣ 0.6, O 3.8 over the dimmed after-TH skyline (kf_24). In that skyline the ␣ column (leftmost, 0–9%) stands about 3.5 bits tall, and O stands about 4.9. The bill's ␣ and O costs are conditioned on **HE** and **E␣**, and nothing on screen says so. The row shows only T H highlighted in purple. A viewer who checks the bill against the bars finds two of three numbers that disagree, at the episode's hardest conceptual step.
2. **3:01–3:19: "person" 1.42 sits outside Shannon's 0.6–1.3 band, and nobody says why** (kf_37). The narration goes straight from "a better guesser could only lower it" to "with 100 letters of context… 0.6 and 1.3". The reason (one 102-letter passage, whose early letters had little or no context) is in facts #26 but not in the video.
3. **2:53: "log₂(1/q) = 3.67" floats right of the tallest columns** (kf_31). Those columns are about 6.7 bits tall. The number belongs to the 2nd-guess column, about 0.6 units to the left. Nothing connects the two.
4. **3:07–3:19: the LLM sentence is a garden path.** "…a book that reached Project Gutenberg after its training needed .84 bits…" (11.5 s, no breath). "Its" can be read as the book's.
5. **3:19.6: the payoff line is the fastest sentence in the episode** (208 wpm). "The hidden character from the start is the Y in the other day" is the moment the opening is re-seen, and it is rushed.

## FIXES (highest impact first)

1. **[2:11–2:20][Clarity] Show each run cost's context.**
   - As each cost appears, flash its two-letter window in the row in purple: T H for E, H E for ␣, E ␣ for O. A purple bracket under the two boxes slides one box right per letter.
   - Write a small purple tag (`Text` 22) under each cost: "after TH", "after HE", "after E␣".
   - Optionally dim the TH skyline to 0% (not 25%) while the bill is up, so the bill cannot be read against the wrong bars.
   - No narration change.
2. **[2:57–3:19][Clarity] Explain the 1.42 vs the band without new words.**
   - Under "≈ 1.42 / upper estimate" at 2:59, add a grey `Text` 22 tag: "one passage · context 0–101".
   - On the payoff line, change the 1.42 tag from "person" to "person, 102 letters".
   - If a spoken clause fits the budget, use "A better guesser, or longer context, could only lower it." (+4 words).
3. **[3:07–3:19][Audio/Clarity] Split the LLM sentence.**
   - New text: "In 2023, a language model compressed part of a book posted to Project Gutenberg after the model was trained. It needed point eight four bits, inside that range."
   - Put a `[pause 0.4]` after "trained", and re-cue the note and marker to the new word times.
   - About +3 words; pay for them with fix 6.
4. **[3:19.6–3:23][Audio] Slow the reveal.**
   - Insert `[pause 0.5]` after "from the start".
   - Set this one sentence to speed 0.78, so it lands near 160 wpm instead of 208.
   - The Y should still drop into the ? box on the spoken "Y".
5. **[2:53][Visual/Clarity] Attach 3.67 to its column.** Move "log₂(1/q) = 3.67" directly above the 2nd-guess column (buff 0.2). If that spot is crowded, keep it where it is but draw a grey leader from the label to the 2nd column's top edge, and flash that column's outline as the value is copied.
6. **[2:57.3][Audio] Ease "A better guesser could only lower it" (203 wpm).** Add a `[pause 0.3]` before it and drop "only" if the budget needs the word for fix 3. ("A better guesser could lower it" keeps the meaning; the down arrow carries "only".)
7. **[2:50.0–2:51.0][Motion] Count flight still crosses the stationary counts.**
   - At 2:50.4 the 1s from lines 1–2 stream through line 3's letters and its counts; at x ≈ 900 a flying 1 overlaps a resting 1, reading "1̶1".
   - Option A: drop the non-1 counts to 30% for the duration of the ones' flight.
   - Option B: route lines 1–2 out to the left margin (x < −6.0), then down, then into the column foot, so no path crosses line 3.
8. **[2:57–2:59][Visual] "≈1" with no visible band.** The band sits behind the poured guess stack, so only its 0.6 edge shows (kf_32), and the green "≈1" label points at nothing. Raise the band above the stack at 40% fill, or outline its top edge at 1.3 in green above the stack.
9. **[2:29–2:31][Visual] Crowded frame** (kf_27): three dashed levels with labels, "all two-letter contexts", "1.81 extra", two grey lines of context arithmetic, and the TH tag. When "possible contexts" is written, fade the meter and "all two-letter contexts" to 30%, so the arithmetic is the one focal point.

## REACHES 9 IF ALL FIXED: yes

- Fixes 1, 2, 3 and 5 take Clarity to 9.
- Fixes 3, 4 and 6 take Audio to 9.
- Fixes 5, 8 and 9 take Visual to 9.
- Fix 7 takes Motion to 9.

That gives 135 + 225 + 135 + 135 + 90 + 90 + 90 = 900, which is **9.0**.

No structural change is needed. The episode has the hook, the measured failure, a picture that becomes the formula, a sourced payoff and a landing that re-sees frame one, and the facts are clean. The margin is thin, so none of these fixes may push runtime past about 3:38.

## KEEP

1. The skyline **pour**: probability-wide, cost-tall columns collapsing into the level (4.11 → 0.16 → 1.67 → 1.42). The animation is the argument.
2. The **context row and the Y**: the cold-open row, the halving chain planting Y at 0:17, the row reading along with Shannon's subject, and Y landing in the ? box.
3. **Shannon's real record** under a cursor with the 79/102 tally and the twin line, plus the live gap meter (3.75 → 3.11 → 1.81 → 0.42 extra) feeding the tagged bits-per-character line.
