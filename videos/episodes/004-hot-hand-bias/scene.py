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

    def build_mini(self, scale: float = 0.81, at=(0, 0.1, 0), op: float = 0.6) -> VGroup:
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
            self.allow_overlap(g_, reason="ghost miniature of the 16-row table (60% opacity): "
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
            # the ringed heads' yellow disc shrinks into the yellow 1 (no letter travels, so no
            # glyph is ever doubled), as the two rings will shrink into the 2
            self.play(self.fly_into([big[1][0]], big_score[0], arc=PI / 2, start=0.3),
                      run_time=0.8)
            self.clean_fly()
            self.play(self.fly_into(list(big_rings), big_score[2], arc=PI / 2, lag=0.1, start=0.4),
                      FadeIn(big_score[1]), run_time=0.8)
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
            self.play(Create(focus), run_time=beat.until("checks", offset=-0.1))
            self.play(LaggedStart(*[Create(r) for r in c1["rings"]], lag_ratio=0.3),
                      run_time=beat.until("two", offset=-0.1))
            heads_chk = VGroup(*[c1["coins"][i] for i in c1["chk"] if c1["seq"][i] == "H"])
            # the two heads' discs shrink into the 2 and the three rings into the 3 (no letters
            # travel), arcing over the row
            self.play(self.fly_into([c[0] for c in heads_chk], c1["score"][0], arc=-1.0, lag=0.1),
                      self.fly_into(list(c1["rings"]), c1["score"][2], arc=-1.0, lag=0.1),
                      FadeIn(c1["score"][1]), run_time=1.0)
            self.clean_fly()
            self.adopt(c1["rings"], c1["score"])
            beat.wait_until("Score", offset=-0.1)
            rest = [k for k in SCORED if k not in (k0, k1)]
            self.play(FadeOut(focus),
                      LaggedStart(*[AnimationGroup(Create(cards[k]["rings"]),
                                                   FadeIn(cards[k]["score"], shift=0.1 * LEFT))
                                    for k in rest], lag_ratio=0.18),
                      run_time=beat.remaining(2.2))

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
        with self.beat("average") as beat:
            beat.wait_until("Drop", offset=-0.1)
            shrink = [cards[k]["score"].copy() for k in SCORED]
            self.add(*shrink)
            self.play(LaggedStart(*[AnimationGroup(s_.animate.move_to(d_).scale(0.15)
                                                   .set_opacity(0), GrowFromCenter(d_))
                                    for s_, d_ in zip(shrink, seeds)], lag_ratio=0.04),
                      run_time=0.6)
            self.remove(*shrink)
            self.play(LaggedStart(*[d_.animate.move_to(t_.get_center())
                                    for d_, t_ in zip(seeds, dots)], lag_ratio=0.06),
                      run_time=beat.until("Their", offset=-0.1))
            self.remove(*seeds)
            self.add(dots)
            mean_num.update()
            self.add(blue_line)
            self.play(FadeIn(mean_num), run_time=0.4)
            self.play(m.animate.set_value(MEAN), run_time=beat.until_end_of("two"),
                      rate_func=smooth)

        GAP_Y = -0.9
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
        frac_a = score_tex(12, 24, size=40)
        frac_a.move_to([fa[2].get_right()[0] - frac_a.width / 2, fa[2].get_center()[1], 0])
        nums = [cards[k]["score"][0] for k in SCORED]
        dens = [cards[k]["score"][2] for k in SCORED]
        axis_group = VGroup(self.axis, dashed, guess_lbl, dots, gap_arrow, cold_lbl)
        with self.beat("pool") as beat:
            # make room for the right column: the line and everything on it slides left; the
            # row-average marker shrinks to the vote lane (below the pooled strip to come), so
            # the pooled strip is read only against the dashed one-half line
            self.play(OFF.animate.set_value(0.0), axis_group.animate.shift(LEFT * SHIFT1),
                      mtop.animate.set_value(SB_Y + TILE_H / 2 + 0.15),
                      run_time=beat.until("Gather", offset=-0.2))
            srcs = heads_src + tails_src
            # each ringed coin's disc becomes a tile (the letters stay in the table)
            self.play(FadeOut(dots), FadeOut(gap_arrow), FadeOut(cold_lbl),
                      LaggedStart(*[TransformFromCopy(c[0], t) for c, t in zip(srcs, a_tiles)],
                                  lag_ratio=0.035),
                      run_time=beat.until("twelve", offset=-0.15))
            self.play(self.fly_into(a_yellow, frac_a[0]), FadeIn(scrim), run_time=0.8)
            self.clean_fly()
            beat.wait_until("twelve", 2, offset=-0.1)
            self.play(self.fly_into(a_tiles, frac_a[2], lag=0.01), FadeIn(frac_a[1]),
                      run_time=0.8)
            self.clean_fly()
            self.adopt(frac_a)
            # "Total heads over total flips": 12/24 restacks; every row's heads count sums into
            # the numerator, every row's checked count into the denominator
            beat.wait_until("Total", offset=-0.2)
            self.play(FadeOut(scrim), ReplacementTransform(frac_a[0], fa[2][0:2]),
                      ReplacementTransform(frac_a[1], fa[2][2]),
                      ReplacementTransform(frac_a[2], fa[2][3:5]), run_time=0.45)
            self.play(self.fly_into(nums, fa_num, lag=0.03), run_time=0.6)
            self.clean_fly()
            beat.wait_until("flips", 2, offset=-0.3)
            self.play(self.fly_into(dens, fa_den, lag=0.03), FadeIn(fa_bar), run_time=0.6)
            self.clean_fly()
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
        with self.beat("votes") as beat:
            mean_num.clear_updaters()            # the line has stopped moving: the label rests
            beat.wait_until("row by row", offset=-0.3)
            srcs = [t[1] for row in rows_b for t in row]
            # the tiles drop past the two labels between the strips, which step back meanwhile
            self.play(LaggedStart(*[TransformFromCopy(s_, t_) for s_, t_ in zip(srcs, b_tiles)],
                                  lag_ratio=0.03),
                      mean_num.animate(rate_func=early(0.3)).set_opacity(0.25),
                      guess_lbl.animate(rate_func=early(0.3)).set_opacity(0.25),
                      run_time=beat.until("one vote", offset=-0.15))
            self.play(Transform(b_tiles, b_vote_targets), Create(vote_boxes),
                      run_time=beat.until("however", offset=-0.1))
            self.play(LaggedStart(*[pulse(d, 1.3) for d in denoms], lag_ratio=0.06),
                      mean_num.animate.set_opacity(1.0), guess_lbl.animate.set_opacity(1.0),
                      run_time=beat.remaining(1.0))

        # crowds: HHHH's three heads share one vote; HTTT's lone tails keeps a whole one
        kA, kB = SEQS.index("HHHH"), SEQS.index("HTTT")
        rA, rB = SCORED.index(kA), SCORED.index(kB)
        cA = cards[kA]
        chain = VGroup(*[CurvedArrow(cA["coins"][i].get_top() + UP * 0.07,
                                     cA["coins"][i + 1].get_top() + UP * 0.07, angle=-PI / 2,
                                     color=BLUE, stroke_width=3, tip_length=0.12)
                         for i in range(3)])
        boxA = box(VGroup(cA["coins"], cA["score"], chain), color=INK, buff=0.06)
        boxB = box(VGroup(cards[kB]["coins"], cards[kB]["score"]), color=INK, buff=0.1)
        segA = vote_boxes[rA].copy().set_stroke(INK, 5)
        segB = vote_boxes[rB].copy().set_stroke(INK, 5)
        with self.beat("crowds") as beat:
            beat.wait_until("crowds", offset=-0.3)
            crowd_rows = [r_i for r_i, row in enumerate(rows_b)
                          if sum(1 for t in row if t[0] == "H") >= 2]
            crowd_tiles = [b_tiles[sum(len(rows_b[q]) for q in range(r_i)) + j]
                           for r_i in crowd_rows for j, t in enumerate(rows_b[r_i])
                           if t[0] == "H"]
            self.play(LaggedStart(*[pulse(t, 1.2) for t in crowd_tiles], lag_ratio=0.08),
                      run_time=1.0)
            beat.wait_until("since", offset=-0.1)
            self.play(LaggedStart(*[Create(a) for a in chain], lag_ratio=0.6),
                      run_time=beat.until("Here", offset=-0.2))
            self.play(Create(boxA), Create(segA), run_time=0.8)
            beat.wait_until("single", offset=-0.1)
            self.play(pulse(VGroup(*[b_tiles[j] for j in range(3)]), 1.15), run_time=0.8)
            beat.wait_until("lone", offset=-0.35)
            self.play(FadeOut(boxA), FadeOut(segA), FadeOut(chain),
                      Create(boxB), Create(segB), run_time=0.8)
            beat.wait_until("whole", offset=-0.1)
            idxB = sum(len(rows_b[q]) for q in range(rB))
            self.play(pulse(b_tiles[idxB], 1.15), run_time=0.8)
            self.play(FadeOut(boxB), FadeOut(segB), run_time=beat.remaining(0.5))

        # lineup: where the heads and the tails live; then pack the votes and count them
        h_rows = [k for k in SCORED if INFO[SEQS[k]]["h"] > 0]
        t_rows = [k for k in SCORED if INFO[SEQS[k]]["n"] - INFO[SEQS[k]]["h"] > 0]
        assert len(h_rows) == 8 and len(t_rows) == 11
        no_h = [k for k in SCORED if k not in h_rows]        # 6 rows: no checked heads
        no_t = [k for k in SCORED if k not in t_rows]        # 3 rows: no checked tails
        rowg = {k: VGroup(cards[k]["coins"], cards[k]["rings"], cards[k]["score"])
                for k in SCORED}
        h_boxes = VGroup(*[box(cards[k]["coins"], color=YELLOW, buff=0.12, stroke_width=4.5)
                           for k in h_rows])
        t_boxes = VGroup(*[box(cards[k]["coins"], color=INK, buff=0.12, stroke_width=3)
                           for k in t_rows])
        flat = [t for row in rows_b for t in row]
        widths = [W / 14 / len(row) for row in rows_b for _ in row]
        order = [i for i, t in enumerate(flat) if t[0] == "H"] + \
                [i for i, t in enumerate(flat) if t[0] == "T"]
        x = X0
        sorted_targets = [None] * len(flat)
        for i in order:
            sorted_targets[i] = tile(flat[i][0], widths[i] - 0.05, x + widths[i] / 2, SB_Y)
            x += widths[i]
        cnt_h = text("12 heads · 8 rows", size=26, color=YELLOW)
        cnt_h.move_to([RC_X + cnt_h.width / 2, CNT_Y1, 0])
        cnt_t = text("12 tails · 11 rows", size=26, color=TGRAY)
        cnt_t.move_to([RC_X + cnt_t.width / 2, CNT_Y2, 0])
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
        for k in SCORED:
            rowg[k].save_state()
        a_tiles.save_state()
        with self.beat("lineup") as beat:
            # "Twelve heads crowd into eight rows": those rows; everything else steps back
            beat.wait_until("Twelve", offset=-0.1)
            self.play(LaggedStart(*[Create(b) for b in h_boxes], lag_ratio=0.1),
                      FadeIn(cnt_h, shift=0.1 * LEFT, rate_func=delayed(0.5)),
                      *[rowg[k].animate.fade(0.7) for k in no_h],
                      a_tiles.animate.fade(0.7), fa.animate.set_opacity(0.3),
                      guess_lbl.animate.set_opacity(0.3), run_time=1.0)
            # "Twelve tails spread across eleven": swap which rows step back
            beat.wait_until("Twelve", 2, offset=-0.3)
            self.play(FadeOut(h_boxes), *[Restore(rowg[k]) for k in no_h],
                      *[rowg[k].animate.fade(0.7) for k in no_t], run_time=0.5)
            self.play(LaggedStart(*[Create(b) for b in t_boxes], lag_ratio=0.08),
                      FadeIn(cnt_t, shift=0.1 * LEFT, rate_func=delayed(0.5)), run_time=1.0)

        crowded = (kA, k1)                                   # HHHH, HHHT: thirds of a vote
        with self.beat("split") as beat:
            # only the two crowded rows stay bright: their heads are the thinnest slices
            self.play(FadeOut(t_boxes), FadeOut(cnt_t, rate_func=early(0.6)),
                      FadeOut(cnt_h, rate_func=early(0.6)),
                      *[Restore(rowg[k]) for k in no_t if k in crowded],
                      *[rowg[k].animate.fade(0.7) for k in SCORED
                        if k not in crowded and k not in no_t],
                      run_time=0.6)
            # "Crowded heads split their votes": HHHH's and HHHT's heads, a third of a vote each
            beat.wait_until("split", offset=-0.15)
            self.play(LaggedStart(*[pulse(t_, 1.3) for t_ in thin], lag_ratio=0.08),
                      pulse(cards[kA]["score"], 1.2), pulse(cards[k1]["score"], 1.2),
                      run_time=0.9)

        with self.beat("pack") as beat:
            # "Line them up": the whole table steps back; the votes pack, heads first.
            # The 14 vote outlines stay, so the heads' part can be counted in votes.
            self.play(FadeOut(guess_lbl), FadeOut(fa),
                      *[rowg[k].animate.fade(0.7) for k in crowded],
                      *[VGroup(cards[k]["coins"], cards[k]["score"]).animate.fade(0.7)
                        for k in UNDEF],
                      *[Transform(b_tiles[i], sorted_targets[i]) for i in range(len(flat))],
                      run_time=beat.until("five", offset=-0.2))
            # "five and two thirds": counted on the strip, then carried into a numerator
            # (routed above the strip and clear of the grey count still to come)
            # the packed heads stop on the 40.5% marker; its label hands over to the vote count
            self.play(FadeOut(mean_num, rate_func=early(0.45)),
                      FadeIn(vh_lbl, shift=0.1 * DOWN, rate_func=delayed(0.4)), run_time=0.7)
            self.play(emerge(vh_lbl[0], f_num, run_time=0.9,
                             path=via((0.0, -0.05, 0), (4.0, -0.15, 0))))
            # "of the fourteen votes": the tails' 8 1/3, and the 14 outlines become the 14
            beat.wait_until("fourteen", offset=-0.15)
            self.play(FadeIn(vt_lbl, shift=0.1 * DOWN),
                      self.fly_into(list(vote_boxes), f_den, lag=0.02),
                      FadeIn(f_bar, rate_func=delayed(0.4)), run_time=0.9)
            self.clean_fly()
            self.adopt(frac57)
            # "That's seventeen out of forty two": 5 2/3 over 14 is 17/42
            beat.wait_until("seventeen", offset=-0.4)
            self.play(carry(frac57, fb[4], run_time=0.9),
                      FadeIn(fb[3], rate_func=delayed(0.6)), run_time=0.9)

        with self.beat("formula") as beat:
            # the worked case steps aside for the general form (no "=" while a side is open)
            self.play(FadeOut(frac57), FadeOut(fb[3]), FadeOut(vh_lbl), FadeOut(vt_lbl),
                      run_time=0.5)
            # "an average": the 14 equal vote outlines become the 1/14 and the sum
            beat.wait_until("average", offset=-0.3)
            self.play(LaggedStart(*[o.animate(rate_func=there_and_back).set_stroke(width=4.5)
                                    for o in vote_boxes], lag_ratio=0.04), run_time=0.5)
            self.play(self.fly_into(list(vote_boxes), fb[0], lag=0.02), FadeOut(vote_boxes),
                      FadeIn(fb[1], rate_func=delayed(0.4)), run_time=0.7)
            self.clean_fly()
            # "of ratios": one row's own ratio (HHHH's 3/3), at table size, becomes h_i / n_i
            self.play(carry(cards[kA]["score"], fb[2], run_time=beat.until("one", offset=-0.1)))
            # "one per row": every row's ratio answers in the table; the "=" joins 17/42
            self.play(FadeIn(fb[3]), pulse(fb[4], 1.12),
                      LaggedStart(*[cards[k]["score"].animate(rate_func=there_and_back)
                                    .set_opacity(1.0) for k in SCORED], lag_ratio=0.04),
                      run_time=0.9)
            self.adopt(fb)
            # "instead of the ratio of totals": the pooled strip and its formula return; the one
            # structural difference is the sum outside the ratio (below) or inside it (above)
            beat.wait_until("instead", offset=-0.15)
            fa.set_opacity(1.0)
            self.play(pulse(VGroup(fb[0], fb[1]), 1.18), FadeIn(fa), Restore(a_tiles),
                      run_time=0.7)
            beat.wait_until("ratio", 2, offset=-0.1)
            self.play(pulse(fa[0][0], 1.35), pulse(fa[0][5], 1.35), run_time=0.8)
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
        lab_H = text("after heads", size=26)
        lab_H.move_to([RC_X + lab_H.width / 2, SA2 + 0.25, 0])
        lab_T = text("after tails", size=26)
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
            # "Swap heads and tails": recolour in place
            beat.wait_until("Swap", offset=-0.1)
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
            beat.wait_until("twenty", offset=-0.15)
            self.play(self.fly_into([block(X0, X0 + W * MEAN_T - 0.05, SB2)], val_T),
                      run_time=0.9)
            self.clean_fly()

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
        # header in grey: the 1985 study's design (the random shooter below is run on that
        # design). It becomes the purple "Cornell, 1985" only when Cornell's own data arrives.
        header = VGroup(text("1985 design", size=30, color=TGRAY),
                        text("· 26 players", size=30, color=TGRAY),
                        text("· up to 100 shots", size=30, color=TGRAY))
        header.arrange(RIGHT, buff=0.2).move_to([0, 3.3, 0])
        h_final = [m_.get_center() for m_ in header]
        _g2 = VGroup(header[0].copy(), header[1].copy()).arrange(RIGHT, buff=0.2)
        _g2.move_to([0, 3.3, 0])
        h_two = [m_.get_center() for m_ in _g2]
        header[0].move_to([0, 3.3, 0])
        header[1].move_to(h_two[1])
        title_C = text("Cornell, 1985", size=30, color=PURPLE).move_to([0, 3.3, 0])
        tracks = VGroup(*[Line([vx(0), y, 0], [vx(1), y, 0], color=DIM, stroke_width=3)
                          for y in (SA2, SB2)])
        gap_live = always_redraw(
            lambda: h_arrow(xs(sT.get_value()), xs(sH.get_value()), LBL2, color=RED, width=5)
            if abs(xs(sT.get_value()) - xs(sH.get_value())) > 0.12 else VMobject())
        t_hits2 = self.axis_title("checked shots that are hits").shift(UP * DY)
        q_H, q_T = value_tex("?"), value_tex("?")
        q_H.move_to(val_H, aligned_edge=LEFT)
        q_T.move_to(val_T, aligned_edge=LEFT)
        lab_H3 = text("after 3 hits", size=26).move_to(lab_H, aligned_edge=LEFT)
        lab_T3 = text("after 3 misses", size=26).move_to(lab_T, aligned_edge=LEFT)
        # each lane's condition, drawn at its left end: three hits (yellow dots) / three misses
        # (hollow grey dots), the same glyphs the streak-length ticks carry later
        g_hits = hit_glyph(3).move_to([X0 + 0.45, SA2 + 0.27, 0])
        g_miss = VGroup(*[Circle(radius=0.065, stroke_color=GRAY, stroke_width=2.5)
                          for _ in range(3)]).arrange(RIGHT, buff=0.07)
        g_miss.move_to([X0 + 0.45, SB2 + 0.27, 0])
        # the one-half line keeps its meaning from the cold open: what the 1985 test assumed a
        # random shooter reads (both cursors sit on it until the crowding pulls them apart)
        obv = text("the obvious guess", size=26).move_to([C, CUR_TOP + 0.38, 0])
        with self.beat("cornell") as beat:
            # "The nineteen eighty five study": the coin strips clear to two thin lanes first;
            # the study's design header (grey) and its citation come in behind them
            beat.wait_until("nineteen", offset=-0.2)
            self.remove(gap19)
            self.add(gap_live)
            self.play(FadeOut(b_tiles, rate_func=early(0.5)), FadeOut(lane_T, rate_func=early(0.5)),
                      FadeIn(tracks), FadeOut(lbl19, rate_func=early(0.5)),
                      sH.animate.set_value(0.5), sT.animate.set_value(0.5),
                      hand_off(val_H, q_H), hand_off(val_T, q_T),
                      FadeIn(header[0], shift=0.15 * DOWN, rate_func=delayed(0.5)),
                      FadeIn(cite_gvt, rate_func=delayed(0.5)), run_time=1.2)
            # "the same comparison", now on shots: lanes and axis title in basketball terms
            beat.wait_until("same", offset=-0.1)
            anims, tok = self.retitle(self.axis[3], t_hits2)
            self.play(hand_off(lab_H, lab_H3), hand_off(lab_T, lab_T3),
                      FadeIn(g_hits, shift=0.1 * RIGHT, rate_func=delayed(0.4)),
                      FadeIn(g_miss, shift=0.1 * RIGHT, rate_func=delayed(0.4)),
                      *anims, run_time=0.8)
            self.retitle_done(tok)
            beat.wait_until("twenty six", offset=-0.1)
            self.play(header[0].animate.move_to(h_two[0]), FadeIn(header[1], shift=0.15 * DOWN),
                      run_time=0.7)
            beat.wait_until("hundred", offset=-0.1)
            self.play(header[0].animate.move_to(h_final[0]), header[1].animate.move_to(h_final[1]),
                      FadeIn(header[2], shift=0.15 * DOWN, rate_func=delayed(0.5)), run_time=0.9)
            self.adopt(header)
            # "from where they'd hit about half": the one-half line and its tick
            beat.wait_until("half", offset=-0.2)
            self.play(pulse(dashed, 1.05), pulse(self.axis[2][2], 1.25),
                      FadeIn(obv, shift=0.1 * DOWN), run_time=0.8)
            # "After three hits, versus after three misses": each lane gets its condition
            beat.wait_until("After", offset=-0.1)
            self.play(pulse(g_hits, 1.35), pulse(lab_H3, 1.1, edge=LEFT), run_time=0.8)
            beat.wait_until("after", 2, offset=-0.1)
            self.play(pulse(g_miss, 1.35), pulse(lab_T3, 1.1, edge=LEFT),
                      header[1:].animate.set_opacity(0.3), run_time=0.8)

        v46, v54 = value_tex(r"46\%"), value_tex(r"54\%")
        v46.move_to(q_H, aligned_edge=LEFT)
        v54.move_to(q_T, aligned_edge=LEFT)
        cite_ms = citation("Miller & Sanjurjo, 2018 · Econometrica", color=TGRAY)
        cite_ms.shift(UP * (cite_gvt.height + 0.2))
        tick_marks, share_nums, ztitle = self.axis[1], self.axis[2], self.axis[3]
        # the difference axis reuses the share axis's tick marks (PT units per point puts
        # -10, -5, 0, +5, +10 exactly on 0, 25, 50, 75, 100 %); only the labels change
        gnums = VGroup(*[MathTex(t, font_size=30, color=TGRAY).move_to(n_)
                         for t, n_ in zip(["-10", "-5", "0", "+5", "+10"], share_nums)])
        assert all(abs(tick_marks[j].get_center()[0] - gx(v)) < 1e-6
                   for j, v in enumerate((-10, -5, 0, 5, 10)))
        gtitle = MathTex(r"\text{after-hits} - \text{after-misses (points)}", font_size=30,
                         color=TGRAY)
        gtitle.move_to([vx(1) + 0.2 - gtitle.width / 2, AX2 - 0.82, 0])
        marker8 = Line([gx(-8), AX2, 0], [gx(-8), G_TOP, 0], color=BLUE, stroke_width=5)
        dashed_g = DashedLine([C, AX2, 0], [C, G_TOP, 0], color=INK, stroke_width=3,
                              dash_length=0.12)
        bias_arrow = h_arrow(C - 0.03, gx(-8) + 0.03, G_ARR, color=RED, width=5)
        bias_lbl = text("bias", size=28, color=RED).move_to([(C + gx(-8)) / 2, G_ARR + 0.36, 0])
        rnd_lbl = VGroup(text("random", size=26, color=BLUE), text("shooter", size=26, color=BLUE))
        rnd_lbl.arrange(DOWN, buff=0.1, aligned_edge=RIGHT)
        rnd_lbl.move_to([gx(-8) - 0.2 - rnd_lbl.width / 2, G_ARR + 0.8, 0])
        m8 = MathTex("-8", font_size=40, color=BLUE)
        m8.move_to([gx(-8) - 0.2 - m8.width / 2, G_ARR, 0])
        # right column: its head says whose numbers these are (not colour alone)
        head_R = text("random", size=26, color=BLUE)
        head_R.move_to([RC_X + head_R.width / 2, SA2 + 0.74, 0])
        right_col = VGroup(head_R, lab_H3, lab_T3, v46, v54)
        # streak length: three ghost ticks (1, 2, 3 hits in a row) slide out of zero; each
        # carries its own flag of yellow hit dots, and the 3-hit one lands exactly under -8
        GH = 0.45
        ghosts = VGroup(*[Line([gx(0), AX2, 0], [gx(0), AX2 + GH, 0], color=BLUE,
                               stroke_width=5, stroke_opacity=0.0) for _ in (1, 2, 3)])
        ghosts.set_z_index(-1)                       # behind the -8 marker it lands under
        glyphs = VGroup(*[hit_glyph(k) for k in (1, 2, 3)])
        gops = [ValueTracker(0.0) for _ in (1, 2, 3)]
        for g_, t_, o_ in zip(glyphs, ghosts, gops):
            flag_to(g_, t_).set_opacity(0)
            g_.add_updater(lambda mob, t_=t_, o_=o_: flag_to(mob, t_).set_opacity(o_.get_value()))
        x100 = {1: gx(STREAK_100[1]), 2: gx(STREAK_100[2]), 3: gx(-8)}   # -7.94 is drawn as -8
        x1000 = {k: gx(STREAK_1000[k]) for k in (1, 2, 3)}
        legend = text("hits in a row", size=24, color=TGRAY)
        _fl2 = hit_glyph(2)
        _fl2.move_to([x100[2] - 0.09 - _fl2.width / 2, AX2 + GH - 0.075, 0])
        legend.move_to([_fl2.get_center()[0], AX2 + GH + 0.2 + legend.height / 2, 0])
        _fl3 = hit_glyph(3)
        long_lbl = text("1,000 shots", size=26, color=BLUE)
        long_lbl.move_to([x1000[3] - 0.09 - _fl3.width - 0.18 - long_lbl.width / 2,
                          AX2 + GH - 0.075, 0])
        with self.beat("minus8") as beat:
            # "For a random shooter": the column is labelled before any number lands in it
            beat.wait_until("random", offset=-0.2)
            self.play(FadeIn(head_R, shift=0.1 * DOWN), run_time=0.6)
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
            # "the gap": measure after-hits from after-misses (slide the pair until after-misses
            # sits on the one-half line), then read the same marks as the gap in points
            beat.wait_until("gap", offset=-0.35)
            self.play(sH.animate.set_value(0.42), sT.animate.set_value(0.50),
                      FadeOut(tracks), FadeOut(g_hits), FadeOut(g_miss), run_time=0.9)
            gap_live.clear_updaters()
            cur_H.clear_updaters()
            cur_T.clear_updaters()
            ga = h_arrow(xs(sT.get_value()), xs(sH.get_value()), LBL2, color=RED, width=5)
            self.remove(gap_live)
            self.add(ga)
            # the lanes are gone: the right column dims until Cornell's numbers join it
            self.play(Transform(cur_H, marker8), Transform(ga, bias_arrow), FadeOut(cur_T),
                      Transform(dashed, dashed_g),
                      *[hand_off(share_nums[j], gnums[j]) for j in range(5)],
                      hand_off(ztitle, gtitle),
                      FadeIn(m8), FadeIn(rnd_lbl), FadeIn(bias_lbl, shift=0.1 * UP),
                      obv.animate.move_to([C, G_TOP + 0.38, 0]),
                      right_col.animate.set_opacity(0.3),
                      run_time=0.9)
            # "Longer streaks grow the bias": 1, 2 and 3 hits in a row slide out of zero
            beat.wait_until("Longer", offset=-0.15)
            self.add(ghosts, glyphs)
            self.play(*[ghosts[k - 1].animate.move_to([x100[k], AX2 + GH / 2, 0])
                        .set_stroke(opacity=0.6) for k in (1, 2, 3)],
                      *[o_.animate.set_value(1.0) for o_ in gops],
                      FadeIn(legend, rate_func=delayed(0.4)),
                      run_time=1.1)
            # hold the 100-shot picture (and its legend) until "Longer records"
            beat.wait_until("Longer", 2, offset=-0.2)
            # "Longer records shrink it": with 1,000 shots the 3-hit tick (GVT's case) slides
            # almost to zero, carrying its flag; the other two step aside
            self.play(ghosts[0].animate.set_stroke(opacity=0), ghosts[1].animate.set_stroke(opacity=0),
                      gops[0].animate.set_value(0), gops[1].animate.set_value(0),
                      FadeOut(legend, rate_func=lambda t: smooth(min(1.0, 2.5 * t))),
                      ghosts[2].animate.move_to([x1000[3], AX2 + GH / 2, 0]),
                      FadeIn(long_lbl, rate_func=delayed(0.55)),
                      run_time=1.2)
            self.remove(ghosts[0], ghosts[1])
            # "but a hundred shots isn't long": back under -8
            beat.wait_until("isn't", offset=-0.1)
            self.play(ghosts[2].animate.move_to([x100[3], AX2 + GH / 2, 0]),
                      FadeOut(long_lbl, rate_func=lambda t: smooth(min(1.0, 6 * t))),
                      header[2].animate(rate_func=there_and_back).set_opacity(1.0),
                      run_time=beat.remaining(0.8))

        # ================================================================ 9 observed
        # Cornell's numbers take the random shooter's slots in the right column (its head
        # changes from "random" to "Cornell"); then 49 - 45 is written next to its marker
        head_C = text("Cornell", size=26, color=PURPLE).move_to(head_R, aligned_edge=LEFT)
        p49 = MathTex(r"49\%", font_size=36, color=PURPLE).move_to(v46, aligned_edge=LEFT)
        p45 = MathTex(r"45\%", font_size=36, color=PURPLE).move_to(v54, aligned_edge=LEFT)
        marker4 = Line([gx(4), AX2, 0], [gx(4), G_TOP, 0], color=PURPLE, stroke_width=5)
        eq4 = MathTex("49", "-", "45", "=", "+4", font_size=40, color=PURPLE)
        eq4.move_to([gx(4) + 0.2 + eq4.width / 2, G_ARR, 0])
        p4 = MathTex("+4", font_size=40, color=PURPLE)
        p4.move_to([gx(4) + SH2 + 0.2 + p4.width / 2, G_ARR, 0])     # once the chart re-centres
        with self.beat("observed") as beat:
            # the 3-hit ghost leaves (it sits under -8); Cornell's data arrives: purple title,
            # GVT's citation back to full, the column's head becomes "Cornell"
            self.play(ghosts[2].animate.set_stroke(opacity=0), gops[2].animate.set_value(0),
                      FadeOut(header[1:]), hand_off(header[0], title_C),
                      lab_H3.animate.set_opacity(1.0), lab_T3.animate.set_opacity(1.0),
                      hand_off(head_R, head_C),
                      cite_gvt.animate.set_opacity(1.0), cite_ms.animate.set_opacity(0.3),
                      run_time=0.8)
            for g_ in glyphs:
                g_.clear_updaters()
            self.remove(ghosts[2], glyphs)
            beat.wait_until("forty nine", offset=-0.2)
            self.play(hand_off(v46, p49), run_time=0.6)
            beat.wait_until("forty five", offset=-0.2)
            self.play(hand_off(v54, p45), run_time=0.6)
            # "...after three misses. The study took that": 49 and 45 travel, whole, to the
            # right of where Cornell's marker will stand, and the subtraction is written there
            beat.wait_until("misses", offset=0.05)
            self.play(emerge(p49[0][0:2], eq4[0], run_time=1.0),
                      emerge(p45[0][0:2], eq4[2], run_time=1.0, arc=-0.5),
                      FadeIn(eq4[1], rate_func=delayed(0.6)), run_time=1.0)
            # "plus four": the difference, and Cornell's marker grows up from the axis
            beat.wait_until("plus", offset=-0.15)
            self.play(Create(marker4), FadeIn(eq4[3]), FadeIn(eq4[4], shift=0.1 * RIGHT),
                      run_time=0.8)
            self.adopt(eq4)
            # "no hot hand": GVT measured +4 from the obvious guess, zero
            beat.wait_until("no hot", offset=-0.2)
            self.play(pulse(dashed, 1.06), pulse(obv, 1.12), run_time=0.9)

        brace = BraceBetweenPoints([gx(-8) + SH2, G_TOP + 0.22, 0], [gx(4) + SH2, G_TOP + 0.22, 0],
                                   direction=UP, color=PURPLE)
        brace_lbl = MathTex(r"+12\text{ points}", font_size=40, color=PURPLE)
        brace_lbl.next_to(brace, UP, buff=0.2)
        gym = text("no defenders", size=26, color=TGRAY, slant=ITALIC)
        gym.next_to(p4, DOWN, buff=0.25, aligned_edge=LEFT)
        chart = VGroup(self.axis[0], tick_marks, gnums, gtitle, dashed, cur_H, ga, m8, rnd_lbl,
                       bias_lbl, marker4)
        # the +4 marker's tag, mirroring "random shooter" at -8: the column head travels there
        tag_C = text("Cornell", size=26, color=PURPLE)
        tag_C.move_to([gx(4) + SH2 + 0.2 + tag_C.width / 2, rnd_lbl.get_center()[1], 0])
        with self.beat("hot") as beat:
            # "Measured from minus eight": the right column has done its job; the chart takes
            # the frame, centred under its title, and +4 sheds its working
            self.play(FadeOut(VGroup(lab_H3, lab_T3, p49, p45), rate_func=early(0.5)),
                      head_C.animate.move_to(tag_C.get_center()),
                      FadeOut(obv, shift=RIGHT * SH2, rate_func=early(0.5)),
                      chart.animate.shift(RIGHT * SH2),
                      FadeOut(eq4[0:4], shift=RIGHT * SH2, rate_func=early(0.5)),
                      ReplacementTransform(eq4[4], p4),
                      cite_ms.animate.set_opacity(1.0), run_time=0.9)
            self.play(GrowFromCenter(brace), run_time=beat.until("twelve", offset=-0.35))
            self.play(FadeIn(brace_lbl, shift=0.15 * DOWN), run_time=0.6)
            beat.wait_until("gym", offset=-0.25)
            self.play(FadeIn(gym, shift=0.1 * UP), run_time=0.7)
            beat.wait_until("defenders", offset=-0.2)
            self.play(pulse(gym, 1.1), pulse(VGroup(marker4, p4), 1.04), run_time=0.9)

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
            self.allow_overlap(g_, reason="ghost miniature of the 16-row table (60% opacity): "
                                          "each letter sits inside its own small coin")
        # the shooter's average sits on the formula's line, on the one-half line
        DOT_Y = LBL_Y + 0.05
        shooter = Dot([vx(0.5), DOT_Y, 0], radius=0.15, color=BLUE)
        hot3 = Arrow([vx(MEAN) + 0.06, DOT_Y, 0], [vx(0.5) - 0.17, DOT_Y, 0], buff=0, color=BLUE,
                     stroke_width=8, max_tip_length_to_length_ratio=0.4, tip_length=0.24)
        hot3_lbl = text("hot", size=38, color=BLUE).next_to(shooter, RIGHT, buff=0.22)
        # what the dot is: this shooter's test score, an average over its rows (not one row)
        avg_tag = MathTex(r"\text{its rows average }1/2", font_size=36, color=TGRAY)
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
        self.play(*[FadeOut(o_) for o_ in outs], run_time=0.5)
        self.play(ReplacementTransform(old_line, self.axis[0]),
                  *[ReplacementTransform(tick_marks[j], self.axis[1][j]) for j in range(5)],
                  *[FadeOut(gnums[j], rate_func=lambda t: smooth(min(1.0, 2.2 * t)))
                    for j in range(5)],
                  *[FadeIn(self.axis[2][j], rate_func=delayed(0.5)) for j in range(5)],
                  ReplacementTransform(old_dashed, dashed2),
                  *[FadeIn(m_, rate_func=delayed(0.35)) for m_ in
                    (self.axis[3], guess2, big2, rings2, arcs2, score2)],
                  run_time=1.0)
        self.adopt(self.axis)
        with self.beat("landing") as beat:
            beat.wait_until("One half", offset=-0.2)
            self.play(pulse(dashed2, 1.06), pulse(guess2, edge=LEFT), run_time=0.9)
            # "a fair coin does": the cold open's sixteen runs return, in the cold open's place
            # and size, while the row steps back (as it did then)
            beat.wait_until("fair", offset=-0.1)
            row2 = VGroup(big2, rings2, arcs2, score2)
            row2.save_state()
            self.play(LaggedStart(*[FadeIn(g, shift=0.06 * DOWN) for g in mini2], lag_ratio=0.05),
                      row2.animate.fade(0.6), FadeOut(guess2),
                      dashed2.animate.set_stroke(opacity=0.15), run_time=0.9)
            # "Seventeen out of forty two": they average into the test's formula, which lands
            # on its marker at 17/42
            beat.wait_until("Seventeen", offset=-0.15)
            scored_rows = [mini2[k] for k in SCORED]
            fly = self.fly_into(scored_rows, VGroup(fl[0], fl[1], fl[2]), lag=0.02)
            self.remove(*scored_rows)             # the rows themselves fly (their copies)
            self.play(fly, *[FadeOut(mini2[k]) for k in UNDEF], Restore(row2),
                      dashed2.animate.set_stroke(opacity=1.0),
                      Create(blue2, rate_func=delayed(0.3)), run_time=0.9)
            self.clean_fly()
            self.remove(*mini2)
            self.play(FadeIn(fl[3]), self.fly_into([blue2], fl[4]), run_time=0.6)
            self.clean_fly()
            self.adopt(fl)
            beat.wait_until("this test", offset=-0.15)
            self.play(pulse(fl[4], 1.12), pulse(blue2, 1.04), run_time=0.8)
            # "A fifty percent shooter": the row is a shooter again, and the one-half line is
            # that shooter's usual rate
            beat.wait_until("fifty percent", offset=-0.15)
            anims, tok = self.retitle(self.axis[3], t_hits3)
            self.swap_glyphs([c[1] for c in big2], list(words2), *anims, pulse(dashed2, 1.06),
                             run_time=0.9)
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
        self.hold(1.35)
