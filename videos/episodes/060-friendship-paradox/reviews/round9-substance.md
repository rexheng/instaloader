# Round 9 — science and story editor (fact-check, hook and tension, clarity, concision, slop; every dimension scored)

**Evidence used**
- The `review/` pack. Its metrics.json (21:38) is newer than final.mp4 (21:36), so I reused it.
- report.md, narration_diff.txt, all 12 contact sheets, and these keyframes at full resolution: kf_01, 05, 11, 13, 19, 23, 27, 30, 33, 35, 37, 39.
- Extra frames I extracted with ffmpeg into /tmp/r9sub060 at 0:44.8, 1:39.8, 2:21.6, 2:47.5, 3:05.6, 3:06.8 and 3:28.5.
- transcript.txt, transcript_words.tsv (0:00–0:15 and 2:28–2:45), narration.txt, script.md and facts.md. I read the round-8 substance review only to check which of its fixes were applied.
- Independent recomputation in Python from Feld's edge list:
  - Degrees: Betty 1, Sue 4, Alice 4, Dale 3, Pam 3, Jane 2, Carol 2, Tina 1.
  - Σk = 20, Σk² = 60, μ = 2.5, σ² = 1.25 (population), Σk²/Σk = 3.0 = μ + σ²/μ.
  - Token layers: 20/8, 38/14 = 2.71, 52/18 = 2.89, 60/20 = 3.0.
  - Friends' means per girl: Betty 4, Sue 2.75, Alice 3, Dale 3.33, Pam 3.33, Jane 3.5, Carol 2, Tina 2. That gives 5 below, 2 above and 1 equal.
  - The C&F schematic's "random students" are Betty, Jane, Pam and Tina. Their counts are 1, 2, 3, 1, mean 1.75. Their tokens read 4, 4, 3, 4, 4, 2, 2, mean 3.29.
  - Facebook: 2 × 68.7e9 / 721e6 = 190.6, and 635 − 190.6 = 444.4. That is 2.34× the mean.
- Citations re-checked online today:
  - Feld 1991, *AJS* 96(6):1464–77 (UVM PDF). Verified: the eight "Marketville" girls; "a total of 20 friends ... mean of 2.5"; 5 below, 2 above, 1 equal.
  - Ugander, Karrer, Backstrom & Marlow, arXiv:1111.4503 (ar5iv text). Verified: "around 190 Facebook friends", "⟨k²⟩/⟨k⟩ = 635", "92.7% of users have less friends than the average friend count of their friends", and the "cutoff at 5000".
  - Christakis & Fowler, *PLoS ONE* 5(9):e12948, 15 Sep 2010 (journals.plos.org). Verified: Harvard College, late 2009; random N = 319 of 6,650 undergraduates; friends N = 425; "13.9 days (95% C.I. 9.9–16.6)" from clinical diagnoses; "a significant but smaller shift in self-reported flu symptoms (3.2 days, 95% C.I. 2.2–4.3)"; the friend group had higher in-degree and betweenness.
- Round-8 fixes confirmed applied:
  - "sides at 1/4 scale" is now inline (kf_19).
  - The C&F hand-off is clean, with no ring or token overlap at 3:05.6 or 3:06.8.
  - Payoff breaths are added: 3:12.0–3:12.6 and 3:14.4–3:14.9.
  - "Take Sue, and split her four" is transcribed cleanly.
  - The "guess" label stays hidden while the box regrows (0:44.8).
  - The YELLOW candidates shrink out at 0:21 instead of browning.

```
EPISODE: 060 — "Why Your Friends Have More Friends Than You"
IDEA: Following a friendship lands on each person once per friend she has, so the friend average is avg(k²)/μ = μ + σ²/μ (the cross term vanishes because distances from the balance point sum to zero), which exceeds the person average whenever counts vary, and that is why the friends students name are an early-warning sample for flu.
SCORES: Hook 9 · Clarity 9 · Visual 9 · Motion 8.5 · Audio 8.5 · Concision 9 · Originality 9
WEIGHTED: 8.9 (135 + 225 + 135 + 127.5 + 85 + 90 + 90 = 887.5 / 100 = 8.875)   AFTER CEILING: 8.9 (lowest 8.5 + 2 = 10.5, does not bind)
CAPS: none. 0 banned phrases or patterns. Every empirical claim has an on-screen citation (Feld/Coleman, Ugander, C&F). No wrong or fabricated claim. All mechanics are in range. Layout audit 0/214, and no overlap in any frame I read.
FINAL: 8.9   PASS: no
FACTS:
- Eight girls at an Illinois high school, every friendship among them | Verified | Feld 1991 Fig. 1 ("Marketville"; Coleman 1961, northern Illinois)
- Counts 1,4,4,2,3,3,2,1; "two and a half friends" | Verified | recomputed; Feld Table 1
- Ring "everyone has 2": 16 tokens, 32/16 = 2.0, labelled hypothetical | Verified | computed
- Real class: tokens read 1–4, 60/20 = 3.0; "+0.5 · 20%"; "fell short by half a friend" | Verified | Feld p. 1467; 0.5/2.5 = 20 %
- Partial counters 15/5 (0:47) and 58/19 (0:49) | Verified | consistent mid-flight partial sums
- "4 on Sue, 4 on Alice, 1 on Betty" | Verified | degrees
- Two girls at each count; girls balance at 2.5; tokens at 3; live fulcrum 2.7 / 2.9 / 3.0 | Verified | layer sums recomputed (2.8 at 1:09 is mid-slide)
- "Sue holds four tokens, each worth four: sixteen"; k² on top, k on bottom; (60÷8)/(20÷8) = 7.5/2.5 | Verified | algebra
- Distances 1.5/0.5; areas 2.25/0.25; σ² = 10/8 = 1.25 (population variance) | Verified | computed
- 4² = (2.5+1.5)² = 2.5² + 1.5² + 2·2.5·1.5 (6.25 + 2.25 + 7.5 = 16) | Verified | algebra
- avg(k²) = μ² + σ² + 2μ·avg(d), with avg(d) = 0 because the beam balances | Verified | Σ(k−μ) = 0 by the definition of μ; a complete proof
- (μ²+σ²)/μ → μ²/μ + σ²/μ → μ + σ²/μ = 2.5 + 0.5 = 3.0; ring 2 + 0/2 = 2 | Verified | computed
- Facebook 2011: users averaged about 190 friends; a few had thousands; 5,000 limit | Verified | Ugander et al. 2011
- Tokens average about 635 | Verified | Ugander: ⟨k²⟩/⟨k⟩ = 635, exactly the episode's token average
- 190 + 445 = 635; "spread term more than twice the mean" | Verified | 444.4 ≈ 445 > 380
- "93% of users had fewer friends than their friends averaged" (92.7 % on screen) | Verified | Ugander, per-user comparison, correctly kept distinct from the 635 token average
- Christakis & Fowler at Harvard; random students vs the friends they named; 319 / 425 | Verified | C&F 2010 Methods
- "Named friends have more friends, so they sit closer to everyone else and should catch flu first" | Verified as C&F's stated rationale | C&F abstract; Fig. 3 caption (higher in-degree and betweenness)
- Raw steps = C&F Fig. 3 redrawn; dashed curves are a disclosed logistic refit with the shift held at 13.9 d | Verified as disclosed | on screen "Fig. 3 redrawn, logistic refit"
- "Fitted curves put them 13.9 days ahead" | Verified | C&F abstract (clinical diagnoses, NLS)
- "With self-reported symptoms, the lead shrank to about three" (3.2 d on screen) | Verified | C&F Results
- "Betty looks at her one friend, Sue, and sees four. Most of us are Betty." | Verified as a fair per-person reading | Feld (5 of 8 below their friends' mean); Ugander 92.7 %
MECHANICS: runtime 3:33.3 · wpm 156 (speech; 141 overall; median sentence 172) · max silence 2.22 s (planned "Pick one" hold, 0:12.1–0:14.3; also 2:40.4 and 3:27.9) · max static 2.67 s · −14.0 LUFS / −2.1 dBTP · lead 0.00 s / trail 1.70 s · WER 0.6 %
FIXES (highest impact first):
1. [1:21.2–1:29.5][Motion] The divide chain changes the main row every ~2 s.
   - Sheet 5 shows four states: 1:21 Σk²/Σk = 60/20 = 3.0; 1:23 (Σk²÷8)/(Σk÷8) = (60÷8)/(20÷8); 1:25–1:27 the numerator becomes avg(k²) = 7.5; 1:29 the denominator becomes μ = 2.5.
   - That is ~2 s per state on a 7-term row. §5 asks for ≥ 2 s + 0.4 s × 7 ≈ 4.8 s before an equation changes. This is the one place where reading time is not respected, and it is the step that turns "tokens" into "average of k²".
   - Change: make it two states.
     - (a) On "Now divide top and bottom by the eight girls", TransformMatchingTex straight to the ÷8 row. Add [pause 0.8] after "eight girls" so it holds ≈ 3 s.
     - (b) On "the average of k squared, seven and a half, over the average count, two and a half", do both relabels in one TransformMatchingTex: numerator → avg(k²) = 7.5 flagged on "k squared", denominator → μ = 2.5 flagged on "average count".
   - The final row already holds 1:29–1:34, so this adds only 0.8 s (≈ 3:34.1 total). Lifts Motion to 9.
2. [0:00.0–0:10.7][Audio] The cold open is the episode's longest run without a breath of ≥ 0.35 s: 10.7 s (report.md).
   - The only gaps are 0.3 s at 0:04.4 and 0:07.8, so the central question ("How many friends does the average friend have?", 7.54 s) follows the 2.5 statistic with no beat. The rest of the episode is shaped (0.7–1.7 s after results); the hook is the one flat stretch.
   - Change in narration.txt: "…every friendship between them. [pause 0.5] On average, each girl has two and a half friends. [pause 0.8] How many friends does the average friend have? Pick one. [pause 2.0]".
   - Retime the count flight (0:05–0:09) and the candidate drop lines (0:09–0:11) by +0.5 s and +1.0 s. Runtime becomes ≈ 3:35, still inside budget if fix 3 is also taken (−1 word).
3. [1:34.0–1:36.5][Audio · Clarity] "Measure each girl's distance from the girls' balance point" reads as "girl's … girl's" when heard (Whisper heard "girl's" at 1:35.5), as if it were one girl's balance point.
   - Change: "Measure each girl's distance from the balance point, two and a half, and square it." Keep the cue that flashes the BLUE fulcrum and 2.5 on "two and a half".
   - With fix 2 this lifts Audio to 9.
4. [2:59–3:05][Clarity] The C&F schematic's BLUE "random students" (kf_35) are Betty, Jane, Pam and Tina.
   - Their counts are 1, 2, 3, 1, mean 1.75 against the class's 2.5. Part of the visible contrast with the named friends (tokens 4, 4, 3, 4, 4, 2, 2, mean 3.29) is that hand-picked low draw, but it is labelled "random students".
   - Change, either one:
     - (a) Add a GRAY text-grade tag "one possible draw" (Text 18) under "name their friends" from 2:59 to 3:05.
     - (b) Better: use the draw {Betty, Dale, Carol}. They are pairwise non-adjacent, with counts 1, 3, 2 (mean 2.0, nearer the class). Their six tokens read 4, 4, 4, 2, 3, 1, mean exactly 3.0, the episode's own number.
5. [2:19–2:27][Visual] The "sides at 1/4 scale" tag fades at ≈ 2:19, but the squares stay on screen through the ring callback (sheet 8 at 2:19 and 2:21; sheet 9 at 2:25 and 2:27). For about 8 s the squares carry no scale.
   - Change: keep the tag with the squares and dim it with them to 35 %. Alternatively, fade the squares together with the tag at 2:19.
6. [3:15–3:23][Visual, nit] The dashed logistic fits start at ≈ 0.7 % and 0.4 % on day 0 (kf_37), where the raw steps sit at 0.
   - Change: draw the fits from the first case (day ≈ 3) onward, or clip them at y ≥ 0.2 %, so no curve claims flu before the data.
REACHES 9 IF ALL FIXED: yes. Fix 1 lifts Motion to 9, and fixes 2 and 3 lift Audio to 9. With the other dimensions held at 9, the weighted score is 9.0. No structural change is needed. The episode has a committed prediction by 0:12, a case where the guess holds (the ring), and a measured +0.5 failure with its cause named. The token beam becomes the formula with a complete cross-term proof. Two correctly cited payoffs follow, with an honest limit (3.2 days), and the landing re-sees the cold-open frame and accounts for all three candidates.
KEEP: (1) The token-weighted beam. The YELLOW fulcrum slides 2.5 → 2.7 → 2.9 → 3.0 as each layer lands, then the signed distances slide into the 0 that kills the cross term (1:06–2:05). (2) The friend bar as a YELLOW outline filled BLUE to μ and PURPLE beyond, carried unchanged from 2.5 + 0.5 to 190 + 445 = 635. The "+0.5 ?" target sits top-right through the derivation. (3) The fact discipline. 635 is exactly the token definition. 92.7 % is worded as "below their own friends' average". The 13.9-day curve is disclosed as a refit, and the 3.2-day self-report is the stated limit.
```

## Notes by dimension (evidence)

**Hook 9.**
- Frame 0 (kf_01) already shows the network and "average friend ?".
- By 0:11 the three YELLOW candidates 2.5 / 3 / 4 hang from drop lines (kf_05). "Pick one" is followed by a 2.2 s hold, so the viewer commits by 0:12.
- The stakes line (0:14–0:20) is paid off at 2:56 with the same picture.
- The landing (3:24–3:31) returns to the 0:11 frame. Betty's token reads 4, which accounts for the 4 candidate. The 2.5 candidate rises into the girl bar, and the friend bar grows to the ringed 3 (kf_39).
- Residual, not docked: the series title ("…More Friends Than You") pre-refutes 2.5. "The natural guess is two and a half again" (0:20.7) therefore voices a belief the title has already broken. The live choice is really 3 vs 4.

**Clarity 9.**
- The order is concrete before abstract:
  - the guess is tested where it holds (ring, 0:27–0:42);
  - it then fails by a measured "+0.5 · 20%" (0:53, kf_11);
  - the cause ("piled up unevenly") is named before any symbol;
  - Σk²/Σk becomes a balance point;
  - the cross term is cancelled from the balance condition (2:01–2:07), not asserted.
- Every number recomputes, and all three sources say what the episode says (see FACTS).
- Not higher, for two reasons:
  - The 1:21–1:29 algebra moves faster than it can be read (fix 1).
  - The C&F "random" draw is unrepresentative (fix 4).
- The derivation (1:31–2:24) is dense but complete. A first-time viewer can follow it because every number has a picture: the distances sit on the ruler and the squares sit under them.

**Visual 9.**
- The semantic palette holds across every beat: BLUE = counted once, YELLOW = reached by a friendship, PURPLE = spread.
- Every settled frame has one focal point:
  - kf_13: beam with stacks;
  - kf_23: split row with boxed cancels;
  - kf_33: Facebook bars with the row built from their segments;
  - kf_37: C&F with tip-aligned read-outs.
- Type is above the floor everywhere I measured. The inline "1/4" now reads at label size (1:39.8).
- Remaining items are nits: the scale tag leaves before its squares (fix 5), and the fits start above 0 (fix 6).

**Motion 8.5.**
- Objects persist and transform throughout:
  - counts fly into the bar (0:07);
  - nodes ride into the ring (0:29) and onto the beam in nested arcs (1:01–1:03);
  - the fulcrum is live;
  - distance segments drop and become squares (1:39);
  - signed labels merge into 0 (2:05);
  - the collapse lands on the baseline (2:19–2:21);
  - 190 / 445 / 635 drop out of their bar segments (2:45–2:47);
  - the C&F hand-off is now two clean passes (3:05.6, 3:06.8).
- 0 glyph morphs; the longest static stretch is 2.67 s.
- Docked for the 2 s-per-state divide chain at 1:21–1:29 (fix 1), the one place where §5 reading time is not met.

**Audio 8.5.**
- On target:
  - −14.0 LUFS and −2.1 dBTP;
  - 156 wpm on speech time;
  - planned holds after "Pick one" (2.2 s), the Facebook question (2.2 s), "sigma squared" (1.7 s) and "sees four" (2.2 s);
  - both deictics land;
  - the round-8 payoff breaths and "Take Sue" are fixed.
- Docked for the flat, breathless cold open (fix 2) and the "girl's / girls'" homophone (fix 3).
- The held "one" in "Pick one" (0.55 s) reads as intended emphasis, and I did not dock it.

**Concision 9.**
- 497 words in 3:33. Every beat earns its place:
  - the ring is both the "works at first" case and the honest callback at 2:24–2:27;
  - the C&F token picture sets up why the named-friend curve should lead.
- The eight repeats of "two and a half" each read a number off the screen. No recap, no preamble.

**Originality 9.**
- The examples (Feld's eight girls, Facebook 635, the Harvard flu sensors) are the standard trio for this topic.
- The angle is not standard. Tokens sent along friendships become a weighted beam whose balance point visibly slides from 2.5 to 3, and the variance gap is the distance between two fulcrums. That is an image a viewer would remember and reuse.
- §4 sweep of transcript and narration: 0 banned phrases. No "it turns out", no question chains (the three questions at 0:08, 1:31 and 2:38 each stand alone), no fake reveals, no lesson-list ending.
