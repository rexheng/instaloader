# Episode 4, round 6: substance review (science and story editor)

Evidence used: `review/` pack (metrics.json 09:04 is newer than final.mp4 09:02, so it was used as is). I read report.md, all 12 contact sheets, 12 full-resolution keyframes (0:13.7, 0:21.0, 0:45.7, 1:14.7, 1:37.8, 1:52.3, 2:16.1, 2:33.9, 2:41.9, 2:50.6, 3:05.0, 3:24.0) and 9 extra frames I extracted myself (0:05.0, 0:37.0, 1:21.0, 1:45.5, 2:17.0, 2:24.5, 2:57.3, 3:15.0, 3:23.5), plus the transcript, word timings, narration.txt, script.md and facts.md. I recomputed every number independently (exhaustive enumeration over the 16 sequences, plus my own exact dynamic program for n = 100) and checked every citation by web search against the Miller & Sanjurjo text (Wharton and Melbourne PDF copies, JSTOR excerpt).

```
EPISODE: 004 — "The Hidden Bias That Hid the Hot Hand"
IDEA: If you average the after-heads share row by row, each sequence gets one vote however many flips it checked, and because heads crowd into the rows that check many flips, a fair coin reads 17/42 instead of 1/2. The same bias puts a random shooter at −8 points on the 1985 hot-hand test, so Cornell's +4 is really 12 points hot.
SCORES: Hook 9 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 8.5
WEIGHTED: 8.6   AFTER CEILING: 8.6 (lowest 8.5 + 2 = 10.5, so the ceiling does not bind)
CAPS: none. Every cap checked: runtime 3:24, 152 wpm, −14.0 LUFS, −2.1 dBTP, max silence 2.06 s (the planned prediction hold), max static 2.73 s, 0 black frames, 0 layout issues, 0 banned phrases, no typos or broken LaTeX in any frame I read, and every empirical claim has an on-screen citation. No number is wrong (see FACTS).
FINAL: 8.6   PASS: no
```

Final working: 15·9 + 25·8.5 + 15·8.5 + 15·8.5 + 10·8.5 + 10·8.5 + 10·8.5 = 857.5, so weighted is 8.6. Ceiling 10.5, no caps, final 8.6.

## FACTS

All values recomputed by me, not copied from facts.md.

| Claim | Status | Source / my check |
|---|---|---|
| HHTH: the flips after a heads are flip 2 (H) and flip 3 (T), "one of the two is heads", 1/2 (0:04) | Verified | enumeration |
| 4 flips land 16 equally likely ways (0:38) | Verified | 2⁴ |
| HHHT checks 3 flips, 2 are heads, 2/3 (0:42) | Verified | enumeration |
| Two rows (TTTH, TTTT) get no score; 14 are scored (0:48) | Verified | enumeration |
| Row scores 0×6, ½×4, ⅔×1, 1×3; all 16 table fractions on screen at 0:53 match | Verified | enumeration, checked cell by cell |
| Average = 17/42 ≈ 40.5%; "cold by nine and a half points" (0:56–1:08) | Verified | (3 + ⅔ + 2)/14 = 17/42 = 0.4048; 50 − 40.48 = 9.52 |
| Pooled: 24 checked flips, 12 H, 12 T, exactly half (1:10–1:18) | Verified | ΣH = 12, Σn = 24 |
| "Twelve heads crowd into eight rows, twelve tails across eleven" (1:36) | Verified | rows with a checked H = 8, with a checked T = 11; the 8 yellow boxes at 1:37.8 are the right rows |
| HHHH's three heads share one vote; HTTT's lone tails gets one (1:31) | Verified | enumeration |
| (1/14) Σ hᵢ/nᵢ = 17/42 vs Σhᵢ/Σnᵢ = 12/24 (1:48–1:55) | Verified | algebra |
| After tails, the average heads share = 25/42 ≈ 59.5% (2:03) | Verified | the 14 rows with a flip after a tails, exact; also follows from H↔T symmetry |
| Gap = 17/42 − 25/42 = −19 points (2:08) | Verified | −8/42 = −19.05 pts; correctly worded as "subtract the two averages" (the per-row mean difference, −1/3, is not claimed) |
| GVT 1985: 26 Cornell players (14 men, 12 women), 100 shots from a distance where they'd hit ≈50% | Verified | M&S 2018 §3.1, verbatim: "26 players from the Cornell University Mens' (14) and Womens' (12) basketball teams … Each player shot 100 times at a distance from which … he/she would make around 50 percent". "Up to 100" is fair because a few players took fewer shots (M&S Table 2) |
| GVT called it "a powerful and widely shared cognitive illusion" (0:27 on screen) | Verified | GVT pp. 312–313, quoted in M&S fn.; JSTOR excerpt |
| Random shooter, n = 100, p = .5: 46% after 3 hits, 54% after 3 misses (2:28) | Verified | my exact DP: 0.46032 / 0.53968 |
| M&S 2018 put the gap at about −8 points (2:36) | Verified | M&S §3.2: "the expected difference (and the strength of the bias) is −8 percentage points"; my DP gives −7.94 |
| Longer streaks grow the bias, longer records shrink it; ghost ticks at −1.0, −3.1, −8 (2:42) | Verified | M&S abstract; my DP at n = 100: −1.01 (k=1), −3.14 (k=2), −7.94 (k=3) |
| Cornell: 49% after 3 hits, 45% after 3 misses, +4 read as no hot hand (2:49–3:00) | Verified | M&S §3.1: "players on average hit .49 when on a hit streak, versus .45 when on a miss streak", and the paired t-test found no significant difference |
| +4 measured from −8 = +12 points hot (3:00) | Verified | M&S: "+4 percentage points observed by GVT is actually +12 percentage points higher than … expected from a Bernoulli i.i.d. shooter" |
| Gym, not game: GVT's controlled task had no defenders (3:03) | Verified | M&S §3.1 (the design eliminated "shot selection and defensive pressure") and fn. 22 |
| Citations: Gilovich et al., 1985 · Cognitive Psychology 17(3):295–314; Miller & Sanjurjo, 2018 · Econometrica 86(6):2019–2047 | Verified | search results and the arXiv/Wharton copy |
| Landing: "A 50% shooter who averages one half on this test is already running hot" (3:17) | Verified (as worded) | 1/2 > 17/42, the i.i.d. p = .5 baseline. The picture is ambiguous, though (fix 3) |

No fabricated, misattributed or wrong claim. This is the cleanest fact sheet I have seen in this series.

## MECHANICS

runtime 3:24.0 · 152 wpm (speech time; 147 overall) · max internal silence 2.06 s (0:12.3–0:14.3, the planned prediction hold) · leading 0.00 s / trailing 1.32 s · max static 2.73 s · −14.0 LUFS / −2.1 dBTP · WER 0.4%. The only mismatches are "a hundred" heard as "one hundred" twice. The doubled "and and" at 2:00.9 is a whisper artifact: the second "and" is 0.02 s long (120.90–120.92 in transcript_words.tsv).

## Transcript audit (§4)

- Banned phrases: 0. Banned patterns: none. There is one question ("Below, at, or above one half?"), no "it turns out", no fake reveal, and no recap ending. "Now score the flip after each tails" is an instruction, not signposting.
- Hook: the first frame (0:00) is the coin row. The puzzle is fully posed and the three answers are on the line by 0:12.3, followed by a 2 s hold. That meets the 9 anchor.
- Beat map against §6: cold open 0:00–0:14, stakes 0:14–0:27, naive build (the test, then calibrating it on a coin) 0:27–0:56, fail (40.5%, cold by 9.5) 0:56–1:08, insight 1:08–1:56, mirror 1:56–2:14, payoff 2:14–3:10, landing 3:10–3:24. The structure is right and proportional to the length.
- Deictics land: "This row checks three flips" (0:42), HHHT box at 0:43. "This row's three heads" (1:31), HHHH box at 1:31–1:33. "this lone tails" (1:34), HTTT box at 1:35. "the strip flips over one half" (2:01), the half-turn at 2:01–2:03. "46 and 54" values appear on the spoken numbers (2:33, 2:35).

## What holds it below 9 (evidence)

1. **2:14–3:03, payoff density (Clarity).** In 49 s the viewer gets nine new numbers (26, 100, 46, 54, −8, 49, 45, +4, +12) and three axis states: 0–100% share at 2:19, the 40–60% zoom at 2:25, and the −10…+10 difference axis at 2:41. The one-picture discipline of the first two minutes gives way to a run of readouts. The simulated 100-shot record (2:21–2:31, sheet 9) doesn't carry its weight. Its rings on 100 tiny tiles can't be read in the ~6 s it is up, no count from it is used, and it fades as the cursors move.
2. **1:36.7–1:47.8, "Fewer rows, fewer votes" (Clarity).** This is the line meant to close the argument, and it is the loosest one. Being in 8 rows instead of 11 doesn't by itself mean fewer votes. The mechanism, which the narration already gave at 1:25, is dilution: a heads drags the next flip into its row's denominator, so each checked heads gets about 0.47 of a vote and each checked tails about 0.69. The thin heads slices on the vote strip (1:37.8) show the right thing, but the sentence names a row count, not the dilution.
3. **3:17–3:24, landing picture (Clarity/Motion).** The blue "shooter's average" dot appears on the 50% line directly beneath the single hit/hit/miss/hit row and its own "1/2" (frame 3:24.0). That invites the reading "this one 4-shot row is hot", which facts.md explicitly says the episode does not claim. The "hot" arrow is about 65 px long, and the finished frame holds about 1.2 s (the arrow completes about 3:22.8; the file ends at 3:24.0), below the 1.5 s reading floor for the last image of the video.
4. **2:14–2:49, header semantics (Visual).** "Cornell, 1985" appears in white over the coin after-heads/after-tails strips (2:15–2:17, sheet 8) and stays over content that is not Cornell data: the simulated record and the random-shooter −8 (kf 2:41.9). Purple, the Cornell hue, arrives only at 2:50. For 35 s the title names data that isn't on screen.
5. **2:49–3:10, citation dimmed while its data is shown (Visual).** The GVT citation sits at about 30% opacity (kf 2:50.6, 3:05.0) exactly while GVT's own 49%, 45% and +4 are on screen, and the M&S line stays bright. At that opacity the citation is below the 4.5:1 contrast floor.

## FIXES (highest impact first)

1. [2:21–2:31 and 2:36–3:01][Clarity/Concision] Too many readouts in the payoff → cut the simulated 100-shot record entirely, and with it the "simulated / random shooter" label. Keep "up to a hundred shots" on the header only. Spend the freed ~2 s on two silent holds: 0.8 s after "minus eight points." (2:42.1) with the −8 marker and red "bias" arrow alone on screen, and 0.8 s after "no hot hand." (3:00.1) with the +4 marker landed and the dashed 0 pulsing. Also say which cursor moves which way: "the same crowding pulls after-hits down to forty six, and after-misses up to fifty four percent."
2. [1:36.7–1:47.8][Clarity] Loose causal line → replace "Twelve heads crowd into eight rows. Twelve tails spread across eleven. Fewer rows, fewer votes: line them up, and heads hold seventeen out of forty two." with "Twelve heads crowd into eight rows; twelve tails spread across eleven. Crowded heads split their votes: line them up, and heads hold seventeen out of forty two." On "split their votes", pulse the three thin HHHH slices and HHHT's two (the existing pulse, retimed). The word count stays almost the same.
3. [3:17–3:24][Clarity/Motion] Ambiguous landing → on "A fifty percent shooter", dim the hit/hit/miss/hit row and its 1/2 to 30%, and grow the blue dot with a 26-px grey tag "average over rows" left of it. Lengthen the "hot" arrow to start at the 17/42 marker's top (it is about 65 px now). Hold the finished frame at least 2.0 s after the arrow completes; the trailing silence is only 1.32 s now, so there is room.
4. [2:14.4–2:49.4][Visual] Header names data that isn't on screen → do not draw "Cornell, 1985" until the coin strips have faded (after 2:17.5). Write it in grey as "1985 design · 26 players · up to 100 shots". Morph it to purple "Cornell, 1985" only at 2:49.5, when 49%/45% arrive (that morph already exists; it would now carry meaning).
5. [2:49.5–3:10][Visual] Citation dimmed during its own data → on "Cornell's players hit" restore "Gilovich et al., 1985 · Cognitive Psychology" to full opacity. Dim M&S instead, and keep both at full from "Measured from minus eight" (3:00) until "evidence" (3:03).
6. [2:25–2:41][Motion/Clarity] Three axis states in 16 s → skip the 40–60% zoom. Run the 46/54 cursors on the 0–100% axis (4 points = 0.4 units at the current scale is still visible), and relabel straight to the difference axis at 2:41. That removes one transform the viewer must track.
7. [0:05.0][Motion, nitpick] As the ringed H lifts into the yellow "1", for about 0.3 s the copy and the coin's H overlap into a doubled glyph (extracted frame 0:05.0). Fade the coin's own letter to 50% during the lift, or start the copy 0.1 units above the coin.

REACHES 9 IF ALL FIXED: yes, but narrowly. Fixes 1, 2, 3 and 6 lift Clarity to 9. Fixes 3, 4 and 5 lift Visual and Motion to 9, and fix 1 lifts Concision to 9. With Audio and Originality at 8.5, that is (135 + 225 + 135 + 135 + 85 + 90 + 85)/100 = 8.9. It reaches 9.0 only if the payoff also reads as calm as the first two minutes, which is what fix 1 is for. No structural change is needed: the hook, the fail-by-a-measured-amount beat, the one-vote-per-row picture and the landing are all in place.

KEEP:
- The one-vote-per-row strip (1:20–1:47): 24 equal tiles regrouped into 14 equal row-votes, so HHHH's three heads visibly squeeze into one vote and the yellow lands exactly on 40.5%. This is the insight as a picture.
- The mirror (1:56–2:14): the after-heads strip copied, recoloured and turned a half-turn about the dashed 50% line to land at 25/42, then the −19 arrow. It derives the two-sided gap with no new formula.
- "Test the test on a shooter we know is random" (0:33), and the landing's return to the HHTH row with 17/42 drawn on the cold-open axis.
