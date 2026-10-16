# Round 1 review: substance (science and story editor)

Evidence: `review/` pack (metrics.json 10:13 is newer than final.mp4 10:11, so I used it as is). I read report.md, all 11 contact sheets, 13 full-resolution frames (kf_01, 03, 07, 09, 12, 13, 15, 25, 29, 35, 38, 40, plus my own extractions at 1:51.0, 1:51.5, 2:00.0, 2:24.6 and 2:54.8), the transcript, narration.json, script.md and facts.md. I re-ran `sim.py`, ran my own invariance simulation (below), and checked the Jaynes and Bertrand citations against the primary texts with web search.

```
EPISODE: 001: "Three Right Answers to One Probability Question"
IDEA: "Pick a chord at random" has no answer until you say what is spread evenly; the three classic recipes spread chord midpoints differently around the one inscribed circle that decides "long", so they give 1/3, 1/2 and 1/4.
SCORES: Hook 8 · Clarity 8 · Visual 8 · Motion 8 · Audio 8 · Concision 8 · Originality 7
WEIGHTED: 7.9   AFTER CEILING: 7.9  (lowest 7 + 2 = 9, not binding)
CAPS: none. Notes: the 1:50.6–1:51.4 transform blob crosses the "0.248" label only while it is moving, and the destination layout is clean, so I did not apply the overlap cap (fix 3). Every empirical claim has an on-screen citation. No banned phrases.
FINAL: 7.9   PASS: no
```

## FACTS

| Claim | Status | Source / check |
|---|---|---|
| Side of the inscribed equilateral triangle = r√3; chord length L = 2√(r²−d²); L > side ⇔ d < r/2; the r/2 circle is the triangle's incircle | Verified | Re-derived. `sim.py`: side 1.73205, chord at d = 1/2 is 1.73205, inradius 0.5 |
| Random endpoints → 1/3 (vertex on first point, far arc 120°/360°) | Verified | Re-derived (inscribed angle) |
| Random radial point → 1/2; random midpoint → π(r/2)²/πr² = 1/4 | Verified | Re-derived |
| Simulated tallies 0.334 / 0.498 / 0.248, n = 10,000 each | Verified | Re-ran `sim.py` (seed 1889): 0.3343 / 0.4976 / 0.2482 |
| "Each tally is good to about one percentage point" | Verified | 95% half-widths 0.92 / 0.98 / 0.85 pp |
| "They disagree by twenty-five" (brace "0.25", 1:19) | Verified, but the unit is missing in the narration | 0.4976 − 0.2482 = 0.249. Should say "percentage points" (fix 5) |
| "Every ring gets an equal share, and inner rings are small" (radial recipe) | Verified | d ~ U(0, r), so areal density ∝ 1/d. On-screen histogram is flat |
| Endpoint recipe "piles them against the rim" | Verified | d-density (2/π)/√(r²−d²); last band 0.284 in sim. Not derived on screen (see Clarity) |
| Bertrand published it in 1889, *Calcul des probabilités* | Verified | Gauthier-Villars 1889, ch. I §5; e-rara scan and secondary sources agree |
| « Aucune des trois n'est fausse, aucune n'est exacte » | Verified, verbatim | The full sentence continues "…la question est mal posée". Matches the scans found by search |
| Jaynes 1973 argued that a physical process (straws) picks one; *Foundations of Physics* | Verified | "The Well-Posed Problem", Found. Phys. 3(4):477–492, 1973 (bayes.wustl.edu/etj/articles/well.pdf) |
| "Only the radius program passes that test" | Verified | Jaynes §5: B eliminated by scale invariance, C "eliminated for lack of translational invariance", f = 1/(2πRr) = solution A |
| Jaynes and Charles Tyler, broom straws, standing height, 5-inch circle, 128 tosses fit | Verified, but imprecise | Jaynes §6: "tossing broom straws from a standing position onto a 5-in.-diameter circle … 128 successful tosses confirmed Eq. (13) with an embarrassingly low value of chi-squared". On screen "128 real tosses" (2:47) drops "successful": 128 is the number of straws that crossed the circle, not the number thrown. The test was the full chord-length distribution in ten bins, not only the 1/2 (fix 4) |
| "A skilled tosser could produce other answers" | Verified | Jaynes §1 and §6 ("a very precise machine … any distribution of chord lengths we please"). Jaynes also stresses that the skill needed is impractically large; the episode is fair to him |
| Spinner picking both ends at random → 1/3 | Verified | Same as recipe 1. Correctly not attributed to Jaynes |
| "Whatever number you picked … some way of drawing chords makes it right" | Verified | Constructive: choose any distribution of d with P(d < r/2) = p |

No Wrong or Fabricated claims. Two items are imprecise wording ("128 real tosses", "disagree by twenty-five").

## MECHANICS
runtime 3:12.5 · wpm 160 in speech (155 overall, 496 words) · max internal silence 1.92 s (the planned "Pick a number" hold, 0:07.7–0:09.6) · leading 0.00 s, trailing 1.69 s · max static 2.87 s · −14.0 LUFS / −1.6 dBTP · 0 black frames · WER 0.8%. The only differences from the script are "Jaynes" heard as "Janes" (a homophone, so the pronunciation is correct) and "Change" missing at 2:54.6. narration.json puts "Change" at 174.58–174.98 s, and the waveform has speech energy there (−13 dBFS), so the word is present but its onset is weak. No caps triggered.

## Transcript and slop audit
- Banned phrases: 0. Banned patterns: none. There is no "it's not just X", and every question is followed by a hold rather than a second question ("What's the chance…? Pick a number." and "Where will they crowd? [1.5 s]"). There are no empty superlatives, and no recap ending.
- The narration has a specific voice and points at things on screen ("this far arc", 0:41, lands as the arc lights at 0:43; "this gold circle", 1:37). It reads as written by someone who understands the problem, not as AI filler.
- Hook: the circle and chord are on screen at 0:00, the question at 0:03, and "Pick a number" at 0:07 with a 1.9 s hold. It lands well before 0:15.

## Story
The spine is good. One puzzle drives the whole video: build (0:20), exact check (0:35), measured failure with error bars and "none of the code has a bug" (1:21), the one unifying picture (the incircle as the midpoint test, 1:21–2:21), payoff (Jaynes), and a landing back on the first frame with the number line swept from 0 to 1. The closing line reframes the opening ("whatever number you picked … makes it right"). That is the BAR §6 shape done properly.

Where it loses tension:
1. **2:21–2:39, the Jaynes "test" is asserted, never shown.** "The answer can't depend on where it sits or how big it is. Only the radius program passes that test." The viewer only sees the radius rain pass (the circle slides and grows while the tally holds at 0.50, 2:33–2:37). They never see the other two fail, and a sharp viewer will object that 1/4 doesn't depend on where the circle is either. The real point is that one rain of straws has to be consistent on every circle at once. This is the payoff's central logical step, and it is the one place the episode tells instead of shows. I checked the claim numerically (my `inv.py`, 2 M lines per recipe, same rain judged on a sub-circle). Radial rain: 0.500 on the big circle, 0.500 on a concentric half-size circle, 0.499 on a circle of radius 0.5 centred at (0.4, 0). Midpoint rain: 0.250 / 0.250 / **0.411**. Endpoint rain: 0.334 / **0.483** / 0.471. This is exactly Jaynes's result (C fails translation, B fails scale), and it would make a strong image.
2. **The stakes are generic and never cashed in.** "Every survey and simulation leans on them" (0:17) is the only data-science stake, and the payoff is a 1970s physics-of-straws result. For a data-science and CSS series, episode 1 should land one real sampling consequence of "what is spread evenly". The closing line gestures at it ("every random sample has a recipe"), but nothing concrete on screen backs it.
3. The spinner beat (2:55–3:00) re-proves recipe 1. It is the one slack sentence.

## Clarity
Concrete before abstract throughout. Each recipe is shown being executed, and the 1/3 is checked exactly (120°/360° built from the gold arc, 0:45). The chord-shrinks-as-the-midpoint-slides move (1:21–1:31) to the gold incircle (1:33) is the canonical way to see this problem. Deductions: (a) the Jaynes invariance step is asserted (above); (b) "the endpoint program piles them against the rim, which gives the third we found" (2:08) is asserted. The histogram spike shows the pile-up, but nothing connects it to 1/3 the way π(r/2)²/πr² and (r/2)/r were connected; (c) "disagree by twenty-five" has no unit (1:17); (d) "Change the machine" (2:54) refers to a machine that was never introduced, since the tosser was a person.

## Visual (§5)
The palette is semantic and consistent all the way through: gold means long, blue/green/purple are the three recipes, grey is short or context. There is one focal point per frame, and citations are bottom-left above y = −3.2 (≈ −2.96 units, measured at 0:13.9 and 2:24.6). Measured type sizes pass: tick labels ≈ 28 px, citations ≈ 26 px cap height. Issues:
- 1:50.6–1:51.4: `TransformFromCopy` from the two filled disks into π(r/2)²/πr² morphs into a lumpy lilac and gold blob that covers "0.248" and the end of "…from center" (frame at 1:51.0). It is the ugliest frame in the video, at the moment the main equation is born.
- 1:11–1:21: the French quote is one 8-word block (limit 7). With the three recipe labels, "gold share" and the citation, about 21 words of prose are on screen (limit 12).
- 2:54.8: "random radial point 1/2" is still at full green next to a tally of 1.000 while the skilled-tosser pull runs. For about 0.5 s the screen contradicts itself.
- 1:23–1:40: the enlarged circle is panel 2, but its green label vanishes behind it. The analysis is recipe-agnostic, yet visually it belongs to recipe 2.
- The 10,000-line textures in the panels (0:47–1:43) read as fur. They are fine as context, but they carry little information compared with the 240-dot midpoint plots that replace them.

## Motion
Objects persist and transform with meaning: the triangle rotates so a vertex sits on the first point (0:37), the big circle shrinks into panel 1 and drops its tally onto the shared number line (0:47), error bars grow and a brace measures the gap (1:15–1:19), chords collapse to their midpoints (1:45, 2:01, 2:09), straws are pulled to the centre (2:51–2:55), and the landing reuses the opening chord, which now shows its midpoint inside the gold circle (3:07). The longest static stretch is 2.87 s. Deductions: the 1:51 morph described above, and the Jaynes section, where motion illustrates the passing case only.

## Originality
This exact problem with these three methods is a canonical example with a high-profile treatment: Numberphile's "Bertrand's Paradox (with 3blue1brown)", Dec 2021, about 1.4 M views. The episode's additions are real: a measured failure with confidence intervals, a single incircle test unifying all three, and Jaynes and Tyler's actual straw experiment. But until the invariance test is shown, or the episode lands a data-science consequence, it is a very good version of a known video, not a new angle.

## FIXES (highest impact first)
1. **[2:21–2:39][Clarity/Motion/Originality] The Jaynes invariance test is asserted, not shown.** After "…how big it is" (2:35), keep the current straw rain and draw a second, smaller circle (radius 0.5 R, centre offset 0.4 R to the right) inside the big one. Give it its own tally and show that the same straws give 0.50 on both circles. Then replay two 3 s mini-rains with the same layout: a "random midpoint" rain (uniform midpoints for the big circle) with big/small tallies **0.25 / 0.41**, and a "random endpoints" rain with **0.33 / 0.47**, each tally coloured by its recipe and the small-circle number flagged. Narration (about 14 words): "Rain midpoints evenly on the big circle, and the small one disagrees. Only one rain agrees everywhere." Then cut "Only the radius program passes that test." Numbers come from a 2 M-line simulation (uniform-midpoint rain: 0.250 on the big circle, 0.411 on the offset half-size circle; endpoint rain: 0.334 / 0.471; radial rain: 0.500 / 0.499). Label "simulated". This turns the one asserted step into the episode's most memorable image.
2. **[0:16–0:20 and 2:54–3:00][Hook/Originality] The data-science stakes are never cashed in.** Replace the spinner sentence (2:54–3:00, which re-proves 1/3) with an 8–10 s social-science consequence of "what is spread evenly". The class-size paradox fits: three classes of 10, 10 and 100 students. Pick a random *class* and the average size is 40. Pick a random *student* and ask about their class, and the average is (10·10 + 10·10 + 100·100)/120 = **85**. Show it as bars that re-weight, with citation "Feld & Grofman, 1977 · Research in Higher Education" (verified: 6(3):215–222). Then change 0:17 to name it: "Every poll, every sample, every simulation has to say what's spread evenly." This also gives the closing line ("every random sample has a recipe") something concrete to point back to.
3. **[1:50.6–1:51.4][Visual/Motion] The disk-to-equation morph is a lumpy blob over "0.248" and the axis caption.** Copy the gold disk and the purple disk, scale each to about 0.35 units, and move them along a path that stays below y = −1.0 to the numerator and denominator slots (0.8 s). Then `ReplacementTransform` (or `FadeTransform`) each icon into its `MathTex` term (0.6 s). Nothing should pass over the tally labels.
4. **[2:41–2:49][Clarity/Correctness of wording] "128 real tosses" overstates the count; Jaynes reports 128 *successful* tosses, tested on the whole chord-length distribution.** On screen: "128 straws that crossed it". Narration: "…and the hundred and twenty-eight straws that crossed it matched the predicted spread of chord lengths." Optionally, while the simulation is dimmed, draw Jaynes's predicted chord-length curve (Eq. 13, the radial recipe's length density L/(2R√(4R²−L²))) as a ten-bin histogram, without fabricated observed bars, since their data was not published.
5. **[1:17][Clarity] "They disagree by twenty-five" has no unit.** Change it to "They disagree by twenty-five percentage points, and none of the code has a bug."
6. **[2:08–2:13][Clarity] The endpoint program's 1/3 is asserted from the pile-up.** While "piles them against the rim" plays, colour the endpoint histogram's five bins inside r/2 gold and sum them on screen: the gold bars `TransformFromCopy` into "0.334 ≈ 1/3" next to the existing tally. This matches how 1/4 and 1/2 were derived.
7. **[2:54][Clarity] "Change the machine" refers to a machine that was never introduced.** If the spinner beat survives fix 2, say "Swap the tosser for a spinner that picks both ends at random, and it's one third again."
8. **[1:11–1:21][Visual] The word load is about 21 words, and the quote is an 8-word block.** Dim the three recipe labels to 30% while the quote is up, and split the quote into two blocks of 4 words, « Aucune des trois n'est fausse, » and « aucune n'est exacte », the second revealed on "none is right" (1:12.6). That keeps each block under 7 words.
9. **[2:51.0–2:55.0][Visual] "random radial point 1/2" stays at full colour beside a tally of 1.000.** Dim the label and its 1/2 to 30% on "A skilled tosser" (2:51.0), before the pull starts.
10. **[1:23–1:40][Visual] The zoomed circle loses its green label and so reads as recipe 2.** Fade panel 2's green tally and label out together with the other panels as it enlarges, so the zoomed circle reads as "any chord" (ink only), then restore them at 1:41 when the gold circle copies into all three panels.

**REACHES 9 IF ALL FIXED: yes, narrowly.** The structure is right: hook, measured failure, one-picture insight, cited payoff, landing on the first frame. Polish fixes 3 and 5–10 alone top out around 8.3. Reaching 9 requires fixes 1 and 2 as *visual* beats: the same-rain/two-circles demonstration turns the payoff from an assertion into the episode's signature image (Clarity 9, Originality 8–9), and a concrete sampling consequence pays off the data-science stakes (Hook 9). Without those two changes this remains a very good retelling of a known Numberphile and 3b1b topic.

**KEEP:**
1. The measured failure at 0:47–1:21: three tallies dropping onto one "gold share" axis, ±1-point error bars, the 0.25 brace and "none of the code has a bug". This is the StuffMadeHere move done right.
2. The midpoint-slide to incircle insight (1:21–1:41) and the chords collapsing to midpoints in all three panels, with gold/grey dots and the derived 1/4 and 1/2.
3. The landing: the opening chord returns, shows its midpoint inside the gold circle, and the number line is swept from 0 to 1 under "whatever number you picked … makes it right".
