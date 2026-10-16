# Round 3 review: craft critic (visual design, motion, A/V sync)

Evidence: the existing pack `review/`. Its metrics.json (19:27) is newer than final.mp4 (19:25), so I did not regenerate it. I read:
- report.md and all 12 contact sheets;
- full-resolution keyframes at 0:15.3, 0:23.9, 0:37.2, 1:21.9, 2:12.8, 2:54.9, 3:23.3 and 3:34.6;
- 37 frames I extracted with ffmpeg at 0:26.0, 0:26.5, 0:27.0, 0:27.5, 0:28.0, 1:22.0, 1:22.6, 1:23.2, 1:24.0, 1:24.5, 1:33.0, 1:41.0, 1:43.0, 2:19.5, 2:27.2, 2:41.0, 2:49.0, 3:02.0, 3:02.6, 3:03.4, 3:04.4, 3:05.0, 3:05.6, 3:10.6, 3:11.4, 3:12.0, 3:14.0, 3:14.4, 3:14.8, 3:18.4, 3:18.8, 3:19.0, 3:19.2, 3:19.6, 3:20.0, 3:32.0 and 3:34.0;
- transcript.txt, transcript_words.tsv, narration.txt, final.srt, script.md, facts.md, CHANGELOG.md, round2-craft.md, and the prior-sweep code in scene.py.

I web-checked the Davies et al. 2018 Cardiff University report ("around 1200 images were enrolled onto watchlists for this event"; "2,470 total matches, 173 'true'").

```
EPISODE: 002-base-rate-fallacy — "When a 99% Accurate Test Says You're Sick"
IDEA: A positive result shrinks the sample space to the people who tested positive; when the condition is rare (1 in 500) that crowd is mostly false alarms, so your chance is 17%, not the test's 99%. Bayes' theorem and a classifier's precision are that share written down.
SCORES: Hook 9 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 8
WEIGHTED: 8.5 (852.5/100)   AFTER CEILING: 8.5 (ceiling = 8 + 2 = 10, not binding)
CAPS: none. Text overlaps occur only inside transforms (0:27.0, 1:23.2, 1:33.0, 1:43.0, 2:27.2), each ≤ ~1.5 s while things move; as in rounds 1–2 they are fixes, not cap 7. No typos, clipping, black frames or banned phrases; every empirical claim is cited on screen.
FINAL: 8.5   PASS: no
FACTS:
 - Premise 1 in 500, 99% caught, 1% of healthy flagged (title "99% accurate" consistent: sens = spec = 99%) | Verified | premise
 - P(sick|+) = 0.002·0.99 / (0.002·0.99 + 0.998·0.01) = 99/598 = 16.6% → "17%" | Verified | recomputed
 - "Six times too high" (0.99/0.1656 = 5.98) | Verified | recomputed
 - 10,000 people: 20 sick → 19.8 ≈ 20 +; 9,980 healthy → 99.8 ≈ 100 +; 20/120 = 16.7% | Verified (labelled "expected counts", then shown unrounded) | recomputed
 - Half sick: 4,950 + 50 positives, 4,950/5,000 = 99% | Verified | recomputed
 - 20/10,000 = 0.002, 9,980/10,000 = 0.998; Bayes with total-probability denominator | Verified | algebra
 - Prior sweep: 1/100 → 50.0%, 1/2 → 99.0% | Verified at rest. In motion the meter lags the "1 in N" label by a few frames (3:19.0: "1 in 74" with 64%, true 57.6%; 3:18.8: "1 in 15" with 90%, true 87.6%) | fix 6, not an error on screen at rest
 - Landing flow widths 19.8 : 99.8 people; "recall" = 99% = P(+|sick), "precision" = 17% = P(sick|+) | Verified | definitions
 - Gigerenzer et al. 2007, PSPI 8(2): gynecologists 21% right before, 87% after natural-frequency training | Verified | doi:10.1111/j.1539-6053.2008.00033.x p. 55, Fig. 2 (as in facts.md and round 2)
 - Cardiff 2017 Champions League final: ~170,000 people; 2,470 alerts; 2,297 wrong → 173 right = 7.0% | Verified | BBC News 4 May 2018; Davies et al. 2018 ("2,470 total matches, 173 'true'")
 - "The watch lists held about 1,200 faces" | Verified | Davies, Innes & Dawson 2018, Cardiff Univ., "around 1200 images were enrolled onto watchlists for this event"
 - "Police also blamed poor-quality photos" | Verified | BBC 4 May 2018 ("poor quality images" from UEFA, Interpol)
 - "1 square = 17 people" (170,000/10,000); 145 lit squares × 17 ≈ 2,465 ≈ 2,470 | Verified (scale; positions illustrative)
MECHANICS: runtime 3:34.6 · wpm 154 (speech time; 148 overall) · max silence 2.08 s (0:13.4, planned prediction hold) · max static 3.63 s (1:58.0) · −14.1 LUFS / −2.2 dBTP · lead 0.00 s / trail 1.73 s · WER 2.1% · 0 banned phrases
```

## What I saw (flipbook notes)

- **0:00–0:15 cold open.** The diagram ("1 in 500", sick/healthy nodes) and a ghosted "chance you're sick ?" meter are in frame 1. The arrows grow on "99%" and "1%", the "you" ring closes on "yours says positive" (0:11), and the "?" brightens on the question. "Pick a number" ends at 0:13.5 and the frame holds 2.1 s before anything new appears (kf 0:15.3). Round 2's fix 6 is done: the commit now lands at ~0:12.6, *before* the "21% right" waffle (0:16–0:22). This is the right order.
- **0:19–0:25 stakes.** The red arrow's "99%" lifts off, parks beside the meter title (0:23) and drops onto the dashed "naive 99%" marker (0:25). It no longer collides with its source or the bar (kf 0:23.9 is clean). Fixed.
- **0:26–0:28 diagram → table.** This is the weakest transform in the episode. The nodes slide *across their own labels* (0:27.0: a red dot sits on "s●ck", a blue dot on "h●althy"). The blue arrow passes through "1%" (0:26.5 "1%you", 0:27.0). The "you" ring detaches from the + and is left behind as a ghost while the + flies to the column header. "1 in 500" is orphaned at 30% on the left. The parts come apart instead of the diagram straightening into rows (fix 2a).
- **0:28–1:13 build and fail.** Strong. The 100 × 100 "expected counts" grid, the yellow beam, live counters (2,809 → 5,000; 765 → 4,950) and the meter filling onto the naive marker (0:41) show the rule holding. The recolour then runs on "rare" (0:45), "That leaves 20 sick people" lands on 20 / 9,980 (0:49), and the same beam ticks the counts to 20 / 100. "17%" lands at 1:05, with the brace "6× too high" on "six times too high" (1:09–1:11). On "1% of nearly everyone" the dim crowd brightens (1:15), which fixes round 2's fix 8.
- **1:15–1:25 the shrink.** Negatives vanish at the end of "…ruled out everyone who tested negative" (1:20–1:21). The survivors swell (kf 1:21.9) and fly into a 24 × 5 strip under the meter, with four red columns exactly under the 17% red segment (1:25). This is still the best idea in the video. The handoff itself (1:22–1:24) is muddy:
  - "10,000 people · expected counts" crossfades *in place* with "120 people who tested +", giving a mush of overprinted glyphs at 1:23.2;
  - the red rings stay behind as the red dots leave them (1:23.2, 1:24.0, dim rings scattered under the strip);
  - the meter slides left *through* the dot cloud (1:23.2, "17%" sits on blue dots).

  Also, from 1:21 to 1:23 the header still reads "10,000 people" over a picture of 120 (fix 2b, fix 8).
- **1:29–2:15 the formula.** It is built from the picture:
  - the braces 20 / 100 fly into the fraction (1:31–1:35);
  - "19.8 / 99.8" lands on the spoken numbers (1:37, 1:39);
  - the people column × the arrow rates (1:41–1:47);
  - "top and bottom ÷ 10,000" (1:49), 0.002 / 0.998 (1:57);
  - two flagged naming steps (2:01–2:07), then boxes on the numerator and denominator (2:11–2:15).

  The table dims to ~30% once used (1:49), so the hierarchy is right. Transient collisions:
  - "100" lands on top of the "+" in the denominator (1:33.0, "20 +100");
  - the table's "9,980" double-strikes as its copy leaves (1:43.0). This is the same artifact round 2 fixed for the 99% copy, now reappearing in the table.

  "Two in a thousand" is spoken at 1:55.0–1:56.3, but 0.002 appears only at ~1:56.5–1:57 (frame 1:55 still shows "20 × 0.99"). That is within ±2 s but late.
- **2:15–2:25 gynecologists.** The formula and table clear, and the waffle returns large on the right ("before: 21% right", citation; frame 2:19.5). On "eighty-seven" the dots turn green (2:25 "after: 87% right"). This is a clean payoff of the cold open. The lower-left quadrant is empty except the citation.
- **2:26–2:29 transition to Cardiff.** It is a layered crossfade. At 2:27.2 the frame holds all of these at once:
  - the dimmed strip and braces over the incoming grey crowd;
  - the meter mid-move, still showing the *old* red/blue fill (17%) under the new, faint title "chance an alert is right";
  - the green waffle and the Gigerenzer citation, still present.

  That is four layers in one frame (fix 2c).
- **2:29–2:45 the crowd.** For about 16 s the picture is a flat grey 100 × 100 block (frames 2:29, 2:31, 2:33, 2:35, 2:37, 2:39, 2:41, 2:43). Only labels are added: "about 170,000 people", "1 square = 17 people", the red "watch lists: about 1,200 faces" and two citations. The narration's mechanism, "the watch lists held about 1,200 faces, so even a small error rate per face would swamp the real matches", is *said* but never *drawn*. Red ("on the list") appears only as a text label; nothing in the crowd is red. At full resolution the grid also shows moiré banding: lighter vertical and horizontal stripes about every 10 cells (frame 2:41.0). "1 square = 17 people" sits 15 px from the grid's right edge, under the 20 px minimum (fix 1, fix 7).
- **2:45–3:02 alerts → precision.** This is good, and it fixes round 2's fix 1:
  - the same yellow beam sweeps the crowd (2:45–2:47);
  - lit squares turn yellow, fly right and become the 26 × 95 raster of exactly 2,470 alerts under a same-width bar (2:49–2:51);
  - the raster colours 173 red / 2,297 blue with braces (2:53), and the meter fills to 7% over the red columns (2:55, kf 2:54.9);
  - the grey honest-limit note follows (2:57);
  - the title becomes "precision" on the word (3:01.8–3:02.0).
- **3:02–3:05 back to the test.** The raster collapses into the yellow + (3:03.4). For ~1.5 s, though, the meter has *no title*, and its value tweens 7% → 16% → 17% (3:04.4). A continuous count from "precision of the Cardiff alerts" to "your chance of being sick" implies a relation between the two numbers that does not exist. The cold-open diagram is redrawn with Write (3:05), not transformed from anything. That is acceptable for a return, but the meter swap is not (fix 2d).
- **3:05–3:34 landing.** The prevalence sweep is excellent: 1 in 500 → 1 in 100 at 50% (3:13) → 1 in 2 at 99% on the returning naive marker (3:15–3:17) → back. The flows' widths carry 20 vs 100, and "20" / "100" sit outside their bands (kf 3:23.3, frame 3:32.0); round 2's fix 7 is done. Two problems:
  - On the fast return sweep the meter lags the "1 in N" label by a few frames, so paused frames read "1 in 74 · 64%" (true 58%) and "1 in 234 · 33%" (true 30%) (fix 6).
  - The closing tags "recall" and "precision" (3:26, 3:30) are the smallest, dimmest text in the frame (grey, about 22 px cap height; frame 3:32.0) at the episode's payoff, and "recall" is never spoken or defined (fix 3).

  The end card arrives 1.6 s after the last word. It is clean.

## Audio / sync

I checked every deictic and numeric reference against frames:
- "these hundred and twenty people" (1:25, strip formed);
- "the red share of this crowd" (1:27–1:30);
- "twenty, out of twenty plus a hundred" (1:31–1:35, braces fly);
- "nineteen point eight" (1:37) and "ninety-nine point eight" (1:39);
- "these two" ×2 (2:01–2:07);
- "about 170,000" (2:33, label);
- "1,200 faces" (label ~2:38, ~1 s after the word);
- "2,470 alerts" (2:49–2:51);
- "seven percent" (meter 7% at ~2:55, ~1 s late);
- "this plus sign" (3:20) and "the red arrow" (3:22).

All are within ±2 s. Pauses are purposeful: a 2.1 s commit hold, ~1 s after "17%" and "six times too high", and a 1.6 s silence while 17% flies in (1:33.0–1:34.6). The insight lines are slower (speed 0.80), which fixes round 2's fix 9. Loudness and peak are on target.

What keeps Audio at 8.5 is the run 1:34.6–1:46.6: one 12 s sentence carrying four spelled-out quantities ("nineteen point eight", "ninety-nine point eight", "nine thousand nine hundred eighty", "ninety-nine percent"). It reads as bookkeeping at speed, and it is the one stretch a viewer is likely to rewind (fix 4).

## Score rationale

- **Hook 9.** The commit lands by 0:12.6 with a held pause. The "doctors got it wrong" baseline arrives as a reveal. Tension rises through the half-sick check into the measured failure. The landing returns to frame 1 and re-reads its 99% and 17%. The only sag is the algebra at 1:34–2:08.
- **Clarity 8.5.**
  - Correct, concrete-first and sourced, with assumptions stated ("expected counts", "assumes a random screen").
  - The Cardiff mechanism is asserted rather than shown (2:35–2:45).
  - "recall" appears unspoken and undefined in the last 8 s.
  - The 12 s algebra sentence needs a rewatch.
- **Visual 8.5.**
  - Strengths: a strict semantic palette (red/blue/yellow/green/grey hold their meanings through all four scenes), one focal group per beat, and the strip/meter and raster/meter alignments.
  - Below 9 because of: the 16 s grey slab with moiré (2:29–2:45); the payoff terms as the weakest type on screen (3:26–3:34); a stale "10,000 people" header over 120 dots (1:21–1:23); and a spacing miss ("1 square = 17 people", 15 px).
- **Motion 8.5.**
  - Most motion encodes a relation: the 99% copy becoming the naive marker, the beam, the recolour, survivors becoming the strip, braces becoming the fraction, table cells becoming formula terms, lit squares becoming the alert raster, and the live prior sweep.
  - Four beat transitions instead come apart into crossfading layers (0:26–0:28, 1:22–1:24, 2:26–2:29, 3:03–3:05).
  - The meter tweens across unrelated quantities (3:04), and the crowd beat is nearly motionless for 16 s.
- **Audio 8.5.** See above.
- **Concision 8.5.** Under 10% is removable, but there is one slack beat each in:
  - the algebra: "Now give each number its name" re-says what the flags do;
  - the stakes: "At ninety-nine percent, you'd start treatment today. That's the tempting answer: the test's own hit rate" says the naive answer twice.
- **Originality 8.** The hook problem is the canonical medical-test paradox (3b1b 2020, Veritasium 2017), with fresh numbers. The images that are this episode's own are the strip hanging under the meter and the Cardiff alerts collapsing into a precision bar. The Cardiff image would become memorable only if the crowd visibly carried its tiny red base rate (fix 1).

## FIXES (highest impact first)

1. **[2:29–2:47][Clarity/Visual/Originality] The base rate is a text label over a grey slab.** On "the watch lists held about twelve hundred faces" (2:35.4), turn ⌈1,200 / 17⌉ = 71 crowd squares red, scattered, with the label changed to "watch lists: ≤ 1,200 faces (≤ 71 squares)". That is an upper bound, consistent with facts.md's "not claimed" list. Hold 1.5 s on "would swamp the real matches", with the 71 red squares pulsing once.

   When the beam passes (2:45–2:48), light the 145 yellow squares so that 10 of them (173 / 17 ≈ 10) are red-underneath. When they fly to the raster, those 10 become the red block. This repeats the 1:15–1:25 shrink exactly ("red share of the lit crowd") and makes the 7% *visible before it is measured*.

   At the same time, fix the moiré: give the crowd an integer pixel pitch (100 cells × 6 px = 600 px = 4.444 units, square side 4 px, gap 2 px), or draw a 50 × 50 crowd at 68 people per square. This lifts Clarity and Visual toward 9 and is the only route to Originality 9.
2. **[Motion] Four beat transitions come apart.** Sequence each one in stages so no frame layers old and new.
   - a. **[0:26–0:28]** FadeOut "sick", "healthy", "1 in 500" and Uncreate the "you" ring (0.3 s) *before* anything moves. Then move node+arrow pairs as rigid groups (`VGroup(node, arrow, rate)`) into the table rows. FadeIn the row labels after the dots land. No dot may cross its own label, and no arrow may cross "1%".
   - b. **[1:20–1:25]** At "tested negative" (1:20) replace the header with `FadeOut(old, shift=UP*0.2)` and, after it finishes, `FadeIn("120 people who tested +")`. Make each ring a child of its dot (or FadeOut the rings at 1:21 before the fly). Move the meter only after the dots have landed in the strip, or route it above y = +3.0, so it never crosses the dot cloud.
   - c. **[2:25.5–2:29]** First FadeOut the waffle, its labels, the citation, the strip and the braces (0.5 s). Then reset the meter to an empty "?" *in place*, swapping the title with fade-out-then-fade-in. Then move it to the top right and FadeIn the crowd. Never show a 17% fill under "chance an alert is right".
   - d. **[3:02.5–3:05]** Do not tween 7% → 17%. FadeOut "precision" and the 7% value and fill, FadeIn the title "chance you're sick", and only then grow the 17% fill from 0, or ReplacementTransform the whole meter group. The meter must never be without a title.
3. **[3:25–3:34][Visual/Clarity] The payoff terms are the weakest type on screen, and "recall" is never spoken.** Set "recall" and "precision" to `MathTex` ≥ 36 / `Text` ≥ 26, at full-ink grey (`#c8ccd4`). Change the last two lines to "Ninety-nine percent is the test's recall: how often the sick test positive. Seventeen percent is its precision: how often the positive are sick." Write each tag on its spoken word, which adds about 1.5 s. Otherwise, drop the "recall" tag.
4. **[1:34.6–1:59][Audio/Clarity] The 12 s, four-number sentence and the late 0.002.** Split it into three sentences with 0.3–0.4 s pauses, each landing on its fly-in:
   - "Before rounding, these are nineteen point eight and ninety-nine point eight."
   - "That's twenty sick people times ninety-nine percent."
   - "And nine thousand nine hundred eighty healthy times one percent."

   Start the 20 → 0.002 TransformMatchingTex at `offset=-0.2` before "two in a thousand" (now ~1 s late; frame 1:55 still shows 20). Do the same for 9,980 → 0.998 on "nine hundred ninety-eight".
5. **[1:33.0, 1:43.0][Motion] Two in-flight collisions.**
   - The "100" brace label lands on the denominator "+" ("20 +100" at 1:33.0). Write "20 +" with its final spacing (target slot from `den.get_part_by_tex("100")`) before the copy flies, and approach from above.
   - The table's "9,980" double-strikes as its copy leaves (1:43.0). Start the copy 0.2 units up at opacity 0 and fade it in on the path, the same fix used for the 99% copy in round 2.
6. **[3:18.0–3:20.5][Motion/Clarity] The meter lags the prevalence label in the return sweep** (3:19.0: "1 in 74" with 64%, true 57.6%; 3:19.6: "1 in 475" with 18%, true 17.3%; 3:18.8: "1 in 15" with 90%, true 87.6%). Drive both from one updater on the same `u` (`num.add_updater(...)` and `meter.share.add_updater(...)` combined into one function called on a single mobject), or add `num` to the scene after `meter.share` so the update order matches. Lengthen the return sweep from ~1.6 s to ≥ 2.5 s with `smooth`.
7. **[2:33–2:47][Visual] Crowd labelling.** Move "1 square = 17 people" to buff ≥ 0.2 from the grid (it is 15 px away now). With fix 1 in place, put the red "≤ 1,200 faces" label next to the red squares' legend swatch, not stacked above "about 170,000 people" (two stacked headers at the top edge, 2:39–3:01).
8. **[1:20–1:23][Visual] Stale header.** "10,000 people · expected counts" stays over a picture of 120 people for ~2 s (kf 1:21.9). Swap it as the negatives vanish (part of 2b).
9. **[0:18.9–0:25.7, 1:59.3–2:01][Concision] Two slack lines (−3 s).** Merge "At ninety-nine percent, you'd start treatment today. That's the tempting answer: the test's own hit rate." into "The tempting answer is the test's own hit rate, ninety-nine percent: you'd start treatment today." Cut "Now give each number its name." The flagged naming steps already say it.

## REACHES 9 IF ALL FIXED: yes, narrowly

No structural change is needed. The episode has the misconception hook with a commit, the build-and-fail with a measured "6× too high", one picture (the strip under the meter) that becomes the formula, a real cited consequence, and a landing that re-reads frame 1.

Fixes 1–6 lift Clarity, Visual and Motion to 9. Fix 4 lifts Audio to about 9, and fix 9 lifts Concision to about 9. Projected: 15×9 + 25×9 + 15×9 + 15×9 + 10×9 + 10×9 + 10×8.5 = 895, i.e. 9.0, with no caps.

Originality stays the binding constraint. The hook is the canonical medical-test paradox, so a 9 depends on fix 1 turning the Cardiff crowd, with its 71 red squares and its 10 red-under-yellow alerts, into the image viewers remember. Without fix 1 the ceiling is about 8.8.

## KEEP

1. The 120-dot strip hanging under the meter, with its red columns aligned to the 17% segment, and the formula built from braces → table → ÷10,000 → names (1:21–2:15).
2. The half-sick check where the rule holds (0:28–0:43), then the same beam on 1 in 500 failing by a measured "6× too high" (0:43–1:11).
3. The landing: the cold-open diagram with people-width flows, the live prevalence sweep onto the returning naive marker, and the 99% / 17% chiasmus (3:05–3:34). The Cardiff beam → 2,470-cell raster → 7% precision bar (2:45–3:02) should also stay.
