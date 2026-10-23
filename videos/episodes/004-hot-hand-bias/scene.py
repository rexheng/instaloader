"""Sample Space, episode 4: The Hidden Bias That Hid the Hot Hand.

    videos/toolkit/render.sh --preview videos/episodes/004-hot-hand-bias/scene.py Episode /tmp/ep4.mp4
    videos/toolkit/render.sh videos/episodes/004-hot-hand-bias/scene.py Episode \
        videos/episodes/004-hot-hand-bias/final.mp4

Palette (one meaning each, see script.md):
    YELLOW  heads / a hit            GRAY  tails / a miss (and axes)
    BLUE    the streak test and its readings: checked flips, row scores, n_i, what it reads
            for a random shooter, and its verdict arrows ("hot")
    RED     the bias (the gap between what the test reads and one half / zero)
    PURPLE  the real Cornell shooters (GVT 1985 data)
    INK dashed  the assumption ("the obvious guess")
"""
from __future__ import annotations

import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import numpy as np
from manim import *
from sample_space import *

sys.path.insert(0, str(Path(__file__).resolve().parent))
from narration_text import BEATS, GAPS, PRONUNCIATIONS, SPEEDS  # noqa: E402

# ----------------------------------------------------------------------------- data
SEQS = ["".join(p) for p in product("HT", repeat=4)]          # HHHH ... TTTT


def checked(s: str) -> list[int]:
    """Indices of the flips that immediately follow a heads."""
    return [i for i in range(1, 4) if s[i - 1] == "H"]


INFO = {}
for _s in SEQS:
    _c = checked(_s)
    INFO[_s] = dict(chk=_c, h=sum(_s[i] == "H" for i in _c), n=len(_c))
SCORED = [k for k, s in enumerate(SEQS) if INFO[s]["n"] > 0]                  # 14 rows
UNDEF = [k for k, s in enumerate(SEQS) if INFO[s]["n"] == 0]                  # TTTH, TTTT
MEAN = float(sum(Fraction(INFO[SEQS[k]]["h"], INFO[SEQS[k]]["n"]) for k in SCORED) / len(SCORED))
MEAN_T = 25 / 42                                                              # after a tails
assert abs(MEAN - 17 / 42) < 1e-12
assert sum(INFO[SEQS[k]]["h"] for k in SCORED) == 12
assert sum(INFO[SEQS[k]]["n"] for k in SCORED) == 24
# expected difference of averages, after k hits - after k misses, fair shooter (points),
# exact by dynamic programming (check_numbers.py section 2): n = 100 and n = 1000 shots
STREAK_100 = {1: -1.010, 2: -3.137, 3: -7.935}
STREAK_1000 = {1: -0.100, 2: -0.301, 3: -0.708}
VOTES_H, VOTES_T = Fraction(17, 3), Fraction(25, 3)       # votes held: 5 2/3 and 8 1/3 of 14
assert sum(Fraction(INFO[SEQS[k]]["h"], INFO[SEQS[k]]["n"]) for k in SCORED) == VOTES_H
assert VOTES_H + VOTES_T == 14 and VOTES_H / 14 == Fraction(17, 42)

# secondary (grey) TEXT: 8.1:1 on the background (BAR: text >= 7:1). Grey shapes (tails tiles,
# axes, coin rims) keep the series GRAY.
TGRAY = "#A9AEB6"

# ----------------------------------------------------------------------------- layout
COIN_R, COIN_STEP = 0.185, 0.5            # table coins (rings clear the neighbours)
RING_R = COIN_R + 0.04
ROW_Y = [3.05, 2.35, 1.65, 0.95]
CARD_PITCH, CARD_LEFT = 3.2, -6.08
BIG_R, BIG_STEP = 0.58, 1.45
BIG_C = np.array([-0.83, 1.5, 0])         # the big row once the axis is drawn
BIG_C0 = np.array([-0.83, 0.55, 0])       # cold open: vertically centred while it is alone

X0, X1, AX_Y = -5.9, 3.1, -1.7            # number line: share 0 -> X0, 1 -> X1 (+ OFF)
SHIFT1 = 1.4                              # phase 1 (no right column yet): axis centred
OFF = ValueTracker(SHIFT1)
LINE_TOP = 0.5                            # top of the vertical markers
EARLY_TOP = -0.05                         # dashed line top while the big row is on screen
LBL_Y = -0.4                              # marker labels sit between the two strips
SA_Y, SB_Y, TILE_H = 0.3, -1.0, 0.4       # top strip (pooled), bottom strip (votes)
CORR_Y = ROW_Y[3] - 0.35                  # the corridor between the table and the pooled strip
DOT_CORR = ROW_Y[3] - 0.5                 # the score dots' corridor (no strip under the table yet)
VLBL_Y = -0.35                            # vote counts, between the two strips
FORM_X = 3.45                             # right column
FA_Y, FB_Y = 0.07, -1.2                   # the formula pair: ratio of totals / average of ratios
CNT_Y1, CNT_Y2 = -0.8, -1.25              # "12 heads · 8 rows" / "12 tails · 11 rows"
RC_X = 3.45
C = X0 + (X1 - X0) * 0.5                  # x of one half once the axis has moved left
W = X1 - X0

# mirror + payoff: once the table is gone the whole picture rises (DY) and the lanes open up
DY = 1.0
AX2 = AX_Y + DY                           # the share / gap axis
SA2, SB2 = 1.4, 0.0                       # lanes: after heads (hits), after tails (misses)
LBL2 = 0.7                                # between the lanes: cursor ends, the -19 arrow
CUR_TOP, CUR_BOT = SA2 + 0.32, SB2 - 0.32
PT = 0.45                                 # payoff: units per point (ticks = the share axis ticks)
SH2 = 1.4                                 # payoff: the chart re-centres once the right column goes
G_TOP, G_ARR = AX2 + 2.2, AX2 + 1.1       # gap axis: marker tops, bias arrow


def vx(v: float) -> float:
    return X0 + OFF.get_value() + (X1 - X0) * v


def gx(points: float) -> float:
    return C + PT * points


def early(end: float = 0.55):
    """smooth, finished by `end` (fraction of the animation)."""
    return lambda t: smooth(min(1.0, t / end))


def hand_off(src: Mobject, dst: Mobject) -> AnimationGroup:
    """`src` slides toward `dst`'s place and is gone by mid-way; `dst` then fades in there.
    No frame shows the two glyph sets on top of each other (unlike a cross-fade morph)."""
    return AnimationGroup(
        FadeOut(src, shift=dst.get_center() - src.get_center(), scale=0.8, rate_func=early()),
        FadeIn(dst, scale=0.8, rate_func=delayed(0.45)))


def window(a: float, b: float):
    """smooth from 0 at `a` to 1 at `b` (fractions of the animation)."""
    return lambda t: smooth(ramp(t, a, b))


def delayed(start: float):
    """smooth, but only from `start` (fraction of the animation) on."""
    return lambda t: smooth(min(1.0, max(0.0, (t - start) / (1.0 - start))))


def via(*waypoints):
    """path_func for a Transform: the shape morphs as usual while its centre travels along a
    Bezier curve through `waypoints` (so a flight can be routed around other labels)."""
    def pf(start, end, alpha):
        c0, c1 = start.mean(axis=0), end.mean(axis=0)
        ctrl = [c0] + [np.array(w, dtype=float) for w in waypoints] + [c1]
        c = bezier(ctrl)(alpha)
        return start + (end - start) * alpha + (c - (c0 + (c1 - c0) * alpha))
    return pf


def route(points, r: float = 0.12):
    """Position along a polyline through `points` with its corners rounded (radius r), by arc
    length: f(t), t in [0, 1].  Used to run a copy along the gaps of the table."""
    pts = [np.array(p, dtype=float) for p in points]
    dense = [pts[0]]
    for j in range(1, len(pts) - 1):
        a, b, c = pts[j - 1], pts[j], pts[j + 1]
        lin, lout = np.linalg.norm(b - a), np.linalg.norm(c - b)
        if lin < 1e-9 or lout < 1e-9:
            continue
        din, dout = (b - a) / lin, (c - b) / lout
        rr = min(r, lin / 2, lout / 2)
        p_in, p_out = b - din * rr, b + dout * rr
        for s in np.linspace(0.0, 1.0, 9):
            dense.append((1 - s) ** 2 * p_in + 2 * (1 - s) * s * b + s ** 2 * p_out)
    dense.append(pts[-1])
    dense = np.array(dense)
    seg = np.linalg.norm(np.diff(dense, axis=0), axis=1)
    cum = np.concatenate([[0.0], np.cumsum(seg)])

    def f(t: float) -> np.ndarray:
        d = min(max(t, 0.0), 1.0) * cum[-1]
        j = int(min(max(np.searchsorted(cum, d, side="right") - 1, 0), len(seg) - 1))
        u = (d - cum[j]) / max(seg[j], 1e-9)
        return dense[j] + (dense[j + 1] - dense[j]) * u
    return f


def ramp(x: float, x0: float, x1: float) -> float:
    return min(1.0, max(0.0, (x - x0) / (x1 - x0)))


def ease_sine(u: float) -> float:
    """ease-in-out sine (peak speed 1.57x the mean; manim's smooth peaks at 2.5x)."""
    u = min(max(u, 0.0), 1.0)
    return 0.5 - 0.5 * np.cos(PI * u)


# round 9 (craft fix 3): the 24 checked flips pour one card column at a time. Each column's
# discs land in a block of the strip right under it (columns 2 and 3, four flips each, pour
# together), then the strip sorts into heads | tails. Each disc runs along the gap under its
# row to the nearer channel beside its card, down it, and along the corridor to its tile.
POUR_GROUPS = ((0,), (1,), (2, 3))
POUR_D, POUR_LAG, POUR_MIN = 0.72, 0.74, 0.24   # flight (s), lag per group (s), min spacing


def pour_plan(seqs, info, tile_x):
    """-> list of dict(k, i, face, block, pts, offset) for the 24 checked flips, and the total
    run time. Tiles within a column's block are assigned to minimise the squared route lengths;
    start offsets are the earliest that keep every two discs >= POUR_MIN apart in flight."""
    from scipy.optimize import linear_sum_assignment
    cols = {c: [] for c in range(4)}
    for k, s in enumerate(seqs):
        r, c = divmod(k, 4)
        for i in info[s]["chk"]:
            cols[c].append(dict(k=k, r=r, c=c, i=i, face=s[i]))
    blocks, j0 = {}, 0
    for c in range(4):
        blocks[c] = list(range(j0, j0 + len(cols[c])))
        j0 += len(cols[c])
    assert j0 == 24

    def pts_for(d, j):
        left = CARD_LEFT + CARD_PITCH * d["c"]
        xc, yg, xt = left + COIN_R + COIN_STEP * d["i"], ROW_Y[d["r"]] - 0.35, tile_x(j)
        best = None
        for xch in [left - 0.24] + ([left + 2.96] if d["c"] < 3 else []):
            if d["r"] < 3:
                p = [(xc, yg), (xch, yg), (xch, CORR_Y), (xt, CORR_Y), (xt, SA_Y)]
            else:
                p = [(xc, yg), (xt, CORR_Y), (xt, SA_Y)]
            L = sum(np.hypot(p[q + 1][0] - p[q][0], p[q + 1][1] - p[q][1])
                    for q in range(len(p) - 1))
            if best is None or L < best[0]:
                best = (L, p)
        return best

    plan = []
    for c in range(4):
        ds = cols[c]
        cost = np.array([[pts_for(d, j)[0] ** 2 for j in blocks[c]] for d in ds])
        rows_, cols_ = linear_sum_assignment(cost)
        perm = [blocks[c][cols_[list(rows_).index(q)]] for q in range(len(ds))]
        for d, j in zip(ds, perm):
            d["block"] = j
            d["pts"] = [(x, y, 0.0) for x, y in pts_for(d, j)[1]]
            plan.append(d)
    # schedule: group by group, lowest rows first; each disc starts as early as it can
    placed = []
    grid = np.linspace(0.0, 1.0, 60)
    for g, gcols in enumerate(POUR_GROUPS):
        ds = sorted([d for d in plan if d["c"] in gcols], key=lambda d: (-d["r"], d["c"], d["i"]))
        for d in ds:
            f = route(d["pts"])
            off = g * POUR_LAG
            while True:
                ok = True
                for (f2, o2) in placed:
                    for u in grid:
                        t = off + u * POUR_D
                        u2 = (t - o2) / POUR_D
                        if u > 0.93 or not (0.0 < u2 < 0.93):
                            continue
                        if np.linalg.norm(f(ease_sine(u)) - f2(ease_sine(u2))) < POUR_MIN:
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    break
                off += 0.02
            d["offset"] = off
            d["route"] = f
            placed.append((f, off))
    total = max(d["offset"] for d in plan) + POUR_D
    return plan, total


def emerge(src: Mobject, dst: Mobject, run_time: float = 1.0, arc: float = 0.0, path=None,
           shift=ORIGIN):
    """TransformFromCopy whose copy starts invisible (and optionally shifted), so no frame
    shows the copy doubled over its source: it fades in as it leaves and lands as `dst`."""
    cp = src.copy().shift(shift)
    cp.set_fill(opacity=0).set_stroke(opacity=0)
    kw = dict(path_func=path) if path is not None else dict(path_arc=arc)
    return ReplacementTransform(cp, dst, run_time=run_time, rate_func=smooth, **kw)


# ----------------------------------------------------------------------------- pieces
def make_coin(face: str, r: float = COIN_R) -> VGroup:
    heads = face == "H"
    col = YELLOW if heads else GRAY
    disk = Circle(radius=r, stroke_color=col, stroke_width=4 if r > 0.3 else 3,
                  fill_color=col, fill_opacity=0.18 if heads else 0.0)
    # table coins: letters at >= 24 px cap height (Text 19 bold: 24.5 px)
    let = Text(face, font=SERIF, font_size=max(46 * r / 0.5, 19), color=YELLOW if heads else TGRAY,
               weight=BOLD).move_to(disk)
    if r < 0.3:
        # a token's own glyph (24.5 px, inside its 0.37-unit coin; the fill already says H or T):
        # held to the 24 px tick floor, since a 34 px letter cannot fit the coin
        let.ss_role = "tick"
    return VGroup(disk, let)


def ring(c: Mobject, r: float, width: float = 3.5) -> Circle:
    return Circle(radius=r, color=BLUE, stroke_width=width).move_to(c)


def score_tex(h, n, size: float = 36) -> MathTex:
    m = MathTex(str(h), "/", str(n), font_size=size)
    m[0].set_color(YELLOW)
    m[1].set_color(TGRAY)
    m[2].set_color(BLUE)
    return m


def value_tex(s: str) -> MathTex:
    """A reading of the test in the right column (blue = what the test reads)."""
    return MathTex(s, font_size=36, color=BLUE)


def pulse(m: Mobject, s: float = 1.12, run_time: float = 0.8, edge=None):
    """<= 1 s colour-preserving emphasis (yellow means heads here, so no yellow flash).
    `edge`: grow away from that edge (a label next to its line grows away from the line)."""
    if edge is None:
        return m.animate(rate_func=there_and_back, run_time=run_time).scale(s)
    return m.animate(rate_func=there_and_back, run_time=run_time).scale(s, about_edge=edge)


def tile(face, width: float, x: float, y: float) -> Rectangle:
    heads = face == "H"
    return Rectangle(width=width, height=TILE_H, stroke_width=0,
                     fill_color=YELLOW if heads else GRAY,
                     fill_opacity=0.9 if heads else 0.45).move_to([x, y, 0])


def block(x_from: float, x_to: float, y: float) -> Rectangle:
    """One merged yellow rectangle (the heads part of a strip, as a single object)."""
    return Rectangle(width=x_to - x_from, height=TILE_H, stroke_width=0, fill_color=YELLOW,
                     fill_opacity=0.9).move_to([(x_from + x_to) / 2, y, 0])


def h_arrow(x_from: float, x_to: float, y: float, color=INK, width: float = 4) -> Arrow:
    return Arrow([x_from, y, 0], [x_to, y, 0], buff=0, color=color, stroke_width=width,
                 max_tip_length_to_length_ratio=0.18, tip_length=0.2)


def pct_ticks(vals, labels, x_of, y=AX_Y):
    marks = VGroup(*[Line([x_of(v), y - 0.08, 0], [x_of(v), y + 0.08, 0], color=GRAY,
                          stroke_width=2.5) for v in vals])
    nums = VGroup(*[MathTex(t, font_size=30, color=TGRAY).move_to([x_of(v), y - 0.36, 0])
                    for v, t in zip(vals, labels)])
    return marks, nums


def lane_label(cond: str) -> VGroup:
    """'after <cond>' as VGroup(after, cond), laid out by one Text (no ligatures, so glyph k is
    character k) so the kerning is natural. "after" is its own piece, so a lane can change its
    condition ("heads" -> "3 hits") while "after" stays where it is (round 10)."""
    s = "after " + cond
    t = Text(s, font=SERIF, font_size=26, color=INK, disable_ligatures=True)
    assert len(t) == len(s), (len(t), s)
    return VGroup(VGroup(*[m for m in t[0:5] if m.has_points()]),
                  VGroup(*[m for m in t[6:] if m.has_points()]))


def hit_glyph(k: int) -> VGroup:
    """k hits in a row: k small yellow dots (yellow = a hit, as everywhere)."""
    return VGroup(*[Dot(radius=0.065, color=YELLOW) for _ in range(k)]).arrange(RIGHT, buff=0.07)


def flag_to(g: Mobject, tick: Line) -> Mobject:
    """Hang glyph `g` like a flag on the left of its tick's top, so it travels with the tick."""
    top = tick.get_top()
    return g.move_to([top[0] - 0.09 - g.width / 2, top[1] - 0.075, 0])


class Episode(NarratedScene):
    EPISODE = 4
    TITLE = "The Hidden Bias That Hid the Hot Hand"
    # PRODUCTION_GUIDE §13: shaped cadence (gaps follow the sense) at 0.83, the series' speed
    CADENCE = "shaped"
    SPEED = 0.82
    PRONUNCIATIONS = PRONUNCIATIONS

    # ========================================================================= build
    def adopt(self, *groups):
        """Pieces animated in one by one live at top level; hand them back to their group so
        later transforms/dims of the group act on exactly what is on screen."""
        for g in groups:
            self.remove(*g.get_family()[1:])
            self.add(g)

    def beat(self, key: str):
        return self.narrate(BEATS[key], gap=GAPS.get(key), speed=SPEEDS.get(key))

    def fly_into(self, srcs, target, lag: float = 0.02, start: float = 0.4, arc: float = 0.0,
                 bright: bool = False):
        """Copies of `srcs` fly into `target` and shrink away as it appears there: each copy
        stays a whole glyph or shape in flight (no glyph-by-glyph shatter). `bright`: copies
        of dimmed glyphs fly at full strength. Call clean_fly() after the play."""
        copies = [s.copy() for s in srcs]
        if bright:
            for cp in copies:
                cp.set_opacity(1.0)
        self.add(*copies)
        self._fly.extend(copies)
        c = target.get_center()
        return AnimationGroup(
            LaggedStart(*[cp.animate(rate_func=smooth, path_arc=arc).move_to(c).scale(0.3)
                          .set_opacity(0) for cp in copies], lag_ratio=lag),
            FadeIn(target, scale=0.6, rate_func=delayed(start)))

    def clean_fly(self):
        self.remove(*self._fly)
        self._fly = []

    def travel(self, src, end, waypoints=(), scale_to: float = 1.0, fade=(0.3, 0.6, 0.85),
               bright: bool = False, start_shift=ORIGIN):
        """A copy of `src` travels whole along a Bezier through `waypoints` to the point `end`.
        Its opacity rises from 0 while it leaves (so it is never seen doubled over its source)
        and falls to 0 before it arrives (so it is never seen over the glyph that replaces it):
        fade = (fully visible at, starts fading at, gone at), as fractions of the run.  Play it
        with rate_func linear (position is eased inside); call clean_fly() after the play.
        `start_shift`: the copy materialises that far from its source (e.g. just below a coin,
        so it never crosses the coin or its neighbours)."""
        base = src.copy().shift(start_shift)
        if bright:
            base.set_opacity(1.0)
        cp = base.copy().fade(1.0)
        self.add(cp)
        self._fly.append(cp)
        curve = bezier([base.get_center()] + [np.array(w, dtype=float) for w in waypoints]
                       + [np.array(end, dtype=float)])
        a, b, c = fade

        def upd(m, alpha):
            t = smooth(alpha)
            k = min(1.0, alpha / a) if a > 0 else 1.0
            if alpha > b:
                k *= max(0.0, 1.0 - (alpha - b) / (c - b))
            m.become(base)
            m.scale(1.0 + (scale_to - 1.0) * t)
            m.move_to(curve(t))
            m.fade(1.0 - k)

        return UpdateFromAlphaFunc(cp, upd, rate_func=linear)

    def pour(self, coin, tile_, pts) -> AnimationGroup:
        """One checked flip pours into its pooled tile: a small disc of the tile's colour
        fades in at the first point (just under its coin), runs along `pts` (the gaps of the
        table) and grows into the tile at the end.  Call clean_fly() after the play."""
        op = tile_.get_fill_opacity()
        dot = Circle(radius=0.07, stroke_width=0, fill_color=tile_.get_fill_color(),
                     fill_opacity=0.0).move_to(pts[0])
        self._fly.append(dot)
        f = route(pts)

        def upd(m, a):
            m.move_to(f(smooth(a)))
            m.set_fill(opacity=op * ramp(a, 0.0, 0.12) * (1.0 - ramp(a, 0.9, 1.0)))

        return AnimationGroup(UpdateFromAlphaFunc(dot, upd, rate_func=linear),
                              FadeIn(tile_, scale=0.3, rate_func=delayed(0.86)))

    @staticmethod
    def depart(m, end, waypoints=(), scale_to: float = 0.3, mid: float = 0.4,
               fade=(0.25, 0.6, 0.9)):
        """`m` itself (no copy, so it is never seen doubled) leaves along a Bezier through
        `waypoints` to `end`: it steps back to `mid` opacity as it lifts off, travels at that
        strength, and is gone before it arrives (fade = (at mid by, starts fading, gone by))."""
        base = m.copy()
        curve = bezier([base.get_center()] + [np.array(w, dtype=float) for w in waypoints]
                       + [np.array(end, dtype=float)])
        a, b, c = fade

        def upd(mob, alpha):
            t = smooth(alpha)
            if alpha < a:
                k = 1.0 - (1.0 - mid) * alpha / a
            elif alpha < b:
                k = mid
            else:
                k = mid * max(0.0, 1.0 - (alpha - b) / (c - b))
            mob.become(base)
            mob.scale(1.0 + (scale_to - 1.0) * min(1.0, t / 0.4))   # small before it travels
            mob.move_to(curve(t))
            mob.fade(1.0 - k)

        return UpdateFromAlphaFunc(m, upd, rate_func=linear)

    def build_table(self):
        self.cards = []
        for k, s in enumerate(SEQS):
            r, c = divmod(k, 4)
            left, y = CARD_LEFT + CARD_PITCH * c, ROW_Y[r]
            coins = VGroup(*[make_coin(f).move_to([left + COIN_R + COIN_STEP * i, y, 0])
                             for i, f in enumerate(s)])
            inf = INFO[s]
            rings = VGroup(*[ring(coins[i], RING_R) for i in inf["chk"]])
            if inf["n"]:
                score = score_tex(inf["h"], inf["n"])
            else:
                score = MathTex(r"\text{--}", font_size=36, color=GRAY)
            score.next_to(coins, RIGHT, buff=0.3)
            self.cards.append(dict(seq=s, coins=coins, rings=rings, score=score, **inf))

    def build_axis(self):
        line = Line([vx(0) - 0.2, AX_Y, 0], [vx(1) + 0.2, AX_Y, 0], color=GRAY, stroke_width=2.5)
        vals = [0, 0.25, 0.5, 0.75, 1]
        ticks, nums = pct_ticks(vals, [r"0\%", r"25\%", r"50\%", r"75\%", r"100\%"], vx)
        title_ = self.axis_title("checked flips that are heads")
        self.axis = VGroup(line, ticks, nums, title_)

    @staticmethod
    def axis_title(s: str) -> VGroup:
        """The share axis title as four word groups (checked | flips | that are | heads), laid
        out by one Text so kerning is natural, right-aligned to the axis, on a fixed baseline
        (the bottom of "checked"), so two titles swap words without any vertical jump."""
        # no ligatures, so glyph k is character k of the string (spaces included)
        t = Text(s, font=SERIF, font_size=26, color=TGRAY, disable_ligatures=True)
        assert len(t) == len(s), (len(t), s)
        words, cuts, i = s.split(" "), [], 0
        for w in words:
            cuts.append((i, i + len(w)))
            i += len(w) + 1
        groups = [(0, 1), (1, 2), (2, 4), (4, 5)]           # checked, flips, that are, heads
        g = VGroup(*[VGroup(*[m for m in t[cuts[a][0]:cuts[b - 1][1]] if m.has_points()])
                     for a, b in groups])
        g.move_to([vx(1) + 0.2 - g.width / 2, AX_Y - 0.82, 0])
        g.shift(UP * (AX_Y - 0.92 - g[0].get_bottom()[1]))
        return g

    def retitle(self, holder: VGroup, dst: VGroup, run_time: float = 0.9):
        """Swap the axis title's words in place: "checked" and "that are" slide to their new
        spots; the other two words rise out while their replacements rise in. The holder
        stays the same object, so every group that contains it stays intact."""
        dst = dst.copy()
        anims, keep = [], []
        for i, (o, n) in enumerate(zip(list(holder.submobjects), dst)):
            if i in (0, 2):
                anims.append(o.animate.move_to(n.get_center()))
                keep.append(o)
            else:
                n.shift(DOWN * 0.12).set_opacity(0)
                holder.add(n)
                anims += [o.animate(rate_func=lambda t: smooth(min(1.0, 1.8 * t)))
                          .shift(UP * 0.12).set_opacity(0),
                          n.animate(rate_func=delayed(0.45)).shift(UP * 0.12).set_opacity(1)]
                keep.append(n)
        return anims, (holder, keep)

    def swap_glyphs(self, holders, targets, *extra, run_time: float = 0.9):
        """Each holder (a coin's letter or word) shrinks out, then its target grows in at the same
        place; the holder then *becomes* the target, so every group that holds it stays intact."""
        tmps = [t.copy() for t in targets]
        self.play(*[h.animate(rate_func=lambda t: smooth(min(1.0, 1.8 * t))).scale(0.6)
                    .set_opacity(0) for h in holders],
                  *[FadeIn(t_, scale=0.6, rate_func=delayed(0.45)) for t_ in tmps],
                  *extra, run_time=run_time)
        for h, t in zip(holders, targets):
            h.become(t)
        self.remove(*tmps)

    @staticmethod
    def retitle_done(token):
        holder, keep = token
        holder.submobjects = list(keep)

    def build_mini(self, scale: float = 0.81, at=(0, 0.1, 0), op: float = 0.75) -> VGroup:
        """A ghost of all sixteen sequences (the table, in miniature): the rows packed tight
        (no room is needed for scores) so the coins keep radius 0.185 * 0.81 = 0.15."""
        rows = []
        for k, cd in enumerate(self.cards):
            r, c = divmod(k, 4)
            g = VGroup(*[make_coin(f).move_to([c * 1.93 + i * 0.42, -r * 0.5, 0])
                         for i, f in enumerate(cd["seq"])])
            rows.append(g)
        mini = VGroup(*rows)
        mini.scale(scale).move_to(np.array(at, dtype=float))
        for mm in mini.family_members_with_points():
            mm.set_stroke(opacity=op * mm.get_stroke_opacity())
            mm.set_fill(opacity=op * mm.get_fill_opacity())
        return mini

    # ========================================================================= scene
    def construct(self):
        self._fly = []
        self.build_table()
        self.build_axis()
        cards = self.cards

        # ---------------------------------------------------------------- big row
        big = VGroup(*[make_coin(f, BIG_R) for f in "HHTH"]).arrange(RIGHT, buff=BIG_STEP - 2 * BIG_R)
        big.move_to(BIG_C0)
        big_rings = VGroup(ring(big[1], BIG_R + 0.1, 5), ring(big[2], BIG_R + 0.1, 5))
        arcs = VGroup(*[CurvedArrow(big[i].get_top() + UP * 0.14, big[i + 1].get_top() + UP * 0.14,
                                    angle=-PI / 2, color=BLUE, stroke_width=5, tip_length=0.22)
                        for i in (0, 1)])
        big_score = score_tex(1, 2, size=60).next_to(big, RIGHT, buff=0.75)
        lift = (BIG_C - BIG_C0)
        mini = self.build_mini(at=(vx(0.5), -0.15, 0))
        for g_ in mini:
            self.allow_overlap(g_, reason="ghost miniature of the 16-row table (75% opacity): "
                                          "each letter sits inside its own small coin")
        qmark = MathTex("?", font_size=64, color=INK).move_to([vx(0.5), AX_Y + 1.15, 0])
        # the three answers the viewer can commit to, on the line itself
        opts = VGroup(*[MathTex(s_, font_size=40, color=INK).move_to([vx(v), AX_Y + 0.45, 0])
                        for s_, v in ((r"<\,1/2", 0.27), (r"=\,1/2", 0.5), (r">\,1/2", 0.73))])

        # ================================================================ 1 cold open
        with self.beat("open") as beat:
            thin = [c.copy().stretch(0.06, 0) for c in big]
            self.play(LaggedStart(*[Transform(t, c) for t, c in zip(thin, big)], lag_ratio=0.3),
                      run_time=beat.until_end_of("times"))
            self.remove(*thin)
            self.add(big)
            beat.wait_until("check", offset=-0.1)
            self.play(Create(arcs[0]), Create(arcs[1]), run_time=beat.until("next", offset=0.1))
            self.play(Create(big_rings[0]), Create(big_rings[1]), run_time=0.7)
            beat.wait_until("one", offset=-0.2)
            # the ringed heads' yellow disc travels under the row into the yellow 1 (no letter
            # travels; the copy fades in as it leaves its coin, so nothing is seen doubled), and
            # the two rings travel the same way into the 2
            # (each copy materialises just below its coin while the coin answers, so no copy
            # ever crosses a coin)
            e1, e2 = big_score[0].get_center(), big_score[2].get_center()
            low = big.get_bottom()[1] - 0.95
            self.play(self.travel(big[1][0], e1, [(big[1].get_x() + 1.0, low - 0.3, 0),
                                                  (e1[0] - 0.5, low - 0.2, 0)],
                                  scale_to=0.3, fade=(0.3, 0.6, 0.85),
                                  start_shift=DOWN * 1.3),
                      pulse(big[1], 1.08, run_time=0.6),
                      FadeIn(big_score[0], scale=0.6, rate_func=delayed(0.7)), run_time=0.9)
            self.clean_fly()
            self.play(LaggedStart(*[self.travel(r_, e2, [(r_.get_x() + 1.0, low - 0.4, 0),
                                                         (e2[0] - 0.5, low - 0.3, 0)],
                                                scale_to=0.25, fade=(0.3, 0.6, 0.85),
                                                start_shift=DOWN * 1.45)
                                    for r_ in big_rings], lag_ratio=0.15),
                      *[r_.animate(rate_func=there_and_back, run_time=0.6).set_stroke(width=8)
                        for r_ in big_rings],
                      FadeIn(big_score[1]),
                      FadeIn(big_score[2], scale=0.6, rate_func=delayed(0.72)), run_time=0.9)
            self.clean_fly()
            self.adopt(big_rings, big_score, arcs)
            # "Do this for every four flip run": the row rises, the share axis draws beneath
            # it, and the ghost of all sixteen runs deals in between while the row steps back
            beat.wait_until("Do", offset=-0.1)
            row = VGroup(big, big_rings, arcs, big_score)
            self.play(row.animate.shift(lift), Create(self.axis[0]), Create(self.axis[1]),
                      run_time=0.8)
            row.save_state()
            self.play(LaggedStart(*[FadeIn(g, shift=0.08 * DOWN) for g in mini], lag_ratio=0.08),
                      row.animate.fade(0.6), FadeIn(self.axis[2]), FadeIn(self.axis[3]),
                      run_time=beat.until_end_of("run"))
            # "and average": the sixteen rows collapse onto the line, as a "?"
            beat.wait_until("average", offset=-0.1)
            self.play(mini.animate.scale(0.12).move_to(qmark).set_opacity(0), Restore(row),
                      FadeIn(qmark, scale=0.6, rate_func=delayed(0.3)),
                      run_time=beat.until("Below", offset=-0.05))
            self.remove(mini, *mini)
            self.adopt(self.axis)
            # "Below, at, or above one half?": each answer appears where it sits on the line
            for w_, o_ in zip(("Below", "at", "above"), opts):
                beat.wait_until(w_, offset=-0.1)
                self.play(FadeIn(o_, shift=0.1 * UP), run_time=0.4)

        # ================================================================ 2 stakes
        dashed = DashedLine([vx(0.5), AX_Y, 0], [vx(0.5), EARLY_TOP, 0], color=INK,
                            stroke_width=3, dash_length=0.12)
        dashed_full = DashedLine([vx(0.5), AX_Y, 0], [vx(0.5), LINE_TOP, 0], color=INK,
                                 stroke_width=3, dash_length=0.12)
        guess_lbl = text("the obvious guess", size=26).move_to([0, LBL_Y, 0])
        guess_lbl.align_to([vx(0.5) + 0.16, 0, 0], LEFT)
        per_flip = MathTex(r"\text{every flip: }", r"1/2", r"\text{ heads}", font_size=38,
                           color=TGRAY).next_to(big, DOWN, buff=0.42)
        quote = text("“a powerful and widely shared cognitive illusion”", size=30,
                     slant=ITALIC).move_to([BIG_C[0] + 0.3, 3.2, 0])
        cite_gvt = citation("Gilovich et al., 1985 · Cognitive Psychology", color=TGRAY)
        words = VGroup(*[text("hit" if f == "H" else "miss", size=28,
                              color=YELLOW if f == "H" else TGRAY, weight=BOLD).move_to(c)
                         for f, c in zip("HHTH", big)])
        letters = VGroup(*[c[1].copy() for c in big])
        # the axis title follows the coins: flips/heads <-> shots/hits
        t_heads = self.axis_title("checked flips that are heads")
        t_hits = self.axis_title("checked shots that are hits")
        with self.beat("stakes") as beat:
            # "One half feels obvious": the "= 1/2" answer becomes the dashed guess
            beat.wait_until("half", offset=-0.25)
            # the answers clear first, then the dashed guess grows up through where they stood
            self.play(hand_off(opts[1], guess_lbl), FadeOut(qmark, shift=0.15 * UP, rate_func=early(0.4)),
                      FadeOut(opts[0], rate_func=early()), FadeOut(opts[2], rate_func=early()),
                      Create(dashed, rate_func=delayed(0.4)), run_time=1.0)
            self.play(FadeIn(per_flip, shift=0.15 * UP), run_time=beat.until("memory"))
            beat.wait_until("nineteen", offset=-0.1)
            self.play(FadeIn(cite_gvt), run_time=0.8)
            # "ran this kind of check": the check is re-run on the row
            beat.wait_until("check", offset=-0.25)
            self.play(arcs.animate(rate_func=there_and_back).set_stroke(width=9),
                      big_rings.animate(rate_func=there_and_back).set_stroke(width=8),
                      FadeOut(per_flip), run_time=0.6)
            # "on basketball shots": heads become hits, tails misses (coins and axis title)
            beat.wait_until("basketball", offset=-0.15)
            anims, tok = self.retitle(self.axis[3], t_hits)
            self.swap_glyphs([c[1] for c in big], list(words), *anims, run_time=0.9)
            self.retitle_done(tok)
            beat.wait_until("illusion", offset=-0.6)
            self.play(FadeIn(quote, shift=0.15 * DOWN), run_time=1.0)

        # ================================================================ 3 the test
        # blue: the test's verdict (ink is reserved for the assumption, the dashed guess)
        hot = VGroup(h_arrow(vx(0.5) + 0.16, vx(0.5) + 1.5, -1.15, color=BLUE),
                     text("hot", size=28, color=BLUE))
        hot[1].next_to(hot[0], RIGHT, buff=0.15)
        with self.beat("test") as beat:
            # "Heads are hits": the hit words answer
            beat.wait_until("Heads", offset=-0.1)
            self.play(LaggedStart(*[pulse(big[i][1], 1.2) for i in (0, 1, 3)], lag_ratio=0.15),
                      run_time=0.8)
            beat.wait_until("hot", offset=-0.3)
            self.play(GrowArrow(hot[0]), FadeIn(hot[1]), FadeOut(quote),
                      run_time=beat.until("usual"))
            # "their usual rate": the one-half line
            self.play(pulse(dashed, 1.06), pulse(guess_lbl, edge=LEFT), run_time=0.9)
            # "a random one should match it": this row's own 1/2 does
            beat.wait_until("match", offset=-0.2)
            self.play(pulse(big_score, 1.15), run_time=0.8)

        # ================================================================ 4 calibrate
        k0 = SEQS.index("HHTH")
        with self.beat("calibrate") as beat:
            self.play(FadeOut(hot), FadeOut(cite_gvt), run_time=1.0)
            beat.wait_until("random", offset=-0.2)
            self.play(LaggedStart(*[pulse(c, 1.1) for c in big], lag_ratio=0.2), run_time=1.0)
            beat.wait_until("fair coin", offset=-0.1)
            anims, tok = self.retitle(self.axis[3], t_heads)
            self.swap_glyphs([c[1] for c in big], list(letters), FadeOut(arcs), *anims,
                             run_time=0.8)
            self.retitle_done(tok)
            beat.wait_until("Four", offset=-0.1)
            tgt = cards[k0]
            self.play(Transform(dashed, dashed_full),
                      ReplacementTransform(big, tgt["coins"]),
                      ReplacementTransform(big_rings, tgt["rings"]),
                      ReplacementTransform(big_score, tgt["score"]),
                      run_time=1.4)
            others = [cards[k]["coins"] for k in range(16) if k != k0]
            self.play(LaggedStart(*[FadeIn(c, shift=0.15 * DOWN) for c in others], lag_ratio=0.12),
                      run_time=beat.remaining(1.5))

        # ================================================================ 5 fail
        k1 = SEQS.index("HHHT")
        c1 = cards[k1]
        focus = box(VGroup(c1["coins"], c1["score"]), color=INK, buff=0.12)
        with self.beat("score") as beat:
            # round 10 (craft fix 5): the box is fully drawn by "row" (0.35 s from "This")
            self.play(Create(focus), run_time=0.35)
            beat.wait_until("checks", offset=-0.1)
            self.play(LaggedStart(*[Create(r) for r in c1["rings"]], lag_ratio=0.3),
                      run_time=beat.until("flips", offset=0.1))
            # "three flips": the three rings answer and their count, 3, is written (nothing
            # flies through the tight row)
            self.play(LaggedStart(*[r.animate(rate_func=there_and_back).set_stroke(width=7)
                                    for r in c1["rings"]], lag_ratio=0.15),
                      FadeIn(c1["score"][1]), FadeIn(c1["score"][2], shift=0.1 * LEFT),
                      run_time=0.6)
            # "two are heads": the two checked heads answer and their count, 2, is written
            heads_chk = VGroup(*[c1["coins"][i] for i in c1["chk"] if c1["seq"][i] == "H"])
            beat.wait_until("two", offset=-0.15)
            self.play(LaggedStart(*[pulse(c, 1.15) for c in heads_chk], lag_ratio=0.2),
                      FadeIn(c1["score"][0], shift=0.1 * LEFT), run_time=0.8)
            self.adopt(c1["rings"], c1["score"])
            # every other row is scored the same way, silently (round 7: the sentence that
            # narrated this cascade is cut; it runs in the pause after "two are heads")
            rest = [k for k in SCORED if k not in (k0, k1)]
            self.play(FadeOut(focus),
                      LaggedStart(*[AnimationGroup(Create(cards[k]["rings"]),
                                                   FadeIn(cards[k]["score"], shift=0.1 * LEFT))
                                    for k in rest], lag_ratio=0.18),
                      run_time=beat.remaining(1.5))

        undef_boxes = VGroup(*[box(cards[k]["coins"], color=INK, buff=0.1) for k in UNDEF])
        with self.beat("undefined") as beat:
            beat.wait_until("Two", offset=-0.1)
            self.play(Create(undef_boxes), run_time=0.8)
            beat.wait_until("last", offset=-0.2)
            self.play(LaggedStart(*[pulse(cards[k]["coins"][3], 1.2) for k in UNDEF],
                                  lag_ratio=0.2), run_time=0.9)
            self.play(FadeOut(undef_boxes),
                      *[cards[k]["coins"].animate.fade(0.7) for k in UNDEF],
                      *[FadeIn(cards[k]["score"]) for k in UNDEF],
                      run_time=beat.remaining(0.8))

        # dots: each scored row's score shrinks to a dot in place, then the dot falls
        stacks: dict[float, int] = {}
        dots = []
        for k in SCORED:
            v = INFO[SEQS[k]]["h"] / INFO[SEQS[k]]["n"]
            key = round(v, 6)
            j = stacks.get(key, 0)
            stacks[key] = j + 1
            dots.append(Dot([vx(v), AX_Y + 0.13 + 0.2 * j, 0], radius=0.085, color=BLUE))
        dots = VGroup(*dots)
        seeds = VGroup(*[Dot(cards[k]["score"].get_right() + RIGHT * 0.2, radius=0.085,
                             color=BLUE) for k in SCORED])
        for sd in seeds:
            self.allow_overlap(sd, reason="for 0.5 s each score shrinks into its own dot, in "
                                          "place, before the dot falls to the line")
        m = ValueTracker(0.5)
        mtop = ValueTracker(LINE_TOP)       # the row-average marker's top (shortened later)
        blue_line = always_redraw(lambda: Line([vx(m.get_value()), AX_Y, 0],
                                               [vx(m.get_value()), mtop.get_value(), 0],
                                               color=BLUE, stroke_width=5))
        mean_num = DecimalNumber(50.0, num_decimal_places=1, unit=r"\%", font_size=40,
                                 color=BLUE)
        mean_num.add_updater(lambda d: d.set_value(100 * m.get_value()).move_to(
            [vx(m.get_value()) - 0.2 - d.width / 2, LBL_Y, 0]))
        # the average as the fraction the narration speaks, left of its readout
        frac_lbl = MathTex(r"17/42", "=", font_size=36, color=BLUE)
        with self.beat("average") as beat:
            beat.wait_until("Drop", offset=-0.1)
            shrink = [cards[k]["score"].copy() for k in SCORED]
            self.add(*shrink)
            self.play(LaggedStart(*[AnimationGroup(s_.animate.move_to(d_).scale(0.15)
                                                   .set_opacity(0), GrowFromCenter(d_))
                                    for s_, d_ in zip(shrink, seeds)], lag_ratio=0.04),
                      run_time=0.6)
            self.remove(*shrink)
            # round 8: each dot runs down the channel beside its card and out under the table
            # before it drops to its place, so no dot passes over a coin (as the 24 flips do at
            # 1:06); the one dot that lands under "the obvious guess" goes round its right end
            gl_l, gl_r, gl_b = guess_lbl.get_left()[0], guess_lbl.get_right()[0], \
                guess_lbl.get_bottom()[1]
            falls = []
            for d_, t_ in zip(seeds, dots):
                (xs_, ys_, _), (xt_, yt_, _) = d_.get_center(), t_.get_center()
                pts = [(xs_, ys_, 0), (xs_, DOT_CORR, 0)]
                if gl_l - 0.1 < xt_ < gl_r + 0.2:          # its dot would cross the label
                    pts += [(gl_r + 0.3, DOT_CORR, 0), (gl_r + 0.3, gl_b - 0.3, 0),
                            (xt_, gl_b - 0.3, 0)]
                else:
                    pts += [(xt_, DOT_CORR, 0)]
                pts += [(xt_, yt_, 0)]
                f_ = route(pts, r=0.15)
                falls.append(UpdateFromAlphaFunc(
                    d_, lambda m_, a_, f_=f_: m_.move_to(f_(smooth(a_))), rate_func=linear))
            self.play(LaggedStart(*falls, lag_ratio=0.05),
                      run_time=beat.until("Their", offset=-0.1))
            self.remove(*seeds)
            self.add(dots)
            mean_num.update()
            self.add(blue_line)
            self.play(FadeIn(mean_num), run_time=0.4)
            # the marker settles as "seventeen" is spoken, and the fraction is written beside
            # its readout ("17/42 = 40.5%"), so the spoken number is on screen (round 7)
            self.play(m.animate.set_value(MEAN), run_time=beat.until("seventeen", offset=0.2),
                      rate_func=smooth)
            frac_lbl.next_to(mean_num, LEFT, buff=0.16)
            frac_lbl.shift(UP * (mean_num[0].get_bottom()[1] - frac_lbl[0][0].get_bottom()[1]))
            self.play(Write(frac_lbl), run_time=0.8)

        GAP_Y = -1.0
        gap_arrow = h_arrow(vx(0.5) - 0.2, vx(MEAN) + 0.06, GAP_Y, color=RED, width=5)
        cold_w = text("cold", size=28, color=RED)
        cold_n = MathTex(r"-9.5\text{ points}", font_size=36, color=RED)
        cold_lbl = VGroup(cold_w, cold_n).arrange(RIGHT, buff=0.2)
        cold_lbl.move_to([vx(MEAN) - 0.25 - cold_lbl.width / 2, GAP_Y, 0])
        with self.beat("cold") as beat:
            beat.wait_until("fair", offset=-0.2)
            self.play(pulse(dashed, 1.06), pulse(guess_lbl, edge=LEFT), run_time=0.9)
            beat.wait_until("cold", offset=-0.3)
            self.play(GrowArrow(gap_arrow), Write(cold_w), run_time=0.8)
            beat.wait_until("nine", offset=-0.2)
            self.play(Write(cold_n), run_time=0.8)

        # ================================================================ 6 insight
        heads_src, tails_src = [], []
        for k in SCORED:
            cd = cards[k]
            for i in cd["chk"]:
                (heads_src if cd["seq"][i] == "H" else tails_src).append(cd["coins"][i])
        a_tiles = VGroup(*[tile("H", W / 24 - 0.05, X0 + (j + 0.5) * W / 24, SA_Y)
                           for j in range(12)],
                         *[tile("T", W / 24 - 0.05, X0 + (j + 12.5) * W / 24, SA_Y)
                           for j in range(12)])
        a_yellow, a_gray = a_tiles[:12], a_tiles[12:]
        scrim = allow_overlap(Rectangle(width=13.4, height=3.0, stroke_width=0, fill_color=BG,
                                        fill_opacity=0.62).move_to([0, 2.0, 0]).set_z_index(5))
        # the formula pair, set alike (displaystyle, one size) with the "=" signs on one
        # vertical: the average of ratios (the test) under the ratio of totals (pooled)
        fb = MathTex(r"\displaystyle\frac{1}{14}", r"\displaystyle\sum_i",
                     r"\displaystyle\frac{h_i}{n_i}", "=", r"\displaystyle\frac{17}{42}",
                     font_size=40)
        fb.move_to([FORM_X + fb.width / 2, FB_Y, 0])
        fa = MathTex(r"\displaystyle\frac{\sum_i h_i}{\sum_i n_i}", "=",
                     r"\displaystyle\frac{12}{24}", font_size=40)
        fa.move_to([0, FA_Y, 0])
        fa.shift(RIGHT * (fb[3].get_center()[0] - fa[1].get_center()[0]))
        fa_num, fa_bar, fa_den = fa[0][0:4], fa[0][4], fa[0][5:9]
        fa_num.set_color(YELLOW)
        fa_den.set_color(BLUE)
        fa[2][0:2].set_color(YELLOW)
        fa[2][3:5].set_color(BLUE)
        fa[2][2].set_color(TGRAY)
        fb[0].set_color(INK)
        fb[2][0:2].set_color(YELLOW)
        fb[2][3:5].set_color(BLUE)
        fb[4].set_color(BLUE)
        for f_ in (fa, fb):
            f_.set_stroke(width=0)
        nums = [cards[k]["score"][0] for k in SCORED]
        dens = [cards[k]["score"][2] for k in SCORED]
        axis_group = VGroup(self.axis, dashed, guess_lbl, dots, gap_arrow, cold_lbl)
        with self.beat("pool") as beat:
            # make room for the right column: the line and everything on it slides left; the
            # row-average marker shrinks to the vote lane (below the pooled strip to come), so
            # the pooled strip is read only against the dashed one-half line
            self.play(OFF.animate.set_value(0.0), axis_group.animate.shift(LEFT * SHIFT1),
                      frac_lbl.animate.shift(LEFT * SHIFT1),
                      mtop.animate.set_value(SB_Y + TILE_H / 2 + 0.15),
                      run_time=beat.until("Gather", offset=-0.2))
            # each ringed coin's flip becomes a tile (the letters stay in the table). Round 9
            # (craft fix 3): one card column at a time, the others stepped back to 30%; each
            # flip's disc appears in the gap just under its own coin, runs along that gap to the
            # nearer channel beside its card, down it and along the corridor into a block of the
            # strip right under its column (no disc passes over a coin; at most 8 in flight)
            plan, t_pour = pour_plan(SEQS, INFO, lambda j: X0 + (j + 0.5) * W / 24)
            p_tiles = VGroup(*[tile(d["face"], W / 24 - 0.05, X0 + (d["block"] + 0.5) * W / 24,
                                    SA_Y) for d in plan])
            p_base = p_tiles.copy()
            p_ops = [0.9 if d["face"] == "H" else 0.45 for d in plan]
            discs = VGroup(*[Circle(radius=0.07, stroke_width=0, fill_color=t_.get_fill_color(),
                                    fill_opacity=0.0).move_to(d["pts"][0])
                             for d, t_ in zip(plan, p_tiles)])
            card_g = [VGroup(cd["coins"], cd["rings"], cd["score"]) for cd in cards]
            card_saved = [g_.copy() for g_ in card_g]
            spans = [(min(d["offset"] for d in plan if d["c"] in gc),
                      max(d["offset"] for d in plan if d["c"] in gc) + POUR_D)
                     for gc in POUR_GROUPS]
            grp_of = {c: g for g, gc in enumerate(POUR_GROUPS) for c in gc}

            def level(g: int, t: float) -> float:
                s0, s1 = spans[g]
                on = smooth(ramp(t, s0 - 0.2, s0 + 1e-3))
                if g < len(spans) - 1:
                    on *= 1.0 - smooth(ramp(t, s1 - 0.2, s1))
                start = 1.0 - smooth(ramp(t, 0.0, 0.25))     # all full at the start
                end = smooth(ramp(t, t_pour - 0.3, t_pour))   # and again at the end
                return 0.3 + 0.7 * max(on, start, end)

            for t_ in p_tiles:
                t_.set_fill(opacity=0)
            self.add(p_tiles, discs)

            def pour_step(_grp, a):
                t = a * t_pour
                for d, disc, tl, base, op in zip(plan, discs, p_tiles, p_base, p_ops):
                    u = (t - d["offset"]) / POUR_D
                    disc.move_to(d["route"](ease_sine(u)))
                    disc.set_fill(opacity=op * ramp(u, 0.0, 0.12) * (1.0 - ramp(u, 0.9, 1.0)))
                    k_ = smooth(ramp(u, 0.86, 1.0))
                    tl.become(base).scale(0.3 + 0.7 * k_).set_fill(opacity=op * k_)
                for k_, (g_, sv) in enumerate(zip(card_g, card_saved)):
                    lv = level(grp_of[k_ % 4], t)
                    g_.become(sv)
                    if lv < 0.999:
                        g_.fade(1.0 - lv)

            beat.wait_until("Gather", offset=-0.2)
            pour_rig = VGroup(discs, p_tiles, *card_g)
            self.play(FadeOut(dots, rate_func=early(0.25)), FadeOut(gap_arrow, rate_func=early(0.25)),
                      FadeOut(cold_lbl, rate_func=early(0.25)),
                      FadeOut(frac_lbl, rate_func=early(0.25)),
                      UpdateFromAlphaFunc(pour_rig, pour_step, rate_func=linear), run_time=t_pour)
            # (removing pour_rig itself would take the cards with it: adding it to the scene
            # moved their families under it)
            self.remove(discs)
            self.add(p_tiles)
            # the poured strip sorts: heads slide left along the strip's upper half, tails right
            # along its lower half (each keeps its order, so no two tiles cross), and the boundary
            # lands on the dashed one-half line
            ys = sorted([j for j, d in enumerate(plan) if d["face"] == "H"],
                        key=lambda j: p_tiles[j].get_x())
            ts_ = sorted([j for j, d in enumerate(plan) if d["face"] == "T"],
                         key=lambda j: p_tiles[j].get_x())
            sort_to = {}
            for q, j in enumerate(ys):
                sort_to[j] = a_yellow[q].get_x()
            for q, j in enumerate(ts_):
                sort_to[j] = a_gray[q].get_x()
            sort_from = {j: p_tiles[j].get_x() for j in range(24)}

            def sort_step(_grp, a):
                sq = smooth(ramp(a, 0.0, 0.25)) * (1.0 - smooth(ramp(a, 0.75, 1.0)))
                sx = smooth(ramp(a, 0.2, 0.8))
                for j, (tl, d) in enumerate(zip(p_tiles, plan)):
                    h = TILE_H * (1.0 - 0.55 * sq)
                    dy = (1 if d["face"] == "H" else -1) * (TILE_H - h) / 2
                    tl.become(Rectangle(width=W / 24 - 0.05, height=h, stroke_width=0,
                                        fill_color=YELLOW if d["face"] == "H" else GRAY,
                                        fill_opacity=p_ops[j]).move_to(
                        [sort_from[j] + (sort_to[j] - sort_from[j]) * sx, SA_Y + dy, 0]))

            self.play(UpdateFromAlphaFunc(p_tiles, sort_step, rate_func=linear),
                      run_time=max(0.6, beat.until("twelve", offset=-0.15)))
            self.remove(p_tiles)
            self.add(a_tiles)
            # round 10 (both critics' 12/24 fix): no inline "12/24" that restacks (its slash
            # tumbled across "12"). The yellow tiles fly straight into the stacked numerator,
            # all 24 into the denominator, and the bar grows between them, in the place where
            # the pooled formula will stand
            num12, bar12, den24 = fa[2][0:2], fa[2][2], fa[2][3:5]
            self.play(self.fly_into(a_yellow, num12), FadeIn(scrim), run_time=0.8)
            self.clean_fly()
            beat.wait_until("twelve", 2, offset=-0.1)
            self.play(self.fly_into(a_tiles, den24, lag=0.01),
                      GrowFromCenter(bar12, rate_func=delayed(0.3)), run_time=0.8)
            self.clean_fly()
            # "Total heads over total flips": every row's heads count answers in the table
            # while the sum over rows is written (in place: 14 digits flying across the table
            # read as debris), then every row's checked count while the denominator's sum is
            # written
            beat.wait_until("Total", offset=-0.2)
            self.play(FadeOut(scrim, rate_func=early(0.6)),
                      LaggedStart(*[pulse(n_, 1.3, edge=RIGHT) for n_ in nums], lag_ratio=0.03),
                      FadeIn(fa_num, shift=0.1 * DOWN), run_time=0.7)
            beat.wait_until("flips", 2, offset=-0.3)
            self.play(LaggedStart(*[pulse(d_, 1.3, edge=LEFT) for d_ in dens], lag_ratio=0.03),
                      FadeIn(fa_den, shift=0.1 * UP), FadeIn(fa_bar), run_time=0.7)
            # "exactly half": only now, with both sides complete, the "="
            beat.wait_until("exactly", offset=-0.15)
            self.play(FadeIn(fa[1]), run_time=0.4)
            self.adopt(fa)
            self.play(pulse(dashed, 1.06), pulse(guess_lbl, edge=LEFT), pulse(fa[2], 1.12),
                      run_time=0.9)

        # strip B: same tiles, regrouped by row, then one vote per row
        rows_b = []
        used_h, used_t = 0, 0
        cum = 0
        for r_i, k in enumerate(SCORED):
            cd = cards[k]
            n = cd["n"]
            row_tiles = []
            for j, i in enumerate(cd["chk"]):
                face = cd["seq"][i]
                if face == "H":
                    src = a_yellow[used_h]
                    used_h += 1
                else:
                    src = a_gray[used_t]
                    used_t += 1
                t_reg = tile(face, W / 24 - 0.05, X0 + (cum + j + 0.5) * W / 24, SB_Y)
                vw = W / 14 / n
                t_vote = tile(face, vw - 0.05, X0 + r_i * W / 14 + (j + 0.5) * vw, SB_Y)
                row_tiles.append((face, src, t_reg, t_vote))
            cum += n
            rows_b.append(row_tiles)
        b_tiles = VGroup(*[t[2].copy() for row in rows_b for t in row])
        b_vote_targets = VGroup(*[t[3] for row in rows_b for t in row])

        def vote_outlines(y=SB_Y, width=1.6):
            return VGroup(*[Rectangle(width=W / 14, height=TILE_H + 0.14, stroke_color=INK,
                                      stroke_width=width, fill_opacity=0)
                            .move_to([X0 + (r_i + 0.5) * W / 14, y, 0]) for r_i in range(14)])

        vote_boxes = vote_outlines()
        denoms = VGroup(*[cards[k]["score"][2] for k in SCORED])
        # every table row as one group, saved at full strength: from "each row gets one vote"
        # on, the table steps back to 30% and a row comes back only while it is named (round 7)
        rowg = {k: VGroup(cards[k]["coins"], cards[k]["rings"], cards[k]["score"])
                for k in range(16)}
        for k in range(16):
            rowg[k].save_state()
        row_lvl = {k: 1.0 for k in range(16)}

        def rows_to(levels: dict) -> list:
            """Animations taking each row k to `levels[k]` of its full strength (from the saved
            full state, so levels never compound)."""
            anims = []
            for k, f in levels.items():
                if abs(row_lvl[k] - f) < 1e-6:
                    continue
                tgt = rowg[k].saved_state.copy()
                if k in UNDEF:
                    tgt[2].fade(1.0 - f)          # its coins already sit at 30%
                elif f < 1.0:
                    tgt.fade(1.0 - f)
                anims.append(Transform(rowg[k], tgt))
                row_lvl[k] = f
            return anims

        a_tiles.save_state()
        # round 8 (substance fix 4): the vote strip is named on screen, above its left end
        vote_tag = text("1 vote per row", size=26, color=TGRAY)
        # round 10 (craft fix 7): the stepped-back readout sits higher (below), so the two
        # never share a baseline (the tag cannot go lower: it keeps 0.15 to the vote outlines)
        vote_tag.move_to([X0 - 0.1 + vote_tag.width / 2, LBL_Y, 0])
        with self.beat("votes") as beat:
            mean_num.clear_updaters()            # the line has stopped moving: the label rests
            srcs = [t[1] for row in rows_b for t in row]
            # "But each row": the tiles regroup row by row, dropping past the two labels between
            # the strips, which step back meanwhile (round 8: "scoring row by row" is cut)
            # round 9 (craft fix 4): the stepped-back readout moves to sit right over its
            # marker's top, so "1 vote per row" (left end) never reads into "40.5%"
            rd_at = [vx(MEAN), mtop.get_value() + 0.28 + mean_num.height / 2, 0]
            self.play(LaggedStart(*[TransformFromCopy(s_, t_) for s_, t_ in zip(srcs, b_tiles)],
                                  lag_ratio=0.03),
                      mean_num.animate(rate_func=early(0.3)).set_opacity(0.25).move_to(rd_at),
                      guess_lbl.animate(rate_func=early(0.3)).set_opacity(0.3),
                      run_time=beat.until("vote", offset=-0.05))
            # "one vote": the vote strip is the one subject; the table, the pooled strip and its
            # formula step back to 30% until each is named again
            self.play(Transform(b_tiles, b_vote_targets), Create(vote_boxes),
                      *rows_to({k: 0.3 for k in range(16)}), a_tiles.animate.fade(0.7),
                      fa.animate.set_opacity(0.3),
                      FadeIn(vote_tag, shift=0.1 * DOWN, rate_func=delayed(0.3)),
                      run_time=beat.until("however", offset=-0.1))
            # "however many flips it checked": every row's checked count answers in the table
            self.play(LaggedStart(*[d.animate(rate_func=there_and_back).scale(1.3)
                                    .set_opacity(1.0) for d in denoms], lag_ratio=0.06),
                      run_time=beat.remaining(1.0))

        # crowds: HHHH's three heads share one vote; HTTT's lone tails keeps a whole one
        kA, kB = SEQS.index("HHHH"), SEQS.index("HTTT")
        rA, rB = SCORED.index(kA), SCORED.index(kB)
        cA = cards[kA]
        chain = VGroup(*[CurvedArrow(cA["coins"][i].get_top() + UP * 0.07,
                                     cA["coins"][i + 1].get_top() + UP * 0.07, angle=-PI / 2,
                                     color=BLUE, stroke_width=3, tip_length=0.12)
                         for i in range(3)])
        # round 7: the boxes take the blue rings in and keep 0.13 clear of them (was ~2 px)
        boxA = box(VGroup(cA["coins"], cA["rings"], cA["score"], chain), color=INK, buff=0.13)
        boxB = box(VGroup(cards[kB]["coins"], cards[kB]["rings"], cards[kB]["score"]),
                   color=INK, buff=0.13)
        segA = vote_boxes[rA].copy().set_stroke(INK, 5)
        segB = vote_boxes[rB].copy().set_stroke(INK, 5)
        # where the heads and the tails live (shown silently right after "a whole one")
        h_rows = [k for k in SCORED if INFO[SEQS[k]]["h"] > 0]
        t_rows = [k for k in SCORED if INFO[SEQS[k]]["n"] - INFO[SEQS[k]]["h"] > 0]
        assert len(h_rows) == 8 and len(t_rows) == 11
        no_h = [k for k in SCORED if k not in h_rows]        # 6 rows: no checked heads
        no_t = [k for k in SCORED if k not in t_rows]        # 3 rows: no checked tails
        h_boxes = VGroup(*[box(cards[k]["coins"], color=YELLOW, buff=0.12, stroke_width=4.5)
                           for k in h_rows])
        t_boxes = VGroup(*[box(cards[k]["coins"], color=INK, buff=0.12, stroke_width=3)
                           for k in t_rows])
        cnt_h = text("12 heads · 8 rows", size=26, color=YELLOW)
        cnt_h.move_to([RC_X + cnt_h.width / 2, CNT_Y1, 0])
        cnt_t = text("12 tails · 11 rows", size=26, color=TGRAY)
        cnt_t.move_to([RC_X + cnt_t.width / 2, CNT_Y2, 0])
        with self.beat("crowds") as beat:
            beat.wait_until("crowds", offset=-0.3)
            crowd_rows = [r_i for r_i, row in enumerate(rows_b)
                          if sum(1 for t in row if t[0] == "H") >= 2]
            crowd_tiles = [b_tiles[sum(len(rows_b[q]) for q in range(r_i)) + j]
                           for r_i in crowd_rows for j, t in enumerate(rows_b[r_i])
                           if t[0] == "H"]
            self.play(LaggedStart(*[pulse(t, 1.2) for t in crowd_tiles], lag_ratio=0.08),
                      run_time=1.0)
            # "since a heads gets the next flip checked too": HHHH, named, comes back to full
            beat.wait_until("since", offset=-0.25)
            self.play(*rows_to({kA: 1.0}), run_time=0.5)
            self.play(LaggedStart(*[Create(a) for a in chain], lag_ratio=0.6),
                      run_time=beat.until("Here", offset=-0.2))
            self.play(Create(boxA), Create(segA), run_time=0.8)
            beat.wait_until("single", offset=-0.1)
            self.play(pulse(VGroup(*[b_tiles[j] for j in range(3)]), 1.15), run_time=0.8)
            # "this lone tails": HHHH steps back, HTTT comes forward
            beat.wait_until("lone", offset=-0.35)
            self.play(FadeOut(boxA), FadeOut(segA), FadeOut(chain),
                      *rows_to({kA: 0.3, kB: 1.0}), Create(boxB), Create(segB), run_time=0.8)
            beat.wait_until("whole", offset=-0.1)
            idxB = sum(len(rows_b[q]) for q in range(rB))
            self.play(pulse(b_tiles[idxB], 1.15), run_time=0.6)
            # round 9 (substance fix 1): the spoken count ("Twelve heads crowd into eight rows.
            # Twelve tails spread across eleven.") is cut; as "a whole one" ends, the picture
            # alone shows where the heads live (8 rows, held 1 s), then where the tails live
            # (11 rows, held through "Line them up:"); both counts stay until "five"
            self.play(FadeOut(boxB), FadeOut(segB),
                      LaggedStart(*[Create(b) for b in h_boxes], lag_ratio=0.1),
                      FadeIn(cnt_h, shift=0.1 * LEFT, rate_func=delayed(0.3)),
                      *rows_to({kB: 0.3, **{k: 1.0 for k in h_rows}}), run_time=0.55)

        # lineup: where the heads and the tails live; then pack the votes and count them
        flat = [t for row in rows_b for t in row]
        widths = [W / 14 / len(row) for row in rows_b for _ in row]
        order = [i for i, t in enumerate(flat) if t[0] == "H"] + \
                [i for i, t in enumerate(flat) if t[0] == "T"]
        x = X0
        sorted_targets = [None] * len(flat)
        for i in order:
            sorted_targets[i] = tile(flat[i][0], widths[i] - 0.05, x + widths[i] / 2, SB_Y)
            x += widths[i]
        # the thinnest heads slices: HHHH's three and HHHT's two, a third of a vote each
        thin = [b_tiles[i] for i, t in enumerate(flat) if t[0] == "H" and widths[i] < W / 35]
        assert len(thin) == 5
        table = VGroup(*[VGroup(cd["coins"], cd["rings"], cd["score"]) for cd in cards])

        def vote_lbl(tex: str, color) -> VGroup:
            g = VGroup(MathTex(tex, font_size=36, color=color), text("votes", size=26, color=color))
            g.arrange(RIGHT, buff=0.14)
            g[1].align_to(g[0][0][0], DOWN)                  # "votes" on the 5's baseline
            return g

        # the votes held, written over the packed strip: heads 5 2/3, tails 8 1/3 (of 14)
        vh_lbl = vote_lbl(r"5\tfrac{2}{3}", YELLOW).move_to([X0 + W * MEAN / 2, VLBL_Y, 0])
        vt_lbl = vote_lbl(r"8\tfrac{1}{3}", TGRAY).move_to([(C + X1) / 2, VLBL_Y, 0])
        # 5 2/3 out of 14, set where the test's formula will stand (left of its "=")
        f_num = MathTex(r"5\tfrac{2}{3}", font_size=40, color=YELLOW)
        f_den = MathTex("14", font_size=40, color=INK)
        f_bar = Line(LEFT, RIGHT, color=TGRAY, stroke_width=2.5).set_width(
            max(f_num.width, f_den.width) + 0.12)
        frac57 = VGroup(f_num, f_bar, f_den).arrange(DOWN, buff=0.1)
        frac57.move_to([fb[3].get_left()[0] - 0.2 - frac57.width / 2, 0, 0])
        frac57.shift(UP * (fb[3].get_center()[1] - f_bar.get_center()[1]))
        self.hold(1.0)
        self.play(FadeOut(h_boxes),
                  *rows_to({**{k: 0.3 for k in no_t}, **{k: 1.0 for k in no_h}}),
                  LaggedStart(*[Create(b) for b in t_boxes], lag_ratio=0.08),
                  FadeIn(cnt_t, shift=0.1 * LEFT, rate_func=delayed(0.35)), run_time=0.5)

        with self.beat("pack") as beat:
            # "Line them up:" (the tails rows stay boxed while it is said) then the table steps
            # back and the tails rows' boxes clear; the votes
            # pack, heads first, and stop on the 40.5% marker, whose readout comes forward as
            # they arrive. The 14 vote outlines stay, so the heads' part can be counted in votes.
            # (the strip's name steps out as the marker's readout steps back in over it)
            beat.wait_until("up", offset=0.3)          # as "up:" ends
            self.play(FadeOut(t_boxes, rate_func=early(0.5)), FadeOut(guess_lbl),
                      *rows_to({k: 0.3 for k in SCORED}),
                      *[Transform(b_tiles[i], sorted_targets[i]) for i in range(len(flat))],
                      FadeOut(vote_tag, rate_func=early(0.4)),
                      mean_num.animate(rate_func=delayed(0.4)).set_opacity(1.0),
                      run_time=beat.until("heads", offset=-0.1))
            # "five and two thirds": counted on the strip, then carried into a numerator
            # (routed above the strip and clear of the grey count still to come);
            # the marker's readout hands over to the vote count; the row counts leave the
            # right column before the numerator arrives there
            beat.wait_until("five", offset=-0.5)
            self.play(FadeOut(mean_num, rate_func=early(0.45)), FadeOut(cnt_h), FadeOut(cnt_t),
                      FadeIn(vh_lbl, shift=0.1 * DOWN, rate_func=delayed(0.4)), run_time=0.7)
            self.play(emerge(vh_lbl[0], f_num, run_time=0.9,
                             path=via((0.0, -0.05, 0), (4.0, -0.15, 0))))
            # "of the fourteen votes": the tails' 8 1/3; the 14 outlines are counted in place
            # (each answers in turn) while their count, 14, is written (round 7: the copies
            # that flew out of them showed doubled boxes)
            beat.wait_until("fourteen", offset=-0.15)
            self.play(FadeIn(vt_lbl, shift=0.1 * DOWN),
                      LaggedStart(*[o.animate(rate_func=there_and_back).set_stroke(width=5)
                                    for o in vote_boxes], lag_ratio=0.06),
                      FadeIn(f_den, shift=0.1 * UP, rate_func=delayed(0.45)),
                      FadeIn(f_bar, rate_func=delayed(0.35)), run_time=1.0)
            self.adopt(frac57)
            # "That's seventeen out of forty two": 5 2/3 over 14 is 17/42
            # (no copy flies: a cross-fade of 5 2/3 over 14 into 17/42 read as glyph soup)
            beat.wait_until("That's", offset=-0.05)
            self.play(FadeIn(fb[3], shift=0.15 * RIGHT, rate_func=early(0.5)),
                      FadeIn(fb[4], shift=0.3 * RIGHT, rate_func=delayed(0.3)), run_time=0.7)
            t_frac57 = self.time

        with self.beat("formula") as beat:
            # 5 2/3 / 14 = 17/42 is held complete >= 3.2 s (BAR: 2 s + 0.4 s per term), then the
            # worked case steps aside for the general form (no "=" while a side is open)
            beat.wait_until("the", offset=0.0)
            if self.time - t_frac57 < 3.25:
                self.hold(3.25 - (self.time - t_frac57))
            self.play(FadeOut(frac57), FadeOut(fb[3]), FadeOut(vh_lbl), FadeOut(vt_lbl),
                      run_time=0.4)
            # "an average": the 14 equal vote outlines themselves (no copies, so nothing is seen
            # doubled) lift off the strip at 40%, run right between the two strips, and become
            # the 1/14 and the sum (the 1/14 lands on "average"); the right-most leaves first,
            # so no outline in flight crosses one still waiting on the strip
            e0 = fb[0].get_center()
            self.play(LaggedStart(*[self.depart(o, e0, [(o.get_x(), -0.1, 0), (e0[0] - 0.6, -0.1, 0)],
                                                scale_to=0.3, mid=0.4)
                                    for o in reversed(vote_boxes)], lag_ratio=0.08),
                      FadeIn(fb[0], rate_func=delayed(0.6)), FadeIn(fb[1], rate_func=delayed(0.65)),
                      run_time=1.0)
            self.remove(vote_boxes, *vote_boxes)
            # "of ratios": every row's own ratio answers in the table (in place, at full
            # strength, one after another) while h_i / n_i is written in the sum (round 7: the
            # copy of HHHH's 3/3 that flew there was first seen doubled over its source)
            beat.wait_until("ratios", offset=-0.1)
            self.play(LaggedStart(*[cards[k]["score"].animate(rate_func=there_and_back)
                                    .scale(1.15).set_opacity(1.0) for k in SCORED],
                                  lag_ratio=0.05),
                      FadeIn(fb[2], shift=0.1 * UP, rate_func=delayed(0.35)), run_time=1.0)
            # "one per row": the "=" joins 17/42
            beat.wait_until("one per row", offset=-0.15)
            self.play(FadeIn(fb[3]), pulse(fb[4], 1.12), run_time=0.7)
            self.adopt(fb)
            # "instead": the sum outside the ratio; "the ratio of totals": the pooled strip and
            # its formula, dimmed since "each row gets one vote", come back to full, and the
            # sums inside that ratio answer (each pulse grows away from its neighbours)
            beat.wait_until("instead", offset=-0.15)
            self.play(pulse(VGroup(fb[0], fb[1]), 1.18, edge=RIGHT), run_time=0.6)
            beat.wait_until("ratio", 2, offset=-0.15)
            self.play(fa.animate.set_opacity(1.0), Restore(a_tiles), run_time=0.6)
            self.play(pulse(fa[0][0], 1.25, edge=DR), pulse(fa[0][5], 1.25, edge=UR),
                      run_time=0.8)
            # the table has done its job
            self.play(FadeOut(table), run_time=beat.remaining(0.6))

        # ================================================================ 7 the mirror
        # two lanes: after heads (top: the vote strip moves up) and after tails (bottom)
        sH, sT, Z = ValueTracker(MEAN), ValueTracker(MEAN_T), ValueTracker(X1 - X0)

        def xs(s: float) -> float:
            return C + (s - 0.5) * Z.get_value()

        cur_H = always_redraw(lambda: Line([xs(sH.get_value()), CUR_TOP, 0],
                                           [xs(sH.get_value()), LBL2, 0], color=BLUE,
                                           stroke_width=5))
        cur_T = always_redraw(lambda: Line([xs(sT.get_value()), CUR_BOT, 0],
                                           [xs(sT.get_value()), LBL2, 0], color=BLUE,
                                           stroke_width=5))
        lab_H = lane_label("heads")
        lab_H.move_to([RC_X + lab_H.width / 2, SA2 + 0.25, 0])
        lab_T = lane_label("tails")
        lab_T.move_to([RC_X + lab_T.width / 2, SB2 + 0.25, 0])
        val_H = value_tex("17/42")
        val_H.move_to([RC_X + val_H.width / 2, SA2 - 0.2, 0])
        val_T = value_tex("25/42")
        val_T.move_to([RC_X + val_T.width / 2, SB2 - 0.2, 0])
        dashed_m = DashedLine([C, AX2, 0], [C, CUR_TOP, 0], color=INK, stroke_width=3,
                              dash_length=0.12)
        # the after-tails strip is the after-heads strip with heads and tails swapped
        # (recolour), mirrored about one half (flip) so that its heads line up from the left
        swap = {"H": "T", "T": "H"}
        flip_data = [(t.get_center()[0], widths[i] - 0.05, flat[i][0])
                     for i, t in enumerate(sorted_targets)]
        lane_T = VGroup(*[tile(f, w, x0, SA2) for x0, w, f in flip_data])
        lane_T_sw = VGroup(*[tile(swap[f], w, x0, SB2) for x0, w, f in flip_data])

        def flip_step(mob, alpha):
            cth = np.cos(PI * rate_functions.ease_in_out_sine(alpha))
            for t, (x0, w, f) in zip(mob, flip_data):
                t.become(tile(swap[f], max(w * abs(cth), 0.004), C + (x0 - C) * cth, SB2))

        with self.beat("mirror") as beat:
            self.remove(blue_line)
            mean_num.clear_updaters()
            blue_static = Line([vx(MEAN), AX_Y, 0], [vx(MEAN), mtop.get_value(), 0], color=BLUE,
                               stroke_width=5)
            self.add(blue_static)
            # "Now score the flip after each tails": the pooled strip and its formula leave in
            # place (nothing crosses the vote strip); the row-average formula hands its 17/42 to
            # the after-heads lane as the picture rises
            beat.wait_until("score", offset=-0.1)
            self.play(FadeOut(VGroup(a_tiles, fa), shift=UP * 0.3), FadeOut(fb[0:4]),
                      run_time=0.5)
            self.play(b_tiles.animate.shift(UP * (SA2 - SB_Y)),
                      self.axis.animate.shift(UP * DY), Transform(dashed, dashed_m),
                      Transform(blue_static, cur_H.copy().clear_updaters()),
                      hand_off(fb[4], val_H),
                      FadeIn(lab_H, rate_func=delayed(0.6)),
                      run_time=0.9)
            self.remove(blue_static)
            self.add(cur_H)
            # a copy drops into the bottom lane, unchanged
            self.add(lane_T)
            self.play(lane_T.animate.shift(DOWN * (SA2 - SB2)), run_time=0.8)
            # "A fair coin can't tell heads from tails": recolour in place (round 9: the swap is
            # given its reason, the coin's symmetry)
            beat.wait_until("tell", offset=-0.1)
            self.play(*[Transform(a_, b_) for a_, b_ in zip(lane_T, lane_T_sw)],
                      run_time=beat.until("tails", 2, end=True, offset=0.05))
            # "and the strip flips over one half": a half turn about the dashed line
            beat.wait_until("strip", offset=-0.25)
            self.play(UpdateFromAlphaFunc(lane_T, flip_step, rate_func=linear),
                      dashed.animate(rate_func=there_and_back).set_stroke(width=7),
                      run_time=1.6)
            beat.wait_until("test", offset=-0.25)
            self.play(FadeIn(cur_T), FadeIn(lab_T), run_time=0.6)
            # "the test reads high": the after-tails cursor sits right of one half
            beat.wait_until("high", offset=-0.2)
            self.play(pulse(lab_T, 1.1), run_time=0.7)
            # "twenty five out of forty two": the after-tails heads part answers in place (a
            # vertical flash, so it never grows into its cursor) and its value is written
            # beside "after tails" (round 7: no translucent copy crosses the strip)
            beat.wait_until("twenty", offset=-0.2)
            heads_T = VGroup(*[t for t, (_x, _w, f) in zip(lane_T, flip_data) if swap[f] == "H"])
            self.play(heads_T.animate(rate_func=there_and_back, run_time=0.6).stretch(1.35, 1),
                      Write(val_T, run_time=0.8), run_time=0.8)

        gap19 = h_arrow(xs(MEAN_T), xs(MEAN), LBL2, color=RED, width=5)
        lbl19 = MathTex(r"-19\text{ points}", font_size=36, color=RED)
        lbl19.move_to([xs(MEAN_T) + 0.3 + lbl19.width / 2, LBL2, 0])
        with self.beat("gap") as beat:
            beat.wait_until("averages", offset=-0.15)
            self.play(pulse(val_H, 1.15), pulse(val_T, 1.15), run_time=0.8)
            beat.wait_until("gap", offset=-0.3)
            self.play(GrowArrow(gap19), run_time=0.8)
            beat.wait_until("minus", offset=-0.15)
            self.play(Write(lbl19), run_time=0.8)

        # ================================================================ 8 Cornell
        # round 10 (substance fixes 1, 2, 5; craft fix 3): no header sentence. The coin strips
        # themselves shrink into the two lanes ("the same comparison"), and the design is
        # tagged where it belongs: the right column's head names whose lanes these are ("26
        # Cornell players", grey: no data yet), with "up to 100 shots" under it. The head
        # becomes "random" for the random shooter's numbers, then the purple "Cornell" for
        # Cornell's; "up to 100 shots" answers "Longer records" and leaves with the design.
        tracks = VGroup(*[Line([vx(0), y, 0], [vx(1), y, 0], color=DIM, stroke_width=3)
                          for y in (SA2, SB2)])
        gap_live = always_redraw(
            lambda: h_arrow(xs(sT.get_value()), xs(sH.get_value()), LBL2, color=RED, width=5)
            if abs(xs(sT.get_value()) - xs(sH.get_value())) > 0.12 else VMobject())
        t_hits2 = self.axis_title("checked shots that are hits").shift(UP * DY)
        q_H, q_T = value_tex("?"), value_tex("?")
        q_H.move_to(val_H, aligned_edge=LEFT)
        q_T.move_to(val_T, aligned_edge=LEFT)
        # each lane keeps its "after" and changes its condition (heads -> 3 hits, tails ->
        # 3 misses) in place
        lab_H3 = lane_label("3 hits")
        lab_H3.shift(lab_H[0].get_center() - lab_H3[0].get_center())
        lab_T3 = lane_label("3 misses")
        lab_T3.shift(lab_T[0].get_center() - lab_T3[0].get_center())
        lab_H3 = VGroup(lab_H[0], lab_H3[1])
        lab_T3 = VGroup(lab_T[0], lab_T3[1])
        col2 = text("up to 100 shots", size=26, color=TGRAY)
        col2.next_to(lab_H3, UP, buff=0.32, aligned_edge=LEFT)
        col1 = text("26 Cornell players", size=26, color=TGRAY)
        col1.next_to(col2, UP, buff=0.2, aligned_edge=LEFT)
        HEAD_Y = col1.get_center()[1]
        # each lane's condition, drawn at its left end: three hits (yellow dots) / three misses
        # (hollow grey dots)
        g_hits = hit_glyph(3).move_to([X0 + 0.45, SA2 + 0.27, 0])
        g_miss = VGroup(*[Circle(radius=0.065, stroke_color=GRAY, stroke_width=2.5)
                          for _ in range(3)]).arrange(RIGHT, buff=0.07)
        g_miss.move_to([X0 + 0.45, SB2 + 0.27, 0])
        # the one-half line keeps its meaning from the cold open: what the 1985 test assumed a
        # random shooter reads (both cursors sit on it until the crowding pulls them apart)
        obv = text("the obvious guess", size=26).move_to([C, CUR_TOP + 0.38, 0])
        with self.beat("cornell") as beat:
            # "The nineteen eighty five study ran the same comparison": round 10 (substance fix
            # 2) the two coin strips are not cleared; each shrinks into its own lane and steps
            # back to half strength (after heads -> after 3 hits, after tails -> after 3 misses);
            # they are the lanes (the grey tracks replace them only when the random shooter
            # arrives), so the
            # lanes are visibly the same comparison. The lanes and the axis title turn into
            # shots in the same move (round 8). Round 9 (craft fix 2): the two cursors and
            # their gap leave where they stand, so nothing covers the dashed one-half line
            # while the design is described; they grow back out of it on "For a random shooter"
            beat.wait_until("nineteen", offset=-0.2)
            anims, tok = self.retitle(self.axis[3], t_hits2)
            self.play(b_tiles.animate(rate_func=smooth).stretch(0.3, 1).fade(0.5),
                      lane_T.animate(rate_func=smooth).stretch(0.3, 1).fade(0.5),
                      FadeOut(lbl19, rate_func=early(0.5)),
                      FadeOut(gap19, rate_func=early(0.5)), FadeOut(cur_H, rate_func=early(0.5)),
                      FadeOut(cur_T, rate_func=early(0.5)),
                      hand_off(val_H, q_H), hand_off(val_T, q_T),
                      FadeOut(lab_H[1], shift=0.12 * UP, rate_func=early(0.5)),
                      FadeOut(lab_T[1], shift=0.12 * UP, rate_func=early(0.5)),
                      FadeIn(lab_H3[1], shift=0.12 * UP, rate_func=delayed(0.45)),
                      FadeIn(lab_T3[1], shift=0.12 * UP, rate_func=delayed(0.45)), *anims,
                      FadeIn(cite_gvt, rate_func=delayed(0.5)), run_time=1.2)
            self.retitle_done(tok)
            self.remove(*lab_H.get_family(), *lab_T.get_family(), *lab_H3.get_family(),
                        *lab_T3.get_family())
            self.add(lab_H3, lab_T3)
            sH.set_value(0.5)
            sT.set_value(0.5)
            # "the same comparison": each lane gets its condition at its left end
            beat.wait_until("same", offset=-0.1)
            self.play(FadeIn(g_hits, shift=0.1 * RIGHT), FadeIn(g_miss, shift=0.1 * RIGHT),
                      run_time=0.6)
            # "twenty six Cornell players": whose lanes these are, as the column's head;
            # "up to a hundred shots each" under it
            beat.wait_until("twenty six", offset=-0.25)
            self.play(FadeIn(col1, shift=0.1 * DOWN), run_time=0.7)
            beat.wait_until("hundred", offset=-0.25)
            self.play(FadeIn(col2, shift=0.1 * DOWN), run_time=0.7)
            # "from where they'd hit about half": the one-half line and its tick
            # (round 9, craft fix 2: the line itself thickens, 3 -> 8 -> 3, with its tick); the
            # design tags step back, the line is the subject
            beat.wait_until("half", offset=-0.2)
            self.play(dashed.animate(rate_func=there_and_back).set_stroke(width=8),
                      self.axis[1][2].animate(rate_func=there_and_back).set_stroke(width=6)
                      .scale(1.6),
                      pulse(self.axis[2][2], 1.25), FadeIn(obv, shift=0.1 * DOWN),
                      col1.animate.set_opacity(0.3), col2.animate.set_opacity(0.3), run_time=0.8)
            # "After three hits, versus after three misses": each lane gets its condition
            beat.wait_until("After", offset=-0.1)
            self.play(pulse(g_hits, 1.35), pulse(lab_H3, 1.1, edge=LEFT), run_time=0.8)
            beat.wait_until("after", 2, offset=-0.1)
            self.play(pulse(g_miss, 1.35), pulse(lab_T3, 1.1, edge=LEFT), run_time=0.8)

        v46, v54 = value_tex(r"46\%"), value_tex(r"54\%")
        v46.move_to(q_H, aligned_edge=LEFT)
        v54.move_to(q_T, aligned_edge=LEFT)
        cite_ms = citation("Miller & Sanjurjo, 2018 · Econometrica", color=TGRAY)
        cite_ms.shift(UP * (cite_gvt.height + 0.2))
        axis_line = self.axis[0]
        tick_marks, share_nums, ztitle = self.axis[1], self.axis[2], self.axis[3]
        # the difference axis reuses the share axis's tick marks (PT units per point puts
        # -10, -5, 0, +5, +10 exactly on 0, 25, 50, 75, 100 %); only the labels change
        gnums = VGroup(*[MathTex(t, font_size=30, color=TGRAY).move_to(n_)
                         for t, n_ in zip(["-10", "-5", "0", "+5", "+10"], share_nums)])
        assert all(abs(tick_marks[j].get_center()[0] - gx(v)) < 1e-6
                   for j, v in enumerate((-10, -5, 0, 5, 10)))
        line_l, line_r = vx(0) - 0.2, vx(1) + 0.2           # the axis line's ends (OFF = 0)
        # the gap axis title sits at the LEFT end (the share axis title is right-aligned), so
        # the two titles cross-fade without ever sharing a place (round 8: no untitled frame)
        gtitle = MathTex(r"\text{after-hits} - \text{after-misses (points)}", font_size=30,
                         color=TGRAY)
        gtitle.move_to([line_l + gtitle.width / 2, AX2 - 0.82, 0])
        assert gtitle.get_right()[0] < ztitle.get_left()[0] - 0.5
        dashed_g = DashedLine([C, AX2, 0], [C, G_TOP, 0], color=INK, stroke_width=3,
                              dash_length=0.12)
        bias_lbl = text("bias", size=28, color=RED).move_to([(C + gx(-8)) / 2, G_ARR + 0.36, 0])
        rnd_lbl = VGroup(text("random", size=26, color=BLUE), text("shooter", size=26, color=BLUE))
        rnd_lbl.arrange(DOWN, buff=0.1, aligned_edge=RIGHT)
        rnd_lbl.move_to([gx(-8) - 0.2 - rnd_lbl.width / 2, G_ARR + 0.8, 0])
        m8 = MathTex("-8", font_size=40, color=BLUE)
        # the random shooter's marker on the gap axis
        mk8 = Line([gx(-8), AX2, 0], [gx(-8), G_TOP, 0], color=BLUE, stroke_width=5)
        # right column: its head says whose numbers these are (not colour alone)
        head_R = text("random", size=26, color=BLUE)
        head_R.move_to([RC_X + head_R.width / 2, HEAD_Y, 0])
        right_col = VGroup(head_R, lab_H3, lab_T3, v46, v54)
        # record length: one ghost of the -8 marker (GVT's 3-hit case) slides to where a
        # 1,000-shot record would put it
        # round 9 (craft fix 5, substance fix 2): the ghosts are 1.0 tall (2.2x before; any
        # taller and the sliding streak ghost would strike through the red gap and its "bias"
        # label) at 60%; their tags sit at G_TAG, at mid-height, under the gap
        GH, G_OP, G_TAG = 1.0, 0.6, AX2 + 0.5
        ghost = Line([gx(-8), AX2, 0], [gx(-8), AX2 + GH, 0], color=BLUE, stroke_width=5,
                     stroke_opacity=0.0)
        ghost.set_z_index(-1)                        # behind the -8 marker it starts under
        x1000 = gx(STREAK_1000[3])
        long_lbl = text("1,000 shots", size=26, color=BLUE)
        long_lbl.move_to([x1000 - 0.2 - long_lbl.width / 2, G_TAG, 0])
        # streak length (round 8, substance fix 2): a ghost at the one-hit gap (-1.0) grows its
        # streak one hit at a time (yellow dots = hits in a row, as on the lanes) and slides to
        # the 2-hit and 3-hit gaps, exact for 100 shots: -1.01, -3.14, -7.94
        ghost2 = Line([gx(STREAK_100[1]), AX2, 0], [gx(STREAK_100[1]), AX2 + GH, 0],
                      color=BLUE, stroke_width=5, stroke_opacity=0.0).set_z_index(-1)
        SD_R = 0.07
        sdots = VGroup(*[Dot(radius=SD_R, color=YELLOW, fill_opacity=0.0) for _ in range(3)])
        DOT_DX = 2 * SD_R + 0.07

        def streak_stepper(R: float):
            """the streak ghost over R seconds: one dot, a second dot, a >= 1 s slide to the
            two-hit gap, a third dot, a >= 1 s slide to the three-hit gap (under -8)"""
            def step(grp, a):
                t = a * R
                x1, x2, x3 = (gx(STREAK_100[k]) for k in (1, 2, 3))
                x_ = x1 + (x2 - x1) * smooth(ramp(t, 0.6, 1.65)) + \
                    (x3 - x2) * smooth(ramp(t, 1.95, R - 0.05))
                ghost2.become(Line([x_, AX2, 0], [x_, AX2 + GH, 0], color=BLUE, stroke_width=5,
                                   stroke_opacity=G_OP * ramp(t, 0.0, 0.3)))
                ks = (ramp(t, 0.0, 0.3), ramp(t, 0.35, 0.6), ramp(t, 1.7, 1.95))
                for j, (d_, k_) in enumerate(zip(sdots, ks)):
                    d_.become(Dot(radius=SD_R * (0.4 + 0.6 * k_), color=YELLOW, fill_opacity=k_))
                    d_.move_to([x_ - 0.09 - SD_R - DOT_DX * j, G_TAG, 0])
            return step

        def long_step(grp, a):
            """the -8 marker's ghost slides to its 1,000-shot place, its tag riding with it"""
            x_ = gx(-8) + (x1000 - gx(-8)) * smooth(a)
            ghost.become(Line([x_, AX2, 0], [x_, AX2 + GH, 0], color=BLUE, stroke_width=5,
                              stroke_opacity=G_OP * ramp(a, 0.0, 0.2)))
            long_lbl.move_to([x_ - 0.2 - long_lbl.width / 2, G_TAG, 0])
            long_lbl.set_opacity(smooth(ramp(a, 0.55, 0.9)))

        # the x5 zoom about the dashed line (the share axis's 25-point ticks become the gap
        # axis's 5-point ticks): the old ticks run outward and fade, the new ones grow out of
        # the centre and arrive while the old are still there at <= 40% (round 8: the axis is
        # never unlabelled); the gap arrow, already measured from the dashed line, stretches
        # with the zoom to -8
        share_v = [0.0, 0.25, 0.5, 0.75, 1.0]
        gap_p = [-10, -5, 0, 5, 10]
        new_marks = VGroup(*[Line([gx(p), AX2 - 0.08, 0], [gx(p), AX2 + 0.08, 0], color=GRAY,
                                  stroke_width=2.5) for p in gap_p])
        num_y = share_nums[0].get_y()

        def zoom_step(rig, t):
            a = smooth(t)
            zf = 5.0 ** a
            for j, v in enumerate(share_v):
                if j == 2:
                    continue                        # the 50% mark is the centre: it stays
                x_ = C + (v - 0.5) * W * zf
                # round 9 (substance fix 4): the old outer labels and marks are gone in the
                # first 0.4 s, before any new label exists, so no labels pile up mid-zoom
                k = 1.0 - ramp(t, 0.0, 0.12 if j in (0, 4) else 0.22)   # the ends go first
                old_marks[j].move_to([x_, AX2, 0]).set_stroke(opacity=k)
                share_nums[j].move_to([x_, num_y, 0]).set_opacity(k)
            for j, p in enumerate(gap_p):
                if j == 2:
                    continue
                x_ = C + p * (PT / 5.0) * zf
                # the new marks ride out from the centre; their labels fade in only once the
                # marks are >= 1 unit apart (zf >= 2.4), riding with them to the end
                new_marks[j].move_to([x_, AX2, 0]).set_stroke(opacity=ramp(zf, 1.25, 1.8))
                gnums[j].move_to([x_, num_y, 0]).set_opacity(ramp(zf, 2.4, 3.4))
            # 50% -> 0 at the centre: the old label leaves before the new one arrives
            share_nums[2].set_opacity(1.0 - ramp(t, 0.1, 0.24))
            gnums[2].set_opacity(ramp(t, 0.25, 0.4))
            # titles: the share title drifts right and is gone before the gap title arrives at
            # the left end (never two titles at once)
            ztitle.move_to(zt_c + RIGHT * 0.3 * ramp(t, 0.0, 0.22)).set_opacity(
                1.0 - ramp(t, 0.0, 0.22))
            gtitle.move_to(gt_c + LEFT * 0.3 * (1.0 - ramp(t, 0.3, 0.6))).set_opacity(
                ramp(t, 0.3, 0.6))
            # the gap: 8 share points = 0.72 units, x zf; it rises to its place on the gap chart
            xt = C - 8 * (W / 100.0) * zf
            ya = LBL2 + (G_ARR - LBL2) * a
            ga.become(h_arrow(C - 0.03 * a, xt + 0.03 * a, ya, color=RED, width=5))
            m8.move_to([xt - 0.2 - m8.width / 2, ya, 0])

        with self.beat("minus8") as beat:
            # "For a random shooter": the column is labelled before any number lands in it
            # round 9 (craft fix 2): both cursors grow out of the one-half line, where a random
            # shooter is assumed to sit, before the crowding pulls them apart
            beat.wait_until("random", offset=-0.2)
            gH0 = Line([C, CUR_TOP, 0], [C, LBL2, 0], color=BLUE, stroke_width=5)
            gT0 = Line([C, CUR_BOT, 0], [C, LBL2, 0], color=BLUE, stroke_width=5)
            # the column's head now says whose numbers these are; the faint coin strips,
            # done, leave the lanes
            self.play(hand_off(col1, head_R), GrowFromPoint(gH0, [C, LBL2, 0]),
                      GrowFromPoint(gT0, [C, LBL2, 0]), FadeOut(b_tiles), FadeOut(lane_T),
                      FadeIn(tracks), run_time=0.6)
            self.remove(gH0, gT0)
            self.add(cur_H, cur_T, gap_live)
            # (a FadeOut restores its mobject when it is removed, and a frozen wait does not run
            # non-time updaters, so redraw the cursors at 50% now)
            for m_ in (cur_H, cur_T, gap_live):
                m_.update()
            # "the same crowding": this computation is Miller & Sanjurjo's
            beat.wait_until("same crowding", offset=-0.1)
            self.play(FadeIn(cite_ms), run_time=0.6)
            # "pulls after hits down to forty six percent"
            beat.wait_until("pulls", offset=-0.1)
            self.play(sH.animate.set_value(0.46), run_time=beat.until("forty six", offset=-0.15),
                      rate_func=smooth)
            self.play(hand_off(q_H, v46), run_time=0.6)
            # "and after misses up to fifty four"
            beat.wait_until("after", 2, offset=-0.1)
            self.play(sT.animate.set_value(0.54), run_time=beat.until("fifty four", offset=-0.15),
                      rate_func=smooth)
            self.play(hand_off(q_T, v54), run_time=0.6)
            beat.wait_until("Miller", offset=-0.2)
            self.play(cite_gvt.animate.set_opacity(0.3), pulse(cite_ms, 1.06, edge=LEFT),
                      run_time=0.8)
            # "puts the gap": the red gap between the cursors (never moved off 46% / 54%) gets its
            # number, -8, and is measured from the dashed line: the arrow slides until its tail
            # sits on it while the cursors and the lanes, done, fade where they stand (round 8:
            # no cursor is ever drawn at a share its label contradicts)
            beat.wait_until("gap", offset=-0.3)
            gap_live.clear_updaters()
            cur_H.clear_updaters()
            cur_T.clear_updaters()
            ga = h_arrow(xs(0.54), xs(0.46), LBL2, color=RED, width=5)
            self.remove(gap_live)
            self.add(ga)
            dx = C - xs(0.54)                          # the tail (54%) onto the dashed 50% line
            m8.move_to([xs(0.46) + dx - 0.2 - m8.width / 2, LBL2, 0])
            self.play(ga.animate.shift(RIGHT * dx), FadeIn(m8, shift=RIGHT * dx),
                      FadeOut(cur_H), FadeOut(cur_T), FadeOut(tracks), FadeOut(g_hits),
                      FadeOut(g_miss), run_time=0.6)
            # "at about minus eight points": zoom x5 about the dashed line; the tick labels turn
            # from shares into gap points, the right column steps back
            beat.wait_until("about", offset=-0.2)
            old_marks = list(tick_marks)
            for j in (0, 1, 3, 4):
                new_marks[j].set_stroke(opacity=0)
                gnums[j].set_opacity(0)
            gnums[2].set_opacity(0)
            gtitle.set_opacity(0)
            zt_c, gt_c = ztitle.get_center(), gtitle.get_center()
            # every piece the zoom changes is drawn once, by the rig: the axis group leaves the
            # scene (its line stays), so no label is drawn twice at partial opacity
            self.remove(self.axis, ga, m8)
            self.add(axis_line)
            rig = VGroup(ga, m8, *old_marks, *[new_marks[j] for j in (0, 1, 3, 4)],
                         *share_nums, *gnums, ztitle, gtitle)
            self.play(UpdateFromAlphaFunc(rig, zoom_step, rate_func=linear),
                      Transform(dashed, dashed_g),
                      obv.animate.move_to([C, G_TOP + 0.38, 0]),
                      right_col.animate.set_opacity(0.3),
                      run_time=1.8)
            # the zoomed axis: its five marks are the gap axis's -10 ... +10
            self.remove(rig)
            tick_marks = VGroup(new_marks[0], new_marks[1], old_marks[2], new_marks[3],
                                new_marks[4])
            self.add(tick_marks, gnums, gtitle, ga, m8)
            assert all(abs(tick_marks[j].get_center()[0] - gx(v)) < 1e-6
                       for j, v in enumerate(gap_p))
            # the random shooter's marker grows at the tip of the gap; the gap is the bias
            self.play(Create(mk8), FadeIn(rnd_lbl, shift=0.1 * DOWN),
                      FadeIn(bias_lbl, shift=0.1 * UP), run_time=0.6)
            # "Longer records shrink it": with 1,000 shots the -8 (GVT's 3-hit case) slides
            # almost to zero (the column's "up to 100 shots" answers)
            beat.wait_until("Longer", offset=-0.15)
            long_lbl.set_opacity(0)
            self.add(ghost, long_lbl)
            self.play(UpdateFromAlphaFunc(VGroup(ghost, long_lbl), long_step, rate_func=linear),
                      col2.animate(rate_func=there_and_back).set_opacity(1.0),
                      run_time=0.9)
            # "longer streaks grow it": the 1,000-shot ghost leaves; a ghost at the one-hit gap
            # gains a hit, slides to the two-hit gap, gains another and lands under -8
            beat.wait_until("longer", 2, offset=-0.5)
            self.play(FadeOut(ghost), FadeOut(long_lbl), run_time=0.4)
            self.add(ghost2, sdots)
            r_st = max(3.0, beat.remaining())
            self.play(UpdateFromAlphaFunc(VGroup(ghost2, sdots), streak_stepper(r_st),
                                          rate_func=linear), run_time=r_st)

        # ================================================================ 9 observed
        # Cornell's numbers take the random shooter's slots in the right column (its head
        # changes from "random" to "Cornell"); then 49 - 45 is written next to its marker
        head_C = text("Cornell", size=26, color=PURPLE).move_to(head_R, aligned_edge=LEFT)
        p49 = MathTex(r"49\%", font_size=36, color=PURPLE).move_to(v46, aligned_edge=LEFT)
        p45 = MathTex(r"45\%", font_size=36, color=PURPLE).move_to(v54, aligned_edge=LEFT)
        # round 9 (craft fix 1): the moment the head says "Cornell", the random shooter's
        # values under it become Cornell's unknowns, so no number sits under the wrong head
        pq_H = MathTex("?", font_size=36, color=PURPLE).move_to(v46, aligned_edge=LEFT)
        pq_T = MathTex("?", font_size=36, color=PURPLE).move_to(v54, aligned_edge=LEFT)
        marker4 = Line([gx(4), AX2, 0], [gx(4), G_TOP, 0], color=PURPLE, stroke_width=5)
        eq4 = MathTex("49", "-", "45", "=", "+4", font_size=40, color=PURPLE)
        eq4.move_to([gx(4) + 0.2 + eq4.width / 2, G_ARR, 0])
        # what the 1985 test made of +4: not distinguishable from zero. Round 10 (substance fix
        # 3): named as the 1985 study's own test (GVT's paired t-test on the players'
        # differences, replicated by M&S 2018 §3.1: p = .49), not a test of the subtraction
        p_lbl = MathTex(r"\text{1985 test: }p = .49", font_size=32, color=TGRAY)
        p_lbl.next_to(eq4, DOWN, buff=0.22, aligned_edge=LEFT)
        with self.beat("observed") as beat:
            # the streak ghost leaves (it sits under -8); Cornell's data arrives: GVT's citation
            # back to full, the column's head becomes "Cornell" (M&S stays at full: the p-value
            # shown below is their replication of GVT's test). Round 10 (substance fix 1): the
            # design tag "up to 100 shots" leaves, its job done
            self.play(FadeOut(ghost2), FadeOut(sdots), FadeOut(col2, rate_func=early(0.5)),
                      lab_H3.animate.set_opacity(1.0), lab_T3.animate.set_opacity(1.0),
                      hand_off(head_R, head_C), hand_off(v46, pq_H), hand_off(v54, pq_T),
                      cite_gvt.animate.set_opacity(1.0), run_time=0.8)
            beat.wait_until("forty nine", offset=-0.2)
            self.play(hand_off(pq_H, p49), run_time=0.6)
            beat.wait_until("forty five", offset=-0.2)
            self.play(hand_off(pq_T, p45), run_time=0.6)
            # "...after three misses. The study found": 49 and 45 travel, whole, to the right
            # of where Cornell's marker will stand, and the subtraction is written there
            beat.wait_until("misses", offset=0.05)
            self.play(emerge(p49[0][0:2], eq4[0], run_time=1.0),
                      emerge(p45[0][0:2], eq4[2], run_time=1.0, arc=-0.5),
                      FadeIn(eq4[1], rate_func=delayed(0.6)), run_time=1.0)
            # "plus four": the difference, and Cornell's marker grows up from the axis
            beat.wait_until("plus", offset=-0.15)
            # round 10 (both critics): as "= +4" lands, the right column steps back to 30% (its
            # two numbers now live in "49 - 45"), so the marker and its working are the subject
            self.play(Create(marker4), FadeIn(eq4[3]), FadeIn(eq4[4], shift=0.1 * RIGHT),
                      VGroup(head_C, lab_H3, lab_T3, p49, p45).animate(rate_func=delayed(0.35))
                      .set_opacity(0.3), run_time=0.8)
            self.adopt(eq4)
            # "too close to zero to count": the test was +4 against zero, the obvious guess
            beat.wait_until("zero", offset=-0.25)
            self.play(pulse(dashed, 1.06), pulse(obv, 1.12),
                      FadeIn(p_lbl, shift=0.1 * UP), run_time=0.9)

        brace = BraceBetweenPoints([gx(-8) + SH2, G_TOP + 0.22, 0], [gx(4) + SH2, G_TOP + 0.22, 0],
                                   direction=UP, color=PURPLE)
        brace_lbl = MathTex(r"+12\text{ points}", font_size=40, color=PURPLE)
        brace_lbl.next_to(brace, UP, buff=0.2)
        gym = text("no defenders", size=26, color=TGRAY, slant=ITALIC)
        # under "49 - 45 = +4", where it will stand once the chart re-centres
        gym.next_to(eq4, DOWN, buff=0.25, aligned_edge=LEFT).shift(RIGHT * SH2)
        chart = VGroup(axis_line, tick_marks, gnums, gtitle, dashed, mk8, ga, m8, rnd_lbl,
                       bias_lbl, marker4, eq4)
        # the +4 marker's tag, mirroring "random shooter" at -8: the column head itself travels
        # there, so "Cornell" is printed once
        tag_pos = np.array([gx(4) + SH2 + 0.2 + head_C.width / 2, rnd_lbl.get_center()[1], 0])
        with self.beat("hot") as beat:
            # "Measured from minus eight": the right column has done its job;
            # the chart takes the frame, carrying 49 - 45 = +4 with its marker; the column head
            # "Cornell" arcs up and over (clear of the column's labels) to tag the +4 marker
            self.play(FadeOut(VGroup(lab_H3, lab_T3, p49, p45), rate_func=early(0.45)),
                      FadeOut(p_lbl, shift=RIGHT * SH2, rate_func=early(0.45)),
                      head_C.animate(rate_func=delayed(0.15), path_arc=1.0).move_to(tag_pos)
                      .set_opacity(1.0),
                      FadeOut(obv, shift=RIGHT * SH2, rate_func=early(0.5)),
                      chart.animate.shift(RIGHT * SH2), run_time=1.1)
            self.play(GrowFromCenter(brace), run_time=beat.until("twelve", offset=-0.35))
            self.play(FadeIn(brace_lbl, shift=0.15 * DOWN), run_time=0.6)
            beat.wait_until("gym", offset=-0.25)
            self.play(FadeIn(gym, shift=0.1 * UP), run_time=0.7)
            beat.wait_until("defenders", offset=-0.2)
            self.play(pulse(gym, 1.1), pulse(eq4[4], 1.15, edge=LEFT), run_time=0.9)

        # ================================================================ 10 landing
        old_line, old_dashed = self.axis[0], dashed
        OFF.set_value(SHIFT1)
        self.build_axis()
        big2 = VGroup(*[make_coin(f, BIG_R) for f in "HHTH"]).arrange(RIGHT, buff=BIG_STEP - 2 * BIG_R)
        big2.move_to(BIG_C)
        rings2 = VGroup(ring(big2[1], BIG_R + 0.1, 5), ring(big2[2], BIG_R + 0.1, 5))
        arcs2 = VGroup(*[CurvedArrow(big2[i].get_top() + UP * 0.14, big2[i + 1].get_top() + UP * 0.14,
                                     angle=-PI / 2, color=BLUE, stroke_width=5, tip_length=0.22)
                         for i in (0, 1)])
        score2 = score_tex(1, 2, size=60).next_to(big2, RIGHT, buff=0.75)
        words2 = VGroup(*[text("hit" if f == "H" else "miss", size=28,
                               color=YELLOW if f == "H" else TGRAY, weight=BOLD).move_to(c)
                          for f, c in zip("HHTH", big2)])
        t_hits3 = self.axis_title("checked shots that are hits")
        dashed2 = DashedLine([vx(0.5), AX_Y, 0], [vx(0.5), LINE_TOP, 0], color=INK,
                             stroke_width=3, dash_length=0.12)
        guess2 = text("the obvious guess", size=26).move_to([0, LBL_Y, 0])
        guess2.align_to([vx(0.5) + 0.16, 0, 0], LEFT)
        blue2 = Line([vx(MEAN), AX_Y, 0], [vx(MEAN), LINE_TOP, 0], color=BLUE, stroke_width=5)
        # the test's own formula returns beside its 17/42 marker
        fl = MathTex(r"\displaystyle\frac{1}{14}", r"\displaystyle\sum_i",
                     r"\displaystyle\frac{h_i}{n_i}", "=", r"\displaystyle\frac{17}{42}",
                     font_size=40)
        fl[2][0:2].set_color(YELLOW)
        fl[2][3:5].set_color(BLUE)
        fl[4].set_color(BLUE)
        fl.set_stroke(width=0)
        fl.move_to([vx(MEAN) - 0.22 - fl.width / 2, LBL_Y + 0.05, 0])
        # the cold open's ghost of the sixteen runs: same place, size and opacity as at 0:09
        mini2 = self.build_mini(at=(vx(0.5), -0.15, 0))
        for g_ in mini2:
            self.allow_overlap(g_, reason="ghost miniature of the 16-row table (75% opacity): "
                                          "each letter sits inside its own small coin")
        # the shooter's average sits on the formula's line, on the one-half line
        DOT_Y = LBL_Y + 0.05
        shooter = Dot([vx(0.5), DOT_Y, 0], radius=0.15, color=BLUE)
        hot3 = Arrow([vx(MEAN) + 0.06, DOT_Y, 0], [vx(0.5) - 0.17, DOT_Y, 0], buff=0, color=BLUE,
                     stroke_width=8, max_tip_length_to_length_ratio=0.4, tip_length=0.24)
        hot3_lbl = text("hot", size=38, color=BLUE).next_to(shooter, RIGHT, buff=0.22)
        # what the dot is: this shooter's test score, an average over its rows (not one row)
        # round 9 (substance fix 6): "4-shot", so the tag is not read as a claim about real
        # 100-shot records (whose one-hit bias is only about -1 point)
        avg_tag = MathTex(r"\text{its 4-shot rows average }1/2", font_size=36, color=TGRAY)
        avg_tag.next_to(hot3_lbl, DOWN, buff=0.28, aligned_edge=LEFT)

        # the payoff clears, but its number line and dashed "no bias" line stay alive and
        # become the cold open's share axis and its dashed one-half guess
        keep = [old_line, old_dashed, tick_marks, gnums]
        outs = []

        def visit(m_):
            if any(m_ is k_ for k_ in keep):
                return
            fam = m_.get_family()
            if any(k_ in fam for k_ in keep):
                for sm in m_.submobjects:
                    visit(sm)
            else:
                outs.append(m_)

        for m_ in list(self.mobjects):
            visit(m_)
        # one move (no near-empty frame between the two pictures): the payoff fades while its
        # line and dashed zero drop into the share axis, and the cold open fades back in
        # round 9 (substance fix 5): the line, its ticks and the dashed line stay at full the
        # whole time and are in place by 0.8 s; the payoff fades out over 0.4 s while the cold
        # open fades in from 0.2 s (both faint where they overlap), so no frame is near-empty
        self.play(*[FadeOut(o_, rate_func=early(0.3)) for o_ in outs],
                  ReplacementTransform(old_line, self.axis[0], rate_func=window(0.05, 0.6)),
                  *[ReplacementTransform(tick_marks[j], self.axis[1][j], rate_func=window(0.05, 0.6))
                    for j in range(5)],
                  *[FadeOut(gnums[j], rate_func=early(0.25)) for j in range(5)],
                  *[FadeIn(self.axis[2][j], rate_func=window(0.2, 0.55)) for j in range(5)],
                  ReplacementTransform(old_dashed, dashed2, rate_func=window(0.05, 0.6)),
                  *[FadeIn(m_, rate_func=window(0.15, 0.55)) for m_ in
                    (self.axis[3], guess2, big2, rings2, arcs2, score2)],
                  run_time=1.3)
        self.adopt(self.axis)
        with self.beat("landing") as beat:
            beat.wait_until("One half", offset=-0.2)
            self.play(pulse(dashed2, 1.06), pulse(guess2, edge=LEFT), run_time=0.9)
            # "is what a fair coin does": the cold open's sixteen runs return, in the cold open's
            # place and size (75%), while the row steps back (as it did then) and the dashed
            # guess steps back to 25% so it does not cut through them (round 7)
            beat.wait_until("is", offset=-0.1)
            row2 = VGroup(big2, rings2, arcs2, score2)
            row2.save_state()
            self.play(LaggedStart(*[FadeIn(g, shift=0.06 * DOWN) for g in mini2], lag_ratio=0.05),
                      row2.animate.fade(0.6), FadeOut(guess2, rate_func=early(0.3)),
                      dashed2.animate.set_stroke(opacity=0.25), run_time=0.8)
            # held >= 1.5 s, then "Seventeen out of forty two": they average, one row after
            # another, into the test's formula, which lands beside its marker at 17/42
            beat.wait_until("Seventeen", offset=-0.15)
            # round 8 (craft fix 3): the rows themselves leave one after another, left-most
            # column first (so none crosses a row still waiting), each stepping back to 40% as
            # it lifts and arcing up and over into the formula (lag 0.22: about four in flight,
            # spread along the arc, never a bunch)
            # round 10 (craft fix 4): "1/14 sum" is written first and the rows land on the sum;
            # h_i / n_i is written only once the last row has landed, so no row in flight
            # passes over a glyph that is still fading in
            e_ = fl[1].get_center()
            order = sorted(SCORED, key=lambda k: (k % 4, k // 4))
            self.play(LaggedStart(*[self.depart(mini2[k], e_, [(mini2[k].get_x(), 0.9, 0),
                                                               (e_[0] + 0.3, 0.9, 0)],
                                                scale_to=0.4, mid=0.4, fade=(0.2, 0.55, 0.9))
                                    for k in order], lag_ratio=0.22),
                      # (only once the left-most column, which stands where the sum is
                      # written, has left)
                      FadeIn(fl[0], rate_func=window(0.4, 0.55)),
                      FadeIn(fl[1], rate_func=window(0.42, 0.58)),
                      *[FadeOut(mini2[k]) for k in UNDEF], Restore(row2), run_time=1.8)
            self.remove(*mini2)
            self.play(FadeIn(fl[2], shift=0.1 * UP), run_time=0.35)
            # the marker draws at 40.5%, and its own reading joins the formula: 17/42 slides out
            # of it to the left on "this test" (no copy of the line, which read as a doubled
            # marker)
            self.play(Create(blue2), run_time=0.4)
            self.play(FadeIn(fl[3]), blue2.animate(rate_func=there_and_back).set_stroke(width=9),
                      FadeIn(fl[4], shift=0.35 * LEFT, rate_func=delayed(0.25)), run_time=0.7)
            self.adopt(fl)
            # "A fifty percent shooter": the row is a shooter again, and the one-half line (back
            # to full) is that shooter's usual rate
            beat.wait_until("fifty percent", offset=-0.15)
            anims, tok = self.retitle(self.axis[3], t_hits3)
            self.swap_glyphs([c[1] for c in big2], list(words2), *anims,
                             dashed2.animate.set_stroke(opacity=1.0), run_time=0.9)
            self.retitle_done(tok)
            # "who averages one half on this test": the shooter's average over its rows, on
            # the one-half line; the single row steps back so it is not read as that score
            beat.wait_until("one half", 2, offset=-0.2)
            self.play(GrowFromCenter(shooter), row2.animate.fade(0.7),
                      FadeIn(avg_tag, shift=0.1 * RIGHT), run_time=0.7)
            beat.wait_until("already", offset=-0.25)
            self.play(GrowArrow(hot3), FadeIn(hot3_lbl, shift=0.1 * RIGHT),
                      run_time=beat.until("hot", offset=-0.05))
        # hold the answered frame >= 2 s after the arrow lands; no ident over it
        self.hold(1.2)
