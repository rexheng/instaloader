EPISODE: 004 — "The Hidden Bias That Hid the Hot Hand"
IDEA: If you average "share of heads after a heads" one short sequence at a time, every sequence gets one vote while checked heads crowd into a few sequences, so a fair coin reads 17/42 instead of 1/2. The same crowding puts a random shooter at −8 points on the 1985 after-3-hits minus after-3-misses test, so Cornell's +4 is really +12.
SCORES: Hook 9 · Clarity 9 · Visual 9 · Motion 9 · Audio 9 · Concision 9 · Originality 9
WEIGHTED: 9.0 (15·9 + 25·9 + 15·9 + 15·9 + 10·9 + 10·9 + 10·9 = 900 / 100)   AFTER CEILING: 9.0 (lowest 9; 9 + 2 = 11 does not bind)
CAPS: none. I checked each one:
- Runtime 3:22.8 (in 2:30–4:00). Pace 151 wpm over speech time (137 overall).
- Loudness −14.1 LUFS, true peak −2.1 dBTP.
- Silence: leading 0.00 s, trailing 1.74 s. The longest internal silence is 2.17 s at 0:12.4–0:14.5, which is the planned prediction hold.
- Longest fully static stretch 3.53 s (2:58.4–3:02.0, the +12 frame).
- 0 black frames. 0 banned phrases. The only question in the episode is the cold-open one, so there is no question chain. No recap ending.
- The layout audit found 0 issues in 219 checks. In the keyframes I read I found no settled overlap, clipping, typo or broken LaTeX.
- Citations are on screen whenever their numbers are:
  - "Gilovich et al., 1985 · Cognitive Psychology" from 0:19 to 0:33 and again from 2:09.
  - "Miller & Sanjurjo, 2018 · Econometrica" from 2:24 to 3:06.
- Hook by 0:15: the question is complete at 0:12.4.
- No factual error (see FACTS).
FINAL: 9.0   PASS: yes

EVIDENCE USED
- `review/metrics.json` (00:26) is newer than `final.mp4` (00:25), so I used the existing `review/` pack.
- I read `report.md`, `narration_diff.txt`, `narration.txt`, `transcript_words.tsv` (deictic timings), the palette block of `script.md`, `facts.md` and the round-10 CHANGELOG. I re-ran `check_numbers.py`.
- All 12 contact sheets.
- 15 full-resolution keyframes: kf_04 0:10.8, kf_07 0:27.6, kf_12 0:47.3, kf_14 0:59.3, kf_17 1:19.0, kf_20 1:31.6, kf_22 1:37.0, kf_25 1:52.5, kf_28 2:09.2, kf_30 2:22.8, kf_31 2:37.8, kf_33 2:52.3, kf_34 3:01.1, kf_37 3:14.9, kf_40 3:22.8.
- 24 extra full frames I extracted into /tmp/ep4r11: 0:41.6, 0:42.0, 1:09.3, 1:09.7, 1:10.0, 1:10.6, 1:11.2, 1:29.6, 1:30.4, 1:34.5, 1:55.8, 2:07.6, 2:08.2, 2:33.6, 2:34.4, 2:53.8, 2:56.6, 2:57.4, 3:12.2, 3:12.8, 3:13.4, 3:18.0, 3:19.8, 3:20.6.
- Strips: 6 fps over 1:08.4–1:10.2 (the 12/24 build) and 4 fps over 1:26.9–1:28.4 ("this lone tails").

FACTS:
- Four flips give 16 equally likely sequences | Verified | 2^4
- HHTH: the checked flips are H and T, so 1/2 | Verified | enumeration
- HHHT checks 3 flips, and 2 are heads | Verified | enumeration
- TTTH and TTTT get no score, so 14 rows are scored | Verified | `check_numbers.py`
- The table scores in kf_12 (3/3, 1/2, 2/2, 1/1 · 2/3, 0/2, 1/2, 0/1 · 1/2, 0/1, 0/1, – · 1/2, 0/1, 0/1, –) | Verified | I enumerated all 16 rows by hand
- The dot stacks in kf_14 are 0 ×6, ½ ×4, ⅔ ×1 and 1 ×3; the mean is 17/42 = 40.5%; "cold by nine and a half points" | Verified | 50 − 40.48 = 9.52
- The 24 checked flips are 12 H and 12 T; Σhᵢ/Σnᵢ = 12/24 | Verified | `check_numbers.py`
- "12 heads · 8 rows", "12 tails · 11 rows" (kf_20) | Verified | 8 rows hold a checked H; 11 hold a checked T
- The heads hold 5⅔ of the 14 votes, so 5⅔/14 = 17/42; the tails hold 8⅓ | Verified | Σhᵢ/nᵢ = 17/3
- After tails the average is 25/42 (mirror about ½ by H↔T symmetry); the gap is −19 points | Verified | 17/42 − 25/42 = −4/21 = −19.05 pts
- GVT 1985, *Cognitive Psychology*, "a powerful and widely shared cognitive illusion" | Verified | GVT 17(3):295–314, quoted in M&S 2018 fn. 8
- 26 Cornell players, up to 100 shots each, from where they hit about half | Verified | M&S 2018 §3.1 and Table 2
- A random shooter (n = 100, k = 3) averages 46% after hits and 54% after misses | Verified | exact DP gives 0.4603 / 0.5397 (`check_numbers.py`); M&S Fig. 1
- M&S put the gap at about −8 points | Verified | M&S §3.2 "-8 percentage points"; DP gives −7.94
- Longer records shrink the gap (−0.71 at 1,000 shots); longer streaks grow it (−1.01, −3.14, −7.94) | Verified | DP; M&S abstract
- Cornell hit 49% after 3 hits and 45% after 3 misses, so +4; "1985 test: p = .49" | Verified | M&S §3.1 Results, quoted in facts.md row 58
- +4 measured from −8 is +12 points | Verified | arithmetic; M&S §3.2 states +12
- "Evidence for a hot hand in a gym, not proof it survives defenders in a game" | Verified | the Cornell study was a controlled shooting test (M&S §3.1)
- Econometrica 86(6):2019–2047 (2018) | Verified | facts.md row 21

MECHANICS: runtime 3:22.8 · wpm 151 (speech time) · max silence 2.17 s (planned prediction hold) · max static 3.53 s · −14.1 LUFS / −2.1 dBTP · leading 0.00 s, trailing 1.74 s · WER 0.7%

WHAT I SAW, BEAT BY BEAT (craft lens)

Cold open, 0:00–0:15:
- The first frame is the object: coins flip in at 0:01.
- At 0:05 the checks are drawn as blue arcs and rings. The 1/2 is built with a yellow numerator and a blue denominator (kf_04), so the palette is taught in the first five seconds.
- At 0:09 a dim ghost of the 16 runs deals in.
- The answers "< 1/2", "= 1/2" and "> 1/2" are written onto the axis at the values they name, during the words (0:11–0:13), and then held silently for 2.2 s.
- Reading the options off their own positions on the axis is a commitment device, not a slide.

Stakes, 0:15–0:37:
- "= 1/2" becomes the dashed line and "the obvious guess".
- H/T morphs to hit/miss, and the axis title changes with it (kf_07).
- The quote and citation are on screen together.
- "→ hot" defines the direction once (0:29), then steps back (0:33).

Calibrate and fail, 0:37–1:05:
- The big row shrinks into its slot in the 16-row table, so the object persists.
- "This row" (0:41.4): the HHHT box is half-drawn at 0:41.6 and complete at 0:42.0. The ring-by-ring check follows.
- The two unscored rows are boxed and then dimmed with "–" (kf_12 → kf_14).
- The dots run to their stacks, and the live marker settles on 17/42 = 40.5%. The red "cold −9.5 points" arrow lands on "cold" (1:01).
- kf_14 is a frame you could teach from: one marker, one guess line, one gap.

Insight, 1:05–1:49:
- The pour runs column by column; the other columns sit at about 30%.
- The tiles sort to 12 | 12 on the dashed line, and Σᵢhᵢ/Σᵢnᵢ = 12/24 is built from them with no glyph morph (6 fps strip 1:08.4–1:10.2).
- The tiles cascade down into 14 equal votes (sheet 5, 1:15).
- Both deictics are on time:
  - "Here, three heads" (1:23.8): HHHH box and strip cell at 1:25.
  - "this lone tails" (1:27.0): HTTT box starts drawing at 1:27.15 (4 fps strip).
- The silent 8-row and 11-row boxing (1:29.6–1:32) shows the crowding in the 2.0 s pause.
- At 1:33 the yellow slices pack exactly onto the blue 40.5% marker (kf_22). 5⅔ travels out and = 17/42 completes.
- (1/14) Σ hᵢ/nᵢ stands under Σhᵢ/Σnᵢ, each beside its own strip (1:47 and 1:49). This is the proof, and it is a picture.

Mirror, 1:49–2:07:
- The copy drops into a second lane and half-turns about the dashed line (1:55.8 is mid-turn).
- It lands at 25/42, and the red −19 arrow joins the two cursors.

Payoff, 2:07–3:06:
- The axis title word-swaps "flips/heads" → "shots/hits" (2:07.6). "after" stays put while "heads/tails" are replaced by "3 hits/3 misses".
- The design column builds phrase by phrase on the words ("26 Cornell players", "up to 100 shots").
- The cursors grow out of 50% on "random shooter" (kf_30) and slide to 46% and 54% on the numbers.
- The gap slides onto zero and the axis zooms ×5 into the gap axis (2:33–2:35).
- The ghosts are readable: "1,000 shots" (kf_31) and ●●● (2:41).
- "random" becomes purple "Cornell" with "?" values. Then come 49%, 45%, "49 − 45 = +4" on the purple marker and "1985 test: p = .49". The right column steps back to 30% (kf_33), the chart re-centres (2:57), and the +12 brace and "no defenders" follow (kf_34).
- The round-10 header sentence is gone, and the payoff frame now has one subject.

Landing, 3:06–3:23:
- HHTH returns on the cold-open axis, and the ghost of the 16 runs returns.
- The rows fly into "1/14 Σ". hᵢ/nᵢ is written only after they land (3:12.8 → 3:13.4), which fixes round 10's fly-over.
- The marker draws at 40.5% = 17/42 (kf_37). The row becomes hit/miss, and the blue dot appears at ½: "its 4-shot rows average 1/2".
- The "hot" arrow ends on that dot (kf_40, 3:20.6). The ending answers the cold-open question on the cold-open image.

Round-10 craft fixes, verified in this cut:
- The 12/24 glyph tumble is gone; tiles fly in instead.
- The right column steps back at 2:53.
- The header sentence is gone.
- The landing fly-over is fixed.
- The "This row" box is on time.
- The hook ends at 0:12.4.

WHAT KEEPS EACH DIMENSION AT 9 RATHER THAN HIGHER (each with evidence)

Visual 9:
- (a) 2:08–2:22. The squashed coin strips are left under the new lane labels "after 3 hits" and "after 3 misses", and the axis now reads "checked shots that are hits" (kf_28, 2:08.2). Their yellow fills still end at 40.5% and 59.5%, the 4-flip coin's values, which are neither Cornell's data nor the random shooter's. A viewer who reads fills as data sees a ~40% after-hits lane under "26 Cornell players". The "?" values and half strength soften this, but the picture is briefly saying something untrue about the lanes.
- (b) 2:13–2:16. The right column stacks four full-strength labels ("26 Cornell players / up to 100 shots / after 3 hits / after 3 misses", 13 words; sheet 8, 2:15) beside the lanes. That reaches the §5 12-word ceiling for about 2 s, until the first two dim at 2:17.
- (c) 1:16–1:36. "1 vote per row", the dimmed "40.5%" and the dimmed "the obvious guess" still sit on one baseline across the strip (kf_17, kf_20), reading as one line of three labels. This is a nitpick.

Motion 9:
- (a) 1:09.0–1:10.0. The 12/24 tile flight is meaningful, but the copies shrink to a roughly 20 px streak in about 0.4 s. The yellow copy passes over the grey half of the strip on its way (6 fps strip, frames 2 and 4; frame 1:09.7 shows the 24-copy as a grey smudge beside "24"). The tile-to-number correspondence is asserted rather than seen.
- (b) 1:34.3–1:34.8. The travelling "5⅔" passes over the dimmed Σᵢhᵢ/Σᵢnᵢ formula on its way to the right column (frame 1:34.5: the "5⅔" glyphs sit on top of "Σᵢnᵢ"). The overlap is transient, under 0.5 s.
- Everything else carries meaning: the persistent table, pour, sort, cascade into votes, pack onto the marker, mirror half-turn, word-swap retitle, ×5 zoom with tick handover, ghosts, and the landing return.

Hook 9: one concrete question with placed answer options and a 2.2 s hold, complete at 0:12.4. The ending resolves it on the same row and axis.

Clarity 9:
- Concrete first, and every number checks.
- Assumptions are stated: "no defenders", "up to 100 shots", "about half", "4-shot rows".
- 46/54 is asserted from M&S rather than derived, but it is cited, labelled "random" and made believable by the 4-flip mechanism.

Audio 9:
- 151 wpm. Loudness on target. Planned pauses after results (1:02.2 1.1 s, 1:39.4 1.6 s, 2:40.0 1.9 s).
- The three deictics I timed land within about 0.2–0.6 s.
- WER 0.7%; the only differences are "a half" heard as "point five" and "a" heard as "one", both harmless.
- The kit flags a 12.6 s run without a ≥0.35 s breath from 1:48.7 (the mirror sentence). It is dense but intelligible in the transcript.

Concision 9:
- 463 words. Each repeat of "17 out of 42" (0:55, 1:37, 3:11) is a deliberate callback.
- The silent 8-row and 11-row beat replaced a spoken sentence, which was the right cut.
- I could not remove a sentence without losing a step.

Originality 9: the vote strip packing onto the 40.5% marker, the half-turn mirror, and a landing that recasts "the obvious" ½ as "already running hot" are images a viewer would remember and share.

FIXES (highest impact first; all are polish, none is needed to pass):
1. [2:07.0–2:22.0][Visual] The squashed 4-flip strips sit under "after 3 hits / after 3 misses" with yellow fills ending at 40.5% and 59.5% (kf_28), which reads as data for the new lanes. On "The nineteen eighty five study", keep the squash and word-swap but recolour both strips to outline-only: fill_opacity 0, stroke at 40%, tile edges kept. They then read as the same comparison with the values unknown, and the "?" carries the unknown. Alternatively, fade the yellow fill to 0 over 0.6 s right after the squash, before "on twenty six Cornell players" (2:10.5).
2. [1:09.0–1:10.0][Motion] The 12/24 tile copies shrink into an illegible streak in about 0.4 s, and the yellow copy crosses the grey half of the strip (strip frames at 1:09.0 and 1:09.7).
   - Lift each copy group 0.6 units above the strip before it travels, so its path clears the tiles. Keep it at ≥ 40% of its size until it is within 0.5 units of the numeral, then shrink into it.
   - Use run_time 0.9 s with rate_func smooth, and a lag_ratio of 0.04 so the 12 (then the 24) tiles read as a stream.
3. [2:13.0–2:17.0][Visual] Four full-strength stacked labels in the right column total 13 words (sheet 8, 2:15). Dim "26 Cornell players" to 40% as soon as "up to 100 shots" is written (about 2:14.0), not on "about half". Keep "up to 100 shots" at full strength until 2:17.
4. [1:34.3–1:34.8][Motion] The travelling "5⅔" crosses the dimmed Σᵢhᵢ/Σᵢnᵢ (frame 1:34.5). Route it on an arc below that formula (path_arc −0.6, end at the 5⅔/14 slot from below), or shift the 12/24 formula up 0.25 before the flight. That keeps 0.15 units of clearance throughout.
5. [1:16–1:36][Visual, nitpick] "1 vote per row", the dim "40.5%" and the dim "the obvious guess" share a baseline (kf_17). Raise the dim "the obvious guess" 0.2 units so it sits at the dashed line's top, as it does at 2:17. Then the strip tag stands alone on its row.

REACHES 9 IF ALL FIXED: yes. It is already at 9.0 with no cap. Fixes 1–2 are what would move Visual and Motion toward 9.5. Nothing structural is missing: the hook commits the viewer, the failure is measured, the insight is one picture, the payoff is cited and states its limits, and the landing re-sees the first frame.
KEEP:
- 1:31–1:49: the yellow third-of-a-vote slices pack exactly onto the blue 40.5% marker, become 5⅔/14 = 17/42, and stand as (1/14) Σ hᵢ/nᵢ under Σhᵢ/Σnᵢ = 12/24, each beside its own strip.
- 1:53–2:07: the half-turn mirror of the vote strip about the dashed 50% line into 25/42, and the red −19 arrow.
- 3:06–3:23: the landing answers the cold-open question on the cold-open row and axis (17/42 marker, then the "hot" arrow onto the one-half dot).
