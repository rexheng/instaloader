# Episode 4, round 8: substance review (science and story editor)

**Evidence.** `review/metrics.json` (18:59) is newer than `final.mp4` (18:57), so I used the existing `review/` pack and did not generate a new one. I read:
- `report.md`, all 12 contact sheets, and 12 full-resolution keyframes: kf_04 0:11.1, kf_06 0:24.3, kf_14 0:59.6, kf_17 1:21.6, kf_20 1:32.6, kf_23 1:46.9, kf_25 1:58.2, kf_28 2:05.7, kf_32 2:42.6, kf_34 2:51.8, kf_35 3:09.3, kf_39 3:27.6.
- 12 frames I extracted myself with ffmpeg: 1:06.3, 1:06.9, 1:07.5, 2:15.6, 2:16.4, 2:17.2, 2:39.5, 2:40.5, 2:41.5, 2:42.5, 2:43.5, 2:44.5.
- `transcript.txt`, the word timings at 1:40–1:52, `narration.txt`, `script.md` and `facts.md`.

**Recomputation.** I redid every number myself rather than reading `check_numbers.py`:
- An exact-fraction enumeration of all 16 four-flip sequences.
- An exact dynamic program over 100-shot records at p = .5 for k = 3.

**Citations.** I checked both against the Miller & Sanjurjo text using web search (the Melbourne repository PDF, the Wharton PDF and the JSTOR excerpt).

```
EPISODE: 004 — "The Hidden Bias That Hid the Hot Hand"
IDEA: If you average each short sequence's after-heads share, every sequence gets one vote however many flips it checked; checked heads crowd into a few sequences and get diluted, so a fair coin reads 17/42, not 1/2. The same bias puts a random shooter at −8 on the 1985 after-3-hits minus after-3-misses test, so Cornell's +4 is about 12 points hot.
SCORES: Hook 9 · Clarity 8.5 · Visual 9 · Motion 8.5 · Audio 9 · Concision 8.5 · Originality 9
WEIGHTED: 8.8   AFTER CEILING: 8.8 (lowest 8.5 + 2 = 10.5; does not bind)
CAPS: none
FINAL: 8.8   PASS: no
```

**Working.** 15·9 + 25·8.5 + 15·9 + 15·8.5 + 10·9 + 10·8.5 + 10·9 = 875. That is 8.75, which rounds half-up to 8.8.

**Caps.** I checked each one and none is triggered:
- Runtime is 3:31.0. Pace is 150 wpm over speech time (487 words).
- Loudness is −14.1 LUFS with a −2.1 dBTP true peak.
- The longest internal silence is 2.17 s. It is the planned prediction hold at 0:12.7–0:14.8.
- The longest static stretch is 3.53 s, at 3:06.6–3:10.2.
- There are 0 black frames and 0 banned phrases.
- There is no rhetorical-question chain. The cold open asks exactly one question.
- The layout audit is clean over 227 settled frames.
- No frame I read has a typo, broken LaTeX or clipping.
- Both studies are cited on screen whenever their numbers are on screen.
- Borderline, not capped: at 2:41.5–2:44.0 the after-hits cursor is plotted at about 42% on an axis still labelled 0–100%, while its readout says 46%. I score this under Clarity and Motion rather than cap 6, for three reasons:
  - The readouts state the correct values.
  - The move is a rigid slide of the pair under "puts the gap".
  - A zoom to a gap axis follows 2.5 s later.

  But a viewer who pauses there reads a false chart. It is the single most important thing to fix (fix 1).

## FACTS

Every number below was recomputed by me or checked against the paper's text.

| Claim | Status | Source / my check |
|---|---|---|
| Four flips can land 16 ways, all equally likely | Verified | 2⁴ = 16, my enumeration |
| HHTH: after each heads the checked flips are H and T, so "one of the two is heads" = 1/2 (0:04) | Verified | enumeration |
| "This row checks three flips, and two are heads" (HHHT → 2/3, 0:41) | Verified | enumeration |
| Two rows (TTTH, TTTT) have no heads before the last flip, so no score; 14 are scored | Verified | enumeration |
| Per-row scores on screen at kf_14: 0 ×6, ½ ×4, ⅔ ×1, 1 ×3 | Verified | enumeration. I also checked all 14 table fractions in kf_14 against their rows: every ring and every fraction is right |
| Average = 17/42 = 40.5%; "reads cold by 9.5 points" | Verified | Σ = 17/3 over 14 = 17/42 = 0.40476; 50 − 40.48 = 9.52 |
| 24 checked flips, 12 heads and 12 tails, so pooled = exactly ½ | Verified | Σh = 12, Σn = 24 |
| 12 heads in 8 rows, 12 tails in 11 rows | Verified | my sets: 8 and 11. The boxed rows at 1:35 and 1:37 match them one for one |
| HHHH: three heads share one vote; HTTT: a lone tails gets a whole one | Verified | HHHH checks 3 flips (all H); HTTT checks 1 flip (T) |
| Heads hold 5⅔ of 14 votes, so 5⅔/14 = 17/42; tails hold 8⅓ | Verified | Σhᵢ/nᵢ = 17/3. In kf_23 the packed yellow ends on the 40.5% marker |
| Vote strip slices (kf_20): the 14 boxes hold 3/3, 2/3, ½, ½, ½, 0/2, 0, 0, 2/2, ½, 0, 0, 1/1, 0 | Verified | matches the 14 scores |
| (1/14)Σᵢ hᵢ/nᵢ = 17/42 vs Σhᵢ/Σnᵢ = 12/24 (kf_25) | Verified | arithmetic |
| After a tails the test reads 25/42 (59.5%), and the strip mirrors about ½ | Verified | my enumeration: 25/42. The H↔T swap maps the 16 sequences onto themselves |
| Gap 17/42 − 25/42 = −19 points | Verified | −19.05. It is the difference of the two averages, which is how it is drawn and said. The per-row mean difference is −1/3, but that is not claimed |
| GVT 1985, *Cognitive Psychology*, called the hot hand "a powerful and widely shared cognitive illusion" | Verified | GVT 17(3):295–314, quote at pp. 312–313, as quoted in M&S 2018 §1 and §3 (Melbourne PDF; JSTOR excerpt "(p. 313)") |
| 26 Cornell players, up to 100 shots each, from where they'd hit about half | Verified | M&S §3.1: "26 players … Mens' (14) and Womens' (12) … Each player shot 100 times at a distance from which the experimenters determined he/she would make around 50 percent." "Up to" is safe |
| Random shooter, n = 100, p = .5: after 3 hits 46%, after 3 misses 54% | Verified | my exact DP: 0.46032 / 0.53968 |
| M&S 2018: the gap is about −8 points | Verified | M&S §3.2: "the expected difference (and the strength of the bias) is -8 percentage points." My DP gives −7.935 |
| 1,000 shots: the ghost tick sits at about −0.7 (2:47) | Verified | facts.md says exact DP −0.708. I did not rerun n = 1,000. The value is consistent with the M&S abstract ("decreases as the sequence gets longer") |
| Cornell: 49% after 3 hits, 45% after 3 misses, so +4 | Verified | M&S §3.1: "players on average hit .49 when on a hit streak, versus .45 when on a miss streak" |
| "too close to zero to count"; on screen "vs 0: p = .49" | Verified | M&S §3.1: "GVT's paired t-test finds the difference to be statistically indistinguishable from zero, and we replicate this result (p=.49)" |
| "Measured from minus eight, it's 12 points hot" | Verified | M&S §3.2: "+4 percentage points observed by GVT is actually +12 percentage points higher than the difference that would be expected from a Bernoulli i.i.d. shooter" |
| Evidence in a gym, not proof it survives defenders in a game | Verified | the GVT controlled experiment had no defense; M&S fn. 22 is on in-game defensive adjustment |
| Miller & Sanjurjo, 2018 · *Econometrica* | Verified | 86(6):2019–2047 |
| "Longer records shrink it, but 100 shots isn't long" (2:46) | Verified, but incomplete | True for k = 3. But the one-hit version the viewer just built shrinks from −19 at n = 4 to only −1.0 at n = 100 (my DP). What keeps the 1985 gap at −8 is the 3-hit streak (the M&S abstract: "increases in streak length"), and that is no longer said. See fix 2 |

## MECHANICS
runtime 3:31.0 · wpm 150 (speech time; 138 overall) · max silence 2.17 s (planned prediction hold, 0:12.7) · leading silence 0.00 s, trailing 1.74 s · max static 3.53 s (3:06.6–3:10.2) · −14.1 LUFS / −2.1 dBTP · WER 1.1% (no term misheard; "Sanjurjo" transcribed correctly)

## Transcript and story

**Slop.** I searched for every §4 phrase and found none.
- Signposting: "Now score the flip after each tails" (1:57) is the only "now", and it is a beat turn.
- "It turns out" does not occur.
- No "not just X, it's Y" construction. The line "evidence for a hot hand in a gym, not proof it survives defenders" is a genuine scope limit, not that pattern.
- No triplets of abstract adjectives, and no colon fake-reveals.
- The voice is concrete throughout: nouns, numbers and pointing ("This row", "Here, three heads", "this lone tails").

**Hook (9).**
- The first frame is the puzzle: coins flipping in at 0:01. The arcs and rings explain the rule at 0:03–0:07.
- The 16-run ghost collapses to "?" at 0:09–0:11, and the three answers sit on the axis. The viewer commits by 0:12.8, followed by a 2.2 s hold.
- Stakes arrive at 0:18 (1985, "illusion", with the citation and verbatim quote on screen at 0:25–0:27).
- The ending resolves the opening exactly. At 3:15–3:31 the same HHTH row and the same ghost collapse onto 17/42, with the test's formula beside it. The final arrow runs from 17/42 to ½, labelled "hot".
- Slight sag: the insight beat runs 55 s (1:03–1:58), with the frame mostly at 30% dim (1:19–1:31). The questions inside it are explanatory, not tension-building.

**Clarity (8.5).** The argument is correct, concrete first, and the viewer could re-derive the 4-flip case after one watch. Two deductions:
1. **2:41.5–2:44.0 (kf_32 and my frames at 2:41.5, 2:42.5, 2:43.5): the chart contradicts its labels.**
   - The ticks still read 0–100% with the title "checked shots that are hits".
   - The after-hits cursor stands at x ≈ 673 px, which is (673 − 163)/(1378 − 163) = 42%, while its readout says 46%.
   - The after-misses cursor stands at 50%, labelled 54%.
   - This lasts about 2.5 s, during "puts the gap at about minus eight".
2. **2:46–2:50: the size of −8 is given the wrong cause.**
   - The viewer's whole intuition comes from the one-heads version at n = 4 (−19).
   - The narration then says only that longer records shrink the bias, "but 100 shots isn't long".
   - But for the version the viewer learned, 100 shots is long: the bias is −1.0 point. The −8 survives because GVT conditioned on three hits in a row.
   - Round 7 cut "Longer streaks grow the bias". That left a viewer who re-derives the idea with the wrong model of why the 1985 number is −8. Nothing said is false; the explanation is incomplete exactly where the payoff depends on it.

**Concision (8.5).** At 487 words in 3:31, under 10% is removable, but there is one double explanation:
- "The skew comes from scoring row by row" (1:14) and "So the test takes an average of ratios, one per row, instead of the ratio of totals" (1:50) state the same cause twice. The second carries the formula; the first only announces it.
- The repeated "seventeen out of forty two" (0:55, 1:47, 3:19) works: each time it is a computed result or the landing callback.

**Originality (9).** The vote strip is the one picture, and it is not the textbook framing.
- One vote per row; heads squeezed into thirds of a vote (1:25–1:31); the packed yellow stopping exactly on the 40.5% marker (1:43).
- The two formulas read off two strips (kf_25).
- Flipping the strip about ½ to get 25/42 (2:03–2:05).

Miller & Sanjurjo and Norvig present this as a table of sequences. This version turns it into a memorable weighting picture.

## Visual and motion notes (contact sheets and frames)

- **Palette is consistent.** Yellow = heads/hit, grey = tails/miss, blue = the test and its readings, red = bias, purple = Cornell, white = the assumption. The landing re-uses every one with the same meaning.
- **Fully clean, screenshot-grade frames:** 0:59.6 (kf_14), 1:46.9 (kf_23), 1:58.2 (kf_25) and 3:09.3 (kf_35).
- **1:06.3–1:07.5:** the 24 disc copies fly across other table rows. At 1:06.9, outlines sit over the HTHT, HTTH and HTTT rows. It lasts under 1 s, but it is the only cluttered moment in the insight beat.
- **1:19–1:31:** the vote strip is never named on screen. "One vote per row" exists only in the narration, and the 14 outlines have no label. With everything else dimmed to 30%, the unlabeled strip is the focal object.
- **2:15.6–2:18:** the header "1985 design" and the GVT citation arrive while the lanes still read "after heads / after tails" with "checked flips that are heads". Header and lanes disagree for about 2.5 s.
- **2:44.5 (my frame):** mid-zoom, the new −10…+10 labels are compressed and dim, and the axis title is absent. This is a nitpick.
- The slide at 2:41.5 also removes the lane lines and the ●●● / ○○○ glyphs, so the condition legend disappears just as the gap is named.

**FIXES (highest impact first):**

1. **[2:41.3–2:44.0][Clarity/Motion]** The cursor pair slides to 42% / 50% on an axis still labelled 0–100% while the readouts say 46% / 54% (kf_32). Remove the slide.
   - On "puts the gap", draw a thin red bracket between the 46% and 54% cursors and write "−8" above it (0.6 s).
   - On "at about minus eight points", run the ×5 zoom about the **after-misses cursor at 54%**, not the dashed 50% line. During the zoom the 0/25/75/100% tick labels fade out and −10…+10 grow in on the same tick marks, centred on the after-misses cursor. Then translate the whole axis 4 points left (0.6 s) so the after-misses cursor lands on the dashed line, which becomes 0.
   - Simpler alternative: fade the % tick labels and the axis title to 0 **before** the pair slides (0.4 s), then slide, then grow the new labels.

   Either way, no frame may show a % label next to a shifted cursor. Gains: Clarity +0.5, Motion +0.5.
2. **[2:46.0–2:50.4][Clarity]** Replace "Longer records shrink it, but a hundred shots isn't long" with "Longer records shrink it; longer streaks grow it."
   - That is 7 words replacing 9, and it matches the M&S abstract.
   - Visual: on "Longer records shrink it", keep the existing ghost slide to −0.7, "1,000 shots".
   - On "longer streaks grow it", show one ghost of the −8 marker at −1.0 tagged with a single yellow dot "●" (one hit, 100 shots). It then slides to −8 as its tag grows to "●●●" (1.2 s, smooth).

   This tells the viewer why their −19 (one heads, 4 flips) became −8 (three hits, 100 shots) rather than about −1.
3. **[1:14.3–1:16.6 and 1:50.5–1:57.5][Concision]** Cut the clause "The skew comes from scoring row by row:" at 1:14 and start the beat with "Each row gets one vote, however many flips it checked." The 1:50 line then names the cause once, with its formula.
   - This saves about 2.3 s and removes the double explanation.
   - Re-time the "however many flips it checked" denominator flash to the new start.
4. **[1:17–1:43][Visual/Clarity]** Name the vote strip.
   - On "Each row gets one vote", write a grey "1 vote per row" (Text ≥ 26) above the left end of the vote strip, 0.2 clear of the 40.5% label.
   - Fade it at "Line them up", when "5⅔ votes" takes that space.
5. **[2:50.4–3:04.5][Audio/Clarity]** Six numbers (49, 3, 45, 3, +4, 0) arrive in 14 s with only 0.4–0.5 s stops.
   - Add [pause 0.6] after "forty five after three misses", so "49 − 45" finishes writing before "The study found".
   - Add [pause 0.4] after "plus four", so "= +4" lands with the purple marker before "too close to zero".
6. **[1:06.3–1:07.5][Motion]** The 24 disc copies cross other rows of the table on their way to the strip. Each copy should fade in just below its own table row, then travel down the column gap between table columns to its tile, as the cold-open copies already do (0:05). No copy should pass over another coin.
7. **[2:15.6–2:18.5][Visual]** For about 2.5 s the header "1985 design" disagrees with the lanes "after heads / after tails" and the axis title "checked flips that are heads". On "The nineteen eighty five study", relabel the lanes to "after 3 hits / after 3 misses" and the title to "checked shots that are hits" together with the header, not after it.
8. **[2:44.0–2:44.6][Motion]** Mid-zoom the axis briefly has no title and its new labels are compressed and dim (my frame at 2:44.5). Cross-fade the title "after-hits − after-misses (points)" in during the zoom, overlapping the outgoing title. This is a nitpick.

**REACHES 9 IF ALL FIXED: yes.**
- Fixes 1 and 2 raise Clarity to 9, and fix 1 raises Motion to 9. Fix 3 raises Concision to 9.
- That gives 15·9 + 25·9 + 15·9 + 15·9 + 10·9 + 10·9 + 10·9 = 900, which is 9.0.
- It is a narrow pass, so fixes 4–8 are the margin. No structural change is needed: the hook, fail, one picture, payoff and landing are all in place.

**KEEP:**
- The vote-strip insight (1:17–1:58): squeezed thirds of a vote, the yellow packing onto the 40.5% marker, and the two formulas read off two strips.
- The landing (3:15–3:31): it answers the cold-open question on the cold-open image, with the test's formula, and the "hot" arrow runs from 17/42 to ½.
- The payoff chain −8 → 49 − 45 = +4 → +12 brace, with "vs 0: p = .49", "no defenders", and both citations at full strength.
