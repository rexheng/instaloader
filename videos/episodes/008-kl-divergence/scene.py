"""Sample Space, episode 8: The Distance That Isn't Symmetric (KL divergence).

    videos/toolkit/render.sh --preview videos/episodes/008-kl-divergence/scene.py Episode /tmp/ep8.mp4
    videos/toolkit/render.sh videos/episodes/008-kl-divergence/scene.py Episode \
        videos/episodes/008-kl-divergence/final.mp4

Palette (one meaning each, see script.md):
    BLUE    the data: eruption bars, the smoothed curve, p, the word "data" (and, in the payoff,
            the curve standing in for a posterior, with its spread 1.14)
    PURPLE  the bell (the model): bells A and B, q, the words "bell"/"model", their stats
    RED     the divergence in bits: every bits number, the log2 term, the two shaded bills
    YELLOW  focus: the one length examined, the 1/2/3 bet, boxes, doublings, "?", brackets
    GRAY    axes, citations, the negative (refund) part of a bill, clipped values
Data: data.json, written by data.py (R `faithful`, 272 eruption lengths).
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from manim import *
from sample_space import *

HERE = Path(__file__).resolve().parent
D = json.loads((HERE / "data.json").read_text())
PI = np.array(D["mix"]["pi"])
MU = np.array(D["mix"]["mu"])
SDS = np.array(D["mix"]["sd"])
MA, SA = D["A"]["mu"], D["A"]["sd"]
MB, SB = D["B"]["mu"], D["B"]["sd"]
PATH = np.array(D["descent_path"])                 # (mu, sd, D(bell||data)) from A to B
RPATH = np.array(D["rdef"]["path_from_A"])         # A -> wide fit, under R's default smoothing
CPATH = np.array(D["cv"]["path_from_wide"])        # wide fit -> long hump, cross-validated
H_RDEF, H_CV = D["rdef"]["h"], D["cv"]["h"]
MW, SW = D["rdef"]["wide"][:2]
MC, SC = CPATH[-1, 0], CPATH[-1, 1]
ERUPT = np.array(D["eruptions"])
EDGES = np.array(D["hist_edges"])
COUNTS = np.array(D["hist_counts"])
N = D["n"]
LN2 = math.log(2.0)
LOG_SQ2PI = 0.5 * math.log(2 * math.pi)

# integration grid (wide: the bell's tails matter when the bell goes first) and plot grid
G = np.linspace(-6.0, 13.0, 7601)
DG = G[1] - G[0]
XS = np.linspace(0.0, 7.0, 421)


def log_norm(x, m, s):
    return -0.5 * ((x - m) / s) ** 2 - math.log(s) - LOG_SQ2PI


def logp_mix(x):
    return np.logaddexp(math.log(PI[0]) + log_norm(x, MU[0], SDS[0]),
                        math.log(PI[1]) + log_norm(x, MU[1], SDS[1]))


def logp_kde(x, h):
    x = np.asarray(x, float)
    out = np.empty_like(x)
    for i in range(0, len(x), 1000):                  # Gaussian kernel smoother, bandwidth h
        z = log_norm(x[i:i + 1000, None], ERUPT[None, :], h)
        mx = z.max(1, keepdims=True)
        out[i:i + 1000] = (mx[:, 0] + np.log(np.exp(z - mx).sum(1))) - math.log(N)
    return out


LP_G = (logp_mix(G), logp_kde(G, H_RDEF), logp_kde(G, H_CV))
LP_X = (logp_mix(XS), logp_kde(XS, H_RDEF), logp_kde(XS, H_CV))


def blend3(lps, wr, wc):
    """log of (1 - wr - wc) * mix + wr * R-default + wc * cross-validated."""
    ws = (1.0 - wr - wc, wr, wc)
    terms = [math.log(w) + lp for w, lp in zip(ws, lps) if w > 1e-9]
    if len(terms) == 1:
        return terms[0]
    return np.logaddexp.reduce(np.stack(terms), axis=0)


def runs(mask):
    """Contiguous runs of equal values in a boolean array -> [(i0, i1, value)], inclusive."""
    out, i0 = [], 0
    for i in range(1, len(mask) + 1):
        if i == len(mask) or mask[i] != mask[i0]:
            out.append((i0, i - 1, bool(mask[i0])))
            i0 = i
    return out


# ------------------------------------------------------------------ layouts
# (origin x, origin y, units per minute, units per density) of the eruption chart
FULL = (-5.0, -1.7, 10.0 / 7.0, 4.0)        # one big chart (x title clears the citation slot)
MID = (-5.85, -2.0, 7.6 / 7.0, 4.2)         # one length examined, right column for the pull-out
TWO = (-5.75, 0.65, 1.0, 2.2)               # chart on top, the data-first bill underneath
THREE = (-5.75, 0.05, 1.0, 2.8)             # chart on top (the subject, 2.8 tall), both bills under
# bills: (origin y, units per bit/minute); y runs over [B_LO, B_HI] bits per minute
# (stacked bills run over [B3_LO, B_HI]: along the A -> B path no bill dips below -0.37)
B1_TWO, B1_THREE, B2_THREE = (-1.3, 0.66), (-1.10, 0.38), (-2.46, 0.38)
B_LO, B_HI, B3_LO = -1.0, 2.5, -0.5
SCAN_HI = 1.8                               # lower scanner line stops under the unit label
RX = 4.4                                    # right column centre
COLX = 1.7                                  # left edge of the formula blocks (stacked panels)
BLK = 38                                    # formula-block type size
ROW1, ROW2 = 3.15, 2.4                      # the two notation lines (full layout)
NX = 2.95                                   # their centre
PIN_Y = 1.2                                 # labels pinned above a bell's crown (full layout)
PX, QX, PW = 3.35, 4.45, 0.7                # pulled-out p and q bars (one-length beat)
Y_RP, Y_RQ, Y_LR = 2.6, 1.95, 1.15          # readouts (beats 5-7)


def panel_mid(b, lo=B_LO):
    """Vertical centre of a bill panel (origin y, units per bit/min)."""
    return b[0] + 0.5 * (lo + B_HI) * b[1]


# two-line formula blocks ("D(.||.) = x bits" over "= int ..."), each centred on its own panel
ROWS_TWO = (panel_mid(B1_TWO) + 0.3, panel_mid(B1_TWO) - 0.3)
MID1_THREE, MID2_THREE = panel_mid(B1_THREE, B3_LO), panel_mid(B2_THREE, B3_LO)
ROWS1_THREE = (MID1_THREE + 0.34, MID1_THREE - 0.26)     # (a hair high: the shared x label
ROWS2_THREE = (MID2_THREE + 0.34, MID2_THREE - 0.26)     #  runs under the lower block)


def note(first: str, second: str, size=36) -> MathTex:
    m = MathTex(r"D(", r"\text{%s}" % first, r"\,\|\,", r"\text{%s}" % second, r")",
                font_size=size)
    for i, w in ((1, first), (3, second)):
        m[i].set_color(BLUE if w in ("data", "posterior") else PURPLE)
    return m


def bits_readout(value: float, size=36) -> VGroup:
    eq = MathTex("=", font_size=size)
    num = DecimalNumber(value, num_decimal_places=2, font_size=size, color=RED)
    unit = MathTex(r"\text{bits}", font_size=size, color=RED)
    g = VGroup(eq, num, unit).arrange(RIGHT, buff=0.18)
    num.align_to(eq, DOWN).shift(0.02 * DOWN)
    unit.align_to(eq, DOWN)
    g.num = num
    return g


def rhs(weight: str, top: str, bot: str, size=40) -> MathTex:
    """= int w log2(top / bot) dx, inline so a block fits next to a short bill panel."""
    m = MathTex(r"=\textstyle\int", weight, r"\,\log_2", r"(", top, r"/", bot, r")", r"\,dx",
                font_size=size)
    col = {"p": BLUE, "q": PURPLE}
    m[1].set_color(col[weight])
    m[2].set_color(RED)
    m[4].set_color(col[top])
    m[6].set_color(col[bot])
    return m


def chart_axes(lay, xlab=True, ytop=1.0) -> Axes:
    ox, oy, xu, yu = lay
    ax = axes((0, 7), (0, ytop), x_length=7 * xu, y_length=ytop * yu, x_ticks=[1, 2, 3, 4, 5, 6],
              y_ticks=[0, 0.5, 1], x_label="eruption length (minutes)",
              y_label="density (per minute)")
    ax.shift(np.array([ox, oy, 0]) - ax.c2p(0, 0))
    if not xlab:                     # stacked panels: the shared x labels sit under the bottom bill
        ax.x_axis.numbers.set_opacity(0)
        ax.x_title.set_opacity(0)
    return ax


def bill_axes(oy, yu, sparse=False, lo=B_LO) -> Axes:
    ax = axes((0, 7), (lo, B_HI), x_length=7 * TWO[2], y_length=(B_HI - lo) * yu,
              x_ticks=[1, 2, 3, 4, 5, 6], y_ticks=[-1, 0, 1, 2] if lo <= -1 else [0, 1, 2])
    ax.x_axis.remove(ax.x_axis.numbers)
    ax.shift(np.array([TWO[0], oy, 0]) - ax.c2p(0, 0))
    if sparse:                       # short panels: label only 0 and 2
        for num in [n for n in ax.y_axis.numbers if abs(n.get_value()) == 1]:
            ax.y_axis.numbers.remove(num)
    return ax


def bill_unit(oy, yu, s="bits/min") -> VMobject:
    """The bill's unit in its top-left corner; 'bits / per min' on two short lines, so it stays
    clear of the clipped data-first mountain (which rises at 1.5 min)."""
    if s == "bits":
        t = MathTex(r"\text{bits}", font_size=34, color=GRAY)
    else:                                   # a stacked unit: narrow enough to clear the mountain
        t = MathTex(r"\dfrac{\text{bits}}{\text{min}}", font_size=34, color=GRAY)
    top = oy + B_HI * yu
    t.move_to([TWO[0] + 0.22, top, 0], aligned_edge=UL)
    return t


def order_tag(oy, yu, first: str) -> VGroup:
    """'data first' / 'bell first' in a stacked bill's top-right corner: which bill is which."""
    w = text(first, size=LABEL, color=BLUE if first == "data" else PURPLE)
    g = VGroup(w, text("first", size=LABEL, color=INK)).arrange(RIGHT, buff=0.12)
    g[1].align_to(g[0], DOWN)
    g.move_to([TWO[0] + 7 * TWO[2] - 0.05, oy + B_HI * yu, 0], aligned_edge=UR)
    return g


def x_labels(y_bottom, side=False) -> VGroup:
    """Shared x-axis labels (1-6 and the name) under the lowest panel; side=True puts the name
    on the numbers' row, right of the 6 (stacked layout: no height to spare)."""
    nums = VGroup(*[MathTex(str(k), font_size=MATH_SMALL, color=GRAY) for k in range(1, 7)])
    for k, m in zip(range(1, 7), nums):
        m.move_to([TWO[0] + TWO[2] * k, y_bottom - 0.16, 0], aligned_edge=UP)
    name = Text("eruption length (minutes)", font=SERIF, font_size=LABEL, color=GRAY)
    if side:
        name.next_to(nums[-1], RIGHT, buff=0.4)
        name.shift((nums[-1].get_bottom()[1] - name[0].get_bottom()[1]) * UP)   # one baseline
    else:
        name.next_to(nums, DOWN, buff=0.16).align_to([TWO[0] + 7 * TWO[2], 0, 0], RIGHT)
    return VGroup(nums, name)


def bracket(left, right, color=YELLOW, tick=0.13, width=4):
    """A horizontal +-1 SD bracket between two points (end ticks)."""
    l, r = np.array(left), np.array(right)
    return VGroup(Line(l, r, color=color, stroke_width=width),
                  Line(l + UP * tick, l + DOWN * tick, color=color, stroke_width=width),
                  Line(r + UP * tick, r + DOWN * tick, color=color, stroke_width=width))


def stack_rows(rows, ys, x=COLX):
    for m, y in zip(rows, ys):
        m.move_to([x, y, 0], aligned_edge=LEFT)
    return rows


def place_block(lhs, f, tot, rows, x=COLX):
    """Two-line block: 'D(.||.) = x bits' on top (result beside its name), '= int ... dx' below."""
    lhs.move_to([x, rows[0], 0], aligned_edge=LEFT)
    tot.next_to(lhs, RIGHT, buff=0.22)
    tot.shift((lhs.get_y() - tot[0].get_y()) * UP)       # '=' on the D-line's math axis
    f.move_to([x, rows[1], 0], aligned_edge=LEFT)
    return VGroup(lhs, f, tot)


class Episode(NarratedScene):
    EPISODE = 8
    TITLE = "The Distance That Isn't Symmetric"
    SPEED = 0.83
    CADENCE = "shaped"           # gaps follow the sense (PRODUCTION_GUIDE §13.3)
    # misaki reads a lone "A" as the article and "imagines" as "im-AY-jen-eez"
    PRONUNCIATIONS = {"Leibler": "lie bler", "Kullback": "cull back", "Blei": "bly", "A": "/ˈA/",
                      "imagines": "/ɪmˈæʤənz/"}

    # ------------------------------------------------------------------ geometry
    def c2p(self, x, y):
        return (self.ox.get_value() + self.xu.get_value() * np.asarray(x),
                self.oy.get_value() + self.yu.get_value() * np.asarray(y))

    def pt(self, x, y):
        px, py = self.c2p(x, y)
        return np.array([px, py, 0.0])

    def bp(self, k, x, y):
        oy, yu = (self.b1y, self.b1u) if k == 1 else (self.b2y, self.b2u)
        return np.array([self.ox.get_value() + self.xu.get_value() * x,
                         oy.get_value() + yu.get_value() * y, 0.0])

    def bps(self, k, xs, ys):
        oy, yu = (self.b1y, self.b1u) if k == 1 else (self.b2y, self.b2u)
        return np.c_[self.ox.get_value() + self.xu.get_value() * np.asarray(xs),
                     oy.get_value() + yu.get_value() * np.asarray(ys), np.zeros(len(xs))]

    def to_layout(self, lay):
        return [t.animate.set_value(v) for t, v in zip((self.ox, self.oy, self.xu, self.yu), lay)]

    def move_axes(self, lay, xlab=True):
        new = chart_axes(lay, xlab)
        anim = ReplacementTransform(self.ax, new)
        self.ax = new
        return anim

    def move_axes_top(self, ytop):
        lay = tuple(t.get_value() for t in (self.ox, self.oy, self.xu, self.yu))
        new = chart_axes(lay, True, ytop=ytop)
        anim = ReplacementTransform(self.ax, new)
        self.ax = new
        return anim

    # ------------------------------------------------------------------ the numbers
    def lp_x(self):
        return blend3(LP_X, self.sm_r.get_value(), self.sm_c.get_value())

    def lp_g(self):
        return blend3(LP_G, self.sm_r.get_value(), self.sm_c.get_value())

    def p_at(self, x):
        return float(np.exp(np.interp(x, XS, self.lp_x())))

    def q_at(self, x, m=None, s=None):
        m = self.mu.get_value() if m is None else m
        s = self.sd.get_value() if s is None else s
        return float(math.exp(log_norm(x, m, s)))

    def total(self, kind=1, upto=None, m=None, s=None):
        """kind 1: D(data||bell); kind 2: D(bell||data); bits, optionally only up to x."""
        m = self.mu.get_value() if m is None else m
        s = self.sd.get_value() if s is None else s
        lp, lq = self.lp_g(), log_norm(G, m, s)
        f = np.exp(lp) * (lp - lq) if kind == 1 else np.exp(lq) * (lq - lp)
        if upto is not None:
            f = np.where(G <= upto, f, 0.0)
        return float(f.sum() * DG / LN2)

    def integrand_x(self, kind):
        m, s = self.mu.get_value(), self.sd.get_value()
        lp, lq = self.lp_x(), log_norm(XS, m, s)
        if kind == 1:
            w = self.weighted.get_value()
            return (lp - lq) / LN2 * ((1 - w) + w * np.exp(lp))
        return (lq - lp) / LN2 * np.exp(lq)

    # ------------------------------------------------------------------ builders
    def make_bars(self):
        h = self.bar_h.get_value()
        op = self.bar_op.get_value()
        g = VGroup()
        for lo, c in zip(EDGES[:-1], COUNTS):
            d = c / (N * 0.25) * h
            g.add(Polygon(self.pt(lo + 0.012, 0), self.pt(lo + 0.238, 0),
                          self.pt(lo + 0.238, d), self.pt(lo + 0.012, d),
                          stroke_width=0, fill_color=BLUE, fill_opacity=op))
        return g

    def curve_pts(self, ys, x0=0.0, x1=7.0, top=1.0):
        msk = (XS >= x0 - 1e-9) & (XS <= x1 + 1e-9)
        px, py = self.c2p(XS[msk], np.minimum(ys[msk], top))
        return np.c_[px, py, np.zeros(msk.sum())]

    def make_pcurve(self):
        pts = self.curve_pts(np.exp(self.lp_x()), 0.6, 6.4, top=1.08)
        c = VMobject(stroke_color=BLUE, stroke_width=self.p_w.get_value(),
                     stroke_opacity=self.p_op.get_value())
        c.set_points_smoothly(pts[::2])
        fo = self.p_fill.get_value()
        if fo < 0.005:
            return VGroup(c)
        fp = self.curve_pts(np.exp(self.lp_x()), 0.0, 7.0, top=1.08)
        poly = Polygon(*fp, [fp[-1][0], self.pt(0, 0)[1], 0], self.pt(0.0, 0), stroke_width=0,
                       fill_color=BLUE, fill_opacity=fo)
        return VGroup(poly, c)

    def bell_shape(self, m, s, color=PURPLE, width=4.5, opacity=1.0, fill=0.0, dashed=False,
                   fill_x=7.0):
        pts = self.curve_pts(np.exp(log_norm(XS, m, s)), top=1.08)
        c = VMobject(stroke_color=color, stroke_width=width, stroke_opacity=opacity)
        c.set_points_as_corners(pts)
        if dashed:
            c = DashedVMobject(c, num_dashes=70, dashed_ratio=0.55)
        if fill <= 0.001 or fill_x <= 0.05:
            return VGroup(c)
        fp = self.curve_pts(np.exp(log_norm(XS, m, s)), 0.0, fill_x, top=1.08)
        if len(fp) < 2:
            return VGroup(c)
        poly = Polygon(*fp, [fp[-1][0], self.pt(0, 0)[1], 0], self.pt(0.0, 0),
                       stroke_width=0, fill_color=color, fill_opacity=fill)
        return VGroup(poly, c)

    def make_bell(self):
        return self.bell_shape(self.mu.get_value(), self.sd.get_value(),
                               fill=self.bell_fill.get_value(), opacity=self.bell_op.get_value(),
                               fill_x=self.bell_fill_x.get_value(), width=self.bell_w.get_value())

    def make_ghost(self):
        """Bell A when another bell is the focus: dashed; solid when it is a contender."""
        op, sol = self.a_op.get_value(), self.a_solid.get_value()
        g = VGroup()
        if op * (1 - sol) > 0.01:
            g.add(self.bell_shape(MA, SA, width=2.5 + 2.0 * max(0.0, op - 0.4) / 0.6,
                                  opacity=op * (1 - sol), dashed=True))
        if op * sol > 0.01:
            g.add(self.bell_shape(MA, SA, opacity=op * sol, fill=self.a_fill.get_value(),
                                  fill_x=self.a_fill_x.get_value(), width=self.a_w.get_value()))
        return g

    def hump_flash(self, ys, thr=0.08, run_time=1.0):
        """ShowPassingFlash along only the parts of a curve that stand above the axis, so the
        highlight never crawls along the flat tails."""
        anims = []
        for i0, i1, on in runs(ys > thr):
            if not on or i1 - i0 < 3:
                continue
            px, py = self.c2p(XS[i0:i1 + 1], np.minimum(ys[i0:i1 + 1], 1.08))
            seg = VMobject(stroke_color=YELLOW, stroke_width=7)
            seg.set_points_as_corners(np.c_[px, py, np.zeros(len(px))])
            anims.append(ShowPassingFlash(seg, time_width=0.6))
        return AnimationGroup(*anims, run_time=run_time)

    def flash_p(self, run_time=1.0):
        return self.hump_flash(np.exp(self.lp_x()), run_time=run_time)

    def flash_bell(self, m=None, s=None, run_time=1.0):
        m = self.mu.get_value() if m is None else m
        s = self.sd.get_value() if s is None else s
        return self.hump_flash(np.exp(log_norm(XS, m, s)), run_time=run_time)

    def make_area(self, k):
        raw = self.integrand_x(k)
        f = np.clip(raw, B_LO, B_HI)
        if k == 1:
            rv, frv = self.reveal.get_value(), self.fill_reveal.get_value()
            fill, op = self.area_fill.get_value(), self.area_op.get_value()
        else:
            rv, frv = 7.0, self.fill2_reveal.get_value()
            fill, op = 1.0, self.area2_op.get_value()
        g = VGroup()
        if op < 0.005:
            return g
        for sign, color, fo in ((1, RED, 0.55), (-1, GRAY, 0.45)):
            part = np.maximum(f, 0) if sign > 0 else np.minimum(f, 0)
            msk = XS <= min(rv, frv) + 1e-9
            if fill * op > 0.001 and msk.sum() >= 2:
                xs, ps = XS[msk], part[msk]
                pts = self.bps(k, xs, ps)
                g.add(Polygon(*pts, self.bp(k, xs[-1], 0), self.bp(k, xs[0], 0), stroke_width=0,
                              fill_color=color, fill_opacity=fo * fill * op))
            n = int((XS <= rv + 1e-9).sum())
            if n < 2:
                continue
            clipped = raw[:n] < B_LO - 1e-9 if sign < 0 else np.zeros(n, bool)
            for i0, i1, cl in runs(clipped):
                j0, j1 = max(0, i0 - 1), min(n - 1, i1 + 1)
                if j1 <= j0:
                    continue
                # clipped stretches (true value far below the panel) are drawn faint
                line = VMobject(stroke_color=color, stroke_width=3,
                                stroke_opacity=op * (0.3 if cl else 1.0))
                line.set_points_as_corners(self.bps(k, XS[j0:j1 + 1], part[j0:j1 + 1]))
                g.add(line)
        return g

    def make_scanner(self):
        """Two dashed lines built once and slid along x by an updater (cheap per frame)."""
        top = DashedLine(UP, DOWN, dash_length=0.08, stroke_color=YELLOW, stroke_width=2.5)
        bot = DashedLine(UP, DOWN, dash_length=0.08, stroke_color=YELLOW, stroke_width=2.5)
        g = VGroup(top, bot)
        cache = [None, None]

        def upd(m):
            x = self.scan.get_value()
            op = self.scan_op.get_value()
            yu, bu = self.yu.get_value(), self.b1u.get_value()
            if cache[0] is None or abs(cache[0] - yu) > 1e-6:
                top.stretch_to_fit_height(yu)
                cache[0] = yu
            if cache[1] is None or abs(cache[1] - bu) > 1e-6:
                bot.stretch_to_fit_height((SCAN_HI - B_LO) * bu)
                cache[1] = bu
            top.move_to(self.pt(x, 0.5))
            bot.move_to(self.bp(1, x, (B_LO + SCAN_HI) / 2))
            top.set_stroke(opacity=op)
            bot.set_stroke(opacity=op * self.bot_scan_op.get_value())
        g.add_updater(upd)
        upd(g)
        return g

    def make_pq_bars(self):
        x = self.scan.get_value()
        op = self.pq_op.get_value()
        p, q = self.p_at(x), self.q_at(x)
        w = 0.2
        base = self.pt(x, 0)
        hp = (self.pt(x, p)[1] - base[1]) * self.p_h.get_value()
        hq = (self.pt(x, min(q, 1.0))[1] - base[1]) * self.q_h.get_value()
        rp = Rectangle(width=w, height=max(hp, 0.004), stroke_width=0, fill_color=BLUE,
                       fill_opacity=op * min(1, 5 * self.p_h.get_value())
                       ).move_to(base + LEFT * 0.115, aligned_edge=DOWN)
        rq = Rectangle(width=w, height=max(hq, 0.004), stroke_width=0, fill_color=PURPLE,
                       fill_opacity=op * min(1, 5 * self.q_h.get_value())
                       ).move_to(base + RIGHT * 0.115, aligned_edge=DOWN)
        return VGroup(rp, rq)

    def redraw(self, func, *trackers):
        """always_redraw that rebuilds only when the layout or one of the given trackers changed."""
        base = (self.ox, self.oy, self.xu, self.yu, self.b1y, self.b1u, self.b2y, self.b2u)
        keyfn = lambda: tuple(round(t.get_value(), 6) for t in base + trackers)
        mob = func()
        state = {"k": keyfn()}

        def upd(m):
            k = keyfn()
            if k != state["k"]:
                state["k"] = k
                m.become(func())
        mob.add_updater(upd)
        return mob

    def pulse(self, *ms, extra=(), run_time=0.9, scale=1.1):
        """Indicate live numbers without fighting their updaters (values are static here)."""
        for m in ms:
            m.suspend_updating()
        self.play(*[Indicate(m, color=YELLOW, scale_factor=scale) for m in ms], *extra,
                  run_time=run_time)
        for m in ms:
            m.resume_updating()

    def swap_in(self, static, dynamic):
        """Replace a just-created static mobject by its always_redraw twin (same shape)."""
        self.remove(static)
        self.add(dynamic)

    def readout(self, sym, color, fn, y):
        """'p = 0.59', switching to scientific notation below 0.01 ('q = 1.6 x 10^-6'), so a
        tiny density never reads as zero next to a finite log ratio."""
        lab = MathTex(sym, "=", font_size=40)
        lab[0].set_color(color)
        dec = DecimalNumber(0.5, num_decimal_places=2, font_size=40, color=color)
        mant = DecimalNumber(1.6, num_decimal_places=1, font_size=40, color=color)
        times = MathTex(r"\times 10", font_size=40, color=color)
        expo = DecimalNumber(-6, num_decimal_places=0, font_size=30, color=color)
        g = VGroup(lab, dec, VGroup(mant, times, expo))
        g.arrange(RIGHT, buff=0.18).move_to([RX, y, 0])
        state = {"dim": False}

        def upd(m):
            k = self.ro_op.get_value()            # dimmed while the scanner is away from 2 min
            if k < 0.999 or state["dim"]:
                lab.set_opacity(k)
                state["dim"] = k < 0.999
            v = max(fn(), 1e-300)
            sci = v < 0.00995
            if sci:
                e = math.floor(math.log10(v))
                mm = v / 10 ** e
                if round(mm, 1) >= 10:
                    mm, e = mm / 10, e + 1
                mant.set_value(mm)
                expo.set_value(e)
                mant.next_to(lab, RIGHT, buff=0.18).set_y(lab[1].get_y())
                times.next_to(mant, RIGHT, buff=0.1).align_to(mant, DOWN)
                expo.next_to(times, RIGHT, buff=0.04).align_to(times, UP).shift(0.14 * UP)
            else:
                dec.set_value(v)
                dec.next_to(lab, RIGHT, buff=0.18).set_y(lab[1].get_y())
            dec.set_opacity(0.0 if sci else k)
            for x in (mant, times, expo):
                x.set_opacity(k if sci else 0.0)
        g.add_updater(upd)
        upd(g)
        return g

    def peak_tag(self):
        """'peak = 11' over the clipped data-first bill, live, shown only while it clips."""
        tag = MathTex(r"\text{peak} \approx", font_size=36, color=RED)
        num = DecimalNumber(11, num_decimal_places=0, font_size=36, color=RED)
        arrow = Arrow(ORIGIN, RIGHT, buff=0, color=RED, stroke_width=3,
                      max_tip_length_to_length_ratio=0.25)
        g = VGroup(tag, num, arrow)

        def upd(m):
            f = self.integrand_x(1)
            ipk = int(np.argmax(f))
            pk = float(f[ipk])
            op = float(np.clip((pk - B_HI - 0.5) / 1.0, 0, 1)) * self.peak_op.get_value()
            num.set_value(pk)
            fr3 = float(np.clip((B1_TWO[1] - self.b1u.get_value()) / (B1_TWO[1] - B1_THREE[1]), 0, 1))
            yt = 2.0 + (0.85 - 2.0) * fr3          # stacked: mid-height, below the "data first" tag
            tag.move_to(self.bp(1, 3.35, yt), aligned_edge=LEFT)
            num.next_to(tag, RIGHT, buff=0.12)
            num.shift((tag[0][3].get_bottom()[1] - num.get_bottom()[1]) * UP)
            # the arrow stops short of the clipped plateau's right shoulder (it points, never touches)
            right = np.nonzero(f[ipk:] < B_HI)[0]
            xr = float(XS[ipk + right[0]]) if len(right) else float(XS[ipk])
            end = self.bp(1, xr, B_HI - 0.08 / max(self.b1u.get_value(), 0.1)) + RIGHT * 0.18
            arrow.put_start_and_end_on(tag.get_left() + LEFT * 0.15, end)
            for x in (tag, num, arrow):
                x.set_opacity(op)
        g.add_updater(upd)
        upd(g)
        return g

    # ================================================================== construct
    def construct(self):
        self.ox, self.oy, self.xu, self.yu = (ValueTracker(v) for v in FULL)
        self.b1y, self.b1u = ValueTracker(B1_TWO[0]), ValueTracker(B1_TWO[1])
        self.b2y, self.b2u = ValueTracker(B2_THREE[0]), ValueTracker(B2_THREE[1])
        self.mu, self.sd = ValueTracker(MA), ValueTracker(SA)
        self.sm_r, self.sm_c = ValueTracker(0.0), ValueTracker(0.0)   # smoothing weights
        self.bar_h = ValueTracker(1.0)
        self.bar_op = ValueTracker(0.3)
        self.p_op = ValueTracker(1.0)
        self.bell_fill = ValueTracker(0.0)
        self.bell_fill_x = ValueTracker(7.0)
        self.bell_op = ValueTracker(1.0)
        self.reveal = ValueTracker(7.0)
        self.fill_reveal = ValueTracker(7.0)
        self.fill2_reveal = ValueTracker(0.0)
        self.weighted = ValueTracker(0.0)
        self.area_fill = ValueTracker(0.0)
        self.area_op = ValueTracker(1.0)
        self.area2_op = ValueTracker(0.0)
        self.peak_op = ValueTracker(0.0)
        self.scan = ValueTracker(2.0)
        self.scan_op = ValueTracker(1.0)
        self.bot_scan_op = ValueTracker(0.0)
        self.pq_op = ValueTracker(0.9)
        self.p_h, self.q_h = ValueTracker(0.0), ValueTracker(0.0)
        self.a_op = ValueTracker(0.0)          # bell A when it is not the current bell
        self.a_solid = ValueTracker(0.0)
        self.a_fill, self.a_fill_x = ValueTracker(0.0), ValueTracker(0.0)
        self.lab_b_op = ValueTracker(1.0)
        self.p_w, self.p_fill = ValueTracker(4.5), ValueTracker(0.0)   # whole-curve pulses
        self.bell_w, self.a_w = ValueTracker(4.5), ValueTracker(4.5)
        self.ro_op = ValueTracker(1.0)         # p / q readouts: dimmed while the scanner is away
        self.lab_a_op = ValueTracker(1.0)

        self.ax = chart_axes(FULL)
        bars = self.redraw(self.make_bars, self.bar_h, self.bar_op)
        pcurve = self.redraw(self.make_pcurve, self.sm_r, self.sm_c, self.p_op, self.p_w,
                             self.p_fill)
        bell = self.redraw(self.make_bell, self.mu, self.sd, self.bell_fill, self.bell_op,
                           self.bell_fill_x, self.bell_w)

        # ============================================================ 1. cold open: the bet
        n_lab = VGroup(text("272 eruptions", size=LABEL, color=BLUE),
                       text("curve: smoothed", size=LABEL, color=GRAY)
                       ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        n_lab.move_to([2.45, 1.15, 0], aligned_edge=LEFT)
        cite_data = citation("Härdle, 1991 · Old Faithful data (R: faithful)")

        n1 = note("data", "bell").move_to([NX, ROW1, 0])
        n2 = note("bell", "data").move_to([NX, ROW2, 0])
        r1 = bits_readout(D["A"]["fwd"]).next_to(n1, RIGHT, buff=0.35)
        r2 = bits_readout(D["A"]["rev"]).next_to(n2, RIGHT, buff=0.35)
        crown = self.pt(MA, D["qA_peak"])
        # the three places the closest bell could go when the order flips
        pk = D["qB_peak"]
        ghost2 = self.bell_shape(MU[0], SB, width=3, opacity=0.6, dashed=True)
        ghost3 = self.bell_shape(MB, SB, width=3, opacity=0.6, dashed=True)
        mk1 = MathTex("1", font_size=44, color=YELLOW).next_to(crown, UP, buff=0.2)
        mk2 = MathTex("2", font_size=44, color=YELLOW).next_to(self.pt(MU[0], pk), UP, buff=0.2)
        mk3 = MathTex("3", font_size=44, color=YELLOW).next_to(self.pt(MB, pk), UP, buff=0.2)

        static_p = self.make_pcurve()
        self.add(self.ax, bars)
        with self.narrate("Old Faithful's eruptions. [pause 0.12] Data first, the closest bell is "
                          "this one. [pause 0.2] Swap the order. If closeness is a distance, order "
                          "can't matter: it stays at one.", gap=0.35) as beat:
            # the order the bet is about is on screen from the first second
            self.play(self.bar_op.animate.set_value(0.42), Create(static_p), Write(n1),
                      FadeIn(n_lab, shift=0.1 * DOWN), FadeIn(cite_data),
                      run_time=beat.until("Data", offset=-0.15), rate_func=SMOOTH)
            self.swap_in(static_p, pcurve)
            self.play(Indicate(n1[1], color=YELLOW, scale_factor=1.25), run_time=0.8)
            beat.wait_until("closest", offset=-0.05)
            static_b = self.make_bell()
            self.play(Create(static_b), run_time=beat.until("one", offset=0.25))
            self.swap_in(static_b, bell)
            beat.wait_until("Swap", offset=-0.1)
            # the two arguments trade places, onto a second line
            self.play(TransformFromCopy(n1[0], n2[0]), TransformFromCopy(n1[2], n2[2]),
                      TransformFromCopy(n1[4], n2[4]),
                      TransformFromCopy(n1[1], n2[3], path_arc=-1.6),
                      TransformFromCopy(n1[3], n2[1], path_arc=-1.6), run_time=1.3)
            beat.wait_until("one", occurrence=2, offset=-0.2)
            self.play(FadeIn(mk1, shift=0.15 * DOWN), run_time=0.6)
        # the bet itself, one question, a touch slower (Kokoro rushes questions: 230 wpm at 0.83)
        with self.narrate("Or does the closest bell move to two, or to three? [pause 1.5]",
                          speed=0.77) as beat:
            beat.wait_until("two", offset=-0.15)
            self.play(Create(ghost2), FadeIn(mk2, shift=0.15 * DOWN), run_time=0.6)
            beat.wait_until("three", offset=-0.15)
            self.play(Create(ghost3), FadeIn(mk3, shift=0.15 * DOWN), run_time=0.6)
            self.play(Indicate(VGroup(mk1, mk2, mk3), color=YELLOW, scale_factor=1.15),
                      run_time=0.9)

        # ============================================================ 2. stakes
        kl_lab = text("KL divergence", size=LABEL).next_to(n1, LEFT, buff=0.4)
        dist_lab = text("a distance?", size=LABEL, color=YELLOW).next_to(n2, LEFT, buff=0.4)
        dist_lab.align_to(kl_lab, LEFT)
        cite_kl = citation("Kullback & Leibler, 1951 · Annals of Mathematical Statistics")
        cite_vi = citation("Blei et al., 2017 · J. American Statistical Association")
        vi_lab = text("variational inference", size=LABEL, color=GRAY)
        vi_lab.next_to(n2, DOWN, buff=0.25).align_to(n2, LEFT)
        ml_lab = text("maximum-likelihood fit", size=LABEL, color=PURPLE).move_to([crown[0], PIN_Y, 0])
        leader = DashedLine(crown + UP * 0.12, ml_lab.get_bottom() + DOWN * 0.15, dash_length=0.07,
                            stroke_color=PURPLE, stroke_width=2)
        with self.narrate("The D is KL divergence, named for Kullback and Leibler. [pause 0.2] "
                          "Every maximum-likelihood fit shrinks it with the data first. [pause 0.2] "
                          "Much of Bayesian machine learning shrinks it with the order flipped. "
                          "[pause 0.2] It's often called a distance.") as beat:
            self.play(FadeOut(VGroup(ghost2, ghost3, mk1, mk2, mk3, n_lab)),
                      n2.animate.set_opacity(0.3), Indicate(n1[0], color=YELLOW, scale_factor=1.25),
                      run_time=0.8)
            beat.wait_until("KL", offset=-0.15)
            self.play(FadeIn(kl_lab, shift=0.1 * RIGHT), run_time=0.7)
            beat.wait_until("Kullback", offset=-0.2)
            self.play(swap(cite_data, cite_kl), run_time=0.7)      # never superimposed
            beat.wait_until("maximum", offset=-0.1)
            self.play(FadeIn(ml_lab, shift=0.1 * UP), Create(leader), flag(n1), run_time=1.0)
            beat.wait_until("shrinks", offset=-0.1)
            self.play(self.flash_bell(run_time=0.7))
            beat.wait_until("data first", offset=-0.1)
            self.play(flag(n1[1]), run_time=0.7)
            # the stakes of the order: Bayesian approximations put the model first
            beat.wait_until("Bayesian", offset=-0.1)
            self.play(n2.animate.set_opacity(1.0), FadeIn(vi_lab, shift=0.1 * UP),
                      swap(cite_kl, cite_vi), run_time=0.8)
            beat.wait_until("flipped", offset=-0.15)
            self.play(flag(n2[1]), flag(n2[3]), run_time=0.8)
            beat.wait_until("distance", offset=-0.15)
            self.play(FadeIn(dist_lab, shift=0.1 * RIGHT), run_time=0.7)

        # ============================================================ 3. naive build
        num1 = r1.num
        num1.add_updater(lambda m: m.set_value(self.total(1)))
        a_lab = MathTex(r"A\!:\ 3.49 \pm 1.14\ \text{min}", font_size=36, color=PURPLE)
        a_lab.move_to(ml_lab)
        mean_line = DashedLine(self.pt(MA, 0), crown + DOWN * 0.02, dash_length=0.07,
                               stroke_color=PURPLE, stroke_width=2)
        dist_lab2 = text("a distance", size=LABEL, color=YELLOW).move_to(dist_lab, aligned_edge=LEFT)
        NV = D["naive"]
        # (A's mean and spread are on its label; the narration does not read them out)
        with self.narrate("So treat it as one. Data first, this bell is point seven six bits away. "
                          "[pause 0.5] Shift it or stretch it, and that number only grows, so bell A "
                          "is the closest.", gap=0.8) as beat:
            # the VI tag and its citation leave with the topic (the naive build cites nothing)
            self.play(TransformMatchingShapes(dist_lab, dist_lab2), FadeOut(vi_lab), FadeOut(cite_vi),
                      n2.animate.set_opacity(0.3), kl_lab.animate.set_opacity(0.35), run_time=0.8)
            beat.wait_until("Data first", offset=-0.1)
            self.play(flag(n1[1]), run_time=0.6)
            # "this bell": the bell flashes as its score appears beside the D-line
            beat.on("this bell", self.flash_bell(run_time=0.7), FadeIn(r1, shift=0.1 * LEFT),
                    run_time=0.7)
            beat.wait_until("Shift", offset=-0.15)
            # each excursion: out, hold and flag the raised number, back
            for tracker, val in ((self.mu, MA + NV["shift"]), (self.sd, SA * NV["stretch"])):
                home = tracker.get_value()
                self.play(tracker.animate.set_value(val), run_time=0.55, rate_func=SMOOTH)
                num1.suspend_updating()
                self.play(Indicate(num1, color=YELLOW, scale_factor=1.15), run_time=0.5)
                num1.resume_updating()
                self.play(tracker.animate.set_value(home), run_time=0.5, rate_func=SMOOTH)
            # "bell A": the pin completes and the label swaps (never superimposed) to A's stats
            beat.wait_until("bell A", offset=-0.2)
            self.play(Create(mean_line), swap(ml_lab, a_lab), run_time=0.9)
        num1.clear_updaters()
        num1.set_value(D["A"]["fwd"])

        # ============================================================ 4. fail
        times = MathTex(r"\times 2.2", font_size=36, color=YELLOW).next_to(r2, DOWN, buff=0.22)
        times.align_to(r2[1], LEFT)
        with self.narrate("But a distance reads the same both ways. [pause 0.15] Put the bell first, "
                          "and the same two curves are one point seven bits apart, more than twice "
                          "as far. [pause 1.0] Only the order changed, so the formula must care about "
                          "order.") as beat:
            self.play(n2.animate.set_opacity(1.0), flag(dist_lab2),
                      VGroup(a_lab, leader, mean_line).animate.set_opacity(0.3), run_time=0.9)
            beat.wait_until("bell first", offset=-0.1)
            self.play(flag(n2[1]), run_time=0.8)
            beat.wait_until("one point", offset=-0.15)
            self.play(FadeIn(r2, shift=0.1 * LEFT), run_time=0.7)
            beat.wait_until("twice", offset=-0.15)
            strike = Line(dist_lab2.get_left() + LEFT * 0.08, dist_lab2.get_right() + RIGHT * 0.08,
                          color=GRAY, stroke_width=3).set_y(dist_lab2.get_y() + 0.02)
            self.allow_overlap(dist_lab2, strike, reason="strike-through: the claim just refuted")
            self.play(FadeIn(times, shift=0.1 * DOWN), Indicate(r1.num, color=YELLOW),
                      Indicate(r2.num, color=YELLOW), dist_lab2.animate.set_color(GRAY),
                      Create(strike), run_time=1.0)
            beat.wait_until("order changed", offset=-0.1)
            bx = VGroup(box(n1, buff=0.12), box(n2, buff=0.12))
            self.play(FadeIn(bx, scale=1.05), run_time=0.6)     # whole boxes, never drawn from a corner
            beat.wait_until("formula", offset=-0.2)
            self.play(FadeOut(bx), run_time=0.5)

        # ============================================================ 5. insight: one length
        lhs = n1
        pq_bars = self.redraw(self.make_pq_bars, self.scan, self.pq_op, self.p_h, self.q_h,
                              self.mu, self.sd, self.sm_r, self.sm_c)
        scanner = self.make_scanner()

        rp = self.readout("p", BLUE, lambda: self.p_at(self.scan.get_value()), Y_RP)
        rq = self.readout("q", PURPLE, lambda: self.q_at(self.scan.get_value()), Y_RQ)
        lr_lab = MathTex(r"\log_2", r"\frac{p}{q}", "=", font_size=40)
        lr_lab[0].set_color(RED)
        fr = sorted(lr_lab[1].submobjects, key=lambda s: -s.get_center()[1])
        fr[0].set_color(BLUE)
        fr[2].set_color(PURPLE)
        lr_num = DecimalNumber(1.98, num_decimal_places=2, font_size=40, color=RED)
        lr = VGroup(lr_lab, lr_num).arrange(RIGHT, buff=0.18).move_to([RX, Y_LR, 0])
        lr_state = {"dim": False}

        def upd_lr(m):
            m.set_value(math.log2(max(self.p_at(self.scan.get_value()), 1e-300)
                                  / max(self.q_at(self.scan.get_value()), 1e-300)))
            k = self.ro_op.get_value()            # dims with the p / q readouts
            if k < 0.999 or lr_state["dim"]:
                m.set_opacity(k)
                lr_state["dim"] = k < 0.999
        lr_num.add_updater(upd_lr)
        for g in (rp, rq):
            g.align_to(lr, LEFT)

        # the pulled-out pair: same baseline and scale as the chart, room to stack
        base_y = MID[1]
        yu_mid = MID[3]
        p2, q2 = D["at_2min"]["A"]["p"], D["at_2min"]["A"]["q"]
        big_p = Rectangle(width=PW, height=p2 * yu_mid, stroke_width=0, fill_color=BLUE,
                          fill_opacity=0.9).move_to([PX, base_y, 0], aligned_edge=DOWN)
        big_q = Rectangle(width=PW, height=q2 * yu_mid, stroke_width=0, fill_color=PURPLE,
                          fill_opacity=0.9).move_to([QX, base_y, 0], aligned_edge=DOWN)
        base_line = Line([PX - 0.65, base_y, 0], [QX + 0.65, base_y, 0], color=GRAY,
                         stroke_width=2.5)
        p_sym = MathTex("p", font_size=40, color=BLUE).next_to(big_p, LEFT, buff=0.18)
        q_sym = MathTex("q", font_size=40, color=PURPLE).next_to(big_q, RIGHT, buff=0.2)
        hq = big_q.height

        with self.narrate("To see why, take one eruption two minutes long. The data's curve stands "
                          "this high there: call it p. [pause 0.45] The bell gives it q, [pause 0.3] "
                          "about a quarter as much. Double q twice and you reach p. [pause 0.45] So log "
                          "base two of p over q is about two: two doublings, or two bits.") as beat:
            # numbers leave first, then the chart shrinks (nothing slides over a label)
            self.play(FadeOut(VGroup(kl_lab, dist_lab2, strike, n2, r2, times, a_lab, leader,
                                     mean_line, r1)), run_time=0.4)
            # the pull-out's empty baseline is drawn as the chart makes room: the right side has a
            # destination before p arrives (it starts once the chart's right end has passed it)
            rt = beat.until("two minutes", offset=-0.15, min_time=1.0)
            self.play(*self.to_layout(MID), self.move_axes(MID),
                      lhs.animate.scale(40 / 36).move_to([RX, 3.2, 0]),
                      self.bar_op.animate.set_value(0.1),
                      Succession(Wait(0.7 * rt), Create(base_line, run_time=0.3 * rt)),
                      run_time=rt, rate_func=SMOOTH)
            self.play(Indicate(self.ax.x_axis.numbers[1], color=YELLOW, scale_factor=1.4),
                      run_time=0.6)
            self.scan.set_value(2.0)
            scanner.update()
            self.play(Create(scanner), run_time=0.6)
            self.add(pq_bars)
            # "this high": the data's bar rises at the scanner as the word lands
            beat.wait_until("this high", offset=-0.3)
            self.play(self.p_h.animate.set_value(1.0), run_time=0.6)
            self.play(TransformFromCopy(pq_bars[0], big_p), FadeIn(p_sym),
                      FadeIn(rp, shift=0.1 * LEFT), run_time=0.8)
            beat.wait_until("gives it q", offset=-0.25)
            self.play(self.q_h.animate.set_value(1.0), run_time=0.6)
            self.play(TransformFromCopy(pq_bars[1], big_q), FadeIn(q_sym),
                      FadeIn(rq, shift=0.1 * LEFT), run_time=0.8)
            beat.wait_until("Double", offset=-0.1)
            c1 = big_q.copy().set_fill(opacity=0.55)
            self.add(c1)
            self.play(c1.animate.shift(UP * hq), run_time=0.6)
            x2a = MathTex(r"\times 2", font_size=36, color=YELLOW).next_to(c1, RIGHT, buff=0.2)
            self.play(FadeIn(x2a, shift=0.1 * LEFT), run_time=0.4)
            c2 = VGroup(big_q.copy().set_fill(opacity=0.55), c1.copy())
            self.add(c2)
            self.play(c2.animate.shift(UP * 2 * hq), run_time=0.6)
            x2b = MathTex(r"\times 2", font_size=36, color=YELLOW).next_to(c2, RIGHT, buff=0.2)
            reach = DashedLine([PX - PW / 2 - 0.1, big_p.get_top()[1], 0],
                               [QX + PW / 2 + 0.1, big_p.get_top()[1], 0], dash_length=0.08,
                               color=YELLOW, stroke_width=3)
            self.play(FadeIn(x2b, shift=0.1 * LEFT), Create(reach), run_time=0.5)
            beat.wait_until("log base", offset=-0.1)
            # p swings up from its bar, around the left of the pull-out; q drops from its readout
            self.play(TransformFromCopy(p_sym, fr[0], path_arc=2.2), run_time=0.8)
            self.play(TransformFromCopy(rq[0][0], fr[2]), FadeIn(fr[1]), run_time=0.7)
            self.play(FadeIn(lr_lab[0]), FadeIn(lr_lab[2]), FadeIn(lr_num), run_time=0.5)
            beat.wait_until("two doublings", offset=-0.1)
            self.pulse(lr_num, extra=(Indicate(x2a, color=YELLOW), Indicate(x2b, color=YELLOW)))
        pullout = VGroup(big_p, big_q, base_line, p_sym, q_sym, c1, c2, x2a, x2b, reach)

        # ============================================================ 6. every length, weighted
        f_fwd = rhs("p", "p", "q", size=BLK)
        tot = bits_readout(D["A"]["fwd"], size=BLK)
        lhs_target = note("data", "bell", size=BLK)
        place_block(lhs_target, f_fwd, tot, ROWS_TWO)
        ax_b1 = bill_axes(*B1_TWO)
        unit1 = bill_unit(*B1_TWO, s="bits")
        unit1b = bill_unit(*B1_TWO)
        xlab = x_labels(B1_TWO[0] + B_LO * B1_TWO[1])
        area = self.redraw(lambda: self.make_area(1), self.mu, self.sd, self.sm_r, self.sm_c,
                           self.weighted, self.reveal, self.fill_reveal, self.area_fill,
                           self.area_op)
        tot_num = tot.num
        refund = text("refund", size=LABEL, color=GRAY)

        # where log2(p/q) runs off the bottom of the panel: say how far it really goes
        LRD = D["log2_p_over_qA"]
        cuts = LRD["crosses_minus1_at"]                 # [1.461, 2.444, 3.588, 5.229]
        clip_specs = [((0.0 + cuts[0]) / 2, 0.0, r"\downarrow\,%d" % round(LRD["at_0"])),
                      (3.03, cuts[1], r"\downarrow\,%.1f" % LRD["gap_min"][1]),
                      ((cuts[3] + 7.0) / 2, cuts[3], r"\downarrow\,%d" % round(LRD["at_7"]))]
        clip_marks = VGroup()
        for xc, x0, tex in clip_specs:
            mk = MathTex(tex, font_size=28, color=GRAY).move_to(
                [TWO[0] + TWO[2] * xc, B1_TWO[0] - 0.5 * B1_TWO[1], 0])
            mk.x0 = x0
            mk.add_updater(lambda m: m.set_opacity(
                float(np.clip((self.reveal.get_value() - m.x0) / 0.3, 0, 1))
                * (1 - self.weighted.get_value()) * self.area_op.get_value()))
            clip_marks.add(mk)

        # the one-length numbers and the chart's own x labels leave first, so nothing slides
        # through the bill's panel while the chart moves up (a silent beat turn)
        self.play(FadeOut(pullout), FadeOut(lhs), self.ax.x_axis.numbers.animate.set_opacity(0),
                  self.ax.x_title.animate.set_opacity(0), run_time=0.3)
        # the chart rises; the scanner rides along back to the left end, and the readouts (which
        # describe 2 min only) dim while it is away
        self.play(*self.to_layout(TWO), self.move_axes(TWO, xlab=False),
                  self.bar_op.animate.set_value(0.25), self.scan.animate.set_value(0.3),
                  self.ro_op.animate.set_value(0.3), lr_lab.animate.set_opacity(0.3),
                  run_time=0.8, rate_func=SMOOTH)
        with self.narrate("Do that at every length. [pause 0.9] Then weight each by p, how often "
                          "eruptions last that long, and add it all up. [pause 0.3] Where the bell "
                          "rises above the data, [pause 0.45] the grey dips pay a little back. "
                          "[pause 0.5] That's the divergence: the same point seven six.", gap=0.9) as beat:
            # the bill's panel draws in the room the chart left
            self.play(Create(ax_b1), FadeIn(unit1), FadeIn(xlab),
                      self.bot_scan_op.animate.set_value(1.0), run_time=0.5)
            self.reveal.set_value(0.3)
            self.add(area, clip_marks)
            # the sweep runs over "every length" and the pause after it; log2 and the ratio fly
            # into the formula row (carried, never morphed glyph by glyph)
            Ts = beat.until("Then", offset=-0.1, min_time=1.2)
            tf = max(0.6, min(1.4, Ts - 0.4))
            self.play(self.scan.animate(rate_func=LINEAR, run_time=Ts).set_value(7.0),
                      self.reveal.animate(rate_func=LINEAR, run_time=Ts).set_value(7.0),
                      Succession(Wait(0.3), allow_morph(TransformFromCopy(lr_lab[0], f_fwd[2],
                                                                          run_time=tf)),
                                 Wait(max(0.01, Ts - 0.3 - tf))),
                      Succession(Wait(0.3), carry(lr_lab[1], VGroup(*f_fwd[3:8]), run_time=tf),
                                 Wait(max(0.01, Ts - 0.3 - tf))))
            # "weight each one": the scanner leaves and the curve is multiplied by p
            self.play(self.scan_op.animate.set_value(0.0), self.pq_op.animate.set_value(0.0),
                      self.weighted.animate.set_value(1.0), swap(unit1, unit1b),
                      run_time=beat.until("by p", offset=-0.3, min_time=0.8), rate_func=SMOOTH)
            self.scan.set_value(2.0)
            self.remove(clip_marks)
            # "by p": the weight p swings out around the readouts' left edge into the formula
            self.play(TransformFromCopy(rp[0][0], f_fwd[1], path_arc=-1.7), run_time=0.7)
            # "how often eruptions last that long": the flash runs along the data's humps
            self.play(self.flash_p(), run_time=1.0)
            beat.wait_until("add it", offset=-0.1)
            tot_num.set_value(0.0)
            # the running total has its subject from the start (faint until it is named)
            lhs_target.set_opacity(0.35)
            self.play(Write(f_fwd[0]), Write(f_fwd[8]), FadeIn(tot), FadeIn(lhs_target), run_time=0.6)
            tot_num.add_updater(lambda m: m.set_value(self.total(1, upto=self.fill_reveal.get_value())))
            self.fill_reveal.set_value(0.0)
            self.area_fill.set_value(1.0)
            self.play(self.fill_reveal.animate.set_value(7.0), run_time=1.4, rate_func=LINEAR)
            tot_num.clear_updaters()
            tot_num.add_updater(lambda m: m.set_value(self.total(1)))
            beat.wait_until("grey dips", offset=-0.15)
            dip_x = 3.55
            refund.move_to(self.bp(1, dip_x, -0.72))
            self.play(FadeIn(refund, shift=0.1 * UP), run_time=0.6)
            beat.wait_until("divergence", offset=-0.15)
            self.play(lhs_target.animate.set_opacity(1.0), run_time=0.6)
            beat.wait_until("point seven", offset=-0.15)
            self.pulse(tot_num, run_time=0.8)
        lhs = lhs_target

        # ============================================================ 7. a bell that skips a hump
        ghost = self.redraw(self.make_ghost, self.a_op, self.a_solid, self.a_fill, self.a_fill_x,
                            self.a_w)
        lab_A = MathTex("A", font_size=36, color=PURPLE)
        lab_A.add_updater(lambda m: m.next_to(
            self.pt(1.1, self.q_at(1.1, MA, SA)), UL, buff=0.22).set_opacity(
            min(1.0, self.a_op.get_value() + 0.2) * self.lab_a_op.get_value()))
        lab_B = MathTex("B", font_size=36, color=PURPLE)

        def upd_b(m):
            mu, sd = self.mu.get_value(), self.sd.get_value()
            near = abs(mu - MB) + abs(math.log(sd / SB))
            m.next_to(self.pt(mu + 0.55 * sd, self.q_at(mu + 0.55 * sd)), UR, buff=0.18)
            m.set_opacity(float(np.clip(1.0 - near / 0.25, 0.0, 1.0)) * self.lab_b_op.get_value())
        lab_B.add_updater(upd_b)
        short_box = Rectangle(width=1.3 * TWO[2], height=0.76 * TWO[3], color=YELLOW,
                              stroke_width=3).move_to(
            [TWO[0] + TWO[2] * 2.0, TWO[1] + 0.38 * TWO[3], 0])
        pct = MathTex(r"36\%", font_size=36, color=YELLOW).next_to(short_box, LEFT, buff=0.15)
        pct.shift(0.22 * UP)                                    # clear of A's tail label
        ptag = self.peak_tag()
        with self.narrate("Try a bell that skips the short eruptions. At two minutes, it falls short "
                          "by eighteen and a half doublings. [pause 0.6] More than a third of all "
                          "eruptions are short, so the bill comes to five point eight bits.",
                          gap=1.1, speed=0.8) as beat:
            self.add(ghost, lab_A, lab_B, ptag)
            lab_A.update()
            lab_B.update()
            self.play(self.scan_op.animate.set_value(1.0), self.pq_op.animate.set_value(0.9),
                      self.ro_op.animate.set_value(1.0), lr_lab.animate.set_opacity(1.0),
                      self.a_op.animate.set_value(0.5), FadeOut(refund), run_time=0.6)
            self.play(self.mu.animate.set_value(MB), self.sd.animate.set_value(SB),
                      run_time=beat.until("two minutes", offset=-0.3), rate_func=SMOOTH)
            beat.wait_until("eighteen", offset=-0.15)
            self.pulse(lr_num, rq)
            beat.wait_until("More than", offset=-0.1)
            self.play(Create(short_box), FadeIn(pct, shift=0.1 * RIGHT), run_time=0.9)
            beat.wait_until("bill", offset=-0.1)
            self.pulse(tot_num, extra=(self.peak_op.animate.set_value(1.0),), run_time=1.0)

        # ============================================================ 8. keep that bill, swap for a second
        ax_b1_3 = bill_axes(*B1_THREE, sparse=True, lo=B3_LO)
        b1_nums = ax_b1_3.y_axis.numbers           # tick labels fade, never morph into other numerals
        ax_b1_3.y_axis.remove(b1_nums)
        ax_b2 = bill_axes(*B2_THREE, sparse=True, lo=B3_LO).set_opacity(0.3)
        unit1_3 = bill_unit(*B1_THREE)
        # (one unit label serves the stacked pair: both bills share one scale)
        # which bill is which, in each panel's own corner
        ord1 = order_tag(*B1_THREE, "data")
        ord2 = order_tag(*B2_THREE, "bell").set_opacity(0.3)
        xlab_p1 = x_labels(B1_THREE[0] + B3_LO * B1_THREE[1])   # under the data-first bill, for now
        xlab3 = x_labels(B2_THREE[0] + B3_LO * B2_THREE[1], side=True)
        area2 = self.redraw(lambda: self.make_area(2), self.mu, self.sd, self.sm_r, self.sm_c,
                            self.fill2_reveal, self.area2_op)
        block1 = VGroup(lhs, f_fwd, tot)
        tgt1 = block1.copy()
        place_block(tgt1[0], tgt1[1], tgt1[2], ROWS1_THREE)
        # the second block: the first one's formula with its result unknown ("= ?" from the start)
        lhs2 = note("data", "bell", size=BLK)
        f2 = rhs("p", "p", "q", size=BLK)
        q_tot = MathTex("=", r"?", font_size=BLK)
        q_tot[1].set_color(YELLOW).shift(0.14 * RIGHT)       # "= ?" spaced like "= 5.77"
        place_block(lhs2, f2, q_tot, ROWS2_THREE)
        lhs_r = note("bell", "data", size=BLK).move_to(lhs2, aligned_edge=LEFT)
        f_rev = rhs("q", "q", "p", size=BLK).move_to(f2, aligned_edge=LEFT)
        # the chart's own key, beside the chart where the p / q readouts stood: the two contenders
        # with their mean and spread (so "less than half as wide" can be read off: 0.44 vs 1.14)
        key_a = MathTex(r"A\!:\ 3.49 \pm", r"1.14", r"\ \text{min}", font_size=BLK, color=PURPLE)
        key_b = MathTex(r"B\!:\ 4.27 \pm", r"0.44", r"\ \text{min}", font_size=BLK, color=PURPLE)
        key = VGroup(key_a, key_b).arrange(DOWN, aligned_edge=LEFT, buff=0.34)
        key.move_to([2.15, THREE[1] + 0.62 * THREE[3], 0], aligned_edge=LEFT)
        with self.narrate("Now keep that bill. [pause 0.12] For a second bill, swap the order: "
                          "[pause 0.2] every p trades places with q. [pause 0.3] The bell supplies the "
                          "lengths, and the data judges them. [pause 0.5] Which bell wins now? "
                          "[pause 1.5]") as beat:
            # readouts, markers and the bill's tick labels leave first, then the panels make room
            self.play(FadeOut(VGroup(rp, rq, lr, short_box, pct, ax_b1.y_axis.numbers)),
                      self.pq_op.animate.set_value(0.0), self.scan_op.animate.set_value(0.0),
                      run_time=0.35)
            ax_b1.y_axis.remove(ax_b1.y_axis.numbers)
            self.remove(pq_bars, scanner)
            tot_num.clear_updaters()
            self.play(*self.to_layout(THREE), self.move_axes(THREE, xlab=False),
                      self.b1y.animate.set_value(B1_THREE[0]), self.b1u.animate.set_value(B1_THREE[1]),
                      ReplacementTransform(ax_b1, ax_b1_3), ReplacementTransform(unit1b, unit1_3),
                      ReplacementTransform(xlab, xlab_p1), Transform(block1, tgt1),
                      self.a_solid.animate.set_value(1.0), self.a_op.animate.set_value(1.0),
                      FadeIn(key, shift=0.1 * LEFT),
                      run_time=beat.until("swap", offset=-0.45, min_time=0.85), rate_func=SMOOTH)
            tot_num.add_updater(lambda m: m.set_value(self.total(1)))
            # the copy appears once the first block has moved clear of its rows
            self.play(FadeIn(b1_nums), FadeIn(ord1), FadeIn(VGroup(lhs2, f2, q_tot), shift=0.1 * DOWN),
                      run_time=0.35)
            beat.wait_until("swap", offset=-0.1)
            # one move: the arguments trade places and every p trades places with q, together,
            # so no frame pairs the new order with the old integrand
            self.play(ReplacementTransform(lhs2[0], lhs_r[0]), ReplacementTransform(lhs2[2], lhs_r[2]),
                      ReplacementTransform(lhs2[4], lhs_r[4]),
                      ReplacementTransform(lhs2[1], lhs_r[3], path_arc=-1.3),
                      ReplacementTransform(lhs2[3], lhs_r[1], path_arc=-1.3),
                      *[ReplacementTransform(f2[i], f_rev[i]) for i in (0, 2, 3, 5, 7, 8)],
                      swap(f2[1], f_rev[1]),          # the weight p -> q: no glyph morph
                      ReplacementTransform(f2[4], f_rev[6], path_arc=-2.0),
                      ReplacementTransform(f2[6], f_rev[4], path_arc=-2.0), run_time=1.6)
            beat.wait_until("places", offset=-0.1)
            self.play(*[Indicate(f_rev[i], color=YELLOW, scale_factor=1.3) for i in (1, 4, 6)],
                      run_time=0.8)
            # the bell is the one doing the sampling: both bells pulse (stroke + fill) on "supplies"
            self.a_fill_x.set_value(7.0)
            self.bell_fill_x.set_value(7.0)
            beat.wait_until("supplies", offset=-0.15)
            self.play(*[tr.animate(rate_func=there_and_back).set_value(v) for tr, v in
                        ((self.bell_w, 6.5), (self.a_w, 6.5), (self.bell_fill, 0.35),
                         (self.a_fill, 0.35))], run_time=0.9)
            # ...and the data curve on "judges"
            beat.wait_until("judges", offset=-0.15)
            self.play(self.p_w.animate(rate_func=there_and_back).set_value(6.5),
                      self.p_fill.animate(rate_func=there_and_back).set_value(0.35), run_time=0.9)
            # the empty bell-first panel appears as the question is asked
            beat.wait_until("Which", offset=-0.1)
            # the shared x numbers drop to the new lowest panel; the axis name fades out and back in
            # at its new place (moving, it would fly through the second formula block)
            self.play(FadeIn(ax_b2), FadeIn(ord2), ReplacementTransform(xlab_p1[0], xlab3[0]),
                      swap(xlab_p1[1], xlab3[1], run_time=0.9),
                      Indicate(lab_A, color=YELLOW), Indicate(lab_B, color=YELLOW), run_time=0.9)
            self.remove(xlab3[0], xlab3[1])
            self.add(xlab3)

        # ============================================================ 9. B then A, bell first
        self.add(area2)
        tot2 = bits_readout(D["B"]["rev"], size=BLK)
        place_block(lhs_r.copy(), f_rev.copy(), tot2, ROWS2_THREE)
        free_box = DashedVMobject(Rectangle(width=1.1 * TWO[2], height=0.8,
                                            color=YELLOW, stroke_width=2.5).move_to(
            [TWO[0] + TWO[2] * 2.0, B2_THREE[0] + 0.25, 0]), num_dashes=36)
        gap_box = Rectangle(width=1.0 * TWO[2], height=2.2 * B2_THREE[1], color=YELLOW,
                            stroke_width=2.5).move_to(
            [TWO[0] + TWO[2] * 2.9, B2_THREE[0] + 0.95 * B2_THREE[1], 0])
        tail_boxes = VGroup(*[Rectangle(width=0.8 * TWO[2], height=0.32, color=YELLOW,
                                        stroke_width=2.5).move_to(
            [TWO[0] + TWO[2] * x, B2_THREE[0] + 0.12, 0]) for x in (0.6, 6.5)])
        tot2_num = tot2.num
        with self.narrate("Take bell B first. [pause 0.15] It almost never imagines a short eruption, "
                          "so ignoring them costs nothing. [pause 0.12] It pays point six two. "
                          "[pause 0.9] Bell A imagines eruptions in the gap and the tails, where the "
                          "data has almost none. [pause 0.2] That's its one point seven.",
                          gap=0.5) as beat:
            self.area2_op.set_value(1.0)
            self.fill2_reveal.set_value(0.0)
            tot2_num.set_value(0.0)
            self.play(FadeOut(q_tot[1]), run_time=0.25)       # the "?" leaves before the number
            self.play(self.a_solid.animate.set_value(0.0), self.a_op.animate.set_value(0.5),
                      self.bell_fill.animate.set_value(0.28), ax_b2.animate.set_opacity(1.0),
                      ord2.animate.set_opacity(1.0),
                      ReplacementTransform(q_tot[0], tot2[0]),
                      FadeIn(tot2[1:]), Indicate(lab_B, color=YELLOW), run_time=0.8)
            tot2_num.add_updater(lambda m: m.set_value(self.total(2, upto=self.fill2_reveal.get_value())))
            self.play(self.fill2_reveal.animate.set_value(7.0),
                      run_time=beat.until("short eruption", offset=-0.1), rate_func=LINEAR)
            tot2_num.clear_updaters()
            tot2_num.add_updater(lambda m: m.set_value(self.total(2)))
            self.play(Create(free_box), run_time=0.8)
            beat.wait_until("pays", offset=-0.1)
            self.pulse(tot2_num, run_time=0.8)
            beat.wait_until("Bell A", offset=-0.1)
            self.play(FadeOut(free_box), self.mu.animate.set_value(MA), self.sd.animate.set_value(SA),
                      run_time=beat.until("gap", offset=-0.1), rate_func=SMOOTH)
            self.play(Create(gap_box), run_time=0.6)
            beat.wait_until("tails", offset=-0.1)
            self.play(Create(tail_boxes), run_time=0.6)
            beat.wait_until("That's its", offset=-0.1)
            self.pulse(tot2_num, extra=(FadeOut(VGroup(gap_box, tail_boxes)),))

        # ============================================================ 10. slide downhill
        t = ValueTracker(0.0)

        def follow(path, tr):
            def f(_):
                k = tr.get_value() * (len(path) - 1)
                i = min(int(k), len(path) - 2)
                fr_ = k - i
                self.mu.set_value((1 - fr_) * path[i, 0] + fr_ * path[i + 1, 0])
                self.sd.set_value(math.exp((1 - fr_) * math.log(path[i, 1])
                                           + fr_ * math.log(path[i + 1, 1])))
            return f

        crown_a3 = np.array([THREE[0] + THREE[2] * MA, THREE[1] + THREE[3] * D["qA_peak"], 0])
        crown_b3 = np.array([THREE[0] + THREE[2] * MB, THREE[1] + THREE[3] * D["qB_peak"], 0])
        crown_g2 = np.array([THREE[0] + THREE[2] * MU[0], THREE[1] + THREE[3] * D["qB_peak"], 0])
        m1b = MathTex("1", font_size=40, color=YELLOW).next_to(crown_a3, UP, buff=0.2)
        m3b = MathTex("3", font_size=40, color=YELLOW).next_to(crown_b3, UP, buff=0.2)
        # "2" sits left of its crown: above it is the chart's y-axis title
        m2b = MathTex("2", font_size=40, color=YELLOW).next_to(crown_g2, LEFT, buff=0.42)
        m2b.set_opacity(0.4)
        moved = CurvedArrow(m1b.get_top() + UP * 0.26, m3b.get_left() + LEFT * 0.17, angle=-0.6,
                            color=YELLOW, stroke_width=4, tip_length=0.18)
        # both integrals have been read: each block collapses to its D-line and total, centred
        # on its own bill, so the frame is the bell and its two bills (in the beat turn)
        tot_num.suspend_updating()
        tot2_num.suspend_updating()
        row1, row2 = VGroup(lhs, tot), VGroup(lhs_r, tot2)
        self.play(FadeOut(f_fwd), FadeOut(f_rev), row1.animate.shift((MID1_THREE - lhs.get_y()) * UP),
                  row2.animate.shift((MID2_THREE - lhs_r.get_y()) * UP), run_time=0.7)
        tot_num.resume_updating()
        tot2_num.resume_updating()
        with self.narrate("Now let bell A slide downhill on the bell-first bill. [pause 0.12] As that "
                          "bill drains, the other swells, and the bell settles into B, less than half "
                          "as wide. [pause 0.3] Flip the order, and the closest bell moves to three. "
                          "[pause 1.2]", gap=0.45) as beat:
            beat.wait_until("bell A", offset=-0.15)
            self.play(Indicate(lab_A, color=YELLOW), self.flash_bell(MA, SA), run_time=0.6)
            driver = Mobject()
            driver.add_updater(follow(PATH, t))
            self.add(driver)
            T = beat.until("settles", offset=0.4)
            t_drain = beat.until("drains", offset=-0.2)
            t_swell = beat.until("swells", offset=-0.2)
            self.play(t.animate(rate_func=SMOOTH, run_time=T).set_value(1.0),
                      Succession(Wait(t_drain), Indicate(lhs_r, color=YELLOW, scale_factor=1.08,
                                                         run_time=0.8), Wait(T - t_drain - 0.8)),
                      Succession(Wait(t_swell), Indicate(lhs, color=YELLOW, scale_factor=1.08,
                                                         run_time=0.8), Wait(T - t_swell - 0.8)))
            driver.clear_updaters()
            self.remove(driver)
            # "less than half as wide": the two spreads in the key, side by side
            beat.wait_until("less", offset=-0.1)
            self.play(Indicate(key_b[1], color=YELLOW, scale_factor=1.25),
                      Indicate(key_a[1], color=YELLOW, scale_factor=1.25), run_time=0.9)
            # the cold-open picture returns: the same dashed ghosts, B now sitting exactly in 3
            ghost2b = self.bell_shape(MU[0], SB, width=3, opacity=0.25, dashed=True)
            ghost3b = self.bell_shape(MB, SB, width=3, opacity=0.6, dashed=True)
            beat.wait_until("Flip", offset=-0.15)
            self.play(Create(ghost2b), Create(ghost3b), FadeIn(m1b, shift=0.1 * DOWN),
                      FadeIn(m2b, shift=0.1 * DOWN), run_time=0.7)
            self.play(Create(moved), run_time=beat.until("three", offset=-0.1, min_time=0.6))
            self.play(FadeIn(m3b, scale=1.3), Indicate(ghost3b, color=YELLOW, scale_factor=1.0),
                      run_time=0.6)
        tot2_num.clear_updaters()
        tot_num.clear_updaters()

        # ============================================================ 11. payoff
        LEG_X = -1.25                              # clear of the y-axis title (ends at -2.09)
        to_a = MathTex(r"\to\ A", font_size=36, color=PURPLE)
        to_b = MathTex(r"\to\ B", font_size=36, color=PURPLE)
        legend1 = VGroup(note("data", "bell"), text("maximum likelihood", size=LABEL), to_a)
        legend2 = VGroup(note("bell", "posterior"), text("variational inference", size=LABEL), to_b)
        for lg in (legend1, legend2):
            lg.arrange(RIGHT, buff=0.2)
        legend1.move_to([LEG_X, 3.38, 0], aligned_edge=LEFT)     # high: the yellow 3 stays on
        legend2.move_to([LEG_X, 2.74, 0], aligned_edge=LEFT)     # B's crown under row 2
        legend1[1].align_to(legend2[1], LEFT)
        legend1[2].next_to(legend1[1], RIGHT, buff=0.2)
        TAG_L, TAG_Y = 2.45, -0.3                  # blue tag, right of the long hump (full layout)
        tag_data = text("data", size=LABEL, color=BLUE)
        tag_data.move_to([TAG_L, TAG_Y, 0], aligned_edge=LEFT)
        tag_post = text("if this were a posterior", size=LABEL, color=BLUE)
        tag_post.move_to([TAG_L, TAG_Y, 0], aligned_edge=LEFT)
        cite_blei = citation("Blei et al., 2017 · J. American Statistical Association")
        cite_bishop = citation("Bishop, 2006 · Pattern Recognition and Machine Learning, §10.1")
        # (the integral lines already left in beat 10; the yellow 3 stays on B's crown)
        bill_stuff = VGroup(lhs, tot, lhs_r, tot2, key, m1b, m2b, moved, ghost2b,
                            ghost3b, xlab3, unit1_3, ord1, ord2, ax_b1_3, b1_nums, ax_b2)
        with self.narrate("Maximum likelihood puts the data first, so a one-bell fit stretches over "
                          "every hump. [pause 0.5] Variational inference approximates a Bayesian "
                          "posterior with the model first, so it tends to settle on one hump.") as beat:
            # first everything that belonged to the bills leaves, chart at full strength (the answer,
            # the yellow 3, rides B's crown through the regrowth)...
            m3b.add_updater(lambda m: m.next_to(self.pt(MB, D["qB_peak"]), UP, buff=0.2 - 0.03 * float(
                np.clip((self.yu.get_value() - THREE[3]) / (FULL[3] - THREE[3]), 0, 1))))
            self.play(FadeOut(bill_stuff), self.area_op.animate.set_value(0.0),
                      self.area2_op.animate.set_value(0.0), self.peak_op.animate.set_value(0.0),
                      run_time=0.4)
            self.remove(area, area2, ptag)
            # ...then the chart alone grows back to full size
            self.play(*self.to_layout(FULL), self.move_axes(FULL),
                      self.bell_fill.animate.set_value(0.0), self.bar_op.animate.set_value(0.42),
                      run_time=beat.until("data first", offset=-0.25, min_time=0.9), rate_func=SMOOTH)
            beat.wait_until("data first", offset=-0.2)
            self.play(FadeIn(legend1[:2], shift=0.1 * DOWN), FadeIn(cite_bishop),
                      FadeIn(tag_data, shift=0.1 * RIGHT), run_time=0.8)
            beat.wait_until("stretches", offset=-0.2)
            # maximum likelihood's bell is the focus: A solid, its fill sweeping over both humps
            self.a_fill.set_value(0.25)
            self.a_fill_x.set_value(0.0)
            self.play(self.a_solid.animate.set_value(1.0), self.a_op.animate.set_value(1.0),
                      self.bell_op.animate.set_value(0.3), self.lab_b_op.animate.set_value(0.3),
                      run_time=0.5)
            self.play(self.a_fill_x.animate.set_value(7.0), FadeIn(to_a, shift=0.1 * RIGHT),
                      run_time=1.1, rate_func=SMOOTH)
            beat.wait_until("posterior", offset=-0.15)
            # the curve is read as a posterior only hypothetically; the eruption axes step back
            self.play(FadeOut(tag_data), self.bar_op.animate.set_value(0.25),
                      self.ax.x_title.animate.set_opacity(0.3), self.ax.y_title.animate.set_opacity(0.3),
                      run_time=0.3)
            self.play(Write(tag_post), FadeIn(legend2[:2], shift=0.1 * DOWN),
                      legend1.animate.set_opacity(0.3), run_time=0.7)
            beat.wait_until("model first", offset=-0.15)
            self.play(Indicate(legend2[0][1], color=YELLOW), run_time=0.7)
            beat.wait_until("settle", offset=-0.15)
            self.bell_fill_x.set_value(0.0)
            self.bell_fill.set_value(0.25)
            self.play(self.a_solid.animate.set_value(0.0), self.a_op.animate.set_value(0.5),
                      self.a_fill.animate.set_value(0.0), self.bell_op.animate.set_value(1.0),
                      self.lab_b_op.animate.set_value(1.0), FadeIn(to_b, shift=0.1 * RIGHT),
                      self.bell_fill_x.animate.set_value(7.0), run_time=1.1, rate_func=SMOOTH)
        m3b.clear_updaters()

        # what "underestimates" looks like here (+-1 SD brackets), then a measured real case
        Apm, Bpm = D["A_pm_sd"], D["B_pm_sd"]
        br_P = bracket(self.pt(Apm[0], 0.12), self.pt(Apm[1], 0.12), color=BLUE)
        br_B = bracket(self.pt(Bpm[0], 0.72), self.pt(Bpm[1], 0.72), color=PURPLE)
        l114 = MathTex(r"\pm 1.14", font_size=36, color=BLUE).move_to(self.pt(3.0, 0.215))
        l044 = MathTex(r"\pm 0.44", font_size=36, color=PURPLE).next_to(br_B, LEFT, buff=0.2)
        # Giordano, Broderick & Jordan 2018 (JMLR), Table 3: logistic GLMM on ad-conversion logs,
        # covariate effect beta_3: MCMC 0.110 +- 0.020, mean-field VI 0.110 +- 0.004
        PANEL_X, HEAD_Y, R1Y, R2Y = -1.45, 3.36, 2.9, 2.46       # all above B's crown and label
        BCX, UNIT = 1.8, 80.0                       # shared mean's x; scene units per unit of effect
        head = text("real ad-conversion model", size=LABEL)
        head.move_to([PANEL_X, HEAD_Y, 0], aligned_edge=LEFT)
        lab_mc = text("MCMC", size=LABEL, color=BLUE).move_to([PANEL_X, R1Y, 0], aligned_edge=LEFT)
        lab_vi = text("VI", size=LABEL, color=PURPLE).move_to([PANEL_X, R2Y, 0], aligned_edge=LEFT)
        sd_mc, sd_vi = 0.020 * UNIT, 0.004 * UNIT
        bar_mc = bracket([BCX - sd_mc, R1Y, 0], [BCX + sd_mc, R1Y, 0], color=BLUE, width=5)
        bar_vi = bracket([BCX - sd_vi, R2Y, 0], [BCX + sd_vi, R2Y, 0], color=PURPLE, width=5)
        val_mc = MathTex(r"0.110 \pm 0.020", font_size=36, color=BLUE)
        val_vi = MathTex(r"0.110 \pm 0.004", font_size=36, color=PURPLE)
        val_mc.move_to([BCX + sd_mc + 0.35, R1Y, 0], aligned_edge=LEFT)
        val_vi.move_to([BCX + sd_mc + 0.35, R2Y, 0], aligned_edge=LEFT)
        mean_ln = DashedLine([BCX, R2Y - 0.22, 0], [BCX, R1Y + 0.22, 0], dash_length=0.07,
                             stroke_color=GRAY, stroke_width=2)
        # five VI spreads laid end to end span one MCMC spread
        tiles = VGroup(*[Line([BCX - sd_mc + 2 * k * sd_vi + 0.03, R1Y, 0],
                              [BCX - sd_mc + 2 * (k + 1) * sd_vi - 0.03, R1Y, 0],
                              color=PURPLE, stroke_width=7) for k in range(5)])
        cite_g = citation("Giordano, Broderick & Jordan, 2018 · JMLR, Tables 2–3")
        with self.narrate("Blei and colleagues note that variational inference generally "
                          "underestimates posterior variance. [pause 0.4] In a real ad-conversion "
                          "model, its average for one effect matched MCMC, but its spread was only a "
                          "fifth as wide.", gap=1.0) as beat:
            beat.wait_until("Blei", offset=-0.2)
            self.play(swap(cite_bishop, cite_blei), FadeOut(m3b), run_time=0.7)
            beat.wait_until("underestimates", offset=-0.1)
            # only the curve and B are compared: A steps out
            self.play(Create(br_P), Create(br_B), self.a_op.animate.set_value(0.0),
                      self.lab_a_op.animate.set_value(0.0), run_time=0.9)
            self.play(FadeIn(l114), FadeIn(l044), run_time=0.5)
            beat.wait_until("real", offset=-0.15)
            self.play(FadeOut(VGroup(legend1, legend2)), swap(cite_blei, cite_g),
                      FadeOut(VGroup(br_P, br_B, l114, l044)), tag_post.animate.set_opacity(0.35),
                      run_time=0.6)
            self.play(Write(head), run_time=0.7)
            # the two estimates of one effect, on one shared mean line ("its average ... matched")
            beat.wait_until("average", offset=-0.15)
            self.play(FadeIn(lab_mc), FadeIn(lab_vi), GrowFromCenter(bar_mc), GrowFromCenter(bar_vi),
                      Create(mean_ln), run_time=0.9)
            beat.wait_until("matched", offset=-0.15)
            self.play(FadeIn(val_mc, shift=0.1 * LEFT), FadeIn(val_vi, shift=0.1 * LEFT),
                      Indicate(mean_ln, color=YELLOW, scale_factor=1.0), run_time=0.7)
            beat.wait_until("fifth", offset=-0.6)
            self.play(LaggedStart(*[TransformFromCopy(bar_vi[0], tl) for tl in tiles],
                                  lag_ratio=0.25), run_time=1.4)
        panel = VGroup(head, lab_mc, lab_vi, bar_mc, bar_vi, val_mc, val_vi, mean_ln, tiles)

        # ============================================================ 12. honest limit
        # one morph out and back: why the data is smoothed at all, then what heavier smoothing does
        gap_box2 = Rectangle(width=1.0 * FULL[2], height=0.42 * FULL[3], color=YELLOW,
                             stroke_width=3).move_to(self.pt(3.0, 0.21))
        tag_rdef = VGroup(text("heavier", size=LABEL, color=BLUE),       # R's default (cited)
                          text("smoothing", size=LABEL, color=BLUE)
                          ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        tag_rdef.move_to([TAG_L, TAG_Y, 0], aligned_edge=LEFT)
        cite_r = citation("Silverman, 1986 · Density Estimation (R's default bandwidth)")
        # the raw data: one tick per eruption on the length axis
        rug = VMobject(stroke_color=BLUE, stroke_width=2.5, stroke_opacity=0.85)
        for x in ERUPT:
            rug.start_new_path(self.pt(x, 0) + UP * 0.06)
            rug.add_line_to(self.pt(x, 0) + UP * 0.42)
        raw_tag = VGroup(text("272 raw points", size=LABEL, color=BLUE))
        raw_tag.move_to([TAG_L, TAG_Y, 0], aligned_edge=LEFT)
        inf_d = note("bell", "data").move_to([NX, ROW2, 0])
        inf_v = MathTex("=", r"\infty", font_size=36)
        inf_v[1].set_color(RED)
        inf_v.next_to(inf_d, RIGHT, buff=0.25)
        inf_line = VGroup(inf_d, inf_v)
        # the best bell-first fit under heavier smoothing: label pinned above its crown
        w_crown = self.pt(MW, math.exp(log_norm(MW, MW, SW)))
        fit_lab = VGroup(text("best bell-first fit:", size=LABEL, color=PURPLE),
                         MathTex(r"%.2f \pm %.2f\ \text{min}" % (MW, SW), font_size=36, color=PURPLE)
                         ).arrange(DOWN, buff=0.14)
        fit_lab.move_to(w_crown + UP * 1.05, aligned_edge=DOWN)
        fl_leader = DashedLine(w_crown + UP * 0.14, fit_lab.get_bottom() + DOWN * 0.15,
                               dash_length=0.07, stroke_color=PURPLE, stroke_width=2)
        # (no spoken "bell-first": Kokoro runs the compound together, whisper heard "belfirst")
        with self.narrate("Against raw points, with the bell first, every score is infinite, so the "
                          "data must be smoothed. [pause 0.3] Smooth it more heavily and the gap partly "
                          "fills: the best fit spreads almost back to A.", gap=0.5) as beat:
            # the measured case leaves as the raw eruptions come in
            self.play(FadeOut(VGroup(cite_g, panel)), swap(tag_post, raw_tag),   # tags never overlap
                      self.bell_fill.animate.set_value(0.0),
                      self.ax.x_title.animate.set_opacity(1.0), self.ax.y_title.animate.set_opacity(1.0),
                      Create(rug), self.p_op.animate.set_value(0.15),
                      self.bar_op.animate.set_value(0.06), run_time=0.9)
            beat.wait_until("infinite", offset=-0.25)
            self.play(Write(inf_line), run_time=0.8)
            beat.wait_until("smoothed", offset=-0.2)
            self.play(FadeOut(VGroup(rug, raw_tag, inf_line)), self.p_op.animate.set_value(1.0),
                      self.bar_op.animate.set_value(0.42), run_time=0.8)
            beat.wait_until("Smooth", offset=-0.15)
            self.play(self.sm_r.animate.set_value(1.0), FadeIn(tag_rdef, shift=0.1 * RIGHT), FadeIn(cite_r),
                      run_time=beat.until("gap", offset=-0.1), rate_func=SMOOTH)
            self.play(Create(gap_box2), run_time=0.6)
            beat.wait_until("best", offset=-0.1)
            # "spreads": the bell widens to the best bell-first fit under this smoothing...
            self.play(FadeOut(gap_box2), self.mu.animate.set_value(MW), self.sd.animate.set_value(SW),
                      run_time=beat.until("back to", offset=-0.1, min_time=0.9), rate_func=SMOOTH)
            # ..."almost back to A": its stats and the dashed data-first fit A, side by side
            self.play(FadeIn(fit_lab, shift=0.1 * DOWN), Create(fl_leader),
                      self.a_op.animate.set_value(0.6), self.lab_a_op.animate.set_value(1.0),
                      run_time=0.7)

        # ============================================================ 13. landing
        LX = NX + 0.3
        land1 = VGroup(note("data", "bell"), MathTex(r"\to\ A", font_size=36, color=PURPLE)
                       ).arrange(RIGHT, buff=0.3)
        land2 = VGroup(note("bell", "data"), MathTex(r"\to\ B", font_size=36, color=PURPLE)
                       ).arrange(RIGHT, buff=0.3)
        land1.move_to([LX, ROW1, 0])
        land2.move_to([LX, ROW2, 0]).align_to(land1, LEFT)
        firsts = VGroup(*[Line(a.get_corner(DL) + DOWN * 0.12 + RIGHT * 0.05,
                               a.get_corner(DR) + DOWN * 0.12 + LEFT * 0.05,
                               color=YELLOW, stroke_width=4)
                          for a in (land1[0][1], land2[0][1])])
        one = MathTex("1", font_size=44, color=YELLOW).next_to(self.pt(MA, D["qA_peak"]), UP, buff=0.2)
        three = MathTex("3", font_size=44, color=YELLOW).next_to(self.pt(MB, D["qB_peak"]), UP,
                                                                  buff=0.2)
        # in the beat turn: back to the eruptions' own curve and to the two bells of the bet
        self.play(self.sm_r.animate.set_value(0.0), FadeOut(VGroup(tag_rdef, fit_lab, fl_leader, cite_r)),
                  self.mu.animate.set_value(MB), self.sd.animate.set_value(SB),
                  run_time=1.3, rate_func=SMOOTH)
        # a real breath between the pair: at 0.1 s "Bell B" was crushed (heard as "be")
        with self.narrate("Bell A never misses an eruption that happens. [pause 0.5] "
                          "Bell B almost never imagines one that doesn't.", gap=0) as beat:
            # "Bell A never misses...": data first, the answer was 1; A solid, its fill over both humps
            self.a_fill.set_value(0.25)
            self.a_fill_x.set_value(0.0)
            self.play(Write(land1), FadeIn(one, shift=0.15 * DOWN), self.a_solid.animate.set_value(1.0),
                      self.a_op.animate.set_value(1.0), self.bell_op.animate.set_value(0.4),
                      run_time=0.8)
            self.play(self.a_fill_x.animate.set_value(7.0), Create(firsts[0]), run_time=1.1,
                      rate_func=SMOOTH)
            # "Bell B almost never imagines...": bell first, the answer was 3; B fills its one hump
            beat.wait_until("Bell B", offset=-0.15)
            self.bell_fill.set_value(0.3)
            self.bell_fill_x.set_value(0.0)
            self.play(Write(land2), FadeIn(three, shift=0.15 * DOWN), Create(firsts[1]),
                      self.a_solid.animate.set_value(0.0), self.a_op.animate.set_value(0.6),
                      self.a_fill.animate.set_value(0.0), self.bell_op.animate.set_value(1.0),
                      self.bell_fill_x.animate.set_value(7.0), run_time=1.2, rate_func=SMOOTH)

        for m in self.mobjects:
            m.clear_updaters()
        self.end_card(hold=0.3)
