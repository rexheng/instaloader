EPISODE: 004 — "The Hidden Bias That Hid the Hot Hand"
IDEA: Averaging "share of heads after a heads" one row at a time gives every short sequence one vote. Checked heads crowd into a few rows, so a fair coin reads 17/42 instead of 1/2. The same crowding puts a random shooter at −8 points on the 1985 after-3-hits minus after-3-misses test, which makes Cornell's +4 really +12.
SCORES: Hook 9 · Clarity 9 · Visual 8.5 · Motion 8.5 · Audio 9 · Concision 9 · Originality 9
WEIGHTED: 8.9 (15·9 + 25·9 + 15·8.5 + 15·8.5 + 10·9 + 10·9 + 10·9 = 885 → 8.85, rounded half-up)   AFTER CEILING: 8.9 (lowest 8.5; 8.5 + 2 = 10.5, does not bind)
CAPS: none. I checked each one:
- Runtime 3:26.6.
- Pace 149 wpm over speech time.
- Loudness −14.0 LUFS and −2.1 dBTP.
- Longest internal silence 2.17 s, the planned prediction hold at 0:12.7–0:14.8.
- Longest static stretch 3.37 s, the held 5⅔/14 = 17/42 at 1:42.4–1:45.7.
- 0 black frames and 0 banned phrases. The cold open asks one question, so there is no rhetorical-question chain.
- The layout audit found 0 issues in 220 frames.
- Both studies are cited on screen whenever they are used: GVT from 0:19, M&S from 2:27.
- 7 of 7 deictic words land.
- I found no settled overlap or clipping in any keyframe I read.
- The 2:46–2:50 label/value mismatch (fix 1) is a visual and clarity defect, not cap 6. The dimmed numbers are the correct random-shooter values, but they sit under the wrong head.
FINAL: 8.9   PASS: no

EVIDENCE USED
- `review/metrics.json` (20:22) is newer than `final.mp4` (20:21), so I used the existing `review/` pack.
- I read `report.md`, all 12 contact sheets, `transcript.txt`, `narration.txt`, `script.md`, `facts.md` and the `check_numbers.py` output (re-run).
- Full-resolution keyframes: kf_04 0:11.1, kf_05 0:16.1, kf_07 0:24.3, kf_13 0:45.9, kf_15 0:59.6, kf_19 1:22.2, kf_23 1:32.1, kf_25 1:41.4, kf_26 1:49.2, kf_29 2:00.2, kf_31 2:18.9, kf_33 2:42.5, kf_34 2:47.2, kf_35 3:05.1, kf_38 3:21.0, kf_40 3:26.6.
- 26 extra frames I extracted with ffmpeg into /tmp/ep4r9: 0:52.6, 0:53.4, 1:06.6, 1:07.6, 1:15.6, 1:27.0/.5, 1:28.0/.5, 1:58.4, 2:19.4/.9, 2:20.4/.9, 2:38.0, 2:38.6, 2:39.6, 2:44.0, 2:45.8, 2:46.2, 2:47.8, 2:49.5, 3:00.6, 3:10.3, 3:15.8, 3:16.6.
- Word timings from `transcript_words.tsv`: "lone" 1:27.08, "about half" 2:19.2–2:20.3, "Cornell" 2:45.8, "49%" 2:47.3, "45" 2:50.5.
- One web search confirmed the M&S −8 pp quote in the Wharton and Melbourne PDFs.

FACTS:
- 4 flips give 16 equally likely sequences | Verified | 2^4
- HHTH: the checked flips are H and T, so 1/2 | Verified | enumeration
- HHHT checks 3 flips and 2 are heads (kf_13) | Verified | enumeration
- TTTH and TTTT have no score, so 14 rows are scored | Verified | enumeration (`check_numbers.py`)
- Dot stacks 0×6, ½×4, ⅔×1, 1×3; mean 17/42 = 40.5%; "cold by 9.5 points" (kf_15) | Verified | exact fractions; 50 − 40.48 = 9.52
- 24 checked flips, 12 H and 12 T, so the pooled share is exactly ½ | Verified | Σh = 12, Σn = 24
- 12 heads sit in 8 rows, 12 tails in 11 rows | Verified | enumeration
- Heads hold 5⅔ of the 14 votes (kf_25); 5⅔/14 = 17/42; tails hold 8⅓ | Verified | Σhᵢ/nᵢ = 17/3
- After a tails the reading is 25/42; the gap is −19 points | Verified | 17/42 − 25/42 = −19.05 pp
- GVT 1985, *Cognitive Psychology*: "a powerful and widely shared cognitive illusion" | Verified | GVT 17(3):295–314, quoted in M&S 2018 fn. 8
- 26 Cornell players, up to 100 shots each, from a distance where they hit about 50% | Verified | M&S §3.1 and Table 2 (facts.md 15)
- Random shooter, n = 100, k = 3: 46% / 54% | Verified | exact DP in `check_numbers.py` (0.4603 / 0.5397); M&S Fig. 1
- M&S 2018: the gap for a random shooter is about −8 points | Verified | M&S §3.2, "-8 percentage points" (Wharton PDF, web search this round)
- Longer records shrink the bias (−0.71 at 1,000 shots); longer streaks grow it (−1.01, −3.14, −7.94) | Verified | DP output; M&S abstract
- Cornell 49% after 3 hits vs 45% after 3 misses, so +4; "vs 0: p = .49" | Verified | M&S §3.1
- Measured from −8, +4 is +12 points | Verified | arithmetic; M&S §3.2 states +12
- The gym vs game caveat ("no defenders") | Verified | M&S §3.1 and fn. 22
- Citations: Gilovich et al., 1985 · Cognitive Psychology; Miller & Sanjurjo, 2018 · Econometrica | Verified | Econometrica 86(6):2019–2047

MECHANICS: runtime 3:26.6 · wpm 149 (speech time) · max silence 2.17 s (planned prediction hold) · max static 3.37 s · −14.0 LUFS / −2.1 dBTP · leading 0.00 s / trailing 1.74 s · WER 0.7%

WHAT I SAW, BEAT BY BEAT (craft lens)

Cold open, 0:00–0:14:
- The first frame is the object: four coins flip in.
- At 0:05 blue arcs and rings show exactly which flips are checked, and 1/2 is built from a yellow numerator and a blue denominator.
- At 0:09 the 16-run ghost deals in and collapses to "?". At 0:13 the three answers sit on the axis where their values are.
- This is a textbook prediction setup, and the question lands at 0:12.8.

Stakes and test, 0:14–0:37:
- "= 1/2" becomes "the obvious guess" with the dashed line.
- On "basketball shots" (0:23) H/T morphs into hit/miss, and the axis title changes with it. That is semantic, not decorative.
- The GVT citation is held from 0:19 to 0:33, well over 3 s.
- The "→ hot" arrow at 0:29 defines the direction once.

Calibrate and fail, 0:37–1:05:
- The big row shrinks into its slot in the 4×4 table (0:39), so the object persists.
- HHHT is worked slowly at 0:43–0:45. TTTH and TTTT are boxed and dimmed with "–" (0:47–0:51).
- The dots run the corridor to their stacks (0:52–0:54), and the live marker counts down to 17/42 = 40.5% (0:55–0:57).
- The red "cold −9.5 points" arrow lands on "cold".
- This is the best stretch of the cut. kf_15 is a frame you could teach from.

Insight, 1:05–1:52:
- The pooled strip, 12/24 and Σhᵢ/Σnᵢ are built from the table's numerators and denominators.
- The same tiles regroup into 14 equal votes. "Here, three heads share a single vote" boxes HHHH (1:25). "This lone tails" boxes HTTT by 1:27.5, 0.4 s after "lone".
- At 1:31 the heads rows are boxed in yellow with "12 heads · 8 rows". At 1:35 the tails rows are boxed in grey.
- At 1:37–1:39 the yellow slices pack exactly onto the blue 40.5% marker. 5⅔ travels to the numerator, the outlines become 14, and = 17/42 completes.
- At 1:47–1:49 the outlines become 1/14 and Σ, and both formulas stand one above the other.
- This is a genuine "the picture is the proof" sequence.

Mirror, 1:53–2:09:
- A copy drops into a second lane, is recoloured, and turns a half-turn about the dashed line (1:57–1:59). It lands at 25/42, and the red −19 arrow joins the two cursors.
- Clean, memorable and meaningful.

Payoff, 2:09–3:10:
- The lanes are relabelled "after 3 hits / after 3 misses" with ●●● and ○○○ conditions. The cursors move 50 → 46 and 50 → 54 on the words.
- The gap slides onto the zero line and the axis zooms ×5 with tick handover (2:37–2:40). The overlap of old and new labels at 2:38.6 is brief and both are labelled, so it is acceptable.
- The "1,000 shots" ghost (2:41) and the ●● → ●●● streak ghost (2:44) follow.
- The Cornell values come in, 49 − 45 = +4 on a purple marker, then "vs 0: p = .49" and the +12 brace (3:03). "no defenders" appears on "in a gym".

Landing, 3:10–3:26:
- The payoff axis drops back into the cold-open share axis, and HHTH returns.
- The 16-run ghost returns, and its rows fly into (1/14) Σ hᵢ/nᵢ (3:15.8). "= 17/42" lands on the marker, and the row becomes hit/miss.
- A blue dot appears on the half line, then the "hot" arrow (3:25). The ending re-sees the first frame exactly.

Every round-8 craft fix is in and working:
- The cursors no longer slide to 42/50.
- "Crowded heads split their votes" is cut.
- The landing rows are staggered on arcs.
- "Cornell" is printed once.
- The axis is never unlabelled mid-zoom.

DEDUCTIONS (evidence)

Visual 8.5. Three minor defects, against an anchor of "nothing to remove" for 9:
- (a) 2:45.8–2:50.5: the column head turns purple "Cornell" while the values under it are still the random shooter's 46% and 54%, dimmed (kf_34 at 2:47.2; h_2_49_5 at 2:49.5 shows "Cornell / 49% / … / 54%"). For up to 4.7 s the misses row is labelled as Cornell data but shows the random baseline.
- (b) 2:10.5–2:20.5: both blue cursors sit exactly on 50%, so they cover the dashed "obvious guess" line. Only a 10 px stub shows between the lower lane and the axis (kf_31; h_2_19_4). On "from where they'd hit about half" (2:19.2) the dashed line's pulse is therefore invisible. The reference the narration points at is hidden behind a placeholder cursor whose value is "?".
- (c) 1:16–1:36: "1 vote per row" and the dimmed blue "40.5%" sit on one baseline about 0.25 units apart (kf_19, kf_23). At a glance they read as one phrase, "1 vote per row 40.5%". The script says the tag is meant to name the strip, not the readout.

Motion 8.5:
- (a) 1:06.0–1:08.4: the pour sends 24 small discs at once through the gaps and channels of the table (frame 1:06.6, 20+ discs in flight over the dimmed rows). Each origin is honest, but the viewer cannot track any one of them. It reads as particles rather than as "these flips become these tiles".
- (b) The 2:19 pulse of the dashed line (Visual b) is a motion whose meaning cannot be seen.
- (c) The 46 → 49 and 54 → 45 swaps lag the head change by 1.5 s and 4.7 s (Visual a).
- Everything else carries meaning: the persistent table, the regroup and resize, the pack onto the marker, the mirror half-turn, the zoom with tick handover, and the landing return.

Hook 9: commitment at 0:12.8 (the anchor says 0:12). The first frame is the object and the ending re-sees it exactly. 10 would need the stakes ("the hot hand was called an illusion") inside the first frame.
Clarity 9: concrete-first, every number checks, assumptions are stated ("no defenders", "up to 100 shots", "about half"). 46/54 is asserted from M&S rather than shown, but it is cited and labelled "random".
Audio 9: 149 wpm, LUFS on target, every deictic lands (for example "lone" at 1:27.08 → box at 1:27.5), and the pauses follow beats. The only transcription difference is "nine and a half" heard as "9.5", which is not a mispronunciation.
Concision 9: 473 words. Each repeat of "17 out of 42" (0:55, 1:42, 3:14) is a deliberate callback. I could not cut a sentence without losing a step.
Originality 9: the vote strip packing onto the 40.5% marker and the mirror half-turn are images a viewer would remember and share.

FIXES (highest impact first):
1. [2:45.8–2:50.5][Visual/Clarity] The "Cornell" head sits over the random shooter's 46% and 54% (kf_34). On "The Cornell players" (2:45.8), in the same move that turns "random" into "Cornell", replace both values with purple "?" (as the lanes did at 2:11). Then write 49% on "forty nine" (2:47.3) and 45% on "forty five" (2:50.5). The column then never shows a number under the wrong head. Visual +0.5.
2. [2:10.5–2:20.5][Visual/Motion] The blue placeholder cursors cover the dashed 50% line, so the "about half" pulse at 2:19.2 is invisible (kf_31). Keep the cursors off the lanes until "For a random shooter" (2:24.5), and grow them up from 50% at that word. If they must stay, draw them at 40% opacity and z-index the dashed line above them. Then on "about half" pulse the dashed line (stroke 4 → 8 → 4 over 0.8 s) with its 50% tick, so the line the narration names is the brightest thing on screen. Visual and Motion, each about +0.25.
3. [1:06.0–1:08.4][Motion] 24 discs in flight at once read as particles (frame 1:06.6). Pour by row group instead. Run the 4 columns of cards one after another (lag ≈ 0.35 s per column, 0.5 s each). Dim the other columns to 30% while a column pours, so at most 6–7 discs are in flight and the eye can follow "this card → these tiles". Keep the total under 2.4 s by shortening each route (drop the corridor leg and go straight down the nearest channel). Motion +0.25.
4. [1:16–1:36][Visual] "1 vote per row" and the dimmed "40.5%" read as one phrase (kf_19, kf_23). Move "1 vote per row" to the strip's left end below the strip (y = strip bottom − 0.35, left-aligned with the strip at x ≈ −5.95). Or keep it above and push the 40.5% readout right of the blue marker (next_to marker, RIGHT, buff 0.15) for this beat only, so they are ≥ 0.8 units apart.
5. [2:41–2:45][Visual, nitpick] The "1,000 shots" ghost tick (height ≈ 0.45) and the ●● streak ghost with its 0.05-radius dots are the smallest marks on screen while they carry two whole sentences (kf_33; frame 2:44.0). Raise the ghost ticks to about 70% of the −8 marker's height at 50% opacity, and the streak dots to radius 0.07, so the "shrink/grow" motion reads at phone size.

REACHES 9 IF ALL FIXED: yes. Fixes 1–2 lift Visual to 9, and fixes 2–3 lift Motion to 9, which makes the weighted 9.0 with no cap in play. Nothing structural is wrong: the hook, the failure beat, the one-picture insight, the cited payoff and the landing that re-sees the first frame are all in place. What remains is local label sequencing and one crowded transition.
KEEP:
- 1:37–1:45: the yellow third-of-a-vote slices pack exactly onto the blue 40.5% marker, then 5⅔/14 = 17/42 and (1/14) Σ hᵢ/nᵢ are built from the strip. This is the episode's proof.
- 1:53–2:09: the half-turn mirror of the vote strip about the dashed line into 25/42 and the −19 arrow.
- 3:10–3:26: the landing returns to the cold-open row and axis, answers its question with 17/42 on the same image, and ends on the blue "hot" arrow.
