"""Sample Space, episode 9: Why Bell Curves Are Everywhere, and When They're Not.

The cold open asks how many bus waits an average needs before a test can trust the bell's
2.5% tails (textbook: 30).  More data never makes lopsided data bell-shaped; averaging does,
because the skewness of an average is the source's skewness over root n (measured, then drawn
as cubes), and the extra tail weight (excess kurtosis) fades as 1/n.  A test estimates the
spread from the same data, so its 95% interval misses lopsidedly (simulated: 7.2% / 1.0% at
n = 30); Kohavi et al.'s (KDD 2014) 355 s^2 rule is our formula and brings both misses to the
2-3% band at 1,420 waits, not 30.  For some data no sample size is enough: the condition
(finite variance) is broken by Gull's lighthouse, whose running average never settles while
the median does.

    videos/toolkit/render.sh --preview videos/episodes/009-central-limit-theorem/scene.py Episode /tmp/ep9.mp4
    videos/toolkit/render.sh videos/episodes/009-central-limit-theorem/scene.py Episode \
        videos/episodes/009-central-limit-theorem/final.mp4

Palette (see script.md): BLUE single pieces · YELLOW averages · GREEN the perfect bell ·
RED an extreme piece / infinite variance · PURPLE the median · GRAY/INK axes, sample sizes,
rules.  Data: data.npz from sim.py (simulated waits and flashes, seeded; the n = 30 / 300 /
1,420 panel distributions and the excess-kurtosis readings exact).
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from manim import *
from sample_space import *

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from narration_text import BEATS, GAP_AFTER, PRONUNCIATIONS as SAY, SPEED as VOICE_SPEED  # noqa: E402

D = np.load(HERE / "data.npz")
BAR_OPACITY = 0.85


def P(x, y):
    return np.array([x, y, 0.0])


def scale_opacity(m, factor):
    """Scale m's fill and stroke opacities in place (a pre-dimmed morph target)."""
    for a in m.get_family():
        a.set_fill(opacity=a.get_fill_opacity() * factor, family=False)
        a.set_stroke(opacity=a.get_stroke_opacity() * factor, family=False)
    return m


# ============================================================================ helpers
def hist_bars(ax, edges, values, color=BLUE, frac=0.86, opacity=BAR_OPACITY):
    """Rectangles for bins [edges[i], edges[i+1]) with heights `values` (axis units)."""
    g = VGroup()
    y0 = ax.c2p(edges[0], 0)[1]
    for lo, hi, v in zip(edges[:-1], edges[1:], values):
        xl, xr = ax.c2p(lo, 0)[0], ax.c2p(hi, 0)[0]
        h = max(ax.c2p(lo, v)[1] - y0, 0.004)
        r = Rectangle(width=(xr - xl) * frac, height=h, stroke_width=0, fill_color=color,
                      fill_opacity=opacity)
        r.move_to(P((xl + xr) / 2, y0 + h / 2))
        g.add(r)
    return g


def spike_bars(ax, xs, values, width, color=BLUE, opacity=BAR_OPACITY):
    """Bars centred on discrete values xs (axis units), `width` in axis x-units."""
    g = VGroup()
    y0 = ax.c2p(xs[0], 0)[1]
    for x, v in zip(xs, values):
        xl, xr = ax.c2p(x - width / 2, 0)[0], ax.c2p(x + width / 2, 0)[0]
        h = max(ax.c2p(x, v)[1] - y0, 0.004)
        r = Rectangle(width=xr - xl, height=h, stroke_width=0, fill_color=color,
                      fill_opacity=opacity)
        r.move_to(P((xl + xr) / 2, y0 + h / 2))
        g.add(r)
    return g


def normal_curve(ax, mean, sd, binw, lo, hi, color=GREEN, width=4):
    """Normal density as 'percent per bin of width binw' on axes ax."""
    def f(x):
        return 100 * binw * np.exp(-0.5 * ((x - mean) / sd) ** 2) / (sd * np.sqrt(2 * np.pi))
    return ax.plot(f, x_range=[lo, hi, (hi - lo) / 160], color=color, stroke_width=width)


def place(ax, origin_xy, x0=0.0):
    """Shift axes so that data point (x0, 0) sits at origin_xy."""
    ax.shift(P(*origin_xy) - ax.c2p(x0, 0))
    return ax


def emph(m, scale=1.12, run_time=0.8):
    """Colour-preserving scale pulse (<= 1 s) for labels and chips, never for data bars."""
    return m.animate(rate_func=there_and_back, run_time=run_time).scale(scale)


def glow(m, alpha=0.45, run_time=0.8):
    """Brightness flag (<= 1 s): fills flash toward white and back.  Bar heights never change."""
    t = m.copy()
    t.clear_updaters()
    for a in t.get_family():
        if a.get_fill_opacity() > 0:
            a.set_fill(interpolate_color(ManimColor(a.get_fill_color()), ManimColor(WHITE), alpha),
                       family=False)
    return Transform(m, t, rate_func=there_and_back, run_time=run_time)


def swap_clean(scene, used, clean):
    """TransformFromCopy pads its target with duplicate glyphs while aligning; stacked
    duplicates then ignore dimming.  Swap every on-screen holder of `used` for `clean`,
    an identical copy taken before any animation."""
    fam = set(map(id, used.get_family()))
    for m in list(scene.mobjects):
        pts = [x for x in m.get_family() if x.has_points()]
        if pts and any(id(x) in fam for x in pts):
            scene.remove(m)
    scene.add(clean)
    return clean


def dimmed(m, factor):
    """Transform to a copy whose fill and stroke opacities are scaled by `factor` (curves and
    outlines stay unfilled, unlike set_opacity)."""
    t = m.copy()
    t.clear_updaters()
    for a, b in zip(m.get_family(), t.get_family()):
        b.set_fill(opacity=a.get_fill_opacity() * factor, family=False)
        b.set_stroke(opacity=a.get_stroke_opacity() * factor, family=False)
    return Transform(m, t)


def consolidate(scene, group):
    """Replace loose top-level pieces of `group` (left by transforms into its parts) by group."""
    fam = set(map(id, group.get_family()))
    for m in list(scene.mobjects):
        if m is not group and all(id(x) in fam for x in m.get_family()):
            scene.remove(m)
    scene.add(group)
    return group


def _first_half(t):
    return smooth(min(1.0, t / 0.45))


def _second_half(t):
    return smooth(max(0.0, (t - 0.55) / 0.45))


def roll(old, new, dist=0.22):
    """Swap a changed term without a double exposure: the old one leaves upward in the first
    half of the animation, the new one rises into place in the second half."""
    return [FadeOut(old, shift=UP * dist, rate_func=_first_half),
            FadeIn(new, shift=UP * dist, rate_func=_second_half)]


def late_in(t):
    return smooth(max(0.0, (t - 0.6) / 0.4))


def chip(value: str, color, size=MATH, width=1.0) -> VGroup:
    t = MathTex(value, font_size=size, color=INK)
    box_ = RoundedRectangle(width=max(width, t.width + 0.4), height=0.56, corner_radius=0.1,
                            stroke_color=color, stroke_width=3, fill_color=color, fill_opacity=0.16)
    t.move_to(box_)
    return VGroup(box_, t)


def bracket(x0, x1, y, color, tick=0.12, stroke=4):
    return VGroup(Line(P(x0, y), P(x1, y), color=color, stroke_width=stroke),
                  Line(P(x0, y - tick), P(x0, y + tick), color=color, stroke_width=stroke),
                  Line(P(x1, y - tick), P(x1, y + tick), color=color, stroke_width=stroke))


def pct(value, color=YELLOW, size=34):
    """A DecimalNumber percentage (1 decimal: the miss rates are simulated) for the meter."""
    return DecimalNumber(value, num_decimal_places=1, unit=r"\%", font_size=size, color=color,
                         unit_buff_per_font_unit=0.0)


CUBE_A = 0.28                                   # edge of one unit cube (the 'why root n' picture)
CUBE_D = np.array([0.45, 0.35, 0.0]) * CUBE_A   # oblique depth offset


def cube(o, color, z=0):
    """A flat-shaded unit cube (front, top, side faces) with front-bottom-left corner o."""
    a, d = CUBE_A, CUBE_D
    c = ManimColor(color)
    faces = [
        (Polygon(o, o + a * RIGHT, o + a * RIGHT + a * UP, o + a * UP), c),
        (Polygon(o + a * UP, o + a * RIGHT + a * UP, o + a * RIGHT + a * UP + d, o + a * UP + d),
         interpolate_color(c, ManimColor(WHITE), 0.3)),
        (Polygon(o + a * RIGHT, o + a * RIGHT + d, o + a * RIGHT + a * UP + d, o + a * RIGHT + a * UP),
         interpolate_color(c, ManimColor(BG), 0.45)),
    ]
    g = VGroup(*[f.set_fill(col, opacity=1).set_stroke(BG, width=1.5) for f, col in faces])
    g.set_z_index(z)
    return g


def marker(x, y, val, name):
    """A required sample size on the log axis: INK dot and value, gray name."""
    d = Dot(P(x, y), radius=0.09, color=INK)
    v = MathTex(val, font_size=MATH, color=INK).next_to(d, UP, buff=0.2)
    nm = Text(name, font_size=LABEL - 2, color=GRAY).next_to(v, UP, buff=0.18)
    return VGroup(d, v, nm)


# ============================================================================ layout
SRC_O = (-5.6, -2.0)               # big source histogram origin (data (0,0))
SRC_W, SRC_H = 7.0, 4.1
CH_O = (2.95, -2.0)                # skewness chart origin (clear of the histogram's 50 tick)
BELL_C = 4.6                       # centre of the predicted bell (cold open + landing)
PX = [-4.1, -1.033, 2.033, 5.1]    # panel centres (room for the y ticks and rotated 'share (%)')
PW, PH, PY0 = 2.5, 2.3, 0.55       # panel width, height, axis y
HEAD_Y = 3.22
XLAB_Y = -0.17
READ_Y = -1.05
FRAC_Y = -2.05
KR_Y = -1.85                       # excess-kurtosis readings, under the skew readings
FORM_Y = -2.67                     # the formula row during the kurtosis beat
NS = [1, 4, 16, 64]
WIN = {1: (0, 50), 4: (-7.5, 30), 16: (1.25, 20), 64: (5.625, 15)}
TICKS = {1: [0, 20, 40], 4: [0, 10, 20], 16: [5, 10, 15], 64: [6, 10, 14]}
BIG_L, BIG_W, BIG_B, BIG_H = -6.0, 4.8, 0.15, 1.9      # the n = 30 panel
ROW1, ROW2, RX = 1.6, -0.08, 3.95                       # payoff equation rows (right column):
ROW_D, ROW_R = ROW1, ROW2                               # derived inequality above, Kohavi's rule below
READ_P = (0.16, 2.95)                                   # the average's skewness, above the meter
MX, M_S, M_W = (-0.42, 0.74), 0.25, 0.42                # miss meter: bar x, units per %, width
SHORE_Y = -1.0                     # lighthouse map: 1 unit = 1 mile
LAMP = P(0, SHORE_Y + 1.0)
STRIP_Y = -2.3
TP_L, TP_R, TP_B, TP_T = -5.2, 5.2, 1.05, 3.0    # trace plot box
TP_MID = (TP_B + TP_T) / 2
TP_S = (TP_T - TP_B) / 6.0                       # units per mile (+-3 miles)


def tp(k, v):
    return P(TP_L + (TP_R - TP_L) * k / 1000.0, TP_MID + TP_S * float(np.clip(v, -2.9, 2.9)))


def meter_bar(i, value):
    h = max(M_S * value, 0.002)
    return Rectangle(width=M_W, height=h, stroke_width=0, fill_color=YELLOW,
                     fill_opacity=BAR_OPACITY).move_to(P(MX[i], BIG_B + h / 2))


class Episode(NarratedScene):
    EPISODE = 9
    TITLE = "Why Bell Curves Are Everywhere, and When They're Not"
    PRONUNCIATIONS = SAY
    SPEED = VOICE_SPEED

    def beat(self, key):
        """Narrate one beat with its planned trailing silence (see narration_text.GAP_AFTER)."""
        return self.narrate(BEATS[key], gap=GAP_AFTER[key])

    # ------------------------------------------------------------------ builders
    def src_axes(self):
        ax = axes((0, 50), (0, 25), x_length=SRC_W, y_length=SRC_H,
                  x_ticks=[0, 10, 20, 30, 40, 50], y_ticks=[0, 10, 20],
                  x_label="wait (minutes)", y_label="share of waits (%)")
        return place(ax, SRC_O)

    def panel_axes(self, i, xr, ticks, ymax, numbers=True, yt=()):
        ax = axes(xr, (0, ymax), x_length=PW, y_length=PH, x_ticks=ticks, y_ticks=list(yt),
                  numbers=numbers)
        if numbers and len(yt):
            for num in ax.y_axis.numbers:                # tick labels at the BAR minimum size
                num.scale(26 / MATH_SMALL, about_edge=RIGHT)
        return place(ax, (PX[i] - PW / 2, PY0), x0=xr[0])

    def big_axes(self, edges, ticks, decimals=0):
        ax = axes((edges[0], edges[-1]), (0, 12.5), x_length=BIG_W, y_length=BIG_H,
                  x_ticks=ticks, y_ticks=[], x_decimals=decimals)
        ax.y_axis.set_opacity(0)
        return place(ax, (BIG_L, BIG_B), x0=edges[0])

    def prediction(self, label="average of 30"):
        """Cold-open right side: arrow -> dashed bell with a question mark, and three guesses."""
        arrow = Arrow(P(1.8, 0.2), P(3.2, 0.2), color=GRAY, stroke_width=4, buff=0)
        more = Text(label, font_size=LABEL - 2, color=INK).next_to(arrow, UP, buff=0.18)
        def bell_y(x):
            return -2.0 + 2.55 * np.exp(-0.5 * ((x - BELL_C) / 0.52) ** 2)
        bell = FunctionGraph(bell_y, x_range=[BELL_C - 1.25, BELL_C + 1.25], color=GREEN, stroke_width=4)
        dashed = DashedVMobject(bell, num_dashes=34)

        def tail_area(a, b):
            xs = np.linspace(a, b, 24)
            return Polygon(P(a, -2.0), *[P(x, bell_y(x)) for x in xs], P(b, -2.0), stroke_width=0,
                           fill_color=GREEN, fill_opacity=0.45)
        zc = 1.96 * 0.52                                   # the bell's 2.5% cut points
        tails = VGroup(tail_area(BELL_C - 1.25, BELL_C - zc), tail_area(BELL_C + zc, BELL_C + 1.25))
        t_lbls = VGroup(*[MathTex(r"2.5\%", font_size=28, color=GREEN).move_to(P(BELL_C + s * 1.42, -1.33))
                          for s in (-1, 1)])
        base = Line(P(BELL_C - 1.35, -2.0), P(BELL_C + 1.4, -2.0), color=GRAY, stroke_width=2.5)
        qmark = MathTex("?", font_size=80, color=INK).move_to(P(BELL_C, -1.15))
        chips = VGroup(chip("30", GRAY, 36, 0.8), chip("300", GRAY, 36, 0.8),
                       chip(r"1{,}000{+}", GRAY, 36, 0.8)).arrange(RIGHT, buff=0.22)
        chips.move_to(P(4.45, -2.68))
        return arrow, more, dashed, base, qmark, chips, tails, t_lbls

    # ------------------------------------------------------------------ construct
    def construct(self):
        self.part_raw()
        self.part_average()
        self.part_how_many()
        self.part_lighthouse()
        self.part_landing()

    # ================================================================== 1-4 raw data
    def part_raw(self):
        edges, shares = D["src_edges"], D["src_shares"] * 100
        ax = self.src_axes()
        bars = hist_bars(ax, edges, shares[0])
        count = Text("100 waits", font_size=LABEL, color=INK)
        count.move_to(P(ax.c2p(50, 0)[0] - count.width / 2, 2.5))
        sim_tag = text("simulated", size=SMALL, color=GRAY, slant=ITALIC)
        sim_tag.next_to(count, DOWN, buff=0.15).align_to(count, RIGHT)
        self.add(ax, bars, count, sim_tag)
        self.src_ax, self.src_bars, self.count, self.sim_tag = ax, bars, count, sim_tag
        arrow, more, dashed, base, qmark, chips, tails, t_lbls = self.prediction()
        head = VGroup(*bars[:8])                                       # 0-20 min
        tail_brace = Brace(Line(ax.c2p(20, 7), ax.c2p(45, 7)), direction=UP, color=GRAY)
        tail_lbl = Text("tail", font_size=LABEL, color=GRAY).next_to(tail_brace, UP, buff=0.2)
        cite_m = citation("Montgomery & Runger, 2010")
        cite_k = citation("Kohavi et al., 2014 · KDD")

        # ---- beat 1: cold open -> commit to a number
        with self.beat("open") as beat:
            self.play(LaggedStart(*[glow(b, 0.35, 0.6) for b in bars], lag_ratio=0.05),
                      emph(count, 1.1), run_time=beat.until("mostly", offset=-0.1, min_time=1.2))
            beat.wait_until("short", offset=-0.3)
            self.play(LaggedStart(*[glow(b, 0.5, 0.6) for b in bars[:4]], lag_ratio=0.12), run_time=0.8)
            beat.wait_until("tail", offset=-0.4)
            self.play(head.animate.set_fill(opacity=0.4), GrowFromCenter(tail_brace),
                      FadeIn(tail_lbl, shift=0.1 * DOWN), run_time=0.6)
            beat.wait_until("Textbooks", offset=-0.1)
            self.play(FadeIn(cite_m), run_time=0.6)
            beat.wait_until("average", offset=-0.2)
            self.play(GrowArrow(arrow), FadeIn(more, shift=0.1 * RIGHT), run_time=0.8)
            # the brace has been read (>= 2 s): it steps back to 40% and stays until the guesses
            self.play(head.animate.set_fill(opacity=BAR_OPACITY), tail_brace.animate.set_opacity(0.4),
                      tail_lbl.animate.set_opacity(0.4), run_time=0.5)
            beat.wait_until("bell", offset=-0.35)
            self.play(Create(base), Create(dashed), run_time=beat.until("does", offset=-0.1, min_time=0.8))
            self.play(FadeIn(qmark, scale=0.8), run_time=0.5)
            for i, cue in enumerate([("thirty", 2), ("three hundred", 1), ("over", 1)]):
                beat.wait_until(cue[0], cue[1], offset=-0.15)
                extra = [FadeOut(tail_brace), FadeOut(tail_lbl)] if i == 0 else []
                self.play(FadeIn(chips[i], shift=0.15 * UP), *extra, run_time=0.45)

        # ---- beat 2: stakes (the criterion: a test trusts the bell's two 2.5% tails)
        with self.beat("stakes") as beat:
            beat.wait_until("bell's", offset=-0.3)
            self.play(Indicate(dashed, color=GREEN, scale_factor=1.04), run_time=0.6)
            beat.wait_until("tails", offset=-0.2)
            self.play(FadeIn(tails), FadeIn(t_lbls, shift=0.1 * UP), run_time=0.7)
            beat.wait_until("revenue", offset=-0.2)
            self.play(FadeTransform(cite_m, cite_k), run_time=0.6)
            beat.wait_until("thirty", offset=-0.2)
            self.play(emph(chips[0], 1.22), run_time=0.9)

        # ---- beat 3: look for the bell in the data itself
        labels = ["1,000 waits", "10,000 waits", "100,000 waits"]
        curve = ax.plot(lambda x: 100 * 0.25065 * np.exp(-x / 10), x_range=[0, 50, 0.25],
                        color=INK, stroke_width=4)
        pred = VGroup(arrow, more, dashed, base, qmark, chips, tails, t_lbls)
        with self.beat("collect") as beat:
            self.play(dimmed(pred, 0.3), FadeOut(cite_k), run_time=beat.until("collecting", offset=-0.2, min_time=0.6))
            self.play(LaggedStart(*[glow(b, 0.35, 0.6) for b in bars], lag_ratio=0.04),
                      run_time=beat.until("Collect a", offset=-0.3, min_time=0.9))
            cues = ["thousand", "ten thousand", "hundred thousand"]
            beat.wait_until(cues[0], offset=-0.3)
            for i, cue in enumerate(cues):
                newc = Text(labels[i], font_size=LABEL, color=INK)
                newc.move_to(count).align_to(count, RIGHT)
                rt = beat.until(cues[i + 1], offset=-0.3, min_time=0.5) if i < 2 else 0.9
                self.play(Transform(bars, hist_bars(ax, edges, shares[i + 1])),
                          FadeTransform(count, newc), run_time=rt)
                count = newc
            beat.wait_until("shape", offset=-0.2)
            self.play(Create(curve), run_time=1.4, rate_func=SMOOTH)
        self.curve, self.count = curve, count

        # ---- beat 4: measured failure: skewness, defined term by term, stays at two
        ch = axes((0.4, 4.9), (0, 2.5), x_length=2.7, y_length=SRC_H, x_ticks=[1, 2, 3, 4],
                  y_ticks=[0, 1, 2])
        place(ch, CH_O, x0=0.4)
        ch.x_axis.remove(ch.x_axis.numbers)
        xl = VGroup(*[MathTex(f"10^{k}", font_size=MATH_SMALL, color=GRAY)
                      .next_to(ch.c2p(i + 1, 0), DOWN, buff=0.2) for i, k in enumerate([2, 3, 4, 5])])
        xt = Text("waits collected", font_size=LABEL - 2, color=GRAY)
        xt.next_to(xl, DOWN, buff=0.16).align_to(ch.x_axis.get_right(), RIGHT)
        zero_lbl = ch.y_axis.numbers[0]
        bell_lbl = Text("bell", font_size=LABEL, color=GREEN).next_to(zero_lbl, LEFT, buff=0.15)
        zero_line = DashedLine(ch.c2p(0.4, 0), ch.c2p(4.9, 0), color=GREEN, stroke_width=4,
                               dash_length=0.12)
        defn = MathTex(r"\text{skewness}", "=", r"\frac{E\big[(x-\mu)^3\big]}{\sigma^3}", font_size=36)
        defn.move_to(P(2.5 + defn.width / 2, 2.3 + defn.height / 2))
        defn[2][0:9].set_color(BLUE)
        # the referent of "gap from the mean": the mean line, one long wait's gap, one short one's
        mu_line = DashedLine(ax.c2p(10, 0), ax.c2p(10, 15), color=GRAY, stroke_width=3, dash_length=0.1)
        mu_lbl = MathTex(r"\mu", font_size=36, color=GRAY).next_to(mu_line, UP, buff=0.1)
        dist = DoubleArrow(ax.c2p(10, 12), ax.c2p(35, 12), color=BLUE, stroke_width=4, buff=0,
                           tip_length=0.2)
        dist_lbl = MathTex(r"x-\mu", font_size=36, color=BLUE).next_to(dist, UP, buff=0.12)
        neg = Arrow(ax.c2p(10, 19), ax.c2p(3.5, 19), color=BLUE, stroke_width=4, buff=0,
                    max_tip_length_to_length_ratio=0.25)
        neg_lbl = MathTex(r"x-\mu<0", font_size=30, color=BLUE)
        neg_lbl.move_to(P(ax.c2p(9.0, 0)[0], neg.get_center()[1] + 0.42))
        skews = D["src_skew"]
        sbars = VGroup(*[Rectangle(width=0.42, height=max(ch.c2p(0, s)[1] - ch.c2p(0, 0)[1], 0.01),
                                   stroke_width=0, fill_color=BLUE, fill_opacity=BAR_OPACITY)
                         .move_to(ch.c2p(i + 1, 0), aligned_edge=DOWN) for i, s in enumerate(skews)])
        vlabs = VGroup(*[MathTex(f"{s:.2f}", font_size=28, color=BLUE).next_to(b, UP, buff=0.17)
                         for s, b in zip(skews, sbars)])
        gap = Brace(Line(ch.c2p(4.4, 0), ch.c2p(4.4, 2.0)), direction=RIGHT, color=GRAY, buff=0.05)
        gap_lbl = VGroup(Text("gap", font_size=LABEL - 2, color=GRAY),
                         MathTex(r"\approx 2", font_size=32, color=GRAY)).arrange(DOWN, buff=0.08)
        gap_lbl.next_to(gap, RIGHT, buff=0.16)
        with self.beat("fail") as beat:
            self.play(FadeOut(pred), run_time=0.5)
            self.play(FadeIn(ch), FadeIn(xl), FadeIn(xt), Write(defn[0:2]),
                      run_time=beat.until("average", offset=-0.3, min_time=1.0))
            self.play(Create(mu_line), FadeIn(mu_lbl), GrowFromCenter(dist), FadeIn(dist_lbl),
                      run_time=0.7)
            beat.wait_until("gap", offset=-0.1)
            self.play(TransformFromCopy(dist_lbl, defn[2][3:6]), FadeIn(defn[2][0:3]), FadeIn(defn[2][6:9]),
                      run_time=beat.until("left", offset=-0.15, min_time=0.8))
            self.play(GrowArrow(neg), FadeIn(neg_lbl), run_time=0.5)
            beat.wait_until("over", offset=-0.45)
            self.play(FadeOut(neg), FadeOut(neg_lbl), run_time=0.35)
            self.play(GrowFromCenter(defn[2][9]), Write(defn[2][10:]), run_time=0.8)
            beat.wait_until("perfect", offset=-0.25)
            self.play(FadeOut(VGroup(mu_line, mu_lbl, dist, dist_lbl)),
                      zero_lbl.animate.set_color(GREEN), FadeIn(bell_lbl, shift=0.1 * RIGHT),
                      Create(zero_line), run_time=0.8)
            beat.wait_until("two", offset=-0.35)
            self.play(LaggedStart(*[AnimationGroup(GrowFromEdge(b, DOWN), FadeIn(v, shift=0.1 * UP))
                                    for b, v in zip(sbars, vlabs)], lag_ratio=0.25),
                      run_time=beat.until("every", offset=0.4, min_time=1.2))
            self.play(GrowFromCenter(gap), FadeIn(gap_lbl), run_time=0.7)
        defn = swap_clean(self, defn, defn.copy())
        self.chart = VGroup(ch, xl, xt, bell_lbl, zero_line, defn, gap, gap_lbl)
        self.sbars, self.vlabs = sbars, vlabs

    # ================================================================== 5-8 averages
    def part_average(self):
        ex = D["example4"]
        # ---- panel row (shares in %, one tick per panel: panel 1 has its own, taller scale)
        ymax = {1: 25}
        for n in NS[1:]:
            ymax[n] = 14.0
        pax = [self.panel_axes(i, WIN[n], TICKS[n], ymax[n], yt=(10, 20) if n == 1 else (10,))
               for i, n in enumerate(NS)]
        heads = VGroup(*[MathTex("n", "=", str(n), font_size=MATH).move_to(P(PX[i], HEAD_Y))
                         for i, n in enumerate(NS)])
        xshared = Text("average of n waits (minutes)", font_size=LABEL - 2, color=GRAY)
        xshared.move_to(P(0, XLAB_Y))
        ylab = Text("share (%)", font_size=LABEL - 4, color=GRAY).rotate(PI / 2)
        ylab.move_to(P(pax[0].y_axis.numbers.get_left()[0] - 0.17 - ylab.width / 2, PY0 + PH / 2))
        new_src = hist_bars(pax[0], D["src_edges"], D["src_shares"][3] * 100)
        avg_bars = {n: hist_bars(pax[i], D[f"avg{n}_edges"], D[f"avg{n}_shares"] * 100, color=YELLOW)
                    for i, n in enumerate(NS) if n > 1}
        reads = VGroup()
        vals = [D["src_skew"][3], D["avg4_skew"], D["avg16_skew"], D["avg64_skew"]]
        for i, v in enumerate(vals):
            r = MathTex(r"\text{skew} =", f"{v:.2f}", font_size=MATH)
            r[1].set_color(BLUE if i == 0 else YELLOW)
            r.move_to(P(PX[i], READ_Y))
            reads.add(r)
        sim_tag2 = text("simulated", size=SMALL, color=GRAY, slant=ITALIC)
        sim_tag2.move_to(P(6.3 - sim_tag2.width / 2, XLAB_Y))

        # ---- beat 5: average four waits (one long wait diluted by three short ones)
        chips = VGroup(*[chip(f"{v:.1f}", RED if v > 20 else BLUE) for v in ex])
        for c, x in zip(chips, [-2.6, -1.25, 0.1, 1.45]):
            c.move_to(P(x, FRAC_Y))
        bins = [int(v // 2.5) for v in ex]
        eq = MathTex(r"\frac{5.2+1.8+25.7+5.3}{4}", "=", f"{ex.mean():.1f}", font_size=MATH)
        eq.move_to(P(-0.9, FRAC_Y))
        terms = [eq[0][0:3], eq[0][4:7], eq[0][8:12], eq[0][13:16]]
        for t, v in zip(terms, ex):
            t.set_color(RED if v > 20 else BLUE)
        pluses = VGroup(eq[0][3], eq[0][7], eq[0][12])
        eq[2].set_color(YELLOW).shift(RIGHT * 0.12)
        ybox = SurroundingRectangle(eq[2], buff=0.12, corner_radius=0.1, color=YELLOW, stroke_width=3,
                                    fill_color=YELLOW, fill_opacity=0.16)
        big = self.src_ax
        keep = self.vlabs[3]                                   # the 1.98 reading travels on
        # full size, straight below its own bar: it drops out of the chart as the chart fades
        # (late, so it never crosses a bar that is still visible), then slides along the
        # readings row to panel 1 once the shrinking histogram has risen above that row
        mid = MathTex(f"{D['src_skew'][3]:.2f}", font_size=MATH, color=BLUE)
        mid.move_to(P(keep.get_center()[0], READ_Y))

        def drop_late(t):
            return smooth(max(0.0, (t - 0.35) / 0.65))

        def slide_late(t):
            return smooth(max(0.0, (t - 0.3) / 0.65)) if t < 0.95 else 1.0
        with self.beat("average") as beat:
            self.play(FadeOut(self.chart, rate_func=_first_half), FadeOut(self.sbars, rate_func=_first_half),
                      FadeOut(VGroup(*self.vlabs[:3])), FadeOut(self.curve), FadeOut(self.count),
                      FadeOut(self.sim_tag), FadeOut(big),
                      ReplacementTransform(keep, mid, rate_func=drop_late), run_time=0.7)
            self.play(ReplacementTransform(self.src_bars, new_src), *[FadeIn(a) for a in pax],
                      FadeIn(heads), FadeIn(xshared), FadeIn(ylab), FadeIn(sim_tag2),
                      ReplacementTransform(mid, reads[0][1], rate_func=slide_late),
                      FadeIn(reads[0][0], rate_func=late_in), run_time=1.2)
            beat.wait_until("Four", offset=-0.1)
            self.play(LaggedStart(*[TransformFromCopy(new_src[b], c, path_arc=0.4) for b, c in zip(bins, chips)],
                                  lag_ratio=0.15), run_time=beat.until("the one", offset=-0.1, min_time=1.0))
            beat.wait_until("long", offset=-0.15)
            self.play(emph(chips[2], 1.18), run_time=0.8)
            beat.wait_until("diluted", offset=-0.2)
            self.play(*[ReplacementTransform(c[1], t) for c, t in zip(chips, terms)],
                      *[FadeOut(c[0]) for c in chips], run_time=0.8)
            self.play(FadeIn(pluses), GrowFromCenter(eq[0][16]), FadeIn(eq[0][17], shift=0.15 * UP),
                      run_time=0.6)
            self.play(FadeIn(eq[1]), Write(eq[2]), Create(ybox), run_time=0.6)
            consolidate(self, eq)
            drop = Dot(pax[1].c2p(ex.mean(), 0) + UP * 0.09, radius=0.09, color=YELLOW)
            beat.wait_until("here", offset=-0.55)
            dot0 = Dot(ybox.get_center(), radius=0.09, color=YELLOW)
            self.play(ReplacementTransform(VGroup(ybox, eq[2]), dot0), FadeOut(VGroup(eq[0], eq[1])),
                      run_time=0.4)
            self.play(ReplacementTransform(dot0, drop, path_arc=0.5), run_time=0.6)
            beat.wait_until("Do", offset=-0.1)
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in avg_bars[4]], lag_ratio=0.04),
                      FadeOut(drop), run_time=beat.remaining(min_time=1.6))

        # ---- beat 6: readings and the green bell (the n = 4 bell is drawn whole: the part
        # below 0 minutes, which no average reaches, is dimmed)
        bells = VGroup()
        for i, n in enumerate(NS[1:], start=1):
            lo, hi = WIN[n]
            if lo < 0:
                neg = normal_curve(pax[i], 10, 10 / np.sqrt(n), (hi - lo) / 24, lo, 0)
                neg.set_stroke(opacity=0.4)
                bells.add(VGroup(neg, normal_curve(pax[i], 10, 10 / np.sqrt(n), (hi - lo) / 24, 0, hi)))
            else:
                bells.add(normal_curve(pax[i], 10, 10 / np.sqrt(n), (hi - lo) / 24, lo, hi))
        with self.beat("avg") as beat:
            beat.wait_until("skewness", offset=-0.2)
            self.play(Write(reads[1]), run_time=0.8)
            beat.wait_until("Sixteen", offset=-0.3)
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in avg_bars[16]], lag_ratio=0.04),
                      run_time=beat.until("point five", offset=-0.2, min_time=1.0))
            self.play(Write(reads[2]), run_time=0.7)
            beat.wait_until("Sixty", offset=-0.3)
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in avg_bars[64]], lag_ratio=0.04),
                      run_time=beat.until("point two five", offset=-0.2, min_time=1.0))
            self.play(Write(reads[3]), run_time=0.7)
            beat.wait_until("perfect", offset=-0.2)
            self.play(LaggedStart(*[Create(b) for b in bells], lag_ratio=0.25),
                      run_time=beat.remaining(min_time=1.2))

        # ---- beat 7: the formula from the readings
        x4 = VGroup()
        for i in range(3):
            a = Arrow(heads[i].get_right() + RIGHT * 0.25, heads[i + 1].get_left() + LEFT * 0.25,
                      color=GRAY, stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.12)
            lab = MathTex(r"\times 4", font_size=MATH_SMALL, color=INK).next_to(a, UP, buff=0.06)
            x4.add(VGroup(a, lab))
        d2 = VGroup()
        for i in range(3):
            a = Arrow(reads[i].get_right() + RIGHT * 0.27, reads[i + 1].get_left() + LEFT * 0.27,
                      color=GRAY, stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.2)
            a.shift(UP * 0.04)
            lab = MathTex(r"\div 2", font_size=MATH_SMALL, color=INK).next_to(a, UP, buff=0.17)
            d2.add(VGroup(a, lab))
        exact = ["2", "1", "0.5", "0.25"]
        fracs = VGroup()
        for i, n in enumerate(NS):
            f = MathTex(r"\frac{2}{\sqrt{%d}}" % n, "=", exact[i], font_size=MATH)
            f[0][0].set_color(BLUE)
            f[2].set_color(BLUE if i == 0 else YELLOW)
            f.move_to(P(PX[i], FRAC_Y))
            fracs.add(f)
        t1 = MathTex(r"\text{skew}(\bar{x})", "=", r"\frac{2}{\sqrt{n}}", font_size=EQ - 6)
        t1[0].set_color(YELLOW)
        t1[2][0].set_color(BLUE)
        t1.move_to(P(0, FRAC_Y))
        gen = MathTex(r"\text{skew}(\bar{x})", "=", r"\frac{\text{skew}(x)}{\sqrt{n}}", font_size=EQ - 6)
        gen[0].set_color(YELLOW)
        gen[2][0:7].set_color(BLUE)
        gen.move_to(P(0, FRAC_Y))
        gen_clean, gen_home = gen.copy(), gen.copy()
        with self.beat("formula") as beat:
            beat.wait_until("grows", offset=-0.3)
            self.play(LaggedStart(*[GrowArrow(g[0]) for g in x4], lag_ratio=0.25),
                      LaggedStart(*[FadeIn(g[1]) for g in x4], lag_ratio=0.25),
                      run_time=beat.until("times", end=True, offset=-0.1, min_time=0.8))
            beat.wait_until("halves", offset=-0.3)
            self.play(LaggedStart(*[GrowArrow(g[0]) for g in d2], lag_ratio=0.2),
                      LaggedStart(*[FadeIn(g[1]) for g in d2], lag_ratio=0.2), run_time=0.7)
            beat.wait_until("two over", offset=-0.3)
            # 2 / root n under each reading: the 2 is one wait's skewness (blue), the radicand is
            # that panel's n (each header pulses as its fraction is written; nothing flies)
            self.play(LaggedStart(*[AnimationGroup(Write(f), emph(heads[i][2], 1.3))
                                    for i, f in enumerate(fracs)], lag_ratio=0.1), run_time=0.8)
            # held while "and two is" is spoken; then the four 2 / root n become one, and
            # skew(x-bar) = arrives in the cleared space
            beat.wait_until("skewness of", offset=-0.2)
            self.play(ReplacementTransform(VGroup(*[f[0][0] for f in fracs]), t1[2][0]),
                      ReplacementTransform(VGroup(*[f[0][1] for f in fracs]), t1[2][1]),
                      ReplacementTransform(VGroup(*[f[0][2] for f in fracs]), t1[2][2]),
                      ReplacementTransform(VGroup(*[f[0][3] for f in fracs]), t1[2][3]),
                      *[FadeOut(f[0][4:]) for f in fracs], *[FadeOut(f[1:], shift=0.12 * DOWN) for f in fracs],
                      FadeIn(t1[2][4]), run_time=0.5)
            self.play(FadeIn(t1[0:2], shift=0.3 * RIGHT), run_time=0.35)
            # "... of one wait": the 2 becomes skew(x) while one wait's 1.98 pulses
            self.play(emph(reads[0][1], 1.25), ReplacementTransform(t1[0], gen[0]),
                      ReplacementTransform(t1[1], gen[1]), FadeTransform(t1[2][0], gen[2][0:7]),
                      ReplacementTransform(t1[2][1:], gen[2][7:]), run_time=0.7)
            self.play(Indicate(gen[2][0:7], color=BLUE, scale_factor=1.1), run_time=0.6)
            gen = swap_clean(self, gen, gen_clean)

        # ---- beat 7b: why root n, drawn: four waits -> cubed gaps x4; spread x2, so its cube x8
        genx = MathTex(r"\text{skew}(\bar{x})", "=", r"\frac{n}{n^{3/2}}", r"\cdot",
                       r"\frac{E\big[(x-\mu)^3\big]}{\sigma^3}", "=", r"\frac{\text{skew}(x)}{\sqrt{n}}",
                       font_size=40)
        genx[0].set_color(YELLOW)
        genx[2][0].set_color(BLUE)                 # x n: the cubed gaps
        genx[2][1].set_color(INK)
        genx[2][2:].set_color(GRAY)                # x n^{3/2}: the spread cubed
        genx[4][0:9].set_color(BLUE)
        genx[6][0:7].set_color(BLUE)
        genx.move_to(P(6.3 - genx.width / 2, FRAC_Y - 0.05))
        slot = DashedVMobject(RoundedRectangle(width=genx[2].width + 0.1, height=genx[2].height + 0.1,
                                               corner_radius=0.08, color=GRAY, stroke_width=2.5)
                              .move_to(genx[2]), num_dashes=24)
        A, B0, GX = CUBE_A, -2.66, -3.7
        blue = VGroup(*[cube(P(-6.25 + k * 0.35, B0), BLUE, z=k) for k in range(4)])
        gray_c = interpolate_color(ManimColor(INK), ManimColor(BG), 0.42)
        # 2 x 2 x 2, drawn back to front, bottom to top, left to right (z_index = draw order)
        spots = [(x, y, z) for z in (1, 0) for y in (0, 1) for x in (0, 1)]
        gcubes = VGroup(*[cube(P(GX, B0) + x * A * RIGHT + y * A * UP + z * CUBE_D, gray_c, z=10 + k)
                          for k, (x, y, z) in enumerate(spots)])
        home = spots.index((0, 0, 0))
        gunit = gcubes[home].copy()
        cap_b = Text("cubed gaps", font_size=SMALL, color=BLUE).move_to(P(blue.get_center()[0], -3.0))
        cap_g = MathTex(r"\text{spread}^3", font_size=30, color=GRAY).move_to(P(GX + A, -3.0))
        # the spread itself: one wait's sigma, then the four-wait sum's 2 sigma (= root 4 sigma)
        y1 = B0 + A + CUBE_D[1] + 0.3
        y2 = B0 + 2 * A + 2 * CUBE_D[1] + 0.28
        bar1 = bracket(GX, GX + A, y1, GRAY, tick=0.08, stroke=4)
        bar2 = bracket(GX, GX + 2 * A, y2, GRAY, tick=0.08, stroke=4)
        sig = MathTex(r"\sigma", font_size=34, color=GRAY).next_to(bar1, RIGHT, buff=0.16)
        x2 = MathTex(r"\times", "2", font_size=MATH, color=GRAY).next_to(bar2, RIGHT, buff=0.42)
        xrn = MathTex(r"\times", r"\sqrt{n}", font_size=MATH, color=GRAY).move_to(x2, aligned_edge=LEFT)
        lab4 = MathTex(r"\times", "4", font_size=MATH, color=BLUE).next_to(blue, RIGHT, buff=0.2)
        lab8 = MathTex(r"\times", "8", font_size=MATH, color=GRAY).next_to(gcubes, RIGHT, buff=0.2)
        lab4n = MathTex(r"\times", "n", font_size=MATH, color=BLUE).move_to(lab4, aligned_edge=LEFT)
        lab8n = MathTex(r"\times", "n^{3/2}", font_size=MATH, color=GRAY).move_to(lab8, aligned_edge=LEFT)
        with self.beat("why") as beat:
            beat.wait_until("comes", offset=-0.2)
            # the formula opens in place: '= skew(x)/root n' slides right, nothing is duplicated
            self.play(ReplacementTransform(gen[0], genx[0]), ReplacementTransform(gen[1], genx[5]),
                      ReplacementTransform(gen[2], genx[6]), run_time=0.7)
            # skew(x), opened up: the cubed gap over the spread cubed; an empty slot waits on the left
            self.play(FadeIn(genx[1]), Create(slot), FadeIn(genx[3]), Write(genx[4]),
                      Indicate(genx[6][0:7], color=BLUE, scale_factor=1.12),
                      run_time=beat.until("Add", offset=-0.2, min_time=0.6))
            # one wait's cubed gap and its spread cubed leave the formula as one cube each
            self.play(Indicate(genx[4][0:9], color=BLUE, scale_factor=1.08),
                      Indicate(genx[4][10:], color=INK, scale_factor=1.15),
                      GrowFromPoint(blue[0], genx[4][0:9].get_center()),
                      GrowFromPoint(gunit, genx[4][10:].get_center()),
                      FadeIn(cap_b), FadeIn(cap_g),
                      run_time=beat.until("cubed gaps", offset=-0.1, min_time=0.9))
            beat.wait_until("add up", offset=-0.2)
            self.play(LaggedStart(*[TransformFromCopy(blue[0], c) for c in blue[1:]], lag_ratio=0.3),
                      run_time=0.6)
            beat.wait_until("four times", offset=-0.15)
            self.play(FadeIn(lab4, shift=0.1 * RIGHT), run_time=0.5)
            beat.wait_until("spread", offset=-0.25)
            self.play(GrowFromEdge(bar1, LEFT), FadeIn(sig), run_time=0.5)
            beat.wait_until("doubles", offset=-0.25)
            self.play(Transform(bar1, bar2), FadeTransform(sig, x2), run_time=0.8)
            beat.wait_until("cube grows", offset=-0.15)
            self.remove(gunit)
            self.add(gcubes[home])
            order = [k for k in range(8) if k != home]
            self.play(LaggedStart(*[FadeIn(gcubes[k], shift=0.12 * DOWN) for k in order], lag_ratio=0.18),
                      run_time=beat.until("eight", offset=0.1, min_time=0.9))
            self.play(FadeIn(lab8, shift=0.1 * RIGHT), run_time=0.5)
            beat.wait_until("Four over", offset=-0.15)
            self.play(flag(lab4), flag(lab8, color=INK), run_time=0.8)
            beat.wait_until("half", offset=-0.2)
            self.play(Indicate(d2[0], color=YELLOW, scale_factor=1.2), run_time=0.8)
            beat.wait_until("In general", offset=-0.2)
            self.play(TransformMatchingTex(lab4, lab4n), TransformMatchingTex(lab8, lab8n),
                      TransformMatchingTex(x2, xrn), run_time=0.7)
            beat.wait_until("n over", offset=-0.15)
            self.play(TransformFromCopy(lab4n[1], genx[2][0], path_arc=-1.0), GrowFromCenter(genx[2][1]),
                      run_time=0.7)
            beat.wait_until("n to", offset=-0.1)
            self.play(TransformFromCopy(lab8n[1], genx[2][2:], path_arc=-1.3), FadeOut(slot), run_time=0.8)
            self.play(flag(genx[2]), run_time=0.7)
            genx = swap_clean(self, genx, genx.copy())
        picture = VGroup(blue, gcubes, bar1, xrn, lab4n, lab8n, cap_b, cap_g)
        # the proof has made its point: it closes back to skew(x-bar) = skew(x)/root n (in the
        # pause), so the next beat starts from one formula and the panels, nothing else
        gen = gen_home.copy().scale(42 / (EQ - 6)).move_to(P(3.2, FORM_Y))
        # first the middle of the expansion and the cubes leave, then the two ends close up
        # (nothing slides through a term that is still fading)
        self.play(FadeOut(genx[1:5]), FadeOut(picture), run_time=0.4)
        self.play(ReplacementTransform(genx[0], gen[0]), ReplacementTransform(genx[5], gen[1]),
                  ReplacementTransform(genx[6], gen[2]), run_time=0.6)

        # ---- beat 8: the extra tail weight fades faster still; only the bell survives
        kv = ["6", "1.5", "0.375", "0.094"]                 # exact: excess kurtosis of an average = 6/n
        kurts = VGroup()
        for i, v in enumerate(kv):
            if i == 0:
                k = MathTex(r"\text{ex. kurt} =", v, font_size=36)
                k[1].set_color(BLUE)
                k.shift(P(reads[0][1].get_center()[0], KR_Y) - k[1].get_center())
            else:
                k = MathTex(v, font_size=36, color=YELLOW).move_to(P(reads[i][1].get_center()[0], KR_Y))
            kurts.add(k)
        d4 = VGroup()
        for i in range(3):
            xa = kurts[i][-1].get_right()[0] if i else kurts[0][1].get_right()[0]
            xb = kurts[i + 1].get_left()[0]
            mid = (xa + xb) / 2
            a = Arrow(P(mid - 0.38, KR_Y), P(mid + 0.38, KR_Y), color=GRAY, stroke_width=3, buff=0,
                      max_tip_length_to_length_ratio=0.25)
            lab = MathTex(r"\div 4", font_size=MATH_SMALL, color=INK).next_to(a, UP, buff=0.16)
            d4.add(VGroup(a, lab))
        clt = Text("central limit theorem", font_size=36, color=INK).move_to(P(-3.0, FORM_Y + 0.26))
        cond_a = Text("independent pieces", font_size=LABEL - 4, color=GRAY)
        cond_b = Text("+ one condition", font_size=LABEL - 4, color=GRAY)
        VGroup(cond_a, cond_b).arrange(RIGHT, buff=0.18).move_to(P(-3.0, FORM_Y - 0.28))
        tail_bars = VGroup(*new_src[8:])                    # one wait's tail (20 minutes and longer)
        with self.beat("kurt") as beat:
            # the skew row steps back; the new reading starts under one wait's 1.98
            self.play(dimmed(VGroup(reads, d2), 0.4), Write(kurts[0]),
                      run_time=beat.until("extra", offset=-0.1, min_time=0.8))
            beat.wait_until("tail", offset=-0.2)
            self.play(glow(tail_bars, 0.5, 0.8), run_time=0.8)
            beat.wait_until("fades", offset=-0.15)
            self.play(LaggedStart(*[FadeIn(k, shift=0.12 * DOWN) for k in kurts[1:]], lag_ratio=0.3),
                      run_time=beat.until("quarters", offset=-0.2, min_time=0.9))
            self.play(LaggedStart(*[GrowArrow(g[0]) for g in d4], lag_ratio=0.2),
                      LaggedStart(*[FadeIn(g[1]) for g in d4], lag_ratio=0.2), run_time=0.7)
            beat.wait_until("Every", offset=-0.1)
            # every finer difference fades faster still: the bars close on their bells, panel by panel
            self.play(LaggedStart(*[Indicate(b, color=GREEN, scale_factor=1.05) for b in bells], lag_ratio=0.45),
                      run_time=beat.until("Only", offset=-0.25, min_time=1.5))
            self.play(glow(avg_bars[64], 0.45, 0.9), Indicate(bells[2], color=GREEN, scale_factor=1.06),
                      run_time=0.9)
            beat.wait_until("central", offset=-0.3)
            self.play(FadeIn(clt, shift=0.12 * UP), run_time=0.6)
            beat.wait_until("independent", offset=-0.15)
            self.play(FadeIn(cond_a, shift=0.1 * UP), run_time=0.5)
            beat.wait_until("one more", offset=-0.15)
            self.play(FadeIn(cond_b, shift=0.1 * UP), run_time=0.5)
        self.gen = gen
        # the n = 16 panel carries on into the textbook's n = 30; everything else leaves
        self.p16 = VGroup(pax[2], avg_bars[16], bells[1], heads[2])
        self.avg_rest = VGroup(pax[0], pax[1], pax[3], new_src, avg_bars[4], avg_bars[64], bells[0], bells[2],
                               heads[0], heads[1], heads[3], x4, d2, reads, kurts, d4, xshared, ylab,
                               sim_tag2, clt, cond_a, cond_b)

    # ================================================================== 9 how many
    def part_how_many(self):
        gen = self.gen
        top = gen.copy().move_to(P(RX, 2.85))
        cite1 = citation("Montgomery & Runger, 2010, via Kohavi et al., 2014")
        cite2 = citation("Kohavi et al., 2014 · KDD; rule from Boos & Hughes-Oliver, 2000")

        # exact distribution of the average of n waits (Gamma), for n = 30, 300, 1,420
        NS3 = (30, 300, 1420)
        TICK = {30: ([5, 10, 15], 0), 300: ([8, 10, 12], 0), 1420: ([9.5, 10, 10.5], 1)}
        AX, BARS, BELL, AREAS, HEAD = {}, {}, {}, {}, {}
        MID = slice(7, 21)                       # inside mean -/+ 1.96 sd (bin edges by construction)
        PDIM = 0.35                              # the panel steps back once the rule takes over
        for n in NS3:
            e, sh = D[f"tail{n}_edges"], D[f"tail{n}_shares"] * 100
            w, sd = e[1] - e[0], 10 / np.sqrt(n)
            AX[n] = self.big_axes(e, TICK[n][0], decimals=TICK[n][1])
            BARS[n] = hist_bars(AX[n], e, sh, color=YELLOW)
            BELL[n] = normal_curve(AX[n], 10, sd, w, e[0], e[-1])
            AREAS[n] = VGroup(AX[n].get_area(BELL[n], x_range=(e[0], e[7]), color=GREEN, opacity=0.35),
                              AX[n].get_area(BELL[n], x_range=(e[21], e[-1]), color=GREEN, opacity=0.35))
            HEAD[n] = MathTex("n", "=", {30: "30", 300: "300", 1420: r"1{,}420"}[n], font_size=MATH)
            HEAD[n].move_to(P(BIG_L + HEAD[n].width / 2, 2.95))
            if n != 30:                          # later panels arrive already dimmed
                for b in BARS[n][MID]:
                    b.set_fill(opacity=0.3)
                for m in (AX[n], BARS[n], BELL[n], AREAS[n], HEAD[n]):
                    scale_opacity(m, PDIM)
        ax30, bars30, bell30, areas30, head30 = AX[30], BARS[30], BELL[30], AREAS[30], HEAD[30]
        exact_tag = text("exact", size=SMALL, color=GRAY, slant=ITALIC)     # beside the n label
        exact_tag.move_to(P(-4.0 + exact_tag.width / 2, 2.95))
        xl30 = Text("average (minutes)", font_size=LABEL - 2, color=GRAY)
        xl30.next_to(ax30.x_axis.numbers, DOWN, buff=0.15).align_to(ax30.x_axis.get_right(), RIGHT)

        # one test of 30 waits with a low average: the interval the true spread would give
        # (green, dashed) and the one its own small spread gives (yellow, above), short of mu
        xb, s_ex, h_known, h_est = D["ex30"]
        y_k, y_e = BIG_B + 1.55, BIG_B + 1.87
        x_mu = ax30.c2p(10, 0)[0]
        mu_line = DashedLine(P(x_mu, BIG_B), P(x_mu, BIG_B + BIG_H), color=GRAY, stroke_width=3,
                             dash_length=0.08)
        mu_lbl = MathTex(r"\mu", font_size=36, color=GRAY).next_to(mu_line, UP, buff=0.12)

        def interval(lo, hi, y, color, dashed=False):
            xl_, xr_ = ax30.c2p(lo, 0)[0], ax30.c2p(hi, 0)[0]
            ln = (DashedLine(P(xl_, y), P(xr_, y), color=color, stroke_width=5, dash_length=0.1)
                  if dashed else Line(P(xl_, y), P(xr_, y), color=color, stroke_width=5))
            return VGroup(ln, Line(P(xl_, y - 0.11), P(xl_, y + 0.11), color=color, stroke_width=5),
                          Line(P(xr_, y - 0.11), P(xr_, y + 0.11), color=color, stroke_width=5))
        ex_dot = Dot(P(ax30.c2p(xb, 0)[0], y_k), radius=0.08, color=YELLOW).set_z_index(3)
        ex_dot2 = Dot(P(ax30.c2p(xb, 0)[0], y_e), radius=0.08, color=YELLOW).set_z_index(3)
        iv_known = interval(xb - h_known, xb + h_known, y_k, GREEN, dashed=True)
        iv_est = interval(xb - h_est, xb + h_est, y_e, YELLOW)
        lab_k = Text("true spread", font_size=SMALL - 2, color=GREEN)
        lab_k.next_to(iv_known, DOWN, buff=0.17).align_to(iv_known, LEFT)
        lab_e = Text("own spread", font_size=SMALL - 2, color=YELLOW)
        lab_e.next_to(iv_est, UP, buff=0.17).align_to(iv_est, LEFT)

        # the miss meter: simulated share of 95% intervals that miss low / high, against 2.5%
        miss = {n: D[f"miss{n}"] * 100 for n in NS3}
        trk = [ValueTracker(0.0), ValueTracker(0.0)]
        y25 = BIG_B + 2.5 * M_S
        m_base = Line(P(MX[0] - 0.36, BIG_B), P(MX[1] + 0.36, BIG_B), color=GRAY, stroke_width=2.5)
        m_ref = DashedLine(P(MX[0] - 0.36, y25), P(MX[1] + 0.36, y25), color=GREEN, stroke_width=3,
                           dash_length=0.08)
        ref_lbl = MathTex(r"2.5\%", font_size=30, color=GREEN).next_to(m_ref, RIGHT, buff=0.3)
        m_band = Rectangle(width=MX[1] - MX[0] + 0.72, height=M_S, stroke_width=0, fill_color=GRAY,
                           fill_opacity=0.3).move_to(P((MX[0] + MX[1]) / 2, y25))
        band_lbl = MathTex(r"2\text{--}3\%", font_size=30, color=GRAY).next_to(m_band, RIGHT, buff=0.3)
        m_lr = VGroup(*[Text(w_, font_size=SMALL, color=GRAY).move_to(P(x, BIG_B - 0.82))
                        for w_, x in zip(("low", "high"), MX)])
        m_ttl = Text("misses (simulated)", font_size=SMALL, color=GRAY)
        m_ttl.move_to(P((MX[0] + MX[1]) / 2, 2.38))
        live = VGroup()
        for t, x in zip(trk, MX):
            num = pct(0.0)
            num.move_to(P(x, BIG_B - 0.4))
            num.add_updater(lambda m, t=t, x=x: m.set_value(t.get_value()).move_to(P(x, BIG_B - 0.4)))
            live.add(num)
        mbars = VGroup(*[always_redraw(lambda i=i: meter_bar(i, trk[i].get_value())) for i in range(2)])

        sub = MathTex(r"\text{skew}(\bar{x})", "=", r"\frac{2}{\sqrt{30}}", "=", font_size=MATH)
        sub[0].set_color(YELLOW)
        sub[2][0].set_color(BLUE)
        sub.move_to(P(RX - 0.45, ROW_D))
        ans = MathTex("0.37", font_size=MATH, color=YELLOW).next_to(sub, RIGHT, buff=0.2)
        sub_clean = sub.copy()
        # the average's skewness, which drives the meter: it sits right above it
        RD = {n: MathTex(r"\text{skew}(\bar{x})", "=", v, font_size=MATH).move_to(P(*READ_P))
              for n, v in ((30, "0.37"), (300, "0.12"), (1420, "0.053"))}
        for r in RD.values():
            r[0].set_color(YELLOW)
            r[2].set_color(YELLOW)
            r.align_to(RD[30], LEFT)
        rd = RD[30]

        # log axis: sample size needed
        AX_Y, L0, L1 = -2.0, -5.4, 5.4
        lo_d, hi_d = 1.0, 5.3

        def lx(n):
            return L0 + (np.log10(n) - lo_d) / (hi_d - lo_d) * (L1 - L0)
        line = Line(P(L0, AX_Y), P(L1, AX_Y), color=GRAY, stroke_width=2.5)
        ticks = VGroup(*[Line(P(lx(10 ** e), AX_Y - 0.07), P(lx(10 ** e), AX_Y + 0.07), color=GRAY,
                              stroke_width=2.5) for e in range(1, 6)])
        tl = VGroup(*[MathTex("10" if e == 1 else f"10^{e}", font_size=MATH_SMALL, color=GRAY)
                      .next_to(P(lx(10 ** e), AX_Y), DOWN, buff=0.27) for e in range(1, 6)])
        ttl = Text("sample size", font_size=LABEL - 2, color=GRAY)
        ttl.next_to(tl, DOWN, buff=0.15).align_to(P(L1, 0), RIGHT)
        m30 = marker(lx(30), AX_Y, "30", "textbook")
        m30[0].set_color(GRAY)
        m30[1].set_color(GRAY)
        d300 = Dot(P(lx(300), AX_Y), radius=0.09, color=GRAY)
        m300 = VGroup(d300, MathTex("300", font_size=MATH, color=GRAY).next_to(d300, UP, buff=0.2))
        m1420 = marker(lx(1420), AX_Y, r"1{,}420", "waits")
        mbing = marker(lx(113746), AX_Y, r"114{,}000", "Bing revenue")
        mcap = marker(lx(9599), AX_Y, r"9{,}600", "capped")
        axis_ctx = VGroup(line, ticks, tl, ttl, m30)

        # ---- beat 9: back to the textbook's thirty: the n = 16 panel grows into n = 30
        p16 = self.p16                           # axes, bars, bell, header of the n = 16 panel
        with self.beat("thirty") as beat:
            self.play(FadeOut(self.avg_rest), run_time=0.5)
            keepf = set(map(id, VGroup(*p16, gen).get_family()))
            for m in list(self.mobjects):           # wrappers left by transforms (nothing visible)
                if not any(id(x) in keepf for x in m.get_family()):
                    if any(x.has_points() and x.get_fill_opacity() + x.get_stroke_opacity() > 0.02
                           for x in m.get_family()):
                        print("[ep9] removing VISIBLE leftover", type(m).__name__, m.get_center())
                    self.remove(m)
            self.play(FadeTransform(p16[0], ax30), ReplacementTransform(p16[1], bars30),
                      ReplacementTransform(p16[2], bell30), ReplacementTransform(p16[3][0:2], head30[0:2]),
                      FadeTransform(p16[3][2], head30[2]), gen.animate.move_to(top),
                      *[FadeIn(m) for m in (line, ticks, tl, ttl, cite1, xl30)],
                      FadeIn(m30, shift=0.1 * UP), run_time=beat.until("Two", offset=-0.3, min_time=1.2))
            # the formula's copy becomes 2 / root 30 on its way down (no doubled formula)
            cp = gen.copy()
            self.play(ReplacementTransform(cp[0], sub[0], path_arc=0.6), ReplacementTransform(cp[1], sub[1], path_arc=0.6),
                      FadeTransform(cp[2][0:7], sub[2][0]), ReplacementTransform(cp[2][7:10], sub[2][1:4], path_arc=0.6),
                      FadeOut(cp[2][10]), TransformFromCopy(head30[2], sub[2][4:]), FadeIn(sub[3]),
                      FadeIn(exact_tag), run_time=beat.until("point", offset=-0.1, min_time=1.0))
            self.play(Write(ans), run_time=0.6)
            sub = swap_clean(self, sub, sub_clean)
            beat.wait_until("Close", offset=-0.2)
            self.play(Indicate(bell30, color=GREEN, scale_factor=1.04), run_time=0.9)

        # ---- beat 10: where tests live: a 95% interval should miss 2.5% each side; with the
        # spread estimated from the same data, a low average gets a short interval
        ctx = VGroup(gen, sub, ans, axis_ctx)
        with self.beat("tails") as beat:
            beat.wait_until("tails", offset=-0.45)
            self.play(*[b.animate.set_fill(opacity=0.3) for b in bars30[MID]], FadeIn(areas30),
                      dimmed(ctx, 0.35), run_time=0.6)
            beat.wait_until("ninety", offset=-0.2)
            self.play(Create(m_base), FadeIn(m_lr), FadeIn(m_ttl), run_time=0.6)
            beat.wait_until("two and", offset=-0.2)
            self.play(Create(m_ref), FadeIn(ref_lbl, shift=0.1 * LEFT), run_time=0.6)
            beat.wait_until("each side", offset=-0.25)
            self.play(glow(areas30, 0.5, 0.8), flag(ref_lbl, color=GREEN), run_time=0.8)
            beat.wait_until("Tests", 2, offset=-0.1)
            self.play(Create(mu_line), FadeIn(mu_lbl, shift=0.1 * DOWN), run_time=0.6)
            beat.wait_until("lopsided", offset=-0.15)
            self.play(glow(VGroup(*bars30[15:]), 0.5, 0.8), run_time=0.8)
            beat.wait_until("low average", offset=-0.25)
            self.play(GrowFromCenter(ex_dot), GrowFromCenter(iv_known), FadeIn(lab_k), run_time=0.6)
            beat.wait_until("small", offset=-0.15)
            # the test's own interval: same average, its own (small) spread, drawn just above
            self.play(TransformFromCopy(iv_known, iv_est), TransformFromCopy(ex_dot, ex_dot2),
                      FadeIn(lab_e, shift=0.1 * UP), dimmed(VGroup(iv_known, ex_dot), 0.5), run_time=0.8)
            beat.wait_until("stops", offset=-0.15)
            self.play(Indicate(iv_est[2], color=YELLOW, scale_factor=1.8), Indicate(mu_line, color=INK),
                      run_time=0.8)
            beat.wait_until("seven", offset=-0.45)
            self.add(live[0])
            target = meter_bar(0, miss[30][0])
            self.play(TransformFromCopy(iv_est, target), trk[0].animate.set_value(miss[30][0]), run_time=0.8)
            self.remove(target)
            self.add(mbars[0])
            beat.wait_until("one percent", offset=-0.35)
            self.add(live[1], mbars[1])
            self.play(trk[1].animate.set_value(miss[30][1]), run_time=0.7)

        # ---- beat 11: Kohavi's rule is our formula; at 300 the lean is still too big; 1,420
        S1 = MathTex("n", r"\ge", "355", r"\cdot", r"\text{skew}(x)^2", font_size=MATH)
        S1[4][0:7].set_color(BLUE)
        S1.move_to(P(RX, ROW_R))
        S2 = MathTex(r"\frac{\text{skew}(x)^2}{n}", r"\le", r"\frac{1}{355}", font_size=MATH)
        S2[0][0:7].set_color(BLUE)
        S2.move_to(P(RX, ROW_D))
        S3 = MathTex(r"\frac{\text{skew}(x)}{\sqrt{n}}", r"\le", r"\frac{1}{\sqrt{355}}", r"\approx",
                     "0.053", font_size=MATH)
        S3[0][0:7].set_color(BLUE)
        S3[4].set_color(YELLOW)
        S3.move_to(P(RX, ROW_D))
        # merged with our formula: the left side IS the average's skewness
        S3b = MathTex(r"\text{skew}(\bar{x})", "=", r"\frac{\text{skew}(x)}{\sqrt{n}}", r"\le", "0.053",
                      font_size=MATH)
        S3b[0].set_color(YELLOW)
        S3b[2][0:7].set_color(BLUE)
        S3b[4].set_color(YELLOW)
        S3b.move_to(P(6.3 - S3b.width / 2, ROW_D))
        S4 = MathTex("n", r"\ge", "355", r"\cdot", "2^2", "=", r"1{,}420", font_size=MATH)
        S4[4][0].set_color(BLUE)
        S4.move_to(P(RX, ROW_R))
        state = {"n": 30, "rd2": rd[2]}

        def to_panel(n):
            """Morph the (dimmed) panel, the skew readout and the meter to the average of n waits.
            Changed numbers roll (old out upward, then new in), so no digits are ever doubled."""
            o = state["n"]
            old_rd = state["rd2"]
            state["n"], state["rd2"] = n, RD[n][2]
            return [FadeTransform(AX[o], AX[n]), ReplacementTransform(BARS[o], BARS[n]),
                    ReplacementTransform(BELL[o], BELL[n]), ReplacementTransform(AREAS[o], AREAS[n]),
                    ReplacementTransform(HEAD[o][0:2], HEAD[n][0:2]), *roll(HEAD[o][2], HEAD[n][2]),
                    *roll(old_rd, RD[n][2]),
                    trk[0].animate.set_value(miss[n][0]), trk[1].animate.set_value(miss[n][1])]
        panel30 = VGroup(ax30, bars30, bell30, areas30, head30, exact_tag, xl30)
        with self.beat("kohavi") as beat:
            self.play(FadeTransform(cite1, cite2),
                      FadeOut(VGroup(ex_dot, ex_dot2, iv_known, iv_est, lab_k, lab_e, mu_line, mu_lbl)),
                      run_time=0.6)
            beat.wait_until("each side", offset=-0.2)
            self.play(glow(VGroup(*bars30[0:7], *bars30[21:]), 0.5, 0.8),
                      *[flag(m, color=YELLOW) for m in live], run_time=0.8)
            beat.wait_until("two and three", offset=-0.25)
            self.play(FadeTransform(ref_lbl, band_lbl), FadeIn(m_band), run_time=0.8)
            self.bring_to_front(mbars, m_ref)
            beat.wait_until("Their rule", offset=-0.2)
            # the panel steps back; the lean of an average of 30 becomes the meter's driver
            # 2 / root 30 has done its job and leaves first (the meter's title steps back so the
            # travelling readout never runs over live text); then "skew(x-bar) = 0.37" moves to sit
            # right above the meter, and the title returns
            self.play(dimmed(panel30, PDIM), FadeOut(sub[2:], shift=0.1 * DOWN), dimmed(m_ttl, 0.15),
                      run_time=0.4)
            self.play(ReplacementTransform(sub[0], rd[0]), ReplacementTransform(sub[1], rd[1]),
                      ReplacementTransform(ans, rd[2]), run_time=0.8)
            self.play(dimmed(m_ttl, 1 / 0.15), run_time=0.3)
            self.play(Write(S1), run_time=beat.until("squared", end=True, offset=-0.1, min_time=1.2))
            beat.wait_until("Divide", offset=-0.2)
            s1c = S1.copy()
            self.play(TransformMatchingShapes(s1c, S2), run_time=1.0)
            beat.wait_until("root", offset=-0.15)
            self.play(TransformMatchingShapes(S2, S3[0:3]), FadeIn(S3[3:]), run_time=0.9)
            beat.wait_until("our formula", offset=-0.45)
            # it's our formula: the dimmed formula lights up with the matching side, then comes
            # down into the inequality, which now reads skew(x-bar) = skew(x)/root n <= 0.053
            self.play(dimmed(gen, 1 / 0.35), Indicate(S3[0], color=YELLOW, scale_factor=1.1), run_time=0.5)
            self.play(ReplacementTransform(gen[0], S3b[0]), ReplacementTransform(gen[1], S3b[1]),
                      ReplacementTransform(gen[2], S3b[2]), FadeOut(S3[0], target_position=S3b[2]),
                      ReplacementTransform(S3[1], S3b[3]), FadeOut(S3[2:4]),
                      ReplacementTransform(S3[4], S3b[4]), run_time=1.0)
            beat.wait_until("average's", offset=-0.2)
            self.play(flag(S3b[0], color=YELLOW), run_time=0.7)
            beat.wait_until("point oh", offset=-0.25)
            self.play(flag(S3b[4], color=YELLOW), run_time=0.7)
            beat.wait_until("At three", offset=-0.2)
            self.play(dimmed(axis_ctx, 1 / 0.35), FadeIn(m300[0], scale=0.5), FadeIn(m300[1], shift=0.2 * UP),
                      *to_panel(300), run_time=1.0)
            beat.wait_until("point", 2, offset=-0.2)
            self.play(flag(state["rd2"], color=YELLOW), flag(S3b[4], color=YELLOW), run_time=0.7)
            beat.wait_until("still", offset=-0.2)
            self.play(flag(live[0], color=YELLOW), run_time=0.6)
            beat.wait_until("these waits", offset=-0.2)
            # the general skewness becomes these waits' 2; the result rolls in (no doubled glyphs)
            self.play(ReplacementTransform(S1[0:4], S4[0:4]), *roll(S1[4], S4[4:]), run_time=0.9)
            consolidate(self, S4)
            beat.wait_until("fourteen", offset=-0.2)
            self.play(flag(S4[6], color=INK), FadeIn(m1420[0], scale=0.5),
                      FadeIn(m1420[1], shift=0.25 * UP), FadeIn(m1420[2], shift=0.1 * UP), *to_panel(1420),
                      run_time=1.1)
            beat.wait_until("lean", 2, offset=-0.15)
            self.play(flag(state["rd2"], color=YELLOW), flag(S3b[4], color=YELLOW), run_time=0.7)
            beat.wait_until("band", offset=-0.3)
            for m in (*live, *mbars):
                m.clear_updaters()
            ring = SurroundingRectangle(VGroup(m_band, mbars), buff=0.07, corner_radius=0.08, color=GREEN,
                                        stroke_width=3)
            self.play(Create(ring), glow(mbars, 0.4, 0.7), *[flag(m, color=YELLOW) for m in live], run_time=0.7)
            self.play(FadeOut(ring), run_time=0.4)

        # ---- beat 12: Bing's revenue, and the cap: the sample-size axis becomes the subject
        UP_AX, AX_DX = 1.9, 0.5                 # the axis rises, and moves left to make room for "never"
        S5 = MathTex("n", r"\ge", "355", r"\cdot", r"17.9^2", r"\approx", r"114{,}000", font_size=MATH)
        S5[4][0:4].set_color(BLUE)
        S5.move_to(P(0, 2.45))
        S6 = MathTex("n", r"\ge", "355", r"\cdot", r"5.2^2", r"\approx", r"9{,}600", font_size=MATH)
        S6[4][0:3].set_color(BLUE)
        S6.move_to(P(0, 2.45))
        for m in (mbing, mcap):
            m.shift(UP * UP_AX + LEFT * AX_DX)
        payoff = VGroup(AX[1420], BARS[1420], BELL[1420], AREAS[1420], HEAD[1420], exact_tag, xl30,
                        rd[0], rd[1], state["rd2"],
                        band_lbl, m_base, m_band, m_ref, mbars, live, m_lr, m_ttl, S3b)
        axis_all = VGroup(axis_ctx, m300, m1420)
        with self.beat("bing") as beat:
            self.play(FadeOut(payoff), run_time=0.45)
            self.play(axis_all.animate.shift(UP * UP_AX + LEFT * AX_DX), S4.animate.move_to(P(0, 2.45)),
                      run_time=0.7)
            beat.wait_until("eighteen", offset=-0.4)
            self.play(ReplacementTransform(S4[0:4], S5[0:4]), *roll(S4[4:], S5[4:]), run_time=1.0)
            consolidate(self, S5)
            beat.wait_until("hundred", offset=-0.2)
            self.play(flag(S5[6], color=INK), FadeIn(mbing[0], scale=0.5),
                      FadeIn(mbing[1], shift=0.25 * UP), run_time=0.8)
            self.play(FadeIn(mbing[2], shift=0.1 * UP), run_time=0.4)
            beat.wait_until("Capping", offset=-0.2)
            self.play(ReplacementTransform(S5[0:4], S6[0:4]), *roll(S5[4:], S6[4:]),
                      run_time=beat.until("under", offset=-0.2, min_time=1.0))
            travel = mbing[0].copy()
            self.play(travel.animate(path_arc=0.9).move_to(mcap[0]), run_time=0.8)
            self.remove(travel)
            self.add(mcap[0])
            self.play(FadeIn(mcap[1:], shift=0.1 * UP), flag(S6[6], color=INK), run_time=0.6)

        # ---- the third answer to the cold open: for some data, no sample size is enough
        ay, l0, l1 = AX_Y + UP_AX, L0 - AX_DX, L1 - AX_DX
        sweep = Line(P(l0, ay), P(l1, ay), color=INK, stroke_width=6)
        ext = DashedLine(P(l1 + 0.05, ay), P(l1 + 0.6, ay), color=RED, stroke_width=3, dash_length=0.08)
        nd = Circle(radius=0.09, color=RED, stroke_width=3).move_to(P(l1 + 0.75, ay))
        nlab = Text("never", font_size=LABEL - 2, color=RED).next_to(nd, UP, buff=0.27)
        with self.beat("never") as beat:
            beat.wait_until("no number", offset=-0.25)
            # every number on the axis is swept past; the sweep runs off its end into "never"
            self.play(Create(sweep), dimmed(S6, 0.35), run_time=0.8, rate_func=smooth)
            self.play(FadeOut(sweep), Create(ext), FadeIn(nd, scale=0.5), FadeIn(nlab, shift=0.1 * UP),
                      run_time=0.6)
            beat.wait_until("enough", offset=-0.2)
            self.play(flag(nlab, color=RED), run_time=0.7)
        self.ss_line = line

    # ================================================================== 10 lighthouse
    def part_lighthouse(self):
        x = D["lh_x"]
        rmean, rmed = D["lh_mean"], D["lh_median"]
        avgs = D["lh_avgs"]
        shore = NumberLine(x_range=[-5.6, 5.6, 1], length=11.2, color=GRAY, stroke_width=3,
                           include_ticks=False).move_to(P(0, SHORE_Y))
        sticks = VGroup(*[Line(P(v, SHORE_Y - 0.07), P(v, SHORE_Y + 0.07), color=GRAY, stroke_width=2.5)
                          for v in range(-5, 6)])
        snums = VGroup(*[MathTex(str(v), font_size=MATH_SMALL, color=GRAY).move_to(P(v, SHORE_Y - 0.36))
                         for v in (-4, -2, 0, 2, 4)])
        stitle = Text("miles", font_size=LABEL - 2, color=GRAY)
        stitle.move_to(P(5.6 - stitle.width / 2, SHORE_Y - 0.75))
        lamp = VGroup(Circle(radius=0.16, color=INK, stroke_width=3).move_to(LAMP),
                      Dot(LAMP, radius=0.07, color=INK))
        lamp_lbl = Text("lighthouse", font_size=LABEL - 2, color=INK)
        lamp_lbl.next_to(lamp, RIGHT, buff=0.15).shift(UP * 0.22)
        drop = DashedLine(LAMP + DOWN * 0.18, P(0, SHORE_Y), color=GRAY, stroke_width=2, dash_length=0.07)
        mile = MathTex(r"1\text{ mi}", font_size=MATH_SMALL, color=GRAY).next_to(drop, LEFT, buff=0.15)
        mile.set_y(SHORE_Y + 0.62)
        cite = citation("Lighthouse problem: Gull, 1988 · Sivia & Skilling, 2006, Data Analysis")
        sim_tag = text("simulated", size=SMALL, color=GRAY, slant=ITALIC)
        sim_tag.move_to(P(6.3 - sim_tag.width / 2, 3.35))

        K = ValueTracker(0)
        dots = VGroup(*[Dot(P(v, SHORE_Y), radius=0.055, color=BLUE, fill_opacity=0)
                        if abs(v) < 5.5 else VectorizedPoint(P(0, SHORE_Y)) for v in x])
        shown = [0]

        def upd_dots(m):
            k = int(K.get_value())
            if k > shown[0]:
                for i in range(shown[0], k):
                    if isinstance(m[i], Dot):
                        m[i].set_fill(opacity=0.6)
                shown[0] = k
        dots.add_updater(upd_dots)

        def beam_end(v):
            if abs(v) <= 5.6:
                return P(v, SHORE_Y)
            t = 6.1 / abs(v)                       # where the ray leaves the picture
            return LAMP + t * (P(v, SHORE_Y) - LAMP)
        beam = Line(LAMP, LAMP + DOWN * 0.01, color=BLUE, stroke_width=3)

        def upd_beam(m):
            k = int(K.get_value())
            if k < 1:
                m.set_stroke(opacity=0)
                return
            m.put_start_and_end_on(LAMP, beam_end(x[k - 1]))
            m.set_stroke(opacity=0.85)
        beam.add_updater(upd_beam)
        self.allow_overlap(mile, beam, reason="a light beam sweeping past the lamp crosses the '1 mi' label for a frame")

        def late(t, d=0.3, e=0.95):
            return smooth(min(1.0, max(0.0, (t - d) / (e - d))))

        def early(t, d=0.65):
            return smooth(min(1.0, t / d))
        self.shore = shore
        # out, then in (no double exposure): in the pause, everything but the sample-size axis
        # line leaves; then that line slides down and becomes the shore
        ss_line = self.ss_line
        self.play(*[FadeOut(m) for m in self.mobjects if m is not ss_line], run_time=0.5)
        with self.beat("lighthouse") as beat:
            self.play(ReplacementTransform(ss_line, shore), FadeIn(lamp, scale=0.6), FadeIn(sticks),
                      FadeIn(snums), FadeIn(stitle), FadeIn(lamp_lbl, shift=0.1 * LEFT), FadeIn(cite),
                      run_time=beat.until("mile", offset=-0.25, min_time=0.5))
            self.play(Create(drop), FadeIn(mile), run_time=0.7)
            beat.wait_until("straight", offset=-0.2)
            self.play(Indicate(shore, color=INK, scale_factor=1.0), run_time=0.6)
            beat.wait_until("flashes", offset=-0.1)
            self.add(dots, beam)
            self.play(K.animate.set_value(9), run_time=beat.remaining(min_time=2.0), rate_func=linear)

        # ---- the running average
        frame = VGroup(Line(P(TP_L, TP_B), P(TP_R, TP_B), color=GRAY, stroke_width=2.5),
                       Line(P(TP_L, TP_B), P(TP_L, TP_T), color=GRAY, stroke_width=2.5))
        zero = DashedLine(P(TP_L, TP_MID), P(TP_R, TP_MID), color=DIM, stroke_width=2, dash_length=0.1)
        yt = VGroup(*[MathTex(("+" if v > 0 else "") + str(v) if v else "0", font_size=MATH_SMALL, color=GRAY)
                      .next_to(P(TP_L, TP_MID + TP_S * v), LEFT, buff=0.15) for v in (-2, 0, 2)])
        ytk = VGroup(*[Line(P(TP_L - 0.06, TP_MID + TP_S * v), P(TP_L, TP_MID + TP_S * v), color=GRAY,
                            stroke_width=2.5) for v in (-2, 0, 2)])
        xt = VGroup(MathTex("0", font_size=MATH_SMALL, color=GRAY).next_to(P(TP_L, TP_B), DOWN, buff=0.18),
                    MathTex("500", font_size=MATH_SMALL, color=GRAY).next_to(P(0, TP_B), DOWN, buff=0.18))
        xlast = Text("1,000 flashes", font_size=LABEL - 4, color=GRAY)
        xlast.next_to(P(TP_R, TP_B), DOWN, buff=0.18)
        xlast.shift(LEFT * max(0, xlast.get_right()[0] - 6.3))
        ttl = Text("miles", font_size=LABEL - 2, color=GRAY)
        ttl.move_to(P(TP_L - 0.45 + ttl.width / 2, TP_T + 0.32))
        avg_lbl = Text("average", font_size=LABEL - 2, color=YELLOW)
        avg_lbl.add_background_rectangle(color=BG, opacity=1, buff=0.06)
        trace = VMobject(color=YELLOW, stroke_width=3.5)

        def upd_trace(m):
            k = max(int(K.get_value()), 1)
            pts = [tp(i + 1, rmean[i]) for i in range(k)]
            if len(pts) < 2:
                pts = [pts[0], pts[0] + RIGHT * 0.001]
            m.set_points_as_corners(pts)
        trace.add_updater(upd_trace)
        marker_ = Triangle(color=YELLOW, fill_opacity=1, stroke_width=0).scale(0.11).rotate(PI)

        def upd_marker(m):
            k = max(int(K.get_value()), 1)
            m.move_to(P(float(np.clip(rmean[k - 1], -5.4, 5.4)), SHORE_Y + 0.2))
        marker_.add_updater(upd_marker)

        def upd_avg_lbl(m):
            end = trace.get_end()
            if end[0] + 0.18 + m.width < TP_R:
                m.move_to(P(end[0] + 0.18 + m.width / 2, end[1]))
            else:
                m.move_to(P(TP_R - m.width / 2, end[1] + 0.32))

        j1 = 20                                   # flash 20 lands 32 miles off
        far_lbl = MathTex(r"\leftarrow 32\text{ mi}", font_size=MATH, color=RED)
        far_lbl.move_to(P(-5.6 + far_lbl.width / 2 + 0.1, SHORE_Y + 0.45))
        with self.beat("runmean") as beat:
            self.play(FadeOut(cite), FadeOut(lamp_lbl), Create(frame), FadeIn(zero), FadeIn(yt), FadeIn(ytk),
                      FadeIn(xt), FadeIn(xlast), FadeIn(ttl), FadeIn(sim_tag), run_time=1.0)
            self.add(trace, marker_)
            avg_lbl.add_updater(upd_avg_lbl)
            self.add(avg_lbl)
            self.play(K.animate.set_value(j1 - 1), run_time=beat.until("aimed", offset=-0.5, min_time=1.0),
                      rate_func=linear)
            self.play(K.animate.set_value(j1), run_time=0.3, rate_func=linear)
            beam.set_color(RED)
            beat.wait_until("absurdly", offset=-0.2)
            self.play(FadeIn(far_lbl, shift=0.2 * LEFT), run_time=0.6)
            beat.wait_until("yanks", offset=-0.25)
            self.play(Indicate(marker_, color=YELLOW, scale_factor=1.6), run_time=0.8)
            beam.set_color(BLUE)
            self.play(FadeOut(far_lbl), K.animate.set_value(250), run_time=beat.remaining(min_time=0.6),
                      rate_func=linear)

        # ---- the farthest of a thousand, then 200 repeats of the whole average
        jf = int(np.abs(x).argmax())             # flash 841: +902 miles
        red_lbl = MathTex(r"902\text{ mi} \rightarrow", font_size=MATH, color=RED)
        red_lbl.move_to(P(5.95 - red_lbl.width / 2, SHORE_Y + 0.55))
        without = (rmean[-1] * 1000 - x[jf]) / 999          # final average without flash 841
        y_a, y_b = tp(1000, without)[1], tp(1000, rmean[-1])[1]
        jx = TP_R + 0.14
        jump = VGroup(Line(P(jx, y_a), P(jx, y_b), color=RED, stroke_width=4),
                      Line(P(jx - 0.08, y_a), P(jx + 0.08, y_a), color=RED, stroke_width=4),
                      Line(P(jx - 0.08, y_b), P(jx + 0.08, y_b), color=RED, stroke_width=4))
        ghost = Circle(radius=0.07, color=RED, stroke_width=3).move_to(tp(1000, without))
        jdot = Dot(tp(jf + 1, rmean[jf]), radius=0.07, color=RED)
        div = MathTex(r"902 \div 1{,}000 \approx 0.9\text{ mi}", font_size=MATH, color=RED)
        div.move_to(P(1.7, TP_T - 0.28))
        # middle half of this run's single flashes, from its quartile dots
        order = np.argsort(x)
        iq1, iq3 = int(order[249]), int(order[750])
        bq1, bq3 = float(x[iq1]), float(x[iq3])
        b1 = bracket(bq1, bq3, SHORE_Y - 0.78, BLUE)
        b1l = Text("one flash", font_size=LABEL - 2, color=BLUE).next_to(b1, RIGHT, buff=0.25)
        half = Text("middle half", font_size=LABEL - 2, color=GRAY).next_to(b1, LEFT, buff=0.3)
        # 200 averages of 1,000 flashes on a second line
        strip = Line(P(-5.5, STRIP_Y), P(5.5, STRIP_Y), color=GRAY, stroke_width=2)
        jit = np.random.default_rng(11).uniform(-0.1, 0.1, len(avgs))
        inside = np.abs(avgs) < 5.5
        adots = VGroup(*[Dot(P(a, STRIP_Y + j), radius=0.05, color=YELLOW, fill_opacity=0.8)
                         for a, j, ok in zip(avgs, jit, inside) if ok])
        n_left, n_right = int(np.sum(avgs < -5.5)), int(np.sum(avgs > 5.5))
        # averages beyond the picture, counted (under the ends of the strip, inside |x| <= 6)
        cnt_l = MathTex(r"\leftarrow %d\text{ more}" % n_left, font_size=MATH_SMALL, color=YELLOW)
        cnt_l.move_to(P(-5.5 + cnt_l.width / 2, STRIP_Y - 0.48))
        cnt_r = MathTex(r"%d\text{ more} \rightarrow" % n_right, font_size=MATH_SMALL, color=YELLOW)
        cnt_r.move_to(P(5.5 - cnt_r.width / 2, STRIP_Y - 0.48))
        srt = np.sort(avgs)
        aq1, aq3 = float(srt[49]), float(srt[150])
        vis = [a for a, ok in zip(avgs, inside) if ok]
        ia1 = int(np.argmin([abs(a - aq1) for a in vis]))
        ia3 = int(np.argmin([abs(a - aq3) for a in vis]))
        b2 = bracket(aq1, aq3, STRIP_Y - 0.5, YELLOW)
        b2l = Text("average of 1,000", font_size=LABEL - 2, color=YELLOW).next_to(b2, RIGHT, buff=0.25)
        with self.beat("dilute") as beat:
            self.play(K.animate.set_value(1000), run_time=beat.until("farthest", offset=-0.3, min_time=1.4),
                      rate_func=lambda t: t ** 1.3)
            beam.clear_updaters()
            self.play(beam.animate.put_start_and_end_on(LAMP, beam_end(x[jf])).set_stroke(RED, opacity=1),
                      FadeIn(red_lbl, shift=0.2 * RIGHT), FadeIn(jdot), run_time=0.9)
            beat.wait_until("Divided", offset=-0.2)
            self.play(Write(div), run_time=1.0)
            beat.wait_until("drags", offset=-0.1)
            self.play(FadeIn(ghost), Create(jump), run_time=0.8)
            beat.wait_until("Half", offset=-0.2)
            # the far flash has made its point: clear it so the spread comparison is the focus
            qd = VGroup(dots[iq1], dots[iq3])
            self.play(FadeOut(beam), FadeOut(red_lbl), FadeOut(ghost), FadeOut(jump), FadeOut(div),
                      *[d.animate.set_fill(opacity=1).scale(2.0) for d in qd], run_time=0.6)
            self.play(TransformFromCopy(qd, b1), FadeIn(half), FadeIn(b1l),
                      run_time=beat.until("Repeat", offset=-0.2, min_time=0.9))
            self.play(Create(strip), run_time=0.4)
            self.play(LaggedStart(*[FadeIn(d, shift=0.25 * DOWN) for d in adots], lag_ratio=0.012),
                      FadeIn(cnt_l), FadeIn(cnt_r),
                      run_time=beat.until("still", 2, offset=-0.2, min_time=1.6))
            aqd = VGroup(adots[ia1], adots[ia3])
            self.play(*[d.animate.set_fill(opacity=1).scale(2.0) for d in aqd], run_time=0.5)
            self.play(TransformFromCopy(aqd, b2), FadeIn(b2l), run_time=0.8)
            self.play(emph(VGroup(b1, b2), 1.06), run_time=0.8)

        # ---- the condition, and the median
        var_ok = MathTex(r"\text{variance} < \infty", font_size=MATH + 4, color=INK)
        var_ok.move_to(P(-3.6, SHORE_Y + 0.62))
        var_bad = MathTex(r"\text{variance} = \infty", font_size=MATH + 4, color=RED).move_to(var_ok)
        Km = ValueTracker(1)
        mtrace = VMobject(color=PURPLE, stroke_width=4)

        def upd_mtrace(m):
            kk = max(int(Km.get_value()), 2)
            m.set_points_as_corners([tp(i + 1, rmed[i]) for i in range(kk)])
        mtrace.add_updater(upd_mtrace)
        mmark = Triangle(color=PURPLE, fill_opacity=1, stroke_width=0).scale(0.11).rotate(PI)
        mmark.add_updater(lambda m: m.move_to(P(float(rmed[max(int(Km.get_value()), 1) - 1]),
                                                SHORE_Y + 0.2)))
        med_lbl = Text("median", font_size=LABEL - 2, color=PURPLE)
        context = VGroup(b1, b2, b1l, b2l, half, strip, adots, cnt_l, cnt_r, dots[iq1], dots[iq3])
        chart = VGroup(frame, zero, yt, ytk, xt, xlast, ttl)
        with self.beat("variance") as beat:
            for m in (dots, trace, marker_):
                m.clear_updaters()
            avg_lbl.clear_updaters()
            beat.wait_until("finite", offset=-0.2)
            # one focus: the condition (and the flash that broke it); the running chart steps back
            self.play(Write(var_ok), dimmed(chart, 0.3), trace.animate.set_stroke(opacity=0.3),
                      avg_lbl.animate.set_opacity(0.3), FadeOut(mile), run_time=1.0)
            beat.wait_until("single piece", offset=-0.2)
            self.play(Indicate(jdot, color=RED, scale_factor=2.2), run_time=0.9)
            beat.wait_until("infinite", offset=-0.4)
            self.play(TransformMatchingTex(var_ok, var_bad), dimmed(context, 0.3), run_time=0.6)
            beat.wait_until("median", offset=-0.2)
            # the chart comes back for the median; the average stays in the background
            self.play(dimmed(chart, 1 / 0.3), marker_.animate.set_opacity(0.4),
                      jdot.animate.set_opacity(0.4), run_time=0.5)
            self.add(mtrace, mmark)
            self.play(Km.animate.set_value(1000), run_time=beat.until("homes", offset=-0.1, min_time=2.0),
                      rate_func=linear)
            end = mtrace.get_end()
            med_lbl.move_to(P(TP_R - 0.05 - med_lbl.width / 2, end[1] - 0.32))
            self.play(FadeIn(med_lbl, shift=0.1 * UP), Indicate(mmark, color=PURPLE, scale_factor=1.6),
                      run_time=0.9)
        for m in (mtrace, mmark):
            m.clear_updaters()

    # ================================================================== 11 landing
    def part_landing(self):
        edges, shares = D["src_edges"], D["src_shares"] * 100
        ax = self.src_axes()
        bars = hist_bars(ax, edges, shares[3])
        curve = ax.plot(lambda x: 100 * 0.25065 * np.exp(-x / 10), x_range=[0, 50, 0.25],
                        color=INK, stroke_width=4)
        count = Text("100,000 waits", font_size=LABEL, color=INK)
        count.move_to(P(ax.c2p(50, 0)[0] - count.width / 2, 2.5))
        sim_tag = text("simulated", size=SMALL, color=GRAY, slant=ITALIC)
        sim_tag.next_to(count, DOWN, buff=0.15).align_to(count, RIGHT)
        arrow, more, dashed, base, qmark, chips, tails, t_lbls = self.prediction()
        head = VGroup(*bars[:8])
        tail_brace = Brace(Line(ax.c2p(20, 7), ax.c2p(45, 7)), direction=UP, color=GRAY)
        tail_lbl = Text("tail", font_size=LABEL, color=GRAY).next_to(tail_brace, UP, buff=0.2)
        # where the guessed bell stood: 10,000 averages of 1,420 waits, under their real bell
        lo, hi = 9.0, 11.0
        rax = axes((lo, hi), (0, 14.0), x_length=2.7, y_length=3.0, x_ticks=[9.5, 10.5],
                   y_ticks=[], x_label="minutes", x_decimals=1)
        place(rax, (BELL_C - 1.3, -2.0), x0=lo)
        rax.y_axis.set_opacity(0)
        rbars = hist_bars(rax, D["avg1420_edges"], D["avg1420_shares"] * 100, color=YELLOW)
        rbell = normal_curve(rax, 10, 10 / np.sqrt(1420), (hi - lo) / 24, lo, hi)
        avg_more = Text("average of 1,420", font_size=LABEL - 2, color=YELLOW).move_to(more)
        right_chip = chips[2]
        # out, then in: the lighthouse fades first, the cold-open frame second (no double
        # exposure), while the shore line itself slides into the waits axis
        shore = self.shore
        xline = Line(ax.c2p(0, 0), ax.c2p(50, 0), color=GRAY, stroke_width=2.5)

        def early(t, d=0.65):
            return smooth(min(1.0, t / d))

        def late(t, d=0.3, e=0.95):
            return smooth(min(1.0, max(0.0, (t - d) / (e - d))))
        # in the pause before the last beat: the lighthouse leaves first (all but the shore), then
        # the shore slides into the waits axis as the cold-open frame returns (no double exposure)
        self.play(*[FadeOut(m) for m in self.mobjects if m is not shore], run_time=0.5)
        self.play(ReplacementTransform(shore, xline),
                  *[FadeIn(m, rate_func=late) for m in (ax, count, sim_tag, bars, curve, arrow, more,
                                                        base, dashed, qmark, chips, tails, t_lbls)],
                  run_time=0.8)
        self.remove(xline)
        with self.beat("landing") as beat:
            beat.wait_until("thousand", offset=-0.2)
            self.play(chips[0].animate.set_opacity(0.3), chips[1].animate.set_opacity(0.3),
                      right_chip[0].animate.set_stroke(INK, width=4), emph(right_chip[1], 1.15), run_time=0.8)
            beat.wait_until("not thirty", offset=-0.2)
            self.play(FadeTransform(more, avg_more), run_time=0.8)
            beat.wait_until("lopsided", offset=-0.35)
            self.play(head.animate.set_fill(opacity=0.4), GrowFromCenter(tail_brace),
                      FadeIn(tail_lbl, shift=0.1 * DOWN), run_time=0.7)
            beat.wait_until("never", offset=-0.25)
            self.play(FadeOut(qmark), dashed.animate.set_stroke(opacity=0.3), FadeOut(chips),
                      FadeOut(tails), FadeOut(t_lbls),
                      head.animate.set_fill(opacity=BAR_OPACITY), FadeOut(tail_brace), FadeOut(tail_lbl),
                      run_time=0.7)
            beat.wait_until("It's", offset=-0.2)
            self.play(FadeOut(base), FadeOut(dashed), FadeIn(rax),
                      LaggedStart(*[GrowFromEdge(b, DOWN) for b in rbars], lag_ratio=0.03),
                      Create(rbell), run_time=1.0)
        # the answer stays on screen (trailing silence < 2 s)
        self.hold(1.45)
