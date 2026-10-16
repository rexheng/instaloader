# Episode 004: Round 2 review (substance: science and story editor)

**Evidence.** `review/metrics.json` (16:21) is newer than `final.mp4` (16:19), so I used the existing pack in `review/` and did not generate a new one. I read:

- report.md, all 11 contact sheets, transcript.txt, narration_diff.txt, script.md, facts.md, CHANGELOG.md, and the round-1 substance and round-2 craft reviews.
- 12 full-resolution keyframes: 0:03.1, 0:14.4, 0:22.3, 0:43.1, 1:08.7, 1:39.8, 1:51.4, 2:05.0, 2:21.5, 2:36.7, 2:50.0 and 3:10.8.
- Extra frames I extracted with ffmpeg: 3:06.5 (full resolution), a 5 fps strip over 1:52.6–1:54.2 (the mirror flip), and a 5 fps strip over 3:08.9–3:10.5 (the ending).

**Independent recomputation.** I did not reuse check_numbers.py.

- I enumerated all 16 four-flip sequences with exact fractions. That covers the after-heads mean, the after-tails mean, the rows holding checked heads and checked tails, the pooled counts, and the per-row mean difference.
- I ran my own Monte Carlo for n = 100, p = .5, k = 1, 2, 3 (2×10⁵ sequences, my own seeds).

**Citations.** I checked these against the Miller & Sanjurjo paper (Wharton PDF, read directly) and by web search for GVT 1985.

```
EPISODE: 004 — "The Hidden Bias That Hid the Hot Hand"
IDEA: Score the flip after each heads row by row and average, and a fair coin reads 17/42, not 1/2, because every row gets one vote and checked heads crowd into few rows; the 1985 hot-hand test (after 3 hits − after 3 misses) carries the same bias, so a random shooter reads −8, and Cornell's +4 is really +12.
SCORES: Hook 8.5 · Clarity 8 · Visual 8 · Motion 7.5 · Audio 8.5 · Concision 8.5 · Originality 8.5
WEIGHTED: 8.2 (815/100 = 8.15)   AFTER CEILING: 8.2 (lowest 7.5 + 2 = 9.5; does not bind)
CAPS: none
FINAL: 8.2   PASS: no
```

## FACTS

| Claim | Verdict | Source / my check |
|---|---|---|
| 4 flips → 16 equally likely sequences | Verified | 2⁴ |
| HHTH: checked flips 2 (H) and 3 (T) → "one of the two is heads" | Verified | enumeration |
| HHHT "checks three flips, two of them are heads" | Verified | enumeration |
| TTTH and TTTT get no score; 14 rows are scored | Verified | enumeration |
| Table scores and dots: 0×6, ½×4, ⅔×1, 1×3 (all 16 labels checked at 1:08.7) | Verified | enumeration |
| Average = 17/42 ≈ 40.5% | Verified | exact: (17/3)/14 = 17/42 = 0.40476 |
| "reads cold by 9.5 points" | Verified | 50 − 40.48 = 9.52 |
| 24 checked flips: 12 H, 12 T, "exactly half" | Verified | enumeration |
| "12 heads crowd into 8 rows, 12 tails spread across 11" | Verified | enumeration: 8 and 11; the 8 yellow boxes and 11 white boxes match at 1:37–1:39.8 |
| Heads hold 17/42 of the 14 votes | Verified | Σhᵢ/nᵢ = 17/3 |
| After a tails, the heads share averages 25/42 | Verified | enumeration over the 14 rows with a checked flip after tails |
| "Subtract the two averages … a gap of minus 19 points" | Verified as worded | 17/42 − 25/42 = −8/42 = −19.05. Caveat: the per-row (per-shooter) mean difference over the 12 rows where both are defined is **−1/3 (−33 pts)**. That is the statistic GVT computed per player. "This very comparison" (2:05) slightly overstates the identity. The two notions agree only at n = 100 (fix 9). |
| GVT 1985, *Cognitive Psychology* 17:295–314; "a powerful and widely shared cognitive illusion" | Verified | GVT pp. 312–313, quoted in M&S 2018; web search confirms the venue and pages |
| 26 Cornell players (14 men, 12 women), "up to 100 shots each" | Verified | M&S 2018 §3.1: "26 players from the Cornell University Mens' (14) and Womens' (12) basketball teams… Each player shot 100 times". "Up to" covers the three shorter records in Table 2. |
| Random shooter, n = 100, p = .5: 46% after 3 hits, 54% after 3 misses | Verified | my simulation: 46.07% / 53.98% |
| M&S 2018: gap "about minus 8 points" | Verified | M&S: "the expected difference (and the strength of the bias) is -8 percentage points"; my simulation −8.0 |
| "Longer streaks grow the bias, longer records shrink it" | Verified | M&S abstract; my simulation at n = 100: k = 1 → −1.1, k = 2 → −3.2, k = 3 → −8.0 |
| Cornell 49% after 3 hits, 45% after 3 misses; GVT read +4 as no hot hand | Verified | M&S: "players on average hit .49 when on a hit streak, versus .45 when on a miss streak … indistinguishable from zero" |
| "Measured from minus 8, it's 12 points hot" | Verified | M&S: "+4 … is actually +12 percentage points higher than the difference that would be expected from a Bernoulli i.i.d. shooter" (their per-player version is +13) |
| Miller & Sanjurjo 2018 · *Econometrica* | Verified | 86(6):2019–2047 |
| The −8 baseline assumes p ≈ .5 | **True but unstated on screen** | M&S: each player shot "at a distance from which the experimenters determined he/she would make around 50%". The video never says this, so "for a random shooter … 46 and 54" hides its assumption (fix 3). |

No wrong, fabricated or uncited numbers. Citations on screen: GVT at 0:21–0:33 and 2:07–2:55; M&S at 2:25–2:55.

## MECHANICS

| Metric | Value |
|---|---|
| Runtime | 3:10.8 |
| Pace | 152 wpm (speech time); 476 words |
| Longest internal silence | 2.07 s (the planned prediction hold, 0:13.0–0:15.1) |
| Leading / trailing silence | 0.00 s / 1.75 s |
| Longest static stretch | 3.43 s (0:19.7–0:23.2); also 3.1 s at 2:30.8–2:33.9 |
| Loudness | −14.1 LUFS / −2.2 dBTP |
| Black frames | 0 |
| WER | 1.1%. "Sanjorjo's" is an acceptable Spanish rendering. |

No mechanical caps.

## Transcript and slop scan (BAR §4)

- **Banned phrases: 0.**
- **Banned patterns.** None:
  - no "not just X";
  - no rhetorical-question chain (the one question at 0:12 stands alone and is followed by a 2.1 s hold);
  - no colon reveal and no empty superlative.
  - "That's evidence for a hot hand, not proof" is an honest hedge, not the banned construction.
- **The ending** re-sees the cold-open frame rather than listing lessons. "One half is what a fair coin does. Seventeen out of forty two is what this test sees." (2:57.8–3:03.9) is a light restatement, but it earns its place by re-reading the opening frame.
- **Hook.** The concrete procedure is on screen from frame 1. "What do you get?" lands at 0:12.0–0:13.2, held over "?" on the share axis. The stakes (GVT and the "illusion" quote) come at 0:18.9–0:27.6.

## Dimension notes (evidence)

### Hook 8.5
- **Works:**
  - The viewer commits to ½ by 0:13.
  - The landing (2:57–3:09) rebuilds HHTH with 17/42 against the dashed "the obvious guess" line, which resolves the opening exactly.
- **Holds it under 9:**
  - The stakes ("a famous study … called the hot hand an illusion") come after the commit. The 0:27.6–0:43 stretch (hit/miss morph, hot/cold arrows, "test the test") is setup, and tension only rises again with the table at 0:43.
  - The stakes are "one study" rather than what made it famous: a textbook case of human irrationality for 30 years.

### Clarity 8
- **The coin half is near-canonical:**
  - It goes from one row, to 16 rows, to a measured failure (−9.5), to pooled 12/24 against one-vote-per-row 17/42 on the same axis (1:51.4 keyframe, both formulas beside their strips).
  - Every number checks.
- **Four substance gaps:**
  1. **The mirror is invisible as a mirror.** In my 5 fps strip, the frame at ≈1:53.2 has no lower strip and the frame at ≈1:53.4 shows the after-tails strip complete. The heads↔tails reflection, which *is* the argument for 25/42, plays in under 0.4 s.
  2. **−19 (4 flips, 1-streak) becomes −8 (100 shots, 3-streak) in words only.** "Longer streaks grow the bias and longer records shrink it" plays over an unchanged gap axis (2:29–2:36, with a 3.1 s static stretch). The viewer cannot re-derive why −19 became −8.
  3. **Cornell's p ≈ .5 design is never stated.** The −8 baseline and the closing "a fifty percent shooter" both depend on it, but the header at 2:13 reads only "26 players · up to 100 shots each".
  4. **The landing picture contradicts the hedged line.** At 3:05–3:06.5 the single row HHTH's own "1/2" drops onto the axis as the blue dot at 50%, and "hot" grows from it. The narration fixed round 1's overclaim ("whose rows average one half"), but the image still says *this one 4-flip row* is hot.
- **Nit:** "The 1985 study ran this very comparison" (2:05) follows a −19 that is a difference of two averages over different row subsets. The per-shooter difference GVT computed would read −33 at n = 4. This is not an error as worded, but "this very" is stronger than the math.

### Visual 8
- The semantic palette holds for the whole runtime: yellow = heads/hits, grey = tails/misses, blue = the test's reading, red = bias, purple = Cornell, ink = assumption.
- 1:39.8 and 1:51.4 are teach-from-them frames.
- **Defects:**
  - **Payoff word load.** About 27 prose words are on screen at 2:50.0: the header, "random shooter", "bias", "+12 points", both lane labels and the two-line axis title. The limit is ≤ 12.
  - **Bottom-heavy frames.** The top 40% of the frame is empty at 2:05.0 and 2:21.5.
  - **Overlapping rings.** Check rings overlap the neighbouring coins in the table (1:08.7).

### Motion 7.5
- **Persistence is good:**
  - the scores become dots;
  - the ringed coins become 24 tiles;
  - each row is resized to one vote;
  - the yellow segments slide onto 40.5%;
  - the blue cursor is carried to the −8 marker;
  - the purple values fly into +4.
- **Defects:**
  - **The mirror flip takes under 0.4 s** (1:53.2–1:53.4). That is below the 0.4 s floor, and it is the one transform whose content is the proof.
  - **Shatter transforms read as debris.** Fraction copies sit doubled over their neighbours at 0:55.0 ("1/2" on "1/2", "0/1" smeared), and glyph fragments scatter over the table at 1:49.0.
  - **Static axis.** The gap axis is static for 3.1 s while two quantitative claims are spoken (2:30.8–2:33.9).
  - **End-card dissolve.** At ≈3:09.7 the end card cross-dissolves over the landing, so both are superimposed.

### Audio 8.5
- **On target:** 152 wpm, −14.1 LUFS / −2.2 dBTP, pauses that vary by role, and deictics that land within about 1.5 s ("this row" at 0:43, "this lone tails" at 1:33).
- **Holds it under 9:**
  - Whisper heard 1:29.9–1:40.5 as one unpunctuated 10.6 s run. This is the densest visual moment, so the breaths are too short.
  - The final image dissolves within about 0.5 s of "hot."

### Concision 8.5
- Almost every sentence carries weight.
- **Slack:**
  - "That's the row average, one vote per row" (1:44.8) restates the strip.
  - "and the argument goes on" (2:53) is vague where BAR §6 asks for a specific limit.
  - The hot/cold arrow beat (0:29–0:34) re-explains the cold open.

### Originality 8.5
- The one-vote-per-row strip is a fresh, memorable picture of Miller–Sanjurjo. Most treatments stop at "the expected proportion is below p". In this strip, HHHH's three heads are squeezed into one vote, a lone tails is stretched to a whole one, and the yellow slides exactly onto 40.5%.
- No slop.
- The topic is well covered elsewhere (NYT Upshot, Numberphile-style), and the payoff visuals (sliders, a brace) are standard.

## FIXES (highest impact first)

1. **[1:51.5–1:55.0][Clarity + Motion] The mirror flip plays in under 0.4 s, so the symmetry argument is never seen.**
   - In scene.py's `mirror` beat, overlap the table FadeOut with the end of "…you get one half".
   - Copy the after-heads strip into the lower lane *unflipped* (0.8 s).
   - Then rotate it about the dashed 50% line (`Rotate(…, PI, axis=UP, about_point=dashed_line_x)`, run_time = 1.4, smooth) while the dashed line pulses as the mirror axis. Recolour yellow↔grey at the midpoint.
   - Set an explicit run_time instead of `beat.until("tails", …)`, and finish by "after a tails" (≈1:54.5).
   - Expected gain: Clarity +0.5, Motion +0.5.

2. **[2:29–2:36][Clarity + Motion] −19 → −8 is asserted verbally over a static axis.**
   - On "Longer streaks", grow two 40%-opacity blue ghost ticks on the gap axis at −1.1 ("1 in a row") and −3.2 ("2 in a row"), and label the existing −8 marker "3 in a row". These are the n = 100 values; my simulation gives −1.07 / −3.21 / −8.03, and facts.md row 18 gives −1.0 / −3.1 / −7.9.
   - On "longer records shrink it", add a small off-scale arrow at the left edge, "4 flips: −19 ←", in red at 60%.
   - Fade all of this on "Cornell's".
   - This removes the 3.1 s static stretch and makes the viewer able to re-derive −8.

3. **[2:09–2:17][Clarity] The p ≈ .5 assumption behind −8 is unstated.**
   - Change the narration to "…twenty six Cornell players, each shooting from where they'd make about half, up to a hundred shots each."
   - Change the header to "Cornell, 1985 · 26 players · ~50% shooters".
   - Source: M&S §3.1, "at a distance from which the experimenters determined he/she would make around 50%".
   - This also sets up the closing "a fifty percent shooter".

4. **[3:04–3:08][Clarity] The landing dot is the single row's "1/2" dropped onto the axis, so the image says one 4-flip row is hot. That contradicts the hedged line.**
   - Leave HHTH's "1/2" where it is.
   - On "whose rows average one half", fade in the 0:09 ghost miniature of 16 rows under the row and collapse it into the dot at 50%. Label the dot "rows avg ½" (Text, size ≥ 26).
   - Then grow "→ hot" from the 17/42 line.

5. **[2:41–2:51][Visual] About 27 prose words on screen at 2:50.0 against a limit of 12.**
   - At 2:23, dim "· 26 players · up to 100 shots each" to 30%.
   - Shorten the axis title to one line of MathTex, "hits − misses gap (points)".
   - Dim the GVT citation to 30% once M&S is on screen.
   - Target ≤ 14 words at 2:45.

6. **[0:54.5–0:57, 1:48.5–1:50][Motion] Shatter transforms.**
   - **Scores → dots.** Scale each fraction copy into a dot *in place* (0.3 s) before it flies, with lag_ratio 0.06.
   - **Σhᵢ/Σnᵢ.** Indicate the 14 numerators, then make two grouped `TransformFromCopy` moves (numerators → Σhᵢ, denominators → Σnᵢ), 0.9 s each.

7. **[1:53–2:05, 2:07–2:45][Visual] Bottom-heavy frames.** Shift the lanes, the axis and the right-column labels up 1.0 unit in the mirror beat and 0.6 units in the payoff. Keep ≥ 0.3 units between the +12 brace and the header.

8. **[2:50–2:55][Clarity / honest limits] "and the argument goes on" names no limit.**
   - Replace it with a concrete, sourced limit, for example: "That's evidence for a hot hand in a gym, not proof it survives defenders in a game." In-game data is confounded by defensive adjustment; see M&S fn. 22–23, as facts.md row 20 already notes.
   - Verify the wording against the paper before use.

9. **[2:05–2:13][Clarity nit] "this very comparison".**
   - Say "The 1985 study ran the same comparison, shooter by shooter, on…". Or add one clause to facts.md and the script noting that −19 is a difference of averages, while the per-shooter difference at n = 4 is −33.
   - Do not put −33 on screen.

10. **[3:09.2–3:10.8][Motion + Audio] The end card dissolves over the landing (superimposed at ≈3:09.7).** Hold the landing with "→ hot" drawn until 0.6 s after the last word. Then fade it out (0.4 s), and show the ident with no overlap or drop the ident.

11. **[1:29.9–1:40.5][Audio] The densest visual stretch has no breathing room.** In narration_text.py, raise the gaps after "a whole one." and "across eleven." to 0.45 s.

12. **[0:00–0:27][Hook] Make the stakes bigger and earlier.**
    - Move "a famous study … called the hot hand an illusion" into the 0:13–0:15 hold.
    - Optionally add one sourced clause on its reach, for example the belief that it was "a massive and widespread cognitive illusion" (Kahneman 2011, as quoted in M&S §1), with an on-screen citation.

## REACHES 9 IF ALL FIXED

Yes, narrowly, and only if fixes 1–4 are executed cleanly. No structural change is needed. The commit, the naive test, the measured failure, the one picture (the vote strip), the real cited payoff and the re-seen opening all match §6.

- Fixes 1–4 take Clarity, the 25-weight dimension, to 9.
- Fixes 1, 2, 6 and 10 take Motion to about 9.
- Fixes 5 and 7 take Visual to about 9.
- Fixes 8, 11 and 12 take Concision, Audio and Hook to about 9.

That gives about 8.95–9.0 weighted. If the mirror is only slowed, without being visibly a reflection about 50%, or if −19 → −8 stays verbal, the episode will stall at about 8.5–8.6.

## KEEP

- The vote strip (1:21–1:51). HHHH's three heads share one vote, the lone tails gets a whole one, the yellow slides exactly onto 40.5%, and pooled 12/24 sits above it with both formulas beside their strips.
- The carry from the after-3-hits cursor to the −8 "random shooter" marker, the relabel in place, and the purple +12 brace from −8 to +4 (2:25–2:49). Real data is measured from the right baseline.
- The landing on the rebuilt cold-open frame (HHTH, 17/42 against "the obvious guess"), with the honest "evidence, not proof" before it.
