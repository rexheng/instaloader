"""Sample Space, episode 7: How Much Information Is in a Letter? (entropy).

    videos/toolkit/render.sh --preview videos/episodes/007-entropy-information/scene.py Episode /tmp/ep7.mp4
    videos/toolkit/render.sh videos/episodes/007-entropy-information/scene.py Episode \
        videos/episodes/007-entropy-information/final.mp4

Palette (one meaning each, see script.md):
    BLUE    probability (tile/column widths, every p, share strips, % braces)
    YELLOW  questions = bits (? box, cuts, counters, 2^k, k, log2(1/p), H, the level line)
    GREEN   Shannon's measurements (the 0.6-1.3 band, first-guess tally, "1 guess")
    PURPLE  context: characters already read (the row, Q, TH, THE OTHER DA)
    GRAY    axes, citations, leaders, the abandoned 4.75 (the only grey level)
    INK     letters, labels, the language-model marker
Data: data.json, written by data.py (Brown Corpus counts + Shannon 1951 record).
"""
from __future__ import annotations

import collections
import json
import math
from pathlib import Path

import numpy as np
from manim import *
from sample_space import *

HERE = Path(__file__).resolve().parent
D = json.loads((HERE / "data.json").read_text())
P = D["p"]                                   # Brown Corpus, 27 symbols
ALPHA = [chr(65 + i) for i in range(26)] + [" "]
ORDER = D["order"]                           # most to least frequent
H0 = math.log2(27)
H1 = D["H1"]
P_Q, H_Q = D["after_Q"]["p"], D["after_Q"]["H"]
P_TH, H_TH = D["after_TH"]["p"], D["after_TH"]["H"]
REC_TEXT, REC_G = D["record"]["text"], D["record"]["guesses"]
LO, HI = D["shannon_bounds_N100"]
UNIFORM = {s: 1 / 27 for s in ALPHA}
GUESS = collections.Counter(sum(REC_G, []))  # guess number -> how often (Shannon p. 56)
N_REC = sum(GUESS.values())                  # 102
H_GUESS = -sum(c / N_REC * math.log2(c / N_REC) for c in GUESS.values())   # 1.42
H_C2 = D["H_given_2_prev"]                   # 2.81: averaged over EVERY two-letter context
LLM_BPC = 0.8426                             # Valmeekam et al. 2023, Table IV: LLaMA-7B + AC
                                             # on a book (Dobie 1924, on Gutenberg 25 May 2023)
RUN = D["run_after_TH"]                      # E _ O after TH (from THE OTHER): two-letter costs
CTXS = D["contexts"]                         # possible contexts vs the corpus

# ------------------------------------------------------------------ chart geometry
X0, X1 = -5.2, 4.4                 # probability 0 .. 1 (room on the right for the tail inset)
W = X1 - X0
Y0 = -1.85                         # 0 questions
UNIT_A = 0.55                      # units per question while the chart only needs 0..6.5
UNIT_B = 0.345                     # ... and once it must hold costs up to 10.4
UNIT_C = 0.69                      # zoomed in (0..5.5) whenever everything drawn is a poured level
UNIT = UNIT_A
TICKS_B, TICKS_C = (0, 5, 10), (0, 2, 4)
YMAX = 11                          # full axis (skyline)
YTOP0 = 6.5                        # short axis until costs need the room
LAB_Y = Y0 - 0.32                  # symbol labels under the axis
XTICK_Y = Y0 - 0.72                # x tick labels (0% ... 100%), a row below the symbols
XTITLE_Y = -2.98                   # x-axis title, on the citation's row (right side)
COL_A = X1 + 0.62                  # right gutter: level values
LEDGER_X0 = -4.65                  # the run's bill (letters, context tags, probabilities,
LEDGER_Y = (1.42, 0.99, 0.45, -0.38, -0.95)  # costs, whole questions); the chart steps out
LEDGER_DX = 1.65                   # one column per letter of the run
LEDGER_FS = 40

# doubling strips sit ABOVE the (short) axis; the formula is then built centre stage
SX0, SX1 = -3.3, 1.5
SW = SX1 - SX0
STRIP_YE, STRIP_YZ, STRIP_HEAD_Y = 1.75, 1.1, 2.32
STRIP_LIFT = 0.65                  # the strips step up (and dim) to free the band for the formula
CNT_X = 2.2
EQ_SIZE = 56                       # the main equation
EQ_X, EQ_Y = 0.0, 0.75             # its '=' (p*2^k = 1, 2^k = 1/p and k = log2(1/p) share it)
TOP_Y = 2.3                        # formula row above the skyline
FS_TOP = 44                        # its font size (clears the context row and the 10 tick)

# tail inset (rare letters, widths magnified, heights true), 0.45 clear of the main axis
TAIL = ORDER[-4:]                  # X J Q Z
ZOOM = 28
INSET_GAP = 0.05                   # inset columns stand apart so their letters never crowd
INSET_X0 = 4.87                    # first inset column
INSET_FRAME_X0 = 4.8               # the inset's own frame (main axis ends at X1 + 0.05)


def cx(share: float) -> float:
    return X0 + W * share


def cy(q: float) -> float:
    return Y0 + UNIT * q


def set_unit(u: float) -> None:
    global UNIT
    UNIT = u


def cost(p: float) -> float:
    return 0.0 if p <= 0 else min(-math.log2(p), 10.4)


# ------------------------------------------------------------------ cold-open layout (reused by the landing)
ROW_Y_OPEN, ROW_Y_TOP = 1.4, 3.27
TILE_Y, CHAIN_Y, QLINE_Y = 0.15, -0.62, -1.62
TILE_LAB_Y = 0.785                 # '26 letters + space', between the row and the tiles
BOX, PITCH = 0.5, 0.6
Q_X = 3.6
CTX = "THE OTHER DA"


def row_x(i: int) -> float:
    return Q_X - (len(CTX) - i) * PITCH


# ------------------------------------------------------------------ small builders
def space_glyph(w: float = 0.17, h: float = 0.075, color=INK, sw: float = 2.6) -> VMobject:
    """The open-box space symbol, drawn (no font glyph needed)."""
    g = VMobject(stroke_color=color, stroke_width=sw)
    g.set_points_as_corners([[-w / 2, h, 0], [-w / 2, 0, 0], [w / 2, 0, 0], [w / 2, h, 0]])
    g.set_fill(opacity=0)
    return g


def glyph(s: str, size: float = 24, color=INK, font=SERIF) -> VMobject:
    if s == " ":
        k = size / 24
        return space_glyph(0.17 * k, 0.075 * k, color, 2.6 * k)
    return Text(s, font=font, font_size=size, color=color)


def set_glyph_opacity(m: VMobject, o: float) -> None:
    if isinstance(m, Text):
        m.set_opacity(o)
    else:                                   # open path: stroke only
        m.set_stroke(opacity=o)


def tile(s: str, side: float = 0.4) -> VGroup:
    sq = Square(side, stroke_color=BLUE, stroke_width=2, fill_color=BLUE, fill_opacity=0.14)
    g = glyph(s, 24)
    g.move_to(sq.get_center() + (DOWN * 0.04 if s == " " else ORIGIN))
    return VGroup(sq, g)


def tile_opacity(t: VGroup, o: float) -> VGroup:
    """Dim a candidate tile without filling the open space glyph."""
    t[0].set_stroke(opacity=o).set_fill(opacity=0.14 * o)
    set_glyph_opacity(t[1], o)
    return t


def dim_tiles(tiles, o: float, run_time: float = 0.5):
    return AnimationGroup(*[t[0].animate.set_stroke(opacity=o).set_fill(opacity=0.14 * o)
                            for t in tiles],
                          *[(t[1].animate.set_opacity(o) if isinstance(t[1], Text)
                             else t[1].animate.set_stroke(opacity=o)) for t in tiles],
                          run_time=run_time)


def column(xl: float, w: float, h: float, base: float = Y0, fill: float = 0.85) -> Rectangle:
    """A probability column. Hairline columns get no edge (so they stay visible), and
    flattened ones a blue outline (so they never vanish into the axis)."""
    empty = w <= 1e-9                       # zero probability: nothing to draw
    w, h = max(w, 0.002), max(h, 0.002)
    if empty:
        sc, sw, fill = BLUE, 0, 0.0
    elif w < 0.03:
        sc, sw = BLUE, 0
    elif h < 0.08:
        sc, sw = BLUE, 3
    else:
        sc, sw = BG, 1.6
    r = Rectangle(width=w, height=h, stroke_color=sc, stroke_width=sw,
                  fill_color=BLUE, fill_opacity=fill)
    return r.move_to([xl + w / 2, base + h / 2, 0])


def layout(order, probs, heights) -> dict:
    out, xl = {}, X0
    for s in order:
        w = W * probs[s]
        out[s] = column(xl, w, UNIT * heights[s])
        xl += w
    return out


def slab(x_left: float, width: float, y_bottom: float, h: float) -> Rectangle:
    hh = max(h, 0.0015)
    r = Rectangle(width=width, height=hh, stroke_color=BG, stroke_width=1.2 if h > 0.03 else 0,
                  fill_color=BLUE, fill_opacity=0.85)
    return r.move_to([x_left + width / 2, y_bottom + hh / 2, 0])


def poured(order, probs, heights) -> dict:
    """Each column becomes a full-width slab of the SAME area; stacked, the slabs reach the
    average height.  (area = p * cost, width 1 -> height p * cost)"""
    out, yb = {}, Y0
    for s in order:
        h = UNIT * probs[s] * heights[s]
        out[s] = slab(X0, W, yb, h)
        yb += h
    return out


def hidden_box() -> Square:
    """A character already read (context), shown dim because the viewer can't see it."""
    return Square(BOX, stroke_color=PURPLE, stroke_width=2, stroke_opacity=0.45,
                  fill_color=PURPLE, fill_opacity=0.07)


def ctx_box(ch: str) -> VGroup:
    sq = Square(BOX, stroke_color=PURPLE, stroke_width=3, fill_color=PURPLE, fill_opacity=0.16)
    g = glyph(ch, 30, PURPLE)
    g.move_to(sq.get_center() + (DOWN * 0.05 if ch == " " else ORIGIN))
    return VGroup(sq, g)


def pflash(m: VMobject, scale: float = 1.1):
    """Context emphasis: a purple flash (yellow already means 'questions')."""
    return Indicate(m, color=PURPLE, scale_factor=scale, run_time=0.9)


def glyph_fade(cells, o: float):
    """Fade record glyphs; the open space glyph is stroke-only (never fill it)."""
    return [c.animate.set_opacity(o) if isinstance(c, Text) else c.animate.set_stroke(opacity=o)
            for c in cells]


def outline_flash(cols, run_time: float = 0.9, lag: float = 0.0):
    """Emphasis on probability columns: white edge + brighter blue, then back."""
    anims = [c.animate(rate_func=there_and_back).set_stroke(INK, 3.5).set_fill(BLUE, opacity=1.0)
             for c in cols]
    if lag:
        return LaggedStart(*anims, lag_ratio=lag, run_time=run_time)
    return AnimationGroup(*anims, run_time=run_time)


def rect_box(m: VMobject):
    lo, hi = m.get_corner(DL), m.get_corner(UR)
    return lo[0], lo[1], max(hi[0] - lo[0], 1e-4), max(hi[1] - lo[1], 1e-4)


def geo_morph(mob: VMobject, tgt: VMobject, rate=smooth):
    """Rectangle -> rectangle with width and height interpolated geometrically.  A column
    poured into a slab of the same area keeps exactly that area at every frame, so the
    pour reads as liquid spreading instead of boxes ballooning."""
    x0, y0, w0, h0 = rect_box(mob)
    x1, y1, w1, h1 = rect_box(tgt)
    sc0, sc1 = mob.get_stroke_color(), tgt.get_stroke_color()
    sw0, sw1 = mob.get_stroke_width(), tgt.get_stroke_width()
    f0, f1 = mob.get_fill_opacity(), tgt.get_fill_opacity()

    def upd(m, a):
        a = rate(a)
        w, h = w0 ** (1 - a) * w1 ** a, h0 ** (1 - a) * h1 ** a
        x, y = x0 + (x1 - x0) * a, y0 + (y1 - y0) * a
        m.set_points_as_corners([[x + w, y + h, 0], [x, y + h, 0], [x, y, 0], [x + w, y, 0],
                                 [x + w, y + h, 0]])
        m.set_stroke(color=interpolate_color(sc0, sc1, a), width=sw0 + (sw1 - sw0) * a)
        m.set_fill(opacity=f0 + (f1 - f0) * a)
    return UpdateFromAlphaFunc(mob, upd)


def hatching(x0: float, y0: float, x1: float, y1: float, step: float = 0.34) -> VGroup:
    """45-degree yellow hatching over a rectangle: marks 'wasted questions' while the
    blue bars underneath stay blue."""
    g, h = VGroup(), y1 - y0
    c = x0 - h
    while c < x1:
        t0, t1 = max(0.0, x0 - c), min(h, x1 - c)
        if t1 - t0 > 0.02:
            g.add(Line([c + t0, y0 + t0, 0], [c + t1, y0 + t1, 0], stroke_width=2.2))
        c += step
    return g.set_stroke(YELLOW, width=2.2, opacity=0.55)


def frac_glyphs(part: VMobject) -> dict:
    """Glyphs of a rendered '\\log_2\\!\\frac{1}{p}': l o g 2, then 1 / bar / p by height."""
    g = list(part.submobjects)
    rest = sorted(g[4:], key=lambda m: -m.get_center()[1])
    return {"log": VGroup(*g[:3]), "two": g[3], "one": rest[0], "bar": rest[1], "p": rest[2]}


def log_formula(*parts: str, size: float = 48) -> MathTex:
    """MathTex whose '\\log_2\\!\\frac{1}{p}' part is yellow with a BLUE p."""
    m = MathTex(*parts, font_size=size)
    for i, t in enumerate(parts):
        if t == r"\log_2\!\frac{1}{p}":
            m[i].set_color(YELLOW)
            frac_glyphs(m[i])["p"].set_color(BLUE)
        elif t == "p":
            m[i].set_color(BLUE)
    return m


def route(points) -> VMobject:
    """A smooth path through the given waypoints (used to steer flying glyphs around text)."""
    p = VMobject()
    p.set_points_smoothly([np.array([x, y, 0.0]) for x, y in points])
    return p


def fly(mob: VMobject, target: VMobject, path: VMobject, rate=linear):
    """Move `mob` along `path` onto `target` (same glyph, possibly another size): its height
    interpolates to the target's, so the arrival is seamless."""
    h0, h1 = max(mob.height, 1e-3), max(target.height, 1e-3)
    start = mob.copy()

    def upd(m, a):
        a = rate(a)
        m.become(start)
        m.scale((h0 + (h1 - h0) * a) / h0)
        m.move_to(path.point_from_proportion(a))
    return UpdateFromAlphaFunc(mob, upd)


def fly_morph(src: VMobject, tgt: VMobject, path: VMobject, rate=smooth, fade=(0.25, 0.75)):
    """A copy of `src` travels along `path` (which ends on `tgt`) and cross-fades into `tgt`
    on the way, so two different glyphs never morph point-by-point into each other.
    Returns (group, animation): after playing, remove the group and add `tgt`."""
    a0, b0 = src.copy(), tgt.copy()
    a_m, b_m = a0.copy(), b0.copy()
    ha, hb = max(a0.height, 1e-3), max(b0.height, 1e-3)
    s_c, s_w, s_h = src.get_center(), src.width, src.height
    oa = [m.get_fill_opacity() for m in a0.family_members_with_points()]
    ob = [m.get_fill_opacity() for m in b0.family_members_with_points()]
    g = VGroup(a_m, b_m)

    def clear_of_source(p, k):
        """Gap between the copy's box (scaled by k, centred at p) and the source's box."""
        w, h = a0.width * k, a0.height * k
        return max(abs(p[0] - s_c[0]) - (w + s_w) / 2, abs(p[1] - s_c[1]) - (h + s_h) / 2)

    def upd(_m, t):
        t = rate(t)
        p = path.point_from_proportion(t)
        h = ha + (hb - ha) * t
        # the old glyph dims out completely before the new one brightens: never superimposed
        mid = (fade[0] + fade[1]) / 2
        fa = float(np.clip((t - fade[0]) / max(mid - fade[0], 1e-6), 0, 1))
        fb = float(np.clip((t - mid) / max(fade[1] - mid, 1e-6), 0, 1))
        # invisible while it still overlaps its source; fully visible once 0.12 clear
        e = float(np.clip(clear_of_source(p, h / ha) / 0.12, 0, 1))
        a_m.become(a0).scale(h / ha).move_to(p)
        b_m.become(b0).scale(h / hb).move_to(p)
        for m, o in zip(a_m.family_members_with_points(), oa):
            m.set_fill(opacity=o * (1 - fa) * e).set_stroke(opacity=0)
        for m, o in zip(b_m.family_members_with_points(), ob):
            m.set_fill(opacity=o * fb * e).set_stroke(opacity=0)
    upd(None, 0)
    return g, UpdateFromAlphaFunc(g, upd, rate_func=linear)     # `rate` is the only easing


def tile_columns(cols: dict, old_order, new_order, probs, heights, unit, rank_lag=0.028):
    """Re-sort columns with NO gaps and NO overlaps in any frame.

    Each column is poured from its old slot into its new one: the part already moved sits in
    the sorted block that grows from the left (in the new order), the rest stays in the old
    block (old order) packed against it.  Widths always sum to 100 %, so every frame tiles
    0..100 %.  Columns move in rank order (the most frequent first).  Returns (animation,
    cleanup); the old-slot pieces are temporary mobjects removed by cleanup."""
    ghosts = {s: cols[s].copy() for s in old_order}
    rank = {s: i for i, s in enumerate(new_order)}
    n = len(new_order)
    span = 1 - rank_lag * (n - 1)
    memo = {}

    def frame(a):
        """(x, w) of every new-slot piece and every old-slot piece at progress a."""
        if a not in memo:
            e = {s: smooth(float(np.clip((a - rank[s] * rank_lag) / span, 0, 1)))
                 for s in new_order}
            new, old, x = {}, {}, X0
            for s in new_order:                       # the sorted block grows from the left
                w = W * probs[s] * e[s]
                new[s] = (x, w)
                x += w
            for s in old_order:                       # what is left, still in the old order
                w = W * probs[s] * (1 - e[s])
                old[s] = (x, w)
                x += w
            memo.clear()
            memo[a] = (new, old)
        return memo[a]

    def rect(m, x, w, h):
        w = max(w, 0.0)
        m.set_points_as_corners([[x + w, Y0 + h, 0], [x, Y0 + h, 0], [x, Y0, 0], [x + w, Y0, 0],
                                 [x + w, Y0 + h, 0]])
        m.set_stroke(BG, width=1.6 if w > 0.03 else 0)
        m.set_fill(BLUE, opacity=0.85 if w > 1e-4 else 0)

    def piece(s, which):
        m = cols[s] if which == 0 else ghosts[s]

        def upd(mob, a):
            x, w = frame(a)[which][s]
            rect(mob, x, w, unit * heights[s])
        return UpdateFromAlphaFunc(m, upd)

    for s in new_order:                               # start: everything still in its old slot
        rect(cols[s], X0, 0, unit * heights[s])
    anims = [piece(s, 0) for s in new_order] + [piece(s, 1) for s in old_order]
    return ghosts, anims


def tile_morph(cols: dict, p0: dict, p1: dict, h0: dict, h1: dict, unit: float, rate=smooth):
    """Re-weight AND re-price the skyline in one move.  Left edges and widths interpolate
    linearly (so the bar tiles 0..100 % in every frame); heights interpolate geometrically,
    so a cost that collapses (U after Q, E after TH) falls at once instead of standing at its
    old height while the column widens: no column ever draws more area than it starts with."""
    anims = []
    xa, xb = X0, X0
    for s in ORDER:
        wa, wb = W * p0[s], W * p1[s]
        ha, hb = max(unit * h0[s], 0.002), max(unit * h1[s], 0.002)

        def upd(m, a, xa=xa, xb=xb, wa=wa, wb=wb, ha=ha, hb=hb):
            a = rate(a)
            w = wa + (wb - wa) * a
            m.become(column(xa + (xb - xa) * a, w, ha ** (1 - a) * hb ** a))
        anims.append(UpdateFromAlphaFunc(cols[s], upd))
        xa += wa
        xb += wb
    return anims


class Episode(NarratedScene):
    EPISODE = 7
    TITLE = "How Much Information Is in a Letter?"
    SPEED = 0.83                       # PRODUCTION_GUIDE §13: 0.82-0.84, never faster
    CADENCE = "shaped"                 # sentence and beat gaps follow the sense
    BEAT_GAP = 0.38                    # an ordinary beat boundary
    TURN_GAP = 0.8                     # the act turns: no context -> context -> a person ->
                                       # the payoff line -> the landing
    PRONUNCIATIONS = {"TH": "tee aitch"}

    # ============================================================== construct
    def construct(self):
        self.cold_open()
        self.halve_alphabet()
        self.target()
        self.fail_alike()
        self.split_probability()
        self.doublings()
        self.skyline()
        self.entropy()
        self.context()
        self.payoff()
        self.landing()
        # no end card: the landing frame (the cold open, re-seen) holds to the end
        self.hold(0.1)

    def exclude(self, group: VMobject, reason: str) -> None:
        """Leave a deliberately tight group out of the overlap audit (with a reason for the
        critics).  Every member is flagged, because members get animated (and so reach the
        scene) on their own."""
        self.allow_overlap(group, reason=reason)
        for m in group.get_family():
            allow_overlap(m)

    def visible(self) -> list:
        """Top-level mobjects worth fading (drivers and trackers are removed outright)."""
        out = []
        for m in list(self.mobjects):
            if isinstance(m, ValueTracker) or type(m) is Mobject:
                m.clear_updaters()
                self.remove(m)
            else:
                out.append(m)
        return out

    # ============================================================== 1 cold open
    def cold_open(self):
        self.hidden = VGroup(*[hidden_box() for _ in CTX])
        for i, b in enumerate(self.hidden):
            b.move_to([row_x(i), ROW_Y_OPEN, 0])
        self.lead = MathTex(r"\cdots", color=PURPLE, font_size=40).set_opacity(0.6)
        self.lead.next_to(self.hidden, LEFT, buff=0.22)
        self.qbox = Square(BOX + 0.06, stroke_color=YELLOW, stroke_width=4)
        self.qbox.move_to([Q_X, ROW_Y_OPEN, 0])
        self.qmark = Text("?", font=SERIF, font_size=36, color=YELLOW).move_to(self.qbox)
        self.row = VGroup(self.lead, self.hidden, self.qbox, self.qmark)
        self.read_lab = text("already read", size=26, color=PURPLE)
        self.read_lab.next_to(self.hidden, UP, buff=0.2)

        self.tiles = VGroup(*[tile(s) for s in ALPHA]).arrange(RIGHT, buff=0.06)
        self.exclude(self.tiles, "alphabet tile row: each letter sits inside its own tile, tiles "
                     "0.06 apart; the halving cuts sit in the gaps between tiles")
        self.tiles.move_to([0, TILE_Y, 0])
        self.tile = dict(zip(ALPHA, self.tiles))

        self.tile_lab = text("26 letters + space", size=26, color=GRAY)
        self.tile_lab.move_to([0, TILE_LAB_Y, 0]).align_to(self.qbox, RIGHT)

        self.qlabel = text("questions per character", size=LABEL, color=INK)
        self.qval = MathTex("?", font_size=EQ, color=YELLOW)
        self.qline = VGroup(self.qlabel, self.qval).arrange(RIGHT, buff=0.3).move_to([0, QLINE_Y, 0])

        # the row is real text: a faint glimpse of it (too faint to read), then it is hidden.
        # The landing reveals it as THE OTHER DA.
        ghosts = VGroup()
        for i, ch in enumerate(CTX):
            g = glyph(ch, 30, PURPLE).move_to(self.hidden[i])
            if ch == " ":
                g.shift(DOWN * 0.05)
            set_glyph_opacity(g, 0.0)
            ghosts.add(g)

        # frame 1 already holds the whole puzzle: the text so far, the hidden slot, and the
        # 27 candidates for it
        with self.narrate("You've read an English sentence up to one hidden character. With "
                          "yes-or-no questions, how many do you need, on average? "
                          "[pause 1.5]") as beat:
            self.add(self.row, self.read_lab, self.tiles, self.tile_lab, ghosts)
            self.play(LaggedStart(*glyph_fade(ghosts, 0.09), lag_ratio=0.12), run_time=0.9)
            self.play(*glyph_fade(ghosts, 0.0), run_time=0.5)
            self.remove(ghosts)
            beat.wait_until("hidden", offset=-0.2)
            # the hidden slot, and the candidates that could fill it
            self.play(flag(VGroup(self.qbox, self.qmark), run_time=0.8),
                      LaggedStart(*[t.animate(rate_func=there_and_back).shift(0.12 * UP)
                                    for t in self.tiles], lag_ratio=0.04),
                      run_time=1.1)
            beat.wait_until("With", offset=-0.1)
            self.play(FadeIn(self.qline, shift=0.1 * UP), run_time=0.7)
            beat.wait_until("average", offset=-0.1)
            self.play(flag(self.qval), run_time=0.9)

    # ============================================================== 2 halve the alphabet
    def halve_alphabet(self):
        five = MathTex("5", font_size=EQ, color=YELLOW).move_to(self.qval)
        # kept groups close on Y: A-N | O-_, O-U | V-_, VWX | YZ_, YZ | _, Y | Z
        cuts = [(13, list(range(0, 14))), (20, list(range(14, 21))),
                (23, list(range(21, 24))), (25, [26]), (24, [25])]
        chain = MathTex("27", r"\to", "13", r"\to", "6", r"\to", "3", r"\to", "2", r"\to", "1",
                        font_size=MATH)
        for i in range(1, 11, 2):
            chain[i].set_color(YELLOW)
        chain.move_to([0, CHAIN_Y, 0])
        self.chain = chain
        lines = VGroup()
        with self.narrate("The natural answer is five: each answer halves what's left, and five "
                          "cuts take twenty-seven to one.") as beat:
            beat.wait_until("five", offset=-0.15)
            self.play(swap(self.qval, five, run_time=0.6))
            self.qval = five
            beat.wait_until("each", offset=-0.1)
            self.play(FadeIn(chain[0], shift=0.1 * UP), run_time=0.5)
            step_rt = [beat.until("halves", offset=0.3), 0.65, 0.65, 0.65, 0.65]
            for k, (after, dropped) in enumerate(cuts):
                a, b = self.tiles[after], self.tiles[after + 1]
                x = (a.get_right()[0] + b.get_left()[0]) / 2
                cut = Line([x, TILE_Y - 0.3, 0], [x, TILE_Y + 0.3, 0], color=YELLOW, stroke_width=4)
                lines.add(cut)
                rt = max(0.6, step_rt[k]) if k else max(0.7, step_rt[0])
                self.play(Create(cut),
                          dim_tiles([self.tiles[j] for j in dropped], 0.22),
                          FadeIn(chain[2 * k + 1], shift=0.1 * RIGHT),
                          FadeIn(chain[2 * k + 2], shift=0.1 * RIGHT), run_time=rt)
            self.play(Indicate(self.tiles[24], color=YELLOW, scale_factor=1.2), run_time=0.7)
        self.cuts = lines

        # the finished line 'questions per character  log2 27 ~ 4.75' is centred at x = 0;
        # its pieces arrive one at a time, each from where it comes from
        logf = MathTex(r"\log_2", "27", r"\approx", "4.75", font_size=EQ)
        logf[3].set_color(YELLOW)
        lab_to = self.qlabel.copy()
        VGroup(lab_to, logf).arrange(RIGHT, buff=0.3).move_to([0, QLINE_Y, 0])
        c27 = chain[0].copy()
        # the 27 travels BELOW the chain and above the label, then drops into its slot
        a, b = chain[0].get_center(), logf[1].get_center()
        y_lane = (chain.get_bottom()[1] + lab_to.get_top()[1]) / 2
        path = route([(a[0], a[1]), (a[0] + 0.35, y_lane), (b[0] - 0.7, y_lane), (b[0], b[1])])
        with self.narrate("The ideal is log base two of twenty-seven: four point seven "
                          "five.") as beat:
            beat.wait_until("ideal", offset=-0.2)
            # make room: the label steps left, the 5 waits where the answer will stand
            self.play(self.qlabel.animate.move_to(lab_to), self.qval.animate.move_to(logf[3]),
                      run_time=0.7)
            beat.wait_until("log", offset=-0.1)
            self.play(Write(logf[0]), run_time=0.6)
            self.add(c27)
            self.play(fly(c27, logf[1], path), rate_func=rate_functions.ease_out_sine,
                      run_time=beat.until("four", offset=-0.15, min_time=0.9))
            self.remove(c27)
            self.add(logf[1])
            # the 5 steps up and out before 4.75 steps in: the two never share the slot
            self.play(Write(logf[2]), swap(self.qval, logf[3], run_time=1.0), run_time=1.0)
        self.logf = logf

    # ============================================================== 3 target + stakes
    def target(self):
        # the baseline stays on top of every column (they flash and re-layer)
        self.x_axis = Line([X0, Y0, 0], [X1 + 0.05, Y0, 0], color=GRAY, stroke_width=2.5).set_z_index(1)
        self.y_axis = Line([X0, Y0, 0], [X0, cy(YTOP0), 0], color=GRAY, stroke_width=2.5)
        self.ytick = {v: self.make_ytick(v) for v in (0, 5)}
        self.y_ticks = VGroup(*self.ytick.values())
        yt = self.y_ticks
        self.y_title = text("questions", size=LABEL - 2, color=GRAY)
        self.y_title.next_to(self.y_axis.get_top(), UP, buff=0.2).align_to(yt, LEFT)

        cols = layout(ALPHA, UNIFORM, {s: H0 for s in ALPHA})
        self.cols = cols
        self.colg = VGroup(*[cols[s] for s in ALPHA])
        labs = {s: glyph(s, 24) for s in ALPHA}
        for s in ALPHA:
            labs[s].move_to([cols[s].get_center()[0], LAB_Y + (0.06 if s == " " else 0), 0])
        self.labs = labs
        self.lab_op = {s: ValueTracker(1.0) for s in ALPHA}   # each label's opacity

        self.avg_line = DashedLine([X0, cy(H0), 0], [X1, cy(H0), 0], color=YELLOW,
                                   stroke_width=3.5, dash_length=0.14).set_z_index(3)
        self.avg_num = MathTex("4.75", font_size=36, color=YELLOW).move_to([COL_A, cy(H0), 0])

        # Shannon's band sits BEHIND the bars; thin edges on top keep it readable
        fill = Rectangle(width=W, height=UNIT * (HI - LO), stroke_width=0, fill_color=GREEN,
                         fill_opacity=0.28).move_to([X0 + W / 2, cy((LO + HI) / 2), 0])
        fill.set_z_index(-1)
        edges = VGroup(Line([X0, cy(LO), 0], [X1, cy(LO), 0]), Line([X0, cy(HI), 0], [X1, cy(HI), 0]))
        edges.set_stroke(GREEN, 2).set_z_index(2)
        self.band_fill, self.band_edges = fill, edges
        self.band = VGroup(fill, edges)
        self.band_lab = MathTex(r"\approx\!1", font_size=36, color=GREEN)
        self.place_band_lab(self.band_lab)
        self.cite_sh = citation("Shannon, 1951 · Bell System Technical Journal")

        with self.narrate("In 1951, Claude Shannon put the true figure at about one. No "
                          "compressor beats it on average, and guessing what comes next is how "
                          "language models are trained.") as beat:
            # 1. clear the halving diagram; 4.75 steps right into the gutter at its own
            #    height, clear of where any column will stand
            self.play(FadeOut(self.chain), FadeOut(self.cuts), FadeOut(self.qlabel),
                      FadeOut(self.tile_lab),
                      FadeOut(VGroup(self.logf[0], self.logf[1], self.logf[2])),
                      self.read_lab.animate.shift(UP * (ROW_Y_TOP - ROW_Y_OPEN)).set_opacity(0),
                      self.row.animate.shift(UP * (ROW_Y_TOP - ROW_Y_OPEN)),
                      self.logf[3].animate.move_to([COL_A + 0.2, self.logf[3].get_y(), 0]),
                      run_time=0.7)
            self.remove(self.read_lab)
            # 2. the baseline grows (the tile row is still up, so no vertical axis yet)
            self.play(Create(self.x_axis), run_time=0.5)
            # 3. each tile drops onto the baseline as the foot of its column ...
            feet = {s: column(cols[s].get_left()[0], cols[s].width, 0.42) for s in ALPHA}
            moves = []
            for s in ALPHA:
                moves.append(ReplacementTransform(self.tile[s][0], feet[s]))
                moves.append(ReplacementTransform(self.tile[s][1], labs[s]))
            self.play(LaggedStart(*moves, lag_ratio=0.02),
                      run_time=beat.until("Shannon", offset=-0.1, min_time=1.0))
            # 4. ... the vertical axis grows as every column rises to the same price; 4.75
            #    climbs the gutter BEHIND the column tops (it never labels a height the bars
            #    have not reached) and settles on the price line as the bars arrive there
            trail = lambda t: smooth(max(0.0, (t - 0.3) / 0.7))
            self.play(Create(self.y_axis), FadeIn(self.y_ticks), FadeIn(self.y_title),
                      *[ReplacementTransform(feet[s], cols[s]) for s in ALPHA],
                      self.logf[3].animate(rate_func=trail).scale_to_fit_height(self.avg_num.height)
                      .move_to(self.avg_num),
                      Create(self.avg_line), FadeIn(self.cite_sh, shift=0.1 * UP),
                      run_time=1.0)
            self.remove(self.logf[3])
            self.add(self.avg_num)
            self.remove(self.y_ticks)              # ticks live on their own (they re-scale)
            self.add(*self.ytick.values())
            self._tick_leavers, self._tick_arrivals = [], []
            self.add_label_updater()
            beat.wait_until("about one", offset=-0.2)
            self.play(FadeIn(self.band), FadeIn(self.band_lab, shift=0.1 * LEFT), run_time=0.9)
            beat.wait_until("compressor", offset=-0.25)
            self.play(Indicate(self.band_edges, color=GREEN, scale_factor=1.0),
                      flag(self.band_lab, color=GREEN), run_time=0.9)
            beat.wait_until("guessing", offset=-0.15)
            self.play(LaggedStart(*[pflash(b) for b in self.hidden], lag_ratio=0.12),
                      run_time=beat.until("language", offset=-0.15, min_time=1.2))
            # ... which is exactly what a language model is trained to fill
            llm = text("LLM", size=28, color=INK)
            llm.move_to([self.qbox.get_right()[0] + 0.98, self.qbox.get_y(), 0])
            llm_arrow = Arrow([llm.get_left()[0] - 0.12, llm.get_y(), 0],
                              [self.qbox.get_right()[0] + 0.12, llm.get_y(), 0], buff=0,
                              color=INK, stroke_width=3, max_tip_length_to_length_ratio=0.4)
            self.play(FadeIn(llm, shift=0.15 * LEFT), GrowArrow(llm_arrow),
                      flag(VGroup(self.qbox, self.qmark)), run_time=0.8)
        self.llm_tag = VGroup(llm, llm_arrow)

    def make_ytick(self, v: float) -> VGroup:
        tk = Line([X0 - 0.06, cy(v), 0], [X0, cy(v), 0], color=GRAY, stroke_width=2.5)
        lb = MathTex(str(v), font_size=MATH_SMALL, color=GRAY).next_to(tk, LEFT, buff=0.12)
        lb.ss_role = "tick"
        return VGroup(tk, lb)

    def add_label_updater(self):
        driver = Mobject()

        def upd(_):
            for s in ALPHA:
                r, m = self.cols[s], self.labs[s]
                m.move_to([r.get_center()[0], LAB_Y + (0.06 if s == " " else 0), 0])
                o = float(np.clip((r.width - 0.265) / 0.03, 0, 1))   # narrow columns: no label
                set_glyph_opacity(m, o * self.lab_op[s].get_value())
        driver.add_updater(upd)
        self.add(driver)
        self.bring_to_back(driver)
        self.lab_driver = driver

    def labels_to(self, value: float, only=None, keep=()):
        """Animations taking the axis letters to `value` opacity (all, or `only`, minus `keep`)."""
        syms = ALPHA if only is None else only
        return [self.lab_op[s].animate.set_value(value) for s in syms if s not in keep]

    def zoom(self, unit: float, extra_lines=()):
        """Re-fit the y-axis to what is drawn: switch the scale to `unit` and return the
        animations that carry every y-anchored object to it (ticks spread or close up, the
        band, reference lines and their labels ride along).  Columns are not included: their
        new targets are computed by the caller with the new unit."""
        old = UNIT
        set_unit(unit)
        k = unit / old
        new_vals = TICKS_C if unit == UNIT_C else TICKS_B
        anims = []
        # ticks: survivors move with the scale; the old ticks are gone (first 30 %) before
        # the new ones fade in at their places (last 35 %), so two scales never share the axis
        for v, g in list(self.ytick.items()):
            if v in new_vals:
                anims.append(g.animate.shift(UP * (Y0 + unit * v - g[0].get_y())))
            else:
                tgt = g.copy().shift(UP * min(0.3, max(-0.3, Y0 + unit * v - g[0].get_y())))
                anims.append(Transform(g, tgt.set_opacity(0),
                                       rate_func=lambda t: smooth(min(1.0, t / 0.3))))
                self._tick_leavers.append(g)
                del self.ytick[v]
        for v in new_vals:
            if v not in self.ytick:
                g = self.make_ytick(v)
                start = g.copy().set_opacity(0)
                self.ytick[v] = g
                self.add(start)
                anims.append(Transform(start, g, rate_func=lambda t: smooth(max(0.0, (t - 0.65) / 0.35))))
                self._tick_arrivals.append((start, g))
        self.y_ticks = VGroup(*self.ytick.values())
        # Shannon's band and its label
        anims.append(self.band_fill.animate.stretch_to_fit_height(UNIT * (HI - LO))
                     .move_to([X0 + W / 2, cy((LO + HI) / 2), 0]))
        anims.append(self.band_edges[0].animate.move_to([X0 + W / 2, cy(LO), 0]))
        anims.append(self.band_edges[1].animate.move_to([X0 + W / 2, cy(HI), 0]))
        anims.append(self.place_band_lab(self.band_lab.copy(), animate_from=self.band_lab))
        # dashed reference levels with their gutter numbers: (line, number, value)
        for line, num, v in extra_lines:
            anims.append(line.animate.move_to([line.get_x(), cy(v), 0]))
            anims.append(num.animate.move_to([num.get_x(), cy(v), 0]))
        return anims

    def zoom_done(self):
        """After a zoom: drop the faded leavers, swap arrivals for their real ticks."""
        for g in self._tick_leavers:
            self.remove(g)
        for start, g in self._tick_arrivals:
            self.remove(start)
            self.add(g)
        self._tick_leavers, self._tick_arrivals = [], []

    def morph(self, order, probs, heights, run_time, extra=(), rate_func=smooth):
        tgt = layout(order, probs, heights)
        anims = [Transform(self.cols[s], tgt[s], rate_func=rate_func) for s in ALPHA]
        self.play(*anims, *extra, run_time=run_time)     # extras keep their own timing

    def hide_labels(self, run_time=0.3):
        self.play(*self.labels_to(0.0), run_time=run_time)

    def show_labels(self, run_time=0.4):
        self.play(*self.labels_to(1.0), run_time=run_time)

    def pour(self, probs, heights, run_time, extra=()):
        """Columns flow, left to right, into full-width slabs stacked from the floor."""
        tgt = poured(ORDER, probs, heights)
        self.play(LaggedStart(*[geo_morph(self.cols[s], tgt[s]) for s in ORDER],
                              lag_ratio=0.06), *extra, run_time=run_time)

    def unpour(self, probs, heights, run_time, extra=()):
        """The stack rises back into a skyline, top slab first."""
        tgt = layout(ORDER, probs, heights)
        self.play(LaggedStart(*[geo_morph(self.cols[s], tgt[s]) for s in reversed(ORDER)],
                              lag_ratio=0.05), *extra, run_time=run_time)

    def place_band_lab(self, m, animate_from=None):
        """Shannon's band is labelled like an axis value: left of the y-axis, centred on the
        band (on the squat scale it rises just enough to clear the 0 tick)."""
        m.move_to([0, max(cy((LO + HI) / 2), Y0 + 0.43), 0]).align_to([X0 - 0.18, 0, 0], RIGHT)
        if animate_from is not None:
            return animate_from.animate.move_to(m)
        return m

    def level_marks(self, value: float):
        line = DashedLine([X0, cy(value), 0], [X1, cy(value), 0], color=YELLOW,
                          stroke_width=3.5, dash_length=0.14).set_z_index(3)
        num = DecimalNumber(value, num_decimal_places=2, font_size=36, color=YELLOW)
        num.move_to([COL_A, cy(value), 0]).set_z_index(3)
        return line, num

    # ============================================================== 4 fail: alike
    def fail_alike(self):
        # a light yellow wash (13 %) + outline, so the bars under it stay blue
        waste = Rectangle(width=W, height=UNIT * (H0 - 1.0), stroke_color=YELLOW, stroke_width=3,
                          fill_color=YELLOW, fill_opacity=0.13)
        waste.set_fill(opacity=0)
        waste.move_to([X0 + W / 2, cy((H0 + 1.0) / 2), 0]).set_z_index(4)
        hatch = hatching(X0, cy(1.0), X1, cy(H0)).set_z_index(4)
        arrow = DoubleArrow([0, cy(1.0), 0], [0, cy(H0), 0], buff=0, color=YELLOW,
                            stroke_width=4, tip_length=0.16,
                            max_tip_length_to_length_ratio=0.2).set_z_index(5)
        wlab = MathTex(r"3.75\ \text{extra}\ (79\%)", font_size=36, color=YELLOW)
        wlab.move_to([0, cy(H0) + 0.38, 0])
        self.cite_br = citation("Letter counts: Brown Corpus (Francis & Kučera, 1964)")
        xt = VGroup()
        for v in (0, 0.25, 0.5, 0.75, 1.0):
            tk = Line([cx(v), Y0, 0], [cx(v), Y0 - 0.07, 0], color=GRAY, stroke_width=2.5)
            lb = MathTex(f"{int(v * 100)}\\%", font_size=26, color=GRAY)
            lb.move_to([cx(v), XTICK_Y, 0])
            lb.ss_role = "tick"
            xt.add(VGroup(tk, lb))
        self.x_ticks = xt
        self.x_title = self.x_title_for(None)

        with self.narrate("So where do four of every five questions go? Z costs as much as E, yet "
                          "E turns up a hundred thirty times as often.") as beat:
            beat.wait_until("where", offset=-0.15)
            self.play(FadeIn(waste), FadeIn(hatch), GrowFromCenter(arrow),
                      FadeIn(wlab, shift=0.1 * DOWN), FadeOut(self.llm_tag), run_time=1.0)
            beat.wait_until("Z", offset=-0.15)
            self.play(FadeOut(hatch), FadeOut(waste), FadeOut(arrow), FadeOut(wlab), FadeOut(self.cite_sh),
                      *[self.cols[s].animate.set_fill(opacity=0.25) for s in ALPHA
                        if s not in ("E", "Z")], *self.labels_to(0.3, keep=("E", "Z")),
                      Indicate(self.labs["Z"], color=BLUE, scale_factor=1.4),
                      run_time=beat.until("E", offset=-0.1, min_time=0.6))
            # ... as much as E: the one price line both pay
            self.play(Indicate(self.labs["E"], color=BLUE, scale_factor=1.4),
                      Indicate(self.avg_line, color=INK, scale_factor=1.0), flag(self.avg_num),
                      run_time=0.8)
            # real widths; E and Z stay the only bright columns, and Z keeps a label of its
            # own (its column is a hairline, too narrow for an axis letter)
            tgt = layout(ALPHA, P, {s: H0 for s in ALPHA})
            for s in ALPHA:
                if s not in ("E", "Z"):
                    tgt[s].set_fill(opacity=0.25)
            z_x = tgt["Z"].get_center()[0]
            z_lab = glyph("Z", 24).move_to([z_x, LAB_Y, 0])
            self.play(*[Transform(self.cols[s], tgt[s]) for s in ALPHA],
                      FadeIn(self.x_ticks), FadeIn(self.x_title), FadeIn(z_lab),
                      FadeIn(self.cite_br),
                      run_time=beat.until("turns", offset=0.0, end=True, min_time=0.8))
            # each share sits on a short grey leader above its own column
            top = cy(H0)
            row_y = top + 0.68
            e_x = self.cols["E"].get_center()[0]
            e_pct = MathTex(r"10.3\%", font_size=36, color=BLUE).move_to([e_x, row_y, 0])
            z_pct = MathTex(r"0.08\%", font_size=36, color=BLUE).move_to([z_x, row_y, 0])
            leads = VGroup(*[Line([x, top + 0.07, 0], [x, row_y - 0.3, 0], color=GRAY,
                                  stroke_width=2) for x in (e_x, z_x)])
            times = MathTex(r"\times 130", font_size=40, color=BLUE)
            times.move_to([(e_pct.get_right()[0] + z_pct.get_left()[0]) / 2, row_y, 0])
            self.play(FadeIn(e_pct, shift=0.1 * UP), FadeIn(z_pct, shift=0.1 * UP),
                      Create(leads), run_time=beat.until("hundred", offset=-0.1, min_time=0.4))
            self.play(GrowFromCenter(times), run_time=beat.until("thirty", end=True, min_time=0.6))
        self.pcts = VGroup(e_pct, z_pct, leads, times, z_lab)

    # ============================================================== 5a split probability
    def split_probability(self):
        cum5 = sum(P[s] for s in ORDER[:5])
        cut = Line([cx(cum5), Y0, 0], [cx(cum5), cy(H0) + 0.45, 0], color=YELLOW,
                   stroke_width=4).set_z_index(4)
        brace = BraceBetweenPoints([cx(0), cy(H0) + 0.12, 0], [cx(cum5), cy(H0) + 0.12, 0],
                                   direction=UP, color=BLUE)
        half = MathTex(r"48\%", font_size=36, color=BLUE).next_to(brace, UP, buff=0.16)
        with self.narrate("Instead, split the probability, not the alphabet: is it a space, E, T, "
                          "A or O? That's nearly half.") as beat:
            # Shannon's band is not discussed until 'four times': dim it to 40 %
            self.play(FadeOut(self.pcts), *self.labels_to(0.0),
                      *[self.cols[s].animate.set_fill(opacity=0.85) for s in ALPHA],
                      self.band_fill.animate.set_fill(opacity=0.11),
                      self.band_edges.animate.set_stroke(opacity=0.4),
                      self.band_lab.animate.set_opacity(0.4), run_time=0.5)
            # the re-sort pours each column from its old slot into its new one: the bar
            # stays one solid 0..100 % block in every frame
            ghosts, anims = tile_columns(self.cols, ALPHA, ORDER, P, {s: H0 for s in ALPHA}, UNIT)
            self.add(*ghosts.values())
            self.bring_to_front(self.x_axis)
            self.play(*anims, run_time=beat.until("is", offset=-0.6, min_time=1.5),
                      rate_func=linear)
            self.remove(*ghosts.values())
            clean = layout(ORDER, P, {x: H0 for x in ALPHA})
            for s in ALPHA:                     # rebuild clean rectangles in the new layout
                self.cols[s].become(clean[s])
            self.play(*self.labels_to(1.0), run_time=0.4)
            beat.wait_until("space", offset=-0.15)
            self.play(outline_flash([self.cols[s] for s in ORDER[:5]], lag=0.45,
                                    run_time=beat.until("O", offset=0.45, end=True, min_time=1.2)))
            beat.wait_until("nearly", offset=-0.15)
            self.play(Create(cut), GrowFromCenter(brace), FadeIn(half, shift=0.1 * UP),
                      run_time=1.0)
        self.half = VGroup(cut, brace, half)

    # ============================================================== 5b doublings
    def doublings(self):
        def strip(y, s, tracker):
            frame = Rectangle(width=SW, height=0.34, stroke_color=GRAY, stroke_width=2)
            frame.move_to([SX0 + SW / 2, y, 0])
            piece = Rectangle(width=SW * P[s], height=0.34, stroke_width=0, fill_color=BLUE,
                              fill_opacity=0.85).move_to([SX0 + SW * P[s] / 2, y, 0])

            def upd(m):
                w = SW * min(1.0, P[s] * 2 ** tracker.get_value())
                m.stretch_to_fit_width(max(w, 0.002))
                m.move_to([SX0 + max(w, 0.002) / 2, y, 0])
            num = DecimalNumber(0, num_decimal_places=1, font_size=36, color=YELLOW)
            num.add_updater(lambda m: m.set_value(tracker.get_value()).move_to([CNT_X, y, 0]))
            name = glyph(s, 30).move_to([SX0 - 0.35, y, 0])
            return frame, piece, upd, num, name

        kE, kZ = ValueTracker(0), ValueTracker(0)
        yE, yZ = STRIP_YE, STRIP_YZ
        fE, pE, uE, nE, lE = strip(yE, "E", kE)
        fZ, pZ, uZ, nZ, lZ = strip(yZ, "Z", kZ)
        head = text("doublings", size=26, color=GRAY).move_to([CNT_X, STRIP_HEAD_Y, 0])
        left_lab = text("what's still possible", size=26, color=GRAY)
        left_lab.move_to([0, STRIP_HEAD_Y, 0]).align_to(fE, LEFT)
        e_share = MathTex(r"10\%", font_size=30, color=BLUE)
        # rescale: the chart steps back (smaller unit, 30 %) to free the band above it
        old_cy = {v: cy(v) for v in (5, H0, YTOP0, LO, HI, (LO + HI) / 2)}
        set_unit(UNIT_B)
        tgt = layout(ORDER, P, {s: H0 for s in ALPHA})
        for s in ALPHA:
            if s != "E":
                tgt[s].set_fill(opacity=0.26)
        title_to = self.y_title.copy().next_to([X0, cy(YTOP0), 0], UP, buff=0.2).align_to(self.y_title, LEFT)
        rescale = [*[Transform(self.cols[s], tgt[s]) for s in ALPHA],
                   self.y_axis.animate.put_start_and_end_on([X0, Y0, 0], [X0, cy(YTOP0), 0]),
                   self.ytick[5].animate.shift(UP * (cy(5) - old_cy[5])).set_opacity(0.3),
                   self.ytick[0].animate.set_opacity(0.3),
                   # the dimmed chart is not read while the strips work: its title steps out,
                   # and everything except E (the strip's referent) drops to 30 %
                   self.y_title.animate.move_to(title_to).set_opacity(0),
                   *self.labels_to(0.3, keep=("E",)),
                   self.x_ticks.animate.set_opacity(0.3), self.x_title.animate.set_opacity(0.3),
                   self.avg_line.animate.shift(UP * (cy(H0) - old_cy[H0])).set_stroke(opacity=0.3),
                   self.avg_num.animate.move_to([COL_A, cy(H0), 0]).set_opacity(0.3),
                   self.band_fill.animate.stretch_to_fit_height(UNIT * (HI - LO))
                   .move_to([X0 + W / 2, cy((LO + HI) / 2), 0]).set_fill(opacity=0.08),
                   self.band_edges[0].animate.shift(UP * (cy(LO) - old_cy[LO])).set_stroke(opacity=0.3),
                   self.band_edges[1].animate.shift(UP * (cy(HI) - old_cy[HI])).set_stroke(opacity=0.3),
                   self.band_lab.animate.move_to(self.place_band_lab(self.band_lab.copy()))
                   .set_opacity(0.3)]
        with self.narrate("E starts near a tenth. Each ideal answer keeps half the probability, "
                          "so E's share doubles. Three point three doublings fill the "
                          "bar.") as beat:
            # the chart steps back (30 %) while the strips work above its axis
            self.play(FadeOut(self.half), *rescale, run_time=0.9)
            self.play(Create(fE), FadeIn(lE), FadeIn(left_lab),
                      TransformFromCopy(self.cols["E"], pE), run_time=0.9)
            e_share.next_to(pE, RIGHT, buff=0.15)
            self.play(FadeIn(e_share), FadeIn(head), FadeIn(nE), run_time=0.6)
            nE.update()
            beat.wait_until("keeps", offset=-0.2)
            mid = SX0 + SW / 2
            cutl = Line([mid, yE - 0.25, 0], [mid, yE + 0.25, 0], color=YELLOW, stroke_width=4)
            shade = Rectangle(width=SW / 2, height=0.34, stroke_width=0, fill_color=GRAY,
                              fill_opacity=0.35).move_to([mid + SW / 4, yE, 0])
            self.play(Create(cutl), FadeIn(shade), FadeOut(e_share),
                      run_time=beat.until("doubles", offset=-0.3, min_time=0.8))
            pE.add_updater(uE)
            self.play(kE.animate.set_value(1), cutl.animate.move_to([SX1, yE, 0]),
                      shade.animate.stretch_to_fit_width(0.01).move_to([SX1, yE, 0]),
                      run_time=1.0, rate_func=SMOOTH)
            self.play(FadeOut(cutl), FadeOut(shade), run_time=0.4)
            beat.wait_until("Three", offset=-0.1)
            self.play(kE.animate.set_value(-math.log2(P["E"])),
                      run_time=beat.until("fill", offset=0.3, min_time=1.6), rate_func=LINEAR)
            pE.clear_updaters()

        # Z's starting share, named under its sliver (the sliver itself is ~1 px wide)
        z_one = MathTex(r"1/1260", font_size=36, color=BLUE)
        z_one.next_to(fZ, DOWN, buff=0.16).align_to(fZ, LEFT)
        with self.narrate("Z, one in twelve hundred sixty, needs ten point three.") as beat:
            # the strip, Z's sliver and its share arrive together; the share is in by "one in"
            self.play(Create(fZ), FadeIn(lZ), TransformFromCopy(self.cols["Z"], pZ),
                      self.cols["Z"].animate.set_fill(opacity=0.85), FadeIn(nZ),
                      FadeIn(z_one, shift=0.1 * UP, rate_func=lambda t: smooth(max(0.0, (t - 0.35) / 0.65))),
                      run_time=beat.until("one in", offset=0.15, min_time=0.8))
            # the doublings start on "twelve" and land on 10.3 as "ten point three" begins
            # (the counter is time-like: linear); the starting share steps back to 40 % once
            # the counter has passed 1 (it is then no longer the bar's share)
            beat.wait_until("twelve", offset=-0.05)
            pZ.add_updater(uZ)
            kz_end = -math.log2(P["Z"])
            past1 = 1.0 / kz_end
            self.play(kZ.animate(rate_func=linear).set_value(kz_end),
                      z_one.animate(rate_func=lambda t: smooth(float(np.clip((t - past1) / 0.15, 0, 1))))
                      .set_opacity(0.4),
                      run_time=beat.until("ten", offset=0.0, min_time=1.6))
            pZ.clear_updaters()
            self.play(flag(nZ), run_time=0.8)
        nE.clear_updaters()
        nZ.clear_updaters()
        self.strips = VGroup(fE, pE, lE, fZ, pZ, lZ, z_one)
        self.nE, self.nZ = nE, nZ

        # formula: p * 2^k = 1  ->  2^k = 1/p  ->  k = log2(1/p), one legal step at a time,
        # built centre stage (the strips step up and back to make room; counters stay bright)
        eq_at = np.array([EQ_X, EQ_Y, 0])            # every version keeps its '=' here
        f1 = MathTex("p", r"\cdot", "2^{k}", "=", "1", font_size=EQ_SIZE)
        f1[0].set_color(BLUE)
        f1[2].set_color(YELLOW)
        f1.shift(eq_at - f1[3].get_center())
        mid = MathTex("2^{k}", "=", r"\frac{1}{p}", font_size=EQ_SIZE)
        mid[0].set_color(YELLOW)
        mid.shift(eq_at - mid[1].get_center())
        m_rest = sorted(mid[2].submobjects, key=lambda m: -m.get_center()[1])
        m_one, m_bar, m_p = m_rest
        m_p.set_color(BLUE)
        f2 = log_formula("k", "=", r"\log_2\!\frac{1}{p}", size=EQ_SIZE)
        f2[0].set_color(YELLOW)                # k counts questions: yellow, like its counters
        f2.shift(eq_at - f2[1].get_center())
        fg = frac_glyphs(f2[2])
        full = VGroup(pE, pZ)
        lift = UP * STRIP_LIFT
        bodies = [fE.animate.shift(lift).set_stroke(opacity=0.4),
                  fZ.animate.shift(lift).set_stroke(opacity=0.4),
                  pE.animate.shift(lift).set_fill(opacity=0.34),
                  pZ.animate.shift(lift).set_fill(opacity=0.34),
                  lE.animate.shift(lift).set_opacity(0.4), lZ.animate.shift(lift).set_opacity(0.4),
                  z_one.animate.shift(lift).set_opacity(0.3),
                  nE.animate.shift(lift), nZ.animate.shift(lift),
                  FadeOut(head, shift=lift), FadeOut(left_lab, shift=lift)]
        with self.narrate("A character with probability p needs k questions, where "
                          "p times two to the k equals one. [pause 1.5] So two to the k equals "
                          "one over p, and k equals log base two of one over p.") as beat:
            # the strips step up and back (40 %): the formula is the focus from here
            self.play(*bodies, run_time=beat.until("probability", offset=-0.1, min_time=0.8))
            self.play(TransformFromCopy(self.cols["E"], f1[0]), run_time=1.0)
            beat.wait_until("k", offset=-0.1)
            self.play(flag(self.nE), flag(self.nZ), run_time=0.8)
            beat.wait_until("times", offset=-0.1)
            # 2^k IS the doublings counter: a copy leaves the counter to the right (never over
            # it), passes right of and under Z's 10.3, and cross-fades into 2^k on the way
            a, b = self.nE.get_center(), f1[2].get_center()
            z = self.nZ.get_center()
            path = route([(a[0], a[1]), (a[0] + 0.75, a[1] + 0.2), (z[0] + 0.95, z[1] + 0.05),
                          (z[0] + 0.55, z[1] - 0.6), (b[0] + 1.3, b[1] + 0.12), (b[0], b[1])])
            pk, pk_anim = fly_morph(self.nE, f1[2], path, rate=smooth, fade=(0.3, 0.8))
            self.add(pk)
            self.play(Write(f1[1], run_time=0.4), pk_anim,
                      run_time=beat.until("equals", offset=-0.15, min_time=1.2))
            self.remove(pk)
            self.add(f1[2])
            beat.wait_until("equals", offset=-0.1)
            self.play(Write(f1[3:]), run_time=0.7)
            # '= 1': the whole bar, which both strips now fill
            self.play(outline_flash(full), flag(f1[4]), run_time=0.9)
            # hold the complete equation (pause in the narration) before any glyph moves
            beat.wait_until("So two", offset=0.15)
            # step 1: divide by p -- p dips under the '=' and lands under the 1
            self.play(ReplacementTransform(f1[2], mid[0]), ReplacementTransform(f1[3], mid[1]),
                      ReplacementTransform(f1[4], m_one),
                      ReplacementTransform(f1[0], m_p, path_arc=0.6 * PI),
                      FadeOut(f1[1]), GrowFromCenter(m_bar),
                      run_time=beat.until("over p", offset=0.0, end=True, min_time=1.0))
            beat.wait_until("and k", offset=0.0)
            # step 2: take log base 2.  The fraction slides right to make room; the 2 dips
            # UNDER the '=' (a downward arc, clear of the k and the '=') into the base's
            # subscript; only once it has passed does k drop out of the exponent into its
            # place, and 'log' is written 0.3 s after the 2 has landed
            rt2 = beat.until("two", occurrence=3, end=True, offset=0.15, min_time=2.2)

            a2, b2 = mid[0][0].get_center(), fg["two"].get_center()
            two_path = route([(a2[0], a2[1]), (a2[0] + 0.3, a2[1] - 0.36), (0.0, 0.27),
                              (b2[0] - 0.45, b2[1] - 0.3), (b2[0], b2[1])])
            # the 2 flies as a rigid top-level copy (a path_arc would rotate the glyph mid-way),
            # and is removed once f2 stands; it lands at LaTeX's own subscript place
            two = mid[0][0].copy()
            self.add(two)
            self.remove(mid[0][0])
            self.allow_overlap(two, reason="the 2 of 2^k lands as the subscript of log2, at LaTeX's "
                               "own spacing from the fraction bar (the final formula's layout)")

            def win(a, b):                    # this part of the move, in seconds of rt2
                a, b = a / rt2, min(1.0, b / rt2)
                return lambda t: smooth(float(np.clip((t - a) / max(b - a, 1e-6), 0, 1)))
            self.play(ReplacementTransform(mid[1], f2[1]),
                      ReplacementTransform(m_one, fg["one"], rate_func=win(0.0, 0.95)),
                      ReplacementTransform(m_bar, fg["bar"], rate_func=win(0.0, 0.95)),
                      ReplacementTransform(m_p, fg["p"], rate_func=win(0.0, 0.95)),
                      fly(two, fg["two"], two_path, rate=win(0.05, 1.15)),
                      ReplacementTransform(mid[0][1], f2[0], rate_func=win(0.6, 1.3)),
                      Write(fg["log"], rate_func=win(1.45, 2.2)), run_time=rt2)
            self.remove(f1, mid, two, *mid.get_family())
            self.add(f2)                       # one clean formula object from here on
            # k is the counter: 3.3 for E, 10.3 for Z
            self.play(flag(f2[0]), flag(self.nE), flag(self.nZ),
                      run_time=beat.until("over p", occurrence=2, end=True, min_time=0.8))
        self.f2 = f2

    # ============================================================== 5c skyline
    def skyline(self):
        # where the formula row will sit (log part fixed while k becomes 'average')
        f3 = log_formula(r"\text{average}", "=", r"\sum", "p", r"\log_2\!\frac{1}{p}", size=FS_TOP)
        f3.move_to([-0.6, TOP_Y, 0])
        f2_top = self.f2.copy().scale(FS_TOP / EQ_SIZE)
        f2_top.shift(f3[4].get_center() - f2_top[2].get_center())

        y_ext = Line([X0, cy(YTOP0), 0], [X0, cy(YMAX), 0], color=GRAY, stroke_width=2.5)
        t10 = self.make_ytick(10)
        title_top = self.y_title.copy().next_to(y_ext.get_top(), UP, buff=0.2).align_to(self.y_title, LEFT)
        self.ytick[10] = t10
        self.y_ticks = VGroup(*self.ytick.values())

        ghost_lab = MathTex("4.75", font_size=30, color=GRAY).move_to([X0 + 0.5, cy(H0) + 0.3, 0])
        self.ghost, self.ghost_lab = self.avg_line, ghost_lab
        e_cost = -math.log2(P["E"])

        # inset: the four rarest letters, widths x30, heights true.  It stands clear of the
        # main axis in its own frame, on its own baseline, with dashed leaders from the four
        # hairlines it magnifies.
        inset, xl = VGroup(), INSET_X0
        inset_cols = {}
        for s in TAIL:
            w = W * P[s] * ZOOM
            inset_cols[s] = column(xl, w, UNIT * cost(P[s]))
            inset.add(inset_cols[s])
            xl += w + INSET_GAP
        xl -= INSET_GAP
        inset_base = Line([INSET_X0 - 0.04, Y0, 0], [xl + 0.04, Y0, 0], color=GRAY, stroke_width=2.5)
        inset_labs = VGroup(*[glyph(s, 20).move_to([inset_cols[s].get_center()[0], LAB_Y, 0])
                              for s in TAIL])
        for m in inset_labs:
            m.ss_role = "tick"                 # the inset's axis letters (BAR tick floor)
        zoom_lab = text(f"×{ZOOM} wide", size=26, color=GRAY)
        z_cost = MathTex(f"{cost(P['Z']):.1f}", font_size=30, color=YELLOW)
        z_cost.next_to(inset_cols["Z"], UP, buff=0.16).align_to([6.2, 0, 0], RIGHT)
        f_top, f_bot, f_right = z_cost.get_top()[1] + 0.16, LAB_Y - 0.19, xl + 0.1
        frame = Polygon([INSET_FRAME_X0, f_bot, 0], [f_right, f_bot, 0], [f_right, f_top, 0],
                        [INSET_FRAME_X0, f_top, 0], color=GRAY, stroke_width=1.5)
        zoom_lab.move_to([(INSET_FRAME_X0 + f_right) / 2, XTITLE_Y, 0])
        tail_w = W * sum(P[s] for s in TAIL)
        src = Polygon([X1 - tail_w - 0.04, Y0 - 0.04, 0], [X1 + 0.04, Y0 - 0.04, 0],
                      [X1 + 0.04, cy(10.4) + 0.08, 0], [X1 - tail_w - 0.04, cy(10.4) + 0.08, 0],
                      color=GRAY, stroke_width=1.5)
        leaders = VGroup(DashedLine([X1 + 0.04, cy(10.4) + 0.08, 0], [INSET_FRAME_X0, f_top, 0],
                                    dash_length=0.07),
                         DashedLine([X1 + 0.04, Y0 - 0.04, 0], [INSET_FRAME_X0, f_bot, 0],
                                    dash_length=0.07)).set_stroke(GRAY, 1.5)
        self.inset = VGroup(inset, inset_base, inset_labs, zoom_lab, z_cost, frame, src, leaders)

        e_lab = MathTex(f"{e_cost:.1f}", font_size=30, color=YELLOW)
        with self.narrate("Now make each character's cost its height.") as beat:
            # the strips and counters clear first, so the formula's path up is empty
            self.play(FadeOut(self.strips), FadeOut(self.nZ), FadeOut(self.nE), run_time=0.4)
            self.play(*[self.cols[s].animate.set_fill(opacity=0.85) for s in ALPHA],
                      Transform(self.f2, f2_top), Create(y_ext), FadeIn(t10),
                      self.y_title.animate.move_to(title_top),
                      # the chart comes back to full strength
                      *self.labels_to(1.0), self.x_ticks.animate.set_opacity(1),
                      self.x_title.animate.set_opacity(1),
                      self.ytick[0].animate.set_opacity(1), self.ytick[5].animate.set_opacity(1),
                      self.band_fill.animate.set_fill(opacity=0.11),
                      self.band_edges.animate.set_stroke(opacity=0.4),
                      self.band_lab.animate.set_opacity(0.4),
                      self.avg_line.animate.set_color(GRAY).set_stroke(width=3, opacity=1),
                      FadeOut(self.avg_num), FadeIn(ghost_lab), run_time=1.0)
            self.y_axis.put_start_and_end_on([X0, Y0, 0], [X0, cy(YMAX), 0])
            self.remove(y_ext)
            self.avg_line.set_z_index(2)
            # E's 3.3 doublings become its height
            e_lab.move_to([self.cols["E"].get_center()[0], cy(e_cost) + 0.27, 0])
            self.morph(ORDER, P, {s: cost(P[s]) for s in ALPHA},
                       run_time=max(1.4, beat.remaining() - 0.1),
                       extra=[self.y_title.animate.set_opacity(1),
                              FadeIn(e_lab, rate_func=lambda t: smooth(max(0.0, (t - 0.6) / 0.4)))])

        sweep = Line([X0, Y0 + 0.02, 0], [X1, Y0 + 0.02, 0], color=BLUE,
                     stroke_width=9).set_z_index(5)
        p_seg = Line(f3[3].get_left(), f3[3].get_right(), color=BLUE, stroke_width=4)
        p_seg.move_to(f3[3].get_bottom()).set_stroke(opacity=0.0).set_z_index(5)
        # the crux: spoken slower (0.80), with a breath after "one" and after "average cost"
        with self.narrate("The widths add to one, [pause 0.25] so the area is the average cost. "
                          "[pause 0.5] Pour the skyline flat, and its height is that average.",
                          speed=0.80) as beat:
            # E's counter has done its job; the hairlines at 100 % get their magnified inset
            # while the sweep adds the widths up (even the ones too thin to see)
            self.play(FadeOut(e_lab), Create(src), Create(leaders), Create(frame),
                      *[TransformFromCopy(self.cols[s], inset_cols[s]) for s in TAIL],
                      FadeIn(inset_base), FadeIn(inset_labs), FadeIn(zoom_lab),
                      FadeIn(z_cost, shift=0.1 * UP), Create(sweep),
                      run_time=beat.until("to one", offset=0.0, end=True, min_time=1.0))
            self.play(flag(self.x_ticks[-1][1], color=BLUE), outline_flash(list(inset)), run_time=0.45)
            beat.wait_until("area", offset=-0.2)
            # each term arrives from what it measures: p from the widths, the cost from k
            self.play(*[c.animate(rate_func=there_and_back).set_fill(YELLOW, opacity=0.85)
                        for c in self.colg],
                      # k leaves before the sum is written where it stood (never superimposed),
                      # and the '=' slides only once k is gone
                      FadeOut(self.f2[0], shift=0.15 * UP, rate_func=lambda t: smooth(min(1.0, t / 0.28))),
                      FadeIn(f3[0], shift=0.15 * UP, rate_func=lambda t: smooth(max(0.0, (t - 0.4) / 0.6))),
                      ReplacementTransform(self.f2[1], f3[1],
                                           rate_func=lambda t: smooth(max(0.0, (t - 0.28) / 0.72))),
                      ReplacementTransform(self.f2[2], f3[4]),
                      Write(f3[2], rate_func=lambda t: smooth(max(0.0, (t - 0.3) / 0.7))),
                      # the widths (the blue sweep along the axis) gather into p: the line
                      # contracts onto the p's place and the p appears there
                      Transform(sweep, p_seg, rate_func=smooth),
                      FadeIn(f3[3], rate_func=lambda t: smooth(max(0.0, (t - 0.55) / 0.45))),
                      FadeOut(self.inset), run_time=1.4)
            for c in self.colg:
                c.set_fill(BLUE, opacity=0.85)
            self.remove(self.f2, sweep)
            self.add(f3)
            beat.wait_until("Pour", offset=-0.35)
            self.hide_labels()
            self.pour(P, {s: cost(P[s]) for s in ALPHA},
                      run_time=beat.until("height", offset=-0.15, min_time=1.6))
            line, num = self.level_marks(H1)
            self.play(Create(line), FadeIn(num, shift=0.1 * LEFT), run_time=0.8)
        self.f3, self.level_line, self.level_num = f3, line, num

    # ============================================================== 5d entropy
    def entropy(self):
        f4 = log_formula("H", "=", r"\sum", "p", r"\log_2\!\frac{1}{p}", size=FS_TOP)
        f4[0].set_color(YELLOW)
        eq_val = DecimalNumber(H1, num_decimal_places=2, font_size=FS_TOP, color=YELLOW)
        eq_tail = VGroup(MathTex("=", font_size=FS_TOP), eq_val, MathTex(r"\text{bits}", font_size=FS_TOP))
        eq_tail.arrange(RIGHT, buff=0.18)
        VGroup(f4, eq_tail).arrange(RIGHT, buff=0.22).move_to([-0.35, TOP_Y, 0])
        new_title = text("bits", size=LABEL - 2, color=GRAY).move_to(self.y_title, aligned_edge=LEFT)
        with self.narrate("Shannon called it entropy, in bits: one bit per yes-or-no answer. For "
                          "English letters: four point one one. [pause 0.8]") as beat:
            beat.wait_until("entropy", offset=-0.35)
            # 'average' and 'H' share no glyphs: the word steps out before the symbol steps in
            # (no frame stacks the two)
            # and the rest of the formula only slides left once the word is (almost) gone
            self.play(FadeOut(self.f3[0], shift=0.15 * UP, rate_func=lambda t: smooth(min(1.0, t / 0.4))),
                      *[ReplacementTransform(self.f3[i], f4[i],
                                             rate_func=lambda t: smooth(max(0.0, (t - 0.32) / 0.68)))
                        for i in range(1, 5)],
                      FadeIn(f4[0], shift=0.15 * UP, rate_func=lambda t: smooth(max(0.0, (t - 0.55) / 0.45))),
                      run_time=0.95)
            self.remove(self.f3)
            self.add(f4)
            beat.wait_until("bits", offset=-0.15)
            self.play(LaggedStart(FadeOut(self.y_title, shift=0.15 * UP),
                                  FadeIn(new_title, shift=0.15 * UP), lag_ratio=0.55), run_time=0.9)
            self.y_title = new_title
            beat.wait_until("answer", offset=-0.3)
            self.play(Indicate(self.level_line, color=INK, scale_factor=1.0), flag(self.level_num),
                      run_time=0.9)
            # the level's value is copied into the equation: the copy leaves the gutter to the
            # right and rises outside the chart, so it never crosses the 4.75 line
            beat.wait_until("English", offset=-0.1)
            a0, b0, y0 = self.level_num.get_center(), eq_val.get_center(), self.level_num.get_y()
            path = route([(a0[0], a0[1]), (COL_A + 0.75, y0 + 0.2), (COL_A + 0.95, y0 + 0.9),
                          (COL_A + 0.6, b0[1] - 0.62), (3.3, b0[1] - 0.64), (b0[0] + 0.1, b0[1] - 0.6),
                          (b0[0], b0[1])])
            cp, cp_anim = fly_morph(self.level_num, eq_val, path, rate=smooth, fade=(0.0, 0.001))
            self.add(cp)
            self.play(cp_anim, FadeIn(eq_tail[0], rate_func=lambda t: smooth(max(0.0, (t - 0.5) / 0.5))),
                      FadeIn(eq_tail[2], rate_func=lambda t: smooth(max(0.0, (t - 0.5) / 0.5))),
                      run_time=beat.until("four", offset=0.45, min_time=1.3))
            self.remove(cp)
            self.add(eq_val)
        self.f4, self.eq_tail, self.eq_val = f4, eq_tail, eq_val
        self.eq_eq, self.eq_bits = eq_tail[0], eq_tail[2]
        self.eq_y, self.bits_y = eq_val.get_y(), eq_tail[2].get_y()

        with self.narrate("That beats four point seven five, but it's four times Shannon's "
                          "estimate: it ignores what came before.", gap=self.TURN_GAP) as beat:
            # the failure metric from the fail beat, measured again: the gap to Shannon's ~1
            # stands at 4.75 (3.75 extra), then shrinks to the new level (3.11 extra)
            top, garrow, glab = self.gap_meter(clear=lambda: cy(H1))
            beat.wait_until("beats", offset=-0.1)
            # the meter grows from Shannon's ~1 up to the ghost 4.75, its reading counting up
            # with the arrow (0 -> 3.75 extra)
            self.add(garrow, glab)
            self.play(Indicate(VGroup(self.ghost, self.ghost_lab), color=INK, scale_factor=1.0),
                      self.band_fill.animate.set_fill(opacity=0.28),
                      self.band_edges.animate.set_stroke(opacity=1.0),
                      self.band_lab.animate.set_opacity(1.0),
                      top.animate.set_value(H0), run_time=0.9)
            # 3.75 extra stands while 'four point seven five' is spoken, then shrinks to 3.11
            beat.wait_until("five", offset=-0.05)
            self.play(top.animate.set_value(H1), FadeOut(self.ghost), FadeOut(self.ghost_lab),
                      run_time=beat.until("four times", offset=-0.15, min_time=0.8))
            glab.clear_updaters()            # the reading is settled (3.11): flag its text only
            self.play(Indicate(self.band_edges, color=GREEN, scale_factor=1.0),
                      flag(self.band_lab, color=GREEN), flag(VGroup(glab[1], glab[2])),
                      flag(self.level_num), run_time=0.9)
            # it ignores what came before: the stack rises back into the skyline, each
            # character priced on its own, and the context row flashes on "came before"
            beat.wait_until("ignores", offset=-0.2)
            gone = lambda t: smooth(min(1.0, t / 0.3))
            self.unpour(P, {s: cost(P[s]) for s in ALPHA},
                        run_time=beat.until("came", offset=-0.1, min_time=0.8),
                        extra=[FadeOut(garrow, rate_func=gone), FadeOut(glab, rate_func=gone)])
            garrow.clear_updaters()
            glab.clear_updaters()
            self.play(pflash(VGroup(self.lead, self.hidden), scale=1.0), *self.labels_to(1.0),
                      run_time=0.9)

    def row_now(self) -> list:
        """The text-so-far row as it stands now (only the pieces still on screen)."""
        on = set(id(m) for m in self.get_mobject_family_members())
        return [m for m in [self.lead, *self.hidden, *self.th, self.qbox, self.qmark,
                            *getattr(self, "live_row", [])] if id(m) in on]

    def gap_meter(self, x: float = 0.0, ymap=None, base: float = 1.0, clear=None):
        """The fail beat's yellow double arrow, back as a live meter: from Shannon's ~1 up to
        the current level, with 'N extra' riding on its top.  It starts at zero length (the
        reading is 0.00 and both are invisible): animate the tracker up to the level and the
        arrow grows while the reading counts up with it, so the number never leads the arrow.
        `ymap` maps bits to scene y (the main chart's cy by default).  With `clear` (a function
        giving a y), the reading stays hidden until it has risen clear of that height (the top
        of the filled stack it grows through), so its backing never shows over the bars.
        Returns (tracker, arrow, label); add arrow and label to the scene, then animate."""
        ymap = ymap or cy
        top = ValueTracker(base)

        def make_arrow():
            y0 = ymap(base)
            ln = ymap(top.get_value()) - y0
            a = DoubleArrow([x, y0, 0], [x, y0 + max(ln, 0.06), 0], buff=0, color=YELLOW,
                            stroke_width=4, tip_length=0.16,
                            max_tip_length_to_length_ratio=0.25).set_z_index(5)
            return a.set_opacity(float(np.clip((ln - 0.04) / 0.2, 0, 1)))
        arrow = always_redraw(make_arrow)
        num = DecimalNumber(0.0, num_decimal_places=2, font_size=36, color=YELLOW)
        word = MathTex(r"\text{extra}", font_size=36, color=YELLOW)
        VGroup(num, word).arrange(RIGHT, buff=0.15)
        # an opaque backing: while the meter shrinks, the reading rides in FRONT of any level
        # line it passes (never struck through by a dashed line)
        bg = BackgroundRectangle(VGroup(num, word), color=BG, fill_opacity=1.0, buff=0.07)
        lab = VGroup(bg, num, word).set_z_index(6)
        bg.set_z_index(5)

        def upd(m):
            v = top.get_value()
            num.set_value(max(0.0, v - base))
            num.set_z_index(6)              # set_value rebuilds the digits (at z 0, under bg)
            word.next_to(num, RIGHT, buff=0.15)
            bg.move_to(VGroup(num, word))
            m.move_to([x, ymap(v) + 0.36, 0])
            o = float(np.clip((ymap(v) - ymap(base) - 0.04) / 0.22, 0, 1))
            if clear is not None:
                o = min(o, float(np.clip((m.get_bottom()[1] - clear()) / 0.12, 0, 1)))
            num.set_opacity(o)
            word.set_opacity(o)
            bg.set_fill(opacity=o)
        lab.add_updater(upd)
        upd(lab)
        return top, arrow, lab

    # ============================================================== 6 context
    def eq_unknown(self):
        """While a new context is being priced, the equation's value is '?', never a stale
        number.  Returns the animations."""
        q = MathTex("?", font_size=FS_TOP, color=YELLOW)
        q.next_to(self.eq_eq, RIGHT, buff=0.18).set_y(self.eq_y)
        # the old value leaves before the '?' arrives: the two never share the slot
        anims = [FadeOut(self.eq_val, shift=0.15 * UP, rate_func=lambda t: smooth(min(1.0, 2 * t))),
                 FadeIn(q, shift=0.15 * UP, rate_func=lambda t: smooth(max(0.0, 2 * t - 1))),
                 self.eq_bits.animate.next_to(q, RIGHT, buff=0.18).set_y(self.bits_y)]
        self.eq_val = q
        return anims

    def eq_known(self, value: float, source: VMobject, via=None):
        """The newborn level value is copied into the equation's slot.  With `via` (waypoints)
        the copy flies along that route instead of a straight line.  Returns (anims, done):
        call done() after playing."""
        v = DecimalNumber(value, num_decimal_places=2, font_size=FS_TOP, color=YELLOW)
        v.next_to(self.eq_eq, RIGHT, buff=0.18).set_y(self.eq_y)
        # 'bits' steps aside first (and the '?' leaves), then the value flies in: the arriving
        # number never runs into 'bits'
        first = lambda t: smooth(min(1.0, t / 0.35))
        after = lambda t: rate_functions.ease_out_cubic(max(0.0, (t - 0.25) / 0.75))  # leaves fast
        a, b = source.get_center(), v.get_center()
        if via is None:
            # out of the gutter to the right, up outside the chart (right of every level label),
            # then left above the chart: the copy never sits on its source or crosses a label
            via = [(COL_A + 0.7, a[1] + 0.2), (COL_A + 0.88, a[1] + 0.9),
                   (COL_A + 0.88, b[1] - 0.95), (3.0, b[1] - 0.68)]
        # ... and the last leg rises straight into the slot, clear of 'bits'
        path = route([(a[0], a[1]), *via, (b[0] + 0.1, b[1] - 0.6), (b[0], b[1])])
        flyer, move = fly_morph(source, v, path, rate=lambda t: smooth(max(0.0, (t - 0.2) / 0.8)),
                                fade=(0.0, 0.001))
        self.add(flyer)
        anims = [move, FadeOut(self.eq_val, scale=0.6, rate_func=first),
                 self.eq_bits.animate(rate_func=first).next_to(v, RIGHT, buff=0.18).set_y(self.bits_y)]
        self.eq_val = v

        def done():
            if flyer is not None:
                self.remove(flyer)
                self.add(v)
        return anims, done

    def swap_title(self, new: Text, ctx_glyphs) -> tuple[list, callable]:
        """'share' stays put; only the tail changes, and the purple context letters fly in
        from the context boxes.  They travel over the row and down the right gutter, so
        they never cross a column, a tick label or the formula."""
        old = self.x_title
        anims, extra, flyers = [], [], []
        if old.text.startswith("share of"):                         # 'of text' -> 'after X'
            after = new[5:10]
            extra.append(after)
            # the old tail is gone before the new one arrives: never two words in one place
            anims += [FadeOut(old[5:], shift=0.12 * DOWN, rate_func=lambda t: smooth(min(1, 3 * t))),
                      FadeIn(after, shift=0.12 * DOWN,
                             rate_func=lambda t: smooth(min(1, max(0, 3 * t - 1))))]
        else:                                                       # 'after Q' -> 'after TH'
            anims += [FadeOut(old[10:], shift=0.12 * DOWN, rate_func=lambda t: smooth(min(1, 3 * t)))]
        n = len(ctx_glyphs)
        for i, g in enumerate(ctx_glyphs):
            c, tgt = g.copy(), new[10 + i]
            a, b = c.get_center(), tgt.get_center()
            lane = 6.15 - 0.36 * (n - 1 - i)                       # T inside, H outside
            path = route([(a[0], a[1]), (a[0] + 0.35, 3.66), (4.7, 3.68), (lane - 0.1, 3.15),
                          (lane, 1.6), (lane, -2.3), (lane - 0.45, b[1]), (b[0], b[1])])
            self.add(c)
            flyers.append(c)
            anims.append(fly(c, tgt, path))

        def done():
            # FadeOut of a slice splits `old` into loose glyphs in the scene: remove them all
            self.remove(old, *old.submobjects, *extra, *new.submobjects, *flyers)
            self.add(new)
            self.x_title = new
        return anims, done

    def tracking_brace(self, sym: str, y: float, tex: str):
        """A blue % label parked at a fixed height over a column, and a brace (fixed y) that
        grows WITH the column as it widens.  Returns (label, brace, animation): show the label
        first, then run the animation alongside the column's own."""
        br, lab = VMobject(), MathTex(tex, font_size=36, color=BLUE)
        y_lab = y + 0.8
        lab.move_to([self.cols[sym].get_x(), y_lab, 0])

        def upd(_g, _a):
            c = self.cols[sym]
            l, r = c.get_left()[0], c.get_right()[0]
            if r - l > 0.5:
                br.become(BraceBetweenPoints([l + 0.08, y, 0], [r - 0.08, y, 0], direction=UP,
                                             color=BLUE))
            br.set_opacity(float(np.clip((r - l - 0.6) / 1.2, 0, 1)))
            lab.move_to([(l + r) / 2, y_lab, 0])
        return lab, br, UpdateFromAlphaFunc(br, upd)

    def run_box(self):
        """The hidden slot widens into a real run of three (E _ O of THE OTHER, after T H),
        and the run's bill is laid out while the chart is out: the three letters, the two
        letters each is conditioned on, its probability given them (they multiply: 0.0329)
        and its cost log2(1/p) (they add: 4.93, the same as log2(1/0.0329)) -> 5 questions,
        and whole questions asked one letter at a time (1 + 1 + 4 = 6).
        Returns (back, wide, run_letters, ledger dict)."""
        sq = self.qbox
        back = sq.copy()
        n_run = len(RUN["letters"])
        wide = Rectangle(width=sq.width + (n_run - 1) * PITCH, height=sq.height, stroke_color=YELLOW,
                         stroke_width=4).move_to(sq, aligned_edge=LEFT)
        letters = VGroup()
        for k, r in enumerate(RUN["letters"]):
            x = sq.get_x() + PITCH * k
            g = glyph(r["ch"], 30, INK).move_to([x, sq.get_y() - (0.05 if r["ch"] == " " else 0), 0])
            letters.add(g)
        costs = [r["cost"] for r in RUN["letters"]]
        probs = [r["p"] for r in RUN["letters"]]
        whole = [math.ceil(c) for c in costs]
        assert sum(whole) == RUN["one_at_a_time"] and math.ceil(RUN["total"]) == RUN["questions"]
        # displayed values: probabilities to 3 significant figures, costs to 2 decimals.  Every
        # relation on screen holds for the DISPLAYED numbers: each cost is log2(1/p) of the p
        # above it, the p's multiply to the run's p, and both log2(1/p_run) and the sum of the
        # costs give the same total
        p_s = [f"{p:.3f}" for p in probs]                   # 0.683, 0.670, 0.072
        c_s = [f"{c:.2f}" for c in costs]                   # 0.55, 0.58, 3.80
        prod = float(np.prod([float(x) for x in p_s]))
        prod_s = f"{prod:.3g}"                              # 0.0329
        tot_s = f"{sum(float(x) for x in c_s):.2f}"         # 4.93
        for ps, cs in zip(p_s, c_s):
            assert f"{-math.log2(float(ps)):.2f}" == cs, (ps, cs)
        assert f"{-math.log2(float(prod_s)):.2f}" == tot_s and abs(float(prod_s) - prod) < 6e-5
        assert math.ceil(float(tot_s)) == RUN["questions"]
        self.run_disp = (p_s, c_s, prod_s, tot_s)
        # row P: the letters' probabilities multiply (blue); row A: their costs add up (yellow
        # = questions); row B: whole questions, one letter at a time (grey, the abandoned
        # way).  5 sits over 6.  Each letter has its own column (letter / context tag / p /
        # cost / whole question), wide enough for the tag.
        nr = n_run
        col_x = [LEDGER_X0 + 0.25 + LEDGER_DX * k for k in range(nr)]
        Pr = MathTex(*[x for ps in p_s for x in (ps, r"\times")][:-1], "=", prod_s, font_size=LEDGER_FS)
        for i in [*range(0, 2 * nr - 1, 2), 2 * nr]:
            Pr[i].set_color(BLUE)
        Pr.move_to([0, LEDGER_Y[2], 0])
        for k in range(nr):                                 # shift x only: baselines stay shared
            Pr[2 * k].set_x(col_x[k])
            if k < nr - 1:
                Pr[2 * k + 1].set_x(col_x[k] + LEDGER_DX / 2)
        ptail = VGroup(*Pr[2 * nr - 1:])
        ptail.shift(RIGHT * (Pr[2 * nr - 2].get_right()[0] + 0.3 - ptail.get_left()[0]))
        A = MathTex(*[x for cs in c_s for x in (cs, "+")][:-1], "=", tot_s,
                    r"\to", str(RUN["questions"]), font_size=LEDGER_FS)
        for i in [*range(0, 2 * nr + 1, 2), 2 * nr + 2]:
            A[i].set_color(YELLOW)
        A.move_to([0, LEDGER_Y[3], 0])
        for k in range(nr):
            A[2 * k].set_x(col_x[k])
            if k < nr - 1:
                A[2 * k + 1].set_x(col_x[k] + LEDGER_DX / 2)
        # the totals stand in one column: '=' under '=', 4.93 under 0.0329
        A[2 * nr - 1].set_x(Pr[2 * nr - 1].get_x())
        A[2 * nr].set_x(Pr[2 * nr].get_x())
        A[2 * nr + 1].next_to(A[2 * nr], RIGHT, buff=0.2).set_y(A[2 * nr - 1].get_y())
        A[2 * nr + 2].next_to(A[2 * nr + 1], RIGHT, buff=0.2).align_to(A[2 * nr], DOWN)
        A_unit = MathTex(r"\text{questions}", font_size=LEDGER_FS, color=YELLOW)
        A_unit.next_to(A, RIGHT, buff=0.2).align_to(A[2 * nr + 2], DOWN)
        # the run priced as ONE symbol: log2(1/p_run) -- the same 4.93 the costs add up to
        L = MathTex(r"\log_2\!\frac{1}{" + prod_s + "}", "=", tot_s, font_size=LEDGER_FS)
        L[0].set_color(YELLOW)
        for g in L[0].submobjects[4:]:                     # the denominator is a probability
            if g.get_y() < L[0].get_y() - 0.05:
                g.set_color(BLUE)
        L[2].set_color(YELLOW)
        L.next_to(Pr, RIGHT, buff=0.55)
        L.shift(UP * (Pr[2 * nr - 1].get_y() - L[1].get_y()))
        B = MathTex(*[x for w in whole for x in (str(w), "+")][:-1], "=", str(RUN["one_at_a_time"]),
                    font_size=LEDGER_FS, color=GRAY)
        for i in range(2 * nr - 1):                         # the terms sit under their costs
            B[i].move_to([A[i].get_x(), LEDGER_Y[4], 0])
        B[2 * nr - 1].move_to([A[2 * nr + 1].get_x(), LEDGER_Y[4], 0])   # '= 6' under '-> 5'
        B[2 * nr].move_to([A[2 * nr + 2].get_x(), LEDGER_Y[4], 0])
        B_lab = text("one at a time", size=28, color=GRAY)
        B_lab.next_to(B[2 * nr], RIGHT, buff=0.3).align_to(B[2 * nr], DOWN)
        head, tags = VGroup(), VGroup()
        for k, r in enumerate(RUN["letters"]):
            h = glyph(r["ch"], 30, INK).move_to([col_x[k], LEDGER_Y[0], 0])
            if r["ch"] == " ":
                h.shift(DOWN * 0.08)
            head.add(h)
            tags.add(self.ctx_tag(r["context"]).move_to([col_x[k], LEDGER_Y[1], 0]))
        # the two letters each cost is conditioned on, bracketed in the context row: T H for
        # E, H E for the space, E _ for O (one box to the right per letter)
        win_y = ROW_Y_TOP - BOX / 2 - 0.2
        brackets = VGroup()
        for k in range(nr):
            xl = sq.get_x() + PITCH * (k - 2) - BOX / 2
            xr = sq.get_x() + PITCH * (k - 1) + BOX / 2
            b = VMobject(stroke_color=PURPLE, stroke_width=4)
            b.set_points_as_corners([[xl, win_y + 0.1, 0], [xl, win_y, 0], [xr, win_y, 0],
                                     [xr, win_y + 0.1, 0]])
            brackets.add(b)
        led = {"A": A, "A_unit": A_unit, "B": B, "B_lab": B_lab, "head": head, "tags": tags,
               "P": Pr, "L": L, "brackets": brackets, "n": nr,
               "all": VGroup(head, tags, Pr, L, A, A_unit, B, B_lab)}
        return back, wide, letters, led

    def ctx_tag(self, ctx: str) -> VGroup:
        """'after TH': grey 'after', the context letters in purple (the open box for a space)."""
        word = text("after", size=22, color=GRAY)
        parts = [word]
        for ch in ctx:
            if ch == " ":
                parts.append(space_glyph(0.13, 0.055, PURPLE, 2.2))
            else:
                parts.append(text(ch, size=22, color=PURPLE))
        g = VGroup(*parts)
        g.arrange(RIGHT, buff=0.05, aligned_edge=DOWN)
        for p in parts[1:]:                           # a word space after 'after'
            p.shift(RIGHT * 0.08)
        for p in parts[1:]:
            if not isinstance(p, Text):               # the space box sits on the baseline
                p.align_to(word, DOWN)
        return g

    def context(self):
        qb = ctx_box("Q").move_to(self.hidden[-1])
        prior = {s: cost(P[s]) for s in ALPHA}          # costs before the context re-prices
        # the no-context answer stays as a dimmed (30 %) reference at its level
        ref_line, ref_num = self.level_line, self.level_num
        ref = (ref_line, ref_num, H1)
        with self.narrate("What comes after a Q? [pause 1.3]") as beat:
            # only the question changes: the slot before ? becomes a Q, the value becomes ?,
            # and the frame holds still for the prediction
            self.play(FadeOut(self.hidden[-1]), FadeIn(qb, scale=1.2),
                      ref_line.animate.set_stroke(opacity=0.3), ref_num.animate.set_opacity(0.3),
                      *self.eq_unknown(),
                      run_time=beat.until("Q", offset=0.1, min_time=0.8))

        with self.narrate("It's U, ninety-eight percent of the time. U swallows the bar, and the "
                          "average falls to point one six bits. [pause 0.6]") as beat:
            beat.wait_until("U", offset=-0.3)
            t_anims, t_done = self.swap_title(self.x_title_for("Q"), [qb[1]])
            u98, u_br, u_grow = self.tracking_brace("U", cy(prior["U"]) + 0.16, r"98\%")
            # U is named, and its after-Q share is labelled over it before anything moves
            self.play(*t_anims, outline_flash([self.cols["U"]]),
                      FadeIn(u98, shift=0.1 * DOWN, rate_func=lambda t: smooth(max(0.0, 2 * t - 1))),
                      run_time=beat.until("time", end=True, min_time=1.6))
            t_done()
            self.add(u_br)
            # U swallows the bar: it widens to 98 % while its cost falls (height drops
            # geometrically, so the drawn area only ever shrinks); the brace grows with it
            beat.wait_until("swallows", offset=-0.2)
            self.play(*tile_morph(self.cols, P, P_Q, prior, {s: cost(P_Q[s]) for s in ALPHA}, UNIT),
                      u_grow, run_time=beat.until("bar", end=True, offset=0.0, min_time=1.2))
            # pour (the 98 % brace and the letters leave in its first 0.3 s); everything left is
            # a level under 4.2, so the axis zooms in with it
            zoom = self.zoom(UNIT_C, extra_lines=[ref])
            gone = lambda t: smooth(min(1.0, t / 0.3))
            self.pour(P_Q, {s: cost(P_Q[s]) for s in ALPHA},
                      run_time=beat.until("falls", offset=-0.1, min_time=0.75),
                      extra=[*zoom, FadeOut(u98, rate_func=gone), FadeOut(u_br, rate_func=gone),
                             *self.labels_to(0.0)])
            self.zoom_done()
            line, num = self.level_marks(H_Q)
            self.play(Create(line), FadeIn(num, shift=0.1 * LEFT), run_time=0.4)
            # the value lands in the equation as it is spoken
            anims, done = self.eq_known(H_Q, num)
            self.play(*anims, run_time=beat.until("six", end=True, min_time=1.1))
            done()
        self.level_line, self.level_num = line, num

        th = VGroup(ctx_box("T").move_to(self.hidden[-2]), ctx_box("H").move_to(self.hidden[-1]))
        th_cost = {s: cost(P_TH[s]) for s in ALPHA}
        with self.narrate("After TH, E takes two thirds of the bar, and costs "
                          "about half a question.") as beat:
            self.play(FadeOut(qb), FadeOut(self.hidden[-2]), FadeIn(th, scale=1.2),
                      FadeOut(self.level_line), FadeOut(self.level_num),
                      *self.eq_unknown(), run_time=0.5)
            t_anims, t_done = self.swap_title(self.x_title_for("TH"), [th[0][1], th[1][1]])
            # the stack rises into the TH-weighted skyline; tall costs are back, so the axis
            # zooms out
            zoom = self.zoom(UNIT_B, extra_lines=[ref])
            self.unpour(P_TH, prior, run_time=beat.until("two", offset=-0.1, min_time=1.0),
                        extra=[*t_anims, *zoom])
            self.zoom_done()
            t_done()
            # on 'two thirds' E is re-priced at once: the share is labelled, the costs drop
            e68 = self.share_brace("E", P_TH, prior["E"], r"68\%")
            self.play(GrowFromCenter(e68[0]), FadeIn(e68[1], shift=0.1 * UP),
                      *tile_morph(self.cols, P_TH, P_TH, prior, th_cost, UNIT),
                      *self.labels_to(1.0), run_time=beat.until("half", offset=-0.15, min_time=1.2))
            # E's cost: about half a question (its height, outlined in the questions colour)
            self.play(self.cols["E"].animate.set_stroke(YELLOW, width=4),
                      self.band_fill.animate.set_fill(opacity=0.1),
                      self.band_edges.animate.set_stroke(opacity=0.35), run_time=0.5)
        self.th = th

        back, wide, run_letters, led = self.run_box()
        A, A_unit, B, B_lab, head = led["A"], led["A_unit"], led["B"], led["B_lab"], led["head"]
        Pr, L = led["P"], led["L"]
        tags, brackets = led["tags"], led["brackets"]
        nr = led["n"]
        TOT, ARW, Q = 2 * nr, 2 * nr + 1, 2 * nr + 2                # parts of row A
        # the cells of the context row, left to right: T, H, then the run's own letters
        win_cells = [th[0][1], th[1][1], *run_letters]
        # the chart steps out completely while the bill is up: its axes, ticks, titles, band
        # and the 4.11 reference belong to the after-TH skyline, not to the bill (only the
        # Brown citation stays: the bill's numbers are counted there)
        ytk = list(self.ytick.values())
        chart_parts = [self.x_axis, self.y_axis, *ytk, self.x_ticks, self.x_title, self.y_title,
                       self.band_fill, self.band_edges, self.band_lab, ref_line, ref_num]
        with self.narrate("Half a question sounds impossible, but a compressor asks about runs of "
                          "letters. Their probabilities multiply, so their costs add: [pause 0.6] "
                          "five questions for these three, not six. After TH, it averages one "
                          "point seven.") as beat:
            self.play(Indicate(self.cols["E"], color=YELLOW, scale_factor=1.0), run_time=0.9)
            # ... impossible for ONE yes/no question per character (the single ? box)
            beat.wait_until("impossible", offset=-0.2)
            self.play(flag(VGroup(self.qbox, self.qmark)), run_time=0.8)
            # a real run from Shannon's passage: THE O(THER), after T H.  The after-TH skyline
            # and its chart leave (0 %), so the bill cannot be read against axes it is not on
            beat.wait_until("compressor", offset=-0.1)
            self.play(Transform(self.qbox, wide), FadeOut(self.qmark),
                      LaggedStart(*[FadeIn(g, shift=0.1 * RIGHT) for g in run_letters], lag_ratio=0.25),
                      *[self.cols[x].animate.set_fill(opacity=0.0).set_stroke(opacity=0.0) for x in ALPHA
                        if x != "E"],
                      self.cols["E"].animate.set_fill(opacity=0.0).set_stroke(BG, width=1.6, opacity=0.0),
                      FadeOut(e68), *self.labels_to(0.0),
                      *[m.animate.set_opacity(0.0) for m in chart_parts], run_time=0.8)
            # each letter of the run, the two letters it is conditioned on (bracketed in the
            # row, and tagged under the letter), its probability given them and its cost
            # log2(1/p) (Brown); one column at a time
            reveal = beat.until("Their", offset=-0.15, min_time=1.8)
            step = reveal / nr
            p_in = lambda t: smooth(float(np.clip((t - 0.25) / 0.45, 0, 1)))
            c_in = lambda t: smooth(float(np.clip((t - 0.5) / 0.5, 0, 1)))
            for k in range(nr):
                win = VGroup(win_cells[k], win_cells[k + 1])
                if k == 0:
                    lead_in = [Create(brackets[0])]
                else:
                    lead_in = [ReplacementTransform(brackets[k - 1], brackets[k])]
                self.play(*lead_in, pflash(win, scale=1.15),
                          Indicate(run_letters[k], color=INK, scale_factor=1.25),
                          FadeIn(head[k], shift=0.15 * DOWN), FadeIn(tags[k], shift=0.15 * DOWN),
                          FadeIn(Pr[2 * k], shift=0.15 * DOWN, rate_func=p_in),
                          FadeIn(A[2 * k], shift=0.15 * DOWN, rate_func=c_in), run_time=step)
            # their probabilities multiply: the product is built left to right, each p lighting
            # up as the 'x' after it is written; '= 0.0329' comes once every factor is in
            beat.wait_until("Their", offset=-0.1)
            mult = []
            for k in range(nr):
                mult.append(Indicate(Pr[2 * k], color=BLUE, scale_factor=1.2))
                if k < nr - 1:
                    mult.append(Write(Pr[2 * k + 1]))
            self.play(LaggedStart(*mult, lag_ratio=0.35),
                      FadeOut(brackets[nr - 1], rate_func=lambda t: smooth(min(1.0, 3 * t))),
                      run_time=beat.until("multiply", end=True, offset=-0.55, min_time=1.0))
            self.play(Write(Pr[2 * nr - 1]), FadeIn(Pr[2 * nr], shift=0.12 * LEFT), run_time=0.45)
            # the run as ONE symbol of that probability costs log2(1/p) -- the formula above
            # (its log2(1/p) flags as the price is written)
            self.play(Write(L), flag(self.f4[4]),
                      run_time=beat.until("costs", offset=-0.1, min_time=0.5))
            # ... so their costs add: the sum is built the same way
            build = []
            for k in range(nr):
                build.append(Indicate(A[2 * k], color=YELLOW, scale_factor=1.2))
                if k < nr - 1:
                    build.append(Write(A[2 * k + 1]))
            self.play(LaggedStart(*build, lag_ratio=0.35),
                      run_time=beat.until("add", end=True, offset=-0.35, min_time=0.6))
            self.play(Write(A[2 * nr - 1]), FadeIn(A[TOT], shift=0.12 * LEFT), run_time=0.35)
            # the two totals agree: the sum of the costs IS the run's own price
            self.play(flag(A[TOT], run_time=0.5), flag(L[2], run_time=0.5), run_time=0.5)
            # whole questions for the whole run
            beat.wait_until("five", offset=-0.15)
            self.play(Write(A[ARW]), FadeIn(A[Q], shift=0.1 * RIGHT), FadeIn(A_unit, shift=0.1 * RIGHT),
                      run_time=beat.until("questions", end=True, offset=-0.1, min_time=0.6))
            # one letter at a time, each cost rounds up to a whole question
            beat.wait_until("these", offset=-0.2)
            # each whole number drops in under its own cost as that cost pulses: column =
            # correspondence, and no two different digits ever share a place
            self.play(LaggedStart(*[AnimationGroup(Indicate(A[2 * k], color=YELLOW, scale_factor=1.2),
                                                   FadeIn(B[2 * k], shift=0.25 * DOWN))
                                    for k in range(nr)], lag_ratio=0.3),
                      LaggedStart(*[FadeIn(B[i]) for i in range(1, 2 * nr - 1, 2)], lag_ratio=0.2),
                      run_time=beat.until("six", offset=-0.2, min_time=0.8))
            # ... not six
            self.play(FadeIn(B[2 * nr - 1]), FadeIn(B[2 * nr], shift=0.1 * RIGHT),
                      FadeIn(B_lab, shift=0.1 * RIGHT),
                      Indicate(A[Q], color=YELLOW, scale_factor=1.3), run_time=0.8)
            # after TH: the chart comes back (the 4.11 reference stays out until the bill has
            # gone: it would run between the bill's rows) and the TH skyline pours, its columns
            # fading in as they flow, so no tall bar is ever drawn over the bill
            beat.wait_until("After", offset=-0.2)
            back_parts = [self.x_axis.animate.set_stroke(opacity=1.0),
                          self.y_axis.animate.set_stroke(opacity=1.0),
                          *[t.animate.set_opacity(1.0) for t in ytk],
                          self.x_ticks.animate.set_opacity(1.0), self.x_title.animate.set_opacity(1.0),
                          self.y_title.animate.set_opacity(1.0),
                          self.band_fill.animate.set_fill(opacity=0.28),
                          self.band_edges.animate.set_stroke(opacity=1.0),
                          self.band_lab.animate.set_opacity(1.0)]
            # (T after TH is a 0.01 % sliver, 0.13 px wide: it stays at 0, so no invisible
            #  hairline is drawn through the bill's last row)
            self.cols["T"].set_fill(opacity=0.0).set_stroke(opacity=0.0)
            for x in ALPHA:
                if x != "T":
                    self.cols[x].set_stroke(opacity=1.0)
            tgt = poured(ORDER, P_TH, th_cost)
            tgt["T"].set_fill(opacity=0.0).set_stroke(opacity=0.0)
            self.play(LaggedStart(*[geo_morph(self.cols[s], tgt[s]) for s in ORDER], lag_ratio=0.06),
                      *back_parts, run_time=beat.until("average", offset=-0.25, min_time=1.2))
            line, num = self.level_marks(H_TH)
            # the newborn level is the focus: the bill and the run box step back to 30 %
            self.play(Create(line), FadeIn(num, shift=0.1 * LEFT),
                      *[m.animate.set_opacity(0.3) for m in (Pr, L, A, A_unit, B, B_lab)],
                      *glyph_fade(head, 0.3), *glyph_fade(run_letters, 0.3),
                      *glyph_fade([p for t in tags for p in t], 0.3),
                      self.qbox.animate.set_stroke(opacity=0.3), run_time=0.5)
            anims, done = self.eq_known(H_TH, num)
            self.play(*anims, run_time=beat.until("seven", end=True, min_time=1.1))
            done()
        self.level_line, self.level_num = line, num

        # honest limits: Q and TH are the best cases; the average over every two-letter
        # context (Brown, recomputed) is 2.81 -- between them and the no-context 4.11
        c2_lab = text("all two-letter contexts", size=26, color=YELLOW)
        top, garrow, glab = self.gap_meter(clear=lambda: cy(H_TH))
        with self.narrate("But averaged over every two-letter context, it's still two point "
                          "eight.", gap=self.TURN_GAP) as beat:
            # TH was one easy context: the run closes back into the one hidden slot, the bill
            # goes, the TH stack steps back, the axis zooms in on the levels, and the 4.11
            # reference returns (60 %) as the comparison
            beat.wait_until("averaged", offset=-0.2)
            zoom = self.zoom(UNIT_C, extra_lines=[ref, (line, num, H_TH)])
            tgt = poured(ORDER, P_TH, th_cost)
            for x in ALPHA:
                tgt[x].set_fill(opacity=0.26)
            tgt["T"].set_fill(opacity=0.0).set_stroke(opacity=0.0)
            th_tag = text("TH", size=28, color=PURPLE)
            th_tag.move_to([COL_A + num.width / 2 + 0.18 + th_tag.width / 2, cy(H_TH), 0])
            gone = lambda t: smooth(min(1.0, t / 0.3))      # the bill is gone before levels move
            self.play(Transform(self.qbox, back), FadeIn(self.qmark),
                      FadeOut(run_letters, rate_func=gone), FadeOut(led["all"], rate_func=gone),
                      *[Transform(self.cols[x], tgt[x]) for x in ALPHA], *zoom,
                      FadeIn(th_tag, shift=0.1 * LEFT, rate_func=lambda t: smooth(max(0.0, (t - 0.5) / 0.5))),
                      pflash(th, scale=1.0), run_time=0.9)
            self.zoom_done()
            c2_line = DashedLine([X0, cy(H_C2), 0], [X1, cy(H_C2), 0], color=YELLOW, stroke_width=3.5,
                                 dash_length=0.14).set_z_index(3)
            c2_num = DecimalNumber(H_C2, num_decimal_places=2, font_size=36, color=YELLOW)
            c2_num.move_to([COL_A, cy(H_C2), 0])
            c2_lab.next_to(c2_line, UP, buff=0.2).align_to([X0 + 0.35, 0, 0], LEFT)
            # the average over every two-letter context is drawn, and the gap meter measures
            # it once, growing from ~1 straight to it (its reading counting 0 -> 1.81)
            self.add(garrow, glab)
            self.play(Create(c2_line), FadeIn(c2_lab, shift=0.1 * UP),
                      FadeIn(c2_num, shift=0.1 * LEFT), top.animate.set_value(H_C2),
                      ref_line.animate.set_stroke(opacity=0.6), ref_num.animate.set_opacity(0.6),
                      # over the dimmed stack the band is its two green edges and a faint fill
                      # (a 28 % fill under the 26 % blue stack mixes to teal).  (Not in the zoom's
                      # play: two .animate calls on one object in one play keep only the last.)
                      self.band_fill.animate.set_fill(opacity=0.08),
                      run_time=beat.until("context", end=True, min_time=1.2))
            # the equation takes the measured average: the copy leaves the gutter to the right
            # and rises past the 4.11 label on the outside, so it never crosses a level
            y0 = c2_num.get_y()
            anims, done = self.eq_known(H_C2, c2_num,
                                        via=[(COL_A + 0.75, y0 + 0.2), (COL_A + 0.95, y0 + 0.9),
                                             (COL_A + 0.85, ref_num.get_y() + 0.72),
                                             (3.3, ref_num.get_y() + 0.74)])
            self.play(*anims, run_time=beat.until("eight", end=True, min_time=1.2))
            done()
            # ... and says what it is: not one distribution's H, but H averaged over contexts
            c2_note = MathTex("H", r"\ \text{averaged over contexts}", font_size=36, color=GRAY)
            c2_note[0].set_color(YELLOW)
            c2_note.next_to(VGroup(self.f4, self.eq_eq, self.eq_val, self.eq_bits), DOWN, buff=0.2)
            c2_note.align_to(self.eq_bits, RIGHT)
            self.play(FadeIn(c2_note, shift=0.1 * UP), run_time=0.5)
        self.c2 = VGroup(c2_line, c2_num, c2_lab, th_tag)
        self.c2_note = c2_note

        self.gap = (top, garrow, glab)

    def x_title_for(self, ctx: str | None) -> Text:
        """x-axis title: share of all text, or share of what follows the context.  'share'
        sits at the same place in every version."""
        s = "share of text" if ctx is None else f"share after {ctx}"
        t = text(s, size=LABEL - 2, color=GRAY, t2c={ctx: PURPLE} if ctx else None)
        ref = text("share after TH", size=LABEL - 2, color=GRAY)
        ref.move_to([0, XTITLE_Y, 0]).align_to([X1, 0, 0], RIGHT)
        t.shift(ref[:5].get_center() - t[:5].get_center())
        t.text = s
        return t

    def share_brace(self, sym: str, probs: dict, prior_h: float, tex: str) -> VGroup:
        """Blue brace over a widened column, parked ABOVE its tallest state, so no level
        line ever crosses the label (levels are always below the prior height here)."""
        xl = X0 + W * sum(probs[s] for s in ORDER[:ORDER.index(sym)])
        xr = xl + W * probs[sym]
        y = max(cy(prior_h), cy(H1)) + 0.16     # above the grey 4.11 reference line too
        br = BraceBetweenPoints([xl + 0.08, y, 0], [xr - 0.08, y, 0], direction=UP, color=BLUE)
        lab = MathTex(tex, font_size=36, color=BLUE).next_to(br, UP, buff=0.16)
        return VGroup(br, lab)

    # ============================================================== 7 payoff
    def payoff(self):
        # Shannon's record, one fixed cell per symbol (pitch 0.33; two-digit counts get 0.45,
        # so '11 5' can never read as '115'); glyphs 12 % larger than the first cut.
        # It is revealed centred in the frame and lifted (LIFT) when the skyline needs room.
        pitch, LIFT, LINE = 0.33, 1.3, 1.12
        line_y = [1.55, 1.55 - LINE, 1.55 - 2 * LINE]     # (0.3 lower than round 7: the context
                                                          # arithmetic stays above it)
        widths = [[0.45 if g >= 10 else pitch for g in lg] for lg in REC_G]
        x_left = -sum(widths[0]) / 2
        cells, nums, gvals, rows = VGroup(), VGroup(), [], []
        for li, (line_s, line_g) in enumerate(zip(REC_TEXT, REC_G)):
            y, x = line_y[li], x_left
            for ch, g, w in zip(line_s, line_g, widths[li]):
                xc = x + w / 2
                x += w
                c = glyph(ch, 27, INK) if ch != " " else space_glyph(0.13, 0.055, GRAY, 2.2)
                c.move_to([xc, y - (0.07 if ch == " " else 0), 0])
                n = Text(str(g), font=SERIF, font_size=24, color=GRAY if g == 1 else YELLOW)
                n.move_to([xc, y - 0.45, 0])
                cells.add(c)
                nums.add(n)
                gvals.append(g)
                rows.append(li)
        self.cells, self.nums = cells, nums
        n_cells = len(cells)
        ones = [g == 1 for g in gvals]
        prog = ValueTracker(0)
        base = ValueTracker(0)              # opacity of the not-yet-read letters
        # a guess count exists only once the subject has guessed that letter: unread counts
        # stay hidden, and each one appears as the cursor passes
        cursor = Rectangle(width=0.37, height=0.86, stroke_color=YELLOW, stroke_width=3)

        # the context row tells the truth while the subject reads: its 12 boxes hold the last
        # 12 symbols already read (purple), and the ? box is the symbol being guessed
        flat = "".join(REC_TEXT)
        live = VGroup(*[glyph(ch, 30, PURPLE) for ch in flat])
        slots = [b.get_center() for b in self.hidden]

        def show(_):
            k, b = prog.get_value(), base.get_value()
            for i in range(n_cells):
                read = i < k
                set_glyph_opacity(cells[i], 1.0 if read else b)
                nums[i].set_opacity(1.0 if read else 0.0)
            kk = int(min(n_cells, max(0, math.floor(k))))
            for i, g in enumerate(live):
                j = i - (kk - len(slots))
                if i < kk and 0 <= j < len(slots):
                    g.move_to(slots[j] + (DOWN * 0.05 if flat[i] == " " else ORIGIN))
                    set_glyph_opacity(g, 1.0)
                else:
                    set_glyph_opacity(g, 0.0)
        show(None)
        self.live_row = live
        rec_driver = Mobject()
        rec_driver.add_updater(show)

        def cur_upd(m):
            i = int(min(n_cells - 1, max(0, math.floor(prog.get_value()))))
            m.move_to([cells[i].get_x(), line_y[rows[i]] - 0.22, 0])
        cursor.add_updater(cur_upd)
        self.exclude(cells, "Shannon's record set as fixed-pitch text (0.33 per symbol); the "
                     "open-box space markers are part of the line")
        self.allow_overlap(cursor, reason="reading cursor frames one symbol of the fixed-pitch "
                           "record, so its edges sit close to the neighbouring symbols by design")
        cur_upd(cursor)

        tally_lab = MathTex(r"\text{first guess: }", font_size=MATH)
        tally_n = DecimalNumber(0, num_decimal_places=0, font_size=MATH, color=GREEN)
        tally_of = MathTex(r"/\ 102", font_size=MATH)
        tally_n.set_value(79)
        tally = VGroup(tally_lab, tally_n, tally_of).arrange(RIGHT, buff=0.15)
        tally.move_to([3.4, line_y[2] - 1.05, 0])
        right_edge = tally_n.get_right()
        tally_n.add_updater(lambda m: m.set_value(sum(ones[:int(prog.get_value())]))
                            .move_to(right_edge, aligned_edge=RIGHT))
        tally_n.update()
        cite = citation("Shannon, 1951 · Bell System Technical Journal")

        # ---- why Shannon needed a person: possible contexts explode, the corpus does not
        top, garrow, glab = self.gap
        ctx_line = MathTex(r"\text{possible contexts: }", r"27^{2} = 729", r"\;\to\;",
                           rf"27^{{100}} \approx 10^{{{int(CTXS['possible_100_log10'])}}}",
                           font_size=36, color=GRAY)
        ctx_line.move_to([-0.35, TOP_Y + 0.32, 0])
        corpus = text(f"Brown Corpus: {D['brown']['characters'] / 1e6:.2f} M characters",
                      size=26, color=GRAY)
        corpus.next_to(ctx_line, DOWN, buff=0.22).align_to(ctx_line, LEFT)
        with self.narrate("Hundred-letter contexts need more text than any corpus holds, so Shannon "
                          "asked a person, a predictor that knows English.") as beat:
            beat.wait_until("need", offset=-0.2)          # (after 'Hundred-letter contexts')
            self.play(FadeOut(self.f4, shift=0.15 * UP), FadeOut(self.eq_eq, shift=0.15 * UP),
                      FadeOut(self.eq_val, shift=0.15 * UP), FadeOut(self.eq_bits, shift=0.15 * UP),
                      FadeOut(self.c2_note, shift=0.15 * UP), run_time=0.4)
            # the arithmetic is the one focal point: the gap meter and the 2.81 label have done
            # their job and leave as it is written
            c2_lab = self.c2[2]
            self.play(Write(ctx_line), FadeOut(garrow, rate_func=lambda t: smooth(min(1.0, 2.5 * t))),
                      FadeOut(glab, rate_func=lambda t: smooth(min(1.0, 2.5 * t))),
                      FadeOut(c2_lab, rate_func=lambda t: smooth(min(1.0, 2.5 * t))),
                      run_time=beat.until("corpus", offset=-0.1, min_time=1.0))
            # 10^143 possible contexts against 5.75 M characters of corpus
            self.play(FadeIn(corpus, shift=0.1 * UP), flag(self.cite_br, color=GRAY),
                      flag(ctx_line[3], color=INK),
                      run_time=beat.until("holds", end=True, min_time=0.8))
            garrow.clear_updaters()
            glab.clear_updaters()
            # so Shannon asked a person: the chart goes (the arithmetic stays, above), and the
            # person's English text arrives, faint (nobody has read it yet)
            beat.wait_until("so", offset=-0.1)
            self.lab_driver.clear_updaters()
            self.remove(self.lab_driver)
            # the row keeps its meaning (text already read): T H belonged to the chart's
            # example, so they leave with it and the row is blank again, as in the cold open
            row = [m for m in self.row_now() if all(m is not b for b in self.th)]
            keep_ids = {id(m) for m in row} | {id(f) for f in ctx_line.get_family()} | \
                       {id(f) for f in corpus.get_family()}
            chart = [m for m in self.visible()
                     if not any(id(f) in keep_ids for f in m.get_family())]
            out_first = lambda t: smooth(min(1.0, t / 0.5))
            in_late = lambda t: smooth(float(np.clip((t - 0.45) / 0.55, 0, 1)))
            self.add(rec_driver, cells, nums, live)
            self.bring_to_back(rec_driver)
            self.play(*[FadeOut(m, rate_func=out_first) for m in chart],
                      FadeIn(self.hidden[-2], rate_func=out_first), FadeIn(self.hidden[-1], rate_func=out_first),
                      base.animate(rate_func=in_late).set_value(0.4),
                      FadeIn(cite, shift=0.1 * UP, rate_func=in_late), run_time=0.95)
            row = self.row_now()
            # ... a person: a reader's cursor locks onto the first letter, with the
            # text-so-far row (what a reader knows) flashing
            beat.wait_until("person", offset=-0.25)
            self.play(FadeIn(cursor, scale=1.6), pflash(VGroup(*row), scale=1.0),
                      run_time=beat.until("person", end=True, offset=0.15, min_time=0.7))
            # ... that knows English: the arithmetic (why no corpus could do it) leaves
            beat.wait_until("knows", offset=-0.2)
            self.play(FadeOut(ctx_line, shift=0.1 * UP), FadeOut(corpus, shift=0.1 * UP), run_time=0.6)

        with self.narrate("His subject read a passage, guessing each next letter until right: "
                          "seventy-nine of a hundred two on the first guess. [pause 0.6]") as beat:
            self.play(FadeIn(tally), run_time=beat.until("read", offset=-0.1, min_time=0.5))
            # the cursor reads at a steady pace; the unread text steps back (40 % -> 15 %)
            # so the line being read is the focus
            self.play(prog.animate(rate_func=LINEAR).set_value(n_cells),
                      base.animate(rate_func=lambda t: smooth(min(1.0, 6 * t))).set_value(0.15),
                      run_time=beat.until("seventy-nine", offset=-0.2, min_time=3.6))
            rec_driver.clear_updaters()
            self.remove(rec_driver)
            cursor.clear_updaters()
            tally_n.clear_updaters()
            tally_n.set_value(79).move_to(right_edge, aligned_edge=RIGHT)
            self.play(FadeOut(cursor), flag(tally_n, color=GREEN), run_time=0.9)
            # ... on the first guess: the 79 grey 1s are the first guesses
            beat.wait_until("first", offset=-0.15)
            self.play(LaggedStart(*[Indicate(nums[i], color=GREEN, scale_factor=1.25)
                                    for i in range(n_cells) if gvals[i] == 1], lag_ratio=0.012),
                      run_time=1.1)
        self.tally, self.cite = tally, cite

        # ---- the guess numbers as a new alphabet: the same skyline, then the same pour.
        # The chart is centred and full size; the record's letters leave (they return for the
        # landing) and its three rows of counts close up at the top of the frame.
        X2, W2, Y2, U2 = -4.0, 8.0, -1.05, 0.4         # centred: the axis spans -4 .. 4
        U2Z = 1.8                            # after the pour the axis zooms in (0..2.1 bits)
        keys = sorted(GUESS)
        lefts, acc = {}, 0
        for k in keys:
            lefts[k] = X2 + W2 * acc / N_REC
            acc += GUESS[k]
        wk = {k: W2 * GUESS[k] / N_REC for k in keys}
        FOOT = 0.1                           # each column's foot (where its counts land)
        mcols = {k: column(lefts[k], wk[k], FOOT, base=Y2) for k in keys}
        for k in keys:
            mcols[k].set_fill(opacity=0).set_stroke(opacity=0)
        final = {k: column(lefts[k], wk[k], U2 * math.log2(N_REC / GUESS[k]), base=Y2) for k in keys}
        mx_axis = Line([X2, Y2, 0], [X2 + W2 + 0.05, Y2, 0], color=GRAY, stroke_width=2.5).set_z_index(1)
        my_axis = Line([X2, Y2, 0], [X2, Y2 + U2 * 7.2, 0], color=GRAY, stroke_width=2.5)

        def mtick(v, unit):
            tk = Line([X2 - 0.06, Y2 + unit * v, 0], [X2, Y2 + unit * v, 0], color=GRAY, stroke_width=2.5)
            lb = MathTex(str(v), font_size=26, color=GRAY).next_to(tk, LEFT, buff=0.1)
            lb.ss_role = "tick"
            return VGroup(tk, lb)
        my_ticks = VGroup(*[mtick(v, U2) for v in (0, 2, 4, 6)])
        mx_ticks = VGroup()
        for v, lab in ((0, r"0\%"), (1, r"100\%")):
            tk = Line([X2 + W2 * v, Y2, 0], [X2 + W2 * v, Y2 - 0.07, 0], color=GRAY, stroke_width=2.5)
            lb = MathTex(lab, font_size=26, color=GRAY).move_to([X2 + W2 * v, Y2 - 0.67, 0])
            lb.ss_role = "tick"
            mx_ticks.add(VGroup(tk, lb))
        my_title = text("bits", size=26, color=GRAY).next_to(my_axis.get_top(), UP, buff=0.15)
        my_title.align_to(my_ticks, LEFT)
        tail_l, tail_r = lefts[3], X2 + W2
        mlabs = VGroup(text("1st", size=26).move_to([lefts[1] + wk[1] / 2, Y2 - 0.3, 0]),
                       text("2nd", size=26).move_to([lefts[2] + wk[2] / 2, Y2 - 0.3, 0]),
                       text("3rd+", size=26).move_to([(tail_l + tail_r) / 2 + 0.08, Y2 - 0.3, 0]))
        mx_title = text("share of guesses", size=26, color=GRAY)
        mx_title.move_to([X2 + W2 / 2, Y2 - 0.92, 0])     # a full row under the 1st/2nd/3rd+ labels
        # the skyline's heights are the same formula again: log2(1/q), q = share of guesses.  It
        # stands over the (low) 1st column, on a grey leader to the 2nd column it measures
        q2 = GUESS[2] / N_REC
        lq = MathTex(r"\log_2\!\frac{1}{q}", "=", f"{math.log2(1 / q2):.2f}", font_size=40)
        lq[0].set_color(YELLOW)
        frac_glyphs(lq[0])["p"].set_color(BLUE)
        lq[2].set_color(YELLOW)
        c2_top = final[2].get_top()
        lq.move_to([c2_top[0] - 2.35, c2_top[1] + 0.75, 0])
        lq_lead = Line(lq.get_right() + RIGHT * 0.22 + DOWN * 0.1, c2_top + UP * 0.1 + LEFT * 0.05,
                       color=GRAY, stroke_width=2)
        mstack, squat, yb, ys = {}, {}, Y2, Y2
        for k in keys:                       # the poured stack, unzoomed and zoomed
            hk = GUESS[k] / N_REC * math.log2(N_REC / GUESS[k])
            squat[k] = slab(X2, W2, ys, U2 * hk)
            mstack[k] = slab(X2, W2, yb, U2Z * hk)
            ys += U2 * hk
            yb += U2Z * hk
        mmap = lambda v: Y2 + U2Z * v
        lvl_y = mmap(H_GUESS)
        mline = DashedLine([X2, lvl_y, 0], [X2 + W2, lvl_y, 0], color=YELLOW, stroke_width=3.5,
                           dash_length=0.12).set_z_index(3)
        mnum = MathTex(r"\approx", f"{H_GUESS:.2f}", font_size=40, color=YELLOW)
        mnum.move_to([0, lvl_y, 0]).align_to([X2 + W2 + 0.3, 0, 0], LEFT)
        down = Arrow([0, 0.27, 0], [0, -0.27, 0], buff=0, color=YELLOW, stroke_width=4,
                     max_tip_length_to_length_ratio=0.4).next_to(mnum, RIGHT, buff=0.2)
        # one passage of 102 symbols, scored with Shannon's upper-bound formula: an estimate
        # from above, which a better guesser could only lower; its early letters had little
        # context (0 to 101 letters), which is why it sits above Shannon's 100-letter band
        upper = text("upper estimate", size=26, color=GRAY)
        upper.next_to(VGroup(mnum, down), UP, buff=0.25).align_to(down, RIGHT)
        why = VGroup(text("one passage,", size=24, color=GRAY),
                     text("context 0–101", size=24, color=GRAY)).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        why.next_to(mnum, DOWN, buff=0.3).align_to(mnum, LEFT)
        # Shannon's ~1 on this axis too, drawn OVER the poured stack (it lies inside it)
        # (two green edges and a 10 % fill: a 30 % green over the blue stack mixed to teal)
        m_band = Rectangle(width=W2, height=U2Z * (HI - LO), stroke_width=0, fill_color=GREEN,
                           fill_opacity=0.1).move_to([X2 + W2 / 2, mmap((LO + HI) / 2), 0])
        m_band.set_z_index(4)
        m_edges = VGroup(Line([X2, mmap(LO), 0], [X2 + W2, mmap(LO), 0]),
                         Line([X2, mmap(HI), 0], [X2 + W2, mmap(HI), 0]))
        m_edges.set_stroke(GREEN, 2.5).set_z_index(5)
        m_band_lab = MathTex(r"\approx\!1", font_size=36, color=GREEN)
        m_band_lab.move_to([0, mmap((LO + HI) / 2), 0]).align_to([X2 - 0.18, 0, 0], RIGHT)
        new_ticks = VGroup(mtick(0, U2Z), mtick(2, U2Z))
        zoom_axis = Line([X2, Y2, 0], [X2, Y2 + U2Z * 2.1, 0], color=GRAY, stroke_width=2.5)

        # ---- the flight plan: the record's three count rows, closed up at the top, are sorted
        # into their columns one row at a time, bottom row first (so no count ever passes over
        # one still at rest).  Each count drops straight down to its group's lane, runs along
        # the lane to its column, and drops straight into the column's foot.  1s, 2s and the
        # rest use separate lanes (each 3+ count its own), so no two ever cross.
        ROW_C = [3.15, 2.68, 2.21]
        L1, L2, L3, SUB = Y2 + 0.5, Y2 + 0.85, Y2 + 1.2, 0.3
        DUR, DEL = 0.9, 0.6                  # one row's flight, and the stagger between rows
        PA, PB, PC = 0.38, 0.36, 0.26        # down to the lane / along it / down into the foot
        start = {2: 0.0, 1: DEL, 0: 2 * DEL}
        TOTAL = 2 * DEL + DUR
        plan = []
        for r in range(3):
            idx = [i for i in range(n_cells) if rows[i] == r]
            for k in keys:
                ds = sorted([i for i in idx if gvals[i] == k], key=lambda i: nums[i].get_x())
                for j, i in enumerate(ds):
                    plan.append({"i": i, "r": r, "k": k, "x0": nums[i].get_x(), "y0": ROW_C[r],
                                 "xt": lefts[k] + wk[k] * (j + 0.5) / len(ds)})
        for r in range(3):                   # 3+ counts: one lane each, farthest-right highest
            rest = sorted([d for d in plan if d["r"] == r and d["k"] >= 3], key=lambda d: d["xt"] - d["x0"])
            for j, d in enumerate(rest):
                d["lane"] = L3 + SUB * j
            for d in plan:
                if d["r"] == r and d["k"] in (1, 2):
                    d["lane"] = L1 if d["k"] == 1 else L2
        st = lambda t: float(np.clip(t, 0, 1)) ** 2 * (3 - 2 * float(np.clip(t, 0, 1)))
        homes = {}

        def flight(_m, alpha):
            tau = alpha * TOTAL
            landed = {k: 0.0 for k in keys}
            for d in plan:
                m, t = nums[d["i"]], (tau - start[d["r"]]) / DUR
                a, b, c = st(t / PA), st((t - PA) / PB), st((t - PA - PB) / PC)
                yl = Y2 + 0.06
                m.become(homes[d["i"]])
                m.scale(1 - 0.45 * float(np.clip(t, 0, 1)))
                m.move_to([d["x0"] + (d["xt"] - d["x0"]) * b,
                           d["y0"] + (d["lane"] - d["y0"]) * a + (yl - d["lane"]) * c, 0])
                m.set_opacity(1.0 if c < 0.6 else max(0.0, (1 - c) / 0.4))
                landed[d["k"]] += float(np.clip((c - 0.6) / 0.4, 0, 1))
            for k in keys:                   # each foot widens as its counts land in it
                w = wk[k] * landed[k] / GUESS[k]
                x0 = lefts[k]
                mcols[k].set_points_as_corners([[x0 + w, Y2 + FOOT, 0], [x0, Y2 + FOOT, 0], [x0, Y2, 0],
                                                [x0 + w, Y2, 0], [x0 + w, Y2 + FOOT, 0]])
                vis = 1.0 if w > 1e-3 else 0.0
                mcols[k].set_fill(BLUE, opacity=0.85 * vis)
                mcols[k].set_stroke(BG, width=1.6 if w > 0.03 else 0, opacity=vis)

        with self.narrate("A twin guessing the same way could rebuild the passage from these "
                          "counts. Treat each count as a symbol: [pause 1.2] the same "
                          "skyline pours flat at about one point four bits.") as beat:
            # Shannon's identical twin: hide the letters, keep only the counts...
            beat.wait_until("twin", offset=-0.2)
            self.play(*glyph_fade(cells, 0.12), FadeOut(tally, shift=UP * 0.3), run_time=0.8)
            # ...and the twin, guessing the same way, writes them back from the counts
            beat.wait_until("rebuild", offset=-0.1)
            self.play(LaggedStart(*glyph_fade(cells, 1.0), lag_ratio=0.02),
                      run_time=beat.until("counts", offset=-0.1, min_time=1.2))
            # the counts carry everything: the letters and the text-so-far row leave first, then
            # the three rows of counts close up at the top (rows keep their order, so none
            # crosses another) and the new chart's baseline is drawn below them
            row = self.row_now()
            first = lambda t: smooth(min(1.0, t / 0.35))
            then = lambda t: smooth(max(0.0, (t - 0.3) / 0.7))
            self.play(*[(c.animate(rate_func=first).set_opacity(0.0) if isinstance(c, Text)
                         else c.animate(rate_func=first).set_stroke(opacity=0.0)) for c in cells],
                      *[FadeOut(m, rate_func=first) for m in row],
                      *[nums[i].animate(rate_func=then).set_y(ROW_C[rows[i]]) for i in range(n_cells)],
                      Create(mx_axis, rate_func=lambda t: smooth(max(0.0, (t - 0.5) / 0.5))),
                      FadeIn(mx_ticks, rate_func=lambda t: smooth(max(0.0, (t - 0.5) / 0.5))),
                      run_time=beat.until("Treat", offset=-0.1, min_time=1.0))
            for i in range(n_cells):
                homes[i] = nums[i].copy()
            self.add(*mcols.values())
            self.bring_to_front(mx_axis)
            # every count is sorted into its own column's foot, the bottom row first; each foot
            # widens as its counts land (width = share of guesses)
            self.play(UpdateFromAlphaFunc(VGroup(*nums, *mcols.values()), flight, rate_func=linear),
                      run_time=TOTAL)
            self.remove(*nums)
            # ... then every column rises to its cost (height = log2(1/share)), and the vertical
            # axis grows with it, as the letter columns did at the start
            self.play(*[Transform(mcols[k], final[k]) for k in keys], Create(my_axis),
                      FadeIn(my_ticks), run_time=0.6)
            # the titles, labels and the formula come only once every count has landed
            self.play(FadeIn(my_title), FadeIn(mx_title), FadeIn(mlabs), Write(lq[0]), Write(lq[1]),
                      run_time=0.5)
            self.check_layout("guess chart labels")   # 1st / 2nd / 3rd+ vs 'share of guesses'
            # the heights are the same formula again, with q = share of guesses: the value is
            # written on a leader to the 2nd-guess column, which flashes (white edge, bright blue)
            self.play(Write(lq[2]), Create(lq_lead), outline_flash([mcols[2]]), run_time=0.8)
            # the columns this label describes pour away, so it leaves with the pour
            beat.wait_until("flat", offset=-0.35)
            self.play(LaggedStart(*[geo_morph(mcols[k], squat[k]) for k in keys], lag_ratio=0.08),
                      FadeOut(mlabs, rate_func=lambda t: smooth(min(1.0, 2.5 * t))),
                      FadeOut(VGroup(lq, lq_lead), rate_func=lambda t: smooth(min(1.0, 2.5 * t))),
                      run_time=beat.until("one point", offset=-0.1, min_time=1.0))
            # the poured level is small: the axis zooms in, Shannon's ~1 band comes with it
            self.play(*[Transform(mcols[k], mstack[k]) for k in keys],
                      Transform(my_axis, zoom_axis),
                      FadeOut(my_ticks, rate_func=lambda t: smooth(min(1.0, t / 0.3))),
                      FadeIn(new_ticks, rate_func=lambda t: smooth(max(0.0, (t - 0.65) / 0.35))),
                      my_title.animate.next_to(zoom_axis.get_top(), UP, buff=0.15).align_to(my_ticks, LEFT),
                      FadeIn(VGroup(m_band, m_edges, m_band_lab),
                             rate_func=lambda t: smooth(max(0.0, (t - 0.6) / 0.4))), run_time=0.8)
            # the level, and why this passage sits where it does (one passage, short contexts)
            self.play(Create(mline), FadeIn(mnum, shift=0.1 * LEFT), run_time=0.6)
            self.play(FadeIn(why, shift=0.1 * UP), run_time=0.6)

        # the gap to Shannon's ~1, measured as before (it grows from ~1, counting 0 -> 0.42)
        m_top, m_gap, m_gap_lab = self.gap_meter(x=X2 + W2 / 2, ymap=mmap, clear=lambda: lvl_y)
        with self.narrate("A better guesser could only lower it.", speed=0.8, gap=0) as beat:
            self.add(m_gap, m_gap_lab)
            self.play(m_top.animate.set_value(H_GUESS),
                      run_time=beat.until("could", offset=-0.15, min_time=0.6))
            # ... could only lower it: the arrow down and 'upper estimate' (read before the turn)
            self.play(GrowArrow(down), FadeIn(upper, shift=0.1 * DOWN), run_time=0.6)
        m_gap.clear_updaters()
        m_gap_lab.clear_updaters()
        mframe = VGroup(mx_axis, my_axis, new_ticks, mx_ticks, my_title, mx_title)
        mini_first = VGroup(*mcols.values(), mframe, mline, why, m_band, m_edges, m_band_lab,
                            m_gap, m_gap_lab, mnum[0])
        mini_last = VGroup(down, upper)          # the verdict on this chart leaves last
        self.mnum = mnum

        # ---- the bits-per-character line: our attempts, this passage, Shannon, a 2023 model.
        # It is the summary picture, so it takes the middle of the frame and every marker says
        # what it measured.  It is BUILT, in story order: the axis grows, the three estimates
        # drop in (halving, no context, two letters), the person's 1.42 drops in last, then
        # the axis title; Shannon's band grows as it is named.
        nl_y, u = 0.25, 2.45

        def nx(v):
            return -6.125 + u * v
        nline = Line([nx(0), nl_y, 0], [nx(5), nl_y, 0], color=GRAY, stroke_width=3)
        nt = VGroup()
        for v in range(6):
            tk = Line([nx(v), nl_y - 0.07, 0], [nx(v), nl_y + 0.07, 0], color=GRAY, stroke_width=2.5)
            lb = MathTex(str(v), font_size=MATH_SMALL, color=GRAY).move_to([nx(v), nl_y - 0.42, 0])
            lb.ss_role = "tick"
            nt.add(VGroup(tk, lb))
        tag_y = nl_y - 0.95
        ntitle = text("bits per character", size=26, color=GRAY)
        ntitle.move_to([0, nl_y - 1.5, 0]).align_to([nx(5), 0, 0], RIGHT)
        nband = Rectangle(width=u * (HI - LO), height=0.3, stroke_color=GREEN, stroke_width=2,
                          fill_color=GREEN, fill_opacity=0.35).move_to([nx((LO + HI) / 2), nl_y, 0])
        nband_lab = MathTex(r"0.6\text{--}1.3", font_size=36, color=GREEN)
        nband_lab.move_to([nx((LO + HI) / 2), tag_y, 0])          # under the band, on the
        nband_lab.shift(UP * (tag_y - 0.1 - nband_lab.get_bottom()[1]))   # tags' baseline

        def marker(v, color, lab, tag=None, left=None, right=None):
            """A triangle on the line, its value above it, and a grey tag (what it measured)
            in the row under the axis; crowded tags hang left or right of their marker."""
            tri = Triangle(color=color, fill_opacity=1).scale(0.12).rotate(PI).move_to([nx(v), nl_y + 0.24, 0])
            lab.move_to([nx(v), nl_y + 0.68, 0])
            g = VGroup(tri, lab)
            if tag is not None:
                t = text(tag, size=28, color=GRAY).move_to([nx(v), tag_y, 0])
                # one shared baseline for the tag row (descenders such as the p of 'person'
                # must not lift a tag above its neighbours)
                flat = [g for g, ch in zip(t, tag.replace(" ", "")) if ch in "acemnorsuvwxz"]
                t.shift(UP * (tag_y - 0.1 - flat[0].get_bottom()[1]))
                if left is not None:
                    t.align_to([left, 0, 0], LEFT)
                if right is not None:
                    t.align_to([right, 0, 0], RIGHT)
                g.add(t)
            return g
        # every Sum p log2(1/p) estimate is yellow; only the abandoned halving price is grey
        m475 = marker(H0, GRAY, MathTex("4.75", font_size=40, color=GRAY), "halving",
                      right=nx(5) + 0.05)
        m411 = marker(H1, YELLOW, MathTex("4.11", font_size=40, color=YELLOW), "no context",
                      right=nx(H1) + 0.35)
        m281 = marker(H_C2, YELLOW, MathTex(f"{H_C2:.2f}", font_size=40, color=YELLOW),
                      "2-letter context")
        m142 = marker(H_GUESS, YELLOW, MathTex(f"{H_GUESS:.2f}", font_size=40, color=YELLOW),
                      "person", left=nx(H_GUESS) - 0.25)
        # ... measured on one 102-letter passage (why it sits above the band)
        m142.add(text("102 letters", size=24, color=GRAY).next_to(m142[2], DOWN, buff=0.14)
                 .align_to(m142[2], LEFT))
        llm_val = MathTex(f"{LLM_BPC:.2f}", font_size=40, color=INK)
        mllm = marker(LLM_BPC, INK, llm_val)
        llm_name = text("LLM", size=28, color=INK).next_to(llm_val, UP, buff=0.17)
        mllm.add(llm_name)
        llm_note = VGroup(text("1924 book", size=26, color=GRAY),
                          text("· Gutenberg, May 2023", size=26, color=GRAY)).arrange(RIGHT, buff=0.14)
        # one baseline for the two parts (descenders must not lift 'Gutenberg, May')
        for part, s, k in zip(llm_note, ("1924book", "·Gutenberg,May2023"), (5, 4)):
            assert len(part) == len(s) and s[k] in "acemnorsuvwxz"
            part.shift(UP * (llm_note[0][5].get_bottom()[1] - part[k].get_bottom()[1]))
        llm_note.next_to(llm_name, UP, buff=0.22).align_to(llm_name, LEFT)
        cite_llm = citation("Valmeekam et al., 2023 · arXiv:2306.04050 (LLMZip), Table IV · 27 symbols")

        # the act turn (silent, 0.9 s): the guess chart leaves (its verdict last), the person's
        # 1.42 rises over the top of the frame and waits above its own place on the line, and
        # the line grows left to right, each tick appearing as the line reaches it
        a = mnum[1].get_center()
        park = np.array([nx(H_GUESS), nl_y + 1.95, 0])
        p142 = route([(a[0], a[1]), (a[0] - 0.3, 2.35), (1.0, 2.5), (park[0] + 0.6, park[1] + 0.12),
                      (park[0], park[1])])
        parked = m142[1].copy().move_to(park)
        x_end = lambda t: nx(0) + (nx(5) - nx(0)) * t

        def ticks_follow(m, t):
            for g in m:
                o = float(np.clip((x_end(t) - g[0].get_x()) / 0.2 + 1.0, 0, 1))
                g.set_opacity(o)
        nt.set_opacity(0)
        self.add(nt)
        turn = self.TURN_GAP
        self.play(FadeOut(mini_first, rate_func=lambda t: smooth(min(1.0, t / 0.45))),
                  FadeOut(mini_last, rate_func=lambda t: smooth(float(np.clip((t - 0.3) / 0.4, 0, 1)))),
                  fly(mnum[1], parked, p142, rate=lambda t: smooth(max(0.0, (t - 0.15) / 0.85))),
                  Create(nline, rate_func=lambda t: float(np.clip((t - 0.15) / 0.85, 0, 1))),
                  UpdateFromAlphaFunc(nt, lambda m, t: ticks_follow(m, float(np.clip((t - 0.15) / 0.85, 0, 1)))),
                  run_time=turn)
        self.remove(mnum[1], mnum)
        self.add(parked)

        def drop(g, dy=0.3):
            return [FadeIn(m, shift=dy * DOWN) for m in g]
        with self.narrate("Shannon's tests, with a hundred letters of context, put English between "
                          "point six and one point three bits.") as beat:
            # the three estimates drop in, in story order, each with its value and its tag
            self.play(LaggedStart(*[AnimationGroup(*drop(m)) for m in (m475, m411, m281)],
                                  lag_ratio=0.35), run_time=0.8)
            # ... then the person's 1.42 drops onto its own marker, with its tags
            self.play(parked.animate.move_to(m142[1]), *drop([m142[0]], 0.3),
                      *drop([m142[2], m142[3]], 0.3), run_time=0.5)
            self.remove(parked)
            self.add(m142[1])
            self.play(FadeIn(ntitle, shift=0.1 * UP), run_time=0.35)
            # a hundred letters of context: Shannon's band grows outward from ~1 to 0.6-1.3
            beat.wait_until("hundred", offset=-0.1)
            l0, r0 = nx(1.0), nx(1.0)
            l1, r1 = nband.get_left()[0], nband.get_right()[0]
            yb, yt = nband.get_bottom()[1], nband.get_top()[1]

            def grow_band(m, t):
                t = smooth(t)
                xl, xr = l0 + (l1 - l0) * t, r0 + (r1 - r0) * t + 0.004
                m.set_points_as_corners([[xr, yt, 0], [xl, yt, 0], [xl, yb, 0], [xr, yb, 0], [xr, yt, 0]])
            band_final = nband.copy()
            grow_band(nband, 0.0)
            self.add(nband)
            self.play(UpdateFromAlphaFunc(nband, grow_band),
                      run_time=beat.until("context", end=True, offset=-0.3, min_time=1.0))
            nband.become(band_final)
            # ... between point six and one point three: the band's label is written as spoken
            beat.wait_until("point", offset=-0.1)
            self.play(Write(nband_lab), run_time=beat.until("three", end=True, offset=0.0, min_time=1.0))
            self.play(Indicate(nband, color=GREEN, scale_factor=1.15), run_time=0.9)

        # the model is a better guesser: its marker is born from the person's 1.42 and waits
        # above it; on 'needed' it slides left at that height (name and note ride along, so
        # nothing crosses) and on 'point eight four' it drops onto 0.84, inside the band
        hi_y = nl_y + 1.2
        s_tri = mllm[0].copy().move_to([nx(H_GUESS), hi_y, 0])
        s_name = llm_name.copy().next_to(s_tri, UP, buff=0.17)
        s_note = llm_note.copy().next_to(s_name, UP, buff=0.22).align_to(s_name, LEFT)
        movers = [(s_tri, mllm[0]), (s_name, llm_name), (s_note, llm_note)]
        # context the LLM's story does not need steps back (30 %) while its note is read;
        # the person, its 102 letters and Shannon's 0.6-1.3 stay bright
        quiet = [m475[2], m411[2], m281[2], ntitle]

        def slide_drop(t):
            for m, tgt in movers:
                a0 = m.saved_state.get_center()
                b0 = tgt.get_center()
                tx = smooth(min(1.0, t / 0.55))
                ty = smooth(max(0.0, (t - 0.5) / 0.5))
                m.move_to([a0[0] + (b0[0] - a0[0]) * tx, a0[1] + (b0[1] - a0[1]) * ty, 0])
        with self.narrate("In twenty twenty-three, a language model compressed part of a book "
                          "[pause 0.3] posted to Project Gutenberg after the model was trained. "
                          "[pause 0.4] It needed point eight four bits, inside that range.",
                          gap=self.TURN_GAP) as beat:
            beat.wait_until("language", offset=-0.2)
            self.play(Succession(FadeOut(self.cite, run_time=0.3), FadeIn(cite_llm, run_time=0.3)),
                      TransformFromCopy(m142[0], s_tri), FadeIn(s_name, shift=0.1 * UP),
                      run_time=0.8)
            beat.wait_until("book", offset=-0.1)
            self.play(FadeIn(s_note[0], shift=0.1 * LEFT),
                      *[m.animate.set_opacity(0.3) for m in quiet], run_time=0.5)
            beat.wait_until("Gutenberg", offset=-0.1)
            self.play(FadeIn(s_note[1], shift=0.1 * LEFT), run_time=0.5)
            beat.wait_until("needed", offset=-0.15)
            for m, _ in movers:
                m.save_state()
            self.play(UpdateFromAlphaFunc(VGroup(s_tri, s_name, s_note), lambda _m, t: slide_drop(t),
                                          rate_func=linear),
                      FadeIn(llm_val, shift=0.1 * DOWN, rate_func=lambda t: smooth(max(0.0, (t - 0.7) / 0.3))),
                      run_time=beat.until("four", end=True, min_time=1.1))
            self.remove(s_tri, s_name, s_note)
            self.add(mllm[0], llm_name, llm_note)
            beat.wait_until("inside", offset=-0.2)
            self.play(Indicate(nband, color=GREEN, scale_factor=1.15), flag(mllm, color=INK),
                      run_time=0.9)
        self.meter = VGroup(nline, nt, ntitle, nband, nband_lab, m475, m411, m281, m142, mllm,
                            llm_note, cite_llm)
        self.m142 = m142

    # ============================================================== 8 landing
    def landing(self):
        start = len(REC_TEXT[0]) + len(REC_TEXT[1])
        idx_ctx = [start + 20 + i for i in range(12)]          # T H E _ O T H E R _ D A
        idx_y = start + 32
        qbox = Square(BOX + 0.06, stroke_color=YELLOW, stroke_width=4).move_to([Q_X, ROW_Y_OPEN, 0])
        ctx_boxes = VGroup(*[ctx_box(ch).move_to([row_x(i), ROW_Y_OPEN, 0]) for i, ch in enumerate(CTX)])
        lead = MathTex(r"\cdots", color=PURPLE, font_size=40).set_opacity(0.6)
        lead.next_to(ctx_boxes, LEFT, buff=0.22)
        ybox_letter = Text("Y", font=SERIF, font_size=34, color=INK).move_to(qbox)
        one = MathTex(r"1\ \text{guess}", font_size=MATH, color=GREEN).next_to(qbox, RIGHT, buff=0.3)

        keep_idx = set(idx_ctx + [idx_y])
        drop_cells = [self.cells[i] for i in range(len(self.cells)) if i not in keep_idx]
        keep_cells = [self.cells[i] for i in idx_ctx + [idx_y]]
        # everything else on screen goes; anything that holds record cells (the record
        # group, or the cells themselves if the group was split) is handled cell by cell
        cell_ids = {id(c) for c in self.cells}
        rest = [m for m in self.visible()
                if not any(id(f) in cell_ids for f in m.get_family())]
        tiles = VGroup(*[tile(s) for s in ALPHA]).arrange(RIGHT, buff=0.06).move_to([0, TILE_Y, 0])
        self.exclude(tiles, "the cold-open alphabet tile row, returning (letters in their own "
                     "tiles, tiles 0.06 apart)")
        for j in list(range(0, 24)) + [25, 26]:
            tile_opacity(tiles[j], 0.22)
        # the Y is the answer to frame one: full blue with a white outline, to the end
        tiles[24][0].set_stroke(INK, width=3).set_fill(BLUE, opacity=0.35)
        chain = MathTex("27", r"\to", "13", r"\to", "6", r"\to", "3", r"\to", "2", r"\to", "1",
                        font_size=MATH)
        for i in range(1, 11, 2):
            chain[i].set_color(YELLOW)
        chain.move_to([0, CHAIN_Y, 0])
        five = MathTex(r"5\ \text{questions}", font_size=MATH, color=YELLOW).move_to([0, QLINE_Y, 0])

        dim_boxes = [b[0].copy().set_stroke(opacity=0.3).set_fill(opacity=0.05) for b in ctx_boxes]
        dim_q = qbox.copy().set_stroke(opacity=0.3)
        dim_lead = lead.copy().set_opacity(0.18)
        # the person's marker (and its tags) lingers after the rest of the line has gone,
        # and fades last as that person's record comes back
        person_ids = {id(f) for f in self.m142.get_family()}
        person = [m for m in rest if any(id(f) in person_ids for f in m.get_family())]
        others = [m for m in rest if all(m is not q for q in person)]
        with self.narrate("The hidden character from the start [pause 0.4] is the Y in the other "
                          "day.", speed=0.8) as beat:
            # 0. the summary line fades (0.65 s), the person's 1.42 last, and Shannon's record
            #    comes back (faint) with THE OTHER DAY at full strength once the marker is gone
            out_first = lambda t: smooth(min(1.0, t / 0.5))
            out_last = lambda t: smooth(float(np.clip((t - 0.3) / 0.38, 0, 1)))
            in_after = lambda t: smooth(float(np.clip((t - 0.7) / 0.3, 0, 1)))   # line gone first
            back_in = []
            for c in self.cells:
                o = 1.0 if any(c is k for k in keep_cells) else 0.22
                back_in.append(c.animate(rate_func=in_after).set_opacity(o) if isinstance(c, Text)
                               else c.animate(rate_func=in_after).set_stroke(opacity=o))
            self.play(*[FadeOut(m, rate_func=out_first) for m in others],
                      *[FadeOut(m, rate_func=out_last) for m in person], *back_in, run_time=1.3)
            rest = []
            # 1. the record goes; the cold-open row comes back faint, in its old place, and
            #    THE OTHER DAY comes back to full strength, each letter stepping under the box
            #    it belongs to (the Y under the ? box), clear of the row
            stage_y = ROW_Y_OPEN - 0.78
            staged = []
            for i, c in enumerate(keep_cells):
                x = row_x(i) if i < 12 else Q_X
                if isinstance(c, Text):
                    staged.append(c.animate.set_opacity(1.0).move_to([x, stage_y, 0]))
                else:                               # the open-box space: stroke only
                    staged.append(c.animate.set_stroke(opacity=1.0).move_to([x, stage_y - 0.07, 0]))
            # the record's letters are gone before the boxes come up between its rows
            gone = lambda t: smooth(min(1.0, t / 0.45))
            after = lambda t: smooth(max(0.0, (t - 0.4) / 0.6))
            self.play(*[FadeOut(c, rate_func=gone) for c in drop_cells],
                      *staged, *[FadeIn(b, rate_func=after) for b in dim_boxes],
                      FadeIn(dim_q, rate_func=after), FadeIn(dim_lead, rate_func=after),
                      run_time=beat.until("is", offset=-0.35, min_time=0.6))
            # 2. the phrase rises straight into its boxes, and the Y into the ? box as it
            #    is named
            self.play(LaggedStart(*[ReplacementTransform(self.cells[idx_ctx[i]], ctx_boxes[i][1])
                                    for i in range(12)], lag_ratio=0.04),
                      ReplacementTransform(self.cells[idx_y], ybox_letter),
                      run_time=beat.until("Y", offset=0.05, min_time=0.7))
            # 3. the boxes come to full strength, the 27 candidates return: frame one, re-seen
            # (the halving chain and its 5 come back faint under them, as at 0:17)
            chain.set_opacity(0.35)
            five.set_color(GRAY).set_opacity(0.8)
            self.play(*[ReplacementTransform(dim_boxes[i], ctx_boxes[i][0]) for i in range(12)],
                      ReplacementTransform(dim_lead, lead), ReplacementTransform(dim_q, qbox),
                      flag(ybox_letter, color=YELLOW), FadeIn(tiles, shift=0.1 * UP),
                      FadeIn(chain, shift=0.1 * UP), FadeIn(five, shift=0.1 * UP), run_time=0.9)
        with self.narrate("Shannon's subject needed one guess: [pause 0.3] is it Y? Splitting "
                          "the alphabet took five. In English, almost no letter arrives without "
                          "a past.") as beat:
            beat.wait_until("one guess", offset=-0.2)
            self.play(FadeIn(one, shift=0.1 * UP), run_time=0.6)
            # ... about this one letter: is it Y?
            beat.wait_until("is it", offset=-0.15)
            self.play(flag(VGroup(qbox, ybox_letter), color=YELLOW), run_time=0.7)
            # one guess against the halving's five questions
            beat.wait_until("Splitting", offset=-0.2)
            self.play(chain.animate.set_opacity(1.0), five.animate.set_color(YELLOW).set_opacity(1.0),
                      run_time=beat.until("five", offset=-0.1, min_time=0.7))
            self.play(flag(five), Indicate(chain, color=YELLOW, scale_factor=1.04), run_time=0.8)
            beat.wait_until("English", offset=-0.2)
            self.play(chain.animate.set_opacity(0.3),
                      five.animate.set_color(GRAY).set_opacity(0.8), pflash(VGroup(lead, ctx_boxes), scale=1.0), run_time=1.0)
