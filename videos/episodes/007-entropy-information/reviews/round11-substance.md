# Round 11 review, substance (science and story editor)

Evidence: `review/` pack (metrics.json 00:05 is newer than final.mp4 00:03, so I used it). I read report.md, all 12 contact sheets, 16 keyframes at full resolution (kf_02, 04, 07, 13, 16, 19, 22, 24, 25, 27, 29, 32, 36, 38, 39, plus kf sheets), five extra frames I pulled with ffmpeg (0:28.3, 0:46.0, 1:17.0, 2:50.5, 3:19.0), transcript.txt, transcript_words.tsv (1:39–1:53), narration.txt, script.md and facts.md.

To check the numbers myself, I recounted the Brown Corpus (a fresh NLTK `brown.zip`, my own reduction script, not `data.py`). I recomputed the Shannon record entropy and the run arithmetic. I also checked the LLMZip v2 HTML (abstract, §IV, Table IV) and the Shannon 1951 PDF (princeton.edu) by web search and scrape.

```
EPISODE: 007 — "How Much Information Is in a Letter?"
IDEA: A character costs log₂(1/p) yes/no questions, so its information depends on how predictable it is; averaged over English with its past, that is about one bit, not the 4.75 that halving the alphabet gives.
SCORES: Hook 9 · Clarity 8.5 · Visual 9 · Motion 9 · Audio 9 · Concision 9 · Originality 9
WEIGHTED: 8.9 (887.5/100 = 8.875)   AFTER CEILING: 8.9 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none
FINAL: 8.9   PASS: no
```

## FACTS

| Claim | Verdict | Source / my check |
|---|---|---|
| 27 symbols (26 letters + space) | Verified | Shannon 1951, p. 56 |
| Halving 27 → 1 takes 5 cuts (27→13→6→3→2→1) | Verified | 2⁴ = 16 < 27 ≤ 32 |
| log₂ 27 = 4.75 | Verified | 4.7549 |
| "In 1951, Claude Shannon put the true figure at about one" | Verified | Shannon, "Prediction and Entropy of Printed English", *BSTJ* 30(1):50–64, 1951: "something of the order of one bit per letter" |
| "No compressor beats it on average" (it = the true figure) | Verified as worded | Source-coding theorem. **But see Fix 1:** the on-screen "floor" line is drawn at exactly 1.0, and the payoff compressor later lands at 0.84, below it. |
| Next-character prediction is how language models are trained | Verified | Standard autoregressive objective; LLMZip §I |
| 3.75 extra (79 %) | Verified | 3.75/4.75 = 0.789 |
| E 10.3 %, Z 0.08 %, ×130 | Verified | My Brown recount: p(E) = 0.103137, p(Z) = 0.000792, ratio 130.28 |
| Space E T A O = 48 % ("nearly half") | Verified | 0.17477 + 0.10314 + 0.07633 + 0.06656 + 0.06265 = 0.48344 |
| E needs 3.3 doublings | Verified | log₂(1/0.10314) = 3.277 |
| Z is 1 in 1260 and needs 10.3 | Verified | 1/p = 1263.1 (shown as 1260, 3 s.f.); log₂ = 10.30 |
| p·2ᵏ = 1 ⇒ k = log₂(1/p) | Verified | Re-derived. The two algebra steps are shown as two separate moves |
| Area = Σ p·log₂(1/p) = average cost | Verified | Definition of expectation; Σp = 1 |
| H₁ = 4.11 bits (Brown, 27 symbols) | Verified | My recount: 4.1111. Shannon's own F₁ = 4.03 comes from older tables, and the screen labels the figure as Brown |
| 4.11 is "four times Shannon's estimate" | Verified | 4.11/≈1 |
| After Q: U 98 %, H = 0.16 | Verified | 5,103 Q's; U 0.98138; H = 0.1560 |
| After TH: E 68 % ("two-thirds"), cost about half a question, H = 1.7 | Verified | 134,673 TH's; E 0.68332; log₂(1/0.6833) = 0.549; H = 1.6675 |
| Run E␣O: 0.683 × 0.670 × 0.072 = 0.0329; log₂(1/0.0329) = 4.93; 0.55 + 0.58 + 3.80 = 4.93 → 5; one at a time 1 + 1 + 4 = 6 | Verified | My recount: E∣TH 0.68332, ␣∣HE 0.66967, O∣E␣ 0.072014. Every displayed relation holds for the displayed values (log₂(1/0.0329) = 4.926). ⌈4.92⌉ = 5 |
| Averaged over every two-letter context: 2.81 | Verified | My recount: H(X∣2 prev) = 2.8105 (H(X∣1) = 3.3811) |
| 27² = 729; 27¹⁰⁰ ≈ 10¹⁴³; Brown has 5.75 M characters | Verified | 100·log₁₀27 = 143.14; my count was 5,751,046 against their 5,751,047 (one terminal space) |
| Shannon's subject guessed until right; 79 of 102 right on the first guess | Verified | Shannon 1951, p. 56, verbatim ("Out of 102 symbols the subject guessed right on the first guess 79 times"). The on-screen record transcribes to 79/8/3/2/2 + 8 |
| Twin argument: the counts let a twin rebuild the passage | Verified | Shannon 1951, p. 55 ("identical twin") |
| Guess skyline 3.67 for the 2nd-guess column; poured value 1.42 | Verified | log₂(102/8) = 3.672; −Σ q log₂ q = 1.4223 |
| "That caps the text" (labelled an upper estimate) | Verified | Shannon eq. 17 upper bound, here as a plug-in on 102 symbols. The "upper estimate" tag and "one passage, context 0–101" state the limitation |
| Shannon, 100 letters of context: 0.6–1.3 bits | Verified | Shannon 1951, p. 64 / Fig. 4, N = 100 |
| A language model compressed part of a book posted to Gutenberg after training: 0.84 bits | Verified | Valmeekam et al., arXiv:2306.04050 v2, §IV and Table IV: LLaMA-7B + AC, M = 511, 0.8426 bpc on 100k tokens of a book released 25 May 2023, preprocessed to lowercase + space (27 symbols). The author list and the citation on screen are correct |
| The hidden Y in "THE OTHER DAY" took 1 guess | Verified | Record line 3, Y count = 1 |
| "Splitting the alphabet took five" | Verified | The halving chain shown at 0:13–0:21 ends on Y |

Nothing is wrong, fabricated or uncited. Every empirical number has its source on screen while it is shown.

## MECHANICS

runtime 3:34.8 · wpm 151 (speech time) · max internal silence 2.01 s (0:07.4, the planned prediction hold) · max static 3.03 s (3:31.8, the final hold) · −14.0 LUFS / −1.8 dBTP · leading 0.00 s / trailing 0.56 s · WER 1.4 % ("pour"→"poor" is a homophone; the other differences are digit normalisation) · banned phrases 0 · layout audit 0 issues. No cap is triggered.

## Transcript and §4 scan

- No banned phrases.
- No question chains: each question stands alone (0:05, 0:34, 0:45, 1:47, 3:27).
- None of the "it's not just" constructions, no colon fake-reveals, no empty superlatives, no recap ending.
- The one rhetorical turn, "Half a question sounds impossible, but…", is paid off on screen by the bill.
- The hook lands by 0:07 with a genuine, likely-wrong commitment (5), and Shannon's "about one" overturns it at 0:25.
- The landing re-sees frame one: the same row, tiles and halving chain, now with the Y filled in. The last line reframes the cold open rather than restating it.

## What I looked at in the frames (and why most of it scores 9)

- **0:10 / 0:21.9 (kf_02, kf_04).** The cold open is one diagram, not a slide. The halving cuts close on Y, which plants the landing.
- **0:42.7 (kf_07).** The E/Z widths are true Brown widths, the leaders and ×130 read clearly, and the citation is bottom-left above the caption zone.
- **1:01.6, 1:17.0, 1:26.6 (kf_13, extra frame, kf_16).** The doubling strips lead straight into p·2ᵏ = 1, and the algebra moves step by step (the 2 runs its lane at 1:17). The formula colours match their referents (p blue, log yellow). The pour is the memorable image of the episode.
- **1:44.4, 1:58.4, 2:27.2 (kf_19, kf_22, kf_27).** The live gap meter (3.75 → 3.11 → 1.81 → 0.42) carries the failure through the whole middle. The equation slot shows "?" until each new level is poured, so no stale value ever sits on screen.
- **2:11.0, 2:17.3 (kf_24, kf_25).** The bill is correct, aligned and colour-true: p blue, cost yellow, whole questions grey.
- **2:42.3 (kf_29).** Shannon's record is real and readable, with the tally at 79/102.
- **2:50.5, 2:55.4 (extra frame, kf_32).** log₂(1/q) = 3.67 is on the 2nd column with q in blue. The pour lands at 1.42 above the band, with its honest caveat beside it.
- **3:12.4, 3:19.0 (kf_36, extra frame).** The bits-per-character line is clean, and the irrelevant tags are dimmed to 30 %.
- **3:25.3, 3:30.8 (kf_38, kf_39).** The landing closes the loop.

## FIXES (highest impact first)

1. **[0:27.2–0:29.8 and 3:15.7–3:19.5][Clarity] The climax compressor lands below the line the episode labelled "floor".**
   - **Problem:**
     - On "No compressor beats it on average", a ghost of the price line is pushed down and stops at exactly 1.0, labelled **floor** (frame 0:28.3: the dashed line sits mid-band at 1.0, tagged "floor" in the right gutter).
     - At 3:17–3:19 a compressor (the LLM) lands at **0.84**, visibly below that line (frame 3:19.0).
     - A careful viewer's first thought is "so it *did* beat the floor?" The words are technically consistent, because "it" is the unknown true figure and 0.84 sits "inside that range". But the picture asserted the floor at 1.0. The episode also never says that a real compressor's rate is an upper bound on the true figure, so 0.84 pushes the floor down.
     - This is the one logical seam in an otherwise airtight argument, and it sits at the payoff.
   - **Change, picture (0:28):** do not end the ghost on a line at 1.0. Let it drop into the green band and dissolve into it: the band brightens for 0.6 s, and **floor** is tagged on the band itself as "floor: somewhere in here", or as "floor" with a bracket spanning 0.6–1.3. The floor then reads as a region, not a value.
   - **Change, words (3:15):** make the payoff say what 0.84 implies: "It needed point eight four bits, *so the floor is lower still*." (+5 words, about 1.5 s. Recover the time by cutting "inside that range", which the band already shows.)
     - As "lower still" is spoken, flash the band's segment below the 0.84 marker (0.6–0.84) green.
     - This turns the number line into the episode's real structure: every marker (4.75, 4.11, 2.81, 1.42, 0.84) is a ceiling, and each better predictor pushes the ceiling down toward a floor no one has measured.
   - It lifts Clarity to 9, and arguably Hook too, because the ending then resolves the "about one" claim exactly rather than approximately.
2. **[2:08–2:18][Clarity, nitpick] The run bill shows 11 numbers in about 10 s while the narration voices only "five" and "six".**
   - **Problem:** the multiply-then-add demonstration is correct and well staged, but the viewer must read 0.683 × 0.670 × 0.072 = 0.0329 and log₂(1/0.0329) = 4.93 while hearing a different clause.
   - **Change:** hold the complete product row for 0.6 s longer before the sum row starts writing (start the sum on "costs", not on "so"). Flag the two 4.93s for 0.6 s rather than the current shorter flash. There is no narration change.
3. **[3:26.8–3:30.8][Clarity, nitpick] The landing compares "1 guess" (green) with "5 questions" (yellow), so the units differ on screen.**
   - The spoken "Is it Y?" bridges the gap, but the labels do not.
   - **Change:** write the green tag as **1 question** (or "1 guess = 1 question"), so the frame compares like with like: one question with context, five without.
4. **[0:51–1:04][Concision, nitpick] Four new figures arrive inside 13 s: "a tenth", 3.3, 1260, 10.3.**
   - Each has a picture, so this is not a deduction.
   - **Option:** if any runtime is needed for Fix 1, the trim "Z, one in every twelve hundred sixty, needs ten point three" → "Z needs ten point three" is safe, because the 1/1260 label already says it.

REACHES 9 IF ALL FIXED: yes. Fix 1 alone moves Clarity to 9, giving a weighted score of 9.0 with no cap in play. No structural change is needed: the hook, the measured failure, the single insight picture (the pour), the cited payoff with its honest limits, and the closing callback are all in place.

## KEEP

- The **pour**: the skyline whose area is the average, poured flat into one level, then reused unchanged for Shannon's guess counts ("the same skyline"). It is the episode's memorable, shareable image.
- The **doubling strips → p·2ᵏ = 1 → k = log₂(1/p)** derivation, built from its referents on screen. A viewer could re-derive it after one watch.
- The **cold-open row and halving chain re-seen at the end**, with the Y planted at 0:17 and paid off at 3:23, plus the live gap meter that measures the failure at every stage.
