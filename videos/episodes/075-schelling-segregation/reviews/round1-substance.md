EPISODE: 075 — "Mild Preferences, Extreme Segregation"
IDEA: In Schelling's model, households that need only a third of their neighbors to match still sort a town to three-quarters matching, because each departure tips a neighbor who was content. So a segregated map cannot tell you what its people wanted.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8 · Motion 8.5 · Audio 8 · Concision 8 · Originality 8
WEIGHTED: 8.3   AFTER CEILING: 8.3 (lowest 8 + 2 = 10, so the ceiling does not bind)
CAPS: none. Notes on the caps I considered: both empirical claims have on-screen citations held ≥ 3 s (2:35–2:55, 3:08–3:15). No banned phrases. The stale inequality at 1:40.6–1:42.0 and 1:44.2–1:44.9 is true arithmetic shown about 1.4 s before the narrated update, so I scored it as a clarity/motion defect and did not apply the error cap. The "random mix" label sitting on the translucent Schelling band at 2:41–2:55 is still legible, so I scored it as a visual fix, not cap 7.
FINAL: 8.3   PASS: no

## FACTS (every number recomputed or traced to source)

I loaded `sim.py` read-only in a separate process. sim_output.txt and my recomputation agree.

| Claim | Status | Source / check |
|---|---|---|
| Final town: on average three quarters of neighbors match; meter 76% | Verified | sim seed 3 final share 0.7553 |
| Rule: stay if ≥ 1/3 of neighbors match; "happy to be outnumbered two to one" | Verified | s/(s+d) ≥ 1/3 ⇔ d ≤ 2s. Magnifier at 0:17–0:22: 2 gold, 4 blue, 2 empty, so 2 of 6 (I counted it in kf_06) |
| Random start: about half of neighbors match; meter 50% | Verified | 0.4992 |
| 238 unhappy, "about one in six" | Verified | 238/1440 = 16.5%; 1/6 = 16.7% |
| Round one: 200 moves, share jumps to 64% | Verified | 200 moves; 0.6441. The 38-move gap is real (38 households became content before their turn) but never explained on screen. See fix 3 |
| Counter reads 74 after round one; "most… content before round one and never moved" | Verified | 74; 67 of 74 were content at start, 68 did not move |
| Corner chain: B 3/8 ≥ 1/3 → 2/7 < 1/3 after A leaves; C, then D, tip in rounds 2 and 3 | Verified | I counted B at 1:24 (3 gold of 8) and C at 1:39 (3 gold of 8) tile by tile in the full-resolution frames; matches sim chain output |
| "Until round seven, when nobody wants to move"; 76% | Verified | unhappy counts by state: 238, 74, 41, 16, 9, 2, 1, 0 |
| Chart: 30 towns per demand, 0–60% | Verified | plotted cluster heights match sim means (50.0, 51.4, 56.9, 58.4, 74.9, 82.2, 86.7, 96.5) |
| Same town at 1/4 → 58% | Verified | 0.5787 |
| "At a quarter, 2/7 is enough, and that chain never starts" | Verified (2/7 = 0.286 ≥ 0.25); incomplete as an account of the jump | I recomputed with sim.init(3): **95** households are unhappy at the start at 1/4, against **238** at 1/3. Most of the jump comes from 2.5× more initial movers, not only from the chain. See fix 4 |
| "Everyone in this simulated town chose where to live" | Imprecise | Total moves are 200+72+41+16+9+2+1 = 341, so at least 1,099 of 1,440 households never moved from their random start. See fix 7 |
| Schelling 1971 ran it "by hand, on a checkerboard" | Verified | Schelling, *J. Math. Sociology* 1(2):143–186, p.154 "like a checkerboard", p.155 "done by hand and eye" (I read the PDF text) |
| His households moved to the nearest satisfying square, on emptier boards | Verified | p.155 "moves to the nearest vacant spot that…"; "25% to 30% vacancies"; p.158 "blank spaces usually equal to about 30%" |
| "There the jump came later, between about a third and a half" | Verified | p.158–159: "slight when the demand is for about one-third… striking when… one-half"; "a rapidly rising function of demands in the range from about 35% to 50%" |
| Quote: "inferences about individual motives can usually not be drawn from aggregate patterns" | Verified, verbatim | Abstract, p.143 |
| 1930s federal lending maps increased racial segregation for decades | Verified | Aaronson, Hartley & Mazumder 2021, *AEJ: Economic Policy* 13(4):355–92. Abstract: "increased racial segregation in later decades." "One study" is appropriately hedged |
| Title "Extreme Segregation" (end card 3:22) | Overclaim | 76% vs a 50% baseline is substantial, not extreme. Schelling himself called the one-third result "slight". See fix 8 |

## MECHANICS
runtime 3:23.5 · wpm 157 (speech) · max silence 1.97 s (prediction hold 0:09.6–0:11.6, intentional) · leading 0.0 s / trailing 1.73 s · max static 3.33 s (2:34.5, 2:44.4) · −14.0 LUFS / −1.6 dBTP · WER 0.4% (only "thirties" heard as "thirty s" at 3:10) · 0 banned phrases. No mechanical caps.

## Transcript and slop scan
I found no §4 phrases. There are no question chains: "How much matching do they demand?", "Is it still content?" and "Why the jump?" each stand alone. "Why the jump?" (2:21) is a self-answered question, close to the fake-reveal pattern. It is allowed once, but don't add another. The voice is specific, the sentences are concrete, and nearly every line points at something on screen ("this counter", "this gold household", "this neighbor moved away"). The deictics land within ±1 s of their highlight. The only stretch is "That town is one point on this chart" (2:02.5–2:06): the dot is not drawn until about 2:06.5. The hook is a misconception with a commit: "? demanded" at 0:07.7, then a 2.0 s hold, then "Just a third." at 0:11.5. The tension question comes at 0:27.6–0:31.9. The ending returns to the cold-open frame with the marker back at "?" (3:15–3:22).

## FIXES (highest impact first)
1. [1:40.6–1:42.0 and 1:44.2–1:44.9][Clarity/Motion] When B's tile empties ("after round 2"), C's patch shows 2 gold of 7, but the formula still reads "3/8 ≥ 1/3" for about 1.4 s. The same thing happens for D at 1:44.2–1:44.9: C has gone and the formula still shows 3/8. facts.md row 14a claims this never happens. **Change:** in the same `AnimationGroup` that fades the departing tile to empty, replace the relation with a "?" and set the stale numerator and denominator to 30% opacity, as you already do for A at 1:26–1:29. Then run the 3→2, 8→7, ?→< transform on "drops to two sevenths" (1:41.5) and "tips" (1:44.8). Alternatively, delay the tile-empty animation so it fires with the formula transform.
2. [2:05–2:55][Visual] (a) The 30 semi-transparent dots per demand level overlap into fuzzy white blobs (kf_27). Draw them at radius 0.05 with ±0.4 % horizontal jitter, then add a solid INK mean tick and a thin min–max whisker per column. (b) The "Schelling's boards" band is unlabeled as to meaning and low-contrast. Relabel it "Schelling's jump: 35–50%" and raise its fill to about 35% opacity. (c) Move the "random mix" label to x ≈ 5–20 (left of the band) so it no longer sits on the band at 2:41–2:55.
3. [0:46.7–1:01][Clarity] The narration says "move each of them" (238), then "Round one takes 200 moves". The gap of 38 is unexplained, and it is the first instance of the episode's own mechanism. **Change:** as the counter passes through the round, flash a small GRAY label "38 fixed by a neighbor's move" next to the counter for 2 s. Or append to the narration: "Thirty-eight didn't need to: a neighbor's move fixed them first."
4. [2:21–2:32][Clarity] "Why the jump?" is answered with one household's chain. That is a good illustration, but it is not the aggregate reason. I recomputed (sim.init(3)) and the same town starts with **95** unhappy households at 1/4 against **238** at 1/3. **Change:** before "Back in our corner", put the two counts under the thumbnails ("unhappy at start: 95" / "238", RED) and say: "At a third, two and a half times as many start unhappy, and each one can start a chain like this." Then keep the 2/7 vs 1/4 patch as the mechanism.
5. [0:13–0:22][Clarity] The rule silently excludes empty squares: the viewer sees 8 squares, 2 empty, and "2 of 6". The 3/8 → 2/7 denominator change at 1:29 depends on this. **Change:** "Each household checks the occupied squares around it…". In the magnifier, mark the two empties with a thin GRAY "×" while "of 6" writes.
6. [0:00–0:05][Hook/Visual] For the first 5 s the board sits left with the right half of the frame empty, and the meter only starts filling at 0:05 (kf_01). **Change:** have the meter and the "? demanded" marker present by 0:01.5 and fill to 76% on "three quarters". Or start the board centered and slide it left as the meter enters, so frame 1 already shows the number the question is about.
7. [0:00–0:03][Clarity] "Everyone in this simulated town chose where to live" is untrue in the model: at least 1,099 of 1,440 households never moved from a random start. **Change to:** "Every household in this simulated town is free to move."
8. [3:22 end card + title][Hook/Correctness] "Extreme Segregation" overclaims a 76% result that Schelling himself would call slight at one-third, and the episode calls 58% "barely sorts". **Change the title/end card to:** "Mild Preferences, Segregated Towns" or "A Third Is Enough". This keeps the bait and makes it true.
9. [1:09–1:14][Visual] "Most of these… never moved. Their neighbors did." is asserted while all 74 tiles look identical. **Change:** give the 6 households that moved in round one a dashed outline, so the 68 solid RED outlines visibly "never moved". Add the GRAY label "68 never moved" for 2 s.
10. [2:02.5–2:06.5][Audio/Motion] The board-to-dot transform finishes about 1 s after "one point on this chart". Start the shrink 0.8 s earlier, or retime the line, so the dot lands on "point".
11. [3:10][Audio] "nineteen thirties" is heard as "thirty s". Respell it as "nineteen-thirtees" or say "the nineteen thirties" with a comma pause, then re-transcribe to confirm.
12. [1:46.5–1:49.3][Concision] "Every departure shrinks a minority that was already small" restates what the C and D steps just showed. Cut it and start straight into "Now let the whole town run" (saves about 3 s). Or keep it and cut "In round three, the next one tips the same way" while still showing D's tip silently.
13. [Structural, Originality] Schelling segregation is heavily taught (Hart & Case, *Parable of the Polygons*, 2014, covers mild bias → segregation). The fresh parts are the measured naive-plan failure (74, not 0), the fraction-level domino, and the "cuts both ways" redlining turn. To reach 9, make the landing thesis an experiment rather than a statement. At 3:13, show the 1/3 town beside a second simulated town with matching share within 1 point that was produced by a different mechanism (for example Schelling's own rule at about 45% demand, or households assigned to "red-graded" blocks). Hold for 1.5 s on "Which one wanted only a third?" and then deliver the final line. This replaces about 6 s of the redlining sentence, keeps the citation, and makes the closing line visibly true.

REACHES 9 IF ALL FIXED: yes, but only with fix 13. Fixes 1–12 lift Clarity, Visual and Motion to about 9 and Hook to 9. That gives about 8.8 weighted, because Originality stays at 8 on a well-trodden topic and Audio sits at 8. The structural landing (two indistinguishable maps, two different causes) is what lifts Originality to 9 and makes the closing line land as proof rather than assertion.

KEEP:
- The measured naive-plan failure: "plan: 0" next to "unhappy 74" (1:02–1:09), with the dim-everything-but-the-74 reveal.
- The tile-level domino with formulas built from real counted tiles (3/8 ≥ 1/3 → 2/7 < 1/3 → C → D, 1:14–1:47), and its return at 2:22–2:32 where 1/3 → 1/4 flips < to ≥.
- The honesty: Schelling's own milder result on his own boards, the verbatim quote, "That cuts both ways", and the return to "? demanded" on the opening frame.
