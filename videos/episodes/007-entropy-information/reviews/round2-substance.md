# Episode 7, review round 2 (substance critic: facts, story, clarity, concision, slop)

**Evidence.** I used the existing `review/` pack, because metrics.json (15:25) is newer than final.mp4 (15:23). I read:
- report.md, narration_diff.txt and transcript.txt
- all 13 contact sheets
- full-resolution keyframes kf_03, 05, 07, 12, 14, 17, 21, 24, 30, 33 and 38
- extra ffmpeg frames at 0:31.0, 1:05.0, 1:46.0, 2:33.0, 2:41.5, 2:58.0 and 3:19.5, plus a crop of the formula at 1:33.2, 1:33.8, 1:34.4 and 1:35.0
- script.md, narration.txt, facts.md, data.json and CHANGELOG.md

**Independent recomputation.** I downloaded the NLTK Brown corpus and wrote my own counter, reducing the text to the same 27-symbol alphabet. It gives n = 5,751,047, H₁ = 4.1111, E/Z = 130.3, 1/p(Z) = 1263, log₂(1/p(Z)) = 10.30, log₂(1/p(E)) = 3.277, top-5 share = 48.34 %, U after Q = 98.14 % with H(·|Q) = 0.156, and E after TH = 68.33 % with H(·|TH) = 1.667. Every value matches data.json. I also computed what the episode does not show: averaged over all contexts, H(X | 1 previous char) = 3.38 and H(X | 2 previous chars) = 2.81. From the 102-symbol record, the guess-number entropy is 1.4223, with a tally of 79/8/3/2/2/3/1/1/1/1/1.

**Web verification.**
- Shannon 1951 (Princeton mirror of BSTJ 30(1):50–64): "something of the order of one bit per letter"; the 102-symbol record with "79 times" on the first guess; the 27-letter row F₀ 4.76, F₁ 4.03, F₂ 3.32, F₃ 3.1; and the N = 100 column, upper 1.3 and lower 0.6.
- LLMZip (arXiv 2306.04050; Valmeekam, Narayanan, Kalathil, Chamberland, Shakkottai; submitted 6 Jun 2023): 0.7101 bits/char on 1 MB of text8; 0.8426 on a 100 KB book text; the preprocessing gives "only lowercase letters and space"; and the authors' own caveat that the text8 results are "likely … optimistic" because LLaMA was trained on Wikipedia.

```
EPISODE: 007 — "How Much Information Is in a Letter?"
IDEA: A character costs log₂(1/p) yes/no questions, so its information is set by how predictable it is, not by the size of the alphabet; priced with the text that came before it, English needs about one bit per character, not the 4.75 that halving the alphabet suggests.
SCORES: Hook 8.5 · Clarity 7.5 · Visual 8 · Motion 8 · Audio 8 · Concision 8.5 · Originality 9
WEIGHTED: 8.1 (127.5 + 187.5 + 120 + 120 + 80 + 85 + 90 = 810 / 100)   AFTER CEILING: 8.1 (lowest 7.5 + 2 = 9.5, not binding)
CAPS: Factual/mathematical error on screen → 6.
  @2:29.3–2:38.5 the equation reads "H = Σ p log₂(1/p) = 0.16 bits" directly above the after-TH skyline, with the purple T H context boxes, the 68 % brace and the axis title "share after TH" (frame 2:33.0, kf_27 2:37.1). H for that distribution is 1.667, so the frame states a wrong value by 10×.
  @2:13.9–2:28.0 the equation reads "= 4.11 bits" over the after-Q skyline and "share after Q" (kf_24 2:23.6). H there is 0.156.
  Under §7 step 2, a number shown on screen is checked against what it labels: "H(after TH) = 0.16" is Wrong. I considered the reading "it is the last computed value and gets replaced on the pour", but nothing on screen marks it as stale, and a paused frame or screenshot teaches a false equation. The fix is one line per beat (fix 1).
  No other caps: mechanics are all in range, there are 0 banned phrases, the hook lands by 0:12, citations are on screen, and the ending is a reframing line.
FINAL: 6.0   PASS: no
FACTS:
- Hidden character is one of 27 symbols (26 letters + space) | Verified | Shannon 1951 p. 56, "an alphabet of 27 symbols"
- 5 halvings take 27 → 1 (on screen 27→13→6→3→2→1, ending on Y) | Verified | 2⁴ = 16 < 27 ≤ 32; kf_05 0:29.1
- log₂ 27 ≈ 4.75 (the "ideal" with perfect 50-50 splits) | Verified | 4.7549; Shannon F₀ = 4.76
- Shannon 1951 estimated the true figure at "about one" | Verified | BSTJ 30(1) p. 50, "of the order of one bit per letter"
- No text compressor can beat the true figure on average | Verified | source-coding theorem; attached correctly to the true entropy rate, not to the estimate
- Guessing what comes next is how language models are trained | Verified | next-token cross-entropy objective; LLMZip §I
- "4 of every 5 questions" wasted; on screen "3.75 extra (79%)" | Verified | 3.75/4.75 = 0.789 (against the ≈1 estimate)
- E turns up 130× as often as Z | Verified (recomputed) | 10.314 % / 0.0792 % = 130.3, Brown
- Space, E, T, A, O are nearly half of all text | Verified (recomputed) | 48.34 %
- E near a tenth; 3.3 doublings | Verified (recomputed) | p = 0.1031, log₂(1/p) = 3.277
- Z is 1 in 1260 and needs 10.3 | Verified (recomputed) | 1/p = 1263, log₂ = 10.30
- p·2ᵏ = 1 ⇒ k = log₂(1/p); area = Σ p log₂(1/p) = average | Verified (re-derived) | definition of expectation; Σp = 1
- Inset X J Q Z at true heights, ×32 wide, Z = 10.3 | Verified | X 9.25, J 9.53, Q 10.14, Z 10.30
- H of English letter frequencies = 4.11 bits | Verified (recomputed) | 4.1111, Brown and labelled as such; Shannon's own 27-letter F₁ is 4.03 from older tables
- "Still four times Shannon's estimate" | Verified | 4.11 / 1
- After Q: U 98 of 100; cost "almost nothing"; average 0.16 bits | Verified (recomputed) | 98.14 %; log₂(1/0.9814) = 0.027; H = 0.156
- After TH: E over two-thirds; ~half a question; 1.7 | Verified (recomputed) | 68.33 %; 0.549; 1.667
- On-screen "H = … = 4.11 bits" over the after-Q skyline (2:13.9–2:28) and "= 0.16 bits" over the after-TH skyline (2:29.3–2:38.5) | **Wrong** | the displayed distributions have H = 0.156 and 1.667 → cap 6
- The after-Q/after-TH numbers imply a short context gets you near 1 bit | **Misleading by omission** | the averages over all contexts are 3.38 (1 char) and 2.81 (2 chars) on the same Brown text (Shannon F₂ 3.32, F₃ 3.1); Q and TH are the best cases, and the episode never says so
- Shannon's protocol: guess until right | Verified | pp. 55–56
- 79 of 102 on the first guess | Verified | p. 56 "Out of 102 symbols … 79 times"; the record on screen reproduces the 79/8/3/2/2/8 tally
- The guess-number skyline pours flat at ~1.4 bits/char | Verified (recomputed) | 1.4223; this is Shannon eq. 17's upper-bound form on one passage, and "about" is appropriate for n = 102
- "A better guesser could only lower it" | Verified (with a caveat) | the ideal predictor's guess distribution majorises any other's, so it minimises −Σq log q; "better" in the sense of closer to the ideal ranking
- With 100 letters of context, Shannon put English at 0.6–1.3 | Verified | p. 64 table, N = 100 column
- 2023 language model, same 27 symbols, 0.71 bits/char, inside the range | Verified, but the context is incomplete | LLMZip Table I, 0.7101 on text8; the paper itself calls this "likely … optimistic" (Wikipedia was in LLaMA's training data); 0.8426 on its second (book) text, also inside the range; the caveat is in facts.md but not in the video
- "None of these numbers depends on what the words mean" | **Misleading** | the formula uses only probabilities (Shannon 1948), but 1.42, 0.6–1.3 and 0.71 come from predictors that exploit meaning (Shannon 1951 p. 50: the method "exploits the knowledge of the language statistics possessed by those who speak the language"); with the five markers on screen the sentence reads as false
- The hidden character is the Y of THE OTHER DAY, got on the first guess | Verified | record line 3, D 1 A 1 Y 1; the 12 boxes = "THE OTHER DA"
- "Splitting the alphabet took five" | Verified | the on-screen chain isolates Y on cut 5
- Citations: Shannon 1951 · BSTJ; Brown Corpus (Francis & Kučera, 1964); Valmeekam et al., 2023 · arXiv:2306.04050 | Verified | author, year and venue correct
MECHANICS: runtime 3:42.8 · 161 wpm · max silence 1.99 s (0:11.4 and 2:15.2, both planned prediction holds) · max static 3.6 s (3:13.9) · −14.1 LUFS / −2.0 dBTP · leading 0.00 s, trailing 1.47 s · WER 1.9 % · 0 banned phrases
FIXES (highest impact first):
1. [2:13.9–2:28.5 and 2:29.3–2:38.5][Clarity/correctness] The equation keeps the previous context's H while a new skyline is drawn: "= 4.11 bits" over after-Q (kf_24) and "= 0.16 bits" over after-TH (frame 2:33.0). On "What comes after a Q?" (2:13.9) and on "After TH" (2:29.3), TransformMatchingTex the right-hand side to "= ? bits" with a yellow "?". Leave the old value as a 30 % grey ghost in the right gutter at its level, so the drop stays readable. After each pour, TransformFromCopy the newborn level label (0.16 at ~2:28, 1.67 at ~2:38.5) into the "?" slot. This removes cap 6.
2. [3:22.5–3:25.4][Clarity/Concision] "None of these numbers depends on what the words mean" is misleading: three of the five markers on screen come from guessers who use meaning. Cut the sentence (saves ~3 s, and "inside that range" then runs straight into the landing). If you want to keep the Shannon-1948 idea, say instead: "The formula never asks what a word means — only how well you saw it coming." Note the dash is fine; it is not a fake reveal.
3. [2:38.4][Clarity — honest limits] Q and TH are the two luckiest contexts. Viewers will leave thinking two letters of context gets you to ~1.7. After "settles at 1.7", add: "Those are the easy cases. Averaged over every two-letter context, it's still two point eight." (+14 words, offset by fix 2.) On screen, bring a grey dashed ghost level at 2.81 (Brown, H(X | 2 previous) = 2.81, recomputed) into the TH chart for 2 s, labelled "all 2-letter contexts: 2.8". Add the same grey marker "2.8" to the 0–5 number line at 3:05. This is what makes "with a hundred letters of context" at 3:02 land: it explains why Shannon needed long context.
4. [3:11.7–3:21.9][Clarity — honest limits / Veritasium sourcing] LLaMA almost certainly saw text8 (Wikipedia) in training, and the authors call the 0.71 result "likely … optimistic". Either (a) use their second figure, 0.84 bits/char on a book text with the same 27-symbol preprocessing (also inside 0.6–1.3), with the narration "…needed point eight four bits per character on a book, inside that range"; or (b) keep 0.71 and add a 24-px grey tag under the marker, "text it may have memorised". (a) is stronger and keeps the claim fully clean. Before scripting "a book it never saw", check that ref. [7] postdates LLaMA's training data (facts.md says it is a 2023 Project Gutenberg book).
5. [1:33.4–1:34.6][Clarity/Motion] The pivotal `p · 2ᵏ = 1` is fully legible for only ~1 s (crops at 1:33.8 and 1:34.4; it is still building at 1:33.2 and already in glyph soup at 1:35.0). §5 asks for ≥ 2 s + 0.4 s × 2 terms = 2.8 s. Add `self.wait(1.8)` after it completes, and start the rearrangement only on "So k equals". That costs ~1.8 s.
6. [1:35.0][Motion] The rearrangement to `k = log₂(1/p)` passes through overlapping glyphs ("k log p 1", frame 1:35.0). Run the three moves the script describes in sequence, 0.7 s each with isolated substrings: p drops under the 1, then k comes down from the exponent, then the 2 becomes the log base. Do not use a single simultaneous TransformMatchingTex.
7. [0:29.5–0:32.5][Motion] The chart entrance is messy (frame 0:31.0): the tiles float above a y-axis still growing through the "B" label, and the "4.75" label morphs through the last column into an unreadable "4❀". Grow the axes first (0.8 s), then drop the tiles onto the baseline, then TransformFromCopy "4.75" along a path above the bars to the right gutter.
8. [Audio, whole episode] Nearly every sentence boundary has the same 0.4–0.5 s gap (report silence list: about 60 gaps of 0.4–0.6 s). That reads as mechanical, not intentional. Within a continuing thought, shorten gaps to ~0.25 s (1:46.7, 1:50.2 and 1:52.0 inside the pour; 2:21.3 and 2:23.3 inside the Q beat). At beat boundaries, lengthen them to 0.8–1.0 s (0:43.3 before "So where do…", 0:58.3 before "Instead", 2:38.4 before "Shannon measured", 3:25.4 before the landing). Whisper heard "guess's number" at 2:53.4, so respell it as "the number of each guess".
9. [2:41.0–2:43.0][Visual] The hard reset leaves a lone empty yellow cursor box at the top left and "first guess: 0 / 102" on an otherwise empty frame (frame 2:41.5). Fade the whole record in at 20 % first, then let the cursor reveal it at full strength. The frame then has a focal point, and the viewer sees how much text there is.
10. [2:43–3:25][Visual] The two-digit guess counts (15, 17, 11) are drawn at 80 %, about 22 px cap height (kf_30 2:52.1), below the 24-px tick floor. Draw them at full size and widen only those cells to 0.36.
11. [3:17–3:25][Visual] Three labels ("0.6–1.3", "LLM 0.71", "1.42") stack within ~120 px around x ≈ 0.6–1.5 (frame 3:19.5). Move "0.6–1.3" below the axis, centred under the band, so each marker has one label above it.
12. [0:00–0:11][Hook] The first frame is 12 empty boxes. The question is concrete but the picture is not. On "You've read this English sentence", flash the 12 boxes filled with ghosted letters at 15 % opacity, too faint to read, for 0.6 s, then blank them. That says "real text is here" without giving away the Y the landing depends on.
REACHES 9 IF ALL FIXED: yes, narrowly. No structural change is needed. Fixes 1–2 remove the only cap, and the episode returns to 8.1. Fixes 1–5 take Clarity to 9: the derivation is already the right one, and what is missing is a correct label, an honest average and a held equation. Fixes 5–7 and 9–11 take Motion and Visual to about 8.5–9, fix 8 takes Audio to 8.5, and fix 2 takes Concision to 9. That gives a weighted score of about 8.9–9.0. Fixes 1, 2 and 3 matter most. Without fix 3 the episode's central story ("context is what removes the questions") rests on two cherry-picked contexts.
KEEP:
- The pour: skyline → equal-area slabs → yellow level line. It is the proof that area = average, and it is reused for Q, TH and the guess numbers. Keep all four pours.
- Shannon's own 102-symbol record, with its real guess counts, flown into the guess-number skyline, and the landing in which THE OTHER DA flies into the cold-open row and Y lands in the "?" box with "1 guess" against "5 questions".
- The doubling strip ("what's still possible") with the live doublings counter: E 3.3, Z 10.3. It is the concrete step that makes p·2ᵏ = 1 something the viewer could have invented.
```

## Notes on scoring

- **Hook 8.5.** The question is concrete and posed by 0:11, followed by a planned 2.0 s hold (0:11.4–0:13.4). "The natural answer is 5" voices the misconception. Shannon's "about 1" at 0:28–0:35 creates the gap, and "So where do 4 of every 5 questions go?" (0:43.9) drives the middle. The landing re-sees the first frame exactly (3:27–3:41). Deductions: the opening picture is abstract, with empty boxes and no real text (fix 12), and the stakes arrive at 0:35–0:44, later than §6's 0:12–0:25 window.
- **Clarity 7.5.** Concrete first, and every step is justified: halving, then splitting probability, then doubling strips, then p·2ᵏ = 1, then log₂(1/p), then area, then the pour to H. All 30-plus numbers recompute. Deductions:
  - two stretches of a wrong on-screen H (fix 1);
  - the key equation is held for about 1 s (fix 5);
  - the contexts are cherry-picked with no average given (fix 3);
  - a misleading semantic line (fix 2);
  - the LLM caveat is in facts.md but not in the video (fix 4).
- **Visual 8.** One semantic palette, applied consistently: blue = probability, yellow = questions/bits, green = Shannon, purple = context. Citations are placed correctly, and the charts carry quantity names. Deductions: the empty reset frame at 2:41.5, the undersized two-digit counts and the label stack at 3:19.5. The X J Q Z inset reaches x ≈ 1820 px at 1:46, just inside the 1824-px safe edge, but it does not cross it.
- **Motion 8.** Objects persist and transform with meaning: tiles become columns, widths become probabilities, heights become costs, then the pours, and the record phrase flies into the cold-open row. Deductions: the messy chart entrance (0:31.0), glyph soup at 1:35.0, and the formula hold that is too short.
- **Audio 8.** 161 wpm, −14.1 LUFS, −2.0 dBTP, 1.9 % WER. Deictics land: "E starts near a tenth of the bar" (1:09.8) arrives with E's strip at 1:11, and "U swallows the bar" (2:21.9) with U widening at 2:21. Deductions: gap lengths are uniform throughout (fix 8), and a possible "guess's" artefact (2:53.4).
- **Concision 8.5.** 583 words, nearly all load-bearing. One slack sentence (3:22.5).
- **Originality 9.** Pouring the skyline flat, the guess-number skyline built from Shannon's own record, and a landing on the actual Y from his 1951 page are not the stock way to teach entropy. Viewers would remember them.

## Slop scan (§4)

- No banned phrases, in either the narration or the transcript.
- No question chains: "So where do 4 of every 5 questions go?" stands alone; "Is it a space, E, T, A, or O?" is the example question and is followed by a statement; "What comes after a Q?" is followed by a hold.
- One "X, not Y" antithesis ("split the probability, not the alphabet", 0:58). It is the thesis, so it is acceptable.
- No empty superlatives, hedges or recap ending. The last line, "In English, almost no letter arrives without a past", reframes the cold open.
