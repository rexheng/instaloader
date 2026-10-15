"""Episode 37 - Separating the Inseparable by Adding a Dimension.

    videos/toolkit/render.sh videos/episodes/037-svm-kernel-trick/scene.py Episode \
        videos/episodes/037-svm-kernel-trick/final.mp4

Palette (script.md): PURPLE in-range class, BLUE out-of-range ring, YELLOW the cut,
GREEN the added height z = x^2 + y^2, RED mistakes (always ringed), INK rings = points a
cut is built from.  All stage data are simulated (data.py, seed 7).
"""
from __future__ import annotations

import os
import sys

import numpy as np
from manim import *
from sample_space import *

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import kernel, lift, make_points, perceptron  # noqa: E402

# ----------------------------------------------------------------------------- data
X, Y = make_points()
F3 = lift(X)
N = len(Y)
H2 = perceptron(X, Y, 5000, seed=3, w0=[0.6, 0.8], b0=0.3)       # 2-D: never converges
M2 = np.array([h[2] for h in H2])
BEST = int(np.argmin(M2))                                          # nudge 187, 22 wrong
H3 = perceptron(F3, Y, 50, seed=44)                                # 3-D: 8 nudges -> 0
NUDGED3 = [h[3] for h in H3[1:]]

from sklearn.svm import SVC  # noqa: E402

_svm = SVC(kernel="precomputed", C=1e6).fit(kernel(X, X), Y)
SV = [int(i) for i in _svm.support_]
_alpha = np.zeros(N)
_alpha[_svm.support_] = _svm.dual_coef_[0]
W_SVM = _alpha @ F3
B_SVM = float(_svm.intercept_[0])
C_LEVEL = 1.65
KZ = 0.45                     # screen scale of the height axis
L = 2.5                       # half-width of the drawn sheet / floor axes

assert BEST == 187 and M2[BEST] == 22 and len(H3) == 9 and H3[-1][2] == 0 and len(SV) == 4


def plane_abc(w, b):
    """w.(x, y, z) + b = 0  ->  z = A + B x + C y."""
    return -b / w[2], -w[0] / w[2], -w[1] / w[2]


SVM_ABC = plane_abc(W_SVM, B_SVM)
GUT_ABC = [plane_abc(W_SVM, B_SVM - s) for s in (1, -1)]
H3_ABC = [plane_abc(h[0], h[1]) for h in H3[1:]]

# view presets: (elevation deg, azimuth deg, scale, cx, cy)
TOP = (0, 0, 1.2, -2.6, 0.15)
TILT = (62, -30, 1.15, -2.6, -1.15)
SMALL3D = (62, -30, 0.78, -4.35, -0.95)


# ----------------------------------------------------------------------------- stage
class Stage:
    def __init__(self):
        el, az, s, cx, cy = TOP
        self.el, self.az, self.S = ValueTracker(el), ValueTracker(az), ValueTracker(s)
        self.cx, self.cy = ValueTracker(cx), ValueTracker(cy)
        self.lift = ValueTracker(0.0)

    def P(self, x, y, z=0.0):
        el, az = np.radians(self.el.get_value()), np.radians(self.az.get_value())
        z = z * KZ * self.lift.get_value()
        x1 = x * np.cos(az) - y * np.sin(az)
        y1 = x * np.sin(az) + y * np.cos(az)
        s = self.S.get_value()
        return np.array([self.cx.get_value() + s * x1,
                         self.cy.get_value() + s * (y1 * np.cos(el) + z * np.sin(el)), 0.0])

    def view(self, preset):
        el, az, s, cx, cy = preset
        return [self.el.animate.set_value(el), self.az.animate.set_value(az),
                self.S.animate.set_value(s), self.cx.animate.set_value(cx),
                self.cy.animate.set_value(cy)]


def clip_plane(A, B, C, zlo=-0.4, zhi=6.0):
    """Sheet z = A + Bx + Cy over the square [-L, L]^2, clipped to zlo <= z <= zhi."""
    poly = [np.array([x, y, A + B * x + C * y]) for x, y in ((-L, -L), (L, -L), (L, L), (-L, L))]
    for bound, keep_below in ((zhi, True), (zlo, False)):
        out = []
        for i, p in enumerate(poly):
            q = poly[(i + 1) % len(poly)]
            pin = p[2] <= bound if keep_below else p[2] >= bound
            qin = q[2] <= bound if keep_below else q[2] >= bound
            if pin:
                out.append(p)
            if pin != qin:
                t = (bound - p[2]) / (q[2] - p[2])
                out.append(p + t * (q - p))
        poly = out
        if not poly:
            break
    return poly


def bowl_cut(A, B, C):
    """Circle where the sheet meets the bowl z = x^2 + y^2: (centre, radius)."""
    r2 = A + (B * B + C * C) / 4
    return np.array([B / 2, C / 2]), np.sqrt(max(r2, 1e-6))


def line_in_square(th, d, half=2.45):
    """Line {p : p.(cos th, sin th) = d} clipped to the square [-half, half]^2."""
    n = np.array([np.cos(th), np.sin(th)])
    u = np.array([-n[1], n[0]])
    p0 = d * n
    lo, hi = -1e9, 1e9
    for k in range(2):
        if abs(u[k]) < 1e-9:
            continue
        t1, t2 = (-half - p0[k]) / u[k], (half - p0[k]) / u[k]
        lo, hi = max(lo, min(t1, t2)), min(hi, max(t1, t2))
    if lo >= hi:
        return p0, p0 + 1e-3 * u
    return p0 + lo * u, p0 + hi * u


def line_params(w, b, near_th=None):
    th = np.arctan2(w[1], w[0])
    d = -b / np.linalg.norm(w)
    if near_th is not None:                      # pick the equivalent (th +- pi, -d) nearest
        best = None
        for k in range(-3, 4):
            for sgn in (1, -1):
                t2 = th + k * np.pi
                d2 = d if k % 2 == 0 else -d
                if sgn < 0:
                    continue
                if best is None or abs(t2 - near_th) < abs(best[0] - near_th):
                    best = (t2, d2)
        th, d = best
    return th, d


DIGIT = [
    "................",
    "....######......",
    "...########.....",
    "..###....###....",
    "..##......##....",
    "..........##....",
    ".........###....",
    "........###.....",
    ".......###......",
    "......###.......",
    ".....###........",
    "....###.........",
    "...###..........",
    "..##########....",
    "..##########....",
    "................",
]


# ----------------------------------------------------------------------------- scene
class Episode(NarratedScene):
    EPISODE = 37
    TITLE = "Separating the Inseparable by Adding a Dimension"
    PRONUNCIATIONS = {"Guyon": "ghee yon", "Vapnik": "vap nick", "Boser": "bow zer",
                      "Rosenblatt": "rose en blat", "Cortes": "cor tez"}

    # -------------------------------------------------------------- builders
    def curve3d(self, fn, n=72, **kw):
        st = self.st
        m = VMobject(**kw)

        def upd(mm):
            mm.set_points_as_corners([st.P(*fn(t)) for t in np.linspace(0, 1, n)])
        upd(m)
        m.add_updater(upd)
        return m

    def construct(self):
        st = self.st = Stage()

        # ---- floor axes, labels, points
        x_axis = Line(ORIGIN, RIGHT, color=GRAY, stroke_width=2)
        y_axis = Line(ORIGIN, UP, color=GRAY, stroke_width=2)
        x_axis.add_updater(lambda m: m.put_start_and_end_on(st.P(-L, 0), st.P(L, 0)))
        y_axis.add_updater(lambda m: m.put_start_and_end_on(st.P(0, -L), st.P(0, L)))
        x_lab = formula("x", size=MATH_SMALL + 6, color=GRAY)
        y_lab = formula("y", size=MATH_SMALL + 6, color=GRAY)
        x_lab.add_updater(lambda m: m.move_to(st.P(L + 0.28, 0)))
        y_lab.add_updater(lambda m: m.move_to(st.P(0, L + 0.3)))
        floor = VGroup(x_axis, y_axis, x_lab, y_lab)
        for m in floor:
            m.update()

        dots_all = VGroup()
        for i in range(N):
            d = Dot(radius=0.075, color=PURPLE if Y[i] > 0 else BLUE)
            d.add_updater(lambda m, i=i: m.move_to(st.P(*F3[i])))
            d.update()
            dots_all.add(d)
        purple = VGroup(*[dots_all[i] for i in range(N) if Y[i] > 0])
        blue = VGroup(*[dots_all[i] for i in range(N) if Y[i] < 0])

        sim = text("simulated data", size=SMALL, color=GRAY)
        sim.move_to([-SAFE_X + sim.width / 2, SAFE_TOP - 0.05 - sim.height / 2, 0])

        def ring(i, color=RED, r=0.16, width=3.5):
            c = Circle(radius=r, color=color, stroke_width=width)
            c.add_updater(lambda m, i=i: m.move_to(dots_all[i].get_center()))
            c.update()
            return c

        # ---- the 2-D cut (angle / offset trackers)
        th = ValueTracker(0.35)
        dd = ValueTracker(0.0)
        cut2d = Line(ORIGIN, RIGHT, color=YELLOW, stroke_width=5)

        def upd_cut(m):
            a, b = line_in_square(th.get_value(), dd.get_value())
            m.put_start_and_end_on(st.P(*a), st.P(*b))
        upd_cut(cut2d)
        cut2d.add_updater(upd_cut)

        def go_line(k, run_time):
            t2, d2 = line_params(H2[k][0], H2[k][1], near_th=th.get_value())
            return [th.animate(run_time=run_time, rate_func=SMOOTH).set_value(t2),
                    dd.animate(run_time=run_time, rate_func=SMOOTH).set_value(d2)]

        # ================================================================ 1 cold open
        with self.narrate("Purple points in the middle, a ring of blue around them. "
                          "You get one straight cut. Can it put all the purple on one side "
                          "and all the blue on the other? [pause 1.5]") as beat:
            self.add(floor)
            self.play(LaggedStart(*[GrowFromCenter(d) for d in purple], lag_ratio=0.04),
                      FadeIn(sim), run_time=beat.until("a ring"))
            self.play(LaggedStart(*[GrowFromCenter(d) for d in blue], lag_ratio=0.04),
                      run_time=beat.until("You get"))
            self.play(Create(cut2d), run_time=beat.until("Can it"))
            # sweep: angle and offset wander while the question is asked and held
            self.play(th.animate.set_value(0.35 + 2.2), dd.animate.set_value(0.9),
                      run_time=beat.until("and all the blue"), rate_func=SMOOTH)
            self.play(th.animate.set_value(0.35 + 3.6), dd.animate.set_value(-0.7),
                      run_time=beat.remaining(), rate_func=SMOOTH)

        # ================================================================ 2 stakes
        leg_p = VGroup(Dot(radius=0.1, color=PURPLE), text("in range", size=LABEL, color=PURPLE)
                       ).arrange(RIGHT, buff=0.22)
        leg_b = VGroup(Dot(radius=0.1, color=BLUE), text("out of range", size=LABEL, color=BLUE)
                       ).arrange(RIGHT, buff=0.22)
        legend = VGroup(leg_p, leg_b).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        legend.move_to([1.6 + legend.width / 2, 2.95, 0])
        with self.narrate("It's the shape you get whenever normal means near the middle, like "
                          "two lab readings that are fine near their usual values and a warning "
                          "when either one strays. The simplest learners can only make straight "
                          "cuts.") as beat:
            beat.wait_until("normal", offset=-0.2)
            self.play(FadeIn(leg_p, shift=0.15 * RIGHT), flag_group(purple), run_time=1.2)
            beat.wait_until("strays", offset=-0.3)
            self.play(FadeIn(leg_b, shift=0.15 * RIGHT), flag_group(blue), run_time=1.2)
            self.play(th.animate.set_value(0.35 + 4.6), dd.animate.set_value(0.4),
                      run_time=beat.remaining(), rate_func=SMOOTH)

        # ================================================================ 3 perceptron
        nud = ValueTracker(0)
        mis = ValueTracker(M2[0])
        nud_lbl = live_number(nud, 0, prefix=r"\text{nudges}", size=MATH)
        mis_lbl = live_number(mis, 0, prefix=r"\text{mistakes}", size=MATH, color=RED)
        counters = VGroup(nud_lbl, mis_lbl).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        counters.move_to([1.6 + counters.width / 2, 1.25, 0])
        cite = citation("Rosenblatt, 1958 · Psychological Review")
        with self.narrate("Try one: Rosenblatt's perceptron, from nineteen fifty-eight. Start "
                          "with a line. Find a point on the wrong side, and nudge the line "
                          "toward it. Repeat until nothing is wrong.") as beat:
            self.play(FadeIn(cite), run_time=0.6)
            beat.wait_until("Start", offset=-0.1)
            self.play(*go_line(0, 1.0), FadeIn(counters), run_time=1.0)
            beat.wait_until("Find", offset=-0.1)
            for k in range(1, 5):
                i = H2[k][3]
                rg = ring(i)
                t_ring = 0.5 if k > 1 else beat.until("nudge", offset=-0.05)
                self.play(Create(rg), run_time=t_ring)
                self.play(*go_line(k, 0.75), nud.animate.set_value(k),
                          mis.animate.set_value(M2[k]), run_time=0.75)
                self.play(FadeOut(rg), run_time=0.4)
            self.play(*go_line(5, beat.remaining()), nud.animate.set_value(5),
                      mis.animate.set_value(M2[5]), run_time=beat.remaining())

        # ================================================================ 4 failure
        ghosts = VGroup()
        for k in range(6, 5001, 20):
            t2, d2 = line_params(H2[k][0], H2[k][1])
            a, b = line_in_square(t2, d2)
            ghosts.add(Line(st.P(*a), st.P(*b), color=YELLOW, stroke_width=1.6,
                            stroke_opacity=0.0))
        best_note = formula(r"\text{best ever:}", r"22", size=MATH)
        best_note[1].set_color(RED)
        floor_note = formula(r"\text{any line:}", r"\ge 21", size=MATH, color=GRAY)
        notes = VGroup(best_note, floor_note).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        notes.next_to(counters, DOWN, buff=0.55, aligned_edge=LEFT)
        best_rings = VGroup()
        with self.narrate("Here, that never happens. After five thousand nudges, the line is "
                          "still thrashing. Its best moment left twenty-two of eighty points "
                          "wrong, and no straight line gets below twenty-one. The perceptron "
                          "stops only at zero mistakes, so it never stops.") as beat:
            beat.wait_until("five thousand", offset=-0.3)
            mis.add_updater(lambda m: m.set_value(M2[min(5000, int(nud.get_value()) // 7 * 7)]))
            n_g = len(ghosts)

            def show_ghosts(m, a):
                for j, g in enumerate(m):
                    g.set_stroke(opacity=0.16 if j < a * n_g else 0.0)
            self.play(nud.animate.set_value(5000), UpdateFromAlphaFunc(ghosts, show_ghosts),
                      cut2d.animate.set_stroke(opacity=0.0), rate_func=LINEAR,
                      run_time=beat.until("Its best", offset=-0.2))
            mis.clear_updaters()
            mis.set_value(M2[-1])
            t2, d2 = line_params(H2[BEST][0], H2[BEST][1], near_th=th.get_value())
            th.set_value(t2)
            dd.set_value(d2)
            wrong = np.flatnonzero(np.sign(X @ H2[BEST][0] + H2[BEST][1]) * Y <= 0)
            best_rings = VGroup(*[ring(int(i), r=0.15, width=3) for i in wrong])
            self.play(ghosts.animate.set_stroke(opacity=0.07),
                      cut2d.animate.set_stroke(opacity=1.0), run_time=0.6)
            self.play(LaggedStart(*[Create(r) for r in best_rings], lag_ratio=0.05),
                      FadeIn(best_note, shift=0.1 * UP), run_time=beat.until("no straight"))
            self.play(FadeIn(floor_note, shift=0.1 * UP), run_time=0.8)
            beat.wait_until("zero", offset=-0.1)
            self.play(flag(mis_lbl, color=RED), run_time=0.9)
            self.play(ghosts.animate.set_stroke(opacity=0.12), run_time=beat.remaining())

        # ================================================================ 5 what would you try
        k_pt = 54                                          # blue point at (1.72, -0.53)
        px, py = X[k_pt]
        radius = Line(st.P(0, 0), st.P(px, py), color=GREEN, stroke_width=5)
        leg_x = DashedLine(st.P(0, 0), st.P(px, 0), color=INK, stroke_width=3)
        leg_y = DashedLine(st.P(px, 0), st.P(px, py), color=INK, stroke_width=3)
        f_z = formula("z", "=", "x^2", "+", "y^2", size=EQ)
        f_z[0].set_color(GREEN)
        f_z.move_to([1.6 + f_z.width / 2, -0.55, 0])
        with self.narrate("What would you try? [pause 1] The two colours differ in one thing a "
                          "line can't see: distance from the centre. So give every point a third "
                          "number, its squared distance, x squared plus y squared.") as beat:
            self.play(FadeOut(best_rings), FadeOut(notes), FadeOut(ghosts), FadeOut(cite),
                      cut2d.animate.set_stroke(opacity=0.0), run_time=1.0)
            beat.wait_until("distance", offset=-0.2)
            self.play(Create(radius), flag(dots_all[k_pt], color=GREEN), run_time=1.0)
            beat.wait_until("third", offset=-0.2)
            self.play(Create(leg_x), Create(leg_y), run_time=0.8)
            beat.wait_until("squared distance", offset=-0.2)
            self.play(TransformFromCopy(radius, f_z[0]), Write(f_z[1]), run_time=0.9)
            beat.wait_until("x squared", offset=-0.15)
            self.play(TransformFromCopy(leg_x, f_z[2]), run_time=0.6)
            self.play(TransformFromCopy(leg_y, f_z[4]), Write(f_z[3]), run_time=beat.remaining())

        # ================================================================ 6 lift
        z_axis = Line(ORIGIN, UP, color=GREEN, stroke_width=3)
        z_axis.add_updater(lambda m: m.put_start_and_end_on(st.P(0, 0, 0), st.P(0, 0, 6.3)))
        z_lab = formula("z", size=MATH_SMALL + 6, color=GREEN)
        z_lab.add_updater(lambda m: m.next_to(z_axis.get_end(), UP, buff=0.12))
        z_axis.update()
        z_lab.update()
        bowl = VGroup()
        for r in (0.6, 1.2, 1.8, 2.4):
            bowl.add(self.curve3d(lambda t, r=r: (r * np.cos(TAU * t), r * np.sin(TAU * t), r * r),
                                  stroke_color=DIM, stroke_width=1.6))
        for k in range(12):
            a = TAU * k / 12
            bowl.add(self.curve3d(lambda t, a=a: (2.4 * t * np.cos(a), 2.4 * t * np.sin(a),
                                                  (2.4 * t) ** 2), n=24,
                                  stroke_color=DIM, stroke_width=1.6))
        with self.narrate("Now use that number as a height. The purple points stay low. The "
                          "blue ones climb the walls of a bowl.") as beat:
            self.play(FadeOut(radius), FadeOut(leg_x), FadeOut(leg_y),
                      *st.view(TILT), run_time=beat.until("as a height", offset=-0.1))
            self.add(bowl)
            self.bring_to_front(dots_all)
            self.play(st.lift.animate.set_value(1.0), Create(z_axis), FadeIn(z_lab),
                      run_time=beat.until("climb", offset=0.2), rate_func=SMOOTH)
            self.play(flag_group(blue), run_time=beat.remaining())

        # ================================================================ 7 fix works
        pA, pB, pC = (ValueTracker(v) for v in H3_ABC[0])
        sheet_op = ValueTracker(0.0)
        sheet = VMobject(stroke_color=YELLOW, fill_color=YELLOW)

        def upd_sheet(m):
            poly = clip_plane(pA.get_value(), pB.get_value(), pC.get_value())
            pts = [st.P(*p) for p in poly] or [st.P(0, 0)] * 3
            m.set_points_as_corners(pts + [pts[0]])
            o = sheet_op.get_value()
            m.set_stroke(opacity=0.9 * o, width=2.5)
            m.set_fill(opacity=0.16 * o)
        upd_sheet(sheet)
        sheet.add_updater(upd_sheet)

        def go_sheet(abc, rt):
            return [pA.animate(run_time=rt).set_value(abc[0]),
                    pB.animate(run_time=rt).set_value(abc[1]),
                    pC.animate(run_time=rt).set_value(abc[2])]

        with self.narrate("Run the same perceptron on three numbers per point. Eight nudges, "
                          "and zero mistakes. A flat sheet now slides between the layers.") as beat:
            self.remove(*dots_all)
            self.add(*purple, sheet, *blue)
            nud.set_value(1)
            mis.set_value(H3[1][2])
            self.play(sheet_op.animate.set_value(1.0), run_time=beat.until("Eight", offset=-1.2))
            n_steps = len(H3_ABC) - 1
            step = beat.until("zero", offset=-0.1) / n_steps
            for k in range(1, len(H3_ABC)):
                rg = ring(NUDGED3[k], color=RED)
                self.play(*go_sheet(H3_ABC[k], step), nud.animate.set_value(k + 1),
                          mis.animate.set_value(H3[k + 1][2]), FadeIn(rg), run_time=step)
                self.remove(rg)
            self.play(Indicate(mis_lbl, color=YELLOW, scale_factor=1.12), run_time=0.9)
            self.play(sheet_op.animate.set_value(1.35), run_time=beat.remaining())

        # ================================================================ 8 formula
        f_c = formula("z", "=", "c", size=EQ)
        f_c[0].set_color(GREEN)
        f_c[2].set_color(YELLOW)
        f_c.next_to(f_z, DOWN, buff=0.45, aligned_edge=LEFT)
        f_circ = formula("x^2", "+", "y^2", "=", "c", size=EQ)
        f_circ[4].set_color(YELLOW)
        f_circ.next_to(f_c, DOWN, buff=0.45, aligned_edge=LEFT)
        cut_op = ValueTracker(0.0)
        cut_curve = self.curve3d(
            lambda t: (*(bowl_cut(pA.get_value(), pB.get_value(), pC.get_value())[0]
                         + bowl_cut(pA.get_value(), pB.get_value(), pC.get_value())[1]
                         * np.array([np.cos(TAU * t), np.sin(TAU * t)])),
                       pA.get_value() + pB.get_value() * 0 + 0.0), n=96,
            stroke_color=YELLOW, stroke_width=5)
        # the curve lies on the sheet AND the bowl: z = x^2 + y^2 on the circle
        cut_curve.clear_updaters()

        def upd_curve(m):
            ctr, r = bowl_cut(pA.get_value(), pB.get_value(), pC.get_value())
            pts = []
            for t in np.linspace(0, 1, 97):
                x, y = ctr + r * np.array([np.cos(TAU * t), np.sin(TAU * t)])
                pts.append(st.P(x, y, x * x + y * y))
            m.set_points_as_corners(pts)
            m.set_stroke(opacity=cut_op.get_value())
        upd_curve(cut_curve)
        cut_curve.add_updater(upd_curve)
        shadow = VMobject(stroke_color=YELLOW, stroke_width=4)

        with self.narrate("Any sheet between them works, so take a level one, at height c. "
                          "The bowl is height equals x squared plus y squared. Set the two equal, "
                          "and you get x squared plus y squared equals c. That's a circle, drawn "
                          "by a flat cut.") as beat:
            self.play(FadeOut(counters), *go_sheet((C_LEVEL, 0.0, 0.0), 1.4),
                      sheet_op.animate.set_value(1.0), run_time=1.4)
            beat.wait_until("height c", offset=-0.1)
            self.play(TransformFromCopy(sheet, f_c), run_time=1.0)
            beat.wait_until("The bowl", offset=-0.1)
            self.play(flag(f_z), Indicate(bowl, color=GRAY, scale_factor=1.0), run_time=1.0)
            beat.wait_until("Set", offset=-0.1)
            self.add(cut_curve)
            self.bring_to_front(*blue)
            self.play(cut_op.animate.set_value(1.0), run_time=beat.until("you get"))
            self.play(TransformFromCopy(f_z[2:], f_circ[0:3]), Write(f_circ[3]),
                      TransformFromCopy(f_c[2], f_circ[4]),
                      run_time=beat.until("That's", offset=-0.1))
            ctr, r = bowl_cut(C_LEVEL, 0, 0)
            shadow.set_points_as_corners([st.P(ctr[0] + r * np.cos(a), ctr[1] + r * np.sin(a), 0)
                                          for a in np.linspace(0, TAU, 97)])
            self.play(TransformFromCopy(cut_curve, shadow), run_time=beat.until("drawn"))
            self.play(flag(f_circ), run_time=beat.remaining())

        # ================================================================ 9 cost
        self.remove(shadow)
        shadow = self.curve3d(lambda t: (r * np.cos(TAU * t), r * np.sin(TAU * t), 0.0), n=97,
                              stroke_color=YELLOW, stroke_width=4)
        self.add(shadow)
        px_size = 0.16
        grid = VGroup()
        for row, line in enumerate(DIGIT):
            for col, ch in enumerate(line):
                sq = Square(px_size, stroke_color=DIM, stroke_width=1,
                            fill_color=INK, fill_opacity=0.9 if ch == "#" else 0.0)
                sq.move_to([col * px_size, -row * px_size, 0])
                grid.add(sq)
        grid.move_to([-0.1, 1.45, 0])
        g_lab = formula(r"16\times16", "=", r"256\ \text{pixels}", size=MATH)
        g_lab.next_to(grid, DOWN, buff=0.3)
        arrow = Arrow(grid.get_right() + 0.15 * RIGHT, grid.get_right() + 1.6 * RIGHT,
                      color=GRAY, stroke_width=4, buff=0)
        cnt_top = formula(r"\text{products of}\le 7\ \text{pixels}", size=MATH)
        cnt = formula(r"\binom{263}{7}", r"\approx", r"1.6\times10^{13}", size=EQ)
        cnt_g = VGroup(cnt_top, cnt).arrange(DOWN, buff=0.3)
        cnt_g.next_to(arrow, RIGHT, buff=0.25)
        keep_in_safe(cnt_g)
        with self.narrate("But I had to guess that extra number. A handwritten digit on a "
                          "sixteen by sixteen grid has two hundred fifty-six pixels. Every product "
                          "of up to seven pixels gives about sixteen trillion new numbers, for "
                          "each image.") as beat:
            self.play(flag(f_z[2:]), run_time=0.9)
            beat.wait_until("A handwritten", offset=-0.3)
            self.play(FadeOut(VGroup(f_z, f_c, f_circ, legend)), *st.view(SMALL3D),
                      run_time=1.2)
            self.play(LaggedStart(*[FadeIn(s) for s in grid], lag_ratio=0.004),
                      run_time=beat.until("two hundred"))
            self.play(Write(g_lab), run_time=1.0)
            beat.wait_until("Every product", offset=-0.1)
            self.play(GrowArrow(arrow), FadeIn(cnt_top, shift=0.1 * RIGHT), run_time=0.9)
            beat.wait_until("sixteen trillion", offset=-0.3)
            self.play(Write(cnt), run_time=1.0)
            self.play(Indicate(cnt[2], color=YELLOW, scale_factor=1.06),
                      run_time=beat.remaining())

        # ================================================================ 10 dot products
        nudge_rings = VGroup(*[ring(i, color=INK, r=0.14, width=3) for i in NUDGED3])
        f_sheet = formula(r"\text{sheet}", "=", r"\pm\phi(p_1)", r"\pm\phi(p_2)", r"\pm\cdots",
                          r"\pm\phi(p_8)", size=MATH)
        f_sheet[0].set_color(YELLOW)
        f_key = formula(r"\phi(p)", "=", r"(x,\ y,\ ", "z", ")", size=MATH_SMALL + 4, color=GRAY)
        f_key[3].set_color(GREEN)
        f_score = formula(r"\text{score}(q)", "=", r"\pm\phi(p_1)\cdot\phi(q)", r"\pm\cdots",
                          r"\pm\phi(p_8)\cdot\phi(q)", size=MATH)
        col = VGroup(f_sheet, f_key, f_score).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        col.move_to([2.35, 1.2, 0])
        keep_in_safe(col)
        with self.narrate("Look at what the perceptron actually kept. Its sheet is a tally of "
                          "the eight lifted points it nudged for, each added or subtracted. So "
                          "scoring a new point needs only dot products with those eight.") as beat:
            self.play(FadeOut(VGroup(grid, g_lab, arrow, cnt_g)), run_time=0.8)
            beat.wait_until("a tally", offset=-0.2)
            self.play(LaggedStart(*[Create(r) for r in nudge_rings], lag_ratio=0.12),
                      run_time=beat.until("the eight", offset=-0.1))
            self.play(Write(f_sheet[0:2]), run_time=0.5)
            self.play(TransformFromCopy(nudge_rings, f_sheet[2:]),
                      run_time=beat.until("each added", offset=-0.1))
            self.play(FadeIn(f_key, shift=0.1 * UP), run_time=0.8)
            beat.wait_until("dot products", offset=-0.2)
            self.play(Write(f_score[0:2]), run_time=0.5)
            self.play(TransformFromCopy(f_sheet[2:], f_score[2:]),
                      run_time=beat.remaining(min_time=0.8))

        # ================================================================ 11 kernel
        ia, ib = 7, 75                                    # one purple, one blue point
        sticks = VGroup()
        for i in (ia, ib):
            s = Line(ORIGIN, UP, color=GREEN, stroke_width=5)
            s.add_updater(lambda m, i=i: m.put_start_and_end_on(st.P(*X[i], 0), st.P(*F3[i])))
            s.update()
            sticks.add(s)
        lab_a = formula("a", size=MATH, color=PURPLE)
        lab_b = formula("b", size=MATH, color=BLUE)
        lab_a.add_updater(lambda m: m.next_to(dots_all[ia], LEFT, buff=0.16))
        lab_b.add_updater(lambda m: m.next_to(dots_all[ib], RIGHT, buff=0.16))
        lab_a.update()
        lab_b.update()
        f_dot = formula(r"\phi(a)\cdot\phi(b)", "=", r"a_1b_1+a_2b_2", "+", r"z_a\,z_b", size=EQ)
        f_dot[4].set_color(GREEN)
        f_dot.move_to([2.35, -0.95, 0])
        f_dot2 = formula(r"\phi(a)\cdot\phi(b)", "=", r"a\cdot b", "+", r"|a|^2\,|b|^2", size=EQ)
        f_dot2[4].set_color(GREEN)
        f_dot2.move_to(f_dot, aligned_edge=LEFT)
        f_K = formula(r"K(a,b)", "=", r"a\cdot b", "+", r"|a|^2\,|b|^2", size=EQ)
        f_K[0].set_color(YELLOW)
        f_K[4].set_color(GREEN)
        f_K.move_to(f_dot, aligned_edge=LEFT)
        with self.narrate("And the dot product of two lifted points never needs the lift. It's "
                          "the flat dot product, plus the product of the two heights, and each "
                          "height is just a squared length. A shortcut like this is called a "
                          "kernel.") as beat:
            self.play(FadeOut(nudge_rings), dim(f_sheet, f_key, f_score), run_time=0.8)
            self.play(Create(sticks), FadeIn(lab_a), FadeIn(lab_b),
                      Write(f_dot[0:2]), run_time=beat.until("It's", offset=-0.1))
            self.play(Write(f_dot[2]), run_time=beat.until("plus the product", offset=-0.1))
            self.play(Write(f_dot[3]), TransformFromCopy(sticks, f_dot[4]),
                      run_time=beat.until("and each", offset=-0.1))
            self.play(TransformMatchingShapes(f_dot[2].copy(), f_dot2[2]), FadeOut(f_dot[2]),
                      run_time=0.9)
            self.play(ReplacementTransform(f_dot[4], f_dot2[4]),
                      run_time=beat.until("A shortcut", offset=-0.1))
            self.play(ReplacementTransform(f_dot[0], f_K[0]),
                      run_time=beat.until("kernel", offset=-0.1))
            self.play(flag(f_K[0]), run_time=beat.remaining(min_time=0.8))
        # tidy: one object for the kernel equation
        kern = VGroup(f_K[0], f_dot[1], f_dot2[2], f_dot[3], f_dot2[4])

        # ================================================================ 12 digits kernel
        f_K7 = formula(r"K(a,b)", "=", r"(a\cdot b", "+", r"1)^{7}", size=EQ)
        f_K7[0].set_color(YELLOW)
        f_K7.move_to(f_dot, aligned_edge=LEFT)
        cost_a = formula(r"256\ \text{multiplications}", size=MATH)
        cost_b = formula(r"\text{not}\ 1.6\times10^{13}", size=MATH, color=GRAY)
        costs = VGroup(cost_a, cost_b).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        costs.next_to(f_K7, DOWN, buff=0.4, aligned_edge=LEFT)
        with self.narrate("For the digits, the kernel is a dot b, plus one, to the seventh "
                          "power. Two hundred fifty-six multiplications stand in for sixteen "
                          "trillion.") as beat:
            self.play(FadeOut(VGroup(sticks, lab_a, lab_b, f_sheet, f_key, f_score)),
                      run_time=0.8)
            beat.wait_until("a dot b", offset=-0.2)
            self.play(TransformMatchingShapes(kern, f_K7), run_time=beat.until("Two hundred"))
            self.play(FadeIn(cost_a, shift=0.1 * UP), run_time=beat.until("stand in"))
            self.play(FadeIn(cost_b, shift=0.1 * UP), run_time=beat.remaining(min_time=0.8))

        # ================================================================ 13 SVM
        gut_ops = ValueTracker(0.0)
        gutters = VGroup()
        for abc in GUT_ABC:
            g = VMobject(stroke_color=YELLOW)

            def upd_g(m, abc=abc):
                ctr, rr = bowl_cut(*abc)
                pts = [st.P(ctr[0] + rr * np.cos(a), ctr[1] + rr * np.sin(a),
                            (ctr[0] + rr * np.cos(a)) ** 2 + (ctr[1] + rr * np.sin(a)) ** 2)
                       for a in np.linspace(0, TAU, 97)]
                m.set_points_as_corners(pts)
                m.set_stroke(width=2.5, opacity=0.75 * gut_ops.get_value())
            upd_g(g)
            g.add_updater(upd_g)
            gutters.add(g)
        sv_rings = VGroup(*[ring(i, color=INK, r=0.16, width=3.5) for i in SV])
        cite2 = citation("Boser, Guyon & Vapnik, 1992 · COLT")
        k7_top = f_K7.copy()
        with self.narrate("In nineteen ninety-two, Boser, Guyon and Vapnik paired kernels with a "
                          "better sheet: the one with the widest gap to its nearest points. Here, "
                          "four points pin it down. They're the support vectors.") as beat:
            self.play(FadeOut(costs), f_K7.animate.scale(0.8).move_to([3.3, 2.9, 0]),
                      *st.view(TILT), FadeIn(cite2), FadeOut(shadow), run_time=1.4)
            beat.wait_until("widest", offset=-0.4)
            self.add(gutters)
            self.bring_to_front(*blue)
            self.play(*go_sheet(SVM_ABC, 1.5), gut_ops.animate.set_value(1.0), run_time=1.5)
            beat.wait_until("four", offset=-0.2)
            self.play(LaggedStart(*[Create(r) for r in sv_rings], lag_ratio=0.2),
                      run_time=beat.until("They're", offset=-0.1))
            self.play(LaggedStart(*[Indicate(dots_all[i], color=INK, scale_factor=1.6)
                                    for i in SV], lag_ratio=0.15),
                      run_time=beat.remaining(min_time=0.8))

        # ================================================================ 14 digits payoff
        cite3 = citation("Cortes & Vapnik, 1995 · Machine Learning")
        rows = [("flat cut, raw pixels", 12.0, GRAY), ("kernel, degree 7", 4.3, YELLOW),
                ("human readers", 2.5, INK)]
        unit = 0.3
        x0 = 1.85
        chart = VGroup()
        bars, vals, names = VGroup(), VGroup(), VGroup()
        for j, (nm, v, colr) in enumerate(rows):
            yy = 0.75 - j * 0.95
            nmt = text(nm, size=LABEL, color=INK)
            nmt.move_to([x0 - 0.25 - nmt.width / 2, yy, 0])
            bar = Rectangle(width=v * unit, height=0.5, stroke_width=0, fill_color=colr,
                            fill_opacity=0.9).move_to([x0 + v * unit / 2, yy, 0])
            val = formula(f"{v:.1f}" + r"\%", size=MATH, color=colr)
            val.next_to(bar, RIGHT, buff=0.18)
            names.add(nmt)
            bars.add(bar)
            vals.add(val)
        base = Line([x0, 1.25, 0], [x0, -1.65, 0], color=GRAY, stroke_width=2)
        ch_title = text("US postal digits · test error", size=LABEL, color=GRAY)
        ch_title.move_to([x0 + 0.6, 1.75, 0])
        chart.add(names, bars, vals, base, ch_title)
        with self.narrate("In nineteen ninety-five, Cortes and Vapnik ran it on US postal "
                          "digits. A flat cut on raw pixels misread twelve percent. The "
                          "seventh-degree kernel misread four point three percent. Human readers "
                          "miss two point five.") as beat:
            self.play(*st.view(SMALL3D), FadeOut(cite2), FadeIn(cite3), run_time=1.2)
            self.play(FadeIn(ch_title), Create(base), run_time=beat.until("A flat", offset=-0.2))
            for j, cue in enumerate(("A flat", "The seventh", "Human")):
                if j:
                    beat.wait_until(cue, offset=-0.2)
                self.play(FadeIn(names[j]), GrowFromEdge(bars[j], LEFT), run_time=0.9)
                self.play(FadeIn(vals[j]), run_time=0.5)
            self.play(Indicate(vals[1], color=YELLOW, scale_factor=1.1),
                      run_time=beat.remaining(min_time=0.8))

        # ================================================================ 15 limit
        choice = SurroundingRectangle(VGroup(f_K7[3], f_K7[4]), color=YELLOW, buff=0.08,
                                      corner_radius=0.06, stroke_width=3)
        choice_lab = text("chosen by hand", size=LABEL, color=YELLOW)
        choice_lab.next_to(choice, DOWN, buff=0.15)
        with self.narrate("Someone still has to choose the kernel. The guess moved from the "
                          "coordinates into the dot product.") as beat:
            self.play(Create(choice), run_time=beat.until("choose", offset=0.2))
            self.play(FadeIn(choice_lab, shift=0.1 * DOWN), run_time=0.8)
            self.play(Indicate(f_K7[2], color=YELLOW, scale_factor=1.08),
                      run_time=beat.remaining(min_time=0.8))

        # ================================================================ 16 landing
        f_end = formula("x^2", "+", "y^2", "=", "c", size=EQ)
        f_end[4].set_color(YELLOW)
        cap = text("one flat cut, seen from above", size=LABEL, color=YELLOW)
        end_grp = VGroup(f_end, cap).arrange(DOWN, buff=0.3)
        end_grp.move_to([3.8, 0.0, 0])
        with self.narrate("So, back to the one straight cut. In this flat picture it can't be "
                          "done. One dimension up, it can, and seen from above, that straight cut "
                          "is this circle.") as beat:
            self.play(FadeOut(VGroup(chart, f_K7, choice, choice_lab, cite3)),
                      *st.view(TILT), run_time=1.2)
            beat.wait_until("One dimension", offset=-0.2)
            self.play(Indicate(sheet, color=YELLOW, scale_factor=1.0), run_time=0.8)
            beat.wait_until("seen from above", offset=-0.5)
            self.play(*st.view(TOP), sheet_op.animate.set_value(0.0),
                      bowl.animate.set_stroke(opacity=0.35),
                      z_axis.animate.set_stroke(opacity=0.0), FadeOut(z_lab),
                      run_time=beat.until("this circle", offset=-0.1))
            self.play(Write(f_end), FadeIn(cap), flag(cut_curve), run_time=beat.remaining(1.2))
        self.hold(0.6)
        self.end_card()


def flag_group(g, color=YELLOW):
    return Indicate(g, color=None, scale_factor=1.15, run_time=1.0)
