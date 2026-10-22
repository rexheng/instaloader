# Round 10 review: craft (visual design, motion, A/V sync)

Critic: independent. My focus is visual design, motion craft and audio/visual sync, but every dimension is scored.

## Evidence

- **Pack.** I reused `review/`, because metrics.json (22:14:40) is newer than final.mp4 (22:12:25).
- **Read in full.**
  - Documents: report.md, narration_diff, all 12 contact sheets, transcript.txt, narration.txt and script.md.
  - Supporting files: the facts.md claims table, round9-craft.md and CHANGELOG round 9.
  - Word timings (transcript_words.tsv) at 1:33–1:52 and 2:46–2:56.
- **Full-resolution keyframes (21).** kf_01, 04, 07, 13, 15, 16, 18, 22, 24, 25, 26, 27, 28, 29, 31, 33, 36, 37, 38 and 40, plus a contrast-boosted crop of kf_31.
- **Extra extractions** (/tmp/claude-0/r10c):
  - 5 fps at 0:22–0:25 (the chart's birth)
  - 2.5 fps at 1:14–1:20 (the algebra)
  - 3.2 fps at 1:39–1:44 (the 3.75 → 3.11 meter)
  - 4 fps at 2:28–2:32 (the context arithmetic)
  - 3.2 fps at 2:48–2:53 (sorting the counts)
  - 5 fps with timecode at 2:50.0–2:53.2 (the log₂(1/q) label)
  - 4 fps at 3:19–3:23 (the landing handover)
- **Recomputed.** log₂27 = 4.755. 3.75/4.755 = 0.789. E/Z = 0.10314/0.000792 = 130.2. log₂(1/0.1031) = 3.28. log₂1263 = 10.30.
- **Run bill.** 0.683·0.670·0.072 = 0.03295 and log₂(1/0.0329) = 4.926. The costs are 0.550 + 0.578 + 3.796.
- **Guess counts.** The counts {79, 8, 3, 2, 2, 3, 1×5} give H = 1.4223 and log₂(102/8) = 3.672. Also 100·log₁₀27 = 143.1.
- **LLMZip.** I re-checked arXiv 2306.04050v2 (HTML table: 0.8426).

```
EPISODE: 007 — "How Much Information Is in a Letter?"
IDEA: A character costs log2(1/p) yes/no questions, so the average cost is the area of a skyline (width = probability, height = cost) poured flat; using more of what came before lowers it from the 4.75 of halving the alphabet toward about 1 bit.
SCORES: Hook 9 · Clarity 9 · Visual 9 · Motion 8.5 · Audio 9 · Concision 9 · Originality 9
WEIGHTED: 8.9 (892.5/100 = 8.925)   AFTER CEILING: 8.9 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none
FINAL: 8.9   PASS: no
```

## FACTS

| Claim | Status | Source / check |
|---|---|---|
| 27 symbols; five halvings 27→13→6→3→2→1 end on Y | Verified | kf_04 (cuts N\|O, U\|V, X\|Y, Y\|Z, Z\|␣) |
| log₂27 ≈ 4.75 ("the ideal") | Verified | 4.7549 |
| Shannon 1951: about 1 bit; 0.6–1.3 at 100 letters of context | Verified | BSTJ 30(1), p. 50 and p. 64 (facts.md 5, 28) |
| "four of every five questions"; 3.75 extra (79%) | Verified | 0.789 |
| E 10.3%, Z 0.08%, ×130; Z 1 in 1260 → 10.3 | Verified | 130.2; 1263 → 1260 at 3 s.f.; 10.30 |
| Space, E, T, A, O ≈ 48% | Verified | 0.4834 (facts.md 11) |
| E needs 3.3 doublings | Verified | 3.28 |
| p·2ᵏ = 1 ⇒ k = log₂(1/p); average = Σ p log₂(1/p) | Verified | re-derived |
| H = 4.11 for Brown letters; "four times Shannon's estimate" | Verified (corpus) | data.json H1 4.111 |
| After Q: U 98%, 0.16 bits; after TH: E 68%, 0.55, H 1.67 | Verified (corpus) | data.json; log₂(1/0.683) = 0.550 |
| Run E␣O: 0.683·0.670·0.072 = 0.0329; 4.93 both ways; 1+1+4 = 6 | Verified | recomputed |
| H averaged over two-letter contexts = 2.81 | Verified (corpus) | data.json H_given_2_prev |
| 27² = 729, 27¹⁰⁰ ≈ 10¹⁴³, Brown 5.75 M characters | Verified | 143.1; 5,751,047 |
| 79 of 102 right on the first guess; the record on screen | Verified | recount from kf_29 = Shannon p. 56 |
| Guess-count entropy ≈ 1.42, labelled "upper estimate"; log₂(1/q) = 3.67 | Verified | 1.4223; 3.672 |
| Twin argument | Verified | Shannon 1951, p. 55 |
| LLMZip: 0.84 bits/char on a 1924 book posted to Gutenberg after training | Verified | arXiv:2306.04050v2 Table IV, 0.8426 (web-checked this round) |
| "No compressor beats it on average" | Verified | source-coding theorem |

No claim is wrong, fabricated or uncited. Shannon 1951, the Brown Corpus (Francis & Kučera 1964) and Valmeekam et al. 2023 are each on screen while their numbers are shown.

## MECHANICS

runtime 3:34.6 · wpm 151 (speech time; 143 overall) · max silence 2.01 s (0:07.4, the planned prediction hold) · max static 3.03 s (closing hold) · −14.1 LUFS / −1.7 dBTP

- **Lead/trail and counts.**
  - Lead 0.00 s, trail 0.56 s, 0 black frames, 0 banned phrases.
  - WER 1.2 %. The differences are "a"→"one", "E's"→"ease", and "a hundred" dropped once, all homophones or articles.
  - The garbled whisper *segment* text at 1:34–1:53 is a segmentation artefact. The word timings (tsv) read cleanly: "four point one one … That beats four point seven five, but it's four times Shannon's estimate".
- **Layout audit.** 0 issues in 225 checks.
- **Sync spot checks:**
  - "four point seven five" is spoken 100.62–102.20 s. The gap meter grows to 3.75 by ~101.2 s and stands, then shrinks to 3.11 from 102.2 s, on "but". It is exact.
  - "pours" is spoken at 171.56 s and the guess skyline starts to pour at 172.2 s. "these three, not six" is spoken at ~2:15–2:17 and "→ 5 questions" and "1 + 1 + 4 = 6" land on it (sheet 8).
  - "needed" ("It needed point eight four") is spoken at ~3:15.5 and the LLM marker drops onto 0.84 by 3:17. The Y lands in the ? box on the spoken "Y" (3:23).
- **Hook.** The question is complete at 0:07.2, followed by a 2.0 s hold. The viewer commits to "five" at 0:08.8.

## What I saw (flipbook)

- **0:00–0:22.** Frame one is the context row, the ? box and 27 tiles (kf_01). The halving chain and `log₂ 27 ≈ 4.75` are built in place (kf_04).
- **0:22–0:52.**
  - In the 5 fps strip the tiles drop on a wave into column feet and rise to 4.75.
  - The band, citation and "floor" ghost follow, and the LLM tag points into the ? box.
  - The hatched 3.75 (79%) appears (kf_07). E and Z are isolated with ×130, then the re-sort to the 48% brace.
- **0:52–1:20.** The doubling strips run with live counters (kf_13). p is copied from E's column, and the two legal algebra steps follow (kf_15).
- **1:20–1:47.** The crux:
  - Heights morph, and the ×28 inset opens.
  - The formula is assembled from its referents (kf_16), and the pour gives 4.11 (kf_18).
  - The live meter goes 3.75 → 3.11 (strip).
- **1:47–2:27.**
  - Q, then "= ? bits". U swallows the bar and the average pours to 0.16 (kf_22).
  - The TH skyline and E at half a question follow.
  - The run bill appears on an empty stage (kf_24, kf_25), then 1.67 (kf_26) and 2.81 with "H averaged over contexts" and 1.81 extra (kf_27).
- **2:27–3:00.**
  - The context arithmetic is written over a chart already at 25 % (strip: fixed since round 9).
  - Shannon's record is read under a cursor with the context row reading along, and the tally reaches 79/102 (kf_28, kf_29).
  - The counts sort into lanes, the guess skyline rises (kf_31) and pours to ≈1.42, with the band as two strong edges, "upper estimate" and 0.42 extra (kf_33).
- **3:00–3:19.** The bits-per-character line is built in story order. The LLM marker waits over its own place with "?" (kf_36, fixed), then drops to 0.84 (kf_37). "bits per character" is now its own centred row at full strength (fixed).
- **3:19–3:34.** The record returns. THE OTHER DA rises into the boxes, and Y lands in the ? box. Frame one is re-seen with "1 guess" against "5 questions" (kf_38, kf_40).

I checked all five round-9 craft defects and all are fixed:
- the arithmetic over a dimmed chart
- the LLM marker parked over 0.84
- the axis title in its own row
- the bill's "=" under "=" and 6 under the 4 (kf_25)
- no lone-4.75 frame at the chart's birth

The palette holds across the whole episode: blue is probability, yellow is questions/bits, green is Shannon, purple is context, grey is reference or abandoned. No frame is slide-like.

## Defects found (evidence)

1. **2:51.1–2:52.1: the guess skyline's formula label is readable for about 1 s (Motion/Visual, reading time).**
   - In the 5 fps timecoded strip from 2:50.0, the columns finish rising at 2:50.2 and "1st / 2nd / 3rd+" fade in at 2:50.4–2:50.6.
   - `log₂(1/q) = 3.67` is written 2:50.4–2:51.2 and is complete only at about 2:51.2. It is already dimming at 2:52.0 and is gone as the pour starts at 2:52.2.
   - The 1st/2nd/3rd+ labels last about 1.8 s.
   - §5 requires an equation to hold for ≥ 2 s + 0.4 s per term, about 3 s here. This label is the one thing that tells the viewer the guess chart is "the same skyline" priced by the same formula. At the episode's second key pour, the reasoning flashes by, so the Motion anchor ("reading time respected") is not met here.
2. **3:19.7–3:21.5: a thin handover into the landing (Motion, minor).**
   - In the 4 fps strip, at 3:19.75 only the person's "1.42 / person / 102 letters" stays on screen. It is the last part of the payoff line to fade, so for a moment it reads as a stray label.
   - At 3:21.0 (sheet 12) the frame is only "THE OTHER DAY" floating mid-screen, with the boxes barely visible at 30 %.
   - The words "from the start" fall on this near-empty frame. The cold-open row should already be legible when "the start" is spoken.
3. **≈1:16.6: an intermediate glyph state that reads "k over 2" (Motion, nitpick).** In the 2.5 fps strip from 1:14 (frame 8, ≈1:16.8) the k sits directly above the travelling 2, which reads as a fraction "k/2 = 1/p" for about 0.3 s before k drops to the baseline.
4. **≈2:22.8–2:23.4: the meter reading grazes the 1.67 TH line (Visual, nitpick).** On sheet 8 at 2:23, "0.74 extra" rides about 18 px above the 1.67 dashed line while it counts, under the 0.15-unit spacing rule. It is transient, and it is clear by 2:25 (kf_27).
5. **0:22.4–0:22.8: brief lone 4.75 (Motion, nitpick).** In the 5 fps strip the tiles are at full strength, with a short centred baseline stub and the 4.75 alone at the far right, for about 0.4 s. This is much better than round 9 and is now only a nitpick.

## Scores (reasoning)

- **Hook 9.** A concrete row and a ? box from frame one. The viewer commits to "five" by 0:09 after a 2 s hold. Tension rises through 4.75 → 4.11 → 0.16 / 1.67 → 2.81 → 1.42 → 0.84. The ending re-sees the first frame: one guess against five questions.
- **Clarity 9.**
  - The argument goes concrete before abstract. The formula is read off the doubling strips, and the area is the average.
  - The sub-one cost is explained by the bill, and every number checks out.
  - Assumptions are stated: "upper estimate", "one passage, context 0–101", "H averaged over contexts".
- **Visual 9.** Every round-9 hierarchy defect is fixed, and each frame I read has one focal structure and clean margins. Only defect 4 remains, and it is transient. Defect 1 is also a reading-time breach of a §5 standard, but I score it under Motion to avoid double counting.
- **Motion 8.5.**
  - Every move encodes a relation: tiles become feet, the pour is the average, the 2 travels into the log base, the counts sort into columns, the meter measures each gap, the LLM marker falls onto its own value.
  - But the second instance of the central picture (2:50–2:52) is rushed. The label that ties it to the formula holds for about 1 s against a ~3 s requirement (defect 1).
  - The landing handover is thin (defect 2).
- **Audio 9.**
  - Pace is 151 wpm, with planned holds at the prediction and act turns.
  - Every deictic I checked lands within about 0.6 s: "these counts", "these three", "the same skyline", "is it Y".
  - Loudness is on target, and no term is mispronounced.
- **Concision 9.** 499 words, and each sentence moves the argument. Cutting the twin line or the 27¹⁰⁰ line would cost a justification.
- **Originality 9.** The poured skyline, the run bill (product versus sum), and the hidden Y re-seen as "1 guess" against "5 questions" are images a viewer would remember and share.

## FIXES (highest impact first)

1. **[2:50.2–2:53.7][Motion] Give `log₂(1/q) = 3.67` a 3 s read without adding narration time.**
   - Start writing it the moment the columns finish rising (2:50.2), at the same time as the 1st/2nd/3rd+ labels. It is then complete by about 2:50.8, on "The same".
   - Keep it at full strength through the pour. At "pours" (171.56 s), fade only its grey leader line, because the 2nd-guess column it points at is flowing away.
   - Fade the formula text only once the 1.42 level is born (≈2:53.7, on "one point four").
   - The label sits above y ≈ 440 px, and the poured stack only reaches about 610 px on the 0–7 axis before the zoom, so nothing collides.
   - Keep 1st/2nd/3rd+ until the pour starts.
   - This removes the only reading-time breach and lifts Motion to 9.
2. **[3:19.3–3:21.5][Motion] Make the landing handover continuous.**
   - Fade the person's 1.42 marker and tags with the rest of the line, not 0.4 s after it.
   - Start the cold-open row (12 boxes and the ? box, at 30 %) fading in during the line's fade (3:19.3), so the boxes are legible when "from the start" is spoken (≈3:20.5).
   - Then THE OTHER DA rises into boxes that are already waiting. No frame shows only a floating "THE OTHER DAY".
3. **[≈1:16.6][Motion] Avoid the momentary "k over 2".** Drop k to the baseline 0.15 s before the 2 passes beneath its x position, or route the 2 down-left below the "=" baseline. At no frame should k sit vertically above the 2.
4. **[2:22.8–2:23.4][Visual] Keep the meter reading 0.15 units clear of 1.67.** Hide "N extra" until the arrow top is at least 0.3 units above the 1.67 TH line. This is the same rule already used for the stack.
5. **[0:22.4–0:22.8][Motion] Start the baseline at full width under the tile row's span,** growing from the tile row's ends rather than from a centred stub, so the 4.75 is never the only right-hand element.

## REACHES 9 IF ALL FIXED: yes

- Fix 1 alone brings Motion to 9: 15 × 0.5 = 7.5 points, so the weighted score becomes 900/100 = 9.0, with no caps.
- Fixes 2–5 are polish that protects the margin.
- No structural change is needed. The hook, the measured failure, the visual insight (the poured skyline), the cited payoff and the landing that re-sees frame one are all in place.

## KEEP

1. The pour (4.11 → 0.16 → 1.67 → 1.42), with the formula assembled from its referents at 1:21–1:31, and the live gap meter synced to "four point seven five".
2. The persistent context row: Shannon's record read under a cursor while the row reads along, and the Y landing in the ? box against "5 questions".
3. The run bill on an empty stage (the product of the probabilities against the sum of the costs, 4.93 both ways, then 5 against 6) and the story-order build of the bits-per-character line with the LLM marker waiting over its own value.
