# Round 9 review: craft (visual design, motion, A/V sync)

Critic: independent. I focus on visual design, motion craft and audio/visual sync, and I scored every dimension.

## Evidence

- **Pack.** I reused the `review/` pack: metrics.json (20:57) is newer than final.mp4 (20:54).
- **Read in full.** report.md, all 12 contact sheets, transcript.txt, the word timings (transcript_words.tsv) at 1:00–1:06, 1:28–1:37, 1:37–1:54 and 2:58–3:06, narration.txt, script.md, the facts.md claims for 21c, 29 and 30, and CHANGELOG round 8.
- **Full-resolution keyframes.** kf_01, 04, 07, 13, 15, 18, 22, 24, 26, 27, 29, 31, 32, 36, 37 and 40.
- **Extra extractions** (scratchpad r9c):
  - single frames at 0:23.0, 2:29.6, 2:30.6 and 2:31.6
  - 4 fps strips at 2:28–2:32 and 2:57.8–3:01.8 (the payoff-line build)
  - a 4 fps crop of the Z counter at 1:02–1:05
  - a 5 fps crop of the travelling "2" at 1:16.4–1:18.8
  - a 2 fps strip at 1:30.5–1:35 (average → H → "bits")
- **Recomputed.** From the record on screen (kf_29): first guesses 25 + 24 + 30 = 79 of 102, guess-number entropy 1.4223, and log2(102/8) = 3.672. Also log2 27 = 4.755, 3.75/4.755 = 0.789, 100·log10 27 = 143.1, and the bill 0.683 × 0.670 × 0.072 = 0.03295 → log2 = 4.92 ≈ 4.93, with 0.550 + 0.578 + 3.796 = 4.92. Corpus figures were checked against data.json: H1 4.111, E/Z 130.3, 1/pZ 1263, top-5 0.483, H(X|2) 2.810.

```
EPISODE: 007 — "How Much Information Is in a Letter?"
IDEA: A character costs log2(1/p) yes/no questions, so the average cost is the area of a skyline (width = probability, height = cost) poured flat, and as the predictor uses more of what came before it falls from the 4.75 of halving the alphabet to about 1 bit.
SCORES: Hook 9 · Clarity 9 · Visual 8.5 · Motion 9 · Audio 9 · Concision 9 · Originality 9
WEIGHTED: 8.9 (892.5/100 = 8.925)   AFTER CEILING: 8.9 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none
FINAL: 8.9   PASS: no
```

## FACTS

| Claim | Status | Source / check |
|---|---|---|
| 27 symbols; five cuts 27→13→6→3→2→1 ending on Y | Verified | kf_04: cuts at N\|O, U\|V, X\|Y, Y\|Z, Z\|␣ keep 13, 6, 3, 2, 1 |
| log2 27 ≈ 4.75 | Verified | 4.7549 |
| Shannon 1951: about 1 bit; 0.6–1.3 bits at 100 letters of context | Verified | Shannon 1951, BSTJ 30(1) (facts.md; p. 64 bounds) |
| "four of every five questions"; 3.75 extra (79%) | Verified | 3.75/4.755 = 0.789 |
| E 10.3%, Z 0.08%, ×130; Z 1 in 1260 needs 10.3 | Verified | data.json: 130.3; 1263 → 1260 at 3 s.f.; log2 1263 = 10.30 |
| Space, E, T, A, O ≈ 48% | Verified | 0.4834 |
| E needs 3.3 doublings | Verified | log2(1/0.1031) = 3.28 |
| p·2^k = 1 ⇒ k = log2(1/p); average = Σ p log2(1/p) | Verified | re-derived |
| H = 4.11 bits for English letters (Brown, 27 symbols) | Verified (corpus) | data.json H1 = 4.1111 |
| "four times Shannon's estimate" | Verified | 4.11 against ≈1 |
| After Q: U 98%, average 0.16 bits | Verified (corpus) | facts.md / data.json after_Q |
| After TH: E 68% at about half a question; H = 1.67 ("1.7") | Verified (corpus) | log2(1/0.683) = 0.55; 1.667 |
| Run E␣O: p = 0.683 × 0.670 × 0.072 = 0.0329; costs 0.55 + 0.58 + 3.80 = 4.93 → 5; one at a time 1 + 1 + 4 = 6 | Verified | recomputed (4.92–4.93 depending on rounding, consistent as displayed) |
| Averaged over two-letter contexts: 2.81 | Verified (corpus) | H(X\|2 prev) = 2.8105 |
| 27² = 729; 27¹⁰⁰ ≈ 10¹⁴³; Brown 5.75 M characters | Verified | 143.1; 5,751,047 |
| 79 of 102 right on the first guess | Verified | recount from the on-screen record; Shannon p. 56 |
| Guess-count entropy ≈ 1.42 (an upper estimate); log2(1/q) = 3.67 for 2nd guesses | Verified | 1.4223; log2(102/8) = 3.672; column heights 5.09/5.67/5.67/5.09/6.67 match kf_31 |
| Twin argument (the counts preserve the text) | Verified | Shannon 1951 |
| LLMZip 2023: 0.84 bits/char on a 1924 book posted to Gutenberg after training | Verified | arXiv 2306.04050 Table IV, 0.8426 (Dobie, *Legends of Texas*, Gutenberg 25 May 2023), as quoted in facts.md 30; re-verified by both round-8 critics |
| "No compressor beats it on average" | Verified | source-coding theorem |

No wrong, fabricated or uncited claim. Every empirical figure has its citation on screen: Shannon 1951, Brown/Francis & Kučera 1964, and Valmeekam et al. 2023.

## MECHANICS

| Measure | Value |
|---|---|
| Runtime | 3:34.7 |
| Pace | 152 wpm over speech time (143 overall); 497 narration words |
| Longest internal silence | 2.01 s (0:07.4, the planned prediction hold) |
| Lead / trail | 0.00 s / 0.56 s |
| Longest static stretch | 3.03 s (the closing hold) |
| Loudness | −14.0 LUFS / −1.7 dBTP |
| Other | WER 1.8 % (the differences are "a"→"one" and "Y"→"why", both homophones); 0 black frames; 0 banned phrases; layout audit 0 issues; 0 glyph morphs |

**Sync spot checks (word timing → frame):**
- "10.3" is spoken at 63.70 s, and the Z counter lands on 10.3 at 63.75 s.
- "entropy" is spoken at 92.46 s, and the cross-fade average → H runs at 92.5 s.
- "bits" is spoken at 93.16 s, and the axis title becomes "bits" by 93.5 s.
- "with 100 letters of context" is spoken at 180.6–182.6 s, and the green band is seeded at 1.0 and grows.
- "0.6 and 1.3" is spoken at 183.8–185.7 s, and "0.6–1.3" is written at 3:05.
- "Y" lands in the ? box on the spoken "Y".

Every round-8 sync complaint is resolved.

**Transcript.**
- No §4 phrase or pattern. "Is it Y?" is one question, not a chain.
- The hook question is complete by 0:07.5, followed by a 1.9 s hold. The viewer commits to "five" at 0:09–0:16.

## What I saw (flipbook)

- **0:00–0:22. Cold open and naive build.** Frame one is the context row, the ? box and 27 tiles (kf_01). The halving chain is built in place, and `log2 27 ≈ 4.75` is assembled from the chain's 27 (kf_04).
- **0:22–0:52. Target and failure.**
  - The tiles drop to become column feet and rise to 4.75. The ≈1 band appears with the Shannon citation, and the LLM tag points into the ? box on "language models".
  - The hatched "3.75 extra (79%)" follows.
  - E and Z are isolated, with real widths and ×130 (kf_07, clean).
  - The re-sort leads to the 48% brace.
- **0:52–1:21. Doubling strips to the derivation.**
  - The doubling strips run (E to 3.3, Z to 10.3, on its word).
  - p is copied from E's column (kf_13). The algebra steps land on their words.
  - The rigid "2" dips under the "=" into the subscript, and "log" is written after it lands. In my 5 fps crop nothing collides.
- **1:21–1:47. The crux.**
  - Heights morph to log2(1/p), and the ×28 inset opens.
  - The formula is assembled from its referents (kf_15). The skyline pours to 4.11, average becomes H, and "questions" becomes "bits".
  - The live meter reads 3.11 (kf_18). This is still the best passage in the series.
- **1:47–2:25. Context.**
  - The purple Q and "= ? bits" set up the prediction hold. U swallows the bar, and the average pours to 0.16.
  - The TH skyline and 68% brace follow, with E outlined (kf_22).
  - The bill appears alone, with the chart stepped out (kf_24, fixed since round 8).
  - 1.67 follows, then 2.81 with "H averaged over contexts" and the 1.81 meter (kf_26).
- **2:25–2:58. The person.**
  - The context arithmetic appears (see defect 1).
  - Shannon's record is revealed under a cursor while the context row reads along, and the 79/102 tally runs (kf_29, excellent).
  - The counts sort into lanes, and the guess skyline rises against ticks 0–6 (kf_31, now centred). It pours to ≈1.42, with the band as edges over the stack (kf_32, no teal).
- **2:58–3:19. The payoff line.**
  - It is built in story order in the silent turn (strip 2:57.8): the axis grows, then 4.75, 4.11 and 2.81 drop in, then 1.42 lands, then the title appears.
  - The band grows on its words. The LLM marker drops to 0.84 (kf_37).
- **3:19–3:34. Landing.** The record returns. THE OTHER DA rises into the boxes, and Y lands in the ? box. Frame one is re-seen with "1 guess" against "5 questions" (kf_40).

Colour semantics hold across the whole episode: blue is probability, yellow is questions/bits, green is Shannon's measurements, purple is context, grey is reference or abandoned. No slide-like frame appears.

## Defects found (evidence)

1. **2:28.6–2:31.6: the context arithmetic is written into a full-strength chart (Visual).**
   - In frames 2:29.6, 2:30.6 and 2:31.6 (extracted) and the strip at 2:28, "possible contexts: 27² = 729 → 27¹⁰⁰ ≈ 10¹⁴³" and "Brown Corpus: 5.75 M characters" are written in the strip between the context row and the chart top. The "bits" axis title sits beside them.
   - Underneath, the axes and ticks, the three dashed levels with their 4.11, 2.81 and "1.67 TH" labels, the stack, the band, "share after TH" and the Brown citation all stay at full strength for about 3 s. They dim only on "so" (strip frame 13, 2:31.0).
   - For those 3 s the frame has two focal structures, and the arithmetic reads as a chart title. This is the same pattern that was fixed for the run bill in round 8.
2. **3:08.5–3:16.0: the waiting LLM marker points at 1.42 (Visual / Clarity).**
   - Sheet 11 (3:09, 3:11, 3:13, 3:15) and kf_36 show the stack "1924 book / LLM / ▼ / 1.42 / ▼" in one column at x ≈ 600 px.
   - For about 7 s, while the narration describes the language model, the LLM triangle sits directly above the person's 1.42 value and reads as "LLM = 1.42". The marker leaves only on "It needed" (3:16).
   - The idea is right: the marker is born from the better guesser. But the parking spot makes a false reading for the whole sentence.
3. **3:00–3:19: "bits per character" reads as a sub-tag of "halving" (Visual).**
   - In kf_36 and kf_37 the axis title is a second row under "halving" at the far right (y ≈ 705 px), two rows below the axis.
   - On the left, "person / 102 letters" uses exactly the same two-row pattern for a tag and its qualifier, so the axis title reads as "halving: bits per character".
   - From 3:11 it is also dimmed to about 30 % with the stepped-back tags, so the line's only unit label is the faintest text in the frame.
4. **2:15.5–2:19.0: alignment in the bill (Visual, nitpick).** In kf_24, "= 6" sits under the "→" (x ≈ 1145 px), not under the "=" column of the row above (x ≈ 930 px). The "questions" baseline also sits about 7 px above the "5" it follows. The two "=" signs, which carry the comparison 5 against 6, do not line up.
5. **0:22.4–0:23.6: near-empty handover (Motion, nitpick).** Frame 0:23.0 shows only the dim tiles, a short grey baseline stub at the left and the 4.75 alone at the far right (x ≈ 1660 px). For about 1 s the eye has nothing to anchor on, between the halving diagram and the chart's birth.

I re-checked the round-8 defects and all are fixed: the payoff line build, the band on its words, the bill off the chart, the crux pace, the act turns, the Z counter, the travelling 2, the payoff word load, the guess-chart centring and ticks, the teal blend and the record return.

## Scores (reasoning)

- **Hook 9.** The viewer commits to the likely-wrong "five" by 0:09 after a 1.9 s hold. Tension rises through 4.75 → 4.11 → 0.16/1.67 → 2.81 → 1.42 → 0.84. The ending resolves the opening frame exactly: one guess against five questions.
- **Clarity 9.** Concrete before abstract. The formula is read off the doubling strip, and the area interpretation is shown. The sub-one cost is explained by the run bill. Every number checks out. Defect 2 is the only place a viewer could misread a value, and only for one sentence.
- **Visual 8.5.** Semantic palette, clean hierarchy, safe area respected. Defect 1 (a second focal structure for about 3 s) and defects 2–3 (a pointing ambiguity and an axis title that reads as a tag) are three small but real issues in the payoff half. They are not nitpicks: they break "one focal point" and the unambiguous labelling of the summary diagram.
- **Motion 9.** Every motion encodes a relation: the tiles become feet, the pour is the average, the 2 travels into the base, the counts sort into columns, the marker is born from the better guesser. The payoff line is now built. Only defect 5 remains, and it is minor.
- **Audio 9.**
  - Pace is 152 wpm, the crux has slowed and the four act turns are about 0.8 s.
  - Every deictic and number I spot-checked lands within 0.4 s.
  - Loudness is on target. "Is it Y" heard as "why" is a homophone that the flagging Y box resolves on screen.
- **Concision 9.** With 497 words, every line moves the argument. The twin line earns its place by licensing "treat each count as a symbol".
- **Originality 9.** The poured skyline and the Y-in-the-box landing are images a viewer would remember and share.

## FIXES (highest impact first)

1. **[2:28.6–2:31.6][Visual] One focal point while the context arithmetic is written.**
   - At the first glyph of "possible contexts" (2:28.6), step the whole chart back to 25 % in 0.5 s, then remove it on "so" as now. Fade the axes, ticks, the three dashed levels and their labels, the stack, the band and "share after TH".
   - Keep the Brown citation at full strength, since 5.75 M is a Brown figure.
   - Alternative: start the chart's fade-out on "Hundred-letter" (2:26.7), before the arithmetic begins.
   - This lifts Visual.
2. **[3:08.5–3:16.0][Visual/Clarity] Park the LLM marker where it cannot be read as 1.42.**
   - Keep its birth from the 1.42 triangle, then slide it in 0.6 s up 0.9 units and left to x ≈ 0.84 on the axis (above the band, clear of the 1.42 label column).
   - Wait there with the triangle at 40 % and the 1924 note above it.
   - On "needed" (3:16), drop it straight down onto 0.84. The fall then points at its own value, and nothing in the frame says LLM = 1.42.
3. **[3:00–3:19][Visual] Give the line's axis title its own place.**
   - Move "bits per character" off the tag rows. Centre it under the whole axis at x = 0, y ≈ 1.0 units below the "102 letters" row (Text ≥ 26, grey).
   - Keep it at full strength when the other tags step back on "book". It is the unit, not a story tag.
4. **[2:15.5–2:19.0][Visual] Align the bill's comparison.**
   - Put "= 6" in the "=" column of the row above, with the 6 under the 4.93's last digit column and "one at a time" left-aligned with "questions".
   - Bottom-align "questions" with the "5". This takes `next_to(..., aligned_edge=DOWN)` and a shared x for both "=" signs.
5. **[0:22.4–0:23.6][Motion] Remove the empty beat in the chart's birth.**
   - Start the x-axis growth from the tile row's own baseline position at the same moment the halving labels leave.
   - Or keep "questions per character" visible until the 4.75 has reached the gutter, so a referent stays on screen through the handover.

## REACHES 9 IF ALL FIXED: yes

- Fixes 1–3 remove the last frames with a second focal structure or an ambiguous label, which lifts Visual to 9. Weighted then comes to 9.0 (900/100), with no caps.
- Fixes 4–5 are polish that protects that margin.
- No structural change is needed: the hook, the failure beat, the visual insight and the landing are all in place.

## KEEP

1. The pour (4.11 → 0.16 → 1.67 → 1.42), with the formula assembled from its referents at 1:21–1:31.
2. The persistent context row: Shannon's record read under a cursor while the row reads along, and the Y landing in the ? box against "5 questions".
3. The run bill on an empty stage (p multiply / costs add, 5 against 6), and the story-order build of the bits-per-character line.
