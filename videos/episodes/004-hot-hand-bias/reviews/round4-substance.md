# Episode 004: Round 4 review (substance: science and story editor)

**Evidence.** `review/metrics.json` (00:31) is newer than `final.mp4` (00:29), so I used the existing pack in `review/` and did not generate a new one. I read:

- report.md, all 11 contact sheets, transcript.txt, narration_diff.txt, narration.txt, script.md, facts.md and narration_text.py (for the TTS lexicon).
- 11 full-resolution keyframes: 0:08.8, 0:21.0, 1:03.7, 1:38.7, 1:52.4, 2:21.4, 2:33.6, 2:39.3, 2:56.7 and 3:15.1, plus the sheet frames at full size.
- Frames I extracted with ffmpeg into my scratchpad:
  - a 0.5 s strip of the formula coda, 1:43.5–1:51.0;
  - a 0.2–0.3 s strip of 1:44.4–1:47.0;
  - the end hold, 3:13.4–3:15.0.

**Independent checks.**
- **Enumeration.** I wrote my own enumeration of all 16 four-flip sequences, separate from `check_numbers.py`. Results:
  - 14 rows are scored, and the scores are 0 ×6, ½ ×4, ⅔ ×1 and 1 ×3. Their mean is 17/42 = 0.4048.
  - Pooled, there are 12 H out of 24 checked flips.
  - 8 rows contain a checked H and 11 rows contain a checked T.
  - The after-tails mean is 25/42, so the gap is −4/21 = −19.05 points. The per-row mean of the difference is −1/3, and the episode does not show it.
- **Simulation.** I ran my own 200,000 simulated 100-shot records at p = .5:
  - after 3 hits: 46.07%;
  - after 3 misses: 53.98%;
  - difference of the averages: −7.91 points;
  - per-record mean difference: −7.91 points.
- **Geometry.** I measured positions on the keyframes:
  - The 40.5% marker sits at 844 px, and 17/42 of the 352–1567 px axis is 844 px.
  - The −8 marker sits at 339 px. At 54 px per point from 0 at 770 px, −8 is 338 px.
  - The +4 marker sits at 986 px, and +4 is 986 px.
  - The 1,000-shot ghost sits at 733 px, which is −0.69 points. The exact value is −0.71.
- **Table and boxes.** I read every row score in the 1:03.7 table. All 14 scores and both "–" rows are correct. The 8 yellow boxes at 1:35 and the 11 white boxes at 1:39 enclose exactly the right rows.
- **Citations.** I web-verified both, reading the Wharton PDF of Miller & Sanjurjo directly. Verbatim quotes:
  - "26 players from the Cornell University Mens' (14) and Womens' (12) basketball teams … Each player shot 100 times at a distance from which the experimenters determined he/she would make around 50 [percent]".
  - "players on average hit .49 when on a hit streak, versus .45 when on a miss streak".
  - "the expected difference (and the strength of the bias) is -8 percentage points … +4 … is actually +12 percentage points higher".
  - GVT's "a powerful and widely shared cognitive illusion" (Gilovich et al. 1985, pp. 312–313, as quoted by M&S).
  - Venues and pages: *Cognitive Psychology* 17, 295–314; *Econometrica* 86(6), 2019–2047.
- **Pronunciation.** "Sanjurjo" has a lexicon override, /sænhˈʊɹhO/ (san-HOOR-ho). Whisper's "Sanjorjo" is consistent with the correct Spanish pronunciation, so I did not deduct for it.

I edited nothing except this file.

```
EPISODE: 004 — "The Hidden Bias That Hid the Hot Hand"
IDEA: Averaging each short sequence's "share of heads after a heads" gives every sequence one vote however many flips it checked, and because checked heads crowd into few sequences a fair coin reads 17/42 instead of 1/2; the same bias, mirrored after misses, makes a random shooter's after-3-hits minus after-3-misses gap about −8 points in GVT's design, so Cornell's "no hot hand" +4 is really +12.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.6 (855/100 = 8.55, half-up)   AFTER CEILING: 8.6 (lowest 8.5 + 2 = 10.5; does not bind)
CAPS: Any factual or mathematical error on screen → 6. A false equation, Σᵢ hᵢ/nᵢ = 17/42, is fully drawn and legible from about 1:44.3 to 1:45.3, before the 1/14 joins (frames 1:44.4, 1:44.7, 1:45.0). Σᵢ hᵢ/nᵢ is 17/3, not 17/42. A second false state follows from about 1:46.7 to 1:47.3: Σᵢ hᵢ = 12/24, with no denominator yet (frames 1:46.8, 1:47.0).
FINAL: 6.0   PASS: no
```

## Why this is capped

The science in the narration is clean. Every spoken number recomputes, and both citations are correct. The honest limits ("from where they'd hit about half", "a hundred shots isn't long", "evidence … in a gym, not proof it survives defenders") are all in place.

The problem is the formula coda (1:43.7–1:50.5), which is built in the wrong order:
- The 14 numerators fly into hᵢ and the 14 denominators into nᵢ, and the right-hand side "= 17/42" is already standing. The frame then reads **Σᵢ hᵢ/nᵢ = 17/42** for about 1 s. A viewer who reads it, or pauses on it, sees a false equation in the one place the episode states its result in general form.
- The 1/14 that makes the equation true arrives only on "vote per row" (about 1:45.3).
- The same thing happens on the pooled side. "Σᵢ hᵢ = 12/24" stands for about 0.5 s before Σᵢ nᵢ slides under it.

These are transient build states, but they are fully rendered, settled and legible equalities, not motion blur. BAR §3 caps "any factual or mathematical error … on screen" at 6. The fix is a reorder that costs no time (fix 1), and it removes the cap. Without the cap the episode is at 8.6. Fixes 2–6 are what lift it to 9.

## FACTS

| Claim | Verdict | Source / my check |
|---|---|---|
| 4 fair flips → 16 equally likely sequences | Verified | 2⁴ |
| HHTH: checked flips 2 (H) and 3 (T) → "one of the two is heads" | Verified | enumeration |
| HHHT "checks three flips, and two of them are heads" | Verified | enumeration (2/3 at 0:45) |
| TTTH and TTTT get no score; 14 rows are scored | Verified | enumeration; same convention as M&S 2018 (expectation conditional on ≥ 1 recorded flip) |
| Dot plot at 1:03.7: 0×6, ½×4, ⅔×1, 1×3 | Verified | enumeration; dot x-positions match |
| Average = 17/42 ≈ 40.5% | Verified | (3 + ⅔ + 2)/14 = 17/42 = 0.4048; marker at 844 px matches |
| "reads cold by nine and a half points" | Verified | 50 − 40.48 = 9.52 |
| 24 checked flips, 12 H / 12 T, "exactly half" | Verified | Σh = 12, Σn = 24 |
| "Twelve heads crowd into eight rows; twelve tails spread across eleven" | Verified | enumeration: 8 and 11; boxes at 1:35 and 1:39 match row by row |
| Heads hold 17/42 of the 14 votes | Verified | Σ hᵢ/nᵢ = 17/3; (17/3)/14 = 17/42 |
| **On screen 1:44.3–1:45.3: "Σᵢ hᵢ/nᵢ = 17/42"** | **Wrong** (transient) | Σᵢ hᵢ/nᵢ = 17/3; true only with the 1/14 that arrives at about 1:45.3 |
| **On screen 1:46.7–1:47.3: "Σᵢ hᵢ = 12/24"** | **Wrong** (transient) | Σᵢ hᵢ = 12; true only once Σᵢ nᵢ is under it (about 1:47.3) |
| After tails: 25/42; the strip is the H↔T-swapped mirror | Verified | enumeration; symmetry H↔T maps the 16 sequences onto themselves |
| "Subtract the two averages … minus nineteen points" | Verified as worded | 17/42 − 25/42 = −19.05 |
| "In 1985, a famous study ran this same check" | Verified, loosely worded | GVT's check was the hit rate after hits within each player's ~100-shot record, using 3-shot streaks for the controlled test. The payoff states this exactly (2:07–2:21), but "this same check" at 0:18 overstates the match to 4-flip rows (fix 5). |
| GVT 1985 · *Cognitive Psychology*; "a powerful and widely shared cognitive illusion" | Verified | M&S 2018 quoting GVT pp. 312–313; *Cogn. Psych.* 17(3):295–314 |
| Cornell: 26 players, about 50% distance, up to 100 shots, after 3 hits vs after 3 misses | Verified | M&S §3.1 (quoted above); Table 2 shows three players with fewer than 100 shots, so "up to" is right |
| Random shooter, n = 100, p = .5: 46% / 54% | Verified | my simulation: 46.07 / 53.98; facts.md DP: 46.03 / 53.97 |
| M&S: gap "about minus eight points" | Verified | M&S §3.2, verbatim (above) |
| Longer streaks grow the bias; longer records shrink it (ghost ticks) | Verified | M&S abstract; ghost positions measured (−0.69 vs exact −0.71 at 1,000 shots) |
| Cornell 49% after 3 hits, 45% after 3 misses; GVT read the +4 as no hot hand | Verified | M&S §3.1, verbatim (above); GVT's paired t-test was not significant |
| "Measured from minus eight, it's twelve points hot" | Verified | +4 − (−8) = +12; M&S: "+12 percentage points higher" |
| "evidence … in a gym, not proof it survives defenders in a game" | Verified | GVT's design removed defensive pressure (M&S §3.1); in-game defensive adjustment (M&S fn. 22) |
| Landing: "A 50% shooter who averages one half on this test is already running hot" | Verified | the i.i.d. p = .5 baseline is 17/42 on this test; an average of ½ is above it |
| Miller & Sanjurjo 2018 · *Econometrica* 86(6):2019–2047 | Verified | Wharton PDF / JSTOR 44955325 |

No fabricated or misattributed claim. Every empirical claim has an on-screen citation: GVT from 0:18, M&S from 2:22.

## MECHANICS

runtime 3:15.1 · 154 wpm over speech time (486 words; 149 overall) · max internal silence 2.07 s (the planned prediction hold, 0:11.7–0:13.8) · leading 0.00 s / trailing 0.89 s · max static 3.87 s (the same planned hold) · −14.0 LUFS / −2.1 dBTP · WER 0.6% · 0 banned phrases · 0 black frames · 0 layout-audit issues.

None of the mechanical caps is triggered.

## Transcript (§4 scan)

- **Banned phrases:** none.
- **"It turns out":** not used.
- **Question chains:** none. "What do you get?" at 0:10.8 is the only question.
- **Triplets, fake reveals, empty superlatives:** none.
- **Ending:** a reframe, not a recap: "One half is what a fair coin does. Seventeen out of forty two is what this test sees …" (3:00–3:14). The first two sentences of that ending restate earlier numbers, but they set up the new claim in the third sentence, so I don't count it as a recap list.
- **Hook timing:** the question lands at 0:10.8–0:11.9, with a 2.1 s hold. That is inside 0:12.
- **Deictics** (all checked against frames):

  | Line | Spoken at | Highlight on screen |
  |---|---|---|
  | "This row checks three flips" | 0:41.5 | HHHT boxed at 0:43 |
  | "This row's three heads" | 1:28.1 | HHHH boxed at 1:29 |
  | "this lone tails" | 1:31.1 | HTTT boxed at 1:33 |
  | "eight rows" | 1:35 | 8 yellow boxes |
  | "across eleven" | 1:39 | 11 white boxes |

## Story and explanation, by beat

- **Cold open (0:00–0:13).** It is concrete: one row, the procedure shown with arcs and rings, then the 16-row ghost collapsing to "?". The weakness is the ask. The viewer has to imagine averaging 16 shares in about 2 s. Many will simply say "half" without feeling they committed to anything, and "What do you get?" is an open question with no stakes attached. A three-way commitment would make the 17/42 sting harder (fix 4).
- **Stakes (0:13–0:26).** "Called the hot hand an illusion", with GVT's verbatim quote, is good legit bait. "This same check" overstates the match (fix 5).
- **Test and calibrate (0:26–0:41).** "Test the test on a shooter we know is random" is the best line in the script. The hit/miss morph out and back costs about 11 s for a definition the payoff restates anyway (fix 7).
- **Fail (0:41–1:07).** Exemplary. The worked row, the cascade, scores becoming dots, the live marker 50 → 40.5%, and "cold −9.5 points". The failure is measured.
- **Insight (1:07–1:50).** The one-vote strip is the episode's real contribution: HHHH squeezed, HTTT stretched, yellow sliding onto 40.5%. It is fresh and correct. The coda is where it slips:
  - the false intermediate equations (cap);
  - two equations in about 3 s (the first true at 1:45.3, the second at 1:47.3);
  - the 12/24 form held about 3 s before the fade at 1:50.3, against BAR's 2 s + 0.4 s per term ≈ 3.6 s;
  - the 16-row table at full brightness behind it all.

  The narration never says what hᵢ and nᵢ are. The viewer gets "That's one vote per row. Count all the flips together first" over notation they must decode alone.
- **Mirror (1:50–2:07).** "Tails crowd the same way" (1:50.1–1:51.6) plays over a frame where the strips fade and rise (1:51.0). Nothing on screen shows tails crowding at that moment. The symmetry argument (swap colours, flip about ½) is correct, but it is compressed into about 6 s and asks for a rewatch (fix 3).
- **Payoff (2:07–3:00).** Strong and honest. Axis relabelled in place, random-shooter column cited to M&S, streak and length ghosts, the purple +12 brace, the "no defenders" limit.
- **Landing (3:00–3:15).** It resolves the cold open exactly: the 16 rows collapse onto 17/42, then "hot" is drawn to the ½ dot. It holds about 1.7 s after the arrow (3:13.4–3:15.0). The entry is a dissolve, not a transform (3:00.6–3:02.4).

## Scores, with evidence

- **Hook 8.5.** Concrete question by 0:12, answered exactly at 3:05–3:15. Docked for the open-ended "What do you get?" with no commitment frame (0:10.8), and a slight sag in the 0:26–0:37 hit/miss interlude.
- **Clarity 8.5.**
  - For: all numbers and sources check out, assumptions are stated, and the one-vote picture is canonical-grade.
  - Against: the formula coda can't be read in time and doesn't decode its symbols (1:43.7–1:50.5). "Tails crowd the same way" has no visual (1:50–1:52). The error itself is handled by the cap, not double-counted here.
- **Visual 8.5.**
  - For: the semantic palette holds for the whole runtime. Frames at 1:38.7, 2:56.7 and 3:15.1 could be screenshotted to teach from.
  - Against: at 1:47–1:49 there is no single focal point (full-bright table, two strips, two equations, 12/24, "the obvious guess"). The two paired equations are typeset differently (1:48).
- **Motion 8.5.** Objects persist and transform throughout (scores → dots → marker; discs → tiles; half-turn mirror; cursor → −8 marker). Docked for the coda's two-equations-in-3 s and the payoff → landing dissolve (3:00.6–3:02.4).
- **Audio 8.5.**
  - For: 154 wpm, −14.0 LUFS, intentional pauses, and every deictic lands on its highlight.
  - Against: 1:33.9–1:49 runs about 168 wpm through the densest content in the episode.
- **Concision 8.5.** About 5% removable: the hit/miss morph back (0:35–0:37) and "A random one should match it" (0:30.3), which "test the test on a shooter we know is random" makes redundant.
- **Originality 9.** "Test the test" on a coin plus the one-vote-per-row strip is a non-obvious angle that viewers would remember. It goes beyond the standard "the 4-flip table from the NYT".

## FIXES (highest impact first)

1. **[1:43.7–1:47.8][Clarity, removes cap 6] False intermediate equations.**
   - **Row-average equation.** Build it so no false equality is ever on screen. Keep the 17/42 block that flew out of the strip parked to the right with no "=" until the left side is complete. Then:
     - on "That's", fly the numerators into hᵢ and the denominators into nᵢ to form Σᵢ hᵢ/nᵢ;
     - on "one vote per row", draw the 14 ink outlines and fly them into the 1/14;
     - only then `Write` the "=" and slide 17/42 into place.

     A better-teaching alternative is to show "Σᵢ hᵢ/nᵢ = 17/3" first (heads' share of 14 whole votes), then grow the 1/14 while 17/3 transforms into 17/42 with `TransformMatchingTex`.
   - **Pooled equation.** Restack 12/24 into a stacked fraction first. Then transform the numerator 12 → Σᵢ hᵢ and the denominator 24 → Σᵢ nᵢ in one `AnimationGroup`, and only then write "=" with a copy of 12/24. "Σᵢ hᵢ = 12/24" is then never on screen.
   - **Verify.** Step through 1:43–1:50 at 10 fps.
2. **[1:43.7–1:50.5][Motion/Clarity] Two equations in about 3 s, unread symbols.**
   - Add `[pause 0.8]` after "and you get one half."
   - Change "That's one vote per row." to "Each row's share, one vote each." Speak it while hᵢ/nᵢ indicates on the HHHT row's 2/3. This ties the symbol to the row it came from.
   - Start the pooled restack no earlier than 5 s after the first equation is complete. Hold the finished pair 3.6 s or more before the 1:50 fade.
   - Set both equations in `\displaystyle` at one font size, left-aligned with their "=" signs on one vertical (as craft r4 also asks).
3. **[1:50.1–1:52.0][Clarity] "Tails crowd the same way" has no visual.**
   - Change the narration to "After a tails, the same crowding happens to tails."
   - On "crowding", flash the 11 tails-holding row outlines from 1:39 for 0.8 s, before the table fades. Alternatively, recolour the copy (yellow ↔ grey) on this phrase instead of on "Swap heads and tails", so the swap is seen while it is named.
4. **[0:06.5–0:13.8][Hook] Make the viewer commit.**
   - Replace "What do you get?" with "More than a half, less, or exactly half?"
   - Keep it one question, not a chain. Delete "What do you get?" entirely.
   - During the 2.1 s hold, show three small grey flags on the share axis: "<½", "½", ">½".
   - At 0:57–0:59, when the marker settles at 40.5%, pulse the "<½" flag once.
5. **[0:17.6–0:21.7][Clarity] "ran this same check" overstates the match to 4-flip rows.**
   - Change it to "In nineteen eighty five, a famous study ran this kind of check on basketball shots". GVT used ~100-shot records and 3-shot streaks, which 2:07–2:21 states exactly.
   - Same word count. This removes the only loosely worded claim in the script.
6. **[1:43.7–1:50.5][Visual] No single focal point.**
   - From "That's" (1:43.7), dim the 16-row table to 30%, and dim the pooled strip to 40% until the pooled equation builds.
   - The equation pair is then the only full-brightness object right of the strips.
7. **[0:26.3–0:37.3][Concision] Hit/miss detour.**
   - Cut "A random one should match it" (0:30.3–0:32.4). "Test the test on a shooter we know is random" already says it.
   - Do the H → hit morph only on the axis title, not on the coins. That removes the coin morph back at 0:35–0:37.
   - Saves about 3 s.
8. **[3:00.3–3:02.4][Motion] The payoff dies in a dissolve.**
   - `ReplacementTransform` the points axis into the 0–100% share axis (dashed 0 → the 50% "obvious guess").
   - Transform the blue −8 random-shooter marker into the 17/42 marker.
   - Fade only the brace, +4, the column and the header. The bias then visibly becomes "what this test sees".

**REACHES 9 IF ALL FIXED: yes, narrowly.**
- Fix 1 removes the cap, which returns the episode to 8.6.
- Fixes 2, 3 and 6 lift Clarity, Motion and Visual to 9. Fix 4 lifts Hook to 9. Fix 7 lifts Concision to 9.
- With Audio at 8.5, that gives (135 + 225 + 135 + 135 + 85 + 90 + 90)/100 = 8.95, which rounds to 9.0 with no ceiling or cap.
- There is no structural problem: hook, measured failure, one-picture insight, cited payoff and reframing landing are all present. The remaining work is execution in a 7-second stretch (1:43.7–1:50.5) and two lines of narration.

**KEEP**
1. "Test the test" with the live marker 50% → 40.5% and "cold −9.5 points" (0:52–1:07). It is the measured failure.
2. The one-vote strip: HHHH's three heads squeezed into one vote, HTTT's lone tails stretched to a whole one, 8 vs 11 boxed rows, and the yellow sliding onto 40.5% (1:19–1:43).
3. The payoff chain into the purple +12 brace with the "no defenders" limit (2:21–3:00), and the landing on the rebuilt cold-open frame with 17/42 → "hot" (3:02–3:15).
