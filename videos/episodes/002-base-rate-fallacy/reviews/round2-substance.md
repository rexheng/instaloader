# Round 2 review (substance: science + story editor), episode 002

Evidence used: `review/` pack (metrics.json 14:06 is newer than final.mp4 14:04, so no new pack was generated); report.md; all 13 contact sheets; keyframes kf_01, 03, 05, 10, 13, 16, 19, 20, 26, 31, 33, 37, 40 at full resolution; 9 extra frames pulled with ffmpeg (0:26.6, 1:44.3, 2:04.6, 2:05.6, 2:16.0, 2:16.8, 2:24.5, 3:16.5, 3:35.5); transcript.txt + transcript_words.tsv; narration.txt; script.md; facts.md; CHANGELOG.md. Sources checked on the web (see FACTS). I wrote this before reading the round-2 craft review.

```
EPISODE: 002 — "When a 99% Accurate Test Says You're Sick"
IDEA: A positive result doesn't give you the test's 99%. It shrinks the sample space to the people who tested positive, and when the condition is rare that crowd is mostly false alarms; Bayes' theorem (and ML "precision") is just that share.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8.5 · Motion 9 · Audio 8.5 · Concision 8 · Originality 7
WEIGHTED: 8.4 (837.5/100 = 8.375)   AFTER CEILING: 8.4 (ceiling = 7 + 2 = 9.0, not binding)
CAPS: none
FINAL: 8.4   PASS: no
```

## FACTS

| Claim (spoken / on screen) | Status | Source / check |
|---|---|---|
| Premise 1 in 1,000; catches 99%; wrongly flags 1% of healthy; title "99% accurate" | Verified (premise) | With sensitivity = specificity = 0.99, accuracy is 99% at any prevalence, so the title is honest |
| "That's 9%" (10 of 110) | Verified | 10/110 = 9.09%; exact 0.99·0.001 / (0.99·0.001 + 0.01·0.999) = 11/122 = 9.02% |
| "11 times too high" | Verified | 0.99 / 0.0902 = 10.98 |
| Half-sick check: 4,950 + 50 positives, "of the 5,000 who lit up, 99% are sick" | Verified | 4,950/5,000 = 0.990 |
| 10 sick → "about 10" positive; 9,990 healthy → "about 100" | Verified | 9.9 and 99.9 expected; labelled "expected counts", later shown exactly as 9.9 / 99.9 (1:39, 1:45) |
| 10 × 0.99 / (10 × 0.99 + 9,990 × 0.01) ≈ 9% | Verified | 9.9 / 109.8 = 0.0902 |
| ÷ 10,000 → 0.001 / 0.999; the named form is Bayes' theorem | Verified | Re-derived: P(s∣+) = P(s)P(+∣s) / [P(s)P(+∣s) + P(h)P(+∣h)]; denominator is the law of total probability |
| Sweep: 50% at 1 in 100; 99% at 1 in 2; 98% at 1 in 3 (frame 3:31) | Verified | 0.0099/0.0198 = 0.500; 0.495/0.500 = 0.990; (0.33)/(0.3367) = 0.980 |
| Landing flows "10 … along the red, 100 along the blue" | Verified | Widths 0.0446 : 0.4504 = 9.9 : 99.9 |
| Cardiff, 2017 Champions League final: 2,470 alerts, 173 right, 7% | Verified | BBC News, 4 May 2018: "out of the 2,470 potential matches with custody pictures … 2,297 were wrong" (on the day of the final, about 170,000 people in Cardiff). 2,470 − 2,297 = 173; 173/2,470 = 7.0% |
| "In a football crowd, almost nobody is on it" | Unverifiable (plausible premise, no number) | Not quantified on screen. The same BBC piece says South Wales Police blamed the false matches on "poor quality images" from UEFA and Interpol and on it being the first major deployment. The video leaves that out (see fix 4) |
| "That share has a name, precision" | Verified | TP / (TP + FP) |
| Gigerenzer, 2007: 160 gynecologists; 1% / 90% / 9%; best answer about 1 in 10 | Verified | Gigerenzer, Gaissmaier, Kurz-Milcke, Schwartz & Woloshin (2007), *Psychological Science in the Public Interest* 8(2):53–96, p. 55: "At the beginning of one continuing-education session in 2007, 160 gynecologists …" with options A 81%, B 9 in 10, C 1 in 10, D 1% |
| "Only 21% chose it, fewer than blind guessing would get" | Verified | Paper: "slightly less than chance (21%)"; 4 options → 25% |
| Most common answer 90%; bars 47 / 13 / 21 / 19 before, 6 / 1 / 87 / 6 after | Verified | Read off Fig. 2 (rendered at 600 dpi): before 47, 13, 21, 19; after 6, 1, 87, 6 |
| "After a session on turning those percentages into counts … 87% chose 1 in 10" | Verified | Paper: "After learning … natural frequencies … 87% of them now understood that 1 in 10 is the best answer" |
| Cold open "Most doctors given a problem like this got it wrong" + "gynecologists / 21% got it right" | Verified | Same source, cited on screen at 0:14–0:20 |

No wrong or fabricated claims. Every number recomputes.

## MECHANICS

runtime 3:46.5 · 155 wpm (speech time; 150 overall) · max internal silence 2.06 s (the planned "Pick a number" hold, 0:16.7–0:18.8) · leading 0.00 s / trailing 1.76 s · max static 2.9 s · −14.0 LUFS / −2.1 dBTP · WER 2.7% · 0 banned phrases.

None of these trigger a cap. The transcript's "becomes a a fraction" at 1:51.9 has overlapping word timestamps (111.86–112.06 and 111.90–112.06), so it is a Whisper duplicate, not a TTS stutter. The "a" → "one" and "twenty oh seven" → "two thousand seven" diffs are ASR number normalisation. "Gigerenzer", "gynecologists", "Cardiff" and "precision" all transcribe correctly.

## Transcript / slop (BAR §4)

- No banned phrases. No rhetorical-question chains: there is exactly one question (0:09–0:12). No "it's not just X". No list ending.
- Borderline cases, not counted: "that share has a name, precision" (2:33, a colon reveal, but it does carry information); "All it does is…" (2:08).
- Deictics land on their referents:
  - "these 110 people" at 1:23: the strip finishes forming at 1:23.
  - "this crowd" at 1:27.
  - "this table" at 1:33: the table's "10" pulses at 1:35.
  - "These two … These two" at 2:01 / 2:03: the terms morph to P(sick) / P(healthy) and then P(+∣·).
  - "this version" at 2:44: the mammography diagram is drawn at 2:43.
  - "this plus sign" at 3:31.

## What works

- **Structure.** The naive rule is tested where it works (half sick, 0:27–0:43), then where it fails (0:44–1:10), and the failure is measured with an "11× too high" brace on the meter (1:09). The landing sweep comes back to the half-sick case: "99 at 1 in 2, where the rule held" (3:27). It is a real SMH-style build-fail with a payoff that explains *why* the naive check passed.
- **The one picture.** The 110 survivors swell into a 22 × 5 strip hung under the meter, with the 2 red columns exactly under the 9% red segment (kf_13). The fraction is built from the braces (kf_16), then made exact and named (kf_19, kf_20). In Cardiff the same strip becomes a 2,470-cell raster under a bar of the same width, so the 173 red cells sit under 7% (kf_26).
- **Closing line.** "99% is how often the sick test positive. 9% is how often the positive are sick." It re-sees the cold-open diagram, where flow width now encodes people, not rates (3:35).

## Where it falls short of 9 (evidence)

1. **Originality: both anchor examples come from the two reference channels' own Bayes videos.**
   - The cold-open numbers (0.1% prevalence, 99% test, answer 9%) are exactly Veritasium's *The Bayesian Trap* (2017).
   - The payoff (2:37–3:13) is 3Blue1Brown's *The medical test paradox* (2020) almost beat for beat. That video has the same Gigerenzer 2006/07 gynecologist seminars and the same 1% / 90% / 9% problem, and the same punchline: "Only a fifth of them gave the correct answer, which is worse than what it would have been if everybody had randomly guessed." This video says: "Only 21% chose it, fewer than blind guessing would get" (2:56).
   - A viewer who knows the genre's two best-known Bayes videos will recognise both.
   - The fresh parts are the Cardiff precision raster and the half-sick → sweep rhyme. → Originality 7.
2. **Concision.**
   - The 9% is computed in words twice within 25 s: "So of 110 positives, only 10 are sick. That's 9%" (1:00–1:05), then "10 out of 10 plus 100, about 9%" (1:28–1:32).
   - The 21% stat is given at 0:15 (on screen, "21% got it right") and again at 2:56.
   - The Gigerenzer beat spends 16 s re-reading a problem with the same structure (2:39.6–2:55.6).
   - Runtime is 3:46 against a 3:00 template. → 8.
3. **Hook.**
   - The question lands at 0:12.5, but the commit prompt "Pick a number" comes only at 0:16.9, after "Most doctors … got it wrong" (0:12.5–0:15.9).
   - That line and the green "21% got it right" waffle (0:15) tell the viewer the obvious answer is wrong *before* they commit, which softens the misconception.
   - The tension sags through the 26 s of algebra (1:32–1:58) and the Gigerenzer restatement. → 8.5.
4. **Clarity.**
   - (a) In Cardiff, "In a football crowd, almost nobody is on it" (2:16) followed by the 7% implies that the base rate is the whole story. The police's own explanation (poor-quality watch-list images, first deployment, BBC 2018) and the second necessary ingredient (a non-zero per-face false-match rate) are never mentioned. facts.md notes this caveat; the viewer never gets it.
   - (b) At 1:35–1:39 the strip's "10" (sick people who tested +) expands into "10 × 0.99", where the 10 is now sick *people*. The same glyph stands for two different quantities. The table's 10 → 9.9 morph (1:39) rescues it, but only for a viewer looking at the dimming table on the right while the equation changes on the left. → 8.5.
5. **Visual (minor, cited).**
   - 0:15–0:19 (kf_03): about 18 prose words on screen, counting the 8-word citation (cap is 12): 1 in 1,000 / sick / healthy / you / chance you're sick / gynecologists / 21% got it right / citation.
   - 2:24.5 (extra frame): during the strip → raster morph, the raster's bottom row spills below the yellow outline.
   - 2:57–3:03 (kf_31): the 79 leftover grey waffle dots sit *inside* the chart's plot area between the 25 and 75 gridlines, next to the "guessing: 25%" line, where they read as data.
   - 2:17 (sheet 8): the title has already become "chance you're on the list" while the meter still shows the disease's 9% for about 1.5 s.
   - None of these is overlap or clipping at cap level. → 8.5.
6. **Motion.** Objects persist and transform throughout:
   - diagram → table (0:26)
   - grid → strip (1:19–1:23)
   - strip → raster (2:24–2:29)
   - waffle → bars (2:57–3:05)
   - chart → diagram morph (3:13–3:17)
   - rates → flows (3:20)

   Only nitpicks remain, such as the double-struck "9%" while the label flies at 1:31. → 9.

## FIXES (highest impact first)

1. **[2:37–3:13] [Originality / Concision] Cut the payoff that duplicates 3Blue1Brown and keep the part that is about this video's method.**
   - Delete:
     - the full mammography problem (2:39.6–2:55.6)
     - the "fewer than blind guessing" clause (2:56–3:00.7)
     - the "most common answer was 90%" line (3:01–3:06)
   - Replace the whole beat with about 10 s that morphs the cold-open waffle *in place*. The 21 green dots grow to 87, with no new chart: "Those gynecologists? After one session turning percentages into counts of women, which is exactly what we just did with ten thousand people, 87% got it right."
   - Keep the citation on screen.
   - Effect: saves about 25 s (runtime about 3:20), turns the training result into proof that the counting picture works, and removes the near-verbatim 3b1b line.
2. **[0:00–0:19] [Hook / Originality] Stop opening on Veritasium's exact numbers.** Two options:
   - **Recommended (structural):** open cold on the Cardiff raster.
     - Narration: "At the 2017 Champions League final, police cameras flagged 2,470 faces as wanted people. How many really were? Pick a number." Hold 1.5 s.
     - Then: "To see why, shrink it to a disease." The current counting build follows unchanged.
     - The precision beat (2:14–2:37) becomes the landing that resolves the open: 173 of 2,470, 7%.
     - End on the existing recall/precision chiasmus.
   - **Minimum:** keep the disease, but change the premise numbers so they no longer reproduce the Bayesian Trap (for example 1 in 500, 98%, 2%, giving about 9%: 0.98·0.002 / (0.98·0.002 + 0.02·0.998) = 8.9%, so the 10/100/110 picture becomes 20/200/220 per 10,000).
   - Either way, the viewer commits to a guess that is not a known YouTube answer.
3. **[0:09–0:19] [Hook] Move the commit before the hint.**
   - Narration order becomes: "…what's the chance you're sick? Pick a number." [hold 1.6 s] "Most doctors given a problem like this got it wrong."
   - Fade the waffle in only *after* the hold.
   - The commit then lands at about 0:13 instead of 0:17, and the doctors' failure becomes a reveal instead of a spoiler.
4. **[2:14–2:20] [Clarity] Give Cardiff its second ingredient and its honest limit.**
   - Change "In a football crowd, almost nobody is on it." to "In a crowd of 170,000, almost nobody is on it, so even a small error rate per face swamps the real matches."
   - After "only 173 were right, 7%", add one grey line on screen for at least 3 s, just above the citation: "police also blamed poor-quality photos".
   - Source: BBC News 2018. The crowd figure is on the same page.
5. **[1:32–1:40] [Clarity] Stop one glyph meaning two quantities.**
   - Before expanding, morph the strip's red "10" into "9.9", saying "that ten was really nine point nine".
   - Then build "10 × 0.99" with `TransformFromCopy` from the table's *people* column "10" and its "99%" arrow label.
   - Do the same for 100 → 99.9 → 9,990 × 0.01.
   - Narration: "Those counts came from this table: that ten was really nine point nine, ten sick people times ninety-nine percent…"
6. **[1:24.9–1:32.1] [Concision] Remove the second spoken "about 9%".**
   - Keep "Your chance of being sick is the red share of this crowd. Ten, out of ten plus a hundred."
   - Let "≈ 9%" fly in from the meter silently. That saves about 2 s and avoids explaining the same thing twice.
7. **[3:37–3:45] [Clarity / Originality] Name the two numbers in the episode's own data-science terms.**
   - As "how often the sick test positive" is spoken, write a small grey "recall" under the red arrow's "99%".
   - As "how often the positive are sick" is spoken, write "precision" under the meter's "9%".
   - The narration stays the same. This ties the ending to the Cardiff payoff and gives a data-science viewer a term to keep.
8. **[2:57–3:03] [Visual] Move the 79 leftover grey waffle dots out of the plot area.**
   - Before the bars grow, shift the waffle to x ≥ 3.6 (right of the 100 tick and left of the diagram), or fade it to 30% outside the axes.
9. **[2:23.5–2:26] [Visual] Fix the outline during the strip → raster morph.**
   - Animate the yellow outline's resize in the same `AnimationGroup` as the raster (or resize it first), so no cells spill below it (frame 2:24.5).
10. **[2:15–2:18] [Visual / Clarity] Reset the meter before the new title.**
    - Reset the meter to "?" *before*, or together with, the title morph to "chance you're on the list". It should never show the disease's 9% under the watch-list title (2:17).
11. **[0:14–0:20] [Visual] Bring on-screen prose down to 12 words or fewer.**
    - Shorten the cold-open citation to "Gigerenzer et al., 2007 · Psychol. Sci. Public Interest".
    - Merge "gynecologists" and "21% got it right" into one label: "gynecologists: 21% right".
12. **[1:30.5–1:31.5] [Motion] Stop the double-struck "9%".**
    - Dim the meter's own "9%" to 40% while its copy flies to the equation.

## REACHES 9 IF ALL FIXED

Yes, but only with the structural fixes 1 and 2.

- Polish alone (fixes 3–12): Hook 9, Clarity 9, Visual 9, Motion 9, Audio 8.5, Concision 8.5, Originality 7. That gives 8.8, still short.
- With the 3b1b payoff cut and a hook that isn't Veritasium's numbers: Originality 8.5, Concision 9, Hook 9 or more. That gives 9.0 to 9.1.

The problem is not the craft, which is already near 9. It is that both of the episode's anchor examples belong to the two reference channels.

## KEEP

1. The half-sick check that works (0:27–0:43) and the landing sweep that returns to it: "99 at 1 in 2, where the rule held" (3:27).
2. The 110-person strip hung under the meter, red columns under the 9% (kf_13), and its reuse as the same-width 2,470-alert raster for precision (kf_26).
3. The closing chiasmus over flows whose width is people ("99% is how often the sick test positive. 9% is how often the positive are sick.").
