# Round 1 review: substance (science and story editor)

Evidence: I used the existing `review/` pack. Its metrics.json (00:31) is newer than final.mp4 (00:29), so I did not generate a new one. I read:
- report.md and all 11 contact sheets;
- 13 full-resolution keyframes: kf_03, 07, 12, 16, 19, 22, 24, 28, 32, 33, 35, 38 and 40;
- 7 extra cropped frames I extracted at 1:43.8–1:47.4 (0.6 s apart) to check the formula build;
- transcript.txt, narration_diff.txt, script.md, narration.txt, facts.md and check_numbers.py.

All the numbers were recomputed with my own code, separate from check_numbers.py:
- exact enumeration of the 16 sequences;
- a separate 100k-sequence Monte Carlo (seed 3) for the n = 100, k = 3 gap.

Citations were checked against the arXiv text of Miller & Sanjurjo (1902.01265, Econometrica 86(6):2019–2047). I extracted it with pdftotext and quoted it directly. The GVT bibliographic data was checked by web search.

```
EPISODE: 004 — "The Hidden Bias That Hid the Hot Hand"
IDEA: If you average the share of heads-after-heads row by row, a fair coin reads cold (17/42), because each
      row gets one vote and checked heads crowd into few rows. The 1985 hot-hand test has the same bias
      (−8 points for a random shooter), so Cornell's "null" +4 is really +12 hot.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8 · Motion 8.5 · Audio 8 · Concision 8 · Originality 8.5
WEIGHTED: 8.3   AFTER CEILING: 8.3  (lowest 8 → ceiling 10)
CAPS: none (see the note on 1:44.4–1:45.6 below, which comes closest to the cap-6 trigger)
FINAL: 8.3   PASS: no
```

## FACTS

| Claim | Status | Source / check |
|---|---|---|
| 4 flips → 16 equally likely sequences | Verified | 2⁴ |
| HHTH: the flips after a heads are H, T → 1/2 | Verified | enumeration |
| HHHT "checks three flips, two of them heads" → 2/3 | Verified | enumeration |
| Two rows (TTTH, TTTT) get no score; 14 are scored | Verified | enumeration |
| Score distribution 0×6, ½×4, ⅔×1, 1×3 (dots on the line at 0:59) | Verified | enumeration; the dot stacks match on screen |
| Average of the 14 scores = 17/42 ≈ 40.5% | Verified | (3 + ⅔ + 2)/14 = 17/42 = 0.40476 |
| "Reads cold by nine and a half points" | Verified | 50 − 40.48 = 9.52 |
| 24 checked flips, 12 H / 12 T → exactly half | Verified | Σh = 12, Σn = 24 |
| "12 heads crowd into eight rows; 12 tails spread across eleven" | Verified | rows with a checked H = 8, rows with a checked T = 11; the boxes at 1:35 and 1:38.7 count 8 and 11 |
| Heads hold 17/3 of 14 votes = 17/42 | Verified | Σ hᵢ/nᵢ = 17/3 |
| After a tails, the share of heads averages 25/42 | Verified | enumeration; symmetric with 17/42 |
| Gap 17/42 − 25/42 = −19 points | Verified | −4/21 = −19.05 (difference of averages, which is what is drawn) |
| Gilovich, Vallone & Tversky 1985, *Cognitive Psychology* 17:295–314; "a powerful and widely shared cognitive illusion" | Verified | M&S fn. 8 quotes GVT pp. 312–313 verbatim; bibliography confirmed via search |
| Cornell: 26 players, "up to 100 shots", taken from where they'd hit about half | Verified | M&S §3.1: "26 players … (14) and (12) … at a distance from which … around 50 percent"; Table 2 lists 90, 75 and 50 shots for three men, so "up to" is correct |
| Random shooter: 46% after 3 hits, 54% after 3 misses (n = 100) | Verified | my Monte Carlo gives 0.460 / 0.539; exact DP gives 0.4603 |
| "Miller and Sanjurjo's 2018 paper puts the gap at about minus eight points" | Verified | M&S §3.2: "the expected difference … is -8 percentage points"; my MC gives −7.87 ± 0.1 |
| Longer streaks grow the bias, longer records shrink it | Verified | M&S abstract: the bias "decreases as the sequence gets longer, but increases in streak length" |
| Ghost ticks at −1.0, −3.1, −8 (n = 100, k = 1, 2, 3) and −0.7 (n = 1000, k = 3) | Verified | exact DP in check_numbers.py, cross-checked; positions only |
| Cornell 49% after 3 hits, 45% after 3 misses; GVT took the +4 as no hot hand | Verified | M&S §3.1: ".49 … versus .45 … statistically indistinguishable from zero" |
| "Measured from minus eight, it's twelve points hot" | Verified | M&S §3.2: "+12 percentage points higher than … a Bernoulli i.i.d. shooter" |
| "Evidence for a hot hand in a gym, not proof it survives defenders" | Verified (fair framing) | GVT designed the experiment to eliminate "defensive pressure" (M&S §3.1); M&S fn. 22 |
| Miller & Sanjurjo 2018, *Econometrica* 86(6):2019–2047 | Verified | arXiv journal-ref |
| Landing: "A 50% shooter who averages one half on this test is already running hot" | Verified (relative to the 17/42 baseline) | follows from the 17/42 result |

The only mathematically false thing on screen is transient. From **1:44.4 to 1:45.6** (frames extracted at 1:44.4 and 1:45.0), the right column shows **Σᵢ hᵢ/nᵢ = 17/42**, a complete equation with its "=", before the 1/14 arrives at about 1:45.6. Σ hᵢ/nᵢ is 17/3, not 17/42.
- I am not applying cap 6, for three reasons. It is a mid-build state that lasts about 1.2 s. The narration never asserts it. It resolves on "one vote per row".
- A viewer who pauses there still sees a false equation, and 3b1b would never let that frame exist. Clarity is docked for it, and it is fix #1.

## MECHANICS

runtime 3:15.1 · 154 wpm (speech), 180 excluding all pauses · max silence 2.07 s (the planned prediction hold at 0:11.7–0:13.8) · leading 0.00 s / trailing 0.89 s · max static 3.87 s (0:10.0–0:13.8, the planned hold) · −14.0 LUFS / −2.1 dBTP · 0 black frames · layout audit 0 issues · WER 0.6% · banned phrases 0.

No cap is triggered.

## Transcript and slop audit

- **Banned phrases and patterns:** none found. I grepped narration.txt for the whole §4 list.
  - There is exactly one question ("What do you get?", 0:11), followed by a 2.1 s hold.
  - There are no "it turns out" signposts and no superlatives.
  - "That's evidence for X, not proof Y" is a precise scope limit, not the banned "not just X, it's Y" pattern.
  - The voice is specific and numeric throughout. Nothing reads as AI-generated.
- **Mispronunciation risk:** at 2:27.9 Whisper heard "Sanjurjo's" as "**Sanjorjo's**". Per §7.4 this is a likely mispronunciation. Kokoro is probably voicing an English "j" where the Spanish name is "san-HOOR-ho".
  - The two "a" → "one" substitutions (2:14.3 "a hundred", 2:39.0) are a number-normalisation artefact, not an error.
- **Hook:** the puzzle is on screen from frame 1, and the question lands at 0:10.8, before 0:15. The first 11 s, though, are three procedural instructions in a row:
  1. "After each heads, check the next flip."
  2. "Here, one of the two is heads."
  3. "Do it for all 16 sequences and average the shares."

  The basketball stakes, the reason to care, wait until 0:17–0:26. The hook works, but it asks the viewer to parse a procedure before giving them a reason to.
- **Narrative tension:** the arc is classic Stuff Made Here, and it works. The structure: the naive test (0:32) is calibrated on a known-random shooter, fails by a measured 9.5 points (1:01–1:07), and the cause is named and pictured (1:07–1:50). It then generalises via the mirror (1:50–2:07) and pays off with real data at 2:07–3:00. The landing at 3:02 re-sees the cold-open frame and answers its question on its own image. That is exactly the §6 template.
- **Midway sag:** 1:33.9–1:48 runs at about 180 wpm with no pauses and packs in four ideas:
  1. heads crowd into 8 rows;
  2. tails spread across 11;
  3. the line-up gives 17/42;
  4. the two formulas.

## Contact-sheet flipbook (sync and continuity)

- **Deictics:** every one lands within ±1 s.
  - "This row checks three flips" puts a box on HHHT at 0:43.
  - "Two rows never show a heads" boxes TTTH and TTTT at 0:49.
  - "This row's three heads" boxes HHHH at 1:29.
  - "This lone tails" boxes HTTT at 1:33.
  - "eight rows" brings 8 yellow boxes at 1:35, and "eleven" brings 11 white boxes at 1:38.7.
  - "flips over one half" starts the mirror turn at 1:55.
  - "46 and 54" moves the cursors at 2:25–2:27.
  - "plus four" puts the purple marker in place at 2:51, and "twelve points" brings the brace at 2:53.
- **Continuity:** excellent. The cold-open row shrinks into its slot in the 16-row table (0:39). Scores become dots, the dots drop onto the line, and a live % marker slides from 50% to 40.5% (0:55–0:59). The ringed coins become pooled tiles (1:11). The tiles regroup into one-vote-per-row segments (1:19–1:21), and the heads parts slide left onto the 40.5% marker (1:41). The strip is copied, recoloured and mirrored (1:51–1:59). The lanes become sliders, and the sliders become a difference axis (2:11–2:33). The cold-open frame returns at 3:03. I saw no hard cut except the payoff→landing fade at 3:01–3:03, which falls on a beat boundary.
- **Sparse stretch:** 2:11–2:19 is about 8 s of two empty grey lanes with "?" values while the header text builds word by word. It has the lowest information density of the episode, and the only new things on screen are header words.
- **Landing axis:** the axis still reads "checked flips that are heads" while the narration talks about "a 50% shooter … running hot" (3:08–3:14). The episode relabelled this axis to "checked shots that are hits" at 0:27, so the landing undoes its own coin→shooter mapping.

## Keyframes (§5 check)

- **Margins and overlaps:** clean in all 13 frames I read. The layout audit reports 0 issues, and I found none either.
- **Palette:** consistent all the way through:
  - yellow = heads/hit;
  - grey = tails/miss;
  - blue = what the test reads;
  - red = the bias;
  - purple = real Cornell data.

  The fraction colouring (yellow numerator = heads, blue denominator = checked) is a lovely touch (kf_16, kf_24).
- **Type size:**
  - The H/T glyphs inside the 16-row table coins are about 20 px cap height in kf_12 / kf_16 / kf_19. That is under the 24 px floor for ticks. The coin colour carries the same meaning, so this is minor, but it is measurable.
  - Score fractions (about 40 px), axis ticks, and citations (about 28 px, kf_07, kf_32) are all fine.
- **Word load:** within limits. At 2:55 (kf_35), eight dimmed items stay in the right column at about 25% opacity. The dimming is legal, but it is residue that adds nothing to the +12 frame.
- **Landing "hot" arrow** (kf_40): about 80 px long, so the final payoff image is the smallest mark in the frame.

## FIXES (highest impact first)

1. **[1:43.7–1:45.6][Clarity] The equation Σᵢ hᵢ/nᵢ = 17/42 sits on screen for about 1.2 s. It is false, because Σ hᵢ/nᵢ = 17/3.**
   - Change the build order in the `formula` beat of scene.py so no false equality is ever drawn:
     1. On "That's", fly the 14 numerators and denominators into Σ hᵢ/nᵢ with no "=" and no 17/42 beside it. Leave 17/42 parked where it is, to the right of the vote strip.
     2. On "vote per row", fly the 14 ink outlines into 1/14 and attach it.
     3. Only then `TransformMatchingTex` in "= 17/42", with a ≤ 1 s flash on 17/42.
   - Removes the closest call to cap 6 and lifts Clarity toward 9.
2. **[1:33.9–1:49.0][Clarity / Concision] The densest 15 s of the episode run at about 180 wpm, and they also repeat earlier lines.**
   - What repeats:
     - "That's one vote per row" restates 1:18 "each row gets one vote".
     - "Count all the flips together first, and you get one half" restates 1:09–1:16 "Gather all 24 checked flips … exactly half".
   - Replace both sentences with one line: "Average the rows: seventeen forty-seconds. Add up the flips: one half." Keep both formula builds on those two clauses.
   - Spend the time saved (about 2 s) as a 0.6 s pause after "seventeen out of forty two" (1:43), and hold the lined-up strip ≥ 2 s before the formulas start.
   - Cuts the one double explanation (Concision → 9) and gives the key image reading time.
3. **[2:27.9][Audio] "Sanjurjo's" is heard as "Sanjorjo's", a likely mispronunciation (English "j" for a Spanish "j").**
   - In narration_text.py, respell it for Kokoro as "Miller and San-hoor-ho's".
   - Re-run the review kit and confirm Whisper no longer returns "Sanjorjo".
4. **[0:00–0:12][Hook] The commit prompt arrives only after three procedural sentences, and the reason to care comes 6 s after the question.**
   - Tighten to two sentences: "Flip a coin four times and score the flips that follow a heads: here, one of two. Average that score over all sixteen sequences: above, below, or exactly one half?"
   - During the 2 s hold, draw three small tick marks on the axis (below / ½ / above, ink, ≥ 26 px) so the viewer commits to an option, not just to a number.
   - This lands the commitment by about 0:09 and frees 2 s for the stakes line.
5. **[2:11–2:19][Visual] About 8 s of empty lanes with "?" values while the header builds. "From where they'd hit about half" is said but not shown with data.**
   - On "twenty six Cornell players" (about 2:12), drop 26 small purple dots (radius 0.06) onto the 40–60% axis at each player's overall hit rate from M&S Table 2, column 3. That column spans .35–.60 with a mean of .47.
   - Let the dots cluster around the dashed 50% on "about half", then fade them to 30% before the cursors move.
   - This turns a text-only stretch into real data and makes "about half" visible. Keep the purple meaning: real Cornell data.
6. **[3:07–3:15][Visual / Clarity] The landing says "a 50% shooter … running hot" over an axis that reads "checked flips that are heads", undoing the 0:27 coin→shooter mapping. The "hot" arrow is only about 80 px.**
   - On "A fifty percent shooter" (3:08.3), morph the HHTH letters into hit/hit/miss/hit and the axis title into "checked shots that are hits", reusing the 0:26 transform.
   - Make the arrow from 17/42 to the shooter dot 1.5× thicker, with "hot" at ≥ 36 px. Extend the final hold from about 0.8 s to 1.5 s, which stays within the 2 s trailing limit.
7. **[0:39–1:50][Visual] The H/T glyphs in the 16-row table are about 20 px cap height, under the 24 px floor.**
   - Raise the table-coin letter font so the cap height is ≥ 24 px (MathTex ≥ 26 equivalent). The coin radius of 0.185 has room, because the glyph currently fills under 40% of the disc.
8. **[2:53–3:00][Visual] The right column ("random / Cornell / after 3 hits / 46% 49% / after 3 misses / 54% 45%") stays dimmed through the +12 frame and the honest-limit line.**
   - Fade it fully out when the brace lands (2:53). It has done its job, and removing it leaves one focal point: the −8 → +4 brace.
9. **[2:21.5–2:27][Clarity, nit] "The same crowding pulls those to 46 and 54" jumps from k = 1, n = 4 to k = 3, n = 100 by assertion.**
   - Optional: add 4 words, "three-hit streaks crowd harder". That foreshadows the ghost ticks at 2:34 and makes the −8 feel derived rather than imported.

**REACHES 9 IF ALL FIXED: yes.**
- With fixes 1–2, Clarity reaches 9 and Concision 9.
- Fix 3 brings Audio to 9.
- Fix 4 brings Hook to 9.
- Fixes 5–8 bring Visual to 9.

Motion and Originality are already 8.5 and would round up with the cleaner build (fix 1) and the data dots (fix 5). Even at 8.5, the other dimensions at 9 give 8.9, and Motion and Originality need to reach 9 for 9.0.

The structure is right and needs no rebuild: the misconception-first hook, the calibrate-and-fail beat with a measured −9.5, the one-picture insight, the cited payoff, and a landing that answers the cold open on its own frame.

## KEEP
- The vote strip: each row resized to one equal vote. HHHH's three heads squeeze into one vote, HTTT's lone tails stretches to a whole one, and the heads parts slide left and stop exactly on the 40.5% marker (1:19–1:43). This is the memorable, original image of the episode.
- The calibration-as-failure beat ("test the test on a shooter we know is random") with a live marker sliding from 50% to 40.5% and a red "−9.5 points" (0:32–1:07). It is the cleanest Stuff Made Here-style fail in the series so far.
- The mirror flip of the strip about 50% into 25/42, and the conversion of the two lanes into the difference axis (−8 → +4 → +12 brace). The number line carries the whole payoff without a single slide.
