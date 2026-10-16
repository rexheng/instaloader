"""Episode 5: Why Random Darts Beat Grids in 100 Dimensions (round 4 cut).

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
ML_Y = -0.3                                                  # one-coin number line (built here, base size)
EQ_POS = np.array([0.0, 2.7, 0.0])                           # the spread formula
EQ_SIZE = 56
BIG = 1.8                                                    # one-coin close-up scale
BIG_C = np.array([0.0, -0.6, 0.0])
SLOT = 0.75                                                  # coin line beside the histograms: 0.75 x close-up
SLOT_C = np.array([0.0, 0.25, 0.0])
CORNER_C = np.array([4.2, -1.95, 0.0])                       # coin line during the random walk
TITLE_Y2 = 2.85                                              # "2 / 100 dimensions" over the coins
# the random walk of sixteen +-1/2 misses (darts 62-77 of the 2-D run: 10 inside, 6 outside)
WALK_IDX = (61, 77)
W0 = np.array([-4.6, -1.2, 0.0])
W_DX, W_U = 0.3, 0.17


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
    bottom = Line(p(0, 0), p(1, 0), color=GRAY, stroke_width=2.5)
    left = Line(p(0, 0), p(0, 1), color=GRAY, stroke_width=2.5)
    rest = VGroup(Line(p(0, 1), p(1, 1), color=DIM, stroke_width=2),
                  Line(p(1, 0), p(1, 1), color=DIM, stroke_width=2))
    ticks = VGroup(MathTex("0", font_size=MATH_SMALL, color=GRAY).next_to(p(0, 0), DL, buff=0.14),
                   MathTex("1", font_size=MATH_SMALL, color=GRAY).next_to(p(1, 0), DOWN, buff=0.18),
                   MathTex("1", font_size=MATH_SMALL, color=GRAY).next_to(p(0, 1), LEFT, buff=0.18))
    xl = text(names[0], size=26, color=GRAY).next_to(bottom, DOWN, buff=0.2)
    yl = text(names[1], size=26, color=GRAY).rotate(PI / 2).next_to(left, LEFT, buff=0.2)
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
    back_sq = Polygon(P(0, 0, 1), P(1, 0, 1), P(1, 1, 1), P(0, 1, 1)).set_stroke(GRAY, 2).set_fill(opacity=0)
    disc_fill = Polygon(Q(0, 0, 0), *[Q(r2d * np.cos(t), r2d * np.sin(t), 0) for t in ts])
    disc_fill.set_fill(INK, 0.12).set_stroke(width=0)
    disc_arc = arc(lambda t: Q(r2d * np.cos(t), r2d * np.sin(t), 0)).set_stroke(INK, 2.5)
    pts = np.array([Q(r3d * np.sin(p) * np.cos(t), r3d * np.sin(p) * np.sin(t), r3d * np.cos(p))
                    for t in ts for p in ts] + [Q(0, 0, 0)])
    hull = SciHull(pts[:, :2])
    dome = Polygon(*[pts[i] for i in hull.vertices]).set_fill(INK, 0.12).set_stroke(width=0)
    back_arc = arc(lambda t: Q(r3d * np.cos(t), r3d * np.sin(t), 0)).set_stroke(INK, 2.5)
    rim = VGroup(DashedVMobject(arc(lambda t: Q(r3d * np.cos(t), 0, r3d * np.sin(t))), num_dashes=12),
                 DashedVMobject(arc(lambda t: Q(0, r3d * np.cos(t), r3d * np.sin(t))), num_dashes=12))
    rim.set_stroke(GRAY, 1.6)                                                     # floor and left-wall edges
    outline = Polygon(*[pts[i] for i in hull.vertices]).set_fill(opacity=0).set_stroke(INK, 2.5)
    front = VGroup(*[Line(P(*u), P(*v)) for u, v in (
        ((0, 0, 0), (1, 0, 0)), ((1, 0, 0), (1, 1, 0)), ((1, 1, 0), (0, 1, 0)), ((0, 1, 0), (0, 0, 0)),
        ((1, 0, 0), (1, 0, 1)), ((1, 1, 0), (1, 1, 1)), ((0, 1, 0), (0, 1, 1)))]).set_stroke(DIM, 2)
    hidden = DashedLine(P(0, 0, 0), P(0, 0, 1), dash_length=0.06).set_stroke(DIM, 1.6)
    # the cube's centre (1/2, 1/2, 1/2): |c|^2 = 0.75 < r3d^2 = 0.97, so it is inside the ball
    centre = Dot(Q(0.5, 0.5, 0.5), radius=0.13, color=PURPLE).set_fill(opacity=0)
    return dict(P=P, back_sq=back_sq, disc_fill=disc_fill, disc_arc=disc_arc, dome=dome,
                back_arc=back_arc, outline=outline, rim=rim, edges=VGroup(front, hidden), centre=centre)


def bracket(x0, x1, y, label, color=RED, size=36, side=RIGHT):
    ln = Line([x0, y, 0], [x1, y, 0], color=color, stroke_width=3)
    ends = VGroup(Line([x0, y - 0.1, 0], [x0, y + 0.1, 0], color=color, stroke_width=3),
                  Line([x1, y - 0.1, 0], [x1, y + 0.1, 0], color=color, stroke_width=3))
    lab = label if isinstance(label, Mobject) else MathTex(*label, font_size=size, color=color)
    lab.next_to(ln, side, buff=0.15)
    return VGroup(ln, ends, lab)


def spread_eq(num, den, size=EQ_SIZE):
    """spread = num / sqrt(den), split into [spread, =, frac-with-numerator, sqrt, den, close]."""
    e = MathTex(r"\text{spread}", "=", r"\frac{" + num + "}{", r"\sqrt{", den, "}}", font_size=size)
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
        self.track = Line([x0, Y_BAR, 0], [x0 + length, Y_BAR, 0], color=GRAY, stroke_width=2)
        xt = x0 + length * r2 / vmax
        self.tick = DashedLine([xt, Y_BAR - 0.16, 0], [xt, Y_BAR + 0.16, 0], color=INK, stroke_width=3,
                               dash_length=0.05)
        self.v = ValueTracker(0.0)
        self.bar = Line([x0, Y_BAR, 0], [x0 + 1e-3, Y_BAR, 0], color=BLUE, stroke_width=9)
        self.num = DecimalNumber(value, num_decimal_places=dec, font_size=36, color=BLUE)
        self.lhs = MathTex(lhs, "=", font_size=36)
        self.rel = MathTex("<" if inside else ">", font_size=36)
        self.rv = MathTex(f"{r2:.{dec}f}", font_size=36)
        self.readout = VGroup(self.lhs, self.num, self.rel, self.rv).arrange(RIGHT, buff=0.14)
        self.readout.move_to([cx, Y_READ, 0])
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
    PRONUNCIATIONS = {"Bengio": "/bˈɛnʤiO/", "Ulam": "/ˈulɑm/", "d-th": "/dˈiθ/"}
    SPEED = 0.86
    BEAT_GAP = 0.1               # within a thought; beat boundaries pass gap=BOUNDARY
    BOUNDARY = 0.6

    # ================================================================== construct
    def construct(self):
        self.cold_open()
        self.build_2d()
        self.climb()
        self.shadows()
        self.diagonal()
        self.bits()
        self.spread()
        self.prediction()
        self.payoff()
        self.limit()
        self.landing()
        self.end_card()

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
        axes_pc = VGroup(*[Line(pc_pt(i, 0), pc_pt(i, 1), color=GRAY, stroke_width=1.6,
                                stroke_opacity=0.8) for i in range(100)])
        lab0 = MathTex("0", font_size=MATH_SMALL, color=GRAY).next_to(pc_pt(0, 0), LEFT, buff=0.15)
        lab1 = MathTex("1", font_size=MATH_SMALL, color=GRAY).next_to(pc_pt(0, 1), LEFT, buff=0.15)
        in1 = text("input 1", size=26, color=GRAY).next_to(pc_pt(0, 0), DOWN, buff=0.22)
        in1.align_to(pc_pt(0, 0) + LEFT * 0.08, LEFT)
        in100 = text("input 100", size=26, color=GRAY).next_to(pc_pt(99, 0), DOWN, buff=0.22)
        in100.align_to(pc_pt(99, 0) + RIGHT * 0.08, RIGHT)
        n_lab = formula(r"N = 1{,}000{,}000", r"\text{ points}", size=44).move_to([PC_CX - 2.6, 3.12, 0])
        d_lab = formula(r"d = 100", r"\text{ inputs}", size=44).move_to([PC_CX + 2.75, 3.12, 0])
        d_lab[0].set_color(YELLOW)
        return axes_pc, VGroup(lab0, lab1), VGroup(in1, in100), n_lab, d_lab

    def cold_open(self):
        axes_pc, ends, ins, n_lab, d_lab = self.make_pc()
        self.add(axes_pc, n_lab)                         # first frame: a million points, 100 axes
        enc = text("each line: one input, from 0 to 1", size=26, color=GRAY).move_to([PC_CX, 2.35, 0])
        q_txt = text("grid values per input:", size=30)
        q_mark = formula("?", size=60, color=PURPLE)
        q = VGroup(q_txt, q_mark).arrange(RIGHT, buff=0.25).move_to([PC_CX, -2.72, 0])
        with self.narrate("Your budget: a million evaluations to average a function of a hundred inputs. "
                          "[pause 0.25] Spread them out as an even grid; that feels thorough. [pause 0.2] How "
                          "many values does each input get? [pause 1.5]") as beat:
            self.play(FadeIn(enc, shift=0.1 * DOWN), FadeIn(ends), FadeIn(ins), run_time=1.0)
            self.play(axes_pc[0].animate(rate_func=there_and_back).set_stroke(INK, width=4, opacity=1),
                      Indicate(ends, color=INK), run_time=beat.until("function", offset=-0.1, min_time=0.8))
            self.play(Write(d_lab), run_time=0.8)
            self.play(LaggedStart(*[a.animate(rate_func=there_and_back).set_stroke(YELLOW, opacity=1)
                                    for a in axes_pc], lag_ratio=0.02),
                      run_time=beat.until("Spread"))
            levels = VGroup(*[DashedLine(pc_pt(0, v), pc_pt(99, v), color=PURPLE, stroke_width=1.6,
                                         dash_length=0.1).set_opacity(0.55) for v in np.arange(0.1, 0.95, 0.1)])
            self.play(LaggedStart(*[Create(l) for l in levels], lag_ratio=0.12), FadeOut(enc),
                      run_time=beat.until("How", offset=-0.2))
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
        with self.narrate("One. [pause 0.2] The whole grid is one point, the centre of the box. [pause 0.2] "
                          "Two values per input would take two to the hundredth points. [pause 0.8]") as beat:
            self.play(ReplacementTransform(q_mark, one),
                      LaggedStart(*[GrowFromCenter(d) for d in centre], lag_ratio=0.03),
                      run_time=1.3)
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
        opt = text("e.g. an option on 100 stocks", size=26, color=GRAY).move_to([PC_CX, 2.35, 0])
        r_lab = VGroup(text("a random point:", size=26, color=BLUE),
                       text("one value per input", size=26, color=GRAY)).arrange(RIGHT, buff=0.2)
        r_lab.move_to([PC_CX, 2.35, 0])
        cite_g = citation("Glasserman, 2003 · Monte Carlo Methods in Financial Engineering, Springer")
        cite_m = citation("Metropolis & Ulam, 1949 · Journal of the American Statistical Association")
        q2_txt = text("a million random points: off by", size=30)
        q2_mark = formula("?", size=60, color=BLUE)
        q2 = VGroup(q2_txt, q2_mark).arrange(RIGHT, buff=0.25).move_to([PC_CX, -2.72, 0])
        with self.narrate("Pricing an option on a hundred stocks is this kind of average. [pause 0.2] Since "
                          "Metropolis and Ulam's 1949 paper, such averages are usually done with random points, "
                          "like this one. "
                          "[pause 0.25] How far off would a million of them land? [pause 0.15] Hold that "
                          "thought.", gap=self.BOUNDARY) as beat:
            self.play(FadeOut(ghosts), FadeOut(big), FadeOut(self.pc["q"]),
                      run_time=beat.until("option", offset=-0.3, min_time=0.5))
            self.play(FadeIn(opt, shift=0.1 * DOWN), FadeIn(cite_g, shift=0.1 * UP),
                      run_time=beat.until("hundred", offset=-0.1, min_time=0.5))
            self.play(Indicate(d_lab, color=YELLOW, scale_factor=1.06),
                      run_time=beat.until("average", offset=-0.2, min_time=0.8))
            self.wait_beat(beat, "Metropolis", offset=-0.35)
            self.play(FadeOut(cite_g, shift=0.1 * DOWN), FadeIn(cite_m, shift=0.1 * UP), run_time=0.7)
            self.play(Create(dart_line), LaggedStart(*[GrowFromCenter(d) for d in dart_dots], lag_ratio=0.02),
                      FadeOut(opt), run_time=beat.until("like", offset=0.1), rate_func=linear)
            self.play(FadeIn(r_lab, shift=0.1 * DOWN), Indicate(dart_line, color=BLUE, scale_factor=1.03),
                      run_time=beat.until("How", offset=-0.3, min_time=0.8))
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
        with self.narrate("Start with two inputs: a square. [pause 0.2] Our function is one inside this "
                          "quarter disc, zero outside, so its average is the disc's share: exactly one "
                          "half.") as beat:
            self.play(FadeOut(VGroup(pc["axes"][2:], pc["ends"], pc["ins"], pc["n_lab"], pc["d_lab"],
                                     pc["centre"], pc["centre_line"], pc["c_lab"],
                                     self.r_lab, self.dart_dots[2:], self.q2)),
                      run_time=beat.until("two", offset=-0.3))
            self.play(ReplacementTransform(pc["axes"][0], frame_R.bottom),
                      ReplacementTransform(pc["axes"][1], frame_R.left),
                      ReplacementTransform(VGroup(self.dart_line, self.dart_dots[:2]), dart1),
                      run_time=1.6)
            self.play(Create(frame_R.rest), FadeIn(frame_R.ticks), FadeIn(frame_R.xl),
                      FadeIn(frame_R.yl), run_time=beat.until("one", offset=-0.1))
            self.play(Create(disc_R[1]), FadeIn(disc_R[0]), FadeIn(f1, scale=0.6),
                      run_time=beat.until("zero", offset=-0.1))
            self.play(FadeIn(f0, scale=0.6), run_time=0.5)
            self.wait_beat(beat, "share", offset=-0.2)
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
        with self.narrate("A ten by ten grid puts fifty-two of its hundred points inside: two points "
                          "off.") as beat:
            self.play(VGroup(frame_R, disc_R, dart1).animate.shift(R_C - C0), FadeOut(f1), FadeOut(f0),
                      VGroup(truth_t, half).animate.shift(LEFT * 3.1),
                      TransformFromCopy(VGroup(frame_R, disc_R), VGroup(frame_L, disc_L)),
                      FadeIn(g_title), run_time=1.1)
            self.play(LaggedStart(*[GrowFromCenter(d) for d in gdots], lag_ratio=0.01),
                      run_time=beat.until("fifty", offset=-0.1))
            g_num = self.count_up(g_in, PURPLE, g2["count"], g_read[0], beat.until_end_of("inside"))
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
                          "two dimensions, the grid wins.", gap=self.BOUNDARY) as beat:
            self.play(FadeIn(d_title), FadeIn(d_sim),
                      LaggedStart(*[FadeIn(d, shift=0.25 * DOWN) for d in ddots[1:]], lag_ratio=0.02),
                      run_time=beat.until("forty", offset=-0.1))
            d_num = self.count_up(d_in, BLUE, d2["count"], d_read[0], beat.until_end_of("inside"))
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
    def make_chart(self):
        X = lambda d: log10(d) - 0.22                 # axis origin sits at the bottom-left
        Y = lambda err: log10(err) + 3                # 0.001 points -> 0
        xs = [X(d) for d in DIMS]
        ax = axes((0, 1.84), (0, 5), x_length=7.7, y_length=3.8, numbers=False,
                  x_ticks=xs, y_ticks=[0, 1, 2, 3, 4, 5])
        ax.move_to([0.45, 0.75, 0])
        ax.X, ax.Y = X, Y
        xl = VGroup(*[MathTex(str(d), font_size=MATH_SMALL, color=GRAY).next_to(ax.c2p(x, 0), DOWN, buff=0.24)
                      for d, x in zip(DIMS, xs)])
        yl = VGroup(*[MathTex(s, font_size=MATH_SMALL, color=GRAY).next_to(ax.c2p(0, y), LEFT, buff=0.18)
                      for s, y in zip(["0.001", "0.01", "0.1", "1", "10", "100"], range(6))])
        y_title = text("error (percentage points)", size=26, color=GRAY)
        y_title.next_to(ax.c2p(0, 5), UP, buff=0.35).align_to(yl, LEFT)
        x_title = text("dimensions", size=26, color=GRAY)
        x_title.move_to([ax.get_center()[0], xl.get_bottom()[1] - 0.3, 0])
        col = [ax.c2p(x, 0)[0] for x in xs]
        rows1 = VGroup(*[MathTex(str(D["grid"][str(d)]["per_axis"]), font_size=MATH_SMALL, color=PURPLE)
                         .move_to([cx, -2.5, 0]) for d, cx in zip(DIMS, col)])
        used = {10 ** 6: r"10^6"}
        rows2 = VGroup(*[MathTex(used.get(D["grid"][str(d)]["points_used"],
                                          f"{D['grid'][str(d)]['points_used']:,}".replace(",", "{,}")),
                                 font_size=MATH_SMALL, color=GRAY).move_to([cx, -2.97, 0])
                         for d, cx in zip(DIMS, col)])
        r1t = text("values per axis", size=26, color=PURPLE).next_to([col[0], -2.5, 0], LEFT, buff=0.45)
        r2t = text("points used", size=26, color=GRAY).next_to([col[0], -2.97, 0], LEFT, buff=0.45)
        r2t.align_to(r1t, RIGHT)
        return ax, xl, yl, y_title, x_title, VGroup(r1t, r2t), rows1, rows2

    def climb(self):
        ax, xl, yl, y_title, x_title, row_t, rows1, rows2 = self.make_chart()
        xs = [ax.X(d) for d in DIMS]
        gp = [ax.c2p(x, ax.Y(D["grid"][str(d)]["error_points"])) for d, x in zip(DIMS, xs)]
        dp = [ax.c2p(x, ax.Y(D["darts"][str(d)]["error_points"])) for d, x in zip(DIMS, xs)]
        gdots = [Dot(p, radius=0.085, color=PURPLE) for p in gp]
        ddots = [Dot(p, radius=0.085, color=BLUE) for p in dp]
        gseg = [Line(gp[i], gp[i + 1], color=PURPLE, stroke_width=3) for i in range(5)]
        dseg = [Line(dp[i], dp[i + 1], color=BLUE, stroke_width=3) for i in range(5)]
        truth = VGroup(text("true answer", size=26), formula(r"\tfrac12", size=40),
                       text("in every dimension", size=26)).arrange(RIGHT, buff=0.18)
        truth.move_to([0, -2.15, 0])
        cur = DashedLine(ax.c2p(xs[0], 0), ax.c2p(xs[0], 5), color=YELLOW, stroke_width=2,
                         dash_length=0.08).set_opacity(0.7)
        sq = self.sq
        # the square -> cube -> eighth-ball morph runs centred, BEFORE the chart exists
        o = np.array([-1.95, -1.0, 0])
        bi = ball_inset(o, 2.3, np.sqrt(D["r2"]["2"]), np.sqrt(D["r2"]["3"]))
        d_in = MathTex(r"d = 2", font_size=44, color=YELLOW).next_to(bi["P"](1.4, 0.6, 0), RIGHT, buff=0.4)
        d_in3 = MathTex(r"d = 3", font_size=44, color=YELLOW).move_to(d_in)
        rest_L = VGroup(*[sq[k] for k in ("frame_L", "disc_L", "gdots", "g_title")])
        rest_R = VGroup(sq["ddots"], sq["d_title"])
        sqR_lines = VGroup(sq["frame_R"].bottom, sq["frame_R"].left, sq["frame_R"].rest)
        with self.narrate("Now give each a million points, and add inputs. [pause 0.2] The disc becomes a "
                          "ball that always covers exactly half the box.") as beat:
            self.play(FadeOut(rest_L, shift=LEFT * 0.4), FadeOut(rest_R), FadeOut(self.sq_extra),
                      FadeOut(sq["frame_R"]), FadeOut(sq["disc_R"]),
                      TransformFromCopy(sqR_lines, bi["back_sq"]),
                      TransformFromCopy(sq["disc_R"][0], bi["disc_fill"]),
                      TransformFromCopy(sq["disc_R"][1], bi["disc_arc"]),
                      ReplacementTransform(self.half, truth[1]),
                      ReplacementTransform(self.truth_t, truth[0]), FadeIn(truth[2]),
                      run_time=beat.until("add", offset=-0.5, min_time=1.4))
            self.play(FadeIn(d_in, shift=0.1 * LEFT), run_time=0.5)
            self.wait_beat(beat, "disc", offset=-0.15)
            # "d = 3" arrives with the depth edges; only the outline inflates, then the fill follows
            self.play(FadeTransform(d_in, d_in3), Create(bi["edges"]), run_time=0.6)
            self.play(Transform(bi["disc_arc"], bi["back_arc"]), Create(bi["rim"]), Create(bi["outline"]),
                      bi["disc_fill"].animate.set_fill(opacity=0),
                      run_time=beat.until("covers", offset=-0.2, min_time=1.0))
            self.remove(bi["disc_fill"])
            self.play(FadeIn(bi["dome"]), run_time=0.4)
            self.wait_beat(beat, "half", offset=-0.2)
            self.play(flag(truth, color=INK), bi["dome"].animate(rate_func=there_and_back).set_fill(opacity=0.35),
                      run_time=beat.remaining(min_time=0.8))
        centre = bi["centre"]
        inset = VGroup(bi["back_sq"], bi["dome"], bi["disc_arc"], bi["edges"], bi["rim"],
                       bi["outline"], centre)

        # ---- step through dimensions
        def step(i):
            anims = [cur.animate.move_to(ax.c2p(xs[i], 2.5)), xl[i].animate.set_color(YELLOW),
                     FadeIn(rows1[i], shift=0.15 * UP), FadeIn(rows2[i], shift=0.15 * UP),
                     GrowFromCenter(gdots[i]), GrowFromCenter(ddots[i])]
            if i:
                anims += [xl[i - 1].animate.set_color(GRAY), Create(gseg[i - 1]), Create(dseg[i - 1])]
            return anims

        truth_top = VGroup(text("true answer", size=26), formula(r"\tfrac12", size=40),
                           text("in every dimension", size=26)).arrange(RIGHT, buff=0.18)
        truth_top.move_to([0, 3.3, 0]).align_to([6.3, 0, 0], RIGHT)
        thumb_c = np.array([5.42, 2.08, 0])
        with self.narrate("The grid splits its million across the axes: a thousand values per axis in two "
                          "dimensions, then a hundred, ten, three.") as beat:
            # the ball shrinks to a thumbnail beside the true answer; only then is the chart drawn
            self.play(LaggedStart(
                AnimationGroup(inset.animate.scale(0.48).move_to(thumb_c).fade(0.6), FadeOut(d_in3, run_time=0.4),
                               ReplacementTransform(truth, truth_top), FadeIn(row_t, shift=0.15 * UP)),
                AnimationGroup(Create(ax), FadeIn(xl), FadeIn(yl), FadeIn(y_title), FadeIn(x_title)),
                lag_ratio=0.5), run_time=beat.until("thousand", offset=-0.75, min_time=1.4))
            self.play(FadeIn(cur), Indicate(row_t[0], color=PURPLE, scale_factor=1.05), run_time=0.45)
            for i, w in enumerate(["thousand", "hundred", "ten", "three"]):
                self.wait_beat(beat, w, offset=-0.3)
                self.play(*step(i), run_time=0.55)
        g_says = formula(r"\text{grid says } 1.000", size=36, color=PURPLE)
        gx_mid = (gp[4][0] + gp[5][0]) / 2
        g_says.move_to([gx_mid, gp[4][1] + 0.88, 0])
        off50 = text("50 points off", size=28, color=RED).move_to([gx_mid, gp[4][1] + 0.38, 0])
        c_note = VGroup(text("centre is", size=26, color=PURPLE), text("inside the ball", size=26, color=PURPLE))
        c_note.arrange(DOWN, buff=0.1, aligned_edge=RIGHT)
        c_note.next_to(inset, LEFT, buff=0.3).set_y(centre.get_y())
        with self.narrate("From twenty dimensions on, just one: the centre, which sits inside the ball. "
                          "[pause 0.15] So the grid says the ball fills the box: fifty points off.") as beat:
            self.play(cur.animate.move_to(ax.c2p(xs[4], 2.5)), xl[4].animate.set_color(YELLOW),
                      xl[3].animate.set_color(GRAY), FadeIn(rows1[4], shift=0.15 * UP),
                      FadeIn(rows2[4], shift=0.15 * UP), run_time=0.6)
            self.play(cur.animate.move_to(ax.c2p(xs[5], 2.5)), xl[5].animate.set_color(YELLOW),
                      xl[4].animate.set_color(GRAY), FadeIn(rows1[5], shift=0.15 * UP),
                      FadeIn(rows2[5], shift=0.15 * UP), run_time=beat.until("one", offset=-0.1, min_time=0.6))
            self.play(Indicate(rows1[4], color=PURPLE), Indicate(rows1[5], color=PURPLE), FadeOut(cur),
                      xl[5].animate.set_color(GRAY), FadeOut(truth_top),
                      run_time=beat.until("centre", offset=-0.2, min_time=0.6))
            self.play(FadeIn(c_note, shift=0.1 * LEFT), centre.animate.set_fill(opacity=1).set_stroke(opacity=1),
                      run_time=beat.until("sits", offset=-0.15, min_time=0.8))
            self.play(Indicate(centre, color=PURPLE, scale_factor=1.8),
                      run_time=beat.until("So", offset=-0.1, min_time=0.8))
            self.play(FadeOut(c_note, shift=0.1 * UP), run_time=0.4)
            self.wait_beat(beat, "fills", offset=-0.45)
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
        r_lab = VGroup(formula(r"2^{19}\text{ points}", size=36, color=PURPLE),
                       text("18 points off", size=26, color=RED)).arrange(RIGHT, buff=0.3)
        r_lab.next_to(rp, RIGHT, buff=0.3).shift(DOWN * 0.08)
        r_how = text("2 values on 19 axes", size=26, color=PURPLE).next_to(r_lab, DOWN, buff=0.2, aligned_edge=LEFT)
        d_lab = VGroup(text("darts", size=28, color=BLUE), text("(simulated)", size=22, color=GRAY))
        d_lab.arrange(DOWN, buff=0.08).next_to(ddots[5], RIGHT, buff=0.25)
        with self.narrate("Even two values on nineteen of the axes, half a million points, is eighteen points "
                          "off. [pause 0.25] The darts stay under a tenth of a point in every dimension.",
                          gap=self.BOUNDARY) as beat:
            self.play(GrowFromCenter(r_dot), FadeIn(r_how, shift=0.1 * LEFT),
                      run_time=beat.until("half", offset=-0.15, min_time=0.8))
            self.play(FadeIn(r_lab[0], shift=0.1 * LEFT), run_time=0.6)
            self.play(r_dot.animate.move_to(rp), Create(trail), run_time=beat.until("eighteen", offset=-0.15))
            self.play(FadeIn(r_lab[1], shift=0.1 * LEFT), run_time=0.6)
            self.wait_beat(beat, "darts", offset=-0.2)
            self.play(GrowFromCenter(ddots[4]), GrowFromCenter(ddots[5]), Create(dseg[3]),
                      Create(dseg[4]), FadeIn(d_lab), run_time=beat.until("tenth", offset=-0.1))
            self.play(Indicate(yl[2], color=BLUE, scale_factor=1.4), run_time=beat.until("every", offset=-0.1))
            self.play(*[Indicate(s, color=BLUE, scale_factor=1.0) for s in dseg],
                      *[Indicate(d, color=BLUE) for d in ddots], run_time=beat.remaining(min_time=0.8))
        self.chart_body = VGroup(ax, xl, yl, y_title, x_title, row_t, rows1, rows2, trail, r_dot, r_lab, r_how, d_lab)
        self.chart_top = VGroup(g_says, off50)
        self.rescue = VGroup(trail, r_dot, r_lab, r_how)
        self.chart_ax = ax
        self.chart_gp, self.chart_dp = gp, dp
        self.chart_xl = xl
        self.chart_gline = VGroup(*gseg, *gdots)
        self.chart_dline = VGroup(*dseg, *ddots)
        self.chart_ddots = VGroup(*ddots)

    # ================================================================== 1:40 shadows
    def shadows(self):
        sq = self.sq
        left = VGroup(sq["frame_L"], sq["disc_L"], sq["gdots"], sq["g_title"])
        right = VGroup(sq["frame_R"], sq["disc_R"], sq["ddots"], sq["d_title"])
        rail_y = -2.3
        rail_Lt = Line(sq_pt(L_C, 0, 0), sq_pt(L_C, 1, 0), color=GRAY, stroke_width=2.5).set_y(rail_y)
        rail_Rt = Line(sq_pt(R_C, 0, 0), sq_pt(R_C, 1, 0), color=GRAY, stroke_width=2.5).set_y(rail_y)

        def tick(x, color):
            return Line([x, rail_y - 0.13, 0], [x, rail_y + 0.13, 0], color=color, stroke_width=3)
        g_ticks = VGroup(*[tick(d.get_x(), PURPLE) for d in sq["gdots"]])
        d_ticks = VGroup(*[tick(d.get_x(), BLUE).set_stroke(width=2) for d in sq["ddots"]])
        g_lab = formula(r"10", r"\text{ values}", size=40, color=PURPLE).move_to([L_C[0], rail_y - 0.58, 0])
        d_lab = formula(r"100", r"\text{ values}", size=40, color=BLUE).move_to([R_C[0], rail_y - 0.58, 0])
        under_L = VGroup(sq["frame_L"].xl, sq["frame_L"].ticks[0], sq["frame_L"].ticks[1])
        under_R = VGroup(sq["frame_R"].xl, sq["frame_R"].ticks[0], sq["frame_R"].ticks[1])
        with self.narrate("Look at the shadows on one axis: the grid's hundred points cast ten, a hundred "
                          "darts cast a hundred.") as beat:
            # zoom back into the d = 2 column of the chart: its two dots open into the two squares
            self.play(Indicate(self.chart_xl[0], color=YELLOW, scale_factor=1.3),
                      FadeOut(self.chart_body), FadeOut(self.chart_top), FadeOut(self.chart_gline),
                      FadeOut(self.chart_dline),
                      GrowFromPoint(left, self.chart_gp[0]), GrowFromPoint(right, self.chart_dp[0]),
                      run_time=beat.until("one", offset=-0.2, min_time=1.0))
            self.play(TransformFromCopy(sq["frame_L"].bottom, rail_Lt), TransformFromCopy(sq["frame_R"].bottom, rail_Rt),
                      run_time=beat.until("axis", end=True, min_time=0.6))
            self.play(TransformFromCopy(sq["gdots"], g_ticks), under_L.animate.set_opacity(0.2),
                      run_time=beat.until("ten", offset=-0.1, min_time=0.6))
            self.play(FadeIn(g_lab, shift=0.1 * UP), under_L.animate.set_opacity(1), run_time=0.5)
            self.play(TransformFromCopy(sq["ddots"], d_ticks), under_R.animate.set_opacity(0.2),
                      run_time=beat.until("hundred", 3, offset=-0.1, min_time=0.6))
            self.play(FadeIn(d_lab, shift=0.1 * UP), under_R.animate.set_opacity(1), run_time=0.5)
        # ---- the formula, built from the picture: 100 points, 2 axes -> 10 values per axis
        conc = MathTex("100", r"^{1/", "2", "}", "=", "10", r"\text{ values}", font_size=40, color=PURPLE)
        conc[2].set_color(YELLOW)
        conc.shift(g_lab[0].get_center() - conc[5].get_center())
        gen = MathTex("N", r"^{1/", "d", "}", r"\text{ values}", r"\text{ per axis}", font_size=40, color=PURPLE)
        gen[2].set_color(YELLOW)
        gen.move_to(g_lab)
        axes_L = VGroup(sq["frame_L"].bottom, sq["frame_L"].left)
        # the specific case is assembled from the picture while the general rule is spoken, then generalised
        with self.narrate("With N points over d axes, [pause 0.4] each axis gets the d-th root of N. [pause 0.3]",
                          gap=0.25) as beat:
            self.play(TransformFromCopy(sq["gdots"], conc[0]), Indicate(sq["gdots"], color=PURPLE, scale_factor=1.02),
                      run_time=beat.until("over", offset=-0.05, min_time=0.7))
            self.play(axes_L.animate(rate_func=there_and_back).set_stroke(YELLOW, width=5),
                      TransformFromCopy(axes_L, conc[2]), FadeIn(conc[1]),
                      run_time=beat.until("axes", end=True, min_time=0.7))
            self.play(FadeIn(conc[4]), ReplacementTransform(g_lab[0], conc[5]),
                      ReplacementTransform(g_lab[1], conc[6]),
                      g_ticks.animate(rate_func=there_and_back).set_stroke(width=5), run_time=0.6)
            self.wait_beat(beat, "d-th", offset=-0.5)
            self.play(FadeOut(conc[4:6], shift=0.15 * DOWN), run_time=0.35)
            self.play(ReplacementTransform(conc[0], gen[0]), ReplacementTransform(conc[1], gen[1]),
                      ReplacementTransform(conc[2], gen[2]), ReplacementTransform(conc[6], gen[4]),
                      FadeIn(gen[5], shift=0.15 * LEFT), run_time=beat.until("N", 2, end=True, min_time=0.9))
            self.add(gen)
            self.play(flag(gen[0:3], color=PURPLE), run_time=beat.remaining(min_time=0.6))
        self.shadow_stuff = dict(rail_Lt=rail_Lt, rail_Rt=rail_Rt, g_ticks=g_ticks, d_ticks=d_ticks, d_lab=d_lab)
        self.gen = gen

    # ================================================================== 2:03 the diagonal: shadows alone are not the fix
    def diagonal(self):
        sq, sh = self.sq, self.shadow_stuff
        grid_side = VGroup(sq["frame_L"], sq["disc_L"], sq["gdots"], sq["g_title"], sh["rail_Lt"], sh["g_ticks"])
        dart_sq = VGroup(sq["frame_R"], sq["disc_R"], sq["ddots"])
        shift = B_L - R_C
        m_axes = VGroup(*[Line(mp(i, 0), mp(i, 1), color=DIM, stroke_width=1.2, stroke_opacity=0.8)
                          for i in range(100)])
        m_lab = VGroup(MathTex("0", font_size=MATH_SMALL, color=GRAY).next_to(mp(0, 0), LEFT, buff=0.18),
                       MathTex("1", font_size=MATH_SMALL, color=GRAY).next_to(mp(0, 1), LEFT, buff=0.18))
        t2 = text("2 dimensions", size=32, t2c={"2": YELLOW}).move_to([B_L[0], TITLE_Y, 0]).set_opacity(0.25)
        t100 = text("100 dimensions", size=32, t2c={"100": YELLOW}).move_to([MCX, TITLE_Y, 0])
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
        one_pt = VGroup(text("one point:", size=26, color=PURPLE),
                        MathTex(r"(t, t, \dots, t)", font_size=36, color=PURPLE)).arrange(DOWN, buff=0.12,
                                                                                         aligned_edge=RIGHT)
        one_pt.next_to(mp(0, ts[k1]), LEFT, buff=0.42)
        edge_lab = text("ball's edge", size=26).next_to(mp(0, dg["t_max"]), LEFT, buff=0.42)
        rest = VGroup(*[l for i, l in enumerate(flat) if i != k1])
        sq_target = dart_sq.copy().shift(shift)
        sq_dim = sq_target.copy().fade(0.75)
        with self.narrate("But shadows alone are not the fix. [pause 0.15] A million points on the diagonal, "
                          "each one a flat line here, give every axis a million values, and still miss by eight "
                          "points. [pause 0.6]", gap=0.25) as beat:
            self.play(sh["d_ticks"].animate(rate_func=there_and_back).set_stroke(width=4),
                      sh["d_lab"].animate(rate_func=there_and_back).scale(1.12),
                      run_time=beat.until("fix", offset=-0.1, min_time=0.7))
            self.play(FadeOut(grid_side), FadeOut(self.gen), FadeOut(sh["rail_Rt"]), FadeOut(sh["d_ticks"]),
                      FadeOut(sh["d_lab"]), FadeOut(sq["d_title"]),
                      Transform(dart_sq, sq_dim),
                      FadeIn(t2), FadeIn(t100), Create(m_axes, lag_ratio=0.01), FadeIn(m_lab),
                      run_time=beat.until("million", offset=-0.2, min_time=1.0))
            self.play(FadeIn(diag_lab, shift=0.1 * UP), run_time=beat.until("each", offset=-0.1, min_time=0.6))
            # one point, alone, for over a second
            self.play(Create(flat[k1]), FadeIn(one_pt, shift=0.1 * RIGHT), run_time=beat.until("flat", offset=-0.1))
            self.play(flat[k1].animate(rate_func=there_and_back).set_stroke(width=5),
                      run_time=beat.until("give", offset=-0.1, min_time=0.6))
            self.play(LaggedStart(*[Create(l) for l in rest], lag_ratio=0.08),
                      run_time=beat.until("million", 2, offset=-0.2, min_time=1.0), rate_func=linear)
            self.play(m_axes.animate(rate_func=there_and_back).set_stroke(PURPLE, width=2.2, opacity=1),
                      run_time=beat.until("and", offset=-0.2, min_time=0.6))
            # lines below the ball's edge stay solid (inside); those above turn dashed (outside)
            outside = [l for l, t in zip(flat, ts) if t > dg["t_max"]]
            dashed = VGroup(*[DashedLine(l.get_start(), l.get_end(), dash_length=0.08, color=PURPLE,
                                         stroke_width=2.2).set_opacity(0.45) for l in outside])
            self.play(Create(level), FadeIn(edge_lab, shift=0.1 * RIGHT),
                      *[ReplacementTransform(l, d) for l, d in zip(outside, dashed)],
                      run_time=beat.until("by", offset=0.0, min_time=0.7))
            self.play(FadeIn(res, shift=0.1 * UP), run_time=beat.until("points", 2, offset=0.0, min_time=0.4))
        flat = VGroup(*[l for l, t in zip(flat, ts) if t <= dg["t_max"]], *dashed)
        self.t2, self.t100, self.sq_target = t2, t100, sq_target
        self.panel = VGroup(m_axes, m_lab)
        self.diag_stuff = VGroup(flat, level, diag_lab, res, one_pt, edge_lab)

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
        with self.narrate("Darts win another way: each one lands inside with a chance equal to the answer, on "
                          "its own, in two dimensions or a hundred. [pause 0.2] Their estimate is a share of "
                          "heads in N coin flips.") as beat:
            self.play(FadeOut(self.diag_stuff), Transform(dart_sq, self.sq_target), Create(ring), Create(hero),
                      self.t2.animate.set_opacity(1),
                      run_time=beat.until("each", offset=-0.1, min_time=1.0))
            self.play(Create(gL.track), Create(gL.tick), FadeIn(gL.lhs), FadeIn(gL.num), run_time=0.4)
            gL.bar.add_updater(gL.follow)
            self.add(gL.bar)
            self.play(gL.v.animate(rate_func=linear).set_value(D["dart2d_sum_sq"]),
                      run_time=beat.until("chance", offset=-0.1, min_time=0.8))
            gL.bar.clear_updaters()
            self.play(FadeIn(gL.rel), FadeIn(gL.rv), FadeIn(gL.result, shift=0.1 * UP), run_time=0.5)
            self.play(Create(gR.track), Create(gR.tick), FadeIn(gR.lhs), FadeIn(gR.num),
                      hero.animate.set_stroke(width=4.5),
                      run_time=beat.until("answer", offset=-0.1, min_time=0.4))
            gR.bar.add_updater(gR.follow)
            self.add(gR.bar)
            self.play(gR.v.animate(rate_func=linear).set_value(D["dart100"]["sum_sq"]),
                      disc_fill.animate(rate_func=there_and_back).set_fill(opacity=0.35),
                      run_time=beat.until("hundred", offset=-0.6, min_time=1.0))
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
            box.set_stroke(GRAY, 2, opacity=0.3)
            # the other 99 darts of the 100-D run, each one a faint polyline on the panel
            others = VGroup(*[polyline([mp(i, W[k][i]) for i in range(100)], BLUE, 1.2, 0.1) for k in range(1, 100)])
            self.wait_beat(beat, "Their", offset=-0.15)
            # everything but each dart's verdict steps away; the verdict becomes that dart's coin,
            # then the other 99 darts follow
            self.play(FadeOut(VGroup(frame.ticks, frame.xl, frame.yl, sq["disc_R"], ring)),
                      frame_lines.animate.set_stroke(opacity=0.3),
                      *[FadeOut(VGroup(g.track, g.tick, g.bar, g.readout)) for g in (gL, gR)], run_time=0.4)
            cL0, cR0 = coinsL[0].copy(), coinsR[0].copy()
            self.play(FadeTransform(gL.result, cL0), ReplacementTransform(dart1, coinsL[0]),
                      FadeTransform(gR.result, cR0), ReplacementTransform(hero, coinsR[0]),
                      run_time=beat.until("share", offset=-0.1, min_time=0.6))
            self.remove(gL.result, gR.result, cL0, cR0)
            self.play(FadeIn(others), run_time=0.5)
            self.play(*[ReplacementTransform(d, c) for d, c in zip(sq["ddots"][1:], coinsL[1:])],
                      *[ReplacementTransform(o, c) for o, c in zip(others, coinsR[1:])],
                      Transform(frame_lines, box), FadeOut(self.panel),
                      run_time=beat.until("coin", offset=-0.1, min_time=0.8))
            self.play(FadeIn(kL, shift=0.1 * UP), FadeIn(kR, shift=0.1 * UP), run_time=0.7)
        # ---- one coin, close up: always exactly a half from its average
        ml = Line([-0.85, ML_Y, 0], [0.85, ML_Y, 0], color=GRAY, stroke_width=2.5)
        ml_t = VGroup(MathTex("0", font_size=MATH_SMALL, color=GRAY).next_to([-0.85, ML_Y, 0], DOWN, buff=0.24),
                      MathTex("1", font_size=MATH_SMALL, color=GRAY).next_to([0.85, ML_Y, 0], DOWN, buff=0.24))
        cap = text("one yes/no dart", size=28, color=GRAY).move_to([0, 1.85, 0])     # not scaled with the line
        mean = DashedLine([0, ML_Y - 0.12, 0], [0, ML_Y + 0.6, 0], color=INK, stroke_width=2,
                          dash_length=0.07).set_opacity(0.6)
        mean_lab = MathTex(r"\tfrac12", font_size=36, color=INK).next_to([0, ML_Y, 0], DOWN, buff=0.15)
        coin0 = marker([-0.85, ML_Y, 0], BLUE, False, r=0.075)
        coin1 = marker([0.85, ML_Y, 0], BLUE, True, r=0.075)
        coin0b = marker([-0.85, ML_Y, 0], BLUE, False, r=0.075)
        by = ML_Y + 0.32

        def miss(xc):
            lab = MathTex(r"\tfrac12", font_size=36, color=RED)
            return bracket(min(xc, 0), max(xc, 0), by, lab, side=UP)
        miss1, miss0 = miss(0.85), miss(-0.85)
        small_c = np.array([0.0, ML_Y, 0.0])

        def big(*ms):
            for m in ms:
                m.scale(BIG, about_point=small_c).shift(BIG_C - small_c)
        big(ml, ml_t, mean, mean_lab, coin0, coin1, coin0b, miss1, miss0)
        t2, t100 = self.t2, self.t100
        with self.narrate("One flip is zero or one. [pause 0.15] Its average is a half, and every flip misses "
                          "that by exactly a half.", gap=0.35) as beat:
            self.play(TransformFromCopy(coinsL[0], coin0), Create(ml), FadeIn(ml_t), FadeIn(cap),
                      VGroup(t2, t100).animate.set_y(TITLE_Y2),
                      run_time=beat.until("or", offset=-0.1, min_time=0.8))
            self.play(Transform(coin0, coin1), run_time=beat.until("Its", offset=-0.1, min_time=0.5))
            self.play(Create(mean), FadeIn(mean_lab, shift=0.1 * UP), run_time=beat.until("and", offset=-0.1, min_time=0.6))
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
            hx = NumberLine(x_range=[lo, hi, 0.1], length=5.0, color=GRAY, stroke_width=2.5,
                            include_tip=False, tick_size=0.06)
            hx.move_to([cx, HIST_Y, 0])
            labs = VGroup(*[MathTex(f"{round(t * 100)}\\%", font_size=MATH_SMALL, color=GRAY)
                            .next_to(hx.n2p(t), DOWN, buff=0.18) for t in (0.3, 0.4, 0.5, 0.6, 0.7)])
            sx = hx.n2p(0.312)[0]
            bar = VGroup(Line([sx, HIST_Y, 0], [sx, HIST_Y + 0.5, 0], color=GRAY, stroke_width=2),
                         Line([sx - 0.05, HIST_Y + 0.5, 0], [sx + 0.05, HIST_Y + 0.5, 0], color=GRAY, stroke_width=2))
            bar_lab = text("10 runs", size=22, color=GRAY).next_to(bar, UP, buff=0.12)
            return hx, labs, (VGroup(bar, bar_lab) if scale_label else VGroup(bar))
        hL, labL, scL = hist_axes(L_C[0])
        hR, labR, scR = hist_axes(R_C[0], scale_label=False)
        x_name = text("estimate from one experiment", size=26, color=GRAY).move_to([0, -2.95, 0])
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
        n4 = formula("N", r"= 400", r"\text{ darts}", size=36, color=BLUE).move_to(n_txt)
        run_ct = VGroup(text("simulated experiments:", size=26, color=GRAY),
                        Integer(1, font_size=36, color=INK)).arrange(RIGHT, buff=0.15)
        run_ct.move_to([0, 2.15, 0])
        run_ct[1].add_updater(lambda m: m.set_value(int(round(runs.get_value()))))
        peak = lambda est: counts(est, 300).max() * unit
        brL = LiveBracket(hL, H["100_2"]["sd"], HIST_Y + peak(estL) + 0.3, side=LEFT)
        brR = LiveBracket(hR, H["100_100"]["sd"], HIST_Y + peak(estR) + 0.3)
        coin_line = self.coin_line
        ml_c = coin_line[0].get_center()
        with self.narrate("Repeat the hundred-dart experiment three hundred times. [pause 0.2] In two dimensions "
                          "the estimates spread this wide; in a hundred, just as wide. [pause 0.25] Quadruple the "
                          "darts, and both get twice as narrow.") as beat:
            # the close-up settles at 0.75x between the histograms as their axes are drawn
            self.play(coin_line.animate.scale(SLOT, about_point=ml_c).shift(SLOT_C - ml_c),
                      FadeOut(self.coin_cap), FadeOut(self.coin_box), Create(hL), Create(hR), FadeIn(labL),
                      FadeIn(labR), FadeIn(x_name), FadeIn(scL), FadeIn(scR), Write(n_txt), run_time=1.0)
            self.play(ReplacementTransform(VGroup(coinsL, kL), barsL[14]),
                      ReplacementTransform(VGroup(coinsR, kR), barsR[18]), FadeIn(run_ct),
                      run_time=beat.until("three", offset=-0.5, min_time=0.8))
            self.remove(barsL[14], barsR[18])
            self.add(barsL, barsR)
            self.play(Create(truthL), Create(truthR), run_time=0.4)
            barsL.add_updater(upd(hL, estL))
            barsR.add_updater(upd(hR, estR))
            self.play(runs.animate.set_value(300), run_time=beat.until("spread", offset=-0.1),
                      rate_func=linear)
            barsL.clear_updaters()
            barsR.clear_updaters()
            self.play(GrowFromCenter(brL), run_time=0.6)
            self.wait_beat(beat, "just", offset=-0.2)
            self.play(GrowFromCenter(brR), run_time=0.6)
            # quadruple: the bars reshape; each bracket's width, height and number follow
            est4L, est4R = H["400_2"]["estimates"], H["400_100"]["estimates"]
            new_L, new_R = make_bars(hL, est4L, 300), make_bars(hR, est4R, 300)
            self.wait_beat(beat, "Quadruple", offset=-0.1)
            self.play(TransformMatchingTex(n_txt, n4, key_map={r"= 100": r"= 400"}), run_time=0.8)
            brL.add_updater(LiveBracket.refresh)
            brR.add_updater(LiveBracket.refresh)
            self.play(Transform(barsL, new_L), Transform(barsR, new_R),
                      brL.w.animate.set_value(H["400_2"]["sd"]), brL.yv.animate.set_value(HIST_Y + peak(est4L) + 0.3),
                      brR.w.animate.set_value(H["400_100"]["sd"]), brR.yv.animate.set_value(HIST_Y + peak(est4R) + 0.3),
                      FadeOut(run_ct), run_time=beat.until("narrow", offset=0.3))
            brL.clear_updaters()
            brR.clear_updaters()

        # ---- why root N: sixteen +-1/2 misses, at random, partly cancel (a random walk)
        seq = D["darts2d"]["inside"][WALK_IDX[0]:WALK_IDX[1]]
        steps = [1 if v else -1 for v in seq]
        cum = np.concatenate([[0], np.cumsum(steps)])
        net_n = int(cum[-1])
        assert len(steps) == 16 and net_n == 4
        P = [W0 + np.array([k * W_DX, c * W_U, 0]) for k, c in enumerate(cum)]
        G = [W0 + np.array([k * W_DX, k * W_U, 0]) for k in range(17)]

        def step_arrow(a, b, opacity=1.0):
            return Arrow(a, b, buff=0, color=RED, stroke_width=3.5, tip_length=0.11,
                         max_tip_length_to_length_ratio=0.4,
                         max_stroke_width_to_length_ratio=20).set_opacity(opacity)
        walk = VGroup(*[step_arrow(P[k], P[k + 1]) for k in range(16)])
        ghost = VGroup(*[step_arrow(G[k], G[k + 1], 0.3) for k in range(16)])
        base = DashedLine(W0, W0 + RIGHT * (16 * W_DX + 0.5), color=INK, stroke_width=2,
                          dash_length=0.07).set_opacity(0.6)
        bx = P[-1][0] + 0.3
        net = VGroup(Line([bx, W0[1], 0], [bx, P[-1][1], 0]),
                     Line([bx - 0.08, W0[1], 0], [bx + 0.08, W0[1], 0]),
                     Line([bx - 0.08, P[-1][1], 0], [bx + 0.08, P[-1][1], 0])).set_stroke(RED, 3)
        net_lab = MathTex(str(net_n), r"\text{ halves}", font_size=36, color=RED).next_to(net, RIGHT, buff=0.2)
        net_labN = MathTex(r"\sqrt{N}", r"\text{ halves}", font_size=36, color=RED)
        net_labN[0].set_color(BLUE)
        net_labN.move_to(net_lab, aligned_edge=LEFT)
        g16 = MathTex("16", r"\text{ halves}", font_size=36, color=RED)
        g_note = text("if they never cancelled", size=26, color=GRAY)
        ghost_lab = VGroup(g16, g_note).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        ghost_lab.next_to(G[-1], RIGHT, buff=0.3).align_to(G[-1] + UP * 0.22, UP)
        gN = MathTex("N", r"\text{ halves}", font_size=36, color=RED).move_to(g16, aligned_edge=LEFT)
        gN[0].set_color(BLUE)
        eq = spread_eq(r"\tfrac{1}{2}", "N").move_to(EQ_POS)
        self.own(eq, net_lab, net_labN, g16, gN)
        hist_all = VGroup(barsL, barsR, truthL, truthR, hL, hR, labL, labR, brL, brR, x_name, scL, scR, n4,
                          self.t2, self.t100)
        miss = self.coin_miss
        with self.narrate("Each dart misses by a half, up or down at random, so the misses partly cancel: sixteen "
                          "darts stray about four halves, not sixteen. [pause 0.25] N darts stray about root N "
                          "halves; per dart, that's a half over the square root of N. [pause 0.8]") as beat:
            # the histograms have made their point; the coin line moves aside to feed the walk
            cur = coin_line[0].get_center()
            self.play(FadeOut(hist_all), coin_line.animate.shift(CORNER_C - cur), Create(base), run_time=0.7)
            # each step is a copy of the coin's half-miss: up for a dart inside, down for one outside
            self.play(LaggedStart(*[TransformFromCopy(miss[0], a) for a in walk], lag_ratio=0.15),
                      run_time=beat.until("random", end=True, min_time=1.6))
            downs = VGroup(*[a for a, st in zip(walk, steps) if st < 0])
            self.play(downs.animate(rate_func=there_and_back).set_stroke(width=7),
                      run_time=beat.until("sixteen", offset=-0.1, min_time=0.8))
            self.play(GrowFromEdge(net, DOWN), run_time=beat.until("four", offset=-0.1, min_time=0.5))
            self.play(FadeIn(net_lab, shift=0.1 * LEFT), run_time=0.5)
            self.wait_beat(beat, "not", offset=-0.15)
            self.play(TransformFromCopy(walk, ghost), FadeIn(ghost_lab, shift=0.1 * LEFT),
                      run_time=beat.until("N", offset=-0.1, min_time=0.9))
            self.play(TransformMatchingTex(g16, gN), run_time=0.5)
            self.wait_beat(beat, "root", offset=-0.15)
            self.play(TransformMatchingTex(net_lab, net_labN), run_time=0.6)
            # the formula, every term from its referent
            self.wait_beat(beat, "per", offset=-0.1)
            self.play(Write(eq[0:2]), run_time=beat.until("half", 2, offset=-0.15, min_time=0.6))
            self.play(TransformFromCopy(self.coin_half, eq[2][:-1]), Create(eq[2][-1]),
                      run_time=beat.until("square", offset=-0.1, min_time=0.6))
            self.play(TransformFromCopy(net_labN[0], eq[3:5]), FadeIn(eq[5]),
                      run_time=beat.until("N", 3, end=True, min_time=0.7))
            self.add(eq)
            self.play(flag(eq[2:5], color=INK), run_time=0.8)
        # ---- any other function: its own spread sigma; then the grid's error law beneath
        LAW_Y = 1.45                                 # the darts' law sits here once the walk has gone
        eq_s = spread_eq(r"\sigma", "N").move_to(eq)
        self.own(eq, eq_s)
        eq_s.shift(eq[0].get_center() - eq_s[0].get_center() + DOWN * (EQ_POS[1] - LAW_Y))
        sig_tag = MathTex(r"\sigma", r"\text{ = one dart's spread}", font_size=34, color=GRAY)
        sig_tag[0].set_color(RED)
        sig_tag.next_to(eq_s, RIGHT, buff=0.45)
        no_d = MathTex(r"\text{no }", "d", font_size=36, color=GRAY)
        no_d[1].set_color(YELLOW)
        g_law = MathTex(r"\text{error}", r"\;\propto\;", "N", r"^{-2/", "d", "}", font_size=EQ_SIZE)
        g_law[0].set_color(RED)
        g_law[1:].set_color(PURPLE)
        g_law[4].set_color(YELLOW)
        g_law.move_to([0, LAW_Y - 2.35, 0]).align_to(eq_s, LEFT)
        self.own(g_law)
        hd_x = eq_s.get_left()[0] - 0.4
        d_hd = text("darts:", size=28, color=BLUE)
        d_hd.move_to([hd_x, eq_s[2][-1].get_y(), 0], aligned_edge=RIGHT)
        g_hd = text("grid, smooth f:", size=28, color=PURPLE, t2s={" f": ITALIC})
        g_hd.move_to([hd_x, g_law[0].get_y(), 0], aligned_edge=RIGHT)
        g_cite = citation("Glasserman, 2003 · Monte Carlo Methods in Financial Engineering, §1.1")
        walk_all = VGroup(walk, ghost, base, net, net_labN, gN, g_note, coin_line)
        with self.narrate("Any other function swaps that half for its own spread, sigma. [pause 0.6] The root "
                          "N stays, and there's no d in it. [pause 0.2] A grid's error, even for smooth "
                          "functions, has d in its exponent.", gap=self.BOUNDARY) as beat:
            self.play(FadeOut(walk_all), eq.animate.shift(DOWN * (EQ_POS[1] - LAW_Y)),
                      run_time=beat.until("swaps", offset=-0.1, min_time=0.8))
            self.wait_beat(beat, "half", offset=-0.15)
            self.play(flag(eq[2][:-1], color=RED), run_time=0.8)
            self.wait_beat(beat, "sigma", offset=-0.3)
            self.play(FadeTransform(eq[2][:-1], eq_s[2][:-1]), Transform(eq[2][-1], eq_s[2][-1]),
                      *[Transform(eq[i], eq_s[i]) for i in (0, 1, 3, 4)], run_time=0.5)
            self.swap(eq, eq_s)
            self.play(flag(eq_s[2][:-1], color=RED), FadeIn(sig_tag, shift=0.1 * LEFT), run_time=0.8)
            self.wait_beat(beat, "root", offset=-0.1)
            self.play(flag(eq_s[3:5], color=BLUE), FadeIn(d_hd, shift=0.1 * RIGHT),
                      run_time=beat.until("no", offset=-0.1, min_time=0.8))
            no_d.next_to(eq_s[3:5], DOWN, buff=0.22)
            self.play(FadeIn(no_d, shift=0.1 * UP), run_time=0.6)
            self.wait_beat(beat, "grid", offset=-0.1)
            # the grid's law; its d is the one the darts' formula lacks
            self.play(Write(g_law[0:4]), FadeIn(g_hd, shift=0.1 * RIGHT), FadeIn(g_cite, shift=0.1 * UP),
                      TransformFromCopy(no_d[1], g_law[4]), FadeIn(g_law[5]),
                      run_time=beat.until("has", offset=-0.1, min_time=1.0))
            self.add(g_law)
            self.play(Indicate(g_law[4], color=YELLOW, scale_factor=1.5),
                      Indicate(no_d[1], color=YELLOW, scale_factor=1.3), run_time=beat.remaining(min_time=0.9))
        self.hold(1.0)                              # both laws, one above the other
        self.eq_s, self.sig_tag, self.no_d = eq_s, sig_tag, no_d
        self.laws = VGroup(g_law, g_hd, d_hd, g_cite)

    # ================================================================== 2:45 the prediction
    def prediction(self):
        eq_s, no_d = self.eq_s, self.no_d
        k = 1.15
        target_c = np.array([0, 0.6, 0])
        # every stage is built at the final (centred, enlarged) size
        sz = EQ_SIZE * k
        eq_h = spread_eq(r"\tfrac{1}{2}", "N", size=sz)
        eq_m = spread_eq(r"\tfrac{1}{2}", r"1{,}000{,}000", size=sz)
        eq_k = MathTex(r"\text{spread}", "=", r"\frac{\tfrac{1}{2}}{", r"1000", "}", font_size=sz)
        eq_k[0].set_color(RED)
        eq_k[2][:-1].set_color(RED)
        eq_k[3].set_color(BLUE)
        eq_v = MathTex(r"\text{spread}", "=", r"0.0005", "=", r"0.05\text{ points}", font_size=sz)
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
        moved = VGroup(eq_s, no_d)
        moved_t = moved.copy().scale(k)
        moved_t.shift(target_c - moved_t[0].get_center())
        with self.narrate("So, back to our ball, with a million darts, in any dimension: how far off is a "
                          "typical estimate? [pause 1.5] One half over a thousand: five hundredths of a point. "
                          "[pause 0.8] Two runs in three land closer; all six of ours did.",
                          gap=self.BOUNDARY) as beat:
            # everything else leaves; the formula takes the centre of the frame
            self.play(FadeOut(self.laws), FadeOut(self.sig_tag),
                      Transform(moved, moved_t), run_time=beat.until("ball", offset=-0.05, min_time=0.6))
            # sigma -> 1/2: our ball is a yes/no question whose answer is one half
            self.play(FadeTransform(eq_s[2][:-1], eq_h[2][:-1]), Transform(eq_s[2][-1], eq_h[2][-1]),
                      *[Transform(eq_s[i], eq_h[i]) for i in (0, 1, 3, 4)], run_time=0.45)
            self.swap(eq_s, eq_h)
            self.play(flag(eq_h[2][:-1], color=RED), run_time=beat.until("million", offset=0.05, min_time=0.5))
            self.play(FadeTransform(eq_h[4], eq_m[4]), Transform(eq_h[3], eq_m[3]),
                      *[Transform(eq_h[i], eq_m[i]) for i in (0, 1, 2)],
                      no_d.animate.next_to(eq_m[3:5], DOWN, buff=0.25), run_time=0.6)
            self.swap(eq_h, eq_m)
            self.wait_beat(beat, "dimension", offset=-0.25)
            self.play(Indicate(no_d, color=YELLOW, scale_factor=1.2), run_time=0.7)
            self.play(FadeOut(no_d), run_time=0.4)
            self.wait_beat(beat, "how", offset=-0.2)
            q.next_to(eq_m, RIGHT, buff=0.25).shift(LEFT * room)
            self.play(eq_m.animate.shift(LEFT * room), FadeIn(q, shift=0.1 * LEFT), run_time=0.6)
            self.wait_beat(beat, "One", offset=-0.15)
            self.play(FadeTransform(VGroup(eq_m[3], eq_m[4]), eq_k[3]),
                      *[Transform(eq_m[i], eq_k[i]) for i in (0, 1, 2)],
                      q.animate.next_to(eq_k, RIGHT, buff=0.25),
                      run_time=beat.until("thousand", end=True, offset=-0.15, min_time=0.8))
            self.swap(eq_m, eq_k)
            # the question mark becomes the answer
            self.play(Transform(eq_k[0], eq_v[0]), Transform(eq_k[1], eq_v[1]),
                      FadeTransform(VGroup(eq_k[2], eq_k[3]), eq_v[2]),
                      FadeTransform(q, VGroup(eq_v[3], eq_v[4])), run_time=0.9)
            self.swap(eq_k, eq_v[0], eq_v[1], eq_v[2], eq_v[3], eq_v[4])
            self.remove(*eq_v)
            self.add(eq_v)
            self.play(flag(eq_v[4], color=RED), run_time=0.8)
            self.wait_beat(beat, "closer", offset=-0.15)
            # the chart returns: the formula's answer becomes its dashed line
            ax = self.chart_ax
            yv = ax.Y(D["darts_typical_error_points"])
            pred = DashedLine(ax.c2p(0, yv), ax.c2p(1.84, yv), color=BLUE, stroke_width=3, dash_length=0.12)
            # one label, just above its own line, in the empty band between d = 20 and d = 100
            pred_lab = VGroup(text("typical miss:", size=26, color=BLUE),
                              MathTex(r"0.05\text{ points}", font_size=36, color=RED)).arrange(RIGHT, buff=0.2)
            pred_lab.move_to(ax.c2p(ax.X(20), yv) + np.array([0.3, 0.2, 0]), aligned_edge=DL)
            # the grid's annotations come back as 40 % context: the focus is the darts and their line
            self.chart_top.fade(0.6)
            self.rescue.fade(0.6)
            self.play(Create(pred), ReplacementTransform(eq_v[4], pred_lab[1]),
                      FadeOut(VGroup(eq_v[0], eq_v[1], eq_v[2], eq_v[3])),
                      FadeIn(self.chart_body), FadeIn(self.chart_top), FadeIn(self.chart_gline),
                      FadeIn(self.chart_dline),
                      run_time=beat.until("all", offset=-0.1, min_time=0.9))
            self.remove(*eq_v.get_family())
            self.play(FadeIn(pred_lab[0], shift=0.1 * RIGHT), run_time=0.5)
            self.play(*[Indicate(d, color=BLUE, scale_factor=1.6) for d in self.chart_ddots],
                      run_time=beat.remaining(min_time=0.8))
        self.chart_extra = VGroup(pred, pred_lab, self.chart_top)

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
        score = VGroup(text("model score", size=26, color=GRAY), text("(schematic)", size=22, color=GRAY))
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
        with self.narrate("In 2012, Bergstra and Bengio found that random search tuned neural networks as well as "
                          "grid search, in a fraction of the time. [pause 0.2] If one setting matters most, nine "
                          "grid trials test three values of it; nine random trials test nine.",
                          gap=self.BOUNDARY) as beat:
            # the chart's two error curves become the two methods of the same contest
            self.play(ReplacementTransform(self.chart_gline, tL), ReplacementTransform(self.chart_dline, tR),
                      FadeOut(self.chart_body), FadeOut(self.chart_extra),
                      run_time=beat.until("Bergstra", offset=-0.2, min_time=1.2))
            self.play(Create(fL[:3]), Create(fR[:3]), FadeIn(fL[3:]), FadeIn(fR[3:]), FadeIn(cite, shift=0.1 * UP),
                      run_time=0.8)
            self.play(LaggedStart(*[GrowFromCenter(d) for d in gd], lag_ratio=0.85),
                      LaggedStart(*[GrowFromCenter(d) for d in rd], lag_ratio=0.85),
                      run_time=beat.until("If", offset=-0.3))
            self.play(Create(cvL), Create(cvR), FadeIn(score), Indicate(fL.xl, color=INK, scale_factor=1.08),
                      Indicate(fR.xl, color=INK, scale_factor=1.08), run_time=beat.until("nine", offset=-0.1))
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
        y_t = text("share of box inside a radius-1 ball", size=26, color=GRAY)
        y_t.next_to(c2p(1, 0), UP, buff=0.35).align_to(yl, LEFT)
        x_t = text("dimensions", size=26, color=GRAY).move_to([ax.get_center()[0], xl.get_bottom()[1] - 0.3, 0])
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
        zone_lab = text("under 1 hit expected", size=26, color=RED)
        zone_lab2 = VGroup(text("darts report 0:", size=26, color=RED),
                           text("off by the whole answer", size=26, color=RED)).arrange(DOWN, buff=0.16,
                                                                                         aligned_edge=LEFT)
        zone_lab2.move_to([zx0 + 0.1, c2p(1, LO)[1] + 0.18, 0], aligned_edge=DL)
        zone_lab.move_to(zone_lab2[1], aligned_edge=LEFT)
        with self.narrate("Darts do have a blind spot: tiny answers. [pause 0.2] By thirty dimensions, a "
                          "radius-one ball fills two parts in a hundred trillion of the box. [pause 0.2] Below "
                          "this line, a million darts expect under one hit, so they usually report zero: off by "
                          "the whole answer.", gap=0.1) as beat:
            # the two search squares' axes become the new chart's axes (no empty frame)
            fL, fR = self.bb_frames
            self.play(FadeOut(VGroup(fL.rest, fL.xl, fL.yl, fR.rest, fR.xl, fR.yl,
                                     *[m for m in self.bb if m not in (fL, fR)])),
                      ReplacementTransform(VGroup(fL.bottom, fR.bottom), ax.x_axis),
                      ReplacementTransform(VGroup(fL.left, fR.left), ax.y_axis),
                      FadeIn(xl), FadeIn(yl), FadeIn(y_t), FadeIn(x_t), run_time=1.0)
            # the curve of ever tinier answers is drawn from "tiny answers" on
            self.play(Create(curve), LaggedStart(*[GrowFromCenter(d) for d in cdots], lag_ratio=0.05),
                      run_time=beat.until("two", offset=-0.1), rate_func=linear)
            self.play(Indicate(cdots[-1], color=INK, scale_factor=1.8), FadeIn(end_lab, shift=0.1 * UP),
                      run_time=1.0)
            self.wait_beat(beat, "line", offset=-0.4)
            self.play(Create(line), FadeIn(line_lab), run_time=0.8)
            self.play(FadeIn(zone), FadeIn(zone_lab), run_time=beat.until("hit", offset=-0.1, min_time=0.6))
            self.wait_beat(beat, "report", offset=-0.2)
            self.play(FadeTransform(zone_lab, zone_lab2[0]), run_time=0.6)
            self.play(FadeIn(zone_lab2[1], shift=0.1 * UP), run_time=beat.until("whole", offset=-0.1, min_time=0.5))
            self.play(flag(zone_lab2, color=RED), run_time=beat.remaining(min_time=0.8))
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
        base = Line(pc_pt(0, 0), pc_pt(99, 0), color=GRAY, stroke_width=1.6)
        # in the breath after the limit: its 1/N line becomes the cold-open header (same N), and its
        # x-axis becomes the floor the 100 input axes grow up from
        self.play(FadeOut(L["rest"]), ReplacementTransform(L["x_axis"], base),
                  ReplacementTransform(VGroup(L["line"], L["line_lab"]), n_lab), run_time=1.0)
        with self.narrate("The darts never noticed the axes: [pause 0.3] a million coin flips, in any "
                          "dimension.") as beat:
            self.play(LaggedStart(*[GrowFromEdge(a, DOWN) for a in axes_pc], lag_ratio=0.01),
                      FadeIn(ends), FadeIn(ins), FadeIn(d_lab), FadeOut(base),
                      run_time=beat.until("noticed", end=True, min_time=1.0))
            self.play(LaggedStart(*[GrowFromCenter(d) for d in centre], lag_ratio=0.01), Create(centre_line),
                      FadeIn(one_lab, shift=0.1 * LEFT), run_time=beat.until("axes", end=True, min_time=0.7))
            self.play(LaggedStart(*[Create(m) for m in many], lag_ratio=0.03),
                      run_time=beat.until("coin", offset=-0.1, min_time=1.0))
            self.play(FadeIn(bands), FadeIn(mil_lab, shift=0.1 * LEFT), run_time=beat.until("in", 1, offset=-0.1, min_time=0.6))
            self.play(Indicate(d_lab, color=YELLOW, scale_factor=1.06), run_time=beat.remaining(min_time=0.8))
        self.hold(0.3)
