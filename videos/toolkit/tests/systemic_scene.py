"""Render-level check of the round-5/6 systemic fixes (PRODUCTION_GUIDE §13):
CADENCE = "shaped", swap(), carry(), beat.on(), the glyph-morph lint, the deictic-sync check,
the text-size audit and the concision budget block in narration.json.

    videos/toolkit/render.sh --preview videos/toolkit/tests/systemic_scene.py Systemic \
        /tmp/systemic/out.mp4
    python3 -c "import json; d=json.load(open('/tmp/systemic/narration.json')); \
        print(d['glyph_morphs'], d['deictic_sync'], d['layout_audit']['counts'], d['budget'])"

Expected: 1 glyph morph (the deliberate Transform at "Now"), 1 unlanded deictic ("this
number", nothing animates on it), 1 text-size issue (the 15 px note), shaped gaps
(question and result sentences followed by longer gaps), no overlap.
"""
from manim import *
from sample_space import *


class Systemic(NarratedScene):
    EPISODE = 0
    TITLE = "Systemic checks"
    CADENCE = "shaped"

    def construct(self):
        cell = formula(r"0.99", size=EQ, color=YELLOW).move_to(LEFT * 3 + UP * 1.5)
        term = formula(r"P(+\mid \text{sick})", size=EQ, color=YELLOW).move_to(RIGHT * 2.5 + UP * 1.5)
        cite_a = citation("Manrai et al., 2014 · JAMA Intern. Med.")
        cite_b = citation("Davies et al., 2018 · Cardiff University")
        with self.narrate("A test catches ninety-nine percent of the sick. Where does that "
                          "number go? It becomes this term.") as beat:
            self.play(FadeIn(cell), FadeIn(cite_a), run_time=beat.until("Where"))
            beat.on("this", carry(cell, term, path_arc=-0.4), run_time=1.0)
        count = formula(r"2{,}470", r"\text{ alerts}", size=MATH_LABEL).move_to(DOWN * 0.5)
        count2 = formula(r"173", r"\text{ right}", size=MATH_LABEL).move_to(DOWN * 0.5)
        note = text("tiny footnote", size=12, color=GRAY).move_to(DOWN * 1.6 + LEFT * 3)
        with self.narrate("Cameras raised two thousand four hundred and seventy alerts. "
                          "Only one hundred and seventy-three were right.") as beat:
            self.play(FadeIn(count), swap(cite_a, cite_b), FadeIn(note), run_time=beat.until("Only"))
            self.play(swap(count, count2), run_time=0.7)
        bad = formula(r"3/8", size=MATH_LABEL).move_to(DOWN * 2.3 + RIGHT * 3)
        bad2 = formula(r"2/7", size=MATH_LABEL).move_to(DOWN * 2.3 + RIGHT * 3)
        with self.narrate("Now look at this number. [pause 0.6] It changes.") as beat:
            self.hold(1.6)                                    # nothing lands on "this" (check)
            self.play(FadeIn(bad), run_time=0.5)
            self.hold(0.4)
            self.play(Transform(bad, bad2), run_time=0.8)     # deliberate glyph morph (lint)
        self.end_card()
