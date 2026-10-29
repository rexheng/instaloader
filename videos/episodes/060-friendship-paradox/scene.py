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
import sample_space.style as _ssstyle

# Round 6b: CADENCE = "shaped" (PRODUCTION_GUIDE §13) sets the gaps between sentences by their
# role (questions, results, turns); section boundaries still get BREAK seconds.
BREAK = 0.7

HERE = Path(__file__).resolve().parent
GRAY_T = GRAY               # text-grade gray (names, ticks, citations): #A2AAB5, 7.7:1 on BG
GRAY = AXIS                 # lines (edges, axes, the dashed guess, the ruler): the old #8B939E

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
NAME_SHIFT = {"Sue": LEFT * 0.55, "Carol": LEFT * 0.06}   # (Carol: round 6b, 27-pt names)
# where each girl's friends' average sits in the landing (free of edges and names)
FAVG_DIR = {"Betty": UP, "Sue": DOWN + 0.45 * LEFT, "Alice": DOWN, "Jane": UP,
            "Pam": RIGHT, "Dale": LEFT, "Tina": UP}

# Round 7 C&F illustration (C&F's design): some of the eight girls are the random sample
# (BLUE rings); only they name friends (C&F asked each for 2-3; here each names all of hers,
# one token per friend), and whoever is named is the friend sample (YELLOW rings).  The random
# girls are not friends of one another, so the two samples do not overlap, as in C&F (319 + 425
# = 744 students).  Round 9 (substance 4): the draw is {Betty, Dale, Carol}, counts 1, 3, 2
# (mean 2.0, near the class's 2.5; the old {Betty, Jane, Pam, Tina} averaged 1.75), and their six
# tokens read 4, 4, 4, 2, 3, 1, which average exactly 3.0, the episode's own friend average.
CF_SHIFT = np.array([2.5, 0.0, 0.0])
CF_RANDOM = ["Betty", "Dale", "Carol"]
CF_DRAW = [("Betty", "Sue"), ("Dale", "Sue"), ("Dale", "Alice"), ("Dale", "Jane"),
           ("Carol", "Pam"), ("Carol", "Tina")]
CF_NAMED = ["Sue", "Alice", "Jane", "Pam", "Tina"]
CF_RING_W = 6                                  # ring stroke (0.06 units; round 9: was 8)
CF_RING_OUT = 0.36 + CF_RING_W * 0.01 / 2      # a ring's outer edge from its node centre
assert all(frozenset((a, b)) not in {frozenset(e) for e in EDGES}
           for i, a in enumerate(CF_RANDOM) for b in CF_RANDOM[i + 1:])
assert all(frozenset(p) in {frozenset(e) for e in EDGES} for p in CF_DRAW)
assert sorted({r for _, r in CF_DRAW}) == sorted(CF_NAMED)
assert not set(CF_RANDOM) & set(CF_NAMED)
CF_LEG_X = 3.45                                # legend (right of the class), left edge
CF_LEG_Y = (1.62, 1.2, 0.5)                    # "random students" / "name one friend each" /
                                               # "named friends"

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
BNAME_FONT = 21                                # 27 px cap height (round 6b)
BNAME_TOP = GIRL_Y - NODE_RB - 0.15            # top of the name labels under the nodes
BEAM_Y = -0.06                                 # 0.16 under the lowest name ink ("Betty")
SP = {}
for _k, (_l, _r) in COLS.items():
    SP[_l] = np.array([BX(_k) - PAIR_DX, GIRL_Y, 0.0])
    SP[_r] = np.array([BX(_k) + PAIR_DX, GIRL_Y, 0.0])
# Round 8: the sort's staging row.  Each girl first moves onto the beam row in her present
# left-to-right order (ties: the higher node first), then the row reorders by friend count.
STAGE_ORDER = sorted(NAMES, key=lambda n: (P[n][0], -P[n][1]))   # Betty Sue Dale Pam Alice ...
STAGE = {n: np.array([x, GIRL_Y, 0.0])
         for n, x in zip(STAGE_ORDER, sorted(SP[m][0] for m in NAMES))}
TOK_SIDE, TOK_GAP = 0.38, 0.06
# Round 6: a GRAY count ruler (ticks 1-4 at BX(k)) runs under the fulcra, so the girls visibly
# sit in pairs either side of their count and the balance points read off a scale.  The PURPLE
# distances are later drawn ON this ruler, with their labels above it and the count labels
# below it; everything under it moved down to make room.
# Round 9 (craft 2): each distance is its own segment, in one of two lanes above the GRAY ruler
# (the 1.5s in the lower lane, the 0.5s in the upper one, so every label sits right above the
# line it names and no segment visibly contains another); the ruler moved down 0.22 to make room
# under the BLUE 2.5, and everything below it moved with it.
DEV_Y = -1.40                                 # the count ruler
DLANE = {1: DEV_Y + 0.10, 4: DEV_Y + 0.10,     # |d| = 1.5: lower lane
        2: DEV_Y + 0.24, 3: DEV_Y + 0.24}     # |d| = 0.5: upper lane
DCAP = 0.04                                   # half-height of a segment's end cap
DLAB_Y = DEV_Y + 0.585                        # distance labels (one row above both lanes)
# each label over its own segment: a 0.5 over its whole length (nudged 0.04 outward so the two
# signed labels keep 0.15 apart), a 1.5 over the stretch only it covers (from 1 to 2, 3 to 4)
DLAB_X = {1: 1.5, 2: 2.25 - 0.025, 3: 2.75 + 0.025, 4: 3.5}
RTICK = 0.10                                  # ruler ticks point up only
RUL_UP = 0.5                                  # round 10: the ruler's lift during the beam beats
SQ_SCALE = BEAM_PER / 4                       # variance squares drawn at exactly 1/4 scale
SQ_TOP = DEV_Y - 0.57                         # their top edge (0.19 under the count labels)
AREA_Y = SQ_TOP - 1.5 * SQ_SCALE - 0.30       # their area labels (MathTex 36)
AREA_DY = 0.38                                # round 8: the zigzag of the area labels
LANE_Y = AREA_Y - AREA_DY - 0.42              # flight lane of the area labels into "10"
# Second review cycle: for the variance and the algebra the stacks leave and the whole beam
# picture moves by OFF (up by LIFT, right by XC so the balance point sits at x = 0); the bar
# panel goes to 0 and the rows are centred under the picture.  At "the extra half friend we
# measured" the picture moves back left (keeping the lift) and the panel returns.
LIFT = 2.3
XC = -BX(2.5)                                  # 3.12: centres the beam picture
OFF = np.array([XC, LIFT, 0.0])
RING_S, RING_C2 = 0.5, np.array([-4.95, -1.55, 0.0])    # ring thumbnail (the ring callback)

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
ROW_M = -2.3                                   # main row during the algebra (centred, x = 0)
ROW_S = -1.08                                  # the "split Sue's count" rows (flat, centred)
ROW_MR, X_MR = -2.2, 3.35                      # where the result row sits after the restore
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
    "open3": "How many friends does the average friend have? Pick one. [pause 1.8]",
    # round 6b (PRODUCTION_GUIDE §13 budget: <= 500 words, 3:15-3:35): every line below was
    # put through the mute test; what the frame already shows is no longer said
    "stakes": "The answer tells flu researchers whom to watch: random students, or the friends "
              "they name.",
    # round 10 (substance 4): the title already says friends have more, so the guess is voiced
    # as the viewer's own reasoning, not as a strawman ("The natural guess is ...")
    "guess": "Every friend is one of these eight girls, so two and a half sounds right.",
    "ring": "Check that on a rewired class where every girl has two friends. Send a token both "
            "ways along every friendship.",
    "ring2": "Each token reads the friend count where it lands: always two. Both averages are "
             "two: the guess holds.",
    "recount": "Now restore the real friendships and send the tokens again. They read one, two, "
               "three, or four, and average three.",
    # round 10 (craft 5): the 8.5 s breath group is split; the shortfall and its cause land
    # separately
    "fail": "The guess fell short by half a friend, [pause 0.5] because the tokens piled up "
            "unevenly: [pause 0.4] four on Sue, four on Alice, one on Betty.",
    "line": "Line the girls up by friend count, two at each count: they balance at two and a "
            "half.",
    "stack": "The tokens stack higher on the right, one per friend, so they balance at three.",
    # round 9 (craft 6): the k-squared sentence (199 wpm at 0.82) is its own beat at 0.78, after
    # a breath that lets "sixteen" land
    "sue": "Sue holds four tokens, each worth four: sixteen.",
    "sue2": "A girl with k friends adds k squared on top, and k on the bottom.",
    # round 6: "Now" gives "divide" a lead-in (Whisper dropped its weak onset); the variance
    # line names WHICH balance point, and "two and a quarter at the ends ..." (a restatement of
    # the area labels) is cut
    # round 9 (substance 1, craft 6): two states; the "÷ 8" row holds through a 0.8 s pause,
    # and the beat is spoken at 0.78
    "divide": "Now divide top and bottom by the eight girls. [pause 0.7] The average of k "
              "squared, seven and a half, over the average count, two and a half.",
    # round 7: the derivation gets a visible target: the measured "+0.5" moves to the corner
    # as "+0.5 ?" and stays there until the algebra fills it
    "ask": "Where does the extra half come from?",
    # round 9 (substance 3): "the girls' balance point" was heard as "girl's ... girl's"; the
    # pause after "square it" is 0.1 s longer, so the areas are read before they fly
    "variance": "Measure each girl's distance from the balance point, two and a half, and "
                "square it. [pause 1.6] The squares average one and a quarter, the variance, sigma "
                "squared. [pause]",
    # round 7: a 0.4 s breath after "four" and after "two and a half", so each number lands
    # (and its glyph flies) before the next one is spoken
    # round 8: "Split Sue's" ran together ("Splitsus", a 0.02 s gap) and "Take Sue's four" lost
    # its possessive ("Take Sue 4"); no possessive now, and the 4 flies on "four" with a 0.5 s
    # breath after it
    "split": "Take Sue, and split her four, [pause 0.5] into the balance point, two and a half, "
             "[pause 0.4] plus her distance, one and a half. Squaring gives two and a half squared, her "
             "distance squared, and a cross term. [pause 0.8] Every girl splits this way. Because the "
             "beam balances, the distances add to zero, and the cross terms cancel. [pause]",
    # round 6: reading pauses after the rebuilt row (C) and the split row (D1); the three
    # collapses happen in one move on "Here that's two and a half, plus a half"
    # round 7: a 0.3 s breath splits the collapse into its two steps (2.5 squared over 2.5, then
    # 1.25 over 2.5)
    # round 10 (substance 1): the rebuilt row and the split row get their equation holds
    # (2 s + 0.4 s per term)
    "result": "So the average of k squared is mu squared plus sigma squared. [pause 1.6] And friends "
              "average mu, plus sigma squared over mu. [pause 1.8] Here that's two and a half, "
              "[pause 0.3] plus a half: exactly the extra half friend we measured. [pause 0.9] With "
              "no spread, the ring had no gap. [pause 1.0]",
    # round 6: the spread cue ("a few had thousands") comes before the prediction, and the
    # title's "you" is paid off with Ugander et al.'s 92.7 % (no "so": the mean inequality does
    # not force a majority)
    "fb": "In twenty eleven, Facebook users averaged about a hundred ninety friends, and a few "
          "had thousands. [pause 0.4] If every friendship sent tokens, what would the tokens "
          "average? [pause 1.45]",
    # round 10 (craft 5): "Odds are, that includes you." is cut; it pre-empted the landing's
    # "Most of us are Betty", and its 2.2 s fund the pauses above
    "fb2": "About six hundred thirty five: the spread term is more than twice the mean. [pause 0.9] "
           "And ninety three percent of users had fewer friends than their friends averaged.",
    # round 6b: the year is on the chart's axis and the group sizes on its labels, so neither
    # is spoken; [pause] marks give the 25 s beat its breaths
    "cf": "Christakis and Fowler put this to work at Harvard. Named friends have more friends, so "
          "they sit closer to everyone else, and should catch flu first. [pause 0.5] They tracked "
          "flu diagnoses in random students, and in the friends the students named. [pause 0.5] "
          "The friends' curve rose first. [pause 0.4] Fitted curves put them thirteen point nine "
          "days ahead. [pause 0.7] With self-reported symptoms, the lead shrank to about three.",
    # round 6b: the landing is one move (the per-girl tally is cut; Facebook's 93 % now makes
    # the per-person point): Betty's view explains the 4, then the 2.5 and the 3
    # round 7: the last line turns the opening onto the viewer (5 of the 8 girls and 92.7 % of
    # Facebook users sit below their friends' average); the 2.5 / 3 resolution is silent
    # round 8: a breath before "Sue", and a 2.1 s silent pause after "sees four" that holds the
    # three-step resolution (2.5 counts the girls, the bar grows to 3, the 3 is ringed)
    "land": "Betty looks at her one friend, [pause 0.3] Sue, and sees four. [pause 2.1] Most of us "
            "are Betty.",
}


# ----------------------------------------------------------------------------- geometry
def unit(v):
    return v / np.linalg.norm(v)


def name_label(n, pos=P):
    t = Text(n, font=SERIF, font_size=27, color=GRAY_T)
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
    t = Text(n, font=SERIF, font_size=27, color=GRAY_T)
    return t.next_to(Circle(radius=R).move_to(RP[n]), ring_name_dir(n), buff=NAME_BUFF_DEFAULT)


def cf_legend():
    """Round 7: the C&F key, right of the class: BLUE "random students" / GRAY "name their
    friends" (one sentence over two lines), YELLOW "named friends"."""
    lr = Text("random students", font=SERIF, font_size=28, color=BLUE)
    ln = Text("name their friends", font=SERIF, font_size=22, color=GRAY_T)
    lf = Text("named friends", font=SERIF, font_size=28, color=YELLOW)
    for t, y in zip((lr, ln, lf), CF_LEG_Y):
        t.move_to([CF_LEG_X, y, 0], aligned_edge=LEFT)
    return lr, ln, lf


def _box_circle_gap(tb, c, r):
    """Gap between an axis-aligned box and a circle of radius r centred at c (exact)."""
    qx, qy = np.clip(c[0], tb[0], tb[2]), np.clip(c[1], tb[1], tb[3])
    return float(np.hypot(c[0] - qx, c[1] - qy)) - r


def cf_tok_end(s, r, pos, gap=0.15):
    """Round 9 (craft 7): where a C&F token parks.  At 45 % of the edge from the receiver's
    centre (not tucked under her ring), moved out along the edge only as far as it must go to
    keep `gap` from both rings' outer edges (exact box-to-circle distance); on an edge too short
    for that it sits where the two gaps are equal."""
    a, b = pos[r], pos[s]
    h = NET_TOK / 2

    def gaps(f):
        c = a + (b - a) * f
        tb = (c[0] - h, c[1] - h, c[0] + h, c[1] + h)
        return _box_circle_gap(tb, a, CF_RING_OUT), _box_circle_gap(tb, b, CF_RING_OUT)
    fs = np.linspace(0.30, 0.70, 401)
    ok = [f for f in fs if min(gaps(f)) >= gap]
    if ok:
        f = min(ok, key=lambda f: abs(f - 0.45))
    else:
        f = max(fs, key=lambda f: min(gaps(f)))
    return a + (b - a) * f


def cf_draw_issues(min_label_gap=0.15):
    """The C&F illustration's parked tokens against the shifted name labels, the legend, the
    rings (round 9: their 0.06 strokes, exact box-to-circle gap >= 0.15), every edge line and
    each other; and the legend against every name label and node."""
    Pc = {n: P[n] + CF_SHIFT for n in NAMES}
    labels = {n: name_label(n).shift(CF_SHIFT) for n in NAMES}
    for t in cf_legend():
        labels[t.text] = t
    h = NET_TOK / 2
    boxes = []
    issues = []
    for snd, rcv in CF_DRAW:
        c = cf_tok_end(snd, rcv, Pc)
        tb = (c[0] - h, c[1] - h, c[0] + h, c[1] + h)
        boxes.append(((snd, rcv), tb))
        for n, lab in labels.items():
            g = _box_gap(tb, _bbox(lab))
            if g < min_label_gap:
                issues.append(f"cf token {snd}->{rcv} is {g:.3f} from label {n!r}")
        for n, c2 in Pc.items():
            g = _box_circle_gap(tb, c2, CF_RING_OUT)
            if g < 0.15 - 1e-6:
                issues.append(f"cf token {snd}->{rcv} is {g:.3f} from the ring of {n}")
        for a, b in EDGES:
            if {a, b} == {snd, rcv}:
                continue
            ln = edge_line(a, b, Pc)
            pts = np.array([ln.point_from_proportion(t) for t in np.linspace(0, 1, 80)])
            inside = ((pts[:, 0] > tb[0] - 0.06) & (pts[:, 0] < tb[2] + 0.06) &
                      (pts[:, 1] > tb[1] - 0.06) & (pts[:, 1] < tb[3] + 0.06))
            if inside.any():
                issues.append(f"cf edge {a}-{b} runs past token {snd}->{rcv}")
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            if _box_gap(boxes[i][1], boxes[j][1]) < 0.04:
                issues.append(f"cf tokens {boxes[i][0]} and {boxes[j][0]} touch")
    for t in cf_legend():
        for n in NAMES:
            if _box_gap(_bbox(t), _bbox(labels[n])) < 0.3:
                issues.append(f"cf legend {t.text!r} is close to name {n!r}")
            cb = (Pc[n][0] - R, Pc[n][1] - R, Pc[n][0] + R, Pc[n][1] + R)
            if _box_gap(_bbox(t), cb) < 0.3:
                issues.append(f"cf legend {t.text!r} is close to node {n!r}")
        if t.get_right()[0] > SAFE_X - 0.05:
            issues.append(f"cf legend {t.text!r} runs to x = {t.get_right()[0]:.2f}")
    return issues


def assert_token_clearance():
    """Round-2 fix: the automated clearance assert the critics asked for."""
    real = {n: name_label(n) for n in NAMES}
    issues = token_layout_issues(P, EDGES, real)
    issues += token_layout_issues(RP, RING_EDGES, {n: ring_label(n) for n in NAMES})
    issues += cf_draw_issues()
    if issues:
        raise AssertionError("token layout:\n  " + "\n  ".join(issues))


# ----------------------------------------------------------------------------- helpers
def tfc(src, dst, **kw):
    """TransformFromCopy that is safe for objects with updaters (DecimalNumber etc.)."""
    return ReplacementTransform(src.copy().clear_updaters(), dst, **kw)


def RT_same(*a, **k):
    """ReplacementTransform between the SAME glyphs whose TeX strings differ only by an
    invisible strut or a TeX space (trow rows); exempt from the glyph-morph lint."""
    return allow_morph(ReplacementTransform(*a, **k))


def TFC_same(*a, **k):
    """TransformFromCopy between the same glyphs (see RT_same)."""
    # (round 9: a copy + ReplacementTransform, so windowed rate functions run forward in time;
    # TransformFromCopy interpolates 1 - alpha and mirrored every window)
    src, dst = a[0], a[1]
    return allow_morph(ReplacementTransform(src.copy(), dst, *a[2:], **k))


def net_token(val):
    """A token as it travels the network: a yellow square that shows the count it reads."""
    sq = Square(NET_TOK, stroke_width=0, fill_color=YELLOW, fill_opacity=1.0)
    lab = MathTex(str(val), font_size=NET_TOK_FONT, color=BG).move_to(sq)
    return VGroup(sq, lab)


def glyphs(m):
    """The glyph paths of a text mobject, flat (round 5: a DecimalNumber nests each digit two
    levels deeper than a MathTex part, so copying it onto a part morphed digits via points)."""
    return VGroup(*m.family_members_with_points())


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


def window(t0, t1, total, ease=smooth):
    """Rate function that runs an animation only between t0 and t1 seconds of a play()
    lasting `total` seconds (so one play can hold staggered starts without Succession)."""
    def f(t):
        return ease(float(np.clip((t * total - t0) / max(t1 - t0, 1e-3), 0, 1)))
    return f


def timed(anim, t0, t1, total):
    """Run a lagged animation (Create, Write) between t0 and t1 seconds of a `total`-second
    play.  (Round 6c: a window rate_func on a lagged animation is applied to every
    submobject's sub-alpha, so its first parts finished at once: the C&F x-axis was drawn
    in one frame across the still-visible class.  Here the window times the group.)"""
    anim.rate_func = linear
    return AnimationGroup(anim, rate_func=window(t0, t1, total))


def leave(t):
    """Ease for copies that start on top of their source: they move off it at once (a
    smooth start lingers half-overlapped, which reads as a doubled glyph)."""
    return rate_functions.ease_out_cubic(t)


# Round 8: the longest opacity ramp any YELLOW object gets.  YELLOW at 30-60 % reads khaki or
# brown (both critics caught it on every fade), so YELLOW enters and leaves in <= 0.2 s, or by
# growing / shrinking at full opacity.
YR = 0.2


def y_in(m, t0, total, shift=ORIGIN, scale=0.85):
    """YELLOW entrance inside a `total`-second play: full colour within YR seconds of t0."""
    return FadeIn(m, shift=shift, scale=scale, rate_func=window(t0, t0 + YR, total))


def y_out(m, t0, total, shift=ORIGIN, scale=0.85):
    """YELLOW exit inside a `total`-second play: gone within YR seconds of t0."""
    return FadeOut(m, shift=shift, scale=scale, rate_func=window(t0, t0 + YR, total))


def shrink_out(m, rate_func=smooth, to=None):
    """YELLOW exit at full colour: shrink to nothing about its centre (or into the point `to`),
    then leave the scene (a remover, so no zero-size remnant is left for the layout audit)."""
    start = m.copy()
    c0 = start.get_center()
    c1 = c0 if to is None else np.array(to, dtype=float)

    def upd(mob, b):
        mob.become(start.copy().scale(max(1.0 - b, 0.02)).move_to(c0 + (c1 - c0) * b))
        if b >= 0.999:
            mob.set_opacity(0.0)
    return UpdateFromAlphaFunc(m, upd, rate_func=rate_func, remover=True)


def swap(old, new, total, t_out=YR, t_in=(0.4, 0.85)):
    """Changed content never crossfades: the old term leaves upward, then the new one
    rises into place (round 2: no double-exposed glyphs).  Round 8: both opacity ramps are
    YR long, so a YELLOW term never sits half-transparent."""
    a1 = min(t_in[1], total)
    return [FadeOut(old, shift=UP * 0.12, rate_func=window(0, min(t_out, YR), total)),
            FadeIn(new, shift=UP * 0.12, rate_func=window(a1 - YR, a1, total))]


def pinch(old, new, total, t0=0.0, dur=0.6, to=None, kmin=0.5):
    """Round 9 (craft 3): replace a term IN ITS SLOT, never leaving the slot empty and never
    morphing glyphs: the old term shrinks to `kmin` of its size at full colour, hands over to
    the new one at that size, and the new term grows from there to full size, about the same
    centre.  `to` is that centre (default: the new term's, so the old one drifts there as the
    row re-centres).  Round 10 (substance 3): the hand-over is a cut at half size, not a
    0.1 s cross, so old and new glyphs are never on screen together (at 1:26.8 "60" and
    "7.5" sat on top of each other), and the slot is never visibly empty."""
    o0, n0 = old.copy(), new.copy()
    c_old = old.get_center().copy()
    c_new = np.array(to, dtype=float) if to is not None else new.get_center().copy()
    t_s1 = t0 + 0.46 * dur                                 # old shrink ends, new growth starts

    def upd_old(m, a):
        tt = a * total
        b = smooth(float(np.clip((tt - t0) / (t_s1 - t0), 0, 1)))
        m.become(o0.copy().scale(1.0 - (1.0 - kmin) * b).move_to(c_old + (c_new - c_old) * b))
        m.set_opacity(1.0 if tt < t_s1 else 0.0)

    def upd_new(m, a):
        tt = a * total
        b = smooth(float(np.clip((tt - t_s1) / (t0 + dur - t_s1), 0, 1)))
        m.become(n0.copy().scale(kmin + (1.0 - kmin) * b).move_to(n0.get_center()))
        m.set_opacity(1.0 if tt >= t_s1 else 0.0)
    new.set_opacity(0.0)
    return [UpdateFromAlphaFunc(old, upd_old, remover=True, rate_func=linear),
            UpdateFromAlphaFunc(new, upd_new, rate_func=linear)]


def pinch_staged(old, new, total, shrink, grow, kmin=0.5):
    """Round 10: pinch() with separate windows.  During `shrink` = (a, b) seconds the old term
    shrinks to kmin at full colour while it moves to the new term's centre; it waits there at
    kmin until grow[0], when it hands over (a cut, never an overlap) to the new term, which
    grows to full size during `grow`.  Used for rows whose terms change width: every term and
    operator moves in the same window, so nothing collides, and the reveal is still left to
    right."""
    o0, n0 = old.copy(), new.copy()
    c_old, c_new = old.get_center().copy(), new.get_center().copy()

    def upd_old(m, a):
        tt = a * total
        b = smooth(float(np.clip((tt - shrink[0]) / (shrink[1] - shrink[0]), 0, 1)))
        m.become(o0.copy().scale(1.0 - (1.0 - kmin) * b).move_to(c_old + (c_new - c_old) * b))
        m.set_opacity(1.0 if tt < grow[0] else 0.0)

    def upd_new(m, a):
        tt = a * total
        b = smooth(float(np.clip((tt - grow[0]) / (grow[1] - grow[0]), 0, 1)))
        m.become(n0.copy().scale(kmin + (1.0 - kmin) * b).move_to(c_new))
        m.set_opacity(1.0 if tt >= grow[0] else 0.0)
    new.set_opacity(0.0)
    return [UpdateFromAlphaFunc(old, upd_old, remover=True, rate_func=linear),
            UpdateFromAlphaFunc(new, upd_new, rate_func=linear)]


def grow_out(new, total, t0, dur):
    """A term grows at full colour out of its own centre between t0 and t0 + dur seconds."""
    n0 = new.copy()

    def upd(m, a):
        u = float(np.clip((a * total - t0) / dur, 0, 1))
        m.become(n0.copy().scale(max(smooth(u), 0.02)).move_to(n0.get_center()))
        if u <= 0.0:
            m.set_opacity(0.0)
    new.set_opacity(0.0)
    return UpdateFromAlphaFunc(new, upd, rate_func=linear)


def fly_into(mob, pts, total, t_fly, t_shrink):
    """Round 9: `mob` (a copy) flies along a smooth path through pts at its own size during
    t_fly = (a, b) seconds, then shrinks to nothing at the end point during t_shrink, at full
    colour (a value going INTO a slot, where its symbol grows out: see grow_out)."""
    m0 = mob.copy()
    path = VMobject().set_points_smoothly([np.array([q[0], q[1], 0.0], dtype=float) for q in pts])

    def upd(m, a):
        tt = a * total
        b = smooth(float(np.clip((tt - t_fly[0]) / (t_fly[1] - t_fly[0]), 0, 1)))
        k = 1.0 - smooth(float(np.clip((tt - t_shrink[0]) / (t_shrink[1] - t_shrink[0]), 0, 1)))
        m.become(m0.copy().scale(max(k, 0.02)).move_to(path.point_from_proportion(b)))
        if k <= 0.02:
            m.set_opacity(0.0)
    return UpdateFromAlphaFunc(mob, upd, rate_func=linear, remover=True)


def grow_down(sq, rate_func=smooth):
    """Round 9: a square grows DOWN from its full-width top edge (its side), height 0 -> side.
    (GrowFromEdge scales from the edge's midpoint, so the squares grew out of dots.)"""
    start = sq.copy()

    def upd(m, a):
        b = rate_func(a)
        if b <= 1e-3:
            m.become(start.copy().stretch(1e-3, 1, about_edge=UP)).set_opacity(0.0)
            return
        m.become(start.copy().stretch(b, 1, about_edge=UP))
    return UpdateFromAlphaFunc(sq, upd, rate_func=linear)     # (real seconds: no double ease)


def M(s, color=INK, size=46):
    return MathTex(s, font_size=size, color=color)


class Fr:
    """A fraction item for trow(): lists of (tex, colour) for the numerator and denominator."""
    def __init__(self, num, den):
        self.num, self.den = num, den


def _item(x):
    return (x, INK) if isinstance(x, str) else x


# Invisible struts: TeX's own numerator/denominator clearance (~0.09 units under a mu) is
# below BAR's 0.15; a phantom depth under every numerator and a phantom height over every
# denominator make TeX shift them all equally, so baselines stay uniform across a row.
NUM_STRUT = r"\vphantom{\rule[-0.45em]{0pt}{0pt}}"
DEN_STRUT = r"\vphantom{\rule{0pt}{0.9em}}"


def trow(*items, size=46):
    """Second review cycle: one TeX-typeset row (so baselines and spacing come from TeX; the
    old hand-built rows centred a lone mu on the fraction bar, which set it ~10 px high).
    items are str | (tex, colour) | Fr(...).  Returns a VGroup of parts mirroring `items`;
    a fraction part is VGroup(num, bar, den) with .num/.bar/.den, where num and den are
    VGroups of their MathTex parts."""
    subs, cols, layout = [], [], []
    for it in items:
        if isinstance(it, Fr):
            num, den = [_item(x) for x in it.num], [_item(x) for x in it.den]
            n0 = len(subs)
            for i, (t, c) in enumerate(num):
                subs.append(("{" + NUM_STRUT if i == 0 else "") + t)
                cols.append(c)
            subs.append(r"\over")
            cols.append(INK)
            for i, (t, c) in enumerate(den):
                subs.append((DEN_STRUT if i == 0 else "") + t + ("}" if i == len(den) - 1 else ""))
                cols.append(c)
            layout.append(("f", n0, len(num), len(den)))
        else:
            t, c = _item(it)
            layout.append(("s", len(subs)))
            subs.append(t)
            cols.append(c)
    m = MathTex(*subs, font_size=size)
    for part, c in zip(m, cols):
        part.set_color(c)
    out = []
    for L in layout:
        if L[0] == "s":
            out.append(m[L[1]])
        else:
            _, n0, nn, nd = L
            num, bar = VGroup(*m[n0:n0 + nn]), m[n0 + nn]
            den = VGroup(*m[n0 + nn + 1:n0 + nn + 1 + nd])
            g = VGroup(num, bar, den)
            g.num, g.bar, g.den = num, bar, den
            out.append(g)
    return VGroup(*out)


def fly(mob, target, waypoints=(), run_time=1.0, rate_func=smooth, squeeze=0.0, fade_in=0.2):
    """Move `mob` (a copy) along a smooth path through waypoints onto `target`, matching its
    height; used where a straight flight would cross labels.  `squeeze` shrinks it mid-flight
    (round 6: so a wider label threads a narrow gap).  Round 6c: the copy fades in over the
    first `fade_in` of its path, so it never sits stacked on the value it was copied from
    (a 2 s contact-sheet frame caught "635 / 635")."""
    pts = [mob.get_center(), *[np.array([w[0], w[1], 0.0], dtype=float) for w in waypoints],
           target.get_center()]
    path = VMobject().set_points_smoothly(pts)
    h0, h1 = mob.height, target.height

    def upd(m, a):
        b = rate_func(a)
        m.scale_to_fit_height((h0 + (h1 - h0) * b) * (1.0 - squeeze * np.sin(np.pi * b)))
        m.move_to(path.point_from_proportion(b))
        if fade_in > 0:
            m.set_opacity(float(np.clip(b / fade_in, 0.0, 1.0)))
    return UpdateFromAlphaFunc(mob, upd, run_time=run_time)


def along(mob, pts, fade_tail=0.0):
    """Move mob along a smooth path through pts (optionally fading over the last part)."""
    path = VMobject().set_points_smoothly([np.array(p, dtype=float) for p in pts])

    def upd(m, a):
        m.move_to(path.point_from_proportion(smooth(a)))
        if fade_tail:
            m.set_opacity(float(np.clip((1 - a) / fade_tail, 0, 1)))
    return UpdateFromAlphaFunc(mob, upd)


def glide(mob, pts, op=None, ease=smooth):
    """Round 7: move mob along a smooth path through pts; op=(a, b) ramps its opacity from a
    to b on the way (one updater, so position and opacity never fight)."""
    path = VMobject().set_points_smoothly([np.array(p, dtype=float) for p in pts])

    def upd(m, a):
        b = ease(a)
        m.move_to(path.point_from_proportion(b))
        if op is not None:
            m.set_opacity(op[0] + (op[1] - op[0]) * float(np.clip(2 * a, 0, 1)))
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
# Round 6c: dimmed YELLOW context sits at 50 %, not 30 % (at 30 % it reads olive, a palette slip
# critics docked in other episodes; PRODUCTION_GUIDE 13.2.8)
CTX_Y = 0.5


class Episode(NarratedScene):
    EPISODE = 60
    TITLE = "Why Your Friends Have More Friends Than You"
    PRONUNCIATIONS = {"Christakis": "/kɹɪstˈɑkɪs/"}
    # Round 5: back to 0.82.  The "166 wpm" flag on the 0.82 master was a Whisper artefact (it
    # transcribed 1:41-1:53 twice, 566 words for a 509-word script); the real pace there was
    # ~152 wpm.  0.80 measured 3:48 and ~143 wpm, slower and longer than the episode needs.
    SPEED = 0.82
    CADENCE = "shaped"

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
        # Round 8 (substance): the sub-part height check.  The toolkit measures a formula's
        # cap height as a whole, so a stacked \tfrac{1}{4} inside a 30-pt label passed at 29 px
        # while its digits were 19 px.  TeX sets scripts, \tfrac and \scriptstyle parts at 70 %
        # of the formula's size: each of those must still clear the 24 px floor.
        for t in texts:
            if not isinstance(t, SingleStringMathTex):
                continue
            tex = getattr(t, "tex_string", "")
            if not any(k in tex for k in (r"\tfrac", "^", "_", r"\scriptstyle")):
                continue
            px = cap_height_px(t)
            if px is not None and 0.7 * px < 24.0:
                out.append(f"script-size: {tex[:24]!r} scripts at {0.7 * px:.0f} px (< 24 px)")
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
                # round 8: a token leaves its sender at full colour, growing from a quarter of
                # its size over the first fifth of its path (it used to fade in, through khaki)
                d.scale_to_fit_width(NET_TOK * (0.25 + 0.75 * min(1.0, p / 0.2)))
                d.move_to(a + (b - a) * p)
                d[0].set_fill(opacity=0.0 if alpha <= w0 else 1.0)
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
        self.Gop = ValueTracker(1.0)                     # the girl read-out's opacity (swaps)
        self.Fop = ValueTracker(1.0)                     # the friend read-out's opacity
        # Round 7: the YELLOW outline has its own opacity.  YELLOW is never dimmed (at 30-60 %
        # it reads brown); when the panel steps back, the outline goes to 0 instead
        self.Yo = ValueTracker(1.0)

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
            m.set_stroke(opacity=self.Dm.get_value() * self.Fo.get_value() * self.Yo.get_value()
                         if w > 0.01 else 0.0)

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
            m.set_opacity(self.Gop.get_value())

        def upd_fn(m):
            m.set_value(self.fv.get_value())
            m.next_to([G["x0"] + max(self.Lf.get_value(), 0), G["yf"], 0], RIGHT, buff=0.2)
            m.set_opacity(self.Fop.get_value())
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

    def guess_tick(self, x_units):
        """Second review cycle: once the friend bar is drawn, the dashed guess box collapses
        into this one dashed tick at the guess (no doubled outline round the bar)."""
        h = BAR_H + 0.2
        t = DashedLine([X0 + x_units, Y_FRIEND - h / 2, 0], [X0 + x_units, Y_FRIEND + h / 2, 0],
                       color=GRAY, stroke_width=3, dash_length=0.075, dashed_ratio=0.55)
        t.ss_bg = True
        return t

    @staticmethod
    def collapse(box, tick, total):
        """The guess box closes onto its right edge, which stays as the tick."""
        return [box.animate(rate_func=window(0, 0.85 * total, total))
                .stretch_to_fit_width(0.02, about_edge=RIGHT).set_stroke(opacity=0),
                FadeIn(tick, rate_func=window(0.45 * total, total, total))]

    def make_counter(self):
        """Live tally: (sum of counts) / (tokens) = average."""
        self.n_tr, self.s_tr = ValueTracker(0), ValueTracker(0)
        self.c_op = ValueTracker(1.0)                    # fades the tally digits as a whole
        self.c_num = DecimalNumber(0, num_decimal_places=0, font_size=44, color=YELLOW)
        self.c_den = DecimalNumber(0, num_decimal_places=0, font_size=44, color=YELLOW)
        self.c_lab_n = Text("sum of counts", font=SERIF, font_size=27, color=INK)
        self.c_lab_d = Text("tokens", font=SERIF, font_size=27, color=INK)
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
        # Round 6: frame 0 already poses the question: the network with its friendships at
        # 40 %, and the two rows it is about ("average girl", "average friend ?") as 30 % ghosts
        # in the right half; each brightens when it is narrated (beat timings unchanged)
        qmark = MathTex("?", font_size=46, color=YELLOW).move_to([X0 + 0.3, Y_FRIEND, 0])
        for n in NAMES:                                   # first frame: the network, at 70 %
            circ[n].set_stroke(opacity=0.7).set_fill(opacity=0.11)
            name[n].set_opacity(0.7)
        ghost_edges = VGroup(*[edges[frozenset(e)].copy().set_stroke(opacity=0.4) for e in EDGES])
        for m in (self.glabel, self.flabel):         # (round 7: the YELLOW "?" is never a
            m.set_opacity(0.3)                        # 30 % ghost; it poses the question at full)
        self.add(ghost_edges, *circ.values(), *name.values(), feld, self.glabel, self.flabel, qmark)
        # round 9 (craft 6, substance 2): a breath after each of the first two sentences (the
        # cold open ran 10.7 s with no pause >= 0.35 s, so the question followed the 2.5 at once)
        with self.narrate(NARR["open1"], gap=0.45) as beat:
            self.play(LaggedStart(*[AnimationGroup(
                circ[n].animate.set_stroke(opacity=1.0).set_fill(opacity=0.16),
                name[n].animate.set_opacity(1.0)) for n in NAMES], lag_ratio=0.15),
                run_time=beat.until("every friendship", offset=-0.1, min_time=1.0))
            # every friendship is drawn at full strength over its 40 % ghost
            self.play(LaggedStart(*[Create(edges[frozenset(e)]) for e in EDGES], lag_ratio=0.12),
                      run_time=min(2.2, beat.remaining()))
            self.remove(ghost_edges)
            self.bring_to_front(*circ.values())

        with self.narrate(NARR["open2"], gap=0.7) as beat:
            self.play(LaggedStart(*[FadeIn(num[n], scale=0.6) for n in NAMES], lag_ratio=0.1),
                      self.glabel.animate.set_opacity(1.0), Create(self.axis),
                      run_time=beat.until("two and a half", offset=-0.3, min_time=1.0))
            self.Gop.set_value(0.0)
            self.gv.set_value(2.5)               # the read-out appears with its value (no count-up)
            self.add(self.gbar, self.gnum)
            copies = VGroup(*[num[n].copy() for n in NAMES])
            target = [X0 + 2.5 * UNIT + 0.45, Y_GIRL, 0]
            self.play(self.Lg.animate.set_value(2.5 * UNIT),
                      self.Gop.animate(rate_func=window(0.85, 1.3, 1.3)).set_value(1.0),
                      LaggedStart(*[c.animate.move_to(target).set_opacity(0) for c in copies],
                                  lag_ratio=0.05), run_time=1.3)
            self.remove(copies)

        # the "?" stops on three candidate answers: the girl average 2.5 (dashed line from
        # the girl bar), 3 and 4 (ghost drop lines above the axis ticks)
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
            self.play(self.flabel.animate.set_opacity(1.0), qmark.animate.set_opacity(1.0),
                      run_time=beat.until("average friend", offset=-0.3, min_time=0.6))
            # (round 8: each candidate grows at full colour, never a half-transparent YELLOW)
            self.play(LaggedStart(*[AnimationGroup(Create(ln), GrowFromCenter(c))
                                    for ln, c in zip((ref, ghosts[0], ghosts[1]), cands)],
                                  lag_ratio=0.45),
                      run_time=min(1.2, max(0.8, beat.until("Pick", offset=-0.15))))
            beat.wait_until("Pick", offset=-0.1)
            self.play(LaggedStart(*[Indicate(c, color=YELLOW, scale_factor=1.25) for c in cands],
                                  lag_ratio=0.35), run_time=1.3)

        # ============================================================ 2. stakes
        lab_r = Text("random", font=SERIF, font_size=27, color=BLUE).next_to(circ["Jane"], UP, buff=0.2)
        lab_f = Text("named friend", font=SERIF, font_size=27, color=YELLOW)
        lab_f.next_to(circ["Alice"], DOWN, buff=0.2).shift(RIGHT * 0.95)
        ring_a = Circle(radius=R, color=YELLOW, stroke_width=8).move_to(P["Alice"])
        ring_a.ss_bg = True
        arrow = Arrow(P["Jane"] + unit(P["Alice"] - P["Jane"]) * (R + 0.16),
                      P["Alice"] + unit(P["Jane"] - P["Alice"]) * (R + 0.14),
                      buff=0, color=YELLOW, stroke_width=5, max_tip_length_to_length_ratio=0.25)
        with self.narrate(NARR["stakes"], gap=BREAK) as beat:
            self.play(Indicate(qmark, color=YELLOW, scale_factor=1.35), run_time=0.9)
            beat.wait_until("whom to watch", offset=-0.1)
            self.play(circ["Jane"].animate.set_stroke(width=8), run_time=0.8)
            beat.wait_until("random students", offset=-0.15)
            self.play(FadeIn(lab_r, shift=0.1 * DOWN), run_time=0.7)
            beat.wait_until("friends they", offset=-0.1)
            self.play(GrowArrow(arrow), run_time=0.8)
            # (round 8: Alice's YELLOW ring is drawn over her BLUE one at full colour; recolouring
            # the stroke BLUE -> YELLOW passed through khaki)
            self.play(Create(ring_a), y_in(lab_f, 0.3, 0.8, shift=0.1 * UP), run_time=0.8)

        # ============================================================ 3. naive build
        guess = self.guess_rect(2.5 * UNIT)
        guess_lab = Text("guess", font=SERIF, font_size=27, color=GRAY_T)
        guess_lab.move_to([X0 + 0.17, Y_FRIEND, 0], aligned_edge=LEFT)
        with self.narrate(NARR["guess"]) as beat:
            # Round 10 (substance 4): the viewer's own reasoning, in its own order.  "Every
            # friend": the stakes labels leave (round 8: the YELLOW label, arrow and ring within
            # 0.2 s, or by shrinking) ...
            T = max(0.45, min(0.7, beat.until("these", offset=-0.2)))
            self.play(FadeOut(lab_r, rate_func=window(0, 0.6 * T, T)), y_out(lab_f, 0, T),
                      y_out(arrow, 0, T), Uncreate(ring_a, rate_func=window(0, 0.8 * T, T)),
                      circ["Jane"].animate.set_stroke(BLUE, width=3.5), run_time=T)
            # ... "one of these eight girls" (round 6b: the deictic lands on the highlight) ...
            beat.on("these", LaggedStart(*[Indicate(circ[n], color=BLUE, scale_factor=1.12)
                                           for n in NAMES], lag_ratio=0.06), run_time=1.1)
            # ... "so two and a half sounds right": the guess box grows to the girl average and
            # the candidates shrink to their centres at full colour
            beat.wait_until("two and a half", offset=-0.25)
            self.play(GrowFromEdge(guess, LEFT), flag(self.gnum, color=BLUE), FadeOut(ghosts),
                      *[shrink_out(c, rate_func=window(0, 0.5, 1.2)) for c in cands],
                      qmark.animate.next_to(guess, RIGHT, buff=0.15), run_time=1.2)
            self.remove(*cands)
            self.play(FadeIn(guess_lab), FadeOut(ref), run_time=0.6)

        # ---- the ring (hypothetical)
        keep = [e for e in RING_EDGES if frozenset(e) in edges]
        drop = [k for k in edges if k not in {frozenset(e) for e in RING_EDGES}]
        new = [e for e in RING_EDGES if frozenset(e) not in edges]
        ring_edges = {frozenset(e): edge_line(*e, RP) for e in RING_EDGES}
        ring_nums = {n: MathTex("2", font_size=38, color=INK) for n in NAMES}
        ring_names = {n: ring_label(n) for n in NAMES}
        whatif = VGroup(Text("what if:", font=SERIF, font_size=27, color=GRAY_T),
                        Text("everyone has 2", font=SERIF, font_size=27, color=GRAY_T),
                        Text("(hypothetical)", font=SERIF, font_size=27, color=GRAY_T, slant=ITALIC)
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
            anims += [self.Lg.animate.set_value(2.0 * UNIT),
                      self.gv.animate(rate_func=lambda t: float(t >= 0.5)).set_value(2.0),
                      self.Gop.animate(rate_func=there_and_back).set_value(0.0),
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

        gt = self.guess_tick(2.0 * UNIT)            # the guess, once the friend bar is drawn
        with self.narrate(NARR["ring2"], gap=BREAK) as beat:
            pile = VGroup(*[t[2] for t in ring_toks])
            beat.wait_until("reads", offset=-0.1)
            self.play(LaggedStart(*[pulse(t[2], 1.35) for t in ring_toks], lag_ratio=0.05),
                      run_time=1.5)
            beat.wait_until("Both averages", offset=-0.1)
            self.play(FadeOut(guess_lab), y_out(qmark, 0, 0.4), run_time=0.4)
            self.Fop.set_value(0.0)
            self.fv.set_value(2.0)               # the read-out appears with its value (no count-up)
            self.add(self.fblue, self.fpurp, self.fout, self.fnum)
            self.c_res.set_value(2.0)
            # the friend bar is drawn; the guess box closes onto its right edge, a single tick
            self.play(self.Lf.animate.set_value(2.0 * UNIT),
                      self.Fop.animate(rate_func=window(0.8, 1.0, 1.0)).set_value(1.0),
                      FadeIn(self.c_eq2), y_in(self.c_res, 0.5, 1.0), *self.collapse(guess, gt, 1.0),
                      run_time=1.0)
            beat.wait_until("guess holds", offset=-0.2)
            self.play(self.Lb.animate.set_value(2.0 * UNIT), flag(self.gnum, color=BLUE),
                      run_time=0.9)

        # ============================================================ 4. fail
        real_toks = self.tokens_for(EDGES, P, K)
        real_nums = {n: MathTex(str(K[n]), font_size=38, color=INK) for n in NAMES}
        guess3 = self.guess_rect(2.5 * UNIT)
        with self.narrate(NARR["recount"]) as beat:
            # the ring's friend bar and readout fade out (no count-down); the girl read-out
            # holds 2.0 until the real class has settled (second cycle: no transient 2.4)
            T = 1.5
            # (round 5: the ring's tokens and its "what if" label are gone before the nodes
            # sweep through them)
            # (round 8: the ring's tokens shrink to their centres at full colour; the YELLOW
            # outline and read-outs go in 0.2 s, the BLUE fills over 0.4 s)
            # Round 10 (substance 2): no YELLOW opacity ramp at all.  The ring's friend bar
            # retracts into the axis origin at full colour (outline and fill together), its
            # "2.0" shrinks into the origin with it, and the tally's 32, 16 and 2.0 shrink to
            # their centres (a 0.2 s fade still showed olive digits on one frame at 0:43.0)
            fnum_c = self.fnum.copy().clear_updaters()
            tally_c = [self.c_num.copy().clear_updaters(), self.c_den.copy().clear_updaters(),
                       self.c_res.copy()]
            self.Fop.set_value(0.0)
            self.c_op.set_value(0.0)
            self.remove(self.c_res)
            self.add(fnum_c, *tally_c)
            anims = [*[shrink_out(t, rate_func=window(0, 0.45, T)) for t in pile],
                     FadeOut(whatif, rate_func=window(0, 0.35, T)),
                     self.Lf.animate(rate_func=window(0, 0.55, T)).set_value(0.0),
                     self.Lb.animate(rate_func=window(0, 0.55, T)).set_value(0.0),
                     shrink_out(fnum_c, rate_func=window(0, 0.55, T), to=[X0 + 0.25, Y_FRIEND, 0]),
                     *[shrink_out(m, rate_func=window(0, 0.4, T)) for m in tally_c],
                     feld.animate.set_opacity(1.0)]
            anims += [FadeOut(ring_edges[frozenset(e)]) for e in new]
            anims += [circ[n].animate.move_to(P[n]) for n in NAMES]
            anims += [count_swap(num[n], real_nums[n], RP[n], P[n]) for n in NAMES]
            anims += [name[n].animate.move_to(name_label(n).get_center()) for n in NAMES]
            anims += [Transform(edges[frozenset(e)], edge_line(*e, P)) for e in keep]
            anims += [FadeOut(self.c_eq2, rate_func=window(0, 0.4, T))]
            self.play(*anims, run_time=T)
            self.remove(self.fnum, *pile, fnum_c, *tally_c)
            for tr in (self.Lf, self.Lb, self.fv):
                tr.set_value(0.0)
            self.Fo.set_value(1.0)
            self.Yo.set_value(1.0)
            self.n_tr.set_value(0)
            self.s_tr.set_value(0)
            self.c_op.set_value(1.0)
            self.remove(*[num[n] for n in NAMES])
            for n in NAMES:
                num[n] = real_nums[n]
            # the real class: the missing friendships return, the girl bar grows to 2.5 (its
            # read-out swaps 2.0 -> 2.5 while invisible), the guess tick follows the girl
            # average, and the guess box re-opens leftward from the tick
            guess.shift(RIGHT * 0.5 * UNIT)          # (collapsed and invisible) onto the new tick
            qmark.next_to(guess3, RIGHT, buff=0.15)
            T = 1.0
            gt0 = gt.copy()

            def upd_gt(m, al):                   # slide to 2.5, then hand over to the box edge
                tt = al * T
                m.become(gt0.copy().shift(RIGHT * 0.5 * UNIT * smooth(min(1.0, tt / 0.4))))
                m.set_stroke(opacity=1.0 - float(np.clip((tt - 0.4) / 0.3, 0, 1)))
            self.play(*[FadeIn(edges[k]) for k in drop],
                      self.Lg.animate(rate_func=window(0, 0.6, T)).set_value(2.5 * UNIT),
                      self.gv.animate(rate_func=lambda t: float(t >= 0.33)).set_value(2.5),
                      self.Gop.animate(rate_func=lambda t: there_and_back(min(1.0, t / 0.66)))
                      .set_value(0.0),
                      UpdateFromAlphaFunc(gt, upd_gt, rate_func=linear),
                      guess.animate(rate_func=window(0.3, 0.75, T))
                      .stretch_to_fit_width(2.5 * UNIT, about_edge=RIGHT).set_stroke(opacity=1),
                      # (round 8: the box's left edge used to sweep through the word; now the
                      # label is written only once the box has settled)
                      FadeIn(guess_lab, rate_func=window(0.78, 1.0, T)),
                      y_in(qmark, 0.78, T), run_time=T)
            self.remove(gt)
            gt.set_stroke(opacity=1.0)           # (kept at 2.5 for the next collapse)
            beat.wait_until("send", offset=-0.15)
            self.add(*[t[2] for t in real_toks])
            # (round 6b: "Twenty tokens add up to sixty" is cut, the counter shows it; the
            # tally flashes as the last token lands, the bar grows on "average three")
            self.play(self.fly_tokens(real_toks, beat.until("and average", offset=-0.15, min_time=3.5),
                                      self.n_tr, self.s_tr, K))
            beat.wait_until("average three", offset=-0.25)
            self.c_res.set_value(3.0)
            self.Fop.set_value(0.0)
            self.fv.set_value(3.0)
            self.add(self.fnum)
            # the YELLOW outline overshoots the guess; the box closes onto its tick at 2.5
            # (the tally flashes in the same move)
            self.play(Indicate(self.c_den, color=YELLOW, scale_factor=1.25),
                      Indicate(self.c_num, color=YELLOW, scale_factor=1.25),
                      FadeOut(guess_lab, rate_func=window(0, 0.4, 1.4)),
                      y_out(qmark, 0, 1.4),
                      self.Lf.animate.set_value(3.0 * UNIT),
                      self.Fop.animate(rate_func=window(1.2, 1.4, 1.4)).set_value(1.0),
                      FadeIn(self.c_eq2, rate_func=window(0, 1.0, 1.4)), y_in(self.c_res, 0.9, 1.4),
                      *self.collapse(guess, gt, 1.4), run_time=1.4)
        tokens = VGroup(*[t[2] for t in real_toks])

        gap_lab = MathTex(r"+0.5", font_size=36, color=PURPLE)
        gap_pct = MathTex(r"\cdot\ 20\%", font_size=36, color=PURPLE)
        gap_lab.next_to([X0 + 2.75 * UNIT, Y_FRIEND + BAR_H / 2, 0], UP, buff=0.26)
        gap_pct.next_to(gap_lab, RIGHT, buff=0.12)
        gap_grp = VGroup(gap_lab, gap_pct)
        toks_of = {n: [t[2] for t in real_toks if t[1] == n] for n in NAMES}
        with self.narrate(NARR["fail"], gap=BREAK) as beat:
            # the guess is the girl average: it fills the friend bar only up to the tick
            self.play(self.Lb.animate.set_value(2.5 * UNIT), flag(self.gnum, color=BLUE),
                      run_time=beat.until("half a friend", offset=-0.25, min_time=0.5))
            self.play(self.Po.animate.set_value(1.0), FadeIn(gap_grp, shift=0.1 * UP), run_time=0.9)
            for who in ("Sue", "Alice", "Betty"):
                beat.wait_until(f"on {who}", offset=-0.05)
                self.play(*[pulse(d, 1.3) for d in toks_of[who]],
                          Indicate(circ[who], color=BLUE, scale_factor=1.08), run_time=0.8)

        # ============================================================ 5. insight
        beam = Line([BX(0.62), BEAM_Y, 0], [BX(4.38), BEAM_Y, 0], color=GRAY, stroke_width=3)
        fulc_b = Triangle(color=BLUE, fill_color=BLUE, fill_opacity=1, stroke_width=0).scale(0.24)
        fulc_b.move_to([BX(2.5), BEAM_Y - 0.06 - fulc_b.height / 2, 0])
        fb_lab = MathTex("2.5", font_size=40, color=BLUE).next_to(fulc_b, LEFT, buff=0.15)
        fb_lab.set_y(BEAM_Y - 0.16 - fb_lab.height / 2)   # 0.16 below the beam
        # the token balance point: a copy of the BLUE fulcrum that slides right as the token
        # layers land, with a live read-out (second cycle; it used to fade in at 3)
        fulc_y = fulc_b.copy().set_fill(BLUE, opacity=0.0)
        fy_num = DecimalNumber(2.5, num_decimal_places=1, font_size=40, color=YELLOW)
        fy_num.set_opacity(0.0)
        # round 3: every girl keeps her name; it rides onto the beam under her node
        bname = {}
        for n in NAMES:
            t = Text(n, font=SERIF, font_size=BNAME_FONT, color=GRAY_T)
            t.move_to([SP[n][0], BNAME_TOP, 0], aligned_edge=UP)
            bname[n] = t
        # Round 6: the count ruler.  Its ticks sit at BX(k), between each pair of girls with k
        # friends, so "two at each count" and the balance points read off a scale.
        # Round 10 (substance 5): while the beam is the picture the ruler sits RUL_UP higher,
        # 0.35 under the fulcrum labels (a 180 px gap detached it from the girls it measures);
        # it drops to DEV_Y (room for the distance lanes) as the picture lifts for the variance
        ry = DEV_Y + RUL_UP
        ruler = Line([BX(0.62), ry, 0], [BX(4.38), ry, 0], color=GRAY, stroke_width=2.5)
        rticks = VGroup(*[Line([BX(k), ry, 0], [BX(k), ry + RTICK, 0], color=GRAY,
                               stroke_width=2.5) for k in COLS])
        rnums = VGroup(*[MathTex(str(k), font_size=30, color=GRAY_T).next_to([BX(k), ry, 0], DOWN,
                                                                             buff=0.17) for k in COLS])
        ruler.ss_bg = True
        for t in rticks:
            t.ss_bg = True
        with self.narrate(NARR["line"]) as beat:
            beat.wait_until("Line", offset=-0.1)
            # Round 8 (craft 2): the sort moves in two stages, so no node ever passes through
            # another and no two names stack.  First the tokens shrink into the girls they
            # landed on (full colour), the friendships and names leave ...
            T = 0.4
            anims = [FadeOut(e) for e in edges.values()]
            anims += [shrink_out(d, to=P[t[1]]) for t, d in zip(real_toks, tokens)]
            anims += [FadeOut(gt), *[FadeOut(name[n], rate_func=window(0, YR, T)) for n in NAMES]]
            self.play(*anims, run_time=T)
            self.remove(*tokens, guess)
            # ... "Line the girls up": every girl moves to the row in her present left-to-right
            # order (Dale above Pam goes first), so no two paths cross ...
            self.play(*[circ[n].animate.move_to(STAGE[n]).scale(0.88) for n in NAMES],
                      *[num[n].animate.move_to(STAGE[n]) for n in NAMES], run_time=0.7)

            # ... "by friend count": the row reorders.  Girls moving left arc over the row and
            # girls moving right under it, each on a half circle centred on her own move, so the
            # paths nest (one slot, 0.8, apart) and never meet; all start and land together.
            def sort_arc(n):
                x0, x1 = STAGE[n][0], SP[n][0]
                dx = x1 - x0
                cx, rr_, sg = x0 + dx / 2, abs(dx) / 2, (1.0 if dx < 0 else -1.0)
                grp = VGroup(circ[n], num[n])

                def upd(m, a):
                    b = smooth(a)
                    m.move_to([cx - dx / 2 * np.cos(np.pi * b), GIRL_Y + sg * rr_ * np.sin(np.pi * b), 0])
                return UpdateFromAlphaFunc(grp, upd)
            self.play(*[sort_arc(n) for n in NAMES], run_time=1.3)
            # the names come back under their girls, and the count ruler draws under the beam
            # (ticks 1-4 between each pair), its labels in order on "two at each count"
            for n in NAMES:
                name[n].scale(BNAME_FONT / 26).move_to(bname[n].get_top(), aligned_edge=UP)
            T = beat.until("balance", offset=-0.5, min_time=1.0)
            self.play(*[FadeIn(name[n], rate_func=window(0, 0.35, T)) for n in NAMES],
                      Create(ruler, rate_func=window(0.1, 0.55, T)),
                      *[Create(tk, rate_func=window(0.3, 0.7, T)) for tk in rticks],
                      *[FadeIn(rn, shift=0.1 * UP, rate_func=window(min(0.4 + 0.15 * i, T - 0.4),
                                                                   min(0.4 + 0.15 * i + 0.35, T), T))
                        for i, rn in enumerate(rnums)],
                      run_time=T)
            # the beam draws once every name has settled (names cross its line in transit)
            self.play(Create(beam, rate_func=window(0, 0.55, 1.3)),
                      GrowFromPoint(fulc_b, fulc_b.get_bottom(), rate_func=window(0.4, 1.0, 1.3)),
                      FadeIn(fb_lab, shift=0.1 * RIGHT, rate_func=window(0.5, 1.1, 1.3)),
                      flag(self.gnum, color=BLUE), run_time=1.3)

        # numbered token squares stacked on their girl, landing layer by layer
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
        # layer j holds the j-th token of every girl with more than j friends.  Layer 1 is one
        # token per girl, so it balances where the girls do (2.5); every later layer lands only
        # further right: 38/14 = 2.71, 52/18 = 2.89, 60/20 = 3.0
        layers = [[(n, stacks[n][j]) for n in NAMES if K[n] > j] for j in range(4)]
        l_cnt = [len(L) for L in layers]                       # 8, 6, 4, 2
        l_sum = [sum(K[n] for n, _ in L) for L in layers]      # 20, 18, 14, 8
        with self.narrate(NARR["stack"]) as beat:
            beat.wait_until("tokens stack", offset=-0.3)
            T = beat.until("three", offset=-0.25, min_time=3.4)
            wins = [(0.0, 0.2 * T), (0.25 * T, 0.47 * T), (0.52 * T, 0.74 * T), (0.78 * T, T)]
            anims = []
            for j, L in enumerate(layers):
                a, b = wins[j]
                # (round 8: each token grows up out of the layer below it at full colour; a
                # fade-in passed through khaki)
                anims += [GrowFromEdge(t, DOWN, rate_func=window(a, b, T)) for n, t in L]

            def balance(tt):
                w = s_ = 0.0
                for j, (a, b) in enumerate(wins):
                    pj = smooth(float(np.clip((tt - a) / (b - a), 0, 1)))
                    w += pj * l_cnt[j]
                    s_ += pj * l_sum[j]
                return 2.5 if w < 1e-6 else s_ / w
            t_go = wins[1][0]
            fy = fulc_b.get_y()

            def upd_bal(_, al):
                tt = al * T
                bal = balance(tt)
                q = float(np.clip((bal - 2.5) / 0.03, 0, 1))   # yellow as soon as it moves
                fulc_y.move_to([BX(bal), fy, 0])
                fulc_y.set_fill(interpolate_color(ManimColor(BLUE), ManimColor(YELLOW), q),
                                opacity=1.0 if tt >= t_go else 0.0)
                fy_num.set_value(bal)
                fy_num.next_to(fulc_y, RIGHT, buff=0.15)
                fy_num.set_y(BEAM_Y - 0.16 - fy_num.height / 2)
                fy_num.set_opacity(float(np.clip((tt - t_go) / YR, 0, 1)))
            self.add(fulc_y, fy_num)
            self.play(*anims, UpdateFromAlphaFunc(VGroup(fulc_y, fy_num), upd_bal, rate_func=linear),
                      run_time=T)
            beat.wait_until("three", offset=-0.1)
            self.play(flag(fy_num, color=YELLOW), flag(self.fnum, color=YELLOW), run_time=0.8)
            # Round 6: the bar panel steps back to 35 % so the beam and the equation are the
            # only full-strength objects; it returns at "the extra half friend we measured"
            # (round 7: its YELLOW outline and read-out go to 0, never to a brown 35 %)
            self.play(self.Dm.animate.set_value(0.35), self.Gop.animate.set_value(0.35),
                      self.Fop.animate(rate_func=window(0, YR, 0.5)).set_value(0.0),
                      self.Yo.animate(rate_func=window(0, YR, 0.5)).set_value(0.0),
                      VGroup(self.glabel, self.flabel, self.axis, gap_grp).animate.set_opacity(0.35),
                      run_time=0.5)

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
        w = max(num_k2.width, den_k.width) + 0.18
        new_bar = Line(LEFT * w / 2, RIGHT * w / 2, stroke_width=3, color=INK)
        new_bar.move_to([self.c_eq1.get_left()[0] - 0.22 - w / 2, self.c_lab.bar.get_y(), 0])
        num_k2.next_to(new_bar, UP, buff=0.1)
        den_k.next_to(new_bar, DOWN, buff=0.1)
        with self.narrate(NARR["sue2"], speed=0.78) as beat:
            # Round 9 (craft 5): Sue's 16 is her share of the top.  On "k squared" a copy of it
            # flies (above Alice's stack, down the gap between the beam and the bar panel) into
            # the numerator, where "sum of counts" has just left, and pinches into the sum of
            # k squared; then "4 x 4 = 16" shrinks away at full colour, so it is no longer a
            # second YELLOW focal point through the algebra.
            beat.wait_until("k squared", offset=-0.55)
            T = 1.3
            # (the label's own 16 flies, so it never sits doubled on its source)
            g16, g44 = VGroup(*sue_eq[0][4:6]), VGroup(*sue_eq[0][0:4])
            x_gap = (BX(4.38) + X0) / 2
            p16 = [g16.get_center(), (g16.get_x() + 0.7, g16.get_y() + 0.02), (x_gap, 2.6),
                   (x_gap, 0.35), (x_gap + 0.55, -0.15), num_k2.get_center()]
            self.play(fly_into(g16, p16, T, (0.0, 0.85), (0.7, 0.9)),
                      *pinch(self.c_lab.num, num_k2, T, t0=0.55, dur=0.6),
                      Transform(self.c_lab.bar, new_bar, rate_func=window(0.1, 0.8, T)),
                      shrink_out(g44, rate_func=window(0.85, 1.3, T)), run_time=T)
            self.remove(sue_eq, g16, g44)
            beat.wait_until("k on the bottom", offset=-0.2)
            self.play(*swap(self.c_lab.den, den_k, 0.8, t_in=(0.35, 0.8)), run_time=0.8)
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
        B = row(frac(M(AVG, YELLOW), M(r"\mu", BLUE)), M("="),
                frac(M("7.5", YELLOW), M("2.5", BLUE)), M("="), M("3.0", YELLOW), buff=0.2)
        place(B, ROW_M0)

        swaps_after = []

        def slide(x, y, rf=None):
            """Same glyphs: move x onto y (matching its size), swap y in after the play."""
            swaps_after.append((x, y))
            r = y.height / max(x.height, 1e-6)
            if rf is None:
                return x.animate.scale(r).move_to(y.get_center())
            return x.animate(rate_func=rf).scale(r).move_to(y.get_center())

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
        with self.narrate(NARR["divide"], speed=0.78) as beat:
            beat.wait_until("Divide", offset=-0.1)
            # Round 5: the terms slide first; each "÷ 8" fades in only once its term has
            # parked (they overlapped mid-slide, "Σk²8" at 1:25).
            T = 1.2
            mv8 = window(0.0, 0.6, T)
            in8 = window(0.6, 1.2, T)
            self.play(slide(num_k2, B1[0].num[0], rf=mv8), FadeIn(B1[0].num[1], shift=0.1 * LEFT, rate_func=in8),
                      slide(den_k, B1[0].den[0], rf=mv8), FadeIn(B1[0].den[1], shift=0.1 * LEFT, rate_func=in8),
                      ReplacementTransform(c_bar, B1[0].bar, rate_func=mv8), slide(self.c_eq1, B1[1], rf=mv8),
                      slide(self.c_num, B1[2].num[0], rf=mv8), FadeIn(B1[2].num[1], shift=0.1 * LEFT, rate_func=in8),
                      slide(self.c_den, B1[2].den[0], rf=mv8), FadeIn(B1[2].den[1], shift=0.1 * LEFT, rate_func=in8),
                      ReplacementTransform(self.c_frac.bar, B1[2].bar, rate_func=mv8),
                      slide(self.c_eq2, B1[3], rf=mv8), slide(self.c_res, B1[4], rf=mv8), run_time=T)
            do_swaps()
            # Round 9 (substance 1, craft 3): one change, not three.  The "÷ 8" row holds through
            # the 0.8 s pause; on "The average" each "÷ 8" flashes BLUE (dividing by the eight
            # girls, each counted once) and is absorbed: every term pinches into its own slot
            # while its average grows out of the same point, numerators and denominators in the
            # same move, so no frame is left without a numerator.
            beat.wait_until("The average", offset=-0.4)
            parts8 = (B1[0].num, B1[0].den, B1[2].num, B1[2].den)
            self.play(*[Indicate(m[1], color=BLUE, scale_factor=1.25) for m in parts8], run_time=0.6)
            T = 0.8
            anims = []
            for i in (0, 2):
                anims += pinch(B1[i].num, B[i].num, T, dur=T)
                anims += pinch(B1[i].den, B[i].den, T, dur=T)
                anims.append(ReplacementTransform(B1[i].bar, B[i].bar))
            anims += [slide(B1[1], B[1]), slide(B1[3], B[3]), slide(B1[4], B[4])]
            self.play(*anims, run_time=T)
            self.remove(*[sm for m in parts8 for sm in m])
            do_swaps()
            # the new terms are flagged as they are named
            beat.wait_until("seven", offset=-0.15)
            self.play(flag(B[0].num, color=YELLOW), flag(B[2].num, color=YELLOW), run_time=0.7)
            beat.wait_until("average count", offset=-0.15)
            self.play(flag(B[0].den, color=BLUE), flag(B[2].den, color=BLUE),
                      flag(fb_lab, color=BLUE), run_time=0.8)

        # ---- variance.  Second cycle: first the stacks leave, the bar panel and the citation
        # go to 0, the main row parks dimmed at the bottom, and the beam picture moves by OFF
        # (up, and centred), so the squares and every row below sit in one centred column.
        def o(x, y):
            return np.array([x + XC, y + LIFT, 0.0])
        xf = BX(2.5) + XC                                   # the balance point, now x = 0
        # Round 9 (craft 2): every distance is its own PURPLE segment from the balance point to
        # its count, in its own lane above the GRAY ruler (1.5s low, 0.5s high), with a cap at
        # its far end; the BLUE mark at 2.5 rises through both lanes, where all four start.
        # Each label sits over its own segment, so no length visibly contains another.
        dseg = {k: Line(o(BX(2.5), DLANE[k]), o(BX(k), DLANE[k]), color=PURPLE, stroke_width=4)
                for k in COLS}
        dcap = {k: Line(o(BX(k), DLANE[k] - DCAP), o(BX(k), DLANE[k] + DCAP), color=PURPLE,
                        stroke_width=4) for k in COLS}
        dev_mark = Line(o(BX(2.5), DEV_Y), o(BX(2.5), DLANE[2] + DCAP), color=BLUE, stroke_width=6)
        dev_mark.ss_bg = True
        for t in (*dseg.values(), *dcap.values()):
            t.ss_bg = True                       # (the labels keep 0.15 from them by layout)
        dev_r = dseg[4]                          # Sue's distance
        dev_labs = {k: MathTex(f"{abs(k - 2.5):g}", font_size=36, color=PURPLE).move_to(
            o(BX(DLAB_X[k]), DLAB_Y)) for k in COLS}
        signed = {k: MathTex(f"{k - 2.5:+g}", font_size=36, color=PURPLE).move_to(dev_labs[k])
                  for k in COLS}
        squares, areas, edges_sq, segs = {}, {}, {}, dseg
        sq_top = SQ_TOP + LIFT
        for k, girls in COLS.items():
            side = SQ_SCALE * abs(k - 2.5)
            for n in girls:
                x = SP[n][0] + XC
                s = Square(side, stroke_color=PURPLE, stroke_width=2.5, fill_color=PURPLE,
                           fill_opacity=0.45)
                s.move_to([x, sq_top - side / 2, 0])
                squares[n] = s
                edges_sq[n] = Line([x - side / 2, sq_top, 0], [x + side / 2, sq_top, 0],
                                   color=PURPLE, stroke_width=2.5)
            # Round 10 (craft 6): one area label per PAIR, on one row, centred under its two
            # equal squares ("2.25 ×2"); round 8's eight zigzagged labels read as noise.  The four
            # labels sum to 4.5 + 0.5 + 0.5 + 4.5 = 10, the "10" they fly into.
            alab = MathTex(f"{(k - 2.5) ** 2:.2f}", r"\,{\times}2", font_size=36)
            alab[0].set_color(PURPLE)
            alab[1].set_color(GRAY_T)
            alab.move_to([BX(k) + XC, AREA_Y + LIFT, 0])
            areas[k] = alab
        lane_y = LANE_Y + LIFT
        # Round 6: the scale tag is MathTex 30, left of the squares, and stays for as long as
        # the squares are on screen (round 7: at full strength, 7.7:1; it is the only key to
        # the squares' sizes)
        # (round 8, substance 1: inline "1/4" at the label size, MathTex 36 = 35 px; the stacked
        # \tfrac's digits were 19 px, under the 24 px floor)
        quarter = MathTex(r"\text{sides at }1/4\text{ scale}", font_size=36, color=GRAY_T)
        quarter.move_to([squares["Betty"].get_left()[0] - 0.3 - quarter.width / 2,
                         sq_top - 1.5 * SQ_SCALE / 2, 0])
        # the variance row (flat), beside the squares it averages: sigma^2 = 10/8 = 1.25
        Vrow = MathTex(r"\sigma^2", "=", "10", "/", "8", "=", "1.25", font_size=38)
        for i in (0, 2, 6):
            Vrow[i].set_color(PURPLE)
        Vrow.move_to([squares["Alice"].get_right()[0] + 0.25, sq_top - 0.3, 0], aligned_edge=LEFT)
        ten = Vrow[2]
        self.gnum.clear_updaters()
        self.fnum.clear_updaters()
        # (round 7: the "+0.5" is not in the panel text: it becomes the derivation's target)
        panel_txt = VGroup(self.glabel, self.flabel, self.gnum, self.fnum, self.axis, gap_pct)
        main = VGroup(*B)
        lift_on = VGroup(*circ.values(), *num.values(), *name.values(), beam, fulc_b, fb_lab)
        ruler_grp = VGroup(ruler, rticks, rnums)  # (round 10: lifts RUL_UP less, back to DEV_Y)
        yfulc = VGroup(fulc_y, fy_num)            # the token balance point (3.0)
        # Round 7: the friend-average row is never dimmed (YELLOW at 50 % read brown): it parks
        # at full strength, scaled 0.8, on the bottom edge; park_c is where the algebra uses it
        m_shift = np.array([-main.get_x(), ROW_M - B[0].bar.get_y(), 0.0])
        park_c = main.get_center() + m_shift
        main_park = main.copy().scale(0.8)
        main_park.move_to([0.0, -3.08 + main_park.height / 2, 0.0])
        # Round 7: the open target.  The measured "+0.5" lifts out of the panel into the top
        # right corner as "+0.5 ?" and stays at full strength through the derivation; the
        # result's 0.5 flies into it at "exactly the extra half friend we measured"
        gap_home = gap_lab.get_center().copy()
        TAG = np.array([5.45, 3.3, 0.0])
        qtag = MathTex("?", font_size=36, color=PURPLE)
        qtag.next_to(gap_lab.copy().move_to(TAG), RIGHT, buff=0.12)
        # (round 7: a short question is read fast by Kokoro, 221 wpm at 0.82; at 0.74 it is a
        # deliberate 171 wpm)
        with self.narrate(NARR["ask"], speed=0.74) as beat:
            beat.wait_until("extra half", offset=-0.35)
            # (the "· 20%" steps out of the way first; the label rises right of the girl
            # bar's read-out, then into the corner)
            self.play(gap_pct.animate(rate_func=window(0, 0.3, 1.0)).set_opacity(0.0),
                      glide(gap_lab, [gap_home, gap_home + np.array([1.1, 0.07, 0]),
                                      [TAG[0] + 0.25, 2.85, 0], TAG], op=(0.35, 1.0)),
                      run_time=1.0)
            self.play(FadeIn(qtag, shift=0.1 * UP), flag(gap_lab, color=PURPLE), run_time=0.6)

        def dip(m, total, t0, t1, low=0.4):
            """Opacity of m dips to `low` between t0 and t1 seconds of a play and comes back."""
            def upd(mob, a):
                tt = a * total
                u = float(np.clip((tt - t0) / max(t1 - t0, 1e-3), 0, 1))
                mob.set_opacity(1.0 - (1.0 - low) * np.sin(np.pi * u))
            return UpdateFromAlphaFunc(m, upd)
        with self.narrate(NARR["variance"]) as beat:
            T = 1.2
            # The YELLOW token balance point (3.0) leaves (round 7: fully, it returns with the
            # result): the distances are measured from the girls' balance point, 2.5.
            # Round 8: the YELLOW stacks shrink back into their girls, and the 3.0 fulcrum and
            # Sue's "4 x 4 = 16" shrink to their centres, all at full colour, before the
            # picture moves (they used to fade out through khaki)
            y_home = [m.copy() for m in yfulc]
            self.play(*[shrink_out(t, rate_func=window(0, 0.45, T), to=SP[n])
                        for n in NAMES for t in stacks[n]],
                      FadeOut(sue_box, rate_func=window(0, 0.3, T)),
                      *[shrink_out(m, rate_func=window(0, 0.4, T)) for m in yfulc],
                      lift_on.animate(rate_func=window(0.45, T, T)).shift(OFF),
                      ruler_grp.animate(rate_func=window(0.45, T, T)).shift(OFF + DOWN * RUL_UP),
                      main.animate(rate_func=window(0.3, T, T)).scale(0.8).move_to(main_park),
                      self.Dm.animate(rate_func=window(0, 0.6, T)).set_value(0.0),
                      panel_txt.animate(rate_func=window(0, 0.6, T)).set_opacity(0.0),
                      feld.animate(rate_func=window(0, 0.6, T)).set_opacity(0.0), run_time=T)
            # (Scene.remove does not reach into a group that is not itself in the scene, so the
            # shrunken tokens are removed one by one)
            self.remove(*[t for n in NAMES for t in stacks[n]], sue_box, *yfulc)
            for m, h in zip(yfulc, y_home):        # (kept, invisible, for the return)
                m.become(h.shift(OFF)).set_opacity(0.0)
            beat.wait_until("distance", offset=-0.1)
            # each segment draws out of the balance point to its count, the two short ones
            # first, then its cap and its label
            T = 1.5
            ords = (2, 3, 1, 4)
            self.play(Create(dev_mark, rate_func=window(0, 0.3, T)),
                      *[Create(dseg[k], rate_func=window(0.1 + 0.22 * i, 0.55 + 0.22 * i, T))
                        for i, k in enumerate(ords)],
                      *[FadeIn(dcap[k], rate_func=window(0.5 + 0.22 * i, 0.65 + 0.22 * i, T))
                        for i, k in enumerate(ords)],
                      *[FadeIn(dev_labs[k], shift=0.08 * UP, rate_func=window(0.5 + 0.22 * i, 0.82 + 0.22 * i, T))
                        for i, k in enumerate(ords)], run_time=T)
            beat.wait_until("two and a half", offset=-0.15)
            self.play(flag(fb_lab, color=BLUE), Indicate(fulc_b, color=BLUE, scale_factor=1.2),
                      Indicate(dev_mark, color=BLUE, scale_factor=1.6), run_time=0.8)
            # each girl's distance drops to her square's top edge, visibly shrinking to the
            # square's 1/4 scale, then the square grows down from it and its area is written
            # (round 6: the count labels the copies pass dip to 40 % for the drop)
            # (round 6 timing: the drop starts on "and square it", the area labels are complete
            # within 1.4 s and are read through the 1.5 s pause; they fly into "10/8" on "The
            # squares average", and "= 1.25" lands on "quarter")
            # Round 9 (craft 1): length, then area.  On "square" each girl's distance drops,
            # shrinking to the 1/4 scale, onto the top edge of her square (0.5 s each, left to
            # right, 0.05 s apart); only then does her square grow down from that side (0.8 s);
            # then its area is written (0.4 s).  (Round 8 grew the squares from points in 0.3 s
            # and dropped the sides onto them afterwards.)
            beat.wait_until("square", offset=-0.3)
            order = sorted(NAMES, key=lambda n: SP[n][0])
            LAG, TD, TG, TA = 0.05, 0.5, 0.8, 0.4
            T = (len(order) - 1) * LAG + TD + TG + TA
            drops, grows, writes = [], [], []
            for i, n in enumerate(order):
                t0 = i * LAG
                # (ReplacementTransform of a copy: TransformFromCopy interpolates 1 - alpha, so a
                # windowed rate function ran mirrored and the sides dropped AFTER the squares grew,
                # which is what the round-9 critic saw)
                drops.append(ReplacementTransform(segs[K[n]].copy(), edges_sq[n],
                                                  rate_func=window(t0, t0 + TD, T)))
                grows.append(grow_down(squares[n], rate_func=window(t0 + TD, t0 + TD + TG, T)))
                if n == COLS[K[n]][1]:           # the pair's second square: write its label
                    writes.append(FadeIn(areas[K[n]], shift=0.08 * DOWN,
                                         rate_func=window(t0 + TD + TG, t0 + TD + TG + TA, T)))
            self.play(*drops, *grows, *writes, dip(rnums, T, 0.0, (len(order) - 1) * LAG + TD),
                      FadeIn(quarter, rate_func=window(TD + 0.2, TD + TG, T)), run_time=T)
            self.remove(*edges_sq.values())
            t_lab = beat.elapsed()
            beat.wait_until("squares", offset=-0.15)
            if beat.elapsed() < t_lab + 0.9:     # the area labels are read before they move
                self.hold(t_lab + 0.9 - beat.elapsed())
            # the labels themselves fly into "10" (no copies over the originals); the scale
            # tag steps back to 40 % and stays as long as the squares do
            x_turn = squares["Alice"].get_right()[0] + 0.4
            fl = [along(areas[k], [areas[k].get_center(), [areas[k].get_x(), lane_y, 0],
                                   [x_turn, lane_y, 0], [ten.get_x() - 0.3, ten.get_y() - 0.5, 0],
                                   ten.get_center()], fade_tail=0.25)
                  for k in sorted(COLS)]
            T = beat.until("quarter", offset=0.3, min_time=1.4)
            self.play(LaggedStart(*fl, lag_ratio=0.04, rate_func=window(0.0, T - 0.5, T)),
                      FadeIn(VGroup(Vrow[2], Vrow[3], Vrow[4]), rate_func=window(T - 0.95, T - 0.45, T)),
                      FadeIn(VGroup(Vrow[5], Vrow[6]), rate_func=window(T - 0.5, T, T)),
                      run_time=T)
            self.remove(*areas.values())
            beat.wait_until("variance", offset=-0.1)
            self.play(FadeIn(VGroup(Vrow[0], Vrow[1]), shift=0.1 * RIGHT), run_time=0.6)
            beat.wait_until("sigma", offset=-0.1)
            self.play(flag(Vrow[0], color=PURPLE), *[flag(s, color=PURPLE) for s in squares.values()],
                      run_time=0.8)

        # ---- why avg(k^2) = mu^2 + sigma^2: split Sue's 4 = 2.5 + 1.5, square, average
        def srow(*parts, colors=None):
            m = MathTex(*parts, font_size=S_FONT)
            for i, c in (colors or {}).items():
                m[i].set_color(c)
            m.move_to([0, ROW_S, 0], aligned_edge=LEFT)
            return m
        S1 = srow("4", "^2", "=", "(", "2.5", "+", "1.5", ")", "^2",
                  colors={4: BLUE, 6: PURPLE})
        S2 = srow("4", "^2", "=", "2.5", "^2", "+", "1.5", "^2", r"+\;\;", "2", r"\cdot", "2.5",
                  r"\cdot", "1.5", colors={3: BLUE, 4: BLUE, 6: PURPLE, 7: PURPLE, 11: BLUE, 13: PURPLE})
        S3 = srow(AVG, "=", r"\mu^2", "+", r"\sigma^2", r"+\;\;", "2", r"\mu", r"\cdot",
                  r"\text{avg}(d)", colors={0: YELLOW, 2: BLUE, 4: PURPLE, 7: BLUE, 9: PURPLE})
        S3z = srow(AVG, "=", r"\mu^2", "+", r"\sigma^2", r"+\;\;", "2", r"\mu", r"\cdot",
                   "0", colors={0: YELLOW, 2: BLUE, 4: PURPLE, 7: BLUE, 9: PURPLE})
        S4 = srow(AVG, "=", r"\mu^2", "+", r"\sigma^2", colors={0: YELLOW, 2: BLUE, 4: PURPLE})
        sx = -S3.width / 2                       # every split row starts where the widest one,
        for m in (S1, S2, S3, S3z, S4):          # centred, starts
            m.shift(RIGHT * sx)
        # round 6: every highlight box keeps the 0.15 spacing standard (buff 0.15; the "+"
        # before the cross term has a wider TeX space so it stays 0.15 clear of the box)
        box_c = SurroundingRectangle(VGroup(*S2[9:14]), color=INK, buff=0.15, corner_radius=0.08,
                                     stroke_width=3)
        box_c3 = SurroundingRectangle(VGroup(*S3[6:10]), color=INK, buff=0.15, corner_radius=0.08,
                                      stroke_width=3)
        # round 3: when avg(d) becomes 0 the box shrinks with it
        box_c3z = SurroundingRectangle(VGroup(S3[6], S3[7], S3[8], S3z[9]), color=INK, buff=0.15,
                                       corner_radius=0.08, stroke_width=3)
        box_c.ss_bg = box_c3.ss_bg = box_c3z.ss_bg = True
        # round 3: d is named where it is measured, between the beam and the distance line
        d_lab = MathTex("d", "=", "k", "-", r"\mu", font_size=36)
        d_lab[0].set_color(PURPLE)
        d_lab[4].set_color(BLUE)
        # Round 5: written at the right end of the PURPLE distance line it names (beside the
        # beam it sat on one line with the YELLOW fulcrum's "3.0" and read "3.0 d = k - mu")
        # (round 6: the count ruler runs on past tick 4, so the label starts 0.22 past its end)
        # Round 10 (craft 3): the signed distances no longer sum to a "0" under the balance
        # point, where it read as a tick label between 2 and 3.  Their average is written as
        # "avg(d) = 0", one line under "d = k - mu" at the ruler's right end (d_lab rises 0.16
        # to make the room; both keep >= 0.17 from each other and from the variance row)
        avgd = MathTex(r"\text{avg}(", "d", ")", "=", "0", font_size=36)
        for i in (0, 1, 2, 4):
            avgd[i].set_color(PURPLE)
        x_dl0 = BX(4.38) + XC + 0.22
        avgd.move_to([x_dl0 + avgd.width / 2, Vrow.get_top()[1] + 0.17 + avgd.height / 2, 0])
        d_lab.move_to([x_dl0 + d_lab.width / 2,
                       max(DLANE[4] + LIFT, avgd.get_top()[1] + 0.17 + d_lab.height / 2), 0])
        avgd.align_to(d_lab, LEFT)

        def whole(f, *extra):
            """After a transition the parts of a formula sit in the scene one by one; put the
            formula back as one object."""
            self.remove(*f.submobjects, *extra)
            self.add(f)
        # flight paths that thread between labels and squares (straight lines would cross them)
        x_sue, y_top = SP["Sue"][0] + XC, GIRL_Y + LIFT
        gap_x = (squares["Dale"].get_right()[0] + squares["Sue"].get_left()[0]) / 2
        with self.narrate(NARR["split"]) as beat:
            # (round 7: each number flies on its own word, and lands in the 0.4 s breath
            # before the next number is spoken)
            # (round 8: her node and name flash on "Sue"; her 4 leaves it on "four")
            beat.wait_until("Sue", offset=-0.1)
            self.play(flag(num["Sue"], color=INK), flag(name["Sue"], color=INK), run_time=0.6)
            beat.wait_until("four", offset=-0.3)
            four = num["Sue"].copy()
            # round 6 path: between the Dale and Sue nodes and names, right of the dimmed 3.0,
            # between the distance labels and the count labels, between Dale's and Sue's
            # squares, then left under the squares
            x_dl = (x_sue + SP["Dale"][0] + XC) / 2              # between the two nodes
            y_sq_bot = sq_top - SQ_SCALE * 1.5                  # bottom of the big squares
            # (round 9: the label row has a gap between "0.5" and "1.5" at count 3.1)
            x_lg = (dev_labs[3].get_right()[0] + dev_labs[4].get_left()[0]) / 2
            self.play(fly(four, S1[0], [(x_dl, y_top - 0.3), (x_dl, BNAME_TOP + LIFT - 0.35),
                                        (x_lg + 0.1, BEAM_Y + LIFT - 0.25),
                                        (x_lg, DLAB_Y + LIFT), (gap_x, DEV_Y + LIFT - 0.3),
                                        (gap_x, sq_top - 0.25), (gap_x - 0.5, y_sq_bot - 0.33),
                                        (S1[0].get_x() + 0.6, y_sq_bot - 0.38)], rate_func=leave),
                      FadeIn(S1[1], rate_func=window(0.8, 1.4, 1.4)),
                      FadeIn(S1[2], rate_func=window(0.8, 1.4, 1.4)), run_time=1.4)
            self.remove(four)
            self.add(S1[0])
            beat.wait_until("the balance point", offset=-0.1)
            self.play(Indicate(fulc_b, color=BLUE, scale_factor=1.2), flag(dev_mark, color=BLUE),
                      run_time=0.8)
            beat.wait_until("two and a half", offset=-0.2)
            self.play(FadeIn(VGroup(S1[3], S1[4]), shift=0.1 * UP), flag(fb_lab, color=BLUE),
                      run_time=0.7)
            beat.wait_until("her distance", offset=-0.1)
            self.play(flag(dev_r, color=PURPLE), timed(Write(d_lab), 0, 0.8, 0.8), run_time=0.8)
            beat.wait_until("one and a half", offset=-0.3)
            d15 = dev_labs[4].copy()
            x15 = dev_labs[4].get_x()
            self.play(fly(d15, S1[6], [(x15 - 0.45, DLAB_Y + LIFT - 0.05), (gap_x + 0.05, DEV_Y + LIFT - 0.3),
                                       (gap_x, sq_top - 0.25), (gap_x - 0.5, y_sq_bot - 0.33),
                                       (S1[6].get_x() + 0.4, y_sq_bot - 0.38)], rate_func=leave,
                          squeeze=0.4),
                      FadeIn(S1[5], rate_func=window(0.6, 1.2, 1.2)),
                      FadeIn(VGroup(S1[7], S1[8]), rate_func=window(0.6, 1.2, 1.2)), run_time=1.2)
            self.remove(d15)
            whole(S1)
            # (2.5 + 1.5)^2 -> 2.5^2 + 1.5^2 + 2*2.5*1.5: shared glyphs slide, the brackets
            # leave before new symbols arrive
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
            # every girl: average the three pieces.  Round 10 (craft 1): term by term, left to
            # right (lag 0.15), each of Sue's numbers pinches IN ITS SLOT into its symbol, so no
            # frame shows the row's operators without their terms: 4^2 -> avg(k^2), 2.5^2 ->
            # mu^2, 1.5^2 -> sigma^2, .2.5 -> mu and 1.5 -> avg(d) inside the box; the operators
            # and the box slide with the re-centred row
            beat.wait_until("Every girl", offset=-0.1)
            # (the row re-spaces in one 0.4 s move, Sue's numbers shrinking to half size into
            # their new slots with the operators; then the symbols grow out of them left to
            # right, 0.15 s apart, so nothing collides while the reveal still reads in order)
            T = 1.45
            SH, LP, GD = (0.0, 0.4), 0.15, 0.4
            gen = [(VGroup(S2[0], S2[1]), S3[0]), (VGroup(S2[3], S2[4]), S3[2]),
                   (VGroup(S2[6], S2[7]), S3[4]), (VGroup(S2[10], S2[11]), S3[7]), (S2[13], S3[9])]
            anims = []
            for i, (a_, b_) in enumerate(gen):
                g0 = SH[1] + LP * i
                anims += pinch_staged(a_, b_, T, SH, (g0, g0 + GD))
            ops = [(S2[2], S3[1]), (S2[5], S3[3]), (S2[8], S3[5]), (S2[9], S3[6]), (S2[12], S3[8])]
            anims += [RT_same(a_, b_, rate_func=window(SH[0], SH[1], T)) for a_, b_ in ops]
            self.play(LaggedStart(*[Indicate(circ[n], color=BLUE, scale_factor=1.1) for n in NAMES],
                                  lag_ratio=0.05, run_time=T),
                      flag(d_lab, color=PURPLE), *anims,
                      ReplacementTransform(box_c, box_c3, rate_func=window(SH[0], SH[1], T)),
                      run_time=T)
            self.remove(*[m for a_, _ in gen for m in a_.get_family()])
            whole(S3)
            # sigma^2 lands: it is the average of the eight squares, which flash with it
            self.play(flag(S3[4], color=PURPLE), *[flag(squares[n], color=PURPLE) for n in NAMES],
                      run_time=0.8)
            # the beam balances: the signed distances add to zero
            beat.wait_until("balances", offset=-0.2)
            T = 0.9
            sw = []
            for k in COLS:
                sw += swap(dev_labs[k], signed[k], T)
            self.play(*sw, run_time=T)
            beat.wait_until("add to zero", offset=-0.35)
            # the four signed distances ride down onto their own segments and along them into
            # the balance point, where they cancel (the BLUE mark flashes); at the same moment
            # "d = k - mu" is copied one line down and averaged: avg(d) = 0, its "k - mu"
            # pinching into the 0
            T = 1.4

            def merge(src, k):
                c = src.copy()
                p0 = c.get_center()
                sgn = np.sign(p0[0] - xf)
                ly = DLANE[k] + LIFT
                path = VMobject().set_points_smoothly([np.array(q, dtype=float) for q in (
                    p0, [p0[0] - sgn * 0.1, ly + 0.05, 0], [xf + sgn * 0.35, ly, 0], [xf, ly, 0])])
                h0 = c.height

                def upd(m, a):
                    b = leave(a)
                    m.move_to(path.point_from_proportion(b))
                    m.scale_to_fit_height(h0 * (1.0 - 0.6 * b))
                    m.set_opacity(1.0 - b ** 2)
                return c, UpdateFromAlphaFunc(c, upd, rate_func=window(0, 0.85, T, linear))
            mc = [merge(signed[k], k) for k in COLS]
            dl_c = d_lab.copy()
            self.play(*[a for _, a in mc],
                      Indicate(dev_mark, color=BLUE, scale_factor=1.6, rate_func=window(0.65, 1.25, T, there_and_back)),
                      TFC_same(VGroup(dl_c[0]), VGroup(avgd[1]), rate_func=window(0.3, 0.9, T)),
                      TFC_same(VGroup(dl_c[1]), VGroup(avgd[3]), rate_func=window(0.3, 0.9, T)),
                      *pinch(VGroup(dl_c[2], dl_c[3], dl_c[4]), avgd[4], T, t0=0.55, dur=0.75),
                      FadeIn(VGroup(avgd[0], avgd[2]), rate_func=window(0.75, 1.15, T)),
                      run_time=T)
            self.remove(*[c for c, _ in mc], dl_c, *dl_c)
            whole(avgd)
            # ... and that average is the one in the box: avg(d) pinches into 0 there while the
            # label's 0 flashes, and the box shrinks around what is left
            T = 0.9
            self.play(flag(avgd[4], color=PURPLE), *pinch(S3[9], S3z[9], T, dur=0.7),
                      Transform(box_c3, box_c3z, rate_func=window(0.35, 0.8, T)), run_time=T)
            beat.wait_until("cancel", offset=0.2)
            self.play(FadeOut(VGroup(S3[5], S3[6], S3[7], S3[8], S3z[9], box_c3), shift=0.12 * UP),
                      run_time=0.6)
            self.remove(S3, *S3.submobjects)
            whole(S4)

        # ---- the main row: numerators rebuilt from the identity and the variance.  Every row
        # from here on is typeset by TeX as one formula (trow), so mu sits on TeX's baseline.
        mu, s2 = (r"\mu", BLUE), (r"\sigma^2", PURPLE)
        C = trow(Fr([(r"\mu^2", BLUE), "+", s2], [mu]), "=",
                 Fr([("2.5", BLUE), ("^2", BLUE), "+", ("1.25", PURPLE)], [("2.5", BLUE)]), "=",
                 ("3.0", YELLOW))
        cnum, nnum = C[0].num, C[2].num
        f_s2mu = Fr([s2], [mu])
        f_125 = Fr([("1.25", PURPLE)], [("2.5", BLUE)])
        f_2552 = Fr([("2.5", BLUE), ("^2", BLUE)], [("2.5", BLUE)])
        # round 6: the split row has wider TeX spaces round the boxed fractions, so the 0.15
        # box buffs stay 0.15 clear of the neighbouring "+" and "="; it collapses straight to D4
        D1 = trow(Fr([mu, ("^2", BLUE)], [mu]), r"\;+\;", f_s2mu, r"\;=\;", f_2552, r"\;+\;", f_125,
                  "=", ("3.0", YELLOW))
        # round 7: the collapse is typeset first (D3, then D4) and happens in two steps on the
        # TeX baseline: mu^2/mu -> mu and 2.5^2/2.5 -> 2.5 (D3), then 1.25/2.5 -> 0.5 (D4)
        D3 = trow(mu, "+", f_s2mu, "=", ("2.5", BLUE), "+", f_125, "=", ("3.0", YELLOW))
        D4 = trow(mu, "+", f_s2mu, "=", ("2.5", BLUE), "+", ("0.5", PURPLE), "=", ("3.0", YELLOW))
        for g in (C, D1, D3, D4):
            place(g, ROW_M, x=0.0)

        # the ring comes back as a picture (thumbnail of the 0:31 ring) with its spread
        # collapsed to a point; 2 + 0/2 = 2 beside it (second cycle: the bars no longer change)
        rpos = {n: RING_C2 + RING_S * (RP[n] - RING_C) for n in NAMES}
        r_th = R * RING_S
        th_edges = VGroup(*[Line(rpos[a] + unit(rpos[b] - rpos[a]) * (r_th + 0.05),
                                 rpos[b] - unit(rpos[b] - rpos[a]) * (r_th + 0.05),
                                 color=GRAY, stroke_width=2) for a, b in RING_EDGES])
        th_nodes = VGroup(*[Circle(radius=r_th, stroke_color=BLUE, stroke_width=2.5, fill_color=BLUE,
                                   fill_opacity=0.16).move_to(rpos[n]) for n in NAMES])
        for c in th_nodes:
            c.ss_bg = True
        th_nums = VGroup(*[MathTex("2", font_size=32, color=INK).move_to(rpos[n]) for n in NAMES])
        for t_, c_ in zip(th_nums, th_nodes):
            t_.ss_host = c_                      # each digit is printed on its own node
        ring_th = VGroup(th_edges, th_nodes, th_nums)
        ring_pt = Dot(RING_C2, radius=0.07, color=PURPLE)
        rr = trow(("2", BLUE), "+", Fr([("0", PURPLE)], [("2", BLUE)]), "=", ("2", YELLOW), size=42)
        rr.move_to([RING_C2[0] + RING_S * RING_R + r_th + 0.45 + rr.width / 2, RING_C2[1], 0])
        rr.shift(UP * (RING_C2[1] - rr[2].bar.get_y()))

        def cancel_box(fr):
            """Round 6: the 0.15 spacing standard (craft) and clear of the exponent (substance)."""
            return SurroundingRectangle(fr, color=INK, buff=0.15, corner_radius=0.08, stroke_width=3)
        box1, box2 = cancel_box(D1[0]), cancel_box(D1[4])
        for bx in (box1, box2):
            bx.ss_bg = True

        pic = VGroup(*circ.values(), *num.values(), *name.values(), beam, fulc_b, fulc_y, fb_lab,
                     fy_num, ruler, rticks, rnums, *dseg.values(), *dcap.values(), dev_mark,
                     *signed.values())
        # the symbols of mu + sigma^2/mu, laid out where the ring's 2 + 0/2 will sit (round 10)
        rr_sym = trow(mu, "+", Fr([s2], [mu]), size=42)
        rr_sym.shift(np.array([rr.get_left()[0] - rr_sym.get_left()[0],
                               rr[2].bar.get_y() - rr_sym[2].bar.get_y(), 0.0]))
        with self.narrate(NARR["result"], gap=BREAK) as beat:
            # the friend average avg(k^2)/mu, parked dimmed at the bottom, comes back, and the
            # identity's right side replaces its numerator
            # Round 5: every glyph transform pairs like with like (a part with a part, never a
            # MathTex wrapper with a bare part); mismatched nesting smeared "1.25" and "3.0"
            # mid-move, because each glyph morphed into the whole target.
            # (round 7: it was parked at full strength, scaled 0.8; it rises back into place)
            # Round 10 (craft 4): one focal point.  As the main row rises, the whole picture
            # (girls, beam, ruler, distances, squares, their labels, d = k - mu and avg(d) = 0)
            # steps back to 35 %; only the identity, the variance row it uses and the "+0.5 ?"
            # target stay at full strength
            ctx = VGroup(*[m for m in pic.submobjects if m is not fulc_y and m is not fy_num],
                         *squares.values(), quarter, d_lab, avgd)
            self.play(main.animate.scale(1 / 0.8).move_to(park_c), flag(S4, color=INK),
                      ctx.animate.fade(0.65), run_time=0.8)
            beat.wait_until("is mu", offset=-0.6)
            T = 1.6
            self.play(FadeOut(VGroup(B[0].num, B[2].num), shift=0.12 * UP, rate_func=window(0, YR, T)),
                      RT_same(B[0].bar, C[0].bar, rate_func=window(0.15, 0.9, T)),
                      RT_same(B[0].den, C[0].den, rate_func=window(0.15, 0.9, T)),
                      RT_same(B[1][0], C[1], rate_func=window(0.15, 0.9, T)),
                      RT_same(B[2].bar, C[2].bar, rate_func=window(0.15, 0.9, T)),
                      RT_same(B[2].den, C[2].den, rate_func=window(0.15, 0.9, T)),
                      RT_same(B[3][0], C[3], rate_func=window(0.15, 0.9, T)),
                      RT_same(B[4][0], C[4], rate_func=window(0.15, 0.9, T)),
                      TFC_same(VGroup(*S4[2:5]), cnum, rate_func=window(0.5, 1.6, T, leave)),
                      TFC_same(B[2].den[0].copy(), nnum[0], path_arc=-1.2,
                                        rate_func=window(0.5, 1.6, T, leave)),
                      FadeIn(VGroup(nnum[1], nnum[2]), rate_func=window(0.9, 1.6, T)),
                      TFC_same(Vrow[6], nnum[3], rate_func=window(0.5, 1.6, T, leave)),
                      run_time=T)
            # round 6: the rebuilt row holds through a 1.6 s pause; it splits on "mu"
            beat.wait_until("average mu", offset=0.25)
            # the split: every term slides to exactly one place (no copies stacked on the
            # originals); the second fraction's bar and denominator then rise in under it
            cL, cR = C[0], C[2]
            T = 1.3
            mv = window(0.0, 0.85, T)
            self.play(RT_same(cL.num[0], D1[0].num, rate_func=mv),
                      RT_same(cL.num[1], D1[1], rate_func=window(0.25, 0.95, T)),
                      RT_same(cL.num[2], D1[2].num[0], rate_func=mv),
                      RT_same(cL.bar, D1[0].bar, rate_func=window(0, 0.55, T)),
                      RT_same(cL.den, D1[0].den, rate_func=window(0, 0.55, T)),
                      GrowFromCenter(D1[2].bar, rate_func=window(0.75, 1.05, T)),
                      FadeIn(D1[2].den, shift=0.15 * UP, rate_func=window(0.85, 1.3, T)),
                      RT_same(C[1], D1[3], rate_func=mv),
                      RT_same(VGroup(cR.num[0], cR.num[1]), D1[4].num, rate_func=mv),
                      RT_same(cR.num[2], D1[5], rate_func=window(0.25, 0.95, T)),
                      RT_same(cR.num[3], D1[6].num[0], rate_func=mv),
                      RT_same(cR.bar, D1[4].bar, rate_func=window(0, 0.55, T)),
                      RT_same(cR.den, D1[4].den, rate_func=window(0, 0.55, T)),
                      GrowFromCenter(D1[6].bar, rate_func=window(0.75, 1.05, T)),
                      FadeIn(D1[6].den, shift=0.15 * UP, rate_func=window(0.85, 1.3, T)),
                      RT_same(C[3], D1[7], rate_func=mv),
                      RT_same(C[4], D1[8], rate_func=mv),
                      FadeOut(Vrow, rate_func=window(0, 0.5, T)),
                      run_time=T)
            # the two fractions that cancel are boxed while "over mu" is said ...
            beat.wait_until("over mu", offset=-0.1)
            self.play(Create(box1), Create(box2), run_time=0.5)
            # ... round 7: then the collapse, in two steps on their own words, every glyph on
            # TeX's baseline.  "two and a half": the boxes, exponents, bars and denominators
            # fade in place, the surviving mu and 2.5 drop straight onto the baseline, then the
            # row closes up (D3)
            beat.wait_until("Here", offset=-0.15)
            T = 1.5
            m_mu, m_25 = D1[0].num[0], D1[4].num[0]

            def drop_slide(m, dst, t_drop=(0.3, 0.75), t_slide=(0.8, 1.5)):
                p0 = m.get_center().copy()
                p1 = np.array([p0[0], dst.get_y(), 0.0])
                p2 = dst.get_center()

                def upd(mob, a):
                    tt = a * T
                    u = smooth(float(np.clip((tt - t_drop[0]) / (t_drop[1] - t_drop[0]), 0, 1)))
                    v = smooth(float(np.clip((tt - t_slide[0]) / (t_slide[1] - t_slide[0]), 0, 1)))
                    mob.move_to(p0 + (p1 - p0) * u + (p2 - p1) * v)
                return UpdateFromAlphaFunc(m, upd)
            slide_t = window(0.8, 1.5, T)
            self.play(FadeOut(VGroup(box1, D1[0].num[1], D1[0].bar, D1[0].den,
                                     box2, D1[4].num[1], D1[4].bar, D1[4].den),
                              rate_func=window(0, 0.4, T)),
                      FadeOut(S4, rate_func=window(0, YR, T)),
                      drop_slide(m_mu, D3[0]), drop_slide(m_25, D3[4]),
                      *[RT_same(D1[i], D3[i], rate_func=slide_t) for i in (1, 2, 3, 5, 6, 7, 8)],
                      run_time=T)
            # "plus a half": 1.25/2.5 fades in place, the row closes up, and 0.5 rises into
            # the settled slot (D4)
            beat.wait_until("plus a half", offset=-0.15)
            T = 1.1
            mv = window(0.25, 0.8, T)
            self.play(FadeOut(D3[6], rate_func=window(0, 0.35, T)),
                      RT_same(m_mu, D4[0], rate_func=mv), RT_same(m_25, D4[4], rate_func=mv),
                      *[RT_same(D3[i], D4[i], rate_func=mv) for i in (1, 2, 3, 5, 7, 8)],
                      FadeIn(D4[6], shift=0.1 * UP, rate_func=window(0.45, 0.85, T)), run_time=T)
            # "exactly the extra half friend we measured": the 0.5 flies into the corner tag
            # and the "?" drops; then the picture moves back left, the bars return, the
            # result row moves under them and the tag goes home onto the PURPLE segment
            beat.wait_until("exactly", offset=-0.3)
            T = 0.8
            c05 = D4[6].copy()
            self.allow_overlap(c05, reason="the result's 0.5 lands on the tag's 0.5 and is removed "
                                           "in the same frame (a merge, not two labels)")
            tag05 = VGroup(*gap_lab[0][1:])
            x05 = D4[6].get_x()
            c05_from = c05.get_center().copy()
            f05 = fly(c05, tag05, [(x05, ROW_M + 0.9), (x05 + 2.8, ROW_M + 1.9),
                                   (TAG[0] - 0.2, 1.2), (TAG[0] + 0.05, 2.4)], run_time=T,
                      rate_func=window(0.05, 0.7, T, leave), fade_in=0.0)
            c05.set_opacity(0)

            def vis05(m, a):
                d = float(np.linalg.norm(m.get_center() - c05_from))
                m.set_opacity(float(np.clip((d - 0.45) / 0.3, 0, 1)))
            # (round 9, substance 5: the squares leave WITH their scale tag; they used to stay
            # 8 s longer with no scale, through the ring callback)
            self.play(FadeOut(VGroup(d_lab, avgd, quarter, *squares.values()), rate_func=window(0, 0.3, T)),
                      f05, UpdateFromAlphaFunc(c05, vis05, run_time=T),
                      FadeOut(qtag, shift=0.12 * UP, rate_func=window(0.55, 0.8, T)), run_time=T)
            self.remove(c05)
            d4 = VGroup(*D4)
            d4_shift = np.array([X_MR - d4.get_x(), ROW_MR - D4[2].bar.get_y(), 0.0])
            T = 1.1
            # Round 10: the beam picture moves back left still at 35 % (its YELLOW 3.0 fulcrum
            # no longer returns: it would be a second focal point beside the bars' 3.0); the bars
            # and their labels return at full strength (YELLOW outline and read-out within 0.2 s)
            self.play(pic.animate(rate_func=window(0, 0.6, T)).shift(LEFT * XC),
                      d4.animate(rate_func=window(0, 0.7, T)).shift(d4_shift),
                      self.Dm.animate(rate_func=window(0.5, 0.95, T)).set_value(1.0),
                      self.Yo.animate(rate_func=window(0.75, 0.95, T)).set_value(1.0),
                      VGroup(*[m for m in panel_txt if m is not gap_pct and m is not self.fnum])
                      .animate(rate_func=window(0.5, 0.95, T)).set_opacity(1.0),
                      self.fnum.animate(rate_func=window(0.75, 0.95, T)).set_opacity(1.0),
                      feld.animate(rate_func=window(0.4, 1.0, T)).set_opacity(1.0),
                      glide(gap_lab, [TAG, [TAG[0] + 0.25, 2.85, 0],
                                      gap_home + np.array([1.1, 0.07, 0]), gap_home],
                            ease=lambda t: smooth(float(np.clip((t * T - 0.25) / 0.7, 0, 1)))),
                      gap_pct.animate(rate_func=window(0.85, 1.1, T)).set_opacity(1.0), run_time=T)
            beat.wait_until("measured", offset=-0.15)
            self.play(flag(D4[6], color=PURPLE), flag(self.fpurp, color=PURPLE),
                      flag(gap_lab, color=PURPLE), run_time=0.9)
            # The ring (round 10, craft 7): the thumbnail of the 0:31 ring appears, its spread
            # collapses to a point, and the result row's own "mu + sigma^2/mu" is carried down
            # beside it (the same glyphs, a copy leaving the row, which stays whole); there each
            # symbol pinches in its slot into the ring's value, 2 + 0/2, and "= 2" grows.  No
            # YELLOW dims (the bars stay as they are), nothing fades out and back in.
            beat.wait_until("With no spread", offset=-0.2)
            self.play(FadeIn(ring_th, scale=0.85), run_time=0.5)
            spread = VGroup(*dseg.values(), *dcap.values()).copy().set_stroke(opacity=1.0)
            self.play(ReplacementTransform(spread, ring_pt), run_time=0.6)
            # (the copy is invisible for the first quarter of its path, so it never sits
            # doubled on the row it leaves)
            src = VGroup(D4[0], D4[1], D4[2]).copy()
            s0, s1 = src.get_center().copy(), rr_sym.get_center().copy()
            h0, h1 = src.height, rr_sym.height
            w0 = src.width

            def ride(m, a):
                b = leave(a)
                m.scale_to_fit_height(h0 + (h1 - h0) * b)
                m.move_to(s0 + (s1 - s0) * b)
                # invisible until it has cleared the row it leaves (no doubled glyphs)
                d = float(np.linalg.norm(m.get_center() - s0))
                m.set_opacity(float(np.clip((d - 0.75 * w0) / 0.35, 0, 1)))
            src.set_opacity(0.0)
            self.play(UpdateFromAlphaFunc(src, ride),
                      run_time=max(0.6, beat.until("no gap", offset=-0.1)))
            self.remove(src)
            self.add(*rr_sym)
            beat.wait_until("no gap", offset=-0.1)
            T = 0.95
            SH = (0.0, 0.3)
            self.play(*pinch_staged(rr_sym[0], rr[0], T, SH, (0.3, 0.6)),
                      RT_same(rr_sym[1], rr[1], rate_func=window(SH[0], SH[1], T)),
                      *pinch_staged(rr_sym[2].num, rr[2].num, T, SH, (0.42, 0.72)),
                      ReplacementTransform(rr_sym[2].bar, rr[2].bar, rate_func=window(SH[0], SH[1], T)),
                      *pinch_staged(rr_sym[2].den, rr[2].den, T, SH, (0.42, 0.72)),
                      FadeIn(rr[3], rate_func=window(0.55, 0.8, T)),
                      grow_out(rr[4], T, 0.6, 0.35), run_time=T)
            whole(rr)
            self.hold(max(0.0, beat.remaining() - 0.1))
            # (round 9: the ring's "2 + 0/2 = 2" stays whole into the Facebook beat, where it
            # leaves with the ring)

        # ============================================================ 6. Facebook
        beam_grp = VGroup(pic, ring_th, ring_pt)
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
        fb_full = trow(mu, "+", f_s2mu, "=", ("190", BLUE), "+", ("445", PURPLE), "=", ("635", YELLOW))
        place(fb_full, -1.75, x=0.0)
        panel = VGroup(self.glabel, self.flabel, self.gbar, self.fblue, self.fpurp, self.fout,
                       self.gnum, self.fnum, self.ax_line, self.ax_ticks, self.ax_nums, self.ax_title)
        fvt, fop = ValueTracker(635), ValueTracker(0.0)   # appears with its value, no count-up

        def upd_fi(m):
            m.set_value(fvt.get_value())
            m.next_to([G["x0"] + max(self.Lf.get_value(), 0), G["yf"], 0], RIGHT, buff=0.2 * s_)
            m.set_opacity(fop.get_value())
        f_int.add_updater(upd_fi)
        fb_gap = MathTex(r"+445", font_size=36 * s_, color=PURPLE)
        fb_gap.next_to([x0n + 635 * fbu, yfn + BAR_H * s_ / 2, 0], UP, buff=0.2)
        fb_gap.align_to([x0n + 635 * fbu, 0, 0], RIGHT)
        # "a few had thousands": the axis breaks and runs on to Facebook's 5,000 limit; a BLUE
        # brace marks the range those few users occupy (a range, not plotted data)
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
        cap_lab = Text("Facebook's limit", font=SERIF, font_size=22, color=GRAY_T)
        cap_lab.next_to(cap_num, DOWN, buff=0.14)
        cap_lab.align_to(cap_num, RIGHT)
        few_br = BraceBetweenPoints([x800 + 1.0, yaxn + 0.16, 0], [x_cap, yaxn + 0.16, 0],
                                    direction=UP, color=BLUE)
        few_lab = Text("a few users", font=SERIF, font_size=27, color=BLUE)
        few_lab.next_to(few_br, UP, buff=0.14)
        fb_tail = VGroup(brk, ext, cap_tick, cap_num, cap_lab, few_br, few_lab)
        # round 6: the title's "you" (Ugander et al. 2011: "92.7% of users have less friends
        # than the average friend count of their friends"), next to the "average user" row
        # (round 7: it sits beside the "average user" row only, away from the 635 bar, and
        # says "their own": Ugander's per-user statistic, not the edge average)
        # (round 8: one 5-word line, and the brace, "a few users" and "Facebook's limit" leave
        # as it is written, so the frame holds at most 12 words of prose)
        pct = MathTex(r"92.7\%", font_size=48, color=BLUE)
        pct_l1 = Text("below their own friends' average", font=SERIF, font_size=27, color=BLUE)
        pct_blk = VGroup(pct, pct_l1).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        pct_blk.move_to([0.55 + pct_blk.width / 2, 3.5 - pct_blk.height / 2, 0])
        # round 7: the axis name sits left of the axis, at its height, so nothing lies under
        # the tick labels where the three numbers drop into the row
        fb_title_to = self.ax_title.copy().scale(s_)
        fb_title_to.move_to([x0n - 0.3 - fb_title_to.width / 2, yaxn, 0])
        for t in pct_blk:
            t.ss_block = "pct"
        with self.narrate(NARR["fb"]) as beat:
            for m, _ in self._bar_upd:
                m.clear_updaters()
            # round 6: the beam picture and the ring (already at 30 %) clear as the beat starts
            # while the panel moves to the centre; the girls' data and Feld's citation stay
            # until "Facebook" ...
            T = beat.until("Facebook", offset=-0.1, min_time=1.0)
            # (round 8: the row's right side "= 2.5 + 0.5 = 3.0" leaves whole, in 0.2 s)
            # (round 10: the ring and its 2 + 0/2 = 2 leave first, the equation whole and at
            # full colour, before the row's mu + sigma^2/mu slides through where it stood)
            self.play(FadeOut(VGroup(pic, gap_grp), rate_func=window(0, min(0.6, T), T)),
                      FadeOut(VGroup(ring_th, ring_pt), rate_func=window(0, 0.4, T)),
                      shrink_out(rr, rate_func=window(0, 0.35, T)),
                      FadeOut(VGroup(*[D4[i] for i in range(3, 9)]), rate_func=window(0, YR, T)),
                      panel.animate(rate_func=window(0.15, T, T)).scale(s_, about_point=FB_C0).shift(FB_C1 - FB_C0),
                      ReplacementTransform(D4[0], fb_full[0], rate_func=window(0.35, T, T)),
                      ReplacementTransform(D4[1], fb_full[1], rate_func=window(0.35, T, T)),
                      ReplacementTransform(D4[2], fb_full[2], rate_func=window(0.35, T, T)),
                      run_time=T)
            G.update(x0=x0n, yg=ygn, yf=yfn, yax=yaxn, s=s_)
            for tr in (self.Lg, self.Lf, self.Lb):
                tr.set_value(tr.get_value() * s_)
            for m, f in self._bar_upd:
                m.add_updater(f)
            g_int.next_to([x0n + 190 * fbu, ygn, 0], RIGHT, buff=0.2 * s_)

            def upd_gi(m):
                m.next_to([G["x0"] + max(self.Lg.get_value(), 0), G["yg"], 0], RIGHT, buff=0.2 * s_)
            # ... and on "Facebook" the source, the row label and the axis change in one move
            T = 1.5
            self.play(FadeOut(feld, rate_func=window(0, 0.45, T)),
                      FadeIn(ugander, rate_func=window(0.5, 1.0, T)),
                      *swap(self.glabel, fb_glabel, T, t_out=0.5, t_in=(0.65, 1.2)),
                      *swap(self.ax_nums, fb_nums, T, t_out=0.5, t_in=(0.65, 1.2)),
                      ReplacementTransform(self.ax_ticks, fb_ticks),
                      self.ax_title.animate(rate_func=window(0.3, 1.2, T)).move_to(fb_title_to),
                      self.Lg.animate.set_value(190 * fbu),
                      self.Lf.animate.set_value(0.0), self.Lb.animate.set_value(0.0),
                      self.Po.animate.set_value(0.0),
                      FadeOut(self.fnum, rate_func=window(0, YR, T)),
                      FadeOut(self.gnum, rate_func=window(0, 0.4, T)),
                      run_time=T)
            g_int.add_updater(upd_gi)
            beat.wait_until("ninety", offset=-0.3)
            self.play(FadeIn(g_int), run_time=0.6)
            # the spread cue comes before the question: a few users had thousands
            beat.wait_until("a few", offset=-0.1)
            self.play(Create(brk), Create(ext), Create(cap_tick), FadeIn(cap_num), FadeIn(cap_lab),
                      run_time=0.6)
            self.play(GrowFromCenter(few_br), FadeIn(few_lab, shift=0.1 * DOWN), run_time=0.9)
            beat.wait_until("every friendship", offset=-0.1)
            self.play(FadeIn(q2, scale=0.7, rate_func=window(0, YR, 0.8)), flag(self.flabel, color=INK),
                      run_time=0.8)
            beat.wait_until("tokens average", offset=-0.15)
            self.play(Indicate(q2, color=YELLOW, scale_factor=1.3), run_time=0.9)

        with self.narrate(NARR["fb2"], gap=BREAK) as beat:
            self.add(f_int)
            T = beat.until("five", offset=0.1, min_time=1.3)
            self.play(self.Lf.animate.set_value(635 * fbu),
                      fop.animate(rate_func=window(max(0.0, T - YR), T, T)).set_value(1.0),
                      FadeOut(q2, rate_func=window(0, YR, T)), run_time=T)
            # the friend bar fills: BLUE up to the mean, PURPLE beyond it; (round 7) the axis
            # numbers and name, done with, step back to 30 % now, before anything flies
            self.play(self.Lb.animate.set_value(190 * fbu), self.Po.animate.set_value(1.0),
                      FadeIn(fb_gap, shift=0.1 * UP), flag(g_int, color=BLUE),
                      VGroup(fb_nums, self.ax_title, cap_num, cap_lab).animate(
                          rate_func=window(0.3, 0.8, 0.8)).set_opacity(0.3), run_time=0.8)
            beat.wait_until("spread term", offset=-0.3)
            # Round 7: each number drops out of the bottom of its own bar segment (190 under the
            # BLUE part, 445 under the PURPLE part, 635 under its label) and threads a gap
            # between the dimmed tick labels into the row.  A copy is invisible until its top
            # is 0.3 below the friend bar, so it never crosses a label or doubles its source.
            T = 1.6
            y_vis = yfn - BAR_H * s_ / 2 - 0.3
            y_num = fb_nums[2].get_y()

            def gap_x(i):                  # the middle of the gap between tick labels i, i+1
                return (fb_nums[i].get_right()[0] + fb_nums[i + 1].get_left()[0]) / 2

            y_show = fb_nums.get_bottom()[1] - 0.3

            def drop(src, dst, x_col, t0, t1):
                pts = [src.get_center(), np.array([x_col, y_vis - 0.05, 0]),
                       np.array([x_col, y_num, 0]), np.array([x_col, y_num - 0.45, 0]),
                       np.array([x_col + 0.75 * (dst.get_x() - x_col), y_num - 0.85, 0]),
                       dst.get_center()]
                path = VMobject().set_points_smoothly(pts)
                h0, h1 = src.height, dst.height
                rf = window(t0, t1, T)

                def upd(m, a):
                    b = rf(a)
                    m.scale_to_fit_height((h0 + (h1 - h0) * b) * (1.0 - 0.3 * np.sin(np.pi * b)))
                    m.move_to(path.point_from_proportion(b))
                    # round 8: invisible until its top is 0.3 below the tick labels, so no
                    # copy is ever seen on the axis line (the 635 crossed it at 2:46)
                    vis = float(np.clip((y_show - m.get_top()[1]) / 0.12, 0, 1))
                    m.set_opacity(vis if b > 0 else 0.0)
                return UpdateFromAlphaFunc(src, upd, rate_func=linear)
            g_int.clear_updaters()               # (both read-outs are fixed now)
            f_int.clear_updaters()
            y_bot = yfn - BAR_H * s_ / 2

            def edge_flash(xa, xb, t0, t1):
                ln = Line([xa, y_bot, 0], [xb, y_bot, 0], color=INK, stroke_width=5)
                return ShowPassingFlash(ln, time_width=0.6, rate_func=window(t0, t1, T, linear))
            c190, c445, c635 = (glyphs(g_int).copy(), fb_gap[0][1:].copy(), glyphs(f_int).copy())
            for c in (c190, c445, c635):
                c.set_opacity(0)
            self.add(c190, c445, c635)
            self.play(Indicate(g_int, color=BLUE, scale_factor=1.15, rate_func=window(0, 0.6, T, there_and_back)),
                      edge_flash(x0n, x0n + 190 * fbu, 0.15, 0.75),
                      Indicate(fb_gap, color=PURPLE, scale_factor=1.15, rate_func=window(0.35, 0.95, T, there_and_back)),
                      edge_flash(x0n + 190 * fbu, x0n + 635 * fbu, 0.5, 1.1),
                      Indicate(f_int, color=YELLOW, scale_factor=1.15, rate_func=window(0.7, 1.3, T, there_and_back)),
                      drop(c190, fb_full[4], gap_x(0), 0.0, 0.9),
                      drop(c445, fb_full[6], gap_x(2), 0.35, 1.25),
                      drop(c635, fb_full[8], gap_x(3), 0.7, 1.6),
                      FadeIn(fb_full[3], rate_func=window(0.6, 0.9, T)),
                      FadeIn(fb_full[5], rate_func=window(0.95, 1.25, T)),
                      FadeIn(fb_full[7], rate_func=window(1.3, 1.6, T)), run_time=T)
            self.remove(c190, c445, c635)
            self.add(fb_full[4], fb_full[6], fb_full[8])
            beat.wait_until("twice", offset=-0.1)
            self.play(flag(fb_full[6], color=PURPLE), flag(fb_full[4], color=BLUE),
                      flag(fb_full[2], color=PURPLE), run_time=0.9)
            # round 6: "ninety three percent ... had fewer friends than their friends averaged";
            # the brace, done with, steps back to 30 %
            beat.wait_until("ninety three", offset=-0.2)
            # (opacity, not FadeOut: they belong to fb_tail, which fades as a group later)
            self.play(Write(pct), VGroup(few_br, few_lab, cap_lab).animate.set_opacity(0.0),
                      run_time=0.9)
            beat.wait_until("had fewer", offset=-0.1)
            self.play(FadeIn(pct_l1, shift=0.1 * UP), run_time=0.8)
            # (round 10: "Odds are, that includes you" is cut; the 92.7 % flashes on the
            # comparison it states)
            beat.wait_until("their friends averaged", offset=-0.1)
            self.play(Indicate(pct, color=BLUE, scale_factor=1.15), run_time=0.9)

        # ============================================================ 7. payoff: Harvard 2009
        for m in (self.gbar, self.fblue, self.fpurp, self.fout, g_int, f_int):
            m.clear_updaters()
        ax = axes((0, 125), (0, 8), x_ticks=[0, 30, 60, 90, 120], y_ticks=[0, 2, 4, 6, 8],
                  x_length=9.4, y_length=3.4, x_label="days since 1 September 2009",
                  y_label="diagnosed with flu (% of group)")
        ax.move_to([0.45, -0.03, 0])           # 0.3 shorter, bottom where it was: the read-out
                                               # rows sit clearly above the y title
        for mm in (ax.x_axis.numbers, ax.y_axis.numbers, ax.x_title, ax.y_title):
            mm.set_color(GRAY_T)
        cf_cite = citation("Christakis & Fowler, 2010 · PLoS ONE · Fig. 3 redrawn, logistic refit",
                           color=GRAY_T)
        ay = 2.8                                       # any height works: the fits are a pure shift
        t_fr = LOG_M + LOG_S * np.log(ay / (LOG_C - ay))
        dpu = (ax.c2p(1, 0)[0] - ax.c2p(0, 0)[0])            # units per day
        x_tip = ax.c2p(t_fr, ay)[0]                          # the in-chart lead arrow's tip
        # Round 7: the y title goes on two lines at the top left, so the column above the
        # in-chart lead arrow holds no text and its copy rises straight up into the read-out
        yt = VGroup(Text("diagnosed with flu", font=SERIF, font_size=LABEL, color=GRAY_T),
                    Text("(% of group)", font=SERIF, font_size=LABEL, color=GRAY_T)
                    ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        yt.next_to(ax.y_axis.get_top(), UP, buff=0.22)
        yt.move_to([-4.95 + yt.width / 2, yt.get_y(), 0])
        assert yt.get_right()[0] < x_tip - 0.3, "y title runs into the lead arrow's column"
        for t in yt:
            t.ss_block = "ytitle"
        ax.remove(ax.y_title)
        ax.y_title = yt
        # the axes are drawn first, lines and ticks only (at 30 %, behind the class); the
        # tick numbers and titles are separate so they appear once the class has gone
        ax_text = VGroup(ax.x_axis.numbers, ax.y_axis.numbers, ax.x_title, yt)
        ax.x_axis.remove(ax.x_axis.numbers)
        ax.y_axis.remove(ax.y_axis.numbers)
        ax.remove(ax.x_title)
        ax.set_z_index(-1)
        lab_rand = Text("319 random students", font=SERIF, font_size=28, color=BLUE)
        lab_rand.move_to(ax.c2p(75, 1.0))           # clear of the blue steps and the axis ticks
        # (round 7: two lines, so it too stays left of the arrow's column)
        lab_fr = VGroup(Text("425 friends", font=SERIF, font_size=28, color=YELLOW),
                        Text("they named", font=SERIF, font_size=28, color=YELLOW)
                        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        lab_fr.move_to([ax.c2p(3, 0)[0] + lab_fr.width / 2, ax.c2p(0, 6.0)[1], 0])
        assert lab_fr.get_right()[0] < x_tip - 0.3, "friends' label runs into the arrow's column"
        for t in lab_fr:
            t.ss_block = "lab_fr"
        # Round 7: raw steps keep their full colour at stroke 1.5 once the fits arrive; the
        # dashed fits (stroke 4) are the heavier mark.  YELLOW is never dimmed by opacity.
        # (round 9, substance 6: each fit starts at its group's first case, day 3.5 / 3.8, so
        # no curve claims flu before the data)
        # (round 10, substance 6: from each group's SECOND case, day 7.6 for both, where the fit
        # sits within 0.25 percentage points of its step; at the first case it sat 0.55 above)
        d1_fr, d1_rd = CF["friends"]["steps_day_cases"][2][0], CF["random"]["steps_day_cases"][2][0]
        fit_fr = DashedVMobject(ax.plot(lambda t: logistic(t), x_range=[d1_fr, 125, 0.5]),
                                num_dashes=68).set_stroke(YELLOW, 4)
        fit_rd = DashedVMobject(ax.plot(lambda t: logistic(t, LEAD), x_range=[d1_rd, 125, 0.5]),
                                num_dashes=68).set_stroke(BLUE, 4)
        TIP = 0.16

        def lead_arrow_at(tip, days, color=INK):
            return Arrow(tip + RIGHT * days * dpu, tip, buff=0, color=color, stroke_width=4,
                         max_tip_length_to_length_ratio=min(0.95, TIP / max(days * dpu, 1e-3)),
                         max_stroke_width_to_length_ratio=40)
        lead_arrow = lead_arrow_at(ax.c2p(t_fr, ay), LEAD)
        # Round 7: the read-out sits directly above the arrow it measures (tips aligned at the
        # arrow's x, at the chart's own day scale), its words to the right
        RO_Y1, RO_Y2 = 3.25, 2.72
        ro_tip = np.array([x_tip, RO_Y1, 0.0])
        ro_arrow = lead_arrow_at(ro_tip, LEAD)
        x_ro = x_tip + LEAD * dpu + 0.28                    # left edge of the read-out words
        lead_lab = Text("C&F fitted lead: 13.9 days", font=SERIF, font_size=27, color=INK)
        lead_lab.move_to([x_ro, RO_Y1, 0], aligned_edge=LEFT)
        ro2_tip = np.array([x_tip, RO_Y2, 0.0])
        # round 6: the self-reported read-out is the same kind of measurement as the 13.9-day
        # one, so it is INK too (its arrow at 50 %); GRAY stays the naive guess and the axes
        ro2_long = lead_arrow_at(ro2_tip, LEAD).set_opacity(0.5)
        self_len, sn_op = ValueTracker(LEAD), ValueTracker(0.0)
        ro2_live = always_redraw(lambda: lead_arrow_at(ro2_tip, self_len.get_value()).set_opacity(0.5))
        self_lab = Text("self-reported:", font=SERIF, font_size=27, color=INK)
        self_lab.move_to([x_ro, RO_Y2, 0], aligned_edge=LEFT)
        base_y = self_lab[0].get_bottom()[1]                # the baseline (bottom of the "s")
        num_w = DecimalNumber(LEAD, num_decimal_places=1, font_size=35, color=INK)
        num_w.next_to(self_lab, RIGHT, buff=0.16)           # placed for the widest value, 13.9
        days_lab = Text("days", font=SERIF, font_size=27, color=INK)
        days_lab.next_to(num_w, RIGHT, buff=0.14)
        days_lab.shift(UP * (base_y - days_lab[0].get_bottom()[1]))
        self_num = DecimalNumber(LEAD, num_decimal_places=1, font_size=35, color=INK)

        def upd_sn(m):
            m.set_value(self_len.get_value())
            m.next_to(days_lab, LEFT, buff=0.14)
            m.shift(UP * (base_y - m.get_bottom()[1]))
            prog = float(np.clip((LEAD - self_len.get_value()) / (LEAD - SELF_LEAD), 0, 1))
            m.set_opacity(sn_op.get_value() * (0.1 + 0.9 * prog ** 2))   # solid only at 3.2
        upd_sn(self_num)
        cal = ValueTracker(0.0)
        rd_live = always_redraw(lambda: stepped_upto(ax, CF["random"]["steps_day_cases"], 319,
                                                     cal.get_value()).set_stroke(BLUE, 5))
        fr_live = always_redraw(lambda: stepped_upto(ax, CF["friends"]["steps_day_cases"], 425,
                                                     cal.get_value()).set_stroke(YELLOW, 5))
        origin = ax.c2p(0, 0)
        origin_b = Dot(origin, radius=0.09, color=BLUE)
        origin_y = Dot(origin, radius=0.05, color=YELLOW)
        for dd in (origin_b, origin_y):
            self.allow_overlap(dd, reason="transient: the random students and the named friends "
                                          "merge into their curves' shared origin, just above the "
                                          "x-axis '0', and the dots fade as the curves grow")
        fade_out = VGroup(*fb_full[0:8], self.ax_line, fb_ticks, fb_nums, self.ax_title, fb_gap, fb_tail,
                          fb_glabel, self.flabel, g_int, pct_blk, self.fblue, self.fpurp)
        fade_out_y = VGroup(fb_full[8], f_int, self.fout)          # (round 8: YELLOW, <= 0.2 s)
        # Round 7: C&F's design on the episode's own machine.  The class returns; four girls are
        # the random sample (BLUE rings, "random students"); only they name friends, one token
        # per friend, and the girls they name are the friend sample (YELLOW rings, "named
        # friends").  Their tokens read 4, 4, 4, 4, 3, 2, 2.
        Pc = {n: P[n] + CF_SHIFT for n in NAMES}
        circ3, num3, name3, edges3 = self.build_network()
        node_fill = interpolate_color(ManimColor(BG), ManimColor(BLUE), 0.16)
        for n in NAMES:                       # opaque, so the faint axes can pass behind
            circ3[n].set_fill(node_fill, opacity=1.0)
        net3 = VGroup(*edges3.values(), *circ3.values(), *num3.values(), *name3.values())
        net3.shift(CF_SHIFT)
        leg_r, leg_n, leg_f = cf_legend()
        cf_toks = []
        for snd, rcv in CF_DRAW:
            d = net_token(K[rcv]).move_to(tok_start(snd, rcv, Pc))
            d[1].ss_host = d[0]
            d[0].set_fill(opacity=0)
            d[1].set_opacity(0)
            cf_toks.append((snd, rcv, d, tok_start(snd, rcv, Pc), cf_tok_end(snd, rcv, Pc)))
        pile = VGroup(*[t[2] for t in cf_toks])
        # round 8: the named friends' YELLOW rings are drawn over their BLUE outlines at full
        # colour (recolouring a stroke BLUE -> YELLOW passes through khaki)
        ring3y = {n: Circle(radius=R, color=YELLOW, stroke_width=CF_RING_W).move_to(Pc[n]) for n in CF_NAMED}
        for c_ in ring3y.values():
            c_.ss_bg = True
        node3 = {n: VGroup(circ3[n], *([ring3y[n]] if n in ring3y else []), num3[n]) for n in NAMES}
        # round 8 hand-off: the class first contracts to 0.55 inside the coming plot area, every
        # node above the x-axis, then the two samples fly to the curves' origin one after the other
        CF_Q = {n: np.array([-0.6, 0.35, 0.0]) + 0.55 * (Pc[n] - np.array([-0.6, 0.1, 0.0])) for n in NAMES}
        # where the two legend entries go: the BLUE one becomes "319 random students", the
        # YELLOW one sits at the friends' label spot until the group size is spoken
        leg_r_to = leg_r.copy().move_to(lab_rand[3:].get_center())
        leg_f_to = leg_f.copy().move_to([lab_fr.get_left()[0] + leg_f.width / 2, lab_fr.get_y(), 0])

        def wave(pairs):
            """Flashes along friendships, each run outward from the first girl of the pair."""
            return [ShowPassingFlash(Line(Pc[a] + unit(Pc[b] - Pc[a]) * R, Pc[b] - unit(Pc[b] - Pc[a]) * R,
                                          color=INK, stroke_width=6), time_width=0.7) for a, b in pairs]
        hop1 = [("Sue", "Betty"), ("Sue", "Dale"), ("Sue", "Pam"), ("Alice", "Jane"),
                ("Alice", "Pam"), ("Alice", "Dale")]
        hop2 = [("Pam", "Carol")]
        hop3 = [("Carol", "Tina")]
        # Round 9 (craft 4): no empty frame between Facebook and Harvard.  The BLUE "average
        # user" bar (a person counted once) splits into eight pieces that become the class's
        # eight BLUE nodes, while the YELLOW 635s and outline shrink away at full colour; the
        # friendships, counts and names then come in around the nodes.
        node_order = sorted(NAMES, key=lambda n: (Pc[n][0], -Pc[n][1]))
        gb_l, gb_w = self.gbar.get_left()[0], self.gbar.width
        pieces = {}
        for i, n in enumerate(node_order):
            pieces[n] = Rectangle(width=gb_w / 8 + 0.012, height=self.gbar.height, stroke_width=0,
                                  fill_color=BLUE, fill_opacity=0.9).move_to(
                [gb_l + gb_w * (i + 0.5) / 8, self.gbar.get_y(), 0])
        for e in edges3.values():
            e.set_stroke(opacity=0.0)
        with self.narrate(NARR["cf"], gap=0.3) as beat:
            T = 1.5
            self.remove(self.gbar)
            self.add(*edges3.values(), *pieces.values())
            self.play(FadeOut(fade_out, rate_func=window(0, 0.5, T)),
                      *[shrink_out(m, rate_func=window(0, 0.4, T)) for m in fade_out_y],
                      FadeOut(ugander, rate_func=window(0, 0.35, T)),
                      FadeIn(cf_cite, rate_func=window(0.45, 1.0, T)),
                      *[ReplacementTransform(pieces[n], circ3[n],
                                             rate_func=window(0.1 + 0.04 * i, 1.0 + 0.04 * i, T))
                        for i, n in enumerate(node_order)],
                      *[e.animate(rate_func=window(0.75, 1.5, T)).set_stroke(opacity=1.0)
                        for e in edges3.values()],
                      FadeIn(VGroup(*num3.values()), rate_func=window(0.95, 1.5, T)),
                      FadeIn(VGroup(*name3.values()), rate_func=window(0.95, 1.5, T)), run_time=T)
            self.remove(*fade_out_y)
            # "put this to work": the random sample, four girls ringed BLUE (as Jane at 0:19)
            beat.wait_until("work", offset=-0.25)
            # (round 7: staggered windows, not a LaggedStart: an AnimationGroup adds its group on
            # top of the scene, and the opaque nodes would then cover their own digits)
            self.play(*[circ3[n].animate(rate_func=window(0.15 * i, 0.15 * i + 0.6, 1.2))
                        .set_stroke(BLUE, width=CF_RING_W) for i, n in enumerate(CF_RANDOM)],
                      FadeIn(leg_r, shift=0.1 * LEFT, rate_func=window(0.2, 0.8, 1.2)),
                      FadeIn(leg_n, shift=0.1 * LEFT, rate_func=window(0.5, 1.1, 1.2)), run_time=1.2)
            # "Named friends": only the random students send tokens, one per friend; whoever
            # they name is ringed YELLOW, as Alice was at 0:19
            beat.wait_until("Named", offset=-0.3)
            self.add(pile)
            T = beat.until("more friends", offset=-0.05, min_time=1.3)
            self.play(self.fly_tokens(cf_toks, T, ValueTracker(0), ValueTracker(0), K, lag=0.06),
                      *[Create(ring3y[n], rate_func=window(0.7 * T, T, T)) for n in CF_NAMED],
                      y_in(leg_f, 0.75 * T, T, shift=0.1 * LEFT), run_time=T)
            # "more friends": the named friends' tokens read 4, 4, 4, 4, 3, 2, 2
            beat.wait_until("more friends", offset=-0.05)
            self.play(*[pulse(t[2], 1.3) for t in cf_toks],
                      *[Indicate(num3[n], color=INK, scale_factor=1.3) for n in CF_NAMED],
                      run_time=0.8)
            # "closer to everyone else": one step from Sue and Alice reaches four more girls
            beat.wait_until("closer", offset=-0.25)
            self.play(LaggedStart(AnimationGroup(*wave(hop1)), AnimationGroup(*wave(hop2)),
                                  AnimationGroup(*wave(hop3)), lag_ratio=0.55), run_time=1.5)
            # Round 8 hand-off (substance 2), "and should catch flu first", in four short moves
            # so the two samples never tangle: (a) the tokens merge into the girls they named
            # and the friendships, names and caption leave; (b) the class contracts to 0.55,
            # every node above where the x-axis will run; (c) the axes draw and the named
            # friends fly, one after another, into the YELLOW origin; (d) the random students
            # into the BLUE one.  Each path stays 0.25 above the axis until its last 0.15 s.
            beat.wait_until("and should", offset=-0.1)
            T = 0.35
            self.play(*[shrink_out(t[2], rate_func=window(0, T, T), to=Pc[t[1]])
                        for t in cf_toks],
                      FadeOut(VGroup(*edges3.values(), *name3.values(), leg_n), rate_func=window(0, T, T)),
                      run_time=T)
            self.remove(pile)
            T = 0.5
            tg = {}
            for n in NAMES:                        # (rings and outlines thin with the nodes)
                tg[n] = node3[n].copy().scale(0.55).move_to(CF_Q[n])
                tg[n][-1].scale(0.75 / 0.55)       # (its digit stays at 27 px, above the floor)
                tg[n][0].set_stroke(width=5 if n in CF_RANDOM else 2.5)
                if n in ring3y:
                    tg[n][1].set_stroke(width=5)
            self.play(*[Transform(node3[n], tg[n]) for n in NAMES], run_time=T)

            def bez(p0, p1, p2, p3, b):
                return (1 - b) ** 3 * p0 + 3 * b * (1 - b) ** 2 * p1 + 3 * b ** 2 * (1 - b) * p2 + b ** 3 * p3

            # (round 9: Carol's arc stays low, so it passes 0.15 under Pam, not 0.05)
            ARC_LIFT = {"Carol": 0.0}

            def into_origin(n, t0, travel, total):
                grp = node3[n]
                start = grp.copy()
                fam0 = start.family_members_with_points()
                widths = [m.get_stroke_width() for m in fam0]
                ops = [(m.get_fill_opacity(), m.get_stroke_opacity()) for m in fam0]
                s0 = CF_Q[n]
                c1 = np.array([s0[0] - 0.45 * (s0[0] - origin[0]),
                               max(s0[1], origin[1] + 0.9) + ARC_LIFT.get(n, 0.35), 0.0])
                c2 = np.array([origin[0] + 0.25, origin[1] + 0.9, 0.0])

                def upd(m, a):
                    tt = a * total
                    u = float(np.clip((tt - t0) / travel, 0, 1))
                    b = smooth(u)
                    k = 1.0 - 0.85 * b
                    m.become(start.copy().scale(k).move_to(bez(s0, c1, c2, origin, b)))
                    q = 1.0 - float(np.clip((tt - t0 - travel + 0.12) / 0.12, 0, 1))
                    for sm, w, (fo, so) in zip(m.family_members_with_points(), widths, ops):
                        sm.set_stroke(width=w * k, opacity=so * q)   # (each part keeps its own
                        sm.set_fill(opacity=fo * q)                  # opacity: a ring stays a ring)
                # (round 9: real seconds; each node eases on its own, so the default smooth on
                # top stalled the hand-off for ~0.5 s between the two passes)
                return UpdateFromAlphaFunc(grp, upd, rate_func=linear)
            # Round 9: the random students (Betty, Dale, Carol) go first, into the BLUE origin,
            # then the named friends into the YELLOW one (the order the narration names them);
            # simulated: no two moving or waiting rings come closer than 0.146 edge to edge.
            LAG, trav = 0.09, 0.5                  # 0.5 s per node
            TP = 0.15 + 2 * LAG + trav
            ax.set_stroke(opacity=0.3)
            self.play(timed(Create(ax), 0.0, 0.45, TP),
                      GrowFromCenter(origin_b, rate_func=window(0, 0.25, TP)),
                      GrowFromCenter(origin_y, rate_func=window(0, 0.25, TP)),
                      *[into_origin(n, 0.15 + LAG * i, trav, TP)
                        for i, n in enumerate(("Betty", "Dale", "Carol"))],
                      run_time=TP)
            self.add(origin_b, origin_y)
            # ... and as the named friends follow, the two legend entries move to the curves
            # they will name, each only once the girls in its way have left (the YELLOW one
            # first, so the two never cross); the axis numbers and titles come in
            TG = 1.2
            self.play(*[into_origin(n, LAG * i, trav, TG)
                        for i, n in enumerate(("Sue", "Alice", "Jane", "Pam", "Tina"))],
                      ax.animate(rate_func=window(0, 0.6, TG)).set_stroke(opacity=1.0),
                      glide(leg_f, [leg_f.get_center(), [leg_f.get_x() - 2.0, leg_f_to.get_y() + 0.2, 0],
                                    leg_f_to.get_center()],
                            ease=lambda t: smooth(float(np.clip((t * TG - 0.55) / 0.6, 0, 1)))),
                      glide(leg_r, [leg_r.get_center(), leg_r_to.get_center()],
                            ease=lambda t: smooth(float(np.clip((t * TG - 0.62) / 0.55, 0, 1)))),
                      FadeIn(ax_text, rate_func=window(0.7, TG, TG)), run_time=TG)
            self.remove(*node3.values(), *circ3.values(), *num3.values(), *ring3y.values())
            self.add(rd_live, fr_live, origin_b, origin_y)
            # the calendar runs linearly from here to "rose first"; the labels gain their group
            # sizes as the groups are named
            t0 = beat.elapsed()
            t_end = beat.time_of("rose first") - 0.1
            TC = max(4.0, t_end - t0)
            a_u = float(np.clip(beat.time_of("random students") - 0.15 - t0, 0.0, TC - 0.8))
            a_f = float(np.clip(beat.time_of("friends the students") - 0.15 - t0, 0.0, TC - 0.9))
            self.play(cal.animate(rate_func=linear).set_value(125),
                      FadeOut(origin_b, rate_func=window(0.3, 0.9, TC)), y_out(origin_y, 0.3, TC),
                      RT_same(leg_r, lab_rand[3:], rate_func=window(a_u, a_u + 0.05, TC)),
                      FadeIn(lab_rand[:3], shift=0.1 * RIGHT, rate_func=window(a_u, a_u + 0.7, TC)),
                      y_out(leg_f, a_f, TC, shift=0.12 * UP),
                      y_in(lab_fr, a_f + 0.3, TC, shift=0.12 * UP),
                      run_time=TC)
            rd_live.clear_updaters()
            fr_live.clear_updaters()
            self.play(ShowPassingFlash(fr_live.copy().set_stroke(INK, 8), time_width=0.35),
                      run_time=1.2)
            beat.wait_until("fitted", offset=-0.15)
            self.play(rd_live.animate.set_stroke(width=1.5), fr_live.animate.set_stroke(width=1.5),
                      Create(fit_fr), Create(fit_rd), run_time=1.2)
            beat.wait_until("thirteen", offset=-0.3)
            self.play(GrowArrow(lead_arrow), run_time=0.8)
            # (round 7: the copy rises straight up into the read-out above it)
            self.play(TransformFromCopy(lead_arrow, ro_arrow),
                      FadeIn(lead_lab, shift=0.1 * LEFT, rate_func=window(0.55, 1.0, 1.0)), run_time=1.0)
            beat.wait_until("self-reported", offset=-0.15)
            # (round 6c: the copy starts transparent, so it never doubles the 13.9 arrow)
            self.play(ReplacementTransform(ro_arrow.copy().set_opacity(0), ro2_long, rate_func=leave),
                      FadeIn(self_lab, shift=0.1 * LEFT),
                      run_time=0.8)
            self.remove(ro2_long)
            self.add(ro2_live)
            # (round 9: the shrink starts on "lead", so the settled "3.2 days" is read ~0.4 s
            # longer before the chart gives way to the landing)
            beat.wait_until("lead", offset=-0.15)
            self.add(self_num)
            self_num.add_updater(upd_sn)
            self.play(sn_op.animate(rate_func=window(0, 0.2, 1.0)).set_value(1.0),
                      FadeIn(days_lab, rate_func=window(0.45, 1.0, 1.0)),
                      self_len.animate.set_value(SELF_LEAD), run_time=1.0)
            ro2_live.clear_updaters()
            self_num.clear_updaters()

        # ============================================================ 8. landing
        # Second cycle: back to the cold-open frame itself (network, girl bar, "average
        # friend ?" with the candidates 2.5 / 3 / 4); the last line answers the question and
        # the friend bar grows to the 3, which is ringed.
        circ2, num2, name2, edges2 = self.build_network()
        glabel2 = Text("average girl", font=SERIF, font_size=28, color=INK)
        glabel2.move_to([X0, Y_GIRL + 0.55, 0], aligned_edge=LEFT)
        flabel2 = Text("average friend", font=SERIF, font_size=28, color=INK)
        flabel2.move_to([X0, Y_FRIEND + 0.6, 0], aligned_edge=LEFT)
        end_g = Rectangle(width=2.5 * UNIT, height=BAR_H, stroke_width=0, fill_color=BLUE,
                          fill_opacity=0.9).move_to([X0 + 1.25 * UNIT, Y_GIRL, 0])
        end_g.ss_bg = True
        end_gn = MathTex("2.5", font_size=40, color=BLUE).next_to(end_g, RIGHT, buff=0.2)
        end_fb = Rectangle(width=2.5 * UNIT, height=BAR_H, stroke_width=0, fill_color=BLUE,
                           fill_opacity=0.9).move_to([X0 + 1.25 * UNIT, Y_FRIEND, 0])
        end_fp = Rectangle(width=0.5 * UNIT, height=BAR_H, stroke_width=0, fill_color=PURPLE,
                           fill_opacity=0.9).move_to([X0 + 2.75 * UNIT, Y_FRIEND, 0])
        end_fo = Rectangle(width=3.0 * UNIT, height=BAR_H, stroke_color=YELLOW, stroke_width=4,
                           fill_opacity=0).move_to([X0 + 1.5 * UNIT, Y_FRIEND, 0])
        for m in (end_fb, end_fp):
            m.ss_bg = True
        q3 = MathTex("?", font_size=46, color=YELLOW).move_to([X0 + 0.3, Y_FRIEND, 0])
        ref2 = DashedLine([X0 + 2.5 * UNIT, top_y, 0], [X0 + 2.5 * UNIT, Y_FRIEND + 0.3, 0],
                          color=GRAY, stroke_width=2.5, dash_length=0.08)
        ghosts2 = VGroup(*[DashedLine([X0 + v * UNIT, top_y - 0.12, 0], [X0 + v * UNIT, Y_FRIEND + 0.3, 0],
                                      color=GRAY, stroke_width=2.5, dash_length=0.08).set_opacity(0.6)
                           for v in (3, 4)])
        cands2 = VGroup(*[MathTex(t, font_size=40, color=YELLOW).move_to([X0 + v * UNIT, Y_FRIEND, 0])
                          for t, v in (("2.5", 2.5), ("3", 3), ("4", 4))])
        ax_line2 = Line([X0, Y_AX, 0], [X0 + 4 * UNIT, Y_AX, 0], color=GRAY, stroke_width=2.5)
        ax_ticks2 = VGroup(*[Line([X0 + v * UNIT, Y_AX - 0.07, 0], [X0 + v * UNIT, Y_AX + 0.07, 0],
                                  color=GRAY, stroke_width=2.5) for v in range(5)])
        for t in ax_ticks2:
            t.ss_bg = True
        ax_nums2 = VGroup(*[MathTex(str(v), font_size=30, color=GRAY_T).next_to(
            [X0 + v * UNIT, Y_AX, 0], DOWN, buff=0.16) for v in range(5)])
        ax_title2 = Text("friends (count)", font=SERIF, font_size=26, color=GRAY_T)
        ax_title2.next_to(ax_nums2, DOWN, buff=0.14).align_to(ax_line2, RIGHT)
        panel2 = VGroup(glabel2, end_g, end_gn, flabel2, q3, ref2, ghosts2, cands2, ax_line2,
                        ax_ticks2, ax_nums2, ax_title2)
        three_to = [X0 + 3.0 * UNIT + 0.45, Y_FRIEND, 0]
        ring3 = Circle(radius=0.35, color=INK, stroke_width=3).move_to(three_to)
        ring3.ss_bg = True
        # Round 6b: the landing is one move.  Betty follows her one friendship: her token lands
        # on Sue and reads 4, as every token reads the count where it lands (the 4 candidate);
        # the girl bar is the 2.5; the friend bar grows to the 3.
        be = edges2[frozenset(("Betty", "Sue"))]
        tok_b = net_token(K["Sue"]).move_to(tok_start("Betty", "Sue", P))
        tok_b[1].ss_host = tok_b[0]
        tok_b[0].set_fill(opacity=0)
        tok_b[1].set_opacity(0)
        tok_b_fl = [("Betty", "Sue", tok_b, tok_start("Betty", "Sue", P), tok_end("Betty", "Sue", P))]
        # Round 10 (craft 2): the 3:07 hand-off played in reverse, so the episode never dips
        # through a near-empty frame.  (a) The four curves and the two group labels contract
        # into the chart's origin at full colour while the read-outs, axes and C&F's citation
        # leave; (b) the eight girls fly back out of the origin to their places in the class,
        # in their C&F colours (BLUE rings for the random three, YELLOW rings for the five
        # named friends); every node grows with its distance from the origin, so the class
        # stays one homothetic picture and no two nodes meet; (c) the rings relax to the
        # class's BLUE, the friendships draw on and the cold-open panel grows from its axis.
        org = ax.c2p(0, 0)
        yring = {n: Circle(radius=R, color=YELLOW, stroke_width=CF_RING_W).move_to(P[n]) for n in CF_NAMED}
        for c_ in yring.values():
            c_.ss_bg = True
        for n in CF_RANDOM:
            circ2[n].set_stroke(width=CF_RING_W)
        node_l = {n: VGroup(circ2[n], *([yring[n]] if n in yring else []), num2[n]) for n in NAMES}
        out_order = sorted(NAMES, key=lambda n: np.linalg.norm(P[n] - org))

        def fly_out(n, t0, trav, total, relax=(1.2, 1.5)):
            """Node n flies out of the origin, growing; then (relax) its C&F ring relaxes: a
            YELLOW ring thins to nothing at full colour, a BLUE ring back to the class's 3.5."""
            grp = node_l[n]
            start = grp.copy()
            widths = [m.get_stroke_width() for m in start.family_members_with_points()]

            def upd(m, a):
                tt = a * total
                u = float(np.clip((tt - t0) / trav, 0, 1))
                b = smooth(u)
                k = 0.3 + 0.7 * b
                m.become(start.copy().scale(k).move_to(org + (P[n] - org) * b))
                for sm, w in zip(m.family_members_with_points(), widths):
                    sm.set_stroke(width=w * k)
                r = smooth(float(np.clip((tt - relax[0]) / (relax[1] - relax[0]), 0, 1)))
                if n in yring:
                    yring[n].set_stroke(width=CF_RING_W * k * (1.0 - r))
                if n in CF_RANDOM:
                    circ2[n].set_stroke(width=(CF_RING_W * (1.0 - r) + 3.5 * r) * k)
                if u <= 0.0:
                    m.set_opacity(0.0)
            return UpdateFromAlphaFunc(grp, upd, rate_func=linear)
        curves = [fr_live, rd_live, fit_fr, fit_rd, lab_fr, lab_rand]
        readouts = VGroup(lead_arrow, ro_arrow, lead_lab, ro2_live, self_lab, self_num, days_lab)
        # one 1.7 s move (round 10: inside the 2.5 s silence limit), so no frame is near-empty: the axes stay until the girls are out, and
        # the friendships and the panel come in while the girls are still landing
        TL = 1.7
        f = TL / 1.85                        # (times laid out for 1.85 s, scaled)
        panel2_rest = VGroup(glabel2, flabel2, end_gn, ax_nums2, ax_title2)
        self.play(*[shrink_out(m, rate_func=window(0.0*f, 0.65*f, TL), to=org) for m in curves],
                  FadeOut(readouts, rate_func=window(0.1*f, 0.5*f, TL)),
                  FadeOut(VGroup(ax, ax_text), rate_func=window(0.5*f, 1.05*f, TL)),
                  FadeOut(cf_cite, rate_func=window(0.0*f, 0.35*f, TL)),
                  FadeIn(feld, rate_func=window(0.5*f, 1.0*f, TL)),
                  *[fly_out(n, (0.2 + 0.04 * i) * f, 0.8 * f, TL, relax=(1.2 * f, 1.5 * f)) for i, n in enumerate(out_order)],
                  *[Create(e, rate_func=window(1.0*f, 1.6*f, TL)) for e in edges2.values()],
                  *[FadeIn(name2[n], rate_func=window(1.05*f, 1.5*f, TL)) for n in NAMES],
                  Create(ax_line2, rate_func=window(0.85*f, 1.2*f, TL)),
                  *[Create(t, rate_func=window(0.95*f, 1.25*f, TL)) for t in ax_ticks2],
                  GrowFromEdge(end_g, LEFT, rate_func=window(1.0*f, 1.55*f, TL)),
                  FadeIn(panel2_rest, rate_func=window(1.05*f, 1.55*f, TL)),
                  Create(ref2, rate_func=window(1.2*f, 1.7*f, TL)),
                  *[Create(g, rate_func=window(1.2*f, 1.7*f, TL)) for g in ghosts2],
                  *[GrowFromCenter(c, rate_func=window(1.35*f, 1.85*f, TL)) for c in (q3, *cands2)],
                  run_time=TL)
        self.remove(*curves, readouts, ax, ax_text)
        self.remove(*yring.values())
        for n in NAMES:                          # (each node back as one circle + its count)
            self.remove(node_l[n])
            self.add(circ2[n], num2[n])
        with self.narrate(NARR["land"]) as beat:
            # Betty looks at her one friend ...
            beat.wait_until("one friend", offset=-0.2)
            self.play(circ2["Betty"].animate.set_stroke(INK, width=6), be.animate.set_stroke(INK, width=5),
                      run_time=0.6)
            # ... Sue: Betty's token travels their friendship, lands on Sue and reads four,
            # the 4 candidate
            beat.wait_until("Sue", offset=-0.25)
            self.add(tok_b)
            self.play(self.fly_tokens(tok_b_fl, beat.until("four", offset=-0.05, min_time=0.9),
                                      ValueTracker(0), ValueTracker(0), K))
            self.play(pulse(tok_b, 1.3), Indicate(num2["Sue"], color=INK, scale_factor=1.3),
                      Indicate(cands2[2], color=YELLOW, scale_factor=1.3), run_time=0.6)
            # Round 8 (craft 1): the resolution plays in the 2.1 s silence after "sees four", in
            # three separate moves, and the last line is left to Betty alone.
            # (a) 2.5 counts the girls: its drop line goes and the 2.5 candidate rises into the
            # girl bar's 2.5, which flashes with the bar
            T = 0.65
            c25 = cands2[0]
            p25 = [c25.get_center(), np.array([c25.get_x(), Y_GIRL - 0.55, 0]),
                   end_gn.get_center() + np.array([-0.15, -0.2, 0]), end_gn.get_center()]
            path25 = VMobject().set_points_smoothly(p25)

            def rise25(m, a):
                b = smooth(float(np.clip(a * T / 0.55, 0, 1)))
                m.move_to(path25.point_from_proportion(b))
                m.set_opacity(1.0 - float(np.clip((a * T - 0.4) / 0.15, 0, 1)))
            self.play(FadeOut(ref2, rate_func=window(0, 0.25, T)), UpdateFromAlphaFunc(c25, rise25),
                      ShowPassingFlash(SurroundingRectangle(end_g, buff=0.03, color=INK, stroke_width=4),
                                       time_width=0.5, rate_func=window(0.3, T, T, linear)),
                      Indicate(end_gn, color=BLUE, scale_factor=1.25, rate_func=window(0.4, T, T, there_and_back)),
                      run_time=T)
            self.remove(c25)
            # (b) 3 counts the tokens: every friendship flashes, the "?" and the drop lines go,
            # and the friend bar grows to 3 at one smooth rate (YELLOW outline, BLUE to 2.5,
            # PURPLE beyond); the 3 candidate steps aside to the bar's end
            T = max(1.0, beat.until("Most", offset=-0.45))
            for m in (end_fb, end_fp, end_fo):
                m.save_state()
            t_g0, t_g1 = 0.15, T

            def grow(_, a):
                u = float(np.clip((a * T - t_g0) / (t_g1 - t_g0), 0, 1))
                w = 3.0 * UNIT * smooth(u)
                wb, wp = min(w, 2.5 * UNIT), max(0.0, w - 2.5 * UNIT)
                for m, x0, wi in ((end_fb, X0, wb), (end_fp, X0 + 2.5 * UNIT, wp), (end_fo, X0, w)):
                    m.restore()
                    m.stretch_to_fit_width(max(wi, 1e-3)).move_to([x0 + max(wi, 1e-3) / 2, Y_FRIEND, 0])
                    if m is end_fo:
                        m.set_stroke(opacity=1.0 if wi > 0.02 else 0.0)
                    else:
                        m.set_fill(opacity=0.9 if wi > 0.02 else 0.0)
            grow(None, 0.0)
            self.add(end_fb, end_fp, end_fo)
            self.play(LaggedStart(*[ShowPassingFlash(e.copy().set_stroke(YELLOW, 7), time_width=0.6)
                                    for e in edges2.values()], lag_ratio=0.05,
                                  rate_func=window(0, 0.6, T, linear)),
                      shrink_out(q3, rate_func=window(0, 0.3, T)),
                      FadeOut(ghosts2, rate_func=window(0, 0.3, T)),
                      UpdateFromAlphaFunc(VGroup(end_fb, end_fp, end_fo), grow),
                      cands2[1].animate(rate_func=window(0.4 * T, 0.8 * T, T)).move_to(three_to),
                      run_time=T)
            self.remove(q3)
            # (c) the 3 is ringed while the 4, what Betty sees, leaves
            self.play(Create(ring3), shrink_out(cands2[2]), run_time=0.45)
            self.remove(cands2[2])
            # "Most of us are Betty": only Betty, and the token that shows her view
            beat.wait_until("Betty", occurrence=2, offset=-0.2)
            self.play(Indicate(circ2["Betty"], color=INK, scale_factor=1.25), pulse(tok_b, 1.3),
                      run_time=0.7)
            self.hold(max(0.0, beat.remaining()))
        self.hold(0.15)                          # the answered frame holds before the card
        # Round 8 (craft 4): the whole scene fades out first (YELLOW within 0.2 s), and only
        # then does the series card come in, so no frame holds both; trailing silence ~1.9 s
        T = 0.35
        ys = (end_fo, cands2[1], tok_b)
        self.remove(*ys)                         # (top level, so no group holds them twice)
        self.add(*ys)
        rest = [m for m in self.mobjects if all(m is not y for y in ys)]
        self.play(FadeOut(VGroup(end_fo, cands2[1], tok_b), rate_func=window(0, YR, T)),
                  FadeOut(Group(*rest), rate_func=window(0, T, T)), run_time=T)
        card = _ssstyle.end_card(self.EPISODE, self.TITLE)
        self.play(FadeIn(card, shift=0.1 * UP), run_time=0.35)
        # round 9 (craft 8): the finished card holds 0.4 s (it was still fading on the last
        # frames); trailing silence ~1.8 s (BAR <= 2 s)
        self.hold(0.4)


if __name__ == "__main__":
    assert_token_clearance()
    print("token layout: ok")
