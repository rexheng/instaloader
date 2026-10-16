"""Narration for episode 4, one string per beat (shared by scene.py and script.md checks).

Pauses: a sentence gap is 0.38 s by default; "[pause 0.12]" tightens a gap inside one thought,
and scene.py lengthens the gap after the beats that close a section (GAPS below)."""

PRONUNCIATIONS = {
    "Sanjurjo": "/sænhˈʊɹhO/",
    "Sanjurjo's": "/sænhˈʊɹhOz/",
}

BEATS = {
    # cold open
    "open": "Flip a fair coin four times. [pause 0.12] After each heads, check the next flip: "
            "here, one of the two is heads. [pause 0.12] Do it for all sixteen sequences and "
            "average the shares. What do you get? [pause 1.6]",
    # stakes
    "stakes": "One half feels obvious, since a coin has no memory. In nineteen eighty five, a "
              "famous study ran this same check on basketball shots, and called the hot hand "
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
            "tails. [pause 0.12] Exactly half.",
    "votes": "The skew comes from scoring row by row, because each row gets one vote, however "
             "many flips it checked.",
    "crowds": "And checked heads come in crowds, since a heads gets the next flip checked too. "
              "This row's three heads share a single vote, while this lone tails gets a whole "
              "one.",
    "lineup": "Twelve heads crowd into eight rows. Twelve tails spread across eleven. [pause 0.55] "
              "Line up the votes, and heads hold seventeen out of forty two.",
    "formula": "That's one vote per row. [pause 0.3] Count all the flips together first, and "
               "you get one half.",
    # the mirror: after tails
    "mirror": "Tails crowd the same way. Swap heads and tails, and the strip flips over one half. "
              "So after a tails, the test reads hot: twenty five out of forty two.",
    "gap": "Subtract the two averages, and a fair coin shows a gap of minus nineteen points.",
    # payoff
    "cornell": "The nineteen eighty five study ran the same comparison on twenty six Cornell "
               "players: up to a hundred shots each, from where they'd hit about half. After "
               "three hits, versus after three misses.",
    "minus8": "For a random shooter, the same crowding pulls those to forty six and fifty four "
              "percent. [pause 0.12] Miller and Sanjurjo's twenty eighteen paper puts the gap at "
              "about minus eight points. [pause 0.6] Longer streaks grow the bias. [pause 0.9] Longer "
              "records shrink it, [pause 0.5] but a hundred shots isn't long.",
    "observed": "Cornell's players hit forty nine percent after three hits, and forty five after "
                "three misses. The study took that plus four to mean no hot hand.",
    "hot": "Measured from minus eight, it's twelve points hot. [pause 0.6] That's evidence for a "
           "hot hand in a gym, not proof it survives defenders in a game.",
    # landing
    "landing": "One half is what a fair coin does. [pause 0.12] Seventeen out of forty two is "
               "what this test sees. A fifty percent shooter [pause 0.3] who averages one half on "
               "this test [pause 0.2] is already running hot.",
}

# breathing room after a beat (s); default NarratedScene.BEAT_GAP = 0.35
GAPS = {"stakes": 0.6, "cold": 0.8, "crowds": 0.6, "formula": 0.9, "gap": 0.7, "hot": 0.3}
