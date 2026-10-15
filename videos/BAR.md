# Sample Space: The Bar

Reference standard: **3Blue1Brown**, **Veritasium**, **Stuff Made Here**. Producers read this before scripting. Critics read it before scoring. A video passes only at **≥ 9.0 after caps**.

---

## 1. The bar in one paragraph

A 9/10 Sample Space episode lets a smart, busy viewer feel they worked out one idea themselves in about three minutes. Within 15 seconds it puts something concrete on screen: a puzzle, a number, or a wrong belief the viewer probably holds, and the viewer commits to an answer. It then tries the obvious approach on concrete data, lets it fail by a measurable amount and names why. The insight arrives as one picture that changes smoothly into the formula, so nothing is announced from nowhere. Every color means one thing for the whole episode, every motion carries information, and every sentence points at something visible. Nothing is decoration. The episode ends on a real, correctly cited data-science or social-science consequence and a closing line that changes how the opening looks. Shown next to 3b1b's Bayes video or Veritasium's 100-prisoners video, it would not look AI-made, and a critic's remaining comments would all be nitpicks.

---

## 2. Technique catalogue (adapted to 3 min, Manim + narrator, no host)

### 3Blue1Brown: explanation and visual craft
- **Concrete before abstract.** In his talk "Concrete before Abstract" (ODSC 2019), Grant says to "let examples precede generality" and to find "the type of example which guides the audience to rediscover the general results." *But what is a neural network?* (2017) starts from one 28×28 digit, not from a definition. **Ours:** the first minute works through one specific dataset with real numbers. Symbols appear only after the viewer has computed the specific case.
- **"You could have invented this."** *Essence of Calculus* (2017) and *Hamming codes, part 1* (2020) are built as steps the viewer could have taken. **Ours:** present the insight as 2–3 reasonable moves, and ask "what would you try?" once.
- **Motivation inside 30 s.** The SoME rules say it should be clear "within the first 30 seconds why they should care." *Probabilities of probabilities, part 1* (2020) opens on three sellers: 100% of 10 reviews, 96% of 50, 93% of 200. **Ours:** open on a decision the viewer would really face.
- **Color as fixed meaning.** In *Essence of Linear Algebra ch. 3* (2016), î is always green and ĵ always red. **Ours:** each script declares a palette, and a hue stays tied to one quantity across plot, label and equation term.
- **Transform, don't cut.** The same video moves the grid continuously, so the matrix columns are visibly where î and ĵ land. *Bayes theorem, the geometry of changing beliefs* (2019) reads the formula off areas. **Ours:** derive equations from the picture with `TransformFromCopy` and `TransformMatchingTex`, and keep objects alive across beats.
- **Honest limits.** *Why do prime numbers make these spirals?* (2019) deflates its own mystery, and the *Central Limit Theorem* video (2023) states its assumptions. **Ours:** say when the result breaks.

### Veritasium: misconceptions, hooks, tension
- **Misconception first.** In Muller et al. 2008 (*J. Computer Assisted Learning* 24(2):144–155, n = 364), videos that refuted misconceptions or staged a dialogue beat plain exposition (effect sizes 0.79 and 0.83). In *Khan Academy and the Effectiveness of Science Videos* (2011), students rated the clear video "clear," felt confident, and learned almost nothing. The "confusing" misconception video roughly doubled post-test scores, from about 6 to about 12 out of 26. **Ours:** voice the wrong belief as reasonable, visualize it, let it predict, then break it with data.
- **Make the viewer commit.** In *The Riddle That Seems Impossible Even If You Know The Answer* (2022), viewers anchor on (½)¹⁰⁰ before the loop strategy gives about 31%. **Ours:** one explicit prediction prompt, then a 1.5–2 s hold.
- **Legit bait, not click traps.** *Clickbait is Unreasonably Effective* (2021): titles should be enticing *and* true. **Ours:** make a surprising, accurate claim, and pay it off in full.
- **Simulation as argument.** *Is Success Luck or Hard Work?* (2019) simulates selection under a small luck weight. The Prisoner's Dilemma video (2023) animates Axelrod's tournaments, where Tit for Tat won. **Ours:** show an agent model's rules, then run it on screen.
- **Sourced claims.** *Is Most Published Research Wrong?* (2016) builds on Ioannidis (2005) and Bem (2011). **Ours:** author and year on screen for every empirical claim.

### Stuff Made Here: build, fail, iterate, measure
- **Measurable goal.** In *Moving hoop won't let you miss* (2020), success is binary and visible. **Ours:** define success as a number, such as "within 5%" or "beat 71% accuracy."
- **Failure chain as engine.** The explosive home-run bat (2020) went through four versions, and the V3 welds failed. In *Wrist rocket* (2022), each fix exposed the next failure. **Ours:** v1 fails visibly on data, the cause is named, then v2. Two iterations at most.
- **Measure, don't adjectivize.** The bat's best hit was measured at 617 ft. **Ours:** show the error metric as a live `DecimalNumber` that changes with the method.
- **Honest outcomes.** LockPickingLawyer opened the "unpickable" locks in 60 s and 52 s, and the postcard robot (2023) admits the time wasted on ML. **Ours:** show where the fixed method still fails.
- **Just-in-time explanation and deadpan humor.** Mechanisms are explained only when a failure demands them, with at most one dry line per episode.

---

## 3. Scoring rubric

| Dimension | Wt | 4 | 6 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|
| **Hook & tension** | 15 | Greeting, title card or definition first; no question by 0:30 | Question by 0:20 but generic ("What is variance?"); no stakes; tension flat | Concrete puzzle or misconception by 0:15; one question drives the episode; slight sag midway | Viewer commits to a likely-wrong prediction by 0:12; tension rises through build and fail; ending resolves the opening exactly | Title and first frame are irresistible; the ending re-sees the first frame; nothing to change |
| **Clarity & correctness** | 25 | Hand-wavy or wrong; jargon undefined; formula announced | Correct but in textbook order (definition, then example); a skipped step or notation jump | Concrete first; every step justified; one transition needs a rewatch | Viewer could re-derive it after one watch; assumptions stated; all numbers check out; sources correct | The canonical way to see this idea |
| **Visual design** | 15 | Slide-like and text-heavy; clutter; inconsistent colors | Clean but generic; crowded frames; color decorative; small labels | Semantic palette and clear hierarchy; at most 2 minor issues | Every frame has one focal point; all §5 standards met; nothing to remove | Frames people would screenshot to teach from |
| **Motion & animation** | 15 | Pops and cuts; static > 8 s, or too fast to read | Mostly FadeIn/Write; few meaningful transforms; uneven pacing | Objects persist and transform; motion follows narration; occasional decorative or rushed move | Every motion encodes a relation (origin, change, correspondence); reading time respected | The animation *is* the proof |
| **Audio / voiceover** | 10 | Missing, garbled or clipped; drift > 2 s | Robotic cadence; a mispronounced term; pace outside 130–175 wpm; gaps | Natural cadence at 140–165 wpm; in sync; one odd emphasis | Each deictic ("this bar") lands as the element highlights; pauses are intentional; loudness on target | Indistinguishable from a skilled human narrator |
| **Concision** | 10 | > 25% removable: preamble, recap, repetition | 10–25% removable; a tangent or a double explanation | < 10% removable; one slack beat | Cutting any sentence loses something | Feels shorter than it is, and complete |
| **Originality / non-slop** | 10 | Banned phrases and stock-like visuals; could be any channel | Competent but predictable (another coin-flip intro); 1 banned phrase | Fresh example or angle; specific voice; no slop | A non-obvious angle or image viewers would remember and share | Changes how the topic is taught |

**How the score is computed**
1. **Weighted** = Σ(weight × score) / 100, to one decimal.
2. **Ceiling rule:** overall ≤ lowest dimension + 2.
3. **Final** = the minimum of the overall score and every triggered cap.
4. **PASS** if and only if Final ≥ 9.0.

**Hard caps**

| Trigger | Max |
|---|---|
| Fabricated or misattributed study, statistic or quote | 4 |
| Voiceover missing, or out of sync (systematic drift > 1 s, or ≥ 2 times the narration names something not visible within ±2 s) | 5 |
| Placeholder or debug text, missing glyphs, render artifacts, black frames | 5 |
| Any factual or mathematical error (narration, on screen or in plotted data) | 6 |
| Generic AI-slop narration (≥ 2 banned phrases or patterns from §4) | 6 |
| Bullet-point slide: ≥ 3 parallel text lines as the main visual | 6 |
| Text overflowing the frame, clipped, or overlapping another element | 7 |
| On-screen typo or broken LaTeX | 7 |
| Not one coherent idea (the critic cannot state it in one sentence) | 7 |
| No hook by 0:15 | 7 |
| Dead air > 2.5 s, or a fully static frame > 8 s | 7 |
| Runtime outside 2:30–4:00; average pace < 120 or > 180 wpm | 7 |
| Ends on a recap list, "thanks for watching", or a subscribe request | 7 |
| Loudness outside −14 ± 3 LUFS integrated, true peak > −1 dBTP, or audible clipping | 7 |
| Exactly one banned phrase; or an empirical claim with no on-screen citation | 8 |

---

## 4. Anti-AI-slop checklist

**Banned phrases** (case-insensitive; each occurrence counts):
"in today's video", "let's dive in", "dive into", "delve", "it's important to note", "it's worth noting", "in conclusion", "in summary", "to sum up", "so to recap", "key takeaway", "game-changer", "unlock", "harness", "leverage", "the world of", "the realm of", "the landscape of", "buckle up", "without further ado", "let's get started", "imagine a world where", "picture this", "ever wondered", "have you ever wondered", "what if I told you", "here's the thing", "here's the kicker", "but here's the twist", "this is where X comes in", "enter: X", "plays a crucial role", "a testament to", "the power of", "the magic of", "navigate the complexities", "rich tapestry", "intricate", "journey", "seamless", "revolutionize", "cutting-edge", "mind-blowing", "incredible", "fascinating", "powerful tool", "data tells a story", "numbers don't lie", "simply put", "in a nutshell", "basically", "essentially", "stay tuned", "thanks for watching", "like and subscribe".

**Banned patterns**
- "It's not just X, it's Y" and "X isn't just Y" constructions.
- Rhetorical-question chains: two or more questions in a row.
- Triplets of abstract adjectives, as in "simple, elegant, and powerful".
- Empty superlatives: calling something "beautiful" or "surprising" without showing why.
- Hedging filler such as "in a sense" or "kind of", and signposting such as "now let's look at", "let's break it down" or "it turns out" (allowed once per episode).
- Colon or dash fake-reveals: "The answer? Simple:".
- Endings that list lessons or restate the video.

**Do instead.** Open on the object ("These three sellers…"). Point at what is on screen ("the orange bar just doubled"). Use nouns, numbers and action verbs. Ask one genuine question, then hold in silence while something visual answers it. End with a line that reframes the cold open.

**Banned visuals**, each with its replacement:
- Title card plus bullets → a single animated diagram.
- Emoji, clip-art or icons (brains, gears, lightbulbs, binary rain, node networks as wallpaper) → the actual data or structure.
- Word art, glows, gradients, drop shadows, particles or sparkles → flat shapes with semantic color.
- Narration repeated verbatim as on-screen sentences → labels, equations and short key terms only.
- Decorative motion (spinning, pulsing or bouncing to fill time) → motion that shows change or correspondence.
- Centered paragraphs → at most 7 words per block, placed next to their referent.
- Random scatterplots unrelated to the story, or fake data presented as real → real data, or data labeled "simulated".
- 3D without a reason → 2D.
- Real organizations' logos → plain text names.

---

## 5. Visual standards (1080p; Manim CE frame 14.22 × 8 units, 135 px per unit)

- **Safe area:** all text stays within x ∈ [−6.4, 6.4] and y ∈ [−3.6, 3.6], which is 5% title-safe. Nothing essential goes below y = −3.2, where captions and the player bar sit.
- **Spacing:** keep ≥ 0.15 units (20 px) between text and any other object. Overlaps are never allowed.
- **Type size, measured as cap height:**
  - Primary text and labels: ≥ 34 px.
  - Tick labels and citations: ≥ 24 px.
  - Main equation: 40–60 px.
  - Measured in Manim CE 0.22 (default config), a `MathTex` font_size is roughly its cap height in px, while `Text` renders about 1.37× larger. That gives these minimums:

    | Use | `MathTex` font_size | `Text` font_size |
    |---|---|---|
    | Primary text and labels | ≥ 36 | ≥ 26 |
    | Ticks and citations | ≥ 26 | ≥ 18 |

- **Word load:** at most 12 words of prose on screen at once (equations and ticks excluded), and at most 7 words per block.
- **Color:**
  - At most 4 semantic hues per frame and 6 per episode, plus neutrals (white and two greys).
  - Each hue has one meaning for the whole episode, declared in the script's palette block.
  - Never use red vs green alone; add a label or a shape.
- **Contrast:**
  - Text ≥ 7:1 against the background; colored labels ≥ 4.5:1.
  - Context you want de-emphasized is dimmed to 25–40% opacity, not deleted.
  - One flat dark background for the whole series.
- **Reading time:**
  - After text finishes drawing, hold it ≥ max(1.5 s, 0.8 s + 0.3 s per word).
  - Equations hold ≥ 2 s + 0.4 s per term before changing.
- **Static limit:** a fully static frame lasts ≤ 4 s. Up to 6 s is allowed only for a planned prediction pause, and 8 s or more triggers the cap.
- **Timing and easing:**
  - Minor moves take 0.5–1 s and transforms 1–2.5 s.
  - Nothing the viewer must track should move in under 0.4 s.
  - Use smooth or ease-in-out rate functions. Linear is only for time-like processes. No bounce, elastic or spin.
- **Equations:**
  - Never FadeIn a finished multi-term equation.
  - Build it term by term from its visual referent (`TransformFromCopy` from the bar or area it measures), and do the algebra with `TransformMatchingTex`.
  - Color each term like its referent, and flag the changed term for ≤ 1 s.
  - At most one new equation per 5 s.
- **Continuity:** objects persist and transform. Allow at most 1 hard cut per 30 s, and only at beat boundaries.
- **Charts:**
  - Every axis carries a quantity name and unit.
  - At most 6 ticks per axis, and numbers to ≤ 3 significant figures.
  - Dots have radius ≥ 0.05 units.
  - Data is real, or explicitly labeled "simulated".
- **Citations on screen:** "Author et al., Year · Venue" at bottom-left above y = −3.2, held ≥ 3 s.
- **Audio:**
  - −14 LUFS integrated (±1), true peak ≤ −1 dBTP.
  - Pace 140–165 wpm (a 3:00 episode is about 420–480 words).
  - Leading silence ≤ 1 s, trailing ≤ 2 s.
  - Any music bed sits ≥ 18 dB under the voice and never uses "inspirational" stock cues.
  - The script spells symbols out the way they should be spoken (for example, "x-bar" or "p less than point oh five").

---

## 6. Narrative template (3:00; scale proportionally to 2:30–4:00)

| Beat | Time | What happens | Source |
|---|---|---|---|
| **Cold open** | 0:00–0:12 | A concrete puzzle, number or common wrong belief is on screen in the first frame. The viewer is asked to predict. No greeting, no title card. | Veritasium, 3b1b |
| **Stakes** | 0:12–0:25 | Why the answer matters in the real world, in one sentence, then the question stated precisely. An optional series ident of ≤ 1.5 s. | 3b1b (SoME 30 s rule) |
| **Naive build** | 0:25–1:05 | The obvious method on a small concrete example with real numbers. It works at first. | SMH |
| **Fail** | 1:05–1:25 | It breaks, and the size of the failure is shown on screen (an error metric, a wrong prediction). The specific cause is named. | SMH, Muller |
| **Insight** | 1:25–2:15 | The one picture. The formula emerges from it by transformation, with one prediction pause. The general case comes only after the specific one. | 3b1b |
| **Payoff** | 2:15–2:45 | A real data-science or social-science result, with author, year and venue on screen, plus where the method still fails. | Veritasium, SMH |
| **Landing** | 2:45–3:00 | Return to the cold-open image, now seen differently. One final line, then end within 2 s. | All three |

---

## 7. Critic protocol

**Calibration.** Start every dimension at 7 and move it only on cited evidence.
- **7:** competent, clean, forgettable.
- **8:** strong; a good SoME entry.
- **9:** "I would believe a top educational channel's small team made this; only nitpicks remain."
- **10:** essentially never given.

Be harsh but fair:
- Every deduction cites a timestamp or frame.
- Do not penalize the absence of a host or live action, or the use of a synthetic voice as such. Do judge cadence, pronunciation and sync.
- Never reward polish that carries no meaning.
- Do not invent defects your evidence cannot show. Frames are 2 s apart, so infer motion from consecutive frames and the static-frame stats.

**Steps, in order**
1. **Script, read cold.** Write the episode's idea in one sentence; if you can't, apply cap 7. List every factual claim: numbers, studies, definitions, formulas, attributions.
2. **Fact-check.**
   - Recompute every number shown or spoken.
   - Re-derive the formulas.
   - Verify each cited study's author, year and finding, with web search if available.
   - Mark each claim Verified, Wrong or Unverifiable. Wrong → cap 6. Fabricated → cap 4. Unverifiable or uncited → a fix item, and cap 8 if there is no on-screen citation.
3. **Mechanical stats.** Record:
   - runtime
   - wpm (transcript words divided by speech seconds)
   - longest internal silence
   - leading and trailing silence
   - longest static stretch
   - LUFS and true peak

   Apply the caps these trigger.
4. **Transcript.**
   - Search for every §4 phrase and pattern.
   - Compare against the script for dropped or garbled lines.
   - Treat a mistranscribed technical term or name as a likely mispronunciation.
   - Locate the hook (first question or tension) and check it lands by 0:15.
5. **Contact sheet, read like a flipbook.** For each 10 s window, check:
   - Does what's visible match what is said at those timestamps (±2 s)?
   - Do objects persist and transform, or vanish and cut?
   - Is any frame slide-like or cluttered?
   - Does the beat structure match §6?
6. **Keyframes at full resolution.** Check against §5: margins, overlaps, clipping, typos and LaTeX, type size, word count, contrast, palette consistency and chart labeling.
7. **Score.** Use the §3 anchors, then compute weighted, ceiling rule, caps, final.
8. **Fixes.**
   - Order them by score impact.
   - Each fix must be specific and executable: timestamp, dimension, problem, exact change. "Improve pacing" is not a fix.
   - State whether applying all fixes would reach 9. If it wouldn't, name the structural problem (wrong hook, no failure beat, no visual insight).

**Required output**
```
EPISODE: <id> — "<title>"
IDEA: <one sentence>
SCORES: Hook _ · Clarity _ · Visual _ · Motion _ · Audio _ · Concision _ · Originality _
WEIGHTED: _._   AFTER CEILING: _._
CAPS: <cap → evidence @ mm:ss> | none
FINAL: _._   PASS: yes/no
FACTS: <claim> | Verified/Wrong/Unverifiable | <source>
MECHANICS: runtime _ · wpm _ · max silence _ s · max static _ s · _ LUFS / _ dBTP
FIXES (highest impact first):
1. [0:42–0:48][Visual] "variance" label overlaps the curve → move it up-right of the peak, buff 0.3; removes cap 7.
2. [0:00–0:09][Hook] opens on title text → open on the three-seller bars and ask "which would you buy from?"
...
REACHES 9 IF ALL FIXED: yes/no (+ why)
KEEP: <≤ 3 things that work and must survive revision>
```

---

*Sources:* Sanderson, "Concrete before Abstract" (ODSC India 2019, confengine.com); 3blue1brown.com/blog/some1 (SoME criteria); Muller et al. 2008, *JCAL* 24(2):144–155, doi:10.1111/j.1365-2729.2007.00248.x; T.H.E. Journal, "Watching Videos Does Not Necessarily Lead to Learning" (2015); University of Sydney, "The element of truth" (2024); veritasium.com (Prisoner's Dilemma references); Hackaday, Stuff Made Here project coverage (2020–23); Wikipedia, "Shane Wighton".
