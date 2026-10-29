"""Episode 5: Why Random Darts Beat Grids in 100 Dimensions (round 5 cut).

    videos/toolkit/render.sh --preview videos/episodes/005-monte-carlo/scene.py Episode /tmp/ep5.mp4
    videos/toolkit/render.sh videos/episodes/005-monte-carlo/scene.py Episode videos/episodes/005-monte-carlo/final.mp4

All numbers come from data.json (written by sim.py).  Palette: PURPLE grid (and any even,
deterministic design), BLUE darts, YELLOW dimension d, RED error / miss, INK target shape and
true answer, GRAY axes.
"""
from __future__ import annotations

import json
from math import log10
from pathlib import Path

import numpy as np
from manim import *
from sample_space import *
from scipy.spatial import ConvexHull as SciHull      # after manim, which exports its own ConvexHull

D = json.loads((Path(__file__).resolve().parent / "data.json").read_text())
DIMS = D["dims"]
RESCUE_ERR = D["rescue20"]["error_points"]             # 2 values on 19 axes, d = 20

# ------------------------------------------------------------------ geometry
PC_X0, PC_X1, PC_Y0, PC_Y1 = -5.05, 4.35, -1.8, 1.8        # parallel coordinates (cold open)
PC_CX = (PC_X0 + PC_X1) / 2
SQ = 3.6                                                     # 2-D square side
L_C = np.array([-3.5, 0.3, 0.0])
R_C = np.array([3.5, 0.3, 0.0])
# the insight layout: the 2-D square on the left, a 100-axis panel on the right, gauges below
B_L = np.array([-3.5, 1.1, 0.0])
MCX = 3.5
MP_X0, MP_X1 = 0.8, 6.2
MP_Y0, MP_Y1 = B_L[1] - SQ / 2, B_L[1] + SQ / 2
TITLE_Y = 3.35
Y_READ, Y_BAR, Y_RES = -1.62, -2.17, -2.72
BLOCK_Y = 0.85
HIST_Y = -2.0                                                # histogram baseline
HIST_X, HIST_LEN = 3.2, 5.5                                  # histogram centres (+-) and axis length
ML_Y = -0.3                                                  # one-coin number line (built here, base size)
EQ_POS = np.array([-2.55, 2.7, 0.0])                         # the typical-miss formula (walk beat)
PRED_Y = 2.45
EQ_SIZE = 56
BIG = 1.8                                                    # one-coin close-up scale
BIG_C = np.array([0.0, -0.6, 0.0])
SLOT = 0.75                                                  # coin line beside the histograms: 0.75 x close-up
SLOT_C = np.array([0.0, 0.6, 0.0])                           # (at 30 %, above the histograms)
CORNER_C = np.array([5.05, -2.3, 0.0])                       # coin line during the random walk
TITLE_Y2 = 2.85                                              # "2 / 100 dimensions" over the coins
# random walks of sixteen +-1/2 misses: the twelve consecutive 16-dart groups of the two 100-dart runs
# (darts 1-96 of the 2-D run and of the 100-D run); the bold one is darts 17-32 of the 2-D run
WALK_BOLD = 1
W0 = np.array([-5.7, -1.15, 0.0])
W_DX, W_U = 0.36, 0.17
PARK = np.array([4.5, 0.45, 0.0])                           # the measured +-4.8 tag waits here


def pc_pt(i, v, n=100, x0=PC_X0, x1=PC_X1, y0=PC_Y0, y1=PC_Y1):
    return np.array([x0 + (x1 - x0) * i / (n - 1), y0 + v * (y1 - y0), 0.0])


def mp(i, v):
    return pc_pt(i, v, x0=MP_X0, x1=MP_X1, y0=MP_Y0, y1=MP_Y1)


def sq_pt(c, x, y, side=SQ):
    return c + np.array([(x - 0.5) * side, (y - 0.5) * side, 0.0])


def marker(pos, color, filled, r=0.065):
    d = Dot(pos, radius=r, color=color)
    if not filled:
        d.set_fill(color, opacity=0).set_stroke(color, width=2.5)
    return d


def polyline(points, color=BLUE, width=2.5, opacity=1.0):
    return VMobject().set_points_as_corners(points).set_stroke(color, width, opacity).set_fill(opacity=0)


def square_frame(c, side=SQ, names=("input 1", "input 2")):
    p = lambda x, y: sq_pt(c, x, y, side)
    bottom = Line(p(0, 0), p(1, 0), color=AXIS, stroke_width=2.5)
    left = Line(p(0, 0), p(0, 1), color=AXIS, stroke_width=2.5)
    rest = VGroup(Line(p(0, 1), p(1, 1), color=DIM, stroke_width=2),
                  Line(p(1, 0), p(1, 1), color=DIM, stroke_width=2))
    ticks = VGroup(MathTex("0", font_size=MATH_SMALL, color=GRAY).next_to(p(0, 0), DL, buff=0.14),
                   MathTex("1", font_size=MATH_SMALL, color=GRAY).next_to(p(1, 0), DOWN, buff=0.18),
                   MathTex("1", font_size=MATH_SMALL, color=GRAY).next_to(p(0, 1), LEFT, buff=0.18))
    xl = text(names[0], size=27, color=GRAY).next_to(bottom, DOWN, buff=0.2)
    yl = text(names[1], size=27, color=GRAY).rotate(PI / 2).next_to(left, LEFT, buff=0.2)
    g = VGroup(bottom, left, rest, ticks, xl, yl)
    g.bottom, g.left, g.rest, g.ticks, g.xl, g.yl = bottom, left, rest, ticks, xl, yl
    return g


def quarter_disc(corner, R):
    ts = np.linspace(0, PI / 2, 64)
    pts = [corner + R * np.array([np.cos(t), np.sin(t), 0.0]) for t in ts]
    fill = VMobject().set_points_as_corners([corner, *pts, corner])
    fill.set_fill(INK, 0.09).set_stroke(width=0)
    arc = VMobject().set_points_smoothly(pts).set_stroke(INK, 3).set_fill(opacity=0)
    return VGroup(fill, arc)


def ball_inset(o, s, r2d, r3d, a=0.40, b=0.28):
    """A unit square holding the 2-D quarter disc, which becomes the BACK face of a cube; the
    eighth of a ball (radius r3d, centred on the back-bottom-left corner) bulges toward the
    viewer.  Oblique projection (x + a z, y + b z); everything is computed in 3-D and projected."""
    P = lambda x, y, z: o + s * np.array([x + a * z, y + b * z, 0.0])
    Q = lambda x, y, w: P(x, y, 1 - w)                 # w = distance in front of the back face
    ts = np.linspace(0, PI / 2, 48)
    arc = lambda f: VMobject().set_points_smoothly([f(t) for t in ts]).set_fill(opacity=0)
    back_sq = Polygon(P(0, 0, 1), P(1, 0, 1), P(1, 1, 1), P(0, 1, 1)).set_stroke(AXIS, 2).set_fill(opacity=0)
    disc_fill = Polygon(Q(0, 0, 0), *[Q(r2d * np.cos(t), r2d * np.sin(t), 0) for t in ts])
    disc_fill.set_fill(INK, 0.12).set_stroke(width=0)
    disc_arc = arc(lambda t: Q(r2d * np.cos(t), r2d * np.sin(t), 0)).set_stroke(INK, 2.5)

    def at(s):
        """The ball at growth s: s = 0 is the flat 2-D quarter disc (radius r2d) on the back face, s = 1 the
        eighth ball (radius r3d).  One family, so there is only ever one boundary: the back-face arc and
        the silhouette coincide at s = 0 and separate as the ball bulges toward the viewer."""
        r = r2d + (r3d - r2d) * s
        pts = np.array([Q(r * np.sin(p) * np.cos(t), r * np.sin(p) * np.sin(t), s * r * np.cos(p))
                        for t in ts for p in ts] + [Q(0, 0, 0)])
        hull = SciHull(pts[:, :2])
        fill = Polygon(*[pts[i] for i in hull.vertices]).set_fill(INK, 0.12).set_stroke(width=0)
        b_arc = arc(lambda t: Q(r * np.cos(t), r * np.sin(t), 0)).set_stroke(INK, 2.5)
        op = min(1.0, s / 0.35)
        rim_ = VGroup(DashedVMobject(arc(lambda t: Q(r * np.cos(t), 0, s * r * np.sin(t) + 1e-4)), num_dashes=12),
                      DashedVMobject(arc(lambda t: Q(0, r * np.cos(t), s * r * np.sin(t) + 1e-4)), num_dashes=12))
        rim_.set_stroke(AXIS, 1.6, opacity=op)                                     # floor and left-wall edges
        out = Polygon(*[pts[i] for i in hull.vertices]).set_fill(opacity=0).set_stroke(INK, 2.5, opacity=op)
        return VGroup(fill, b_arc, out, rim_)
    dome, back_arc, outline, rim = at(1.0)
    front = VGroup(*[Line(P(*u), P(*v)) for u, v in (
        ((0, 0, 0), (1, 0, 0)), ((1, 0, 0), (1, 1, 0)), ((1, 1, 0), (0, 1, 0)), ((0, 1, 0), (0, 0, 0)),
        ((1, 0, 0), (1, 0, 1)), ((1, 1, 0), (1, 1, 1)), ((0, 1, 0), (0, 1, 1)))]).set_stroke(DIM, 2)
    hidden = DashedLine(P(0, 0, 0), P(0, 0, 1), dash_length=0.06).set_stroke(DIM, 1.6)
    # the cube's centre (1/2, 1/2, 1/2): |c|^2 = 0.75 < r3d^2 = 0.97, so it is inside the ball
    centre = Dot(Q(0.5, 0.5, 0.5), radius=0.13, color=PURPLE).set_fill(opacity=0)
    return dict(P=P, at=at, back_sq=back_sq, disc_fill=disc_fill, disc_arc=disc_arc, dome=dome,
                back_arc=back_arc, outline=outline, rim=rim, edges=VGroup(front, hidden), centre=centre)


def bracket(x0, x1, y, label, color=RED, size=36, side=RIGHT):
    ln = Line([x0, y, 0], [x1, y, 0], color=color, stroke_width=3)
    ends = VGroup(Line([x0, y - 0.1, 0], [x0, y + 0.1, 0], color=color, stroke_width=3),
                  Line([x1, y - 0.1, 0], [x1, y + 0.1, 0], color=color, stroke_width=3))
    lab = label if isinstance(label, Mobject) else MathTex(*label, font_size=size, color=color)
    lab.next_to(ln, side, buff=0.15)
    return VGroup(ln, ends, lab)


def miss_eq(num, den, size=EQ_SIZE):
    """typical miss = num / sqrt(den), split into [lhs, =, frac-with-numerator, sqrt, den, close]."""
    e = MathTex(r"\text{typical miss}", "=", r"\frac{" + num + "}{", r"\sqrt{", den, "}}", font_size=size)
    e[0].set_color(RED)
    e[2][:-1].set_color(RED)
    e[3:5].set_color(BLUE)
    return e


class LiveBracket(VGroup):
    """A +-sd bracket over a histogram whose width, height and number follow two trackers;
    the number is a DecimalNumber and 'pts' a static glyph, so nothing double-exposes."""

    def __init__(self, hx, sd, y, side=RIGHT):
        super().__init__()
        self.hx, self.w, self.yv, self.side = hx, ValueTracker(sd), ValueTracker(y), side
        self.ln = Line(ORIGIN, RIGHT, color=RED, stroke_width=3)
        self.e0 = Line(ORIGIN, UP, color=RED, stroke_width=3)
        self.e1 = Line(ORIGIN, UP, color=RED, stroke_width=3)
        self.num = DecimalNumber(sd * 100, num_decimal_places=1, font_size=36, color=RED)
        self.lab = VGroup(MathTex(r"\pm", font_size=36, color=RED), self.num,
                          MathTex(r"\text{pts}", font_size=36, color=RED))
        self.add(self.ln, VGroup(self.e0, self.e1), self.lab)
        self.refresh()

    def refresh(self, *_):
        a, b = self.hx.n2p(0.5 - self.w.get_value())[0], self.hx.n2p(0.5 + self.w.get_value())[0]
        y = self.yv.get_value()
        self.ln.put_start_and_end_on([a, y, 0], [b, y, 0])
        self.e0.put_start_and_end_on([a, y - 0.1, 0], [a, y + 0.1, 0])
        self.e1.put_start_and_end_on([b, y - 0.1, 0], [b, y + 0.1, 0])
        self.num.set_value(self.w.get_value() * 100)
        self.lab.arrange(RIGHT, buff=0.08).next_to(self.ln, self.side, buff=0.15)
        return self


class Gauge(VGroup):
    """One dart's squared distance from the corner: a readout, a bar that grows to it against a
    dashed INK tick at the ball's r^2, and the resulting bit."""

    def __init__(self, cx, lhs, value, r2, vmax, dec, inside, length=3.0):
        super().__init__()
        x0 = cx - length / 2
        self.x0, self.length, self.vmax = x0, length, vmax
        self.track = Line([x0, Y_BAR, 0], [x0 + length, Y_BAR, 0], color=AXIS, stroke_width=2)
        xt = x0 + length * r2 / vmax
        self.tick = DashedLine([xt, Y_BAR - 0.16, 0], [xt, Y_BAR + 0.16, 0], color=INK, stroke_width=3,
                               dash_length=0.05)
        self.v = ValueTracker(0.0)
        self.bar = Line([x0, Y_BAR, 0], [x0 + 1e-3, Y_BAR, 0], color=BLUE, stroke_width=9)
        self.num = DecimalNumber(value, num_decimal_places=dec, font_size=36, color=BLUE)
        self.lhs = MathTex(lhs, "=", font_size=36)
        self.rel = MathTex("<" if inside else ">", font_size=36)
        # the threshold is the ball's radius squared, written out (the radius grows with d)
        self.rv = MathTex(f"{r2:.{dec}f}", "=", f"{np.sqrt(r2):.2f}^2", font_size=36)
        self.readout = VGroup(self.lhs, self.num, self.rel, self.rv).arrange(RIGHT, buff=0.14)
        self.readout.move_to([cx, Y_READ, 0])
        over = self.readout.get_right()[0] - 6.3
        if over > 0:
            self.readout.shift(LEFT * over)
        self.num.set_value(0)
        self.result = VGroup(text("inside" if inside else "outside", size=28),
                             formula(r"\to 1" if inside else r"\to 0", size=40, color=BLUE))
        self.result.arrange(RIGHT, buff=0.15).move_to([cx, Y_RES, 0])
        self.add(self.track, self.tick, self.bar, self.readout, self.result)

    def follow(self, m):
        v = self.v.get_value()
        self.bar.put_start_and_end_on([self.x0, Y_BAR, 0],
                                      [self.x0 + max(self.length * v / self.vmax, 1e-3), Y_BAR, 0])
        self.num.set_value(v)


class Episode(NarratedScene):
    EPISODE = 5
    TITLE = "Why Random Darts Beat Grids in 100 Dimensions"
    PRONUNCIATIONS = {"Bengio": "/bˈɛnʤiO/", "Ulam": "/ˈulɑm/", "d-th": "/dˈiθ/", "Bergstra": "/bˈɜɹɡstɹɑ/"}
    CADENCE = "shaped"           # gaps follow the sense (PRODUCTION_GUIDE §4, §13.3)
    SPEED = 0.84                 # top of the guide's 0.82-0.84 band (round 6: pays for the added derivation)

    # ================================================================== construct
    def construct(self):
        self.cold_open()
        self.build_2d()
        self.climb()
        self.diagonal()
        self.bits()
        self.spread()
        self.prediction()
        self.payoff()
        self.limit()
        self.landing()
        self.end_card(hold=0.6)

    # ================================================================== helpers
    def wait_beat(self, beat, word, occurrence=1, offset=0.0):
        beat.wait_until(word, occurrence, offset)

    def swap(self, old, *new):
        """After part-by-part transforms, take every piece of `old` off screen and show `new` whole."""
        self.remove(*old.get_family())
        self.add(*new)

    def own(self, *eqs):
        """The parts of one MathTex are spaced by LaTeX itself (radical under a fraction bar, etc.)."""
        for e in eqs:
            self.allow_overlap(e, e, reason="parts of one LaTeX-typeset formula, spaced by LaTeX")

    # ================================================================== 0:00 cold open
    def make_pc(self):
        axes_pc = VGroup(*[Line(pc_pt(i, 0), pc_pt(i, 1), color=AXIS, stroke_width=1.6,
                                stroke_opacity=0.8) for i in range(100)])
        lab0 = MathTex("0", font_size=MATH_SMALL, color=GRAY).next_to(pc_pt(0, 0), LEFT, buff=0.15)
        lab1 = MathTex("1", font_size=MATH_SMALL, color=GRAY).next_to(pc_pt(0, 1), LEFT, buff=0.15)
        in1 = text("input 1", size=27, color=GRAY).next_to(pc_pt(0, 0), DOWN, buff=0.22)
        in1.align_to(pc_pt(0, 0) + LEFT * 0.08, LEFT)
        in100 = text("input 100", size=27, color=GRAY).next_to(pc_pt(99, 0), DOWN, buff=0.22)
        in100.align_to(pc_pt(99, 0) + RIGHT * 0.08, RIGHT)
        n_lab = formula(r"N = 1{,}000{,}000", r"\text{ points}", size=44).move_to([PC_CX - 2.6, 3.12, 0])
        d_lab = formula(r"d = 100", r"\text{ inputs}", size=44).move_to([PC_CX + 2.75, 3.12, 0])
        d_lab[0].set_color(YELLOW)
        return axes_pc, VGroup(lab0, lab1), VGroup(in1, in100), n_lab, d_lab

    def cold_open(self):
        axes_pc, ends, ins, n_lab, d_lab = self.make_pc()
        # first frame: the budget, input 1, and a YELLOW counter that counts the axes as they sweep in
        trk = ValueTracker(1.0)
        for i, a in enumerate(axes_pc):
            a.set_stroke(opacity=0.8 if i == 0 else 0)

        def reveal(m):
            k = trk.get_value()
            for i, a in enumerate(m):
                a.set_stroke(opacity=0.8 * min(1.0, max(0.0, k - i)))
        slot = d_lab[0][2:]                                  # the glyphs "100" of the final label
        d_num = Integer(1, font_size=44, color=YELLOW).move_to(slot, aligned_edge=DL)
        d_num.add_updater(lambda m: m.set_value(min(100, max(1, int(trk.get_value()))))
                          .move_to(slot, aligned_edge=DL))
        d_head = d_lab[0][:2]                                # "d =", kept as one object for the swap below
        self.add(axes_pc, n_lab, d_head, d_num, ends, ins[0])
        opt = text("e.g. an option on 100 stocks", size=27, color=GRAY).move_to([PC_CX, 2.35, 0])
        cite_g0 = citation("Glasserman, 2003 · Monte Carlo Methods in Financial Engineering, Springer")
        enc = text("each line: one input, from 0 to 1", size=27, color=GRAY).move_to([PC_CX, 2.35, 0])
        q_txt = text("grid values per input:", size=30)
        q_mark = formula("?", size=60, color=PURPLE)
        q = VGroup(q_txt, q_mark).arrange(RIGHT, buff=0.25).move_to([PC_CX, -2.72, 0])
        with self.narrate("A million evaluations to price an option on a hundred stocks: an average over a "
                          "hundred inputs. [pause 0.2] Spread them as a grid; that feels thorough. [pause 0.2] How many values "
                          "does each input get? [pause 1.5]") as beat:
            axes_pc.add_updater(reveal)
            self.play(trk.animate(rate_func=linear).set_value(70),
                      run_time=beat.until("option", offset=-0.1, min_time=1.0))
            self.play(trk.animate(rate_func=linear).set_value(100), FadeIn(opt, shift=0.1 * DOWN),
                      FadeIn(cite_g0, shift=0.1 * UP), run_time=beat.until("hundred", end=True, min_time=0.8))
            axes_pc.clear_updaters()
            d_num.clear_updaters()
            self.remove(d_num, d_head)
            self.add(d_lab[0])
            self.play(FadeIn(d_lab[1], shift=0.1 * LEFT), FadeIn(ins[1]), run_time=0.5)
            self.wait_beat(beat, "average", offset=-0.15)
            self.play(swap(opt, enc, run_time=0.7))
            self.play(axes_pc[0].animate(rate_func=there_and_back).set_stroke(INK, width=4, opacity=1),
                      Indicate(ends, color=INK), run_time=beat.until("Spread", offset=-0.1, min_time=0.8))
            levels = VGroup(*[DashedLine(pc_pt(0, v), pc_pt(99, v), color=PURPLE, stroke_width=1.6,
                                         dash_length=0.1).set_opacity(0.55) for v in np.arange(0.1, 0.95, 0.1)])
            self.play(LaggedStart(*[Create(l) for l in levels], lag_ratio=0.12), FadeOut(enc),
                      run_time=beat.until("How", offset=-0.6, min_time=1.0))
            self.play(FadeOut(cite_g0), run_time=0.35)
            self.play(FadeOut(levels), FadeIn(q_txt, shift=0.1 * UP), run_time=beat.until("get", offset=-0.1))
            self.play(FadeIn(q_mark, scale=0.6), run_time=0.6)
        # ---- reveal
        centre = VGroup(*[Dot(pc_pt(i, 0.5), radius=0.05, color=PURPLE) for i in range(100)])
        centre_line = polyline([pc_pt(i, 0.5) for i in range(100)], color=PURPLE, width=3)
        one = formula("1", size=60, color=PURPLE).move_to(q_mark)
        c_lab = text("the centre", size=28, color=PURPLE).next_to(pc_pt(99, 0.5), RIGHT, buff=0.25)
        ghosts = VGroup(*[Dot(pc_pt(i, v), radius=0.05, color=PURPLE, fill_opacity=0.5)
                          for i in range(100) for v in (0.25, 0.75)])
        big = MathTex(r"2^{100}", "=", D["two_pow_100"].replace(",", "{,}"),
                      r"\text{ points}", font_size=40).move_to([0, 2.38, 0])
        big[0].set_color(PURPLE)
        fit(big, width=12.4)
        with self.narrate("One. [pause 0.2] The whole grid is one point: the centre. [pause 0.2] "
                          "Two values per input would take two to the hundredth points. [pause 0.6]") as beat:
            # the "1" lands on the word "One" (the swap is quick; the centre dots keep growing after it)
            self.play(AnimationGroup(swap(q_mark, one, run_time=0.55),
                                     LaggedStart(*[GrowFromCenter(d) for d in centre], lag_ratio=0.03,
                                                 run_time=1.3)))
            self.play(Create(centre_line), run_time=beat.until("centre"))
            self.play(FadeIn(c_lab, shift=0.1 * LEFT), run_time=0.6)
            self.play(LaggedStart(*[FadeIn(g, scale=0.5) for g in ghosts], lag_ratio=0.005),
                      run_time=beat.until("two", 2, offset=-0.05))
            # the 31 digits are written on "two to the hundredth" and then held (>= 1.5 s legible)
            self.play(Write(big), run_time=1.2)
        self.pc = dict(axes=axes_pc, ends=ends, ins=ins, n_lab=n_lab, d_lab=d_lab, q=VGroup(q_txt, one),
                       centre=centre, centre_line=centre_line, c_lab=c_lab)
        # ---- stakes: a real 100-input average, a random point, and the open question
        v = D["dart100"]["x"]
        dart_pts = [pc_pt(i, v[i]) for i in range(100)]
        dart_line = polyline(dart_pts, color=BLUE, width=2.5)
        dart_dots = VGroup(*[Dot(p, radius=0.05, color=BLUE) for p in dart_pts])
        r_lab = VGroup(text("a random point:", size=27, color=BLUE),
                       text("one value per input", size=27, color=GRAY)).arrange(RIGHT, buff=0.2)
        r_lab.move_to([PC_CX, 2.35, 0])
        # two sources on one line, bottom-left: the origin of the method and its standard use in pricing
        cite_m = citation("Metropolis & Ulam, 1949 · JASA;   Glasserman, 2003 · Springer")
        q2_txt = text("a million random points: off by", size=30)
        q2_mark = formula("?", size=60, color=BLUE)
        q2 = VGroup(q2_txt, q2_mark).arrange(RIGHT, buff=0.25).move_to([PC_CX, -2.72, 0])
        with self.narrate("Since Metropolis and Ulam in 1949, the standard tool has been random points, like "
                          "this one. How far off would a million random points land?") as beat:
            self.play(LaggedStart(FadeOut(VGroup(ghosts, big, self.pc["q"]), run_time=0.45),
                                  FadeIn(cite_m, shift=0.1 * UP, run_time=0.45), lag_ratio=0.9), run_time=0.85)
            self.wait_beat(beat, "random", offset=-0.5)
            self.play(Create(dart_line), LaggedStart(*[GrowFromCenter(d) for d in dart_dots], lag_ratio=0.02),
                      run_time=beat.until("like", offset=0.1, min_time=0.8), rate_func=linear)
            self.play(FadeIn(r_lab, shift=0.1 * DOWN), Indicate(dart_line, color=BLUE, scale_factor=1.03),
                      run_time=beat.until("How", offset=-0.4, min_time=0.8))
            self.play(FadeOut(cite_m), run_time=0.35)
            self.play(FadeIn(q2_txt, shift=0.1 * UP), run_time=beat.until("land", offset=-0.2, min_time=0.6))
            self.play(FadeIn(q2_mark, scale=0.6), run_time=0.6)
            self.play(Indicate(q2_mark, color=BLUE, scale_factor=1.25), run_time=beat.remaining(min_time=0.6))
        self.dart_line, self.dart_dots, self.r_lab, self.q2 = dart_line, dart_dots, r_lab, q2

    # ================================================================== 0:38 the 2-D test
    def count_up(self, dots_in, color, n, anchor, run_time):
        """Fill the inside dots one by one while an Integer under the square counts them."""
        trk = ValueTracker(0)
        num = Integer(0, font_size=40, color=color).move_to(anchor, aligned_edge=RIGHT)
        num.add_updater(lambda m: m.set_value(int(round(trk.get_value()))).set_color(color)
                        .move_to(anchor, aligned_edge=RIGHT))
        self.add(num)
        self.play(LaggedStart(*[d.animate.set_fill(color, opacity=1) for d in dots_in], lag_ratio=0.02),
                  trk.animate(rate_func=linear).set_value(n), run_time=run_time)
        num.clear_updaters()
        return num

    def build_2d(self):
        pc = self.pc
        v = D["dart100"]["x"]
        C0 = np.array([0.0, 0.3, 0.0])
        frame_R = square_frame(C0)
        disc_R = quarter_disc(sq_pt(C0, 0, 0), SQ * np.sqrt(D["r2"]["2"]))
        dart1 = marker(sq_pt(C0, v[0], v[1]), BLUE, filled=False, r=0.06)
        truth_t = text("true answer", size=28, color=GRAY).move_to([3.1, 1.15, 0])
        f1 = formula("1", size=44).move_to(sq_pt(C0, 0.3, 0.3))
        f0 = formula("0", size=44).move_to(sq_pt(C0, 0.86, 0.55))
        half = formula(r"\tfrac{1}{2}", size=64).move_to([3.1, 0.3, 0])
        with self.narrate("Start with two inputs. [pause 0.2] Our function is one inside this quarter disc, "
                          "zero outside: its average is exactly one half.") as beat:
            # only the dart's values on inputs 1 and 2 survive: those two dots merge into the 2-D dart
            self.play(FadeOut(VGroup(pc["axes"][2:], pc["ends"], pc["ins"], pc["n_lab"], pc["d_lab"],
                                     pc["centre"], pc["centre_line"], pc["c_lab"],
                                     self.r_lab, self.dart_dots[2:], self.dart_line, self.q2)),
                      self.dart_dots[:2].animate.scale(1.5),
                      run_time=beat.until("two", offset=-0.3, min_time=0.4))
            self.play(ReplacementTransform(pc["axes"][0], frame_R.bottom),
                      ReplacementTransform(pc["axes"][1], frame_R.left),
                      ReplacementTransform(self.dart_dots[:2], dart1),
                      run_time=1.6)
            self.play(Create(frame_R.rest), FadeIn(frame_R.ticks), FadeIn(frame_R.xl),
                      FadeIn(frame_R.yl), run_time=beat.until("one", offset=-0.1))
            self.play(Create(disc_R[1]), FadeIn(disc_R[0]), FadeIn(f1, scale=0.6),
                      run_time=beat.until("zero", offset=-0.1))
            self.play(FadeIn(f0, scale=0.6), run_time=0.5)
            self.wait_beat(beat, "average", offset=-0.2)
            self.play(disc_R[0].animate(rate_func=there_and_back).set_fill(opacity=0.35),
                      run_time=beat.until("exactly", offset=-0.1))
            self.play(FadeIn(truth_t), Write(half), run_time=1.0)
        # ---- grid on the left
        frame_L = square_frame(L_C)
        disc_L = quarter_disc(sq_pt(L_C, 0, 0), SQ * np.sqrt(D["r2"]["2"]))
        g2 = D["grid2d"]
        gdots = VGroup(*[marker(sq_pt(L_C, x, y), PURPLE, False)
                         for x, y in zip(g2["x"], g2["y"])])
        g_in = VGroup(*[d for d, i in zip(gdots, g2["inside"]) if i])
        g_title = text("grid", size=32, color=PURPLE).move_to(L_C + UP * 2.25)
        g_read = formula(str(g2["count"]), r"/100", size=40, color=PURPLE).move_to(L_C + DOWN * 2.76)
        g_err = text("off by 2 points", size=28, color=RED).move_to(L_C + DOWN * 3.3)
        with self.narrate("A grid of a hundred points puts fifty-two inside: two points off.") as beat:
            # the true answer steps out of the way first (it never crosses a moving square); then the square
            # slides right while a copy of its lines and disc slides left for the grid (labels fade in after,
            # so no label is ever doubled)
            self.play(FadeOut(VGroup(truth_t, half), shift=0.15 * UP), FadeOut(f1), FadeOut(f0), run_time=0.25)
            frame_L_lines = VGroup(frame_L.bottom, frame_L.left, frame_L.rest)
            frame_R_lines = VGroup(frame_R.bottom, frame_R.left, frame_R.rest)
            self.play(VGroup(frame_R, disc_R, dart1).animate.shift(R_C - C0),
                      TransformFromCopy(VGroup(frame_R_lines, disc_R), VGroup(frame_L_lines, disc_L)),
                      run_time=0.6)
            truth_t.move_to([0, 1.15, 0])
            half.move_to([0, 0.3, 0])
            self.play(FadeIn(VGroup(frame_L.ticks, frame_L.xl, frame_L.yl)), FadeIn(g_title),
                      FadeIn(truth_t), FadeIn(half),
                      LaggedStart(*[GrowFromCenter(d) for d in gdots], lag_ratio=0.01),
                      run_time=beat.until("puts", offset=-0.05, min_time=0.6))
            # the count lands on the spoken "fifty-two" (it starts on "puts")
            g_num = self.count_up(g_in, PURPLE, g2["count"], g_read[0],
                                  beat.until("fifty", end=True, offset=-0.05, min_time=0.6))
            self.play(FadeIn(g_read[1], shift=0.1 * LEFT), run_time=beat.until("two", offset=-0.1, min_time=0.4))
            self.play(FadeIn(g_err, shift=0.1 * UP), run_time=0.6)
        g_read = VGroup(g_num, g_read[1])
        # ---- darts on the right
        d2 = D["darts2d"]
        ddots = VGroup(dart1, *[marker(sq_pt(R_C, x, y), BLUE, False, r=0.06)
                                for x, y in zip(d2["x"][1:], d2["y"][1:])])
        d_in = VGroup(*[d for d, i in zip(ddots, d2["inside"]) if i])
        d_title = text("random darts", size=32, color=BLUE).move_to(R_C + UP * 2.25)
        d_sim = text("simulated", size=22, color=GRAY).next_to(d_title, RIGHT, buff=0.25)
        d_sim.align_to(d_title, DOWN)
        d_read = formula(str(d2["count"]), r"/100", size=40, color=BLUE).move_to(R_C + DOWN * 2.76)
        d_err = text("off by 6 points", size=28, color=RED).move_to(R_C + DOWN * 3.3)
        with self.narrate("A hundred random darts put forty-four inside: six points off. [pause 0.25] In "
                          "two dimensions, the grid wins.") as beat:
            self.play(FadeIn(d_title), FadeIn(d_sim),
                      LaggedStart(*[FadeIn(d, shift=0.25 * DOWN) for d in ddots[1:]], lag_ratio=0.02),
                      run_time=beat.until("put", offset=-0.05, min_time=0.6))
            # the count lands on the spoken "forty-four" (it starts on "put")
            d_num = self.count_up(d_in, BLUE, d2["count"], d_read[0],
                                  beat.until("forty", end=True, offset=-0.05, min_time=0.6))
            self.play(FadeIn(d_read[1], shift=0.1 * LEFT), run_time=beat.until("six", offset=-0.1, min_time=0.4))
            self.play(FadeIn(d_err, shift=0.1 * UP), run_time=0.6)
            win = SurroundingRectangle(VGroup(g_read, g_err), color=PURPLE, buff=0.07, corner_radius=0.08,
                                       stroke_width=3)
            self.wait_beat(beat, "grid", offset=-0.2)
            self.play(Create(win), run_time=0.7)
        d_read = VGroup(d_num, d_read[1])
        self.sq = dict(frame_L=frame_L, disc_L=disc_L, gdots=gdots, g_title=g_title,
                       frame_R=frame_R, disc_R=disc_R, ddots=ddots, d_title=VGroup(d_title, d_sim))
        self.sq_extra = VGroup(g_read, g_err, d_read, d_err, win)
        self.truth_t, self.half = truth_t, half

    # ================================================================== 1:02 climb at fixed budget
    def make_chart(self, compact=False):
        """The dimension chart.  Full: centred, with the 'values per axis / points used / ball radius' rows.
        Compact: lower-left, no rows, for the laws and the prediction (same data, same colours)."""
        X = lambda d: log10(d) - 0.22                 # axis origin sits at the bottom-left
        Y = lambda err: log10(err) + 3                # 0.001 points -> 0
        xs = [X(d) for d in DIMS]
        if compact:
            ax = axes((0, 1.84), (0, 5), x_length=6.0, y_length=2.55, numbers=False,
                      x_ticks=xs, y_ticks=[0, 1, 2, 3, 4, 5])
            ax.move_to(ORIGIN).shift(np.array([-4.55, -2.2, 0]) - ax.c2p(0, 0))
        else:
            ax = axes((0, 1.84), (0, 5), x_length=7.7, y_length=3.6, numbers=False,
                      x_ticks=xs, y_ticks=[0, 1, 2, 3, 4, 5])
            ax.move_to([0.45, 0.95, 0])
        ax.X, ax.Y = X, Y
        xl = VGroup(*[MathTex(str(d), font_size=MATH_SMALL, color=GRAY).next_to(ax.c2p(x, 0), DOWN, buff=0.24)
                      for d, x in zip(DIMS, xs)])
        yl = VGroup(*[MathTex(s, font_size=MATH_SMALL, color=GRAY).next_to(ax.c2p(0, y), LEFT, buff=0.18)
                      for s, y in zip(["0.001", "0.01", "0.1", "1", "10", "100"], range(6))])
        y_title = text("miss (percentage points)", size=27, color=GRAY)
        y_title.next_to(ax.c2p(0, 5), UP, buff=0.3).align_to(yl, LEFT)
        x_title = text("dimensions", size=27, color=GRAY)
        if compact:
            x_title.next_to(xl[-1], RIGHT, buff=0.35).align_to(xl[-1], DOWN)
            return ax, xl, yl, y_title, x_title
        x_title.move_to([ax.get_center()[0], xl.get_bottom()[1] - 0.28, 0])
        col = [ax.c2p(x, 0)[0] for x in xs]
        ROW_Y = (-2.12, -2.58, -3.04)
        rows1 = VGroup(*[MathTex(str(D["grid"][str(d)]["per_axis"]), font_size=MATH_SMALL, color=PURPLE)
                         .move_to([cx, ROW_Y[0], 0]) for d, cx in zip(DIMS, col)])
        used = {10 ** 6: r"10^6"}
        rows2 = VGroup(*[MathTex(used.get(D["grid"][str(d)]["points_used"],
                                          f"{D['grid'][str(d)]['points_used']:,}".replace(",", "{,}")),
                                 font_size=MATH_SMALL, color=GRAY).move_to([cx, ROW_Y[1], 0])
                         for d, cx in zip(DIMS, col)])
        rows3 = VGroup(*[MathTex(f"{np.sqrt(D['r2'][str(d)]):.2f}", font_size=MATH_SMALL, color=GRAY)
                         .move_to([cx, ROW_Y[2], 0]) for d, cx in zip(DIMS, col)])
        r1t = text("values per axis", size=27, color=PURPLE).next_to([col[0], ROW_Y[0], 0], LEFT, buff=0.45)
        r2t = text("points used", size=27, color=GRAY).next_to([col[0], ROW_Y[1], 0], LEFT, buff=0.45)
        r3t = text("ball radius", size=27, color=GRAY).next_to([col[0], ROW_Y[2], 0], LEFT, buff=0.45)
        r2t.align_to(r1t, RIGHT)
        r3t.align_to(r1t, RIGHT)
        return ax, xl, yl, y_title, x_title, VGroup(r1t, r2t, r3t), rows1, rows2, rows3

    def climb(self):
        ax, xl, yl, y_title, x_title, row_t, rows1, rows2, rows3 = self.make_chart()
        xs = [ax.X(d) for d in DIMS]
        gp = [ax.c2p(x, ax.Y(D["grid"][str(d)]["error_points"])) for d, x in zip(DIMS, xs)]
        dp = [ax.c2p(x, ax.Y(D["darts"][str(d)]["error_points"])) for d, x in zip(DIMS, xs)]
        gdots = [Dot(p, radius=0.085, color=PURPLE) for p in gp]
        ddots = [Dot(p, radius=0.085, color=BLUE) for p in dp]
        gseg = [Line(gp[i], gp[i + 1], color=PURPLE, stroke_width=3) for i in range(5)]
        dseg = [Line(dp[i], dp[i + 1], color=BLUE, stroke_width=3) for i in range(5)]
        truth = VGroup(text("true answer", size=27), formula(r"\tfrac{1}{2}", size=40),
                       text("in every dimension", size=27)).arrange(RIGHT, buff=0.18)
        truth.move_to([0, -2.15, 0])
        cur = DashedLine(ax.c2p(xs[0], 0), ax.c2p(xs[0], 5), color=YELLOW, stroke_width=2,
                         dash_length=0.08).set_opacity(0.7)
        sq = self.sq
        # the square -> cube -> eighth-ball morph runs centred, BEFORE the chart exists
        o = np.array([-1.95, -1.0, 0])
        bi = ball_inset(o, 2.3, np.sqrt(D["r2"]["2"]), np.sqrt(D["r2"]["3"]))
        d_in = MathTex(r"d = 2", font_size=44, color=YELLOW).next_to(bi["P"](1.4, 0.6, 0), RIGHT, buff=0.4)
        d_in3 = MathTex(r"d = 3", font_size=44, color=YELLOW).move_to(d_in)
        # the ball's radius is said and shown: it grows just enough to keep half the box
        rad = ValueTracker(np.sqrt(D["r2"]["2"]))
        rad_num = DecimalNumber(rad.get_value(), num_decimal_places=2, font_size=36, color=GRAY)
        rad_lab = VGroup(text("ball radius", size=27, color=GRAY), rad_num).arrange(RIGHT, buff=0.18)
        rad_lab.next_to(d_in, DOWN, buff=0.35).align_to(d_in, LEFT)
        rad_num.add_updater(lambda m: m.set_value(rad.get_value()))
        rest_L = VGroup(*[sq[k] for k in ("frame_L", "disc_L", "gdots", "g_title")])
        rest_R = VGroup(sq["ddots"], sq["d_title"])
        sqR_lines = VGroup(sq["frame_R"].bottom, sq["frame_R"].left, sq["frame_R"].rest)
        with self.narrate("Now give each a million points, and add inputs. [pause 0.2] The disc becomes a "
                          "ball, grown to cover exactly half the box.") as beat:
            # first the squares' contents clear and the true answer settles below (nothing crosses it);
            # then the darts square's four edges and disc travel, edge to edge, to the cube's back face
            P = bi["P"]
            back_edges = VGroup(Line(P(0, 0, 1), P(1, 0, 1)), Line(P(0, 0, 1), P(0, 1, 1)),
                                VGroup(Line(P(0, 1, 1), P(1, 1, 1)), Line(P(1, 0, 1), P(1, 1, 1))))
            back_edges.set_stroke(AXIS, 2)
            # the squares' contents clear first; only then does the true answer travel (over empty space)
            self.play(FadeOut(rest_L, shift=LEFT * 0.4), FadeOut(rest_R), FadeOut(self.sq_extra),
                      FadeOut(VGroup(sq["frame_R"].ticks, sq["frame_R"].xl, sq["frame_R"].yl)), run_time=0.4)
            self.play(ReplacementTransform(self.half, truth[1]), ReplacementTransform(self.truth_t, truth[0]),
                      FadeIn(truth[2]), run_time=0.5)
            # one square travels: the original leaves the frame as its copy starts moving (never two squares)
            self.remove(*sqR_lines.get_family(), *sq["disc_R"].get_family())
            self.play(TransformFromCopy(sqR_lines, back_edges), TransformFromCopy(sq["disc_R"][0], bi["disc_fill"]),
                      TransformFromCopy(sq["disc_R"][1], bi["disc_arc"]),
                      run_time=beat.until("add", offset=-0.5, min_time=0.8))
            self.remove(*back_edges.get_family())
            self.add(bi["back_sq"])
            self.play(FadeIn(d_in, shift=0.1 * LEFT), FadeIn(rad_lab, shift=0.1 * LEFT), run_time=0.5)
            self.wait_beat(beat, "disc", offset=-0.15)
            # "d = 3" arrives with the depth edges (a swap: the two labels are never superimposed)
            self.play(swap(d_in, d_in3, run_time=0.6), Create(bi["edges"]), run_time=0.6)
            # the disc itself bulges into the ball: one family of shapes, so there is only ever one boundary
            # (the flat disc at s = 0 is drawn exactly where the 2-D disc was; it never leaves the cube)
            grow = ValueTracker(0.0)
            ball = bi["at"](0.0)
            self.remove(*bi["disc_fill"].get_family(), *bi["disc_arc"].get_family())
            self.add(ball)
            ball.add_updater(lambda m: m.become(bi["at"](grow.get_value())))
            self.play(grow.animate.set_value(1.0), rad.animate.set_value(np.sqrt(D["r2"]["3"])),
                      run_time=beat.until("cover", offset=-0.2, min_time=1.0))
            ball.clear_updaters()
            rad_num.clear_updaters()
            self.remove(*ball.get_family())
            self.add(bi["dome"], bi["back_arc"], bi["outline"], bi["rim"])
            self.wait_beat(beat, "half", offset=-0.2)
            self.play(flag(truth, color=INK), bi["dome"].animate(rate_func=there_and_back).set_fill(opacity=0.35),
                      run_time=beat.remaining(min_time=0.8))
        centre = bi["centre"]
        inset = VGroup(bi["back_sq"], bi["dome"], bi["back_arc"], bi["edges"], bi["rim"],
                       bi["outline"], centre)

        # ---- step through dimensions
        # the grid's line is named the moment its first point appears; the darts join later, on "darts"
        g_name = text("grid", size=27, color=PURPLE).next_to(gp[3], DR, buff=0.2)

        def step(i):
            anims = [cur.animate.move_to(ax.c2p(xs[i], 2.5)), xl[i].animate.set_color(YELLOW),
                     FadeIn(rows1[i], shift=0.15 * UP), FadeIn(rows2[i], shift=0.15 * UP),
                     FadeIn(rows3[i], shift=0.15 * UP), GrowFromCenter(gdots[i])]
            if i:
                anims += [xl[i - 1].animate.set_color(GRAY), Create(gseg[i - 1])]
            if i == 3:
                anims += [FadeIn(g_name, shift=0.1 * LEFT)]
            return anims

        truth_top = VGroup(text("true answer", size=27), formula(r"\tfrac{1}{2}", size=40),
                           text("in every dimension", size=27)).arrange(RIGHT, buff=0.18)
        truth_top.move_to([0, 3.3, 0]).align_to([6.3, 0, 0], RIGHT)
        thumb_c = np.array([5.42, 2.08, 0])
        with self.narrate("Per axis, the grid gets a thousand values in two dimensions, then a hundred, ten, "
                          "three.") as beat:
            # the ball shrinks to a thumbnail beside the true answer; only then is the chart drawn
            self.play(LaggedStart(
                AnimationGroup(inset.animate.scale(0.48).move_to(thumb_c).fade(0.6), FadeOut(d_in3, run_time=0.4),
                               FadeOut(rad_lab, run_time=0.4),
                               FadeOut(truth, shift=0.1 * DOWN), FadeIn(row_t, shift=0.15 * UP)),
                AnimationGroup(Create(ax), FadeIn(xl), FadeIn(yl), FadeIn(y_title), FadeIn(x_title),
                               FadeIn(truth_top, shift=0.1 * DOWN)),
                lag_ratio=0.5), run_time=beat.until("thousand", offset=-0.65, min_time=1.1))
            self.play(FadeIn(cur), Indicate(row_t[0], color=PURPLE, scale_factor=1.05), run_time=0.35)
            for i, w in enumerate(["thousand", "hundred", "ten", "three"]):
                self.wait_beat(beat, w, offset=-0.3)
                self.play(*step(i), run_time=0.55)
        g_says = formula(r"\text{grid says } 1.000", size=36, color=PURPLE)
        gx_mid = (gp[4][0] + gp[5][0]) / 2
        g_says.move_to([gx_mid, gp[4][1] + 0.86, 0])
        off50 = text("50 points off", size=28, color=RED).move_to([gx_mid, gp[4][1] + 0.37, 0])
        c_note = VGroup(text("centre is", size=27, color=PURPLE), text("inside the ball", size=27, color=PURPLE))
        c_note.arrange(DOWN, buff=0.1, aligned_edge=RIGHT)
        c_note.next_to(inset, LEFT, buff=0.3).set_y(centre.get_y())
        with self.narrate("From twenty dimensions on, just the centre, inside the ball. "
                          "[pause 0.15] So the grid's estimate is the whole box. Fifty points off. [pause 0.8]") as beat:
            self.play(cur.animate.move_to(ax.c2p(xs[4], 2.5)), xl[4].animate.set_color(YELLOW),
                      xl[3].animate.set_color(GRAY), FadeIn(rows1[4], shift=0.15 * UP),
                      FadeIn(rows2[4], shift=0.15 * UP), FadeIn(rows3[4], shift=0.15 * UP),
                      run_time=beat.until("on", offset=-0.1, min_time=0.5))
            self.play(cur.animate.move_to(ax.c2p(xs[5], 2.5)), xl[5].animate.set_color(YELLOW),
                      xl[4].animate.set_color(GRAY), FadeIn(rows1[5], shift=0.15 * UP),
                      FadeIn(rows2[5], shift=0.15 * UP), FadeIn(rows3[5], shift=0.15 * UP),
                      run_time=beat.until("just", offset=-0.1, min_time=0.5))
            self.play(Indicate(rows1[4], color=PURPLE), Indicate(rows1[5], color=PURPLE), FadeOut(cur),
                      xl[5].animate.set_color(GRAY), FadeOut(truth_top), FadeIn(c_note, shift=0.1 * LEFT),
                      centre.animate.set_fill(opacity=1).set_stroke(opacity=1),
                      run_time=beat.until("inside", offset=-0.15, min_time=0.8))
            self.play(Indicate(centre, color=PURPLE, scale_factor=1.8),
                      run_time=beat.until("So", offset=-0.1, min_time=0.8))
            self.play(FadeOut(c_note, shift=0.1 * UP), run_time=0.4)
            self.wait_beat(beat, "estimate", offset=-0.35)
            # the centre is the grid's whole estimate: the dot itself flies onto the chart
            self.play(TransformFromCopy(centre, gdots[4]), TransformFromCopy(centre, gdots[5]),
                      Create(gseg[3]), Create(gseg[4]), FadeIn(g_says, shift=0.1 * DOWN), run_time=0.9)
            self.play(FadeOut(inset), run_time=0.4)
            self.wait_beat(beat, "fifty", offset=-0.1)
            self.play(FadeIn(off50, shift=0.1 * UP), run_time=0.6)
        # ---- the fairest rescue: spend half the budget on two values for 19 of the 20 axes
        rp = ax.c2p(xs[4], ax.Y(RESCUE_ERR))
        r_dot = Circle(radius=0.085, color=PURPLE, stroke_width=3).move_to(gp[4])
        trail = DashedLine(gp[4], rp, color=PURPLE, stroke_width=2, dash_length=0.05).set_opacity(0.7)
        # two lines beside the dot (what it is, how far off it lands); its cost goes into the table's
        # "points used" cell for d = 20
        r_how = text("2 values on 19 axes", size=27, color=PURPLE)
        r_lab = VGroup(text("18 points off", size=27, color=RED))
        r_stack = VGroup(r_how, r_lab[0]).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        r_stack.next_to(rp, RIGHT, buff=0.3)
        r_stack.shift(UP * (rp[1] + 0.05 - r_stack.get_top()[1]))     # stays under the grid's 50-point line
        r_cost = MathTex(r"524{,}288", font_size=MATH_SMALL, color=PURPLE).move_to(rows2[4])
        r_cost.align_to(rows2[4], LEFT).shift(RIGHT * 0.05)
        d_lab = VGroup(text("darts", size=28, color=BLUE), text("(simulated)", size=22, color=GRAY))
        d_lab.arrange(DOWN, buff=0.08).next_to(ddots[5], RIGHT, buff=0.25)
        with self.narrate("Even two values on nineteen axes: eighteen points off. The darts stay "
                          "under a tenth of a point.") as beat:
            # the rescue dot is the subject: the grid's "says 1.000" leaves, the table steps back to 30 %
            table = VGroup(row_t, rows1, *[r for i, r in enumerate(rows2) if i != 4], rows3)
            self.play(FadeOut(g_says), GrowFromCenter(r_dot), FadeIn(r_how, shift=0.1 * LEFT),
                      table.animate.set_opacity(0.3), rows2[4].animate.set_opacity(0.3),
                      run_time=beat.until("nineteen", offset=-0.1, min_time=0.8))
            self.play(r_dot.animate.move_to(rp), Create(trail), swap(rows2[4], r_cost, run_time=0.7),
                      run_time=beat.until("eighteen", offset=-0.15, min_time=0.7))
            self.play(FadeIn(r_lab[0], shift=0.1 * LEFT), run_time=0.6)
            # the darts' line arrives only now, all at once, with its name
            self.wait_beat(beat, "darts", offset=-0.25)
            self.play(LaggedStart(*[AnimationGroup(GrowFromCenter(ddots[i]),
                                                   *([Create(dseg[i - 1])] if i else []))
                                    for i in range(6)], lag_ratio=0.5),
                      FadeIn(d_lab, shift=0.1 * LEFT), run_time=1.2)
            self.play(Indicate(yl[2], color=BLUE, scale_factor=1.4),
                      *[Indicate(d, color=BLUE) for d in ddots], run_time=beat.remaining(min_time=0.8))
        # (the d = 20 "points used" cell left with the swap: it is not faded out again later)
        self.chart_body = VGroup(ax, xl, yl, y_title, x_title, row_t, rows1,
                                 *[r for i, r in enumerate(rows2) if i != 4], rows3, trail, r_dot, r_lab,
                                 r_how, d_lab, r_cost, g_name)
        self.chart_top = VGroup(off50)
        self.rescue = VGroup(trail, r_dot, r_lab, r_how)
        self.chart_ax = ax
        self.chart_gp, self.chart_dp = gp, dp
        self.chart_xl = xl
        self.chart_gline = VGroup(*gseg, *gdots)
        self.chart_dline = VGroup(*dseg, *ddots)
        self.chart_ddots = VGroup(*ddots)

    # ================================================================== 1:30 the diagonal: more values per axis is not the fix
    def diagonal(self):
        sq = self.sq
        dart_sq = VGroup(sq["frame_R"], sq["disc_R"], sq["ddots"])
        dart_sq.shift(B_L - R_C)                 # (off screen) the darts square returns on the left
        sq_target = dart_sq.copy()
        sq_dim = sq_target.copy().fade(0.75)
        m_axes = VGroup(*[Line(mp(i, 0), mp(i, 1), color=DIM, stroke_width=1.2, stroke_opacity=0.8)
                          for i in range(100)])
        m_lab = VGroup(MathTex("0", font_size=MATH_SMALL, color=GRAY).next_to(mp(0, 0), LEFT, buff=0.18),
                       MathTex("1", font_size=MATH_SMALL, color=GRAY).next_to(mp(0, 1), LEFT, buff=0.18))
        t2 = text("2 dimensions", size=32, t2c={"2": YELLOW}).move_to([B_L[0], TITLE_Y, 0])
        t100 = text("100 dimensions", size=32, t2c={"100": YELLOW}).move_to([MCX, TITLE_Y, 0])
        # the misconception's picture: the darts' 100 shadows on one axis, 100 distinct values
        rail_y = B_L[1] - SQ / 2 - 0.8
        rail = Line(sq_pt(B_L, 0, 0), sq_pt(B_L, 1, 0), color=AXIS, stroke_width=2.5).set_y(rail_y)
        d_ticks = VGroup(*[Line([d.get_x(), rail_y - 0.13, 0], [d.get_x(), rail_y + 0.13, 0], color=BLUE,
                                stroke_width=2) for d in sq["ddots"]])
        d_vals = formula(r"100", r"\text{ values on one axis}", size=36, color=BLUE)
        d_vals.next_to(rail, DOWN, buff=0.3)
        under = VGroup(sq["frame_R"].xl, sq["frame_R"].ticks[0], sq["frame_R"].ticks[1])
        dg = D["diag100"]
        ts = (np.arange(26) + 0.5) / 26
        flat = VGroup(*[Line(mp(0, t), mp(99, t), color=PURPLE, stroke_width=2.2) for t in ts])
        level = DashedLine(mp(0, dg["t_max"]) + LEFT * 0.05, mp(99, dg["t_max"]) + RIGHT * 0.05, color=INK,
                           stroke_width=2.5, dash_length=0.1)
        diag_lab = formula(r"10^6\text{ points on the diagonal}", size=36, color=PURPLE).move_to([MCX, Y_READ, 0])
        res = VGroup(text(f"{dg['estimate'] * 100:.1f}% inside:", size=28),
                     text(f"{dg['error_points']:.1f} points off", size=28, color=RED)).arrange(RIGHT, buff=0.2)
        res.move_to([MCX, Y_BAR - 0.1, 0])
        # one flat line first: a point (t, t, ..., t) of the diagonal, drawn on the 100 axes
        k1 = 8                                                       # t = 0.33, inside the ball
        one_pt = VGroup(text("one point:", size=27, color=PURPLE),
                        MathTex(r"(t, t, \dots, t)", font_size=36, color=PURPLE)).arrange(DOWN, buff=0.12,
                                                                                         aligned_edge=RIGHT)
        one_pt.next_to(mp(0, ts[k1]), LEFT, buff=0.42)
        edge_lab = text("ball’s edge", size=27).next_to(mp(0, dg["t_max"]), LEFT, buff=0.42)
        rest = VGroup(*[l for i, l in enumerate(flat) if i != k1])
        # in the breath after the climb: the chart clears, then the chart's 2-D darts point opens back
        # into the darts square (the chart is gone before the square is large)
        # the 100-axis panel waits on the right at low strength (context), so no half of the frame is empty
        m_axes.set_stroke(opacity=0.3)
        t100.set_opacity(0.3)
        self.play(LaggedStart(
            FadeOut(VGroup(self.chart_body, self.chart_top, self.chart_gline, self.chart_dline), run_time=0.35),
            AnimationGroup(GrowFromPoint(dart_sq, self.chart_dp[0]), FadeIn(t2, shift=0.1 * DOWN),
                           Create(m_axes, lag_ratio=0.01), FadeIn(t100), run_time=0.6),
            lag_ratio=0.5), run_time=0.78)
        with self.narrate("Maybe darts win by giving every axis more values. [pause 0.8] A million points on the "
                          "diagonal give every axis a million values, and still miss by eight points: their "
                          "coordinates move in lockstep. [pause 0.3]") as beat:
            # the misconception gets its picture at once: the darts' shadows drop on "darts win", and the
            # count "100 values on one axis" is legible for about two seconds before the diagonal starts
            self.play(Create(rail), run_time=beat.until("darts", offset=-0.1, min_time=0.35))
            self.play(TransformFromCopy(sq["ddots"], d_ticks), under.animate.set_opacity(0.2),
                      run_time=beat.until("by", offset=-0.1, min_time=0.7))
            self.play(FadeIn(d_vals, shift=0.1 * UP), under.animate.set_opacity(1), run_time=0.6)
            # the label holds through "giving every axis more values" and the breath after it (about 2.6 s)
            self.wait_beat(beat, "million", offset=-0.85)
            # the 100-axis panel: a million points on the diagonal; the misconception's picture stays as dimmed
            # context with its square
            mis = VGroup(rail, d_ticks, d_vals)
            self.play(mis.animate.set_opacity(0.25), Transform(dart_sq, sq_dim), t2.animate.set_opacity(0.25),
                      t100.animate.set_opacity(1), m_axes.animate.set_stroke(opacity=0.8), FadeIn(m_lab),
                      run_time=beat.until("million", offset=-0.1, min_time=0.8))
            # one point of the diagonal, alone, for over a second: a flat line on the 100 axes
            self.play(FadeIn(diag_lab, shift=0.1 * UP), Create(flat[k1]), FadeIn(one_pt, shift=0.1 * RIGHT),
                      run_time=beat.until("give", offset=-0.1, min_time=0.8))
            self.play(LaggedStart(*[Create(l) for l in rest], lag_ratio=0.08),
                      run_time=beat.until("million", 2, offset=-0.2, min_time=0.8), rate_func=linear)
            self.play(m_axes.animate(rate_func=there_and_back).set_stroke(PURPLE, width=2.2, opacity=1),
                      run_time=beat.until("and", offset=-0.2, min_time=0.6))
            # lines below the ball's edge stay solid (inside); those above turn dashed (outside)
            outside = [l for l, t in zip(flat, ts) if t > dg["t_max"]]
            dashed = VGroup(*[DashedLine(l.get_start(), l.get_end(), dash_length=0.08, color=PURPLE,
                                         stroke_width=2.2).set_opacity(0.45) for l in outside])
            self.play(Create(level), FadeIn(edge_lab, shift=0.1 * RIGHT),
                      *[ReplacementTransform(l, d) for l, d in zip(outside, dashed)],
                      run_time=beat.until("by", 2, offset=0.0, min_time=0.6))
            self.play(FadeIn(res, shift=0.1 * UP), run_time=beat.until("points", 2, offset=0.0, min_time=0.4))
            # lockstep: one diagonal point slides as a whole; all 100 coordinates change together
            self.wait_beat(beat, "coordinates", offset=-0.15)
            dy = (0.86 - ts[k1]) * (MP_Y1 - MP_Y0)
            self.play(flat[k1].animate(rate_func=there_and_back).shift(UP * dy).set_stroke(width=5),
                      Indicate(one_pt[1], color=PURPLE, scale_factor=1.1),
                      run_time=beat.until("lockstep", end=True, min_time=1.2))
        self.diag_line = flat[k1]                    # stays (dimmed) to contrast with the dart's jagged line
        flat = VGroup(*[l for i, (l, t) in enumerate(zip(flat, ts)) if t <= dg["t_max"] and i != k1], *dashed)
        self.t2, self.t100, self.sq_target = t2, t100, sq_target
        self.panel = VGroup(m_axes, m_lab)
        self.diag_stuff = VGroup(flat, level, diag_lab, res, one_pt, edge_lab, mis)

    # ================================================================== 2:13 one bit per dart
    def bits(self):
        sq = self.sq
        dart_sq = VGroup(sq["frame_R"], sq["disc_R"], sq["ddots"])
        W = D["darts100d"]["x"]
        hero = polyline([mp(i, W[0][i]) for i in range(100)], BLUE, 3.0, 1.0)
        dart1 = sq["ddots"][0]
        ring = Circle(radius=0.17, color=BLUE, stroke_width=3).move_to(dart1.get_center())
        gL = Gauge(B_L[0], r"x_1^2+x_2^2", D["dart2d_sum_sq"], D["r2"]["2"], 2.0, 2, inside=False)
        gR = Gauge(MCX, r"x_1^2+\dots+x_{100}^2", D["dart100"]["sum_sq"], D["r2"]["100"], 40.0, 1, inside=True)
        disc_fill = sq["disc_R"][0]
        diag_line = self.diag_line
        with self.narrate("A dart's coordinates are drawn independently and uniformly. [pause 0.3] So it lands "
                          "inside with a chance equal to the answer, in any dimension. [pause 0.4] Each dart is a "
                          "coin flip. [pause 0.6]") as beat:
            self.play(FadeOut(self.diag_stuff), Transform(dart_sq, self.sq_target), Create(ring), Create(hero),
                      diag_line.animate.set_stroke(opacity=0.3), self.t2.animate.set_opacity(1),
                      run_time=beat.until("drawn", offset=-0.1, min_time=1.0))
            # independent coordinates: a jagged line, not the diagonal's flat one
            self.play(hero.animate(rate_func=there_and_back).set_stroke(width=5),
                      diag_line.animate(rate_func=there_and_back).set_stroke(opacity=0.8),
                      run_time=beat.until("so", offset=-0.1, min_time=0.8))
            self.play(Create(gL.track), Create(gL.tick), FadeIn(gL.lhs), FadeIn(gL.num), FadeOut(diag_line),
                      run_time=0.4)
            gL.bar.add_updater(gL.follow)
            self.add(gL.bar)
            self.play(gL.v.animate(rate_func=linear).set_value(D["dart2d_sum_sq"]),
                      run_time=beat.until("chance", offset=-0.1, min_time=0.8))
            gL.bar.clear_updaters()
            self.play(FadeIn(gL.rel), FadeIn(gL.rv), FadeIn(gL.result, shift=0.1 * UP), run_time=0.5)
            self.play(Create(gR.track), Create(gR.tick), FadeIn(gR.lhs), FadeIn(gR.num),
                      hero.animate.set_stroke(width=4.5), run_time=0.4)
            gR.bar.add_updater(gR.follow)
            self.add(gR.bar)
            self.play(gR.v.animate(rate_func=linear).set_value(D["dart100"]["sum_sq"]),
                      disc_fill.animate(rate_func=there_and_back).set_fill(opacity=0.35),
                      run_time=beat.until("any", offset=-0.1, min_time=1.0))
            gR.bar.clear_updaters()
            self.play(FadeIn(gR.rel), FadeIn(gR.rv), FadeIn(gR.result, shift=0.1 * UP),
                      hero.animate.set_stroke(width=3.0), run_time=0.5)

            def block(c):
                return [c + np.array([(k % 10 - 4.5) * 0.17, (4.5 - k // 10) * 0.17, 0]) for k in range(100)]
            bL, bR = block(np.array([B_L[0], BLOCK_Y, 0])), block(np.array([MCX, BLOCK_Y, 0]))
            coinsL = VGroup(*[marker(p, BLUE, bool(i), r=0.06) for p, i in zip(bL, D["darts2d"]["inside"])])
            coinsR = VGroup(*[marker(p, BLUE, bool(i), r=0.06) for p, i in zip(bR, D["darts100d"]["inside"])])
            kL = formula(str(D["darts2d"]["count"]), r"/100", size=40, color=BLUE).move_to([B_L[0], -0.8, 0])
            kR = formula(str(D["darts100d"]["count"]), r"/100", size=40, color=BLUE).move_to([MCX, -0.8, 0])
            # the square's outline will become the 2-D coin block's bounding box
            frame = sq["frame_R"]
            frame_lines = VGroup(frame.bottom, frame.left, frame.rest[0], frame.rest[1])
            bb = SurroundingRectangle(coinsL, buff=0.12)
            c4 = [bb.get_corner(DL), bb.get_corner(DR), bb.get_corner(UR), bb.get_corner(UL)]
            box = VGroup(Line(c4[0], c4[1]), Line(c4[0], c4[3]), Line(c4[3], c4[2]), Line(c4[1], c4[2]))
            box.set_stroke(AXIS, 2, opacity=0.3)
            # the other 99 darts of the 100-D run, each one a faint polyline on the panel
            others = VGroup(*[polyline([mp(i, W[k][i]) for i in range(100)], BLUE, 1.0, 0.07) for k in range(1, 100)])
            self.wait_beat(beat, "each", offset=-0.3)
            # everything but each dart's verdict steps away; the verdict becomes that dart's coin
            # (on "coin flip"), then the other 99 darts follow
            self.play(FadeOut(VGroup(frame.ticks, frame.xl, frame.yl, sq["disc_R"], ring)),
                      frame_lines.animate.set_stroke(opacity=0.3),
                      *[FadeOut(VGroup(g.track, g.tick, g.bar, g.readout)) for g in (gL, gR)], run_time=0.4)
            # each verdict becomes its dart's coin: the 2-D dart dot moves to its slot; the 100-D dart's
            # polyline shrinks rigidly (same shape, smaller) onto its slot while the coin grows there.
            # No FadeTransform between unlike shapes (a polyline stretched into a dot reads as a blob).
            def shrink_into(line, coin):
                return AnimationGroup(line.animate.scale(0.04).move_to(coin.get_center()).set_stroke(opacity=0),
                                      GrowFromCenter(coin))
            self.play(FadeOut(gL.result, shift=(coinsL[0].get_center() - gL.result.get_center()) * 0.5, scale=0.4),
                      FadeOut(gR.result, shift=(coinsR[0].get_center() - gR.result.get_center()) * 0.5, scale=0.4),
                      ReplacementTransform(dart1, coinsL[0]), shrink_into(hero, coinsR[0]), FadeIn(others),
                      run_time=beat.until("coin", offset=0.1, min_time=0.7))
            self.remove(hero)
            # then the other 99 darts of each run follow: 2-D dots slide into the block, each faint 100-D
            # polyline shrinks into its own coin
            self.play(*[ReplacementTransform(d, c) for d, c in zip(sq["ddots"][1:], coinsL[1:])],
                      LaggedStart(*[shrink_into(o, c) for o, c in zip(others, coinsR[1:])], lag_ratio=0.01),
                      Transform(frame_lines, box), FadeOut(self.panel),
                      run_time=beat.remaining(min_time=1.0))
            self.remove(*others)
            self.play(FadeIn(kL, shift=0.1 * UP), FadeIn(kR, shift=0.1 * UP), run_time=0.6)
        # ---- one coin, close up: always exactly a half from its average
        ml = Line([-0.85, ML_Y, 0], [0.85, ML_Y, 0], color=AXIS, stroke_width=2.5)
        ml_t = VGroup(MathTex("0", font_size=MATH_SMALL, color=GRAY).next_to([-0.85, ML_Y, 0], DOWN, buff=0.24),
                      MathTex("1", font_size=MATH_SMALL, color=GRAY).next_to([0.85, ML_Y, 0], DOWN, buff=0.24))
        cap = text("one yes/no dart", size=28, color=GRAY).move_to([0, 1.85, 0])     # not scaled with the line
        mean = DashedLine([0, ML_Y - 0.12, 0], [0, ML_Y + 0.6, 0], color=INK, stroke_width=2,
                          dash_length=0.07).set_opacity(0.6)
        mean_lab = MathTex(r"\tfrac{1}{2}", font_size=36, color=INK).next_to([0, ML_Y, 0], DOWN, buff=0.15)
        coin0 = marker([-0.85, ML_Y, 0], BLUE, False, r=0.075)
        coin1 = marker([0.85, ML_Y, 0], BLUE, True, r=0.075)
        coin0b = marker([-0.85, ML_Y, 0], BLUE, False, r=0.075)
        by = ML_Y + 0.32

        def miss(xc):
            lab = MathTex(r"\tfrac{1}{2}", font_size=36, color=RED)
            return bracket(min(xc, 0), max(xc, 0), by, lab, side=UP)
        miss1, miss0 = miss(0.85), miss(-0.85)
        small_c = np.array([0.0, ML_Y, 0.0])

        def big(*ms):
            for m in ms:
                m.scale(BIG, about_point=small_c).shift(BIG_C - small_c)
        big(ml, ml_t, mean, mean_lab, coin0, coin1, coin0b, miss1, miss0)
        t2, t100 = self.t2, self.t100
        with self.narrate("A flip is zero or one. [pause 0.15] Its average is a half, so every flip misses "
                          "by exactly a half.") as beat:
            self.play(TransformFromCopy(coinsL[0], coin0), Create(ml), FadeIn(ml_t), FadeIn(cap),
                      VGroup(t2, t100).animate.set_y(TITLE_Y2),
                      run_time=beat.until("or", offset=-0.1, min_time=0.8))
            self.play(Transform(coin0, coin1), run_time=beat.until("Its", offset=-0.1, min_time=0.5))
            self.play(Create(mean), FadeIn(mean_lab, shift=0.1 * UP), run_time=beat.until("so", offset=-0.1, min_time=0.6))
            self.wait_beat(beat, "misses", offset=-0.2)
            self.play(GrowFromPoint(miss1, miss1[0].get_center()), run_time=0.6)
            self.wait_beat(beat, "exactly", offset=-0.1)
            self.play(Transform(coin0, coin0b), Transform(miss1, miss0), run_time=0.8)
        self.coins = (coinsL, kL, coinsR, kR)
        self.coin_box = frame_lines
        self.coin_line = VGroup(ml, ml_t, mean, mean_lab, coin0, miss1)
        self.coin_cap = cap
        self.coin_half = miss1[2]
        self.coin_miss = miss1

    # ================================================================== 2:26 the spread
    def spread(self):
        coinsL, kL, coinsR, kR = self.coins
        H = D["hist"]
        lo, hi = 0.3, 0.7

        def hist_axes(cx, scale_label=True):
            hx = NumberLine(x_range=[lo, hi, 0.1], length=HIST_LEN, color=AXIS, stroke_width=2.5,
                            include_tip=False, tick_size=0.06)
            hx.move_to([cx, HIST_Y, 0])
            labs = VGroup(*[MathTex(f"{round(t * 100)}\\%", font_size=MATH_SMALL, color=GRAY)
                            .next_to(hx.n2p(t), DOWN, buff=0.18) for t in (0.3, 0.4, 0.5, 0.6, 0.7)])
            sx = hx.n2p(0.312)[0]
            bar = VGroup(Line([sx, HIST_Y, 0], [sx, HIST_Y + 0.5, 0], color=AXIS, stroke_width=2),
                         Line([sx - 0.05, HIST_Y + 0.5, 0], [sx + 0.05, HIST_Y + 0.5, 0], color=AXIS, stroke_width=2))
            bar_lab = text("10 runs", size=22, color=GRAY).next_to(bar, UP, buff=0.12)
            return hx, labs, (VGroup(bar, bar_lab) if scale_label else VGroup(bar))
        hL, labL, scL = hist_axes(-HIST_X)
        hR, labR, scR = hist_axes(HIST_X, scale_label=False)
        x_name = text("estimate from one experiment", size=27, color=GRAY).move_to([0, -2.95, 0])
        truthL = DashedLine(hL.n2p(0.5), hL.n2p(0.5) + UP * 2.9, color=INK, stroke_width=2,
                            dash_length=0.07).set_opacity(0.6)
        truthR = DashedLine(hR.n2p(0.5), hR.n2p(0.5) + UP * 2.9, color=INK, stroke_width=2,
                            dash_length=0.07).set_opacity(0.6)
        unit = 0.05                                          # height per run in a 1-point bin
        edges = np.round(np.arange(lo, hi + 1e-9, 0.01), 4)

        def counts(est, k):
            e = np.asarray(est[:k])
            idx = np.clip(np.floor((e - lo) / 0.01 + 1e-6).astype(int), 0, len(edges) - 2)
            return np.bincount(idx, minlength=len(edges) - 1)

        def make_bars(hx, est, k, color=BLUE):
            c = counts(est, k)
            w = hx.get_unit_size() * 0.01
            return VGroup(*[Rectangle(width=w * 0.86, height=max(n * unit, 0.001), stroke_width=0,
                                      fill_color=color, fill_opacity=0.85 if n else 0)
                            .move_to(hx.n2p(edges[j] + 0.005), aligned_edge=DOWN)
                            for j, n in enumerate(c)])
        estL, estR = H["100_2"]["estimates"], H["100_100"]["estimates"]
        runs = ValueTracker(1)
        barsL = make_bars(hL, estL, 1)
        barsR = make_bars(hR, estR, 1)

        def upd(hx, est):
            def f(m):
                c = counts(est, int(round(runs.get_value())))
                for r, n in zip(m, c):
                    r.stretch_to_fit_height(max(n * unit, 0.001))
                    r.move_to([r.get_x(), HIST_Y, 0], aligned_edge=DOWN)
                    r.set_fill(opacity=0.85 if n else 0)
            return f
        n_txt = formula("N", r"= 100", r"\text{ darts}", size=36, color=BLUE).move_to([0, 3.35, 0])
        run_ct = VGroup(text("simulated experiments:", size=27, color=GRAY),
                        Integer(1, font_size=36, color=INK)).arrange(RIGHT, buff=0.15)
        run_ct.move_to([0, 2.15, 0])
        run_ct[1].add_updater(lambda m: m.set_value(int(round(runs.get_value()))))
        peak = lambda est: counts(est, 300).max() * unit
        brL = LiveBracket(hL, H["100_2"]["sd"], HIST_Y + peak(estL) + 0.3, side=LEFT)
        brR = LiveBracket(hR, H["100_100"]["sd"], HIST_Y + peak(estR) + 0.3)
        coin_line = self.coin_line
        ml_c = coin_line[0].get_center()
        # the coin line waits, small and at 30 %, above the histograms (one focal point: the histograms)
        slot_full = coin_line.copy().scale(SLOT, about_point=ml_c).shift(SLOT_C - ml_c)
        slot_dim = slot_full.copy().fade(0.7)
        t2, t100 = self.t2, self.t100
        hist_all = VGroup(barsL, barsR, truthL, truthR, hL, hR, labL, labR, x_name, scL, scR, n_txt,
                          run_ct, self.t2, self.t100)
        miss = self.coin_miss
        corner_full = slot_full.copy().shift(CORNER_C - slot_full[0].get_center())
        # the measured spread is kept as one tag: both brackets' "+-4.8 pts" fly together into it
        meas0 = MathTex(r"\text{measured:}", font_size=36, color=RED)
        lab_at = brR.lab.copy()
        VGroup(meas0, lab_at).arrange(RIGHT, buff=0.2).move_to(PARK)
        meas = VGroup(meas0, brR.lab)
        with self.narrate("Repeat the hundred-dart experiment three hundred times. [pause 0.2] In both, the "
                          "estimates spread this wide. [pause 1.25]") as beat:
            self.play(Transform(coin_line, slot_dim), t2.animate.set_x(-HIST_X), t100.animate.set_x(HIST_X),
                      FadeOut(self.coin_cap), FadeOut(self.coin_box), Create(hL), Create(hR), FadeIn(labL),
                      FadeIn(labR), FadeIn(x_name), FadeIn(scL), FadeIn(scR), FadeIn(n_txt, shift=0.1 * DOWN),
                      run_time=0.8)
            self.play(ReplacementTransform(VGroup(coinsL, kL), barsL[14]),
                      ReplacementTransform(VGroup(coinsR, kR), barsR[18]), FadeIn(run_ct),
                      run_time=beat.until("three", offset=-0.15, min_time=0.6))
            self.remove(barsL[14], barsR[18])
            self.add(barsL, barsR)
            self.play(Create(truthL), Create(truthR), run_time=0.4)
            barsL.add_updater(upd(hL, estL))
            barsR.add_updater(upd(hR, estR))
            self.play(runs.animate.set_value(300), run_time=beat.until("spread", offset=-0.15, min_time=1.0),
                      rate_func=linear)
            barsL.clear_updaters()
            barsR.clear_updaters()
            run_ct[1].clear_updaters()
            # "spread this wide": both brackets grow while the words are spoken, the same width in 2-D and 100-D
            self.play(GrowFromCenter(brL), GrowFromCenter(brR),
                      run_time=beat.until("wide", end=True, min_time=0.8))
            # they hold, fully legible, through the pause: the two measured numbers are flagged side by side
            self.hold(0.25)
            self.play(Indicate(brL.lab, color=RED, scale_factor=1.12),
                      Indicate(brR.lab, color=RED, scale_factor=1.12), run_time=0.9)

        # ---- why root N: the twelve 16-dart groups of our two runs, as random walks of +-1/2 misses
        ins = (D["darts2d"]["inside"][:96], D["darts100d"]["inside"][:96])
        blocks = [run[16 * k:16 * k + 16] for run in ins for k in range(6)]
        cums = [np.concatenate([[0], np.cumsum([1 if v else -1 for v in b])]) for b in blocks]
        ends_n = [int(c[-1]) for c in cums]
        assert ends_n == [-10, 2, -2, 0, 4, -4, 2, 0, 0, -6, 2, -2], ends_n
        assert abs(np.sqrt(np.mean(np.square(ends_n))) - 3.96) < 0.01      # typical stray 3.96 halves; sqrt(16) = 4
        wpt = lambda k, c: W0 + np.array([k * W_DX, c * W_U, 0])
        cum = cums[WALK_BOLD]
        steps = np.diff(cum)
        P = [wpt(k, c) for k, c in enumerate(cum)]
        G = [wpt(k, k) for k in range(17)]
        xe = W0[0] + 16 * W_DX

        def step_arrow(a, b, opacity=1.0):
            return Arrow(a, b, buff=0, color=RED, stroke_width=6, tip_length=0.14,
                         max_tip_length_to_length_ratio=0.4,
                         max_stroke_width_to_length_ratio=20).set_opacity(opacity)
        walk = VGroup(*[step_arrow(P[k], P[k + 1]) for k in range(16)])
        ghost = VGroup(*[step_arrow(G[k], G[k + 1], 0.3) for k in range(16)])
        others = [j for j in range(12) if j != WALK_BOLD]
        faint = VGroup(*[polyline([wpt(k, c) for k, c in enumerate(cums[j])], RED, 2.0, 0.35) for j in others])
        f_ends = VGroup(*[Dot(wpt(16, cums[j][-1]), radius=0.055, color=RED, fill_opacity=0.6) for j in others])
        walks_lab = text("12 groups of 16 darts (simulated)", size=22, color=GRAY)
        walks_lab.move_to([W0[0], -2.98, 0], aligned_edge=LEFT)
        base = DashedLine(W0, [xe + 0.12, W0[1], 0], color=INK, stroke_width=2, dash_length=0.07).set_opacity(0.6)
        # the typical stray: a band of +-4 halves at the walks' end
        xb = xe + 0.32
        y4, ym4 = wpt(0, 4)[1], wpt(0, -4)[1]
        band = VGroup(Line([xb, ym4, 0], [xb, y4, 0]),
                      Line([xb - 0.08, ym4, 0], [xb + 0.08, ym4, 0]),
                      Line([xb - 0.08, y4, 0], [xb + 0.08, y4, 0]),
                      Line([xb - 0.05, W0[1], 0], [xb + 0.05, W0[1], 0])).set_stroke(RED, 3)
        band_lab = MathTex(r"\pm", "4", r"\text{ halves}", font_size=36, color=RED)
        band_lab.next_to([xb, wpt(0, -2.4)[1], 0], RIGHT, buff=0.22)
        band_labN = MathTex(r"\pm", r"\sqrt{N}", r"\text{ halves}", font_size=36, color=RED)
        band_labN[1].set_color(BLUE)
        band_labN.move_to(band_lab, aligned_edge=LEFT)
        # why four: each miss's half-by-half square; sixteen of them tile a square four halves wide
        tiles = VGroup(*[Square(side_length=W_U).set_stroke(RED, 1.5).set_fill(RED, 0.35)
                         .move_to((P[k] + P[k + 1]) / 2) for k in range(16)])
        tx0 = xb + 0.2
        targets = [np.array([tx0 + (i + 0.5) * W_U, W0[1] + (j + 0.5) * W_U, 0]) for j in range(4) for i in range(4)]
        g16 = MathTex("16", r"\text{ halves}", font_size=36, color=RED)
        g_note = text("if they never cancelled", size=27, color=GRAY)
        ghost_lab = VGroup(g16, g_note).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        ghost_lab.next_to(G[-1], RIGHT, buff=0.3).align_to(G[-1] + UP * 0.22, UP)
        gN = MathTex("N", r"\text{ halves}", font_size=36, color=RED).move_to(g16, aligned_edge=LEFT)
        gN[0].set_color(BLUE)
        # the share's miss: N darts' total miss (root N halves), divided by N, is a half over root N
        e2 = MathTex(r"\text{typical miss}", "=", r"\frac{", r"\sqrt{N}", r"\cdot", r"\tfrac{1}{2}", "}{", "N", "}",
                     font_size=EQ_SIZE)
        e2[0].set_color(RED)
        e2[3].set_color(BLUE)
        e2[5].set_color(RED)
        e2[7].set_color(BLUE)
        e2.move_to(EQ_POS)
        eq = miss_eq(r"\tfrac{1}{2}", "N")
        eq.shift(e2[1].get_center() - eq[1].get_center())
        # the check, built from the formula itself with N = 100 substituted
        chk = MathTex(r"\frac{\tfrac{1}{2}}{", r"\sqrt{", "100", "}}", "=", "0.05", "=", r"5\text{ pts}",
                      font_size=44, color=GRAY)
        chk[0][:-1].set_color(RED)
        chk[1:3].set_color(BLUE)
        chk.next_to(eq, DOWN, buff=0.35).align_to(eq[2], LEFT)
        self.own(e2, eq, chk, band_lab, band_labN, g16, gN)
        # any other function: its own spread sigma, in the same place (the formula never moves)
        eq_s = miss_eq(r"\sigma", "N")
        eq_s.shift(eq[1].get_center() - eq_s[1].get_center())
        self.own(eq_s)
        sig_tag = MathTex(r"\sigma", r"\text{ = one dart's spread}", font_size=36, color=GRAY)
        sig_tag[0].set_color(RED)
        sig_tag.next_to(eq_s, DOWN, buff=0.4).align_to(eq_s, LEFT)
        no_d = MathTex(r"\text{no }", "d", font_size=36, color=GRAY)
        no_d[1].set_color(YELLOW)
        no_d.next_to(eq_s, RIGHT, buff=0.3).align_to(eq_s[3:5], DOWN)
        walk_all = VGroup(walk, faint, f_ends, walks_lab, base, band, band_labN, tiles, coin_line)
        with self.narrate("Those misses fall up or down at random, so they partly cancel. [pause 0.3] Sixteen darts "
                          "typically stray four halves, not sixteen. [pause 0.3] What adds is their squares: sixteen "
                          "of them fill a square four halves wide. [pause 0.4] N darts stray about root N halves. "
                          "[pause 0.3] Divide by N, and the typical miss is a half over root N. [pause 0.8] For a "
                          "hundred darts: five points. We measured four point eight. [pause 0.3] Any other function "
                          "swaps the half for its own spread, sigma; there's still no d.") as beat:
            # both "+-4.8 pts" fly together into one tag, parked at the right (it returns for the check);
            # the histograms clear, and the coin line comes back full size in the corner
            self.play(brL.lab.animate.move_to(lab_at), brR.lab.animate.move_to(lab_at),
                      FadeIn(meas0, shift=0.1 * RIGHT),
                      FadeOut(VGroup(brL.ln, brL[1], brR.ln, brR[1])), FadeOut(hist_all),
                      Transform(coin_line, corner_full), Create(base), run_time=0.6)
            self.remove(*brL.lab.get_family())
            # each step is a copy of the coin's half-miss: up for a dart inside, down for one outside
            self.play(LaggedStart(*[TransformFromCopy(miss[0], a) for a in walk], lag_ratio=0.15),
                      run_time=beat.until("random", end=True, min_time=1.3))
            downs = VGroup(*[a for a, st in zip(walk, steps) if st < 0])
            self.play(downs.animate(rate_func=there_and_back).set_stroke(width=10), meas.animate.set_opacity(0.6),
                      run_time=beat.until("Sixteen", offset=-0.15, min_time=0.8))
            # the other eleven groups of sixteen darts, from the same start: most end within +-4 halves
            self.play(LaggedStart(*[Create(f) for f in faint], lag_ratio=0.08), FadeIn(f_ends),
                      FadeIn(walks_lab), run_time=beat.until("four", offset=-0.15, min_time=1.0))
            self.play(GrowFromCenter(band), FadeIn(band_lab, shift=0.1 * LEFT),
                      run_time=beat.until("not", offset=-0.15, min_time=0.6))
            self.play(TransformFromCopy(walk, ghost), FadeIn(ghost_lab, shift=0.1 * LEFT),
                      run_time=beat.until("sixteen", 2, end=True, min_time=0.9))
            # why four: the squares of the misses add.  Each step grows its half-by-half square ...
            self.wait_beat(beat, "What", offset=-0.1)
            self.play(LaggedStart(*[GrowFromCenter(t) for t in tiles], lag_ratio=0.06),
                      faint.animate.set_stroke(opacity=0.18), f_ends.animate.set_opacity(0.3),
                      run_time=beat.until("squares", end=True, min_time=0.8))
            # ... and sixteen of them tile one square: its side is four halves, the band's top
            self.play(LaggedStart(*[t.animate.move_to(c) for t, c in zip(tiles, targets)], lag_ratio=0.04),
                      run_time=beat.until("four", 2, offset=-0.1, min_time=1.0))
            self.play(flag(tiles, color=RED), flag(band_lab, color=RED),
                      run_time=beat.until("wide", end=True, min_time=0.6))
            self.wait_beat(beat, "N", offset=-0.1)
            self.play(TransformMatchingTex(g16, gN), run_time=0.5)
            self.wait_beat(beat, "root", offset=-0.15)
            self.play(TransformMatchingTex(band_lab, band_labN), run_time=0.6)
            # total stray of N darts: root N halves, i.e. root N times one half
            self.play(TransformFromCopy(band_labN[1], e2[3]), TransformFromCopy(self.coin_half, e2[5]),
                      FadeIn(e2[4]), run_time=beat.until("Divide", offset=-0.1, min_time=0.7))
            # divide by N: the N comes from "N halves"
            self.play(FadeIn(e2[0:2], shift=0.1 * RIGHT), Create(e2[6]),
                      run_time=beat.until("N", 3, offset=-0.1, min_time=0.5))
            self.play(TransformFromCopy(gN[0], e2[7]), run_time=beat.until("N", 3, end=True, min_time=0.5))
            self.add(e2)
            self.wait_beat(beat, "half", offset=-0.15)
            # one root N cancels: the numerator's root N drops into the N below, which grows a root sign;
            # the staircase has given its N and clears
            self.play(ReplacementTransform(e2[0], eq[0]), ReplacementTransform(e2[1], eq[1]),
                      ReplacementTransform(e2[5], eq[2][:-1]), ReplacementTransform(e2[6], eq[2][-1]),
                      ReplacementTransform(e2[7], eq[4]), Create(eq[3]),
                      FadeOut(VGroup(e2[3], e2[4]), shift=(eq[3:5].get_center() - e2[3].get_center()) * 0.8),
                      FadeOut(VGroup(ghost, gN, g_note)),
                      run_time=beat.until("root", 2, end=True, min_time=0.9))
            self.remove(*e2.get_family(), *eq.get_family())
            self.add(eq)
            self.play(flag(eq[3:5], color=BLUE), run_time=0.8)
            # check against the histograms: the formula itself, with N = 100, predicts 5 points
            self.wait_beat(beat, "For", offset=-0.1)
            n_fly = eq[4].copy()
            self.allow_overlap(n_fly, chk, reason="the N copy sits in the check's denominator slot for one frame, then swaps to 100")
            self.play(TransformFromCopy(eq[2], chk[0]), TransformFromCopy(eq[3], chk[1]),
                      TransformFromCopy(eq[5], chk[3]), n_fly.animate.move_to(chk[2]), run_time=0.8)
            self.play(swap(n_fly, chk[2], run_time=0.6), FadeIn(chk[4:], shift=0.1 * LEFT),
                      run_time=beat.until("points", end=True, min_time=0.8))
            # ... and the measured tag comes back from its parking place to sit beside it
            self.wait_beat(beat, "measured", offset=-0.25)
            self.play(meas.animate.set_opacity(1).next_to(chk, RIGHT, buff=0.45).set_y(chk[4].get_y()),
                      run_time=beat.until("eight", offset=-0.1, min_time=0.8))
            self.play(flag(meas[1], color=RED), run_time=beat.until("eight", end=True, min_time=0.5))
            # any other function: the walk steps back to 30 % context, the half becomes sigma
            self.wait_beat(beat, "Any", offset=-0.1)
            self.play(walk_all.animate.fade(0.7), FadeOut(VGroup(chk, meas)), run_time=0.6)
            self.wait_beat(beat, "half", 2, offset=-0.15)
            self.play(flag(eq[2][:-1], color=RED), run_time=0.7)
            self.wait_beat(beat, "sigma", offset=-0.3)
            self.play(FadeTransform(eq[2][:-1], eq_s[2][:-1]), Transform(eq[2][-1], eq_s[2][-1]),
                      *[Transform(eq[i], eq_s[i]) for i in (0, 1, 3, 4)], run_time=0.5)
            self.swap(eq, eq_s)
            self.play(flag(eq_s[2][:-1], color=RED), FadeIn(sig_tag, shift=0.1 * UP), run_time=0.7)
            self.wait_beat(beat, "no", offset=-0.15)
            self.play(FadeIn(no_d, shift=0.1 * LEFT), flag(eq_s[3:5], color=BLUE),
                      run_time=beat.remaining(min_time=0.7))
        self.eq_s, self.no_d, self.sig_tag, self.walk_all = eq_s, no_d, sig_tag, walk_all

    def make_compact_chart(self):
        """The dimension chart again, smaller and lower-left, with the same data: the laws sit above it."""
        ax, xl, yl, y_title, x_title = self.make_chart(compact=True)
        xs = [ax.X(d) for d in DIMS]
        gp = [ax.c2p(x, ax.Y(D["grid"][str(d)]["error_points"])) for d, x in zip(DIMS, xs)]
        dp = [ax.c2p(x, ax.Y(D["darts"][str(d)]["error_points"])) for d, x in zip(DIMS, xs)]
        gdots = VGroup(*[Dot(p, radius=0.075, color=PURPLE) for p in gp])
        ddots = VGroup(*[Dot(p, radius=0.075, color=BLUE) for p in dp])
        gseg = VGroup(*[Line(gp[i], gp[i + 1], color=PURPLE, stroke_width=3) for i in range(5)])
        dseg = VGroup(*[Line(dp[i], dp[i + 1], color=BLUE, stroke_width=3) for i in range(5)])
        g_lab = text("grid", size=27, color=PURPLE).next_to(gdots[-1], RIGHT, buff=0.25)
        d_lab = VGroup(text("darts", size=27, color=BLUE), text("(simulated)", size=22, color=GRAY))
        d_lab.arrange(DOWN, buff=0.06, aligned_edge=LEFT).next_to(ddots[-1], RIGHT, buff=0.25)
        x4 = ax.c2p(ax.X(4), 0)
        d4 = DashedLine(x4, ax.c2p(ax.X(4), 5), color=YELLOW, stroke_width=2.5, dash_length=0.08)
        d4_lab = MathTex("4", font_size=MATH_SMALL, color=YELLOW).next_to(x4, DOWN, buff=0.24)
        d4_lab.align_to(xl[0], DOWN)
        yv = ax.Y(D["darts_typical_error_points"])
        pred = DashedLine(ax.c2p(0, yv), ax.c2p(1.84, yv), color=BLUE, stroke_width=3, dash_length=0.12)
        pred_lab = VGroup(text("typical miss:", size=27, color=RED),
                          MathTex(r"0.05\text{ points}", font_size=36, color=RED)).arrange(RIGHT, buff=0.2)
        pred_lab.next_to(ax.c2p(1.84, yv), RIGHT, buff=0.3).shift(UP * 0.12)
        return dict(ax=ax, base=VGroup(ax, xl, yl, y_title, x_title), labels=VGroup(g_lab, d_lab),
                    gline=VGroup(gseg, gdots), dline=VGroup(dseg, ddots), gdots=gdots, ddots=ddots,
                    d4=d4, d4_lab=d4_lab, pred=pred, pred_lab=pred_lab)

    # ================================================================== 2:45 the prediction
    def prediction(self):
        eq_s, no_d = self.eq_s, self.no_d
        chart = self.make_compact_chart()
        target_c = np.array([0, PRED_Y, 0])
        sz = EQ_SIZE
        eq_h = miss_eq(r"\tfrac{1}{2}", "N", size=sz)
        eq_m = miss_eq(r"\tfrac{1}{2}", r"1{,}000{,}000", size=sz)
        eq_k = MathTex(r"\text{typical miss}", "=", r"\frac{\tfrac{1}{2}}{", r"1000", "}", font_size=sz)
        eq_k[0].set_color(RED)
        eq_k[2][:-1].set_color(RED)
        eq_k[3].set_color(BLUE)
        eq_v = MathTex(r"\text{typical miss}", "=", r"0.0005", "=", r"0.05\text{ points}", font_size=sz)
        for i in (0, 2, 4):
            eq_v[i].set_color(RED)
        for e in (eq_h, eq_m, eq_k, eq_v):
            e.move_to(target_c)
        # the open question from the stakes ("off by ?") comes back as "= ?" during the prediction pause
        q = MathTex("=", r"\ ?", font_size=sz)
        q[1].set_color(BLUE)
        room = (q.width + 0.25) / 2
        eq_k.shift(LEFT * room)
        self.own(eq_h, eq_m, eq_k, eq_v)
        eq_c = eq_s.copy().move_to(target_c)                              # sigma version, centred
        no_d_c = no_d.copy()
        no_d_c.next_to(eq_c, RIGHT, buff=0.3).align_to(eq_c[3:5], DOWN)
        pred, pred_lab = chart["pred"], chart["pred_lab"]
        with self.narrate("Back to our ball: a million darts, any dimension. [pause 1.5] One half over a "
                          "thousand: five hundredths of a point. [pause 0.9]") as beat:
            # the walk leaves; the darts' law takes the top centre
            self.play(FadeOut(self.walk_all), FadeOut(self.sig_tag), Transform(eq_s, eq_c), Transform(no_d, no_d_c),
                      run_time=beat.until("ball", offset=-0.05, min_time=0.7))
            # sigma -> 1/2 (our ball is a yes/no question whose answer is one half); the chart of our
            # million-dart runs returns frame first (axes, ticks, titles), then its two data lines
            self.play(FadeTransform(eq_s[2][:-1], eq_h[2][:-1]), Transform(eq_s[2][-1], eq_h[2][-1]),
                      *[Transform(eq_s[i], eq_h[i]) for i in (0, 1, 3, 4)],
                      FadeIn(chart["base"], shift=0.2 * UP), run_time=0.6)
            self.swap(eq_s, eq_h)
            # N -> 1,000,000 (the old symbol leaves before the number arrives), while the lines are drawn
            self.play(swap(eq_h[4], eq_m[4], run_time=0.7), Transform(eq_h[3], eq_m[3]),
                      *[Transform(eq_h[i], eq_m[i]) for i in (0, 1, 2)],
                      no_d.animate.next_to(eq_m, RIGHT, buff=0.3).align_to(eq_m[3:5], DOWN),
                      Create(chart["gline"]), Create(chart["dline"]), FadeIn(chart["labels"]),
                      run_time=beat.until("any", offset=-0.1, min_time=1.0))
            self.swap(eq_h, eq_m)
            self.play(Indicate(no_d, color=YELLOW, scale_factor=1.2),
                      run_time=beat.until("dimension", end=True, offset=-0.2, min_time=0.6))
            # the open question from the stakes ("off by ?") comes back as "= ?" for the prediction pause
            q.next_to(eq_m, RIGHT, buff=0.25).shift(LEFT * room)
            self.play(FadeOut(no_d), eq_m.animate.shift(LEFT * room), FadeIn(q, shift=0.1 * LEFT), run_time=0.6)
            self.wait_beat(beat, "One", offset=-0.15)
            self.play(swap(VGroup(eq_m[3], eq_m[4]), eq_k[3]),
                      *[Transform(eq_m[i], eq_k[i]) for i in (0, 1, 2)],
                      q.animate.next_to(eq_k, RIGHT, buff=0.25),
                      run_time=beat.until("thousand", end=True, offset=-0.15, min_time=0.8))
            self.swap(eq_m, eq_k)
            # the question mark becomes the answer, on "five hundredths"
            self.wait_beat(beat, "five", offset=-0.25)
            self.play(Transform(eq_k[0], eq_v[0]), Transform(eq_k[1], eq_v[1]),
                      swap(VGroup(eq_k[2], eq_k[3], eq_k[4], q), VGroup(eq_v[2], eq_v[3], eq_v[4])), run_time=0.8)
            self.swap(eq_k, eq_v[0], eq_v[1], eq_v[2], eq_v[3], eq_v[4])
            self.remove(*eq_v)
            self.add(eq_v)
            # flag the answer by growing it rightward only (a centred Indicate pushes it into the "=")
            self.play(eq_v[4].animate(rate_func=there_and_back).scale(1.1, about_edge=LEFT), run_time=0.6)
            # the answer stays; a rigid copy (same glyphs, scaled and moved) labels the darts' new dashed
            # line, and all six runs sit under it
            # (the copy starts invisible and becomes opaque as it leaves, so it never double-exposes the answer)
            tag = eq_v[4].copy().set_opacity(0)
            self.add(tag)
            self.play(Create(pred), tag.animate.scale(pred_lab[1].height / eq_v[4].height).move_to(pred_lab[1])
                      .set_opacity(1), run_time=0.9)
            self.remove(tag)
            self.add(pred_lab[1])
            self.play(FadeIn(pred_lab[0], shift=0.1 * RIGHT),
                      *[Indicate(d, color=BLUE, scale_factor=1.6) for d in chart["ddots"]],
                      run_time=0.7)
        self.chart = chart
        self.chart_extra = VGroup(pred, pred_lab)
        self.answer = eq_v

    # ================================================================== 3:01 payoff
    def payoff(self):
        side = 2.8
        cL, cR = np.array([-2.75, -0.75, 0]), np.array([3.4, -0.75, 0])
        fL = square_frame(cL, side, ("important setting", "unimportant"))
        fR = square_frame(cR, side, ("important setting", "unimportant"))
        for f in (fL, fR):
            f.remove(f.ticks)
        g = lambda x: np.exp(-((x - 0.62) / 0.16) ** 2)
        base_y, amp = 1.0, 1.05

        def curve(c):
            xs = np.linspace(0, 1, 120)
            pts = [np.array([c[0] + (x - 0.5) * side, base_y + amp * g(x), 0]) for x in xs]
            base = Line([c[0] - side / 2, base_y, 0], [c[0] + side / 2, base_y, 0], color=DIM, stroke_width=2)
            return VGroup(base, VMobject().set_points_smoothly(pts).set_stroke(INK, 3))
        cvL, cvR = curve(cL), curve(cR)
        score = VGroup(text("model score", size=27, color=GRAY), text("(schematic)", size=22, color=GRAY))
        score.arrange(DOWN, buff=0.08, aligned_edge=RIGHT)
        score.next_to([cL[0] - side / 2, base_y + 0.45, 0], LEFT, buff=0.25)
        tL = text("grid search", size=32, color=PURPLE).move_to([cL[0], 2.62, 0])
        tR = text("random search", size=32, color=BLUE).move_to([cR[0], 2.62, 0])
        gpts = D["bb"]["grid"]
        rpts = [[0.06 + 0.88 * x, 0.06 + 0.88 * y] for x, y in D["bb"]["random"]]
        gd = VGroup(*[Dot(sq_pt(cL, x, y, side), radius=0.075, color=PURPLE) for x, y in gpts])
        rd = VGroup(*[Dot(sq_pt(cR, x, y, side), radius=0.075, color=BLUE) for x, y in rpts])

        def hits(c, pts, color):
            sh = VGroup(*[DashedLine(sq_pt(c, x, y, side), [c[0] + (x - 0.5) * side, base_y + amp * g(x), 0],
                                     color=color, stroke_width=1.6, dash_length=0.06).set_opacity(0.55)
                          for x, y in pts])
            on = VGroup(*[Dot([c[0] + (x - 0.5) * side, base_y + amp * g(x), 0], radius=0.075, color=color)
                          for x, y in pts])
            return sh, on
        shL, onL = hits(cL, gpts, PURPLE)
        shR, onR = hits(cR, rpts, BLUE)
        cite = citation("Bergstra & Bengio, 2012 · Journal of Machine Learning Research")
        with self.narrate("In 2012, Bergstra and Bengio found random search tuned neural networks as well as "
                          "grid search in a fraction of the time. [pause 0.45] Few settings really matter; with "
                          "one, the search is one-dimensional: nine grid trials test three values of it; nine random "
                          "trials test nine. [pause 0.3]") as beat:
            # the chart's grid points become the grid's trials, its darts the random trials
            ch = self.chart
            # the chart fades completely while its dots travel; only then are the squares drawn (no mixed frame)
            self.play(LaggedStart(
                FadeOut(VGroup(ch["base"], ch["labels"], self.chart_extra, self.answer,
                               ch["gline"][0], ch["dline"][0]), run_time=0.45),
                AnimationGroup(ReplacementTransform(ch["gdots"], gd), ReplacementTransform(ch["ddots"], rd),
                               run_time=0.8), lag_ratio=0.5), run_time=1.025)
            self.play(Create(fL[:3]), Create(fR[:3]), FadeIn(fL[3:]), FadeIn(fR[3:]), FadeIn(cite, shift=0.1 * UP),
                      run_time=beat.until("Bergstra", end=True, min_time=0.6))
            self.wait_beat(beat, "random", offset=-0.2)
            # method names fade up on their words (no stroke-first Write: its outlines read as broken glyphs)
            self.play(FadeIn(tR, shift=0.12 * DOWN, run_time=0.6), Indicate(rd, color=BLUE, scale_factor=1.2,
                                                                         run_time=0.8))
            self.wait_beat(beat, "grid", offset=-0.2)
            self.play(FadeIn(tL, shift=0.12 * DOWN, run_time=0.6), Indicate(gd, color=PURPLE, scale_factor=1.2,
                                                                         run_time=0.8))
            # "only a few settings matter": the score depends (almost) only on the important setting
            self.wait_beat(beat, "Few", offset=-0.3)
            self.play(Create(cvL), Create(cvR), FadeIn(score), run_time=beat.until("with", offset=-0.1, min_time=0.8))
            # "the search is one-dimensional": the important axis flashes, the other steps back to 30 %
            self.wait_beat(beat, "one-dimensional", offset=-0.2)
            self.play(Indicate(fL.xl, color=INK, scale_factor=1.12), Indicate(fR.xl, color=INK, scale_factor=1.12),
                      fL.yl.animate.set_opacity(0.3), fR.yl.animate.set_opacity(0.3),
                      fL.bottom.animate(rate_func=there_and_back).set_stroke(INK, width=5),
                      fR.bottom.animate(rate_func=there_and_back).set_stroke(INK, width=5),
                      run_time=beat.until("nine", offset=-0.1, min_time=0.8))
            self.play(Create(shL), TransformFromCopy(gd, onL), run_time=beat.until("three", offset=-0.1))
            self.play(Indicate(onL, color=PURPLE, scale_factor=1.3), run_time=0.8)
            self.wait_beat(beat, "nine", 2, offset=-0.1)
            self.play(Create(shR), TransformFromCopy(rd, onR), run_time=beat.until("nine", 3, offset=-0.1))
            self.play(Indicate(onR, color=BLUE, scale_factor=1.3), run_time=beat.remaining(min_time=0.8))
        self.bb = VGroup(fL, fR, cvL, cvR, score, tL, tR, gd, rd, shL, onL, shR, onR, cite)
        self.bb_frames = (fL, fR)

    # ================================================================== 3:19 honest limit
    def limit(self):
        LO = -18
        ax = axes((1, 31), (0, -LO), x_length=8.4, y_length=4.0, numbers=False,
                  x_ticks=[5, 10, 15, 20, 25, 30], y_ticks=[0, 6, 12, 18])
        ax.move_to([0.1, 0.35, 0])
        c2p = lambda x, ly: ax.c2p(x, ly - LO)          # ly = log10(share)
        xl = VGroup(*[MathTex(str(t), font_size=MATH_SMALL, color=GRAY).next_to(c2p(t, LO), DOWN, buff=0.18)
                      for t in (5, 10, 15, 20, 25, 30)])
        yl = VGroup(*[MathTex(s, font_size=MATH_SMALL, color=GRAY).next_to(c2p(1, y), LEFT, buff=0.18)
                      for s, y in zip([r"10^{-18}", r"10^{-12}", r"10^{-6}", "1"], (-18, -12, -6, 0))])
        y_t = text("share of box inside a radius-1 ball", size=27, color=GRAY)
        y_t.next_to(c2p(1, 0), UP, buff=0.35).align_to(yl, LEFT)
        x_t = text("dimensions", size=27, color=GRAY).move_to([ax.get_center()[0], xl.get_bottom()[1] - 0.3, 0])
        share = D["ball_r1"]
        ds = list(range(2, 31))
        pts = [c2p(d, log10(share[str(d)])) for d in ds]
        curve = VMobject().set_points_as_corners(pts).set_stroke(INK, 3)
        cdots = VGroup(*[Dot(p, radius=0.055, color=INK) for p in pts])
        end_lab = MathTex(r"2\times10^{-14}", font_size=36, color=INK).next_to(pts[-1], UR, buff=0.2)
        line = DashedLine(c2p(1, -6), c2p(31, -6), color=BLUE, stroke_width=3, dash_length=0.12)
        line_lab = MathTex(r"1/N", font_size=36, color=BLUE).next_to(c2p(31, -6), UP, buff=0.12)
        line_lab.align_to(c2p(31, -6), RIGHT)
        # the zone where a million darts expect under one hit: from the crossing (d = 17.06) on
        l17, l18 = log10(share["17"]), log10(share["18"])
        d_x = 17 + (-6 - l17) / (l18 - l17)
        zx0, zx1 = c2p(d_x, LO)[0], c2p(31, LO)[0]
        zone = Rectangle(width=zx1 - zx0, height=c2p(1, -6)[1] - c2p(1, LO)[1], stroke_width=0,
                         fill_color=RED, fill_opacity=0.13).move_to(c2p(d_x, LO), aligned_edge=DL)
        zone_lab = text("under 1 hit expected", size=27, color=RED)
        zone_lab2 = VGroup(text("darts report 0:", size=27, color=RED),
                           text("off by the whole answer", size=27, color=RED)).arrange(DOWN, buff=0.16,
                                                                                         aligned_edge=LEFT)
        zone_lab2.move_to([zx0 + 0.1, c2p(1, LO)[1] + 0.18, 0], aligned_edge=DL)
        zone_lab.move_to(zone_lab2[1], aligned_edge=LEFT)
        # the Bergstra & Bengio panel leaves completely before the new chart is drawn (no mixed frame)
        with self.narrate("Darts have a blind spot: tiny answers. [pause 0.2] Keep the ball's radius at one, and "
                          "in thirty dimensions it fills two parts in a hundred trillion of the box. [pause 0.4] Below "
                          "this line, a million darts expect under one hit, so they usually report zero: a tiny miss, "
                          "but the whole answer.") as beat:
            # the new axes start drawing as the panel's last 15 % fades (no empty frame, no mixed frame)
            self.play(LaggedStart(FadeOut(self.bb, run_time=0.45),
                                  AnimationGroup(Create(ax), FadeIn(xl), FadeIn(yl), FadeIn(y_t), FadeIn(x_t)),
                                  lag_ratio=0.85),
                      run_time=beat.until("tiny", offset=-0.15, min_time=1.2))
            # "tiny answers": the curve of ever tinier answers, d = 2 .. 30, drawn as the words land
            self.play(Create(curve), LaggedStart(*[GrowFromCenter(d) for d in cdots], lag_ratio=0.05),
                      run_time=beat.until("radius", offset=-0.1, min_time=1.2), rate_func=linear)
            # "radius at one": the chart's own title says it; "thirty dimensions": the last dot
            self.play(Indicate(y_t, color=INK, scale_factor=1.05), run_time=beat.until("thirty", offset=-0.1, min_time=0.6))
            self.play(Indicate(cdots[-1], color=INK, scale_factor=1.8), run_time=beat.until("two", offset=-0.1, min_time=0.6))
            self.play(FadeIn(end_lab, shift=0.1 * UP), run_time=beat.until("box", end=True, min_time=0.8))
            self.wait_beat(beat, "line", offset=-0.4)
            self.play(Create(line), FadeIn(line_lab), run_time=0.8)
            self.play(FadeIn(zone), FadeIn(zone_lab), run_time=beat.until("hit", offset=-0.1, min_time=0.6))
            self.wait_beat(beat, "report", offset=-0.2)
            self.play(swap(zone_lab, zone_lab2[0], run_time=0.6))
            self.play(Indicate(zone_lab2[0], color=RED, scale_factor=1.05),
                      run_time=beat.until("whole", offset=-0.25, min_time=0.6))
            self.play(FadeIn(zone_lab2[1], shift=0.1 * UP), run_time=beat.until("answer", end=True, min_time=0.6))
            self.play(flag(zone_lab2[1], color=RED), run_time=beat.remaining(min_time=0.6))
        self.limit_parts = dict(x_axis=ax.x_axis, line=line, line_lab=line_lab,
                                rest=VGroup(ax.y_axis, xl, yl, y_t, x_t, curve, cdots, end_lab, zone, zone_lab2))

    # ================================================================== 3:37 landing
    def landing(self):
        axes_pc, ends, ins, n_lab, d_lab = self.make_pc()
        centre = VGroup(*[Dot(pc_pt(i, 0.5), radius=0.05, color=PURPLE) for i in range(100)])
        centre_line = polyline([pc_pt(i, 0.5) for i in range(100)], color=PURPLE, width=3)
        centre.set_z_index(3)
        centre_line.set_z_index(3)
        one_lab = VGroup(text("1 value", size=28, color=PURPLE), text("per axis", size=28, color=PURPLE))
        one_lab.arrange(DOWN, buff=0.12).next_to(pc_pt(99, 0.5), RIGHT, buff=0.25)
        rng = np.random.default_rng(12)
        many = VGroup(*[polyline([pc_pt(i, v) for i, v in enumerate(rng.random(100))], BLUE, 1.0, 0.18)
                        for _ in range(90)])
        bands = VGroup(*[Line(pc_pt(i, 0), pc_pt(i, 1), color=BLUE, stroke_width=3.2) for i in range(100)])
        mil_lab = VGroup(text("1,000,000", size=28, color=BLUE), text("coin flips", size=28, color=BLUE))
        mil_lab.arrange(DOWN, buff=0.12).next_to(pc_pt(99, 0.82), RIGHT, buff=0.25)
        L = self.limit_parts
        base = Line(pc_pt(0, 0), pc_pt(99, 0), color=AXIS, stroke_width=1.6)
        # in the breath after the limit: its 1/N line becomes the cold-open header (same N), and its
        # x-axis becomes the floor the 100 input axes grow up from
        # (the chart clears first; the line then rises into the header as one shape, no glyph soup)
        # (the chart clears completely first; then the dashed 1/N line rises and shrinks, as one rigid shape, into
        # a rule under the header's place, and the header N = 1,000,000 points settles on it: no ghost text)
        line = L["line"]
        self.play(FadeOut(L["rest"]), FadeOut(L["line_lab"]), run_time=0.25)
        self.play(ReplacementTransform(L["x_axis"], base),
                  line.animate.scale(n_lab.width / line.width).next_to(n_lab, DOWN, buff=0.12), run_time=0.4)
        # the YELLOW counter of the first frame is back too, at "d = 1"
        trk = ValueTracker(1.0)
        slot = d_lab[0][2:]
        d_num = Integer(1, font_size=44, color=YELLOW).move_to(slot, aligned_edge=DL)
        d_head = d_lab[0][:2]
        self.play(FadeIn(n_lab, shift=0.1 * DOWN), FadeOut(line), FadeIn(d_head), FadeIn(d_num), run_time=0.25)
        d_num.add_updater(lambda m: m.set_value(min(100, max(1, int(trk.get_value()))))
                          .move_to(slot, aligned_edge=DL))
        with self.narrate("The darts never counted the axes: [pause 0.4] a million coin flips, in any "
                          "dimension.") as beat:
            # the axes grow back while the counter counts them again, as in the first frame (we counted
            # them; the darts never did)
            self.play(LaggedStart(*[GrowFromEdge(a, DOWN) for a in axes_pc], lag_ratio=0.01),
                      trk.animate(rate_func=linear).set_value(100),
                      FadeIn(ends), FadeIn(ins), FadeOut(base),
                      run_time=beat.until("counted", end=True, min_time=1.0))
            d_num.clear_updaters()
            self.remove(d_num, d_head)
            self.add(d_lab[0])
            self.play(LaggedStart(*[GrowFromCenter(d) for d in centre], lag_ratio=0.01), Create(centre_line),
                      FadeIn(one_lab, shift=0.1 * LEFT), FadeIn(d_lab[1], shift=0.1 * LEFT),
                      run_time=beat.until("axes", end=True, min_time=0.7))
            self.play(LaggedStart(*[Create(m) for m in many], lag_ratio=0.03),
                      run_time=beat.until("coin", offset=-0.1, min_time=1.0))
            self.play(FadeIn(bands), FadeIn(mil_lab, shift=0.1 * LEFT), run_time=beat.until("in", 1, offset=-0.1, min_time=0.6))
            self.play(Indicate(d_lab, color=YELLOW, scale_factor=1.06), run_time=beat.remaining(min_time=0.8))
