EPISODE: 004 — "The Hidden Bias That Hid the Hot Hand"
IDEA: If you score "share of heads after a heads" row by row in short sequences and average the rows, a fair coin reads below one half (17/42 for four flips). Each row gets one vote, and checked heads crowd into a few rows. The same bias puts a random shooter at −8 points on the 1985 after-3-hits minus after-3-misses test, so Cornell's +4 is really about +12.
SCORES: Hook 9 · Clarity 9 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.8 (15·9 + 25·9 + 15·8.5 + 15·8.5 + 10·8.5 + 10·8.5 + 10·9 = 875 → 8.75, rounded half-up)   AFTER CEILING: 8.8 (the lowest score is 8.5; 8.5 + 2 = 10.5, so the ceiling does not bind)
CAPS: none. I checked every cap:
- Runtime 3:32.7.
- Pace 151 wpm over speech time.
- Loudness −14.0 LUFS and −1.9 dBTP.
- Longest silence 2.17 s. This is the planned prediction hold at 0:12.1–0:14.2.
- Longest static stretch 3.6 s, at 3:08.4–3:12.0.
- 0 black frames and 0 banned phrases.
- The layout audit found 0 issues in 220 settled frames.
- Both studies are cited on screen.
- All 7 deictic words land within ±0.6 s.
- I found no settled text overlap. The overlaps I did find all happen mid-motion, so I scored them under Motion rather than as the cap-7 overlap rule.
FINAL: 8.8   PASS: no

FACTS:
- 4 flips give 16 equally likely sequences | Verified | 2^4 = 16
- In HHTH, the flips after a heads are H and T, so "one of the two is heads" (1/2) | Verified | enumeration
- HHHT checks 3 flips and 2 are heads (2/3) | Verified | enumeration; the table at 0:51.9 matches cell by cell (16 rows re-derived)
- TTTH and TTTT get no score, so 14 rows are scored | Verified | enumeration
- Dot stacks at 0:55: 0 ×6, ½ ×4, ⅔ ×1, 1 ×3 | Verified | enumeration (kf_16)
- The average is 17/42 = 40.48%, so it "reads cold by 9.5 points" | Verified | my own recomputation: (3 + ⅔ + 2)/14 = 17/42
- 24 checked flips, 12 heads and 12 tails, so the pooled share is exactly ½ | Verified | Σh = 12, Σn = 24, recomputed
- 12 heads sit in 8 rows and 12 tails in 11 rows | Verified | recomputed (8 and 11). The 11 boxed rows at 1:39 match.
- The heads hold 5⅔ of the 14 votes; 5⅔/14 = 17/42; the tails hold 8⅓ | Verified | Σhᵢ/nᵢ = 17/3
- After a tails the reading is 25/42 = 59.5%; the gap is −8/42 = −19.05 points | Verified | H↔T symmetry
- GVT 1985, *Cognitive Psychology*: "a powerful and widely shared cognitive illusion" | Verified | GVT 17(3):295–314; quote as reproduced in M&S 2018 (facts.md 13)
- 26 Cornell players, up to 100 shots each, shooting from where they would hit about half | Verified | M&S 2018 §3.1 and Table 2
- A random shooter with n = 100 and k = 3 scores 46% after 3 hits and 54% after 3 misses, a gap of about −8 points | Verified | M&S 2018 §3.2 ("−8 percentage points"); exact DP in check_numbers.py
- Cornell: 49% after 3 hits and 45% after 3 misses, read as "no hot hand" | Verified | M&S 2018 §3.1
- Measured from −8, the +4 becomes +12 points | Verified | arithmetic; M&S state +12 (their per-player correction gives +13, which is not claimed here)
- The bias grows with streak length and shrinks with record length | Verified | M&S abstract. The ghost-tick positions −1.0, −3.1, −7.9 and −0.7 (1,000 shots) match facts.md 18.
- "Evidence for a hot hand in a gym, not proof it survives defenders in a game" | Verified (stated as a limit) | M&S §3.1 and fn. 22
- Miller & Sanjurjo 2018, *Econometrica* | Verified | 86(6):2019–2047

MECHANICS: runtime 3:32.7 · wpm 151 (speech time) · max silence 2.17 s (planned prediction hold) · max static 3.6 s · −14.0 LUFS / −1.9 dBTP · leading 0.00 s, trailing 1.88 s · WER 0.8%. The only transcript misses are "a" heard as "one" at 2:22.5 and 2:51.6, and "a half" as "point five" at 1:02.

## Evidence read
- I used the `review/` pack, because metrics.json (17:38) is newer than final.mp4 (17:36).
- I read report.md, all 12 contact sheets, and the transcript, script.md and facts.md.
- Full-resolution keyframes: kf_03, 04, 07, 15, 16, 19, 21, 23, 24, 28, 32, 34 and 40.
- I extracted these frames with ffmpeg into /tmp/ep4r7:
  - single frames at 0:04.8, 0:05.2, 0:41.5, 1:00.8–1:01.6, 1:28, 1:30, 1:47, 1:51, 1:53, 2:08, 2:49.5 and 3:19.0–3:21.4
  - frame strips at 1:45–1:54 (2 fps), 2:05.5–2:08.5 (3 fps) and 2:42–2:48 (2 fps)
  - a 2× crop of the HHHH box at 1:30
- I checked font sizes in scene.py:
  - Table coin letters use Text 19 (about 24.5 px cap height). That is at the tick floor, and the fill colour also encodes H/T.
  - Row scores use MathTex 36.

## What I saw, beat by beat
- **0:00–0:14 Cold open.** The HHTH row and its arcs and rings are there from the first frame. The 1/2 is built from the coin (a yellow numerator from the heads disc, a blue denominator from the two rings). The 16-run ghost deals in on "every four-flip run" (0:09) and collapses to "?". The three answers sit on the axis where they belong, followed by a 2.2 s hold. This is a real commit-a-prediction hook by 0:12.
- **0:14–0:32 Stakes and test.** The "= 1/2" answer becomes "the obvious guess" (0:15). The GVT citation arrives on "1985" (0:19). H/T morph to hit/miss on "basketball shots" (0:23). The quote appears on "illusion" (0:25) and "→ hot" on "beats their usual rate" (0:29).
- **0:32–1:04 Fail.** The row shrinks into its slot in the 4×4 table (0:37–0:39), which is good continuity. HHHT is worked slowly (0:43–0:45), then the rest cascade. The dots fall onto the line, and the marker slides with a live readout (43.9% at 0:57, settling at 40.5%). "cold −9.5 points" lands on "nine" (1:03). This is the SMH measured failure, done right.
- **1:04–1:56 Insight.** The pooled strip lands on the dashed 50% line and Σh/Σn = 12/24 is built from the table digits (1:09–1:15). The one-vote strip regroups (1:19). HHHH is boxed with its strip segment (1:29), and so is HTTT's lone tails (1:33). The 8 and 11 rows are boxed (1:35, 1:39). Then the decisive move: the yellow slices pack left and stop exactly on the 40.5% marker (1:43–1:45, kf_23). The animation is the proof here. The formula follows: 5⅔/14 = 17/42, then (1/14)Σhᵢ/nᵢ = 17/42 under the pooled formula.
- **1:56–2:15 Mirror.** A copy of the vote strip drops into the bottom lane, recolours, and turns a half turn about the dashed line (2:01–2:04). Its heads end at 59.5%, and the red arrow gives −19 (2:13–2:15).
- **2:15–3:16 Payoff.** The strips thin to two lanes and the header builds phrase by phrase. The cursors move 50 → 46 / 54 (2:33–2:39). The share axis relabels to a difference axis with −8 (2:44–2:46). Ghost ticks show the streak and record lengths (2:47–2:53). Cornell's 49/45 replace 46/54 in the same slots (2:55–2:59), then "49 − 45 = +4" (3:03), the re-centred chart and the +12 brace (3:07–3:09), and "no defenders" (3:13).
- **3:16–3:32 Landing.** The cold-open row, axis and guess return (3:17). The ghost reappears and flies into (1/14)Σhᵢ/nᵢ = 17/42 at the blue marker (3:20–3:23). The row becomes hit/miss, a blue dot appears on ½ tagged "its rows average 1/2", and a blue arrow labelled "hot" runs from 17/42 to it (3:27–3:31). The episode holds 1.9 s and ends. The final frame re-sees the opening exactly.

## Deductions (evidence)
- **Visual, −0.5**
  - **1:19–1:27 (kf_19, 1:25.9): no single focal point.** The 64-coin table and 14 scores, the pooled 24-tile strip, the new 14-box vote strip, the 40.5% marker, "the obvious guess", the axis and Σh/Σn = 12/24 are all at full strength at once. The strip being introduced competes with five other groups. Dimming arrives only at 1:35.
  - **0:55–0:58: the spoken and on-screen numbers differ in form.** The narration says "seventeen out of forty two" while the only number on screen is "40.5%". The fraction 17/42 first appears at 1:47.
  - **Minor items:**
    - At 1:29–1:33 the HHHH highlight box's lower edge sits about 2 px from the coins' blue rings (crop of 1:30).
    - At 3:07–3:16 "Cornell" is printed twice: the purple header "Cornell, 1985" and the marker tag "Cornell".
    - At 3:19.0–3:20.6 the landing ghost appears at about 60% opacity for roughly 1 s, and the dashed guess line runs through the middle of its grid.
- **Motion, −0.5**
  - **2:43.5–2:44.6 (2 fps strip): an unshown ×10 rescale.** On the share axis the 46 → 54 gap is 8 points, about 0.36 units. In about one second it becomes a 3.6-unit "bias" arrow from 0 to −8, while the ticks relabel in place. The rescale itself is never shown, so a viewer cannot see that the long arrow is the short gap magnified.
  - **1:46.5–1:55: equation cadence breaks §5.**
    - "5⅔/14 = 17/42" is complete from about 1:47.5 and is already dimming at 1:49.5 (strip frames 6–10). That is about 2 s against the ≥3.2 s it needs.
    - Then (1/14)Σhᵢ/nᵢ = 17/42 builds between 1:50 and 1:53, and the pooled formula returns at 1:55.
    - That makes three equation events in about 8 s, against a limit of one per 5 s.
  - **2:06.6–2:07.4: muddy copy.** A translucent copy of the heads block slides across the after-tails strip's grey tiles and its cursor on its way to "25/42". For about 0.6 s it is a muddy overlap.
  - **1:50.5–1:51.5: doubled outlines.** The 14 vote outlines fly into the 1/14 stacked on top of each other, so the frame at 1:51 shows doubled outlines across the strip.
- **Audio, −0.5**
  - **1:38.7–1:56: rushed lineup.** Six sentences carrying 5⅔, 14, 17/42, "ratios" and "totals" are separated by gaps of 0.4–0.6 s. The kit's cadence line gives full stops a median of 0.35 s. The only pause of 1 s or more is the 1.2 s after "forty two" at 1:48.8.
  - **1:38.7–1:55.9: whisper merges the stretch into one unpunctuated segment.** That usually means the turns are not audible as turns.
  - Everything else (sync, pronunciation including "Sanjurjo", the 1.0–1.2 s pauses after −9.5, −19, −8 and +12) is at the 9 level.
- **Concision, −0.5**
  - Runtime has grown to 3:32.7 (round 6 was 3:24.0).
  - "Score every row the same way" (0:44.6–0:47.0) narrates a cascade the screen already shows.
  - "Longer streaks grow the bias" (2:46.6–2:48.1), with the 1- and 2-hit ghost ticks, is a side branch. Only "records shrink it, but a hundred shots isn't long" serves the argument.
  - "Seventeen out of forty two" is spoken four times (0:57, 1:47, 3:21, plus "twenty five out of forty two" at 2:07). The landing callback is deliberate; the 0:57 use is fine once the fraction is on screen (fix 2).
- I made no deduction to Clarity. Every number checks out, the assumptions are stated (fair coin, gym, no defenders), and the one-vote strip packing onto the marker is the canonical picture of this bias.

FIXES (highest impact first):
1. [1:18.4–1:35][Visual] Five groups compete with the new vote strip at 1:19–1:27 (kf_19). On "Each row gets one vote", fade these to 30%: the table rows other than the one being pointed at, the pooled strip, Σh/Σn = 12/24, and "the obvious guess". Bring each back only when it is named (HHHH and HTTT at 1:26.7 and 1:30; the pooled formula on "ratio of totals" at 1:54). This gives every frame from 1:19 to 1:35 one bright group: the vote strip plus the row being discussed.
2. [0:55.1–0:58.9][Visual/Clarity] The narration says "seventeen out of forty two" but only "40.5%" is visible. When the marker settles (about 0:57.5), write a blue `MathTex("=17/42", font_size=36)` directly under the 40.5% readout, buffered 0.15 from it, and keep it with the readout through 1:07. When the marker shortens at 1:05, the label goes with it. At 1:47 the "17/42" that slides out of 5⅔/14 then repeats a number the viewer has already seen.
3. [2:43.5–2:46][Motion] The percentage-to-difference relabel hides a ×10 zoom. First draw a thin red bracket between the 46% and 54% cursors labelled "−8" (0.6 s). Then, over 2.0 s with smooth easing, scale the bracket about the dashed line ×10 until its left end reaches −8 on the new axis. While it scales, keep the old 25/50/75% labels at 30% and cross-fade them to −5/0/+5. The bracket then becomes the "bias" arrow. Add [pause 0.6] before "puts the gap" so the move has narration room.
4. [1:46.5–1:56][Motion] The equation cadence violates the §5 hold and rate limits. Insert [pause 1.0] after "That's seventeen out of forty two." and hold 5⅔/14 = 17/42 complete for ≥3.2 s before it steps aside. Leave the pooled formula dimmed (not removed) during the Σ build, so at 1:55 it brightens rather than appearing as a third new equation. The result is one new equation per 5 s or less.
5. [1:38.7–1:56][Audio] The lineup sentences run on with gaps of 0.4–0.6 s. In narration_text.py use [pause 0.8] after "split their votes." and after "Line them up:", and [pause 1.0] after "the fourteen votes." (with fix 4's pause after "forty two"). This costs about 2 s, which fix 6 pays back.
6. [0:44.6–0:47.0, 2:46.6–2:48.1][Concision] Cut "Score every row the same way." and let the cascade run silently under a 0.8 s pause. Cut "Longer streaks grow the bias." and the 1- and 2-hit ghost ticks, and keep "Longer records shrink it, but a hundred shots isn't long." with the 3-hit ghost sliding to 1,000 shots. This saves about 4.5 s and 11 words and brings the runtime to about 3:28 even with fix 5's pauses.
7. [2:06.6–2:07.4][Motion] The translucent heads-block copy crosses the grey tiles and the cursor. Either route the copy above the lane (arc up 0.5 units, fading out before it reaches the label), or remove the copy: flash the packed heads part (0.6 s) and write "25/42" beside "after tails" on "twenty five".
8. [1:50.5–1:51.5][Motion] The 14 vote outlines stack up and double while they fly. Stagger them with `lag_ratio=0.08` along a path that leaves the strip upward first, or fade each outline to 40% stroke as it leaves, so the strip never shows doubled boxes.
9. [3:19.0–3:20.6][Visual] The landing ghost is faint and short, and the dashed line cuts through it. Fade the dashed guess line to 25% while the ghost is up, raise the ghost to 75% opacity, and hold it 1.5 s before it flies into the formula. Restore the dashed line on "A fifty percent shooter".
10. [3:07–3:16][Visual] "Cornell" appears twice. When the "Cornell" tag lands on the +4 marker (3:06.4), fade the "Cornell, 1985" header to 0 and move "1985" into the tag ("Cornell, 1985", purple, 30). That leaves one label per object.
11. [1:29–1:33][Visual] The HHHH highlight box's lower edge sits about 2 px from the blue rings. Increase that box's buff by 0.12 units (and the matching HTTT box at 1:31–1:33).

REACHES 9 IF ALL FIXED: yes, narrowly. Fixes 1, 2, 9, 10 and 11 move Visual to 9, and fixes 3, 4, 7 and 8 move Motion to 9. Fix 5 moves Audio to 9, or fix 6 moves Concision to 9. Visual and Motion at 9 plus either of those gives 15·9 + 25·9 + 15·9 + 15·9 + 10·9 + 10·8.5 + 10·9 = 895 → 9.0 (rounded half-up). All fixes together give 900 → 9.0. No structural change is needed: the hook, the measured failure, the one picture, the cited payoff with its honest limit, and the landing that re-sees the cold open are all in place. What remains is frame-level focus and transition craft.

KEEP:
- The one-vote strip whose yellow slices pack left and stop exactly on the 40.5% marker (1:43–1:45). The animation is the proof; keep it untouched.
- "Test the test": the cold-open row shrinking into the 16-row table, the live 50% → 40.5% readout, and "cold −9.5 points" (0:37–1:03). Also the half-turn mirror of the strip about the dashed line into −19 (2:01–2:15).
- The landing on the cold-open frame: the ghost flies into (1/14)Σhᵢ/nᵢ = 17/42 and a blue "hot" arrow runs to the one-half dot (3:17–3:31). The last frame changes how the first one reads.
