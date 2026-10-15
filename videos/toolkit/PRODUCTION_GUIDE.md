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
    # SPEED = 0.78                                   # tune 0.74-0.84 to land at 150-160 wpm

    def construct(self):
        coins = VGroup(*[Circle(0.4, color=YELLOW) for _ in range(10)]).arrange(RIGHT)
        with self.narrate("Flip a fair coin ten times. How often do you get exactly five heads?") as beat:
            self.play(LaggedStart(*map(Create, coins)), run_time=beat.until_end_of("times"))
            beat.wait_until("five", offset=-0.1)      # next animation lands on "five"
            self.play(flag(coins[4]))
        # leaving the block waits for the audio to finish, then BEAT_GAP (0.35 s)
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
| `beat.remaining()` | seconds of audio left in this beat |
| `beat.time_of("word")`, `beat.duration`, `beat.words`, `beat.elapsed()` | raw timings |

Word matching ignores case and punctuation. Phrases work ("seven heads"), a prefix works ("flip" matches "flipped"), and `occurrence=2` picks the second hit. An unknown word raises `KeyError`, and the error lists the words that were spoken.

The scene logs **warnings**, which render.sh prints and stores in `narration.json`, when:
- animations ran past the narration, which leaves silence;
- an animation reached a cue word more than 0.3 s late (sync);
- the scene waits on a static frame for more than 4 s;
- the first beat starts after 1 s;
- the layout check fails at the end of a beat: text outside x∈[-6.4, 6.4] or y∈[-3.6, 3.6], text below y = -3.2, text overlapping text, or a shape running through text.

Call `self.check_layout()` at any point, and use `allow_overlap(m)` to exempt a deliberate overlap. Every warning is something a critic will also see, so fix them all.

Other members:
- `NarratedMovingCameraScene` adds camera moves (`self.camera.frame.animate...`).
- `self.fade_out_all(*keep)` is a deliberate hard reset (BAR allows ≤ 1 hard cut per 30 s).
- `narrate(..., gap=0)` chains two beats with no breathing room. `voice=`, `speed=` and `overrides=` apply per beat.

## 3. Style (`sample_space.style`, BAR §5)

| | |
|---|---|
| Background | `BG #14161B`, one flat dark slate. Set automatically |
| Colours | `BLUE` = primary quantity · `YELLOW` = focus / changing term · `GREEN` = positive / correct · `RED` = negative / error · `PURPLE` = spare second series · `INK` = text · `GRAY` = axes and secondary · `DIM` = grid and context. Each hue keeps **one meaning per episode**, declared in script.md. Never contrast red and green by colour alone. All text colours are ≥ 4.5:1 on BG, and INK is 14.9:1 |
| Fonts | `SERIF` = CMU Serif, which matches LaTeX, for all prose and labels. `SANS` = Inter, for tables only |
| `Text` sizes | `TITLE 46 · HEADING 38 · BODY 32 · LABEL 28 · SMALL 22`. Minimums are 26 for labels and 18 for ticks and citations |
| `MathTex` sizes | `EQ 52` for the main equation · `MATH 40` · `MATH_SMALL 30` for ticks. Minimums are 36 and 26 |
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
| `citation("Muller et al., 2008 · JCAL")` or `citation(author=, year=, venue=)` | Bottom-left source. Hold ≥ 3 s |
| `live_number(tracker, decimals, prefix=r"\text{error}=")` | DecimalNumber that follows a ValueTracker, as a measured metric |
| `axes((lo, hi), (lo, hi), x_label="height (cm)", y_label=..., x_ticks=[...])` | ≤ 6 ticks chosen automatically. Grey axes and MathTex ticks. `.x_title`, `.y_title` |
| `dots(ax, xs, ys, color)` | Scatter, radius 0.06 |
| `underline(m)`, `box(m)` | Mobjects; animate them with `Create` |
| `flag(m)` | ≤ 1 s indicate for a changed term |
| `dim(*ms)`, `undim(*ms)` | Context to 30 % opacity |
| `wordmark()`, `end_card(ep, title)` | Series ident and closing card |

For bar charts, pad the x range so the edge bars stay inside the axes, as in `axes((-0.6, 10.6), ..., x_ticks=[0, 2, 4, 6, 8, 10])`.

## 4. Voice (Kokoro-82M, local)

- **Narrator and pace:** the narrator is `af_heart` at speed 0.78, about 150–160 wpm for prose (BAR asks for 140–165). Kokoro is a fast talker at speed 1.0 (≈ 200 wpm), so do not raise the speed.
- **Text handling:** the text is split into sentences with a 0.38 s pause between them. `[pause]` inserts 0.6 s and `[pause 1.5]` inserts 1.5 s. Use a pause for prediction holds.
- **Loudness and timestamps:** each clip is normalized to -16 LUFS (mono, peak ≤ -2 dBFS), and render.sh masters the mix to -14 LUFS. Word timestamps come from Kokoro's own duration predictor. They agree with whisper to within about 0.1 s.
- **Writing for the voice:** write narration the way it should be spoken. Spell symbols out: "x bar", "p less than point oh five", "one thousand and twenty four". misaki reads plain digits well ("0.87" becomes "zero point eight seven", "2024" becomes "twenty twenty four"), but spelled-out words give you control.
- **Pronunciation overrides:** `voice.PRONUNCIATIONS` holds the series defaults, for example PCA, k-means, R², p-value, LaTeX, NumPy, i.i.d., t-SNE, e.g. and i.e. Add per-episode entries with the `PRONUNCIATIONS` class attribute. A value is either a respelling (`"ber new lee"`) or IPA in misaki's alphabet between slashes (`"/kˈAmˌinz/"`). The written key stays the token, so `beat.until("R²")` still works.
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
   - WER of the whisper transcript against `narration.json`. A mis-heard technical term means a mispronunciation, so add an override.
3. **Look at the pictures** with the Read tool:
   - `review/sheets/sheet_NN.png`: a frame every 2 s with the words spoken at that moment underneath. Check that what is said is visible.
   - `review/keyframes/*.png`: full-resolution frames where each layout settles. Check margins, overlaps, clipping, LaTeX glyphs, label sizes, at most 12 words of prose on screen, and the palette.
4. Fix, re-render, re-run. Then `publish.sh videos/episodes/NNN-slug`.

## 7. Manim pitfalls (CE 0.22)

- **Text overflow:** build prose with `wrap()`, and run `fit()`/`keep_in_safe()` on any group you place near an edge. The layout check catches most cases; the keyframes catch the rest.
- **Overlapping labels:**
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
