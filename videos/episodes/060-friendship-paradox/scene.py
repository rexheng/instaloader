"""Episode 60 - Why Your Friends Have More Friends Than You.

    videos/toolkit/render.sh --preview videos/episodes/060-friendship-paradox/scene.py Episode /tmp/ep60.mp4
    videos/toolkit/render.sh videos/episodes/060-friendship-paradox/scene.py Episode \
        videos/episodes/060-friendship-paradox/final.mp4

Data: Feld (1991, AJS) Fig. 1 / Table 1 (eight Marketville girls, Coleman 1961);
Ugander et al. (2011, arXiv:1111.4503); Christakis & Fowler (2010, PLoS ONE) Fig. 3, redrawn
from cf_fig3_digitized.json.  Numbers are recomputed in sim.py; see facts.md.

`python scene.py` runs the layout asserts (token / label / node clearance) without rendering.
"""
from __future__ import annotations

import contextlib
import json
from pathlib import Path

import numpy as np
from manim import *
from sample_space import *
import sample_space.voice as _ssvoice

# Round 2: sentences inside a beat are separated by 0.26 s (series default 0.38 s, which
# sounded metronomic); beat boundaries get BREAK seconds instead of the 0.35 s default.
_ssvoice.SENTENCE_PAUSE = 0.26
BREAK = 0.7

HERE = Path(__file__).resolve().parent
GRAY_T = "#9EA5AF"          # text-grade gray (names, ticks, citations): 7.3:1 on BG

# ----------------------------------------------------------------------------- data
NAMES = ["Betty", "Sue", "Alice", "Jane", "Pam", "Dale", "Carol", "Tina"]
EDGES = [("Betty", "Sue"), ("Sue", "Alice"), ("Sue", "Dale"), ("Sue", "Pam"),
         ("Alice", "Jane"), ("Alice", "Pam"), ("Alice", "Dale"), ("Jane", "Dale"),
         ("Pam", "Carol"), ("Carol", "Tina")]
NBR = {n: [] for n in NAMES}
for _a, _b in EDGES:
    NBR[_a].append(_b)
    NBR[_b].append(_a)
K = {n: len(NBR[n]) for n in NAMES}                       # 1,4,4,2,3,3,2,1
# each girl's friends' average (Feld 1991, p. 1465): shown in the landing
FAVG_TXT = {"Betty": "4", "Sue": "2.75", "Alice": "3", "Jane": "3.5", "Pam": "3.33",
            "Dale": "3.33", "Carol": "2", "Tina": "2"}

# real layout (left half of the frame)
P = {n: np.array([x, y, 0.0]) for n, (x, y) in {
    "Betty": (-5.85, 0.75), "Sue": (-4.4, 0.75), "Alice": (-2.4, 0.75), "Dale": (-3.4, 2.3),
    "Jane": (-1.35, 2.45), "Pam": (-3.4, -0.8), "Carol": (-2.2, -1.85), "Tina": (-0.8, -2.25),
}.items()}
NAME_DIR = {"Betty": DOWN, "Sue": UP, "Alice": RIGHT, "Dale": UP, "Jane": RIGHT,
            "Pam": LEFT, "Carol": DOWN, "Tina": RIGHT}
NAME_BUFF = {"Sue": 0.13}
# Sue's name sits up-LEFT of her node: the token parked at her end of the Sue-Dale edge
# used to cover the "e" (round 2, cap 7).  assert_token_clearance() checks every label.
NAME_SHIFT = {"Sue": LEFT * 0.55}
# where each girl's friends' average sits in the landing (free of edges and names)
FAVG_DIR = {"Betty": UP, "Sue": DOWN + 0.45 * LEFT, "Alice": DOWN, "Jane": UP,
            "Pam": RIGHT, "Dale": LEFT, "Tina": UP}

# "what if" ring: same girls, every count 2
RING_ORDER = ["Alice", "Jane", "Dale", "Sue", "Betty", "Pam", "Carol", "Tina"]
RING_C, RING_R = np.array([-3.0, 0.3, 0.0]), 1.9
RP = {n: RING_C + RING_R * np.array([np.cos(i * TAU / 8), np.sin(i * TAU / 8), 0.0])
      for i, n in enumerate(RING_ORDER)}
RING_EDGES = [(RING_ORDER[i], RING_ORDER[(i + 1) % 8]) for i in range(8)]


def ring_name_dir(n):
    v = RP[n] - RING_C
    return v / np.linalg.norm(v)          # radially outward, away from both ring edges


# sorted beam (insight): column k at BX(k), two girls per column
COLS = {1: ["Betty", "Tina"], 2: ["Jane", "Carol"], 3: ["Pam", "Dale"], 4: ["Sue", "Alice"]}
NODE_DX = 0.8                                  # every girl sits 0.8 from the next (round 3:
BEAM_PER = 2 * NODE_DX                         # room for her name under her node)


def BX(k):                                    # beam x for a friend count k (may be fractional)
    return -7.12 + BEAM_PER * k               # Betty at -5.92 ... Alice at -0.32


# Round 3 layout, top to bottom: token stacks, nodes, NAMES (they now ride onto the beam),
# beam, fulcra, distance line, squares.  Once the stacks leave ("Split Sue's four") the whole
# picture lifts by LIFT and the lower-left band holds the ring thumbnail.
GIRL_Y, PAIR_DX = 0.84, NODE_DX / 2
NODE_RB = 0.36 * 0.88                          # node radius on the beam
BNAME_FONT = 20
BNAME_TOP = GIRL_Y - NODE_RB - 0.15            # top of the name labels under the nodes
BEAM_Y = -0.04                                 # 0.16 under the lowest name ink ("Betty")
SP = {}
for _k, (_l, _r) in COLS.items():
    SP[_l] = np.array([BX(_k) - PAIR_DX, GIRL_Y, 0.0])
    SP[_r] = np.array([BX(_k) + PAIR_DX, GIRL_Y, 0.0])
TOK_SIDE, TOK_GAP = 0.38, 0.06
DEV_Y = -0.80                                 # distance-from-the-balance-point line
SQ_SCALE = BEAM_PER / 4                       # variance squares drawn at exactly 1/4 scale
SQ_TOP = DEV_Y - 0.55                         # their top edge
AREA_Y = SQ_TOP - 1.5 * SQ_SCALE - 0.27       # their area labels
LANE_Y = AREA_Y - 0.36                        # flight lane of the area labels into "10"
LIFT = 1.6                                    # phase B: the beam picture moves up
RING_S, RING_C2 = 0.42, np.array([-5.15, -1.62, 0.0])   # ring thumbnail (the 2:23 callback)

R = 0.36                                       # node radius
NAME_BUFF_DEFAULT = 0.2
NET_TOK = 0.30                                 # network token (numbered square) side
NET_TOK_FONT = 30
TOK_GAP_NODE = 0.11                            # token clears its receiver's circle by this
SHORT_EDGE, LANE, LANE_RING = 1.65, 0.17, 0.22   # tokens on short edges keep right

# bar panel (right half)
X0, UNIT = 1.3, 1.2                            # bar origin, units per friend (girls)
FB_UNIT = 4.8 / 800                            # units per friend (Facebook), before scaling
Y_GIRL, Y_FRIEND, BAR_H, Y_AX = 2.78, 1.5, 0.42, 0.86
FB_S, FB_C0, FB_C1 = 1.25, np.array([3.75, 1.72, 0.0]), np.array([0.0, 1.3, 0.0])

# equation rows (right panel)
RX = 3.45                                      # row centre x
ROW_M0 = -0.9                                  # main row (the counter) before the variance step
ROW_M = -2.22                                  # main row after it moves down
ROW_V = -0.45                                  # variance row (flat)
ROW_S = -1.15                                  # the "split Sue's four" row (flat)
SX = 0.8                                       # left edge of the split rows
S_FONT = 38

# Christakis & Fowler (2010) Fig. 3, digitized (whole cases)
CF = json.loads((HERE / "cf_fig3_digitized.json").read_text())
# cumulative logistic c/(1+exp(-(t-m)/s)), shared c and s, random group shifted by the
# published lead 13.9 days; c, m, s least-squares fitted to the redrawn data (sim.py).
# A free fit of the shift to the redrawn data gives 14.5 days (inside C&F's 9.9-16.6 CI).
LOG_C, LOG_M, LOG_S, LEAD, SELF_LEAD = 8.320, 52.79, 21.86, 13.9, 3.2

NARR = {
    "open1": "Eight girls at an Illinois high school, and every friendship between them.",
    "open2": "On average, each girl has two and a half friends.",
    "open3": "How many friends does the average friend have? Pick one. [pause 2.0]",
    "stakes": "It matters to health researchers choosing whom to watch for flu: random "
              "students, or the friends those students name.",
    "guess": "The natural guess is two and a half again: every friend is one of these same "
             "eight girls.",
    "ring": "Check that on a rewired class where every girl has two friends. Send a token both "
            "ways along every friendship.",
    "ring2": "Each token reads the friend count where it lands, here always two. Both averages "
             "are two: the guess holds.",
    "recount": "Now restore the real friendships and send the tokens again. They read one, two, "
               "three, or four. Twenty tokens add up to sixty: friends average three.",
    "fail": "The guess was half a friend too low: friends average twenty percent more than "
            "girls. The tokens piled up unevenly: four on Sue, four on Alice, one on Betty.",
    "line": "Line the girls up by friend count: two at each count, from one to four, so they "
            "balance at two and a half.",
    "stack": "The tokens stack higher on the right, one per friend, so they balance at three.",
    "sue": "Sue holds four tokens, each worth four: sixteen. A girl with k friends adds k "
           "squared on top, and k on the bottom. Sixty over twenty.",
    "divide": "Divide top and bottom by the eight girls: the average of k squared, seven and a "
              "half, over the average girl, two and a half.",
    "variance": "Measure each girl's distance from the balance point and square it: two and a "
                "quarter at the ends, a quarter in the middle. They average one and a quarter, "
                "the variance, sigma squared. [pause]",
    "split": "Split Sue's four into the balance point, two and a half, plus her distance, one "
             "and a half. Squaring gives two and a half squared, her distance squared, and a "
             "cross term. [pause] Every girl splits this way, and because the beam balances, the "
             "left and right distances add to zero and the cross terms cancel. [pause]",
    "result": "So the average of k squared is mu squared plus sigma squared, and friends average "
              "mu, plus sigma squared over mu. Here that's two and a half, plus a half: exactly "
              "the extra half friend we measured. The ring had no spread, so it had no gap. "
              "[pause 1.3]",
    "fb": "In twenty eleven, Facebook users averaged about a hundred and ninety friends. If every "
          "friendship sent tokens, what would the tokens average? [pause 1.6]",
    "fb2": "About six hundred and thirty five. A few users had thousands of friends, so the "
           "spread term is more than twice the mean itself.",
    "cf": "In twenty oh nine, Christakis and Fowler tested this at Harvard. Friends sit closer "
          "to everyone else in the network, so they should catch it first. They tracked flu diagnoses "
          "in three hundred nineteen random students and four hundred twenty five friends they "
          "named. The friends' curve rose first: fitted curves put them thirteen point nine days "
          "ahead. With self-reported symptoms, the lead shrank to about three.",
    "land1": "Back to the eight girls. Five have fewer friends than their friends average, and "
             "only Sue and Alice have more.",
    "land2": "Follow any friendship, yours included, and you land on a Sue four times as often "
             "as on a Betty. So Betty looks at her one friend and sees four. From most seats in "
             "this class, the view is the same.",
}


# ----------------------------------------------------------------------------- geometry
def unit(v):
    return v / np.linalg.norm(v)


def name_label(n, pos=P):
    t = Text(n, font=SERIF, font_size=26, color=GRAY_T)
    t.next_to(Circle(radius=R).move_to(pos[n]), NAME_DIR[n], buff=NAME_BUFF.get(n, NAME_BUFF_DEFAULT))
    t.shift(NAME_SHIFT.get(n, ORIGIN))
    return t


def lane_of(a, b, pos):
    if np.linalg.norm(pos[a] - pos[b]) >= SHORT_EDGE:
        return 0.0
    return LANE_RING if pos is RP else LANE


def tok_off(u):
    """Distance from a node centre to a token centre along direction u, so that the token
    square clears the circle by TOK_GAP_NODE whatever the edge angle."""
    return R + TOK_GAP_NODE + NET_TOK / 2 * (abs(u[0]) + abs(u[1]))


def _lane_shift(s, r, pos):
    d = unit(pos[r] - pos[s])                     # direction of travel
    return np.array([d[1], -d[0], 0.0]) * lane_of(s, r, pos)    # keep to the right


def tok_end(s, r, pos):
    """Where a token sent along s->r comes to rest (just outside the receiver)."""
    u = unit(pos[s] - pos[r])
    return pos[r] + u * tok_off(u) + _lane_shift(s, r, pos)


def tok_start(s, r, pos):
    u = unit(pos[r] - pos[s])
    return pos[s] + u * tok_off(u) + _lane_shift(s, r, pos)


def edge_line(a, b, pos, color=GRAY, width=3.0):
    d = unit(pos[b] - pos[a])
    return Line(pos[a] + d * R, pos[b] - d * R, color=color, stroke_width=width)


def _box_gap(b1, b2):
    dx = max(b1[0] - b2[2], b2[0] - b1[2], 0.0)
    dy = max(b1[1] - b2[3], b2[1] - b1[3], 0.0)
    return float(np.hypot(dx, dy))


def _bbox(m):
    return (m.get_left()[0], m.get_bottom()[1], m.get_right()[0], m.get_top()[1])


def token_layout_issues(pos, edges, labels, min_label_gap=0.15, min_tok_gap=0.04,
                        min_node_gap=0.05):
    """Every parked token position (both directions of every edge) against every name
    label, every node circle, every other token and every other edge line."""
    issues = []
    h = NET_TOK / 2
    toks = []
    for a, b in edges:
        for s, r in ((a, b), (b, a)):
            c = tok_end(s, r, pos)
            toks.append(((s, r), (c[0] - h, c[1] - h, c[0] + h, c[1] + h)))
    for (sr, tb) in toks:
        for n, lab in labels.items():
            g = _box_gap(tb, _bbox(lab))
            if g < min_label_gap:
                issues.append(f"token {sr[0]}->{sr[1]} is {g:.3f} from label {n!r}")
        for n, c in pos.items():
            qx, qy = np.clip(c[0], tb[0], tb[2]), np.clip(c[1], tb[1], tb[3])
            g = float(np.hypot(c[0] - qx, c[1] - qy)) - R
            if g < min_node_gap:
                issues.append(f"token {sr[0]}->{sr[1]} is {g:.3f} from node {n}")
        for a, b in edges:
            if {a, b} == set(sr):
                continue
            ln = edge_line(a, b, pos)
            pts = np.array([ln.point_from_proportion(t) for t in np.linspace(0, 1, 60)])
            inside = ((pts[:, 0] > tb[0] - 0.02) & (pts[:, 0] < tb[2] + 0.02) &
                      (pts[:, 1] > tb[1] - 0.02) & (pts[:, 1] < tb[3] + 0.02))
            if inside.any():
                issues.append(f"edge {a}-{b} runs through token {sr[0]}->{sr[1]}")
    for i in range(len(toks)):
        for j in range(i + 1, len(toks)):
            g = _box_gap(toks[i][1], toks[j][1])
            if g < min_tok_gap:
                issues.append(f"tokens {toks[i][0]} and {toks[j][0]} are {g:.3f} apart")
    return issues


def ring_label(n):
    t = Text(n, font=SERIF, font_size=26, color=GRAY_T)
    return t.next_to(Circle(radius=R).move_to(RP[n]), ring_name_dir(n), buff=NAME_BUFF_DEFAULT)


def assert_token_clearance():
    """Round-2 fix: the automated clearance assert the critics asked for."""
    real = {n: name_label(n) for n in NAMES}
    issues = token_layout_issues(P, EDGES, real)
    issues += token_layout_issues(RP, RING_EDGES, {n: ring_label(n) for n in NAMES})
    if issues:
        raise AssertionError("token layout:\n  " + "\n  ".join(issues))


# ----------------------------------------------------------------------------- helpers
def tfc(src, dst, **kw):
    """TransformFromCopy that is safe for objects with updaters (DecimalNumber etc.)."""
    return ReplacementTransform(src.copy().clear_updaters(), dst, **kw)


def net_token(val):
    """A token as it travels the network: a yellow square that shows the count it reads."""
    sq = Square(NET_TOK, stroke_width=0, fill_color=YELLOW, fill_opacity=1.0)
    lab = MathTex(str(val), font_size=NET_TOK_FONT, color=BG).move_to(sq)
    return VGroup(sq, lab)


def pulse(m, s=1.3, run_time=0.8):
    return m.animate(rate_func=there_and_back, run_time=run_time).scale(s)


def frac(num, den, size=46, color_num=INK, color_den=INK, bar_color=INK, buff=0.1):
    n = num if isinstance(num, Mobject) else MathTex(num, font_size=size, color=color_num)
    d = den if isinstance(den, Mobject) else MathTex(den, font_size=size, color=color_den)
    w = max(n.width, d.width) + 0.18
    bar = Line(LEFT * w / 2, RIGHT * w / 2, stroke_width=3, color=bar_color)
    bar.ss_bg = True                     # numerator / denominator sit on it by design
    n.next_to(bar, UP, buff=buff)
    d.next_to(bar, DOWN, buff=buff)
    g = VGroup(n, bar, d)
    g.num, g.bar, g.den = n, bar, d
    return g


def row(*parts, buff=0.2):
    """Arrange equation parts left to right, centring fractions' bars on the '=' axis."""
    g = VGroup(*parts).arrange(RIGHT, buff=buff)
    axis_y = None
    for p in parts:
        if hasattr(p, "bar"):
            axis_y = p.bar.get_center()[1]
            break
    if axis_y is not None:
        for p in parts:
            if not hasattr(p, "bar"):
                p.set_y(axis_y)
    return g


def place(g, y, x=RX):
    """Put a row so that its fraction bars sit at height y and it is centred on x."""
    first = next(p for p in g if hasattr(p, "bar"))
    g.shift(UP * (y - first.bar.get_y()))
    g.set_x(x)
    return g


def window(t0, t1, total):
    """Rate function that runs an animation only between t0 and t1 seconds of a play()
    lasting `total` seconds (so one play can hold staggered starts without Succession)."""
    def f(t):
        return smooth(float(np.clip((t * total - t0) / max(t1 - t0, 1e-3), 0, 1)))
    return f


def swap(old, new, total, t_out=0.35, t_in=(0.4, 0.85)):
    """Changed content never crossfades: the old term leaves upward, then the new one
    rises into place (round 2: no double-exposed glyphs)."""
    a1 = min(t_in[1], total)
    return [FadeOut(old, shift=UP * 0.12, rate_func=window(0, t_out, total)),
            FadeIn(new, shift=UP * 0.12, rate_func=window(min(t_in[0], a1 - 0.2), a1, total))]


def M(s, color=INK, size=46):
    return MathTex(s, font_size=size, color=color)


def along(mob, pts, fade_tail=0.0):
    """Move mob along a smooth path through pts (optionally fading over the last part)."""
    path = VMobject().set_points_smoothly([np.array(p, dtype=float) for p in pts])

    def upd(m, a):
        m.move_to(path.point_from_proportion(smooth(a)))
        if fade_tail:
            m.set_opacity(float(np.clip((1 - a) / fade_tail, 0, 1)))
    return UpdateFromAlphaFunc(mob, upd)


def count_swap(old, new, a, b, t_out=0.42, t_in=0.58):
    """A node's count rides with the node from a to b; the old count fades out before the
    new one fades in (no crossfade of different digits)."""
    new.move_to(a).set_opacity(0)

    def upd(_, alpha):
        p = a + (b - a) * smooth(alpha)
        old.move_to(p)
        new.move_to(p)
        old.set_opacity(float(1 - np.clip(alpha / t_out, 0, 1)))
        new.set_opacity(float(np.clip((alpha - t_in) / (1 - t_in), 0, 1)))
    return UpdateFromAlphaFunc(VGroup(old, new), upd)


def stepped_upto(ax, steps, n, day):
    """The cumulative step curve revealed up to `day` (both groups share one calendar)."""
    day = max(day, 0.05)
    pts = [ax.c2p(0, 0)]
    level = 0.0
    for d, cases in steps[1:]:
        if d > day:
            break
        pts.append(ax.c2p(d, level))
        level = 100.0 * cases / n
        pts.append(ax.c2p(d, level))
    pts.append(ax.c2p(day, level))
    m = VMobject()
    m.set_points_as_corners(pts)
    return m


def logistic(t, shift=0.0):
    return LOG_C / (1 + np.exp(-(t - LOG_M - shift) / LOG_S))


TEXT_TYPES = (Text, MathTex, SingleStringMathTex, Tex, DecimalNumber)


class Episode(NarratedScene):
    EPISODE = 60
    TITLE = "Why Your Friends Have More Friends Than You"
    PRONUNCIATIONS = {"Christakis": "/kɹɪstˈɑkɪs/"}
    SPEED = 0.82

    # ------------------------------------------------------------------ checks
    @contextlib.contextmanager
    def narrate(self, text, **kw):
        with super().narrate(text, **kw) as beat:
            yield beat
        self.audit(f"end of beat {beat.index}")

    def audit(self, tag, gap=0.12):
        """Stricter than the toolkit check: visible text must keep `gap` from other text
        and from small shapes (tokens, nodes, squares), and no line may enter a text box
        grown by `gap`.  Warnings land in narration.json."""
        texts, shapes = [], []

        def vis(x):
            try:
                op = max(x.get_fill_opacity(), x.get_stroke_opacity() if x.get_stroke_width() > 0 else 0)
            except Exception:
                op = 1.0
            return len(x.points) > 0 and op > 0.06

        def collect(ms):
            for m in ms:
                if getattr(m, "ss_allow_overlap", False):
                    continue
                if isinstance(m, TEXT_TYPES):
                    if any(vis(x) for x in m.get_family()) and m.width > 0:
                        texts.append(m)
                    continue
                if isinstance(m, VMobject) and vis(m):
                    shapes.append(m)
                collect(m.submobjects)
        collect(self.mobjects)
        boxes = [_bbox(t) for t in texts]
        out = []
        for i in range(len(texts)):
            for j in range(i + 1, len(texts)):
                bi, bj = getattr(texts[i], "ss_block", None), getattr(texts[j], "ss_block", None)
                if bi is not None and bi == bj:
                    continue
                if _box_gap(boxes[i], boxes[j]) < gap:
                    out.append(f"{type(texts[i]).__name__}({getattr(texts[i], 'tex_string', getattr(texts[i], 'text', ''))[:18]!r}) "
                               f"near {type(texts[j]).__name__}({getattr(texts[j], 'tex_string', getattr(texts[j], 'text', ''))[:18]!r})")
        for t, b in zip(texts, boxes):
            host = getattr(t, "ss_host", None)
            if host is not None:            # a digit printed on an opaque token
                continue
            for s in shapes:
                if s is host or getattr(s, "ss_bg", False):
                    continue
                sb = _bbox(s)
                if _box_gap(b, sb) >= gap or max(sb[2] - sb[0], sb[3] - sb[1]) < 0.03:
                    continue
                if max(sb[2] - sb[0], sb[3] - sb[1]) < 0.9 and not isinstance(s, Line):   # small shape
                    out.append(f"{type(t).__name__}({getattr(t, 'tex_string', getattr(t, 'text', ''))[:18]!r}) near small {type(s).__name__}")
                    continue
                n = max(2, len(s.points) // 4)
                pts = np.array([s.point_from_proportion(a) for a in np.linspace(0, 1, min(400, 30 * n))])
                inside = ((pts[:, 0] > b[0] - gap) & (pts[:, 0] < b[2] + gap) &
                          (pts[:, 1] > b[1] - gap) & (pts[:, 1] < b[3] + gap))
                if inside.any():
                    out.append(f"{type(s).__name__} enters {type(t).__name__}({getattr(t, 'tex_string', getattr(t, 'text', ''))[:18]!r})")
        for o in sorted(set(out)):
            self._warn(self.time, f"{tag} audit: {o}")
        return out

    # ------------------------------------------------------------------ building blocks
    def build_network(self):
        circ, num, name = {}, {}, {}
        for n in NAMES:
            c = Circle(radius=R, stroke_color=BLUE, stroke_width=3.5, fill_color=BLUE,
                       fill_opacity=0.16).move_to(P[n])
            c.ss_bg = True                       # counts sit inside their node by design
            circ[n] = c
            num[n] = MathTex(str(K[n]), font_size=38, color=INK).move_to(P[n])
            name[n] = name_label(n)
        edges = {frozenset(e): edge_line(*e, P) for e in EDGES}
        return circ, num, name, edges

    def tokens_for(self, edges, pos, vals):
        """One numbered token per direction of every edge: (sender, receiver, tok, start, end)."""
        out = []
        for a, b in edges:
            for s, r in ((a, b), (b, a)):
                d = net_token(vals[r]).move_to(tok_start(s, r, pos))
                d[1].ss_host = d[0]
                d[0].set_fill(opacity=0)
                d[1].set_opacity(0)
                out.append((s, r, d, tok_start(s, r, pos), tok_end(s, r, pos)))
        return out

    def fly_tokens(self, toks, run_time, n_tr, s_tr, kvals, lag=None):
        """Senders launch one after another; a token shows its count as it lands, and each
        landing increments the live counters.  lag: start offset between senders as a
        fraction of the play (None = the slower, readable stagger)."""
        senders = [n for n in NAMES if any(t[0] == n for t in toks)]
        ns = len(senders)
        windows = []
        for s, r, *_ in toks:
            i = senders.index(s)
            if lag is None:
                slot = 1.0 / (ns + 1.2)
                windows.append((i * slot, i * slot + 2.2 * slot))
            else:
                windows.append((i * lag, i * lag + 1.0 - (ns - 1) * lag))
        group = VGroup(*[t[2] for t in toks])

        def upd(_, alpha):
            n = 0
            tot = 0
            for (s, r, d, a, b), (w0, w1) in zip(toks, windows):
                if alpha <= w0:
                    p = 0.0
                elif alpha >= w1:
                    p = 1.0
                else:
                    p = smooth((alpha - w0) / (w1 - w0))
                d.move_to(a + (b - a) * p)
                d[0].set_fill(opacity=0.0 if alpha <= w0 else min(1.0, 0.25 + 3 * p))
                d[1].set_opacity(0.0 if alpha <= w0 else float(np.clip((p - 0.7) / 0.3, 0, 1)))
                if alpha >= w1:
                    n += 1
                    tot += kvals[r]
            n_tr.set_value(n)
            s_tr.set_value(tot)
        return UpdateFromAlphaFunc(group, upd, run_time=run_time, rate_func=linear)

    def make_bars(self):
        """Two horizontal bars on a shared axis.  Average girl: BLUE.  Average friend: a
        YELLOW outline (the total), filled BLUE up to the girl average (mu) and PURPLE beyond
        it (the excess, sigma^2/mu).  Geometry lives in self.G so the panel can be moved and
        rescaled for the Facebook beat."""
        G = self.G = dict(x0=X0, yg=Y_GIRL, yf=Y_FRIEND, yax=Y_AX, s=1.0)
        self.Lg, self.Lf, self.Lb, self.Po = (ValueTracker(0.0) for _ in range(4))
        self.Dm = ValueTracker(1.0)                      # dims the whole bar panel
        self.Fo = ValueTracker(1.0)                      # fades the friend bar alone (reset)
        self.gv, self.fv = ValueTracker(0.0), ValueTracker(0.0)

        def fill_rect(color, y):
            r = Rectangle(width=1.0, height=BAR_H, stroke_width=0, fill_color=color,
                          fill_opacity=0.9).move_to([X0 + 0.5, y, 0])
            r.ss_bg = True                               # bar labels sit next to bars
            return r

        self.gbar = fill_rect(BLUE, Y_GIRL)
        self.fblue = fill_rect(BLUE, Y_FRIEND)
        self.fpurp = fill_rect(PURPLE, Y_FRIEND)
        self.fout = Rectangle(width=1.0, height=BAR_H, stroke_color=YELLOW, stroke_width=4,
                              fill_opacity=0).move_to([X0 + 0.5, Y_FRIEND, 0])

        def seg(m, a, b, y, op):
            w = max(b - a, 1e-3)
            m.stretch_to_fit_width(w).move_to([G["x0"] + a + w / 2, y, 0])
            m.set_fill(opacity=op * self.Dm.get_value() if w > 0.01 else 0.0)

        def upd_g(m):
            seg(m, 0.0, self.Lg.get_value(), G["yg"], 0.9)

        def upd_b(m):
            seg(m, 0.0, min(self.Lb.get_value(), self.Lf.get_value()), G["yf"],
                0.9 * self.Fo.get_value())

        def upd_p(m):
            seg(m, min(self.Lb.get_value(), self.Lf.get_value()), self.Lf.get_value(), G["yf"],
                0.9 * self.Po.get_value() * self.Fo.get_value())

        def upd_o(m):
            w = max(self.Lf.get_value(), 1e-3)
            m.stretch_to_fit_width(w).move_to([G["x0"] + w / 2, G["yf"], 0])
            m.set_stroke(opacity=self.Dm.get_value() * self.Fo.get_value() if w > 0.01 else 0.0)

        self._bar_upd = [(self.gbar, upd_g), (self.fblue, upd_b), (self.fpurp, upd_p),
                         (self.fout, upd_o)]
        for m, f in self._bar_upd:
            m.add_updater(f)

        self.glabel = Text("average girl", font=SERIF, font_size=28, color=INK)
        self.glabel.move_to([X0, Y_GIRL + 0.55, 0], aligned_edge=LEFT)
        self.flabel = Text("average friend", font=SERIF, font_size=28, color=INK)
        self.flabel.move_to([X0, Y_FRIEND + 0.6, 0], aligned_edge=LEFT)

        self.gnum = DecimalNumber(0, num_decimal_places=1, font_size=40, color=BLUE)
        self.fnum = DecimalNumber(0, num_decimal_places=1, font_size=40, color=YELLOW)

        def upd_gn(m):
            m.set_value(self.gv.get_value())
            m.next_to([G["x0"] + max(self.Lg.get_value(), 0), G["yg"], 0], RIGHT, buff=0.2)

        def upd_fn(m):
            m.set_value(self.fv.get_value())
            m.next_to([G["x0"] + max(self.Lf.get_value(), 0), G["yf"], 0], RIGHT, buff=0.2)
        self.gnum.add_updater(upd_gn)
        self.fnum.add_updater(upd_fn)
        self._num_upd = [(self.gnum, upd_gn), (self.fnum, upd_fn)]

        # axis 0..4 friends
        self.ax_line = Line([X0, Y_AX, 0], [X0 + 4 * UNIT, Y_AX, 0], color=GRAY, stroke_width=2.5)
        self.ax_ticks = VGroup(*[Line([X0 + v * UNIT, Y_AX - 0.07, 0], [X0 + v * UNIT, Y_AX + 0.07, 0],
                                      color=GRAY, stroke_width=2.5) for v in range(5)])
        self.ax_nums = VGroup(*[MathTex(str(v), font_size=30, color=GRAY_T).next_to(
            [X0 + v * UNIT, Y_AX, 0], DOWN, buff=0.16) for v in range(5)])
        self.ax_title = Text("friends (count)", font=SERIF, font_size=26, color=GRAY_T)
        self.ax_title.next_to(self.ax_nums, DOWN, buff=0.14).align_to(self.ax_line, RIGHT)
        for t in self.ax_ticks:
            t.ss_bg = True
        self.axis = VGroup(self.ax_line, self.ax_ticks, self.ax_nums, self.ax_title)

    def guess_rect(self, length):
        r = Rectangle(width=length, height=BAR_H + 0.08, stroke_color=GRAY, stroke_width=3)
        r.move_to([X0 + length / 2, Y_FRIEND, 0])
        d = DashedVMobject(r, num_dashes=int(12 + 6 * length), dashed_ratio=0.55)
        d.ss_bg = True                                    # "guess" is written inside it
        return d

    def make_counter(self):
        """Live tally: (sum of counts) / (tokens) = average."""
        self.n_tr, self.s_tr = ValueTracker(0), ValueTracker(0)
        self.c_op = ValueTracker(1.0)                    # fades the tally digits as a whole
        self.c_num = DecimalNumber(0, num_decimal_places=0, font_size=44, color=YELLOW)
        self.c_den = DecimalNumber(0, num_decimal_places=0, font_size=44, color=YELLOW)
        self.c_lab_n = Text("sum of counts", font=SERIF, font_size=26, color=INK)
        self.c_lab_d = Text("tokens", font=SERIF, font_size=26, color=INK)
        self.c_lab = frac(self.c_lab_n, self.c_lab_d, buff=0.14)
        self.c_eq1 = MathTex("=", font_size=46)
        self.c_frac = frac(self.c_num, self.c_den, buff=0.12)
        self.c_frac.bar.set_width(0.9)
        self.c_eq2 = MathTex("=", font_size=46)
        self.c_res = DecimalNumber(3.0, num_decimal_places=1, font_size=46, color=YELLOW)
        self.counter = row(self.c_lab, self.c_eq1, self.c_frac, self.c_eq2, self.c_res, buff=0.2)
        place(self.counter, ROW_M0, x=3.45)
        cx = self.c_frac.bar.get_center()

        def upd_num(m):
            m.set_value(self.s_tr.get_value())
            m.next_to(cx, UP, buff=0.12)
            m.set_opacity(self.c_op.get_value() if self.n_tr.get_value() > 0.5 else 0.0)

        def upd_den(m):
            m.set_value(self.n_tr.get_value())
            m.next_to(cx, DOWN, buff=0.12)
            m.set_opacity(self.c_op.get_value() if self.n_tr.get_value() > 0.5 else 0.0)
        self.c_num.add_updater(upd_num)
        self.c_den.add_updater(upd_den)

    # ------------------------------------------------------------------ the episode
    def construct(self):
        assert_token_clearance()
        circ, num, name, edges = self.build_network()
        self.make_bars()
        self.make_counter()
        feld = citation("Feld, 1991 · Am. J. Sociology · data: Coleman, 1961", color=GRAY_T)

        # ============================================================ 1. cold open
        for n in NAMES:                                   # first frame: the network, at 70 %
            circ[n].set_stroke(opacity=0.7).set_fill(opacity=0.11)
            name[n].set_opacity(0.7)
        self.add(*circ.values(), *name.values(), feld)
        with self.narrate(NARR["open1"], gap=0.2) as beat:
            self.play(LaggedStart(*[AnimationGroup(
                circ[n].animate.set_stroke(opacity=1.0).set_fill(opacity=0.16),
                name[n].animate.set_opacity(1.0)) for n in NAMES], lag_ratio=0.15),
                run_time=beat.until("every friendship", offset=-0.1, min_time=1.0))
            self.play(LaggedStart(*[Create(edges[frozenset(e)]) for e in EDGES], lag_ratio=0.12),
                      run_time=min(2.2, beat.remaining()))

        with self.narrate(NARR["open2"], gap=0.2) as beat:
            self.play(LaggedStart(*[FadeIn(num[n], scale=0.6) for n in NAMES], lag_ratio=0.1),
                      FadeIn(self.glabel), Create(self.axis),
                      run_time=beat.until("two and a half", offset=-0.3, min_time=1.0))
            self.add(self.gbar, self.gnum)
            copies = VGroup(*[num[n].copy() for n in NAMES])
            target = [X0 + 2.5 * UNIT + 0.45, Y_GIRL, 0]
            self.play(self.Lg.animate.set_value(2.5 * UNIT), self.gv.animate.set_value(2.5),
                      LaggedStart(*[c.animate.move_to(target).set_opacity(0) for c in copies],
                                  lag_ratio=0.05), run_time=1.3)
            self.remove(copies)

        # the "?" stops on three candidate answers: the girl average 2.5 (dashed line from
        # the girl bar), 3 and 4 (ghost drop lines above the axis ticks)
        qmark = MathTex("?", font_size=46, color=YELLOW).move_to([X0 + 0.3, Y_FRIEND, 0])
        top_y = Y_GIRL - BAR_H / 2 - 0.05
        ref = DashedLine([X0 + 2.5 * UNIT, top_y, 0], [X0 + 2.5 * UNIT, Y_FRIEND + 0.3, 0],
                         color=GRAY, stroke_width=2.5, dash_length=0.08)
        ghosts = VGroup(*[DashedLine([X0 + v * UNIT, top_y - 0.12, 0], [X0 + v * UNIT, Y_FRIEND + 0.3, 0],
                                     color=GRAY, stroke_width=2.5, dash_length=0.08).set_opacity(0.6)
                          for v in (3, 4)])
        # round 3: the three candidates are numbers the viewer can pick, each under its line
        cands = VGroup(*[MathTex(t, font_size=40, color=YELLOW).move_to([X0 + v * UNIT, Y_FRIEND, 0])
                         for t, v in (("2.5", 2.5), ("3", 3), ("4", 4))])
        with self.narrate(NARR["open3"], gap=0.1) as beat:
            self.play(FadeIn(self.flabel), FadeIn(qmark, scale=0.7),
                      run_time=beat.until("average friend", offset=-0.3, min_time=0.6))
            self.play(LaggedStart(*[AnimationGroup(Create(ln), FadeIn(c, shift=0.15 * DOWN))
                                    for ln, c in zip((ref, ghosts[0], ghosts[1]), cands)],
                                  lag_ratio=0.45),
                      run_time=min(1.2, max(0.8, beat.until("Pick", offset=-0.15))))
            beat.wait_until("Pick", offset=-0.1)
            self.play(LaggedStart(*[Indicate(c, color=YELLOW, scale_factor=1.25) for c in cands],
                                  lag_ratio=0.35), run_time=1.3)

        # ============================================================ 2. stakes
        lab_r = Text("random", font=SERIF, font_size=26, color=BLUE).next_to(circ["Jane"], UP, buff=0.2)
        lab_f = Text("named friend", font=SERIF, font_size=26, color=YELLOW)
        lab_f.next_to(circ["Alice"], DOWN, buff=0.2).shift(RIGHT * 0.95)
        arrow = Arrow(P["Jane"] + unit(P["Alice"] - P["Jane"]) * (R + 0.16),
                      P["Alice"] + unit(P["Jane"] - P["Alice"]) * (R + 0.14),
                      buff=0, color=YELLOW, stroke_width=5, max_tip_length_to_length_ratio=0.25)
        with self.narrate(NARR["stakes"], gap=BREAK) as beat:
            self.play(Indicate(qmark, color=YELLOW, scale_factor=1.35), run_time=0.9)
            beat.wait_until("whom to watch", offset=-0.1)
            self.play(circ["Jane"].animate.set_stroke(width=8), run_time=0.8)
            beat.wait_until("random students", offset=-0.15)
            self.play(FadeIn(lab_r, shift=0.1 * DOWN), run_time=0.7)
            beat.wait_until("friends those", offset=-0.1)
            self.play(GrowArrow(arrow), run_time=0.8)
            self.play(circ["Alice"].animate.set_stroke(YELLOW, width=8), FadeIn(lab_f, shift=0.1 * UP),
                      run_time=0.8)

        # ============================================================ 3. naive build
        guess = self.guess_rect(2.5 * UNIT)
        guess_lab = Text("guess", font=SERIF, font_size=26, color=GRAY_T)
        guess_lab.move_to([X0 + 0.17, Y_FRIEND, 0], aligned_edge=LEFT)
        with self.narrate(NARR["guess"]) as beat:
            beat.wait_until("natural guess", offset=-0.25)
            self.play(FadeOut(VGroup(lab_r, lab_f, arrow)),
                      circ["Jane"].animate.set_stroke(BLUE, width=3.5),
                      circ["Alice"].animate.set_stroke(BLUE, width=3.5),
                      GrowFromEdge(guess, LEFT), flag(self.gnum, color=BLUE), FadeOut(ghosts),
                      FadeOut(cands, rate_func=window(0, 0.45, 1.2)),
                      qmark.animate.next_to(guess, RIGHT, buff=0.15), run_time=1.2)
            self.play(FadeIn(guess_lab), FadeOut(ref), run_time=0.6)
            beat.wait_until("eight girls", offset=-0.1)
            self.play(LaggedStart(*[Indicate(circ[n], color=BLUE, scale_factor=1.12)
                                    for n in NAMES], lag_ratio=0.06), run_time=1.0)

        # ---- the ring (hypothetical)
        keep = [e for e in RING_EDGES if frozenset(e) in edges]
        drop = [k for k in edges if k not in {frozenset(e) for e in RING_EDGES}]
        new = [e for e in RING_EDGES if frozenset(e) not in edges]
        ring_edges = {frozenset(e): edge_line(*e, RP) for e in RING_EDGES}
        ring_nums = {n: MathTex("2", font_size=38, color=INK) for n in NAMES}
        ring_names = {n: ring_label(n) for n in NAMES}
        whatif = VGroup(Text("what if:", font=SERIF, font_size=26, color=GRAY_T),
                        Text("everyone has 2", font=SERIF, font_size=26, color=GRAY_T),
                        Text("(hypothetical)", font=SERIF, font_size=26, color=GRAY_T, slant=ITALIC)
                        ).arrange(DOWN, buff=0.12).move_to(RING_C)
        for t in whatif:
            t.ss_block = "whatif"
        guess2 = self.guess_rect(2.0 * UNIT)
        ring_toks = self.tokens_for(RING_EDGES, RP, {n: 2 for n in NAMES})
        with self.narrate(NARR["ring"]) as beat:
            beat.wait_until("rewired", offset=-0.15)
            anims = [FadeOut(edges[k]) for k in drop]
            anims += [circ[n].animate.move_to(RP[n]) for n in NAMES]
            anims += [count_swap(num[n], ring_nums[n], P[n], RP[n]) for n in NAMES]
            anims += [name[n].animate.move_to(ring_names[n].get_center()) for n in NAMES]
            anims += [Transform(edges[frozenset(e)], ring_edges[frozenset(e)]) for e in keep]
            anims += [self.Lg.animate.set_value(2.0 * UNIT), self.gv.animate.set_value(2.0),
                      guess.animate.stretch_to_fit_width(guess2.width, about_edge=LEFT),
                      qmark.animate.next_to(guess2, RIGHT, buff=0.15),
                      feld.animate.set_opacity(0.25)]
            self.play(*anims, run_time=2.0)
            self.remove(*[num[n] for n in NAMES])
            self.play(*[Create(ring_edges[frozenset(e)]) for e in new], FadeIn(whatif),
                      run_time=0.9)
            for n in NAMES:
                num[n] = ring_nums[n]
            beat.wait_until("token", offset=-0.25)
            self.add(*[t[2] for t in ring_toks])
            self.play(FadeIn(VGroup(self.c_lab, self.c_eq1, self.c_frac.bar)), run_time=0.5)
            self.add(self.c_num, self.c_den)
            self.play(self.fly_tokens(ring_toks, 2.5, self.n_tr, self.s_tr, {n: 2 for n in NAMES},
                                      lag=0.04))

        with self.narrate(NARR["ring2"], gap=BREAK) as beat:
            pile = VGroup(*[t[2] for t in ring_toks])
            beat.wait_until("reads", offset=-0.1)
            self.play(LaggedStart(*[pulse(t[2], 1.35) for t in ring_toks], lag_ratio=0.05),
                      run_time=1.5)
            beat.wait_until("Both averages", offset=-0.1)
            self.play(FadeOut(guess_lab), FadeOut(qmark), run_time=0.4)
            self.add(self.fblue, self.fpurp, self.fout, self.fnum)
            self.c_res.set_value(2.0)
            self.play(self.Lf.animate.set_value(2.0 * UNIT), self.fv.animate.set_value(2.0),
                      FadeIn(VGroup(self.c_eq2, self.c_res)), run_time=1.0)
            beat.wait_until("guess holds", offset=-0.2)
            self.play(self.Lb.animate.set_value(2.0 * UNIT), flag(self.gnum, color=BLUE),
                      run_time=0.9)

        # ============================================================ 4. fail
        real_toks = self.tokens_for(EDGES, P, K)
        real_nums = {n: MathTex(str(K[n]), font_size=38, color=INK) for n in NAMES}
        guess3 = self.guess_rect(2.5 * UNIT)
        with self.narrate(NARR["recount"]) as beat:
            qmark.next_to(guess3, RIGHT, buff=0.15)
            # round 3: the ring's friend bar and readout fade out (they no longer count down
            # through 1.9 while the girl bar still reads 2.0)
            anims = [FadeOut(pile), FadeOut(whatif), FadeIn(qmark),
                     FadeOut(self.fnum, rate_func=window(0, 0.35, 1.7)),
                     self.Fo.animate(rate_func=window(0, 0.4, 1.7)).set_value(0.0),
                     FadeIn(guess_lab), feld.animate.set_opacity(1.0)]
            anims += [FadeOut(ring_edges[frozenset(e)]) for e in new]
            anims += [circ[n].animate.move_to(P[n]) for n in NAMES]
            anims += [count_swap(num[n], real_nums[n], RP[n], P[n]) for n in NAMES]
            anims += [name[n].animate.move_to(name_label(n).get_center()) for n in NAMES]
            anims += [Transform(edges[frozenset(e)], edge_line(*e, P)) for e in keep]
            anims += [self.Lg.animate.set_value(2.5 * UNIT), self.gv.animate.set_value(2.5),
                      guess.animate.stretch_to_fit_width(guess3.width, about_edge=LEFT),
                      FadeOut(VGroup(self.c_eq2, self.c_res), rate_func=window(0, 0.4, 1.7)),
                      self.c_op.animate(rate_func=window(0, 0.4, 1.7)).set_value(0.0)]
            self.play(*anims, run_time=1.7)
            for tr in (self.Lf, self.Lb, self.fv):
                tr.set_value(0.0)
            self.Fo.set_value(1.0)
            self.n_tr.set_value(0)
            self.s_tr.set_value(0)
            self.c_op.set_value(1.0)
            self.remove(*[num[n] for n in NAMES])
            self.play(*[FadeIn(edges[k]) for k in drop], run_time=0.6)
            for n in NAMES:
                num[n] = real_nums[n]
            beat.wait_until("send", offset=-0.15)
            self.add(*[t[2] for t in real_toks])
            self.play(self.fly_tokens(real_toks, beat.until("Twenty", offset=-0.2, min_time=3.5),
                                      self.n_tr, self.s_tr, K))
            self.play(Indicate(self.c_den, color=YELLOW, scale_factor=1.25), run_time=0.8)
            beat.wait_until("sixty", offset=-0.1)
            self.play(Indicate(self.c_num, color=YELLOW, scale_factor=1.25),
                      FadeOut(guess_lab), FadeOut(qmark), run_time=0.8)
            beat.wait_until("average three", offset=-0.2)
            self.c_res.set_value(3.0)
            self.add(self.fnum)
            self.play(self.Lf.animate.set_value(3.0 * UNIT), self.fv.animate.set_value(3.0),
                      FadeIn(VGroup(self.c_eq2, self.c_res)), run_time=1.4)
        tokens = VGroup(*[t[2] for t in real_toks])

        gap_lab = MathTex(r"+0.5", font_size=36, color=PURPLE)
        gap_pct = MathTex(r"\cdot\ 20\%", font_size=36, color=PURPLE)
        gap_lab.next_to([X0 + 2.75 * UNIT, Y_FRIEND + BAR_H / 2, 0], UP, buff=0.17)
        gap_pct.next_to(gap_lab, RIGHT, buff=0.12)
        gap_grp = VGroup(gap_lab, gap_pct)
        toks_of = {n: [t[2] for t in real_toks if t[1] == n] for n in NAMES}
        with self.narrate(NARR["fail"], gap=BREAK) as beat:
            # the guess is the girl average: it fills the friend bar only up to 2.5
            self.play(self.Lb.animate.set_value(2.5 * UNIT), flag(self.gnum, color=BLUE),
                      run_time=beat.until("half a friend", offset=-0.25, min_time=0.5))
            self.play(self.Po.animate.set_value(1.0), FadeIn(gap_lab, shift=0.1 * UP), run_time=0.9)
            beat.wait_until("twenty percent", offset=-0.1)
            self.play(FadeIn(gap_pct, shift=0.1 * UP), run_time=0.6)
            for who in ("Sue", "Alice", "Betty"):
                beat.wait_until(f"on {who}", offset=-0.05)
                self.play(*[pulse(d, 1.3) for d in toks_of[who]],
                          Indicate(circ[who], color=BLUE, scale_factor=1.08), run_time=0.8)

        # ============================================================ 5. insight
        beam = Line([BX(0.62), BEAM_Y, 0], [BX(4.38), BEAM_Y, 0], color=GRAY, stroke_width=3)
        fulc_b = Triangle(color=BLUE, fill_color=BLUE, fill_opacity=1, stroke_width=0).scale(0.24)
        fulc_b.move_to([BX(2.5), BEAM_Y - 0.06 - fulc_b.height / 2, 0])
        fulc_y = Triangle(color=YELLOW, fill_color=YELLOW, fill_opacity=1, stroke_width=0).scale(0.24)
        fulc_y.move_to([BX(3.0), BEAM_Y - 0.06 - fulc_y.height / 2, 0])
        fb_lab = MathTex("2.5", font_size=40, color=BLUE).next_to(fulc_b, LEFT, buff=0.15)
        fy_lab = MathTex("3", font_size=40, color=YELLOW).next_to(fulc_y, RIGHT, buff=0.15)
        for lab in (fb_lab, fy_lab):             # 0.16 below the beam, clear of the distance line
            lab.set_y(BEAM_Y - 0.16 - lab.height / 2)
        # round 3: every girl keeps her name; it rides onto the beam under her node
        bname = {}
        for n in NAMES:
            t = Text(n, font=SERIF, font_size=BNAME_FONT, color=GRAY_T)
            t.move_to([SP[n][0], BNAME_TOP, 0], aligned_edge=UP)
            bname[n] = t
        with self.narrate(NARR["line"]) as beat:
            beat.wait_until("Line", offset=-0.1)
            anims = [FadeOut(e) for e in edges.values()]
            anims += [d.animate.move_to(P[t[1]]).set_opacity(0) for t, d in zip(real_toks, tokens)]
            anims += [FadeOut(guess)]
            self.play(*anims, run_time=1.0)
            self.remove(*tokens)
            # each name rides with its node; it dims in flight (the sort crosses nodes)
            def ride(m, ref):
                start = m.copy()                 # same glyphs, so point arrays line up exactly
                target = m.copy().scale(BNAME_FONT / 26).move_to(ref.get_top(), aligned_edge=UP)
                fam = list(zip(m.family_members_with_points(), start.family_members_with_points(),
                               target.family_members_with_points()))

                def upd(mob, a):
                    b_ = smooth(a)
                    for sm, s0, s1 in fam:      # (Mobject.interpolate skips the glyphs)
                        sm.points = s0.points + (s1.points - s0.points) * b_
                    mob.set_opacity(1.0 - 0.7 * np.sin(np.pi * a))
                return UpdateFromAlphaFunc(m, upd)
            self.play(*[circ[n].animate.move_to(SP[n]).scale(0.88) for n in NAMES],
                      *[num[n].animate.move_to(SP[n]) for n in NAMES],
                      *[ride(name[n], bname[n]) for n in NAMES],
                      run_time=beat.until("balance", offset=-0.5, min_time=1.4))
            # the beam draws once every name has settled (names cross its line in transit)
            self.play(Create(beam, rate_func=window(0, 0.55, 1.3)),
                      GrowFromPoint(fulc_b, fulc_b.get_bottom(), rate_func=window(0.4, 1.0, 1.3)),
                      FadeIn(fb_lab, shift=0.1 * RIGHT, rate_func=window(0.5, 1.1, 1.3)),
                      flag(self.gnum, color=BLUE), run_time=1.3)

        # numbered token squares stacked on their girl
        stacks = {}
        for n in NAMES:
            sq = VGroup()
            for j in range(K[n]):
                s = Square(TOK_SIDE, stroke_width=0, fill_color=YELLOW, fill_opacity=0.95)
                lab = MathTex(str(K[n]), font_size=32, color=BG)
                lab.ss_host = s
                t = VGroup(s, lab)
                t.move_to(SP[n] + UP * (R + 0.1 + TOK_SIDE / 2 + j * (TOK_SIDE + TOK_GAP)))
                sq.add(t)
            stacks[n] = sq
        all_stack = VGroup(*stacks.values())
        with self.narrate(NARR["stack"]) as beat:
            beat.wait_until("tokens stack", offset=-0.2)
            seq = []
            for kk in (1, 2, 3, 4):
                for n in COLS[kk]:
                    seq.append(AnimationGroup(*[FadeIn(t, target_position=SP[n], scale=0.4)
                                                for t in stacks[n]], lag_ratio=0.15))
            self.play(LaggedStart(*seq, lag_ratio=0.3),
                      run_time=beat.until("balance at three", offset=-0.2, min_time=2.0))
            self.play(GrowFromPoint(fulc_y, fulc_y.get_bottom()), FadeIn(fy_lab, shift=0.1 * LEFT),
                      flag(self.fnum, color=YELLOW), run_time=1.1)

        # Sue's stack -> sum of k squared over sum of k
        sue_box = SurroundingRectangle(stacks["Sue"], color=INK, buff=0.07, corner_radius=0.05,
                                       stroke_width=3)
        sue_box.ss_bg = True
        sue_eq = MathTex(r"4 \times 4 = 16", font_size=38, color=YELLOW)
        sue_eq.next_to(stacks["Sue"], UP, buff=0.22)
        num_k2 = MathTex(r"\sum k^2", font_size=46, color=YELLOW)
        den_k = MathTex(r"\sum k", font_size=46, color=YELLOW)
        with self.narrate(NARR["sue"]) as beat:
            beat.wait_until("Sue", offset=-0.1)
            self.play(Create(sue_box), flag(name["Sue"], color=INK), run_time=0.7)
            beat.wait_until("sixteen", offset=-0.5)
            self.play(Write(sue_eq), run_time=0.8)
            beat.wait_until("k squared", offset=-0.35)
            w = max(num_k2.width, den_k.width) + 0.18
            new_bar = Line(LEFT * w / 2, RIGHT * w / 2, stroke_width=3, color=INK)
            new_bar.move_to([self.c_eq1.get_left()[0] - 0.22 - w / 2, self.c_lab.bar.get_y(), 0])
            num_k2.next_to(new_bar, UP, buff=0.1)
            den_k.next_to(new_bar, DOWN, buff=0.1)
            self.play(*swap(self.c_lab.num, num_k2, 1.0),
                      Transform(self.c_lab.bar, new_bar), flag(sue_eq, color=YELLOW), run_time=1.0)
            beat.wait_until("k on the bottom", offset=-0.2)
            self.play(*swap(self.c_lab.den, den_k, 0.8, t_in=(0.35, 0.8)), run_time=0.8)
            beat.wait_until("Sixty", offset=-0.1)
            self.play(Indicate(self.c_num, color=YELLOW, scale_factor=1.2),
                      Indicate(self.c_den, color=YELLOW, scale_factor=1.2), run_time=0.9)

        # ---- divide by the eight girls: sum k^2 / sum k = 60/20 -> avg(k^2)/mu = 7.5/2.5
        self.c_num.clear_updaters()
        self.c_den.clear_updaters()
        c_bar = self.c_lab.bar
        AVG = r"\text{avg}(k^2)"

        def D8(main, color):
            m = MathTex(main, r"\div 8", font_size=46)
            m[0].set_color(color)
            m[1].set_color(GRAY_T)
            return m
        B1 = row(frac(D8(r"\sum k^2", YELLOW), D8(r"\sum k", YELLOW)), M("="),
                 frac(D8("60", YELLOW), D8("20", YELLOW)), M("="), M("3.0", YELLOW), buff=0.2)
        place(B1, ROW_M0)
        B2 = row(frac(M(AVG, YELLOW), D8(r"\sum k", YELLOW)), M("="),
                 frac(M("7.5", YELLOW), D8("20", YELLOW)), M("="), M("3.0", YELLOW), buff=0.2)
        place(B2, ROW_M0)
        B = row(frac(M(AVG, YELLOW), M(r"\mu", BLUE)), M("="),
                frac(M("7.5", YELLOW), M("2.5", BLUE)), M("="), M("3.0", YELLOW), buff=0.2)
        place(B, ROW_M0)

        swaps_after = []

        def slide(x, y):
            """Same glyphs: move x onto y (matching its size), swap y in after the play."""
            swaps_after.append((x, y))
            r = y.height / max(x.height, 1e-6)
            return x.animate.scale(r).move_to(y.get_center())

        def do_swaps():
            for x, y in swaps_after:
                self.remove(x)
                self.add(y)
            swaps_after.clear()

        def morph_row(src, dst, total, change=()):
            """Move every part of one row onto the next.  Parts named in `change` hold new
            content: they leave upward and the new term rises in (no crossfade); the rest
            keep their glyphs and slide."""
            anims = []
            for i, (a, b) in enumerate(zip(src, dst)):
                pairs = ([(a.num, b.num, "num"), (a.bar, b.bar, "bar"), (a.den, b.den, "den")]
                         if hasattr(a, "bar") else [(a, b, "")])
                for x, y, tag in pairs:
                    if (i, tag) in change:
                        anims += swap(x, y, total)
                    elif tag == "bar":
                        anims.append(ReplacementTransform(x, y))
                    else:
                        anims.append(slide(x, y))
            return anims
        with self.narrate(NARR["divide"]) as beat:
            beat.wait_until("Divide", offset=-0.1)
            self.play(slide(num_k2, B1[0].num[0]), FadeIn(B1[0].num[1], shift=0.1 * LEFT),
                      slide(den_k, B1[0].den[0]), FadeIn(B1[0].den[1], shift=0.1 * LEFT),
                      ReplacementTransform(c_bar, B1[0].bar), slide(self.c_eq1, B1[1]),
                      slide(self.c_num, B1[2].num[0]), FadeIn(B1[2].num[1], shift=0.1 * LEFT),
                      slide(self.c_den, B1[2].den[0]), FadeIn(B1[2].den[1], shift=0.1 * LEFT),
                      ReplacementTransform(self.c_frac.bar, B1[2].bar), slide(self.c_eq2, B1[3]),
                      slide(self.c_res, B1[4]), run_time=1.1)
            do_swaps()
            beat.wait_until("average of k", offset=-0.2)
            self.play(*morph_row(B1, B2, 0.9, change={(0, "num"), (2, "num")}), run_time=0.9)
            do_swaps()
            beat.wait_until("average girl", offset=-0.2)
            self.play(*morph_row(B2, B, 0.9, change={(0, "den"), (2, "den")}),
                      flag(fb_lab, color=BLUE), run_time=0.9)
            do_swaps()
            beat.wait_until("two and a half", offset=-0.1)
            self.play(flag(B[0].den, color=BLUE), flag(B[2].den, color=BLUE), run_time=0.8)

        # ---- variance: squared distances from the balance point, drawn under the beam
        xf = BX(2.5)
        dev_l = Line([xf, DEV_Y, 0], [BX(1), DEV_Y, 0], color=PURPLE, stroke_width=4)
        dev_r = Line([xf, DEV_Y, 0], [BX(4), DEV_Y, 0], color=PURPLE, stroke_width=4)
        dev_mark = Line([xf, DEV_Y - 0.08, 0], [xf, DEV_Y + 0.08, 0], color=BLUE, stroke_width=4)
        dev_mark.ss_bg = True
        dev_ticks = {k: Line([BX(k), DEV_Y - 0.08, 0], [BX(k), DEV_Y + 0.08, 0], color=PURPLE,
                             stroke_width=4) for k in COLS}
        for t in dev_ticks.values():
            t.ss_bg = True                       # tick labels sit under their ticks
        dev_labs = {k: MathTex(f"{abs(k - 2.5):g}", font_size=30, color=PURPLE).next_to(
            [BX(k), DEV_Y, 0], DOWN, buff=0.17) for k in COLS}
        signed = {k: MathTex(f"{k - 2.5:+g}".replace("-", "-"), font_size=30, color=PURPLE).move_to(
            dev_labs[k]) for k in COLS}
        squares, areas, edges_sq, segs = {}, {}, {}, {}
        for k, girls in COLS.items():
            side = SQ_SCALE * abs(k - 2.5)
            segs[k] = Line([xf, DEV_Y, 0], [BX(k), DEV_Y, 0], color=PURPLE, stroke_width=4)
            for n in girls:
                s = Square(side, stroke_color=PURPLE, stroke_width=2.5, fill_color=PURPLE,
                           fill_opacity=0.45)
                s.move_to([SP[n][0], SQ_TOP - side / 2, 0])
                squares[n] = s
                edges_sq[n] = Line([SP[n][0] - side / 2, SQ_TOP, 0], [SP[n][0] + side / 2, SQ_TOP, 0],
                                   color=PURPLE, stroke_width=4)
                areas[n] = MathTex(f"{(k - 2.5) ** 2:.2f}", font_size=28, color=PURPLE).move_to(
                    [SP[n][0], AREA_Y, 0])
        ends = [n for n in NAMES if K[n] in (1, 4)]
        mids = [n for n in NAMES if K[n] in (2, 3)]
        # round 3: the tag says what is scaled (the side), in full-size type
        quarter = Text("square side = distance, drawn at 1/4 scale", font=SERIF, font_size=20,
                       color=GRAY_T)
        quarter.move_to([0.25 + quarter.width / 2, -1.2, 0])        # beside the squares
        # the variance row (flat): sigma^2 = 10/8 = 1.25
        Vrow = MathTex(r"\sigma^2", "=", "10", "/", "8", "=", "1.25", font_size=44)
        for i in (0, 2, 6):
            Vrow[i].set_color(PURPLE)
        Vrow.move_to([RX, ROW_V, 0])
        ten = Vrow[2]
        dims = VGroup(all_stack, sue_box, sue_eq)
        self.gnum.clear_updaters()
        self.fnum.clear_updaters()
        panel_txt = VGroup(self.glabel, self.flabel, self.gnum, self.fnum, self.axis, gap_grp)
        with self.narrate(NARR["variance"]) as beat:
            main = VGroup(*B)
            self.play(dims.animate.set_opacity(0.3), main.animate.shift(UP * (ROW_M - ROW_M0)),
                      self.Dm.animate.set_value(0.25), panel_txt.animate.set_opacity(0.25),
                      run_time=0.8)
            beat.wait_until("distance", offset=-0.1)
            self.play(Create(dev_l), Create(dev_r), FadeIn(dev_mark),
                      LaggedStart(*[FadeIn(VGroup(dev_ticks[k], dev_labs[k])) for k in (2, 3, 1, 4)],
                                  lag_ratio=0.3), run_time=1.2)
            # each girl's distance drops to her square's top edge, visibly shrinking to the
            # square's 1/4 scale, then the square grows down from it
            beat.wait_until("square it", offset=-0.25)
            T = 1.25
            drops = [TransformFromCopy(segs[K[n]], edges_sq[n], rate_func=window(0, 0.7, T)) for n in NAMES]
            grows = [GrowFromEdge(squares[n], UP, rate_func=window(0.65, 1.2, T)) for n in NAMES]
            self.play(*drops, *grows, FadeIn(quarter, rate_func=window(0.6, 1.2, T)), run_time=T)
            self.remove(*edges_sq.values())
            beat.wait_until("two and a quarter", offset=-0.15)
            self.play(LaggedStart(*[FadeIn(areas[n], shift=0.1 * DOWN) for n in ends], lag_ratio=0.15),
                      run_time=0.8)
            beat.wait_until("a quarter in", offset=-0.1)
            self.play(LaggedStart(*[FadeIn(areas[n], shift=0.1 * DOWN) for n in mids], lag_ratio=0.15),
                      run_time=0.8)
            beat.wait_until("They average", offset=-0.35)
            # round 3: the labels themselves fly into "10" (no copies over the originals, so no
            # doubled glyphs); the scale tag steps out of their lane first
            fl = [along(areas[n], [areas[n].get_center(), [areas[n].get_x(), LANE_Y, 0],
                                   [-0.25, LANE_Y, 0], [0.9, ten.get_y() - 0.55, 0],
                                   ten.get_center()], fade_tail=0.25)
                  for n in NAMES]
            T = beat.until("variance", offset=-0.2, min_time=1.8)
            t125 = max(0.6, beat.time_of("one and a quarter") - 0.15 - beat.elapsed())
            self.play(FadeOut(quarter, rate_func=window(0, 0.3, T)),
                      LaggedStart(*fl, lag_ratio=0.04, rate_func=window(0.2, 1.5, T)),
                      FadeIn(VGroup(Vrow[2], Vrow[3], Vrow[4]), rate_func=window(1.05, 1.6, T)),
                      FadeIn(VGroup(Vrow[5], Vrow[6]), rate_func=window(max(t125, 1.4), max(t125, 1.4) + 0.5, T)),
                      run_time=T)
            self.remove(*areas.values())
            beat.wait_until("variance", offset=-0.1)
            self.play(FadeIn(VGroup(Vrow[0], Vrow[1]), shift=0.1 * RIGHT), run_time=0.6)
            self.play(flag(Vrow[0], color=PURPLE), *[flag(s, color=PURPLE) for s in squares.values()],
                      run_time=0.8)
            # round 3: the token stacks have done their job and leave; so does the old main
            # row (it returns at "So"); the beam picture lifts into the freed band
            lift_on = VGroup(*circ.values(), *num.values(), *name.values(), beam, fulc_b, fulc_y,
                             fb_lab, fy_lab, dev_l, dev_r, dev_mark, *dev_ticks.values(),
                             *dev_labs.values(), *squares.values())
            T = 0.8
            self.play(FadeOut(dims, rate_func=window(0, 0.55, T)),
                      FadeOut(VGroup(*B), rate_func=window(0, 0.5, T)),
                      lift_on.animate.shift(UP * LIFT), run_time=T)
            for m in signed.values():
                m.shift(UP * LIFT)

        # ---- why avg(k^2) = mu^2 + sigma^2: split Sue's 4 = 2.5 + 1.5, square, average
        def srow(*parts, colors=None):
            m = MathTex(*parts, font_size=S_FONT)
            for i, c in (colors or {}).items():
                m[i].set_color(c)
            m.move_to([SX, ROW_S, 0], aligned_edge=LEFT)
            return m
        S1 = srow("4", "^2", "=", "(", "2.5", "+", "1.5", ")", "^2",
                  colors={4: BLUE, 6: PURPLE})
        S2 = srow("4", "^2", "=", "2.5", "^2", "+", "1.5", "^2", r"+\;", "2", r"\cdot", "2.5",
                  r"\cdot", "1.5", colors={3: BLUE, 4: BLUE, 6: PURPLE, 7: PURPLE, 11: BLUE, 13: PURPLE})
        S3 = srow(AVG, "=", r"\mu^2", "+", r"\sigma^2", r"+\;", "2", r"\mu", r"\cdot",
                  r"\text{avg}(d)", colors={0: YELLOW, 2: BLUE, 4: PURPLE, 7: BLUE, 9: PURPLE})
        S3z = srow(AVG, "=", r"\mu^2", "+", r"\sigma^2", r"+\;", "2", r"\mu", r"\cdot",
                   "0", colors={0: YELLOW, 2: BLUE, 4: PURPLE, 7: BLUE, 9: PURPLE})
        S4 = srow(AVG, "=", r"\mu^2", "+", r"\sigma^2", colors={0: YELLOW, 2: BLUE, 4: PURPLE})
        box_c = SurroundingRectangle(VGroup(*S2[9:14]), color=INK, buff=0.06, corner_radius=0.06,
                                     stroke_width=3)
        box_c3 = SurroundingRectangle(VGroup(*S3[6:10]), color=INK, buff=0.06, corner_radius=0.06,
                                      stroke_width=3)
        # round 3: when avg(d) becomes 0 the box shrinks with it
        box_c3z = SurroundingRectangle(VGroup(S3[6], S3[7], S3[8], S3z[9]), color=INK, buff=0.06,
                                       corner_radius=0.06, stroke_width=3)
        box_c.ss_bg = box_c3.ss_bg = box_c3z.ss_bg = True
        # round 3: d is named where it is measured, between the beam and the distance line
        d_lab = MathTex("d", "=", "k", "-", r"\mu", font_size=36)
        d_lab[0].set_color(PURPLE)
        d_lab[4].set_color(BLUE)
        # (right-aligned past the beam's end, well clear of the YELLOW fulcrum's "3")
        d_lab.move_to([0.3 - d_lab.width / 2, (BEAM_Y + DEV_Y) / 2 + LIFT, 0])
        zero = MathTex("0", font_size=32, color=PURPLE).move_to([xf, dev_labs[2].get_y(), 0])

        def whole(f, *extra):
            """After a transition the parts of a formula sit in the scene one by one; put the
            formula back as one object."""
            self.remove(*f.submobjects, *extra)
            self.add(f)
        with self.narrate(NARR["split"]) as beat:
            beat.wait_until("four", offset=-0.15)
            self.play(flag(num["Sue"], color=INK), flag(name["Sue"], color=INK),
                      tfc(num["Sue"], S1[0]), FadeIn(S1[1]), FadeIn(S1[2]), run_time=0.6)
            beat.wait_until("the balance point", offset=-0.1)
            self.play(flag(fb_lab, color=BLUE), flag(dev_mark, color=BLUE),
                      FadeIn(VGroup(S1[3], S1[4]), shift=0.1 * UP), run_time=0.8)
            beat.wait_until("her distance", offset=-0.1)
            self.play(flag(dev_r, color=PURPLE), Write(d_lab, rate_func=window(0, 0.8, 1.0)),
                      TransformFromCopy(dev_labs[4], S1[6]),
                      FadeIn(S1[5]), FadeIn(VGroup(S1[7], S1[8])), run_time=1.0)
            whole(S1)
            # (2.5 + 1.5)^2 -> 2.5^2 + 1.5^2 + 2*2.5*1.5: shared glyphs slide, the copies
            # for the cross term peel off, the brackets leave before new symbols arrive
            beat.wait_until("Squaring", offset=-0.15)
            T = 0.9
            self.play(ReplacementTransform(S1[0], S2[0]), ReplacementTransform(S1[1], S2[1]),
                      ReplacementTransform(S1[2], S2[2]),
                      FadeOut(VGroup(S1[3], S1[7], S1[8]), rate_func=window(0, 0.3, T)),
                      ReplacementTransform(S1[4], S2[3], rate_func=window(0.15, 0.75, T)),
                      ReplacementTransform(S1[5], S2[5], rate_func=window(0.15, 0.75, T)),
                      ReplacementTransform(S1[6], S2[6], rate_func=window(0.15, 0.75, T)),
                      FadeIn(VGroup(S2[4], S2[7]), rate_func=window(0.55, 0.9, T)),
                      run_time=T)
            # the cross term rises in place while its two factors flash in their colours
            self.play(flag(S2[3], color=BLUE), flag(S2[6], color=PURPLE),
                      FadeIn(VGroup(*S2[8:14]), shift=0.12 * UP), run_time=0.9)
            whole(S2)
            beat.wait_until("cross term", offset=-0.1)
            self.play(Create(box_c), run_time=0.6)
            # every girl: average the three pieces
            beat.wait_until("Every girl", offset=-0.1)
            T = 1.3
            self.play(LaggedStart(*[Indicate(circ[n], color=BLUE, scale_factor=1.1) for n in NAMES],
                                  lag_ratio=0.05, run_time=T),
                      flag(d_lab, color=PURPLE),
                      *swap(S2[0:2], S3[0], T, t_in=(0.45, 1.0)),
                      ReplacementTransform(S2[2], S3[1], rate_func=window(0.2, 1.0, T)),
                      *swap(S2[3:5], S3[2], T, t_in=(0.45, 1.0)),
                      ReplacementTransform(S2[5], S3[3], rate_func=window(0.2, 1.0, T)),
                      *swap(S2[6:8], S3[4], T, t_in=(0.45, 1.0)),
                      ReplacementTransform(S2[8], S3[5], rate_func=window(0.2, 1.0, T)),
                      ReplacementTransform(S2[9], S3[6], rate_func=window(0.2, 1.0, T)),
                      *swap(VGroup(S2[10], S2[11]), S3[7], T, t_in=(0.45, 1.0)),
                      ReplacementTransform(S2[12], S3[8], rate_func=window(0.2, 1.0, T)),
                      *swap(S2[13], S3[9], T, t_in=(0.45, 1.0)),
                      ReplacementTransform(box_c, box_c3, rate_func=window(0.2, 1.0, T)),
                      run_time=T)
            whole(S3)
            self.play(flag(S3[4], color=PURPLE), *[flag(squares[n], color=PURPLE) for n in NAMES],
                      run_time=0.8)
            # the beam balances: the signed distances add to zero
            beat.wait_until("left and right", offset=-0.2)
            T = 0.9
            sw = []
            for k in COLS:
                sw += swap(dev_labs[k], signed[k], T)
            self.play(*sw, run_time=T)
            beat.wait_until("distances", offset=0.0)
            # round 3: the four signed distances merge into the 0 under the balance point ...
            self.play(TransformFromCopy(VGroup(*[signed[k] for k in COLS]), zero), run_time=0.8)
            # ... and that 0 travels (under the split row, clear of sigma^2) to replace avg(d);
            # the box shrinks around what is left
            T = 1.1
            z = zero.copy()
            z_to = S3z[9].get_center()
            zpath = VMobject().set_points_smoothly([np.array(q, dtype=float) for q in (
                zero.get_center(), [xf, -0.55, 0], [0.6, -1.75, 0], [z_to[0] - 0.4, -1.75, 0], z_to)])
            h0, h1 = zero.height, S3z[9].height

            def zmove(m, al):
                bb = smooth(float(np.clip((al * T - 0.1) / (T - 0.1), 0, 1)))
                m.scale_to_fit_height(h0 + (h1 - h0) * bb)
                m.move_to(zpath.point_from_proportion(bb))
            self.play(FadeOut(S3[9], shift=0.12 * UP, rate_func=window(0, 0.35, T)),
                      UpdateFromAlphaFunc(z, zmove),
                      Transform(box_c3, box_c3z, rate_func=window(0.7, 1.1, T)), run_time=T)
            self.remove(z)
            self.add(S3z[9])
            beat.wait_until("cancel", offset=0.2)
            self.play(FadeOut(VGroup(S3[5], S3[6], S3[7], S3[8], S3z[9], box_c3), shift=0.12 * UP),
                      run_time=0.6)
            self.remove(S3, *S3.submobjects)
            whole(S4)

        # ---- the main row: numerators rebuilt from the identity and the variance
        cnum = MathTex(r"\mu^2", "+", r"\sigma^2", font_size=46)
        cnum[0].set_color(BLUE)
        cnum[2].set_color(PURPLE)
        nnum = MathTex("2.5", "^2", "+", "1.25", font_size=46)
        nnum[0].set_color(BLUE)
        nnum[1].set_color(BLUE)
        nnum[3].set_color(PURPLE)
        C = row(frac(cnum, M(r"\mu", BLUE)), M("="), frac(nnum, M("2.5", BLUE)), M("="),
                M("3.0", YELLOW), buff=0.24)
        place(C, ROW_M)

        def stage(*parts, buff=0.17):
            return place(row(*parts, buff=buff), ROW_M)

        def mu2(c1, c2=BLUE):
            m = MathTex(c1, "^2", font_size=46)
            m.set_color(c2)
            return m
        f_s2mu = lambda: frac(M(r"\sigma^2", PURPLE), M(r"\mu", BLUE))
        f_125 = lambda: frac(M("1.25", PURPLE), M("2.5", BLUE))
        D1 = stage(frac(mu2(r"\mu"), M(r"\mu", BLUE)), M("+"), f_s2mu(), M("="),
                   frac(mu2("2.5"), M("2.5", BLUE)), M("+"), f_125(), M("="),
                   M("3.0", YELLOW), buff=0.24)
        D2 = stage(M(r"\mu", BLUE), M("+"), f_s2mu(), M("="),
                   frac(mu2("2.5"), M("2.5", BLUE)), M("+"), f_125(), M("="), M("3.0", YELLOW),
                   buff=0.24)
        D3 = stage(M(r"\mu", BLUE), M("+"), f_s2mu(), M("="), M("2.5", BLUE), M("+"), f_125(),
                   M("="), M("3.0", YELLOW), buff=0.24)
        D4 = stage(M(r"\mu", BLUE), M("+"), f_s2mu(), M("="), M("2.5", BLUE), M("+"),
                   M("0.5", PURPLE), M("="), M("3.0", YELLOW), buff=0.24)
        xmin_r, xmax_r = -0.15, 6.32
        s_fit = min(1.0, (xmax_r - xmin_r) / D1.width)
        for g in (C, D1, D2, D3, D4):
            g.scale(s_fit)
            place(g, ROW_M, x=(xmin_r + xmax_r) / 2)

        # round 3: the ring comes back as a picture (thumbnail of the 0:31 ring) with its
        # spread collapsed to a point, and the bars show it: no spread, no gap
        rpos = {n: RING_C2 + RING_S * (RP[n] - RING_C) for n in NAMES}
        r_th = R * RING_S
        th_edges = VGroup(*[Line(rpos[a] + unit(rpos[b] - rpos[a]) * (r_th + 0.05),
                                 rpos[b] - unit(rpos[b] - rpos[a]) * (r_th + 0.05),
                                 color=GRAY, stroke_width=2) for a, b in RING_EDGES])
        th_nodes = VGroup(*[Circle(radius=r_th, stroke_color=BLUE, stroke_width=2.5, fill_color=BLUE,
                                   fill_opacity=0.16).move_to(rpos[n]) for n in NAMES])
        for c in th_nodes:
            c.ss_bg = True
        th_nums = VGroup(*[MathTex("2", font_size=26, color=INK).move_to(rpos[n]) for n in NAMES])
        for t_, c_ in zip(th_nums, th_nodes):
            t_.ss_host = c_                      # each digit is printed on its own node
        ring_th = VGroup(th_edges, th_nodes, th_nums)
        ring_pt = Dot(RING_C2, radius=0.07, color=PURPLE)
        rr = row(M("2", BLUE, 42), M("+", INK, 42), frac(M("0", PURPLE, 42), M("2", BLUE, 42)),
                 M("=", INK, 42), M("2", YELLOW, 42), buff=0.2)
        rr.move_to([RING_C2[0] + RING_S * RING_R + r_th + 0.45 + rr.width / 2, RING_C2[1], 0])
        rr.shift(UP * (RING_C2[1] - rr[2].bar.get_y()))

        def shift_all(src, dst, skip=(), rf=None):
            kw = {} if rf is None else {"rate_func": rf}
            return [ReplacementTransform(src[i], dst[i], **kw) for i in range(len(src)) if i not in skip]

        def cancel(fr, target, total):
            """mu^2/mu -> mu: the box, the square and the denominator leave, the base slides."""
            box = SurroundingRectangle(fr, color=INK, buff=0.05, corner_radius=0.06, stroke_width=3)
            return box, [FadeOut(VGroup(box, fr.num[1], fr.bar, fr.den), shift=0.12 * UP,
                                 rate_func=window(0, 0.4, total)),
                         ReplacementTransform(fr.num[0], target, rate_func=window(0.25, total, total))]

        with self.narrate(NARR["result"], gap=BREAK) as beat:
            # the friend average avg(k^2)/mu returns where it stood, and the identity's right
            # side replaces its numerator
            self.play(FadeIn(VGroup(*B), shift=0.12 * UP), flag(S4, color=INK), run_time=0.6)
            beat.wait_until("is mu", offset=-0.6)
            T = 1.6
            self.play(FadeOut(VGroup(B[0].num, B[2].num), shift=0.12 * UP, rate_func=window(0, 0.35, T)),
                      ReplacementTransform(B[0].bar, C[0].bar, rate_func=window(0.15, 0.9, T)),
                      ReplacementTransform(B[0].den, C[0].den, rate_func=window(0.15, 0.9, T)),
                      ReplacementTransform(B[1], C[1], rate_func=window(0.15, 0.9, T)),
                      ReplacementTransform(B[2].bar, C[2].bar, rate_func=window(0.15, 0.9, T)),
                      ReplacementTransform(B[2].den, C[2].den, rate_func=window(0.15, 0.9, T)),
                      ReplacementTransform(B[3], C[3], rate_func=window(0.15, 0.9, T)),
                      ReplacementTransform(B[4], C[4], rate_func=window(0.15, 0.9, T)),
                      TransformFromCopy(VGroup(*S4[2:5]), cnum, rate_func=window(0.5, 1.6, T)),
                      TransformFromCopy(B[2].den.copy(), nnum[0], rate_func=window(0.5, 1.6, T)),
                      FadeIn(VGroup(nnum[1], nnum[2]), rate_func=window(0.9, 1.6, T)),
                      TransformFromCopy(Vrow[6], nnum[3], rate_func=window(0.5, 1.6, T)),
                      run_time=T)
            beat.wait_until("friends average", offset=-0.1)
            cL, cR = C[0], C[2]
            self.play(ReplacementTransform(cL.num[0], D1[0].num),
                      ReplacementTransform(cL.num[1], D1[1]),
                      ReplacementTransform(cL.num[2], D1[2].num),
                      ReplacementTransform(cL.bar, D1[0].bar), TransformFromCopy(cL.bar, D1[2].bar),
                      ReplacementTransform(cL.den, D1[0].den), TransformFromCopy(cL.den, D1[2].den),
                      ReplacementTransform(C[1], D1[3]),
                      ReplacementTransform(VGroup(cR.num[0], cR.num[1]), D1[4].num),
                      ReplacementTransform(cR.num[2], D1[5]),
                      ReplacementTransform(cR.num[3], D1[6].num),
                      ReplacementTransform(cR.bar, D1[4].bar), TransformFromCopy(cR.bar, D1[6].bar),
                      ReplacementTransform(cR.den, D1[4].den), TransformFromCopy(cR.den, D1[6].den),
                      ReplacementTransform(C[3], D1[7]), ReplacementTransform(C[4], D1[8]),
                      FadeOut(Vrow, rate_func=window(0, 0.5, 1.1)),
                      run_time=1.1)
            beat.wait_until("plus sigma", occurrence=2, offset=-0.2)
            box1, canc = cancel(D1[0], D2[0], 1.0)
            self.play(Create(box1), run_time=0.45)
            self.play(*canc, *shift_all(D1, D2, skip=(0,)), run_time=1.0)
            beat.wait_until("Here", offset=-0.1)
            box2, canc = cancel(D2[4], D3[4], 0.9)
            self.play(Create(box2), FadeOut(S4, rate_func=window(0, 0.4, 0.45)), run_time=0.45)
            self.play(*canc, *shift_all(D2, D3, skip=(4,)), run_time=0.9)
            beat.wait_until("plus a half", offset=-0.15)
            self.play(*shift_all(D3, D4, skip=(6,)), *swap(D3[6], D4[6], 0.9), run_time=0.9)
            beat.wait_until("extra half", offset=-0.25)
            self.play(self.Dm.animate.set_value(1.0), panel_txt.animate.set_opacity(1.0), run_time=0.5)
            self.play(flag(D4[6], color=PURPLE), flag(self.fpurp, color=PURPLE),
                      flag(gap_lab, color=PURPLE), run_time=0.9)
            # the ring: a thumbnail of the 0:31 class, its distance line collapses to a point
            beat.wait_until("ring", offset=-0.2)
            self.play(FadeIn(ring_th, scale=0.85), run_time=0.6)
            beat.wait_until("no spread", offset=-0.15)
            spread = VGroup(dev_l, dev_r, *dev_ticks.values()).copy()
            self.play(ReplacementTransform(spread, ring_pt), run_time=0.8)
            # ... so the bars meet at 2 (no purple), and mu + sigma^2/mu reads 2 + 0/2
            beat.wait_until("no gap", offset=-0.3)
            for m, f in self._num_upd:
                m.add_updater(f)
            self.play(self.Lg.animate.set_value(2.0 * UNIT), self.Lf.animate.set_value(2.0 * UNIT),
                      self.Lb.animate.set_value(2.0 * UNIT), self.gv.animate.set_value(2.0),
                      self.fv.animate.set_value(2.0), FadeOut(gap_grp, rate_func=window(0, 0.4, 1.0)),
                      TransformFromCopy(VGroup(D4[0], D4[1], D4[2]), VGroup(rr[0], rr[1], rr[2])),
                      FadeIn(VGroup(rr[3], rr[4]), rate_func=window(0.5, 1.0, 1.0)),
                      run_time=1.0)
            self.hold(max(0.0, beat.remaining()))
            # back to the real class (the bars return to 2.5 and 3.0)
            self.play(self.Lg.animate.set_value(2.5 * UNIT), self.Lf.animate.set_value(3.0 * UNIT),
                      self.Lb.animate.set_value(2.5 * UNIT), self.gv.animate.set_value(2.5),
                      self.fv.animate.set_value(3.0), FadeIn(gap_grp, rate_func=window(0.5, 1.0, 0.8)),
                      run_time=0.8)
            for m, f in self._num_upd:
                m.remove_updater(f)

        # ============================================================ 6. Facebook
        # (only what is on screen: the stacks, area labels and scale tag have already left)
        dev_grp = VGroup(dev_l, dev_r, dev_mark, *dev_ticks.values(), *signed.values(), zero,
                         *squares.values(), d_lab)
        beam_grp = VGroup(*circ.values(), *num.values(), *name.values(), beam, fulc_b, fulc_y,
                          fb_lab, fy_lab, dev_grp, ring_th, ring_pt, rr)
        ugander = citation("Ugander et al., 2011 · arXiv:1111.4503 (Facebook, May 2011)", color=GRAY_T)
        G = self.G
        s_ = FB_S
        fbu = FB_UNIT * s_
        # new panel geometry after the move (scale s_ about FB_C0, then centre on FB_C1)
        mp = lambda p: FB_C1 + s_ * (np.array(p, dtype=float) - FB_C0)
        x0n, ygn, yfn, yaxn = mp([X0, 0, 0])[0], mp([0, Y_GIRL, 0])[1], mp([0, Y_FRIEND, 0])[1], mp([0, Y_AX, 0])[1]
        fb_glabel = Text("average user", font=SERIF, font_size=28 * s_, color=INK)
        fb_glabel.move_to([x0n, ygn + 0.55 * s_, 0], aligned_edge=LEFT)
        fb_vals = (0, 200, 400, 600, 800)
        fb_nums = VGroup(*[MathTex(str(v), font_size=30 * s_, color=GRAY_T).next_to(
            [x0n + v * fbu, yaxn, 0], DOWN, buff=0.16 * s_) for v in fb_vals])
        fb_ticks = VGroup(*[Line([x0n + v * fbu, yaxn - 0.07 * s_, 0], [x0n + v * fbu, yaxn + 0.07 * s_, 0],
                                 color=GRAY, stroke_width=2.5) for v in fb_vals])
        for t in fb_ticks:
            t.ss_bg = True
        g_int = DecimalNumber(190, num_decimal_places=0, font_size=40 * s_, color=BLUE)
        f_int = DecimalNumber(0, num_decimal_places=0, font_size=40 * s_, color=YELLOW)
        q2 = MathTex("?", font_size=46 * s_, color=YELLOW).next_to([x0n, yfn, 0], RIGHT, buff=0.2)
        fb_full = row(M(r"\mu", BLUE), M("+"), f_s2mu(), M("="), M("190", BLUE), M("+"),
                      M("445", PURPLE), M("="), M("635", YELLOW), buff=0.2)
        place(fb_full, -1.75, x=0.0)
        panel = VGroup(self.glabel, self.flabel, self.gbar, self.fblue, self.fpurp, self.fout,
                       self.gnum, self.fnum, self.ax_line, self.ax_ticks, self.ax_nums, self.ax_title)
        with self.narrate(NARR["fb"]) as beat:
            for m, _ in self._bar_upd:
                m.clear_updaters()
            T = 1.3
            self.play(FadeOut(VGroup(beam_grp, *[D4[i] for i in range(3, 9)], gap_grp),
                              rate_func=window(0, 0.5, T)),
                      FadeOut(feld, rate_func=window(0, 0.35, T)),
                      FadeIn(ugander, rate_func=window(0.45, 0.9, T)),
                      panel.animate(rate_func=window(0.3, 1.3, T)).scale(s_, about_point=FB_C0).shift(FB_C1 - FB_C0),
                      ReplacementTransform(D4[0], fb_full[0], rate_func=window(0.3, 1.3, T)),
                      ReplacementTransform(D4[1], fb_full[1], rate_func=window(0.3, 1.3, T)),
                      ReplacementTransform(D4[2], fb_full[2], rate_func=window(0.3, 1.3, T)),
                      run_time=T)
            G.update(x0=x0n, yg=ygn, yf=yfn, yax=yaxn, s=s_)
            for tr in (self.Lg, self.Lf, self.Lb):
                tr.set_value(tr.get_value() * s_)
            for m, f in self._bar_upd:
                m.add_updater(f)
            beat.wait_until("users", offset=-0.1)
            g_int.next_to([x0n + 190 * fbu, ygn, 0], RIGHT, buff=0.2 * s_)

            def upd_gi(m):
                m.next_to([G["x0"] + max(self.Lg.get_value(), 0), G["yg"], 0], RIGHT, buff=0.2 * s_)
            T = 1.5
            self.play(*swap(self.glabel, fb_glabel, T, t_out=0.5, t_in=(0.65, 1.2)),
                      *swap(self.ax_nums, fb_nums, T, t_out=0.5, t_in=(0.65, 1.2)),
                      ReplacementTransform(self.ax_ticks, fb_ticks),
                      self.Lg.animate.set_value(190 * fbu),
                      self.Lf.animate.set_value(0.0), self.Lb.animate.set_value(0.0),
                      self.Po.animate.set_value(0.0),
                      FadeOut(self.fnum, rate_func=window(0, 0.4, T)),
                      FadeOut(self.gnum, rate_func=window(0, 0.4, T)),
                      run_time=T)
            g_int.add_updater(upd_gi)
            self.play(FadeIn(g_int), run_time=0.6)
            beat.wait_until("every friendship", offset=-0.1)
            self.play(FadeIn(q2, scale=0.7), flag(self.flabel, color=INK), run_time=0.8)
            beat.wait_until("tokens average", offset=-0.15)
            self.play(Indicate(q2, color=YELLOW, scale_factor=1.3), run_time=0.9)

        fvt = ValueTracker(0)

        def upd_fi(m):
            m.set_value(fvt.get_value())
            m.next_to([G["x0"] + max(self.Lf.get_value(), 0), G["yf"], 0], RIGHT, buff=0.2 * s_)
        f_int.add_updater(upd_fi)
        fb_gap = MathTex(r"+445", font_size=36 * s_, color=PURPLE)
        fb_gap.next_to([x0n + 635 * fbu, yfn + BAR_H * s_ / 2, 0], UP, buff=0.2)
        fb_gap.align_to([x0n + 635 * fbu, 0, 0], RIGHT)
        # round 3: "a few users had thousands of friends" gets a picture: users (BLUE dots)
        # slide out past 800, through a break in the axis, toward Facebook's 5,000 limit
        x800 = x0n + 800 * fbu
        x_cap = 5.55
        brk = VGroup(*[Line([x800 + dx - 0.05, yaxn - 0.13, 0], [x800 + dx + 0.05, yaxn + 0.13, 0],
                            color=GRAY, stroke_width=2.5) for dx in (0.56, 0.7)])
        ext = DashedLine([x800 + 0.86, yaxn, 0], [x_cap, yaxn, 0], color=GRAY, stroke_width=2.5,
                         dash_length=0.1)
        cap_tick = Line([x_cap, yaxn - 0.07 * s_, 0], [x_cap, yaxn + 0.07 * s_, 0], color=GRAY,
                        stroke_width=2.5)
        cap_tick.ss_bg = True
        cap_num = MathTex(r"5{,}000", font_size=30 * s_, color=GRAY_T).next_to(
            [x_cap, yaxn, 0], DOWN, buff=0.16 * s_)
        cap_lab = Text("Facebook's limit", font=SERIF, font_size=20, color=GRAY_T)
        cap_lab.next_to(cap_num, DOWN, buff=0.14)
        cap_lab.align_to(cap_num, RIGHT)
        few_x1 = [x800 + 1.1, x800 + 1.65, x800 + 2.15, x_cap - 0.24]
        few = VGroup(*[Dot([x0n + v * fbu, yaxn, 0], radius=0.07, color=BLUE)
                       for v in (520, 610, 690, 760)])
        few_lab = Text("a few users", font=SERIF, font_size=20, color=BLUE)
        few_lab.move_to([(few_x1[0] + few_x1[-1]) / 2, yaxn + 0.36, 0])
        fb_tail = VGroup(brk, ext, cap_tick, cap_num, cap_lab, few, few_lab)
        with self.narrate(NARR["fb2"], gap=BREAK) as beat:
            self.add(f_int)
            T = beat.until("A few", offset=-0.8, min_time=1.3)
            self.play(self.Lf.animate.set_value(635 * fbu), fvt.animate.set_value(635),
                      FadeOut(q2, rate_func=window(0, 0.3, T)), run_time=T)
            # the friend bar fills: BLUE up to the mean, PURPLE beyond it
            self.play(self.Lb.animate.set_value(190 * fbu), self.Po.animate.set_value(1.0),
                      FadeIn(fb_gap, shift=0.1 * UP), flag(g_int, color=BLUE), run_time=0.8)
            beat.wait_until("A few", offset=-0.1)
            self.play(Create(brk), Create(ext), Create(cap_tick), FadeIn(cap_num), FadeIn(cap_lab),
                      FadeIn(few, scale=0.5), run_time=0.6)
            self.play(*[d.animate.move_to([x1, yaxn, 0]) for d, x1 in zip(few, few_x1)],
                      FadeIn(few_lab, rate_func=window(0.7, 1.3, 1.3)), run_time=1.3)
            beat.wait_until("spread term", offset=-0.15)
            self.play(flag(self.fpurp, color=PURPLE), flag(fb_gap, color=PURPLE),
                      tfc(g_int, fb_full[4]), FadeIn(fb_full[3]), FadeIn(fb_full[5]),
                      TransformFromCopy(fb_gap[0][1:], fb_full[6]),
                      FadeIn(fb_full[7]), tfc(f_int, fb_full[8]), run_time=1.1)
            beat.wait_until("twice", offset=-0.1)
            self.play(flag(fb_full[6], color=PURPLE), flag(fb_full[4], color=BLUE),
                      flag(fb_full[2], color=PURPLE), run_time=0.9)

        # ============================================================ 7. payoff: Harvard 2009
        for m in (self.gbar, self.fblue, self.fpurp, self.fout, g_int, f_int):
            m.clear_updaters()
        ax = axes((0, 125), (0, 8), x_ticks=[0, 30, 60, 90, 120], y_ticks=[0, 2, 4, 6, 8],
                  x_length=9.4, y_length=3.7, x_label="days since 1 September 2009",
                  y_label="diagnosed with flu (% of group)")
        ax.move_to([0.45, 0.12, 0])            # round 3: shorter, so the read-out rows clear the y title
        for mm in (ax.x_axis.numbers, ax.y_axis.numbers, ax.x_title, ax.y_title):
            mm.set_color(GRAY_T)
        cf_cite = citation("Christakis & Fowler, 2010 · PLoS ONE · Fig. 3 redrawn, logistic refit",
                           color=GRAY_T)
        lab_rand = Text("319 random students", font=SERIF, font_size=28, color=BLUE)
        lab_rand.move_to(ax.c2p(60, 0.72))          # clear of the blue fit (round 3)
        lab_fr = Text("425 friends they named", font=SERIF, font_size=28, color=YELLOW)
        lab_fr.next_to(ax.c2p(3, 5.6), RIGHT, buff=0)
        fit_fr = DashedVMobject(ax.plot(lambda t: logistic(t), x_range=[0, 125, 0.5]),
                                num_dashes=70).set_stroke(YELLOW, 3.5)
        fit_rd = DashedVMobject(ax.plot(lambda t: logistic(t, LEAD), x_range=[0, 125, 0.5]),
                                num_dashes=70).set_stroke(BLUE, 3.5)
        ay = 2.8                                       # any height works: the fits are a pure shift
        t_fr = LOG_M + LOG_S * np.log(ay / (LOG_C - ay))
        dpu = (ax.c2p(1, 0)[0] - ax.c2p(0, 0)[0])            # units per day
        TIP = 0.16

        def lead_arrow_at(tip, days, color=INK):
            return Arrow(tip + RIGHT * days * dpu, tip, buff=0, color=color, stroke_width=4,
                         max_tip_length_to_length_ratio=min(0.95, TIP / max(days * dpu, 1e-3)),
                         max_stroke_width_to_length_ratio=40)
        lead_arrow = lead_arrow_at(ax.c2p(t_fr, ay), LEAD)
        # read-out above the plot frame (round 3): label left, arrow right, the two arrow tips
        # aligned at the chart's own day scale.  "C&F" says whose 13.9 days it is (the dashed
        # curves are a refit with that shift); the self-reported number is a live readout of
        # its own arrow, counting down as the arrow shrinks.
        RO_TIPX, RO_Y1, RO_Y2 = 5.5, 3.42, 2.92
        ro_tip = np.array([RO_TIPX, RO_Y1, 0.0])
        ro_arrow = lead_arrow_at(ro_tip, LEAD)
        lead_lab = Text("C&F fitted lead: 13.9 days", font=SERIF, font_size=26, color=INK)
        lead_lab.move_to([RO_TIPX - 0.25, RO_Y1, 0], aligned_edge=RIGHT)
        ro2_tip = np.array([RO_TIPX, RO_Y2, 0.0])
        ro2_long = lead_arrow_at(ro2_tip, LEAD, color=GRAY)
        self_len, sn_op = ValueTracker(LEAD), ValueTracker(0.0)
        ro2_live = always_redraw(lambda: lead_arrow_at(ro2_tip, self_len.get_value(), color=GRAY))
        days_lab = Text("days", font=SERIF, font_size=26, color=GRAY_T)
        days_lab.move_to([RO_TIPX - 0.25, RO_Y2, 0], aligned_edge=RIGHT)
        base_y = days_lab[0].get_bottom()[1]                 # the baseline (bottom of the "d")
        self_num = DecimalNumber(LEAD, num_decimal_places=1, font_size=35, color=GRAY_T)

        def upd_sn(m):
            m.set_value(self_len.get_value())
            m.next_to(days_lab, LEFT, buff=0.14)
            m.shift(UP * (base_y - m.get_bottom()[1]))
            prog = float(np.clip((LEAD - self_len.get_value()) / (LEAD - SELF_LEAD), 0, 1))
            m.set_opacity(sn_op.get_value() * (0.1 + 0.9 * prog ** 2))   # solid only at 3.2
        upd_sn(self_num)
        self_lab = Text("self-reported:", font=SERIF, font_size=26, color=GRAY_T)
        self_lab.next_to(self_num, LEFT, buff=0.16)          # placed for the widest value, 13.9
        self_lab.shift(UP * (base_y - self_lab[0].get_bottom()[1]))
        cal = ValueTracker(0.0)
        rd_live = always_redraw(lambda: stepped_upto(ax, CF["random"]["steps_day_cases"], 319,
                                                     cal.get_value()).set_stroke(BLUE, 5))
        fr_live = always_redraw(lambda: stepped_upto(ax, CF["friends"]["steps_day_cases"], 425,
                                                     cal.get_value()).set_stroke(YELLOW, 5))
        origin_b = Dot(ax.c2p(0, 0), radius=0.05, color=BLUE)
        origin_y = Dot(ax.c2p(0, 0), radius=0.05, color=YELLOW)
        for dd in (origin_b, origin_y):
            self.allow_overlap(dd, reason="transient: each Facebook bar lands on its curve's origin, "
                                          "just above the x-axis '0', and fades as the curve grows")
        fade_out = VGroup(fb_full, self.ax_line, fb_ticks, fb_nums, self.ax_title, fb_gap, fb_tail,
                          fb_glabel, self.flabel, g_int, f_int)
        with self.narrate(NARR["cf"], gap=BREAK) as beat:
            # round 3: no Facebook legend parked over the Harvard chart.  Each bar flies straight
            # to the origin of the curve it becomes, and the curves grow from "tested".
            T = 1.6
            self.play(FadeOut(fade_out, rate_func=window(0, 0.45, T)),
                      FadeOut(ugander, rate_func=window(0, 0.35, T)),
                      FadeIn(cf_cite, rate_func=window(0.45, 1.0, T)),
                      Create(ax, rate_func=window(0.3, 1.45, T)),
                      ReplacementTransform(self.gbar, origin_b, rate_func=window(0.35, 1.6, T)),
                      ReplacementTransform(VGroup(self.fblue, self.fpurp, self.fout), origin_y,
                                           rate_func=window(0.35, 1.6, T)),
                      run_time=T)
            self.add(rd_live, fr_live, origin_b, origin_y)
            beat.wait_until("tested", offset=-0.1)
            T = beat.until("rose first", offset=-0.1, min_time=4.0)
            d_u = max(0.05, beat.time_of("three hundred") - 0.15 - beat.elapsed())
            d_fr = max(0.1, beat.time_of("four hundred") - 0.15 - beat.elapsed())
            self.play(cal.animate(rate_func=linear).set_value(125),
                      FadeOut(VGroup(origin_b, origin_y), rate_func=window(0.3, 0.8, T)),
                      FadeIn(lab_rand, shift=0.1 * UP, rate_func=window(d_u, d_u + 0.7, T)),
                      FadeIn(lab_fr, shift=0.1 * UP, rate_func=window(d_fr, d_fr + 0.7, T)),
                      run_time=T)
            rd_live.clear_updaters()
            fr_live.clear_updaters()
            self.play(ShowPassingFlash(fr_live.copy().set_stroke(INK, 8), time_width=0.35),
                      run_time=1.2)
            beat.wait_until("fitted", offset=-0.15)
            self.play(rd_live.animate.set_stroke(opacity=0.45), fr_live.animate.set_stroke(opacity=0.45),
                      Create(fit_fr), Create(fit_rd), run_time=1.2)
            beat.wait_until("thirteen", offset=-0.3)
            self.play(GrowArrow(lead_arrow), run_time=0.8)
            self.play(TransformFromCopy(lead_arrow, ro_arrow), FadeIn(lead_lab, shift=0.1 * RIGHT,
                      rate_func=window(0.5, 1.0, 1.0)), run_time=1.0)
            beat.wait_until("self-reported", offset=-0.15)
            self.play(TransformFromCopy(ro_arrow, ro2_long), FadeIn(self_lab, shift=0.1 * RIGHT),
                      run_time=0.8)
            self.remove(ro2_long)
            self.add(ro2_live)
            beat.wait_until("shrank", offset=-0.25)
            self.add(self_num)
            self_num.add_updater(upd_sn)
            self.play(sn_op.animate(rate_func=window(0, 0.2, 1.1)).set_value(1.0),
                      FadeIn(days_lab, rate_func=window(0.5, 1.1, 1.1)),
                      self_len.animate.set_value(SELF_LEAD), run_time=1.1)
            ro2_live.clear_updaters()
            self_num.clear_updaters()

        # ============================================================ 8. landing
        circ2, num2, name2, edges2 = self.build_network()
        glabel2 = Text("average girl", font=SERIF, font_size=28, color=INK)
        glabel2.move_to([X0, Y_GIRL + 0.55, 0], aligned_edge=LEFT)
        flabel2 = Text("average friend", font=SERIF, font_size=28, color=INK)
        flabel2.move_to([X0, Y_FRIEND + 0.6, 0], aligned_edge=LEFT)
        end_g = Rectangle(width=2.5 * UNIT, height=BAR_H, stroke_width=0, fill_color=BLUE,
                          fill_opacity=0.9).move_to([X0 + 1.25 * UNIT, Y_GIRL, 0])
        end_fb = Rectangle(width=2.5 * UNIT, height=BAR_H, stroke_width=0, fill_color=BLUE,
                           fill_opacity=0.9).move_to([X0 + 1.25 * UNIT, Y_FRIEND, 0])
        end_fp = Rectangle(width=0.5 * UNIT, height=BAR_H, stroke_width=0, fill_color=PURPLE,
                           fill_opacity=0.9).move_to([X0 + 2.75 * UNIT, Y_FRIEND, 0])
        end_fo = Rectangle(width=3.0 * UNIT, height=BAR_H, stroke_color=YELLOW, stroke_width=4,
                           fill_opacity=0).move_to([X0 + 1.5 * UNIT, Y_FRIEND, 0])
        end_gn = MathTex("2.5", font_size=40, color=BLUE).next_to(end_g, RIGHT, buff=0.2)
        end_fn = MathTex("3.0", font_size=40, color=YELLOW).next_to(end_fo, RIGHT, buff=0.2)
        panel2 = VGroup(glabel2, flabel2, end_g, end_fb, end_fp, end_fo, end_gn, end_fn)
        fewer = ["Betty", "Jane", "Pam", "Dale", "Tina"]
        more = ["Sue", "Alice"]
        favg = {}
        for n in fewer + more:
            favg[n] = MathTex(FAVG_TXT[n], font_size=36, color=YELLOW).next_to(
                circ2[n], FAVG_DIR[n], buff=0.26)
        favg["Sue"].move_to([-4.62, -0.12, 0])
        legend = Text("her friends' average", font=SERIF, font_size=26, color=YELLOW)
        legend.move_to([-SAFE_X + legend.width / 2 + 0.05, -2.4, 0])
        chart = VGroup(ax, fr_live, rd_live, fit_fr, fit_rd, lab_rand, lab_fr, lead_arrow, ro_arrow,
                       lead_lab, ro2_live, self_lab, self_num, days_lab)
        with self.narrate(NARR["land1"]) as beat:
            w_in = window(0.15, 1.15, 1.4)
            self.play(FadeOut(chart, rate_func=window(0, 1.0, 1.4)),
                      FadeOut(cf_cite, rate_func=window(0, 0.35, 1.4)),
                      FadeIn(feld, rate_func=window(0.45, 0.9, 1.4)),
                      *[FadeIn(circ2[n], rate_func=w_in) for n in NAMES],
                      *[FadeIn(num2[n], rate_func=w_in) for n in NAMES],
                      *[FadeIn(name2[n], rate_func=w_in) for n in NAMES],
                      *[Create(e, rate_func=window(0.6, 1.4, 1.4)) for e in edges2.values()],
                      FadeIn(panel2, rate_func=w_in), run_time=1.4)
            beat.wait_until("Five", offset=-0.1)
            self.play(FadeIn(legend, shift=0.1 * UP),
                      LaggedStart(*[AnimationGroup(circ2[n].animate.set_stroke(INK, width=6),
                                                   FadeIn(favg[n], scale=0.7))
                                    for n in fewer], lag_ratio=0.22), run_time=1.8)
            beat.wait_until("only Sue", offset=-0.1)
            self.play(*[circ2[n].animate.set_stroke(BLUE, width=3.5) for n in fewer],
                      *[favg[n].animate.set_opacity(0.3) for n in fewer],
                      circ2["Sue"].animate.set_stroke(INK, width=8), FadeIn(favg["Sue"], scale=0.7),
                      run_time=0.6)
            beat.wait_until("Alice", offset=-0.1)
            self.play(circ2["Alice"].animate.set_stroke(INK, width=8), FadeIn(favg["Alice"], scale=0.7),
                      run_time=0.6)

        last_toks = self.tokens_for(EDGES, P, K)
        cnt_n, cnt_s = ValueTracker(0), ValueTracker(0)
        toks_last = {n: [t[2] for t in last_toks if t[1] == n] for n in NAMES}
        others = [t[2] for t in last_toks if t[1] not in ("Sue", "Betty")]
        tal_x, ty1, ty2 = 2.55, 0.3, -0.45
        tal_sue = VGroup(*[net_token(4) for _ in range(4)]).arrange(RIGHT, buff=0.1)
        tal_sue.move_to([tal_x, ty1, 0], aligned_edge=LEFT)
        tal_bet = net_token(1).move_to([tal_x, ty2, 0], aligned_edge=LEFT)
        for t in (*tal_sue, tal_bet):
            t[1].ss_host = t[0]
        n_sue = Text("Sue", font=SERIF, font_size=28, color=GRAY_T)
        n_sue.move_to([tal_x - 0.25, ty1, 0], aligned_edge=RIGHT)
        n_bet = Text("Betty", font=SERIF, font_size=28, color=GRAY_T)
        n_bet.move_to([tal_x - 0.25, ty2, 0], aligned_edge=RIGHT)
        four = MathTex(r"4\times", font_size=40, color=YELLOW)
        four.move_to([tal_sue.get_right()[0] + 0.3, ty1, 0], aligned_edge=LEFT)
        one = MathTex(r"1\times", font_size=40, color=YELLOW)
        one.move_to([tal_sue.get_right()[0] + 0.3, ty2, 0], aligned_edge=LEFT)
        with self.narrate(NARR["land2"]) as beat:
            self.add(*[t[2] for t in last_toks])
            T = beat.until("and you land", offset=-0.1, min_time=1.6)
            self.play(FadeOut(VGroup(*favg.values(), legend), rate_func=window(0, 0.4, T)),
                      *[circ2[n].animate(rate_func=window(0, 0.4, T)).set_stroke(BLUE, width=3.5)
                        for n in more],
                      self.fly_tokens(last_toks, T, cnt_n, cnt_s, K), run_time=T)
            # every friendship lands somewhere: keep only Sue's four and Betty's one bright
            dimy = interpolate_color(ManimColor(BG), ManimColor(YELLOW), 0.3)
            self.play(*[AnimationGroup(d[0].animate.set_fill(dimy, opacity=1.0),
                                       d[1].animate.set_color(interpolate_color(ManimColor(BG), ManimColor(YELLOW), 0.08)))
                        for d in others], run_time=0.6)
            # the tally: Sue's tokens and Betty's token, counted side by side
            beat.wait_until("a Sue", offset=-0.15)
            self.play(*[pulse(d, 1.3) for d in toks_last["Sue"]], FadeIn(n_sue),
                      LaggedStart(*[FadeIn(t, shift=0.25 * RIGHT) for t in tal_sue], lag_ratio=0.15),
                      FadeIn(four, scale=0.7), run_time=0.9)
            beat.wait_until("a Betty", offset=-0.15)
            self.play(*[pulse(d, 1.3) for d in toks_last["Betty"]], FadeIn(n_bet),
                      FadeIn(tal_bet, shift=0.25 * RIGHT), FadeIn(one, scale=0.7), run_time=0.8)
            # Betty's view: her one friend has four
            beat.wait_until("Betty looks", offset=-0.1)
            self.play(circ2["Betty"].animate.set_stroke(INK, width=6), run_time=0.6)
            beat.wait_until("sees four", offset=-0.1)
            self.play(Indicate(num2["Sue"], color=INK, scale_factor=1.3), run_time=0.8)
            # most seats: the five girls whose friends average more than they have
            beat.wait_until("most seats", offset=-0.15)
            self.play(LaggedStart(*[circ2[n].animate.set_stroke(INK, width=6)
                                    for n in ("Jane", "Pam", "Dale", "Tina")], lag_ratio=0.25),
                      run_time=1.2)

        self.end_card(hold=0.55)                 # trailing silence ~1.5 s


if __name__ == "__main__":
    assert_token_clearance()
    print("token layout: ok")
