"""Episode 44 - 99.8% Accurate and Completely Useless (ROC vs precision-recall under imbalance).

    videos/toolkit/render.sh --preview videos/episodes/044-roc-pr-class-imbalance/scene.py Episode /tmp/ep44.mp4
"""
from math import erfc, exp, pi, sqrt

import numpy as np
from manim import *
from sample_space import *

# ---------------------------------------------------------------- data (see facts.md)
P, N = 492, 284_315                # real class counts (Dal Pozzolo et al. 2015 dataset)
D = 3.6079                         # simulated: honest ~ N(0,1), fraud ~ N(D,1)
T90 = 2.3263                       # threshold: catches 90% of fraud, flags 1% of honest
T70 = 3.0902                       # threshold: flags 0.1% of honest, catches 69.8%
X_LO, X_HI = -3.0, 7.0


def sf(x):
    return 0.5 * erfc(x / sqrt(2))


def tpr(t):
    return sf(t - D)


def fpr(t):
    return sf(t)


def prec(t):
    a, b = tpr(t) * P, fpr(t) * N
    return a / (a + b) if a + b > 1e-12 else 1.0


def phi(x):
    return exp(-x * x / 2) / sqrt(2 * pi)


def make_waffle():
    """579 squares, ~492 transactions each: 578 honest (blue) + 1 fraud (red, last)."""
    sq = VGroup()
    for i in range(579):
        r, c = divmod(i, 30)
        sq.add(Square(0.15, stroke_width=0, fill_color=BLUE, fill_opacity=0.85)
               .move_to([-6.0 + 0.2 * c, -2.2 + 0.2 * r, 0]))
    sq[-1].set_fill(RED, 1.0)
    return sq


class Episode(NarratedScene):
    EPISODE = 44
    TITLE = "99.8% Accurate and Completely Useless"
    PRONUNCIATIONS = {"Rehmsmeier": "raymz my er", "Saito": "sigh toe", "Plos": "plahss"}

    def construct(self):
        # ============================================================ B0 cold open
        waffle = make_waffle()
        blue_sq, red_sq = VGroup(*waffle[:-1]), waffle[-1]
        heading = label("284,807 card transactions", color=GRAY)
        heading.move_to([-6.075 + heading.width / 2, 2.75, 0])
        red_lbl = label("492 fraud", color=RED).next_to(red_sq, RIGHT, buff=0.2)
        acc0 = formula(r"\text{accuracy}", "=", r"99.8\%", size=EQ).move_to([3.4, 1.2, 0])
        caught = formula(r"\text{frauds caught}", "=", "?", size=MATH + 4).move_to([3.4, -0.2, 0])
        caught[2].set_color(YELLOW)

        with self.narrate("This model is ninety-nine point eight percent accurate on real "
                          "credit card data. Of the four hundred ninety-two frauds in it, how "
                          "many did it catch? [pause 1.5]") as beat:
            self.play(LaggedStart(*[FadeIn(s, scale=0.5) for s in waffle], lag_ratio=0.003),
                      FadeIn(heading), run_time=1.0)
            beat.wait_until("ninety-nine", offset=-0.1)
            self.play(Write(acc0), run_time=1.2)
            beat.wait_until("four hundred", offset=-0.15)
            self.play(Indicate(red_sq, color=RED, scale_factor=2.5), FadeIn(red_lbl, shift=0.1 * LEFT),
                      run_time=1.0)
            beat.wait_until("how", offset=-0.1)
            self.play(Write(caught), run_time=0.9)

        # ============================================================ B1 the do-nothing model
        zero = formula("0", size=MATH + 4, color=RED).move_to(caught[2])
        frame = SurroundingRectangle(waffle, color=BLUE, buff=0.12, stroke_width=3)
        pred = label("every one predicted honest", color=BLUE)
        pred.next_to(frame, UP, buff=0.15).align_to(frame, RIGHT)
        key_sq = Square(0.15, stroke_width=0, fill_color=BLUE, fill_opacity=0.85)
        key_tx = formula(r"\approx 492\ \text{transactions}", size=MATH_SMALL + 6, color=GRAY)
        key = VGroup(key_sq, key_tx).arrange(RIGHT, buff=0.2).move_to([3.4, -1.5, 0])
        acc1 = MathTex(r"\text{accuracy}", "=", r"\frac{578}{579}", "=", r"99.8\%",
                       substrings_to_isolate=["578", "579"], font_size=EQ)
        acc1.move_to(acc0).align_to(acc0, LEFT).shift(LEFT * 0.6)
        fit(acc1, width=5.9)
        if acc1.get_right()[0] > 6.25:
            acc1.shift(LEFT * (acc1.get_right()[0] - 6.25))
        num1, den1 = acc1.get_part_by_tex("578"), acc1.get_part_by_tex("579")
        eqs = acc1.get_parts_by_tex("=")
        frac_bar = VGroup(*[m for m in acc1[2:5] if m is not num1 and m is not den1
                            and m not in eqs and m is not acc1.get_part_by_tex(r"99.8")])
        num1.set_color(BLUE)
        cite1 = citation("Data: Dal Pozzolo et al., 2015 · IEEE SSCI")

        with self.narrate("None. It calls every transaction honest. Each square here is about "
                          "four hundred ninety-two transactions, and the model is wrong only on "
                          "this red one. Five hundred seventy-eight right for every one wrong is "
                          "ninety-nine point eight percent.") as beat:
            self.play(ReplacementTransform(caught[2], zero), FadeIn(cite1), run_time=0.6)
            beat.wait_until("honest", offset=-0.2)
            self.play(Create(frame), FadeIn(pred, shift=0.1 * DOWN), heading.animate.set_opacity(0.0),
                      run_time=0.9)
            beat.wait_until("Each", offset=-0.1)
            self.play(FadeIn(key, shift=0.1 * UP), run_time=0.7)
            beat.wait_until("red one", offset=-0.2)
            self.play(Indicate(red_sq, color=RED, scale_factor=2.5), run_time=0.9)
            beat.wait_until("Five", offset=-0.1)
            self.play(ReplacementTransform(acc0[0], acc1.get_part_by_tex("accuracy")),
                      ReplacementTransform(acc0[1], eqs[0]),
                      ReplacementTransform(acc0[2], acc1.get_part_by_tex("99.8")),
                      FadeIn(eqs[1]), FadeIn(frac_bar),
                      TransformFromCopy(blue_sq, num1),
                      run_time=1.4)
            self.play(TransformFromCopy(waffle, den1), run_time=1.0)
        self.remove(heading)

        # ============================================================ B2 a real model: scores
        ax = axes((X_LO, X_HI), (0, 0.45), x_ticks=[-2, 0, 2, 4, 6], y_ticks=[],
                  x_length=5.8, y_length=3.0, x_label="fraud score (simulated)",
                  y_label="share of each group")
        ax.move_to([-3.2, 0.45, 0])
        baseline_y = ax.c2p(0, 0)[1]

        def area(fn, color, opacity=0.3):
            xs = np.linspace(X_LO, X_HI, 160)
            pts = [ax.c2p(x, fn(x)) for x in xs] + [ax.c2p(X_HI, 0), ax.c2p(X_LO, 0)]
            return Polygon(*pts, stroke_color=color, stroke_width=4, fill_color=color,
                           fill_opacity=opacity)

        blue_area = area(phi, BLUE)
        red_area = area(lambda x: phi(x - D), RED)
        honest_lbl = label("honest", color=BLUE).move_to(ax.c2p(-1.75, 0.33))
        fraud_lbl = label("fraud", color=RED).move_to(ax.c2p(5.45, 0.33))
        guide = DashedLine(ax.c2p(-0.6, phi(0)), ax.c2p(D + 0.6, phi(0)), color=GRAY,
                           stroke_width=2.5, dash_length=0.12)

        th = ValueTracker(5.0)
        rs = ValueTracker(1.0)          # red vertical scale (1 = same height, 1/578 = true)

        def tail(fn, color, scale=lambda: 1.0):
            def build():
                t = th.get_value()
                if t >= X_HI - 0.02:
                    return VMobject()
                xs = np.linspace(max(t, X_LO), X_HI, 70)
                s = scale()
                pts = [ax.c2p(x, fn(x) * s) for x in xs] + [ax.c2p(X_HI, 0), ax.c2p(xs[0], 0)]
                return Polygon(*pts, stroke_width=0, fill_color=color, fill_opacity=0.8)
            return always_redraw(build)

        blue_tail = tail(phi, BLUE)
        red_tail = tail(lambda x: phi(x - D), RED, lambda: rs.get_value())
        thr = always_redraw(lambda: DashedLine(ax.c2p(th.get_value(), 0), ax.c2p(th.get_value(), 0.44),
                                               color=YELLOW, stroke_width=4, dash_length=0.1))

        with self.narrate("A useful model has to hand investigators a short list of alerts. So "
                          "it gives every transaction a fraud score. Here are the scores, "
                          "simulated, with each group drawn to the same height. It flags "
                          "everything to the right of this line.") as beat:
            self.play(FadeOut(acc1), FadeOut(zero), FadeOut(caught[:2]), FadeOut(key),
                      FadeOut(frame), FadeOut(pred), FadeOut(red_lbl), FadeOut(cite1),
                      run_time=0.8)
            beat.wait_until("score", offset=-0.4)
            self.play(Create(ax), run_time=1.0)
            beat.wait_until("Here", offset=-0.1)
            self.play(ReplacementTransform(blue_sq, blue_area), ReplacementTransform(red_sq, red_area),
                      run_time=1.8)
            self.play(FadeIn(honest_lbl), FadeIn(fraud_lbl), run_time=0.6)
            beat.wait_until("same height", offset=-0.2)
            self.play(Create(guide), run_time=0.9)
            beat.wait_until("this line", offset=-0.3)
            self.add(blue_tail, red_tail)
            self.play(Create(thr), run_time=0.6)

        # ============================================================ B3 ROC
        roc = axes((0, 1), (0, 1), x_ticks=[0, 0.5, 1], y_ticks=[0, 0.5, 1], x_length=3.2,
                   y_length=3.2, x_label="honest flagged", y_label="fraud caught")
        roc.move_to([3.85, 0.55, 0])
        ts = np.linspace(X_HI + 0.5, X_LO - 0.5, 400)

        def roc_curve():
            t = th.get_value()
            pts = [roc.c2p(fpr(s), tpr(s)) for s in ts if s >= t] + [roc.c2p(fpr(t), tpr(t))]
            m = VMobject(stroke_color=PURPLE, stroke_width=5)
            m.set_points_as_corners(pts) if len(pts) > 1 else None
            return m
        roc_line = always_redraw(roc_curve)
        roc_dot = always_redraw(lambda: Dot(roc.c2p(fpr(th.get_value()), tpr(th.get_value())),
                                            radius=0.09, color=YELLOW))
        tp_tr = ValueTracker(100 * tpr(5.0))
        fp_tr = ValueTracker(100 * fpr(5.0))
        tp_tr.add_updater(lambda m: m.set_value(100 * tpr(th.get_value())))
        fp_tr.add_updater(lambda m: m.set_value(100 * fpr(th.get_value())))
        self.add(tp_tr, fp_tr)
        rd_c = live_number(tp_tr, 0, size=MATH, color=RED, prefix=r"\text{caught}", suffix=r"\%")
        rd_f = live_number(fp_tr, 1, size=MATH, color=BLUE, prefix=r"\text{flagged}", suffix=r"\%")
        rd_c.move_to([2.55, -2.45, 0])
        rd_f.move_to([5.25, -2.45, 0])
        auc = formula(r"\text{area} = 0.995", size=MATH, color=PURPLE).move_to(roc.c2p(0.6, 0.22))

        with self.narrate("Slide the line, and track two rates: the share of fraud caught, and "
                          "the share of honest purchases flagged. Together they trace the ROC "
                          "curve. It hugs the top-left corner, with an area of point nine nine "
                          "five.") as beat:
            self.play(Create(roc), th.animate.set_value(X_HI), run_time=1.2)
            self.add(roc_line, roc_dot)
            beat.wait_until("caught", offset=-0.2)
            self.play(FadeIn(rd_c), run_time=0.5)
            beat.wait_until("flagged", offset=-0.2)
            self.play(FadeIn(rd_f), run_time=0.5)
            self.play(th.animate.set_value(X_LO), run_time=beat.until("hugs", offset=-0.1),
                      rate_func=EASE)
            self.play(Indicate(roc_line, color=PURPLE, scale_factor=1.04), run_time=0.9)
            beat.wait_until("area", offset=-0.2)
            self.play(Write(auc), run_time=0.9)

        # ============================================================ B4 prediction
        with self.narrate("Park the line here. It catches ninety percent of fraud and flags "
                          "only one percent of honest purchases. When this model raises an "
                          "alert, what is the chance it is really fraud? [pause 2]") as beat:
            self.play(th.animate.set_value(T90), run_time=2.0, rate_func=SMOOTH)
            beat.wait_until("ninety", offset=-0.15)
            self.play(flag(rd_c), run_time=0.8)
            beat.wait_until("one percent", offset=-0.15)
            self.play(flag(rd_f), run_time=0.8)
            beat.wait_until("alert", offset=-0.2)
            self.play(Indicate(VGroup(blue_tail, red_tail), color=YELLOW, scale_factor=1.0),
                      run_time=1.0)

        # ============================================================ B5 fail: 13%
        prec_lbl = formula(r"\text{precision}", "=", r"13\%", size=EQ, color=GREEN)
        prec_lbl.move_to([3.85, 3.05, 0])
        with self.narrate("Thirteen percent. That is the model's precision, and the picture hid "
                          "the reason. I drew both groups at the same height.") as beat:
            self.play(FadeIn(prec_lbl, scale=1.2), run_time=0.7)
            beat.wait_until("precision", offset=-0.2)
            self.play(flag(prec_lbl, color=GREEN), run_time=0.8)
            beat.wait_until("same height", offset=-0.2)
            self.play(Indicate(guide, color=YELLOW, scale_factor=1.0), run_time=1.0)

        # ============================================================ B6 true scale
        roc_grp = VGroup(roc, auc, rd_c, rd_f)
        k = 2.75 / (443 + 2843)
        bar_x = 1.35
        red_seg = Rectangle(width=0.8, height=443 * k, stroke_width=0, fill_color=RED, fill_opacity=0.9)
        red_seg.move_to([bar_x, baseline_y, 0], aligned_edge=DOWN)
        blue_seg = Rectangle(width=0.8, height=2843 * k, stroke_width=0, fill_color=BLUE, fill_opacity=0.9)
        blue_seg.next_to(red_seg, UP, buff=0)
        blue_n = label("2,843 false alarms", color=BLUE).next_to(blue_seg, RIGHT, buff=0.25)
        red_n = label("443 fraud", color=RED).next_to(red_seg, RIGHT, buff=0.25)
        bar_title = label("alerts", color=GRAY).next_to(blue_seg, UP, buff=0.2)
        new_ytitle = label("number of transactions", color=GRAY).move_to(ax.y_title, aligned_edge=LEFT)

        with self.narrate("At true scale, the honest group is five hundred seventy-eight times "
                          "bigger, so the fraud hill flattens into this sliver. Past the line, one "
                          "percent of the honest mountain is two thousand eight hundred "
                          "forty-three false alarms. Ninety percent of the sliver is only four "
                          "hundred forty-three frauds.") as beat:
            for m in (roc_line, roc_dot):
                m.clear_updaters()
            self.play(FadeOut(roc_grp), FadeOut(roc_line), FadeOut(roc_dot), FadeOut(prec_lbl),
                      run_time=0.8)
            self.remove(tp_tr, fp_tr)
            beat.wait_until("five hundred", offset=-0.2)
            self.play(rs.animate.set_value(1 / 578),
                      red_area.animate.stretch(1 / 578, 1, about_point=[0, baseline_y, 0]),
                      fraud_lbl.animate.move_to(ax.c2p(5.45, 0.07)),
                      FadeOut(guide), Transform(ax.y_title, new_ytitle),
                      run_time=beat.until("sliver", offset=-0.1), rate_func=SMOOTH)
            self.play(Indicate(red_area, color=RED, scale_factor=1.0), run_time=0.8)
            beat.wait_until("two thousand", offset=-0.5)
            self.play(FadeIn(bar_title), TransformFromCopy(blue_tail, blue_seg), run_time=1.2)
            self.play(FadeIn(blue_n, shift=0.1 * LEFT), run_time=0.6)
            beat.wait_until("four hundred", offset=-0.5)
            self.play(TransformFromCopy(red_tail, red_seg), run_time=1.2)
            self.play(FadeIn(red_n, shift=0.1 * LEFT), run_time=0.6)

        # ============================================================ B7 formula from the bar
        bar = VGroup(bar_title, blue_seg, red_seg, blue_n, red_n)
        dist = VGroup(ax, blue_area, red_area, honest_lbl, fraud_lbl)
        F1 = MathTex(r"\text{precision} = \frac{443}{443 + 2843}",
                     substrings_to_isolate=["443", "2843"], font_size=EQ)
        F1.move_to([2.3, 0.9, 0])
        f1_num = F1.get_parts_by_tex("443")[0]
        f1_den_r = F1.get_parts_by_tex("443")[1]
        f1_den_b = F1.get_part_by_tex("2843")
        for m in (f1_num, f1_den_r):
            m.set_color(RED)
        f1_den_b.set_color(BLUE)
        f1_rest = VGroup(*[m for m in F1 if m not in (f1_num, f1_den_r, f1_den_b)])

        F2 = MathTex(r"\text{precision} = \frac{0.90 \times 492}{0.90 \times 492 + 0.01 \times 284{,}315}",
                     substrings_to_isolate=["0.90", "492", "0.01", "284{,}315"], font_size=EQ)
        F2.move_to([2.3, 0.9, 0])
        fit(F2, width=7.6)
        F2.move_to([2.3, 0.9, 0])
        for m in F2.get_parts_by_tex("0.90"):
            m.set_color(RED)
        for m in F2.get_parts_by_tex("492"):
            m.set_color(RED)
        F2.get_part_by_tex("0.01").set_color(BLUE)
        F2.get_part_by_tex("284{,}315").set_color(BLUE)

        F3 = MathTex(r"\text{precision} = \frac{1}{1 + \frac{0.01}{0.90} \times 578}",
                     substrings_to_isolate=["0.01", "0.90", "578"], font_size=EQ)
        F3.move_to([2.3, 0.9, 0])
        F3.get_part_by_tex("0.01").set_color(BLUE)
        F3.get_part_by_tex("0.90").set_color(RED)
        F3.get_part_by_tex("578").set_color(YELLOW)
        approx = formula(r"\approx 0.13", size=EQ, color=GREEN).next_to(F3, RIGHT, buff=0.25)
        tail_terms = VGroup(F3.get_part_by_tex("0.01"), F3.get_part_by_tex("0.90"),
                            F3.get_part_by_tex("578"))
        br = Brace(tail_terms, DOWN, buff=0.15, color=GRAY)
        br_lbl = label("6.4 false alarms per fraud", color=INK).next_to(br, DOWN, buff=0.15)

        with self.narrate("Precision is this red part over the whole bar. Write each part as a "
                          "rate times a count. Divide through, and the ratio of the counts, five "
                          "hundred seventy-eight, multiplies the false-alarm rate, giving more "
                          "than six false alarms for every fraud.") as beat:
            for m in (blue_tail, red_tail, thr):
                m.clear_updaters()
            self.play(FadeOut(dist), FadeOut(blue_tail), FadeOut(red_tail), FadeOut(thr),
                      bar.animate.shift(LEFT * 5.8), run_time=1.0)
            self.play(Write(f1_rest[0:1]), run_time=0.6)
            self.play(TransformFromCopy(red_seg, f1_num), run_time=beat.until("whole", offset=-0.1))
            self.play(TransformFromCopy(red_seg, f1_den_r), TransformFromCopy(blue_seg, f1_den_b),
                      FadeIn(f1_rest[1:]), run_time=1.0)
            beat.wait_until("Write", offset=-0.1)
            self.play(ReplacementTransform(f1_rest[0], F2[0]),
                      ReplacementTransform(f1_num, VGroup(*F2[1:4])),
                      ReplacementTransform(f1_den_r, VGroup(*F2[4:7])),
                      ReplacementTransform(f1_den_b, VGroup(*F2[7:])),
                      FadeOut(f1_rest[1:]), run_time=1.5)
            beat.wait_until("Divide", offset=-0.1)
            self.play(TransformMatchingTex(F2, F3, key_map={"284{,}315": "578"}), run_time=1.6)
            beat.wait_until("five hundred", offset=-0.2)
            self.play(flag(F3.get_part_by_tex("578")), run_time=0.8)
            beat.wait_until("giving", offset=-0.1)
            self.play(GrowFromCenter(br), FadeIn(br_lbl, shift=0.1 * DOWN), Write(approx), run_time=1.0)

        # ============================================================ B8 general form
        F4 = MathTex(r"\text{precision} = \frac{1}{1 + \frac{\text{flagged}}{\text{caught}} "
                     r"\times \frac{\text{honest}}{\text{fraud}}}",
                     substrings_to_isolate=[r"\text{flagged}", r"\text{caught}",
                                            r"\frac{\text{honest}}{\text{fraud}}"], font_size=EQ)
        F4.move_to(F3).align_to(F3, LEFT)
        F4.get_part_by_tex("flagged").set_color(BLUE)
        F4.get_part_by_tex("caught").set_color(RED)
        ratio = F4.get_part_by_tex("honest")
        ratio.set_color(YELLOW)
        rates = VGroup(F4.get_part_by_tex("flagged"), F4.get_part_by_tex("caught"))
        roc_box = SurroundingRectangle(rates, color=PURPLE, buff=0.1, corner_radius=0.06)
        ratio_box = SurroundingRectangle(ratio, color=YELLOW, buff=0.1, corner_radius=0.06)
        sees = label("ROC sees", color=PURPLE).next_to(roc_box, DOWN, buff=0.2)
        never = label("ROC never sees", color=YELLOW).next_to(ratio_box, DOWN, buff=0.2)
        if never.get_left()[0] < sees.get_right()[0] + 0.3:
            never.next_to(ratio_box, UP, buff=0.2)

        with self.narrate("The ROC curve plots only the two rates, flagged and caught. The ratio "
                          "of the counts never enters it, which is why it looked so good.") as beat:
            self.play(FadeOut(br), FadeOut(br_lbl), FadeOut(approx), run_time=0.5)
            self.play(TransformMatchingTex(F3, F4, key_map={
                "0.01": r"\text{flagged}", "0.90": r"\text{caught}",
                "578": r"\frac{\text{honest}}{\text{fraud}}"}), run_time=1.5)
            beat.wait_until("flagged", offset=-0.3)
            self.play(Create(roc_box), FadeIn(sees), run_time=0.8)
            beat.wait_until("ratio", offset=-0.2)
            self.play(Create(ratio_box), FadeIn(never), run_time=0.8)

        # ============================================================ B9 precision-recall
        roc2 = axes((0, 1), (0, 1), x_ticks=[0, 0.5, 1], y_ticks=[0, 0.5, 1], x_length=3.0,
                    y_length=3.0, x_label="honest flagged", y_label="fraud caught")
        roc2.move_to([-3.1, -0.55, 0])
        pr = axes((0, 1), (0, 1), x_ticks=[0, 0.5, 1], y_ticks=[0, 0.5, 1], x_length=3.0,
                  y_length=3.0, x_label="fraud caught", y_label="precision")
        pr.move_to([3.3, -0.55, 0])
        pr.y_title.set_color(GREEN)
        th.set_value(X_HI)

        def traced(axx, fx, fy, color):
            def build():
                t = th.get_value()
                pts = [axx.c2p(fx(s), fy(s)) for s in ts if s >= t] + [axx.c2p(fx(t), fy(t))]
                m = VMobject(stroke_color=color, stroke_width=5)
                if len(pts) > 1:
                    m.set_points_as_corners(pts)
                return m
            return always_redraw(build)
        roc_line2 = traced(roc2, fpr, tpr, PURPLE)
        pr_line = traced(pr, tpr, prec, GREEN)
        dot_r = always_redraw(lambda: Dot(roc2.c2p(fpr(th.get_value()), tpr(th.get_value())),
                                          radius=0.09, color=YELLOW))
        dot_p = always_redraw(lambda: Dot(pr.c2p(tpr(th.get_value()), prec(th.get_value())),
                                          radius=0.09, color=YELLOW))
        base = ValueTracker(0.5)
        base_line = always_redraw(lambda: DashedLine(pr.c2p(0, base.get_value()), pr.c2p(1, base.get_value()),
                                                     color=GRAY, stroke_width=3, dash_length=0.1))
        base_lbl = always_redraw(lambda: label("random model", color=GRAY, size=SMALL + 4)
                                 .next_to(pr.c2p(1, base.get_value()), RIGHT, buff=0.15))
        base_val = label("0.17%", color=GRAY, size=SMALL + 4)
        F4_small_target = VGroup(F4, roc_box, ratio_box, sees, never)

        with self.narrate("So plot precision against fraud caught instead. Slide the line "
                          "again. Where the ROC curve hugged its corner, this one sags, and a "
                          "random model would sit at point one seven percent, not fifty.") as beat:
            self.play(FadeOut(bar), FadeOut(roc_box), FadeOut(ratio_box), FadeOut(sees), FadeOut(never),
                      F4.animate.scale(0.72).move_to([0.1, 2.85, 0]).set_color(INK), run_time=1.0)
            self.play(FadeIn(roc2), Create(pr), run_time=beat.until("Slide", offset=-0.1))
            self.add(roc_line2, pr_line, dot_r, dot_p)
            self.play(th.animate.set_value(X_LO), run_time=beat.until("sags", offset=0.2), rate_func=EASE)
            beat.wait_until("random", offset=-0.2)
            self.play(Create(base_line), FadeIn(base_lbl), run_time=0.7)
            beat.wait_until("point one", offset=-0.2)
            base_val.next_to(pr.c2p(1, 0.0017), RIGHT, buff=0.15).shift(DOWN * 0.05)
            self.play(base.animate.set_value(0.0017), run_time=1.4, rate_func=SMOOTH)
            base_lbl.clear_updaters()
            self.play(base_lbl.animate.next_to(base_val, UP, buff=0.12).align_to(base_val, LEFT),
                      FadeIn(base_val), run_time=0.6)

        # ============================================================ B10 the trade
        rc_tr = ValueTracker(100 * tpr(X_LO))
        pc_tr = ValueTracker(100 * prec(X_LO))
        rc_tr.add_updater(lambda m: m.set_value(100 * tpr(th.get_value())))
        pc_tr.add_updater(lambda m: m.set_value(100 * prec(th.get_value())))
        self.add(rc_tr, pc_tr)
        rd_rc = live_number(rc_tr, 0, size=MATH, color=RED, prefix=r"\text{caught}", suffix=r"\%")
        rd_pc = live_number(pc_tr, 0, size=MATH, color=GREEN, prefix=r"\text{precision}", suffix=r"\%")
        rd_rc.move_to([-1.0, -2.75, 0])
        rd_pc.move_to([2.6, -2.75, 0])

        with self.narrate("Every point is a trade. Raise the line, and you catch seventy percent "
                          "of fraud, but now more than half the alerts are real. The right point "
                          "depends on what a missed fraud costs, against an investigator's "
                          "hour.") as beat:
            self.play(th.animate.set_value(T90), FadeIn(rd_rc), FadeIn(rd_pc),
                      run_time=beat.until("Raise", offset=-0.1), rate_func=SMOOTH)
            self.play(th.animate.set_value(T70), run_time=beat.until("seventy", offset=0.1),
                      rate_func=SMOOTH)
            self.play(flag(rd_rc), run_time=0.8)
            beat.wait_until("half", offset=-0.2)
            self.play(flag(rd_pc, color=GREEN), run_time=0.8)
            beat.wait_until("missed", offset=-0.2)
            self.play(th.animate.set_value(2.7), run_time=1.6, rate_func=there_and_back)
            beat.wait_until("investigator", offset=-0.2)
            self.play(th.animate.set_value(3.5), run_time=1.6, rate_func=there_and_back)

        # ============================================================ B11 payoff
        for m in (roc_line2, pr_line, dot_r, dot_p):
            m.clear_updaters()
        W = 6.6
        x0 = -2.2
        track1 = Rectangle(width=W, height=0.5, stroke_color=GRAY, stroke_width=2, fill_opacity=0)
        track2 = track1.copy()
        track1.move_to([x0 + W / 2, 0.55, 0])
        track2.move_to([x0 + W / 2, -0.75, 0])
        fill1 = Rectangle(width=W * 22 / 33, height=0.5, stroke_width=0, fill_color=PURPLE, fill_opacity=0.9)
        fill1.move_to(track1, aligned_edge=LEFT)
        fill2 = Rectangle(width=W * 4 / 33, height=0.5, stroke_width=0, fill_color=GREEN, fill_opacity=0.9)
        fill2.move_to(track2, aligned_edge=LEFT)
        n1 = label("ROC", color=PURPLE).next_to(track1, LEFT, buff=0.3)
        n2 = label("precision-recall", color=GREEN).next_to(track2, LEFT, buff=0.3)
        v1 = formula(r"22", size=MATH, color=INK).next_to(fill1, RIGHT, buff=0.2)
        v2 = formula(r"4", size=MATH, color=INK).next_to(fill2, RIGHT, buff=0.2)
        hdr = label("33 imbalanced genome-wide studies", color=GRAY).move_to([x0 + W / 2 - 0.4, 1.55, 0])
        cite2 = citation("Saito & Rehmsmeier, 2015 · PLoS ONE")

        with self.narrate("Saito and Rehmsmeier made this case in Plos One in twenty fifteen. Of "
                          "thirty-three genome-wide studies with imbalanced data that they "
                          "reviewed, twenty-two judged their models by ROC, and only four by "
                          "precision-recall. ROC is not wrong. It measures ranking, and ranking "
                          "ignores how rare the positives are.") as beat:
            self.play(FadeOut(VGroup(roc2, pr, roc_line2, pr_line, dot_r, dot_p, base_line, base_lbl,
                                     base_val, rd_rc, rd_pc)), FadeIn(cite2), run_time=0.9)
            self.remove(rc_tr, pc_tr)
            beat.wait_until("thirty-three", offset=-0.2)
            self.play(FadeIn(hdr), Create(track1), Create(track2), FadeIn(n1), FadeIn(n2), run_time=1.0)
            beat.wait_until("twenty-two", offset=-0.2)
            self.play(GrowFromEdge(fill1, LEFT), FadeIn(v1), run_time=1.0)
            beat.wait_until("four", offset=-0.2)
            self.play(GrowFromEdge(fill2, LEFT), FadeIn(v2), run_time=0.8)
            beat.wait_until("ranking", offset=-0.2)
            ratio_y = F4.get_part_by_tex("honest")
            self.play(ratio_y.animate.set_color(YELLOW), run_time=0.6)
            beat.wait_until("ignores", offset=-0.1)
            self.play(Create(SurroundingRectangle(ratio_y, color=YELLOW, buff=0.08, corner_radius=0.06)),
                      run_time=0.8)

        # ============================================================ B12 landing
        waffle2 = make_waffle()
        accL = formula(r"\text{accuracy}", "=", r"99.8\%", size=EQ).move_to([3.4, 0.6, 0])
        accR = formula(r"\text{honest share}", "=", r"99.8\%", size=EQ).move_to([3.4, 0.6, 0])
        accR[0].set_color(BLUE)
        with self.narrate("Back to the red square. Ninety-nine point eight percent never described "
                          "the model. It described how rare fraud is.") as beat:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)
            self.play(LaggedStart(*[FadeIn(s, scale=0.5) for s in waffle2], lag_ratio=0.002),
                      run_time=1.0)
            self.play(Indicate(waffle2[-1], color=RED, scale_factor=2.5), run_time=0.8)
            beat.wait_until("Ninety", offset=-0.1)
            self.play(Write(accL), run_time=1.0)
            beat.wait_until("described", 2, offset=-0.1)
            self.play(TransformMatchingTex(accL, accR), run_time=1.2)
        self.end_card()
