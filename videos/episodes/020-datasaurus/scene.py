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


def sim_cloud(seed, Tt, zones, lo=0.8, hi=99.2, tries=200):
    """The simulated what-if cloud (B9): 142 points uniform inside the Mahalanobis disc of
    radius 2 (unit SD per coordinate), given exactly the five numbers Tt by `fix`. A point
    that lands outside the plot, or under one of the labels that must sit on bare background
    (`zones`: data-coordinate boxes (cx, cy, half_w, half_h)), is drawn again from the same
    generator and the five numbers are re-imposed, until none does. Returns the points and
    how many were redrawn."""
    g = np.random.default_rng(seed)

    def disc(n):
        th = g.uniform(0, 2 * np.pi, n)
        rad = 2 * np.sqrt(g.uniform(0, 1, n))
        return np.column_stack([rad * np.cos(th), rad * np.sin(th)])
    raw = disc(N)
    redrawn = 0
    for _ in range(tries):
        P = fix(raw, Tt)
        bad = (P.min(1) < lo) | (P.max(1) > hi)
        for cx, cy, hx, hy in zones:
            bad |= (np.abs(P[:, 0] - cx) < hx) & (np.abs(P[:, 1] - cy) < hy)
        if not bad.any():
            return P, redrawn
        redrawn += int(bad.sum())
        raw[bad] = disc(int(bad.sum()))
    raise RuntimeError("sim_cloud: no clean cloud for this seed")


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
SIM_SEED = 19530                          # the simulated r = 0.50 cloud (B9): fits the plot, label and rise spots bare, slice mean on the line
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


def elbow_path(src, dst, cx, t1=0.28, t2=0.72):
    """path_func for ReplacementTransform(src_copy, dst): the copy's centre slides sideways to
    the lane x = cx at the source's height, runs straight down (or up) the lane, then slides
    sideways into the target, each leg eased. Unlike a Bezier through the same corners it
    really stays in the lane, so it never cuts the corner through text beside the lane. The
    shape (and size) interpolate as usual; the offset is the same for every glyph."""
    cs, ce = src.get_center(), dst.get_center()
    A = np.array([cx, cs[1], 0.0])
    B = np.array([cx, ce[1], 0.0])

    def centre(a):
        if a <= t1:
            return cs + (A - cs) * smooth(a / t1)
        if a <= t2:
            return A + (B - A) * smooth((a - t1) / (t2 - t1))
        return B + (ce - B) * smooth((a - t2) / (1 - t2))

    def pf(s, e, a):
        return s + (e - s) * a + (centre(a) - (cs + (ce - cs) * a))
    return pf


def dip(*ms, lo=0.2, out=0.05, back=0.75, start=0.0):
    """While a copy flies out of a table glyph, the source steps back to `lo` (over the first
    `out` of the move) and returns once the copy is clear (from `back`), so the two never read
    as one doubled glyph. Use with rate_func=linear. `start`: the copy sets off later in a
    longer play (alpha units)."""
    def f(m, a):
        if a < start:
            v = 1.0
        elif a < back:
            v = 1 - (1 - lo) * min(1.0, (a - start) / out)
        else:
            v = lo + (1 - lo) * min(1.0, (a - back) / (1 - back))
        for x in ms:
            x.set_opacity(v)
    return UpdateFromAlphaFunc(VGroup(*ms), f, rate_func=linear)


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
    CADENCE = "shaped"          # sense-shaped gaps: longer at turns and after results (§13.3)

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
        # Frame 1 is already the puzzle: the five numbers written in, an empty plot holding a
        # faint "?" (the cloud's shape) and the count. The commit asks for both halves: the shape
        # (likely wrong: a shapeless oval) and the tilt of the line (likely right: nearly flat).
        # While the tilt is asked, three candidate lines through (x-bar, y-bar) are drawn: up,
        # nearly flat (the line the five numbers fix, slope -0.10) and down
        qmark = MathTex("?", font_size=110, color=GRAY).move_to(ax.c2p(54, 75))
        qmark.set_opacity(0.55)
        n_lbl.move_to(ax.c2p(54, 21))                        # below the candidate lines

        def cand_line(sl, x0=12, x1=96):
            return DashedLine(ax.c2p(x0, T[1] + sl * (x0 - T[0])), ax.c2p(x1, T[1] + sl * (x1 - T[0])),
                              color=GRAY, stroke_width=3, dash_length=0.14).set_stroke(opacity=0.6)
        cands = [cand_line(sl) for sl in (0.6, slope_d, -0.6)]
        guess_line = cands[1]                                # the nearly flat one becomes "your line"
        for c_ in cands:
            require_clear(qmark, c_, what="'?' vs candidate line")
            require_clear(n_lbl, c_, what="'n = 142' vs candidate line")
        self.add(ax, n_lbl, qmark, *rows)
        with self.narrate("Two averages, two standard deviations, and a correlation of minus "
                          "point oh six. What shape is the cloud, and which way does its best-fit "
                          "line tilt? [pause 1.8]") as beat:
            beat.wait_until("averages", offset=-0.2)
            self.play(flag(VGroup(tgts[0], tgts[1])), run_time=0.8)
            beat.wait_until("standard", offset=-0.2)
            self.play(flag(VGroup(tgts[2], tgts[3])), run_time=0.8)
            beat.wait_until("minus", offset=-0.15)
            self.play(flag(tgts[4]), run_time=0.9)
            beat.wait_until("shape", offset=-0.2)
            self.play(qmark.animate(rate_func=there_and_back).scale(1.15).set_opacity(0.9),
                      run_time=0.9)
            beat.wait_until("which", offset=-0.1)
            self.play(LaggedStart(*[Create(c_) for c_ in cands], lag_ratio=0.3),
                      run_time=beat.until_end_of("tilt", offset=0.1))

        with self.narrate("You probably pictured a shapeless oval, with a nearly flat line. Here "
                          "are the real points. [pause 1.1] A dinosaur, drawn by Alberto Cairo, "
                          "with these same five numbers.", gap=0.65) as beat:
            self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in
                                    sorted(self.dots, key=lambda d: np.linalg.norm(
                                        d.get_center() - ax.c2p(*T[:2])))], lag_ratio=0.012),
                      FadeOut(qmark, scale=1.2, rate_func=lambda t: smooth(min(1.0, 3 * t))),
                      FadeOut(n_lbl, rate_func=lambda t: smooth(min(1.0, 3 * t))),
                      FadeIn(guess_lbl), run_time=beat.until("nearly", offset=-0.1))
            self.remove(*self.dots)
            self.add(self.dots)
            # the two wrong tilts leave; the nearly flat one is "your line"
            self.play(FadeOut(cands[0]), FadeOut(cands[2]),
                      guess_line.animate.set_stroke(opacity=1.0),
                      FadeIn(line_lbl, shift=0.1 * LEFT),
                      run_time=beat.until("Here", offset=-0.1))
            # the reveal: 1.8 s from "real", then a 0.4 s look before it is named
            beat.wait_until("real", offset=-0.25)              # lands on "Here are the real…"
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
                           color=YELLOW, stroke_width=3, fill_color=YELLOW,
                           fill_opacity=0.12).set_z_index(1)
        # the error bar is drawn over the (dimmed) strip, so the +- s_y it names is never buried
        err_bar = vbar(ax, T[0], T[1], T[3], YELLOW, sw=5, cap=0.16).set_z_index(3)
        def pct_label(num, words):
            return VGroup(MathTex(num, font_size=36, color=TXT_GRAY),
                          Text(words, font=SERIF, font_size=28, color=TXT_GRAY)).arrange(
                DOWN, buff=0.12, aligned_edge=LEFT)
        pct86 = pct_label(r"86\%", "used bars").next_to(bar_rect, LEFT, buff=0.3)
        pct13 = pct_label(r"13\%", "showed points").next_to(bar_rect, RIGHT, buff=0.3)
        pct13.set_y(ax.c2p(0, 62)[1])
        require_safe(pct86, "'86% used bars'")
        x_ctx = VGroup(ax.x_axis.numbers, ax.x_axis.ticks, ax.x_name)
        strip_dots = VGroup(*[Dot(p, radius=0.055) for p in to_screen(ax, strip)])
        # which error bar this is: most of the reviewed bar graphs drew +- SE (Weissgerber 2015),
        # ours is +- 1 SD (the squeezed ellipse at the landing has exactly that extent)
        def sd_tag_for(cap_pt, bar_right):
            t_ = MathTex(r"\pm 1\ \text{SD}", font_size=36, color=TXT_GRAY)
            t_.move_to([bar_right + 0.2 + t_.width / 2, cap_pt[1] + 0.06, 0])
            return t_
        sd_tag = sd_tag_for(ax.c2p(T[0], T[1] + T[3]), bar_rect.get_right()[0])
        require_clear(pct86, strip_dots, bar_rect, err_bar, what="'86 %'")
        require_clear(pct13, strip_dots, bar_rect, err_bar, what="'13 %'")
        require_clear(sd_tag, strip_dots, bar_rect, err_bar, pct13, what="'+-1 SD' tag")
        # (round 8: a breath after "papers" and speed 0.80, so 703 and 86 % each get their own beat)
        with self.narrate("In a review of seven hundred three physiology papers, [pause 0.4] "
                          "eighty-six percent used bar graphs: [pause 0.4] an average and an error "
                          "bar. [pause 0.6] Only thirteen percent showed the points.", speed=0.80,
                          gap=0.75) as beat:
            self.play(Succession(FadeOut(cite_cairo, run_time=0.3), FadeIn(cite_w, run_time=0.3)),
                      run_time=0.6)
            beat.wait_until("papers", offset=-0.2)
            # the strip keeps every y but squeezes x, so the x ticks stop meaning anything
            self.go(lambda a: lerp(dino, strip, a), 1.2, smooth,
                    UpdateFromAlphaFunc(ax, lambda m, a: x_ctx.set_opacity(1 - 0.75 * a)))
            beat.wait_until("bar graphs", offset=-0.1)
            self.play(GrowFromEdge(bar_rect, DOWN), self.dots.animate.set_opacity(0.3),
                      Write(pct86), run_time=0.8)
            beat.wait_until("average", offset=-0.1)
            self.play(flag(rows[1]), run_time=0.8)
            beat.wait_until("error", offset=-0.15)
            self.play(Create(err_bar), flag(rows[3]), FadeIn(sd_tag, rate_func=window(0.0, 0.5)),
                      run_time=0.8)
            # "Only thirteen percent showed the points": the bar and its error bar leave (they
            # come back at the landing), so the points alone carry the 13 %. Round 8: the bar,
            # error bar, tag and "86%" are fully gone (0.4 s from "Only") before "13% showed
            # points" starts writing on "showed", so the two label sets never share a frame
            beat.wait_until("Only", offset=-0.05)
            self.play(FadeOut(VGroup(bar_rect, err_bar, sd_tag, pct86)),
                      self.dots.animate.set_opacity(1.0), run_time=0.4)
            beat.wait_until("showed", offset=-0.1)
            self.play(Write(pct13), run_time=max(0.8, beat.until_end_of("points", offset=0.1)))

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
        note = Text("first two decimals, as published", font=SERIF, font_size=27, color=TXT_GRAY)
        note.next_to(self.count, DOWN, buff=0.3).set_x(3.62)
        require_safe(note, "decimals note")

        with self.narrate("How much can five numbers hide? Let's hide a star in them, and "
                          "demand that all five match the dinosaur's to two decimals.", gap=0.66) as beat:
            # the labels beside the strip are gone before the points spread out over them
            self.go(lambda a: lerp(strip, dino, a), 1.3, smooth,
                    FadeOut(cite_w),
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
        with self.narrate("The first version slides every point onto its own spot on a star.",
                          gap=0.66) as beat:
            self.play(self.dots.animate.set_opacity(1.0), run_time=beat.until("slides", offset=-0.1))
            self.go(lambda a: lerp(dino, star0, a), 3.0)

        cen_y = self.cen_y = Dot(ax.c2p(T[0], T[1]), radius=0.09, color=YELLOW).set_z_index(3)
        harm_y = hbar(ax, T[0], T[1], T[2], YELLOW).set_z_index(2)
        varm_y = vbar(ax, T[0], T[1], T[3], YELLOW).set_z_index(2)
        self.cen_r = Dot(ax.c2p(T[0], T[1]), radius=0.09, color=RED).set_z_index(5)
        harm_r = hbar(ax, *s_star0[:3], RED).set_z_index(4)
        varm_r = vbar(ax, s_star0[0], s_star0[1], s_star0[3], RED).set_z_index(4)
        with self.narrate("We got the star, and lost all five numbers. [pause 0.9] The center moved, the x "
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
                          gap=0.75) as beat:
            self.play(self.dots.animate.set_opacity(0.28), run_time=0.45)
            beat.wait_until("averages", offset=-0.1)
            self.play(flag(VGroup(tgts[0], tgts[1])), run_time=0.8)
            beat.wait_until("single", offset=-0.1)
            # one label, flown as one: a copy of "(x-bar, y-bar)" whose x-bar and y-bar sit on the
            # table's symbols (white, table size) and whose brackets and comma wait, invisible, in
            # place. Same string and structure as the target, so each glyph maps onto itself; the
            # two symbols travel on parallel paths that never meet, and the brackets fade in
            xy_src = xy_lbl.copy().set_color(INK)
            for k_, sym_ in ((1, syms[0]), (3, syms[1])):
                xy_src[k_].scale(42 / 38).move_to(sym_)
            for k_ in (0, 2, 4):
                xy_src[k_].set_opacity(0)
            self.add(xy_src)
            self.play(ReplacementTransform(xy_src, xy_lbl), dip(syms[0], syms[1]),
                      FadeIn(xy_patch, rate_func=window(0.55, 0.85)), run_time=1.1)
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
        with self.narrate("The two standard deviations reach out on each side, "
                          "and draw a box.", gap=0.66) as beat:
            beat.wait_until("standard", offset=-0.15)
            self.play(flag(VGroup(tgts[2], tgts[3])),
                      FadeOut(VGroup(xy_lbl, xy_patch), rate_func=window(0.0, 0.6)),
                      run_time=0.8)
            beat.wait_until("reach", offset=-0.15)
            q_sx = MathTex(r"s_x", font_size=42).move_to(syms[2]).set_z_index(7)
            q_sy = MathTex(r"s_y", font_size=42).move_to(syms[3]).set_z_index(7)
            self.play(Succession(
                AnimationGroup(ReplacementTransform(q_sx, c_sx, path_arc=-0.5),   # dips under the arm cap
                               dip(syms[2]), FadeIn(pt_sx, rate_func=window(0.5, 1.0))),
                AnimationGroup(ReplacementTransform(q_sy, c_sy), dip(syms[3]),
                               FadeIn(pt_sy, rate_func=window(0.5, 1.0)))),
                run_time=min(1.2, beat.until("out", offset=-0.25)))
            beat.wait_until("out", offset=-0.2)
            self.play(Create(seg_x), Create(seg_y), run_time=0.6)
            self.play(FadeOut(VGroup(c_sx, pt_sx, c_sy, pt_sy), scale=0.8), run_time=0.4)
            beat.wait_until("draw", offset=-0.1)
            self.play(*[GrowFromCenter(sd) for sd in sides], run_time=0.7)
            self.remove(*sides)
            self.add(box_y)
            self.play(FadeOut(VGroup(seg_x, seg_y, harm_y, varm_y)), run_time=0.5)

        # The correlation: which of the many ellipses that touch all four walls (B9a). Then a
        # "what if" at r = 0.50 (B9b), drawn at 60 % so it never reads as the dinosaur's own
        # summary, while everything that still describes the dinosaur (its "now" column, the =
        # marks, "matching", its own r) steps back to 25 %, so the yellow "r = 0.50" is the only
        # live r on screen. A simulated 142-point cloud with these SDs and r = 0.50 appears. One
        # standard deviation to the right (the run, labelled s_x), the points of the vertical
        # slice at the wall average r s_y up: their copies merge into a NEW white dot at that
        # height, which turns yellow and is the touch dot. The rise (r s_y, its label built from
        # the "r" of "r = 0.50" and the readout's s_y) stands 0.15 right of the wall and the box
        # steps back to a 40 % grey, so the rise, the band and the touch dot never share one
        # column. That is the best-fit line, through the middle of every slice of the ellipse; at
        # the wall a slice shrinks to the touch point. Then r sweeps back to the dinosaur's -0.06:
        # the run, the rise and its label leave, and only the dashed line, the centre and the two
        # touch dots stay.
        now_col = [hdr_n, *self.nows]
        wall_x = T[0] + T[2]
        WOP = 0.6                                            # stroke strength of the what-if
        wop = ValueTracker(1.0)
        R_WI = 0.5                                           # the what-if correlation
        U_ = ax.x_axis.unit_size                             # screen units per data unit
        cen_pt = ax.c2p(T[0], T[1])
        run9 = Line(cen_pt, ax.c2p(wall_x, T[1]), color=YELLOW,
                    stroke_width=4).set_z_index(2).set_stroke(opacity=WOP)
        # under the run's left part: the r = 0.50 ellipse, the centre dot and the dashed line all
        # keep >= 0.15 clear of it there. No backing plate (it clipped the points round it into
        # half-moons): the simulated cloud leaves this spot bare instead (facts #36)
        run9_lbl = MathTex("s_x", font_size=36, color=YELLOW).set_z_index(6)
        run9_lbl.move_to(cen_pt + np.array([0.24, -0.34, 0]))
        ghosts = VGroup(*[ell_mob(ax, (T[0], T[1], T[2], T[3], rg), GRAY, 3)
                          for rg in (0.5, -0.5)]).set_stroke(opacity=0.4)
        RISE_DX = 0.15                                       # the rise stands just right of the wall
        wall_s = ax.c2p(wall_x, T[1])[0]
        rise_x = wall_s + RISE_DX
        y_c = ax.c2p(0, T[1])[1]
        y_t = ax.c2p(0, T[1] + R_WI * T[3])[1]
        touchR = ax.c2p(wall_x, T[1] + R_WI * T[3])
        touchL = ax.c2p(T[0] - T[2], T[1] - R_WI * T[3])
        # a dimension: the rise itself, with thin extension ticks back to the run's end and to
        # the touch point, so it measures that height without sitting on the wall
        rise9 = VGroup(Line([rise_x, y_c, 0], [rise_x, y_t, 0], stroke_width=6),
                       Line([wall_s, y_c, 0], [rise_x + 0.02, y_c, 0], stroke_width=2.5),
                       Line([wall_s, y_t, 0], [rise_x + 0.02, y_t, 0], stroke_width=2.5))
        rise9.set_stroke(YELLOW, opacity=WOP).set_z_index(3)
        rs_lbl = MathTex("r", r"\,s_y", font_size=36, color=YELLOW).set_z_index(6)
        rs_lbl.move_to([rise_x + 0.22 + rs_lbl.width / 2, ax.c2p(0, T[1] + R_WI * T[3] / 2)[1], 0])
        BFL_EXT = 1.05                                       # just past both touch dots

        def bfl_line(r):
            """best-fit line y - y_bar = r s_y/s_x (x - x_bar), through both touch dots"""
            return DashedLine(ax.c2p(T[0] - BFL_EXT * T[2], T[1] - BFL_EXT * r * T[3]),
                              ax.c2p(T[0] + BFL_EXT * T[2], T[1] + BFL_EXT * r * T[3]),
                              color=YELLOW, stroke_width=3, dash_length=0.12,
                              dashed_ratio=0.6).set_z_index(2)
        bfl = bfl_line(R_WI).set_stroke(opacity=WOP)
        KS = (-0.8, -0.4, 0.0, 0.4, 0.8)                     # slice positions, in units of s_x
        qv = ValueTracker(0.0)                               # 0: spread out, 1: all at the wall

        def chord_pts(k, r):
            """vertical slice of the 1-SD ellipse at x = x_bar + k s_x: ends and midpoint"""
            h = T[3] * np.sqrt(1 - r * r) * np.sqrt(max(0.0, 1 - k * k))
            c = T[1] + r * k * T[3]
            x = T[0] + k * T[2]
            return ax.c2p(x, c - h), ax.c2p(x, c + h), ax.c2p(x, c)
        chords = VGroup(*[Line(*chord_pts(k, R_WI)[:2]) for k in KS]).set_stroke(
            YELLOW, 2.5, opacity=0.6).set_z_index(2)
        mids = VGroup(*[Dot(chord_pts(k, R_WI)[2], radius=0.065, color=YELLOW).set_z_index(4)
                        for k in KS]).set_fill(opacity=WOP)

        def upd_chords(m):
            q = qv.get_value()
            for ln, d, k in zip(chords, mids, KS):
                lo, hi, mid = chord_pts(min(k + (1 - k) * q, 0.9995), R_WI)
                ln.put_start_and_end_on(lo, hi)
                d.move_to(mid)

        # the what-if's own readout, top left of the plot (where the r = 0.50 cloud never goes)
        sim_tag = label("simulated", color=TXT_GRAY).next_to(ax.c2p(3, 100), DR, buff=0.0)
        sim_tag.shift(DOWN * 0.05)
        r_live = VGroup(MathTex(r"r =", font_size=36, color=YELLOW),
                        DecimalNumber(float(T[4]), num_decimal_places=2, font_size=36,
                                      color=YELLOW)).arrange(RIGHT, buff=0.12).set_z_index(5)
        r_live.next_to(sim_tag, DOWN, buff=0.2, aligned_edge=LEFT)

        def upd_live(m):
            m[1].set_value(rt.get_value())
            m[1].next_to(m[0], RIGHT, buff=0.12)

        # the simulated cloud (labelled): uniform inside the 2-SD ellipse, then given exactly the
        # dinosaur's means and SDs and r = 0.50, so this ellipse is its 1-SD ellipse and the
        # dashed line is its least-squares line. The two labels written over it and the what-if
        # readout sit on bare background: points that would land under them (or outside the
        # plot) are drawn again (seed chosen so the slice at the wall averages on the line)
        def zone(m, pad=MIN_GAP + 0.055):                    # label box + clearance + dot radius
            c = ax.p2c(m.get_center())
            return (c[0], c[1], (m.width / 2 + pad) / U_, (m.height / 2 + pad) / U_)
        T_wi = np.array([T[0], T[1], T[2], T[3], R_WI])
        # round 8: nor between the wall and the rise (the dimension's own rectangle, from the
        # wall to the rise plus 0.1, from y-bar to the touch height plus 0.1, plus a dot radius),
        # so no simulated point sits inside the measurement the viewer is reading
        rz_pad = (0.1 + 0.055) / U_
        rz_x0, rz_x1 = wall_x, wall_x + (RISE_DX + 0.1 + 0.055) / U_
        rz_y0, rz_y1 = T[1] - rz_pad, T[1] + R_WI * T[3] + rz_pad
        rise_zone = ((rz_x0 + rz_x1) / 2, (rz_y0 + rz_y1) / 2, (rz_x1 - rz_x0) / 2,
                     (rz_y1 - rz_y0) / 2)
        sim, n_redrawn = sim_cloud(SIM_SEED, T_wi,
                                   [zone(run9_lbl), zone(rs_lbl), zone(VGroup(sim_tag, r_live)),
                                    rise_zone])
        assert np.allclose(stats(sim), T_wi) and sim.min() > 0.5 and sim.max() < 99.5
        assert n_redrawn <= 12, n_redrawn
        sim_dots = VGroup(*[Dot(p, radius=0.055, color=GRAY) for p in to_screen(ax, sim)])
        band = np.abs(sim[:, 0] - wall_x) < 0.12 * T[2]      # the vertical slice at the wall
        band_y = float(sim[band, 1].mean())
        assert band.sum() >= 8 and abs(band_y - (T[1] + R_WI * T[3])) < 0.1
        # the averaged dot lands on bare wall: no band point within 0.15 of its edge
        band_scr = to_screen(ax, sim[band])
        assert np.min(np.linalg.norm(band_scr - ax.c2p(wall_x, band_y), axis=1)) > 0.075 + 0.055 + 0.07
        band_dots = VGroup(*[sim_dots[i] for i in np.where(band)[0]])
        rest_dots = VGroup(*[sim_dots[i] for i in np.where(~band)[0]])
        band_rect = Rectangle(width=2 * 0.12 * T[2] * ax.x_axis.unit_size,
                              height=100 * ax.y_axis.unit_size, stroke_width=0,
                              fill_color=GRAY, fill_opacity=0.14).move_to(ax.c2p(wall_x, 50))
        band_rect.set_z_index(-1)                            # behind the points it singles out
        band_avg = ax.c2p(wall_x, band_y)
        everything = VGroup(*syms, *eqs, *tgts, *self.nows)
        touch_dot = Dot(touchR, radius=0.075)
        require_clear(VGroup(sim_tag, r_live), sim_dots, chords, mids, box_mob(ax, T),
                      what="what-if labels vs the simulated cloud")
        require_safe(VGroup(sim_tag, r_live), "what-if labels")
        for lab_, nm_ in ((run9_lbl, "B9 s_x label"), (rs_lbl, "B9 r s_y label")):
            require_clear(lab_, ell_mob(ax, T_wi), box_mob(ax, T), cen_y, run9, rise9,
                          bfl_line(R_WI), touch_dot, sim_dots, everything, what=nm_)
        require_clear(run9_lbl, rs_lbl, what="s_x vs r s_y")
        for r_chk in (float(T[4]), 0.25, R_WI):              # the what-if readout during the sweep
            s_chk = (T[0], T[1], T[2], T[3], r_chk)
            require_clear(VGroup(sim_tag, r_live), ell_mob(ax, s_chk), bfl_line(r_chk),
                          what=f"what-if labels at r={r_chk:.2f}")

        # slope = r s_y / s_x (round 8, substance fix 3): built in the insight beat, on "That's
        # the best-fit line", its numerator from the rise's label and its denominator from the
        # run's, in the open band under the readout (P1, where "matching" sits; it steps out
        # for the what-if). It then parks under "matching", small and grey (P2), and moves up
        # to the top right of Anscombe's frame (F3), where "Same rule" lights it again
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
        numC = MathTex("r", r"\,s_y", font_size=FS, color=YELLOW)
        denC = MathTex("s_x", font_size=FS, color=YELLOW)
        barC = frac(numC, denC)
        F3 = VGroup(f_lhs, numC, barC, denC)                 # Anscombe's frame, top right
        require_safe(F3, "slope = r s_y / s_x")
        P1_BAR_Y = -2.1
        f1 = F3.copy().shift([1.0 - f_lhs.get_left()[0], P1_BAR_Y - barC.get_y(), 0])
        lhs1, num1, bar1, den1 = f1
        F2 = f1.copy().scale(0.65)
        F2.shift([1.0 - F2.get_left()[0], -2.32 - F2.get_top()[1], 0])
        F2.set_color(TXT_GRAY).set_opacity(0.5)
        F3_dim = F3.copy().set_color(TXT_GRAY).set_opacity(0.5)
        require_safe(f1, "B9 slope")
        require_safe(F2, "parked slope")
        require_clear(f1, everything, hdr_n, gap=0.2, what="B9 slope vs readout")
        require_clear(f1, ax, what="B9 slope vs the plot")
        require_clear(F2, self.count, everything, ax, what="parked slope vs 'matching'")
        assert f1.get_left()[0] - ax.x_name.get_right()[0] >= 0.75, "B9 slope too near 'x'"

        with self.narrate("Many ellipses touch all four walls. [pause 0.2] The correlation, r, "
                          "picks one. [pause 0.6]", gap=0.66) as beat:
            beat.wait_until("Many", offset=-0.1)
            self.play(LaggedStart(*[Create(g) for g in ghosts], lag_ratio=0.35), run_time=0.9)
            beat.wait_until("walls", offset=-0.2)
            self.play(Indicate(box_y, color=YELLOW, scale_factor=1.04), run_time=0.8)
            beat.wait_until("correlation", offset=-0.1)
            self.play(flag(VGroup(syms[4], tgts[4])), run_time=0.7)
            beat.wait_until("picks", offset=-0.15)
            # the ellipse is drawn from its right touch point round to the left one: each touch
            # dot appears as the stroke reaches its wall (no glyph-to-dot morph across the table)
            self.play(FadeOut(ghosts), Create(self.ell),
                      FadeIn(tR, scale=0.4, rate_func=window(0.0, 0.2)),
                      FadeIn(tL, scale=0.4, rate_func=window(0.45, 0.65)), run_time=1.0)

        def sweep(m):
            s = (T[0], T[1], T[2], T[3], rt.get_value())
            m.become(ell_mob(ax, s).set_z_index(2))
            m.set_stroke(opacity=wop.get_value())

        def touch_upd(sign):
            def f(m):
                m.move_to(ax.c2p(T[0] + sign * T[2], T[1] + sign * rt.get_value() * T[3]))
                m.set_fill(opacity=wop.get_value())
            return f

        def dim_dino():
            """the dinosaur's live column, marks and own r step back to 25 % (green and yellow go
            grey first: dimmed further than 60 % they read as olive / moss); "matching" steps
            out altogether, so the slope formula can be built in its band"""
            return [*[m.animate.set_opacity(0.25) for m in now_col],
                    *[m.animate.set_color(TXT_GRAY).set_opacity(0.25) for m in self.marks],
                    self.count[0].animate.set_opacity(0), self.count[2].animate.set_opacity(0),
                    self.count.number.animate.set_color(TXT_GRAY).set_opacity(0),
                    syms[4].animate.set_opacity(0.25), eqs[4].animate.set_opacity(0.25),
                    tgts[4].animate.set_color(TXT_GRAY).set_opacity(0.25)]

        def undim_dino():
            return [*[m.animate.set_opacity(1.0) for m in now_col],
                    *[m.animate.set_color(GREEN).set_opacity(1.0) for m in self.marks],
                    syms[4].animate.set_opacity(1.0), eqs[4].animate.set_opacity(1.0),
                    tgts[4].animate.set_color(YELLOW).set_opacity(1.0)]

        def count_back():
            return [self.count[0].animate.set_opacity(1.0), self.count[2].animate.set_opacity(1.0),
                    self.count.number.animate.set_color(GREEN).set_opacity(1.0)]

        LANE_X = 0.85                                        # the flights' lane, between plot and table
        with self.narrate("This one barely tilts. [pause 0.4] Say r is point five. Go one standard deviation "
                          "right. [pause 0.4] On average, the cloud rises r times ess why. "
                          "[pause 0.7] That's the best-fit line, [pause 1.1] through the middle of "
                          "every slice of the ellipse. [pause 0.7] At the wall, the slices shrink to "
                          "the touch point. [pause 0.4] For the dinosaur, it's just below the middle.",
                          gap=0.66, speed=0.80) as beat:
            r_live.add_updater(upd_live)
            # "This one barely tilts" (round 8: the what-if has its reason): the dinosaur's own
            # ellipse pulses and its touch dots, nearly level with the centre, flag
            beat.on("This one", self.ell.animate(rate_func=there_and_back).set_stroke(width=8),
                    flag(tR), flag(tL), lead=0.15, run_time=0.8)
            self.ell.add_updater(sweep)
            beat.wait_until("Say", offset=-0.1)
            # the what-if: the dinosaur steps aside, its live column and its r step back,
            # "matching" steps out, the box steps back to a grey 40 %, the touch dots go (the
            # slice will find the right one), and the geometry drops to 60 % (yellow dimmed
            # further reads olive)
            self.play(self.dots.animate.set_opacity(0), *dim_dino(),
                      box_y.animate.set_stroke(GRAY, opacity=0.4),
                      FadeOut(tR, scale=0.5), FadeOut(tL, scale=0.5),
                      FadeIn(r_live), FadeIn(sim_tag), wop.animate.set_value(WOP), run_time=0.5)
            self.play(rt.animate.set_value(R_WI),
                      FadeIn(sim_dots, rate_func=window(0.35, 1.0)),
                      run_time=beat.until_end_of("five", offset=0.15))
            tR.move_to(touchR).set_fill(opacity=WOP)
            tL.move_to(touchL).set_fill(opacity=WOP)
            beat.wait_until("one standard", offset=-0.1)
            self.play(Create(run9), Write(run9_lbl), run_time=beat.until_end_of("right"))
            # "on average": the slice at the wall, its points singled out in white ...
            beat.wait_until("average", offset=-0.25)
            self.play(FadeIn(band_rect), band_dots.animate.set_color(INK),
                      rest_dots.animate.set_opacity(0.3), run_time=0.5)
            # ... and averaged: copies converge on their mean while the rise grows beside the wall
            avg_cp = VGroup(*[d.copy().set_z_index(4) for d in band_dots])
            self.add(avg_cp)
            T_c = max(0.9, beat.until("r times", offset=-0.35))
            t_rise = min(0.5, max(0.0, beat.until("rises", offset=-0.15) / T_c))
            self.play(*[c.animate.move_to(band_avg).scale(0.075 / 0.055) for c in avg_cp],
                      Create(rise9, rate_func=window(t_rise, 1.0)), run_time=T_c)
            merged = Dot(band_avg, radius=0.075, color=INK).set_z_index(4)
            self.remove(*avg_cp)
            self.add(merged)
            # "r times ess why": the rise's label, its r from the what-if's "r = 0.50" and its s_y
            # from the readout (each source steps back while its copy leaves)
            beat.wait_until("r times", offset=-0.3)
            T_l = max(1.2, beat.until_end_of("why", offset=0.1))
            t_s = min(0.5, max(0.3, beat.until("ess", offset=-0.25) / T_l))
            r_glyph = r_live[0][0][0]
            cp_r = MathTex("r", font_size=36, color=YELLOW).move_to(r_glyph)
            cp_s = MathTex(r"\,s_y", font_size=42).move_to(syms[3])[0]
            self.play(ReplacementTransform(cp_r, rs_lbl[0], rate_func=window(0.0, t_s + 0.1)),
                      ReplacementTransform(cp_s, rs_lbl[1], rate_func=window(t_s, 1.0)),
                      dip(r_glyph, lo=0.0, back=t_s + 0.05), dip(syms[3], lo=0.0, start=t_s, back=0.9),
                      run_time=T_l)
            self.remove(rs_lbl[0], rs_lbl[1])
            self.add(rs_lbl)
            # in the pause: the averaged point turns yellow and is the touch dot; the 14 points it
            # averages step back to 40 % (round 8: they stayed full white beside the rise)
            self.play(merged.animate.set_color(YELLOW).set_opacity(WOP).move_to(touchR),
                      band_dots.animate.set_opacity(0.4), run_time=0.5)
            self.remove(merged)
            self.add(tR)
            # "That's the best-fit line": the cloud leaves and the dashed line grows from the
            # centre through the touch dot to the left one. In the pause the slope is assembled
            # from the two labels (round 8, substance fix 3): the run's s_x itself drops into the
            # denominator, a copy of the rise's r s_y into the numerator (the rise's own label is
            # hidden while its copy leaves it, so it never reads doubled), each down the lane
            # between the plot and the readout and in under the readout's last row; then the bar
            # and "slope =". The run is then unlabelled, so no slice crosses a label
            beat.wait_until("best-fit", offset=-0.3)
            T_f = max(2.1, beat.until("through", offset=-0.1))
            cp_rs = rs_lbl.copy()
            self.play(FadeOut(sim_dots, rate_func=window(0.0, 0.3)),
                      FadeOut(band_rect, rate_func=window(0.0, 0.3)),
                      FadeOut(sim_tag, rate_func=window(0.0, 0.3)),
                      GrowFromCenter(bfl, rate_func=window(0.0, 0.4)),
                      FadeIn(tL, scale=0.4, rate_func=window(0.28, 0.4)),
                      ReplacementTransform(run9_lbl, den1, rate_func=window(0.3, 0.66),
                                           path_func=elbow_path(run9_lbl, den1, LANE_X)),
                      ReplacementTransform(cp_rs, num1, rate_func=window(0.5, 0.86),
                                           path_func=elbow_path(cp_rs, num1, LANE_X)),
                      dip(rs_lbl, lo=0.0, out=0.02, start=0.5, back=0.78),
                      Create(bar1, rate_func=window(0.74, 0.92)),
                      # (Write applies its rate per glyph after its lag, so a window would start
                      # the first letters early: wait explicitly instead)
                      Succession(Wait(run_time=0.8), Write(lhs1, run_time=0.2)),
                      run_time=T_f)
            self.remove(lhs1, num1, bar1, den1)
            self.add(f1)
            # "through the middle of every slice of the ellipse": each slice's midpoint lands on
            # the dashed line
            beat.wait_until("middle", offset=-0.3)
            self.play(LaggedStart(*[AnimationGroup(Create(c), FadeIn(d, scale=0.4,
                                                                    rate_func=window(0.5, 1.0)))
                                    for c, d in zip(chords, mids)], lag_ratio=0.2),
                      run_time=max(1.3, beat.until_end_of("ellipse") - 0.1))
            # at the wall a slice is a single point: every slice slides there and collapses,
            # and the box comes back at full strength
            beat.wait_until("the wall", offset=-0.1)
            self.play(qv.animate.set_value(1.0), UpdateFromFunc(chords, upd_chords),
                      box_y.animate.set_stroke(YELLOW, opacity=1.0),
                      run_time=beat.until("touch point", offset=-0.15), rate_func=smooth)
            self.play(FadeOut(chords), FadeOut(mids), flag(tR), flag(rs_lbl), run_time=0.7)
            # back to the data. Round 8: the run, the rise and its label leave first (0.4 s),
            # so no dimension ever measures an r it no longer shows; then r sweeps back to the
            # dinosaur's -0.06 and the geometry is the dinosaur's again (full strength): only the
            # dashed line, the centre and the two touch dots stay
            self.play(FadeOut(VGroup(run9, rise9, rs_lbl)), run_time=0.4)
            beat.wait_until("dinosaur", offset=-0.25)
            tR.add_updater(touch_upd(1))
            tL.add_updater(touch_upd(-1))
            bfl.add_updater(lambda m: m.become(bfl_line(rt.get_value())).set_stroke(
                opacity=wop.get_value()))
            # (the "r = …" readout is driven explicitly: the dip on its r glyph broke the group
            # apart in the scene, so its own updater no longer runs)
            self.play(rt.animate.set_value(float(T[4])), wop.animate.set_value(1.0),
                      UpdateFromFunc(r_live, upd_live), run_time=0.9, rate_func=smooth)
            for m in (self.ell, tR, tL, r_live, bfl):
                m.clear_updaters()
            self.play(FadeOut(r_live), *undim_dino(), run_time=0.45)
            # the touch dot and the dinosaur's own r, each value flagged on its own (a group
            # Indicate would push 0.06 into its "=")
            beat.wait_until("middle", occurrence=2, offset=-0.3)
            self.play(flag(tR), LaggedStart(flag(tgts[4]), flag(self.nows[4]), lag_ratio=0.25),
                      run_time=0.8)

        with self.narrate("That ellipse is everything the five numbers know. [pause 1.0]") as beat:
            beat.wait_until("ellipse", offset=-0.15)
            self.play(FadeOut(bfl),
                      self.ell.animate(rate_func=there_and_back).set_stroke(width=8),
                      run_time=0.8)
            # the dinosaur returns, and the formula steps back, small and grey, under the band
            # where "matching" returns (it is carried to Anscombe's frame later)
            beat.wait_until("everything", offset=-0.1)
            self.play(self.dots.animate.set_opacity(1.0), Transform(f1, F2), run_time=0.8)
            beat.wait_until("five", offset=-0.1)
            self.play(LaggedStart(*[flag(t) for t in tgts], lag_ratio=0.1), *count_back(),
                      run_time=1.1)

        # replay version one, now watching the ellipse
        self.cen_r = Dot(cen_y.get_center(), radius=0.09, color=RED).set_z_index(1)
        self.box_r = box_mob(ax, T, RED).set_z_index(1)
        self.ell_r = ell_mob(ax, T, RED, 4).set_z_index(1)
        red = VGroup(self.cen_r, self.box_r, self.ell_r)
        with self.narrate("Now replay the first version, and watch the ellipse.", gap=0.75) as beat:
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
        with self.narrate("How would you fix it? [pause 1.5]") as beat:
            self.play(UpdateFromAlphaFunc(box_y, set_box_op), self.dots.animate.set_opacity(0.4),
                      run_time=0.6)

        with self.narrate("Slide it until the centers meet. Stretch it until the boxes match. "
                          "Then tip it, keeping the box, [pause 0.2] until it touches the walls at the same "
                          "height.", gap=0.66) as beat:
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

        with self.narrate("All five match now, to every decimal place. [pause 0.6]", gap=0.6) as beat:
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
        # built from "=" and then shown as the sign: become() keeps the original's height as
        # its font size, so a mark built from the taller "≠" would measure tiny as "="
        self.med_mark = self.med_eq.copy().become(self.med_neq)
        med_row = VGroup(
            MathTex(r"\mathrm{med}\,y", font_size=42).move_to([X_SYM_R, MED_Y, 0],
                                                             aligned_edge=RIGHT),
            MathTex("=", font_size=42).move_to([X_EQ, MED_Y, 0]),
            MathTex(f"{t2(self.med_t):.2f}", font_size=42, color=YELLOW).move_to(
                [X_TGT_L, MED_Y, 0], aligned_edge=LEFT),
            self.med_now, self.med_mark)
        require_clear(F2, med_row, what="parked slope vs the median row")
        with self.narrate("But add a sixth number: the median of y. Our star misses it by "
                          "six.", gap=0.75) as beat:
            beat.wait_until("sixth", offset=-0.15)
            self.play(FadeOut(self.count), run_time=0.5)       # in place: the parked slope is below
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
        order = ["bullseye", "x_shape", "h_lines"]           # round 8: our own star is not re-shown
        for name in order:
            cur = match(cur, D[name])
            seq[name] = cur
        five_cols = VGroup(*[VGroup(syms[i], eqs[i], tgts[i], self.nows[i], self.marks[i])
                             for i in range(5)])
        hl5 = box(five_cols, color=YELLOW, buff=0.14)
        require_clear(hl5, hdr_t, hdr_n, med_row, what="'these five' box")
        self.live = self.med_live = True
        circ_line = DashedVMobject(Circle(radius=circ_R * ax.x_axis.unit_size, color=GRAY,
                                          stroke_width=2.5).move_to(ax.c2p(*circ_c)),
                                   num_dashes=48, dashed_ratio=0.55)
        # the search, shown rather than described: the target is drawn on "nudges" and the
        # points set off one by one toward it while the five numbers never change
        with self.narrate("In 2017, Justin Matejka and George Fitzmaurice built a search. [pause 0.4] It "
                          "keeps these five numbers fixed while it nudges points toward a "
                          "target.", gap=0.66) as beat:
            beat.wait_until("Matejka", offset=-0.3)
            self.play(FadeIn(cite_mf), run_time=0.6)
            self.geo_live = True
            # our star walks back to the dinosaur with the five held
            self.go(self.path_fixed(fixed_star, dino), beat.until("these", offset=-0.15))
            # "these five numbers": a box round the five rows (as for Anscombe's), not a scale
            # flash, which would push each value into its "="
            self.play(Create(hl5), run_time=0.6)
            beat.wait_until("nudges", offset=-0.35)
            self.play(Create(circ_line), FadeOut(hl5), run_time=0.6)
            self.go(self.path_nudge(dino, seq["circle"]),
                    max(1.6, beat.remaining()), rate_func=linear)

        names = ["circle"] + order
        with self.narrate("From the dinosaur they grew twelve shapes: this circle, [pause 0.8] "
                          "this bullseye, [pause 0.8] this X, [pause 0.8] and these stripes. Each "
                          "one has this same ellipse, and a different median.", gap=0.72) as beat:
            beat.on("this circle", FadeOut(circ_line), Indicate(self.dots, color=BLUE,
                                                                scale_factor=1.04), lead=0.3,
                    run_time=0.8)
            for (prev, nxt), word in zip(zip(names[:-1], names[1:]),
                                         ["bullseye", "X", "stripes"]):
                beat.wait_until(word, offset=-0.7)          # lands 0.2 s before its noun
                self.go(self.path_fixed(seq[prev], seq[nxt]), 0.5)
            beat.wait_until("Each", offset=-0.1)
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
            for i in keep:
                d = self.dots[i]
                d.move_to(lerp(start[i], dest[i], a))
                d.set(width=2 * (0.055 + 0.025 * a))
        ell_a = ell_mob(ax2, TA).set_z_index(2)
        box_a = box_mob(ax2, TA).set_z_index(2)
        cen_a = Dot(ax2.c2p(xa, ya), radius=0.09, color=YELLOW).set_z_index(3)
        tch_a = Dot(ax2.c2p(xa + sxa, ya + ra * sya), radius=0.09, color=YELLOW).set_z_index(3)
        tchL_a = Dot(ax2.c2p(xa - sxa, ya - ra * sya), radius=0.075, color=YELLOW).set_z_index(3)
        old_nums = VGroup(ax.x_axis.numbers, ax.y_axis.numbers, ax.x_axis.ticks, ax.y_axis.ticks)
        new_nums = VGroup(ax2.x_axis.numbers, ax2.y_axis.numbers, ax2.x_axis.ticks,
                          ax2.y_axis.ticks)
        new_nums.set_opacity(0)

        # Anscombe's own readout (ordinary rounding, as his numbers are always quoted). It builds
        # in its final bottom-right slot, r first (round 7: it used to land mid-right and then
        # jump down to make room for the slope formula, a move that meant nothing)
        an_vals = [f"{xa:.2f}", f"{ya:.2f}", f"{sxa:.2f}", f"{sya:.2f}", f"{ra:.2f}"]
        an = [item(s, v) for s, v in zip((r"\bar{x}", r"\bar{y}", "s_x", "s_y", "r"), an_vals)]
        GAP = 0.45
        # the two rows straddle the centre line (y-bar), so neither right-hand quadrant sits empty
        # while his points are introduced (it used to sit level with the touch point, leaving the
        # lower right empty for ~16 s); r is the top row's left-most entry, so its 0.82 still
        # rises straight out of the table on its way to the touch dot
        RA_MID_TOUCH = tch_a.get_center()[1]
        RA_MID = cen_a.get_center()[1] + 0.35
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
        readout_a.shift(LOW)
        readout_low = readout_a
        require_safe(readout_a, "Anscombe readout")

        # geometry on Anscombe I: derive the best-fit slope from the box
        slope = ra * sya / sxa
        line_a = Line(ax2.c2p(AN_X[0] + 0.5, ya + slope * (AN_X[0] + 0.5 - xa)),
                      ax2.c2p(AN_X[1] - 0.5, ya + slope * (AN_X[1] - 0.5 - xa)),
                      color=YELLOW, stroke_width=4).set_z_index(2)
        run_seg = Line(ax2.c2p(xa, ya), ax2.c2p(xa + sxa, ya), color=YELLOW,
                       stroke_width=6).set_z_index(3)
        rise_seg = Line(ax2.c2p(xa + sxa, ya), ax2.c2p(xa + sxa, ya + ra * sya), color=YELLOW,
                        stroke_width=6).set_z_index(3)
        dots_a_final = VGroup(*[Dot(p, radius=0.08) for p in scr_a])
        require_clear(readout_a, ell_a, box_a, tch_a, dots_a_final, line_a, ax2,
                      what="readout vs plot")

        # (slope = r s_y / s_x, F3, is defined with the insight beat, where it is built)
        require_clear(VGroup(f_lhs, numC, denC, barC), readout_low, what="slope vs readout")

        with self.narrate("In 1973, Francis Anscombe did it with just eleven points. [pause 1.2]",
                          gap=0.66) as beat:
            self.add(ax2)                    # same frame, axis lines and names as ax
            # Round 8: no axis number ever labels data it does not describe.
            # 1. Everything that belongs only to the dinosaur leaves first: the sixth number, its
            # readout, its citation and the 131 points that will not travel. The 11 that will,
            # and the dinosaur's ellipse and box, still sit on the 0-100 axes they belong to
            dino_tab = VGroup(hdr_t, hdr_n, *syms, *eqs, *tgts, *self.nows, *self.marks)
            others = VGroup(*[d for i, d in enumerate(self.dots) if i not in keep])
            self.remove(self.dots)
            self.add(others, dots_a)
            self.play(FadeOut(med_row), FadeOut(dino_tab), FadeOut(cite_mf), FadeOut(others),
                      run_time=0.5)
            # 2. Then the tick numbers, the 11 points, the ellipse, box, centre and touch dots all
            # change together, on one smooth rate function, while the parked slope moves up to
            # the top right (still grey) through the now empty right half. Where an old and a new
            # number would share a spot (x: 75 and 12) the old one is out before the new one comes
            # in, so no two numbers ever overprint. It follows step 1 at once (on "1973")
            T_m = 1.2
            olds = list(ax.x_axis.numbers) + list(ax.y_axis.numbers)
            news = list(ax2.x_axis.numbers) + list(ax2.y_axis.numbers)

            def clash(m_, others_):
                return any(abs(m_.get_x() - o_.get_x()) < (m_.width + o_.width) / 2 + 0.1 and
                           abs(m_.get_y() - o_.get_y()) < (m_.height + o_.height) / 2 + 0.1
                           for o_ in others_)
            seq_ids = {id(m_) for m_ in olds if clash(m_, news)} | \
                      {id(m_) for m_ in news if clash(m_, olds)}
            old_ticks = VGroup(ax.x_axis.ticks, ax.y_axis.ticks)
            new_ticks = VGroup(ax2.x_axis.ticks, ax2.y_axis.ticks)

            def ticks_over(m_, a):                        # a is already smoothed (same as the data)
                h1, h2 = min(1.0, 2 * a), max(0.0, 2 * a - 1)
                for o_ in olds:
                    o_.set_opacity(1 - (h1 if id(o_) in seq_ids else a))
                for n_ in news:
                    n_.set_opacity(h2 if id(n_) in seq_ids else a)
                old_ticks.set_opacity(1 - a)
                new_ticks.set_opacity(a)
            self.play(UpdateFromAlphaFunc(ax, ticks_over, rate_func=smooth),
                      UpdateFromAlphaFunc(dots_a, to_anscombe, rate_func=smooth),
                      Transform(self.ell, ell_a), Transform(box_y, box_a), Transform(cen_y, cen_a),
                      Transform(tR, tch_a), Transform(tL, tchL_a),
                      Transform(f1, F3_dim), run_time=T_m)
            self.remove(ax)
            # 3. His readout builds in its bottom-right slot, entry by entry (r first: no "r ="
            # ever waits without its value), and his citation comes in as his points settle
            T_r = max(0.8, beat.until("points", offset=-0.15))
            self.play(LaggedStart(*[FadeIn(an[i], shift=0.1 * UP) for i in (4, 2, 3, 0, 1)],
                                  lag_ratio=0.15),
                      FadeIn(cite_an, rate_func=window(0.3, 1.0)), run_time=T_r)
            beat.wait_until("points", offset=-0.1)
            # his eleven points flagged on "points"
            self.play(LaggedStart(*[Indicate(d, color=BLUE, scale_factor=1.6) for d in dots_a],
                                  lag_ratio=0.06), run_time=0.8)
            # in the pause: his r rises out of its row and travels, intact, to the touch dot it
            # sets (up out of its row first, never across "r ="; the source hides meanwhile)
            c82 = an[4][2].copy()
            d82 = c82.copy().next_to(tR, RIGHT, buff=0.3)
            self.play(ReplacementTransform(c82, d82, path_func=lift_path(c82, d82, 1.0, (0.6, 0.0))),
                      dip(an[4][2], lo=0.0, back=0.8), run_time=0.75)
            self.play(flag(tR), run_time=0.55)

        # "Same rule, same line." (round 8: B9b's rule is not taught again; the formula built
        # there lights up, the run and the rise it names are drawn, and the line grows through
        # the touch point the 0.82 set)
        with self.narrate("Same rule, [pause 0.3] same line. [pause 0.8]") as beat:
            beat.wait_until("Same", offset=-0.15)
            self.play(FadeOut(d82, target_position=tR.get_center(), scale=0.3,
                              rate_func=window(0.0, 0.4)),
                      Transform(f1, F3, rate_func=window(0.0, 0.5)),
                      Create(run_seg, rate_func=window(0.3, 0.62)),
                      Create(rise_seg, rate_func=window(0.62, 0.95)), run_time=1.2)
            beat.wait_until("line", offset=-0.3)
            self.play(GrowFromPoint(line_a, cen_y.get_center()), run_time=0.9)

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
        top_f1 = F3.copy().scale(0.85)
        top_row = VGroup(top_f1).move_to([0, 3.0, 0])
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

        hl_read = box(readout_q, color=YELLOW, buff=0.15)

        def shrink(m, a):
            for d, s0_, d1 in zip(dots_a, start1, dest1):
                d.move_to(lerp(s0_, d1, a))
                d.set(width=2 * (0.08 - 0.02 * a))

        with self.narrate("All four of his datasets share these five numbers. [pause 0.5] A "
                          "trend, a curve, an outlier, and one point doing all the work.") as beat:
            # "All four": Anscombe I's axis lines and ticks transform into panel I's, on the same
            # smooth rate function as his points, ellipse and line, so the points never leave
            # their axes and no second set of axes ghosts under the panel (round 8). Each old
            # tick number rides to where its value sits on the new axis while it fades out; each
            # new one rides in from where its value sat on the old axis and fades in late, so two
            # numbers never overprint. The "y" travels; the other three panels arrive meanwhile
            p0 = panels[0]
            a2x, a2y = ax2.x_axis.copy(), ax2.y_axis.copy()
            a2x.remove(a2x.numbers)
            a2y.remove(a2y.numbers)
            p0x, p0y = p0.x_axis.copy(), p0.y_axis.copy()
            p0x.remove(p0x.numbers)
            p0y.remove(p0y.numbers)
            old_n = VGroup(*ax2.x_axis.numbers, *ax2.y_axis.numbers)
            new_n = VGroup(*p0.x_axis.numbers, *p0.y_axis.numbers)
            rides = []
            for A_s, A_d in ((ax2.x_axis, p0.x_axis), (ax2.y_axis, p0.y_axis)):
                o_s = A_s.numbers[0].get_center() - A_s.n2p(A_s.numbers[0].get_value())
                o_d = A_d.numbers[0].get_center() - A_d.n2p(A_d.numbers[0].get_value())
                for num in A_s.numbers:
                    rides.append((num, num.get_center().copy(),
                                  A_d.n2p(num.get_value()) + o_d, True))
                for num in A_d.numbers:
                    rides.append((num, A_s.n2p(num.get_value()) + o_s,
                                  num.get_center().copy(), False))

            def ride(m, a):                                   # a: smoothed, as for the data
                for num, q0, q1, out in rides:
                    num.move_to(q0 + (q1 - q0) * a)
                    num.set_opacity(1 - min(1.0, a / 0.35) if out else
                                    min(1.0, max(0.0, (a - 0.6) / 0.4)))
            ax2_x_name, ax2_y_name = ax2.x_name, ax2.y_name
            self.remove(ax2)
            self.add(a2x, a2y, old_n, new_n, ax2_x_name, ax2_y_name)
            new_n.set_opacity(0)
            self.bring_to_front(dots_a)
            T_q = max(1.3, beat.until("share", offset=-0.1))
            self.play(FadeOut(VGroup(box_y, tR, tL, run_seg, rise_seg), rate_func=window(0.0, 0.3)),
                      FadeOut(cen_y, rate_func=window(0.0, 0.5)),
                      ReplacementTransform(a2x, p0x), ReplacementTransform(a2y, p0y),
                      UpdateFromAlphaFunc(VGroup(old_n, new_n), ride, rate_func=smooth),
                      ReplacementTransform(ax2_y_name, p_yt),
                      FadeOut(ax2_x_name, rate_func=window(0.0, 0.3)),
                      UpdateFromAlphaFunc(dots_a, shrink, rate_func=smooth),
                      Transform(self.ell, pells[0]), Transform(line_a, plines[0]),
                      Transform(f1, top_f1),
                      readout_a.animate.shift(Q_SHIFT),
                      *[FadeIn(VGroup(panels[jj], pdots[jj]),
                               rate_func=window(0.4 + 0.12 * jj, 0.7 + 0.08 * jj))
                        for jj in (1, 2, 3)],
                      FadeIn(p_xt, rate_func=window(0.5, 1.0)), run_time=T_q)
            self.remove(p0x, p0y, old_n, new_n)
            self.add(p0)
            self.bring_to_front(self.ell, line_a, dots_a)
            # "share": copies of the ellipse and its line, as one, arc over the panel row to the
            # other three, farthest panel first. Each copy launches already moving (ease-out) and
            # they leave 0.15 s apart, so no second stroke lingers on panel I (round 8: a slow
            # smooth start left a doubled ellipse there for ~0.4 s); "these five numbers": the
            # readout is boxed
            T_s = 1.75
            t_th = min(0.6, max(0.0, beat.until("these", offset=-0.1) / T_s))

            def launch(k, dur=1.25):
                s0, dd = 0.15 * k / T_s, dur / T_s
                return lambda t: 1 - (1 - min(1.0, max(0.0, (t - s0) / dd))) ** 3
            # (ReplacementTransform of an explicit copy: TransformFromCopy runs its rate
            # function on 1 - alpha, which would turn the ease-out into a delayed ease-in)
            pair = VGroup(self.ell, line_a)
            self.play(*[ReplacementTransform(pair.copy(), VGroup(pells[jj], plines[jj]),
                                             path_arc=0.6, rate_func=launch(k))
                        for k, jj in enumerate((3, 2, 1))],
                      Create(hl_read, rate_func=window(t_th, t_th + 0.3)), run_time=T_s)
            beat.wait_until("trend", offset=-0.15)
            self.play(FadeIn(tags[0], shift=0.1 * UP), FadeOut(hl_read), run_time=0.5)
            beat.wait_until("curve", offset=-0.15)
            self.play(FadeIn(tags[1], shift=0.1 * UP), run_time=0.5)
            beat.wait_until("outlier", offset=-0.15)
            self.play(FadeIn(tags[2], shift=0.1 * UP), Create(ring3), run_time=0.6)
            beat.wait_until("one point", offset=-0.15)
            self.play(FadeIn(tags[3], shift=0.1 * UP), Create(ring4), run_time=0.6)

        # ================================================================ LANDING
        # Panel I becomes the opening frame: its axis lines and ticks transform into the 0-100
        # axes (the tick numbers hand over: old out, then new in), its "y" travels to the big
        # plot's "y", its ellipse grows back to the dinosaur's, and "slope = r s_y / s_x" is
        # carried down to the band under the readout. Only the guess cloud, its labels and the
        # readout fade in. The rest of the quartet leaves first.
        f1_fam = set(f1.get_family())
        p0 = panels[0]
        p0_nums = VGroup(p0.x_axis.numbers, p0.y_axis.numbers)
        src_x, src_y = p0.x_axis.copy(), p0.y_axis.copy()
        src_x.remove(src_x.numbers)
        src_y.remove(src_y.numbers)
        self.remove(p0)
        self.add(src_x, src_y, p0_nums)
        keep_l = {id(m_) for m_ in (self.ell, src_x, src_y, p0_nums, p_yt)}
        quartet = [m_ for m_ in self.mobjects
                   if id(m_) not in keep_l and not (set(m_.get_family()) & f1_fam)]
        self.ax = ax = main_axes()
        self.dots = VGroup(*[Dot(radius=0.055, color=GRAY) for _ in range(N)])
        self.place(guess)
        ell_l = ell_mob(ax, T).set_z_index(2)
        guess_lbl2 = guess_lbl.copy()
        guess_line2 = DashedLine(*line_xy(ax), color=GRAY, stroke_width=3, dash_length=0.14)
        line_lbl2 = line_lbl.copy()
        line_l = Line(*line_xy(ax), color=YELLOW, stroke_width=4).set_z_index(3)
        cen_l = ax.c2p(T[0], T[1])
        # the stakes bar returns: an average and an error bar are two of the five numbers
        bar_l = bar_rect.copy().set_fill(opacity=0.15).set_stroke(opacity=1.0).set_z_index(1)
        err_l = vbar(ax, T[0], T[1], T[3], YELLOW, sw=5, cap=0.16).set_z_index(3)
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
        bar_out[0].set_fill(opacity=0.09).set_stroke(opacity=0.6)
        bar_out[1].set_stroke(opacity=0.6)
        require_clear(ax.x_name, bar_out, what="axis name vs parked bar")
        require_clear(table_cold, bar_out, what="readout vs parked bar")

        # "your line" answered with a number: the dinosaur's r, s_y and s_x go into the slope
        FSL = 36                                             # label size: keeps it narrow enough
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
        # its left edge sits >= 0.75 right of the plot's axis name "x" (at 0.5 the two read as
        # one expression, "x slope ="), and the substituted form ends at the safe margin
        l_lhs.move_to([1.0, -1.9, 0], aligned_edge=LEFT)
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
        assert l_lhs.get_left()[0] - ax.x_name.get_right()[0] >= 0.75, "landing slope too near 'x'"
        # the parked bar keeps its tag: "86% used bars" sits over its error bar in the last frame,
        # and "+-1 SD" beside its top cap, on the open side away from the readout
        pct86_out = pct86_l.copy().next_to(bar_out[1], UP, buff=0.3)
        require_safe(pct86_out, "parked '86%'")
        dino_scr = VGroup(*[Dot(p, radius=0.055) for p in to_screen(ax, dino)])
        require_clear(pct86_out, table_cold, bar_out, dino_scr, cite_w2, what="parked '86%'")
        cap_top = bar_out[1][2]                              # the error bar's top cap
        sd_out = MathTex(r"\pm 1\ \text{SD}", font_size=36, color=TXT_GRAY)
        sd_out.next_to(cap_top, LEFT, buff=0.2).shift(DOWN * 0.05)
        require_safe(sd_out, "parked '+-1 SD'")
        require_clear(sd_out, pct86_out, table_cold, bar_out, dino_scr, ell_l, line_l,
                      what="parked '+-1 SD'")
        rows_three = VGroup(table_cold[0], table_cold[2], table_cold[4])   # x-bar, s_x, r

        # one continuous object: panel I's axes grow into the opening's axes around the ellipse
        # (the frame is never an ellipse on an empty field); the rest of the quartet has left
        # before the formula sets off, and the formula clears the readout's slot before the
        # readout fades in, so it never crosses the panels or the readout
        dst_x, dst_y = ax.x_axis.copy(), ax.y_axis.copy()
        dst_nums = VGroup(dst_x.numbers, dst_y.numbers)
        dst_x.remove(dst_x.numbers)
        dst_y.remove(dst_y.numbers)
        dst_yname = ax.y_name.copy()
        dst_xname = ax.x_name.copy()
        ax_late = VGroup(dst_xname)                         # "x": fades in as its axis arrives
        # each 0-100 tick number rides its own spot on the growing axis (from where it sits on
        # panel I's axis to where it sits on the opening's), fading in on the way, so the axes
        # are never without numbers for long and no number floats ahead of its axis
        ride = []
        for a_src, a_dst, span in ((src_x, dst_x, 20.0), (src_y, dst_y, 15.0)):
            for num in a_dst.numbers:
                v_ = float(num.get_value())
                off_ = num.get_center() - a_dst.n2p(v_)
                ride.append((num, a_src.n2p(v_ * span / 100) + off_, num.get_center().copy()))
        AX_RATE = window(0.05, 0.75)

        def ride_nums(m, a):
            al_, op_ = AX_RATE(a), window(0.22, 0.6)(a)
            for num, q0, q1 in ride:
                num.move_to(q0 + (q1 - q0) * al_)
                num.set_opacity(op_)
        late_fam = {id(f_) for f_ in VGroup(readout_a, cite_an).get_family()}

        def is_late(m_):
            return all(id(f_) in late_fam for f_ in m_.get_family())
        late_out = [m_ for m_ in quartet if is_late(m_)]
        quartet = [m_ for m_ in quartet if not is_late(m_)]
        self.play(FadeOut(Group(*quartet), rate_func=window(0.0, 0.3)),
                  # his readout and citation stay a little longer (the right half is never empty
                  # for long); they are gone before the formula reaches their slot
                  FadeOut(Group(*late_out), rate_func=window(0.0, 0.3)),
                  FadeOut(p0_nums, rate_func=window(0.0, 0.2)),
                  ReplacementTransform(src_x, dst_x, rate_func=AX_RATE),
                  ReplacementTransform(src_y, dst_y, rate_func=AX_RATE),
                  ReplacementTransform(p_yt, dst_yname, rate_func=AX_RATE),
                  UpdateFromAlphaFunc(dst_nums, ride_nums, rate_func=linear),
                  ReplacementTransform(self.ell, ell_l, rate_func=window(0.05, 0.75)),
                  # down the open middle first, then in from the left under the readout, so it
                  # never passes over the readout's r row as that fades in. Round 8: it is in its
                  # band by half-time, and the readout, the guess cloud and its labels fade in
                  # from 0.3-0.4 of the move (they used to start at 0.5-0.6, leaving ~1 s of a lone
                  # ellipse and a floating formula); the formula is always clear of them
                  Transform(f1, f_land, rate_func=window(0.08, 0.52),
                            path_func=bez_path(f1, f_land, (0.8, -0.5), (1.0, -1.9))),
                  FadeIn(ax_late, rate_func=window(0.55, 0.85)),
                  FadeIn(table_cold, rate_func=window(0.3, 0.72)),
                  FadeIn(VGroup(self.dots, guess_lbl2, guess_line2, line_lbl2),
                         rate_func=window(0.4, 0.8)), run_time=1.5)
        self.remove(dst_x, dst_y, ax_late, dst_yname, dst_nums)
        self.add(ax)
        with self.narrate("Your line was right: five numbers fix it exactly, slope minus point "
                          "one. [pause 0.8] Your cloud was wrong: a blur around this ellipse, all that five "
                          "numbers can draw. [pause 0.6] Most of those papers used a bar graph, "
                          "which draws only two. [pause 0.6] The dinosaur lived in everything they "
                          "leave out.") as beat:
            beat.wait_until("line", offset=-0.1)
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
                       elbow_path(src_, dst_, 6.0))
                # a whole-MathTex copy (same structure as its target), so each glyph maps onto
                # itself and the number stays legible in flight
                cp_ = MathTex(f"{TR[i_]:.2f}", font_size=42, color=YELLOW).move_to(src_)
                flights.append(ReplacementTransform(cp_, dst_, path_func=pf_))
            # each symbol floats up (or down) and out before its value arrives, so a value never
            # lands on a fading symbol (no cross-fade in place); the numerator values land at
            # about 0.62 and 0.81 of the move, the denominator's at 1.0. Each source value is
            # hidden while its copy leaves it and fades back once the copy is clear, so the two
            # never read as a doubled number
            srcs_l = [table_cold[i_][2] for i_ in (4, 3, 2)]
            starts = [0.0, 0.1875, 0.375]                      # LaggedStart(lag 0.3) of three

            def dim_sources(m, a):
                for src_, s0 in zip(srcs_l, starts):
                    up = min(1.0, max(0.0, (a - s0) / 0.02))
                    down = min(1.0, max(0.0, (a - s0 - 0.25) / 0.15))
                    src_.set_opacity(1 - up * (1 - down))
            self.play(f1[1].animate(rate_func=window(0.0, 0.25)).shift(UP * 0.25).set_opacity(0),
                      f1[3].animate(rate_func=window(0.3, 0.55)).shift(DOWN * 0.25).set_opacity(0),
                      Transform(f1[2], v_bar, rate_func=window(0.25, 0.6)),
                      LaggedStart(*flights, lag_ratio=0.3),
                      UpdateFromAlphaFunc(VGroup(*srcs_l), dim_sources, rate_func=linear),
                      FadeIn(v_x, rate_func=window(0.55, 0.8)), run_time=1.3)
            for src_ in srcs_l:
                src_.set_opacity(1.0)
            # "exactly": the line the five numbers fix grows onto the dashed guess
            beat.wait_until("exactly", offset=-0.2)
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
            # the line and the ellipse step back to 60 %, so the squeezed copy, the bar
            # and the error bar are the only full-strength strokes where they meet
            self.play(FadeIn(cite_w2), FadeIn(pct86_l, shift=0.1 * DOWN),
                      FadeOut(VGroup(f1, v_num, v_den, v_ap, v_val)),
                      self.dots.animate.set_opacity(0.15),
                      line_l.animate.set_stroke(opacity=0.6),
                      ell_l.animate.set_stroke(opacity=0.6), run_time=0.6)
            beat.wait_until("bar graph", offset=-0.15)
            # the ellipse squeezed to its vertical extent is exactly the error bar, y-bar +- s_y
            self.add(squash)
            self.play(squash.animate.stretch(0.01, 0), GrowFromEdge(bar_l, DOWN), run_time=1.1)
            self.play(FadeIn(err_l), FadeOut(squash), run_time=0.3)
            # "which draws only two": the three rows a bar cannot draw step back, so the two
            # bright rows are exactly the two numbers the bar draws (y-bar and s_y)
            beat.wait_until("only", offset=-0.15)
            self.play(*[r_[k_].animate.set_opacity(0.3) for r_ in rows_three for k_ in (0, 1)],
                      *[r_[2].animate.set_color(TXT_GRAY).set_opacity(0.3) for r_ in rows_three],
                      run_time=0.5)
            beat.wait_until("two", offset=-0.15)
            self.play(flag(rows_two), run_time=0.8)
            beat.wait_until("dinosaur", offset=-0.2)
            # the points return at full strength and are the one focal point: the ellipse and
            # the line (what the five numbers know) step back to 60 % and a thin stroke; the bar and its error bar
            # leave the plot in place and reappear beside it (never sliding across the cloud or
            # the axis name), and their tag moves with them (out at the top left, back in over
            # the parked bar, so it never crosses the returning points)
            self.go(lambda a: lerp(guess, dino, a), 1.6, smooth,
                    FadeOut(VGroup(bar_l, err_l), rate_func=window(0.0, 0.25)),
                    FadeIn(bar_out, rate_func=window(0.5, 0.75)),
                    FadeOut(pct86_l, rate_func=window(0.0, 0.35)),
                    FadeIn(pct86_out, shift=0.1 * DOWN, rate_func=window(0.65, 1.0)),
                    FadeIn(sd_out, rate_func=window(0.65, 1.0)),
                    # (60 % and a thinner stroke: yellow dimmed further reads olive, a new hue)
                    line_l.animate.set_stroke(opacity=0.6, width=2.5),
                    ell_l.animate.set_stroke(opacity=0.6, width=2.5),
                    color_from=GRAY, color_to=BLUE, op_from=0.15, op_to=1.0)

        # clean exit: the plot leaves first, so the card never sits on top of the data
        self.play(*[FadeOut(m) for m in list(self.mobjects)], run_time=0.4)
        self.end_card(hold=0.6, run_time=0.4)
