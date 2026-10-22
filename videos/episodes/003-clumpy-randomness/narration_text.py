"""Narration beats for episode 3 (imported by scene.py; also used for timing checks).

Round 5 (second pass): cut to the PRODUCTION_GUIDE section 13 budget (<= 500 words, <= 3:35),
spoken at 0.84 with shaped cadence (gaps follow the sense; 0.9-1.4 s holds after the key
results), no deictic without an animation on it.
Round 6: "force pile-ups ... a hundred eighty-three hits" (only the extra hits are forced),
"Call that P of zero", "London's clusters were no sign of precise aim" (the stakes answered),
breaths in the gaps, two-hit and limits beats; paid for by cutting "Both are simulated. The
question isn't." and "So look again."."""

PRON = {"Poisson": "/pwɑsˈOn/", "A": "/ˈA/"}   # map name A, never the article
SPEED = 0.84
CADENCE = "shaped"
BEAT_SPEED: dict[str, float] = {"landing": 0.82}   # the closing line, a touch slower
# breathing room after the beats that end where the story turns (into the insight, into the
# honest detector, into aim and the real data): longer than a full stop, so the turns are heard
BEAT_GAP_AFTER: dict[str, float] = {"reveal": 0.55, "two": 0.8, "poisson": 0.55, "fixb": 0.55,
                                    # the landing transform (Clarke's area squares up) runs here
                                    "limit": 0.9}

# Numbers are written without "and" ("five hundred seventy-six"): Kokoro stretched the "and"
# inside "five hundred and seventy-six" to 0.8 s, and whisper heard two numbers.
B = dict(
    cold="Each map holds five hundred thirty-seven bomb hits. One is pure chance; the other "
         "follows a rule. Which is chance? [pause 1.2]",
    stakes="In nineteen forty-four, Londoners claimed flying bombs fell in clusters, and "
           "precise aim would put factories at risk.",
    build="Build the detector your eye is running. Cut each map into five hundred "
          "seventy-six squares, and flag any square with three or more hits, like this one.",
    flags="Map A lights up with thirty-nine targets, map B with none. So A looks aimed.",
    reveal="Backwards. [pause 0.6] I dropped every hit on map A at random, so all thirty-nine "
           "targets are false alarms. Map B's rule: no two hits closer than four fifths of a "
           "square. Your eye, like the detector, expects chance to look that even.",
    square="Each bomb has a one in five seventy-six chance of landing in this square. "
           "To stay empty, all five hundred thirty-seven must miss.",
    guess="Guess how many squares stay empty. [pause 1.1]",
    empty="About two hundred twenty-seven. [pause 0.3] Map A has two hundred twenty-two. "
          "[pause 0.5]",
    gaps="Those empty squares force pile-ups: [pause 0.3] the other three hundred fifty-four share all "
         "the hits, so a hundred eighty-three must land where another already did. To judge "
         "London, chance must predict every bar.",
    lam="Let's call the average hits per square lambda. [pause 0.5] One minus a small slice, raised "
        "to a big power, is e to the minus lambda, almost exactly. Call that P of zero.",
    two="For two hits in this square, pick two bombs: five thirty-seven times five thirty-six "
        "ways, over two, since each pair counts twice. [pause 0.8] Each has that same chance, "
        "and the rest miss: e to the minus lambda again.",
    poisson="Five thirty-six is almost five thirty-seven. [pause 0.3] For three hits, each two "
            "becomes a three; for any k, a k. [pause 0.5] The powers merge into lambda to the "
            "k: the Poisson distribution. [pause 0.5] Times five seventy-six squares, it "
            "predicts these purple bars.",
    fix="The honest detector compares whole histograms. [pause 0.4] Thirty-nine targets, and "
        "chance predicts thirty-nine. [pause 0.4] The chi-squared misfit squares each bar's gap "
        "and divides by chance's bar, so a miss on a short bar counts more. Map A scores [pause 0.2] two "
        "point oh. Three out of four simulated chance maps score worse. That share, p, "
        "is point seven four. [pause 0.7]",
    fixb="Now map B: half the expected empty squares, a tower of single hits, misfit two hundred "
         "seventy-two. [pause 0.3] A pattern this even is the fingerprint of a spacing rule.",
    clarke="Aimed bombs would miss the other way: extra empty squares, extra pile-ups. [pause 0.4] "
           "In nineteen forty-six, R D Clarke published the same test on London's real hits: "
           "five thirty-seven in five seventy-six squares.",
    london="Chance predicted two hundred twenty-seven empty squares; Clarke counted two "
           "hundred twenty-nine. [pause 0.3] Overall, p equals point eight eight. [pause 0.5] "
           "London's clusters were no sign of precise aim.",
    limit="The bombs were aimed at central London but tended to fall short, so farther north, "
          "hits were about half as dense. [pause 0.6] The test needs one lambda: Clarke chose an area "
          "where it held steady.",
    landing="The clumps in map A [pause 0.4] are what no aim at all looks like. If you chose "
            "map B, [pause 0.3] you chose the rule.",
)
ORDER = ["cold", "stakes", "build", "flags", "reveal", "square", "guess", "empty", "gaps", "lam",
         "two", "poisson", "fix", "fixb", "clarke", "london", "limit", "landing"]
