# Round 7 — science and story editor (fact-check, hook and tension, clarity, concision, slop; every dimension scored)

**Evidence used**
- The `review/` pack. Its metrics.json (18:00) is newer than final.mp4 (17:59), so I reused it.
- report.md, all 12 contact sheets, and these keyframes at full resolution: kf_01, 05, 10, 14, 18, 20, 24, 27, 31, 33, 35, 37, 39.
- Extra frames I extracted with ffmpeg into /tmp/r7sub060 at 1:01.5, 2:15.0, 2:49.5 and 3:01.2.
- transcript.txt, narration_diff.txt, narration.txt, script.md, facts.md and the round-6 CHANGELOG.
- Independent recomputation in Python from the edge list. Degrees are Betty 1, Sue 4, Alice 4, Jane 2, Pam 3, Dale 3, Carol 2, Tina 1, which gives Σk = 20, Σk² = 60, μ = 2.5, σ² = 1.25, Σk²/Σk = 3.0. The per-girl friends' means are 4, 2.75, 3, 3.5, 3.33, 3.33, 2, 2.
- Citations checked online:
  - PLoS ONE e12948 page: 13.9 d (CI 9.9–16.6), 3.2 d (CI 2.2–4.3), N = 319 / 425, Fig. 3 left panel = NPMLE cumulative incidence, whole-sample incidence 8 %, the in-degree/betweenness sentence, published 15 Sep 2010, 5(9).
  - ar5iv text of arXiv:1111.4503: authors Ugander, Karrer, Backstrom, Marlow; "around 190", "⟨k²⟩/⟨k⟩ = 635", "92.7% of users have less friends than the average friend count of their friends", "cutoff at 5000", "many hundreds or even thousands", 721 M users, 68.7 B edges.
  - Feld 1991, AJS 96(6):1464–1477, Marketville eight girls, 2.5 vs 3: bibliographic search plus secondary sources (UVM copy, Psychology Today). The fetch of the cs.umd PDF returned 503. The network itself reproduces Feld's Table 1 exactly in my recomputation.

```
EPISODE: 060 — "Why Your Friends Have More Friends Than You"
IDEA: A friendship lands on each girl once per friend she has, so the friend average is avg(k²)/μ = μ + σ²/μ (the cross term dies because distances from the balance point sum to zero), which exceeds the person average whenever counts vary — so named friends are an early-warning sample for flu.
SCORES: Hook 8.5 · Clarity 9 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 9 · Originality 9
WEIGHTED: 8.7 (872.5/100)   AFTER CEILING: 8.7 (lowest 8.5 + 2 = 10.5, does not bind)
CAPS: none (0 banned phrases/patterns in transcript; every empirical claim has an on-screen citation; no wrong or fabricated claim; all mechanics in range; layout audit 0/197)
FINAL: 8.7   PASS: no
FACTS:
- 8 girls in an Illinois high school, every friendship | Verified | Feld 1991 AJS 96(6):1464–77 ("Marketville", Coleman 1961; Coleman's 10 schools were in northern Illinois)
- Counts 1,4,4,2,3,3,2,1; mean 2.5 | Verified | recomputed; Feld Table 1
- Ring: 16 tokens, 32/16 = 2.0 (labelled hypothetical) | Verified | computed
- Real class: 20 tokens, 60/20 = 3.0; "+0.5 · 20%" | Verified | computed; Feld "mean of 3.0 friends per friend"
- Running counters 27/9, 58/19 (0:47, 0:49) are partial sums mid-flight | Verified | consistent with the token order
- "4 on Sue, 4 on Alice, 1 on Betty" | Verified | the degrees
- Two girls at each count; girls balance at 2.5; tokens at 3; live fulcrum 2.7 (38/14), 2.9 (52/18), 3.0 (60/20) | Verified | layer sums recomputed
- Sue 4×4 = 16; k² on top, k on the bottom; (60÷8)/(20÷8) = 7.5/2.5 | Verified | algebra
- Distances ±1.5, ±0.5; squares 2.25, 0.25; σ² = 10/8 = 1.25 (population) | Verified | computed
- 4² = (2.5+1.5)² = 2.5² + 1.5² + 2·2.5·1.5; avg(k²) = μ² + σ² + 2μ·avg(d), avg(d) = 0 by balance | Verified | re-derived; complete proof
- (μ²+σ²)/μ = μ + σ²/μ = 2.5 + 0.5 = 3.0; ring 2 + 0/2 = 2 | Verified | computed
- Facebook 2011, ~190 friends | Verified | Ugander et al. 2011 arXiv:1111.4503 (2×68.7e9/721e6 = 190.6)
- Tokens average ~635 | Verified | Ugander: "⟨k²⟩/⟨k⟩ = 635" (edge-end average — exactly the episode's token average)
- "a few had thousands"; 5,000 limit | Verified | Ugander
- "spread term more than twice the mean": 445 > 380 | Verified | computed (2.34×)
- "93% of users had fewer friends than their friends averaged" (92.7% on screen) | Verified | Ugander (per-user comparison with the mean of one's own friends' counts)
- Christakis & Fowler at Harvard; random students vs friends they named; 319 / 425 | Verified | C&F 2010 PLoS ONE 5(9):e12948
- "Named friends have more friends, so they sit closer to everyone else" | Verified as C&F's rationale | C&F: friends had higher in-degree and betweenness; Fig. 1 caption on shorter path lengths
- Raw steps = Fig. 3 left (NPMLE, diagnosed) redrawn; totals 32/425 = 7.5 %, 25/319 = 7.8 % | Verified as disclosed | C&F whole-sample incidence 8 %; cf_fig3_digitized.json
- "Fitted curves put them 13.9 days ahead"; dashed fits = shape refit with shift held at 13.9 (disclosed "logistic refit") | Verified | C&F abstract; sim.py
- "With self-reported symptoms, the lead shrank to about three" (3.2 d) | Verified | C&F Results
- "Betty looks at her one friend, Sue, and sees four" | Verified | Feld
MECHANICS: runtime 3:29.5 · wpm 155 (speech; 140 overall; median sentence 172) · max silence 2.22 s (planned "Pick one" hold, 0:12.1–0:14.3) · max static 3.70 s (2:06.7–2:10.4) · −14.0 LUFS / −2.1 dBTP · lead 0.00 s / trail 1.91 s · WER 3.6 % (number formatting and girls'/girl's only)
FIXES (highest impact first):
1. [1:30.8–2:17][Hook] The 46 s derivation has no visible target. The bar panel and its PURPLE "+0.5 · 20%" go to 0 at 1:31 (sheet 6) and come back only at 2:19, and no line states what the algebra is hunting for. This is the "slight sag midway" of the Hook-8 anchor. Change: prefix 1:30.8 with the single question "So where does the extra half come from?" (one question; the next sentence answers it). Keep a PURPLE "+0.5 ?" tag (Text 26) at full strength at the top right (x ≈ 5.4, y ≈ 3.2) from 1:31 to 2:17. On "exactly the extra half friend we measured" fly the row's 0.5 into it and drop the "?".
2. [3:20–3:29][Hook/Originality] The last line, "Two and a half counts the girls, three counts the tokens", restates the result the viewer saw at 2:16. It does not change how the opening looks, and it leaves the title's "you" behind with the eight girls. Betty's line is the reframe, so end on it and on the viewer. Change: "Betty looks at her one friend, Sue, and sees four. Most of us are Betty." Keep the visual resolution silent: the bar grows to the ringed 3 and the 2.5 candidate flashes BLUE. Accuracy: 5 of the 8 girls and 92.7 % of Facebook users sit below their friends' average, so "most of us" is defensible, and it calls back the 2:49 "includes you" without repeating it.
3. [3:00–3:03][Motion] The C&F hand-off empties the frame. At 3:01.2 (extracted) the only things on screen are "random", "named friend" and eight shrinking 20 %-opacity rings in the lower left, while the narration says "should catch flu first". So the girls → BLUE origin and pile → YELLOW origin correspondence cannot be seen. Change: draw the axes at 30 % from 2:59.5 behind the network. Then shrink the 8 nodes into the BLUE curve's origin dot and the 8 tokens into the YELLOW one in a single 1.2 s path_arc move, keeping each node's digit until it merges. No frame may contain less than the axes plus both labels.
4. [2:55–3:01][Clarity] The sampling design is drawn wrong. "random" rings only Jane (kf_35), yet all eight girls send a token and every node wears the thick BLUE ring. In C&F only the random sample names friends, and the friend group is whoever they named. Change: on "Named friends", ring 4 of the 8 girls BLUE as "random students", for example Betty, Jane, Dale and Tina. Only they send tokens: Betty→Sue, Jane→Alice, Dale→Sue, Tina→Carol, which gives 2 on Sue, 1 on Alice, 1 on Carol, reading 4, 4, 4, 2. Retag "one possible draw" as "random students name one friend each". The piles still sit on Sue and Alice, and the picture now matches "the friends the students named" at 3:05.
5. [1:31–2:17, 3:09–3:20][Visual] Dimmed YELLOW stops reading as the "reached by following a friendship" hue. In kf_18, kf_20 and kf_24 the 50 % 3.0 fulcrum and the parked avg(k²)/μ row read brown/khaki. In kf_37 the 60 % friends' raw steps are ochre beside the full-YELLOW label, so a seventh hue appears. Change: fade the YELLOW 3.0 fulcrum out completely from 1:31 and restore it at 2:17. Keep the parked row at 100 % but scale it 0.8 to the bottom edge. Draw the raw C&F steps in full YELLOW/BLUE at stroke_width 1.5 and the dashed fits at stroke_width 4, so weight, not opacity, sets the hierarchy.
6. [2:45–2:52][Clarity] The BLUE "92.7% / had fewer friends than / their friends' average" block sits directly above and right of the YELLOW 635 bar (f 2:49.5). That invites "92.7 % had fewer than 635". It is a different statistic: Ugander's per-user comparison with one's own friends' mean, not the edge average. Change: move the block beside the "average user" row only (left-aligned at x ≈ 1.2, y of the 190 bar) and reword the second line to "than their own friends' average" (Text 26). The narration already says this correctly.
7. [1:39.9–1:52][Audio] "Split Sue's count, four, into the balance point, two and a half, plus her distance, one and a half. Squaring gives two and a half squared…" is a 9.8 s transcript segment with five numbers. Each glyph flight (Sue's 4 at 1:45, her 1.5 at 1:47; sheet 6) lands while the next number is already being spoken. Median sentence pace is 172 wpm. Change: insert [pause 0.4] after "four" and after "two and a half", and cue each flight to start on its own word.
8. [2:14.5–2:16.5][Motion] At 2:15.0 (extracted) the collapse shows "= 2.5 +0.5  = 3.0" with the 2.5 riding about 20 px above the +0.5 and uneven gaps. Change: typeset the target "μ + σ²/μ = 2.5 + 0.5 = 3.0" first, ReplacementTransform the surviving numerator 2.5 onto the target's 2.5 glyph, fade the ² and the denominators in place, and use TransformMatchingTex for 1.25/2.5 → 0.5.
9. [3:13–3:20][Visual] The read-out "C&F fitted lead: 13.9 days ←" sits at the top right (x ≈ 1030–1790 px, y ≈ 100), about 500 px up and 600 px right of the in-chart arrow it measures (≈ 795–935 px, y 598; kf_37). Change: left-align the read-out block at the arrow's x (≈ −1.0 units) just above the chart title, so the copied arrow rises vertically, and keep the 3.2-day row tip-aligned under it.
10. [2:40–2:42][Motion] Copies of 190, 445 and 635 fly straight down through the tick labels. At 2:41.0 a fading "635" sits under the "635" label (sheet 9). Change: route them with path_arc −0.6 to the right of the 800 tick, and keep them at 0 opacity until they clear the bar's lower edge by 0.3.
REACHES 9 IF ALL FIXED: yes, narrowly. Fixes 1 and 2 lift Hook to 9: the derivation gets a visible target, and the ending re-sees the opening through Betty and the viewer. Fixes 3, 8 and 10 lift Motion to 9. Fixes 5, 6 and 9 lift Visual to 9. Fix 7 lifts Audio to 9. Fixes 4 and 6 secure Clarity at 9 or above. With every dimension at 9 or more, the weighted score is ≥ 9.0. No structural change is needed: misconception hook, test case where the guess holds, measured +0.5 failure, beam proof, two cited payoffs with an honest limit (3.2 days), and a return to the 0:11 frame are all present.
KEEP: (1) The token-weighted beam: the YELLOW fulcrum slides 2.5 → 2.7 → 2.9 → 3.0 as each layer lands, then the signed distances merge into the 0 that replaces avg(d), a complete, honest proof of avg(k²) = μ² + σ² (1:06–2:05). (2) The friend bar as a YELLOW outline filled BLUE to μ and PURPLE beyond, carried unchanged to Facebook 190 + 445 = 635 (kf_31). The spread cue comes before the "?", so the second prediction is a transfer test. (3) The fact discipline: the edge-end statistic 635 matches the token definition exactly, the 13.9-day fit is disclosed as a refit, and the self-reported 3.2 days stated as the method's limit.
```

## Notes by dimension (evidence)

**Hook 8.5.**
- What meets the 9 anchor:
  - Frame 0 (kf_01) already poses the question, with ghosted "average girl / average friend ?".
  - The YELLOW candidates 2.5 / 3 / 4 sit on the axis scale by 0:11 (kf_05), and "Pick one" is followed by a 2.2 s hold.
  - The stakes line is done by 0:20.7. The flu thread returns visibly at 2:55 (the stakes picture is reused).
- Reasons it stays below 9:
  - The title already says "more", which pre-refutes the 2.5 candidate. So the commitment is mostly 3 vs 4, not a likely-wrong belief. This is inherent to the title, so I do not dock it further.
  - The derivation sags from 1:31 to 2:17 with no target on screen (fix 1).
  - The last sentence restates rather than reframes (fix 2).

**Clarity 9.**
- Concrete before abstract throughout:
  - the guess is tested where it holds (ring, 0:27–0:42);
  - it then fails by a measured +0.5 · 20 % (0:53);
  - the cause ("piled up unevenly") is named before any symbol;
  - the beam makes Σk²/Σk a balance point;
  - the cross-term cancellation is derived from the balance condition, not asserted (1:55–2:05).
- "The girls' balance point, two and a half" now disambiguates the two fulcra, and the count ruler makes distances land on ticks 1–4 (kf_18).
- Every number recomputes.
- Two picture/wording mismatches stop it going higher: the all-eight-girls draw versus "the friends the students named" (fix 4), and the 92.7 % block placed against the 635 bar (fix 6). Neither is a factual error in the narration.

**Visual 8.5.** A semantic palette, clean hierarchy and safe area held. Deductions:
- the brown dimmed YELLOW (fix 5);
- the C&F read-out detached from its arrow (fix 9);
- the 92.7 % block placement (fix 6);
- the "sides at ¼ scale" tag at 40 % (kf_18). It is the only explanation of why 1.5-long distances make 0.375-wide squares; raise it to 70 %.

**Motion 8.5.**
- Objects persist and carry meaning: counts fly into the bar, tokens read where they land, the fulcrum slides, distances drop into squares, and signs merge into 0.
- Deductions:
  - the empty hand-off at 3:01.2 (fix 3);
  - the baseline jitter at 2:15.0 (fix 8);
  - the flights through tick labels at 2:41 (fix 10).

**Audio 8.5.**
- Loudness, peak and silences are on target, and the pauses are planned (0:12, 2:36, 2:22).
- Deictics land: "Sue holds four tokens" with the box at 1:13, "her distance" with d = k − μ at 1:49, "sees four" with Betty's token at 3:23.
- "Christakis" is transcribed correctly, so it is pronounced correctly.
- Docked for the number-dense run at 1:40–1:52 (fix 7) and an 11.5 s breathless stretch in the Facebook sentence from 2:24.9.

**Concision 9.**
- 494 words in 3:29.5.
- I tried to cut each sentence and every candidate loses something:
  - the ring sets up "no spread, no gap";
  - "every friend is one of these same eight girls" is the reason the guess feels right;
  - "Odds are that includes you" pays off the title.
- The nine "two and a half"s are anchors tied to visible 2.5s.

**Originality 9.**
- Feld's eight girls, Facebook 190/635 and C&F flu are the canonical trio.
- The balance-beam proof, where the token fulcrum moves and the beam's own balance kills the cross term, is a picture I have not seen elsewhere and would remember.
- Carrying the token machine into C&F's sampling is a fresh link.

**AI-slop sweep (BAR §4).**
- 0 banned phrases.
- No question chains: 0:08 and 2:32 are each a single question.
- No "it turns out", no colon fake-reveals and no "not just X" constructions.
- The ending is one line, not a list, though it restates (fix 2).
- The voice is specific and noun-driven ("Sue holds four tokens, each worth four").
