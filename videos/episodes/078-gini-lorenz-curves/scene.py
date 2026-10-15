"""Episode 78 - Two Countries, Same Inequality Score, Different Worlds.

videos/toolkit/render.sh --preview videos/episodes/078-gini-lorenz-curves/scene.py Episode /tmp/ep78.mp4
"""
import numpy as np
from manim import *
from sample_space import *

# --------------------------------------------------------------------------- data
# Two invented ("toy") societies of ten people; each value = % of all income.
A = [2, 4, 6, 7, 8, 9, 13, 17, 17, 17]       # struggling bottom
B = [5, 7, 7, 7, 7, 7, 7, 8, 8, 37]          # runaway top
LA = np.concatenate([[0], np.cumsum(A)]) / 100.0
LB = np.concatenate([[0], np.cumsum(B)]) / 100.0
XS = np.arange(11) / 10.0
CROSS = (2 / 3, 0.36 + 0.13 * 2 / 3)        # where the two Lorenz curves cross


def gini(x):
    x = np.sort(np.asarray(x, float))
    n = len(x)
    return 2 * np.sum(np.arange(1, n + 1) * x) / (n * x.sum()) - (n + 1) / n


def atkinson(x, e):
    x = np.asarray(x, float) / np.mean(x)
    if abs(e) < 1e-9:
        return 0.0
    if abs(e - 1) < 1e-9:
        return 1 - np.exp(np.mean(np.log(x)))
    return 1 - np.mean(x ** (1 - e)) ** (1 / (1 - e))


assert abs(gini(A) - 0.30) < 1e-12 and abs(gini(B) - 0.30) < 1e-12

# --------------------------------------------------------------------------- layout
U = 4.6                                   # 1.0 of income share = 4.6 units, everywhere
O = np.array([1.4, -2.2, 0])              # Lorenz plot origin
SLOT = U / 10                             # one person's width
BAR_X0 = -6.1                             # left edge of both bar charts
YA, YB = 1.0, -2.2                        # bar-chart baselines


def P(x, y):
    return O + np.array([x * U, y * U, 0])


def bar_chart(shares, base_y, color):
    bars = VGroup()
    for k, s in enumerate(shares):
        r = Rectangle(width=SLOT, height=s / 100 * U, stroke_color=BG, stroke_width=3,
                      fill_color=color, fill_opacity=0.9)
        r.move_to([BAR_X0 + SLOT * (k + 0.5), base_y, 0], aligned_edge=DOWN)
        bars.add(r)
    base = Line([BAR_X0 - 0.05, base_y, 0], [BAR_X0 + 10 * SLOT + 0.05, base_y, 0],
                color=GRAY, stroke_width=2.5)
    lo = label("poorest", size=SMALL, color=GRAY).next_to(base, DOWN, buff=0.12).align_to(base, LEFT)
    hi = label("richest", size=SMALL, color=GRAY).next_to(base, DOWN, buff=0.12).align_to(base, RIGHT)
    return bars, VGroup(base, lo, hi)


def column_target(bar, k, L):
    """Where person k's bar sits when stacked on the Lorenz plot."""
    return bar.copy().move_to(P((k + 0.5) / 10, L[k]), aligned_edge=DOWN)


def curve(L, color):
    return VMobject(stroke_color=color, stroke_width=5).set_points_as_corners(
        [P(x, y) for x, y in zip(XS, L)])


def interp(L, x):
    return float(np.interp(x, XS, L))


def lens(lower, upper, x0, x1, color):
    """Region between two Lorenz curves for x in [x0, x1]."""
    xs = [x0] + [x for x in XS if x0 < x < x1] + [x1]
    top = [P(x, interp(upper, x)) for x in xs]
    bot = [P(x, interp(lower, x)) for x in reversed(xs)]
    return Polygon(*top, *bot, stroke_width=0, fill_color=color, fill_opacity=0.55)


class Episode(NarratedScene):
    EPISODE = 78
    TITLE = "Two Countries, Same Inequality Score, Different Worlds"
    PRONUNCIATIONS = {"Gini": "/ʤˈini/", "Ginis": "/ʤˈiniz/"}

    def construct(self):
        # ================================================================ COLD OPEN
        def country(name):
            n = text(name, size=HEADING)
            g = formula(r"G", "=", r"0.410", size=EQ)
            return VGroup(n, g).arrange(DOWN, buff=0.4)

        india = country("India, 1950").move_to([-3.4, 1.3, 0])
        wger = country("West Germany, 1950").move_to([3.4, 1.3, 0])
        eq = formula("=", size=72, color=YELLOW).move_to([0, india[1].get_center()[1], 0])
        cite0 = citation("Gini values: Ranadive, 1965, as tabulated in Atkinson, 1970 · J. Economic Theory")

        with self.narrate("In nineteen fifty, India and West Germany had exactly the same "
                          "income inequality score: a Gini coefficient of point four one oh.") as beat:
            self.play(FadeIn(india[0], shift=0.2 * DOWN), FadeIn(wger[0], shift=0.2 * DOWN),
                      run_time=1.0)
            self.play(FadeIn(cite0), run_time=beat.until("Gini", offset=-0.3))
            self.play(Write(india[1]), Write(wger[1]), run_time=1.2)
            beat.wait_until("point", offset=-0.1)
            self.play(GrowFromCenter(eq), flag(india[1][2]), flag(wger[1][2]), run_time=1.0)

        opts = VGroup(*[label(s, size=LABEL) for s in ("India", "West Germany", "a tie")])
        opts.arrange(RIGHT, buff=1.4).move_to([0, -1.1, 0])
        frames = VGroup(*[SurroundingRectangle(o, color=GRAY, buff=0.18, corner_radius=0.1,
                                               stroke_width=2.5) for o in opts])
        timer = Line(frames.get_left(), frames.get_right(), color=YELLOW, stroke_width=5)
        timer.next_to(frames, DOWN, buff=0.35)
        with self.narrate("So which country was more unequal: India, West Germany, or "
                          "neither. Lock in your answer. [pause 1.5]") as beat:
            beat.wait_until("India", offset=-0.1)
            self.play(FadeIn(opts[0]), Create(frames[0]), run_time=0.5)
            beat.wait_until("West", offset=-0.1)
            self.play(FadeIn(opts[1]), Create(frames[1]), run_time=0.5)
            beat.wait_until("neither", offset=-0.1)
            self.play(FadeIn(opts[2]), Create(frames[2]), run_time=0.5)
            beat.wait_until("Lock", offset=-0.1)
            self.play(Create(timer), run_time=0.6)
            self.play(timer.animate.put_start_and_end_on(timer.get_right(), timer.get_right()),
                      run_time=beat.remaining(), rate_func=LINEAR)
        self.remove(timer)

        # ================================================================ STAKES -> BUILD
        cards = VGroup(india, wger, eq)
        with self.narrate("Economists rank whole countries by this one number. To see what it "
                          "notices, and what it misses, we'll build one from scratch.") as beat:
            self.play(FadeOut(opts), FadeOut(frames), run_time=0.8)
            beat.wait_until("one number", offset=-0.2)
            self.play(Indicate(VGroup(india[1][2], wger[1][2]), color=YELLOW, scale_factor=1.08),
                      run_time=0.9)
            beat.wait_until("build", offset=-0.3)
            self.play(FadeOut(cards, shift=0.3 * UP), FadeOut(cite0), run_time=beat.remaining())

        # bar chart A
        barsA, frameA = bar_chart(A, YA, BLUE)
        nameA = label("Society A", color=BLUE).move_to([BAR_X0, 2.35, 0], aligned_edge=LEFT)
        toyA = label("toy data", size=SMALL, color=GRAY).next_to(nameA, RIGHT, buff=0.3)
        toyA.align_to(nameA, DOWN)
        with self.narrate("Here's a made-up society of ten people, lined up from poorest to "
                          "richest. Each bar is one person's share of all the income, so "
                          "together they make a hundred percent.") as beat:
            self.play(FadeIn(nameA), FadeIn(toyA), Create(frameA[0]), run_time=1.0)
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in barsA], lag_ratio=0.15),
                      run_time=beat.until("poorest", offset=-0.1))
            self.play(FadeIn(frameA[1], shift=0.1 * UP), flag(barsA[0]), run_time=0.8)
            beat.wait_until("richest", offset=-0.1)
            self.play(FadeIn(frameA[2], shift=0.1 * UP), flag(barsA[9]), run_time=0.8)
            beat.wait_until("Each bar", offset=-0.1)
            self.play(Indicate(barsA[6], color=YELLOW, scale_factor=1.15), run_time=1.0)
            beat.wait_until("hundred", offset=-0.4)
            self.play(LaggedStart(*[Indicate(b, color=YELLOW, scale_factor=1.06) for b in barsA],
                                  lag_ratio=0.08), run_time=beat.remaining())

        # Lorenz axes
        xax = Line(P(0, 0), P(1, 0), color=GRAY, stroke_width=2.5)
        yax = Line(P(0, 0), P(0, 1), color=GRAY, stroke_width=2.5)
        ticks = VGroup()
        for v, s in ((0, "0"), (0.5, r"50\%"), (1, r"100\%")):
            ticks.add(MathTex(s, font_size=MATH_SMALL, color=GRAY).next_to(P(v, 0), DOWN, buff=0.15))
            if v > 0:
                ticks.add(MathTex(s, font_size=MATH_SMALL, color=GRAY).next_to(P(0, v), LEFT, buff=0.15))
        xt = label("share of people, poorest first", size=SMALL + 2, color=GRAY)
        xt.next_to(ticks[0], DOWN, buff=0.1).align_to(P(1, 0), RIGHT)
        xt.set_y(-2.95)
        yt = label("share of all income", size=SMALL + 2, color=GRAY)
        yt.next_to(P(0, 1), UP, buff=0.25).align_to(P(0, 1) + LEFT * 0.75, LEFT)
        lor_axes = VGroup(xax, yax, ticks, xt, yt)

        colsA = VGroup(*[column_target(b, k, LA) for k, b in enumerate(barsA)])
        dotsA = VGroup(*[Dot(P(x, y), radius=0.06, color=BLUE) for x, y in zip(XS, LA)])
        curveA = curve(LA, BLUE)
        lorenz_name = label("Lorenz curve", color=BLUE).next_to(P(0.78, 0.5), RIGHT, buff=0.1)
        cite1 = citation("Lorenz, 1905 · Publications of the American Statistical Association")

        run_lbl = MathTex(r"2\%", font_size=MATH_SMALL, color=YELLOW)
        with self.narrate("Now stack them. The poorest person alone holds two percent. Add the "
                          "next, and the poorest two hold six. Keep stacking, and the running "
                          "totals trace this curve: the Lorenz curve, from nineteen oh five.") as beat:
            self.play(Create(lor_axes), run_time=beat.until("poorest", offset=-0.2))
            self.play(TransformFromCopy(barsA[0], colsA[0]), FadeIn(dotsA[0]), run_time=0.9)
            run_lbl.next_to(dotsA[1], UL, buff=0.12)
            self.play(FadeIn(dotsA[1]), FadeIn(run_lbl, shift=0.1 * UP),
                      run_time=beat.until("Add", offset=-0.1))
            self.play(TransformFromCopy(barsA[1], colsA[1]), run_time=0.9)
            lbl6 = MathTex(r"6\%", font_size=MATH_SMALL, color=YELLOW).next_to(dotsA[2], UL, buff=0.12)
            self.play(FadeIn(dotsA[2]), ReplacementTransform(run_lbl, lbl6),
                      run_time=beat.until("Keep", offset=-0.1))
            run_lbl = lbl6
            for k in range(2, 10):
                nxt = MathTex(rf"{int(round(LA[k + 1] * 100))}\%", font_size=MATH_SMALL,
                              color=YELLOW).next_to(dotsA[k + 1], UL, buff=0.12)
                self.play(TransformFromCopy(barsA[k], colsA[k]), FadeIn(dotsA[k + 1]),
                          ReplacementTransform(run_lbl, nxt), run_time=0.45)
                run_lbl = nxt
            self.play(Create(curveA), FadeIn(cite1), run_time=beat.until("Lorenz", offset=-0.2))
            self.play(FadeIn(lorenz_name, shift=0.1 * LEFT), FadeOut(run_lbl),
                      run_time=beat.remaining())

        diag = DashedLine(P(0, 0), P(1, 1), color=GRAY, stroke_width=3, dash_length=0.12)
        eq_lbl = label("everyone equal", size=SMALL + 2, color=GRAY).rotate(PI / 4)
        eq_lbl.move_to(P(0.36, 0.36) + 0.3 * np.array([-1, 1, 0]))
        gapA = Polygon(*[P(x, y) for x, y in zip(XS, LA)], stroke_width=0,
                       fill_color=BLUE, fill_opacity=0.35)
        with self.narrate("If everyone earned the same, the stack would climb this straight "
                          "diagonal instead. So inequality is this gap between them: the area "
                          "where the curve sags below equality.") as beat:
            self.play(FadeOut(cite1), colsA.animate.set_fill(opacity=0.25),
                      run_time=beat.until("diagonal", offset=-0.6))
            self.play(Create(diag), FadeIn(eq_lbl), run_time=1.0)
            beat.wait_until("gap", offset=-0.2)
            self.bring_to_back(gapA)
            self.play(FadeIn(gapA), FadeOut(lorenz_name), run_time=1.2)
            beat.wait_until("sags", offset=-0.1)
            self.play(Indicate(curveA, color=YELLOW, scale_factor=1.0), run_time=1.0)

        # Gini = gap / triangle = 2 x gap
        tri = Polygon(P(0, 0), P(1, 0), P(1, 1), stroke_color=GRAY, stroke_width=3,
                      fill_color=GRAY, fill_opacity=0.12)
        g_lhs = formula("G", "=", size=EQ).move_to([-5.1, -0.55, 0])
        gap_icon = gapA.copy().set_fill(opacity=0.6).scale(0.3)
        tri_icon = tri.copy().scale(0.3)
        bar_line = Line(LEFT * 0.75, RIGHT * 0.75, color=INK, stroke_width=3)
        frac = VGroup(gap_icon, bar_line, tri_icon).arrange(DOWN, buff=0.15)
        frac.next_to(g_lhs, RIGHT, buff=0.3)
        half = formula(r"\tfrac{1}{2}", size=MATH, color=GRAY).next_to(tri_icon, RIGHT, buff=0.25)
        row2 = formula("=", "2", r"\times", "0.15", "=", "0.30", size=EQ)
        row2.next_to(g_lhs, DOWN, buff=0.75, aligned_edge=LEFT).shift(DOWN * 0.3)
        row2[3].set_color(BLUE)
        gap_val = MathTex("0.15", font_size=MATH_SMALL, color=BLUE).move_to(P(0.58, 0.46))
        allow_overlap(gap_val)
        with self.narrate("The Gini coefficient is that gap as a fraction of the whole triangle. "
                          "The triangle's area is one half, so the Gini is twice the gap. Here "
                          "the gap is point one five, so the Gini is point three oh.") as beat:
            self.play(Write(g_lhs), run_time=0.8)
            self.play(TransformFromCopy(gapA, gap_icon), Create(bar_line),
                      run_time=beat.until("triangle", offset=-0.2))
            self.bring_to_back(tri)
            self.play(FadeIn(tri), TransformFromCopy(tri, tri_icon), run_time=1.2)
            beat.wait_until("one half", offset=-0.1)
            self.play(FadeIn(half, shift=0.1 * LEFT), run_time=0.7)
            beat.wait_until("twice", offset=-0.2)
            self.play(Write(row2[0]), TransformFromCopy(half, row2[1]), Write(row2[2]),
                      FadeOut(tri), run_time=1.0)
            beat.wait_until("point one", offset=-0.2)
            self.play(FadeIn(gap_val, scale=0.8), TransformFromCopy(gap_val, row2[3]), run_time=1.0)
            beat.wait_until("point three", offset=-0.3)
            self.play(Write(row2[4:]), run_time=0.8)
            self.play(flag(row2[5]), run_time=0.8)

        # condense the formula into a readout next to the society's name
        readA = formula("G", "=", "0.30", size=MATH).next_to(nameA, RIGHT, buff=0.45)
        readA.align_to(nameA, DOWN)

        # ================================================================ SOCIETY B (prediction)
        barsB, frameB = bar_chart(B, YB, PURPLE)
        nameB = label("Society B", color=PURPLE).move_to([BAR_X0, -0.1, 0], aligned_edge=LEFT)
        toyB = label("toy data", size=SMALL, color=GRAY).next_to(nameB, RIGHT, buff=0.3)
        toyB.align_to(nameB, DOWN)
        braceA = Brace(barsA[0:2], UP, buff=0.08, color=YELLOW)
        sixA = MathTex(r"6\%", font_size=MATH_SMALL, color=YELLOW).next_to(braceA, UP, buff=0.08)
        braceB = Brace(barsB[0:2], UP, buff=0.08, color=YELLOW)
        twB = MathTex(r"12\%", font_size=MATH_SMALL, color=YELLOW).next_to(braceB, UP, buff=0.08)
        topA = MathTex(r"17\%", font_size=MATH_SMALL, color=YELLOW).next_to(barsA[9], UP, buff=0.12)
        topB = MathTex(r"37\%", font_size=MATH_SMALL, color=YELLOW).next_to(barsB[9], UP, buff=0.12)
        q = formula("G", "=", "?", size=MATH).next_to(nameB, RIGHT, buff=0.45).align_to(nameB, DOWN)
        q[2].set_color(YELLOW)
        with self.narrate("Now a second society, with very different people. Its poorest two hold "
                          "twelve percent, not six, but its richest person holds thirty seven "
                          "percent, not seventeen. Will its Gini come out higher or lower. "
                          "[pause 1.5]") as beat:
            self.play(FadeOut(VGroup(g_lhs, frac, half, row2[:5])), FadeOut(toyA),
                      ReplacementTransform(row2[5], readA[2]), FadeIn(readA[:2]),
                      run_time=1.0)
            self.play(FadeIn(nameB), FadeIn(toyB), FadeIn(frameB),
                      LaggedStart(*[GrowFromEdge(b, DOWN) for b in barsB], lag_ratio=0.12),
                      run_time=beat.until("poorest", offset=-0.2))
            self.play(GrowFromCenter(braceB), FadeIn(twB, shift=0.1 * UP), run_time=0.7)
            beat.wait_until("not six", offset=-0.1)
            self.play(GrowFromCenter(braceA), FadeIn(sixA, shift=0.1 * UP), run_time=0.7)
            beat.wait_until("richest", offset=-0.1)
            self.play(FadeIn(topB, shift=0.1 * UP), flag(barsB[9]), run_time=0.8)
            beat.wait_until("seventeen", offset=-0.2)
            self.play(FadeIn(topA, shift=0.1 * UP), flag(barsA[9]), run_time=0.8)
            beat.wait_until("Will", offset=-0.1)
            self.play(Write(q), run_time=0.8)
            self.play(Indicate(q[2], color=YELLOW, scale_factor=1.25), run_time=1.0)
            self.play(Indicate(q[2], color=YELLOW, scale_factor=1.25), run_time=1.0)

        colsB = VGroup(*[column_target(b, k, LB) for k, b in enumerate(barsB)])
        colsB.set_fill(opacity=0.5)
        dotsB = VGroup(*[Dot(P(x, y), radius=0.06, color=PURPLE) for x, y in zip(XS, LB)])
        curveB = curve(LB, PURPLE)
        readB = formula("G", "=", "0.30", size=MATH).move_to(q, aligned_edge=LEFT)
        with self.narrate("Neither. Stack it up, and the Gini is point three oh again, to the "
                          "last digit.") as beat:
            self.play(FadeOut(gapA), FadeOut(gap_val), colsA.animate.set_fill(opacity=0.12),
                      run_time=0.7)
            self.play(LaggedStart(*[TransformFromCopy(b, c) for b, c in zip(barsB, colsB)],
                                  lag_ratio=0.12),
                      run_time=beat.until("Gini", offset=-0.3))
            self.play(Create(curveB), FadeIn(dotsB), run_time=1.0)
            beat.wait_until("point", offset=-0.2)
            self.play(ReplacementTransform(q, readB), run_time=0.8)
            self.play(flag(readB[2]), flag(readA[2]), run_time=0.9)

        # measured failure
        dG = formula(r"\Delta G", "=", "0.00", size=MATH).move_to([-3.8, 0.55, 0])
        x2 = formula(r"\times 2", size=MATH, color=YELLOW)
        with self.narrate("So the Gini gap between these societies is zero, while the bottom's "
                          "share differs by a factor of two. One number, two different worlds.") as beat:
            self.play(colsB.animate.set_fill(opacity=0.12), run_time=0.8)
            beat.wait_until("zero", offset=-0.4)
            self.play(Write(dG), run_time=0.9)
            beat.wait_until("factor", offset=-0.2)
            x2.next_to(twB, RIGHT, buff=0.35)
            self.play(Indicate(sixA, color=YELLOW), Indicate(twB, color=YELLOW),
                      FadeIn(x2, shift=0.1 * LEFT), run_time=1.0)
            beat.wait_until("One number", offset=-0.1)
            self.play(Indicate(VGroup(readA, readB), color=YELLOW, scale_factor=1.05), run_time=0.9)
            self.play(Indicate(curveA, color=BLUE, scale_factor=1.0),
                      Indicate(curveB, color=PURPLE, scale_factor=1.0), run_time=beat.remaining())

        # ================================================================ INSIGHT: two lenses
        lensA = lens(LA, LB, 0, CROSS[0], BLUE)        # A sags lower (bottom)
        lensB = lens(LB, LA, CROSS[0], 1, PURPLE)      # B sags lower (top)
        cross_dot = Dot(P(*CROSS), radius=0.08, color=YELLOW)
        headA = VGroup(nameA, readA)
        headB = VGroup(nameB, toyB, readB)
        with self.narrate("Look where the curves cross. Below the crossing, society A sags lower: "
                          "this blue lens is where its poor are poorer. Above it, society B sags "
                          "lower: this purple lens is its runaway top.") as beat:
            self.play(FadeOut(VGroup(barsA, frameA, braceA, sixA, topA, barsB, frameB, braceB,
                                     twB, topB, x2, dG, toyB)),
                      FadeOut(colsA), FadeOut(colsB), FadeOut(dotsA), FadeOut(dotsB),
                      headB.animate.move_to([BAR_X0, 1.7, 0], aligned_edge=LEFT),
                      run_time=beat.until("cross", offset=-0.3))
            self.play(GrowFromCenter(cross_dot), run_time=0.8)
            beat.wait_until("blue lens", offset=-0.2)
            self.bring_to_back(lensA)
            self.play(FadeIn(lensA), run_time=1.0)
            beat.wait_until("purple lens", offset=-0.2)
            self.bring_to_back(lensB)
            self.play(FadeIn(lensB), run_time=1.0)

        # the Gini difference read off the lenses
        dlhs = formula(r"G_A - G_B", "=", "2", r"\big(", size=EQ)
        icA = lensA.copy().scale(0.45)
        icB = lensB.copy().scale(0.45)
        minus = formula("-", size=EQ)
        rpar = formula(r"\big)", size=EQ)
        lens_eq = VGroup(dlhs, icA, minus, icB, rpar).arrange(RIGHT, buff=0.2)
        lens_eq.move_to([-3.6, 0.15, 0])
        valA = MathTex("0.032", font_size=MATH_SMALL, color=BLUE).next_to(icA, DOWN, buff=0.25)
        valB = MathTex("0.032", font_size=MATH_SMALL, color=PURPLE).next_to(icB, DOWN, buff=0.25)
        valB.align_to(valA, UP)
        res = formula("=", "0", size=EQ).next_to(lens_eq, DOWN, buff=1.0).align_to(dlhs[1], LEFT)
        with self.narrate("The Gini only counts total area. So the difference between the two "
                          "Ginis is twice this lens minus this one. Both lenses measure point "
                          "oh three two, so the difference is exactly zero.") as beat:
            self.play(Write(dlhs[0:2]), run_time=beat.until("twice", offset=-0.3))
            self.play(Write(dlhs[2:]), run_time=0.5)
            self.play(TransformFromCopy(lensA, icA), run_time=beat.until("minus", offset=-0.1))
            self.play(Write(minus), TransformFromCopy(lensB, icB), Write(rpar), run_time=1.0)
            beat.wait_until("point", offset=-0.2)
            self.play(FadeIn(valA, shift=0.1 * DOWN), FadeIn(valB, shift=0.1 * DOWN), run_time=0.9)
            beat.wait_until("exactly", offset=-0.2)
            self.play(Write(res), run_time=0.8)
            self.play(flag(res[1]), run_time=0.8)

        with self.narrate("Make the bottom sag more and the top sag less by the same area, "
                          "and the Gini won't move. It can't tell you where the gap lives.") as beat:
            self.play(Indicate(lensA, color=BLUE, scale_factor=1.0), run_time=1.0)
            beat.wait_until("top sag", offset=-0.1)
            self.play(Indicate(lensB, color=PURPLE, scale_factor=1.0), run_time=1.0)
            beat.wait_until("won't", offset=-0.2)
            self.play(flag(readA[2]), flag(readB[2]), run_time=0.9)
            beat.wait_until("where", offset=-0.1)
            self.play(Indicate(icA, color=YELLOW), Indicate(icB, color=YELLOW),
                      run_time=beat.remaining())

        # ================================================================ ITERATE: Atkinson's dial
        ax = axes((0, 2.6), (0, 0.5), x_length=4.4, y_length=2.6, x_ticks=[0, 1, 2],
                  y_ticks=[0, 0.2, 0.4], y_label="Atkinson index")
        ax.move_to([-3.55, -1.2, 0])
        eps_t = MathTex(r"\varepsilon", font_size=MATH, color=YELLOW)
        eps_t.next_to(ax.x_axis.get_right(), RIGHT, buff=0.2)
        eps_sub = label("weight on the poorest", size=SMALL + 2, color=YELLOW)
        eps_sub.next_to(ax.x_axis, DOWN, buff=0.62).align_to(ax.x_axis, RIGHT)
        cite2 = citation("Atkinson, 1970 · Journal of Economic Theory")
        e = ValueTracker(0.0)
        es = np.linspace(0, 2.6, 131)

        def trace(x, color):
            def f():
                v = e.get_value()
                pts = [ax.c2p(t, atkinson(x, t)) for t in es if t <= v + 1e-9]
                if len(pts) < 2:
                    pts = [ax.c2p(0, 0), ax.c2p(1e-3, 0)]
                return VMobject(stroke_color=color, stroke_width=5).set_points_as_corners(pts)
            return always_redraw(f)

        trA, trB = trace(A, BLUE), trace(B, PURPLE)
        knob = always_redraw(lambda: Line(ax.c2p(e.get_value(), 0), ax.c2p(e.get_value(), 0.5),
                                          color=YELLOW, stroke_width=3))
        lensA.add_updater(lambda m: m.set_fill(opacity=0.25 + 0.6 * min(1, e.get_value() / 2.6)))
        lensB.add_updater(lambda m: m.set_fill(opacity=0.85 - 0.6 * min(1, e.get_value() / 2.6)))
        with self.narrate("In nineteen seventy, Anthony Atkinson made the hidden choice explicit. "
                          "His index asks what share of all income you could give up to make "
                          "everyone equal, and be no worse off, with a dial, epsilon, for how much the poorest matter.") as beat:
            self.play(FadeOut(VGroup(lens_eq, valA, valB, res)), FadeIn(cite2),
                      run_time=beat.until("index", offset=-0.3))
            self.play(Create(ax), run_time=1.2)
            beat.wait_until("dial", offset=-0.2)
            self.add(knob)
            self.play(Write(eps_t), FadeIn(eps_sub), run_time=beat.until("poorest", offset=-0.3))
            self.add(trA, trB)
            self.play(e.animate.set_value(0.5), run_time=beat.remaining(), rate_func=SMOOTH)

        tagB = label("B higher", size=SMALL + 2, color=PURPLE)
        tagA = label("A higher", size=SMALL + 2, color=BLUE)
        with self.narrate("With the dial low, society B, with its runaway top, scores as more "
                          "unequal. Turn the dial past about one point one, and the ranking flips: "
                          "A's struggling bottom now counts for more.") as beat:
            beat.wait_until("society B", offset=-0.2)
            tagB.next_to(ax.c2p(0.5, atkinson(B, 0.5)), UP, buff=0.3).shift(LEFT * 0.1)
            self.play(FadeIn(tagB, shift=0.1 * UP), Indicate(trB, color=PURPLE, scale_factor=1.0),
                      run_time=1.0)
            beat.wait_until("Turn", offset=-0.1)
            self.play(FadeOut(tagB), e.animate.set_value(1.106), rate_func=SMOOTH,
                      run_time=beat.until("flips", offset=-0.2))
            xmark = Dot(ax.c2p(1.106, atkinson(A, 1.106)), radius=0.08, color=YELLOW)
            self.play(GrowFromCenter(xmark), run_time=0.5)
            self.play(e.animate.set_value(2.6), rate_func=SMOOTH,
                      run_time=beat.until("counts", offset=-0.2))
            tagA.next_to(ax.c2p(2.0, atkinson(A, 2.0)), UP, buff=0.25)
            self.play(FadeIn(tagA, shift=0.1 * UP), run_time=beat.remaining())

        with self.narrate("Atkinson proved a flip is always possible: whenever two Lorenz curves "
                          "cross, you can find two reasonable welfare judgments that rank them in "
                          "opposite orders. Only curves that never cross get one verdict from all "
                          "of them.") as beat:
            beat.wait_until("cross", offset=-0.2)
            self.play(Indicate(cross_dot, color=YELLOW, scale_factor=1.6), run_time=1.0)
            beat.wait_until("opposite", offset=-0.2)
            self.play(Indicate(xmark, color=YELLOW, scale_factor=1.6), run_time=1.0)
            beat.wait_until("never", offset=-0.2)
            self.play(Indicate(curveA, color=BLUE, scale_factor=1.0),
                      Indicate(curveB, color=PURPLE, scale_factor=1.0), run_time=beat.remaining())
        lensA.clear_updaters()
        lensB.clear_updaters()
        trA.clear_updaters()
        trB.clear_updaters()
        knob.clear_updaters()

        # ================================================================ PAYOFF: real data
        waffle = VGroup(*[Square(0.4, stroke_width=0) for _ in range(66)])
        waffle.arrange_in_grid(rows=6, cols=11, buff=0.1).move_to([-2.4, 0.4, 0])
        for i, sq in enumerate(waffle):
            if i < 50:
                sq.set_fill(YELLOW, opacity=0.85)
            else:
                sq.set_fill(opacity=0).set_stroke(GRAY, width=2)
        w_title = label("12 countries, around 1950 · 66 pairs", size=LABEL)
        w_title.next_to(waffle, UP, buff=0.35)
        leg1 = VGroup(Square(0.3, stroke_width=0, fill_color=YELLOW, fill_opacity=0.85),
                      label("Lorenz curves cross: 50", size=LABEL)).arrange(RIGHT, buff=0.2)
        leg2 = VGroup(Square(0.3, stroke_color=GRAY, stroke_width=2),
                      label("never cross: 16", size=LABEL)).arrange(RIGHT, buff=0.2)
        legend = VGroup(leg1, leg2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        legend.next_to(waffle, RIGHT, buff=0.6)
        cite3 = citation("Atkinson, 1970 · J. Economic Theory, data from Kuznets, 1963")
        with self.narrate("Then he checked real data: twelve countries from around nineteen "
                          "fifty. Of the sixty six pairs, fifty had Lorenz curves that cross.") as beat:
            self.play(*[FadeOut(m) for m in self.mobjects if m is not cite2],
                      run_time=0.8)
            self.play(ReplacementTransform(cite2, cite3), FadeIn(w_title, shift=0.1 * DOWN),
                      run_time=beat.until("sixty", offset=-0.2))
            self.play(LaggedStart(*[FadeIn(s, scale=0.6) for s in waffle], lag_ratio=0.02),
                      run_time=beat.until("fifty had", offset=-0.2))
            self.play(FadeIn(leg1), FadeIn(leg2), *[Indicate(s, color=YELLOW, scale_factor=1.1)
                                                     for s in waffle[:50]],
                      run_time=beat.remaining())

        # the two countries return
        india2 = country("India, 1950")
        wger2 = country("West Germany, 1950")
        for c in (india2, wger2):
            c[0].scale(0.85)
            c[1].scale(0.85)
            c.arrange(DOWN, buff=0.35)
        india2.move_to([-3.4, 1.6, 0])
        wger2.move_to([3.4, 1.6, 0])
        eq2 = formula("=", size=60, color=YELLOW).move_to([0, india2[1].get_center()[1], 0])
        atkI = formula(r"I_{\varepsilon=2}", "=", "0.399", size=EQ).next_to(india2, DOWN, buff=0.6)
        atkW = formula(r"I_{\varepsilon=2}", "=", "0.498", size=EQ).next_to(wger2, DOWN, buff=0.6)
        for m in (atkI, atkW):
            m[0].set_color(YELLOW)
        lt = formula("<", size=60, color=YELLOW).move_to([0, atkI.get_center()[1], 0])
        with self.narrate("India and West Germany were tied on Gini. With the dial at two, India "
                          "scored about point four, and West Germany about point five.") as beat:
            self.play(FadeOut(VGroup(waffle, w_title, legend)), run_time=0.8)
            self.play(FadeIn(india2), FadeIn(wger2), GrowFromCenter(eq2),
                      run_time=beat.until("dial", offset=-0.3))
            self.play(Write(atkI), run_time=beat.until("West Germany", offset=-0.3))
            self.play(Write(atkW), run_time=1.0)
            self.play(GrowFromCenter(lt), run_time=beat.remaining())

        note = label("poorer countries: more equal at the bottom,", size=LABEL, color=GRAY)
        note2 = label("less equal at the top", size=LABEL, color=GRAY)
        notes = VGroup(note, note2).arrange(DOWN, buff=0.15).move_to([0, -1.75, 0])
        with self.narrate("Atkinson saw why: poorer countries were typically more equal at the "
                          "bottom, and less equal at the top. He also warned that the old data "
                          "were rough, so treat the ranking as an illustration.") as beat:
            self.play(FadeIn(note, shift=0.1 * UP), run_time=beat.until("less", offset=-0.2))
            self.play(FadeIn(note2, shift=0.1 * UP), run_time=0.8)
            beat.wait_until("warned", offset=-0.2)
            self.play(Indicate(cite3, color=YELLOW, scale_factor=1.05), run_time=1.0)
            beat.wait_until("illustration", offset=-0.3)
            self.play(notes.animate.set_opacity(0.4), run_time=beat.remaining())

        # ================================================================ LANDING
        with self.narrate("So the tie we started with wasn't a fact about two countries. It was "
                          "a choice, hidden inside one number, about whose income counts most.") as beat:
            self.play(FadeOut(notes), FadeOut(VGroup(atkI, atkW, lt)), FadeOut(cite3),
                      VGroup(india2, wger2, eq2).animate.move_to([0, 0.4, 0]),
                      run_time=beat.until("fact", offset=-0.2))
            self.play(Indicate(eq2, color=YELLOW, scale_factor=1.3), run_time=1.0)
            beat.wait_until("choice", offset=-0.2)
            dial = formula(r"\varepsilon", "=", "?", size=EQ, color=YELLOW)
            dial.next_to(eq2, DOWN, buff=1.2)
            self.play(Write(dial), run_time=1.0)
            beat.wait_until("whose", offset=-0.2)
            self.play(Indicate(dial[2], color=YELLOW, scale_factor=1.3), run_time=beat.remaining())

        self.end_card()
