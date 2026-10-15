"""Episode 27 - When Missing Data Isn't Missing at Random.

    videos/toolkit/render.sh --preview videos/episodes/027-missing-data-mechanisms/scene.py Episode /tmp/ep27.mp4
"""
import sys
from pathlib import Path

import numpy as np
from manim import *
from sample_space import *

sys.path.insert(0, str(Path(__file__).resolve().parent))
from data import build  # noqa: E402

D = build()
AGE, INC, T = D["age"], D["inc"], D["T"]
N = len(AGE)


def dollars(k):                      # $ thousands -> dollars rounded to $10
    return round(k * 100) * 10


# Table 3, column (1), men: nonresponse share by SSA earnings decile / top percentiles
TAILS = [26.7, 25.3, 21.7, 21.0, 18.9, 17.9, 17.8, 17.6, 18.5, 20.0, 19.9, 22.7, 25.2, 27.1, 32.0]


class Episode(NarratedScene):
    EPISODE = 27
    TITLE = "When Missing Data Isn't Missing at Random"
    PRONUNCIATIONS = {"Molenberghs": "moh len bergs"}

    # ------------------------------------------------------------------ helpers
    def dot_at(self, a, y, color=BLUE, r=0.06):
        return Dot(self.ax.c2p(a, y), radius=r, color=color)

    def tick_at(self, a):
        p = self.ax.c2p(a, 0)
        return Line(p + UP * 0.06, p + UP * 0.30, color=PURPLE, stroke_width=3.5)

    def hline(self, y, color, dashed=False):
        a, b = self.ax.c2p(20, y), self.ax.c2p(65, y)
        if dashed:
            return DashedLine(a, b, color=color, stroke_width=3, dash_length=0.12)
        return Line(a, b, color=color, stroke_width=4)

    def reg_line(self, a, b, color, dashed=False):
        p, q = self.ax.c2p(20, a + b * 20), self.ax.c2p(65, a + b * 65)
        if dashed:
            return DashedLine(p, q, color=color, stroke_width=3, dash_length=0.12)
        return Line(p, q, color=color, stroke_width=4)

    def fog(self, kind, n=28, peak=0.55):
        f = D["fog"][kind]
        x0, y0 = self.ax.c2p(20, 0)[:2]
        x1, y1 = self.ax.c2p(65, 90)[:2]
        g = VGroup()
        if kind == "MCAR":
            g.add(Rectangle(width=x1 - x0, height=y1 - y0, stroke_width=0, fill_color=PURPLE,
                            fill_opacity=peak * 0.3).move_to([(x0 + x1) / 2, (y0 + y1) / 2, 0]))
        elif kind == "MAR":
            w = (x1 - x0) / n
            for i in range(n):
                a = 20 + 45 * (i + 0.5) / n
                g.add(Rectangle(width=w + 0.005, height=y1 - y0, stroke_width=0, fill_color=PURPLE,
                                fill_opacity=peak * f(a, 0)).move_to([x0 + w * (i + 0.5), (y0 + y1) / 2, 0]))
        else:
            h = (y1 - y0) / n
            for i in range(n):
                y = 90 * (i + 0.5) / n
                g.add(Rectangle(width=x1 - x0, height=h + 0.005, stroke_width=0, fill_color=PURPLE,
                                fill_opacity=peak * f(0, y)).move_to([(x0 + x1) / 2, y0 + h * (i + 0.5), 0]))
        g.set_z_index(-2)
        return g

    def erase(self, kind, run_time):
        miss = D[kind]["miss"]
        idx = [i for i in np.random.default_rng(5).permutation(N) if miss[i]]
        return LaggedStart(*[Transform(self.people[i], self.tick_at(AGE[i])) for i in idx],
                           lag_ratio=0.02, run_time=run_time)

    def restore(self, run_time):
        return AnimationGroup(*[Transform(p, self.dot_at(AGE[i], INC[i])) for i, p in enumerate(self.people)],
                              run_time=run_time)

    def row(self, name, color, tracker, y, sign=False):
        lab = text(name, size=LABEL, color=color)
        lab.move_to([self.PX0 + lab.width / 2, y, 0])
        num = DecimalNumber(dollars(tracker.get_value()), num_decimal_places=0, include_sign=sign,
                            font_size=MATH, color=color, edge_to_fix=RIGHT)
        num.move_to([self.PX1 - num.width / 2, y, 0])
        num.add_updater(lambda m: m.set_value(dollars(tracker.get_value())))
        return VGroup(lab, num)

    # ------------------------------------------------------------------ scene
    def construct(self):
        self.PX0, self.PX1 = 2.05, 6.3          # right-hand readout panel
        ax = axes((20, 65), (0, 90), x_ticks=[20, 30, 40, 50, 60], y_ticks=[0, 20, 40, 60, 80],
                  x_length=7.3, y_length=4.75, x_label="age (years)", y_label="income ($ thousands)")
        ax.shift(np.array([-6.3 - ax.get_left()[0], -2.75 - ax.get_bottom()[1], 0]))
        self.ax = ax
        sim = text("simulated", size=SMALL, color=GRAY)
        sim.next_to(ax.c2p(65, 90), DOWN, buff=0.05).align_to(ax.c2p(65, 0), RIGHT)
        self.people = VGroup(*[self.dot_at(a, y) for a, y in zip(AGE, INC)])
        order = np.argsort(AGE)

        truth = ValueTracker(T)
        est = ValueTracker(D["MNAR"]["cc"])
        err = ValueTracker(D["MNAR"]["cc"] - T)
        header = text("average income ($)", size=LABEL, color=GRAY)
        header.move_to([self.PX0 + header.width / 2, 2.55, 0])
        r_true = self.row("everyone", INK, truth, 1.8)
        r_est = self.row("answers only", BLUE, est, 1.1)
        r_err = self.row("error", RED, err, 0.4, sign=True)
        est_line = always_redraw(lambda: self.hline(est.get_value(), BLUE))
        true_line = self.hline(T, INK, dashed=True)
        gap = always_redraw(lambda: Line(self.ax.c2p(65, T), self.ax.c2p(65, est.get_value()),
                                         color=RED, stroke_width=7))

        # ---------------------------------------------------------- 1. cold open
        self.add(ax, sim)
        with self.narrate("Three hundred people answer a survey about age and income. Ninety of them "
                          "leave the income blank, so for them we know the age, but not the income.") as beat:
            self.play(LaggedStart(*[FadeIn(self.people[i], scale=0.5) for i in order], lag_ratio=0.004),
                      run_time=beat.until("Ninety", offset=-0.2))
            self.play(self.erase("MNAR", run_time=beat.until("know", offset=-0.1)))
            ticks_hint = VGroup(*[self.people[i] for i in range(N) if D["MNAR"]["miss"][i]])
            self.play(Indicate(ticks_hint, color=PURPLE, scale_factor=1.15), run_time=1.0)

        with self.narrate("Drop the blanks and average the two hundred and ten answers. "
                          "Is that too high, too low, or about right? [pause 1.5]") as beat:
            self.play(FadeIn(header), FadeIn(r_est), run_time=beat.until("average", offset=-0.1))
            self.play(Create(est_line), run_time=1.0)
            q = text("?", size=TITLE, color=INK).move_to([self.PX1 - 0.15, 1.8, 0])
            lab_q = r_true[0].copy()
            beat.wait_until("too high", offset=-0.1)
            self.play(FadeIn(lab_q), FadeIn(q), run_time=0.8)
            beat.wait_until("about right", offset=0.6)
            # prediction hold: the blue line and the empty slot for the truth
            self.play(Indicate(q, color=YELLOW, scale_factor=1.2), run_time=1.0)

        # ---------------------------------------------------------- 2. reveal
        with self.narrate("This survey is simulated, so we know the truth: thirty nine thousand, two hundred "
                          "and fifty. Deleting the blanks came in about fifty seven hundred dollars low, "
                          "and nothing in the remaining dots looks wrong.") as beat:
            self.play(Indicate(sim, color=YELLOW, scale_factor=1.15), run_time=1.0)
            beat.wait_until("truth", offset=-0.3)
            self.play(Create(true_line), FadeOut(q), FadeOut(lab_q), FadeIn(r_true), run_time=1.2)
            beat.wait_until("Deleting", offset=-0.1)
            self.add(gap)
            self.play(FadeIn(r_err), Create(gap), run_time=1.0)
            beat.wait_until("nothing", offset=-0.1)
            survivors = VGroup(*[self.people[i] for i in range(N) if not D["MNAR"]["miss"][i]])
            self.play(Indicate(survivors, color=BLUE, scale_factor=1.12), run_time=1.6)

        # ---------------------------------------------------------- 3. stakes
        panel = VGroup(header, r_true, r_est, r_err)
        waffle = VGroup(*[Square(0.25, stroke_width=0, fill_color=PURPLE if k < 43 else GRAY,
                                 fill_opacity=0.95 if k < 43 else 0.35) for k in range(100)])
        waffle.arrange_in_grid(10, 10, buff=0.07, flow_order="dr")
        waffle.move_to([(self.PX0 + self.PX1) / 2, 0.95, 0])
        w43 = formula(r"43\%", size=EQ, color=PURPLE)
        w_lab = text("of earnings unreported", size=LABEL, color=INK)
        w_src = text("US Current Population Survey, 2016", size=SMALL, color=GRAY)
        w_txt = VGroup(w43, w_lab, w_src).arrange(DOWN, buff=0.14).next_to(waffle, DOWN, buff=0.3)
        cite_b = citation("Bollinger et al., 2019 · J. Political Economy")
        with self.narrate("America's official income and poverty numbers come from a survey where, by "
                          "twenty sixteen, forty three percent of earnings went unreported.") as beat:
            self.play(FadeOut(panel), dim(self.people, est_line, true_line, opacity=0.25),
                      FadeOut(gap), run_time=0.8)
            self.play(LaggedStart(*[FadeIn(s, scale=0.6) for s in waffle], lag_ratio=0.01),
                      run_time=beat.until("forty three", offset=-0.2))
            self.play(Write(w43), FadeIn(w_lab), FadeIn(w_src), FadeIn(cite_b), run_time=1.0)

        # ---------------------------------------------------------- 4. three erasers: restore
        truth.set_value(T)
        est.set_value(T)
        err.set_value(0)
        with self.narrate("Whether deletion is safe depends on who skipped. So let's restore all ninety, "
                          "and try three erasers.") as beat:
            self.play(FadeOut(waffle), FadeOut(w_txt), FadeOut(cite_b), run_time=0.8)
            self.remove(est_line)
            self.people.set_opacity(1)
            true_line.set_opacity(1)
            self.play(FadeIn(panel), run_time=0.6)
            beat.wait_until("restore", offset=-0.1)
            self.play(self.restore(run_time=1.6))
            self.add(est_line, gap)

        # ---------------------------------------------------------- eraser 1: MCAR
        f1 = self.fog("MCAR")
        e1 = text("eraser 1: coin flip", size=LABEL, color=PURPLE).move_to([self.PX0, -0.5, 0], aligned_edge=LEFT)
        with self.narrate("Eraser one flips a coin for each person, so its fog is even everywhere. "
                          "The average of the rest misses by under five hundred dollars. Deletion works.") as beat:
            self.play(FadeIn(e1), run_time=0.6)
            beat.wait_until("fog", offset=-0.1)
            self.play(FadeIn(f1), run_time=1.0)
            self.play(self.erase("MCAR", run_time=beat.until("average", offset=-0.1)))
            m = D["MCAR"]["cc"]
            self.play(est.animate.set_value(m), err.animate.set_value(m - T), run_time=1.2)
            beat.wait_until("works", offset=-0.2)
            self.play(Indicate(r_err, color=YELLOW, scale_factor=1.1), run_time=0.8)

        # ---------------------------------------------------------- eraser 2: MAR (fail)
        f2 = self.fog("MAR")
        e2 = text("eraser 2: takes the young", size=LABEL, color=PURPLE).move_to(e1, aligned_edge=LEFT)
        with self.narrate("Eraser two takes the young. Its fog is thick on the left and thin on the right. "
                          "Now deletion comes in high, by about forty six hundred dollars, because the "
                          "survivors are too old, and older people here earn more.") as beat:
            self.play(self.restore(run_time=1.0), est.animate.set_value(T), err.animate.set_value(0),
                      ReplacementTransform(e1, e2), ReplacementTransform(f1, f2), run_time=1.2)
            self.play(self.erase("MAR", run_time=beat.until("Now", offset=-0.1)))
            m = D["MAR"]["cc"]
            self.play(est.animate.set_value(m), err.animate.set_value(m - T), run_time=beat.until("because"))
            old = VGroup(*[self.people[i] for i in range(N) if (not D["MAR"]["miss"][i]) and AGE[i] > 45])
            beat.wait_until("too old", offset=-0.2)
            self.play(Indicate(old, color=BLUE, scale_factor=1.25), run_time=1.2)
            beat.wait_until("earn more", offset=-0.3)
            arrow = Arrow(self.ax.c2p(30, 15), self.ax.c2p(58, 70), color=GRAY, stroke_width=4, buff=0,
                          max_tip_length_to_length_ratio=0.06).set_z_index(-1)
            self.play(GrowArrow(arrow), run_time=1.0)

        # ---------------------------------------------------------- insight: one age slice
        a0, a1 = 29, 35
        band = Rectangle(width=self.ax.c2p(a1, 0)[0] - self.ax.c2p(a0, 0)[0],
                         height=self.ax.c2p(0, 90)[1] - self.ax.c2p(0, 0)[1],
                         stroke_color=YELLOW, stroke_width=3, fill_color=YELLOW, fill_opacity=0.08)
        band.move_to(self.ax.c2p((a0 + a1) / 2, 45)).set_z_index(-1)
        in_band = VGroup(*[self.people[i] for i in range(N) if a0 <= AGE[i] <= a1 and not D["MAR"]["miss"][i]])
        mar_line = self.reg_line(D["MAR"]["a"], D["MAR"]["b"], BLUE)
        true_reg = self.reg_line(*D["true_line"], INK, dashed=True)
        with self.narrate("But look inside one slice of age. Here the fog is even, so within this slice, "
                          "the eraser picked at random. Survivors in every slice are a fair sample, "
                          "and a line through them lands on the true line.") as beat:
            self.play(FadeOut(arrow), Create(band), run_time=beat.until("Here", offset=-0.1))
            self.play(Indicate(VGroup(*f2[8:11]), color=PURPLE, scale_factor=1.0), run_time=1.0)
            beat.wait_until("random", offset=-0.2)
            self.play(Indicate(in_band, color=YELLOW, scale_factor=1.3), run_time=1.0)
            beat.wait_until("every slice", offset=-0.2)
            self.play(band.animate.move_to(self.ax.c2p(56, 45)), run_time=beat.until("line", offset=-0.2))
            self.play(Create(mar_line), FadeOut(band), run_time=1.0)
            beat.wait_until("true line", offset=-0.2)
            self.play(Create(true_reg), run_time=1.0)

        fill_lab = text("answers + fills", size=LABEL, color=GREEN).move_to(r_est[0], aligned_edge=LEFT)
        miss2 = np.where(D["MAR"]["miss"])[0]
        with self.narrate("Fill each blank from that line, plus the usual scatter, and the error drops "
                          "under two hundred dollars.") as beat:
            self.play(LaggedStart(*[Transform(self.people[i], self.dot_at(AGE[i], f, GREEN))
                                    for i, f in zip(miss2, D["MAR"]["fill"])], lag_ratio=0.01),
                      run_time=beat.until("error", offset=-0.2))
            m = D["MAR"]["imp"]
            self.play(Transform(r_est[0], fill_lab), r_est[1].animate.set_color(GREEN),
                      est.animate.set_value(m), err.animate.set_value(m - T), run_time=1.5)
            est_line.set_color(GREEN)

        # ---------------------------------------------------------- formula from the picture
        fA = formula(r"P(", r"\text{blank}", r"\mid", r"\text{age}", r",\,", r"\text{income}", r")",
                     size=38)
        fB = formula(r"=", r"P(", r"\text{blank}", r"\mid", r"\text{age}", r")", size=38)
        for f, (b, a) in ((fA, (1, 3)), (fB, (2, 4))):
            f[b].set_color(PURPLE)
            f[a].set_color(YELLOW)
        fA[5].set_color(BLUE)
        fA.move_to([(self.PX0 + self.PX1) / 2, -0.95, 0])
        fB.next_to(fA, DOWN, buff=0.25).align_to(fA, LEFT).shift(RIGHT * 0.35)
        mar_txt = text("missing at random", size=LABEL, color=INK).next_to(fB, DOWN, buff=0.3)
        mar_txt.set_x((self.PX0 + self.PX1) / 2)
        cite_r = citation("Rubin, 1976 · Biometrika")
        blanks_now = VGroup(*[self.people[i] for i in miss2])
        with self.narrate("In symbols, the chance of a blank, given age and income, equals the chance given "
                          "age alone. Donald Rubin named this missing at random, in nineteen seventy six.") as beat:
            self.play(FadeOut(e2), Write(fA[0]), run_time=beat.until("blank", offset=-0.2))
            self.play(TransformFromCopy(blanks_now, fA[1]), run_time=0.9)
            beat.wait_until("age", offset=-0.2)
            self.play(Write(fA[2]), TransformFromCopy(ax.x_title, fA[3]), run_time=0.8)
            self.play(Write(fA[4]), TransformFromCopy(ax.y_title, fA[5]), Write(fA[6]),
                      run_time=beat.until("equals", offset=-0.1))
            self.play(Write(fB[0:2]), TransformFromCopy(fA[1], fB[2]), Write(fB[3]),
                      TransformFromCopy(fA[3], fB[4]), Write(fB[5]), run_time=beat.until("alone", offset=0.2))
            beat.wait_until("Rubin", offset=-0.2)
            self.play(FadeIn(mar_txt, shift=0.1 * UP), FadeIn(cite_r), run_time=0.9)
            self.play(Indicate(f2, color=PURPLE, scale_factor=1.0), run_time=1.2)

        # ---------------------------------------------------------- eraser 3: MNAR, prediction
        f3 = self.fog("MNAR")
        e3 = text("eraser 3: takes high earners", size=LABEL, color=PURPLE)
        e3.move_to([self.PX0, 2.55, 0], aligned_edge=LEFT)
        surv_line3 = self.reg_line(D["MNAR"]["a"], D["MNAR"]["b"], BLUE)
        with self.narrate("Eraser three takes high earners. Its fog thickens toward the top. This is the "
                          "survey we started with. Will the same fix rescue it? [pause 1.5]") as beat:
            self.play(FadeOut(cite_r), FadeOut(mar_line), self.restore(run_time=1.2),
                      Transform(r_est[0], text("answers only", size=LABEL, color=BLUE).move_to(r_est[0], aligned_edge=LEFT)),
                      r_est[1].animate.set_color(BLUE), est.animate.set_value(T), err.animate.set_value(0),
                      run_time=1.2)
            est_line.set_color(BLUE)
            beat.wait_until("fog", offset=-0.2)
            self.play(ReplacementTransform(f2, f3), run_time=1.0)
            self.play(self.erase("MNAR", run_time=beat.until("Will", offset=-0.2)))
            self.play(Indicate(VGroup(fA, fB), color=YELLOW, scale_factor=1.05), run_time=1.0)

        # ---------------------------------------------------------- the fix fails by a measured amount
        miss3 = np.where(D["MNAR"]["miss"])[0]
        with self.narrate("Only halfway. Deletion was fifty seven hundred low, and filling from the line "
                          "still leaves twenty eight hundred. Inside each slice, the top is erased, so the "
                          "survivors' line sinks, and every fill lands on the sunken line.") as beat:
            m = D["MNAR"]["cc"]
            self.play(est.animate.set_value(m), err.animate.set_value(m - T), run_time=beat.until("filling", offset=-0.2))
            self.play(Create(surv_line3), run_time=0.8)
            self.play(LaggedStart(*[Transform(self.people[i], self.dot_at(AGE[i], f, GREEN))
                                    for i, f in zip(miss3, D["MNAR"]["fill"])], lag_ratio=0.01),
                      Transform(r_est[0], fill_lab.copy()), r_est[1].animate.set_color(GREEN),
                      est.animate.set_value(D["MNAR"]["imp"]), err.animate.set_value(D["MNAR"]["imp"] - T),
                      run_time=beat.until("Inside", offset=-0.2))
            est_line.set_color(GREEN)
            band.move_to(self.ax.c2p((a0 + a1) / 2 + 20, 45))
            ghosts = VGroup(*[Circle(0.07, color=PURPLE, stroke_width=3).move_to(self.ax.c2p(AGE[i], INC[i]))
                              for i in miss3 if a0 + 20 <= AGE[i] <= a1 + 20])
            self.play(Create(band), run_time=0.7)
            self.play(LaggedStart(*[FadeIn(g, scale=0.5) for g in ghosts], lag_ratio=0.1),
                      run_time=beat.until("sinks", offset=-0.2))
            self.play(Indicate(surv_line3, color=YELLOW, scale_factor=1.0), run_time=1.0)
            beat.wait_until("every fill", offset=-0.2)
            fills3 = VGroup(*[self.people[i] for i in miss3])
            self.play(Indicate(fills3, color=GREEN, scale_factor=1.3), run_time=1.2)

        neq = formula(r"\neq", size=38).move_to(fB[0])
        mnar_txt = text("missing not at random", size=LABEL, color=INK).move_to(mar_txt)
        with self.narrate("The chance of a blank now depends on income, the very number that is missing.") as beat:
            self.play(FadeOut(band), FadeOut(ghosts), Transform(fB[0], neq), run_time=beat.until("income", offset=-0.2))
            self.play(Indicate(fA[5], color=BLUE, scale_factor=1.25), Transform(mar_txt, mnar_txt), run_time=1.0)
            self.play(Indicate(VGroup(*f3[18:]), color=PURPLE, scale_factor=1.0), run_time=beat.remaining())

        # ---------------------------------------------------------- honest limit: MAR twin
        cite_m = citation("Molenberghs et al., 2008 · JRSS B")
        fillB = [self.dot_at(AGE[i], f + 14, GREEN) for i, f in zip(miss3, D["MNAR"]["fill"])]
        fillA = [self.dot_at(AGE[i], f, GREEN) for i, f in zip(miss3, D["MNAR"]["fill"])]
        frozen = VGroup(*[self.people[i] for i in range(N) if not D["MNAR"]["miss"][i]])
        tw_a = text("if at random", size=LABEL, color=GREEN)
        tw_b = text("if high earners skip", size=LABEL, color=GREEN)
        for t in (tw_a, tw_b):
            t.move_to([(self.PX0 + self.PX1) / 2, -3.0 + t.height / 2 + 0.1, 0])
        with self.narrate("And the remaining dots can't warn you. Molenberghs and colleagues proved that "
                          "every not-at-random model has an at-random twin that fits the observed data just "
                          "as well. Only outside information can tell them apart.") as beat:
            self.play(FadeOut(surv_line3), FadeOut(true_reg), run_time=beat.until("Molenberghs", offset=-0.2))
            self.play(FadeIn(cite_m), FadeIn(tw_b), *[Transform(self.people[i], t) for i, t in zip(miss3, fillB)],
                      run_time=1.5)
            beat.wait_until("twin", offset=-0.2)
            self.play(Transform(tw_b, tw_a), *[Transform(self.people[i], t) for i, t in zip(miss3, fillA)],
                      run_time=1.5)
            beat.wait_until("observed", offset=-0.2)
            self.play(Indicate(frozen, color=BLUE, scale_factor=1.12), run_time=1.4)
            self.play(Transform(tw_b, text("if high earners skip", size=LABEL, color=GREEN).move_to(tw_b)),
                      *[Transform(self.people[i], t.copy()) for i, t in zip(miss3, fillB)],
                      run_time=beat.until("outside", offset=-0.1))

        # ---------------------------------------------------------- payoff: real nonresponse U
        bx = axes((-0.7, 14.7), (0, 35), x_ticks=[], y_ticks=[0, 10, 20, 30], x_length=9.4, y_length=4.4,
                  y_label="earnings left unreported (%)")
        bx.move_to([0.2, 0.05, 0])
        bars = VGroup(*[Rectangle(width=0.62 * bx.x_axis.unit_size, height=v * bx.y_axis.unit_size,
                                  stroke_width=0, fill_color=PURPLE, fill_opacity=0.9)
                        .move_to(bx.c2p(k, 0), aligned_edge=DOWN) for k, v in enumerate(TAILS)])
        lab_bot = text("bottom 10%", size=LABEL, color=GRAY).next_to(bx.c2p(0, 0), DOWN, buff=0.25)
        lab_mid = text("middle", size=LABEL, color=GRAY).next_to(bx.c2p(4, 0), DOWN, buff=0.25)
        lab_top = text("top 1%", size=LABEL, color=GRAY).next_to(bx.c2p(14, 0), DOWN, buff=0.25)
        brace = Brace(VGroup(*bars[9:]), DOWN, buff=0.12, color=DIM)
        lab_fine = text("top tenth, by percentile", size=SMALL, color=GRAY).next_to(brace, DOWN, buff=0.1)
        lab_fine.align_to(lab_top, RIGHT).shift(DOWN * 0.45)
        xt = text("men, ranked by Social Security earnings records", size=LABEL, color=GRAY)
        xt.next_to(bx.c2p(7, 0), DOWN, buff=1.05)
        v_bot = formula(r"27\%", size=MATH_SMALL, color=PURPLE).next_to(bars[0], UP, buff=0.12)
        v_mid = formula(r"19\%", size=MATH_SMALL, color=PURPLE).next_to(bars[4], UP, buff=0.12)
        v_top = formula(r"32\%", size=MATH_SMALL, color=PURPLE).next_to(bars[14], UP, buff=0.12)
        cite_b2 = citation("Bollinger et al., 2019 · J. Political Economy")
        with self.narrate("Bollinger and colleagues had that outside information: Social Security earnings "
                          "records, linked to the survey.") as beat:
            self.fade_out_all(run_time=0.8)
            self.play(Create(bx), FadeIn(cite_b2), run_time=1.0)
            self.play(FadeIn(xt, shift=0.1 * UP), run_time=beat.remaining())
        with self.narrate("Among men, more than a quarter of the bottom tenth left earnings unreported, under "
                          "a fifth through the middle, and nearly a third of the top one percent. In the real "
                          "survey, the eraser works both ends.") as beat:
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.12),
                      run_time=beat.until("quarter", offset=-0.2))
            self.play(FadeIn(lab_bot), FadeIn(v_bot), flag(bars[0], color=YELLOW), run_time=0.8)
            beat.wait_until("fifth", offset=-0.2)
            self.play(FadeIn(lab_mid), FadeIn(v_mid), flag(bars[4], color=YELLOW), run_time=0.8)
            beat.wait_until("third", offset=-0.2)
            self.play(FadeIn(lab_top), FadeIn(v_top), GrowFromCenter(brace), FadeIn(lab_fine),
                      flag(bars[14], color=YELLOW), run_time=0.9)
            beat.wait_until("both ends", offset=-0.2)
            self.play(Indicate(VGroup(bars[0], bars[1]), color=YELLOW, scale_factor=1.05),
                      Indicate(VGroup(bars[13], bars[14]), color=YELLOW, scale_factor=1.05), run_time=1.0)

        # ---------------------------------------------------------- landing: the first frame, re-seen
        for i in range(N):
            if D["MNAR"]["miss"][i]:
                self.people[i].become(self.tick_at(AGE[i]))
        r_est[0].become(text("answers only", size=LABEL, color=BLUE).move_to(r_est[0], aligned_edge=LEFT))
        r_est[1].set_color(BLUE)
        est.set_value(D["MNAR"]["cc"])
        err.set_value(D["MNAR"]["cc"] - T)
        est_line.set_color(BLUE)
        with self.narrate("Back to our first survey. The two hundred and ten answers were never wrong. "
                          "The bias was in why the other ninety left.") as beat:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)
            self.play(FadeIn(ax), FadeIn(sim), FadeIn(self.people), FadeIn(panel), FadeIn(est_line),
                      FadeIn(true_line), FadeIn(gap), run_time=beat.until("two hundred", offset=-0.3))
            self.play(Indicate(frozen, color=BLUE, scale_factor=1.12), run_time=1.2)
            beat.wait_until("why", offset=-0.3)
            self.play(LaggedStart(*[Transform(self.people[i], Circle(0.07, color=PURPLE, stroke_width=3)
                                              .move_to(self.ax.c2p(AGE[i], INC[i]))) for i in miss3],
                                  lag_ratio=0.015), run_time=beat.remaining() + 0.6)
        self.hold(0.6)
        self.end_card()
