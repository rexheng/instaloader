# Episode 7, review round 3 (substance critic: facts, story, clarity, concision, slop; all dimensions scored)

**Evidence.** I used the existing `review/` pack: metrics.json (19:32) is newer than final.mp4 (19:30). I read:
- report.md, narration_diff.txt, transcript.txt and transcript_words.tsv
- all 13 contact sheets
- full-resolution keyframes kf_01, 05, 09, 13, 19, 21, 26, 28, 31, 35 and 38
- extra ffmpeg frames at 0:53.5, 0:55.0, 0:56.3, 0:57.5 (plus a 2× crop of the Z/"0.08%" region), 2:31.5, 2:32.8, 2:33.8, 2:34.6, 3:51.0 and 3:52.2
- an audio RMS trace at 1:53.8–1:56.0
- script.md, narration.txt, facts.md, data.py, data.json and CHANGELOG.md

**Independent recomputation.** I wrote my own counter (not data.py) over the NLTK Brown corpus, reduced to the 27-symbol alphabet. It gives:
- n = 5,751,047; H₁ = 4.1111
- E/Z = 130.3; 1/p(Z) = 1263; log₂(1/p(Z)) = 10.30; log₂(1/p(E)) = 3.277
- top five (space, E, T, A, O) = 48.34 %
- after Q: n = 5,103, U = 98.14 %, cost 0.027, H = 0.156
- after TH: n = 134,673, E = 68.33 %, cost 0.549, H = 1.667
- H(X | 1 previous) = 3.381; H(X | 2 previous) = 2.810

From Shannon's 102-symbol record:
- tally 79/8/3/2/2/3/1/1/1/1/1
- plug-in guess-count entropy 1.4223 (Miller–Madow corrected 1.49, so "about 1.4" is fair)
- mean guesses per symbol 198/102 = 1.94

Arithmetic: log₂27 = 4.755; 3.75/4.75 = 78.9 %.

I also measured on-screen values against the axes:
- the 4.11, 1.67 and 2.81 levels and the X/J/Q/Z inset heights (9.23, 9.5, 10.1, 10.28) match the data to within 1 px
- the number-line markers sit at 1.42, 2.81, 4.11 and 4.75, and the band at 0.6–1.3, all exactly placed

**Web verification.**
- **LLMZip** (arXiv 2306.04050v2, HTML), §IV: "we also tested the performance of LLaMA-7B on a recently released (May 25, 2023) book … We extracted text that corresponds to 100,000 tokens … only lowercase letters and space … The compression ratio for LLaMA with arithmetic coding is only 0.8426 bits/character". Table IV, M = 511: ρ_LLaMA+AC = 0.8426, N_c = 508,463 characters. The authors are Valmeekam, Narayanan, Kalathil, Chamberland and Shakkottai (Texas A&M).
- **Shannon 1951** (Princeton mirror of BSTJ, January 1951, pp. 50–64): "something of the order of one bit per letter"; "Out of 102 symbols the subject guessed right on the first guess 79 times … on the second guess 8 times, on the third guess 3 times, the fourth and fifth guesses 2 each and only eight times required more than five guesses". The N = 100 bounds (upper 1.3, lower 0.6) match the p. 64 table.
- **Brown Corpus:** Francis & Kučera, Brown University, 1964 is the correct attribution.

```
EPISODE: 007 — "How Much Information Is in a Letter?"
IDEA: A character costs log₂(1/p) yes/no questions, so information is set by predictability rather than alphabet size; priced with the text before it, English needs about one bit per character, not the 4.75 that halving the alphabet suggests.
SCORES: Hook 8.5 · Clarity 8 · Visual 8 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.4 (127.5 + 200 + 120 + 127.5 + 85 + 85 + 90 = 835 / 100 = 8.35)   AFTER CEILING: 8.4 (lowest 8 + 2 = 10, not binding)
CAPS: none. I checked every number spoken and drawn and found no wrong value. Citations are on screen for Shannon (0:33–0:53, 2:53–3:25), Brown (0:55–2:53) and LLMZip (3:26–3:35). There are 0 banned phrases and no rhetorical-question chains. Mechanics are all inside the bar. The ending is a reframing line, not a recap. I considered a cap for the "0.08%" label floating over the space column (0:55–0:59, fix 3): the plotted data is correct but the label has no visible referent. I score it as a clarity defect rather than a factual error.
FINAL: 8.4   PASS: no
```

## FACTS

| Claim | Status | Source / check |
|---|---|---|
| The hidden character is one of 26 letters or a space (27 symbols) | Verified | Shannon 1951, p. 56 |
| Five halving cuts take 27 to 1 (on screen 27→13→6→3→2→1, ending on Y) | Verified | 2⁴ < 27 ≤ 2⁵; kf_05 |
| "Perfect fifty-fifty splits": ideal log₂27 ≈ 4.75 | Verified | 4.755; Shannon F₀ = 4.76 |
| Shannon (1951) estimated the true figure at "about one" | Verified | BSTJ 30(1), p. 50 |
| No text compressor can beat the true figure on average | Verified | Source-coding theorem; attached to the true rate, not to the estimate |
| Guessing what comes next is how language models are trained | Verified | Next-token cross-entropy objective; LLMZip §I |
| "4 of every 5 questions"; on screen "3.75 extra (79%)" | Verified | 3.75 / 4.75 = 0.789 |
| E turns up 130 times as often as Z; on screen 10.3 % and 0.08 % | Verified (recomputed) | 10.314 % / 0.0792 % = 130.3. The values are right, but "0.08%" is drawn over the space column (fix 3). |
| Space, E, T, A and O are nearly half of all text; on screen 48 % | Verified (recomputed) | 48.34 % |
| E near a tenth; 3.3 doublings | Verified (recomputed) | 0.1031; 3.277 |
| Z is 1 in 1,260 and needs 10.3 | Verified (recomputed) | 1263; 10.30 |
| p·2ᵏ = 1 ⇒ 2ᵏ = 1/p ⇒ k = log₂(1/p); area = Σ p log₂(1/p) = average | Verified (re-derived) | Σp = 1; definition of expectation |
| Inset X J Q Z "×32 wide", Z = 10.3 | Verified | Measured Z width ≈ 32 px against 1.02 px true. facts.md row 15 still says "×30" (a doc nit only). |
| Entropy of English letters = 4.11 bits | Verified (recomputed) | Brown, labelled on screen; Shannon's own 27-letter F₁ = 4.03 |
| "Still four times Shannon's estimate" | Verified | 4.11 / ~1 |
| "Shannon called that average the entropy, counted in bits" | Verified | Shannon 1948 uses both terms (bits credited to Tukey) |
| After Q: U 98 of 100; cost "almost nothing"; average 0.16 bits | Verified (recomputed) | 98.14 %; 0.027; 0.156 |
| After TH: E over two-thirds; "about half a question"; 1.7 | Verified (recomputed) | 68.33 %; 0.549; 1.667 |
| Averaged over every two-letter context: 2.8 | Verified (recomputed) | 2.810 |
| Protocol: the subject guesses each next character until right | Verified | pp. 55–56 |
| 79 of 102 on the first guess | Verified (web + record) | p. 56 |
| Guess-count skyline pours flat at about 1.4 bits/char | Verified (recomputed) | 1.4223, Shannon eq. 17 form. The step from guess counts to the text's information is not explained (fix 2). |
| "A better guesser could only lower it" | Verified | Holds if "better" means closer to the true-probability ranking (majorisation and Schur-concavity) |
| With 100 letters of context, Shannon put English at 0.6–1.3 bits/char | Verified | p. 64, N = 100 column |
| In 2023 a language model compressing a book in the same 27 symbols needed 0.84 bits/char, inside the range | Verified, with a wording nit | LLMZip Table IV, 0.8426. It is a 100,000-token (508,463-character) excerpt of the book, not the whole book (fix 14). |
| The hidden character is the Y of THE OTHER DAY, got on the first guess, "a single yes-or-no question" | Verified | Record line 3 ends D 1, A 1, Y 1. Literally true for this Y, though the subject averages 1.94 guesses per symbol on the passage. |
| "Splitting the alphabet took five" | Verified | The on-screen chain isolates Y on cut 5 |
| Citations: Shannon, 1951 · BSTJ; Brown Corpus (Francis & Kučera, 1964); Valmeekam et al., 2023 · arXiv:2306.04050 (LLMZip), Table IV | Verified | Author, year, venue and finding are all correct |

```
MECHANICS: runtime 3:52.4 · 162 wpm (speech time) · max silence 1.95 s (2:20.3, planned prediction hold) · max static 3.13 s (3:11.4, 3:42.3) · −14.0 LUFS / −2.1 dBTP · lead 0.00 s / trail 1.47 s · WER 2.1 % · 0 banned phrases · layout audit 0/204
```

## Story and clarity read (why it is 8.4 and not 9)

**Story.** The spine is strong:
- a concrete puzzle and a commit ("the natural answer is 5")
- a measured failure ("3.75 extra (79%)")
- the reason it fails (the same price for E and Z)
- one picture that becomes the formula (doubling strip → p·2ᵏ = 1 → k = log₂(1/p) → skyline area → pour → H)
- honest limits ("easy cases", 2.81)
- a real-world payoff (Shannon's own record, then LLMZip)
- a landing that re-sees the first frame (the Y lands in the ? box)

This is a 3b1b-quality structure. What holds it below 9 is a handful of conceptual gaps and frame-level misreads, not structure.

**1. Fractions of a yes/no question are never earned.** The hook literally asks "With yes or no questions, how many do you need per character?" Then the video prices U at "almost nothing" (2:28.6), E after TH at "about half a question" (2:37.8), and lands the headline at 0.6–1.3 and 0.84 bits per character, which is fewer than one yes/no question per character. Asked one character at a time, you can never use fewer than one question for a character that is not certain. Sub-one averages exist only when you ask about runs of characters at once, which is what arithmetic coding, and LLMZip, does. A sharp viewer hits this wall at 2:37 and nothing resolves it. The landing even sharpens the confusion: it celebrates "a single yes-or-no question" (3:42.9) as the best case, while the headline band sits mostly below 1. Stating this assumption takes one sentence, and the 9 anchor requires it ("assumptions stated").

**2. "Treat each guess count as a symbol" (3:05.3) is asserted, not argued.** Why should the entropy of guess counts measure the text's information? Shannon's answer is that an identical twin with the same predictor rebuilds the passage from the counts alone. Without that clause, the 1.42 arrives as a trick.

**3. "0.08%" points at the wrong column (0:55–0:59).** At 0:53.5, E and Z are isolated (bright, with E and Z axis labels). On "yet in real text" the widths become real, and two things happen:
- Every column returns to full brightness, so the isolation is lost.
- The axis keeps only A D E H I L N O R S T ␣ as labels, so Z is unlabelled and invisible as a ~1 px hairline at x ≈ 1367 (2× crop).

"0.08%" sits at x ≈ 1490–1600, directly above the space column, which is the widest column on the chart (17.5 %). A paused frame reads "space = 0.08%". The spoken "130 times" has no on-screen counterpart.

**4. "0.16" is in the equation for under 1 s.** The level is born at about 2:32.8. "= 0.16 bits" is copied into the equation at about 2:33.5 and is gone by 2:34.6, when TH arrives and the slot reverts to "?". That is less than the §5 1.5 s reading minimum, and it lands after the spoken "0.16" (2:32.4). By contrast, 1.67 holds from 2:44 to 2:51.

**Concision.** 599 words, and almost every sentence carries weight. The slack is small: the spoken "In the Brown Corpus," duplicates the on-screen citation, and so does "Whatever it is,". Those are the trims to fund fixes 1 and 2 under 4:00.

**Slop.** I found none. The voice is specific and physical: "U swallows the bar", "pour the skyline flat", "almost no letter arrives without a past". There is one "X, not Y" antithesis ("split the probability, not the alphabet"), but it is the episode's thesis and earned, so I did not penalise it.

**Hook.** The question lands at 0:13.1, just past the 0:12 anchor, and the first frame (kf_01) is 12 empty boxes and a "?", which says little before the narration does. "The natural answer is 5" is the narrator committing for the viewer. It works, but it is not irresistible.

## FIXES (highest impact first)

1. **[2:37–2:43, also 1:19][Clarity] Fractional questions are unexplained,** although the hook is literally about yes/no questions per character. Right after "Its cost shrinks to about half a question" (about 2:40), add: "Half a question sounds impossible, but ask about long runs of letters at once, as a compressor does, and the fractions add up." Visual: briefly bracket the after-TH skyline with a yellow "per run of text ÷ characters" note, ≤ 7 words, next to the 1.67 level. About 5 s. Optionally foreshadow at 1:19 with "three point three doublings, fractions included".
2. **[3:05.3–3:12.7][Clarity] Guess count → bits is unearned.** Before "Treat each guess count as a symbol", add: "Give a twin the same guesser, and these counts alone rebuild the passage." Visual: for 1.5 s, the letters dim to 15 % while the count row brightens; then the counts fly into the skyline as now. About 4 s.
3. **[0:55–0:59][Clarity/Visual] "0.08%" floats above the space column, and Z is unlabelled and invisible.**
   - Keep E and Z at full blue, and every other column at 35 %, through the width change until "130 times as often" ends (0:59.1).
   - Keep the E and Z axis labels.
   - Anchor "0.08%" above Z's hairline (x ≈ 82.4 % of the axis) with a 0.4-unit grey leader. Shift the label left of the "4.75" gutter label so they do not collide.
   - On "130", grow a blue "×130" between the two percentage labels.
4. **[2:32.4–2:35.5][Clarity/Motion] "= 0.16 bits" is held under 1 s and lands after the word.** Start the TransformFromCopy of the 0.16 level label on "falls to" (≈2:32.0) so it lands on "0.16". Delay the TH context switch and the "?" revert until ≥ 1.5 s after it lands (≈2:35.0; add a 0.6 s pause after "point one six bits" if needed).
5. **[0:00–0:13][Hook] The question lands at 0:13.1, and the first frame is empty boxes.**
   - Show the 27 tiles from frame 1, under the row.
   - Cut the spoken "one of twenty-six letters, or a space" (the tiles say it; put "26 letters + space" as a ≤ 5-word grey label).
   - Have the question end by about 0:08, followed by the 1.5 s hold.

   The viewer then commits by 0:10.
6. **[2:31–2:53][Visual] The y-axis stays 0–10 while every quantity is ≤ 2.81 (kf_28),** so about 70 % of the plot is empty and 0.16, 1.67, 2.81 and the band are squeezed into the bottom 100 px. Once U flattens (≈2:31), animate the axis to 0–5, with the 4.11 reference and band riding along.
7. **[1:49–1:55][Visual] The ×32 inset abuts the 100 % edge (kf_19),** so X J Q Z read as columns beyond 100 %. Add a 0.35-unit gap, a thin frame or its own baseline, and a dashed grey leader from the last four hairlines to the inset.
8. **[0:24.6–0:28.7][Motion] The log₂27 build is glyph soup** (the copied 27 overlaps "→ 13", a half-written "lo"; sheet 2, 0:25). Write "log₂" first, then TransformFromCopy the chain's 27 along an arc below the chain into its slot, then TransformMatchingTex "5" → "≈ 4.75". Centre the final line at x = 0.
9. **[1:00–1:02][Motion] The re-sort leaves black gaps,** and columns pass through each other (sheet 4, 1:01). Interpolate the left edges cumulatively so the columns tile 0–100 % in every frame (1.5 s, smooth).
10. **[1:11–1:43][Visual] The chart is "dimmed" behind the strips** but its letter labels, % ticks and yellow 4.75 line and label stay full strength (kf_13). Dim them to 30 % with the chart. Keep only E's column and its label bright as the strip's referent.
11. **[1:54.8][Audio] "questions" in "the average number of questions" is swallowed.** There is a plosive burst at 1:54.90, then 0.6 s of energy at about a third of the level; ASR drops the word. This is the key noun of the area sentence. Regenerate the line with the 0.2 s pause moved to after "questions" and lengthened to 0.35 s. Confirm that the WER delete disappears.
12. **[3:51.6–3:52.4][Motion/Landing] The 0.8 s series ident flashes in and steals the last beat.** Drop it and hold the landing frame (THE OTHER DAY Y, "1 guess", dimmed "5 questions") to the end, or move a ≤ 1.5 s ident to after the stakes beat (§6).
13. **[3:00–3:35][Visual] In row 3, "11 5" reads as "115"** (kf_31). Add a 0.08-unit gap after every two-digit count, or widen two-digit cells to 0.42.
14. **[3:24.3–3:28.0][Clarity/Concision] "compressing a book"** was a 100,000-token excerpt. Say "compressing a new book" (it was released after the model was trained, which is the point of using it), or "part of a new book". To fund fixes 1 and 2 under 4:00, cut the spoken "In the Brown Corpus," at 2:21 (the citation is on screen) and "Whatever it is," at 0:34.6, and drop the end ident (fix 12): together about −2.8 s. Fixes 1 and 2 add about 9 s, so the episode lands at about 3:58.5.

REACHES 9 IF ALL FIXED: yes, narrowly. Nothing structural is missing. The scores would move as follows:
- Fixes 1–4 move Clarity to 9.
- Fixes 3, 6, 7, 10 and 13 move Visual to 9.
- Fixes 4, 8, 9 and 12 move Motion to 9.
- Fix 11 moves Audio to 9.
- Fix 5 moves Hook to 9.
- Fix 14 moves Concision to 9.

That gives (135 + 225 + 135 + 135 + 90 + 90 + 90) / 100 = 9.0. There is no slack: if the hook fix is skipped, the episode tops out at about 8.9. Fixes 1–5 are the ones that matter.

KEEP:
- The doubling strips with live counters, which derive p·2ᵏ = 1 → 2ᵏ = 1/p → k = log₂(1/p) one legal step per spoken clause.
- The "pour": skyline area → full-width slabs → level line → value copied into H. It is reused for after-Q and after-TH with the "? bits" slot, and the honest "easy cases → 2.81" correction follows.
- Shannon's real record (cursor and live tally) → guess skyline → bits-per-character line → THE OTHER DAY flying into the cold-open row so that Y fills the ? box.
