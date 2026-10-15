"""Episode 58: How a Few Shortcuts Shrink the Whole World (small-world networks).

All network numbers come from data.json, written by make_data.py (simulated, seeded).
    videos/toolkit/render.sh videos/episodes/058-small-world-networks/scene.py Episode \
        videos/episodes/058-small-world-networks/final.mp4
"""
import json
from pathlib import Path

import numpy as np
from manim import *
from sample_space import *

D = json.loads((Path(__file__).resolve().parent / "data.json").read_text())
N = 200
RC = np.array([-3.75, -0.15, 0.0])      # ring centre
RAD = 2.55
DOT_R = 0.05
LINK_W = 1.6


def node_pos(i):
    th = PI / 2 - i * TAU / N
    return RC + RAD * np.array([np.cos(th), np.sin(th), 0.0])


def lattice_edges():
    return [(i, (i + d) % N) for i in range(N) for d in (1, 2)]


def link(a, b, color=BLUE, width=LINK_W, opacity=0.75):
    return Line(node_pos(a), node_pos(b), stroke_width=width, color=color,
                stroke_opacity=opacity)


class Episode(NarratedScene):
    EPISODE = 58
    TITLE = "How a Few Shortcuts Shrink the Whole World"
    PRONUNCIATIONS = {"Strogatz": "stro gats"}

    # ------------------------------------------------------------------ helpers
    def wave(self, dots, hops, tracker):
        hops = np.array(hops)

        def upd(g):
            h = tracker.get_value()
            for d, k in zip(g, hops):
                reached = k <= h + 1e-6
                d.set_fill(PURPLE if reached else BLUE)
                d.set_width(2 * DOT_R * (1.5 if reached else 1.0))
        return upd

    def construct(self):
        L0, C0 = D["L0"], D["C0"]
        L8, C8 = D["L8"], D["C8"]
        Lr, Cr = D["Lr"], D["Cr"]

        # ---------------------------------------------------------------- ring
        edges = lattice_edges()
        lines = {e: link(*e) for e in edges}
        link_group = VGroup(*lines.values())
        dots = VGroup(*[Dot(node_pos(i), radius=DOT_R, color=BLUE) for i in range(N)])
        dots.set_z_index(3)

        # readout row (persistent): L purple, C green
        Lt = ValueTracker(L0)
        Ct = ValueTracker(C0)
        L_num = live_number(Lt, 1, size=EQ, color=PURPLE, prefix=r"L =")
        C_num = live_number(Ct, 2, size=EQ, color=GREEN, prefix=r"C =")
        L_num.move_to([1.55, 2.95, 0])
        C_num.move_to([4.95, 2.95, 0])
        L_cap = label("average trip (steps)", size=26, color=GRAY).next_to(L_num, DOWN, buff=0.2)
        C_cap = label("clustering", size=26, color=GRAY).next_to(C_num, DOWN, buff=0.2)
        C_cap.align_to(C_num, LEFT)
        L_cap.align_to(L_num, LEFT)
        sim_tag = label("simulated", size=22, color=GRAY).move_to([-3.75, -3.0, 0])

        # ============================================================ COLD OPEN
        with self.narrate("Two hundred people stand in a ring, each knowing only the four "
                          "people nearest them.") as beat:
            self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.01),
                      run_time=beat.until_end_of("ring"))
            self.play(Create(link_group, lag_ratio=0.002), FadeIn(sim_tag),
                      run_time=beat.until("four", offset=-0.15))
            # one person and the four links they have
            me = dots[0]
            mine = VGroup(lines[(0, 1)], lines[(0, 2)], lines[(N - 1, 0)], lines[(N - 2, 0)])
            self.play(me.animate.set_color(INK).scale(1.6),
                      *[m.animate.set_stroke(INK, width=3.5, opacity=1) for m in mine],
                      *[dots[j].animate.scale(1.5) for j in (1, 2, N - 1, N - 2)],
                      run_time=0.8)
            beat.wait_until("nearest", offset=0.3)
            self.play(me.animate.set_color(BLUE).scale(1 / 1.6),
                      *[m.animate.set_stroke(BLUE, width=LINK_W, opacity=0.75) for m in mine],
                      *[dots[j].animate.scale(1 / 1.5) for j in (1, 2, N - 1, N - 2)],
                      run_time=beat.remaining(0.6))

        hop = ValueTracker(0)
        hop_num = live_number(hop, 0, size=MATH, color=PURPLE, prefix=r"\text{hop}")
        hop_num.move_to(RC)
        upd = self.wave(dots, D["hops_ring"], hop)
        with self.narrate("A note passed hand to hand between two of them takes twenty-five "
                          "steps, on average.") as beat:
            dots.add_updater(upd)
            self.add(hop_num)
            self.play(hop.animate.set_value(50), run_time=beat.until("twenty", offset=-0.5),
                      rate_func=LINEAR)
            self.play(FadeIn(L_num, shift=0.2 * LEFT), FadeIn(L_cap), run_time=0.7)
            dots.remove_updater(upd)
            self.play(dots.animate.set_fill(BLUE).set_width(dots.width), FadeOut(hop_num),
                      run_time=beat.remaining(0.6))
        for d in dots:
            d.set_width(2 * DOT_R)

        # the 8 shortcuts: unhook a ring link, reattach it across the circle
        removed = [tuple(e) for e in D["removed"]]
        shortcuts = [tuple(e) for e in D["shortcuts"]]

        def key(a, b):
            return (a, b) if (a, b) in lines else (b, a)
        rem_lines = [lines[key(*e)] for e in removed]
        rem_orig = [l.copy() for l in rem_lines]
        chord_targets = [link(u, w, color=YELLOW, width=3.2, opacity=1) for (u, w) in shortcuts]
        arrow = MathTex(r"\rightarrow", font_size=EQ, color=GRAY)
        qmark = MathTex(r"?", font_size=EQ, color=YELLOW)
        with self.narrate("Now rewire just eight of the four hundred links, at random. "
                          "How short does that average trip get? [pause 1.5]") as beat:
            beat.wait_until("eight", offset=-0.15)
            self.play(LaggedStart(*[Transform(l, t) for l, t in zip(rem_lines, chord_targets)],
                                  lag_ratio=0.25), run_time=beat.until("How", offset=-0.1))
            L_static = L_num  # live number already reads 25.4
            arrow.next_to(L_num, RIGHT, buff=0.25)
            qmark.next_to(arrow, RIGHT, buff=0.25)
            self.play(FadeIn(arrow, shift=0.1 * RIGHT), Write(qmark),
                      run_time=beat.until("trip", offset=0.2))

        # ============================================================ STAKES
        with self.narrate("Hold that guess. Real social networks look like this ring up "
                          "close, where your friends tend to know each other, yet strangers "
                          "are only a few hops apart.") as beat:
            self.play(LaggedStart(*[Transform(l, o) for l, o in zip(rem_lines, rem_orig)],
                                  lag_ratio=0.1), FadeOut(arrow), FadeOut(qmark),
                      run_time=beat.until_end_of("guess"))
            # magnifier on one person's neighborhood
            mag = Circle(radius=0.42, color=INK, stroke_width=2.5).move_to(node_pos(0))
            beat.wait_until("ring", offset=-0.3)
            self.play(Create(mag), run_time=0.8)
            # two strangers across the ring
            a, b = 57, 157
            sa = Circle(radius=0.16, color=PURPLE, stroke_width=3).move_to(dots[a])
            sb = Circle(radius=0.16, color=PURPLE, stroke_width=3).move_to(dots[b])
            beat.wait_until("strangers", offset=-0.2)
            self.play(Create(sa), Create(sb), run_time=0.8)
            gap = DashedLine(dots[a].get_center(), dots[b].get_center(), color=PURPLE,
                             stroke_width=2.5, dash_length=0.12)
            self.play(Create(gap), run_time=beat.remaining(0.6))

        # ============================================================ SCORE THE RING
        with self.narrate("So score every network on two numbers. The first is L, the "
                          "average trip: twenty-five point four steps on the ring.") as beat:
            self.play(FadeOut(gap), FadeOut(sa), FadeOut(sb), run_time=beat.until("two", offset=-0.1))
            self.play(Indicate(L_num, color=PURPLE, scale_factor=1.06), run_time=0.9)
            beat.wait_until("twenty", offset=-0.2)
            self.play(Create(underline(L_num[1], color=PURPLE)), run_time=0.6)
            ul_L = self.mobjects[-1]
            self.play(FadeOut(ul_L), run_time=beat.remaining(0.5))

        # inset: one person (centre) and four friends, laid out in a row
        xs = [0.75, 2.1, 3.45, 4.8, 6.0]
        ys = -0.55
        ring_ids = [N - 2, N - 1, 0, 1, 2]
        idots = VGroup(*[Dot([x, ys, 0], radius=0.13, color=BLUE) for x in xs]).set_z_index(3)
        idots[2].set_color(INK)
        P = [d.get_center() for d in idots]

        def ilink(i, j, color=BLUE, width=4):
            if j - i == 1:
                return Line(P[i], P[j], color=color, stroke_width=width)
            return ArcBetweenPoints(P[i], P[j], angle=-PI / 2.2, color=color, stroke_width=width)
        ilinks = {(i, j): ilink(i, j) for i in range(5) for j in range(i + 1, 5) if j - i <= 2}
        stubs = VGroup(Line(P[0] + LEFT * 0.6, P[0], color=BLUE, stroke_width=4, stroke_opacity=0.35),
                       Line(P[4], P[4] + RIGHT * 0.35, color=BLUE, stroke_width=4, stroke_opacity=0.35))
        inset = VGroup(*ilinks.values())
        with self.narrate("The second is clustering, C. Take one person. Their four friends "
                          "make six possible pairs, and three of those pairs are friends with "
                          "each other.") as beat:
            self.play(FadeIn(C_num, shift=0.2 * LEFT), FadeIn(C_cap),
                      run_time=beat.until("Take", offset=-0.1))
            self.play(LaggedStart(*[TransformFromCopy(dots[r], idots[k])
                                    for k, r in enumerate(ring_ids)], lag_ratio=0.1),
                      run_time=1.0)
            self.play(Create(inset), FadeIn(stubs), run_time=beat.until("six", offset=-0.2))
            # six pairs among the four friends: three missing ones dashed below
            missing = [(0, 3), (1, 4), (0, 4)]
            dashes = VGroup(*[DashedVMobject(ArcBetweenPoints(P[i], P[j], angle=PI / 2.6 + 0.1 * (j - i),
                                                              color=GRAY, stroke_width=3),
                                             num_dashes=14 + 3 * (j - i)) for i, j in missing])
            friend_pairs = [(0, 1), (1, 3), (3, 4)]
            self.play(Create(dashes), *[ilinks[p].animate.set_stroke(INK, width=6) for p in friend_pairs],
                      run_time=1.0)
            self.play(*[ilinks[p].animate.set_stroke(BLUE, width=4) for p in friend_pairs],
                      run_time=beat.until("three", offset=-0.15))
            self.play(*[ilinks[p].animate.set_stroke(GREEN, width=7) for p in friend_pairs],
                      run_time=0.8)

        frac = formula(r"C", "=", r"\frac{3}{6}", "=", r"0.5", size=EQ).move_to([3.4, -2.35, 0])
        frac[0].set_color(GREEN)
        frac[4].set_color(GREEN)
        with self.narrate("Three out of six: C is one half.") as beat:
            self.play(Write(frac[0:2]), TransformFromCopy(VGroup(*[ilinks[p] for p in friend_pairs]),
                                                          frac[2]), run_time=1.0)
            self.play(Write(frac[3:]), run_time=0.7)
            self.play(flag(C_num), run_time=beat.remaining(0.6))

        # ============================================================ THE MAP
        ax = axes((0, 27), (0, 0.55), x_length=5.2, y_length=3.0,
                  x_ticks=[0, 5, 10, 15, 20, 25], y_ticks=[0, 0.1, 0.2, 0.3, 0.4, 0.5],
                  y_decimals=1, x_label="average trip L (steps)", y_label="clustering C")
        ax.x_title.set_color(PURPLE)
        ax.y_title.set_color(GREEN)
        ax.move_to([3.45, -0.75, 0])
        goal = DashedVMobject(RoundedRectangle(width=ax.c2p(7.5, 0)[0] - ax.c2p(0.4, 0)[0],
                                               height=ax.c2p(0, 0.54)[1] - ax.c2p(0, 0.36)[1],
                                               corner_radius=0.12, color=INK, stroke_width=2.5),
                              num_dashes=40)
        goal.move_to((ax.c2p(0.4, 0.36) + ax.c2p(7.5, 0.54)) / 2)
        goal_lbl = label("goal", size=26, color=INK).next_to(goal, DOWN, buff=0.12)

        def map_point(L, C, name, direction, color=INK):
            d = Dot(ax.c2p(L, C), radius=0.09, color=color).set_z_index(4)
            t = label(name, size=26, color=color).next_to(d, direction, buff=0.15)
            return VGroup(d, t)
        p_ring = map_point(L0, C0, "ring", DOWN)

        with self.narrate("Put both numbers on a map. A real social network belongs up here, "
                          "in the corner: short trips, high clustering. The ring sits far to "
                          "the right.") as beat:
            self.play(FadeOut(inset), FadeOut(stubs), FadeOut(dashes), FadeOut(idots), FadeOut(frac),
                      FadeOut(mag), run_time=0.6)
            self.play(Create(ax), run_time=beat.until("real", offset=-0.2))
            beat.wait_until("up here", offset=-0.2)
            self.play(Create(goal), FadeIn(goal_lbl), run_time=1.0)
            beat.wait_until("ring sits", offset=-0.2)
            self.play(TransformFromCopy(VGroup(L_num, C_num), p_ring[0]), run_time=1.0)
            self.play(FadeIn(p_ring[1]), run_time=beat.remaining(0.5))

        # ============================================================ NAIVE FIX: all random
        rand_edges = [tuple(e) for e in D["random_edges"]]
        rng = np.random.default_rng(3)
        order = rng.permutation(len(rand_edges))
        rand_targets = [link(*rand_edges[j], color=YELLOW, width=1.0, opacity=0.45) for j in order]
        lattice_orig = [l.copy() for l in link_group]
        p_rand = map_point(Lr, Cr, "random", UR)
        p_rand[1].shift(RIGHT * 0.1)
        with self.narrate("The obvious fix for long trips is to rewire all four hundred links "
                          "at random.") as beat:
            beat.wait_until("rewire", offset=-0.2)
            self.play(LaggedStart(*[Transform(l, t) for l, t in zip(link_group, rand_targets)],
                                  lag_ratio=0.004), run_time=beat.remaining(1.5))

        with self.narrate("Trips collapse to four steps. But clustering crashes to point oh "
                          "one eight, nearly thirty times lower. Friends of friends are now "
                          "strangers.") as beat:
            self.play(Lt.animate.set_value(Lr), run_time=beat.until_end_of("steps"))
            beat.wait_until("crashes", offset=-0.2)
            self.play(Ct.animate.set_value(Cr), run_time=beat.until_end_of("eight"))
            self.play(TransformFromCopy(VGroup(L_num, C_num), p_rand[0]), run_time=1.0)
            self.play(FadeIn(p_rand[1]), run_time=0.6)
            self.play(Indicate(C_num, color=RED, scale_factor=1.08), run_time=beat.remaining(0.8))

        # ============================================================ IN BETWEEN: 8 links
        p8 = map_point(L8, C8, "8 rewired", DOWN, color=YELLOW)
        with self.narrate("Neither network reaches the corner. So go back to the ring, and "
                          "rewire only eight links: two percent.") as beat:
            self.play(Indicate(goal, color=INK, scale_factor=1.04), run_time=beat.until("So", offset=-0.1))
            self.play(LaggedStart(*[Transform(l, o) for l, o in zip(link_group, lattice_orig)],
                                  lag_ratio=0.002), Lt.animate.set_value(L0), Ct.animate.set_value(C0),
                      run_time=beat.until("eight", offset=-0.1))
            for l, o in zip(rem_lines, rem_orig):
                pass
            self.play(LaggedStart(*[Transform(l, t.copy()) for l, t in zip(rem_lines, chord_targets)],
                                  lag_ratio=0.2), run_time=beat.remaining(1.2))

        with self.narrate("The average trip falls from twenty-five point four to eleven point "
                          "five: less than half. Clustering barely moves, to point four "
                          "eight.") as beat:
            beat.wait_until("falls", offset=-0.1)
            self.play(Lt.animate.set_value(L8), run_time=beat.until_end_of("five"))
            beat.wait_until("Clustering", offset=-0.1)
            self.play(Ct.animate.set_value(C8), run_time=1.0)
            self.play(TransformFromCopy(VGroup(L_num, C_num), p8[0]), run_time=1.0)
            self.play(FadeIn(p8[1]), run_time=beat.remaining(0.5))

        # ============================================================ INSIGHT 1: triangles
        map_group = VGroup(ax, goal, goal_lbl, p_ring, p_rand, p8)
        tri = [(2, 3), (3, 4), (2, 4)]
        idots2 = idots.copy()
        inset2 = VGroup(*[ilink(i, j) for (i, j) in ilinks]).set_z_index(1)
        inset_all = VGroup(inset2, idots2).shift(UP * 1.35)
        P2 = [d.get_center() for d in idots2]
        tri_links = VGroup(*[inset2[list(ilinks).index(e)] for e in tri])
        with self.narrate("Why so lopsided? Clustering is made of triangles like this one, and "
                          "a triangle breaks only if one of its own three links gets "
                          "rewired.") as beat:
            self.play(FadeOut(map_group), run_time=0.6)
            mag.move_to(node_pos(1))
            self.play(Create(mag), LaggedStart(*[TransformFromCopy(dots[r], idots2[k])
                                                 for k, r in enumerate(ring_ids)], lag_ratio=0.1),
                      run_time=1.0)
            self.play(Create(inset2), run_time=beat.until("triangles", offset=-0.2))
            self.play(*[l.animate.set_stroke(GREEN, width=7) for l in tri_links],
                      idots2[3].animate.set_color(GREEN), idots2[4].animate.set_color(GREEN),
                      idots2[2].animate.set_color(GREEN), run_time=0.8)
            beat.wait_until("three links", offset=-0.2)
            self.play(LaggedStart(*[Indicate(l, color=GREEN, scale_factor=1.15) for l in tri_links],
                                  lag_ratio=0.3), run_time=1.0)

        # survival labels on each triangle link, then the formula built from them
        surv = VGroup(*[formula(r"1-p", size=MATH_SMALL + 4, color=INK) for _ in tri])
        surv[0].next_to(tri_links[0], DOWN, buff=0.15)
        surv[1].next_to(tri_links[1], DOWN, buff=0.15)
        surv[2].next_to(tri_links[2], UP, buff=0.12)
        for s in surv:
            s.set_color_by_tex("p", YELLOW)
        eq1 = formula(r"C(p)", r"\approx", r"C(0)", r"\,(1-p)^3", size=EQ).move_to([3.4, -0.75, 0])
        eq1[0].set_color(GREEN)
        eq1[2].set_color(GREEN)
        cite_bw = citation("Barrat & Weigt, 2000 · Eur. Phys. J. B")
        with self.narrate("Each link survives with probability one minus p, so the triangle "
                          "survives with one minus p, cubed, and so does clustering.") as beat:
            self.play(LaggedStart(*[FadeIn(s, shift=0.1 * DOWN) for s in surv], lag_ratio=0.3),
                      run_time=beat.until("so the", offset=-0.1))
            self.play(TransformFromCopy(surv, eq1[3]), run_time=beat.until("and so", offset=-0.1))
            self.play(Write(eq1[0:3]), FadeIn(cite_bw), run_time=beat.remaining(0.8))

        eq2 = formula(r"0.98^3", r"\approx", r"0.94", size=EQ).next_to(eq1, DOWN, buff=0.5)
        eq2[0].set_color(YELLOW)
        eq2[2].set_color(GREEN)
        with self.narrate("With p at two percent, that is point nine eight cubed, about point "
                          "nine four. Ninety-four percent of the clustering stays.") as beat:
            beat.wait_until("point nine eight", offset=-0.2)
            self.play(TransformFromCopy(eq1[3], eq2[0]), run_time=beat.until("about", offset=-0.1))
            self.play(Write(eq2[1:]), run_time=0.8)
            beat.wait_until("Ninety", offset=-0.1)
            self.play(flag(eq2[2], color=GREEN), flag(C_num, color=GREEN), run_time=0.9)

        # ============================================================ INSIGHT 2: trips use every link
        hop2 = ValueTracker(0)
        hop_ring_lbl = formula(r"\text{ring: } 50 \text{ hops}", size=MATH, color=GRAY)
        hop_now = live_number(hop2, 0, size=EQ, color=PURPLE, prefix=r"\text{now:}",
                              suffix=r"\text{hops}")
        hops_block = VGroup(hop_ring_lbl, hop_now).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        hops_block.move_to([3.4, -2.0, 0])
        upd8 = self.wave(dots, D["hops_8"], hop2)
        with self.narrate("Trips are different. A note can walk to any shortcut and jump, so "
                          "each of the eight serves all two hundred people.") as beat:
            self.play(FadeOut(eq1), FadeOut(eq2), FadeOut(surv), FadeOut(inset_all), FadeOut(mag),
                      FadeOut(cite_bw), run_time=0.6)
            chords = VGroup(*rem_lines)
            beat.wait_until("shortcut", offset=-0.2)
            self.play(LaggedStart(*[Indicate(c, color=YELLOW, scale_factor=1.03) for c in chords],
                                  lag_ratio=0.15), run_time=beat.until("each", offset=-0.1))
            beat.wait_until("all two", offset=-0.1)
            self.play(LaggedStart(*[Indicate(d, color=INK, scale_factor=1.8) for d in dots],
                                  lag_ratio=0.004), run_time=beat.remaining(1.0))

        with self.narrate("On the ring, a note needed fifty hops to reach everyone. Now watch "
                          "it spread: it needs seventeen.") as beat:
            self.play(FadeIn(hop_ring_lbl, shift=0.1 * UP), run_time=beat.until_end_of("everyone"))
            dots.add_updater(upd8)
            self.add(hop_now)
            beat.wait_until("watch", offset=-0.1)
            self.play(hop2.animate.set_value(17), run_time=beat.until("seventeen", offset=0.1),
                      rate_func=LINEAR)
            self.play(flag(hop_now, color=PURPLE), run_time=0.8)
            dots.remove_updater(upd8)

        # ============================================================ THE SWEEP
        ps = np.array(D["ps"])
        Lc = np.array(D["Lc"]) * L0
        Cc = np.array(D["Cc"]) * C0
        lp = np.log10(ps)
        t = ValueTracker(-3.4)   # log10 p ; below -3 = ring point (p = 0)

        def state(v):
            if v <= -3:
                a = (v + 3.4) / 0.4
                return (L0 + a * (Lc[0] - L0), C0 + a * (Cc[0] - C0))
            return (float(np.interp(v, lp, Lc)), float(np.interp(v, lp, Cc)))
        pval = ValueTracker(0.0)
        p_num = live_number(pval, 3, size=MATH, color=YELLOW, prefix=r"p =")
        sim_note = label("simulated · n = 200, k = 4, 100 runs per p", size=22, color=GRAY)
        with self.narrate("Now slide the rewiring fraction, p, from a tenth of a percent up to "
                          "every link.") as beat:
            self.play(FadeOut(hops_block), dots.animate.set_fill(BLUE), run_time=0.6)
            for d in dots:
                d.set_width(2 * DOT_R)
            self.play(FadeIn(map_group), run_time=0.8)
            tracer = Dot(ax.c2p(L0, C0), radius=0.1, color=YELLOW).set_z_index(5)
            tracer.add_updater(lambda m: m.move_to(ax.c2p(*state(t.get_value()))))
            trail = TracedPath(tracer.get_center, stroke_color=YELLOW, stroke_width=4)
            p_num.next_to(ax.c2p(27, 0.55), DOWN + LEFT, buff=0.0).shift(DOWN * 0.05)
            p_num.move_to([4.6, 1.75, 0])
            sim_note.next_to(ax.x_title, DOWN, buff=0.12).align_to(ax.x_title, RIGHT)
            self.add(trail, tracer)
            self.play(FadeIn(p_num), FadeIn(sim_note), dim(p_ring, p_rand, p8, opacity=0.35),
                      run_time=beat.remaining(0.6))

        pval.add_updater(lambda m: m.set_value(0 if t.get_value() <= -3 else 10 ** t.get_value()))
        self.add(pval)
        dC = label("C: −10.5%", size=28, color=GREEN)
        dL = label("L: −65%", size=28, color=PURPLE)
        with self.narrate("The network races left along the top. By the time clustering has "
                          "lost ten percent, trips are already two thirds shorter.") as beat:
            self.play(t.animate.set_value(np.log10(0.0398)), run_time=beat.until("lost", offset=0.2),
                      rate_func=EASE)
            dl = VGroup(dL, dC).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
            dl.next_to(tracer, DOWN + RIGHT, buff=0.25)
            self.play(FadeIn(dl, shift=0.1 * UP), run_time=0.8)
            self.play(Indicate(dl, color=INK, scale_factor=1.04), run_time=beat.remaining(0.6))

        sw_lbl = label("small world", size=30, color=INK).next_to(goal, UP, buff=0.12)
        sw_lbl.align_to(goal, LEFT)
        with self.narrate("Only near the end does clustering fall. That top-left corner, short "
                          "and cliquish, is the small world.") as beat:
            self.play(FadeOut(dl), t.animate.set_value(0), run_time=beat.until("That", offset=-0.1),
                      rate_func=EASE)
            beat.wait_until("small world", offset=-0.2)
            self.play(Write(sw_lbl), Indicate(goal, color=INK, scale_factor=1.03), run_time=1.0)

        # ============================================================ PAYOFF
        tracer.clear_updaters()
        pval.clear_updaters()
        sweep_group = VGroup(map_group, trail, tracer, p_num, sim_note, sw_lbl)
        hdr_a = label("film actors", size=28, color=INK)
        hdr_b = label("random graph", size=28, color=GRAY)
        rowL = formula(r"L", size=EQ, color=PURPLE)
        rowC = formula(r"C", size=EQ, color=GREEN)
        vLa = formula(r"3.65", size=EQ, color=PURPLE)
        vLb = formula(r"2.99", size=EQ, color=GRAY)
        vCa = formula(r"0.79", size=EQ, color=GREEN)
        vCb = formula(r"0.00027", size=EQ, color=GRAY)
        cx = [0.6, 2.75, 5.15]
        hdr_a.move_to([cx[1], 2.0, 0]); hdr_b.move_to([cx[2], 2.0, 0])
        rowL.move_to([cx[0], 1.0, 0]); vLa.move_to([cx[1], 1.0, 0]); vLb.move_to([cx[2], 1.0, 0])
        rowC.move_to([cx[0], -0.1, 0]); vCa.move_to([cx[1], -0.1, 0]); vCb.move_to([cx[2], -0.1, 0])
        times = formula(r"\approx 2{,}900\times", size=MATH, color=GREEN).move_to([3.95, -1.05, 0])
        cite_ws = citation("Watts & Strogatz, 1998 · Nature")
        with self.narrate("Watts and Strogatz found real networks in this corner in nineteen "
                          "ninety-eight. Film actors clustered at point seven nine, nearly three "
                          "thousand times a random graph of the same size.") as beat:
            self.play(FadeOut(sweep_group), FadeOut(L_num), FadeOut(C_num), FadeOut(L_cap),
                      FadeOut(C_cap), dim(dots, link_group, opacity=0.3), FadeOut(sim_tag),
                      run_time=0.8)
            self.play(FadeIn(cite_ws), FadeIn(hdr_a), FadeIn(hdr_b),
                      run_time=beat.until("Film", offset=-0.2))
            self.play(FadeIn(rowC), FadeIn(vCa, shift=0.1 * UP), run_time=beat.until("nearly", offset=-0.1))
            self.play(FadeIn(vCb, shift=0.1 * UP), run_time=0.7)
            self.play(Write(times), run_time=beat.remaining(0.8))

        with self.narrate("Yet their average trip, three point six five steps, stayed close to "
                          "random's three.") as beat:
            self.play(FadeIn(rowL), FadeIn(vLa, shift=0.1 * UP), run_time=beat.until("stayed", offset=-0.1))
            self.play(FadeIn(vLb, shift=0.1 * UP), run_time=beat.remaining(0.7))

        table = VGroup(hdr_a, hdr_b, rowL, rowC, vLa, vLb, vCa, vCb, times)
        fb_lbl = label("Facebook, 2011: 721 million users", size=30, color=INK)
        fb_val = formula(r"L", "=", r"4.74", size=72, color=PURPLE)
        ring_val = formula(r"L", "=", r"25.4", size=MATH, color=GRAY)
        ring_lbl = label("our ring: 200 people", size=26, color=GRAY)
        fb = VGroup(fb_lbl, fb_val).arrange(DOWN, buff=0.35).move_to([3.4, 1.2, 0])
        rr = VGroup(ring_lbl, ring_val).arrange(RIGHT, buff=0.35).move_to([3.4, -0.6, 0])
        cite_fb = citation("Backstrom et al., 2012 · Four Degrees of Separation, WebSci")
        with self.narrate("And in twenty eleven, Facebook's seven hundred twenty-one million "
                          "active users sat an average of four point seven four hops "
                          "apart.") as beat:
            self.play(FadeOut(table), FadeOut(cite_ws), run_time=0.6)
            self.play(FadeIn(fb_lbl), FadeIn(cite_fb), FadeIn(rr), run_time=beat.until("average", offset=-0.2))
            self.play(Write(fb_val), run_time=beat.remaining(1.0))

        # Milgram: 296 chains, 64 arrived
        cols, rows_ = 37, 8
        cells = VGroup(*[Square(0.12, stroke_width=0, fill_opacity=1, fill_color=DIM)
                         for _ in range(296)])
        cells.arrange_in_grid(rows=rows_, cols=cols, buff=0.045).move_to([3.3, -0.2, 0])
        mg_lbl = label("letter chains started: 296", size=28, color=INK).next_to(cells, UP, buff=0.3)
        arrived = formula(r"64", r"\text{ arrived}", size=MATH, color=PURPLE).next_to(cells, DOWN, buff=0.3)
        cite_mg = citation("Travers & Milgram, 1969 · Sociometry")
        with self.narrate("Short paths are not easy to find, though. Of the two hundred ninety-six "
                          "letter chains in Milgram's study, only sixty-four reached their "
                          "target.") as beat:
            self.play(FadeOut(fb), FadeOut(rr), FadeOut(cite_fb), run_time=0.6)
            beat.wait_until("two hundred", offset=-0.2)
            self.play(LaggedStart(*[FadeIn(c) for c in cells], lag_ratio=0.004), FadeIn(mg_lbl),
                      FadeIn(cite_mg), run_time=beat.until("only", offset=-0.1))
            self.play(LaggedStart(*[c.animate.set_fill(PURPLE) for c in cells[:64]], lag_ratio=0.01),
                      run_time=beat.until("reached", offset=0.1))
            self.play(Write(arrived), run_time=beat.remaining(0.7))

        # ============================================================ LANDING
        idots3 = idots.copy()
        inset3 = VGroup(*[ilink(i, j) for (i, j) in ilinks])
        local = VGroup(inset3, idots3).move_to([3.4, 0.4, 0])
        with self.narrate("Stand anywhere on this ring, and your neighborhood looks just as it "
                          "did.") as beat:
            self.play(FadeOut(cells), FadeOut(mg_lbl), FadeOut(arrived), FadeOut(cite_mg),
                      undim(dots, link_group), run_time=0.8)
            for l in link_group:
                l.set_stroke(opacity=0.75)
            for c in rem_lines:
                c.set_stroke(opacity=1)
            mag.move_to(node_pos(0))
            self.play(Create(mag), LaggedStart(*[TransformFromCopy(dots[r], idots3[k])
                                                 for k, r in enumerate(ring_ids)], lag_ratio=0.1),
                      run_time=1.0)
            self.play(Create(inset3), run_time=beat.remaining(0.8))

        with self.narrate("The world got less than half as wide, through eight links you cannot "
                          "see from where you stand.") as beat:
            self.play(Lt.animate.set_value(L8), run_time=0.1)
            beat.wait_until("eight", offset=-0.15)
            self.play(LaggedStart(*[Indicate(c, color=YELLOW, scale_factor=1.03) for c in rem_lines],
                                  lag_ratio=0.15), run_time=beat.remaining(1.0))

        self.end_card()
