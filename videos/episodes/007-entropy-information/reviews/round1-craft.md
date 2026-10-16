# Episode 7, review round 1 (craft critic: visual design, motion, A/V sync)

Evidence: the existing `review/` pack (metrics.json 23:28 is newer than final.mp4 23:26): report.md, narration_diff.txt, all 13 contact sheets, and these full-resolution keyframes: kf_01 (0:03.8), kf_03 (0:25.9), kf_07 (0:52.0), kf_10 (1:08.9), kf_14 (1:23.7), kf_16 (1:45.2), kf_17 (1:51.0), kf_19 (1:58.4), kf_21 (2:22.4), kf_23 (2:31.6), kf_26 (2:38.7), kf_28 (2:50.9), kf_30 (2:58.8), kf_33 (3:13.3), kf_36 (3:29.7), kf_37 (3:39.8), kf_40 (3:54.6). I also pulled extra ffmpeg frames at 0:27.0, 1:29.0, 1:32.5, 1:35.5, 2:16.0, 2:32.5, 2:51.6, 2:52.6 and 3:45.0. I read the transcript and word timings, script.md, narration.txt, facts.md and data.json, recomputed the corpus and guess-record numbers from data.json, and checked LLMZip Table IV on arXiv (v2).

```
EPISODE: 007 — "How Much Information Is in a Letter?"
IDEA: A character costs log2(1/p) yes/no questions, so how much information it carries depends on how predictable it is; averaged over English with the preceding text as context, that is about 1 bit per character, not the 4.75 you get by halving the alphabet.
SCORES: Hook 8 · Clarity 8 · Visual 8 · Motion 8 · Audio 8 · Concision 8 · Originality 8
WEIGHTED: 8.0   AFTER CEILING: 8.0  (lowest 8 + 2 = 10, not binding)
CAPS: none
FINAL: 8.0   PASS: no
```

## FACTS

| Claim | Verdict | Source / check |
|---|---|---|
| 27 symbols (26 letters + space) | Verified | Shannon 1951 p. 56 |
| Halving 27 → 1 takes 5 cuts; chain 27→13→6→3→2→1 | Verified | arithmetic (2⁴ < 27 ≤ 2⁵) |
| log₂27 ≈ 4.75 | Verified | 4.7549 |
| Shannon 1951 estimated "about one" bit per character | Verified | Shannon 1951 p. 50; bounds 0.6–1.3 at N = 100, p. 64 |
| No text compressor can beat the true entropy rate on average | Verified | source-coding theorem; worded about the true figure, not the estimate |
| "3.75 extra (79%)" | Verified | 3.75 / 4.75 = 0.789 |
| E 10.3 %, Z 0.08 %, ×130 | Verified | data.json: 0.10314, 0.000792, ratio 130.3 |
| Space+E+T+A+O ≈ half of text (48 %) | Verified | 0.4834 |
| E needs 3.3 doublings; Z 1 in 1260, needs 10.3 | Verified | log₂(1/0.1031) = 3.28; 1/p = 1263; log₂ = 10.30 |
| p·2ᵏ = 1 ⇒ k = log₂(1/p) | Verified | algebra |
| H = Σ p log₂(1/p) = 4.11 bits (Brown, 27 symbols) | Verified | recomputed 4.1111 |
| "Four times Shannon's estimate" | Verified | 4.11 / ~1 |
| After Q: U 98 %, H = 0.16 | Verified | 0.9814; 0.156 |
| After TH: E 68 %, cost ≈ 0.55 ("about half a question"), H = 1.67 | Verified | 0.6833; 0.549; 1.667 |
| All two-letter contexts: 2.81 | Verified | data.json H_given_2_prev = 2.8105 |
| 79 of 102 on the first guess | Verified | Shannon 1951 p. 56; recount from the record = 79/102 |
| Guess-count entropy ≈ 1.42 bits | Verified | recomputed 1.4223 from counts {1:79, 2:8, 3:3, 4:2, 5:2, 6:3, 7,8,11,15,17:1} |
| Identical-twin reconstruction | Verified | Shannon 1951 p. 55 |
| "A better guesser could only lower it" | Verified (simplified) | majorisation argument in facts.md #27 holds for ideal ranking |
| 0.6–1.3 bits/char with 100 letters of context | Verified | Shannon 1951 p. 64 |
| LLM: 0.84 bits/char on part of a book released after training, 27 symbols | Verified | Valmeekam et al. 2023, arXiv:2306.04050 v2, Table IV (M = 511, Nc = 508,463, ρ_LLaMA+AC = 0.8426) |
| The hidden character is the Y of THE OTHER DAY, guessed first time | Verified | record line 3 |

No wrong, fabricated or uncited claims found. Every empirical number has an on-screen citation (Shannon 1951 at 0:29–0:53 and 2:53–3:27, Brown Corpus 0:51–2:52, Valmeekam 3:29–3:40).

## MECHANICS

runtime 3:54.6 · wpm 160 (speech) / 156 (overall) · max silence 1.96 s (0:08.3, the planned prediction hold) · max static 3.63 s (3:51.0 end hold) · −14.0 LUFS / −1.9 dBTP · leading 0.00 s, trailing 1.24 s · black frames 0 · layout audit 0 issues · banned phrases 0 · WER 2.0 %. No cap triggered. The runtime is 5.4 s inside the 4:00 cap, so any beat added below has to be paid for with a cut.

## What I saw (flipbook notes)

- **0:00–0:25:** strong, quiet open. The row of "already read" boxes ends in a yellow ? (kf_01), the question is posed by 0:08, and the hold is silent (0:08.3–0:10.2). The halving cuts and the 27→1 chain build one cut per spoken step, and log₂27 ≈ 4.75 is assembled in place (kf_03). Clean.
- **0:27–0:53:** the tiles drop onto a baseline and become columns (0:27 shows the baseline origin starting to grow, not a stray glyph), then rise to 4.75 together. The green ≈1 band sits behind them and the hatched "3.75 extra (79%)" block lands on "four of every five". The E/Z isolation and the real-width reflow (kf_07) are excellent: the same columns take their Brown widths while heights stay fixed, which is the "same price" argument made visible.
- **0:55–1:23:** the re-sort without gaps works. The flash sweeps through space, E, T, A, O as each is named (1:01 shows T outlined), and the 48 % brace arrives on "nearly half". The doubling strips (kf_10, kf_14) are the best idea in the video: one cut, the kept half stretches, and the counter runs to 3.3 and then 10.3.
- **1:25–1:37:** the key derivation is built in the right-hand margin, beside the strips (1:29, 1:32.5, 1:35.5). The algebra moves are legal and timed to the words, but the episode's central formula gets the least prominent position on screen.
- **1:39–2:13:** the 27 heights morph from 4.75 to log₂(1/p) (kf_16, with a correct ×28 inset). The Σ assembly (kf_17), the pour into full-width slabs and the 4.11 level (kf_19) are the visual insight, and they land.
- **2:14–2:52:** the context beats are strong (kf_21, kf_23, kf_26, kf_28), with the y-axis zoom, the "?" slot in the equation and the 4.11 grey reference. Weak spots: the prediction pause at 2:15 is filled with the unpour (2:16 frame); U sits at its old height while 98 % wide (kf_21, 2:19–2:23); and the "fractions add up" step has only a four-? run as its picture (2:41–2:44).
- **2:53–3:18:** Shannon's real record revealed under a cursor (kf_30) is the right exhibit. The twin fade/rebuild and the guess-count skyline (kf_33) reuse the episode's own picture, which is good. The 1.42 level is poured from it.
- **3:19–3:37:** the bits-per-character ladder (kf_36) is clean. The LLM marker then slides from 4.75 down the whole line before dropping at 0.84 (sheets 3:29–3:35).
- **3:38–3:54:** "THE OTHER DAY" floats alone, small and right of centre, on an otherwise empty frame (kf_37, about 3:38.5–3:42). Then it docks into the cold-open row, with "1 guess" against "5 questions" (3:45, kf_40). The ending re-sees frame one exactly, and the idea lands.

## FIXES (highest impact first)

1. **[2:34–2:44][Clarity + Motion] "The fractions add up" is asserted, not shown.** The only picture is the ? box widening into four ? boxes (sheet 2:41–2:43). The viewer is told that half a question becomes possible but never sees fractions sum to a whole. **Change:** when the slot widens, fill the four boxes with the record's actual run "E R E ␣" (from THERE, so it ties to the payoff text). Under each box, write its ideal cost in yellow, computed by `data.py` from the two-letter-context table (log₂ 1/p(x | previous two)). Then grow one yellow brace under the four that sums them and rounds up to a whole number of questions ("≈ N questions for 4 letters"), all on "and the fractions add up". Then pour the TH skyline as now. This turns the one transition that needs a rewatch into a picture, and lifts Clarity to 9.
2. **[3:29–3:35][Motion] The LLM marker's 6 s slide from 4.75 past 4.11, 2.81 and 1.42 encodes a trajectory that does not exist.** The model never "passed through" those values; the move is decorative and implies a progression. **Change:** on "a language model", spawn the marker with `TransformFromCopy` from the 1.42 (human guesser) triangle, recoloured INK and stacked "LLM" above it. Hold it there through "compressing part of a new book in the same twenty-seven symbols". On "needed point eight four", move it the short distance 1.42 → 0.84 into the band. Now the motion means "a better guesser lowers it" and pays off the 3:17 line. Edit around `scene.py` L1567–1580 (drop the `shift(RIGHT * (nx(LLM_BPC) - nx(H0)))` from H0).
3. **[2:14.4–2:17.5][Hook + Motion] The prediction pause after "What comes after a Q?" is spent watching the 1.4 s unpour** (frame 2:16.0: slabs mid-flight). The viewer's eye is pulled to the chart rebuilding instead of to the Q and the question. **Change:** in `context()` (L1230–1238), move `self.unpour(P, prior, run_time=1.4)` and `show_labels()` to the end of the previous beat (during "as if nothing came before it", 2:11–2:13.9). The question beat then only swaps in the purple Q, sets the equation slot to "?" and holds a static frame for the 1.3 s pause (raise the pause to 1.6 s if the clock allows).
4. **[1:25–1:37][Visual] The episode's main equation is built small, in the right margin** (x ≈ 2.8–6.0, beside the strips; frames 1:29, 1:32.5, 1:35.5). It competes with the two bright strips and the counters, so there is no single focal point while the formula is born. **Change:** at 1:22.5, once both strips are full, dim the strip bodies to 40 % and keep the 3.3/10.3 counters bright. Build `p · 2^k = 1` centred at x = 0 in the clear band between the strips and the chart (y ≈ 0.9), at font_size 56, with p copied from E's column and 2ᵏ from the counters as now. Run the two algebra steps there, then carry `k = log₂(1/p)` up to its 1:39 title position as it already goes.
5. **[3:38.5–3:42][Visual + Motion] The landing reveal plays on an almost empty frame.** "THE OTHER DAY" sits alone at about x = +2.4, y = +1, small (kf_37), for about 3 s while the narration delivers the payoff line, and the boxes only arrive afterwards (3:43). **Change:** fade the cold-open row of 12 boxes plus the ? box in at 30 % while the record fades (3:37.5). THE OTHER DA then flies straight into its boxes, and the Y drops into the ? box on the spoken "Y" (3:40.4). The reveal becomes one transform into frame one rather than a float, then a dock.
6. **[2:19–2:23 and 2:29–2:33][Clarity + Motion] The two-step re-price shows a wrong intermediate state.** U widens to 98 % at its unconditional height of 5.48 (kf_21) and stays there about 3 s, so the drawn area momentarily reads as about 5.4 bits after Q, above the 4.11 reference. The TH beat does the same with E at 3.28 (kf_23). **Change:** start the height change on "swallows" (2:20.5) instead of "its cost drops" (2:22.2), overlapping width and height so the area never exceeds the previous level. For TH, start E's re-price on "two thirds" rather than after the brace completes.
7. **[2:45–2:52][Clarity] The ladder mixes two distributions without saying so.** The equation still reads "= 1.67 bits" and the x title still says "share after TH" while the narration says "averaged over every two-letter context, it's still 2.8" (frame 2:51.6). **Change:** on "Averaged over every two-letter context", dim the TH stack to 30 % and attach a small purple "TH" tag to the 1.67 number. Then grow the 2.81 line and turn the equation value grey with "2.81" copied in from the gutter, so the equation always matches the level being discussed.
8. **[3:04–3:18][Clarity] The guess-count skyline is not re-anchored to the formula.** The viewer sees "the same skyline" (kf_33) but is not shown that the heights are log₂(1/share) again. **Change:** when the guess columns land, copy `log₂(1/q)` in yellow from a small reprise of the equation (or write it next to the 2nd-guess column with its value 3.7), and label the poured level "≤ 1.42" (upper bound), so "a better guesser could only lower it" has a visible referent.
9. **[0:35.8–0:39.3][Audio/Visual sync] "Guessing what comes next is how language models are trained" has no visible referent.** The only thing on screen is a faint purple ripple on dim boxes behind a dominant chart (sheet 0:37). **Change:** during this line, place the same INK "LLM" tag used at 3:29 beside the ? box with a short arrow into it, then fade it. This seeds the 3:29 payoff and lets the deictic land.
10. **[3:28.5–3:29.5][Visual] The citations cross-fade in the same spot**, garbling "Shannon, 1951…" and "Valmeekam et al., 2023…" on top of each other (sheet 3:29). **Change:** fade the Shannon citation out completely (0.3 s) before fading in Valmeekam (use `Succession`, not simultaneous animations).
11. **[2:53–3:05][Visual] The record frame is dense:** about 20 words of prose plus 102 counts plus the tally (kf_30), above the 12-word load, with empty bands above y = +2 and below y = −1.3. **Change:** scale the record group by 1.12 so the counts are easier to read, and keep lines not yet reached at 15 % (not 20 %) so the cursor line is the clear focal point. The tally stays as it is.
12. **[0:10–0:25][Hook/Concision] The surprise ("about one") lands at 0:26.** Cut "With perfect fifty-fifty splits," (about 1.5 s) and say "The ideal is log base two of twenty-seven, about four point seven five". Also fold "Q and TH are the easy cases." into "But averaged over every two-letter context, it's still two point eight" (about 2 s). This buys about 3.5 s of clock for fixes 1 and 3 while staying under 4:00.
13. **[2:45.5][Audio, verify] Check "TH" at 2:45.5.** The override "tee aitch" is in place, but Whisper transcribes "th" at 2:45.5 in 0.32 s, much shorter than at 2:28.9 (0.74 s). Listen. If it comes out as one clipped syllable, insert a comma ("Q, and T H, are the easy cases") or slow that sentence slightly.

REACHES 9 IF ALL FIXED: yes. The structure is right: misconception committed by 0:08, a measured failure (79 % extra), a picture-first derivation (doubling strips, then skyline, then pour), two iterations (frequency, then context), a real cited payoff, and an ending that re-sees frame one. What holds it at 8 is local: one asserted step (fractions), two motions that carry no true relation (the LLM slide, the unpour inside the prediction pause), one off-focus equation build, and a sparse reveal frame. Fixes 1–5 alone should move Clarity, Motion and Visual to 9. With fixes 6–9, Hook and Audio should also reach 9, for a weighted score of about 9.0–9.1.

KEEP:
- The doubling strips (1:07–1:23): one cut, the kept half stretches, a counter to 3.3 and 10.3. This is the "you could have invented it" moment, and it must survive any re-layout.
- The skyline that pours flat into the entropy (1:45–2:00), reused for the contexts and for Shannon's guess counts (3:12). One picture carries the whole episode.
- The landing: Shannon's real record docks into the cold-open row, with "1 guess" against "5 questions" (3:43–3:54).
