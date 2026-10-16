"""Sample Space, episode 4: The Hidden Bias That Hid the Hot Hand.

    videos/toolkit/render.sh --preview videos/episodes/004-hot-hand-bias/scene.py Episode /tmp/ep4.mp4
    videos/toolkit/render.sh videos/episodes/004-hot-hand-bias/scene.py Episode \
        videos/episodes/004-hot-hand-bias/final.mp4

Palette (one meaning each, see script.md):
    YELLOW  heads / a hit            GRAY  tails / a miss (and axes)
    BLUE    the streak test: checked flips, row scores, n_i, what it reads for a random shooter
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
from narration_text import BEATS, GAPS, PRONUNCIATIONS  # noqa: E402

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

# ----------------------------------------------------------------------------- layout
COIN_R, COIN_STEP = 0.185, 0.49           # table coins (rings clear the neighbours)
RING_R = COIN_R + 0.05
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
SA_Y, SB_Y, TILE_H = 0.2, -1.0, 0.4       # top strip (pooled), bottom strip (votes)
FORM_X = 3.45                             # right column
RC_X = 3.45
C = X0 + (X1 - X0) * 0.5                  # x of one half once the axis has moved left
W = X1 - X0

# mirror + payoff: once the table is gone the whole picture rises (DY) and the lanes open up
DY = 1.0
AX2 = AX_Y + DY                           # the share / gap axis
SA2, SB2 = 1.4, 0.0                       # lanes: after heads (hits), after tails (misses)
LBL2 = 0.7                                # between the lanes: cursor ends, the -19 arrow
CUR_TOP, CUR_BOT = SA2 + 0.32, SB2 - 0.32
PT = 0.40                                 # payoff: units per percentage point
G_TOP, G_ARR = AX2 + 2.2, AX2 + 1.1       # gap axis: marker tops, bias arrow


def vx(v: float) -> float:
    return X0 + OFF.get_value() + (X1 - X0) * v


def gx(points: float) -> float:
    return C + PT * points


def delayed(start: float):
    """smooth, but only from `start` (fraction of the animation) on."""
    return lambda t: smooth(min(1.0, max(0.0, (t - start) / (1.0 - start))))


# ----------------------------------------------------------------------------- pieces
def make_coin(face: str, r: float = COIN_R) -> VGroup:
    heads = face == "H"
    col = YELLOW if heads else GRAY
    disk = Circle(radius=r, stroke_color=col, stroke_width=4 if r > 0.3 else 3,
                  fill_color=col, fill_opacity=0.18 if heads else 0.0)
    let = Text(face, font=SERIF, font_size=46 * r / 0.5, color=col, weight=BOLD).move_to(disk)
    return VGroup(disk, let)


def ring(c: Mobject, r: float, width: float = 3.5) -> Circle:
    return Circle(radius=r, color=BLUE, stroke_width=width).move_to(c)


def score_tex(h, n, size: float = 36) -> MathTex:
    m = MathTex(str(h), "/", str(n), font_size=size)
    m[0].set_color(YELLOW)
    m[1].set_color(GRAY)
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
    nums = VGroup(*[MathTex(t, font_size=30, color=GRAY).move_to([x_of(v), y - 0.36, 0])
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
    SPEED = 0.81
    PRONUNCIATIONS = PRONUNCIATIONS

    # ========================================================================= build
    def adopt(self, *groups):
        """Pieces animated in one by one live at top level; hand them back to their group so
        later transforms/dims of the group act on exactly what is on screen."""
        for g in groups:
            self.remove(*g.get_family()[1:])
            self.add(g)

    def beat(self, key: str):
        return self.narrate(BEATS[key], gap=GAPS.get(key))

    def fly_into(self, srcs, target, lag: float = 0.02, start: float = 0.4, arc: float = 0.0):
        """Copies of `srcs` fly into `target` and shrink away as it appears there: each copy
        stays a whole glyph or shape in flight (no glyph-by-glyph shatter). Call clean_fly()
        after the play."""
        copies = [s.copy() for s in srcs]
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
        t = Text(s, font=SERIF, font_size=26, color=GRAY, disable_ligatures=True)
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
                anims += [o.animate.shift(UP * 0.12).set_opacity(0),
                          n.animate.shift(UP * 0.12).set_opacity(1)]
                keep.append(n)
        return anims, (holder, keep)

    @staticmethod
    def retitle_done(token):
        holder, keep = token
        holder.submobjects = list(keep)

    def build_mini(self, scale: float = 0.42, at=(0, 0.1, 0), op: float = 0.45,
                   compact: bool = False) -> VGroup:
        """A ghost of all sixteen sequences (the table, in miniature). `compact` packs the rows
        tighter (no room is needed for scores), so the ghost can be drawn larger."""
        rows = []
        for k, cd in enumerate(self.cards):
            g = cd["coins"].copy()
            if compact:
                r, c = divmod(k, 4)
                g.move_to([c * 2.35, -r * 0.56, 0])
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
        mini = self.build_mini(scale=0.66, at=(vx(0.5), 0.02, 0), op=0.6, compact=True)
        for g_ in mini:
            self.allow_overlap(g_, reason="ghost miniature of the 16-row table (60% opacity): "
                                          "each letter sits inside its own small coin")
        qmark = MathTex("?", font_size=64, color=INK).move_to([vx(0.5), AX_Y + 0.75, 0])

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
            self.play(self.fly_into([big[1][1]], big_score[0], arc=PI / 2, start=0.3),
                      run_time=0.7)
            self.clean_fly()
            self.play(self.fly_into(list(big_rings), big_score[2], arc=PI / 2, lag=0.1, start=0.4),
                      FadeIn(big_score[1]), run_time=0.8)
            self.clean_fly()
            self.adopt(big_rings, big_score, arcs)
            # "Do it for all sixteen sequences": the row rises, the share axis draws beneath
            # it, and the ghost of the whole table deals in between
            beat.wait_until("Do", offset=-0.1)
            row = VGroup(big, big_rings, arcs, big_score)
            self.play(row.animate.shift(lift), Create(self.axis[0]), Create(self.axis[1]),
                      run_time=0.8)
            self.play(LaggedStart(*[FadeIn(g, shift=0.08 * DOWN) for g in mini], lag_ratio=0.08),
                      FadeIn(self.axis[2]), FadeIn(self.axis[3]),
                      run_time=beat.until("average", offset=-0.15))
            # "and average the shares": the sixteen rows collapse onto the line, as a "?"
            self.play(mini.animate.scale(0.12).move_to(qmark).set_opacity(0),
                      FadeIn(qmark, scale=0.6, rate_func=delayed(0.3)), run_time=1.0)
            self.remove(mini, *mini)
            self.adopt(self.axis)

        # ================================================================ 2 stakes
        dashed = DashedLine([vx(0.5), AX_Y, 0], [vx(0.5), EARLY_TOP, 0], color=INK,
                            stroke_width=3, dash_length=0.12)
        dashed_full = DashedLine([vx(0.5), AX_Y, 0], [vx(0.5), LINE_TOP, 0], color=INK,
                                 stroke_width=3, dash_length=0.12)
        guess_lbl = text("the obvious guess", size=26).move_to([0, LBL_Y, 0])
        guess_lbl.align_to([vx(0.5) + 0.16, 0, 0], LEFT)
        per_flip = MathTex(r"\text{every flip: }", r"1/2", r"\text{ heads}", font_size=38,
                           color=GRAY).next_to(big, DOWN, buff=0.42)
        quote = text("“a powerful and widely shared cognitive illusion”", size=30,
                     slant=ITALIC).move_to([BIG_C[0] + 0.3, 3.2, 0])
        cite_gvt = citation("Gilovich et al., 1985 · Cognitive Psychology")
        with self.beat("stakes") as beat:
            beat.wait_until("half", offset=-0.25)
            self.play(ReplacementTransform(qmark, dashed), run_time=0.9)
            self.play(FadeIn(guess_lbl, shift=0.1 * RIGHT), run_time=beat.until("since"))
            self.play(FadeIn(per_flip, shift=0.15 * UP), run_time=beat.until("memory"))
            beat.wait_until("nineteen", offset=-0.1)
            self.play(FadeIn(cite_gvt), run_time=0.8)
            beat.wait_until("basketball", offset=-0.2)
            self.play(FadeOut(per_flip), run_time=0.7)
            beat.wait_until("illusion", offset=-0.6)
            self.play(FadeIn(quote, shift=0.15 * DOWN), run_time=1.0)

        # ================================================================ 3 the test
        words = VGroup(*[text("hit" if f == "H" else "miss", size=28,
                              color=YELLOW if f == "H" else GRAY, weight=BOLD).move_to(c)
                         for f, c in zip("HHTH", big)])
        letters = VGroup(*[c[1].copy() for c in big])
        hot = VGroup(h_arrow(vx(0.5) + 0.16, vx(0.5) + 1.5, -1.15), text("hot", size=28))
        hot[1].next_to(hot[0], RIGHT, buff=0.15)
        # the axis title follows the coins: flips/heads <-> shots/hits
        t_heads = self.axis_title("checked flips that are heads")
        t_hits = self.axis_title("checked shots that are hits")
        with self.beat("test") as beat:
            beat.wait_until("Heads", offset=-0.1)
            anims, tok = self.retitle(self.axis[3], t_hits)
            self.play(*[Transform(c[1], w) for c, w in zip(big, words)], *anims, run_time=0.9)
            self.retitle_done(tok)
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
            self.play(*[Transform(c[1], l_) for c, l_ in zip(big, letters)], FadeOut(arcs),
                      *anims, run_time=0.8)
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
            self.play(TransformFromCopy(heads_chk, c1["score"][0]),
                      TransformFromCopy(c1["rings"], c1["score"][2]), FadeIn(c1["score"][1]),
                      run_time=1.0)
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
            self.play(m.animate.set_value(MEAN), run_time=beat.until("about", offset=-0.2),
                      rate_func=smooth)
            self.play(pulse(mean_num, 1.15), run_time=0.9)

        GAP_Y = -0.9
        gap_arrow = h_arrow(vx(0.5) - 0.2, vx(MEAN) + 0.06, GAP_Y, color=RED, width=5)
        cold_w = text("cold", size=28, color=RED)
        cold_n = MathTex(r"-9.5\text{ points}", font_size=36, color=RED)
        cold_lbl = VGroup(cold_w, cold_n).arrange(RIGHT, buff=0.2)
        cold_lbl.move_to([vx(MEAN) - 0.25 - cold_lbl.width / 2, GAP_Y, 0])
        with self.beat("cold") as beat:
            beat.wait_until("perfectly", offset=-0.2)
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
        frac_a = score_tex(12, 24, size=40)
        frac_a.move_to([FORM_X + frac_a.width / 2, SA_Y, 0])
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
            beat.wait_until("Exactly", offset=-0.1)
            self.play(pulse(dashed, 1.06), pulse(guess_lbl, edge=LEFT), run_time=0.9)

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
            beat.wait_until("row by row", offset=-0.3)
            srcs = [t[1] for row in rows_b for t in row]
            self.play(LaggedStart(*[TransformFromCopy(s_, t_) for s_, t_ in zip(srcs, b_tiles)],
                                  lag_ratio=0.03),
                      run_time=beat.until("one vote", offset=-0.15))
            self.play(Transform(b_tiles, b_vote_targets), Create(vote_boxes),
                      run_time=beat.until("however", offset=-0.1))
            self.play(FadeOut(scrim), run_time=0.4)
            self.play(LaggedStart(*[pulse(d, 1.3) for d in denoms], lag_ratio=0.06),
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
                      run_time=beat.until("This", offset=-0.2))
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

        # lineup: where the heads and the tails live; then pack the votes
        h_rows = [k for k in SCORED if INFO[SEQS[k]]["h"] > 0]
        t_rows = [k for k in SCORED if INFO[SEQS[k]]["n"] - INFO[SEQS[k]]["h"] > 0]
        assert len(h_rows) == 8 and len(t_rows) == 11
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
        frac_b = MathTex(r"\frac{17}{42}", font_size=38, color=BLUE)
        frac_b.move_to([FORM_X + frac_b.width / 2, SB_Y, 0])
        with self.beat("lineup") as beat:
            beat.wait_until("Twelve", offset=-0.1)
            self.play(LaggedStart(*[Create(b) for b in h_boxes], lag_ratio=0.1), run_time=1.0)
            beat.wait_until("Twelve", 2, offset=-0.3)
            self.play(FadeOut(h_boxes), run_time=0.4)
            self.play(LaggedStart(*[Create(b) for b in t_boxes], lag_ratio=0.08), run_time=1.0)
            beat.wait_until("Line", offset=-0.2)
            self.play(FadeOut(t_boxes), FadeOut(vote_boxes),
                      *[Transform(b_tiles[i], sorted_targets[i]) for i in range(len(flat))],
                      run_time=beat.until("seventeen", offset=-0.2))
            # the packed heads part, as one block, becomes 17/42
            self.play(self.fly_into([block(X0, X0 + W * MEAN - 0.05, SB_Y)], frac_b),
                      pulse(blue_line, 1.05), run_time=1.0)
            self.clean_fly()

        # formulas, built from the vote outlines, the table's own scores and the strips
        fa = MathTex(r"\frac{\sum_i h_i}{\sum_i n_i}", "=", r"\frac{12}{24}", font_size=38,
                     substrings_to_isolate=[r"\sum_i h_i", r"\sum_i n_i"])
        fb = MathTex(r"\frac{1}{14}", r"\sum_i", r"\frac{h_i}{n_i}", "=", r"\frac{17}{42}",
                     font_size=38)
        fa.move_to([FORM_X + fa.width / 2, SA_Y - 0.1, 0])
        fb.move_to([FORM_X + fb.width / 2, SB_Y - 0.08, 0])
        fa.get_part_by_tex(r"\sum_i h_i").set_color(YELLOW)
        fa.get_part_by_tex(r"\sum_i n_i").set_color(BLUE)
        fa_num, fa_bar, fa_den = fa[0][0:4], fa[0][4], fa[0][5:9]
        fa[2][0:2].set_color(YELLOW)
        fa[2][3:5].set_color(BLUE)
        fa[2][2].set_color(GRAY)
        fb[0].set_color(INK)
        fb[2][0:2].set_color(YELLOW)
        fb[2][3:5].set_color(BLUE)
        fb[4].set_color(BLUE)
        for f_ in (fa, fb):
            f_.set_stroke(width=0)
        nums = [cards[k]["score"][0] for k in SCORED]
        dens = [cards[k]["score"][2] for k in SCORED]
        table = VGroup(*[VGroup(cd["coins"], cd["rings"], cd["score"]) for cd in cards])
        outlines = vote_outlines(width=2.2)
        with self.beat("formula") as beat:
            # "That's one vote per row": every row's own h and n fly in as one numerator and
            # one denominator, then 14 equal vote outlines become the 1/14
            beat.wait_until("That's", offset=-0.15)
            self.play(ReplacementTransform(frac_b, fb[4]),
                      self.fly_into(nums, fb[2][0:2], lag=0.03),
                      self.fly_into(dens, fb[2][3:5], lag=0.03),
                      FadeIn(fb[2][2]), FadeIn(fb[1]), FadeIn(fb[3]),
                      run_time=beat.until("vote", offset=-0.05))
            self.clean_fly()
            self.play(LaggedStart(*[Create(o) for o in outlines], lag_ratio=0.05), run_time=0.5)
            self.play(self.fly_into(list(outlines), fb[0], lag=0.02), FadeOut(outlines),
                      run_time=0.7)
            self.clean_fly()
            self.adopt(fb)
            # "Count all the flips together first": 12/24 restacks digit by digit, then all the
            # numerators sum into one and all the denominators into the other
            beat.wait_until("Count", offset=-0.1)
            fa_frac = fa[2]
            self.play(ReplacementTransform(frac_a[0], fa_frac[0:2]),
                      ReplacementTransform(frac_a[1], fa_frac[2]),
                      ReplacementTransform(frac_a[2], fa_frac[3:5]),
                      LaggedStart(*[pulse(n_, 1.25) for n_ in nums], lag_ratio=0.03),
                      run_time=0.6, rate_func=smooth)
            self.play(self.fly_into(nums, fa_num, lag=0.03), FadeIn(fa[1]), run_time=0.7)
            self.clean_fly()
            self.play(self.fly_into(dens, fa_den, lag=0.03), FadeIn(fa_bar), run_time=0.7)
            self.clean_fly()
            self.adopt(fa)
            beat.wait_until("half", offset=-0.2)
            # the table has done its job: it leaves while "one half" is still sounding
            self.play(pulse(dashed, 1.06), pulse(guess_lbl, edge=LEFT), FadeOut(table),
                      run_time=beat.remaining(0.9))

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
            # "Tails crowd the same way": first the pooled strip and both formulas leave, in
            # place (nothing crosses the vote strip), then the picture rises and the vote strip
            # takes the top lane
            self.play(FadeOut(VGroup(a_tiles, fa, fb), shift=UP * 0.3), FadeOut(guess_lbl),
                      FadeOut(mean_num), run_time=0.5)
            self.play(b_tiles.animate.shift(UP * (SA2 - SB_Y)),
                      self.axis.animate.shift(UP * DY), Transform(dashed, dashed_m),
                      Transform(blue_static, cur_H.copy().clear_updaters()),
                      FadeIn(lab_H, rate_func=delayed(0.6)),
                      run_time=0.8)
            self.remove(blue_static)
            self.add(cur_H)
            # a copy drops into the bottom lane, unchanged
            self.add(lane_T)
            self.play(lane_T.animate.shift(DOWN * (SA2 - SB2)),
                      self.fly_into([block(X0, X0 + W * MEAN - 0.05, SA2)], val_H), run_time=0.8)
            self.clean_fly()
            # "Swap heads and tails": recolour in place
            beat.wait_until("Swap", offset=-0.1)
            self.play(*[Transform(a_, b_) for a_, b_ in zip(lane_T, lane_T_sw)],
                      run_time=beat.until("tails", 2, end=True, offset=0.05))
            # "and the strip flips over one half": a half turn about the dashed line
            beat.wait_until("strip", offset=-0.25)
            self.play(UpdateFromAlphaFunc(lane_T, flip_step, rate_func=linear),
                      dashed.animate(rate_func=there_and_back).set_stroke(width=7),
                      run_time=1.6)
            beat.wait_until("So", offset=-0.1)
            self.play(FadeIn(cur_T), FadeIn(lab_T), run_time=0.6)
            beat.wait_until("hot", offset=-0.2)
            self.play(pulse(lab_T, 1.1), run_time=0.7)
            beat.wait_until("twenty", offset=-0.15)
            self.play(self.fly_into([block(X0, X0 + W * MEAN_T - 0.05, SB2)], val_T),
                      run_time=0.9)
            self.clean_fly()

        gap19 = h_arrow(xs(MEAN_T), xs(MEAN), LBL2, color=RED, width=5)
        lbl19 = MathTex(r"-19\text{ points}", font_size=36, color=RED)
        lbl19.move_to([xs(MEAN_T) + 0.3 + lbl19.width / 2, LBL2, 0])
        with self.beat("gap") as beat:
            beat.wait_until("two averages", offset=-0.15)
            self.play(pulse(val_H, 1.15), pulse(val_T, 1.15), run_time=0.8)
            beat.wait_until("gap", offset=-0.3)
            self.play(GrowArrow(gap19), run_time=0.8)
            beat.wait_until("minus", offset=-0.15)
            self.play(Write(lbl19), run_time=0.8)

        # ================================================================ 8 Cornell
        header = VGroup(text("Cornell, 1985", size=30, color=PURPLE),
                        text("· 26 players", size=30), text("· up to 100 shots", size=30))
        header.arrange(RIGHT, buff=0.2).move_to([0, 3.3, 0])
        tracks = VGroup(*[Line([vx(0), y, 0], [vx(1), y, 0], color=DIM, stroke_width=3)
                          for y in (SA2, SB2)])
        gap_live = always_redraw(
            lambda: h_arrow(xs(sT.get_value()), xs(sH.get_value()), LBL2, color=RED, width=5)
            if abs(xs(sT.get_value()) - xs(sH.get_value())) > 0.3 else VMobject())
        # zoomed share axis: 40 % ... 60 %, then the same marks relabelled as the gap
        zvals = [0.40, 0.45, 0.50, 0.55, 0.60]
        zx = lambda s: C + (s - 0.5) * 100 * PT                                   # noqa: E731
        zticks, znums = pct_ticks(zvals, [r"40\%", r"45\%", r"50\%", r"55\%", r"60\%"], zx,
                                  y=AX2)
        ztitle = Text("next-shot hit rate", font=SERIF, font_size=26, color=GRAY)
        ztitle.move_to([vx(1) + 0.2 - ztitle.width / 2, AX2 - 0.82, 0])
        q_H, q_T = value_tex("?"), value_tex("?")
        q_H.move_to(val_H, aligned_edge=LEFT)
        q_T.move_to(val_T, aligned_edge=LEFT)
        lab_H3 = text("after 3 hits", size=26).move_to(lab_H, aligned_edge=LEFT)
        lab_T3 = text("after 3 misses", size=26).move_to(lab_T, aligned_edge=LEFT)
        old_ticks = VGroup(self.axis[1][0], self.axis[1][1], self.axis[1][3], self.axis[1][4])
        with self.beat("cornell") as beat:
            beat.wait_until("nineteen", offset=-0.2)
            self.play(FadeIn(header[0], shift=0.15 * DOWN), FadeIn(cite_gvt), run_time=0.8)
            beat.wait_until("ran", offset=-0.1)
            self.remove(gap19)
            self.add(gap_live)
            self.play(FadeOut(b_tiles), FadeOut(lane_T), FadeIn(tracks), FadeOut(lbl19),
                      sH.animate.set_value(0.5), sT.animate.set_value(0.5),
                      ReplacementTransform(val_H, q_H), ReplacementTransform(val_T, q_T),
                      run_time=1.0)
            # re-scale the line around one half: old ticks out first, then the new ones
            self.play(FadeOut(self.axis[2]), FadeOut(self.axis[3]), FadeOut(old_ticks),
                      run_time=0.4)
            Z.set_value(100 * PT)
            self.play(FadeIn(zticks), FadeIn(znums), FadeIn(ztitle), run_time=0.5)
            beat.wait_until("twenty six", offset=-0.1)
            self.play(FadeIn(header[1], shift=0.15 * DOWN), run_time=0.7)
            beat.wait_until("hundred", offset=-0.1)
            self.play(FadeIn(header[2], shift=0.15 * DOWN), run_time=0.7)
            self.adopt(header)
            # "from where they'd hit about half": the design puts each shooter at 50 %
            beat.wait_until("about half", offset=-0.2)
            self.play(pulse(dashed, 1.05), pulse(znums[2], 1.25), run_time=0.9)
            beat.wait_until("After three hits", offset=-0.2)
            self.play(ReplacementTransform(lab_H, lab_H3), run_time=0.7)
            beat.wait_until("after three misses", offset=-0.2)
            self.play(ReplacementTransform(lab_T, lab_T3), header[1:].animate.set_opacity(0.3),
                      run_time=0.7)

        v46, v54 = value_tex(r"46\%"), value_tex(r"54\%")
        v46.move_to(q_H, aligned_edge=LEFT)
        v54.move_to(q_T, aligned_edge=LEFT)
        cite_ms = citation("Miller & Sanjurjo, 2018 · Econometrica")
        cite_ms.shift(UP * (cite_gvt.height + 0.2))
        gnums = VGroup(*[MathTex(t, font_size=30, color=GRAY).move_to(n_)
                         for t, n_ in zip(["-10", "-5", "0", "+5", "+10"], znums)])
        gtitle = MathTex(r"\text{after-hits} - \text{after-misses (points)}", font_size=30,
                         color=GRAY)
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
        # right column: column heads say whose numbers these are (not colour alone)
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
        legend = text("hits in a row", size=24, color=GRAY)
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
            # "the same crowding": the cursors slide; this computation is Miller & Sanjurjo's
            beat.wait_until("same crowding", offset=-0.1)
            self.play(sH.animate.set_value(0.46), sT.animate.set_value(0.54),
                      FadeIn(cite_ms, rate_func=lambda t: smooth(min(1.0, 2 * t))),
                      run_time=beat.until("forty six", offset=-0.15), rate_func=smooth)
            self.play(ReplacementTransform(q_H, v46), run_time=0.5)
            beat.wait_until("fifty four", offset=-0.15)
            self.play(ReplacementTransform(q_T, v54), run_time=0.5)
            beat.wait_until("Miller", offset=-0.2)
            self.play(cite_gvt.animate.set_opacity(0.3), pulse(cite_ms, 1.06, edge=LEFT),
                      run_time=0.8)
            beat.wait_until("gap", offset=-0.35)
            # measure the after-hits score from the after-misses score: slide the pair until
            # after-misses sits on the zero line, and read the marks as the gap
            self.play(FadeOut(znums), FadeOut(ztitle), run_time=0.4)
            self.play(sH.animate.set_value(0.42), sT.animate.set_value(0.50),
                      FadeOut(tracks), run_time=1.0)
            gap_live.clear_updaters()
            cur_H.clear_updaters()
            cur_T.clear_updaters()
            ga = h_arrow(xs(sT.get_value()), xs(sH.get_value()), LBL2, color=RED, width=5)
            self.remove(gap_live)
            self.add(ga)
            # the lanes are gone: the right column dims until Cornell's numbers join it
            self.play(Transform(cur_H, marker8), Transform(ga, bias_arrow), FadeOut(cur_T),
                      Transform(dashed, dashed_g),
                      FadeIn(gnums), FadeIn(gtitle),
                      FadeIn(m8), FadeIn(rnd_lbl), FadeIn(bias_lbl, shift=0.1 * UP),
                      right_col.animate.set_opacity(0.3),
                      run_time=1.0)
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
        # the Cornell column starts 0.45 right of the "random" head, values under their head
        head_C = text("Cornell", size=26, color=PURPLE)
        head_C.next_to(head_R, RIGHT, buff=0.45).align_to(head_R, DOWN)
        p49 = MathTex(r"49\%", font_size=36, color=PURPLE)
        p45 = MathTex(r"45\%", font_size=36, color=PURPLE)
        p49.move_to([head_C.get_left()[0] + p49.width / 2, v46.get_center()[1], 0])
        p45.move_to([head_C.get_left()[0] + p45.width / 2, v54.get_center()[1], 0])
        marker4 = VGroup(Line([gx(4), AX2, 0], [gx(4), G_TOP, 0], color=PURPLE, stroke_width=5),
                         Dot([gx(4), AX2, 0], radius=0.1, color=PURPLE))
        p4 = MathTex("+4", font_size=40, color=PURPLE)
        p4.move_to([gx(4) + 0.2 + p4.width / 2, G_ARR, 0])
        with self.beat("observed") as beat:
            # the 3-hit ghost leaves (it sits under -8); "Cornell" heads the second column
            self.play(ghosts[2].animate.set_stroke(opacity=0), gops[2].animate.set_value(0),
                      FadeOut(header[1:]), header[0].animate.move_to([0, 3.3, 0]),
                      right_col.animate.set_opacity(1.0),
                      FadeIn(head_C, shift=0.1 * DOWN), run_time=0.7)
            for g_ in glyphs:
                g_.clear_updaters()
            self.remove(ghosts[2], glyphs)
            beat.wait_until("forty nine", offset=-0.2)
            self.play(FadeIn(p49, shift=0.1 * LEFT), run_time=0.6)
            beat.wait_until("forty five", offset=-0.2)
            self.play(FadeIn(p45, shift=0.1 * LEFT), run_time=0.6)
            beat.wait_until("plus four", offset=-0.5)
            # both values fly into the +4 dot; the arcs keep them clear of the column's other
            # labels (49% passes above "after 3 misses", 45% dips under 54%)
            c49, c45 = p49.copy(), p45.copy()
            self.add(c49, c45)
            self._fly.extend([c49, c45])
            dot_c = marker4[1].get_center()
            self.play(c49.animate(rate_func=smooth, path_arc=0.35).move_to(dot_c).scale(0.3)
                      .set_opacity(0),
                      Succession(Wait(0.1), c45.animate(rate_func=smooth, path_arc=-0.5)
                                 .move_to(dot_c).scale(0.3).set_opacity(0)),
                      FadeIn(marker4[1], scale=0.6, rate_func=delayed(0.5)),
                      Create(marker4[0], rate_func=delayed(0.5)), FadeIn(p4, rate_func=delayed(0.6)),
                      run_time=1.1)
            self.clean_fly()
            self.adopt(marker4)
            beat.wait_until("no hot", offset=-0.2)
            self.play(pulse(dashed, 1.06), run_time=0.9)

        brace = BraceBetweenPoints([gx(-8), G_TOP + 0.22, 0], [gx(4), G_TOP + 0.22, 0],
                                   direction=UP, color=PURPLE)
        brace_lbl = MathTex(r"+12\text{ points}", font_size=40, color=PURPLE)
        brace_lbl.next_to(brace, UP, buff=0.2)
        gym = text("no defenders", size=26, color=GRAY, slant=ITALIC)
        gym.next_to(p4, DOWN, buff=0.25, aligned_edge=LEFT)
        with self.beat("hot") as beat:
            self.play(GrowFromCenter(brace), VGroup(right_col, head_C).animate.set_opacity(0.3),
                      p49.animate.set_opacity(0.3), p45.animate.set_opacity(0.3),
                      run_time=beat.until("twelve", offset=-0.5))
            self.play(FadeIn(brace_lbl, shift=0.15 * DOWN), run_time=0.6)
            beat.wait_until("evidence", offset=-0.2)
            self.play(VGroup(header[0], cite_gvt, cite_ms).animate.set_opacity(0.3), run_time=0.8)
            beat.wait_until("gym", offset=-0.25)
            self.play(FadeIn(gym, shift=0.1 * UP), run_time=0.7)
            beat.wait_until("defenders", offset=-0.2)
            self.play(pulse(gym, 1.1), pulse(VGroup(marker4, p4), 1.04), run_time=0.9)

        # ================================================================ 10 landing
        OFF.set_value(SHIFT1)
        self.build_axis()
        big2 = VGroup(*[make_coin(f, BIG_R) for f in "HHTH"]).arrange(RIGHT, buff=BIG_STEP - 2 * BIG_R)
        big2.move_to(BIG_C)
        rings2 = VGroup(ring(big2[1], BIG_R + 0.1, 5), ring(big2[2], BIG_R + 0.1, 5))
        arcs2 = VGroup(*[CurvedArrow(big2[i].get_top() + UP * 0.14, big2[i + 1].get_top() + UP * 0.14,
                                     angle=-PI / 2, color=BLUE, stroke_width=5, tip_length=0.22)
                         for i in (0, 1)])
        score2 = score_tex(1, 2, size=60).next_to(big2, RIGHT, buff=0.75)
        dashed2 = DashedLine([vx(0.5), AX_Y, 0], [vx(0.5), LINE_TOP, 0], color=INK,
                             stroke_width=3, dash_length=0.12)
        guess2 = text("the obvious guess", size=26).move_to([0, LBL_Y, 0])
        guess2.align_to([vx(0.5) + 0.16, 0, 0], LEFT)
        blue2 = Line([vx(MEAN), AX_Y, 0], [vx(MEAN), LINE_TOP, 0], color=BLUE, stroke_width=5)
        num2 = MathTex(r"\frac{17}{42}", font_size=44, color=BLUE)
        num2.move_to([vx(MEAN) - 0.2 - num2.width / 2, LBL_Y, 0])
        mini2 = self.build_mini(scale=0.5, at=(vx(MEAN) - 2.45, -0.55, 0), op=0.6, compact=True)
        for g_ in mini2:
            self.allow_overlap(g_, reason="ghost miniature of the 16-row table (60% opacity): "
                                          "each letter sits inside its own small coin")
        HOT_Y = -1.0
        shooter = Dot([vx(0.5), HOT_Y, 0], radius=0.11, color=BLUE)
        hot3 = h_arrow(vx(MEAN) + 0.07, vx(0.5) - 0.16, HOT_Y)
        hot3_lbl = text("hot", size=30).next_to(shooter, RIGHT, buff=0.2)
        # out first, then the cold-open frame back in: the two frames never overlap
        self.play(*[FadeOut(m_) for m_ in list(self.mobjects)], run_time=0.5)
        self.play(FadeIn(big2), FadeIn(rings2), FadeIn(arcs2), FadeIn(score2),
                  FadeIn(self.axis), FadeIn(dashed2), FadeIn(guess2), run_time=0.8)
        with self.beat("landing") as beat:
            beat.wait_until("One half", offset=-0.2)
            self.play(pulse(dashed2, 1.06), pulse(guess2, edge=LEFT), run_time=0.9)
            # the sixteen rows of the cold open, averaged, land on 17/42
            beat.wait_until("fair", offset=-0.1)
            self.play(LaggedStart(*[FadeIn(g, shift=0.06 * DOWN) for g in mini2], lag_ratio=0.05),
                      run_time=0.9)
            beat.wait_until("Seventeen", offset=-0.15)
            self.play(mini2.animate.scale(0.1).move_to([vx(MEAN), LBL_Y, 0]).set_opacity(0),
                      Create(blue2, rate_func=delayed(0.35)), FadeIn(num2, rate_func=delayed(0.5)),
                      run_time=1.2)
            self.remove(mini2, *mini2)
            beat.wait_until("this test", offset=-0.15)
            self.play(pulse(num2, 1.12), run_time=0.8)
            # "A fifty percent shooter": that shooter's usual rate is the one-half line
            beat.wait_until("fifty percent", offset=-0.15)
            self.play(pulse(dashed2, 1.06), pulse(guess2, edge=LEFT), run_time=0.9)
            # "who averages one half on this test": the shooter's average, on the 50% line
            beat.wait_until("one half", 2, offset=-0.2)
            self.play(GrowFromCenter(shooter), run_time=0.6)
            beat.wait_until("already", offset=-0.25)
            self.play(GrowArrow(hot3), FadeIn(hot3_lbl, shift=0.1 * RIGHT),
                      run_time=beat.until("hot", offset=-0.05))
        # hold the answered frame; no ident over it
        self.hold(0.45)
