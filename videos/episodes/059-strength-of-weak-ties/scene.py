"""Episode 59 - Why Acquaintances Find You Jobs.

    videos/toolkit/render.sh videos/episodes/059-strength-of-weak-ties/scene.py Episode \
        videos/episodes/059-strength-of-weak-ties/final.mp4
"""
import json
from pathlib import Path

import numpy as np
from manim import *
from sample_space import *

HERE = Path(__file__).resolve().parent
FIG = json.loads((HERE / "data" / "fig3b_digitized.json").read_text())


def _clean(points):
    """Merge the dot split by the dashed zero line (three centres at x~32.2)."""
    out, seen = [], set()
    for x, y in points:
        key = round(x)
        if key in seen:
            continue
        seen.add(key)
        out.append((x, max(0.0, y)))
    return out


IV = _clean(FIG["iv"])        # randomized (instrumental-variable) estimates, per 1,000 ties
OLS = _clean(FIG["ols"])      # plain correlation estimates, per 1,000 ties

# Granovetter 1973, p. 1371: N = 54; often 16.7 %, occasionally 55.6 %, rarely 27.8 %
COUNTS = [9, 30, 15]
PILE_X = [-4.0, 0.0, 4.0]
PILE_BASE = -1.35
DOT_R = 0.085
STEP = 0.255
COLS = 3

YOU = np.array([-3.3, -0.45, 0.0])
RING_R = 1.55
RING_ANG = [20 + 40 * k for k in range(9)]      # your 9 close friends
SAM_I = 3                                       # the friend at 140 degrees
SHARED_I = 8                                    # the friend at 340 degrees, who also knows Ana
ANA_C = np.array([3.45, -0.45, 0.0])
ANA_R = 1.35


def pol(c, r, deg):
    a = np.deg2rad(deg)
    return c + r * np.array([np.cos(a), np.sin(a), 0.0])


def pile_slot(pile, i):
    """Position of the i-th dot in a pile (COLS dots per row, bottom up)."""
    row, col = divmod(i, COLS)
    x = PILE_X[pile] + (col - (COLS - 1) / 2) * STEP
    y = PILE_BASE + DOT_R + 0.05 + row * STEP
    return np.array([x, y, 0.0])


def node(p, color, r=0.12, fill=1.0):
    return Dot(p, radius=r, color=color, fill_opacity=fill).set_z_index(3)


def edge(a, b, color=DIM, width=2.0, opacity=1.0):
    return Line(a, b, color=color, stroke_width=width, stroke_opacity=opacity).set_z_index(1)


class Episode(NarratedScene):
    EPISODE = 59
    TITLE = "Why Acquaintances Find You Jobs"
    PRONUNCIATIONS = {}

    # ------------------------------------------------------------------ piles
    def make_piles(self):
        bases = VGroup(*[Line(LEFT * 0.62, RIGHT * 0.62, color=GRAY, stroke_width=3)
                         .move_to([x, PILE_BASE, 0]) for x in PILE_X])
        names = ["often", "occasionally", "rarely"]
        subs = ["twice a week or more", "in between", "once a year or less"]
        labels = VGroup()
        for x, n, s in zip(PILE_X, names, subs):
            t = label(n, size=LABEL).move_to([x, PILE_BASE - 0.38, 0])
            st = label(s, size=22, color=GRAY).next_to(t, DOWN, buff=0.14)
            labels.add(VGroup(t, st))
        return bases, labels

    def construct(self):
        # ============================================================ 1. cold open
        people = VGroup(*[Dot(radius=DOT_R, color=INK) for _ in range(54)])
        people.arrange_in_grid(rows=6, cols=9, buff=STEP - 2 * DOT_R).move_to(UP * 2.35)
        bases, pile_labels = self.make_piles()
        n54 = formula(r"54", size=MATH).next_to(people, LEFT, buff=0.4)

        with self.narrate("Fifty-four people each got a job through someone they knew. "
                          "Sort them by how often they saw that person back then. "
                          "Which pile will be biggest? [pause 1.5]") as beat:
            self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in people], lag_ratio=0.02),
                      FadeIn(n54), run_time=beat.until_end_of("knew"))
            beat.wait_until("Sort", offset=-0.1)
            self.play(LaggedStart(*[AnimationGroup(Create(b), FadeIn(l, shift=0.15 * UP))
                                    for b, l in zip(bases, pile_labels)], lag_ratio=0.35),
                      run_time=beat.until("Which", offset=-0.1))
            beat.wait_until("biggest", offset=-0.1)
            # the prediction hold: a slow sweep across the three empty piles
            sweep = SurroundingRectangle(VGroup(bases[0], pile_labels[0]), color=YELLOW,
                                         buff=0.15, corner_radius=0.08, stroke_width=2.5)
            self.play(Create(sweep), run_time=0.6)
            for k in (1, 2):
                tgt = SurroundingRectangle(VGroup(bases[k], pile_labels[k]), color=YELLOW,
                                           buff=0.15, corner_radius=0.08, stroke_width=2.5)
                self.play(Transform(sweep, tgt), run_time=0.7)
            self.play(FadeOut(sweep), run_time=beat.remaining(min_time=0.3))

        # ============================================================ 2. naive guess
        ghost_h = 10 * STEP + 0.1
        ghost = DashedVMobject(Rectangle(width=COLS * STEP + 0.2, height=ghost_h, color=RED,
                                         stroke_width=3), num_dashes=40)
        ghost.move_to([PILE_X[0], PILE_BASE + ghost_h / 2, 0])
        ghost_lbl = label("close-friends guess", size=26, color=RED).next_to(ghost, UP, buff=0.18)
        with self.narrate("Most of us would bet on the left pile. "
                          "Close friends know us best, and they want to help.") as beat:
            self.play(FadeOut(n54), people.animate.move_to(UP * 2.35 + RIGHT * 2.2),
                      run_time=beat.until("left", offset=-0.2))
            self.play(GrowFromEdge(ghost, DOWN), run_time=1.0)
            self.play(FadeIn(ghost_lbl, shift=0.1 * UP), run_time=0.6)
            self.hold(beat.remaining() - 0.05)

        # ============================================================ 3. reveal
        order = [0] * 9 + [1] * 30 + [2] * 15
        idx_in_pile = [0, 0, 0]
        targets = []
        for p in order:
            targets.append(pile_slot(p, idx_in_pile[p]))
            idx_in_pile[p] += 1
        groups = [VGroup(*people[0:9]), VGroup(*people[9:39]), VGroup(*people[39:54])]
        count_tex = [formula(str(c), size=MATH) for c in COUNTS]
        for k, (c, g) in enumerate(zip(count_tex, groups)):
            top = PILE_BASE + (np.ceil(COUNTS[k] / COLS)) * STEP + 0.05
            c.move_to([PILE_X[k], top + 0.35, 0])
        cite_g = citation("Granovetter, 1973 · American Journal of Sociology")
        with self.narrate("Mark Granovetter published this survey in nineteen seventy-three. "
                          "Nine people saw their contact often. Thirty, occasionally. "
                          "Fifteen, rarely.") as beat:
            self.play(FadeIn(cite_g), run_time=beat.until("Nine", offset=-0.5))
            for k, word in enumerate(["Nine", "Thirty", "Fifteen"]):
                beat.wait_until(word, offset=-0.25)
                g = groups[k]
                self.play(LaggedStart(*[d.animate.move_to(targets[order.index(k) + j])
                                        for j, d in enumerate(g)], lag_ratio=0.03),
                          run_time=1.0 if k else 0.9)
                if k == 0:
                    # the ghost label moves above the real count to make room
                    self.play(FadeIn(count_tex[k], shift=0.1 * UP), run_time=0.4)
                else:
                    self.play(FadeIn(count_tex[k], shift=0.1 * UP), run_time=0.4)

        # ============================================================ 4. measured fail
        frac = formula(r"\tfrac{9}{54}", r"=", r"17\%", size=MATH, color=RED)
        frac.next_to(ghost, RIGHT, buff=0.3).shift(UP * 0.6)
        quote = text("“Not a friend, an acquaintance.”", size=34, slant=ITALIC)
        quote.move_to(UP * 3.05)
        with self.narrate("The close-friends pile holds nine of fifty-four, seventeen percent. "
                          "His respondents kept correcting him: not a friend, an acquaintance.") as beat:
            beat.wait_until("nine", offset=-0.2)
            self.play(TransformFromCopy(count_tex[0], frac[0]), run_time=0.9)
            self.play(Write(frac[1:]), run_time=beat.until("kept", offset=-0.3))
            beat.wait_until("not a friend", offset=-0.3)
            self.play(Write(quote), run_time=beat.remaining(min_time=1.0))

        # ============================================================ 5. objection
        split = formula(r"\text{pile}", r"=", r"\text{number of ties}", r"\times",
                        r"\text{help per tie}", size=MATH)
        split.move_to(UP * 3.05)
        split[4].set_color(YELLOW)
        hbox = box(split[4])
        with self.narrate("A fair objection, which Granovetter printed in a footnote: "
                          "most of us have far more acquaintances than close friends. "
                          "Maybe they win on numbers alone. "
                          "So split each pile into how many ties, times help per tie.") as beat:
            self.play(FadeOut(quote, shift=0.2 * UP), FadeOut(cite_g),
                      run_time=beat.until("most", offset=-0.2))
            # acquaintances outnumber close friends: the two right piles pulse together
            self.play(LaggedStart(flag(groups[1]), flag(groups[2]), lag_ratio=0.3),
                      run_time=beat.until("numbers", offset=-0.1))
            beat.wait_until("split", offset=-0.2)
            self.play(Write(split[0:2]), run_time=0.6)
            self.play(TransformFromCopy(groups[2], split[2]), run_time=beat.until("times", offset=-0.1))
            self.play(Write(split[3]), run_time=0.3)
            self.play(Write(split[4]), run_time=beat.until_end_of("tie", offset=-0.05))
            self.play(Create(hbox), run_time=0.5)

        # ============================================================ 6. network: you
        anchor = VGroup(split[4], hbox)
        fr = [pol(YOU, RING_R, a) for a in RING_ANG]
        you = node(YOU, INK, r=0.2)
        you_lbl = label("you", size=LABEL).next_to(you, DOWN, buff=0.16).shift(LEFT * 0.0)
        you_lbl.set_z_index(4)
        friends = VGroup(*[node(p, BLUE) for p in fr])
        strong = VGroup(*[edge(YOU, p, BLUE, 7) for p in fr])
        # close friends know each other: ring neighbours plus a few chords
        pairs = [(k, (k + 1) % 9) for k in range(9)] + [(k, (k + 2) % 9) for k in range(0, 9, 2)]
        among = VGroup(*[edge(fr[a], fr[b], DIM, 2) for a, b in pairs])
        with self.narrate("Take one person: you. Here are your close friends, "
                          "and close friends tend to know each other.") as beat:
            self.play(*[FadeOut(m) for m in (*groups, *count_tex, bases, pile_labels, ghost,
                                              ghost_lbl, frac, split[0:4])],
                      anchor.animate.move_to(UP * 3.2), run_time=0.9)
            self.play(GrowFromCenter(you), FadeIn(you_lbl), run_time=beat.until("Here", offset=-0.1))
            self.play(LaggedStart(*[AnimationGroup(Create(e), FadeIn(f, scale=0.5))
                                    for e, f in zip(strong, friends)], lag_ratio=0.12),
                      run_time=beat.until("know", offset=-0.2))
            self.play(LaggedStart(*[Create(e) for e in among], lag_ratio=0.05),
                      run_time=beat.remaining(min_time=1.0))

        # ============================================================ 7. Sam
        sam = friends[SAM_I]
        sam_lbl = label("Sam", size=LABEL).next_to(sam, UP + LEFT, buff=0.08)
        sam_new_pos = [np.array([-5.75, 1.55, 0]), np.array([-4.85, 2.15, 0])]
        sam_new = VGroup(*[node(p, PURPLE) for p in sam_new_pos])
        others = [k for k in range(9) if k != SAM_I]
        sam_edges_shared = VGroup(*[edge(fr[SAM_I], fr[k], BLUE, 2.5, 0.85) for k in others])
        sam_edges_new = VGroup(*[edge(fr[SAM_I], p, PURPLE, 2.5) for p in sam_new_pos])
        sam_shared_lbl = formula(r"8", r"\text{ shared}", size=MATH, color=BLUE)
        sam_new_lbl = formula(r"2", r"\text{ new}", size=MATH, color=PURPLE)
        sam_new_lbl.move_to([-5.55, 2.75, 0])
        sam_shared_lbl.move_to([-0.95, 1.7, 0])
        with self.narrate("Here's Sam, your best friend. Of Sam's ten other contacts, "
                          "eight are already yours.") as beat:
            self.play(sam.animate.scale(1.35), FadeIn(sam_lbl, shift=0.1 * DR),
                      dim(among, opacity=0.35), run_time=beat.until("Of", offset=-0.1))
            self.play(LaggedStart(*[Create(e) for e in sam_edges_shared], lag_ratio=0.08),
                      LaggedStart(*[FadeIn(n, scale=0.5) for n in sam_new], lag_ratio=0.3),
                      LaggedStart(*[Create(e) for e in sam_edges_new], lag_ratio=0.3),
                      run_time=beat.until("eight", offset=-0.15))
            self.play(LaggedStart(*[f.animate.scale(1.3) for k, f in enumerate(friends)
                                    if k != SAM_I], lag_ratio=0.05),
                      FadeIn(sam_shared_lbl), FadeIn(sam_new_lbl), run_time=0.9)
            self.play(LaggedStart(*[f.animate.scale(1 / 1.3) for k, f in enumerate(friends)
                                    if k != SAM_I], lag_ratio=0.05),
                      run_time=beat.remaining(min_time=0.5))

        # ============================================================ 8. a job inside the circle
        src = fr[6]                                   # the friend at 260 degrees
        burst = Circle(radius=0.15, color=BLUE, stroke_width=4).move_to(src)
        pk_you = node(src, BLUE, r=0.09).set_z_index(5)
        pk_sam = node(src, BLUE, r=0.09).set_z_index(5)
        heard = label("already heard", size=26, color=GRAY).next_to(you, RIGHT, buff=0.3).shift(DOWN * 0.45)
        with self.narrate("When a job opens in this circle, the news reaches you and Sam "
                          "at the same moment. Sam's tip arrives as a rerun.") as beat:
            beat.wait_until("job", offset=-0.15)
            self.play(burst.animate.scale(4).set_stroke(opacity=0), run_time=0.8)
            self.remove(burst)
            self.add(pk_you, pk_sam)
            beat.wait_until("reaches", offset=-0.1)
            self.play(pk_you.animate.move_to(YOU), pk_sam.animate.move_to(fr[SAM_I]),
                      run_time=beat.until("same", offset=0.1), rate_func=LINEAR)
            self.play(Flash(you, color=BLUE, line_length=0.18, flash_radius=0.32),
                      Flash(sam, color=BLUE, line_length=0.18, flash_radius=0.3), run_time=0.6)
            self.remove(pk_you)
            beat.wait_until("tip", offset=-0.3)
            self.play(pk_sam.animate.move_to(YOU).set_color(GRAY),
                      run_time=beat.until("rerun", offset=-0.3), rate_func=LINEAR)
            self.play(FadeIn(heard, shift=0.1 * RIGHT), FadeOut(pk_sam), run_time=0.5)

        # ============================================================ 9. Ana
        ana_pos = pol(ANA_C, ANA_R, 180)
        her = [pol(ANA_C, ANA_R, 180 + 36 * k) for k in range(1, 10)]
        ana = node(ana_pos, INK, r=0.15)
        ana_lbl = label("Ana", size=LABEL).next_to(ana, UP, buff=0.18).shift(RIGHT * 0.05)
        her_nodes = VGroup(*[node(p, PURPLE) for p in her])
        weak = edge(YOU, ana_pos, INK, 2.2)
        ana_spokes = VGroup(*[edge(ana_pos, p, PURPLE, 2.0, 0.6) for p in her])
        her_ring = VGroup(*[edge(her[k], her[k + 1], DIM, 2) for k in range(8)])
        ana_shared_edge = edge(ana_pos, fr[SHARED_I], BLUE, 2.5)
        ana_shared_lbl = formula(r"1", r"\text{ shared}", size=MATH, color=BLUE)
        ana_shared_lbl.move_to([0.25, -2.05, 0])
        ana_new_lbl = formula(r"9", r"\text{ new}", size=MATH, color=PURPLE)
        ana_new_lbl.move_to([ANA_C[0], 1.55, 0])
        with self.narrate("Now Ana, someone you see once a year. Of her ten contacts, "
                          "you know one. The other nine live in a circle you never hear from, "
                          "except through her.") as beat:
            self.play(FadeOut(heard), Create(weak), FadeIn(ana, scale=0.5),
                      run_time=beat.until("someone", offset=-0.1))
            self.play(FadeIn(ana_lbl), run_time=0.5)
            self.play(LaggedStart(*[FadeIn(n, scale=0.5) for n in her_nodes], lag_ratio=0.06),
                      LaggedStart(*[Create(e) for e in ana_spokes], lag_ratio=0.06),
                      Create(her_ring), run_time=beat.until("you know", offset=-0.2))
            self.play(Create(ana_shared_edge), FadeIn(ana_shared_lbl),
                      friends[SHARED_I].animate.scale(1.4), run_time=0.8)
            self.play(friends[SHARED_I].animate.scale(1 / 1.4), run_time=0.4)
            beat.wait_until("nine", offset=-0.2)
            self.play(FadeIn(ana_new_lbl),
                      LaggedStart(*[n.animate.scale(1.35) for n in her_nodes], lag_ratio=0.05),
                      run_time=0.9)
            self.play(LaggedStart(*[n.animate.scale(1 / 1.35) for n in her_nodes], lag_ratio=0.05),
                      run_time=0.5)
            # a job opens in her circle; the only way to you is the thin edge
            src2 = her[4]
            burst2 = Circle(radius=0.15, color=PURPLE, stroke_width=4).move_to(src2)
            beat.wait_until("never", offset=-0.2)
            self.play(burst2.animate.scale(4).set_stroke(opacity=0), run_time=0.7)
            self.remove(burst2)
            pk = node(src2, PURPLE, r=0.09).set_z_index(5)
            self.add(pk)
            self.play(pk.animate.move_to(ana_pos), run_time=beat.until("except", offset=0.0),
                      rate_func=LINEAR)
            self.play(pk.animate.move_to(YOU), run_time=beat.until_end_of("her", offset=-0.1),
                      rate_func=LINEAR)
            self.play(Flash(you, color=PURPLE, line_length=0.2, flash_radius=0.34),
                      FadeOut(pk), run_time=0.6)

        # ============================================================ 10. the stranger
        st_pos = np.array([0.2, 2.0, 0])
        stranger = node(st_pos, GRAY, r=0.15)
        st_lbl = label("stranger", size=26, color=GRAY).next_to(stranger, UP, buff=0.15)
        st_c = [st_pos + 0.75 * np.array([np.cos(a), np.sin(a), 0]) for a in np.deg2rad([-10, 25, 60, 165])]
        st_contacts = VGroup(*[node(p, PURPLE, r=0.1) for p in st_c])
        st_edges = VGroup(*[edge(st_pos, p, PURPLE, 1.8, 0.6) for p in st_c])
        st_zero = formula(r"0", r"\text{ shared}", size=MATH, color=BLUE).next_to(st_lbl, RIGHT, buff=0.35)
        with self.narrate("So are the weakest ties of all the best? "
                          "A stranger shares none of your friends, so everything they hear is "
                          "new to you, but they have no reason to tell you any of it.") as beat:
            beat.wait_until("stranger", offset=-0.2)
            self.play(FadeIn(stranger, scale=0.5), FadeIn(st_lbl),
                      LaggedStart(*[Create(e) for e in st_edges], lag_ratio=0.1),
                      LaggedStart(*[FadeIn(n) for n in st_contacts], lag_ratio=0.1),
                      run_time=beat.until("none", offset=-0.1))
            self.play(FadeIn(st_zero), run_time=0.6)
            beat.wait_until("no reason", offset=-0.3)
            tip = node(st_pos, PURPLE, r=0.09).set_z_index(5)
            mid = st_pos + 0.45 * (YOU - st_pos)
            self.add(tip)
            self.play(tip.animate.move_to(mid).set_opacity(0), run_time=beat.remaining(min_time=1.0),
                      rate_func=rate_functions.ease_out_sine)
            self.remove(tip)

        # ============================================================ 11. s from the counts
        s_sam = formula(r"s_{\text{Sam}}", r"=", r"\tfrac{8}{10}", size=MATH)
        s_ana = formula(r"s_{\text{Ana}}", r"=", r"\tfrac{1}{10}", size=MATH)
        s_sam[2].set_color(BLUE)
        s_ana[2].set_color(BLUE)
        s_col = VGroup(s_sam, s_ana).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        s_col.move_to([-5.0, 1.2, 0])
        ax = axes((0, 1), (0, 1), x_length=7.4, y_length=4.4, x_ticks=[0, 0.5, 1],
                  y_ticks=[0, 0.5, 1], x_decimals=1, y_decimals=1,
                  x_label="s  (share of their contacts you know)", y_label="per tie")
        ax.move_to([1.55, -0.55, 0])
        willing = ax.plot(lambda s: s, x_range=[0, 1], color=GREEN, stroke_width=5)
        novel = ax.plot(lambda s: 1 - s, x_range=[0, 1], color=PURPLE, stroke_width=5)
        w_lbl = label("passes a tip on", size=26, color=GREEN)
        w_lbl.next_to(ax.c2p(1, 1), LEFT, buff=0.15).shift(UP * 0.05 + LEFT * 0.05)
        w_toy = label("(toy assumption)", size=22, color=GRAY).next_to(w_lbl, DOWN, buff=0.1)
        w_toy.align_to(w_lbl, RIGHT)
        n_lbl = label("new to you", size=26, color=PURPLE)
        n_lbl.next_to(ax.c2p(0, 1), RIGHT, buff=0.2).shift(DOWN * 0.05)
        net = VGroup(you, you_lbl, friends, strong, among, sam_lbl, sam_new, sam_edges_shared,
                     sam_edges_new, ana, ana_lbl, her_nodes, weak, ana_spokes, her_ring,
                     ana_shared_edge, stranger, st_lbl, st_contacts, st_edges)
        with self.narrate("Call s the share of their contacts you already know: "
                          "eight in ten for Sam, one in ten for Ana. "
                          "As a toy assumption, say their willingness to pass a tip on grows with s. "
                          "The share of their news that's new to you is one minus s.") as beat:
            self.play(Write(s_sam[0:2]), Write(s_ana[0:2]), FadeOut(st_zero),
                      run_time=beat.until("eight", offset=-0.15))
            self.play(TransformFromCopy(sam_shared_lbl[0], s_sam[2]), run_time=0.9)
            beat.wait_until("one in ten", offset=-0.15)
            self.play(TransformFromCopy(ana_shared_lbl[0], s_ana[2]), run_time=0.9)
            self.play(FadeOut(net), FadeOut(sam_shared_lbl), FadeOut(sam_new_lbl),
                      FadeOut(ana_shared_lbl), FadeOut(ana_new_lbl),
                      run_time=beat.until("As a", offset=-0.1))
            self.play(Create(ax), run_time=beat.until("willingness", offset=-0.1))
            self.play(Create(willing), FadeIn(w_lbl), FadeIn(w_toy),
                      run_time=beat.until_end_of("grows with s", offset=-0.05))
            beat.wait_until("new to you", offset=-0.2)
            self.play(Create(novel), FadeIn(n_lbl), run_time=beat.remaining(min_time=1.0))

        # ============================================================ 12. product + prediction
        prod_eq = formula(r"\text{help per tie}", r"\propto", r"s", r"\times", r"(1-s)", size=EQ)
        prod_eq[0].set_color(YELLOW)
        prod_eq[2].set_color(GREEN)
        prod_eq[4].set_color(PURPLE)
        prod_eq.move_to(UP * 3.15 + RIGHT * 0.9)
        with self.narrate("Help per tie is the product. Where does it peak? [pause 1.5]") as beat:
            self.play(ReplacementTransform(anchor[0], prod_eq[0]), FadeOut(anchor[1]),
                      run_time=beat.until("product", offset=-0.1))
            self.play(TransformFromCopy(w_lbl, prod_eq[2]), Write(prod_eq[1]), run_time=0.7)
            self.play(Write(prod_eq[3]), TransformFromCopy(n_lbl, prod_eq[4]), run_time=0.7)
            beat.wait_until("peak", offset=0.3)
            # prediction hold: a probe slides along the s axis without revealing anything
            probe = Line(ax.c2p(0.02, 0), ax.c2p(0.02, 1), color=YELLOW, stroke_width=2,
                         stroke_opacity=0.6)
            self.play(Create(probe), run_time=0.4)
            self.play(probe.animate.move_to(ax.c2p(0.98, 0.5)), run_time=beat.remaining(min_time=1.0),
                      rate_func=EASE)
            self.play(FadeOut(probe), run_time=0.3)

        hump = ax.plot(lambda s: s * (1 - s), x_range=[0, 1], color=YELLOW, stroke_width=6)
        pts = {"Ana": 0.1, "half": 0.5, "Sam": 0.8}
        mk = {k: Dot(ax.c2p(v, v * (1 - v)), radius=0.1, color=YELLOW).set_z_index(4)
              for k, v in pts.items()}
        mk_lbl = {
            "Ana": formula(r"\text{Ana } 0.09", size=MATH_SMALL + 4, color=YELLOW),
            "half": formula(r"\text{half shared } 0.25", size=MATH_SMALL + 4, color=YELLOW),
            "Sam": formula(r"\text{Sam } 0.16", size=MATH_SMALL + 4, color=YELLOW),
        }
        mk_lbl["half"].next_to(mk["half"], UP, buff=0.22)
        mk_lbl["Sam"].next_to(mk["Sam"], UP, buff=0.25).shift(RIGHT * 0.25)
        mk_lbl["Ana"].next_to(mk["Ana"], UP, buff=0.25).shift(LEFT * 0.05)
        with self.narrate("Not at either end. Sam scores point one six, Ana point oh nine, "
                          "and a friend with half your contacts in common scores point two five. "
                          "Where exactly the peak sits depends on the toy assumption.") as beat:
            self.play(Create(hump), run_time=beat.until("Sam", offset=-0.1))
            self.play(GrowFromCenter(mk["Sam"]), FadeIn(mk_lbl["Sam"]), run_time=0.6)
            beat.wait_until("Ana", offset=-0.1)
            self.play(GrowFromCenter(mk["Ana"]), FadeIn(mk_lbl["Ana"]), run_time=0.6)
            beat.wait_until("half", offset=-0.1)
            self.play(GrowFromCenter(mk["half"]), FadeIn(mk_lbl["half"]), run_time=0.6)
            beat.wait_until("toy", offset=-0.3)
            self.play(flag(w_toy), run_time=0.9)

        # ============================================================ 13. LinkedIn
        ax2 = axes((-1, 35), (0, 6), x_length=9.6, y_length=4.4, x_ticks=[0, 10, 20, 30],
                   y_ticks=[0, 2, 4, 6], x_decimals=0, y_decimals=0,
                   x_label="mutual friends with the new connection",
                   y_label="jobs through that tie, per 1,000 new ties")
        ax2.move_to([0.35, -0.5, 0])
        cite_r = citation("Rajkumar et al., 2022 · Science")
        with self.narrate("In twenty twenty-two, researchers at LinkedIn, Harvard, Stanford and MIT "
                          "tested this causally. Over five years, People You May Know randomly "
                          "nudged more than twenty million people toward weaker or stronger "
                          "new connections.") as beat:
            self.play(FadeIn(cite_r), run_time=beat.until("researchers", offset=-0.1))
            self.play(*[FadeOut(m) for m in (s_col, w_lbl, w_toy, n_lbl, willing, novel,
                                             *mk.values(), *mk_lbl.values(), prod_eq)],
                      run_time=beat.until("tested", offset=-0.1))
            self.play(ReplacementTransform(ax, ax2), hump.animate.set_stroke(opacity=0.25),
                      run_time=beat.until("randomly", offset=-0.1))
            nudge = VGroup(
                label("randomized", size=26, color=YELLOW),
                label("20 million people · 5 years", size=24, color=GRAY),
            ).arrange(DOWN, buff=0.12, aligned_edge=RIGHT)
            nudge.move_to([4.6, 2.75, 0])
            self.play(FadeIn(nudge[0]), run_time=beat.until("twenty million", offset=-0.1))
            self.play(FadeIn(nudge[1]), run_time=beat.remaining(min_time=0.6))

        iv_dots = VGroup(*[Dot(ax2.c2p(x, y), radius=0.085, color=YELLOW).set_z_index(4)
                           for x, y in IV])
        iv_line = VMobject(color=YELLOW, stroke_width=2.5, stroke_opacity=0.55)
        iv_line.set_points_as_corners([ax2.c2p(x, y) for x, y in IV])
        peak = max(IV, key=lambda p: p[1])
        peak_lbl = formula(r"\text{peak} \approx 10", size=MATH_SMALL + 4, color=YELLOW)
        peak_lbl.next_to(ax2.c2p(*peak), UP, buff=0.2)
        digit = label("digitized from Fig. 3B · 2015 wave", size=20, color=GRAY)
        digit.next_to(cite_r, RIGHT, buff=0.4).align_to(cite_r, DOWN)
        with self.narrate("For each new connection, they measured the chance it led to a job "
                          "at the contact's company. It rose with mutual friends, peaked around "
                          "ten, then fell.") as beat:
            self.play(FadeOut(hump), FadeIn(digit), run_time=beat.until("rose", offset=-0.2))
            n_up = sum(1 for x, _ in IV if x <= peak[0] + 0.1)
            self.play(LaggedStart(*[GrowFromCenter(d) for d in iv_dots[:n_up]], lag_ratio=0.2),
                      Create(iv_line, rate_func=lambda t: min(1, t * n_up / len(IV))),
                      run_time=beat.until("peaked", offset=-0.1))
            self.play(FadeIn(peak_lbl, shift=0.1 * UP), run_time=beat.until("then", offset=-0.1))
            self.play(LaggedStart(*[GrowFromCenter(d) for d in iv_dots[n_up:]], lag_ratio=0.12),
                      run_time=beat.remaining(min_time=1.2))
        self.add(iv_line)

        # ============================================================ 14. per tie, correlation, limit
        ols_dots = VGroup(*[Circle(radius=0.075, color=GRAY, stroke_width=3).move_to(ax2.c2p(x, y))
                            .set_z_index(3) for x, y in OLS])
        ols_lbl = label("plain correlation", size=26, color=GRAY)
        ols_lbl.next_to(ax2.c2p(34, OLS[-1][1]), UP, buff=0.3).align_to(ax2.c2p(34.5, 0), RIGHT)
        iv_lbl = label("randomized", size=26, color=YELLOW)
        limit = label("less digital industries: strong ties helped more", size=24, color=GRAY)
        limit.move_to([0.0, 3.38, 0])
        with self.narrate("Because the nudges were random and the count is per tie, sheer numbers "
                          "can't explain it. Plain correlations in the same data pointed the other "
                          "way, toward the strongest ties. In less digital industries, strong ties "
                          "did help more.") as beat:
            self.play(LaggedStart(*[flag(d) for d in iv_dots[:8]], lag_ratio=0.1),
                      run_time=beat.until("per tie", offset=-0.1))
            beat.wait_until("Plain", offset=-0.2)
            self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in ols_dots], lag_ratio=0.08),
                      FadeIn(ols_lbl), run_time=beat.until("strongest", offset=-0.1))
            beat.wait_until("less digital", offset=-0.2)
            self.play(FadeIn(limit, shift=0.1 * DOWN), run_time=beat.remaining(min_time=0.8))

        # ============================================================ 15. landing
        bases2, labels2 = self.make_piles()
        piles2 = VGroup()
        for k, c in enumerate(COUNTS):
            piles2.add(VGroup(*[Dot(pile_slot(k, j), radius=DOT_R, color=INK) for j in range(c)]))
        counts2 = VGroup(*[formula(str(c), size=MATH).move_to(count_tex[k]) for k, c in enumerate(COUNTS)])
        with self.narrate("Look back at the fifty-four. The biggest pile wasn't the rarest contacts "
                          "either. It was the middle one: people close enough to think of you, "
                          "and far enough to know something you don't.") as beat:
            self.play(*[FadeOut(m) for m in (ax2, iv_dots, iv_line, ols_dots, ols_lbl, peak_lbl,
                                             digit, cite_r, limit, nudge)],
                      run_time=0.7)
            self.play(FadeIn(bases2), FadeIn(labels2),
                      LaggedStart(*[FadeIn(p, shift=0.2 * DOWN) for p in piles2], lag_ratio=0.2),
                      FadeIn(counts2), run_time=beat.until("biggest", offset=-0.2))
            self.play(piles2[2].animate.set_opacity(0.35), counts2[2].animate.set_opacity(0.35),
                      run_time=beat.until("middle", offset=-0.2))
            self.play(piles2[1].animate.set_color(YELLOW), counts2[1].animate.set_color(YELLOW),
                      labels2[1][0].animate.set_color(YELLOW), run_time=0.8)
            self.play(piles2[0].animate.set_opacity(0.35), counts2[0].animate.set_opacity(0.35),
                      run_time=beat.remaining(min_time=0.8))

        self.end_card()
