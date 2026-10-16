# Episode 004: Round 3 review (substance: science and story editor)

**Evidence.** `review/metrics.json` (21:31) is newer than `final.mp4` (21:29), so I used the existing pack in `review/` and did not generate a new one. I read:

- report.md, all 11 contact sheets, transcript.txt, narration_diff.txt, narration.txt, script.md, facts.md, check_numbers.py (and ran it), and the round-2 substance and round-3 craft reviews.
- 12 full-resolution keyframes: 0:08.3, 0:20.5, 1:03.6, 1:38.8, 1:56.3, 2:22.7, 2:40.3, 2:54.2, plus the 3:01–3:13 sheet frames.
- Extra frames I extracted with ffmpeg into /tmp/ep4r3s: 0:09.5, 0:30.5, 0:51.0, 1:51.0, 2:27.0, 2:34.8, 2:37.5, 2:52.4 and 3:12.8, plus a 6-frame crop strip of the ghost-tick beat (2:36.0–2:39.0).

**Independent checks.**
- I re-enumerated all 16 four-flip sequences and checked every on-screen score against the 0:47 / 1:03.6 table: HHHH 3/3, HHHT 2/3, HHTH 1/2, HHTT 1/2, HTHH 1/2, HTHT 0/2, HTTH 0/1, HTTT 0/1, THHH 2/2, THHT 1/2, THTH 0/1, THTT 0/1, TTHH 1/1, TTHT 0/1, TTTH –, TTTT –.
- I read the 14-cell vote strip at 1:38.8 cell by cell: [3 heads], [2H 1T], [1H 1T], [1H 1T], [1T 1H], [2T], [T], [T], [2H], [1H 1T], [T], [T], [H], [T]. The yellow sums to 17/3 of 14 votes = 17/42.
- I measured the 1,000-shot ghost positions on the 2:37.8 crop at 54 px per point: about −0.8, −0.35 and −0.13, against the exact −0.71, −0.30 and −0.10. They agree to within a tick width.
- I web-verified the GVT quote and the M&S numbers (Wharton PDF of Miller & Sanjurjo, read directly; JSTOR 44955325 for the Econometrica pagination).

I edited nothing except this file.

```
EPISODE: 004 — "The Hidden Bias That Hid the Hot Hand"
IDEA: Averaging each sequence's "share of heads after a heads" gives every sequence one vote however many flips it checked, and because heads-after-heads crowd into few sequences a fair coin reads 17/42, not 1/2; the same bias (mirrored after misses) makes a random shooter's after-3-hits − after-3-misses gap −8 points in GVT's design, so Cornell's "no hot hand" +4 is really +12.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.6 (855/100 = 8.55, rounded half-up)   AFTER CEILING: 8.6 (lowest 8.5 + 2 = 10.5; does not bind)
CAPS: none
FINAL: 8.6   PASS: no
```

The science in this round is clean. Every number recomputes, both citations are right, and the assumptions that round 2 found missing are now stated:
- "from where they'd hit about half" (2:16), with the 50% tick pulsing;
- "a hundred shots isn't long" (2:38);
- "evidence … in a gym, not proof it survives defenders" (2:54–3:01).

The round-2 landing contradiction is fixed. HHTH keeps its own 1/2, the 16-row ghost collapses onto 17/42, and the shooter is a separate dot (3:03–3:13).

What keeps the episode under 9 is a set of explanation-level frictions, none of them errors:
- For 35 s the row-average marker cuts through the pooled strip.
- The 46%/54% random-shooter values first appear under a "Cornell, 1985" header with only the GVT citation.
- The streak-length dot code is never decoded, and the beat is too fast to read.
- The reframe sentence is crammed into one breath with a homophone ("rows"/"rose").

## FACTS

| Claim | Verdict | Source / my check |
|---|---|---|
| 4 fair flips → 16 equally likely sequences | Verified | 2⁴ |
| HHTH: checked flips 2 (H), 3 (T) → "one of the two is heads" | Verified | enumeration |
| HHHT "checks three flips, and two of them are heads" | Verified | enumeration (2/3 at 0:45) |
| TTTH, TTTT get no score; 14 rows scored | Verified | enumeration; same convention as M&S 2018 (expectation conditional on ≥1 recorded flip) |
| Dot plot: 0×6, ½×4, ⅔×1, 1×3 (1:03.6) | Verified | enumeration |
| Average = 17/42 ≈ 40.5% | Verified | (3 + ⅔ + 4·½)/14 = (17/3)/14 = 17/42 = 0.4048 |
| "reads cold by nine and a half points" | Verified | 50 − 40.48 = 9.52 |
| 24 checked flips, 12 H / 12 T, "exactly half" | Verified | Σh = 12, Σn = 24 |
| "Twelve heads crowd into eight rows; twelve tails spread across eleven" | Verified | enumeration: 8 and 11 (the outlines at 1:35 and 1:39 match) |
| Heads hold 17/42 of the 14 votes | Verified | strip read cell by cell at 1:38.8 |
| After tails: 25/42; strip is the H↔T-swapped mirror | Verified | enumeration; geometry checked at 1:56.3 (heads part ends at ≈59.5%) |
| "gap of minus nineteen points" | Verified as worded ("subtract the two averages") | 17/42 − 25/42 = −4/21 = −19.05 |
| GVT 1985 · *Cognitive Psychology*; "a powerful and widely shared cognitive illusion" | Verified | M&S 2018 quotes GVT pp. 312–313 verbatim (Wharton PDF; JSTOR) |
| Cornell: 26 players, ~50% distance, after 3 hits vs after 3 misses | Verified | M&S §3.1: "26 players from the Cornell University Mens' (14) and Womens' (12) basketball teams … Each player shot 100 times at a distance from which the experimenters determined he/she would make around 50 percent". "Up to 100" is safe whether or not some records were shorter. |
| Random shooter, n = 100, p = .5: 46% / 54% | Verified | check_numbers.py DP: 0.4603 / 0.5397 |
| M&S: gap "about minus eight points" | Verified | M&S: "the expected difference (and the strength of the bias) is -8 percentage points" |
| Longer streaks grow the bias; longer records shrink it (ghosts −1.0, −3.1, −7.9 → −0.1, −0.3, −0.7) | Verified | M&S abstract; DP values reproduced by check_numbers.py; on-screen positions measured (above) |
| Cornell 49% after 3 hits, 45% after 3 misses; read as no hot hand | Verified | M&S: "players on average hit .49 when on a hit streak, versus .45 when on a miss streak"; GVT's test found it indistinguishable from zero |
| "Measured from minus eight, it's twelve points hot" | Verified | M&S: "+4 … is actually +12 percentage points higher than the difference that would be expected from a Bernoulli i.i.d. shooter". (Their bias-adjusted per-player estimate is +13, p < .01; not claimed.) |
| "evidence … in a gym, not proof it survives defenders" | Verified | M&S §3.1 (design eliminated defensive pressure), fn. 22 |
| Miller & Sanjurjo, 2018 · *Econometrica* | Verified | 86(6):2019–2047 (JSTOR pagination 2022, 2031 in range) |
| Landing: a 50% shooter whose rows average ½ "is already running hot" | Verified (as a statement about the 4-shot-row test vs the 17/42 baseline) | follows from rows 6 and 23 of facts.md |

There are no wrong, fabricated or uncited numbers.

One precision nit, not an error. The cold-open question says "average that share over all sixteen sequences" (0:06.5), but only 14 sequences have a share. The video corrects this explicitly at 0:47 ("Two rows … get no score"), so I treat it as a fix item, not a fact error.

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
| Layout audit | 0 issues in 196 settled frames |
| WER | 1.3%: rows→"rose" (3:09.6), pool→"pull" (1:46.8), "Sanjorjo's" (an acceptable rendering) |

No mechanical caps.

## Transcript and slop scan (BAR §4)

- **Banned phrases: 0.** I checked the full list by hand against the transcript.
- **Banned patterns: 0.**
  - There is one genuine question ("What do you get?", 0:10.4), and it stands alone with a 2.06 s hold.
  - There is no "not just X", no colon reveal and no abstract-adjective triplet.
  - "That's evidence for a hot hand in a gym, not proof it survives defenders in a game" is a substantive scope limit, not the banned "isn't just" construction.
  - "a famous study" (0:17) is the only near-empty adjective, and the GVT quote on screen earns it.
- **Dropped or garbled lines.** None against narration.json. All six diffs are homophones or articles.
- **Hook.** The procedure is on screen from frame 1 (coins mid-flip at 0:01). The question lands at 0:10.9 and the prediction hold runs 0:11.3–0:13.4, inside the 0:15 limit.
- **Ending.** "One half is what a fair coin does. Seventeen out of forty two is what this test sees." (3:01–3:06) restates the opening, but it does so over the rebuilt cold-open frame and pays it off in the next sentence. It is a reframe, not a lesson list.

## Story structure vs BAR §6

| Beat | Target | Here | Note |
|---|---|---|---|
| Cold open | 0:00–0:12 | 0:00–0:13 | HHTH worked, 16-row ghost, "?" on the share axis |
| Stakes | 0:12–0:25 | 0:13–0:26 | "one half feels obvious" + GVT + "cognitive illusion" quote |
| Naive build | 0:25–1:05 | 0:26–1:01 | hit/miss mapping, "test the test", 16-row table, 14 scores |
| Fail | 1:05–1:25 | 0:57–1:07 | live marker 50% → 40.5%, "cold −9.5 points" |
| Insight | 1:25–2:15 | 1:07–2:07 | pooled 12/24 vs one-vote 17/42, mirror, −19 |
| Payoff | 2:15–2:45 | 2:07–3:01 | Cornell, −8 baseline, ghost ticks, +12, defenders limit |
| Landing | 2:45–3:00 | 3:01–3:14 | cold-open frame rebuilt; 17/42 answers the "?"; "hot" |

The beats are in order and scale well to 3:14.

The one sag is 0:26–0:41. Three sentences of framing play over the same HHTH row: the hit/miss morph, "→ hot" / "cold ←" arrows, and "test the test". There is no new information on screen until the table deals at 0:38. The pre-seeded "cold ←" arrow (0:33) also spends the word the fail beat cashes at 1:05.

## Dimension notes (evidence)

### Hook 8.5
- **Works:**
  - The first frame is the object itself: four coins mid-flip (0:01).
  - The worked example comes before the question (0:04–0:08), and the 16-row ghost (0:09.5) makes "all sixteen" visible.
  - The landing (3:01–3:13) rebuilds the exact cold-open frame and drops 17/42 onto the "?" position. The ending resolves the opening exactly.
- **Holds it under 9:**
  - The question is procedural rather than irresistible. "Average that share over all sixteen sequences" asks the viewer to hold a two-step operation in their head, and it is slightly imprecise (14, not 16).
  - The stakes (GVT, "illusion") arrive after the commit.
  - 0:26–0:41 is setup with no rising tension (see above).

### Clarity 8.5
- **Near-canonical:**
  - The coin half goes one row → sixteen rows → fourteen dots → a live marker that settles at 40.5% → pooled 12/24 vs one-vote 17/42 on the same axis.
  - The mirror is now a real, visible proof of 25/42: copy, recolour, half turn about 50% (1:53–1:56).
  - Every on-screen number checks, and the GVT design assumption (≈50% distance) is now shown and spoken (2:16–2:18).
- **What costs the half point:**
  1. **The pooled strip appears to read 40.5% (1:13–1:49).** The blue row-average marker runs from the axis up through the pooled 12/24 strip, crossing its 11th yellow tile (1:38.8 at x ≈ 655 px). The beat exists to separate "pooled = ½" from "row average = 17/42", and the picture fuses them for 35 s.
  2. **The 46%/54% random-shooter expectation is shown as if it were Cornell data (2:23–2:29).**
     - The numbers appear under the purple "Cornell, 1985 · 26 players · up to 100 shots" header.
     - The only citation on screen is "Gilovich et al., 1985" (frame 2:27.0).
     - The M&S citation, whose computation these are, arrives at 2:29, and the "random shooter" label not until 2:33.
     - A first-time viewer can read "Cornell: 46% after 3 hits". The narration says "for a random shooter", so this is not an attribution error, but the picture says otherwise for about 6 s.
  3. **The streak-length dot code is never decoded (2:34–2:40).**
     - Nothing on screen or in the narration says that ●, ●● and ●●● mean "1, 2, 3 hits in a row".
     - In the 1,000-shot state the dots are left behind at about 15% opacity (2:37.8 crop), so the tick-to-streak correspondence disappears exactly when "longer records shrink it" is spoken.
  4. **The reframe sentence needs a rewatch (3:07.1–3:13.0).** "A fifty percent shooter whose rows average one half here is already running hot" is spoken in one breath, and "rows" is heard as "rose".

### Visual 8.5
- **What works:**
  - Six semantic hues, each held to one meaning for the whole runtime: yellow for heads/hits, grey for tails/misses, blue for the test's reading, red for bias, purple for real Cornell data, ink for the assumption.
  - Charts carry quantity names ("checked flips that are heads", "next-shot hit rate", "after-hits − after-misses (points)") with ≤ 5 ticks.
  - Citations are in BAR format, bottom-left (0:20.5, 2:40.3).
  - Safe areas are clean, and the 0:20.5 keyframe meets the type minimums.
  - 1:03.6, 1:38.8 and 2:54.2 are teach-from-them frames.
- **Defects:**
  1. The marker-through-pooled-strip layering (1:13–1:49), as under Clarity.
  2. **The payoff right column relies on colour alone (2:43–3:00).** "46% 49%" / "54% 45%" sit side by side, and only blue vs purple says which pair is the random shooter and which is Cornell (2:54.2). The lane labels "after 3 hits / after 3 misses" no longer label anything on the gap axis.
  3. **The −8 marker reads as a double stroke.** At 2:36–2:39 the ●●● ghost tick sits a few px right of the −8 marker.
  4. **Mid-Write glyph debris on "+12 points".** At 2:52.4 the frame shows a half-drawn "+1?" (my frame), and the 2:53.0 sheet frame shows "points" with a stray raised "s".

### Motion 8.5
- **Strong, meaningful persistence:**
  - scores → dots → falling onto the axis (0:53–0:57);
  - coin discs → tiles (1:11–1:13);
  - each row resized to one vote (1:19–1:23);
  - yellow slides onto 40.5% (1:40–1:43);
  - the half-turn mirror (1:54–1:56);
  - the cursors become the −8 marker with the axis relabelled in place (2:29–2:33);
  - purple values fly into +4 (2:47–2:49).
- **Defects:**
  1. **The exit from the insight is muddy (1:50.5–1:52, frame 1:51.0).**
     - The pooled strip cross-fades through the vote strip.
     - Σhᵢ/Σnᵢ = 12/24 stays at full brightness after its strip is gone.
     - The fading 1/14 Σ formula touches the "100%" tick ("100%14").
  2. **The ghost-tick beat is rushed (2:34–2:40).** The 1,000-shot state holds about 1.0 s (2:37.8–2:38.3 static, moving back by 2:39.0), which is below the 1.5 s reading floor for "1,000 shots".
  3. The Write debris on "+12 points" (2:52.3–2:53.0).

### Audio 8.5
- **On target:**
  - 154 wpm, −14.0 LUFS / −2.1 dBTP;
  - the prediction hold is 2.06 s;
  - pauses vary by role;
  - every deictic lands within ±2 s ("This row checks three flips" 0:41 → HHHT boxed by 0:43; "this lone tails" 1:31 → HTTT boxed 1:33; "eight rows" 1:35 → outlines 1:35; "minus nineteen" 2:05 → red arrow 2:05).
- **Holds it under 9:**
  - "rows" → "rose" (3:09.6) in the most important sentence, which also has no internal pause.
  - "Pool" → "pull" (1:46.8), on the one word that names the contrasting method.

### Concision 8.5
- 484 words, and nearly every sentence carries a step.
- **Slack:**
  - "A hot shooter should score above their usual rate. A random one should match it." plus the hot/cold arrows (0:27–0:33) re-frame what the cold open already set up.
  - "That's the row average, one vote per row" (1:43.2–1:46.6) restates the strip, although it carries the hᵢ/nᵢ flights.

### Originality 9
- The one-vote-per-row strip is a non-obvious, memorable picture of Miller–Sanjurjo that I have not seen elsewhere:
  - HHHH's three heads squeeze into one vote while HTTT's lone tails gets a whole one (1:29–1:33);
  - the yellow slides exactly onto 40.5%.
- "Test the test on a shooter we know is random" is a strong SMH-style calibration move.
- The half-turn mirror turns a symmetry argument into motion.
- No slop.

## FIXES (highest impact first)

1. **[1:11–1:49][Clarity + Visual] The row-average marker cuts through the pooled 12/24 strip (1:38.8, x ≈ 655 px), so the pooled strip appears to read 40.5% while the narration says it reads ½.**
   - When the pooled strip lands (≈1:11), re-span the blue marker so it runs only from the axis to the vote-strip lane: `marker.animate.put_start_and_end_on(axis.n2p(17/42), [x, vote_strip.get_top()[1] + 0.15, 0])`, run_time 0.6. Keep that height until the mirror beat.
   - Keep the pooled strip's own boundary on the dashed 50% line.
   - The two readings then sit on two separate lanes, each with its own marker.

2. **[2:23–2:33][Clarity + Visual] The random-shooter 46%/54% expectation appears under the "Cornell, 1985" header with only the GVT citation (frame 2:27.0).**
   - In the `minus8` beat, write the blue "random shooter" label (the one now introduced at 2:33) above the after-3-hits cursor on "For a random shooter" (≈2:21.7).
   - Bring in the M&S citation on "the same crowding" (≈2:23) rather than on "Miller" (2:29).
   - At 2:43, when 49%/45% appear, add two 26 px column heads above the right column: "random" (blue) over 46%/54% and "Cornell" (purple) over 49%/45%.
   - This also removes the colour-only encoding.

3. **[2:34–2:40][Clarity + Motion] The streak-length ghost ticks are undecoded and their 1,000-shot state holds about 1 s.**
   - On "Longer streaks grow the bias", write a 26 px yellow-and-grey legend "● = 1 hit in a row" next to the ● ghost for 1.5 s, then fade it.
   - Centre each dot glyph directly above its own tick rather than to its right, and move the glyphs *with* their ticks (`always_redraw` or group them) instead of dimming them in place.
   - Lengthen the "Longer records shrink it" hold to ≥ 1.8 s. Insert [pause 0.5] after "Longer records shrink it" in narration_text.py and re-time the `minus8` beat.
   - Offset the ●●● ghost so it sits exactly under the −8 marker (both at −7.94), which removes the double stroke.

4. **[3:07–3:13][Audio + Clarity] The reframe sentence is spoken in one breath, and "rows" is heard as "rose".**
   - Change the last sentence to: "A fifty percent shooter [pause 0.3] who averages one half on this test [pause 0.2] is already running hot."
   - This removes the homophone and gives the arrow-to-"hot" animation (3:12) its own breath.
   - Keep the 0.8 s hold after "hot".

5. **[1:50.3–1:52.0][Motion] The pooled strip cross-fades through the vote strip, 12/24 lingers after its strip is gone, and "1/14" touches "100%" (frame 1:51.0).**
   - In the `mirror` beat, first play `FadeOut(VGroup(pool_strip, pool_formula, row_formula), shift=UP*0.3, run_time=0.5)` on "Tails crowd".
   - Then raise the vote strip (0.8 s).
   - No two strips should be superimposed in any frame.

6. **[2:52.3–2:53.5][Motion + Visual] Mid-Write debris on "+12 points" ("+1?" at 2:52.4; stray raised "s" at 2:53.0).**
   - Replace `Write(label)` with `FadeIn(label, shift=DOWN*0.15, run_time=0.6)`, or build "+12 points" as one MathTex with `\text{ points}` so Write strokes left to right without a separate overlapping glyph group.

7. **[1:43–1:50][Audio + Concision] "Pool" is heard as "pull" on the word that names the fix, and "That's the row average, one vote per row" restates the strip.**
   - Narration: "That's one vote per row. [pause 0.12] Count all the flips together first, and you get one half."
   - This cuts 3 words and removes the homophone. Keep the hᵢ/nᵢ flights on "one vote per row".

8. **[0:26–0:41][Hook + Concision] Framing sag; "cold ←" is pre-spent at 0:33.**
   - Drop the "cold ←" half-arrow at 0:31–0:33, leaving "→ hot" only, so "cold" is new at 1:05.
   - Merge "A hot shooter should score above their usual rate. A random one should match it." into "A hot shooter beats their usual rate; a random one should match it." This saves about 1 s.

9. **[0:06.5–0:10.4][Clarity, nit] "average that share over all sixteen sequences", but only 14 sequences have a share.**
   - Change to "Now do that for all sixteen sequences, and average the shares." The 0:47 line ("Two rows … get no score") then reads as the natural detail it is, not a correction.

REACHES 9 IF ALL FIXED: yes, narrowly. Fixes 1–4 are the decisive ones.
- Fixes 1–3 lift Clarity to 9 and Visual to 9.
- Fixes 3, 5 and 6 lift Motion to 9.
- Fix 4 (with 7) lifts Audio to 9.
- That gives 0.15·8.5 + 0.25·9 + 0.15·9 + 0.15·9 + 0.10·9 + 0.10·8.5 + 0.10·9 = 8.875.
- Fix 8 is then needed to move Hook to 9 (+0.075) and fix 7 to move Concision to 9 (+0.05), for about 9.0.

There is no structural problem: the hook, the measured failure, the one picture, the cited payoff and the landing are all in place. What remains is execution.

KEEP:
- The one-vote-per-row strip (1:19–1:43): HHHH's three heads squeezed into one vote, HTTT's lone tails stretched to a whole one, and the yellow sliding exactly onto the 40.5% marker.
- "Test the test on a shooter we know is random" → the live marker sliding 50% → 40.5% → "cold −9.5 points" (0:32–1:07). This is the SMH failure beat, measured.
- The landing (3:01–3:13): the exact cold-open frame, with the 16-row ghost collapsing onto 17/42 where the "?" sat, and a separate shooter dot at ½ marked "hot".
