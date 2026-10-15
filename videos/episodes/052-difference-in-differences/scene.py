"""Episode 52 - difference-in-differences, told through Card & Krueger (1994).

    videos/toolkit/render.sh videos/episodes/052-difference-in-differences/scene.py Episode \
        videos/episodes/052-difference-in-differences/final.mp4

Palette: PURPLE = New Jersey (treated) · BLUE = Pennsylvania (control) ·
YELLOW = estimated effect of the raise · RED = bias (how far a naive estimate is off).
"""
import numpy as np
from manim import *
from sample_space import *

# Card & Krueger (1994), Table 3: mean FTE employment per store (rows 1-2).
NJ0, NJ1 = 20.44, 21.03
PA0, PA1 = 23.33, 21.17
D_NJ = round(NJ1 - NJ0, 2)          # +0.59
D_PA = round(PA1 - PA0, 2)          # -2.16
GHOST = round(NJ0 + D_PA, 2)        # 18.28
DID = round(D_NJ - D_PA, 2)         # 2.75 (paper: 2.76 from unrounded means)
AX = 1.12                           # x-position of the change arrows (just right of "after")


def varrow(ax, x, y0, y1, color, width=6):
    a = Arrow(ax.c2p(x, y0), ax.c2p(x, y1), buff=0, color=color, stroke_width=width,
              max_tip_length_to_length_ratio=0.3, max_stroke_width_to_length_ratio=20)
    return a


def vbracket(ax, x, y0, y1, color, tick=0.12, width=5):
    p0, p1 = ax.c2p(x, y0), ax.c2p(x, y1)
    return VGroup(Line(p0, p1, color=color, stroke_width=width),
                  Line(p0 + LEFT * tick, p0 + RIGHT * tick, color=color, stroke_width=width),
                  Line(p1 + LEFT * tick, p1 + RIGHT * tick, color=color, stroke_width=width))


def jitter_grid(n, x0, x1, y0, y1, cols, rng):
    rows = int(np.ceil(n / cols))
    xs = np.linspace(x0, x1, cols)
    ys = np.linspace(y1, y0, rows)
    pts = [(x, y) for y in ys for x in xs][:n]
    return [np.array([x + rng.uniform(-0.07, 0.07), y + rng.uniform(-0.06, 0.06), 0])
            for x, y in pts]


class Episode(NarratedScene):
    EPISODE = 52
    TITLE = "The Minimum Wage Study That Used New Jersey as a Lab"
    PRONUNCIATIONS = {"Krueger": "kroo ger", "Wascher": "wash er", "Neumark": "noy mark"}

    def construct(self):
        rng = np.random.default_rng(7)

        # ================================================================ 1. cold open
        border = DashedLine(UP * 2.9, DOWN * 2.6, color=GRAY, stroke_width=2, dash_length=0.12)
        pa_name = text("Pennsylvania", size=HEADING, color=BLUE).move_to([-3.3, 3.2, 0])
        nj_name = text("New Jersey", size=HEADING, color=PURPLE).move_to([3.3, 3.2, 0])
        date = text("April 1, 1992", size=LABEL, color=INK).move_to([0, 3.2, 0])
        base_y, k = -2.0, 0.8
        pa_bar = Rectangle(width=1.5, height=4.25 * k, stroke_width=0, fill_color=BLUE,
                           fill_opacity=0.85).move_to([-3.3, base_y, 0], aligned_edge=DOWN)
        nj_bar = Rectangle(width=1.5, height=4.25 * k, stroke_width=0, fill_color=PURPLE,
                           fill_opacity=0.85).move_to([3.3, base_y, 0], aligned_edge=DOWN)
        nj_top = Rectangle(width=1.5, height=0.80 * k, stroke_width=0, fill_color=PURPLE,
                           fill_opacity=0.5).move_to(nj_bar.get_top(), aligned_edge=DOWN)
        pa_wage = text("$4.25 / hour", size=BODY, color=BLUE).next_to(pa_bar, UP, buff=0.2)
        nj_wage = text("$4.25 / hour", size=BODY, color=PURPLE).next_to(nj_bar, UP, buff=0.2)
        nj_wage2 = text("$5.05 / hour", size=BODY, color=PURPLE).next_to(nj_top, UP, buff=0.2)
        plus80 = text("+80¢", size=LABEL, color=PURPLE).next_to(nj_top, LEFT, buff=0.2)
        mw_lab = VGroup(text("minimum wage", size=LABEL - 2, color=GRAY).next_to(pa_bar, DOWN, buff=0.2),
                        text("minimum wage", size=LABEL - 2, color=GRAY).next_to(nj_bar, DOWN, buff=0.2))
        jobs = text("jobs", size=BODY, color=INK).move_to([5.45, 1.0, 0])
        jobs_arrow = Arrow([5.45, 0.65, 0], [5.45, -0.85, 0], buff=0, color=GRAY, stroke_width=6)
        qmark = text("?", size=64, color=YELLOW).next_to(jobs_arrow, RIGHT, buff=0.2)

        with self.narrate("April first, nineteen ninety-two. New Jersey raises its minimum wage "
                          "from four twenty-five to five oh five an hour.") as beat:
            self.play(Create(border), FadeIn(date), FadeIn(pa_name), FadeIn(nj_name),
                      run_time=0.6)
            self.play(GrowFromEdge(pa_bar, DOWN), GrowFromEdge(nj_bar, DOWN),
                      FadeIn(pa_wage), FadeIn(nj_wage), FadeIn(mw_lab),
                      run_time=beat.until("four twenty", offset=-0.2))
            self.play(flag(nj_wage), run_time=beat.until("five oh", offset=-0.15))
            self.play(GrowFromEdge(nj_top, DOWN), ReplacementTransform(nj_wage, nj_wage2),
                      FadeIn(plus80, shift=0.2 * UP), run_time=1.2)
        with self.narrate("Pennsylvania, next door, stays at four twenty-five.") as beat:
            self.play(Indicate(pa_bar, color=BLUE, scale_factor=1.04),
                      flag(pa_wage), run_time=beat.until("stays", offset=-0.1))
            self.play(Indicate(pa_wage, color=BLUE, scale_factor=1.08), run_time=1.0)
        with self.narrate("Textbook economics says New Jersey's fast-food restaurants should now "
                          "cut jobs. Did they? Make your guess now. [pause 1.6]") as beat:
            beat.wait_until("fast", offset=-0.2)
            self.play(FadeIn(jobs, shift=0.15 * DOWN), run_time=0.6)
            self.play(GrowArrow(jobs_arrow), run_time=beat.until("cut", offset=0.2))
            beat.wait_until("Did", offset=-0.1)
            self.play(FadeIn(qmark, scale=0.6), run_time=0.6)
            beat.wait_until("guess", offset=0.2)
            self.play(Indicate(qmark, color=YELLOW, scale_factor=1.15), run_time=1.0)

        # ================================================================ 2. the survey
        pa_chip = text("$4.25", size=LABEL, color=BLUE).move_to([-3.3, 2.55, 0])
        nj_chip = text("$4.25 → $5.05", size=LABEL, color=PURPLE).move_to([3.3, 2.55, 0])
        nj_pts = jitter_grid(331, 0.75, 5.85, -1.85, 1.75, 19, rng)
        pa_pts = jitter_grid(79, -3.05, -0.75, -0.25, 1.75, 9, rng)
        nj_dots = VGroup(*[Dot(p, radius=0.055, color=PURPLE) for p in nj_pts])
        pa_dots = VGroup(*[Dot(p, radius=0.055, color=BLUE) for p in pa_pts])
        nj_count = text("331 restaurants", size=LABEL, color=PURPLE).move_to([3.3, -2.35, 0])
        pa_count = text("79 restaurants", size=LABEL, color=BLUE).next_to(pa_dots, DOWN, buff=0.3)
        cite = citation("Card & Krueger, 1994 · American Economic Review 84(4)")
        wave1 = text("Feb–Mar 1992", size=LABEL, color=INK).move_to([0, 3.2, 0])
        wave2 = text("Nov–Dec 1992", size=LABEL, color=INK).move_to([0, 3.2, 0])
        for w in (wave1, wave2):
            w.add_background_rectangle(color=BG, opacity=1, buff=0.1)

        with self.narrate("You can't randomly assign a minimum wage to a state. So two economists, "
                          "David Card and Alan Krueger, surveyed four hundred and ten fast-food "
                          "restaurants on both sides of the border, once just before the raise, "
                          "and again eight months after.") as beat:
            self.play(FadeOut(VGroup(jobs, jobs_arrow, qmark, plus80, mw_lab)),
                      ReplacementTransform(VGroup(pa_bar, pa_wage), pa_chip),
                      ReplacementTransform(VGroup(nj_bar, nj_top, nj_wage2), nj_chip),
                      run_time=1.2)
            beat.wait_until("David", offset=-0.2)
            self.play(FadeIn(cite, shift=0.1 * UP), run_time=0.6)
            beat.wait_until("four hundred", offset=-0.3)
            self.play(LaggedStart(*[GrowFromCenter(d) for d in nj_dots], lag_ratio=0.004),
                      LaggedStart(*[GrowFromCenter(d) for d in pa_dots], lag_ratio=0.015),
                      run_time=beat.until("both", offset=-0.1))
            self.play(FadeIn(nj_count), FadeIn(pa_count), run_time=0.7)
            beat.wait_until("once", offset=-0.1)
            self.play(FadeOut(date), FadeIn(wave1), run_time=0.5)
            self.play(LaggedStart(Indicate(pa_dots, color=INK, scale_factor=1.0),
                                  Indicate(nj_dots, color=INK, scale_factor=1.0), lag_ratio=0.2),
                      run_time=beat.until("again", offset=-0.1))
            self.play(ReplacementTransform(wave1, wave2), run_time=0.5)
            self.play(LaggedStart(Indicate(pa_dots, color=INK, scale_factor=1.0),
                                  Indicate(nj_dots, color=INK, scale_factor=1.0), lag_ratio=0.2),
                      run_time=max(1.0, beat.remaining() - 0.2))

        # ================================================================ 3. the measure + chart
        ax = axes((-0.9, 2.55), (17, 24), x_length=7.3, y_length=5.0, numbers=False,
                  x_ticks=[0, 1], y_ticks=[18, 20, 22, 24])
        ax.shift(np.array([-5.55, -2.25, 0]) - ax.c2p(-0.9, 17))
        ax.y_axis.add_numbers(x_values=[18, 20, 22, 24], font_size=MATH_SMALL, color=GRAY)
        y_title = text("workers per store (full-time equivalent)", size=LABEL, color=GRAY)
        y_title.next_to(ax.c2p(-0.9, 24), UP, buff=0.3).align_to(ax.y_axis.numbers, LEFT)
        xt = VGroup()
        for xv, a, b in ((0, "before raise", "Feb–Mar 1992"), (1, "after raise", "Nov–Dec 1992")):
            g = VGroup(text(a, size=LABEL - 2, color=INK), text(b, size=SMALL, color=GRAY))
            g.arrange(DOWN, buff=0.08).next_to(ax.c2p(xv, 17), DOWN, buff=0.18)
            xt.add(g)
        fte = formula(r"\text{worker count}", "=", r"\text{full-time}", "+",
                      r"\tfrac{1}{2}\times\text{part-time}", size=MATH).move_to([0, 3.2, 0])
        fte[4].set_color(INK)

        def P(x, y):
            return ax.c2p(x, y)

        nj0 = Dot(P(0, NJ0), radius=0.09, color=PURPLE).set_z_index(3)
        pa0 = Dot(P(0, PA0), radius=0.09, color=BLUE).set_z_index(3)
        nj1 = Dot(P(1, NJ1), radius=0.09, color=PURPLE).set_z_index(3)
        pa1 = Dot(P(1, PA1), radius=0.09, color=BLUE).set_z_index(3)
        lab = lambda s, c: formula(s, size=MATH_SMALL + 2, color=c)
        nj0_l = lab("20.44", PURPLE).next_to(nj0, LEFT, buff=0.2)
        pa0_l = lab("23.33", BLUE).next_to(pa0, LEFT, buff=0.2)
        nj1_l = lab("21.03", PURPLE).next_to(nj1, DR, buff=0.08)
        pa1_l = lab("21.17", BLUE).next_to(pa1, UR, buff=0.08)

        with self.narrate("At each store they counted workers, with a part-timer as half a "
                          "worker, and averaged.") as beat:
            self.play(FadeOut(VGroup(border, pa_name, nj_name, pa_chip, nj_chip, nj_count,
                                     pa_count, cite)),
                      wave2.animate.set_opacity(0), run_time=0.6)
            self.remove(wave2)
            self.play(Write(fte[0:3]), run_time=beat.until("part", offset=-0.1))
            self.play(Write(fte[3:]), run_time=beat.until("averaged", offset=-0.3))
            self.play(Create(ax), FadeIn(xt), ReplacementTransform(fte, y_title),
                      ReplacementTransform(nj_dots, nj0), ReplacementTransform(pa_dots, pa0),
                      run_time=1.6)
            self.play(FadeIn(nj0_l), FadeIn(pa0_l), pa0.animate.set_opacity(0.3),
                      pa0_l.animate.set_opacity(0.3), run_time=0.6)

        # ---- ledger (right panel)
        LX0, LX1 = 2.0, 6.35
        led_head = text("estimated effect of the raise", size=LABEL - 2, color=GRAY)
        led_head.move_to([(LX0 + LX1) / 2, 3.15, 0])
        led_rule = Line([LX0, 2.85, 0], [LX1, 2.85, 0], color=DIM, stroke_width=2)

        def row_label(s, t2c, y):
            m = text(s, size=LABEL, color=INK, t2c=t2c)
            return m.move_to([LX0 + m.width / 2, y, 0])

        def row_num(s, y, color=YELLOW):
            m = formula(s, size=MATH + 4, color=color)
            return m.move_to([LX1 - m.width / 2, y, 0])

        r1y, r2y, r3y = 2.3, 1.45, 0.6
        r1 = row_label("NJ after − NJ before", {"NJ": PURPLE}, r1y)
        r2 = row_label("NJ − PA, after raise", {"NJ": PURPLE, "PA": BLUE}, r2y)
        n1 = row_num("+0.59", r1y)
        n2 = row_num("-0.14", r2y)

        # ================================================================ 4. naive 1
        nj_seg = Line(P(0, NJ0), P(1, NJ1), color=PURPLE, stroke_width=5)
        pa_seg = Line(P(0, PA0), P(1, PA1), color=BLUE, stroke_width=5)
        nj_guide = DashedLine(P(0, NJ0), P(AX, NJ0), color=PURPLE, stroke_width=2,
                              dash_length=0.08).set_opacity(0.6)
        nj_arrow = varrow(ax, AX, NJ0, NJ1, PURPLE)
        nj_d_l = lab("+0.59", PURPLE).next_to(nj_arrow, RIGHT, buff=0.15)

        with self.narrate("Start with the obvious comparison. The average New Jersey store had "
                          "twenty point four workers before the raise, and twenty-one point oh "
                          "after. Up by point five nine. So the raise added jobs.") as beat:
            self.play(FadeIn(led_head), Create(led_rule), run_time=0.8)
            beat.wait_until("twenty point", offset=-0.2)
            self.play(flag(nj0), flag(nj0_l), run_time=0.8)
            beat.wait_until("twenty-one", offset=-0.3)
            self.play(Create(nj_seg), GrowFromPoint(nj1, nj0.get_center()), run_time=1.0)
            self.play(FadeIn(nj1_l), run_time=0.5)
            self.play(Create(nj_guide), run_time=beat.until("Up", offset=-0.1, min_time=0.4))
            self.play(GrowArrow(nj_arrow), FadeIn(nj_d_l), run_time=0.8)
            beat.wait_until("So the", offset=-0.1)
            self.play(FadeIn(r1), TransformFromCopy(nj_d_l, n1), run_time=1.2)

        conf1 = text("+ everything else\nthat changed", size=LABEL - 2, color=RED,
                     line_spacing=0.8)
        conf1.next_to(nj_d_l, RIGHT, buff=0.25).shift(DOWN * 0.15)
        rec = text("recession year", size=LABEL - 2, color=RED)
        with self.narrate("Except nineteen ninety-two was a recession year. This comparison "
                          "credits the wage with everything else that changed between the two "
                          "surveys.") as beat:
            beat.wait_until("recession", offset=-0.2)
            rec.next_to(n1, DOWN, buff=0.12).align_to(n1, RIGHT)
            self.play(FadeIn(rec, shift=0.1 * DOWN), run_time=0.6)
            beat.wait_until("everything", offset=-0.2)
            self.play(FadeIn(conf1), Indicate(nj_arrow, color=RED, scale_factor=1.1),
                      run_time=1.0)
            self.play(Circumscribe(n1, color=RED, buff=0.12), run_time=beat.remaining(1.0))

        # ================================================================ 5. naive 2
        after_gap = vbracket(ax, 1.0, NJ1, PA1, YELLOW, tick=0.08, width=4)
        with self.narrate("So compare the two states after the raise instead. Pennsylvania "
                          "stores averaged twenty-one point two, so New Jersey is point one four "
                          "lower, and the raise cost jobs. Two obvious methods, two different "
                          "signs.") as beat:
            self.play(FadeOut(conf1), FadeOut(rec), FadeOut(nj_guide),
                      nj_arrow.animate.set_opacity(0.0), nj_d_l.animate.set_opacity(0.0),
                      run_time=0.6)
            self.remove(nj_arrow, nj_d_l)
            beat.wait_until("Pennsylvania", offset=-0.2)
            self.play(FadeIn(pa1, scale=0.5), FadeIn(pa1_l), run_time=0.8)
            beat.wait_until("point one four", offset=-0.25)
            self.play(Indicate(VGroup(nj1, pa1), color=INK, scale_factor=1.3), run_time=0.8)
            beat.wait_until("cost", offset=-0.3)
            self.play(FadeIn(r2), TransformFromCopy(VGroup(nj1_l, pa1_l), n2), run_time=1.0)
            beat.wait_until("Two obvious", offset=-0.1)
            self.play(flag(n1), run_time=0.7)
            self.play(flag(n2), run_time=0.7)

        gap0 = vbracket(ax, -0.14, NJ0, PA0, RED, tick=0.09)
        gap0_l = lab("-2.89", RED).next_to(gap0, LEFT, buff=0.15)
        with self.narrate("This one credits the wage with every way the states differed. Before "
                          "any raise, New Jersey's stores were already two point eight nine "
                          "workers smaller.") as beat:
            beat.wait_until("Before", offset=-0.2)
            self.play(pa0.animate.set_opacity(1), pa0_l.animate.set_opacity(1),
                      nj0_l.animate.shift(LEFT * 0.0), run_time=0.6)
            self.play(Create(pa_seg), run_time=beat.until("already", offset=-0.1))
            # move the before-labels out of the bracket's way
            self.play(nj0_l.animate.next_to(nj0, DOWN, buff=0.15),
                      pa0_l.animate.next_to(pa0, UP, buff=0.15), run_time=0.6)
            self.play(Create(gap0), FadeIn(gap0_l), run_time=beat.until("smaller", offset=0.0,
                                                                         min_time=0.5))
            off2 = formula("-2.89", size=MATH_SMALL + 2, color=RED)
            off2.next_to(n2, DOWN, buff=0.12).align_to(n2, RIGHT)
            self.play(TransformFromCopy(gap0_l, off2), run_time=beat.remaining(0.8))

        # ================================================================ 6. insight
        pa_guide = DashedLine(P(0, PA0), P(AX, PA0), color=BLUE, stroke_width=2,
                              dash_length=0.08).set_opacity(0.6)
        pa_arrow = varrow(ax, AX, PA0, PA1, BLUE)
        pa_d_l = lab("-2.16", BLUE).next_to(pa_arrow, RIGHT, buff=0.15)
        with self.narrate("Pennsylvania never got the raise. Its drop, two point one six workers, "
                          "shows what those months did to a restaurant with no new wage. So where "
                          "would New Jersey have ended up, on that same path? [pause 1.2]") as beat:
            self.play(FadeOut(pa1_l), FadeOut(nj1_l), run_time=0.5)
            self.play(Indicate(pa_seg, color=BLUE, scale_factor=1.0), flag(pa0),
                      run_time=beat.until("drop", offset=-0.3, min_time=0.5))
            self.play(Create(pa_guide), run_time=0.5)
            self.play(GrowArrow(pa_arrow), FadeIn(pa_d_l), run_time=1.0)
            beat.wait_until("where", offset=-0.1)
            self.play(Indicate(nj0, color=PURPLE, scale_factor=1.6),
                      Indicate(nj0_l, color=PURPLE), run_time=1.0)
            self.play(Indicate(pa_arrow, color=BLUE, scale_factor=1.1), run_time=1.0)

        ghost_arrow = varrow(ax, AX, NJ0, GHOST, BLUE)
        ghost_dot = Dot(P(1, GHOST), radius=0.09, color=PURPLE, fill_opacity=0.0,
                        stroke_width=3).set_stroke(PURPLE).set_z_index(3)
        ghost_seg = DashedLine(P(0, NJ0), P(1, GHOST), color=PURPLE, stroke_width=4,
                               dash_length=0.14)
        ghost_l = lab("18.3", PURPLE).next_to(ghost_dot, DL, buff=0.08)
        ghost_name = text("NJ without the raise", size=LABEL - 2, color=PURPLE)
        nj_arrow2 = varrow(ax, AX, NJ0, NJ1, PURPLE)
        nj_d_l2 = lab("+0.59", PURPLE).next_to(nj_arrow2, RIGHT, buff=0.15)
        gap_br = vbracket(ax, 1.9, GHOST, NJ1, YELLOW, tick=0.12, width=6)
        gap_l = formula("2.75", size=MATH + 4, color=YELLOW).next_to(gap_br, RIGHT, buff=0.15)
        with self.narrate("Slide Pennsylvania's drop onto New Jersey's starting point. This "
                          "dashed line is New Jersey without the raise, at eighteen point three. "
                          "The real New Jersey is at twenty-one. That gap, two point seven five "
                          "workers per store, is the estimate.") as beat:
            moving = pa_arrow.copy()
            self.add(moving)
            nj_guide2 = DashedLine(P(0, NJ0), P(AX, NJ0), color=PURPLE, stroke_width=2,
                                   dash_length=0.08).set_opacity(0.6)
            self.play(Create(nj_guide2), run_time=0.5)
            self.play(Transform(moving, ghost_arrow), pa_d_l.copy().animate.move_to(
                ghost_arrow.get_right() + RIGHT * 0.15 + RIGHT * pa_d_l.width / 2).set_opacity(0),
                run_time=beat.until("This", offset=-0.1, min_time=1.2))
            ghost_d_l = lab("-2.16", BLUE).next_to(ghost_arrow, RIGHT, buff=0.15)
            self.play(Create(ghost_seg), FadeIn(ghost_dot), FadeIn(ghost_d_l),
                      run_time=beat.until("eighteen", offset=-0.2))
            ghost_name.next_to(ghost_seg.get_center(), DOWN, buff=0.35).shift(LEFT * 0.25)
            self.play(FadeIn(ghost_l), FadeIn(ghost_name), run_time=0.6)
            beat.wait_until("real", offset=-0.1)
            self.play(GrowArrow(nj_arrow2), FadeIn(nj_d_l2), flag(nj1), run_time=0.9)
            beat.wait_until("gap", offset=-0.25)
            self.play(TransformFromCopy(VGroup(moving, nj_arrow2), gap_br),
                      run_time=beat.until("two point seven", offset=-0.1, min_time=0.8))
            self.play(FadeIn(gap_l, shift=0.1 * RIGHT), run_time=0.6)
            beat.wait_until("estimate", offset=-0.1)
            self.play(Circumscribe(gap_l, color=YELLOW, buff=0.1), run_time=1.0)

        # ---- equation built from the three arrows
        eq = formula(r"(+0.59)", "-", r"(-2.16)", "=", r"2.75", size=MATH + 4)
        eq[0].set_color(PURPLE); eq[2].set_color(BLUE); eq[4].set_color(YELLOW)
        eq.move_to([(LX0 + LX1) / 2, -0.75, 0])
        gen = formula(r"\Delta_{\text{NJ}}", "-", r"\Delta_{\text{PA}}", "=", r"\delta",
                      size=EQ)
        gen[0].set_color(PURPLE); gen[2].set_color(BLUE); gen[4].set_color(YELLOW)
        gen.move_to([(LX0 + LX1) / 2, -1.85, 0])
        did_name = text("a difference in differences", size=LABEL, color=INK)
        did_name.next_to(gen, DOWN, buff=0.3)
        with self.narrate("Written out, it's New Jersey's change minus Pennsylvania's change. "
                          "A difference in differences.") as beat:
            self.play(TransformFromCopy(nj_d_l2, eq[0]), run_time=beat.until("minus", offset=-0.2,
                                                                                min_time=0.8))
            self.play(Write(eq[1]), TransformFromCopy(ghost_d_l, eq[2]),
                      run_time=beat.until("change", occurrence=2, offset=0.3, min_time=0.8))
            self.play(Write(eq[3]), TransformFromCopy(gap_l, eq[4]), run_time=0.8)
            beat.wait_until("difference", offset=-0.3)
            self.play(TransformFromCopy(eq, gen), run_time=1.2)
            self.play(FadeIn(did_name, shift=0.1 * UP), run_time=beat.remaining(0.6))

        # ================================================================ 6b. repairs both naive answers
        off1 = formula("-2.16", size=MATH_SMALL + 2, color=RED)
        off1.next_to(n1, DOWN, buff=0.12).align_to(n1, RIGHT)
        r3 = row_label("difference in differences", {}, r3y)
        n3 = row_num("+2.75", r3y)
        with self.narrate("It also repairs both naive answers. Plus point five nine was off by "
                          "Pennsylvania's drop. Minus point one four was off by the starting "
                          "gap. Correct either one, and you land on the same two point seven "
                          "five.") as beat:
            self.play(FadeOut(did_name), run_time=0.5)
            beat.wait_until("Plus", offset=-0.2)
            self.play(flag(n1), run_time=0.6)
            beat.wait_until("off by", offset=-0.1)
            self.play(TransformFromCopy(ghost_d_l, off1), Indicate(pa_arrow, color=RED,
                                                                    scale_factor=1.1),
                      run_time=1.0)
            beat.wait_until("Minus", offset=-0.2)
            self.play(flag(n2), run_time=0.6)
            beat.wait_until("starting", offset=-0.2)
            off2_now = [m for m in self.mobjects if isinstance(m, MathTex)
                        and m.get_tex_string() == "-2.89"]
            self.play(Indicate(gap0, color=RED, scale_factor=1.1),
                      *[Indicate(m, color=RED) for m in off2_now], run_time=1.0)
            beat.wait_until("Correct", offset=-0.1)
            n1_fix = row_num("+2.75", r1y)
            n2_fix = row_num("+2.75", r2y)
            self.play(FadeIn(r3), TransformFromCopy(eq[4], n3), run_time=1.0)
            self.play(ReplacementTransform(VGroup(n1, off1), n1_fix),
                      ReplacementTransform(VGroup(n2, *off2_now), n2_fix),
                      run_time=beat.until("same", offset=0.1, min_time=1.0))
            self.play(flag(n1_fix), flag(n2_fix), flag(n3), run_time=beat.remaining(0.8))

        # ================================================================ 7. stress test (simulated)
        self.fade_out_all(run_time=0.6)
        ax2 = axes((-3.5, 2.5), (16, 24), x_length=7.6, y_length=4.6, numbers=False,
                   x_ticks=[-3, -2, -1, 0, 1, 2], y_ticks=[16, 18, 20, 22, 24])
        ax2.shift(np.array([-5.6, -2.0, 0]) - ax2.c2p(-3.5, 16))
        ax2.y_axis.add_numbers(x_values=[16, 18, 20, 22, 24], font_size=MATH_SMALL, color=GRAY)
        ax2.x_axis.add_numbers(x_values=[-3, -2, -1, 0, 1, 2], font_size=MATH_SMALL, color=GRAY)
        x2t = text("survey period", size=LABEL, color=GRAY)
        x2t.next_to(ax2.x_axis.numbers, DOWN, buff=0.15).align_to(ax2.c2p(2.5, 16), RIGHT)
        y2t = text("workers per store", size=LABEL, color=GRAY)
        y2t.next_to(ax2.c2p(-3.5, 24), UP, buff=0.3).align_to(ax2.y_axis.numbers, LEFT)
        sim_tag = text("simulated", size=LABEL, color=GRAY, slant=ITALIC)
        sim_tag.next_to(y2t, RIGHT, buff=0.6)
        pol = DashedLine(ax2.c2p(0.5, 16), ax2.c2p(0.5, 24), color=GRAY, stroke_width=2,
                         dash_length=0.1)
        pol_l = text("policy", size=LABEL - 2, color=GRAY).next_to(pol, UP, buff=0.12)
        T = [-3, -2, -1, 0, 1, 2]
        s = ValueTracker(-0.3)
        ctrl = lambda t: 22 - 0.3 * t
        trt = lambda t: 18 + s.get_value() * t
        c_line = VMobject(color=BLUE, stroke_width=5).set_points_as_corners(
            [ax2.c2p(t, ctrl(t)) for t in T])
        c_dots = VGroup(*[Dot(ax2.c2p(t, ctrl(t)), radius=0.08, color=BLUE) for t in T])
        t_line = always_redraw(lambda: VMobject(color=PURPLE, stroke_width=5).set_points_as_corners(
            [ax2.c2p(t, trt(t)) for t in T]))
        t_dots = always_redraw(lambda: VGroup(*[Dot(ax2.c2p(t, trt(t)), radius=0.08,
                                                    color=PURPLE) for t in T]))
        g2_line = DashedLine(ax2.c2p(0, 18), ax2.c2p(2, 18 - 0.6), color=PURPLE, stroke_width=4,
                             dash_length=0.14)
        g2_dot = Dot(ax2.c2p(2, 17.4), radius=0.08, color=PURPLE, fill_opacity=0,
                     stroke_width=3).set_stroke(PURPLE)
        g2_br = always_redraw(lambda: Line(ax2.c2p(2.25, 17.4), ax2.c2p(2.25, 18 + 2 * s.get_value()),
                                           color=YELLOW, stroke_width=6))
        c_lab = text("PA", size=LABEL, color=BLUE).next_to(ax2.c2p(-3, ctrl(-3)), LEFT, buff=0.2)

        RX = 4.55
        rep_head = text("method reports", size=LABEL, color=GRAY).move_to([RX, 1.4, 0])
        rep = ValueTracker(0.0)
        rep_num = DecimalNumber(0, num_decimal_places=1, include_sign=True, font_size=EQ + 8,
                                color=YELLOW).move_to([RX, 0.65, 0])
        rep_num.add_updater(lambda m: m.set_value(2 * s.get_value() + 0.6))
        true_l = VGroup(text("true effect", size=LABEL, color=GRAY),
                        formula("0", size=EQ + 8, color=INK)).arrange(DOWN, buff=0.2)
        true_l.move_to([RX, -1.25, 0])

        with self.narrate("Everything rests on that dashed line, the assumption that the two "
                          "states would have moved in parallel. After the policy, no one can see "
                          "it. Before, you can check.") as beat:
            self.play(Create(ax2), FadeIn(x2t), FadeIn(y2t), FadeIn(sim_tag), run_time=1.0)
            self.play(Create(c_line), FadeIn(c_dots), FadeIn(c_lab), FadeIn(t_line),
                      FadeIn(t_dots), run_time=1.0)
            beat.wait_until("dashed", offset=-0.2)
            self.play(Create(g2_line), FadeIn(g2_dot), run_time=1.0)
            beat.wait_until("After", offset=-0.2)
            self.play(Create(pol), FadeIn(pol_l), run_time=0.7)
            post_zone = Rectangle(width=ax2.c2p(2.5, 0)[0] - ax2.c2p(0.5, 0)[0],
                                  height=ax2.c2p(0, 24)[1] - ax2.c2p(0, 16)[1], stroke_width=0,
                                  fill_color=GRAY, fill_opacity=0.12)
            post_zone.move_to(ax2.c2p(1.5, 20))
            pre_zone = Rectangle(width=ax2.c2p(0.5, 0)[0] - ax2.c2p(-3.5, 0)[0],
                                 height=post_zone.height, stroke_width=0, fill_color=GRAY,
                                 fill_opacity=0.12).move_to(ax2.c2p(-1.5, 20))
            self.play(FadeIn(post_zone), run_time=beat.until("Before", offset=-0.1, min_time=0.5))
            self.play(FadeOut(post_zone), FadeIn(pre_zone), run_time=0.7)
            self.play(FadeOut(pre_zone), run_time=beat.remaining(0.6))
        t_lab = text("NJ", size=LABEL, color=PURPLE)
        t_lab.add_updater(lambda m: m.next_to(ax2.c2p(-3, trt(-3)), LEFT, buff=0.2))
        with self.narrate("In this simulated example the lines were already drifting apart, "
                          "and the method reports an effect where the true one is zero.") as beat:
            self.add(g2_br)
            self.play(FadeIn(t_lab), FadeIn(rep_head), FadeIn(rep_num), run_time=0.6)
            self.play(s.animate.set_value(0.5), run_time=beat.until("method", offset=-0.1),
                      rate_func=SMOOTH)
            self.play(Circumscribe(rep_num, color=YELLOW, buff=0.12), run_time=1.0)
            beat.wait_until("true", offset=-0.2)
            self.play(FadeIn(true_l, shift=0.1 * UP), run_time=0.7)
        with self.narrate("Card and Krueger had a single before-survey, so they couldn't run "
                          "this check.") as beat:
            only = vbracket(ax2, 0, 15.9, 15.9, GRAY)  # placeholder (unused)
            pre_dim = [ax2.x_axis.numbers[i] for i in range(3)]
            self.play(*[m.animate.set_opacity(0.25) for m in pre_dim],
                      t_dots.animate.set_opacity(0.3), c_dots.animate.set_opacity(0.3),
                      run_time=beat.until("single", offset=-0.1, min_time=0.6))
            box0 = box(VGroup(ax2.x_axis.numbers[3]), color=GRAY)
            self.play(Create(box0), run_time=0.8)
            self.play(Indicate(ax2.x_axis.numbers[3], color=INK), run_time=beat.remaining(0.8))

        # ================================================================ 8. payoff
        t_lab.clear_updaters()
        rep_num.clear_updaters()
        self.fade_out_all(run_time=0.6)
        nl = NumberLine(x_range=[-1, 6.5, 1], length=10.5, color=GRAY, stroke_width=2.5,
                        include_ticks=False).move_to([0.2, 1.0, 0])
        for v in (0, 2, 4, 6):
            nl.add(nl.get_tick(v))
        nl.add_numbers(x_values=[0, 2, 4, 6], font_size=MATH_SMALL, color=GRAY)
        nl_t = text("effect on workers per store (NJ vs PA)", size=LABEL, color=GRAY)
        nl_t.next_to(nl.numbers, DOWN, buff=0.2)
        zero = DashedLine(nl.n2p(0) + DOWN * 0.1, nl.n2p(0) + UP * 1.3, color=GRAY, stroke_width=2,
                          dash_length=0.08)
        zero_l = text("no effect", size=LABEL - 2, color=GRAY).next_to(zero, UP, buff=0.1)
        ci = Line(nl.n2p(2.76 - 1.96 * 1.36), nl.n2p(2.76 + 1.96 * 1.36), color=YELLOW,
                  stroke_width=6).shift(UP * 0.55)
        ci_caps = VGroup(*[Line(p + DOWN * 0.12, p + UP * 0.12, color=YELLOW, stroke_width=6)
                           for p in (ci.get_start(), ci.get_end())])
        est = Dot(ci.get_center(), radius=0.12, color=YELLOW).move_to(
            nl.n2p(2.76) + UP * 0.55)
        est_l = formula(r"2.76", size=EQ, color=YELLOW).next_to(est, UP, buff=0.25)
        ci_l = text("95% interval", size=SMALL + 2, color=GRAY).next_to(ci, UP, buff=0.12)
        ci_l.align_to(ci, RIGHT)
        note = text("(2.75 earlier: rounded table means)", size=SMALL, color=GRAY)
        note.next_to(est_l, RIGHT, buff=0.3)
        cite94 = citation("Card & Krueger, 1994 · American Economic Review 84(4)")
        nw = VGroup(text("Neumark & Wascher, 2000", size=SMALL + 2, color=GRAY),
                    text("payroll records: jobs fell", size=LABEL, color=INK)).arrange(
            DOWN, buff=0.12, aligned_edge=LEFT)
        ck = VGroup(text("Card & Krueger, 2000", size=SMALL + 2, color=GRAY),
                    text("government records: no drop", size=LABEL, color=INK)).arrange(
            DOWN, buff=0.12, aligned_edge=LEFT)
        nw.move_to([-3.2, -1.75, 0])
        ck.move_to([3.2, -1.75, 0])
        venue = text("both in American Economic Review 90(5)", size=SMALL, color=GRAY)
        venue.move_to([0, -2.75, 0])
        with self.narrate("They published two point seven six, with a standard error of one "
                          "point three six, in the American Economic Review in nineteen "
                          "ninety-four. No sign that the higher wage cut jobs.") as beat:
            self.play(Create(nl), FadeIn(nl_t), run_time=1.0)
            self.play(FadeIn(est, scale=0.5), Write(est_l), FadeIn(cite94),
                      run_time=beat.until("with", offset=-0.1, min_time=0.6))
            self.play(Create(ci), FadeIn(ci_caps), FadeIn(ci_l),
                      run_time=beat.until("in the", offset=-0.1, min_time=0.8))
            self.play(FadeIn(note), run_time=0.6)
            beat.wait_until("No sign", offset=-0.2)
            self.play(Create(zero), FadeIn(zero_l), run_time=0.8)
            self.play(Indicate(ci_caps[0], color=YELLOW, scale_factor=1.4),
                      run_time=beat.remaining(0.8))
        with self.narrate("Then came the fight. Neumark and Wascher, using restaurant payroll "
                          "records, found jobs fell. Card and Krueger answered with government "
                          "employment records, and found no drop.") as beat:
            self.play(FadeOut(cite94), FadeOut(note), run_time=0.5)
            beat.wait_until("Neumark", offset=-0.2)
            self.play(FadeIn(nw, shift=0.1 * UP), run_time=beat.until("found", offset=-0.1,
                                                                     min_time=0.7))
            self.play(Indicate(nw[1], color=INK, scale_factor=1.05), run_time=0.8)
            beat.wait_until("Card", offset=-0.2)
            self.play(FadeIn(ck, shift=0.1 * UP), FadeIn(venue),
                      run_time=beat.until("found", occurrence=2, offset=-0.1, min_time=0.7))
            self.play(Indicate(ck[1], color=INK, scale_factor=1.05), run_time=beat.remaining(0.8))

        # ================================================================ 9. landing
        self.fade_out_all(run_time=0.6)
        border2 = DashedLine(UP * 2.9, DOWN * 2.6, color=GRAY, stroke_width=2, dash_length=0.12)
        pa_n2 = text("Pennsylvania", size=HEADING, color=BLUE).move_to([-3.3, 3.2, 0])
        nj_n2 = text("New Jersey", size=HEADING, color=PURPLE).move_to([3.3, 3.2, 0])
        pa_c2 = text("$4.25", size=LABEL, color=BLUE).move_to([-3.3, 2.55, 0])
        nj_c2 = text("$4.25 → $5.05", size=LABEL, color=PURPLE).move_to([3.3, 2.55, 0])
        jobs2 = text("jobs", size=BODY, color=INK).move_to([3.3, 1.75, 0])
        q2 = text("?", size=64, color=YELLOW).move_to([4.6, 0.0, 0])
        sc = 0.62  # arrow units per worker
        nj_up = Arrow([3.3, -0.2, 0], [3.3, -0.2 + 0.59 * sc, 0], buff=0, color=PURPLE,
                      stroke_width=7, max_tip_length_to_length_ratio=0.45,
                      max_stroke_width_to_length_ratio=30)
        nj_up_l = formula("+0.59", size=MATH, color=PURPLE).next_to(nj_up, LEFT, buff=0.2)
        pa_dn = Arrow([-3.3, 1.2, 0], [-3.3, 1.2 - 2.16 * sc, 0], buff=0, color=BLUE,
                      stroke_width=7, max_tip_length_to_length_ratio=0.2)
        pa_dn_l = formula("-2.16", size=MATH, color=BLUE).next_to(pa_dn, LEFT, buff=0.2)
        pa_dn_target = Arrow([3.3, -0.2, 0], [3.3, -0.2 - 2.16 * sc, 0], buff=0, color=BLUE,
                             stroke_width=7, max_tip_length_to_length_ratio=0.2)
        end_br = VGroup(
            Line([4.0, -0.2 - 2.16 * sc, 0], [4.0, -0.2 + 0.59 * sc, 0], color=YELLOW, stroke_width=6),
            Line([3.88, -0.2 - 2.16 * sc, 0], [4.12, -0.2 - 2.16 * sc, 0], color=YELLOW, stroke_width=6),
            Line([3.88, -0.2 + 0.59 * sc, 0], [4.12, -0.2 + 0.59 * sc, 0], color=YELLOW, stroke_width=6))
        end_l = formula("2.75", size=MATH + 4, color=YELLOW).next_to(end_br, RIGHT, buff=0.2)
        with self.narrate("So did New Jersey lose jobs? Watching New Jersey alone could never "
                          "tell you.") as beat:
            self.play(Create(border2), FadeIn(pa_n2), FadeIn(nj_n2), FadeIn(pa_c2),
                      FadeIn(nj_c2), FadeIn(jobs2), FadeIn(q2), run_time=1.0)
            beat.wait_until("Watching", offset=-0.1)
            self.play(GrowArrow(nj_up), FadeIn(nj_up_l), run_time=1.0)
            self.play(Indicate(q2, color=YELLOW, scale_factor=1.15), run_time=beat.remaining(0.8))
        with self.narrate("The most important number in a study of New Jersey came from "
                          "Pennsylvania.") as beat:
            self.play(GrowArrow(pa_dn), FadeIn(pa_dn_l), run_time=beat.until("came",
                                                                           offset=-0.3,
                                                                           min_time=0.8))
            self.play(ReplacementTransform(pa_dn, pa_dn_target),
                      pa_dn_l.animate.next_to(pa_dn_target, LEFT, buff=0.2), run_time=1.3)
            self.play(ReplacementTransform(q2, end_br), FadeIn(end_l), run_time=beat.remaining(0.9))
        self.hold(0.9)
        self.end_card()
