EPISODE: 002 — "When a 99% Accurate Test Says You're Sick"
IDEA: A positive result shrinks the sample space to the people who tested positive. When the condition is rare, most of that crowd are false alarms, so your chance of being sick (the test's precision, which is Bayes' theorem) is about 17%, not the test's 99%.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8.5 · Motion 9 · Audio 8.5 · Concision 9 · Originality 8.5
WEIGHTED: 8.6 (862.5/100)   AFTER CEILING: 8.6 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none. I recomputed every number and found no arithmetic, formula or plotted-data error. There are 0 banned phrases or patterns. Every empirical claim has an on-screen citation. All mechanics are inside the bar.
FINAL: 8.6   PASS: no

Reviewer: science and story editor, independent critic, round 7.

Evidence used:
- The review/ pack. metrics.json (21:12) is newer than final.mp4 (21:10), so I used it rather than generating my own.
- All 12 contact sheets.
- 12 full-resolution keyframes: 0:12.4, 0:24.3, 0:40.8, 0:56.5, 1:08.6, 1:41.4, 1:59.6, 2:24.2, 2:41.2, 2:51.4, 3:18.8, 3:34.1.
- 8 extra frames I extracted with ffmpeg: 0:14.5, 0:30.5, 1:19.8, 2:07.8, 2:30.2, 2:56.5, 3:05.6, 3:06.6.
- transcript.txt, narration.txt, script.md, facts.md, and the round-6 substance review (to check which fixes landed).

Citations re-verified by web search on 2026-10-22:
- Manrai et al.: JAMA, PMC and PubMed.
- The BBC article of 4 May 2018.
- Davies, Innes & Dawson (2018): the Cardiff University PDF, queried for direct quotes.

## FACTS

- 1 in 500 prevalence, 99% sensitivity, 1% false-positive rate → P(sick|+) = 0.00198 / (0.00198 + 0.00998) = 99/598 = 16.56% → "17%". | Verified | recomputed
- Per 10,000 people: 20 sick → 19.8 positive; 9,980 healthy → 99.8 positive. Shown as expected counts 20 / 100 / 120, and spoken as "about". 20/120 = 16.7%. | Verified | recomputed
- "Six times too high": the bracket reads "99 ÷ 17 ≈ 6×" (5.82). The exact figure is 0.99 / 0.1656 = 5.98. | Verified | recomputed
- Half sick: 5,000 → 4,950 positive and 5,000 → 50 positive, giving 5,000 positives and 4,950/5,000 = 99% ("the rule holds", kf 0:40.8 and 0:45). | Verified | recomputed
- Slider frames I sampled:
  - 1 in 12: 833 → 825, 9,167 → 92, sum 917, 825/917 = 90.0% (0:51).
  - 1 in 470: 21 / 100 / 121 = 17.4% → 17% (0:53).
  - Every label matches its meter.
  - | Verified | recomputed
- Formula stages:
  - 20 × 0.99 / (20 × 0.99 + 100) = 16.5% (1:41); this is a transient stage, and "≈ 17%" is honest.
  - 20 × 0.99 / (20 × 0.99 + 9,980 × 0.01) = 19.8/119.6.
  - Dividing by 10,000 gives 0.002 / 0.998 and 0.00198 / 0.00998, with the ratio unchanged (1:49).
  - | Verified | re-derived
- Bayes: P(sick|+) = P(sick)P(+|sick) / [P(sick)P(+|sick) + P(healthy)P(+|healthy)] (kf 1:59.6). The denominator is the law of total probability. | Verified | re-derived
- Landing sweep:
  - 1 in 100: 99 / 99 → 50% (3:17).
  - 1 in 2: 4,950 / 50 → 99% (3:19, kf 3:18.8).
  - Transients 1 in 475 → 21/100 → 17% and 1 in 455 → 22/100 → 18% are internally consistent.
  - | Verified | recomputed
- Recall = P(+|sick) = 99%; precision = P(sick|+) = 17%. | Verified | definitions
- "The title's ninety-nine percent is the test's recall" (3:21.8). | Verified with a caveat | The title says "accurate". In this construction sensitivity = specificity = 99%, so accuracy = 0.002·0.99 + 0.998·0.99 = 99% at any prevalence, and the statement is not false. But it maps the word "accurate" onto "recall" without saying they coincide only here. See fix 1.
- Manrai, Bhatia, Strymish, Kohane & Jain, 2014, *JAMA Internal Medicine* 174(6):991–993. | Verified | jamanetwork.com/…/1861033 ("The most common answer was 95%, provided by 27 of 61 respondents"); PMC4955674 (Boston-area hospital; 24 attendings, 26 house officers, 10 students, 1 retired physician)
  - 14/61 = 23% right, which is "most … got it wrong".
  - 27/61 = 44% said 95%.
  - The waffle's 23/44/33 = 100.
- "Their most common answer was their test's own accuracy: 95%", with the on-screen tag "their test: 95% accurate" (0:23–0:29). | Verified as an interpretation | The Manrai question gave a "false positive rate of 5%" and never said "95% accurate". With sensitivity taken as perfect (as the paper's 2% answer assumes), accuracy = 0.001 + 0.999 × 0.95 = 95.0%. The arithmetic is sound, but the on-screen wording is not what respondents read. See fix 1b.
- ≈170,000 people in Cardiff for the Real Madrid v Juventus final; 2,470 potential matches, 2,297 wrong → 173 right = 7.0%. | Verified | BBC News, 4 May 2018 ("about 170,000 people were in Cardiff … out of the 2,470 potential matches … 2,297 were wrong")
- "Over four days" and the dateline "Champions League final week, 2017". | Verified | Davies et al. table: "Champions League (4 days) | extremely large | 2632 | 78 (3%) | 1". This fixes round 6's main conflict.
- "The watch lists held about twelve hundred photos"; "≤ 1 in 140". | Verified | Davies et al.: "In total, around 1200 images were enrolled onto watchlists for this event". 1,200/170,000 = 1 in 141.7, so "≤ 1 in 140" is a valid, looser bound on the listed share of the 170,000.
- Evaluators: "counted only alerts the logbooks confirmed: three percent" (2,632 alerts, 3%). | Verified | Davies et al.: "Operator logs were then used to clarify whether or not these matches were accurate, and indicated that 3% (N=78) were 'true positives' (confirmed by the operators)"
- "Months later … their count rose to forty-six percent" (Six Nations 2018, 48 alerts). | Verified, but incomplete | Davies et al.: "removing 'blues' … 48 were left. 46% of these were judged 'true positives' by operators (n=22)". The rise from 3% to 46% "was due to both the new algorithm and increased operator familiarity". The same page adds: "Of the initial 22 'true positives' … 32% (n=7) were stopped but turned out to be false positives according to Intervention Teams". The 46% is the operators' first call, and the video doesn't say so. See fix 3.
- "Better photos". | Verified | per facts.md's quote that only high-standard custody images were enrolled after the final. I did not re-locate that quote myself, but it is consistent with the report's key findings.
- "P(+ ∣ not listed) ↓" / "the blue term in Bayes' denominator". | Verified (direction only) | Every change the report credits lowers the false-alarm rate per unlisted face. No value is claimed.
- "In machine learning, that share is called precision." | Verified | definition
- Crowd scale "■ = 17 people · illustration": 170,000/10,000 = 17. 71 listed squares × 17 ≈ 1,207. 145 flagged × 17 = 2,465. 10 red flagged × 17 = 170 ≈ 173. The raster is 26 × 95 = 2,470. | Verified (labelled as an illustration) | recomputed. There is an implied-recall nit; see fix 4.

## MECHANICS

Runtime 3:34.2 · wpm 147 (speech time; 136 overall; 487 transcript words, 470 narration words) · max silence 2.24 s (3:05.8–3:08.0, the planned "first frame re-seen" pause; the "Pick a number" hold is 2.15 s at 0:13.5–0:15.6) · max static 3.03 s (3:30.2–3:33.3, the final two-tag hold) · −14.0 LUFS / −2.1 dBTP · leading silence 0.00 s, trailing 1.62 s · black frames 0 · WER 2.1%. Every difference is a number format ("a hundred" heard as "one hundred"), "watchlist" or "practiced". No technical term or name is misheard. The layout audit reports 0 issues across 216 checks. The report's narration-craft section notes the longest stretch without a breath is 12.4 s at 2:51.7. See fix 2.

## Transcript and slop audit

- 0 banned phrases.
- No banned patterns: no "not just X", no abstract triplets, no fake reveals, no lesson-list ending.
- Only one question, at 0:09–0:12 ("what's the chance you're sick?"); "Pick a number" is an imperative, so there is no rhetorical chain.
- Signposting appears once ("Back to your test"), which is allowed.
- The voice is specific and deadpan: "you'd start treatment today", "Here, the rule holds", "Six times too high".
- The narration matches script.md line for line.

## Hook

- The puzzle is on screen from frame 1: the sick/healthy nodes, "1 in 500" and the ghosted meter.
- The question lands at 0:12.6, then "Pick a number" with a 2.1 s hold while the "your guess" marker slides along the empty bar (f 0:14.5).
- The stakes are cited by 0:23: the Manrai waffle, then "you'd start treatment today" at 0:31.

## Beat structure against §6 (scaled to 3:34)

| Beat | Time | Content |
|---|---|---|
| Cold open | 0:00–0:15 | the puzzle and the commit |
| Stakes | 0:15–0:33 | Manrai, then the naive rule placed on the meter at 99% (f 0:30.5) |
| Naive build | 0:33–0:47 | half sick; the meter fills onto the naive marker |
| Fail | 0:47–1:16 | the live prevalence slider takes the meter from 99 to 90 to 17; "6×" bracket (sheet 4) |
| Insight | 1:16–2:06 | negatives vanish, 24 × 5 strip under the meter, brackets, terms fly from the table, ÷ 10,000, braces, names, Bayes, boxes on "shrink" and "take the share" |
| Payoff | 2:06–3:05 | Cardiff crowd, beam, 2,470-cell raster, 7% precision, evaluators' 3% → 46% with P(+∣not listed) ↓ |
| Landing | 3:05–3:34 | the first frame re-seen as people-width flows, the slider run backwards, then "recall" / "precision" |

Every beat is present and in order. The payoff runs 59 s against a template of 30 s, but it carries its own build, fail and second lever, so I don't count it as sag.

## What landed since round 6

Every round-6 substance fix is visible in the cut:
- Four days and the final-week dateline (sheet 8, 2:11).
- The blue term and "P(+ ∣ not listed) ↓" (sheet 11, 3:01).
- The Cardiff word load is down to about 12 prose words (kf 2:24.2).
- No ring overlaps in the fail beat (kf 1:08.6).
- The landing says "The title's…".
- The second "nine thousand nine hundred eighty" is cut.
- The half-sick grid is a clean block (kf 0:40.8).
- The squares file into the raster blocks (f 2:30.2).
- Above all, the fail is now one continuous prevalence slider with the meter falling live (sheet 3, 0:47–0:53). That is the episode's own signature image, and it is run backwards in the landing (3:13–3:21).

## Why it is not a 9

**Hook 8.5.** It is concrete from frame 1, with a commit and a hold by 0:15, stakes from a real study, and an ending that resolves the opening's diagram. The ceiling is the puzzle itself: it is the best-known Bayes setup on YouTube. 3Blue1Brown's *The medical test paradox* (2020) and Veritasium's *The Bayesian Trap* (2017) both use a 1-in-N disease and a 99% test. A large share of this channel's audience will commit to "low, it's the base-rate thing", so the "likely-wrong prediction" the 9 anchor asks for is not reliably wrong. Nothing in 0:00–0:15 is new to those viewers. The Cardiff numbers, which are new, sit at 2:09.

**Clarity 8.5.** The derivation is clean, justified at every step, and checks out to the decimal. A viewer could re-derive it after one watch. Two precision problems remain, both in the episode's terminology, which matters because the closing line is a lesson about terminology:
1. Three names for one family of numbers drift. At 0:23 the respondents' 95% (really 1 − false-positive rate) is called "their test's own accuracy", with the tag "their test: 95% accurate". The title says "99% accurate". The closing line at 3:21.8 then says "the title's ninety-nine percent is the test's recall". That is true here only because sensitivity = specificity = accuracy = 99%, and the video never says so. A viewer can leave thinking "accurate" means recall.
2. The 46% at 3:03 is the operators' first call. The same page of Davies et al. reports that 7 of those 22 were stopped and turned out to be false positives. The episode presents the 46% as a clean outcome, which misses the SMH "show where the fixed method still fails" note that is sitting in the source.

There is also a smaller implied claim. During the beam sweep (2:25–2:31), the 61 unflagged red "listed" squares are dimmed as "cleared". That implies 61 listed people were present and missed, a recall of about 14% that no source supports, since 1,200 images is only an upper bound on who was there.

**Visual 8.5.** The semantic palette holds for the whole runtime: red = has it, blue = doesn't, yellow = positive, grey = naive or secondary, green = correct. Most frames have one focal point, the LaTeX is clean, and the citations sit bottom-left at full size. Minor issues:
1. In flight, the flagged squares cross the ghosted meter title (f 2:30.2: a square sits on the "c" of "chance").
2. At 1 in 500 the 20 surviving sick all lie in the left ~45% of the grid (kf 0:56.5, kf 1:08.6), a residue of the right-edge drain. It reads as spatial clustering, which carries no meaning.
3. At 2:43–2:47 the "your test 17% / precision too" ghost meter adds a third bar beside the 7% meter, and the landing repeats that link anyway (3:28).

**Motion 9.** Objects persist and transform throughout:
- The diagram morphs into the table (0:31–0:35).
- The slider drives grid, table and meter from one N (0:47–0:53).
- The 120 positives become dots, then the strip that docks under the meter (1:19–1:27).
- Formula terms fly out of the table and the arrows (1:37–1:45).
- One ÷ 10,000 move rolls every number in the table and formula (1:45–1:49).
- The 120 dots spread into the crowd (2:07).
- The flagged squares file into the raster (2:29–2:31).
- The raster collapses into the + disk (3:05–3:06.6).
- The flows swell to people-width (3:09).

The static maximum is 3.0 s, at the planned end hold.

**Audio 8.5.**
- Pace (147 wpm), loudness, true peak and silences are all on target.
- Deictics land: "these 120 people" with the yellow outline (1:25), "red share of this crowd" with the brackets (1:31), "these are how common" with the braces (1:53).
- Shaped cadence gives real pauses after "Seventeen percent" and "Six times too high" (1:05.6–1:06.8, 1:10.2–1:11.3).
- The weak spot is 2:44.8–3:05: two long sentences joined into a 12.4 s run with no breath. The 29-word "Months later, a new algorithm, better photos and practised operators thinned out the false alarms, the blue term in Bayes' denominator, and their count rose to forty-six percent" stacks a three-item list, an appositive and the result, and it is the most number-dense, idea-dense passage in the episode.

**Concision 9.** 470 words in 3:34. I could not find a sentence whose removal loses nothing. The 3% sentence is what makes the 46% a same-method comparison. "One percent sounds small…" names the cause of the failure. The repeated "one in five hundred" (0:00, 0:52, 3:12) is a deliberate callback each time.

**Originality 8.5.** These are fresh and memorable:
- The half-sick control where the naive rule works.
- The live prevalence slider and its reversal in the landing.
- The people-width flows.
- The Cardiff crowd collapsing into a 2,470-cell raster with the meter docked on it.
- The "other lever" (P(+∣not listed) ↓), which shows precision rising with no change in base rate.

But the frame the viewer meets first, and the core picture (restrict to positives, take the share), are the canonical ones (see Hook).

## FIXES (highest impact first)

1. [3:21.8–3:32.6 and 0:23–0:29][Clarity] The "accurate" → "recall" slippage.

   (a) Change the closing two sentences from "The title's ninety-nine percent is the test's recall: how often the sick test positive. Seventeen percent is its precision: how often the positive are sick." to "The title's ninety-nine percent describes the test: its recall, how often the sick test positive. Seventeen percent describes your result: its precision, how often the positive are sick." That adds 4 words (about 1.5 s) and turns the last line into a test-versus-result chiasmus that re-reads the title. Keep the "recall" / "precision" tag animation as is.

   (b) Change the waffle tag "their test: 95% accurate" to "their test: 5% false alarms" and keep the narration. The on-screen text then states what Manrai's respondents actually read, and the spoken "their test's own accuracy" stays a correct interpretation.

   Expected effect: Clarity +0.5.
2. [2:44.8–3:05.0][Audio/Clarity] Split the 12.4 s breathless run. Change the narration to: "Cardiff University's evaluators counted only alerts the logbooks confirmed: three percent. [pause 0.6] Months later, a new algorithm, better photos and practised operators thinned out the false alarms. [pause 0.4] That's the blue term in Bayes' denominator. [pause 0.3] Their count rose to forty-six percent. [pause 0.8]" Retime the "P(+ ∣ not listed) ↓" label to start on "blue term" and the bar's red growth to "rose". This costs about 1.5 s and is the episode's only hurried passage. Expected effect: Audio +0.5.
3. [3:03–3:05][Clarity/honest limit] Davies et al. report that 7 of the 22 Six Nations "true positives" were stopped and turned out to be false positives. After the evaluators' bar reaches 46%, add a grey Text tag under its right label, font_size 20: "7 of the 22 later cleared" (5 words). Hold it 2.0 s through the existing 0.8 s pause and into "Back to your test", then fade it with the Cardiff picture. No narration change. If a spoken version is preferred, use "…rose to forty-six percent, though seven of those turned out wrong." (+7 words). This is the SMH honest outcome the source already provides.
4. [2:25–2:31][Clarity] The beam's dimming of the 61 unflagged red squares as "cleared" implies a measured recall of about 14%, which no source gives. In the sweep, apply the same dim to unflagged squares regardless of colour: red and blue both go to 35% opacity, with no separate "cleared listed" treatment. Then only the flagged squares, with yellow rings, carry information, and the "≤ 1 in 140" legend keeps the upper-bound meaning.
5. [2:28–2:31][Visual] Flagged squares cross the ghosted title "chance an alert is right" in flight (f 2:30.2). Give the flight a path_arc that passes below y = −0.3 (under the meter), or fade the ghost title to 0.15 opacity for the 1.5 s flight and restore it on "Shrink to the alerts".
6. [0:52–1:16][Visual] At 1 in 500 the 20 sick all sit in the left ~45% of the grid (kf 0:56.5). In the last 0.8 s of the slider, as the label reaches "1 in 500", swap each remaining red cell with a random blue cell elsewhere in the grid. Use one smooth 0.8 s cross-fade in place, with no travel, so the 20 end uniformly scattered before the rings appear on "twenty sick people". Keep the counts and meter untouched.
7. [2:43–2:47][Visual/Concision] The "your test 17% / precision too" ghost meter is a third bar in the frame, and the landing makes the same link at 3:28. Cut the ghost meter. Keep "precision" rolling in as the main meter's title on the word. That frees the frame for the evaluators' bar to enter 2 s earlier, on "Cardiff University's".
8. [0:00–0:15][Hook/Originality, structural] The cold open is the canonical rare-disease puzzle. Fixes 1–7 cannot lift Hook or Originality to 9; see below.

## REACHES 9 IF ALL FIXED: no, narrowly

Fixes 1–7 plausibly lift Clarity to 9, Audio to 9 and Visual to 9, with Motion 9 and Concision 9 unchanged. That gives (8.5·15 + 9·25 + 9·15 + 9·15 + 9·10 + 9·10 + 8.5·10)/100 = 8.88, or about 8.9.

The binding limit is structural. The first 15 seconds are the textbook puzzle that this channel's audience has most likely already seen, so Hook and Originality stay at 8.5. Two ways past it:

1. **Open on Cardiff.** Use frame 2:31, with the 2,470-cell raster and the ghosted "chance an alert is right ?": "Cameras at the 2017 Champions League final in Cardiff flagged 2,470 faces as wanted. How many were? Pick a number." Viewers have not met that puzzle, and 7% is a real surprise. Then run the disease case as the controlled build (half sick works, slide to 1 in 500 fails 6×, shrink, Bayes). Return to Cardiff for the 7% resolution and the 3% → 46% second lever. Land on "the test versus your result". About 10 s of narration moves, and the runtime is roughly unchanged.
2. **Keep the disease open but make savvy viewers commit too.** After "Pick a number", add one beat at 0:13: "If you know this is a trick, guess how low." Then make the half-sick success and the slider the surprise for both groups. This is a weaker fix; I'd expect Hook at 9 only if the payoff then visibly overturns the savvy guess as well.

## KEEP

- The live prevalence slider (0:47–0:53). One N drives the grid, table and meter, and the meter falls from the naive marker to 17% before anything is explained. It is run backwards in the landing (3:13–3:21, "1 in 2 … 99, where the rule held"). This is the episode's own image.
- The one continuous insight picture (1:16–2:06): survivors → 24 × 5 strip under the meter → brackets → terms flown from the table → a single ÷ 10,000 move → braces → names → Bayes, with "shrink" and "take the share" boxed on their words.
- The Cardiff second lever (2:51–3:05). The evaluators' same-method 3% → 46%, tied to "P(+ ∣ not listed) ↓", shows that precision can be raised without changing the base rate. Every number in it is traceable to Davies et al. or the BBC.
