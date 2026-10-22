"""Narration beats for episode 3 (imported by scene.py; also used for timing checks)."""

PRON = {"Poisson": "/pwɑsˈOn/", "A": "/ˈA/"}   # map name A, never the article
SPEED = 0.86
# slower delivery for the densest number beats and the closing line
BEAT_SPEED = {"gaps": 0.83, "lam": 0.83, "two": 0.83, "poisson": 0.80, "landing": 0.78}

# Numbers are written without "and" ("five hundred seventy-six"): Kokoro stretched the "and"
# inside "five hundred and seventy-six" to 0.8 s, and whisper heard two numbers.
B = dict(
    cold="Each map holds five hundred thirty-seven bomb hits. On one, every hit landed by "
         "pure chance. The other follows a rule. Which one is chance? [pause 1.5]",
    stakes="Both are simulated. The question isn't. In nineteen forty-four, Londoners "
           "claimed German flying bombs fell in clusters, and precise aim would put factories "
           "at risk.",
    build="Build the detector your eye is running. Cut each map into five hundred "
          "seventy-six squares, count the hits, and flag any square with three or more, like "
          "this one.",
    flags="Map A lights up with thirty-nine targets. Map B gets none. So A looks aimed.",
    reveal="Backwards. [pause 0.9] I dropped every hit on map A at random, so all thirty-nine "
           "targets are false alarms. Map B's rule: no two hits closer than four fifths of a "
           "square. The detector, like your eye, expected chance to spread out that evenly.",
    square="Take one square. Each bomb has a one in five hundred seventy-six chance of "
           "landing in it. To stay empty, all five hundred thirty-seven must miss.",
    guess="Guess how many squares get no hit at all. [pause 1.5]",
    empty="About two hundred twenty-seven squares stay empty. Map A has two hundred "
          "twenty-two.",
    gaps="Those empty squares force the clumps: the other three hundred fifty-four squares "
         "share all the hits, one and a half each, so plenty must double up. To judge "
         "London, chance must predict every bar.",
    lam="Call the average hits per square lambda. [pause 0.5] One minus a small slice, raised "
        "to a big power, is almost exactly e to the minus lambda. [pause 0.5]",
    two="For two hits, pick which two bombs land here: five thirty-seven times five "
        "thirty-six ways, over two, since order doesn't matter. [pause 0.4] Each lands with "
        "chance one in five seventy-six, and the rest miss: e to the minus lambda again. "
        "[pause 0.4]",
    # "k." reads as an abbreviation to the sentence splitter, so the pause is explicit
    poisson="Five thirty-six is almost five thirty-seven. [pause 0.4] For three hits, each two "
            "becomes a three; for any k, a k. [pause 0.6] The powers merge into lambda to the "
            "k: the Poisson distribution. [pause 0.7] Times five hundred seventy-six squares, "
            "it predicts these purple bars.",
    fix="The honest detector compares whole histograms. [pause 0.8] Thirty-nine targets, and "
        "chance predicts thirty-nine. The chi-squared misfit: square each bar's gap and divide "
        "by chance's bar, so a miss of two on seven outweighs a miss of five on two hundred "
        "twenty-seven. Add them up: map A scores two point oh. Three in four simulated chance "
        "maps score worse. [pause 0.3] That share, p, is point seven four.",
    fixb="Map B: half the expected empty squares, a tower of single hits, and a misfit of two "
         "hundred seventy-two. A pattern this even is the fingerprint of a spacing rule.",
    clarke="Aimed bombs would miss the other way: extra empty squares, extra pile-ups. In "
           "nineteen forty-six, the actuary R D Clarke published this test on real flying-bomb "
           "hits: five hundred thirty-seven, in five hundred seventy-six squares of London.",
    london="Chance predicted two hundred twenty-seven empty squares; Clarke counted two "
           "hundred twenty-nine. [pause 0.2] Single hits: two hundred eleven, exactly as "
           "predicted. [pause 0.2] Same test: p equals point eight eight.",
    limit="The bombs were aimed, at Tower Bridge, but half fell outside this circle, "
          "more than twelve kilometres away. And the test needs one lambda everywhere: "
          "farther north, hits were about half as dense, so Clarke chose an area where lambda "
          "held steady.",
    landing="So look again. [pause 1.2] The clumps in map A are what no aim at all looks like. "
            "If you chose map B, you chose the one following a rule.",
)
ORDER = ["cold", "stakes", "build", "flags", "reveal", "square", "guess", "empty", "gaps", "lam",
         "two", "poisson", "fix", "fixb", "clarke", "london", "limit", "landing"]
