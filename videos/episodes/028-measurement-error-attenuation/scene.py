"""Episode 28 - Noisy Data Makes Real Effects Look Smaller (measurement error attenuation).

    videos/toolkit/render.sh videos/episodes/028-measurement-error-attenuation/scene.py Episode \
        videos/episodes/028-measurement-error-attenuation/final.mp4
"""
import numpy as np
from manim import *
from sample_space import *

# ----------------------------------------------------------------------------- data
# Simulated: true diastolic pressure T ~ N(80, 8^2); cuff error E ~ N(0, 6^2);
# stroke risk (%) = 5 + 0.1 (T - 80) + U.  Slopes are reported per 10 mmHg.
_rng = np.random.default_rng(79)
N = 200
T = 80 + 8 * _rng.standard_normal(N)
E = 6 * _rng.standard_normal(N)
E2 = 6 * _rng.standard_normal(N)
U = 0.6 * _rng.standard_normal(N)
Y = 5 + 0.1 * (T - 80) + U
VN = E / 5.0                       # same-sized noise moved onto the risk axis
X1, X2 = T + E, T + E2
COL = (X1 > 92) & (X1 < 98)        # the "reading about 95" column (19 patients)
R12 = float(np.corrcoef(X1, X2)[0, 1])


def fit(xs, ys):
    b = np.cov(xs, ys)[0, 1] / np.var(xs, ddof=1)
    return b, ys.mean() - b * xs.mean()


B_TRUE, A_TRUE = fit(T, Y)
B_OBS, A_OBS = fit(X1, Y)
X_LO, X_HI = 44, 116


class Episode(NarratedScene):
    EPISODE = 28
    TITLE = "Noisy Data Makes Real Effects Look Smaller"
    PRONUNCIATIONS = {"MacMahon": "mak MAA hun"}

    def construct(self):
        # ------------------------------------------------------------ persistent plot
        ax = axes((40, 120), (0, 12), x_ticks=[40, 60, 80, 100, 120], y_ticks=[0, 4, 8, 12],
                  x_length=6.4, y_length=4.2)
        ax.move_to([-2.55, 0.35, 0])
        p = ax.c2p
        x_true = label("true blood pressure (mmHg)", color=GRAY)
        x_meas = label("measured blood pressure (mmHg)", color=GRAY)
        for t in (x_true, x_meas):
            t.next_to(ax.x_axis.numbers, DOWN, buff=0.18).align_to(ax.x_axis.get_right(), RIGHT)
        y_title = label("stroke risk (%)", color=GRAY)
        y_title.next_to(ax.y_axis.get_top(), UP, buff=0.22).align_to(ax.y_axis.numbers, LEFT)
        sim_tag = label("simulated · 200 patients", size=SMALL, color=GRAY)
        sim_tag.move_to(p(119, 0.9), aligned_edge=RIGHT)

        s = ValueTracker(0.0)      # horizontal (pressure) error scale: reading = T + s E
        v = ValueTracker(0.0)      # vertical (risk) error scale
        c = ValueTracker(0.0)      # column patients slide back to their true pressure
        k = ValueTracker(0.0)      # correction progress for the green line

        def xs_now():
            return T + s.get_value() * E

        def ys_now():
            return Y + v.get_value() * VN

        def slope_now():
            return fit(xs_now(), ys_now())[0]

        pts = VGroup(*[Dot(p(x, y), radius=0.055, color=BLUE, fill_opacity=0.85)
                       for x, y in zip(T, Y)])

        def upd_pts(g):
            xs = xs_now() - c.get_value() * s.get_value() * E * COL
            ys = ys_now()
            for d, x, y in zip(g, xs, ys):
                d.move_to(p(x, y))
        pts.add_updater(upd_pts)

        def make_line():
            b, a = fit(xs_now(), ys_now())
            return Line(p(X_LO, a + b * X_LO), p(X_HI, a + b * X_HI), color=YELLOW, stroke_width=5)
        fit_line = always_redraw(make_line)

        readout_lbl = formula(r"\text{slope} =", size=MATH)
        readout_num = DecimalNumber(10 * B_TRUE, num_decimal_places=2, font_size=MATH, color=YELLOW)
        readout_lbl.move_to(p(42, 11.3), aligned_edge=LEFT)
        readout_num.next_to(readout_lbl, RIGHT, buff=0.15)
        readout_num.add_updater(lambda m: m.set_value(10 * slope_now()))
        units = label("% risk per 10 mmHg", size=SMALL, color=GRAY)
        units.next_to(readout_lbl, DOWN, buff=0.15, aligned_edge=LEFT)

        # =========================================================== 0 · cold open
        self.add(ax, x_true, y_title, pts, sim_tag)
        cx, cy = float(T.mean()), float(Y.mean())

        def cand(slope, x0, x1):
            return DashedLine(p(x0, cy + slope * (x0 - cx)), p(x1, cy + slope * (x1 - cx)),
                              color=GRAY, stroke_width=3, dash_length=0.12)
        steep = cand(0.17, 63, 97)
        flat = cand(0.045, X_LO, X_HI)
        lab_steep = label("steeper").next_to(steep.get_end(), UP, buff=0.15)
        lab_flat = label("flatter").next_to(flat.get_end(), RIGHT, buff=0.15)
        idx = [int(np.argmin(np.abs(T - t0) + 3 * np.abs(Y - (5 + 0.1 * (t0 - 80)))))
               for t0 in (66, 74, 82, 90, 97)]
        arrows = VGroup(*[DoubleArrow(p(T[i] - 6, Y[i]), p(T[i] + 6, Y[i]), buff=0, color=RED,
                                      stroke_width=3, tip_length=0.12, max_tip_length_to_length_ratio=0.3)
                          for i in idx])
        with self.narrate("This line links blood pressure to stroke risk for two hundred patients. "
                          "Now make every reading off by a random amount, high as often as low. "
                          "Does the line get steeper, flatter, or stay the same? [pause 1.5]") as beat:
            self.play(Create(fit_line), run_time=beat.until("stroke"))
            self.add(fit_line)
            self.play(FadeIn(readout_lbl), FadeIn(readout_num), FadeIn(units),
                      run_time=beat.until("random", offset=-0.2))
            self.play(LaggedStart(*[GrowFromCenter(a) for a in arrows], lag_ratio=0.15),
                      run_time=beat.until("high"))
            self.play(*[a.animate.shift(p(84, 0) - p(80, 0)) for a in arrows], run_time=0.5,
                      rate_func=there_and_back)
            self.play(*[a.animate.shift(p(76, 0) - p(80, 0)) for a in arrows],
                      run_time=beat.until("steeper", offset=-0.1), rate_func=there_and_back)
            self.play(Create(steep), FadeIn(lab_steep), run_time=beat.until("flatter", offset=-0.1))
            self.play(Create(flat), FadeIn(lab_flat), run_time=beat.until("same", offset=-0.1))
            lab_same = label("same").next_to(p(X_HI, A_TRUE + B_TRUE * X_HI), RIGHT, buff=0.15)
            self.play(FadeIn(lab_same), run_time=0.6)

        # =========================================================== 1 · stakes
        hax = axes((-21, 21), (0, 60), x_ticks=[-20, 0, 20], y_ticks=[0, 30, 60], x_length=4.0,
                   y_length=2.4, x_label="cuff error (mmHg)", y_label="patients")
        hax.move_to([4.1, -0.2, 0])
        counts, edges = np.histogram(E, bins=np.arange(-20, 21, 4))
        hbars = VGroup(*[Rectangle(width=(hax.c2p(4, 0) - hax.c2p(0, 0))[0] * 0.92,
                                   height=max(1e-3, (hax.c2p(0, n) - hax.c2p(0, 0))[1]),
                                   stroke_width=0, fill_color=RED, fill_opacity=0.85)
                         .move_to(hax.c2p(e + 2, 0), aligned_edge=DOWN)
                         for n, e in zip(counts, edges[:-1])])
        mean_ln = DashedLine(hax.c2p(E.mean(), 0), hax.c2p(E.mean(), 62), color=INK, stroke_width=2.5)
        mean_lbl = formula(r"\text{average} \approx 0", size=MATH_SMALL + 6).next_to(mean_ln, UP, buff=0.15)
        with self.narrate("Most people pick the same. The errors cancel out on average, "
                          "so the trend should survive.") as beat:
            self.play(flag(lab_same, color=INK), run_time=0.8)
            self.play(FadeOut(VGroup(steep, flat, lab_steep, lab_flat)), run_time=beat.until("errors"))
            self.play(Create(hax), run_time=0.6)
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in hbars], lag_ratio=0.08),
                      run_time=beat.until("average", offset=-0.2))
            self.play(Create(mean_ln), FadeIn(mean_lbl), run_time=0.7)
            self.play(FadeOut(arrows), FadeOut(lab_same), run_time=beat.remaining(0.5))

        # =========================================================== 2 · the two spreads
        def bracket(x0, x1, y, color, axes_):
            a, b = axes_.c2p(x0, y), axes_.c2p(x1, y)
            tk = 0.1 * UP
            return VGroup(Line(a, b), Line(a - tk, a + tk), Line(b - tk, b + tk)).set_stroke(color, 4)
        bT = bracket(72, 88, 9.8, BLUE, ax)
        bT_lbl = formula(r"\sigma_T = 8", color=BLUE).next_to(bT, UP, buff=0.15)
        bE = bracket(-6, 6, 50, RED, hax)
        bE.shift(UP * ((hax.c2p(0, 58) - hax.c2p(0, 50))[1]))
        bE_lbl = formula(r"\sigma_E = 6", color=RED).next_to(bE, RIGHT, buff=0.2)
        with self.narrate("Let's test it. True pressures here spread about eight points either "
                          "side of eighty. The cuff adds an error that spreads about six.") as beat:
            beat.wait_until("spread", offset=-0.2)
            self.play(GrowFromCenter(bT), run_time=0.8)
            self.play(Write(bT_lbl), run_time=beat.until("cuff", offset=-0.1))
            beat.wait_until("spreads", offset=-0.2)
            self.play(GrowFromCenter(bE), run_time=0.8)
            self.play(Write(bE_lbl), run_time=0.7)

        # =========================================================== 3 · switch the error on
        truth = DashedLine(p(X_LO, A_TRUE + B_TRUE * X_LO), p(X_HI, A_TRUE + B_TRUE * X_HI),
                           color=BLUE, stroke_width=3.5, dash_length=0.14)
        with self.narrate("Switch the error on, and refit the line through the readings "
                          "we would actually record.") as beat:
            self.add(truth)
            self.bring_to_front(fit_line)
            self.play(s.animate.set_value(1.0), run_time=beat.until("readings"), rate_func=SMOOTH)
            self.play(ReplacementTransform(x_true, x_meas), run_time=0.8)
            self.play(flag(fit_line, color=YELLOW), run_time=beat.remaining(0.6))

        # =========================================================== 4 · fail
        drop = formula(r"-37\%", color=RED).next_to(readout_num, RIGHT, buff=0.3)
        with self.narrate("The slope falls from one to point six four. More than a third of the "
                          "effect is gone, and no patient changed.") as beat:
            beat.wait_until("point", offset=-0.2)
            self.play(flag(readout_num), run_time=0.8)
            self.play(FadeIn(drop, shift=0.1 * DOWN), run_time=beat.until("third"))
            self.play(Indicate(truth, color=BLUE, scale_factor=1.0), run_time=beat.until("no patient"))
            self.play(flag(pts, color=BLUE), run_time=beat.remaining(0.6))

        # =========================================================== 5 · contrast: noise in y
        tag_y = label("error in risk:  line holds").set_color_by_t2c({"error in risk": RED})
        tag_x = label("error in pressure:  line flattens").set_color_by_t2c({"error in pressure": RED})
        tags = VGroup(tag_y, tag_x).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to([3.85, 0.2, 0])
        with self.narrate("Now move the same kind of noise onto the risk instead. The cloud "
                          "thickens, but the slope stays near one. Noise in the outcome blurs. "
                          "Noise in the predictor flattens.") as beat:
            self.play(FadeOut(VGroup(hax, hbars, mean_ln, mean_lbl, bE, bE_lbl)), FadeOut(drop),
                      run_time=0.6)
            self.play(s.animate.set_value(0.0), v.animate.set_value(1.0),
                      run_time=beat.until("thickens"), rate_func=SMOOTH)
            beat.wait_until("near", offset=-0.2)
            self.play(flag(readout_num), run_time=0.8)
            self.play(FadeIn(tag_y, shift=0.1 * RIGHT), run_time=beat.until("predictor", offset=-0.3))
            self.play(s.animate.set_value(1.0), v.animate.set_value(0.0), FadeIn(tag_x, shift=0.1 * RIGHT),
                      run_time=beat.remaining(1.2), rate_func=SMOOTH)

        # =========================================================== 6 · why: one column
        band = Rectangle(width=(p(98, 0) - p(92, 0))[0], height=(p(0, 12) - p(0, 0))[1],
                         stroke_color=GRAY, stroke_width=2, fill_color=INK, fill_opacity=0.08)
        band.move_to(p(95, 6))
        band_lbl = formula(r"\text{readings} \approx 95", size=MATH_SMALL + 4).next_to(band, UP, buff=0.12)
        band_lbl.align_to(band, RIGHT)
        col_ids = np.where(COL)[0]
        trails = always_redraw(lambda: VGroup(*[
            Line(p(X1[i], Y[i]), pts[i].get_center(), color=RED, stroke_width=2.5) for i in col_ids]))
        with self.narrate("Here's why. Take the patients whose reading came out high, around ninety "
                          "five. A few really are that high. Many more are ordinary patients whose "
                          "cuff read high, because ordinary patients are far more common.") as beat:
            self.play(FadeOut(tags), FadeOut(VGroup(bT, bT_lbl)), run_time=beat.until("high", offset=-0.3))
            self.play(FadeIn(band), FadeIn(band_lbl), *[pts[i].animate.set_color(INK) for i in col_ids],
                      run_time=1.0)
            beat.wait_until("A few", offset=-0.1)
            self.add(trails)
            self.play(c.animate.set_value(1.0), run_time=beat.until("ordinary", offset=0.4), rate_func=SMOOTH)
            self.play(Indicate(trails, color=RED, scale_factor=1.0), run_time=beat.until("common"))
            self.play(Indicate(ax.x_axis.numbers[2], color=INK), run_time=beat.remaining(0.6))

        # =========================================================== 7 · their average
        mt = float(T[COL].mean())
        mean_true = DashedLine(p(mt, 2.5), p(mt, 9.6), color=BLUE, stroke_width=3)
        mt_lbl = formula(r"\text{true average} \approx 90", size=MATH_SMALL + 4, color=BLUE)
        mt_lbl.next_to(mean_true.get_end(), LEFT, buff=0.15).shift(0.05 * DOWN)
        on_fit = Dot(p(94, A_OBS + B_OBS * 94), radius=0.09, color=YELLOW)
        on_true = Dot(p(mt, A_TRUE + B_TRUE * mt), radius=0.09, color=BLUE)
        link = DashedLine(on_true.get_center(), on_fit.get_center(), color=INK, stroke_width=2.5,
                          dash_length=0.06)
        lo_col = (X1 > 62) & (X1 < 68)
        arr_hi = Arrow(p(94, 1.5), p(mt, 1.5), buff=0, color=BLUE, stroke_width=4,
                       max_tip_length_to_length_ratio=0.4)
        arr_lo = Arrow(p(X1[lo_col].mean(), 1.5), p(T[lo_col].mean(), 1.5), buff=0, color=BLUE,
                       stroke_width=4, max_tip_length_to_length_ratio=0.4)
        with self.narrate("Their true pressures average only about ninety, so their risk is the "
                          "risk of ninety. Every column slides toward the middle like this, and the "
                          "line tilts flatter.") as beat:
            self.play(Create(mean_true), FadeIn(mt_lbl), run_time=beat.until("so their", offset=-0.1))
            self.play(FadeIn(on_true, scale=0.5), run_time=0.6)
            self.play(Create(link), FadeIn(on_fit, scale=0.5), run_time=beat.until("Every", offset=-0.1))
            self.play(GrowArrow(arr_hi), GrowArrow(arr_lo), run_time=beat.until("like this"))
            self.play(c.animate.set_value(0.0), FadeOut(trails), run_time=beat.until("line tilts"),
                      rate_func=SMOOTH)
            self.remove(trails)
            self.play(flag(fit_line, color=YELLOW), run_time=beat.remaining(0.6))

        # =========================================================== 8 · the squares
        u = 0.2                                     # units per mmHg of spread
        base = np.array([1.75, -0.45, 0])           # bottom-left corner of the picture
        sq_T = Square(8 * u, stroke_width=0, fill_color=BLUE, fill_opacity=0.75)
        sq_T.move_to(base, aligned_edge=DL)
        sq_E = Square(6 * u, stroke_width=0, fill_color=RED, fill_opacity=0.75)
        sq_E.move_to(base + RIGHT * (8 * u + 0.6), aligned_edge=DL)
        side_T = formula(r"8", size=MATH_SMALL, color=BLUE).next_to(sq_T, DOWN, buff=0.15)
        side_E = formula(r"6", size=MATH_SMALL, color=RED).next_to(sq_E, DOWN, buff=0.15)
        n64 = formula(r"64").move_to(sq_T)
        n36 = formula(r"36").move_to(sq_E)
        edge_T = Line(sq_T.get_corner(DL), sq_T.get_corner(DR), color=BLUE, stroke_width=4)
        edge_E = Line(sq_E.get_corner(DL), sq_E.get_corner(DR), color=RED, stroke_width=4)

        sig_e = ValueTracker(6.0)                   # error spread in the square picture

        def layout_split():
            tot = 64 + sig_e.get_value() ** 2
            side = u * np.sqrt(tot)
            hT = side * 64 / tot
            return side, hT, side - hT
        side0, hT0, hE0 = layout_split()
        blue_rect = Rectangle(width=side0, height=hT0, stroke_width=0, fill_color=BLUE,
                              fill_opacity=0.75).move_to(base, aligned_edge=DL)
        red_rect = Rectangle(width=side0, height=hE0, stroke_width=0, fill_color=RED,
                             fill_opacity=0.75).next_to(blue_rect, UP, buff=0)
        outline = Square(side0, color=INK, stroke_width=2.5).move_to(base, aligned_edge=DL)
        tot_num = DecimalNumber(100, num_decimal_places=0, font_size=MATH)
        tot_lbl = VGroup(formula(r"\text{total}"), tot_num).arrange(RIGHT, buff=0.2)
        tot_lbl.next_to(outline, UP, buff=0.18)
        with self.narrate("How much flatter depends on spreads, measured in squares. True pressures "
                          "give eight squared, sixty four. The cuff adds six squared, thirty six. "
                          "The readings vary by a hundred in total.") as beat:
            self.play(FadeOut(VGroup(band, band_lbl, mean_true, mt_lbl, on_fit, on_true, link,
                                     arr_hi, arr_lo)),
                      *[pts[i].animate.set_color(BLUE) for i in col_ids], run_time=beat.until("True", offset=-0.3))
            self.play(Create(edge_T), FadeIn(side_T), run_time=beat.until("eight", offset=-0.1))
            self.play(GrowFromEdge(sq_T, DOWN), run_time=beat.until("sixty", offset=-0.1))
            self.play(FadeIn(n64), run_time=0.5)
            beat.wait_until("six squared", offset=-0.3)
            self.play(Create(edge_E), FadeIn(side_E), run_time=0.6)
            self.play(GrowFromEdge(sq_E, DOWN), run_time=beat.until("thirty", offset=-0.1))
            self.play(FadeIn(n36), run_time=0.5)
            beat.wait_until("vary", offset=-0.2)
            self.remove(edge_T, edge_E)
            self.play(ReplacementTransform(sq_T, blue_rect), ReplacementTransform(sq_E, red_rect),
                      n64.animate.move_to(blue_rect), FadeOut(side_T), FadeOut(side_E),
                      run_time=1.3)
            # numbers follow the regions from here on
            n36.generate_target().move_to(red_rect)
            self.play(MoveToTarget(n36), Create(outline), FadeIn(tot_lbl), run_time=beat.remaining(0.8))

        def follow_rects():
            side, hT, hE = layout_split()
            blue_rect.stretch_to_fit_width(side).stretch_to_fit_height(hT).move_to(base, aligned_edge=DL)
            red_rect.stretch_to_fit_width(side).stretch_to_fit_height(hE).next_to(blue_rect, UP, buff=0)
            outline.stretch_to_fit_width(side).stretch_to_fit_height(side).move_to(base, aligned_edge=DL)
        rect_upd = lambda m: follow_rects()
        blue_rect.add_updater(rect_upd)
        n64.add_updater(lambda m: m.move_to(blue_rect))
        n36_num = DecimalNumber(36, num_decimal_places=0, font_size=MATH).move_to(n36)
        self.remove(n36)
        self.add(n36_num)
        n36_num.add_updater(lambda m: m.set_value(sig_e.get_value() ** 2).move_to(red_rect))
        tot_num.add_updater(lambda m: m.set_value(64 + sig_e.get_value() ** 2))
        tot_lbl.add_updater(lambda m: m.next_to(outline, UP, buff=0.18))

        # =========================================================== 9 · the formula
        lam = formula(r"\lambda", "=", size=EQ)
        num = formula(r"\sigma_T^2", size=EQ, color=BLUE)
        den = VGroup(formula(r"\sigma_T^2", size=EQ, color=BLUE), formula("+", size=EQ),
                     formula(r"\sigma_E^2", size=EQ, color=RED)).arrange(RIGHT, buff=0.12)
        bar = Line(LEFT, RIGHT, color=INK, stroke_width=3).set_width(den.width + 0.1)
        frac = VGroup(num, bar, den)
        num.next_to(bar, UP, buff=0.12)
        den.next_to(bar, DOWN, buff=0.12)
        eq_val = formula("=", size=EQ)
        lam_num = DecimalNumber(0.64, num_decimal_places=2, font_size=EQ)
        lam_num.add_updater(lambda m: m.set_value(64 / (64 + sig_e.get_value() ** 2)))
        row1 = VGroup(lam, frac, eq_val, lam_num).arrange(RIGHT, buff=0.2)
        row1.move_to([3.85, -1.55, 0])
        lam_num.clear_updaters()
        lam_num.add_updater(lambda m: m.set_value(64 / (64 + sig_e.get_value() ** 2)))
        row2 = MathTex(r"b_{\text{obs}}", "=", r"\lambda", r"\cdot", r"b_{\text{true}}", font_size=EQ)
        row2[0].set_color(YELLOW)
        row2[4].set_color(BLUE)
        row2.move_to([3.85, -2.75, 0])
        with self.narrate("The real share is sixty four out of a hundred, exactly the slope that "
                          "survived. Call it lambda, the reliability. The observed slope is lambda "
                          "times the true one.") as beat:
            self.play(Write(lam), run_time=0.6)
            self.play(TransformFromCopy(n64, num), run_time=beat.until("out of", offset=-0.1))
            self.play(Create(bar), TransformFromCopy(n64, den[0]), FadeIn(den[1]),
                      TransformFromCopy(n36_num, den[2]), run_time=beat.until("exactly", offset=-0.1))
            self.play(FadeIn(eq_val), FadeIn(lam_num), run_time=0.6)
            self.play(flag(lam_num, color=YELLOW), flag(readout_num), run_time=beat.until("Call", offset=-0.1))
            self.play(flag(lam, color=INK), run_time=beat.until("observed", offset=-0.1))
            self.play(TransformFromCopy(readout_num, row2[0]), FadeIn(row2[1]), run_time=0.8)
            self.play(TransformFromCopy(lam[0], row2[2]), FadeIn(row2[3]), run_time=0.7)
            self.play(TransformFromCopy(truth, row2[4]), run_time=beat.remaining(0.7))

        # =========================================================== 10 · prediction
        sloppy = formula(r"\sigma_E:\ 6 \to 12", size=MATH, color=RED)
        sloppy.move_to([5.35, 0.3, 0])
        with self.narrate("If the cuff were twice as sloppy, an error spread of twelve, how much "
                          "slope would survive? [pause 1.5]") as beat:
            beat.wait_until("twelve", offset=-0.3)
            self.play(Write(sloppy), run_time=0.9)
            self.play(flag(lam_num, color=INK), run_time=beat.until("survive"))
            self.play(Indicate(fit_line, color=YELLOW, scale_factor=1.0), run_time=beat.remaining(1.0))

        # =========================================================== 11 · the answer
        with self.narrate("Sixty four out of two hundred and eight, under a third. The line on the "
                          "left agrees: point three oh.") as beat:
            self.play(sig_e.animate.set_value(12.0), run_time=beat.until("under", offset=-0.1), rate_func=SMOOTH)
            beat.wait_until("line", offset=-0.2)
            self.play(s.animate.set_value(2.0), run_time=beat.until("point", offset=-0.2), rate_func=SMOOTH)
            self.play(flag(readout_num), run_time=beat.remaining(0.6))

        # =========================================================== 12 · measure twice
        rax = axes((40, 120), (40, 120), x_ticks=[40, 80, 120], y_ticks=[40, 80, 120], x_length=2.9,
                   y_length=2.9)
        rax.move_to([4.2, 1.05, 0])
        r_x = label("reading 1 (mmHg)", size=SMALL + 2, color=GRAY)
        r_x.next_to(rax.x_axis.numbers, DOWN, buff=0.12).align_to(rax.x_axis.get_right(), RIGHT)
        r_y = label("reading 2", size=SMALL + 2, color=GRAY)
        r_y.next_to(rax.y_axis.get_top(), UP, buff=0.18).align_to(rax.y_axis.numbers, LEFT)
        rpts = VGroup(*[Dot(rax.c2p(a, b), radius=0.05, color=PURPLE, fill_opacity=0.8)
                        for a, b in zip(X1, X2)])
        r_lbl = formula(r"r =", f"{R12:.2f}", size=MATH, color=PURPLE)
        r_lbl.move_to(rax.c2p(44, 112), aligned_edge=UL)
        with self.narrate("In real data the true pressures are hidden, so measure everyone twice. "
                          "Two readings share only the true part, so their correlation estimates "
                          "lambda: point six four.") as beat:
            self.play(s.animate.set_value(1.0), sig_e.animate.set_value(6.0), FadeOut(sloppy),
                      run_time=1.2, rate_func=SMOOTH)
            for m in (blue_rect, n64, n36_num, tot_num, tot_lbl):
                m.clear_updaters()
            self.play(FadeOut(VGroup(blue_rect, red_rect, outline, n64, n36_num, tot_lbl)),
                      run_time=beat.until("twice", offset=-0.6))
            self.play(Create(rax), FadeIn(r_x), FadeIn(r_y), run_time=0.8)
            self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in rpts], lag_ratio=0.01),
                      run_time=beat.until("correlation", offset=-0.1))
            self.play(Write(r_lbl), run_time=beat.until("lambda", offset=-0.1))
            self.play(flag(lam_num, color=PURPLE), flag(r_lbl[1], color=PURPLE), run_time=beat.remaining(0.8))

        # =========================================================== 13 · correct it
        row3 = MathTex(r"\hat b_{\text{true}}", "=", r"b_{\text{obs}}", r"/", r"r", font_size=EQ)
        row3[0].set_color(GREEN)
        row3[2].set_color(YELLOW)
        row3[4].set_color(PURPLE)
        corr_num = DecimalNumber(1.00, num_decimal_places=2, font_size=EQ, color=GREEN)
        row3_full = VGroup(row3, formula("=", size=EQ), corr_num).arrange(RIGHT, buff=0.2)
        row3_full.move_to(row2)

        def make_green():
            b0, a0 = B_OBS, A_OBS
            b = b0 * (1 + k.get_value() * (1 / R12 - 1))
            xm, ym = X1.mean(), Y.mean()
            return Line(p(X_LO, ym + b * (X_LO - xm)), p(X_HI, ym + b * (X_HI - xm)), color=GREEN,
                        stroke_width=5)
        with self.narrate("Divide the flattened slope by it, and the line swings back to one, "
                          "matching the truth we built in.") as beat:
            self.play(TransformMatchingTex(row2, row3), run_time=beat.until("line", offset=-0.2))
            self.play(FadeIn(row3_full[1:]), run_time=0.5)
            green = always_redraw(make_green)
            self.add(green)
            self.play(k.animate.set_value(1.0), run_time=beat.until("matching"), rate_func=SMOOTH)
            self.play(Indicate(truth, color=BLUE, scale_factor=1.0), run_time=beat.remaining(0.6))
        green.clear_updaters()

        # =========================================================== 14 · Spearman
        plot = VGroup(ax, x_meas, y_title, sim_tag, truth, readout_lbl, units)
        quote = VGroup(text("“two or more independent", slant=ITALIC, size=BODY),
                       text("series of observations”", slant=ITALIC, size=BODY)).arrange(DOWN, buff=0.15)
        who = label("Spearman, 1904", color=GRAY)
        qgroup = VGroup(quote, who).arrange(DOWN, buff=0.3).move_to([3.9, 0.6, 0])
        cite1 = citation("Spearman, 1904 · American Journal of Psychology")
        self.remove(fit_line)
        frozen = make_line()
        self.add(frozen)
        pts.clear_updaters()
        readout_num.clear_updaters()
        with self.narrate("Charles Spearman called this attenuation in nineteen oh four, and his "
                          "cure was the same: repeat the measurements.") as beat:
            self.play(FadeOut(VGroup(rax, r_x, r_y, rpts, r_lbl, row1, row3, row3_full[1:])),
                      dim(plot, pts, frozen, green, readout_num), run_time=1.0)
            self.play(FadeIn(cite1), run_time=beat.until("cure", offset=-0.2))
            self.play(Write(quote), run_time=beat.until("repeat"))
            self.play(FadeIn(who), run_time=beat.remaining(0.6))

        # =========================================================== 15 · MacMahon
        head = VGroup(label("link to stroke and heart disease"),
                      label("9 studies · 420,000 people", color=GRAY)).arrange(DOWN, buff=0.15)
        x0 = 3.55
        lab1 = label("single reading", color=GRAY)
        lab2 = label("corrected", color=GRAY)
        bar1 = Rectangle(width=1.7, height=0.5, stroke_width=0, fill_color=YELLOW, fill_opacity=0.9)
        bar2 = Rectangle(width=1.7 * 1.6, height=0.5, stroke_width=0, fill_color=GREEN, fill_opacity=0.9)
        bar1.move_to([x0, 0.3, 0], aligned_edge=LEFT)
        bar2.move_to([x0, -0.65, 0], aligned_edge=LEFT)
        lab1.next_to(bar1, LEFT, buff=0.2)
        lab2.next_to(bar2, LEFT, buff=0.2)
        v1 = formula(r"1.0\times", size=MATH_SMALL + 4).next_to(bar1, RIGHT, buff=0.15)
        plus = formula(r"+60\%", color=GREEN).next_to(bar2, UP, buff=0.15).align_to(bar2, RIGHT)
        plus.shift(UP * 0.0)
        head.move_to([3.9, 1.9, 0])
        cite2 = citation("MacMahon et al., 1990 · The Lancet")
        base_ln = Line([x0, 0.75, 0], [x0, -1.1, 0], color=GRAY, stroke_width=2)
        with self.narrate("In nineteen ninety, MacMahon and colleagues pooled nine studies, four "
                          "hundred and twenty thousand people, each with blood pressure measured "
                          "once at the start. Correcting for this dilution made the links to stroke "
                          "and heart disease about sixty percent stronger.") as beat:
            self.play(FadeOut(qgroup), ReplacementTransform(cite1, cite2), run_time=0.8)
            self.play(FadeIn(head[1]), run_time=beat.until("each", offset=-0.2))
            self.play(Create(base_ln), FadeIn(lab1), GrowFromEdge(bar1, LEFT), FadeIn(v1),
                      run_time=beat.until("Correcting", offset=-0.1))
            self.play(FadeIn(lab2), TransformFromCopy(bar1, bar2), run_time=beat.until("links", offset=-0.1))
            self.play(FadeIn(head[0]), run_time=beat.until("sixty", offset=-0.2))
            self.play(FadeIn(plus, shift=0.1 * UP), run_time=beat.remaining(0.6))

        # =========================================================== 16 · limits
        holds = label("holds: random error, one predictor")
        breaks = label("breaks: systematic error, many predictors")
        holds.set_color_by_t2c({"holds:": GRAY})
        breaks.set_color_by_t2c({"breaks:": GRAY})
        lim = VGroup(holds, breaks).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to([3.85, -2.05, 0])
        with self.narrate("The fix assumes random error in one predictor. Systematic error, or "
                          "several noisy predictors at once, can push estimates either way.") as beat:
            self.play(FadeIn(holds, shift=0.1 * RIGHT), run_time=beat.until("Systematic", offset=-0.2))
            self.play(FadeIn(breaks, shift=0.1 * RIGHT), run_time=beat.until("either", offset=-0.1))
            self.play(Indicate(breaks, color=INK, scale_factor=1.04), run_time=beat.remaining(0.6))

        # =========================================================== 17 · landing
        ans = label("flatter").next_to(frozen.get_end(), RIGHT, buff=0.15)
        true_lbl = label("true", color=BLUE).next_to(truth.get_end(), RIGHT, buff=0.15)
        with self.narrate("So in the opening, the answer was flatter, by the share of each reading "
                          "that's noise. The effect was never weaker. The ruler was.") as beat:
            self.play(FadeOut(VGroup(head, lab1, lab2, bar1, bar2, v1, plus, base_ln, lim, cite2)),
                      FadeOut(green), undim(plot, pts, frozen, readout_num), run_time=1.0)
            self.play(FadeIn(ans), FadeIn(true_lbl), run_time=beat.until("flatter", offset=-0.1))
            box_a = box(ans)
            self.play(Create(box_a), run_time=0.6)
            self.play(Indicate(pts, color=RED, scale_factor=1.0), run_time=beat.until("effect", offset=-0.1))
            self.play(Indicate(truth, color=BLUE, scale_factor=1.0), run_time=beat.until("ruler", offset=-0.1))
            self.play(flag(x_meas, color=INK), run_time=beat.remaining(0.6))
        self.end_card()
