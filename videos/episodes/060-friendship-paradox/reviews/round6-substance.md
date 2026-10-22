EPISODE: 060 — "Why Your Friends Have More Friends Than You"
IDEA: Following a friendship lands on each girl once per friend she has, so the average friend has avg(k²)/μ = μ + σ²/μ friends (the cross term dies because the balance point makes the distances sum to zero). That is more than the average person whenever counts vary, and epidemiologists use the gap to see a flu outbreak early.
SCORES: Hook 8.5 · Clarity 9 · Visual 8.5 · Motion 9 · Audio 8.5 · Concision 8.5 · Originality 8.5
WEIGHTED: 8.7 (870/100)   AFTER CEILING: 8.7 (lowest 8.5 + 2 = 10.5, so the ceiling does not bind)
CAPS: none
FINAL: 8.7   PASS: no

Reviewer: science/story editor, round 6 (independent).
- Evidence: review/ pack (metrics.json 08:49 is newer than final.mp4 08:47), report.md, all 12 contact sheets, and keyframes 0:07.9, 0:15.9, 0:32.4, 0:46.4, 1:00.8, 1:17.7, 1:27.0, 1:43.2, 2:01.6, 2:13.8, 2:24.7, 2:43.1, 3:12.2, 3:22.3, 3:24.9 and 3:32.3.
- Extra frames I extracted: 2:16.4, 2:17.0, 2:17.6, 2:18.2 and 3:31.6. I also made crops of the "sides at 1/4 scale" tag and the "Facebook's limit" tag.
- Audio: RMS in 0.1 s windows over 1:24.0–1:25.6.
- Sources: Feld (uvm.edu PDF), Christakis & Fowler (journals.plos.org), and the Ugander et al. arXiv PDF, all fetched and grepped.

## FACTS
I recomputed everything from the edge list.
- Degrees: Betty 1, Sue 4, Alice 4, Jane 2, Pam 3, Dale 3, Carol 2, Tina 1.
- Σk = 20 and Σk² = 60.

- Eight girls, every friendship between them, "an Illinois high school" | Verified | Feld 1991, AJS 96(6):1464–77. The paper says "eight girls in 'Marketville,' one of the high schools included in the study". The data are Coleman 1961, from northern-Illinois schools. The PDF's Table 1 reproduces exactly: Betty 1/4/4, Sue 4/11/2.75, Alice 4/12/3, Dale 3/10/3.3, Carol 2/4/2, Tina 1/2/2.
- On average each girl has 2.5 friends (20/8) | Verified | Feld 1991, Table 1.
- Ring: 16 tokens, 32/16 = 2.0, both averages 2 | Verified | computed (hypothetical, labelled on screen).
- Real class: 20 tokens add up to 60, so friends average 3.0. "+0.5 · 20%" (0.5/2.5) | Verified | Feld: "a total of 20 friends ... having a total of 60 friends, with a mean of 3.0".
- "Four on Sue, four on Alice, one on Betty" | Verified | equal to the degrees.
- Two girls at each count 1–4, so the girls balance at 2.5. The tokens (k at position k) balance at Σk²/Σk = 3 | Verified | geometry checked on kf 1:17.7.
  - Girls sit 108 px apart and 216 px make 1 friend.
  - The 2.5 ▲ is at x 538 = mean girl x. The 3.0 ▲ is at x 646 = token-weighted mean.
  - The live read-outs 2.7 (38/14) and 2.9 (52/18) are exact.
- "Sue holds four tokens, each worth four: sixteen". "k² on top, k on the bottom". Σk²÷8 / Σk÷8 = 7.5/2.5 | Verified | algebra.
- Squared distances 2.25 ×4 and 0.25 ×4 give σ² = 10/8 = 1.25 (population variance). The squares are drawn at ¼ side scale and tagged | Verified | computed; the crop shows 82 px vs 27 px sides = 1.5 : 0.5.
- 4² = (2.5 + 1.5)² = 2.5² + 1.5² + 2·2.5·1.5 = 6.25 + 2.25 + 7.5 = 16 | Verified.
- avg(k²) = μ² + σ² + 2μ·avg(d), and avg(d) = 0 because Σ(k − μ) = Σk − nμ = 0, which is the beam's balance condition | Verified | re-derived. This is a correct and complete proof of avg(k²) = μ² + σ².
- Friends average μ + σ²/μ = 2.5 + 0.5 = 3.0. The ring: 2 + 0/2 = 2 | Verified | Feld p. 1469–70 gives the same identity.
- 2011 Facebook users averaged about 190 friends | Verified | Ugander, Karrer, Backstrom & Marlow 2011, arXiv:1111.4503: "68.7 billion friendship edges ... the average Facebook user in our study had around 190 Facebook friends". n = 721 million in May 2011.
- Tokens would average about 635 | Verified | the same PDF, line 435 of the text: "The expected number of friends at the end of a randomly chosen edge, ⟨k²⟩/⟨k⟩ = 635". This is exactly the episode's token average, so the comparison is like for like.
- "A few users had thousands of friends"; 5,000 limit on screen | Verified | Ugander et al.: "a much smaller population have many hundreds or even thousands of friends"; "a clear cutoff at 5000 friends, a limit imposed by Facebook".
- "the spread term is more than twice the mean": 635 − 190 = 445 > 380 | Verified | computed (2.34×).
- Christakis and Fowler, Harvard, 2009; citation reads "2010 · PLoS ONE" | Verified | PLoS ONE 5(9):e12948, published 15 Sep 2010. Study period 1 Sep – 31 Dec 2009.
- 319 random students and 425 friends they named | Verified | C&F Methods: "(N = 319) ... a 'friends' sample (N = 425) composed of individuals who were named as a friend at least once by a member of this random sample".
- "Named friends have more friends, so they sit closer to everyone else" | Verified as C&F's rationale | C&F: "The friend group was observed to have significantly higher measured in-degree and betweenness centrality". Abstract: "individuals near the center ... are likely to be infected sooner".
- "Fitted curves put them 13.9 days ahead" | Verified | Abstract: "Based on clinical diagnoses, the progression of the epidemic in the friend group occurred 13.9 days (95% C.I. 9.9–16.6) in advance". Methods: cumulative logistic fit via NLS. The on-screen fits are an honest refit with the shift held at 13.9, labelled "logistic refit". The arrow measures about 140 px ≈ 13.8 days.
- "With self-reported symptoms, the lead shrank to about three" (3.2 on screen) | Verified | C&F: "a significant but smaller shift in self-reported flu symptoms (3.2 days, 95% C.I. 2.2–4.3)".
- Seat by seat, five fewer, and only Sue and Alice more. Labels 4, 3.5, 3.33, 3.33, 2 and 2.75, 3 | Verified | Feld p. 1465: "five (Betty, Jane, Pam, Dale, and Tina) ... only two (Sue and Alice) ... one (Carol) has as many". Recomputed.
- "Betty looks at her one friend and sees four" | Verified | Feld: "Betty's only friend, Sue".

No wrong, fabricated or uncited claim. Every empirical beat carries its on-screen citation.

Wording nit, no cap: "three counts the friendships" (3:28). The 3 averages over the 20 friendship *ends*, each of the 10 friendships followed both ways. Loose, but not false, because the narration defined the tokens as going "both ways along every friendship". Fix 6 below tightens it.

## MECHANICS
runtime 3:33.3 · wpm 160 (speech time; 152 overall; 540 transcript words) · max silence 2.23 s (planned "Pick one" hold, 0:11.7–0:14.0) · leading 0.00 s / trailing 1.81 s · max static 2.60 s · −14.0 LUFS / −2.1 dBTP · 0 black frames · layout audit 0 issues in 194 checks · WER 0.8 %. No mechanical cap is triggered.

Transcript and audio notes:
- **"Divide" at 1:24.5.** Whisper drops the word. My RMS check shows speech at −12.6 to −15.6 dBFS from 84.5 to 84.96 s, right after digital silence, and then "top" at 84.96. So the word is spoken, but it lasts only about 0.46 s and Whisper still misses it at full level. That suggests a weak, clipped onset (see fix 7).
- **No slop.** The §4 sweep finds no banned phrases, no question chains, no "it turns out", no fake reveals and no recap ending. The voice is specific and noun-driven.
- **Hook timing.** The question lands at 0:08.1–0:11.0, "Pick one" at 0:11.9, then a 2.2 s hold. That meets the 0:12 commitment.

## FLIPBOOK / BEATS
The structure follows BAR §6 closely:

| Time | Beat | What happens |
|---|---|---|
| 0:00–0:14 | Cold open | Network, "average girl 2.5", YELLOW candidates 2.5 / 3 / 4 placed on the axis scale (2.5 at x 1540, 3 at x 1621, 4 at x 1783: correct) |
| 0:14–0:22 | Stakes | Jane "random" → Alice "named friend" |
| 0:22–0:44 | Naive build that works | The ring, 32/16 = 2.0 |
| 0:44–1:03 | Fail | 60/20 = 3.0, a measured "+0.5 · 20%" |
| 1:03–2:24 | Insight | Beam, sliding fulcrum, divide by 8, variance squares, cross-term cancellation, μ + σ²/μ, ring callback |
| 2:25–2:47 | General case | Facebook |
| 2:47–3:17 | Payoff and honest limit | C&F |
| 3:17–3:33 | Landing | The cold-open frame itself; the 3 is ringed |

Deictic sync is tight:
- "Sue holds four tokens": box at 1:17.
- "her distance": d = k − μ at 1:51.
- "add to zero": signed labels and the 0 at 2:03–2:05.
- "cancel": the box leaves at 2:07.
- "rose first": flash at 3:07.
- "Back to the eight girls": network back by 3:19.

Objects persist throughout: network → ring → network → beam → algebra → bars → Facebook bars → curve origins → network.

## WHAT HOLDS IT BELOW 9 (evidence)
1. **Hook and Originality: the "you" in the title is never paid off.**
   - The title says *your* friends. The episode never turns to the viewer: the cold open is 1950s girls (0:00), the payoff is a Harvard sample (2:47), and the last line is about the girls (3:28).
   - All three examples (Feld's eight girls, Facebook 190/635, C&F flu) are the same trio as Strogatz's 2012 NYT column "Friends You Can Count On". What is fresh here is the token/beam proof, not the material.
   - The verified Ugander statistic that would implicate the viewer, "92.7% of users have less friends than the average friend count of their friends", is left unused.
2. **Hook and Clarity: the Facebook prediction (2:31–2:37) is a blind guess.**
   - The viewer is asked "what would the tokens average?" before being told anything about the spread.
   - The spread cue, "a few users had thousands", arrives *after* the answer (2:40).
   - So the second prediction tests nothing the viewer learned. If the order were reversed, the viewer would apply μ + σ²/μ and predict "far more than 190", which is the transfer moment 3b1b would build in.
3. **Clarity at 1:33.6: "Measure each girl's distance from the balance point".**
   - Two balance points are on screen (kf 1:43.2): BLUE 2.5 and YELLOW 3.0. The last one narrated was "they balance at three" (1:15).
   - The picture uses 2.5 (BLUE centre tick), but the words do not say which one. A first-time viewer can measure from 3 and get 2, 1, 0, 1, which breaks the next step.
4. **Clarity and Visual (1:05–2:24): the beam has no count scale.**
   - The girls sit at k ± 0.25 in pairs (kf 1:17.7), so no girl stands at 1, 2, 3 or 4.
   - The PURPLE distance endpoints (kf 1:43.2, x 635/851/1068/1284) fall *between* the paired girls.
   - So "they balance at two and a half" and "distance 1.5" are read from labels, not from geometry. The proof is exact, but the viewer cannot check it by eye.
5. **Visual (1:13–1:33): the most crowded stretch.** Kf 1:27.0 holds:
   - a 20-token beam with two fulcra
   - "4 × 4 = 16"
   - the full bar panel with "+0.5 · 20%"
   - a two-row divide equation
   - the citation

   That is three competing focal regions for about 20 s.
6. **Clarity and Visual (3:21–3:27): the landing tally does not add up on screen.**
   - Five outlines plus two thick outlines leave Carol unmarked (5 + 2 ≠ 8). Nothing says she ties.
   - "2.75" sits under Sue's node at (335, 555), closer to the "Betty" label than to "Sue" (kf 3:24.9).
7. **Hook: the stakes thread breaks.**
   - Flu is raised at 0:14–0:22 and then absent for 2 min 25 s until 2:47.
   - The 0:19 "random → named friend" image is not reused when the payoff arrives, so the payoff does not visibly answer the stakes.
8. **Audio at 1:24.5.** "Divide" is weak at onset (see Mechanics).
9. **Motion and Visual nits.**
   - 2:16.4: the cancel box's top-right corner nearly touches the ² of 2.5².
   - 2:17.0: the surviving 2.5 sits on the numerator line, raised above the baseline, for about 0.5 s before it settles.

## FIXES (highest impact first)
1. **[2:43–2:47][Hook + Originality]** Pay off the "you" in the title with a verified number.
   - After "...more than twice the mean itself", add: "And ninety-three percent of users had fewer friends than their friends averaged. Odds are, that includes you."
   - On screen, add a BLUE "92.7% had fewer than their friends' average" (Text ≥ 26) under the brace. Keep the Ugander citation, which already covers it.
   - Do not say "so" or "that's why": Feld notes that the mean inequality does not force a majority.
   - Cost: about 5 s, and the runtime stays under 3:40.
2. **[2:25–2:47][Hook + Clarity]** Make the Facebook prediction an application of the formula, not a guess.
   - New order: "In twenty eleven, Facebook users averaged about a hundred and ninety friends, and a few had thousands. If every friendship sent tokens, what would the tokens average?" *[pause 1.6]* "About six hundred and thirty-five: the spread term is more than twice the mean itself."
   - Move the axis break, "5,000 / Facebook's limit" and the "a few users" brace to "a few had thousands", *before* the "?" appears.
3. **[1:33.6][Clarity]** Name the balance point.
   - Change the line to "Measure each girl's distance from the girls' balance point, two and a half, and square it".
   - From 1:33 to 2:19, dim the YELLOW 3.0 fulcrum and its label to 30 % so only the BLUE 2.5 is live.
4. **[1:05–1:10][Clarity + Visual]** Give the beam a scale.
   - On "Line the girls up by friend count", draw GRAY ticks with labels 1, 2, 3, 4 (MathTex ≥ 26) under the beam at the count positions BX(k), between each pair.
   - Keep them through the variance step so the PURPLE distance endpoints visibly land on 1, 2, 3, 4 and the 2.5 fulcrum sits midway between 2 and 3.
5. **[1:19–1:33][Visual]** Reduce the frame to one focal point.
   - After the "three" flash (1:16), dim the bar panel and "+0.5 · 20%" to 35 %, as the variance step already does.
   - The beam and the divide equation are then the only full-strength objects. Restore the panel at "exactly the extra half friend".
6. **[3:19–3:31][Clarity]** Make the landing count close, and tighten the last line.
   - Give Carol a GRAY "2 = 2" tie label above her node (Text ≥ 26, no outline).
   - Move "2.75" to directly above-left of Sue's node, next to "Sue", and "3" to directly above Alice's node, each at buff ≥ 0.15.
   - Change the final words to "...three counts the tokens." This is exact (60/20) and calls back the episode's own device.
7. **[1:24.5][Audio]** "Divide" is swallowed at onset.
   - Re-synthesise the sentence as "Now divide top and bottom by the eight girls", or add 0.15 s of lead-in.
   - Confirm in the review kit that Whisper returns "divide" (the WER diff line should disappear).
8. **[2:47–2:53][Hook]** Close the stakes loop visually.
   - On "put this to work at Harvard", bring back the 0:19 picture as a 0.5× inset: Jane's BLUE "random" ring and the YELLOW arrow to Alice, "named friend".
   - Then transform "random" into "319 random students" and "named friend" into "425 friends they named" as each is spoken.
9. **[2:16.4–2:17.2][Visual + Motion]** Polish the cancel step.
   - Add 0.08 units of buff to the top of the cancel box so it clears the ².
   - Make the surviving 2.5 move to the row's baseline in the same animation as the cancel, instead of parking on the numerator line.

REACHES 9 IF ALL FIXED: yes, narrowly.
- Fixes 1, 2 and 8 lift Hook to 9 and Originality to about 9: the viewer is implicated, and the second prediction becomes a transfer test.
- Fixes 3, 4, 5 and 6 lift Visual to 9 and keep Clarity at 9 or above.
- Fix 7 lifts Audio to 9.
- That gives 15·9 + 25·9 + 15·9 + 15·9 + 10·9 + 10·8.5 + 10·9 = 895, so about 9.0. With Concision at 9 (fix 2 removes a sentence's worth of reshuffle cost), it is 9.0 clean.
- No structural change is needed: the build, fail, insight and payoff chain and the central picture are already at the bar. Without fixes 1–2 the episode stays an excellent 8.7.

KEEP:
- The token beam: the girls balance at 2.5, the tokens at 3 (the fulcrum slides 2.7 → 2.9 → 3.0 as layers land), and the *same* balance makes Σd = 0, which kills the cross term (1:03–2:12). The animation is the proof.
- The naive-build and fail pair on real data: the ring passes at 32/16 = 2.0, the real class fails by a measured +0.5 · 20 %, and "The ring had no spread, so it had no gap" (2:21) closes it.
- The honest payoff: C&F Fig. 3 redrawn, the "C&F fitted lead: 13.9 days" arrow at chart scale, and the live shrink to "3.2 days" with self-report (3:07–3:17).
