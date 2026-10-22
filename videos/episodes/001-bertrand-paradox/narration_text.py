"""Narration for episode 1, one entry per beat (kept separate so it can be timed offline).

Round 6 (continued): cut from 568 to under 500 words for the PRODUCTION_GUIDE §13 budget
(<= 500 words, 3:15-3:35), spoken with CADENCE = "shaped".  Every cut is a restatement or a
phrase the frame already shows; no beat and no on-screen step was removed.  Round 6 (final
pass): "accurate to about one point" became "good to about one percentage point" (500 words), so
the tally's unit is spoken and "point" no longer echoes into "One point sets a chord's length".
Round 7: "[pause 0.8]" after "the code has no bug" (the biggest turn gets a breath); "One program's
rain" (the rain is a program's lines, not the straws); "[pause 0.6]" after "the same on both";
"none is wrong, none is right" (the French quote's own shape, -1 word); landing "a half for
unaimed straws" (Jaynes's condition is spoken, and Whisper no longer hears "toss straws").
500 words."""
LINES = {
    "open": "Draw a chord across this circle, at random. What's the chance it's longer than a side "
            "of this triangle? Pick a number. [pause 1.5]",
    "stakes": "Bertrand posed this puzzle in eighteen eighty-nine, as a warning about two words: "
              "at random. Leave them vague, and one college's average class is forty, or a hundred "
              "forty-seven.",
    "build1": "Start with the obvious simulation: two random points on the rim, joined. If the "
              "chord beats the triangle's side, it turns gold.",
    "rain1": "Ten thousand chords in, the gold share settles near point three three.",
    "arc": "Geometry agrees. With a corner on the first point, the chord is long only when its "
           "other end lands on this arc, a third of the rim. [pause 1.0]",
    "build2": "Case closed, until you code it a second way: a random radius, a point on it, and "
              "the chord through it at right angles.",
    "rain2": "This one settles near point five.",
    "build3": "A third program picks any point inside as the chord's midpoint. That settles near "
              "point two five.",
    "gap": "Bertrand printed all three, writing that none is wrong, none is right. Each tally "
           "is good to about one percentage point. They disagree by twenty-five, and the code has "
           "no bug. [pause 0.8]",
    "follow": "One point sets a chord's length: its midpoint. Slide it outward and the chord "
              "shrinks. It matches the side at half a radius, on the circle inside the triangle.",
    "inside": "So a chord is long exactly when its midpoint lands in this gold circle. Each "
              "program is a way of scattering midpoints.",
    "area": "Shrink every chord to its midpoint. The midpoint program fills the disk evenly, so "
            "this circle, a quarter of the area, catches a quarter.",
    "radius": "The radius program spreads them evenly along the radius. Where will they crowd? "
              "[pause 1.5] Toward the center: every ring gets an equal share, and inner rings "
              "are small. Half the radius: one half.",
    "rim": "The endpoints program piles them against the rim: only a third land inside, the "
           "third we found.",
    "which": "Three programs, three things spread evenly: rim, radius, area. At random never said "
             "which. [pause 0.9]",
    "jaynes": "Edwin Jaynes argued a physical process picks one. Straws tossed from a standing "
              "height can't be aimed, so the answer can't depend on where the circle sits, or its size.",
    "test": "One program's rain lands on both circles. Each judges with its own gold circle, so "
            "a fair program scores the same on both. [pause 0.6] Midpoint: a quarter, then point four one. "
            "[pause 1.0] Endpoints: a third, then point four seven. [pause 1.0] Only the "
            "radius program gives a half on both. [pause 0.9]",
    "tyler": "Jaynes and Charles Tyler tossed real straws at a five-inch circle. The hundred "
             "twenty-eight that crossed it matched the radius program. [pause 0.9]",
    "classes": "Surveys hide the same two words. Take classes of ten, ten and a hundred. Pick a "
               "class at random: the average is forty. Pick a student instead, and it's "
               "eighty-five. At Stony Brook, the same two picks gave forty and a hundred "
               "forty-seven. [pause 0.5]",
    "land": "Whatever number you picked, some way of drawing chords makes it right. Name the way, "
            "and the answer is fixed: a half for unaimed straws, a hundred forty-seven for a "
            "random student.",
}
