"""Narration for episode 9, one string per beat (scene.py imports these).

Kept separate so the script can be synthesized and timed without rendering:
    python videos/episodes/009-central-limit-theorem/narration_text.py

Cadence (round 5): CADENCE = "shaped" at speed 0.83 sets the sentence gaps; explicit pauses
only after key results and at the prediction; GAP_AFTER gives the silence after each narrate
block (>= 0.45 s at story-beat turns, about 0.9 s after the key results).  "the skewness,
squared" carries a comma because whisper heard the run-together "skewness squared" as "skewn".
"""

SPEED = 0.83                    # PRODUCTION_GUIDE §13.1: 0.82-0.84 (round 5: was 0.86, "hurried")
CADENCE = "shaped"              # sentence and beat gaps follow the sense (§4, §13.3)

PRONUNCIATIONS = {
    "Kohavi": "/kOhˈɑvi/",
    "A-B": "/ˈA bˈi/",
}

# Round 5 (continued): cut from 591 to under 500 words for the 3:15-3:35 budget (§13.1): the
# collect line, "for a bus" (repeated), the lean restated at 1,420, the Bing cap, the farthest-flash
# arithmetic, the median, and the landing's "collect forever".  Sentences are joined by plain
# spaces so the shaped cadence sets the gaps; explicit pauses only after key results and turns.
BEATS = {
    # 1 cold open: commit to a number (the textbook's thirty is the likely-wrong answer)
    "open": ("A hundred waits for a bus: mostly short, with a long tail. "
             "Textbooks say the average of thirty is safe to treat as a bell. "
             "For these waits, does it take thirty, three hundred, or over a thousand? [pause 1.6]"),
    # 2 stakes (the criterion: the bell's tails)
    "stakes": ("A-B tests lean on that bell's tails, and on revenue data, thirty is off by a "
               "factor of thousands."),
    # 3 naive build: voice the naive reading of the textbook's thirty, then test it
    "collect": "Maybe thirty means collecting enough waits. Collect a hundred thousand: smoother bars, same shape.",
    # 4 measured failure (skewness defined, term by term, with signed gaps)
    "fail": ("Measure the lean with skewness: the average cubed gap from the mean, left gaps "
             "counting negative, over the spread cubed. A perfect bell scores zero. "
             "These waits score about two, at every size."),
    # 5 the fix: average (the dilution, slowly)
    "average": ("So average instead. [pause 0.5] Four bus waits: one long wait, diluted by three "
                "short ones. [pause 0.8] Drop the average here. Do that ten thousand times."),
    "avg": ("These averages lean less: skewness one. Sixteen: point five. "
            "Sixty-four: point two five, nearly this perfect bell."),
    # 6 insight: the formula from the readings, then why it is root n (drawn as cubes)
    "formula": ("Each time n grows four times, the skewness halves: two over root n, and two is "
                "the skewness of one wait."),
    "why": ("The root comes from the cubes: add four bus waits, and the cubed gaps add up, "
            "four times one wait's. But the spread only doubles, so its cube grows eight times. "
            "Four over eight: half the lean. In general, n, over n to the one and a half."),
    # 7 why it is a bell: the extra tail weight fades faster still (on the same four panels)
    "kurt": ("Kurtosis, the extra tail weight, quarters each time. Every finer "
             "difference fades faster still, until only the bell survives. That's the central "
             "limit theorem: independent pieces, plus one condition."),
    # 8 payoff: how many is enough, measured where tests live (95% interval misses)
    "thirty": ("Back to the textbook's thirty. [pause 0.3] Two over root thirty is point three "
               "seven: close to a bell, by eye."),
    "tails": ("But tests live in the tails: a ninety-five percent interval should miss two and "
              "a half percent each side. [pause 0.4] A test estimates the spread from its own data. With "
              "lopsided waits, a low average comes with a small spread, so its interval stops "
              "short. [pause 0.8] At thirty: seven percent low, one percent high. [pause 0.5]"),
    "kohavi": ("Ron Kohavi and colleagues want each side within two to three percent. Their "
               "rule: n at least three hundred fifty-five times the skewness, squared. "
               "[pause 0.3] Divide by n and take the root: [pause 1.0] it's our formula, the "
               "average's skewness at most point oh five three. At three hundred, the lean is "
               "point one two: still too much. For these waits, fourteen twenty, and both "
               "misses reach the band. [pause 1.2]"),
    "bing": ("Bing's revenue per user had a skewness near eighteen: a hundred fourteen "
             "thousand users."),
    # the third answer to the cold open: for some data, no sample size is enough
    "never": "And for some data, no number on this axis is enough.",
    # 9 the condition: the lighthouse (one honest limit, words already defined)
    "lighthouse": ("A lighthouse a mile off a straight shore flashes at random angles, landing "
                   "somewhere on the shore."),
    "runmean": ("Track the average landing spot: it never settles. One flash, aimed almost along "
                "the shore, lands nine hundred miles away."),
    "dilute": "Repeat the thousand-flash average two hundred times: still as spread out as one flash.",
    "variance": "The theorem needs finite variance: no single piece can outweigh the rest. Here, it's infinite.",
    # 10 landing: answer the opening question on the opening image
    "landing": ("So the answer is over a thousand, not thirty. The bell was never in the data. "
                "[pause 0.3] It's in the average."),
}

# per-beat voice speed (default SPEED): the closing line is spoken a little slower (§4: >= 0.80)
BEAT_SPEED = {"landing": 0.80}

# silence after each narrate block (s): >= 0.45 at story-beat turns, longer after key results.
# "why" and "never" end with 0: the animation that follows them (the proof closing up, 1.0 s;
# the lighthouse fade, 0.5 s) is the pause.
GAP_AFTER = {
    "open": 0.12, "stakes": 0.65, "collect": 0.6, "fail": 0.9, "average": 0.55, "avg": 0.6,
    "formula": 1.0, "why": 0.0, "kurt": 0.6, "thirty": 0.55, "tails": 0.1, "kohavi": 0.05,
    "bing": 0.6, "never": 0.1, "lighthouse": 0.6, "runmean": 0.65, "dilute": 0.6,
    "variance": 0.3, "landing": 0.35,
}

if __name__ == "__main__":
    import sys
    sys.path.insert(0, "videos/toolkit")
    from sample_space.voice import synthesize
    total_w = total_t = 0
    for k, t in BEATS.items():
        s = synthesize(t, overrides=PRONUNCIATIONS, speed=SPEED, cadence=CADENCE)
        n = len(s.words)
        total_w += n
        total_t += s.duration + GAP_AFTER[k] + 0.12
        print(f"{k:10s} {s.duration:5.1f}s {n:3d}w {60 * n / s.duration:4.0f}wpm  cum {total_t:6.1f}")
    print(f"TOTAL {total_w} words, {total_t:.1f}s speech+gaps ({60 * total_w / total_t:.0f} wpm)")
