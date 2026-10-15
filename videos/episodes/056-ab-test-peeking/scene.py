"""Episode 56 - Why Checking Your A/B Test Early Breaks It.

    videos/toolkit/render.sh videos/episodes/056-ab-test-peeking/scene.py Episode \
        videos/episodes/056-ab-test-peeking/final.mp4

Data: data.npz from make_data.py (1,000 simulated A/A tests, seed 47).
"""
from pathlib import Path

import numpy as np
from manim import *
from sample_space import *

HERE = Path(__file__).resolve().parent
D = np.load(HERE / "data.npz")
Z = D["Z"]                       # (1000, 20) z after each day
FIRST = D["first"]               # first day index crossing +-1.96 (-1 = never)
FIRST_OBF = D["first_obf"]       # first day index crossing the O'Brien-Fleming funnel
OBF = D["obf"]                   # funnel per day
OBF_C = float(D["C"])
HERO = int(D["hero"])
T, DAYS = Z.shape
ZC = 1.959964

N_PEEK = int((FIRST >= 0).sum())                     # 249
N_ONCE = int((np.abs(Z[:, -1]) > ZC).sum())          # 52
N_OBF = int((FIRST_OBF >= 0).sum())                  # 49
SLICES = [int((FIRST == k).sum()) for k in range(DAYS)]
SLICES_OBF = [int((FIRST_OBF == k).sum()) for k in range(DAYS)]

# right-hand panel and stacked-bar geometry
PANEL_X = 4.75
BAR_BOTTOM = -2.45
PCT = 0.15                       # units per percentage point
BAR1_X, BAR2_X, BAR_W = 4.05, 5.65, 0.72


def button(letter: str) -> VGroup:
    body = RoundedRectangle(corner_radius=0.2, width=2.7, height=0.95, stroke_color=GRAY,
                            stroke_width=3, fill_color=DIM, fill_opacity=0.55)
    word = text("Sign up", size=BODY).move_to(body)
    tag = text(letter, size=LABEL, color=GRAY).next_to(body, UP, buff=0.18)
    g = VGroup(body, word, tag)
    g.body = body
    return g


class Episode(NarratedScene):
    EPISODE = 56
    TITLE = "Why Checking Your A/B Test Early Breaks It"
    PRONUNCIATIONS = {
        "Johari": "jo harry",
        "Optimizely": "optimize lee",
        "McPherson": "mick fur son",
    }

    # ------------------------------------------------------------------ helpers
    def P(self, day, z):
        return self.ax.c2p(day, z + 4)

    def make_paths(self, first, skip=()):
        paths, dots = VGroup(), VGroup()
        for i in range(T):
            if i in skip:
                continue
            f = int(first[i])
            end = f + 1 if f >= 0 else DAYS
            pts = [self.P(d, Z[i, d - 1]) for d in range(1, end + 1)]
            if len(pts) >= 2:
                p = VMobject(stroke_color=BLUE, stroke_width=1.3, stroke_opacity=0.32)
                p.set_points_as_corners(pts)
                p.full = p.copy()
                p.n_end = end
                p.win = f >= 0
                p.is_red = False
                p.pointwise_become_partial(p.full, 0, 0)
                paths.add(p)
            if f >= 0:
                d = Dot(pts[-1], radius=0.055, color=RED, fill_opacity=0)
                d.day = end
                d.test = i
                dots.add(d)
        allow_overlap(paths)
        allow_overlap(dots)
        return paths, dots

    def sweep(self, paths, dots, tracker, run_time, extra=()):
        def upd(_):
            d = tracker.get_value()
            for p in paths:
                n = p.n_end
                a = float(np.clip((d - 1) / (n - 1), 0, 1))
                p.pointwise_become_partial(p.full, 0, a)
                if p.win and not p.is_red and d >= n - 1e-6:
                    p.set_stroke(RED, opacity=0.7, width=1.4)
                    p.is_red = True
            for dt in dots:
                dt.set_fill(opacity=1.0 if d >= dt.day - 1e-6 else 0.0)
        holder = VGroup(paths, dots)
        self.play(tracker.animate.set_value(DAYS), UpdateFromFunc(holder, upd), *extra,
                  run_time=run_time, rate_func=linear)

    # ------------------------------------------------------------------ scene
    def construct(self):
        # ============================================================ COLD OPEN
        btn_a, btn_b = button("A"), button("B")
        btns = VGroup(btn_a, btn_b).arrange(RIGHT, buff=1.6).move_to(UP * 2.35)
        eq = formula("=", size=60).move_to(VGroup(btn_a.body, btn_b.body).get_center())
        rate_a = formula(r"10\%", size=MATH).next_to(btn_a.body, DOWN, buff=0.3)
        rate_b = formula(r"10\%", size=MATH).next_to(btn_b.body, DOWN, buff=0.3)
        rate_lbl = label("true click rate", color=GRAY).move_to(
            [0, rate_a.get_center()[1], 0])
        head = VGroup(btns, eq)

        with self.narrate("These two sign-up buttons are identical. Same color, same words, "
                          "and the same true click rate, ten percent.") as beat:
            self.play(LaggedStart(FadeIn(btn_a, shift=0.2 * DOWN), FadeIn(btn_b, shift=0.2 * DOWN),
                                  lag_ratio=0.35), run_time=beat.until("identical", offset=-0.1))
            self.play(Write(eq), flag(btn_a.body, color=INK), flag(btn_b.body, color=INK),
                      run_time=0.9)
            beat.wait_until("click rate", offset=-0.2)
            self.play(FadeIn(rate_lbl), TransformFromCopy(btn_a.body, rate_a),
                      TransformFromCopy(btn_b.body, rate_b), run_time=beat.until("ten", offset=0.3))

        looks = VGroup(*[Circle(radius=0.13, stroke_color=GRAY, stroke_width=2.5,
                                fill_color=INK, fill_opacity=0) for _ in range(DAYS)])
        looks.arrange(RIGHT, buff=0.24).move_to(UP * 0.05 + RIGHT * 0.9)
        looks_lbl = label("daily checks", color=GRAY).next_to(looks, LEFT, buff=0.35)
        rule = formula(r"p < 0.05", r"\;\Rightarrow\;", r"\text{stop}", size=MATH, color=YELLOW)
        rule.move_to(DOWN * 1.05)
        with self.narrate("You run an A B test on them anyway. Every day for twenty days you "
                          "check the p-value, and you stop the first time it drops below "
                          "point oh five.") as beat:
            self.play(FadeIn(looks_lbl), LaggedStart(*[Create(c) for c in looks], lag_ratio=0.1),
                      run_time=beat.until("Every", offset=-0.1))
            self.play(LaggedStart(*[c.animate.set_fill(INK, opacity=0.85) for c in looks],
                                  lag_ratio=0.35), run_time=beat.until("check"))
            self.play(LaggedStart(*[c.animate.set_fill(opacity=0.0) for c in looks],
                                  lag_ratio=0.2), run_time=beat.until("stop", offset=-0.1))
            self.play(Write(rule), run_time=1.2)

        question = formula(r"P(\text{a winner})", "=", "?", size=EQ).move_to(DOWN * 2.3 + LEFT * 2.2)
        question[2].scale(1.25)
        with self.narrate("How often does one of two identical buttons get declared the "
                          "winner? [pause 1.5]") as beat:
            self.play(Write(question[:2]), run_time=beat.until("declared"))
            self.play(Write(question[2]), flag(eq, color=INK), run_time=1.0)

        promise_lbl = label("promised", color=GRAY)
        promise_frac = formula(r"\tfrac{1}{20}", "=", r"5\%", size=EQ, color=YELLOW)
        promise = VGroup(promise_lbl, promise_frac).arrange(RIGHT, buff=0.3)
        promise.move_to(DOWN * 2.3 + RIGHT * 3.4)
        with self.narrate("Point oh five comes with a promise. When the buttons truly match, "
                          "you get fooled in one test out of twenty, five percent.") as beat:
            self.play(flag(rule[0], color=YELLOW), run_time=beat.until("promise", offset=-0.2))
            self.play(FadeIn(promise_lbl, shift=0.1 * UP), run_time=0.6)
            beat.wait_until("one test", offset=-0.1)
            self.play(Write(promise_frac[0]), run_time=0.8)
            beat.wait_until("five percent", offset=-0.2)
            self.play(Write(promise_frac[1:]), run_time=0.8)

        # ============================================================ NAIVE BUILD
        ax = axes((0, 20.6), (0, 8), x_length=7.4, y_length=4.6, x_ticks=[1, 5, 10, 15, 20],
                  y_ticks=[0, 2, 4, 6, 8], x_label="day of test", y_label="z (std. errors)")
        self.ax = ax
        ax.shift(np.array([-5.3, 0, 0]) - ax.c2p(0, 4))
        # relabel the shifted y axis as z = -4..4
        ax.y_axis.remove(ax.y_axis.numbers)
        ynums = VGroup(*[formula(f"{v}", size=MATH_SMALL, color=GRAY)
                         .next_to(ax.c2p(0, v + 4), LEFT, buff=0.18) for v in (-4, -2, 0, 2, 4)])
        ax.remove(ax.y_title)
        ax.y_title.next_to(ax.c2p(0, 8), UP, buff=0.25).align_to(ynums, LEFT)
        ax.remove(ax.x_title)
        ax.x_title.next_to(ax.x_axis, RIGHT, buff=0.15).shift(DOWN * 0.38)
        zero = DashedLine(self.P(0, 0), self.P(20.6, 0), color=DIM, stroke_width=1.5,
                          dash_length=0.08)
        chart = VGroup(ax, ynums, ax.y_title, ax.x_title)
        day_marks = VGroup(*[Dot(self.P(d, -4), radius=0.06, color=GRAY) for d in range(1, DAYS + 1)])

        mini = head.copy().scale(0.42).move_to([PANEL_X, 3.12, 0])
        mini_a, mini_b = mini[0][0], mini[0][1]
        zf = MathTex("z", "=", r"{\hat p_B", "-", r"\hat p_A", r"\over", r"\text{SE}}",
                     font_size=MATH).move_to([PANEL_X, 1.85, 0])
        zf[0].set_color(BLUE)

        with self.narrate("That p-value comes from one number, z. It's the gap between the two "
                          "click rates, divided by the noise you'd expect in that gap.") as beat:
            self.play(FadeOut(question), FadeOut(rule), FadeOut(rate_a), FadeOut(rate_b),
                      FadeOut(rate_lbl), FadeOut(looks_lbl),
                      Transform(head, mini),
                      promise.animate.scale(0.8).move_to([PANEL_X, 0.75, 0]),
                      run_time=1.0)
            self.play(Create(ax), FadeIn(ynums), FadeIn(ax.y_title), FadeIn(ax.x_title),
                      ReplacementTransform(looks, day_marks), Create(zero),
                      run_time=beat.until("z", offset=-0.1))
            self.play(Write(zf[0:2]), run_time=0.6)
            beat.wait_until("gap", offset=-0.2)
            self.play(TransformFromCopy(head[0][1][1], zf[2]), TransformFromCopy(head[0][0][1], zf[4]),
                      Write(zf[3]), run_time=1.2)
            beat.wait_until("noise", offset=-0.2)
            self.play(Write(zf[5]), Write(zf[6]), run_time=0.9)

        up_line = Line(self.P(0.3, ZC), self.P(20.4, ZC), color=YELLOW, stroke_width=3)
        lo_line = Line(self.P(0.3, -ZC), self.P(20.4, -ZC), color=YELLOW, stroke_width=3)
        up_lbl = formula(r"+1.96", size=MATH_SMALL, color=YELLOW).next_to(up_line, RIGHT, buff=0.12)
        lo_lbl = formula(r"-1.96", size=MATH_SMALL, color=YELLOW).next_to(lo_line, RIGHT, buff=0.12)
        with self.narrate("P below point oh five means z has escaped these two lines, at plus "
                          "and minus one point nine six.") as beat:
            beat.wait_until("these", offset=-0.15)
            self.play(Create(up_line), Create(lo_line), run_time=beat.until("plus", offset=-0.1))
            self.play(FadeIn(up_lbl, shift=0.1 * LEFT), FadeIn(lo_lbl, shift=0.1 * LEFT),
                      run_time=0.8)

        # ---- one simulated test, day by day
        hz = Z[HERO]
        hero_pts = [self.P(d, hz[d - 1]) for d in range(1, DAYS + 1)]
        hero_dots = VGroup(*[Dot(p, radius=0.07, color=BLUE) for p in hero_pts])
        segs = VGroup(*[Line(hero_pts[k], hero_pts[k + 1], color=BLUE, stroke_width=3.5)
                        for k in range(DAYS - 1)])
        sim_tag = label("simulated", size=SMALL, color=GRAY).move_to(self.P(18, 4.55))
        with self.narrate("Here is one simulated test, with five hundred visitors per button "
                          "each day. Day one, day two, still inside.") as beat:
            self.play(FadeIn(sim_tag), run_time=beat.until("Day one", offset=-0.15))
            self.play(FadeIn(hero_dots[0], scale=0.5), run_time=0.5)
            beat.wait_until("day two", offset=-0.15)
            self.play(Create(segs[0]), FadeIn(hero_dots[1]), run_time=0.5)
            rest = beat.remaining() - 0.1
            self.play(LaggedStart(*[AnimationGroup(Create(segs[k]), FadeIn(hero_dots[k + 1]))
                                    for k in range(1, 5)], lag_ratio=1.0),
                      run_time=max(rest, 1.2), rate_func=linear)

        win_dot = hero_dots[6]
        p_tag = formula(r"p = 0.04", size=MATH_SMALL, color=RED).next_to(win_dot, UP, buff=0.22)
        stop_tag = label("stop: B wins", size=LABEL, color=RED)
        with self.narrate("On day seven, z pokes above the line. P is point oh four. You stop, "
                          "and ship button B.") as beat:
            self.play(Create(segs[5]), FadeIn(hero_dots[6]), run_time=beat.until("pokes", offset=0.2))
            self.play(win_dot.animate.set_color(RED).scale(1.4), segs[5].animate.set_color(RED),
                      run_time=0.6)
            beat.wait_until("P is", offset=-0.15)
            self.play(FadeIn(p_tag, shift=0.1 * UP), run_time=0.6)
            stop_tag.next_to(p_tag, RIGHT, buff=0.3)
            beat.wait_until("stop", offset=-0.1)
            self.play(FadeIn(stop_tag, shift=0.1 * UP), run_time=0.6)
            beat.wait_until("ship", offset=-0.1)
            ring = SurroundingRectangle(head[0][1][0], color=RED, buff=0.05, corner_radius=0.1)
            self.play(Create(ring), run_time=0.7)

        later = VGroup(*segs[6:], *hero_dots[7:])
        end_lbl = label("no winner", size=LABEL, color=GRAY)
        with self.narrate("Had you kept going, this same test would have drifted back and "
                          "finished day twenty inside the lines. No winner.") as beat:
            self.play(dim(stop_tag, p_tag, opacity=0.35), FadeOut(ring), run_time=0.6)
            for m in later:
                m.set_color(GRAY)
            self.play(LaggedStart(*[AnimationGroup(Create(segs[k]), FadeIn(hero_dots[k + 1]))
                                    for k in range(6, DAYS - 1)], lag_ratio=1.0),
                      run_time=beat.until("No winner", offset=-0.3), rate_func=linear)
            end_lbl.next_to(hero_dots[-1], DOWN, buff=0.25).shift(LEFT * 0.4)
            self.play(FadeIn(end_lbl, shift=0.1 * UP), flag(hero_dots[-1], color=INK), run_time=0.8)

        # ============================================================ FAIL: 1,000 tests
        paths, cdots = self.make_paths(FIRST, skip={HERO})
        hero_red = VGroup(*segs[:6]).copy()
        hero_red.set_stroke(RED, width=1.4, opacity=0.7)
        hero_cross = Dot(hero_pts[6], radius=0.055, color=RED)
        hero_cross.day = 7
        hero_cross.test = HERO
        allow_overlap(hero_red)
        day = ValueTracker(1)

        peek_lbl = label("peek daily", color=GRAY)
        peek_num = DecimalNumber(0, num_decimal_places=1, font_size=EQ * 0.8, color=RED,
                                 unit=r"\%")
        peek_row = VGroup(peek_lbl, peek_num).arrange(RIGHT, buff=0.3)
        peek_row.move_to([PANEL_X, -0.35, 0])
        peek_num.add_updater(lambda m: m.set_value(
            100 * ((FIRST >= 0) & (FIRST + 1 <= day.get_value() + 1e-6)).sum() / T))

        with self.narrate("Now run a thousand of these tests, every one between identical "
                          "buttons, and stop each one at its first crossing.") as beat:
            self.play(FadeOut(VGroup(*segs, *hero_dots)), FadeOut(stop_tag), FadeOut(p_tag),
                      FadeOut(end_lbl), FadeOut(zf), FadeIn(hero_red), FadeIn(hero_cross),
                      FadeIn(peek_row), run_time=1.0)
            self.add(paths, cdots)
            self.sweep(paths, cdots, day, run_time=beat.remaining() + 0.2)
        peek_num.clear_updaters()
        peek_num.set_value(100 * N_PEEK / T)
        all_cross = VGroup(*cdots, hero_cross)

        times5 = formula(r"\times 5", size=MATH, color=GRAY)
        with self.narrate("Two hundred and forty nine of them crown a winner. That's twenty "
                          "five percent, five times the promise.") as beat:
            self.play(flag(peek_num, color=RED), run_time=0.9)
            beat.wait_until("five times", offset=-0.2)
            times5.next_to(peek_row, UP, buff=0.12).align_to(peek_num, LEFT)
            self.play(FadeIn(times5, shift=0.2 * UP), flag(promise_frac[2], color=YELLOW),
                      run_time=0.9)

        once_idx = np.where(np.abs(Z[:, -1]) > ZC)[0]
        once_dots = VGroup(*[Dot(self.P(20, Z[i, -1]), radius=0.06, color=RED) for i in once_idx])
        allow_overlap(once_dots)
        once_lbl = label("one look", color=GRAY)
        once_num = formula(f"{100 * N_ONCE / T:.1f}" + r"\%", size=EQ * 0.8, color=RED)
        once_row = VGroup(once_lbl, once_num).arrange(RIGHT, buff=0.3)
        once_row.next_to(peek_row, DOWN, buff=0.5).align_to(peek_row, RIGHT)
        with self.narrate("Check only once, on day twenty, and just fifty two land outside "
                          "the lines.") as beat:
            self.play(FadeOut(times5), dim(paths, hero_red, opacity=0.12),
                      all_cross.animate.set_opacity(0.25),
                      run_time=beat.until("day twenty", offset=-0.1))
            self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in once_dots], lag_ratio=0.05),
                      run_time=beat.until("fifty", offset=-0.1))
            self.play(FadeIn(once_row, shift=0.1 * UP), run_time=0.8)

        order = sorted(range(len(all_cross)), key=lambda k: all_cross[k].day)
        with self.narrate("No single p-value lied. But every check is another chance to touch "
                          "a line, and one touch is enough.") as beat:
            self.play(FadeOut(once_dots), dim(once_row, opacity=0.35),
                      paths.animate.set_stroke(opacity=0.22), hero_red.animate.set_stroke(opacity=0.22),
                      run_time=beat.until("every check", offset=-0.1))
            self.play(LaggedStart(*[all_cross[k].animate.set_opacity(1).scale(1.3)
                                    for k in order], lag_ratio=0.01),
                      run_time=beat.until("one touch", offset=-0.1))
            self.play(flag(up_line, color=YELLOW), flag(lo_line, color=YELLOW), run_time=0.9)

        # ============================================================ INSIGHT
        def stack(counts, x):
            g, y = VGroup(), BAR_BOTTOM
            for c in counts:
                h = max(c * PCT * 100 / T, 0.001)
                r = Rectangle(width=BAR_W, height=h, stroke_color=BG, stroke_width=1.5,
                              fill_color=RED, fill_opacity=0.9)
                r.move_to([x, y + h / 2, 0])
                g.add(r)
                y += c * PCT * 100 / T
            return g

        bar1 = stack(SLICES, BAR1_X)
        groups = [VGroup(*[d for d in all_cross if d.day == k + 1]) for k in range(DAYS)]
        with self.narrate("Sort the winners by the day they first crossed.") as beat:
            self.play(FadeOut(once_row), FadeOut(head), FadeOut(promise_lbl),
                      promise_frac.animate.move_to([PANEL_X, 2.5, 0]),
                      peek_lbl.animate.set_opacity(0),
                      peek_num.animate.scale(0.8).next_to(bar1, UP, buff=0.18),
                      run_time=0.9)
            self.remove(peek_lbl)
            self.play(LaggedStart(*[ReplacementTransform(groups[k], bar1[k])
                                    for k in range(DAYS)], lag_ratio=0.12),
                      run_time=beat.remaining() + 0.6)

        a1 = formula(r"\alpha_1", size=MATH, color=RED).next_to(bar1[0], RIGHT, buff=0.2)
        a2 = formula(r"\alpha_2", size=MATH, color=RED).next_to(bar1[1], RIGHT, buff=0.2)
        a2.shift(UP * 0.12)
        share = VGroup(*[Line(self.P(d, -4), self.P(d, 4), color=GRAY, stroke_width=2)
                         for d in (10, 11)])
        share_lbl = label("10 of 11 days shared", size=LABEL, color=GRAY)
        share_lbl.next_to(share, UP, buff=0.12)
        with self.narrate("Day one takes about five percent. Day two adds three more. Later "
                          "days add less and less, because day eleven's z is built mostly "
                          "from day ten's visitors.") as beat:
            self.play(flag(bar1[0], color=RED), FadeIn(a1, shift=0.1 * LEFT),
                      run_time=beat.until("Day two", offset=-0.1))
            self.play(flag(bar1[1], color=RED), FadeIn(a2, shift=0.1 * LEFT), run_time=0.8)
            beat.wait_until("Later", offset=-0.1)
            self.play(LaggedStart(*[bar1[k].animate.set_fill(INK) for k in range(2, DAYS)],
                                  lag_ratio=0.15), run_time=1.6)
            self.play(*[bar1[k].animate.set_fill(RED) for k in range(2, DAYS)], run_time=0.6)
            beat.wait_until("eleven", offset=-0.3)
            self.play(FadeOut(sim_tag), Create(share), FadeIn(share_lbl, shift=0.1 * DOWN),
                      run_time=1.0)

        alpha = MathTex(r"\alpha_1", "+", r"\alpha_2", "+", r"\cdots", "+", r"\alpha_{20}", "=",
                        r"24.9\%", font_size=EQ)
        alpha.move_to([0.6, 3.15, 0])
        for k in (0, 2, 6, 8):
            alpha[k].set_color(RED)
        with self.narrate("Stacked up, alpha one plus alpha two, all the way to alpha twenty, "
                          "comes to twenty five percent.") as beat:
            self.play(FadeOut(share), FadeOut(share_lbl),
                      promise_frac.animate.move_to([PANEL_X + 0.1, 2.0, 0]),
                      run_time=beat.until("alpha one", offset=-0.2))
            self.play(TransformFromCopy(a1, alpha[0]), run_time=0.7)
            self.play(Write(alpha[1]), TransformFromCopy(a2, alpha[2]),
                      run_time=beat.until("all the way", offset=-0.1))
            self.play(Write(alpha[3:6]), TransformFromCopy(VGroup(*bar1[2:]), alpha[6]),
                      run_time=beat.until("comes", offset=-0.1))
            self.play(Write(alpha[7]), TransformFromCopy(peek_num, alpha[8]), run_time=1.0)

        budget = DashedLine([BAR1_X - 0.6, BAR_BOTTOM + 5 * PCT, 0],
                            [BAR2_X + 0.6, BAR_BOTTOM + 5 * PCT, 0], color=YELLOW,
                            stroke_width=3, dash_length=0.12)
        budget_lbl = formula(r"5\%", size=MATH_SMALL, color=YELLOW)
        budget_lbl.move_to([(BAR1_X + BAR2_X) / 2, BAR_BOTTOM + 5 * PCT + 0.28, 0])
        with self.narrate("The promise allows five percent in total. How would you spend it "
                          "across twenty looks? [pause 1.5]") as beat:
            self.play(Create(budget), ReplacementTransform(promise_frac, budget_lbl),
                      run_time=beat.until("total", offset=0.2))
            beat.wait_until("spend", offset=-0.1)
            self.play(flag(budget, color=YELLOW), flag(budget_lbl, color=YELLOW), run_time=0.9)

        # ---- reshape the boundary: O'Brien-Fleming funnel
        t0 = 20 * (OBF_C / 4.0) ** 2           # day where the funnel enters the chart top
        def funnel(sign):
            ts = np.linspace(t0, 20.4, 60)
            return VMobject(stroke_color=GREEN, stroke_width=3.5).set_points_smoothly(
                [self.P(t, sign * min(4.0, OBF_C * np.sqrt(20 / t))) for t in ts])
        f_up, f_lo = funnel(1), funnel(-1)
        ghost = VGroup(up_line.copy(), lo_line.copy()).set_stroke(opacity=0.3)
        ob_lbl = label("O'Brien–Fleming boundary", size=LABEL, color=GREEN)
        ob_lbl.move_to(self.P(9.5, 4.5))
        cite_ob = citation("O'Brien & Fleming, 1979 · Biometrics")
        with self.narrate("Spend almost nothing early. Make the lines very wide on the first "
                          "days, and narrow them toward the end. This funnel is the O'Brien "
                          "Fleming boundary, from clinical trials.") as beat:
            self.play(FadeOut(paths), FadeOut(hero_red), FadeOut(hero_cross),
                      run_time=beat.until("very wide", offset=-0.3))
            self.add(ghost)
            self.play(Transform(up_line, f_up), Transform(lo_line, f_lo),
                      up_lbl.animate.set_opacity(0.3), lo_lbl.animate.set_opacity(0.3),
                      run_time=beat.until("This funnel", offset=-0.2))
            self.play(FadeIn(ob_lbl, shift=0.1 * DOWN), FadeIn(cite_ob), run_time=0.9)

        paths2, cdots2 = self.make_paths(FIRST_OBF)
        bar2 = stack(SLICES_OBF, BAR2_X)
        for r in bar2:
            r.set_fill(opacity=0)
            r.set_stroke(opacity=0)
        day2 = ValueTracker(1)
        obf_num = DecimalNumber(0, num_decimal_places=1, font_size=EQ * 0.64, color=RED, unit=r"\%")
        obf_num.next_to(bar2, UP, buff=0.18)
        obf_num.add_updater(lambda m: m.set_value(
            100 * ((FIRST_OBF >= 0) & (FIRST_OBF + 1 <= day2.get_value() + 1e-6)).sum() / T)
            .next_to([BAR2_X, BAR_BOTTOM + max(m.get_value(), 0.01) * PCT, 0], UP, buff=0.18))
        lbl1 = formula(r"\pm 1.96", size=MATH_SMALL, color=YELLOW).next_to(bar1, DOWN, buff=0.2)
        lbl2 = label("funnel", size=SMALL + 4, color=GREEN).next_to(
            [BAR2_X, BAR_BOTTOM, 0], DOWN, buff=0.2)
        lbl2.align_to(lbl1, UP)

        def bar2_upd(_):
            d = day2.get_value()
            for k, r in enumerate(bar2):
                on = d >= k + 1 - 1e-6 and SLICES_OBF[k] > 0
                r.set_fill(RED, opacity=0.9 if on else 0)
                r.set_stroke(BG, opacity=1 if on else 0)

        alpha_new = MathTex(r"\alpha_1", "+", r"\alpha_2", "+", r"\cdots", "+", r"\alpha_{20}",
                            "=", r"4.9\%", font_size=EQ).move_to(alpha)
        for k in (0, 2, 6, 8):
            alpha_new[k].set_color(RED)
        with self.narrate("Run the same thousand tests again. Forty nine winners. Five percent, "
                          "with twenty looks.") as beat:
            self.play(FadeOut(cite_ob), dim(bar1, peek_num, opacity=0.35),
                      FadeIn(lbl1), FadeIn(lbl2), run_time=0.7)
            self.add(paths2, cdots2, bar2, obf_num)
            self.sweep(paths2, cdots2, day2, run_time=beat.until("Forty", offset=-0.2),
                       extra=[UpdateFromFunc(bar2, bar2_upd)])
            obf_num.clear_updaters()
            self.play(flag(obf_num, color=RED), run_time=0.8)
            beat.wait_until("Five percent", offset=-0.2)
            self.play(TransformMatchingTex(alpha, alpha_new), run_time=1.0)

        new_up = formula(r"2.13", size=MATH_SMALL, color=GREEN)
        with self.narrate("The price is small. On day twenty, z must pass two point one three "
                          "instead of one point nine six.") as beat:
            beat.wait_until("day twenty", offset=-0.2)
            self.play(paths2.animate.set_stroke(opacity=0.15),
                      up_lbl.animate.set_opacity(1).shift(DOWN * 0.22),
                      run_time=0.6)
            new_up.next_to(up_lbl, UP, buff=0.12).align_to(up_lbl, LEFT)
            mark = Dot(self.P(20, OBF[-1]), radius=0.08, color=GREEN)
            beat.wait_until("two point", offset=-0.2)
            self.play(FadeIn(new_up, shift=0.1 * DOWN), FadeIn(mark, scale=0.5), run_time=0.8)
            beat.wait_until("instead", offset=-0.1)
            self.play(flag(up_lbl, color=YELLOW), run_time=0.9)

        # ============================================================ PAYOFF
        looks_n = [1, 2, 5, 10, 20, 100]
        rates = [5.0, 8.3, 14.2, 19.3, 24.8, 37.4]
        ax2 = axes((-0.6, 5.6), (0, 40), x_length=8.0, y_length=4.4, x_ticks=list(range(6)),
                   y_ticks=[0, 10, 20, 30, 40], x_label="looks at the data",
                   y_label="false winners (%)")
        ax2.move_to([-0.9, 0.05, 0])
        ax2.x_axis.remove(ax2.x_axis.numbers)
        xn = VGroup(*[formula(str(n), size=MATH_SMALL, color=GRAY).next_to(ax2.c2p(i, 0), DOWN,
                                                                             buff=0.18)
                      for i, n in enumerate(looks_n)])
        ax2.remove(ax2.x_title)
        ax2.x_title.next_to(xn, DOWN, buff=0.15).align_to(ax2.x_axis, RIGHT)
        bw = 0.62 * ax2.x_axis.unit_size
        bars = VGroup(*[Rectangle(width=bw, height=r * ax2.y_axis.unit_size, stroke_width=0,
                                  fill_color=RED, fill_opacity=0.9)
                        .move_to(ax2.c2p(i, 0), aligned_edge=DOWN) for i, r in enumerate(rates)])
        vals = VGroup(*[formula(f"{round(r)}" + r"\%", size=MATH_SMALL, color=INK)
                        .next_to(b, UP, buff=0.12) for b, r in zip(bars, rates)])
        prom = DashedLine(ax2.c2p(-0.6, 5), ax2.c2p(5.6, 5), color=YELLOW, stroke_width=3,
                          dash_length=0.12)
        prom_lbl = formula(r"5\%", size=MATH_SMALL, color=YELLOW).next_to(prom, RIGHT, buff=0.12)
        cite_arm = citation("Armitage, McPherson & Rowe, 1969 · J. Royal Statistical Society A")
        with self.narrate("Medical statisticians mapped this trap decades before A B tests. "
                          "In nineteen sixty nine, Armitage, McPherson and Rowe calculated how "
                          "fast it grows: five looks give fourteen percent, twenty give twenty "
                          "five, a hundred give thirty seven.") as beat:
            keep = VGroup(bar1, budget, budget_lbl)
            others = [m for m in self.mobjects if m not in (bar1, budget, budget_lbl)]
            self.play(*[FadeOut(m) for m in others], run_time=1.0)
            self.play(Create(ax2), FadeIn(xn), ReplacementTransform(bar1, bars[4]),
                      ReplacementTransform(budget, prom), ReplacementTransform(budget_lbl, prom_lbl),
                      run_time=beat.until("nineteen", offset=-0.2))
            self.play(LaggedStart(*[GrowFromEdge(bars[i], DOWN) for i in (0, 1, 2, 3, 5)],
                                  lag_ratio=0.2), FadeIn(cite_arm),
                      run_time=beat.until("calculated"))
            self.play(LaggedStart(*[FadeIn(v, shift=0.1 * UP) for v in vals], lag_ratio=0.15),
                      run_time=beat.until("five looks", offset=-0.1))
            for i, w in ((2, "five looks"), (4, "twenty give"), (5, "a hundred")):
                beat.wait_until(w, offset=-0.1)
                self.play(flag(bars[i], color=RED), flag(vals[i], color=INK), run_time=0.8)

        cite_jo = citation("Johari, Koomen, Pekelis & Walsh, 2017 · KDD")
        valid = VGroup(*[Rectangle(width=bw * 0.9, height=5 * ax2.y_axis.unit_size,
                                   stroke_color=GREEN, stroke_width=3, fill_opacity=0)
                         .move_to(b.get_bottom(), aligned_edge=DOWN) for b in bars])
        valid_lbl = label("always-valid p-values: at most 5%", size=LABEL, color=GREEN)
        valid_lbl.move_to(ax2.c2p(1.4, 30))
        with self.narrate("In twenty seventeen, Johari and colleagues, working with the testing "
                          "company Optimizely, built p-values that stay valid however often you "
                          "look.") as beat:
            self.play(FadeOut(cite_arm), FadeIn(cite_jo), bars.animate.set_fill(opacity=0.35),
                      run_time=beat.until("built", offset=-0.2))
            self.play(LaggedStart(*[Create(v) for v in valid], lag_ratio=0.15),
                      FadeIn(valid_lbl, shift=0.1 * UP), run_time=beat.until("however"))
            self.play(LaggedStart(*[flag(v, color=GREEN) for v in valid], lag_ratio=0.15),
                      run_time=1.4)

        # ============================================================ LANDING
        btn_a2, btn_b2 = button("A"), button("B")
        btns2 = VGroup(btn_a2, btn_b2).arrange(RIGHT, buff=1.6).move_to(UP * 1.6)
        eq2 = formula("=", size=60).move_to(VGroup(btn_a2.body, btn_b2.body).get_center())
        looks2 = VGroup(*[Circle(radius=0.13, stroke_color=GRAY, stroke_width=2.5,
                                 fill_color=INK, fill_opacity=0) for _ in range(DAYS)])
        looks2.arrange(RIGHT, buff=0.24).move_to(DOWN * 0.6)
        with self.narrate("Looking is harmless. Stopping because of what you saw is what spends "
                          "the budget.") as beat:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)
            self.play(FadeIn(btns2), FadeIn(eq2), LaggedStart(*[Create(c) for c in looks2],
                                                              lag_ratio=0.05),
                      run_time=beat.until("Stopping", offset=-0.6))
            self.play(LaggedStart(*[c.animate.set_fill(INK, opacity=0.85) for c in looks2[:7]],
                                  lag_ratio=0.3), run_time=beat.until("what you saw", offset=-0.1))
            self.play(looks2[6].animate.set_fill(RED, opacity=1).set_stroke(RED),
                      *[c.animate.set_stroke(opacity=0.3) for c in looks2[7:]],
                      run_time=0.8)

        wins = label("B wins", size=LABEL, color=RED).next_to(btn_b2.body, DOWN, buff=0.3)
        with self.narrate("These two buttons never differed. They just got twenty chances to "
                          "look like they did.") as beat:
            self.play(flag(eq2, color=INK), FadeIn(wins, shift=0.1 * UP),
                      run_time=beat.until("twenty", offset=-0.2))
            self.play(LaggedStart(*[c.animate.set_stroke(GRAY, opacity=1).set_fill(INK, opacity=0.85)
                                    for c in looks2[7:]], lag_ratio=0.15),
                      run_time=beat.remaining())
        self.end_card()
