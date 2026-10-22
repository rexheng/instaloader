"""Episode 20 - A Dinosaur Hiding in Your Summary Statistics.

    videos/toolkit/render.sh --preview videos/episodes/020-datasaurus/scene.py Episode /tmp/e20.mp4
    videos/toolkit/render.sh videos/episodes/020-datasaurus/scene.py Episode videos/episodes/020-datasaurus/final.mp4

Data: datasaurus_dozen.tsv (datasauRus CRAN package, Matejka & Fitzmaurice 2017) and
anscombe.csv (Anscombe 1973). Every number on screen is computed here from those files.
"""
import csv
import math
from pathlib import Path

import numpy as np
from manim import *
from scipy.optimize import linear_sum_assignment

from sample_space import *

HERE = Path(__file__).resolve().parent
N = 142


# ----------------------------------------------------------------------------- data
def load_dozen():
    out = {}
    with open(HERE / "datasaurus_dozen.tsv") as f:
        rows = csv.reader(f, delimiter="\t")
        next(rows)
        for name, x, y in rows:
            out.setdefault(name, []).append((float(x), float(y)))
    return {k: np.array(v) for k, v in out.items()}


def load_anscombe():
    out = {}
    with open(HERE / "anscombe.csv") as f:
        rows = csv.reader(f)
        next(rows)
        for name, x, y in rows:
            out.setdefault(name, []).append((float(x), float(y)))
    return {k: np.array(v) for k, v in out.items()}


def t2(v):
    """Two decimals the way Matejka & Fitzmaurice compare them: the first two decimal digits
    (truncated toward zero). All 13 Datasaurus Dozen sets agree on 54.26, 47.83, 16.76, 26.93,
    -0.06 this way; with ordinary rounding some of them would differ by 0.01."""
    q = math.trunc(v * 100 + (1e-7 if v >= 0 else -1e-7)) / 100
    return 0.0 if q == 0 else q


def stats(P):
    """x-bar, y-bar, s_x, s_y, r  (sample SDs, ddof = 1)."""
    x, y = P[:, 0], P[:, 1]
    return np.array([x.mean(), y.mean(), x.std(ddof=1), y.std(ddof=1), np.corrcoef(x, y)[0, 1]])


def fix(P, T):
    """Slide + stretch + tip: the affine map giving P exactly the five numbers T."""
    m = P.mean(0)
    u = (P[:, 0] - m[0]) / P[:, 0].std(ddof=1)
    w = (P[:, 1] - m[1]) / P[:, 1].std(ddof=1)
    rs = float(np.mean(u * w) * N / (N - 1))
    b = np.sqrt((1 - T[4] ** 2) / (1 - rs ** 2))
    a = T[4] - b * rs
    return np.column_stack([T[0] + T[2] * u, T[1] + T[3] * (a * u + b * w)])


def match(A, B):
    """Rows of B reordered so B'[i] is the partner of A[i] (min total squared travel)."""
    C = ((A[:, None, :] - B[None, :, :]) ** 2).sum(-1)
    _, col = linear_sum_assignment(C)
    return B[col]


def star_spots(cx, cy, R, k, n):
    V = []
    for i in range(10):
        ang = np.deg2rad(90 + 36 * i)
        rr = R if i % 2 == 0 else R * k
        V.append((cx + rr * np.cos(ang), cy + rr * np.sin(ang)))
    V = np.array(V + [V[0]])
    seg = np.linalg.norm(np.diff(V, axis=0), axis=1)
    cum = np.concatenate([[0], np.cumsum(seg)])
    t = (np.arange(n) + 0.5) / n * cum[-1]
    pts = []
    for tt in t:
        i = np.searchsorted(cum, tt) - 1
        f = (tt - cum[i]) / seg[i]
        pts.append(V[i] + f * (V[i + 1] - V[i]))
    return np.array(pts), V


def ellipse_xy(s, n=140):
    t = np.linspace(0, 2 * np.pi, n, endpoint=False)
    x = s[0] + s[2] * np.cos(t)
    y = s[1] + s[3] * (s[4] * np.cos(t) + np.sqrt(1 - s[4] ** 2) * np.sin(t))
    return np.column_stack([x, y])


def to_screen(ax, P):
    o = ax.c2p(0, 0)
    ex = ax.c2p(1, 0) - o
    ey = ax.c2p(0, 1) - o
    return o + P[:, 0:1] * ex + P[:, 1:2] * ey


def ell_mob(ax, s, color=YELLOW, sw=4.5):
    return Polygon(*to_screen(ax, ellipse_xy(s)), color=color, stroke_width=sw)


def box_mob(ax, s, color=YELLOW, sw=2.5):
    c = [(s[0] - s[2], s[1] - s[3]), (s[0] + s[2], s[1] - s[3]),
         (s[0] + s[2], s[1] + s[3]), (s[0] - s[2], s[1] + s[3])]
    return Polygon(*to_screen(ax, np.array(c)), color=color, stroke_width=sw)


def lerp(A, B, a):
    return A + (B - A) * a


def window(t0, t1):
    """rate function: nothing before t0, smooth in [t0, t1], done after t1"""
    return lambda t: smooth(min(1.0, max(0.0, (t - t0) / (t1 - t0))))


TXT_GRAY = "#A6ADB7"      # grey for TEXT only: 8.0:1 on BG (BAR asks >= 7:1); GRAY stays for axes/ghosts


def hbar(ax, cx, cy, half, color, sw=4, cap=0.1):
    """Horizontal error bar cx +- half at height cy (the mean +- one SD in x)."""
    a, b = ax.c2p(cx - half, cy), ax.c2p(cx + half, cy)
    return VGroup(Line(a, b), Line(a + UP * cap, a + DOWN * cap),
                  Line(b + UP * cap, b + DOWN * cap)).set_stroke(color, sw)


def vbar(ax, cx, cy, half, color, sw=4, cap=0.1):
    """Vertical error bar cy +- half at cx (the mean +- one SD in y)."""
    a, b = ax.c2p(cx, cy - half), ax.c2p(cx, cy + half)
    return VGroup(Line(a, b), Line(a + LEFT * cap, a + RIGHT * cap),
                  Line(b + LEFT * cap, b + RIGHT * cap)).set_stroke(color, sw)


# ----------------------------------------------------------------------------- layout checks
def _sample(o, n=200):
    """(points, radius) for every drawn part of o: Dots by centre + radius, strokes sampled."""
    out = []
    if isinstance(o, np.ndarray):
        return [(o[:, :2], 0.0)]
    for s in o.family_members_with_points():
        if isinstance(s, Dot):
            out.append((s.get_center()[None, :2], s.width / 2))
        else:
            P = np.array([s.point_from_proportion(t)[:2] for t in np.linspace(0, 1, n)])
            out.append((P, 0.02))                      # ~ half a 4-5 px stroke
    return out


def clearance(m, *others, n=200):
    """Smallest gap (units) between m's bounding box and anything drawn in `others`."""
    lo, hi = m.get_corner(DL)[:2], m.get_corner(UR)[:2]
    best = np.inf
    for o in others:
        for P, rad in _sample(o, n):
            dx = np.maximum(np.maximum(lo[0] - P[:, 0], 0), P[:, 0] - hi[0])
            dy = np.maximum(np.maximum(lo[1] - P[:, 1], 0), P[:, 1] - hi[1])
            best = min(best, float((np.hypot(dx, dy) - rad).min()))
    return best


def require_clear(m, *others, gap=MIN_GAP, what=""):
    c = clearance(m, *others)
    assert c >= gap, f"layout: {what} only {c:.3f} units from its neighbours (need {gap})"
    return c


def require_safe(m, what="", right=6.2):
    assert m.get_right()[0] <= right and m.get_left()[0] >= -SAFE_X, \
        f"layout: {what} spans x [{m.get_left()[0]:.2f}, {m.get_right()[0]:.2f}]"
    assert m.get_top()[1] <= SAFE_TOP and m.get_bottom()[1] >= CONTENT_BOTTOM, \
        f"layout: {what} spans y [{m.get_bottom()[1]:.2f}, {m.get_top()[1]:.2f}]"


# ----------------------------------------------------------------------------- layout
PLOT_C = np.array([-2.85, 0.35, 0])      # centre of the 5.3 x 5.3 data square
SIDE = 5.3
ROW_Y = [2.05, 1.3, 0.55, -0.2, -0.95]
MED_Y = -1.75
# shifted 0.3 right of the round-1 block so "med y" never reads as "x  med y" with the axis name
X_SYM_R, X_EQ, X_TGT_L, X_NOW_L, X_MARK = 1.8, 2.15, 2.5, 4.3, 6.15
COLD_SHIFT = 1.15                         # table sits further right before the "now" column
AN_X = (3, 15)                            # Anscombe axes: zoomed so the slope labels have room
AN_Y = (3.5, 11.5)


def main_axes(xr=(0, 100), yr=(0, 100), ticks_x=(0, 25, 50, 75, 100),
              ticks_y=(0, 25, 50, 75, 100), center=PLOT_C):
    ax = axes(xr, yr, x_length=SIDE, y_length=SIDE, x_ticks=list(ticks_x), y_ticks=list(ticks_y))
    ax.shift(center - (ax.c2p(*xr[:1], yr[0]) + ax.c2p(xr[1], yr[1])) / 2)
    xt = MathTex("x", font_size=38, color=TXT_GRAY).next_to(ax.c2p(xr[1], yr[0]), RIGHT, buff=0.22)
    xt.shift(UP * 0.12)                   # clear of the last tick label (>= 0.15)
    yt = MathTex("y", font_size=38, color=TXT_GRAY).next_to(ax.c2p(xr[0], yr[1]), UP, buff=0.22)
    ax.x_axis.numbers.set_color(TXT_GRAY)
    ax.y_axis.numbers.set_color(TXT_GRAY)
    ax.add(xt, yt)
    ax.x_name, ax.y_name = xt, yt
    return ax


def axes_op(axx, line_op, num_op):
    """Opacity of an Axes' lines/ticks and of its tick numbers and names, set separately (driven
    through the Axes itself, so nothing in the scene is restructured)."""
    for na in (axx.x_axis, axx.y_axis):
        na.set_stroke(opacity=line_op, family=False)
        na.ticks.set_stroke(opacity=line_op)
        if getattr(na, "numbers", None) is not None:
            na.numbers.set_opacity(num_op)
    for nm in (getattr(axx, "x_name", None), getattr(axx, "y_name", None)):
        if nm is not None:
            nm.set_opacity(num_op)


def lane_path(cx, src, dst, rise=0.0):
    """path_func for Transform(src_copy, dst): leave sideways at the source's height, travel in a
    vertical lane at x = cx, and arrive sideways (from a little above) at the target. The offsets
    come from the whole mobjects, because Transform calls path_func glyph by glyph, so every
    glyph moves by the same amount and the number stays legible in flight; a value flown out of
    a table this way never crosses the table's other rows."""
    d1 = np.array([cx - src.get_center()[0], 0.0, 0.0])
    d2 = np.array([cx - dst.get_center()[0], rise, 0.0])

    def pf(s, e, a):
        b = 1 - a
        return b ** 3 * s + 3 * a * b * b * (s + d1) + 3 * a * a * b * (e + d2) + a ** 3 * e
    return pf


def lift_path(src, dst, up=1.0, arrive=(0.0, 0.0)):
    """path_func for ReplacementTransform(src_copy, dst): rise straight up out of the source's
    row first (so the copy never drags across its neighbours in a table), then travel, arriving
    along `arrive`. Constant offsets for every glyph, so the copy stays legible in flight."""
    U = np.array([0.0, up, 0.0])
    V = np.array([arrive[0], arrive[1], 0.0])

    def pf(s, e, a):
        b = 1 - a
        return b ** 3 * s + 3 * a * b * b * (s + U) + 3 * a * a * b * (e + V) + a ** 3 * e
    return pf


def bez_path(src, dst, c1, c2):
    """path_func for ReplacementTransform(src_copy, dst): a cubic Bezier through the absolute
    control points c1, c2 (for the mobject's centre). Every glyph is offset by the same amount,
    so the copy stays legible and can be routed around text it must not cross."""
    d1 = np.array([c1[0], c1[1], 0.0]) - src.get_center()
    d2 = np.array([c2[0], c2[1], 0.0]) - dst.get_center()

    def pf(s, e, a):
        b = 1 - a
        return b ** 3 * s + 3 * a * b * b * (s + d1) + 3 * a * a * b * (e + d2) + a ** 3 * e
    return pf


def item(sym, val, size=36):
    """One readout entry 'sym = val' (symbol in ink, value in yellow)."""
    m = MathTex(sym, "=", val, font_size=size)
    m[2].set_color(YELLOW)
    return m


class Episode(NarratedScene):
    EPISODE = 20
    TITLE = "A Dinosaur Hiding in Your Summary Statistics"
    PRONUNCIATIONS = {"Matejka": "Matayka"}
    SPEED = 0.84

    # ------------------------------------------------------------------ point engine
    def place(self, P, ax=None):
        """Put the 142 dots at data coords P and refresh everything computed from them."""
        ax = ax or self.ax
        self.cur = P
        for d, p in zip(self.dots, to_screen(ax, P)):
            d.move_to(p)
        s = stats(P)
        if self.live:
            n_ok = 0
            for i in range(5):
                v = t2(float(s[i]))
                ok = v == t2(float(self.T[i]))
                n_ok += ok
                self.nows[i].set_value(v)
                self.nows[i].set_color(INK if ok else RED)
                self.marks[i].become(self.eqp[i] if ok else self.neqp[i])
            self.count.number.set_value(n_ok)
            self.count.number.set_color(GREEN if n_ok == 5 else RED)
        if self.med_live:                      # the sixth number, never held by anyone
            v = t2(float(np.median(P[:, 1])))
            ok = v == t2(self.med_t)
            self.med_now.set_value(v)
            self.med_now.set_color(INK if ok else RED)
            self.med_mark.become(self.med_eq if ok else self.med_neq)
        if self.cross_on:                      # the points' own mean +- SD cross (red, or
            col = self.cross_col               # turning yellow as it slides home)
            self.cen_r.move_to(ax.c2p(s[0], s[1])).set_color(col)
            self.harm_r.become(hbar(ax, s[0], s[1], s[2], col)).set_z_index(4)
            self.varm_r.become(vbar(ax, s[0], s[1], s[3], col)).set_z_index(4)
        if self.red_on:                        # the points' own centre / box / ellipse (red)
            self.cen_r.move_to(ax.c2p(s[0], s[1]))
            self.box_r.become(box_mob(ax, s, RED, 2.5).set_stroke(
                opacity=self.box_op)).set_z_index(1)
            self.ell_r.become(ell_mob(ax, s, RED, 4)).set_z_index(1)
        if self.geo_live:                      # yellow geometry recomputed from the points
            self.ell.become(ell_mob(ax, s)).set_z_index(2)
            self.box_y.become(box_mob(ax, s)).set_z_index(2)
            self.cen_y.move_to(ax.c2p(s[0], s[1]))
            self.tR.move_to(ax.c2p(s[0] + s[2], s[1] + s[4] * s[3]))
            self.tL.move_to(ax.c2p(s[0] - s[2], s[1] - s[4] * s[3]))

    def flow(self, f, color_from=None, color_to=None, op_from=None, op_to=None):
        def upd(m, a):
            self.place(f(a))
            if color_from is not None:
                c = interpolate_color(ManimColor(color_from), ManimColor(color_to), a)
                for d in self.dots:
                    d.set_fill(c)
            if op_from is not None:
                for d in self.dots:
                    d.set_opacity(op_from + (op_to - op_from) * a)
        return UpdateFromAlphaFunc(self.dots, upd)

    def go(self, f, run_time, rate_func=smooth, *extra, **kw):
        # rate_func goes on the point flow only, so the extras keep their own (window(...))
        fl = self.flow(f, **kw)
        fl.rate_func = rate_func
        self.play(fl, *extra, run_time=run_time)
        self.place(f(1.0))

    def path_fixed(self, A, B):
        """A -> B while the five numbers follow the straight line between their values."""
        sA, sB = stats(A), stats(B)
        return lambda a: B if a >= 1 else (A if a <= 0 else fix(lerp(A, B, a), lerp(sA, sB, a)))

    def path_nudge(self, A, B, seed=11, window=0.42, wobble=2.2):
        """A -> B the way the search looks: points set off one by one in random order, each on
        a slightly wandering path, while the five numbers are held (as in every intermediate
        frame of the authors' own animations). Endpoints are exactly A and B."""
        rng = np.random.default_rng(seed)
        start = rng.uniform(0, 1 - window, len(A))
        phase = rng.uniform(0, 2 * np.pi, len(A))
        d = B - A
        perp = np.column_stack([-d[:, 1], d[:, 0]])
        perp /= np.maximum(np.linalg.norm(perp, axis=1, keepdims=True), 1e-9)
        sA, sB = stats(A), stats(B)

        def f(a):
            if a <= 0:
                return A
            if a >= 1:
                return B
            ai = np.clip((a - start) / window, 0, 1)
            ai = ai * ai * (3 - 2 * ai)
            wig = wobble * np.sin(np.pi * ai) * np.sin(3 * np.pi * ai + phase)
            P = A + d * ai[:, None] + perp * wig[:, None]
            return fix(P, lerp(sA, sB, a))
        return f

    # ------------------------------------------------------------------ construct
    def construct(self):
        D = load_dozen()
        dino = D["dino"]
        T = self.T = stats(dino)
        TR = np.array([t2(v) for v in T])
        rng = np.random.default_rng(7)
        z = rng.standard_normal((4000, 2))
        z = z[np.linalg.norm(z, axis=1) < 1.7][:N]
        L = np.linalg.cholesky(np.cov(dino.T, ddof=1))
        guess = match(dino, T[:2] + z @ L.T)                 # guess[i] travels to dino[i]
        slope_d = T[4] * T[3] / T[2]                         # the five numbers' best-fit slope
        strip = np.column_stack([T[0] + (dino[:, 0] - T[0]) * 0.12, dino[:, 1]])
        spots, star_v = star_spots(50, 50, 40, 0.45, N)
        star0 = match(dino, spots)                           # version one
        s_star0 = stats(star0)
        m0, s0 = star0.mean(0), star0.std(0, ddof=1)
        slid = star0 + (T[:2] - m0)
        k = T[2:4] / s0
        stretched = T[:2] + (slid - T[:2]) * k
        u = (stretched[:, 0] - T[0]) / T[2]
        w = (stretched[:, 1] - T[1]) / T[3]
        r_s = float(np.corrcoef(u, w)[0, 1])

        def tipped(a):
            rr = r_s + a * (T[4] - r_s)
            b = np.sqrt((1 - rr ** 2) / (1 - r_s ** 2))
            return np.column_stack([stretched[:, 0], T[1] + T[3] * ((rr - b * r_s) * u + b * w)])
        fixed_star = tipped(1.0)
        self.med_t = float(np.median(dino[:, 1]))
        med_n = float(np.median(fixed_star[:, 1]))

        self.live = self.red_on = self.geo_live = self.cross_on = self.med_live = False
        self.box_op = 1.0                                    # red box opacity (hidden in the hold)
        self.cross_col = RED

        # ---------------------------------------------------------------- objects
        ax = self.ax = main_axes()
        n_lbl = MathTex(r"n = 142", font_size=44, color=TXT_GRAY).move_to(ax.c2p(50, 50))
        self.dots = VGroup(*[Dot(radius=0.055, color=GRAY) for _ in range(N)])
        self.place(guess)

        syms = [MathTex(t, font_size=42) for t in (r"\bar{x}", r"\bar{y}", r"s_x", r"s_y", r"r")]
        eqs = [MathTex("=", font_size=42) for _ in range(5)]
        tgts = [MathTex(f"{v:.2f}", font_size=42, color=YELLOW) for v in TR]
        for i in range(5):
            syms[i].move_to([X_SYM_R, ROW_Y[i], 0], aligned_edge=RIGHT)
            eqs[i].move_to([X_EQ, ROW_Y[i], 0])
            tgts[i].move_to([X_TGT_L, ROW_Y[i], 0], aligned_edge=LEFT)
        rows = [VGroup(syms[i], eqs[i], tgts[i]) for i in range(5)]
        table = VGroup(*rows).shift(RIGHT * COLD_SHIFT)
        table_cold = table.copy()                            # for the landing

        def line_xy(a, x0=12, x1=96):
            return ax.c2p(x0, T[1] + slope_d * (x0 - T[0])), ax.c2p(x1, T[1] + slope_d * (x1 - T[0]))

        cite_cairo = citation("Datasaurus: Alberto Cairo, 2016 · The Functional Art", color=TXT_GRAY)
        cite_w = citation("Weissgerber et al., 2015 · PLOS Biology", color=TXT_GRAY)
        guess_lbl = label("your guess", color=TXT_GRAY).next_to(ax.c2p(3, 100), DR, buff=0.0)
        guess_lbl.shift(DOWN * 0.05)
        guess_line = DashedLine(*line_xy(ax), color=GRAY, stroke_width=3, dash_length=0.14)
        line_lbl = label("your line", color=TXT_GRAY).next_to(guess_line.get_end(), RIGHT, buff=0.2)
        require_clear(guess_lbl, self.dots, what="'your guess'")
        require_clear(line_lbl, self.dots, table, what="'your line'")

        # ================================================================ COLD OPEN
        # the commit is about the one thing the five numbers really do fix: the line
        qmark = MathTex("?", font_size=96, color=GRAY).move_to(ax.c2p(50, 50))
        qmark.set_opacity(0.55)
        self.add(ax, n_lbl, *[VGroup(syms[i], eqs[i]) for i in range(5)])
        # the viewer pictures the cloud (likely wrong) and commits to its line (likely right)
        with self.narrate("A hundred and forty-two points with two averages, two standard "
                          "deviations, and a correlation of minus point oh six. Picture the cloud. "
                          "Which way does its best-fit line tilt? [pause 1.5]") as beat:
            self.play(flag(n_lbl), run_time=0.9)
            beat.wait_until("points", offset=-0.05)
            self.play(LaggedStart(*[flag(s) for s in syms], lag_ratio=0.12), run_time=0.7)
            beat.wait_until("averages", offset=-0.35)
            self.play(Write(tgts[0]), Write(tgts[1]), run_time=0.9)
            beat.wait_until("standard", offset=-0.3)
            self.play(Write(tgts[2]), Write(tgts[3]), run_time=0.9)
            beat.wait_until("correlation", offset=-0.1)
            self.play(Write(tgts[4]), run_time=0.8)
            beat.wait_until("minus", offset=-0.1)
            self.play(flag(tgts[4]), run_time=0.9)
            beat.wait_until("Picture", offset=-0.05)
            self.play(FadeOut(n_lbl, scale=0.9), run_time=1.0)
            beat.wait_until("tilt", offset=0.0)
            self.play(FadeIn(qmark, scale=0.8), run_time=0.8)

        with self.narrate("You probably pictured a shapeless oval, with a nearly flat line. Here "
                          "are the real points. [pause 1.1] A dinosaur, drawn by Alberto Cairo, "
                          "with these same five numbers.", gap=0.65) as beat:
            self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in
                                    sorted(self.dots, key=lambda d: np.linalg.norm(
                                        d.get_center() - ax.c2p(*T[:2])))], lag_ratio=0.012),
                      FadeOut(qmark, scale=1.2, rate_func=lambda t: smooth(min(1.0, 3 * t))),
                      FadeIn(guess_lbl), run_time=beat.until("nearly", offset=-0.1))
            self.remove(*self.dots)
            self.add(self.dots)
            self.play(Create(guess_line), FadeIn(line_lbl, shift=0.1 * LEFT),
                      run_time=beat.until("Here", offset=-0.1))
            # the reveal: 1.8 s from "real", then a 0.4 s look before it is named
            beat.wait_until("real", offset=-0.1)
            self.go(lambda a: lerp(guess, dino, a), 1.8, smooth,
                    FadeOut(guess_lbl, rate_func=window(0.0, 0.25)),
                    FadeOut(guess_line, rate_func=window(0.0, 0.25)),
                    FadeOut(line_lbl, rate_func=window(0.0, 0.25)),
                    color_from=GRAY, color_to=BLUE)
            beat.wait_until("drawn", offset=-0.2)
            self.play(FadeIn(cite_cairo), run_time=0.6)
            beat.wait_until("these same", offset=-0.1)
            self.play(LaggedStart(*[flag(t) for t in tgts], lag_ratio=0.12), run_time=1.2)

        # ================================================================ STAKES
        bar_hw = 9
        bar_rect = Polygon(ax.c2p(T[0] - bar_hw, 0), ax.c2p(T[0] + bar_hw, 0),
                           ax.c2p(T[0] + bar_hw, T[1]), ax.c2p(T[0] - bar_hw, T[1]),
                           color=YELLOW, stroke_width=3, fill_color=YELLOW, fill_opacity=0.22)
        err_bar = vbar(ax, T[0], T[1], T[3], YELLOW, sw=4, cap=0.16).set_z_index(2)
        def pct_label(num, words):
            return VGroup(MathTex(num, font_size=36, color=TXT_GRAY),
                          Text(words, font=SERIF, font_size=26, color=TXT_GRAY)).arrange(
                DOWN, buff=0.12, aligned_edge=LEFT)
        pct86 = pct_label(r"86\%", "used bars").next_to(bar_rect, LEFT, buff=0.3)
        pct13 = pct_label(r"13\%", "showed points").next_to(bar_rect, RIGHT, buff=0.3)
        pct13.set_y(ax.c2p(0, 62)[1])
        require_safe(pct86, "'86% used bars'")
        x_ctx = VGroup(ax.x_axis.numbers, ax.x_axis.ticks, ax.x_name)
        strip_dots = VGroup(*[Dot(p, radius=0.055) for p in to_screen(ax, strip)])
        require_clear(pct86, strip_dots, bar_rect, err_bar, what="'86 %'")
        require_clear(pct13, strip_dots, bar_rect, err_bar, what="'13 %'")
        with self.narrate("In a review of seven hundred and three physiology papers, eighty-six "
                          "percent used bar graphs: an average and an error bar. Only thirteen "
                          "percent showed the points.") as beat:
            self.play(Succession(FadeOut(cite_cairo, run_time=0.3), FadeIn(cite_w, run_time=0.3)),
                      run_time=0.6)
            beat.wait_until("papers", offset=-0.2)
            # the strip keeps every y but squeezes x, so the x ticks stop meaning anything
            self.go(lambda a: lerp(dino, strip, a), 1.2, smooth,
                    UpdateFromAlphaFunc(ax, lambda m, a: x_ctx.set_opacity(1 - 0.75 * a)))
            beat.wait_until("bar graphs", offset=-0.1)
            self.play(GrowFromEdge(bar_rect, DOWN), self.dots.animate.set_opacity(0.25),
                      Write(pct86), run_time=0.8)
            beat.wait_until("average", offset=-0.1)
            self.play(flag(rows[1]), run_time=0.8)
            beat.wait_until("error", offset=-0.15)
            self.play(Create(err_bar), flag(rows[3]), run_time=0.8)
            beat.wait_until("Only", offset=-0.05)
            self.play(bar_rect.animate.set_fill(opacity=0.05).set_stroke(opacity=0.3),
                      err_bar.animate.set_stroke(opacity=0.3), pct86.animate.set_opacity(0.4),
                      self.dots.animate.set_opacity(1.0), Write(pct13),
                      run_time=beat.until("points", offset=0.1))

        # ================================================================ GOAL
        star_line = DashedVMobject(Polygon(*to_screen(ax, star_v[:-1]), color=GRAY,
                                           stroke_width=2.5), num_dashes=70, dashed_ratio=0.55)
        hdr_t = label("dinosaur", color=TXT_GRAY)
        hdr_n = label("now", color=TXT_GRAY)
        self.nows = [DecimalNumber(float(TR[i]), num_decimal_places=2, font_size=42, color=INK)
                     for i in range(5)]
        self.eqp = [MathTex("=", font_size=44, color=GREEN) for _ in range(5)]
        self.neqp = [MathTex(r"\neq", font_size=44, color=RED) for _ in range(5)]
        for i in range(5):
            self.nows[i].move_to([X_NOW_L, ROW_Y[i], 0], aligned_edge=LEFT)
            self.eqp[i].move_to([X_MARK, ROW_Y[i], 0])
            self.neqp[i].move_to([X_MARK, ROW_Y[i], 0])
        self.marks = [self.eqp[i].copy() for i in range(5)]
        hdr_t.move_to([X_TGT_L + 0.65, 2.8, 0])
        hdr_n.move_to([X_NOW_L + 0.65, 2.8, 0]).align_to(hdr_t, DOWN)
        cnt = ValueTracker(5)
        self.count = live_number(cnt, 0, size=42, color=GREEN, prefix=r"\text{matching:}",
                                 suffix=r"/\,5")
        self.count.number.clear_updaters()
        self.count.move_to([3.85, -1.85, 0])
        self.count[0].set_color(TXT_GRAY)
        self.count[2].set_color(TXT_GRAY)
        note = Text("first two decimals, as published", font=SERIF, font_size=25, color=TXT_GRAY)
        note.next_to(self.count, DOWN, buff=0.3).set_x(3.7)
        require_safe(note, "decimals note")

        with self.narrate("So how much can five numbers hide? Let's hide a star in them, and "
                          "demand that all five still match the dinosaur's to two "
                          "decimals.", gap=0.2) as beat:
            # the labels beside the strip are gone before the points spread out over them
            self.go(lambda a: lerp(strip, dino, a), 1.3, smooth,
                    FadeOut(bar_rect), FadeOut(err_bar), FadeOut(cite_w),
                    FadeOut(pct86, rate_func=window(0.0, 0.25)),
                    FadeOut(pct13, rate_func=window(0.0, 0.25)),
                    UpdateFromAlphaFunc(ax, lambda m, a: x_ctx.set_opacity(0.25 + 0.75 * a)))
            beat.wait_until("Let's", offset=-0.05)
            self.play(self.dots.animate.set_opacity(0.3), run_time=0.5)
            beat.wait_until("star", offset=-0.1)
            self.play(Create(star_line), run_time=1.1)
            beat.wait_until("demand", offset=-0.1)
            self.play(table.animate.shift(LEFT * COLD_SHIFT), run_time=0.6)
            beat.wait_until("all five", offset=-0.1)
            self.play(LaggedStart(*[FadeIn(self.nows[i], shift=0.3 * RIGHT) for i in range(5)],
                                  lag_ratio=0.15),
                      FadeIn(hdr_t, shift=0.1 * DOWN), FadeIn(hdr_n, shift=0.1 * DOWN),
                      run_time=1.0)
            beat.wait_until("match", offset=-0.05)
            self.play(LaggedStart(*[FadeIn(m, scale=0.6) for m in self.marks], lag_ratio=0.1),
                      FadeIn(self.count, shift=0.1 * UP), run_time=1.0)
            beat.wait_until("two decimals", offset=-0.1)
            self.play(FadeIn(note), run_time=0.5)
            self.live = True

        # ================================================================ VERSION ONE
        with self.narrate("Version one slides every point onto its own spot on a star.") as beat:
            self.play(self.dots.animate.set_opacity(1.0), run_time=beat.until("slides", offset=-0.1))
            self.go(lambda a: lerp(dino, star0, a), 3.0)

        cen_y = self.cen_y = Dot(ax.c2p(T[0], T[1]), radius=0.09, color=YELLOW).set_z_index(3)
        harm_y = hbar(ax, T[0], T[1], T[2], YELLOW).set_z_index(2)
        varm_y = vbar(ax, T[0], T[1], T[3], YELLOW).set_z_index(2)
        self.cen_r = Dot(ax.c2p(T[0], T[1]), radius=0.09, color=RED).set_z_index(5)
        harm_r = hbar(ax, *s_star0[:3], RED).set_z_index(4)
        varm_r = vbar(ax, s_star0[0], s_star0[1], s_star0[3], RED).set_z_index(4)
        with self.narrate("We got the star, and lost all five numbers. [pause 0.2] The center moved, the x "
                          "spread grew, and the y spread shrank by almost a quarter.",
                          gap=0.65) as beat:
            beat.wait_until("lost", offset=-0.1)
            self.play(Indicate(self.count, color=RED, scale_factor=1.1), run_time=0.9)
            beat.wait_until("center", offset=-0.25)
            self.play(FadeIn(cen_y, scale=0.5), FadeIn(self.cen_r, scale=0.5), run_time=0.35)
            self.play(self.cen_r.animate.move_to(ax.c2p(s_star0[0], s_star0[1])),
                      Indicate(VGroup(self.nows[0], self.nows[1]), color=RED, scale_factor=1.1),
                      run_time=0.8)
            beat.wait_until("x spread", offset=-0.2)
            self.play(GrowFromCenter(harm_y), run_time=0.45)
            self.play(TransformFromCopy(harm_y, harm_r),
                      Indicate(self.nows[2], color=RED, scale_factor=1.1), run_time=0.9)
            beat.wait_until("y spread", offset=-0.2)
            self.play(GrowFromCenter(varm_y), run_time=0.45)
            self.play(TransformFromCopy(varm_y, varm_r),
                      Indicate(self.nows[3], color=RED, scale_factor=1.1), run_time=0.9)
        self.harm_r, self.varm_r = harm_r, varm_r
        self.cross_on = True

        # ================================================================ INSIGHT
        seg_x = Line(ax.c2p(T[0], T[1]), ax.c2p(T[0] + T[2], T[1]), color=YELLOW, stroke_width=9)
        seg_y = Line(ax.c2p(T[0], T[1]), ax.c2p(T[0], T[1] + T[3]), color=YELLOW, stroke_width=9)
        sides = [Line(ax.c2p(T[0] + sx * T[2], T[1] - T[3]), ax.c2p(T[0] + sx * T[2], T[1] + T[3]))
                 for sx in (-1, 1)] + \
                [Line(ax.c2p(T[0] - T[2], T[1] + sy * T[3]), ax.c2p(T[0] + T[2], T[1] + sy * T[3]))
                 for sy in (-1, 1)]
        for sd in sides:
            sd.set_stroke(YELLOW, 2.5)
        box_y = self.box_y = box_mob(ax, T).set_z_index(2)
        self.ell = ell_mob(ax, T).set_z_index(2)
        rt = ValueTracker(float(T[4]))
        tR = self.tR = Dot(ax.c2p(T[0] + T[2], T[1] + T[4] * T[3]), radius=0.075,
                           color=YELLOW).set_z_index(3)
        tL = self.tL = Dot(ax.c2p(T[0] - T[2], T[1] - T[4] * T[3]), radius=0.075,
                           color=YELLOW).set_z_index(3)

        def cross_to_yellow(m, a):
            self.cross_col = interpolate_color(ManimColor(RED), ManimColor(YELLOW), a)
        with self.narrate("So what exactly do five numbers pin down?") as beat:
            # back to the dinosaur first: the question is about its five numbers. The red cross
            # (drifted) turns yellow as it slides home, so it never reads red over a 5/5 readout
            ticker = VMobject()
            self.go(lambda a: lerp(star0, dino, a), beat.until("five", offset=-0.1), smooth,
                    FadeOut(star_line), FadeOut(note),
                    UpdateFromAlphaFunc(ticker, cross_to_yellow))
            self.cross_on = False
            self.remove(ticker, self.cen_r, self.harm_r, self.varm_r)   # cross = the yellow one
            self.play(LaggedStart(*[flag(t) for t in tgts], lag_ratio=0.1), run_time=1.0)

        # the point is labelled with the symbols of the two averages: (x-bar, y-bar). The
        # symbols are the left-most glyphs of their rows, so their copies leave the table
        # without crossing any other glyph (a value would have to cross its own "x-bar =")
        xy_lbl = MathTex("(", r"\bar{x}", ",", r"\bar{y}", ")", font_size=38,
                         color=YELLOW).set_z_index(7)
        xy_lbl.next_to(cen_y, UR, buff=0.24)                 # >= 0.2 from the arms and the right cap
        xy_patch = BackgroundRectangle(xy_lbl, color=BG, fill_opacity=1.0,
                                       buff=0.06).set_z_index(6)
        require_clear(xy_lbl, harm_y, varm_y, cen_y, what="(x-bar, y-bar) label")
        require_safe(xy_lbl, "(x-bar, y-bar) label")
        with self.narrate("The two averages mark a single point: the cloud's balance point.",
                          gap=0.15) as beat:
            self.play(self.dots.animate.set_opacity(0.28), run_time=0.45)
            beat.wait_until("averages", offset=-0.1)
            self.play(flag(VGroup(tgts[0], tgts[1])), run_time=0.8)
            beat.wait_until("single", offset=-0.1)
            # part -> part copies (same structure, so each glyph maps onto itself); the x-bar
            # copy leaves first and the two paths never meet
            p_xb = MathTex(r"\bar{x}", font_size=42).move_to(syms[0])[0].set_z_index(7)
            p_yb = MathTex(r"\bar{y}", font_size=42).move_to(syms[1])[0].set_z_index(7)
            self.play(FadeIn(xy_patch, rate_func=window(0.0, 0.3)),
                      LaggedStart(ReplacementTransform(p_xb, xy_lbl[1]),
                                  ReplacementTransform(p_yb, xy_lbl[3]), lag_ratio=0.35),
                      FadeIn(VGroup(xy_lbl[0], xy_lbl[2], xy_lbl[4]),
                             rate_func=window(0.6, 1.0)), run_time=1.1)
            beat.wait_until("balance", offset=-0.1)
            self.play(flag(cen_y), run_time=0.8)

        # each SD symbol travels to the half-arm it measures (s_x under the right half-arm,
        # s_y beside the upper one, each on an opaque patch over the dimmed points), the arm
        # lights up, and the walls grow out of the arm tips on "box". The symbols are the
        # left-most glyphs of their rows, so the copies leave the table without crossing any
        # glyph, and they travel one after the other (s_x is home before s_y sets off)
        c_sx = MathTex(r"s_x", font_size=40, color=YELLOW).set_z_index(7)
        c_sy = MathTex(r"s_y", font_size=40, color=YELLOW).set_z_index(7)
        # under the right half-arm, clear of the vertical arm and of the right cap (>= 0.15)
        c_sx.move_to(ax.c2p(T[0] + T[2] / 2, T[1]) + DOWN * (0.3 + c_sx.height / 2))
        c_sy.move_to(ax.c2p(T[0], T[1] + T[3] / 2) + RIGHT * (0.24 + c_sy.width / 2))
        pt_sx = BackgroundRectangle(c_sx, color=BG, fill_opacity=1.0, buff=0.06).set_z_index(6)
        pt_sy = BackgroundRectangle(c_sy, color=BG, fill_opacity=1.0, buff=0.06).set_z_index(6)
        require_clear(c_sx, harm_y, varm_y, cen_y, seg_x, seg_y, what="s_x by its arm")
        require_clear(c_sy, harm_y, varm_y, cen_y, seg_x, seg_y, what="s_y by its arm")
        require_clear(c_sx, c_sy, what="s_x vs s_y arm labels")
        with self.narrate("The two standard deviations reach one deviation out on each side, "
                          "and draw a box.", gap=0.2) as beat:
            beat.wait_until("standard", offset=-0.15)
            self.play(flag(VGroup(tgts[2], tgts[3])),
                      FadeOut(VGroup(xy_lbl, xy_patch), rate_func=window(0.0, 0.6)),
                      run_time=0.8)
            beat.wait_until("reach", offset=-0.15)
            q_sx = MathTex(r"s_x", font_size=42).move_to(syms[2]).set_z_index(7)
            q_sy = MathTex(r"s_y", font_size=42).move_to(syms[3]).set_z_index(7)
            self.play(Succession(
                AnimationGroup(ReplacementTransform(q_sx, c_sx, path_arc=-0.5),   # dips under the arm cap
                               FadeIn(pt_sx, rate_func=window(0.5, 1.0))),
                AnimationGroup(ReplacementTransform(q_sy, c_sy), FadeIn(pt_sy, rate_func=window(0.5, 1.0)))),
                run_time=min(1.2, beat.until("out", offset=-0.25)))
            beat.wait_until("out", offset=-0.2)
            self.play(Create(seg_x), Create(seg_y), run_time=0.6)
            self.play(FadeOut(VGroup(c_sx, pt_sx, c_sy, pt_sy), scale=0.8), run_time=0.4)
            beat.wait_until("draw", offset=-0.1)
            self.play(*[GrowFromCenter(sd) for sd in sides], run_time=0.7)
            self.remove(*sides)
            self.add(box_y)
            self.play(FadeOut(VGroup(seg_x, seg_y, harm_y, varm_y)), run_time=0.5)

        # The correlation: which of the many ellipses that touch all four walls. Correlation r
        # means one s_x to the right goes with r s_y up on average: that is the best-fit line. It
        # runs through the middle of every vertical slice of the ellipse, and at the wall the
        # slice shrinks to the touch point, so the touch point sits r s_y above the centre. Shown,
        # not asserted: a dashed line through the centre and both touch dots, five vertical
        # slices with their midpoints on it, and the slices sliding to the wall where each one
        # collapses onto the touch dot. The sweep is a "what if" ellipse, so the dinosaur steps
        # aside while it runs and the data's own r row is dimmed; a live label shows the r drawn.
        r_row = VGroup(syms[4], eqs[4], tgts[4], self.nows[4], self.marks[4])
        wall_x = T[0] + T[2]
        run9 = Line(ax.c2p(T[0], T[1]), ax.c2p(wall_x, T[1]), color=YELLOW,
                    stroke_width=3.5).set_z_index(2)
        run9_lbl = MathTex("s_x", font_size=36, color=YELLOW).set_z_index(5)
        # above the run's left part: clear of the ellipse for every r in the sweep (-0.06..0.8);
        # it leaves when the best-fit line (which would cross it) is drawn
        run9_lbl.next_to(run9.point_from_proportion(0.3), UP, buff=0.25)
        ghosts = VGroup(*[ell_mob(ax, (T[0], T[1], T[2], T[3], rg), GRAY, 3)
                          for rg in (0.5, -0.5)]).set_stroke(opacity=0.4)

        def rise_line(r):
            r = r if abs(r) > 2e-3 else 2e-3                 # never a zero-length line
            return Line(ax.c2p(wall_x, T[1]), ax.c2p(wall_x, T[1] + r * T[3]), color=YELLOW,
                        stroke_width=8).set_z_index(3)
        rise9 = rise_line(float(T[4]))
        BFL_EXT = 1.05                                       # just past both touch dots

        def bfl_line(r):
            """best-fit line y - y_bar = r s_y/s_x (x - x_bar), through both touch dots"""
            return DashedLine(ax.c2p(T[0] - BFL_EXT * T[2], T[1] - BFL_EXT * r * T[3]),
                              ax.c2p(T[0] + BFL_EXT * T[2], T[1] + BFL_EXT * r * T[3]),
                              color=YELLOW, stroke_width=3, dash_length=0.12,
                              dashed_ratio=0.6).set_z_index(2)
        bfl = bfl_line(0.8)
        KS = (-0.8, -0.4, 0.0, 0.4, 0.8)                     # slice positions, in units of s_x
        qv = ValueTracker(0.0)                               # 0: spread out, 1: all at the wall

        def chord_pts(k, r):
            """vertical slice of the 1-SD ellipse at x = x_bar + k s_x: ends and midpoint"""
            h = T[3] * np.sqrt(1 - r * r) * np.sqrt(max(0.0, 1 - k * k))
            c = T[1] + r * k * T[3]
            x = T[0] + k * T[2]
            return ax.c2p(x, c - h), ax.c2p(x, c + h), ax.c2p(x, c)
        chords = VGroup(*[Line(*chord_pts(k, 0.8)[:2]) for k in KS]).set_stroke(
            YELLOW, 2.5, opacity=0.6).set_z_index(2)
        mids = VGroup(*[Dot(chord_pts(k, 0.8)[2], radius=0.065, color=YELLOW).set_z_index(4)
                        for k in KS])

        def upd_chords(m):
            q = qv.get_value()
            for ln, d, k in zip(chords, mids, KS):
                lo, hi, mid = chord_pts(min(k + (1 - k) * q, 0.9995), 0.8)
                ln.put_start_and_end_on(lo, hi)
                d.move_to(mid)
        rs_lbl = MathTex("r", r"\,s_y", font_size=36, color=YELLOW).set_z_index(5)
        r_live = VGroup(MathTex(r"r =", font_size=36, color=YELLOW),
                        DecimalNumber(float(T[4]), num_decimal_places=2, font_size=36,
                                      color=YELLOW)).arrange(RIGHT, buff=0.12).set_z_index(5)

        rs_w, rs_h = rs_lbl.width, rs_lbl.height

        def rs_left(r):                                      # left-centre point of the r s_y label
            return ax.c2p(wall_x, T[1] + r * T[3] / 2) + RIGHT * 0.25

        def place_rs(r):
            rs_lbl.move_to(rs_left(r), aligned_edge=LEFT)

        def place_live(r):
            r_live[1].set_value(r)
            r_live.move_to(rs_left(r) + DOWN * (rs_h / 2 + 0.15 + r_live.height / 2),
                           aligned_edge=LEFT)

        def place_labels(r):
            place_rs(r)
            place_live(r)

        # once "r s_y" names the rise, the live r label steps up to the box's top-right corner
        # (it names the ellipse being drawn, not the rise), so the rise never has two labels
        corner_l = ax.c2p(wall_x, T[1] + T[3]) + RIGHT * 0.25

        def place_live_corner(r):
            r_live[1].set_value(r)
            r_live.move_to(corner_l, aligned_edge=LEFT)
        for r_chk in (float(T[4]), 0.0, 0.4, 0.8):           # settled states of the sweep
            place_labels(r_chk)
            s_chk = (T[0], T[1], T[2], T[3], r_chk)
            dot_chk = Dot(ax.c2p(wall_x, T[1] + r_chk * T[3]), radius=0.075)
            dotL_chk = Dot(ax.c2p(T[0] - T[2], T[1] - r_chk * T[3]), radius=0.075)
            for m_chk in (rs_lbl, r_live):
                require_clear(m_chk, ell_mob(ax, s_chk), box_mob(ax, T), dot_chk, bfl_line(r_chk),
                              VGroup(*syms, *eqs, *tgts, *self.nows),
                              what=f"B9 label at r={r_chk:.2f}")
            if r_chk != 0.4:
                require_clear(run9_lbl, ell_mob(ax, s_chk), box_mob(ax, T), dot_chk, dotL_chk,
                              cen_y, run9, rise_line(r_chk),
                              what=f"B9 s_x label at r={r_chk:.2f}")
        place_labels(0.8)
        require_clear(VGroup(rs_lbl, r_live), chords, mids, what="B9 labels vs slices")
        for r_chk in (0.8, 0.4, 0.0, float(T[4])):           # the corner label, sweeping back
            place_live_corner(r_chk)
            place_rs(r_chk)
            require_clear(r_live, ell_mob(ax, (T[0], T[1], T[2], T[3], r_chk)), box_mob(ax, T),
                          bfl_line(r_chk), rs_lbl, rise_line(r_chk),
                          Dot(ax.c2p(wall_x, T[1] + r_chk * T[3]), radius=0.075),
                          VGroup(*syms, *eqs, *tgts, *self.nows),
                          what=f"B9 corner r label at r={r_chk:.2f}")
            require_safe(r_live, f"B9 corner r label at r={r_chk:.2f}")
        place_labels(float(T[4]))

        with self.narrate("Many ellipses touch all four walls. [pause 0.2] The correlation picks "
                          "one. Correlation r means one standard deviation to the right, on "
                          "average r standard deviations up. That's the best-fit line, through "
                          "the middle of every vertical slice. At the wall, the slice is just the "
                          "touch point, r times ess why above the center. For minus point oh six, "
                          "that's just below the middle.") as beat:
            beat.wait_until("Many", offset=-0.1)
            self.play(LaggedStart(*[Create(g) for g in ghosts], lag_ratio=0.35), run_time=0.9)
            beat.wait_until("walls", offset=-0.2)
            self.play(Indicate(box_y, color=YELLOW, scale_factor=1.04), run_time=0.8)
            beat.wait_until("correlation", offset=-0.1)
            self.play(flag(tgts[4]), run_time=0.6)
            beat.wait_until("picks", offset=-0.15)
            # the ellipse is drawn from its right touch point round to the left one: each touch
            # dot appears as the stroke reaches the wall (no glyph-to-dot morph across the table)
            self.play(FadeOut(ghosts), Create(self.ell),
                      FadeIn(tR, scale=0.4, rate_func=window(0.0, 0.2)),
                      FadeIn(tL, scale=0.4, rate_func=window(0.45, 0.65)), run_time=1.0)

            def sweep(m):
                s = (T[0], T[1], T[2], T[3], rt.get_value())
                m.become(ell_mob(ax, s).set_z_index(2))
            self.ell.add_updater(sweep)
            tR.add_updater(lambda m: m.move_to(ax.c2p(wall_x, T[1] + rt.get_value() * T[3])))
            tL.add_updater(lambda m: m.move_to(ax.c2p(T[0] - T[2], T[1] - rt.get_value() * T[3])))
            rise9.add_updater(lambda m: m.become(rise_line(rt.get_value())))
            r_live.add_updater(lambda m: place_live(rt.get_value()))
            beat.wait_until("Correlation", occurrence=2, offset=-0.15)
            # start from r = 0: the touch point sits level with the centre
            self.play(self.dots.animate.set_opacity(0), r_row.animate.set_opacity(0.35),
                      self.count.animate.set_opacity(0.35), FadeIn(r_live), run_time=0.5)
            # (separate play: the live label's digits change while r crosses zero)
            self.play(rt.animate.set_value(0.0), run_time=0.6)
            beat.wait_until("one standard", offset=-0.1)
            self.play(Create(run9), Write(run9_lbl), run_time=beat.until("right", offset=0.25))
            self.add(rise9)
            beat.wait_until("on average", offset=0.1)
            self.play(rt.animate.set_value(0.8), run_time=beat.until("up", offset=0.35),
                      rate_func=smooth)
            # the best-fit line: from the centre through both touch dots
            beat.wait_until("best-fit", offset=-0.2)
            self.play(GrowFromCenter(bfl), FadeOut(run9_lbl), run_time=0.9)
            beat.wait_until("middle", offset=-0.3)
            self.play(LaggedStart(*[Create(c) for c in chords], lag_ratio=0.15), run_time=0.9)
            beat.wait_until("vertical", offset=-0.1)
            self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in mids], lag_ratio=0.15),
                      run_time=0.8)
            # at the wall a slice is a single point: every slice slides there and collapses
            beat.wait_until("the wall", offset=-0.1)
            self.play(qv.animate.set_value(1.0), UpdateFromFunc(chords, upd_chords),
                      run_time=beat.until("touch point", offset=-0.15), rate_func=smooth)
            # the r label steps up to the corner first, so "r s_y" is written into free space
            r_live.clear_updaters()
            self.play(FadeOut(chords), FadeOut(mids), flag(tR),
                      r_live.animate.move_to(corner_l, aligned_edge=LEFT), run_time=0.7)
            r_live.add_updater(lambda m: place_live_corner(rt.get_value()))
            beat.wait_until("times", offset=-0.3)
            place_rs(rt.get_value())
            self.play(Write(rs_lbl), run_time=0.8)
            rs_lbl.add_updater(lambda m: place_rs(rt.get_value()))
            bfl.add_updater(lambda m: m.become(bfl_line(rt.get_value())))
            beat.wait_until("minus", offset=-0.2)
            self.play(rt.animate.set_value(float(T[4])), run_time=1.2, rate_func=smooth)
            for m in (self.ell, tR, tL, rise9, r_live, rs_lbl, bfl):
                m.clear_updaters()
            place_rs(float(T[4]))
            place_live_corner(float(T[4]))
            self.play(FadeOut(r_live), r_row.animate.set_opacity(1.0),
                      self.count.animate.set_opacity(1.0), run_time=0.45)
            # each value flagged on its own (a group Indicate would push 0.06 into its "=")
            self.play(LaggedStart(flag(tgts[4]), flag(self.nows[4]), lag_ratio=0.25),
                      run_time=0.75)
            beat.wait_until("middle", occurrence=2, offset=-0.3)
            self.play(flag(tR), run_time=0.8)

        with self.narrate("That ellipse is everything the five numbers know.") as beat:
            beat.wait_until("ellipse", offset=-0.15)
            self.play(FadeOut(VGroup(rise9, rs_lbl, run9, bfl)),
                      self.ell.animate(rate_func=there_and_back).set_stroke(width=8),
                      run_time=0.8)
            beat.wait_until("everything", offset=-0.1)
            self.play(self.dots.animate.set_opacity(1.0), run_time=0.8)
            beat.wait_until("five", offset=-0.1)
            self.play(LaggedStart(*[flag(t) for t in tgts], lag_ratio=0.1), run_time=1.1)

        # replay version one, now watching the ellipse
        self.cen_r = Dot(cen_y.get_center(), radius=0.09, color=RED).set_z_index(1)
        self.box_r = box_mob(ax, T, RED).set_z_index(1)
        self.ell_r = ell_mob(ax, T, RED, 4).set_z_index(1)
        red = VGroup(self.cen_r, self.box_r, self.ell_r)
        with self.narrate("Now replay version one, and watch the ellipse.", gap=0.15) as beat:
            self.add(red)
            self.red_on = True
            beat.wait_until("replay", offset=-0.1)
            self.go(lambda a: lerp(dino, star0, a), 3.2)

        # the prediction hold: the boxes leave so the two ellipses and centres carry the picture;
        # they come back on "Stretch", the move that matches them
        def set_box_op(m, a, lo=0.0, hi=1.0, up=False):
            v = lo + (hi - lo) * (a if up else 1 - a)
            self.box_op = v
            self.box_r.set_stroke(opacity=v)
            box_y.set_stroke(opacity=v)
        # the star steps back to 40 % for the hold, so the two ellipses are the one focal point
        with self.narrate("How would you fix the star? [pause 1.5]") as beat:
            self.play(UpdateFromAlphaFunc(box_y, set_box_op), self.dots.animate.set_opacity(0.4),
                      run_time=0.6)

        with self.narrate("Slide it until the centers meet. Stretch it until the boxes match. "
                          "Then tip it, a slight shear, until it touches the walls at the same "
                          "height.") as beat:
            self.go(lambda a: lerp(star0, slid, a), beat.until("centers", offset=0.5),
                    op_from=0.4, op_to=1.0)
            beat.wait_until("Stretch", offset=-0.05)
            self.go(lambda a: lerp(slid, stretched, a), beat.until("boxes", offset=0.5), smooth,
                    UpdateFromAlphaFunc(box_y, lambda m, a: set_box_op(m, min(1.0, a / 0.35),
                                                                       up=True)))
            beat.wait_until("tip", offset=-0.05)
            self.go(tipped, beat.until("same height", offset=0.2))
            self.red_on = False
            self.play(FadeOut(red), run_time=0.6)

        with self.narrate("All five match now, to every decimal place.", gap=0.65) as beat:
            self.play(flag(self.count, color=GREEN), run_time=0.9)
            beat.wait_until("every", offset=-0.15)
            self.play(LaggedStart(*[flag(n, color=GREEN) for n in self.nows], lag_ratio=0.1),
                      LaggedStart(*[flag(m, color=GREEN) for m in self.marks], lag_ratio=0.1),
                      run_time=1.1)
        self.live = False

        # ================================================================ LIMIT
        self.med_now = DecimalNumber(t2(med_n), num_decimal_places=2, font_size=42, color=RED)
        self.med_now.move_to([X_NOW_L, MED_Y, 0], aligned_edge=LEFT)
        self.med_eq = MathTex("=", font_size=44, color=GREEN).move_to([X_MARK, MED_Y, 0])
        self.med_neq = MathTex(r"\neq", font_size=44, color=RED).move_to([X_MARK, MED_Y, 0])
        self.med_mark = self.med_neq.copy()
        med_row = VGroup(
            MathTex(r"\mathrm{med}\,y", font_size=42).move_to([X_SYM_R, MED_Y, 0],
                                                             aligned_edge=RIGHT),
            MathTex("=", font_size=42).move_to([X_EQ, MED_Y, 0]),
            MathTex(f"{t2(self.med_t):.2f}", font_size=42, color=YELLOW).move_to(
                [X_TGT_L, MED_Y, 0], aligned_edge=LEFT),
            self.med_now, self.med_mark)
        with self.narrate("But add a sixth number, the median of y, and our star misses it by "
                          "six.") as beat:
            beat.wait_until("sixth", offset=-0.15)
            self.play(FadeOut(self.count, shift=0.2 * DOWN), run_time=0.5)
            self.play(LaggedStart(*[FadeIn(m, shift=0.2 * UP) for m in med_row], lag_ratio=0.12),
                      run_time=beat.until("misses", offset=-0.1))
            self.play(Indicate(VGroup(self.med_now, self.med_mark), color=RED, scale_factor=1.1),
                      run_time=0.9)

        # ================================================================ PAYOFF: the dozen
        geo = VGroup(self.ell, box_y, cen_y, tR, tL)
        cite_mf = citation("Matejka & Fitzmaurice, 2017 · CHI", color=TXT_GRAY)
        circle = D["circle"]
        circ_c = circle.mean(0)
        circ_R = float(np.linalg.norm(circle - circ_c, axis=1).mean())
        seq = {"dino": dino}
        cur = match(dino, circle)
        seq["circle"] = cur
        order = ["star", "bullseye", "x_shape", "h_lines", "dots"]
        for name in order:
            cur = match(cur, D[name])
            seq[name] = cur
        five_cols = VGroup(*[VGroup(syms[i], eqs[i], tgts[i], self.nows[i], self.marks[i])
                             for i in range(5)])
        hl5 = box(five_cols, color=YELLOW, buff=0.14)
        require_clear(hl5, hdr_t, hdr_n, med_row, what="'these five' box")
        self.live = self.med_live = True
        # one nudge, acted out: a step toward the target circle breaks the numbers, so it is
        # undone
        j = int(np.argmin(np.linalg.norm(dino - np.array([91.0, 41.5]), axis=1)))   # the tail
        to_c = circ_c - dino[j]
        step = 5.5 * to_c / np.linalg.norm(to_c)             # toward the nearest circle point
        nudged = dino.copy()
        nudged[j] = dino[j] + step
        assert np.linalg.norm(nudged[j] - circ_c) < np.linalg.norm(dino[j] - circ_c)
        ring = Circle(radius=0.15, color=INK, stroke_width=3).move_to(ax.c2p(*fixed_star[j]))
        ring.add_updater(lambda m: m.move_to(self.dots[j].get_center()))
        circ_line = DashedVMobject(Circle(radius=circ_R * ax.x_axis.unit_size, color=GRAY,
                                          stroke_width=2.5).move_to(ax.c2p(*circ_c)),
                                   num_dashes=48, dashed_ratio=0.55)
        with self.narrate("In 2017, Justin Matejka and George Fitzmaurice built a search that "
                          "keeps these five numbers fixed. It nudges a random point toward a "
                          "target shape, and undoes any nudge that breaks them. Repeat it enough "
                          "times, and the dinosaur becomes a circle.", gap=0.35) as beat:
            beat.wait_until("Matejka", offset=-0.3)
            self.play(FadeIn(cite_mf), run_time=0.6)
            self.geo_live = True
            # our star walks back to the dinosaur with the five held; the readout flashes on "these"
            self.go(self.path_fixed(fixed_star, dino), beat.until("these", offset=-0.1))
            # "these five numbers": a box round the five rows (as for Anscombe's), not a scale
            # flash, which would push each value into its "="
            self.play(Create(hl5), run_time=0.6)
            beat.wait_until("nudges", offset=-0.1)
            self.play(Create(ring), Create(circ_line), FadeOut(hl5), run_time=0.6)
            beat.wait_until("toward", offset=-0.15)
            self.go(lambda a: lerp(dino, nudged, a), 0.45)        # x-bar and s_x break
            beat.wait_until("undoes", offset=-0.1)
            self.go(lambda a: lerp(nudged, dino, a), 0.45)        # rejected
            beat.wait_until("breaks", offset=-0.1)
            self.play(Indicate(VGroup(*self.nows), color=INK, scale_factor=1.08),
                      Indicate(VGroup(*self.marks), color=GREEN, scale_factor=1.08),
                      self.ell.animate(rate_func=there_and_back).set_stroke(width=8),
                      FadeOut(ring), run_time=0.7)
            beat.wait_until("Repeat", offset=-0.1)
            self.go(self.path_nudge(dino, seq["circle"]), beat.until("circle", offset=0.3),
                    rate_func=linear)
            self.play(FadeOut(circ_line), run_time=0.5)

        names = ["circle"] + order
        with self.narrate("From the dinosaur they grew twelve shapes, like this star, [pause 1.0] "
                          "this bullseye, [pause 0.8] this X, [pause 1.0] these stripes, "
                          "[pause 0.8] and these dots. Every one of them has this same "
                          "ellipse, and a different median.", gap=0.7) as beat:
            for (prev, nxt), word in zip(zip(names[:-1], names[1:]),
                                         ["star", "bullseye", "X", "stripes", "dots"]):
                beat.wait_until(word, offset=-0.7)          # lands 0.2 s before its noun
                self.go(self.path_fixed(seq[prev], seq[nxt]), 0.5)
            beat.wait_until("Every", offset=-0.1)
            self.play(self.ell.animate.set_stroke(width=9), run_time=0.5)
            self.play(self.ell.animate.set_stroke(width=4.5), run_time=0.4)
            beat.wait_until("different", offset=-0.1)
            self.play(Indicate(VGroup(self.med_now, self.med_mark), color=RED,
                               scale_factor=1.12), run_time=0.9)
        self.geo_live = self.live = self.med_live = False

        # ================================================================ ANSCOMBE
        A = load_anscombe()
        TA = stats(A["I"])
        xa, ya, sxa, sya, ra = TA
        ax2 = main_axes(AN_X, AN_Y, (4, 8, 12), (4, 6, 8, 10), center=PLOT_C)
        cite_an = citation("Anscombe, 1973 · The American Statistician", color=TXT_GRAY)
        scr_now = to_screen(ax, self.cur)
        scr_a = to_screen(ax2, A["I"])
        C = ((scr_now[:, None, :2] - scr_a[None, :, :2]) ** 2).sum(-1)
        pick, col = linear_sum_assignment(C)          # 11 dots chosen, dot pick[j] -> A["I"][col[j]]
        keep = set(int(p) for p in pick)
        dest = {int(p): scr_a[c] for p, c in zip(pick, col)}
        start = {i: self.dots[i].get_center().copy() for i in range(N)}
        dots_a = VGroup(*[self.dots[int(p)] for p in pick])
        pts_a = A["I"][col]

        def to_anscombe(m, a):
            fade = 1 - min(1.0, a / 0.6)
            for i, d in enumerate(self.dots):
                if i in keep:
                    d.move_to(lerp(start[i], dest[i], a))
                    d.set(width=2 * (0.055 + 0.025 * a))
                else:
                    d.set_opacity(fade)
        ell_a = ell_mob(ax2, TA).set_z_index(2)
        box_a = box_mob(ax2, TA).set_z_index(2)
        cen_a = Dot(ax2.c2p(xa, ya), radius=0.09, color=YELLOW).set_z_index(3)
        tch_a = Dot(ax2.c2p(xa + sxa, ya + ra * sya), radius=0.09, color=YELLOW).set_z_index(3)
        tchL_a = Dot(ax2.c2p(xa - sxa, ya - ra * sya), radius=0.075, color=YELLOW).set_z_index(3)
        old_nums = VGroup(ax.x_axis.numbers, ax.y_axis.numbers, ax.x_axis.ticks, ax.y_axis.ticks)
        new_nums = VGroup(ax2.x_axis.numbers, ax2.y_axis.numbers, ax2.x_axis.ticks,
                          ax2.y_axis.ticks)
        new_nums.set_opacity(0)

        # Anscombe's own readout (ordinary rounding, as his numbers are always quoted). It lands
        # mid-right with r first, level with the touch point it sets; on "Least squares" it steps
        # down to the bottom slot to make room for the derivation.
        an_vals = [f"{xa:.2f}", f"{ya:.2f}", f"{sxa:.2f}", f"{sya:.2f}", f"{ra:.2f}"]
        an = [item(s, v) for s, v in zip((r"\bar{x}", r"\bar{y}", "s_x", "s_y", "r"), an_vals)]
        GAP = 0.45
        RA_MID = tch_a.get_center()[1]
        RB_MID = RA_MID - 0.7
        RA_Y = -1.85                                     # bottom slot (upper row)
        an[4].move_to([0.95, 0, 0], aligned_edge=LEFT)
        an[2].next_to(an[4], RIGHT, buff=GAP)
        an[3].next_to(an[2], RIGHT, buff=GAP)
        an[0].move_to([0.95, 0, 0], aligned_edge=LEFT)
        an[1].move_to([an[2].get_left()[0], 0, 0], aligned_edge=LEFT)
        for i_, y_ in ((0, RB_MID), (1, RB_MID), (2, RA_MID), (3, RA_MID), (4, RA_MID)):
            an[i_].shift(UP * (y_ - an[i_][1].get_center()[1]))   # "=" signs on one line
        readout_a = VGroup(*an)
        LOW = DOWN * (RA_MID - RA_Y)
        readout_low = readout_a.copy().shift(LOW)
        require_safe(readout_a, "Anscombe readout (mid)")
        require_safe(readout_low, "Anscombe readout (low)")

        # geometry on Anscombe I: derive the best-fit slope from the box
        slope = ra * sya / sxa
        line_a = Line(ax2.c2p(AN_X[0] + 0.5, ya + slope * (AN_X[0] + 0.5 - xa)),
                      ax2.c2p(AN_X[1] - 0.5, ya + slope * (AN_X[1] - 0.5 - xa)),
                      color=YELLOW, stroke_width=4).set_z_index(2)
        run_seg = Line(ax2.c2p(xa, ya), ax2.c2p(xa + sxa, ya), color=YELLOW,
                       stroke_width=6).set_z_index(3)
        rise_seg = Line(ax2.c2p(xa + sxa, ya), ax2.c2p(xa + sxa, ya + ra * sya), color=YELLOW,
                        stroke_width=6).set_z_index(3)
        # s_x sits under the right part of the run, where the ellipse has already crossed above
        lbl_run = MathTex(r"s_x", font_size=40, color=YELLOW)
        lbl_run.next_to(run_seg.point_from_proportion(0.75), DOWN, buff=0.18).set_z_index(4)
        lbl_rise = MathTex("r", r"\,s_y", font_size=40, color=YELLOW)
        lbl_rise.next_to(rise_seg.point_from_proportion(0.5), RIGHT, buff=0.25).set_z_index(4)
        dots_a_final = VGroup(*[Dot(p, radius=0.08) for p in scr_a])
        for lab, nm in ((lbl_run, "s_x run label"), (lbl_rise, "r s_y rise label")):
            require_clear(lab, ell_a, box_a, cen_a, tch_a, tchL_a, dots_a_final, line_a,
                          what=nm)
        require_clear(lbl_run, rise_seg, what="s_x vs rise")
        require_clear(lbl_rise, run_seg, what="r s_y vs run")
        require_clear(readout_a, ell_a, box_a, tch_a, dots_a_final, line_a, ax2,
                      what="mid readout vs plot")

        FS = 48
        f_lhs = MathTex(r"\text{slope}", "=", font_size=FS)
        f_lhs.move_to([0.9, 1.75, 0], aligned_edge=LEFT)
        frac_l = f_lhs.get_right()[0] + 0.25
        frac_y = f_lhs[1].get_center()[1]

        def frac(num, den, left=frac_l, y=frac_y):
            w_ = max(num.width, den.width) + 0.2
            bar = Line([left, y, 0], [left + w_, y, 0], color=INK, stroke_width=3)
            num.next_to(bar, UP, buff=0.13)
            den.next_to(bar, DOWN, buff=0.13)
            return bar
        # slope = rise / run, each term flown from the labelled segment it measures
        numC = MathTex("r", r"\,s_y", font_size=FS, color=YELLOW)
        denC = MathTex("s_x", font_size=FS, color=YELLOW)
        barC = frac(numC, denC)
        require_safe(VGroup(f_lhs, numC, barC, denC), "slope = r s_y / s_x")

        # the substitution, left-aligned under "slope"; numbers arrive from the readout
        FS2 = 44
        s_eq = MathTex("=", font_size=FS2)
        sub_n1 = MathTex(an_vals[4], font_size=FS2, color=YELLOW)
        sub_x = MathTex(r"\times", font_size=FS2)
        sub_n2 = MathTex(an_vals[3], font_size=FS2, color=YELLOW)
        sub_num = VGroup(sub_n1, sub_x, sub_n2).arrange(RIGHT, buff=0.14)
        sub_den = MathTex(an_vals[2], font_size=FS2, color=YELLOW)
        sub_ap = MathTex(r"\approx", font_size=FS2)
        sub_val = MathTex(f"{slope:.2f}", font_size=FS2, color=YELLOW)
        s_eq.move_to([f_lhs.get_left()[0], 0, 0], aligned_edge=LEFT)
        sub_bar = frac(sub_num, sub_den, left=s_eq.get_right()[0] + 0.22, y=s_eq.get_center()[1])
        sub_ap.next_to(sub_bar, RIGHT, buff=0.22).match_y(s_eq)
        sub_val.next_to(sub_ap, RIGHT, buff=0.22).match_y(s_eq)
        subst = VGroup(s_eq, sub_num, sub_bar, sub_den, sub_ap, sub_val)
        sub_top = denC.get_bottom()[1] - 0.5
        subst.shift(UP * (sub_top - subst.get_top()[1]))
        require_safe(subst, "substitution")
        require_clear(subst, readout_low, what="substitution vs readout")
        require_clear(VGroup(f_lhs, numC, denC), subst, what="slope vs substitution")
        require_clear(VGroup(f_lhs, numC, denC, barC), readout_low, what="slope vs readout")

        with self.narrate("Francis Anscombe made the point in 1973, with eleven points of his "
                          "own.", gap=0.2) as beat:
            self.add(ax2)                    # same frame, axis lines and names as ax
            # the dinosaur's values leave with the dinosaur; the empty symbol slots wait for his
            self.play(FadeOut(VGroup(hdr_t, hdr_n, *self.nows, *self.marks, med_row),
                              shift=0.15 * RIGHT),
                      *[FadeOut(tgts[i], shift=0.2 * DOWN) for i in range(5)],
                      FadeOut(VGroup(*syms, *eqs), shift=0.15 * LEFT), run_time=0.5)
            beat.wait_until("Anscombe", offset=-0.25)
            T_m = beat.until("eleven", offset=-0.05)
            self.play(Succession(FadeOut(cite_mf, run_time=0.35), FadeIn(cite_an, run_time=0.35),
                                 Wait(run_time=max(0.1, T_m - 0.7))),
                      # old tick labels out first, new ones in after (never overlapping); driven
                      # through the axes already in the scene so nothing gets restructured
                      UpdateFromAlphaFunc(ax, lambda m, a: old_nums.set_opacity(max(0.0, 1 - a / 0.4))),
                      UpdateFromAlphaFunc(ax2, lambda m, a: new_nums.set_opacity(
                          min(1.0, max(0.0, (a - 0.55) / 0.45)))),
                      UpdateFromAlphaFunc(self.dots, to_anscombe),
                      Transform(self.ell, ell_a), Transform(box_y, box_a), Transform(cen_y, cen_a),
                      Transform(tR, tch_a), Transform(tL, tchL_a),
                      # his readout arrives whole, entry by entry, in its own two-row layout
                      # (r first) while his points travel: the right half is empty for well
                      # under a second, and no "r =" ever waits without its value
                      LaggedStart(*[FadeIn(an[i], shift=0.1 * UP) for i in (4, 2, 3, 0, 1)],
                                  lag_ratio=0.15, rate_func=window(0.12, 0.6)),
                      run_time=T_m)
            self.remove(ax)
            self.remove(self.dots)
            self.add(dots_a)
            beat.wait_until("points", offset=-0.1)
            # his eleven points flagged on "points"
            self.play(LaggedStart(*[Indicate(d, color=BLUE, scale_factor=1.6) for d in dots_a],
                                  lag_ratio=0.06), run_time=1.0)

        with self.narrate("His correlation is point eight two, so the ellipse touches the right "
                          "wall high up.") as beat:
            beat.wait_until("correlation", offset=-0.15)
            self.play(flag(an[4]), run_time=0.8)
            beat.wait_until("touches", offset=-0.5)
            # r is level with the touch point: its value travels straight left, intact, and
            # settles into the touch dot (no glyph-to-dot morph)
            c82 = an[4][2].copy()
            d82 = c82.copy().next_to(tR, RIGHT, buff=0.3)
            # up out of its row first (never across "r ="), then left to the touch dot
            self.play(ReplacementTransform(c82, d82, path_func=lift_path(c82, d82, 1.0, (0.6, 0.0))),
                      run_time=0.7)
            self.play(FadeOut(d82, target_position=tR.get_center(), scale=0.3), flag(tR),
                      run_time=0.6)

        # B9's rule, recognised: one s_x across, r s_y up, through the centre and the touch point.
        # The labels come from Anscombe's readout; then slope = rise / run is built from them.
        with self.narrate("His best-fit line follows the same rule: one ess ex across, r ess why "
                          "up, through the center and that touch point.", gap=0.2) as beat:
            # make room for the formula
            self.play(readout_a.animate.shift(LOW), run_time=0.8)
            beat.wait_until("one", offset=-0.45)
            self.play(Indicate(an[2][0], color=YELLOW, scale_factor=1.25), run_time=0.35)
            # each symbol copy lifts straight out of the readout, then travels to its segment.
            # The copies are built with the same structure as their targets (a whole MathTex
            # into a whole MathTex, a part into a part), so every glyph maps onto itself and
            # the symbol stays legible in flight
            p_sx = MathTex("s_x", font_size=36).move_to(an[2][0])
            self.play(Create(run_seg), ReplacementTransform(
                p_sx, lbl_run, path_func=lift_path(p_sx, lbl_run, 1.0, (0.6, 0.0))),
                run_time=0.8)
            beat.wait_until("r ess", offset=-0.4)
            # each symbol flagged about its own centre (a group Indicate pushed s_y into its "=")
            self.play(Indicate(an[4][0], color=YELLOW, scale_factor=1.25),
                      Indicate(an[3][0], color=YELLOW, scale_factor=1.25), run_time=0.35)
            p_r = MathTex("r", font_size=36).move_to(an[4][0])[0]
            p_sy = MathTex("s_y", font_size=36).move_to(an[3][0])[0]
            self.play(Create(rise_seg),
                      ReplacementTransform(p_r, lbl_rise[0],
                                           path_func=lift_path(p_r, lbl_rise[0], 1.0)),
                      ReplacementTransform(p_sy, lbl_rise[1],
                                           path_func=lift_path(p_sy, lbl_rise[1], 1.0)),
                      run_time=0.8)
            beat.wait_until("center", offset=-0.2)
            self.play(flag(cen_y), run_time=0.5)
            self.play(GrowFromPoint(line_a, cen_y.get_center()),
                      run_time=max(0.8, beat.until("point", offset=0.0)))
            self.play(flag(tR), run_time=0.6)

        bar = barC
        f1 = VGroup(f_lhs, numC, bar, denC)
        with self.narrate("So the slope is rise over run. [pause 1.0] Plug in his numbers, and "
                          "it's one half.") as beat:
            beat.wait_until("slope", offset=-0.15)
            self.play(Write(f_lhs), run_time=0.55)
            # the numerator climbs straight up from the rise, then crosses high above
            # "slope =" and drops into place (never through the formula); the denominator's
            # flight dips under it
            beat.wait_until("rise", offset=-0.2)
            c_rise = lbl_rise.copy()
            hi_y = f_lhs.get_top()[1] + 0.75
            self.play(ReplacementTransform(c_rise, numC, path_func=bez_path(
                          c_rise, numC, (c_rise.get_x(), hi_y + 0.1), (numC.get_x() - 0.8, hi_y + 0.25))),
                      Create(barC, rate_func=window(0.4, 1.0)), run_time=0.8)
            beat.wait_until("run", offset=-0.2)
            self.play(TransformFromCopy(lbl_run, denC, path_arc=-0.7), run_time=0.75)
            beat.wait_until("Plug", offset=-0.5)
            srcs = [an[4][2], an[3][2], an[2][2]]
            dsts = [sub_n1, sub_n2, sub_den]
            self.play(Write(s_eq), Indicate(srcs[0], color=YELLOW, scale_factor=1.15),
                      run_time=0.4)
            # the fraction bar grows with the first value's flight: never an empty template
            # each value: a whole-MathTex copy (same structure as its target, so the digits
            # map onto themselves) lifts out of the readout row, then travels up to its slot
            def fly_val(k):
                pr_ = MathTex(an_vals[(4, 3, 2)[k]], font_size=36, color=YELLOW).move_to(srcs[k])
                return ReplacementTransform(pr_, dsts[k], path_func=lift_path(pr_, dsts[k], 0.6))
            self.play(fly_val(0), Create(sub_bar), Write(sub_x),
                      Indicate(srcs[1], color=YELLOW, scale_factor=1.15), run_time=0.55)
            self.play(fly_val(1), Indicate(srcs[2], color=YELLOW, scale_factor=1.15),
                      run_time=0.55)
            self.play(fly_val(2), run_time=0.55)
            beat.wait_until("half", offset=-0.45)
            self.play(Write(sub_ap), Write(sub_val), run_time=0.5)
            self.play(flag(sub_val), run_time=0.8)

        # four panels
        px = [-4.575, -1.475, 1.625, 4.725]
        PY = 0.68
        panels, pdots, pells, plines = [], [], [], []
        for jj, key in enumerate(["I", "II", "III", "IV"]):
            p = axes((0, 20), (0, 15), x_length=2.55, y_length=2.6, x_ticks=[0, 10, 20],
                     y_ticks=[0, 5, 10, 15])
            p.shift(np.array([px[jj], PY, 0]) - (p.c2p(0, 0) + p.c2p(20, 15)) / 2)
            p.x_axis.numbers.set_color(TXT_GRAY)
            p.y_axis.numbers.set_color(TXT_GRAY)
            if jj > 0:
                p.y_axis.remove(p.y_axis.numbers)
            panels.append(p)
            data = A[key]
            pdots.append(VGroup(*[Dot(p.c2p(*q), radius=0.06, color=BLUE) for q in data]))
            s = stats(data)
            pells.append(ell_mob(p, s, sw=3.5))
            sl = s[4] * s[3] / s[2]
            plines.append(Line(p.c2p(1, s[1] + sl * (1 - s[0])), p.c2p(19, s[1] + sl * (19 - s[0])),
                               color=YELLOW, stroke_width=3))
        p_xt = MathTex("x", font_size=34, color=TXT_GRAY).next_to(panels[3].c2p(20, 0), RIGHT, buff=0.15)
        p_xt.shift(UP * 0.12)                                # clear of the "20" tick label
        p_yt = MathTex("y", font_size=34, color=TXT_GRAY).next_to(panels[0].c2p(0, 15), UP, buff=0.15)
        p_yt.shift(RIGHT * 0.15)                             # clear of the "15" tick label
        top_f1, top_ap, top_val = f1.copy().scale(0.85), sub_ap.copy(), sub_val.copy()
        top_row = VGroup(top_f1, top_ap, top_val).arrange(RIGHT, buff=0.22).move_to([0, 3.0, 0])
        # labels on one baseline: every tag starts with a letter that sits on it (a, a, a, o)
        tags = [label(t) for t in ("a trend", "a curve", "an outlier", "one point")]
        panel_floor = min(p.get_bottom()[1] for p in panels)
        tag_base = panel_floor - 0.36 - tags[0][0].height
        for jj, t in enumerate(tags):
            t.move_to([px[jj], 0, 0])
            t.shift(UP * (tag_base - t[0].get_bottom()[1]))
        tags_floor = min(t.get_bottom()[1] for t in tags)
        # the readout steps down under panels III-IV, >= 0.45 below the labels
        q_top = tags_floor - 0.5
        Q_SHIFT = UP * (q_top - readout_low.get_top()[1])
        readout_q = readout_low.copy().shift(Q_SHIFT)
        ring3 = Circle(radius=0.16, color=INK, stroke_width=3).move_to(panels[2].c2p(13, 12.74))
        ring4 = Circle(radius=0.16, color=INK, stroke_width=3).move_to(panels[3].c2p(19, 12.5))
        dest1 = [panels[0].c2p(*q) for q in pts_a]
        start1 = [d.get_center().copy() for d in dots_a]
        require_safe(readout_q, "quartet readout")
        require_safe(top_row, "quartet slope row")
        require_clear(readout_q, cite_an, *panels, what="quartet readout")
        require_clear(readout_q, *tags, gap=0.45, what="quartet readout vs labels")
        require_clear(top_row, p_yt, *panels, what="quartet slope row")
        for t in tags:
            require_clear(t, *panels, *pdots, what="quartet tag")
            require_safe(t, "quartet tag")

        ap_t = sub_ap.copy().next_to(bar, RIGHT, buff=0.25).match_y(bar)
        val_t = sub_val.copy().next_to(ap_t, RIGHT, buff=0.22).match_y(bar)
        require_safe(VGroup(f1, ap_t, val_t), "slope = r s_y / s_x = 0.50")
        hl_read = box(readout_low, color=YELLOW, buff=0.15)

        def shrink(m, a):
            for d, s0_, d1 in zip(dots_a, start1, dest1):
                d.move_to(lerp(s0_, d1, a))
                d.set(width=2 * (0.08 - 0.02 * a))

        with self.narrate("All four of his datasets share these five numbers, so they share the "
                          "ellipse and the line. [pause 0.3] A trend, a curve, an outlier, and one "
                          "point doing all the work.", gap=0.1) as beat:
            self.play(FadeOut(VGroup(box_y, tR, tL, run_seg, rise_seg, lbl_run, lbl_rise,
                                     s_eq, sub_num, sub_bar, sub_den)),
                      sub_ap.animate.move_to(ap_t), sub_val.animate.move_to(val_t), run_time=0.7)
            beat.wait_until("these five", offset=-0.1)
            self.play(Create(hl_read), run_time=0.5)
            # the two sets of axis lines crossfade over the same stretch (the points are never
            # without axes); the tick numbers hand over in sequence so they never overprint
            axes_op(panels[0], 0.0, 0.0)
            self.add(panels[0])
            self.bring_to_front(dots_a)
            self.play(UpdateFromAlphaFunc(ax2, lambda m, a: axes_op(
                          ax2, 1 - window(0.0, 0.55)(a), 1 - window(0.0, 0.3)(a)), rate_func=linear),
                      UpdateFromAlphaFunc(panels[0], lambda m, a: axes_op(
                          panels[0], window(0.0, 0.55)(a), window(0.35, 0.7)(a)), rate_func=linear),
                      FadeOut(cen_y), FadeOut(hl_read, rate_func=window(0.0, 0.4)),
                      UpdateFromAlphaFunc(dots_a, shrink),
                      Transform(self.ell, pells[0]), Transform(line_a, plines[0]),
                      Transform(f1, top_f1), Transform(sub_ap, top_ap), Transform(sub_val, top_val),
                      readout_a.animate.shift(Q_SHIFT),
                      *[FadeIn(VGroup(panels[jj], pdots[jj]),
                               rate_func=window(0.45 + 0.12 * jj, 0.75 + 0.08 * jj))
                        for jj in (1, 2, 3)],
                      FadeIn(p_xt, rate_func=window(0.5, 1.0)),
                      FadeIn(p_yt, rate_func=window(0.5, 1.0)), run_time=1.4)
            self.remove(ax2)
            # copies arc over the panel row, farthest panel first, so no two ever overlap
            beat.wait_until("ellipse", offset=-0.15)
            self.play(LaggedStart(*[TransformFromCopy(self.ell, pells[jj], path_arc=0.6)
                                    for jj in (3, 2, 1)],
                                  *[TransformFromCopy(line_a, plines[jj], path_arc=0.6)
                                    for jj in (3, 2, 1)], lag_ratio=0.5), run_time=1.75)
            beat.wait_until("trend", offset=-0.15)
            self.play(FadeIn(tags[0], shift=0.1 * UP), run_time=0.5)
            beat.wait_until("curve", offset=-0.15)
            self.play(FadeIn(tags[1], shift=0.1 * UP), run_time=0.5)
            beat.wait_until("outlier", offset=-0.15)
            self.play(FadeIn(tags[2], shift=0.1 * UP), Create(ring3), run_time=0.6)
            beat.wait_until("one point", offset=-0.15)
            self.play(FadeIn(tags[3], shift=0.1 * UP), Create(ring4), run_time=0.6)

        # ================================================================ LANDING
        # Panel I's ellipse is carried home and so is "slope = r s_y / s_x": the quartet leaves
        # first, the ellipse grows back to the dinosaur-scale ellipse, the formula takes the
        # top-right slot, then the opening frame returns around them.
        f1_fam = set(f1.get_family())
        quartet = [m_ for m_ in self.mobjects
                   if m_ is not self.ell and not (set(m_.get_family()) & f1_fam)]
        self.ax = ax = main_axes()
        self.dots = VGroup(*[Dot(radius=0.055, color=GRAY) for _ in range(N)])
        self.place(guess)
        ell_l = ell_mob(ax, T).set_z_index(2)
        guess_lbl2 = guess_lbl.copy()
        guess_line2 = DashedLine(*line_xy(ax), color=GRAY, stroke_width=3, dash_length=0.14)
        line_lbl2 = line_lbl.copy()
        line_l = Line(*line_xy(ax), color=YELLOW, stroke_width=4).set_z_index(3)
        cen_l = ax.c2p(T[0], T[1])
        opening = VGroup(ax, table_cold, self.dots, guess_lbl2, guess_line2, line_lbl2)
        # the stakes bar returns: an average and an error bar are two of the five numbers
        bar_l = bar_rect.copy().set_fill(opacity=0.22).set_stroke(opacity=1.0).set_z_index(1)
        err_l = vbar(ax, T[0], T[1], T[3], YELLOW, sw=4, cap=0.16).set_z_index(3)
        pct86_l = pct_label(r"86\%", "used bars")         # top left, where "your guess" was
        pct86_l.next_to(ax.c2p(3, 100), DR, buff=0.0).shift(DOWN * 0.1 + RIGHT * 0.05)
        cite_w2 = citation("Weissgerber et al., 2015 · PLOS Biology", color=TXT_GRAY)
        require_clear(pct86_l, self.dots, bar_l, err_l, ell_l, line_l, what="landing '86%'")
        require_safe(pct86_l, "landing '86%'")
        rows_two = VGroup(table_cold[1], table_cold[3])          # y-bar and s_y
        squash = ell_l.copy().set_z_index(3)
        # at the very end the bar and error bar step out of the plot, beside the 142 points
        bar_dx = RIGHT * (ax.c2p(124, 0)[0] - ax.c2p(T[0], 0)[0])
        bar_out = VGroup(bar_l.copy(), err_l.copy()).shift(bar_dx)
        require_clear(ax.x_name, bar_out, what="axis name vs parked bar")
        require_clear(table_cold, bar_out, what="readout vs parked bar")

        # "your line" answered with a number: the dinosaur's r, s_y and s_x go into the slope
        FSL = 40
        l_lhs = MathTex(r"\text{slope}", "=", font_size=FSL)
        l_num = MathTex("r", r"\,s_y", font_size=FSL, color=YELLOW)
        l_den = MathTex("s_x", font_size=FSL, color=YELLOW)
        v_n1 = MathTex(f"{TR[4]:.2f}", font_size=FSL, color=YELLOW)
        v_x = MathTex(r"\times", font_size=FSL)
        v_n2 = MathTex(f"{TR[3]:.2f}", font_size=FSL, color=YELLOW)
        v_num = VGroup(v_n1, v_x, v_n2).arrange(RIGHT, buff=0.12)
        v_den = MathTex(f"{TR[2]:.2f}", font_size=FSL, color=YELLOW)
        v_ap = MathTex(r"\approx", font_size=FSL)
        v_val = MathTex(f"{TR[4] * TR[3] / TR[2]:.2f}", font_size=FSL, color=YELLOW)
        assert f"{TR[4] * TR[3] / TR[2]:.2f}" == f"{slope_d:.2f}" == "-0.10"
        # under the readout (the open band below the r row), not squeezed into the strip above
        # x-bar: the r value is the closest row, and every value flies down into it
        l_lhs.move_to([0.5, -1.85, 0], aligned_edge=LEFT)
        fl_left, fl_y = l_lhs.get_right()[0] + 0.22, l_lhs[1].get_center()[1]
        l_bar = frac(l_num, l_den, left=fl_left, y=fl_y)
        v_bar = frac(v_num, v_den, left=fl_left, y=fl_y)
        v_num.shift(UP * 0.05)                               # >= 0.15 from the fraction bar
        v_den.shift(DOWN * 0.05)
        v_ap.next_to(v_bar, RIGHT, buff=0.22).match_y(l_lhs[1])
        v_val.next_to(v_ap, RIGHT, buff=0.22).match_y(l_lhs[1])
        f_land = VGroup(l_lhs, l_num, l_bar, l_den)
        land_eq = VGroup(l_lhs, v_num, v_bar, v_den, v_ap, v_val)
        require_safe(land_eq, "landing slope", right=6.35)
        require_clear(land_eq, table_cold, ax, what="landing slope vs readout and plot")
        require_clear(land_eq, table_cold, gap=0.25, what="landing slope vs readout (breathing room)")
        require_clear(VGroup(f_land, v_ap, v_val), self.dots, guess_line2, line_lbl2, ell_l, line_l,
                      what="landing slope vs the cloud and its lines")
        assert table_cold.get_bottom()[1] - land_eq.get_top()[1] >= 0.25

        # one continuous object: the quartet leaves, then the opening returns around the ellipse.
        # The formula sets off only once the quartet has gone and has cleared the readout's slot
        # before the opening fades in, so it never crosses the panels or the readout
        self.play(FadeOut(Group(*quartet), rate_func=window(0.0, 0.32)),
                  ReplacementTransform(self.ell, ell_l, rate_func=window(0.0, 0.7)),
                  Transform(f1, f_land, rate_func=window(0.3, 0.72)),
                  FadeIn(opening, rate_func=window(0.55, 0.95)), run_time=1.35)
        with self.narrate("Your line was exactly right: five numbers fix its slope, minus point "
                          "one. Your cloud was wrong: a blur around this ellipse, all that five "
                          "numbers can draw. [pause 0.6] Most of those papers used a bar graph, "
                          "which draws only two. [pause 0.6] The dinosaur lived in everything they "
                          "leave out.") as beat:
            beat.wait_until("exactly", offset=-0.15)
            self.play(Indicate(VGroup(guess_line2, line_lbl2), color=INK, scale_factor=1.0),
                      run_time=0.7)
            # the symbols give way to the dinosaur's own values, flown down from the readout:
            # r (the bottom row) drops straight out of its row and slides left into its slot;
            # s_y and s_x leave sideways and descend a lane right of the readout, so neither
            # crosses another row, then slide in from the right
            beat.wait_until("five numbers", offset=-0.5)
            flights = []
            for i_, dst_ in ((4, v_n1), (3, v_n2), (2, v_den)):
                src_ = table_cold[i_][2]
                pf_ = (lift_path(src_, dst_, -0.6) if i_ == 4 else
                       lane_path(6.0, src_, dst_, 0.0))
                # a whole-MathTex copy (same structure as its target), so each glyph maps onto
                # itself and the number stays legible in flight
                cp_ = MathTex(f"{TR[i_]:.2f}", font_size=42, color=YELLOW).move_to(src_)
                flights.append(ReplacementTransform(cp_, dst_, path_func=pf_))
            # each symbol gives way only as its value arrives (numerator values land at about
            # 0.62 and 0.81 of the move, the denominator's at 1.0), so the formula never reads
            # as an empty template
            self.play(f1[1].animate(rate_func=window(0.4, 0.72)).set_opacity(0),
                      f1[3].animate(rate_func=window(0.68, 0.95)).set_opacity(0),
                      Transform(f1[2], v_bar, rate_func=window(0.25, 0.6)),
                      LaggedStart(*flights, lag_ratio=0.3),
                      FadeIn(v_x, rate_func=window(0.55, 0.8)), run_time=1.3)
            beat.wait_until("slope", offset=-0.35)
            self.play(GrowFromPoint(line_l, cen_l), run_time=0.7)
            beat.wait_until("minus", offset=-0.15)
            self.play(Write(v_ap), Write(v_val), run_time=0.6)
            beat.wait_until("cloud", offset=-0.1)
            self.play(Indicate(guess_lbl2, color=INK, scale_factor=1.1), run_time=0.8)
            beat.wait_until("this ellipse", offset=-0.1)
            self.play(ell_l.animate(rate_func=there_and_back).set_stroke(width=8),
                      self.dots.animate.set_opacity(0.35), run_time=0.9)
            beat.wait_until("all that", offset=-0.1)
            self.play(FadeOut(VGroup(guess_lbl2, line_lbl2, guess_line2)),
                      VGroup(ell_l, line_l).animate(rate_func=there_and_back).set_stroke(width=7),
                      run_time=0.9)
            beat.wait_until("Most", offset=-0.1)
            # the line steps back to 30 % and the ellipse to 60 %, so the squeezed copy, the bar
            # and the error bar are the only full-strength strokes where they meet
            self.play(FadeIn(cite_w2), FadeIn(pct86_l, shift=0.1 * DOWN),
                      FadeOut(VGroup(f1, v_num, v_den, v_ap, v_val)),
                      self.dots.animate.set_opacity(0.15),
                      line_l.animate.set_stroke(opacity=0.3),
                      ell_l.animate.set_stroke(opacity=0.6), run_time=0.6)
            beat.wait_until("bar graph", offset=-0.15)
            # the ellipse squeezed to its vertical extent is exactly the error bar, y-bar +- s_y
            self.add(squash)
            self.play(squash.animate.stretch(0.01, 0), GrowFromEdge(bar_l, DOWN), run_time=1.1)
            self.play(FadeIn(err_l), FadeOut(squash), run_time=0.3)
            beat.wait_until("two", offset=-0.15)
            self.play(flag(rows_two), run_time=0.8)
            beat.wait_until("dinosaur", offset=-0.2)
            # the points return; the two numbers step out of the plot and sit beside them
            self.go(lambda a: lerp(guess, dino, a), 1.6, smooth,
                    bar_l.animate.shift(bar_dx).set_fill(opacity=0.09).set_stroke(opacity=0.4),
                    err_l.animate.shift(bar_dx).set_stroke(opacity=0.4),
                    FadeOut(pct86_l, rate_func=window(0.0, 0.35)),
                    line_l.animate.set_stroke(opacity=1.0), ell_l.animate.set_stroke(opacity=1.0),
                    color_from=GRAY, color_to=BLUE, op_from=0.15, op_to=1.0)

        # clean exit: the plot leaves first, so the card never sits on top of the data
        self.play(*[FadeOut(m) for m in list(self.mobjects)], run_time=0.4)
        self.end_card(hold=0.6, run_time=0.4)
