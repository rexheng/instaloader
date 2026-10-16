# Episode 7, review round 4 (substance critic: facts, story, clarity, concision, slop; all dimensions scored)

**Evidence.** I used the existing `review/` pack, because metrics.json (23:28) is newer than final.mp4 (23:26). I read:
- report.md, narration_diff.txt, transcript.txt and transcript_words.tsv
- all 13 contact sheets
- full-resolution keyframes kf_01, kf_03, kf_07, kf_14, kf_17, kf_22, kf_30 and kf_40
- 13 extra ffmpeg frames: 0:53.6, 1:39.0, 1:59.0, 2:27.2, 2:51.5, 2:52.6, 2:53.2, 3:12.0, 3:28.6, 3:29.0, 3:29.4, 3:38.8 and 3:40.5
- script.md, narration.txt, narration.json, facts.md, data.json and the round-3 substance review (to check which fixes landed)

**Independent recomputation.** I downloaded the NLTK Brown corpus and recounted it with my own script (not `data.py`), reduced to the 27-symbol alphabet. It gives:
- n = 5,751,046 (data.json says 5,751,047, an off-by-one trailing space); 1,005,119 words; H₁ = 4.1111
- p(E) = 10.314 %, p(Z) = 0.0792 %; E/Z = 130.3; 1/p(Z) = 1263; log₂(1/p(Z)) = 10.30; log₂(1/p(E)) = 3.277
- top five (space, E, T, A, O) = 48.34 %
- H(X | 1 previous) = 3.381; H(X | 2 previous) = 2.8105
- after Q: n = 5,103, U = 98.14 %, cost 0.027, H = 0.156
- after TH: n = 134,673, E = 68.33 %, cost 0.549, H = 1.6675
- inset heights: X 9.25, J 9.53, Q 10.14, Z 10.30

From Shannon's record in data.json:
- the tally is 79/8/3/2/2 and 8 above five (3+1+1+1+1+1), exactly Shannon's text
- the plug-in guess-count entropy is 1.4223
- the mean is 198/102 = 1.94 guesses per symbol

Arithmetic: log₂27 = 4.755; 3.75/4.75 = 78.9 %; 4.11/1 ≈ 4.

I measured on-screen values against the axes:
- E at 3.26 and space at 2.51 (kf_17)
- the 0.6–1.3 band at 0.61–1.31 on the zoomed axis (kf_22)
- 0.16 and 1.67 at their levels

All are correct to within a pixel. The running tally (kf_30, "54 / 102" with the cursor on the 75th cell) counts every cell before the cursor. It lags by one cell by design, and the final 79 is right.

**Web verification.**
- **Shannon 1951**, "Prediction and Entropy of Printed English", *BSTJ* 30(1): 50–64 (Princeton mirror): "Out of 102 symbols the subject guessed right on the first guess 79 times … on the second guess 8 times, on the third guess 3 times, the fourth and fifth guesses 2 each". "Order of one bit per letter" and the N = 100 bounds of 0.6 and 1.3 match. Verified.
- **LLMZip**, arXiv:2306.04050 v2 (abstract page and HTML). The authors are Valmeekam, Narayanan, Kalathil, Chamberland and Shakkottai (2023). §IV: "a recently released (May 25, 2023) book [7] under Project Gutenberg. We extracted text that corresponds to 100,000 tokens … only lowercase letters and space … 0.8426 bits/character". Table IV, M = 511: ρ_LLaMA+AC = 0.8426. **Reference [7] is J. Frank Dobie, *Legends of Texas*, Texas Folk-Lore Society, 1924.** The number and citation are verified. The narration's "a new book" is not accurate (see FACTS and fix 1).
- **Kokoro G2P** (misaki, run locally): "TH" → /tˌiˈAʧ/ ("tee-aitch"), Q → "cue", U → "you", Y → "why". So the ASR "th", "cue", "you" and "why" are spellings, not mispronunciations, and "pores" for "pours" is a homophone.

```
EPISODE: 007 — "How Much Information Is in a Letter?"
IDEA: A character costs log₂(1/p) yes/no questions, so its information is set by how predictable it is, not by alphabet size; priced with the text before it, English needs about one bit per character, not the 4.75 that halving the alphabet suggests.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.6 (127.5 + 212.5 + 127.5 + 127.5 + 85 + 85 + 90 = 855 / 100 = 8.55)   AFTER CEILING: 8.6 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none. Every number spoken, drawn or plotted recomputes from raw Brown and Shannon's record. Citations are on screen for Shannon (0:31–0:53, 2:55–3:28), Brown (0:51–2:53) and LLMZip (3:29–3:37). There are 0 banned phrases and no question chains. Mechanics are all inside the bar. The ending is a reframe, not a recap.
  - I considered cap 6 for "a new book" (3:31): the book is from 1924. I did not apply it, because the paper itself calls it "a recently released … book" and "a recently published book in Project Gutenberg" (Table IV caption), so the narration is a lossy paraphrase of the source, not an invented fact. It is the top fix. If it survives another round, I would treat it as Wrong.
  - I considered cap 7 for overlapping text at 3:28.8–3:29.2, where two citations are superimposed mid-crossfade. I did not apply it because it lasts about 0.5 s inside a transition, not a layout overlap.
FINAL: 8.6   PASS: no
```

## FACTS

| Claim | Status | Source / check |
|---|---|---|
| The hidden character is one of 26 letters + space (27) | Verified | Shannon 1951, p. 56 |
| Five halving cuts take 27 to 1 (27→13→6→3→2→1, ending on Y) | Verified | 2⁴ < 27 ≤ 2⁵; kf_03 |
| Perfect 50-50 splits: log₂27 ≈ 4.75 | Verified | 4.7549 |
| Shannon (1951) estimated "about one" | Verified | BSTJ 30(1), p. 50 ("of the order of one bit per letter") |
| No text compressor can beat the true figure on average | Verified | Source-coding theorem; attached to the true rate, not the estimate |
| Guessing what comes next is how LMs are trained | Verified | Next-token cross-entropy; LLMZip §I |
| "Four of every five questions" / on screen "3.75 extra (79%)" | Verified | 3.75 / 4.75 = 0.789 |
| E turns up 130× as often as Z; 10.3 % vs 0.08 % | Verified (my recount) | 130.3; labels now sit over their own columns (f 0:53.6) |
| Space, E, T, A and O are nearly half of all text (48 %) | Verified (my recount) | 48.34 % |
| E near a tenth, 3.3 doublings | Verified | 0.1031; 3.277 |
| Z 1 in 1,260, needs 10.3 | Verified | 1263; 10.30 |
| p·2ᵏ = 1 ⇒ 2ᵏ = 1/p ⇒ k = log₂(1/p); area Σp·log₂(1/p) = average | Verified (re-derived) | Σp = 1; definition of expectation |
| Inset X J Q Z ×28 wide, Z = 10.3 | Verified | 9.25 / 9.53 / 10.14 / 10.30 |
| English letter entropy 4.11 bits (Brown, labelled) | Verified (my recount) | 4.1111; Shannon's own F₁ = 4.03 from older tables |
| "Four times Shannon's estimate" | Verified | 4.11 / ~1 |
| Entropy, bits, one bit per yes/no answer | Verified | Shannon 1948 |
| After Q: U 98 of 100; cost "almost nothing"; average 0.16 | Verified (my recount) | 98.14 %; 0.027; 0.156 |
| After TH: E two-thirds; "about half a question"; average 1.7 | Verified (my recount) | 68.33 %; 0.549; 1.667 |
| A compressor asks about runs, and the fractions add up | Verified | Chain rule: log₂ 1/P(run) = Σ log₂ 1/p(xᵢ \| past); arithmetic coding; LLMZip uses AC |
| Averaged over every two-letter context: 2.8 | Verified (my recount) | 2.8105 |
| Protocol: the subject guesses each next character until right | Verified | pp. 55–56 |
| 79 of 102 on the first guess | Verified (web + record) | p. 56 |
| The twin rebuilds the passage from the counts | Verified | p. 55 ("identical twin") |
| Guess-count skyline pours flat at about 1.4 | Verified (my recount) | 1.4223 (Shannon eq. 17 form, one 102-symbol passage) |
| A better guesser could only lower it | Verified | Twin argument plus majorisation/Schur-concavity |
| With 100 letters of context: 0.6–1.3 bits/char | Verified | p. 64, N = 100 |
| 2023 LM, same 27 symbols, 0.84 bits/char, inside the range | Verified (number) | LLMZip Table IV, 0.8426 |
| "…compressing part of **a new book**" | **Misleading** | Ref. [7] is Dobie, *Legends of Texas*, **1924**; only its Project Gutenberg release (25 May 2023) is new (fix 1) |
| The hidden character is the Y of THE OTHER DAY, got on the first guess, "a single yes-or-no question" | Verified | Record line 3: …D 1 A 1 Y 1 |
| "Splitting the alphabet took five" | Verified | The on-screen chain isolates Y on cut 5 |
| Citations: Shannon 1951 · BSTJ; Brown Corpus (Francis & Kučera, 1964); Valmeekam et al., 2023 · arXiv:2306.04050 (LLMZip), Table IV | Verified | Author, year, venue and finding are all correct |

```
MECHANICS: runtime 3:54.6 · 160 wpm (speech time) · max silence 1.96 s (0:08.3, planned prediction hold) · max static 3.63 s (3:51.0, end hold) · −14.0 LUFS / −1.9 dBTP · lead 0.00 s / trail 1.24 s · WER 2.0 % (all diffs are homophones or number spellings) · 0 banned phrases · layout audit 0/218
```

## Story and clarity read (why 8.6 and not 9)

Round 3's substantive gaps are fixed, and they are fixed well:
- the fractional-question line (2:34–2:43)
- the identical-twin argument (3:04–3:11)
- the 0.08 % label anchored over Z with ×130 (f 0:53.6)
- "= 0.16 bits" held about 2 s (f 2:27.2)
- the question ending by 0:08.5
- the zoomed context axis (kf_22, f 2:51.5)

The spine is now complete:
1. puzzle and commit
2. measured failure (3.75 extra, 79 %)
3. cause (same price for E and Z)
4. doubling strip → p·2ᵏ = 1 → log₂(1/p) → skyline → pour → H
5. context (Q, TH) and the honest correction to 2.81
6. Shannon's real record → twin → guess skyline → bits line → LLM
7. the Y dropping into the cold-open ? box

What stops it at 8.6 is the second half's argument, not structure.

**1. "A new book" (3:27–3:31) is a 1924 book.** A viewer hears that a language model compressed fresh 2023 prose. In fact it compressed text written 99 years earlier, which was simply posted to Project Gutenberg after LLaMA was trained. The episode's own facts.md (claim 30) admits that "a 1924 book may exist elsewhere online in scanned form", so "new" is the only signal of out-of-sample, and it is literally false. A research editor would not let it air.

**2. Why a person? (2:47–2:55).** The narration goes straight from "Averaged over every two-letter context, it's still 2.8" to "Shannon measured this with a person". It never says why corpus counting stops. Two-letter contexts number at most 729, but 100-letter contexts essentially never repeat, so they cannot be counted, and a human brings that knowledge instead. Without that clause, the human experiment arrives as a change of topic rather than as the next forced move, which is the step a viewer needs in order to re-derive the argument. script.md even states the intent ("This is why Shannon needed long context"), but no line carries it.

**3. "The fractions add up" is shown with no fractions (2:39–2:43).** On "long runs of letters" the ? box widens into four empty ? boxes (sheet 9, 2:41; sheet 10, 2:43). The idea that half a question per letter becomes about one question per two letters is never shown as a number. The data to show it is already in the episode. In THE OTHER, E after TH costs 0.55 and the space after HE costs 0.58 (my Brown recount): 1.13 questions for two letters.

**4. 1.42 lands above Shannon's 1.3 ceiling with no reason given (3:15–3:25).** The guess skyline pours to 1.42. Ten seconds later the band shows an upper bound of 1.3 from the "same" method, with 1.42 visibly outside it (f 3:28.6). The reason (one 102-letter passage versus Shannon's larger N = 100 tables) is never given. "A better guesser could only lower it" half-covers this.

**Hook.**
- What works: the question ends at 0:08.5, there is a 1.7 s hold, "the natural answer is five" lands at 0:10.2, and the ending re-sees the first frame exactly (kf_40).
- What holds it below 9: for the first 4 s the frame is a dim box row and a tile strip (kf_01) with no question on screen; "questions per character ?" arrives only at about 0:04.5 (sheet 1). The opening question is also abstract for a muted or first-second viewer. It is strong, but not irresistible.

**Concision.** 608 words in 3:54.6. I could find only about 3 % removable: the "Q and TH are the easy cases" sentence can fold into a "But" (2:44.7), and the 1.3 s hold after "What comes after a Q?" is long for a question the bar answers. The runtime sits 5 s under the cap, so fixes 1–2 must be funded by these cuts.

**Slop.** I found none.
- 0 banned phrases. The only antithesis, "split the probability, not the alphabet", is the thesis and is earned.
- "Half a question sounds impossible" voices a real objection.
- The voice is physical and specific ("U swallows the bar", "pour the skyline flat").

**Visual and motion (scored, but secondary to my brief).** The palette is disciplined, with one meaning per hue, and the chart labelling is complete. The defects are all transitions:
- **3:28.8–3:29.2:** the Shannon and Valmeekam citations are superimposed and illegible (f 3:29.0).
- **2:52.6–2:53.8:** the context chart, H equation, "all two-letter contexts" label and Shannon record are superimposed in one cross-dissolve (f 2:53.2).
- **1:59.0:** the "questions"→"bits" axis-title morph is glyph soup (f 1:59.0).
- **3:12.0:** guess digits melt into bars mid-flight (f 3:12.0).
- **3:39–3:42:** the landing passes through THE OTHER DAY floating alone right of centre (sheet 13, 3:39), then a letter-spaced purple row with an unboxed Y (3:41), before the boxes arrive.

## FIXES (highest impact first)

1. **[3:27–3:31][Clarity/correctness] "part of a new book" describes J. Frank Dobie's *Legends of Texas* (1924), posted to Project Gutenberg on 25 May 2023.**
   - Replace the line with: "In twenty twenty-three, a language model compressing part of a 1924 book, first put online that May, in the same twenty-seven symbols, needed point eight four bits, inside that range." That is +5 words, about 2 s.
   - Under the LLM marker, add a grey tag "1924 book · online May 2023" (Text font_size 18) for the marker's hold.
   - Update facts.md claim 30 to match.
   - This removes the cap-6 risk.
2. **[2:47–2:55][Clarity] The switch to a human experiment is unmotivated.**
   - Replace "Shannon measured this with a person, who read a passage one character at a time" with "Longer contexts almost never repeat, so you can't count them. Shannon used a person instead, who read a passage one character at a time". That is +9 words, about 3 s.
   - Visual: on "almost never repeat", grow a grey dashed placeholder level labelled "100 letters: ?" just above 0 on the zoomed axis. Let it hang there as the chart fades, so the record visibly answers it.
3. **[2:39–2:44][Clarity] "The fractions add up" is shown as four empty ? boxes.** Use a real run.
   - On "long runs of letters", widen the ? box into two boxes holding E and ␣ (the "E␣" of THE OTHER).
   - Write yellow costs under them, "0.55" and "0.58" (Brown, two-letter context; computed: E after TH 0.549, ␣ after HE 0.577).
   - On "the fractions add up", TransformFromCopy both into "= 1.13 for 2 letters" under the pair (≤ 5 words).
   - The narration is unchanged.
4. **[3:15–3:25][Clarity] 1.42 sits outside Shannon's 0.6–1.3 band (f 3:28.6) with no explanation.**
   - When 1.42 flies onto the bits line (3:20), add a grey tag "one 102-letter passage" under it (Text 18, ≤ 4 words), held to 3:37.
   - Optionally change "about one point four bits" to "about one point four bits, from this one passage" (+4 words) if fixes 9–10 free the time.
5. **[2:52.6–2:53.8][Visual/Motion] The chart, equation and ladder labels are cross-dissolved under the record (f 2:53.2).**
   - FadeOut the chart group fully (0.5 s, shift DOWN×0.3), then FadeIn the record at 20 %.
   - Never superimpose the two.
   - Hold the finished ladder (4.11 / 2.81 / 1.67, band) ≥ 2 s before the fade starts.
6. **[3:28.6–3:29.4][Visual] The two citations are superimposed and illegible (f 3:29.0).** FadeOut the Shannon citation (0.35 s), then FadeIn Valmeekam (0.35 s), sequentially and never overlapping.
7. **[0:00–0:04.5][Hook] The puzzle text is absent for the first 4.5 s (kf_01).**
   - Put "questions per character ?" on screen from frame 1 at its y ≈ −1.6 slot, with the ? box already yellow.
   - Keep the flag on "hidden".
   - A muted or scrolling viewer then sees the whole puzzle in the first frame.
8. **[3:38.5–3:43][Visual/Motion] The landing passes through two orphan states (sheet 13, 3:39 and 3:41).**
   - Fade the record and bits line to 0 while bringing the 12 boxes and the ? box in at their cold-open positions.
   - Then fly T H E ␣ O T H E R ␣ D A straight from the record into the boxes, and Y into the ? box, as one 1.5 s LaggedStart (lag 0.05) ending on "the Y" (≈3:40.4).
   - Cut the centred and letter-spaced intermediates.
9. **[2:44.7–2:47.4][Concision] Fold "Q and TH are the easy cases."** into "But averaged over every two-letter context, it's still two point eight." This saves about 2.4 s.
10. **[2:14.4–2:17.5][Concision/Audio] Shorten the post-question pause** after "What comes after a Q?" from 1.3 to 0.9 s (the U column answers it). With fix 9, this saves about 2.8 s in total, which funds fixes 1, 2 and 4 (about +5–6.5 s). The runtime lands at about 3:57–3:58.
11. **[1:59.0][Motion] The axis-title "questions"→"bits" morph is glyph soup.** Use FadeOut(shift UP×0.2) of "questions" followed by FadeIn(shift UP×0.2) of "bits" (0.4 s each), or a ReplacementTransform with run_time ≥ 0.8.
12. **[1:51.8–1:54][Motion] All 27 columns pour simultaneously and cross (sheet 7, 1:53).** Pour space, then E, then the remaining 25 with LaggedStart(lag_ratio 0.04) in sorted order, each stacking on the previous top, about 2.5 s in total. Reuse this for the after-Q, after-TH and guess-count pours.
13. **[3:11.5–3:13][Motion] Guess digits melt into bars mid-flight (f 3:12.0).** Replace the digit→bar morph with FadeOut of the digit copies plus GrowFromEdge(DOWN) of each bar, timed together.
14. **[0:39.5, 1:37.2, 2:52.0, 3:37.4][Audio] Every sentence gap is a uniform 0.4–0.6 s (report silence list), so beat changes don't register by ear.**
    - Lengthen these four beat-boundary gaps (fail, skyline, Shannon's experiment, landing) to 0.9 s.
    - Trim the intra-beat gaps inside 2:17–2:47 to 0.3 s so the runtime is unchanged.
    - Re-check that the deictics still land: "this" at 2:52, "these counts" at 3:09.

REACHES 9 IF ALL FIXED: yes, narrowly. The scores would move as follows:
- Fixes 1–4 lift Clarity to 9 (+12.5).
- Fixes 5, 6 and 8 lift Visual to 9 (+7.5).
- Fixes 5, 8, 11, 12 and 13 lift Motion to 9 (+7.5).
- Fix 7 lifts Hook to 9 (+7.5).
- Fixes 9–10 lift Concision to 9 (+5).

That gives 895 / 100 = 8.95 with Audio left at 8.5, which reaches 9.0 only by rounding. A safe 9.0 also needs fix 14 (Audio to 9, +5 → 900). There is no slack, so fixes 1–4 are mandatory. No structural change is needed: the hook, the measured failure and the one-picture derivation are all present.

KEEP:
- The doubling strips with live yellow counters, which derive p·2ᵏ = 1 → 2ᵏ = 1/p → k = log₂(1/p) one clause per legal step (1:05–1:39).
- The skyline → pour → level → value copied into H, reused with the "? bits" slot for Q and TH, and the honest "easy cases → 2.81" correction on a zoomed axis (1:45–2:51).
- Shannon's real record → identical twin → guess skyline → bits line → THE OTHER DA with Y dropping into the cold-open ? box (2:55–3:54).
