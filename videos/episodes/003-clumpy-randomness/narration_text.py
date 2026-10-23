"""Narration beats for episode 3 (imported by scene.py; also used for timing checks).

Round 5 (second pass): cut to the PRODUCTION_GUIDE section 13 budget (<= 500 words, <= 3:35),
spoken at 0.84 with shaped cadence (gaps follow the sense; 0.9-1.4 s holds after the key
results), no deictic without an animation on it.
Round 6: "force pile-ups ... a hundred eighty-three hits" (only the extra hits are forced),
"Call that P of zero", "London's clusters were no sign of precise aim" (the stakes answered),
breaths in the gaps, two-hit and limits beats; paid for by cutting "Both are simulated. The
question isn't." and "So look again.".
Round 7: no spoken 354 (on screen 537 - (576 - 222)); "To judge London, chance must predict every
bar" cut; "because short bars wobble less" (the whiskers); the limit is measured - the north box
scored alone fits chance too (p = 0.45), so the aim shows only in lambda.
Round 8: the guess comes before the computation ("Almost one hit per square. Guess how many
squares stay empty."), the answer is set against it ("four squares in ten"); the stakes are two
sentences (clusters -> aim -> factories); "Five thirty-six is almost five thirty-seven" is cut (the
screen does it in the gap after the two-hit beat); "Map A scores two point oh" is its own beat
at 0.80 with no internal pause; "Aimed bombs would break the fit the other way"; a 0.9 s hold
between the landing's two sentences."""

PRON = {"Poisson": "/pwɑsˈOn/", "A": "/ˈA/"}   # map name A, never the article
SPEED = 0.84
CADENCE = "shaped"
# the closing line a touch slower; the one-line score at 0.80 (at 0.84 it ran 208 wpm)
BEAT_SPEED: dict[str, float] = {"landing": 0.82, "score": 0.80}
# breathing room after the beats that end where the story turns (into the insight, into the
# honest detector, into aim and the real data): longer than a full stop, so the turns are heard
# ("two": the 536 -> 537 step runs in this gap, on screen only)
BEAT_GAP_AFTER: dict[str, float] = {"reveal": 0.55, "two": 0.9, "poisson": 0.55, "fixb": 0.55,
                                    # the score is one sentence of the honest-detector beat:
                                    # sentence-length gaps around it
                                    "fix": 0.35, "score": 0.3,
                                    # the landing transform (Clarke's area squares up) runs here
                                    "limit": 0.9}

# Numbers are written without "and" ("five hundred seventy-six"): Kokoro stretched the "and"
# inside "five hundred and seventy-six" to 0.8 s, and whisper heard two numbers.
B = dict(
    cold="Each map holds five hundred thirty-seven bomb hits. One is pure chance; the other "
         "follows a rule. Which is chance? [pause 1.2]",
    stakes="In nineteen forty-four, Londoners saw flying bombs land in clusters. If that meant "
           "precise aim, factories were at risk.",
    build="Build the detector your eye is running. Cut each map into five hundred "
          "seventy-six squares, and flag any square with three or more hits, like this one.",
    flags="Map A lights up with thirty-nine targets, map B with none. So A looks aimed.",
    reveal="Backwards. [pause 0.6] I dropped every hit on map A at random, so all thirty-nine "
           "targets are false alarms. Map B's rule: no two hits closer than four fifths of a "
           "square. Your eye, like the detector, expects chance to look that even.",
    guess="Almost one hit per square. Guess how many squares stay empty. [pause 1.1]",
    square="Each bomb has a one in five seventy-six chance of landing in this square. "
           "To stay empty, all five hundred thirty-seven must miss. [pause 0.4]",
    empty="About two hundred twenty-seven: four squares in ten. [pause 0.3] Map A has two "
          "hundred twenty-two. [pause 0.3]",
    gaps="Those empty squares force pile-ups: [pause 0.3] a hundred eighty-three hits must land "
         "where another already did. [pause 0.5]",
    lam="Let's call the average hits per square lambda. [pause 0.5] One minus a small slice, raised "
        "to a big power, is e to the minus lambda, almost exactly. Call that P of zero.",
    two="For two hits in this square, pick two bombs: five thirty-seven times five thirty-six "
        "ways, over two, since each pair counts twice. [pause 0.6] Each has that same chance, "
        "and the rest miss: e to the minus lambda again.",
    poisson="For three hits, each two becomes a three; for any k, a k. [pause 0.5] The powers "
            "merge into lambda to the k: the Poisson distribution. [pause 0.5] Times five seventy-six squares, it "
            "predicts these purple bars.",
    fix="The honest detector compares whole histograms. [pause 0.4] Thirty-nine targets, and "
        "chance predicts thirty-nine. [pause 0.4] The chi-squared misfit squares each bar's gap "
        "and divides by chance's bar, because short bars wobble less: a miss on a short bar "
        "counts more.",
    score="Map A scores two point oh. [pause 0.6]",
    null="Three out of four simulated chance maps score worse. That share, p, is point seven "
         "four. [pause 0.7]",
    fixb="Now map B: half the expected empty squares, a tower of single hits, misfit two hundred "
         "seventy-two. [pause 0.3] A pattern this even is the fingerprint of a spacing rule.",
    clarke="Aimed bombs would break the fit the other way: extra empty squares, extra pile-ups. "
           "[pause 0.4] "
           "In nineteen forty-six, R D Clarke published the same test on London's real hits: "
           "five thirty-seven in five seventy-six squares.",
    london="Chance predicted two hundred twenty-seven empty squares; Clarke counted two "
           "hundred twenty-nine. [pause 0.3] Overall, p equals point eight eight. [pause 0.5] "
           "London's clusters were no sign of precise aim.",
    limit="The bombs were aimed at central London but tended to fall short, so farther north, "
          "hits were about half as dense. [pause 0.6] Score the north alone, and it fits chance "
          "too: p equals point four five. [pause 0.3] The aim hides in lambda, which the test "
          "holds fixed.",
    landing="The clumps in map A [pause 0.4] are what no aim at all looks like. [pause 0.9] If "
            "you chose map B, [pause 0.3] you chose the rule.",
)
ORDER = ["cold", "stakes", "build", "flags", "reveal", "guess", "square", "empty", "gaps", "lam",
         "two", "poisson", "fix", "score", "null", "fixb", "clarke", "london", "limit", "landing"]
