"""Episode 6 — Seven Shuffles: When a Deck Suddenly Becomes Random.

    videos/toolkit/render.sh --preview videos/episodes/006-riffle-shuffle-cutoff/scene.py Episode /tmp/ep6.mp4
    videos/toolkit/render.sh videos/episodes/006-riffle-shuffle-cutoff/scene.py Episode \
        videos/episodes/006-riffle-shuffle-cutoff/final.mp4

Numbers: sim.py -> data.json (exact), deck_pick.py -> decks.json (seeded example decks).
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from manim import *
from sample_space import *

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "data.json").read_text())
DECKS = json.loads((HERE / "decks.json").read_text())
N = 52
TGRAY = ManimColor("#A3AAB4")          # grey for TEXT (7.7:1 on BG); GRAY stays for axes/lines

# --------------------------------------------------------------------------- exact maths
# Bayer & Diaconis (1992) Thm 1: after an a-shuffle (a = 2^k for k riffles) a permutation with
# r rising sequences has chance C(a+n-r, n)/a^n.  The formula is a polynomial in a, so it also
# gives a smooth path between whole numbers of riffles (used ONLY to animate the slide; every
# number written on screen is evaluated at a whole number of riffles).


def _eulerian(n: int) -> list[int]:
    A = [1]
    for m in range(2, n + 1):
        B = [0] * m
        for d in range(m):
            B[d] = (d + 1) * (A[d] if d < len(A) else 0) + (m - d) * (A[d - 1] if d >= 1 else 0)
        A = B
    return A


_LOGE = np.array([math.log(x) for x in _eulerian(N)])
RS = np.arange(1, N + 1)
U_PMF = np.exp(_LOGE - math.lgamma(N + 1))
_J = np.arange(N)


def rs_pmf(k: float) -> np.ndarray:
    a = 2.0 ** k
    terms = a + N - RS[:, None] - _J[None, :]
    sign = np.prod(np.sign(terms), axis=1)
    logc = np.sum(np.log(np.abs(terms) + 1e-300), axis=1) - math.lgamma(N + 1) - N * math.log(a)
    p = np.clip(sign * np.exp(logc + _LOGE), 0, None)
    return p / p.sum()


def tv_of(k: float) -> float:
    return 0.5 * float(np.abs(rs_pmf(k) - U_PMF).sum())


def mean_of(k: float) -> float:
    return float(rs_pmf(k) @ RS)


MEAN_U = 26.5
SD_U = DATA["uniform"]["sd"]                         # 2.1016
TV = [r["tv"] for r in DATA["shuffled"]]             # k = 1..12
TOP_TV = [r["tv"] for r in DATA["top_card"]]         # top-card-only distance, k = 1..12
TOP4 = DATA["top_card"][3]["pmf"]                    # chance each card ends on top, 4 riffles
GAP_TXT = {4: "12.4", 5: "6.89", 6: "3.55", 7: "1.79"}
RATIO_TXT = {4: "5.9", 7: "0.85"}                     # gap / spread: 12.401/2.1016, 1.790/2.1016
PROD_TXT = ["198", "220", "227", "229"]               # 12.4*16, 6.89*32, 3.55*64, 1.79*128

# --------------------------------------------------------------------------- deck
CARD_LO = ManimColor("#566275")
PITCH, BAR_W, H0, H1 = 0.2, 0.13, 0.1, 0.052
LH0 = 0.06                                            # level view: base height of a bar
WASH = 0.5                                            # packet tint (toward yellow) on riffle 2

COLD_L = dict(cx=-3.1, by=-0.5, s=0.5, hs=0.8)        # cold open: the riffled deck (left) ...
COLD_R = dict(cx=3.1, by=-0.5, s=0.5, hs=0.8)         # ... and the perfectly shuffled deck
SIDE_A = dict(cx=-3.1, by=-0.5, s=0.5, hs=1.0, step=0.09)   # the same two places, level view
SIDE_B = dict(cx=3.1, by=-0.5, s=0.5, hs=1.0, step=0.09)
STEPS = {1: 0.55, 2: 0.5, 3: 0.32, 4: 0.2}             # level unit shrinks as levels double


def card_color(c: int):
    return interpolate_color(CARD_LO, ManimColor(INK), (c - 1) / (N - 1))


def level_map(runs):
    return {c: j + 1 for j, run in enumerate(runs) for c in run}


class Deck:
    """52 bars, left = top of the deck; shade = card number.
    Card view: bar height = card number.  Level view: bar height = the index of the card's
    rising sequence (so every rising sequence is one horizontal level, and the deck's height
    is its number of rising sequences)."""

    def __init__(self, order, cx=0.0, by=0.0, s=1.0, hs=None, step=0.17, runs=None, levels=False):
        self.order, self.cx, self.by, self.s = list(order), cx, by, s
        self.hs = s if hs is None else hs
        self.step = step
        self.runs = runs
        self.wash: dict[int, float] = {}
        self.levels = level_map(runs) if (levels and runs) else None
        self.cards = {c: self._bar(c, i) for i, c in enumerate(self.order)}
        self.group = VGroup(*[self.cards[c] for c in range(1, N + 1)])

    def color(self, c):
        w = self.wash.get(c, 0.0)
        return interpolate_color(card_color(c), ManimColor(YELLOW), w) if w else card_color(c)

    def height(self, c):
        if self.levels is None:
            return (H0 + H1 * c) * self.hs
        return (LH0 + self.step * self.levels[c]) * self.hs

    def level_y(self, lv):
        return self.by + (LH0 + self.step * lv) * self.hs

    def _bar(self, c, i):
        r = Rectangle(width=BAR_W * self.s, height=self.height(c), stroke_width=0,
                      fill_color=self.color(c), fill_opacity=1)
        return r.move_to([self.slot_x(i), self.by, 0], aligned_edge=DOWN)

    def _set(self, order=None, cx=None, by=None, s=None, hs=None, step=None, runs=None,
             levels=None):
        if order is not None:
            self.order = list(order)
        self.cx = self.cx if cx is None else cx
        self.by = self.by if by is None else by
        if s is not None:
            self.s = s
            self.hs = s if hs is None else hs
        elif hs is not None:
            self.hs = hs
        if step is not None:
            self.step = step
        if runs is not None:
            self.runs = runs
        if levels is True:
            self.levels = level_map(self.runs)
        elif levels is False:
            self.levels = None

    def slot_x(self, i):
        return self.cx + (i - (N - 1) / 2) * PITCH * self.s

    def target(self, c, i):
        return self._bar(c, i)

    def relayout(self, **kw):
        """Animations moving every card to its slot (optionally new order / place / size /
        view).  kw: order, cx, by, s, hs, step, runs, levels (True/False), plus anim kwargs."""
        keys = ("order", "cx", "by", "s", "hs", "step", "runs", "levels")
        self._set(**{k: kw.pop(k) for k in keys if k in kw})
        return [Transform(self.cards[c], self.target(c, i), **kw) for i, c in enumerate(self.order)]

    def left(self):
        return self.slot_x(0) - BAR_W * self.s / 2

    def right(self):
        return self.slot_x(N - 1) + BAR_W * self.s / 2

    def top_y(self):
        if self.levels is None:
            return self.by + (H0 + H1 * N) * self.hs
        return self.level_y(max(self.levels.values()))

    def card_at(self, i):
        return self.cards[self.order[i]]


def deck_marks(deck: Deck) -> VGroup:
    """Yellow rising-sequence marks read off the bars' CURRENT tops (use with always_redraw).
    Card view: a polyline joining each sequence's bar tops.  Level view: one cap per bar plus a
    faint shelf line (behind the bars) joining the caps of each level."""
    g = VGroup()
    if deck.runs is None:
        return g
    cap = (BAR_W + 0.07) * deck.s
    for run in deck.runs:
        tops = [deck.cards[c].get_top() for c in run]
        if len(tops) >= 2:
            if deck.levels is None:
                g.add(VMobject(stroke_color=YELLOW, stroke_width=2.4).set_points_as_corners(tops))
            else:
                g.add(Line(tops[0], tops[-1], stroke_color=YELLOW, stroke_width=1.6,
                           stroke_opacity=0.55).set_z_index(-1))
        for p in tops:
            g.add(Line(p + LEFT * cap / 2, p + RIGHT * cap / 2, color=YELLOW,
                       stroke_width=4.5).set_z_index(2))
    return g


# --------------------------------------------------------------------------- meter
class Meter:
    """'How often you'd be right': 50 % (coin flip) to 100 % (always right).
    The red fill is the edge over a coin flip = half the distance d.  The grey 'top card'
    ghost sits UNDER the track; the live needle and its value sit above it."""

    X0, X1, Y = -1.2, 4.0, -2.05

    def __init__(self):
        self.acc = ValueTracker(0.5)
        x0, x1, y = self.X0, self.X1, self.Y
        xm = (x0 + x1) / 2
        self.track = Line([x0, y, 0], [x1, y, 0], color=DIM, stroke_width=7)
        self.ticks = VGroup(*[Line([x, y - 0.1, 0], [x, y + 0.1, 0], color=GRAY, stroke_width=2.5)
                              for x in (x0, xm, x1)])
        l50 = MathTex(r"50\%", font_size=MATH_SMALL, color=TGRAY)
        l50.move_to([x0, y - 0.45, 0]).align_to([x0, 0, 0], RIGHT)
        l75 = MathTex(r"75\%", font_size=MATH_SMALL, color=TGRAY).move_to([xm, y - 0.45, 0])
        l100 = MathTex(r"100\%", font_size=MATH_SMALL, color=TGRAY).move_to([x1, y - 0.45, 0])
        self.tick_labels = VGroup(l50, l75, l100)
        self.left_lbl = text("coin flip", size=LABEL - 2, color=TGRAY).next_to(self.track, LEFT, buff=0.35)
        self.right_lbl = text("always right", size=LABEL - 2, color=TGRAY).next_to(self.track, RIGHT, buff=0.3)
        self.base = VGroup(self.track, self.ticks, self.tick_labels, self.left_lbl, self.right_lbl)
        self.make_live()

    def make_live(self):
        self.fill = always_redraw(self._fill)
        self.needle = always_redraw(self._needle)
        self.new_value()

    def new_value(self):
        self.value = DecimalNumber(100 * self.acc.get_value(), num_decimal_places=1, unit=r"\%",
                                   font_size=MATH, color=INK)
        self.value.add_updater(lambda m: m.set_value(100 * self.acc.get_value()))
        self.value.add_updater(lambda m: m.next_to(self.needle, UP, buff=0.18))

    def freeze(self):
        for m in (self.fill, self.needle, self.value):
            m.clear_updaters()

    def x_of(self, a):
        return self.X0 + (a - 0.5) / 0.5 * (self.X1 - self.X0)

    def _fill(self):
        x = max(self.x_of(self.acc.get_value()), self.X0 + 0.002)
        return Line([self.X0, self.Y, 0], [x, self.Y, 0], color=RED, stroke_width=11)

    def _needle(self):
        x = self.x_of(self.acc.get_value())
        return Triangle(color=INK, fill_color=INK, fill_opacity=1, stroke_width=0) \
            .scale(0.09).rotate(PI).move_to([x, self.Y + 0.2, 0])

    def ghost(self, acc):
        """Grey 'top card' marker under the track, with its label on the row below the ticks."""
        x = self.x_of(acc)
        tri = Triangle(color=GRAY, fill_color=GRAY, fill_opacity=1, stroke_width=0) \
            .scale(0.09).move_to([x, self.Y - 0.2, 0])
        lbl = VGroup(text("top card", size=SMALL, color=TGRAY),
                     MathTex(rf"{100 * acc:.1f}\%", font_size=MATH_SMALL - 4, color=TGRAY))
        lbl.arrange(RIGHT, buff=0.12)
        lbl.move_to([x, self.Y - 0.95, 0]).align_to([x - 0.1, 0, 0], LEFT)
        return tri, lbl


# --------------------------------------------------------------------------- charts
def step_line(ax, p, lo, hi, color, width):
    pts = [ax.c2p(lo - 0.5, 0)]
    for r in range(lo, hi + 1):
        v = float(p[r - 1])
        pts += [ax.c2p(r - 0.5, v), ax.c2p(r + 0.5, v)]
    pts.append(ax.c2p(hi + 0.5, 0))
    return VMobject(stroke_color=color, stroke_width=width).set_points_as_corners(pts)


def step_area(ax, p, lo, hi, color, opacity):
    pts = [ax.c2p(lo - 0.5, 0)]
    for r in range(lo, hi + 1):
        v = float(p[r - 1])
        pts += [ax.c2p(r - 0.5, v), ax.c2p(r + 0.5, v)]
    pts.append(ax.c2p(hi + 0.5, 0))
    return Polygon(*pts, stroke_width=0, fill_color=color, fill_opacity=opacity)


def support(p, eps=0.003, lo=8, hi=36):
    idx = [r for r in range(lo, hi + 1) if p[r - 1] > eps]
    return (min(idx), max(idx)) if idx else (lo, lo)


def bar_rect(ax, x, y0, y1, w, **kw):
    a, b = ax.c2p(x - w / 2, y0), ax.c2p(x + w / 2, y1)
    return Rectangle(width=max(b[0] - a[0], 1e-3), height=max(b[1] - a[1], 1e-4), **kw) \
        .move_to((a + b) / 2)


def bracket(a, b, color, tick=0.12, width=3.5):
    """Horizontal measuring bracket between points a and b (same y)."""
    return VGroup(Line(a, b, color=color, stroke_width=width),
                  Line(a + UP * tick, a + DOWN * tick, color=color, stroke_width=width),
                  Line(b + UP * tick, b + DOWN * tick, color=color, stroke_width=width))


def regray(ax):
    """Axis numbers and titles in the text grey (7:1); axis lines keep GRAY."""
    for axis in (ax.x_axis, ax.y_axis):
        if getattr(axis, "numbers", None) is not None:
            axis.numbers.set_color(TGRAY)
    for t in (ax.x_title, ax.y_title):
        if t is not None:
            t.set_color(TGRAY)
    return ax


def riffles_tex(k, size=MATH_SMALL + 4):
    return MathTex(str(k), r"\text{ riffles}", font_size=size, color=PURPLE)


def fraction(num_tex, den_tex, size=MATH + 2):
    num = MathTex(num_tex, font_size=size, color=YELLOW)
    den = MathTex(den_tex, font_size=size, color=BLUE)
    w = max(num.width, den.width) + 0.12
    bar = Line(LEFT * w / 2, RIGHT * w / 2, stroke_width=2.5, color=INK)
    return VGroup(num, bar, den).arrange(DOWN, buff=0.1)


class Episode(NarratedScene):
    EPISODE = 6
    TITLE = "Seven Shuffles"
    PRONUNCIATIONS = {"Diaconis": "/dˌIəkˈOnɪs/", "Trefethen": "/tɹəfˈɛθən/", "Aldous": "/ˈɔldʌs/"}
    SPEED = 0.84

    # ------------------------------------------------------------------ helpers
    def riffle(self, deck: Deck, k: int, t_cut=0.4, t_drop=0.65, lift=0.3, extra=(), extra_drop=()):
        """Riffle number k (decks.json): cut and lift the top packet, then the cards drop
        bottom-first (right to left) into their interleaved slots.  Bars also take their
        current colour (deck.wash) during the cut."""
        old, new, c = DECKS["decks"][k - 1], DECKS["decks"][k], DECKS["cuts"][k - 1]
        s = deck.s
        anims = [deck.cards[x].animate.shift(UP * lift * s + LEFT * 0.12 * s).set_fill(deck.color(x))
                 for x in old[:c]]
        anims += [deck.cards[x].animate.shift(RIGHT * 0.12 * s).set_fill(deck.color(x))
                  for x in old[c:]]
        self.play(*anims, *extra, run_time=t_cut, rate_func=SMOOTH)
        deck.order = list(new)
        drops = [Transform(deck.cards[new[i]], deck.target(new[i], i)) for i in reversed(range(N))]
        self.play(LaggedStart(*drops, lag_ratio=0.025), *extra_drop, run_time=t_drop)

    def split(self, deck: Deck, k: int, step: float, run_time=0.6, extra=()):
        """After riffle k: re-read the rising sequences; every bar moves to its new level
        (and the level unit rescales smoothly)."""
        self.play(*deck.relayout(runs=DECKS["runs"][k], levels=True, step=step), *extra,
                  run_time=run_time, rate_func=SMOOTH)

    # ------------------------------------------------------------------ scene
    def construct(self):
        meter = Meter()
        acc_top = 0.5 + DATA["top_card"][3]["tv"] / 2
        ghost, ghost_lbl = meter.ghost(acc_top)

        # ============================================================ 1. cold open: two decks
        deck = Deck(range(1, N + 1), **COLD_L)
        perfect0 = Deck(range(1, N + 1), **COLD_R)
        top_lbl = text("top", size=LABEL - 2, color=TGRAY).next_to(
            [deck.left(), deck.by, 0], DOWN, buff=0.18).align_to([deck.left(), 0, 0], LEFT)
        bot_lbl = text("bottom", size=LABEL - 2, color=TGRAY).next_to(
            [deck.right(), deck.by, 0], DOWN, buff=0.18).align_to([deck.right(), 0, 0], RIGHT)
        one = MathTex("1", font_size=MATH_SMALL, color=TGRAY).next_to(deck.cards[1], UP, buff=0.2)
        fifty2 = MathTex("52", font_size=MATH_SMALL, color=TGRAY).next_to(deck.cards[52], UP, buff=0.2)
        heads = text("heads: 4 riffles", size=LABEL, color=PURPLE).move_to([COLD_L["cx"], 2.45, 0])
        tails = text("tails: perfect shuffle", size=LABEL, color=BLUE).move_to([COLD_R["cx"], 2.45, 0])
        guess = MathTex("?", font_size=60, color=INK)
        self.add(deck.group, perfect0.group, top_lbl, bot_lbl, one, fifty2)
        with self.narrate("Heads, I riffle shuffle a sorted deck four times. Tails, a computer "
                          "shuffles it perfectly. From the deck alone, how often could you tell "
                          "which? Pick fifty, seventy five, or a hundred percent. [pause 1.5]") as beat:
            self.play(FadeIn(heads, shift=0.15 * DOWN), run_time=0.6)
            beat.wait_until("sorted", offset=-0.15)
            self.play(FadeOut(one), FadeOut(fifty2), run_time=0.3)
            t_tails = beat.time_of("Tails") - 0.15
            shown = False
            for k in range(1, 5):
                extra = ()
                if not shown and beat.elapsed() + 0.35 >= t_tails:
                    extra, shown = (FadeIn(tails, shift=0.15 * DOWN),), True
                self.riffle(deck, k, t_cut=0.35, t_drop=0.55, extra=extra)
            if not shown:
                beat.wait_until("Tails", offset=-0.15)
                self.play(FadeIn(tails, shift=0.15 * DOWN), run_time=0.5)
            # the computer's perfect shuffle: every card jumps to a uniformly random slot
            perf_moves = perfect0.relayout(order=DECKS["random"])
            self.play(LaggedStart(*perf_moves, lag_ratio=0.012),
                      run_time=max(0.8, beat.until("From", offset=-0.1)), rate_func=SMOOTH)
            self.play(FadeOut(top_lbl), FadeOut(bot_lbl), run_time=0.5)
            beat.wait_until("how often", offset=-0.3)
            guess.move_to([meter.x_of(0.75), meter.Y + 0.55, 0])
            self.play(Create(meter.base), run_time=1.0)
            self.play(FadeIn(guess, shift=0.2 * DOWN), run_time=0.5)
            for a, w, lab in ((0.5, "fifty", 0), (0.75, "seventy", 1), (1.0, "hundred", 2)):
                beat.wait_until(w, offset=-0.25)
                self.play(guess.animate.move_to([meter.x_of(a), meter.Y + 0.55, 0]),
                          Indicate(meter.tick_labels[lab], color=INK, scale_factor=1.25),
                          run_time=0.45)

        # ============================================================ 2. stakes
        sorted_ghost = DashedLine([deck.left(), deck.by + (H0 + H1) * deck.hs, 0],
                                  [deck.right(), deck.top_y(), 0], color=TGRAY,
                                  stroke_width=3, dash_length=0.12)
        with self.narrate("Any simulation that mixes by random steps faces this question: stopped "
                          "too early, it still remembers where it started.") as beat:
            beat.wait_until("mixes", offset=-0.2)
            self.play(Indicate(heads, color=PURPLE, scale_factor=1.08), run_time=0.9)
            beat.wait_until("stopped", offset=-0.2)
            self.play(Indicate(deck.group, color=INK, scale_factor=1.03), run_time=0.9)
            beat.wait_until("remembers", offset=-0.3)
            self.play(Create(sorted_ghost), run_time=1.3, rate_func=LINEAR)

        # ============================================================ 3. naive: the top card
        th = dict(cx=3.95, by=2.1, s=0.42)
        ax1 = axes((0, 53), (0, 7.5), x_length=8.6, y_length=3.0, x_ticks=[1, 13, 26, 39, 52],
                   y_ticks=[0, 2, 4, 6], x_label="card number", y_label="chance on top (%)")
        regray(ax1)
        ax1.shift(np.array([-5.6, -0.75, 0]) - ax1.c2p(0, 0))
        q = 100 / N
        hb = VGroup(*[bar_rect(ax1, c, 0, 100 * TOP4[c - 1], 0.62, stroke_width=0,
                               fill_color=PURPLE, fill_opacity=0.85) for c in range(1, N + 1)])
        excess = bar_rect(ax1, 1, q, 100 * TOP4[0], 0.62, stroke_width=0, fill_color=RED,
                          fill_opacity=1)                        # only card 1's excess (96 % of it)
        perfect_line = DashedLine(ax1.c2p(0.4, q), ax1.c2p(52.6, q), color=BLUE, stroke_width=3,
                                  dash_length=0.12)
        perfect_lbl = VGroup(text("perfect:", size=LABEL - 2, color=BLUE),
                             text("1 in 52", size=LABEL - 2, color=BLUE)) \
            .arrange(DOWN, buff=0.1, aligned_edge=LEFT).next_to(perfect_line, RIGHT, buff=0.2)
        one15 = text("1 in 15", size=LABEL, color=RED).next_to(ax1.c2p(1, 100 * TOP4[0]), RIGHT, buff=0.3)
        with self.narrate("The obvious check is the top card, the one you'd be dealt. Here's how "
                          "often each card lands there after four riffles.") as beat:
            self.play(FadeOut(heads), FadeOut(tails), FadeOut(guess), FadeOut(sorted_ghost),
                      FadeOut(perfect0.group),
                      meter.left_lbl.animate.set_opacity(0.4),
                      meter.right_lbl.animate.set_opacity(0.4), run_time=0.7)
            topcard = deck.card_at(0)
            tbox = box(topcard, color=INK, buff=0.08, stroke_width=3)
            tlabel = text("top card", size=LABEL, color=INK).next_to(tbox, DOWN, buff=0.15)
            beat.wait_until("top card", offset=-0.2)
            self.play(Create(tbox), FadeIn(tlabel, shift=0.1 * UP), run_time=0.7)
            beat.wait_until("dealt", offset=-0.1)
            moves = deck.relayout(**th)
            tbox_t = box(deck.target(deck.order[0], 0), color=INK, buff=0.06, stroke_width=2.5)
            tlabel_t = text("top card", size=LABEL - 2, color=INK).next_to(tbox_t, DOWN, buff=0.15)
            self.play(*moves, Transform(tbox, tbox_t), Transform(tlabel, tlabel_t), run_time=0.7)
            self.play(Create(ax1), run_time=beat.until("how often", offset=-0.1, min_time=0.5))
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in hb], lag_ratio=0.02),
                      run_time=1.6)
            fly = topcard.copy()
            tgt = hb[deck.order[0] - 1]
            self.play(fly.animate.move_to(tgt.get_top(), aligned_edge=DOWN).set_opacity(0),
                      tgt.animate.set_fill(INK), run_time=0.9)
            self.remove(fly)
            self.play(tgt.animate.set_fill(PURPLE), run_time=0.5)

        with self.narrate("Almost flat. Only the old top card stands out: one time in fifteen. "
                          "Judging by the top card, you'd be right fifty two percent of the time. "
                          "Four riffles look like plenty.") as beat:
            self.play(Create(perfect_line), FadeIn(perfect_lbl, shift=0.1 * LEFT), run_time=1.0)
            beat.wait_until("old top card", offset=-0.2)
            self.play(FadeIn(excess), Indicate(hb[0], color=RED, scale_factor=1.0), run_time=0.7)
            beat.wait_until("fifteen", offset=-0.4)
            self.play(FadeIn(one15, shift=0.1 * LEFT), run_time=0.5)
            beat.wait_until("Judging", offset=-0.1)
            self.add(meter.fill, meter.needle, meter.value)
            self.play(meter.acc.animate.set_value(acc_top),
                      run_time=beat.until("fifty two", min_time=0.8))
            self.play(Indicate(meter.value, color=RED, scale_factor=1.15), run_time=0.8)
            beat.wait_until("Four riffles", offset=-0.1)
            self.play(Indicate(deck.group, color=INK, scale_factor=1.04), run_time=1.0)

        # ============================================================ 4. fail
        C = dict(cx=-1.3, by=-1.25, s=0.74, hs=0.95)   # centre slot: the slow riffle
        gsr = citation("Gilbert, 1955 · Reeds, 1981", color=TGRAY)
        with self.narrate("A guesser who sees the whole deck does far better. The model cuts near "
                          "the middle, then drops cards from each half in proportion to its "
                          "size.") as beat:
            meter.value.clear_updaters()
            # the chart leaves BEFORE the deck moves, so the deck never flies over the bars
            self.play(FadeOut(VGroup(ax1, hb, excess, perfect_line, perfect_lbl, one15)),
                      FadeOut(tbox), FadeOut(tlabel), FadeOut(meter.value), run_time=0.45)
            self.play(FadeIn(ghost, shift=0.1 * UP), FadeIn(ghost_lbl),
                      *deck.relayout(**C), run_time=1.0)
            self.play(*deck.relayout(order=range(1, N + 1)),
                      run_time=beat.until("model", offset=-0.1, min_time=0.8))
            c0 = DECKS["cuts"][0]
            xc = deck.slot_x(c0 - 1) + PITCH * deck.s / 2
            cut_line = DashedLine([xc, deck.by - 0.15, 0], [xc, deck.top_y() + 0.2, 0],
                                  color=GRAY, stroke_width=2.5, dash_length=0.08)
            cut_lbl = MathTex(rf"{c0}\ |\ {N - c0}", font_size=MATH_SMALL, color=TGRAY) \
                .next_to(cut_line, UP, buff=0.08)
            beat.wait_until("cuts", offset=-0.1)
            self.play(FadeIn(gsr), Create(cut_line), FadeIn(cut_lbl), run_time=0.8)
            beat.wait_until("drops", offset=-0.5)
            total = max(2.0, beat.remaining() - 0.1)
            self.riffle(deck, 1, t_cut=0.7, t_drop=total - 0.7, lift=0.55,
                        extra=(FadeOut(cut_line), FadeOut(cut_lbl)))

        # counter (top right) and the two sequences of riffle 1
        cnt_pos = np.array([4.75, 3.1, 0])
        cnt = MathTex("2", font_size=64, color=YELLOW).move_to(cnt_pos)
        cnt_lbl = text("rising sequences", size=LABEL - 2, color=TGRAY).next_to(cnt, DOWN, buff=0.12)
        deck.runs = DECKS["runs"][1]
        marks = always_redraw(lambda: deck_marks(deck))
        r1, r2 = DECKS["runs"][1]
        lowlab = MathTex(r"1, 2, 3, \dots, 26", font_size=MATH_SMALL + 2, color=YELLOW)
        hilab = MathTex(r"27, 28, \dots, 52", font_size=MATH_SMALL + 2, color=YELLOW)
        hilab.next_to([deck.right(), deck.cards[52].get_top()[1], 0], RIGHT, buff=0.25)
        lowlab.next_to([deck.right(), deck.cards[26].get_top()[1], 0], RIGHT, buff=0.25)
        seq1_path = VMobject().set_points_as_corners([deck.cards[c].get_top() for c in r1])
        reader = Dot(radius=0.08, color=YELLOW).move_to(seq1_path.get_start())
        with self.narrate("Each half stays in order, so one riffle leaves two rising sequences: "
                          "runs of consecutive cards, reading left to right.") as beat:
            beat.wait_until("two rising", offset=-0.2)
            self.play(FadeIn(marks), FadeIn(cnt, scale=0.8), FadeIn(cnt_lbl), run_time=1.0)
            beat.wait_until("consecutive", offset=-0.2)
            self.play(FadeIn(lowlab, shift=0.1 * LEFT), FadeIn(hilab, shift=0.1 * LEFT), run_time=0.7)
            beat.wait_until("left to right", offset=-0.2)
            self.add(reader)
            self.play(MoveAlongPath(reader, seq1_path), run_time=max(1.2, beat.remaining() - 0.1),
                      rate_func=LINEAR)

        # ---- level view: why a riffle at most doubles the count
        def ceil_y(k):
            return deck.by + (LH0 + STEPS[k] * (2 ** k + 0.5)) * deck.hs

        def ceil_line(k):
            y = ceil_y(k)
            return DashedLine([deck.left() - 0.15, y, 0], [deck.right() + 0.15, y, 0],
                              color=GRAY, stroke_width=2.5, dash_length=0.09)

        def ceil_tex(k):
            m = MathTex(rf"\le 2^{k} = {2 ** k}", font_size=MATH_SMALL + 2, color=TGRAY)
            return m.next_to([deck.right() + 0.15, ceil_y(k), 0], RIGHT, buff=0.15)

        with self.narrate("Give each sequence its own level. The cut crosses each level once, so "
                          "a riffle can at most split it in two.") as beat:
            self.play(FadeOut(reader), run_time=0.3)
            beat.wait_until("each sequence", offset=-0.1)
            self.play(*deck.relayout(levels=True, step=STEPS[1], hs=1.0), FadeOut(lowlab),
                      FadeOut(hilab), run_time=1.0, rate_func=SMOOTH)
            c2 = DECKS["cuts"][1]
            xc2 = deck.slot_x(c2 - 1) + PITCH * deck.s / 2
            cut2 = DashedLine([xc2, deck.by - 0.15, 0], [xc2, deck.level_y(2) + 0.45, 0],
                              color=GRAY, stroke_width=2.5, dash_length=0.08)
            cut2_lbl = text("cut", size=LABEL - 2, color=TGRAY).next_to(cut2, UP, buff=0.12)
            beat.wait_until("cut", offset=-0.2)
            self.play(Create(cut2), FadeIn(cut2_lbl), run_time=0.6)
            rings = VGroup(*[Circle(radius=0.13, color=YELLOW, stroke_width=3.5)
                             .move_to([xc2, deck.level_y(j), 0]) for j in (1, 2)])
            right2 = DECKS["decks"][1][c2:]
            deck.wash = {c: WASH for c in right2}
            beat.wait_until("crosses", offset=-0.1)
            self.play(LaggedStart(*[Create(r) for r in rings], lag_ratio=0.5),
                      *[deck.cards[c].animate.set_fill(deck.color(c)) for c in right2], run_time=1.0)
            beat.wait_until("so a riffle", offset=-0.15)
            self.riffle(deck, 2, t_cut=0.45, t_drop=0.7, lift=0.4, extra=(FadeOut(rings),),
                        extra_drop=(FadeOut(cut2), FadeOut(cut2_lbl)))
            ceil = ceil_line(2)
            ceil_lbl = ceil_tex(2)
            self.split(deck, 2, STEPS[2], run_time=max(0.9, beat.until("two", occurrence=1, offset=0.3)),
                       extra=(Transform(cnt, MathTex("4", font_size=64, color=YELLOW).move_to(cnt_pos)),
                              FadeIn(ceil), FadeIn(ceil_lbl)))

        tag_sim = text("one simulated deck (GSR model)", size=SMALL, color=TGRAY)
        tag_sim.move_to([0, 2.95, 0]).align_to([-6.2, 0, 0], LEFT)
        with self.narrate("Three riffles, [pause 0.8] eight. Four riffles, [pause 0.6] at most "
                          "sixteen; this deck has fourteen.") as beat:
            deck.wash = {}                                  # the packet tint goes back to grey
            self.riffle(deck, 3, t_cut=0.5, t_drop=0.9, lift=0.35)
            self.split(deck, 3, STEPS[3], run_time=max(0.7, beat.until("eight", offset=0.25)),
                       extra=(Transform(cnt, MathTex("8", font_size=64, color=YELLOW).move_to(cnt_pos)),
                              Transform(ceil, ceil_line(3)), Transform(ceil_lbl, ceil_tex(3))))
            beat.wait_until("Four", offset=-0.1)
            self.riffle(deck, 4, t_cut=0.45, t_drop=0.8, lift=0.3)
            self.split(deck, 4, STEPS[4], run_time=max(0.7, beat.until("sixteen", offset=0.2)),
                       extra=(Transform(cnt, MathTex("14", font_size=64, color=YELLOW).move_to(cnt_pos)),
                              Transform(ceil, ceil_line(4)), Transform(ceil_lbl, ceil_tex(4))))
            self.play(Indicate(ceil_lbl, color=INK, scale_factor=1.15), run_time=0.7)
            beat.wait_until("fourteen", offset=-0.3)
            self.play(Indicate(cnt, color=YELLOW, scale_factor=1.25), FadeIn(tag_sim), run_time=0.8)

        # ---- side by side with a perfect shuffle: the two cold-open decks, same level unit
        perfect = Deck(DECKS["random"], runs=DECKS["random_runs"], levels=True, **SIDE_B)
        p_marks = deck_marks(perfect)
        ghostA = Deck(DECKS["decks"][4], runs=DECKS["runs"][4], levels=True, **SIDE_A)
        line16_y = ghostA.level_y(16.5)
        line16 = DashedLine([ghostA.left() - 0.15, line16_y, 0], [ghostA.right() + 0.15, line16_y, 0],
                            color=GRAY, stroke_width=2.5, dash_length=0.09)
        line16_full = DashedLine([ghostA.left() - 0.15, line16_y, 0], [perfect.right() + 0.15, line16_y, 0],
                                 color=GRAY, stroke_width=2.5, dash_length=0.09)
        lbl16 = MathTex("16", font_size=MATH_SMALL, color=TGRAY).next_to(line16, LEFT, buff=0.1)
        cntA_pos = np.array([ghostA.left() + 0.35, line16_y + 0.45, 0])
        cntA = MathTex("14", font_size=56, color=YELLOW).move_to(cntA_pos)
        cntA_lbl = text("rising sequences", size=LABEL - 2, color=TGRAY).next_to(cntA, RIGHT, buff=0.2)
        tagA = text("4 riffles", size=LABEL, color=PURPLE).next_to(VGroup(cntA, cntA_lbl), UP, buff=0.2)
        tagA.align_to(cntA, LEFT)
        tag_simA = text("one simulated deck (GSR model)", size=SMALL, color=TGRAY)
        tag_simA.next_to([SIDE_A["cx"], SIDE_A["by"], 0], DOWN, buff=0.28)
        cntP = MathTex("26", font_size=56, color=YELLOW).move_to([perfect.left() + 0.35, perfect.top_y() + 0.45, 0])
        avg = MathTex(r"\text{average } 26.5", font_size=MATH_SMALL + 2, color=TGRAY)
        avg.next_to(cntP, RIGHT, buff=0.3)
        tagP = text("perfect shuffle", size=LABEL, color=BLUE).next_to(VGroup(cntP, avg), UP, buff=0.2)
        tagP.align_to(cntP, LEFT)
        rare = MathTex(r"\le 16\text{: 1 in 2.1 million}", font_size=MATH_SMALL, color=TGRAY)
        rare.next_to([SIDE_B["cx"], SIDE_B["by"], 0], DOWN, buff=0.28)
        with self.narrate("A perfect shuffle averages twenty six and a half, and gives sixteen or "
                          "fewer once in two million decks.") as beat:
            self.play(*deck.relayout(**SIDE_A),
                      Transform(ceil, line16), FadeOut(ceil_lbl), FadeIn(lbl16),
                      Transform(cnt, cntA), Transform(cnt_lbl, cntA_lbl), FadeIn(tagA),
                      Transform(tag_sim, tag_simA),
                      LaggedStart(*[FadeIn(perfect.cards[c], shift=0.2 * UP) for c in perfect.order],
                                  lag_ratio=0.01),
                      FadeIn(tagP), run_time=beat.until("averages", offset=-0.3, min_time=1.0))
            self.play(FadeIn(p_marks), FadeIn(cntP, scale=0.8),
                      run_time=beat.until("twenty six", offset=-0.2, min_time=0.5))
            self.play(FadeIn(avg, shift=0.1 * LEFT), run_time=0.6)
            beat.wait_until("sixteen", offset=-0.2)
            self.play(Transform(ceil, line16_full), run_time=0.8)
            self.play(FadeIn(rare, shift=0.1 * UP), run_time=0.6)

        acc4 = 1 - DATA["p_uniform_le16"] / 2
        with self.narrate("Call any deck with sixteen or fewer riffled, and you'd be wrong about "
                          "once in four million games. The top card can't see this; it lives in "
                          "the order between cards.") as beat:
            below = Rectangle(width=line16_full.width, height=line16_y - SIDE_A["by"], stroke_width=0,
                              fill_color=PURPLE, fill_opacity=0.12)
            below.move_to(line16_full.get_center(), aligned_edge=UP)
            below.set_z_index(-2)
            self.play(FadeIn(below), Indicate(lbl16, color=INK, scale_factor=1.3), run_time=0.8)
            beat.wait_until("wrong", offset=-0.5)
            meter.new_value()
            self.add(meter.value)
            self.play(meter.acc.animate.set_value(acc4), run_time=1.4)
            meter.value.clear_updaters()
            precise = MathTex(r"99.99998\%", font_size=MATH, color=INK)
            precise.next_to(meter.needle, UP, buff=0.18).align_to(meter.value, RIGHT)
            self.play(ReplacementTransform(meter.value, precise), run_time=0.5)
            beat.wait_until("top card", offset=-0.2)
            tbox2 = box(deck.card_at(0), color=INK, buff=0.05, stroke_width=2.5)
            self.play(Create(tbox2), run_time=0.6)
            beat.wait_until("order between", offset=-0.2)
            self.play(FadeOut(tbox2), FadeOut(below), Indicate(marks, color=YELLOW, scale_factor=1.0),
                      Indicate(p_marks, color=YELLOW, scale_factor=1.0), run_time=1.0)

        # ============================================================ 5. insight: one chart
        ax = axes((7.5, 36.5), (0, 0.4), x_length=7.4, y_length=3.0,
                  x_ticks=[10, 15, 20, 25, 30, 35], y_ticks=[0, 0.1, 0.2, 0.3, 0.4],
                  x_label="rising sequences", y_label="chance")
        regray(ax)
        ax.shift(np.array([-5.72, -1.6, 0]) - ax.c2p(7.5, 0))
        bd_cite = citation("Bayer & Diaconis, 1992 · Ann. Appl. Probab.", size=20, color=TGRAY)
        blue_bars = VGroup(*[bar_rect(ax, r, 0, U_PMF[r - 1], 0.86, stroke_width=0, fill_color=BLUE,
                                      fill_opacity=0.28) for r in range(8, 37)])
        lo_u, hi_u = support(U_PMF)
        blue_line = step_line(ax, U_PMF, lo_u, hi_u, BLUE, 3)
        kt = ValueTracker(4.0)
        red_op = ValueTracker(0.0)
        K = [4]                                             # the whole-riffle count the tag shows

        def purple_now():
            p = rs_pmf(kt.get_value())
            lo, hi = support(p)
            g = VGroup()
            for r in range(lo, hi + 1):
                if p[r - 1] > U_PMF[r - 1] + 1e-4:
                    g.add(bar_rect(ax, r, U_PMF[r - 1], p[r - 1], 0.86, stroke_width=0,
                                   fill_color=RED, fill_opacity=0.9 * red_op.get_value()))
            g.add(step_line(ax, p, lo, hi, PURPLE, 4))
            return g

        purple = always_redraw(purple_now)
        TAG_Y = ax.c2p(0, 0.4)[1] + 0.32                     # just above the plot, over purple

        def tag_now():
            return riffles_tex(K[0]).move_to([ax.c2p(mean_of(kt.get_value()), 0)[0], TAG_Y, 0])

        tagB = text("perfect", size=LABEL - 2, color=BLUE).move_to(ax.c2p(32.5, 0.14))

        inset = axes((0, 10.5), (0, 1), x_length=3.4, y_length=1.75, x_ticks=[0, 2, 4, 6, 8, 10],
                     y_ticks=[0, 0.5, 1], x_label="riffles", y_label="distance d")
        regray(inset)
        inset.shift(np.array([2.75, -1.8, 0]) - inset.c2p(0, 0))

        SQ = ax.c2p(0.86, 0)[0] - ax.c2p(0, 0)[0]           # one deck = one square token
        y_ax = ax.c2p(0, 0)[1]

        def square_xy(x, y_bottom, color):
            return Square(SQ, stroke_width=0, fill_color=color, fill_opacity=1) \
                .move_to([x, y_bottom + SQ / 2, 0])

        def square_at(r, color):
            return square_xy(ax.c2p(r, 0)[0], y_ax, color)

        def squeeze(d: Deck, x, y_bottom, color):
            """Each bar becomes one 1/52 slice of the square, keeping its left-right order."""
            x0 = x - SQ / 2
            anims = []
            for i, c in enumerate(d.order):
                tgt = Rectangle(width=SQ / N, height=SQ, stroke_width=0, fill_color=color,
                                fill_opacity=1).move_to([x0 + (i + 0.5) * SQ / N, y_bottom + SQ / 2, 0])
                anims.append(Transform(d.cards[c], tgt))
            return anims

        # chance of ONE ordering (Bayer & Diaconis Thm 1): C(16+52-14, 52)/16^52 and 1/52!
        chA = MathTex(r"\text{chance } 3.5\times10^{-60}", font_size=MATH_SMALL + 2, color=PURPLE)
        chA.move_to([SIDE_A["cx"], SIDE_A["by"] - 0.38, 0])
        chP = MathTex(r"\text{chance } 1.2\times10^{-68}", font_size=MATH_SMALL + 2, color=BLUE)
        chP.move_to([SIDE_B["cx"], SIDE_B["by"] - 0.38, 0])
        same = text("same chance", size=LABEL - 2, color=PURPLE).next_to(chA, DOWN, buff=0.18)
        alt_runs = DECKS["alt14_runs"]
        with self.narrate("Bayer and Diaconis proved that in this model, decks with the same count "
                          "are equally likely. [pause 0.7]") as beat:
            meter.freeze()
            self.play(FadeOut(VGroup(meter.base, meter.fill, meter.needle, precise, ghost, ghost_lbl)),
                      FadeOut(gsr), FadeOut(tag_sim), FadeOut(rare), run_time=0.6)
            self.play(FadeIn(bd_cite), run_time=0.5)
            beat.wait_until("model", offset=-0.2)
            self.play(Indicate(cnt, color=YELLOW, scale_factor=1.25),
                      Indicate(cntP, color=YELLOW, scale_factor=1.25), run_time=0.9)
            beat.wait_until("same count", offset=-0.3)
            self.play(FadeIn(chA, shift=0.1 * UP), FadeIn(chP, shift=0.1 * UP), run_time=0.7)
            beat.wait_until("equally", offset=-0.5)
            self.play(*deck.relayout(order=DECKS["alt14"], runs=alt_runs, levels=True),
                      FadeIn(same, shift=0.1 * LEFT), run_time=1.2, rate_func=SMOOTH)
            self.hold(0.4)
            # each deck becomes ONE token (its 52 bars squeeze, in order, into a square) in place
            marks.clear_updaters()
            self.play(FadeOut(VGroup(marks, p_marks, ceil, lbl16, avg, cnt_lbl, chA, chP, same,
                                     tagA, tagP), rate_func=lambda t: smooth(min(1.0, 2.0 * t))),
                      *squeeze(deck, SIDE_A["cx"], SIDE_A["by"], PURPLE),
                      *squeeze(perfect, SIDE_B["cx"], SIDE_B["by"], BLUE),
                      cnt.animate.scale(0.6).move_to([SIDE_A["cx"], SIDE_A["by"] + SQ + 0.33, 0]),
                      cntP.animate.scale(0.6).move_to([SIDE_B["cx"], SIDE_B["by"] + SQ + 0.33, 0]),
                      run_time=max(1.0, beat.remaining()), rate_func=SMOOTH)
            self.remove(*deck.cards.values(), *perfect.cards.values())
            blockA = square_xy(SIDE_A["cx"], SIDE_A["by"], PURPLE)
            blockP = square_xy(SIDE_B["cx"], SIDE_B["by"], BLUE)
            self.add(blockA, blockP)

        one_deckA = text("1 deck", size=SMALL, color=TGRAY)
        one_deckP = text("1 deck", size=SMALL, color=TGRAY)
        with self.narrate("So pile each deck onto its count. [pause 0.4]") as beat:
            # the axes first, on their own; then each token drops onto its count
            self.play(Create(ax), run_time=0.7)
            tA, tP = square_at(14, PURPLE), square_at(26, BLUE)
            self.play(blockA.animate.move_to(tA), blockP.animate.move_to(tP),
                      cnt.animate.next_to(tA, UP, buff=0.18), cntP.animate.next_to(tP, UP, buff=0.18),
                      run_time=max(0.8, beat.until("count", offset=0.1)), rate_func=SMOOTH)
            one_deckA.next_to(cnt, UP, buff=0.2)
            one_deckP.next_to(cntP, UP, buff=0.2)
            self.play(FadeIn(one_deckA, shift=0.1 * DOWN), FadeIn(one_deckP, shift=0.1 * DOWN),
                      run_time=0.5)

        dlive = always_redraw(lambda: Dot(inset.c2p(kt.get_value(), tv_of(kt.get_value())),
                                          radius=0.075, color=RED))

        def d_label(k):
            v = TV[k - 1]
            m = MathTex(rf"d = {v:.2f}", font_size=MATH_SMALL + 2, color=RED)
            # up-right of the dot while d is high; down-left once it is low (keeps x <= 6.4)
            return m.next_to(inset.c2p(k, v), UR if v > 0.5 else DL, buff=0.2)

        dlab = d_label(4)
        with self.narrate("Blue is a perfect shuffle, purple is four riffles. The red area, purple "
                          "above blue, is the distance from random. Right now it's one.") as beat:
            self.play(FadeOut(VGroup(cntP, one_deckP, one_deckA, cnt)), run_time=0.35)
            self.play(FadeOut(blockP),
                      LaggedStart(*[GrowFromEdge(b, DOWN) for b in blue_bars], lag_ratio=0.03),
                      Create(blue_line), FadeIn(tagB),
                      run_time=beat.until("purple", offset=-0.1, min_time=1.0))
            p4 = rs_pmf(4.0)
            pl4 = step_line(ax, p4, *support(p4), PURPLE, 4)
            tagK = always_redraw(tag_now)
            self.play(FadeOut(blockA), Create(pl4), FadeIn(tagK, shift=0.1 * DOWN), run_time=1.0)
            self.remove(pl4)
            self.add(purple)
            beat.wait_until("red area", offset=-0.2)
            self.play(red_op.animate.set_value(1.0), run_time=0.9)
            beat.wait_until("distance", offset=-0.2)
            self.play(Create(inset), run_time=1.0)
            beat.wait_until("Right now", offset=-0.2)
            dot4 = Dot(inset.c2p(4, TV[3]), radius=0.075, color=RED)
            self.play(FadeIn(dot4, scale=1.6), FadeIn(dlab), run_time=0.6)
            self.add(dlive)

        # ---- the gap between the centres (bracket legs stand on the two histograms)
        def gap_y(k):
            p = rs_pmf(k)
            m = mean_of(k)
            yp = float(p[int(round(m)) - 1])
            return max(yp, float(U_PMF[26])) + 0.022, yp

        def gap_now():
            k = kt.get_value()
            m = mean_of(k)
            yb, yp = gap_y(k)
            yu = float(U_PMF[26])
            a, b = ax.c2p(m, yb), ax.c2p(MEAN_U, yb)
            return VGroup(Line(a, b, color=YELLOW, stroke_width=3.5),
                          Line(a, ax.c2p(m, yp), color=YELLOW, stroke_width=2.5),
                          Line(b, ax.c2p(MEAN_U, yu), color=YELLOW, stroke_width=2.5))

        def gap_label(k):
            return MathTex(GAP_TXT[k], font_size=MATH_SMALL + 2, color=YELLOW) \
                .next_to(gap_now()[0], UP, buff=0.18)

        row = MathTex(r"\text{gap:}\;", GAP_TXT[4], r"\to", GAP_TXT[5], r"\to", GAP_TXT[6],
                      r"\to", GAP_TXT[7], font_size=MATH_SMALL + 6, color=YELLOW)
        row.move_to([-3.2, 3.05, 0])
        row.shift((-4.75 - row[0].get_right()[0]) * RIGHT)
        half = DashedLine(inset.c2p(0, 0.5), inset.c2p(10.5, 0.5), color=GRAY, stroke_width=2.5,
                          dash_length=0.08)
        with self.narrate("How many more riffles to bring it below a half? [pause 1.5]") as beat:
            gnum = gap_label(4)
            gap_br = always_redraw(gap_now)
            self.play(Create(gap_br), FadeIn(gnum, shift=0.1 * UP), Write(row[0]), run_time=0.6)
            self.play(TransformFromCopy(gnum, row[1]), run_time=0.5)
            beat.wait_until("below a half", offset=-0.3)
            self.play(Create(half), Indicate(inset.y_axis.numbers[1], color=INK, scale_factor=1.3),
                      run_time=0.9)

        def fade_fast(m):
            return FadeOut(m, rate_func=lambda t: smooth(min(1.0, 3.0 * t)))

        def slide_to(k, run_time):
            """Slide purple to k riffles; the tag names the target at the start; the gap and d
            labels are hidden while the riffle count is not a whole number."""
            K[0] = k
            return [kt.animate(run_time=run_time, rate_func=EASE).set_value(k)]

        dots = {4: dot4}
        with self.narrate("A fifth riffle: point nine two. A sixth: point six one.") as beat:
            for k, cue, val in ((5, "fifth", "nine"), (6, "sixth", "six one")):
                if beat.elapsed() < beat.time_of(cue) - 0.3:
                    beat.wait_until(cue, offset=-0.3)
                rt = beat.until(val, offset=-0.15, min_time=0.8)
                self.play(*slide_to(k, rt), fade_fast(gnum), fade_fast(dlab), run_time=rt)
                d = Dot(inset.c2p(k, TV[k - 1]), radius=0.075, color=RED)
                dots[k] = d
                self.add(d)
                gnum, dlab = gap_label(k), d_label(k)
                self.play(FadeIn(gnum), FadeIn(dlab), run_time=0.3)
                i = k - 4
                self.play(Write(row[2 * i]), TransformFromCopy(gnum, row[2 * i + 1]), run_time=0.5)

        # ---- the accuracy rule, read off the chart at k = 6
        p6 = rs_pmf(6.0)
        zone_x = 24.5                                       # purple > blue for r <= 24 at k = 6
        z0, zm, z1, ztop = ax.c2p(7.5, 0), ax.c2p(zone_x, 0), ax.c2p(36.5, 0), ax.c2p(0, 0.4)[1]
        zA = Rectangle(width=zm[0] - z0[0], height=ztop - z0[1], stroke_width=0, fill_color=PURPLE,
                       fill_opacity=0.1).move_to([(z0[0] + zm[0]) / 2, (z0[1] + ztop) / 2, 0]).set_z_index(-3)
        zB = Rectangle(width=z1[0] - zm[0], height=ztop - z0[1], stroke_width=0, fill_color=BLUE,
                       fill_opacity=0.1).move_to([(zm[0] + z1[0]) / 2, (z0[1] + ztop) / 2, 0]).set_z_index(-3)
        zy = ax.c2p(0, 0.37)[1]
        zA_lbl = text("say riffled", size=LABEL - 2, color=PURPLE).move_to([ax.c2p(17.0, 0)[0], zy, 0])
        zB_lbl = text("say perfect", size=LABEL - 2, color=BLUE).move_to([ax.c2p(30.5, 0)[0], zy, 0])
        areaP = step_area(ax, p6, 8, 24, PURPLE, 0.55)
        areaU = VGroup(*[bar_rect(ax, r, 0, U_PMF[r - 1], 0.86, stroke_width=0, fill_color=BLUE,
                                  fill_opacity=0.95) for r in range(15, 25)])
        EQ_R, EQ_Y, K_Y = 6.2, 2.7, 1.55
        e1 = MathTex(r"\text{accuracy}", "=", r"\tfrac12", "(", "0.78", ")", "+", r"\tfrac12", "(",
                     "1", "-", "0.17", ")", font_size=MATH)
        e1[4].set_color(PURPLE)
        e1[11].set_color(BLUE)
        e1.move_to([3.7, EQ_Y, 0]).align_to([EQ_R, 0, 0], RIGHT)
        e2 = MathTex("=", r"\tfrac12", "+", r"\tfrac12", "(", "0.78", "-", "0.17", ")", font_size=MATH)
        e2[5].set_color(PURPLE)
        e2[7].set_color(BLUE)
        e2.next_to(e1, DOWN, buff=0.3).align_to(e1[1], LEFT)      # '=' under '='
        e3 = MathTex(r"\text{accuracy}", "=", r"\tfrac12", "+", r"\tfrac12", "d", font_size=MATH)
        e3[5].set_color(RED)
        e3.move_to(e1, aligned_edge=LEFT)
        with self.narrate("Guess riffled wherever purple is higher. You catch seventy eight percent "
                          "of riffled decks, but flag seventeen percent of perfect ones. Accuracy "
                          "is a half plus half the difference: the red area.") as beat:
            # one focal point: the gap story steps aside while accuracy is read off the areas
            gap_br.clear_updaters()
            self.play(FadeOut(VGroup(row[0:6], gap_br, gnum, tagB)),
                      FadeIn(zA), FadeIn(zB), FadeIn(zA_lbl), FadeIn(zB_lbl), run_time=1.0)
            beat.wait_until("seventy eight", offset=-0.4)
            self.play(FadeIn(areaP), Write(e1[0:4]), run_time=0.7)
            self.play(ReplacementTransform(areaP.copy(), e1[4]), Write(e1[5]), run_time=0.8)
            beat.wait_until("seventeen", offset=-0.4)
            self.play(FadeOut(areaP), FadeIn(areaU), Write(e1[6:11]), run_time=0.7)
            self.play(ReplacementTransform(areaU.copy(), e1[11]), Write(e1[12]), run_time=0.8)
            beat.wait_until("half plus", offset=-0.5)
            pairs = ((1, 0), (7, 1), (6, 2), (2, 3), (3, 4), (4, 5), (10, 6), (11, 7), (12, 8))
            self.play(FadeOut(areaU),
                      LaggedStart(*[TransformFromCopy(e1[a], e2[b]) for a, b in pairs], lag_ratio=0.12),
                      run_time=1.6)
            beat.wait_until("red area", offset=-0.3)
            self.play(Indicate(VGroup(*e2[4:9]), color=RED, scale_factor=1.1),
                      red_op.animate.set_value(0.35), run_time=0.5)
            self.play(red_op.animate.set_value(1.0), run_time=0.5)

        gap_br = always_redraw(gap_now)
        with self.narrate("A seventh riffle: point three three.") as beat:
            self.play(ReplacementTransform(VGroup(*e1[0:2]), VGroup(*e3[0:2])),
                      ReplacementTransform(VGroup(*e2[1:4]), VGroup(*e3[2:5])),
                      FadeTransform(VGroup(*e2[4:9]), e3[5], stretch=False),
                      FadeOut(VGroup(*e1[2:])), FadeOut(e2[0]),
                      FadeOut(VGroup(zA, zB, zA_lbl, zB_lbl)), FadeIn(row[0:6]), FadeIn(gap_br),
                      run_time=0.8)
            rt = beat.until("three three", offset=-0.15, min_time=0.8)
            self.play(*slide_to(7, rt), fade_fast(dlab), e3.animate.set_opacity(0.3), run_time=rt)
            dots[7] = Dot(inset.c2p(7, TV[6]), radius=0.075, color=RED)
            self.add(dots[7])
            gnum, dlab = gap_label(7), d_label(7)
            self.play(FadeIn(gnum), FadeIn(dlab), run_time=0.3)
            self.play(Write(row[6]), TransformFromCopy(gnum, row[7]), run_time=0.5)

        halves = MathTex(r"(\text{each step} \approx \div 2)", font_size=MATH_SMALL, color=TGRAY)
        halves.next_to(row, RIGHT, buff=0.4)
        spread_y = 0.607 * float(U_PMF[26])          # a bell is 61 % of its peak one spread out
        spread = bracket(ax.c2p(MEAN_U, spread_y), ax.c2p(MEAN_U + SD_U, spread_y), BLUE, tick=0.1)
        spread_num = MathTex(r"\text{spread } 2.1", font_size=MATH_SMALL + 2, color=BLUE)
        spread_num.next_to(ax.c2p(30.0, spread_y), RIGHT, buff=0.05)
        with self.narrate("Meanwhile the gap between the centers roughly halved each riffle, while "
                          "purple's spread settled to blue's: about two.") as beat:
            self.play(FadeOut(e3), run_time=0.5)
            beat.wait_until("gap", offset=-0.2)
            self.play(Indicate(VGroup(row[1:8]), color=YELLOW, scale_factor=1.06), run_time=0.9)
            beat.wait_until("halved", offset=-0.3)
            self.play(FadeIn(halves, shift=0.1 * LEFT), run_time=0.8)
            beat.wait_until("spread", offset=-0.2)
            self.play(Create(spread), FadeIn(spread_num), run_time=0.9)
            beat.wait_until("about two", offset=-0.2)
            self.play(Indicate(spread_num, color=BLUE, scale_factor=1.15), run_time=0.8)

        # ---- the mechanism, shown: rewind to 4 riffles, measure the gap in spreads, replay
        HOP_H = 0.17
        hop_op = ValueTracker(0.0)

        def hops_now():
            g = VGroup()
            op = hop_op.get_value()
            if op <= 1e-3:
                return g
            k = kt.get_value()
            xl = mean_of(k)
            yb, _ = gap_y(k)
            j = 0
            while True:
                xb = MEAN_U - SD_U * j
                if xb <= xl + 1e-6:
                    break
                frac = min(1.0, (xb - xl) / SD_U)
                pa, pb = ax.c2p(xb - SD_U, yb), ax.c2p(xb, yb)
                r = (pb[0] - pa[0]) / 2
                ang = math.acos(1 - 2 * frac)            # a cut hop ends exactly at the gap's end
                arc = Arc(radius=r, start_angle=0, angle=ang, arc_center=(pa + pb) / 2,
                          stroke_color=BLUE, stroke_width=3.5, stroke_opacity=op)
                arc.stretch(HOP_H / r, 1, about_point=(pa + pb) / 2)
                g.add(arc)
                j += 1
            return g

        def ratio_label(k):
            m = MathTex(RATIO_TXT[k], r"\text{ spreads}", font_size=MATH_SMALL + 2)
            m[0].set_color(YELLOW)
            m[1].set_color(BLUE)
            yb, _ = gap_y(k)
            return m.next_to(ax.c2p(MEAN_U, yb), RIGHT, buff=0.3).shift(0.12 * UP)

        hops = always_redraw(hops_now)
        cliff = VMobject(stroke_color=RED, stroke_width=3.5)
        early = VGroup(*[Dot(inset.c2p(k, TV[k - 1]), radius=0.075, color=RED) for k in (1, 2, 3)])
        with self.narrate("While the gap spans several spreads, the distance stays near one. Once "
                          "it's down to about one spread, the distance halves too. That's the "
                          "cliff.") as beat:
            rt = beat.until("several", offset=0.05, min_time=0.9)
            self.play(*slide_to(4, rt), fade_fast(gnum), fade_fast(dlab), run_time=rt)
            self.add(hops)
            self.play(hop_op.animate.set_value(1.0), run_time=0.6)
            r4 = ratio_label(4)
            self.play(FadeIn(r4, shift=0.1 * LEFT), run_time=0.4)
            beat.wait_until("stays near one", offset=-0.3)
            self.play(LaggedStart(*[FadeIn(d, scale=1.6) for d in early], lag_ratio=0.3),
                      Indicate(dots[4], color=RED, scale_factor=1.6), run_time=1.0)
            beat.wait_until("Once", offset=-0.1)
            rt = beat.until("one spread", offset=0.45, min_time=1.2)
            self.play(*slide_to(7, rt), fade_fast(r4), run_time=rt)
            r7 = ratio_label(7)
            self.play(FadeIn(r7, shift=0.1 * LEFT), run_time=0.4)
            beat.wait_until("halves too", offset=-0.3)
            dots[8] = Dot(inset.c2p(8, TV[7]), radius=0.075, color=RED)
            self.play(Indicate(dots[6], color=RED, scale_factor=1.6),
                      Indicate(dots[7], color=RED, scale_factor=1.6), FadeIn(dots[8], scale=1.6),
                      run_time=1.0)
            beat.wait_until("cliff", offset=-0.3)
            cliff.set_points_smoothly([inset.c2p(k, TV[k - 1]) for k in range(1, 9)])
            self.play(Create(cliff), run_time=1.0)

        # ---- 230 from the data, then k: one equation, transformed in place
        prods = VGroup(*[MathTex(PROD_TXT[i], font_size=MATH_SMALL + 6, color=YELLOW)
                         .move_to([row[2 * i + 1].get_center()[0], 2.45, 0]) for i in range(4)])
        prod_head = MathTex(r"\times 2^k\;\approx", font_size=MATH_SMALL + 6, color=YELLOW)
        prod_head.move_to([row[0].get_center()[0], 2.45, 0]).align_to([-4.75, 0, 0], RIGHT)
        prod_arrows = VGroup(*[MathTex(r"\to", font_size=MATH_SMALL + 6, color=YELLOW)
                               .move_to([row[2 * i].get_center()[0], 2.45, 0]) for i in (1, 2, 3)])
        p230 = MathTex(r"\to 230", font_size=MATH_SMALL + 6, color=YELLOW).next_to(prods[3], RIGHT, buff=0.18)
        ES = MATH + 4
        eq1 = MathTex(r"\text{gap}", r"\approx", "230", "/", "2^k", "=", "2.1", font_size=ES)
        eq1[0].set_color(YELLOW); eq1[2:5].set_color(YELLOW); eq1[6].set_color(BLUE)
        eq1.move_to([3.9, EQ_Y, 0]).align_to([EQ_R, 0, 0], RIGHT)
        eq2 = MathTex(r"2^k", r"\approx", "230", "/", "2.1", r"\approx", "110", font_size=ES)
        eq2[0].set_color(YELLOW); eq2[2].set_color(YELLOW); eq2[4].set_color(BLUE)
        eq2.move_to(eq1).align_to(eq1, RIGHT)
        kline = MathTex(r"\Rightarrow\ k", r"\approx", "6.8", font_size=ES)
        kline.move_to([4.5, K_Y, 0]).align_to([EQ_R, 0, 0], RIGHT)
        with self.narrate("Gap times two to the k levels off near two hundred thirty. [pause 1.2] "
                          "So the gap meets the spread when two to the k is about a hundred and "
                          "ten: just under seven. [pause 0.8]") as beat:
            hops.clear_updaters()
            self.play(FadeOut(hops), FadeOut(r7), run_time=0.4)
            self.play(Write(prod_head), run_time=0.5)
            self.play(LaggedStart(*[TransformFromCopy(row[2 * i + 1], prods[i]) for i in range(4)],
                                  lag_ratio=0.35),
                      LaggedStart(*[FadeIn(a) for a in prod_arrows], lag_ratio=0.35),
                      run_time=beat.until("two hundred", offset=-0.3, min_time=1.4))
            self.play(Write(p230), run_time=0.6)
            # sources dim first, then each term flies in from what it measures
            rows = VGroup(row, prod_head, prods, prod_arrows, p230)
            self.play(rows.animate.set_opacity(0.3), spread_num.animate.set_opacity(0.3),
                      FadeOut(halves), run_time=0.35)
            gap_src = gap_now()[0].copy()
            self.play(ReplacementTransform(gap_src, eq1[0], path_arc=-0.9),
                      TransformFromCopy(p230[0][1:], eq1[2], path_arc=0.5),
                      TransformFromCopy(spread_num[0][-3:], eq1[6], path_arc=1.2),
                      Write(eq1[1]), Write(eq1[3:6]), run_time=1.2)
            # staged rearrangement: gap and = leave, 2^k arcs over, 2.1 arcs under, then ≈ 110
            beat.wait_until("about", offset=0.0)
            self.play(FadeOut(eq1[0]), FadeOut(eq1[5]), run_time=0.35)
            self.play(ReplacementTransform(eq1[4], eq2[0], path_arc=1.6),
                      ReplacementTransform(eq1[1], eq2[1]), ReplacementTransform(eq1[2], eq2[2]),
                      ReplacementTransform(eq1[3], eq2[3]),
                      ReplacementTransform(eq1[6], eq2[4], path_arc=-1.6), run_time=0.9)
            self.play(Write(eq2[5:7]), run_time=0.5)
            beat.wait_until("just under", offset=-0.2)
            k68 = DashedLine(inset.c2p(6.77, 0), inset.c2p(6.77, 1.0), color=GRAY, stroke_width=2.5,
                             dash_length=0.08)
            self.play(Write(kline), Create(k68), run_time=1.0)

        # ---- the same equation for n cards (no re-layout: the numbers become their formulas)
        lhsF = MathTex(r"2^k", r"\approx", font_size=ES)
        lhsF[0].set_color(YELLOW)
        fracF = fraction(r"52\cdot 53/12", r"\sqrt{53/12}")
        tailF = MathTex(r"\approx", "110", font_size=ES)
        eqF = VGroup(lhsF, fracF, tailF).arrange(RIGHT, buff=0.2)
        eqF.move_to([3.9, EQ_Y, 0]).align_to([EQ_R, 0, 0], RIGHT)
        lhsN = MathTex(r"2^k", r"\approx", font_size=ES)
        lhsN[0].set_color(YELLOW)
        fracN = fraction(r"n(n+1)/12", r"\sqrt{(n+1)/12}")
        sq = MathTex(r"\sim n^2", font_size=MATH_SMALL + 4, color=YELLOW)
        rt_n = MathTex(r"\sim \sqrt{n}", font_size=MATH_SMALL + 4, color=BLUE)
        eqN = VGroup(lhsN, fracN).arrange(RIGHT, buff=0.2)
        sq.next_to(fracN[0], RIGHT, buff=0.25)
        rt_n.next_to(fracN[2], RIGHT, buff=0.25)
        VGroup(eqN, sq, rt_n).move_to([3.9, EQ_Y, 0]).align_to([EQ_R, 0, 0], RIGHT)
        kN = MathTex("k", r"\approx", r"\tfrac32 \log_2 n - 1.8", font_size=ES)
        kN.move_to(kline).align_to([EQ_R, 0, 0], RIGHT)
        heur = text("(gap = spread rule)", size=SMALL, color=TGRAY).next_to(kN, DOWN, buff=0.15)
        heur.align_to(kN, RIGHT)
        with self.narrate("Both numbers come from the deck's size. [pause 1.0] For n cards, the "
                          "gap grows like n squared, but the spread only like root n, so the cliff "
                          "sits near three halves log base two of n.") as beat:
            purple.clear_updaters()
            gap_br.clear_updaters()
            tagK.clear_updaters()
            ctx = VGroup(ax, blue_bars, blue_line, purple, gap_br, tagK, spread, spread_num)
            self.play(ctx.animate.fade(0.7),
                      ReplacementTransform(eq2[0:2], lhsF), FadeTransform(eq2[2], fracF[0], stretch=False),
                      ReplacementTransform(eq2[3], fracF[1]), FadeTransform(eq2[4], fracF[2], stretch=False),
                      ReplacementTransform(eq2[5:7], tailF), run_time=1.2)
            beat.wait_until("gap grows", offset=-0.2)
            nF, nN = fracF[0][0], fracN[0][0]
            dF, dN = fracF[2][0], fracN[2][0]
            # only the 52s and 53s change (52 -> n, 53 -> n+1); /12, the bar and the root just move
            self.play(ReplacementTransform(lhsF, lhsN), FadeOut(tailF),
                      FadeTransform(VGroup(*nF[0:2]), nN[0], stretch=False),
                      FadeOut(nF[2]),
                      FadeTransform(VGroup(*nF[3:5]), VGroup(*nN[1:6]), stretch=False),
                      ReplacementTransform(VGroup(*nF[5:8]), VGroup(*nN[6:9])),
                      ReplacementTransform(fracF[1], fracN[1]),
                      ReplacementTransform(VGroup(*dF[0:2]), VGroup(*dN[0:2])),
                      FadeTransform(VGroup(*dF[2:4]), VGroup(*dN[2:7]), stretch=False),
                      ReplacementTransform(VGroup(*dF[4:7]), VGroup(*dN[7:10])), run_time=1.0)
            beat.wait_until("squared", offset=-0.2)
            self.play(FadeIn(sq, shift=0.1 * LEFT), run_time=0.5)
            beat.wait_until("root n", offset=-0.1)
            self.play(FadeIn(rt_n, shift=0.1 * LEFT), run_time=0.5)
            beat.wait_until("three halves", offset=-0.3)
            self.play(FadeOut(kline[0][0]), ReplacementTransform(kline[0][1], kN[0]),
                      ReplacementTransform(kline[1], kN[1]), FadeTransform(kline[2], kN[2], stretch=False),
                      run_time=1.2)
            self.play(FadeIn(heur), run_time=0.5)

        # ============================================================ 6. payoff
        big = axes((0, 10.5), (0, 1), x_length=7.0, y_length=3.5, x_ticks=[0, 2, 4, 6, 8, 10],
                   y_ticks=[0, 0.5, 1], x_label="riffles", y_label="distance d")
        regray(big)
        big.shift(np.array([-5.3, -1.9, 0]) - big.c2p(0, 0))
        big_dots = VGroup(*[Dot(big.c2p(k, TV[k - 1]), radius=0.08, color=RED) for k in range(1, 11)])
        big_cliff = VMobject(stroke_color=RED, stroke_width=4).set_points_smoothly(
            [big.c2p(k, TV[k - 1]) for k in range(1, 11)])
        big_half = DashedLine(big.c2p(0, 0.5), big.c2p(10.5, 0.5), color=GRAY, stroke_width=2.5,
                              dash_length=0.1)
        vals = VGroup(*[MathTex(f"{TV[k - 1]:.2f}", font_size=MATH_SMALL, color=RED)
                        .next_to(big.c2p(k, TV[k - 1]), UR, buff=0.22) for k in (5, 6, 7, 8)])
        EQX = 4.05
        small_dots = VGroup(*early, *[dots[k] for k in (4, 5, 6, 7, 8)])
        ald_cite = VGroup(citation("Bayer & Diaconis, 1992 · Ann. Appl. Probab.", size=20, color=TGRAY))
        ald_cite.add_to_back(citation("Aldous, 1983 · Séminaire de Probabilités XVII", size=20,
                                      color=TGRAY).shift(0.3 * UP))
        with self.narrate("Aldous, then Bayer and Diaconis, proved it: for fifty two cards, seven "
                          "riffles is the first count that brings the distance below a half.") as beat:
            dlive.clear_updaters()
            self.play(FadeOut(VGroup(ax, blue_bars, blue_line, purple, tagK, gap_br, spread,
                                     spread_num, rows, k68, dlive)),
                      ReplacementTransform(inset, big), ReplacementTransform(small_dots, big_dots[:8]),
                      ReplacementTransform(cliff, big_cliff), ReplacementTransform(half, big_half),
                      FadeOut(bd_cite), run_time=1.0)
            self.play(FadeIn(big_dots[8:], scale=1.5), FadeIn(ald_cite), run_time=0.8)
            beat.wait_until("fifty two", offset=-0.3)
            self.play(LaggedStart(*[FadeIn(v, shift=0.1 * LEFT) for v in vals], lag_ratio=0.25),
                      run_time=1.3)
            beat.wait_until("seven", offset=-0.2)
            self.play(Indicate(big_dots[6], color=RED, scale_factor=1.8), run_time=0.9)
            beat.wait_until("below", offset=-0.2)
            self.play(Indicate(big_half, color=INK, scale_factor=1.0), run_time=0.8)

        tref = citation("Trefethen & Trefethen, 2000 · Proc. R. Soc. A", color=TGRAY)
        info = VGroup(text("information yardstick:", size=LABEL - 2, color=TGRAY),
                      text("no cliff, 5–6 riffles", size=LABEL - 2, color=TGRAY)) \
            .arrange(DOWN, buff=0.2, aligned_edge=LEFT).move_to([EQX, -1.35, 0])
        band = Rectangle(width=big.c2p(6, 0)[0] - big.c2p(5, 0)[0], height=big.c2p(0, 1)[1] - big.c2p(0, 0)[1],
                         stroke_width=0, fill_color=GRAY, fill_opacity=0.22)
        band.move_to((big.c2p(5, 0) + big.c2p(6, 1)) / 2)
        with self.narrate("Seven belongs to this yardstick. Trefethen and Trefethen measured "
                          "information instead: no cliff, and five or six shuffles do a reasonable "
                          "job.") as beat:
            self.play(Indicate(big.y_title, color=INK, scale_factor=1.1),
                      FadeOut(VGroup(vals[0], vals[1], vals[3])),
                      Indicate(vals[2], color=RED, scale_factor=1.2), run_time=1.0)
            beat.wait_until("Trefethen", offset=-0.2)
            self.play(FadeOut(ald_cite), FadeIn(tref), run_time=0.6)
            beat.wait_until("information", offset=-0.2)
            self.play(FadeIn(info[0], shift=0.1 * UP), run_time=0.7)
            beat.wait_until("no cliff", offset=-0.3)
            self.play(FadeIn(info[1], shift=0.1 * UP), run_time=0.7)
            beat.wait_until("five or six", offset=-0.2)
            self.play(FadeIn(band), run_time=0.8)

        top_curve = DashedVMobject(VMobject(stroke_color=GRAY, stroke_width=3.5).set_points_smoothly(
            [big.c2p(k, TOP_TV[k - 1]) for k in range(1, 11)]), num_dashes=45)
        top_dots = VGroup(*[Dot(big.c2p(k, TOP_TV[k - 1]), radius=0.06, color=GRAY) for k in range(1, 5)])
        top_lbl = text("top card only", size=LABEL - 2, color=TGRAY).next_to(
            big.c2p(1.3, TOP_TV[0]), RIGHT, buff=0.2)
        whole_lbl = text("whole deck", size=LABEL - 2, color=RED).next_to(
            big.c2p(8.25, TV[7] + 0.06), RIGHT, buff=0.15)
        dia = citation("Diaconis, 1996 · PNAS", color=TGRAY)
        eq_final = VGroup(eqN, sq, rt_n, kN)
        with self.narrate("Many Markov chains share this cliff, and samplers share the trap: one "
                          "statistic can settle, like the top card, long before the whole chain "
                          "has.") as beat:
            self.play(FadeOut(tref), FadeIn(dia), FadeOut(info), FadeOut(band), FadeOut(vals[2]),
                      FadeOut(heur), eq_final.animate.set_opacity(0.3), run_time=0.8)
            self.play(Indicate(big_cliff, color=RED, scale_factor=1.0),
                      LaggedStart(*[Indicate(d, color=RED, scale_factor=1.5) for d in big_dots[3:8]],
                                  lag_ratio=0.2), run_time=1.2)
            beat.wait_until("statistic", offset=-0.3)
            self.play(Create(top_curve), FadeIn(top_dots), FadeIn(top_lbl), FadeIn(whole_lbl),
                      run_time=1.4)
            beat.wait_until("top card", offset=-0.2)
            self.play(Indicate(top_dots[3], color=INK, scale_factor=1.6), run_time=0.8)
            beat.wait_until("whole chain", offset=-0.2)
            self.play(Indicate(big_dots[3], color=RED, scale_factor=1.6),
                      Indicate(whole_lbl, color=RED, scale_factor=1.1), run_time=1.0)

        # ============================================================ 7. landing
        land_cnt_pos = np.array([4.6, 2.85, 0])
        tag_pos = np.array([-4.3, 2.85, 0])
        L = dict(cx=0.0, by=-1.1, s=0.8, hs=1.0, step=0.1)
        with self.narrate("Back to the coin flip. After four riffles you'd almost never be wrong, "
                          "same as with an unshuffled deck.") as beat:
            deck2 = Deck(DECKS["decks"][4], runs=DECKS["runs"][4], levels=True, **L)
            marks2 = always_redraw(lambda: deck_marks(deck2))
            meter.acc.set_value(acc4)
            meter.make_live()
            meter.value.clear_updaters()
            meter.left_lbl.set_opacity(0.4)
            meter.right_lbl.set_opacity(0.4)
            prec2 = MathTex(r"99.99998\%", font_size=MATH, color=INK)
            prec2.next_to(meter._needle(), UP, buff=0.18).align_to(precise, RIGHT)
            tagL = riffles_tex(4, MATH).move_to(tag_pos)
            cntL = MathTex("14", font_size=60, color=YELLOW).move_to(land_cnt_pos)
            cntL_lbl = text("rising sequences", size=LABEL - 2, color=TGRAY).next_to(cntL, LEFT, buff=0.25)
            simL = text("one simulated deck (GSR model)", size=SMALL, color=TGRAY)
            simL.next_to(tagL, DOWN, buff=0.15).align_to(tagL, LEFT)
            self.play(FadeOut(VGroup(big, big_dots, big_cliff, big_half, top_curve, top_dots, top_lbl,
                                     whole_lbl, eq_final, dia)), run_time=0.5)
            self.play(FadeIn(deck2.group), FadeIn(marks2), FadeIn(tagL), FadeIn(cntL),
                      FadeIn(cntL_lbl), FadeIn(simL), FadeIn(meter.base), FadeIn(meter.fill),
                      FadeIn(meter.needle), FadeIn(prec2), FadeIn(ghost), FadeIn(ghost_lbl), run_time=0.8)
            beat.wait_until("almost never", offset=-0.2)
            self.play(Indicate(prec2, color=RED, scale_factor=1.12), run_time=0.8)
            beat.wait_until("unshuffled", offset=-0.2)
            self.play(Indicate(marks2, color=YELLOW, scale_factor=1.0), run_time=0.9)

        val = DecimalNumber(100 * acc4, num_decimal_places=1, unit=r"\%", font_size=MATH, color=INK)
        val.add_updater(lambda m: m.set_value(100 * meter.acc.get_value()))
        val.add_updater(lambda m: m.next_to(meter.needle, UP, buff=0.18))
        # the 99.99998 % label hands over to the live number once the needle has moved
        meter.acc.set_value(0.5 + TV[4] / 2)
        val5 = DecimalNumber(100 * meter.acc.get_value(), num_decimal_places=1, unit=r"\%",
                             font_size=MATH, color=INK).next_to(meter._needle(), UP, buff=0.18)
        meter.acc.set_value(acc4)

        def land_riffle(k, t_cut, t_drop, t_split, extra=()):
            self.riffle(deck2, k, t_cut=t_cut, t_drop=t_drop, lift=0.3)
            self.play(*deck2.relayout(runs=DECKS["runs"][k], levels=True),
                      Transform(cntL, MathTex(str(DECKS["R"][k - 1]), font_size=60, color=YELLOW)
                                .move_to(land_cnt_pos)),
                      Transform(tagL, riffles_tex(k, MATH).move_to(tag_pos)),
                      meter.acc.animate.set_value(0.5 + TV[k - 1] / 2), *extra,
                      run_time=t_split, rate_func=SMOOTH)

        with self.narrate("Three more riffles, [pause 1.2] and you'd be right only two times in "
                          "three.") as beat:
            for k in (5, 6, 7):
                hand = (Transform(prec2, val5),) if k == 5 else ()
                land_riffle(k, 0.25, 0.4, 0.4, extra=hand)
                if k == 5:
                    self.remove(prec2)
                    self.add(val)
            beat.wait_until("two times", offset=-0.2)
            self.play(Indicate(val, color=RED, scale_factor=1.15), run_time=0.8)

        with self.narrate("Four riffles fool someone watching the top card. Fooling someone who "
                          "counts sequences that well takes ten.") as beat:
            beat.wait_until("top card", offset=-0.2)
            self.play(Indicate(VGroup(ghost, ghost_lbl), color=INK, scale_factor=1.15), run_time=0.7)
            for k in (8, 9, 10):
                land_riffle(k, 0.28, 0.42, 0.4)
            beat.wait_until("ten", offset=-0.1)
            self.play(Indicate(VGroup(ghost, ghost_lbl), color=INK, scale_factor=1.15), run_time=0.6)

        self.hold(0.6)
        val.clear_updaters()
        meter.freeze()
        marks2.clear_updaters()
        self.play(*[FadeOut(m) for m in list(self.mobjects)], run_time=0.35)
        self.end_card(hold=0.2, run_time=0.3)
