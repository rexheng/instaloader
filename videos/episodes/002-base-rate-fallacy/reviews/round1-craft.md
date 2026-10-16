# Round 1 review: craft (motion design, visual design, A/V sync)

Critic: independent craft critic (visual design, motion, audio/visual sync); every dimension is scored.
Evidence: `review/` pack (metrics.json 01:24, newer than final.mp4 01:23), all 13 contact sheets, 13 full-res
keyframes (kf_01, 05, 07, 08, 14, 17, 21, 24, 26, 27, 29, 40) and 12 extra ffmpeg frames (0:29.0, 0:47.5,
1:00.5, 1:27, 1:38, 2:01, 2:16.5, 2:41, 2:57, 3:06, 3:27, 3:34). I also made a crop of the 2:42.7 brace and
re-transcribed 2:39.5–2:46.5 to check the "police" word the review kit's diff flagged as deleted.

```
EPISODE: 002 — "When a 99% Accurate Test Says You're Sick"
IDEA: A positive result shrinks the sample space to the people who tested positive. When the disease is rare,
      false alarms from the huge healthy group dominate that crowd, so the chance you're sick is 17%, not 99%.
      That share is Bayes' theorem, and in machine learning it is precision (the 99% is recall).
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8 · Motion 8.5 · Audio 8.5 · Concision 8 · Originality 8.5
WEIGHTED: 8.4   AFTER CEILING: 8.4  (lowest 8 + 2 = 10, so the ceiling does not bind)
CAPS: none (checked every BAR §3 trigger; evidence below)
FINAL: 8.4   PASS: no
FACTS:
- 1 in 500, 99% sensitivity, 1% FPR → 20 sick → 19.8 +, 9,980 healthy → 99.8 + → 99/598 = 16.6% ≈ 17% | Verified | recomputed
- 20/(20+100) = 16.7% → "17%"; 0.99/0.166 = 5.98 → "six times too high" | Verified | recomputed
- Half sick: 4,950 + 50 = 5,000 positives, 4,950/5,000 = 99% | Verified | recomputed
- 20/10,000 = 0.002, 9,980/10,000 = 0.998; Bayes form with total probability in denominator | Verified | derivation
- Accuracy (TP+TN)/N = (19.8 + 9,880.2)/10,000 = 99.0%; "everyone healthy" = 9,980/10,000 = 99.8% | Verified | recomputed
- Prior 1/100 → 0.0099/0.0198 = 50%; prior 1/2 → 0.495/0.500 = 99% | Verified | recomputed
- Recall = P(+|sick) = 99%; precision = P(sick|+) = 17% | Verified | definitions
- Manrai et al. 2014, JAMA Intern. Med. 174(6):991–3: 61 respondents, 14 right (23%), most common answer 95% (27/61 = 44%) | Verified | jamanetwork.com/…/1861033; PMC4955674
- "Most doctors and medical students… got it wrong" (77% wrong; 51 doctors + 10 students) | Verified | same
- "Their most common answer was the test's own accuracy" (95% = accuracy of a perfectly sensitive test with 5% FPR) | Verified (interpretive; see fix 4) | same
- Cardiff, 2017 UCL final: ≈170,000 people, 2,470 alerts, 2,297 wrong, so 173 right = 7.0% | Verified | BBC News, 4 May 2018
- ≈1,200 images on the watch lists | Verified (as cited in facts.md, p. 10) | Davies, Innes & Dawson 2018, Cardiff Univ. UPSI
- Evaluators: 3% true positives at the final → 46% at the Six Nations (new algorithm; only high-standard custody images afterwards) | Verified | Davies et al. 2018 exec. summary (cardiff.ac.uk AFRReportDigital.pdf)
MECHANICS: runtime 3:42.9 · wpm 152 (speech time) · max silence 2.16 s (0:13.4–0:15.5, the planned
           "pick a number" hold) · max static 3.57 s (2:55.0–2:58.6) · −14.0 LUFS / −2.1 dBTP ·
           leading 0.00 s / trailing 1.73 s · 0 banned phrases · WER 2.7%
```

## Cap check (none triggered)
- **Sync:** every spoken referent lands within ±2 s except one: "Swap the disease for a police watch list" (2:13.5–2:17.7). At 2:15 the frame is a half-faded title and a draining bar, and no watch list is shown until 2:26 (kf_26 at 2:20.4, sheet 9 at 2:27). That is one miss; the cap needs ≥ 2. Checked and fine: "most doctors" → waffle 0:17; "most common answer" → "44% said 95%" 0:21; "10,000 people" → header 0:31; "20 sick people" → table 0:51; "17%" → meter 1:07; "these 120 people" → yellow outline 1:27; "2,470 alerts" → raster label 2:39; "three percent" → tick 2:55; "forty-six" → tick 3:01; "99% accuracy is real" → bar 3:09; "1 in 100… 50%" → label and meter 3:25.
- **Transcript diff "police" deleted at 2:42.8:** this is a Whisper miss, not a dropped line. Re-transcribing 2:39.5–2:46.5 gives "…take the red share. Police counted 173 as right, 7%", with "Police" at 2:42.0.
- **Text and layout:** the layout audit found 0 issues in 207 frames. The keyframes show no clipping and no text overlap. The dashed markers that cross bars (naive 99% marker, the 3% tick) are deliberate markers, not overlaps. I found no typos or broken LaTeX.
- **Citations:** every empirical claim has an on-screen citation (Manrai 0:16–0:26; BBC 2:18–3:03; Davies 2:26–3:03).
- **Ending:** the end card (3:41–3:43) is title-only, with no recap and no subscribe request.

## What the flipbook shows (by beat)
- **0:00–0:15 cold open (strong).** The first frame is the object itself: "1 in 500", red sick, blue healthy, and a ghosted meter (kf_01). The arrows grow on their rates, "you" rings on "yours says positive", and "Pick a number" gets a real 2.1 s hold. The commit lands at 0:13, about a second after the BAR §3 "9" anchor of 0:12.
- **0:15–0:27 doctors.** The waffle and citation are clean (kf_05). But the screen reads "44% said 95%" while the voice says "the test's own accuracy, here ninety-nine percent". The viewer is never told that the doctors' test was a different one, 95% accurate, so it is a one-rewatch moment (fix 4).
- **0:28–0:31 diagram → table.** The diagram breaks into unlabelled fragments: bare dots, detached arrows, and the + parked top-right (frame 0:29.0). It looks like a crossfade with motion rather than a morph that carries meaning (fix 8).
- **0:31–0:45 naive build.** The counts tick, the beam sweeps, and the meter fills to 99% on the naive marker. Every motion here encodes something. Good.
- **0:45–1:17 fail.** The prevalence drop is animated (4,662 → 514 → 20, sheets 3–4). The 17% fill and the "6× too high" brace are well timed. **The main visual flaw is here:** the 20 sick people get 50 px red rings, while the 100 false positives are ~6 px lit squares in a 100 × 100 grid (frame 1:00.5, kf_14). At a glance the eye counts the red rings, so the frame's visual weight says the opposite of the narration ("of 120 positives, only 20 are sick"). The "1% of nearly everyone" brighten at 1:17 does not fix it, because it brightens all 9,980 people, not the 100 who matter (fix 1).
- **1:17–2:13 insight (the best stretch).** The negatives vanish, the 120 swell and line up into a 24 × 5 strip, and the meter docks onto it so its 17% red segment sits exactly over the 4 red columns (kf_17). Braces count "20" and "100", the labels fly into the fraction, the table's 20 and 100 become 19.8 and 99.8 as the terms expand (kf_21), and the named Bayes form arrives with the yellow box on "shrink" (kf_24). This is close to 3b1b-grade.
  - The weak spot is the ÷10,000 sub-beat (1:47–2:01): 14 s in which the formula does not change from 1:47 to 1:59, the table relabels two numbers, and the stretch includes a 3.4 s static hold (1:53.3–1:56.7) (fix 5).
- **2:13–3:03 Cardiff.**
  - The bridge at 2:15 is a nearly empty frame (fix 6).
  - The crowd is a 100 × 100 grid of ~6 px dim-blue squares (kf_26). On a laptop it reads as a dark texture, and it will moiré under YouTube compression. For 15 s the right half below the meter is empty, and the legend is squeezed into the lower middle (kf_27) (fix 7).
  - The beam, the flagged squares flying into the 2,470-cell raster, and the meter filling to 7% over the red columns are excellent continuity (sheets 9–10).
  - The narrow red brace under the 173 red columns renders as a malformed "bird" glyph from 2:42 to 3:03 (crop of kf_29; frame 2:57) (fix 2).
  - Three precision numbers sit on one bar: the 7% fill, a 3% tick drawn *inside* the red fill, and a 46% tick (frame 2:57; sheet 11 at 3:01). A viewer will ask "so which is it?" (fix 3).
- **3:03–3:41 landing.** The raster collapsing into the + disk is a lovely rhyme with the cold open. The live sweep, where flow widths, label and meter are driven together and the naive marker returns at 1 in 2 (frame 3:27), is the most memorable image in the episode. The closing chiasmus writes "recall" and "precision" on their words (frame 3:34).
  - The landing still carries three separate moves in 38 s: the accuracy paradox (3:05–3:15), the prevalence sweep (3:15–3:30) and the recall/precision definitions (3:30–3:41). BAR §6 asks for one return and one line in about 15 s (fix 9).

## Scores, with evidence
- **Hook 8.5:** concrete first frame, a genuine commit with a hold, and tension that rises (works at 1 in 2, fails 6× at 1 in 500). It loses half a point for the commit landing at 0:13 rather than by 0:12, and for the mid-episode sag at 1:47–2:01.
- **Clarity 8.5:** concrete before abstract, every number checks, assumptions are stated ("assumes a random screen"), and the derivation is fully justified. It loses points for the 95% vs 99% mismatch (0:21–0:26), the inverted visual weight of the false positives (0:53–1:20), and the three-number precision bar (2:55–3:03).
- **Visual 8:** the semantic palette is excellent and stays consistent from start to end (red/blue/yellow/grey/green), the type is all legible, and the safe area is clean. Against that: fix 1 (focal point on the wrong group), the malformed brace (2:42–3:03), the low-contrast moiré-prone crowd and lopsided composition (2:16–2:31), and the tick-inside-fill clutter (2:55). That is more than "at most 2 minor issues".
- **Motion 8.5:** objects persist all the way through (the meter is never recreated), the formula is built by fly-ins from braces and the table, and the raster becomes the + disk. It loses points for the fragmenting transition at 0:28–0:31, the near-empty bridge at 2:15, and the ÷10,000 stretch where the formula is static for 12 s.
- **Audio 8.5:** 152 wpm with intentional pauses (1.1 s before "the rule said", 2.1 s commit hold), loudness on target, and deictics such as "these 120 people" landing on the outline. One deictic has nothing to land on (2:13.5).
- **Concision 8:** about 10–12% is removable. The ÷10,000 sub-beat could be roughly halved, and the landing's accuracy-paradox move is a second idea competing with the chiasmus.
- **Originality 8.5:** the topic is the most-covered one in the genre (3b1b's *The medical test paradox*, Veritasium's *The Bayesian Trap*). It earns its place through the channel-name framing ("shrink the sample space"), the Cardiff face-recognition payoff with honest police-vs-evaluator counts, and the recall/precision chiasmus.

Weighted = (8.5·15 + 8.5·25 + 8·15 + 8.5·15 + 8.5·10 + 8·10 + 8.5·10)/100 = 837.5/100 = **8.4**.

## FIXES (highest impact first)
1. **[0:51–1:20][Visual + Clarity] The false positives are visually weaker than the true positives.** The 20 sick wear 50 px red rings; the 100 lit healthy are ~6 px squares (frame 1:00.5, kf_14).
   - Mark the 20 sick at 0:51 by scaling their squares ×3 (red fill, no ring).
   - When the beam passes, give **every** positive the same yellow ring (yellow = positive in the palette) and scale the 100 lit healthy squares ×3 as well, so 100 yellow-ringed blue squares visibly outnumber 20 yellow-ringed red ones.
   - On "one percent of nearly everyone" (1:13–1:18), pulse only those 100 ringed blue squares instead of brightening the whole grid.
2. **[2:42–3:03][Visual] The red brace under "173 right" renders as a malformed bird-shaped glyph** (crop of kf_29). Replace it with a straight bracket (a Line with two 0.12-unit end ticks, red, stroke 4) the width of the red columns, or drop it and point "173 right" at the columns with a short red Arrow. Check the 1:31 "20" brace under the 4 red strip columns too: if it is narrower than about 0.6 units, use the same bracket.
3. **[2:51–3:03][Clarity + Visual] Three precision figures on one bar, and the 3% tick sits inside the red 7% fill** (frame 2:57). Keep the police 7% on the main bar. Add a second thin grey bar under the raster titled "evaluators (Davies et al.)" with a dot at 3% on "three percent". On "new algorithm and better photos", animate that dot sliding to 46% (smooth, 1.5 s) with a counter. The motion then encodes the improvement, and the main bar stays one number.
4. **[0:20–0:27][Clarity] The screen says "44% said 95%" while the narration says "here ninety-nine percent".** Change the narration to: "Their most common answer was their test's own accuracy: ninety-five percent. For our test, that's ninety-nine." On "ninety-nine", TransformFromCopy the "95%" label into the "99%" that flies to the naive marker, with a small grey "their test: 95% accurate" under the waffle legend for the 4 s it is up.
5. **[1:47–2:01][Concision + Motion] The ÷10,000 sub-beat is 14 s, the formula is static from 1:47 to 1:59, and there is a 3.4 s fully static hold (1:53.3–1:56.7).**
   - Tighten the narration to: "Divide top and bottom by the ten thousand: twenty becomes point zero zero two, nine thousand nine hundred eighty becomes point nine nine eight. The share can't change." (about 7 s).
   - Run the table relabel and the TransformMatchingTex in the formula **simultaneously**, so each number changes in both places on its spoken word.
   - This saves about 6 s and removes the static stretch.
6. **[2:13.5–2:17.7][Motion + Audio sync] "Swap the disease for a police watch list" lands on a near-empty frame** (2:15: faded title, draining bar).
   - ReplacementTransform the 120-dot strip directly into the crowd grid while the meter retitles in place, so nothing goes empty.
   - On "watch list", fade in the red legend "■ on a watch list" (no count yet). The count "≤ 1,200" and the 71 red squares come on "twelve hundred faces" as now.
   - This fixes the one sync miss.
7. **[2:16–2:31][Visual] The crowd is a dim 100 × 100 texture of ~6 px squares, and the right half below the meter is empty for 15 s** (kf_26, kf_27).
   - Raise the crowd square brightness to full BLUE at 70% opacity, or use a 50 × 50 grid (1 square = 68 people) so squares are ≥ 0.1 units and survive compression.
   - Move the legend into the empty space under the meter on the right.
   - Add a grey "Cardiff · 3 June 2017" above the crowd on "Champions League final" so the spoken setting is on screen.
8. **[0:28–0:31][Motion] The cold-open diagram falls apart into unlabelled fragments before the table forms** (frame 0:29.0). Do it as one 1.5 s morph: each node+label pair transforms into its table row bullet+label, each arrow into its row arrow with its rate label riding along, and the + moves into the column header. Do not fade the labels out first.
9. **[3:03–3:41][Concision + Hook] The landing has three moves in 38 s.** Move the accuracy-paradox couplet ("The title's ninety-nine percent accuracy is real… more accurate, and useless") into the fail beat, right after "Six times too high" (1:12), where it explains the title at the moment of the surprise. The landing then becomes "Back to your test" + the prevalence sweep + the recall/precision chiasmus, about 25 s, and ends on the chiasmus.
10. **[0:39.7–0:44][Clarity, minor] "Of the five thousand who lit up" is spoken, but no 5,000 total is shown** (the table shows 4,950 and 50). On that phrase, write a grey "= 5,000 +" sum under the positives column. Mirror it at 1:02 with "= 120 +", so the denominator is always visible as a sum before it becomes the strip.

## REACHES 9 IF ALL FIXED: yes, but narrowly.
- Fixes 1–3 and 7 lift Visual to 9.
- Fixes 4 and 10 lift Clarity to 9.
- Fixes 5 and 9 lift Concision to 9.
- Fixes 6 and 8 lift Motion and the Audio sync to 9.
- With Hook and Originality at 8.5–9, that gives ≈ 8.9–9.0. Clearing the bar with margin depends on fix 1 (the fail beat is the emotional core and today its picture argues the wrong way) and fix 9 (a landing that ends on one line).
- No structural change is needed. The hook, build-fail-insight chain and real payoff are all in place.

## KEEP
1. The persistent "chance you're sick" meter, docked onto the 24 × 5 strip so its 17% red segment sits exactly over the 4 red columns. Do the same alignment again with the 2,470-cell raster at 7%.
2. The derivation built from the picture: braces → 20/(20+100), table → 20 × 0.99 and 9,980 × 0.01, then the named Bayes form with the yellow box on "shrink" and the red box on "take the share".
3. The landing sweep: one updater drives the label, flow widths and meter, "1 in 100 · 50%" holds while it is spoken, and the naive 99% marker comes back at 1 in 2. Keep the raster → + disk rhyme too.
