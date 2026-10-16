# Round 4 review: substance (science + story editor), episode 002

**Evidence**

I used the existing `review/` pack: metrics.json (22:36) is newer than final.mp4 (22:35). I read:
- report.md;
- all 13 contact sheets;
- 14 full-resolution keyframes: kf_02 (0:15.3), kf_03 (0:20.2), kf_06 (0:31.7), kf_10 (0:57.4), kf_12 (1:20.8), kf_14 (1:28.2), kf_17 (1:42.1), kf_22 (2:04.5), kf_23 (2:10.0), kf_26 (2:26.0), kf_27 (2:40.8), kf_30 (2:55.7), kf_34 (3:17.5) and kf_39 (3:39.4);
- 19 frames I extracted with ffmpeg:
  - 2:11.0, 2:11.4 and 2:12.0 (the numerator box);
  - 3:03–3:06 (the Six Nations marker);
  - 9 frames across the prevalence sweep, 3:25.3–3:30.2;
  - 4 frames on "this plus", 3:33.8–3:35.2;
- transcript.txt, transcript_words.tsv, narration.txt, script.md and facts.md.

On the web I checked:
- BBC News, 4 May 2018;
- The Guardian, 5 May 2018;
- WalesOnline / Belfast Telegraph syndication;
- Davies, Innes & Dawson 2018, the cardiff.ac.uk PDF, quoted directly;
- Gigerenzer et al. 2007 (MPG PDF, PubMed);
- Frontiers in Psychology 2015, which cites "160 gynecologists … 21 to 87%".

I scored before reading anything past the header of round4-craft.md.

```
EPISODE: 002-base-rate-fallacy — "When a 99% Accurate Test Says You're Sick"
IDEA: A positive result doesn't hand you the test's 99%; it shrinks the sample space to the people
      who tested positive, and when the condition is rare (1 in 500) that crowd is mostly false
      alarms, so the chance is 17%. That share is Bayes' theorem, and a classifier's precision.
SCORES: Hook 9 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8 · Originality 8
WEIGHTED: 8.5 (847.5/100 = 8.475)   AFTER CEILING: 8.5 (lowest 8 + 2 = 10, not binding)
CAPS: none
FINAL: 8.5   PASS: no
```

## FACTS

| Claim (spoken / on screen) | Status | Source / my recomputation |
|---|---|---|
| Premise: 1 in 500 sick, the test catches 99% and flags 1% of the healthy | Premise | Stylised and not attributed to a real test (facts.md §D). |
| 10,000 people → 20 sick, 9,980 healthy; "about 20" and "about 100" positive ("expected counts" on screen) | Verified | 10,000/500 = 20; 20 × 0.99 = 19.8; 9,980 × 0.01 = 99.8 |
| "Of 120 positives, only 20 are sick. That's 17%" | Verified | 20/120 = 16.7%; exact 19.8/119.6 = 99/598 = 16.56% → 17% |
| "The rule said 99, six times too high"; brace "6× too high" | Verified | 0.99/0.1656 = 5.98 |
| Half sick: 4,950 + 50; "of the 5,000 who lit up, 99% are sick" | Verified | 5,000 × 0.99 = 4,950; 5,000 × 0.01 = 50; 4,950/5,000 = 0.990 |
| 20/(20+100) → 19.8/(19.8+99.8) → 20×0.99/(20×0.99+9,980×0.01) → ÷10,000 → 0.002, 0.998 | Verified | Ratio unchanged; 20/10,000 = 0.002; 9,980/10,000 = 0.998 |
| Bayes' theorem as drawn at 2:04.5, with total probability in the denominator | Verified | Re-derived: P(s∣+) = P(s)P(+∣s) / [P(s)P(+∣s) + P(h)P(+∣h)] |
| "The title's 99% accuracy is real" (grey bar, 99%) | Verified | TP + TN = 19.8 + 9,880.2 = 9,900 of 10,000. With sensitivity = specificity = 0.99, accuracy is 0.99 at any prevalence. |
| "A test that calls everyone healthy scores 99.8" | Verified | 9,980/10,000; recall 0 |
| "50% at 1 in 100, 99 at 1 in 2, where the rule held"; mid-sweep frames | Verified | 0.0099/0.0198 = 0.500 and 0.495/0.500 = 0.990. Frames I recomputed: "1 in 297 · 25%" = 0.2506; "1 in 59 · 63%" = 0.6305; "1 in 333 · 23%" = 0.2297; "1 in 152 · 40%" = 0.3989; "1 in 4 · 97%" = 0.9706. The label and the meter agree on every frame. |
| Landing flows "20 … along the red, 100 along the blue" | Verified | Widths 19.8 : 99.8 |
| Recall = 99% = P(+∣sick); precision = 17% = P(sick∣+) | Verified | Definitions |
| "Most doctors given a problem like this got it wrong"; waffle "gynecologists · 21% right"; after one natural-frequency session, 87% | Verified | Gigerenzer, Gaissmaier, Kurz-Milcke, Schwartz & Woloshin (2007), *PSPI* 8(2):53–96, p. 55: "the gynecologists' confusion disappeared; 87% of them now understood…". Frontiers 2015: "Among 160 gynecologists … increased from 21 to 87%". The citation is on screen at 0:17–0:24 and 2:13–2:23. |
| "About 170,000 people were in Cardiff" at the 2017 final | Verified | BBC, 4 May 2018: "about 170,000 people were in Cardiff for the Real Madrid v Juventus game" |
| "The watch lists held about 1,200 faces" (on screen "watch-listed: ≤ 1,200") | Verified | Davies et al. 2018: "In total, around 1200 images were enrolled onto watchlists" |
| "Raised 2,470 alerts. Police counted 173 as right, 7%" | Verified (attributed correctly) | BBC, Guardian and WalesOnline: 2,470 potential matches, 2,297 wrong (police data). 2,470 − 2,297 = 173, and 173/2,470 = 7.0%. |
| "A new algorithm and better photos cut the false alarms, and 46% of alerts were judged right" | Verified, with a framing caveat | Davies et al.: "the proportion of true positives increased from 3% at the initial Champions League deployment to 46% at the Six Nations … due to both the new algorithm and increased operator familiarity". Also: "At all subsequent deployments, only custody images of a high standard were entered into watchlists". Six Nations: "46% … judged 'true positives' by operators (n=22)". **Caveat:** the meter puts the 46% marker on the same bar as the police's 7%. The evaluators' own like-for-like figure for the final is 3%, so the on-screen comparison mixes two measures (fix 3). |

No wrong, fabricated or misattributed claim. Every empirical claim carries an on-screen citation.

## MECHANICS

runtime 3:49.8 · 153 wpm (speech time; 562 words) · max silence 2.08 s (the planned "Pick a number" hold, 0:13.4–0:15.5) · max static 3.33 s (2:15.9–2:19.2) · −14.0 LUFS / −1.7 dBTP

- Leading silence 0.00 s, trailing 1.73 s.
- 0 black frames.
- WER 2.0%; every difference is the "a"/"one" or "where"/"were" homophone.
- 0 banned phrases; 0 layout-audit issues.
- No mechanical cap. Runtime is 10 s inside the 4:00 limit, which matters for concision.

## STORY, CLARITY AND SLOP NOTES

**Hook (9)**
- Frame 1 (kf_01) is the problem itself, with no title card. The question lands at 0:09.3–0:12.6, and "Pick a number" gets a silent hold of 2.1 s.
- "Most doctors … got it wrong" (0:15.5) adds a cited baseline.
- "You'd start treatment today" (0:23.4) states the stakes.
- The ending re-forms the exact cold-open diagram (3:07) and re-reads its two numbers as recall and precision.
- Why it is not 9.5: after "That's Bayes' theorem" (2:05) the opening question is answered, and the second act has to reopen tension twice: "chance an alert is right ?" at 2:25, then the accuracy beat at 3:07.

**Clarity (8.5)**
- The chain of counting, shrinking, then the formula (0:43–2:06) is correct and concrete-first. At 1:28 the strip of 120 hangs under the meter, with the red columns under the red share (kf_14).
- The honest limits are stated: "Your 17% assumes a random screen" (3:17.6), and the 46% shows that precision moves with the false-alarm term.
- Deductions:
  1. The 1:34–2:06 derivation changes the equation 8 times in 32 s:
     - 19.8 → 20×0.99 (1:40);
     - 99.8 → 9,980×0.01 (1:44);
     - "÷10,000" (1:47);
     - 0.002 (1:54);
     - 0.998 (1:57);
     - P(sick)/P(healthy) (2:00);
     - P(+∣·) (2:03);
     - boxes (2:09–2:11).

     §5 allows one new equation per 5 s. The ÷10,000 step, where a count becomes a probability, is the step most viewers will rewind.
  2. The 7% vs 46% marker compares the police count with the evaluators' logbook figure (3:02–3:05).
  3. The accuracy bars at 3:13–3:17 look identical, 99% against 99.8%. The picture does not show why the second test is "useless": its recall of 0 is never drawn.

**Concision (8)**
- 20 and 100 are stated three times: 0:58–1:03, 1:30–1:32, and 3:32–3:38 ("On a random screen, twenty reach this plus…").
- The landing runs 44 s (3:05–3:49) and carries three separate ideas: the accuracy paradox, prevalence dependence, and recall vs precision. §6 budgets about 15 s for the landing.
- "Before rounding, these are 19.8 and 99.8" re-explains numbers the table already shows. About 8–10% of the runtime is removable.

**Originality (8)**
- The premise and the Gigerenzer gynecologist statistic are exactly what 3Blue1Brown's *The medical test paradox* (2020) uses. Veritasium's *The Bayesian Trap* (2017) covers the same ground.
- What is this channel's own:
  - the Cardiff precision case, with the watch-list crowd flying into a raster that sits under the 7% meter;
  - the half-sick control case where the rule holds;
  - the people-width flows in the prevalence sweep;
  - the accuracy-vs-useless-classifier line;
  - the recall/precision chiasmus.

**Slop scan (§4)**
- 0 banned phrases.
- No question chain: the one question at 0:09–0:12 is followed by an instruction.
- No "it turns out", no fake colon reveal, no "isn't just".
- Mild verbal tic: four sentences open with "That's…" ("That's about a hundred", "That's 17%", "That's 20 sick people times…", "That's Bayes' theorem"). This is not a cap.
- The closing chiasmus re-reads the cold open; it is not a recap list.

**Sync**
- The deictics land:
  - "these hundred and twenty people": the outline closes at 1:25;
  - "the red share": the brace "20" at 1:29;
  - "these two": the terms pulse at 1:59–2:03;
  - "this plus": the ring scale-pulses, 3:34.4–3:34.9, verified across 4 frames.
- One early lead in the sweep. "Fifty percent" (3:25.2) shows "1 in 152 · 40%". "1 in 100 · 50%" sits from 3:25.8 to 3:26.4. While "at one in a hundred" is spoken (3:26.4–3:27.8), the screen already reads "1 in 59 · 63%" (3:27.0) and "1 in 4 · 97%" (3:27.6). The viewer hears "fifty percent at one in a hundred" over a meter at 63–97%.
- The numerator box (2:11.4–2:12.0) clears the fraction bar by only about 10 px. This is a nitpick.

```
FIXES (highest impact first):
1. [1:46.5–2:06.0][Clarity/Motion] 8 equation states in ~20 s. Split the ÷10,000 step into its own
   picture: on "Divide top and bottom by ten thousand" re-label the strip's braces "20 of 10,000" →
   "0.002 of everyone" and "9,980 of 10,000" → "0.998" (TransformFromCopy from the table's people column
   into the formula), and hold each new term ≥ 2.4 s (2 s + 0.4 s/term) before the P(·) naming step.
   Merge the two naming steps into one sentence ("These are how common each group is, and how often each
   tests positive") with both pairs pulsing in sequence, so the formula changes at most once per 5 s.
   Pays for itself with fix 4's cut.
2. [3:25.2–3:28.9][Audio/Motion] The sweep leaves "1 in 100 · 50%" before "at one in a hundred" is
   spoken. Re-time the prevalence tracker: reach N = 100 at 3:25.4 ("fifty"), hold it to 3:27.8 (end of
   "hundred"), then sweep 100 → 2 over 1.0 s (smooth) to land at 3:28.9 on "one in two". Every spoken
   number then sits on its own frame.
3. [2:57.3–3:05.2][Clarity] The 46% marker sits on a meter whose fill is the police's 7%, but Davies et al.'s
   comparable figure for the final is 3%. Change the marker label to "Six Nations 2018: 46%" plus a second
   grey tick at 3% labelled "same evaluators, final: 3%" (font ≥ 18 Text), and say "the evaluators' own
   count went from three percent at the final to forty-six" instead of "and forty-six percent of alerts were
   judged right". This makes the comparison like-for-like and shows the false-alarm term of Bayes'
   denominator falling (2,470 alerts → 48).
4. [3:31.0–3:38.0][Concision] Cut "On a random screen, twenty reach this plus along the red, a hundred
   along the blue." That's the third time 20/100 is stated. Keep the "20"/"100" flow labels, but write them
   silently during the 1.0 s pause after "where the rule held". Saves ~6 s.
5. [3:07.2–3:17.5][Clarity/Visual] Two near-identical grey bars (99% vs 99.8%) don't show why the second
   test is useless. On "calls everyone healthy", collapse the red arrow to zero width and set its label
   "99%" → "0%" (the useless test's recall), and drop the meter's red segment to 0 for 1.5 s before
   restoring. Keep the 99.8% bar. Then "more accurate, and useless" has a visible referent.
6. [1:34.1–1:38.9][Concision] "Before rounding, these are nineteen point eight and ninety-nine point eight."
   repeats what the table's 19.8 / 99.8 already show. Fold it in: "Unrounded, that's twenty sick people
   times ninety-nine percent, and nine thousand nine hundred eighty healthy times one percent." with
   20→19.8→20×0.99 in one TransformMatchingTex. Saves ~3 s.
7. [2:12.1–2:23.1][Hook] The gynecologist callback sits between Bayes and Cardiff and lets tension sag.
   Move the "87% got it right" clause directly after "That's Bayes' theorem. All it does is…" so it is
   heard as proof that the counting picture works, then cut straight to "Swap the disease for a police
   watch list" with the meter re-titling as the question mark of act 2.
8. [2:11.4–2:12.0][Visual] The red numerator box clears the fraction bar by ~10 px and the ")" by ~15 px.
   Use buff 0.15 on the SurroundingRectangle and shift the numerator up 0.05 so the box clears the bar
   by ≥ 0.15 units.
9. [0:59.6, 1:03.6, 1:34.1, 2:05.0][Originality/Audio] Four sentences open with "That's". Rewrite two:
   "Seventeen percent." (1:03.6) and "Twenty sick people times ninety-nine percent…" (1:38.9).

REACHES 9 IF ALL FIXED: borderline, about 8.9–9.0.
- Fixes 1–3 and 5 lift Clarity to 9. Fix 2 lifts Audio and Motion to 9. Fixes 4 and 6 (≈ 9 s cut, runtime ≈ 3:41)
  lift Concision to 8.5–9.
- 9·15 + 9·25 + 9·15 + 9·15 + 9·10 + 9·10 + 8·10 = 890, i.e. 8.9.
- 9.0 also needs Originality 9. The structural limit is that the spine (a medical test with 1 in N prevalence,
  natural frequencies, the Gigerenzer gynecologists) is 3b1b's *medical test paradox*.
- What would make it this channel's own: let the Cardiff precision case or the accuracy-vs-useless-classifier
  line carry more of the runtime. For example, open the second act on "this camera system is 99.9% accurate
  per face" before the alerts, so the ML framing is the twist rather than an epilogue.

KEEP:
- The SMH failure chain: the half-sick control where the rule holds, then the same test at 1 in 500 failing
  by a measured "6× too high" brace (0:27–1:11).
- The 120-person strip hanging under the 17% meter with its red columns aligned to the red share, and the
  formula built term by term from it and the table (1:21–2:11).
- The landing: the cold-open diagram re-formed, the people-width flows in the prevalence sweep landing on
  the naive 99% marker, and the recall/precision chiasmus (3:07–3:48).
```
