"""Episode 62 - How the Medici Won Florence Without Being the Richest.

    videos/toolkit/render.sh --preview videos/episodes/062-centrality-medici/scene.py Episode /tmp/e62.mp4
"""
import itertools
import math

import networkx as nx
from manim import *
from sample_space import *

# ----------------------------------------------------------------------------- data
G = nx.florentine_families_graph()          # Padgett marriage network (Breiger & Pattison 1986)
G.add_node("Pucci")                         # the 16th family: no marriage ties in the data
DEG = dict(G.degree())
BTW = nx.betweenness_centrality(G, normalized=False)     # each unordered pair once
WEALTH = {"Strozzi": 146, "Medici": 103}    # net wealth 1427, thousand lira (Padgett, UCINET PADGW)

RAW = {
    "Medici": (-2.5, 0.35), "Acciaiuoli": (-4.3, 1.8), "Salviati": (-4.15, -0.35),
    "Pazzi": (-5.5, -1.3), "Barbadori": (-1.55, 2.2), "Castellani": (0.3, 2.45),
    "Peruzzi": (1.2, 1.15), "Strozzi": (-0.05, 0.75), "Ridolfi": (-1.15, -0.2),
    "Tornabuoni": (-1.9, -1.15), "Bischeri": (0.85, -0.6), "Guadagni": (-0.55, -2.0),
    "Lamberteschi": (0.85, -2.45), "Albizzi": (-3.2, -1.9), "Ginori": (-4.6, -2.45),
    "Pucci": (-5.6, 2.7),
}
POS = {k: np.array([-2.6 + (x + 2.5) * 0.9, y, 0.0]) for k, (x, y) in RAW.items()}
LABEL_DIR = {
    "Medici": UL, "Acciaiuoli": UP, "Salviati": UP, "Pazzi": DOWN, "Barbadori": UP,
    "Castellani": UP, "Peruzzi": RIGHT, "Strozzi": UL, "Ridolfi": DR, "Tornabuoni": DL,
    "Bischeri": RIGHT, "Guadagni": DOWN, "Lamberteschi": DOWN, "Albizzi": UL, "Ginori": LEFT,
    "Pucci": RIGHT,
}
FAM_COLOR = {"Medici": YELLOW, "Strozzi": PURPLE}

R_UNIFORM = 0.17


def r_degree(f):
    return 0.12 + 0.055 * DEG[f]


def r_btw(f):
    return 0.15 + 0.08 * math.sqrt(BTW[f])


# panel (right side)
NAME_X = 3.6          # right edge of row names
BAR_X = 3.78          # left edge of bars
BAR_MAX = 1.75
ROW_Y = {"Medici": 1.75, "Strozzi": 1.15, "Guadagni": 0.55}
PANEL_CX = 4.35


class Episode(NarratedScene):
    EPISODE = 62
    TITLE = "How the Medici Won Florence Without Being the Richest"
    PRONUNCIATIONS = {
        "Strozzi": "/stɹˈɑtsi/",
        "Guadagni": "/ɡwɑdˈɑnji/",
        "Acciaiuoli": "/ˌɑʧəjwˈOli/",
        "Tornabuoni": "/tˌɔɹnəbwˈOni/",
        "Albizzi": "/ɑlbˈitsi/",
        "Salviati": "/sˌɑlviˈɑti/",
        "Pazzi": "/pˈɑtsi/",
        "Cosimo": "/kˈOzimO/",
        "Palla": "/pˈɑlə/",
        "Ansell": "/ˈænsəl/",
    }

    # ------------------------------------------------------------------ builders
    def build_network(self):
        self.nodes, self.labels, self.edges = {}, {}, {}
        for f, p in POS.items():
            col = FAM_COLOR.get(f, GRAY)
            c = Circle(radius=R_UNIFORM, stroke_color=col, stroke_width=3,
                       fill_color=col, fill_opacity=0.85 if f in FAM_COLOR else 0.55)
            c.move_to(p).set_z_index(3)
            self.nodes[f] = c
            size = LABEL if f in FAM_COLOR else SMALL
            lbl = text(f, size=size, color=col if f in FAM_COLOR else GRAY).set_z_index(4)
            d = LABEL_DIR[f]

            def upd(m, c=c, d=d):
                m.next_to(c, d, buff=0.1 if d[0] == 0 or d[1] == 0 else 0.0)
            lbl.add_updater(upd)
            upd(lbl)
            self.labels[f] = lbl
        for a, b in G.edges():
            e = Line(POS[a], POS[b], stroke_color=BLUE, stroke_width=3, stroke_opacity=0.75)
            na, nb = self.nodes[a], self.nodes[b]
            e.add_updater(lambda m, na=na, nb=nb: m.put_start_and_end_on(na.get_center(),
                                                                           nb.get_center()))
            e.set_z_index(1)
            self.edges[frozenset((a, b))] = e
        return VGroup(*self.edges.values()), VGroup(*self.nodes.values()), VGroup(*self.labels.values())

    def edge(self, a, b):
        return self.edges[frozenset((a, b))]

    def incident(self, f):
        return [e for k, e in self.edges.items() if f in k]

    def resize(self, rfun):
        return [self.nodes[f].animate.scale_to_fit_width(2 * rfun(f)) for f in self.nodes]

    def path_mob(self, fams, color=GREEN, width=9):
        p = VMobject(stroke_color=color, stroke_width=width).set_z_index(2)
        p.set_points_as_corners([self.nodes[f].get_center() for f in fams])
        return p

    def make_row(self, f, color):
        name = text(f, size=LABEL, color=color)
        name.move_to([NAME_X - name.width / 2, ROW_Y[f], 0])
        val = ValueTracker(0.0)
        bar = Rectangle(width=0.01, height=0.34, stroke_width=0, fill_color=color,
                        fill_opacity=0.9)
        y = ROW_Y[f]

        def upd(b):
            w = max(0.01, val.get_value() * self.unit.get_value())
            b.stretch_to_fit_width(w)
            b.move_to([BAR_X + w / 2, y, 0])
        bar.add_updater(upd)
        upd(bar)
        return name, bar, val

    def number_for(self, f, value, decimals=0, color=INK, tracker=None):
        """Number to the right of a row's bar; follows the bar (and the tracker if given)."""
        n = DecimalNumber(value, num_decimal_places=decimals, font_size=MATH_SMALL + 4,
                          color=color).set_z_index(4)
        bar = self.bars[f]

        def upd(m):
            if tracker is not None:
                m.set_value(tracker.get_value())
            m.next_to(bar, RIGHT, buff=0.15)
        n.add_updater(upd)
        upd(n)
        return n

    def heading(self, main, unit):
        h = text(main, size=HEADING - 4, color=INK)
        u = text(unit, size=SMALL, color=GRAY)
        g = VGroup(h, u).arrange(DOWN, buff=0.12)
        return g.move_to([PANEL_CX, 2.85, 0])

    # ------------------------------------------------------------------ scene
    def construct(self):
        edges, nodes, labels = self.build_network()
        self.unit = ValueTracker(BAR_MAX / 146)
        rows = {}
        self.bars = {}
        for f in ("Medici", "Strozzi", "Guadagni"):
            col = FAM_COLOR.get(f, GRAY)
            name, bar, val = self.make_row(f, col)
            rows[f] = (name, bar, val)
            self.bars[f] = bar
        self.add(edges, nodes, labels)           # concrete network from the first frame

        # ============================================================ 1 cold open
        head = self.heading("net wealth, 1427", "(thousand lira)")
        data_cite = citation("Padgett's data via Breiger & Pattison, 1986 · Social Networks")
        with self.narrate("Florence, fourteen twenty-seven. The Strozzi are richer, but the "
                          "Medici will rule.") as beat:
            self.play(FadeIn(head, shift=0.15 * DOWN), FadeIn(data_cite), run_time=1.0)
            beat.wait_until("Strozzi", offset=-0.2)
            sname, sbar, sval = rows["Strozzi"]
            mname, mbar, mval = rows["Medici"]
            self.add(sbar, mbar)
            snum = self.number_for("Strozzi", 146)
            self.play(FadeIn(sname), sval.animate.set_value(146), FadeIn(snum),
                      flag(self.nodes["Strozzi"], color=PURPLE), run_time=1.1)
            beat.wait_until("Medici", offset=-0.2)
            mnum = self.number_for("Medici", 103)
            self.play(FadeIn(mname), mval.animate.set_value(103), FadeIn(mnum),
                      flag(self.nodes["Medici"], color=YELLOW), run_time=1.1)

        # count marriages -> badges
        def badge(f, n, d):
            b = formula(str(n), size=MATH + 4, color=FAM_COLOR[f]).set_z_index(5)
            b.next_to(self.nodes[f], d, buff=0.12)
            return b
        mb = badge("Medici", 6, DR).shift(0.05 * LEFT + 0.05 * UP)
        sb = badge("Strozzi", 4, DOWN).shift(0.35 * LEFT + 0.05 * UP)
        with self.narrate("Count their marriages: the Medici have six, the Strozzi four. How "
                          "much stronger is the Medici position? Make a guess. [pause 1.5]") as beat:
            beat.wait_until("Medici", offset=-0.3)
            self.play(LaggedStart(*[e.animate.set_stroke(YELLOW, width=6, opacity=1)
                                    for e in self.incident("Medici")], lag_ratio=0.15),
                      run_time=beat.until("six", offset=-0.05))
            self.play(FadeIn(mb, scale=0.6), run_time=0.5)
            self.play(LaggedStart(*[e.animate.set_stroke(PURPLE, width=6, opacity=1)
                                    for e in self.incident("Strozzi")], lag_ratio=0.15),
                      run_time=beat.until("four", offset=-0.05))
            self.play(FadeIn(sb, scale=0.6), run_time=0.5)
            q = formula(r"6", r"\,:\,", r"4", r"\;\to\;", r"?", size=EQ)
            q[0].set_color(YELLOW)
            q[2].set_color(PURPLE)
            q.move_to([PANEL_CX, -0.6, 0])
            beat.wait_until("stronger", offset=-0.2)
            self.play(TransformFromCopy(mb, q[0]), TransformFromCopy(sb, q[2]),
                      FadeIn(q[1]), run_time=1.0)
            self.play(Write(q[3:]), run_time=0.8)

        # ============================================================ 2 naive: degree
        dhead = self.heading("degree", "(number of marriage ties)")
        with self.narrate("Pick the wrong measure of importance, and you misread who holds "
                          "power. The obvious measure is degree: count each family's ties.") as beat:
            self.play(FadeOut(q), FadeOut(data_cite),
                      *[e.animate.set_stroke(BLUE, width=3, opacity=0.75) for e in edges],
                      run_time=1.0)
            beat.wait_until("degree", offset=-0.2)
            self.play(ReplacementTransform(head, dhead), FadeOut(snum), FadeOut(mnum),
                      rows["Medici"][2].animate.set_value(0), rows["Strozzi"][2].animate.set_value(0),
                      run_time=0.9)
            self.unit.set_value(BAR_MAX / 6)
            self.play(*self.resize(r_degree), run_time=beat.until("count", offset=-0.1) + 0.6)

        with self.narrate("By degree, the Medici lead, with the Strozzi and the Guadagni tied "
                          "behind them at four. Six to four is one and a half to one.") as beat:
            mname, mbar, mval = rows["Medici"]
            sname, sbar, sval = rows["Strozzi"]
            gname, gbar, gval = rows["Guadagni"]
            mnum = self.number_for("Medici", 6, color=YELLOW)
            snum = self.number_for("Strozzi", 4, color=PURPLE)
            gnum = self.number_for("Guadagni", 4, color=GRAY)
            mnum.suspend_updating(); snum.suspend_updating()
            self.play(mval.animate.set_value(6), ReplacementTransform(mb, mnum),
                      run_time=1.0)
            mnum.resume_updating()
            beat.wait_until("Strozzi", offset=-0.2)
            self.play(sval.animate.set_value(4), ReplacementTransform(sb, snum), run_time=0.9)
            snum.resume_updating()
            beat.wait_until("Guadagni", offset=-0.2)
            self.add(gbar)
            self.play(FadeIn(gname), gval.animate.set_value(4), FadeIn(gnum),
                      flag(self.nodes["Guadagni"], color=INK), run_time=0.9)
            ratio = ValueTracker(1.5)
            rlabel = VGroup(text("Medici", size=LABEL, color=YELLOW),
                            formula(r"\div", size=MATH), text("Strozzi", size=LABEL, color=PURPLE),
                            formula("=", size=MATH)).arrange(RIGHT, buff=0.15)
            rnum = DecimalNumber(1.5, num_decimal_places=1, font_size=MATH + 4)
            rx = formula(r"\times", size=MATH)
            rrow = VGroup(rlabel, rnum, rx).arrange(RIGHT, buff=0.15).move_to([PANEL_CX, -0.05, 0])
            rnum.add_updater(lambda m: m.set_value(ratio.get_value()))
            beat.wait_until("Six", offset=-0.2)
            self.play(TransformFromCopy(VGroup(mnum, snum), rnum), FadeIn(rlabel), FadeIn(rx),
                      run_time=1.2)

        # ============================================================ 3 fail: removal
        dmg_title = text("pairs cut off", size=LABEL, color=RED)
        dmg_rows = {}
        for f in ("Strozzi", "Medici"):
            nm = text("without " + f, size=SMALL + 2, color=FAM_COLOR[f])
            dmg_rows[f] = nm
        dmg_title.move_to([PANEL_CX, -0.95, 0])
        dmg_rows["Strozzi"].move_to([PANEL_CX - 0.55, -1.55, 0])
        dmg_rows["Medici"].move_to([PANEL_CX - 0.55, -2.15, 0])
        dmg_rows["Medici"].align_to(dmg_rows["Strozzi"], LEFT)
        s_cut = ValueTracker(0)
        m_cut = ValueTracker(0)
        s_num = DecimalNumber(0, num_decimal_places=0, font_size=MATH + 4, color=RED)
        m_num = DecimalNumber(0, num_decimal_places=0, font_size=MATH + 4, color=RED)
        s_num.add_updater(lambda m: m.set_value(s_cut.get_value()).next_to(dmg_rows["Strozzi"], RIGHT, buff=0.3))
        m_num.add_updater(lambda m: m.set_value(m_cut.get_value()).next_to(dmg_rows["Medici"], RIGHT, buff=0.3))
        s_num.update(); m_num.update()
        m_num.align_to(s_num, LEFT)

        def removal_mobs(f):
            return [self.nodes[f], self.labels[f], *self.incident(f)]

        with self.narrate("Now test that ranking. Remove the Strozzi, and every family in the "
                          "web can still reach every other through some chain of marriages.") as beat:
            self.play(FadeIn(dmg_title, shift=0.1 * UP), run_time=0.8)
            beat.wait_until("Remove", offset=-0.1)
            self.play(*[m.animate.set_opacity(0.12) for m in removal_mobs("Strozzi")],
                      FadeIn(dmg_rows["Strozzi"]), run_time=1.0)
            self.play(FadeIn(s_num), run_time=0.5)
            # connectivity wave: breadth-first from the Medici through the remaining web
            H = G.copy(); H.remove_node("Strozzi")
            order = [frozenset(e) for e in nx.bfs_edges(H, "Medici")]
            beat.wait_until("reach", offset=-0.3)
            waves = [ShowPassingFlash(self.edges[k].copy().clear_updaters()
                                      .set_stroke(GREEN, width=8, opacity=1), time_width=0.6)
                     for k in order]
            self.play(LaggedStart(*waves, lag_ratio=0.18), run_time=beat.remaining(1.5))
            self.play(flag(s_num, color=RED), run_time=0.6)

        pieces_a = VGroup(self.nodes["Acciaiuoli"])
        pieces_b = VGroup(self.nodes["Salviati"], self.nodes["Pazzi"])
        with self.narrate("Put them back, and remove the Medici instead. The web breaks into "
                          "three pieces, and thirty-five pairs of families lose every "
                          "connection.") as beat:
            self.play(*[m.animate.set_opacity(1) for m in removal_mobs("Strozzi")],
                      *[e.animate.set_stroke(opacity=0.75) for e in self.incident("Strozzi")],
                      run_time=beat.until("remove", offset=-0.1))
            self.nodes["Strozzi"].set_fill(opacity=0.85)
            self.play(*[m.animate.set_opacity(0.12) for m in removal_mobs("Medici")],
                      FadeIn(dmg_rows["Medici"]), FadeIn(m_num),
                      run_time=beat.until("breaks", offset=-0.1))
            self.play(pieces_a.animate.shift(0.45 * UL), pieces_b.animate.shift(0.5 * LEFT + 0.2 * DOWN),
                      run_time=beat.until("thirty", offset=-0.15))
            self.play(m_cut.animate.set_value(35), run_time=beat.until("connection", offset=0.2),
                      rate_func=SMOOTH)

        with self.narrate("Degree called it six to four. The damage is thirty-five to zero. "
                          "Counting ties misses which ties nobody else can replace.") as beat:
            beat.wait_until("six", offset=-0.2)
            self.play(flag(rrow), run_time=0.8)
            beat.wait_until("thirty", offset=-0.2)
            self.play(flag(m_num, color=RED), flag(s_num, color=RED), run_time=0.9)
            beat.wait_until("nobody", offset=-0.5)
            bridges = [self.edge("Medici", "Acciaiuoli"), self.edge("Medici", "Salviati")]
            self.play(pieces_a.animate.shift(-0.45 * UL), pieces_b.animate.shift(-0.5 * LEFT - 0.2 * DOWN),
                      *[m.animate.set_opacity(1) for m in removal_mobs("Medici")],
                      run_time=1.2)
            self.nodes["Medici"].set_fill(opacity=0.85)
            self.play(*[b.animate.set_stroke(YELLOW, width=7, opacity=1) for b in bridges],
                      run_time=beat.remaining(0.8))

        # ============================================================ 4 insight: routes
        bhead = self.heading("betweenness", "(points for shortest routes)")
        mval, gval, sval = rows["Medici"][2], rows["Guadagni"][2], rows["Strozzi"][2]
        with self.narrate("So score routes instead. The Pazzi and the Acciaiuoli are joined by "
                          "one shortest chain, through the Salviati and the Medici. The Medici "
                          "sit on it, so they score one point.") as beat:
            self.play(FadeOut(VGroup(dmg_title, dmg_rows["Strozzi"], dmg_rows["Medici"], s_num, m_num, rrow)),
                      *[b.animate.set_stroke(BLUE, width=3, opacity=0.75) for b in bridges],
                      ReplacementTransform(dhead, bhead),
                      FadeOut(mnum), FadeOut(snum), FadeOut(gnum),
                      mval.animate.set_value(0), sval.animate.set_value(0), gval.animate.set_value(0),
                      run_time=1.2)
            self.unit.set_value(0.5)
            mnum = self.number_for("Medici", 0, 1, YELLOW, tracker=mval)
            snum = self.number_for("Strozzi", 0, 1, PURPLE, tracker=sval)
            gnum = self.number_for("Guadagni", 0, 1, GRAY, tracker=gval)
            self.play(FadeIn(mnum), FadeIn(snum), FadeIn(gnum), run_time=0.6)
            beat.wait_until("Pazzi", offset=-0.2)
            ends1 = [self.nodes["Pazzi"], self.nodes["Acciaiuoli"]]
            self.play(*[flag(n, color=GREEN) for n in ends1], run_time=0.8)
            p1 = self.path_mob(["Pazzi", "Salviati", "Medici", "Acciaiuoli"])
            beat.wait_until("chain", offset=-0.2)
            self.play(Create(p1), run_time=beat.until("sit", offset=-0.1), rate_func=SMOOTH)
            plus = formula("+1", size=MATH, color=GREEN).set_z_index(6)
            plus.next_to(self.nodes["Medici"], DR, buff=0.05)
            self.play(FadeIn(plus, scale=0.7), run_time=0.5)
            beat.wait_until("score", offset=-0.1)
            self.play(plus.animate.move_to(mnum).set_opacity(0), mval.animate.set_value(1),
                      run_time=1.0)
            self.remove(plus)

        with self.narrate("The Albizzi and the Tornabuoni have two equally short chains, one "
                          "through the Medici and one through the Guadagni. Each family gets "
                          "half a point.") as beat:
            self.play(p1.animate.set_stroke(opacity=0.0), run_time=0.6)
            self.remove(p1)
            beat.wait_until("Albizzi", offset=-0.2)
            self.play(*[flag(self.nodes[f], color=GREEN) for f in ("Albizzi", "Tornabuoni")],
                      run_time=0.8)
            pm = self.path_mob(["Albizzi", "Medici", "Tornabuoni"])
            pg = self.path_mob(["Albizzi", "Guadagni", "Tornabuoni"])
            beat.wait_until("one through", offset=-0.1)
            self.play(Create(pm), run_time=beat.until("Guadagni", offset=-0.3))
            self.play(Create(pg), run_time=0.9)
            hm = formula(r"+\tfrac{1}{2}", size=MATH, color=GREEN).set_z_index(6)
            hg = formula(r"+\tfrac{1}{2}", size=MATH, color=GREEN).set_z_index(6)
            hm.next_to(self.nodes["Medici"], DR, buff=0.05)
            hg.next_to(self.nodes["Guadagni"], UR, buff=0.02)
            beat.wait_until("half", offset=-0.4)
            self.play(FadeIn(hm, scale=0.7), FadeIn(hg, scale=0.7), run_time=0.5)
            self.play(hm.animate.move_to(mnum).set_opacity(0), hg.animate.move_to(gnum).set_opacity(0),
                      mval.animate.set_value(1.5), gval.animate.set_value(0.5),
                      run_time=beat.remaining(0.9))
            self.remove(hm, hg)

        # formula from the two routes
        frac = formula(r"{1", r"\over", r"2}", size=EQ + 4)
        frac[0].set_color(GREEN)
        frac[2].set_color(GREEN)
        frac.move_to([PANEL_CX, -0.75, 0])
        full = MathTex(r"C_B(", r"v", r")", r"=", r"\sum_{\text{pairs } s,t}",
                       r"{\sigma_{st}(", r"v", r")", r"\over", r"\sigma_{st}}", font_size=EQ - 4)
        full[1].set_color(YELLOW)
        full[6].set_color(YELLOW)
        for i in (5, 7, 9):
            full[i].set_color(GREEN)
        full.move_to([PANEL_CX + 0.05, -0.75, 0])
        num_lbl = text("shortest routes through v", size=SMALL, color=GRAY)
        den_lbl = text("all shortest routes", size=SMALL, color=GRAY)
        lbls = VGroup(num_lbl, den_lbl).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        lbls.move_to([PANEL_CX + 0.1, -2.15, 0])
        sig_n = formula(r"\sigma_{st}(v):", size=MATH_SMALL, color=GREEN)
        sig_d = formula(r"\sigma_{st}:", size=MATH_SMALL, color=GREEN)
        with self.narrate("That half is the routes through the Medici, one, over all the "
                          "shortest routes, two. Add those fractions over every pair of "
                          "families, and you get betweenness.") as beat:
            beat.wait_until("one", offset=-0.3)
            self.play(TransformFromCopy(pm, frac[0]), run_time=0.9)
            beat.wait_until("two", offset=-0.5)
            self.play(TransformFromCopy(VGroup(pm, pg), frac[2]), FadeIn(frac[1]), run_time=0.9)
            beat.wait_until("Add", offset=-0.2)
            self.play(FadeOut(pm), FadeOut(pg), run_time=0.5)
            self.play(ReplacementTransform(frac[0], VGroup(*full[5:8])),
                      ReplacementTransform(frac[1], full[8]),
                      ReplacementTransform(frac[2], full[9]),
                      run_time=1.2)
            self.play(Write(VGroup(*full[0:5])), run_time=beat.until("betweenness", offset=-0.2))
            self.play(flag(full[0:3]), run_time=0.8)

        fcite = citation("Freeman, 1977 · Sociometry")
        rng = np.random.default_rng(7)
        others = [f for f in G if f != "Medici"]
        all_paths = []
        for s, t in itertools.combinations(others, 2):
            if nx.has_path(G, s, t):
                ps = list(nx.all_shortest_paths(G, s, t))
                all_paths.append(ps[0])
        order = rng.permutation(len(all_paths))
        with self.narrate("Freeman wrote it down in nineteen seventy-seven. Now run it on all "
                          "one hundred and five pairs that leave the Medici out.") as beat:
            sig_n.next_to(num_lbl, LEFT, buff=0.15)
            sig_d.next_to(den_lbl, LEFT, buff=0.15)
            legend = VGroup(sig_n, num_lbl, sig_d, den_lbl)
            legend.move_to([PANEL_CX, -2.2, 0])
            self.play(FadeIn(fcite), FadeIn(legend), run_time=0.9)
            beat.wait_until("run", offset=-0.2)
            flashes = [ShowPassingFlash(self.path_mob(all_paths[i], width=6), time_width=0.5)
                       for i in order]
            run = beat.remaining(1.0) + 3.2
            self.play(LaggedStart(*flashes, lag_ratio=0.06, run_time=run),
                      mval.animate(run_time=run, rate_func=SMOOTH).set_value(BTW["Medici"]),
                      gval.animate(run_time=run, rate_func=SMOOTH).set_value(BTW["Guadagni"]),
                      sval.animate(run_time=run, rate_func=SMOOTH).set_value(BTW["Strozzi"]),
                      self.unit.animate(run_time=run, rate_func=SMOOTH).set_value(BAR_MAX / 47.5),
                      *[a for a in self.resize(r_btw)],
                      run_time=run)

        with self.narrate("The Medici collect forty-seven and a half points. The Guadagni, about "
                          "twenty-three. The Strozzi, nine and a third. Against the Strozzi, the "
                          "lead is about five to one, not one and a half.") as beat:
            self.play(FadeOut(fcite), FadeOut(legend), run_time=0.6)
            self.play(flag(mnum), run_time=beat.until("Guadagni", offset=-0.2))
            self.play(flag(gnum, color=INK), run_time=beat.until("Strozzi", offset=-0.2))
            self.play(flag(snum, color=PURPLE), run_time=beat.until("Against", offset=-0.3))
            rnum.clear_updaters()
            rrow2 = VGroup(rlabel.copy(), rnum.copy().set_value(1.5), rx.copy())
            rrow2.arrange(RIGHT, buff=0.15).move_to([PANEL_CX, -0.05, 0])
            r2 = rrow2[1]
            self.play(full.animate.shift(1.0 * DOWN), FadeIn(rrow2), run_time=0.8)
            beat.wait_until("five", offset=-0.5)
            ratio2 = ValueTracker(1.5)
            r2.add_updater(lambda m: m.set_value(ratio2.get_value()))
            self.play(ratio2.animate.set_value(BTW["Medici"] / BTW["Strozzi"]),
                      run_time=1.3)
            self.play(flag(r2), run_time=beat.remaining(0.8))

        # ============================================================ 5 payoff
        pcite = citation("Padgett & Ansell, 1993 · American Journal of Sociology")
        partners = list(G["Medici"])
        others_dim = [f for f in G if f not in partners and f != "Medici"]
        dim_mobs = [self.nodes[f] for f in others_dim] + [self.labels[f] for f in others_dim] + \
            [e for k, e in self.edges.items() if "Medici" not in k]
        with self.narrate("Padgett and Ansell found this structure in the marriage and business "
                          "ties of ninety-two elite families. The Medici's allies were tied to "
                          "each other almost only through the Medici.") as beat:
            self.play(FadeOut(full), FadeIn(pcite), run_time=1.0)
            n92 = VGroup(formula("92", size=EQ, color=INK), text("families in the full study", size=LABEL - 2, color=GRAY))
            n92.arrange(RIGHT, buff=0.2).move_to([PANEL_CX, -1.1, 0])
            fit(n92, width=4.0)
            beat.wait_until("ninety", offset=-0.3)
            self.play(FadeIn(n92, shift=0.1 * UP), run_time=0.8)
            beat.wait_until("allies", offset=-0.3)
            self.play(*[m.animate.set_opacity(0.25) for m in dim_mobs],
                      *[self.nodes[f].animate.set_stroke(YELLOW, width=4) for f in partners],
                      run_time=1.2)
            self.play(*[e.animate.set_stroke(YELLOW, width=6, opacity=1) for e in self.incident("Medici")],
                      run_time=beat.remaining(0.8))

        pairs = list(itertools.combinations(partners, 2))
        dashed = VGroup()
        for a, b in pairs:
            if G.has_edge(a, b):
                continue
            d = DashedLine(self.nodes[a].get_center(), self.nodes[b].get_center(), dash_length=0.1,
                           stroke_width=2.5, color=GRAY, stroke_opacity=0.9).set_z_index(0)
            dashed.add(d)
        allow_overlap(dashed)
        married = self.edge("Ridolfi", "Tornabuoni")
        mfrac = formula(r"1", r"\text{ of }", r"15", size=MATH + 4, color=YELLOW)
        sfrac = formula(r"2", r"\text{ of }", r"6", size=MATH + 4, color=PURPLE)
        ptitle = text("partner pairs married", size=LABEL, color=INK)
        ptitle.move_to([PANEL_CX, -1.0, 0])
        mfrac.move_to([PANEL_CX - 0.95, -1.75, 0])
        sfrac.move_to([PANEL_CX + 0.95, -1.75, 0])
        with self.narrate("Even in this slice, the Medici's six partners form fifteen possible "
                          "pairs, and just one of those pairs is married. Among the Strozzi's four "
                          "partners, two of six pairs are.") as beat:
            self.play(FadeOut(n92), FadeIn(ptitle), run_time=0.8)
            beat.wait_until("fifteen", offset=-0.4)
            self.play(LaggedStart(*[Create(d) for d in dashed], lag_ratio=0.1),
                      married.animate.set_stroke(INK, width=6, opacity=1),
                      run_time=beat.until("just", offset=-0.1))
            self.play(Write(mfrac), flag(married, color=INK), run_time=1.0)
            beat.wait_until("Among", offset=-0.2)
            spart = list(G["Strozzi"])
            self.play(FadeOut(dashed),
                      married.animate.set_stroke(BLUE, width=3, opacity=0.75),
                      *[e.animate.set_stroke(BLUE, width=3, opacity=0.25) for e in self.incident("Medici")],
                      *[self.nodes[f].animate.set_stroke(GRAY, width=3) for f in partners],
                      *[m.animate.set_opacity(0.25) for m in [self.nodes[f] for f in partners] + [self.labels[f] for f in partners]],
                      *[m.animate.set_opacity(1) for m in [self.nodes[f] for f in spart] + [self.labels[f] for f in spart]],
                      self.nodes["Strozzi"].animate.set_opacity(1),
                      *[e.animate.set_stroke(PURPLE, width=6, opacity=1) for e in self.incident("Strozzi")],
                      run_time=1.2)
            sdash = VGroup()
            for a, b in itertools.combinations(spart, 2):
                if G.has_edge(a, b):
                    self.edge(a, b).set_stroke(opacity=1)
                    continue
                sdash.add(DashedLine(self.nodes[a].get_center(), self.nodes[b].get_center(),
                                     dash_length=0.1, stroke_width=2.5, color=GRAY).set_z_index(0))
            allow_overlap(sdash)
            sm = [self.edge("Castellani", "Peruzzi"), self.edge("Peruzzi", "Bischeri")]
            self.play(LaggedStart(*[Create(d) for d in sdash], lag_ratio=0.15),
                      *[e.animate.set_stroke(INK, width=6, opacity=1) for e in sm],
                      run_time=1.0)
            self.play(Write(sfrac), run_time=beat.remaining(0.8))

        limit = VGroup(text("this web: marriages only,", size=SMALL + 2, color=GRAY),
                       text("16 of 92 families", size=SMALL + 2, color=GRAY)).arrange(DOWN, buff=0.1)
        limit.move_to([PANEL_CX, -2.6, 0])
        with self.narrate("Centrality is only part of their argument. They also traced business, "
                          "class and neighborhood, and this web holds sixteen of their ninety-two "
                          "families.") as beat:
            self.play(FadeOut(sdash),
                      *[e.animate.set_stroke(BLUE, width=3, opacity=0.75) for e in edges],
                      *[n.animate.set_opacity(1) for n in nodes],
                      *[l.animate.set_opacity(1) for l in labels],
                      *[self.nodes[f].animate.set_stroke(GRAY, width=3) for f in partners],
                      run_time=1.2)
            for f, n in self.nodes.items():
                n.set_fill(opacity=0.85 if f in FAM_COLOR else 0.55)
                if f in FAM_COLOR:
                    n.set_stroke(FAM_COLOR[f])
            beat.wait_until("sixteen", offset=-0.4)
            self.play(FadeIn(limit, shift=0.1 * UP), run_time=0.9)

        # ============================================================ 6 landing
        whead = self.heading("net wealth, 1427", "(thousand lira)")
        exile = text("exiled 1434", size=SMALL + 2, color=PURPLE)
        back = text("returned 1434", size=SMALL + 2, color=YELLOW)
        with self.narrate("In fourteen thirty-four, Cosimo de Medici returned from exile, and "
                          "Palla Strozzi, the richest man in Florence, left it for good.") as beat:
            self.play(FadeOut(VGroup(ptitle, mfrac, sfrac, limit, pcite, rrow2)), run_time=0.8)
            beat.wait_until("returned", offset=-0.3)
            back.next_to(self.nodes["Medici"], DOWN, buff=0.15).shift(0.2 * LEFT)
            self.play(FadeIn(back, shift=0.1 * UP), flag(self.nodes["Medici"]), run_time=1.0)
            beat.wait_until("Palla", offset=-0.2)
            exile.next_to(self.nodes["Strozzi"], DOWN, buff=0.15).shift(0.3 * LEFT)
            self.play(*[m.animate.set_opacity(0.3) for m in removal_mobs("Strozzi")],
                      FadeIn(exile), run_time=1.0)
            beat.wait_until("richest", offset=-0.2)
            self.play(ReplacementTransform(bhead, whead), FadeOut(mnum), FadeOut(snum),
                      FadeOut(gnum), FadeOut(gname), gval.animate.set_value(0),
                      self.unit.animate.set_value(BAR_MAX / 146),
                      mval.animate.set_value(103), sval.animate.set_value(146),
                      run_time=1.2)
            self.remove(gbar)
            wm = self.number_for("Medici", 103, 0, YELLOW)
            ws = self.number_for("Strozzi", 146, 0, PURPLE)
            self.play(FadeIn(wm), FadeIn(ws), run_time=0.6)

        bhead2 = self.heading("betweenness", "(points for shortest routes)")
        with self.narrate("The Strozzi owned more of Florence. The Medici stood between more "
                          "of it.") as beat:
            self.play(flag(ws, color=PURPLE), flag(sbar, color=PURPLE),
                      run_time=beat.until("Medici", offset=-0.3))
            bm = self.number_for("Medici", BTW["Medici"], 1, YELLOW, tracker=mval)
            bs = self.number_for("Strozzi", BTW["Strozzi"], 1, PURPLE, tracker=sval)
            self.play(ReplacementTransform(whead, bhead2), FadeOut(wm), FadeOut(ws),
                      FadeIn(bm), FadeIn(bs),
                      mval.animate.set_value(BTW["Medici"]), sval.animate.set_value(BTW["Strozzi"]),
                      self.unit.animate.set_value(BAR_MAX / 47.5),
                      run_time=beat.until("between", offset=0.3))
            self.play(flag(self.nodes["Medici"]), run_time=beat.remaining(0.8))

        for m in self.mobjects:
            m.clear_updaters()
        self.end_card()
