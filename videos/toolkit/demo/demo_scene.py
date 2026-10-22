"""Toolkit demo (~30 s): NarratedScene + style + MathTex + axes plot + word triggers.
Models the round-6 conventions (PRODUCTION_GUIDE §13): CADENCE = "shaped", default voice
speed, numbers written without "and", carry() for a value flying into a different symbol,
beat.on() for a deictic, and a render with zero warnings.

    videos/toolkit/render.sh videos/toolkit/demo/demo_scene.py Demo videos/toolkit/demo/demo.mp4
"""
from math import comb

from manim import *
from sample_space import *

FLIPS = "HTHHHTHHTH"            # one concrete run: 7 heads out of 10
PMF = [comb(10, k) / 2 ** 10 for k in range(11)]


def coin(face: str) -> VGroup:
    heads = face == "H"
    disk = Circle(radius=0.42, stroke_color=YELLOW if heads else GRAY, stroke_width=3,
                  fill_color=YELLOW if heads else GRAY, fill_opacity=0.18)
    return VGroup(disk, text(face, size=LABEL, color=YELLOW if heads else GRAY).move_to(disk))


class Demo(NarratedScene):
    EPISODE = 0
    TITLE = "Toolkit demo"
    CADENCE = "shaped"            # gaps follow the sense (PRODUCTION_GUIDE §4, §13.3)

    def construct(self):
        coins = VGroup(*[coin(f) for f in FLIPS]).arrange(RIGHT, buff=0.24).move_to(UP * 2.5)
        heads = VGroup(*[c for c, f in zip(coins, FLIPS) if f == "H"])

        # 1 - concrete question, coins on screen from the first second
        with self.narrate("Flip a fair coin ten times. How likely is it that exactly "
                          "seven of them land heads?") as beat:
            self.play(LaggedStart(*[FadeIn(c, shift=0.3 * DOWN) for c in coins], lag_ratio=0.3),
                      run_time=beat.until_end_of("times"))
            count = formula(r"7", r"\text{ heads out of }", r"10").next_to(coins, DOWN, buff=0.5)
            count[0].set_color(YELLOW)
            beat.wait_until("seven", offset=-0.1)
            self.play(LaggedStart(*[flag(c) for c in heads], lag_ratio=0.12),
                      FadeIn(count, shift=0.15 * UP), run_time=1.4)

        # 2 - both counts emerge from the coins they count
        total = formula(r"2^{10}", "=", r"1024", size=EQ).move_to(LEFT * 3.2 + DOWN * 0.5)
        ways = MathTex(r"\binom{10}{7}", "=", r"120", font_size=EQ,
                       substrings_to_isolate=["10", "7"]).move_to(RIGHT * 3.2 + DOWN * 0.5)
        w10, w7 = ways.get_part_by_tex("10"), ways.get_part_by_tex("7")   # glyph groups
        w_eq, w120 = ways[1], ways[2]
        w_paren = VGroup(*[g for g in ways[0] if g not in w10 and g not in w7])
        VGroup(w10, w7, w_paren, w120).set_color(YELLOW)
        with self.narrate("Ten flips give one thousand twenty-four equally likely "
                          "sequences. One hundred twenty of them have seven heads.") as beat:
            beat.wait_until("thousand", offset=-0.2)
            # "10" -> "2^10": different glyphs, so carry() (a cross-fade flight), not a morph
            self.play(carry(count[2], total[0], path_arc=0.4), run_time=1.2)
            self.play(Write(total[1:]), run_time=0.8)
            beat.wait_until("hundred", offset=-0.2)
            # each number flies into its own slot of the binomial (isolated parts)
            self.play(carry(count[2], w10, path_arc=-0.4), carry(count[0], w7, path_arc=-0.4),
                      run_time=1.2)
            self.play(FadeIn(w_paren), Write(VGroup(w_eq, w120)), run_time=0.8)

        # 3 - the probability is built from those two numbers
        prob = MathTex(r"P(7)", "=", r"\frac{120}{1024}", r"\approx", r"0.117", font_size=EQ,
                       substrings_to_isolate=["120", "1024"]).move_to(DOWN * 2.3)
        num, den = prob.get_part_by_tex("120"), prob.get_part_by_tex("1024")
        frac_bar = VGroup(*[g for g in prob[2] if g not in num and g not in den])
        num.set_color(YELLOW)
        prob[4].set_color(YELLOW)
        with self.narrate("So the chance is one hundred twenty out of one thousand twenty "
                          "four, about twelve percent.") as beat:
            self.play(Write(prob[0:2]), run_time=0.8)
            self.play(TransformFromCopy(w120, num), run_time=beat.until("out of"))
            self.play(TransformFromCopy(total[2], den), Create(frac_bar), run_time=1.0)
            beat.wait_until("about")
            self.play(Write(prob[3:]), run_time=0.9)

        # 4 - every count at once: the binomial hump
        ax = axes((-0.6, 10.6), (0, 0.25), x_ticks=[0, 2, 4, 6, 8, 10], x_length=8.6,
                  y_length=4.0, x_label="heads (count)", y_label="probability")
        ax.move_to(LEFT * 1.6 + DOWN * 0.15)
        bars = VGroup(*[
            Rectangle(width=0.62 * ax.x_axis.unit_size, height=max(p * ax.y_axis.unit_size, 0.01),
                      stroke_width=0, fill_color=BLUE, fill_opacity=0.9)
            .move_to(ax.c2p(k, 0), aligned_edge=DOWN)
            for k, p in enumerate(PMF)])
        small = prob.copy().scale(0.72).to_corner(UR, buff=0.0).shift(LEFT * 0.9 + DOWN * 0.75)
        with self.narrate("Do that count for every number of heads, and the chances form "
                          "this hump. Seven sits on its right shoulder.") as beat:
            self.play(FadeOut(coins), FadeOut(count), FadeOut(total), FadeOut(ways),
                      Transform(prob, small), run_time=1.0)
            self.play(Create(ax), run_time=beat.until("chances"))
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.08),
                      run_time=beat.until("this", offset=-0.15))
            beat.on("this", flag(bars), run_time=0.8)        # the deictic lands on its picture
            beat.wait_until("Seven", offset=-0.1)
            tag = MathTex(r"0.117", font_size=MATH_SMALL, color=YELLOW).next_to(bars[7], UP, buff=0.15)
            self.play(bars[7].animate.set_fill(YELLOW),
                      TransformFromCopy(prob[4], tag), run_time=1.2)

        self.end_card()
