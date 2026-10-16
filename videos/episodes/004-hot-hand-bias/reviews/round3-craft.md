# Episode 004 — Round 3 review (craft critic: visual design · motion · A/V sync)

**Evidence.** I used the existing pack in `review/` because `review/metrics.json` (21:31) is newer than `final.mp4` (21:29).

What I read:
- report.md and all 11 contact sheets.
- The transcript and the word timings (transcript_words.tsv).
- script.md, narration.txt, facts.md, CHANGELOG.md and the round-2 craft review.
- 13 full-resolution keyframes: 0:08.3, 0:20.5, 0:25.6, 0:34.4, 1:03.6, 1:38.8, 1:52.5, 1:56.3, 2:22.7, 2:40.3, 2:54.2, plus the 3:08.9 and 3:13.8 sheet frames.

Frames I extracted myself into /tmp/ep4r3:
- Single frames at 0:09.5, 1:11.5, 1:47.0, 1:51.0, 1:54.8, 2:11.0, 2:35.5, 2:38.5, 2:52.3, 2:53.0 and 3:12.5.
- 2 fps strips for the mirror beat (1:50–1:57) and the ghost-tick beat (2:33.5–2:40.5).
- A 4 fps strip for the hot/cold arrows (0:29.5–0:33.5) and for the cold open (0:00–0:02).

I re-enumerated all 16 sequences myself (14 scored, mean 17/42; after tails 25/42; 12 H of 24 checked; 8 rows with a checked H, 11 with a checked T). I edited nothing except this file.

```
EPISODE: 004 — "The Hidden Bias That Hid the Hot Hand"
IDEA: Averaging "share of heads after a heads" row by row gives every sequence one vote however many flips it checked, so heads-after-heads (which crowd into few rows) are under-weighted and a fair coin reads 17/42; the mirror bias after tails makes a random shooter's after-hits − after-misses gap −8 for GVT's design, so Cornell's +4 is really +12.
SCORES: Hook 9 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.6 (862.5/100 = 8.625)   AFTER CEILING: 8.6 (lowest 8.5 + 2 = 10.5, does not bind)
CAPS: none
FINAL: 8.6   PASS: no
```

Round 3 is a clear step up from 8.2. Round 2's three biggest craft defects are fixed:
- The mirror flip now plays over about 1.4 s (1:54.2 → 1:55.6), synced to "flips over one half".
- The −19 → −8 relation is now drawn with ghost ticks.
- The glyph-shatter transforms are gone.

What keeps it below 9 is a set of smaller, real problems:
- One layering choice muddies the central contrast: the row-average marker cuts through the pooled strip.
- The transition out of the insight is muddy (1:50.5–1:51.5).
- The ghost-tick beat is rushed and its dot code is never decoded.
- The payoff's right column relies on colour alone.
- There are a few Write and pulse debris moments.

## FACTS

| Claim | Verdict | Source / check |
|---|---|---|
| 4 flips → 16 equally likely sequences | Verified | 2^4 |
| HHTH: checked flips 2, 3 → "one of the two is heads" | Verified | my enumeration |
| HHHT "checks three flips, two of them heads" (2/3) | Verified | enumeration |
| 2 rows (TTTH, TTTT) unscored; 14 scored; dots 0×6, ½×4, ⅔×1, 1×3 | Verified | enumeration (matches the 1:03.6 dot plot) |
| Mean 17/42 ≈ 40.5%; "reads cold by nine and a half points" | Verified | 17/42 = 0.4048; 50 − 40.48 = 9.52 |
| 24 checked flips: 12 H / 12 T, "exactly half" | Verified | Σh = 12, Σn = 24 |
| "Twelve heads crowd into eight rows; twelve tails spread across eleven" | Verified | enumeration: 8 and 11 |
| After tails: 25/42 (strip mirrored about ½, colours swapped) | Verified | enumeration; mirror geometry checked at 1:56.3 (heads part ends at 59.5%) |
| Gap 17/42 − 25/42 = "minus nineteen points" | Verified | −8/42 = −19.05 |
| GVT 1985, *Cognitive Psychology*; "a powerful and widely shared cognitive illusion" | Verified | GVT pp. 312–313 via Miller & Sanjurjo 2018 fn. 8 (verified in rounds 1–2) |
| 26 Cornell players, up to 100 shots, from about 50%; 3 hits vs 3 misses | Verified | M&S 2018 §3.1, Table 2 |
| Random shooter 46% / 54%; M&S "about minus eight points" | Verified | M&S 2018 §3.2 ("expected difference … is −8 percentage points"); facts.md exact DP 0.4603 |
| Longer streaks grow the bias; longer records shrink it (ghost positions −1.0, −3.1, −7.9 → −0.1, −0.3, −0.7) | Verified | M&S abstract; facts.md row 18 DP values; the positions on screen match (2:35.5, 2:38.5) |
| Cornell 49% / 45%, +4; "+12 points hot" | Verified | M&S 2018 §3.1–3.2 ("+12 percentage points higher") |
| "Evidence in a gym, not proof it survives defenders" | Verified | M&S §3.1 (design removed defensive pressure), fn. 22 |
| M&S 2018 · *Econometrica* | Verified | 86(6):2019–2047 |

No wrong, uncited or fabricated claims. Citations are on screen at 0:19–0:33 (GVT) and from 2:09 to the end of the payoff (GVT, then M&S from 2:29).

## MECHANICS

| Metric | Value |
|---|---|
| Runtime | 3:13.9 |
| Pace | 154 wpm (speech time); 484 words |
| Longest internal silence | 2.06 s (the planned prediction hold, 0:11.3–0:13.4) |
| Leading / trailing silence | 0.00 s / 0.91 s |
| Longest static stretch | 3.2 s (0:18.1–0:21.3) |
| Loudness | −14.0 LUFS / −2.1 dBTP |
| Black frames | 0 |
| Layout audit | 0 issues |
| WER | 1.3% (rows/rose, pool/pull: homophones; "Sanjorjo's" is an acceptable rendering) |
| §4 banned phrases or patterns | 0 |

No mechanical caps.

## Sync audit (deictic → visible, ±2 s)

| Spoken (word time) | On screen | OK |
|---|---|---|
| "Here, one of the two" 0:04.1 | rings at 0:05, "1/2" by 0:07 | yes |
| "all sixteen sequences" 0:08.3 | ghost miniature at 0:09.5 | yes |
| "What do you get?" ends 0:10.9 | "?" over the axis at 0:11, hold to 0:13.4 | yes |
| "One half feels obvious" 0:13.3 | dashed "the obvious guess" at 0:15 | yes |
| "In 1985" 0:17.5 | GVT citation at 0:19 | yes |
| "illusion" 0:25 | quote at 0:25 | yes |
| "Heads are hits" 0:25.9 | hit/miss morph by 0:27 | yes |
| "This row checks three flips" 0:41.0 | HHHT boxed by 0:43 | yes |
| "Two rows never…" 0:47.6 | TTTH/TTTT boxed by 0:49 | yes |
| "17 out of 42 … 40.5%" 0:57–1:00.8 | live marker 48.8% → 40.5% at 0:57–0:59 | yes |
| "reads cold by nine and a half" 1:03–1:07 | red arrow and "cold −9.5 points" at 1:05–1:07 | yes |
| "Gather all 24" 1:09.8 | tiles fly 1:11–1:13; 12/24 by 1:15 | yes |
| "This row's three heads" 1:28.3 / "this lone tails" 1:31.4 | HHHH box 1:29 / HTTT box 1:33 | yes |
| "eight rows" 1:35.1 / "eleven" 1:38 | outlines at 1:35 / 1:37–1:39 | yes |
| "seventeen out of forty two" 1:41.9 | yellow slides onto 40.5% by 1:43; 17/42 at 1:43 | yes |
| "Swap heads and tails" 1:51.9 | recolour at 1:53.0–1:53.5 | yes |
| "flips over one half" 1:54.4–1:55.4 | half turn 1:54.2–1:55.6 | yes |
| "twenty five out of forty two" 1:59.4 | 25/42 at 2:01 | yes |
| "minus nineteen" 2:05.4 | red arrow at 2:05, "−19 points" at 2:07 | yes |
| "Miller and Sanjurjo" 2:27.6 | M&S citation at 2:29 | yes |
| "Longer streaks" 2:34.0 / "records shrink it" 2:36 / "isn't long" 2:39.3 | ghosts out by 2:35 / shrink 2:36–2:37 / back by 2:39 | yes (rushed, see Motion) |
| "49%" 2:41.7 / "45" 2:45 / "plus 4" 2:48.1 | values at 2:43 / 2:45 / +4 marker 2:49 | yes |
| "twelve points hot" 2:52.4 | brace 2:51–2:52.3, label 2:52.3–2:53.5 | yes |
| "seventeen out of forty two" 3:03.5 | rows collapse, 17/42 marker by 3:05 | yes |
| "running hot" 3:12.1 | arrow and "hot" at 3:12.5 | yes |

Every deictic lands, and the sync cap is not triggered.

## Dimension notes (evidence)

### Hook 9
- **0:00.** The first frame shows four coins edge-on, mid-flip. There is no title card.
- **0:04–0:11.** The worked example (HHTH → 1/2) sets up the question, which ends at 0:10.9 over a "?" on the share axis. A planned 2.06 s hold follows (0:11.3–0:13.4).
- **Stakes.** They arrive inside the stakes slot: GVT plus the "cognitive illusion" quote at 0:17–0:27.
- **Landing (3:01–3:13).** It rebuilds the exact cold-open frame, collapses the ghost of the 16 rows onto 17/42 and draws "→ hot" to 50%. It resolves the opening exactly.
- **Remaining nits:**
  - The 0:26–0:41 stretch (hit/miss morph, hot/cold arrows, "test the test") is the only place tension dips.
  - The question "average that share over all sixteen sequences" is abstract for a first watch. The ghost miniature at 0:09.5 is tiny and dim (≈ 0.18-unit coins), so the "all sixteen" is barely seen.

### Clarity 8.5
- **What works.** The coin half is close to canonical:
  - one row, then 16 rows;
  - a measured failure (−9.5 points);
  - the pooled 12/24 shown against the one-vote 17/42 on the same axis;
  - and now a visible mirror (1:53–1:56: copy, recolour, half turn about 50%, heads part ends at 59.5%).
- **What costs the half point:**
  1. **The central contrast is muddied by layering.** From 1:13 to 1:49 the blue 40.5% row-average marker runs from the axis up through the *pooled* 12/24 strip (keyframe 1:38.8: the line crosses the 11th yellow pooled tile at x ≈ 655 px; again at 1:47.0). For 35 s the pooled strip looks as if it reads 40.5%, which is exactly the confusion the beat exists to remove.
  2. **The ghost-tick dot code is never decoded (2:34–2:40).** ●, ●● and ●●● mean "1, 2, 3 hits in a row", but no label or narration says so. The glyphs sit *between* ticks: at 2:40.3 the ●● sits between the −3.1 and −1.0 ticks, and the ● between −1.0 and 0. Which glyph belongs to which tick is ambiguous.
  3. **The landing sentence is dense.** "A fifty percent shooter whose rows average one half here is already running hot" (3:07.1–3:13.0) is spoken in one breath, and "rows" is heard as "rose". This is the reframe line, and it needs a rewatch.

### Visual 8.5
- **What works:**
  - The semantic palette is held for the whole runtime: yellow for heads/hits, grey for tails/misses, blue for the test's reading, red for bias, purple for real Cornell data, ink for the assumption.
  - Type sizes pass. Ticks are about 30 px digits and citations about 28 px cap height, both at 0:20.5.
  - The safe area is respected; the layout audit found 0 issues.
  - The mirror and payoff are re-centred: the round-2 bottom-heavy problem is fixed (1:52.5, 2:22.7).
  - The 1:38.8 vote-strip frame and the 2:54.2 "+12 points" brace frame are teach-from-them screenshots.
- **Defects:**
  1. **The marker passes through the pooled strip** (1:13–1:49), as described under Clarity 1.
  2. **The payoff right column relies on colour alone and floats (2:33–2:58).**
     - After the lanes collapse into the gap axis at 2:31–2:33, "after 3 hits / 46%" and "after 3 misses / 54%" no longer label anything on screen.
     - At 2:43–2:47, 49% and 45% are set beside 46% and 54% (2:54.2). The only cue that one pair is "random shooter" and the other is "Cornell" is blue vs purple, with no header.
  3. **A doubled line at the −8 marker.** At 2:35–2:40 the ●●● ghost tick sits about 7 px right of the bright −8 marker (2:40.3, x ≈ 338 vs 345 px), so the marker reads as a double stroke.
  4. **A label mismatch (0:27–0:36).** The coins read hit/miss while the axis still says "checked flips that are heads" (0:34.4).

### Motion 8.5
- **What works.** Objects persist and transform with meaning, and these moves are the episode's strength:
  - scores shrink to dots and fall (0:53–0:57);
  - coin discs morph into tiles (1:11–1:13);
  - each row resizes to one vote (1:19–1:23);
  - yellow slides onto the 40.5% marker (1:40–1:43);
  - the half-turn mirror (1:54.2–1:55.6, one sine ease);
  - the cursors carry into the −8 marker with the axis relabelled in place (2:29–2:33);
  - the purple values fly into +4 (2:47–2:49).
- **Defects:**
  1. **The exit from the insight is muddy (1:50.5–1:51.5, mirror strip).** The pooled strip slides down and cross-fades *through* the vote strip, so two strips are superimposed for about 1 s. Σhᵢ/Σnᵢ = 12/24 stays at full brightness at 1:51.0 after its strip is gone. In the same frame, the fading 1/14 Σ formula touches the "100%" tick label ("100%14").
  2. **The ghost-tick beat is rushed (2:34.0–2:39.5, 2 fps strip).**
     - Out, shrink and back each take about 1–1.5 s.
     - The 1,000-shot state holds about 1.0 s (2:37.0–2:38.0), with the "1,000 shots" label readable about 1.3 s. That is below the 1.5 s reading floor.
     - The yellow dot glyphs do not travel with their ticks. They are left behind and dimmed at 2:37–2:38, which breaks the tick-to-streak correspondence at exactly the moment it matters.
  3. **Write debris on "+12 points" (2:52.3–2:53.0).** At 2:52.3 a stray "L" stroke floats above the brace; at 2:53.0 the "t" and "s" overprint ("pointts").
  4. **The cross-fade of 12/24 into the stacked fraction (1:47.0)** shows doubled glyphs for about 0.5 s.
  5. **The pulse on "the obvious guess" (0:30.5)** scales the label about its centre, so it collides with the dashed line it labels.

### Audio 8.5
- The mechanics are on target:
  - 154 wpm;
  - −14.0 LUFS / −2.1 dBTP;
  - pauses vary by role;
  - the prediction hold is 2.06 s.
- Every deictic lands (table above), and "Sanjurjo" is fine.
- What holds it under 9:
  - The landing line, the most important sentence, has no internal pause (3:07.1–3:13.0).
  - "rows" reads as "rose" in isolation (whisper heard "rose" at 3:09.6).
  - "Pool" is heard as "pull" (1:46.8), at the one line where the word carries the concept.

### Concision 8.5
- 484 words in 3:14. Nearly every sentence carries a step.
- Slack:
  - "That's the row average, one vote per row" (1:43.2–1:46.6) restates what the strip just showed, although it carries the hᵢ/nᵢ flights.
  - The hot/cold arrows (0:29–0:33) are pre-seeding that the "cold −9.5" beat re-does at 1:05.

### Originality 9
- The one-vote-per-row strip is a non-obvious, memorable image of Miller–Sanjurjo. HHHH's three heads squeeze into one vote while HTTT's lone tails gets a whole one (1:29–1:33).
- The half-turn mirror and "test the test on a coin" are also fresh. Most treatments stop at "the expected proportion is below p".
- No slop.

## FIXES (highest impact first)

1. **[1:13–1:49][Visual + Clarity] The row-average marker runs through the pooled strip (1:38.8, 1:47.0), so the pooled 12/24 strip looks as if it reads 40.5%.**
   - When the pooled strip appears (1:11), split the 40.5% marker so it spans only the vote-strip lane and the axis: top = lower strip's top + 0.15. Use `marker.put_start_and_end_on(axis_pt, vote_strip.get_top()+UP*0.15)` and keep it that height through 1:49.
   - Move the "40.5%" label to sit left of the marker *below* the pooled strip's bottom by ≥ 0.15 (it already does).
   - Give the pooled strip its own short ink tick at its 50% boundary. The dashed line already marks it, so no new label is needed.

2. **[1:50.3–1:51.8][Motion] The pooled strip slides into and through the vote strip, and 12/24 lingers after its strip is gone (1:51.0).**
   - In the `mirror` beat, fade the pooled strip *together with* Σhᵢ/Σnᵢ = 12/24 in place: `FadeOut(VGroup(pool_strip, pool_formula), shift=UP*0.3, run_time=0.5)`. Do this before the rise, not during it.
   - Fade the 1/14 Σ formula in the same play.
   - Only then raise the vote strip (0.8 s). Nothing should overlap the "100%" tick label at any frame.

3. **[2:34–2:40][Motion + Clarity] The ghost ticks are rushed and their dot code is never decoded.**
   - (a) Attach each dot glyph above its own tick: `dots.add_updater(lambda m, t=tick: m.next_to(t, UP, buff=0.08))`. That way ●, ●● and ●●● travel with their ticks and never sit between ticks.
   - (b) On "Longer streaks" (2:34.0), write one grey tick-size label "hits in a row" (Text 20) above the ●●● group. The same effect is possible with no new words by placing a small "3" / "2" / "1" (MathTex 28, yellow) above each tick instead of dots.
   - (c) Start the slide-back on "isn't" (2:39.3) instead of on "but" (2:37.9), so the 1,000-shot state and its label hold ≥ 1.5 s. If the hold still runs short, shift the ghost clear-out 0.3 s into "Cornell's".
   - (d) Start the 3-hit ghost exactly at the −8 marker's x (or hide it under the marker) to remove the doubled stroke seen at 2:40.3.

4. **[2:41–2:58][Visual] The payoff right column distinguishes random vs Cornell by colour alone, and its labels float after the lanes collapse.**
   - At 2:41, when 49% appears, add two column headers above the values: "random" (blue) over 46%/54% and "Cornell" (purple) over 49%/45%, as Text 20 (tick-size).
   - From 2:33 to 2:41, while no lanes exist, keep the column dimmed to 30% (it currently returns to full at 2:41 only).

5. **[2:52.3–2:53.5][Motion] Writing "+12 points" leaves stroke debris.**
   - Replace `Write(plus12)` with `FadeIn(plus12, shift=DOWN*0.15, run_time=0.6)`, started when the brace finishes (≈ 2:52.3), so it lands on "twelve" (2:52.4).

6. **[3:07.1–3:13.0][Audio + Clarity] The reframe line is one breath, and "rows" is heard as "rose".**
   - In narration_text.py, change it to: "A fifty percent shooter whose rows average one half [pause 0.4] is already running hot on this test."
   - Grow the blue shooter dot on "one half". Draw the "hot" arrow on "running hot".
   - Keep the 0.8 s end hold (trailing silence stays < 2 s).

7. **[1:46.9–1:47.5][Motion] The "12/24" to stacked-fraction cross-fade shows doubled glyphs.**
   - Move "12" and "24" as separate mobjects into the numerator and denominator slots: `ReplacementTransform(t12, frac[0])` and `ReplacementTransform(t24, frac[2])`, with the slash transforming into the fraction bar.
   - Use a 0.6 s `smooth` run, with no FadeTransform.

8. **[0:30.3–0:31.0][Motion] The "obvious guess" pulse collides with the dashed line.**
   - Use `Indicate(label, scale_factor=1.15)` with the label scaled about its left edge (`label.animate.scale(1.15, about_edge=LEFT)` and back), or pulse the dashed line instead of the label.

9. **[0:26–0:36][Visual] The axis title says "checked flips that are heads" while the coins read hit/miss.**
   - On "Heads are hits", `TransformMatchingTex` the title to "checked shots that are hits", and morph it back on "a fair coin" (0:36), alongside the existing letter morphs.

10. **[1:43.2–1:46.6][Concision] Trim the restating line.**
    - Change "That's the row average, one vote per row." to "That's one vote per row."
    - Keep the hᵢ/nᵢ and 1/14 flights timed to "one vote per row". This saves about 1 s.

11. **[0:08.3–0:11][Hook] The 16-row ghost miniature is too small and dim to register.**
    - Raise its coin radius to ≥ 0.12 and its opacity to 60%, so "all sixteen sequences" is seen as well as heard.
    - It already collapses into the "?" on "What".

## REACHES 9 IF ALL FIXED

Yes, narrowly. No structural change is needed: the misconception hook, the measured failure, the one picture (the vote strip) and its mirror, the cited payoff and the reframing landing are all in place.

- Fixes 1, 2, 3 and 5 lift Motion and Visual to 9.
- Fixes 1, 3 and 6 lift Clarity to 9.
- Fix 6 lifts Audio to 9.

With Concision at 8.5 (9 with fix 10), the weighted score is ≈ 8.95–9.0. Fixes 1–4 must be executed cleanly. If the ghost-tick beat is only slowed and its dots remain undecoded, the episode stays at about 8.7.

## KEEP
- The vote strip (1:13–1:49): HHHH's three heads squeezed into one vote and HTTT's lone tails stretched to a whole one, with the yellow sliding onto 40.5% and the pooled 12/24 shown on the same axis.
- The half-turn mirror about the dashed 50% line (1:53–1:56), and the after-hits cursor carried into the −8 "random shooter" marker with the axis relabelled in place, ending on the purple +12 brace.
- The landing on the rebuilt cold-open frame: the 16 rows collapse onto 17/42 and "→ hot" is drawn to the 50% dot.
