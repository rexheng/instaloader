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
TWO = (-5.75, 0.65, 8.0 / 7.0, 2.2)         # chart on top, the data-first bill underneath
THREE = (-5.75, 1.0, 8.0 / 7.0, 1.85)       # chart on top, both bills underneath
# bills: (origin y, units per bit/minute); y runs over [B_LO, B_HI] bits per minute
B1_TWO, B1_THREE, B2_THREE = (-1.3, 0.66), (-0.25, 0.38), (-1.83, 0.38)
B_LO, B_HI = -1.0, 2.5
SCAN_HI = 1.8                               # lower scanner line stops under the unit label
RX = 4.4                                    # right column centre
COLX = 2.75                                 # left edge of the formula blocks
ROW1, ROW2 = 3.15, 2.4                      # the two notation lines (full layout)
NX = 2.95                                   # their centre
PIN_Y = 1.2                                 # labels pinned above a bell's crown (full layout)
PX, QX, PW = 3.35, 4.45, 0.7                # pulled-out p and q bars (one-length beat)
Y_RP, Y_RQ, Y_LR = 2.6, 1.95, 1.15          # readouts (beats 5-7)
ROWS_TWO = (-0.2, -0.8, -1.4)               # formula block next to the bill (two panels)
ROWS1_THREE = (0.75, 0.15, -0.45)           # data-first block (three panels)
ROWS2_THREE = (-1.1, -1.7, -2.3)            # bell-first block


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


def chart_axes(lay, xlab=True) -> Axes:
    ox, oy, xu, yu = lay
    ax = axes((0, 7), (0, 1), x_length=7 * xu, y_length=yu, x_ticks=[1, 2, 3, 4, 5, 6],
              y_ticks=[0, 0.5, 1], x_label="eruption length (minutes)",
              y_label="density (per minute)")
    ax.shift(np.array([ox, oy, 0]) - ax.c2p(0, 0))
    if not xlab:                     # stacked panels: the shared x labels sit under the bottom bill
        ax.x_axis.numbers.set_opacity(0)
        ax.x_title.set_opacity(0)
    return ax


def bill_axes(oy, yu, sparse=False) -> Axes:
    ax = axes((0, 7), (B_LO, B_HI), x_length=7 * TWO[2], y_length=(B_HI - B_LO) * yu,
              x_ticks=[1, 2, 3, 4, 5, 6], y_ticks=[-1, 0, 1, 2])
    ax.x_axis.remove(ax.x_axis.numbers)
    ax.shift(np.array([TWO[0], oy, 0]) - ax.c2p(0, 0))
    if sparse:                       # short panels: label only 0 and 2
        for num in [n for n in ax.y_axis.numbers if abs(n.get_value()) == 1]:
            ax.y_axis.numbers.remove(num)
    return ax


def bill_unit(oy, yu, s="bits/min") -> Text:
    t = text(s, size=26, color=GRAY)
    top = oy + B_HI * yu
    t.move_to([TWO[0] + 0.22, top, 0], aligned_edge=UL)
    return t


def x_labels(y_bottom) -> VGroup:
    """Shared x-axis labels (1-6 and the name) under the lowest panel."""
    nums = VGroup(*[MathTex(str(k), font_size=MATH_SMALL, color=GRAY) for k in range(1, 7)])
    for k, m in zip(range(1, 7), nums):
        m.move_to([TWO[0] + TWO[2] * k, y_bottom - 0.18, 0], aligned_edge=UP)
    name = Text("eruption length (minutes)", font=SERIF, font_size=LABEL, color=GRAY)
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


class Episode(NarratedScene):
    EPISODE = 8
    TITLE = "The Distance That Isn't Symmetric"
    SPEED = 0.84
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
        c = VMobject(stroke_color=BLUE, stroke_width=4.5,
                     stroke_opacity=self.p_op.get_value())
        c.set_points_smoothly(pts[::2])
        return c

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
                               fill_x=self.bell_fill_x.get_value())

    def make_ghost(self):
        """Bell A when another bell is the focus: dashed; solid when it is a contender."""
        op, sol = self.a_op.get_value(), self.a_solid.get_value()
        g = VGroup()
        if op * (1 - sol) > 0.01:
            g.add(self.bell_shape(MA, SA, width=2.5 + 2.0 * max(0.0, op - 0.4) / 0.6,
                                  opacity=op * (1 - sol), dashed=True))
        if op * sol > 0.01:
            g.add(self.bell_shape(MA, SA, opacity=op * sol, fill=self.a_fill.get_value(),
                                  fill_x=self.a_fill_x.get_value()))
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

        def upd(m):
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
            dec.set_opacity(0.0 if sci else 1.0)
            for x in (mant, times, expo):
                x.set_opacity(1.0 if sci else 0.0)
        g.add_updater(upd)
        upd(g)
        return g

    def peak_tag(self):
        """'peak = 11' over the clipped data-first bill, live, shown only while it clips."""
        tag = MathTex(r"\text{peak} \approx", font_size=30, color=RED)
        num = DecimalNumber(11, num_decimal_places=0, font_size=30, color=RED)
        arrow = Arrow(ORIGIN, RIGHT, buff=0, color=RED, stroke_width=3,
                      max_tip_length_to_length_ratio=0.25)
        g = VGroup(tag, num, arrow)

        def upd(m):
            f = self.integrand_x(1)
            pk = float(f.max())
            op = float(np.clip((pk - B_HI - 0.5) / 1.0, 0, 1)) * self.peak_op.get_value()
            num.set_value(pk)
            tag.move_to(self.bp(1, 3.35, 2.0), aligned_edge=LEFT)
            num.next_to(tag, RIGHT, buff=0.12).align_to(tag, DOWN)
            xpk = float(XS[int(np.argmax(f))])
            arrow.put_start_and_end_on(tag.get_left() + LEFT * 0.2,
                                       self.bp(1, xpk + 0.15, B_HI - 0.05))
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

        self.ax = chart_axes(FULL)
        bars = self.redraw(self.make_bars, self.bar_h, self.bar_op)
        pcurve = self.redraw(self.make_pcurve, self.sm_r, self.sm_c, self.p_op)
        bell = self.redraw(self.make_bell, self.mu, self.sd, self.bell_fill, self.bell_op,
                           self.bell_fill_x)

        # ============================================================ 1. cold open: the bet
        n_lab = VGroup(text("272 eruptions", size=LABEL, color=BLUE),
                       text("curve: smoothed", size=24, color=GRAY)
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
        with self.narrate("Old Faithful's eruptions. [pause 0.12] With the data first, the closest "
                          "bell curve is this one. [pause 0.2] Put the bell first, and if closeness "
                          "works both ways, it stays at one. Or does it move to two, or three? "
                          "[pause 1.5]") as beat:
            self.play(self.bar_op.animate.set_value(0.42), Create(static_p),
                      FadeIn(n_lab, shift=0.1 * DOWN), FadeIn(cite_data),
                      run_time=beat.until("With", offset=-0.1), rate_func=SMOOTH)
            self.swap_in(static_p, pcurve)
            self.play(Write(n1), run_time=beat.until("closest", offset=-0.05))
            static_b = self.make_bell()
            self.play(Create(static_b), run_time=beat.until("one", offset=0.25))
            self.swap_in(static_b, bell)
            beat.wait_until("bell first", offset=-0.15)
            # the two arguments trade places, onto a second line
            self.play(TransformFromCopy(n1[0], n2[0]), TransformFromCopy(n1[2], n2[2]),
                      TransformFromCopy(n1[4], n2[4]),
                      TransformFromCopy(n1[1], n2[3], path_arc=-1.6),
                      TransformFromCopy(n1[3], n2[1], path_arc=-1.6), run_time=1.3)
            beat.wait_until("one", occurrence=2, offset=-0.2)
            self.play(FadeIn(mk1, shift=0.15 * DOWN), run_time=0.6)
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
        ml_lab = text("maximum-likelihood fit", size=26, color=PURPLE).move_to([crown[0], PIN_Y, 0])
        leader = DashedLine(crown + UP * 0.12, ml_lab.get_bottom() + DOWN * 0.15, dash_length=0.07,
                            stroke_color=PURPLE, stroke_width=2)
        with self.narrate("The D stands for KL divergence, named for Kullback and Leibler. "
                          "[pause 0.2] Every maximum-likelihood fit is the closest model by it, and "
                          "it's often called a distance between distributions.") as beat:
            self.play(FadeOut(VGroup(ghost2, ghost3, mk1, mk2, mk3, n_lab)),
                      n2.animate.set_opacity(0.3), Indicate(n1[0], color=YELLOW, scale_factor=1.25),
                      run_time=0.8)
            beat.wait_until("KL", offset=-0.15)
            self.play(FadeIn(kl_lab, shift=0.1 * RIGHT), run_time=0.7)
            beat.wait_until("Kullback", offset=-0.2)
            self.play(FadeOut(cite_data), FadeIn(cite_kl), run_time=0.7)
            beat.wait_until("maximum", offset=-0.1)
            self.play(FadeIn(ml_lab, shift=0.1 * UP), Create(leader), flag(n1), run_time=1.0)
            beat.wait_until("closest model", offset=-0.1)
            self.play(self.flash_bell(run_time=1.1))
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
        with self.narrate("So treat it as one. Data first, this bell is point seven six bits away. "
                          "[pause 0.12] Shift it or stretch it, and that number only grows, so this "
                          "is bell A: three and a half minutes, give or take one point one.") as beat:
            self.play(TransformMatchingShapes(dist_lab, dist_lab2),
                      kl_lab.animate.set_opacity(0.35), run_time=0.8)
            beat.wait_until("Data first", offset=-0.1)
            self.play(flag(n1[1]), run_time=0.8)
            beat.wait_until("point", offset=-0.15)
            self.play(FadeIn(r1, shift=0.1 * LEFT), run_time=0.7)
            beat.wait_until("Shift", offset=-0.15)
            # each excursion: out, hold and flag the raised number, back
            for tracker, val in ((self.mu, MA + NV["shift"]), (self.sd, SA * NV["stretch"])):
                home = tracker.get_value()
                self.play(tracker.animate.set_value(val), run_time=0.6, rate_func=SMOOTH)
                num1.suspend_updating()
                self.play(Indicate(num1, color=YELLOW, scale_factor=1.15), run_time=0.5)
                num1.resume_updating()
                self.play(tracker.animate.set_value(home), run_time=0.55, rate_func=SMOOTH)
            beat.wait_until("bell A", offset=-0.2)
            self.play(Create(mean_line), run_time=0.5)
            beat.wait_until("three", offset=-0.15)
            self.play(FadeTransform(ml_lab, a_lab), run_time=0.9)
        num1.clear_updaters()
        num1.set_value(D["A"]["fwd"])

        # ============================================================ 4. fail
        times = MathTex(r"\times 2.2", font_size=36, color=YELLOW).next_to(r2, DOWN, buff=0.22)
        times.align_to(r2[1], LEFT)
        with self.narrate("But a distance reads the same both ways. [pause 0.15] Put the bell first, "
                          "and the same two curves are one point seven bits apart, more than twice "
                          "as far. [pause 0.75] Only the order changed, so the order must be built "
                          "into the formula.") as beat:
            self.play(n2.animate.set_opacity(1.0), flag(dist_lab2),
                      VGroup(a_lab, leader, mean_line).animate.set_opacity(0.3), run_time=0.9)
            beat.wait_until("bell first", offset=-0.1)
            self.play(flag(n2[1]), run_time=0.8)
            beat.wait_until("one point", offset=-0.15)
            self.play(FadeIn(r2, shift=0.1 * LEFT), run_time=0.7)
            beat.wait_until("twice", offset=-0.15)
            self.play(FadeIn(times, shift=0.1 * DOWN), Indicate(r1.num, color=YELLOW),
                      Indicate(r2.num, color=YELLOW), run_time=1.0)
            beat.wait_until("order changed", offset=-0.1)
            bx = VGroup(box(n1, buff=0.12), box(n2, buff=0.12))
            self.play(Create(bx), run_time=0.8)
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
        lr_num.add_updater(lambda m: m.set_value(
            math.log2(max(self.p_at(self.scan.get_value()), 1e-300)
                      / max(self.q_at(self.scan.get_value()), 1e-300))))
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

        with self.narrate("To see why, open it up at one real eruption, two minutes long. The data's "
                          "curve gives that length a height, p. [pause 0.12] The bell gives it q, "
                          "about a quarter as much. Double q twice and you reach p, so log base two "
                          "of p over q is about two: two doublings, or two bits.") as beat:
            # numbers leave first, then the chart shrinks (nothing slides over a label)
            self.play(FadeOut(VGroup(kl_lab, dist_lab2, n2, r2, times, a_lab, leader, mean_line,
                                     cite_kl, r1)), run_time=0.4)
            self.play(*self.to_layout(MID), self.move_axes(MID),
                      lhs.animate.scale(40 / 36).move_to([RX, 3.2, 0]),
                      self.bar_op.animate.set_value(0.1),
                      run_time=beat.until("one real", offset=-0.1), rate_func=SMOOTH)
            self.play(Indicate(self.ax.x_axis.numbers[1], color=YELLOW, scale_factor=1.4),
                      run_time=0.6)
            self.scan.set_value(2.0)
            scanner.update()
            self.play(Create(scanner), run_time=0.6)
            self.add(pq_bars)
            beat.wait_until("height", offset=-0.35)
            self.play(self.p_h.animate.set_value(1.0), run_time=0.6)
            self.play(TransformFromCopy(pq_bars[0], big_p), Create(base_line), FadeIn(p_sym),
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
        f_fwd = rhs("p", "p", "q")
        tot = bits_readout(D["A"]["fwd"], size=40)
        stack_rows((lhs.copy(), f_fwd, tot), ROWS_TWO)
        lhs_target = lhs.copy().scale(1.0)
        stack_rows((lhs_target,), ROWS_TWO[:1])
        ax_b1 = bill_axes(*B1_TWO)
        unit1 = bill_unit(*B1_TWO, s="bits")
        unit1b = bill_unit(*B1_TWO)
        xlab = x_labels(B1_TWO[0] + B_LO * B1_TWO[1])
        area = self.redraw(lambda: self.make_area(1), self.mu, self.sd, self.sm_r, self.sm_c,
                           self.weighted, self.reveal, self.fill_reveal, self.area_fill,
                           self.area_op)
        tot_num = tot.num
        refund = text("refund", size=26, color=GRAY)

        # where log2(p/q) runs off the bottom of the panel: say how far it really goes
        LRD = D["log2_p_over_qA"]
        cuts = LRD["crosses_minus1_at"]                 # [1.461, 2.444, 3.588, 5.229]
        clip_specs = [((0.0 + cuts[0]) / 2, 0.0, r"\downarrow\,%d" % round(LRD["at_0"])),
                      (3.0, cuts[1], r"\downarrow\,%.1f" % LRD["gap_min"][1]),
                      ((cuts[3] + 7.0) / 2, cuts[3], r"\downarrow\,%d" % round(LRD["at_7"]))]
        clip_marks = VGroup()
        for xc, x0, tex in clip_specs:
            mk = MathTex(tex, font_size=30, color=GRAY).move_to(
                [TWO[0] + TWO[2] * xc, B1_TWO[0] - 0.5 * B1_TWO[1], 0])
            mk.x0 = x0
            mk.add_updater(lambda m: m.set_opacity(
                float(np.clip((self.reveal.get_value() - m.x0) / 0.3, 0, 1))
                * (1 - self.weighted.get_value()) * self.area_op.get_value()))
            clip_marks.add(mk)

        with self.narrate("Do that at every length. [pause 0.12] Then weight each one by how often "
                          "eruptions last that long, which is p, and add it all up. [pause 0.3] "
                          "Where the bell rises above the data, the grey dips pay a little back. "
                          "[pause 0.5] That's the divergence: point seven six bits.", gap=0.9) as beat:
            self.play(FadeOut(pullout), FadeOut(lhs), run_time=0.4)
            self.play(*self.to_layout(TWO), self.move_axes(TWO, xlab=False), Create(ax_b1),
                      FadeIn(unit1), FadeIn(xlab), self.bar_op.animate.set_value(0.25),
                      self.bot_scan_op.animate.set_value(1.0), run_time=1.0, rate_func=SMOOTH)
            self.play(self.scan.animate.set_value(0.3), run_time=0.5, rate_func=SMOOTH)
            self.reveal.set_value(0.3)
            self.add(area, clip_marks)
            Ts = beat.until("weight", offset=-0.1)
            self.play(self.scan.animate(rate_func=LINEAR, run_time=Ts).set_value(7.0),
                      self.reveal.animate(rate_func=LINEAR, run_time=Ts).set_value(7.0),
                      Succession(Wait(0.3), TransformFromCopy(lr_lab[0], f_fwd[2], run_time=1.4),
                                 Wait(max(0.01, Ts - 1.7))),
                      Succession(Wait(0.3), TransformFromCopy(lr_lab[1], VGroup(*f_fwd[3:8]),
                                                              run_time=1.4),
                                 Wait(max(0.01, Ts - 1.7))))
            self.play(self.scan_op.animate.set_value(0.0), self.pq_op.animate.set_value(0.0),
                      run_time=0.4)
            self.scan.set_value(2.0)
            self.play(self.weighted.animate.set_value(1.0), FadeOut(unit1), FadeIn(unit1b),
                      run_time=beat.until("which is", offset=-0.05), rate_func=SMOOTH)
            self.remove(clip_marks)
            # the weight p swings out around the readouts' left edge into the formula
            self.play(TransformFromCopy(rp[0][0], f_fwd[1], path_arc=-1.7), self.flash_p(),
                      run_time=1.0)
            beat.wait_until("add it", offset=-0.1)
            tot_num.set_value(0.0)
            self.play(Write(f_fwd[0]), Write(f_fwd[8]), FadeIn(tot), run_time=0.6)
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
            self.play(FadeIn(lhs_target, shift=0.1 * DOWN), run_time=0.6)
            beat.wait_until("point seven", offset=-0.15)
            self.pulse(tot_num, run_time=0.8)
        lhs = lhs_target

        # ============================================================ 7. a bell that skips a hump
        ghost = self.redraw(self.make_ghost, self.a_op, self.a_solid, self.a_fill, self.a_fill_x)
        lab_A = MathTex("A", font_size=36, color=PURPLE)
        lab_A.add_updater(lambda m: m.next_to(
            self.pt(1.1, self.q_at(1.1, MA, SA)), UL, buff=0.15).set_opacity(
            min(1.0, self.a_op.get_value() + 0.2)))
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
        ptag = self.peak_tag()
        with self.narrate("Try a bell that ignores the short eruptions and sits on the long hump. At "
                          "two minutes, it falls short by eighteen and a half doublings. [pause 0.6] "
                          "More than a third of all eruptions are short ones like this, so the bill "
                          "comes to five point eight bits.") as beat:
            self.add(ghost, lab_A, lab_B, ptag)
            lab_A.update()
            lab_B.update()
            self.play(self.scan_op.animate.set_value(1.0), self.pq_op.animate.set_value(0.9),
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
        ax_b1_3 = bill_axes(*B1_THREE, sparse=True)
        ax_b2 = bill_axes(*B2_THREE, sparse=True).set_opacity(0.3)
        unit1_3 = bill_unit(*B1_THREE)
        unit2 = bill_unit(*B2_THREE).set_opacity(0.3)
        xlab3 = x_labels(B2_THREE[0] + B_LO * B2_THREE[1])
        area2 = self.redraw(lambda: self.make_area(2), self.mu, self.sd, self.sm_r, self.sm_c,
                            self.fill2_reveal, self.area2_op)
        block1 = VGroup(lhs, f_fwd, tot)
        # the second block starts as an exact copy that splits off downwards, then swaps in place
        lhs2, f2, tot_c = lhs.copy(), f_fwd.copy(), tot.copy()
        block2 = VGroup(lhs2, f2, tot_c)
        tgt1, tgt2 = block1.copy(), block2.copy()
        stack_rows(tgt1, ROWS1_THREE)
        stack_rows(tgt2, ROWS2_THREE)
        lhs_r = note("bell", "data", size=40).move_to(tgt2[0], aligned_edge=LEFT)
        f_rev = rhs("q", "q", "p").move_to(tgt2[1], aligned_edge=LEFT)
        q_tot = MathTex("=", r"\ ?", font_size=40)
        q_tot[1].set_color(YELLOW)
        q_tot.move_to(tgt2[2], aligned_edge=LEFT)
        with self.narrate("Now keep that bill, and swap the order for a second one. [pause 0.12] "
                          "Every p trades places with q. [pause 0.3] The bell supplies the lengths, "
                          "and the data judges them. [pause 0.5] Which bell wins now? "
                          "[pause 1.5]") as beat:
            # readouts and markers leave first, then the panels make room for a second bill
            self.play(FadeOut(VGroup(rp, rq, lr, short_box, pct)),
                      self.pq_op.animate.set_value(0.0), self.scan_op.animate.set_value(0.0),
                      run_time=0.4)
            self.remove(pq_bars, scanner)
            tot_num.clear_updaters()
            tot_c.num.clear_updaters()
            block2.become(tgt2)
            self.play(*self.to_layout(THREE), self.move_axes(THREE, xlab=False),
                      self.b1y.animate.set_value(B1_THREE[0]), self.b1u.animate.set_value(B1_THREE[1]),
                      ReplacementTransform(ax_b1, ax_b1_3), ReplacementTransform(unit1b, unit1_3),
                      ReplacementTransform(xlab, xlab3), Transform(block1, tgt1),
                      FadeIn(ax_b2), FadeIn(unit2),
                      self.a_solid.animate.set_value(1.0), self.a_op.animate.set_value(1.0),
                      run_time=beat.until("swap", offset=-0.45, min_time=0.9), rate_func=SMOOTH)
            tot_num.add_updater(lambda m: m.set_value(self.total(1)))
            # the copy appears only once the first block has moved clear of its rows
            self.play(FadeIn(block2), run_time=0.35)
            beat.wait_until("swap", offset=-0.1)
            # the arguments trade places, in the copy only
            self.play(ReplacementTransform(lhs2[0], lhs_r[0]), ReplacementTransform(lhs2[2], lhs_r[2]),
                      ReplacementTransform(lhs2[4], lhs_r[4]),
                      ReplacementTransform(lhs2[1], lhs_r[3], path_arc=-1.6),
                      ReplacementTransform(lhs2[3], lhs_r[1], path_arc=-1.6), run_time=1.2)
            beat.wait_until("Every p", offset=-0.1)
            self.play(*[ReplacementTransform(f2[i], f_rev[i]) for i in (0, 2, 3, 5, 7, 8)],
                      ReplacementTransform(f2[1], f_rev[1]),
                      ReplacementTransform(f2[4], f_rev[6], path_arc=-2.2),
                      ReplacementTransform(f2[6], f_rev[4], path_arc=-2.2),
                      ReplacementTransform(tot_c, q_tot), run_time=1.5)
            self.play(Indicate(f_rev[1], color=YELLOW), run_time=0.7)
            beat.wait_until("supplies", offset=-0.1)
            self.play(self.flash_bell(), self.hump_flash(np.exp(log_norm(XS, MA, SA))),
                      run_time=1.0)
            beat.wait_until("judges", offset=-0.1)
            self.play(self.flash_p())
            beat.wait_until("Which", offset=-0.1)
            self.play(Indicate(lab_A, color=YELLOW), Indicate(lab_B, color=YELLOW), run_time=0.9)

        # ============================================================ 9. B then A, bell first
        self.add(area2)
        tot2 = bits_readout(D["B"]["rev"], size=40)
        tot2.move_to(q_tot, aligned_edge=LEFT)
        free_box = DashedVMobject(Rectangle(width=1.1 * TWO[2], height=1.0 * B2_THREE[1] + 0.5,
                                            color=YELLOW, stroke_width=2.5).move_to(
            [TWO[0] + TWO[2] * 2.0, B2_THREE[0] + 0.55 * B2_THREE[1], 0]), num_dashes=36)
        gap_box = Rectangle(width=1.0 * TWO[2], height=2.2 * B2_THREE[1], color=YELLOW,
                            stroke_width=2.5).move_to(
            [TWO[0] + TWO[2] * 2.9, B2_THREE[0] + 0.95 * B2_THREE[1], 0])
        tail_boxes = VGroup(*[Rectangle(width=0.8 * TWO[2], height=0.32, color=YELLOW,
                                        stroke_width=2.5).move_to(
            [TWO[0] + TWO[2] * x, B2_THREE[0] + 0.12, 0]) for x in (0.6, 6.5)])
        tot2_num = tot2.num
        with self.narrate("Take bell B first. [pause 0.15] It almost never imagines a short eruption, "
                          "so ignoring them costs it nothing. [pause 0.12] It pays point six two. "
                          "[pause 0.6] Bell A imagines eruptions in the gap and out in the tails, "
                          "lengths the data almost never shows. [pause 0.2] That costs one point "
                          "seven bits.", gap=0.9) as beat:
            self.area2_op.set_value(1.0)
            self.fill2_reveal.set_value(0.0)
            tot2_num.set_value(0.0)
            self.play(self.a_solid.animate.set_value(0.0), self.a_op.animate.set_value(0.5),
                      self.bell_fill.animate.set_value(0.28), ax_b2.animate.set_opacity(1.0),
                      unit2.animate.set_opacity(1.0), ReplacementTransform(q_tot[0], tot2[0]),
                      FadeOut(q_tot[1]), FadeIn(tot2[1:]),
                      Indicate(lab_B, color=YELLOW), run_time=0.9)
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
            beat.wait_until("That costs", offset=-0.1)
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
        b_lab = MathTex(r"B\!:\ 4.27 \pm 0.44\ \text{min}", font_size=34, color=PURPLE)
        b_lab.next_to(crown_b3, RIGHT, buff=0.55).shift(0.05 * UP)
        b_leader = DashedLine(crown_b3 + RIGHT * 0.12, b_lab.get_left() + LEFT * 0.12,
                              dash_length=0.07, stroke_color=PURPLE, stroke_width=2)
        m1b = MathTex("1", font_size=40, color=YELLOW).next_to(crown_a3, UP, buff=0.2)
        m3b = MathTex("3", font_size=40, color=YELLOW).next_to(crown_b3, UP, buff=0.2)
        moved = CurvedArrow(m1b.get_top() + UP * 0.22, m3b.get_left() + LEFT * 0.15, angle=-0.6,
                            color=YELLOW, stroke_width=4, tip_length=0.18)
        with self.narrate("Now start from A, and let the bell slide downhill on the bell-first bill. "
                          "[pause 0.12] As that bill drains, the other one swells, and the bell "
                          "settles on the long hump, less than half as wide. [pause 0.3] Flip the "
                          "order, and the closest bell moves to three.", gap=0.9) as beat:
            beat.wait_until("A", offset=-0.1)
            self.play(Indicate(lab_A, color=YELLOW), self.flash_bell(MA, SA), run_time=0.9)
            beat.wait_until("slide", offset=-0.2)
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
            beat.wait_until("less", offset=-0.1)
            self.play(FadeIn(b_lab, shift=0.1 * LEFT), Create(b_leader),
                      self.lab_b_op.animate.set_value(0.0), run_time=0.7)
            beat.wait_until("Flip", offset=-0.1)
            self.play(FadeIn(m1b), run_time=0.4)
            self.play(Create(moved), run_time=beat.until("three", offset=-0.1, min_time=0.6))
            self.play(FadeIn(m3b, scale=1.3), run_time=0.5)
        tot2_num.clear_updaters()
        tot_num.clear_updaters()

        # ============================================================ 11. payoff
        LEG_X = -1.8
        to_a = MathTex(r"\to\ A", font_size=36, color=PURPLE)
        to_b = MathTex(r"\to\ B", font_size=36, color=PURPLE)
        legend1 = VGroup(note("data", "model"), text("maximum likelihood", size=LABEL), to_a)
        legend2 = VGroup(note("model", "posterior"), text("variational inference", size=LABEL), to_b)
        for lg in (legend1, legend2):
            lg.arrange(RIGHT, buff=0.25)
        legend1.move_to([LEG_X, ROW1 + 0.08, 0], aligned_edge=LEFT)
        legend2.move_to([LEG_X, ROW2, 0], aligned_edge=LEFT)
        legend1[1].align_to(legend2[1], LEFT)
        legend1[2].next_to(legend1[1], RIGHT, buff=0.25)
        TAG_L, TAG_Y = 2.55, -0.3                  # blue tag, right of the long hump (full layout)
        tag_data = text("data", size=LABEL, color=BLUE)
        tag_data.move_to([TAG_L, TAG_Y, 0], aligned_edge=LEFT)
        tag_post = text("posterior", size=LABEL, color=BLUE)
        tag_post.move_to([TAG_L, TAG_Y, 0], aligned_edge=LEFT)
        stand_in = text("same curve, as a stand-in", size=22, color=GRAY)
        stand_in.next_to(tag_post, DOWN, buff=0.18).align_to(tag_post, LEFT)
        cite_blei = citation("Blei et al., 2017 · J. American Statistical Association")
        cite_bishop = citation("Bishop, 2006 · Pattern Recognition and Machine Learning, §10.1")
        bill_stuff = VGroup(lhs, f_fwd, tot, lhs_r, f_rev, tot2, b_lab, b_leader, m1b, m3b, moved,
                            xlab3, unit1_3, unit2)
        with self.narrate("Maximum likelihood puts the data first, so its fits stretch over every "
                          "hump. [pause 0.2] Variational inference approximates a Bayesian "
                          "posterior with the model first, so it settles on one hump.") as beat:
            # the bills' labels and fills leave first, then the chart returns to full size
            self.play(FadeOut(bill_stuff), self.area_op.animate.set_value(0.0),
                      self.area2_op.animate.set_value(0.0), self.peak_op.animate.set_value(0.0),
                      FadeOut(ax_b1_3.y_axis.numbers), FadeOut(ax_b2.y_axis.numbers),
                      run_time=0.4)
            self.remove(area, area2, ptag)
            ax_b1_3.y_axis.remove(ax_b1_3.y_axis.numbers)
            ax_b2.y_axis.remove(ax_b2.y_axis.numbers)
            self.play(*self.to_layout(FULL), self.move_axes(FULL), FadeOut(ax_b1_3), FadeOut(ax_b2),
                      self.bell_fill.animate.set_value(0.0), self.bar_op.animate.set_value(0.42),
                      run_time=1.1, rate_func=SMOOTH)
            beat.wait_until("data first", offset=-0.2)
            self.play(FadeIn(legend1[:2], shift=0.1 * DOWN), FadeIn(cite_bishop),
                      FadeIn(tag_data, shift=0.1 * RIGHT), run_time=0.8)
            beat.wait_until("stretch", offset=-0.2)
            # maximum likelihood's bell is the focus: A solid, its fill sweeping over both humps
            self.a_fill.set_value(0.25)
            self.a_fill_x.set_value(0.0)
            self.play(self.a_solid.animate.set_value(1.0), self.a_op.animate.set_value(1.0),
                      self.bell_op.animate.set_value(0.3), self.lab_b_op.animate.set_value(0.3),
                      run_time=0.5)
            self.play(self.a_fill_x.animate.set_value(7.0), FadeIn(to_a, shift=0.1 * RIGHT),
                      run_time=1.1, rate_func=SMOOTH)
            beat.wait_until("posterior", offset=-0.15)
            self.play(FadeOut(tag_data), self.bar_op.animate.set_value(0.25),
                      self.ax.x_title.animate.set_opacity(0.3), run_time=0.3)
            self.play(Write(tag_post), FadeIn(stand_in), FadeIn(legend2[:2], shift=0.1 * DOWN),
                      run_time=0.7)
            beat.wait_until("model first", offset=-0.15)
            self.play(Indicate(legend2[0][1], color=YELLOW), run_time=0.7)
            beat.wait_until("settles", offset=-0.15)
            self.bell_fill_x.set_value(0.0)
            self.bell_fill.set_value(0.25)
            self.play(self.a_solid.animate.set_value(0.0), self.a_op.animate.set_value(0.5),
                      self.a_fill.animate.set_value(0.0), self.bell_op.animate.set_value(1.0),
                      self.lab_b_op.animate.set_value(1.0), FadeIn(to_b, shift=0.1 * RIGHT),
                      self.bell_fill_x.animate.set_value(7.0), run_time=1.1, rate_func=SMOOTH)

        # measured, not just named: B's spread against the posterior curve's own spread
        Apm, Bpm = D["A_pm_sd"], D["B_pm_sd"]
        br_P = bracket(self.pt(Apm[0], 0.12), self.pt(Apm[1], 0.12), color=BLUE)
        br_B = bracket(self.pt(Bpm[0], 0.72), self.pt(Bpm[1], 0.72), color=PURPLE)
        l114 = MathTex("1.14", font_size=34, color=BLUE).move_to(self.pt(3.0, 0.19))
        l044 = MathTex("0.44", font_size=34, color=PURPLE).next_to(br_B, LEFT, buff=0.2)
        ratio = MathTex("(", "0.44", "/", "1.14", ")^2", "=", r"15\%", font_size=40)
        ratio[1].set_color(PURPLE)
        ratio[3].set_color(BLUE)
        ratio[6].set_color(YELLOW)
        ratio.move_to([4.3, 0.85, 0])
        with self.narrate("Blei and colleagues note that variational inference generally "
                          "underestimates posterior variance. [pause 0.15] Here, bell B keeps only "
                          "fifteen percent of the posterior's variance.", gap=0.8) as beat:
            beat.wait_until("Blei", offset=-0.2)
            self.play(FadeOut(cite_bishop), FadeIn(cite_blei), run_time=0.7)
            beat.wait_until("underestimates", offset=-0.1)
            self.play(Create(br_P), Create(br_B), run_time=0.9)
            self.play(FadeIn(l114), FadeIn(l044), run_time=0.5)
            beat.wait_until("Here", offset=-0.1)
            self.play(TransformFromCopy(l044, ratio[1]), TransformFromCopy(l114, ratio[3], path_arc=0.6),
                      run_time=1.0)
            self.play(Write(VGroup(ratio[0], ratio[2], ratio[4], ratio[5], ratio[6])),
                      run_time=beat.until("fifteen", offset=0.1, min_time=0.5))
            self.play(Indicate(ratio[6], color=YELLOW), run_time=0.8)

        # ============================================================ 12. honest limit
        gap_box2 = Rectangle(width=1.0 * FULL[2], height=0.42 * FULL[3], color=YELLOW,
                             stroke_width=3).move_to(self.pt(3.0, 0.21))
        tag_rdef = VGroup(text("R's default", size=LABEL, color=BLUE),
                          text("smoothing", size=LABEL, color=BLUE)
                          ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        tag_rdef.move_to([TAG_L, TAG_Y, 0], aligned_edge=LEFT)
        tag_cv = VGroup(text("cross-validated", size=LABEL, color=BLUE),
                        text("smoothing", size=LABEL, color=BLUE)
                        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        tag_cv.move_to([TAG_L, TAG_Y, 0], aligned_edge=LEFT)
        b_dim = self.bell_shape(MB, SB, opacity=0.25)
        FIT_Y = 2.85

        def fit_label(m, s):
            lab = VGroup(text("best bell-first fit:", size=26, color=PURPLE),
                         MathTex(r"%.2f \pm %.2f\ \text{min}" % (m, s), font_size=34, color=PURPLE)
                         ).arrange(RIGHT, buff=0.15)
            lab[1].align_to(lab[0], DOWN).shift(0.02 * DOWN)
            return lab.move_to([1.3, FIT_Y, 0])

        w_lab = fit_label(MW, SW)
        c_lab = fit_label(MC, SC)
        crown_w = self.pt(MW, math.exp(log_norm(MW, MW, SW)))
        w_leader = DashedLine(crown_w + UP * 0.12, [crown_w[0], w_lab.get_bottom()[1] - 0.15, 0],
                              dash_length=0.07, stroke_color=PURPLE, stroke_width=2)
        foot = VGroup(text("With raw points,", size=22, color=GRAY),
                      MathTex(r"D(\text{bell}\,\|\,\text{data}) = \infty", font_size=30, color=GRAY),
                      text("for every bell", size=22, color=GRAY)).arrange(RIGHT, buff=0.12)
        foot[1].align_to(foot[0], DOWN).shift(0.04 * DOWN)
        foot.move_to(citation("x").get_left(), aligned_edge=LEFT)
        t2 = ValueTracker(0.0)
        t3 = ValueTracker(0.0)
        with self.narrate("Settling on one hump needs that gap to be nearly empty. [pause 0.2] Smooth "
                          "the data with R's default setting, and the gap fills enough that the best "
                          "bell-first fit comes out wide. [pause 0.8] Smoothing chosen by "
                          "cross-validation keeps the gap nearly empty, and the fit on one hump.",
                          gap=0.7) as beat:
            self.play(FadeOut(VGroup(cite_blei, br_P, br_B, l114, l044, ratio, legend1, legend2,
                                     stand_in, tag_post)),
                      self.bell_fill.animate.set_value(0.0), self.bar_op.animate.set_value(0.42),
                      self.ax.x_title.animate.set_opacity(1.0), run_time=0.6)
            self.play(FadeIn(tag_data), run_time=0.4)
            beat.wait_until("gap", offset=-0.15)
            self.play(Create(gap_box2), run_time=0.7)
            beat.wait_until("Smooth", offset=-0.1)
            self.play(self.sm_r.animate.set_value(1.0), FadeTransform(tag_data, tag_rdef),
                      FadeIn(foot), run_time=beat.until("fills", offset=0.2), rate_func=SMOOTH)
            # the fit starts from A (where a slide from A really ends), B stays as a faint reference
            self.add(b_dim)
            self.play(self.bell_op.animate.set_value(0.0), FadeOut(gap_box2),
                      self.a_op.animate.set_value(0.35), run_time=0.4)
            self.mu.set_value(MA)
            self.sd.set_value(SA)
            self.play(self.bell_op.animate.set_value(1.0), run_time=0.4)
            driver2 = Mobject()
            driver2.add_updater(follow(RPATH, t2))
            self.add(driver2)
            self.play(t2.animate.set_value(1.0), run_time=beat.until("wide", offset=0.1),
                      rate_func=SMOOTH)
            driver2.clear_updaters()
            self.remove(driver2)
            self.play(FadeIn(w_lab, shift=0.1 * DOWN), Create(w_leader), run_time=0.7)
            beat.wait_until("Smoothing chosen", offset=-0.1)
            self.play(self.sm_r.animate.set_value(0.0), self.sm_c.animate.set_value(1.0),
                      FadeTransform(tag_rdef, tag_cv), FadeOut(foot),
                      run_time=beat.until("keeps", offset=-0.1), rate_func=SMOOTH)
            self.play(FadeOut(w_lab), FadeOut(w_leader), run_time=0.3)
            driver3 = Mobject()
            driver3.add_updater(follow(CPATH, t3))
            self.add(driver3)
            self.play(t3.animate.set_value(1.0),
                      run_time=beat.until("empty", occurrence=2, offset=0.2), rate_func=SMOOTH)
            driver3.clear_updaters()
            self.remove(driver3)
            self.play(FadeIn(c_lab, shift=0.1 * DOWN), run_time=0.6)

        # ============================================================ 13. landing
        land1 = VGroup(note("data", "bell"), MathTex(r"\to\ A", font_size=36, color=PURPLE)
                       ).arrange(RIGHT, buff=0.3)
        land2 = VGroup(note("bell", "data"), MathTex(r"\to\ B", font_size=36, color=PURPLE)
                       ).arrange(RIGHT, buff=0.3)
        land1.move_to([NX, ROW1, 0])
        land2.move_to([NX, ROW2, 0]).align_to(land1, LEFT)
        firsts = VGroup(*[Line(a.get_corner(DL) + DOWN * 0.12 + RIGHT * 0.05,
                               a.get_corner(DR) + DOWN * 0.12 + LEFT * 0.05,
                               color=YELLOW, stroke_width=4)
                          for a in (land1[0][1], land2[0][1])])
        with self.narrate("So closeness depends on which curve goes first. [pause 0.6] Bell A never "
                          "misses an eruption that happens. [pause 0.1] Bell B almost never imagines "
                          "one that doesn't.", gap=0) as beat:
            self.play(self.sm_c.animate.set_value(0.0), FadeOut(VGroup(tag_cv, c_lab)),
                      FadeIn(tag_data),
                      self.mu.animate.set_value(MB), self.sd.animate.set_value(SB),
                      FadeOut(b_dim), self.a_op.animate.set_value(1.0),
                      Write(land1), Write(land2),
                      run_time=beat.until("first", offset=-0.5), rate_func=SMOOTH)
            self.play(Create(firsts), run_time=0.6)
            beat.wait_until("Bell A", offset=-0.1)
            self.play(FadeOut(firsts), self.bar_op.animate.set_value(0.75),
                      Indicate(lab_A, color=YELLOW), run_time=1.0)
            self.play(self.bar_op.animate.set_value(0.42), run_time=0.6)
            beat.wait_until("Bell B", offset=-0.1)
            self.bell_fill_x.set_value(7.0)
            self.play(self.bell_fill.animate.set_value(0.3), Indicate(lab_B, color=YELLOW),
                      run_time=1.2)

        for m in self.mobjects:
            m.clear_updaters()
        self.end_card(hold=0.3)
