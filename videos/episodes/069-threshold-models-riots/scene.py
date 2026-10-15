"""Episode 69 - Two Nearly Identical Crowds: One Riots, One Doesn't.

    videos/toolkit/render.sh videos/episodes/069-threshold-models-riots/scene.py Episode \
        videos/episodes/069-threshold-models-riots/final.mp4
"""
import numpy as np
from scipy.stats import norm

from manim import *
from sample_space import *

N = 100
TH_A = list(range(N))                 # Granovetter's uniform crowd: 0, 1, ..., 99
TH_B = list(range(N))
TH_B[1] = 2                           # the one perturbed person
F_A = [sum(t <= r for t in TH_A) for r in range(11)]   # 1, 2, ..., 11
F_B = [sum(t <= r for t in TH_B) for r in range(11)]   # 1, 1, 3, 4, ...

# Granovetter Fig. 2: thresholds ~ Normal(25, sigma), N = 100; equilibrium = first root of
# 100*Phi((r-25)/sigma) - r from r = 0 (recomputed; critical sigma ~ 12.22)
_XS = np.linspace(0, 100, 20001)
SIG_GRID = np.round(np.arange(7.0, 16.001, 0.005), 3)


def _eq(s):
    g = 100 * norm.cdf(_XS, 25, s) - _XS
    return float(_XS[np.argmax(g <= 0)])


EQ_GRID = np.array([_eq(s) for s in SIG_GRID])


def eq_of(s):
    i = int(np.clip(np.searchsorted(SIG_GRID, s), 0, len(SIG_GRID) - 1))
    return float(EQ_GRID[i])


def make_cell(t):
    c = Circle(radius=0.22, stroke_color=BLUE, stroke_width=2.5, fill_color=BLUE,
               fill_opacity=0.12)
    n = Text(str(t), font=SANS, font_size=22, color=INK).move_to(c)
    return VGroup(c, n)


def make_crowd(ths):
    g = VGroup(*[make_cell(t) for t in ths])
    g.arrange_in_grid(10, 10, buff=0.08)
    return g


def riot(cell):
    return cell[0].animate.set_fill(RED, 0.55).set_stroke(RED, 3)


class Episode(NarratedScene):
    EPISODE = 69
    TITLE = "Two Nearly Identical Crowds"
    PRONUNCIATIONS = {"Granovetter": "gran oh vetter"}

    def construct(self):
        crowd_a = make_crowd(TH_A).move_to(LEFT * 3.3 + DOWN * 0.05)
        crowd_b = make_crowd(TH_B).move_to(RIGHT * 3.3 + DOWN * 0.05)
        key = text("number = rioters needed before joining", size=LABEL, color=GRAY)
        key.move_to(UP * 3.25)

        # ------------------------------------------------------------ 1 cold open
        with self.narrate("Two crowds, a hundred people each. Each number is how many others "
                          "must already be rioting before that person joins in.") as beat:
            self.play(LaggedStart(FadeIn(crowd_a, lag_ratio=0.01), FadeIn(crowd_b, lag_ratio=0.01),
                                  lag_ratio=0.25), run_time=beat.until("Each"))
            beat.wait_until("number", offset=-0.1)
            self.play(Write(key), run_time=1.0)
            beat.wait_until("rioting", offset=-0.3)
            self.play(LaggedStart(*[flag(crowd_a[i][1], run_time=0.7) for i in (5, 23, 61)],
                                  lag_ratio=0.35), run_time=1.6)

        ring_a = Circle(radius=0.3, color=YELLOW, stroke_width=4).move_to(crowd_a[1])
        ring_b = Circle(radius=0.3, color=YELLOW, stroke_width=4).move_to(crowd_b[1])
        with self.narrate("One person differs. Here, a one. Here, a two. "
                          "How many people riot in each crowd? [pause 1.5]") as beat:
            beat.wait_until("Here", offset=-0.15)
            self.play(Create(ring_a), crowd_a[1][1].animate.set_color(YELLOW), run_time=0.6)
            beat.wait_until("Here", occurrence=2, offset=-0.15)
            self.play(Create(ring_b), crowd_b[1][1].animate.set_color(YELLOW), run_time=0.6)
            beat.wait_until("How", offset=-0.1)
            qa = formula(r"\text{rioting} = \,?", color=RED).next_to(crowd_a, DOWN, buff=0.25)
            qb = formula(r"\text{rioting} = \,?", color=RED).next_to(crowd_b, DOWN, buff=0.25)
            self.play(FadeIn(qa, shift=0.1 * UP), FadeIn(qb, shift=0.1 * UP), run_time=0.8)

        # ------------------------------------------------------------ 2 stakes + averages
        avg_a = formula(r"\text{average} = 49.5").next_to(crowd_a, DOWN, buff=0.25)
        avg_b = formula(r"\text{average} = 49.51").next_to(crowd_b, DOWN, buff=0.25)
        with self.narrate("When a protest turns violent, we explain it by who was in the crowd. "
                          "So describe each crowd the usual way, by its average threshold.") as beat:
            self.play(FadeOut(key), run_time=0.8)
            beat.wait_until("average", offset=-0.2)
            self.play(FadeOut(qa), FadeOut(qb), run_time=0.5)

        with self.narrate("Left: forty nine point five. Right: forty nine point five one. "
                          "By that measure they are the same crowd, so they should do the "
                          "same thing.") as beat:
            self.play(TransformFromCopy(VGroup(*[c[1] for c in crowd_a]), avg_a),
                      run_time=beat.until("Right", offset=-0.1))
            self.play(TransformFromCopy(VGroup(*[c[1] for c in crowd_b]), avg_b),
                      run_time=beat.until("By", offset=-0.1))
            eq_sign = formula(r"\approx", size=EQ).move_to((avg_a.get_center() + avg_b.get_center()) / 2)
            self.play(FadeIn(eq_sign, scale=0.8), run_time=0.6)
            beat.wait_until("same", offset=-0.1)
            self.play(Indicate(avg_a, color=YELLOW, scale_factor=1.05),
                      Indicate(avg_b, color=YELLOW, scale_factor=1.05), run_time=1.0)

        # ------------------------------------------------------------ 3 run crowd A
        ta, tb = ValueTracker(0), ValueTracker(0)
        cnt_a = live_number(ta, 0, prefix=r"\text{rioting} =", color=RED)
        cnt_b = live_number(tb, 0, prefix=r"\text{rioting} =", color=RED)
        cnt_a.move_to(avg_a)
        cnt_b.move_to(avg_b)
        cite = citation("Example from Granovetter, 1978 · American Journal of Sociology")
        with self.narrate("Run them. The person with threshold zero breaks a window. One rioter "
                          "is enough for the one. Two rioters bring in the two, and the wave "
                          "carries all the way to a hundred.") as beat:
            self.play(FadeOut(eq_sign), FadeOut(avg_a, shift=0.2 * DOWN), FadeOut(avg_b, shift=0.2 * DOWN),
                      FadeIn(cnt_a, shift=0.2 * DOWN), FadeIn(cnt_b, shift=0.2 * DOWN),
                      FadeIn(cite), run_time=0.8)
            beat.wait_until("breaks", offset=-0.1)
            self.play(riot(crowd_a[0]), ta.animate.set_value(1), run_time=0.6)
            beat.wait_until("one", occurrence=2, offset=-0.15)
            self.play(riot(crowd_a[1]), ring_a.animate.set_stroke(RED), ta.animate.set_value(2),
                      run_time=0.6)
            beat.wait_until("two", occurrence=2, offset=-0.15)
            self.play(riot(crowd_a[2]), ta.animate.set_value(3), run_time=0.6)
            self.play(LaggedStart(*[riot(crowd_a[i]) for i in range(3, N)], lag_ratio=0.12),
                      ta.animate(rate_func=linear).set_value(100),
                      run_time=beat.remaining(min_time=3.5))
        cnt_a.number.clear_updaters()

        # ------------------------------------------------------------ 4 run crowd B
        with self.narrate("On the right, the same instigator breaks the same window. But nobody "
                          "here has a threshold of one. The two waits for a second rioter who "
                          "never comes.") as beat:
            beat.wait_until("breaks", offset=-0.1)
            self.play(riot(crowd_b[0]), tb.animate.set_value(1), run_time=0.6)
            beat.wait_until("nobody", offset=-0.1)
            self.play(Indicate(ring_b, color=YELLOW, scale_factor=1.2), run_time=0.9)
            beat.wait_until("waits", offset=-0.2)
            for _ in range(2):
                self.play(Indicate(ring_b, color=YELLOW, scale_factor=1.25), run_time=0.9)
        cnt_b.number.clear_updaters()

        # ------------------------------------------------------------ 5 the measured failure
        miss = formula(r"\text{off by } 99", size=EQ, color=YELLOW).move_to(DOWN * 3.05 + RIGHT * 2.0)
        with self.narrate("A hundred against one. The average missed by ninety nine people, "
                          "because a riot is a chain, and an average can't see a missing link.") as beat:
            self.play(FadeOut(cite), Indicate(cnt_a, color=RED, scale_factor=1.12), run_time=0.9)
            self.play(Indicate(cnt_b, color=RED, scale_factor=1.12), run_time=0.9)
            beat.wait_until("missed", offset=-0.2)
            self.play(Write(miss), run_time=0.9)
            beat.wait_until("chain", offset=-0.1)
            self.play(LaggedStart(*[Indicate(crowd_a[i], color=YELLOW, scale_factor=1.25)
                                    for i in range(0, 6)], lag_ratio=0.3), run_time=1.6)
            beat.wait_until("missing", offset=-0.1)
            self.play(Indicate(crowd_b[1], color=YELLOW, scale_factor=1.35), run_time=1.0)

        # ------------------------------------------------------------ 6 draw the chain
        mini_a = VGroup(crowd_a, ring_a)
        mini_b = VGroup(crowd_b, ring_b)
        ax = axes((-0.6, 10.6), (0, 12), x_ticks=[0, 2, 4, 6, 8, 10], y_ticks=[0, 3, 6, 9, 12],
                  x_length=7.6, y_length=4.9, x_label="rioters so far", y_label="people willing")
        ax.move_to(LEFT * 2.0 + DOWN * 0.05)
        ux, uy = ax.x_axis.unit_size, ax.y_axis.unit_size

        def block(r, j, color=BLUE):
            return Rectangle(width=0.62 * ux, height=uy - 0.05, stroke_width=0, fill_color=color,
                             fill_opacity=0.8).move_to(ax.c2p(r, j + 0.5))

        bars_a = VGroup(*[VGroup(*[block(r, j) for j in range(F_A[r])]) for r in range(11)])
        with self.narrate("So draw the chain. Across: how many are rioting so far. Up: how many "
                          "people are willing at that count, everyone whose threshold is that "
                          "low or lower.") as beat:
            self.play(FadeOut(miss), FadeOut(cnt_a), FadeOut(cnt_b),
                      *[c[1].animate.set_opacity(0) for c in [*crowd_a, *crowd_b]],
                      run_time=0.6)
            self.play(mini_a.animate.scale(0.27).move_to(RIGHT * 3.95 + UP * 2.75),
                      mini_b.animate.scale(0.27).move_to(RIGHT * 5.6 + UP * 2.75),
                      run_time=1.0)
            self.play(Create(ax.x_axis), Write(ax.x_title), run_time=beat.until("Up", offset=-0.1))
            self.play(Create(ax.y_axis), Write(ax.y_title), run_time=0.9)
            beat.wait_until("everyone", offset=-0.2)
            # each block is a person: bar r collects everyone with threshold <= r
            for r in range(3):
                self.play(*[TransformFromCopy(crowd_a[j][0], bars_a[r][j]) for j in range(F_A[r])],
                          run_time=0.7)
            self.play(LaggedStart(*[TransformFromCopy(VGroup(*[crowd_a[j][0] for j in range(F_A[r])]),
                                                      bars_a[r]) for r in range(3, 11)],
                                  lag_ratio=0.2), run_time=beat.remaining(min_time=2.0))

        line = Line(ax.c2p(0, 0), ax.c2p(10.6, 10.6), color=PURPLE, stroke_width=4)
        line_lbl = text("willing = rioting", size=LABEL, color=PURPLE)
        line_lbl.rotate(np.arctan2(uy, ux)).move_to(ax.c2p(9.2, 10.15)).shift(0.45 * (UP + LEFT) * 0.7)
        with self.narrate("The purple line is where willing equals rioting. Wherever a bar pokes "
                          "above it, someone new joins, and the count steps right.") as beat:
            self.play(Create(line), run_time=beat.until("willing", offset=-0.1))
            self.play(FadeIn(line_lbl), run_time=0.7)
            beat.wait_until("pokes", offset=-0.1)
            top0 = bars_a[0][0]
            self.play(Indicate(top0, color=YELLOW, scale_factor=1.15), run_time=0.9)
            beat.wait_until("steps", offset=-0.2)
            step0 = VMobject(color=YELLOW, stroke_width=5).set_points_as_corners(
                [ax.c2p(0, 0), ax.c2p(0, 1), ax.c2p(1, 1)])
            self.play(Create(step0), run_time=1.0)

        pts = [ax.c2p(0, 0)]
        for r in range(10):
            pts += [ax.c2p(r, r + 1), ax.c2p(r + 1, r + 1)]
        stair_a = VMobject(color=YELLOW, stroke_width=5).set_points_as_corners(pts)
        onward = formula(r"\to 100", color=RED).next_to(ax.c2p(10, 11), RIGHT, buff=0.25)
        with self.narrate("In the left crowd every bar sits one person above the line, so the "
                          "staircase climbs and never stops.") as beat:
            self.play(Indicate(mini_a, color=YELLOW, scale_factor=1.1), run_time=0.8)
            self.play(LaggedStart(*[Indicate(b[-1], color=YELLOW, scale_factor=1.1) for b in bars_a],
                                  lag_ratio=0.15), run_time=beat.until("staircase", offset=-0.1))
            self.play(Create(stair_a), run_time=beat.remaining(min_time=2.0), rate_func=linear)
            self.remove(step0)
            self.play(Write(onward), run_time=0.6)

        # crowd B: the threshold-1 person leaves bar 1 (they now need 2)
        leaver = bars_a[1][1]
        stair_b = VMobject(color=YELLOW, stroke_width=5).set_points_as_corners(
            [ax.c2p(0, 0), ax.c2p(0, 1), ax.c2p(1, 1)])
        stop = Dot(ax.c2p(1, 1), radius=0.11, color=YELLOW)
        with self.narrate("Now the right crowd. One person's threshold moves from one to two, so "
                          "this bar loses them. At one rioter, only one person is willing. The bar "
                          "touches the line, and the riot stops dead.") as beat:
            self.play(FadeOut(stair_a), FadeOut(onward), Indicate(mini_b, color=YELLOW, scale_factor=1.1),
                      run_time=0.9)
            beat.wait_until("this", offset=-0.15)
            self.play(leaver.animate.set_fill(YELLOW), run_time=0.5)
            self.play(FadeOut(leaver, shift=0.6 * UP), run_time=0.9)
            beat.wait_until("touches", offset=-0.2)
            self.play(Create(stair_b), run_time=1.0)
            self.play(FadeIn(stop, scale=0.5), Flash(stop, color=YELLOW, flash_radius=0.35),
                      run_time=0.8)

        # ------------------------------------------------------------ 7 the rule
        f_lbl = formula(r"F(r)", color=BLUE).next_to(bars_a[4], UP, buff=0.18)
        rule = formula(r"F(r)", r"=", r"r", size=EQ).move_to(RIGHT * 4.75 + UP * 0.9)
        rule[0].set_color(BLUE)
        rule[2].set_color(PURPLE)
        first = text("first r where", size=LABEL, color=GRAY).next_to(rule, UP, buff=0.3)
        with self.narrate("Call the willing count F of r. The riot ends at the first r where "
                          "F of r equals r.") as beat:
            self.play(Write(f_lbl), Indicate(bars_a[4], color=BLUE, scale_factor=1.05),
                      run_time=beat.until("riot", offset=-0.1))
            self.play(FadeIn(first), run_time=0.6)
            beat.wait_until("F", occurrence=2, offset=-0.1)
            self.play(TransformFromCopy(f_lbl, rule[0]), run_time=0.8)
            self.play(Write(rule[1]), run_time=0.4)
            self.play(TransformFromCopy(line_lbl, rule[2]), run_time=0.8)
            self.play(flag(stop), run_time=0.8)

        # ------------------------------------------------------------ 8 Granovetter's bell curve
        ax2 = axes((0, 100), (0, 100), x_ticks=[0, 20, 40, 60, 80, 100],
                   y_ticks=[0, 20, 40, 60, 80, 100], x_length=7.6, y_length=4.9,
                   x_label="rioters so far", y_label="people willing")
        ax2.move_to(ax)
        sig = ValueTracker(9.0)
        curve = always_redraw(lambda: ax2.plot(
            lambda x: 100 * norm.cdf(x, 25, sig.get_value()), x_range=[0, 100, 0.25],
            color=BLUE, stroke_width=5))
        line2 = Line(ax2.c2p(0, 0), ax2.c2p(100, 100), color=PURPLE, stroke_width=4)
        lbl2 = text("willing = rioting", size=LABEL, color=PURPLE)
        lbl2.rotate(np.arctan2(4.9, 7.6)).move_to(ax2.c2p(70, 76)).shift(0.3 * (UP + LEFT))
        dot = always_redraw(lambda: Dot(ax2.c2p(eq_of(sig.get_value()), eq_of(sig.get_value())),
                                        radius=0.11, color=YELLOW))
        sig_lbl = live_number(sig, 1, prefix=r"\text{spread } \sigma =", color=YELLOW)
        mean_lbl = formula(r"\text{average} = 25", color=GRAY)
        rt = ValueTracker(eq_of(9.0))
        riot_lbl = live_number(rt, 1, prefix=r"\text{rioting} =", color=RED)
        rt.add_updater(lambda m: m.set_value(eq_of(sig.get_value())))
        panel = VGroup(mean_lbl, sig_lbl, riot_lbl).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        panel.move_to(RIGHT * 4.55 + DOWN * 0.95)
        cite2 = citation("Recomputed from Granovetter, 1978 · AJS, Fig. 2 (N = 100)")
        with self.narrate("Granovetter ran this picture on a bell curve of thresholds, average "
                          "twenty five. Make the crowd more varied, with more radicals and more "
                          "holdouts. Does the riot grow or shrink? [pause 1.5]") as beat:
            self.play(FadeOut(VGroup(bars_a, stair_b, f_lbl, stop)), FadeOut(line_lbl),
                      FadeOut(first), rule.animate.scale(0.75).move_to(RIGHT * 4.75 + UP * 1.0),
                      run_time=0.8)
            self.play(ReplacementTransform(ax, ax2), ReplacementTransform(line, line2),
                      FadeIn(cite2), run_time=1.2)
            self.play(Create(curve), FadeIn(lbl2), run_time=beat.until("twenty", offset=-0.1))
            self.play(FadeIn(mean_lbl, shift=0.1 * LEFT), run_time=0.6)
            beat.wait_until("varied", offset=-0.1)
            self.play(FadeIn(sig_lbl, shift=0.1 * LEFT), run_time=0.6)
            self.play(sig.animate.set_value(10.0), run_time=1.2)
            self.play(sig.animate.set_value(9.0), run_time=1.2)
            beat.wait_until("grow", offset=-0.2)
            self.play(FadeIn(dot), FadeIn(riot_lbl, shift=0.1 * LEFT), run_time=0.6)

        self.add(rt)
        with self.narrate("With a narrow spread, the curve meets the line almost at once, and "
                          "barely anyone riots. Widen it, and the count creeps up to about six. "
                          "Then, near a spread of twelve point two, that first crossing vanishes, "
                          "and the riot leaps to nearly a hundred. The average never moved.") as beat:
            self.play(Flash(dot, color=YELLOW, flash_radius=0.3), run_time=beat.until("Widen", offset=-0.1))
            self.play(sig.animate.set_value(12.15), run_time=beat.until("Then", offset=-0.1), rate_func=smooth)
            self.play(sig.animate.set_value(12.21), run_time=beat.until("vanishes", offset=0.1),
                      rate_func=linear)
            self.play(sig.animate.set_value(12.6), run_time=beat.until("hundred", offset=0.1),
                      rate_func=smooth)
            beat.wait_until("average", offset=-0.2)
            self.play(Indicate(mean_lbl, color=YELLOW, scale_factor=1.1), run_time=1.0)
        rt.clear_updaters()

        caveat = text("stylized: thresholds can't be measured", size=LABEL, color=GRAY)
        caveat.next_to(ax2, UP, buff=0.2).align_to(ax2.y_axis, LEFT).shift(RIGHT * 1.2)
        with self.narrate("This is a stylized model. Nobody can measure a real person's threshold, "
                          "so it explains no particular riot. It shows what an average hides.") as beat:
            self.play(FadeIn(caveat), FadeOut(cite2), run_time=0.8)
            beat.wait_until("shows", offset=-0.2)
            self.play(Indicate(mean_lbl, color=YELLOW, scale_factor=1.1), run_time=1.0)

        # ------------------------------------------------------------ 9 landing
        curve.clear_updaters()
        dot.clear_updaters()
        hl_a = text("“A crowd of radicals”", size=BODY, slant=ITALIC)
        hl_b = text("“…solid citizens looked on”", size=BODY, slant=ITALIC)
        cite3 = citation("Granovetter, 1978 · American Journal of Sociology")
        with self.narrate("Granovetter imagined the next day's headlines. Left: a crowd of radicals "
                          "engaged in riotous behavior. Right: a demented troublemaker broke a "
                          "window while a group of solid citizens looked on.") as beat:
            self.play(FadeOut(VGroup(ax2, curve, line2, lbl2, dot, panel, rule, caveat)),
                      run_time=0.7)
            self.play(mini_a.animate.scale(0.8 / 0.27).move_to(LEFT * 3.3 + UP * 0.55),
                      mini_b.animate.scale(0.8 / 0.27).move_to(RIGHT * 3.3 + UP * 0.55), run_time=1.2)
            self.play(*[c[1].animate.set_opacity(1) for c in [*crowd_a, *crowd_b]], run_time=0.6)
            hl_a.next_to(crowd_a, DOWN, buff=0.35)
            hl_b.next_to(crowd_b, DOWN, buff=0.35)
            self.play(FadeIn(cite3), run_time=0.5)
            beat.wait_until("crowd", offset=-0.2)
            self.play(Write(hl_a), run_time=1.2)
            beat.wait_until("demented", offset=-0.2)
            self.play(Indicate(crowd_b[0], color=RED, scale_factor=1.3), run_time=1.0)
            beat.wait_until("solid", offset=-0.2)
            self.play(Write(hl_b), run_time=1.2)

        with self.narrate("Same hundred people, minus one link. What a crowd did tells you very "
                          "little about who was in it.") as beat:
            self.play(FadeOut(cite3), Indicate(ring_a, color=YELLOW, scale_factor=1.3),
                      Indicate(ring_b, color=YELLOW, scale_factor=1.3), run_time=1.0)
            beat.wait_until("who", offset=-0.2)
            self.play(Indicate(hl_a, color=YELLOW, scale_factor=1.04),
                      Indicate(hl_b, color=YELLOW, scale_factor=1.04), run_time=1.0)

        self.end_card()
