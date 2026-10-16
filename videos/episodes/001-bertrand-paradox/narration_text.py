"""Narration for episode 1, one entry per beat (kept separate so it can be timed offline)."""
LINES = {
    "open": "Draw a chord across this circle at random. What's the chance it comes out longer "
            "than a side of this triangle? Pick a number. [pause 1.5]",
    "stakes": "Joseph Bertrand published this puzzle in eighteen eighty-nine, as a warning about "
              "two words: at random. Leave them vague, and one college can report an average class "
              "of forty, or a hundred forty-seven.",
    "build1": "Start with the obvious simulation. Pick two points on the rim at random, and join "
              "them. If the chord beats the triangle's side, it turns gold.",
    "rain1": "Run ten thousand chords, and the gold share settles near point three three.",
    "arc": "Geometry agrees. Put a corner of the triangle on the first point. The chord is long "
           "only when the second point lands on this far arc, a third of the rim. [pause 1.2]",
    "build2": "Case closed, until you code it a second way. Pick a random radius, a random point "
              "along it, and draw the chord through that point at right angles.",
    "rain2": "This one settles near point five.",
    "build3": "A third program picks a random point anywhere inside, and makes it the chord's "
              "midpoint. That settles near point two five.",
    "gap": "Bertrand printed all three, and wrote that none is wrong, and none is right. Each "
           "tally is good to about one percentage point. They disagree by twenty-five percentage "
           "points, and none of the code has a bug.",
    "follow": "One point sets a chord's length: its midpoint. Slide it outward and the chord "
              "shrinks. It matches the triangle's side when the midpoint is half a radius out, on "
              "the circle that fits inside the triangle.",
    "inside": "So a chord is long exactly when its midpoint lands in this gold circle, and each "
              "program is just a way of scattering midpoints.",
    "area": "Shrink every chord to its midpoint. The midpoint program spreads them evenly, so this "
            "circle, with a quarter of the area, catches a quarter of them.",
    "radius": "The radius program spreads them evenly along the radius. Where will they crowd? "
              "[pause 1.3] Toward the center: every ring gets an equal share, and inner rings "
              "are small. Half the radius, so one half.",
    "rim": "And the endpoints program piles them against the rim, so only a third land inside, "
           "the third we found.",
    "which": "Three programs, three things spread evenly: rim, radius, area. At random never said "
             "which. [pause 0.8]",
    "jaynes": "Edwin Jaynes argued that a physical process picks one: straws "
              "tossed from a standing height can't be aimed, so the answer can't depend on where "
              "the circle sits or how big it is.",
    "test": "One rain lands on both circles at once, and each judges with its own gold circle, "
            "so a fair recipe must score the same on both. Midpoint gives a quarter, then point "
            "four one. [pause 0.8] Endpoints give a third, then point four seven. [pause 0.8] Only "
            "the radius program gives a half on both. [pause 0.6]",
    "tyler": "Jaynes and Charles Tyler tossed real broom straws at a five-inch circle, and the "
             "hundred and twenty-eight that crossed it matched the radius program's flat "
             "spread. [pause 0.8]",
    "classes": "Surveys hide the same two words. Take classes of ten, ten and a hundred. Pick a "
               "class at random, and the average size is forty. Pick a student at random, spread "
               "evenly over students instead of classes, and it's eighty-five. At Stony Brook in "
               "nineteen seventy-four, those two picks gave forty, and a hundred forty-seven. "
               "[pause 0.5]",
    "land": "So whatever number you picked, some way of drawing chords makes it right. Name the "
            "way, and only one is. Forty and a hundred forty-seven are both right, once you say "
            "who's picked.",
}
