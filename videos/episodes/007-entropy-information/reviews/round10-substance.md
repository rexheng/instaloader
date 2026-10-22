# Round 10 review: substance (facts, story, clarity, concision, slop)

Critic: an independent science and story editor. I did not make this video. I recomputed every number, re-derived every formula, checked the citations on the web and scored every dimension under BAR §7.

## Evidence

**Review pack.** `review/metrics.json` (22:14) is newer than `final.mp4` (22:12), so I reused `review/` rather than building a new pack. I read:
- `report.md`, `transcript.txt`, `transcript_words.tsv`, `narration_diff.txt`, `metrics.json`
- `narration.txt`, `script.md`, `facts.md`, `data.json`, and the round-9 entries of `CHANGELOG.md` and `reviews/round9-substance.md`

**Frames.**
- All 12 contact sheets.
- Full-resolution keyframes kf_01 (0:03.6), kf_06 (0:33.6), kf_08 (0:42.7), kf_14 (1:09.1), kf_16 (1:27.0), kf_19 (1:44.8), kf_22 (1:59.1), kf_25 (2:17.4), kf_27 (2:27.6) and kf_29 (2:42.8).
- Frames I extracted myself: 0:28.6 (the new "floor" ghost), 2:18.6 (bill exit), 2:29.2 and 2:31.2 (context arithmetic), 2:49.6 (count sort), 3:09.0 (LLM marker waiting) and 3:21.6 (landing).
- Two 0.4 s strips:
  - 2:15.6–2:18.4: the bill's "one at a time" row and its exit.
  - 2:50.4–2:53.2: the guess skyline, log₂(1/q) = 3.67, and the pour.

**Independent Brown recount.** I wrote my own tokenizer (scratchpad `ep7r10/recount.py`, which reads `brown.zip` directly and does not use `data.py`). It found:
- N = 5,751,046 characters (`data.json` has 5,751,047; that is a trailing-space difference) and 1,005,119 words.
- H₁ = 4.1111. E 10.314 %, Z 0.0792 %, E/Z = 130.28, 1/p(Z) = 1263.1.
- Top five = 48.34 %.
- After Q: n = 5,103, U 98.14 %, H = 0.156.
- After TH: n = 134,673, E 68.33 %, cost 0.549, H = 1.667.
- ␣∣HE: n = 123,249, p 0.6697, cost 0.578. O∣E␣: n = 203,030, p 0.0720, cost 3.796.
- H(X∣1 previous) = 3.3811 and H(X∣2 previous) = 2.8105.

**Shannon's record** (from `data.json`, checked against the ucalgary and princeton copies of the paper, below):
- 102 symbols, 198 guesses. Counter {1: 79, 2: 8, 3: 3, 4: 2, 5: 2, 6: 3, and one each of 7, 8, 11, 15, 17}. That is "the second eight times, the third three times, the fourth and fifth twice each, … only eight" above five.
- −Σ q log₂ q = 1.4223. log₂(102/8) = 3.672 and log₂(102/79) = 0.369.
- Y in THE OTHER DAY has a guess count of 1.

**Run bill.**
- 0.683 × 0.670 × 0.072 = 0.032948 → 0.0329, and log₂(1/0.0329) = 4.926 → 4.93.
- The costs: log₂(1/0.683) = 0.550, log₂(1/0.670) = 0.578 and log₂(1/0.072) = 3.796. Their sum is 0.55 + 0.58 + 3.80 = 4.93, and ⌈4.92⌉ = 5. One at a time, ⌈cost⌉ gives 1 + 1 + 4 = 6.

**Other arithmetic.**
- log₂ 27 = 4.755.
- 3.75 / 4.75 = 0.789 ("four of every five").
- log₂(1/0.1031) = 3.28 and log₂ 1263 = 10.30.
- 27² = 729 and log₁₀ 27¹⁰⁰ = 143.14.
- The derivation re-derives: p·2ᵏ = 1 ⇒ 2ᵏ = 1/p ⇒ k = log₂(1/p). Because the widths sum to 1, Σ (width × height) is the expectation, so pouring the skyline flat gives E[log₂ 1/p] = H.

**Web checks.**
- Shannon 1951, princeton.edu PDF:
  - "in ordinary literary English, the long range statistical effects (up to 100 letters) reduce the entropy to something of the order of one bit per letter"
  - "Out of 102 symbols the subject guessed right on the first guess 79 times"
  - The table "Upper and lower experimental bounds for the entropy of 27-letter English", column 100: upper 1.3, lower .6
  - "possible … to recover the first line from the second"
- LLMZip, arXiv 2306.04050v2 §IV: "we also tested the performance of LLaMA-7B on a recently released (May 25, 2023) book [7] under Project Gutenberg. The compression ratio for LLaMA with arithmetic coding is only 0.8426 bits/character". The Table IV row is M = 511, N_c = 508,463, ρ_LLaMA+AC = 0.8426. The authors are Valmeekam, Narayanan, Kalathil, Chamberland and Shakkottai, 2023.

```
EPISODE: 007 — "How Much Information Is in a Letter?"
IDEA: A character costs log₂(1/p) yes/no questions, so the average (a probability-wide, cost-tall skyline poured flat) depends on how predictable the next letter is, and with context English falls from the 4.75 that halving the alphabet suggests to about one bit.
SCORES: Hook 9 · Clarity 9 · Visual 9 · Motion 8.5 · Audio 9 · Concision 9 · Originality 9
WEIGHTED: 8.9   AFTER CEILING: 8.9 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none
FINAL: 8.9   PASS: no
```

Weighted = (15·9 + 25·9 + 15·9 + 15·8.5 + 10·9 + 10·9 + 10·9) / 100 = 892.5 / 100 = 8.9 (8.925 rounds to 8.9).

## FACTS

| Claim (spoken / shown) | Status | Source / my check |
|---|---|---|
| 26 letters + space = 27 symbols | Verified | Shannon 1951 (27-letter English) |
| Halving: 27 → 13 → 6 → 3 → 2 → 1, five cuts, ending on Y | Verified | 2⁴ < 27 ≤ 2⁵. Sheet 1 at 0:13–0:17 keeps O…␣ (13), then V…␣, …, Y |
| "The ideal is log base two of 27: 4.75" | Verified | 4.7549 |
| Shannon (1951) put the true figure "at about one" | Verified | "of the order of one bit per letter" (web) |
| "No compressor beats it on average" (it = the true figure); "floor" ghost at ≈1 | Verified | Source-coding theorem. The ghost is drawn at 1.0 on the 0–5 axis (f 0:28.6). |
| "Guessing what comes next is how language models are trained" | Verified | The next-token objective. It is definitional, so no citation is needed. |
| "3.75 extra (79%)"; "four of every five questions" | Verified | 3.75/4.75 = 0.789 |
| E 10.3 %, Z 0.08 %, ×130 | Verified | My recount: 10.314 %, 0.0792 %, 130.28 |
| Space, E, T, A, O "nearly half" (48 %) | Verified | 48.34 % |
| E "near a tenth"; 3.3 doublings | Verified | 3.277 |
| Z "one in 1260" needs 10.3 | Verified | 1/p = 1263 (3 s.f. 1260); 10.30 |
| p·2ᵏ = 1 → 2ᵏ = 1/p → k = log₂(1/p) | Verified | Re-derived; each step is shown on its words (1:09–1:19) |
| The widths add to 1, so area = average; the pour | Verified | Definition of the expectation |
| H = 4.11 bits (Brown, labelled) | Verified | 4.1111 |
| "Four times Shannon's estimate" | Verified | 4.11 / ≈1 |
| After Q: U 98 %, average 0.16 | Verified | 98.14 %; 0.156 |
| After TH: E two thirds, "about half a question"; average 1.7 | Verified | 68.33 %; 0.549; 1.667 |
| Run E␣O: 0.683 × 0.670 × 0.072 = 0.0329, log₂(1/0.0329) = 4.93 = 0.55 + 0.58 + 3.80 → 5; one at a time 1 + 1 + 4 = 6 | Verified | Recomputed (above). The chain rule for a second-order model, plus a Shannon code ⌈4.92⌉ = 5. |
| Every two-letter context: 2.8 (screen 2.81, "H averaged over contexts", "1.81 extra") | Verified | H(X∣2) = 2.8105, my recount |
| 27² = 729; 27¹⁰⁰ ≈ 10¹⁴³; Brown 5.75 M characters | Verified | 143.14; 5,751,046 |
| Subject guesses until right; 79 of 102 on the first guess | Verified | Shannon 1951 (web) |
| A twin could rebuild the passage from the counts | Verified | Shannon 1951 ("recover the first line from the second"; identical twin) |
| Guess skyline log₂(1/q) = 3.67; pours to ≈ 1.42; "upper estimate"; "context 0–101" | Verified | 1.4223 and 3.672 recomputed. It is a plug-in estimate of eq. 17's upper bound, honestly labelled. |
| "That caps the text; more context or a better guesser could only lower it" | Verified | The upper bound holds for any predictor (§6). Eq. 11 covers more context; ideal ranking majorises any other guesser's distribution, and entropy is Schur-concave. |
| Shannon, 100 letters of context: 0.6–1.3 bits | Verified | Table column 100 (web) |
| LLM, part of a 1924 book posted to Gutenberg after training: 0.84 bits; 27 symbols | Verified | LLMZip §IV and Table IV, 0.8426 (web); Gutenberg 25 May 2023; LLaMA Feb 2023 |
| The hidden character is the Y in "the other day"; one guess | Verified | Record line 3: … D 1, A 1, Y 1 |
| On-screen citations | Verified | "Shannon, 1951 · Bell System Technical Journal"; "Letter counts: Brown Corpus (Francis & Kučera, 1964)"; "Valmeekam et al., 2023 · arXiv:2306.04050 (LLMZip), Table IV · 27 symbols" |

No claim is Wrong, Fabricated or Unverifiable.

## MECHANICS

| Metric | Value | Status |
|---|---|---|
| Runtime | 3:34.6 | ok |
| Pace | 151 wpm over speech time (143 overall) | ok |
| Longest internal silence | 2.01 s (0:07.4, the planned prediction hold) | ok |
| Leading / trailing silence | 0.00 s / 0.56 s | ok |
| Longest static stretch | 3.03 s (3:31.6, the closing hold) | ok |
| Loudness / true peak | −14.1 LUFS / −1.7 dBTP | ok |
| Black frames | 0 | ok |
| Banned phrases | 0 | ok |
| WER | 1.2 % | ok |
| Layout audit | 0 issues | ok |

No mechanical cap triggers.

## Step notes

**1. Script, read cold.**
- The idea fits in one sentence (above).
- The beats follow BAR §6:

| Beat | Time | What happens |
|---|---|---|
| Cold open | 0:00–0:09 | Puzzle, then a 2.0 s hold |
| Naive build | 0:09–0:22 | Five cuts, log₂ 27 |
| Stakes | 0:22–0:34 | ≈1, floor, LLM |
| Fail | 0:34–0:43 | 3.75 extra; Z priced like E at 1/130 the frequency |
| Insight | 0:43–1:47 | Strips, k = log₂(1/p), skyline, pour, 4.11 |
| Context | 1:48–2:26 | 0.16, 1.67, the run bill, 2.81 |
| Payoff | 2:27–3:18 | The person, 1.42, 0.6–1.3, LLM 0.84 |
| Landing | 3:19–3:34 | Frame one re-seen with the Y |

**2. Fact-check.**
- Every number reproduces, both web sources check out, and every formula re-derives.
- One nitpick, not a defect: "27¹⁰⁰ ≈ 10¹⁴³" counts every possible string, which overstates the corpus problem. Even typical strings, about 2^(100·H), number ≥ 10³⁰, so the spoken claim "more text than any corpus holds" stays true.

**3. Mechanics.** All within the bar.

**4. Transcript and slop.**
- I found none of the §4 phrases, no "not just X" construction and no question chain. "So where do four of every five questions go?", "What comes after a Q?" and "is it Y?" each stand alone.
- The colons are explanatory pauses, not fake reveals.
- The ending reframes the cold open rather than recapping it.
- The hook question is complete at 0:07.2 and the likely-wrong "five" lands at 0:10.
- Two narration-vs-transcript differences point at the ear, not the text:
  - "so E's share doubles" is heard as "ease share doubles" (0:56.5).
  - "Z, one in twelve hundred sixty" is heard as "Z one and 1260", with "in" dropped (1:01.3–1:02.0).
  - The screen carries both (the E strip, "1/1260"), so these are nitpicks.

**5. Contact sheets.**
- Narration and picture match within ±2 s throughout. For example:
  - "130 times" at 0:41: ×130 between the leaders.
  - "U swallows the bar" at 1:55.
  - "costs add" at 2:13.
  - "79 of 102" at 2:39.
  - "point eight four" at 3:17: the marker lands at 0.84.
- Objects persist: the context row, the tiles that become column feet, the poured stacks, the levels and the payoff markers.
- Every round-9 visual fix holds:
  - The LLM marker waits over its own place as "LLM / ? / ▼" (3:09–3:15, f 3:09.0); nothing stacks on 1.42.
  - The bill leaves before the after-TH axes return (f 2:18.6).
  - The guess-chart band is two 5 px green edges past the stack (2:55–2:59).
  - The context arithmetic is written over a 25 % chart (f 2:29.2, f 2:31.2).
  - "bits per character" sits in its own centred row (3:03).
  - The "floor" ghost stops at ≈1 (f 0:28.6).
- **New finding: two key comparison frames are not held long enough to read** (strips 2:15.6–2:18.4 and 2:50.4–2:53.2).
  - **(a) The bill's punchline row.** "1 + 1 + 4 = 6 · one at a time" completes at about 2:16.8. The whole bill fades on "After" at about 2:17.6, so the "5 vs 6" comparison is complete on screen for about 0.9 s. §5 asks for ≥ max(1.5 s, 0.8 + 0.3 s/word). "Not six." ends at 2:17.0, and the next sentence starts 0.3 s later with no act-turn pause.
  - **(b) The guess skyline.** The new chart gets its labels (1st / 2nd / 3rd+, "share of guesses") at about 2:50.6. "log₂(1/q) = 3.67" is complete only from about 2:51.4 to 2:52.2, because the pour starts at 2:52.0 and the label leaves with its columns.
    - The equation is readable for about 0.8 s against §5's ≥ 2 s + 0.4 s/term.
    - The fully labelled chart is readable for about 1.4 s.
    - This equation is never spoken ("the same skyline pours flat…"), so the viewer must read it.
    - It is the one visual proof that the guess counts go through the same formula.

**6. Keyframes.**
- No clipping or overlap, and the safe area is respected (citations at y ≈ 940 px).
- LaTeX is clean ("Kučera", "␣", log₂, 10¹⁴³).
- Each frame uses ≤ 4 hues plus greys, and the palette holds for the whole episode: blue p, yellow questions/bits, green Shannon, purple context, grey reference, ink LLM.
- The axes carry quantity names ("questions" → "bits", "share of text / after Q / after TH", "share of guesses", "bits per character").
- The densest frame is the run bill (kf_25, 14 numbers in four rows). It is built term by term on its words and is the one focal point once the chart steps out, so it does not read as a slide.

## Dimension notes

- **Hook 9.**
  - The concrete puzzle is in frame 1, followed by the question, a 2.0 s hold and the plausible wrong answer "five" (0:00–0:10).
  - The gap meter keeps the tension rising: 3.75 → 3.11 → 1.81 → 0.42 → inside the band.
  - The landing re-sees frame one with the actual Y (3:21–3:34).
  - The stakes line now has a picture (the floor ghost, 0:27–0:30).
- **Clarity 9.**
  - Concrete first, with every algebra step on its words. The 1.42 cap and "more context" are now argued (2:54–3:00), and every number checks.
  - The two short holds (above) are scored under Motion, because the narration carries the content in (a). In (b) it hurts clarity a little too, since the 3.67 correspondence is only on screen.
- **Visual 9.** All three round-9 issues are fixed (above). Every frame I checked has one focal point, and nothing needs removing.
- **Motion 8.5.**
  - The pours (1:27–1:31, 1:55–1:58, 2:53–2:55), the count sort bottom row first (f 2:49.6), the 2 dipping under the "=" (1:15–1:18) and the LLM drop straight onto 0.84 (3:15–3:17) all encode relations.
  - But the anchor's "reading time respected" fails twice, at the two places where a comparison is the point: the bill's 6 row (about 0.9 s) and the guess skyline's equation (about 0.8 s) and labelled chart (about 1.4 s).
- **Audio 9.**
  - 151 wpm, −14.1 LUFS, −1.7 dBTP.
  - The act turns run about 0.8 s against 0.38 s ordinary gaps, and the results get 1.1–1.4 s holds (1:38.8, 1:58.4, 2:42.0).
  - Both deictics land.
  - The "ease share" and "one and" hearings are nitpicks.
- **Concision 9.** There are 499 words. Each beat buys a distinct number on the path 4.75 → 4.11 → 2.81 → 1.42 → 0.84. The repeats ("log base two of", "four point seven five", "two to the k") are deliberate callbacks.
- **Originality 9.** The poured skyline, used on four distributions, is the memorable image. Shannon's own passage and twin argument, and the post-training Gutenberg book, are real, non-obvious material.

## FIXES (highest impact first)

1. **[2:50.4–2:52.2][Motion/Clarity] The guess skyline and "log₂(1/q) = 3.67" pour away before they can be read.**
   - **Problem:** the equation is complete for about 0.8 s and the labelled chart for about 1.4 s before the pour starts at 2:52.0 (strip 2:50.4–2:53.2).
   - **Change:** split the sentence so the picture gets its own beat: "Treat each count as a symbol: [pause 1.2] the same skyline, [pause 1.0] poured flat, sits at about one point four bits." (+1 word, about +1.2 s).
     - Write "log₂(1/q) = 3.67" during the existing 1.2 s pause, as soon as the columns stand.
     - Flag it on "same skyline".
     - Start the pour on "poured", so the equation is held for ≥ 2.5 s and the labelled chart for ≥ 3 s.
   - This lifts Motion to 9.
2. **[2:16.8–2:17.7][Motion] The bill's punchline row, "1 + 1 + 4 = 6 · one at a time", is on screen for about 0.9 s.**
   - **Problem:** the bill fades on "After" (2:17.6), 0.3 s after "not six." ends.
   - **Change:** add `[pause 0.8]` after "five questions for these three, not six." (an act turn, as at the other turns). In that pause, flag the 5 and the 6 together (white outline, 0.6 s). Start the bill's 0.45 s exit only on "After".
   - This gives a ≥ 1.7 s hold for the comparison and about +0.8 s of runtime.
3. **[0:56.5][Audio, nitpick] "so E's share doubles" is heard as "ease share doubles".**
   - **Change:** "so E doubles its share." (+1 word). This removes the E's/ease homophone and keeps the subject on the strip being pointed at.
4. **[1:01.3–1:02.0][Audio, nitpick] "Z, one in twelve hundred sixty" is heard as "Z one and 1260", with "in" swallowed.**
   - **Change:** "Z, one in every twelve hundred sixty, needs ten point three." (+1 word). Alternatively, render that clause at speed 0.78. Re-check that whisper hears "in".

Runtime after fixes 1–4: about 3:37, still inside 2:30–4:00. If the §13 budget target of 3:35 must hold, recover the time by trimming the 0.8 s act turn after "inside that range" (3:19) to 0.5 s.

REACHES 9 IF ALL FIXED: yes.
- Fixes 1 and 2 restore "reading time respected" and lift Motion to 9.
- That gives (15·9 + 25·9 + 15·9 + 15·9 + 10·9 + 10·9 + 10·9) / 100 = 9.0.
- No structural change is needed: the hook, the measured failure, the visual insight, the cited payoff and the reframing landing are all in place, and every number is correct.

KEEP:
- The poured skyline (area = average), reused for letters, after-Q, after-TH and the guess counts, with the formula assembled from its referents. It is the proof and the image people will remember.
- The measured gap meter (3.75 → 3.11 → 1.81 → 0.42 → inside the band), and the landing that turns frame one into THE OTHER DA[Y], "1 guess" against "5 questions".
- The sourcing discipline: Brown recounts that reproduce exactly, Shannon's own passage and twin argument, and LLMZip's post-training Gutenberg book with its caveat respected.
