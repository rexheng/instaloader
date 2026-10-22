# Episode 3, review round 8 (craft critic: visual design, motion, A/V sync)

Evidence. I used the existing `review/` pack, because metrics.json (22:46) is newer than final.mp4 (22:44).

What I read:
- report.md, narration_diff.txt, transcript.txt and transcript_words.tsv
- script.md and narration.txt
- the CHANGELOG round 7 plan
- the round 7 craft review and the substance review's scores
- all 12 contact sheets

Keyframes at full resolution: kf_03, 07, 09, 11, 13, 15, 19, 22, 26, 28, 32, 37, 39 and 40.

Frames I extracted with ffmpeg:
- 1:00.6–1:05.0, every 0.4 s (the guess hold and the 227 swap)
- 1:10.8, 1:11.4
- 1:18.4–1:19.9 (the λ second-row birth)
- 1:26.6–1:27.5 (P(empty) → P(0))
- 1:39.0
- 2:21.0–2:24.4, every 0.3–0.6 s (the null thumbnails)
- 2:51, 2:53
- 3:13.0, 3:15.0, 3:16.4, 3:17.0, 3:17.6 (the limits handover)
- 3:34.3
- deictic checks at 0:27.6–0:28.4, 1:59.2–2:00.6, 2:32.2–2:33.0, 3:13.0–3:15.4 and 3:22.4

I recomputed every number with Python and scipy. Pixel values of the knockout boxes were measured at 3:17.0.

```
EPISODE: 003 — "Which Map Is Pure Chance?"
IDEA: Pure chance leaves empty squares, and the empty squares force hits to pile up elsewhere, so clusters are not evidence of aim. The honest test scores the whole count histogram against Poisson's prediction, and a pattern that is too even is the real fingerprint of a rule.
SCORES: Hook 9 · Clarity 9 · Visual 9 · Motion 8.5 · Audio 8.5 · Concision 9 · Originality 8.5
WEIGHTED: 8.8 (882.5/100)   AFTER CEILING: 8.8 (lowest 8.5 + 2 = 10.5, so the ceiling does not bind)
CAPS: none.
  - Every empirical claim has an on-screen citation held ≥ 3 s:
    - Clarke + Shaw & Shaw, 0:10–0:21 and 2:51–3:24
    - Falk & Konold, 0:47–0:52
    - Evans & Delaney, 3:11–3:24
    - "hits/km²: our count · L. Shaw, 2025 · Zenodo", 3:15–3:24
  - Mechanics are all inside limits, there are 0 banned phrases, and there is no factual error.
  - The layout audit is clean (0 issues in 240 settled frames).
  - The glyph collisions below happen only while objects are moving. Each lasts ≤ 0.5 s, so I score them under Motion, not cap 7. Rounds 6 and 7 used the same convention.
FINAL: 8.8   PASS: no
FACTS:
- 537 hits in 576 squares (Clarke 1946, J. Inst. Actuaries 72:481) | Verified | Clarke 1946; Shaw & Shaw 2019
- "...tended to be grouped in clusters." | Verified | Clarke 1946, p. 481 (facts.md, read on the scan)
- Precise aim would put factories at risk | Verified (paraphrase) | Shaw & Shaw 2019, Significance 16(5)
- λ = 537/576 ≈ 0.93 | Verified (0.9323) | recomputed
- (1 − 1/576)^537 ≈ 0.3933; × 576 ≈ 227 | Verified (0.39333; 226.56) | recomputed
- e^−λ ≈ 0.3937, "almost exactly" | Verified (0.39365) | recomputed
- Convergence dots 0.068 / 0.285 / 0.356 / 0.385 / 0.3933 at n = 1, 2, 5, 20, 537 | Verified | recomputed
- Map A: 222 empty, 39 targets (3+ hits) | Verified from the counts 222/223/92/28/9/2 (576 squares; 527 + two 5-hit squares = 537 hits) | sim.py, recomputed
- 537 − (576 − 222) = 183 extra hits | Verified | recomputed
- Poisson bars 227 / 211 / 98.5 / 30.6 / 7.1 / 1.6; "chance predicts 39" (39.3) | Verified (226.74 / 211.39 / 98.54 / 30.62 / 7.14 / 1.57; 3+ = 39.33) | recomputed
- Whiskers ±12 (bar 0) and ±2.7 (bar 4) | Verified (binomial s.d. 11.73 and 2.65) | recomputed
- χ²_A terms 0.10 + 0.64 + 0.43 + 0.22 + 0.49 + 0.12; running sums 0.10, 0.74, 1.17, 1.39, 1.88, 2.00 | Verified (2.000) | recomputed
- p = 0.74, "three out of four simulated chance maps score worse" | Verified (χ²₄ tail 0.736; facts.md Monte Carlo 74.5 %) | recomputed
- Map B: 109 empty ("half the expected"), 397 single hits, misfit 271.7 ("272") | Verified (109/227 = 0.48) | facts.md, sim.py
- B's rule: no two hits closer than 4/5 of a square | Verified (radius-0.4 discs never overlap) | facts.md
- Clarke's table 229 / 211 / 93 / 35 / 7 / 1; χ² = 1.17, p = 0.88 | Verified (1.169; 0.883) | Clarke 1946, recomputed
- The eye expects chance to look too even | Verified | Falk & Konold 1997, Psych. Review 104(2):301–318
- Aimed at central London (Tower Bridge), tended to fall short, so impact density was lower north of the Thames | Verified per facts.md quotes | Evans & Delaney 2018, Applied Geography 99
- North box fits chance, p = 0.45 | Unverifiable by me: it is the producer's own simulation (200,000 maps), and it is consistent with the merged-tail χ² I checked | facts.md
- 1.9 vs 3.7 hits/km² | 3.7 checks (537/144 km²); 1.9 is the producer's own count and is credited on screen as such | L. Shaw 2025, Zenodo
MECHANICS: runtime 3:34.6 · wpm 159 (speech time; 152 overall) · max silence 1.76 s (planned hold at 0:08.0) · max static 2.57 s · −14.0 LUFS / −1.9 dBTP · leading 0.00 s / trailing 1.60 s · WER 3.1 % (the "bars gap" insert at 2:10.3 is a whisper segment overlap: the word times overlap, 130.32 < 130.80) · 0 banned phrases · 6/6 deictics on an animation
FIXES (highest impact first):
1. [1:19.0–1:19.4][Motion] The second row is born on top of the first.
   Problem:
   - At 1:19.0 a copy of the whole P(empty) row sits over the original: a doubled "=" reads as "≡", plus a doubled fraction bar, "1" and "537".
   - At 1:19.3 the incoming λ/537 flies straight through the 1/576 it is meant to replace.
   - This is the moment the viewer is supposed to see that 1/576 equals λ/537, and it renders as glyph soup.
   Change:
   - Write the frame of the second row, "= (1 − □/□)^537", 1.4 units under row one with Write (0.6 s).
   - Then TransformFromCopy λ from the "λ = 537/576" label into the numerator slot and 537 from the hits counter into the denominator slot, with path_arc = −0.5 so both paths pass right of row one (0.8 s each, lag 0.3).
   - Nothing passes through an existing glyph.
2. [2:21.3–2:23.6][Motion/Clarity] The three null thumbnails collide with their own tags, and the "one map = one entry" mapping is never visible.
   Problem:
   - At 2:21.9 the tags "3.7" and "2.1" cross-fade on top of each other.
   - At 2:23.0 the "2.8" tag is cut by its own thumbnail's bottom border.
   - Each drop takes 0.4 s, and each map adds a sub-pixel sliver to a 20,000-map histogram (frames 2:22.2, 2:23.3), so the drop looks like a vanish.
   Change:
   - Put each tag next_to(thumb, RIGHT, buff=0.15), and fade it out before the drop.
   - Shrink each thumbnail (0.7 s, smooth) into a purple dot (radius 0.06) that lands on the misfit axis at x = its score (3.7, 2.1, 2.8, all right of A's yellow 2.0 marker) and stays.
   - Then grow the 20,000-map bins behind the dots.
   - Adds about 0.9 s, which fits the existing 0.6 s pause plus "simulated chance maps".
3. [3:29.2–3:30.0][Audio] The landing's two sentences run together.
   Problem:
   - The full stop after "looks like." gets 0.4 s (silence 3:29.6–3:30.0), the same as the comma after "map B," (3:31.5–3:31.9).
   - Whisper heard "...what no aim at all looks like if you chose map B. You chose the rule." That parse breaks the closing line.
   Change: in narration_text.py, put [pause 0.9] after "looks like." and keep [pause 0.3] after "map B,". This adds about 0.5 s, so the runtime becomes about 3:35.1, still inside the budget.
4. [3:14.3–3:15.4][Audio/Sync] The density labels arrive about 1.1 s after the word they illustrate.
   Problem: "half" is spoken at 3:14.32, but "· 1.9 hits/km²" and "3.7 hits/km²" are absent at 3:14.8 and complete only at about 3:15.4, after "half as dense" ends (3:15.08).
   Change: start that Write at 3:14.2, on "half" (run_time 0.6).
5. [3:16.6–3:17.6][Motion] The north handover is messy.
   Problem:
   - "north" travels to the chart straight across the "Thames" label (frame 3:17.0: "north" printed over "Thames").
   - "· 1.9 hits/km²" is left stranded with its orphan leading dot for about 0.6 s.
   - The two label knockouts show as faint boxes, 2 levels darker than the background (measured (18,19,24) vs (20,21,26)).
   Change:
   - FadeOut "· 1.9 hits/km²" and "3.7 hits/km²" together with their knockouts in the same AnimationGroup as north's departure.
   - Route "north" with path_arc = 0.6 over the top of the map, or fade "Thames" to 0 at 3:16.4. It is not needed again.
6. [1:01.4–1:04.6][Clarity/Visual] The guess loses its unit.
   Problem:
   - The prediction "empty squares ≈ ?" stands only about 1.2 s (1:01.4–1:02.6) before it becomes "0.3933 × 576 ≈ ?".
   - The yellow label "empty squares" disappears, so the yellow 227 lands at 1:04.6 with no unit.
   Change:
   - Keep the label as the line's left side, "empty squares ≈ 0.3933 × 576 ≈ ?". Use TransformMatchingTex with the "empty squares" glyphs held fixed, so only "?" is replaced by the product and then by 227.
   - The yellow then links straight to the yellow empty outlines on "Map A has 222".
7. [1:26.9–1:27.3][Motion] "empty" and "0" cross-fade in the same slot ("P(mpty0)" at 1:26.9), and a ghost "empty" is left of the P at 1:27.2.
   Change:
   - FadeOut "empty" with shift 0.2·UP (0.3 s).
   - Then FadeIn the yellow 0 with shift 0.2·UP (0.3 s).
   - Then close the gap with the row's left part (0.4 s).
8. [Originality/Clarity, 3:19–3:25] "The aim hides in lambda" has no picture of λ. Only the formula's λ flags (3:22).
   Change:
   - Replace the two hits/km² labels with the quantity the narration names: "λ = 0.48" beside the north box and "λ = 0.93" beside Clarke's area.
     - North: 86 hits in 180 squares.
     - Clarke's area: 537/576. This is the same 2:1 ratio as 1.9 vs 3.7 per km², at the same 0.25 km² squares.
   - On "holds fixed", flag both λ's and join them with the red aim arrow.
   - The limit becomes one image: two areas, each a perfect Poisson, at two different λ's. The aim is the gap between them.
   - This also retires the "hits/km²: our count" citation line, so the frame loses one of its four citation lines.
9. [3:19–3:24][Visual] During the north histogram (kf_37) the ×5 inset holds only three hairline bars (2, 0, 0 squares). It is clutter. FadeOut the inset on "Score the north alone" and bring it back only if the landing needs it.
10. [2:46.5–2:49.0][Visual] Between the aimed map and London, the left half of the frame is near-empty for about 2 s (sheet 2:47) while "In nineteen forty-six, R D Clarke" is spoken.
    Change: start the London rain 0.5 s earlier, overlapping the aimed map's fade, and write "real V-1 hits, 1944–45" on "nineteen forty-six" rather than on "London's real hits".
11. [3:34.0–3:34.6][Visual] Nitpick: the end-card Ω is BLUE, which means "observed counts" for the whole episode. Make it INK, or GRAY #A6ABB5.
REACHES 9 IF ALL FIXED: yes, narrowly.
  - Fixes 1, 2, 5 and 7 remove the last in-motion glyph collisions and lift Motion to 9.
  - Fixes 3 and 4 put every spoken reference and sentence boundary on its beat and lift Audio to 9.
  - That gives 135 + 225 + 135 + 135 + 90 + 90 + 85 = 895, which is 8.95 and rounds to 9.0.
  - Fix 8 is the margin: it gives the honest-limit beat a memorable image (Originality 9 → 905).
  - No structural change is needed. Hook, failure beat, insight picture, payoff and landing are all in place.
KEEP:
- The cold-open A/B pair, "Backwards." and the re-rain of map A. The landing returns to the same pair, now tagged "misfit 2.0" and "misfit 271.7".
- Carried numbers: the 537 counter becomes the exponent, the square's 1/576 flies into P(empty), and the k-hit squares fly count by count into their bars. Every equation term has a visible origin.
- The one-colour-per-sentence discipline that fixed 1:06 (yellow-only empties) and the in-place χ² running sum (2:16–2:19).
```

## Notes behind the scores

- **Hook 9.**
  - The question "Which is chance?" lands at 0:07, with a 1.8 s hold and a grey "A or B?".
  - Map B is the natural wrong pick, and "Backwards." at 0:35 pays it off.
  - The stakes come at 0:10–0:18 with a citation.
  - The landing re-sees the first frame.
- **Clarity 9.** The round 7 gaps are closed:
  - the convergence plot (1:21–1:27);
  - chance's own whiskers (2:14–2:18);
  - the same 16-hit rule for both zooms (kf_07);
  - simulated maps before the null histogram.

  Remaining small rewatch points are the unit drop at the guess (fix 6) and the invisible single-map increments (fix 2).
- **Visual 9.** Round 7's labels-beside-referents fix holds at 3:16.4: "north · 1.9 hits/km²" sits beside its box, and "3.7 hits/km²" sits under "≈ Clarke's area". Other checks:
  - kf_11 has one coloured layer.
  - kf_28's aimed frame stays grey.
  - kf_32 dims the title and "Thames".
  - All settled frames respect the safe area and type sizes.

  What is left is nitpicks (fixes 9–11).
- **Motion 8.5.** The transforms carry meaning almost everywhere: counts fly into bars, numbers are carried, terms flag in place. But four moves still render as overlapping glyphs or stranded parts, at 1:19.0–1:19.4, 1:26.9–1:27.2, 2:21.9–2:23.0 and 3:17.0. Each lasts ≤ 0.5 s; together they keep this off 9.
- **Audio 8.5.**
  - These deictics land within about 0.4 s:
    - "like this one" (ring at 0:28.0)
    - "these purple bars" (bars growing 1:59.6–2:00.0)
    - "a tower" (ring and 397 at 2:32.6)
  - The pace is 159 wpm, and loudness is on target.
  - Docked for the run-together landing (fix 3) and the late density labels (fix 4).
- **Concision 9.** 494 words. I found no sentence whose removal would not lose a step.
- **Originality 8.5.** Clarke's bombs and the "which pattern is random" pair are both textbook-classic. The fresh parts are the measured detector failure (39 false alarms), the too-even fingerprint and the "aim hides in λ" limit, and the last of these still lacks its own image (fix 8).
