"""Sample Space, episode 1: Three Right Answers to One Probability Question.

Bertrand's chord paradox.  Three honest simulations of "a random chord" disagree (1/3, 1/2,
1/4); the disagreement is explained by one picture (a chord is long iff its midpoint lands in
the triangle's inscribed circle, and each recipe scatters midpoints differently).  Jaynes's
invariance test is then run on screen (one rain, two circles: only the radius recipe agrees
with itself), his straw experiment is cited, and the same "what is spread evenly" split is
shown in real data (Feld & Grofman's class-size paradox).

    videos/toolkit/render.sh --preview videos/episodes/001-bertrand-paradox/scene.py Episode out.mp4
"""
from __future__ import annotations

import logging
import sys
from pathlib import Path

import numpy as np
from manim import *
from sample_space import *

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import sim                      # noqa: E402
import textures as tx           # noqa: E402
from narration_text import LINES  # noqa: E402


def P3(x, y):
    return np.array([x, y, 0.0])


def late(t):
    """Rate function for whatever arrives together with a lifted term (its last 40 %)."""
    return smooth(float(np.clip((t - 0.6) / 0.4, 0, 1)))


def window(a, b, f=there_and_back):
    """Rate function that runs `f` only between fractions a and b of a longer animation (so a
    short flag can ride inside a long play and land on its word)."""
    a, b = float(np.clip(a, 0, 0.98)), float(np.clip(b, 0, 1))
    b = max(b, a + 0.02)
    return lambda t: f(float(np.clip((t - a) / (b - a), 0, 1)))


# ----------------------------------------------------------------------------- layout
BIG_C = np.array([-2.75, 0.05, 0.0])
BIG_R = 2.6
COL_X = 3.35                      # right-hand column (cold open, naive build, landing)
PANEL_R = 1.35
PANEL_Y = 1.45
PANEL_X = [-4.4, 0.0, 4.4]
LABEL_Y = 3.2
TALLY_Y = -0.64
HIST_BASE = -2.72
HIST_W = 3.0
HIST_SCALE = 3.6                  # bar height per unit share
RECIPE_COL = [BLUE, GREEN, PURPLE]
RECIPE_NAME = ["random endpoints", "random radius point", "random midpoint"]
KEYS = ["endpoints", "radial", "midpoint"]
N_HAND = [8, 3, 1]                # chords drawn by hand before each rain
N_DOTS = 240                      # midpoints shown per panel
FRAC = 36                         # size of the small theory fractions (and tally-row equations)
RAIN_DIM = 0.3                    # a settled chord rain steps back to context
TAU_ = 2 * np.pi

# payoff: the floor, one big circle and a smaller off-centre one inside it (sim.SMALL_*)
FLOOR = (-6.25, 0.85, -2.55, 3.0)            # x0, x1, y0, y1 of the toss region
JC_B, JR_B = P3(-2.7, 0.2), 2.0
JR_S = JR_B * sim.SMALL_R
JC_S = JC_B + JR_B * P3(*sim.SMALL_C)
SB_LAB_L, SB_BIG, SB_SYM, SB_SMALL = 1.63, 3.95, 4.65, 5.35   # scoreboard columns (labels left-aligned)
SB_ROWS = [1.6, 1.0, 0.4, -0.2]

# class sizes (Feld & Grofman's paradox, toy example)
SIZES = [10, 10, 100]
CB_BASE, CB_X0, CB_H = -0.95, -6.0, 0.03     # baseline, left edge, height per student
W_EQ, W_PER, CB_GAP = 0.8, 0.03, 0.4         # equal widths -> width per student
ST_ROWS, ST_DY = 5, 0.15                     # student dots: 5 rows under each bar, 0.15 apart
ST_Y0 = CB_BASE - 0.2                        # first row of student dots


def rim(c, R, a):
    return c + R * P3(np.cos(a), np.sin(a))


def set_pixels(img, arr, opacity=1.0):
    img.pixel_array = arr.copy()
    img.orig_alpha_pixel_array = arr[:, :, 3].copy()
    if opacity < 1:
        img.pixel_array[:, :, 3] = (img.orig_alpha_pixel_array * opacity).astype(np.uint8)


def frac(num, den, num_col=INK, den_col=INK, size=MATH, buff=0.1):
    """Display-style fraction from separate pieces (so each piece can be a transform target)."""
    n = MathTex(num, font_size=size, color=num_col)
    d = MathTex(den, font_size=size, color=den_col)
    w = max(n.width, d.width) + 0.12
    bar = Line(LEFT * w / 2, RIGHT * w / 2, stroke_width=2.2 * size / 40, color=INK)
    n.next_to(bar, UP, buff=buff)
    d.next_to(bar, DOWN, buff=buff)
    g = VGroup(n, bar, d)
    g.num, g.bar, g.den = n, bar, d
    return g


def place_row(items, x, y, buff=0.18):
    """Lay items left to right centred at (x, y); fractions sit with their bar on y."""
    VGroup(*items).arrange(RIGHT, buff=buff).move_to(P3(x, y))
    for m in items:
        if hasattr(m, "bar"):
            m.shift(UP * (y - m.bar.get_y()))
        else:
            m.set_y(y)
    return VGroup(*items)


class Panel:
    """A circle with its inscribed equilateral triangle (vertex up) and an optional texture."""

    def __init__(self, center, R):
        self.circle = Circle(radius=R, color=INK, stroke_width=3).move_to(center)
        self.tri = Polygon(*[rim(center, R, PI / 2 + k * TAU / 3) for k in range(3)],
                           color=GRAY, stroke_width=2.5)
        self.circle.set_z_index(3)
        self.tri.set_z_index(3)
        self.img = None
        self.group = Group(self.circle, self.tri)

    @property
    def c(self):
        return self.circle.get_center()

    @property
    def R(self):
        return self.circle.width / 2

    def pt(self, uv):
        return self.c + self.R * P3(uv[0], uv[1])

    def make_texture(self, arr):
        img = ImageMobject(arr)
        img.height = 2 * tx.MARGIN * self.R
        img.move_to(self.c)
        img.set_z_index(0)
        img.ss_stage = -1
        set_pixels(img, arr)
        self.img = img
        self.group.add(img)
        return img

    def side(self, k=1):
        """Triangle side k as a Line (k=1: the bottom side)."""
        v = self.tri.get_vertices()
        return Line(v[k], v[(k + 1) % 3])


def question(size=MATH):
    """P( chord > side ) = ?  with the two segments drawn as glyphs."""
    p_open = MathTex(r"P\big(", font_size=size)
    gt = MathTex(">", font_size=size)
    p_close = MathTex(r"\big)", font_size=size)
    eq = MathTex("=", font_size=size)
    qm = MathTex("?", font_size=size)
    ch = Line(ORIGIN, RIGHT * 1.09 * size / 40, color=INK, stroke_width=5)
    sd = Line(ORIGIN, RIGHT * 0.99 * size / 40, color=GRAY, stroke_width=5)
    g = VGroup(p_open, ch, gt, sd, p_close, eq, qm).arrange(RIGHT, buff=0.16)
    for seg in (ch, sd):
        seg.set_y(gt.get_y())
    g.chord, g.side, g.qm = ch, sd, qm
    return g


def clip_to_floor(n, off):
    """The part of the line {x : x.n = off} inside the floor rectangle, or None."""
    t = np.array([-n[1], n[0]])
    base = n * off
    x0, x1, y0, y1 = FLOOR
    lo, hi = -1e9, 1e9
    for comp, a, b in ((0, x0, x1), (1, y0, y1)):
        if abs(t[comp]) < 1e-9:
            if not (a <= base[comp] <= b):
                return None
            continue
        s1, s2 = (a - base[comp]) / t[comp], (b - base[comp]) / t[comp]
        lo, hi = max(lo, min(s1, s2)), min(hi, max(s1, s2))
    if hi - lo < 0.3:
        return None
    return base + t * lo, base + t * hi


class Rain:
    """A set of lines {x : x.n = off} in scene units, judged on the big and small circles.
    `k` = how many of the `shown` lines are drawn; the tallies use the matching fraction of
    all lines (so they converge the way the drawing fills in)."""

    def __init__(self, th, off, shown, floor):
        self.n = np.stack([np.cos(th), np.sin(th)], 1)
        self.off = off
        self.shown = shown
        self.floor = floor
        self.k = ValueTracker(0)
        self.alpha = ValueTracker(1.0)
        self.skill = None
        self.judge = None           # floor rains (straws) are judged only once the answer is known
        self.pb = self.n @ JC_B[:2]
        self.ps = self.n @ JC_S[:2]

    def eff(self):
        if self.skill is None or self.skill.get_value() <= 0:
            return self.off
        # a skilled tosser: every straw pulled 93 % of the way toward the big circle's centre
        return self.off + self.skill.get_value() * 0.93 * (self.pb - self.off)

    def share(self, which, all_lines=False):
        offs = self.eff()
        m = len(offs) if all_lines else max(60, int(len(offs) * self.k.get_value() / len(self.shown)))
        p, r = (self.pb, JR_B) if which == "big" else (self.ps, JR_S)
        dist = np.abs(offs[:m] - p[:m])
        hit = dist < r
        return float((dist[hit] < r / 2).mean()) if hit.any() else 0.5


class Episode(NarratedScene):
    EPISODE = 1
    TITLE = "Three Right Answers to One Probability Question"
    SPEED = 0.84
    BEAT_GAP = 0.3

    # ------------------------------------------------------------------ data
    def prepare(self):
        res = sim.results()
        # chords are i.i.d.; start each recipe's list on a long chord so the first hand-drawn
        # example shows the gold rule (a swap does not change any statistic)
        for k in KEYS:
            r = res[k]
            i = int(np.argmax(r["long"]))
            for a in ("p", "q", "long"):
                r[a][[0, i]] = r[a][[i, 0]]
            r["share"] = sim.running_share(r["long"])
            r["mid"] = sim.mids(r["p"], r["q"])
            r["dist"] = np.hypot(r["mid"][:, 0], r["mid"][:, 1])
        self.res = res
        self.ns = tx.stage_counts()
        self.stages = {
            "endpoints": tx.stages(res["endpoints"]["p"], res["endpoints"]["q"],
                                   res["endpoints"]["long"], self.ns, 720),
            "radial": tx.stages(res["radial"]["p"], res["radial"]["q"], res["radial"]["long"],
                                self.ns, 400),
            "midpoint": tx.stages(res["midpoint"]["p"], res["midpoint"]["q"],
                                  res["midpoint"]["long"], self.ns, 400),
        }
        # straws: isotropic random lines in scene coordinates (Jaynes's zero-skill limit)
        rng = np.random.default_rng(1973)
        st_th = rng.uniform(0, np.pi, sim.N_STRAWS)
        st_off = rng.uniform(-7.5, 7.5, sim.N_STRAWS)
        n_st = np.stack([np.cos(st_th), np.sin(st_th)], 1)
        shown = [i for i in range(400) if clip_to_floor(n_st[i], st_off[i]) is not None][:150]
        self.straws = Rain(st_th, st_off, shown, floor=True)
        # one straw to follow: it crosses both circles, clearly long on the big one and clearly
        # short on the small one (same line, two verdicts)
        db = np.abs(st_off - n_st @ JC_B[:2])
        ds = np.abs(st_off - n_st @ JC_S[:2])
        good = [i for i in shown if db[i] < 0.3 * JR_B and 0.62 * JR_S < ds[i] < 0.88 * JR_S]
        good.sort(key=lambda i: -abs(np.cos(st_th[i])))         # prefer a steep straw
        self.follow_straw = good[0] if good else shown[0]
        logging.getLogger("sample_space").info(f"follow straw {self.follow_straw}: big d/R={db[self.follow_straw] / JR_B:.2f} "
                 f"small d/R={ds[self.follow_straw] / JR_S:.2f} ({len(good)} candidates)")
        # each recipe's chords of the big circle, as lines in scene coordinates (sim.py seeds)
        self.prog = {}
        for k, (th, d) in sim.test_rains().items():
            off = JR_B * d + JC_B[0] * np.cos(th) + JC_B[1] * np.sin(th)
            self.prog[k] = Rain(th, off, list(range(80)), floor=False)
        # one midpoint-program line to show how a program is judged on both circles: short for
        # the big circle, long for the small one (same line, two verdicts)
        Rm = self.prog["midpoint"]
        db, ds = np.abs(Rm.off - Rm.pb), np.abs(Rm.off - Rm.ps)
        # (the centres are 0.4 R apart, so the clearest flip is a near-vertical line between them)
        cand = [i for i in range(3000) if db[i] > 0.5 * JR_B and ds[i] < 0.5 * JR_S]
        cand.sort(key=lambda i: -min(db[i] / JR_B - 0.5, 0.5 - ds[i] / JR_S))   # widest margins
        self.demo_line = cand[0] if cand else 0
        logging.getLogger("sample_space").info(
            f"demo line {self.demo_line}: big d/R={db[self.demo_line] / JR_B:.2f} "
            f"small d/R={ds[self.demo_line] / JR_S:.2f} ({len(cand)} candidates)")

    # ------------------------------------------------------------------ helpers
    def chord_line(self, panel, p, q, long, width=4, opacity=1.0):
        return Line(panel.pt(p), panel.pt(q), stroke_width=width,
                    color=YELLOW if long else GRAY, stroke_opacity=opacity).set_z_index(2)

    def dedupe(self):
        """Drop duplicate top-level entries (removing a texture dissolves its Group and can
        leave a member listed twice; a later ReplacementTransform would then leave a ghost)."""
        seen, out = set(), []
        for m in self.mobjects:
            if id(m) not in seen:
                seen.add(id(m))
                out.append(m)
        self.mobjects = out

    def purge(self, *mobs):
        for m in mobs:
            while m in self.mobjects:
                self.mobjects.remove(m)
        self.remove(*mobs)

    def visible(self):
        """Top-level mobjects worth fading (not ValueTrackers or bare driver Mobjects)."""
        return [m for m in self.mobjects
                if not isinstance(m, ValueTracker) and (m.has_points() or m.submobjects
                                                       or isinstance(m, ImageMobject))]

    def flatten_groups(self):
        for m in list(self.mobjects):
            if type(m) is Group:
                subs = list(m.submobjects)
                self.remove(m)
                self.add(*[x for x in subs if x not in self.mobjects])
        self.dedupe()

    def lift_into(self, pairs, extra=(), rt=0.9, width=4):
        """Each (source shape, target term, colour): an outline copy lifts off the source and
        flies straight into the term in one move (scale shrinks geometrically while it
        travels), handing over to the glyphs in the last 40 %.  No filled morph, no pause."""
        anims, icons = [], []
        for src, term, col in pairs:
            ic = src.copy().set_fill(opacity=0).set_stroke(col, width=width, opacity=1)
            ic.clear_updaters()
            start = ic.copy()
            k = max(term.height, 0.28) / max(start.height, 1e-3)

            def upd(m, a, start=start, term=term, k=k):
                m.become(start)
                m.scale(k ** smooth(min(1.0, a / 0.6)))      # shrink first ...
                m.move_to(interpolate(start.get_center(), term.get_center(), smooth(a)))  # ... travel
                m.set_stroke(opacity=1 - float(np.clip((a - 0.6) / 0.4, 0, 1)))
            icons.append(ic)
            anims.append(UpdateFromAlphaFunc(ic, upd))
            anims.append(FadeIn(term, rate_func=late))
        self.add(*icons)
        self.play(*anims, *extra, run_time=rt)
        self.remove(*icons)

    def rain(self, panel, key, tally, counter, run_time):
        """Replay the simulation: texture stages + live tally + live count, log-time."""
        ns, stages, share = self.ns, self.stages[key], self.res[key]["share"]
        u = ValueTracker(0.0)
        n0, n1 = ns[0], ns[-1]

        def n_now():
            return int(round(n0 * (n1 / n0) ** u.get_value()))

        def upd_img(m):
            k = max(0, int(np.searchsorted(ns, n_now(), side="right")) - 1)
            if m.ss_stage != k:
                set_pixels(m, stages[k])
                m.ss_stage = k

        panel.img.add_updater(upd_img)
        tally.add_updater(lambda m: m.set_value(share[n_now() - 1]))
        fix = getattr(counter, "ss_fix", None)        # keeps a live count on its text baseline

        def upd_cnt(m):
            m.set_value(n_now())
            if fix:
                fix(m)
        if counter is not None:
            counter.add_updater(upd_cnt)
        self.play(u.animate.set_value(1.0), run_time=run_time, rate_func=linear)
        for m in (panel.img, tally, counter):
            if m is not None:
                m.clear_updaters()
        tally.set_value(share[-1])
        if counter is not None:
            counter.set_value(n1)
            if fix:
                fix(counter)

    def make_hist(self, key, x):
        """Share of all 10,000 midpoints in ten distance bands; gold = closer than r/2."""
        counts, _ = np.histogram(self.res[key]["dist"], bins=10, range=(0, 1))
        share = counts / counts.sum()
        x0 = x - HIST_W / 2
        bw = HIST_W / 10
        bars = VGroup(*[
            Rectangle(width=bw * 0.84, height=max(s * HIST_SCALE, 0.012), stroke_width=0,
                      fill_color=YELLOW if i < 5 else GRAY, fill_opacity=0.92)
            .move_to(P3(x0 + bw * (i + 0.5), HIST_BASE), aligned_edge=DOWN)
            for i, s in enumerate(share)])
        axis = Line(P3(x0 - 0.06, HIST_BASE), P3(x0 + HIST_W + 0.06, HIST_BASE), color=GRAY,
                    stroke_width=2.5)
        ticks = VGroup(*[MathTex(t, font_size=MATH_SMALL - 2, color=GRAY)
                         .next_to(P3(x0 + HIST_W * f, HIST_BASE), DOWN, buff=0.17)
                         for t, f in (("0", 0), ("r/2", 0.5), ("r", 1))])
        # one baseline for all three: "0" and "r" sit where the "2" of r/2 sits
        base = ticks[1][0][2].get_bottom()[1]
        for t in (ticks[0], ticks[2]):
            t.shift(UP * (base - t.get_bottom()[1]))
        g = VGroup(axis, bars, ticks)
        g.bars, g.axis, g.ticks, g.share = bars, axis, ticks, share
        return g

    def rain_mob(self, R, big_alpha, small_on, sim_alpha):
        """Draw the first k shown lines of rain R: faint straw (floor rains), the chord it cuts
        on the big circle and on the small one, each gold if long for that circle."""
        def build():
            g = VGroup()
            a = R.alpha.get_value() * sim_alpha.get_value()
            k = int(R.k.get_value())
            if a < 0.02 or k <= 0:
                return g
            offs = R.eff()
            jg = 1.0 if R.judge is None else R.judge.get_value()
            ab, asm = big_alpha.get_value() * jg, small_on.get_value() * jg
            for j in R.shown[:k]:
                n, d = R.n[j], offs[j]
                t = np.array([-n[1], n[0]])
                if R.floor:
                    seg = clip_to_floor(n, d)
                    if seg is not None:
                        g.add(Line(P3(*seg[0]), P3(*seg[1]), color=GRAY, stroke_width=1.5,
                                   stroke_opacity=0.42 * a))
                # the chords judged on the small circle sit at 70 % so its gold rule stays legible
                for c, r, al, w in ((JC_B, JR_B, ab, 3.0), (JC_S, JR_S, 0.7 * asm, 3.6)):
                    if al < 0.02:
                        continue
                    dist = d - n @ c[:2]
                    if abs(dist) < r:
                        h = np.sqrt(r * r - dist * dist)
                        m = c[:2] + n * dist
                        g.add(Line(P3(*(m - h * t)), P3(*(m + h * t)), stroke_width=w,
                                   color=YELLOW if abs(dist) < r / 2 else GRAY,
                                   stroke_opacity=a * al))
            return g.set_z_index(1)
        return always_redraw(build)

    # ------------------------------------------------------------------ scene
    def construct(self):
        self.prepare()
        R0 = self.res
        big = Panel(BIG_C, BIG_R)
        self.add(big.circle, big.tri)

        # ============================================================ cold open
        a0, b0 = np.deg2rad(148), np.deg2rad(290)
        e0 = VGroup(Dot(rim(BIG_C, BIG_R, a0), radius=0.07, color=INK),
                    Dot(rim(BIG_C, BIG_R, b0), radius=0.07, color=INK)).set_z_index(4)
        chord0 = Line(rim(BIG_C, BIG_R, a0), rim(BIG_C, BIG_R, b0), color=INK,
                      stroke_width=5).set_z_index(2)
        q = question(size=48).move_to(P3(COL_X, 2.25))
        side_hl = big.side(1).set_stroke(INK, 6).set_z_index(4)
        with self.narrate(LINES["open"]) as beat:
            self.play(FadeIn(e0, scale=0.5), run_time=0.5)
            self.play(Create(chord0), run_time=beat.until("at random", offset=-0.1))
            beat.wait_until("longer", offset=-0.1)
            self.play(TransformFromCopy(chord0, q.chord), Write(q[0]), Write(q[2]),
                      run_time=beat.until("side", offset=-0.1))
            self.play(Create(side_hl), run_time=0.5)
            self.play(TransformFromCopy(side_hl, q.side), Write(q[4]), run_time=0.8)
            self.play(FadeOut(side_hl), Write(q[5:]), run_time=beat.until("Pick", offset=-0.1))
            self.play(Indicate(q.qm, color=INK, scale_factor=1.25), run_time=0.8)

        # ============================================================ stakes
        cite_b = citation("Bertrand, 1889 · Calcul des probabilités")
        atr = text("at random", size=HEADING, slant=ITALIC).move_to(P3(COL_X, 1.25))
        atr_ul = underline(atr, color=GRAY, buff=0.08, stroke_width=3)
        with self.narrate(LINES["stakes"]) as beat:
            beat.wait_until("puzzle", offset=-0.2)
            self.play(Indicate(q, color=INK, scale_factor=1.06), run_time=0.8)
            beat.wait_until("eighteen", offset=-0.2)
            self.play(FadeIn(cite_b, shift=0.1 * UP), run_time=0.6)
            beat.wait_until("two words", offset=-0.2)
            self.play(Write(atr), run_time=0.9)
            beat.wait_until("at random", offset=-0.1)
            self.play(Create(atr_ul), run_time=0.6)
            beat.wait_until("decide", offset=-0.2)
            self.play(Indicate(atr, color=INK, scale_factor=1.08), run_time=0.9)

        # ============================================================ naive build: recipe 1
        r1 = R0["endpoints"]
        lab1 = label(RECIPE_NAME[0], size=32, color=BLUE).move_to(P3(COL_X, 1.25))
        hand1 = VGroup()
        with self.narrate(LINES["build1"]) as beat:
            self.play(FadeOut(cite_b), FadeOut(chord0), FadeOut(e0), run_time=0.6)
            beat.wait_until("obvious", offset=-0.1)
            self.play(FadeOut(atr, shift=0.15 * UP), FadeOut(atr_ul, shift=0.15 * UP), run_time=0.45)
            self.play(FadeIn(lab1, shift=0.15 * UP), run_time=0.55)
            p, qq = r1["p"][0], r1["q"][0]
            d1 = VGroup(Dot(big.pt(p), radius=0.07, color=INK),
                        Dot(big.pt(qq), radius=0.07, color=INK)).set_z_index(4)
            beat.wait_until("two", offset=-0.1)
            self.play(LaggedStart(*[GrowFromCenter(d) for d in d1], lag_ratio=0.5), run_time=1.0)
            beat.wait_until("join", offset=-0.1)
            c1 = self.chord_line(big, p, qq, False, width=5).set_color(INK)
            self.play(Create(c1), run_time=0.7)
            # compare with the side: lay a copy of the side along the chord from its first end
            beat.wait_until("beats", offset=-0.15)
            u = (big.pt(qq) - big.pt(p)) / np.linalg.norm(big.pt(qq) - big.pt(p))
            nrm = P3(-u[1], u[0]) * 0.16
            target = Line(big.pt(p) + nrm, big.pt(p) + nrm + u * big.R * np.sqrt(3)).set_stroke(INK, 6)
            self.play(TransformFromCopy(big.side(1).set_stroke(INK, 6), target),
                      run_time=beat.until("gold", offset=-0.15))
            self.play(c1.animate.set_color(YELLOW), FadeOut(target), run_time=0.6)
            hand1.add(c1)

        tally1 = DecimalNumber(0, num_decimal_places=3, font_size=60, color=BLUE)
        tally1.move_to(P3(COL_X, 0.3))
        cnt = DecimalNumber(10000, num_decimal_places=0, font_size=MATH_SMALL + 4, color=INK,
                            group_with_commas=True)
        cap_a = label("gold share of", size=26, color=GRAY)
        cap_b = label("simulated chords", size=26, color=GRAY)
        cap = VGroup(cap_a, cnt, cap_b).arrange(RIGHT, buff=0.14).move_to(P3(COL_X, -0.45))
        base_y = cap_a[1].get_bottom()[1]            # baseline of "gold share of" (bottom of "o")

        def on_baseline(m):
            m.shift(UP * (base_y - m[0].get_bottom()[1]))
        cnt.ss_fix = on_baseline
        tally1.set_value(r1["share"][self.ns[0] - 1])
        cnt.set_value(self.ns[0])
        on_baseline(cnt)
        cap_b.add_updater(lambda m: m.next_to(cnt, RIGHT, buff=0.14).shift(
            UP * (base_y - m.get_bottom()[1])))
        with self.narrate(LINES["rain1"]) as beat:
            more = []
            for i in range(1, N_HAND[0]):
                more.append(self.chord_line(big, r1["p"][i], r1["q"][i], r1["long"][i], width=3))
            self.play(LaggedStart(*[Create(m) for m in more], lag_ratio=0.4), FadeOut(d1),
                      run_time=beat.until("chords", end=True, offset=-0.1))
            hand1.add(*more)
            img1 = big.make_texture(self.stages["endpoints"][0])
            self.play(FadeIn(img1), hand1.animate.set_stroke(opacity=0.0), FadeIn(tally1),
                      FadeIn(cap), run_time=0.4)
            self.remove(hand1)
            self.rain(big, "endpoints", tally1, cnt, run_time=max(3.2, beat.remaining() + 0.5))
            cap_b.clear_updaters()

        # ---- geometry: corner on the first point, second point sweeps, far arc = 1/3
        a1 = np.deg2rad(150)
        P1 = Dot(rim(BIG_C, BIG_R, a1), radius=0.08, color=INK).set_z_index(5)
        phi = ValueTracker(a1 + np.deg2rad(25))

        def sweep_chord():
            a = phi.get_value()
            dang = (a - a1) % TAU_
            longc = np.deg2rad(120) < dang < np.deg2rad(240)
            return Line(rim(BIG_C, BIG_R, a1), rim(BIG_C, BIG_R, a), stroke_width=5,
                        color=YELLOW if longc else GRAY).set_z_index(4)

        P2 = always_redraw(lambda: Dot(rim(BIG_C, BIG_R, phi.get_value()), radius=0.08,
                                       color=INK).set_z_index(5))
        sw = always_redraw(sweep_chord)
        far = Arc(radius=BIG_R, start_angle=a1 + np.deg2rad(120), angle=np.deg2rad(120),
                  arc_center=BIG_C, color=YELLOW, stroke_width=9).set_z_index(4)
        arc_eq = VGroup(frac(r"120^\circ", r"360^\circ", YELLOW, BLUE, size=MATH + 4),
                        MathTex("=", font_size=MATH + 4),
                        frac("1", "3", BLUE, BLUE, size=MATH + 4)).arrange(RIGHT, buff=0.25)
        arc_eq.move_to(P3(COL_X, -1.85))
        with self.narrate(LINES["arc"]) as beat:
            self.play(img1.animate.set_opacity(0.16), GrowFromCenter(P1),
                      run_time=beat.until("Put", offset=-0.1))
            self.play(Rotate(big.tri, angle=a1 - PI / 2, about_point=BIG_C), run_time=1.6)
            beat.wait_until("The chord", offset=-0.1)
            self.add(sw, P2)
            self.play(phi.animate.set_value(a1 + np.deg2rad(205)),
                      run_time=beat.until("this far", offset=-0.05), rate_func=smooth)
            self.play(Create(far), phi.animate.set_value(a1 + np.deg2rad(180)), run_time=0.8)
            # the far arc itself flies into "120 degrees", then the whole rim into "360 degrees"
            self.lift_into([(far, arc_eq[0].num, YELLOW)], extra=[Create(arc_eq[0].bar, rate_func=late)],
                           rt=0.85, width=6)
            self.lift_into([(big.circle, arc_eq[0].den, BLUE)], rt=0.85)
            self.play(Write(arc_eq[1:]), run_time=0.5)

        # ============================================================ fail: three panels
        p2 = Panel(P3(PANEL_X[1], PANEL_Y), PANEL_R)
        p3 = Panel(P3(PANEL_X[2], PANEL_Y), PANEL_R)
        labs = [lab1.copy().scale(28 / 32).move_to(P3(PANEL_X[0], LABEL_Y))]
        for i in (1, 2):
            labs.append(label(RECIPE_NAME[i], size=28, color=RECIPE_COL[i]).move_to(P3(PANEL_X[i], LABEL_Y)))
        small_frac = frac("1", "3", BLUE, BLUE, size=FRAC)
        ap1 = MathTex(r"\approx", font_size=MATH)
        t1_target = tally1.copy().set(font_size=MATH)
        place_row([t1_target, ap1, small_frac], PANEL_X[0], TALLY_Y)
        shared_cap = label("10,000 simulated chords each", size=26, color=GRAY)
        shared_cap.move_to(P3(0, -1.6))
        # the scoreboard: each recipe's tally drops onto one number line as soon as it settles
        nl = NumberLine(x_range=[0.2, 0.55, 0.1], length=9.0, color=GRAY, stroke_width=2.5,
                        include_numbers=True, font_size=MATH_SMALL,
                        decimal_number_config={"num_decimal_places": 1, "color": GRAY},
                        tick_size=0.07)
        nl.move_to(P3(-0.3, -2.35))          # (centre includes the numbers: the line sits ~0.2 higher)
        nl_title = label("gold share", size=26, color=GRAY).next_to(nl, RIGHT, buff=0.25)
        nl_title.shift(UP * (nl.n2p(0.3)[1] - nl_title.get_y()))
        finals = [R0[k]["share"][-1] for k in KEYS]

        def errbar(v, col):
            half = 1.96 * np.sqrt(v * (1 - v) / sim.N)      # 95 % half-width (facts.md)
            l, r_ = nl.n2p(v - half), nl.n2p(v + half)
            h = 0.13
            return VGroup(Line(l, r_, color=col, stroke_width=4),
                          Line(l + UP * h, l + DOWN * h, color=col, stroke_width=4),
                          Line(r_ + UP * h, r_ + DOWN * h, color=col, stroke_width=4),
                          Dot(nl.n2p(v), radius=0.08, color=col)).set_z_index(3)

        ebars = [errbar(v, c) for v, c in zip(finals, RECIPE_COL)]

        def drop_dot(tally, dot):
            """The settled tally drops a dot onto the shared number line (from just under it)."""
            src = dot.copy().move_to(tally.get_bottom() + DOWN * 0.12)
            return TransformFromCopy(src, dot)
        with self.narrate(LINES["build2"]) as beat:
            self.remove(sw, P2)
            sw_static = sweep_chord()
            p2dot = Dot(rim(BIG_C, BIG_R, phi.get_value()), radius=0.08, color=INK).set_z_index(5)
            self.add(sw_static, p2dot)
            # the arc and its equation hold through "Case closed" (BAR: >= 3.2 s for 3 terms)
            beat.wait_until("way", offset=-0.35)
            # 1. the question, the caption and "120/360 =" leave first, so the 1/3 never
            #    travels through them
            self.play(FadeOut(arc_eq[0]), FadeOut(arc_eq[1]), FadeOut(q, shift=0.2 * UP),
                      FadeOut(cap), run_time=0.35)
            # 2. one move: the big circle becomes panel 1 (rain dimmed to context, triangle back
            #    upright, the sweep and arc shrinking with it as they fade), and its label, its
            #    tally and the exact third travel with it
            ratio, dest = PANEL_R / BIG_R, P3(PANEL_X[0], PANEL_Y)
            big.group.generate_target()
            big.group.target.scale(ratio).move_to(dest)
            big.group.target.submobjects[2].set_opacity(RAIN_DIM)
            big.group.target.submobjects[1].rotate(-(a1 - PI / 2), about_point=dest)
            riders = [m.animate.scale(ratio, about_point=BIG_C).shift(dest - BIG_C).set_opacity(0)
                      for m in (sw_static, p2dot, P1, far)]
            self.play(MoveToTarget(big.group), *riders,
                      ReplacementTransform(lab1, labs[0], path_arc=0.5),        # over the circle
                      ReplacementTransform(tally1, t1_target, path_arc=-0.6),   # under it
                      ReplacementTransform(arc_eq[2], small_frac), run_time=0.95)
            self.remove(sw_static, p2dot, P1, far)
            tally1 = t1_target
            self.play(FadeIn(ap1), Create(nl), FadeIn(nl_title), FadeIn(shared_cap),
                      Create(p2.circle), Create(p2.tri), FadeIn(labs[1], shift=0.1 * DOWN),
                      drop_dot(tally1, ebars[0][3]),
                      run_time=max(0.5, beat.until("radius", offset=-0.35)))
            r2 = R0["radial"]
            hand2 = VGroup()
            m = r2["mid"][0]
            th = np.arctan2(m[1], m[0])
            rad = Line(p2.c, rim(p2.c, p2.R, th), color=GREEN, stroke_width=4).set_z_index(4)
            pdot = Dot(p2.pt(m), radius=0.07, color=INK).set_z_index(5)
            ch = self.chord_line(p2, r2["p"][0], r2["q"][0], r2["long"][0], width=4)
            ra = RightAngle(Line(p2.pt(m), p2.c), Line(p2.pt(m), ch.get_end()), length=0.14,
                            color=INK, stroke_width=2).set_z_index(5)
            beat.wait_until("radius", offset=-0.15)
            self.play(Create(rad), run_time=0.7)
            beat.wait_until("random point", offset=-0.1)
            self.play(GrowFromCenter(pdot), run_time=0.5)
            beat.wait_until("draw", offset=-0.1)
            col = ch.get_color()
            ch.set_color(INK)
            self.play(GrowFromCenter(ch), Create(ra), run_time=beat.until("right angles", offset=0.2))
            self.play(ch.animate.set_color(col), run_time=0.5)
            self.play(FadeOut(rad), FadeOut(pdot), FadeOut(ra), run_time=0.4)
            hand2.add(ch)

        tally2 = DecimalNumber(r2["share"][self.ns[0] - 1], num_decimal_places=3, font_size=MATH,
                               color=GREEN)
        tally2.move_to(P3(PANEL_X[1], TALLY_Y))
        with self.narrate(LINES["rain2"]) as beat:
            for i in range(1, N_HAND[1]):
                m = r2["mid"][i]
                th = np.arctan2(m[1], m[0])
                rad = Line(p2.c, rim(p2.c, p2.R, th), color=GREEN, stroke_width=4).set_z_index(4)
                pdot = Dot(p2.pt(m), radius=0.06, color=INK).set_z_index(5)
                ch = self.chord_line(p2, r2["p"][i], r2["q"][i], r2["long"][i], width=4)
                self.play(Create(rad), GrowFromCenter(pdot), run_time=0.4)
                self.play(GrowFromCenter(ch), FadeOut(rad), FadeOut(pdot), run_time=0.4)
                hand2.add(ch)
            img2 = p2.make_texture(self.stages["radial"][0])
            self.play(FadeIn(img2), FadeIn(tally2), hand2.animate.set_stroke(opacity=0),
                      run_time=0.4)
            self.remove(hand2)
            self.rain(p2, "radial", tally2, None, run_time=max(2.6, beat.remaining() + 0.3))

        r3 = R0["midpoint"]
        tally3 = DecimalNumber(r3["share"][self.ns[0] - 1], num_decimal_places=3, font_size=MATH,
                               color=PURPLE)
        tally3.move_to(P3(PANEL_X[2], TALLY_Y))
        with self.narrate(LINES["build3"]) as beat:
            self.play(Create(p3.circle), Create(p3.tri), FadeIn(labs[2], shift=0.1 * DOWN),
                      drop_dot(tally2, ebars[1][3]), img2.animate.set_opacity(RAIN_DIM),
                      run_time=1.2)
            m = r3["mid"][0]
            mdot = Dot(p3.pt(m), radius=0.07, color=INK).set_z_index(5)
            ch = self.chord_line(p3, r3["p"][0], r3["q"][0], r3["long"][0], width=4)
            beat.wait_until("random point", offset=-0.1)
            self.play(GrowFromCenter(mdot), run_time=0.5)
            beat.wait_until("makes", offset=-0.1)
            self.play(GrowFromCenter(ch), run_time=0.9)
            beat.wait_until("That", offset=-0.5)
            img3 = p3.make_texture(self.stages["midpoint"][0])
            self.play(FadeIn(img3), FadeIn(tally3), FadeOut(ch), FadeOut(mdot), run_time=0.4)
            self.rain(p3, "midpoint", tally3, None, run_time=max(2.8, beat.remaining() + 0.3))

        # ---- the measured failure: error bars and the gap; Bertrand's verdict, both halves
        q1 = text("« Aucune des trois n'est fausse,", size=28, slant=ITALIC, color=INK)
        q2 = text("aucune n'est exacte »", size=28, slant=ITALIC, color=INK)
        VGroup(q1, q2).arrange(DOWN, buff=0.1).move_to(P3(-0.3, -1.46))
        cite_b2 = citation("Bertrand, 1889 · Calcul des probabilités")
        gap_brace = BraceBetweenPoints(nl.n2p(finals[2]) + UP * 0.2, nl.n2p(finals[1]) + UP * 0.2,
                                       direction=UP, color=INK)
        gap_lbl = label("25 points", size=28, color=INK).next_to(gap_brace, UP, buff=0.18)
        with self.narrate(LINES["gap"]) as beat:
            self.play(FadeOut(shared_cap), drop_dot(tally3, ebars[2][3]),
                      img3.animate.set_opacity(RAIN_DIM), FadeIn(cite_b2, shift=0.1 * UP),
                      run_time=0.8)
            beat.wait_until("wrong", offset=-0.5)
            self.play(FadeIn(q1, shift=0.1 * UP), *[lb.animate.set_opacity(0.3) for lb in labs],
                      run_time=0.6)
            beat.wait_until("right", offset=-0.4)
            self.play(FadeIn(q2, shift=0.1 * UP), run_time=0.6)
            beat.wait_until("Each", offset=-0.2)
            self.play(*[Create(VGroup(*e[:3])) for e in ebars], run_time=0.6)
            self.play(*[Indicate(VGroup(*e[:3]), color=e[0].get_color(), scale_factor=1.3)
                        for e in ebars], run_time=0.9)
            beat.wait_until("disagree", offset=-0.3)
            self.play(FadeOut(q1), FadeOut(q2), FadeOut(cite_b2), run_time=0.35)
            self.play(GrowFromCenter(gap_brace), run_time=0.5)
            self.play(Write(gap_lbl), run_time=beat.until("points", occurrence=1, offset=0.2))
            beat.wait_until("code", offset=-0.3)
            self.play(*[lb.animate.set_opacity(1.0) for lb in labs], run_time=0.3)
            self.play(LaggedStart(*[Indicate(lb, color=lb.get_color(), scale_factor=1.1) for lb in labs],
                                  lag_ratio=0.25), run_time=1.1)

        # ============================================================ insight
        p1 = big
        panels = [p1, p2, p3]
        dimmables = [*p1.group.submobjects, *p3.group.submobjects, labs[0], labs[2], tally1,
                     tally3, ap1, small_frac]
        for m in dimmables:
            m.save_state()
        p2_stuff = Group(labs[1], tally2)
        BIGP = P3(0, 0.33)
        RB = 2.65
        dtr = ValueTracker(0.0)
        atr_ang = ValueTracker(-PI / 2)

        def demo_mid():
            return p2.c + p2.R * dtr.get_value() * P3(np.cos(atr_ang.get_value()), np.sin(atr_ang.get_value()))

        def demo_chord():
            dd, a = dtr.get_value(), atr_ang.get_value()
            m = demo_mid()
            t = P3(-np.sin(a), np.cos(a))
            h = p2.R * np.sqrt(max(1 - dd * dd, 0))
            col = YELLOW if dd < 0.4985 else (INK if dd < 0.5015 else GRAY)
            return Line(m - h * t, m + h * t, color=col, stroke_width=6).set_z_index(6)

        with self.narrate(LINES["follow"]) as beat:
            # panel 2 grows into an ink-only "any chord" circle: no label, tally or rain
            p2.group.generate_target()
            p2.group.target.scale(RB / PANEL_R).move_to(BIGP)
            p2.group.target.submobjects[2].set_opacity(0.0)
            # the scoreboard leaves first, so the growing circle never passes over it
            self.play(FadeOut(nl), FadeOut(nl_title), *[FadeOut(e) for e in ebars],
                      FadeOut(gap_brace), FadeOut(gap_lbl), FadeOut(p2_stuff), run_time=0.4)
            self.play(*[m.animate.fade(0.72) for m in dimmables], MoveToTarget(p2.group),
                      run_time=0.9)
            dchord = always_redraw(demo_chord)
            ddot = always_redraw(lambda: Dot(demo_mid(), radius=0.09, color=INK).set_z_index(7))
            # "one point sets a chord's length": the chord first, then the point that sets it
            beat.wait_until("length", offset=-0.05)
            self.play(GrowFromCenter(dchord), run_time=0.6)
            beat.wait_until("midpoint", offset=-0.15)
            self.play(GrowFromCenter(ddot), run_time=0.5)
            beat.wait_until("Slide", offset=-0.1)
            self.play(dtr.animate.set_value(0.86), run_time=beat.until("matches", offset=-0.1),
                      rate_func=smooth)
            self.play(dtr.animate.set_value(0.5), run_time=beat.until("half", offset=-0.1))
            seg = Line(p2.c, demo_mid(), color=YELLOW, stroke_width=5).set_z_index(5)
            r_lab = MathTex(r"r/2", font_size=MATH, color=YELLOW).next_to(seg, LEFT, buff=0.22)
            r_lab.shift(UP * 0.12)
            self.play(Create(seg), Write(r_lab), run_time=0.9)
            beat.wait_until("circle", offset=-0.2)
            inc2 = Circle(radius=p2.R / 2, color=YELLOW, stroke_width=4).move_to(p2.c).set_z_index(4)
            self.play(Create(inc2), run_time=1.2)

        wander = ValueTracker(0.0)

        def wander_set(m):
            s = wander.get_value()
            dtr.set_value(0.5 + 0.34 * np.sin(TAU_ * 1.25 * s))
            atr_ang.set_value(-PI / 2 + TAU_ * 0.55 * s)
        incs = [None, inc2, None]
        with self.narrate(LINES["inside"]) as beat:
            driver = Mobject()
            driver.add_updater(wander_set)
            self.add(driver)
            self.play(FadeOut(seg), FadeOut(r_lab), wander.animate.set_value(0.42),
                      run_time=beat.until("inside", offset=-0.3), rate_func=linear)
            self.play(inc2.animate.set_fill(YELLOW, 0.14), wander.animate.set_value(1.0),
                      run_time=beat.until("Each", offset=-0.3), rate_func=linear)
            driver.clear_updaters()
            self.remove(driver)
            dchord.clear_updaters()
            ddot.clear_updaters()
            self.play(FadeOut(dchord), FadeOut(ddot), run_time=0.4)
            p2.group.add(inc2)
            p2.group.generate_target()
            p2.group.target.scale(PANEL_R / RB).move_to(P3(PANEL_X[1], PANEL_Y))
            p2.group.target.submobjects[2].set_opacity(RAIN_DIM)
            self.play(MoveToTarget(p2.group), *[Restore(m) for m in dimmables], run_time=1.0)
            # its label and tally return only once the circle has landed
            incs[0], incs[2] = inc2.copy().move_to(p1.c), inc2.copy().move_to(p3.c)
            self.play(FadeIn(p2_stuff), TransformFromCopy(inc2, incs[0]),
                      TransformFromCopy(inc2, incs[2]), run_time=max(0.8, beat.remaining() - 0.1))
        for P_, inc in zip(panels, incs):
            P_.group.add(inc)

        # ---- collapse chords to midpoints, one panel at a time; histogram of distances
        def do_collapse(P_, key, rt_lines=0.6, rt_shrink=1.6):
            r = R0[key]
            lines = VGroup(*[self.chord_line(P_, r["p"][i], r["q"][i], r["long"][i], width=1.6,
                                             opacity=0.9) for i in range(N_DOTS)])
            dots_ = VGroup(*[Dot(P_.pt(r["mid"][i]), radius=0.05,
                                 color=YELLOW if r["long"][i] else GRAY).set_z_index(2)
                             for i in range(N_DOTS)])
            self.play(FadeIn(lines), P_.img.animate.set_opacity(0.0), run_time=rt_lines)
            self.play(*[Transform(l, d) for l, d in zip(lines, dots_)], run_time=rt_shrink,
                      rate_func=smooth)
            P_.group.remove(P_.img)
            self.purge(P_.img)
            self.dedupe()
            return lines

        def grow_hist(h, extra=(), run_time=0.9):
            self.play(Create(h.axis), FadeIn(h.ticks),
                      LaggedStart(*[GrowFromEdge(b, DOWN) for b in h.bars], lag_ratio=0.08),
                      *extra, run_time=run_time)

        hists = [self.make_hist(k, x) for k, x in zip(KEYS, PANEL_X)]
        # the caption sits over the only histogram until the row fills, then moves to the middle
        cap2 = VGroup(label("share of midpoints,", size=24, color=GRAY),
                      label("by distance from center", size=24, color=GRAY)).arrange(DOWN, buff=0.06)
        cap2.move_to(P3(PANEL_X[2], -1.55))
        cap1 = label("share of midpoints, by distance from center", size=24, color=GRAY)
        cap1.move_to(P3(0, -1.385))

        # random midpoint: pi (r/2)^2 / pi r^2, built in the tally row from the two disks
        t3_slot = tally3.copy()
        ap3 = MathTex(r"\approx", font_size=MATH)
        eq3f = frac(r"\pi (r/2)^2", r"\pi r^2", YELLOW, PURPLE, size=FRAC)
        eq3s = MathTex("=", font_size=FRAC)
        eq3r = frac("1", "4", PURPLE, PURPLE, size=FRAC)
        place_row([t3_slot, ap3, eq3f, eq3s, eq3r], PANEL_X[2] - 0.05, TALLY_Y)
        with self.narrate(LINES["area"]) as beat:
            dots3 = do_collapse(p3, "midpoint", rt_lines=0.6,
                                rt_shrink=max(1.2, beat.until("midpoint program", offset=-0.2) - 0.6))
            grow_hist(hists[2], extra=[FadeIn(cap2)])
            self.play(ReplacementTransform(tally3, t3_slot), run_time=0.5)
            tally3 = t3_slot
            beat.wait_until("this circle", offset=-0.15)
            self.play(Indicate(incs[2], color=YELLOW, scale_factor=1.12),
                      run_time=max(0.5, min(0.8, beat.until("quarter", offset=-0.35))))
            # the two disks' outlines fly straight down into the fraction; the approximately
            # sign arrives with them, so the tally never shows an unfinished relation
            self.lift_into([(incs[2], eq3f.num, YELLOW), (p3.circle, eq3f.den, PURPLE)],
                           extra=[Create(eq3f.bar, rate_func=late), FadeIn(ap3, rate_func=late)], rt=0.9)
            beat.wait_until("quarter", occurrence=2, offset=-0.3)
            self.play(Write(eq3s), Write(eq3r), run_time=0.6)
        sf3 = frac("1", "4", PURPLE, PURPLE, size=FRAC)
        ap3b = ap3.copy()
        row3 = place_row([tally3.copy(), ap3b, sf3], PANEL_X[2], TALLY_Y)

        # radius recipe: prediction pause, collapse, equal rings, (r/2)/r in the tally row
        rad2 = Line(p2.c, rim(p2.c, p2.R, np.deg2rad(-30)), color=GREEN, stroke_width=6).set_z_index(5)
        t2_slot = tally2.copy()
        ap2 = MathTex(r"\approx", font_size=MATH)
        eq2f = frac(r"r/2", r"r", YELLOW, GREEN, size=FRAC)
        eq2s = MathTex("=", font_size=FRAC)
        eq2r = frac("1", "2", GREEN, GREEN, size=FRAC)
        place_row([t2_slot, ap2, eq2f, eq2s, eq2r], PANEL_X[1], TALLY_Y)
        with self.narrate(LINES["radius"]) as beat:
            beat.wait_until("spreads", offset=-0.1)
            self.play(Create(rad2), run_time=0.8)
            # the 1/4 has been up >= 4 s: fold it into the tally
            beat.wait_until("Where", offset=-0.1)
            self.play(FadeOut(eq3f), FadeOut(eq3s), run_time=0.35)
            self.play(ReplacementTransform(tally3, row3[0]), ReplacementTransform(ap3, ap3b),
                      ReplacementTransform(eq3r, sf3), run_time=0.6)
            tally3 = row3[0]
            beat.wait_until("Toward", offset=-0.5)
            dots2 = do_collapse(p2, "radial", rt_lines=0.4, rt_shrink=1.2)
            grow_hist(hists[1], extra=[FadeOut(cap2)], run_time=0.8)
            self.play(FadeIn(cap1), run_time=0.4)
            inner = Circle(radius=p2.R * 0.1, color=GREEN, fill_opacity=0.55, stroke_width=0).move_to(p2.c).set_z_index(4)
            outer = Annulus(inner_radius=p2.R * 0.9, outer_radius=p2.R, color=GREEN,
                            fill_opacity=0.55, stroke_width=0).move_to(p2.c).set_z_index(4)
            def bar_box(b):      # open at the baseline side: nothing dips toward the tick labels
                return Rectangle(width=b.width + 0.1, height=b.height + 0.05, color=GREEN,
                                 stroke_width=3).move_to(b, aligned_edge=DOWN)
            bx_in, bx_out = bar_box(hists[1].bars[0]), bar_box(hists[1].bars[9])
            beat.wait_until("equal", offset=-0.2)
            self.play(FadeIn(inner), FadeIn(outer), Create(bx_in), Create(bx_out), run_time=0.7)
            beat.wait_until("inner", offset=-0.1)
            self.play(Indicate(inner, color=GREEN, scale_factor=1.6), run_time=0.8)
            self.play(FadeOut(inner), FadeOut(outer), FadeOut(bx_in), FadeOut(bx_out),
                      ReplacementTransform(tally2, t2_slot), run_time=0.5)
            tally2 = t2_slot
            beat.wait_until("Half", offset=-0.2)
            half_seg = Line(p2.c, p2.c + (rad2.get_end() - p2.c) * 0.5, color=YELLOW,
                            stroke_width=7).set_z_index(6)
            self.play(Create(half_seg), run_time=0.5)
            self.play(TransformFromCopy(half_seg, eq2f.num), TransformFromCopy(rad2, eq2f.den),
                      Create(eq2f.bar), FadeIn(ap2, rate_func=late), run_time=0.9)
            self.play(Write(eq2s), Write(eq2r), run_time=0.6)

        # endpoint recipe: midpoints pile at the rim; the gold bars stack up to a third
        # the five gold bars are copied into their own column, left of the axis origin (no
        # tick), so the histogram itself keeps showing where the midpoints really are
        heights = [b.height for b in hists[0].bars[:5]]
        x_stack = hists[0].axis.get_left()[0] - 0.36
        stack_top = HIST_BASE + sum(heights)
        stack_base = Line(P3(x_stack - 0.2, HIST_BASE), P3(x_stack + 0.2, HIST_BASE), color=GRAY,
                          stroke_width=2.5)
        stack = VGroup()
        cum = 0.0
        for b, h in zip(hists[0].bars[:5], heights):
            stack.add(b.copy().move_to(P3(x_stack, HIST_BASE + cum + h / 2)))
            cum += h
        stack_lbl = MathTex(f"{sum(hists[0].share[:5]):.3f}", font_size=MATH_SMALL, color=INK)
        stack_lbl.next_to(P3(x_stack + 0.13, stack_top), RIGHT, buff=0.15).shift(DOWN * 0.12)
        rim_ring = Annulus(inner_radius=p1.R * 0.9, outer_radius=p1.R, color=BLUE, fill_opacity=0.55,
                           stroke_width=0).move_to(p1.c).set_z_index(4)
        with self.narrate(LINES["rim"]) as beat:
            dots1 = do_collapse(p1, "endpoints", rt_lines=0.3, rt_shrink=1.0)
            grow_hist(hists[0], run_time=0.55)
            # "against the rim": the outer ring of the panel and the last bar light up together
            beat.wait_until("rim", offset=-0.25)
            last_bar = hists[0].bars[9]
            self.play(FadeIn(rim_ring), last_bar.animate.set_fill(BLUE, opacity=0.92), run_time=0.35)
            self.hold(0.3)
            self.play(FadeOut(rim_ring), last_bar.animate.set_fill(GRAY, opacity=0.92), run_time=0.35)
            beat.wait_until("only", offset=-0.2)
            self.play(Create(stack_base), *[TransformFromCopy(b, s) for b, s in zip(hists[0].bars[:5], stack)],
                      *[b.animate.set_opacity(0.35) for b in hists[0].bars[:5]], run_time=0.9)
            self.play(FadeIn(stack_lbl, shift=0.1 * RIGHT), run_time=0.5)
            beat.wait_until("third we found", offset=-0.2)
            self.play(flag(small_frac, color=BLUE), flag(tally1, color=BLUE),
                      flag(stack_lbl, color=INK), run_time=0.9)

        # ---- what each recipe spreads evenly
        sf2 = frac("1", "2", GREEN, GREEN, size=FRAC)
        ap2b = ap2.copy()
        row2 = place_row([tally2.copy(), ap2b, sf2], PANEL_X[1], TALLY_Y)
        rad_hl = Line(p2.c, rim(p2.c, p2.R, np.deg2rad(-30)), color=GREEN, stroke_width=11).set_z_index(6)
        with self.narrate(LINES["which"]) as beat:
            # the 1/2 has been up through the whole endpoint beat: fold it into the tally
            self.play(FadeOut(eq2f), FadeOut(eq2s), FadeOut(half_seg), run_time=0.35)
            self.play(ReplacementTransform(tally2, row2[0]), ReplacementTransform(ap2, ap2b),
                      ReplacementTransform(eq2r, sf2), run_time=0.5)
            tally2 = row2[0]
            beat.wait_until("spread", offset=-0.2)
            self.play(*[h.animate.set_opacity(0.3) for h in hists], cap1.animate.set_opacity(0.3),
                      stack_lbl.animate.set_opacity(0.3), stack.animate.set_opacity(0.3),
                      stack_base.animate.set_opacity(0.3), rad2.animate.set_stroke(opacity=0.3),
                      run_time=0.8)
            beat.wait_until("rim", offset=-0.15)
            self.play(p1.circle.animate.set_stroke(BLUE, width=7), run_time=0.5)
            beat.wait_until("radius", offset=-0.2)
            self.play(Create(rad_hl), run_time=0.5)
            beat.wait_until("area", offset=-0.15)
            self.play(p3.circle.animate.set_fill(PURPLE, opacity=0.22), run_time=0.5)
            beat.wait_until("never", offset=-0.2)
            self.play(*[Indicate(lb, color=lb.get_color(), scale_factor=1.12) for lb in labs],
                      run_time=1.0)

        # ============================================================ payoff: Jaynes's test
        floor_rect = RoundedRectangle(corner_radius=0.12, width=FLOOR[1] - FLOOR[0] + 0.1,
                                      height=FLOOR[3] - FLOOR[2] + 0.1, color=DIM, stroke_width=2)
        floor_rect.move_to(P3((FLOOR[0] + FLOOR[1]) / 2, (FLOOR[2] + FLOOR[3]) / 2))
        sim_tag = label("simulated", size=24, color=GRAY, slant=ITALIC)
        sim_tag.next_to(floor_rect, UP, buff=0.16).align_to(floor_rect, LEFT).shift(RIGHT * 0.1)
        bcirc = Circle(radius=JR_B, color=INK, stroke_width=3).move_to(JC_B).set_z_index(4)
        btri = Polygon(*[rim(JC_B, JR_B, PI / 2 + k * TAU / 3) for k in range(3)], color=GRAY,
                       stroke_width=2.5).set_z_index(4)
        binc = Circle(radius=JR_B / 2, color=YELLOW, stroke_width=3).move_to(JC_B).set_z_index(4)
        # the small circle and its own gold rule sit above the chords, the rule on a dark halo
        scirc = Circle(radius=JR_S, color=INK, stroke_width=3.5).move_to(JC_S).set_z_index(6)
        sinc = Circle(radius=JR_S / 2, color=YELLOW, stroke_width=4.5).move_to(JC_S).set_z_index(6)
        shalo = Circle(radius=JR_S / 2, color=BG, stroke_width=13).move_to(JC_S).set_z_index(5)
        cite_j = citation("Jaynes, 1973 · Foundations of Physics")
        sim_alpha = ValueTracker(1.0)       # the whole simulation steps back for the real experiment
        big_alpha = ValueTracker(1.0)       # big-circle chords (subdued once the small circle judges)
        small_on = ValueTracker(0.0)
        straws = self.straws
        straws.skill = ValueTracker(0.0)
        straws.judge = ValueTracker(0.0)
        prog = self.prog
        rains = {"straws": self.rain_mob(straws, big_alpha, small_on, sim_alpha)}
        for k in ("midpoint", "endpoints", "radial"):
            prog[k].alpha.set_value(1.0)
            rains[k] = self.rain_mob(prog[k], big_alpha, small_on, sim_alpha)

        # scoreboard: one row per rain, big circle | small circle
        sb_title = label("gold share", size=26, color=GRAY).move_to(P3((SB_BIG + SB_SMALL) / 2, 2.85))
        icon_b = VGroup(Circle(radius=0.22, color=INK, stroke_width=2.5),
                        Circle(radius=0.11, color=YELLOW, stroke_width=2)).move_to(P3(SB_BIG, 2.3))
        icon_s = VGroup(Circle(radius=0.12, color=INK, stroke_width=2.5),
                        Circle(radius=0.06, color=YELLOW, stroke_width=2)).move_to(P3(SB_SMALL, 2.3))

        def sb_row(i, name, col):
            y = SB_ROWS[i]
            lab = label(name, size=26, color=col)
            lab.move_to(P3(SB_LAB_L + lab.width / 2, y))
            bn = DecimalNumber(0.5, num_decimal_places=2, font_size=MATH, color=col).move_to(P3(SB_BIG, y))
            sn = DecimalNumber(0.5, num_decimal_places=2, font_size=MATH, color=col).move_to(P3(SB_SMALL, y))
            return VGroup(lab, bn, sn)

        def dash_at(x, y):
            return MathTex(r"\text{--}", font_size=MATH, color=GRAY).move_to(P3(x, y))

        # row labels are the names the narration uses: midpoint, endpoints, radius
        rows = {"straws": sb_row(0, "straws", INK), "midpoint": sb_row(1, "midpoint", PURPLE),
                "endpoints": sb_row(2, "endpoints", BLUE), "radial": sb_row(3, "radius", GREEN)}
        # an empty cell reads "-" until that rain has started (no number before its evidence)
        dashes = {k: VGroup(dash_at(SB_BIG, SB_ROWS[i]), dash_at(SB_SMALL, SB_ROWS[i]))
                  for i, k in enumerate(rows)}
        syms = {k: MathTex("=" if k in ("straws", "radial") else r"\neq", font_size=MATH,
                           color=GRAY).move_to(P3(SB_SYM, SB_ROWS[i]))
                for i, k in enumerate(rows)}
        # the straws' own answer is never simulated into the test: it is unknown, but a toss
        # nobody can aim cannot tell the two circles apart, so it must be the same on both
        qmarks = VGroup(*[MathTex("?", font_size=MATH, color=GRAY).move_to(P3(x, SB_ROWS[0]))
                          for x in (SB_BIG, SB_SMALL)])
        dash = dashes["straws"][0]
        rs = rows["straws"]
        rs[0].set_opacity(0.4)

        def live(num, R, which):
            num.add_updater(lambda m: m.set_value(R.share(which)))

        with self.narrate(LINES["jaynes"]) as beat:
            keep = [p2.circle, p2.tri, inc2]
            self.flatten_groups()
            gone = [m for m in self.visible() if m not in keep]
            self.play(*[FadeOut(m) for m in gone], run_time=0.8)
            # the scoreboard (title, icon, the straws row and its empty slot) and the citation
            # are there from the first frame of the payoff
            self.play(ReplacementTransform(p2.circle, bcirc), ReplacementTransform(p2.tri, btri),
                      ReplacementTransform(inc2, binc), FadeIn(cite_j, shift=0.1 * UP),
                      FadeIn(sb_title), FadeIn(icon_b), FadeIn(rs[0]), FadeIn(dash), run_time=1.3)
            self.purge(p2.circle, p2.tri, inc2)
            self.dedupe()
            beat.wait_until("physical", offset=-0.2)
            self.play(Create(floor_rect), FadeIn(sim_tag), run_time=1.0)
            # unaimed straws (simulated): the lines only; their share is the unknown "?"
            beat.wait_until("straws", offset=-0.3)
            self.add(rains["straws"])
            straws.k.set_value(0)
            self.play(straws.k.animate(rate_func=linear).set_value(6), rs[0].animate.set_opacity(1.0),
                      ReplacementTransform(dash, qmarks[0]), run_time=0.6)
            self.play(straws.k.animate.set_value(len(straws.shown)),
                      run_time=beat.until("where", offset=-0.25), rate_func=linear)
            # same floor, a second circle: smaller and somewhere else
            ghost = VGroup(bcirc.copy(), binc.copy())
            halo_in = binc.copy().set_stroke(BG, width=13, opacity=0.0).set_z_index(5)
            self.play(Transform(ghost, VGroup(scirc, sinc)), Transform(halo_in, shalo),
                      small_on.animate.set_value(1.0),
                      big_alpha.animate.set_value(0.4), btri.animate.set_stroke(opacity=0.3),
                      binc.animate.set_stroke(opacity=0.5), FadeIn(icon_s),
                      run_time=max(1.0, beat.until("big", offset=0.1)))
            self.remove(ghost, halo_in)
            self.add(shalo, scirc, sinc)
            self.play(FadeIn(syms["straws"]), FadeIn(qmarks[1]), run_time=max(0.4, beat.remaining() - 0.1))

        # one straw, followed: it lands on both circles at once
        fs = self.follow_straw
        f_n, f_d = straws.n[fs], straws.off[fs]
        f_seg = clip_to_floor(f_n, f_d)
        f_line = Line(P3(*f_seg[0]), P3(*f_seg[1]), color=INK, stroke_width=3.5).set_z_index(7)

        def crossings(c, r):
            dist = f_d - f_n @ c[:2]
            h = np.sqrt(max(r * r - dist * dist, 0.0))
            m = c[:2] + f_n * dist
            t = np.array([-f_n[1], f_n[0]])
            return VGroup(*[Dot(P3(*(m + sg * h * t)), radius=0.085, color=INK).set_z_index(8)
                            for sg in (-1, 1)])
        f_big, f_small = crossings(JC_B, JR_B), crossings(JC_S, JR_S)

        # how a program is judged on both circles: one of its chords of the big circle (judged
        # there) and the piece of the same line inside the small circle (judged by the small
        # circle's own rule)
        R_m = prog["midpoint"]
        d_n, d_off = R_m.n[self.demo_line], R_m.off[self.demo_line]

        def demo_chord(c, r, width):
            dist = d_off - d_n @ c[:2]
            h = np.sqrt(max(r * r - dist * dist, 0.0))
            m = c[:2] + d_n * dist
            t = np.array([-d_n[1], d_n[0]])
            return Line(P3(*(m - h * t)), P3(*(m + h * t)), stroke_width=width,
                        color=YELLOW if abs(dist) < r / 2 else GRAY)
        demo_big = demo_chord(JC_B, JR_B, 5).set_z_index(7)
        demo_small = demo_chord(JC_S, JR_S, 9).set_z_index(8)

        def start_rain(key):
            """The row's dashes give way to live numbers as the first lines fall."""
            R, row = prog[key], rows[key]
            R.k.set_value(3)
            row[1].set_value(R.share("big"))
            row[2].set_value(R.share("small"))
            R.k.set_value(0)
            self.add(rains[key])
            self.play(R.k.animate(rate_func=linear).set_value(3), FadeOut(dashes[key]), FadeIn(row[1]),
                      FadeIn(row[2]), run_time=0.45)
            live(row[1], R, "big")
            live(row[2], R, "small")

        def rain_to(key, k, rt, *extra):
            self.play(prog[key].k.animate(rate_func=linear).set_value(k), *extra, run_time=max(0.5, rt))

        def finish_rain(key):
            R, row = prog[key], rows[key]
            for m in row[1:]:
                m.clear_updaters()
            row[1].set_value(R.share("big", all_lines=True))
            row[2].set_value(R.share("small", all_lines=True))

        failed = VGroup(rows["midpoint"], syms["midpoint"], rows["endpoints"], syms["endpoints"])
        straw_eq = VGroup(qmarks, syms["straws"])
        with self.narrate(LINES["test"]) as beat:
            # one rain lands on both circles at once: follow a single straw
            beat.wait_until("rain", offset=-0.15)
            self.play(Create(f_line), straws.alpha.animate.set_value(0.35), run_time=0.8)
            beat.wait_until("both", offset=-0.1)
            self.play(LaggedStart(GrowFromCenter(f_big[0]), GrowFromCenter(f_big[1]),
                                  GrowFromCenter(f_small[0]), GrowFromCenter(f_small[1]),
                                  lag_ratio=0.25), run_time=0.8)
            # every program gets a row; each fills only when its own rain starts
            beat.wait_until("so", offset=-0.1)
            self.play(FadeOut(f_line), FadeOut(f_big), FadeOut(f_small),
                      straws.alpha.animate.set_value(0.0),
                      LaggedStart(*[FadeIn(VGroup(rows[k][0], dashes[k]))
                                    for k in ("midpoint", "endpoints", "radial")], lag_ratio=0.25),
                      run_time=0.55)
            # one midpoint-program chord, judged on the big circle and then on the small one
            beat.wait_until("honest", offset=-0.15)
            self.play(Create(demo_big), run_time=0.6)
            self.play(Create(demo_small), run_time=0.6)
            self.hold(0.25)
            self.play(FadeOut(demo_big), FadeOut(demo_small), run_time=0.3)
            start_rain("midpoint")
            # the criterion is the straws' "? = ?": the same on both circles
            rt = max(0.5, beat.until("quarter", offset=0.2))
            a = max(0.0, beat.time_of("same") - 0.15 - beat.elapsed()) / rt
            rain_to("midpoint", len(prog["midpoint"].shown), rt,
                    btri.animate.set_stroke(opacity=0.0), binc.animate.set_stroke(opacity=0.2),
                    Indicate(straw_eq, color=INK, scale_factor=1.2, rate_func=window(a, a + 0.8 / rt)))
            finish_rain("midpoint")
            self.play(Indicate(rows["midpoint"][1], color=PURPLE, scale_factor=1.25), run_time=0.5)
            beat.wait_until("point", offset=-0.1)
            self.play(Indicate(rows["midpoint"][2], color=PURPLE, scale_factor=1.25),
                      FadeIn(syms["midpoint"], scale=0.6), run_time=0.7)
            self.play(prog["midpoint"].alpha.animate.set_value(0.0), run_time=0.3)
            start_rain("endpoints")
            rain_to("endpoints", len(prog["endpoints"].shown), beat.until("third", offset=-0.2))
            finish_rain("endpoints")
            self.play(Indicate(rows["endpoints"][1], color=BLUE, scale_factor=1.25), run_time=0.5)
            beat.wait_until("point", occurrence=2, offset=-0.1)
            self.play(Indicate(rows["endpoints"][2], color=BLUE, scale_factor=1.25),
                      FadeIn(syms["endpoints"], scale=0.6), run_time=0.7)
            self.play(prog["endpoints"].alpha.animate.set_value(0.0), run_time=0.3)
            start_rain("radial")
            rain_to("radial", len(prog["radial"].shown), beat.until("half", offset=-0.2))
            finish_rain("radial")
            self.play(FadeIn(syms["radial"], scale=0.6),
                      Indicate(rows["radial"][1:], color=GREEN, scale_factor=1.15), run_time=0.5)
            # "on both": the failed rows step back and the program's chords clear; the radius
            # row's "=" is the one that answers the straws' "? = ?"
            beat.wait_until("both", occurrence=3, offset=-0.1)
            self.play(failed.animate.set_opacity(0.3), prog["radial"].alpha.animate.set_value(0.0),
                      Indicate(straw_eq, color=INK, scale_factor=1.15),
                      Indicate(syms["radial"], color=GREEN, scale_factor=1.4), run_time=0.8)

        real = VGroup(label("5-inch circle", size=28, color=INK),
                      label("128 straws crossed it", size=28, color=INK)).arrange(DOWN, buff=0.16,
                                                                                  aligned_edge=LEFT)
        real.move_to(P3(0, -0.6)).align_to(P3(SB_LAB_L, 0), LEFT)
        skill_tag = label("simulated", size=24, color=GRAY, slant=ITALIC)
        skill_tag.move_to(P3(SB_SYM, SB_ROWS[0])).align_to(P3(SB_BIG + 0.62, 0), LEFT)
        with self.narrate(LINES["tyler"]) as beat:
            # 1. the test is over: its circle, its column and the failed rows leave first
            self.play(FadeOut(scirc), FadeOut(sinc), FadeOut(shalo), FadeOut(icon_s),
                      FadeOut(qmarks[1]), FadeOut(syms["straws"]), FadeOut(failed),
                      FadeOut(rows["radial"][2]), FadeOut(syms["radial"]),
                      small_on.animate.set_value(0.0), run_time=0.6)
            # 2. then the straws come back on the one circle, and radius moves up under straws
            self.play(straws.alpha.animate.set_value(1.0), big_alpha.animate.set_value(1.0),
                      binc.animate.set_stroke(opacity=1.0),
                      rows["radial"][:2].animate.shift(UP * (SB_ROWS[1] - SB_ROWS[3])), run_time=0.7)
            # the real experiment answers the straws' "?": the simulation steps back to context
            beat.wait_until("tossed", offset=-0.2)
            self.play(sim_alpha.animate.set_value(0.3), floor_rect.animate.set_stroke(opacity=0.3),
                      sim_tag.animate.set_opacity(0.3), run_time=1.0)
            beat.wait_until("five-inch", offset=-0.2)
            self.play(FadeIn(real[0], shift=0.1 * UP), run_time=0.6)
            beat.wait_until("hundred", offset=-0.2)
            self.play(FadeIn(real[1], shift=0.1 * UP), run_time=0.7)
            beat.wait_until("radius", offset=-0.3)
            self.play(Indicate(rows["radial"][:2], color=GREEN, scale_factor=1.2), run_time=0.8)

        with self.narrate(LINES["limit"]) as beat:
            # a skilled tosser is a different machine: simulated, judged, and set apart from the
            # real data; the straws' "?" becomes that simulation's live share
            sn = rows["straws"][1]
            sn.set_value(straws.share("big"))
            self.play(sim_alpha.animate.set_value(1.0), floor_rect.animate.set_stroke(opacity=1.0),
                      sim_tag.animate.set_opacity(1.0), straws.judge.animate.set_value(1.0),
                      real.animate.set_opacity(0.3), rows["radial"][:2].animate.set_opacity(0.3),
                      FadeOut(qmarks[0], rate_func=lambda t: smooth(min(1.0, t / 0.45))),
                      FadeIn(sn, rate_func=lambda t: smooth(max(0.0, (t - 0.5) / 0.5))),
                      FadeIn(skill_tag), run_time=0.6)
            live(sn, straws, "big")
            self.play(straws.skill.animate.set_value(1.0),
                      run_time=beat.until("other", offset=-0.1), rate_func=smooth)
            sn.clear_updaters()

        # ============================================================ the same two words in data
        wt = ValueTracker(0.0)          # 0: every class counts once -> 1: every student counts once

        def widths():
            t = wt.get_value()
            return [(1 - t) * W_EQ + t * W_PER * s for s in SIZES]

        def bar_left(i, w=None):
            w = widths() if w is None else w
            return CB_X0 + sum(w[:i]) + CB_GAP * i

        def bar_rect(i):
            w = widths()
            s = SIZES[i]
            return Rectangle(width=w[i], height=s * CB_H, stroke_color=GRAY, stroke_width=2,
                             fill_color=GRAY, fill_opacity=0.45).move_to(
                P3(bar_left(i, w) + w[i] / 2, CB_BASE + s * CB_H / 2))

        def right_end():
            return CB_X0 + sum(widths()) + 2 * CB_GAP

        def mean_w():
            w = widths()
            return sum(a * s for a, s in zip(w, SIZES)) / sum(w)

        cbase = Line(P3(CB_X0 - 0.15, CB_BASE), P3(right_end() + 0.15, CB_BASE), color=GRAY,
                     stroke_width=2.5)
        ytitle = label("class size (students)", size=24, color=GRAY)
        ytitle.move_to(P3(0, 2.84)).align_to(P3(CB_X0 - 0.15, 0), LEFT)
        ex_tag = label("example", size=22, color=GRAY, slant=ITALIC)
        ex_tag.next_to(ytitle, UP, buff=0.14).align_to(ytitle, LEFT)
        bars = [bar_rect(i) for i in range(3)]
        sz_lbl = [MathTex(str(s), font_size=MATH_SMALL + 2, color=INK).next_to(b, UP, buff=0.17)
                  for s, b in zip(SIZES, bars)]
        # one dot per class (equal widths) ... then one dot per student (width = students)
        w0 = [W_EQ] * 3
        w1 = [W_PER * s for s in SIZES]
        mid_row = ST_Y0 - (ST_ROWS - 1) / 2 * ST_DY
        cdots = VGroup(*[Dot(P3(bar_left(i, w0) + W_EQ / 2, mid_row), radius=0.06, color=INK)
                         for i in range(3)])
        st_from, st_to = [], []
        for i, s in enumerate(SIZES):
            ncol = s // ST_ROWS
            for j in range(s):
                col, row = j // ST_ROWS, j % ST_ROWS
                st_from.append(np.array([bar_left(i, w0) + W_EQ / 2, mid_row, 0.0]))
                st_to.append(np.array([bar_left(i, w1) + (col + 0.5) * w1[i] / ncol,
                                       ST_Y0 - row * ST_DY, 0.0]))
        sdots = VGroup(*[Dot(p, radius=0.06, color=INK) for p in st_from])

        def place_students(m):
            t = wt.get_value()
            for d, a, b in zip(m, st_from, st_to):
                d.move_to(a + (b - a) * t)
        wlab = label("width = students", size=22, color=GRAY)
        wlab.move_to(P3((CB_X0 + bar_left(2, w1) + w1[2]) / 2, ST_Y0 - (ST_ROWS - 1) * ST_DY - 0.38))
        y40 = CB_BASE + 40 * CB_H
        line40 = DashedLine(P3(CB_X0 - 0.15, y40), P3(right_end() + 0.15, y40), color=GRAY,
                            stroke_width=3, dash_length=0.12).set_z_index(3)
        lab40 = VGroup(label("random class", size=24, color=GRAY),
                       MathTex("40", font_size=MATH, color=INK)).arrange(RIGHT, buff=0.15)
        lab40.next_to(line40.get_end(), RIGHT, buff=0.2)
        cite_fg = citation("Feld & Grofman, 1977 · Research in Higher Education")
        # the real university, in its own framed block (not on the toy chart's scale)
        SBX = 2.3
        sb_rule = Line(P3(SBX - 0.3, 3.05), P3(SBX - 0.3, 0.4), color=GRAY, stroke_width=2.5)
        sb_head = VGroup(label("Stony Brook, 1974", size=28, color=INK),
                         label("737 classes", size=24, color=GRAY)).arrange(DOWN, buff=0.12,
                                                                            aligned_edge=LEFT)
        sb_head.move_to(P3(0, 2.55)).align_to(P3(SBX, 0), LEFT)

        def sb_line(y, glyph, name, col, num):
            g = glyph.move_to(P3(SBX + 0.25, y))
            lb = label(name, size=24, color=col).next_to(g, RIGHT, buff=0.2)
            lb.set_y(y)
            n = MathTex(num, font_size=48, color=INK)
            n.move_to(P3(0, y)).align_to(P3(6.2, 0), RIGHT)
            return VGroup(g, lb, n)
        sb_r1 = sb_line(1.4, DashedLine(LEFT * 0.25, RIGHT * 0.25, color=GRAY, stroke_width=3,
                                        dash_length=0.1), "random class", GRAY, "40")
        sb_r2 = sb_line(0.7, Line(LEFT * 0.25, RIGHT * 0.25, color=INK, stroke_width=4),
                        "random student", INK, "147")
        # "the same two words": the stakes beat's italic "at random", back as the chart's caption,
        # above its title and right-aligned to the chart (it is context, not the subject)
        chart_right = CB_X0 + sum(w1) + 2 * CB_GAP + 0.15
        atr2 = text("at random", size=28, slant=ITALIC)
        atr2.move_to(P3(0, 3.3)).align_to(P3(chart_right + 0.1, 0), RIGHT)
        atr2_ul = underline(atr2, color=GRAY, buff=0.07, stroke_width=2.5)
        cap_atr = VGroup(atr2, atr2_ul).set_opacity(0.7)
        # ... but it first returns at the stakes beat's size, as the frame's one subject
        atr_big = text("at random", size=HEADING, slant=ITALIC).move_to(P3(-3.8, 0.7))
        atr_big_ul = underline(atr_big, color=GRAY, buff=0.08, stroke_width=3)
        with self.narrate(LINES["classes"]) as beat:
            rains_all = list(rains.values())
            for m in rains_all + [rows["straws"][1]]:
                m.clear_updaters()
            self.flatten_groups()
            # the floor gives way straight to the two words: no empty frame in between
            self.play(*[FadeOut(m) for m in self.visible()], FadeIn(cite_fg, shift=0.1 * UP),
                      run_time=0.45)
            self.play(Write(atr_big), run_time=0.75)
            self.play(Create(atr_big_ul), run_time=0.35)
            # the chart builds with its bars (no empty baseline); the words step up to become
            # its caption
            beat.wait_until("Take", offset=-0.35)
            self.play(ReplacementTransform(atr_big, atr2), ReplacementTransform(atr_big_ul, atr2_ul),
                      run_time=0.6)
            self.play(FadeIn(ytitle), FadeIn(ex_tag), run_time=0.35)
            for occ, i in ((1, 0), (2, 1)):
                beat.wait_until("ten", occurrence=occ, offset=-0.15)
                extra = [Create(cbase)] if i == 0 else []
                self.play(GrowFromEdge(bars[i], DOWN), FadeIn(sz_lbl[i], shift=0.1 * UP), *extra,
                          run_time=0.5)
            beat.wait_until("hundred", offset=-0.15)
            self.play(GrowFromEdge(bars[2], DOWN), FadeIn(sz_lbl[2], shift=0.1 * UP), run_time=0.7)
            # a random class: one dot per class, every bar the same width, mean 40; the caption
            # flags on the spoken "at random"
            beat.wait_until("class", offset=-0.15)
            rt = 1.0
            a = max(0.0, beat.time_of("at random") - 0.1 - beat.elapsed()) / rt
            self.play(LaggedStart(*[GrowFromCenter(d) for d in cdots], lag_ratio=0.3),
                      Indicate(cap_atr, color=INK, scale_factor=1.1, rate_func=window(a, a + 0.6 / rt)),
                      run_time=rt)
            self.play(Create(line40), run_time=max(0.6, beat.until("forty", offset=-0.45)))
            self.play(FadeIn(lab40, shift=0.1 * LEFT), run_time=0.5)
            # a random student: each class dot becomes its students, each bar as wide as its
            # students, and the width-weighted mean rises to 85
            beat.wait_until("Pick", occurrence=2, offset=-0.05)
            self.remove(*cdots)
            self.add(sdots)
            for i, b in enumerate(bars):
                b.add_updater(lambda m, i=i: m.become(bar_rect(i)))
                sz_lbl[i].add_updater(lambda m, i=i: m.next_to(bars[i], UP, buff=0.17))
            cbase.add_updater(lambda m: m.put_start_and_end_on(P3(CB_X0 - 0.15, CB_BASE),
                                                               P3(right_end() + 0.15, CB_BASE)))
            sdots.add_updater(place_students)
            mline = always_redraw(lambda: Line(P3(CB_X0 - 0.15, CB_BASE + mean_w() * CB_H),
                                               P3(right_end() + 0.15, CB_BASE + mean_w() * CB_H),
                                               color=INK, stroke_width=4).set_z_index(4))
            mval = DecimalNumber(40, num_decimal_places=0, font_size=MATH, color=INK)
            mlab = VGroup(label("random student", size=24, color=INK), mval).arrange(RIGHT, buff=0.15)
            mval.add_updater(lambda m: m.set_value(mean_w()))

            def place_mlab(m):
                m.next_to(P3(right_end() + 0.15, CB_BASE + mean_w() * CB_H), RIGHT, buff=0.2)
                m.set_opacity(float(np.clip((mean_w() - 57) / 6, 0, 1)))   # clear of the 40 label first
            mlab.add_updater(place_mlab)
            wlab.add_updater(lambda m: m.set_opacity(float(np.clip((wt.get_value() - 0.35) / 0.3, 0, 1))))
            line40.add_updater(lambda m: m.put_start_and_end_on(P3(CB_X0 - 0.15, y40),
                                                                P3(right_end() + 0.15, y40)))
            lab40.add_updater(lambda m: m.next_to(P3(right_end() + 0.15, y40), RIGHT, buff=0.2))
            mlab.set_opacity(0)
            wlab.set_opacity(0)
            self.add(mline, mlab, wlab)
            rt = max(1.6, beat.until("eighty-five", offset=0.3))
            a = max(0.0, beat.time_of("at random", 2) - 0.1 - beat.elapsed()) / rt
            self.play(wt.animate.set_value(1.0),
                      Indicate(cap_atr, color=INK, scale_factor=1.1, rate_func=window(a, a + 0.6 / rt)),
                      run_time=rt)
            for m in [*bars, *sz_lbl, cbase, sdots, mval, mlab, wlab, line40, lab40, mline]:
                m.clear_updaters()
            mval.set_value(85)
            mlab.set_opacity(1)
            wlab.set_opacity(1)
            # the real university: the example steps back (its lines stay, dimmed; its labels and
            # numbers leave, so the only bright numbers are Stony Brook's), the cited figures get
            # their own block
            beat.wait_until("Stony", offset=-0.2)
            toy = VGroup(*bars, *sz_lbl, cbase, sdots, line40, mline, ytitle, ex_tag)
            self.play(toy.animate.set_opacity(0.3), FadeOut(lab40), FadeOut(mlab), FadeOut(wlab),
                      FadeOut(cap_atr), Create(sb_rule), FadeIn(sb_head, shift=0.1 * DOWN), run_time=0.8)
            beat.wait_until("forty", occurrence=2, offset=-0.2)
            self.play(FadeIn(sb_r1, shift=0.15 * LEFT), run_time=0.5)
            beat.wait_until("hundred", occurrence=2, offset=-0.15)
            self.play(FadeIn(sb_r2, shift=0.15 * LEFT), run_time=0.6)

        # ============================================================ landing
        q_end = question(size=48).move_to(P3(COL_X, 2.25))
        # the 0-1 line carries only its ends: the three answers are the only marks on it
        line01 = NumberLine(x_range=[0, 1, 1], length=5.2, color=GRAY, stroke_width=3,
                            include_numbers=False, tick_size=0.08).move_to(P3(COL_X, 0.45))
        ends_lbl = VGroup(MathTex("0", font_size=MATH_SMALL + 2, color=GRAY).next_to(line01.n2p(0), DOWN, buff=0.22),
                          MathTex("1", font_size=MATH_SMALL + 2, color=GRAY).next_to(line01.n2p(1), DOWN, buff=0.22))
        marks = VGroup()
        mark_vals = (1 / 4, 1 / 3, 1 / 2)
        for v, col, (nn, dd) in zip(mark_vals, (PURPLE, BLUE, GREEN), (("1", "4"), ("1", "3"), ("1", "2"))):
            dot = Dot(line01.n2p(v), radius=0.09, color=col).set_z_index(3)
            f = frac(nn, dd, col, col, size=FRAC)
            f.next_to(dot, DOWN if v == 1 / 3 else UP, buff=0.2)
            marks.add(VGroup(dot, f))
        marker = Triangle(color=INK, fill_opacity=1, stroke_width=0).scale(0.12).rotate(PI)
        mk = ValueTracker(0.0)
        marker.add_updater(lambda m: m.move_to(line01.n2p(mk.get_value()) + UP * 0.24))
        overlay = always_redraw(lambda: Line(line01.n2p(0), line01.n2p(max(mk.get_value(), 1e-3)),
                                             color=INK, stroke_width=6).set_z_index(2))
        for mark, v in zip(marks, mark_vals):       # each answer appears as the sweep passes it
            mark.set_opacity(0)
            mark.add_updater(lambda m, v=v: m.set_opacity(float(np.clip((mk.get_value() - v) / 0.05, 0, 1))))
        # "name the way": the unaimed straws are the way that picks the green half
        straw_tag = label("straws", size=26, color=INK).next_to(marks[2][1], RIGHT, buff=0.25)
        e0b = e0.copy()
        chord0b = Line(rim(BIG_C, BIG_R, a0), rim(BIG_C, BIG_R, b0), color=INK, stroke_width=5).set_z_index(2)
        mid0 = (chord0b.get_start() + chord0b.get_end()) / 2
        inc0 = Circle(radius=BIG_R / 2, color=YELLOW, stroke_width=4).move_to(BIG_C).set_z_index(1)
        big_end = Circle(radius=BIG_R, color=INK, stroke_width=3).move_to(BIG_C).set_z_index(3)
        tri_end = Polygon(*[rim(BIG_C, BIG_R, PI / 2 + k * TAU / 3) for k in range(3)], color=GRAY,
                          stroke_width=2.5).set_z_index(3)
        # Stony Brook's two right answers keep their own rows, left-aligned with the question and
        # well below the 0-1 line (never read as values on it)
        sb_shift = np.array([q_end.get_left()[0] - sb_r1.get_left()[0], -1.6 - sb_r1[0].get_y(), 0.0])
        with self.narrate(LINES["land"]) as beat:
            self.flatten_groups()
            # the block's header and rule clear first; its two rows stay
            self.play(*[FadeOut(m) for m in self.visible() if m not in (sb_r1, sb_r2)], run_time=0.45)
            # the first frame, back again; Stony Brook's rows step down out of its way, dimmed
            self.play(sb_r1.animate.shift(sb_shift).set_opacity(0.35),
                      sb_r2.animate.shift(sb_shift).set_opacity(0.35),
                      FadeIn(big_end), FadeIn(tri_end), FadeIn(chord0b), FadeIn(e0b), FadeIn(q_end),
                      run_time=0.8)
            # the axis first, then the sweep that finds every answer on it
            self.play(Create(line01), FadeIn(ends_lbl), run_time=0.5)
            self.add(overlay, marker, marks)
            self.play(mk.animate.set_value(1.0), run_time=max(1.2, beat.until("right", offset=0.1)),
                      rate_func=smooth)
            for mark in marks:
                mark.clear_updaters()
                mark.set_opacity(1)
            marker.clear_updaters()
            # the opening chord, re-seen: its midpoint sits inside the gold circle (outline
            # first, then the fill, so the disk never draws as a wedge)
            self.play(FadeOut(marker), chord0b.animate.set_color(YELLOW),
                      GrowFromCenter(Dot(mid0, radius=0.09, color=INK).set_z_index(5)),
                      Create(inc0), run_time=0.7)
            # "Name the way, and only one is": the straws pick the green half, the others step back
            beat.wait_until("Name", offset=-0.1)
            self.play(inc0.animate.set_fill(YELLOW, 0.12), FadeIn(straw_tag, shift=0.1 * LEFT),
                      Indicate(marks[2], color=GREEN, scale_factor=1.25), run_time=0.6)
            beat.wait_until("only", offset=-0.1)
            self.play(marks[0].animate.set_opacity(0.3), marks[1].animate.set_opacity(0.3), run_time=0.5)
            # "Forty and a hundred forty-seven are both right, once you say who's picked"
            beat.wait_until("Forty", offset=-0.25)
            self.play(sb_r1.animate.set_opacity(1.0), sb_r2.animate.set_opacity(1.0), run_time=0.5)
            beat.wait_until("both", offset=-0.15)
            self.play(*[Indicate(r[2], color=INK, scale_factor=1.15) for r in (sb_r1, sb_r2)], run_time=0.6)
            beat.wait_until("who's", offset=-0.25)
            self.play(*[Indicate(r[1], color=INK, scale_factor=1.1) for r in (sb_r1, sb_r2)], run_time=0.7)
        overlay.clear_updaters()
        self.hold(1.4)
