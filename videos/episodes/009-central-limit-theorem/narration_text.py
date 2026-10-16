"""Narration for episode 9, one string per beat (scene.py imports these).

Kept separate so the script can be synthesized and timed without rendering:
    python videos/episodes/009-central-limit-theorem/narration_text.py

Cadence (round 3): sentences inside a beat are joined by "[pause 0.15]" (about 0.27 s of
silence once the clip trim pads are added), and GAP_AFTER gives the silence after each narrate
block: short inside a story beat, about 0.9 s at the seven story-beat boundaries.
"""

SPEED = 0.86
S = " [pause 0.15] "            # the short breath between sentences of one beat

PRONUNCIATIONS = {
    "Kohavi": "/kOhˈɑvi/",
    "A-B": "/ˈA bˈi/",
}

BEATS = {
    # 1 cold open: commit to a number (the textbook's thirty is the likely-wrong answer)
    "open": ("A hundred waits for a bus: mostly short, with a long tail." + S +
             "Textbooks say the average of thirty is safe to treat as a bell." + S +
             "For these waits, does it take thirty, three hundred, or over a thousand? [pause 1.5]"),
    # 2 stakes
    "stakes": ("A-B tests lean on that bell, and on revenue data, thirty is off by a factor "
               "of thousands."),
    # 3 naive build: look for the bell in the data itself
    "collect": ("First, look for the bell in the data itself." + S + "Collect a thousand, ten "
                "thousand, a hundred thousand." + S + "The bars get smoother, but the shape "
                "doesn't budge."),
    # 4 measured failure (skewness defined, term by term, with signed gaps)
    "fail": ("Measure the lean with skewness: the average cubed gap from the mean, left gaps "
             "counting negative, over the spread cubed." + S + "A perfect bell scores zero." + S +
             "These waits for a bus score about two at every sample size."),
    # 5 the fix: average (the dilution, slowly)
    "average": ("So average instead. [pause 0.5] Four bus waits: the one long wait gets "
                "diluted by three short ones. [pause 0.8] Drop that one number here." + S +
                "Do that ten thousand times."),
    "avg": ("These averages lean less: skewness one." + S + "Sixteen per average: point five." + S +
            "Sixty-four: point two five, nearly this perfect bell in green."),
    # 6 insight: the formula from the readings, then why it is root n (drawn as cubes)
    "formula": ("Each time the group grows four times, the skewness halves: two over root "
                "n, and two is the skewness of one wait."),
    "why": ("The root comes from the cubes." + S + "Add four waits: their cubed gaps add up, four "
            "times one wait's." + S + "But the spread only doubles, so its cube grows eight "
            "times." + S + "Four over eight: half the lean." + S + "In general, n over n to the "
            "one and a half."),
    # 7 universality, and why it is a bell (every other difference fades too)
    "coin": ("A coin that lands heads one time in ten is just two spikes, yet its averages "
             "make the same bell, by the same rule." + S + "Kurtosis, the extra tail weight, fades "
             "faster, as one over n, and every finer difference faster still." + S + "Only the "
             "bell survives." + S + "That's the central limit theorem." + S + "It needs "
             "independent pieces, and one more condition."),
    # 8 payoff: how many is enough, measured where tests live (95% interval misses)
    "thirty": ("Back to the textbook's thirty. [pause 0.5] Two over root thirty: point three "
               "seven." + S + "Close to a bell, by eye."),
    "tails": ("But tests live in the tails: a ninety-five percent interval should miss two and "
              "a half percent on each side." + S + "Tests estimate the spread from the same data, so "
              "a low average gets a small spread, and its interval stops short." + S +
              "With thirty waits: seven percent low, one percent high."),
    "kohavi": ("Ron Kohavi and colleagues, using Bing's data, want each side between two and "
               "three percent." + S + "Their rule: n at least three hundred fifty-five times the "
               "skewness squared. [pause 0.3] Divide by n and take the root: [pause 1.0] "
               "it's our formula: the average's skewness at most point oh five three." + S +
               "Three hundred still misses." + S + "For these waits: fourteen twenty, and both "
               "misses reach the band. [pause 1.2]"),
    "bing": ("Bing's revenue per user had a skewness near eighteen: a hundred and fourteen "
             "thousand users." + S + "Capping each user at ten dollars a week: under ten "
             "thousand."),
    # 9 the condition: the lighthouse
    "lighthouse": ("Now the condition." + S + "A lighthouse one mile off a straight shore flashes "
                   "at random angles, and each flash lands somewhere on the shore."),
    "runmean": ("Track the average landing spot." + S + "It never settles: a flash aimed almost "
                "along the shore lands absurdly far away, and yanks it."),
    "dilute": ("Among a thousand flashes, the farthest typically lands about nine hundred "
               "miles off." + S + "Divided by a thousand, it still drags the average about a "
               "mile." + S + "Half of single flashes land within a mile of the middle." + S +
               "Repeat the thousand-flash average two hundred times, and still only half do."),
    "variance": ("The theorem needs finite variance: no single piece can outweigh the rest." + S +
                 "Here the variance is infinite." + S + "The median ignores how far the extremes "
                 "fly, so it homes in."),
    # 10 landing: answer the opening question on the opening image
    "landing": ("So the answer is over a thousand, not thirty." + S + "And collect forever: this "
                "histogram stays lopsided." + S + "The bell was never in the data." + S + "It's in "
                "the average."),
}

# silence after each narrate block (s); about 0.9 s at story-beat boundaries
GAP_AFTER = {
    "open": 0.12, "stakes": 0.35, "collect": 0.2, "fail": 0.8, "average": 0.15, "avg": 0.2,
    "formula": 0.8, "why": 0.8, "coin": 0.8, "thirty": 0.2, "tails": 0.2, "kohavi": 0.05,
    "bing": 0.05, "lighthouse": 0.2, "runmean": 0.2, "dilute": 0.8, "variance": 0.05,
    "landing": 0.35,
}

if __name__ == "__main__":
    import sys
    sys.path.insert(0, "videos/toolkit")
    from sample_space.voice import synthesize
    total_w = total_t = 0
    for k, t in BEATS.items():
        s = synthesize(t, overrides=PRONUNCIATIONS, speed=SPEED)
        n = len(s.words)
        total_w += n
        total_t += s.duration + GAP_AFTER[k] + 0.12
        print(f"{k:10s} {s.duration:5.1f}s {n:3d}w {60 * n / s.duration:4.0f}wpm  cum {total_t:6.1f}")
    print(f"TOTAL {total_w} words, {total_t:.1f}s speech+gaps ({60 * total_w / total_t:.0f} wpm)")
