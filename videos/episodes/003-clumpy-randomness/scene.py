"""Sample Space, episode 3: Which Map Is Pure Chance?

Two simulated maps of 537 hits: which one is pure chance?  A "hot-spot" detector (flag any
square with 3+ hits) agrees with the eye and gets it backwards: 39 false alarms on the truly
random map, none on the rule-based even one.  One square's chance of staying empty,
(1 - 1/576)^537 = 0.3933, explains why chance leaves gaps, and gaps force clumps; the same
counting (pick k bombs in, the rest out) gives the Poisson formula, whose bars are the honest
detector: the chi-squared misfit (sum of gap^2/chance) is 2.0 for A - three in four of 20,000
simulated pure-chance maps score worse - and 271.7 for B.  Simulated aim fails the other way.
Payoff: R. D. Clarke's 1946 flying-bomb table for south London on the real V-1 map (Shaw &
Shaw's digitised LCC data, the Thames from OS Open Rivers); limit, measured: the bombs fell
short of Tower Bridge, so farther north the hits were half as dense, yet the north box scored
alone fits chance too (p = 0.45) - the aim shows only in lambda, which the test holds fixed.

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
from narration_text import B, BEAT_GAP_AFTER, BEAT_SPEED, CADENCE, PRON, SPEED   # noqa: E402

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
EMPTY_FILL = 0.0                                   # empty squares: a full-yellow outline of each
                                                   # empty region, no fill (a yellow tint under 60 %
                                                   # reads olive on the slate background)
EMPTY_EDGE = 2.6                                   # its stroke width
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
MF_X0, MF_LEN, MF_MAX, MF_Y = -5.3, 3.0, 16, -1.85   # room on the left for the "maps" label
MF_H = 2.0
# Tower Bridge, the V-1 campaign's nominal aiming point (Evans & Delaney 2018), BNG km
# (OS grid reference TQ 336 802); half the V-1s fell more than 12.5 km from it (their CEP-T)
TOWER_BRIDGE = (533.6, 180.2)
# their overall mean point of impact (2,111 V-1s, June-August 1944) lay "in Dulwich": drawn at
# Dulwich Village, OS grid TQ 333 735 (approximate: the paper names the district, not a point)
DULWICH = (533.3, 173.5)
RS = 1.35                                          # real map scale-up for the limits beat


def rm(e, n):
    return np.array([RM_X0 + (e - RM_E0) * RM_S, RM_Y0 + (n - RM_N0) * RM_S, 0.0])


def mfx(v):
    return MF_X0 + v / MF_MAX * MF_LEN


def shade(c: int) -> float:
    return SHADE[min(int(c), 5)]


def flag(m: Mobject, color=YELLOW, run_time: float = 0.8, **kw):
    """Colour-only flag (no scaling, so a flagged frame/bar never grows into its labels)."""
    return Indicate(m, color=color, scale_factor=1.0, run_time=min(run_time, 1.0), **kw)


def ring_flash(m: Mobject, color=INK, run_time: float = 0.8):
    """A 'look here' that leaves the object's fill alone: an outline draws round it and fades."""
    return Circumscribe(m, Rectangle, color=color, buff=0.06, stroke_width=4, fade_out=True,
                        run_time=run_time)


def window(a: float, d: float):
    """Rate function that runs smoothly from alpha a to a + d of its animation (0 before,
    1 after): lets one animation inside a longer play() start late."""
    return lambda t: smooth(min(1.0, max(0.0, (t - a) / d)))


def tb_window(a: float, d: float):
    """there_and_back run between alpha a and a + d of a longer animation (for a flag that
    starts late inside a play)."""
    return lambda t: there_and_back(min(1.0, max(0.0, (t - a) / d)))


def grayify(ax: Axes) -> Axes:
    """Series axes, with tick numbers and titles in this episode's lighter GRAY."""
    for m in (ax.x_axis.numbers, ax.y_axis.numbers, ax.x_title, ax.y_title):
        if m is not None:
            m.set_color(GRAY)
    return ax


def cite(s: str, size: float = 22) -> Text:
    """Bottom-left source line.  Not shrunk to fit (the series helper fits to 75 % of the safe
    width, which took round 1's two-source line below the 24 px citation minimum)."""
    m = Text(s, font=SERIF, font_size=size, color=GRAY)
    m.ss_role = "citation"                       # held to the 24 px citation floor
    assert m.width <= 2 * SAFE_X, (s, m.width)
    return m.move_to([-SAFE_X + m.width / 2, CONTENT_BOTTOM + 0.08 + m.height / 2, 0])


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
        self.sim = Text("simulated", font_size=27, color=GRAY)   # the narration names it
        self.sim.next_to(self.name, RIGHT, buff=0.22, aligned_edge=DOWN)
        self.hits_t = ValueTracker(N)
        self.hits = live_number(self.hits_t, 0, size=36, suffix=r"\text{hits}")
        self.hits[-1].set_color(GRAY)
        self.hits.next_to(self.frame, UP, buff=0.2).align_to(self.frame, RIGHT)
        self.top = VGroup(self.name, self.sim, self.hits)
        self.pts = pts
        self.yellow_empties = False                  # set once the empty squares are filled
        self.edges = None                            # yellow outline of the empty regions
        self.cell_k = 1.0                            # extra factor on the blue count shading

    def where(self, k: int) -> list[int]:
        """Cell indices with exactly k hits (k=5 means 5 or more)."""
        return [i for i, c in enumerate(self.counts) if (c >= 5 if k == 5 else c == k)]

    def cells_with(self, k: int) -> VGroup:
        return VGroup(*[self.cells[i] for i in self.where(k)])

    def empty_edges(self, color=YELLOW, width: float = EMPTY_EDGE) -> VMobject:
        """Outline of every connected region of empty squares: the cell edges that separate an
        empty square from a hit square (no inner grid lines).  Edges on the map's border are
        left to the GRAY frame, so the frame never turns yellow."""
        cell = self.frame.width / G                  # the map may have been rescaled
        o = self.frame.get_corner(DL)
        empty = {(i, j) for i in range(G) for j in range(G) if self.counts[i * G + j] == 0}
        m = VMobject(stroke_color=color, stroke_width=width).set_z_index(2)
        for i, j in empty:
            for di, dj, a, b in ((-1, 0, (0, 0), (0, 1)), (1, 0, (1, 0), (1, 1)),
                                 (0, -1, (0, 0), (1, 0)), (0, 1, (0, 1), (1, 1))):
                ni, nj = i + di, j + dj
                if not (0 <= ni < G and 0 <= nj < G):
                    continue
                if (ni, nj) not in empty:
                    p0 = o + np.array([(i + a[0]) * cell, (j + a[1]) * cell, 0])
                    p1 = o + np.array([(i + b[0]) * cell, (j + b[1]) * cell, 0])
                    m.start_new_path(p0)
                    m.add_line_to(p1)
        return m

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
                c.set_fill(BLUE, shade(self.counts[i]) * f * self.cell_k)
        if self.edges is not None:
            self.edges.set_stroke(opacity=yellow if self.yellow_empties else 0.0)
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
    TITLE = "Which Map Is Pure Chance?"
    PRONUNCIATIONS = PRON
    SPEED = SPEED
    CADENCE = CADENCE

    def say_beat(self, key: str):
        return self.narrate(B[key], speed=BEAT_SPEED.get(key), gap=BEAT_GAP_AFTER.get(key))

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

    def end_card(self, hold: float = 0.3, run_time: float = 0.5):
        card = end_card(self.EPISODE, self.TITLE)
        card[1].set_color(GRAY)
        # the closing A/B frame fades out fully before the card fades in (no double exposure)
        self.play(*[FadeOut(m) for m in list(self.mobjects)], run_time=0.35)
        self.play(FadeIn(card, shift=0.1 * UP), run_time=0.4)
        self.hold(hold)

    # ------------------------------------------------------------------ construct
    def construct(self):
        A = Panel(PTS_A, CNT_A, "A", P1_SIDE, P1_A)
        Bp = Panel(PTS_B, CNT_B, "B", P1_SIDE, P1_B)
        for p in (A, Bp):
            p.dots.set_opacity(0)
            p.hits_t.set_value(0)
        self.add(A.frame, Bp.frame, A.top, Bp.top, A.dots, Bp.dots)

        # the clusters the stakes circles land on: A's three densest squares away from the
        # border, so each circle (radius 1.35 squares) stays inside the map's frame
        big = sorted((i for i in range(G * G) if 0 < i // G < G - 1 and 0 < i % G < G - 1),
                     key=lambda i: -A.counts[i])[:3]

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
                      run_time=beat.until("rule", end=True))
            beat.wait_until("Which", offset=-0.1)
            self.play(flag(A.name), FadeIn(aorb, shift=0.1 * UP), run_time=0.7)
            self.play(flag(Bp.name), run_time=0.7)
        for p in (A, Bp):
            p.hits[0].clear_updaters()

        # ============================================================ 2. stakes
        circles = VGroup(*[Circle(radius=A.cellsize * 1.35, stroke_color=YELLOW, stroke_width=3)
                           .move_to(A.cells[i]) for i in big]).set_z_index(2)
        quote = Text("“…tended to be grouped in clusters.”", font_size=26, slant=ITALIC)
        quote.move_to([0, -2.5, 0])
        cite1 = cite("R. D. Clarke, 1946 · J. Inst. Actuaries 72:481;  "
                     "Shaw & Shaw, 2019 · Significance 16(5)", size=SMALL)
        with self.say_beat("stakes") as beat:
            # the prompt gives way to the source as "In nineteen forty-four" is spoken
            self.play(FadeOut(aorb, rate_func=window(0, 0.6)),
                      FadeIn(cite1, rate_func=window(0.3, 0.7)), run_time=0.8)
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
            self.play(Create(A.grid), Create(Bp.grid),
                      run_time=beat.until("squares", end=True))
            self.bring_to_front(A.frame, Bp.frame, A.dots, Bp.dots)
            self.play(UpdateFromAlphaFunc(VGroup(A.cells, Bp.cells), sweep),
                      run_time=beat.until("hits", offset=-0.1))
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
            # the counter lands on 39 as "thirty-nine" is spoken
            T = beat.until("thirty-nine", end=True, offset=-0.05)
            # the ring leaves just after "Map A lights up"
            t_off = beat.time_of("up", end=True) + 0.15 - beat.elapsed()
            self.play(LaggedStart(*[Create(b) for b in boxes], lag_ratio=0.06, rate_func=linear),
                      tA.animate(rate_func=linear).set_value(39),
                      FadeOut(ring, rate_func=window(t_off / T, 0.5 / T)), run_time=T)
            beat.wait_until("Map B", offset=-0.1)
            self.play(FadeIn(cntB, shift=0.1 * UP), run_time=0.6)
            beat.wait_until("aimed", offset=-0.25)
            self.play(FadeIn(tagA, shift=0.1 * UP), run_time=0.6)
            self.play(FadeIn(tagB, shift=0.1 * UP), run_time=0.5)
        boxes.add(ex_box)

        # ============================================================ 5. reveal
        tagA2 = A.below(Text("pure chance", font_size=26, color=PURPLE))
        tagB2 = Bp.below(formula(r"\text{rule: spacing}", r"\ge", r"\tfrac{4}{5}",
                                 r"\text{ square}", size=36))
        # zoom blocks on the maps' right edge, both chosen by the same rule: the 4 x 4 block
        # whose count is closest to the 16-hit average (A: rows 18-21, 16 hits; B: rows 8-11,
        # 16 hits), so a typical patch of chance is compared with a typical patch of the rule
        jA = min(range(2, G - 5), key=lambda j: (abs(CNT_A[ZONE_I0:, j:j + 4].sum() - 16), j))
        assert CNT_A[ZONE_I0:, jA:jA + 4].sum() == 16, jA
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

        # which cell each hit lands in, and which cell each red outline marks
        dot_cell = np.array([int(p[0]) * G + int(p[1]) for p in PTS_A])
        box_cells = [i for i in tgt_idx if i != ex_idx] + [ex_idx]   # the order of `boxes`
        base_fill = A.shaded_targets()

        def rerain(m, a):
            # "I dropped every hit on map A at random": the hits clear and fall again, in the
            # same order and places as the cold open.  The picture stays true at every frame:
            # the shading and the red outlines clear with the hits, then each cell re-shades by
            # the hits that have landed in it and its red outline returns when it reaches 3,
            # while the hits and target counters recount (0 -> 537, 0 -> 39)
            if a < 0.15:
                f = 1 - a / 0.15
                for d in A.dots:
                    d.set_opacity(f)
                for c, b in zip(A.cells, base_fill):
                    c.set_fill(opacity=b * f)
                boxes.set_stroke(opacity=f)
                return
            n = (a - 0.15) / 0.85 * N
            k = min(N, int(n))
            for i, d in enumerate(A.dots):
                d.set_opacity(float(np.clip(n - i, 0, 1)))
            cnt = np.bincount(dot_cell[:k], minlength=G * G)
            for c, v in zip(A.cells, cnt):
                c.set_fill(opacity=shade(v))
            on = 0
            for b, ci in zip(boxes, box_cells):
                hit = cnt[ci] >= 3
                b.set_stroke(opacity=1.0 if hit else 0.0)
                on += int(hit)
            tA.set_value(on)
            A.hits_t.set_value(k)

        def hits_upd(m):
            m.set_value(A.hits_t.get_value())
            A.hits[1].next_to(m, RIGHT, buff=0.15)

        with self.say_beat("reveal") as beat:
            self.play(swap(tagA, tagA2), FadeOut(tagB, shift=0.1 * DOWN),
                      run_time=beat.until("dropped", offset=-0.15))
            A.hits[0].add_updater(hits_upd)
            self.play(UpdateFromAlphaFunc(A.dots, rerain, rate_func=linear),
                      Indicate(tagA2, color=YELLOW, scale_factor=1.0,
                               rate_func=lambda t: there_and_back(min(1.0, t / 0.45))),
                      run_time=1.8)
            A.hits[0].clear_updaters()
            A.dots.set_opacity(1)
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
            # "Your eye expects chance to look that even": A's zoom builds, and its discs that
            # crowd a neighbour (closer than B's rule) turn red on "even"
            self.play(Create(insA[0]), FadeIn(citeFK), run_time=0.4)
            self.play(Create(insA[1]), FadeIn(insA[2:4]), FadeIn(insA[5]), run_time=0.5)
            self.play(LaggedStart(*[GrowFromCenter(d) for d in insA.discs], lag_ratio=0.05),
                      run_time=beat.until("look", offset=-0.1, min_time=0.6))
            # the crowding discs are red as "that even" is spoken, and stay red into the pause
            beat.wait_until("that even", offset=-0.3)
            self.play(insA.close.animate.set_fill(RED, 0.4).set_stroke(RED, 2.5), run_time=0.8)

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
        # (1.5 below: room under the second row for the (1 - lambda/n)^n convergence plot)
        EL.shift(e_eq.get_center() - EL[0].get_center() + 1.5 * DOWN)
        blk = VGroup(E1, EL)
        # high enough that the histogram preview (axes top 0.75, title above) clears it
        blk.shift(np.array([RX - 0.15, 1.95, 0]) - np.array([blk.get_center()[0], E1.get_center()[1], 0]))
        e_word.set_color(YELLOW)
        EL[5].set_color(PURPLE)
        E1_DROP = 1.0                                  # E1 sits lower until the preview needs room
        E1.shift(E1_DROP * DOWN)
        ysq = A.outline(pick, color=YELLOW, width=4.5, z=3)
        gP = Square(P2_SIDE).move_to(P2_C)
        for m in (A.name, A.sim, tagA2):
            m.generate_target()
            m.target.scale(s)
        A.name.target.next_to(gP, UP, buff=0.2 * s).align_to(gP, LEFT)
        A.sim.target.next_to(A.name.target, RIGHT, buff=0.22 * s, aligned_edge=DOWN)
        tagA2.target.next_to(gP, DOWN, buff=0.2 * s).align_to(gP, LEFT)
        A.hits.scale(s).next_to(gP, UP, buff=0.2 * s).align_to(gP, RIGHT)
        # the one square, outlined where it will sit once A has grown back
        ysq.become(Square(P2_SIDE / G, stroke_color=YELLOW, stroke_width=4.5).set_z_index(3)
                   .move_to(P2_C + (A.cells[pick].get_center() - A.frame.get_center())
                            * (P2_SIDE / Z_SIDE)))
        # the square's 1/576 is first written right beside the square (on a knockout over the
        # hits), then carried into its slot in P(empty) on "To stay empty"
        frac_home = e_frac.get_center().copy()
        e_frac.next_to(ysq, RIGHT, buff=0.3).set_z_index(6)
        frac_bg = BackgroundRectangle(e_frac, color=BG, fill_opacity=1, buff=0.07).set_z_index(5)
        with self.say_beat("square") as beat:
            # B and the zooms clear out before A grows over the zooms' place; the one square is
            # outlined as "Each bomb" is spoken
            self.play(FadeOut(VGroup(Bp.map, Bp.name, Bp.sim, tagB2, insA, insB, cntA.number,
                                     alarm, citeFK), rate_func=window(0, 0.4)),
                      VGroup(A.map, boxes).animate.scale(P2_SIDE / Z_SIDE,
                                                         about_point=A.frame.get_center())
                      .shift(P2_C - A.frame.get_center()),
                      *[MoveToTarget(m) for m in (A.name, A.sim, tagA2)], FadeIn(A.hits),
                      A.level_anim(MAP_DIM, 1, extra=dim_boxes),
                      Create(ysq, rate_func=window(0.55, 0.45)), run_time=0.9)
            # "...has a one in five seventy-six chance": the square and the grid become 1/576
            beat.wait_until("one in", offset=-0.1)
            self.allow_overlap(e_frac[1], e_pow, reason="fraction bar and the closing \\Big) "
                               "of the same typeset equation (TeX spacing)")
            self.allow_overlap(EL[2][1], EL[3], reason="fraction bar and the closing \\Big) "
                               "of the same typeset equation (TeX spacing)")
            self.play(FadeIn(frac_bg, rate_func=window(0.15, 0.35)),
                      TransformFromCopy(ysq, e_frac[0]), Create(e_frac[1]),
                      FadeIn(e_frac[2:], shift=0.4 * RIGHT),
                      A.grid.animate(rate_func=there_and_back).set_stroke(YELLOW, 2, 0.9),
                      boxes.animate.set_stroke(opacity=0.3), run_time=1.3)
            # "...of landing in this square": the square pulses on the word
            beat.on("this square", ysq.animate(rate_func=there_and_back).set_stroke(width=9),
                    run_time=0.7)
            beat.wait_until("To stay", offset=-0.1)
            # P(empty) = (1 - ... is written and the square's 1/576 flies into its slot
            self.play(Write(VGroup(e_P, e_word, e_close, e_eq, e_open)),
                      e_frac.animate.move_to(frac_home), FadeOut(frac_bg, rate_func=window(0, 0.3)),
                      run_time=1.0)
            beat.wait_until("all five", offset=-0.1)
            # the hits counter's 537 is carried into the exponent (a cross-fade, no glyph morph)
            self.play(carry(A.hits[0], e_pow), run_time=1.1)

        # ============================================================ 7. guess
        Q = formula(r"\text{empty squares}", r"\approx", r"\ ?", size=FS)
        Q.move_to([RX, E1.get_center()[1] - 1.4, 0])
        Q[0].set_color(YELLOW)
        # the method the guess can use, built in the hold: 0.3933 x 576 ~ ?  (the "?" is the
        # only thing that changes when the answer is spoken)
        L2 = formula(r"0.3933", r"\times", r"576", r"\approx", r"227", size=FS)
        L2.move_to(Q)
        L2[4].set_color(YELLOW)
        q2 = formula(r"\ ?", size=FS, color=YELLOW).move_to(L2[4], aligned_edge=LEFT)
        with self.say_beat("guess") as beat:
            self.play(Write(Q), run_time=1.0)
            beat.wait_until("empty", offset=0.05)
            self.play(Write(e_val), run_time=0.6)
            self.play(FadeOut(Q[0], shift=0.15 * UP, rate_func=window(0, 0.35)),
                      TransformFromCopy(e_val[1:], L2[0], rate_func=window(0.25, 0.75)),
                      Write(L2[1], rate_func=window(0.35, 0.65)),
                      TransformFromCopy(e_frac[2:5], L2[2], rate_func=window(0.3, 0.7)),
                      ReplacementTransform(Q[1], L2[3]), ReplacementTransform(Q[2], q2),
                      run_time=0.9)

        # ============================================================ 8. empty
        tE = ValueTracker(222)
        cntE = live_number(tE, 0, size=36, color=YELLOW, suffix=r"\text{empty}")
        A.below(cntE, RIGHT)
        tE.set_value(0)
        cntE[0].update()

        def focus_empties(m, a):
            # "Map A has 222": the yellow empties are the only coloured layer - the blue count
            # shading goes, the hits step back to 60 % (they return on "pile-ups")
            A.cell_k = 1 - a
            for i, c in enumerate(A.cells):
                c.set_fill(BLUE, shade(A.counts[i]) * A.cell_k)
            A.dots.set_opacity(1 - 0.4 * a)
        with self.say_beat("empty") as beat:
            # "About two hundred twenty-seven": only the "?" changes
            beat.wait_until("two", offset=-0.12)
            self.play(swap(q2, L2[4], run_time=0.5))
            beat.wait_until("Map A", offset=-0.2)
            self.add(cntE)
            # the empty squares: a full-yellow outline of each empty region (no fill), drawn as
            # the counter runs
            A.edges = A.empty_edges()
            self.play(Create(A.edges), tE.animate.set_value(222), FadeOut(ysq),
                      UpdateFromAlphaFunc(A.map, focus_empties),
                      boxes.animate.set_stroke(opacity=0),
                      run_time=beat.until("twenty-two", offset=0.2))
            A.yellow_empties = True
            self.play(flag(cntE, color=INK), run_time=0.8)

        # ============================================================ 9. gaps force clumps
        # what the empty squares force: 537 hits, but only 354 squares to put a first hit in, so
        # 183 hits land where another already did (a pile-up need not reach 3: only the extra
        # hits are forced)
        # 537 hits, but only 576 - 222 squares to take a first hit: the rest are extra
        L3 = formula("537", "-", "(", "576", "-", "222", ")", "=", "183", r"\text{ extra hits}",
                     size=FS)
        L3.move_to(L2)
        VGroup(L3[8], L3[9]).set_color(BLUE)
        assert L3.get_left()[0] > A.frame.get_right()[0] + 0.6 and L3.get_right()[0] < SAFE_X - 0.1, \
            (L3.get_left(), L3.get_right())
        ge2_idx = [i for i, n in enumerate(A.counts) if n >= 2]
        ge2 = VGroup(*[A.outline(i, color=BLUE, width=3, z=2) for i in ge2_idx])
        assert sum(max(c - 1, 0) for c in A.counts) == 183 == N - (G * G - 222)
        # the histogram the derivation has to fill: bar 0 is the 227 just computed, the rest are
        # still unknown (drawn here as a preview, then again when the Poisson bars grow)
        ax = axes((0, 6.2), (0, 400), x_length=6.0, y_length=2.75,
                  x_ticks=[k + X0 for k in range(6)], y_ticks=[0, 100, 200, 300, 400],
                  x_label="hits per square", y_label="squares", x_decimals=1)
        for k, num in enumerate(ax.x_axis.numbers):
            t = MathTex(r"5{+}" if k == 5 else str(k), font_size=MATH_SMALL, color=GRAY)
            num.become(t.move_to(num, aligned_edge=UP))
        grayify(ax)
        ax.shift(np.array([-0.2, -2.0, 0]) - ax.c2p(0, 0))
        pbars = exp_bars(ax)
        p227 = formula("227", size=MATH_SMALL, color=PURPLE).next_to(pbars[0], UP, buff=0.18)

        def blue_back(m, a):
            # "pile-ups": the blue count shading returns at 40 % (so the blue 2+ outlines are
            # the one full-strength blue layer) and the hits come back to full strength
            A.cell_k = 0.4 * a
            for i, c in enumerate(A.cells):
                c.set_fill(BLUE, shade(A.counts[i]) * A.cell_k)
            A.dots.set_opacity(0.6 + 0.4 * a)
        with self.say_beat("gaps") as beat:
            cntE[0].clear_updaters()
            # "Those empty squares": their yellow outline pulses on the word
            beat.on("Those", A.edges.animate(rate_func=there_and_back).set_stroke(width=6),
                    run_time=0.8)
            # "...force pile-ups": the squares holding 2+ hits get blue outlines; the red 3+
            # detector outlines stay off (they return at the histogram)
            beat.wait_until("pile", offset=-0.25)
            self.play(LaggedStart(*[Create(b) for b in ge2], lag_ratio=0.02, rate_func=linear),
                      UpdateFromAlphaFunc(A.map, blue_back), run_time=0.9)
            # "a hundred eighty-three hits must land where another already did": the empties
            # step back to grey and the 227 line gives way; 537 hits (the counter) less the
            # 576 - 222 squares that take a first hit (the 576 of 1/576, the 222 counter)
            self.play(FadeOut(L2, shift=0.12 * UP, rate_func=window(0, 0.3)),
                      A.edges.animate(rate_func=window(0, 0.4)).set_stroke(GRAY, opacity=0.6),
                      cntE.animate(rate_func=window(0, 0.4)).set_color(GRAY),
                      carry(A.hits[0], L3[0], rate_func=window(0.25, 0.75)),
                      TransformFromCopy(e_frac[2:5], L3[3], rate_func=window(0.3, 0.7)),
                      carry(cntE[0], L3[5], rate_func=window(0.35, 0.65)),
                      Write(VGroup(L3[1], L3[2], L3[4], L3[6]), rate_func=window(0.3, 0.7)),
                      run_time=0.85)
            beat.wait_until("eighty-three", offset=-0.1)
            self.play(Write(L3[7:]), run_time=0.7)
            self.play(flag(VGroup(L3[8], L3[9]), color=INK), run_time=0.6)
            beat.wait_until("already", offset=-0.2)
            self.play(ge2.animate(rate_func=there_and_back).set_stroke(width=5.5), run_time=0.8)
        assert len(ge2_idx) == 131

        # ============================================================ 10. lambda
        LAMB = formula(r"\lambda", "=", r"\frac{537}{576}", r"\approx 0.93", size=FS)
        LAMB.move_to([RX, 3.0, 0])
        LAMB[0].set_color(PURPLE)

        def dim_companions(f):
            # the map's labels step back with it; the 222-empty count goes; the red outlines
            # stay off (they left on "double up") and return with the map at the histogram
            boxes.set_stroke(opacity=max(0.0, (f - MAP_DIM) / (1 - MAP_DIM)))
            VGroup(A.top, tagA2).set_opacity(f)

        def dim_labels(f):
            # the map's labels step back with it (the red outlines are already off)
            VGroup(A.top, tagA2).set_opacity(f)

        # "Call that P of zero": the word "empty" gives way to a 0 inside the same line, and
        # P( closes up to the right so ")" and "=" stay where they are
        P0n = formula("P(", "0", ")", size=FS)
        P0n[1].set_color(YELLOW)
        # "One minus a small slice, raised to a big power": (1 - lambda/n)^n for n = 1, 2, 5,
        # 20, 537 (log n axis) creeps up to the purple e^-lambda line (0.068, 0.285, 0.356,
        # 0.385, 0.3933 -> 0.3937)
        LAM = N / G ** 2
        CV_N = [1, 2, 5, 20, 537]
        cv = axes((0, 2.85), (0, 0.4), x_length=4.3, y_length=1.45,
                  x_ticks=[float(np.log10(n)) for n in CV_N], y_ticks=[0, 0.2, 0.4], y_decimals=1)
        for n_, num in zip(CV_N, cv.x_axis.numbers):
            num.become(MathTex(str(n_), font_size=MATH_SMALL, color=GRAY).move_to(num, aligned_edge=UP))
        y0n = cv.y_axis.numbers[0]
        y0n.become(MathTex("0", font_size=MATH_SMALL, color=GRAY).move_to(y0n, aligned_edge=RIGHT))
        grayify(cv)
        cv.shift(np.array([1.2, -2.5, 0]) - cv.c2p(0, 0))
        cv_xt = formula("n", size=36, color=GRAY).next_to(cv.x_axis.get_right(), RIGHT, buff=0.15)
        cv_yt = formula(r"(1-\lambda/n)^{n}", size=36, color=GRAY)
        cv_yt.next_to(cv.y_axis.get_top(), UP, buff=0.2).align_to(cv.y_axis.numbers, LEFT)
        cv_vals = [(1 - LAM / n) ** n for n in CV_N]
        assert [round(v, 3) for v in cv_vals] == [0.068, 0.285, 0.356, 0.385, 0.393], cv_vals
        cv_dots = VGroup(*[Dot(cv.c2p(np.log10(n), v), radius=0.07, color=INK).set_z_index(3)
                           for n, v in zip(CV_N, cv_vals)])
        e_lam = float(np.exp(-LAM))
        cv_line = DashedLine(cv.c2p(0, e_lam), cv.c2p(2.85, e_lam), color=PURPLE, stroke_width=3,
                             dash_length=0.12)
        cv_lbl = formula(r"e^{-\lambda}", size=36, color=PURPLE).next_to(cv_line, RIGHT, buff=0.15)
        assert cv_lbl.get_right()[0] < SAFE_X - 0.05 and cv_yt.get_top()[1] < EL.get_bottom()[1] - 0.2, \
            (cv_lbl.get_right(), cv_yt.get_top(), EL.get_bottom())
        cvgrp = VGroup(cv, cv_xt, cv_yt, cv_dots, cv_line, cv_lbl)
        with self.say_beat("lam") as beat:
            self.play(TransformFromCopy(A.hits[0], LAMB[2][0:3]), Create(LAMB[2][3]),
                      TransformFromCopy(e_frac[2:5], LAMB[2][4:7]), run_time=0.85)
            beat.wait_until("lambda", offset=-0.2)
            # the map steps back uniformly; only the one square stays lit.  The 183 line, the
            # grey empties and their count leave, and P(empty) rises to make room
            ysq.set_stroke(opacity=1)
            edgesE = A.edges
            A.edges, A.yellow_empties = None, False
            self.play(Write(LAMB[0:2]), Write(LAMB[3]), FadeOut(ge2),
                      FadeOut(VGroup(L3, cntE, edgesE)), E1.animate.shift(E1_DROP * UP),
                      A.level_anim(1, MAP_DIM, 0, 0, extra=dim_labels),
                      FadeIn(ysq), run_time=0.8)
            # second row copied from the first; 1/576 = lambda/537 is assembled from
            # lambda = 537/576 (lambda and 537 fly in from the definition)
            self.play(TransformFromCopy(e_eq, EL[0]), TransformFromCopy(e_open, EL[1]),
                      TransformFromCopy(e_pow, EL[3]), TransformFromCopy(LAMB[0], EL[2][0]),
                      TransformFromCopy(e_frac[1], EL[2][1]),
                      TransformFromCopy(LAMB[2][0:3], EL[2][2:5]),
                      run_time=beat.until("small", offset=-0.15, min_time=1.1))
            # "One minus a small slice": the slice lights up and the plot of (1 - lambda/n)^n
            # draws under the row
            beat.wait_until("small slice", offset=-0.1)
            self.play(flag(e_frac), flag(EL[2]), Create(cv), FadeIn(cv_xt), FadeIn(cv_yt),
                      run_time=0.8)
            # "...raised to a big power": the power n grows, 1 -> 537, and the value climbs
            beat.wait_until("raised", offset=-0.1)
            self.play(LaggedStart(*[FadeIn(d, shift=0.35 * DOWN) for d in cv_dots], lag_ratio=0.5),
                      flag(EL[3][1:], rate_func=tb_window(0.3, 0.7)), run_time=1.5)
            # "...is e to the minus lambda, almost exactly": the limit and its value, then the
            # check - 0.3933 and 0.3937 light up together on "almost exactly"
            beat.wait_until("e to", offset=-0.1)
            self.play(Write(EL[4]), Write(EL[5]), Create(cv_line), FadeIn(cv_lbl), run_time=0.6)
            self.play(Write(EL[6]), run_time=0.5)
            beat.wait_until("almost", offset=-0.1)
            self.play(flag(e_val[1:]), flag(EL[6][1:]), flag(cv_dots[-1]), run_time=0.8)
            # "Call that P of zero": the empty square's probability is renamed in place
            P0n.shift(e_close.get_right() - P0n[2].get_right())
            P0n.shift((e_P.get_center()[1] - P0n[0].get_center()[1]) * UP)
            beat.wait_until("zero", offset=-0.3)
            self.play(FadeOut(e_word, shift=0.2 * UP), FadeIn(P0n[1], shift=0.2 * UP),
                      ReplacementTransform(e_P, P0n[0]), ReplacementTransform(e_close, P0n[2]),
                      run_time=0.7)
            self.settle(P0n)

        # ============================================================ 11. two hits
        P0 = formula("P(", "0", ")", r"\approx", r"e^{-\lambda}", size=FS)
        P0.move_to([0.75, 2.95, 0])
        P0[4].set_color(PURPLE)
        LAMB_T = LAMB.copy().move_to([4.55, 2.95, 0])
        # the 537 bombs, lined up as a block of dots (47 per row)
        ticks = VGroup(*[Dot([-0.5 + (i % 47) * 0.14, 2.2 - (i // 47) * 0.085, 0], radius=0.034,
                             color=INK, fill_opacity=0.8) for i in range(N)])
        bombs_lbl = Text("537 bombs", font_size=27, color=GRAY)
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
        others = VGroup(*[t for i, t in enumerate(ticks) if i not in pick2])   # the 535 that miss
        # each bomb's chance of landing in the square, carried out of the P(0) row and kept
        # beside the big square ("Each has that same chance")
        frac_lbl = formula(r"\frac{1}{576}", size=FS).next_to(bigsq, RIGHT, buff=0.4)
        with self.say_beat("two") as beat:
            # one move per phrase.  "For two hits": the two empty-chance rows (and the limit
            # plot) collapse to P(0) = e^-lambda, and lambda moves aside; only 1/576 survives
            # (the rows fade first; then "= e^-lambda" climbs on an arc that keeps clear of
            # the surviving 1/576)
            mv = window(0.3, 0.7)
            self.play(FadeOut(VGroup(e_eq, e_open, e_pow, e_val, *EL[0:4], EL[6], cvgrp),
                              rate_func=window(0, 0.35)),
                      ReplacementTransform(P0n[0], P0[0], rate_func=mv),
                      ReplacementTransform(P0n[1], P0[1], rate_func=mv),
                      ReplacementTransform(P0n[2], P0[2], rate_func=mv),
                      ReplacementTransform(EL[4], P0[3], path_arc=PI / 3, rate_func=mv),
                      ReplacementTransform(EL[5], P0[4], path_arc=PI / 3, rate_func=mv),
                      Transform(LAMB, LAMB_T, rate_func=mv), run_time=0.7)
            self.settle(P0)
            # "...in this square": the square is enlarged, its 1/576 settling beside it
            beat.on("this square", TransformFromCopy(ysq, bigsq),
                    ReplacementTransform(e_frac, frac_lbl), run_time=0.65)
            # "pick two bombs": map A's 537 hits line up as a block of 537 bombs, then two of
            # them turn yellow and drop into the square
            beat.wait_until("pick", offset=-0.15)
            self.play(ReplacementTransform(A.dots.copy(), ticks),
                      FadeIn(bombs_lbl, rate_func=window(0.5, 0.5)), run_time=0.9)
            self.play(*[ticks[i].animate.set_fill(YELLOW, 1).scale(1.8) for i in pick2],
                      *[TransformFromCopy(ticks[i], h) for i, h in zip(pick2, hits2)],
                      run_time=0.5)
            # each factor is written as its own objects light up (no dots-to-digits morph):
            # 537 choices for the first bomb, the other 536 for the second, 2! orders
            beat.wait_until("five thirty-seven", offset=-0.15)
            self.play(Write(P2[0:4]), carry(bombs_lbl[0:3], fr2[0:3]),
                      flag(ticks, color=YELLOW, run_time=0.7), run_time=0.7)
            beat.wait_until("five thirty-six", offset=-0.15)
            self.play(FadeIn(fr2[3]), Write(fr2[4:7]), ticks[pick2[0]].animate.set_opacity(0.3),
                      flag(rest, color=YELLOW, run_time=0.7), run_time=0.7)
            beat.wait_until("over two", offset=-0.1)
            self.play(Create(fr2[7]), Write(fr2[8:10]), flag(hits2, color=INK, run_time=0.7),
                      run_time=0.7)
            # "since each pair counts twice": the two hits trade places - the same pair, in both
            # orders, is counted twice
            beat.wait_until("each pair", offset=-0.15)
            self.play(Swap(hits2[0], hits2[1], path_arc=PI / 2), flag(fr2[8:10]), run_time=0.8)
            # "Each has that same chance": the square's 1/576 is carried in, once per hit
            beat.wait_until("Each has", offset=-0.15)
            self.play(Write(P2[5]), run_time=0.5)
            beat.wait_until("same", offset=-0.2)
            self.play(carry(frac_lbl, P2[6]), flag(frac_lbl), run_time=1.0)
            # "and the rest miss": the other 535 bombs step back; "e to the minus lambda again"
            # is copied from P(0)
            beat.wait_until("rest", offset=-0.1)
            self.play(others.animate.set_opacity(0.3), run_time=0.6)
            beat.wait_until("e to", offset=-0.1)
            self.play(Write(P2[7]), TransformFromCopy(P0[4], P2[8]), run_time=1.0)

        # ============================================================ 12. Poisson
        # in place: 536 ~ 537, so the top is 537^2; then every 2 becomes a 3 (three hits), then a k
        def state(p, num, den, pk):
            m = formula("P(", p, ")", r"\approx", r"\frac{537^{%s}}{%s!}" % (num, den), r"\cdot",
                        r"\Big(\frac{1}{576}\Big)^{%s}" % pk, r"\cdot", r"e^{-\lambda}", size=FS)
            m[8].set_color(PURPLE)
            return m.move_to(P2).align_to(P2, LEFT)
        F1 = state("2", "2", "2", "2")
        F3 = state("3", "3", "3", "3")
        F5 = state("k", "k", "k", "k")
        changed = [(1, 0), (4, 3), (4, 5), (6, 7)]     # P(2), 537^2, 2!, (1/576)^2
        n537 = formula("537", size=FS, color=YELLOW)
        n537.match_height(fr2[4:7]).move_to(fr2[4:7])

        def swap_glyphs(src, dst, run_time=0.6):
            """Every count glyph changes at once (lifts out, the new one rises in yellow); the
            rest of the formula slides to its new spacing."""
            anims = []
            for i in range(len(src)):
                for j in range(len(src[i])):
                    if (i, j) in changed:
                        dst[i][j].set_color(YELLOW)
                        anims += [FadeOut(src[i][j], shift=0.2 * UP),
                                  FadeIn(dst[i][j], shift=0.2 * UP)]
                    else:
                        anims.append(ReplacementTransform(src[i][j], dst[i][j]))
            self.play(*anims, run_time=run_time)
            self.settle(dst)

        # (a thin space before e^-lambda keeps it >= 0.15 from the fraction bar)
        E5 = formula(r"P(k)", r"\approx", r"\frac{\lambda^{k}}{k!}", r"\,e^{-\lambda}", size=44)
        E5.move_to(F5)
        E5[3].set_color(PURPLE)
        E5[2][0:2].set_color(PURPLE)                   # lambda^k is the purple lambda
        E5_top = E5.copy().set_color(PURPLE)
        E5_top.move_to([0, EQ1_Y, 0]).align_to([-0.35, 0, 0], LEFT)
        pois = Text("Poisson", font_size=28, color=PURPLE).next_to(E5, RIGHT, buff=0.45)
        pois_top = pois.copy().next_to(E5_top, RIGHT, buff=0.45)
        ins = inset_frame(ax)
        ipb = inset_exp(ax)
        ylab = formula(r"=", r"576\cdot P(k)", size=36)
        ylab[0].set_color(GRAY)
        ylab[1].set_color(PURPLE)
        ylab.next_to(ax.y_title, RIGHT, buff=0.18).align_to(ax.y_title, DOWN)
        picture = VGroup(ticks, bombs_lbl, bigsq, hits2, frac_lbl)
        with self.say_beat("poisson") as beat:
            # "Five thirty-six": the 536 lights up; the picture steps back
            self.play(fr2[4:7].animate.set_color(YELLOW),
                      VGroup(ticks, bombs_lbl, hits2, frac_lbl).animate.set_opacity(0.3),
                      bigsq.animate.set_stroke(opacity=0.3), run_time=0.8)
            # "... is almost five thirty-seven": the 536 becomes a 537, in place
            beat.wait_until("five thirty-seven", offset=-0.1)
            self.play(FadeOut(fr2[4:7], shift=0.2 * UP), FadeIn(n537, shift=0.2 * UP),
                      run_time=0.6)
            # 537 times 537 is 537 squared: the second 537 folds into the exponent
            fn = F1[4]
            fn[3].set_color(YELLOW)
            self.play(*[ReplacementTransform(P2[i], F1[i]) for i in range(9) if i != 4],
                      ReplacementTransform(fr2[0:3], fn[0:3]),
                      FadeOut(VGroup(fr2[3], n537), target_position=fn[3], scale=0.3),
                      FadeIn(fn[3], rate_func=window(0.4, 0.6)),
                      ReplacementTransform(fr2[7:], fn[4:]), run_time=0.8)
            self.settle(F1)
            self.play(fn[3].animate.set_color(INK), run_time=0.4)
            # "For three hits, each two becomes a three": all four 2s light up, then turn to 3s
            beat.wait_until("each two", offset=-0.1)
            self.play(*[F1[i][j].animate.set_color(YELLOW) for i, j in changed], run_time=0.5)
            beat.wait_until("becomes", offset=0.0)
            swap_glyphs(F1, F3)
            # "for any k, a k"
            beat.wait_until("k", offset=-0.1)
            swap_glyphs(F3, F5)
            beat.wait_until("The powers", offset=-0.3)
            Pk = F5
            # 537 and 576 (the powers' bases) and lambda = 537/576 light up together
            self.play(Pk[4][0:3].animate.set_color(YELLOW), Pk[6][3:6].animate.set_color(YELLOW),
                      LAMB[2].animate.set_color(YELLOW),
                      *[Pk[i][j].animate.set_color(INK) for i, j in changed], run_time=0.6)
            beat.wait_until("into lambda", offset=-0.1)
            self.play(ReplacementTransform(VGroup(*Pk[0], *Pk[1], *Pk[2]), E5[0]),
                      ReplacementTransform(Pk[3], E5[1]),
                      # the same e^-lambda glyphs (E5's copy only has a thin space in front)
                      allow_morph(ReplacementTransform(Pk[8], E5[3])),
                      ReplacementTransform(Pk[4][3], E5[2][1]),
                      ReplacementTransform(Pk[4][4:7], E5[2][2:5]),
                      FadeOut(VGroup(Pk[4][0:3], Pk[6], Pk[5], Pk[7]),
                              target_position=E5[2][0], scale=0.4),
                      TransformFromCopy(LAMB[0], E5[2][0]),
                      LAMB[2].animate.set_color(INK), run_time=1.3)
            self.settle(E5)
            beat.wait_until("Poisson", offset=-0.2)
            self.play(FadeIn(pois, shift=0.1 * LEFT), run_time=0.6)
            # the finished formula holds through the pause while the scaffolding leaves (so the
            # formula never travels through fading text), then rises to make room
            self.play(FadeOut(picture), FadeOut(P0), FadeOut(LAMB), run_time=0.6)
            beat.wait_until("Times", offset=-0.1)
            self.play(Transform(E5, E5_top), pois.animate.move_to(pois_top), run_time=0.8)
            # P(k) is copied down into the axis title first; "= 576·" is written in front of it
            # only once it has landed (the copy never flies through other glyphs)
            self.play(Create(ax), Create(ins), TransformFromCopy(E5[0], ylab[1][4:]),
                      run_time=0.8)
            self.play(FadeIn(ylab[0]), Write(ylab[1][:4]), run_time=0.5)
            beat.wait_until("these", offset=-0.2)
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
        # the misfit readout: chi^2_A = sum gap^2/chance = [live]
        tM = ValueTracker(0)
        rd = formula(r"\chi^2_{\text{A}}", "=", r"\sum \text{gap}^2/\text{chance}", "=", size=36)
        # A's readout shows the running sum of its two-decimal terms (0.10 ... 2.00); B's has
        # one decimal (271.7)
        rnum = DecimalNumber(0, num_decimal_places=2, font_size=36, color=YELLOW)
        rgrp = VGroup(rd, rnum).arrange(RIGHT, buff=0.18).move_to([RX + 0.25, 1.95, 0])
        rnumB = DecimalNumber(0, num_decimal_places=1, font_size=36, color=YELLOW)
        rnumB.move_to(rnum, aligned_edge=LEFT)
        rdB = formula(r"\chi^2_{\text{B}}", size=36)
        rdB.move_to(rd[0], aligned_edge=LEFT)
        # until its terms are added, the readout says "= ?" (never a false "= 0.0" or a
        # stale "= 2.0" under the B subscript)
        qA = formula(r"?", size=36, color=YELLOW).move_to(rnum, aligned_edge=LEFT)
        qB = qA.copy()

        def roll_in(q, num, value, run_time, *extra):
            """The "?" gives way to the live readout, which counts up to `value`."""
            tM.set_value(0)
            num.set_value(0)
            num.set_opacity(0)
            self.add(num)
            num.add_updater(lambda m: m.set_value(tM.get_value()))

            def fade(m, a):
                m.set_opacity(1 - min(1.0, a / 0.2))
                num.set_opacity(min(1.0, max(0.0, (a - 0.12) / 0.2)))
            self.play(UpdateFromAlphaFunc(q, fade), tM.animate.set_value(value), *extra,
                      run_time=run_time)
            self.remove(q)
            num.clear_updaters()
            num.set_value(value)
            num.set_opacity(1)
        # "Map A scores two point oh": each term flags in place while the readout steps
        # through the running sums 0.10, 0.74, 1.17, 1.39, 1.88, 2.00
        SUMS = np.cumsum([float(t) for t in PARTS_TXT])
        assert [round(x, 2) for x in SUMS] == [0.10, 0.74, 1.17, 1.39, 1.88, 2.00], SUMS
        T_SUM, LAG = 1.4, 0.25
        SUM_T0 = [i * LAG * T_SUM / (1 + 5 * LAG) for i in range(6)]   # each flag's start

        def sum_step(m, a):
            t = a * T_SUM
            k = sum(1 for t0 in SUM_T0 if t >= t0 + 0.1)
            qA.set_opacity(1.0 if k == 0 else 0.0)
            if k:
                rnum.set_value(SUMS[k - 1])
            rnum.set_opacity(0.0 if k == 0 else 1.0)
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
        # y axis: the bar heights count maps
        my0 = MF_X0 - 0.1
        myax = Line([my0, MF_Y, 0], [my0, MF_Y + MF_H + 0.1, 0], stroke_color=GRAY,
                    stroke_width=2.5)
        mylab = Text("maps", font_size=24, color=GRAY)
        mylab.next_to(myax.get_end(), LEFT, buff=0.15).align_to(myax.get_end(), UP)
        hist_n, _ = np.histogram(NULL, bins=np.arange(0, MF_MAX + 1))
        hscale = MF_H / hist_n.max()
        # two numbered ticks on the maps axis (maps per unit of misfit)
        myt = VGroup()
        for v in (1000, 2000):
            yv = MF_Y + v * hscale
            tk = Line([my0 - 0.06, yv, 0], [my0 + 0.06, yv, 0], stroke_color=GRAY, stroke_width=2.5)
            nm = formula(r"%d" % v, size=MATH_SMALL, color=GRAY).next_to([my0 - 0.06, yv, 0], LEFT,
                                                                       buff=0.12)
            nm.ss_role = "tick"
            myt.add(tk, nm)
        myax = VGroup(myax, myt)
        nbars = VGroup(*[Rectangle(width=MF_LEN / MF_MAX * 0.86, height=max(c * hscale, 0.004),
                                   stroke_width=0, fill_color=PURPLE, fill_opacity=0.55)
                         .move_to([mfx(k + 0.5), MF_Y, 0], aligned_edge=DOWN)
                         for k, c in enumerate(hist_n)])
        worse = VGroup(*nbars[2:])                     # bins from 2.0 up: scores worse than A
        mhead = VGroup(Text("20,000 chance maps", font_size=27, color=PURPLE),
                       Text("(simulated)", font_size=27, color=GRAY)).arrange(RIGHT, buff=0.18,
                                                                              aligned_edge=DOWN)
        mhead.move_to([MF_X0 + mhead.width / 2 - 0.1, 2.3, 0])
        TH = 1.1                                       # thumbnail side
        thumb_c = np.array([mfx(2.0), 1.2, 0])
        mark = Line([mfx(2.0), MF_Y, 0], [mfx(2.0), thumb_c[1] - TH / 2 - 0.08, 0],
                    stroke_color=YELLOW, stroke_width=4).set_z_index(3)
        alab = Text("A", font_size=32).next_to(thumb_c + TH / 2 * RIGHT, RIGHT, buff=0.2)
        pval = formula(r"p = 0.74", size=MATH, color=PURPLE).move_to([mfx(10.0), -0.3, 0])
        # map A as a thumbnail: its hits and frame only (the cold-open picture, no shading)
        thumb = VGroup(A.frame, A.dots)
        # what one entry of the 20,000 is: the first three simulated chance maps of the null
        # run (sim.null_misfits, seed 2026), drawn as thumbnails tagged with their scores, each
        # dropping into its bin.  Their squares are the null run's own; each hit is placed
        # uniformly inside its square (the score depends only on the squares' counts)
        rng_cells = np.random.default_rng(sim.SEED_NULL)
        rng_xy = np.random.default_rng(5)
        samples = []
        for _ in range(3):
            cells = rng_cells.integers(0, G * G, size=N)
            pts = np.stack([cells // G + rng_xy.random(N), cells % G + rng_xy.random(N)], axis=1)
            samples.append(pts)
        s_scores = [sim.misfit(sim.hist(sim.counts(p_))) for p_ in samples]
        assert np.allclose(s_scores, NULL[:3]), (s_scores, NULL[:3])
        stage = np.array([-2.6, thumb_c[1], 0])
        s_thumbs, s_tags, s_tokens = [], [], []
        for pts, sc in zip(samples, s_scores):
            o_t = stage - np.array([TH / 2, TH / 2, 0])
            fr = Square(TH, stroke_color=GRAY, stroke_width=2.5).move_to(stage)
            ds = VGroup(*[Dot(o_t + np.array([p_[0], p_[1], 0]) * TH / G, radius=0.0129,
                              color=INK) for p_ in pts])
            s_thumbs.append(VGroup(fr, ds))
            s_tags.append(formula("%.1f" % sc, size=36, color=PURPLE).next_to(fr, DOWN, buff=0.15))
            k = int(sc)
            s_tokens.append(Rectangle(width=MF_LEN / MF_MAX * 0.86, height=0.05, stroke_width=0,
                                      fill_color=PURPLE, fill_opacity=0.9)
                            .move_to([mfx(k + 0.5), MF_Y, 0], aligned_edge=DOWN))

        def drop(i):
            g, tag, tok = s_thumbs[i], s_tags[i], s_tokens[i]
            # appear with its score, hold long enough to read it, then drop into its bin
            return Succession(FadeIn(VGroup(g, tag), run_time=0.3), Wait(0.3),
                              AnimationGroup(g.animate.scale(0.12).move_to(tok).set_opacity(0),
                                             FadeOut(tag), FadeIn(tok, rate_func=window(0.6, 0.4)),
                                             run_time=0.4))
        # why divide by chance's bar: "short bars wobble less" - each chance bar's spread from
        # map to map (binomial s.d. of 576 squares: 11.7 for bar 0, 2.65 for bar 4), drawn as
        # INK whiskers on chance's bars 0 (main chart) and 4 (the x5 inset)
        SD = [float(np.sqrt(G * G * (e / (G * G)) * (1 - e / (G * G)))) for e in EXP]
        assert round(SD[0], 1) == 11.7 and round(SD[4], 2) == 2.65, SD

        def whisker(x, yc, half):
            return VGroup(Line([x, yc - half, 0], [x, yc + half, 0]),
                          Line([x - 0.07, yc + half, 0], [x + 0.07, yc + half, 0]),
                          Line([x - 0.07, yc - half, 0], [x + 0.07, yc - half, 0])
                          ).set_stroke(INK, 3).set_z_index(4)
        y_unit = ax.c2p(0, 1)[1] - ax.c2p(0, 0)[1]
        wk0 = whisker(pbars[0].get_right()[0] + 0.12, ax.c2p(0, EXP[0])[1], SD[0] * y_unit)
        wk4 = whisker(ipb[1].get_right()[0] + 0.08, inset_base(ax) + EXP[4] * inset_unit(ax),
                      SD[4] * inset_unit(ax))
        wl0 = formula(r"\pm 12", size=32).next_to(wk0, UP, buff=0.15)
        wl4 = formula(r"\pm 2.7", size=32).next_to(wk4, UP, buff=0.15)
        whisk = VGroup(wk0, wk4, wl0, wl4)

        # the map becomes the histogram one count at a time: the k-hit squares light up in
        # place, then fly and stack into bar k as tiles that fill it exactly
        unit_sq = Square(1.0).get_points().copy()

        def tile_plan(k):
            cells = [A.cells[i] for i in A.where(k)]
            b = bA[k]
            w, h = b.width, b.height
            n = len(cells)
            c = max(1, int(round(w / np.sqrt(w * h / n))))
            r = int(np.ceil(n / c))
            tw, th_ = w / c, h / r
            x0, y0 = b.get_left()[0], b.get_bottom()[1]
            tgt = [np.array([x0 + (j % c + 0.5) * tw, y0 + (j // c + 0.5) * th_, 0])
                   for j in range(n)]
            return cells, tgt, tw, th_
        plans = [tile_plan(k) for k in range(6)]
        tiles = [VGroup(*[Square(1.0, stroke_width=0, fill_color=BLUE, fill_opacity=0)
                          .set_z_index(4) for _ in pl[0]]) for pl in plans]

        def dim_all(f):                        # labels and outlines dim with the map
            boxes.set_stroke(opacity=f)
            VGroup(A.top, tagA2).set_opacity(f)
        with self.say_beat("fix") as beat:
            A.cell_k = 1.0
            self.play(FadeOut(ylab), FadeOut(ysq),
                      A.level_anim(MAP_DIM, 1, 0, 0, extra=dim_companions), run_time=0.6)
            T = beat.until("Thirty-nine", offset=-0.25)
            lit, fly = 0.25, 0.55
            step = (T - lit - fly) / 5
            src_c = [[np.array(c.get_center()) for c in pl[0]] for pl in plans]
            cs = A.cells[0].width

            def stack(m, a):
                for k in range(6):
                    t = (a * T - k * step) / (lit + fly)
                    t = min(1.0, max(0.0, t))
                    if t <= 0:
                        continue
                    f_lit = min(1.0, t * (lit + fly) / lit)          # light up in place
                    f_fly = smooth(max(0.0, (t * (lit + fly) - lit) / fly))
                    _, tgt, tw, th_ = plans[k]
                    for sq, p0, p1 in zip(tiles[k], src_c[k], tgt):
                        w = cs + (tw - cs) * f_fly
                        h = cs + (th_ - cs) * f_fly
                        sq.set_points(unit_sq * np.array([w, h, 1]) + (p0 + (p1 - p0) * f_fly))
                        sq.set_fill(BLUE, 0.6 * f_lit + 0.32 * f_fly)
                        sq.set_stroke(INK, 1.2, 0.8 * f_lit * (1 - f_fly))
            for g in tiles:
                self.add(g)
            self.play(UpdateFromAlphaFunc(VGroup(*tiles), stack), run_time=T, rate_func=linear)
            self.remove(*tiles)
            self.add(*bA)
            self.play(*[TransformFromCopy(bA[k], ibA[i]) for i, k in enumerate((3, 4, 5))],
                      GrowFromCenter(brace), FadeIn(b39, shift=0.1 * DOWN), run_time=0.9)
            # "and chance predicts": chance's three tail bars light up, then their sum
            beat.wait_until("chance predicts", offset=-0.15)
            self.play(flag(ipb, color=INK, run_time=0.6), run_time=0.6)
            self.play(Write(c39), run_time=0.7)
            beat.wait_until("chi", offset=-0.15)
            # the map steps back: the yellow gap slivers will be the only full-strength yellow
            # (the Poisson formula steps back too: the misfit readout is the equation in focus)
            self.play(Write(rd), FadeIn(qA), VGroup(E5, pois).animate.set_opacity(0.55),
                      A.level_anim(1, MAP_LOW, 0, 0, extra=dim_all, rate_func=window(0, 0.67)),
                      run_time=0.9)
            beat.wait_until("square", offset=-0.2)
            self.play(FadeOut(VGroup(brace, b39, c39)), run_time=0.5)
            beat.wait_until("gap", offset=-0.2)
            self.play(LaggedStart(*[GrowFromCenter(r) for r in slA], lag_ratio=0.1), run_time=0.6)
            beat.wait_until("divide", offset=-0.1)
            self.play(*[TransformFromCopy(slA[k], terms[k]) for k in range(6)],
                      FadeIn(pluses), flag(VGroup(pbars, ipb), color=INK), run_time=1.0)
            # "because short bars wobble less": chance's own spread on a tall bar and a short one
            beat.wait_until("wobble", offset=-0.25)
            self.play(Create(wk0), Create(wk4), FadeIn(wl0), FadeIn(wl4), FadeOut(p227),
                      run_time=0.7)
            # "...: a miss on a short bar counts more" - the 4-hit bar's miss of 1.9 nearly fills
            # its +-2.7 and costs 0.49; the 0-hit bar's bigger miss of 4.7 sits well inside its
            # +-12 and costs 0.10
            beat.wait_until("short", occurrence=2, offset=-0.15)
            self.play(flag(VGroup(slA[4], terms[4], ipb[1], wk4), color=INK), run_time=0.9)
            # "Map A scores two point oh": each term flags in place while the readout steps
            # through the running sums (no copies fly)
            beat.wait_until("Map A", offset=-0.15)
            self.add(rnum)
            rnum.set_opacity(0)
            self.play(LaggedStart(*[flag(t, color=INK) for t in terms], lag_ratio=LAG),
                      UpdateFromAlphaFunc(VGroup(rnum, qA), sum_step, rate_func=linear),
                      FadeOut(whisk, rate_func=window(0, 0.3)), run_time=T_SUM)
            self.remove(qA)
            rnum.set_value(SUMS[-1]).set_opacity(1)
            # map A (hits and frame) comes back to full strength as it shrinks into one score
            # among many
            beat.wait_until("oh", offset=-0.3)
            self.play(FadeOut(VGroup(terms, pluses, slA)),
                      FadeOut(VGroup(A.top, tagA2, boxes, A.grid, A.cells)),
                      thumb.animate.scale_to_fit_width(TH).move_to(thumb_c),
                      UpdateFromAlphaFunc(VGroup(A.dots), lambda m, a: (
                          A.dots.set_opacity(MAP_LOW + (1 - MAP_LOW) * a),
                          A.frame.set_stroke(opacity=MAP_LOW + (1 - MAP_LOW) * a))),
                      # the panel appears once the shrinking map has cleared its place (the
                      # map never passes over the header or the axis labels)
                      *[a_(m, rate_func=window(0.55, 0.45)) for a_, m in
                        ((Create, mline), (FadeIn, mticks), (FadeIn, mnums), (FadeIn, mtitle),
                         (Create, myax), (FadeIn, mylab), (FadeIn, mhead))],
                      VGroup(E5, pois).animate.set_opacity(0),
                      Create(mark, rate_func=window(0.6, 0.4)),
                      FadeIn(alab, rate_func=window(0.6, 0.4)), run_time=0.9)
            # "Three out of four simulated chance maps": three of them, scored, drop into
            # their bins; then the other 19,997 grow the bins
            self.play(LaggedStart(*[drop(i) for i in range(3)], lag_ratio=0.6), run_time=2.2)
            self.remove(*s_thumbs)
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in nbars], lag_ratio=0.04),
                      FadeOut(VGroup(*s_tokens), rate_func=window(0.3, 0.4)),
                      run_time=beat.until("worse", offset=-0.4, min_time=0.6))
            self.play(worse.animate.set_fill(opacity=0.95),
                      VGroup(*nbars[:2]).animate.set_fill(opacity=0.25), run_time=0.7)
            beat.wait_until("share", offset=0.2)
            # "That share, p": the bright bins hand their share to the p label (a cross-fade
            # along the path, not a bars-to-glyphs morph)
            self.play(carry(worse, pval), run_time=0.9)

        # ============================================================ 13b. map B
        zeros = obs_bars(ax, H_B)
        izeros = inset_obs(ax, H_B)
        # B's tower is labelled with its value above it, clear of every outline; its half-height
        # empty-squares bar is read off the y axis against chance's outline (no label inside it)
        l397 = formula("397", size=36, color=BLUE).next_to(zeros[1], UP, buff=0.2)
        slB = gap_slivers(ax, H_B)
        b_y = MF_Y + 0.45
        barr = Arrow([mfx(MF_MAX) + 0.05, b_y, 0], [mfx(MF_MAX) + 0.85, b_y, 0], buff=0,
                     color=INK, stroke_width=4, max_tip_length_to_length_ratio=0.3)
        blab = formula(r"\text{B: }", r"271.7", size=36)
        blab.next_to(barr, UP, buff=0.15).align_to(barr, RIGHT)
        # map B's own thumbnail (hits and frame only), placed past the end of the misfit axis,
        # where its score lands: position equals score throughout
        Bt = Panel(PTS_B, CNT_B, "B", P2_SIDE, ORIGIN)
        bthumb = VGroup(Bt.frame, Bt.dots)
        bthumb.scale(TH / Bt.frame.width)
        bthumb.move_to([barr.get_end()[0] - TH / 2, thumb_c[1], 0])
        blt = Text("B", font_size=32).next_to(bthumb, LEFT, buff=0.2).align_to(alab, DOWN)
        a_side = VGroup(alab, mark, pval)

        def a_level(f):
            A.dots.set_opacity(f)
            A.frame.set_stroke(opacity=f)
            a_side.set_opacity(f)
            mark.set_stroke(opacity=max(f, 0.6))       # yellow below 60 % reads olive
        with self.say_beat("fixb") as beat:
            rnum.clear_updaters()
            # the subscript becomes B and A's 2.0 gives way to "?" until B's gaps are added
            self.play(Transform(bA, zeros), Transform(ibA, izeros),
                      FadeOut(rd[0][-1], shift=0.15 * UP), FadeIn(rdB[0][-1], shift=0.15 * UP),
                      FadeOut(rnum, shift=0.15 * UP), FadeIn(qB, shift=0.15 * UP),
                      FadeIn(bthumb), FadeIn(blt),
                      UpdateFromAlphaFunc(thumb, lambda m, a: a_level(1 - (1 - MAP_LOW) * a),
                                          rate_func=window(0, 0.6)), run_time=0.85)
            rd[0].remove(rd[0][-1])
            rd[0].add(rdB[0][-1])
            # "half the expected empty squares": B's bar and chance's outline are ringed in INK
            # (a "look here" that changes no fill: yellow in this chart means only gap)
            beat.wait_until("half", offset=-0.15)
            self.play(ring_flash(bA[0]),
                      pbars[0].animate(rate_func=there_and_back).set_stroke(INK, width=5),
                      run_time=0.8)
            beat.wait_until("tower", offset=-0.15)
            self.play(FadeIn(l397, shift=0.1 * UP, rate_func=window(0, 0.55)), ring_flash(bA[1]),
                      run_time=0.8)
            # the bar value leaves before B's gap slivers grow
            beat.wait_until("misfit", offset=-0.4)
            self.play(FadeOut(l397), run_time=0.35)
            roll_in(qB, rnumB, MIS_B, beat.until("seventy-two", end=True, offset=-0.1, min_time=1.0),
                    LaggedStart(*[GrowFromCenter(r) for r in slB], lag_ratio=0.08))
            self.hold(0.15)
            # B's score lands off the end of the axis while the readout it comes from flashes
            # (no number flies across the chart)
            self.play(GrowArrow(barr), FadeIn(blab, shift=0.15 * RIGHT),
                      flag(rnumB, color=INK), FadeOut(slB),
                      UpdateFromAlphaFunc(thumb, lambda m, a: a_level(MAP_LOW + (1 - MAP_LOW) * a)),
                      run_time=0.7)
            # "A pattern this even": B's evenly spaced hits light up with its off-scale score
            beat.on("this even", flag(bthumb), flag(VGroup(blab, barr)), run_time=0.9)

        # ============================================================ 14. aim, Clarke + real map
        flat, iflat = obs_bars(ax, [0] * 6), inset_obs(ax, [0] * 6)
        abars = VGroup(*[bar(ax, k, v, 0.5, stroke_color=RED, stroke_width=3.5, fill_opacity=0)
                         .set_z_index(3) for k, v in enumerate(H_AIM)])
        left_panel = VGroup(thumb, alab, mark, mline, mticks, mnums, mtitle, myax, mylab, nbars,
                            mhead, pval, barr, blab, bthumb, blt)
        # the simulated aimed map itself, in the left slot: 537 hits around 3 aim points
        acell = P2_SIDE / G
        Am = Panel(PTS_AIM, sim.counts(PTS_AIM), "aimed", P2_SIDE, P2_C)
        aframe, agrid, adots = Am.frame, Am.grid, Am.dots
        a_o = aframe.get_corner(DL)
        adots.set_opacity(0)
        # its empty squares, drawn the way map A's were (yellow outline of each empty region)
        aempty = Am.cells_with(0).set_fill(YELLOW, 0)
        aedges = Am.empty_edges()
        aims = VGroup(*[VGroup(Line(LEFT, RIGHT), Line(DOWN, UP)).scale(0.16).rotate(PI / 4)
                        .set_stroke(RED, 5).move_to(a_o + [q[0] * acell, q[1] * acell, 0])
                        .set_z_index(2) for q in _D["aims"]])
        ahead = VGroup(Text("aimed", font_size=40, color=RED),
                       Text("simulated", font_size=27, color=GRAY)).arrange(RIGHT, buff=0.22,
                                                                            aligned_edge=DOWN)
        ahead.next_to(aframe, UP, buff=0.2).align_to(aframe, LEFT)
        # laid out at its final value, right-aligned to the frame like the A/B counters (the
        # number's left edge stays put as it counts, so "537 hits" ends on the frame's edge)
        aim_t = ValueTracker(N)
        ahits = live_number(aim_t, 0, size=36, suffix=r"\text{hits}")
        ahits[-1].set_color(GRAY)
        ahits.next_to(aframe, UP, buff=0.2).align_to(aframe, RIGHT)
        assert ahits.get_left()[0] - ahead.get_right()[0] > 0.2, \
            (ahits.get_left()[0], ahead.get_right()[0])
        aim_t.set_value(0)
        ahits[0].update()
        aimed_map = VGroup(aempty, agrid, aframe, aedges, adots, aims, ahead, ahits)

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
        cite3 = cite("map: Shaw & Shaw, 2019 · Significance 16(5)", size=20)
        cite2 = cite("R. D. Clarke, 1946 · J. Inst. Actuaries 72:481", size=20)
        for c_ in (cite2, cite3):
            c_.align_to([-SAFE_X, 0, 0], LEFT)
        cite3.next_to(cite2, UP, buff=0.14, aligned_edge=LEFT)
        # the real map
        rdots = VGroup(*[Dot(rm(e, n), radius=RDOT, color=INK) for e, n in REAL])
        rdots.set_opacity(0)
        rtitle = Text("real V-1 hits, 1944–45", font_size=26).move_to([-4.6, 3.25, 0])
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
            self.play(FadeOut(VGroup(rd, rnumB)), VGroup(E5, pois).animate.set_opacity(1),
                      Transform(bA, flat), Transform(ibA, iflat),
                      FadeOut(left_panel, shift=0.4 * LEFT), inset_anim(1, MAP_DIM),
                      run_time=0.6)
            # as in the cold open: frame, header and counter first, then the hits rain in
            self.add(aempty)
            self.play(Create(aframe), Create(agrid), FadeIn(ahead), FadeIn(ahits), run_time=0.6)
            self.add(adots)
            self.play(UpdateFromAlphaFunc(adots, rain_aim, rate_func=linear),
                      run_time=beat.until("empty", offset=-0.2, min_time=1.0))
            ahits[0].clear_updaters()
            beat.wait_until("empty", offset=-0.2)
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in abars[:3]], lag_ratio=0.2),
                      Create(aedges), run_time=0.9)
            beat.wait_until("pile", offset=-0.2)
            # the empties step back as the pile-ups (and the aim points) take the focus
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in abars[3:]], lag_ratio=0.2),
                      LaggedStart(*[GrowFromCenter(x) for x in aims], lag_ratio=0.2),
                      aedges.animate.set_stroke(opacity=0), run_time=0.9)
            beat.wait_until("nineteen", offset=-0.1)
            # the aimed outline bars travel with the chart while they fade (none left behind)
            self.play(abars.animate.shift(shift3).set_stroke(opacity=0),
                      FadeOut(aimed_map, shift=0.4 * LEFT),
                      hist_grp.animate.shift(shift3),
                      inset_anim(MAP_DIM, 1), run_time=1.0)
            self.remove(abars)
            self.add(rdots)
            # London's real hits rain in like the cold open; the title and the river arrive as
            # "London's real hits" is spoken
            self.play(FadeIn(cite2, shift=0.1 * UP), FadeIn(cite3),
                      UpdateFromAlphaFunc(rdots, rain_real, rate_func=linear),
                      FadeIn(rtitle, shift=0.1 * DOWN, rate_func=window(0.45, 0.55)),
                      Create(river, rate_func=window(0.45, 0.55)),
                      FadeIn(tl, rate_func=window(0.6, 0.4)),
                      run_time=beat.until("hits", end=True, min_time=1.5))
            beat.wait_until("five thirty-seven", offset=-0.2)
            self.play(Create(cbox), run_time=0.9)
            beat.wait_until("five seventy-six", offset=-0.2)
            self.play(Create(cgrid), outside.animate.set_opacity(0.35), run_time=1.0)
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
        rL.next_to(E5, RIGHT, buff=0.4).align_to(E5[0], DOWN)
        assert rL.get_right()[0] < SAFE_X - 0.05, rL.get_right()
        with self.say_beat("london") as beat:
            # the table builds; the map's title and river label step back to context
            self.play(FadeIn(hdrP),
                      LaggedStart(*[TransformFromCopy(pbars[k], rowP[k]) for k in range(6)],
                                  lag_ratio=0.1),
                      VGroup(rtitle, tl).animate.set_opacity(0.35),
                      run_time=beat.until("two hundred", offset=-0.1))
            self.play(flag(rowP[0]), run_time=0.8)
            # "Clarke counted two hundred twenty-nine": his bars grow into chance's outlines,
            # the empty-square bar first, with his row of counts
            beat.wait_until("Clarke counted", offset=-0.1)
            self.play(FadeIn(hdrB),
                      LaggedStart(*[AnimationGroup(Transform(bA[k], lond[k]),
                                                   FadeIn(rowB[k], shift=0.1 * UP))
                                    for k in range(6)], lag_ratio=0.2),
                      Transform(ibA, ilond, rate_func=window(0.4, 0.6)),
                      run_time=beat.until("Overall", offset=-0.1, min_time=1.6))
            self.play(FadeOut(pois), FadeIn(rL[0], shift=0.1 * UP), run_time=0.6)
            beat.wait_until("p equals", offset=-0.1)
            self.play(Write(rL[1]), run_time=0.8)
            # "London's clusters were no sign of precise aim": the clusters are the 3+ columns,
            # where Clarke's 35, 7, 1 sit on chance's 30.6, 7.1, 1.6; then the verdict, p = 0.88
            beat.wait_until("clusters", offset=-0.2)
            self.play(ring_flash(VGroup(rowP[3:], rowB[3:]), run_time=1.0),
                      ring_flash(ins.frame, run_time=1.0), run_time=1.0)
            beat.wait_until("precise", offset=-0.2)
            self.play(flag(rL[1], color=INK), run_time=0.8)

        # ============================================================ 16. limits
        # one honest limit, measured: the V-1s were aimed at central London (Tower Bridge) but
        # fell short on average (mean point of impact in Dulwich; Evans & Delaney 2018), so hits
        # thin out to the north (1.9 vs 3.7 per km^2).  Score the north box alone with the same
        # test and it fits chance too (p = 0.45): the aim shows only in lambda itself, which the
        # test holds fixed.  The map grows for the geography, then shrinks back beside the chart
        # for the north's own test.
        m_top = rm(RM_E0, REAL[:, 1].max())[1]
        anchor = np.array([RM_X0, m_top, 0.0])
        # grown and moved right, so the map and the labels beside its boxes fill the frame
        lift = np.array([1.1, 2.9 - m_top, 0.0])

        def T(p):
            return anchor + (np.asarray(p, dtype=float) - anchor) * RS + lift
        mapgrp = VGroup(rdots, river, cbox, cgrid)
        tbx, dul = T(rm(*TOWER_BRIDGE)), T(rm(*DULWICH))
        xmark = VGroup(Line(LEFT, RIGHT), Line(DOWN, UP)).scale(0.2).rotate(PI / 4)
        xmark.set_stroke(RED, 6).move_to(tbx).set_z_index(6)
        short = Arrow(tbx, dul, buff=0.2, color=RED, stroke_width=6,
                      max_tip_length_to_length_ratio=0.16).set_z_index(6)
        # "aim:" names the red marks the source stands behind (the x and the arrow), as "map:"
        # and "hits/km²:" do for the lines beside it
        citeE = cite("aim: Evans & Delaney, 2018 · Applied Geography 99", size=20)
        citeE[:4].set_color(RED)                       # "aim:" in the marks' own red
        citeE.next_to(cite2, RIGHT, buff=0.5).align_to(cite2, DOWN)
        cite4 = cite("hits/km²: our count · L. Shaw, 2025 · Zenodo", size=20)
        cite4.next_to(cite3, RIGHT, buff=0.5).align_to(cite3, DOWN)
        n0, n1 = T(rm(NBOX[0], NBOX[2])), T(rm(NBOX[1], NBOX[3]))
        nbox = Rectangle(width=n1[0] - n0[0], height=n1[1] - n0[1], stroke_color=INK,
                         stroke_width=4)
        nbox.move_to((n0 + n1) / 2).set_z_index(3)
        cb0, cb1 = T(c0), T(c1)
        # each density sits next to its own box, on a knockout over the dimmed context hits:
        # "north · 1.9 hits/km²" right of the north box; "≈ Clarke's area" (re-created) with
        # "3.7 hits/km²" under it, a short yellow leader to the rectangle
        lblN = formula(r"\text{north}", r"\ \cdot\ 1.9\ \text{hits/km}^2", size=36)
        lblN.next_to(nbox, RIGHT, buff=0.25)
        bgN = BackgroundRectangle(lblN, color=BG, fill_opacity=1, buff=0.08).set_z_index(5)
        lblN.set_z_index(6)
        clbl_t = clbl.copy().move_to([0, (cb0[1] + cb1[1]) / 2 + 0.3, 0])
        clbl_t.align_to([cb1[0] + 0.45, 0, 0], LEFT)
        recr_t = recr.copy().next_to(clbl_t, RIGHT, buff=0.25).align_to(clbl_t, DOWN)
        dc_val = formula(r"3.7\ \text{hits/km}^2", size=36, color=YELLOW)
        dc_val.next_to(clbl_t, DOWN, buff=0.18).align_to(clbl_t, LEFT)
        bgC = BackgroundRectangle(VGroup(clbl_t, recr_t, dc_val), color=BG, fill_opacity=1,
                                  buff=0.08).set_z_index(5)
        for m in (clbl, recr, dc_val):
            m.set_z_index(6)
        # a short leader, tip on the rectangle
        arrC = Arrow([clbl_t.get_left()[0] - 0.17, clbl_t.get_y(), 0],
                     [cb1[0] + 0.03, clbl_t.get_y(), 0], buff=0, color=YELLOW, stroke_width=3,
                     max_tip_length_to_length_ratio=0.35).set_z_index(6)
        assert arrC.get_length() <= 0.5, arrC.get_length()
        assert recr_t.get_right()[0] < SAFE_X - 0.05 and lblN.get_right()[0] < SAFE_X - 0.05
        # the Thames label, re-placed for the enlarged map: near the river, clear of the hits,
        # both boxes and both label blocks
        qT = np.array([T(p) for p in q])
        rT = np.array([T(p) for p in rs])
        avoid = [(bgN.get_corner(DL), bgN.get_corner(UR)), (bgC.get_corner(DL), bgC.get_corner(UR)),
                 (n0, n1), (cb0, cb1)]
        bestT = None
        for cx in np.arange(-2.5, 3.8, 0.02):
            for cy in np.arange(-0.6, 2.4, 0.02):
                if rect_gap(cx, cy, qT).min() - RDOT * RS < 0.2:
                    continue
                if not 0.15 <= rect_gap(cx, cy, rT).min() <= 0.45:
                    continue
                if any(box_gap(cx, cy, a0, a1) < 0.2 for a0, a1 in avoid):
                    continue
                d_end = np.hypot(cx - rT[-1][0], cy - rT[-1][1])
                if bestT is None or d_end < bestT[0]:
                    bestT = (d_end, cx, cy)
        assert bestT is not None
        tl_home = tl.get_center().copy()
        tl_t = np.array([bestT[1], bestT[2], 0.0])
        chart = VGroup(ax, pbars, bA, ins, ipb, ibA, rowP, rowB, hdrP, hdrB, rL)

        # the north box's own histogram (Shaw's data, 0.5 km squares): 180 squares, 86 hits,
        # lambda = 0.478, scored against its own Poisson bars; p = the share of 200,000
        # simulated chance maps of the box (86 uniform hits in 180 squares) that score worse
        def box_counts(b):
            sel = (REAL[:, 0] > b[0]) & (REAL[:, 0] < b[1]) & (REAL[:, 1] > b[2]) & (REAL[:, 1] < b[3])
            pp = REAL[sel]
            c = np.zeros((int(round((b[1] - b[0]) * 2)), int(round((b[3] - b[2]) * 2))), int)
            np.add.at(c, (((pp[:, 0] - b[0]) // 0.5).astype(int),
                          ((pp[:, 1] - b[2]) // 0.5).astype(int)), 1)
            return c
        CN = box_counts(NBOX)
        H_N = sim.hist(CN)
        assert H_N == [115, 46, 17, 2, 0, 0] and CN.size == 180, H_N
        EXP_N = np.array(sim.poisson_expected(CN.sum() / CN.size, CN.size))
        MIS_N = float(((np.array(H_N) - EXP_N) ** 2 / EXP_N).sum())
        rngN = np.random.default_rng(sim.SEED_NULL)
        worseN = 0
        for _ in range(10):
            cc = rngN.integers(0, CN.size, size=(20000, int(CN.sum())))
            cnt = np.zeros((20000, CN.size), int)
            np.add.at(cnt, (np.repeat(np.arange(20000), cc.shape[1]), cc.ravel()), 1)
            hh = np.stack([(cnt == k).sum(1) for k in range(5)] + [(cnt >= 5).sum(1)], 1)
            worseN += int((((hh - EXP_N) ** 2 / EXP_N).sum(1) >= MIS_N - 1e-9).sum())
        P_N = worseN / 200000
        assert round(P_N, 2) == 0.45, P_N
        pN = VGroup(*[bar(ax, k, v, 0.72, stroke_color=PURPLE, stroke_width=3, fill_color=PURPLE,
                          fill_opacity=0.14) for k, v in enumerate(EXP_N)])
        ipN = VGroup(*[inset_bar(ax, k, EXP_N[k], 0.72, stroke_color=PURPLE, stroke_width=3,
                                 fill_color=PURPLE, fill_opacity=0.14) for k in (3, 4, 5)])
        bN, ibN = obs_bars(ax, H_N), inset_obs(ax, H_N)
        tagN_pos = np.array([bx(ax, 0), max(pN[0].get_top()[1], bN[0].get_top()[1]) + 0.32, 0])
        rN = formula(r"p = %.2f" % P_N, size=36)
        rN.move_to(rL, aligned_edge=LEFT)

        # ---- the landing's pieces
        A2 = Panel(PTS_A, CNT_A, "A", P1_SIDE, P1_A)
        B2 = Panel(PTS_B, CNT_B, "B", P1_SIDE, P1_B)
        # each map's tag and its measured misfit (the episode's tool, applied to the opening)
        tagA3 = A2.below(Text("pure chance", font_size=26, color=PURPLE))
        tagB3 = B2.below(Text("spacing rule", font_size=26))
        scoreA = formula(r"\text{misfit}", r"\ 2.0", size=36)
        scoreB = formula(r"\text{misfit}", r"\ 271.7", size=36)
        for sc, pan, tg in ((scoreA, A2, tagA3), (scoreB, B2, tagB3)):
            sc[0].set_color(GRAY)
            sc[1].set_color(YELLOW)
            sc.next_to(pan.frame, DOWN, buff=0.2).align_to(pan.frame, RIGHT).align_to(tg, UP)
            assert sc.get_left()[0] - tg.get_right()[0] > 0.4
        # the 0:39 detector outlines, redrawn
        red3 = VGroup(*[A2.outline(i, z=3) for i in tgt_idx])
        f0 = A2.frame.get_corner(DL)
        B2.dots.set_opacity(1)
        b2grp = VGroup(B2.frame, B2.dots, B2.top)
        b2grp.shift(8 * RIGHT)
        inside = VGroup(*[d for d, f in zip(rdots, in_c) if f])
        marks = VGroup(nbox, xmark, short)

        with self.say_beat("limit") as beat:
            # the chart and table leave first (nothing grows under fading text), then the map
            # grows into the frame; Clarke's label fades out and back in at its new place
            self.play(FadeOut(chart), FadeOut(clbl), FadeOut(recr), run_time=0.45)
            clbl.move_to(clbl_t)
            recr.move_to(recr_t)
            self.play(mapgrp.animate.scale(RS, about_point=anchor).shift(lift),
                      tl.animate.move_to(tl_t),
                      FadeIn(bgC, rate_func=window(0.6, 0.4)),
                      FadeIn(clbl, rate_func=window(0.6, 0.4)),
                      FadeIn(recr, rate_func=window(0.6, 0.4)),
                      GrowArrow(arrC, rate_func=window(0.7, 0.3)), run_time=0.9)
            # "aimed at central London": the aiming point, Tower Bridge
            beat.wait_until("London", offset=-0.15)
            self.play(GrowFromCenter(xmark), FadeIn(citeE, shift=0.1 * UP), run_time=0.6)
            # "but tended to fall short": from the aiming point to their mean point of impact
            beat.wait_until("fall short", offset=-0.1)
            self.play(GrowArrow(short), run_time=0.8)
            # "so farther north": the north box and its hits; "north" beside it
            beat.wait_until("farther", offset=-0.2)
            self.play(Create(nbox), north_dots.animate.set_opacity(1), FadeIn(bgN),
                      FadeIn(lblN[0], shift=0.1 * LEFT), run_time=0.8)
            # "...hits were about half as dense": 1.9 against 3.7 per km^2, each by its box
            beat.wait_until("half", offset=-0.2)
            self.play(FadeIn(lblN[1], shift=0.1 * LEFT), FadeIn(dc_val, shift=0.1 * LEFT),
                      FadeIn(cite4, shift=0.1 * UP), run_time=0.7)
            # "Score the north alone": the map shrinks back beside the chart, the labels leave
            # ("north" travels to tag the bars), and the chart's axes return
            beat.wait_until("Score", offset=-0.1)
            back = VGroup(mapgrp, marks)
            back.generate_target()
            back.target.shift(-lift).scale(1 / RS, about_point=anchor)
            back.target[0][2].set_stroke(opacity=0.6)          # Clarke's area steps back
            back.target[0][3].set_stroke(opacity=0.3)
            self.play(MoveToTarget(back), tl.animate.move_to(tl_home),
                      FadeOut(VGroup(bgN, lblN[1], bgC, clbl, recr, dc_val, arrC)),
                      lblN[0].animate.move_to(tagN_pos).set_color(BLUE),
                      FadeIn(VGroup(ax, ins), rate_func=window(0.4, 0.6)), run_time=1.0)
            # "...and it fits chance too": its own chance bars, then its counts grow into them
            beat.wait_until("fits", offset=-0.2)
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in pN], lag_ratio=0.1),
                      LaggedStart(*[GrowFromEdge(b, DOWN) for b in ipN], lag_ratio=0.1),
                      LaggedStart(*[GrowFromEdge(b, DOWN) for b in bN], lag_ratio=0.1,
                                  rate_func=window(0.35, 0.65)),
                      LaggedStart(*[GrowFromEdge(b, DOWN) for b in ibN], lag_ratio=0.1,
                                  rate_func=window(0.35, 0.65)), run_time=1.2)
            # "p equals point four five", where Clarke's p sat
            beat.wait_until("p equals", offset=-0.1)
            self.play(Write(rN), run_time=0.7)
            # "The aim hides in lambda": the aim marks, then the formula's one lambda
            beat.wait_until("aim", offset=-0.15)
            self.play(flag(VGroup(xmark, short), color=INK), run_time=0.7)
            beat.wait_until("lambda", offset=-0.15)
            self.play(flag(E5[2][0]), flag(E5[3]), run_time=0.8)
            # "...which the test holds fixed": the test's two verdicts, p = 0.45 here and
            # Clarke's own area
            beat.wait_until("holds", offset=-0.15)
            self.play(flag(rN, color=INK), cbox.animate.set_stroke(opacity=1), run_time=0.6)
            # everything but Clarke's area and its hits leaves at once, so the area is alone
            keep = {id(m) for m in (cbox, *rdots.get_family())}
            outgoing = [m for m in list(self.mobjects)
                        if not any(id(x) in keep for x in m.get_family())]
            for m in (river, cgrid):
                if m not in outgoing:
                    outgoing.append(m)
            self.play(*[FadeOut(m) for m in outgoing], outside.animate.set_opacity(0),
                      run_time=0.5)
            # the area squares up (equal area) while London's hits hand over to map A's, which
            # appear at their true geometry (the two cross at half strength)
            side = float(np.sqrt(cbox.width * cbox.height))
            csq = Square(side, stroke_color=YELLOW, stroke_width=3.5).set_z_index(3)
            csq.move_to(cbox)
            zs = side / P1_SIDE
            k0 = csq.get_corner(DL)
            adots0 = VGroup(*[Dot(k0 + (d.get_center() - f0) * zs, radius=RDOT, color=INK)
                              for d in A2.dots]).set_z_index(1)
            adots0.set_opacity(0)
            self.add(adots0)
            a_in = window(0.25, 0.6)
            self.play(Transform(cbox, csq),
                      UpdateFromAlphaFunc(inside, lambda m, a: m.set_opacity(1 - smooth(a))),
                      UpdateFromAlphaFunc(adots0, lambda m, a: m.set_opacity(a_in(a))),
                      run_time=0.9)
            self.remove(rdots)

        # ============================================================ 17. landing
        with self.say_beat("landing") as beat:
            # the square opens into map A's frame as map B slides back in: the cold-open pair;
            # A's header is written only once its frame is there
            self.play(ReplacementTransform(cbox, A2.frame), ReplacementTransform(adots0, A2.dots),
                      b2grp.animate.shift(8 * LEFT), run_time=0.9)
            # "...map A": its header, and the clumps the 0:39 detector flagged, redrawn; then on
            # "no aim at all" the map's verdict - pure chance, misfit 2.0
            self.play(FadeIn(A2.top, shift=0.1 * DOWN, rate_func=window(0, 0.6)),
                      LaggedStart(*[Create(b) for b in red3], lag_ratio=0.02), run_time=0.9)
            beat.wait_until("no aim", offset=-0.15)
            self.play(FadeIn(tagA3, shift=0.1 * UP), FadeIn(scoreA, shift=0.1 * UP), run_time=0.7)
            beat.wait_until("map B", offset=-0.2)
            self.play(FadeIn(tagB3, shift=0.1 * UP), FadeIn(scoreB, shift=0.1 * UP), run_time=0.7)
            beat.wait_until("rule", offset=-0.2)
            self.play(B2.frame.animate(rate_func=there_and_back).set_stroke(YELLOW, width=6),
                      flag(tagB3), run_time=0.8)

        self.end_card()
