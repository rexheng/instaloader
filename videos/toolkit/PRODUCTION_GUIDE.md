# Sample Space — Production Guide

For producer agents. Read `videos/BAR.md` first: it sets the quality bar. This file explains how to meet it with the toolkit.

```
videos/toolkit/setup.sh                                    # once per container (idempotent)
videos/toolkit/render.sh --preview ep/scene.py Episode /tmp/ep_preview.mp4   # iterate
videos/toolkit/render.sh ep/scene.py Episode ep/final.mp4  # 1080p30 master
videos/toolkit/review_kit.sh ep/final.mp4 ep/review        # evidence pack + BAR mechanics
videos/toolkit/publish.sh ep                               # commit + push this episode only
```

## 1. Episode layout

```
videos/episodes/NNN-slug/
  script.md        narration (beat by beat) + palette block (colour -> meaning) + sources
  scene.py         one NarratedScene subclass, class name `Episode`
  final.mp4        written by render.sh (1920x1080, 30 fps, H.264 CRF 22, AAC 160k, -14 LUFS)
  final.srt        subtitles (side effect)
  narration.json   beat start times, word timings, timing/layout warnings (side effect)
  narration.txt    "[mm:ss.s] beat text" (side effect, for critics)
  review/          review_kit output; report.md, metrics.json and transcripts are committed,
                   sheets/ and keyframes/ PNGs are git-ignored (regenerate in ~15 s)
  reviews.json     critic scores
```

## 2. Writing a scene

```python
from manim import *
from sample_space import *          # NarratedScene, colours, sizes, helpers, synth

class Episode(NarratedScene):
    EPISODE = 12
    TITLE = "Why five heads is rare"
    PRONUNCIATIONS = {"Bernoulli": "ber new lee"}   # extra, per episode
    CADENCE = "shaped"                               # gaps follow the sense; voice speed 0.83 (§4, §13.3)

    def construct(self):
        coins = VGroup(*[Circle(0.4, color=YELLOW) for _ in range(10)]).arrange(RIGHT)
        with self.narrate("Flip a fair coin ten times. How often do you get exactly five heads?") as beat:
            self.play(LaggedStart(*map(Create, coins)), run_time=beat.until_end_of("times"))
            beat.wait_until("five", offset=-0.1)      # next animation lands on "five"
            self.play(flag(coins[4]))
        # leaving the block waits for the audio to finish, then BEAT_GAP (0.35 s; shaped 0.45 s)
        self.say("Most people guess about half the time. [pause 1.5]")   # narrate over a still frame
        self.narrate_play("The real answer is closer to a quarter.", coins.animate.shift(UP))
        self.end_card()                                # <= 1.3 s, keeps trailing silence < 2 s
```

`with self.narrate(text) as beat:` synthesizes (cached), adds the audio at the current time with `add_sound`, and yields a `Beat`:

| Beat member | meaning |
|---|---|
| `beat.until("word", occurrence=1, offset=0)` | seconds from now until the word starts. Use it as the `run_time` of the animation *before* the word, so the next one starts on it |
| `beat.until_end_of("word")` | same, but until the word ends |
| `beat.wait_until("word", offset=-0.1)` | hold the frame until the word. A negative offset lands a highlight just before it |
| `beat.on("this", anim, ..., lead=0.15, run_time=...)` | deictic sync in one line: hold until 0.15 s before the word, then play. Use it for every "this / these / here" (§13.3) |
| `beat.remaining()` | seconds of audio left in this beat |
| `beat.time_of("word")`, `beat.duration`, `beat.words`, `beat.elapsed()` | raw timings |

Word matching ignores case and punctuation. Phrases work ("seven heads"), a prefix works ("flip" matches "flipped"), and `occurrence=2` picks the second hit. An unknown word raises `KeyError`, and the error lists the words that were spoken.

The scene logs **warnings**, which render.sh prints and stores in `narration.json`, when:
- animations ran past the narration, which leaves silence;
- an animation reached a cue word more than 0.3 s late (sync);
- the scene waits on a static frame for more than 4 s;
- the first beat starts after 1 s;
- the **overlap audit** finds text closer than 0.15 to anything, or outside the safe area (after every animation and hold; see §6, "Automatic overlap audit"), or text under the 24 px cap-height floor (`text-size`; 24–26 px labels are listed as `small-label`);
- a **glyph morph**: a `Transform`, `ReplacementTransform` or `TransformFromCopy` between *different* strings, or `number.animate.set_value(...)`, which renders as glyph soup (use `swap()`, `carry()`, `live_number()` or `TransformMatchingTex`; exempt a deliberate one with `allow_morph(anim)`);
- a **deictic** ("this X", "these", "those", "here") with no animation starting within −0.8…+0.4 s of the word;
- the voice speed is above 0.84, or the narration is over the concision budget (500 words, 3:35). See §13.

Call `self.check_layout()` to audit the frame at any point. Every warning is something a critic will also see, so fix them all.

Other members:
- `NarratedMovingCameraScene` adds camera moves (`self.camera.frame.animate...`).
- `self.fade_out_all(*keep)` is a deliberate hard reset (BAR allows ≤ 1 hard cut per 30 s).
- `narrate(..., gap=0)` chains two beats with no breathing room. `voice=`, `speed=`, `overrides=` and `cadence=` apply per beat.
- `CADENCE = "shaped"` (class attribute) makes sentence and beat gaps follow the sense (§4, §13.3). Recommended for every revision.

## 3. Style (`sample_space.style`, BAR §5)

| | |
|---|---|
| Background | `BG #14161B`, one flat dark slate. Set automatically |
| Colours | `BLUE` = primary quantity · `YELLOW` = focus / changing term · `GREEN` = positive / correct · `RED` = negative / error · `PURPLE` = spare second series · `INK` = text · `GRAY` = secondary text (ticks, axis titles, citations, notes) · `AXIS` = axis lines and tick marks · `DIM` = grid and context, never text. Each hue keeps **one meaning per episode**, declared in script.md. Never contrast red and green by colour alone. INK is 14.9:1 on BG and GRAY 7.7:1 (BAR: text ≥ 7:1; GRAY was 5.8:1 before round 6). Coloured labels are ≥ 4.5:1 |
| Fonts | `SERIF` = CMU Serif, which matches LaTeX, for all prose and labels. `SANS` = Inter, for tables only |
| `Text` sizes | `TITLE 46 · HEADING 38 · BODY 32 · LABEL 28 · SMALL 22`. Measured cap height is 1.28 × font_size, so the minimums are **27** for labels (34 px) and **19** for ticks and citations (24 px): Text 18 and 26 come out at 23 and 33 px, just under the floors critics measure |
| `MathTex` sizes | `EQ 52` for the main equation · `MATH 40` · `MATH_LABEL 36` for labels · `MATH_SMALL 30` for ticks only (29 px is under the 34 px label floor). Cap height is 0.96 × font_size: minimums 36 for labels, 26 for ticks. `cap_height_px(m)` measures any text after scaling |
| Layout | `SAFE_X 6.4`, `SAFE_TOP 3.6`, `CONTENT_BOTTOM -3.2`, `MIN_GAP 0.15` |
| Motion | `QUICK 0.5 · MOVE 0.8 · TRANSFORM 1.5 · SLOW 2.2`. `SMOOTH`/`EASE` rate functions; `LINEAR` only for time-like processes. `reading_time(text)` and `equation_hold(n_terms)` give BAR hold times |

Helpers:

| Helper | Purpose |
|---|---|
| `text(s)`, `label(s)` | Text in series style |
| `formula(*tex, size=EQ)` | MathTex; pass terms separately to colour or transform them |
| `wrap(s, max_width)` | Greedy wrap, at most 7 words per line, never wider than the frame |
| `fit(m)`, `keep_in_safe(m)` | Scale or shift a mobject into the safe area |
| `title(s)`, `caption(s)` | Top line, or a bottom line above y = -3.2. Use sparingly: no title + bullets |
| `citation("Muller et al., 2008 · JCAL")` or `citation(author=, year=, venue=)` | Bottom-left source. Hold ≥ 3 s. Change one citation into the next with `swap(old, new)` |
| `swap(old, new, run_time=0.7)` | Replace a label, citation or counter **in place**: old fades up and out, then new fades up and in. The two are never on screen together and no glyph morphs |
| `carry(source, target, path_arc=...)` | A value flies into its symbol or slot ("0.99" → "P(+∣sick)", a bar's "3.3" → "2ᵏ") as a cross-fade, never as glyph soup. Use instead of `TransformFromCopy` whenever the strings differ |
| `live_number(tracker, decimals, prefix=r"\text{error}=")` | DecimalNumber that follows a ValueTracker, as a measured metric |
| `axes((lo, hi), (lo, hi), x_label="height (cm)", y_label=..., x_ticks=[...])` | ≤ 6 ticks chosen automatically. `AXIS` lines, `GRAY` MathTex ticks and titles. `.x_title`, `.y_title` |
| `dots(ax, xs, ys, color)` | Scatter, radius 0.06 |
| `underline(m)`, `box(m)` | Mobjects; animate them with `Create` |
| `flag(m)` | ≤ 1 s indicate for a changed term |
| `dim(*ms)`, `undim(*ms)` | Context to 30 % opacity |
| `wordmark()`, `end_card(ep, title)` | Series ident and closing card |

For bar charts, pad the x range so the edge bars stay inside the axes, as in `axes((-0.6, 10.6), ..., x_ticks=[0, 2, 4, 6, 8, 10])`.

## 4. Voice (Kokoro-82M, local)

- **Narrator and pace:** the narrator is `af_heart`. The flat default speed is 0.78 (about 144 wpm over speech time in the demo; BAR asks for 140–165); with `CADENCE = "shaped"` and no `SPEED` set, NarratedScene uses 0.83. Kokoro is a fast talker at speed 1.0 (≈ 200 wpm), and its speed is not linear: 0.84 → 0.82 adds 2 % of runtime, 0.82 → 0.80 another 7 %. Use 0.82–0.84; the render warns above 0.84. All 12 episodes in round 5 ran 0.81–0.87, and the ones that were docked as hurried were docked for run-ons and flat gaps: every Audio 9 in rounds 3–4 was spoken at 160–164 wpm, which is 0.82–0.84 (§13.3). Below 0.80 with shaped cadence the pace falls under BAR's 140 wpm. Fit the budget by cutting words, not by speeding up.
- **Text handling:** the text is split into sentences with a 0.38 s pause between them. `[pause]` inserts 0.6 s and `[pause 1.5]` inserts 1.5 s. Use a pause for prediction holds and 0.9–1.4 s after each key result. A sentence that ends on a one-letter variable ("…becomes a k.") is now split correctly; it used to run into the next one.
- **Cadence (`CADENCE = "shaped"`, opt-in):** instead of a flat 0.38 s after every sentence, the gap follows the sentence's role: 0.30 s base (shorter than the flat 0.38), +0.30 after a question, +0.20 after a sentence that lands a number, +0.20 before a turn ("But", "So", "Now", "Then", "Back", "Here"…), +0.10 after a punch line of ≤ 4 words (capped at 0.9 s). A question or a result at the end of a beat gets 0.15–0.20 s of tail, beats are separated by 0.45 s instead of 0.35 s, number-dense sentences (two or more numbers) are spoken 2 % slower, and "hundred and twenty" is read "hundred twenty". Explicit `[pause x]` markers are kept exactly. Unless the scene sets `SPEED`, shaped cadence speaks at 0.83. Measured on episode 075's narration at speed 0.84, it adds 3 % of runtime and keeps the pace at 150 wpm. (A first version with longer gaps added 9 % and pulled the pace to 143 wpm, and at 0.80 to 132 wpm.) The long holds after key results stay explicit `[pause 0.9–1.4]`. Flat stays the default, so existing scenes are unchanged.
- **Loudness and timestamps:** each clip is normalized to -16 LUFS (mono, peak ≤ -2 dBFS), and render.sh masters the mix to -14 LUFS. Word timestamps come from Kokoro's own duration predictor. They agree with whisper to within about 0.1 s.
- **Writing for the voice:** write narration the way it should be spoken. Spell symbols out: "x bar", "p less than point oh five", "one thousand twenty-four" (US style with no "and": Kokoro can stretch the "and", and whisper then hears two numbers). misaki reads plain digits well ("0.87" becomes "zero point eight seven", "2024" becomes "twenty twenty four"), but spelled-out words give you control.
- **Pronunciation overrides:** `voice.PRONUNCIATIONS` holds the series defaults, for example PCA, k-means, R², p-value, LaTeX, NumPy, i.i.d., t-SNE, e.g. and i.e., plus researchers misaki gets audibly wrong (Sanjurjo, Gilovich, Tversky, Matejka, Weissgerber, Gelman, Ginsberg, Krueger, Hochberg, Ioannidis, Pfungst, Diaconis, Trefethen, LLaMA). Check any new name with `python3 -c "from sample_space.voice import _Engine; print(_Engine.get().g2p('Name')[0])"`; a soft "g", an English "j" in a Spanish name, or a stress on the wrong syllable needs an entry. Add per-episode entries with the `PRONUNCIATIONS` class attribute. A value is either a respelling (`"ber new lee"`) or IPA in misaki's alphabet between slashes (`"/kˈAmˌinz/"`). The written key stays the token, so `beat.until("R²")` still works.
- **Hearing a line:** `python -m sample_space "text" --out /tmp/a.wav --json` prints the word timings. `estimate_duration(text)` gives a rough length without running TTS.
- **Cache:** clips are cached in `~/.cache/sample_space/tts`, keyed by text, voice, speed and the overrides used. Editing one beat re-synthesizes only that beat, at about 0.5 s of CPU per second of speech.
- **Quirks:**
  - A very short single-word beat ("Yes.") can sound clipped, so attach it to a sentence.
  - ALL-CAPS words are read as letters.
  - Avoid unicode math in narration; write words instead.
  - Questions get a rising intonation, so do not end statements with "?".

## 5. Rendering

`render.sh [--preview] [--no-cache] <scene.py> <Class> <out.mp4>`

- **Queue:** a global flock queue (`/tmp/sample_space_render_slots`) runs at most `nproc-1` renders at once; the default is 3. Extra calls wait, so just call it. The queue wait is printed.
- **Work dir:** Manim media and its partial-movie cache live in `~/.cache/sample_space/renders/<hash>`, one per scene, class and quality. They are reused across your re-renders, so unchanged animations are not re-rendered, and they are pruned after 24 h.
- **Mastering:** postprocess.py masters the mix to -14.0 LUFS integrated with true peak ≤ -1.5 dBTP, verified on the final AAC. It then encodes x264 (preset slow, tune animation, CRF 22, yuv420p, +faststart) with AAC 160k at 48 kHz.
- **`--preview`:** renders 854x480 at 15 fps with a fast encode, for timing and layout passes. It is about 2.2× cheaper.
- **Music:** off by default. A procedurally made bed could not be judged tasteful without ears, so none ships. `SS_MUSIC=/path/bed.wav` mixes a supplied bed at -24 dB, side-chain-ducked under the voice (BAR: ≥ 18 dB under, no "inspirational" cues).
- **Measured speed** (4 vCPU, 1080p30, the 32.9 s demo; render seconds per video second):

  | Run | Wall time | s/s |
  |---|---|---|
  | Cold: TTS + Manim + master | 72 s | 2.2 |
  | TTS cached, fresh Manim | 50 s | 1.5 |
  | Re-render with everything cached (master only) | 25 s | 0.77 |
  | `--preview` (TTS cached) | 21 s | 0.63 |

  The x264-slow master is ≈ 0.5 s/s of that. For a 3-min episode of demo complexity, expect **≈ 6–7 min cold and ≈ 2.5–4.5 min to re-render after an edit** (only changed animations and beats are redone). Heavy scenes cost more (see §8).
- **Cache safety:** NarratedScene works around two Manim 0.22 cache problems, so cached re-renders are frame-identical to cold ones:
  - Manim drops `add_sound` right after a cached animation. Use `self.add_audio(path)` for sound effects; narration does this already.
  - Cached clips drift scene time by up to a frame each. Use `self.hold(seconds)` for a frame-exact wait.

## 6. Self-check before hand-off (mandatory)

1. `render.sh` prints `[sample_space] WARNING` lines. Fix every one.
2. `review_kit.sh ep/final.mp4 ep/review`, then read `review/report.md`. It reports:
   - runtime (2:30–4:00);
   - wpm over speech time (140–165);
   - leading silence (≤ 1 s), trailing silence (≤ 2 s) and the longest internal silence (≤ 2.5 s);
   - the longest fully static stretch (≤ 4 s; 8 s is a cap);
   - LUFS and true peak, black and empty frames, the BAR §4 banned-phrase and pattern scan (on both the transcript and the script);
   - WER of the whisper transcript against `narration.json`. A mis-heard technical term means a mispronunciation, so add an override;
   - **Narration craft** (§13): word and runtime budget, voice speed and per-sentence pace, cadence (full stops vs beat turns, the longest stretch without a breath), number load per 20 s, repeated phrases, "and" inside numbers, glyph morphs and deictic sync. Each flagged line is a defect critics docked in round 5–6.
3. **Look at the pictures** with the Read tool:
   - `review/sheets/sheet_NN.png`: a frame every 2 s with the words spoken at that moment underneath. Check that what is said is visible.
   - `review/keyframes/*.png`: full-resolution frames where each layout settles. Check margins, overlaps, clipping, LaTeX glyphs, label sizes, at most 12 words of prose on screen, and the palette.
4. Fix, re-render, re-run. Then `publish.sh videos/episodes/NNN-slug`.

### Automatic overlap audit

Critics cap an episode at 7 for a single small overlap, such as a token's digit covering the "e" of a name, or a fraction's "7" crossing the x-axis. The audit runs inside every render, after each `play()` and each `wait()`/`hold()`, so you see these defects before the critics do.

**What it checks.** For every visible text object (Text, each MathTex part, DecimalNumber), it measures real geometry: the text's bounding box against the actual stroke path of everything else (Bezier curves, not bounding boxes):
- text within 0.15 units of other text, or of any line, curve, arrow, graph edge, ellipse, dot, bar or panel;
- text outside x∈[-6.4, 6.4], y∈[-3.6, 3.6], or below y = -3.2 (the caption zone).

**What it lets pass.** These cases are reported only if the ink actually touches:
- a closed shape that fully contains the text, such as a label in its box, a digit in its token or a name inside an ellipse;
- the text's own small group, such as a fraction bar, a token's square, `underline(m)` or `box(m)`;
- axis lines and ticks, because tick labels and axis titles hug the axis by design;
- context fainter than 20 %.

It also skips anything under 5 % opacity, and anything drawn beneath an opaque panel that holds the text (a graph edge running under a token).

**Reading the warnings.** render.sh prints one line per finding, merged into time ranges. The most serious kinds come first:
```
[sample_space] WARNING overlap 0:57.2-1:12.9 (held 15.7s) Text 'Sue' @(-4.40, +1.44) vs Square [with MathTex '4'] @(-4.11, +1.20): overlapping by 0.02 (need >= 0.15)
[sample_space] WARNING overlap 2:41.4-2:50.9 (held 9.5s) MathTex '\frac{2}{7}' @(-1.70, -1.32) vs NumberLine (x-axis) of Axes @(-1.80, -1.62): overlapping by 0.05 (must not touch)
[sample_space] WARNING clearance 1:42.6-1:48.0 (held 5.4s) MathTex '\text{peak} \approx 11' @(-1.81, -0.90) vs Arrow @(-2.85, -0.81): gap 0.08 (need >= 0.15)
[sample_space] INFO layout audit: 12 issue(s) (5 overlap, 7 clearance < 0.15, 0 safe-area, 0 caption-zone; 0 allowed) in 164 checks; ...
```
- **`overlap`** means the text is touching or crossing something. That is a cap 7 for the critics, so fix every one.
- **`safe-area`** and **`caption-zone`** mean text that leaves the frame or sits in the player-bar zone. That is also a cap 7.
- **`clearance`** means the text keeps clear but sits closer than BAR's 0.15. It reads as cramped and costs Visual points.
- **`@(x, y)`** is each object's centre, in scene units.
- **`held 9.3s`** is how long the defect stays on screen. **"end of an animation, not held"** means it shows only in the last frame of an animation.

The findings also go to `narration.json` → `layout_audit`, with the kind, time range, both objects and the gap. `review_kit.sh` puts the count and the top 10 in `report.md`, and turns a held overlap into an implied cap 7.

**Fix it or allow it, with a reason.** To fix a finding, use `next_to(..., buff=0.2)`, move the label into free space, or put the label on an opaque `add_background_rectangle(color=BG, opacity=1)`. If an overlap is deliberate, such as a label meant to sit on its line or a strikethrough, declare it:
```python
self.allow_overlap(label, axis_line, reason="label marks where the curve crosses")
self.allow_overlap(watermark, reason="...")   # leave one mobject out of the audit entirely
```
- Allowed pairs are listed in `narration.json` and `report.md`, with their reasons, so critics can check them.
- `LAYOUT_AUDIT = False` turns the audit off for a whole scene, which you should rarely need: the critics' cap still applies.
- `LAYOUT_CLEARANCE` (default 0.15) changes the threshold. Never set it below the BAR value.
- The audit costs about 1–2 % of render time: it took 1.0 % on the demo, 1.8 % on episode 60 and 1.0 % on episode 75. It can never stop a render: if it fails internally, that check is skipped and counted in the summary line.

## 7. Manim pitfalls (CE 0.22)

- **Text overflow:** build prose with `wrap()`, and run `fit()`/`keep_in_safe()` on any group you place near an edge. The layout check catches most cases; the keyframes catch the rest.
- **Overlapping labels** (the overlap audit reports them; see §6):
  - Use `next_to(target, dir, buff=0.2)`, never absolute coordinates guessed for a moving object.
  - Re-place labels after `scale`/`shift`.
  - For labels that follow moving things, use `add_updater(lambda m: m.next_to(dot, UP, buff=0.15))`.
- **MathTex:**
  - Always use raw strings (`r"\frac{a}{b}"`).
  - `\text{...}` for words, `\%` for percent; Unicode such as Ω or ² fails, so use `\Omega` and `^2`.
  - Never split a tex argument inside braces (`"\frac{", "a}"` breaks). Use `substrings_to_isolate=["a"]` + `get_part_by_tex("a")` instead.
  - A LaTeX error shows up in `~/.cache/sample_space/renders/<hash>/render.log` with the .tex path. Test a formula in 2 s with `python -c 'from manim import *; MathTex(r"...")'`.
- **Text vs MathTex:** `Text` (Pango) is for prose and labels; it is fast, with no LaTeX. `MathTex` is for anything mathematical: variables in prose labels ("k = 7") belong in MathTex.
- **Z-order:** the last added is drawn on top. Use `m.set_z_index(2)` for labels over data and `self.bring_to_front(m)`. `TransformFromCopy` adds the copy on top.
- **Objects left on screen:**
  - After `Transform(a, b)` the *a* object is on screen (looking like b) and *b* is not, so keep animating *a*. Use `ReplacementTransform` if you want to continue with *b*.
  - `FadeOut` what you no longer need, or `dim()` it.
  - `self.mobjects` shows what is on screen.
- **Updaters:** call `m.clear_updaters()` before transforming an object that has updaters. `always_redraw` rebuilds every frame, so use it only for small objects.
- **Timing:**
  - Drive run_times from the beat (`until`, `remaining`) instead of constants.
  - Nothing the viewer must track moves in under 0.4 s.
  - Hold text for `reading_time(text)` and equations for `equation_hold(n)`.
  - Avoid > 4 s of total stillness; let something meaningful change, such as a highlight moving along the data.
- **Equations:** never `FadeIn` a finished multi-term equation. Build it with `TransformFromCopy(referent, term)` and `TransformMatchingTex`, as in the demo.
- **Coordinates:** the frame is 14.22 × 8 units at 135 px per unit, and (0, 0) is the centre. Keep text in x∈[-6.4, 6.4] and y∈[-3.2, 3.6]; citations sit just above y = -3.2.

## 8. Performance (minutes, not hours)

- **Iterate cheaply:**
  - Use `--preview` while iterating, which is about 2× cheaper.
  - Render the 1080p master only for the review.
  - Partial-movie caching means only changed animations re-render; keep the scene deterministic and seed randomness with `np.random.default_rng(7)`.
- **Precompute:** do data work with numpy/scipy/pandas at the top of `construct` (or cache it to a .npz), never inside updaters.
- **Mobject count** is the main cost:
  - Up to ~2 000 `Dot`s is fine.
  - Beyond that, draw one `VMobject` with many subpaths, or rasterize with matplotlib to an `ImageMobject`.
  - Don't `LaggedStart` 5 000 animations; animate groups.
- **Updaters:**
  - `always_redraw` and updaters that build new `MathTex`/`Text` each frame are slow; a new tex string means a LaTeX run.
  - Prefer `DecimalNumber` (`live_number`), which is glyph-cached, and updaters that move or recolour existing objects.
- **Static waits are free:** Manim reuses the frame. Long animations over many objects are not.
- **Camera:** `MovingCameraScene` zooms redraw everything each frame; that is fine for simple scenes but costly with thousands of objects.

## 9. Publishing

`publish.sh videos/episodes/NNN-slug ["message"]`:
- takes a global git lock;
- stages only that directory (honouring .gitignore);
- commits only that path, with the series trailer lines;
- pushes to `claude/modest-bardeen-s6wt4b`, running `git pull --rebase` when the remote moved, with retries and backoff.

It refuses files larger than 95 MB and refuses to run from another branch. It never touches other agents' files.

## 10. Troubleshooting

| Symptom | Fix |
|---|---|
| `Kokoro model not found` | Run `setup.sh`. Models live in `~/.cache/sample_space/models/kokoro` |
| `KeyError ... not in narration` | The cue word isn't in the beat text; the error lists the spoken words |
| Render hangs at "queued" | Other renders hold the slots: `cat /tmp/sample_space_render_slots/slot.*.owner` |
| Stale-looking output | `render.sh --no-cache ...` |
| Whisper fails in review_kit | Groq unreachable: re-run later or use `--no-whisper` |
| Audio slightly late or early vs a cue | Use the `offset=` on `until`/`wait_until` (typically -0.1 to -0.2 s) |

## 11. Lessons from critic rounds (read before scripting and before every revision)

Round-1 critics scored first drafts 6.0–8.4. These recurring defects cost the most points; check each one explicitly.

1. **On-screen arithmetic must be exactly right as displayed.** If the screen shows `0.39 × 576 ≈ 227`, that is a factual error (it is 224.6) → cap 6. Show the precision you computed with, or round the result from the displayed inputs. Recompute every displayed number in `facts.md`, including simulated values (rerun sims with a fixed seed and enough draws; quote "about" when noisy).
2. **Picture and numbers must agree at every moment.** No readout that says r = −0.06 while the ellipse shows r ≈ 0.85; no "N = 1,000,000" header over 400-dart histograms. Live labels need correct singular/plural ("1 target").
3. **Build key equations from the picture.** Every term of the central formula arrives by `TransformFromCopy` from the object it measures. A symbol-only morph (e.g. mean(k²) → μ² + σ²) with no geometric reason behind it reads as "announced", not derived.
4. **Respect reading time (BAR §5).** Results and equations hold ≥ 2 s + 0.4 s per term before they move. Each state of a flipbook or sequence must stay fully formed ≥ 1.5 s.
5. **No hard resets or whole-scene dissolves.** Transform persistent objects into the next beat. Never leave a near-empty frame (a lone axis, a blank background) while narration speaks.
6. **Check overlaps during motion, not just at rest.** Keyframes show settled layouts only. Extract frames every 0.25 s across each transform (`ffmpeg -ss T -t 2 -vf fps=4`) and look for labels struck through by moving lines, labels flying through formulas, and Indicate/scale effects that grow into neighbours.
7. **Show the payoff, don't assert it.** If the narration says "only X passes the test", the animation must show the others failing.
8. **Be original against the reference channels.** Don't reuse a famous video's exact example and numbers (e.g. Veritasium's "Bayesian Trap" 0.1% / 99% setup). Choose a fresh concrete case, a different real dataset, or a new angle on it.
9. **Specific stakes and landings.** "Every survey leans on this" is generic. Name a real data-science or social-science consequence (study, dataset, decision) and land the closing line on the cold-open image.
10. **Name the mechanism.** When a step depends on a causal or intuitive link (e.g. "more friends → exposed earlier"), say it in one sentence; don't leave the viewer to bridge it.

## 12. From 8.5 to 9 (every revision)

Polish alone plateaus around 8.4–8.5: critics' dimension scores cluster at 8–8.5. Passing needs a weighted score ≥ 9.0 with no dimension below 7 and no cap, which in practice means most dimensions at 9.

1. **Clear every cap first.** One overlap (cap 7) or one arithmetic slip (cap 6) sinks an otherwise strong episode. Sweep frames during motion as well as at rest (§11.6), and recompute every displayed number.
2. **Plan the climb.** At the start of a revision, for each dimension any critic scored below 9: quote BAR §3's "9" anchor, say concretely where the episode falls short, and name the specific upgrade. Write this in CHANGELOG.md before editing.
3. **Upgrades that move a dimension to 9:**
   - **Hook:** the first frame poses a concrete question with an explicit prediction prompt and a 1.5 s hold, by 0:12. The landing answers exactly that question on the same image.
   - **Concision:** cut 10–15 % of the words. Every sentence must change what is on screen; delete restatements and throat-clearing.
   - **Originality:** one image or angle unique to this episode (not the textbook figure) that a viewer would remember and describe to a friend; a fresh real-world anchor.
   - **Visual:** one focal point per frame; enlarge the subject; dim context rather than adding it; keep ≥ 0.15 units of clearance everywhere.
   - **Motion:** every move encodes a relation (origin, change, correspondence). Replace fades with transforms that carry meaning.
   - **Audio:** deictic words land on their highlight (`beat.until`); planned pauses at the prediction and at the reveal.

## 13. The systemic 9-blockers (from 28 critic reviews)

**Evidence.** These are the 28 most recent reviews: round 1 of the restarted cycle (filed as `round5-*`) for 12 episodes, plus round 6 for 002 and 007. Four dimensions never reached 9:

| Dimension | Mean | Reviews at 9 or above |
|---|---|---|
| Visual | 8.16 | 0 of 28. No surviving review (rounds 2–6) has scored Visual 9 |
| Audio | 8.34 | 0 of 28 |
| Concision | 8.04 | 0 of 28 |
| Clarity | 8.30 | 1 of 28 |

The 36 reviews from rounds 3–4 show the same defects. Below, "(n/28)" counts the round 5–6 reviews that docked a defect, and "(k/12)" counts episodes.

**The common cause.** Every episode carries 487–609 words of narration. To fit that under 4:00, producers raised the voice speed and shrank the gaps:
- `SPEED` is 0.81–0.87 in all 12 episodes; the toolkit default is 0.78.
- `BEAT_GAP` was cut to as low as 0.1 s.

Critics then docked:
- **Concision** for the length (16/28).
- **Audio** for a hurried, metronomic delivery (9/28, plus 10 reviews in rounds 3–4).
- **Visual** for frames that carry too much at once (20/28).
- **Clarity** for steps that are said instead of shown (19/28).

The cure is fewer words and fewer things per frame, not a faster voice. Episodes at 3:15–3:37 were never asked to get shorter. 9 of the 10 episodes at 3:41 or longer were told to cut runtime, and the tenth (009, 3:53) was handed about 8 s of cuts.

### 13.1 Targets

Check these before every hand-off. Each one comes from what critics penalised or rewarded. The render warnings and the "Narration craft" section of `review/report.md` measure most of them for you.

**Length and voice**

| Target | Value | Evidence |
|---|---|---|
| Runtime | **3:15–3:35**, never over 3:37 | 16/28 docked 3:41–3:58 and named 3:30 (four times), 3:35, 3:40 or 3:45 as the goal. None at 3:15–3:37 was told to cut |
| Narration words | **≤ 500** (aim for 470–500) | Episodes ran 487–609. A finished episode runs about 0.42 s of video per narration word (075: 526 words, 3:43), so 500 words ≈ 3:30 |
| Voice speed | **0.82–0.84**: never above 0.84, never below 0.80 | All 12 ran 0.81–0.87 and 9/28 called the delivery hurried. But every Audio 9 (rounds 3–4) was at 160–164 wpm, i.e. these speeds, with planned pauses. Below 0.80 the shaped pace falls under BAR's 140 wpm |
| Speech pace | **145–160 wpm** over speech time | BAR asks 140–165. Rewarded episodes ran 160–164; 075 at 0.84 with shaped cadence measures 150 |
| Pace inside sentences | **no sentence above 200 wpm** (report flags 4 or more) | Medians were 165–178 wpm whether or not critics called the episode hurried. The 2–8 sentences per episode above 200 wpm are long, number-dense ones, and that is where "hurried" and "rushed key number" were heard |
| Cadence | `CADENCE = "shaped"`. Beat turns at least **0.15 s longer** than full stops. **0.9–1.4 s** after each of the 2–4 key results. Prediction holds of **1.5–2 s** | Every Audio 9 given (rounds 3–4) cited planned 0.9–1.4 s pauses after results and pauses at beat turns |
| Breath | no stretch longer than **15 s** without a pause of at least 0.35 s | Found in 7/12 episodes, up to 35 s. 009's critic heard "26 s without a sentence break" |

**Sync, density and the frame**

| Target | Value | Evidence |
|---|---|---|
| Deictics | every "this / these / those / here" lands on an animation that starts **−0.8 to +0.4 s** from the word (`beat.on`) | 11/28 docked misses of 1–2 s. Audio 9 required every one within about 0.6 s |
| Numbers | at most **one new number per sentence**, and **≤ 8 different numbers** in any 20 s | 10/28 docked runs such as "355, 0.053, 1,420, 18, 114,000, $10, 10,000 in 35 s" |
| Ideas | one new idea per beat; every step of the key derivation drawn | 19/28 docked a key step that was said, not shown |
| Focal point | one object at full strength, the rest at ≤ 30 % (`dim()`) or gone. **≤ 2 equations** and **≤ 12 words of prose** on screen | 20/28 docked frames with no single focal point. Prose loads of 20–22 words were measured in 4 reviews |
| Composition | no half or quadrant of the frame empty for more than 4 s while narration runs (planned holds excepted) | 12/28 docked half-empty frames held 6–40 s |
| Labels | Text ≥ 27 / MathTex ≥ 36 for anything the narration refers to. Text ≥ 19 / MathTex ≥ 26 for ticks and citations, **after any scaling** | 10/28 measured labels at 20–26 px |
| Charts | every axis has a name, a unit and at least 2 numbered ticks. Every marker on a summary line has a tag of ≤ 3 words | 10/28 docked unlabelled axes or bare numbers |
| Glyph morphs | **0** | 13/28 docked a Transform between different strings |
| Landing and payoff | landing ≤ 15 s, one move. Payoff: one real result (≤ 30 s) plus one honest limit (≤ 15 s, no new terms) | 10/28 docked a second payoff, a three-idea landing (38–44 s) or a late tangent |

### 13.2 Visual (mean 8.16)

1. **No single focal point (20/28, 12/12).** The worst frames were the payoff frames.
   - 009 at 2:40 held a readout, a histogram, a miss meter, three stacked equations, a log axis and a citation.
   - 075's ladder held 14 bars, counts, fractions, a 3×3 patch and two thumbnails.
   - 008's middle third held three panels and a six-line equation stack.

   *Fix:* name the one object the current sentence is about. Dim everything else to 30 % or remove it. When a derivation ends, collapse it to its one-line result before the next beat. Keep at most two equations and 12 words of prose on screen.
2. **Empty or lopsided frames (12/28, 10/12).**
   - The right half was empty for 15 s (002).
   - The lower-left quadrant was empty for 33 s (060).
   - The cold open used the top 55 % of the frame (006).
   - A reveal floated alone on an empty frame (007).
   - Narration ran over a near-empty bridge frame (002, 004).

   *Fix:* scale the subject up into free space and centre it. Turn the outgoing object into the incoming one so no frame goes empty. A layout that will hold for 10 s should fill at least half the frame width.
3. **Unlabelled axes and anonymous markers (10/28).**
   - Histograms with no y scale (001, 003, 009).
   - A ladder with no vertical quantity (075).
   - Four bare numbers on the payoff line (007).
   - Empty "?" lanes (004).

   *Fix:* give every axis a quantity, a unit and at least two numbered ticks. Give every marker a short tag: "halving", "letter odds", "LLM".
4. **Text below the size floors (10/28, 8/12).** Measured sizes included:
   - "your guess" at 25 px;
   - citations at 22–23 px (Text 18);
   - ghost digits at 22 px (`MATH_SMALL - 4`);
   - "×28 wide" and "peak ≈ 11" at 24 px;
   - run costs at 30 px;
   - thumbnail digits at 20 px (a group scaled to 0.42×).

   *Fix:* use the measured minimums in §3. Never scale a group that holds text without resizing the text. The audit reports `text-size` for anything under 24 px and lists 24–26 px labels as `small-label`. Axis numbers and `citation()` are held only to the 24 px floor; mark a hand-made tick label with `m.ss_role = "tick"` to do the same.
5. **Cross-fades in place, and copies flying through text (9/28).**
   - Citations swapped by simultaneous FadeOut and FadeIn read as garbled text (006, 007).
   - "our jump" sat superimposed on "Schelling's jump" (075).
   - A "?" overlapped a counter (008).
   - A formula slid through a fading label (005).

   *Fix:* `swap(old, new)`. Route flights around text, and dim the record before 102 numbers fly through it.
6. **Glyph soup (13/28).** Examples: "2/7 <" morphing into "3/8 ≥" (075); counters showing "¿ riffles" and "9▒%" (006); "3.3" becoming "2ᵏ" (007); 16.76 smeared mid-flight (020); doubled "μ μ" (060). *Fix:* use `swap()` for a changed label, `carry()` for a value flying into a symbol, `live_number()` for counters, and `TransformMatchingTex` with identical tokens for algebra. The render warns on each one.
7. **Grey text under 7:1.** Two critics measured 6.1–6.5:1. The old GRAY was 5.8:1 in every episode. *Fix:* GRAY is now 7.7:1, and axis lines use `AXIS`. Never use DIM or AXIS for text.
8. **Palette slips (6/28).**
   - Yellow dimmed to 30 % turned olive (002).
   - Yellow carried five jobs in one episode (003).
   - Purple meant "Cornell data" while no data was on screen (004).
   - A red "drifted" cross was still shown after the drift was fixed (020).

   *Fix:* fade a saturated hue only to 60 %, or recolour it GRAY. A hue appears only while its quantity is on screen.

### 13.3 Audio (mean 8.34)

1. **Hurried, metronomic delivery (9/28 and 7/12, plus 10 reviews in rounds 3–4).**

   Measured in narration.json:
   - Every full stop gets 0.40–0.42 s, with a variation of 0.05–0.08.
   - In 8/12 episodes the beat turns are no longer (medians 0.35–0.44 s).
   - Sentences run 165–178 wpm at the median.
   - 7/12 episodes have a stretch longer than 15 s with no pause of at least 0.35 s.

   Critics heard this as "the cadence is the TTS default", "metronomic", "beat boundaries get the same breath as mid-thought commas" and "the thesis gets no air".

   *Fix:*
   - Keep `SPEED` at 0.82–0.84; never 0.85–0.87 to squeeze words in, and never below 0.80, where the pace drops under 140 wpm.
   - Set `CADENCE = "shaped"`.
   - Split every sentence the report lists above 200 wpm; they are usually long sentences full of numbers.
   - Add `[pause 0.9]` to `[pause 1.4]` after the 2–4 sentences that land a result.
   - Never chain a beat turn with `gap=0`, and never set `BEAT_GAP` below 0.35.
2. **Deictics that miss (11/28, 7/12).** The failures came in three kinds:
   - The visual arrives 1–2 s after the word: "halves", "tails", "seven percent", "infinite" (009); "box" (020).
   - The word comes before its referent exists: "this chart" (075), "data first" (008), "police watch list" over an empty frame (002).
   - The word names something no longer on screen: "three point three doublings" (007).

   *Fix:* `beat.on("this", anim)`. Never point back at an object that has left: bring back a ghost at 40 %, or cut the phrase. The render lists every deictic word with no animation landing on it.
3. **Word-level TTS artefacts (10/28).**
   - "Edwin" was held for 1.2 s.
   - "That" lasted 1.04 s right after a rushed "four point one one" (0.74 s).
   - "In the other" was crushed to 0.57 s, and "other" vanished.
   - The "-ed" of "picked" and the "in" of "three in four" were swallowed.
   - The "and" in "five hundred and seventy-six" was stretched.
   - "Nine thousand nine hundred eighty" was spoken three times in the same flat tone.

   *Fix:*
   - Write numbers without "and"; shaped cadence drops it for you.
   - Round long numbers in speech ("about ten thousand") and let the screen carry the exact value.
   - End a sentence on its key number.
   - Keep contrast words ("other", "second") away from clause edges.
   - Re-synthesize a doubtful beat with `python -m sample_space "…" --json`. A function word held 0.5 s or longer is a defect, and so is a key number shorter than 0.25 s per word.
4. **Names and symbols (7/28).**
   - "Jaynes" was heard as "Jane".
   - "Sanjurjo" was read with an English "j".
   - "Sue's" was heard as "sus".
   - "s x" fused into "sx".

   *Fix:* the global dictionary now covers the names misaki gets wrong (§4). Rephrase possessives of short names ("Sue's count, four"). Spell symbols ("ess ex") and keep them out of fast clauses.
5. **Garden paths and homophones (4/28).** "Two to the k levels off" (where "levels" was a noun earlier in the episode), "halves too" heard as "halves two", and waits/weights in a sentence about cubes. *Fix:* read every sentence aloud once, looking for a second parse.

### 13.4 Concision (mean 8.04)

1. **The narration says what the frame shows, or says it twice (24/28, 12/12).** Examples:
   - "Same circle, same gold rule" over the same circle.
   - "Sixty over twenty" while 60/20 sits on screen.
   - A ÷10,000 step narrated for 14 s.
   - Landings that re-explain the token pile-up.
   - "That's one vote per row" 25 s after "each row gets one vote".

   *Fix:* apply the mute test to every sentence. If muting it loses nothing the frame does not already show, cut it. `report.md` lists every repeated four-word phrase; each repeat must be a deliberate callback.
2. **Too long (16/28, 9/12).** See the budget in 13.1. Cut in this order:
   1. Restatements.
   2. The landing's extra moves.
   3. The second payoff.
   4. Spoken arithmetic the picture already shows.
3. **Second payoffs, multi-move landings and late tangents (10/28).**
   - A landing with three ideas in 38–44 s, where §6 budgets 15 s (002).
   - An honest-limit beat that introduces kernel bandwidth, "R's default" and cross-validation in 18 s (008).
   - A 48 s lighthouse appendix after the question was already answered (009).
   - Three payoffs in 3:42 (020).

   *Fix:* one payoff, one limit that uses only words already defined, and one closing move.

Concision 9 was given only when the critic wrote "I could not find a sentence whose removal costs nothing."

### 13.5 Clarity (mean 8.30)

1. **The key step is asserted, not shown (19/28, 11/12).**
   - "The fractions add up" with no sum and no comparison on screen (007).
   - The ÷N step between √N halves and ½/√N, missing (005).
   - The tangent point placed at r·s_y "so…" with no picture of why (020).
   - "12 heads in 8 rows" never visibly producing 17/42 (004).
   - Why a low average gets a short interval, covered in 5 s (009).

   *Fix:* find the one step a viewer could not redo on paper. Give it its own picture and at least 4 s. The critics' 9 reads "I could re-derive it after one watch."
2. **The screen contradicts the narration for a moment (11/28).**
   - A false equation held for 1–1.5 s mid-build: Σhᵢ/nᵢ = 17/42 (004), and D(bell‖data) = … = 5.77 (008).
   - Stale counts left under a new header (002).
   - 2.0 and 2.5 shown in the same frame (060).
   - A column that balloons before it shrinks (007).

   *Fix:* every frame must be true if paused. Write "= ?" before swapping a result. Change dependent numbers in the same animation. Animate width and height together.
3. **One word with two meanings, undefined terms, and pronouns with no antecedent (10/28, 9/12).**
   - "gap" used three ways (003).
   - "hot" reused for after-tails (004).
   - Four names for one quantity (005).
   - GSR, "spread", covariance, "R's default" and cross-validation left undefined.
   - "it" used 2.5 min after flu was last mentioned (060).

   *Fix:* keep a glossary in script.md with one name per quantity. Never say a term that is not defined on screen. Never let a pronoun reach across a beat.
4. **Too much in 20 s (10/28).** Examples: four ideas in 15 s at 180 wpm (004); three equations in 7 s (009); four equation states in 20 s (006); three precision figures in 18 s (002). *Fix:* keep to the number and equation limits in 13.1. `report.md` shows the busiest 20 s as "Number load".

### 13.6 What the toolkit now does, and what it cannot do

| Change | Targets |
|---|---|
| `GRAY` 7.7:1 for text; `AXIS` (the old grey) for axis lines and ticks | Grey text under 7:1 |
| Measured size constants (`TEXT_LABEL_MIN 27`, `TEXT_TICK_MIN 19`, `MATH_LABEL 36`, `MATH_TICK_MIN 26`, `cap_height_px`); the `text-size` / `small-label` audit in every render | Labels at 20–26 px |
| `swap()`, `carry()`, and the glyph-morph warning (`allow_morph(anim)` to exempt one) | Cross-fade garble and glyph soup. Six episodes had written their own `swap` |
| `CADENCE = "shaped"`; sentences ending in a one-letter variable now split; dictionary entries for misread names | Metronomic gaps, run-ons, name errors |
| `beat.on(word, anim)` and the deictic-sync warning | Deictic misses |
| Warnings for speed above 0.84 and for the 500-word / 3:35 budget | Hurried voice, length |
| `review_kit` "Narration craft" section: budget, pace, cadence, breathless runs, number load, repeated phrases, "and" in numbers, glyph morphs, deictic sync, small labels | Makes each defect visible before the critics see it |

What the toolkit cannot decide is what the frame is *about*. Focal point, empty halves, asserted steps, contradictory frames and terminology are still craft. They account for most of the Visual and Clarity points.

### 13.7 Revision order that clears all four

1. **Cut to budget first** (≤ 500 words, 3:15–3:35):
   1. Apply the mute test.
   2. Reduce the landing to one move.
   3. Drop the second payoff.
   4. Shorten spoken arithmetic.
2. **Set the voice.** Set `SPEED` to 0.82–0.84 and `CADENCE = "shaped"`. Add `[pause 0.9–1.4]` after the key results, and leave the prediction hold at 1.5–2 s. Split the sentences listed above 200 wpm.
3. **Render a preview** and fix every warning: glyph-morph, deictic sync, text-size, overlap, budget.
4. **Frame pass**, one keyframe at a time:
   - Name the focal object, then dim or remove the rest.
   - Label every axis and marker.
   - Fill any half of the frame that stays empty for more than 4 s.
5. **Clarity pass.**
   - Give the one hard step a picture.
   - Pause in the middle of every transform and check that what is on screen is still true.
   - Keep one name per quantity.
6. **Run `review_kit`.** The "Narration craft" section should have no flagged line. If one remains, its text names the fix.

## 14. Revision budget (finish inside one usage window)

Revisions that run for hours get cut off by usage limits before critics ever see them. Keep each revision to roughly 60–90 minutes:
- Iterate on layout and timing with `render.sh --preview` (about 6× faster); check frames there.
- At most **2 full 1080p master renders** per revision: one after the fixes, one final after inspecting it.
- Fix the highest-impact items first (caps, then the lowest-scoring dimensions per §12–13); stop polishing once every listed fix has landed.
