# Episode 3, review round 7 (craft critic: visual design, motion, A/V sync)

Evidence. I used the existing `review/` pack: metrics.json (20:32) is newer than final.mp4 (20:30). I read report.md, all 12 contact sheets, script.md, narration.txt, transcript.txt and transcript_words.tsv, facts.md (the claims tables) and CHANGELOG round 6. I read these keyframes at full resolution: kf_03, 07, 09, 10, 12, 15, 19, 22, 24, 26, 28, 29, 32, 35, 36 and 40. I also extracted frames with ffmpeg at 0:27.9, 0:28.5, 0:48.6, 0:52.6, 0:53.2, 1:01.2, 1:03.6, 1:04.4, 1:05.2, 1:06.0, 1:23.0, 1:33.8, 1:34.6, 1:35.4, 1:44.6, 1:45.0, 1:45.6, 2:05.8, 2:06.4, 2:23.2, 2:23.8, 2:38.4, 2:39.2, 2:40.0, 2:46.4, 2:52.0, 3:13.6, 3:24.4, 3:26.6, 3:33.4, 3:33.9 and 3:34.1. I recomputed every number with Python and scipy.

```
EPISODE: 003 — "Which Map Is Pure Chance?"
IDEA: Pure chance leaves empty squares, and the empty squares force hits to pile up elsewhere, so clusters are not evidence of aim. The honest test scores the whole count histogram against Poisson's prediction, and a pattern that is too even is the real fingerprint of a rule.
SCORES: Hook 9 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 9 · Originality 8.5
WEIGHTED: 8.6 (862.5/100)   AFTER CEILING: 8.6 (lowest 8.5 + 2 = 10.5, does not bind)
CAPS: none.
  - Every empirical claim has an on-screen citation held ≥ 3 s:
    - Clarke + Shaw & Shaw, 0:10–0:21 and 2:53–3:23
    - Falk & Konold, from 0:47.3 for about 4–5 s
    - Evans & Delaney, 3:15–3:23
    - "hits/km²: our count", 3:19–3:23
  - Mechanics are all inside limits, there are 0 banned phrases, and there is no factual error.
  - Three glyph overlaps happen only while objects are moving (1:05.2, 2:23.2, 3:33.9–3:34.1). Each lasts ≤ 0.5 s, so I score them under Motion, not cap 7. Round 6 used the same convention.
FINAL: 8.6   PASS: no
FACTS:
- 537 hits in 576 squares; Clarke 1946, J. Inst. Actuaries 72:481 | Verified | Clarke 1946; Shaw & Shaw 2019
- "...tended to be grouped in clusters." | Verified | Clarke 1946, p. 481
- Precise aim would put factories at risk | Verified (paraphrase) | Shaw & Shaw 2019, Significance 16(5)
- λ = 537/576 ≈ 0.93 | Verified (0.9323) | recomputed
- (1 − 1/576)^537 ≈ 0.3933; × 576 ≈ 227 | Verified (0.39333; 226.6) | recomputed
- e^−λ ≈ 0.3937, "almost exactly" | Verified (0.39365) | recomputed
- Map A: 222 empty, 39 with 3+ hits | Verified from counts 222/223/92/28/9/2 (576 squares, 537 hits) | facts.md, sim.py
- 354 non-empty squares; 537 − 354 = 183 "land where another already did" | Verified (Σ(count − 1) over occupied squares) | recomputed
- Poisson bars 227 / 211 / 98.5 / 30.6 / 7.1 / 1.6; "chance predicts 39" | Verified (226.74 / 211.39 / 98.54 / 30.62 / 7.14 / 1.57; 3+ = 39.33) | recomputed
- χ²_A terms 0.10 + 0.64 + 0.43 + 0.22 + 0.49 + 0.12 = 2.0 | Verified (2.000) | recomputed
- p = 0.74 ("three out of four simulated chance maps score worse") | Verified (χ²₄ tail 0.736; facts.md Monte Carlo 74.5 % of 20,000) | recomputed
- Map B: 109 empty ("half the expected"), 397 single hits ("tower"), misfit 272 | Verified (271.71; 109/227 = 0.48) | recomputed
- B's rule: no two hits closer than 4/5 of a square | Verified (radius-0.4 discs that never overlap) | facts.md, sim.py
- Clarke's table 229 / 211 / 93 / 35 / 7 / 1; χ² = 1.17, p = 0.88 | Verified (χ² 1.169; χ²₄ tail 0.883) | Clarke 1946
- The eye expects chance to look too even | Verified | Falk & Konold 1997, Psych. Review 104(2):301–318
- Aimed at central London (Tower Bridge); fell short (mean point of impact in Dulwich); lower density north | Verified per facts.md quotes | Evans & Delaney 2018, Applied Geography 99:44–53
- 1.9 vs 3.7 hits/km² | Unverifiable by me (own count of the Zenodo data; 537/144 = 3.73 checks) but honestly credited on screen | L. Shaw 2025, Zenodo
- Clarke chose an area where λ held steady | Verified ("not subject to material variation") | Clarke 1946
MECHANICS: runtime 3:34.6 · wpm 158 (speech time; 152 overall) · max silence 1.76 s (planned hold at 0:08.0) · max static 2.73 s · −14.0 LUFS / −1.9 dBTP · leading 0.00 s / trailing 1.33 s · WER 2.9 % · 0 banned phrases · 6/6 deictics on an animation
FIXES (highest impact first):
1. [3:15–3:24][Visual] The limits frame breaks the §5 word load, and its numbers sit far from their referents (kf_35 at 3:22.6).
   Problem:
   - Prose on screen: "real V-1 hits, 1944–45", "north", "Thames", "≈ Clarke's area re-created", "1.9 hits/km²" and "3.7 hits/km²" make 13 words, plus four citation lines.
   - "1.9 hits/km²" sits at x 1485–1760, about 885 px from the north box's right edge (x 600). "north" is 470 px away at the end of a long arrow.
   - "3.7 hits/km²" is about 600 px from the rectangle, so the 2:1 comparison is read across empty space.
   Change:
   - Replace "north" + arrow + "1.9 hits/km²" with one label, "north · 1.9 hits/km²", placed next_to(north_box, RIGHT, buff=0.25) at the box's vertical centre.
   - Put "3.7 hits/km²" directly under "≈ Clarke's area" (in place of "re-created", which can move under the rectangle's bottom-left corner at font 18) and shorten the yellow leader to ≤ 0.5 units.
   - On "farther", fade "real V-1 hits, 1944–45" to 35 %; it has been on screen since 2:55.
   - Each number then touches its referent and the prose count drops to ≤ 12.
2. [1:06–1:12][Visual] On "Map A has two hundred twenty-two", map A carries four layers at once (kf_10 at 1:08.4): the blue count shading, dozens of yellow empty-region outlines, faint red 3+ outlines (still at about 30 %, visible as pink squares in kf_09 and kf_10) and 537 INK dots.
   - Problem: the yellow reads as a tangled wire across the whole map, not as 222 empty squares, and the frame has no focal point.
   - Change: on "Map A", fade the blue shading and the residual red outlines to 0 and dim the dots to 60 %, so the only coloured layer is the yellow empties. Bring the blue back on "pile-ups" (1:10.2), as now. The red 3+ outlines are not needed again until 2:09.
3. [1:03.9–1:06.0][Audio/Motion] The answer is spoken before it is on screen.
   - Problem: "two hundred twenty-seven" is spoken at 64.14–65.32 s, but "227" is written only at 65.2–65.9 s. At 65.2 s the flying copy of 0.3933 sits on top of "× 576" (extracted frame 1:05.2). The prediction pause pays off on a half-built line.
   - Change: build "≈ 0.3933" and "0.3933 × 576 ≈ ?" during the guess hold (1:02.0–1:03.8). It is the method the viewer can use to make their guess. Then, on "two hundred" (64.14 s), only swap the yellow "?" for "227" (FadeTransform, 0.5 s).
4. [2:22.8–2:24.2][Motion] The χ² terms' flight into the readout renders as glyph soup.
   - Problem: at 2:23.2 the six copies rise through the original row and make two overlapping lines of "0.10 + 0.64 + …". At 2:23.8 they have shrunk to an unreadable string about 10 px tall ("0.1064822212") under "= 1.6".
   - Change: drop the flying copies. Flag each term yellow in place with LaggedStart (lag_ratio 0.25, 1.4 s total), and have the readout DecimalNumber step through the running sums 0.10 → 0.74 → 1.17 → 1.39 → 1.88 → 2.0 as each term flags. The sum is then legible as a sum.
5. [1:34.5–1:36.5][Motion] Five things move at once on "For two hits in the square, pick…" (frame 1:35.4): the P(empty) and second rows collapse to P(0) ≈ e^−λ, the 1/576 relocates, the yellow square enlarges, and 537 dots stream out of the map into the block. The eye cannot track any of them. Sequence them on the words, which already span 1:33.6–1:36.8:
   - (a) the rows collapse (0.8 s) on "For two hits";
   - (b) the square enlarges with its 1/576 (0.8 s) on "in the square";
   - (c) the dots stream into the "537 bombs" block (1.2 s) on "pick two bombs".
6. [2:25–2:31][Clarity] The null distribution arrives as a finished histogram of 20,000 misfits, and nothing shows what one entry is.
   - Change: during "Three out of four simulated chance maps", first drop three simulated-map thumbnails (the size of A's) into their bins, each tagged with its score (e.g. "1.3", "3.8", "0.9"), at 0.4 s each. Then grow the remaining bins.
   - p then reads as "the share of these maps to the right of A's marker", which a viewer could reconstruct after one watch.
7. [3:33.6–3:34.3][Motion] The end card cross-fades on top of the closing frame. "Ω Sample Space" and "Episode 3 · Which Map Is Pure Chance?" overlap map A's dots and red outlines for about 0.4 s (frames 3:33.9 and 3:34.1), so the episode's last image is a double exposure.
   - Change: FadeOut the A/B frame fully (0.35 s) before FadeIn of the card.
   - Or drop the card and hold the A/B frame with its misfit tags to the end; the title is already the cold-open question.
8. [2:47.0–2:50.5][Visual] The aimed map's yellow empty-region outline runs along all four sides of the frame (kf_28 at 2:48.4), so the frame itself turns yellow. That is the same look as the 0:45 zoom boxes and B's closing "rule" flash.
   - Change: inset the empty-region outline 0.03 units inside the frame, or set the GRAY frame's z_index above it, so only interior boundaries are yellow.
9. [3:00–3:12][Visual] The Clarke frame (kf_32 at 3:12.3) is the episode's densest. It holds the map, its title, "Thames", "≈ Clarke's area re-created", two citation lines, the formula, "χ² = 1.17, p = 0.88", the histogram, the ×5 inset and a two-row table, and the eye splits between p (top right) and the table (bottom right).
   - Change: when the table starts building (3:00), fade "Thames" and the title to 35 %.
   - Optionally, write "χ² = 1.17, p = 0.88" at the end of the Clarke row instead of beside the formula, so the eye finishes where the comparison is.
10. [0:55–0:59][Visual] Nitpick: on "this square" the fraction 1/576 sits about 910 px right of the yellow square it describes (kf_09 at 0:56.2: square x ≈ 375, fraction x ≈ 1285), with no leader.
   - Change: place P(empty) and its 1/576 at the square's height with a thin 0.4-opacity yellow leader from the square to the 1/576, or start the fraction beside the square and move it into the equation on "To stay empty".
REACHES 9 IF ALL FIXED: yes, narrowly.
  - Fixes 1, 2, 8 and 9 lift Visual to 9: every frame gets one focal point and §5 word load is met.
  - Fixes 3, 4, 5 and 7 lift Motion and Audio to 9: the answer lands on its word and no flight renders as glyph soup.
  - Fix 6 lifts Clarity to 9: the simulated null becomes derivable.
  - That gives 9·15 + 9·25 + 9·15 + 9·15 + 9·10 + 9·10 + 8.5·10 = 895, which is 8.95 and rounds to 9.0.
  - The structure needs no change. It has a commitment by 0:08 with a 1.7 s hold, a measured failure (39 false alarms where chance predicts 39.3), a derivation from one square, χ² built from the gap slivers, a simulated null, a counterexample and an aimed map on the same chart, Clarke's real table, an honest one-λ limit, and a landing on the cold-open frame carrying each map's misfit.
  - Without fixes 1–5 it stays at about 8.6.
KEEP:
- The cold-open A/B pair raining in with live counters, returned at 3:27–3:33 with "pure chance · misfit 2.0" and "spacing rule · misfit 271.7" under the same frames.
- The one-square derivation (0:52–2:02): the grid collapsing into the 576 of 1/576, 537 carried into the exponent, the 537-bomb block with two yellow picks, and every 2 turning into 3 and then k in place.
- One histogram reused for A, B, the aimed map and Clarke, with one colour code (blue observed, purple chance, red aim/flag, yellow focus/gap), the count-by-count flight from cells into bars, and the yellow gap slivers that become the χ² terms (2:07–3:12).
```

## Notes by dimension

**Hook (9).**
- The first frame is the two maps with hits raining in and counting to 537.
- "Which is chance?" ends at 0:08.2, and a GRAY "A or B?" holds through the 1.7 s silence (0:08.0–0:09.7). Most viewers pick B, which is the misconception the episode needs.
- The stakes and citation follow by 0:18 ("precise aim would put factories at risk").
- "Backwards." at 0:35.2 is a real turn. A second commitment, "Guess how many squares stay empty?" (1:00.4), keeps the viewer working through the insight.
- The stakes are answered at 3:08.8 ("London's clusters were no sign of precise aim").
- The landing puts the episode's own measurement onto the opening frame, which is the 9-anchor "ending resolves the opening".
- Remaining sag: 1:22–2:05 is 43 s of algebra with no new stakes. It is carried by the forward line "To judge London, chance must predict every bar".

**Clarity (8.5).**
- The order is concrete first: one square, 1/576, 537 misses, then 227 against 222, all before λ is named.
- Every number checks (see FACTS).
- The χ² weighting is motivated on screen: at 2:20 the 4-hit sliver, its 0.49 and chance's 7.1 bar flag together.
- The one-λ assumption is stated and drawn.
- Deductions:
  - The simulated null is shown but not built (fix 6).
  - Number load is high: 34 spoken numbers, five different ones inside 20 s from 0:40. Each does have a picture.
  - The two-hit step (1:33.6–1:52.3) packs 537, 536, 2!, (1/576)² and e^−λ into 19 s.

**Visual (8.5).**
- The palette holds for the whole episode with four hues, and colour-only flags never grow into labels.
- Charts have quantity names on both axes, with ≤ 6 ticks.
- Citations sit at y ≈ −2.9 units, above the caption zone.
- kf_22, kf_26 and kf_32 are frames people would screenshot.
- Below 9 because of:
  - the limits-frame word load and far-flung labels (fix 1);
  - the four-layer map at 1:06–1:12 (fix 2);
  - the yellow aimed-map frame (fix 8);
  - Clarke-frame density (fix 9);
  - a detached 1/576 (fix 10).
- Two of these are clear, the rest nitpicks.

**Motion (8.5).** Nearly every move encodes a relation:
- the re-rain rebuilds the same 39 targets (0:37–0:41);
- the grid collapses into the 576 of 1/576 (0:53);
- 537 is carried into the exponent (0:57);
- 2 → 3 → k swap in place (1:53–1:57);
- k-hit squares fly into bar k (2:09);
- gap slivers become terms (2:19);
- A's score becomes a marker on the null (2:27);
- the aimed red bars ride up and fade (2:51);
- Clarke's rectangle squares up into map A (3:24–3:27).

The longest static stretch is 2.7 s. Deductions are the overlapping flights and the simultaneous moves at 1:05.2 (fix 3), 2:23 (fix 4), 1:35 (fix 5) and the end-card double exposure (fix 7).

**Audio (8.5).**
- Pace is 158 wpm on speech time; loudness −14.0 LUFS and true peak −1.9 dBTP.
- All six deictics land: the red ring on "like this one" begins at 0:27.9 (word at 27.74 s), and the purple bars are growing at 2:05.8 under "these purple bars" (125.69 s).
- Planned holds land at 0:08, 1:02, 2:32 and 3:09.
- The one sync miss that matters is the 227 reveal, about 1 s late (fix 3).
- Kokoro's cadence is clean, and no technical term was mistranscribed. "Clark" for "Clarke" is the same sound.

**Concision (9).** 496 words in 3:34.6, and every beat follows the §6 template. I could not find a sentence whose removal would not lose a step. The two cuts made in round 6 ("Both are simulated. The question isn't." and "So look again.") were the slack.

**Originality (8.5).** Clarke's V-1 data is the textbook Poisson example. The fresh parts are:
- the eye-as-detector;
- the too-even map B as the real rule;
- the aimed counterexample on the same chart;
- the Evans & Delaney fall-short bias turning the honest limit into geography.

That last one is the image viewers would share. It is not yet a reframing of how the topic is taught.
