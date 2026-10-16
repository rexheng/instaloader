"""Narration beats for episode 3 (imported by scene.py; also used for timing checks)."""

PRON = {"Poisson": "/pwɑsˈOn/", "A": "/ˈA/"}   # map name A, never the article
SPEED = 0.86
# slower delivery for the densest number beats and the closing line
BEAT_SPEED = {"gaps": 0.83, "lam": 0.83, "two": 0.83, "poisson": 0.80, "landing": 0.78}

B = dict(
    cold="Each map holds five hundred and thirty-seven hits. On one, every hit landed by pure "
         "chance. The other follows a rule. Which one is chance? [pause 1.5]",
    stakes="Both are simulated, but the question is real. In nineteen forty-four, Londoners "
           "claimed German flying bombs fell in clusters, and precise aim would put factories "
           "at risk.",
    build="Build the detector your eye is running. Cut each map into five hundred and "
          "seventy-six squares, count the hits, and flag any square with three or more, like "
          "this one.",
    flags="Map A lights up with thirty-nine targets. Map B gets none. So A looks aimed, and B "
          "looks like chance.",
    reveal="Backwards. [pause 0.9] I dropped every hit on map A at random, so all thirty-nine "
           "targets are false alarms. Map B's rule: no two hits closer than four fifths of a "
           "square. The detector, like your eye, expected chance to spread out that evenly.",
    square="Take one square. Each bomb has a one in five hundred and seventy-six chance of "
           "landing in it. To stay empty, all five hundred and thirty-seven must miss.",
    guess="Guess how many squares get no hit at all. [pause 1.5]",
    empty="About two hundred and twenty-seven squares stay empty. Map A has two hundred and "
          "twenty-two. [pause 0.6]",
    gaps="Those gaps force the clumps: the other three hundred and fifty-four squares share "
         "all the hits, one and a half each, so plenty must double up.",
    lam="Call the average hits per square lambda. [pause 0.5] One minus a small slice, raised "
        "to a big power, is almost exactly e to the minus lambda. [pause 0.7]",
    two="For two hits, pick which two bombs land here: five thirty-seven times five "
        "thirty-six, over two, ways. [pause 0.6] Each lands with chance one in five seventy-six, "
        "and the rest miss: e to the minus lambda again. [pause 0.6]",
    poisson="Five thirty-six is almost five thirty-seven, so for any k, each two becomes a "
            "k. The powers merge into "
            "lambda to the k: the Poisson distribution. [pause 0.7] Times five hundred and "
            "seventy-six squares, it predicts these purple bars.",
    fix="The honest detector compares whole histograms. Map A sits on the purple bars: "
        "thirty-nine targets, and chance predicts thirty-nine. The chi-squared misfit: square "
        "each bar's gap, divide by chance's bar, and add them up. Map A scores two point oh. "
        "Pure-chance maps score worse three times in four: p equals point seven four.",
    fixb="Map B: half the expected empty squares, a tower of single hits, and a misfit of two "
         "hundred and seventy-two. A pattern this even is the fingerprint of a spacing rule.",
    clarke="Aimed bombs would miss the other way: extra empty squares, extra pile-ups. In "
           "nineteen forty-six, the actuary R D Clarke published this test on real flying-bomb "
           "hits: five hundred and thirty-seven, in five seventy-six squares of south London.",
    london="Chance predicted two hundred and twenty-seven empty squares; Clarke counted two "
           "hundred and twenty-nine. [pause 0.2] Single hits: two hundred and eleven, exactly as "
           "predicted. [pause 0.2] Same test: p equals point eight eight. [pause 0.2] No "
           "sign of clustering.",
    limit="That doesn't mean the bombs were unaimed: they were aimed at London, just too "
          "loosely to choose a street. And the test needs one lambda everywhere: farther north, "
          "hits fell about half as densely, so Clarke chose an area where lambda held "
          "steady.",
    landing="So look again. [pause 0.9] The clumps in map A are what no aim at all looks like. "
            "If you picked map B, you picked the one following a rule.",
)
ORDER = ["cold", "stakes", "build", "flags", "reveal", "square", "guess", "empty", "gaps", "lam",
         "two", "poisson", "fix", "fixb", "clarke", "london", "limit", "landing"]
