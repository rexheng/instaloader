# Round 1 review: craft (visual design, motion, A/V sync)

Evidence: `review/` pack (metrics.json 23:40, newer than final.mp4 23:38). I read report.md, all 13 contact sheets, the transcript, script.md, facts.md and narration.txt. Full-resolution keyframes checked: 0:13.9, 0:36.5, 0:49.3, 1:13.8, 1:15.3, 1:25.1, 1:44.5, 2:04.7, 2:20.2, 2:28.4, 2:43.5, 2:54.0, 3:03.6, 3:15.9, 3:29.0, 3:31.7, 3:42.5, 3:51.3. I also pulled extra frames into /tmp/ep1r1 at 0:00.3, 0:51.0, 1:20.8, 1:57.0, 2:17.0, 2:42.0, 2:47.2, 3:18.0, 3:49.4. I re-ran the invariance test as an independent 2M-line Monte Carlo (/tmp/ep1r1/mc.py).

```
EPISODE: 001 — "Three Right Answers to One Probability Question"
IDEA: "Pick a chord at random" has no answer until you say what is spread evenly. A chord is long exactly when its midpoint falls inside the inscribed circle, so the endpoint, radius and midpoint recipes give 1/3, 1/2 and 1/4 because each scatters midpoints differently. A physical process (Jaynes's straws) fixes the choice, and surveys hide the same choice (a random class vs a random student).
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8 · Motion 8.5 · Audio 8.5 · Concision 8 · Originality 8.5
WEIGHTED: 8.4   AFTER CEILING: 8.4   (lowest 8 + 2 = 10, so the ceiling does not bind)
CAPS: none
FINAL: 8.4   PASS: no
```

## FACTS

| Claim | Status | Source / check |
|---|---|---|
| Side of the inscribed equilateral triangle = r√3; chord long ⇔ midpoint distance < r/2 (the incircle) | Verified | 2√(r²−d²) > r√3 ⇔ d < r/2; inradius = R/2 |
| Endpoints recipe: far arc 120°/360° = 1/3 (0:47, on screen) | Verified | inscribed-angle argument |
| Radius recipe 1/2 = (r/2)/r (2:13); midpoint recipe 1/4 = π(r/2)²/πr² (1:57) | Verified | exact |
| Simulated tallies 0.334 / 0.498 / 0.248 at n = 10,000; "good to about one percentage point" (95% half-widths 0.85–0.98 pt) | Verified | 1.96·√(p(1−p)/n) |
| "Disagree by 25 percentage points" (0.498 − 0.248 = 0.250) | Verified | arithmetic |
| Endpoints histogram: the gold bars stack to 0.334, and the last band holds about 28% ("piles against the rim") | Verified | (2/π)(asin((i+1)/10) − asin(i/10)) |
| Invariance test: midpoint 0.25 → 0.41, endpoints 0.33 → 0.47, radius 0.50 → 0.50 | Verified | my own 2M-line MC: 0.250/0.411, 0.334/0.471, 0.500/0.500 |
| Bertrand 1889, *Calcul des probabilités*; « Aucune des trois n'est fausse, aucune n'est exacte » | Verified | Gauthier-Villars 1889, ch. I §5 (well-known text; matches facts.md H3) |
| Jaynes 1973, *Foundations of Physics* 3(4); invariance argument; straws with C. E. Tyler, 5-inch circle, 128 successful tosses, fit the uniform-distance law | Verified | "The Well-Posed Problem", §5–6 |
| "A skilled tosser could produce other answers" | Verified | Jaynes 1973 §1, §6 |
| Toy classes 10, 10, 100: random class 40, random student 85 | Verified | 120/3 = 40; 10,200/120 = 85 |
| Feld & Grofman 1977, *Research in Higher Education*: Stony Brook spring 1974, 737 classes, 40 per class, 147 as experienced by students | Verified | 6(3):215–222; consistent with 40.5·(1 + 65.8²/40.5²) ≈ 147 |

No wrong, fabricated or uncited empirical claims. Every empirical claim has a bottom-left citation that is held for at least 3 s.

## MECHANICS

runtime 3:51.3 · wpm 161 (speech time; 152 overall) · max silence 1.92 s (0:07.7, the planned prediction pause) · leading 0.00 s / trailing 1.81 s · max static 3.0 s (0:16.7) · −14.0 LUFS / −1.6 dBTP · 0 black frames · WER 2.0% · 0 banned phrases. The layout audit reports 0 issues in 252 frames. No mechanical cap triggered. The runtime is 9 s under the 4:00 limit.

**Transcript and sync check.** Each deictic lands while its referent is visible and highlighted:
- "this circle" (0:00) and "this triangle" (0:05)
- "this far arc" (0:43, the arc lights at 0:44)
- "this gold circle" (1:43)
- "land here" (1:48, the gold circle copies land in the three panels)
- "this circle, with a quarter of the area" (1:55)
- "rim, radius, area" (2:23–2:27, each lights in its own colour)
- "both circles at once" (2:43–2:45, the crossing dots appear)

There are two intentional prediction holds: "Pick a number" is followed by 1.9 s, and "Where will they crowd?" by 1.6 s, with the panel collapse arriving only at 2:07. "chord" heard as "cord" is a homophone, not an error. "Jaynes" heard as "Jane" at 2:30.9 suggests a swallowed final s (see fix 9). There are no §4 phrases or patterns. "Case closed, until you code it a second way" is the one dry line, and it works.

## What the frames show (flipbook notes)

- **0:00–0:24 Cold open and stakes.** The first frame is concrete: circle, triangle and chord. The question is built as math out of the two actual segments, P(— > —) = ?. That is a strong, original hook glyph. "at random" is underlined on its words.
- **0:24–0:50 Naive build.** One chord turns gold, then 10,000 rain as a texture while a live tally climbs. The triangle rotates so a vertex sits on the first point, the far arc lights, and 120°/360° is built from the arc. Good.
- **0:50–1:25 Fail.** The panel shrinks left carrying its tally, and two more recipes rain. Dots, error bars and the "25 points" brace make the failure measured, in Stuff Made Here fashion. The French quote is two short lines (8 words), not a slide.
- **1:25–2:28 Insight.** This is the best stretch of the episode. The midpoint slides, the chord shrinks, r/2 appears and the incircle draws. Each panel collapses chords to midpoints, histograms grow, and the formulas are built from the outlines. The endpoint program's gold bars stack into a 0.334 column. Then rim, radius and area light in recipe colours. Every motion encodes a relation.
- **2:28–3:16 Payoff 1 (Jaynes).** The idea is right, but this is the weakest-looking stretch (see fixes 1–3). At 2:42–2:48 there are four circle outlines (big, its incircle at about 50% instead of the scripted 20%, small, small incircle) plus a faint big triangle and straws, and the dimmed big incircle cuts through the small circle and its incircle. At 2:49–2:57 the three program rains are spaghetti: you cannot read the per-line judging on the small circle, so the scoreboard numbers carry the whole argument. At 3:00–3:11 the real experiment is just two text lines over a dimmed simulation.
- **3:16–3:38 Payoff 2 (class size).** The bars widen to "width = students" while the mean line rises continuously from 40 to 85. That motion *is* the weighting argument, and it is excellent. Stony Brook sits in its own framed block, the example dims to 30%, and the citation is on screen.
- **3:38–3:51 Landing.** The episode returns exactly to the first frame, and the opening chord turns gold with its midpoint inside the incircle. 1/4, 1/3 and 1/2 appear on a 0–1 line, and 1/2 gets a "straws" tag. The frame holds two separate focal groups (the number line and the 40/147 rows), and at 3:51 the "random class" label is grey while "random student" is white.

## Why each score

- **Hook 8.5.** The concrete puzzle is in the first frame and the viewer commits by 0:07 with a held pause. The ending re-sees the first frame. Tension sags in the double payoff (Jaynes 48 s, then a second domain for 22 s), so it misses the 9 anchor ("tension rises through build and fail") by a little.
- **Clarity 8.5.** The midpoint picture is the canonical way to see this, and every number checks. Three things keep it from a 9:
  - The invariance test (2:42–3:00) cannot be read from the picture, only from the table.
  - "Matched the radius program's spread of chord lengths" (3:07) names a distribution that is never drawn. The episode plotted midpoint distances, never chord lengths, so this is a notation jump.
  - The class-size bridge ("Surveys hide the same two words", 3:16) is asserted rather than drawn as the same "what is spread evenly" picture.
- **Visual 8.** The palette is semantic and consistent: gold means long, and blue, green and purple are the three recipes. Typography is clean and the safe area is respected. There are more than two minor issues:
  - 2:42–2:48 overlapping outlines (above).
  - Scoreboard column headers are bare circle icons, about 60 px and 36 px across (2:31–3:00, kf 2:43.5).
  - Rain spaghetti at 2:49–2:57.
  - The landing has two focal groups with inconsistent label brightness (3:51).
  - The Bertrand citation sits about 27 px under the "0.2" tick label (kf 1:13.8).
  - The histograms have no y scale (2:09–2:28).
- **Motion 8.5.** Objects persist and transform, formulas grow from their referents, the bars stack, and the mean line rises continuously. Three things fall short:
  - The real-experiment beat (3:00–3:11) is text fading in over a dimmed rain.
  - The invariance rains are closer to texture than to argument.
  - The panel triangle rotates back to upright in mid-shrink at 0:49–0:52, a rotation that means nothing.
- **Audio 8.5.** Pace is on target, loudness is exact, deictics land and the pauses are intentional. Holding it back: the likely "Jaynes" → "Jane" swallow at 2:30.9, and long unpunctuated Whisper runs at 1:48.9–2:02.7 and 2:19.7–2:36.7, which hint at some flat stretches I cannot confirm from frames.
- **Concision 8.** At 3:51 it is near the top of the window. There are two payoffs plus the skilled-tosser coda. "Same circle, same gold rule" (0:58) repeats what the frame already shows. The 2:31–2:41 straws "– → ? → ? = ?" scaffolding takes about 10 s before the test starts. Less than 10% is removable, with one slack beat.
- **Originality 8.5.** The unification of the three recipes through midpoints is known (it is on Wikipedia). The fresh, shareable parts are the on-screen invariance test (one rain judged on two circles) and the tie to the class-size paradox.

## FIXES (highest impact first)

1. **[2:40–2:59][Visual/Clarity] The invariance test is unreadable clutter.**
   - At 2:40, when the small circle appears, fade the big triangle and the big gold incircle to 0 (they currently sit near 50% and cut through the small circle at kf 2:43.5 and frame 2:47.2). The small circle and its gold incircle become the only gold-and-white pair inside the big circle.
   - For each program rain (2:48–2:57), draw the big-circle chords at ≤ 15% opacity. Draw only the segments inside the small circle at full strength (gold or grey under the small circle's rule), and cap each program at about 30 visible lines so individual verdicts can be read.
   - Hold each finished row for 1 s before the next rain starts.
   - Expected gain: Visual +0.5, Clarity +0.5.
2. **[3:00–3:11][Clarity/Motion] The real experiment has no picture, and the straws "?" is never answered by real data.**
   - On "spread of chord lengths", grow a small 10-bin chord-length curve on the right: the radius program's predicted density, labelled "radius program: predicted chord lengths". Under it, tag "128 real tosses fit this · Jaynes & Tyler" (no fabricated bars, since their data were not published).
   - On "matched", turn the straws row's "?" into "≈ radius" with the green row flagging. Only after that may the "?" hand over to the "simulated" skilled-tosser share at 3:12.
   - This removes the current reading that a simulated 0.50 is what answered the question.
3. **[2:31–3:00][Visual] The scoreboard column heads are tiny icons (about 60 px and 36 px) under a generic "gold share".**
   - Replace them with text heads "big circle" / "small circle" (Text font_size ≥ 26) centred over the two number columns, or keep the icons at ≥ 0.6 units with those words beneath.
   - Without readable heads, "0.25 ≠ 0.41" relies on the viewer remembering which column is which.
4. **[3:16–3:29][Clarity] The class-size beat claims the "same two words" link but never draws it.**
   - When the dots appear under the bars (3:23, one per class), add a short label "spread evenly over: classes" where the 2:23 "rim / radius / area" words sat.
   - On "Pick a student at random" (3:26), transform that label to "spread evenly over: students" as the dots split.
   - This makes the bridge a visible echo of 2:20–2:27 instead of an assertion.
5. **[3:38–3:51][Visual/Hook] The landing has two focal groups and mismatched label brightness.**
   - At 3:51 "random class" is grey while "random student" is white. Bring both labels to the same ink on "who's picked" (the numbers already match).
   - Place the two rows so their numbers right-align under the 0–1 line's right end, giving one tidy block rather than a second centre of mass.
   - Keep the 1/2 "straws" tag.
6. **[0:58–1:00 and 2:31–2:41][Concision] Cut about 6 s.**
   - Delete "Same circle, same gold rule." The frame already shows the same circle and gold chords.
   - Collapse the straws row's "– → ? → ? = ?" sequence into a single "? = ?" that appears on "where the circle sits or how big it is".
   - Target runtime ≤ 3:45.
7. **[2:09–2:28][Visual] The histograms have no y scale.** Add one y tick, "10%", on the radius-program histogram (its bars are 0.095–0.104). "Every ring gets an equal share" then reads as a number, and the chart meets §5's axis rule.
8. **[1:11–1:25][Visual] The Bertrand citation sits about 27 px below the "0.2" tick label (kf 1:13.8).** Raise the number line by 0.25 units, or shift the citation down to y = −3.05, so the gap is ≥ 0.3 units.
9. **[2:30.9, 3:00.1, 3:12.4][Audio] "Jaynes" was transcribed as "Jane" once and "Janes" twice.** Respell it in narration_text as "Jaynz" (or add a Kokoro phoneme override) so the final /z/ is voiced consistently, then re-check with Whisper.
10. **[0:49–0:52][Motion] The left panel's triangle rotates back to upright while the panel shrinks (frame 0:51.0).** Either do the rotation during the 0.5 s fade of the sweep and arc (before the shrink), or let the panel keep the rotated pose. A rotation that carries no meaning should not happen in flight.

## REACHES 9 IF ALL FIXED: yes

The structure is right: a cold-open commit, a measured failure, one insight picture with formulas grown from it, a cited payoff, honest limits, and a return to the first frame. Every remaining deduction is local craft. Fixes 1–4 lift Visual and Clarity to 9, fix 6 lifts Concision to about 8.5–9, and fixes 2 and 10 lift Motion to 9. That puts the weighted score at about 9.0–9.1.

## KEEP

1. 1:25–2:28: midpoint slide → incircle → chords collapsing to midpoints → histograms → outline-to-term formulas → gold bars stacking into 0.334. This is the episode's proof, and it must survive intact.
2. 1:15–1:25: the measured failure, three dots with 95% error bars and the "25 points" brace.
3. 3:25–3:29: class bars widening to "width = students" while the mean line rises continuously from 40 to 85, plus the landing's exact return to the opening frame.
