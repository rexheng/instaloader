# Episode 3, review round 6 (craft critic: visual design, motion, A/V sync)

Evidence: I used the existing `review/` pack, because metrics.json (18:06) is newer than final.mp4 (18:04). I read report.md, all 12 contact sheets, script.md, narration via transcript.txt / transcript_words.tsv, facts.md (claims table), and these keyframes at full resolution: kf_01, 03, 07, 09, 12, 14, 15, 17, 19, 20, 24, 25, 27, 28, 29, 30, 33, 36. I extracted extra frames with ffmpeg at 0:09.0, 0:41.0, 0:57.4, 1:21.0/1:21.4/1:21.8 (tick strip), 2:36.5, 2:37.3, 2:40.2, 2:50.5, 3:24.5 and 3:25.5, and measured the "109" label clearance by pixel scan on the 2:37.3 frame. I recomputed every number with Python.

```
EPISODE: 003 — "Which Map Is Random?"
IDEA: Pure chance leaves empty squares, which force hits to pile up elsewhere, so clusters are not evidence of aim; the honest test scores the whole count histogram against Poisson, and a pattern that is too even is the real fingerprint of a rule.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 8.5
WEIGHTED: 8.4 (842.5/100)   AFTER CEILING: 8.4 (lowest 8 + 2 = 10, does not bind)
CAPS: none. No factual error; every empirical claim carries an on-screen citation; mechanics all inside limits; no held-frame overlap that crosses another element's ink (the "109" label at 2:35.5–2:41 sits inside the chance bar with 11–12 px to its stroke: a clearance breach, scored under Visual, not cap 7; the 3:24.5 header collision is mid-cross-fade, scored under Motion; the 1:21.0 "400" blob is a mid-Write fill, gone by 1:21.4).
FINAL: 8.4   PASS: no
FACTS:
- 537 hits, 576 squares, Clarke 1946, J. Inst. Actuaries 72:481 | Verified | Clarke 1946; Shaw & Shaw 2019
- "...tended to be grouped in clusters." | Verified (Clarke's opening sentence) | Clarke 1946
- Precise aim would put factories at risk | Verified (paraphrase) | Shaw & Shaw 2019, Significance 16(5)
- λ = 537/576 ≈ 0.93 | Verified (0.9323) | recomputed
- (1 − 1/576)^537 ≈ 0.3933; × 576 ≈ 227 | Verified (0.39333; 226.6) | recomputed
- e^−λ ≈ 0.3937 | Verified (0.39365) | recomputed
- Map A: 222 empty, 39 with 3+, 131 with 2+, 354 non-empty, 537/354 ≈ 1.5 | Verified from counts 222/223/92/28/9/2 (sum 576, hits 537) | facts.md, sim.py
- Poisson bars 227, 211, 98.5, 30.6, 7.1, 1.6; "chance predicts 39" | Verified (226.7, 211.4, 98.5, 30.6, 7.14, 1.57; 3+ = 39.33) | recomputed
- χ²_A terms 0.10+0.64+0.43+0.22+0.49+0.12 = 2.0 | Verified (2.000) | recomputed
- p = 0.74 ("three out of four chance maps score worse") | Verified (χ²₄ tail 0.736; facts.md Monte Carlo 74.5 %) | recomputed
- Map B: 109 empty ("half"), 397 singles, misfit 272 (271.7) | Verified (counts 109/397/70 sum 576, hits 537; χ² 271.71) | recomputed
- B's rule: no two hits closer than 4/5 square | Verified (sequential rejection, d = 0.8) | facts.md, sim.py
- Clarke's table 229, 211, 93, 35, 7, 1; χ² = 1.17, p = 0.88 | Verified (χ² 1.169; χ²₄ tail 0.883) | Clarke 1946
- People expect chance to look too even | Verified | Falk & Konold 1997, Psych. Review 104(2):301–318
- Aimed at central London (Tower Bridge), fell short (mean impact Dulwich), lower density north | Verified per facts.md quotes | Evans & Delaney 2018, Applied Geography 99:44–53; Shaw & Shaw 2019
- 1.9 vs 3.7 hits/km² | Unverifiable by me (own count of Zenodo data; 537/144 = 3.73 checks), honestly credited on screen "our count · L. Shaw, 2025 · Zenodo"
- Clarke chose an area where λ held steady | Verified (Clarke: mean density "not subject to material variation") | Clarke 1946
MECHANICS: runtime 3:34.7 · wpm 157 (speech time; 151 overall) · max silence 1.76 s (planned hold, 0:08.0) · max static 2.6 s · −14.0 LUFS / −1.5 dBTP · leading 0.0 s / trailing 1.6 s · WER 2.5 % · 0 banned phrases
FIXES (highest impact first):
1. [3:24.0–3:25.2][Motion/Visual] During the landing cross-fade, map A's header "A  simulated  537 hits" is written into the same top-left spot while "real V-1 hits, 1944–45" is still fading (frame 3:24.5 reads "realA V-1 hits simulated"); the dim north box, Thames label, densities and four citation lines are also still on screen behind the square. This is the one frame of the episode that should be cleanest. → FadeOut the real-map title, "Thames", the north box, both density labels, "≈ Clarke's area / re-created" and all citation lines together (run_time 0.5) as the first step of "So look again", before the rectangle starts squaring; Write A's header only after the square has opened into A's frame.
2. [1:33.9–1:52.4][Clarity/Audio] The two-hit derivation is 15 s carrying 537, 536, 2, 576 and e^−λ. Whisper transcribed 1:37.2–1:52.4 as one unpunctuated run ("...since order doesn matter Each has a one in 576 chance and the rest miss E to the minus lambda again 536 is almost 537"), so the planned 0.5 s breath after "matter" does not read as a sentence boundary, and the final t of "doesn't" is swallowed. → In narration_text.py raise the pause after "since order doesn't matter." to [pause 0.8] and add [pause 0.8] after "e to the minus lambda again." (before "Five thirty-six is almost five thirty-seven"); hold each new factor (2!, (1/576)², e^−λ) at full strength for ≥ 1 s before the next is written. Re-run the review kit and confirm whisper splits that run into three sentences.
3. [2:37.0–2:41.0][Visual/Clarity] On "a tower of single hits", B's entire 397 bar flashes solid YELLOW (frame 2:37.3). Yellow in this chart has meant "gap" since 2:17 (the slivers χ² squares), and 3 s later the same bar is yellow again above 211 as its gap (2:40.2). The viewer cannot tell "look here" from "this is misfit". Its "397" label is also dim navy (frame 2:37.3), under the 4.5:1 floor for coloured labels. → Flag the tower with a 0.8 s INK stroke (white outline, no fill change) and write "397" at full-strength BLUE above it, so yellow means only gap inside the chart.
4. [2:35.5–2:41.0][Visual] B's "109" label is centred inside chance's purple 0-bar outline. Pixel scan at 2:37.3: text x 977–1045, stroke inner edges at 965 and 1057, so 11–12 px each side, under §5's 20 px (0.15 unit). → Set the label's MathTex font_size to 28 (above the 26 tick/label floor), keep it centred over the blue bar: about 52 px wide, which leaves ≥ 20 px to each stroke. Or drop the number, since "half the expected empty squares" is spoken and the yellow gap shows it.
5. [3:13.0–3:24.0][Visual] "north" sits about 500 px right of its white box, on the same baseline as "Thames" (kf_36: "Thames" x 825–990, "north" x 1095–1215), so it reads as "Thames north" and the box itself is unlabelled where the eye is. → Put "north" directly above the white box (next_to(box, UP, aligned_edge=LEFT, buff=0.15)). Put "1.9 hits/km²" immediately right of the box (buff 0.25, box's vertical centre), and "3.7 hits/km²" immediately right of the yellow rectangle in the same x column. Each density then touches its referent and the 2:1 comparison stays in one column.
6. [1:13.0–1:20.4][Visual] Map A carries three overlay systems at once: blue count shading, the yellow outline of 222 empty regions, and the 39 red 3+ outlines. The equation and "537 hits / 354 squares ≈ 1.5" sit beside it (kf_12 at 1:18.2), and the eye has no single focal point while the voice says "the other 354 share all the hits". → On "The other three hundred fifty-four", drop the yellow empty-region outline to 35 % opacity and fade the red 3+ outlines out (they return at 2:09 anyway). Bring in only the blue 2+ outlines on "double up", as now.
7. [0:40.3–0:43.1][Motion] On "I dropped every hit on map A at random", A's dots clear and re-rain, but the blue count shading and all 39 red outlines stay at full strength over empty cells (frame 0:41.0: counter at 162 hits, cells shaded for hits not yet there). Shading means count, so for 2 s the picture contradicts itself. → When the dots clear, dim the cell shading and red outlines to 25 %. Restore them over the last 0.5 s of the rain, or per cell as its hits land. The re-rain then visibly rebuilds the same 39 targets.
8. [3:24.0–3:34.0][Hook] The landing re-states the 0:40–0:50 reveal ("pure chance", "rule: spacing ≥ 4/5 square") and carries none of the measurement the episode built. → On "So look again", write each map's score under its frame, in its referent colour, in place of the yellow circles: A "misfit 2.0 · p = 0.74", B "misfit 272". The final frame then shows the opening seen through the new tool, which is the 9-anchor "ending re-sees the first frame".
9. [3:11.4–3:24.0][Audio] The longest stretch without a ≥ 0.35 s breath is 12.1 s (kit), across the whole limits beat ("…fall short, so farther north, hits were about half as dense. The test needs one lambda…"). → Add [pause 0.6] after "half as dense." so the limit and its consequence land as two thoughts, timed to the north-box density write.
10. [2:47.0–2:51.0][Visual] The aimed map's header ends at x ≈ 810 px, about 50 px past the aimed frame's right edge at 758 px (frame 2:50.5), while every A/B header right-aligns to its frame. → Right-align "537 hits" to the aimed frame (aligned_edge=RIGHT), reducing the gap after "simulated" if needed.
REACHES 9 IF ALL FIXED: yes, narrowly. The structure already meets the bar: commitment by 0:09 with "A or B?" held 1.8 s, a measured failure (39 false alarms vs 39.3 predicted), the formula derived from the one square, χ² built from gap slivers, a simulated null, a counterexample, Clarke's real table, an honest one-λ limit, and a landing on the opening frame. What keeps it at 8.4 is a set of craft defects, each small: a garbled frame in the landing (fix 1), a 15 s derivation that is heard as one run (fix 2), and four frames where colour or labels blur the focal point (fixes 3–6). Fixes 1–6 lift Visual to 9 and Clarity/Motion/Audio to about 9. Fix 8 lifts Hook. Without 1–3 the episode stays below 9.
KEEP:
- The cold-open A/B pair raining in with live counters, and the landing where Clarke's rectangle squares up into map A's frame as B slides back (3:24–3:34).
- The one-square derivation: 537 carried into the exponent, λ folded from 537/576, the 537-bomb block with the two yellow picks, and all the 2s turning to 3 and then k (0:55–2:02).
- The same histogram reused for A, B, the aimed map and Clarke's real table, with one colour code (blue observed, purple chance, red aim, yellow gap), and the count-by-count flight from cells into bars (2:07–2:12).
```

## Notes by dimension

**Hook (8.5).** Frame 1 is the two maps with hits raining in. "Which is chance?" lands at 0:07, and "A or B?" holds through a 1.8 s silence (0:08.0–0:09.7, frame 0:09.0). Most viewers will pick B, which is the misconception the episode needs. Stakes arrive by 0:22 with the Clarke quote and citation. "Backwards." at 0:38.7 is a real turn. Tension sags during 1:24–2:02, a 40 s derivation with no new stakes beyond the forward line "To judge London, chance must predict every bar" (1:20). The landing returns to the exact first frame, but it re-tells the 0:40 answer rather than re-seeing it (fix 8).

**Clarity (8.5).** Concrete first: one square, 1/576, then 537 misses, then 227 against 222, all before λ is named. That is textbook 3b1b order. Every number checks (see FACTS). The χ² is motivated ("so a miss on a short bar counts more", 2:20, with the 4-hit sliver, its 0.49 and chance's 7.1 flagged). The one-λ assumption is stated and shown. Deductions:
- The two-hit step is dense and heard as one run (fix 2).
- The p-value-by-simulation idea gets about 6 s (2:26–2:32): it is legible, but it is the second new statistical idea inside 20 s.
- "Aimed bombs would miss the other way" (2:45) needs the red bars to decode "the other way".

**Visual (8).** The semantic palette holds the whole way: blue observed, purple chance, red aim/flag, yellow focus/gap. Typography is consistent, citations sit above y = −3.2, and the null histogram now has a "maps" axis with ticks. More than two minor issues remain, which holds this at 8:
- Yellow fill used for focus and for gap on the same bar (fix 3).
- The "109" clearance (fix 4).
- "north" far from its box and next to "Thames" (fix 5).
- Triple overlays at 1:13–1:20 (fix 6).
- The aimed header overhang (fix 10).

**Motion (8.5).** Objects persist and transform with meaning almost everywhere:
- Hits re-rain to prove "random" (0:40).
- 537 is carried from the counter into the exponent (1:01).
- The 2s turn to 3 and then k in place (1:53–1:57).
- k-hit squares fly into bar k (2:09).
- Gap slivers lift into χ² terms and fly into the readout (2:19–2:25).
- A's score lands on the null as a marker (2:27).
- Clarke's rectangle becomes map A (3:24–3:27).

Longest static stretch is 2.6 s. Deductions: the landing collision (fix 1) and shading that contradicts the counter during the re-rain (fix 7).

**Audio (8.5).** Pace is 157 wpm on speech time, −14.0 LUFS, −1.5 dBTP, 0 sentences above 200 wpm. Planned holds land at 0:08, 1:06, 2:32 and 3:10. All 6 deictics start an animation within the window: "like this one" gets the red ring at 0:31–0:33, "this square" the pulse at 0:59, "these purple bars" the bars growing at 2:05–2:07. Deductions: the 1:37–1:52 run-on and the swallowed "doesn't" (fix 2), and a 12.1 s breathless run in the limits beat (fix 9).

**Concision (8.5).** 492 words in 3:34.7, every beat on the §6 template. The repeats ("one in five seventy-six chance", "five hundred seventy-six squares") are deliberate parallels, between the single-square and two-hit steps and between the simulation and Clarke's real map. One slack beat: "Both are simulated. The question isn't." (0:09.7–0:13.2) is 3.5 s of framing that the "simulated" tags already carry. I am not requiring the cut.

**Originality (8.5).** Clarke's V-1 data is a classic Poisson example. The angle is fresh, though: the eye-as-detector, the too-even map B as the real rule, the aimed counterexample on the same chart, and Evans & Delaney's fall-short bias turning the limit into geography. That last one would get shared.
