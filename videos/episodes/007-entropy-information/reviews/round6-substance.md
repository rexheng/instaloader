# Round 6 review: substance (facts, story, clarity, concision, slop)

Critic: an independent science and story editor. I recomputed every number, re-derived the formulas and checked the sources. All dimensions are scored.

Evidence used:
- `review/` pack. metrics.json (07:01) is newer than final.mp4 (06:54), so I reused it.
- report.md, transcript.txt, narration_diff.txt, narration.txt, script.md and facts.md.
- All 14 contact sheets.
- Full-resolution keyframes kf_01, kf_07, kf_17, kf_27, kf_28 and kf_31.
- Frames I extracted with ffmpeg at 0:53.0, 1:25.0, 1:29.2, 1:40.5, 2:36.5, 2:44.8, 3:10.8, 3:11.6, 3:21.5 and 3:37.5.
- A 5 fps strip of 2:35.6–2:38.0 (run costs → total).
- A 5 fps strip of 3:36.8–3:39.2 (LLM marker move).
- An independent Brown recount (my own script, not `data.py`).
- Web checks of Shannon 1951 (princeton.edu PDF) and LLMZip (arXiv 2306.04050v2, §IV).

```
EPISODE: 007 — "How Much Information Is in a Letter?"
IDEA: A character costs log2(1/p) yes/no questions, so the average cost (entropy, the area of a probability-wide, cost-tall skyline poured flat) falls from the 4.75 that halving the alphabet suggests to about 1 bit once the guesser uses what came before.
SCORES: Hook 9 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.6   AFTER CEILING: 8.6 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none
FINAL: 8.6   PASS: no
```

Weighted = (15·9 + 25·8.5 + 15·8.5 + 15·8.5 + 10·8.5 + 10·8.5 + 10·9) / 100 = 862.5 / 100 = 8.6.

## FACTS

My own recount of Brown (NLTK, 27 symbols) gives **N = 5,751,047** characters.

| Claim | Status | Source / check |
|---|---|---|
| 27 symbols; halving 27→13→6→3→2→1 takes 5 cuts | Verified | 2⁴ = 16 < 27 ≤ 32 |
| log₂27 ≈ 4.75 | Verified | 4.7549 |
| Shannon 1951: "about one" bit per letter | Verified | BSTJ 30(1):50–64, Jan 1951. Abstract: "something of the order of one bit per letter" (princeton.edu PDF, checked this round) |
| No compressor beats the true figure on average; LMs are trained by next-character/token prediction | Verified | source-coding theorem; standard LM objective |
| "Four of every five", on screen 3.75 extra (79%) | Verified | 3.7549 / 4.7549 = 0.789 |
| E 10.3%, Z 0.08%, ×130 | Verified | recount: 0.103137 / 0.000792 = 130.3 |
| Space, E, T, A, O ≈ half (48%) | Verified | recount: 17.48 + 10.31 + 7.63 + 6.66 + 6.26 = 48.34% |
| E needs 3.3 doublings; Z is 1/1260 and needs 10.3 | Verified | log₂(1/0.10314) = 3.28; 1/p(Z) = 1263; log₂ 1263 = 10.30 |
| p·2ᵏ = 1 ⇒ k = log₂(1/p); average = Σ p log₂(1/p) = area | Verified | re-derived; Σp = 1, so the area is the expectation |
| H₁ = 4.11 bits (Brown) | Verified | recount: 4.1111 |
| "Four times Shannon's estimate" | Verified | 4.11 / 1 |
| After Q: U 98%, cost ≈ 0, H = 0.16 | Verified | recount: 5,103 Q's; U 0.9814; log₂(1/0.9814) = 0.027; H = 0.156 |
| After TH: E 68%, cost ≈ 0.55, H = 1.67 | Verified | recount: 134,673 TH's; E 0.6833; 0.549; H = 1.667 |
| Run E R E ␣ after T H: 0.5 + 3.0 + 2.6 + 1.6 = 7.7 → 8 | Verified | recount: 0.549 + 2.959 + 2.564 + 1.626 = 7.699; ⌈7.699⌉ = 8 |
| Average over every two-letter context = 2.8 | Verified | recount: H(X ∣ 2 previous) = 2.8105 (H(X ∣ 1 previous) = 3.381) |
| 27² = 729; 27¹⁰⁰ ≈ 10¹⁴³; Brown 5.75 M characters | Verified | log₁₀ 27¹⁰⁰ = 143.14 |
| "Longer contexts need more text than any corpus holds" | Verified for the 100-letter contexts on screen; **imprecise as worded** | Brown handles 3-letter contexts easily (19,683 contexts). The claim holds for long contexts. See fix 8. |
| Shannon's subject: guesses until right; 79 of 102 on the first guess | Verified | p. 56: "Out of 102 symbols the subject guessed right on the first guess 79 times" (checked this round). On-screen record matches display (9); my tally 79/8/3/2/2/3/1/1/1/1/1 sums to 102 |
| Twin can rebuild the passage from the counts | Verified | Shannon p. 55, "identical twin" |
| Guess-count entropy ≈ 1.42; log₂(1/q₂) = 3.67 | Verified (arithmetic) | −Σ q̂ log₂ q̂ = 1.4223; log₂(102/8) = 3.672 |
| On-screen "≤ 1.42" | Verified as Shannon's eq. (17) applied with his own plug-in convention; **caveat** | It is an estimate from 102 samples. The Miller–Madow bias correction (m − 1)/(2N ln 2) ≈ 0.07 puts the bound itself nearer 1.49. Narration says "about one point four", which is fine. See fix 10. |
| "A better guesser could only lower it" | Verified | the guess distribution majorises; entropy is Schur-concave (facts #27) |
| Shannon N = 100: 0.6–1.3 bits | Verified | p. 64 bounds table / Fig. 4 |
| LLMZip 2023: 0.84 bits/char on a book released on Gutenberg after training, 27 symbols, inside the range | Verified | arXiv 2306.04050v2 §IV: "The compression ratio for LLaMA with arithmetic coding is only 0.8426 bits/character"; Gutenberg book of May 25, 2023; text8-style preprocessing (checked this round) |
| The hidden Y took 1 guess; halving took 5 | Verified for this letter | record line 3, Y = 1; chain at 0:13–0:21 ends on Y. The landing is true but cherry-picked: the subject averaged 198/102 = 1.94 guesses per character (see fix 9) |

There is no wrong, fabricated or misattributed claim. Every empirical claim has an on-screen citation: Shannon 1951 at 0:27–0:47 and 2:53–3:27, Brown at 0:48–2:52, Valmeekam et al. 2023 at 3:29–3:41.

## MECHANICS

- Runtime 3:57.7. Inside the cap, but only 2.3 s under 4:00.
- Pace 157 wpm over speech time (607 words).
- Longest internal silence 2.09 s (2:08.5, the planned Q prediction pause).
- Longest static stretch 3.5 s (the closing hold).
- Loudness −14.1 LUFS, true peak −2.2 dBTP.
- Leading silence 0.00 s, trailing 1.04 s.
- 0 black frames; layout audit 0 issues; WER 1.7%.

None of these triggers a cap.

ASR differences:
- "other" for "longer" (2:47) and the dropped "treat" (3:10.6) are segment-boundary artifacts. The surrounding words are intact and the craft critic's re-ASR confirms both.
- "pores" and "why" are homophones.

## TRANSCRIPT / SLOP

I searched the whole transcript for every §4 phrase and pattern:
- 0 banned phrases.
- No "it's not just X" constructions.
- No rhetorical-question chains. The three questions, at 0:04, 0:38 and 2:07, each stand alone and each gets an answer.
- No "it turns out", no fake reveals, no empty superlatives. The ending is not a recap.

The voice is specific and noun-heavy ("U swallows the bar", "Pour the skyline flat"). The single dry line, "A person.", lands. The hook question is spoken by 0:08, held 2.0 s, and "the natural answer is five" commits the viewer at 0:10. The reversal ("about one") arrives at 0:24.

## STORY / CLARITY NOTES

**What works.**
- The misconception-first structure is textbook Veritasium: 5 → 4.75 → "Shannon says about one". After that the gap meter keeps the tension measurable: 3.75 → 3.11 → 1.81 → 0.42.
- The derivation (doubling strips → p·2ᵏ = 1 → k = log₂(1/p) → area → pour) is the canonical picture, built from its referents.
- The landing re-sees frame one exactly: Y lands in the ? box.

**Where a careful viewer stalls.**
1. **2:28–2:38, the "fractions add up" demo shows a total but no saving.** The run box shows 0.5 3.0 2.6 1.6 → "7.7 → 8 questions". Nothing on screen says what 8 is better *than*. The comparison is asking whole questions letter by letter, ⌈0.55⌉ + ⌈2.96⌉ + ⌈2.56⌉ + ⌈1.63⌉ = 1 + 3 + 3 + 2 = 9 (already in `data.json`, not shown). Without the 9, "the fractions add up" is asserted, not demonstrated. This is the episode's hardest conceptual step, and it gets 10 s with ~28 px numbers in the top-right corner (kf_27, extracted frame at 2:36.5).
2. **3:19–3:41, the payoff number line carries four bare numbers.** 1.42, 2.81, 4.11 and 4.75 have no identity on screen (extracted frame at 3:21.5). The viewer must remember four numbers from the last two minutes to read the episode's summary picture. The dimmed record still fills the top 45% of the frame.
3. **2:52–3:41, the context row is stale.** It still shows purple **T H ?** throughout Shannon's record (kf_31). The episode taught that this row means "what's already read", but the subject is reading THERE IS NO REVERSE… The row is the episode's best device, and here it says something false.
4. **3:46–3:51, the landing equates guesses with yes/no questions.** "A single yes-or-no question" is true for this Y ("is it Y?"). But the episode's ~1-bit answer came from the *entropy of guess counts* (1.42), not from counting guesses, and on average this subject needed 1.94 guesses per character. Nothing false is said, but the 1-vs-5 contrast uses one lucky letter.

## FIXES (highest impact first)

1. **[2:34–2:40][Clarity] The fractional-question demo shows no saving.**
   - On "and the fractions add up", keep "7.7 → 8 questions" and add a grey row under it: "one at a time: 1 + 3 + 3 + 2 = 9". Build it by `TransformFromCopy` of each cost to its ceiling, with the four ⌈·⌉ results popping in yellow over 1.2 s.
   - Flag the 8 against the 9 for ≤ 1 s.
   - Raise the cost labels to `MathTex` font_size ≥ 36, and move the run's numbers into the empty chart area above the skyline (the skyline is dimmed at that moment) instead of the top-right corner.
   - Pay for it by cutting "like three point three doublings" (fix 4).
2. **[3:19–3:41][Clarity/Visual] The payoff markers are anonymous.**
   - Add a second label row under the axis numbers in grey `Text` 20–22 (ticks/citation size), one short tag per marker: "halving" (4.75), "letter odds" (4.11), "2-letter context" (2.81), "human guesser" (1.42), "LLM" (0.84, already labelled).
   - Fade the record to 0 when the line appears at 3:19.5; bring it back at 3:41 for the landing, which needs it.
   - Centre the number line at y ≈ 0.3 and scale it ×1.15, so the summary frame is the only focal object.
3. **[3:10.0–3:12.0][Motion/Clarity] The guess-count flight is unreadable.**
   - Verified at 3:10.8: ~102 numerals sit mid-flight on top of the passage text, a stray "1" sits on the "bits" axis title, and duplicate "3", "4" and "2" ghosts are visible.
   - Fly by guess number, so each column is born from its own counts: first all 79 ones (`lag_ratio` 0.01, run_time 1.0, paths dipping below the record), then the 2s, then the rest (0.8 s).
   - Drop the passage letters to 12% before the flight.
   - Place the "bits" axis title after the flight.
   - Take the ~1 s from a 0.5 s narration pause after "symbol" plus the existing 0.5 s gap at 3:09.8.
4. **[2:28–2:31][Audio/Concision] "like three point three doublings" points at nothing.** The doubling strips left at 1:35 and nothing on screen refers to 3.3 here (sheet 9, 2:29). Cut the phrase: "Half a question sounds impossible, but a compressor asks about long runs of letters, and the fractions add up." This saves ~1.6 s, which helps the 3:57.7 runtime.
5. **[2:52–3:41][Visual/Clarity] Make the context row tell the truth during Shannon's experiment.**
   - At 2:52, when the chart fades, clear T H back to empty boxes.
   - As the cursor walks the record (2:56–3:01), let the row show the last 12 characters the subject has read in purple, with the yellow ? box holding the letter under the cursor.
   - This ties the cold-open apparatus to Shannon's procedure for free, and makes the landing's THE OTHER DA → Y the natural end state rather than a cut.
6. **[2:36.6–2:37.4][Motion] Glyph soup from the run costs to the total.** The 5 fps strip shows "0.5 3.0 2.6 1.6" doubling into overlapping copies, then morphing into "7̶7̶.7" and "→ ° que…". Use `TransformFromCopy` of each cost into a "+" chain ("0.5 + 3.0 + 2.6 + 1.6"), then `TransformMatchingTex` to "= 7.7", then write "→ 8". No `Transform` between unlike glyphs.
7. **[1:24.6–1:25.4][Motion] The 3.3 → 2ᵏ copy garbles over its source.** The frame at 1:25.0 shows "3,3" overlapping the "3.3" counter.
   - Lift the copy 0.4 down (0.3 s) before it moves.
   - `FadeTransform` it into 2ᵏ along `path_arc=-0.5`.
8. **[2:47–2:52][Clarity, wording] "Longer contexts need more text than any corpus holds" overstates.** Three- to five-letter contexts are countable (Shannon lacked the *tables* in 1951; Brown handles N = 3 easily). Change it to "Contexts of a hundred letters need more text than any corpus holds…". The on-screen 27¹⁰⁰ already says this. Same word count.
9. **[3:46–3:51][Clarity] Make the landing honest about guesses vs bits.** Either:
   - change "a single yes-or-no question" to "a single yes-or-no question: is it Y?", so it is explicitly about this letter, or
   - add "1 guess" in green next to a grey "(1.9 per letter on average)" under it for 2 s.

   The first is cheaper and keeps the rhythm.
10. **[3:16–3:19][Clarity] "≤ 1.42" reads as a proven bound from 102 samples.** Relabel it "≈ 1.42 (upper estimate)", or keep "≤" and add a tiny grey "one passage" tag. The narration's "about one point four" is already right.
11. **[3:37.4–3:37.7][Motion] The "LLM" label passes through the "1924 book" note while both move** (5 fps strip). Move the note first (0.4 s), then the marker, or route the note up 0.3 before it slides left.
12. **[3:33–3:41][Visual] The book note is under the citation minimum.** "1924 book · on Gutenberg May 2023 · 27 symbols" measures ~22 px cap height (frame at 3:37.5). Set it to `Text` ≥ 18 at 24 px cap, or shorten it to "1924 book · online after training" at ≥ 26.

## REACHES 9 IF ALL FIXED: yes

Fixes 1, 2, 5, 8, 9 and 10 take Clarity to 9. Fixes 2, 5 and 12 take Visual to 9. Fixes 3, 6, 7 and 11 take Motion to 9. Fix 4 takes Audio and Concision to 9. That gives 135 + 225 + 135 + 135 + 90 + 90 + 90 = 900, so **9.0**, with Hook or Originality able to add a margin.

No structural change is needed: hook, measured failure, a picture that turns into the formula, a sourced payoff and a landing that re-sees frame one are all in place. The margin is thin, though. Every fix above has to land, and none may add runtime: the episode is already at 3:57.7.

## KEEP

1. The skyline **pour**: probability-wide, cost-tall columns collapsing into a level (4.11 / 0.16 / 1.67 / 1.42). The animation is the argument.
2. The **context row and the Y**: the cold-open row, the halving chain planting Y at 0:17, purple Q/TH, and Y landing in the ? box at 3:43.
3. **Shannon's real record** revealed under a cursor with the 79/102 tally, the identical-twin line, and the live gap meter (3.75 → 3.11 → 1.81 → 0.42 extra).
