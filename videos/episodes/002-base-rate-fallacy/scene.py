"""Sample Space, episode 2: When a 99% Accurate Test Says You're Sick (base-rate fallacy).

    videos/toolkit/render.sh --preview videos/episodes/002-base-rate-fallacy/scene.py Episode /tmp/ep2.mp4
    videos/toolkit/render.sh videos/episodes/002-base-rate-fallacy/scene.py Episode \
        videos/episodes/002-base-rate-fallacy/final.mp4

Premise: 1 in 500 people sick, the test catches 99 % and wrongly flags 1 % of the healthy.
Per 10,000 people: 20 sick -> 19.8 positive, 9,980 healthy -> 99.8 positive; P(sick | +) = 16.6 % ("17 %").

Palette (one meaning each, see script.md):
    RED    has the condition the test looks for (sick / on a police watch list)
    BLUE   does not have it (healthy / not on a list)
    YELLOW a positive result (the evidence): the + badge, the test beam, the outline of the positives
    GREEN  the correct answer (doctors and students who chose it, Manrai et al. 2014)
    GRAY   the naive rule (and accuracy, the naive score), secondary labels, citations
    low opacity: ruled out (tested negative) / context
"""
from __future__ import annotations

import numpy as np
from manim import *
from sample_space import *
from sample_space import style as ss_style

PX = 1 / 135                       # one 1080p pixel in scene units
N_SIDE = 100                       # 100 x 100 = 10,000 people
CELL_PX, SQ_PX = 8, 6              # each person: a 6 px square in an 8 px cell
G = N_SIDE * CELL_PX * PX          # grid side (5.93 units)
CELL = CELL_PX * PX

PREV_N = 500                       # 1 in 500 sick
N_RARE = 20                        # 10,000 / 500
N_FP = 100                         # 1 % of 9,980 = 99.8, shown as 100 people
N_POS = N_RARE + N_FP              # 120 positives
STRIP_COLS = N_POS // 5            # 24 x 5 strip


def snap(v: float) -> float:
    """Snap a coordinate to the 1080p pixel lattice so raster grids stay crisp."""
    return round(v * 135) / 135


GRID_C = np.array([snap(-3.39), snap(-0.09), 0.0])
GRID_L, GRID_T = GRID_C[0] - G / 2, GRID_C[1] + G / 2
GRID_R, GRID_B = GRID_C[0] + G / 2, GRID_C[1] - G / 2

# right-hand panel (table + meter) during the counting beats
ROW_Y = {"sick": 2.3, "healthy": 1.3}
HEADER_Y = 3.08
X_DOT, X_LABEL, X_COUNT_R, X_ARROW, X_RES_L = 0.55, 0.85, 3.35, (3.55, 4.8), 5.02

METER_W, METER_H = 4.8, 0.34
METER_OPEN = np.array([3.8, 0.0, 0])        # bar centre in the cold open
METER_GRID = np.array([3.8, -1.0, 0])       # ... while the grid is on screen
METER_LOW = np.array([-3.0, -1.0, 0])       # ... where the 120 positives first gather under it
METER_STRIP = np.array([-3.0, 2.45, 0])     # ... with the 120 positives hanging below it
DY_RISE = METER_STRIP[1] - METER_LOW[1]
LAND_DY = -0.6                              # the landing sits 0.6 lower than the cold open
METER_LAND = METER_OPEN + np.array([0, LAND_DY, 0])
TITLE_BUFF = 0.62                           # meter title always sits ABOVE the bar
STRIP_TITLE_BUFF = 0.3
WAFFLE_OPEN = np.array([1.95, -1.72, 0])    # the surveyed doctors, under the cold-open meter

# Cardiff 2017 (South Wales Police figures, BBC News 4 May 2018; Davies et al. 2018)
ALERTS, ALERTS_RIGHT = 2470, 173            # 2,297 wrong, 173 counted right (7.0 %)
AL_ROWS, AL_COLS, AL_CELL = 26, 95, 8       # 26 x 95 = 2,470 cells of 8 px
K_CARDIFF = AL_COLS * AL_CELL / (METER_W * 135)   # bar width = raster width (760 px)
CARDIFF_BAR = np.array([snap(3.05), snap(2.45), 0])
CROWD_N, CROWD_CELL, CROWD_SQ = 100, 6, 4   # 100 x 100 squares, 1 square = 17 of 170,000 people
CROWD_G = CROWD_N * CROWD_CELL * PX         # 600 px = 4.44 units, an integer pixel pitch
CROWD_C = np.array([snap(-3.65), snap(0.05), 0])
N_LISTED = 71                               # ceil(1,200 / 17): squares holding a listed face, at most
CROWD_LIT = 145                             # 2,470 alerts / 17 per square ~ 145 squares
LIT_RED = 10                                # 173 right / 17 per square ~ 10 squares
BLK_COLS, BLK_ROWS = 29, 5                  # 145 blocks of ~17 alerts each in the raster
SIX_NATIONS = 0.46                          # Davies et al. 2018: 46 % judged true (Six Nations 2018)

# Manrai et al. 2014 (JAMA Intern Med 174:991): 61 doctors and medical students, prevalence
# 1/1000, false-positive rate 5 %.  14 of 61 right (2 %), 27 of 61 said 95 % (the test's own
# accuracy), 20 gave other answers.  Shown per 100: 23 / 44 / 33 (sums to 100).
MANRAI = {"2": 23, "95": 44, "other": 33}
EVALUATORS_CL = 0.03                        # Davies et al. 2018: 78 of 2,632 at the final (3 %)


def rgb255(c) -> np.ndarray:
    return np.array(ManimColor(c).to_rgb(), dtype=np.float32) * 255


def emph(m: Mobject, color=None, scale: float = 1.15, run_time: float = 0.8):
    """A <= 1 s scale pulse that keeps the object's own colours (yellow means 'tested +'
    in this episode, so the house yellow flag() is not used)."""
    return m.animate(rate_func=there_and_back, run_time=run_time).scale(scale)


def early(t: float) -> float:
    """Rate function: done in the first 30 % of the animation (clear the old thing first)."""
    return smooth(min(1.0, t / 0.3))


def late(t: float) -> float:
    """Rate function: starts after 35 % of the animation (the new thing arrives second)."""
    return smooth(max(0.0, (t - 0.35) / 0.65))


def last_quarter(t: float) -> float:
    """Rate function: only the last 25 % (a label that waits until a moving bar has passed)."""
    return smooth(max(0.0, (t - 0.75) / 0.25))


def out_first(t: float) -> float:
    return smooth(min(1.0, t / 0.35))


def in_second(t: float) -> float:
    return smooth(max(0.0, (t - 0.4) / 0.6))


def window(a: float, b: float):
    """Rate function that runs only between a and b (fractions of the animation)."""
    return lambda t: smooth(min(1.0, max(0.0, (t - a) / (b - a))))


def swap(old: Mobject, new: Mobject, shift=0.16 * UP, shift_in=None, t_out=(0.0, 0.45),
         t_in=(0.3, 1.0)) -> list:
    """Replace a glyph without a cross-fade, like an odometer: the old one rolls up and out
    while the new one rolls up from below, so the two never overprint (in the brief overlap
    of the two windows they are 0.3 apart and both nearly transparent)."""
    return [FadeOut(old, shift=shift, rate_func=window(*t_out)),
            FadeIn(new, shift=shift if shift_in is None else shift_in, rate_func=window(*t_in))]


def swap_num(old, new, **kw) -> list:
    return swap(old, new, shift=0.14 * UP, **kw)


def swap_den(old, new, **kw) -> list:
    return swap(old, new, shift=0.14 * UP, **kw)


class Flight:
    """A copy of `dst` that leaves `src` (starting `lift` above it, invisible), fades in along
    a path (a cubic Bezier through c1, c2, or a smooth curve through the points `via`) and lands
    exactly on `dst`.  It never double-strikes its source.
    Usage: self.add(f.mob); self.play(f.anim, ...); f.land(self)  (see Episode.fly)."""

    def __init__(self, src: Mobject, dst: Mobject, c1=None, c2=None, via=None, lift: float = 0.2,
                 fade: float = 0.3, rate_func=smooth, k0: float | None = None):
        self.dst = dst
        base = dst.copy()
        if k0 is None:
            k0 = (src.height / dst.height) if dst.height > 1e-6 else 1.0
        p0 = src.get_center() + lift * UP
        p3 = dst.get_center()
        if via is not None:
            path = VMobject().set_points_smoothly([p0, *[np.array(v, dtype=float) for v in via], p3])
        else:
            c1 = p0 + (p3 - p0) / 3 if c1 is None else np.array(c1, dtype=float)
            c2 = p0 + 2 * (p3 - p0) / 3 if c2 is None else np.array(c2, dtype=float)
            path = CubicBezier(p0, c1, c2, p3)
        self.path = path
        self.mob = base.copy().set_opacity(0)

        def upd(m, a):
            m.become(base.copy().scale(k0 + (1 - k0) * a).move_to(path.point_from_proportion(a)))
            m.set_opacity(min(1.0, a / fade))
        self.anim = UpdateFromAlphaFunc(self.mob, upd, rate_func=rate_func)

    def land(self, scene: Scene):
        scene.remove(self.mob)
        scene.add(self.dst)


def plus_badge(r: float = 0.3) -> VGroup:
    disk = Circle(radius=r, fill_color=YELLOW, fill_opacity=1, stroke_width=0)
    a = 0.45 * r
    bar_w = max(2.0, 16 * r)
    cross = VGroup(Line(LEFT * a, RIGHT * a, stroke_width=bar_w, color=BG),
                   Line(DOWN * a, UP * a, stroke_width=bar_w, color=BG))
    return VGroup(disk, cross)


def ppv(n: float) -> float:
    """P(sick | +) for prevalence 1 in n, sensitivity 99 %, false-positive rate 1 %."""
    p = 1.0 / n
    return 0.99 * p / (0.99 * p + 0.01 * (1 - p))


def n_of(u: float) -> float:
    """Prevalence sweep: 1 in 500 (u = 0) to 1 in 2 (u = 1), log-spaced."""
    return 10 ** (np.log10(PREV_N) * (1 - u) + np.log10(2.0) * u)


def u_of(n: float) -> float:
    return (np.log10(PREV_N) - np.log10(n)) / (np.log10(PREV_N) - np.log10(2.0))


def waffle(center, r: float = 0.065, step: float = 0.165) -> VGroup:
    """Manrai et al. 2014, one dot per percent of the 61 respondents, grouped by answer:
    23 gave the right answer (2 %, green), 44 said 95 % (the test's own accuracy, the naive
    rule: grey), 33 gave other wrong answers (grey)."""
    dots = VGroup()
    k = 0
    for key, n in MANRAI.items():
        for _ in range(n):
            row, col = divmod(k, 10)
            d = Dot([center[0] + (col - 4.5) * step, center[1] + (4.5 - row) * step, 0], radius=r,
                    color=GREEN if key == "2" else GRAY)
            d.set_opacity(0.95 if key == "2" else 0.55)
            d.answer, d.k = key, k
            dots.add(d)
            k += 1
    return dots


def swatch(color, side: float = 0.17, opacity: float = 1.0) -> Square:
    return Square(side, fill_color=color, fill_opacity=opacity, stroke_width=0)


# =========================================================================== population
class Population:
    """10,000 people as a raster (one ImageMobject), driven by ValueTrackers.

    Counts are *expected* counts (natural frequencies), rounded to whole people:
      half sick:  5,000 sick -> 4,950 test +;   5,000 healthy -> 50 test +
      1 in 500:      20 sick ->    20 test + (19.8); 9,980 healthy -> 100 test + (99.8)
    """

    def __init__(self, seed: int = 7):
        rng = np.random.default_rng(seed)
        n = N_SIDE * N_SIDE
        rare: list[tuple[int, int]] = []
        while len(rare) < N_RARE:                 # twenty sick people, spread out
            r, c = (int(v) for v in rng.integers(6, 94, size=2))
            if all((r - r2) ** 2 + (c - c2) ** 2 >= 14 ** 2 for r2, c2 in rare):
                rare.append((r, c))
        rare_idx = np.array([r * N_SIDE + c for r, c in rare])
        others = rng.permutation(np.setdiff1d(np.arange(n), rare_idx))
        n_extra = 5000 - N_RARE
        extra, healthy50 = others[:n_extra], others[n_extra:]
        self.n = n
        self.rare = np.zeros(n, bool)
        self.rare[rare_idx] = True
        self.sick50 = self.rare.copy()
        self.sick50[extra] = True
        sick_idx = np.flatnonzero(self.sick50)
        self.rank_in = np.full(n, 9.0, np.float32)       # blue -> red order (to 50 %)
        self.rank_in[sick_idx] = rng.permutation(len(sick_idx)) / len(sick_idx)
        self.rank_out = np.full(n, 9.0, np.float32)      # red -> blue order (to 1 in 500)
        self.rank_out[extra] = rng.permutation(len(extra)) / len(extra)
        # scenario A (half sick): 99 % of 5,000 sick and 1 % of 5,000 healthy test +
        self.posA = np.zeros(n, bool)
        self.posA[sick_idx] = True
        self.posA[rng.choice(sick_idx, 50, replace=False)] = False
        self.posA[rng.choice(healthy50, 50, replace=False)] = True
        # scenario B (1 in 500): the 20 sick and 100 of 9,980 healthy test +
        self.posB = self.rare.copy()
        self.posB[rng.choice(np.flatnonzero(~self.rare), N_FP, replace=False)] = True
        assert self.posA[self.sick50].sum() == 4950 and self.posA[~self.sick50].sum() == 50
        assert self.posB[self.rare].sum() == N_RARE and self.posB[~self.rare].sum() == N_FP
        self.row = np.arange(n) // N_SIDE
        self.col = np.arange(n) % N_SIDE
        self.colf = (self.col + 0.5) / N_SIDE

        self.flip_in = ValueTracker(0.0)
        self.flip_out = ValueTracker(0.0)
        self.sweep = ValueTracker(0.0)
        self.dim = ValueTracker(0.22)          # opacity of people who tested negative
        self.opacity = ValueTracker(0.0)
        self.scenario = 0
        self.hidden = np.zeros(n, bool)

        m = np.zeros((CELL_PX, CELL_PX), np.float32)
        m[1:1 + SQ_PX, 1:1 + SQ_PX] = 1.0
        self.mask = np.tile(m, (N_SIDE, N_SIDE))
        self.red, self.blue = rgb255(RED), rgb255(BLUE)
        self.image = ImageMobject(self.pixels())
        self.image.height = G
        self.image.move_to(GRID_C)
        alg = "nearest" if config.pixel_height >= 1080 else "bilinear"
        self.image.set_resampling_algorithm(RESAMPLING_ALGORITHMS[alg])
        self.image.add_updater(lambda m: setattr(m, "pixel_array", self.pixels()))

    # -- state
    def sick_now(self) -> np.ndarray:
        s = self.sick50 & (self.rank_in < self.flip_in.get_value())
        return s & ~(self.rank_out < self.flip_out.get_value())

    def positives(self) -> np.ndarray:
        return self.posA if self.scenario == 0 else self.posB

    def tested(self) -> np.ndarray:
        return self.colf < self.sweep.get_value()

    def counts(self) -> dict:
        sick = self.sick_now()
        hit = self.tested() & self.positives()
        return {"sick": int(sick.sum()), "healthy": int(self.n - sick.sum()),
                "sick+": int((hit & sick).sum()), "healthy+": int((hit & ~sick).sum())}

    def pixels(self) -> np.ndarray:
        sick = self.sick_now()
        a = np.where(self.tested() & ~self.positives(), self.dim.get_value(), 1.0)
        a = a * self.opacity.get_value()
        a[self.hidden] = 0.0
        cells = np.empty((self.n, 4), np.float32)
        cells[:, :3] = np.where(sick[:, None], self.red, self.blue)
        cells[:, 3] = 255 * a
        big = cells.reshape(N_SIDE, N_SIDE, 4).repeat(CELL_PX, 0).repeat(CELL_PX, 1)
        big[..., 3] *= self.mask
        return big.astype(np.uint8)

    def cell_center(self, i: int) -> np.ndarray:
        return np.array([GRID_L + (self.col[i] + 0.5) * CELL, GRID_T - (self.row[i] + 0.5) * CELL, 0])


class Crowd:
    """The ~170,000 people in Cardiff as 100 x 100 squares (1 square ~ 17 people, an
    illustration).  Blue = not on a watch list.  71 squares (1,200 / 17, an upper bound: every
    listed face present) turn red.  The camera beam flags 145 squares (~2,470 alerts / 17): 10 of
    them red (~173 counted right / 17), 135 blue.  Squares the beam clears dim (ruled out).

    The 600 px raster sits on the pixel lattice and is never scaled, so it has no moire."""

    BASE = 0.55                                 # opacity of an unchecked square (context)
    RED_PX = 6                                  # listed squares fill their whole cell, to read

    def __init__(self, seed: int = 11):
        rng = np.random.default_rng(seed)
        n = CROWD_N * CROWD_N
        self.n = n
        red: list[tuple[int, int]] = []
        while len(red) < N_LISTED:              # listed faces, scattered through the crowd
            r, c = (int(v) for v in rng.integers(3, 97, size=2))
            if all((r - r2) ** 2 + (c - c2) ** 2 >= 6 ** 2 for r2, c2 in red):
                red.append((r, c))
        self.red_idx = np.array([r * CROWD_N + c for r, c in red])
        self.lit_red = set(int(i) for i in rng.choice(self.red_idx, LIT_RED, replace=False))
        others = np.setdiff1d(np.arange(n), self.red_idx)
        self.lit_blue = [int(i) for i in rng.choice(others, CROWD_LIT - LIT_RED, replace=False)]
        self.row = np.arange(n) // CROWD_N
        self.col = np.arange(n) % CROWD_N
        self.colf = (self.col + 0.5) / CROWD_N
        self.sweep = ValueTracker(0.0)
        self.dim = 0.22                         # squares the camera cleared: ruled out, dimmed
        self.opacity = ValueTracker(0.0)
        self.hidden = np.zeros(n, bool)
        m = np.zeros((CROWD_CELL, CROWD_CELL), np.float32)
        m[1:1 + CROWD_SQ, 1:1 + CROWD_SQ] = 1.0
        self.mask = np.tile(m, (CROWD_N, CROWD_N))
        self.blue = rgb255(BLUE)
        self.image = ImageMobject(self.pixels())
        self.image.height = CROWD_G
        self.image.move_to(CROWD_C)
        self.image.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        self.image.add_updater(lambda m: setattr(m, "pixel_array", self.pixels()))
        self.left = CROWD_C[0] - CROWD_G / 2
        self.top = CROWD_C[1] + CROWD_G / 2
        sq = (CROWD_SQ + 1) * PX                # a flagged square grows to 5 px: easier to see
        # vector overlays: the listed (red) squares and the flagged squares' cores + yellow rings
        self.red_sq = VGroup(*[Square(self.RED_PX * PX, fill_color=RED, fill_opacity=1,
                                      stroke_width=0).move_to(self.cell_center(i))
                               for i in self.red_idx])
        self.lit_idx = sorted(list(self.lit_red) + self.lit_blue,
                              key=lambda i: (self.col[i], self.row[i]))
        self.cores, self.rings = VGroup(), VGroup()
        red_of = {int(i): s for i, s in zip(self.red_idx, self.red_sq)}
        for i in self.lit_idx:
            core = red_of[i] if i in self.lit_red else \
                Square(sq, fill_color=BLUE, fill_opacity=self.BASE, stroke_width=0).move_to(
                    self.cell_center(i))
            self.cores.add(core)
            self.rings.add(Square(sq + 5 * PX, stroke_color=YELLOW, stroke_width=1.8,
                                  stroke_opacity=0, fill_opacity=0).move_to(self.cell_center(i)))

    def tested_at(self, i: int) -> bool:
        return self.colf[i] < self.sweep.get_value()

    def start_overlays(self):
        """From the beam on, vector squares follow it: flagged ones light up with a yellow
        ring, the listed squares the camera passes over without flagging dim."""
        self.hidden[self.red_idx] = True
        self.hidden[self.lit_blue] = True
        lit = set(self.lit_idx)
        for i, s in zip(self.red_idx, self.red_sq):
            if int(i) not in lit:
                s.add_updater(lambda m, i=int(i): m.set_fill(
                    opacity=self.dim if self.tested_at(i) else 1.0))
        for i, core, ring in zip(self.lit_idx, self.cores, self.rings):
            red = i in self.lit_red
            core.add_updater(lambda m, i=i, red=red: m.set_fill(
                opacity=1.0 if (red or self.tested_at(i)) else self.BASE))
            ring.add_updater(lambda m, i=i: m.set_stroke(opacity=1.0 if self.tested_at(i) else 0.0))

    def pixels(self) -> np.ndarray:
        tested = self.colf < self.sweep.get_value()
        a = np.where(tested, self.dim, self.BASE) * self.opacity.get_value()
        a[self.hidden] = 0.0
        cells = np.empty((self.n, 4), np.float32)
        cells[:, :3] = self.blue
        cells[:, 3] = 255 * a
        big = cells.reshape(CROWD_N, CROWD_N, 4).repeat(CROWD_CELL, 0).repeat(CROWD_CELL, 1)
        big[..., 3] *= self.mask
        return big.astype(np.uint8)

    def cell_center(self, i: int) -> np.ndarray:
        c = CROWD_CELL * PX
        return np.array([self.left + (self.col[i] + 0.5) * c, self.top - (self.row[i] + 0.5) * c, 0])


def alert_raster() -> np.ndarray:
    """The 2,470 Cardiff alerts as a 26 x 95 raster, filled column by column: the 173 counted
    right first (red), then the 2,297 wrong ones (blue)."""
    k = np.arange(ALERTS).reshape(AL_COLS, AL_ROWS).T          # column-major index
    rgb = np.empty((AL_ROWS, AL_COLS, 3), np.float32)
    rgb[:] = np.where((k < ALERTS_RIGHT)[..., None], rgb255(RED), rgb255(BLUE))
    big = np.zeros((AL_ROWS * AL_CELL, AL_COLS * AL_CELL, 4), np.float32)
    cell = np.zeros((AL_CELL, AL_CELL), np.float32)
    cell[1:AL_CELL - 1, 1:AL_CELL - 1] = 1.0
    big[..., :3] = rgb.repeat(AL_CELL, 0).repeat(AL_CELL, 1)
    big[..., 3] = 255 * np.tile(cell, (AL_ROWS, AL_COLS))
    return big.astype(np.uint8)


# =========================================================================== meter
class Meter:
    """'chance you're sick': a 100 % bar split into red (sick) and blue (healthy) shares
    of the people who tested positive.  The title always sits above the bar."""

    def __init__(self, center):
        self.share = ValueTracker(0.0)
        self.fill = ValueTracker(0.0)
        self.track = Rectangle(width=METER_W, height=METER_H, stroke_color=GRAY,
                               stroke_width=2.5, fill_opacity=0).move_to(center)
        self.red = Polygon(ORIGIN, RIGHT, UP, fill_color=RED, fill_opacity=1, stroke_width=0)
        self.blue = Polygon(ORIGIN, RIGHT, UP, fill_color=BLUE, fill_opacity=1, stroke_width=0)
        self.red.add_updater(lambda m: self._seg(m, 0.0, self.share.get_value()))
        self.blue.add_updater(lambda m: self._seg(m, self.share.get_value(), 1.0))
        self.value = DecimalNumber(0, num_decimal_places=0, unit=r"\%", font_size=MATH,
                                   color=INK)
        self.value.add_updater(self._place_value)
        self.qmark = MathTex("?", font_size=EQ, color=INK)
        self.qmark.add_updater(lambda m: m.next_to(self.track, LEFT, buff=0.22))
        self.title = label("chance you're sick", size=LABEL)
        self.title.move_to(self.title_at(center))
        self.bar = VGroup(self.red, self.blue, self.track)
        for m in (self.red, self.blue):
            m.update()
        self.value.update()

    def title_at(self, center, buff: float = TITLE_BUFF, k: float = 1.0, title=None) -> np.ndarray:
        t = title if title is not None else self.title
        left = center[0] - k * METER_W / 2
        return np.array([left + t.width / 2, center[1] + k * METER_H / 2 + buff + t.height / 2, 0])

    def _seg(self, m, a, b):
        f = self.fill.get_value()
        l, w = self.track.get_left()[0], self.track.width
        y0, y1 = self.track.get_bottom()[1], self.track.get_top()[1]
        x0, x1 = l + w * a * f, l + w * b * f
        if x1 - x0 < 1e-4:
            x1 = x0 + 1e-4
        m.set_points_as_corners([[x0, y0, 0], [x1, y0, 0], [x1, y1, 0], [x0, y1, 0], [x0, y0, 0]])

    def _place_value(self, m):
        m.set_value(round(100 * self.share.get_value()))
        m.next_to(self.track, LEFT, buff=0.22)

    def x_at(self, s: float) -> float:
        return self.track.get_left()[0] + self.track.width * s


# =========================================================================== formula
def colour_glyphs(m: MathTex, part: int, spans):
    for a, b, col in spans:
        m[part][a:b].set_color(col)
    return m


def lhs_tex(fs) -> MathTex:
    m = MathTex(r"P(\text{sick}\mid +)", font_size=fs)
    return colour_glyphs(m, 0, [(2, 6, RED), (7, 8, YELLOW)])


def frac(num: Mobject, den: Mobject, buff: float = 0.18) -> VGroup:
    w = max(num.width, den.width) + 0.2
    bar = Line(LEFT * w / 2, RIGHT * w / 2, stroke_width=3, color=INK)
    num.next_to(bar, UP, buff=buff)
    den.next_to(bar, DOWN, buff=buff)
    return VGroup(num, bar, den)


FS = EQ - 8          # 44: main equation size
FS4 = FS - 4         # 40: the named (wider) forms
EQ_Y = -1.55


def row(*ms, buff=0.26, y=EQ_Y) -> VGroup:
    g = VGroup(*ms).arrange(RIGHT, buff=buff)
    return g.move_to([0, y, 0])


def build_stage(k: str):
    """Returns (lhs, eq, num, bar, den, tail) for stage k of the derivation.

    1   positives counted off the strip      20 / (20 + 100)
    2a  red count = people x rate            20 x 0.99 / (20 x 0.99 + 100)
    2   both counts = people x rate          20 x 0.99 / (20 x 0.99 + 9,980 x 0.01)   (exact)
    3   head counts / 10,000 -> shares       0.002 x 0.99 / (0.002 x 0.99 + 0.998 x 0.01)
    4   the numbers get their names          Bayes' theorem
    Four changes in all, each at least 5 s after the last (BAR: one new equation per 5 s).
    """
    fs = FS if k in ("1", "2a", "2", "3") else FS4
    lhs, eq = lhs_tex(fs), MathTex("=", font_size=fs)
    tail = MathTex(r"\approx", r"17\%", font_size=fs)
    if k == "1":
        num = MathTex("20", font_size=fs, color=RED)
        den = MathTex("20", "+", "100", font_size=fs)
        den[0].set_color(RED)
        den[2].set_color(BLUE)
    elif k == "2a":
        num = MathTex("20", r"\times", "0.99", font_size=fs)
        num[0].set_color(RED)
        den = MathTex("20", r"\times", "0.99", "+", "100", font_size=fs)
        den[0].set_color(RED)
        den[4].set_color(BLUE)
    elif k in ("2", "3"):
        a, b = ("20", "9{,}980") if k == "2" else ("0.002", "0.998")
        num = MathTex(a, r"\times", "0.99", font_size=fs)
        num[0].set_color(RED)
        den = MathTex(a, r"\times", "0.99", "+", b, r"\times", "0.01", font_size=fs)
        den[0].set_color(RED)
        den[4].set_color(BLUE)
    else:
        num = MathTex(r"P(\text{sick})", r"\,P(+\mid\text{sick})", font_size=fs)
        den = MathTex(r"P(\text{sick})", r"\,P(+\mid\text{sick})", "+", r"P(\text{healthy})",
                      r"\,P(+\mid\text{healthy})", font_size=fs)
        for m in (num, den):
            colour_glyphs(m, 0, [(2, 6, RED)])
            colour_glyphs(m, 1, [(2, 3, YELLOW), (4, 8, RED)])
        colour_glyphs(den, 3, [(2, 9, BLUE)])
        colour_glyphs(den, 4, [(2, 3, YELLOW), (4, 11, BLUE)])
        tail = None
    # the named form gets more air above and below its bar: the boxes drawn round its
    # numerator and denominator then stay >= 0.15 clear of the bar
    f = frac(num, den, buff=0.3 if k == "4" else 0.18)
    row(lhs, eq, f, *([tail] if tail is not None else []))
    return lhs, eq, num, f[1], den, tail


# =========================================================================== scene
class Episode(NarratedScene):
    EPISODE = 2
    TITLE = "When a 99% Accurate Test Says You're Sick"
    SPEED = 0.84
    PRONUNCIATIONS = {}

    # ------------------------------------------------------------------ diagram
    def build_diagram(self, dy: float = 0.0, rate_at: float = 0.5):
        red_c = np.array([-4.5, 1.55 + dy, 0])
        blue_c = np.array([-4.5, -1.55 + dy, 0])
        plus_c = np.array([-0.75, dy, 0])
        d = {}
        d["red"] = Dot(red_c, radius=0.28, color=RED)
        d["blue"] = Dot(blue_c, radius=0.28, color=BLUE)
        d["sick"] = label("sick", color=RED).next_to(d["red"], LEFT, buff=0.22)
        d["healthy"] = label("healthy", color=BLUE).next_to(d["blue"], LEFT, buff=0.22)
        d["prev"] = MathTex("1", r"\text{ in }", "500", font_size=44).next_to(d["red"], UP,
                                                                               buff=0.25)
        d["plus"] = plus_badge(0.3).move_to(plus_c)
        d["ring"] = Circle(radius=0.62, color=INK, stroke_width=3).move_to(plus_c)
        d["you"] = label("you").next_to(d["ring"], DOWN, buff=0.2)

        def arrow(a, b, col):
            u = (b - a) / np.linalg.norm(b - a)
            return Arrow(a + 0.42 * u, b - 0.76 * u, buff=0, color=col, stroke_width=5,
                         tip_length=0.24, max_tip_length_to_length_ratio=0.2,
                         max_stroke_width_to_length_ratio=20)
        d["ra"] = arrow(red_c, plus_c, RED)
        d["ba"] = arrow(blue_c, plus_c, BLUE)

        def rate(tex, a, b, side):
            p = a + rate_at * (b - a)
            u = (b - a) / np.linalg.norm(b - a)
            nrm = np.array([-u[1], u[0], 0]) * side
            return MathTex(tex, font_size=MATH).move_to(p + 0.68 * nrm)
        d["r99"] = rate(r"99\%", red_c, plus_c, +1)
        d["r1"] = rate(r"1\%", blue_c, plus_c, -1)
        d["centers"] = (red_c, blue_c, plus_c)
        return d

    def end_card(self, hold: float = 0.8, run_time: float = 0.5):
        """Series card, with the wordmark's Omega in ink (blue means 'healthy' here)."""
        card = ss_style.end_card(self.EPISODE, self.TITLE)
        card[0][0].set_color(INK)
        mobs = list(self.mobjects)
        self.play(*[FadeOut(m) for m in mobs], FadeIn(card, shift=0.1 * UP), run_time=run_time)
        self.hold(hold)

    def fly(self, flights, *anims, run_time: float):
        """Play Flight copies together with other animations, then land them."""
        for f in flights:
            self.add(f.mob)
        self.play(*[f.anim for f in flights], *anims, run_time=run_time)
        for f in flights:
            f.land(self)

    # ------------------------------------------------------------------ construct
    def construct(self):
        pop = Population()
        D = self.build_diagram()
        meter = Meter(METER_OPEN)

        # ============================================================ 1. cold open
        # first frame: the evidence on the left, the unknown (ghosted) on the right
        meter.track.set_stroke(opacity=0.3)
        meter.title.set_opacity(0.3)
        meter.qmark.set_opacity(0.3)
        self.add(D["red"], D["blue"], D["sick"], D["healthy"], D["prev"],
                 meter.track, meter.title, meter.qmark)
        ghost = waffle(WAFFLE_OPEN)
        g_lbls = VGroup(label("doctors & students", size=26, color=GRAY),
                        label("23% right", size=26, color=GREEN))
        g_lbls.arrange(DOWN, buff=0.16, aligned_edge=LEFT).next_to(ghost, RIGHT, buff=0.32)
        said95 = label("44% said 95%", size=26, color=GRAY)
        said95.next_to(g_lbls, DOWN, buff=0.16, aligned_edge=LEFT)
        g_unit = label("1 dot = 1%", size=22, color=GRAY).next_to(ghost, DOWN, buff=0.2)
        cite_g = citation("Manrai et al., 2014 · JAMA Intern. Med.")
        with self.narrate("One in five hundred people has this disease. A test catches ninety-nine "
                          "percent of cases and wrongly flags one percent of the healthy. If yours "
                          "says positive, what's the chance you're sick? [pause 0.3] Pick a "
                          "number. [pause 1.6]", speed=0.86) as beat:
            beat.wait_until("five hundred", offset=-0.15)
            self.play(emph(D["prev"]), emph(D["red"]), run_time=0.9)
            beat.wait_until("catches", offset=-0.1)
            self.play(GrowArrow(D["ra"]), FadeIn(D["plus"], scale=0.6),
                      run_time=beat.until("ninety-nine", offset=-0.05))
            self.play(Write(D["r99"]), run_time=0.7)
            beat.wait_until("wrongly", offset=-0.1)
            self.play(GrowArrow(D["ba"]), run_time=beat.until("one percent", offset=-0.05))
            self.play(Write(D["r1"]), run_time=0.6)
            beat.wait_until("yours", offset=-0.1)
            self.play(Create(D["ring"]), FadeIn(D["you"], shift=0.1 * UP),
                      run_time=beat.until("positive", offset=0.2))
            self.play(emph(D["plus"], scale=1.25), run_time=0.6)
            beat.wait_until("what's", offset=-0.1)
            self.play(meter.track.animate.set_stroke(opacity=1.0),
                      meter.title.animate.set_opacity(1.0), meter.qmark.animate.set_opacity(1.0),
                      run_time=0.9)
            beat.wait_until("Pick", offset=-0.1)
            self.play(emph(meter.qmark, scale=1.4), run_time=0.9)

        # the baseline arrives only after the viewer has committed
        with self.narrate("Most doctors and medical students given a problem like this got it "
                          "wrong.") as beat:
            self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in ghost], lag_ratio=0.012),
                      FadeIn(g_lbls, shift=0.1 * RIGHT), FadeIn(g_unit, shift=0.1 * UP),
                      FadeIn(cite_g, shift=0.1 * UP),
                      run_time=beat.until("wrong", offset=0.1))

        # ============================================================ 2. stakes + naive rule
        naive_x = meter.x_at(0.99)
        marker = DashedLine([naive_x, METER_OPEN[1] - METER_H / 2 - 0.14, 0],
                            [naive_x, METER_OPEN[1] + METER_H / 2 + 0.14, 0],
                            color=GRAY, stroke_width=3, dash_length=0.06)
        naive_pct = MathTex(r"99\%", font_size=36, color=GRAY)
        naive_pct.next_to(marker, UP, buff=0.1).align_to(meter.track, RIGHT)
        naive_word = label("naive", size=26, color=GRAY)
        naive_word.next_to(naive_pct, LEFT, buff=0.18).align_to(naive_pct, DOWN)
        naive_lbl = VGroup(naive_word, naive_pct)
        meter_naive = VGroup(marker, naive_lbl)

        # the copy of "99%" rises off the arrow, travels above the meter title, and drops onto
        # the marker: it never crosses its source, the title or the bar outline
        fly = D["r99"].copy()
        p0, p3 = fly.get_center(), naive_pct.get_center()
        fly_path = CubicBezier(p0, p0 + 1.1 * UP, p3 + 1.4 * UP + 0.3 * LEFT, p3)
        fly_base = fly.copy()
        k_end = naive_pct.height / fly_base.height

        def fly_upd(m, a):
            # leaves its source fast (no double-struck glyph) and lands gently
            m.become(fly_base.copy().scale(1 + (k_end - 1) * a)
                     .set_color(interpolate_color(ManimColor(INK), ManimColor(GRAY), a))
                     .move_to(fly_path.point_from_proportion(a))
                     .set_opacity(min(1.0, a / 0.2)))
        said = VGroup(*[d for d in ghost if d.answer == "95"])
        others = VGroup(*[d for d in ghost if d.answer == "other"])
        with self.narrate("Their most common answer was the test's own accuracy, here ninety-nine "
                          "percent: you'd start treatment today.") as beat:
            # the most common wrong answer (95 %, the test's own accuracy) lights up: it is the
            # naive rule, so it is grey, the naive rule's colour
            beat.wait_until("most common", offset=-0.15)
            self.play(said.animate.set_opacity(1.0), others.animate.set_opacity(0.3),
                      FadeIn(said95, shift=0.08 * UP), run_time=0.9)
            beat.wait_until("accuracy", offset=-0.2)
            self.play(emph(D["r99"]), emph(D["r1"]), run_time=0.7)
            beat.wait_until("ninety-nine", offset=-0.45)
            self.add(fly)
            self.play(UpdateFromAlphaFunc(fly, fly_upd, rate_func=rush_from),
                      FadeOut(ghost, rate_func=early), FadeOut(g_lbls, rate_func=early),
                      FadeOut(said95, rate_func=early),
                      FadeOut(g_unit, rate_func=early), FadeOut(cite_g, rate_func=early),
                      run_time=1.2)
            self.remove(fly)
            self.add(naive_pct)
            self.play(FadeIn(naive_word, shift=0.08 * RIGHT), Create(marker), run_time=0.5)
            beat.wait_until("treatment", offset=-0.15)
            self.play(emph(VGroup(D["ring"], D["you"], D["plus"]), scale=1.12), run_time=0.9)

        # ============================================================ 3. naive build: half sick
        dot_s = Dot([X_DOT, ROW_Y["sick"], 0], radius=0.13, color=RED)
        dot_h = Dot([X_DOT, ROW_Y["healthy"], 0], radius=0.13, color=BLUE)
        lab_s = label("sick", color=RED)
        lab_s.move_to([X_LABEL + lab_s.width / 2, ROW_Y["sick"], 0])
        lab_h = label("healthy", color=BLUE)
        lab_h.move_to([X_LABEL + lab_h.width / 2, ROW_Y["healthy"], 0])

        def row_arrow(y, col):
            return Arrow([X_ARROW[0], y, 0], [X_ARROW[1], y, 0], buff=0, color=col,
                         stroke_width=5, tip_length=0.22, max_tip_length_to_length_ratio=0.2,
                         max_stroke_width_to_length_ratio=20)
        arr_s, arr_h = row_arrow(ROW_Y["sick"], RED), row_arrow(ROW_Y["healthy"], BLUE)
        rate_s = MathTex(r"99\%", font_size=MATH - 4).next_to(arr_s, UP, buff=0.15)
        rate_h = MathTex(r"1\%", font_size=MATH - 4).next_to(arr_h, UP, buff=0.15)
        res_x_c = X_RES_L + 0.5
        head_plus = plus_badge(0.19).move_to([res_x_c, HEADER_Y, 0])
        head_people = label("people", size=26, color=GRAY).move_to([X_COUNT_R - 0.55, HEADER_Y, 0])

        def counter(key, right=None, left=None, y=0.0):
            n = DecimalNumber(0, num_decimal_places=0, group_with_commas=True,
                              font_size=MATH - 4, color=INK)

            def upd(m):
                m.set_value(pop.counts()[key])
                if right is not None:
                    m.move_to([right - m.width / 2, y, 0])
                else:
                    m.move_to([left + m.width / 2, y, 0])
            n.add_updater(upd)
            n.update()
            return n
        cnt_s = counter("sick", right=X_COUNT_R, y=ROW_Y["sick"])
        cnt_h = counter("healthy", right=X_COUNT_R, y=ROW_Y["healthy"])
        res_s = counter("sick+", left=X_RES_L, y=ROW_Y["sick"])
        res_h = counter("healthy+", left=X_RES_L, y=ROW_Y["healthy"])

        grid_lbl = VGroup(label("10,000 people"), label("expected counts", size=26, color=GRAY))
        grid_lbl.arrange(RIGHT, buff=0.3, aligned_edge=DOWN)
        grid_lbl.move_to([GRID_C[0], GRID_T + 0.36, 0])

        beam = Line([0, GRID_T + 0.1, 0], [0, GRID_B - 0.1, 0], color=YELLOW, stroke_width=4)
        beam.add_updater(lambda m: m.move_to([GRID_L + G * pop.sweep.get_value(), GRID_C[1], 0]))

        # the diagram straightens into the counting table in three clean stages:
        # labels leave first, then the nodes / arrows / + travel (nothing textual in motion),
        # then the row labels and rates appear beside the parts that have landed
        plus_c0 = D["plus"].get_center()
        plus_path = CubicBezier(plus_c0, plus_c0 + 2.6 * UP, head_plus.get_center() + 2.4 * LEFT,
                                head_plus.get_center())
        plus_base = D["plus"].copy()
        k_plus = head_plus.width / plus_base.width

        def plus_upd(m, a):
            m.become(plus_base.copy().scale(1 + (k_plus - 1) * a)
                     .move_to(plus_path.point_from_proportion(a)))
        with self.narrate("Check that rule by counting. [pause 0.2] Here are ten thousand people, "
                          "and suppose half of them are sick.") as beat:
            self.play(FadeOut(D["sick"]), FadeOut(D["healthy"]), FadeOut(D["prev"]),
                      FadeOut(D["you"]), FadeOut(D["r99"]), FadeOut(D["r1"]),
                      Uncreate(D["ring"]),
                      meter.track.animate.move_to(METER_GRID),
                      meter.title.animate.move_to(meter.title_at(METER_GRID)),
                      meter_naive.animate.shift(METER_GRID - METER_OPEN), run_time=0.6)
            self.play(ReplacementTransform(D["red"], dot_s), ReplacementTransform(D["blue"], dot_h),
                      ReplacementTransform(D["ra"], arr_s), ReplacementTransform(D["ba"], arr_h),
                      UpdateFromAlphaFunc(D["plus"], plus_upd), run_time=1.0)
            self.remove(D["plus"])
            self.add(head_plus)
            self.play(FadeIn(lab_s, shift=0.1 * RIGHT), FadeIn(lab_h, shift=0.1 * RIGHT),
                      FadeIn(rate_s, shift=0.1 * DOWN), FadeIn(rate_h, shift=0.1 * DOWN),
                      run_time=beat.until("ten thousand", offset=-0.2, min_time=0.5))
            self.add(pop.image)
            self.play(pop.opacity.animate.set_value(1.0), FadeIn(grid_lbl, shift=0.1 * DOWN),
                      FadeIn(head_people), FadeIn(cnt_s), FadeIn(cnt_h),
                      run_time=beat.until("half", offset=-0.1))
            self.play(pop.flip_in.animate.set_value(1.0), run_time=beat.remaining() + 0.2,
                      rate_func=EASE)

        # ---------------------------------------------------------- test everyone
        with self.narrate("Test everyone. [pause 0.2] Ninety-nine percent of the sick light up, "
                          "and one percent of the healthy.") as beat:
            self.add(beam)
            self.play(FadeIn(beam), FadeIn(res_s), FadeIn(res_h), run_time=0.4)
            self.play(pop.sweep.animate.set_value(1.0), run_time=beat.remaining() - 0.2,
                      rate_func=LINEAR)
            self.play(FadeOut(beam), run_time=0.4)

        with self.narrate("Of the five thousand who lit up, ninety-nine percent are sick. "
                          "[pause 0.3] Here, the rule holds.") as beat:
            beat.wait_until("five", offset=-0.1)
            self.play(emph(res_s), emph(res_h), emph(head_plus), run_time=0.9)
            beat.wait_until("ninety-nine", offset=-0.3)
            meter.share.set_value(0.99)
            meter.value.update()
            self.add(meter.red, meter.blue, meter.track)
            self.play(meter.fill.animate.set_value(1.0), FadeOut(meter.qmark, rate_func=early),
                      FadeIn(meter.value, rate_func=late), run_time=1.2)
            beat.wait_until("holds", offset=-0.1)
            self.play(emph(naive_lbl), emph(meter.value), run_time=0.9)

        # ============================================================ 4. fail: one in five hundred
        rings = VGroup(*[Circle(radius=0.11, color=RED, stroke_width=2.5).move_to(pop.cell_center(i))
                         for i in np.flatnonzero(pop.rare)])
        with self.narrate("Now make the disease rare, like yours: one in five hundred. [pause 0.2] "
                          "That leaves twenty sick people.") as beat:
            self.play(pop.dim.animate.set_value(1.0), meter.fill.animate.set_value(0.0),
                      FadeOut(meter.value, rate_func=early),
                      FadeIn(meter.qmark, rate_func=late), run_time=0.8)
            pop.sweep.set_value(0.0)
            pop.dim.set_value(0.22)
            pop.scenario = 1
            meter.share.set_value(N_RARE / N_POS)
            self.play(pop.flip_out.animate.set_value(1.0),
                      run_time=beat.until("That leaves", offset=-0.25), rate_func=EASE)
            beat.wait_until("twenty sick", offset=-0.1)
            self.play(LaggedStart(*[Create(r) for r in rings], lag_ratio=0.08),
                      emph(cnt_s), run_time=1.4)

        with self.narrate("Run the same test. [pause 0.2] About twenty sick people light up, plus "
                          "one percent of the nine thousand nine hundred eighty healthy ones. "
                          "[pause 0.2] That's about a hundred.") as beat:
            self.play(FadeIn(beam), run_time=0.4)
            self.play(pop.sweep.animate.set_value(1.0),
                      run_time=beat.until("That's", offset=-0.5), rate_func=LINEAR)
            self.play(FadeOut(beam), run_time=0.4)
            beat.wait_until("hundred", occurrence=2, offset=-0.1)
            self.play(emph(res_h), run_time=0.8)

        brace = BraceBetweenPoints([meter.x_at(N_RARE / N_POS), METER_GRID[1] - METER_H / 2 - 0.05, 0],
                                   [naive_x, METER_GRID[1] - METER_H / 2 - 0.05, 0],
                                   direction=DOWN, color=GRAY)
        brace_lbl = label("6× too high", size=LABEL).next_to(brace, DOWN, buff=0.18)
        with self.narrate("So of a hundred and twenty positives, only twenty are sick.",
                          gap=0.2) as beat:
            beat.wait_until("hundred and twenty", offset=-0.1)
            self.play(emph(res_s), emph(res_h), run_time=0.9)
        with self.narrate("Seventeen percent.", speed=0.80, gap=1.0) as beat:
            beat.wait_until("seventeen", offset=-0.3)
            meter.value.update()
            self.play(meter.fill.animate.set_value(1.0), FadeOut(meter.qmark, rate_func=early),
                      FadeIn(meter.value, rate_func=late), run_time=1.1)
        with self.narrate("The rule said ninety-nine. [pause 0.2] Six times too high.",
                          speed=0.80, gap=1.0) as beat:
            beat.wait_until("ninety-nine", offset=-0.1)
            self.play(emph(naive_lbl), run_time=0.8)
            beat.wait_until("Six", offset=-0.15)
            self.play(GrowFromCenter(brace), FadeIn(brace_lbl, shift=0.1 * DOWN), run_time=0.9)

        with self.narrate("One percent sounds small, but here it's one percent of nearly "
                          "everyone.") as beat:
            self.play(emph(rate_h, scale=1.3), emph(arr_h), run_time=0.9)
            beat.wait_until("nearly", offset=-0.15)
            # "nearly everyone": the dimmed crowd of healthy negatives itself lights up
            self.play(pop.dim.animate(rate_func=there_and_back).set_value(0.62),
                      emph(cnt_h, scale=1.25), emph(res_h, scale=1.25), run_time=1.2)

        # ============================================================ 5. insight: shrink the space
        pos_idx = np.flatnonzero(pop.posB)
        red_idx = sorted([i for i in pos_idx if pop.rare[i]], key=lambda i: (pop.col[i], pop.row[i]))
        blue_idx = sorted([i for i in pos_idx if not pop.rare[i]], key=lambda i: (pop.col[i], pop.row[i]))
        strip_r = 0.074
        survivors = VGroup()
        for i in red_idx + blue_idx:
            col = RED if pop.rare[i] else BLUE
            survivors.add(Square(SQ_PX * PX, fill_color=col, fill_opacity=1, stroke_width=0)
                          .move_to(pop.cell_center(i)))
        big = [Dot(s.get_center(), radius=strip_r, color=s.get_fill_color()) for s in survivors]
        pos_lbl = label("120 people who tested +", t2c={"+": YELLOW}).move_to(grid_lbl)
        with self.narrate("Your positive result ruled out everyone who tested negative.",
                          speed=0.80, gap=0.6) as beat:
            pop.hidden[pos_idx] = True            # the positives become vector dots, same look
            self.add(survivors)
            beat.wait_until("ruled", offset=-0.1)
            # the header changes as the picture changes: 10,000 people -> the 120 who tested +
            self.play(pop.dim.animate.set_value(0.0),
                      *[Transform(s, b) for s, b in zip(survivors, big)],
                      FadeOut(rings, rate_func=early),
                      *swap(grid_lbl, pos_lbl, shift=0.2 * UP),
                      FadeOut(brace), FadeOut(brace_lbl), FadeOut(meter_naive),
                      run_time=beat.until("negative", offset=0.3))
        red_dots = survivors[:N_RARE]

        # the 120 positives line up in a strip; the meter joins them from the right (along an
        # empty row, crossing nothing), and the pair rises to make room for the algebra.
        # The strip hangs under the meter: its red columns sit under the red 17 %.
        sp = METER_W / STRIP_COLS
        strip_left = METER_STRIP[0] - METER_W / 2
        strip_top = METER_STRIP[1] - METER_H / 2 - 0.24 - sp / 2

        def slot(k, rows=5):
            c, r = divmod(k, rows)
            return np.array([strip_left + (c + 0.5) * sp, strip_top - r * sp, 0])
        slots = [slot(k) for k in range(N_POS)]
        low = DY_RISE * DOWN
        outline = SurroundingRectangle(VGroup(*[Dot(p, radius=strip_r) for p in slots]),
                                       color=YELLOW, buff=0.1, corner_radius=0.08, stroke_width=3)
        strip_lbl = label("120 people who tested +", size=LABEL, t2c={"+": YELLOW})
        strip_lbl.next_to(outline, DOWN, buff=0.2)
        outline.shift(low)
        strip_lbl.shift(low)
        with self.narrate("What's left is a smaller sample space: these hundred and twenty "
                          "people.", speed=0.80) as beat:
            self.play(LaggedStart(*[s.animate.move_to(p + low) for s, p in zip(survivors, slots)],
                                  lag_ratio=0.006),
                      run_time=beat.until("smaller", offset=0.1), rate_func=SMOOTH)
            self.play(meter.track.animate.move_to(METER_LOW),
                      meter.title.animate.move_to(meter.title_at(METER_LOW, STRIP_TITLE_BUFF)),
                      run_time=1.0, rate_func=SMOOTH)
            self.play(Create(outline), FadeIn(strip_lbl, shift=0.1 * UP),
                      run_time=beat.until("these", offset=0.1))
            self.remove(pop.image)
            pop.image.clear_updaters()
            self.play(VGroup(survivors, outline, strip_lbl, meter.track, meter.title)
                      .animate.shift(DY_RISE * UP),
                      FadeOut(pos_lbl, rate_func=early), run_time=1.0)
        meter.value.suspend_updating()            # the meter holds still through the algebra

        # stage 1: the red share of this crowd, counted with braces first
        S1 = build_stage("1")
        lhs1, eq1, num1, bar1, den1, tail1 = S1
        ob = outline.get_bottom()[1]
        red_span = Line([strip_left + 0.04, ob, 0], [strip_left + 4 * sp - 0.04, ob, 0])
        blue_span = Line([strip_left + 4 * sp + 0.04, ob, 0],
                         [strip_left + STRIP_COLS * sp - 0.04, ob, 0])
        br_r = Brace(red_span, DOWN, buff=0.08, color=RED)
        br_b = Brace(blue_span, DOWN, buff=0.08, color=BLUE)
        n20 = MathTex("20", font_size=FS - 4, color=RED).next_to(br_r, DOWN, buff=0.16)
        n100 = MathTex("100", font_size=FS - 4, color=BLUE).next_to(br_b, DOWN, buff=0.16)
        with self.narrate("Your chance of being sick is the red share of this crowd. [pause 0.3] "
                          "Twenty, out of twenty plus a hundred. [pause 1.1]") as beat:
            beat.wait_until("chance", offset=-0.1)
            # the meter's title becomes the left-hand side: it pulses while P(sick | +) arrives
            self.play(emph(meter.title, scale=1.08), FadeIn(lhs1, shift=0.15 * DOWN),
                      FadeIn(eq1), FadeOut(strip_lbl, shift=0.1 * DOWN), run_time=1.2)
            beat.wait_until("red share", offset=-0.1)
            self.play(GrowFromCenter(br_r), FadeIn(n20, shift=0.1 * DOWN),
                      LaggedStart(*[emph(d, scale=1.4) for d in red_dots], lag_ratio=0.04),
                      run_time=0.9)
            beat.wait_until("crowd", offset=-0.2)
            self.play(GrowFromCenter(br_b), FadeIn(n100, shift=0.1 * DOWN), run_time=0.8)
            beat.wait_until("Twenty", offset=-0.15)
            self.fly([Flight(n20, num1, lift=-0.3)], run_time=beat.until("out of", offset=-0.05))
            self.play(Create(bar1), run_time=0.4)
            # "20 +" is written with its final spacing; the 20 passes under the left-hand side
            # and rises into its slot from below
            d0 = den1[0].get_center()
            lb = lhs1.get_bottom()[1]
            self.fly([Flight(n20, den1[0], lift=-0.3,
                             via=[(lhs1.get_left()[0] - 0.75, lb + 0.2, 0),
                                  (lhs1.get_x(), lb - 0.65, 0), (d0[0], lb - 0.75, 0)])],
                     FadeIn(den1[1]), run_time=beat.until("hundred", offset=-0.1))
            # the 100 comes round the right-hand side and slides in from the right: it never
            # crosses the "+", the bar or the numerator
            d2 = den1[2].get_center()
            bar_r = bar1.get_right()[0]
            self.fly([Flight(n100, den1[2], lift=-0.3,
                             via=[(num1.get_x() - 0.6, -0.45, 0), (bar_r + 0.7, -0.85, 0),
                                  (bar_r + 0.75, d2[1], 0)])], run_time=1.0)
            # the 17 % comes from the meter in silence: down the left edge (clear of the strip),
            # across the open band above the fraction, and down onto its place
            v0 = meter.value.get_center()
            t1 = tail1[1].get_center()
            self.fly([Flight(meter.value, tail1[1], lift=0.0,
                             via=[(v0[0], -0.05, 0), (v0[0] + 1.7, -0.55, 0),
                                  (t1[0] - 1.2, -0.55, 0), (t1[0], -0.95, 0)])],
                     FadeIn(tail1[0], rate_func=late), run_time=1.3)

        # stage 2: each head count = people x rate (exact: 19.8 / 119.6), one term per sentence,
        # >= 5 s apart.  The table's rounded results turn exact (19.8, 99.8) as their terms expand.
        for m in (cnt_s, cnt_h, res_s, res_h):
            m.clear_updaters()
        S2a = build_stage("2a")
        S2 = build_stage("2")
        exact_s = MathTex("19.8", font_size=MATH - 4).move_to(res_s, aligned_edge=LEFT)
        exact_h = MathTex("99.8", font_size=MATH - 4).move_to(res_h, aligned_edge=LEFT)

        def move_eq(live, new, rate_func=smooth):
            """The on-screen lhs / = / bar / tail carried onto stage `new`'s layout."""
            l0, e0, b0, t0 = live
            l1, e1, _, b1, _, t1 = new
            anims = [l0.animate(rate_func=rate_func).move_to(l1),
                     e0.animate(rate_func=rate_func).move_to(e1),
                     Transform(b0, b1, rate_func=rate_func)]
            if t0 is not None and t1 is not None:
                anims.append(t0.animate(rate_func=rate_func).move_to(t1))
            return anims
        live = (lhs1, eq1, bar1, tail1)
        row_gap = (lab_s.get_bottom()[1] + lab_h.get_top()[1]) / 2
        x_gap = (outline.get_right()[0] + dot_s.get_left()[0]) / 2
        with self.narrate("Unrounded, the red count is twenty sick people times ninety-nine "
                          "percent. [pause 0.6] The blue count is nine thousand nine hundred "
                          "eighty healthy people times one percent.") as beat:
            beat.wait_until("red count", offset=-0.15)
            self.play(emph(num1, scale=1.12), emph(den1[0], scale=1.12), emph(res_s, scale=1.25),
                      run_time=0.8)
            # 20 positives = 20 sick people (table, people column) x 99 % (the red arrow), in ONE
            # move: the layout opens first, the old 20s leave, the 20 and the 0.99 fly out of the
            # table along the gap between its rows and down the gap beside the strip, the
            # denominator repeats the new numerator term in place, and the table's rounded 20
            # positives become the exact 19.8
            beat.wait_until("twenty sick", offset=-0.3)
            n0, n2 = S2a[2][0].get_center(), S2a[2][2].get_center()
            f20 = Flight(cnt_s, S2a[2][0], lift=-(cnt_s.get_y() - row_gap) + 0.12,
                         via=[(cnt_s.get_x() - 0.6, row_gap, 0), (x_gap + 0.15, row_gap, 0),
                              (x_gap, row_gap - 0.6, 0), (x_gap, 0.2, 0), (n0[0], -0.45, 0)],
                         rate_func=window(0.0, 0.5))
            arrow_gap = (arr_s.get_bottom()[1] + rate_h.get_top()[1]) / 2
            f99 = Flight(arr_s, S2a[2][2], lift=-(arr_s.get_y() - arrow_gap),
                         k0=0.75 * rate_s.height / S2a[2][2].height,
                         via=[(arr_s.get_x() - 0.9, row_gap, 0), (x_gap + 0.15, row_gap, 0),
                              (x_gap, row_gap - 0.6, 0), (x_gap, 0.2, 0), (n2[0], -0.3, 0)],
                         rate_func=window(0.35, 1.0))
            first = window(0.0, 0.3)
            self.fly([f20, f99],
                     *move_eq(live, S2a, first),
                     FadeOut(num1, shift=0.14 * UP, rate_func=window(0.2, 0.38)),
                     *swap_den(den1[0], VGroup(*S2a[4][:3]), t_out=(0.3, 0.5), t_in=(0.42, 0.8)),
                     den1[1].animate(rate_func=first).move_to(S2a[4][3]),
                     den1[2].animate(rate_func=first).move_to(S2a[4][4]),
                     FadeIn(S2a[2][1], rate_func=window(0.45, 0.65)),
                     *swap(res_s, exact_s, t_out=(0.55, 0.75), t_in=(0.7, 1.0)),
                     run_time=beat.until("percent", offset=0.15))

            # 100 positives = 9,980 healthy people x 1 %: the 9,980 drops out of the table, comes
            # down beside the fraction and rises into its slot; then x 0.01 arrives from the arrow
            beat.wait_until("blue count", offset=-0.15)
            self.play(emph(den1[2], scale=1.12), emph(res_h, scale=1.25), run_time=0.8)
            beat.wait_until("nine thousand", offset=-0.25)
            d4, d6 = S2[4][4].get_center(), S2[4][6].get_center()
            # round the right of the tail and under the denominator, then up into its slot:
            # it never crosses the bar, the tail or another glyph
            f998 = Flight(cnt_h, S2[4][4], lift=-0.35,
                          via=[(cnt_h.get_x() + 0.4, 0.55, 0), (5.45, 0.1, 0), (5.45, -2.45, 0),
                               (d4[0] + 0.3, -2.45, 0)],
                          rate_func=window(0.0, 0.55))
            tail_r = S2[5].get_right()[0]          # where the tail sits once the layout opens
            f01 = Flight(arr_h, S2[4][6], lift=-0.35, k0=0.75 * rate_h.height / S2[4][6].height,
                         via=[(tail_r + 0.75, -0.5, 0), (tail_r + 0.65, d6[1] - 0.6, 0),
                              (d6[0] + 0.7, d6[1] - 0.55, 0)], rate_func=window(0.55, 1.0))
            self.fly([f998, f01],
                     *move_eq(live, S2, first),
                     *[m.animate(rate_func=first).move_to(t) for m, t in zip(S2a[2], S2[2])],
                     *[S2a[4][i].animate(rate_func=first).move_to(S2[4][i]) for i in (0, 1, 2)],
                     den1[1].animate(rate_func=first).move_to(S2[4][3]),
                     FadeOut(den1[2], shift=0.14 * DOWN, rate_func=window(0.0, 0.25)),
                     FadeIn(S2[4][5], rate_func=window(0.72, 0.9)),
                     *swap(res_h, exact_h, t_out=(0.55, 0.75), t_in=(0.7, 1.0)),
                     run_time=beat.until("one percent", offset=0.35))
        res_s, res_h = exact_s, exact_h
        # bookkeeping: the live stage-2 parts on screen
        lhs, eq, bar, tail = lhs1, eq1, bar1, tail1
        num2 = VGroup(*S2a[2])
        den2 = VGroup(S2a[4][0], S2a[4][1], S2a[4][2], den1[1], S2[4][4], S2[4][5], S2[4][6])

        # stage 3: the head counts divided by 10,000 -> shares of everyone.  Its own picture
        # first: the table's people column divides, in place; only then do the shares fly in.
        S3 = build_stage("3")
        lhs3, eq3, num3, bar3, den3, tail3 = S3
        div_tag = MathTex(r"\div\,10{,}000", font_size=34, color=INK)
        div_tag.move_to([X_COUNT_R - div_tag.width / 2, HEADER_Y, 0])
        sh_s = MathTex("0.002", font_size=MATH - 4, color=INK)
        sh_s.move_to([X_COUNT_R - sh_s.width / 2, ROW_Y["sick"], 0])
        sh_h = MathTex("0.998", font_size=MATH - 4, color=INK)
        sh_h.move_to([X_COUNT_R - sh_h.width / 2, ROW_Y["healthy"], 0])
        context = VGroup(arr_s, arr_h, rate_s, rate_h, res_s, res_h, head_plus)
        with self.narrate("Divide top and bottom by the ten thousand we started with. [pause 0.2] "
                          "Twenty people become two in a thousand, and nine thousand nine hundred "
                          "eighty become nine hundred ninety-eight in a thousand. [pause 0.2] The "
                          "share can't change.") as beat:
            beat.wait_until("Divide", offset=-0.1)
            self.play(*swap(head_people, div_tag, shift=0.12 * UP), dim(context), run_time=0.9)
            beat.wait_until("ten thousand", offset=-0.15)
            self.play(emph(div_tag, scale=1.15), emph(cnt_s, scale=1.15), emph(cnt_h, scale=1.15),
                      run_time=0.8)
            beat.wait_until("two in a thousand", offset=-0.45)
            self.play(*swap(cnt_s, sh_s), run_time=0.9)
            beat.wait_until("nine hundred ninety-eight", offset=-0.45)
            self.play(*swap(cnt_h, sh_h), run_time=0.9)
            # "The share can't change": the shares fly into the formula (one change) and the
            # 17 % stays where it was
            beat.wait_until("share", offset=-1.0)
            # 1) the layout opens: every glyph moves to its new place, the old head counts to
            #    the middle of their (wider) slots - no hole, nothing overprinted
            self.play(*move_eq((lhs, eq, bar, tail), S3),
                      num2[0].animate.move_to(num3[0]), den2[0].animate.move_to(den3[0]),
                      den2[4].animate.shift([den3[4].get_x() - den2[4].get_x(), 0, 0]),
                      *[ReplacementTransform(num2[i], num3[i]) for i in (1, 2)],
                      *[ReplacementTransform(den2[i], den3[i]) for i in (1, 2, 3, 5, 6)],
                      run_time=0.45)
            # 2) the shares fly in from the table's people column: 0.002 through the gap
            #    between the rows and down beside the strip (small while it passes), 0.998 round
            #    the right of the tail and up into its slot; each old count leaves as its share
            #    arrives
            n0 = num3[0].get_center()
            fa = Flight(sh_s, num3[0], lift=-(sh_s.get_y() - row_gap) + 0.12, k0=0.5,
                        via=[(sh_s.get_x() - 0.7, row_gap, 0), (x_gap + 0.1, row_gap, 0),
                             (x_gap, row_gap - 0.5, 0), (x_gap, 0.0, 0), (n0[0], -0.62, 0)])
            d4 = den3[4].get_center()
            fc = Flight(sh_h, den3[4], lift=-0.35,
                        via=[(sh_h.get_x() + 0.4, 0.55, 0), (5.75, 0.1, 0), (5.75, -2.45, 0),
                             (d4[0] + 0.3, -2.45, 0)])
            self.fly([fa, fc],
                     FadeOut(num2[0], shift=0.14 * UP, rate_func=window(0.55, 0.75)),
                     *swap_den(den2[0], den3[0], t_out=(0.6, 0.85), t_in=(0.75, 1.0)),
                     FadeOut(den2[4], rate_func=window(0.5, 0.7)),
                     run_time=1.4)
            self.play(emph(tail, scale=1.15), run_time=0.7)

        # stage 4: name the numbers, in ONE change -> Bayes' theorem
        lhs4, eq4, num4, bar4, den4, _ = build_stage("4")

        def term_box(m, col):
            r = RoundedRectangle(corner_radius=0.06, width=m.width + 0.36, height=m.height + 0.24,
                                 stroke_color=col, stroke_width=3, fill_opacity=0).move_to(m)
            return ss_style._decorates(r, m)
        den_box = term_box(den4, YELLOW)
        num_box = term_box(num4, RED)
        bayes_lbl = label("Bayes' theorem", size=LABEL, color=GRAY)
        bayes_lbl.next_to(lhs4, DOWN, buff=0.55, aligned_edge=LEFT)
        bayes_lbl.shift(DOWN * max(0.0, bayes_lbl.get_top()[1] - (den_box.get_bottom()[1] - 0.22)))
        priors = VGroup(num3[0], den3[0], den3[4])
        rates = VGroup(num3[2], den3[2], den3[6])
        with self.narrate("These are how common each group is, and these, how often each group "
                          "tests positive: Bayes' theorem.") as beat:
            self.play(*[emph(m, scale=1.12) for m in priors], emph(sh_s, scale=1.15),
                      emph(sh_h, scale=1.15), run_time=0.7)
            beat.wait_until("these", occurrence=2, offset=-0.1)
            self.play(*[emph(m, scale=1.12) for m in rates],
                      *[m.animate(rate_func=there_and_back).set_opacity(1.0)
                        for m in (arr_s, arr_h, rate_s, rate_h)], run_time=0.7)
            beat.wait_until("Bayes", offset=-0.95)
            self.play(ReplacementTransform(lhs, lhs4), ReplacementTransform(eq, eq4),
                      ReplacementTransform(bar, bar4), FadeOut(tail, rate_func=out_first),
                      *swap_num(num3[0], num4[0]), FadeOut(num3[1], rate_func=out_first),
                      *swap_num(num3[2], num4[1]),
                      *swap_den(den3[0], den4[0]), FadeOut(den3[1], rate_func=out_first),
                      *swap_den(den3[2], den4[1]), ReplacementTransform(den3[3], den4[2]),
                      *swap_den(den3[4], den4[3]), FadeOut(den3[5], rate_func=out_first),
                      *swap_den(den3[6], den4[4]), run_time=1.2)
            self.play(FadeIn(bayes_lbl, shift=0.1 * UP), run_time=0.6)

        with self.narrate("All it does is shrink the sample space to what the evidence allows, "
                          "then take the share. [pause 0.8]") as beat:
            beat.wait_until("shrink", offset=-0.1)
            self.play(Create(den_box), run_time=1.0)
            beat.wait_until("take the share", offset=-0.1)
            self.play(Create(num_box), LaggedStart(*[emph(d, scale=1.4) for d in red_dots],
                                                   lag_ratio=0.04), run_time=1.1)
            # the pause after the thesis: the shrunk sample space itself pulses once
            self.hold(beat.until_end_of("share", offset=0.1))
            self.play(emph(outline, scale=1.04), run_time=0.8)

        # ============================================================ 7. Cardiff 2017: precision
        formula_grp = VGroup(lhs4, eq4, num4, bar4, den4, bayes_lbl, den_box, num_box)
        table = VGroup(dot_s, dot_h, lab_s, lab_h, arr_s, arr_h, rate_s, rate_h, head_plus,
                       sh_s, sh_h, res_s, res_h, div_tag)
        K = K_CARDIFF
        cb = CARDIFF_BAR
        meter.value.resume_updating()
        title_alert = label("chance an alert is right", size=LABEL)
        title_alert.move_to(meter.title_at(METER_STRIP, STRIP_TITLE_BUFF, title=title_alert))
        alert_title_at = meter.title_at(cb, STRIP_TITLE_BUFF, K, title=title_alert)
        crowd = Crowd()
        crowd_lbl = label("≈ 170,000 people", size=26)
        crowd_lbl.next_to(crowd.image, UP, buff=0.2)
        # legend, bottom-right of the crowd: what one square is, and what red means
        leg_scale = VGroup(swatch(BLUE, 0.15, Crowd.BASE),
                           label("= 17 people · illustration", size=22, color=GRAY))
        leg_scale.arrange(RIGHT, buff=0.15)
        leg_list = VGroup(swatch(RED, 0.15), label("watch-listed: ≤ 1,200", size=26, color=RED))
        leg_list.arrange(RIGHT, buff=0.15)
        legend = VGroup(leg_list, leg_scale).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        legend.next_to(crowd.image, RIGHT, buff=0.3, aligned_edge=DOWN)
        cite_bbc = citation("South Wales Police figures, 2018 · BBC News")
        cite_dav = citation("Davies et al., 2018 · Cardiff University")
        cite_dav.next_to(cite_bbc, UP, buff=0.18, aligned_edge=LEFT)
        with self.narrate("Swap the disease for a police watch list.") as beat:
            # 1) the patients' picture clears while the meter empties and is retitled in place;
            # 2) the meter makes ONE move to the top right while the crowd fades in at its
            #    final place, so the new population is there on "police watch list"
            self.add(crowd.image)
            self.play(*[FadeOut(m, rate_func=early) for m in
                        (formula_grp, table, survivors, outline, VGroup(br_r, br_b, n20, n100))],
                      meter.fill.animate.set_value(0.0),
                      FadeOut(meter.value, rate_func=early), FadeIn(meter.qmark, rate_func=late),
                      *swap(meter.title, title_alert, shift=0.12 * UP), run_time=0.8)
            # the crowd fades in as soon as the meter has cleared its top edge
            self.play(meter.track.animate(rate_func=SMOOTH).scale(K).move_to(cb),
                      title_alert.animate(rate_func=SMOOTH).move_to(alert_title_at),
                      crowd.opacity.animate(rate_func=window(0.5, 1.0)).set_value(1.0),
                      run_time=1.1)

        with self.narrate("At the twenty seventeen Champions League final, about a hundred and "
                          "seventy thousand people were in Cardiff. [pause 0.2] The watch lists "
                          "held about twelve hundred faces, so even a small error rate per face "
                          "would swamp the real matches.") as beat:
            beat.wait_until("twenty", offset=-0.15)
            self.play(FadeIn(cite_bbc, shift=0.1 * UP), run_time=0.8)
            beat.wait_until("hundred and seventy", offset=-0.3)
            self.play(FadeIn(crowd_lbl, shift=0.1 * DOWN), run_time=0.9)
            beat.wait_until("Cardiff", offset=-0.2)
            self.play(FadeIn(leg_scale, shift=0.1 * LEFT), run_time=0.8)
            beat.wait_until("twelve hundred", offset=-0.3)
            # the base rate, drawn: at most 71 of the 10,000 squares hold a listed face
            self.play(LaggedStart(*[FadeIn(s, scale=4.0) for s in crowd.red_sq], lag_ratio=0.03),
                      FadeIn(leg_list, shift=0.1 * LEFT), FadeIn(cite_dav, shift=0.1 * UP),
                      run_time=1.6)
            # "per face": every one of the 10,000 squares is a chance for a false alarm
            beat.wait_until("error rate", offset=-0.1)
            self.play(crowd.opacity.animate(rate_func=there_and_back).set_value(1.25),
                      run_time=1.0)
            beat.wait_until("swamp", offset=-0.1)
            self.play(LaggedStart(*[emph(s, scale=2.2, run_time=0.8) for s in crowd.red_sq],
                                  lag_ratio=0.008), run_time=1.3)

        # the alerts: flagged squares collapse into a 26 x 95 raster (2,470 cells) under the meter
        al_h = AL_ROWS * AL_CELL * PX
        al_c = np.array([cb[0], snap(cb[1] - K * METER_H / 2 - 0.3 - al_h / 2), 0])
        alerts_col = ImageMobject(alert_raster())
        alerts_col.height = al_h
        alerts_col.move_to(al_c)
        alerts_col.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"
                                                                  if config.pixel_height >= 1080
                                                                  else "bilinear"])
        al_out = SurroundingRectangle(alerts_col, color=YELLOW, buff=0.1, corner_radius=0.08,
                                      stroke_width=3)
        al_left, al_w = alerts_col.get_left()[0], alerts_col.width
        al_top = alerts_col.get_top()[1]
        bw, bh = al_w / BLK_COLS, al_h / BLK_ROWS
        # the 10 red flagged squares become the first 10 blocks (the raster's red columns);
        # every block keeps its yellow ring (it tested positive) until it lands
        order = [i for i in crowd.lit_idx if i in crowd.lit_red] + \
                [i for i in crowd.lit_idx if i not in crowd.lit_red]
        block_of = {i: k for k, i in enumerate(order)}
        blocks = []
        for i in crowd.lit_idx:
            c, r = divmod(block_of[i], BLK_ROWS)
            col = RED if i in crowd.lit_red else BLUE
            p = [al_left + (c + 0.5) * bw, al_top - (r + 0.5) * bh, 0]
            blk = Rectangle(width=bw * 0.7, height=bh * 0.7, fill_color=col, fill_opacity=0.95,
                            stroke_width=0).move_to(p)
            ring = Rectangle(width=bw * 0.86, height=bh * 0.86, stroke_color=YELLOW,
                             stroke_width=1.6, stroke_opacity=1, fill_opacity=0).move_to(p)
            blocks.append(VGroup(blk, ring))
        c_beam = Line([0, crowd.top + 0.08, 0], [0, crowd.top - CROWD_G - 0.02, 0], color=YELLOW,
                      stroke_width=4)
        c_beam.add_updater(lambda m: m.move_to([crowd.left + CROWD_G * crowd.sweep.get_value(),
                                                CROWD_C[1], 0]))
        al_lbl = label("2,470 alerts")
        al_lbl.next_to(al_out, DOWN, buff=0.3).set_x(cb[0])
        unflagged_red = VGroup(*[s for i, s in zip(crowd.red_idx, crowd.red_sq)
                                 if int(i) not in crowd.lit_red])
        with self.narrate("Face-recognition cameras scanned the crowd. [pause 0.3] They raised two "
                          "thousand four hundred and seventy alerts.", gap=0.4) as beat:
            crowd.start_overlays()
            self.add(*[c for i, c in zip(crowd.lit_idx, crowd.cores) if i not in crowd.lit_red],
                     crowd.rings, c_beam)
            self.play(FadeIn(c_beam), run_time=0.3)
            self.play(crowd.sweep.animate.set_value(1.0),
                      run_time=beat.until("crowd", end=True, offset=-0.25), rate_func=LINEAR)
            self.play(FadeOut(c_beam), run_time=0.3)
            for m in list(crowd.cores) + list(crowd.rings) + list(unflagged_red):
                m.clear_updaters()
            flagged = [VGroup(c, r) for c, r in zip(crowd.cores, crowd.rings)]
            red_flagged = [f for i, f in zip(crowd.lit_idx, flagged) if i in crowd.lit_red]
            # the beam is done; a beat later the 10 flagged watch-listed squares pulse (in red,
            # rings on): the red share of the lit crowd is seen in the crowd, before it flies
            beat.wait_until("They", offset=-0.05)
            self.play(LaggedStart(*[emph(f, scale=2.2, run_time=0.7) for f in red_flagged],
                                  lag_ratio=0.04), run_time=0.9)
            # each flagged square becomes one ~17-alert block of the raster, keeping its colour
            # and its ring; the legend steps aside first, so no flying square crosses its text
            self.play(FadeOut(leg_list, rate_func=window(0.0, 0.2)),
                      FadeOut(leg_scale, rate_func=window(0.0, 0.2)),
                      LaggedStart(*[Transform(f, b) for f, b in zip(flagged, blocks)],
                                  lag_ratio=0.004),
                      run_time=beat.until("alerts", offset=-0.1))
            self.add(alerts_col, *flagged)
            self.play(FadeIn(alerts_col), *[FadeOut(f) for f in flagged], Create(al_out),
                      FadeIn(al_lbl, shift=0.1 * UP), run_time=0.8)

        # "shrink to the alerts": the crowd leaves and the alerts + meter take the centre
        shift_v = np.array([-cb[0], snap(-0.75), 0])
        cb2 = cb + shift_v
        ob2 = al_out.get_bottom()[1] + shift_v[1]
        al_left2 = al_left + shift_v[0]
        xr = al_left2 + al_w * ALERTS_RIGHT / ALERTS
        br_r2 = Brace(Line([al_left2, ob2, 0], [xr, ob2, 0]), DOWN, buff=0.08, color=RED)
        br_b2 = Brace(Line([xr + 0.04, ob2, 0], [al_left2 + al_w, ob2, 0]), DOWN, buff=0.08,
                      color=BLUE)
        right_lbl = label("173 right", color=RED)
        right_lbl.next_to(br_r2, DOWN, buff=0.18)
        right_lbl.set_x(max(right_lbl.get_x(), br_r2.get_x()))
        wrong_lbl = label("2,297 wrong", color=BLUE)
        wrong_lbl.next_to(br_b2, DOWN, buff=0.18)
        with self.narrate("Shrink to the alerts, and take the red share. Police counted a hundred "
                          "and seventy-three as right: seven percent.") as beat:
            self.play(FadeOut(crowd.image), FadeOut(unflagged_red), FadeOut(crowd_lbl),
                      run_time=0.6)
            self.remove(crowd.image)
            crowd.image.clear_updaters()
            self.play(Group(meter.track, title_alert, alerts_col, al_out, al_lbl)
                      .animate(rate_func=SMOOTH).shift(shift_v), run_time=1.0)
            beat.wait_until("red share", offset=-0.15)
            self.play(GrowFromCenter(br_r2), GrowFromCenter(br_b2),
                      FadeOut(al_lbl, rate_func=early), run_time=0.8)
            beat.wait_until("hundred and seventy-three", offset=-0.2)
            meter.share.set_value(ALERTS_RIGHT / ALERTS)
            meter.value.update()
            self.play(FadeIn(right_lbl, shift=0.1 * DOWN), FadeIn(wrong_lbl, shift=0.1 * DOWN),
                      run_time=0.9)
            beat.wait_until("seven percent", offset=-0.3)
            self.play(meter.fill.animate.set_value(1.0), FadeOut(meter.qmark, rate_func=early),
                      FadeIn(meter.value, rate_func=late), run_time=1.1)

        title_prec = label("precision", size=LABEL)
        title_prec.move_to(meter.title_at(cb2, STRIP_TITLE_BUFF, K, title=title_prec))
        with self.narrate("In machine learning, the share of alerts that are right is called "
                          "precision.") as beat:
            beat.wait_until("share", offset=-0.15)
            self.play(emph(VGroup(br_r2, right_lbl), scale=1.15), emph(meter.value, scale=1.2),
                      run_time=0.9)
            beat.wait_until("precision", offset=-0.25)
            self.play(*swap(title_alert, title_prec, shift=0.12 * UP),
                      emph(meter.value, scale=1.25), run_time=1.0)

        # an honest limit, like-for-like: the evaluators' own count at this final (3 %) and at
        # the Six Nations (46 %), where fewer false alarms per face lifted precision
        tr = meter.track
        bar_top = tr.get_top()[1]

        def eval_marker(frac_, text_, side=RIGHT):
            x = meter.x_at(frac_)
            mk = DashedLine([x, tr.get_bottom()[1] - 0.12, 0], [x, bar_top + 0.14, 0],
                            color=INK, stroke_width=4, dash_length=0.05)
            lb = label(text_, size=24, color=GRAY)
            lb.move_to([x + side[0] * (0.15 + lb.width / 2), bar_top + 0.2 + lb.height / 2, 0])
            return mk, lb
        mk03, lb03 = eval_marker(EVALUATORS_CL, "evaluators: 3%", side=LEFT)
        mk46, lb46 = eval_marker(SIX_NATIONS, "Six Nations 2018: 46%")
        lift = max(0.0, max(lb03.get_top()[1], lb46.get_top()[1]) + 0.18
                   - title_prec.get_bottom()[1])
        with self.narrate("The university's evaluators counted three percent here. After a new "
                          "algorithm and better photos cut the false alarms, they counted "
                          "forty-six at the Six Nations.") as beat:
            self.play(title_prec.animate.shift(lift * UP), run_time=0.6)
            beat.wait_until("three percent", offset=-0.2)
            self.play(Create(mk03), FadeIn(lb03, shift=0.1 * LEFT), run_time=0.8)
            beat.wait_until("false alarms", offset=-0.15)
            self.play(emph(VGroup(br_b2, wrong_lbl), scale=1.1), run_time=0.9)
            beat.wait_until("forty-six", offset=-0.2)
            self.play(Create(mk46), FadeIn(lb46, shift=0.1 * RIGHT), run_time=0.9)

        # ============================================================ 8. landing
        L2 = self.build_diagram(dy=LAND_DY, rate_at=0.28)
        red_c, blue_c, plus_c = L2["centers"]
        disk, cross = L2["plus"][0], L2["plus"][1]
        ring_tmp = Circle(radius=disk.width / 2, stroke_color=YELLOW, stroke_width=3,
                          fill_opacity=0).move_to(plus_c)
        title_land = label("chance you're sick", size=LABEL)
        title_land.move_to(meter.title_at(cb2, STRIP_TITLE_BUFF, K, title=title_land)
                           + lift * UP)
        title_land_at = meter.title_at(METER_LAND, title=title_land)

        def acc_bar(y, frac_, text_, tex):
            track = Rectangle(width=METER_W, height=0.22, stroke_color=GRAY, stroke_width=2,
                              fill_opacity=0).move_to([METER_LAND[0], y, 0])
            fill_ = Rectangle(width=METER_W * frac_, height=0.22, fill_color=GRAY,
                              fill_opacity=0.6, stroke_width=0)
            fill_.move_to(track.get_left() + RIGHT * METER_W * frac_ / 2)
            lbl_ = label(text_, size=26, color=GRAY).next_to(track, UP, buff=0.15)
            lbl_.align_to(track, LEFT)
            val = MathTex(tex, font_size=36, color=GRAY).next_to(track, LEFT, buff=0.22)
            return track, fill_, lbl_, val
        acc1 = acc_bar(-1.7, 0.99, "accuracy", r"99\%")
        acc2 = acc_bar(-2.6, 0.998, "calls everyone healthy", r"99.8\%")
        # the useless test: nobody tests positive, so both flows carry 0 %
        r99_keep, r1_keep = L2["r99"].copy(), L2["r1"].copy()
        z99 = MathTex(r"0\%", font_size=MATH).move_to(L2["r99"])
        z1 = MathTex(r"0\%", font_size=MATH).move_to(L2["r1"])
        with self.narrate("Back to your test. [pause 0.9] The title's ninety-nine percent accuracy "
                          "is real. But a test that calls everyone healthy scores ninety-nine point "
                          "eight: more accurate, and useless.") as beat:
            # everyone the camera flagged collapses into the + they stand for: the raster's
            # outline becomes the badge's disk (two closed shapes), the raster shrinks into it,
            # and the cross appears only once the disk has landed.  Meanwhile the meter empties
            # and is retitled in place (never untitled)
            self.play(*[FadeOut(m, rate_func=early) for m in (br_r2, br_b2, right_lbl, wrong_lbl,
                                                              cite_bbc, cite_dav, mk03, lb03,
                                                              mk46, lb46)],
                      FadeOut(alerts_col, target_position=plus_c, scale=0.05),
                      ReplacementTransform(al_out, ring_tmp),
                      meter.fill.animate.set_value(0.0), FadeOut(meter.value, rate_func=early),
                      *swap(title_prec, title_land, shift=0.12 * UP), run_time=1.0)
            self.play(ReplacementTransform(ring_tmp, disk),
                      FadeIn(cross, scale=0.6, rate_func=late), run_time=0.5)
            meter.share.set_value(ppv(PREV_N))
            meter.value.update()
            self.play(meter.track.animate.scale(1 / K).move_to(METER_LAND),
                      title_land.animate.move_to(title_land_at),
                      FadeIn(L2["red"], scale=0.5), FadeIn(L2["blue"], scale=0.5),
                      FadeIn(L2["sick"]), FadeIn(L2["healthy"]), FadeIn(L2["prev"]),
                      GrowArrow(L2["ra"]), GrowArrow(L2["ba"]),
                      Create(L2["ring"]), FadeIn(L2["you"], shift=0.1 * UP), run_time=0.9)
            self.play(meter.fill.animate.set_value(1.0), FadeIn(meter.value, rate_func=late),
                      FadeIn(L2["r99"], shift=0.08 * UP), FadeIn(L2["r1"], shift=0.08 * UP),
                      run_time=0.8)
            # accuracy, the naive score (grey): the real test, then one that never says "sick"
            beat.wait_until("accuracy", offset=-0.25)
            self.play(Create(acc1[0]), FadeIn(acc1[2], shift=0.08 * UP), run_time=0.6)
            self.play(GrowFromEdge(acc1[1], LEFT), FadeIn(acc1[3], rate_func=late),
                      run_time=beat.until("real", offset=0.25, min_time=0.6))
            beat.wait_until("calls", offset=-0.15)
            # it never says "sick", so nothing reaches the +: both flows drain to 0 %
            self.play(Create(acc2[0]), FadeIn(acc2[2], shift=0.08 * UP),
                      L2["ra"].animate.set_opacity(0.12), L2["ba"].animate.set_opacity(0.12),
                      L2["plus"].animate.set_opacity(0.3),
                      *swap(L2["r99"], z99), *swap(L2["r1"], z1), run_time=0.9)
            beat.wait_until("ninety-nine", occurrence=2, offset=-0.1)
            self.play(GrowFromEdge(acc2[1], LEFT), FadeIn(acc2[3], rate_func=late),
                      run_time=beat.until("eight", offset=0.25))
            beat.wait_until("more accurate", offset=-0.1)
            self.play(emph(acc2[3], scale=1.2), emph(acc1[3], scale=1.2), run_time=0.7)
            beat.wait_until("useless", offset=-0.1)
            self.play(emph(z99, scale=1.3), emph(L2["red"], scale=1.2), run_time=0.7)
        L2["r99"], L2["r1"] = r99_keep, r1_keep

        # prior sweep: ONE driver updates the meter from the same rounded prevalence the label
        # shows, before anything that reads it is redrawn (no frame of lag)
        u = ValueTracker(0.0)
        W = 0.45                                    # total flow width = everyone who reaches +

        def n_now() -> int:
            return max(2, int(round(n_of(u.get_value()))))

        def band(a, b, width, col):
            v = (b - a) / np.linalg.norm(b - a)
            nrm = np.array([-v[1], v[0], 0]) * max(width, 0.004) / 2
            s, e = a + 0.3 * v, b - 0.66 * v
            return Polygon(s + nrm, e + nrm, e - nrm, s - nrm, fill_color=col, fill_opacity=0.95,
                           stroke_width=0)
        red_band0 = band(red_c, plus_c, W * ppv(PREV_N), RED)
        blue_band0 = band(blue_c, plus_c, W * (1 - ppv(PREV_N)), BLUE)
        red_band = always_redraw(lambda: band(red_c, plus_c, W * ppv(n_now()), RED))
        blue_band = always_redraw(lambda: band(blue_c, plus_c, W * (1 - ppv(n_now())), BLUE))
        driver = Mobject()
        driver.add_updater(lambda m: meter.share.set_value(ppv(n_now())))
        prev = L2["prev"]
        num = DecimalNumber(PREV_N, num_decimal_places=0, group_with_commas=True, font_size=44)
        n_left, n_base = prev[2].get_left()[0], prev[2][0].get_bottom()[1]

        def upd_num(m):
            m.set_value(n_now())
            m.shift([n_left - m.get_left()[0], n_base - m[0].get_bottom()[1], 0])
        num.add_updater(upd_num)
        num.update()
        naive_x2 = meter.x_at(0.99)
        marker2 = DashedLine([naive_x2, METER_LAND[1] - METER_H / 2 - 0.14, 0],
                             [naive_x2, METER_LAND[1] + METER_H / 2 + 0.14, 0],
                             color=GRAY, stroke_width=3, dash_length=0.06)
        naive2 = naive_lbl.copy()
        naive2.next_to(marker2, UP, buff=0.1).align_to(meter.track, RIGHT)

        # head counts sit OUTSIDE the flows, beside the band that carries them
        def beside(m, a, b, width, side, f=0.6, gap=0.2):
            v = (b - a) / np.linalg.norm(b - a)
            nrm = np.array([-v[1], v[0], 0]) * side
            p = a + f * (b - a)
            ext = 0.5 * (abs(nrm[0]) * m.width + abs(nrm[1]) * m.height)
            return m.move_to(p + nrm * (width / 2 + gap + ext))
        cnt20 = beside(MathTex("20", font_size=FS, color=RED), red_c, plus_c,
                       W * ppv(PREV_N), +1)
        cnt100 = beside(MathTex("100", font_size=FS, color=BLUE), blue_c, plus_c,
                        W * (1 - ppv(PREV_N)), -1)
        with self.narrate("Your seventeen percent assumes a random screen. [pause 0.3] Symptoms "
                          "raise the one in five hundred, and the answer climbs: at one in a "
                          "hundred, fifty percent; at one in two, ninety-nine, where the rule held. "
                          "[pause 1.2]") as beat:
            # your test again: the flows refill, the rates return, the accuracy bars leave
            self.play(emph(meter.value, scale=1.25),
                      L2["ra"].animate.set_opacity(1.0), L2["ba"].animate.set_opacity(1.0),
                      L2["plus"].animate.set_opacity(1.0),
                      *swap(z99, L2["r99"]), *swap(z1, L2["r1"]),
                      *[FadeOut(m, shift=0.1 * DOWN) for grp in (acc1, acc2) for m in grp],
                      run_time=0.9)
            beat.wait_until("random", offset=-0.2)
            self.play(emph(prev, scale=1.2), run_time=0.9)
            beat.wait_until("Symptoms", offset=-0.1)
            self.play(ReplacementTransform(L2["ra"], red_band0),
                      ReplacementTransform(L2["ba"], blue_band0),
                      FadeIn(marker2), FadeIn(naive2), run_time=1.0)
            self.remove(red_band0, blue_band0, meter.red, meter.blue, meter.track, meter.value,
                        prev[2])
            # update order: driver -> meter segments / value -> flows -> label
            self.add(driver, meter.red, meter.blue, meter.track, meter.value, red_band, blue_band,
                     num)
            self.bring_to_front(L2["red"], L2["blue"], L2["plus"], L2["ring"])
            # every spoken number gets its own frame: the label reaches 1 in 100 as it is said,
            # holds through "fifty percent", then 1 in 2 lands on "ninety-nine"
            beat.wait_until("climbs", offset=-0.2)
            self.play(u.animate.set_value(u_of(100)),
                      run_time=beat.until("hundred", occurrence=2, offset=0.1), rate_func=SMOOTH)
            beat.wait_until("fifty", offset=-0.1)
            self.play(emph(meter.value, scale=1.2), run_time=0.7)
            beat.wait_until("at", occurrence=2, offset=-0.15)
            self.play(u.animate.set_value(1.0), run_time=beat.until("ninety-nine", offset=0.05),
                      rate_func=SMOOTH)
            beat.wait_until("rule", offset=-0.3)
            self.play(emph(naive2, scale=1.2), emph(meter.value, scale=1.2), run_time=0.75)
            # back to a random screen; the head counts appear outside their flows in silence
            self.play(u.animate(rate_func=SMOOTH).set_value(0.0),
                      FadeOut(marker2, rate_func=early), FadeOut(naive2, rate_func=early),
                      FadeIn(cnt20, rate_func=window(0.75, 1.0)),
                      FadeIn(cnt100, rate_func=window(0.75, 1.0)), run_time=2.0)
            self.hold(0.4)

        recall_lbl = label("recall", size=34, color=INK).next_to(L2["r99"], RIGHT, buff=0.22)
        prec_lbl = label("precision", size=34, color=INK)
        prec_lbl.next_to(meter.track, DOWN, buff=0.28).align_to(meter.track, LEFT)
        rec_ul = underline(recall_lbl, color=INK, buff=0.1, stroke_width=3)
        prec_ul = underline(prec_lbl, color=INK, buff=0.1, stroke_width=3)
        with self.narrate("Ninety-nine percent is the test's recall: how often the sick test "
                          "positive. [pause 0.3] Seventeen percent is its precision: how often the "
                          "positive are sick.") as beat:
            beat.wait_until("Ninety-nine", offset=-0.15)
            self.play(emph(L2["r99"], scale=1.2), run_time=0.8)
            beat.wait_until("recall", offset=-0.1)
            self.play(LaggedStart(Write(recall_lbl), Create(rec_ul), lag_ratio=0.45),
                      run_time=0.9)
            beat.wait_until("Seventeen", offset=-0.15)
            self.play(emph(meter.value, scale=1.3), run_time=0.8)
            beat.wait_until("precision", offset=-0.1)
            self.play(LaggedStart(Write(prec_lbl), Create(prec_ul), lag_ratio=0.45),
                      run_time=0.9)

        num.clear_updaters()
        driver.clear_updaters()
        self.end_card()
