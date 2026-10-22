"""Episode 75 - Mild Preferences, Segregated Towns (Schelling's model).

    videos/toolkit/render.sh --preview videos/episodes/075-schelling-segregation/scene.py Episode /tmp/ep75.mp4
    videos/toolkit/render.sh videos/episodes/075-schelling-segregation/scene.py Episode \
        videos/episodes/075-schelling-segregation/final.mp4

Every town on screen is simulated by sim.py (same directory, seeded, deterministic).
"""
from __future__ import annotations

import bisect
import json
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np
from manim import *
from manim.utils.paths import path_along_arc
from sample_space import *
from sample_space import style as ss_style

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import sim  # noqa: E402

# ----------------------------------------------------------------------------- geometry
N = sim.N
P = 0.145                 # board pitch (units per square)
TILE = 0.115              # tile side
GX, GY = -3.2, 0.3        # board centre (working position)
UNH_W = 2.8               # unhappy ring: stroke 2.8 -> a 0.028-unit (3.8 px) ring OUTSIDE the tile
COL = {1: BLUE, 2: YELLOW}

TL, TR = 1.3, 5.3         # meter track left / right
TY0, TY1 = 0.55, 2.55     # meter height: centred (open / landing) and docked (working)
TH = 0.30                 # meter track height
HUD_Y = 0.45              # HUD first row (rows step 0.64-0.72 down: beside the board's middle)

MAG_P, MAG_T = 1.0, 0.83           # insight magnifier pitch and tile (5 x 1.0 u = 675 px wide)
MAG_UNH = 6.0                      # its unhappy ring width
PATCH_R = (2, 5)                   # rows 2..5
PATCH_C = (11, 15)                 # cols 11..15
MAG_C = np.array([-1.72 + 5 * MAG_P / 2 + 0.03, -0.83, 0])
RS = 0.7                           # board scale during the replay (board parked at the left edge)
RC = (-6.3 + (N * P + 0.07) * RS / 2, -0.55)   # board centre during the replay
A_, B_, C_, D_ = (4, 15), (4, 14), (3, 13), (3, 12)   # the domino chain (seed 3)
EX = (15, 15)                      # gold household with 2 gold of 6 neighbours (final town)
PREVIEW_MOVE = 34                  # round-1 move (23,18) -> (21,34), shown as the plan preview
RULE_P, RULE_T = 0.6, 0.5          # rule magnifier pitch and tile
RULE_C = np.array([1.85, -1.95, 0])     # (x 2.3 -> 1.85: "empty: not counted" at Text 27)


def cell(r, c, centre=(GX, GY), s=1.0):
    p = P * s
    x0 = centre[0] - (N - 1) / 2 * p
    y0 = centre[1] + (N - 1) / 2 * p
    return np.array([x0 + c * p, y0 - r * p, 0.0])


def mx(share):
    return TL + share * (TR - TL)


def mag_cell(r, c):
    nr = PATCH_R[1] - PATCH_R[0] + 1
    nc = PATCH_C[1] - PATCH_C[0] + 1
    x0 = MAG_C[0] - (nc - 1) / 2 * MAG_P
    y0 = MAG_C[1] + (nr - 1) / 2 * MAG_P
    return np.array([x0 + (c - PATCH_C[0]) * MAG_P, y0 - (r - PATCH_R[0]) * MAG_P, 0.0])


def set_unhappy(tile, flag, width=UNH_W, base=TILE, color=RED):
    """Unhappy = a red ring drawn OUTSIDE the tile; the household colour stays at full
    strength.  The square grows by the stroke width so the stroke's inner edge sits exactly
    on the tile's edge (Manim strokes are centred on the path; width w = 0.01 w units)."""
    if flag:
        tile.set_stroke(color, width=width, opacity=1.0)
        tile.set_width(base + width * 0.01)
    else:
        tile.set_stroke(color, width=0, opacity=0.0)
        tile.set_width(base)
    tile.ss_unhappy = flag


def nb8(rc):
    return [(rc[0] + dr, rc[1] + dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0)]


def cross(m, size, color=GRAY, width=3):
    """A thin grey x inside square slot m (an empty square: not counted)."""
    h = size / 2
    c = m.get_center()
    return VGroup(Line(c + np.array([-h, -h, 0]), c + np.array([h, h, 0])),
                  Line(c + np.array([-h, h, 0]), c + np.array([h, -h, 0]))).set_stroke(color, width)


class Episode(NarratedScene):
    EPISODE = 75
    TITLE = "Mild Preferences, Segregated Towns"
    SPEED = 0.84
    CADENCE = "shaped"                   # gaps follow the sense (PRODUCTION_GUIDE §13.3)

    # ------------------------------------------------------------------ data
    def prep(self):
        st, rounds = sim.run(sim.SEED, 1 / 3)
        self.states, self.rounds = st, rounds
        g0, ids0 = st[0]
        gF, idsF = st[-1]
        self.g0, self.gF = g0, gF
        self.colour = {int(ids0[r, c]): int(g0[r, c]) for r, c in np.argwhere(g0 > 0)}
        self.start_pos = {int(ids0[r, c]): (int(r), int(c)) for r, c in np.argwhere(g0 > 0)}
        self.final_pos = {int(idsF[r, c]): (int(r), int(c)) for r, c in np.argwhere(gF > 0)}
        self.share0 = sim.avg_share(g0)
        self.shareF = sim.avg_share(gF)
        self.unh0 = {int(ids0[r, c]) for r, c in np.argwhere(sim.unhappy_mask(g0, 1 / 3))}
        self.id_at0 = {v: k for k, v in self.start_pos.items()}
        self.id_atF = {v: k for k, v in self.final_pos.items()}
        g, idg = g0.copy(), ids0.copy()
        self.trace = []
        for mv in rounds:
            rt = []
            for hid, (r, c), (er, ec), col in mv:
                g[r, c] = 0
                g[er, ec] = col
                idg[r, c] = -1
                idg[er, ec] = hid
                um = sim.unhappy_mask(g, 1 / 3)
                rt.append((frozenset(int(idg[a, b]) for a, b in np.argwhere(um)), sim.avg_share(g)))
            self.trace.append(rt)
        sq, _ = sim.run(sim.SEED, 0.25)
        qF, qids = sq[-1]
        self.q_pos = {int(qids[r, c]): (int(r), int(c)) for r, c in np.argwhere(qF > 0)}
        self.q_share = sim.avg_share(qF)
        cache = json.loads((HERE / "sim_cache.json").read_text())
        assert cache["seed"] == sim.SEED
        self.sweep = {float(k): v for k, v in cache["sweep"].items()}
        same, occ = sim.same_occ(gF)
        assert gF[EX] == 2 and same[EX] == 2 and occ[EX] == 6
        # the share ladder of the random start
        self.ladder = sim.share_ladder(g0)
        self.unh_q = sum(v for f, v in self.ladder.items() if f < Fraction(1, 4))
        self.unh_t = sum(v for f, v in self.ladder.items() if f < Fraction(1, 3))
        assert (self.unh_q, self.unh_t) == (95, 238) == (self.unh_q, len(self.unh0))
        b1 = sim.round1_breakdown()
        assert b1 == {"moved": 200, "content_before_turn": 38, "no_destination": 0}, b1
        # the preference-free comparison town
        self.gZ, self.zone = sim.zoned_town()
        self.shareZ = sim.avg_share(self.gZ)
        assert round(100 * self.shareZ) == round(100 * self.shareF) == 76

    # ------------------------------------------------------------------ builders
    def build_board(self):
        self.tiles = {}
        for hid, (r, c) in sorted(self.final_pos.items()):
            t = Square(TILE, fill_color=COL[self.colour[hid]], fill_opacity=1, stroke_width=0)
            t.move_to(cell(r, c))
            t.ss_unhappy = False
            self.tiles[hid] = t
        self.board = VGroup(*[self.tiles[h] for h in sorted(self.tiles)])
        self.frame = Rectangle(width=N * P + 0.07, height=N * P + 0.07, stroke_color=DIM,
                               stroke_width=2).move_to([GX, GY, 0])
        self.town = VGroup(self.frame, self.board)

    def build_meter(self):
        self.match = ValueTracker(self.shareF)
        self.dem = ValueTracker(self.shareF)
        self.ty = ValueTracker(TY0)
        ty = self.ty
        track = Rectangle(width=TR - TL, height=TH, stroke_color=GRAY, stroke_width=2)
        track.add_updater(lambda m: m.move_to([(TL + TR) / 2, ty.get_value(), 0]))
        fill = Rectangle(width=1, height=TH, fill_color=INK, fill_opacity=0.9, stroke_width=0)

        def fill_upd(m):
            w = max(mx(self.match.get_value()) - TL, 1e-3)
            m.stretch_to_fit_width(w)
            m.move_to([TL + w / 2, ty.get_value(), 0])
        fill.add_updater(fill_upd)
        lo = MathTex(r"0\%", font_size=MATH_SMALL, color=GRAY)
        hi = MathTex(r"100\%", font_size=MATH_SMALL, color=GRAY)
        lo.add_updater(lambda m: m.next_to(track, LEFT, buff=0.15))
        hi.add_updater(lambda m: m.next_to(track, RIGHT, buff=0.15))

        pct = DecimalNumber(100 * self.shareF, num_decimal_places=0, unit=r"\%",
                            font_size=56, color=INK)
        word = text("match", size=32)
        ink_lab = VGroup(pct, word)

        def ink_upd(m):
            v = 100 * self.match.get_value()
            if abs(pct.get_value() - v) > 1e-9:
                pct.set_value(v)
            word.next_to(pct, RIGHT, buff=0.16)
            word.align_to(pct, DOWN)
            m.move_to([mx(self.match.get_value()), 0, 0])
            m.set_y(ty.get_value() + TH / 2 + 0.3 + m.height / 2)
        ink_lab.add_updater(ink_upd)

        mline = Line(UP * 0.28, DOWN * 0.28, color=PURPLE, stroke_width=7)
        mline.add_updater(lambda m: m.move_to([mx(self.dem.get_value()), ty.get_value(), 0]))
        self.dem_sym = MathTex("?", font_size=56, color=PURPLE)
        dword = text("demanded", size=32, color=PURPLE)
        pur_lab = VGroup(self.dem_sym, dword)

        def pur_upd(m):
            dword.next_to(m[0], RIGHT, buff=0.16)
            m.move_to([mx(self.dem.get_value()), 0, 0])
            m.set_y(ty.get_value() - TH / 2 - 0.3 - m.height / 2)
        pur_lab.add_updater(pur_upd)
        for m in (track, fill, ink_lab, pur_lab, mline, lo, hi):
            m.update()
        self.track, self.fill, self.ink_lab, self.pur_lab = track, fill, ink_lab, pur_lab
        self.mline, self.lo, self.hi, self.dword = mline, lo, hi, dword
        self.meter = VGroup(track, fill, lo, hi, mline, ink_lab, pur_lab)

    def build_counter(self):
        """HUD as a two-column table under the meter: labels right-aligned on one edge,
        numbers right-aligned on the meter's 100 % end (TR), so 74 / 0 / 1 share a column."""
        self.unh = ValueTracker(0)
        NUM_R = TR                                   # number column: right edge = meter's 100 % end
        LAB_R = NUM_R - 0.76 - 0.25                 # label column: right edge (widest number "238")
        Y0 = HUD_Y                                   # first row (the HUD sits beside the board's middle)
        word = text("unhappy", size=LABEL, color=RED)
        num = DecimalNumber(238, num_decimal_places=0, font_size=52, color=RED)
        word.move_to([LAB_R - word.width / 2, Y0, 0])
        num.set_value(0)

        def right_at(m, ref):
            m.shift(RIGHT * (NUM_R - m.get_right()[0]))
            m.align_to(ref, DOWN)

        def nupd(m):
            v = self.unh.get_value()
            if m.get_value() != v:
                m.set_value(v)
            right_at(m, word)
        num.add_updater(nupd)
        num.update()
        self.counter = VGroup(word, num)
        # the plan's prediction: same columns, its 0 directly under the count's last digit
        pword = text("plan predicts", size=28, color=GRAY)
        pword.move_to([LAB_R - pword.width / 2, Y0 - 0.72, 0])
        pnum = MathTex("0", font_size=40, color=GRAY)
        right_at(pnum, pword)
        self.plan = VGroup(pword, pnum)
        self.round_no = ValueTracker(1)
        rword = text("round", size=28, color=GRAY)
        rword.move_to([LAB_R - rword.width / 2, Y0 - 1.36, 0])
        rnum = Integer(1, font_size=40, color=GRAY)

        def rupd(m):
            v = int(round(self.round_no.get_value()))
            if m.get_value() != v:
                m.set_value(v)
            right_at(m, rword)
        rnum.add_updater(rupd)
        rnum.update()
        self.round_lab = VGroup(rword, rnum)
        # moves made so far in the current round (live: 200 in round one, then 72, 41, ...)
        self.moves_n = ValueTracker(0)
        mword = text("moves", size=28, color=GRAY)
        mword.move_to([LAB_R - mword.width / 2, Y0 - 2.0, 0])
        mnum = Integer(200, font_size=40, color=GRAY)
        mnum.set_value(0)

        def mupd(m):
            v = int(round(self.moves_n.get_value()))
            if m.get_value() != v:
                m.set_value(v)
            right_at(m, mword)
        mnum.add_updater(mupd)
        mnum.update()
        self.moves_lab = VGroup(mword, mnum)
        self.note_y = Y0 - 2.68
        self.num_r = NUM_R

    # ------------------------------------------------------------------ board placement
    def bcell(self, r, c):
        """Square (r, c) of the board where it currently sits (normal, or parked for the replay)."""
        return cell(r, c, centre=self.bc, s=self.bs)

    def bring(self, tile, flag):
        """Unhappy ring on a board tile at the board's current scale."""
        set_unhappy(tile, flag, width=UNH_W * self.bs, base=TILE * self.bs)

    def relayout(self, centre, s, opacity=None, rings=None):
        """Animation: move/scale the whole board (frame, tiles at self.pos) to centre/s.
        opacity: {hid: final fill opacity} (interpolated); rings: {hid: unhappy?} (switch at 1/2)."""
        c0, s0 = np.array(self.bc, dtype=float), self.bs
        c1 = np.array(centre, dtype=float)
        tiles = self.tiles
        op0 = {h: tiles[h].get_fill_opacity() for h in (opacity or {})}
        rings = dict(rings or {})

        def upd(_m, a):
            u = smooth(a)
            cc, ss = c0 + (c1 - c0) * u, s0 + (s1_ - s0) * u
            if a >= 0.5:
                for h, want in rings.items():
                    tiles[h].ss_unhappy = want
            for h, t in tiles.items():
                ring = t.ss_unhappy
                if opacity and h in opacity:
                    o = op0[h] + (opacity[h] - op0[h]) * u
                    t.set_fill(opacity=o)
                else:
                    o = t.get_fill_opacity()
                t.set_stroke(RED, width=UNH_W * ss if ring else 0, opacity=o if ring else 0)
                t.set_width(TILE * ss + (UNH_W * ss * 0.01 if ring else 0))
                t.move_to(cell(*self.pos[h], centre=cc, s=ss))
            self.frame.scale_to_fit_width((N * P + 0.07) * ss)
            self.frame.move_to([cc[0], cc[1], 0])
        s1_ = s

        def fin():
            self.bc, self.bs = (float(c1[0]), float(c1[1])), s
        return UpdateFromAlphaFunc(self.town, upd), fin

    def note(self, s):
        """GRAY HUD note, right-aligned on the number column."""
        m = text(s, size=TEXT_LABEL_MIN, color=GRAY)
        return m.move_to([self.num_r - m.width / 2, self.note_y, 0])

    def flash_box(self, *ms, color=INK, run_time=1.2, buff=0.1):
        """Point at mobjects with a box that draws on and fades (never recolours them)."""
        boxes = [SurroundingRectangle(m, color=color, buff=buff, corner_radius=0.06,
                                      stroke_width=3) for m in ms]
        self.play(*[Create(b) for b in boxes], run_time=run_time * 0.5)
        self.play(*[FadeOut(b) for b in boxes], run_time=run_time * 0.5)

    def swap(self, m, new):
        """Change a glyph in place without a point morph (a morph between digits passes
        through garbled shapes): fade out, take the new shape at the midpoint, fade in.
        The mobject keeps its identity, so later animations can still address it.
        Use run_time >= 0.6 so each half (out, then in) lasts >= 0.3 s."""
        # the MathTex parent has no points of its own (its opacity can read 0): use the glyphs'
        op0 = max([x.get_fill_opacity() for x in m.get_family() if len(x.points)] + [1e-3])
        state = {"done": False}

        def upd(mm, a):
            if a < 0.5:
                mm.set_opacity(op0 * (1 - 2 * a))
            else:
                if not state["done"]:
                    c = mm.get_center()
                    mm.become(new.copy().move_to(c))
                    state["done"] = True
                mm.set_opacity(min(1.0, 2 * a - 1))
        return UpdateFromAlphaFunc(m, upd)

    def pulse(self, m, scale=1.12, run_time=0.9):
        """Brief scale-up of a label in its own colour (no recolouring)."""
        self.play(m.animate(rate_func=there_and_back).scale(scale), run_time=run_time)

    @staticmethod
    def soft_dim(group, k):
        """Fade every drawn part of `group` to k x its own fill and stroke opacity (k=1 restores).
        Unlike set_opacity, hollow squares stay hollow (their fill opacity stays 0)."""
        anims = []
        for m in group.get_family():
            if not len(m.points):
                continue
            if not hasattr(m, "ss_op0"):
                m.ss_op0 = (m.get_fill_opacity(), m.get_stroke_opacity())
            f0, s0 = m.ss_op0
            anims.append(m.animate.set_fill(opacity=f0 * k).set_stroke(opacity=s0 * k))
        return anims

    def ctx_fade(self, ms, k):
        """Dim (k=0.3) or restore (k=1) context.  Unlike style.dim/undim this keeps the
        hollow meter track hollow (set_opacity would fill it) and the fill at 0.9."""
        anims = []
        for m in ms:
            if m is self.track or m is self.mline:
                anims.append(m.animate.set_stroke(opacity=k))
            elif m is self.fill:
                anims.append(m.animate.set_fill(opacity=0.9 * k))
            else:
                anims.append(m.animate.set_opacity(k))
        return anims

    def fly_into(self, pairs, extra=(), run_time=1.0):
        """Each source square's copy flies (staying square) to its digit and fades into it.
        pairs: [(source squares, target digit), ...].  No shape morph, so no blobs mid-flight."""
        flights, targets = [], []
        for srcs, tgt in pairs:
            side = 0.55 * tgt.height
            for s in srcs:
                c = s.copy().set_stroke(width=0).set_fill(opacity=1).set_z_index(6)
                flights.append(c.animate.move_to(tgt.get_center()).set(width=side))
            targets.append(tgt)
        copies = [f.mobject for f in flights]
        self.play(*flights, *extra, run_time=run_time * 0.65, rate_func=SMOOTH)
        self.play(*[FadeOut(c) for c in copies], *[FadeIn(t) for t in targets],
                  run_time=run_time * 0.35)

    def end_card(self, hold: float = 0.8, run_time: float = 0.5):
        """Series card, with the Omega in INK: BLUE means 'blue households' in this episode."""
        card = ss_style.end_card(self.EPISODE, self.TITLE)
        card[0][0].set_color(INK)
        anims = [FadeOut(m) for m in list(self.mobjects)] + [FadeIn(card, shift=0.1 * UP)]
        self.play(*anims, run_time=run_time)
        self.hold(hold)

    # ------------------------------------------------------------------ moves
    def play_round(self, k, run_time, flight=0.9, arc=0.9, extra=()):
        """Animate round k (0-based): tiles hop, outlines, meter and counter follow the sim."""
        moves = self.rounds[k]
        trace = self.trace[k]
        M = len(moves)
        flight = min(flight, run_time * 0.6)
        span = max(run_time - flight, 1e-3)
        starts = [i * span / max(M - 1, 1) for i in range(M)]
        lands = [s + flight for s in starts]
        prev_set = self.cur_unhappy
        prev_share = self.match.get_value()
        involved = {m[0] for m in moves}
        allsets = [prev_set] + [t[0] for t in trace]
        for a, b in zip(allsets, allsets[1:]):
            involved |= set(a ^ b)
        # households the corner replay already moved to their destination (shown early, in
        # sync with the inset): no ring until their real round has passed
        skip = {h for h, kk in self.early.items() if kk >= k}
        involved -= skip
        paths = {}
        for (hid, a, b, col) in moves:
            # start from where the tile is (an early mover is already at b: zero-length flight)
            paths[hid] = (self.tiles[hid].get_center(), self.bcell(*b),
                          path_along_arc(arc if (b[1] >= a[1]) else -arc))
        state = {"j": -1}

        def upd(group, alpha):
            t = alpha * run_time
            done = alpha >= 1 - 1e-9          # float noise must never skip the final state
            for i, (hid, a, b, col) in enumerate(moves):
                u = 1.0 if done else (t - starts[i]) / flight
                if u <= 0:
                    continue
                p0, p1, path = paths[hid]
                tile = self.tiles[hid]
                if u >= 1:
                    tile.move_to(p1)
                    tile.set_z_index(0)
                else:
                    tile.set_z_index(5)
                    tile.move_to(path(p0, p1, smooth(u)))
            j = M if done else bisect.bisect_right(lands, t)
            if j != state["j"]:
                state["j"] = j
                cur = trace[j - 1][0] if j > 0 else prev_set
                for h in involved:
                    want = h in cur
                    if self.tiles[h].ss_unhappy != want:
                        self.bring(self.tiles[h], want)
                self.match.set_value(trace[j - 1][1] if j > 0 else prev_share)
                self.unh.set_value(len(cur))
                self.moves_n.set_value(j)
        self.moves_n.set_value(0)
        # extra animations keep their own run_times (no play-level run_time)
        self.play(UpdateFromAlphaFunc(self.board, upd, run_time=run_time, rate_func=linear), *extra)
        self.cur_unhappy = trace[-1][0]
        for hid, a, b, col in moves:
            self.pos[hid] = b
        # belt and braces: the board, outlines and meters equal the simulated state exactly
        for h, tile in self.tiles.items():
            tile.move_to(self.bcell(*self.pos[h])).set_z_index(0)
            want = h in self.cur_unhappy and h not in skip
            if tile.ss_unhappy != want:
                self.bring(tile, want)
        self.match.set_value(trace[-1][1])
        self.unh.set_value(len(self.cur_unhappy))
        self.moves_n.set_value(M)

    # ------------------------------------------------------------------ scene
    def construct(self):
        self.prep()
        self.build_board()
        self.build_meter()
        self.build_counter()
        self.pos = dict(self.final_pos)
        self.cur_unhappy = frozenset()
        self.early = {}                  # hid -> round index it moves in, if shown early (replay)
        self.bc, self.bs = (GX, GY), 1.0  # where the board sits and its scale
        FS = 56

        def fpiece(s, color=INK):
            return MathTex(s, font_size=FS, color=color)

        # 1 - cold open: the finished town (centred), then the meter and the question ------
        sim_tag = text("simulated", size=22, color=GRAY)
        sim_tag.next_to(self.frame, DOWN, buff=0.22).align_to(self.frame, LEFT)
        assert sim_tag.get_bottom()[1] >= -3.2
        opener = VGroup(self.town, sim_tag)
        opener.shift(RIGHT * (0 - GX))                  # frame 1: the town fills the centre
        self.add(self.town, sim_tag)                    # tagged "simulated" from frame 0
        with self.narrate("In this simulated town, on average, three quarters of a household's "
                          "neighbors match its color. How much matching do these households "
                          "demand? [pause 1.5]") as beat:
            # the puzzle's number is on screen before it is spoken: the town slides left, the
            # meter is drawn already at 76 % (it never counts up from a 0 % that never existed)
            beat.wait_until("simulated", offset=-0.25)
            self.play(opener.animate.shift(LEFT * (0 - GX)),
                      FadeIn(self.track), FadeIn(self.lo), FadeIn(self.hi), FadeIn(self.fill),
                      run_time=0.8, rate_func=SMOOTH)
            self.play(Write(self.ink_lab), run_time=0.6)
            beat.wait_until("three", offset=-0.15)
            self.pulse(self.ink_lab, 1.12)
            # the unknown demand arrives on "these households demand" (deictic sync)
            beat.on("these", FadeIn(self.mline), FadeIn(self.pur_lab, shift=0.15 * UP),
                    lead=0.15, run_time=0.8)
            beat.wait_until("demand", offset=-0.05)
            self.pulse(self.pur_lab, 1.15, run_time=0.8)

        # 2 - reveal: a third, and what the rule looks like -------------------------------
        third_sym = MathTex(r"\tfrac{1}{3}", font_size=56, color=PURPLE)
        ex = cell(*EX)
        ex_box = Square(3 * P, stroke_color=INK, stroke_width=3).move_to(ex)
        rule_tiles = VGroup()
        rule_slots = VGroup()
        rule_x = VGroup()
        gold_nb = []
        for (r, c) in [EX] + nb8(EX):
            pos = RULE_C + np.array([(c - EX[1]) * RULE_P, -(r - EX[0]) * RULE_P, 0])
            slot = Square(RULE_T, stroke_color=DIM, stroke_width=2).move_to(pos)
            rule_slots.add(slot)
            v = int(self.gF[r, c])
            if v:
                t = Square(RULE_T, fill_color=COL[v], fill_opacity=1, stroke_width=0).move_to(pos)
                rule_tiles.add(t)
                if (r, c) != EX and v == 2:
                    gold_nb.append(t)
            else:
                rule_x.add(cross(slot, 0.6 * RULE_T))
        assert len(rule_x) == 2
        src_tiles = VGroup(*[self.tiles[self.id_atF[q]] for q in [EX] + nb8(EX) if q in self.id_atF])
        rule_frame = Square(3 * RULE_P + 0.06, stroke_color=INK, stroke_width=3).move_to(RULE_C)
        centre_ring = Square(RULE_T + 0.1, stroke_color=INK, stroke_width=3).move_to(RULE_C)
        gold_rings = VGroup(*[Square(RULE_T + 0.1, stroke_color=INK, stroke_width=3).move_to(t)
                              for t in gold_nb])
        two = MathTex("2", font_size=56, color=YELLOW)
        of6 = text("of 6 match", size=32)
        rule_lab = VGroup(two, of6).arrange(RIGHT, buff=0.18)
        of6.align_to(two, DOWN)
        rule_lab.next_to(rule_frame, RIGHT, buff=0.3).shift(UP * 0.38)
        empty_lab = text("empty: not counted", size=TEXT_LABEL_MIN, color=GRAY)
        empty_lab.next_to(rule_lab, DOWN, buff=0.32).align_to(rule_lab, LEFT)
        with self.narrate("Just a third. [pause 0.25] Each household counts the occupied squares "
                          "around it. If fewer than a third match, it moves, so it is happy to be "
                          "outnumbered two to one.", speed=0.82) as beat:
            self.play(self.dem.animate.set_value(1 / 3),
                      self.swap(self.dem_sym, third_sym),
                      Create(ex_box),
                      run_time=beat.until("Each", min_time=1.0), rate_func=SMOOTH)
            self.play(TransformFromCopy(src_tiles, rule_tiles), FadeIn(rule_slots),
                      TransformFromCopy(ex_box, rule_frame),
                      run_time=beat.until("occupied", offset=-0.05, min_time=0.9))
            self.play(Create(rule_x), FadeIn(empty_lab, shift=0.1 * LEFT), run_time=0.6)
            beat.wait_until("fewer", offset=-0.2)
            self.play(Create(centre_ring), Create(gold_rings), run_time=0.8)
            self.play(FadeIn(rule_lab, shift=0.1 * LEFT), run_time=0.7)
            beat.wait_until("outnumbered", offset=-0.2)
            self.pulse(rule_lab, 1.12)

        # 3 - stakes ---------------------------------------------------------------------
        rule_all = VGroup(rule_slots, rule_tiles, rule_x, rule_frame, centre_ring, gold_rings,
                          rule_lab, empty_lab)
        with self.narrate("We read real city maps the same way, guessing motives from "
                          "patterns. So how can a demand of one third build a town of three "
                          "quarters?", speed=0.82, gap=0.45) as beat:
            # (round 5 cont.) the rule stays, dimmed to 60 %, so the lower right is not left
            # empty for the whole stakes beat; it comes back to full strength when the question
            # names it ("a demand of one third") and leaves with the rewind
            self.play(*self.soft_dim(rule_all, 0.6), FadeOut(ex_box), run_time=0.7)
            beat.wait_until("motives", offset=-0.25)
            self.pulse(self.pur_lab, 1.12, run_time=0.6)
            beat.wait_until("patterns", offset=-0.2)
            self.flash_box(self.town, buff=0.05)
            beat.wait_until("demand", offset=-0.15)
            self.play(*self.soft_dim(rule_all, 1.0),
                      self.pur_lab.animate(rate_func=there_and_back).scale(1.15), run_time=0.9)
            beat.wait_until("town", offset=-0.15)
            self.pulse(self.ink_lab, 1.12)

        # 4 - naive build: rewind to a random mix -------------------------------------------
        with self.narrate("Rewind to the start, a random mix. Here, on average, half the "
                          "neighbors match, well above a third.", gap=0.12) as beat:
            starts = {h: self.tiles[h].get_center() for h in self.tiles}
            ends = {h: cell(*self.start_pos[h]) for h in self.tiles}
            order = sorted(self.tiles)

            def rewind(group, alpha):
                a = smooth(alpha)
                for h in order:
                    self.tiles[h].move_to(starts[h] + (ends[h] - starts[h]) * a)
            self.play(UpdateFromAlphaFunc(self.board, rewind),
                      self.match.animate.set_value(self.share0), FadeOut(rule_all),
                      run_time=beat.until("Here", min_time=2.2), rate_func=linear)
            self.pos = dict(self.start_pos)
            # "Here, on average, half": the 50 % readout pulses as "Here" lands
            beat.wait_until("Here", offset=-0.1)
            self.pulse(self.ink_lab, 1.12)
            # dock the meter now, so the counter can arrive on "these" (never crossing labels)
            self.play(self.ty.animate.set_value(TY1), run_time=0.9, rate_func=SMOOTH)
            beat.wait_until("above", offset=-0.1)
            self.pulse(self.pur_lab, 1.15)

        with self.narrate("Still, these two hundred thirty-eight are unhappy.") as beat:
            self.play(FadeIn(self.counter, shift=0.1 * UP),
                      run_time=beat.until("these", offset=-0.1, min_time=0.4))
            unh_tiles = [self.tiles[h] for h in sorted(self.unh0)]
            self.play(LaggedStart(*[UpdateFromAlphaFunc(
                t, lambda m, a: set_unhappy(m, a > 0.5)) for t in unh_tiles], lag_ratio=0.004),
                self.unh.animate.set_value(len(self.unh0)),
                run_time=1.6, rate_func=linear)
            self.cur_unhappy = frozenset(self.unh0)
            beat.wait_until("unhappy", offset=-0.1)
            self.pulse(self.counter, 1.1, run_time=0.8)

        # the plan, previewed on its first mover
        m0 = self.rounds[0][PREVIEW_MOVE]          # a real round-1 move, long enough to read
        a0, b0 = cell(*m0[1]), cell(*m0[2])
        preview = DashedVMobject(ArcBetweenPoints(a0, b0, angle=0.9 if m0[2][1] >= m0[1][1] else -0.9),
                                 num_dashes=24, color=INK).set_stroke(width=4)
        dest_box = Square(TILE + 0.14, stroke_color=INK, stroke_width=4).move_to(b0)
        src_box = Square(TILE + 0.14, stroke_color=INK, stroke_width=4).move_to(a0)
        with self.narrate("The obvious plan is to move each one to a random empty square "
                          "where it would be content. [pause 0.2] Then everyone is content, and "
                          "the town stays mixed.", speed=0.82) as beat:
            beat.wait_until("each", offset=-0.2)
            self.play(Create(src_box), run_time=0.6)
            beat.wait_until("random", offset=-0.2)
            self.play(Create(preview), Create(dest_box), run_time=1.0)
            beat.wait_until("everyone", offset=-0.2)
            self.play(FadeIn(self.plan, shift=0.1 * DOWN), run_time=0.8)
            beat.wait_until("stays", offset=-0.2)
            self.pulse(self.ink_lab, 1.1)

        # 5 - run round one, and the measured failure -----------------------------------
        # (round 5: "The matching share jumps to sixty-four percent" was cut: the meter shows it)
        with self.narrate("Round one takes two hundred moves; the other thirty-eight were "
                          "content by their turn.") as beat:
            # (a number that changes digits cannot fade in while it counts: rows first)
            self.play(FadeOut(preview), FadeOut(src_box), FadeOut(dest_box),
                      FadeIn(self.round_lab), FadeIn(self.moves_lab), run_time=0.4)
            # the live "moves" count reaches 200 as the round ends; the unhappy count is live too
            self.play_round(0, run_time=beat.until("other", offset=-0.05, min_time=2.2))
            b1 = sim.round1_breakdown()
            note38 = self.note(f"{b1['content_before_turn']} content by their turn")
            beat.wait_until("thirty", offset=-0.2)
            self.play(FadeIn(note38, shift=0.1 * UP), run_time=0.6)
            # (the meter climbs 50 % -> 64 % live during the round; no spoken number)

        movers1 = {m[0] for m in self.rounds[0]}
        others = [self.tiles[h] for h in self.tiles if h not in self.cur_unhappy]
        was_unh = [self.tiles[h] for h in sorted(self.cur_unhappy) if h in self.unh0]
        n_content0 = sum(h not in self.unh0 for h in self.cur_unhappy)
        assert (len(self.cur_unhappy), n_content0, len(was_unh)) == (74, 67, 7)
        assert all(h not in movers1 for h in self.cur_unhappy if h not in self.unh0)
        note67 = self.note(f"{n_content0} content at the start")
        with self.narrate("If the plan had worked, this counter would read zero. It reads "
                          "seventy-four. [pause 0.9] Sixty-seven of these were content before "
                          "round one. [pause 0.15] They never moved. Their neighbors did.",
                          gap=0.6) as beat:
            beat.wait_until("this", offset=-0.3)
            self.pulse(self.counter, 1.15, run_time=0.8)
            beat.wait_until("zero", offset=-0.25)
            self.pulse(self.plan, 1.15)
            beat.wait_until("seventy", offset=-0.25)
            self.pulse(self.counter, 1.1)
            beat.wait_until("sixty", offset=-0.2)
            # keep red rings on the 67 that were content at the start; the other 7 go grey
            # the 38 note leaves before the 67 note arrives in its slot (never superimposed)
            # (the dim runs 1.4 s, through "of these", so the deictic lands on it)
            self.play(*[t.animate(run_time=1.4).set_fill(opacity=0.22) for t in others],
                      *[t.animate(run_time=1.4).set_stroke(GRAY) for t in was_unh],
                      Succession(FadeOut(note38, run_time=0.35),
                                 FadeIn(note67, shift=0.1 * UP, run_time=0.65)))
            beat.wait_until("never", offset=-0.2)
            self.pulse(note67, 1.1, run_time=0.8)
            beat.wait_until("Their", offset=-0.2)
            self.play(*[t.animate.set_fill(opacity=1.0) for t in others],
                      *[t.animate.set_stroke(RED) for t in was_unh], run_time=1.0)

        # 6 - insight: replay one corner -------------------------------------------------
        r0, r1 = PATCH_R
        c0, c1 = PATCH_C
        # the focus box sits on the board's corner where the board is parked for the replay
        rp = P * RS
        tl = cell(r0, c0, RC, RS) + np.array([-rp / 2, rp / 2, 0])
        br = cell(r1, c1, RC, RS) + np.array([rp / 2, -rp / 2, 0])
        src = Rectangle(width=br[0] - tl[0] + 0.04, height=tl[1] - br[1] + 0.04, stroke_color=INK,
                        stroke_width=4).move_to((tl + br) / 2)

        def in_patch(rc):
            return r0 <= rc[0] <= r1 and c0 <= rc[1] <= c1
        hA, hB, hC, hD = (self.id_at0[q] for q in (A_, B_, C_, D_))
        patch0 = {h for h, rc in self.start_pos.items() if in_patch(rc)}
        patch1 = {h for h, rc in self.pos.items() if in_patch(rc)}
        assert patch0 - patch1 == {hA} and patch1 <= patch0, patch0 ^ patch1
        # the board's own corner replays in step with the inset, with the real tiles and the
        # real moves: round 2 = B out + one blue arrival at A's old square; round 3 = C out
        mv2 = [(h, a, b) for h, a, b, _ in self.rounds[1] if in_patch(a) or in_patch(b)]
        mv3 = [(h, a, b) for h, a, b, _ in self.rounds[2] if in_patch(a) or in_patch(b)]
        assert {m[0] for m in mv2 if in_patch(m[1])} == {hB} and len(mv2) == 2, mv2
        assert [m[0] for m in mv3] == [hC] and all(not in_patch(m[2]) for m in mv3), mv3
        a_home = self.pos[hA]                               # where A lives after round 1
        ctx_ids = [h for h in self.tiles if h not in patch1 and h != hA]

        def board_fly(h, rc, opacity, ring, arc=0.8):
            """A real board tile flies to square rc, landing at `opacity` with ring state `ring`."""
            t = self.tiles[h]
            t.generate_target()
            self.bring(t.target, ring)
            t.target.move_to(self.bcell(*rc)).set_opacity(opacity)
            t.ss_unhappy = ring
            t.set_z_index(5)
            return MoveToTarget(t, path_arc=arc)

        def ring_state(hs, unhappy):
            """Switch the rings of board tiles hs to a given unhappy set, halfway through."""
            tiles = [self.tiles[h] for h in hs]

            def f(_m, a):
                if a >= 0.5:
                    for h, t in zip(hs, tiles):
                        want = h in unhappy
                        if t.ss_unhappy != want:
                            self.bring(t, want)
            return UpdateFromAlphaFunc(VGroup(*tiles), f)

        def ring_on(h):
            return UpdateFromAlphaFunc(self.tiles[h], lambda m, a: self.bring(m, a > 0.3))

        mtl = mag_cell(r0, c0) + np.array([-MAG_P / 2, MAG_P / 2, 0])
        mbr = mag_cell(r1, c1) + np.array([MAG_P / 2, -MAG_P / 2, 0])
        mframe = Rectangle(width=mbr[0] - mtl[0] + 0.06, height=mtl[1] - mbr[1] + 0.06,
                           stroke_color=INK, stroke_width=3).move_to((mtl + mbr) / 2)
        mtiles = {}
        mempty = VGroup()
        for r in range(r0, r1 + 1):
            for c in range(c0, c1 + 1):
                hid = self.id_at0.get((r, c))
                slot = Square(MAG_T, stroke_color=DIM, stroke_width=2).move_to(mag_cell(r, c))
                mempty.add(slot)
                if hid is not None:
                    t = Square(MAG_T, fill_color=COL[self.colour[hid]], fill_opacity=1,
                               stroke_width=0).move_to(mag_cell(r, c))
                    set_unhappy(t, hid in self.unh0, width=MAG_UNH, base=MAG_T)
                    if (r, c) == A_:
                        # A's ring stays at half strength until A is the subject ("Then this
                        # neighbor moved away"), so the eye goes to B first
                        t.set_stroke(opacity=0.5)
                    mtiles[(r, c)] = t
        mag = VGroup(mempty, *mtiles.values())

        def recap(s):
            """Replace the caption in place: the old one fades out, THEN the new one fades in
            (toolkit swap; a simultaneous cross-fade showed "aftere round 1" for a few frames)."""
            new = text(s, size=28, color=GRAY)
            new.move_to(caps[-1]).align_to(caps[-1], LEFT)
            old = caps[-1]
            caps.append(new)
            return [swap(old, new, shift=0.0)]

        def ring3(rc, color=INK):
            return Square(3 * MAG_P + 0.06, stroke_color=color, stroke_width=5).move_to(mag_cell(*rc))

        def focus(rc, extra=()):
            """Dim magnified tiles outside rc's 3x3 neighbourhood (context at 30 %)."""
            keep = set(nb8(rc)) | {rc} | set(extra)
            return [t.animate.set_opacity(1.0 if q in keep else 0.3) for q, t in mtiles.items()
                    if not (q in keep and t.get_fill_opacity() > 0.99)]

        def mag_ring(rc):
            return UpdateFromAlphaFunc(mtiles[rc], lambda m, a: set_unhappy(
                m, a > 0.3, width=MAG_UNH, base=MAG_T))

        # the formula's pieces live in F: a new household gets new glyph objects (they slide in),
        # the same household's numbers cross-fade in place (swap)
        F = {"num": fpiece("3", YELLOW), "den": fpiece("8"),
             "bar": Line(LEFT * 0.3, RIGHT * 0.3, stroke_width=3.5, color=INK),
             "rel": fpiece(r"\geq")}
        frac = VGroup(F["num"], F["bar"], F["den"]).arrange(DOWN, buff=0.1)
        f_third = MathTex(r"\frac{1}{3}", font_size=FS, color=PURPLE)
        formula_grp = VGroup(frac, F["rel"], f_third).arrange(RIGHT, buff=0.28)
        formula_grp.next_to(mframe, RIGHT, buff=0.4)
        frac_c, rel_c = frac.get_center().copy(), F["rel"].get_center().copy()
        # the state caption sits under the formula it describes (under the inset it would
        # reach the caption zone: the inset is 675 px wide now)
        cap = text("before round 1", size=28, color=GRAY).next_to(formula_grp, DOWN, buff=0.45)
        cap.align_to(formula_grp, LEFT)                 # clear of the inset frame on its left
        caps = [cap]                                   # the caption currently on screen
        parked_right = RC[0] + (N * P + 0.07) * RS / 2
        assert formula_grp.get_right()[0] <= 6.4 and cap.get_right()[0] <= 6.4, formula_grp.get_right()
        assert mframe.get_left()[0] > parked_right + 0.3, (mframe.get_left(), parked_right)
        assert mframe.get_top()[1] <= self.pur_lab.get_bottom()[1] - 0.18 + (TY1 - self.ty.get_value()), \
            (mframe.get_top(), self.pur_lab.get_bottom())
        hud = [self.counter, self.plan, self.round_lab, self.moves_lab, note67]
        # the round-1 readout (64 %) would be stale during the replay: fade it out completely;
        # only the demand ("1/3 demanded") stays, since the formula copies its 1/3
        meter_ink = [self.track, self.fill, self.ink_lab, self.lo, self.hi, self.mline]

        def pending():
            """The neighbourhood just changed: the old fraction is stale, so dim it and ask."""
            return [self.swap(F["rel"], fpiece("?")),
                    F["num"].animate.set_opacity(0.3), F["den"].animate.set_opacity(0.3)]

        def resolve_to(n, d, r):
            """Same household, new numbers: each glyph fades out, then the new one fades in."""
            return [self.swap(F["num"], fpiece(n, YELLOW)), self.swap(F["den"], fpiece(d)),
                    self.swap(F["rel"], fpiece(r))]

        def next_household(n, d, r, run_time):
            """A different household: its fraction and relation slide out to the left and
            fade, THEN the next household's slide in from the right (never superimposed).
            The demand (1/3) stays put: it is the same for everyone."""
            nn, dd, rr = fpiece(n, YELLOW), fpiece(d), fpiece(r)
            bb = F["bar"].copy().set_opacity(1)
            VGroup(nn, bb, dd).arrange(DOWN, buff=0.1).move_to(frac_c)
            rr.move_to(rel_c)
            old = [F["num"], F["bar"], F["den"], F["rel"]]
            out_t, in_t = 0.42 * run_time, 0.58 * run_time
            anim = Succession(
                AnimationGroup(*[FadeOut(m, shift=0.35 * LEFT) for m in old], run_time=out_t),
                AnimationGroup(*[FadeIn(m, shift=0.35 * LEFT) for m in (nn, bb, dd, rr)],
                               run_time=in_t))
            F.update(num=nn, bar=bb, den=dd, rel=rr)
            return anim

        # the subject household: a white inner outline (B, then C, then D)
        subj = Square(MAG_T - 0.12, stroke_color=INK, stroke_width=4).move_to(mag_cell(*B_))
        subj.set_z_index(4)

        with self.narrate("Replay one corner. [pause 0.3] At the start, this gold household "
                          "had three gold neighbors out of eight. Three eighths beats a third, so "
                          "it stayed.", speed=0.82) as beat:
            # the board parks at the left edge at 0.7 (context dimmed), making room for the inset
            park, park_done = self.relayout(RC, RS, opacity={h: 0.3 for h in ctx_ids})
            fw = (N * P + 0.07) * RS
            tag_to = [RC[0] - fw / 2 + sim_tag.width / 2, RC[1] - fw / 2 - 0.22 - sim_tag.height / 2, 0]
            self.play(park, sim_tag.animate.move_to(tag_to), FadeOut(*hud),
                      *self.ctx_fade(meter_ink, 0.0), run_time=0.9)
            park_done()
            # the corner rewinds to before round one (A flies home, rings go to the start state)
            # while the inset flies out of it: one move
            self.play(Create(src), board_fly(hA, A_, 1.0, hA in self.unh0, arc=-0.8),
                      ring_state(sorted(patch1), self.unh0),
                      TransformFromCopy(src, mframe), FadeIn(mag, scale=0.3, target_position=src),
                      FadeIn(cap), run_time=1.1)
            self.tiles[hA].set_z_index(0)
            ringB = ring3(B_)
            beat.wait_until("this", offset=-0.2)
            self.play(Create(ringB), Create(subj), *focus(B_), run_time=0.8)
            golds = [mtiles[q] for q in nb8(B_) if q in mtiles and self.colour[self.id_at0[q]] == 2]
            alln = [mtiles[q] for q in nb8(B_) if q in mtiles]
            assert (len(golds), len(alln)) == (3, 8)
            beat.wait_until("three", offset=-0.15)
            self.fly_into([(golds, F["num"])], run_time=1.0)
            beat.wait_until("eight", offset=-0.3)
            self.fly_into([(alln, F["den"])], extra=[Create(F["bar"])], run_time=1.0)
            beat.wait_until("beats", offset=-0.2)
            self.play(Write(F["rel"]), run_time=0.5)
            # (the same glyphs, 1 over 3, at two sizes: a move and a scale, not a glyph morph;
            # the meter's symbol was "?" until it became 1/3, so the lint sees different strings)
            self.play(allow_morph(TransformFromCopy(self.dem_sym, f_third, path_arc=0.6 * PI)),
                      run_time=1.1)

        a_in = mtiles.pop(A_)
        with self.narrate("Then this neighbor moved away. Is it still content? [pause 1.2]") as beat:
            # A becomes the subject: its ring comes to full strength as it pulses
            a_c, a_w = a_in.get_center().copy(), a_in.width

            def a_pulse(m, a):
                m.set_stroke(opacity=0.5 + 0.5 * a)
                m.scale_to_fit_width(a_w * (1 + 0.15 * there_and_back(a))).move_to(a_c)
            self.play(UpdateFromAlphaFunc(a_in, a_pulse), run_time=0.7, rate_func=linear)
            beat.wait_until("moved", offset=-0.1)
            # the departure and the "?" are one event: the fraction is never stale on screen;
            # on the board, the same household flies to the square it really moved to
            self.play(a_in.animate.shift(UP * 1.0).set_opacity(0),
                      board_fly(hA, a_home, 0.3, hA in self.cur_unhappy),
                      *recap("after round 1"), *pending(), run_time=1.2)
            self.tiles[hA].set_z_index(0)
            self.remove(a_in)
            beat.wait_until("still", offset=-0.2)
            self.pulse(ringB, 1.06, run_time=0.8)

        with self.narrate("Two gold out of seven. Two sevenths is less than a third, so now "
                          "it wants out.", speed=0.82) as beat:
            self.play(self.swap(F["num"], fpiece("2", YELLOW)), run_time=0.6)
            beat.wait_until("seven", offset=-0.25)
            self.play(self.swap(F["den"], fpiece("7")), run_time=0.6)
            beat.wait_until("less", offset=-0.25)
            self.play(self.swap(F["rel"], fpiece("<")), run_time=0.6)
            self.play(flag(F["rel"], color=INK), run_time=0.7)
            beat.wait_until("wants", offset=-0.2)
            self.play(ringB.animate.set_stroke(RED), mag_ring(B_), ring_on(hB), run_time=0.6)

        g1, g2 = self.states[1][0], self.states[2][0]
        arrivals2 = [(r, c) for r in range(r0, r1 + 1) for c in range(c0, c1 + 1)
                     if g1[r, c] == 0 and g2[r, c] > 0]
        # (round 5 cont.: the third step, "Then the next one, also at three eighths, tips in round
        # three", was cut for the concision budget; two links already make the chain, A -> B -> C)
        with self.narrate("Its neighbor here also has three eighths. In round two, our household "
                          "leaves, and this one drops to two sevenths.", speed=0.83,
                          gap=0.6) as beat:
            ringC = ring3(C_)
            beat.wait_until("neighbor", offset=-0.25)
            # the focus moves to C, and C's own formula replaces B's (slide = new household)
            self.play(ReplacementTransform(ringB, ringC), subj.animate.move_to(mag_cell(*C_)),
                      *focus(C_, extra=[B_]), next_household("3", "8", r"\geq", 0.9),
                      run_time=0.9)
            beat.wait_until("three", offset=-0.2)
            self.play(flag(F["num"]), run_time=0.6)
            beat.wait_until("leaves", offset=-0.4)
            b_in = mtiles.pop(B_)
            arr = []
            for (r, c) in arrivals2:
                t = Square(MAG_T, fill_color=COL[int(g2[r, c])], fill_opacity=0.3,
                           stroke_width=0).move_to(mag_cell(r, c))
                t.ss_unhappy = False
                mtiles[(r, c)] = t
                arr.append(FadeIn(t))
            self.play(b_in.animate.shift(UP * 1.0).set_opacity(0),
                      *[board_fly(h, b, 1.0 if in_patch(b) else 0.3, False) for h, a, b in mv2],
                      *recap("after round 2"), *arr, *pending(), run_time=1.0)
            for h, a, b in mv2:
                self.pos[h] = b
                self.early[h] = 1
                self.tiles[h].set_z_index(0)
            self.remove(b_in)
            beat.wait_until("drops", offset=-0.45)
            self.play(*resolve_to("2", "7", "<"), ringC.animate.set_stroke(RED), mag_ring(C_),
                      ring_on(hC), run_time=0.7)
            # C's 2/7 < 1/3 then holds through the pause and into the next beat (>= 1.5 s)

        # 7 - the cascade completes ------------------------------------------------------
        with self.narrate("Now run the whole town. [pause 1.4] After round seven, nobody wants "
                          "to move.", gap=0.25) as beat:
            mag_all = VGroup(mframe, mempty, *mtiles.values(), ringC, subj, caps[-1], F["num"],
                             F["bar"], F["den"], F["rel"], f_third)
            self.round_no.set_value(1)
            # the corner's replay folds away first, so the growing board never runs under it
            beat.wait_until("Now", offset=-0.1)
            self.play(FadeOut(mag_all), FadeOut(src), run_time=0.45)
            # back to the whole town after round one (the replayed movers are already home):
            # the board returns to full size and full strength, the HUD returns
            in_now = sorted(h for h, rc in self.pos.items() if in_patch(rc))
            unpark, unpark_done = self.relayout(
                (GX, GY), 1.0, opacity={h: 1.0 for h, t in self.tiles.items()
                                        if t.get_fill_opacity() < 0.99},
                rings={h: (h in self.cur_unhappy and h not in self.early) for h in in_now})
            fw1 = N * P + 0.07
            tag_home = [GX - fw1 / 2 + sim_tag.width / 2, GY - fw1 / 2 - 0.22 - sim_tag.height / 2, 0]
            self.moves_n.set_value(len(self.rounds[0]))
            self.play(*self.ctx_fade(meter_ink, 1.0), unpark,
                      sim_tag.animate.move_to(tag_home),
                      FadeIn(self.counter), FadeIn(self.plan), FadeIn(self.round_lab),
                      FadeIn(self.moves_lab), run_time=0.8)
            unpark_done()
            # rounds 2-7 run in the silence; the counter reaches 0 on "nobody"
            total = beat.until("nobody", offset=-0.25, min_time=2.6)
            weights = np.array([2.4, 1.6, 1.15, 0.95, 0.8, 0.7])
            durs = total * weights / weights.sum()
            for k, d in zip(range(1, 7), durs):
                self.round_no.set_value(k + 1)
                self.play_round(k, run_time=float(d), flight=min(0.8, float(d) * 0.6))
            assert len(self.cur_unhappy) == 0
            self.pulse(self.counter, 1.1)
            beat.wait_until("move", offset=0.1)
            self.pulse(self.ink_lab, 1.12)

        # 8 - the tipping curve ------------------------------------------------------------
        ax = axes((0, 60), (40, 100), x_ticks=[0, 20, 40, 60], y_ticks=[40, 60, 80, 100],
                  x_length=7.0, y_length=4.5, x_label="demanded (% of neighbors)",
                  y_label="neighbors matching (%)")
        ax.shift(np.array([-5.3, -1.62, 0]) - ax.c2p(0, 40))
        ax.x_title.set_color(PURPLE)
        ax.y_title.set_color(INK)
        base = DashedLine(ax.c2p(0, 50), ax.c2p(60, 50), color=GRAY, stroke_width=2,
                          dash_length=0.08)
        base_lab = text("random mix", size=TEXT_LABEL_MIN, color=GRAY)
        base_lab.next_to(ax.c2p(2.5, 50), DOWN, buff=0.25, aligned_edge=LEFT)
        TS = 2.0                                   # thumbnail side
        TOP = np.array([5.3, 2.15, 0])
        BOT = np.array([5.3, -2.0, 0])
        s_thumb = TS / (N * P + 0.07)
        rng = np.random.default_rng(7)
        cloud, means = {}, {}
        for tval, vals in sorted(self.sweep.items()):
            xs = 100 * tval + rng.uniform(-0.6, 0.6, len(vals))
            dots_ = VGroup(*[Dot(ax.c2p(x, 100 * v), radius=0.05, color=INK, fill_opacity=0.38)
                             for x, v in zip(xs, vals)])
            x = 100 * tval
            whisk = Line(ax.c2p(x, 100 * min(vals)), ax.c2p(x, 100 * max(vals)), color=GRAY,
                         stroke_width=2)
            mtick = Line(ax.c2p(x, 100 * np.mean(vals)) + LEFT * 0.17,
                         ax.c2p(x, 100 * np.mean(vals)) + RIGHT * 0.17, color=INK, stroke_width=5)
            cloud[tval] = VGroup(whisk, dots_, mtick)
            means[tval] = mtick
        ours = Dot(ax.c2p(100 / 3, 100 * self.shareF), radius=0.08, color=INK)
        dot_note = text("each dot: one simulated town", size=TEXT_LABEL_MIN, color=GRAY)
        dot_note.next_to(ax.c2p(0, 100), RIGHT, buff=0.25).shift(DOWN * 0.12)

        def thumb_label(frac_tex, share):
            return VGroup(MathTex(frac_tex, font_size=44, color=PURPLE),
                          MathTex(r"\rightarrow", font_size=36, color=GRAY),
                          MathTex(rf"{round(100 * share)}\%", font_size=44, color=INK)
                          ).arrange(RIGHT, buff=0.18)
        top_lab = thumb_label(r"\tfrac{1}{3}", self.shareF)
        top_lab.next_to(TOP + LEFT * TS / 2, LEFT, buff=0.3)
        bot_lab = thumb_label(r"\tfrac{1}{4}", self.q_share)
        bot_lab.next_to(BOT + LEFT * TS / 2, LEFT, buff=0.3)

        # the HUD leaves and the finished town shrinks into its slot (the meter is gone before
        # the town reaches it). The axes start drawing halfway through the shrink: the x-axis
        # (y = -1.62) and the y-axis (x = -5.3) are drawn first, while the town is already
        # above y = -0.74 and right of x = -0.92; the titles come last, after it has landed.
        # So the frame never holds a lone thumbnail, and the chart is complete before "That
        # whole town ... this chart"
        self.play(FadeOut(self.meter, run_time=0.4), FadeOut(self.counter, run_time=0.4),
                  FadeOut(self.plan, run_time=0.4), FadeOut(self.round_lab, run_time=0.4),
                  FadeOut(self.moves_lab, run_time=0.4), FadeOut(sim_tag, run_time=0.4),
                  self.town.animate(run_time=0.9, rate_func=SMOOTH).scale(s_thumb).move_to(TOP),
                  Succession(Wait(run_time=0.45), Create(ax, run_time=0.8)))
        with self.narrate("That whole town is one point on this chart.", gap=1.2) as beat:
            # (the town's copy flies left past where "1/3 -> 76%" will sit: the label arrives
            # only after the copy has landed, so nothing ever flies through it). It leaves on
            # "whole" (the chart is already drawn) and lands on "point"
            beat.wait_until("whole", offset=-0.1)
            self.play(TransformFromCopy(self.town, ours),
                      run_time=beat.until("point", offset=0.15, min_time=0.6))
            # thirty simulated towns per demand: the note says it, the dots show it (no words)
            beat.wait_until("chart", offset=-0.1)
            self.play(LaggedStart(*[FadeIn(cloud[t], lag_ratio=0.02) for t in sorted(cloud)],
                                  lag_ratio=0.25),
                      Create(base), FadeIn(base_lab), FadeIn(dot_note),
                      FadeIn(top_lab, shift=0.1 * LEFT), run_time=1.5)

        qtiles = {}
        for hid, (r, c) in self.start_pos.items():
            t = Square(TILE, fill_color=COL[self.colour[hid]], fill_opacity=1, stroke_width=0)
            t.move_to(cell(r, c))
            qtiles[hid] = t
        qboard = VGroup(*[qtiles[h] for h in sorted(qtiles)])
        qframe = Rectangle(width=N * P + 0.07, height=N * P + 0.07, stroke_color=DIM,
                           stroke_width=2).move_to([GX, GY, 0])
        qtown = VGroup(qframe, qboard).scale(s_thumb).move_to(BOT)
        q_start = {h: qtiles[h].get_center() for h in qtiles}

        def qcell(r, c):
            return BOT + (cell(r, c) - np.array([GX, GY, 0])) * s_thumb
        q_end = {h: qcell(*self.q_pos[h]) for h in qtiles}
        q_moving = [h for h in qtiles if self.q_pos[h] != self.start_pos[h]]
        qpt = Dot(ax.c2p(25, 100 * self.q_share), radius=0.08, color=INK)

        # the two spoken columns: each demand flies from its thumbnail label to a PURPLE mark
        # at its column (inside the plot, between the x-axis and the random-mix line), and
        # that column brightens while the others dim to 40 %
        k_q = min(cloud, key=lambda t: abs(t - 0.25))
        k_t = min(cloud, key=lambda t: abs(t - 1 / 3))
        mark_y = (ax.c2p(0, 40)[1] + ax.c2p(0, 50)[1]) / 2
        q_mark = MathTex(r"\tfrac{1}{4}", font_size=32, color=PURPLE).move_to(
            [ax.c2p(25, 40)[0], mark_y, 0])
        t_mark = MathTex(r"\tfrac{1}{3}", font_size=32, color=PURPLE).move_to(
            [ax.c2p(100 / 3, 40)[0], mark_y, 0])
        for m_ in (q_mark, t_mark):
            assert m_.get_bottom()[1] - ax.c2p(0, 40)[1] >= 0.15 and \
                ax.c2p(0, 50)[1] - m_.get_top()[1] >= 0.15, m_.get_top()

        def col_state(bright):
            """Columns in `bright` at full strength (dots 0.6), the rest at 40 %."""
            anims = []
            for t, c_ in cloud.items():
                on = t in bright
                anims += [c_[0].animate.set_stroke(opacity=1.0 if on else 0.4),
                          c_[1].animate.set_fill(opacity=0.6 if on else 0.15),
                          c_[2].animate.set_stroke(opacity=1.0 if on else 0.4)]
            return anims

        with self.narrate("Demand a quarter, and the same starting town barely sorts: "
                          "fifty-eight percent. Demand a third, and it jumps to seventy-six. "
                          "[pause 0.9]", gap=0.15) as beat:
            self.play(FadeIn(qtown, shift=0.2 * LEFT), FadeIn(bot_lab[0], shift=0.2 * LEFT),
                      run_time=beat.until("quarter", offset=-0.1, min_time=0.4))
            self.play(TransformFromCopy(bot_lab[0], q_mark, path_arc=-0.9), *col_state({k_q}),
                      run_time=0.7)

            def qrun(group, alpha):
                a = smooth(alpha)
                for h in q_moving:
                    qtiles[h].move_to(q_start[h] + (q_end[h] - q_start[h]) * a)
            self.play(UpdateFromAlphaFunc(qboard, qrun),
                      run_time=beat.until("fifty", offset=-0.1, min_time=1.5), rate_func=linear)
            # the copy flies over the spot where "-> 58%" sits: the result arrives after it lands
            self.play(TransformFromCopy(qtown, qpt), run_time=0.8)
            self.play(FadeIn(VGroup(bot_lab[1], bot_lab[2]), shift=0.1 * LEFT), run_time=0.5)
            beat.wait_until("third", offset=-0.25)
            self.play(TransformFromCopy(top_lab[0], t_mark, path_arc=0.6), *col_state({k_q, k_t}),
                      run_time=0.7)
            beat.wait_until("jumps", offset=-0.1)
            self.play(Indicate(ours, color=INK, scale_factor=1.8), run_time=0.8)

        # why the jump: the share ladder of the random start ---------------------------------
        # Its own chart, larger and higher than the dot chart (whose x-axis line becomes its
        # baseline): bars stand on a GRAY baseline; counts sit centred above their bars; rung
        # fractions sit in one row under the baseline; the demand is a PURPLE caret between the
        # baseline and that row, plus a PURPLE outline on the threshold bar (never drawn inside
        # a bar).
        rungs = sorted(f for f in self.ladder if f <= Fraction(3, 5))
        LX0, LXS = -6.08, 13.0                    # x of share 0; units per unit of share
        BL, HMAX, BW = -0.85, 3.2, 0.17           # baseline y; tallest bar; bar width
        HS = HMAX / max(self.ladder[f] for f in rungs)   # units per household

        def lx(f):
            return LX0 + float(f) * LXS
        F14, F27, F13, F38, F35 = (Fraction(1, 4), Fraction(2, 7), Fraction(1, 3),
                                   Fraction(3, 8), Fraction(3, 5))
        assert rungs[0] == 0 and rungs[-1] == F35 and len(rungs) == 14
        lbase = Line([lx(0) - 0.25, BL, 0], [lx(F35) + 0.25, BL, 0], color=AXIS, stroke_width=2.5)
        x_line = Line(ax.c2p(0, 40), ax.c2p(60, 40), color=AXIS, stroke_width=2.5)  # = the axes
        bars = {}
        for f in rungs:
            h = self.ladder[f] * HS
            b = Rectangle(width=BW, height=h, stroke_width=0, fill_color=GRAY, fill_opacity=0.9)
            b.move_to([lx(f), BL + h / 2, 0])
            b.set_z_index(2)
            bars[f] = b
        bar_grp = VGroup(*bars.values())
        b14, b27, b38 = bars[F14], bars[F27], bars[F38]
        assert (self.ladder[F14], self.ladder[F27], self.ladder[F38]) == (76, 67, 125)
        # the vertical's quantity name, where a y-axis title sits (top of the left end)
        bars_note = text("households (simulated start)", size=TEXT_LABEL_MIN, color=INK)
        bars_note.move_to([lx(0) - 0.08 + bars_note.width / 2, BL + HMAX + 0.45, 0])
        assert bars_note.get_bottom()[1] > max(b.get_top()[1] for b in bars.values()
                                               if b.get_center()[0] < bars_note.get_right()[0] + 0.2) + 0.5
        chart_ctx = [*cloud.values(), ours, qpt, base, base_lab, dot_note,
                     ax.y_axis, ax.y_title, ax.x_axis]
        # the two thumbnails and their labels leave the ladder (one focal region); they come
        # back with the dot chart
        thumbs = [self.town, top_lab, qtown, bot_lab]
        xt_share = text("share of neighbors matching", size=28, color=INK)

        def count_lab(f):
            return MathTex(str(self.ladder[f]), font_size=32, color=GRAY).next_to(
                bars[f], UP, buff=0.22)
        c14, c27, c38 = count_lab(F14), count_lab(F27), count_lab(F38)
        assert c27.get_left()[0] - c14.get_right()[0] >= 0.15, (c14.get_right(), c27.get_left())

        # under-baseline row: rung fractions (INK), the demand's fraction (PURPLE), the ends
        CARET_H = 0.18
        ROW_TOP = BL - 0.08 - CARET_H - 0.18

        def under(tex, f, color=INK, size=32):
            m = MathTex(tex, font_size=size, color=color)
            return m.move_to([lx(f), ROW_TOP - m.height / 2, 0])
        l27 = under(r"\frac{2}{7}", F27)
        l38 = under(r"\frac{3}{8}", F38)
        row_mid = l27.get_y()
        end0 = MathTex(r"0\%", font_size=28, color=GRAY).move_to([lx(0), row_mid, 0])
        end60 = MathTex(r"60\%", font_size=28, color=GRAY).move_to([lx(F35), row_mid, 0])
        xt_share.move_to([lx(F35) + 0.25 - xt_share.width / 2,
                          l27.get_bottom()[1] - 0.2 - xt_share.height / 2, 0])
        assert xt_share.get_bottom()[1] >= -3.2, xt_share.get_bottom()
        assert bot_lab.get_left()[0] - max(end60.get_right()[0], xt_share.get_right()[0]) >= 0.3

        def caret_at(d, opacity=1.0):
            t = Triangle().set_stroke(width=0).set_fill(PURPLE, opacity=opacity)
            t.stretch_to_fit_height(CARET_H).stretch_to_fit_width(0.22)
            return t.move_to([lx(d), BL - 0.08 - CARET_H / 2, 0]).set_z_index(3)

        def outline_on(f, dashed=False, opacity=1.0):
            """Three sides of a PURPLE box around the threshold bar, open at the baseline."""
            b = bars[f]
            x0, x1 = b.get_left()[0] - 0.05, b.get_right()[0] + 0.05
            y1 = b.get_top()[1] + 0.05
            pts = [np.array([x0, BL + 0.03, 0]), np.array([x0, y1, 0]), np.array([x1, y1, 0]),
                   np.array([x1, BL + 0.03, 0])]
            m = VMobject().set_points_as_corners(pts)
            if dashed:
                m = DashedVMobject(m, num_dashes=10, dashed_ratio=0.55)
            return m.set_stroke(PURPLE, width=3, opacity=opacity).set_fill(opacity=0).set_z_index(3)

        caret = caret_at(1 / 3)
        out13 = outline_on(F13)
        dlab = under(r"\frac{1}{3}", F13, PURPLE, 34)
        q_caret = caret_at(0.25, 0.5)
        q_out = outline_on(F14, dashed=True, opacity=0.6)
        q_lab = under(r"\frac{1}{4}", F14, PURPLE, 34).set_opacity(0.5)
        for a_, b_ in ((q_lab, l27), (l27, dlab), (dlab, l38)):
            assert b_.get_left()[0] - a_.get_right()[0] >= 0.15, (a_, b_)
        assert c14.get_bottom()[1] - q_out.get_top()[1] >= 0.15

        unh_word = text("unhappy", size=TEXT_LABEL_MIN, color=RED)
        unh_num = DecimalNumber(self.unh_t, num_decimal_places=0, font_size=40, color=RED)
        unh_lab = VGroup(unh_word, unh_num).arrange(RIGHT, buff=0.2)
        unh_num.align_to(unh_word, DOWN)
        low_top = max(bars[f].get_top()[1] for f in rungs if f < Fraction(1, 5) + Fraction(1, 100))
        unh_lab.move_to([lx(0) - 0.08 + unh_lab.width / 2, low_top + 0.3 + unh_lab.height / 2, 0])
        assert unh_lab.get_right()[0] < b14.get_left()[0] - 0.3

        def unh_fix(m):
            unh_num.next_to(unh_word, RIGHT, buff=0.2).align_to(unh_word, DOWN)

        # one lost match moves a household from 3/8 down to 2/7
        drop = CurvedArrow(c38.get_top() + UP * 0.17 + LEFT * 0.04, c27.get_top() + UP * 0.17,
                           angle=PI / 2, color=GRAY, stroke_width=3, tip_length=0.18)
        drop_lab = text("lose one match", size=TEXT_LABEL_MIN, color=GRAY).next_to(drop, UP, buff=0.22)
        assert drop_lab.get_top()[1] < bars_note.get_bottom()[1] - 0.15

        def ladder_state(d):
            """Bars strictly left of the demand are unhappy (share < demand); returns count."""
            n = 0
            for f, b in bars.items():
                red = float(f) < d - 1e-9
                b.set_fill(RED if red else GRAY)
                n += self.ladder[f] if red else 0
            return n

        with self.narrate("To see why that happens, sort the random start by each household's "
                          "share of matching neighbors. With at most eight neighbors, these are "
                          "the only shares up to sixty percent.") as beat:
            # the dot chart leaves completely, and its x-axis line becomes the ladder's baseline
            beat.wait_until("sort", offset=-0.2)
            self.add(x_line)
            # one move (round 5 cont.; the frame never holds a lone line). In seconds:
            #   0.00-0.35  the dot chart and thumbnails fade out completely
            #   0.15-0.75  its x-axis line rises into the ladder's baseline; it reaches the
            #              "random mix" / 1/4 / 1/3 row (y = -1.25) at ~0.45 s and the dot rows
            #              only at the end, both long gone (nothing moves through anything)
            #   0.40-1.00  both ladder titles fade in (the old x title is gone by 0.35 s)
            #   0.50-1.34  the bars sprout from the line, left to right, standing on it
            T_ALL = max(2.0, beat.until("With", offset=-0.15))
            L0, L1 = 0.1, 0.6                           # line start; line duration
            B0, BDUR = 0.25, 0.9                        # first bar; one bar's growth
            BLAG = (T_ALL - B0 - BDUR) / (len(rungs) - 1)   # left to right, as the line speaks
            assert BLAG > 0 and B0 + BLAG * (len(rungs) - 1) + BDUR <= T_ALL + 1e-6
            xs0, xe0 = x_line.get_start().copy(), x_line.get_end().copy()
            xs1, xe1 = lbase.get_start().copy(), lbase.get_end().copy()
            hfull = {f: bars[f].height for f in rungs}
            for f in rungs:
                bars[f].stretch_to_fit_height(1e-3).move_to([lx(f), xs0[1], 0])

            def rise(m, a):
                u = smooth(float(np.clip((a * T_ALL - L0) / L1, 0.0, 1.0)))
                m.put_start_and_end_on(xs0 + (xs1 - xs0) * u, xe0 + (xe1 - xe0) * u)

            def sprout(_m, a):
                y = x_line.get_start()[1]           # bars stand on the line wherever it is
                for i, f in enumerate(rungs):
                    v = smooth(float(np.clip((a * T_ALL - B0 - BLAG * i) / BDUR, 0.0, 1.0)))
                    h = max(hfull[f] * v, 1e-3)
                    bars[f].stretch_to_fit_height(h).move_to([lx(f), y + h / 2, 0])
            self.play(*[m.animate(run_time=0.3).set_opacity(0) for m in chart_ctx],
                      ax.x_title.animate(run_time=0.3).set_opacity(0),
                      *[FadeOut(m, run_time=0.3) for m in thumbs],
                      FadeOut(q_mark, run_time=0.3), FadeOut(t_mark, run_time=0.3),
                      UpdateFromAlphaFunc(x_line, rise, run_time=T_ALL, rate_func=linear),
                      UpdateFromAlphaFunc(bar_grp, sprout, run_time=T_ALL, rate_func=linear),
                      Succession(Wait(run_time=0.35), FadeIn(xt_share, run_time=0.6)),
                      Succession(Wait(run_time=0.35), FadeIn(bars_note, run_time=0.6)))
            for f in rungs:
                assert abs(bars[f].height - hfull[f]) < 1e-6 and abs(bars[f].get_bottom()[1] - BL) < 1e-6
            beat.wait_until("these", offset=-0.2)
            # point at every value that occurs, left to right
            self.play(LaggedStart(*[b.animate(rate_func=there_and_back).stretch(
                1.18, 1, about_edge=DOWN) for b in bar_grp], lag_ratio=0.12), run_time=1.3)
            beat.wait_until("sixty", offset=-0.2)
            self.play(FadeIn(end0, shift=0.1 * UP), FadeIn(end60, shift=0.1 * UP), run_time=0.6)

        # the household that started our corner's chain (A), at the random start
        WP, WT, WFS = 0.42, 0.36, 56
        w_patch = VGroup()
        w_gold, w_all = [], []
        w_centre = None
        for (r, c) in [A_] + nb8(A_):
            pos = np.array([(c - A_[1]) * WP, -(r - A_[0]) * WP, 0])
            w_patch.add(Square(WT, stroke_color=DIM, stroke_width=2).move_to(pos))
            v = int(self.g0[r, c])
            if v:
                t = Square(WT, fill_color=COL[v], fill_opacity=1, stroke_width=0).move_to(pos)
                t.ss_unhappy = False
                w_patch.add(t)
                if (r, c) == A_:
                    w_centre = t
                else:
                    w_all.append(t)
                    if v == 2:
                        w_gold.append(t)
        assert len(w_gold) == 2 and len(w_all) == 7 and int(self.g0[A_]) == 2
        set_unhappy(w_centre, True, width=4, base=WT)
        w_patch.add(Square(3 * WP + 0.05, stroke_color=INK, stroke_width=3))

        def wpiece(t, color=INK):
            return MathTex(t, font_size=WFS, color=color)
        w_num, w_den = wpiece("2", YELLOW), wpiece("7")
        w_bar = Line(LEFT * 0.3, RIGHT * 0.3, stroke_width=3.5, color=INK)
        w_frac = VGroup(w_num, w_bar, w_den).arrange(DOWN, buff=0.09)
        w_rel = wpiece("<")
        w_t = MathTex(r"\frac{1}{3}", font_size=WFS, color=PURPLE)
        w_eq = VGroup(w_frac, w_rel, w_t).arrange(RIGHT, buff=0.22)
        why = VGroup(w_patch, w_eq).arrange(RIGHT, buff=0.3)
        # the right column the thumbnails vacated, beside the bars' middle
        why_x0 = lx(F35) + 0.25 + 0.6
        why.move_to([(why_x0 + 6.3) / 2, BL + 1.15, 0])
        assert why.get_right()[0] <= 6.35 and why.get_left()[0] >= why_x0 - 0.05, why.get_left()
        assert why.get_bottom()[1] > BL + 0.15

        # (round 5 cont.: the spoken "two hundred and thirty-eight" was cut: "unhappy 238" is on
        # screen, and the number had already been spoken at 0:41)
        with self.narrate("At a third, everyone left of it is unhappy, including the neighbor "
                          "that started our corner's chain, at two sevenths.") as beat:
            beat.wait_until("third", offset=-0.25)
            self.play(FadeIn(caret, shift=0.12 * UP), Create(out13), FadeIn(dlab, shift=0.1 * UP),
                      run_time=0.7)
            beat.wait_until("left", offset=-0.2)
            red_now = [b for f, b in bars.items() if float(f) < 1 / 3]
            self.play(LaggedStart(*[b.animate.set_fill(RED) for b in reversed(red_now)],
                                  lag_ratio=0.15),
                      FadeIn(unh_lab, shift=0.1 * DOWN), run_time=1.2)
            beat.wait_until("including", offset=-0.2)
            self.play(FadeIn(w_patch, scale=0.6), run_time=0.6)
            self.fly_into([(w_gold, w_num), (w_all, w_den)], extra=[Create(w_bar)], run_time=1.0)
            # its demand comes from the town that demanded a third (top right), a short clear path
            # its demand is the caret's 1/3 (the thumbnails have left the ladder)
            self.play(Write(w_rel), TransformFromCopy(dlab, w_t), run_time=0.9)
            beat.wait_until("two sevenths", offset=-0.2)
            self.play(FadeIn(l27, shift=0.1 * UP), FadeIn(c27, shift=0.1 * DOWN), run_time=0.5)
            self.flash_box(VGroup(b27, c27), w_frac, color=INK, buff=0.06, run_time=1.0)

        with self.narrate("Every household at three eighths is one lost match away from it.",
                          gap=0.45) as beat:
            beat.wait_until("three", offset=-0.2)
            # one focal point: the bars. A's patch (the last sentence's subject) dims to 60 % until
            # the slide brings it back for "that chain never starts"
            self.play(FadeIn(l38, shift=0.1 * UP), FadeIn(c38, shift=0.1 * DOWN),
                      *self.soft_dim(why, 0.6), run_time=0.6)
            beat.wait_until("lost", offset=-0.3)
            self.play(Create(drop), FadeIn(drop_lab, shift=0.05 * DOWN),
                      run_time=beat.until("it", offset=0.1, min_time=0.9))

        with self.narrate("At a quarter, how many would start unhappy? [pause 1.5]",
                          gap=0.25) as beat:
            beat.wait_until("quarter", offset=-0.25)
            self.play(FadeIn(q_caret, shift=0.12 * UP), Create(q_out), FadeIn(q_lab, shift=0.1 * UP),
                      FadeIn(c14, shift=0.1 * DOWN), run_time=0.7)
            beat.wait_until("unhappy", offset=-0.2)
            self.pulse(unh_lab, 1.1, run_time=0.8)

        out14 = outline_on(F14)
        with self.narrate("Only these two bars change sides, and they're tall: just "
                          "ninety-five start unhappy, and that chain never starts. [pause 0.9]") as beat:
            # the threshold's outline and label lift off; the caret carries the demand to 1/4;
            # the 3/8 -> 2/7 arrow goes with it (at 1/4 the 2/7 bar is content)
            self.play(FadeOut(dlab), FadeOut(out13), run_time=0.3)
            unh_num.add_updater(lambda m: unh_fix(unh_lab))
            dline_t = ValueTracker(1 / 3)
            caret.add_updater(lambda m: m.move_to([lx(dline_t.get_value()), m.get_y(), 0]))

            def slide(mob, alpha):
                d = 1 / 3 + (1 / 4 - 1 / 3) * smooth(alpha)
                dline_t.set_value(d)
                unh_num.set_value(ladder_state(d if alpha < 1 else 0.25))
            self.play(UpdateFromAlphaFunc(bar_grp, slide), FadeOut(drop), FadeOut(drop_lab),
                      *self.soft_dim(why, 1.0),
                      run_time=beat.until("change", offset=0.1, min_time=1.2), rate_func=linear)
            caret.clear_updaters()
            unh_num.clear_updaters()
            assert int(unh_num.get_value()) == self.unh_q
            self.remove(q_caret)
            self.play(FadeOut(q_out), Create(out14), q_lab.animate.set_opacity(1),
                      self.swap(w_t, MathTex(r"\frac{1}{4}", font_size=WFS, color=PURPLE)),
                      self.swap(w_rel, wpiece(r"\geq")),
                      UpdateFromAlphaFunc(w_centre, lambda m, a: set_unhappy(
                          m, a < 0.5, width=4, base=WT)), run_time=0.6)
            beat.wait_until("tall", offset=-0.2)
            self.flash_box(VGroup(b14, c14, b27, c27), buff=0.08, run_time=1.0)
            beat.wait_until("ninety", offset=-0.2)
            self.pulse(unh_lab, 1.1, run_time=0.8)
            beat.wait_until("never", offset=-0.2)
            self.flash_box(w_eq, buff=0.08)

        # 9 - payoff: Schelling ---------------------------------------------------------
        # his band is a different model's result: a light hatched band (not a solid block),
        # and while it is shown our own dots and mean ticks dim to 35 %
        bx0, bx1 = ax.c2p(35, 40)[0], ax.c2p(50, 40)[0]
        by0, by1 = ax.c2p(0, 40)[1], ax.c2p(0, 100)[1]
        band = Rectangle(width=bx1 - bx0, height=by1 - by0, stroke_width=0, fill_color=GRAY,
                         fill_opacity=0.07)
        band.move_to([(bx0 + bx1) / 2, (by0 + by1) / 2, 0])
        band.set_z_index(-1)
        band_w = band.width
        band_l = band.get_left()
        hatch = VGroup()
        HD = 0.22                                       # hatch spacing along x
        H = by1 - by0
        u = bx0 - H
        while u < bx1:
            # the 45-degree line from (u, by0) to (u + H, by1), clipped to [bx0, bx1]
            t0 = max(0.0, (bx0 - u) / H)
            t1 = min(1.0, (bx1 - u) / H)
            if t1 - t0 > 1e-3:
                hatch.add(Line([u + t0 * H, by0 + t0 * H, 0], [u + t1 * H, by0 + t1 * H, 0]))
            u += HD
        hatch.set_stroke(GRAY, width=2, opacity=0.5).set_z_index(-1)

        def bracket(x0, x1, y=96.5):
            p0, p1 = ax.c2p(x0, y), ax.c2p(x1, y)
            return VGroup(Line(p0, p1), Line(p0 + DOWN * 0.1, p0 + UP * 0.1),
                          Line(p1 + DOWN * 0.1, p1 + UP * 0.1)).set_stroke(GRAY, 3)
        # each bracket's label sits on the bracket's own row, to its left, inside the plot
        ours_br = bracket(25, 100 / 3)
        ours_br_lab = text("our jump", size=TEXT_LABEL_MIN, color=GRAY).next_to(ours_br, LEFT, buff=0.2)
        his_br = bracket(35, 50)
        band_lab = text("Schelling: 35–50%", size=TEXT_LABEL_MIN, color=GRAY)
        band_lab.next_to(his_br, LEFT, buff=0.2)
        # (round 5 cont.: the rules label "nearest move · 25–30% empty" is gone. At the new label
        # floor (Text 27) it no longer fits left of his band, and it only repeated the narration)
        assert band_lab.get_left()[0] >= ax.c2p(0, 40)[0] + 0.2, band_lab.get_left()
        assert band_lab.get_top()[1] <= ax.y_title.get_bottom()[1] - 0.2
        assert band_lab.get_right()[0] <= bx0 - 0.15 and ours_br_lab.get_left()[0] >= ax.c2p(0, 40)[0] + 0.2
        cite1 = citation("Schelling, 1971 · Journal of Mathematical Sociology")
        cite1_ul = underline(cite1, color=GRAY, buff=0.05, stroke_width=3)
        assert cite1_ul.get_bottom()[1] >= -3.2
        ladder_lab = VGroup(bars_note, caret, out14, q_lab, l27, l38, c14, c27, c38, unh_lab, why,
                            end0, end60)
        with self.narrate("In his 1971 paper, Thomas Schelling ran this model. His households "
                          "moved to the nearest suitable square, on emptier boards, and there the "
                          "jump came later, between about a third and a half.") as beat:
            # the 2:19 morph in reverse: bars sink into the baseline, the baseline becomes the
            # x-axis again, and only then does the dot chart come back (never both at once)
            # (the ladder's x title leaves with the bars, before the chart's title returns: the
            # two titles never overlap; the thumbnails return as the baseline moves)
            # (the two thumbnails return while the bars sink: their column is clear of the
            # ladder, and the frame is never a lone line)
            self.play(*[b.animate.stretch_to_fit_height(0.01).move_to([b.get_x(), BL, 0])
                        for b in bar_grp], FadeOut(ladder_lab), FadeOut(xt_share),
                      *[FadeIn(m) for m in thumbs], run_time=0.5)
            self.remove(bar_grp)
            self.play(Transform(x_line, Line(ax.c2p(0, 40), ax.c2p(60, 40), color=AXIS,
                                             stroke_width=2.5)),
                      ax.x_title.animate.set_opacity(1), run_time=0.6)
            # ("random mix" stays out from here on: fewer words while Schelling's labels show)
            restore = [m.animate.set_opacity(1) for m in [ours, qpt, base, ax.y_axis,
                                                          ax.y_title, ax.x_axis]]
            for c_ in cloud.values():                 # whisker and mean tick solid, dots translucent
                restore += [c_[0].animate.set_opacity(1), c_[1].animate.set_opacity(0.38),
                            c_[2].animate.set_opacity(1)]
            # the source arrives with the chart it belongs to (just after "paper"); the two
            # towns come back to their slots
            self.play(*restore, FadeIn(cite1, shift=0.1 * UP), run_time=0.7)
            self.remove(x_line)
            beat.wait_until("model", offset=-0.2)
            self.flash_box(self.town, qtown, buff=0.05, run_time=1.0)
            beat.wait_until("His", occurrence=2, offset=-0.1)
            self.play(Create(ours_br), FadeIn(ours_br_lab), run_time=0.8)
            # his rules come from his paper: its citation is underlined as they are spoken
            beat.wait_until("nearest", offset=-0.2)
            self.play(Create(cite1_ul), run_time=0.8)
            # one thing at a time on the label row: our label leaves, the bracket slides to his
            # range, and only when it has stopped does his label arrive
            beat.wait_until("jump", offset=-0.15)
            self.play(FadeOut(ours_br_lab), run_time=0.3)
            self.play(ReplacementTransform(ours_br, his_br), run_time=0.6)
            self.play(FadeIn(band_lab, shift=0.1 * LEFT), run_time=0.4)
            beat.wait_until("between", offset=-0.1)
            band.stretch_to_fit_width(0.01).move_to(band_l, aligned_edge=LEFT)
            self.add(band)

            def grow(m, a):
                m.stretch_to_fit_width(max(0.01, band_w * a)).move_to(band_l, aligned_edge=LEFT)
            ours_dim = []
            for c_ in cloud.values():
                ours_dim += [c_[0].animate.set_stroke(opacity=0.3),
                             c_[1].animate.set_fill(opacity=0.08),
                             c_[2].animate.set_stroke(opacity=0.3)]
            # our two towns' dots (1/4 -> 58 %, 1/3 -> 76 %) stay at full strength: they are the
            # ends of "our jump", left of his band, and they are tied to the two thumbnails
            self.play(UpdateFromAlphaFunc(band, grow),
                      LaggedStart(*[Create(l) for l in hatch], lag_ratio=0.15), *ours_dim,
                      run_time=beat.until("half", end=True, offset=0.05, min_time=1.5),
                      rate_func=SMOOTH)

        # 10 - the test: two towns, one picture ---------------------------------------------
        ZS = 0.76
        LPOS, RPOS = np.array([-3.45, 0.35, 0]), np.array([3.45, 0.35, 0])
        ztiles = VGroup()
        for r, c in np.argwhere(self.gZ > 0):
            ztiles.add(Square(TILE, fill_color=COL[int(self.gZ[r, c])], fill_opacity=1,
                              stroke_width=0).move_to(cell(r, c)))
        zframe = Rectangle(width=N * P + 0.07, height=N * P + 0.07, stroke_color=DIM,
                           stroke_width=2).move_to([GX, GY, 0])
        # the rule's zone boundaries: edges between squares of differently marked zones
        zlines = VMobject(stroke_color=INK, stroke_width=3)
        for r in range(N):
            for c in range(N):
                p = cell(r, c)
                if c + 1 < N and self.zone[r, c] != self.zone[r, c + 1]:
                    zlines.start_new_path(p + np.array([P / 2, P / 2, 0]))
                    zlines.add_line_to(p + np.array([P / 2, -P / 2, 0]))
                if r + 1 < N and self.zone[r, c] != self.zone[r + 1, c]:
                    zlines.start_new_path(p + np.array([-P / 2, -P / 2, 0]))
                    zlines.add_line_to(p + np.array([P / 2, -P / 2, 0]))
        ztown = VGroup(zframe, ztiles, zlines)
        ztown.scale(ZS).move_to(LPOS)
        zlines.set_stroke(opacity=0)

        def match_lab(share, town_pos):
            g = VGroup(MathTex(rf"{round(100 * share)}\%", font_size=44, color=INK),
                       text("match", size=28)).arrange(RIGHT, buff=0.14)
            g[1].align_to(g[0], DOWN)
            return g.move_to(town_pos + DOWN * (N * P * ZS / 2 + 0.42))
        zmatch = match_lab(self.shareZ, LPOS)
        omatch = match_lab(self.shareF, RPOS)

        board_top = RPOS[1] + (N * P + 0.07) * ZS / 2
        HEAD_GAP = 0.25

        def demand_lab(tex, town_pos, rule=False):
            """Header centred on its board; the word 'demanded' sits on one shared baseline,
            HEAD_GAP above the boards.  With rule=True the GRAY suffix is part of the same
            Text, so its baseline matches exactly."""
            words = "demanded · placed by a rule" if rule else "demanded"
            kw = {"t2c": {"· placed by a rule": GRAY}} if rule else {}
            m = MathTex(tex, font_size=44, color=PURPLE)
            t = text(words, size=28, color=PURPLE, **kw)
            g = VGroup(m, t).arrange(RIGHT, buff=0.16)
            word = t[:8]
            t.shift(UP * (m.get_bottom()[1] - word.get_bottom()[1] + 0.02))
            g.shift(RIGHT * (town_pos[0] - g.get_x()))
            g.shift(UP * (board_top + HEAD_GAP - min(m.get_bottom()[1], word.get_bottom()[1])))
            return g
        o_dem = demand_lab(r"\tfrac{1}{3}", RPOS)
        z_full = demand_lab("0", LPOS, rule=True)
        z_dem_full = VGroup(VGroup(z_full[0], z_full[1][:8]), z_full[1][8:])
        z_rule = z_dem_full[1]
        z_dem = z_dem_full[0]
        assert abs(o_dem[1][:8].get_bottom()[1] - z_dem[1].get_bottom()[1]) < 0.01
        assert z_full.get_left()[0] >= -6.4 and z_full.get_bottom()[1] >= board_top + 0.15
        assert o_dem.get_top()[1] <= 3.6
        # before the reveal, both demands wait in the gap between the towns, unassigned
        chipA = o_dem.copy().move_to([0, 1.1, 0])
        chipB = z_dem.copy().move_to([0, -0.22, 0])
        qmark = MathTex("?", font_size=56, color=GRAY).move_to([0, 0.42, 0])
        assert chipA.width < 2 * (3.45 - N * P * ZS / 2) - 0.3
        cite2 = citation("Aaronson, Hartley & Mazumder, 2021 · AEJ: Economic Policy")
        # one tag for both towns, centred in the gap on the row of their "76% match" labels
        tt_tag = text("simulated", size=22, color=GRAY).move_to([0, zmatch.get_y(), 0])
        assert tt_tag.get_left()[0] - zmatch.get_right()[0] >= 0.3
        LANE_Y = o_dem.get_y()                 # chips travel up the gap, then along this lane

        def via_gap(chip, target, run_time):
            """Up the empty gap between the towns, then sideways above them: never over tiles."""
            p0, p2 = chip.get_center().copy(), target.get_center().copy()
            p1 = np.array([p0[0], LANE_Y, 0])
            d1, d2 = np.linalg.norm(p1 - p0), np.linalg.norm(p2 - p1)

            def f(m, a):
                u = smooth(a) * (d1 + d2)
                m.move_to(p0 + (p1 - p0) * min(u / d1, 1) if u <= d1 else
                          p1 + (p2 - p1) * (u - d1) / d2)
            return UpdateFromAlphaFunc(chip, f, run_time=run_time)
        chart = VGroup(ax, base, base_lab, *cloud.values(), ours, qpt, band, hatch, band_lab, his_br, cite1_ul,
                       top_lab, bot_lab, qtown, cite1)

        # cross-fade (beat boundary): nothing tells the viewer which town is which
        self.play(FadeOut(chart), FadeOut(self.town), run_time=0.7)
        self.town.scale(ZS / s_thumb).move_to(RPOS)
        bottom_town = max(ztown.get_top()[1], self.town.get_top()[1])
        assert LANE_Y - o_dem.height / 2 - bottom_town >= 0.15, (LANE_Y, bottom_town)
        with self.narrate("Two simulated towns, both seventy-six percent. In one town, households "
                          "demand a third. In the other, nobody minds their neighbors at all. Which "
                          "one wanted a third? [pause 1.5]") as beat:
            self.play(FadeIn(ztown), FadeIn(self.town), FadeIn(tt_tag), run_time=0.9)
            beat.wait_until("both", offset=-0.2)
            self.play(FadeIn(zmatch, shift=0.1 * UP), FadeIn(omatch, shift=0.1 * UP), run_time=0.7)
            beat.wait_until("third", offset=-0.25)
            self.play(FadeIn(chipA, shift=0.1 * DOWN), run_time=0.6)
            beat.wait_until("nobody", offset=-0.2)
            self.play(FadeIn(chipB, shift=0.1 * UP), FadeIn(qmark), run_time=0.6)
            beat.wait_until("Which", offset=-0.2)
            self.play(*[m.animate(rate_func=there_and_back).scale(1.08) for m in (chipA, chipB)],
                      run_time=0.8)

        # (round 5 cont.: "It traces this to reduced credit in the areas marked in red" is folded
        # into the study's sentence as "through reduced credit", the abstract's own words; the
        # second "at all" is cut)
        with self.narrate("This one. [pause 0.2] The other was placed by a rule, with no "
                          "preferences. In real cities, one study finds that 1930s federal lending "
                          "maps increased racial segregation for decades, through reduced credit.",
                          speed=0.84, gap=0.35) as beat:
            box_o = SurroundingRectangle(self.town, color=INK, buff=0.02, stroke_width=3)
            self.play(Create(box_o), via_gap(chipA, o_dem, 1.0), FadeOut(qmark), run_time=1.0)
            self.remove(chipA)
            self.add(o_dem)
            beat.wait_until("other", offset=-0.2)
            self.play(FadeOut(box_o), zlines.animate.set_stroke(opacity=1),
                      via_gap(chipB, z_dem_full[0], 1.1), run_time=1.1)
            self.remove(chipB)
            self.add(z_dem_full[0])
            # the suffix arrives only once "0 demanded" has landed: one phrase
            self.play(FadeIn(z_rule, shift=0.1 * LEFT), run_time=0.6)
            beat.wait_until("study", offset=-0.3)
            self.play(FadeIn(cite2, shift=0.1 * UP), run_time=0.7)
            # real cities are not the toy towns: both towns dim slowly under "1930s federal
            # lending maps" (the toy rule is not a model of those maps); only the citation and
            # the two "76% match" labels (the segregation measure) stay in focus, and they pulse
            # on "segregation"
            beat.wait_until("1930s", offset=-0.2)
            self.play(ztiles.animate.set_fill(opacity=0.3), zlines.animate.set_stroke(opacity=0.3),
                      self.board.animate.set_fill(opacity=0.3),
                      run_time=beat.until("lending", end=True, offset=0.1, min_time=0.8))
            beat.wait_until("segregation", offset=-0.25)
            self.play(*[m.animate(rate_func=there_and_back).scale(1.1) for m in (zmatch, omatch)],
                      run_time=0.9)
            beat.wait_until("credit", offset=-0.2)
            cite_ul = underline(cite2, color=GRAY, buff=0.05, stroke_width=3)
            assert cite_ul.get_bottom()[1] >= -3.2
            self.play(Create(cite_ul), run_time=0.8)

        # 11 - landing: back to the opening frame ---------------------------------------------
        q_sym = MathTex("?", font_size=56, color=PURPLE)
        self.dem.set_value(1 / 3)
        self.match.set_value(self.shareF)
        self.ty.set_value(TY0)
        for m in (self.track, self.fill, self.lo, self.hi, self.mline, self.ink_lab, self.pur_lab):
            m.update()
        # the rule town and every label leave first, in the pause between the beats (round 5:
        # the growing town used to pass over them while they faded); then one move on the town:
        # it grows back home and its tiles return to full strength, landing on "first"
        self.town.generate_target()
        self.town.target.scale(1 / ZS).move_to([GX, GY, 0])
        self.town.target[1].set_fill(opacity=1.0)
        # (round 5 cont.: our town returns to full strength as the rest fades, so the one town
        # left on screen is the focus of "Look again at the first town", not a dim leftover)
        self.play(FadeOut(ztown), FadeOut(zmatch), FadeOut(omatch), FadeOut(z_dem_full[0]),
                  FadeOut(z_rule), FadeOut(tt_tag),
                  FadeOut(cite2), FadeOut(cite_ul), FadeOut(o_dem),
                  self.board.animate.set_fill(opacity=1.0), run_time=0.45)
        with self.narrate("Look again at the first town. As Schelling argued, whatever you guessed "
                          "its people demanded, the map alone could not have told you.",
                          speed=0.82) as beat:
            self.play(MoveToTarget(self.town),
                      run_time=beat.until("first", offset=-0.1, min_time=0.6))
            self.play(FadeIn(self.meter), FadeIn(sim_tag), run_time=0.7)
            beat.wait_until("Whatever", offset=-0.2)
            self.play(self.swap(self.dem_sym, q_sym),
                      self.dem.animate.set_value(self.shareF), run_time=1.6, rate_func=SMOOTH)
            beat.wait_until("not", offset=-0.2)
            self.pulse(self.pur_lab, 1.15)

        self.end_card(hold=0.6)
