# Episode 60 — craft review, round 1 (visual design / motion / A-V sync emphasis)

Evidence: `review/` pack (metrics.json 00:53 is newer than final.mp4 00:51, so reused). Read report.md, all 13 contact sheets,
keyframes kf_03, 05, 09, 11, 16, 19, 24, 25, 38 at full resolution, plus extra frames extracted at 0:13.0, 0:20.5, 2:29.0, 2:46.0,
3:19.0, 3:24.0, 1:16.0–1:18.6 (fulcrum) and 3:09.0–3:10.6 (flash). Read script.md, narration.txt, facts.md, transcript and word timings.
The "Thank you" at 3:40.8 in the transcript is a Whisper hallucination: volumedetect on 3:40.0–3:41.4 gives a mean of −91 dB (silence).

```
EPISODE: 060 — "Why Your Friends Have More Friends Than You"
IDEA: Following a friendship lands on each girl once per friend, so the average friend has avg(k²)/μ = μ + σ²/μ friends, more than the average person whenever counts vary, and epidemiologists can use those better-connected friends as early outbreak sensors.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8 · Motion 8.5 · Audio 8 · Concision 8 · Originality 8.5
WEIGHTED: 8.3   AFTER CEILING: 8.3  (lowest 8 + 2 = 10, not binding)
CAPS: none (all empirical claims carry on-screen citations; no overlaps or typos; runtime, pace, loudness, silence and static all inside limits)
FINAL: 8.3   PASS: no
FACTS:
- 8 girls, 10 reciprocated friendships, Marketville, Coleman data | Verified | Feld 1991 AJS 96(6) Fig. 1/Table 1 (facts.md quotes)
- "an Illinois high school" | Verified | Coleman 1961; 10 northern-Illinois schools (GESIS ZA1196)
- counts 1,4,4,2,3,3,2,1; mean 2.5 | Verified | recomputed: 20/8
- 20 tokens sum to 60, so friends average 3.0; +0.5 = 20 % | Verified | Σk² = 1+16+16+4+9+9+4+1 = 60; 3/2.5 = 1.2
- ring: 32/16 = 2.0 | Verified | 8 nodes × 2, 16 tokens of value 2
- Sue 4×4 = 16; avg(k²) = 60/8 = 7.5 | Verified | arithmetic
- squared distances 2.25 ×4 and 0.25 ×4, σ² = 10/8 = 1.25 | Verified | arithmetic
- 4² = (2.5+1.5)² = 2.5² + 1.5² + 2·2.5·1.5 = 16 | Verified | 6.25 + 2.25 + 7.5
- avg(k²) = μ² + σ² + 2μ·avg(d), avg(d) = 0 | Verified | Σ(k − μ) = 0 by the definition of μ
- μ + σ²/μ = 2.5 + 0.5 = 3.0; ring 2 + 0/2 = 2 | Verified | arithmetic
- Facebook 2011: mean ≈ 190, ⟨k²⟩/⟨k⟩ = 635, 5,000 cap, "a few … thousands" | Verified | Ugander et al. 2011 arXiv:1111.4503
- σ²/μ = 445 > 2 × 190 | Verified | 635 − 190 = 445 > 380
- Harvard 2009, 319 random students, 425 named friends | Verified | Christakis & Fowler 2010 PLoS ONE 5(9) e12948, Methods
- 13.9-day fitted lead; self-reported 3.2 days | Verified | C&F 2010 abstract/Results (web search confirms 3.2, 95 % CI 2.2–4.3)
- friends more central, so infected sooner | Verified | C&F 2010 Fig. 1 and Fig. 3 captions
- 5 of 8 have fewer friends than their friends' average; Sue and Alice more | Verified | Feld 1991 p. 1465
- per-girl friends' averages 4, 3.5, 3.33, 3.33, 2; Sue 2.75, Alice 3 | Verified | recomputed from the edge list
MECHANICS: runtime 3:41.4 · wpm 160 (speech) / 153 overall · max silence 2.23 s (planned prediction pause 0:11.7) · max static 2.50 s · −14.0 LUFS / −2.1 dBTP · lead 0.00 s / trail 1.49 s · WER 1.5 %
FIXES (highest impact first):
1. [1:13.5–1:18.8][Motion] The yellow "▲ 3" fulcrum fades in at its final spot (frames 1:17.4 → 1:18.0 show a dot growing at x = 3; nothing travels). This is the one moment where the motion could be the proof: the extra weight on the right moves the balance point. → As the token stacks land, TransformFromCopy the blue ▲ 2.5 and slide it right along the beam (smooth, 2 s) with an attached DecimalNumber counting 2.50 → 3.00, so it lands on "so they balance at three". Turn it yellow as it moves.
2. [2:21–2:52][Visual] In the episode's key formula, the leading μ of "μ + σ²/μ" sits about 15 px high: its descender ends level with the digits' baseline, and the gap after it is wider than the other "+" gaps (kf_25 at 2:23.3, crop; it carries into the Facebook beat, frame 2:46). → After the "μ slides" step, TransformMatchingTex into a freshly typeset `MathTex("\mu", "+", "{\sigma^2", "\over", "\mu}", ...)` of the final state, so baseline and spacing come from TeX, not from a moved glyph.
3. [0:55–1:06][Visual] The dashed gray "guess" box shows 3–5 px above and below the yellow-outlined friend bar, a doubled, fuzzy edge (kf_09 at 1:00.4, y ≈ 303 and 370). → When the bar fills, transform the guess box into a single dashed vertical tick at 2.5 inside the bar (or scale its height to 0.8× of the bar), so the bar shows one crisp outline and the guess is a mark.
4. [0:57.9 and 1:51.3][Audio/Clarity] (a) "friends average twenty percent more than girls": friends are girls, so the comparison is muddled, and Whisper drops "friends" there. → Change it to "the average friend has twenty percent more than the average girl." (b) "Split Sue's four" is transcribed "sus four", likely a clipped vowel. → Change it to "Split Sue's count, four, into…" or respell it for Kokoro ("Sooz"), then re-check the transcript.
5. [2:27–2:30][Clarity] The bar panel switches to 2.0 / 2.0 while the beam above still shows 2.5▲ / ▲3 and the main row reads 3.0. Nothing marks the bars as now describing the ring, so one frame claims two different friend averages. → For those 2 s, tag the bar values "ring" (GRAY, Text ≥ 18) and draw a short connector from the thumbnail, or leave the bars on 2.5/3.0 and let "2 + 0/2 = 2" beside the ring carry the callback alone.
6. [3:26.8–3:36.8][Concision] The landing re-explains the token pile-up already shown at 1:01–1:05 ("four on Sue … one on Betty"), and adds a tally panel. → Keep "Five have fewer… only Sue and Alice have more" and "So Betty looks at her one friend and sees four". Compress the middle to "Follow any friendship, yours included, and you land on a Sue far more often than on a Betty." Drop the "Sue ■■■■ 4× / Betty ■ 1×" panel and keep only the token pulse. That saves about 4 s.
7. [0:44–0:46][Motion] The average-girl readout counts up through "2.4" while the ring is still dissolving into the real network (sheet 3, 0:45). That is a momentary false value, the same class as the round-2 "1.9" fix. → Hold "2.0" until the real network has settled, then switch to 2.5 with a 0.5 s crossfade, or count only after the edges have drawn.
8. [1:51–2:24][Visual] After the beam lifts, the lower-left quadrant (below y ≈ −0.5, left of x ≈ −1) stays empty for about 33 s. Meanwhile a 25 % ghost of the bar panel holds the top-right, and the algebra is squeezed bottom-right (kf_19 at 2:04.8). → Fade the ghost panel to 0 for this beat (it returns at 2:25 anyway) and centre the algebra rows under the beam, so the eye moves straight down from picture to equation.
9. [1:43–1:47][Visual] The 8-word tag "square side = distance, drawn at 1/4 scale" is prose apologising for a drawing choice, and it competes with the squares. → Shorten it to "sides at ¼ scale" in GRAY, Text 18, placed directly under the squares' row.
10. [3:15–3:19][Visual] The read-outs hug the safe-area edge: text top ≈ 55 px (y ≈ 3.59) and the 13.9-day arrow tip at x ≈ 1843 px (6.54 units). They are also far from the in-chart arrow they copy. → Shift the read-out block 0.3 units down and 0.4 units left, and draw the copy's flight path, or park it directly above the chart's arrow at day 38–52.
11. [2:27–2:29][Visual] The ring thumbnail's node digits have a cap height of about 20 px, below the 24 px floor. → Scale the thumbnail to 0.55× instead of 0.42× (the lower-left band has room), or drop the digits and label it "everyone 2".
REACHES 9 IF ALL FIXED: yes. The structure already meets the bar: commit-by-0:12 hook with three candidates, stakes by 0:22, naive guess passing on the ring and failing by a measured +0.5 on real data, the beam/token picture turning into μ + σ²/μ, a cited real payoff with an honest limit (self-report 3.2 days), and a return to the cold-open graph. What remains is execution. Fix 1 (make the moving fulcrum the proof) and fixes 2–5 (formula typesetting, doubled outline, wording/pronunciation, the contradictory 2.0 bars) are what lift Motion, Visual, Audio and Clarity to 9.
KEEP: (1) The token device: every token reads the count where it lands, the counter 60/20, then the same tokens restacked on the lineup with two fulcra. It is a memorable, original way to see the size-biased average. (2) The colour grammar of the friend bar: a YELLOW outline filled BLUE to μ and PURPLE beyond, carried exactly into 190 + 445 = 635. (3) The ring-test-then-fail chain and its callback ("no spread, no gap", 2 + 0/2 = 2).
```

## Notes behind the scores

- **Hook 8.5.** Frame 0 shows the concrete object (Feld's eight girls). By 0:11 the viewer has a precise question with candidates 2.5 / 3 / 4 under drop lines, and "Pick one" is followed by a 2.2 s hold. Stakes (whom to watch for flu) land by 0:22 and pay off at 2:51. Tension sags through the 33 s algebra block (1:51–2:24). The closing line ("From most seats in this class, the view is the same") reframes the title more than the opening question.
- **Clarity 8.5.** Concrete first: 20 tokens and 60/20 come before Σk²/Σk. Every algebra step is justified on screen: d = k − μ is named, the signed distances merge into 0, and that 0 replaces avg(d). The cost is the wording at 0:57.9 and the contradictory 2.0 bars at 2:27–2:30 (fixes 4 and 5).
- **Visual 8.** One series background, a declared and consistent 3-hue palette, labelled axes with units, citations bottom-left held for the whole beat, no overlaps (198 checked states), and generous type. Deductions: the raised μ in the key formula, the doubled guess outline, the 33 s of lopsided composition with a ghost panel, the meta-tag, read-outs at the safe edge, and tiny thumbnail digits.
- **Motion 8.5.** Objects persist throughout. Counts ride with nodes into the ring and the lineup, tokens fly and restack, squares grow from their distance segments, area labels fly into σ², signed labels merge into 0, the Facebook bars fly to become the flu curves' origins, and the chart dissolves back into the cold-open graph. Static never exceeds 2.5 s. Two deductions: the decisive fulcrum shift is a fade, not a move, and the false "2.4" readout appears in transit.
- **Audio 8.** Pace is 160 wpm and loudness is exactly −14.0 LUFS with −2.1 dBTP. Sync is excellent: I checked about 25 deictics ("Sue holds four tokens" → box at 1:21, "cross term" → box at 2:01, "add to zero" → 0 at 2:09, "319 random students" → label at 3:05, "a Betty" → tally at 3:33, "most seats" → outlines at 3:39), and all landed within about 1.5 s. Deducted for the likely clipped "Sue's" at 1:51.3 and the swallowed "friends" at 0:57.9.
- **Concision 8.** About 5 % is removable, mostly the landing's re-explanation of the token pile-up.
- **Originality 8.5.** It uses real Feld data rather than a toy, a token/beam picture I have not seen used this way, the real Harvard curves rather than a simulated SIR, and no slop (0 banned phrases; one "So" signpost only).
