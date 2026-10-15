"""Synthetic layout-audit test: known overlaps at known times, and known-clean layouts.

    videos/toolkit/render.sh --preview videos/toolkit/tests/audit_synthetic_scene.py \
        AuditSynthetic /tmp/audit_synth/out.mp4
    # expect: overlap 'Sue' ~3.5-5.5 s, overlap '2/7' vs Line from ~7 s, clearance 'A' vs Dot
    # from ~9.5 s, safe-area 'too far right' from ~11 s, 1 allowed (B on the ellipse);
    # nothing for the boxed label, the coin or the token on its edge.

Timeline (s)          on screen                                      expected finding
 0.0-1.0  FadeIn      label in its own box, coin, token on an edge     -
 1.0-3.0  wait        same                                             -
 3.0-3.5  FadeIn      "Sue" + token covering its 'e'                   overlap 3.5-6.0
 3.5-5.5  hold        (held)
 5.5-6.0  move token away                                              (fixed at 6.0)
 6.0-7.0  FadeIn      axis + rung label "2/7" crossing it              overlap 7.0-13.5
 7.0-9.0  wait
 9.0-9.5  label next_to a dot at buff 0.08                             clearance 9.5-13.5
 9.5-10.5 wait
10.5-11.0 text pushed past the right safe edge                         safe-area 11.0-13.5
11.0-12.0 wait
12.0-12.5 label on an ellipse's stroke, allowed via allow_overlap()    allowed (not printed)
12.5-13.5 wait
13.5-14.0 FadeOut everything                                           -
"""
from manim import *
from sample_space import *


def token(v):
    sq = Square(0.26, stroke_width=0, fill_color=YELLOW, fill_opacity=1)
    return VGroup(sq, MathTex(str(v), font_size=26, color=BG).move_to(sq))


class AuditSynthetic(NarratedScene):
    EPISODE = 0
    TITLE = "audit synthetic"

    def construct(self):
        lab = text("inside its box", size=LABEL).move_to(UP * 2.8 + LEFT * 3)
        bx = box(lab)
        disk = Circle(radius=0.42, stroke_color=YELLOW, stroke_width=3, fill_color=YELLOW,
                      fill_opacity=0.18).move_to(UP * 2.8 + RIGHT * 1)
        coin = VGroup(disk, text("H", size=LABEL, color=YELLOW).move_to(disk))
        edge = Line(RIGHT * 2.5 + UP * 2.8, RIGHT * 5.5 + UP * 2.8, color=GRAY, stroke_width=3)
        t1 = token(3).move_to(edge.point_from_proportion(0.3))
        self.play(FadeIn(lab), Create(bx), FadeIn(coin), Create(edge), FadeIn(t1), run_time=1.0)
        self.wait(2.0)

        sue = text("Sue", size=26, color=GRAY).move_to(LEFT * 4 + UP * 0.8)
        t4 = token(4).move_to(sue.get_corner(DR) + LEFT * 0.03 + DOWN * 0.04)
        self.play(FadeIn(sue), FadeIn(t4), run_time=0.5)
        self.hold(2.0)
        self.play(t4.animate.shift(RIGHT * 0.6 + DOWN * 0.3), run_time=0.5)

        ax = Line(LEFT * 1 + DOWN * 0.5, RIGHT * 5 + DOWN * 0.5, color=GRAY, stroke_width=2.5)
        l27 = MathTex(r"\frac{2}{7}", font_size=32).move_to(RIGHT * 2 + DOWN * 0.55)
        self.play(Create(ax), FadeIn(l27), run_time=1.0)
        self.wait(2.0)

        d = Dot(LEFT * 4 + DOWN * 1.5, radius=0.06, color=BLUE)
        a = text("A", size=LABEL).next_to(d, UP, buff=0.08)
        self.play(FadeIn(d), FadeIn(a), run_time=0.5)
        self.wait(1.0)

        far = text("too far right", size=LABEL).move_to(RIGHT * 5.9 + DOWN * 2.2)
        self.play(FadeIn(far), run_time=0.5)
        self.wait(1.0)

        ell = Ellipse(width=2.4, height=1.2, color=BLUE).move_to(LEFT * 1 + DOWN * 2.2)
        on = text("B", size=LABEL).move_to(ell.point_from_proportion(0.0))
        self.allow_overlap(on, ell, reason="test: label deliberately on the ellipse")
        self.play(Create(ell), FadeIn(on), run_time=0.5)
        self.wait(1.0)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)
