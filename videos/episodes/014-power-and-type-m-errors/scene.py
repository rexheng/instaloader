"""Episode 14 - Why Small Studies Find Huge Effects (Type M errors).

    videos/toolkit/render.sh --preview videos/episodes/014-power-and-type-m-errors/scene.py Episode /tmp/ep14.mp4
"""
from math import erf, exp, log, sqrt, pi

import numpy as np
from manim import *
from sample_space import *

# ----------------------------------------------------------------------------- data
D = 0.2                      # true effect (SD units)
N0 = 20                      # per group
SE0 = sqrt(2 / N0)
Z = 1.96
RNG = np.random.default_rng(13)
EST = RNG.normal(D, SE0, 1000)            # simulated: one estimate per lab
SIG = np.abs(EST) > Z * SE0               # 97 significant, 6 with the wrong sign
BIN = 0.04


def Phi(x):
    return 0.5 * (1 + erf(x / sqrt(2)))


def phi(x):
    return exp(-x * x / 2) / sqrt(2 * pi)


def design(n, d=D):
    """power, Type-S rate, E[signed significant estimate]/d for n per group (normal model)."""
    s = sqrt(2 / n)
    w = Z * s
    pu, pl = 1 - Phi((w - d) / s), Phi((-w - d) / s)
    mu_up = d + s * phi((w - d) / s) / max(pu, 1e-12)
    mu_lo = d - s * phi((-w - d) / s) / max(pl, 1e-300)
    p = pu + pl
    return p, pl / p, (pu * mu_up + pl * mu_lo) / p / d


AX_Y = -1.7
TILE_W, TILE_H, PITCH = 0.145, 0.05, 0.065
BELL_H = 1000 * BIN * PITCH / (SE0 * sqrt(2 * pi))     # histogram-matched peak height


class Episode(NarratedScene):
    EPISODE = 14
    TITLE = "Why Small Studies Find Huge Effects"
    PRONUNCIATIONS = {"Carlin": "car lin", "Gelman": "gell man"}

    # ------------------------------------------------------------------ builders
    def make_axis(self, lo, hi, step, title_s, length=10.5, x0=-4.5):
        nl = NumberLine(x_range=[lo, hi, step], length=length, color=GRAY, stroke_width=2.5,
                        include_numbers=False, tick_size=0.07)
        nl.move_to([x0 + length / 2, AX_Y, 0])
        nums = VGroup()
        v = lo
        while v <= hi + 1e-9:
            s = f"{v:g}"
            m = MathTex(s.replace("-", "-"), font_size=MATH_SMALL, color=GRAY)
            m.next_to(nl.n2p(v), DOWN, buff=0.2)
            nums.add(m)
            v += step
        ttl = text(title_s, size=LABEL, color=GRAY)
        ttl.next_to(nums, DOWN, buff=0.15).align_to(nl.get_right(), RIGHT)
        return VGroup(nl, nums, ttl)

    def bell_path(self, nl, center, s, height, lo, hi, x_from=None, x_to=None):
        a = lo if x_from is None else max(lo, x_from)
        b = hi if x_to is None else min(hi, x_to)
        xs = np.linspace(a, b, 160)
        pts = [nl.n2p(x) + UP * (height * exp(-0.5 * ((x - center) / s) ** 2)) for x in xs]
        return pts

    # ------------------------------------------------------------------ scene
    def construct(self):
        axis = self.make_axis(-1, 1.5, 0.5, "estimated effect (standard deviations)")
        nl = axis[0]
        unit = nl.n2p(1)[0] - nl.n2p(0)[0]

        def X(v):
            return nl.n2p(v)

        top_y = AX_Y + 0.05 + 66 * PITCH + 0.1           # just above the tallest stack
        truth = Line(X(D), X(D) + UP * (top_y - AX_Y + 0.15), color=GREEN, stroke_width=4)
        truth_lbl = MathTex(r"\text{true effect } 0.2", font_size=MATH, color=GREEN)
        truth_lbl.next_to(truth, UP, buff=0.15)

        # cold-open context
        setup = VGroup(
            MathTex(r"1000\text{ labs}", font_size=MATH),
            MathTex(r"20\text{ people per group}", font_size=MATH),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        setup.to_corner(UL, buff=0).move_to([-6.4 + setup.width / 2, 3.1 - setup.height / 2 + 0.25, 0])
        q = MathTex(r"\text{printed average} = \,?", font_size=MATH, color=YELLOW)
        q.move_to([6.4 - q.width / 2, 3.2, 0])

        # ---------------------------------------------------------- B0 cold open
        with self.narrate("The true effect of this treatment is small: point two. A thousand "
                          "small labs test it, and journals print only the significant "
                          "results. On average, what effect do the printed studies report? "
                          "[pause 1.5]") as beat:
            self.play(Create(nl), FadeIn(axis[1]), run_time=0.8)
            self.play(Create(truth), Write(truth_lbl), FadeIn(axis[2]),
                      run_time=beat.until("thousand", offset=-0.1))
            self.play(FadeIn(setup[0], shift=0.2 * RIGHT), run_time=0.8)
            self.play(FadeIn(setup[1], shift=0.2 * RIGHT), run_time=0.8)
            beat.wait_until("printed", offset=-0.2)
            self.play(Write(q), run_time=1.0)
            beat.wait_until("report", offset=0.2)
            self.play(Indicate(q[0][-1], color=YELLOW, scale_factor=1.3), run_time=1.0)

        # ---------------------------------------------------------- B1 stakes
        guess = MathTex(r"0.2?", font_size=MATH, color=GRAY)
        guess.next_to(truth_lbl, RIGHT, buff=0.4)
        with self.narrate("Point two is a fair guess, maybe a little more. Reviews, guidelines "
                          "and the next lab's sample size are all built on that printed "
                          "number.") as beat:
            self.play(FadeIn(guess, shift=0.2 * UP), run_time=0.8)
            beat.wait_until("Reviews", offset=-0.1)
            self.play(flag(q), run_time=1.0)
            beat.wait_until("printed", offset=-0.1)
            self.play(Circumscribe(q, color=YELLOW, buff=0.12), run_time=1.2)

        # ---------------------------------------------------------- B2 naive build
        counts = {}
        tiles = VGroup()
        for i, e in enumerate(EST):
            b = int(np.floor(e / BIN))
            k = counts.get(b, 0)
            counts[b] = k + 1
            xc = (b + 0.5) * BIN
            r = Rectangle(width=TILE_W, height=TILE_H, stroke_width=0, fill_color=BLUE,
                          fill_opacity=0.9)
            r.move_to(X(xc) + UP * (0.05 + TILE_H / 2 + k * PITCH))
            tiles.add(r)
        sim_tag = text("simulated", size=SMALL, color=GRAY)
        sim_tag.move_to([-6.4 + sim_tag.width / 2, CONTENT_BOTTOM + 0.08 + sim_tag.height / 2, 0])
        one = int(np.argmax(EST))
        one_box = SurroundingRectangle(tiles[one], color=INK, buff=0.07, stroke_width=2.5)
        one_lbl = text("one lab", size=LABEL).next_to(one_box, UP, buff=0.15)
        one_lbl.shift(LEFT * 0.35)

        with self.narrate("So run it. Each lab gives twenty people the treatment and twenty a "
                          "placebo, and measures the difference. Each block on this line is "
                          "one lab's estimate.") as beat:
            self.play(FadeOut(guess), FadeIn(sim_tag), run_time=0.6)
            self.play(LaggedStart(*[FadeIn(t, shift=DOWN * 0.6) for t in tiles],
                                  lag_ratio=0.006),
                      run_time=beat.until("Each block", offset=-0.1))
            self.play(Create(one_box), FadeIn(one_lbl), run_time=beat.until("estimate"))

        # ---------------------------------------------------------- B3 spread + mean
        lo_v, hi_v = float(EST.min()), float(EST.max())
        span = DoubleArrow(X(lo_v) + DOWN * 0.0 + UP * 0.9, X(hi_v) + UP * 0.9, buff=0,
                           color=GRAY, stroke_width=2.5, tip_length=0.18)
        allmean = MathTex(r"\text{mean of all } 1000 = 0.20", font_size=MATH, color=BLUE)
        allmean.move_to([-6.4 + allmean.width / 2, 3.2, 0])
        with self.narrate("Noise scatters them widely, from about minus point eight to plus "
                          "one and a half. But the pile is centred on the truth: all thousand "
                          "together average point two oh.") as beat:
            self.play(FadeOut(one_box), FadeOut(one_lbl), run_time=0.6)
            beat.wait_until("minus", offset=-0.3)
            self.play(GrowFromCenter(span), run_time=beat.until("But", offset=-0.2))
            self.play(FadeOut(span), flag(truth), run_time=beat.until("all thousand", offset=-0.1))
            self.play(FadeOut(setup), FadeIn(allmean, shift=0.2 * RIGHT),
                      run_time=beat.until("two oh", offset=0.4))

        # ---------------------------------------------------------- B4 filter
        W0 = Z * SE0
        wall_top = 1.3
        wall_l = Line(X(-W0), [X(-W0)[0], wall_top, 0], color=PURPLE, stroke_width=5)
        wall_r = Line(X(W0), [X(W0)[0], wall_top, 0], color=PURPLE, stroke_width=5)
        walls = VGroup(wall_l, wall_r)
        wall_lbl = MathTex(r"p<0.05", font_size=MATH_SMALL + 4, color=PURPLE)
        wall_lbl.next_to(wall_l, UP, buff=0.15)
        wall_lbl_r = wall_lbl.copy().next_to(wall_r, UP, buff=0.15)
        inside = VGroup(*[t for t, s in zip(tiles, SIG) if not s])
        outside_idx = [i for i in np.argsort(np.abs(EST)) if SIG[i]]
        outside = VGroup(*[tiles[i] for i in outside_idx])
        printed_n = ValueTracker(0)
        cnt = DecimalNumber(0, num_decimal_places=0, font_size=MATH, color=YELLOW)
        cnt_pre = MathTex(r"\text{printed: }", font_size=MATH, color=YELLOW)
        cnt_post = MathTex(r"\text{ of } 1000", font_size=MATH, color=YELLOW)
        cnt_row = VGroup(cnt_pre, cnt, cnt_post).arrange(RIGHT, buff=0.12)
        cnt_row.move_to([-6.4 + cnt_row.width / 2, 2.5, 0])
        cnt.add_updater(lambda m: m.set_value(round(printed_n.get_value())))

        with self.narrate("Now apply the filter. A result is significant only if it lands "
                          "beyond these walls. Ninety-seven of the thousand get through.") as beat:
            beat.wait_until("these walls", offset=-0.3)
            self.play(Create(walls), FadeIn(wall_lbl), FadeIn(wall_lbl_r), run_time=1.0)
            self.play(inside.animate.set_fill(opacity=0.22), run_time=0.9)
            self.add(cnt_row)
            self.play(LaggedStart(*[t.animate.set_fill(YELLOW, opacity=1) for t in outside],
                                  lag_ratio=0.03),
                      printed_n.animate.set_value(97),
                      FadeOut(q),
                      run_time=beat.until_end_of("through", offset=-0.05))
        cnt.clear_updaters()

        # ---------------------------------------------------------- B5 printed mean
        pm = float(EST[SIG].mean())
        avg_line = DashedLine(X(pm), [X(pm)[0], 2.15, 0], color=YELLOW, stroke_width=4,
                              dash_length=0.12)
        avg_lbl = MathTex(r"\text{printed average } 0.69", font_size=MATH, color=YELLOW)
        avg_lbl.next_to(avg_line, UP, buff=0.15)
        if avg_lbl.get_right()[0] > 6.4:
            avg_lbl.shift(LEFT * (avg_lbl.get_right()[0] - 6.4))
        ratio = MathTex(r"= 3.5\times\text{ true}", font_size=MATH, color=YELLOW)
        ratio.next_to(cnt_row, DOWN, buff=0.3, aligned_edge=LEFT)
        wrong = VGroup(*[tiles[i] for i in range(1000) if SIG[i] and EST[i] < 0])
        wrong_lbl = MathTex(r"6\text{ wrong sign}", font_size=MATH, color=YELLOW)
        wrong_lbl.move_to([-6.4 + wrong_lbl.width / 2, -0.75, 0])
        wrong_arrow = Arrow(wrong_lbl.get_bottom() + RIGHT * 0.6, wrong.get_top() + UP * 0.1,
                            buff=0.08, color=YELLOW, stroke_width=3, tip_length=0.18)

        with self.narrate("Their average is point six nine, three and a half times the true "
                          "effect. And six of them point the wrong way.") as beat:
            self.play(Create(avg_line), run_time=0.8)
            self.play(Write(avg_lbl), run_time=beat.until("three and", offset=-0.2))
            self.play(TransformFromCopy(avg_lbl[0][-4:], ratio), run_time=1.2)
            beat.wait_until("six of", offset=-0.2)
            self.play(FadeIn(wrong_lbl), GrowArrow(wrong_arrow),
                      LaggedStart(*[flag(t) for t in wrong], lag_ratio=0.1),
                      run_time=1.2)

        # ---------------------------------------------------------- B6 cause
        far_l = Arrow(X(0) + UP * 0.7, X(-0.55) + UP * 0.7, buff=0, color=GRAY, stroke_width=3,
                      tip_length=0.2)
        far_r = Arrow(X(0.45) + UP * 2.3, X(1.05) + UP * 0.9, buff=0, color=GRAY,
                      stroke_width=3, tip_length=0.2)
        with self.narrate("No lab made a mistake. The filter only lets through the estimates "
                          "that noise pushed far from zero.") as beat:
            self.play(FadeOut(wrong_arrow), FadeOut(wrong_lbl), run_time=0.6)
            beat.wait_until("lets through", offset=-0.2)
            self.play(LaggedStart(*[t.animate.set_fill(opacity=0.55) for t in outside],
                                  lag_ratio=0.01), run_time=0.6)
            self.play(LaggedStart(*[t.animate.set_fill(opacity=1) for t in outside],
                                  lag_ratio=0.01), run_time=0.6)
            beat.wait_until("noise", offset=-0.1)
            self.play(GrowArrow(far_r), run_time=beat.until("far", offset=0.1))
            self.play(GrowArrow(far_l), run_time=0.7)

        # ---------------------------------------------------------- B7 insight: SE and wall
        lo, hi = -1.0, 1.5
        bell = VMobject(color=BLUE, stroke_width=4)
        bell.set_points_smoothly(self.bell_path(nl, D, SE0, BELL_H, lo, hi))
        se_y = AX_Y + BELL_H * exp(-0.5)
        se_br = BraceBetweenPoints(X(D) + UP * (se_y - AX_Y), X(D + SE0) + UP * (se_y - AX_Y),
                                   direction=UP, color=INK)
        se_tag = MathTex(r"\text{SE}", font_size=MATH, color=INK).next_to(se_br, UP, buff=0.1)

        eq1 = MathTex(r"\text{SE}", "=", r"\sqrt{2/20}", "=", "0.32", font_size=MATH + 4)
        eq2 = MathTex(r"\text{wall}", "=", "1.96", r"\times", r"\text{SE}", "=", "0.62",
                      font_size=MATH + 4)
        eq2[0].set_color(PURPLE)
        eq2[6].set_color(PURPLE)
        eqs = VGroup(eq1, eq2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        eqs.move_to([6.4 - eqs.width / 2, 2.85, 0])

        with self.narrate("So where do the walls sit? A single lab's typical error, its "
                          "standard error, is the square root of two over twenty: point three "
                          "two. Significance needs one point nine six of those, so the wall "
                          "stands at point six two.") as beat:
            self.play(FadeOut(far_l), FadeOut(far_r), FadeOut(avg_lbl), Create(bell),
                      tiles.animate.set_fill(opacity=0.12), run_time=1.6)
            beat.wait_until("typical", offset=-0.2)
            self.play(GrowFromCenter(se_br), FadeIn(se_tag), run_time=0.9)
            beat.wait_until("standard error", offset=0.1)
            self.play(TransformFromCopy(se_tag, eq1[0]), Write(eq1[1]), run_time=1.0)
            self.play(Write(eq1[2]), run_time=beat.until("point three", offset=-0.1))
            self.play(Write(eq1[3:]), run_time=0.8)
            beat.wait_until("one point", offset=-0.2)
            self.play(TransformFromCopy(VGroup(wall_lbl_r), eq2[0]), Write(eq2[1:3]),
                      run_time=1.0)
            self.play(Write(eq2[3]), TransformFromCopy(eq1[0], eq2[4]), run_time=0.9)
            # the wall is literally 1.96 SE-brackets away from zero
            ruler = VGroup(*[
                Line(X(k * SE0) + UP * 0.35, X(min((k + 1) * SE0, W0)) + UP * 0.35,
                     color=INK, stroke_width=4)
                for k in range(2)])
            beat.wait_until("stands", offset=-0.3)
            self.play(Write(eq2[5:]), Create(ruler, lag_ratio=1), run_time=1.0)
            self.play(flag(wall_r, color=PURPLE), flag(eq2[6], color=PURPLE), run_time=0.8)

        # ---------------------------------------------------------- B8 truth is unprintable
        tri = Brace(Line(X(0), X(W0)), direction=DOWN, color=PURPLE)
        with self.narrate("That is the smallest effect this design can print, three times the "
                          "truth. The real answer, point two, sits inside the walls, where no "
                          "study of this size can print it.") as beat:
            self.play(FadeOut(ruler), FadeOut(se_br), FadeOut(se_tag), run_time=0.6)
            self.play(Indicate(wall_r, color=PURPLE, scale_factor=1.05), run_time=0.9)
            beat.wait_until("three times", offset=-0.2)
            self.play(Indicate(truth, color=GREEN), run_time=0.9)
            beat.wait_until("inside", offset=-0.2)
            band = Rectangle(width=X(W0)[0] - X(-W0)[0], height=wall_top - AX_Y,
                             stroke_width=0, fill_color=PURPLE, fill_opacity=0.12)
            band.move_to([X(0)[0], (wall_top + AX_Y) / 2, 0])
            self.play(FadeIn(band), Indicate(truth_lbl, color=GREEN), run_time=1.0)
            self.play(FadeOut(band), run_time=beat.remaining(min_time=0.6))

        # ---------------------------------------------------------- live model
        logn = ValueTracker(log(N0))

        def n_now():
            return exp(logn.get_value())

        def s_now():
            return sqrt(2 / n_now())

        def make_bell():
            return VMobject(color=BLUE, stroke_width=4).set_points_smoothly(
                self.bell_path(nl, D, s_now(), BELL_H, lo, hi))

        def tail(side):
            s = s_now()
            w = Z * s
            pts = (self.bell_path(nl, D, s, BELL_H, lo, hi, x_from=w) if side > 0 else
                   self.bell_path(nl, D, s, BELL_H, lo, hi, x_to=-w))
            if len(pts) < 2:
                return VMobject()
            base = [pts[-1][0], AX_Y, 0], [pts[0][0], AX_Y, 0]
            poly = Polygon(*pts, *base, stroke_width=0, fill_color=YELLOW, fill_opacity=0.55)
            return poly

        tail_r = tail(1)
        tail_l = tail(-1)
        new_eq = MathTex(r"\text{wall}", "=", "1.96", r"\times", r"\sqrt{2/n}",
                         font_size=MATH + 4)
        new_eq[0].set_color(PURPLE)
        new_eq.move_to(eq2, aligned_edge=LEFT)

        # readout panel (top-left), replacing the counters
        def readout(prefix, fn, dec, suffix=None, color=INK):
            pre = MathTex(prefix, font_size=MATH, color=color)
            num = DecimalNumber(fn(), num_decimal_places=dec, font_size=MATH, color=color)
            parts = [pre, num]
            if suffix:
                parts.append(MathTex(suffix, font_size=MATH, color=color))
            g = VGroup(*parts).arrange(RIGHT, buff=0.15)
            num.add_updater(lambda m: m.set_value(fn()))
            return g

        r_n = readout(r"n =", lambda: round(n_now()), 0, r"\text{ per group}")
        r_pow = readout(r"\text{power} =", lambda: round(100 * design(n_now())[0]), 0, r"\%")
        r_rat = readout(r"\text{printed} \div \text{true} =", lambda: design(n_now())[2], 1,
                        color=YELLOW)
        panel = VGroup(r_n, r_pow, r_rat).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        panel.move_to([-6.4 + panel.width / 2, 2.75, 0])

        # ---------------------------------------------------------- B9 prediction
        with self.narrate("Now give every lab four hundred people per group. Where do the "
                          "walls go? [pause 1.5]") as beat:
            self.play(FadeOut(eq1), TransformMatchingTex(eq2, new_eq),
                      FadeOut(allmean), FadeOut(cnt_row), FadeOut(ratio),
                      FadeIn(panel), FadeIn(tail_r), FadeIn(tail_l),
                      FadeOut(tiles), FadeOut(sim_tag), run_time=1.5)
            beat.wait_until("four hundred", offset=-0.2)
            n400 = MathTex(r"\to 400", font_size=MATH, color=INK).next_to(r_n, RIGHT, buff=0.2)
            self.play(FadeIn(n400, shift=0.2 * RIGHT), flag(new_eq[4]), run_time=1.0)
            beat.wait_until("walls go", offset=-0.1)
            self.play(Indicate(walls, color=PURPLE, scale_factor=1.05), run_time=1.0)

        # attach the live geometry
        bell.add_updater(lambda m: m.become(make_bell()))
        tail_r.add_updater(lambda m: m.become(tail(1)))
        tail_l.add_updater(lambda m: m.become(tail(-1)))
        wall_l.add_updater(lambda m: m.put_start_and_end_on(
            X(-Z * s_now()), [X(-Z * s_now())[0], wall_top, 0]))
        wall_r.add_updater(lambda m: m.put_start_and_end_on(
            X(Z * s_now()), [X(Z * s_now())[0], wall_top, 0]))
        wall_lbl.add_updater(lambda m: m.next_to(wall_l, UP, buff=0.15))
        wall_lbl_r.add_updater(lambda m: m.next_to(wall_r, UP, buff=0.15))
        avg_line.add_updater(lambda m: m.move_to(
            [X(D * design(n_now())[2])[0], m.get_center()[1], 0]))

        # ---------------------------------------------------------- B10 fix
        with self.narrate("Because the n sits under the square root, the bell narrows and the "
                          "walls close in. Near two hundred per group, they pass the truth. At "
                          "four hundred, power is eighty-one percent, and the printed average "
                          "is only twelve percent too high.") as beat:
            self.play(FadeOut(n400), flag(new_eq[4]), run_time=0.8)
            self.play(logn.animate.set_value(log(192)), rate_func=EASE,
                      run_time=beat.until("pass", offset=0.2))
            self.play(Indicate(truth, color=GREEN), run_time=0.8)
            self.play(logn.animate.set_value(log(400)), rate_func=EASE,
                      run_time=beat.until("power is", offset=-0.1))
            self.play(flag(r_pow), run_time=0.8)
            beat.wait_until("printed average", offset=-0.1)
            self.play(flag(r_rat), flag(avg_line), run_time=1.0)

        # ---------------------------------------------------------- B11 planning trap
        plan = MathTex(r"\text{plan for }", "0.69", r"\Rightarrow n = 33", font_size=MATH)
        plan[1].set_color(YELLOW)
        plan.next_to(panel, DOWN, buff=0.45, aligned_edge=LEFT)
        with self.narrate("But choosing that sample size needs a guess at the true effect. Plan "
                          "for the printed point six nine, and the standard formula says "
                          "thirty-three per group. Against the real point two, that study has "
                          "thirteen percent power.") as beat:
            beat.wait_until("Plan", offset=-0.2)
            self.play(Write(plan[0]), Write(plan[1]), run_time=1.0)
            beat.wait_until("thirty", offset=-0.2)
            self.play(Write(plan[2]), run_time=0.8)
            self.play(logn.animate.set_value(log(33)), rate_func=EASE,
                      run_time=beat.until("thirteen", offset=-0.2))
            self.play(flag(r_pow), run_time=0.8)

        # ---------------------------------------------------------- B12 Button
        cite1 = citation("Button et al., 2013 · Nature Reviews Neuroscience")
        with self.narrate("Real fields often sit there. Button and colleagues estimated the "
                          "median power of neuroscience studies at twenty-one percent. In this "
                          "picture, that power means printed effects about two point two "
                          "times the truth.") as beat:
            self.play(FadeOut(plan), FadeIn(cite1), run_time=0.8)
            beat.wait_until("twenty-one", offset=-1.6)
            self.play(logn.animate.set_value(log(66.1)), rate_func=EASE, run_time=1.6)
            self.play(flag(r_pow), run_time=0.8)
            beat.wait_until("two point two", offset=-0.2)
            self.play(flag(r_rat), flag(avg_line), run_time=1.0)

        # freeze the live geometry
        for m in (bell, tail_r, tail_l, wall_l, wall_r, wall_lbl, wall_lbl_r, avg_line):
            m.clear_updaters()
        for r in (r_n, r_pow, r_rat):
            r[1].clear_updaters()

        # ---------------------------------------------------------- B13 Kanazawa
        axis2 = self.make_axis(-10, 12.5, 5, "difference in girls born (percentage points)")
        axis2[1][-1].set_opacity(0)          # no tick label past 10
        nl2 = axis2[0]
        K_S = 3.3
        K_W = 6.5
        lo2, hi2 = -10, 12.5

        def X2(v):
            return nl2.n2p(v)

        bell2 = VMobject(color=BLUE, stroke_width=4).set_points_smoothly(
            self.bell_path(nl2, 0.1, K_S, BELL_H, lo2, hi2))
        t2r = Polygon(*self.bell_path(nl2, 0.1, K_S, BELL_H, lo2, hi2, x_from=K_W),
                      [X2(hi2)[0], AX_Y, 0], [X2(K_W)[0], AX_Y, 0],
                      stroke_width=0, fill_color=YELLOW, fill_opacity=0.55)
        t2l = Polygon(*self.bell_path(nl2, 0.1, K_S, BELL_H, lo2, hi2, x_to=-K_W),
                      [X2(-K_W)[0], AX_Y, 0], [X2(lo2)[0], AX_Y, 0],
                      stroke_width=0, fill_color=YELLOW, fill_opacity=0.55)
        w2l = Line(X2(-K_W), [X2(-K_W)[0], wall_top, 0], color=PURPLE, stroke_width=5)
        w2r = Line(X2(K_W), [X2(K_W)[0], wall_top, 0], color=PURPLE, stroke_width=5)
        w2l_lbl = MathTex(r"-6.5", font_size=MATH_SMALL + 4, color=PURPLE).next_to(w2l, UP, buff=0.15)
        w2r_lbl = MathTex(r"+6.5", font_size=MATH_SMALL + 4, color=PURPLE).next_to(w2r, UP, buff=0.15)
        green_band = Rectangle(width=X2(1)[0] - X2(-1)[0], height=top_y - AX_Y + 0.15,
                               stroke_width=0, fill_color=GREEN, fill_opacity=0.35)
        green_band.move_to([X2(0)[0], (top_y + 0.15 + AX_Y) / 2, 0])
        band_lbl = MathTex(r"\text{known effects} \le 1", font_size=MATH, color=GREEN)
        band_lbl.next_to(green_band, UP, buff=0.15)
        rep_line = DashedLine(X2(8), [X2(8)[0], 2.15, 0], color=YELLOW, stroke_width=4,
                              dash_length=0.12)
        rep_lbl = MathTex(r"\text{reported } 8", font_size=MATH, color=YELLOW)
        rep_lbl.next_to(rep_line, UP, buff=0.15)
        if rep_lbl.get_right()[0] > 6.4:
            rep_lbl.shift(LEFT * (rep_lbl.get_right()[0] - 6.4))
        study = MathTex(r"\text{most attractive parents:}", font_size=MATH)
        study2 = MathTex(r"56\%\text{ vs } 48\%\text{ girls}", font_size=MATH)
        st = VGroup(study, study2).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        st.move_to([-6.4 + st.width / 2, 2.95, 0])
        cite2 = citation("Gelman & Carlin, 2014 · Perspectives on Psychological Science")

        with self.narrate("Gelman and Carlin called this a Type M error, M for magnitude. Their "
                          "example: a two thousand and seven study found eight points more "
                          "girls among the firstborn children of the most attractive parents. "
                          "That study's walls sat at six and a half points, while known "
                          "sex-ratio effects are about one point or less.") as beat:
            self.play(FadeOut(cite1), FadeIn(cite2), FadeOut(panel), FadeOut(new_eq),
                      run_time=0.8)
            beat.wait_until("example", offset=-0.2)
            self.play(ReplacementTransform(axis, axis2), ReplacementTransform(bell, bell2),
                      ReplacementTransform(tail_r, t2r), ReplacementTransform(tail_l, t2l),
                      ReplacementTransform(wall_l, w2l), ReplacementTransform(wall_r, w2r),
                      ReplacementTransform(wall_lbl, w2l_lbl),
                      ReplacementTransform(wall_lbl_r, w2r_lbl),
                      ReplacementTransform(avg_line, rep_line),
                      FadeOut(truth), FadeOut(truth_lbl), run_time=1.8)
            beat.wait_until("eight points", offset=-0.2)
            self.play(Write(rep_lbl), run_time=0.9)
            beat.wait_until("firstborn", offset=-0.2)
            self.play(FadeIn(st, shift=0.2 * RIGHT), run_time=1.0)
            beat.wait_until("six and", offset=-0.2)
            self.play(flag(w2l_lbl, color=PURPLE), flag(w2r_lbl, color=PURPLE), run_time=0.9)
            beat.wait_until("known", offset=-0.2)
            self.play(FadeIn(green_band), Write(band_lbl), run_time=1.0)

        # ---------------------------------------------------------- B14 77x
        t01 = Line(X2(0.1), X2(0.1) + UP * (top_y - AX_Y + 0.15), color=GREEN, stroke_width=4)
        k1 = MathTex(r"\text{if true} = 0.1\text{:}", font_size=MATH, color=GREEN)
        k2 = MathTex(r"\text{printed} \div \text{true} \approx 77", font_size=MATH, color=YELLOW)
        k3 = MathTex(r"46\%\text{ wrong sign}", font_size=MATH, color=YELLOW)
        kk = VGroup(k1, k2, k3).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        kk.move_to([-6.4 + kk.width / 2, 2.75, 0])
        with self.narrate("If the true effect were point one, a significant result would "
                          "overstate it seventy-seven times on average, and nearly half would "
                          "point the wrong way.") as beat:
            self.play(FadeOut(st), green_band.animate.set_fill(opacity=0.15), FadeOut(band_lbl),
                      Create(t01), FadeIn(k1), run_time=1.0)
            beat.wait_until("seventy", offset=-0.3)
            self.play(FadeIn(k2, shift=0.2 * RIGHT), flag(t2r), run_time=1.0)
            beat.wait_until("nearly half", offset=-0.2)
            self.play(FadeIn(k3, shift=0.2 * RIGHT), flag(t2l), run_time=1.0)

        # ---------------------------------------------------------- B15 landing
        axis3 = self.make_axis(-1, 1.5, 0.5, "estimated effect (standard deviations)")
        bell3 = VMobject(color=BLUE, stroke_width=4).set_points_smoothly(
            self.bell_path(nl, D, SE0, BELL_H, lo, hi))
        w3 = VGroup(Line(X(-W0), [X(-W0)[0], wall_top, 0], color=PURPLE, stroke_width=5),
                    Line(X(W0), [X(W0)[0], wall_top, 0], color=PURPLE, stroke_width=5))
        w3_lbl = MathTex(r"0.62", font_size=MATH_SMALL + 4, color=PURPLE).next_to(w3[1], UP, buff=0.15)
        w3_lbl_l = MathTex(r"-0.62", font_size=MATH_SMALL + 4, color=PURPLE).next_to(w3[0], UP, buff=0.15)
        avg3 = DashedLine(X(pm), [X(pm)[0], 2.15, 0], color=YELLOW, stroke_width=4,
                          dash_length=0.12)
        avg3_lbl = MathTex(r"\text{printed average } 0.69", font_size=MATH, color=YELLOW)
        avg3_lbl.next_to(avg3, UP, buff=0.15)
        if avg3_lbl.get_right()[0] > 6.4:
            avg3_lbl.shift(LEFT * (avg3_lbl.get_right()[0] - 6.4))
        n20 = MathTex(r"n = 20\text{ per group}", font_size=MATH)
        n20.move_to([-6.4 + n20.width / 2, 3.2, 0])
        tiles.set_fill(opacity=0.22)
        for i, t in enumerate(tiles):
            if SIG[i]:
                t.set_fill(YELLOW, opacity=1)
        truth3 = truth.copy()
        truth3_lbl = truth_lbl.copy()

        with self.narrate("Back to the thousand labs. Point six nine was never a fluke. With "
                          "twenty per group, nothing under point six two could get out. In a "
                          "small study, huge is the only size an effect is allowed to be.") as beat:
            self.play(FadeOut(kk), FadeOut(cite2), FadeOut(green_band), FadeOut(t01),
                      FadeOut(rep_lbl),
                      ReplacementTransform(axis2, axis3), ReplacementTransform(bell2, bell3),
                      FadeOut(t2r), FadeOut(t2l),
                      ReplacementTransform(VGroup(w2l, w2r), w3),
                      ReplacementTransform(w2l_lbl, w3_lbl_l),
                      ReplacementTransform(w2r_lbl, w3_lbl),
                      ReplacementTransform(rep_line, avg3), run_time=1.8)
            self.play(FadeIn(tiles), FadeIn(truth3), FadeIn(truth3_lbl), FadeIn(n20),
                      run_time=beat.until("Point six", offset=-0.3))
            self.play(Write(avg3_lbl), run_time=1.0)
            beat.wait_until("nothing under", offset=-0.2)
            self.play(flag(w3_lbl, color=PURPLE), flag(w3_lbl_l, color=PURPLE),
                      Indicate(truth3, color=GREEN), run_time=1.0)
            beat.wait_until("huge", offset=-0.2)
            outside3 = VGroup(*[tiles[i] for i in range(1000) if SIG[i]])
            self.play(LaggedStart(*[flag(t) for t in outside3], lag_ratio=0.02),
                      run_time=min(2.0, beat.remaining(min_time=1.0)))

        self.end_card()
