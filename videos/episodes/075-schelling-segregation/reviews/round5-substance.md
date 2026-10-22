EPISODE: 075 — "Mild Preferences, Extreme Segregation" (script title now "Mild Preferences, Segregated Towns")
REVIEWER: science and story editor (substance), round 1 of this review cycle. I am independent of the producer. Evidence is the review/ pack: metrics.json was written at 01:13, after final.mp4 at 01:12. I read all 13 contact sheets and 9 full-res keyframes (kf_01, 04, 10, 14, 18, 22, 26, 27, 31). I extracted 20 more frames at 1:30.6–1:32.6, 1:44.6–1:45.4, 2:33, 3:04.4–3:05.6, 3:15 and 3:41. I re-ran a copy of sim.py in a scratch directory, and its output matches sim_output.txt line for line. I checked both citations by web search, including the Schelling 1971 full text.

IDEA: In Schelling's model, households that need only a third of their neighbors to match still sort into a town where three quarters match, because each departure tips a neighbor who was content. So a segregated map, or its 76% statistic, cannot tell you what its people wanted.

SCORES: Hook 9 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8 · Originality 9
WEIGHTED: 8.6 (135 + 212.5 + 127.5 + 127.5 + 85 + 80 + 90 = 857.5 / 100)   AFTER CEILING: 8.6 (lowest 8 + 2 = 10, does not bind)
CAPS: none.
- Runtime is 3:50.4, inside 2:30–4:00.
- Pace is 154 wpm.
- Loudness is −14.0 LUFS, true peak −1.7 dBTP.
- Longest silence is 1.96 s (the planned hold at 0:09). Longest static stretch is 3.5 s.
- 0 banned phrases. No question chains: the 4 questions at 0:06, 0:28, 1:27, 2:41 and 3:19 each stand alone.
- Both empirical sources are cited on screen: Schelling at 2:55–3:08, Aaronson et al. at 3:29–3:40.
- No factual error.
- I considered the 3:05 label superimposition for the overlap cap (7) and did not apply it. It is a 0.4 s mid-transition cross-fade, not a resting layout. It is still a defect, and it is penalised under Motion.
FINAL: 8.6   PASS: no

FACTS (recomputed independently; sim re-run identical):
- "on average, three quarters of a household's neighbors match"; meter 76% | Verified | sim 0.7553.
- "fewer than a third … it moves"; "happy to be outnumbered two to one" | Verified | s/(s+d) ≥ 1/3 ⇔ d ≤ 2s. The boxed example (kf_04, 0:22) has 2 gold, 4 blue and 2 empty: 2/6 = 1/3, so the household is content. The empties are correctly marked "not counted".
- Random start: "half … match"; 50% | Verified | 0.4992.
- "238 are not, about one in six" | Verified | 238/1440 = 0.165, which is 1 in 6.05. The ladder bars sum to the same: 23+15+23+11+23+76+67 = 238.
- "Round one takes 200 moves … sixty-four percent" | Verified | 200 moves. The other 38 were content when their turn came, and 0 found no square to move to. Share 0.6441.
- "It reads 74, and 67 … content before round one. They never moved." | Verified | Only households unhappy at the start of a round move in it. The code (step()) confirms this.
- Chain: B 3/8 → 2/7 after A leaves; C 3/8 → 2/7 after round 2; D 3/8 → 2/7 after round 3 | Verified | verify_chain() rows. I recounted the tiles in kf_14 (1:36.7: 2 gold of 7, one empty) and kf_18 (1:46.6: 3 gold of 8). The comparisons hold: 0.375 > 0.333 > 0.286.
- "after round seven, nobody wants to move"; 76% | Verified | Unhappy counts by round run 74, 41, 16, 9, 2, 1, 0.
- "Thirty towns at each demand, from zero to sixty percent"; ¼ → 58%, ⅓ → 76 | Verified | Same start at ¼: 0.5787. 30-seed means: 0.584 at ¼ and 0.749 at ⅓. The "1/3 → 76%" label refers to the seed-3 town, so it is consistent.
- "these are the only shares up to sixty percent" (14 bars) | Verified | The distinct k/n ≤ 0.6 with n ≤ 8 are exactly the 14 bars. The full ladder sums to 1440.
- "Every household at three eighths is one lost match away" from 2/7 | Verified | arithmetic.
- At ¼: "only these two bars change sides … just ninety-five" | Verified | 238 − 76 − 67 = 95. The ¼ bar is content because the rule is ≥.
- "that chain never starts" | Verified | At ¼, no chain household (A, B, C or D) ever moves. A's 2/7 ≥ ¼ is shown.
- "In his 1971 paper, Thomas Schelling ran this model"; "Schelling, 1971 · Journal of Mathematical Sociology" | Verified | JMS 1(2):143–186, doi 10.1080/0022250X.1971.9989794 (tandfonline).
- "moved to the nearest square that suited them, on emptier boards" | Verified | The full text defines "nearest" for the move. Quote: "25% to 30% vacancies allows fair freedom of movement".
- "the jump came later, between about a third and a half"; band 35–50% | Verified | Quote: "a rapidly rising function of demands in the range from about 35% to 50%". Quote: "slight when the demand is for about one-third … striking when the demand is as high as one-half".
- "As Schelling argued … the map alone could not have told you" | Verified as a paraphrase | Abstract: "Inferences about individual motives can usually not be drawn from aggregate patterns." See Clarity (b) for a precision issue with "map".
- "one study finds that 1930s federal lending maps increased racial segregation for decades. It traces this to reduced credit in the areas marked in red"; "Aaronson, Hartley & Mazumder, 2021 · AEJ: Economic Policy" | Verified | AEJ: Policy 13(4):355–92, doi 10.1257/pol.20190414. Abstract: "increased racial segregation in later decades … through reduced credit access and subsequent disinvestment." The "one study" hedge is appropriate.
- Two towns "both seventy-six percent" | Verified | 0.7553 vs 0.7554. The rule town is labelled "simulated".

MECHANICS: runtime 3:50.4 · wpm 154 (speech), 147 overall · max silence 1.96 s · max static 3.5 s (3:24.9) · −14.0 LUFS / −1.7 dBTP · lead 0.0 s / trail 1.73 s · WER 0.4%.

WHAT WORKS AND WHAT DOESN'T (evidence)

Hook (9)
- Frame 1 is the finished town. "76% match" is on screen by 0:03, and the question "How much matching do these households demand?" ends at 0:09.2.
- A 2.0 s hold follows. Then "Just a third" (0:11.4) breaks the viewer's likely guess, which is something at or above one half.
- Stakes arrive at 0:22.6: "We read maps of real cities the same way".
- The landing (3:43–3:50) is the exact opening frame with "? demanded" restored, so the ending re-sees the first frame.
- One small sag: the sweep chart at 2:00–2:16 shows 8 demand levels, but only two are used until 2:53.

Clarity (8.5)
- The build–fail–explain chain is strong. "plan predicts 0" against a counter reading 74, with 67 that never moved (0:58–1:16), is a measured failure in the SMH sense. The domino uses real tiles and real moves, with fractions built from them.
- Deductions:
  - (a) 0:43–0:59, a "wait, why?" gap. The narration says "move each of them" (the 238), then "Round one takes two hundred moves". The 38 who were fixed before their turn are never accounted for. An attentive viewer stalls on the mismatch at exactly the moment the failure should land.
  - (b) 3:08–3:50, "the map alone could not have told you". The two maps are not visually identical. At 3:13 (sheet 11) the rule-made left town has smoother, larger single-colour blobs and fewer isolated tiles. The Schelling town on the right is visibly more fragmented. A viewer who guesses by texture can win the 3:19 test. That undercuts "map alone": what the test really shows is that the 76% statistic cannot distinguish the two towns. Either the line or the rule town needs tightening.
  - (c) 3:31–3:37. The zone lines of the toy rule town pulse on "increased" and on "credit". That visually equates the HOLC finding (credit withdrawal, then disinvestment) with "households placed into colour zones". facts.md (claim 19) explicitly says the toy is not a model of HOLC, but the picture says it is. This is the same conflation that was removed from the words in an earlier round.
  - (d) 1:44.8–1:45.2. On "Then the next one", C's "2/7 <" morphs into D's "3/8 ≥". A morph says "the same quantity changed", but this is a different household. See Motion.

Visual (8.5)
- The palette is disciplined and holds for the whole episode:
  - blue and gold are households;
  - RED appears only as rings and counts;
  - PURPLE is always the demand;
  - INK is always the outcome.
- Dimming is used instead of deletion (kf_10, kf_14). Charts carry quantity names and units (kf_22). The "simulated" tags are always present. The ladder (kf_26, kf_27) is now clean: baseline, caret, outline, counts above bars, and no collisions.
- Deductions:
  - The 3:04.9–3:05.2 superimposition of "our jump" and "Schelling's jump: 35–50%" on one row (frames 184.8 and 185.0: both legible at about 50% opacity, reading "Schelling'sour jump35–50%").
  - At 3:07 (kf_31), Schelling's 35–50% band is drawn over our own dots. A casual viewer may read our 82% and 87% dots as his results. The label mitigates this but does not remove it.

Motion (8.5)
- Excellent persistence:
  - tiles fly home on "Rewind" (0:33–0:36);
  - the board corner and the inset replay in step (1:17–1:51);
  - the town shrinks into its chart dot (2:01–2:04);
  - the x-axis becomes the ladder baseline (2:19);
  - the caret slides to ¼ and two bars flip (2:45–2:49).
- Deductions: two transitions show exactly what the CHANGELOG says was fixed.
  - 1:44.85–1:45.2: garbled, superimposed glyphs. The "2" sits inside a "3", the "7" over an "8", and a bold, distorted "<" becomes "≥" (frames 104.9 and 105.1). The swap() helper evidently does not prevent this on the "Then" transition, which uses `resolve_to("3","8",r"\geq")` inside the same play as `ReplacementTransform(ringC, ringD)`.
  - 3:04.9–3:05.2: the old and new jump labels are both visible. The custom rate_funcs on FadeOut and FadeIn are meant to keep them apart, but they do not.

Audio (8.5)
- Natural cadence at 154 wpm, with variable gaps. Deictics land:
  - "these two hundred and thirty-eight" as the rings and counter appear (0:43–0:47);
  - "this neighbor moved away" as A's tile leaves (1:25.6–1:27.6);
  - "these two bars" with the dashed ¼ outline (2:45).
- One flag: at 3:15.5 whisper heard "In the nobody minds", dropping "other". Kokoro places "other" at 195.62–196.07 s, but whisper's "nobody" starts at 195.72 s. That suggests "other" is swallowed or slurred. It is the hinge word of the two-town contrast, so it should be checked by ear.

Concision (8)
- At 3:50 the episode is 10 s from the cap and 50 s over the 3:00 template.
- Slack:
  - The sweep beat (2:00–2:16) introduces 30 towns × 8 demands, and the episode immediately abandons them for a 37 s share-ladder beat. The sweep only pays off at 2:53.
  - The ladder is a second "why" after the domino has already answered the opening question. It earns its place, because it explains ¼ versus ⅓, but the two together run 1:17–2:53, which is 96 s of explanation.
- Under 10% is removable, but at least one beat is slack.

Originality (9)
- "plan predicts 0 / it reads 74 / 67 never moved", the real-tile domino, and the two-towns identifiability test are memorable and non-generic.
- The topic itself is well trodden (Hart & Case, *Parable of the Polygons*, 2014). The identifiability test is what makes this episode distinct, and the 3:19 test makes that pay off.

FIXES (highest impact first):
1. [1:44.8–1:45.2][Motion/Clarity] On "Then the next one", C's formula point-morphs into D's (garbled "2"/"3", "7"/"8" and "<"/"≥"). In scene.py, in the `beat.wait_until("Then")` play, replace `*resolve_to("3","8",r"\geq")` with two sequential plays:
   - first `FadeOut(num, den, rel, run_time=0.25)` together with the ring move;
   - then set the new glyphs and `FadeIn(num, den, rel, run_time=0.3)`.
   Better still, slide the old formula 0.3 units left while fading it and slide D's in from the right, so the motion says "a different household". Dump that second at 30 fps and confirm that no frame shows two digit sets. Apply the same check to every `resolve_to` call (1:28, 1:32, 1:42, 1:48) and to A's ladder formula flip at 2:48.
2. [3:04.9–3:05.2][Motion/Visual] "our jump" and "Schelling's jump: 35–50%" are superimposed on one row. Split the play at scene.py:1287 into three plays:
   - `self.play(FadeOut(ours_br_lab), run_time=0.35)`;
   - then `self.play(ReplacementTransform(ours_br, his_br), run_time=0.6)`;
   - then `self.play(FadeIn(band_lab), run_time=0.35)`.
   Move the "later" cue offset to −0.6 so the label still lands on "later".
3. [3:08–3:50][Clarity] "the map alone could not have told you" is stronger than the test shows, because the rule town's texture (smooth blobs, 3:13) differs visibly from the Schelling town's. Do one of the following:
   - (a) Regenerate `zoned_town()` with a finer zone field (shorter smoothing length, or fill 92% of each colour by sampling Schelling-like cluster sizes) until a blind viewer cannot pick the Schelling town at better than chance. Check that by eye against the 3:13 frame.
   - (b) Change the landing to "the map's seventy-six percent could not have told you". Then also change the test line at 3:08 to "Two simulated towns, both seventy-six percent" plus "Which one wanted a third?", and accept that texture is a tell.
   (a) keeps the stronger and better line.
4. [3:31–3:37][Clarity] The zone-line pulses on "increased" and "credit" equate the toy placement rule with the HOLC finding. Remove both zone pulses. Instead, on "1930s federal lending maps", fade the rule town to 30% and keep only the citation plus the two "76% match" labels (they pulse on "decades"). Optionally add a GRAY note under the left town, "toy rule, not a model of 1930s maps" (Text 18, ≤ 7 words).
5. [0:57–1:03][Clarity] Close the 238 vs 200 gap with a short clause: "Round one takes two hundred moves (thirty-eight were fixed by a neighbor's move first), and the matching share jumps to sixty-four percent." Shorter alternative: "Round one takes two hundred moves; the rest were fixed before their turn." Show "200 moved" as a GRAY HUD row while it is spoken. This also seeds "their neighbors did".
6. [3:15.5][Audio] "In the other, nobody minds" transcribes as "In the nobody minds" ("other" at 195.62–196.07 s may be swallowed). Listen to the line. If "other" is weak, re-synthesize the beat with "In the other town, nobody minds their neighbors at all" or insert [pause 0.15] after "other", then re-run the review kit and confirm WER shows no deletion there.
7. [2:00–2:16][Concision] Cut "Thirty towns at each demand, from zero to sixty percent." (about 3.5 s) from narration. Let the chart's own GRAY note "each dot: one simulated town" carry it, and hold the dots on screen silently through the next sentence's start. This brings the runtime toward 3:46 and removes the slack sentence before the ladder.
8. [3:05–3:15][Visual] Schelling's band sits over our dots and reads as his data. While the band is shown, dim our dots to 30% (`ctx_fade` on the dot group). Or draw the band only on the x-axis (a 0.25-unit-tall PURPLE-gray strip between 35 and 50, just above the axis) instead of a full-height column.

REACHES 9 IF ALL FIXED: yes, narrowly. No structural change is needed: the misconception hook, the measured failure, the real-tile domino, the cited payoff with honest limits, and the exact-return landing are all present and factually clean.
- Fixes 1–2 take Motion to 9.
- Fixes 3–5 take Clarity to 9.
- Fixes 2 and 8 take Visual to 9.
- Fix 6 takes Audio to 9, if the word is confirmed or re-synthesized.
- Fix 7 takes Concision to 8.5.
- Result: 135 + 225 + 135 + 135 + 90 + 85 + 90 = 895, a weighted 9.0 (8.9 if Audio stays 8.5).
To clear 9 with margin, the episode needs to be shorter (aim for about 3:30). The cleanest place to save time is the sweep-plus-ladder span (2:00–2:53).

KEEP:
- The SMH failure beat: "plan predicts 0", the counter reading 74, then "67 of these were content before round one. They never moved. Their neighbors did." (0:58–1:16).
- The real-tile domino with fractions built from the inset (1:17–1:51), and the ⅓ → ¼ caret slide that flips exactly two bars (2:45–2:53).
- The two-towns identifiability test, with the landing returning to the exact opening frame (3:08–3:50).

NOTE FOR PUBLISH: curriculum.json still titles the episode "Mild Preferences, Extreme Segregation". The script retitled it "Segregated Towns", correctly: 76% against a 50% baseline, and Schelling himself called one-third results "slight". The published title should use the script's version.
