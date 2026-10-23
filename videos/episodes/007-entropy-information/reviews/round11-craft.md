# Round 11 review: craft (visual design, motion, A/V sync)

Critic: independent. My focus is visual design, motion craft and audio/visual sync, but I score every dimension.

## Evidence

- **Pack.** I reused `review/`. metrics.json and report.md were written at 00:05, after final.mp4 (00:03).
- **Read in full.**
  - report.md and narration_diff.txt.
  - All 12 contact sheets.
  - transcript.txt, plus the word timings in transcript_words.tsv at 0:42–0:53, 1:39–1:52, 2:04–2:10, 2:58–3:06 and 3:19–3:24.
  - narration.txt and script.md.
  - round10-craft.md and the round-10 CHANGELOG, to check the claimed fixes.
- **Full-resolution keyframes (17).** kf_01, 04, 07, 13, 16, 18, 22, 25, 27, 29, 31, 33, 36, 37 and 40.
- **Extra timecoded strips** (`/tmp/claude-0/r11c`):

  | Window | Rate | What it shows |
  |---|---|---|
  | 0:22.0–0:24.4 | 5 fps | chart birth |
  | 0:48.0–0:51.2 | 5 fps | "That's nearly half" |
  | 1:13.6–1:17.6 | 4 fps | the algebra |
  | 2:04.0–2:08.0 | 4 fps | the bill handover |
  | 2:45.0–2:50.0 | 3.2 fps | the count sort |
  | 2:59.6–3:03.6 | 4 fps | the act turn into the line |
  | 3:19.0–3:22.2 | 5 fps | the landing handover |

- **Recomputed (Python, from data.json and the record).**
  - log₂27 = 4.755. 3.75/4.755 = 0.789. E/Z = 130.3, and 1/p_Z = 1263, which is 1260 at 3 s.f.
  - Top five = 48.3 %. H1 = 4.111. H given two letters = 2.810.
  - Run: 0.683·0.670·0.072 = 0.03295, log₂(1/0.03295) = 4.926. The costs are 0.550 + 0.578 + 3.796 = 4.924.
  - Guess counts {79, 8, 3, 2, 2, 3, 1×5}: n = 102, H = 1.422, log₂(102/8) = 3.672.
  - 100·log₁₀27 = 143.1. After Q, U = 0.981. After TH, E = 0.683.

```
EPISODE: 007 — "How Much Information Is in a Letter?"
IDEA: A character costs log2(1/p) yes/no questions, so the average cost is the area of a skyline (width = probability, height = cost) poured flat; feeding in more of what came before drops it from the 4.75 of halving the alphabet toward about 1 bit.
SCORES: Hook 9 · Clarity 9 · Visual 9 · Motion 9 · Audio 9 · Concision 9 · Originality 9
WEIGHTED: 9.0 (900/100)   AFTER CEILING: 9.0 (lowest 9 + 2 = 11, not binding)
CAPS: none
FINAL: 9.0   PASS: yes
```

## FACTS

| Claim | Status | Source / check |
|---|---|---|
| 27 symbols; five halvings 27→13→6→3→2→1 end on Y | Verified | kf_04: cuts at N\|O, U\|V, X\|Y, Y\|Z, Z\|␣ |
| "The ideal is log base two of 27: 4.75" | Verified | 4.7549 |
| Shannon 1951 put English at about 1 bit; 0.6–1.3 with 100 letters of context | Verified | BSTJ 30(1) pp. 50, 64; data.json `shannon_bounds_N100` [0.6, 1.3] |
| "No compressor beats it on average" | Verified | source-coding theorem |
| 3.75 extra (79 %) = "four of every five questions" | Verified | 0.789 |
| E 10.3 %, Z 0.08 %, ×130; Z 1 in 1260 needs 10.3 | Verified | 130.3; 1263; log₂1263 = 10.30 |
| Space, E, T, A, O ≈ 48 % | Verified | 0.4834 |
| E needs 3.3 doublings | Verified | log₂(1/0.1031) = 3.28 |
| p·2ᵏ = 1 ⇒ k = log₂(1/p); average = Σ p log₂(1/p) | Verified | re-derived |
| H = 4.11 for Brown letters; "four times Shannon's estimate" | Verified | H1 = 4.111 |
| After Q: U 98 %, 0.16 bits | Verified (corpus) | U = 0.981 |
| After TH: E 68 %, ≈0.55 questions; H = 1.67 | Verified (corpus) | 0.6833; 0.549; context_H 1.667 |
| Run E␣O: 0.0329; 4.93 both ways; 1 + 1 + 4 = 6 versus 5 | Verified | recomputed |
| Averaged over two-letter contexts: 2.81 | Verified (corpus) | H_given_2_prev 2.8105 |
| 27² = 729; 27¹⁰⁰ ≈ 10¹⁴³; Brown 5.75 M characters | Verified | 143.1; 5,751,047 |
| 79 of 102 on the first guess (Shannon's record) | Verified | recount from kf_29 |
| Guess-count entropy ≈ 1.42 ("upper estimate"); log₂(1/q) = 3.67 | Verified | 1.4223; 3.672 |
| Twin argument | Verified | Shannon 1951 p. 55 (facts.md) |
| LLMZip 0.84 bits/char on a 1924 book posted to Gutenberg after training | Verified | arXiv:2306.04050 Table IV (web-checked in round 10; facts.md) |

No claim is wrong, fabricated or uncited. Each source is on screen while its numbers are shown:
- Shannon 1951 at 0:24–0:37 and 2:31–3:08.
- Brown Corpus (Francis & Kučera 1964) at 0:41–2:29.
- Valmeekam et al. 2023 at 3:10–3:19.

## MECHANICS

runtime 3:34.8 · wpm 151 (speech time; 144 overall) · max silence 2.01 s (0:07.4, the planned prediction hold) · max static 3.03 s (closing hold) · −14.0 LUFS / −1.8 dBTP

- **Lead/trail and counts.**
  - Lead 0.00 s, trail 0.56 s. 0 black frames, 0 banned phrases, WER 1.4 %.
  - The diffs are articles read as "one", "pour" heard as "poor" (a homophone), and leading zeros. None is a mispronounced term.
  - The garbled whisper *segment* at 1:39.7–1:53.7 is a segmentation artefact. The word timings read "That beats 4.75 [100.28–101.90], but it's four times Shannon's estimate".
- **Layout audit.** 0 issues in 227 checks. 0 glyph morphs, 0 unlanded deictics.
- **Hook.**
  - The question is complete at 0:07.5, followed by a 2.0 s hold.
  - The viewer anchors on "five" at 0:09.3, well before 0:12.
- **Sync spot checks (word timings against strips):**
  - "O?" is spoken at 47.84 s, and the fifth column's white flash is on screen at 48.0–48.2 s.
  - "That's nearly half" is spoken at 49.20–50.18 s. The yellow cut rises from 49.6 s, and the 48 % brace is complete at 50.2 s, the moment "half" ends.
  - "4.75" is spoken at 100.28–101.90 s, and the meter stands at 3.75 extra (sheet 6, 1:41). It reads 3.11 on "four times" (1:43).
  - "context" is spoken at 183.58–184.22 s, and the green band grows from 3:03.1.
  - "Y" is spoken at 202.46 s, and the Y is in the ? box by 3:22.0 (0.4 s early, inside the window).
  - "is it Y" flags the box (sheet 12, 3:27). "five" brings the chain and "5 questions" to full strength (3:29).

## Round-10 craft defects: re-checked against this master

1. **The log₂(1/q) = 3.67 hold is fixed.**
   - In the 2:45–2:50 strip it is complete at 2:49.7, as the columns finish rising.
   - It is still on screen at 2:53.0, during the pour (sheet 10), so the complete hold is about 3.5 s or more.
   - The 1st/2nd/3rd+ labels arrive with the first flying counts (2:47.5).
2. **The landing handover is fixed.**
   - At 3:19.8 the whole line fades in one move, and the 12 boxes are already legible at 3:20.0, before "from the start" (200.52 s).
   - The phrase rises and spreads to the box pitch (3:21.0–3:21.8) and lands in boxes that are already waiting.
3. **The "k over 2" state is gone.** The 2 leaves the base down-left and runs under the row. A different, milder transient remains (defect 1 below).
4. **The meter clearance is fixed.** At 2:23 the reading "1.58 extra" rides well above the 1.67 line.
5. **The baseline is fixed.** At 0:22.6 it appears at full width under the tile row's span, with no centred stub. The tiles then drop into column feet on a left-to-right wave (0:23.2–0:24.0).

## What I saw (flipbook)

- **0:00–0:22.**
  - Frame one shows the purple context row and the yellow ? box over 27 blue tiles (kf_01).
  - The halving cuts and the chain are built in place, ending in `log₂ 27 ≈ 4.75` (kf_04).
- **0:22–0:52.**
  - The tiles become column feet and rise to 4.75, then the band, the citation, the "floor" ghost and the LLM tag appear.
  - The hatched 3.75 extra (79 %) follows. E and Z are isolated, then given real widths with 10.3 % / ×130 / 0.08 % (kf_07). Gap-free re-sort, the 48 % brace.
- **0:52–1:20.**
  - The doubling strips run with live counters, 3.3 and 10.3 (kf_13).
  - p is copied from E's column, then the algebra runs in two legal steps.
- **1:20–1:47.** The crux:
  - The heights morph to log₂(1/p), and the ×28 inset opens.
  - The yellow area sweep becomes "average = Σ p log₂(1/p)" (kf_16). The pour gives 4.11 and H (kf_18).
  - The live meter reads 3.75 → 3.11 against the ghost.
- **1:47–2:27.** Context:
  - Q, then "= ? bits". U swallows the bar, and the axis zooms to 0.16 (kf_22). The TH skyline follows, with E at half a question.
  - The run bill appears on an empty stage, with the product against the sum and 5 against 6 (kf_25).
  - The levels pour to 1.67, then 2.81 with "H averaged over contexts" (kf_27).
- **2:27–3:00.**
  - The context arithmetic is written over a chart at 25 %. Shannon's record is read under a cursor while the row reads along, reaching 79/102 (kf_29).
  - The counts sort into lanes and the guess skyline rises (kf_31), then pours to ≈ 1.42. It is marked "upper estimate" and "0.42 extra" (kf_33).
- **3:00–3:19.**
  - The bits-per-character line is built in story order, and the band grows on "context".
  - The LLM marker waits with a "?" (kf_36), then drops onto 0.84 inside the band (kf_37).
- **3:19–3:35.** The landing returns to frame one, re-seen: THE OTHER DAY in the row, the Y in the ? box, "1 guess" against a dimmed "5 questions" (kf_40).

**Overall.**
- The palette holds for the whole runtime: blue is probability, yellow is questions/bits, green is Shannon's measurements, purple is context, grey is reference or abandoned.
- No frame is slide-like. Every hard transition happens at a beat boundary and carries an object across it: the context row persists from 0:00 to 3:35.

## Defects found (evidence). All are nitpicks or minor.

1. **[1:14.35–1:17.35] The algebra still passes through two misleading glyph states (Motion, minor).**
   - In the 4 fps strip, at 1:14.35–1:14.85 a lone multiplication "·" stays to the left of `2ᵏ = 1` after p has dropped into the denominator.
   - At 1:16.35–1:17.10 (about 0.75 s) the line reads `k =   1/p`, with a small subscript 2 floating below the gap, before "log" is written at 1:17.35.
   - This is the episode's one derivation step, and for most of a second the formula on screen is wrong. The three-move choreography fixes "k/2" by adding a different detour.
2. **[2:21–2:29, kf_27] The 2.81 frame is the busiest in the video (Visual, minor).**
   - The frame holds a reference level (4.11), a new level (2.81) with a yellow in-plot label, the TH level with its purple tag (1.67 TH), the meter with "1.81 extra", the formula, and the note "H averaged over contexts". That is 4 hues and about 9 words of label.
   - The line also reads `H = Σ p log₂(1/p) = 2.81`. The formula as written is the single-context entropy, while 2.81 is that quantity averaged over contexts. The note rescues this, but the eye goes to the equation first.
3. **[3:00.6–3:02.6] The line's markers and tags build under unrelated words (Visual/sync, minor).**
   - About 8 labels drop in: 4.75 halving, 4.11 no context, 2.81 2-letter context, then 1.42 person / 102 letters.
   - The words over them are "Shannon's tests, with a hundred letters of context". None of those markers is Shannon's tests.
   - The spoken referent (the band) arrives correctly on "context", at 3:03.1. The tags stay on screen until 3:19, so reading time is not breached, but for 2 s the eye and the ear are on different objects.
4. **[3:20.2–3:20.8] The record flashes back for about 0.6 s (Motion, nitpick).**
   - Shannon's three-line record fades up to about 22 % and is gone again by 3:21.0. It reads as a flicker rather than an origin.
   - The phrase rises cleanly afterwards.
5. **[3:00.35] The new axis starts growing over the fading guess chart (Visual, nitpick).** For about 0.25 s the line's left segment crosses the chart's "≈1" label while that chart is at about 40 %.
6. **[2:54–3:00, kf_33] The band edges are heavy (Visual, nitpick).**
   - The band's two green edges are 5 px rules across the whole stack. The 1.3 edge sits only about 30 px below the 1.42 dashed level, and the 0.42 meter crosses it.
   - The result is three near-parallel lines at the top of the stack.

## Scores (reasoning)

- **Hook 9.**
  - The concrete row and ? box appear from frame 1, the question is complete at 0:07.5 with a 2 s hold, and the viewer is anchored on "five" by 0:09.
  - Tension rises through 4.75 → 4.11 → 0.16 / 1.67 → 2.81 → 1.42 → 0.84, and the ending re-sees frame one as "1 guess" against "5 questions".
  - It is not a 10: the first frame is clean but not irresistible, because the sentence is hidden at 9 %.
- **Clarity 9.**
  - It runs concrete before abstract: the doubling strips come before p·2ᵏ = 1, the area before the formula, and the bill before "half a question".
  - Every number checks out, and the assumptions are on screen: "upper estimate", "one passage, context 0–101", "H averaged over contexts".
  - Defect 2 is the one notational blur, and it is labelled.
- **Visual 9.**
  - Each keyframe I read has one focal structure, safe margins, legible type, and colour that never changes meaning. Citations sit above the caption zone.
  - Defects 2, 5 and 6 are minor or transient. Nothing is decorative.
- **Motion 9.**
  - Every move encodes a relation:
    - tiles become feet
    - heights morph to cost
    - the sweep becomes Σ
    - the pour is the average
    - counts sort into share-width columns
    - the meter measures each gap
    - the LLM marker falls onto its own value
    - the phrase rises into its boxes
  - All round-10 reading-time breaches are fixed (verified in the strips). Static stretches never exceed 3.03 s.
  - Defect 1 is the remaining blemish. It lasts under 1 s and does not stop me believing a top channel's team made this, but it is the first thing to fix.
- **Audio 9.**
  - Pace is 151 wpm, with planned holds at the prediction (2.0 s) and the Q (1.4 s). Loudness is on target, and no term is mispronounced.
  - Every deictic I timed lands within about 0.5 s: "nearly half", "these three", "these counts", "the same skyline", "is it Y".
  - Defect 3 is a visual-side mismatch rather than drift.
- **Concision 9.**
  - 500 words in 3:34.8. Every sentence carries a step:
    - The detour on half a question is what justifies sub-one costs.
    - The 27¹⁰⁰ line is what justifies asking a person.
    - "That caps the text" is what justifies "upper estimate".
  - The repeats are deliberate callbacks: "log base two of", and 4.75 at 1:40.
- **Originality 9.**
  - The poured skyline, the run bill (the probabilities multiply while the costs add), the guess record re-plotted as the same skyline, and the hidden Y landing against "5 questions" are images a viewer would remember and share.

## FIXES (highest impact first; none is needed to pass)

1. **[1:14.3–1:17.4][Motion] Make the second algebra step one continuous move.**
   - Fade the "·" together with p when p drops (same 0.4 s).
   - Then replace the three-move step with a single 1.4 s `TransformMatchingTex(2ᵏ = 1/p → k = log₂(1/p))`. Give the 2 a `path_arc` of about −1.2 rad, so it swings down and right into the log's subscript slot. Drop k into place in the same animation, and Write "log" over the same interval, timed to land on "log" (≈ 76.0 s).
   - At no frame should `k = 1/p` be readable without its log.
2. **[2:21–2:29][Visual/Clarity] Unclutter the 2.81 frame and make the equation say what it is.**
   - When the 2.81 level is born, dim the 1.67 level and its "TH" tag to 40 %.
   - Delete the in-plot "all two-letter contexts" label. The gutter reads "2.81", and the note under the equation already names it.
   - Write the slot as `= 2.81 bits (average)`, or swap H for H̄ with a short cross-fade, so the formula line is not literally Σ p log₂(1/p) = 2.81.
3. **[3:00.4–3:02.6][Visual/Sync] Put the line's markers in the act turn, not under "Shannon's tests".**
   - Option A: extend the silent act turn by 0.6 s, so the four markers have landed before 181.0 s. This costs runtime.
   - Option B: drop the three reference markers (halving, no context, 2-letter) at 30 % immediately and the person's at 60 %. On "Shannon's tests" only the 0–5 axis is bright, and the band grows on "context" as now.
4. **[3:20.2–3:20.8][Motion] Remove the record's 0.6 s flicker.** Either bring back only THE OTHER DAY at full strength, rising from where it sat in the record, or hold the record at 22 % for at least 1.2 s before the other lines leave.
5. **[3:00.35][Visual] Start the axis growth 0.3 s later,** once the guess chart's fade is complete, so nothing crosses the fading "≈1".
6. **[2:54–3:00][Visual] Thin the band edges** on the guess chart from 5 px to 3 px, at 70 % opacity, so they are not a third heavy rule beside the 1.42 dashed level and the meter.

## REACHES 9 IF ALL FIXED: yes (already at 9.0)

- No cap applies, and every dimension sits at its 9 anchor. The remaining items are nitpicks.
- Fixes 1 and 2 are the ones that would protect the margin, by removing the last momentarily wrong formula state and the one crowded frame.
- No structural change is needed. The hook with a commitment, the measured failure (3.75 extra, 79 %), the one picture (the poured skyline) that changes into Σ p log₂(1/p), the cited payoff and the landing that re-sees frame one are all in place.

## KEEP

1. The pour (4.11 → 0.16 → 1.67 → 1.42), with the formula assembled from its referents at 1:21–1:31, and the live gap meter on "four point seven five".
2. The persistent context row from 0:00 to 3:35: it reads along under Shannon's record, and the Y lands in the ? box against "5 questions".
3. The run bill on an empty stage (0.0329 against 4.93 both ways, then 5 against 6), and the LLM marker waiting with a "?" above its own value before dropping onto 0.84.
