"""Episode 93 - The Strange Bump at 20 Friends (algorithmic confounding).

    videos/toolkit/render.sh videos/episodes/093-algorithmic-confounding/scene.py Episode \
        videos/episodes/093-algorithmic-confounding/final.mp4
"""
import sys
from pathlib import Path

import numpy as np
import networkx as nx
from manim import *
from sample_space import *

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sim import run  # noqa: E402

SEED = 30
N_PEOPLE, M0 = 48, 60
LOG5000 = np.log10(5000)


# ----------------------------------------------------------------- schematic degree curve
def smooth_curve(x):
    return -1.7 - 0.55 * x - 0.33 * x ** 2


def nudge(x):
    return (-0.22 * np.exp(-((x - 1.12) / 0.09) ** 2)
            + 0.34 * np.exp(-((x - 1.32) / 0.045) ** 2))


def frac(num, den, size=EQ, color_num=INK, color_den=INK):
    """A stacked fraction from two independent MathTex parts (so each can be transformed)."""
    n = MathTex(num, font_size=size, color=color_num)
    d = MathTex(den, font_size=size, color=color_den)
    w = max(n.width, d.width) + 0.2
    bar = Line(LEFT * w / 2, RIGHT * w / 2, stroke_width=3, color=INK)
    n.next_to(bar, UP, buff=0.14)
    d.next_to(bar, DOWN, buff=0.14)
    return VGroup(n, bar, d)


class Episode(NarratedScene):
    EPISODE = 93
    TITLE = "The Strange Bump at 20 Friends"
    PRONUNCIATIONS = {"Salganik": "sal guh nick"}

    # ------------------------------------------------------------------ pieces
    def degree_plot(self):
        ax = axes((0, 3.9), (-9, -1), x_length=10.2, y_length=5.0, numbers=False,
                  x_ticks=[0, 1, 2, 3, LOG5000], y_ticks=[-8, -6, -4, -2],
                  y_label="share of users (log scale)")
        ax.move_to(DOWN * 0.25 + RIGHT * 0.35)
        ticks = VGroup()
        for v, s in [(0, "1"), (1, "10"), (2, "100"), (3, "1000"), (LOG5000, "5000")]:
            t = MathTex(s, font_size=MATH_SMALL, color=GRAY)
            t.next_to(ax.c2p(v, -9), DOWN, buff=0.2)
            ticks.add(t)
        xt = Text("friends (log scale)", font=SERIF, font_size=LABEL, color=GRAY)
        xt.next_to(ticks, DOWN, buff=0.18).align_to(ax.x_axis.get_right(), RIGHT)
        tag = text("schematic redraw of the paper's Fig. 1", size=SMALL, color=GRAY)
        tag.move_to(ax.c2p(3.9, -1.2), aligned_edge=RIGHT)
        return ax, ticks, xt, tag

    def construct(self):
        # ---------------------------------------------------------- data
        g0, res = run(N_PEOPLE, M0, 1, SEED)
        pos = nx.spring_layout(g0, seed=4, k=0.33, iterations=200)
        P = np.array([pos[i] for i in range(N_PEOPLE)])
        P = P - P.mean(axis=0)
        P = P / np.max(np.linalg.norm(P, axis=1)) * 2.15

        # ========================================================== 0 cold open
        ax, ticks, xt, tag = self.degree_plot()
        s = ValueTracker(1.0)
        xs = np.linspace(0, LOG5000, 700)

        def curve_pts():
            return [ax.c2p(x, smooth_curve(x) + s.get_value() * nudge(x)) for x in xs]

        curve = VMobject(stroke_color=BLUE, stroke_width=5)
        curve.set_points_smoothly(curve_pts())
        kink_pt = ax.c2p(1.25, smooth_curve(1.25))
        ring = DashedVMobject(Circle(radius=0.55, color=GRAY, stroke_width=3), num_dashes=24)
        ring.move_to(kink_pt)
        ring_lbl = MathTex(r"\approx 20", font_size=MATH_SMALL, color=GRAY)
        ring_lbl.next_to(ring, UP, buff=0.15)
        plot = VGroup(ax, ticks, xt, tag)

        with self.narrate("These are the friend counts of seven hundred and twenty one million "
                          "Facebook users, in May twenty eleven. The curve falls smoothly, except "
                          "for one small kink, near twenty friends. Is that kink about people, "
                          "or about the website? [pause 1.5]") as beat:
            self.play(FadeIn(ax), FadeIn(ticks), FadeIn(xt), run_time=0.8)
            self.play(Create(curve), run_time=beat.until("May", offset=-0.2), rate_func=EASE)
            self.play(FadeIn(tag), run_time=0.6)
            beat.wait_until("kink", offset=-0.2)
            self.play(Create(ring), FadeIn(ring_lbl, shift=0.1 * DOWN), run_time=0.9)
            beat.wait_until("people", offset=-0.1)
            self.play(Indicate(curve, color=BLUE, scale_factor=1.0), run_time=0.9)
            beat.wait_until("website", offset=-0.1)
            self.play(ax.x_axis.animate.set_color(GRAY), run_time=0.4)
            # prediction hold: the ring breathes once so the frame is not frozen
            self.play(ring.animate.scale(1.12), run_time=1.0, rate_func=there_and_back)

        # ========================================================== 1 reveal
        curve.add_updater(lambda m: m.set_points_smoothly(curve_pts()))
        cite1 = citation("Ugander, Karrer, Backstrom & Marlow, 2011 · arXiv:1111.4503")
        arrows = VGroup(*[
            CurvedArrow(ax.c2p(x0, smooth_curve(x0) + 0.9), ax.c2p(1.31, smooth_curve(1.31) + 0.75),
                        angle=-PI / 2.2, color=YELLOW, stroke_width=4, tip_length=0.18)
            for x0 in (0.92, 1.08)])
        wall = Line(ax.c2p(LOG5000, -9), ax.c2p(LOG5000, -1.6), color=YELLOW, stroke_width=6)
        wall_lbl = text("cap: 5,000", size=LABEL, color=YELLOW)
        wall_lbl.next_to(wall, LEFT, buff=0.2).align_to(ax.c2p(0, -6.6), UP)
        with self.narrate("Facebook's own researchers explained it. The product pushed people "
                          "with few friends to keep adding them, until they reached twenty. And "
                          "the curve stops dead at five thousand, because Facebook capped friend "
                          "lists there.") as beat:
            self.play(FadeIn(cite1), s.animate.set_value(0.0), run_time=beat.until("pushed", offset=-0.1))
            self.play(LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.3),
                      s.animate.set_value(1.0), ring.animate.set_color(YELLOW),
                      ring_lbl.animate.set_color(YELLOW),
                      run_time=beat.until("twenty", end=True), rate_func=SMOOTH)
            beat.wait_until("stops", offset=-0.1)
            self.play(Create(wall), run_time=0.9)
            self.play(FadeIn(wall_lbl, shift=0.1 * LEFT), run_time=0.6)
        curve.clear_updaters()

        # ========================================================== 2 stakes
        with self.narrate("So the most basic statistic of the largest social network anyone had "
                          "analyzed carries the platform's fingerprints. A kink is easy to spot. "
                          "The dangerous case is a pattern that looks like a law of human "
                          "behaviour.") as beat:
            beat.wait_until("fingerprints", offset=-0.2)
            self.play(flag(VGroup(ring, arrows)), flag(VGroup(wall, wall_lbl)), run_time=1.0)
            beat.wait_until("spot", offset=-0.3)
            self.play(FadeOut(arrows), run_time=0.6)
            beat.wait_until("dangerous", offset=-0.2)
            self.play(FadeOut(VGroup(plot, curve, ring, ring_lbl, wall, wall_lbl, cite1), shift=LEFT * 0.6),
                      run_time=beat.until("law", offset=-0.1))

        # ========================================================== 3 ego network
        E = np.array([-3.4, -0.35, 0])
        R = 2.05
        F = [E + R * np.array([np.cos(a), np.sin(a), 0])
             for a in np.deg2rad(90 + 72 * np.arange(5))]
        ego = Dot(E, radius=0.16, color=BLUE)
        friends = VGroup(*[Dot(p, radius=0.12, color=BLUE) for p in F])
        spokes = VGroup(*[Line(E, p, color=GRAY, stroke_width=3) for p in F])
        pairs = {(i, j): DashedLine(F[i], F[j], color=DIM, stroke_width=3, dash_length=0.12)
                 for i in range(5) for j in range(i + 1, 5)}
        dashed = VGroup(*pairs.values())
        linked = [(0, 1), (2, 4)]
        links = VGroup(*[Line(F[i], F[j], color=BLUE, stroke_width=5) for i, j in linked])
        for m in (ego, friends):
            m.set_z_index(3)

        C1 = MathTex("C", "=", font_size=EQ)
        f1 = frac("2", "10", color_num=BLUE, color_den=GRAY)
        v1 = MathTex(r"=", r"0.2", font_size=EQ)
        line1 = VGroup(C1, f1, v1).arrange(RIGHT, buff=0.25).move_to([2.6, 1.85, 0])
        f1[0].set_color(BLUE)
        clu_lbl = text("clustering", size=LABEL, color=GRAY).next_to(C1, DOWN, buff=0.35)
        with self.narrate("Here is one person with five friends. Five friends make ten possible "
                          "pairs, and two of those pairs are friends themselves. Two out of ten "
                          "is this person's clustering.") as beat:
            self.play(GrowFromCenter(ego), run_time=0.6)
            self.play(LaggedStart(*[Create(sp) for sp in spokes], lag_ratio=0.15),
                      LaggedStart(*[GrowFromCenter(f) for f in friends], lag_ratio=0.15),
                      run_time=beat.until("ten", offset=-0.1))
            self.play(LaggedStart(*[Create(d) for d in dashed], lag_ratio=0.12),
                      run_time=beat.until("two", offset=-0.1))
            self.play(LaggedStart(*[Create(l) for l in links], lag_ratio=0.4),
                      run_time=beat.until("Two out", offset=-0.2))
            self.play(Write(C1), TransformFromCopy(links, f1[0]), Create(f1[1]), run_time=0.9)
            self.play(TransformFromCopy(dashed, f1[2]), run_time=beat.until("clustering", offset=-0.1))
            self.play(Write(v1), FadeIn(clu_lbl, shift=0.1 * UP), run_time=0.8)

        # ========================================================== 4 general + real number
        k_lbl = MathTex("k", "=", "5", font_size=MATH, color=GRAY).next_to(ego, DOWN, buff=0.3)
        k_lbl.shift(LEFT * 0.35)
        C2 = MathTex("C", "=", font_size=EQ)
        f2 = frac("L", r"k(k-1)/2", color_num=BLUE, color_den=GRAY)
        line2 = VGroup(C2, f2).arrange(RIGHT, buff=0.25)
        line2.next_to(line1, DOWN, buff=1.0).align_to(line1, LEFT)
        L_lbl = text("links among friends", size=SMALL + 2, color=BLUE)
        L_lbl.next_to(f2[0], RIGHT, buff=0.3)
        fb = MathTex(r"k = 100:\quad C = 0.14", font_size=MATH)
        fb.next_to(line2, DOWN, buff=0.75).align_to(line1, LEFT)
        msn = text("about 5x an IM network, 2008", size=SMALL + 2, color=GRAY)
        msn.next_to(fb, DOWN, buff=0.22).align_to(fb, LEFT)
        cite2 = citation("Ugander et al., 2011 · arXiv  |  Leskovec & Horvitz, 2008 · WWW")
        with self.narrate("With k friends, the bottom is k times k minus one, over two. On "
                          "Facebook, people with a hundred friends score point one four, about "
                          "five times an instant messaging network studied in two thousand "
                          "eight.") as beat:
            self.play(FadeIn(k_lbl), FadeOut(clu_lbl), run_time=0.6)
            self.play(TransformFromCopy(C1, C2), TransformFromCopy(f1[1], f2[1]),
                      TransformFromCopy(f1[0], f2[0]), FadeIn(L_lbl),
                      run_time=beat.until("bottom", offset=-0.2))
            self.play(TransformFromCopy(f1[2], f2[2]), run_time=beat.until("over", end=True))
            beat.wait_until("Facebook", offset=-0.2)
            self.play(FadeIn(cite2), Write(fb), run_time=beat.until("point one four", end=True))
            self.play(FadeIn(msn, shift=0.1 * UP), run_time=0.8)

        # ========================================================== 5 the naive reading
        tri = Polygon(E, F[0], F[1], stroke_width=0, fill_color=BLUE, fill_opacity=0.28)
        tri.set_z_index(-1)
        reading = text("textbook reading: people close triangles", size=LABEL, color=INK)
        reading.next_to(ego, UP, buff=0).move_to([E[0], 3.15, 0])
        reading.align_to(np.array([-6.2, 0, 0]), LEFT)
        with self.narrate("The textbook reading is that people close triangles: your friends "
                          "meet, and become friends. So let's build people who never do that, "
                          "and measure.") as beat:
            self.play(FadeIn(reading, shift=0.1 * DOWN), run_time=0.8)
            beat.wait_until("triangles", offset=-0.2)
            self.play(FadeIn(tri), run_time=0.8)
            beat.wait_until("become", offset=-0.1)
            self.play(flag(links[0]), run_time=0.8)
            beat.wait_until("build", offset=-0.2)
            ego_all = VGroup(ego, friends, spokes, dashed, links, tri, k_lbl)
            formulas = VGroup(line1, line2, L_lbl, fb, msn)
            self.play(FadeOut(ego_all), FadeOut(formulas), FadeOut(reading), FadeOut(cite2),
                      run_time=beat.until("measure", offset=-0.1))

        # ========================================================== 6 simulation setup
        CL, CR = np.array([-3.35, -0.15, 0]), np.array([3.35, -0.15, 0])

        def panel(center):
            nodes = VGroup(*[Dot(center + np.array([*P[i], 0]), radius=0.085, color=BLUE)
                             for i in range(N_PEOPLE)])
            for d in nodes:
                d.set_z_index(3)
            base = VGroup(*[Line(nodes[a].get_center(), nodes[b].get_center(), color=GRAY,
                                 stroke_width=2.2, stroke_opacity=0.8) for a, b in g0.edges()])
            return nodes, base

        nL, bL = panel(CL)
        nR, bR = panel(CR)
        sim_tag = text("simulated: 48 people, 60 starting friendships", size=SMALL, color=GRAY)
        sim_tag.move_to([0, 3.35, 0])
        tL = text("random stranger", size=LABEL, color=BLUE).move_to(CL + UP * 2.95)
        tR = text("friend of a friend", size=LABEL, color=YELLOW).move_to(CR + UP * 2.95)

        def new_edges(nodes, adds, rule):
            g = VGroup()
            for (a, b, via) in adds:
                col = YELLOW if (rule == "fof" and via is not None) else BLUE
                g.add(Line(nodes[a].get_center(), nodes[b].get_center(), color=col,
                           stroke_width=3.2, stroke_opacity=0))
            return g

        eL = new_edges(nL, res["random"][2], "random")
        eR = new_edges(nR, res["fof"][2], "fof")
        trajL, trajR = res["random"][1], res["fof"][1]
        t = ValueTracker(0.0)

        def edge_upd(group):
            def f(g):
                tv = t.get_value()
                for i, e in enumerate(g):
                    e.set_stroke(opacity=float(np.clip(tv - i, 0, 1)))
            return f

        def counter(center, traj, color):
            pre = MathTex("C", "=", font_size=MATH)
            num = DecimalNumber(traj[0], num_decimal_places=2, font_size=MATH, color=color)
            grp = VGroup(pre, num).arrange(RIGHT, buff=0.18).move_to(center + DOWN * 2.75)
            num.add_updater(lambda m: m.set_value(traj[min(int(t.get_value()), len(traj) - 1)]))
            return grp

        cntL = counter(CL, trajL, INK)
        cntR = counter(CR, trajR, INK)
        with self.narrate("Here are forty eight simulated people with sixty random friendships, "
                          "copied twice. Each person adds one new friend. On the left, a stranger "
                          "picked at random. On the right, a suggestion: a friend of a friend. "
                          "Nobody on either side cares about triangles. Both start at point oh "
                          "four. Where does each side end up? [pause 1.5]") as beat:
            self.play(FadeIn(sim_tag),
                      LaggedStart(*[GrowFromCenter(d) for d in nL], lag_ratio=0.03),
                      run_time=beat.until("sixty", offset=-0.1))
            self.play(LaggedStart(*[Create(e) for e in bL], lag_ratio=0.03),
                      run_time=beat.until("copied", offset=-0.1))
            self.play(TransformFromCopy(VGroup(nL, bL), VGroup(nR, bR)), run_time=1.2)
            beat.wait_until("left", offset=-0.2)
            self.play(FadeIn(tL, shift=0.1 * DOWN), run_time=0.7)
            beat.wait_until("right", offset=-0.2)
            self.play(FadeIn(tR, shift=0.1 * DOWN), run_time=0.7)
            beat.wait_until("Nobody", offset=-0.1)
            self.play(Indicate(nL, color=BLUE, scale_factor=1.0),
                      Indicate(nR, color=BLUE, scale_factor=1.0), run_time=1.0)
            beat.wait_until("Both", offset=-0.2)
            self.play(FadeIn(cntL), FadeIn(cntR), run_time=0.8)
            beat.wait_until("Where", offset=-0.1)
            self.add(eL, eR)
            self.play(Circumscribe(cntL, color=GRAY, buff=0.12),
                      Circumscribe(cntR, color=GRAY, buff=0.12), run_time=1.6)

        # ========================================================== 7 run + measured failure
        eL.add_updater(edge_upd(eL))
        eR.add_updater(edge_upd(eR))
        cntL[1].clear_updaters()
        cntR[1].clear_updaters()
        cntL[1].add_updater(lambda m: m.set_value(trajL[min(int(t.get_value()), len(trajL) - 1)]))
        cntR[1].add_updater(lambda m: m.set_value(trajR[min(int(t.get_value()), len(trajR) - 1)]))
        with self.narrate("Run it, one new friendship at a time. Random strangers reach point oh "
                          "nine. The suggestions reach point four eight, more than five times as "
                          "high. A theory of human triangle closing would fit the right side "
                          "well, and the suggestion rule made every one of those "
                          "triangles.") as beat:
            self.play(t.animate.set_value(len(trajL) - 1 + 0.999),
                      run_time=beat.until("Random", offset=1.0), rate_func=LINEAR)
            beat.wait_until("point oh nine", offset=-0.2)
            self.play(flag(cntL), run_time=0.8)
            beat.wait_until("point four eight", offset=-0.2)
            self.play(flag(cntR), run_time=0.8)
            boxR = box(VGroup(nR, bR, eR), color=GRAY, buff=0.12)
            beat.wait_until("theory", offset=-0.1)
            self.play(Create(boxR), dim(bL, eL, nL), run_time=1.0)
            beat.wait_until("suggestion rule", offset=-0.1)
            yel = VGroup(*[e for e in eR if e.get_stroke_color().to_hex().upper() == YELLOW.upper()])
            for e in eR:
                e.clear_updaters()
            eR.clear_updaters()
            self.play(LaggedStart(*[e.animate.set_stroke(width=5.5) for e in yel], lag_ratio=0.02),
                      run_time=1.4)
        t.clear_updaters()
        for m in (eL, eR, cntL[1], cntR[1]):
            m.clear_updaters()

        # ========================================================== 8 insight
        self.play(FadeOut(VGroup(nL, bL, eL, nR, bR, eR, boxR, tL, tR, cntL, sim_tag)),
                  cntR.animate.scale(0.8).move_to([4.9, -2.75, 0]), run_time=0.7)
        f1b = frac("2", "10", color_num=BLUE, color_den=GRAY).move_to(f1)
        new_link = Line(F[1], F[2], color=YELLOW, stroke_width=6)
        num3 = MathTex("2", "+", "1", font_size=EQ).move_to(f1[0])
        num3[0].set_color(BLUE)
        num3[2].set_color(YELLOW)
        v3 = MathTex(r"=", r"0.3", font_size=EQ).move_to(v1)
        v3[1].set_color(YELLOW)
        with self.narrate("The reason is in the fraction. A friend of a friend suggestion exists "
                          "because of a shared friend, like this one. When it's accepted, her k "
                          "stays the same, and the top goes up by one. The algorithm writes "
                          "straight into the numerator.") as beat:
            self.play(FadeIn(VGroup(ego, friends, spokes, dashed, links, k_lbl)),
                      FadeIn(VGroup(line1, line2, L_lbl)), run_time=beat.until("suggestion", offset=-0.2))
            beat.wait_until("shared", offset=-0.1)
            self.play(Indicate(ego, color=BLUE, scale_factor=1.6),
                      Indicate(VGroup(spokes[1], spokes[2]), color=BLUE, scale_factor=1.0), run_time=1.0)
            beat.wait_until("accepted", offset=-0.1)
            self.play(Create(new_link), FadeOut(pairs[(1, 2)]), run_time=0.9)
            beat.wait_until("k stays", offset=-0.1)
            self.play(flag(k_lbl), run_time=0.8)
            beat.wait_until("top", offset=-0.1)
            num_c = num3.copy()
            self.play(ReplacementTransform(f1[0], num3[0]), FadeIn(num3[1]),
                      TransformFromCopy(new_link, num3[2]),
                      ReplacementTransform(v1, v3), run_time=1.2)
            beat.wait_until("numerator", offset=-0.3)
            nbox = box(num3, color=YELLOW)
            self.play(Create(nbox), run_time=0.8)

        # ========================================================== 9 payoff: the loop
        self.play(FadeOut(VGroup(ego, friends, spokes, dashed, links, k_lbl, new_link, line1,
                                 line2, L_lbl, num3, v3, nbox, f1[1], f1[2], cntR)),
                  run_time=0.6)
        term = text("algorithmic confounding", size=HEADING, color=INK).move_to([0, 3.05, 0])

        def node_box(s, color, at, w=2.7):
            t_ = text(s, size=LABEL, color=color)
            r = RoundedRectangle(width=max(w, t_.width + 0.5), height=0.95, corner_radius=0.12,
                                 color=color, stroke_width=3)
            return VGroup(r, t_.move_to(r)).move_to(at)

        people = node_box("people", BLUE, [-4.4, 1.3, 0])
        platform = node_box("platform code", YELLOW, [-4.4, -1.3, 0])
        data = node_box("data", INK, [0.4, 0, 0], w=2.2)
        theory = node_box("theory: triangles close", GRAY, [4.25, 1.6, 0], w=3.6)
        a_p = Arrow(people.get_right(), data.get_left() + UP * 0.2, color=BLUE, buff=0.15, stroke_width=4)
        a_c = Arrow(platform.get_right(), data.get_left() + DOWN * 0.2, color=YELLOW, buff=0.15, stroke_width=4)
        pymk = text("People You May Know", size=SMALL + 2, color=YELLOW)
        pymk.next_to(platform, DOWN, buff=0.22)
        a_t = Arrow(data.get_right(), theory.get_bottom() + LEFT * 0.6, color=GRAY, buff=0.15, stroke_width=3)
        conf = text("confirms", size=SMALL + 2, color=GRAY).next_to(a_t.get_center(), DR, buff=0.12)
        a_back = CurvedArrow(theory.get_bottom() + RIGHT * 0.6 + DOWN * 0.05,
                             platform.get_bottom() + RIGHT * 0.9 + DOWN * 0.05,
                             angle=-PI * 0.55, color=GRAY, stroke_width=3, tip_length=0.2)
        built = text("built in", size=SMALL + 2, color=GRAY)
        cite3 = citation("Salganik, 2018 · Bit by Bit (Princeton University Press)")
        with self.narrate("Matthew Salganik calls this algorithmic confounding: the platform is "
                          "part of the process that makes the data. Facebook does suggest friends "
                          "of friends, through People You May Know. So when Facebook data confirm "
                          "that triangles close, part of that confirmation was built into the "
                          "system.") as beat:
            self.play(FadeIn(cite3), Write(term), run_time=beat.until("platform", offset=-0.2))
            self.play(FadeIn(people), FadeIn(data), GrowArrow(a_p), run_time=0.8)
            self.play(FadeIn(platform), GrowArrow(a_c), run_time=beat.until("Facebook", offset=-0.2))
            beat.wait_until("People You", offset=-0.2)
            self.play(FadeIn(pymk, shift=0.1 * UP), run_time=0.7)
            beat.wait_until("confirm", offset=-0.2)
            self.play(GrowArrow(a_t), FadeIn(theory), FadeIn(conf), run_time=1.0)
            beat.wait_until("built", offset=-0.3)
            built.move_to(a_back.point_from_proportion(0.5) + DOWN * 0.35)
            self.play(Create(a_back), FadeIn(built), run_time=beat.remaining(min_time=1.0))

        # ========================================================== 10 honest limit
        BW = 4.4
        split = ValueTracker(0.5)
        bar_left = data.get_left()[0] - 1.1
        bar_y = -0.0

        def bar_parts():
            x0 = bar_left
            xm = x0 + BW * split.get_value()
            blue = Rectangle(width=max(xm - x0, 0.001), height=0.6, stroke_width=0,
                             fill_color=BLUE, fill_opacity=0.85).move_to([(x0 + xm) / 2, bar_y, 0])
            yel = Rectangle(width=max(x0 + BW - xm, 0.001), height=0.6, stroke_width=0,
                            fill_color=YELLOW, fill_opacity=0.85).move_to([(xm + x0 + BW) / 2, bar_y, 0])
            return VGroup(blue, yel)

        with self.narrate("From the traces alone, nobody can split point one four into people and "
                          "code. To split it, you have to break the loop: switch the suggestions "
                          "off for a random group, and see what's left.") as beat:
            bar = bar_parts()
            bar_lbl = MathTex(r"C = 0.14", font_size=MATH).next_to(bar, UP, buff=0.25)
            bar_lbl.align_to(bar, LEFT)
            q = MathTex("?", font_size=MATH, color=INK)
            q.add_updater(lambda m: m.move_to([bar_left + BW * split.get_value(), bar_y - 0.62, 0]))
            self.play(FadeOut(VGroup(theory, a_t, conf, a_back, built, cite3)),
                      data.animate.set_opacity(0), FadeIn(bar), FadeIn(bar_lbl), FadeIn(q),
                      a_p.animate.put_start_and_end_on(people.get_right(), [bar_left - 0.1, 0.15, 0]),
                      a_c.animate.put_start_and_end_on(platform.get_right(), [bar_left - 0.1, -0.15, 0]),
                      run_time=beat.until("split", offset=-0.1))
            bar.add_updater(lambda m: m.become(bar_parts()))
            self.play(split.animate.set_value(0.25), run_time=1.1, rate_func=EASE)
            self.play(split.animate.set_value(0.75), run_time=beat.until("break", offset=-0.1), rate_func=EASE)
            self.play(split.animate.set_value(0.5), run_time=0.8, rate_func=EASE)
            beat.wait_until("switch", offset=-0.1)
            cut = Cross(a_c, stroke_color=YELLOW, stroke_width=5, scale_factor=0.35)
            self.play(a_c.animate.set_opacity(0.3), pymk.animate.set_opacity(0.3), Create(cut),
                      run_time=0.9)
            beat.wait_until("left", offset=-0.2)
            self.play(split.animate.set_value(1.0), FadeOut(q), run_time=1.2)
            bar.clear_updaters()
            left_lbl = text("what's left: people", size=LABEL, color=BLUE)
            left_lbl.next_to(bar, DOWN, buff=0.3).align_to(bar, LEFT)
            self.play(FadeIn(left_lbl, shift=0.1 * UP), run_time=0.7)

        # ========================================================== 11 landing
        self.play(FadeOut(VGroup(*[m for m in self.mobjects])), run_time=0.6)
        s.set_value(1.0)
        curve.set_points_smoothly(curve_pts())
        ring.set_color(YELLOW)
        lbl_people = text("people", size=LABEL, color=BLUE).move_to(ax.c2p(2.35, -3.3))
        lbl_code = text("code", size=LABEL, color=YELLOW).next_to(ring, RIGHT, buff=0.25)
        lbl_code2 = text("code", size=LABEL, color=YELLOW).next_to(wall, LEFT, buff=0.2).align_to(wall_lbl, UP)
        with self.narrate("The kink at twenty is the rare case where the code left a visible mark. "
                          "Triangles leave none. Every curve from a platform has two authors: the "
                          "people, and the code.") as beat:
            self.play(FadeIn(VGroup(ax, ticks, xt)), Create(curve), run_time=1.2)
            self.play(FadeIn(ring), FadeIn(ring_lbl.set_color(YELLOW)), Create(wall),
                      run_time=beat.until("visible", offset=-0.3))
            self.play(flag(ring), run_time=0.8)
            beat.wait_until("people", offset=-0.2)
            self.play(FadeIn(lbl_people, shift=0.1 * UP), run_time=0.7)
            beat.wait_until("code", occurrence=2, offset=-0.2)
            self.play(FadeIn(lbl_code, shift=0.1 * LEFT), FadeIn(lbl_code2, shift=0.1 * LEFT), run_time=0.7)

        self.end_card()
