# Episode 4, round 10: substance review (science and story editor)

**Evidence.** `review/metrics.json` (21:52) is newer than `final.mp4` (21:50), so I used the existing `review/` pack. I read:
- `report.md`, all 12 contact sheets, `transcript.txt`, `narration.txt`, `script.md`, `facts.md` and the end of `CHANGELOG.md`.
- 12 full-resolution keyframes: kf_04 0:11.1, kf_07 0:24.3, kf_09 0:32.5, kf_15 0:59.6, kf_20 1:27.1, kf_24 1:37.2, kf_26 1:48.6, kf_29 2:09.5, kf_32 2:38.1, kf_34 3:01.4, kf_40 3:23.1.
- 11 frames I extracted myself with ffmpeg into the scratchpad `r10s/` folder: 0:45.0, 1:05.8, 1:09.0, 1:10.6, 1:11.0, 2:07.8, 2:08.5, 2:53.0, 2:54.0, 3:09.5, 3:12.6.

**Recomputation.** I did not use `check_numbers.py`. I wrote my own script:
- An exact-fraction enumeration of all 16 four-flip sequences, scoring after heads and after tails.
- A 200,000-sequence Monte Carlo of 100-shot records at p = .5, k = 3.

**Citations.** I verified both by web search and by reading the Miller & Sanjurjo PDF (Wharton copy, 49 pp.). I quoted §3.1 and §3.2, and pulled Table 2 (the per-player reproduction of GVT's Table 4).

```
EPISODE: 004 — "The Hidden Bias That Hid the Hot Hand"
IDEA: Averaging each short run's after-heads share gives every run one vote however many flips it checked, so heads (which crowd into few runs) are diluted and a fair coin reads 17/42, not 1/2; the same bias puts a random shooter at −8 on the 1985 after-3-hits minus after-3-misses test, so Cornell's +4 is really +12.
SCORES: Hook 9 · Clarity 9 · Visual 8.5 · Motion 9 · Audio 9 · Concision 9 · Originality 9
WEIGHTED: 8.9 (15·9 + 25·9 + 15·8.5 + 15·9 + 10·9 + 10·9 + 10·9 = 892.5 → 8.925 → 8.9)   AFTER CEILING: 8.9 (lowest 8.5 + 2 = 10.5, does not bind)
CAPS: none
FINAL: 8.9   PASS: no
```

The miss is narrow and it has one cause. The payoff frame at 2:51–2:56 carries about 16 words of full-strength prose and three competing focal points (fix 1). That is a §5 word-load miss. Fixing it alone takes Visual to 9 and the episode to 9.0.

## Caps checked (none triggered)
- **Runtime and pace.** 3:23.1. 151 wpm over speech time (463 words), median sentence 168 wpm, 0 sentences above 200 wpm.
- **Loudness.** −14.1 LUFS / −2.1 dBTP.
- **Silence.** Leading 0.00 s, trailing 1.74 s. The longest internal silence is 2.17 s, the planned prediction hold at 0:12.7–0:14.8.
- **Static frames.** The longest static stretch is 3.53 s (the +12 frame, 2:58.7–3:02.3). 0 black frames.
- **Banned phrases and patterns.** 0 banned phrases. The episode asks one question (0:12.8), so there is no question chain. Two lines look like banned patterns but are not:
  - "Evidence for a hot hand in a gym, not proof it survives defenders" is a scope limit, not the "not just X, it's Y" construction.
  - "Below, at, or above" is three answer options, not an adjective triplet.
- **Hook and ending.** The hook lands by 0:12.8: the coin row is on screen from 0:00, and the viewer commits with "< 1/2 / = 1/2 / > 1/2". The ending is a reframing of the cold-open row, not a recap list.
- **Layout and text.** The layout audit is clean (0 issues in 218 frames). I found no settled typo, broken LaTeX, clipping or overlap in any frame I read. The 1:11.0 glyph crossing (fix 4) lasts a fraction of a second, mid-transform.
- **Citations.** Every empirical number has an on-screen citation:
  - GVT at 0:19–0:33 and 2:09–3:06.
  - M&S from 2:25 to 3:06.

## FACTS
Recomputed by me or checked against the source text.

| Claim | Status | Source / my check |
|---|---|---|
| 4 flips give 16 equally likely runs | Verified | 2⁴ |
| HHTH: the flips after a heads are H and T, so 1/2 | Verified | enumeration |
| HHHT checks 3 flips and 2 are heads (0:41.7) | Verified | enumeration |
| Two runs (TTTH, TTTT) get no score; 14 are scored | Verified | enumeration |
| Score dots: 0 ×6, ½ ×4, ⅔ ×1, 1 ×3 (0:53–0:59) | Verified | enumeration (Counter output) |
| Average of the 14 scores = 17/42 = 40.5% | Verified | exact: (17/3)/14 |
| "Reads cold by 9.5 points" | Verified | 50 − 40.48 = 9.52 |
| Pooled: 24 checked flips, 12 H / 12 T, so exactly ½ | Verified | Σh = 12, Σn = 24 |
| Checked heads in 8 runs, checked tails in 11 (on screen, 1:31–1:35) | Verified | enumeration |
| HHHH: three heads share one vote; HTTT: one tails holds a whole vote | Verified | definition, enumeration |
| Heads hold 5⅔ of 14 votes, so 17/42; tails 8⅓ | Verified | Σ hᵢ/nᵢ = 17/3; 14 − 17/3 = 25/3 |
| (1/14) Σᵢ hᵢ/nᵢ = 17/42 vs Σᵢhᵢ/Σᵢnᵢ = 12/24 | Verified | re-derived; correct notation, the "=" joins only after both sides exist |
| After tails: 25/42 (59.5%); mirror by H↔T symmetry | Verified | enumeration: 25/42 over 14 runs; the symmetry argument holds at p = ½ |
| Gap 17/42 − 25/42 = −19 points | Verified | −8/42 = −19.05 |
| GVT 1985 called the hot hand "a powerful and widely shared cognitive illusion" | Verified | GVT p. 313 as quoted in M&S fn. 8; the quote is widely reproduced |
| Gilovich, Vallone & Tversky, 1985, *Cognitive Psychology* 17(3):295–314 | Verified | bibliographic listings, M&S reference list |
| 26 Cornell players; "up to 100 shots"; distance set so each player would hit about half | Verified | M&S §3.1: "26 players from the Cornell University Mens' (14) and Womens' (12) basketball teams… Each player shot 100 times at a distance from which the experimenters determined he/she would make around 50 percent". Table 2 lists 90, 75 and 50 shots for three men, so "up to" is the accurate wording |
| Random shooter, n = 100, p = .5: after 3 hits ≈ 46%, after 3 misses ≈ 54% | Verified | my Monte Carlo: 46.07% / 53.98% (200k sequences) |
| M&S put the expected gap at about −8 points | Verified | M&S §3.2: "the expected difference (and the strength of the bias) is -8 percentage points"; my MC −7.91 |
| "Longer records shrink it; longer streaks grow it" | Verified | M&S abstract: "generally decreases as the sequence gets longer, but increases in streak length" |
| Cornell: 49% after 3 hits, 45% after 3 misses; +4 | Verified | M&S §3.1: "players on average hit .49 when on a hit streak, versus .45 when on a miss streak"; §3.2 calls it "+4 percentage points observed by GVT" |
| "Too close to zero to count" / on screen "vs 0: p = .49" | Verified, with a nuance (fix 3) | M&S §3.1: "GVT's paired t-test finds the difference to be statistically indistinguishable from zero, and we replicate this result (p=.49)". That test is on per-player differences, whose mean in Table 2 is +.03 over 25 players (player F12 has no 3-hit streak). The difference of the averages is +.04. The p = .49 belongs to the paired +3, not literally to "49 − 45" |
| "Measured from minus eight, it's 12 points hot" | Verified | M&S §3.2: "+4 … is actually +12 percentage points higher than the difference that would be expected from a Bernoulli i.i.d. shooter" (their per-player correction gives +13, p < .01; the simpler +12 matches the picture) |
| Gym vs game: no defenders in the experiment | Verified | M&S §3.1: the controlled design was meant to eliminate "shot selection and defensive pressure" |
| Miller & Sanjurjo, 2018, *Econometrica* 86(6):2019–2047 | Verified | title page of the published-version PDF; JSTOR listing |
| Landing: a 50% shooter whose 4-shot rows average ½ reads hot against the 17/42 baseline | Verified | follows from the 17/42 baseline; the tag "its 4-shot rows average 1/2" scopes it correctly |

No claim is wrong, fabricated or unverifiable. This is a clean fact base. The p = .49 placement is a precision nit, not an error.

## MECHANICS
runtime 3:23.1 · wpm 151 (speech time) · max silence 2.17 s (planned) · max static 3.53 s · −14.1 LUFS / −2.1 dBTP · leading 0.00 s · trailing 1.74 s · WER 0.7% (both diffs are number normalisation: "a half" heard as "point five", "a hundred" as "one hundred") · 7/7 deictics land

## Dimension notes

**Hook 9.**
- The concrete object is on screen at 0:00 (HHTH with blue arcs). A precise procedure is shown on that one row (0:04–0:07). The 16-run ghost collapses into one "?" (0:09). Three answers then sit on the line at 0:11–0:13 and the voice holds for 2 s. That is a real commitment to a likely-wrong answer.
- Stakes arrive by 0:26: "In 1985 a study… called the hot hand an illusion", with the verbatim quote at 0:27.
- The ending re-sees the first frame exactly (3:07–3:23): same row, same axis, now carrying 17/42 and a "hot" arrow to ½.
- Tension sags slightly in the 2:09–2:21 design recital (see Visual).

**Clarity 9.**
- Concrete first throughout. Every number has a picture:
  - dots for the 14 scores
  - a live readout for 17/42
  - 24 tiles for 12/24
  - equal vote boxes for "one vote per row"
  - the yellow slices packing exactly onto the 40.5% marker for 5⅔/14
- The formula is read off the two strips: Σh/Σn above, (1/14)Σh/n below (kf_26, 1:48.6). A viewer could re-derive it.
- Honest limits are stated: longer records shrink the bias, and the result comes from a gym with no defenders.
- Two nits keep it from 9.5:
  - The p = .49 nuance (fix 3).
  - "Cornell" is spoken at 2:11 but not printed until 2:43. For 30 s the viewer reads "1985 design" and must remember whose data is coming.

**Visual 8.5.**
- The palette holds its meanings all the way through: yellow heads/hits, grey tails/misses, blue test readings, red bias, purple Cornell.
- Contrast is good and citations sit in the BAR position.
- Deductions:
  1. **2:51–2:56 (my frame 2:54.0).** I counted the full-strength prose:
     - "1985 design"
     - "the obvious guess"
     - "random shooter"
     - "bias"
     - the "Cornell / after 3 hits / after 3 misses" column
     - "vs 0:"

     That is about 16 words, plus 8 more dimmed words in the header. The frame also has three labelled markers, the 49 − 45 = +4 working, the right-hand table and two citations. That is over the §5 limit of 12 words, and the frame has three focal points (the −8 marker, the +4 working, the right column).
  2. **2:09–2:21 (kf_29, my frame 2:08.5).** For about 12 s the picture is two empty grey lanes with blue "?". The only thing that changes is a header sentence growing word by word ("· 26 players · up to 100 shots"). That is a text line doing the picture's job while 14 s of design facts are narrated.
  3. **1:11.0.** As the inline "12/24" restacks into a display fraction, the slash crosses both numbers for a few frames. It is transient and minor.

**Motion 9.**
- Strong transforms that carry relations:
  - the score dots fall into place
  - the pour into tiles
  - the regroup and resize into equal votes
  - the pack onto the marker
  - the half-turn mirror about the dashed line (1:53–1:57)
  - the ×5 zoom into the gap axis (2:33–2:35)
  - the Cornell marker growing beside its working
  - the brace for +12
- One soft spot is 2:07.0 → 2:08.5. The two coin strips and their 17/42 / 25/42 cursors disappear in about 1.5 s and are replaced by empty lanes. The line says "the same comparison", but the picture does not show that the lanes *are* the strips (fix 2). It is a near-cut at a beat boundary, allowed, but it misses a correspondence the narration names.

**Audio 9.**
- 151 wpm. Shaped pauses after the key results, measured in the silence list:
  - 1.6 s after "5⅔ of the 14 votes"
  - 1.9 s after "minus eight points"
  - 1.7 s after "it's 12 points hot"
- All 7 deictics land. Loudness is on target. "Sanjurjo" is transcribed correctly, so it is pronounced recognisably.
- No evidence of a defect.

**Concision 9.**
- 463 words with no preamble and no recap. "17 out of 42" is spoken three times, and each repeat does work:
  - the measurement (0:55)
  - the vote derivation (1:38)
  - the landing callback (3:11)
- The report's fourth "out of forty two" (2:00) is "25 out of 42", a different number.
- The design recital at 2:07–2:21 is load-bearing: n = 100 and "about half" are the inputs to −8.

**Originality 9.**
- "Each row gets one vote", with the heads' third-of-a-vote slices squeezing up against a 40.5% marker, is the memorable, shareable image here. It is a non-obvious way to teach the Miller–Sanjurjo bias: an average of ratios versus a ratio of totals, which is Simpson-style weighting made visible.
- It is not the standard Monte Carlo histogram.

## FIXES (highest impact first)
1. **[2:42–2:58][Visual] Payoff frame over word load, with three focal points (frame 2:54.0).**
   - **Header.** Fade the "1985 design · 26 players · up to 100 shots" header to 0 on "The Cornell players" (2:42.3). The GVT citation already carries the year and the column head says "Cornell".
   - **Right column.** On "plus four" (2:50.8), as "= +4" lands, dim the whole right column ("Cornell / after 3 hits 49% / after 3 misses 45%") to 30%. Its two numbers now live in "49 − 45", so the purple marker plus its working is the one subject.
   - **Result.** Full-strength prose drops from about 16 words to about 9. Visual goes to 9 and Final to 9.0.
2. **[2:07–2:10][Motion/Clarity] "The same comparison" is said but not shown (frames 2:07.8, 2:08.5).**
   - Do not clear the after-heads and after-tails strips. On "The 1985 study" (2:07.2), shrink each strip vertically into its thin lane (1.2 s, smooth), so the after-heads strip becomes the "after 3 hits" lane and the after-tails strip the "after 3 misses" lane.
   - Let the 17/42 and 25/42 labels hand over to the "?" in place, and slide the lane labels "after heads" → "after 3 hits" and "after tails" → "after 3 misses" by TransformMatchingTex. "After" stays; "3" and "hits/misses" swap in.
   - This makes the beat's key word visible and removes the near-cut.
3. **[2:53–2:56][Clarity] The p = .49 tag sits directly under "49 − 45 = +4", but it is GVT's paired t-test on per-player differences (mean +.03 over 25 players, M&S Table 2), not a test of the 4-point difference of averages.**
   - Change the tag from "vs 0: p = .49" to "GVT's test: p = .49" and place it under the purple marker's foot rather than under the "= +4" equation.
   - Alternatively, cut it: "too close to zero to count" already carries the claim, and fix 1 wants fewer words.
4. **[1:10.6–1:11.4][Visual] The inline "12/24" restacks into a display fraction through frames where the slash crosses "12" and "24" (frame 1:11.0).**
   - Fade the slash out over 0.3 s while "12" rises and "24" drops, then grow the fraction bar from its centre. Use TransformMatchingTex with key_map on the numerals only.
5. **[2:09–2:21][Visual] About 12 s of empty lanes plus a growing header sentence (kf_29).**
   - After fix 2 the lanes inherit the strips, so keep the old vote strips inside them at 20% until "For a random shooter" (2:21.7). The lanes then read as "same machine, new data", not blank.
   - Replace the growing header text with tags placed on their referents:
     - "100 shots" tagged at the right end of the top lane, on "up to a hundred shots"
     - "26 players" tagged under the lane labels, on "twenty six Cornell players"
   - Print "Cornell" in that tag ("26 Cornell players"), so the name is on screen from 2:11 rather than 2:43.

REACHES 9 IF ALL FIXED: yes. Fix 1 alone moves Visual to 9 (weighted 900/100 = 9.0). Fixes 2–5 would give margin: Motion and Clarity could reach 9.5. Nothing structural is missing. The hook, the failure measured on a known-random coin, the one-picture insight, the cited payoff with honest limits, and a landing that re-sees the cold open are all present and correct.

KEEP:
- The vote strip: "1 vote per row", HHHH's three heads squeezed into one vote and HTTT's lone tails stretched to a whole one, then the yellow slices packing exactly onto the 40.5% marker into 5⅔/14 = 17/42, with (1/14)Σᵢhᵢ/nᵢ read against Σᵢhᵢ/Σᵢnᵢ = 12/24.
- The half-turn mirror of the strip about the dashed ½ line into 25/42 and −19, then the ×5 zoom into the gap axis where 46/54 become the red −8 "bias".
- The payoff chain −8 → 49 − 45 = +4 → +12 brace, with "no defenders" and both citations, and the landing that answers the cold-open question on the cold-open row with the test's own formula.
