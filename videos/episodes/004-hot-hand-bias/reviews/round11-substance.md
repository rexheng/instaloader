EPISODE: 004 — "The Hidden Bias That Hid the Hot Hand"
IDEA: Averaging each short sequence's "share of heads after a heads" gives every sequence one vote, and checked heads crowd into fewer sequences. So a fair coin reads 17/42 instead of 1/2 on this test. The same bias puts a random 100-shot shooter at about −8 points on the 1985 after-3-hits vs after-3-misses test, which makes Cornell's "null" +4 about 12 points hot.

SCORES: Hook 9 · Clarity 9 · Visual 8.5 · Motion 9 · Audio 9 · Concision 9 · Originality 9
WEIGHTED: 8.9 (15·9 + 25·9 + 15·8.5 + 15·9 + 10·9 + 10·9 + 10·9 = 892.5 → 8.925 → 8.9)   AFTER CEILING: 8.9 (lowest 8.5 + 2 = 10.5, does not bind)
CAPS: none. I checked each one:
- Fabrication or misattribution: none. Every study claim was checked against the arXiv text of Miller & Sanjurjo.
- Sync: holds; every spoken number has its element on screen within ±1 s on the sheets.
- Debug text, glyphs, black frames: none (0 black runs, layout audit 0 issues).
- Factual or mathematical error: none. Every number was recomputed independently; see FACTS.
- Slop: 0 banned phrases. "this kind of check" (0:20) is literal ("this type of check"), not hedging filler.
- Bullet slide: none.
- Overflow, typos, LaTeX: none seen in 14 full-resolution frames.
- One idea: yes.
- Hook by 0:15: yes, the question ends at 0:12.5.
- Dead air: max silence 2.17 s, the planned prediction hold.
- Static frames: max 3.53 s.
- Runtime and pace: 3:22.8 and 151 wpm.
- Ending: none of the banned endings; it closes on a re-seen cold open.
- Loudness: −14.1 LUFS, −2.1 dBTP.
- On-screen citation: present for both studies.
FINAL: 8.9   PASS: no

FACTS:
- 4 flips, 16 equally likely rows | Verified | 2^4, enumerated
- HHTH: flips after a heads are H, T → "one of the two is heads", 1/2 | Verified | enumeration
- TTTH, TTTT have no heads before the last flip → no score; 14 scored | Verified | own enumeration (14 rows)
- HHHT checks 3 flips, 2 heads (2/3) | Verified | enumeration
- Score dots: 0 ×6, 1/2 ×4, 2/3 ×1, 1 ×3 (0:53–1:05 dot stacks) | Verified | own enumeration; the table's per-row h/n (kf 0:59.3) all check
- Mean of the 14 scores = 17/42 = 40.5% | Verified | Σ = 17/3, /14 = 17/42 = 0.40476
- "Reads cold by 9.5 points" | Verified | 50 − 40.48 = 9.52
- 24 checked flips, 12 H / 12 T, pooled = exactly 1/2 | Verified | Σh = 12, Σn = 24
- 12 heads in 8 rows, 12 tails in 11 rows (1:29–1:33 boxes) | Verified | own count; the boxed sets at 1:31 are the correct 11 rows
- HHHH: three heads share one vote; HTTT: lone tails gets a whole vote | Verified | 3/3 and 0/1
- Heads hold 5⅔ of 14 votes = 17/42; tails 8⅓ | Verified | 17/3 and 25/3
- (1/14) Σ hᵢ/nᵢ = 17/42 vs Σhᵢ/Σnᵢ = 12/24 | Verified | re-derived
- After tails: 25/42 = 59.5% by H↔T symmetry; mirror strip correct | Verified | own enumeration 25/42
- Gap 17/42 − 25/42 = −19 points | Verified | −8/42 = −19.05
- GVT 1985: 26 Cornell players, 100 shots (some fewer → "up to 100"), distance set for about 50% | Verified | M&S 2018 §3.1 ("26 players … Mens' (14) and Womens' (12)"; "shot 100 times"); "up to" per M&S Table 2 as recorded in facts.md
- GVT called the hot hand "a powerful and widely shared cognitive illusion" (on screen 0:24–0:28) | Verified | GVT p. 313, quoted in M&S 2018
- Random shooter, n = 100, p = .5, 3-streaks: after hits 46%, after misses 54%, gap about −8 | Verified | own Monte Carlo (200k records): 46.06% / 53.96%, gap −7.90; M&S: "the expected difference … is −8 percentage points"
- Ghosts: 1,000 shots → −0.7; 1/2/3-hit streaks → −1.0 / −3.1 / −7.9 | Verified | own simulation: −0.72, −1.02, −3.15, −7.90
- Cornell: 49% after 3 hits, 45% after 3 misses, +4, not significant (tag "1985 test: p = .49") | Verified | M&S: "players on average hit .49 … versus .45"; "we replicate this result (p=.49)". The p-value is M&S's replication of GVT's test; the label "1985 test" is acceptable.
- Measured from −8, +4 is 12 points hot | Verified | M&S: "+12 percentage points higher than … expected from a Bernoulli i.i.d. shooter"
- Gym, not a game: no defenders | Verified | M&S §3.1: designed for "eliminating the effects of shot selection and defensive pressure"
- Citations: Gilovich, Vallone & Tversky 1985, Cognitive Psychology 17(3):295–314; Miller & Sanjurjo 2018, Econometrica 86(6):2019–2047 | Verified | causeweb / colorado.edu copy; econometricsociety.org, doi 10.3982/ECTA14943
- Landing: a 50% shooter whose 4-shot rows average 1/2 is above the 17/42 baseline → reads hot | Verified | follows from the above

MECHANICS: runtime 3:22.8 · wpm 151 (speech time; 463 words) · max silence 2.17 s (0:12.4, the planned prediction hold) · leading 0.00 s / trailing 1.74 s · max static 3.53 s (2:58.4) · −14.1 LUFS / −2.1 dBTP · WER 0.7%. "a half" was heard as "point five", which is the same spoken value, so not a mispronunciation.

TRANSCRIPT / NARRATIVE NOTES
- The hook works. The concrete four-coin row arrives at 0:00. The procedure is shown on one row with its 1/2, and the three answers sit on the line where they belong. Then comes a 2.2 s silent hold at 0:12.4–0:14.5. The stakes (GVT's "illusion") land at 0:18–0:28.
- The failure is measured on a known-random coin: 17/42, cold by 9.5 points (0:54–1:02).
- The insight is one picture: the vote strip, with 5⅔ of 14 votes packing exactly onto the 40.5% marker at 1:33–1:37. The formulas are built from the strip (1:41–1:47).
- The mirror gives −19 (1:49–2:07). The payoff gives the −8 baseline and Cornell's +4 → +12 (2:07–3:00). The honest limit follows (3:00–3:06). The landing re-sees the cold-open row and axis with the formula and a "hot" arrow (3:07–3:22).
- No dropped or garbled lines, one question, no rhetorical chains.
- This is a strong, correct episode. What keeps it under 9 is craft, not substance.

FIXES (highest impact first):
1. [2:42.3–2:52][Visual] Word load over the §5 limit while the Cornell numbers arrive (kf 2:43.3, sheet 2:43–2:49).
   - Full-strength prose is about 16 words, plus two citations: "Cornell", "after 3 hits", "after 3 misses", "the obvious guess", "random shooter", "bias", and the axis title "after-hits − after-misses (points)". That is three competing focal points: the left marker group, the dashed line, and the right column.
   - On "The Cornell players" (2:42.3), fade "the obvious guess" to 30% over 0.5 s. It already pulses back on "no hot hand" (2:54), so return it to full there.
   - At the same moment, step "random shooter" and "bias" back to 40%, leaving the −8 numeral at full. Restore them on "Measured from minus eight" (2:56.2).
   - Result: about 9 full-strength words, with one subject, the right column filling in. Visual goes to 9 and Final to 9.0.
2. [2:07.5–2:21.5][Clarity/Visual] For about 14 s the faint coin strips carry 4-flip, 1-streak data under lane labels that say "after 3 hits" and "after 3 misses" (frames 2:11, 2:13.6, 2:14.2).
   - The bottom lane's yellow runs to 59.5% (the after-tails 25/42). It sits under "after 3 misses" on a "checked shots that are hits" axis.
   - Seconds later the true random-shooter value for that lane is 54%, so the lane is plotted data under the wrong label.
   - Keep the shrink-into-lane continuity, but fade both strips to 0 over 0.6 s in the same move that changes "heads/tails" to "3 hits/3 misses" (2:08.8). Leave only the grey tracks, which the cursors already use from 2:21.7.
   - Alternatively, keep the labels "after heads" and "after tails" until the strips leave at "For a random shooter" (2:21.7), and swap to "3 hits/3 misses" then.
3. [1:29.2–1:31.1][Clarity] The mechanism's one counting fact appears only as silent text: "12 heads · 8 rows" against "12 tails · 11 rows", that is, heads crowd into fewer rows and so get fewer votes. The narration goes from the HHHH/HTTT example straight to "the heads hold five and two thirds".
   - Use the existing 1.9 s silent gap for six words: "Twelve heads, eight rows. Twelve tails, eleven." Say them as the two box sets light up.
   - This costs about 1 s net, since the gap absorbs most of it. The viewer then hears why 5⅔ is below 7 instead of having to infer it.
4. [0:52.0][Motion] A falling score dot passes over the "0/1" label of TTHT (column 2, row 4) mid-flight (frame 0:52.0).
   - Route that column's dots 0.15 units further right of the label before the drop, or start the drop below the label's baseline.
5. [0:53–1:05][Visual] The four-dot stack at 50% sits on top of the dashed "obvious guess" line and hides its lower 0.4 units (kf 0:59.3).
   - Raise the dashed line's z-index above the dots, or nudge the 50% stack 0.06 units right, so the reference line reads continuously down to the axis.
6. [2:53–2:56][Clarity, nitpick] "1985 test: p = .49" is M&S's replication of GVT's paired test.
   - Either keep it, or make it "GVT's test: p = .49" so the viewer does not read it as a test of the 49 − 45 difference of averages. The two citations are already on screen.

REACHES 9 IF ALL FIXED: yes. Fix 1 alone lifts Visual to 9, which gives a weighted score of exactly 9.0. Fixes 2 and 3 add margin on Clarity, which could reach 9.5, since the vote strip is close to the canonical picture of this bias. Nothing structural is missing:
- the commit-first hook
- the measured failure on a known-random coin
- the one-picture insight with its formula built from it
- the cited real payoff with its honest limit
- a landing that re-sees the opening

KEEP:
- The vote strip (1:15–1:37): 14 equal votes, HHHH's three heads squeezed into one, then 5⅔ of 14 packing exactly onto the 40.5% marker. That is the episode's proof.
- "Test the test" on a known-random coin before touching basketball, and the −8 baseline re-measuring Cornell's +4 as +12 on one difference axis.
- The landing: the cold-open row and axis return with (1/14) Σ hᵢ/nᵢ = 17/42 and the "hot" arrow to a shooter whose rows average 1/2.
