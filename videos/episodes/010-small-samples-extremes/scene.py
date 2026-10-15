"""Episode 10 - Why the Best Schools Are Small, and So Are the Worst.

    videos/toolkit/render.sh --preview videos/episodes/010-small-samples-extremes/scene.py Episode /tmp/e10.mp4
"""
import sys
from pathlib import Path

import numpy as np
from manim import *
from sample_space import *

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sim import MU, N, SIGMA, simulate  # noqa: E402

# ----------------------------------------------------------------------------- data
SIM = simulate()
NS, MEANS = SIM["n"], SIM["means"]
TOP, BOT, SMALL, OUT = SIM["top"], SIM["bot"], SIM["small"], SIM["out"]
I16, I400 = SIM["i16"], SIM["i400"]
assert (SIM["n_small"], SIM["top_small"], SIM["bot_small"], SIM["n_out"], SIM["out_small"]) == \
    (48, 7, 7, 75, 1), SIM
ORDER = np.argsort(-MEANS)
TOP_CUT = 0.5 * (MEANS[ORDER[49]] + MEANS[ORDER[50]])
BOT_CUT = 0.5 * (MEANS[ORDER[-50]] + MEANS[ORDER[-51]])

_rng = np.random.default_rng(2024)
RETEST16 = [SIM["draws16"]] + [_rng.normal(MU, SIGMA, 16) for _ in range(3)]
RETEST16_1000 = _rng.normal(MU, SIGMA, (1000, 16)).mean(axis=1)          # sd ~ 25.2
RETEST400 = [MEANS[I400]] + list(_rng.normal(MU, SIGMA, (3, 400)).mean(axis=1))
_jit = np.random.default_rng(5).uniform(-0.45, 0.45, N)
XS = np.log10(NS + _jit)                                                   # x jitter only

# real data (Wainer 2007): 1,662 PA schools; smallest 3 % in top 50 = 6, in bottom 50 = 9
REAL_TOP, REAL_BOT, REAL_CHANCE = 6, 9, 1.5

CITE_WAINER = "Wainer, 2007 · American Scientist 95(3)"


# ----------------------------------------------------------------------------- pieces
def make_grid(color):
    cells = VGroup(*[Square(0.38, stroke_color=color, stroke_width=2.2, fill_color=color,
                            fill_opacity=0.12) for _ in range(50)])
    cells.arrange_in_grid(rows=5, cols=10, buff=0.09)
    return cells


def make_strip():
    w = 12.0
    body = Rectangle(width=w, height=0.26, stroke_width=0, fill_color=DIM, fill_opacity=1)
    seg = w * 50 / 1662
    g = Rectangle(width=seg, height=0.26, stroke_width=0, fill_color=GREEN, fill_opacity=1)
    r = Rectangle(width=seg, height=0.26, stroke_width=0, fill_color=RED, fill_opacity=1)
    g.align_to(body, LEFT)
    r.align_to(body, RIGHT)
    strip = VGroup(body, g, r).move_to(UP * 2.55)
    l1 = text("rank 1", size=SMALL, color=GRAY).next_to(body, DOWN, buff=0.15).align_to(body, LEFT)
    l2 = text("rank 1,662", size=SMALL, color=GRAY).next_to(body, DOWN, buff=0.15).align_to(body, RIGHT)
    return strip, g, r, VGroup(l1, l2)


def coldopen_layout():
    head = text("1,662 Pennsylvania schools, by 5th-grade average",
                size=LABEL, color=INK).move_to(UP * 3.3)
    strip, gseg, rseg, ranks = make_strip()
    top = make_grid(GREEN).move_to(LEFT * 3.4 + UP * 0.35)
    bot = make_grid(RED).move_to(RIGHT * 3.4 + UP * 0.35)
    top_t = text("top 50", size=LABEL, color=GREEN).next_to(top, UP, buff=0.22)
    bot_t = text("bottom 50", size=LABEL, color=RED).next_to(bot, UP, buff=0.22)
    return head, strip, gseg, rseg, ranks, top, bot, top_t, bot_t


def count_row(num_tex, color=YELLOW):
    n = MathTex(num_tex, font_size=72, color=color)
    w = text("from the smallest 3%", size=LABEL, color=INK)
    return VGroup(n, w).arrange(RIGHT, buff=0.25)


def backing(m, buff=0.08):
    """Label sitting over dimmed dots: a BG plate so it stays legible."""
    plate = BackgroundRectangle(m, color=BG, fill_opacity=0.85, buff=buff)
    g = VGroup(plate, m)
    return allow_overlap(g)


class Episode(NarratedScene):
    EPISODE = 10
    TITLE = "Why the Best Schools Are Small, and So Are the Worst"
    PRONUNCIATIONS = {"Moivre's": "/mwˈɑvz/", "Zwerling": "zwer ling"}

    # ------------------------------------------------------------------ scatter helpers
    def build_axes(self):
        ax = axes((1.0, 2.65), (400, 600), x_length=8.0, y_length=4.7, numbers=False,
                  x_ticks=[np.log10(v) for v in (10, 20, 50, 100, 200, 400)],
                  y_ticks=[400, 450, 500, 550, 600])
        ax.move_to(LEFT * 1.75 + DOWN * 0.1)
        xl = VGroup(*[MathTex(str(v), font_size=MATH_SMALL, color=GRAY)
                      .next_to(ax.c2p(np.log10(v), 400), DOWN, buff=0.18)
                      for v in (10, 20, 50, 100, 200, 400)])
        yl = VGroup(*[MathTex(str(v), font_size=MATH_SMALL, color=GRAY)
                      .next_to(ax.c2p(1.0, v), LEFT, buff=0.15)
                      for v in (400, 450, 500, 550, 600)])
        xt = text("students tested per school", size=LABEL, color=GRAY)
        xt.next_to(xl, DOWN, buff=0.14).align_to(ax.x_axis, RIGHT)
        yt = text("school average (points)", size=LABEL, color=GRAY)
        yt.next_to(ax.c2p(1.0, 600), UP, buff=0.22).align_to(yl, LEFT)
        mid = DashedLine(ax.c2p(1.0, 500), ax.c2p(2.65, 500), color=DIM, stroke_width=2,
                         dash_length=0.08)
        return ax, xl, yl, xt, yt, mid

    def construct(self):
        # ================================================================= COLD OPEN
        head, strip, gseg, rseg, ranks, top, bot, top_t, bot_t = coldopen_layout()
        self.add(head, strip)
        with self.narrate("These are sixteen hundred and sixty two Pennsylvania schools, ranked by "
                          "their fifth graders' average test score. Here are the top fifty.") as beat:
            self.play(FadeIn(ranks), run_time=beat.until("ranked"))
            self.play(Indicate(strip[0], color=GRAY, scale_factor=1.0), run_time=1.0)
            beat.wait_until("top fifty", offset=-0.4)
            self.play(TransformFromCopy(gseg, top), FadeIn(top_t, shift=0.1 * DOWN), run_time=1.2)

        cite = citation(CITE_WAINER)
        row_top = count_row(str(REAL_TOP)).next_to(top, DOWN, buff=0.45)
        chance = MathTex(r"\text{chance alone: } 1.5", font_size=MATH_SMALL, color=GRAY)
        chance.next_to(row_top, DOWN, buff=0.22)
        with self.narrate("Six of them are among the smallest three percent of schools. "
                          "If size didn't matter, you'd expect one or two.") as beat:
            beat.wait_until("Six", offset=-0.2)
            self.play(LaggedStart(*[top[i].animate.set_fill(YELLOW, 0.9).set_stroke(YELLOW)
                                    for i in range(REAL_TOP)], lag_ratio=0.15),
                      FadeIn(row_top, shift=0.1 * UP), FadeIn(cite), run_time=1.6)
            beat.wait_until("expect", offset=-0.2)
            self.play(Write(chance), run_time=1.0)

        qmark = MathTex("?", font_size=96, color=YELLOW).next_to(bot, DOWN, buff=0.35)
        qmark.match_y(row_top)
        with self.narrate("Now the bottom fifty. How many of the smallest schools would you "
                          "expect down here? [pause 1.5]") as beat:
            self.play(TransformFromCopy(rseg, bot), FadeIn(bot_t, shift=0.1 * DOWN),
                      run_time=beat.until("How"))
            self.play(FadeIn(qmark, scale=0.8), run_time=0.8)
            self.play(Circumscribe(bot, color=YELLOW, buff=0.12, time_width=0.6), run_time=2.0)

        money = text("small-schools movement: over $1 billion", size=LABEL, color=INK).move_to(head)
        with self.narrate("Top lists like this one fed the small schools movement, which drew over "
                          "a billion dollars, much of it from the Gates Foundation. Before you split "
                          "up a big school, you'd want to know whether small schools teach better, "
                          "or only rank better.") as beat:
            self.play(Indicate(top, color=YELLOW, scale_factor=1.03), run_time=1.2)
            beat.wait_until("billion", offset=-0.6)
            self.play(ReplacementTransform(head, money), run_time=1.0)
            beat.wait_until("teach", offset=-0.2)
            self.play(Indicate(row_top, color=YELLOW), run_time=1.0)
            beat.wait_until("rank better", offset=-0.2)
            self.play(Indicate(top_t, color=GREEN, scale_factor=1.15), run_time=0.9)

        # ================================================================= NAIVE BUILD
        self.fade_out_all(run_time=0.6)
        ax, xl, yl, xt, yt, mid = self.build_axes()
        tag = text("simulated · every school identical", size=LABEL, color=GRAY)
        tag.move_to(UP * 3.3 + RIGHT * 1.6)
        with self.narrate("So build a state where the answer is known. Here are sixteen hundred and "
                          "sixty two simulated schools, and every one is identical.") as beat:
            self.play(Create(ax), FadeIn(xl), FadeIn(yl), FadeIn(xt), FadeIn(yt), Create(mid),
                      run_time=beat.until("sixteen"))
            dots_all = VGroup(*[Dot(ax.c2p(XS[i], MEANS[i]), radius=0.05, color=BLUE,
                                    fill_opacity=0.8) for i in range(N)])
            order_x = np.argsort(XS)
            chunks = [VGroup(*[dots_all[i] for i in c]) for c in np.array_split(order_x, 24)]
            self.play(LaggedStart(*[FadeIn(c) for c in chunks], lag_ratio=0.12),
                      run_time=beat.until("every one", offset=-0.1))
            self.play(FadeIn(tag, shift=0.1 * DOWN), run_time=0.8)

        # student bell inset (right panel)
        bx0, bx1, base = 3.0, 6.2, 1.75

        def bx(v):
            return bx0 + (np.clip(v, 200, 800) - 200) / 600 * (bx1 - bx0)

        def bh(v):
            return 1.1 * np.exp(-0.5 * ((v - MU) / SIGMA) ** 2)
        bell_axis = Line([bx0, base, 0], [bx1, base, 0], color=GRAY, stroke_width=2)
        bell = VMobject(color=GRAY, stroke_width=3).set_points_smoothly(
            [[bx(v), base + bh(v), 0] for v in np.linspace(200, 800, 61)])
        b_ticks = VGroup(*[MathTex(str(v), font_size=MATH_SMALL, color=GRAY)
                           .next_to([bx(v), base, 0], DOWN, buff=0.15) for v in (200, 800)])
        c_tick = Line([bx(500), base - 0.07, 0], [bx(500), base + 0.07, 0], color=GRAY, stroke_width=2)
        sig_line = Line([bx(500), base + bh(600), 0], [bx(600), base + bh(600), 0], color=GRAY,
                        stroke_width=3)
        sig_lab = MathTex(r"\sigma", "=", "100", font_size=MATH, color=GRAY)
        sig_lab.next_to(sig_line, RIGHT, buff=0.15).shift(UP * 0.2)
        bell_t = text("one student's score", size=LABEL, color=GRAY).move_to([4.6, 3.3, 0])
        bell_grp = VGroup(bell_axis, bell, b_ticks, c_tick, sig_line, sig_lab, bell_t)
        with self.narrate("Each student's score comes from the same bell curve, centered on five "
                          "hundred, with a standard deviation of one hundred. The only thing that "
                          "changes is how many students a school tests, from ten up to four "
                          "hundred.") as beat:
            self.play(FadeIn(bell_t), Create(bell_axis), FadeIn(b_ticks),
                      run_time=beat.until("bell"))
            self.play(Create(bell), run_time=beat.until("centered"))
            self.play(Create(c_tick), Indicate(mid, color=GRAY), run_time=1.0)
            beat.wait_until("standard", offset=-0.2)
            self.play(Create(sig_line), Write(sig_lab), run_time=1.2)
            beat.wait_until("ten", offset=-0.3)
            self.play(Indicate(xl[0], color=INK, scale_factor=1.3), run_time=0.9)
            beat.wait_until("four", offset=-0.2)
            self.play(Indicate(xl[-1], color=INK, scale_factor=1.3), Indicate(xt, color=INK),
                      run_time=1.0)

        # ---- rank them
        top_line = DashedLine(ax.c2p(1.0, TOP_CUT), ax.c2p(2.65, TOP_CUT), color=GREEN,
                              stroke_width=2.5, dash_length=0.1)
        bot_line = DashedLine(ax.c2p(1.0, BOT_CUT), ax.c2p(2.65, BOT_CUT), color=RED,
                              stroke_width=2.5, dash_length=0.1)
        top_lab = backing(text("top 50", size=LABEL, color=GREEN)
                          .next_to(ax.c2p(2.65, TOP_CUT), UP, buff=0.12).align_to(top_line, RIGHT))
        bot_lab = backing(text("bottom 50", size=LABEL, color=RED)
                          .next_to(ax.c2p(2.65, BOT_CUT), DOWN, buff=0.12).align_to(bot_line, RIGHT))
        sweep_y = ValueTracker(600)
        sweep = always_redraw(lambda: DashedLine(ax.c2p(1.0, sweep_y.get_value()),
                                                 ax.c2p(2.65, sweep_y.get_value()), color=GREEN,
                                                 stroke_width=2.5, dash_length=0.1))
        with self.narrate("Rank them the obvious way, by average score, and keep the top fifty.") as beat:
            self.add(sweep)
            self.play(sweep_y.animate.set_value(TOP_CUT), run_time=beat.until("top fifty"),
                      rate_func=SMOOTH)
            self.remove(sweep)
            self.add(top_line)
            self.play(*[dots_all[i].animate.set_color(GREEN).scale(1.25) for i in TOP],
                      FadeIn(top_lab), run_time=1.0)

        band = Rectangle(width=ax.c2p(np.log10(11.5), 0)[0] - ax.c2p(np.log10(9.5), 0)[0],
                         height=ax.c2p(1, 600)[1] - ax.c2p(1, 400)[1], stroke_width=0,
                         fill_color=YELLOW, fill_opacity=0.16)
        band.move_to([0.5 * (ax.c2p(np.log10(9.5), 0)[0] + ax.c2p(np.log10(11.5), 0)[0]),
                      ax.c2p(1, 500)[1], 0])
        band_lab = backing(text("smallest 3%", size=LABEL, color=YELLOW)
                           .next_to(band, RIGHT, buff=0.15).align_to(band, DOWN).shift(UP * 0.12))
        # counters (right panel)
        hdr = text("from the smallest 3%", size=LABEL, color=YELLOW).move_to([4.6, 0.75, 0])
        t_top, t_bot = ValueTracker(0), ValueTracker(0)
        c_top = live_number(t_top, 0, size=MATH, color=INK)
        c_bot = live_number(t_bot, 0, size=MATH, color=INK)
        r1 = VGroup(text("top 50", size=LABEL, color=GREEN), c_top)
        r2 = VGroup(text("bottom 50", size=LABEL, color=RED), c_bot)
        r3 = VGroup(text("chance", size=LABEL, color=GRAY),
                    MathTex("1.4", font_size=MATH, color=GRAY))
        rows = VGroup(r1, r2, r3)
        for i, r in enumerate(rows):
            r[0].move_to([3.2, 0.1 - 0.62 * i, 0], aligned_edge=LEFT)
            r[1].move_to([5.6, 0.1 - 0.62 * i, 0])
        with self.narrate("Seven of them come from the smallest three percent, schools that tested "
                          "ten or eleven students. Chance predicts one or two. In a world where size "
                          "does nothing, the ranking says small is better.") as beat:
            self.play(FadeIn(band), FadeIn(band_lab), FadeIn(hdr), FadeIn(r1[0]), FadeIn(c_top),
                      run_time=0.8)
            self.play(t_top.animate.set_value(7),
                      *[Indicate(dots_all[i], color=YELLOW, scale_factor=2.0)
                        for i in TOP if SMALL[i]], run_time=beat.until("Chance", offset=-0.2))
            self.play(FadeIn(r3), run_time=0.8)
            beat.wait_until("small is", offset=-0.3)
            self.play(Circumscribe(VGroup(r1, hdr), color=YELLOW, buff=0.12), run_time=1.4)

        with self.narrate("And the bottom fifty holds another seven. The same tiny schools fill "
                          "both ends.") as beat:
            sweep_b = BOT_CUT
            self.play(Create(bot_line), FadeIn(bot_lab), FadeIn(r2[0]), FadeIn(c_bot),
                      *[dots_all[i].animate.set_color(RED).scale(1.25) for i in BOT],
                      run_time=beat.until("seven"))
            self.play(t_bot.animate.set_value(7),
                      *[Indicate(dots_all[i], color=YELLOW, scale_factor=2.0)
                        for i in BOT if SMALL[i]], run_time=1.2)
            beat.wait_until("both", offset=-0.2)
            self.play(Indicate(band, color=YELLOW, scale_factor=1.0), run_time=1.0)

        # ================================================================= INSIGHT
        def dotplot(draws):
            bins = np.clip(np.round((draws - 200) / 25).astype(int), 0, 24)
            counts = {}
            pts = []
            for b in bins:
                k = counts.get(b, 0)
                counts[b] = k + 1
                pts.append([bx(200 + 25 * b), base + 0.08 + 0.115 * k, 0])
            return VGroup(*[Dot(p, radius=0.05, color=INK) for p in pts])

        def marker(v):
            return Triangle(color=INK, fill_opacity=1, stroke_width=0).scale(0.09) \
                .move_to([bx(v), base - 0.14, 0])

        p16 = dots_all[I16]
        hl16 = Dot(ax.c2p(XS[I16], MEANS[I16]), radius=0.09, color=INK)
        n16 = backing(MathTex("n = 16", font_size=MATH, color=INK)
                      .next_to(ax.c2p(XS[I16], 432), DOWN, buff=0.05))
        studs = dotplot(RETEST16[0])
        mk = marker(RETEST16[0].mean())
        context = VGroup(dots_all, band, top_line, bot_line)
        with self.narrate("Here is why. Take one school with sixteen students. Their average "
                          "lands here.") as beat:
            self.play(FadeOut(VGroup(hdr, rows)), FadeOut(top_lab), FadeOut(bot_lab),
                      FadeOut(band_lab), context.animate.set_opacity(0.18), run_time=1.0)
            beat.wait_until("sixteen", offset=-0.3)
            self.play(FadeIn(hl16, scale=2), FadeIn(n16), LaggedStart(
                *[FadeIn(d, shift=0.3 * DOWN) for d in studs], lag_ratio=0.06),
                run_time=beat.until("average", offset=-0.1))
            self.play(FadeIn(mk, shift=0.1 * UP), run_time=0.6)
            beat.wait_until("here", offset=-0.3)
            self.play(TransformFromCopy(mk, hl16), run_time=0.9)

        trail = VGroup()

        def tick_at(v, x, w=0.22):
            return Line(ax.c2p(x, v) + LEFT * w / 2, ax.c2p(x, v) + RIGHT * w / 2,
                        color=PURPLE, stroke_width=3)

        def retest(k, rt):
            new = dotplot(RETEST16[k])
            m = RETEST16[k].mean()
            old_t = tick_at(hl16.get_center()[1] and ax.p2c(hl16.get_center())[1], XS[I16])
            trail.add(old_t)
            self.add(old_t)
            self.play(Transform(studs, new), mk.animate.move_to([bx(m), base - 0.14, 0]),
                      hl16.animate.move_to(ax.c2p(XS[I16], m)), run_time=rt)

        with self.narrate("Test sixteen fresh students, and it lands somewhere else. And "
                          "again.") as beat:
            beat.wait_until("fresh", offset=-0.2)
            retest(1, beat.until("lands", offset=0.3))
            beat.wait_until("again", offset=-0.3)
            retest(2, 0.9)
            retest(3, 0.9)

        # histogram of 1000 retests, beside the school
        x16 = ax.c2p(XS[I16], 500)[0]
        edges = np.arange(400, 601, 10)
        cnt, _ = np.histogram(RETEST16_1000, bins=edges)
        unit_h = ax.c2p(1, 410)[1] - ax.c2p(1, 400)[1]
        bars = VGroup(*[Rectangle(width=max(1e-3, 1.25 * c / cnt.max()), height=unit_h * 0.86,
                                  stroke_width=0, fill_color=PURPLE, fill_opacity=0.75)
                        .move_to([x16 + 0.18, ax.c2p(1, e + 5)[1], 0], aligned_edge=LEFT)
                        for c, e in zip(cnt, edges[:-1]) if c > 0])
        bx_r = x16 + 0.18 + 1.25 + 0.2
        br16 = VGroup(Line(ax.c2p(1, 475) * 0 + [bx_r, ax.c2p(1, 475)[1], 0],
                           [bx_r, ax.c2p(1, 525)[1], 0], color=PURPLE, stroke_width=4),
                      Line([bx_r - 0.08, ax.c2p(1, 475)[1], 0], [bx_r + 0.08, ax.c2p(1, 475)[1], 0],
                           color=PURPLE, stroke_width=4),
                      Line([bx_r - 0.08, ax.c2p(1, 525)[1], 0], [bx_r + 0.08, ax.c2p(1, 525)[1], 0],
                           color=PURPLE, stroke_width=4))
        lab16 = backing(MathTex(r"\pm 25", font_size=MATH, color=PURPLE).next_to(br16, RIGHT, buff=0.15))
        with self.narrate("Retest it a thousand times, and the averages wobble with a standard "
                          "deviation of about twenty five points.") as beat:
            self.play(FadeOut(trail), LaggedStart(*[GrowFromEdge(b, LEFT) for b in bars],
                                                  lag_ratio=0.05),
                      run_time=beat.until("wobble"))
            beat.wait_until("standard", offset=-0.1)
            self.play(Create(br16), run_time=0.8)
            beat.wait_until("twenty", offset=-0.3)
            self.play(Write(lab16), run_time=0.8)

        hl400 = Dot(ax.c2p(XS[I400], MEANS[I400]), radius=0.09, color=INK)
        n400 = backing(MathTex("n = 400", font_size=MATH, color=INK)
                       .next_to(ax.c2p(XS[I400], 432), DOWN, buff=0.05).shift(LEFT * 0.35))
        x4 = ax.c2p(XS[I400], 500)[0] + 0.22
        br400 = VGroup(Line([x4, ax.c2p(1, 495)[1], 0], [x4, ax.c2p(1, 505)[1], 0], color=PURPLE,
                            stroke_width=4),
                       Line([x4 - 0.08, ax.c2p(1, 495)[1], 0], [x4 + 0.08, ax.c2p(1, 495)[1], 0],
                            color=PURPLE, stroke_width=4),
                       Line([x4 - 0.08, ax.c2p(1, 505)[1], 0], [x4 + 0.08, ax.c2p(1, 505)[1], 0],
                            color=PURPLE, stroke_width=4))
        lab400 = backing(MathTex(r"\pm 5", font_size=MATH, color=PURPLE)
                         .next_to(br400, UP, buff=0.3))
        with self.narrate("A school with four hundred students barely moves. Its wobble is about "
                          "five points.") as beat:
            self.play(FadeIn(hl400, scale=2), FadeIn(n400), run_time=beat.until("barely"))
            for k in (1, 2, 3):
                self.play(hl400.animate.move_to(ax.c2p(XS[I400], RETEST400[k])), run_time=0.55)
            beat.wait_until("five", offset=-0.4)
            self.play(Create(br400), Write(lab400), run_time=0.9)

        # ---- the formula, built from its referents
        f1 = MathTex(r"\text{wobble}", "=", r"\frac{\sigma}{\sqrt{n}}", font_size=EQ,
                     substrings_to_isolate=[r"\sigma", "n"])
        f1.move_to([4.55, -0.15, 0])
        f1.get_part_by_tex(r"\sigma").set_color(GRAY)
        f1.get_part_by_tex(r"\text{wobble}").set_color(PURPLE)
        sig_part, n_part = f1.get_part_by_tex(r"\sigma"), f1.get_parts_by_tex("n")[-1]
        rest1 = VGroup(*[m for m in f1 if m is not sig_part and m is not n_part])
        ratio = VGroup(MathTex(r"\times 25", font_size=MATH, color=INK).move_to([3.7, 0.95, 0]),
                       MathTex(r"\div 5", font_size=MATH, color=PURPLE).move_to([5.5, 0.95, 0]))
        rat_lab = VGroup(text("students", size=SMALL + 4, color=GRAY).next_to(ratio[0], DOWN, buff=0.1),
                         text("wobble", size=SMALL + 4, color=GRAY).next_to(ratio[1], DOWN, buff=0.1))
        with self.narrate("Twenty five times the students, yet only five times less wobble. The "
                          "wobble is the student spread, sigma, divided by the square root of the "
                          "number of students, n.") as beat:
            self.play(TransformFromCopy(VGroup(n16, n400), ratio[0]), FadeIn(rat_lab[0]),
                      run_time=beat.until("yet"))
            self.play(TransformFromCopy(VGroup(lab16, lab400), ratio[1]), FadeIn(rat_lab[1]),
                      run_time=beat.until("wobble is", offset=-0.2))
            self.play(FadeOut(ratio), FadeOut(rat_lab), Write(rest1), run_time=0.9)
            beat.wait_until("sigma", offset=-0.25)
            self.play(TransformFromCopy(sig_lab[0], sig_part), run_time=1.0)
            beat.wait_until("n", occurrence=1, offset=-0.3) if False else None
            self.play(TransformFromCopy(VGroup(n16[1][0][0]), n_part),
                      run_time=beat.until("n.", offset=0.2) if False else max(0.6, beat.remaining() - 0.2))

        f2 = MathTex(r"\frac{100}{\sqrt{16}}", "=", "25", font_size=EQ,
                     substrings_to_isolate=["100", "16"]).move_to([4.55, -1.75, 0])
        f2.get_part_by_tex("100").set_color(GRAY)
        f2[-1].set_color(PURPLE)
        f3 = MathTex(r"\frac{100}{\sqrt{400}}", "=", "5", font_size=EQ,
                     substrings_to_isolate=["100", "400"]).move_to(f2)
        f3.get_part_by_tex("100").set_color(GRAY)
        f3[-1].set_color(PURPLE)
        cite2 = citation("de Moivre's equation · Wainer, 2007 · American Scientist")
        with self.narrate("A hundred over root sixteen is twenty five. A hundred over root four "
                          "hundred is five. Howard Wainer calls this de Moivre's equation, and "
                          "nominates it as the most dangerous equation.") as beat:
            f2_frame = VGroup(*[m for m in f2 if m is not f2.get_part_by_tex("100")
                                and m is not f2.get_part_by_tex("16") and m is not f2[-1]])
            self.play(TransformFromCopy(sig_lab[2], f2.get_part_by_tex("100")),
                      TransformFromCopy(n16[1][0][2:], f2.get_part_by_tex("16")),
                      FadeIn(f2_frame), run_time=beat.until("is"))
            self.play(TransformFromCopy(lab16[1][0][1:], f2[-1]), Indicate(lab16, color=PURPLE),
                      run_time=beat.until("A hundred", occurrence=2, offset=-0.1))
            self.play(TransformMatchingTex(f2, f3), run_time=beat.until("is five", offset=0.3))
            self.play(Indicate(lab400, color=PURPLE), run_time=0.8)
            beat.wait_until("Wainer", offset=-0.3)
            self.play(FadeIn(cite2), Create(box(f1, color=PURPLE)), run_time=1.0)
        f1_box = self.mobjects[-1]

        # ================================================================= FIX: the funnel
        def funnel(sign):
            return ax.plot(lambda x: MU + sign * 2 * SIGMA / np.sqrt(10 ** x),
                           x_range=[1.0, np.log10(400), 0.01], color=PURPLE, stroke_width=4)
        up, lo = funnel(1), funnel(-1)
        f_lab = MathTex(r"500 \pm 2", r"\frac{\sigma}{\sqrt{n}}", font_size=MATH, color=PURPLE)
        f_lab.move_to(ax.c2p(2.25, 578))
        with self.narrate("Now draw two wobbles above and below five hundred, at every size. The "
                          "lines trace a funnel.") as beat:
            self.play(br16.animate.stretch(2, 1), lab16.animate.shift(UP * 0.0),
                      run_time=beat.until("above", offset=-0.1))
            self.play(Create(up), Create(lo), FadeOut(bars), FadeOut(br16), FadeOut(lab16),
                      FadeOut(br400), FadeOut(lab400), FadeOut(n16), FadeOut(n400),
                      FadeOut(hl16), FadeOut(hl400), FadeOut(VGroup(studs, mk)),
                      run_time=beat.until("funnel", offset=-0.2), rate_func=SMOOTH)
            self.play(context.animate.set_opacity(0.85), band.animate.set_opacity(0.16),
                      TransformFromCopy(f1[2:], f_lab[1]), FadeIn(f_lab[0]),
                      FadeOut(f1), FadeOut(f1_box), FadeOut(f2), FadeOut(f3) if f3 in self.mobjects else Wait(0),
                      run_time=1.2)

        o_cnt = ValueTracker(0)
        c_out = live_number(o_cnt, 0, size=MATH, color=PURPLE)
        q1 = VGroup(text("outside funnel", size=LABEL, color=PURPLE), c_out)
        q2 = VGroup(text("luck predicts", size=LABEL, color=GRAY),
                    MathTex("76", font_size=MATH, color=GRAY))
        q3 = VGroup(text("smallest 3%", size=LABEL, color=YELLOW),
                    MathTex("1", font_size=MATH, color=YELLOW))
        qrows = VGroup(q1, q2, q3)
        for i, r in enumerate(qrows):
            r[0].move_to([3.0, 0.35 - 0.62 * i, 0], aligned_edge=LEFT)
            r[1].move_to([5.85, 0.35 - 0.62 * i, 0])
        inside = VGroup(*[dots_all[i] for i in range(N) if not OUT[i]])
        outside = VGroup(*[dots_all[i] for i in range(N) if OUT[i]])
        with self.narrate("That's version two: judge each school against its own funnel, not "
                          "against the other schools. Luck alone predicts about seventy six outside. "
                          "Seventy five land there, and only one of them is small.") as beat:
            self.play(inside.animate.set_opacity(0.2), outside.animate.scale(1.3),
                      run_time=beat.until("Luck", offset=-0.2))
            self.play(FadeIn(q2), run_time=0.8)
            beat.wait_until("Seventy five", offset=-0.2)
            self.play(FadeIn(q1[0]), FadeIn(c_out), o_cnt.animate.set_value(75), run_time=1.4)
            beat.wait_until("one of", offset=-0.2)
            self.play(FadeIn(q3), Indicate(band, color=YELLOW, scale_factor=1.0), run_time=1.0)

        with self.narrate("Those seventy five are still pure luck. The funnel only tells you how "
                          "far a school must stray before it earns a second look.") as beat:
            self.play(Indicate(outside, color=PURPLE, scale_factor=1.4),
                      run_time=beat.until("funnel", offset=-0.2))
            self.play(Indicate(up, color=YELLOW, scale_factor=1.0),
                      Indicate(lo, color=YELLOW, scale_factor=1.0), run_time=1.4)
            self.play(Indicate(f_lab, color=PURPLE), run_time=1.0)

        # ================================================================= PAYOFF (real data)
        self.fade_out_all(run_time=0.6)
        head2, strip, gseg, rseg, ranks, top, bot, top_t, bot_t = coldopen_layout()
        for i in range(REAL_TOP):
            top[i].set_fill(YELLOW, 0.9).set_stroke(YELLOW)
        row_top = count_row(str(REAL_TOP)).next_to(top, DOWN, buff=0.45)
        row_bot = count_row(str(REAL_BOT)).next_to(bot, DOWN, buff=0.45)
        qmark = MathTex("?", font_size=96, color=YELLOW).move_to(row_bot[0]).match_y(row_top)
        cite3 = citation("Wainer & Zwerling data · Wainer, 2007 · American Scientist")
        with self.narrate("Back in Pennsylvania, Howard Wainer and Harris Zwerling counted the "
                          "bottom fifty. Nine of them came from the smallest three percent, even "
                          "more than at the top.") as beat:
            self.play(FadeIn(VGroup(head2, strip, ranks, top, bot, top_t, bot_t, row_top, qmark)),
                      FadeIn(cite3), run_time=beat.until("counted"))
            beat.wait_until("Nine", offset=-0.3)
            self.play(LaggedStart(*[bot[i].animate.set_fill(YELLOW, 0.9).set_stroke(YELLOW)
                                    for i in range(REAL_BOT)], lag_ratio=0.12),
                      ReplacementTransform(qmark, row_bot[0]), FadeIn(row_bot[1]), run_time=1.6)
            beat.wait_until("more", offset=-0.2)
            self.play(Indicate(row_bot[0], color=YELLOW, scale_factor=1.3),
                      Indicate(row_top[0], color=YELLOW, scale_factor=1.3), run_time=1.0)

        gates = text("2005: Gates Foundation changes course", size=LABEL, color=INK).move_to(head2)
        cite4 = citation("Seattle Times, Oct 2005 · quoted in Wainer, 2007")
        with self.narrate("In two thousand five, the Gates Foundation said it was moving away from "
                          "converting large high schools into small ones.") as beat:
            self.play(ReplacementTransform(head2, gates), ReplacementTransform(cite3, cite4),
                      run_time=beat.until("Gates", offset=0.2))
            self.play(Indicate(gates, color=INK, scale_factor=1.05), run_time=1.0)

        same = text("same kind of school", size=LABEL, color=YELLOW).move_to(DOWN * 2.55)
        ar1 = Arrow(same.get_left() + LEFT * 0.05, row_top.get_bottom() + DOWN * 0.05 + RIGHT * 0.6,
                    color=YELLOW, buff=0.1, stroke_width=4, max_tip_length_to_length_ratio=0.15)
        ar2 = Arrow(same.get_right() + RIGHT * 0.05, row_bot.get_bottom() + DOWN * 0.05 + LEFT * 0.6,
                    color=YELLOW, buff=0.1, stroke_width=4, max_tip_length_to_length_ratio=0.15)
        with self.narrate("None of this says small schools are worse. Size sets how far an average "
                          "can swing, and the ranking only saw the swing.") as beat:
            self.play(FadeOut(cite4), FadeIn(same, shift=0.1 * UP), run_time=beat.until("Size"))
            self.play(GrowArrow(ar1), GrowArrow(ar2), run_time=beat.until("swing", offset=-0.1))
            self.play(Indicate(VGroup(*top[:REAL_TOP]), color=YELLOW),
                      Indicate(VGroup(*bot[:REAL_BOT]), color=YELLOW), run_time=1.2)

        # ================================================================= LANDING
        with self.narrate("So when the top of a ranking is full of small groups, check the bottom. "
                          "The best schools are small. So are the worst.") as beat:
            self.play(Indicate(top_t, color=GREEN, scale_factor=1.15), run_time=beat.until("check"))
            self.play(Indicate(bot_t, color=RED, scale_factor=1.15), run_time=1.0)
            beat.wait_until("best", offset=-0.2)
            self.play(Circumscribe(VGroup(top, top_t), color=YELLOW, buff=0.1), run_time=1.2)
            beat.wait_until("worst", offset=-0.2)
            self.play(Circumscribe(VGroup(bot, bot_t), color=YELLOW, buff=0.1), run_time=1.0)

        self.end_card()
