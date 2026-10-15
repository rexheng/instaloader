"""Episode 53 - What Happens the Night You Turn 21 (regression discontinuity).

    videos/toolkit/render.sh --preview videos/episodes/053-regression-discontinuity/scene.py Episode /tmp/ep53.mp4
"""
from pathlib import Path

import numpy as np
from manim import *
from sample_space import *

HERE = Path(__file__).resolve().parent
_D = np.genfromtxt(HERE / "mlda_mva.csv", delimiter=",", names=True)
AGE = _D["agecell"]                 # 48 cells of 30 days, ages 19-23
MVA = _D["mva"]                     # motor-vehicle deaths per 100,000 person-years
CELL = 30 / 365
LEFT_I = np.where(AGE < 21)[0]
RIGHT_I = np.where(AGE >= 21)[0]


def rd_fit(c: float, k: int):
    """Local linear fit with k cells on each side of cutoff c (separate slopes).
    Returns (yL(c), slopeL, yR(c), slopeR, x_lo, x_hi)."""
    L = np.where(AGE < c)[0][-k:]
    R = np.where(AGE >= c)[0][:k]
    mL, bL = np.polyfit(AGE[L] - c, MVA[L], 1)
    mR, bR = np.polyfit(AGE[R] - c, MVA[R], 1)
    return bL, mL, bR, mR, AGE[L][0], AGE[R][-1]


class Episode(NarratedScene):
    EPISODE = 53
    TITLE = "What Happens the Night You Turn 21"
    PRONUNCIATIONS = {"Dobkin": "dob kin"}

    def construct(self):
        # ------------------------------------------------------------- numbers
        mean_l, mean_r = MVA[LEFT_I].mean(), MVA[RIGHT_I].mean()          # 32.46, 30.78
        naive_pct = 100 * (mean_r - mean_l) / mean_l                        # -5.2
        yL, mL, yR, mR, _, _ = rd_fit(21.0, 24)                             # 29.93, 34.46
        tau = yR - yL                                                       # 4.53
        tau_pct = 100 * tau / yL                                            # 15.1

        # ------------------------------------------------------------- axes
        ax = axes((18.8, 23.2), (22, 40), x_ticks=[19, 20, 21, 22, 23], y_ticks=[25, 30, 35, 40],
                  x_length=8.6, y_length=5.3, x_label="age (years)",
                  y_label="car crash deaths per 100,000 person-years")
        ax.move_to(LEFT * 1.75 + DOWN * 0.15)
        P = ax.c2p
        dots_all = VGroup(*[Dot(P(a, v), radius=0.065, color=BLUE) for a, v in zip(AGE, MVA)])
        dL = VGroup(*[dots_all[i] for i in LEFT_I])
        dR = VGroup(*[dots_all[i] for i in RIGHT_I])
        src = citation("Data: Carpenter & Dobkin, 2009 · AEJ: Applied (via Angrist & Pischke, 2015)")
        cut = DashedLine(P(21, 22), P(21, 40), color=YELLOW, stroke_width=3, dash_length=0.12)

        # 1 ------------------------------------------------------------ cold open
        self.add(ax)
        with self.narrate("Car crash deaths among young Americans, by age. "
                          "Each dot is thirty days of age.") as beat:
            self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in dL], lag_ratio=0.5),
                      run_time=beat.until("Each"), rate_func=LINEAR)
            self.play(FadeIn(src), flag(dL[-1], color=BLUE), run_time=1.0)

        # 2 ------------------------------------------------------------ prediction
        o = P(21.06, MVA[LEFT_I[-1]])
        fan = VGroup(*[Arrow(o, P(22.35, v), buff=0.12, color=GRAY, stroke_width=4,
                             max_tip_length_to_length_ratio=0.12) for v in (35.6, MVA[LEFT_I[-1]], 25.2)])
        fan_lbl = VGroup(*[label(s, color=GRAY).next_to(a.get_end(), RIGHT, buff=0.15)
                           for s, a in zip(("up", "flat", "down"), fan)])
        legal = label("drinking legal", color=YELLOW).next_to(P(21, 40), UP, buff=0.12)
        with self.narrate("At twenty one, drinking becomes legal. Past this line, do the dots go up, "
                          "stay flat, or go down? [pause 1.5]") as beat:
            self.play(Create(cut), run_time=beat.until("legal", offset=-0.1))
            self.play(FadeIn(legal, shift=0.1 * DOWN), run_time=QUICK)
            for i, w in enumerate(("up", "flat", "down")):
                beat.wait_until(w, offset=-0.15)
                self.play(GrowArrow(fan[i]), FadeIn(fan_lbl[i]), run_time=QUICK)
            # prediction hold: the last left dot pulses once as the question hangs
            self.hold(0.6)
            self.play(Indicate(dL[-1], color=YELLOW, scale_factor=1.6), run_time=1.0)

        # 3 ------------------------------------------------------------ the other side
        with self.narrate("Here is the other side. No one can be assigned to drink for a study, "
                          "so this is the evidence we get.") as beat:
            self.play(FadeOut(fan), FadeOut(fan_lbl), run_time=QUICK)
            self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in dR], lag_ratio=0.5),
                      run_time=beat.until("No one"), rate_func=LINEAR)
            self.play(Indicate(dR[0], color=BLUE, scale_factor=1.6), run_time=1.0)

        # 4 ------------------------------------------------------------ naive averages
        segL = Line(P(19.0, mean_l), P(20.98, mean_l), color=RED, stroke_width=6)
        segR = Line(P(21.02, mean_r), P(23.0, mean_r), color=RED, stroke_width=6)
        with self.narrate("The obvious test: average every dot before twenty one, "
                          "and every dot after.") as beat:
            self.play(dim(dR, opacity=0.35), run_time=beat.until("average", offset=-0.2))
            self.play(Create(segL), run_time=beat.until("and every", offset=-0.1))
            self.play(undim(dR), dim(dL, opacity=0.35), run_time=QUICK)
            self.play(Create(segR), run_time=1.0)
            self.play(undim(dL), run_time=QUICK)

        # 5 ------------------------------------------------------------ scoreboard
        vL = formula(f"{mean_l:.1f}", color=RED, size=MATH).next_to(segL.get_start(), UP, buff=0.15)
        vL.align_to(segL, LEFT).shift(UP * 0.55)
        vR = formula(f"{mean_r:.1f}", color=RED, size=MATH).next_to(P(23.0, mean_r), RIGHT, buff=0.15)
        board_x = 4.85
        row1_lbl = label("averages", color=INK)
        row1_val = formula(r"-5\%", color=RED, size=EQ)
        row1 = VGroup(row1_lbl, row1_val).arrange(DOWN, buff=0.15).move_to([board_x, 2.55, 0])
        with self.narrate("The average drops from thirty two point five to thirty point eight, "
                          "five percent fewer deaths. Taken at face value, legal alcohol made "
                          "young people safer on the road.") as beat:
            self.play(FadeIn(vL, shift=0.1 * UP), run_time=beat.until("to", offset=-0.1))
            self.play(FadeIn(vR, shift=0.1 * LEFT), run_time=beat.until("five", offset=-0.1))
            self.play(FadeIn(row1_lbl), TransformFromCopy(VGroup(vL, vR), row1_val), run_time=1.2)
            beat.wait_until("safer", offset=-0.15)
            self.play(flag(row1_val, color=RED), run_time=0.9)

        # 6 ------------------------------------------------------------ the confounder
        ageL, ageR = AGE[LEFT_I].mean(), AGE[RIGHT_I].mean()
        span = DoubleArrow(P(ageL, 38.6), P(ageR, 38.6), buff=0, color=PURPLE, stroke_width=4,
                           tip_length=0.2)
        tickL = DashedLine(P(ageL, 38.6), P(ageL, mean_l), color=PURPLE, stroke_width=2,
                           dash_length=0.08)
        tickR = DashedLine(P(ageR, 38.6), P(ageR, mean_r), color=PURPLE, stroke_width=2,
                           dash_length=0.08)
        span_lbl = label("2 years older", color=PURPLE).next_to(span, UP, buff=0.12)
        trend = Arrow(P(19.15, 29.3), P(22.9, 25.0), buff=0, color=PURPLE, stroke_width=5,
                      max_tip_length_to_length_ratio=0.06)
        trend_lbl = label("aging", color=PURPLE).next_to(trend.point_from_proportion(0.25), DOWN,
                                                          buff=0.18)
        with self.narrate("The catch is who sits on each side. The people on the right are, on "
                          "average, two years older, and crash deaths fall with age the whole "
                          "way across.") as beat:
            self.play(FadeOut(legal), run_time=QUICK)
            beat.wait_until("two years", offset=-0.3)
            self.play(Create(tickL), Create(tickR), GrowFromCenter(span), FadeIn(span_lbl),
                      run_time=1.2)
            beat.wait_until("fall", offset=-0.2)
            self.play(GrowArrow(trend), FadeIn(trend_lbl), run_time=beat.remaining(1.2))

        # 7 ------------------------------------------------------------ size of the bias
        bias = formula(r"\approx -6", color=PURPLE, size=MATH).next_to(trend_lbl, RIGHT, buff=0.2)
        strike = Line(row1_val.get_corner(DL) + LEFT * 0.08, row1_val.get_corner(UR) + RIGHT * 0.08,
                      color=INK, stroke_width=4)
        with self.narrate("Two years of that decline is worth about six deaths per hundred "
                          "thousand. The averages measured getting older, not drinking.") as beat:
            beat.wait_until("six", offset=-0.3)
            self.play(FadeIn(bias, shift=0.1 * RIGHT), run_time=0.8)
            beat.wait_until("getting older", offset=-0.2)
            self.play(Create(strike), dim(row1_lbl, row1_val), run_time=1.0)

        # 8 ------------------------------------------------------------ shrink the window
        c_t = ValueTracker(21.0)
        h_t = ValueTracker(24 * CELL)      # window half-width in years

        def window():
            c, h = c_t.get_value(), h_t.get_value()
            r = Rectangle(width=max(ax.x_axis.unit_size * 2 * h, 0.02),
                          height=ax.y_axis.unit_size * 18, stroke_color=YELLOW, stroke_width=2,
                          fill_color=YELLOW, fill_opacity=0.07)
            return r.move_to(P(c, 31))
        win = always_redraw(window)

        def shade_dots(m):
            c, h = c_t.get_value(), h_t.get_value()
            for d, a in zip(dots_all, AGE):
                d.set_opacity(1.0 if abs(a - c) <= h + 1e-6 else 0.25)
        naive_stuff = VGroup(segL, segR, vL, vR, span, tickL, tickR, span_lbl, trend, trend_lbl, bias)
        with self.narrate("So shrink the comparison. Someone a month before their twenty first "
                          "birthday and someone a month after are alike in almost every way, "
                          "except the law.") as beat:
            self.play(FadeOut(naive_stuff), run_time=0.8)
            self.add(win)
            dots_all.add_updater(shade_dots)
            self.play(FadeIn(win), run_time=0.5)
            self.play(h_t.animate.set_value(1.05 * CELL), run_time=beat.until("Someone"),
                      rate_func=SMOOTH)
            beat.wait_until("before", offset=-0.1)
            self.play(Indicate(dots_all[LEFT_I[-1]], color=BLUE, scale_factor=1.7), run_time=0.9)
            beat.wait_until("after", offset=-0.1)
            self.play(Indicate(dots_all[RIGHT_I[0]], color=BLUE, scale_factor=1.7), run_time=0.9)
            beat.wait_until("except", offset=-0.1)
            self.play(Indicate(cut, color=YELLOW), run_time=1.0)

        # 9 ------------------------------------------------------------ local lines
        reach = ValueTracker(0.0)          # 0: lines stop short of 21; 1: lines touch 21

        def fit_lines():
            c, h = c_t.get_value(), h_t.get_value()
            k = int(np.clip(round(h / CELL), 4, 24))
            bL, sL, bR, sR, xlo, xhi = rd_fit(c, k)
            gap = (1 - reach.get_value()) * 0.32
            lo = Line(P(xlo, bL + sL * (xlo - c)), P(c - gap, bL - sL * gap), color=GREEN,
                      stroke_width=6)
            hi = Line(P(c + gap, bR + sR * gap), P(xhi, bR + sR * (xhi - c)), color=GREEN,
                      stroke_width=6)
            return VGroup(lo, hi)
        lines0 = fit_lines()
        lines0_static = lines0.copy()
        with self.narrate("But that leaves two noisy dots. So fit a straight line on each side, and "
                          "let each line carry the age trend right up to the birthday.") as beat:
            beat.wait_until("two noisy", offset=-0.1)
            self.play(Indicate(dots_all[LEFT_I[-1]], color=BLUE, scale_factor=1.5),
                      Indicate(dots_all[RIGHT_I[0]], color=BLUE, scale_factor=1.5), run_time=0.9)
            beat.wait_until("fit", offset=-0.2)
            self.play(h_t.animate.set_value(24 * CELL), run_time=1.0, rate_func=SMOOTH)
            lo, hi = lines0_static
            self.play(Create(lo), Create(hi), run_time=beat.until("right up", offset=-0.1))
            self.play(Indicate(VGroup(lo, hi), color=GREEN, scale_factor=1.03), run_time=0.9)

        # 10 ----------------------------------------------------------- the reveal (pause)
        self.remove(lo, hi)
        lines = always_redraw(fit_lines)
        self.add(lines)

        def endpoints():
            c, h = c_t.get_value(), h_t.get_value()
            k = int(np.clip(round(h / CELL), 4, 24))
            bL, _, bR, _, _, _ = rd_fit(c, k)
            gL = Dot(P(c, bL), radius=0.09, color=GREEN)
            gR = Dot(P(c, bR), radius=0.09, color=GREEN)
            g = Line(P(c, bL), P(c, bR), color=YELLOW, stroke_width=9)
            return VGroup(g, gL, gR)
        with self.narrate("Watch where the two lines reach the cutoff. [pause 1.5]") as beat:
            beat.wait_until("reach", offset=0.1)
            self.play(reach.animate.set_value(1.0), run_time=1.4, rate_func=SMOOTH)
            ends = always_redraw(endpoints)
            ends_static = endpoints()
            self.play(GrowFromCenter(ends_static[0]), FadeIn(ends_static[1:], scale=0.5),
                      run_time=1.0)
            self.remove(ends_static)
            self.add(ends)

        # 11 ----------------------------------------------------------- read the gap
        nL = formula(f"{yL:.2f}", color=GREEN).next_to(P(21, yL), DL, buff=0.18).shift(DOWN * 0.35)
        nR = formula(f"{yR:.2f}", color=GREEN).next_to(P(21, 37.6), UP, buff=0.05)
        led_R = formula(f"{yR:.2f}", color=GREEN)
        led_L = formula(f"{yL:.2f}", color=GREEN)
        minus = formula("-")
        eqs = formula("=")
        tau_v = formula(f"{tau:.2f}", color=YELLOW)
        diff = VGroup(led_R, minus, led_L, eqs, tau_v).arrange(RIGHT, buff=0.15)
        diff.move_to([board_x - 0.05, 0.75, 0])
        row2_lbl = label("at the cutoff", color=INK)
        row2_val = formula(rf"+{tau_pct:.0f}\%", color=GREEN, size=EQ)
        row2 = VGroup(row2_lbl, row2_val).arrange(DOWN, buff=0.15).move_to([board_x, -1.0, 0])
        with self.narrate("On the left, just under thirty. On the right, almost thirty four and a "
                          "half. The gap is four and a half more deaths per hundred thousand: "
                          "fifteen percent up, not five percent down.") as beat:
            beat.wait_until("left", offset=-0.2)
            self.play(FadeIn(nL, shift=0.1 * DOWN), run_time=0.7)
            beat.wait_until("right", offset=-0.2)
            self.play(FadeIn(nR, shift=0.1 * UP), run_time=0.7)
            beat.wait_until("gap", offset=-0.4)
            self.play(TransformFromCopy(nR, led_R), TransformFromCopy(nL, led_L), FadeIn(minus),
                      run_time=1.2)
            self.play(FadeIn(eqs), TransformFromCopy(ends[0], tau_v), run_time=1.0)
            beat.wait_until("fifteen", offset=-0.3)
            self.play(FadeIn(row2_lbl), TransformFromCopy(tau_v, row2_val), run_time=1.0)
            beat.wait_until("not five", offset=-0.1)
            self.play(flag(row1_val, color=RED), run_time=0.8)

        # 12 ----------------------------------------------------------- name + symbol form
        sym = formula(r"\hat y(21^{+})", "-", r"\hat y(21^{-})", "=", r"\tau")
        sym[0].set_color(GREEN)
        sym[2].set_color(GREEN)
        sym[4].set_color(YELLOW)
        sym.move_to(diff)
        fit(sym, width=3.0)
        name = label("regression discontinuity", color=INK)
        name.next_to(sym, UP, buff=0.35)
        keep_in_safe(name)
        with self.narrate("That gap is the estimate. The method is called regression "
                          "discontinuity: the jump in the fitted lines, right at the cutoff.") as beat:
            self.play(Indicate(ends[0], color=YELLOW, scale_factor=1.05), run_time=0.9)
            beat.wait_until("regression", offset=-0.2)
            self.play(FadeIn(name, shift=0.1 * DOWN), run_time=0.8)
            beat.wait_until("jump", offset=-0.2)
            self.play(ReplacementTransform(led_R, sym[0]), ReplacementTransform(minus, sym[1]),
                      ReplacementTransform(led_L, sym[2]), ReplacementTransform(eqs, sym[3]),
                      ReplacementTransform(tau_v, sym[4]), run_time=1.5)

        # 13 ----------------------------------------------------------- robustness: bandwidth
        self.play(FadeOut(nL), FadeOut(nR), FadeOut(name), run_time=QUICK)
        tau_live = live_number(ValueTracker(tau), decimals=2, color=YELLOW, prefix=r"\tau =")
        tau_live.move_to(sym)

        def cur_tau():
            c, h = c_t.get_value(), h_t.get_value()
            k = int(np.clip(round(h / CELL), 4, 24))
            bL, _, bR, _, _, _ = rd_fit(c, k)
            return bR - bL
        tau_live.number.clear_updaters()
        tau_live.number.add_updater(lambda m: m.set_value(cur_tau()))
        win_live = live_number(h_t, decimals=1, size=MATH, color=YELLOW,
                               prefix=r"\text{window} \pm", suffix=r"\text{yr}")
        win_live.number.clear_updaters()
        win_pre, win_suf = win_live[0], win_live[2]
        win_live.number.add_updater(lambda m: m.set_value(h_t.get_value())
                                    .next_to(win_pre, RIGHT, buff=0.15))
        win_live.next_to(tau_live, DOWN, buff=0.35)
        win_suf.add_updater(lambda m: m.next_to(win_live.number, RIGHT, buff=0.15))
        with self.narrate("Narrow the window from two years to six months, and the gap stays "
                          "between four and six.") as beat:
            self.play(ReplacementTransform(sym, tau_live), FadeIn(win_live), run_time=1.0)
            beat.wait_until("six months", offset=-0.6)
            self.play(h_t.animate.set_value(6 * CELL), run_time=2.6, rate_func=SMOOTH)
            self.play(h_t.animate.set_value(12 * CELL), run_time=beat.remaining(1.0),
                      rate_func=SMOOTH)

        # 14 ----------------------------------------------------------- placebo cutoffs
        cut_lbl = formula(r"\text{cutoff}", color=YELLOW, size=MATH_SMALL + 6)
        cut_lbl.add_updater(lambda m: m.next_to(P(c_t.get_value(), 40), UP, buff=0.1))
        cut.add_updater(lambda m: m.put_start_and_end_on(P(c_t.get_value(), 22),
                                                         P(c_t.get_value(), 40)))
        with self.narrate("Slide the cutoff to twenty, or to twenty two, birthdays where no law "
                          "changes, and the gap falls below one.") as beat:
            self.play(FadeIn(cut_lbl), run_time=QUICK)
            self.play(c_t.animate.set_value(20.0), run_time=beat.until("or to", offset=-0.1),
                      rate_func=SMOOTH)
            self.play(c_t.animate.set_value(22.0), run_time=beat.until("birthdays", offset=0.4),
                      rate_func=SMOOTH)
            beat.wait_until("falls", offset=-0.3)
            self.play(flag(tau_live, color=YELLOW), run_time=0.9)
            self.play(c_t.animate.set_value(21.0), run_time=beat.remaining(1.0), rate_func=SMOOTH)
        for m in (cut, cut_lbl, dots_all, tau_live.number, win_live.number, win_suf):
            m.clear_updaters()

        # 15 ----------------------------------------------------------- payoff
        plot = VGroup(ax, dots_all, win, lines, ends, cut, cut_lbl)
        win.clear_updaters()
        lines.clear_updaters()
        ends.clear_updaters()
        cites = citation("Carpenter & Dobkin, 2009 · American Economic Journal: Applied")
        bars_ax_x0 = 0.9
        unit = 4.9 / 35.0
        rows = [("car crashes", 15), ("deaths mentioning alcohol", 35), ("all causes", 9)]
        bars, names, vals = VGroup(), VGroup(), VGroup()
        for i, (nm, v) in enumerate(rows):
            y = 1.7 - 1.45 * i
            b = Rectangle(width=v * unit, height=0.42, stroke_width=0, fill_color=GREEN,
                          fill_opacity=0.85)
            b.move_to([bars_ax_x0 + v * unit / 2, y, 0])
            n = label(nm, color=INK).next_to(b, UP, buff=0.12).align_to(b, LEFT)
            t = formula(rf"+{v}\%", color=GREEN).next_to(b, RIGHT, buff=0.15)
            bars.add(b)
            names.add(n)
            vals.add(t)
        heading = label("jump at 21", color=GRAY).move_to([bars_ax_x0 + 1.0, 3.25, 0]).align_to(
            names, LEFT)
        base = Line([bars_ax_x0, 2.55, 0], [bars_ax_x0, -1.85, 0], color=GRAY, stroke_width=2)
        with self.narrate("Carpenter and Dobkin ran this on American death certificates. At twenty "
                          "one, car crash deaths jump about fifteen percent, deaths that mention "
                          "alcohol about thirty five, and deaths from every cause about nine.") as beat:
            self.play(FadeOut(tau_live), FadeOut(win_live), FadeOut(row1), FadeOut(strike),
                      FadeOut(src), FadeOut(cut_lbl), run_time=QUICK)
            self.play(plot.animate.scale(0.52).to_edge(LEFT, buff=0.35).shift(DOWN * 0.2),
                      FadeIn(cites), run_time=1.2)
            self.play(Create(base), FadeIn(heading), run_time=0.6)
            beat.wait_until("car crash", offset=-0.2)
            self.play(FadeIn(names[0]), GrowFromEdge(bars[0], LEFT),
                      ReplacementTransform(row2_val, vals[0]), FadeOut(row2_lbl), run_time=1.2)
            beat.wait_until("alcohol", offset=-0.3)
            self.play(FadeIn(names[1]), GrowFromEdge(bars[1], LEFT), FadeIn(vals[1]), run_time=1.1)
            beat.wait_until("every cause", offset=-0.3)
            self.play(FadeIn(names[2]), GrowFromEdge(bars[2], LEFT), FadeIn(vals[2]), run_time=1.1)

        # 16 ----------------------------------------------------------- the limit
        payoff = VGroup(bars, names, vals, heading, base)
        rng = np.random.default_rng(7)
        nb = 16

        def hist(heights, x0, color_fn):
            w = 0.27
            g = VGroup()
            for i, hgt in enumerate(heights):
                r = Rectangle(width=w * 0.86, height=max(hgt, 0.02), stroke_width=0,
                              fill_color=color_fn(i), fill_opacity=0.9)
                r.move_to([x0 + w * i + w / 2, -1.6 + hgt / 2, 0])
                g.add(r)
            return g
        flat = 0.9 + 0.08 * rng.standard_normal(nb)
        bunch = 0.9 + 0.08 * rng.standard_normal(nb)
        bunch[6:8] = [0.35, 0.2]
        bunch[8:10] = [1.85, 1.45]
        hA = hist(flat, -5.9, lambda i: GRAY)
        hB = hist(bunch, 0.75, lambda i: RED if i in (6, 7, 8, 9) else GRAY)
        cA = DashedLine([-5.9 + 0.27 * 8, -1.75, 0], [-5.9 + 0.27 * 8, 0.75, 0], color=YELLOW,
                        stroke_width=3, dash_length=0.1)
        cB = DashedLine([0.75 + 0.27 * 8, -1.75, 0], [0.75 + 0.27 * 8, 0.75, 0], color=YELLOW,
                        stroke_width=3, dash_length=0.1)
        baseA = Line([-5.95, -1.6, 0], [-5.9 + 0.27 * nb + 0.05, -1.6, 0], color=GRAY, stroke_width=2)
        baseB = Line([0.7, -1.6, 0], [0.75 + 0.27 * nb + 0.05, -1.6, 0], color=GRAY, stroke_width=2)
        tA = label("people, by birthday", color=INK).next_to(hA, DOWN, buff=0.35)
        tA2 = label("cutoff: 21st birthday", color=YELLOW, size=26).next_to(cA, UP, buff=0.12)
        tB = label("people, by test score", color=INK).next_to(hB, DOWN, buff=0.35)
        tB2 = label("cutoff: pass mark", color=YELLOW, size=26).next_to(cB, UP, buff=0.12)
        sim = label("simulated", color=GRAY, size=SMALL).next_to(tB, DOWN, buff=0.12)
        pile = label("retakers pile up", color=RED, size=26).next_to(hB[8], RIGHT, buff=0.15)
        pile.shift(UP * 0.55)
        tA.align_to(hA, LEFT)
        tB.align_to(hB, LEFT)
        sim.align_to(tB, LEFT)
        histA = VGroup(baseA, hA, cA, tA, tA2)
        histB = VGroup(baseB, hB, cB, tB, tB2, sim)
        scope = label("measured at 21, not at 40", color=GREEN).move_to([0, 2.6, 0])
        with self.narrate("It works because no one chooses their birthday, so people spread evenly "
                          "across the line. Put the cutoff on a test score, and people who just miss "
                          "can retake it and pile up above it. Then the two sides stop being alike. "
                          "And the jump describes people turning twenty one, not drinkers at forty."
                          ) as beat:
            self.play(FadeOut(payoff), FadeOut(cites), plot.animate.set_opacity(0.0), run_time=0.8)
            self.remove(plot)
            self.play(Create(baseA), LaggedStart(*[GrowFromEdge(r, DOWN) for r in hA], lag_ratio=0.06),
                      FadeIn(tA), run_time=1.3)
            beat.wait_until("across", offset=-0.3)
            self.play(Create(cA), FadeIn(tA2), run_time=0.8)
            beat.wait_until("test score", offset=-0.2)
            self.play(Create(baseB), LaggedStart(*[GrowFromEdge(r, DOWN) for r in hB], lag_ratio=0.06),
                      FadeIn(tB), FadeIn(sim), Create(cB), FadeIn(tB2), run_time=1.4)
            beat.wait_until("pile", offset=-0.2)
            self.play(FadeIn(pile, shift=0.1 * LEFT), flag(VGroup(*hB[8:10]), color=RED),
                      run_time=1.0)
            beat.wait_until("stop", offset=-0.2)
            self.play(Indicate(VGroup(*hB[6:10]), color=RED, scale_factor=1.06), run_time=1.0)
            beat.wait_until("And the jump", offset=-0.2)
            self.play(dim(histA, histB, pile), FadeIn(scope, shift=0.1 * DOWN), run_time=1.0)

        # 17 ----------------------------------------------------------- landing
        self.play(FadeOut(histA), FadeOut(histB), FadeOut(pile), FadeOut(scope), run_time=0.6)
        ax_l = axes((18.8, 23.2), (22, 40), x_ticks=[19, 20, 21, 22, 23], y_ticks=[25, 30, 35, 40],
                    x_length=8.6, y_length=5.3, x_label="age (years)",
                    y_label="car crash deaths per 100,000 person-years")
        ax_l.move_to(LEFT * 1.75 + DOWN * 0.15)
        P2 = ax_l.c2p
        dots_l = VGroup(*[Dot(P2(a, v), radius=0.065, color=BLUE) for a, v in zip(AGE, MVA)])
        cut_l = DashedLine(P2(21, 22), P2(21, 40), color=YELLOW, stroke_width=3, dash_length=0.12)
        land = VGroup(ax_l, cut_l, dots_l)
        up = Arrow(P2(21.0, yL), P2(21.0, yR), buff=0, color=YELLOW, stroke_width=7,
                   max_tip_length_to_length_ratio=0.3)
        up_lbl = label("up 15%", color=YELLOW).next_to(P2(21.0, 37.8), LEFT, buff=0.15)
        down = Arrow(P2(21.2, yR + 2.4), P2(22.95, yR + mR * 1.95 + 2.4), buff=0, color=PURPLE,
                     stroke_width=6, max_tip_length_to_length_ratio=0.08)
        down_lbl = label("then down", color=PURPLE).next_to(down.get_center(), UR, buff=0.12)
        with self.narrate("So, past the line, the dots go up, and then down. Crash deaths jump the "
                          "night drinking becomes legal, then keep falling with age. The average "
                          "only saw the fall.") as beat:
            self.play(FadeIn(land), run_time=0.9)
            beat.wait_until("go up", offset=-0.15)
            self.play(GrowArrow(up), FadeIn(up_lbl), run_time=0.8)
            beat.wait_until("then down", offset=-0.15)
            self.play(GrowArrow(down), FadeIn(down_lbl), run_time=0.9)
            beat.wait_until("average", offset=-0.2)
            segs = VGroup(Line(P2(19.0, mean_l), P2(20.98, mean_l)),
                          Line(P2(21.02, mean_r), P2(23.0, mean_r))).set_stroke(RED, 6)
            self.play(Create(segs), dim(up, up_lbl), run_time=1.0)
        self.end_card()
