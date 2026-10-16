# Episode 2 — fact sheet

Every number spoken or shown, how it was checked, and where it comes from.
Recomputation (exact fractions + a 10-million-person Monte Carlo, seed 7) in `check.py`,
re-run 2026-10-16 for the round 4 revision (Manrai lines added); output (abridged):

```
PPV exact 99/598 0.1656  naive/ppv 5.98
expected counts: sick 20 -> + 19.8 ; healthy 9980 -> + 99.8
count picture 20/120 = 0.1667
before rounding 19.8/(19.8+99.8) = 0.1656
table route (20*0.99)/(20*0.99+9980*0.01) = 0.1656
shares route (0.002*0.99)/(0.002*0.99+0.998*0.01) = 0.1656
20/10000 = 0.002  9980/10000 = 0.998
half sick: 4950.0 50.0 0.99
strip 24 x 5 = 120  red columns 4/24 = 0.1667 (meter red share 20/120)
MC P(sick|+) = 0.1652
prior 1/500 -> P(sick|+) = 0.1656
prior 1/100 -> P(sick|+) = 0.5000
prior 1/2 -> P(sick|+) = 0.9900
flow widths at 1/500: 0.0745 0.3755 (ratio 19.8 : 99.8)
Cardiff right: 173  precision 0.0700  press '92%' is really 0.9300  raster 26 x 95 = 2470
crowd: 1 square = 17.0 people; lit squares 2470/17 = 145.3 -> 145 squares = 2465 alerts at that scale; blocks 29 x 5 = 145
watch lists ~1,200 of 170,000 = 0.7059% (upper bound on listed share)
Manrai: right 14 / 61 = 0.230 ; said 95% 27 = 0.443 ; other 20 ; per 100 dots [23, 44, 33] sum 100 ; wrong 47 = 0.770
Manrai correct answer: 0.0196 ; that test's accuracy (TP+TN)/N: 0.9500
accuracy: right = 9900.0 of 10,000 = 0.9900 ; says 'healthy' to everyone: right = 9980 = 0.9980 (recall 0)
listed squares: ceil(1200/17) = 71 (1200/17 = 70.6) ; flagged red: 173/17 = 10.2 -> 10 ; red share of 145 flagged = 0.0690 vs 173/2470 = 0.0700
listed share of crowd (upper bound): 71/10000 = 0.0071  1200/170000 = 0.0071
Davies CL: 0.030  Six Nations: 0.458
  1 in 74: P(sick|+) = 0.576   (the landing sweep's label and meter now read the same rounded N)
stage 2a (transient) 20*0.99/(20*0.99+100) = 0.1653 -> 17%
evaluators' tick at the final: 78/2632 = 0.0296 -> 3%
```

## A. The hook problem (a stylised screening problem, not a real disease)

Round 2 changed the prevalence from 1 in 1,000 to 1 in 500. The old numbers (0.1 %, 99 %, answer 9 %)
are exactly Veritasium's *The Bayesian Trap* (2017); the production guide (§11.8) and the round-2
substance critic both asked for a fresh case. The test (99 % sensitivity, 1 % false-positive rate)
is kept because the episode title promises a 99 % accurate test.

| Claim (as said / shown) | Check | Status |
|---|---|---|
| Prevalence 1 in 500; test catches 99 % of cases (sensitivity); wrongly flags 1 % of healthy people (false-positive rate) | Stated as the premise. Sensitivity and false-positive rate are given separately on screen (two arrows: 99 %, 1 %). With sensitivity = specificity = 99 %, accuracy is 99 % at any prevalence, so the title is consistent; the landing now says so and pays it off (rows below). | Premise |
| Chance you are sick given a positive ≈ 17 % | Exact: 0.002·0.99 / (0.002·0.99 + 0.998·0.01) = 99/598 = **0.1656**. Monte Carlo (10⁷ people): 0.1652. | Verified |
| "Six times too high" (99 % vs 17 %); brace "6× too high" | 0.99 / 0.1656 = **5.98** (counted picture: 0.99 / 0.1667 = 5.94) | Verified |
| Out of 10,000 people: 20 sick, about 20 test +; 9,980 healthy, about 100 test + | Expected counts: 20 sick → 19.8 positive; 9,980 healthy → 99.8 positive. Shown as whole people (20, 100) under the label "expected counts"; narration says "about twenty", "about a hundred". The insight then shows them unrounded (19.8, 99.8). | Verified (rounded, labelled, then shown exactly) |
| "Of a hundred and twenty positives, only twenty are sick. That's seventeen percent." | 20/120 = 16.7 % (count picture); exact 16.6 %. Both round to 17 %. The meter shows round(100 × 20/120) = 17 %. | Verified |
| Strip of 120 positives under the meter, red columns under the red share | 24 × 5 = 120; 4 red columns of 24 = 16.7 % of the strip's width = the meter's red segment (strip width = bar width). | Verified |
| Naive rule works when half are sick: of 5,000 who light up, 99 % are sick | 5,000 sick → 4,950 +; 5,000 healthy → 50 +; 4,950/5,000 = **0.99** exactly. | Verified |
| "Twenty, out of twenty plus a hundred" → 20 / (20 + 100) ≈ 17 % | 0.1667 → 17 %. | Verified |
| "Unrounded, the red count is twenty sick people times ninety-nine percent. The blue count is nine thousand nine hundred eighty healthy people times one percent." → 20 × 0.99 / (20 × 0.99 + 100), then 20 × 0.99 / (20 × 0.99 + 9,980 × 0.01) ≈ 17 %; the table's rounded positives 20 and 100 become 19.8 and 99.8 as their terms expand | 20 × 0.99 = 19.8; 9,980 × 0.01 = 99.8; 19.8 / 119.6 = **0.1656** (= 99/598). The transient middle state 19.8 / 119.8 = 0.1653 also rounds to 17 %. The "20" in 20 × 0.99 flies from the table's *people* column; the rounded "20" it replaces was the *positives* count, which turns into 19.8 in the table at the same moment. Four formula changes in the derivation, each at least 5 s after the last. | Verified |
| "Divide top and bottom by the ten thousand we started with. Twenty people become two in a thousand, and nine thousand nine hundred eighty become nine hundred ninety-eight in a thousand. The share can't change." The table's people column gets "÷ 10,000" and its 20 / 9,980 turn into 0.002 / 0.998 first; then they fly into 0.002 × 0.99 / (0.002 × 0.99 + 0.998 × 0.01) ≈ 17 % | 20/10,000 = 0.002 and 9,980/10,000 = 0.998 exactly; dividing numerator and denominator by the same number leaves the ratio unchanged. | Verified |
| "These are how common each group is, and these, how often each group tests positive: Bayes' theorem." (one change: all four numbers get their names) → P(sick), P(healthy), P(+∣sick), P(+∣healthy) | Definitions of prior and likelihood. | Verified |
| Bayes' theorem as shown: P(sick∣+) = P(sick)P(+∣sick) / [P(sick)P(+∣sick) + P(healthy)P(+∣healthy)] | Standard Bayes' rule with the law of total probability in the denominator. | Verified |
| "Your seventeen percent assumes a random screen. Symptoms raise the one in five hundred, and the answer climbs: at one in a hundred, fifty percent; at one in two, ninety-nine, where the rule held." (live sweep of the prevalence, meter tracking; the label holds "1 in 100 · 50%" while it is spoken) | Prior 1/100: 0.0099/(0.0099 + 0.0099) = **0.500** exactly. Prior 1/2: 0.495/(0.495 + 0.005) = **0.990** exactly, the half-sick case of beat 3. The sweep is log-spaced between 1/500 and 1/2 and the meter shows P(sick∣+) computed every frame. | Verified |
| Flow widths in the landing; "20" and "100" written outside the flows (silently, after the sweep returns) | Widths are the shares of everyone reaching +: 0.45 × 0.1656 = 0.0745 vs 0.45 × 0.8344 = 0.3755, i.e. 19.8 : 99.8 people. | Verified |
| "The title's ninety-nine percent accuracy is real." (grey bar "accuracy", 99 %) | Accuracy = (TP + TN) / N. Per 10,000: TP = 20 × 0.99 = 19.8, TN = 9,980 × 0.99 = 9,880.2; 19.8 + 9,880.2 = **9,900** → 99.0 %. With sensitivity = specificity = 99 % accuracy is 99 % at any prevalence. | Verified |
| "But a test that calls everyone healthy scores ninety-nine point eight: more accurate, and useless." (grey bar "calls everyone healthy", 99.8 %; both flows drain and their rates read 0 %, the + dims) | It is right about every healthy person: 9,980 / 10,000 = **99.8 %**. It never says positive, so its true-positive rate (recall) is 0 % and its false-positive rate is 0 %: nothing reaches the +. Its precision is undefined (no positives), so the meter is not changed. | Verified |
| Closing lines: "Ninety-nine percent is the test's recall: how often the sick test positive. Seventeen percent is its precision: how often the positive are sick." Tags "recall" (beside the arrow's 99 %) and "precision" (under the meter's 17 %), written on the spoken word | Recall = TP / (TP + FN) = P(+∣sick) = sensitivity = 99 %. Precision = TP / (TP + FP) = P(sick∣+) = 17 %. | Verified (definitions) |
| Landing sweep, in motion | The "1 in N" label and the meter are driven by one updater from the same rounded N (e.g. 1 in 74 → 57.6 % → "58%"; round 3 showed 64 % for one frame because the meter updated a frame late). | Verified (check.py) |

## B. The doctors: Manrai et al. (2014)

Round 4 replaced the Gigerenzer et al. (2007) gynecologists (21 % → 87 %), because the substance
critic noted that 3Blue1Brown's *The medical test paradox* (2020) uses exactly that study. The
training result (87 % after one session) is no longer claimed anywhere in the episode.

Source, read 2026-10-16 in full (PMC author manuscript PMC4955674): Manrai, A. K., Bhatia, G.,
Strymish, J., Kohane, I. S., & Jain, S. H. (2014). *Medicine's uncomfortable relationship with math:
calculating positive predictive value.* **JAMA Internal Medicine**, 174(6), 991–993.
doi:10.1001/jamainternmed.2014.1059. On screen: "Manrai et al., 2014 · JAMA Intern. Med."

- Method: July 2013, a convenience sample of 24 attending physicians, 26 house officers, 10 medical
  students and 1 retired physician at a Boston-area hospital (61 respondents), asked the Casscells
  et al. (1978) question: "If a test to detect a disease whose prevalence is 1/1000 has a false
  positive rate of 5%, what is the chance that a person found to have a positive result actually has
  the disease, assuming you know nothing about the person's symptoms or signs?" Correct answer,
  assuming a perfectly sensitive test: 1.96 % ("2%").
- Results: "Approximately three-quarters of respondents answered the question incorrectly … 14 of 61
  respondents (23%) gave a correct response … the most common answer was '95%,' given by 27 of 61
  respondents (44%)." Median answer 66 %.

| Claim (as said / shown) | Check | Status |
|---|---|---|
| "Most doctors and medical students given a problem like this got it wrong." Waffle "doctors & students", "23% right", "1 dot = 1%", citation | 47 of 61 wrong (77 %); 14 of 61 right = 23.0 %. 51 of the 61 are doctors (attendings, house officers, one retired physician) and 10 are medical students, hence "doctors and medical students". "A problem like this": the same structure (rare condition, false-positive rate, positive result → chance of disease). | Verified |
| Waffle per 100: 23 green, 44 grey "said 95%", 33 grey other | 14/61 = 22.95 % → 23; 27/61 = 44.26 % → 44; 20/61 = 32.79 % → 33; 23 + 44 + 33 = 100. One dot per percent, labelled "1 dot = 1%", so no per-person counts are implied. | Verified (check.py) |
| "Their most common answer was the test's own accuracy, here ninety-nine percent" (label "44% said 95%") | The most common answer was 95 % (27 of 61). For their test (perfect sensitivity, 5 % false positives, prevalence 1/1000) accuracy = 0.001 × 1 + 0.999 × 0.95 = 95.0 %, i.e. the answer is the test's own accuracy (1 − false-positive rate). Our test has sensitivity = specificity = 99 %, so its accuracy, and the same tempting answer, is 99 %. | Verified (check.py) |

On screen: the citation bottom-left from "Most doctors" until the 99 % flies to the naive marker (≈ 9 s).

## C. Data-science consequence: precision, Cardiff 2017

Sources (read 2026-10-15; Davies et al. re-read in full for round 3 via the cardiff.ac.uk PDF):
- **BBC News, 4 May 2018**, "2,000 wrongly matched with possible criminals at Champions League"
  (bbc.com/news/uk-wales-south-west-wales-44007872): "South Wales Police used the technology as about
  170,000 people were in Cardiff for the Real Madrid v Juventus game. But out of the 2,470 potential
  matches with custody pictures - 92% - or 2,297 were wrong … according to data on the force's
  website." And: "South Wales Police said the high volume of false matches was down to 'poor quality
  images' supplied by other agencies including UEFA and Interpol - and it being the first major use of
  the equipment."
- **Davies, B., Innes, M., & Dawson, A. (2018).** *An Evaluation of South Wales Police's Use of
  Automated Facial Recognition.* Universities' Police Science Institute, Cardiff University
  (cardiff.ac.uk/__data/assets/pdf_file/0006/2426604/AFRReportDigital.pdf).
  - p. 10, Champions League Final pilot: four watch lists (red, amber, green, and a blue "friendlies"
    list of police officers); "In total, around 1200 images were enrolled onto watchlists for this
    event."
  - Executive summary, key findings: "Overall, the proportion of true positives increased from 3% at
    the initial Champions League deployment to 46% at the Six Nations deployments. This was due to
    both the new algorithm and increased operator familiarity with the system settings."
  - Champions League results (Section 4): "Across the whole event and all watchlists (including
    blue), there were 2632 matches (alerts) made by the system … 3% (N=78) were 'true positives'";
    "A key influence upon these figures was the poor quality of many of the images uploaded onto the
    system"; "The top 15 individuals by match numbers … accounted for more than 25% of the total
    matches" (so alerts are not distinct people).
  - Six Nations 2018 (3 Feb, 11 Mar, 17 Mar, Cardiff): 48 non-police matches, "46% of these were
    judged 'true positives' by operators (n=22)".
  - What changed: the M20 algorithm replaced S17 ("The improvements between the two algorithms were
    quite remarkable"); "At all subsequent deployments, only custody images of a high standard were
    entered into watchlists"; the similarity threshold was raised from .55 to .59 for the Six Nations.
- The Guardian, 5 May 2018, "Welsh police wrongly identify thousands as potential criminals"
  (same 2,470 / 2,297 figures).

**Round 3 substance critic, fix 2 (Cardiff 7 % treated as purely a base-rate effect; "were right"
states the police figure too firmly). Accepted.** The force's own count (173 of 2,470 = 7 %) and the
evaluators' logbook count (78 of 2,632 = 3 %, all watch lists) differ; the video now attributes the
7 % to the police ("Police counted … as right") and adds the evaluators' later figure, which shows the
other term of Bayes' denominator at work: fewer false alarms per face.

| Claim (as said / shown) | Check | Status |
|---|---|---|
| "At the twenty seventeen Champions League final, about a hundred and seventy thousand people were in Cardiff" (label "≈ 170,000 people") | BBC: "about 170,000 people were in Cardiff for the Real Madrid v Juventus game" (final on 3 June 2017). | Verified |
| Crowd drawn as 100 × 100 squares, legend "■ = 17 people · illustration" | 170,000 / 10,000 = 17 people per square. Labelled an illustration (round 3 substance fix 10): the squares the beam lights stand for alerts at the crowd's scale, and alerts repeat faces (Davies et al.: top 15 individuals > 25 % of matches), so they are not 2,470 distinct people. Blue = not on a watch list (the episode's palette). | Verified (scale; illustration) |
| "The watch lists held about twelve hundred faces" → 71 squares turn red; legend "■ watch-listed: ≤ 1,200" | Davies et al. 2018, p. 10: "around 1200 images were enrolled onto watchlists for this event". ⌈1,200 / 17⌉ = 71 squares. This is an upper bound on listed faces in the crowd (everyone listed present), hence "≤"; the list figure itself includes the blue list of police officers. 71 / 10,000 = 0.71 % = 1,200 / 170,000. | Verified (upper bound, labelled) |
| "…so even a small error rate per face would swamp the real matches" (the crowd brightens on "error rate per face"; the 71 red squares pulse on "swamp") | The mechanism, stated before the result: with at most ~0.7 % listed, the false alarms from ≥ 99.3 % of faces outnumber true matches unless the per-face false-match rate is far below the listed share. No per-face rate for Cardiff is claimed. | Reasoning (no number claimed) |
| "Face-recognition cameras scanned the crowd and raised two thousand four hundred and seventy alerts" | 2,470 potential matches (BBC; Guardian; police data). | Verified |
| The beam flags 145 squares, 10 of them red; they fly into a 29 × 5 block layout that becomes the 2,470-cell raster, the 10 red ones landing in its first columns | 2,470 / 17 = 145.3 → 145 squares; 173 / 17 = 10.2 → 10 red; 10 / 145 = 6.9 % vs 173 / 2,470 = 7.0 %. Each block ≈ 17 alerts; the first 10 blocks (2 of 29 block columns = 6.55 cells of 95) cover the raster's 173 red cells (6.65 cells). Which squares light, and which red squares are not flagged, is illustrative: the sources give neither how many listed people were present nor how many faces were scanned. | Verified (scale); positions illustrative |
| "Shrink to the alerts, and take the red share. Police counted a hundred and seventy-three as right: seven percent" (the crowd leaves, the alerts and meter take the centre; braces "173 right", "2,297 wrong"; meter 7 %) | 2,470 − 2,297 = 173; 173/2,470 = 7.0 %, the force's figure (BBC). Davies et al.'s own logbook analysis gives 3 % (78 of 2,632, all watch lists) for this deployment, so 7 % is if anything generous. The press's "92 %" wrong is 2,297/2,470 = 93.0 %; the video shows counts and 7 %. | Verified (attributed to police) |
| The raster has exactly 2,470 cells, the first 173 red | 26 × 95 = 2,470; red columns cover 173/2,470 = 7.0 % of the width, the same as the meter's red segment (bar width = raster width = 760 px). | Verified |
| "In machine learning, the share of alerts that are right is called precision." | Precision = true positives / (true positives + false positives) = 173 / 2,470. | Verified (definition) |
| "The university's evaluators counted three percent here. After a new algorithm and better photos cut the false alarms, they counted forty-six at the Six Nations." Two dashed ink ticks on the precision meter: 3 % ("evaluators: 3%") and 46 % ("Six Nations 2018: 46%"); citation "Davies et al., 2018 · Cardiff University" | Round 4 (both critics): the round 3 marker put the evaluators' 46 % beside the force's 7 % as if like-for-like. Now both ticks are the evaluators' own logbook counts: 78 of 2,632 = 2.96 % → 3 % at the final (all watch lists), 22 of 48 = 45.8 % → 46 % at the 2018 Six Nations ("judged" true by operators). Davies et al.: "the proportion of true positives increased from 3% at the initial Champions League deployment to 46% at the Six Nations deployments … due to both the new algorithm and increased operator familiarity"; after the final only high-standard custody images were enrolled; threshold .55 → .59. "Better photos" = the custody-image standard; "cut the false alarms" = 2,632 alerts at the final vs 48 at the Six Nations (the other term of Bayes' denominator). The 7 % meter fill stays the force's figure, attributed in narration. | Verified |

On screen: "South Wales Police figures, 2018 · BBC News" bottom-left for the whole beat, with
"Davies et al., 2018 · Cardiff University" above it from the watch-list sentence to the end of the
Six Nations line (≈ 25 s).

## D. Things deliberately not claimed

- No real disease or test is named for the hook numbers; they are a stylised screening case.
- The 10,000-person grid is an illustration of expected counts, labelled "expected counts", not data.
- No claim about the Cardiff system's per-face false-match rate, the number of faces scanned, or how
  many listed people were actually in Cardiff; only the watch-list size (drawn as an upper bound,
  "≤"), the crowd size and the measured alerts are shown. The crowd picture is labelled an
  illustration.
- No claim that the 46 % and the 7 % were measured the same way: the 46 % sits beside the evaluators'
  own 3 % for the final (both from their logbooks); the 7 % is the force's own count and is said so.
- No claim about what "most people" answer to the hook; the baseline is the cited doctors and students
  (Manrai et al. 2014). No claim that training fixes it (the Gigerenzer training result was cut).
- Not used, but checked (round 4): the Metropolitan Police's "one error in 1,000 faces" (0.1 %) vs the
  Essex review's 8 of 42 matches verified (Sky News, 4 July 2019), and Oxford Circus 27 Feb 2020
  (8,600 faces, 8 alerts, 7 false; Met deployment data via Business Insider / Big Brother Watch). A
  second force would have mixed two systems in one act; kept here for a future episode.

## E. Pronunciation

- "twenty seventeen" is written out so the year is read as a year.
- No study author is spoken; names are in the on-screen citations only.
