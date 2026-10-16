"""Sample Space, episode 3: Which Map Is Random?

Two simulated maps of 537 hits: which one is pure chance?  A "hot-spot" detector (flag any
square with 3+ hits) agrees with the eye and gets it backwards: 39 false alarms on the truly
random map, none on the rule-based even one.  One square's chance of staying empty,
(1 - 1/576)^537 = 0.3933, explains why chance leaves gaps, and gaps force clumps; the same
counting (pick k bombs in, the rest out) gives the Poisson formula, whose bars are the honest
detector: the chi-squared misfit (sum of gap^2/chance) is 2.0 for A - three in four of 20,000
simulated pure-chance maps score worse - and 271.7 for B.  Simulated aim fails the other way.
Payoff: R. D. Clarke's 1946 flying-bomb table for south London on the real V-1 map (Shaw &
Shaw's digitised LCC data, the Thames from OS Open Rivers); limit: one lambda everywhere -
north of the Thames the hits were half as dense.

    videos/toolkit/render.sh --preview videos/episodes/003-clumpy-randomness/scene.py Episode out.mp4
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from manim import *
from sample_space import *

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import sim                                         # noqa: E402
from narration_text import B, BEAT_SPEED, PRON, SPEED   # noqa: E402

# secondary text a little lighter than the series grey: 7.9:1 on BG (BAR: text >= 7:1)
GRAY = "#A6ABB5"

# ----------------------------------------------------------------------------- data
G, N = sim.G, sim.N
_D = np.load(HERE / "sim_data.npz")
PTS_A, PTS_B, PTS_AIM = _D["a"], _D["b"], _D["aimed"]
NULL = _D["null"]                                  # misfit of 20,000 pure-chance maps
CNT_A, CNT_B = sim.counts(PTS_A), sim.counts(PTS_B)
H_A, H_B, H_AIM = sim.hist(CNT_A), sim.hist(CNT_B), sim.hist(sim.counts(PTS_AIM))
assert H_A == [222, 223, 92, 28, 9, 2], H_A
assert H_B == [109, 397, 70, 0, 0, 0], H_B
assert H_AIM == [399, 58, 37, 30, 13, 39], H_AIM
EXP = sim.poisson_expected()                       # 226.74 211.39 98.54 30.62 7.14 1.57
EXP_TXT = ["227", "211", "98.5", "30.6", "7.1", "1.6"]
CLARKE = [229, 211, 93, 35, 7, 1]                  # Clarke 1946, actual squares
assert round(sum(EXP[3:]), 1) == 39.3
PARTS_A = [(o - e) ** 2 / e for o, e in zip(H_A, EXP)]          # misfit per bar, map A
PARTS_TXT = ["%.2f" % x for x in PARTS_A]
assert PARTS_TXT == ["0.10", "0.64", "0.43", "0.22", "0.49", "0.12"], PARTS_TXT
assert round(sum(float(t) for t in PARTS_TXT), 2) == 2.00 and round(sum(PARTS_A), 1) == 2.0
MIS_B = sim.misfit(H_B)
assert round(MIS_B, 1) == 271.7
P_A = float((NULL >= 2.0).mean())
assert round(P_A, 2) == 0.74, P_A                  # chi2_4 tail: 0.736; simulation: 0.745
_R = np.load(HERE / "real_data.npz")               # realdata.py: Shaw & Shaw's V-1 sites (BNG m)
REAL = _R["pts"] / 1000.0                          # km
CBOX = _R["clarke_box"] / 1000.0                   # (x0, x1, y0, y1) km
NBOX = _R["north_box"] / 1000.0
THAMES = _R["thames"] / 1000.0                     # OS Open Rivers centreline (km)

# ----------------------------------------------------------------------------- layout
P1_SIDE = 4.8
P1_A = np.array([-3.45, 0.25, 0])
P1_B = np.array([3.45, 0.25, 0])
P2_SIDE = 4.7
P2_C = np.array([-3.85, -0.02, 0])
RX = 2.75                                          # right-panel centre x (phase 2)
EQ1_Y = 3.05                                       # Poisson formula row once the histogram is up
SHADE = [0.0, 0.17, 0.34, 0.52, 0.68, 0.8]         # cell fill opacity by hit count
FS = 38                                            # working equation size
EMPTY_FILL = 0.85                                  # empty squares: clearly YELLOW, not olive
INSET_SCALE = 5                                    # tail inset magnification
MAP_DIM = 0.3                                      # map behind the derivation / zoom insets
MAP_LOW = 0.35                                     # map beside the chi-squared build
# zoom row (reveal beat): [A][A zoom][B][B zoom] across the safe area, zooms in the gutters
ZS, Z_INS, Z_GAP, Z_MID = 0.7, 2.3, 0.3, 0.6
Z_SIDE = P1_SIDE * ZS
_z0 = -(2 * Z_SIDE + 2 * Z_INS + 2 * Z_GAP + Z_MID) / 2
ZA_C = np.array([_z0 + Z_SIDE / 2, P1_A[1], 0])
ZA_INS_X = _z0 + Z_SIDE + Z_GAP + Z_INS / 2
ZB_C = np.array([_z0 + Z_SIDE + Z_GAP + Z_INS + Z_MID + Z_SIDE / 2, P1_B[1], 0])
ZB_INS_X = ZB_C[0] + Z_SIDE / 2 + Z_GAP + Z_INS / 2
ZONE_I0 = G - 4                                    # zoom blocks touch the map's right edge
# real map (phase 3): km -> scene units
RM_S = 0.2
RM_X0, RM_Y0 = -6.3, -1.7                          # scene position of (E min, N min)
RM_E0, RM_N0 = REAL[:, 0].min(), REAL[:, 1].min()
RDOT = 0.035                                       # dot diameter < one 0.5 km square (0.1)
# misfit distribution (phase 2b, left)
MF_X0, MF_LEN, MF_MAX, MF_Y = -6.2, 3.8, 16, -1.85
MF_H = 2.3


def rm(e, n):
    return np.array([RM_X0 + (e - RM_E0) * RM_S, RM_Y0 + (n - RM_N0) * RM_S, 0.0])


def mfx(v):
    return MF_X0 + v / MF_MAX * MF_LEN


def shade(c: int) -> float:
    return SHADE[min(int(c), 5)]


def flag(m: Mobject, color=YELLOW, run_time: float = 0.8):
    """Colour-only flag (no scaling, so a flagged frame/bar never grows into its labels)."""
    return Indicate(m, color=color, scale_factor=1.0, run_time=min(run_time, 1.0))


def window(a: float, d: float):
    """Rate function that runs smoothly from alpha a to a + d of its animation (0 before,
    1 after): lets one animation inside a longer play() start late."""
    return lambda t: smooth(min(1.0, max(0.0, (t - a) / d)))


def grayify(ax: Axes) -> Axes:
    """Series axes, with tick numbers and titles in this episode's lighter GRAY."""
    for m in (ax.x_axis.numbers, ax.y_axis.numbers, ax.x_title, ax.y_title):
        if m is not None:
            m.set_color(GRAY)
    return ax


def cite(s: str, size: float = 20) -> Text:
    return citation(s, size=size, color=GRAY)


def count_label(tracker, one: str, many: str, color, size=36) -> VGroup:
    """Live integer + a singular/plural word ("1 target", "39 targets")."""
    num = DecimalNumber(tracker.get_value(), num_decimal_places=0, font_size=size, color=color)
    w1 = MathTex(r"\text{%s}" % one, font_size=size, color=color)
    w2 = MathTex(r"\text{%s}" % many, font_size=size, color=color)
    g = VGroup(num, w2, w1)
    w2.next_to(num, RIGHT, buff=0.15)
    w1.next_to(num, RIGHT, buff=0.15).align_to(w2, DOWN)

    def upd(m):
        v = tracker.get_value()
        m.set_value(v)
        w2.next_to(m, RIGHT, buff=0.15)
        w1.next_to(m, RIGHT, buff=0.15).align_to(w2, DOWN)
        single = int(round(v)) == 1
        w1.set_opacity(1.0 if single else 0.0)
        w2.set_opacity(0.0 if single else 1.0)
    num.add_updater(upd)
    upd(num)
    g.number, g.many, g.one = num, w2, w1
    return g


class Panel:
    """One square map: cells (shaded by count), grid, frame, dots + its label rows."""

    def __init__(self, pts, cnt, name: str, side: float, center):
        self.cnt = cnt
        self.side = side
        cell = side / G
        self.cellsize = cell
        c = np.array(center, dtype=float)
        o = c - np.array([side / 2, side / 2, 0])
        self.frame = Square(side, stroke_color=GRAY, stroke_width=2.5).move_to(c)
        lines = [Line(o + [k * cell, 0, 0], o + [k * cell, side, 0]) for k in range(1, G)]
        lines += [Line(o + [0, k * cell, 0], o + [side, k * cell, 0]) for k in range(1, G)]
        self.grid = VGroup(*lines).set_stroke(DIM, 1.2)
        self.counts = []
        cells = []
        for i in range(G):
            for j in range(G):
                sq = Square(cell, stroke_width=0, fill_color=BLUE, fill_opacity=0)
                sq.move_to(o + [(i + 0.5) * cell, (j + 0.5) * cell, 0])
                cells.append(sq)
                self.counts.append(int(cnt[i, j]))
        self.cells = VGroup(*cells)
        self.dots = VGroup(*[Dot(o + [p[0] * cell, p[1] * cell, 0], radius=0.055, color=INK)
                             for p in pts]).set_z_index(1)   # always above the cell shading
        self.map = VGroup(self.cells, self.grid, self.frame, self.dots)
        self.name = Text(name, font_size=40).next_to(self.frame, UP, buff=0.2)
        self.name.align_to(self.frame, LEFT)
        self.sim = Text("simulated", font_size=24, color=GRAY)
        self.sim.next_to(self.name, RIGHT, buff=0.22, aligned_edge=DOWN)
        self.hits_t = ValueTracker(N)
        self.hits = live_number(self.hits_t, 0, size=36, suffix=r"\text{hits}")
        self.hits[-1].set_color(GRAY)
        self.hits.next_to(self.frame, UP, buff=0.2).align_to(self.frame, RIGHT)
        self.top = VGroup(self.name, self.sim, self.hits)
        self.pts = pts
        self.yellow_empties = False                  # set once the empty squares are filled

    def where(self, k: int) -> list[int]:
        """Cell indices with exactly k hits (k=5 means 5 or more)."""
        return [i for i, c in enumerate(self.counts) if (c >= 5 if k == 5 else c == k)]

    def cells_with(self, k: int) -> VGroup:
        return VGroup(*[self.cells[i] for i in self.where(k)])

    def outline(self, idx: int, color=RED, width: float = 3.5, z: float = 2) -> Square:
        c = self.cells[idx]
        return Square(c.width, stroke_color=color, stroke_width=width).move_to(c).set_z_index(z)

    def below(self, m: Mobject, side=LEFT) -> Mobject:
        return m.next_to(self.frame, DOWN, buff=0.2).align_to(self.frame, side)

    def shaded_targets(self):
        """Fill opacity each cell should have when shaded by count."""
        return [shade(c) for c in self.counts]

    def set_level(self, f: float, yellow: float = 1.0):
        """Uniform dimming of the whole map: cells, grid, frame and dots at level f.  Empty
        squares that were filled yellow fade by `yellow` instead (a dimmed yellow reads olive)."""
        for i, c in enumerate(self.cells):
            if self.counts[i] == 0 and self.yellow_empties:
                c.set_fill(YELLOW, EMPTY_FILL * yellow)
            else:
                c.set_fill(BLUE, shade(self.counts[i]) * f)
        self.dots.set_opacity(f)
        self.grid.set_stroke(opacity=f)
        self.frame.set_stroke(opacity=f)

    def level_anim(self, f0, f1, y0=1.0, y1=1.0, extra=None, **kw):
        """Animate set_level from (f0, y0) to (f1, y1); `extra(m, f)` dims companions."""
        def upd(m, a):
            f = f0 + (f1 - f0) * a
            self.set_level(f, y0 + (y1 - y0) * a)
            if extra is not None:
                extra(f)
        return UpdateFromAlphaFunc(self.map, upd, **kw)


X0 = 0.6                                           # bar k sits at data x = k + X0


def bx(ax: Axes, k: int) -> float:
    return ax.c2p(k + X0, 0)[0]


def bar(ax: Axes, k: int, v: float, w: float, **style) -> Rectangle:
    unit = ax.x_axis.unit_size
    h = max(ax.c2p(0, v)[1] - ax.c2p(0, 0)[1], 0.002)
    return Rectangle(width=w * unit, height=h, **style).move_to(ax.c2p(k + X0, 0),
                                                                 aligned_edge=DOWN)


def exp_bars(ax: Axes) -> VGroup:
    return VGroup(*[bar(ax, k, v, 0.72, stroke_color=PURPLE, stroke_width=3,
                        fill_color=PURPLE, fill_opacity=0.14) for k, v in enumerate(EXP)])


def obs_bars(ax: Axes, vals) -> VGroup:
    return VGroup(*[bar(ax, k, v, 0.42, stroke_width=0, fill_color=BLUE, fill_opacity=0.92)
                    .set_z_index(2) for k, v in enumerate(vals)])


# ---- the x5 tail inset: same columns as bars 3, 4, 5+, five times taller
def inset_base(ax: Axes) -> float:
    return ax.c2p(0, 0)[1] + 0.55


def inset_unit(ax: Axes) -> float:
    return INSET_SCALE * (ax.c2p(0, 1)[1] - ax.c2p(0, 0)[1])


def inset_bar(ax: Axes, k: int, v: float, w: float, **style) -> Rectangle:
    unit = ax.x_axis.unit_size
    h = max(v * inset_unit(ax), 0.002)
    return Rectangle(width=w * unit, height=h, **style).move_to(
        [bx(ax, k), inset_base(ax), 0], aligned_edge=DOWN)


def inset_frame(ax: Axes) -> VGroup:
    base = inset_base(ax)
    x0, x1 = bx(ax, 3) - 0.45, bx(ax, 5) + 0.5
    top = base + 40 * inset_unit(ax) + 0.12
    fr = Rectangle(width=x1 - x0, height=top - (base - 0.08), stroke_color=GRAY,
                   stroke_width=1.5).move_to([(x0 + x1) / 2, (top + base - 0.08) / 2, 0])
    baseline = Line([x0 + 0.08, base, 0], [x1 - 0.08, base, 0], stroke_color=GRAY,
                    stroke_width=2)
    lbl = MathTex(r"\times 5", font_size=MATH_SMALL, color=GRAY)
    lbl.next_to(fr.get_corner(UR), DL, buff=0.12)
    g = VGroup(fr, baseline, lbl)
    g.frame, g.lbl = fr, lbl
    return g


def inset_exp(ax: Axes) -> VGroup:
    return VGroup(*[inset_bar(ax, k, EXP[k], 0.72, stroke_color=PURPLE, stroke_width=3,
                              fill_color=PURPLE, fill_opacity=0.14) for k in (3, 4, 5)])


def inset_obs(ax: Axes, vals) -> VGroup:
    return VGroup(*[inset_bar(ax, k, vals[k], 0.42, stroke_width=0, fill_color=BLUE,
                              fill_opacity=0.92).set_z_index(2) for k in (3, 4, 5)])


def gap_slivers(ax: Axes, vals) -> VGroup:
    """Yellow outline of each bar's gap between observed and chance (bars 0-2 in the chart,
    3-5+ in the x5 inset, where they are visible)."""
    out = VGroup()
    unit = ax.x_axis.unit_size
    for k, (o, e) in enumerate(zip(vals, EXP)):
        if k < 3:
            y0, y1 = ax.c2p(0, min(o, e))[1], ax.c2p(0, max(o, e))[1]
        else:
            y0 = inset_base(ax) + min(o, e) * inset_unit(ax)
            y1 = inset_base(ax) + max(o, e) * inset_unit(ax)
        r = Rectangle(width=0.42 * unit, height=max(y1 - y0, 0.02), stroke_color=YELLOW,
                      stroke_width=3.5, fill_color=YELLOW, fill_opacity=0.9)
        out.add(r.move_to([bx(ax, k), (y0 + y1) / 2, 0]).set_z_index(3))
    return out


def best_region(cnt, n: int, lo: int, hi: int, most: bool = True):
    """Lower-left cell (i0, j0) of the n x n block with the most (or median) hits."""
    best, arg = None, None
    for i0 in range(lo, hi):
        for j0 in range(lo, hi):
            v = int(cnt[i0:i0 + n, j0:j0 + n].sum())
            if best is None or (v > best if most else abs(v - n * n) < abs(best - n * n)):
                best, arg = v, (i0, j0)
    return arg


def inset(panel: "Panel", i0: int, j0: int, n: int, center, size: float, r_cells: float = 0.4):
    """Zoomed view of an n x n block of cells: dots with discs of radius r_cells (in square
    widths; two discs overlap exactly when two hits are closer than 2 r_cells), the block's
    grid, a source outline and two zoom lines.  .close marks discs that overlap another."""
    cell = panel.frame.width / G
    o = panel.frame.get_corner(DL)
    src = Square(n * cell, stroke_color=YELLOW, stroke_width=2.5)
    src.move_to(o + np.array([(i0 + n / 2) * cell, (j0 + n / 2) * cell, 0]))
    pad = 0.5
    z = size / ((n + 2 * pad) * cell)
    c = np.array(center, dtype=float)
    margin = Square(size + 0.16, stroke_width=0, fill_color=BG, fill_opacity=1).move_to(c)
    box_ = Square(size, stroke_color=YELLOW, stroke_width=2.5, fill_color=BG, fill_opacity=1)
    box_.move_to(c)

    def w(x, y):
        return c + np.array([(x - (i0 + n / 2)) * cell * z, (y - (j0 + n / 2)) * cell * z, 0])
    grid = VGroup(*[Line(w(i0 + k, j0), w(i0 + k, j0 + n)) for k in range(n + 1)],
                  *[Line(w(i0, j0 + k), w(i0 + n, j0 + k)) for k in range(n + 1)])
    grid.set_stroke(DIM, 1.5)
    inside = np.array([p for p in panel.pts if i0 <= p[0] < i0 + n and j0 <= p[1] < j0 + n])
    d = np.hypot(*(inside[:, None, :] - inside[None, :, :]).transpose(2, 0, 1))
    np.fill_diagonal(d, 99)
    close = d.min(axis=1) < 2 * r_cells
    discs = VGroup(*[Circle(r_cells * cell * z, stroke_color=GRAY, stroke_width=1.5,
                            fill_color=GRAY, fill_opacity=0.28).move_to(w(*p)) for p in inside])
    pts = VGroup(*[Dot(w(*p), radius=0.07, color=INK) for p in inside])
    # the inset sits in the gutter to the map's right and the block touches the map's right
    # edge, so the leader lines run only through empty gutter (never across data)
    lines = VGroup(Line(src.get_corner(UR), box_.get_corner(UL)),
                   Line(src.get_corner(DR), box_.get_corner(DL))).set_stroke(YELLOW, 1.5, 0.6)
    g = VGroup(src, lines, VGroup(margin, box_), grid, discs, pts).set_z_index(4)
    g.discs = discs
    g.close = VGroup(*[dd for dd, cl in zip(discs, close) if cl])
    return g


class Episode(NarratedScene):
    EPISODE = 3
    TITLE = "Which Map Is Random?"
    PRONUNCIATIONS = PRON
    SPEED = SPEED

    def say_beat(self, key: str):
        return self.narrate(B[key], speed=BEAT_SPEED.get(key))

    def settle(self, m: Mobject):
        """After glyph-wise Replacement transforms, keep one copy of m on screen."""
        self.remove(*m.get_family())
        self.add(m)

    @staticmethod
    def ghost(src: Mobject, dst: Mobject):
        """src flies into dst's shape without padding dst with duplicate sub-paths (which a
        TransformFromCopy from many objects into few glyphs would leave behind)."""
        g = dst.copy()
        return ReplacementTransform(src.copy(), g), g

    def land(self, g: Mobject, dst: Mobject):
        self.remove(g)
        self.add(dst)

    def end_card(self, hold: float = 0.8, run_time: float = 0.5):
        card = end_card(self.EPISODE, self.TITLE)
        card[1].set_color(GRAY)
        self.play(*[FadeOut(m) for m in list(self.mobjects)], FadeIn(card, shift=0.1 * UP),
                  run_time=run_time)
        self.hold(hold)

    # ------------------------------------------------------------------ construct
    def construct(self):
        A = Panel(PTS_A, CNT_A, "A", P1_SIDE, P1_A)
        Bp = Panel(PTS_B, CNT_B, "B", P1_SIDE, P1_B)
        for p in (A, Bp):
            p.dots.set_opacity(0)
            p.hits_t.set_value(0)
        self.add(A.frame, Bp.frame, A.top, Bp.top, A.dots, Bp.dots)

        # pick the clusters the stakes circles land on (A's 5-hit cells + densest 4)
        big = sorted(range(G * G), key=lambda i: -A.counts[i])[:3]

        # ============================================================ 1. cold open
        def rain(m, a):
            n = a * N
            for p in (A, Bp):
                for i, d in enumerate(p.dots):
                    d.set_opacity(float(np.clip(n - i, 0, 1)))
                p.hits_t.set_value(min(N, int(n)))

        aorb = Text("A or B?", font_size=30, color=GRAY).move_to([0, -3.0, 0])
        with self.say_beat("cold") as beat:
            self.play(UpdateFromAlphaFunc(VGroup(A.dots, Bp.dots), rain), rate_func=linear,
                      run_time=beat.until("chance"))
            beat.wait_until("Which", offset=-0.1)
            self.play(flag(A.name), FadeIn(aorb, shift=0.1 * UP), run_time=0.7)
            self.play(flag(Bp.name), run_time=0.7)
        for p in (A, Bp):
            p.hits[0].clear_updaters()

        # ============================================================ 2. stakes
        circles = VGroup(*[Circle(radius=A.cellsize * 1.35, stroke_color=YELLOW, stroke_width=3)
                           .move_to(A.cells[i]) for i in big]).set_z_index(2)
        quote = Text("“…tended to be grouped in clusters.”", font_size=26, slant=ITALIC)
        quote.move_to([0, -2.55, 0])
        cite1 = cite("R. D. Clarke, 1946 · J. Inst. Actuaries 72:481;  "
                     "Shaw & Shaw, 2019 · Significance 16(5)", size=SMALL)
        with self.say_beat("stakes") as beat:
            self.play(FadeOut(aorb), run_time=0.4)
            beat.wait_until("simulated", offset=-0.2)
            self.play(flag(A.sim), flag(Bp.sim), run_time=0.8)
            beat.wait_until("nineteen", offset=-0.1)
            self.play(FadeIn(cite1), run_time=0.7)
            beat.wait_until("Londoners", offset=-0.1)
            self.play(FadeIn(quote, shift=0.1 * UP), run_time=1.0)
            beat.wait_until("clusters", offset=-0.3)
            self.play(LaggedStart(*[Create(c) for c in circles], lag_ratio=0.3), run_time=1.2)
            beat.wait_until("factories", offset=-0.2)
            self.play(LaggedStart(*[c.animate.scale(1.25).set_stroke(opacity=0) for c in circles],
                                  lag_ratio=0.2), run_time=1.4)
            self.remove(circles)

        # ============================================================ 3. naive build
        ex_idx = min((i for i in A.where(3)),
                     key=lambda i: abs(i // G - 11) + abs(i % G - 13))
        ex_box = A.outline(ex_idx, z=3)
        ex_dots = VGroup(*[d for d, p in zip(A.dots, PTS_A)
                           if int(p[0]) * G + int(p[1]) == ex_idx])

        def sweep(m, a):
            for p in (A, Bp):
                tg = p.shaded_targets()
                for idx, c in enumerate(p.cells):
                    col = idx // G
                    w = float(np.clip(a * (G + 6) - col, 0, 6) / 6)
                    c.set_fill(opacity=tg[idx] * w)

        ring = Circle(radius=0.35, stroke_color=RED, stroke_width=3).move_to(A.cells[ex_idx])
        ring.set_z_index(3)
        with self.say_beat("build") as beat:
            self.play(FadeOut(quote), FadeOut(cite1), run_time=0.6)
            beat.wait_until("Cut", offset=-0.1)
            self.add(A.cells, Bp.cells)
            self.bring_to_front(A.dots, Bp.dots)
            self.play(Create(A.grid), Create(Bp.grid), run_time=beat.until("count"))
            self.bring_to_front(A.frame, Bp.frame, A.dots, Bp.dots)
            self.play(UpdateFromAlphaFunc(VGroup(A.cells, Bp.cells), sweep),
                      run_time=beat.until("flag", offset=-0.1))
            beat.wait_until("this one", offset=-0.3)
            self.play(Create(ex_box), LaggedStart(*[flag(d) for d in ex_dots], lag_ratio=0.15),
                      Create(ring, run_time=0.4), run_time=1.0)

        # ============================================================ 4. flags
        tgt_idx = [i for i, c in enumerate(A.counts) if c >= 3]
        boxes = VGroup(*[A.outline(i, z=3) for i in tgt_idx if i != ex_idx])
        tA = ValueTracker(39)
        cntA = count_label(tA, "target", "targets", RED)
        # the number sits where "39 false alarms" will need it, so it never moves
        alarm = formula(r"\text{false alarms}", size=36, color=RED)
        probe = VGroup(DecimalNumber(39, num_decimal_places=0, font_size=36), alarm.copy())
        probe.arrange(RIGHT, buff=0.15)
        A.below(probe, RIGHT)
        cntA.number.move_to(probe[0].get_center())
        cntA.number.update()
        tA.set_value(1)
        cntA.number.update()
        tB = ValueTracker(0)
        cntB = count_label(tB, "target", "targets", RED)
        Bp.below(cntB, RIGHT)
        tagA = A.below(Text("aimed?", font_size=26, color=RED))
        tagB = Bp.below(Text("chance?", font_size=26, color=PURPLE))
        with self.say_beat("flags") as beat:
            self.play(FadeIn(cntA), run_time=0.4)
            T = beat.until("Map B", offset=-0.1)
            # the ring leaves just after "Map A lights up"
            t_off = beat.time_of("up", end=True) + 0.15 - beat.elapsed()
            self.play(LaggedStart(*[Create(b) for b in boxes], lag_ratio=0.06, rate_func=linear),
                      tA.animate(rate_func=linear).set_value(39),
                      FadeOut(ring, rate_func=window(t_off / T, 0.5 / T)), run_time=T)
            self.play(FadeIn(cntB, shift=0.1 * UP), run_time=0.6)
            beat.wait_until("aimed", offset=-0.25)
            self.play(FadeIn(tagA, shift=0.1 * UP), run_time=0.6)
            beat.wait_until("chance", offset=-0.25)
            self.play(FadeIn(tagB, shift=0.1 * UP), run_time=0.6)
        boxes.add(ex_box)

        # ============================================================ 5. reveal
        tagA2 = A.below(Text("pure chance", font_size=26, color=PURPLE))
        tagB2 = Bp.below(formula(r"\text{rule: gap}", r"\ge", r"\tfrac{4}{5}", r"\text{ square}",
                                 size=36))
        # zoom blocks on the maps' right edge: A's densest 4 x 4 block, B's most typical one
        jA = max(range(2, G - 5), key=lambda j: CNT_A[ZONE_I0:, j:j + 4].sum())
        jB = min(range(2, G - 5), key=lambda j: (abs(CNT_B[ZONE_I0:, j:j + 4].sum() - 16),
                                                 abs(j - jA)))
        gA, gB = Square(Z_SIDE).move_to(ZA_C), Square(Z_SIDE).move_to(ZB_C)

        def zoom_y(j):                         # inset centred on its block, inside the map's span
            y = P1_A[1] - Z_SIDE / 2 + (j + 2) * Z_SIDE / G
            return float(np.clip(y, P1_A[1] - Z_SIDE / 2 + Z_INS / 2,
                                 P1_A[1] + Z_SIDE / 2 - Z_INS / 2))
        tagB2.next_to(gB, DOWN, buff=0.2).align_to(gB, LEFT)
        citeFK = cite("Falk & Konold, 1997 · Psych. Review 104(2)")

        def dim_boxes(f):
            boxes.set_stroke(opacity=f)

        with self.say_beat("reveal") as beat:
            self.play(ReplacementTransform(tagA, tagA2), FadeOut(tagB, shift=0.1 * DOWN),
                      run_time=beat.until("dropped", offset=-0.1))
            self.play(flag(tagA2), run_time=0.8)
            beat.wait_until("false", offset=-0.3)
            cntA.number.clear_updaters()
            alarm.next_to(cntA.number, RIGHT, buff=0.15).align_to(cntA.number, DOWN)
            self.remove(cntA.one)
            self.play(FadeOut(cntA.many, shift=0.2 * UP), FadeIn(alarm, shift=0.2 * UP),
                      run_time=0.6)
            # "Map B's rule": both maps shrink to make a row with a gutter for each zoom
            beat.wait_until("map", occurrence=2, offset=-0.1)
            alarm_grp = VGroup(cntA.number, alarm)
            for m in (A.name, A.sim, Bp.name, Bp.sim, tagA2, alarm_grp):
                m.generate_target()
            A.name.target.next_to(gA, UP, buff=0.2).align_to(gA, LEFT)
            A.sim.target.next_to(A.name.target, RIGHT, buff=0.22, aligned_edge=DOWN)
            Bp.name.target.next_to(gB, UP, buff=0.2).align_to(gB, LEFT)
            Bp.sim.target.next_to(Bp.name.target, RIGHT, buff=0.22, aligned_edge=DOWN)
            tagA2.target.next_to(gA, DOWN, buff=0.2).align_to(gA, LEFT)
            alarm_grp.target.next_to(gA, DOWN, buff=0.2)
            alarm_grp.target.align_to(tagA2.target.get_right() + 0.45 * RIGHT, LEFT)
            self.play(FadeOut(cntB), FadeOut(A.hits), FadeOut(Bp.hits),
                      VGroup(A.map, boxes).animate.scale(ZS, about_point=A.frame.get_center())
                      .shift(ZA_C - A.frame.get_center()),
                      Bp.map.animate.scale(ZS, about_point=Bp.frame.get_center())
                      .shift(ZB_C - Bp.frame.get_center()),
                      *[MoveToTarget(m) for m in (A.name, A.sim, Bp.name, Bp.sim, tagA2,
                                                  alarm_grp)], run_time=0.8)
            insB = inset(Bp, ZONE_I0, jB, 4, [ZB_INS_X, zoom_y(jB), 0], Z_INS)
            insA = inset(A, ZONE_I0, jA, 4, [ZA_INS_X, zoom_y(jA), 0], Z_INS)
            self.play(FadeIn(tagB2, shift=0.1 * UP), run_time=0.4)
            # both maps step back while the zooms are up: the zooms are the only focus
            beat.wait_until("no two", offset=-0.25)
            self.play(Bp.level_anim(1, MAP_DIM), A.level_anim(1, MAP_DIM, extra=dim_boxes),
                      Create(insB[0]), run_time=0.5)
            self.play(Create(insB[1]), FadeIn(insB[2:4]), FadeIn(insB[5]), run_time=0.6)
            self.play(LaggedStart(*[GrowFromCenter(d) for d in insB.discs], lag_ratio=0.08),
                      run_time=beat.until("square", occurrence=1, offset=0.2, end=True))
            beat.wait_until("detector", offset=-0.2)
            self.play(Create(insA[0]), FadeIn(citeFK), run_time=0.5)
            self.play(Create(insA[1]), FadeIn(insA[2:4]), FadeIn(insA[5]), run_time=0.7)
            self.play(LaggedStart(*[GrowFromCenter(d) for d in insA.discs], lag_ratio=0.05),
                      run_time=1.2)
            beat.wait_until("spread", offset=-0.1)
            self.play(insA.close.animate.set_fill(RED, 0.4).set_stroke(RED, 2.5), run_time=0.9)

        # ============================================================ 6. one square
        s = P2_SIDE / P1_SIDE
        empty_ids = [i for i, c in enumerate(A.counts) if c == 0]

        def clearance(i):                      # distance from the cell to the nearest dot
            ci, cj = i // G + 0.5, i % G + 0.5
            dx = np.maximum(np.abs(PTS_A[:, 0] - ci) - 0.5, 0)
            dy = np.maximum(np.abs(PTS_A[:, 1] - cj) - 0.5, 0)
            return float(np.min(np.hypot(dx, dy)))
        clear_ids = [i for i in empty_ids if clearance(i) > 0.35] or empty_ids
        pick = min(clear_ids, key=lambda i: abs(i // G - 12) + abs(i % G - 12))
        # P( empty ) = (1 - 1/576)^537 ~ 0.3933, with P( and ) as their own parts
        E1 = formula("P(", r"\text{empty}", ")", "=", r"\Big(1-", r"\frac{1}{576}",
                     r"\Big)^{537}", r"\approx 0.3933", size=FS)
        e_P, e_word, e_close, e_eq, e_open, e_frac, e_pow, e_val = E1
        EL = formula("=", r"\Big(1-", r"\frac{\lambda}{537}", r"\Big)^{537}", r"\approx",
                     r"e^{-\lambda}", r"\approx 0.3937", size=FS)
        # place the two rows so their "=" signs line up and the block is centred
        EL.shift(e_eq.get_center() - EL[0].get_center() + 1.3 * DOWN)
        blk = VGroup(E1, EL)
        blk.shift(np.array([RX - 0.15, 1.05, 0]) - np.array([blk.get_center()[0], E1.get_center()[1], 0]))
        e_word.set_color(YELLOW)
        EL[5].set_color(PURPLE)
        ysq = A.outline(pick, color=YELLOW, width=4.5, z=3)
        gP = Square(P2_SIDE).move_to(P2_C)
        for m in (A.name, A.sim, tagA2):
            m.generate_target()
            m.target.scale(s)
        A.name.target.next_to(gP, UP, buff=0.2 * s).align_to(gP, LEFT)
        A.sim.target.next_to(A.name.target, RIGHT, buff=0.22 * s, aligned_edge=DOWN)
        tagA2.target.next_to(gP, DOWN, buff=0.2 * s).align_to(gP, LEFT)
        A.hits.scale(s).next_to(gP, UP, buff=0.2 * s).align_to(gP, RIGHT)
        with self.say_beat("square") as beat:
            # B and the zooms clear out before A grows over the zooms' place
            self.play(FadeOut(VGroup(Bp.map, Bp.name, Bp.sim, tagB2, insA, insB, cntA.number,
                                     alarm, citeFK), rate_func=window(0, 0.4)),
                      VGroup(A.map, boxes).animate.scale(P2_SIDE / Z_SIDE,
                                                         about_point=A.frame.get_center())
                      .shift(P2_C - A.frame.get_center()),
                      *[MoveToTarget(m) for m in (A.name, A.sim, tagA2)], FadeIn(A.hits),
                      A.level_anim(MAP_DIM, 1, extra=dim_boxes), run_time=1.1)
            ysq.become(A.outline(pick, color=YELLOW, width=4.5, z=3))
            self.play(Create(ysq), boxes.animate.set_stroke(opacity=0.3), run_time=0.5)
            beat.wait_until("one in", offset=-0.1)
            self.allow_overlap(e_frac[1], e_pow, reason="fraction bar and the closing \\Big) "
                               "of the same typeset equation (TeX spacing)")
            self.play(TransformFromCopy(ysq, e_frac[0]), Create(e_frac[1]),
                      FadeIn(e_frac[2:], shift=0.4 * RIGHT),
                      A.grid.animate(rate_func=there_and_back).set_stroke(YELLOW, 2, 0.9),
                      run_time=1.3)
            beat.wait_until("To stay", offset=-0.1)
            self.play(Write(VGroup(e_P, e_word, e_close, e_eq, e_open)), run_time=1.0)
            beat.wait_until("all five", offset=-0.1)
            self.play(TransformFromCopy(A.hits[0], e_pow), run_time=1.1)

        # ============================================================ 7. guess
        Q = formula(r"\text{empty squares}", r"\approx", r"\ ?", size=FS)
        Q.move_to([RX, EL.get_center()[1], 0])
        Q[0].set_color(YELLOW)
        with self.say_beat("guess") as beat:
            self.play(Write(Q), run_time=1.0)

        # ============================================================ 8. empty
        L2 = formula(r"0.3933", r"\times", r"576", r"\approx", r"227", size=FS)
        L2.move_to(Q)
        L2[4].set_color(YELLOW)
        tE = ValueTracker(222)
        cntE = live_number(tE, 0, size=36, color=YELLOW, suffix=r"\text{empty}")
        A.below(cntE, RIGHT)
        tE.set_value(0)
        cntE[0].update()
        empties = A.cells_with(0)
        with self.say_beat("empty") as beat:
            # the answer arrives with its arithmetic: 0.3933, then 0.3933 x 576 ~ 227
            self.play(Write(e_val), FadeOut(Q, shift=0.15 * UP), run_time=0.6)
            self.play(TransformFromCopy(e_val[1:], L2[0]), Write(L2[1:]),
                      run_time=beat.until("squares", offset=-0.1, min_time=1.0))
            beat.wait_until("stay", offset=-0.2)
            self.add(cntE)
            self.play(LaggedStart(*[c.animate.set_fill(YELLOW, EMPTY_FILL) for c in empties],
                                  lag_ratio=0.01),
                      tE.animate.set_value(222), FadeOut(ysq),
                      run_time=beat.until("twenty-two", offset=0.2))
            A.yellow_empties = True
            self.play(flag(cntE, color=INK), run_time=0.8)

        # ============================================================ 9. gaps force clumps
        L3 = formula(r"\frac{537\ \text{hits}}{354\ \text{squares}}", r"\approx 1.5", size=FS)
        L3.move_to(L2)
        ge2_idx = [i for i, n in enumerate(A.counts) if n >= 2]
        ge2 = VGroup(*[A.outline(i, color=BLUE, width=3, z=2) for i in ge2_idx])
        t2 = ValueTracker(0)
        cnt2 = live_number(t2, 0, size=36, color=BLUE, suffix=r"\text{squares with 2+}")
        cnt2.move_to([RX, L2.get_center()[1] - 1.25, 0])
        with self.say_beat("gaps") as beat:
            cntE[0].clear_updaters()
            beat.wait_until("clumps", offset=-0.25)
            self.play(boxes.animate.set_stroke(opacity=1), run_time=0.8)
            beat.wait_until("three hundred", offset=-0.2)
            self.play(FadeOut(L2, shift=0.1 * UP), FadeIn(L3, shift=0.1 * UP), run_time=1.0)
            beat.wait_until("one and", offset=-0.15)
            self.play(flag(L3[1]), run_time=0.8)
            beat.wait_until("plenty", offset=-0.3)
            self.add(cnt2)
            # one focal layer: the 131 blue outlines and the dots; the yellow gaps step back
            # and the red 3+ outlines (a subset of the 2+) leave until the histogram
            self.play(LaggedStart(*[Create(b) for b in ge2], lag_ratio=0.02, rate_func=linear),
                      t2.animate(rate_func=linear).set_value(len(ge2_idx)),
                      boxes.animate.set_stroke(opacity=0), A.level_anim(1, 1, 1, 0),
                      run_time=beat.until("up", end=True, offset=0.1))
        assert len(ge2_idx) == 131

        # ============================================================ 10. lambda
        LAMB = formula(r"\lambda", "=", r"\frac{537}{576}", r"\approx 0.93", size=FS)
        LAMB.move_to([RX, 2.5, 0])
        LAMB[0].set_color(PURPLE)

        def dim_companions(f):
            # the map's labels step back with it; the 222-empty count goes; the red outlines
            # stay off (they left on "double up") and return with the map at the histogram
            boxes.set_stroke(opacity=max(0.0, (f - MAP_DIM) / (1 - MAP_DIM)))
            VGroup(A.top, tagA2).set_opacity(f)
            cntE.set_opacity(max(0.0, (f - MAP_DIM) / (1 - MAP_DIM)))

        with self.say_beat("lam") as beat:
            cnt2[0].clear_updaters()
            self.play(TransformFromCopy(A.hits[0], LAMB[2][0:3]), Create(LAMB[2][3]),
                      TransformFromCopy(e_frac[2:5], LAMB[2][4:7]), run_time=0.85)
            beat.wait_until("lambda", offset=-0.2)
            # the map steps back uniformly; only the one square stays lit
            ysq.set_stroke(opacity=1)
            self.play(Write(LAMB[0:2]), Write(LAMB[3]),
                      FadeOut(L3), FadeOut(ge2), FadeOut(cnt2),
                      A.level_anim(1, MAP_DIM, 0, 0, extra=dim_companions),
                      FadeIn(ysq), run_time=0.8)
            # second row copied from the first; 1/576 = lambda/537 is assembled from
            # lambda = 537/576 (lambda and 537 fly in from the definition)
            self.play(TransformFromCopy(e_eq, EL[0]), TransformFromCopy(e_open, EL[1]),
                      TransformFromCopy(e_pow, EL[3]), TransformFromCopy(LAMB[0], EL[2][0]),
                      TransformFromCopy(e_frac[1], EL[2][1]),
                      TransformFromCopy(LAMB[2][0:3], EL[2][2:5]),
                      run_time=beat.until("small", offset=-0.15, min_time=1.1))
            beat.wait_until("small slice", offset=-0.1)
            self.play(flag(e_frac), flag(EL[2]), run_time=0.8)
            beat.wait_until("big power", offset=-0.1)
            self.play(flag(EL[3][1:]), run_time=0.8)
            beat.wait_until("almost", offset=-0.1)
            self.play(Write(EL[4]), Write(EL[5]), run_time=0.9)
            self.play(Write(EL[6]), run_time=0.7)
            self.play(flag(e_val[1:], color=INK), flag(EL[6][1:], color=INK), run_time=0.8)

        # ============================================================ 11. two hits
        P0 = formula("P(", "0", ")", r"\approx", r"e^{-\lambda}", size=FS)
        P0.move_to([0.75, 2.95, 0])
        P0[4].set_color(PURPLE)
        P0_here = P0.copy()                            # P(0) written in place of P(empty)
        P0_here.shift(e_P.get_left() - P0_here[0].get_left())
        LAMB_T = LAMB.copy().move_to([4.55, 2.95, 0])
        # the 537 bombs, lined up as a block of dots (47 per row)
        ticks = VGroup(*[Dot([-0.5 + (i % 47) * 0.14, 2.2 - (i // 47) * 0.085, 0], radius=0.034,
                             color=INK, fill_opacity=0.8) for i in range(N)])
        bombs_lbl = Text("537 bombs", font_size=24, color=GRAY)
        bombs_lbl.next_to(ticks, DOWN, buff=0.12).align_to(ticks, RIGHT)
        bigsq = Square(1.3, stroke_color=YELLOW, stroke_width=4.5).move_to([0.35, 0.15, 0])
        pick2 = (150, 371)
        drop = [bigsq.get_center() + np.array([-0.28, 0.22, 0]),
                bigsq.get_center() + np.array([0.25, -0.2, 0])]
        hits2 = VGroup(*[Dot(p, radius=0.09, color=YELLOW) for p in drop]).set_z_index(3)
        # P(2) ~ 537*536/2! (1/576)^2 e^-lambda, written straight from the picture
        P2 = formula("P(", "2", ")", r"\approx", r"\frac{537\cdot 536}{2!}", r"\cdot",
                     r"\Big(\frac{1}{576}\Big)^{2}", r"\cdot", r"e^{-\lambda}", size=FS)
        P2.move_to([RX, -1.3, 0])
        P2[8].set_color(PURPLE)
        fr2 = P2[4]                                    # 537 [0:3]  . [3]  536 [4:7]  bar [7]  2! [8:10]
        rest = VGroup(*[t for i, t in enumerate(ticks) if i != pick2[0]])
        with self.say_beat("two") as beat:
            # the two empty-chance rows collapse to P(0) = e^-lambda; lambda moves beside it
            self.play(FadeOut(VGroup(e_eq, e_open, e_frac, e_pow, e_val, *EL[0:4], EL[6])),
                      ReplacementTransform(e_P, P0_here[0]),
                      ReplacementTransform(e_close, P0_here[2]),
                      FadeOut(e_word, shift=0.2 * UP), FadeIn(P0_here[1], shift=0.2 * UP),
                      ReplacementTransform(EL[4], P0_here[3]),
                      ReplacementTransform(EL[5], P0_here[4]), run_time=0.4)
            self.settle(P0_here)
            self.play(ReplacementTransform(P0_here, P0), Transform(LAMB, LAMB_T), run_time=0.45)
            beat.wait_until("pick", offset=-0.1)
            self.play(ReplacementTransform(A.dots.copy(), ticks), FadeIn(bombs_lbl), run_time=0.9)
            beat.wait_until("land here", offset=-0.2)
            self.play(TransformFromCopy(ysq, bigsq),
                      *[ticks[i].animate.set_fill(YELLOW, 1).scale(1.8) for i in pick2], run_time=0.6)
            self.play(*[TransformFromCopy(ticks[i], h) for i, h in zip(pick2, hits2)],
                      run_time=0.5)
            beat.wait_until("five thirty-seven", offset=-0.15)
            a_, g_ = self.ghost(ticks, fr2[0:3])
            self.play(Write(P2[0:4]), a_, run_time=0.7)
            self.land(g_, fr2[0:3])
            beat.wait_until("five thirty-six", offset=-0.15)
            a_, g_ = self.ghost(rest, fr2[4:7])
            self.play(FadeIn(fr2[3]), a_, run_time=0.7)
            self.land(g_, fr2[4:7])
            beat.wait_until("over two", offset=-0.1)
            a_, g_ = self.ghost(hits2, fr2[8])
            self.play(Create(fr2[7]), a_, FadeIn(fr2[9]), run_time=0.7)
            self.land(g_, fr2[8])
            beat.wait_until("Each", offset=-0.15)
            self.play(Write(P2[5]), run_time=0.5)
            beat.wait_until("one in", offset=-0.15)
            self.play(FadeTransform(bigsq.copy(), P2[6]), run_time=1.0)
            beat.wait_until("rest miss", offset=-0.1)
            self.play(Write(P2[7]), TransformFromCopy(P0[4], P2[8]), run_time=1.0)

        # ============================================================ 12. Poisson
        # 537*536 ~ 537^2, then every 2 becomes a k, one glyph at a time
        S = formula(r"537\cdot 536", r"\approx", r"537^{2}", size=36)
        S.next_to(P2, DOWN, buff=0.5).align_to(P2[4], LEFT).shift(0.3 * LEFT)
        S[0][4:7].set_color(YELLOW)

        def state(p, num, den, pk):
            m = formula("P(", p, ")", r"\approx", r"\frac{537^{%s}}{%s!}" % (num, den), r"\cdot",
                        r"\Big(\frac{1}{576}\Big)^{%s}" % pk, r"\cdot", r"e^{-\lambda}", size=FS)
            m[8].set_color(PURPLE)
            return m.move_to(P2).align_to(P2, LEFT)
        F1 = state("2", "2", "2", "2")
        F5 = state("k", "k", "k", "k")

        E5 = formula(r"P(k)", r"\approx", r"\frac{\lambda^{k}}{k!}", r"e^{-\lambda}", size=44)
        E5.move_to(F5)
        E5[3].set_color(PURPLE)
        E5[2][0:2].set_color(PURPLE)                   # lambda^k is the purple lambda
        E5_top = E5.copy().set_color(PURPLE)
        E5_top.move_to([0, EQ1_Y, 0]).align_to([-0.35, 0, 0], LEFT)
        pois = Text("Poisson", font_size=28, color=PURPLE).next_to(E5_top, RIGHT, buff=0.45)
        ax = axes((0, 6.2), (0, 400), x_length=6.0, y_length=2.75,
                  x_ticks=[k + X0 for k in range(6)], y_ticks=[0, 100, 200, 300, 400],
                  x_label="hits per square", y_label="squares", x_decimals=1)
        for k, num in enumerate(ax.x_axis.numbers):
            t = MathTex(r"5{+}" if k == 5 else str(k), font_size=MATH_SMALL, color=GRAY)
            num.become(t.move_to(num, aligned_edge=UP))
        grayify(ax)
        ax.shift(np.array([-0.2, -2.0, 0]) - ax.c2p(0, 0))
        pbars = exp_bars(ax)
        ins = inset_frame(ax)
        ipb = inset_exp(ax)
        p227 = formula("227", size=MATH_SMALL, color=PURPLE).next_to(pbars[0], UP, buff=0.18)
        ylab = formula(r"=", r"576\cdot P(k)", size=36)
        ylab[0].set_color(GRAY)
        ylab[1].set_color(PURPLE)
        ylab.next_to(ax.y_title, RIGHT, buff=0.18).align_to(ax.y_title, DOWN)
        picture = VGroup(ticks, bombs_lbl, bigsq, hits2)
        with self.say_beat("poisson") as beat:
            # "five thirty-six is almost five thirty-seven"
            self.play(TransformFromCopy(fr2[0:7], S[0]),
                      VGroup(ticks, bombs_lbl, hits2).animate.set_opacity(0.3),
                      bigsq.animate.set_stroke(opacity=0.3), run_time=1.0)
            beat.wait_until("almost", offset=-0.1)
            self.play(Write(S[1:]), run_time=0.6)
            beat.wait_until("five thirty-seven", offset=-0.1)
            self.play(flag(S[0][4:7]), flag(S[2]), run_time=0.8)
            # the numerator becomes 537^2: the "2" comes down from 537^2 below
            fn = F1[4]
            self.play(*[ReplacementTransform(P2[i], F1[i]) for i in range(9) if i != 4],
                      ReplacementTransform(fr2[0:3], fn[0:3]),
                      FadeOut(fr2[3:7], target_position=fn[3], scale=0.3),
                      TransformFromCopy(S[2][3], fn[3]),
                      ReplacementTransform(fr2[7:], fn[4:]), run_time=0.9)
            self.settle(F1)
            # "for any k": P(2) -> P(k); "each two becomes a k": the other three, in turn.  One
            # move, so the in-between (part-2, part-k) forms are only ever seen in motion.
            beat.wait_until("any k", offset=-0.15)
            t0 = beat.elapsed()
            starts = [0.1] + [beat.time_of("each") + 0.1 - t0 + 0.35 * i for i in range(3)]
            T = starts[-1] + 0.5
            changed = [(1, 0), (4, 3), (4, 5), (6, 7)]

            def win(a, d=0.5):
                return lambda t: smooth(min(1.0, max(0.0, (t * T - a) / d)))
            anims = []
            for i in range(len(F1)):
                for j in range(len(F1[i])):
                    if (i, j) in changed:
                        a = starts[changed.index((i, j))]
                        F5[i][j].set_color(YELLOW)
                        anims += [FadeOut(F1[i][j], shift=0.25 * UP, rate_func=win(a)),
                                  FadeIn(F5[i][j], shift=0.25 * UP, rate_func=win(a))]
                    else:
                        anims.append(ReplacementTransform(F1[i][j], F5[i][j], rate_func=win(0.1)))
            anims.append(FadeOut(S, rate_func=win(T - 0.5)))
            self.play(*anims, run_time=T)
            self.settle(F5)
            cur = F5
            Pk = cur
            beat.wait_until("powers", offset=-0.15)
            self.play(Pk[4][0:3].animate.set_color(YELLOW), Pk[6][3:6].animate.set_color(YELLOW),
                      LAMB[2].animate.set_color(YELLOW),
                      *[Pk[i][j].animate.set_color(INK) for i, j in changed], run_time=0.6)
            beat.wait_until("into lambda", offset=-0.1)
            self.play(ReplacementTransform(VGroup(*Pk[0], *Pk[1], *Pk[2]), E5[0]),
                      ReplacementTransform(Pk[3], E5[1]), ReplacementTransform(Pk[8], E5[3]),
                      ReplacementTransform(Pk[4][3], E5[2][1]),
                      ReplacementTransform(Pk[4][4:7], E5[2][2:5]),
                      FadeOut(VGroup(Pk[4][0:3], Pk[6], Pk[5], Pk[7]),
                              target_position=E5[2][0], scale=0.4),
                      TransformFromCopy(LAMB[0], E5[2][0]),
                      LAMB[2].animate.set_color(INK), run_time=1.3)
            self.settle(E5)
            beat.wait_until("Poisson", offset=-0.2)
            self.play(FadeOut(picture), FadeOut(P0), FadeOut(LAMB), run_time=0.5)
            self.play(Transform(E5, E5_top), FadeIn(pois, shift=0.1 * LEFT), run_time=0.9)
            beat.wait_until("Times", offset=-0.1)
            self.play(Create(ax), Create(ins), FadeIn(ylab[0]),
                      TransformFromCopy(E5[0], ylab[1]), run_time=0.9)
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in pbars], lag_ratio=0.15),
                      LaggedStart(*[GrowFromEdge(b, DOWN) for b in ipb], lag_ratio=0.15),
                      run_time=1.2)
            self.play(FadeIn(p227, shift=0.1 * UP), run_time=0.5)

        # ============================================================ 13. honest detector (A)
        bA = obs_bars(ax, H_A)
        ibA = inset_obs(ax, H_A)
        brace = Brace(ins.frame, UP, buff=0.1, color=RED)
        b39 = formula(r"39", r"\text{ targets}", size=36, color=RED)
        c39 = formula(r"\text{chance: }", r"39.3", size=36, color=PURPLE)
        c39.next_to(brace, UP, buff=0.18)
        b39.next_to(c39, UP, buff=0.12)
        # the misfit readout: chi^2 = sum gap^2/chance = [live]
        tM = ValueTracker(0)
        rd = formula(r"\chi^2", "=", r"\sum \text{gap}^2/\text{chance}", "=", size=36)
        rnum = DecimalNumber(0, num_decimal_places=1, font_size=36, color=YELLOW)
        rgrp = VGroup(rd, rnum).arrange(RIGHT, buff=0.18).move_to([RX + 0.25, 1.95, 0])
        rnum.add_updater(lambda m: m.set_value(tM.get_value()))
        slA = gap_slivers(ax, H_A)
        terms = VGroup(*[formula(t, size=MATH_SMALL, color=YELLOW) for t in PARTS_TXT])
        for k, t in enumerate(terms):
            t.move_to([bx(ax, k), 0.4, 0])
        pluses = VGroup(*[formula("+", size=MATH_SMALL, color=YELLOW)
                          .move_to([(bx(ax, k) + bx(ax, k + 1)) / 2, 0.4, 0]) for k in range(5)])
        # left: map A becomes one score among 20,000 simulated pure-chance maps
        mline = NumberLine(x_range=[0, MF_MAX, 1], length=MF_LEN, color=GRAY, stroke_width=2.5,
                           include_ticks=False).move_to([MF_X0 + MF_LEN / 2, MF_Y, 0])
        mticks = VGroup(*[Line([mfx(v), MF_Y - 0.06, 0], [mfx(v), MF_Y + 0.06, 0],
                               stroke_color=GRAY, stroke_width=2.5) for v in (0, 4, 8, 12, 16)])
        mnums = VGroup(*[formula(str(v), size=MATH_SMALL, color=GRAY)
                         .next_to([mfx(v), MF_Y, 0], DOWN, buff=0.18) for v in (0, 4, 8, 12, 16)])
        mtitle = Text("misfit", font_size=LABEL, color=GRAY)
        mtitle.next_to(mnums, DOWN, buff=0.15).align_to(mline, RIGHT)
        hist_n, _ = np.histogram(NULL, bins=np.arange(0, MF_MAX + 1))
        hscale = MF_H / hist_n.max()
        nbars = VGroup(*[Rectangle(width=MF_LEN / MF_MAX * 0.86, height=max(c * hscale, 0.004),
                                   stroke_width=0, fill_color=PURPLE, fill_opacity=0.55)
                         .move_to([mfx(k + 0.5), MF_Y, 0], aligned_edge=DOWN)
                         for k, c in enumerate(hist_n)])
        worse = VGroup(*nbars[2:])                     # bins from 2.0 up: scores worse than A
        mhead = VGroup(Text("20,000 chance maps", font_size=26, color=PURPLE),
                       Text("simulated", font_size=24, color=GRAY)).arrange(RIGHT, buff=0.2,
                                                                            aligned_edge=DOWN)
        mhead.move_to([MF_X0 + mhead.width / 2 - 0.1, 2.3, 0])
        thumb_c = np.array([mfx(2.0), 1.1, 0])
        mark = Line([mfx(2.0), MF_Y, 0], [mfx(2.0), thumb_c[1] - 0.6, 0], stroke_color=YELLOW,
                    stroke_width=4).set_z_index(3)
        alab = Text("A", font_size=32).next_to(thumb_c + 0.55 * RIGHT, RIGHT, buff=0.2)
        pval = formula(r"p = 0.74", size=MATH, color=PURPLE).move_to([mfx(10.0), -0.3, 0])
        thumb = VGroup(A.cells, A.frame, A.dots)
        with self.say_beat("fix") as beat:
            self.play(FadeOut(ylab), FadeOut(ysq),
                      A.level_anim(MAP_DIM, 1, 0, 1, extra=dim_companions), run_time=0.8)
            beat.wait_until("Map A", offset=-0.1)
            # ReplacementTransform from a copy keeps each bar a single rectangle (a
            # TransformFromCopy would leave ~200 stacked duplicates that defeat dimming)
            self.play(LaggedStart(*[ReplacementTransform(A.cells_with(k).copy(), bA[k])
                                    for k in range(6)], lag_ratio=0.12),
                      run_time=max(1.6, beat.until("thirty-nine", offset=-0.25)))
            # swap the morphed bars (which carry 222 aligned sub-paths each) for clean ones
            clean = obs_bars(ax, H_A)
            self.remove(*bA)
            for k in range(6):
                bA.submobjects[k] = clean[k]
            self.add(*bA)
            self.play(*[TransformFromCopy(bA[k], ibA[i]) for i, k in enumerate((3, 4, 5))],
                      GrowFromCenter(brace), FadeIn(b39, shift=0.1 * DOWN), run_time=0.9)
            beat.wait_until("chance predicts", offset=-0.15)
            self.play(TransformFromCopy(ipb, c39[1]), FadeIn(c39[0]), run_time=1.0)
            beat.wait_until("chi", offset=-0.15)

            def dim_all(f):                        # labels and outlines dim with the map
                boxes.set_stroke(opacity=f)
                VGroup(A.top, tagA2, cntE).set_opacity(f)
            # the map steps back: the yellow gap slivers become the only full-strength yellow
            self.play(Write(rd), FadeIn(rnum),
                      A.level_anim(1, MAP_LOW, 1, 0, extra=dim_all, rate_func=window(0, 0.67)),
                      run_time=0.9)
            beat.wait_until("square", offset=-0.2)
            self.play(FadeOut(VGroup(brace, b39, c39)), run_time=0.5)
            beat.wait_until("gap", offset=-0.2)
            self.play(LaggedStart(*[GrowFromCenter(r) for r in slA], lag_ratio=0.1), run_time=0.6)
            beat.wait_until("divide", offset=-0.1)
            self.play(*[TransformFromCopy(slA[k], terms[k]) for k in range(6)],
                      FadeIn(pluses), flag(VGroup(pbars, ipb), color=INK), run_time=1.0)
            beat.wait_until("add", offset=-0.15)
            self.play(*[FadeOut(t.copy(), target_position=rnum.get_center(), scale=0.6)
                        for t in terms],
                      tM.animate.set_value(sum(PARTS_A)), run_time=1.1)
            beat.wait_until("scores", offset=-0.1)
            self.play(flag(rnum, color=INK), FadeOut(VGroup(A.top, tagA2, cntE, boxes, A.grid)),
                      run_time=0.8)
            beat.wait_until("Pure", offset=-0.3)
            # map A comes back to full strength as it shrinks into one score among many
            self.play(FadeOut(VGroup(terms, pluses, slA)),
                      thumb.animate.scale_to_fit_width(1.1).move_to(thumb_c),
                      UpdateFromAlphaFunc(thumb, lambda m, a: A.set_level(
                          MAP_LOW + (1 - MAP_LOW) * a, a)),
                      Create(mline), FadeIn(mticks), FadeIn(mnums), FadeIn(mtitle),
                      FadeIn(mhead), run_time=0.9)
            self.play(Create(mark), FadeIn(alab),
                      LaggedStart(*[GrowFromEdge(b, DOWN) for b in nbars], lag_ratio=0.04),
                      run_time=beat.until("three", offset=-0.1, min_time=0.9))
            self.play(worse.animate.set_fill(opacity=0.95),
                      VGroup(*nbars[:2]).animate.set_fill(opacity=0.25), run_time=0.7)
            beat.wait_until("p equals", offset=-0.1)
            a_, g_ = self.ghost(worse, pval)
            self.play(a_, run_time=0.9)
            self.land(g_, pval)

        # ============================================================ 13b. map B
        zeros = obs_bars(ax, H_B)
        izeros = inset_obs(ax, H_B)
        l109 = formula("109", size=MATH_SMALL, color=BLUE).next_to(zeros[0], UP, buff=0.18)
        l397 = formula("397", size=MATH_SMALL, color=BLUE).next_to(zeros[1], UP, buff=0.18)
        slB = gap_slivers(ax, H_B)
        b_y = MF_Y + 0.45
        barr = Arrow([mfx(MF_MAX) + 0.05, b_y, 0], [mfx(MF_MAX) + 0.75, b_y, 0], buff=0,
                     color=INK, stroke_width=4, max_tip_length_to_length_ratio=0.3)
        blab = formula(r"\text{B: }", r"271.7", size=36)
        blab.next_to(barr, UP, buff=0.15).align_to(barr, RIGHT)
        # map B's own thumbnail beside A's, so B's bars have a named referent
        Bt = Panel(PTS_B, CNT_B, "B", P2_SIDE, ORIGIN)
        for i, c in enumerate(Bt.cells):
            if Bt.counts[i] == 0:
                c.set_fill(YELLOW, EMPTY_FILL)
            else:
                c.set_fill(BLUE, shade(Bt.counts[i]))
        bthumb = VGroup(Bt.cells, Bt.frame, Bt.dots)
        bthumb.scale(A.frame.width / Bt.frame.width)
        bthumb.next_to(alab, RIGHT, buff=0.45).align_to(A.frame, DOWN)
        blt = Text("B", font_size=32).next_to(bthumb, RIGHT, buff=0.2).align_to(alab, DOWN)
        a_side = VGroup(alab, mark, pval)

        def a_level(f):
            A.set_level(f, (f - MAP_LOW) / (1 - MAP_LOW))   # yellow leaves rather than going olive
            a_side.set_opacity(f)
        with self.say_beat("fixb") as beat:
            rnum.clear_updaters()
            self.play(Transform(bA, zeros), Transform(ibA, izeros),
                      FadeIn(bthumb), FadeIn(blt),
                      UpdateFromAlphaFunc(thumb, lambda m, a: a_level(1 - (1 - MAP_LOW) * a),
                                          rate_func=window(0, 0.6)), run_time=0.85)
            beat.wait_until("half", offset=-0.15)
            self.play(FadeIn(l109, shift=0.1 * UP), flag(bA[0]), run_time=0.9)
            beat.wait_until("tower", offset=-0.15)
            self.play(FadeIn(l397, shift=0.1 * UP), flag(bA[1]), run_time=0.9)
            beat.wait_until("misfit", offset=-0.2)
            rnum.add_updater(lambda m: m.set_value(tM.get_value()))
            self.play(LaggedStart(*[GrowFromCenter(r) for r in slB], lag_ratio=0.08),
                      FadeOut(l109), FadeOut(l397), tM.animate.set_value(MIS_B),
                      run_time=beat.until("seventy-two", end=True, offset=-0.1))
            rnum.clear_updaters()
            self.play(GrowArrow(barr), FadeIn(blab[0]), TransformFromCopy(rnum, blab[1]),
                      UpdateFromAlphaFunc(thumb, lambda m, a: a_level(MAP_LOW + (1 - MAP_LOW) * a)),
                      run_time=0.8)
            beat.wait_until("pattern", offset=-0.2)
            self.play(FadeOut(slB), run_time=0.5)
            beat.wait_until("fingerprint", offset=-0.2)
            self.play(flag(VGroup(blab, barr)), run_time=0.9)

        # ============================================================ 14. aim, Clarke + real map
        flat, iflat = obs_bars(ax, [0] * 6), inset_obs(ax, [0] * 6)
        abars = VGroup(*[bar(ax, k, v, 0.5, stroke_color=RED, stroke_width=3.5, fill_opacity=0)
                         .set_z_index(3) for k, v in enumerate(H_AIM)])
        left_panel = VGroup(thumb, alab, mark, mline, mticks, mnums, mtitle, nbars, mhead, pval,
                            barr, blab, bthumb, blt)
        # the simulated aimed map itself, in the left slot: 537 hits around 3 aim points
        acell = P2_SIDE / G
        aframe = Square(P2_SIDE, stroke_color=GRAY, stroke_width=2.5).move_to(P2_C)
        a_o = aframe.get_corner(DL)
        adots = VGroup(*[Dot(a_o + [p_[0] * acell, p_[1] * acell, 0], radius=0.054, color=INK)
                         for p_ in PTS_AIM]).set_z_index(1)
        adots.set_opacity(0)
        aims = VGroup(*[VGroup(Line(LEFT, RIGHT), Line(DOWN, UP)).scale(0.16).rotate(PI / 4)
                        .set_stroke(RED, 5).move_to(a_o + [q[0] * acell, q[1] * acell, 0])
                        .set_z_index(2) for q in _D["aims"]])
        ahead = VGroup(Text("aimed", font_size=40, color=RED),
                       Text("simulated", font_size=24, color=GRAY)).arrange(RIGHT, buff=0.22,
                                                                            aligned_edge=DOWN)
        ahead.next_to(aframe, UP, buff=0.2).align_to(aframe, LEFT)
        aim_t = ValueTracker(0)
        ahits = live_number(aim_t, 0, size=36, suffix=r"\text{hits}")
        ahits[-1].set_color(GRAY)
        ahits.next_to(aframe, UP, buff=0.2).align_to(aframe, RIGHT)
        assert ahits.get_left()[0] - ahead.get_right()[0] > 0.3
        aimed_map = VGroup(aframe, adots, aims, ahead, ahits)

        def rain_aim(m, a):
            n = a * N
            for i, d in enumerate(adots):
                d.set_opacity(float(np.clip(n - i, 0, 1)))
            aim_t.set_value(min(N, int(n)))

        def inset_level(f):
            ins.frame.set_stroke(opacity=f)
            ins[1].set_stroke(opacity=f)
            ins.lbl.set_opacity(f)
            ipb.set_stroke(opacity=f).set_fill(opacity=0.14 * f)

        def inset_anim(f0, f1):
            return UpdateFromAlphaFunc(ins, lambda m, a: inset_level(f0 + (f1 - f0) * a))
        shift3 = np.array([0.3, 0.95, 0])
        hist_grp = VGroup(ax, pbars, bA, ins, ipb, ibA)
        cite3 = cite("map: Shaw & Shaw, 2019 · Significance 16(5)", size=18)
        cite2 = cite("R. D. Clarke, 1946 · J. Inst. Actuaries 72:481", size=18)
        for c_ in (cite2, cite3):
            c_.align_to([-SAFE_X, 0, 0], LEFT)
        cite3.next_to(cite2, UP, buff=0.18, aligned_edge=LEFT)
        # the real map
        rdots = VGroup(*[Dot(rm(e, n), radius=RDOT, color=INK) for e, n in REAL])
        rdots.set_opacity(0)
        rtitle = Text("real V-1 hits, 1944–45", font_size=26).move_to([-4.6, 2.95, 0])
        rtitle.align_to(rm(RM_E0, 0), LEFT)
        th = THAMES[THAMES[:, 0] <= 548.0]
        river = VMobject(stroke_color=GRAY, stroke_width=4, stroke_opacity=0.85)
        river.set_points_as_corners([rm(e, n) for e, n in th]).set_z_index(2)
        c0, c1 = rm(CBOX[0], CBOX[2]), rm(CBOX[1], CBOX[3])
        cbox = Rectangle(width=c1[0] - c0[0], height=c1[1] - c0[1], stroke_color=YELLOW,
                         stroke_width=3.5).move_to((c0 + c1) / 2).set_z_index(3)
        nx, ny = int(round((CBOX[1] - CBOX[0]) * 2)), int(round((CBOX[3] - CBOX[2]) * 2))
        cw = (c1[0] - c0[0]) / nx
        cgrid = VGroup(*[Line([c0[0] + i * cw, c0[1], 0], [c0[0] + i * cw, c1[1], 0])
                         for i in range(1, nx)],
                       *[Line([c0[0], c0[1] + j * cw, 0], [c1[0], c0[1] + j * cw, 0])
                         for j in range(1, ny)]).set_stroke(YELLOW, 1.0, 0.5).set_z_index(2)
        assert nx * ny == 576
        in_c = (REAL[:, 0] > CBOX[0]) & (REAL[:, 0] < CBOX[1]) & (REAL[:, 1] > CBOX[2]) & \
               (REAL[:, 1] < CBOX[3])
        in_n = (REAL[:, 0] > NBOX[0]) & (REAL[:, 0] < NBOX[1]) & (REAL[:, 1] > NBOX[2]) & \
               (REAL[:, 1] < NBOX[3])
        outside = VGroup(*[d for d, f in zip(rdots, in_c) if not f])
        north_dots = VGroup(*[d for d, f in zip(rdots, in_n) if f])
        clbl = formula(r"\approx\text{ Clarke's area}", size=36, color=YELLOW)
        clbl.next_to(cbox, DOWN, buff=0.15).set_y(-2.08).align_to(cbox, LEFT)
        # Clarke never published where his grid was: this rectangle is Shaw & Shaw's re-creation
        recr = Text("re-created", font_size=24, color=GRAY)
        recr.next_to(clbl, RIGHT, buff=0.25).align_to(clbl, DOWN)
        # "Thames" label at the river's east end, in open ground: no knockout, >= 0.2 from
        # every hit, 0.15-0.4 from the river, clear of both boxes and of the chart
        tl = Text("Thames", font_size=26, color=GRAY)
        q = np.array([rm(a, b) for a, b in REAL])
        rpts = np.array([rm(e, n) for e, n in th])
        rs = np.concatenate([np.linspace(a_, b_, 8, endpoint=False)
                             for a_, b_ in zip(rpts[:-1], rpts[1:])] + [rpts[-1:]])
        n0_, n1_ = rm(NBOX[0], NBOX[2]), rm(NBOX[1], NBOX[3])
        hw, hh = tl.width / 2, tl.height / 2

        def rect_gap(cx, cy, P):
            return np.hypot(np.maximum(np.abs(P[:, 0] - cx) - hw, 0),
                            np.maximum(np.abs(P[:, 1] - cy) - hh, 0))

        def box_gap(cx, cy, b0, b1):
            gx = max(b0[0] - (cx + hw), (cx - hw) - b1[0], 0)
            gy = max(b0[1] - (cy + hh), (cy - hh) - b1[1], 0)
            return np.hypot(gx, gy)
        best = None
        for cx in np.arange(-3.0, -0.7, 0.02):
            for cy in np.arange(-0.6, 1.6, 0.02):
                if cx + hw > -1.3:
                    continue
                if rect_gap(cx, cy, q).min() - RDOT < 0.2:
                    continue
                dr = rect_gap(cx, cy, rs).min()
                if not 0.15 <= dr <= 0.4:
                    continue
                if box_gap(cx, cy, c0, c1) < 0.2 or box_gap(cx, cy, n0_, n1_) < 0.2:
                    continue
                d_end = np.hypot(cx - rpts[-1][0], cy - rpts[-1][1])
                if best is None or d_end < best[0]:
                    best = (d_end, cx, cy)
        assert best is not None
        tl.move_to([best[1], best[2], 0]).set_z_index(4)

        def rain_real(m, a):
            n = a * len(rdots)
            for i, d in enumerate(rdots):
                d.set_opacity(float(np.clip(n - i, 0, 1)))

        with self.say_beat("clarke") as beat:
            self.play(FadeOut(p227), FadeOut(rgrp),
                      Transform(bA, flat), Transform(ibA, iflat),
                      FadeOut(left_panel, shift=0.4 * LEFT), inset_anim(1, MAP_DIM),
                      run_time=0.6)
            # as in the cold open: frame, header and counter first, then the hits rain in
            self.play(Create(aframe), FadeIn(ahead), FadeIn(ahits), run_time=0.5)
            self.add(adots)
            self.play(UpdateFromAlphaFunc(adots, rain_aim, rate_func=linear),
                      run_time=beat.until("empty", offset=-0.2, min_time=1.0))
            ahits[0].clear_updaters()
            beat.wait_until("empty", offset=-0.2)
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in abars[:3]], lag_ratio=0.2),
                      run_time=0.9)
            beat.wait_until("pile", offset=-0.2)
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in abars[3:]], lag_ratio=0.2),
                      LaggedStart(*[GrowFromCenter(x) for x in aims], lag_ratio=0.2),
                      run_time=0.9)
            beat.wait_until("nineteen", offset=-0.1)
            self.play(FadeOut(abars), FadeOut(aimed_map, shift=0.4 * LEFT),
                      hist_grp.animate.shift(shift3),
                      inset_anim(MAP_DIM, 1), run_time=1.0)
            self.add(rdots)
            self.play(FadeIn(cite2, shift=0.1 * UP), FadeIn(cite3),
                      UpdateFromAlphaFunc(rdots, rain_real), rate_func=linear,
                      run_time=beat.until("real", offset=-0.1))
            self.play(FadeIn(rtitle, shift=0.1 * DOWN), Create(river), FadeIn(tl), run_time=1.0)
            beat.wait_until("five hundred", offset=-0.2)
            self.play(Create(cbox), run_time=0.9)
            beat.wait_until("five seventy-six", offset=-0.2)
            self.play(Create(cgrid), outside.animate.set_opacity(0.35), run_time=1.0)
            beat.wait_until("south", offset=-0.2)
            self.play(FadeIn(clbl, shift=0.1 * UP), FadeIn(recr, shift=0.1 * UP), run_time=0.7)

        # ============================================================ 15. London's table
        rowP = VGroup(*[formula(t, size=MATH_SMALL, color=PURPLE) for t in EXP_TXT])
        rowB = VGroup(*[formula(str(v), size=MATH_SMALL, color=BLUE) for v in CLARKE])
        y_p = ax.x_title.get_bottom()[1] - 0.36
        for k in range(6):
            rowP[k].move_to([bx(ax, k), y_p, 0])
            rowB[k].move_to([bx(ax, k), y_p - 0.45, 0])
        hdrP = Text("chance", font_size=24, color=PURPLE)
        hdrB = Text("Clarke", font_size=24, color=BLUE)
        for h, r in ((hdrP, rowP), (hdrB, rowB)):
            h.next_to(r[0], LEFT, buff=0.22)
            h.align_to(rowB[0].get_left() + 0.22 * LEFT, RIGHT).set_y(r[0].get_y())
        lond, ilond = obs_bars(ax, CLARKE), inset_obs(ax, CLARKE)
        rL = formula(r"\chi^2 = 1.17,", r"\ \ p = 0.88", size=36)
        rL.next_to(E5, RIGHT, buff=0.5).align_to(E5[0], DOWN)
        assert rL.get_right()[0] < SAFE_X - 0.05, rL.get_right()
        with self.say_beat("london") as beat:
            self.play(FadeIn(hdrP),
                      LaggedStart(*[TransformFromCopy(pbars[k], rowP[k]) for k in range(6)],
                                  lag_ratio=0.1), run_time=beat.until("two hundred", offset=-0.1))
            self.play(flag(rowP[0]), run_time=0.8)
            beat.wait_until("Clarke counted", offset=-0.1)
            self.play(Transform(bA[0], lond[0]), FadeIn(rowB[0], shift=0.1 * UP), FadeIn(hdrB),
                      run_time=0.9)
            beat.wait_until("Single", offset=-0.2)
            self.play(flag(rowP[1]), run_time=0.8)
            beat.wait_until("eleven", offset=-0.1)
            self.play(Transform(bA[1], lond[1]), FadeIn(rowB[1], shift=0.1 * UP), run_time=0.9)
            self.play(LaggedStart(*[AnimationGroup(Transform(bA[k], lond[k]),
                                                   FadeIn(rowB[k], shift=0.1 * UP))
                                    for k in range(2, 6)], lag_ratio=0.25),
                      Transform(ibA, ilond),
                      run_time=beat.until("Same", offset=-0.1))
            self.play(FadeOut(pois), FadeIn(rL[0], shift=0.1 * UP), run_time=0.6)
            beat.wait_until("p equals", offset=-0.1)
            self.play(Write(rL[1]), run_time=0.8)
            beat.wait_until("No sign", offset=-0.1)
            self.play(flag(rL[1], color=INK), run_time=0.8)

        # ============================================================ 16. limits
        sb0 = np.array([rtitle.get_right()[0] + 0.5, rtitle.get_bottom()[1] + 0.04, 0])
        sbar = VGroup(Line(sb0, sb0 + 5 * RM_S * RIGHT, stroke_color=INK, stroke_width=3),
                      Line(sb0 + 0.07 * DOWN, sb0 + 0.07 * UP, stroke_color=INK, stroke_width=3),
                      Line(sb0 + 5 * RM_S * RIGHT + 0.07 * DOWN, sb0 + 5 * RM_S * RIGHT + 0.07 * UP,
                           stroke_color=INK, stroke_width=3))
        sb_lbl = Text("5 km", font_size=24, color=INK).next_to(sbar, UP, buff=0.14)
        assert sbar.get_right()[0] < E5.get_left()[0] - 0.5
        n0, n1 = rm(NBOX[0], NBOX[2]), rm(NBOX[1], NBOX[3])
        nbox = Rectangle(width=n1[0] - n0[0], height=n1[1] - n0[1], stroke_color=INK,
                         stroke_width=4)
        nbox.move_to((n0 + n1) / 2).set_z_index(3)
        dn = formula(r"\text{north: }1.9\ \text{hits/km}^2", size=36)
        dn.next_to(nbox, UP, buff=0.15).align_to(nbox, LEFT)
        # left-aligned on the box, lifted only as far as the hits above the box require
        span = (q[:, 0] > dn.get_left()[0] - 0.2) & (q[:, 0] < dn.get_right()[0] + 0.2)
        dn.set_y(max(dn.get_y(), q[span, 1].max() + RDOT + 0.17 + dn.height / 2))
        assert dn.get_top()[1] < rtitle.get_bottom()[1] - 0.15
        dc = formula(r"\approx\text{ Clarke's area}", r"\text{: }3.7\ \text{hits/km}^2", size=36,
                     color=YELLOW)
        dc.move_to(clbl).align_to([-6.3, 0, 0], LEFT)
        cite4 = cite("hits/km²: our count · L. Shaw, 2025 · Zenodo", size=18)
        cite4.move_to(cite2, aligned_edge=LEFT)
        with self.say_beat("limit") as beat:
            self.play(ax.animate.set_opacity(0.35),
                      VGroup(ins.frame, ins[1]).animate.set_stroke(opacity=0.35),
                      ins.lbl.animate.set_opacity(0.35),
                      VGroup(pbars, ipb).animate.set_stroke(opacity=0.35).set_fill(opacity=0.06),
                      *[b.animate.set_fill(opacity=0.3) for b in (*bA, *ibA)],
                      VGroup(rowP, rowB, hdrP, hdrB, rL).animate.set_opacity(0.35),
                      run_time=0.8)
            beat.wait_until("aimed at", offset=-0.2)
            self.play(flag(rdots), run_time=0.9)
            beat.wait_until("loosely", offset=-0.2)
            self.play(Create(sbar), FadeIn(sb_lbl), run_time=0.9)
            beat.wait_until("one lambda", offset=-0.2)
            self.play(flag(E5[2][0]), flag(E5[3]), run_time=0.9)
            beat.wait_until("farther", offset=-0.25)
            self.play(Create(nbox), north_dots.animate.set_opacity(1), run_time=0.7)
            self.play(flag(nbox), run_time=0.7)
            beat.wait_until("half", offset=-0.2)
            self.play(FadeIn(dn, shift=0.1 * DOWN), FadeOut(cite2), FadeIn(cite4), run_time=0.7)
            beat.wait_until("Clarke chose", offset=-0.15)
            self.play(cbox.animate(rate_func=there_and_back).set_stroke(width=8),
                      FadeOut(recr, rate_func=window(0, 0.35)),
                      clbl.animate(rate_func=window(0.2, 0.45)).move_to(dc[0]),
                      FadeIn(dc[1], shift=0.1 * LEFT, rate_func=window(0.6, 0.4)), run_time=1.2)

        # ============================================================ 17. landing
        A2 = Panel(PTS_A, CNT_A, "A", P1_SIDE, P1_A)
        B2 = Panel(PTS_B, CNT_B, "B", P1_SIDE, P1_B)
        tagA3 = A2.below(Text("pure chance", font_size=26, color=PURPLE))
        tagB3 = B2.below(formula(r"\text{rule: gap}", r"\ge", r"\tfrac{4}{5}",
                                 r"\text{ square}", size=36))
        circles2 = VGroup(*[Circle(radius=A2.cellsize * 1.35, stroke_color=YELLOW,
                                   stroke_width=3).move_to(A2.cells[i]) for i in big]).set_z_index(2)
        # the 0:39 detector outlines, redrawn
        red3 = VGroup(*[A2.outline(i, z=3) for i in tgt_idx])
        # map A's hits start inside Clarke's area, at the real dots' size, then the area
        # opens out into map A's frame
        f0, f1 = A2.frame.get_corner(DL), A2.frame.get_corner(UR)
        k0, k1 = cbox.get_corner(DL), cbox.get_corner(UR)
        sq_x, sq_y = (k1[0] - k0[0]) / (f1[0] - f0[0]), (k1[1] - k0[1]) / (f1[1] - f0[1])
        adots0 = VGroup(*[Dot([k0[0] + (d.get_x() - f0[0]) * sq_x,
                               k0[1] + (d.get_y() - f0[1]) * sq_y, 0], radius=RDOT, color=INK)
                          for d in A2.dots]).set_z_index(1)
        base_op = [d.get_fill_opacity() for d in rdots]
        keep = {id(m) for m in (cbox, *rdots.get_family())}

        def cross(m, a):
            # A's hits reach half strength before London's drop below it
            fa = smooth(min(1.0, a / 0.6))
            fl = 1 - smooth(min(1.0, max(0.0, (a - 0.35) / 0.65)))
            adots0.set_opacity(fa)
            for d, b in zip(rdots, base_op):
                d.set_opacity(b * fl)
        adots0.set_opacity(0)
        B2.dots.set_opacity(1)
        b2grp = VGroup(B2.frame, B2.dots, B2.top)
        b2grp.shift(8 * RIGHT)
        with self.say_beat("landing") as beat:
            self.add(adots0)
            # everything else leaves; groups that hold real dots (e.g. the dimmed
            # "outside" set) stay and are faded by cross() through their dots
            self.play(*[FadeOut(m) for m in list(self.mobjects)
                        if m is not adots0 and not any(id(x) in keep for x in m.get_family())],
                      UpdateFromAlphaFunc(VGroup(adots0, rdots), cross), run_time=0.8)
            self.play(ReplacementTransform(cbox, A2.frame), ReplacementTransform(adots0, A2.dots),
                      FadeIn(A2.top, shift=0.1 * DOWN), b2grp.animate.shift(8 * LEFT),
                      run_time=1.3)
            beat.wait_until("clumps", offset=-0.25)
            self.play(LaggedStart(*[Create(c) for c in circles2], lag_ratio=0.25),
                      FadeIn(tagA3, shift=0.1 * UP), run_time=1.1)
            beat.wait_until("no aim", offset=-0.2)
            self.play(LaggedStart(*[Create(b) for b in red3], lag_ratio=0.02), run_time=1.0)
            beat.wait_until("map B", offset=-0.2)
            self.play(FadeIn(tagB3, shift=0.1 * UP), run_time=0.7)
            beat.wait_until("rule", offset=-0.2)
            self.play(B2.frame.animate(rate_func=there_and_back).set_stroke(YELLOW, width=6),
                      flag(tagB3), run_time=0.8)

        self.end_card()
