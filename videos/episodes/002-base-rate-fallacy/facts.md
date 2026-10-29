# Episode 2 — fact sheet

Every number spoken or shown, how it was checked, and where it comes from.
Recomputation (exact fractions + a 10-million-person Monte Carlo, seed 7) in `check.py`,
re-run 2026-10-16 for the round 4 revision (Manrai lines added), for the review-cycle-2 revision, and on
2026-10-22 for rounds 5 and 6 (landing counts; the round-6 slider, divided positives and Six Nations
caveat are the last block); output (abridged):

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
6x bracket label: 99 / 17 = 5.82 -> '99 / 17 ~ 6x'; exact 0.99 / ppv = 5.98
watch-list base rate (upper bound): 170,000 / 1,200 = 141.7 -> 1 in 142 ; shown '<= 1 in 140' since 1/141.7 <= 1/140 = 0.00714 >= 0.00706
  (more common than the hook's 1 in 500 = 0.002 -> no comparison is drawn)
sums shown under the positives column: half sick 4950 + 50 = 5000 ; 1 in 500: 20 + 100 = 120
evaluators' bar: final 78/2632 = 0.030 -> 3% ; Six Nations 22/48 = 0.458 -> 46% ; false at Six Nations 22 of 48, missing 4
crowd raster: 100 x 100 squares in 7 px cells = 700 px = 5.185 units
fail beat: positives drawn at 3x (18 px): 20 sick + 100 healthy = 120 ; healthy share of the ringed squares = 0.833
landing counts at 1 in 500: red 19.8 -> 20 ; blue 99.8 -> 100 ; share 0.166
landing counts at 1 in 271: red 36.5 -> 37 ; blue 99.6 -> 100 ; share 0.268
landing counts at 1 in 100: red 99.0 -> 99 ; blue 99.0 -> 99 ; share 0.500
landing counts at 1 in 2: red 4950.0 -> 4950 ; blue 50.0 -> 50 ; share 0.990
slider 1 in 2: sick 5000 -> + 4950 ; healthy 5000 -> + 50 ; positives 5000 ; meter 0.990
slider 1 in 10: sick 1000 -> + 990 ; healthy 9000 -> + 90 ; positives 1080 ; meter 0.917
slider 1 in 100: sick 100 -> + 99 ; healthy 9900 -> + 99 ; positives 198 ; meter 0.500
slider 1 in 500: sick 20 -> + 20 ; healthy 9980 -> + 100 ; positives 120 ; meter 0.166
positives / 10,000: 19.8 -> 0.00198  99.8 -> 0.00998 ; = 0.002 x 0.99 = 0.00198 ; 0.998 x 0.01 = 0.00998
Six Nations, operators' Y: 0.458 ; if the 7 later found false are removed: 0.312 (still 10x the final's 3 %)
live meter from displayed counts: 1 in 388 -> 26 / 126 = 20.6 % -> 21 % ; 1 in 340 -> 29 / 129 = 22.5 % -> 22 % ; exact-vs-shown differs by 1 point at 59 of 499 N (now the counts govern)
```

## A. The hook problem (a stylised screening problem, not a real disease)

Round 2 changed the prevalence from 1 in 1,000 to 1 in 500. The old numbers (0.1 %, 99 %, answer 9 %)
are exactly Veritasium's *The Bayesian Trap* (2017); the production guide (§11.8) and the round-2
substance critic both asked for a fresh case. The test (99 % sensitivity, 1 % false-positive rate)
is kept because the episode title promises a 99 % accurate test.

| Claim (as said / shown) | Check | Status |
|---|---|---|
| Prevalence 1 in 500; test catches 99 % of the sick (sensitivity; spoken "catches ninety-nine percent of the sick" since cycle 2); wrongly flags 1 % of healthy people (false-positive rate) | Stated as the premise. Sensitivity and false-positive rate are given separately on screen (two arrows: 99 %, 1 %). With sensitivity = specificity = 99 %, accuracy is 99 % at any prevalence, so the title is consistent; the landing now says so and pays it off (rows below). | Premise |
| Chance you are sick given a positive ≈ 17 % | Exact: 0.002·0.99 / (0.002·0.99 + 0.998·0.01) = 99/598 = **0.1656**. Monte Carlo (10⁷ people): 0.1652. | Verified |
| "Six times too high" (99 % vs 17 %); grey bracket from the meter's 17 % fill edge to the naive 99 % marker, labelled "99 ÷ 17 ≈ 6×" | 99 / 17 = **5.82** → 6 (as displayed); exact 0.99 / 0.1656 = **5.98** (counted picture: 0.99 / 0.1667 = 5.94). The bracket's ends are `meter.x_at(20/120)` and `meter.x_at(0.99)` (cycle-2 substance fix 5). | Verified |
| Out of 10,000 people: 20 sick, about 20 test +; 9,980 healthy, about 100 test + ("About twenty sick people light up, plus one percent of everyone else: about a hundred."; the 9,980 is on the table, no longer spoken) | Expected counts: 20 sick → 19.8 positive; 9,980 healthy → 99.8 positive. Shown as whole people (20, 100) under the label "expected counts"; narration says "about twenty", "about a hundred". The insight then shows them unrounded (19.8, 99.8). The 120 positives are drawn ≥ 5 cells apart, so all 120 rings are distinct. | Verified (rounded, labelled, then shown exactly) |
| "So of a hundred and twenty positives, only twenty are sick. Seventeen percent." (column sum "120" under the positives column; all 120 positives drawn 3x with the same yellow ring, so the 100 healthy ones visibly outnumber the 20 sick) | 20/120 = 16.7 % (count picture); exact 16.6 %. Both round to 17 %. The meter shows round(100 × 20/120) = 17 %. | Verified |
| Strip of 120 positives under the meter, red columns under the red share | 24 × 5 = 120; 4 red columns of 24 = 16.7 % of the strip's width = the meter's red segment (strip width = bar width). | Verified |
| Naive rule works when half are sick: of 5,000 who light up, 99 % are sick (column sum "5,000" written under the positives column on "five thousand"; round 6: the sick are drawn as the grid's left 50 columns, the table's header carries "1 in 2"; round 6 cont.: the grid first appears at the header's own 1 in 500, 20 red of 10,000, and floods to half on "half of them sick" as the header rolls to "1 in 2", so no frame shows "1 in 500" over an all-healthy grid; the same 20 are the ones the slider ends on) | 5,000 sick → 4,950 +; 5,000 healthy → 50 +; 4,950/5,000 = **0.99** exactly. The raster realises exactly these counts (50 "missed" sick in the left half, 50 false alarms in the right half). | Verified |
| (round 6) "Now keep the same test, and make the disease rarer and rarer, down to yours: one in five hundred." One slider: the table's "1 in N" runs 2 → 500 (log-spaced), its four counts and the column sum are the *expected* counts at that N (rounded to whole people), the meter shows the red share of the positives *as displayed* (red ÷ column sum), the left block drains from its right edge | Expected counts at 1 in N: sick 10,000/N, + 0.99 × 10,000/N; healthy + 0.01 × (10,000 − 10,000/N). E.g. 1 in 10: 1,000 → 990, 9,000 → 90, meter 990 / 1,080 = 91.7 %; 1 in 388: 26 + 100 = 126, meter 26 / 126 = 20.6 % → 21 % (round-6 self-check: the meter used to show the exact P(sick∣+) at N, 20.4 % → 20 %, so at 59 of the 499 integer N a frame's meter sat one point off its own displayed counts; it is now driven from the displayed counts, so every frame re-derives, and the exact value never differs by more than one point); 1 in 100: 100 → 99, 9,900 → 99, 50.0 %; 1 in 500: 20 → 20 (19.8), 9,980 → 100 (99.8), 120 positives, 16.6 % (check.py, last block). The raster's own lit counts stay within one person of these (fixed per-person results: 50 of the 4,980 draining sick carry a false-alarm flag, so they stay lit as they turn blue). | Verified (check.py) |
| "Twenty, out of twenty plus a hundred" → 20 / (20 + 100) ≈ 17 % | 0.1667 → 17 %. | Verified |
| (round 6, one sentence) "Unrounded, the red count is twenty sick people times ninety-nine percent, and the blue, every healthy person times one percent." → 20 × 0.99 / (20 × 0.99 + 9,980 × 0.01) ≈ 17 % in one move (red term on its words, blue term on its words); the table's rounded positives 20 and 100 become 19.8 and 99.8 as their terms arrive | 20 × 0.99 = 19.8; 9,980 × 0.01 = 99.8; 19.8 / 119.6 = **0.1656** (= 99/598). The transient middle state (red term exact, blue still 100) 19.8 / 119.8 = 0.1653 also rounds to 17 %. The "20" in 20 × 0.99 flies from the table's *people* column; the rounded "20" it replaces was the *positives* count, which turns into 19.8 in the table at the same moment. The 9,980 flies from the people column on "every healthy person" (the number is no longer spoken a second time). | Verified |
| "Divide everything by ten thousand: counts become shares. The share stays the same." (round 6, cont.: was "The share can't change", which whisper heard as "can change" in the full-file transcript) The table's people column gets "÷ 10,000"; on "counts become shares" both rows (20 → 0.002, 19.8 → 0.00198; 9,980 → 0.998, 99.8 → 0.00998) and every count in the formula divide in one move → 0.002 × 0.99 / (0.002 × 0.99 + 0.998 × 0.01) ≈ 17 % | 19.8 / 10,000 = 0.00198 = 0.002 × 0.99 and 99.8 / 10,000 = 0.00998 = 0.998 × 0.01, so no number in the table is stale under the "÷ 10,000" header (round-6 craft fix 3). | 20/10,000 = 0.002 and 9,980/10,000 = 0.998 exactly; dividing numerator and denominator by the same number leaves the ratio unchanged. Since the round-6 self-check there is no transient mixed state (counts and shares together), so no paused frame shows a false equation. | Verified |
| "These are how common each group is, and these are how often each group tests positive. Name them, and you have Bayes' theorem." Grey braces "how common" grow under 0.002 and 0.998, "how often" under 0.99 and 0.01, each on its words; then each number turns into its name in place (0.002 → P(sick), 0.99 → P(+∣sick), 0.998 → P(healthy), 0.01 → P(+∣healthy), numerator first) and the braces stretch with their terms; "≈ 17 %" stays on the right | Definitions of prior (how common) and likelihood (how often a group tests +). Naming the numbers changes no value, so ≈ 17 % still holds. | Verified |
| Bayes' theorem as shown: P(sick∣+) = P(sick)P(+∣sick) / [P(sick)P(+∣sick) + P(healthy)P(+∣healthy)] | Standard Bayes' rule with the law of total probability in the denominator. | Verified |
| "Your seventeen percent assumes a random screen. Symptoms raise the one in five hundred: at one in a hundred, fifty percent; at one in two, ninety-nine, where the rule held." (live sweep of the prevalence, meter tracking; the label holds "1 in 100 · 50%" while it is spoken) | Prior 1/100: 0.0099/(0.0099 + 0.0099) = **0.500** exactly. Prior 1/2: 0.495/(0.495 + 0.005) = **0.990** exactly, the half-sick case of beat 3. The sweep is log-spaced between 1/500 and 1/2; every frame the meter shows the red share of the two counts displayed beside the flows (e.g. 1 in 340: 29 / 129 = 22.5 % → 22 %), which is within one point of P(sick∣+) at that N and equal to it at every N that is spoken (500, 100, 2). | Verified (check.py) |
| Flow widths in the landing; live counts beside the flows with "per 10,000 people" between them (round 5: they appear in the pause after "Back to your test" and follow the prevalence sweep) | Widths are the shares of everyone reaching +: 0.45 × 0.1656 = 0.0745 vs 0.45 × 0.8344 = 0.3755, i.e. 19.8 : 99.8 people. Counts per 10,000 people = 10,000/N × 0.99 (red) and (10,000 − 10,000/N) × 0.01 (blue), rounded to whole people: 1 in 500 → 19.8 / 99.8 → "20" / "100"; 1 in 100 → 99 / 99 (50 %); 1 in 2 → 4,950 / 50 (99 %), the same numbers as the half-sick table of beat 3 (check.py, last block). Label, flows, counts and meter are driven from the same rounded N. | Verified (check.py) |
| (cut in review cycle 2) "The title's ninety-nine percent accuracy is real." | Was: accuracy 9,900 of 10,000 = 99.0 %. Cut with the next row: the accuracy paradox is episode 44's whole topic ("99.8% Accurate and Completely Useless"), and both critics asked for a one-move landing. | Not claimed |
| (cut in review cycle 2) "But a test that calls everyone healthy scores ninety-nine point eight…" | Was: 9,980 / 10,000 = 99.8 %. | Not claimed |
| Closing lines (round 6): "The title's ninety-nine percent is the test's recall: how often the sick test positive. Seventeen percent is its precision: how often the positive are sick." Tags "recall" (beside the arrow's 99 %) and "precision" (under the meter's 17 %), written on the spoken word | Recall = TP / (TP + FN) = P(+∣sick) = sensitivity = 99 %. Precision = TP / (TP + FP) = P(sick∣+) = 17 %. The title's "99 % accurate": with sensitivity = specificity = 99 %, accuracy = 99 % at any prevalence, so the title's number is the test's recall here (and its specificity); the hook introduced it as "catches ninety-nine percent of the sick". | Verified (definitions; equal here) |
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
| "At one Boston-area hospital, most doctors and medical students given a problem like this got it wrong." (round 6, cont.: the setting is now said, so the claim is not generalised beyond the sample) Waffle "doctors & students", "23% right", "1 dot = 1%", citation | Methods, verbatim (PMC4955674, re-read 2026-10-22): "we surveyed a convenience sample of 24 attending physicians, 26 house officers, 10 medical students, and 1 retired physician at a Boston-area hospital". 47 of 61 wrong (77 %); 14 of 61 right = 23.0 %. 51 of the 61 are doctors (attendings, house officers, one retired physician) and 10 are medical students, hence "doctors and medical students". "A problem like this": the same structure (rare condition, false-positive rate, positive result → chance of disease). | Verified |
| Waffle per 100: 23 green, 44 grey "said 95%", 33 grey other | 14/61 = 22.95 % → 23; 27/61 = 44.26 % → 44; 20/61 = 32.79 % → 33; 23 + 44 + 33 = 100. One dot per percent, labelled "1 dot = 1%", so no per-person counts are implied. | Verified (check.py) |
| "Their most common answer was their test's own accuracy: ninety-five percent. For our test, that's ninety-nine: you'd start treatment today." Labels "44% said 95%" and, under it, "their test: 95% accurate"; the "95%" morphs into the naive marker's "99%" on "ninety-nine" | The most common answer was 95 % (27 of 61). For their test (perfect sensitivity, 5 % false positives, prevalence 1/1000) accuracy = 0.001 × 1 + 0.999 × 0.95 = 95.0 %, i.e. the answer is the test's own accuracy (1 − false-positive rate). Our test has sensitivity = specificity = 99 %, so its accuracy, and the same tempting answer, is 99 % (9,900 of 10,000 right at any prevalence). | Verified (check.py) |

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
- **Round 6 (substance fix 1), re-read 2026-10-22: the alerts cover the whole four-day deployment, not
  the match day.** Davies et al. 2018, deployment table: "Champions League (4 days) | extremely large |
  2632 | 78 (3%) | 1". Wired UK (Matt Burgess, 4 May 2018, "Facial recognition tech used by UK police is
  making a ton of mistakes"): "During the UEFA Champions League Final week in Wales last June, when the
  facial recognition cameras were used for the first time, there were 2,470 alerts of possible matches
  from the automated system. Of these 2,297 turned out to be false positives and 173 were correctly
  identified". The BBC piece says "on the day of the Champions League Final", which the primary source
  does not support. So the video now says "Over four days, they raised two thousand four hundred and
  seventy alerts", dates the crowd "Cardiff · Champions League final week, 2017" and tags the evaluators'
  bar "final week · 2,632 alerts". The ≈ 170,000 is still the BBC's figure for the people in Cardiff for
  the game; the crowd picture stays labelled an illustration.
- **Re-checked 2026-10-22 (round 6, cont.).** Wired UK ("During the UEFA Champions League Final week in Wales last June … there were 2,470 alerts"), the EFF (2022: "first deployed in June 2017 during UEFA Champions League Final week … 2,297 false positives from 2,470 'potential matches'") and Davies et al. ("Champions League (2,470 total matches, 173 'true')" for the police figures; their own logbook count 2,632 / 78 over "Champions League (4 days)") agree: the alerts are the week's, which is what the narration ("Over four days") and the dateline ("Champions League final week, 2017") say.
- **Round 6 nits, both accepted.** (1) "around 1200 *images*" (Davies p. 10), including the blue
  "friendlies" list of police officers: the narration now says "about twelve hundred photos", and the
  1,200 is no longer written on screen; only the bound it implies ("≤ 1 in 140") is. Images ≥ people, so
  the bound still holds. (2) Six Nations: "a total of 56 matches … removing 'blues' … 48 were left. 46%
  of these were judged 'true positives' by operators (n=22) … Of the initial 22 'true positives' … 23%
  (n=5) were stopped, confirmed as 'true' and arrested; 32% (n=7) were stopped but turned out to be false
  positives according to Intervention Teams; 41% (n=8) had unclear/unsure outcomes". The 46 % is the
  operators' logbook judgment, the same method as the final's 3 % ("confirmed by the operators" in the
  logs), so the two are like for like, which is what the narration claims ("their count"). Removing the
  7 later found false would give at most 15 / 48 = 31 %, still ten times the final's 3 %; the video's
  point (the share rose a lot when false alarms per face fell) holds either way. The tag shows the small
  base: "Six Nations 2018 · 48 alerts".

**Round 3 substance critic, fix 2 (Cardiff 7 % treated as purely a base-rate effect; "were right"
states the police figure too firmly). Accepted.** The force's own count (173 of 2,470 = 7 %) and the
evaluators' logbook count (78 of 2,632 = 3 %, all watch lists) differ; the video now attributes the
7 % to the police ("Police counted … as right") and adds the evaluators' later figure, which shows the
other term of Bayes' denominator at work: fewer false alarms per face.

| Claim (as said / shown) | Check | Status |
|---|---|---|
| "For the twenty seventeen Champions League final, about a hundred and seventy thousand people came to Cardiff" (label "≈ 170,000 people"; dateline "Cardiff · Champions League final week, 2017", which fades once read) | BBC: "about 170,000 people were in Cardiff for the Real Madrid v Juventus game" (final on 3 June 2017). Re-checked 2026-10-22 (BBC, Guardian 5 May 2018, WalesOnline: 2,470 potential matches, 2,297 incorrect). | Verified |
| Crowd drawn as 100 × 100 squares (7 px cells, 80 % opacity), header "≈ 170,000 people" under the dateline "Cardiff · Champions League final week, 2017", legend "■ = 17 people · illustration" | 170,000 / 10,000 = 17 people per square. The final was Real Madrid v Juventus, National Stadium of Wales, Cardiff, 3 June 2017. Labelled an illustration (round 3 substance fix 10): the squares the beam lights stand for alerts at the crowd's scale, and alerts repeat faces (Davies et al.: top 15 individuals > 25 % of matches), so they are not 2,470 distinct people. Blue = not on a watch list (the episode's palette). The 20 red and 100 blue dots of the previous act spread into the crowd on "Swap the disease…" (a transition, no claim). | Verified (scale; illustration) |
| "The watch lists held about twelve hundred photos" → the crowd holds 71 red squares; legend "■ watch list" (on "watch list"), then "· ≤ 1 in 140" appended (round 6: two legend lines, docked under the meter) | Davies et al. 2018, p. 10: "around 1200 images were enrolled onto watchlists for this event". ⌈1,200 / 17⌉ = 71 squares. This is an upper bound on listed faces in the crowd (everyone listed present), hence "≤"; the list figure itself includes the blue list of police officers. 71 / 10,000 = 0.71 % = 1,200 / 170,000 = 1 in 141.7, so "≤ 1 in 140" is a true (rounded, looser) upper bound (cycle-2 substance fix 8). Note: this bound is *more* common than the hook's 1 in 500, so the video draws no comparison between the two (the critic's aside that the targets are "rarer than the disease" is not right, and is not used). | Verified (upper bound, labelled) |
| "…so even a small error rate per face would swamp the real matches" (the crowd brightens on "error rate per face"; the 71 red squares pulse on "swamp") | The mechanism, stated before the result: with at most ~0.7 % listed, the false alarms from ≥ 99.3 % of faces outnumber true matches unless the per-face false-match rate is far below the listed share. No per-face rate for Cardiff is claimed. | Reasoning (no number claimed) |
| "Face-recognition cameras scanned the crowds. Over four days, they raised two thousand four hundred and seventy alerts." | 2,470 potential matches (BBC; Guardian; police data), over the four-day "Champions League Final week" deployment (Wired; Davies et al.'s table: "Champions League (4 days)"). | Verified (round 6: four days) |
| The beam flags 145 squares, 10 of them red; they fly into a 29 × 5 block layout that becomes the 2,470-cell raster, the 10 red ones landing in its first columns | 2,470 / 17 = 145.3 → 145 squares; 173 / 17 = 10.2 → 10 red; 10 / 145 = 6.9 % vs 173 / 2,470 = 7.0 %. Each block ≈ 17 alerts; the first 10 blocks (2 of 29 block columns = 6.55 cells of 95) cover the raster's 173 red cells (6.65 cells). Which squares light, and which red squares are not flagged, is illustrative: the sources give neither how many listed people were present nor how many faces were scanned. | Verified (scale); positions illustrative |
| "Shrink to the alerts. Take the red share. The police counted a hundred and seventy-three as right: seven percent" (the crowd leaves, the alerts and meter take the centre; straight brackets "173 right", "2,297 wrong"; meter 7 %, tagged "police count") | 2,470 − 2,297 = 173; 173/2,470 = 7.0 %, the force's figure (BBC). Davies et al.'s own logbook analysis gives 3 % (78 of 2,632, all watch lists) for this deployment, so 7 % is if anything generous. The press's "92 %" wrong is 2,297/2,470 = 93.0 %; the video shows counts and 7 %. | Verified (attributed to police) |
| The raster has exactly 2,470 cells, the first 173 red | 26 × 95 = 2,470; red columns cover 173/2,470 = 7.0 % of the width, the same as the meter's red segment (bar width = raster width = 760 px). | Verified |
| "In machine learning, that share is called precision." (round 6, cont.: was "the share of alerts that are right is called precision"; the meter's title "chance an alert is right" says it on screen as the word replaces it) The meter's title "chance an alert is right" turns into "precision"; a small ghost of the disease meter (17 %, "your test") appears beside it and the word is copied under it as "precision too" | Precision = true positives / (true positives + false positives) = 173 / 2,470; for the test, P(sick∣+) = 17 % is its precision too (the closing line says so). | Verified (definition) |
| "Cardiff University's evaluators counted only alerts the logbooks confirmed: three percent. Months later, a new algorithm, better photos and practised operators thinned out the false alarms, the blue term in Bayes' denominator, and their count rose to forty-six percent." Shown on a separate thin bar under the alerts, red/blue like the meter, tagged on the right like the main bar ("police count / 2,470 alerts" vs "evaluators' count / final week · 2,632 alerts"): it fills to 3 %, its second tag line becomes "Six Nations 2018 · 48 alerts" on "Months later", and on "thinned out" the blue share shrinks as red grows to 46 % while a blue "P(+ ∣ not listed) ↓" appears under the shrinking blue segment. Citation "Davies et al., 2018 · Cardiff University" | Davies et al., Champions League Final section: "Across the whole event and all watchlists (including blue), there were 2632 matches (alerts) made by the system. Operator logs were then used to clarify whether or not these matches were accurate, and indicated that 3% (N=78) were 'true positives' (confirmed by the operators)"; for the blue list "for almost half (N=157) a decision was not recorded in the log books". So "counted only alerts the logbooks confirmed" is the reason their 3 % is below the force's 7 %. (Cycle-2 substance fix 1 proposed "checking every alert themselves"; that is not what the report describes, so it was not used.) Six Nations 2018 (3 Feb, 11 Mar, 17 Mar 2018; 8–9 months after the final): 48 non-police matches, "46% of these were judged 'true positives' by operators (n=22)", 22 false, 4 missing → 22/48 = 45.8 % → 46 %. Key findings: the rise from 3 % to 46 % "was due to both the new algorithm and increased operator familiarity with the system settings"; after the final "only custody images of a high standard were entered into watchlists" ("better photos"); threshold .55 → .59. "Thinned out the false alarms": 2,554 false of 2,632 alerts at the final vs 22 of 48 at the Six Nations. "The blue term in Bayes' denominator" / "P(+ ∣ not listed) ↓" (round-6 substance fix 2): in Bayes' form the false alarms are P(not listed) · P(+ ∣ not listed); every change the report credits (the M20 algorithm, "quite remarkable" improvements; the threshold raised .55 → .59; only high-standard custody images enrolled) lowers the chance that an unlisted face triggers an alert, i.e. P(+ ∣ not listed). Only the direction is claimed, no value. (Base rates also differ between events; the report does not attribute the rise to them.) | Verified (direction) |

On screen: "South Wales Police figures, 2018 · BBC News" bottom-left for the whole beat, with
"Davies et al., 2018 · Cardiff University" beside it on the same line from the watch-list sentence
to the end of the evaluators' sentences (≈ 40 s).

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

## Round 7 (2026-10-22): new and changed on-screen / spoken claims

| Claim (narration or screen) | Check | Status |
|---|---|---|
| Cold open: "In twenty seventeen, police cameras in Cardiff raised two thousand four hundred seventy watch-list alerts. How many were right?" Raster of 26 × 95 = 2,470 grey (unchecked) cells; dateline "Cardiff · Champions League final week, 2017"; citation "South Wales Police figures, 2018 · BBC News" | BBC News 4 May 2018 ("out of the 2,470 potential matches with custody pictures … 2,297 were wrong"); Wired UK 4 May 2018 ("During the UEFA Champions League Final week … there were 2,470 alerts of possible matches"); Davies et al. deployment table ("Champions League (4 days)"). The narration names the year and the city, not the match day; the dateline names the week. Answered at the payoff on the same raster: 173 right = 7.0 %. | Verified |
| "Each alert is a positive test result." | An alert is the system's positive call on a face (a match above threshold); a test result's "+" is the same object. Definitional. | Verified |
| "At one Boston-area hospital, doctors and students given a problem like this most often answered with their test's own accuracy: ninety-five percent. For our test, that's ninety-nine." Tag "their test: 5% false alarms" (round-7 substance fix 1b; was "their test: 95% accurate") | Manrai et al. 2014 gave "a false positive rate of 5%" (and prevalence 1/1000); the most common answer was 95 %, 27 of 61. 1 − 5 % = 95 % is the test's accuracy when sensitivity is perfect (0.001 + 0.999 × 0.95 = 95.0 %). The tag now states what respondents read; the narration's "their test's own accuracy" is the interpretation, as before. "Most often answered" = the modal answer (44 %); the waffle shows 23 % right. | Verified |
| The 20 sick, scattered after the slider (substance fix 6) | Display only: 20 cells cross-fade with 20 healthy-negative cells chosen 5 per quadrant (seed 13), ≥ 9 cells apart and ≥ 5 from every false alarm. Counts (20 / 9,980; 20 + 100 positives) and the meter (20 / 120 = 17 %) are unchanged. | Verified (scene) |
| Strip → crowd (craft fix 8): the 120 dots shrink into the 24 × 5 squares at the crowd's centre and turn blue | Display only: in Cardiff red means "on a watch list"; the 71 listed squares (⌈1,200 / 17⌉) all appear on "twelve hundred photos", scattered. No count changes: 71 × 17 ≈ 1,207 ≥ 1,200. | Verified |
| Every square the beam passes without flagging dims to 35 %, listed or not (substance fix 4) | The 1,200 images are an upper bound on who was present, so the unflagged listed squares are no longer singled out ("cleared"); no recall is implied. | Verified |
| "About a hundred seventy thousand people came" (dateline on screen: "Cardiff · Champions League final week, 2017") | BBC: "about 170,000 people were in Cardiff for the Real Madrid v Juventus game". | Verified |
| "For four days, face-recognition cameras scanned the crowds. Every face they flagged joined the alerts." | Davies et al.: "Champions League (4 days)"; each AFR match is an alert. | Verified |
| "The police counted a hundred seventy-three as right: seven percent." | 2,470 − 2,297 = 173; 173 / 2,470 = 7.00 %. | Verified (check.py) |
| Lever, four sentences (round-7 substance fix 2): "…counted only alerts the logbooks confirmed: three percent. Months later, a new algorithm and better photos thinned out the false alarms. That's the blue term in Bayes' denominator. Their count rose to forty-six percent." | Same sources as the round-6 row above (78 / 2,632 = 3.0 %; 22 / 48 = 45.8 %; "due to both the new algorithm and increased operator familiarity"; only high-standard custody images after the final). "Practised operators" was cut for breath, not for accuracy: the source credits the algorithm and operator familiarity, and the narration names the algorithm and the photos without claiming they are the only causes. | Verified |
| Ghost of the boxed denominator P(sick)P(+∣sick) + P(healthy)P(+∣healthy); its blue term P(healthy)P(+∣healthy) becomes "P(+ ∣ not listed) ↓" (craft fix 3) | In Cardiff's terms "healthy" = not listed, so the blue term is P(not listed) · P(+ ∣ not listed); the credited changes lower P(+ ∣ not listed). Direction only. | Verified (direction) |
| "7 of 22 later proved false" (grey tag under the Six Nations tags; round-7 substance fix 3) | Davies et al., Six Nations: "Of the initial 22 'true positives' … 32% (n=7) were stopped but turned out to be false positives according to Intervention Teams" (re-found 2026-10-22 in cardiff.ac.uk AFRReportDigital.pdf). With those 7 removed the share is at most 15 / 48 = 31 %, still ten times 3 %. | Verified |
| "That ninety-nine percent describes the test: its recall, how often the sick test positive. Seventeen percent describes your result: its precision." (said while the red arrow's 99 % and the meter's 17 % pulse; craft fix 4, substance fix 1a) | Recall = P(+ ∣ sick) = 99 % (the arrow from "sick" to +). Precision = P(sick ∣ +) = 99 / 598 = 16.6 % → 17 %. "That ninety-nine percent" points at the arrow, not at the title's word "accurate"; accuracy is also 99 % here (sensitivity = specificity), so the title is consistent. | Verified |
| "Your test didn't say you're sick. It said you're in this crowd." (over the 20 + 100 flows into the +) | A positive result identifies membership of the positive group (20 + 100 per 10,000); P(sick ∣ +) is the red share of that group. Interpretive closing line, consistent with every number above. | Verified |

## Round 8 (2026-10-22): new and changed on-screen / spoken claims

No factual error was claimed by either round-8 critic (both re-verified Manrai et al. 2014, BBC
4 May 2018 and Davies et al. 2018 by web). Both flagged one borderline plotted-data defect: the
evaluators' single bar showed the final-week 3 % under the tag "Six Nations 2018 · 48 alerts" for
about 8 s. Fixed by giving each event its own bar (below).

| Claim (narration or screen) | Check | Status |
|---|---|---|
| Cold open: "What percent were right? Pick a number." over the meter "chance an alert is right" with "0%" / "100%" under its ends | The question now asks for a share (the meter's quantity), answered at the payoff: 173 / 2,470 = 7.0 %. The scale is the meter's own (0–100 % of the alerts). | Verified |
| "If yours says positive, what's the chance you're sick? [1.5 s hold]" with the guess marker on the same 0–100 % scale | Prompt only; answered at 1:15 (17 %). | n/a |
| "At one Boston-area hospital, doctors and students got a problem like this. Their most common answer was the test's own accuracy: ninety-five percent." Tags "23% right" (beside the green rows), "44% said 95%" (beside the grey rows), "their test: 5% false alarms" (under the waffle); citation "Manrai et al., 2014 · JAMA Intern. Med. · 1 dot = 1%" | Manrai et al. 2014 (PMC4955674): "the most common answer was '95%,' given by 27 of 61 respondents (44%)"; 14 of 61 correct (23 %); respondents were given prevalence 1/1000 and "a false positive rate of 5%". The round-8 craft critic's proposed wording "Most answered with their test's own accuracy" was **not** used: 44 % is the modal answer, not a majority, so the narration says "Their most common answer". | Verified |
| (cut) "Even a small error rate per face would swamp the real matches." | Reasoning sentence, no number; cut for concision (round-8 craft fix 8). | Not claimed |
| "Your chance is the red share of this crowd." (brackets 20 / 100 → 20 / (20 + 100) ≈ 17 %) | 20 / 120 = 16.7 % → 17 %, as before; the spoken "Twenty, out of twenty plus a hundred" is cut (the same share is counted aloud at 1:11). | Verified |
| Scale legend: hollow grey square "= 17 people · illustration" (was a blue swatch) | 170,000 / 10,000 = 17 people per square, for red and blue squares alike. | Verified |
| "■ watch list · ≤ 1 in 140" now appears with the 71 red squares on "twelve hundred photos" | As before: ⌈1,200 / 17⌉ = 71 squares; 1,200 / 170,000 = 1 in 141.7 ≤ 1 in 140 bound. | Verified |
| Lever, two bars: "evaluators' count / final week · 2,632 alerts" fills to 3 %; on "Months later" it dims and a second bar "Six Nations 2018 / 48 alerts" is drawn empty ("?"), filling to 46 % on "rose" | Davies et al. 2018: final, all watch lists, 78 of 2,632 = 2.96 % → 3 %; Six Nations 2018, 48 non-police matches, 22 judged true by operators = 45.8 % → 46 %. Each number now sits only under its own event's tag. | Verified |
| "Months later, a new algorithm and better photos cut the false alarms." | Same sources as round 7 ("thinned out" → "cut"): new M20 algorithm, high-standard custody images only after the final; 2,554 false of 2,632 at the final vs 22 (+ 4 unrecorded) of 48 at the Six Nations. Direction only. | Verified |
| Ghost of the boxed denominator re-read: P(sick)P(+∣sick) + P(healthy)P(+∣healthy) → P(listed)P(+∣listed) + P(not listed)P(+∣not listed); its blue term becomes "P(+ ∣ not listed) ↓" | The same law-of-total-probability denominator with Cardiff's two groups (on a watch list or not); the false alarms are P(not listed)·P(+∣not listed). Direction only, no value. | Verified |
| (cut from screen) "7 of 22 later proved false" | Davies et al., Six Nations: "Of the initial 22 'true positives' … 32% (n=7) were stopped but turned out to be false positives according to Intervention Teams". Both critics asked to cut it or narrate it; it was on screen ~1.7 s, unnarrated. Cut; the 46 % is still the operators' judgment, the same method as the 3 % beside it, so the comparison on screen is like for like. With the 7 removed the share would be ≤ 15 / 48 = 31 %, still ten times 3 %. | Not claimed (kept here) |
| "That ninety-nine percent, the test's accuracy, is also its recall: how often the sick test positive." | Accuracy = (0.99·S + 0.99·(N − S)) / N = 99 % at any prevalence, because sensitivity = specificity = 99 %; recall = P(+∣sick) = 99 %. "Also" states that the two coincide for this test (not in general). Bridges "their test's own accuracy … for our test, that's ninety-nine" (0:35) with "recall" (landing). | Verified |
| Closing: on "this crowd" 120 dots (20 red, 100 blue) stream from the + into a 24 × 5 strip under the meter, red columns under its red 17 % | The counts beside the flows at 1 in 500 (19.8 → 20, 99.8 → 100); 4 of 24 columns = 16.7 % of the strip's width = the meter's red share (strip width = bar width = 4.8). Same strip as at 1:35. | Verified |

## Round 9 (2026-10-23): new and changed on-screen / spoken claims

Neither round-9 critic claimed a factual error; both re-verified Manrai et al. 2014 (PMC4955674),
BBC News 4 May 2018 and Davies et al. 2018 (cardiff.ac.uk AFRReportDigital.pdf) by web. The
substance critic's two nits (the evaluators' 2,632 vs the police 2,470; "the blue term" over-crediting
one cause) are accepted below.

| Claim (narration or screen) | Check | Status |
|---|---|---|
| "Each alert is a positive test result. Take a simpler case: one in five hundred people has a disease." (was "…has this disease", which had no referent) | Premise of the stylised case, as before; "a disease" names no real one (section D). | Premise |
| "Unrounded, the red count is the twenty who are sick, [pause 0.2] times ninety-nine percent, and the blue, every healthy person times one percent." (was "twenty sick people times…", which whisper heard as "twenty-six people") | 20 × 0.99 = 19.8; 9,980 × 0.01 = 99.8, as before. The 20 is the table's people column (the 20 who are sick). | Verified |
| "At most one person in a hundred forty was on a list." (replaces "Every face they flagged joined the alerts."), said while the legend "■ watch list · ≤ 1 in 140" and then the 71 listed squares pulse | Davies et al. 2018, p. 10: "around 1200 images were enrolled onto watchlists for this event"; BBC: "about 170,000 people were in Cardiff for the Real Madrid v Juventus game". Listed people ≤ listed images (a person can have several images; the lists include the blue "friendlies" list of officers, still a list), and not every listed person came, so the listed share of the ~170,000 is at most 1,200 / 170,000 = 0.706 % = 1 in 141.7, which is ≤ 1 in 140 (0.714 %). "Person" (not "face") because the bound is over the people who came; faces were scanned repeatedly over four days, which only makes alerts, not listed people, more numerous. | Verified (upper bound) |
| "Shrink to the alerts." (the flagged squares now file into the 2,470-cell raster on these words; "2,470 alerts" under the raster is no longer written there: it stays in the cold open and on the police bar's tag) | Display only; 145 squares ≈ 2,470 / 17, 10 red ≈ 173 / 17, as before. | Verified (scale) |
| "University evaluators counted only alerts the logbooks confirmed: three percent." Tag under their bar: "evaluators' count / logbook-confirmed" (was "final week · 2,632 alerts") | Davies et al. 2018, Champions League section: "Across the whole event and all watchlists (including blue), there were 2632 matches (alerts) made by the system. Operator logs were then used to clarify whether or not these matches were accurate, and indicated that 3% (N=78) were 'true positives' (confirmed by the operators)". 78 / 2,632 = 2.96 % → 3 %. Their 2,632 includes the blue (police "friendlies") list, which the force's 2,470 does not; both critics found two totals for one week confusing on screen, so the tag now states the reason the bar is lower (only logbook-confirmed matches count) and the 2,632 is kept here only. The authors are at the Universities' Police Science Institute, Cardiff University ("University evaluators"; citation "Davies et al., 2018 · Cardiff University" on screen since the watch-list sentence). | Verified |
| "Months later, a new algorithm and better photos cut the false alarms. That's mostly the blue term in Bayes' denominator." (was "That's the blue term…") | Davies et al., key findings: the rise from 3 % to 46 % "was due to both the new algorithm and increased operator familiarity with the system settings"; after the final "only custody images of a high standard were entered into watchlists"; the threshold was raised .55 → .59. Each of these lowers the chance that an unlisted face triggers an alert, P(+ ∣ not listed). The two events also differ in crowd, watch-list size and which lists were counted (the Six Nations 48 exclude the blue list), which moves the base rate too; the report does not quantify that, so the narration now says "mostly", not "all". Direction only; no value is claimed. | Verified (direction, hedged) |
| The ghost denominator P(listed)P(+∣listed) + P(not listed)P(+∣not listed) now fades out once its blue term has risen into "P(+ ∣ not listed) ↓" | Display only. | n/a |
| The disease diagram parks as a 30 % ghost (bottom right, no text) from "Swap the disease…" until "Back to your test" | Display only: the counting table's bullets, arrows and + fold back into the diagram they came from at 0:44. | n/a |
| Landing flow counts (20 / 100 at 1 in 500 … 4,950 / 50 at 1 in 2) now sit at 70 % (red) / 60 % (blue) of their flows, 0.25 + width / 2 off the centre line | Same values as before (check.py, last block). | Verified |
