# Round 2: substance review (science and story editor)

Evidence: `review/` pack (metrics.json 15:40 is newer than final.mp4 15:37, so I reused it). I read report.md, all 13 contact sheets, the transcript and word timings, script.md, facts.md, narration.txt and CHANGELOG.md. I looked at 12 full-resolution keyframes (0:19.1, 0:39.6, 0:57.7, 1:56.5, 2:14.3, 2:33.3, 2:54.7, 3:07.8, 3:20.9, 3:40.1, 3:46.6, 3:51.5) plus frames I extracted myself at 0:51.3, 0:52.0, 3:34.6 and 3:35.6. I recomputed every number with scipy and re-ran `sim.py` and `realdata.py`. I checked the citations against Shaw & Shaw 2019 (full text, ORA Oxford) and the Clarke 1946 record (JIA 72:481, doi:10.1017/S0020268100035435).

```
EPISODE: 003 — "Randomness Looks Clumpier Than You Think"
IDEA: Pure chance leaves gaps, and the gaps force clumps, so clusters alone are not evidence of aim. The honest test compares the whole count histogram with Poisson's prediction, and a pattern that is too even is the real fingerprint of a rule.
SCORES: Hook 8.5 · Clarity 8 · Visual 8 · Motion 8.5 · Audio 8 · Concision 8 · Originality 8.5
WEIGHTED: 8.2   AFTER CEILING: 8.2  (lowest 8 + 2 = 10, not binding)
CAPS: none
FINAL: 8.2   PASS: no
```

## FACTS

| Claim | Status | Source / check |
|---|---|---|
| Each map holds 537 hits; 576 squares (24×24) | Verified | sim.py; Clarke 1946 |
| Map A = 537 independent uniform points; counts 0..5+ = 222, 223, 92, 28, 9, 2 | Verified | re-ran sim.py |
| "39 targets" (≥3 hits) on A; "0" on B | Verified | 28+9+2 = 39; B = 109, 397, 70, 0, 0, 0 |
| B's rule: no two hits closer than 4/5 square | Verified | min pair distance 0.801 |
| P(one bomb in a square) = 1/576 | Verified | uniform over 576 equal squares |
| P(empty) = (1−1/576)^537 ≈ 0.3933, "point three nine three" | Verified | 0.393332 |
| "0.3933 × 576 ≈ 227" | Verified | 226.54 → 227 |
| "four in ten", "almost a bomb per square" | Verified | 39.3 %; λ = 0.932 |
| Map A has 222 empty squares | Verified | sim.py |
| 354 squares share 537 hits, "one and a half each" | Verified | 537/354 = 1.517 |
| "so a hundred and thirty-one take two or more" | Verified (number); the "so" overstates the logic | 92+28+9+2 = 131 is counted, not derived from 1.5 |
| λ = 537/576 ≈ 0.93; 1/576 = λ/537 | Verified | 0.9323; exact identity |
| (1−λ/537)^537 ≈ e^−λ ≈ 0.3937, "almost exactly" | Verified | e^−0.9323 = 0.39365 |
| P(2) ≈ (537·536/2!)(1/576)² e^−λ | Verified (≈) | 0.1708 vs exact binomial 0.1712 |
| P(k) ≈ 537^k/k!·(1/576)^k·e^−λ = λ^k e^−λ/k! | Verified (≈), but the step 537·536 → 537² is never shown | C(537,k) ≈ 537^k/k! for small k |
| Purple bars 227, 211, 98.5, 30.6, 7.1, 1.6 | Verified | 576·Pois(0.9323) = 226.74, 211.39, 98.54, 30.62, 7.14, 1.57 |
| "chance predicts thirty-nine" / "chance: 39.3" | Verified | 30.62+7.14+1.57 = 39.33 |
| Map A χ² test p = 0.74; "pure chance misses by more, three times in four" | Verified | χ² = 2.000, df 4, p = 0.736; the reading of p is correct |
| B: "half the expected empty squares", "tower of single hits", p < 10^−50 | Verified | 109/226.7 = 0.48; 397 vs 211; χ² = 271.7, p = 1.4×10⁻⁵⁷ |
| Aim → extra empties and extra pile-ups | Verified | Clarke 1946 (excess of high and zero classes) |
| 1944: Londoners claimed the flying bombs fell in clusters; quote "…tended to be grouped in clusters." | Verified | Clarke 1946, p. 481, quoted verbatim in Shaw & Shaw 2019 ("frequent assertions were made…") |
| Precise aim would put factories at risk | Verified | Shaw & Shaw 2019: "if it could be accurately targeted at munitions factories it would also become a strategic threat" |
| "In 1946, the actuary R D Clarke **ran** this test" | Imprecise | Clarke **published** in 1946. The analysis was wartime work ("recently had occasion to make in the course of a practical investigation"; Ministry of Aircraft Production, per Shaw & Shaw). Not capped; fix 5 |
| R. D. Clarke was an actuary (Prudential) | Verified | byline, Clarke 1946; Shaw & Shaw 2019 |
| 537 hits, 576 squares, 144 km² of south London | Verified | Clarke 1946; Shaw & Shaw 2019 |
| Clarke's table: chance 227/211…; London 229, 211, 93, 35, 7, 1 | Verified | Shaw & Shaw Table 1 (226.74/229, 211.39/211, 98.54/93, 30.62/35, 7.14/7, 1.57/1) |
| "Same test: p = 0.88" | Verified | recomputed χ² = 1.171, df 4, p = 0.883; Shaw & Shaw "p=0.88" |
| Citation "R. D. Clarke, 1946 · J. Inst. Actuaries 72:481" | Verified | author, year, venue, page correct |
| Citation "Shaw & Shaw, 2019 · Significance 16(5)" | Verified | Liam P. Shaw & Luke F. Shaw, Significance 16(5):12–17, Oct 2019 |
| "real V-1 hits, 1944–45" (887 LCC sites) | Verified | Shaw & Shaw: 887 V-1s on the LCC maps; campaign June 1944 to March 1945 |
| Clarke chose an area where λ held steady | Verified | Shaw & Shaw: "selected a 144km² area where the mean number of V-1s seemed roughly constant" / "very nearly constant" |
| "north of the river, hits fell about half as densely": 1.9 vs 3.7 hits/km² | Verified (producer's own computation; consistent with Shaw & Shaw "skewed to the south") | realdata.py: 86/45 = 1.91 vs 532/144 = 3.69 (Clarke 537/144 = 3.73). The north box was chosen by the producer, and the on-screen credit ("map: Shaw & Shaw") does not say the density figure is the channel's own analysis |
| They were aimed at London, too loosely to choose a street | Verified | Shaw & Shaw: V-1s "tended to fall short of the centre of London" |
| (facts.md only, not on screen) Shaw & Shaw re-created area "χ² 6.2, p = 0.18" | Conflicts with source | Shaw & Shaw publish p = 0.70 for the same 237/189/115/28/6/1 table. My recomputation of the Pearson χ² gives 6.2 (p = 0.18), so their 0.70 must come from a different procedure. Not on screen, so no deduction; note it in facts.md |

No fabricated or wrong on-screen claims, so no cap 4 or cap 6. One imprecision (fix 5).

## MECHANICS

runtime 3:51.6 · wpm 164 (speech) / 159 overall · max internal silence 2.0 s (the planned 0:09.8 hold) · leading 0.0 s / trailing 1.74 s · max static 3.63 s (0:45.1, 1:11.6) · −14.0 LUFS / −2.0 dBTP · 0 black frames · WER 3.0 % · banned phrases 0. No mechanical caps.

Slop scan (BAR §4): no banned phrases. Patterns: no "not just X", no two questions in a row, no adjective triplets, no colon fake reveals, no recap ending. "Backwards." is a real reversal with evidence behind it, not a fake reveal. The voice is specific and numeric. Clean.

Hook: "Which one is chance?" lands at 0:08.7, followed by a 2.0 s hold. Stakes at 0:15–0:24, with Clarke's quote and citation on screen. Fail at 0:42 ("Backwards", 39 false alarms). The landing at 3:42–3:50 reverses the cold open exactly. Weak points: the title "Randomness Looks Clumpier Than You Think" gives away the cold-open answer, and tension sags through the 47 s derivation (1:37–2:24).

Deictic sync: "like this one" (0:33) gets a red outline; "these purple bars" (2:22) has the bars growing; "a tower of single hits" (2:45) shows the 397 label; "aimed at London" has the dots flag; "Clarke chose an area" has the rectangle pulse. **One miss:** "north of the river" (3:34–3:37). No river, coastline, boundary or place name is drawn on the real map at any point (3:01–3:40), so the white box sits "north" of nothing visible. One miss is below the cap threshold of ≥ 2.

## Dimension notes

- **Hook 8.5.** Everything in the 9 anchor is met: commitment by 0:10, a measured fail, and a landing that changes how the first frame looks ("If you picked map B, you picked the one with a plan"). Held below 9 by the title spoiling the puzzle and the mid-episode sag.
- **Clarity 8.** Concrete first, numbers check, and the assumption (one λ everywhere) is stated with real data. Three gaps:
  - (a) The v2 "honest detector" is a black box. "A chi-squared test scores the misfit at p = 0.74" (2:33–2:41) shows only a number. The viewer never sees what is being scored, so the fix in this build-fail-fix story is taken on trust.
  - (b) 537·536/2! becomes 537^k/k! (2:07–2:13) without saying 537·536 ≈ 537². This is the one step a viewer cannot re-derive.
  - (c) "so a hundred and thirty-one take two or more" (1:33) presents a counted number as if it followed from "one and a half each".
- **Visual 8.** The palette holds all episode (blue observed, purple chance, red flags, yellow focus), and frames are mostly single-focus. Issues:
  - The real V-1 map (3:01–3:40) is a featureless dot cloud. Dots are so large that Clarke's rectangle turns into a solid cream block, and the 576-square grid is barely visible (3:07.8, 3:20.9). No river or boundary is drawn (see deixis).
  - During the derivation (1:39–2:21) map A stays on screen with dimmed-yellow (olive) empties and faint red outlines, a 5th tonal colour competing with the equations (2:14.3).
  - A's zoom inset (0:57.7) covers the upper right of map A, and a red target outline peeks out under its bottom edge (~x 630–686 px, y 520).
  - The "rule: gap ≥ 4/5 square" tag fades in touching the fading "0 targets" (0 px gap at 0:51.3).
  - Row headers "chance"/"London" (3:11–3:40) and "simulated" are Text size 20, below the 26 minimum for primary labels.
- **Motion 8.5.** Strong persistence: dots rain in with live counters, cells fly into histogram bars (2:29), A's bars morph into B's (2:43), the λ assembly and P(2)→P(k) use TransformFromCopy, and the cold-open maps return. Some text changes are plain cross-fades, and the χ² verdict pops in as text instead of being built.
- **Audio 8.** Loudness is on target and sync is good. Pace sits at the top of the band (164 wpm on speech), which is heavy for a number-dense script. "Times five seventy-six squares" is split by the TTS into "Times 5, | 76" (2:19.2–2:21.1, with a 0.5 s stretched "five"). "Too even" is heard as "2 even" (2:51), which is ambiguous by ear. One deictic miss ("north of the river").
- **Concision 8.** 612 words with almost no padding. One slack line: "four in ten, with almost a bomb per square" (1:20) restates 0.393. The two-hits beat plus the general-k beat (1:52–2:24) runs 32 s and could be tighter. Runtime is 3:51.6, so any additions must be paid for with cuts.
- **Originality 8.5.** Clarke's V-1 study is a textbook classic (Feller 1950), but the framing is fresh: two maps, "build the detector your eye is running", the spacing-rule map as the non-random one, "too even is the fingerprint", and the real digitised hits. The closing line is memorable.

## FIXES (highest impact first)

1. **[2:31–2:42][Clarity + Motion] The χ² verdict is a black box.**
   - Problem: "A chi-squared test scores the misfit at p equals point seven four" shows only "χ² test: p = 0.74", so the v2 detector's score is never shown being computed.
   - Change: after the blue bars land, draw each bar's gap to its purple outline as a short yellow segment. Fly each segment into a running sum, "misfit = Σ gap²/chance", shown as a live DecimalNumber: 2.0 for A, 271.7 for B when the bars morph at 2:43. Then show p as the share of 1,000 simulated pure-chance maps that score worse. Either a strip of dots with the 74 % right of 2.0 shaded, or the χ²₄ curve with the tail shaded.
   - Narration: "Add up each bar's squared gap, scaled by chance's bar: map A scores 2.0. Pure-chance maps score worse three times in four."
   - Pay for the ~5 s by cutting "four in ten, with almost a bomb per square" (1:20, 2.8 s) and tightening fix 7.
2. **[2:07–2:16][Clarity] The jump from 537·536/2! to 537^k/k! is never justified.**
   - Change: as "537·536" morphs, flash "537·536 ≈ 537²" (287,832 vs 288,369, 0.2 % apart) for ≥ 2 s.
   - Narration: "five thirty-seven times five thirty-six is almost five thirty-seven squared, so for k hits: five thirty-seven to the k over k factorial…".
3. **[3:01–3:40][Visual + Audio-sync] The real map has no geography, so "north of the river" points at nothing.**
   - Change: from 3:01, draw the Thames as a thin GRAY polyline from OS grid coordinates (it runs roughly through northings 177–181 km across eastings 521–547), labelled "Thames" in GRAY at Text size ≥ 22. On "north of the river" (3:34), flag the river line, then draw the white box.
   - This also makes "south London" (3:09) readable.
4. **[3:01–3:40][Visual] The real-map dots saturate Clarke's rectangle.**
   - Problem: at 3:07.8 and 3:20.9 the 532 dots merge into a cream block and the 576-square grid is invisible.
   - Change: cut the real-map dot radius by about 40 % and dim dots outside the rectangle to 35 % opacity once it is drawn.
   - Result: the grid reads, and the 1.9 vs 3.7 hits/km² difference shows in the dots themselves.
5. **[2:57–3:03][Clarity/Fact] "In nineteen forty-six, the actuary R D Clarke ran this test" is imprecise.**
   - Clarke published in 1946; the analysis was wartime work.
   - Change the line to: "In nineteen forty-six, the actuary R D Clarke published this test, run during the war on real flying-bomb hits…" (or "In nineteen forty-six, R D Clarke revealed he had run this test…").
6. **[3:31–3:40][Clarity/Citation] The density comparison is the channel's own analysis but carries only the "map: Shaw & Shaw, 2019" credit.**
   - Change cite3 during 3:34–3:40 to "data: L. Shaw 2025 · Zenodo (our count)", or add "our analysis" under "1.9 hits/km²", so the viewer knows the number is not from the paper.
7. **[1:52–2:07][Concision] Tighten the two-hits beat.**
   - Problem: "537 bombs" tick-block, big square, ways label and P(2) take 15 s.
   - Change: drop the separate "537·536/2! ways" label and write it straight into P(2) by TransformFromCopy from the two yellow ticks. That saves ~3 s toward fix 1's budget.
8. **[1:39–2:21][Visual] Map A competes with the derivation.**
   - Problem: the dimmed-yellow empties read as a new olive hue, and the faint red outlines add clutter (2:14.3).
   - Change: dim the whole map group (dots, cells, outlines) uniformly to 30 % opacity instead of tinting only the empties. Restore it at 2:25 when the cells fly into bars.
9. **[1:33–1:37][Clarity] "so a hundred and thirty-one take two or more" implies a derivation.**
   - Change to: "one and a half each, so plenty must double up: on map A, a hundred and thirty-one".
10. **[Hook][end card 3:50 + publish title] The title spoils the cold-open question.**
    - Retitle to "Which Map Is Random?" or "The Bombs That Weren't Aimed" in the end card and episode metadata. This keeps the prediction honest for viewers who read the title first.
11. **[2:19–2:21][Audio] The TTS splits "five seventy-six".**
    - Problem: "Times five seventy-six squares" is read as "Times five, seventy-six".
    - Change: write "times five hundred and seventy-six squares".
12. **[2:51][Audio] "Too even" is heard as "two even".**
    - Change: "Spacing that even is the fingerprint of a rule", which also removes the homophone at a key line.
13. **[0:57–0:59][Visual] Zoom-inset overlaps.**
    - Problem: A's zoom inset covers map A, and a red outline peeks out under it.
    - Change: move both insets above or between the maps (outside the frames), or set z-order and opacity so no outline shows at the inset edge.
14. **[0:51][Visual] Rule tag collides with "0 targets".**
    - Problem: "rule: gap ≥ 4/5 square" touches "0 targets" mid-cross-fade.
    - Change: finish FadeOut("0 targets") before writing the rule tag (sequence instead of simultaneous).
15. **[3:11–3:40, 0:00–3:50][Visual] Labels are undersized.**
    - Change: raise the "chance"/"London" row headers and the "simulated" tags from Text 20 to ≥ 24.
16. **[facts.md] Reconcile the published figure.**
    - Note that Shaw & Shaw report p = 0.70 for their re-created area, while the episode's own Pearson χ² gives 0.18. No on-screen change.

**REACHES 9 IF ALL FIXED: yes, narrowly.** The structure is right: misconception-first hook, a measured naive detector that fails, an insight drawn from the picture, a real cited payoff, honest limits, and a landing that reverses the cold open. Fixes 1–4 lift Clarity, Visual and Motion to 9. Fixes 10–12 lift Hook and Audio. Projected weighted score is about 8.9–9.1 (Hook 9 · Clarity 9 · Visual 9 · Motion 9 · Audio 8.5 · Concision 8.5 · Originality 8.5 gives 8.9; it clears 9.0 only if Audio or Concision also reaches 9). The binding constraint is runtime: fix 1 adds time, and the episode is already at 3:51.6, so fixes 1 and 2 must be paid for with the cuts in fixes 1 and 7, keeping the master under 4:00.

**KEEP:**
1. The two-map cold open and its exact reversal at the end ("If you picked map B, you picked the one with a plan"), with A's 39 targets re-shaded red.
2. "Build the detector your eye is running" → 39 targets → "Backwards. … all thirty-nine targets are false alarms", with the red disc-overlap zoom. It is the episode's StuffMadeHere spine.
3. Clarke's real table building under the purple bars with London's blue bars growing into them, then the honest-limits beat (aimed at London but too loosely; one λ everywhere) on the real V-1 data.
