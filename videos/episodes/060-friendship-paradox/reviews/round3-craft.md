# Review, round 3 (craft critic: visual design, motion, A/V sync; all dimensions scored)

Evidence: the existing `review/` pack. metrics.json (19:53:56) is newer than final.mp4 (19:52:19), so I reused it. I read report.md, all 13 contact sheets, transcript.txt and transcript_words.tsv, narration_diff.txt, script.md, facts.md, CHANGELOG.md and the round-2 craft review. Full-resolution keyframes read: kf_05 (0:09.9), kf_12 (0:56.5), kf_15 (1:30.7), kf_19 (1:42.9), kf_25 (2:22.7), kf_29 (2:43.4), kf_33 (3:10.3) and kf_39 (3:35.3). Extra frames I pulled with ffmpeg: 1:45.0, 2:07.5, 2:28.0, 2:52.0, 3:13.0 and 3:20.0. I also made these crops:
- the Σk² row at 1:30.7 (3×);
- the square-label row at 1:44.0, 1:44.5, 1:45.5 and 1:46.0;
- the Facebook legend at 2:52.0 (3×);
- the network pulses at 1:02.3, 1:03.6 and 1:04.8;
- the cross-term row at 1:59.8, 2:00.4 and 2:01.0.

I re-verified the two external sources myself:
- arXiv:1111.4503, by direct quote: "around 190 Facebook friends" and "⟨k²⟩/⟨k⟩ = 635".
- PLoS ONE 10.1371/journal.pone.0012948, by direct quote: "13.9 days (95% C.I. 9.9–16.6)", N = 319 and N = 425.

```
EPISODE: 060 — "Why Your Friends Have More Friends Than You"
IDEA: Following a friendship lands on each girl once per friend she has, so the average friend has Σk²/Σk = μ + σ²/μ friends (the cross terms vanish because distances from the balance point sum to zero), which beats the average person whenever counts vary, and the friends of random students caught a real flu outbreak early.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 8.5
WEIGHTED: 8.4 (842.5/100)   AFTER CEILING: 8.4 (lowest 8 + 2 = 10, does not bind)
CAPS: none. Round 2's Sue label/token overlap is fixed (kf_12: Sue's label bottom ≈375 px, nearest token top ≈397 px). The legend's label-to-bar gap at 2:52 is 7 px, which breaks the §5 0.15-unit spacing standard, but nothing overlaps or is clipped, so it is a Visual deduction, not cap 7.
FINAL: 8.4   PASS: no
FACTS:
- 8 girls, 10 reciprocated friendships, Coleman's Marketville (Illinois) data | Verified | Feld 1991 AJS 96(6) Fig. 1/Table 1 as quoted in facts.md; Coleman 1961
- counts 1,4,4,2,3,3,2,1 → μ = 20/8 = 2.5; Σk² = 60; 60/20 = 3.0 | Verified | recomputed
- ring: 16 tokens, 32/16 = 2.0, σ² = 0 → "no spread, no gap" | Verified | recomputed
- "half a friend too low", "20% more than girls" | Verified | 0.5; 3.0/2.5 = 1.20
- "Sue holds four tokens, each worth four, 16" | Verified | 4×4
- ÷8: 7.5 / 2.5; squares 2.25 (×4) and 0.25 (×4), sum 10, σ² = 10/8 = 1.25 | Verified | recomputed (population variance)
- 4² = (2.5+1.5)² = 2.5² + 1.5² + 2·2.5·1.5 = 6.25 + 2.25 + 7.5 = 16 | Verified | recomputed
- signed distances sum to 0 → avg(k²) = μ² + σ² = 6.25 + 1.25 = 7.5 | Verified | algebra
- μ + σ²/μ = 2.5 + 0.5 = 3.0 | Verified | recomputed
- Facebook 2011 average user ≈190 friends | Verified | arXiv:1111.4503 ("around 190 Facebook friends")
- tokens average ≈635 (⟨k²⟩/⟨k⟩) | Verified | arXiv:1111.4503 ("⟨k²⟩/⟨k⟩ = 635")
- 190 + 445 = 635; spread term > twice the mean | Verified | 635 − 190 = 445 > 380
- Harvard 2009; 319 random students, 425 named friends | Verified | PLoS ONE e12948 Methods
- fitted lead 13.9 days (diagnosed flu) | Verified | PLoS ONE e12948 Abstract
- self-reported lead ≈3 (screen 3.2 days) | Verified | C&F 2010 Results (facts.md quote; verified in round 2 against PMC2939797)
- friends' averages 4, 3.5, 3.33, 3.33, 2 (Betty, Jane, Pam, Dale, Tina); Sue 2.75, Alice 3; 5 below, 2 above, Carol equal | Verified | recomputed from the edge list
- "land on a Sue four times as often as on a Betty" | Verified | 4/20 vs 1/20
MECHANICS: runtime 3:37.2 · 159 wpm (speech time; 164 wpm inside the 1:37–2:26 algebra) · max silence 2.08 s (planned holds 0:10.6, 2:35.9) · max static 3.43 s (0:58.4) · −14.0 LUFS / −2.1 dBTP · lead 0.00 s / trail 1.75 s · WER 0.9 % · 0 banned phrases
FIXES (highest impact first):
1. [1:49–2:26][Visual] The insight frame accumulates nine groups (kf_25 @ 2:22.7): dimmed token stacks plus "4×4=16", the beam, the fulcra, the signed-distance line, 8 squares with 8 area labels, the "squares at ¼ scale" tag, the dimmed bar panel, σ², the identity row and the main row. No single focal point survives. Fix: on "Split Sue's four" (1:49.2), FadeOut the token stacks, the white box and "4×4=16" (run_time 0.6). They are not referenced again, because the 4 in "4² = (2.5 + 1.5)²" comes from Sue's node. Then shift the distance line, squares and area labels up by 1.2 units into the freed band, so the squares sit right under the beam they measure. That leaves more room on the right too: the identity row can sit 0.3 units lower, clear of σ².
2. [1:59–2:09][Clarity] "avg(d)" appears at 2:00.4 (crop) but d is never named on screen. The viewer has to infer that d is "her distance" from colour alone. Fix: when the PURPLE distance line draws (1:39), write `MathTex(r"d = k - \mu", font_size=36)` in PURPLE left of the line (next_to(line, LEFT, buff=0.25)). On "add to zero" (2:05.5), TransformFromCopy the four signed labels into "Σd = 0" under the purple 0 tick before avg(d) → 0. The general identity then has a visible referent, which completes the re-derivation (Clarity 9).
3. [2:47.5–2:55.5][Motion] The flu axes stand empty for about 8 s (frame 2:52.0, sheet 10 @ 2:49–2:55) while the narration states the hypothesis. Only a legend pulse moves. Fix: put the hypothesis on the axes. On "so friends should get sick first" (2:54), draw two GRAY dashed ghost S-curves, with the YELLOW-outlined one shifted left and a tiny "prediction" tag (Text 20, GRAY). Then fly the legend bars into the origin as now, and let the real steps draw over the ghosts. Alternatively, start the axes on "tested this at Harvard" (2:50) rather than at 2:47, so the empty frame shrinks to under 3 s.
4. [2:47–2:55][Visual] The legend label "average friend" ends 7 px from its bar outline (3× crop @ 2:52.0: text right edge x≈1415, outline x≈1422). §5 needs at least 20 px. The buff was set before the 60 % scale-down. Fix: after scaling the legend, re-place each label with `lab.next_to(bar, LEFT, buff=0.2)`, and right-align both labels to that x.
5. [1:05–1:20][Clarity/Sync] The names drop away when the girls slide onto the beam (sheet 4 @ 1:07). So "Sue holds four tokens" (1:17.6) boxes an anonymous "4" (kf_15), and the viewer cannot tell Sue from Alice. Fix: TransformMatchingShapes each name label into a 24-pt GRAY label under her beam node (just above the fulcrum row), or at least keep "Sue" under column 7 from 1:17 until 2:26. The split row "Split Sue's four" then points at a visible name.
6. [2:23–2:26][Sync/Motion] "The ring had no spread, so it had no gap" shows only a text row, "ring: 2 + 0/2 = 2" (sheet 9 @ 2:25). The ring itself never comes back. Fix: bring back a 0.35× thumbnail of the ring from 0:31 in the freed lower-left band, with its distance line collapsed to a single point at 2. On "no gap", Transform the friend bar briefly to 2.0, flush with the girl bar, then restore it to 3.0. The callback then lands on a picture, not on text.
7. [2:06.5–2:08.5][Motion] The white box keeps the width of "2μ·avg(d)" after its content becomes "2μ·0" (frame 2:07.5: box x 1563–1817 px, content x 1567–1690 px). That leaves a 130 px empty box. Fix: in the same animation, `Transform(box, SurroundingRectangle(new_term, buff=0.08))`.
8. [3:11–3:14][Visual/Sync] "self-reported: 3.2 days" sits beside a GRAY arrow that is still about 11 days long (frame 3:13.0: arrow 112 px; 3.2 days is 32 px at this scale) for about 2 s, until "shrank". Fix: write "self-reported:" first. Make the number a DecimalNumber tied to the arrow length with an updater, so it counts from 13.9 down to 3.2 as the arrow shrinks on "shrank".
9. [2:40–2:46][Sync] "A few users had thousands of friends" has no referent, because the axis stops at 800 (kf_29). Fix: on "thousands", slide a handful of small BLUE dots (radius 0.06) out along the axis past 800, then off-frame right toward a GRAY tag "→ 5,000 (cap)". Pulse the PURPLE segment on "spread term". This shows why σ²/μ is big.
10. [1:39–2:26][Visual] The "squares at ¼ scale" tag is smaller than the citation (kf_19: cap height about 22 px, and the ¼ digits about 13 px, below the 24 px minimum). Fix: use `Text("squares at 1/4 scale", font_size=20)`, or MathTex `\tfrac{1}{4}` at font_size ≥ 30.
11. [1:37–2:26][Audio/Clarity] The densest beat runs at 164 wpm (134 words in 49 s), with 0.26 s sentence gaps between new equations. Fix: add 0.6 s holds after "sigma squared" (1:48.6), "and a cross term" (2:00.0) and "cross terms cancel" (2:09.3). Each new row then holds ≥ 2 s + 0.4 s per term before the next change, per §5. That adds about 2 s, still well inside 4:00.
REACHES 9 IF ALL FIXED: yes, narrowly. Fixes 1, 4, 7 and 10 lift Visual to 9: one focal point per frame and clean spacing. Fixes 2, 5 and 11 make the derivation re-derivable after one watch (Clarity 9). Fixes 3, 6, 8 and 9 put a moving picture under every remaining spoken claim (Motion and Audio 9). The structure is already right, so no structural change is needed. It has a number-commit hook, an easy case where the guess works, a measured failure (+0.5, 20 %), a beam that becomes μ + σ²/μ, two cited payoffs with an honest limit, and a landing that re-sees the cold-open network.
KEEP: (1) the token-weighted balance beam with two exactly placed fulcra (2.5 BLUE, 3 YELLOW); it is the episode's memorable image. (2) The friend bar as a YELLOW outline filled BLUE to μ and PURPLE beyond, carried unchanged to Facebook (190 + 445 = 635). (3) The closing tally "Sue ■■■■ 4× / Betty ■ 1×" with "Betty looks at her one friend and sees four".
```

## Notes by dimension

**Hook (8.5).** The real network is on screen from frame 0 at 70 %, with the Feld citation (sheet 1 @ 0:01). The question "How many friends does the average friend have?" ends at 0:10.8. The "?" stops at three candidate drop lines (2.5, 3, 4; kf_05), and a 2.1 s hold follows. Asking for the size, not the direction, fixes round 2's title-spoils-it problem. The stakes come at 0:12.7, with a "random" ring on Jane and a "named friend" arrow to Alice (sheet 2 @ 0:21). The ending re-sees the opening network with the answer bar filled. Below 9: the ring easy case (0:27–0:42) demonstrates the method without raising tension.

**Clarity (8.5).** The round-2 gap is closed: Sue's 4 is split into 2.5 + 1.5, the cross term is boxed, the distances get signs, and avg(d) → 0 is shown (sheets 7–8). Every number checks out. What still costs a rewatch:
- d is undefined on screen (fix 2).
- The beam nodes are anonymous, so "Sue" cannot be located (fix 5).
- The six-step algebra runs at 164 wpm.

**Visual (8).** The palette is strictly semantic all the way through: BLUE for counted once, YELLOW for reached by friendship, PURPLE for spread. Citations sit bottom-left above y = −3.2, and the closing frame has a clear focal point (kf_39). The C&F chart is clean, and its read-out arrows are drawn at chart scale (frame 3:13.0). Deductions:
- the overloaded insight frame (kf_25);
- the 7 px legend gap (2:52);
- the undersized ¼ tag;
- the oversized cancel box (2:07.5).

The Σk² ÷ 8 row at 1:30.7 sits about 5 px below "friends (count)" (3× crop). It is legal, because the axis is about to dim, but it is tight.

**Motion (8.5).** Almost every move encodes a relation:
- the counts fly into the μ bar (0:07);
- the tokens travel their edges and read degrees (0:47);
- the bar overshoots the dashed guess;
- the girls sort onto a beam, and the tokens stack into columns;
- the distance segments shrink into squares;
- the specific split becomes the general identity with shared operators held in place (crop @ 2:00.4);
- the Facebook bars fly into the curve origins;
- the 13.9-day arrow is copied into the read-out and the 3.2-day copy shrinks.

The doubled area labels at 1:45.0 are copies leaving for σ² (clean at 1:44.5 and 1:45.5), so I did not penalize them. Deductions: an 8 s empty chart (2:47.5–2:55.5), a ring callback that is text only, and a box that does not resize.

**Audio (8.5).** −14.0 LUFS, −2.1 dBTP, 159 wpm, WER 0.9 %. The planned holds are at 0:10.6 and 2:35.9. The deictics land within ±2 s:
- "Four on Sue": Sue's tokens are enlarged at 1:02.3 (crop);
- "Sue holds four tokens": box at 1:19;
- "k squared on top": Σk² at 1:25;
- "seven and a half": 1:33;
- "sigma squared": 1:47;
- "cross term": box at 1:59;
- "left and right distances": signs at 2:05;
- "635": revealed after the hold.

Misses without a referent: "thousands of friends" (2:41) and "the ring" (2:24). Whisper's long unpunctuated runs (1:43–1:55, 2:35–2:50) hint at flat sentence boundaries, but the silence log shows real gaps there, so I did not deduct for them.

**Concision (8.5).** At 3:37 it carries one idea plus two payoffs. Nothing is repeated. "The guess was half a friend too low" and "Friends average 20% more than girls" give the same gap in two units, which is defensible. The ring beat (≈16 s) is the one slack stretch.

**Originality (8.5).** The token-weighted beam with a second fulcrum, the signed-distance proof that the cross terms cancel, the redrawn Harvard curves, and "you land on a Sue four times as often as on a Betty" are specific and memorable. No banned phrases or patterns. The topic and Feld's example are well trodden, which keeps it short of 9.
