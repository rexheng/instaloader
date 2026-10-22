EPISODE: 004 — "The Hidden Bias That Hid the Hot Hand"
IDEA: If you average "share of heads after a heads" one short sequence at a time, each sequence gets one vote while checked heads crowd into a few sequences, so a fair coin reads 17/42 instead of 1/2. The same crowding puts a random shooter at −8 points on the 1985 after-3-hits minus after-3-misses test, so Cornell's +4 is really +12.
SCORES: Hook 9 · Clarity 9 · Visual 9 · Motion 9 · Audio 9 · Concision 9 · Originality 9
WEIGHTED: 9.0 (15·9 + 25·9 + 15·9 + 15·9 + 10·9 + 10·9 + 10·9 = 900 / 100)   AFTER CEILING: 9.0 (lowest 9; 9 + 2 = 11, does not bind)
CAPS: none. I checked each one:
- Runtime 3:23.1.
- Pace 151 wpm over speech time (136 overall).
- Loudness −14.1 LUFS and −2.1 dBTP.
- Leading silence 0.00 s, trailing 1.74 s.
- Longest internal silence 2.17 s, the planned prediction hold at 0:12.7–0:14.8.
- Longest static stretch 3.53 s, the +12 frame at 2:58.7–3:02.3.
- 0 black frames and 0 banned phrases. The cold open asks one question, not a chain.
- The layout audit found 0 issues in 218 frames. I found no settled overlap or clipping in any keyframe I read.
- Citations: GVT is on screen from 0:19 to 0:33 and from 2:09 on. M&S is on screen from 2:24 on, whenever 46/54, −8, p = .49 or +12 is shown.
- The deictics land: "This row" 0:41.2 → box by 0:42.2; "Here, three heads" 1:24.1 → HHHH box at 1:24.4; "this lone tails" 1:27.3 → HTTT box growing at 1:27.6.
- I found no factual or mathematical error (see FACTS).
FINAL: 9.0   PASS: yes

EVIDENCE USED
- `review/metrics.json` (21:52) is newer than `final.mp4` (21:50), so I used the existing `review/` pack.
- I read `report.md`, all 12 contact sheets, `transcript.txt`, `transcript_words.tsv` (deictic timings), `script.md`, `facts.md`, `narration_diff.txt` and the round-9 CHANGELOG, and re-ran `check_numbers.py`.
- Full-resolution keyframes: kf_04 0:11.1, kf_07 0:24.3, kf_13 0:45.9, kf_15 0:59.6, kf_19 1:22.6, kf_23 1:33.5, kf_25 1:45.1, kf_27 1:52.8, kf_29 2:09.5, kf_31 2:24.2, kf_32 2:38.1, kf_33 2:43.6, kf_34 3:01.4, kf_36 3:10.8, kf_37 3:15.2, kf_40 3:23.1.
- Extra frames I extracted with ffmpeg into /tmp/ep4r10: 0:13.5, 0:41.6, 0:42.2, 0:42.6, 0:52.6, 1:06.6, 1:10.6, 1:11.0, 1:11.6, 1:24.4, 1:24.9, 1:27.6, 1:34.2, 1:35.6, 1:55.8, 2:20.0, 2:33.0, 2:40.4, 2:53.2, 2:57.0, 3:17.8, 3:19.2.
- Strips: a 10 fps crop of 1:10.6–1:11.8 (the 12/24 restack) and a 5 fps strip of 3:11.6–3:14.0 (the landing rows flying into the formula).

FACTS:
- 4 flips give 16 equally likely sequences | Verified | 2^4
- HHTH: the checked flips are H and T, so 1/2 | Verified | enumeration
- HHHT checks 3 flips and 2 are heads | Verified | enumeration
- TTTH and TTTT have no score, so 14 rows are scored | Verified | `check_numbers.py`
- Dot stacks 0×6, ½×4, ⅔×1, 1×3 (kf_15); mean 17/42 = 40.5%; "cold by 9.5 points" | Verified | 50 − 40.48 = 9.52
- 24 checked flips, 12 H and 12 T, so the pooled share is exactly ½ (Σhᵢ/Σnᵢ = 12/24) | Verified | `check_numbers.py`
- 12 heads sit in 8 rows, 12 tails in 11 rows | Verified | `check_numbers.py`
- Heads hold 5⅔ of the 14 votes (kf_23); 5⅔/14 = 17/42; tails hold 8⅓ | Verified | Σhᵢ/nᵢ = 17/3
- After a tails the reading is 25/42; the gap is −19 points | Verified | −4/21 = −19.05 pp
- GVT 1985, *Cognitive Psychology*: "a powerful and widely shared cognitive illusion" | Verified | GVT 17(3):295–314, quoted in M&S 2018 fn. 8 (facts.md row 13)
- 26 Cornell players, up to 100 shots each, from a distance where they hit about half | Verified | M&S 2018 §3.1 and Table 2
- Random shooter, n = 100, k = 3: 46% / 54% "on average" | Verified | exact DP 0.4603 / 0.5397 (`check_numbers.py`); M&S Fig. 1
- M&S: the gap for a random shooter is about −8 points | Verified | M&S §3.2 "-8 percentage points"; DP −7.94, simulation −7.93
- Longer records shrink it (ghost at −0.71 for 1,000 shots); longer streaks grow it (−1.01, −3.14, −7.94) | Verified | DP output; M&S abstract
- Cornell: 49% after 3 hits, 45% after 3 misses, so +4; "vs 0: p = .49" | Verified | M&S §3.1
- Measured from −8, +4 is +12 points | Verified | arithmetic; M&S §3.2 states +12
- "Evidence for a hot hand in a gym, not proof it survives defenders in a game" / "no defenders" | Verified | GVT's Cornell study was a controlled shooting test (M&S §3.1)
- Citations "Gilovich et al., 1985 · Cognitive Psychology" and "Miller & Sanjurjo, 2018 · Econometrica" | Verified | Econometrica 86(6):2019–2047

MECHANICS: runtime 3:23.1 · wpm 151 (speech time) · max silence 2.17 s (planned prediction hold) · max static 3.53 s · −14.1 LUFS / −2.1 dBTP · leading 0.00 s / trailing 1.74 s · WER 0.7%

WHAT I SAW, BEAT BY BEAT (craft lens)

Cold open, 0:00–0:15:
- The first frame is the object: four coins flip in.
- At 0:05 blue arcs and rings mark the two checked flips, and 1/2 is built with a yellow numerator and a blue denominator.
- At 0:09 a ghost of the 16 runs deals in and collapses to "?". At 0:13 the answers "< 1/2", "= 1/2" and "> 1/2" sit on the axis at their values.
- The question ends at 0:12.8 and is followed by a 2.2 s hold.

Stakes and test, 0:15–0:37:
- "= 1/2" becomes "the obvious guess" with the dashed line.
- At 0:23 H/T morphs into hit/miss, and the axis title changes with it (kf_07).
- The quote appears at 0:27, and "→ hot" defines the direction once at 0:29.
- The palette stays semantic throughout: yellow is heads, grey is tails, blue is what the test reads, red is the bias, purple is Cornell.

Calibrate and fail, 0:37–1:05:
- The big row shrinks into its slot in the table, so the object persists.
- HHHT is worked ring by ring. TTTH and TTTT are boxed and dimmed with "–".
- The dots run the channels to their stacks (0:52.6), and the live marker settles on 17/42 = 40.5%.
- The red "cold −9.5 points" arrow lands on "cold".
- kf_15 is a frame you could teach from: one marker, one guess line, one gap.

Insight, 1:05–1:49:
- The pour now runs one card column at a time with the other columns at 30% (1:06.6). Each disc is traceable to its coin, which fixes round 9's particle cloud.
- The tiles sort to 12 | 12 on the dashed line. Σhᵢ/Σnᵢ = 12/24 is built from the table's numerators and denominators.
- The same tiles regroup into 14 equal votes (kf_19). HHHH and HTTT are boxed on their words.
- The 8 heads rows (1:31) and then the 11 tails rows get their counts.
- At 1:33 the yellow slices pack exactly onto the blue 40.5% marker (kf_23). 5⅔ travels out, the outlines brighten as they are counted into 14 (1:35.6), and = 17/42 completes.
- 1/14 Σ hᵢ/nᵢ = 17/42 then stands beside Σhᵢ/Σnᵢ = 12/24, each next to its own strip (kf_25). This is the episode's proof, and it is genuinely visual.

Mirror, 1:49–2:07:
- The copy drops into a second lane, recolours on "can't tell heads from tails", and half-turns about the dashed line (1:55.8 is mid-turn, foreshortened about 50%).
- It lands at 25/42, and the red −19 arrow joins the two cursors.

Payoff, 2:07–3:06:
- The cursors leave with the strips, and the dashed line stays visible for the "about half" pulse (kf_29, frame 2:20.0). This fixes round 9.
- The cursors grow from 50% on "For a random shooter" (kf_31) and slide to 46% / 54% on the words.
- The gap slides onto zero and the axis becomes −10…+10 (2:33–2:35).
- The ghosts are now readable at phone size: "1,000 shots" (kf_32) and the ●● streak ghost (2:40.4).
- "random" turns into "Cornell" with purple "?" values (kf_33). This fixes round 9's wrong-header numbers.
- Then come 49%, 45%, 49 − 45 = +4 on the purple marker, "vs 0: p = .49" (2:53.2), the re-centre, the +12 brace (kf_34) and "no defenders".

Landing, 3:06–3:23:
- The gap axis drops into the cold-open share axis, and HHTH returns (3:07).
- The ghost of the 16 runs returns (kf_36), and its rows fly into (1/14) Σ hᵢ/nᵢ (3:12–3:13).
- The marker draws at 40.5% with = 17/42 (kf_37). The row becomes hit/miss, and a blue dot appears at one half: "its 4-shot rows average 1/2".
- The "hot" arrow ends on that dot (kf_40). The ending re-sees the first frame and answers its question on the same image.

All round-9 craft fixes are in and working:
- Cornell "?" values.
- No cursors over the dashed line on "about half".
- The column-by-column pour.
- The "1 vote per row" / 40.5% separation, now about 1 unit apart with the readout dimmed.
- Bigger ghosts.

WHAT KEEPS EACH DIMENSION AT 9 RATHER THAN 10 (nitpicks, each with evidence)

Visual 9:
- (a) 2:13–2:36: the grey header "1985 design · 26 players · up to 100 shots" is an 8-word block, which breaks §5's 7-per-block rule (kf_31, kf_32). It also repeats the narration word for word. It is dimmed after 2:21, so the damage is small.
- (b) 2:51–2:56: the right column (Cornell / 49% / 45%) stays bright beside the "49 − 45 = +4" working, which already carries the same numbers. The working's right end is about 0.44 units from "after 3 misses" (frame 2:53.2), so the frame has two competing focal points for about 5 s.
- (c) 1:16–1:36: "1 vote per row" and the dimmed "40.5%" still share one baseline (kf_19). They are now about 1 unit apart, so this is a nitpick only.

Motion 9:
- (a) 1:10.9–1:11.3: the inline "12/24" restacks into a vertical fraction by morphing glyphs. In frame 1:11.0 the slash tumbles across "12" as a grey blob before it becomes the fraction bar. It lasts about 0.3 s, but it is the only glyph soup in the cut.
- (b) 3:12.5–3:13.3: the landing's 14 rows arc into the sum while hᵢ/nᵢ is already fading in, so small coins pass over the fraction glyphs (strip frame 3:13.0).
- Everything else carries meaning: the persistent table, pour, sort, regroup, resize, pack, mirror half-turn, zoom with tick handover, the ghosts, and the landing return.

Hook 9: the question ends at 0:12.8, slightly past the anchor's 0:12. The ending resolves the opening exactly.

Clarity 9:
- Concrete first, and every number checks.
- Assumptions are stated: "no defenders", "up to 100 shots", "about half", and the "4-shot rows" tag.
- The 46/54 are asserted from M&S rather than derived on screen, but they are cited and labelled "random". The 4-flip mechanism makes them believable.

Audio 9:
- 151 wpm, LUFS on target, and pauses placed after results (1:02.5 1.1 s, 1:39.7 1.6 s, 2:40.3 1.9 s).
- Every deictic lands within about 0.3–1.0 s.
- "This row" is the slowest: the box is absent at 0:41.6 and present at 0:42.2 for a word that starts at 0:41.2.
- WER 0.7%. The only differences are "a half" heard as "point five" (9.5, correct) and "a" heard as "one".

Concision 9:
- 462 words. Each repeat of "17 out of 42" (0:55, 1:37, 3:11) is a deliberate callback.
- "Longer records shrink it. Longer streaks grow it." is the honest-limits line and earns its 5 s.
- I could not cut a sentence without losing a step.

Originality 9: the vote strip packing onto the 40.5% marker and the mirror half-turn are images a viewer would remember and share. The landing reframes the cold open's "obvious" one half as "already running hot".

FIXES (highest impact first; all are polish, none needed to pass):
1. [1:10.9–1:11.3][Motion] The inline "12/24" → stacked-fraction morph tumbles the slash across "12" (frame 1:11.0). Never write the inline 12/24. Have the yellow tiles fly into a stacked numerator "12" and all 24 tiles into the denominator "24" with the fraction bar GrowFromCenter between them, so the tile-to-number correspondence is kept and there is no glyph morph. Otherwise keep the two numbers as separate mobjects: move them into stacked position, FadeOut the slash (shift DOWN·0.1) and GrowFromCenter the bar (0.6 s, smooth).
2. [2:51.5–2:56.3][Visual] Two focal points compete: the right column's Cornell / 49% / 45% and "49 − 45 = +4" beside the purple marker (frame 2:53.2). As soon as "49 − 45" is fully written (2:51.5), dim the right column to 30% over 0.5 s, as was already done to the random column at 2:35. The marker and its working are then the one subject.
3. [2:13–2:36][Visual] The header block is 8 words and repeats the narration (kf_31). Shorten it to "1985 · 26 players · 100 shots" (6 words; "up to" is already spoken) and keep the same phrase-by-phrase build. On "Longer records" (2:36.3) pulse only "100 shots", as now.
4. [3:12.5–3:13.3][Motion] The landing rows fly over the hᵢ/nᵢ glyphs while they fade in. Write "1/14 Σ" first and land the 14 rows on the Σ (lag as now), then write hᵢ/nᵢ only after the last row has landed (about +0.2 s).
5. [0:41.2–0:42.2][Audio/sync] The "This row" box arrives about 0.7–1.0 s after the word begins (absent at 0:41.6). Start the HHHT box's Create at 0:41.1, 0.1 s before "This", with run_time 0.5.
6. [0:10.2–0:12.8][Hook] To put the commitment at the 0:12 anchor, shorten the pause after "and average" (0:10.2–0:10.6) and the one after "one of the two is heads" (0:06.7–0:07.1) from 0.4 s to 0.2 s. The question then ends about 0:12.4, and the 2.2 s prediction hold stays as it is.
7. [1:16–1:36][Visual, nitpick] "1 vote per row" and the dimmed "40.5%" still share a baseline (kf_19). Drop "1 vote per row" 0.1 units and set it in the grey secondary text colour (#A9AEB6). The tag then reads as a strip name, not as a phrase with the readout.

REACHES 9 IF ALL FIXED: yes. It is already at 9.0 with no cap in play. Fixes 1–2 are what would move Motion and Visual toward 9.5. Nothing structural is wrong: the hook, the measured failure, the one-picture insight, the cited payoff with honest limits, and the landing that re-sees the first frame are all in place.
KEEP:
- 1:31–1:47: the yellow third-of-a-vote slices pack exactly onto the blue 40.5% marker, become 5⅔/14 = 17/42, and stand as (1/14) Σ hᵢ/nᵢ beside Σhᵢ/Σnᵢ = 12/24 next to their own strips.
- 1:53–2:07: the half-turn mirror of the vote strip about the dashed 50% line into 25/42 and the red −19 arrow.
- 3:06–3:23: the landing answers the cold-open question on the cold-open row and axis (17/42 marker, "hot" arrow onto the one-half dot).
