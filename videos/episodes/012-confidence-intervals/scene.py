"""Episode 12 - What '95% Confident' Actually Means.

    videos/toolkit/render.sh videos/episodes/012-confidence-intervals/scene.py Episode \
        videos/episodes/012-confidence-intervals/final.mp4
"""
import numpy as np
from manim import *
from sample_space import *

# ------------------------------------------------------------------ data (see sim.py)
MU, SIGMA, N, RUNS, SEED = 0.25, 0.13, 5, 100, 4335
ZC, TC = 1.96, 2.7764451051977934            # t_{0.975, 4}
_rng = np.random.default_rng(SEED)
X = _rng.normal(MU, SIGMA, size=(RUNS, N))
M = X.mean(1)
S = X.std(1, ddof=1)
SE = S / np.sqrt(N)
RANK = np.argsort(np.argsort(S))              # 0 = narrowest interval
HIT_Z = np.abs(M - MU) <= ZC * SE
HIT_T = np.abs(M - MU) <= TC * SE
assert HIT_Z.sum() == 88 and HIT_T.sum() == 95 and HIT_Z[:4].all()
assert (~HIT_Z[RANK < 50]).sum() == 11
PAIR_HIT, PAIR_MISS = 52, 94                  # equal-width pair for the freeze

STEP = 0.045                                  # vertical slot spacing (scene units)
BASE = 0.8                                    # slot 0 height above the axis
ROW = 0.45                                    # "workbench" row height above the axis
RAIN_CENTER = np.array([2.6, -2.25, 0])       # where n2p(0.25) sits in the main layout
PANEL_X = -3.95                               # left panel centre


class Episode(NarratedScene):
    EPISODE = 12
    TITLE = "What '95% Confident' Actually Means"
    PRONUNCIATIONS = {
        "Hoekstra": "/hˈʊkstɹə/",
        "Hoekstra's": "/hˈʊkstɹəz/",
        "Gosset": "/ɡˈɑsɪt/",
        "Neyman's": "/nˈAmənz/",
        "Jerzy": "/jˈɛʒi/",
    }

    # -------------------------------------------------------------- geometry helpers
    def sc(self):
        return (self.nl.n2p(0.5)[0] - self.nl.n2p(0.0)[0]) / 6.0

    def y_at(self, h):
        return self.nl.n2p(MU)[1] + self.sc() * h

    def px(self, v):
        return self.nl.n2p(v)[0]

    def slot_h(self, j):
        return BASE + STEP * j

    # -------------------------------------------------------------- bars
    def update_bars(self, group):
        P, K, Sv = self.P.get_value(), self.K.get_value(), self.Ssort.get_value()
        D, V = self.D.get_value(), self.V.get_value()
        sc = self.sc()
        for i, bar in enumerate(group):
            g = float(np.clip((P - i) / 3.0, 0, 1)) if i >= 4 else float(P >= i + 1)
            half = K * SE[i] * max(g, 1e-3)
            j = (1 - Sv) * i + Sv * RANK[i]
            y = self.y_at(self.slot_h(j))
            bar.put_start_and_end_on(np.array([self.px(M[i] - half), y, 0]),
                                     np.array([self.px(M[i] + half), y, 0]))
            hit = abs(M[i] - MU) <= K * SE[i]
            col = interpolate_color(ManimColor(BLUE), ManimColor(GREEN if hit else RED), V)
            bar.set_stroke(col, width=3.6 * sc, opacity=D if g > 0 else 0)

    def hits_now(self):
        P, K = self.P.get_value(), self.K.get_value()
        n = int(np.floor(P + 1e-6))
        return int((np.abs(M[:n] - MU) <= K * SE[:n]).sum())

    def shown_now(self):
        return int(np.floor(self.P.get_value() + 1e-6))

    def run_dots(self, i):
        return VGroup(*[Dot([self.px(v), self.y_at(ROW), 0], radius=0.07, color=BLUE)
                        for v in X[i]])

    def bench_bar(self, i, k=ZC, width=3.6, color=BLUE):
        y = self.y_at(ROW)
        return Line([self.px(M[i] - k * SE[i]), y, 0], [self.px(M[i] + k * SE[i]), y, 0],
                    color=color, stroke_width=width)

    # -------------------------------------------------------------- scene
    def construct(self):
        # number line built at its main ("rain") size, then shrunk for the hook
        nl = NumberLine(x_range=[-0.05, 0.55, 0.1], length=7.2, color=GRAY, stroke_width=2.5,
                        include_ticks=False, include_tip=False)
        nl.ticks = VGroup(*[nl.get_tick(v, size=0.07) for v in (0, .1, .2, .3, .4, .5)])
        nl.add(nl.ticks)
        nl.add_numbers(x_values=[0, .1, .2, .3, .4, .5], num_decimal_places=1,
                       font_size=32, color=GRAY, buff=0.2)
        nl.move_to(RAIN_CENTER - (nl.n2p(MU) - nl.get_center()))
        ax_title = label("measured value (arbitrary units)", size=26, color=GRAY)
        ax_title.next_to(nl.numbers, DOWN, buff=0.14).align_to(nl.n2p(0.55), RIGHT)
        axis_grp = VGroup(nl, ax_title)
        self.nl = nl
        rain_state = axis_grp.copy()
        axis_grp.scale(0.86).move_to([3.05, -0.55, 0])

        # ============================================================ 1. cold open
        hook_bar = Line([self.px(0.1), 0, 0], [self.px(0.4), 0, 0], color=BLUE, stroke_width=9)
        hook_bar.move_to([hook_bar.get_center()[0], nl.get_center()[1] + 0.75, 0])
        caps = VGroup(*[Line(UP * 0.16, DOWN * 0.16, color=BLUE, stroke_width=5)
                        .move_to(p) for p in (hook_bar.get_start(), hook_bar.get_end())])
        ci_label = label("95% confidence interval", color=BLUE).next_to(hook_bar, UP, buff=0.32)
        stmt = VGroup(text("95% chance the true mean", size=HEADING),
                      text("is inside?", size=HEADING)).arrange(DOWN, buff=0.2)
        stmt.move_to([-3.45, 1.55, 0])
        opt_t = text("true", size=BODY)
        opt_f = text("false", size=BODY)
        opts = VGroup(opt_t, opt_f).arrange(RIGHT, buff=1.4).next_to(stmt, DOWN, buff=0.75)
        boxes = VGroup(*[SurroundingRectangle(o, color=GRAY, buff=0.2, corner_radius=0.08,
                                              stroke_width=2.5) for o in opts])
        with self.narrate("A study reports a ninety-five percent confidence interval for a "
                          "mean: from point one to point four. True or false: there is a "
                          "ninety-five percent chance that the true mean lies inside it. "
                          "[pause 1.8]") as beat:
            self.play(Create(nl), FadeIn(ax_title), run_time=beat.until("confidence"))
            self.play(GrowFromCenter(hook_bar), FadeIn(caps), FadeIn(ci_label, shift=0.1 * UP),
                      run_time=beat.until("point one", offset=-0.1))
            self.play(Indicate(caps[0], color=INK, scale_factor=1.3),
                      run_time=beat.until("point four", offset=-0.1))
            self.play(Indicate(caps[1], color=INK, scale_factor=1.3), run_time=0.8)
            self.play(FadeIn(stmt, shift=0.1 * UP), run_time=beat.until("there is"))
            self.play(Create(boxes), FadeIn(opts), run_time=beat.until("inside", end=True))
            # prediction pause: the two options breathe in turn (nothing else moves)
            self.play(boxes[0].animate.set_stroke(INK, 4), run_time=0.8)
            self.play(boxes[0].animate.set_stroke(GRAY, 2.5),
                      boxes[1].animate.set_stroke(INK, 4), run_time=0.8)
            self.play(boxes[1].animate.set_stroke(GRAY, 2.5), run_time=0.6)

        # ============================================================ 2. stakes
        waffle = VGroup(*[Circle(radius=0.095, stroke_color=GRAY, stroke_width=2,
                                 fill_color=INK, fill_opacity=0) for _ in range(118)])
        waffle.arrange_in_grid(rows=12, cols=10, buff=0.18).move_to([3.1, 0.2, 0])
        w_top = label("118 researchers", color=GRAY).next_to(waffle, UP, buff=0.3)
        filled = waffle[:70]
        w_bot = label("59% ticked true").next_to(waffle, DOWN, buff=0.3)
        cite1 = citation("Hoekstra, Morey, Rouder & Wagenmakers, 2014 · Psychonomic Bulletin & Review")
        answer = SurroundingRectangle(opt_f, color=INK, buff=0.2, corner_radius=0.08, stroke_width=5)
        ans_lbl = label("survey's answer", color=INK).next_to(answer, DOWN, buff=0.25)
        with self.narrate("In twenty fourteen, Hoekstra and colleagues put this exact sentence "
                          "to a hundred and eighteen psychology researchers. Fifty-nine percent "
                          "ticked true. The survey's authors had written it as a false "
                          "statement.") as beat:
            self.play(FadeOut(VGroup(axis_grp, hook_bar, caps, ci_label)), FadeIn(cite1),
                      run_time=beat.until("this exact", offset=-0.2))
            self.play(flag(stmt, color=INK), run_time=0.9)
            self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in waffle], lag_ratio=0.02),
                      FadeIn(w_top), run_time=beat.until("Fifty", offset=-0.1))
            self.play(LaggedStart(*[d.animate.set_fill(INK, 1).set_stroke(INK)
                                    for d in filled], lag_ratio=0.03),
                      FadeIn(w_bot, shift=0.1 * UP), boxes[0].animate.set_stroke(INK, 4),
                      run_time=beat.until("ticked", end=True))
            beat.wait_until("false", offset=-0.2)
            self.play(boxes[0].animate.set_stroke(GRAY, 2.5), Create(answer),
                      FadeIn(ans_lbl, shift=0.1 * UP), run_time=1.0)

        # ============================================================ 3. set-up
        self.P, self.K = ValueTracker(0), ValueTracker(ZC)
        self.Ssort, self.D, self.V = ValueTracker(0), ValueTracker(1), ValueTracker(1)
        with self.narrate("To see why, we'll build the machine that makes these intervals, "
                          "and test it in a world where we know the truth.") as beat:
            self.play(FadeOut(VGroup(waffle, w_top, w_bot, stmt, opts, boxes, answer, ans_lbl,
                                     cite1)), run_time=1.0)
            axis_grp.become(rain_state)
            self.play(Create(nl), FadeIn(ax_title), run_time=beat.until("test"))
            sim_tag = label("simulated", color=GRAY).move_to([5.55, 3.38, 0])
            self.play(FadeIn(sim_tag, shift=0.1 * DOWN), run_time=beat.until("truth"))

        # ============================================================ 4. naive build
        mu_line = Line(color=YELLOW, stroke_width=4)
        mu_line.add_updater(lambda l: l.put_start_and_end_on(
            np.array([self.px(MU), self.y_at(0), 0]),
            np.array([self.px(MU), self.y_at(self.slot_h(99) + 0.05), 0])))
        mu_lbl = VGroup(label("true mean", color=YELLOW),
                        formula(r"\mu = 0.25", size=36, color=YELLOW)).arrange(RIGHT, buff=0.2)
        mu_lbl.add_updater(lambda m: m.move_to(
            [self.px(MU), self.y_at(self.slot_h(99)) + 0.38, 0]))
        F1 = formula(r"\bar{x}", r"\pm", r"1.96", r"\cdot", r"\frac{s}{\sqrt{5}}", size=EQ)
        F1[0].set_color(BLUE)
        F1.move_to([PANEL_X, 2.65, 0])
        dots0 = self.run_dots(0)
        xbar_tick = Line(UP * 0.2, DOWN * 0.2, color=BLUE, stroke_width=4).move_to(
            [self.px(M[0]), self.y_at(ROW), 0])
        bar0 = self.bench_bar(0)
        promise = label("textbook 95% interval", color=GRAY).next_to(F1, DOWN, buff=0.35)
        with self.narrate("In this simulated world the true mean is point two five: this "
                          "yellow line. Each run, the machine gets five measurements, these "
                          "dots, and draws the textbook interval: their average, plus or "
                          "minus one point nine six times the spread s, over root five.") as beat:
            beat.wait_until("point two five", offset=-0.3)
            self.play(Create(mu_line), FadeIn(mu_lbl), run_time=beat.until("yellow", end=True))
            beat.wait_until("these dots", offset=-0.2)
            self.play(LaggedStart(*[FadeIn(d, shift=0.4 * DOWN) for d in dots0], lag_ratio=0.2),
                      run_time=beat.until("textbook", offset=-0.1))
            self.play(FadeIn(promise), run_time=beat.until("average", offset=-0.1))
            self.play(TransformFromCopy(dots0, xbar_tick), run_time=0.8)
            self.play(TransformFromCopy(xbar_tick, F1[0]), run_time=beat.until("plus", offset=-0.1))
            self.play(Write(F1[1]), run_time=0.5)
            self.play(Write(F1[2]), run_time=beat.until("spread", offset=-0.1))
            self.play(Write(F1[3]), TransformFromCopy(dots0, F1[4]),
                      run_time=beat.until("five", 2, end=True))
            self.play(GrowFromPoint(bar0, xbar_tick.get_center()), run_time=1.0)

        # ============================================================ 5. it works... then rain
        bars = VGroup(*[Line(LEFT, RIGHT) for _ in range(RUNS)])
        bars.add_updater(self.update_bars)
        self.add(bars)
        hits_lbl = label("hits", size=BODY, color=GREEN)
        hits_num = Integer(0, font_size=MATH)
        hits_den = formula(r"/\ 100", color=GRAY)
        hits_row = VGroup(hits_lbl, hits_num, hits_den).arrange(RIGHT, buff=0.25)
        hits_row.move_to([PANEL_X, 1.15, 0])
        miss_lbl = label("misses", size=BODY, color=RED)
        miss_num = Integer(0, font_size=MATH)
        miss_row = VGroup(miss_lbl, miss_num).arrange(RIGHT, buff=0.25)
        miss_row.next_to(hits_row, DOWN, buff=0.35).align_to(hits_row, LEFT)
        hits_num.add_updater(lambda d: d.set_value(self.hits_now()).next_to(hits_lbl, RIGHT, buff=0.25))
        hits_den.add_updater(lambda d: d.next_to(hits_num, RIGHT, buff=0.2))
        miss_num.add_updater(lambda d: d.set_value(self.shown_now() - self.hits_now())
                             .next_to(miss_lbl, RIGHT, buff=0.25))

        def rise(i, bench, dots):
            target = self.y_at(self.slot_h(i))
            return AnimationGroup(bench.animate.set_y(target).set_color(GREEN if HIT_Z[i] else RED),
                                  FadeOut(dots), run_time=0.6)

        with self.narrate("The first four intervals all catch the line. Now run it a hundred "
                          "times. Green caught the true mean, red missed it.") as beat:
            self.play(FadeIn(hits_row), FadeIn(miss_row), rise(0, bar0, VGroup(dots0, xbar_tick)))
            self.remove(bar0)
            self.P.set_value(1)
            for i in (1, 2, 3):
                d, b = self.run_dots(i), self.bench_bar(i)
                self.play(FadeIn(d, shift=0.3 * DOWN), GrowFromCenter(b), run_time=0.45)
                self.play(rise(i, b, d))
                self.remove(b)
                self.P.set_value(i + 1)
            self.play(self.P.animate.set_value(RUNS + 3), run_time=beat.until("Green", offset=-0.1),
                      rate_func=linear)
            self.P.set_value(RUNS + 3)
            self.play(flag(hits_lbl, color=GREEN), run_time=0.8)
            beat.wait_until("red", offset=-0.1)
            self.play(flag(miss_lbl, color=RED), run_time=0.8)

        # ============================================================ 6. fail, measured
        million = formula(r"10^6\text{ runs: }", r"87.8\%", size=36).move_to([PANEL_X, -0.35, 0])
        with self.narrate("Eighty-eight hits out of a hundred. A million runs settle at "
                          "eighty-eight percent. The label promised ninety-five.") as beat:
            self.play(Circumscribe(hits_row, color=GREEN, buff=0.15), run_time=beat.until("A million"))
            self.play(FadeIn(million, shift=0.1 * UP), run_time=beat.until("label", offset=-0.1))
            self.play(promise.animate.set_color(INK), flag(promise, color=INK),
                      run_time=beat.remaining(0.8))

        # ============================================================ 7. cause
        lo_y, hi_y = self.y_at(self.slot_h(0)), self.y_at(self.slot_h(49))
        brace = BraceBetweenPoints([-1.2, hi_y, 0], [-1.2, lo_y, 0], direction=LEFT, color=GRAY)
        brace.shift(RIGHT * 0)
        cause_lbl = VGroup(label("narrower half:"), label("11 of 12 misses", color=RED)) \
            .arrange(DOWN, buff=0.15).move_to([PANEL_X, -1.55, 0])
        s_term = F1[4]
        with self.narrate("Sort the intervals by width, and the misses pile up at the narrow "
                          "end. With five points, the spread s is itself noisy. When it comes "
                          "out too small, the interval shrinks and stops short of the line. "
                          "Over a million runs, nearly nine in ten misses come from the "
                          "narrower half.") as beat:
            self.play(self.Ssort.animate.set_value(1), run_time=beat.until("pile", end=True))
            self.play(GrowFromCenter(brace), FadeIn(cause_lbl, shift=0.1 * RIGHT),
                      run_time=beat.until("With", offset=-0.1))
            self.play(Circumscribe(s_term, color=BLUE, buff=0.1), run_time=beat.until("When"))
            # the narrowest miss, magnified on the bench: its s shrinks, it falls short
            nm = int(np.argmin(np.where(~HIT_Z, S, np.inf)))
            probe_s = ValueTracker(SIGMA / np.sqrt(N))
            demo = always_redraw(lambda: Line(
                [self.px(M[nm] - ZC * probe_s.get_value()), self.y_at(ROW), 0],
                [self.px(M[nm] + ZC * probe_s.get_value()), self.y_at(ROW), 0],
                color=BLUE, stroke_width=7))
            self.play(FadeIn(demo), run_time=0.5)
            self.play(probe_s.animate.set_value(SE[nm]), run_time=beat.until("short", end=True))
            demo.clear_updaters()
            self.play(demo.animate.set_color(RED), run_time=0.5)
            beat.wait_until("nearly", offset=-0.2)
            self.play(FadeOut(demo), flag(cause_lbl[1], color=RED), run_time=1.0)

        # ============================================================ 8. fix
        F1b = formula(r"\bar{x}", r"\pm", r"2.78", r"\cdot", r"\frac{s}{\sqrt{5}}", size=EQ)
        F1b[0].set_color(BLUE)
        F1b.move_to(F1)
        cite2 = citation("Student (W. S. Gosset), 1908 · Biometrika")
        million_b = formula(r"10^6\text{ runs: }", r"95.0\%", size=36).move_to(million)
        with self.narrate("William Gosset, writing as Student in nineteen oh eight, worked out "
                          "the fix: with five points, multiply by two point seven eight instead "
                          "of one point nine six. Every bar stretches by the same factor. "
                          "Ninety-five of a hundred now catch the line, and a million runs "
                          "give ninety-five percent.") as beat:
            self.play(FadeIn(cite2), FadeOut(VGroup(brace, cause_lbl)),
                      run_time=beat.until("two point seven", offset=-0.2))
            self.play(TransformMatchingTex(F1, F1b), run_time=1.0)
            self.play(flag(F1b[2]), run_time=beat.until("Every", offset=-0.1))
            self.play(self.K.animate.set_value(TC), run_time=beat.until("Ninety", offset=-0.1))
            self.play(Circumscribe(hits_row, color=GREEN, buff=0.15),
                      run_time=beat.until("a million", offset=-0.1))
            self.play(TransformMatchingTex(million, million_b), run_time=1.0)
            self.play(flag(million_b[1], color=INK), run_time=beat.remaining(0.6))
        F1 = F1b
        million = million_b

        # ============================================================ 9. insight
        plo, phi = ValueTracker(M[0] - TC * SE[0]), ValueTracker(M[0] + TC * SE[0])
        probe = always_redraw(lambda: Line([self.px(plo.get_value()), self.y_at(ROW), 0],
                                           [self.px(phi.get_value()), self.y_at(ROW), 0],
                                           color=BLUE, stroke_width=8))
        Lp = formula("L", color=BLUE)
        Up = formula("U", color=BLUE)
        Lp.add_updater(lambda m: m.next_to(probe.get_start(), LEFT, buff=0.18))
        Up.add_updater(lambda m: m.next_to(probe.get_end(), RIGHT, buff=0.18))
        F2 = MathTex("P(", "L", r"\le", r"\mu", r"\le", "U", ")", "=", "0.95", font_size=EQ)
        F2[1].set_color(BLUE); F2[5].set_color(BLUE); F2[3].set_color(YELLOW); F2[8].set_color(GREEN)
        F2.move_to([PANEL_X, -0.6, 0])
        jumps = [17, 63, 5, 41, 88]
        with self.narrate("Now read the ninety-five percent off this picture. It counts hits "
                          "across runs. Before the data arrive, the endpoints L and U are "
                          "random: they jump from run to run, while the mean mu stays put. The "
                          "chance that this random interval covers mu is point nine five.") as beat:
            self.play(FadeOut(VGroup(miss_row, million, cite2)), run_time=beat.until("It counts"))
            self.play(Circumscribe(hits_row, color=GREEN, buff=0.15), run_time=beat.until("Before"))
            self.play(GrowFromCenter(probe), run_time=beat.until("L and U", offset=-0.1))
            self.play(FadeIn(Lp), FadeIn(Up), run_time=0.6)
            t_jump = beat.until("while", offset=-0.1)
            for k in jumps[:3]:
                self.play(plo.animate.set_value(M[k] - TC * SE[k]),
                          phi.animate.set_value(M[k] + TC * SE[k]), run_time=t_jump / 3)
            self.play(Indicate(mu_lbl, color=YELLOW, scale_factor=1.12),
                      plo.animate.set_value(M[jumps[3]] - TC * SE[jumps[3]]),
                      phi.animate.set_value(M[jumps[3]] + TC * SE[jumps[3]]),
                      run_time=beat.until("The chance", offset=-0.1))
            self.play(Write(F2[0]), TransformFromCopy(Lp, F2[1]), run_time=0.6)
            self.play(Write(F2[2]), TransformFromCopy(mu_lbl[1][0][0], F2[3]), Write(F2[4]),
                      run_time=0.6)
            self.play(TransformFromCopy(Up, F2[5]), Write(F2[6:8]),
                      run_time=beat.until("point nine five", offset=-0.1))
            self.play(TransformFromCopy(hits_row, F2[8]), run_time=beat.remaining(0.9))

        # ============================================================ 10. one interval
        F3 = MathTex("P(", "0.1", r"\le", r"\mu", r"\le", "0.4", ")", "=", r"1\text{ or }0",
                     font_size=EQ)
        F3[1].set_color(BLUE); F3[5].set_color(BLUE); F3[3].set_color(YELLOW)
        F3.move_to(F2)
        with self.narrate("Run the study once, and the endpoints become numbers, say point one "
                          "and point four. Now nothing in the statement is random. Mu is inside "
                          "or it isn't, so the probability is one or zero, and you can't see "
                          "which.") as beat:
            self.play(plo.animate.set_value(0.1), phi.animate.set_value(0.4),
                      run_time=beat.until("point one", offset=-0.1))
            self.play(FadeOut(Lp), FadeOut(Up), ReplacementTransform(F2[1], F3[1]),
                      ReplacementTransform(F2[5], F3[5]), run_time=1.0)
            self.play(flag(F3[1]), flag(F3[5]), run_time=beat.until("Mu is", offset=-0.1))
            self.play(Indicate(mu_line, color=YELLOW, scale_factor=1.0), run_time=beat.until("one or zero", offset=-0.1))
            rest_old = VGroup(F2[0], F2[2], F2[3], F2[4], F2[6], F2[7], F2[8])
            rest_new = VGroup(F3[0], F3[2], F3[3], F3[4], F3[6], F3[7])
            self.play(ReplacementTransform(rest_old[:-1], rest_new), FadeOut(F2[8], shift=0.2 * UP),
                      FadeIn(F3[8], shift=0.2 * UP), run_time=1.0)
            self.play(flag(F3[8], color=INK), run_time=beat.remaining(0.6))
        F3_full = F3

        # ============================================================ 11. prediction pause
        def stack_bar_pos(i):
            y = self.y_at(self.slot_h(RANK[i]))
            return np.array([self.px(M[i] - TC * SE[i]), y, 0]), np.array([self.px(M[i] + TC * SE[i]), y, 0])

        pA = Line(*stack_bar_pos(PAIR_HIT), color=GREEN, stroke_width=9)
        pB = Line(*stack_bar_pos(PAIR_MISS), color=RED, stroke_width=9)
        yA, yB = 1.35, 0.35
        lblA = label("top", color=GRAY)
        with self.narrate("Here are two intervals from the machine, the same width. Without "
                          "the line, which a real study never shows you, which one caught the "
                          "mean? [pause 1.6] The top one caught it. The bottom one missed. From "
                          "the inside, a hit and a miss look identical.") as beat:
            self.play(FadeOut(probe), FadeIn(pA), FadeIn(pB), self.D.animate.set_value(0.12),
                      run_time=0.8)
            self.play(pA.animate.move_to([pA.get_center()[0], yA, 0]),
                      pB.animate.move_to([pB.get_center()[0], yB, 0]), run_time=beat.until("Without"))
            self.play(FadeOut(mu_line), FadeOut(mu_lbl), axis_grp.animate.set_opacity(0.12),
                      pA.animate.move_to([2.6, yA, 0]).set_color(BLUE),
                      pB.animate.move_to([2.6, yB, 0]).set_color(BLUE),
                      run_time=beat.until("which one", offset=-0.1))
            ctrA = Dot(pA.get_center(), radius=0.07, color=INK)
            ctrB = Dot(pB.get_center(), radius=0.07, color=INK)
            self.play(FadeIn(ctrA), FadeIn(ctrB), run_time=0.6)
            beat.wait_until("The top", offset=-0.6)
            self.play(axis_grp.animate.set_opacity(1), FadeIn(mu_line), FadeIn(mu_lbl),
                      pA.animate.move_to([(self.px(M[PAIR_HIT] - TC * SE[PAIR_HIT]) +
                                           self.px(M[PAIR_HIT] + TC * SE[PAIR_HIT])) / 2, yA, 0]),
                      pB.animate.move_to([(self.px(M[PAIR_MISS] - TC * SE[PAIR_MISS]) +
                                           self.px(M[PAIR_MISS] + TC * SE[PAIR_MISS])) / 2, yB, 0]),
                      ctrA.animate.move_to([self.px(M[PAIR_HIT]), yA, 0]),
                      ctrB.animate.move_to([self.px(M[PAIR_MISS]), yB, 0]),
                      run_time=beat.until("caught it", offset=-0.1))
            self.play(pA.animate.set_color(GREEN), run_time=beat.until("bottom", offset=-0.1))
            self.play(pB.animate.set_color(RED), run_time=beat.until("From"))
            self.play(Wiggle(VGroup(pA, pB), scale_value=1.0, rotation_angle=0.0, n_wiggles=0),
                      run_time=0.1) if False else None
            self.play(pA.animate.set_color(BLUE), pB.animate.set_color(BLUE),
                      FadeOut(mu_line), run_time=beat.until("identical", end=True))

        # ============================================================ 12. payoff
        F2b = MathTex("P(", "L", r"\le", r"\mu", r"\le", "U", ")", "=", "0.95", font_size=EQ)
        F2b[1].set_color(BLUE); F2b[5].set_color(BLUE); F2b[3].set_color(YELLOW); F2b[8].set_color(GREEN)
        F2b.move_to([PANEL_X, 2.65, 0])
        cite3 = citation("Neyman, 1937 · Philosophical Transactions of the Royal Society A")
        cite4 = citation("Hoekstra et al., 2014 · Psychonomic Bulletin & Review")
        proc = label("a property of the procedure", color=GRAY).next_to(F2b, DOWN, buff=0.3)
        # Hoekstra means, horizontal bars, 0..6 false statements endorsed
        cx0, unit, cy = -3.75, 0.75, -1.85
        caxis = Line([cx0, cy, 0], [cx0 + 6 * unit, cy, 0], color=GRAY, stroke_width=2.5)
        cticks = VGroup(*[VGroup(Line(UP * 0.07, DOWN * 0.07, color=GRAY, stroke_width=2.5)
                                 .move_to([cx0 + v * unit, cy, 0]),
                                 formula(str(v), size=MATH_SMALL, color=GRAY)
                                 .move_to([cx0 + v * unit, cy - 0.32, 0])) for v in (0, 2, 4, 6)])
        ctitle = label("false readings endorsed (of 6)", size=26, color=GRAY) \
            .next_to(cticks, DOWN, buff=0.14).align_to(caxis, RIGHT)
        rows = []
        for k, (name, val) in enumerate((("researchers", 3.45), ("first-years", 3.51))):
            y = cy + 1.45 - 0.75 * k
            r = Rectangle(width=val * unit, height=0.42, stroke_width=0, fill_color=INK,
                          fill_opacity=0.85).move_to([cx0 + val * unit / 2, y, 0])
            nm_ = label(name).next_to([cx0, y, 0], LEFT, buff=0.22)
            v_ = formula(f"{val:.2f}", size=36).next_to(r, RIGHT, buff=0.2)
            rows.append(VGroup(r, nm_, v_))
        chart = VGroup(caxis, cticks, ctitle, *rows)
        thumb_target = np.array([4.35, -2.2, 0])
        with self.narrate("This is Jerzy Neyman's theory of confidence intervals from nineteen "
                          "thirty-seven: the confidence belongs to the procedure. In Hoekstra's "
                          "survey, researchers endorsed on average three and a half of six false "
                          "readings, about as many as first-year students who had never been "
                          "taught inference.") as beat:
            self.play(FadeOut(VGroup(pA, pB, ctrA, ctrB, hits_row, F1, promise, sim_tag)),
                      FadeOut(mu_lbl), self.D.animate.set_value(1), self.V.animate.set_value(1),
                      nl.numbers.animate.set_opacity(0), ax_title.animate.set_opacity(0),
                      run_time=0.8)
            mu_line.set_stroke(opacity=1)
            self.play(nl.animate.scale(0.55).shift(thumb_target - nl.n2p(MU)),
                      FadeIn(mu_line), F3_full.animate.move_to(F2b), FadeIn(cite3),
                      run_time=beat.until("the confidence", offset=-0.2))
            self.play(TransformMatchingTex(F3_full, F2b), run_time=1.0)
            self.play(FadeIn(proc, shift=0.1 * UP), run_time=beat.until("In Hoekstra"))
            self.play(Create(caxis), FadeIn(cticks), FadeIn(ctitle), FadeOut(cite3), FadeIn(cite4),
                      run_time=beat.until("three and a half", offset=-0.3))
            self.play(FadeIn(rows[0][1]), GrowFromEdge(rows[0][0], LEFT), FadeIn(rows[0][2]),
                      run_time=beat.until("about as many", offset=-0.1))
            self.play(FadeIn(rows[1][1]), GrowFromEdge(rows[1][0], LEFT), FadeIn(rows[1][2]),
                      run_time=beat.until("never", offset=-0.1))
            self.play(flag(rows[1][1], color=INK), run_time=beat.remaining(0.8))

        # ============================================================ 13. honest limits
        tags = VGroup(label("random sampling", color=GRAY), label("model fits", color=GRAY)) \
            .arrange(RIGHT, buff=0.6).next_to(F2b, DOWN, buff=0.3)
        bl = NumberLine(x_range=[0, 0.5, 0.1], length=5.0, color=GRAY, stroke_width=2.5,
                        include_tip=False, tick_size=0.07)
        bl.add_numbers(x_values=[0, .1, .2, .3, .4, .5], num_decimal_places=1, font_size=MATH_SMALL,
                       color=GRAY, buff=0.2)
        bl.move_to([PANEL_X + 0.35, -1.95, 0])
        bl_title = formula(r"\mu", size=36, color=PURPLE).next_to(bl.n2p(0.5), RIGHT, buff=0.25)
        se_h = 0.15 / TC

        def post(v):
            tt = (v - 0.25) / se_h
            return (1 + tt * tt / 4) ** (-2.5)            # t4 kernel, peak 1
        curve = VMobject(color=PURPLE, stroke_width=4).set_points_smoothly(
            [bl.n2p(v) + UP * 1.7 * post(v) for v in np.linspace(0, 0.5, 120)])
        area = Polygon(*([bl.n2p(0.1)] + [bl.n2p(v) + UP * 1.7 * post(v)
                                         for v in np.linspace(0.1, 0.4, 80)] + [bl.n2p(0.4)]),
                       stroke_width=0, fill_color=PURPLE, fill_opacity=0.35)
        bayes = VGroup(label("Bayesian: 95% inside", color=PURPLE),
                       label("needs a prior", color=PURPLE)).arrange(DOWN, buff=0.12)
        bayes.next_to(curve, UP, buff=0.2)
        with self.narrate("The promise has conditions: random sampling, and a model that fits "
                          "the data. And a ninety-five percent chance for one interval is what a "
                          "Bayesian credible interval offers, but only after you choose a "
                          "prior.") as beat:
            self.play(FadeOut(chart), FadeOut(cite4), FadeOut(proc), run_time=0.6)
            self.play(FadeIn(tags[0], shift=0.1 * UP), run_time=beat.until("model", offset=-0.1))
            self.play(FadeIn(tags[1], shift=0.1 * UP), run_time=beat.until("And a", offset=-0.1))
            self.play(Create(bl), FadeIn(bl_title), run_time=beat.until("Bayesian", offset=-0.2))
            self.play(Create(curve), FadeIn(area), FadeIn(bayes[0]),
                      run_time=beat.until("only after", offset=-0.1))
            self.play(FadeIn(bayes[1], shift=0.1 * UP), run_time=beat.until("prior", end=True))

        # ============================================================ 14. landing
        land_bar = Line([0, 0, 0], [1, 0, 0], color=BLUE, stroke_width=9)
        record = label("the machine's record", color=GREEN).next_to(F2b, DOWN, buff=0.35)
        with self.narrate("So, point one to point four. It is one more bar in this stack, with "
                          "the line hidden. Ninety-five percent was the machine's record, never "
                          "this bar's chance.") as beat:
            self.play(FadeOut(VGroup(tags, bl, bl_title, curve, area, bayes)),
                      nl.animate.scale(1 / 0.55).shift(RAIN_CENTER - thumb_target),
                      run_time=1.2)
            self.play(nl.numbers.animate.set_opacity(1), ax_title.animate.set_opacity(1),
                      run_time=0.5)
            land_bar.put_start_and_end_on([self.px(0.1), self.y_at(ROW), 0],
                                          [self.px(0.4), self.y_at(ROW), 0])
            qm = formula("?", size=EQ, color=INK).next_to(land_bar, RIGHT, buff=0.3)
            self.play(GrowFromCenter(land_bar), run_time=beat.until("one more", offset=-0.1))
            self.play(Indicate(land_bar, color=BLUE, scale_factor=1.05), run_time=beat.until("line"))
            self.play(FadeOut(mu_line), self.V.animate.set_value(0), FadeIn(qm),
                      run_time=beat.until("Ninety", offset=-0.1))
            self.play(Indicate(F2b[8], color=GREEN), FadeIn(record, shift=0.1 * UP),
                      run_time=beat.until("never", offset=-0.1))
            self.play(Circumscribe(VGroup(land_bar, qm), color=INK, buff=0.15),
                      run_time=beat.remaining(0.8))
        bars.clear_updaters()
        self.end_card()
