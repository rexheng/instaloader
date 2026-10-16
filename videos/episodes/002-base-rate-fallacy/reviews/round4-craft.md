# Round 4 — craft review (visual design, motion, A/V sync; all dimensions scored)

Evidence: `review/` pack (metrics.json 22:36 is newer than final.mp4 22:35), all 13 contact sheets, 16 full-resolution
keyframes (kf_02, 03, 05, 06, 12, 14, 16, 22, 23, 25, 27, 28, 30 plus extracted frames at 0:25.8, 0:26.4, 0:43.6, 1:16.5,
1:22.0, 1:30.5, 1:32.0, 1:36.9, 1:37.3, 1:58.6, 1:59.6, 2:13.0, 2:24.0, 2:25.5, 2:26.2, 2:44.2, 2:46.0, 3:04.6, 3:05.4,
3:06.0, 3:06.6, 3:30.0), 10 fps tiles of 2:45.2–2:46.8 (alert flight), 3:05.4–3:06.8 (raster → "+" morph) and 4 fps
tiles of 3:24–3:28 (prevalence sweep), per-frame luma of the crowd region 3:05.9–3:06.4, transcript, narration.txt and script.md.

```
EPISODE: 002 — "When a 99% Accurate Test Says You're Sick"
IDEA: A positive result shrinks the sample space to the people who tested positive; when the condition is rare
      that crowd is mostly false alarms, so a 99%-sensitive test gives only ~17% (Bayes' theorem = precision).
SCORES: Hook 9 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 8.5
WEIGHTED: 8.6   AFTER CEILING: 8.6   (lowest 8.5 + 2 = 10.5, no effect)
CAPS: none
FINAL: 8.6   PASS: no
```

## FACTS

| Claim | Status | Source / check |
|---|---|---|
| 1 in 500, 99 % sensitivity, 1 % FPR → P(sick∣+) ≈ 17 % | Verified | 0.002·0.99 / (0.002·0.99 + 0.998·0.01) = 99/598 = 16.6 % |
| "six times too high" | Verified | 0.99 / 0.1656 = 5.98 |
| 10,000 people: 20 sick → ~20 +, 9,980 healthy → ~100 + (labelled "expected counts") | Verified | 19.8 and 99.8, shown unrounded at 1:34 |
| Half sick: 4,950 + 50 positives, 99 % of them sick | Verified | 4,950/5,000 = 0.99 |
| 20/(20+100) ≈ 17 %; 19.8/(19.8+99.8); ÷10,000 → 0.002, 0.998 | Verified | recomputed |
| Bayes' theorem as drawn at 2:04 (law of total probability in the denominator) | Verified | standard form |
| 50 % at 1 in 100; 99 % at 1 in 2; mid-sweep frames (1 in 101 → 50 %, 1 in 109 → 48 %, 1 in 43 → 70 %) | Verified | recomputed per frame |
| Accuracy 99 %; "calls everyone healthy" 99.8 % | Verified | 9,900/10,000; 9,980/10,000 |
| Recall = 99 % = P(+∣sick); precision = 17 % = P(sick∣+) | Verified | definitions |
| Most doctors got it wrong; gynecologists 21 % → 87 % after natural-frequency training | Verified | Gigerenzer et al. 2007, PSPI 8(2) p. 55, Fig. 2 (160 gynecologists); cited on screen |
| ~170,000 people in Cardiff, 2,470 alerts, 2,297 wrong → 173 right = 7 % | Verified | BBC News 4 May 2018 (South Wales Police data); cited on screen |
| Watch lists ~1,200 images | Verified | Davies, Innes & Dawson 2018, p. 10 (per facts.md); cited on screen |
| 46 % judged right at Six Nations after new algorithm | Verified | Davies et al. 2018 exec summary: "3 % … to 46 %" (re-checked via cardiff.ac.uk PDF excerpt) |
| "new algorithm and better photos cut the false alarms" | Verified with nuance | Davies credits the M20 algorithm and operator familiarity; high-standard custody images only after the final. The 7 % (police count) and 46 % (evaluators' logbooks) are different measures; the like-for-like change is 3 % → 46 %. Not wrong, but the meter invites a 7 → 46 comparison (fix 6). |

No fabricated or wrong claim found.

## MECHANICS

runtime 3:49.8 · 153 wpm (speech time; 562 words) · max silence 2.08 s (planned "Pick a number" hold, 0:13.4–0:15.5) ·
max static 3.33 s (2:15.9–2:19.2) · −14.0 LUFS / −1.7 dBTP · leading 0.00 s / trailing 1.73 s · 0 black frames ·
WER 2.0 % (only "a"→"one", "where"→"were" homophones) · 0 banned phrases · layout audit 0 issues.
No mechanical cap triggers. Runtime sits 10 s under the 4:00 ceiling.

## What round 3's fixes changed (verified in frames)

- Beat transitions are now staged: 0:25.8 → 0:26.4 (labels leave before nodes travel), 1:16.5 → 1:22 (header swaps to
  "120 people who tested +" as the negatives vanish, strip forms before the meter moves), 2:24.0 (meter empties in place
  with title dimmed, nothing else on screen), 3:05.4 (7 % fill retracts under a fading title).
- Formula swaps are clean: 1:36.9 / 1:37.3 show old glyph leaving and new arriving with no hole and no double-strike;
  0.002 / 0.998 pulse on "these two" (1:59.6).
- The return sweep agrees with its label on every frame I sampled (3:24–3:28 at 4 fps: "1 in 100 · 50 %" held
  ~0.5 s under "fifty percent"; "1 in 2 · 99 %" lands on the naive marker as "one in two" is spoken).
- Cardiff crowd now carries its base rate: 71 red squares appear on "twelve hundred faces" (2:35), legend reads
  "■ watch-listed: ≤ 1,200" / "■ = 17 people · illustration"; flagged squares fly into the 26 × 95 raster with the
  red block first (2:45–2:47) and the meter's 7 % red segment sits exactly over the raster's red columns (kf 2:55.7).
- Sync: every deictic I checked lands within ±1 s ("these hundred and twenty people" 1:25 outline closes; "the red share"
  1:29 brace "20"; "1,200 faces" 2:35; "2,470 alerts" 2:47 label; "seven percent" meter 7 % ~2:52.5, ~1 s late;
  "precision" title swap 2:57; "46" marker 3:03; "accuracy … real" bar 3:09–3:11; "ninety-nine point eight" bar 3:13–3:15;
  "recall" tag 3:41; "precision" tag 3:45).

## Score rationale

- **Hook 9.** Frame 1 is the problem (nodes, "1 in 500", ghosted meter). The question lands at 0:09–0:12.6, "Pick a
  number" at 0:13 with a 2.1 s hold, and only then the 21 % gynecologist waffle (0:16). The ending re-reads frame 1 (99 % vs
  17 %, recall vs precision). The sag is the algebra stretch 1:34–2:11.
- **Clarity 8.5.** Concrete before abstract, every number checks, the formula is read off the strip/table. Held below 9 by:
  (a) the landing packs four ideas into 43 s (accuracy paradox 3:07–3:17, prevalence sweep 3:17–3:31, flow recap
  3:31–3:38, recall/precision 3:38–3:48), and "recall" is introduced in the last 10 s; (b) the meter at 3:03 puts the
  police's 7 % next to the evaluators' 46 % as if like-for-like.
- **Visual 8.5.** Strict palette (red/blue/yellow/green/grey hold their meaning from 0:01 to 3:49), one focal group per
  beat, strip-under-meter and raster-under-meter alignments are exact. Below 9 because:
  - 2:50–3:06: the dimmed 600 × 600 px crowd keeps the left third of the frame for ~16 s after its label leaves (2:50),
    unlabelled and carrying nothing (its red squares are invisible at that opacity, kf 2:55.7). The precision story is
    entirely in the right half; the left is a dark slab.
  - 2:25.0–2:26.2: the meter sits alone top-left for ~1 s, then slides to the top-right while the crowd fades in: a layout
    shuffle with no information.
  - 2:43–2:45 (f 2:44.2): the 10 flagged watch-listed squares are not distinguishable from the 135 flagged others while in
    the crowd (4–5 px squares, yellow rings over red); the "red share of the lit crowd" becomes visible only after landing.
- **Motion 8.5.** Most motion encodes a relation (99 % copy → naive marker, beam, survivors → strip, braces → fraction,
  table cells → formula terms, flagged squares → alert raster, live prior sweep). Below 9 because:
  - 3:05.6–3:06.1: the raster-with-outline is Transformed into the "+" badge; the in-between frames show a deformed glyph
    (a yellow lozenge with a mangled "+" that reads as a boat, f 3:06.0). It is the episode's most important
    callback ("Back to your test") and it passes through ~0.5 s of mush.
  - 3:06.2: the dimmed crowd vanishes in a single frame (crowd-region luma 45.4 → 35.0 between consecutive frames).
  - 2:45.2–2:45.8: the beam is still sweeping while the first flagged squares are already flying (10 fps tile), so two
    actions compete; the squares lose their yellow rings mid-flight and arrive as red/blue blocks that then get a yellow
    outline back at 2:47.
- **Audio 8.5.** On-target loudness and pace; deictics land. The one intentional 1.1 s pause (1:32.7–1:33.8) and the 2.1 s
  commit hold work. The topic switch "…then take the share. / As for those gynecologists" has only 0.5 s (2:11.7–2:12.1)
  between the episode's thesis line and a new beat; the thesis gets no air.
- **Concision 8.5.** Under 10 % removable. Slack: "On a random screen, twenty reach this plus along the red, a hundred along
  the blue" (3:31–3:38) re-states 0:51–1:00 and the flow widths already show it; "Swap the disease for a police watch list"
  is spoken over an empty meter (2:23–2:26).
- **Originality 8.5.** The hook is the canonical medical-test paradox (3b1b 2020, Veritasium 2017) with fresh numbers.
  What is this episode's own: the 120-dot strip hanging under the meter, the Cardiff crowd → 2,470-cell raster → precision
  bar, and "calls everyone healthy: 99.8 %, more accurate and useless", which turns the title's own word against it.
  The Cardiff image would be the shareable one if the red-under-yellow were legible in the crowd (fix 3).

## FIXES (highest impact first)

1. **[3:05.4–3:06.4][Motion] The callback morph passes through a mangled "+" and the crowd pops out.** Do not Transform the
   raster group into the badge. Instead: (a) FadeOut the dim crowd over 0.5 s *first* (`FadeOut(crowd, run_time=0.5)`),
   (b) shrink the raster + outline toward the badge position with `raster.animate.scale(0.05).move_to(badge_pos).set_opacity(0)`
   (1.0 s, `smooth`) while the outline alone `ReplacementTransform`s into the badge's yellow circle (both are closed
   curves, so the interpolation stays a rounded shape), and (c) `FadeIn(plus_glyph, scale=0.6)` only after the circle
   lands. No frame should show the "+" glyph mid-interpolation.
2. **[2:50–3:06][Visual] Dead crowd slab.** When the raster has landed (2:47.5), either FadeOut the crowd entirely with its
   label (the raster now carries the story), or scale it to 0.45× and park it bottom-left under the citations at 25 %
   opacity with "≈ 170,000 people" kept beside it. Then re-centre the meter + raster + braces group to x ≈ 0
   (`VGroup(meter, raster, braces).animate.move_to(ORIGIN + UP*0.8)`) so the precision picture is the frame's single focal
   point for 2:50–3:05.
3. **[2:42–2:46][Visual/Motion/Originality] Make the 10 flagged watch-listed squares visible before they fly, and separate
   beam from flight.** (a) Let the beam finish (2:44.9) and hold 0.5 s. (b) Give the 10 red flagged squares a 1.6× scale
   pulse in red (`Indicate(red_flagged, color=RED, scale_factor=1.6)`, 0.6 s) while the other 135 stay yellow-ringed, so
   "7 % of the lit crowd is red" is seen in the crowd. (c) Only then fly them, keeping the yellow rings on until they land
   inside the yellow outline. Bump each crowd square to ≥ 6 px (100 × 6 px pitch, 4 px square + 2 px gap) so a red square
   reads on a phone.
4. **[3:31–3:38][Concision/Clarity] Cut the flow recap.** Delete "On a random screen, twenty reach this plus along the red,
   a hundred along the blue." Instead, after the sweep returns to 1 in 500 (3:31), hold 1.0 s with the 20 / 100 flow labels
   fading in silently, then go straight to the recall/precision chiasmus. Saves ~5 s and leaves the landing with three
   moves (accuracy trap → prevalence → recall vs precision).
5. **[2:11.7–2:12.1][Audio] No air after the thesis line.** Insert `[pause 0.8]` after "…then take the share." and on that
   pause pulse the yellow outline of the strip once (the "shrunk" sample space), so the thesis gets a beat before the
   gynecologists return.
6. **[2:57–3:05][Clarity] 7 % and 46 % are different measures on one meter.** Change the line to "The force counted seven
   percent. The university's evaluators, counting the same way later, found three percent at this final and forty-six
   percent at the Six Nations, after a new algorithm and better photos." and add a second grey dashed marker at 3 %
   labelled "evaluators: 3 %" next to the 46 % one. Or keep the narration and relabel the marker "Six Nations 2018: 46%
   (evaluators' count)". Either way the comparison on screen becomes like-for-like.
7. **[2:23.1–2:26.2][Visual/Concision] Empty-meter shuffle.** Make the crowd FadeIn on "Swap the disease for a police watch
   list" (2:23.5) *at its final left position*, with the meter moving directly from its strip-top position to the top-right
   in one 1 s `smooth` move. Do not park it top-left first. The viewer then sees the new "population" on the words that
   introduce it.
8. **[3:38–3:48][Visual] Closing tags.** "recall" (beside the arrow's 99 %) and "precision" (under the meter) are ink at
   size 30 next to labels of the same weight; for the episode's last image, set both to size 34 and underline each with a
   0.6 s `Create(Underline(...))` on its spoken word so the chiasmus reads as the final frame's focal pair.

## REACHES 9 IF ALL FIXED: yes, narrowly

Fixes 1–3 and 7 lift Visual and Motion to 9; fixes 4 and 6 lift Clarity and Concision to 9; fix 5 lifts Audio to ~9;
fix 3 is the route to Originality 9 (otherwise 8.5). Projected with Originality 8.5:
15×9 + 25×9 + 15×9 + 15×9 + 10×9 + 10×9 + 10×8.5 = 895 → 9.0 (8.95 rounds up), no caps. With Originality 9 it is 9.0
with margin. No structural change is needed: misconception hook with commit, naive rule passing at 50 % and failing by a
measured 6×, one picture (strip under meter) that becomes Bayes' theorem, a cited real-world precision failure, and a
landing that re-reads frame 1. The remaining risk is that the episode is a craft-polish distance from 9, not a content
distance: every remaining defect is in transitions and composition of the Cardiff → landing hand-off (2:45–3:07).

## KEEP

1. The 120-dot strip hanging under the meter with its 4 red columns exactly under the 17 % segment, and the formula built
   from it: braces → 20/(20+100) → 19.8/99.8 → table cells → ÷10,000 → names (1:21–2:10).
2. The half-sick check where the rule holds (0:28–0:43), then the same beam at 1 in 500 failing by a measured "6× too
   high" (0:43–1:11).
3. The landing diagram with people-width flows and the live prevalence sweep onto the returning naive marker, plus the
   "calls everyone healthy: 99.8 %" accuracy bar (3:07–3:31).
