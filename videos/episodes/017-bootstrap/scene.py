"""Episode 17 - The Bootstrap: Error Bars From Your Own Data.

    videos/toolkit/render.sh --preview videos/episodes/017-bootstrap/scene.py Episode /tmp/ep17.mp4
    videos/toolkit/render.sh videos/episodes/017-bootstrap/scene.py Episode videos/episodes/017-bootstrap/final.mp4

Data: Efron & Tibshirani (1993) law-school data (R package `bootstrap`, datasets `law`
and `law82`): a random sample of 15 of 82 American law schools, class-average LSAT and
undergraduate GPA.  Every number on screen is computed below (see facts.md).
"""
from math import comb

import numpy as np
from manim import *
from sample_space import *

# ----------------------------------------------------------------------------- data
POP = np.array([(622, 3.23), (542, 2.83), (579, 3.24), (653, 3.12), (606, 3.09), (576, 3.39), (620, 3.10), (615, 3.40), (553, 2.97), (607, 2.91), (558, 3.11), (596, 3.24), (635, 3.30), (581, 3.22), (661, 3.43), (547, 2.91), (599, 3.23), (646, 3.47), (622, 3.15), (611, 3.33), (546, 2.99), (614, 3.19), (628, 3.03), (575, 3.01), (662, 3.39), (627, 3.41), (608, 3.04), (632, 3.29), (587, 3.16), (581, 3.17), (605, 3.13), (704, 3.36), (477, 2.57), (591, 3.02), (578, 3.03), (572, 2.88), (615, 3.37), (606, 3.20), (603, 3.23), (535, 2.98), (595, 3.11), (575, 2.92), (573, 2.85), (644, 3.38), (545, 2.76), (645, 3.27), (651, 3.36), (562, 3.19), (609, 3.17), (555, 3.00), (586, 3.11), (580, 3.07), (594, 2.96), (594, 3.05), (560, 2.93), (641, 3.28), (512, 3.01), (631, 3.21), (597, 3.32), (621, 3.24), (617, 3.03), (637, 3.33), (572, 3.08), (610, 3.13), (562, 3.01), (635, 3.30), (614, 3.15), (546, 2.82), (598, 3.20), (666, 3.44), (570, 3.01), (570, 2.92), (605, 3.45), (565, 3.15), (686, 3.50), (608, 3.16), (595, 3.19), (590, 3.15), (558, 2.81), (611, 3.16), (564, 3.02), (575, 2.74)])
SAMPLE_IDX = [5, 12, 78, 34, 69, 51, 49, 14, 46, 30, 3, 81, 44, 35, 52]   # rows of `law` in `law82`
LAW = POP[SAMPLE_IDX]
OTHERS = np.array([p for i, p in enumerate(POP) if i not in SAMPLE_IDX])   # the other 67


def corr(X):
    """Pearson r along axis -2 for arrays (..., n, 2)."""
    a = X - X.mean(axis=-2, keepdims=True)
    return (a[..., 0] * a[..., 1]).sum(-1) / np.sqrt((a[..., 0] ** 2).sum(-1) * (a[..., 1] ** 2).sum(-1))


R_OBS = corr(LAW)                     # 0.776
RHO = corr(POP)                       # 0.760
# truth: 100 000 fresh samples of 15 distinct schools from the 82 (simulated)
_rng = np.random.default_rng(17)
_truth_idx = np.argsort(_rng.random((100_000, 82)), axis=1)[:, :15]
R_TRUE = corr(POP[_truth_idx])
SD_TRUE = R_TRUE.std(ddof=1)          # 0.118
# bootstrap: 2000 resamples with replacement from the 15
BOOT_IDX = np.random.default_rng(1008).integers(0, 15, (2000, 15))
R_BOOT = corr(LAW[BOOT_IDX])
SD_BOOT = R_BOOT.std(ddof=1)          # 0.134
CUM_SD = np.array([0.0] + [R_BOOT[:k].std(ddof=1) for k in range(2, 2001)])  # index k-1

# the one resample shown slowly (np.random.default_rng(11).integers(0, 15, 15))
DRAWS = [2, 1, 11, 7, 8, 9, 10, 0, 7, 2, 6, 13, 8, 1, 8]
COUNTS = np.bincount(DRAWS, minlength=15)
R_ONE = corr(LAW[DRAWS])              # 0.800

BINS = np.linspace(0, 1, 41)          # r histogram, bin width 0.025
TRUE_SHARE = np.histogram(R_TRUE, BINS)[0] / len(R_TRUE)
BOOT_CUM = np.array([np.histogram(R_BOOT[:k], BINS)[0] for k in range(0, 2001, 10)])  # every 10

# maximum LSAT: exact distributions
MAXBINS = np.arange(540, 715, 5)
v = np.unique(LAW[:, 0])
_bp = np.diff(np.r_[0, [((LAW[:, 0] <= x).sum() / 15) ** 15 for x in v]])
BOOT_MAX = np.histogram(v, MAXBINS, weights=_bp)[0]
V = np.unique(POP[:, 0])
_tp = np.diff(np.r_[0, [comb(int((POP[:, 0] <= x).sum()), 15) / comb(82, 15) for x in V]])
TRUE_MAX = np.histogram(V, MAXBINS, weights=_tp)[0]
SD_BMAX = np.sqrt((v ** 2 * _bp).sum() - (v * _bp).sum() ** 2)          # 5.73
SD_TMAX = np.sqrt((V ** 2 * _tp).sum() - (V * _tp).sum() ** 2)          # 23.0
P_MISS = (14 / 15) ** 15                                               # 0.355

assert abs(R_OBS - 0.776) < 5e-4 and abs(SD_TRUE - 0.118) < 1.5e-3 and abs(SD_BOOT - 0.134) < 5e-4
assert abs(R_ONE - 0.800) < 5e-4 and round(SD_BMAX, 1) == 5.7 and round(SD_TMAX) == 23


def step_outline(ax, edges, heights, color=GREEN, width=4):
    pts = [ax.c2p(edges[0], 0)]
    for i, h in enumerate(heights):
        pts += [ax.c2p(edges[i], h), ax.c2p(edges[i + 1], h)]
    pts.append(ax.c2p(edges[-1], 0))
    return VMobject(stroke_color=color, stroke_width=width).set_points_as_corners(pts)


def bars(ax, edges, heights, color=PURPLE, opacity=0.8, gap=0.12):
    w = edges[1] - edges[0]
    g = VGroup()
    for i, h in enumerate(heights):
        lo, hi = ax.c2p(edges[i] + gap * w / 2, 0), ax.c2p(edges[i + 1] - gap * w / 2, h)
        r = Rectangle(width=max(hi[0] - lo[0], 1e-3), height=max(hi[1] - lo[1], 1e-3),
                      stroke_width=0, fill_color=color, fill_opacity=opacity if h > 0 else 0)
        r.move_to([(lo[0] + hi[0]) / 2, lo[1], 0], aligned_edge=DOWN)
        g.add(r)
    return g


class Episode(NarratedScene):
    EPISODE = 17
    TITLE = "The Bootstrap: Error Bars From Your Own Data"
    PRONUNCIATIONS = {"Efron": "eff ron"}

    def construct(self):
        # ============================================================ scatter
        sax = axes((470, 710), (2.5, 3.6), x_ticks=[500, 550, 600, 650, 700],
                   y_ticks=[2.6, 2.8, 3.0, 3.2, 3.4], x_length=5.4, y_length=3.5,
                   x_label="class-average LSAT score", y_label="class-average college GPA",
                   y_decimals=1)
        sdots = dots(sax, LAW[:, 0], LAW[:, 1], BLUE, radius=0.075)
        scat = VGroup(sax, sdots)
        scat.move_to([-3.25, -0.35, 0])
        odots = dots(sax, OTHERS[:, 0], OTHERS[:, 1], GRAY, radius=0.06, opacity=0.55)
        home = scat.copy()
        scat.scale(1.2).move_to([-1.3, 0.05, 0])

        rlab = formula("r", "=", "0.78", r"\pm", "?", size=EQ)
        rlab[0:3].set_color(BLUE)
        rlab[3:].set_color(YELLOW)
        rlab.next_to(scat, RIGHT, buff=0.45).align_to(scat, UP).shift(DOWN * 0.6)
        src = citation("Efron & Tibshirani, 1993 · An Introduction to the Bootstrap (law-school data)")

        # ---- B0: cold open
        with self.narrate("Fifteen real American law schools. Across, each school's average "
                          "entrance-test score. Up, its students' average college grades.") as beat:
            self.play(Create(sax), run_time=1.0)
            self.play(LaggedStart(*[GrowFromCenter(d) for d in sdots], lag_ratio=0.08),
                      FadeIn(src), run_time=1.4)
            beat.wait_until("Across", offset=-0.1)
            self.play(Indicate(sax.x_title, color=INK, scale_factor=1.05), run_time=0.9)
            beat.wait_until("Up", offset=-0.1)
            self.play(Indicate(sax.y_title, color=INK, scale_factor=1.05), run_time=0.9)

        # ---- B1: the question + prediction pause
        with self.narrate("The correlation is point seven eight. Using only these fifteen dots, "
                          "can you say how far off that number might be? Yes, or no. [pause 1.5]") as beat:
            self.play(Write(rlab[0:3]), run_time=1.0)
            beat.wait_until("these", offset=-0.1)
            self.play(LaggedStart(*[Indicate(d, color=YELLOW, scale_factor=1.6) for d in sdots],
                                  lag_ratio=0.06), run_time=1.6)
            beat.wait_until("how far", offset=-0.1)
            self.play(Write(rlab[3:]), run_time=0.8)
            beat.wait_until("Yes", offset=0.4)
            self.play(Circumscribe(rlab[4], color=YELLOW, fade_out=True), run_time=1.6)

        # ---- B2: the instinct; make room
        hax = axes((0, 1), (0, 0.16), x_ticks=[0, 0.2, 0.4, 0.6, 0.8, 1.0],
                   y_ticks=[0, 0.05, 0.10, 0.15], x_length=5.4, y_length=3.1,
                   x_label="correlation r", y_label="share of draws", x_decimals=1, y_decimals=2)
        hax.move_to([3.25, -0.55, 0])
        with self.narrate("The instinct is no. To see a number wobble, you would need fresh samples.") as beat:
            self.play(Transform(scat, home), FadeOut(src),
                      rlab.animate.scale(0.8).move_to([3.3, 2.75, 0]), run_time=1.6)
            self.play(Create(hax), run_time=beat.remaining())

        # ---- B3: here we can check
        with self.narrate("But these fifteen were drawn at random from eighty two schools, "
                          "so here we can take fresh samples.") as beat:
            beat.wait_until("eighty", offset=-0.2)
            self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in odots], lag_ratio=0.02),
                      run_time=1.8)
            self.bring_to_front(sdots)
            beat.wait_until("fresh", offset=-0.1)
            # one fresh sample of 15 from the 82, highlighted
            fresh_idx = _truth_idx[0]
            alld = {}
            for i, p in enumerate(POP):
                if i in SAMPLE_IDX:
                    alld[i] = sdots[SAMPLE_IDX.index(i)]
                else:
                    alld[i] = odots[[j for j in range(82) if j not in SAMPLE_IDX].index(i)]
            rings = VGroup(*[Circle(radius=0.13, color=GREEN, stroke_width=3).move_to(alld[i])
                             for i in fresh_idx])
            self.play(LaggedStart(*[Create(c) for c in rings], lag_ratio=0.1), run_time=1.5)

        # ---- B4: truth histogram
        true_bars = bars(hax, BINS, TRUE_SHARE, color=GREEN, opacity=0.35)
        true_line = step_outline(hax, BINS, TRUE_SHARE)
        sd_true = formula(r"\mathrm{SD}(r)", "=", f"{SD_TRUE:.3f}", color=GREEN)
        sd_true.next_to(hax.c2p(0.02, 0.155), DR, buff=0).shift(RIGHT * 0.1)
        brace_true = BraceBetweenPoints(hax.c2p(R_TRUE.mean() - SD_TRUE, 0.135),
                                        hax.c2p(R_TRUE.mean() + SD_TRUE, 0.135), UP, color=GREEN)
        sim = text("simulated: 100,000 draws", size=SMALL, color=GRAY)
        sim.next_to(sd_true, DOWN, buff=0.15).align_to(sd_true, LEFT)
        with self.narrate("Draw fifteen of the eighty two, a hundred thousand times. The correlation "
                          "wobbles, with a standard deviation of point one one eight.") as beat:
            self.play(FadeOut(rings), run_time=0.5)
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in true_bars], lag_ratio=0.03),
                      Create(true_line), run_time=beat.until("wobbles", offset=-0.1))
            beat.wait_until("standard", offset=-0.2)
            self.play(GrowFromCenter(brace_true), run_time=0.8)
            self.play(TransformFromCopy(brace_true, sd_true), FadeIn(sim), run_time=1.0)

        # ---- B5: the target; hide the 82
        target = VGroup(text("target", size=LABEL, color=GRAY), sd_true.copy())
        target.arrange(RIGHT, buff=0.25)
        with self.narrate("That is the target. Hide the eighty two, and recover it from the fifteen alone.") as beat:
            target.move_to([3.3, 2.0, 0])
            self.play(TransformFromCopy(sd_true, target[1]), FadeIn(target[0]),
                      run_time=1.2)
            beat.wait_until("Hide", offset=-0.1)
            self.play(FadeOut(odots), FadeOut(true_bars), FadeOut(true_line), FadeOut(brace_true),
                      FadeOut(sd_true), FadeOut(sim), run_time=1.2)
            self.play(LaggedStart(*[Indicate(d, color=YELLOW, scale_factor=1.5) for d in sdots],
                                  lag_ratio=0.05), run_time=beat.remaining(min_time=1.0))

        # ============================================================ naive
        bw = hax.c2p(0.025, 0)[0] - hax.c2p(0, 0)[0]

        def block(rv, k):
            b0 = np.floor(rv / 0.025) * 0.025
            sq = Square(side_length=bw * 0.9, stroke_width=0, fill_color=PURPLE, fill_opacity=0.9)
            return sq.move_to(hax.c2p(b0 + 0.0125, 0) + UP * (bw * (k + 0.5)))

        spread = formula(r"\mathrm{SD}(r^*)", "=", "0.000", color=RED)
        spread[0].set_color(PURPLE)
        with self.narrate("The obvious move: treat the fifteen as the whole population, "
                          "and draw fifteen schools from them.") as beat:
            self.play(Circumscribe(scat, color=BLUE, buff=0.1), run_time=beat.until("draw"))
            perm = np.random.default_rng(3).permutation(15)
            r1 = VGroup(*[Circle(radius=0.14, color=YELLOW, stroke_width=3).move_to(sdots[i])
                          for i in perm])
            self.play(LaggedStart(*[Create(c) for c in r1], lag_ratio=0.25),
                      run_time=beat.remaining(min_time=2.0))

        rstar = formula("r^*", "=", "0.78", color=PURPLE)
        rstar.next_to(rlab, DOWN, buff=0.25).align_to(rlab, LEFT)
        rstar.move_to([4.2, 1.3, 0])
        target.generate_target().move_to([3.3, 2.05, 0])
        with self.narrate("Without putting any back, every draw yields the same fifteen schools, "
                          "in a new order.") as beat:
            self.play(FadeOut(rlab), MoveToTarget(target), run_time=0.8)
            self.play(Write(rstar), run_time=1.0)
            self.play(TransformFromCopy(rstar[2], block(R_OBS, 0)), run_time=1.0)
            r2 = VGroup(*[Circle(radius=0.14, color=YELLOW, stroke_width=3).move_to(sdots[i])
                          for i in np.random.default_rng(4).permutation(15)])
            self.play(FadeOut(r1), run_time=0.4)
            self.play(LaggedStart(*[Create(c) for c in r2], lag_ratio=0.2),
                      run_time=beat.remaining(min_time=1.6))
        blocks = VGroup(*[m for m in self.mobjects if isinstance(m, Square)])

        with self.narrate("So every redraw gives point seven eight again. The spread is zero, "
                          "and we miss the target by the full point one one eight.") as beat:
            for k in (1, 2, 3):
                b = block(R_OBS, k)
                self.play(TransformFromCopy(rstar[2], b), run_time=0.6)
                blocks.add(b)
            spread.move_to([4.0, 1.3, 0])
            beat.wait_until("spread", offset=-0.1)
            self.play(ReplacementTransform(rstar, spread), FadeOut(r2), run_time=1.0)
            beat.wait_until("miss", offset=-0.1)
            self.play(flag(spread[2], color=RED), flag(target[1][2], color=YELLOW), run_time=1.0)

        # ============================================================ fix
        with self.narrate("The fix is one change: put each school back before the next draw.") as beat:
            self.play(FadeOut(blocks), FadeOut(spread), run_time=0.8)
            back = VGroup(*[Circle(radius=0.14, color=YELLOW, stroke_width=3).move_to(sdots[i])
                            for i in range(15)])
            self.play(LaggedStart(*[Create(c) for c in back], lag_ratio=0.05), run_time=1.0)
            self.play(FadeOut(back), run_time=beat.remaining(min_time=0.6))

        seen = np.zeros(15, int)
        rings = VGroup()
        ring_anims = []
        for i in DRAWS:
            c = Circle(radius=0.14 + 0.075 * seen[i], color=YELLOW, stroke_width=3).move_to(sdots[i])
            seen[i] += 1
            rings.add(c)
            ring_anims.append(Create(c))
        never = [i for i in range(15) if COUNTS[i] == 0]
        twice, thrice = 1, 8
        with self.narrate("Now this school is picked twice, this one three times, and these five never.") as beat:
            self.play(LaggedStart(*ring_anims, lag_ratio=0.5), run_time=beat.until("this school", offset=-0.1))
            self.play(sdots[twice].animate.set_color(YELLOW).scale(1.4), run_time=0.6)
            beat.wait_until("this one", offset=-0.1)
            self.play(sdots[twice].animate.set_color(BLUE).scale(1 / 1.4),
                      sdots[thrice].animate.set_color(YELLOW).scale(1.4), run_time=0.6)
            beat.wait_until("these five", offset=-0.1)
            self.play(sdots[thrice].animate.set_color(BLUE).scale(1 / 1.4),
                      *[sdots[i].animate.set_opacity(0.25) for i in never], run_time=0.9)

        rstar1 = formula("r^*", "=", f"{R_ONE:.2f}", color=PURPLE).move_to([4.2, 1.3, 0])
        b_one = block(R_ONE, 0)
        with self.narrate("This resample has its own correlation, point eight oh.") as beat:
            self.play(Write(rstar1), run_time=beat.until("point", offset=-0.1))
            self.play(TransformFromCopy(rstar1[2], b_one), run_time=1.0)

        # ============================================================ insight
        def panel(cx, pts_main, pts_ctx=None, rings_for=None):
            box_ = RoundedRectangle(corner_radius=0.12, width=2.7, height=2.0, stroke_color=DIM,
                                    stroke_width=2).move_to([cx, 1.15, 0])

            def m(p):
                return np.array([cx - 1.15 + 2.3 * (p[0] - 470) / 240,
                                 1.15 - 0.8 + 1.6 * (p[1] - 2.5) / 1.1, 0])
            g = VGroup()
            if pts_ctx is not None:
                g.add(VGroup(*[Dot(m(p), radius=0.05, color=GRAY, fill_opacity=0.55) for p in pts_ctx]))
            g.add(VGroup(*[Dot(m(p), radius=0.055, color=BLUE) for p in pts_main]))
            extra = VGroup()
            if rings_for is not None:
                for i, c in enumerate(rings_for):
                    for k in range(1, c):
                        extra.add(Circle(radius=0.055 + 0.05 * k, color=YELLOW, stroke_width=2).move_to(m(LAW[i])))
            return box_, g, extra

        b1, g1, _ = panel(-4.55, LAW, OTHERS)
        b2, g2, _ = panel(0.0, LAW)
        b3, g3, e3 = panel(4.55, LAW[COUNTS > 0], rings_for=COUNTS)
        n1 = label("82 schools", color=GRAY).next_to(b1, UP, buff=0.18)
        n2 = label("the sample", color=GRAY).next_to(b2, UP, buff=0.18)
        n3 = label("a resample", color=GRAY).next_to(b3, UP, buff=0.18)
        a1 = Arrow(b1.get_right(), b2.get_left(), buff=0.12, color=GRAY, stroke_width=4)
        a2 = Arrow(b2.get_right(), b3.get_left(), buff=0.12, color=GRAY, stroke_width=4)
        l1 = VGroup(label("draw 15", size=26), label("at random", size=26)).arrange(DOWN, buff=0.08).next_to(a1, DOWN, buff=0.15)
        l2 = VGroup(label("draw 15", size=26), label("put back", size=26)).arrange(DOWN, buff=0.08).next_to(a2, DOWN, buff=0.15)
        s1 = formula(r"\rho", "=", f"{RHO:.2f}", color=GREEN).next_to(b1, DOWN, buff=0.25)
        s2 = formula("r", "=", f"{R_OBS:.2f}", color=BLUE).next_to(b2, DOWN, buff=0.25)
        s3 = formula("r^*", "=", f"{R_ONE:.2f}", color=PURPLE).next_to(b3, DOWN, buff=0.25)

        with self.narrate("Why should that help? The real sample came from fifteen random draws "
                          "out of a population.") as beat:
            self.play(FadeOut(hax), FadeOut(b_one), FadeOut(target), FadeOut(rings),
                      FadeOut(rstar1), *[sdots[i].animate.set_opacity(1) for i in never], run_time=0.8)
            self.play(ReplacementTransform(sdots.copy(), g2[0]), FadeOut(scat),
                      Create(b2), FadeIn(n2), run_time=1.4)
            self.play(Write(s2), run_time=0.8)
            beat.wait_until("population", offset=-0.6)
            self.play(Create(b1), FadeIn(g1), FadeIn(n1), GrowArrow(a1), FadeIn(l1),
                      run_time=1.2)
            self.play(Write(s1), run_time=0.8)

        with self.narrate("Resampling repeats that step on the sample itself: fifteen random draws, "
                          "from the best stand-in for the population we have.") as beat:
            self.play(GrowArrow(a2), FadeIn(l2), Create(b3), FadeIn(n3), run_time=1.2)
            self.play(TransformFromCopy(VGroup(*[g2[0][i] for i in range(15) if COUNTS[i] > 0]), g3[0]),
                      run_time=1.4)
            self.play(LaggedStart(*[Create(c) for c in e3], lag_ratio=0.2), Write(s3),
                      run_time=beat.until("stand", offset=-0.1, min_time=1.0))
            self.play(Indicate(g2, color=YELLOW, scale_factor=1.04), run_time=1.0)

        eq = MathTex(r"\mathrm{SD}(", "r", "-", r"\rho", ")", r"\approx", r"\mathrm{SD}(", "r^*",
                     "-", "r", ")", font_size=EQ)
        eq[1].set_color(BLUE); eq[3].set_color(GREEN); eq[7].set_color(PURPLE); eq[9].set_color(BLUE)
        eq.move_to([0, -1.85, 0])
        with self.narrate("So the wobble of r star around point seven eight should mimic the "
                          "wobble of r around the truth.") as beat:
            self.play(Write(VGroup(eq[6], eq[8], eq[10])), run_time=0.6)
            self.play(TransformFromCopy(s3[0], eq[7]), run_time=beat.until("around", offset=-0.1, min_time=0.8))
            self.play(TransformFromCopy(s2[2], eq[9]), run_time=0.9)
            beat.wait_until("wobble", occurrence=2, offset=-0.1)
            self.play(Write(VGroup(eq[0], eq[2], eq[4], eq[5])), TransformFromCopy(s2[0], eq[1]),
                      run_time=1.0)
            beat.wait_until("truth", offset=-0.2)
            self.play(TransformFromCopy(s1[0], eq[3]), run_time=0.9)

        # ============================================================ run 2000
        hgrp = VGroup(hax)
        big_center = np.array([0.25, -0.75, 0])
        prog = ValueTracker(0)

        def boot_bars():
            k = int(round(prog.get_value() / 10))
            return bars(hax, BINS, BOOT_CUM[k] / 2000, color=PURPLE, opacity=0.8)
        bb = always_redraw(boot_bars)
        cnt = live_number(prog, 0, size=MATH, prefix=r"\text{resamples} =")
        sd_tr = ValueTracker(0)
        sd_tr.add_updater(lambda m: m.set_value(CUM_SD[max(int(prog.get_value()) - 1, 0)]))
        sdl = live_number(sd_tr, 3, size=MATH, color=PURPLE, prefix=r"\mathrm{SD}(r^*) =")
        with self.narrate("Run two thousand resamples, each one dropping its own r star onto the pile.") as beat:
            self.play(FadeOut(VGroup(b1, b2, b3, g1, g2, g3, e3, n1, n2, n3, a1, a2, l1, l2, s1, s2, s3)),
                      eq.animate.scale(0.85).move_to([0, 3.1, 0]), run_time=1.0)
            hax.scale(1.35).move_to(big_center)
            leg = VGroup(cnt, sdl).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            leg.next_to(hax.c2p(0.0, 0.16), DR, buff=0).shift(RIGHT * 0.25 + DOWN * 0.05)
            self.play(FadeIn(hax), FadeIn(leg), run_time=0.8)
            self.add(bb, sd_tr)
            self.play(prog.animate.set_value(2000), run_time=beat.remaining(min_time=1.0),
                      rate_func=rate_functions.ease_in_quad)
        bb.clear_updaters(); sd_tr.clear_updaters()
        cnt.number.clear_updaters(); sdl.number.clear_updaters()
        cnt.number.set_value(2000); sdl.number.set_value(SD_BOOT)

        true_line2 = step_outline(hax, BINS, TRUE_SHARE, width=5)
        sdt = formula(r"\mathrm{SD}(r) =", f"{SD_TRUE:.3f}", color=GREEN)
        sdt.next_to(leg, DOWN, buff=0.25).align_to(leg, LEFT)
        with self.narrate("Their spread is point one three four. Will it match the true spread? [pause 1.5]") as beat:
            self.play(Circumscribe(sdl, color=PURPLE, fade_out=True), run_time=1.2)

        with self.narrate("The truth is point one one eight, so we land within two hundredths, "
                          "using no new data.") as beat:
            self.play(Create(true_line2), run_time=beat.until("one", offset=-0.2, min_time=1.0))
            self.play(Write(sdt), run_time=1.0)
            beat.wait_until("within", offset=-0.1)
            self.play(flag(sdt[1], color=GREEN), flag(sdl.number, color=PURPLE), run_time=1.0)

        with self.narrate("It runs slightly wide, mostly because the real fifteen came from a pool "
                          "of only eighty two, without repeats.") as beat:
            br_b = BraceBetweenPoints(hax.c2p(R_BOOT.mean() - SD_BOOT, 0.145), hax.c2p(R_BOOT.mean() + SD_BOOT, 0.145), UP, color=PURPLE)
            br_t = BraceBetweenPoints(hax.c2p(R_TRUE.mean() - SD_TRUE, 0.115), hax.c2p(R_TRUE.mean() + SD_TRUE, 0.115), UP, color=GREEN)
            self.play(GrowFromCenter(br_b), run_time=0.9)
            self.play(GrowFromCenter(br_t), run_time=0.9)
            beat.wait_until("eighty", offset=-0.3)
            self.play(Indicate(br_t, color=GREEN), run_time=1.0)

        # ============================================================ payoff
        quote = text("“for reasons which will become obvious”", size=BODY, color=INK,
                     slant=ITALIC).move_to([0, 3.1, 0])
        cite = citation("Efron, 1979 · Annals of Statistics 7(1): 1–26")
        with self.narrate("Bradley Efron published this in nineteen seventy nine, and named it the "
                          "bootstrap, for reasons, he wrote, which will become obvious.") as beat:
            self.play(FadeOut(eq, shift=UP * 0.3), FadeOut(br_b), FadeOut(br_t), FadeIn(cite), run_time=1.0)
            beat.wait_until("reasons", offset=-0.1)
            self.play(Write(quote), run_time=beat.remaining(min_time=1.2))
        self.hold(0.6)

        # ============================================================ the blind spot: maximum
        with self.narrate("It has a blind spot. Ask instead about the top score among the fifteen: "
                          "six hundred and sixty six.") as beat:
            self.play(FadeOut(VGroup(hax, bb, leg, sdt, true_line2, quote, cite)), run_time=0.8)
            scat.become(home)
            for i in never:
                sdots[i].set_opacity(1)
            self.play(FadeIn(scat), run_time=0.8)
            top = int(np.argmax(LAW[:, 0]))
            beat.wait_until("top", offset=-0.1)
            vline = DashedLine(sax.c2p(666, 2.5), sax.c2p(666, 3.6), color=YELLOW, stroke_width=3)
            tl = formula("666", color=YELLOW, size=MATH).next_to(vline, UP, buff=0.1)
            self.play(sdots[top].animate.set_color(YELLOW).scale(1.5), Create(vline), run_time=1.0)
            beat.wait_until("six", offset=-0.1)
            self.play(Write(tl), run_time=0.8)

        pm = MathTex(r"\left(\tfrac{14}{15}\right)", "^{15}", r"\approx", f"{P_MISS:.3f}", font_size=EQ)
        pm.move_to([3.3, 2.2, 0])
        pm[0].set_color(INK)
        draws_row = VGroup(*[MathTex(r"\tfrac{14}{15}", font_size=30, color=GRAY) for _ in range(15)])
        draws_row.arrange_in_grid(3, 5, buff=(0.25, 0.15)).move_to([3.3, 0.6, 0])
        with self.narrate("Each draw misses that school with chance fourteen in fifteen. All fifteen "
                          "draws miss it about thirty five percent of the time.") as beat:
            beat.wait_until("fourteen", offset=-0.2)
            self.play(Write(draws_row[0]), run_time=0.8)
            beat.wait_until("All", offset=-0.1)
            self.play(LaggedStart(*[TransformFromCopy(draws_row[0], d) for d in draws_row[1:]],
                                  lag_ratio=0.08), run_time=1.6)
            self.play(TransformFromCopy(draws_row, VGroup(pm[0], pm[1])), run_time=1.2)
            self.play(Write(pm[2:]), run_time=beat.remaining(min_time=0.8))

        # max histogram
        mx = axes((540, 712), (0, 0.7), x_ticks=[550, 600, 650, 700], y_ticks=[0, 0.2, 0.4, 0.6],
                  x_length=5.6, y_length=3.0, x_label="highest LSAT among the 15",
                  y_label="share of draws", y_decimals=1)
        mx.move_to([3.2, -0.5, 0])
        bmax = bars(mx, MAXBINS, BOOT_MAX, color=PURPLE)
        tmax = step_outline(mx, MAXBINS, TRUE_MAX, width=4)
        hit = formula(r"1-0.355", "=", "0.645", color=PURPLE, size=MATH)
        with self.narrate("So sixty four percent of resamples report exactly six sixty six, "
                          "and none can go higher.") as beat:
            self.play(FadeOut(draws_row), pm.animate.scale(0.8).move_to([3.3, 3.1, 0]), run_time=0.8)
            self.play(Create(mx), run_time=0.8)
            beat.wait_until("sixty four", offset=-0.2)
            hit.next_to(mx.c2p(645, 0.645), LEFT, buff=0.3)
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bmax], lag_ratio=0.02),
                      TransformFromCopy(pm[3], hit[0]), run_time=1.4)
            self.play(Write(hit[1:]), run_time=0.7)
            beat.wait_until("none", offset=-0.1)
            ceil = DashedLine(mx.c2p(670, 0), mx.c2p(670, 0.7), color=RED, stroke_width=4)
            self.play(Create(ceil), run_time=0.8)

        sbm = formula(r"\mathrm{SD} =", f"{SD_BMAX:.1f}", color=PURPLE)
        stm = formula(r"\mathrm{SD} =", f"{SD_TMAX:.0f}", color=GREEN)
        third = formula(r"P(\text{above }666)", r"\approx", r"\tfrac{1}{3}", color=GREEN, size=MATH)
        with self.narrate("A fresh fifteen from the eighty two tops six sixty six about a third of "
                          "the time. The bootstrap's spread is six points; the true spread is "
                          "twenty three.") as beat:
            self.play(FadeOut(hit), run_time=0.5)
            self.play(Create(tmax), run_time=1.4)
            beat.wait_until("third", offset=-0.4)
            third.next_to(mx.c2p(690, 0.3), UP, buff=0.1)
            self.play(Write(third), run_time=1.0)
            beat.wait_until("spread", offset=-0.2)
            VGroup(sbm, stm).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(mx.c2p(545, 0.68), DR, buff=0)
            self.play(Write(sbm), run_time=0.8)
            beat.wait_until("true", offset=-0.1)
            self.play(Write(stm), run_time=0.8)

        with self.narrate("Resampling cannot invent a school better than the best one it has seen. "
                          "It works for smooth statistics like the correlation, not for extremes.") as beat:
            self.play(Indicate(ceil, color=RED, scale_factor=1.02), sdots[top].animate.scale(1.2), run_time=1.2)
            beat.wait_until("smooth", offset=-0.2)
            self.play(Indicate(sdots, color=BLUE, scale_factor=1.15), run_time=1.0)
            beat.wait_until("extremes", offset=-0.2)
            self.play(flag(VGroup(vline, tl), color=RED), run_time=1.0)

        # ============================================================ landing
        final = formula("r", "=", "0.78", r"\pm", "0.13", size=EQ)
        final[0:3].set_color(BLUE)
        final[3:].set_color(PURPLE)
        q = formula("r", "=", "0.78", r"\pm", "?", size=EQ)
        q[0:3].set_color(BLUE); q[3:].set_color(YELLOW)
        with self.narrate("So the answer to the opening question is yes: point seven eight, "
                          "give or take point one three.") as beat:
            self.play(FadeOut(VGroup(mx, bmax, tmax, ceil, sbm, stm, third, pm, vline, tl)),
                      sdots[top].animate.set_color(BLUE).scale(1 / 1.8), run_time=0.8)
            self.play(scat.animate.scale(1.2).move_to([-1.3, 0.05, 0]), run_time=1.2)
            q.next_to(scat, RIGHT, buff=0.45).align_to(scat, UP).shift(DOWN * 0.6)
            final.move_to(q, aligned_edge=LEFT)
            self.play(FadeIn(q), run_time=0.6)
            beat.wait_until("give", offset=-0.2)
            self.play(TransformMatchingTex(q, final), run_time=1.0)

        with self.narrate("The fifteen dots were enough, once each school was allowed to count twice, "
                          "or not at all.") as beat:
            self.play(LaggedStart(*[Indicate(sdots[i], color=YELLOW, scale_factor=1.6)
                                    for i in range(15) if COUNTS[i] >= 2], lag_ratio=0.2),
                      run_time=beat.until("not", offset=-0.1, min_time=1.0))
            self.play(*[sdots[i].animate.set_opacity(0.3) for i in never], run_time=0.8)
        self.end_card()
