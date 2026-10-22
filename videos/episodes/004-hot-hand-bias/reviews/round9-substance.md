# Episode 4, round 9: substance review (science and story editor)

**Evidence.** `review/metrics.json` (20:22) is newer than `final.mp4` (20:21), so I used the existing `review/` pack and did not generate a new one. I read:
- `report.md` and all 12 contact sheets.
- 14 full-resolution keyframes: 0:11.1, 0:24.3, 0:50.9, 0:59.6, 1:22.2, 1:41.4, 1:49.2, 2:00.2, 2:12.1, 2:42.5, 2:47.2, 3:05.1, 3:26.6 and the sheet frames around them.
- 18 frames I extracted myself with ffmpeg:
  - 0:25.8, 1:07.6, 1:16.0, 2:38.0, 2:38.7, 3:09.8, 3:10.3, 3:10.8, 3:15.8.
  - 2:40.6–2:45.4, every 0.6 s (the "shrink / grow" ghosts).
- `transcript.txt`, `narration.txt`, `script.md` and `facts.md`.

**Recomputation.** I redid every number myself rather than reading `check_numbers.py`:
- An exact-fraction enumeration of all 16 four-flip sequences, after heads and after tails.
- An exact dynamic program over 100-shot records at p = .5 for k = 1, 2, 3.
- A 200,000-sequence simulation of 1,000-shot records for k = 3.

**Citations.** I verified both by web search: the Wharton copy of the Miller & Sanjurjo PDF (direct quotes below) and several independent bibliographic listings for GVT 1985.

```
EPISODE: 004 — "The Hidden Bias That Hid the Hot Hand"
IDEA: Averaging each short sequence's after-heads share gives every sequence one vote however many flips it checked, so heads (which crowd into few sequences) are diluted and a fair coin reads 17/42, not 1/2; the same bias puts a random shooter at −8 on the 1985 after-3-hits minus after-3-misses test, so Cornell's +4 is really about +12.
SCORES: Hook 9 · Clarity 9 · Visual 9 · Motion 9 · Audio 9 · Concision 8.5 · Originality 9
WEIGHTED: 9.0 (895/100 = 8.95, rounded half-up)   AFTER CEILING: 9.0 (lowest 8.5 + 2 = 10.5; does not bind)
CAPS: none
FINAL: 9.0   PASS: yes
```

**Working.** 15·9 + 25·9 + 15·9 + 15·9 + 10·9 + 10·8.5 + 10·9 = 895. That is 8.95, which rounds half-up to 9.0, the same convention used in rounds 7 and 8. This is a pass at the threshold, not with margin. Fixes 1–3 are the cheapest way to move it clear.

**Caps.** I checked each one and none is triggered:
- Runtime is 3:26.6. Pace is 149 wpm over speech time (472 words).
- Loudness is −14.0 LUFS with a −2.1 dBTP true peak.
- The longest internal silence is 2.17 s, the planned prediction hold at 0:12.7–0:14.8.
- The longest static stretch is 3.37 s, the held 5⅔/14 = 17/42 at 1:42.4–1:45.7.
- There are 0 black frames.
- Banned phrases: 0. "This kind of check" (0:21) means "this type of check" and is not hedging filler.
- The episode asks exactly one question (0:12.8), so there is no question chain.
- The layout audit is clean over 220 settled frames.
- I found no typo, broken LaTeX or clipping in any frame I read.
- Each empirical number is on screen together with its citation:
  - GVT: 0:19–0:33 and 2:11–3:09.
  - Miller & Sanjurjo: 2:27–3:09.
- The narration never names something that is absent within ±2 s.

FACTS:
- "Four flips can land sixteen ways, all equally likely" | Verified | 2⁴ = 16
- Cold-open HHTH: two checked flips, one heads, so 1/2 | Verified | enumeration
- "This row checks three flips, and two are heads" (HHHT: flips 2–4 = H H T) | Verified | enumeration
- Two rows (TTTH, TTTT) have no heads before the last flip, so no score; 14 are scored | Verified | enumeration
- Row scores: six 0s, four 1/2s, one 2/3, three 1s (dots at 0:59.6). The table cells at 0:50.9 all check: 3/3, 2/3, 1/2, 1/2 / 1/2, 0/2, 0/1, 0/1 / 2/2, 1/2, 0/1, 0/1 / 1/1, 0/1, –, – | Verified | enumeration
- Average 17/42 = 40.48% ("17/42 = 40.5%"); "cold by 9.5 points" (50 − 40.48 = 9.52) | Verified | exact fractions
- Pooled: 24 checked flips, 12 H / 12 T, Σh/Σn = 12/24 = 1/2 | Verified | enumeration
- Checked heads in 8 rows, checked tails in 11 rows | Verified | enumeration
- Heads hold 17/3 = 5⅔ of 14 votes, tails 25/3 = 8⅓; 5⅔/14 = 17/42; (1/14)Σhᵢ/nᵢ = 17/42 | Verified | exact fractions; formula re-derived
- After tails, the heads share averages 25/42 = 59.5% (the flipped strip's yellow ends at 59.3% by pixel measurement at 2:00.2). The H↔T swap maps the 16 sequences onto themselves, so the mirror image is exact | Verified | enumeration plus symmetry
- Gap 17/42 − 25/42 = −8/42 = −19.05 points ("minus nineteen") | Verified | exact
- GVT 1985: 26 Cornell players, up to 100 shots each, at a distance chosen for about 50%; compared after 3 hits with after 3 misses; called the belief "a powerful and widely shared cognitive illusion" | Verified | Gilovich, Vallone & Tversky 1985, *Cognitive Psychology* 17(3):295–314; the quote via M&S 2018 (GVT pp. 312–313); 26 players (14 men, 12 women) per M&S §3.1
- Random shooter, n = 100, p = .5: after 3 hits 46%, after 3 misses 54% | Verified | my DP: 46.03% / 53.97%
- "puts the gap at about minus eight points" | Verified | my DP gives −7.94. M&S §3.2, verbatim: "Under GVT's design target of each player taking n = 100 shots and making half (p = .5) of them … the expected difference (and the strength of the bias) is -8 percentage points."
- "Longer records shrink it; longer streaks grow it"; the ghosts at −0.71 (1,000 shots) and −1.01 → −3.14 → −7.94 (k = 1, 2, 3 at n = 100) | Verified | my DP: −1.010, −3.137, −7.935; my simulation at n = 1,000, k = 3: −0.70. M&S abstract: "decreases as the sequence gets longer, but increases in streak length".
- Cornell: 49% after 3 hits, 45% after 3 misses, +4, "too close to zero to count" ("vs 0: p = .49") | Verified | M&S §3.1, verbatim: "players on average hit .49 when on a hit streak, versus .45 when on a miss streak. GVT's paired t-test finds the difference to be statistically indistinguishable from zero, and we replicate this result (p=.49)."
- "Measured from minus eight, it's twelve points hot" | Verified | M&S §3.2, verbatim: "the difference … of +4 percentage points observed by GVT is actually +12 percentage points higher than the difference that would be expected from a Bernoulli i.i.d. shooter"
- "evidence for a hot hand in a gym, not proof it survives defenders in a game" | Verified | M&S §3.1 (the controlled design removes defensive pressure) and fn. 22 (defensive adjustment in games)
- Miller & Sanjurjo 2018 · Econometrica | Verified | *Econometrica* 86(6):2019–2047, doi:10.3982/ECTA14943
- Landing: "A fifty percent shooter who averages one half on this test is already running hot" | Verified, in context | correct against the four-shot baseline 17/42 the landing redraws. See fix 6 on how it may generalise.

MECHANICS: runtime 3:26.6 · wpm 149 · max silence 2.17 s · max static 3.37 s · −14.0 LUFS / −2.1 dBTP. Leading silence 0.00 s, trailing 1.74 s. WER 0.7%. Whisper's only slips:
- "a half" heard as "point five".
- At 1:40, "That's" heard as "That".

No technical term or name was misheard; "Sanjurjo" is transcribed correctly.

## Dimension notes (evidence)

**Hook, 9**
- The first frame is the HHTH row (0:01).
- The rule is applied on screen at 0:03–0:07.
- The question "Below, at, or above one half?" lands at 0:12.8 with "< 1/2 / = 1/2 / > 1/2" on the line and a 2.2 s hold. The viewer commits to a likely-wrong answer.
- Stakes: by 0:26 a 1985 study "called the hot hand an illusion", with the verbatim quote on screen at 0:25.8.
- Tension rises in steps:
  - the test reads cold on a fair coin (1:01)
  - yet no flip is biased (1:03)
  - the vote picture
  - the same crowding hid Cornell's hot hand
- The landing (3:11–3:25) redraws the cold-open row and axis and answers the question on them.
- Not a 10: the title promises a "hidden bias", but the first frame alone is not irresistible.

**Clarity, 9**
- Concrete before abstract throughout: the 16-row table, then the 24 pooled flips, then the equal-vote strip packing exactly onto the 40.5% marker (1:41.4). Only after that does the formula (1/14)Σhᵢ/nᵢ = 17/42 sit under Σhᵢ/Σnᵢ = 12/24 (1:49.2).
- After one watch a viewer can re-derive 17/42 and say why it is below 1/2.
- Assumptions are stated:
  - a fair coin
  - the 100-shot design at about 50%
  - "in a gym, not … in a game"
- Every number checks and both sources are correct.
- Remaining soft spots:
  - The mirror (1:53–2:00) is asserted ("Swap heads and tails, and the strip flips over one half") without saying why: the fair coin is symmetric.
  - The bridge from −19 (k = 1, four flips) to −8 (k = 3, 100 shots) rests on one 4.2 s line with two ghosts (2:40.6–2:44.8, fix 2).
  - The payoff carries 15 spoken numbers in 54 s (2:09–3:03).

**Visual, 9**
- Hues are used consistently:
  - yellow: heads/hits
  - grey: tails/misses
  - blue: the test and what it reads
  - red: bias
  - purple: Cornell's real data
  - white dashed: the obvious guess
- Context steps back to 25–40% rather than vanishing (1:22.2, 1:41.4).
- Every settled frame I read has one focal point. All axes are labelled with quantity and unit. Citations sit bottom-left, above y = −3.2.
- Not a 10, for two nitpicks:
  - The 1:13–1:50 frames carry the dimmed table, the pooled strip, its formula and the vote strip together. They are legible but dense.
  - The transition frames listed under Motion.

**Motion, 9**
- These moves carry the argument:
  - each check ring is drawn on its flip
  - the dots fall onto the line
  - the live marker settles on 17/42
  - the vote regroup and resize (1:15–1:17)
  - the pack onto the marker
  - the half-turn mirror about 50%
  - the ×5 zoom from the share axis to the gap axis
  - the −8 → +4 brace
  - the 14 landing rows flying into (1/14)Σ
- Objects persist: the axis lives from 0:07 to the end.
- Nitpicks:
  - Mid-zoom at 2:38.7, six tick labels (25%, −10, −5, +5, +10, 75%) and two dim axis titles pile into the middle half of the axis for about 0.5 s.
  - The streak ghost's −1 → −3 → −8 steps take about 0.6 s each (2:43.6–2:45.4).
  - At 3:10.3 everything, axis included, dips to about 15% opacity, so the "axis carries into the landing" reads as a near-empty dip.

**Audio, 9**
- Pace is 149 wpm, with shaped pauses after key results (0.9–1.1 s at 1:02.5, 2:39.6, 3:03.0).
- All 7 deictics landed.
- There is no mispronunciation; "Sanjurjo" and "Cornell" are transcribed correctly.
- Loudness is on target.

**Concision, 8.5**
- 472 words in 3:26.6, and almost every sentence carries weight.
- One slack beat: 1:18–1:35 demonstrates crowding twice in a row, first by example ("three heads share a single vote … this lone tails gets a whole one"), then by count ("Twelve heads crowd into eight rows. Twelve tails spread across eleven"). The on-screen "12 heads · 8 rows / 12 tails · 11 rows" already carries the count.
- "Out of forty two" is spoken four times (0:56, 1:42, 2:03, 3:15). I count these as deliberate callbacks, not slack.

**Originality, 9**
- The equal-vote strip whose yellow slices pack exactly onto the 40.5% marker is a memorable, shareable image of a famously slippery result.
- So is the half-turn mirror into −19.
- The payoff follows the Veritasium misconception arc with real sources and an honest limit ("no defenders").
- No slop.

## FIXES (highest impact first)

1. **[1:18–1:35][Concision] Crowding is shown twice in a row.** The example and then the count make the same point.
   - Cut the spoken "Twelve heads crowd into eight rows. [pause 0.3] Twelve tails spread across eleven."
   - Keep the boxed rows and the "12 heads · 8 rows / 12 tails · 11 rows" labels, and run them silently under the last 2 s of "while this lone tails gets a whole one" and the [pause 0.8] after "Line them up:".
   - This saves about 5.5 s and lifts Concision to 9.
2. **[2:40.6–2:45.4][Clarity/Motion] The bridge from −19 to −8 is too fast to read.** "Longer records shrink it; longer streaks grow it" passes in 4.2 s. The 1,000-shot ghost sits at about 40% opacity, and the streak ghost's two slides take about 0.6 s each.
   - Raise both ghosts to 75% opacity.
   - Make each streak slide (−1.01 → −3.14 and −3.14 → −7.94) last at least 1.0 s, adding [pause 0.6] after "longer streaks grow it" to absorb it.
   - Spend 0.4 s more on the 1,000-shot ghost before it leaves.
3. **[1:53–1:58][Clarity] The mirror is asserted, not justified.** Change "Now score the flip after each tails. Swap heads and tails, and the strip flips over one half:" to "Now score the flip after each tails. A fair coin can't tell heads from tails, so the strip flips over one half:". That is +3 words, roughly paid for by fix 1, and it gives the one-clause reason the 59.5% must mirror 40.5%.
4. **[2:38.4–2:39.2][Motion/Visual] Mid-zoom label pile-up (frame 2:38.7).** Fade 25%/75% (and 0%/100%) fully out in the first 0.4 s of the zoom, before −10/−5/+5/+10 appear. Then fade the new labels in at their final tick positions instead of growing them out of the centre. This also keeps the two axis titles from sharing the frame.
5. **[3:09.6–3:10.8][Motion] Near-empty dip at 3:10.3 (everything at about 15%).** Keep the number line, its ticks and the dashed line at 100% through the 1.3 s move, as `script.md` §9 specifies. Then only the payoff marks fade and the axis visibly becomes the cold-open axis.
6. **[3:22–3:26][Clarity] The landing tag may be over-applied to real players.** The payoff has just shown that real 100-shot records carry only about −1 point of one-hit bias.
   - Change the grey tag "its rows average 1/2" to "its 4-shot rows average 1/2", in the same Text size and place, 0.15 clear of the dot.
   - The spoken line can stay.
7. **[2:33.8–2:37.3][Concision/Clarity] One number too many.** The busiest payoff stretch speaks "twenty eighteen" while the M&S citation is already on screen. Change "Miller and Sanjurjo's twenty eighteen paper [pause 0.5] puts the gap" to "Miller and Sanjurjo [pause 0.4] put the gap". That removes one spoken number from 2:24–2:41, and the citation holds the year.

REACHES 9 IF ALL FIXED: yes. It is already at 9.0 by rounding. Fixes 1–3 would put Concision at 9 and give Clarity margin, to about 9.1–9.2, with no structural change needed.

KEEP:
- The equal-vote strip: the 1:15–1:17 resize to one vote per row and the 1:37–1:41 pack of the yellow slices exactly onto the 40.5% marker, then 5⅔/14 = 17/42.
- The half-turn mirror into the −19 gap (1:57–2:09), and the payoff chain 46/54 → −8 → 49 − 45 = +4 → "+12 points", with "vs 0: p = .49", "no defenders" and both citations at full strength.
- The landing that answers the cold-open question on the cold-open row and axis with (1/14)Σᵢhᵢ/nᵢ = 17/42 and the blue "hot" arrow.
