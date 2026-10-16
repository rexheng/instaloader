# Round 2 review: craft critic (visual design, motion, A/V sync)

Evidence: the existing pack `review/`. Its metrics.json (14:06) is newer than final.mp4 (14:04), so I did not regenerate it. I read report.md, all 13 contact sheets, the full-resolution keyframes at 0:18.6, 0:37.1, 1:08.1, 1:24.7, 1:53.3, 2:03.2, 2:14.0, 2:35.5, 2:41.7, 3:06.6 and 3:46.4, and 33 extra frames I extracted with ffmpeg. The extracted frames are at 0:00.2, 0:13.4, 0:20.6, 0:21.4, 0:22.6, 0:23.0, 0:23.4, 0:24.0, 1:13.5, 1:16.5, 1:17.6, 1:29.2, 2:15.8, 2:16.8, 2:17.8, 2:18.6, 2:24.8, 2:37.8, 2:38.4, 2:39.2, 2:45.5, 2:57.6, 3:00.0, 3:14.6, 3:16.2, 3:17.4, 3:37.95, 3:38.6, 3:39.6, 3:41.4, 3:42.8, 3:44.0 and 3:46.0. I also read the transcript, the word timings, narration.txt, script.md, facts.md, CHANGELOG.md, round1-craft.md and the landing code in scene.py. I web-checked the Cardiff figures (BBC, 4 May 2018; Guardian, 5 May 2018) and the Gigerenzer figures (PSPI 2007 via SAGE; Frontiers 2015 secondary).

```
EPISODE: 002-base-rate-fallacy — "When a 99% Accurate Test Says You're Sick"
IDEA: A positive result shrinks the sample space to the people who tested positive; when the condition is rare that crowd is mostly false alarms, so P(sick|+) is about 9%, not the test's 99%. Bayes' theorem (and a classifier's precision) is that share written down.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8 · Originality 8
WEIGHTED: 8.4   AFTER CEILING: 8.4 (lowest 8 + 2 = 10, not binding)
CAPS: none. Transient in-motion overlaps at 0:22.6–0:23.4 ("99%" copy over its source, through the bar outline, touching "naive") and the mid-morph glyph overlap at 2:05 last ≤ 0.5 s inside transforms, consistent with round 1, so they are fixes, not cap 7. No typos, clipping, black frames or banned phrases.
FINAL: 8.4   PASS: no
FACTS:
 - 1 in 1,000, 99% sensitivity, 1% FPR → P(sick|+) = 11/122 = 9.02% ("9%") | Verified | recomputed
 - 10,000 people: 10 sick → 9.9 ≈ 10 positives; 9,990 healthy → 99.9 ≈ 100; 10/110 = 9.1% | Verified (labelled "expected counts", then shown as 9.9 / 99.9) | recomputed
 - "11 times too high" (0.99 / 0.0902 = 10.98) | Verified | recomputed
 - Half sick: 4,950 + 50 positives, 4,950/5,000 = 99% | Verified | recomputed
 - 10×0.99 / (10×0.99 + 9,990×0.01) → ÷10,000 → 0.001, 0.999 → Bayes with total-probability denominator | Verified | algebra
 - Prior sweep: 1/100 → 50.0%, 1/2 → 99.0%, 1/3 → 98% (frame 3:31) | Verified | recomputed
 - Landing flows 10 vs 100 (9.9 : 99.9) | Verified | recomputed
 - Cardiff, 2017 Champions League final: 2,470 alerts, 2,297 wrong → 173 right, 7.0% | Verified | BBC News 4 May 2018; Guardian 5 May 2018
 - "In machine learning, that share has a name: precision" | Verified (definition, TP/(TP+FP))
 - Gigerenzer et al. 2007, PSPI: 160 gynecologists, 1%/90%/9% problem, 21% chose 1 in 10 (< 25% chance), modal answer 90%, 87% after natural-frequency training | Verified | journals.sagepub.com doi:10.1111/j.1539-6053.2008.00033.x; Frontiers Psychol 2015 (10.3389/fpsyg.2015.01473) quoting "160 gynecologists … 21 to 87%"
 - Fig. 2 bars 47/13/21/19 → 6/1/87/6 | Verified (facts.md reading of Fig. 2; sums to 100; consistent with the text) | Gigerenzer et al. 2007 Fig. 2
 - "Most doctors given a problem like this got it wrong" (cold open, cited on screen 0:13–0:20) | Verified (79% of 160) | same
 - Omitted, not wrong: BBC attributes the Cardiff false matches partly to "poor quality images" and the first deployment; the video frames the 7% purely as a base-rate effect (fix 1)
MECHANICS: runtime 3:46.5 · wpm 155 (speech time; 179 excluding all pauses) · max silence 2.06 s (0:16.7, planned prediction hold) · max static 2.9 s · −14.0 LUFS / −2.1 dBTP · lead 0.00 s / trail 1.76 s · WER 2.7% · 0 banned phrases
```

## What I saw (flipbook notes)

- **0:00–0:18 cold open.** Frame 1 has both halves of the problem: the red and blue nodes with "1 in 1,000" on the left and the ghosted meter on the right (frame 0:00.2), which fixes round 1's empty right half. The arrows grow on "99%" (0:05) and "1%" (0:07), the "you" ring closes on "yours says positive" (0:11), and the meter brightens on the question. The waffle and the citation fade in on "Most doctors…" (0:13.4), and the frame holds 2.06 s after "Pick a number". The sync is clean. The commit lands at 0:15.9, about 4 s later than the 9-anchor's 0:12, and the viewer sees "21% got it right" before being asked to pick, which half-answers the puzzle (fix 9).
- **0:18–0:25 stakes.** The red arrow's "99%" lifts off and becomes the dashed "naive 99%" marker, which is semantically right. In flight it duplicates over its source (0:22.6, "99%99%"), passes *through* the meter's bar outline (0:23.0, a strike-through look) and lands touching "naive" (0:23.4, "naive99%"). That is three collisions in one second (fix 4).
- **0:25–0:43 naive build.** The diagram straightens into the counting table and the 10,000 grid fills in. The beam sweep, live counters (906 → 2,919 → 4,950) and the meter filling onto the naive marker (0:41) work as a measured check. This is excellent.
- **0:43–1:15 fail.** The recolour starts on "Now make the disease rare" (0:45 counters at 4,453 / 5,547), and "That leaves ten sick people" lands on 10 / 9,990 (0:49). Same beam: the counts tick to 10 / 100, the meter fills 9% red, and the "11× too high" brace appears on cue (1:09). On "1% of nearly everyone" (1:10.8–1:15.3) only the table's healthy row pulses (sheet 1:15). The dimmed 9,990-cell grid, which *is* "nearly everyone", is never pointed at (fix 8).
- **1:15–2:14 insight.** The negatives vanish while the 110 survivors swell into real dots (1:19). They fly into a 22×5 strip under the meter, whose two red columns sit exactly under the 9% segment (kf 1:24.7). This is the best frame in the episode and fixes round 1's "dust". The braces count 10 / 100, and the fraction is built from the brace labels (1:29.2). The table expansion runs on the spoken products (9.9 at 1:39, 99.9 at 1:45). The table dims to 30% before ÷10,000 (1:47), and the names arrive in two flagged steps (2:01–2:06). The numerator is boxed red and the denominator yellow (kf 2:14.0). Hierarchy is now clear: one bright group on the left, a dimmed reference on the right. Nitpick: the bottom-right quadrant is empty for the whole 55 s.
- **2:14–2:37 Cardiff.** The strip slides to centre and the legend swaps to "on the list / not on it". **For about 1.8 s (2:16.8–2:18.6) the meter reads "chance you're on the list 9%"**, a stale disease value under the new title, while the narration says "In a football crowd, almost nobody is on it". The picture on screen is not a crowd but the 110 *alerts*, 9% of them red. The 110 dots then cross-dissolve into a grey 26×95 raster (2:24.8), the checks turn 173 red and 2,297 blue, the meter fills to 7% over the red columns, and the title becomes "precision" (kf 2:35.5 is clean and well-built). What is missing is the move the whole episode taught: the ~170,000-person crowd shrinking to 2,470 alerts. The beat asserts the base rate instead of showing it (fix 1).
- **2:37.8–2:45 transition.** Everything fades out, and a 220 px waffle appears alone, left of centre, in an otherwise empty frame (2:38.4–2:43; kf 2:41.7). The narration says "gave a hundred and sixty of them" while the only label reads "per 100 gynecologists". This is the weakest composition in the video and the only beat change that is a fade rather than a transform (fix 2).
- **2:43–3:14 payoff.** The mammography diagram builds on the right in the opening's grammar. The dots sort into bars (2:57 green 21%, then 47 / 13 / 19 at 3:03), with values riding the bar ends and a "guessing: 25%" line. The bars then move before → after (3:09–3:13). While it waits, the waffle sits *inside* the chart's plot area at x ≈ 45–75 (frames 2:57.6, 3:00), where it reads as plotted data (fix 5). The finished chart is clean (kf 3:06.6).
- **3:14–3:45 landing.** The chart clears while the mini diagram slides to the cold-open position and morphs (3:14.6 → 3:16.2), and the "you" ring and the meter redraw (3:17.4). This is the right continuity. The arrows become flows. The prevalence sweeps 1/1,000 → 1/100 (50%, 3:25) → 1/2 (99%, onto the returning naive marker, 3:27–3:29) and back. Then come a hairline red flow labelled 10 and a fat blue flow labelled 100 (3:33–3:45). The closing chiasmus pulses "99%" (3:37.95, visible) and then the meter's "9%". The end card arrives 1.7 s after the last word. A small layout point: the "10" and "100" labels stack together in the wedge *between* the two flows (3:37–3:45), and the bottom ~28% of the frame stays empty through the most screenshot-worthy 30 s (fix 7).

## Audio / sync

Every deictic I checked lands within ±1.5 s: "this crowd" (1:25, strip), "this table" (1:32; the table's "10" pulses at 1:35), "these two" ×2 (2:01, 2:03, with the morphs and flags), "this plus sign" (3:33, the + pulses) and "along the red arrow" (3:35, "10" and the red flow pulse). Pauses now vary: 0.3 s inside thoughts and about 1.1 s after the three reveals (1:05, 1:10, 3:01). The reveals are slower, which fixes round 1's metronome. "a a" at 1:51.9 has overlapping Whisper timestamps (111.86–112.06 vs 111.90–112.06), the same artifact as round 1's "scan scan", so I made no deduction. The key insight sentence ("ruled out everyone who tested negative… a smaller sample space", 1:15.8–1:24.4) is delivered at the same clip as the bookkeeping lines, at 179 wpm within phrases. Loudness and peak are on target. Score 8.5.

## FIXES (highest impact first)

1. **[2:14–2:31][Clarity/Originality/Visual]** The Cardiff beat skips its own mechanism. "In a football crowd, almost nobody is on it" plays over the 110-alert strip, and the meter shows a stale "chance you're on the list 9%" (2:16.8–2:18.6). Change it as follows:
   - On "Swap the disease…", empty the meter to "?" in the same animation as the title morph.
   - FadeOut the strip and bring back the 100×100 grid labelled "crowd ≈ 170,000 (each cell ≈ 17 people)", with ~0 red cells.
   - On "raised 2,470 alerts", run the same yellow beam, dim the rest and collapse the lit cells into the 26×95 raster under the meter. This is the 1:15–1:23 shrink, reused.
   - Title the meter "chance you're on the list, given an alert" before it becomes "precision".
   - Add the honest limit the BBC reports, in one clause or a grey on-screen note: "…and the custody photos were poor".

   This lifts Clarity and Originality toward 9 and removes the stale-state frame.
2. **[2:37.8–2:45][Visual/Motion]** The Cardiff picture fades to an empty frame and a lone 220 px waffle sits off-centre for about 6 s (kf 2:41.7). Keep the precision meter on screen. On "Back to those gynecologists", FadeIn the waffle at its cold-open position (x ≈ +2.4, y ≈ −1.6) and move it to its payoff spot at ×1.5 scale. Draw the mammography diagram on the right *during* "In 2007…" rather than after it, so the frame never holds one small object. Relabel the waffle "per 100 of the 160 gynecologists" so the spoken "160" has a referent.
3. **[2:14–3:45][Concision]** Post-insight material runs 91 s, 40% of a 3:46 episode, against the template's ~55 s. The 21% statistic is shown twice (0:13 and 2:57), and "the scan's own hit rate" re-says the 0:22 naive rule. Make three cuts:
   - Cut "The most common answer was ninety percent: the scan's own hit rate" and instead pulse the 47% bar together with the diagram's "90%" in silence (−4 s).
   - Shorten "this version: one percent of women have breast cancer, the mammogram catches ninety percent, and wrongly flags nine percent" to "the same problem: one in a hundred, ninety percent caught, nine percent false alarms", built while spoken (−3 s).
   - Drop "Those counts came from this table:" (the table pulse already says it, −2 s).

   Target runtime ≤ 3:37.
4. **[0:22.6–0:23.6][Motion]** The flying "99%" copy overlaps its source, crosses the bar outline and lands touching "naive". Give the copy a path_arc that clears the bar's top edge by ≥ 0.3 units. Write "naive" 0.3 s *after* the label lands, with buff ≥ 0.15. Start the copy offset 0.2 units upward so frame 1 never doubles the glyph.
5. **[2:55–3:02][Visual]** The waffle waits inside the chart's plot area (x ≈ 45–75; frames 2:57.6, 3:00), where it reads as plotted data. Before the axes write, move the waffle left of the y-axis labels (x ≈ −5.6) or right of x = 100, then fly its dots into the rows.
6. **[0:00–0:17][Hook]** The commit lands at 0:15.9, after the 21% waffle has already signalled "the answer is surprising". Reorder to: "…what's the chance you're sick? Pick a number. [pause 1.5] Most doctors given a problem like this got it wrong." The waffle fades in on "Most doctors", so the viewer commits by ~0:13 and the baseline arrives as a reveal, not a hint.
7. **[3:15–3:45][Visual]** In the landing, the "10" and "100" flow labels stack in the wedge between the flows, and the bottom ~28% of the frame is empty for 30 s. Shift the diagram+meter group down 0.6 units. Put "10" *above* the red hairline at its midpoint and "100" *below* the blue band at its midpoint, both at font_size ≥ 44.
8. **[1:10.8–1:15.3][Motion/Clarity]** On "one percent of nearly everyone", only the table row pulses. Raise the dimmed 9,990-cell grid from 25% to 60% opacity and back over 1 s on "nearly everyone", together with the 100 blue positives, so the deictic points at the crowd it names.
9. **[1:15.8–1:24.4][Audio]** The insight sentence plays at the same clip as the bookkeeping. Render "Your positive result ruled out everyone who tested negative" and "What's left is a smaller sample space" at speed 0.80, with a 0.6 s pause between them, timed to the negatives vanishing.
10. **[2:24.8][Motion]** The 110 dots cross-dissolve into the 2,470-cell raster with no correspondence. If fix 1 is done this disappears. If not, FadeOut the strip dots first (0.4 s), then grow the raster from the left edge of the outline.

## REACHES 9 IF ALL FIXED: yes, narrowly

No structural change is needed. The episode now has the misconception hook, a measured build-and-fail, one picture that becomes the formula, a real DS consequence and a landing that re-sees frame 1. What holds it at 8.4 is the back 40%:
- the Cardiff beat states the base rate rather than showing the crowd shrink (Clarity, Originality);
- one dead composition at 2:38–2:45 (Visual, Motion);
- about 15 s of slack in the payoff (Concision).

Fixes 1–3 together move Clarity, Visual, Motion and Concision to about 9. Originality reaches 9 only through fix 1, because the hook numbers (1 in 1,000, 99%, 9%) are still Veritasium's *The Bayesian Trap* (2017), so the fresh image has to come from the Cardiff crowd collapsing into its alerts.

## KEEP

1. The 110-dot strip hanging under the meter, with its two red columns aligned to the 9% segment, and the formula built from the braces, then the table, then ÷10,000, then the names (1:19–2:14).
2. The half-sick check where the rule holds, then the same beam on the rare case failing by a measured "11× too high" (0:25–1:10).
3. The payoff diagram morphing into the cold-open diagram, the live prior sweep onto the returning naive marker, and the 10-vs-100 flow widths under the closing chiasmus (3:14–3:45).
