"""Narration for episode 4, one string per beat (shared by scene.py and script.md checks).

Pauses: a sentence gap is 0.38 s by default; "[pause 0.12]" tightens a gap inside one thought,
and scene.py lengthens the gap after the beats that close a section (GAPS below)."""

PRONUNCIATIONS = {
    # /sɑnhˈuɹhO/ ("san-HOOR-ho"): whisper transcribes this as "Sanjurjo's" (round 5); the
    # earlier /sænhˈʊɹhO/ came back as "Sanjorjo's"
    "Sanjurjo": "/sɑnhˈuɹhO/",
    "Sanjurjo's": "/sɑnhˈuɹhOz/",
}

BEATS = {
    # cold open
    # round 7: 0.3 s breaths after the two clauses of the rule (substance fix 9)
    "open": "Flip a fair coin four times. [pause 0.12] After each heads, check the next flip: "
            "[pause 0.3] here, one of the two is heads. [pause 0.3] Do this for every four flip "
            "run, and average. Below, at, or above one half? [pause 1.6]",
    # stakes
    "stakes": "One half feels obvious, since a coin has no memory. In nineteen eighty five, a "
              "study ran this kind of check on basketball shots, and called the hot hand "
              "an illusion.",
    # naive build: the streak test
    "test": "Heads are hits. [pause 0.12] A hot shooter beats their usual rate; a random one "
            "should match it.",
    "calibrate": "First, test the test on a shooter we know is random: a fair coin. "
                 "[pause 0.12] Four flips can land sixteen ways, all equally likely.",
    # fail
    # round 7: "Score every row the same way." cut; the cascade runs in the pause
    "score": "This row checks three flips, and two are heads. [pause 1.0]",
    "undefined": "Two rows show no heads before the last flip, so they get no score.",
    "average": "Drop the other fourteen scores onto the line. Their average is seventeen out of "
               "forty two.",
    "cold": "On a fair coin, the test reads cold, by nine and a half points.",
    # insight
    "pool": "Yet no flip is biased. [pause 0.5] Gather all twenty four checked flips: twelve heads, twelve "
            "tails. Total heads over total flips: exactly half.",
    # round 8: "The skew comes from scoring row by row:" cut (the formula line names the cause)
    "votes": "But each row gets one vote, however many flips it checked.",
    "crowds": "Checked heads come in crowds, since a heads gets the next flip checked too. "
              "Here, three heads share a single vote, while this lone tails gets a whole one.",
    # round 6: three clips (craft 9: the densest run was heard as one run-on sentence);
    # round 8: "Crowded heads split their votes." cut (it restated "three heads share a single vote")
    "lineup": "Twelve heads crowd into eight rows. [pause 0.3] Twelve tails spread across eleven.",
    # round 7: breaths after "Line them up:" and after the vote count (both critics)
    "pack": "Line them up: [pause 0.8] the heads hold five and two thirds of the fourteen "
            "votes. [pause 1.0] That's seventeen out of forty two.",
    "formula": "So the test takes an average of ratios, one per row, [pause 0.3] instead of the "
               "ratio of totals. [pause 0.5]",
    # the mirror: after tails
    "mirror": "Now score the flip after each tails. Swap heads and tails, and the strip flips "
              "over one half: the test reads high, twenty five out of forty two.",
    # round 7: "a fair coin shows" cut (the coin is the only subject on screen)
    "gap": "Subtract the averages: a gap of minus nineteen points.",
    # payoff
    "cornell": "The nineteen eighty five study ran the same comparison on twenty six Cornell "
               "players: up to a hundred shots each, from where they'd hit about half. After "
               "three hits, versus after three misses.",
    "minus8": "For a random shooter, the same crowding pulls after hits down to forty six percent "
              "on average, and after misses up to fifty four. [pause 0.45] Miller and Sanjurjo's "
              "twenty eighteen paper [pause 0.5] puts the gap at about minus eight points. "
              "[pause 0.9] Longer records shrink it; [pause 0.9] longer streaks grow it. [pause 0.5]",
    # "The Cornell players": a beat-initial "Cornell's" was heard as "Daniel's" (round 6 v2)
    # round 8: breaths after the two readings and after "plus four" (substance fix 5)
    "observed": "The Cornell players hit forty nine percent after three hits, and forty five "
                "after three misses. [pause 0.6] The study found plus four, [pause 0.4] too close "
                "to zero to count, so no hot hand.",
    "hot": "Measured from minus eight, it's twelve points hot. [pause 0.9] That's evidence for a "
           "hot hand in a gym, not proof it survives defenders in a game.",
    # landing
    "landing": "One half [pause 0.15] is what a fair coin does. [pause 0.8] Seventeen out of forty two is "
               "what this test sees. A fifty percent shooter [pause 0.3] who averages one half on "
               "this test [pause 0.2] is already running hot.",
}

# voice speed per beat (default: the scene's SPEED). Round 6: the short, plain sentences of
# these beats came out above 200 wpm at the series speed; the closing lines get a slower read.
SPEEDS = {"undefined": 0.80, "cold": 0.80, "crowds": 0.80, "mirror": 0.80, "observed": 0.80,
          "landing": 0.80}

# breathing room after a beat (s); default NarratedScene.BEAT_GAP = 0.35
# (round 6: CADENCE = "shaped", whose default beat gap is 0.45 s; 0.9-1.0 s after the key results)
# round 7: "split" 0.9 (a breath after "split their votes"), "pack" 1.3 (17/42 held >= 3.2 s)
GAPS = {"stakes": 0.6, "cold": 0.9, "crowds": 0.6, "lineup": 0.6, "pack": 1.3,
        "formula": 1.0, "gap": 0.8, "observed": 0.8, "hot": 0.3}
