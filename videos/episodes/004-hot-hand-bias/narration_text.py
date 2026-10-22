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
    "open": "Flip a fair coin four times. [pause 0.12] After each heads, check the next flip: "
            "here, one of the two is heads. [pause 0.12] Do this for every four flip run, and "
            "average. Below, at, or above one half? [pause 1.6]",
    # stakes
    "stakes": "One half feels obvious, since a coin has no memory. In nineteen eighty five, a "
              "famous study ran this kind of check on basketball shots, and called the hot hand "
              "an illusion.",
    # naive build: the streak test
    "test": "Heads are hits. [pause 0.12] A hot shooter beats their usual rate; a random one "
            "should match it.",
    "calibrate": "So first, test the test on a shooter we know is random: a fair coin. "
                 "[pause 0.12] Four flips can land sixteen ways, all equally likely.",
    # fail
    "score": "This row checks three flips, and two of them are heads. [pause 0.6] Score every row "
             "the same way.",
    "undefined": "Two rows never show a heads before the last flip, so they get no score.",
    "average": "Drop the other fourteen scores onto the line. Their average is seventeen out of "
               "forty two: about forty point five percent.",
    "cold": "On a perfectly fair coin, the test reads cold, by nine and a half points.",
    # insight
    "pool": "Yet no flip is biased. [pause 0.6] Gather all twenty four checked flips: twelve heads, twelve "
            "tails. Total heads over total flips: exactly half.",
    "votes": "The skew comes from scoring row by row, because each row gets one vote, however "
             "many flips it checked.",
    "crowds": "And checked heads come in crowds, since a heads gets the next flip checked too. "
              "This row's three heads share a single vote, while this lone tails gets a whole "
              "one.",
    # round 6: three clips (craft 9: the densest run was heard as one run-on sentence)
    "lineup": "Twelve heads crowd into eight rows. [pause 0.3] Twelve tails spread across eleven.",
    "split": "Crowded heads split their votes.",
    "pack": "Line them up, and the heads hold five and two thirds of the fourteen votes. "
            "[pause 0.5] That's seventeen out of forty two.",
    "formula": "So the test takes an average of ratios, one per row, [pause 0.3] instead of the "
               "ratio of totals. [pause 0.5]",
    # the mirror: after tails
    "mirror": "Now score the flip after each tails. Swap heads and tails, and the strip flips "
              "over one half: after a tails, the test reads high, twenty five out of forty two.",
    "gap": "Subtract the two averages, and a fair coin shows a gap of minus nineteen points.",
    # payoff
    "cornell": "The nineteen eighty five study ran the same comparison on twenty six Cornell "
               "players: up to a hundred shots each, from where they'd hit about half. After "
               "three hits, versus after three misses.",
    "minus8": "For a random shooter, the same crowding pulls after hits down to forty six percent "
              "on average, and after misses up to fifty four. [pause 0.12] Miller and Sanjurjo's "
              "twenty eighteen paper puts the gap at about minus eight points. [pause 0.8] Longer "
              "streaks grow the bias. [pause 0.9] Longer records shrink it, [pause 0.5] but a "
              "hundred shots isn't long.",
    "observed": "Cornell's players hit forty nine percent after three hits, and forty five after "
                "three misses. The study took that plus four to mean no hot hand.",
    "hot": "Measured from minus eight, it's twelve points hot. [pause 0.6] That's evidence for a "
           "hot hand in a gym, not proof it survives defenders in a game.",
    # landing
    "landing": "One half is what a fair coin does. [pause 0.5] Seventeen out of forty two is "
               "what this test sees. A fifty percent shooter [pause 0.3] who averages one half on "
               "this test [pause 0.2] is already running hot.",
}

# breathing room after a beat (s); default NarratedScene.BEAT_GAP = 0.35
GAPS = {"stakes": 0.6, "cold": 0.8, "crowds": 0.6, "lineup": 0.5, "split": 0.5, "pack": 0.65,
        "formula": 1.0, "gap": 0.7, "observed": 0.8, "hot": 0.3}
