"""Episode 19 - How to Sample From a Shape You Can't Normalize (Metropolis MCMC).

    videos/toolkit/render.sh --preview videos/episodes/019-mcmc-metropolis/scene.py Episode /tmp/ep19.mp4
"""
from manim import *
from sample_space import *

# ----------------------------------------------------------------------------- data
S, ML, MR = 0.55, -1.7, 1.3                     # two hills: small (height 1) left, big (3) right
Z_TRUE = 4 * S * np.sqrt(2 * np.pi)              # 5.5146
VALLEY = -0.328                                  # lowest point between the hills


def H(x):
    return 3 * np.exp(-(x - MR) ** 2 / (2 * S * S)) + np.exp(-(x - ML) ** 2 / (2 * S * S))


def metropolis(rng, n, sig, x0):
    """Random-walk Metropolis, identical call order to sim_check.py."""
    x, out, acc = x0, np.empty(n), 0
    for i in range(n):
        y = x + sig * rng.normal()
        if rng.random() < H(y) / H(x):
            x, acc = y, acc + 1
        out[i] = x
    return out, acc / n


EDGES = np.linspace(-4, 4, 41)
BW = 0.2


class Episode(NarratedScene):
    EPISODE = 19
    TITLE = "How to Sample From a Shape You Can't Normalize"
    PRONUNCIATIONS = {"Bayes'": "Bayes"}

    # ------------------------------------------------------------------ helpers
    def pt(self, x):
        return self.ax.c2p(x, H(x))

    def arc_to(self, x0, x1, color=YELLOW):
        a, b = self.pt(x0), self.pt(x1)
        ang = -PI / 2.6 if x1 > x0 else PI / 2.6
        return DashedVMobject(ArcBetweenPoints(a, b, angle=ang, color=color, stroke_width=4),
                              num_dashes=16)

    def footprint(self, x):
        i = int(np.clip(np.searchsorted(EDGES, x) - 1, 0, 39))
        k = self.stack.get(i, 0)
        self.stack[i] = k + 1
        p = self.ax.c2p(EDGES[i] + BW / 2, 0) + UP * (0.09 + 0.13 * k)
        return Dot(p, radius=0.055, color=PURPLE)

    def step(self, x0, x1, accept, rt=1.5, foot=True):
        """One Metropolis proposal from x0 to x1, drawn on the curve."""
        arc = self.arc_to(x0, x1)
        ghost = Dot(self.pt(x1), radius=0.12, color=YELLOW, fill_opacity=0.35)
        t1 = 0.45 * rt
        self.play(Create(arc), FadeIn(ghost, scale=0.6), run_time=t1)
        if accept:
            path = ArcBetweenPoints(self.pt(x0), self.pt(x1),
                                    angle=-PI / 2.6 if x1 > x0 else PI / 2.6)
            self.play(arc.animate.set_color(GREEN), MoveAlongPath(self.walker, path),
                      FadeOut(ghost), run_time=0.35 * rt)
            xf = x1
        else:
            self.play(arc.animate.set_color(GRAY).set_opacity(0.5),
                      ghost.animate.set_color(GRAY), run_time=0.35 * rt)
            xf = x0
        anims = [FadeOut(arc)] + ([] if accept else [FadeOut(ghost)])
        if foot:
            fp = self.footprint(xf)
            self.feet.add(fp)
            anims.append(FadeIn(fp, shift=0.2 * DOWN))
        self.play(*anims, run_time=0.2 * rt)
        return xf

    # ------------------------------------------------------------------ scene
    def construct(self):
        self.stack = {}
        self.feet = VGroup()
        rng = np.random.default_rng(8)
        chain, acc_main = metropolis(rng, 50000, 1.5, MR)
        idx = np.clip(np.searchsorted(EDGES, chain) - 1, 0, 39)
        small = np.cumsum(chain < VALLEY)
        rng3 = np.random.default_rng(3)
        tiny, acc_tiny = metropolis(rng3, 2000, 0.05, MR)
        huge, acc_huge = metropolis(rng3, 2000, 25.0, MR)

        # ============================================================ 1. cold open
        ax = axes((-4, 4), (0, 3.5), x_ticks=[-4, -2, 0, 2, 4], y_ticks=[0, 1, 2, 3],
                  x_length=9.6, y_length=4.0, x_label="parameter value",
                  y_label="height (unnormalized)")
        ax.shift(UP * (-2.15 - ax.c2p(0, 0)[1]) + RIGHT * (0.3 - ax.c2p(0, 0)[0]))
        self.ax = ax
        curve = ax.plot(H, x_range=[-4, 4, 0.02], color=BLUE, stroke_width=5).set_z_index(2)
        h1 = formula(r"h = 1", color=BLUE).next_to(self.pt(ML), UP, buff=0.3)
        h3 = formula(r"h = 3", color=BLUE).next_to(self.pt(MR), UP, buff=0.3)
        self.walker = Dot(self.pt(ML), radius=0.13, color=YELLOW).set_z_index(5)

        q_txt = text("footprints on the small hill:", size=BODY)
        q_mark = formula(r"?", size=EQ, color=PURPLE)
        question = VGroup(q_txt, q_mark).arrange(RIGHT, buff=0.3).move_to(UP * 3.05 + RIGHT * 0.9)
        q_mark.align_to(q_txt, DOWN)

        with self.narrate("A walker on two hills, one a third as tall as the other. "
                          "It always steps uphill, and only sometimes steps down. "
                          "What share of its footprints land on the small hill? [pause 1.5]") as beat:
            self.add(ax, curve, self.walker)
            self.play(FadeIn(h1, shift=0.1 * UP), FadeIn(h3, shift=0.1 * UP), run_time=0.8)
            beat.wait_until("always", offset=-0.2)
            x = ML
            x = self.step(x, -0.9, False, rt=1.2)
            x = self.step(x, 0.9, True, rt=1.2)
            x = self.step(x, 1.4, True, rt=1.1)
            x = self.step(x, 2.3, False, rt=1.1)
            beat.wait_until("What", offset=-0.1)
            self.play(Write(q_txt), run_time=beat.until("small hill"))
            self.play(FadeIn(q_mark, scale=1.4), run_time=0.6)
            x = self.step(x, 0.8, True, rt=1.4)
            x = self.step(x, -1.5, True, rt=1.6)

        with self.narrate("Climbing keeps pulling it toward the summit, so nearly zero "
                          "feels right.") as beat:
            x = self.step(x, -0.6, False, rt=1.3)
            x = self.step(x, 1.1, True, rt=1.4)
            self.play(Indicate(h3, color=YELLOW), run_time=0.9)

        # ============================================================ 2. stakes
        lik = text("prior × likelihood", size=LABEL, color=BLUE).next_to(ax.c2p(2.6, 2.2), RIGHT, buff=0)
        area = ax.get_area(curve, x_range=(-4, 4), color=RED, opacity=0.35)
        zlab = formula("Z", size=EQ, color=RED).move_to(ax.c2p(MR, 1.05)).set_z_index(3)
        allow_overlap(zlab)
        bayes = MathTex(r"\text{posterior} = \frac{\text{prior} \times \text{likelihood}}{Z}",
                        font_size=MATH, substrings_to_isolate=[r"\text{prior} \times \text{likelihood}", "Z"])
        bayes.move_to(UP * 2.95 + RIGHT * 2.3)
        num = bayes.get_part_by_tex(r"\text{prior} \times \text{likelihood}").set_color(BLUE)
        zden = bayes.get_part_by_tex("Z").set_color(RED)
        head = VGroup(*[m for m in bayes[0]]) if len(bayes) == 1 else bayes[0]
        rest = VGroup(*[m for m in bayes if m is not num and m is not zden and m is not bayes[0]])
        with self.narrate("These hills could be a Bayesian posterior. Bayes' rule hands you "
                          "its shape: prior times likelihood. To turn that shape into "
                          "probabilities, you divide by the total area under it, called Z. "
                          "And Z is an integral over every parameter in the model.") as beat:
            self.play(FadeOut(question), FadeOut(self.feet), FadeOut(self.walker),
                      run_time=0.8)
            self.play(Write(bayes[0]), run_time=beat.until("prior", offset=-0.1))
            self.play(FadeIn(lik, shift=0.1 * LEFT), run_time=0.7)
            self.play(TransformFromCopy(lik, num), run_time=1.2)
            beat.wait_until("divide", offset=-0.1)
            self.play(Write(rest), run_time=0.6)
            self.play(FadeIn(area), run_time=beat.until("called", offset=0.1))
            self.play(Write(zlab), run_time=0.6)
            self.play(TransformFromCopy(zlab, zden), run_time=1.0)
            beat.wait_until("integral", offset=-0.2)
            zint = MathTex(r"Z = \int \!\cdots\! \int \text{prior} \times \text{likelihood}\; "
                           r"d\theta_1 \cdots d\theta_k", font_size=MATH,
                           substrings_to_isolate=[r"\text{prior} \times \text{likelihood}", "Z"])
            zint.get_part_by_tex("Z").set_color(RED)
            zint.get_part_by_tex(r"\text{prior} \times \text{likelihood}").set_color(BLUE)
            zint.move_to(bayes).align_to(bayes, RIGHT)
            self.play(TransformMatchingTex(bayes, zint), run_time=1.5)
            self.play(Indicate(zint[-1], color=YELLOW), run_time=0.9)

        # ============================================================ 3. naive grid
        slices = ax.get_riemann_rectangles(curve, x_range=[-4, 4], dx=0.08,
                                           input_sample_type="center", stroke_width=0,
                                           fill_opacity=0.6, color=RED)
        ev_t = ValueTracker(0)
        evals = live_number(ev_t, 0, size=MATH, suffix=r"\text{ evaluations}")
        evals.move_to(UP * 3.0 + RIGHT * 0.6)
        zres = formula(r"Z \approx 5.51", color=RED).next_to(evals, RIGHT, buff=0.9)
        with self.narrate("The obvious move is to measure Z directly. Evaluate the height at "
                          "a hundred grid points and add up the slices. One parameter, a "
                          "hundred evaluations, and Z comes out to five point five one.") as beat:
            self.play(FadeOut(zint), FadeOut(lik), run_time=beat.until("Evaluate"))
            self.play(FadeIn(evals), run_time=0.5)
            self.play(LaggedStart(*[GrowFromEdge(r, DOWN) for r in slices], lag_ratio=0.03),
                      ev_t.animate.set_value(100), FadeOut(area),
                      run_time=beat.until("One"), rate_func=linear)
            self.play(Indicate(evals, color=YELLOW), run_time=0.9)
            beat.wait_until("comes", offset=-0.2)
            self.play(ReplacementTransform(zlab, zres[0][0]), FadeIn(zres[0][1:]), run_time=1.0)

        # ============================================================ 4. fail
        X0, X1, Y0, Y1 = -6.0, -2.0, -2.1, 1.9
        xs = np.linspace(X0, X1, 100)
        ys = np.linspace(Y0, Y1, 100)
        row = VGroup(*[Line([x, Y0 - 0.12, 0], [x, Y0 + 0.12, 0], color=RED, stroke_width=1.6)
                       for x in xs])
        vlines = VGroup(*[Line([x, Y0, 0], [x, Y1, 0], color=RED, stroke_width=1.0,
                               stroke_opacity=0.75) for x in xs])
        hlines = VGroup(*[Line([X0, y, 0], [X1, y, 0], color=RED, stroke_width=1.0,
                               stroke_opacity=0.75) for y in ys])
        mesh_lbl = formula(r"100 \times 100", size=MATH, color=RED).next_to(vlines, UP, buff=0.25)
        k_lbl = [formula(r"k = %d \text{ parameter%s}" % (k, "" if k == 1 else "s"))
                 for k in (1, 2, 10)]
        cost = [formula(r"100^{1}", "=", r"100", size=EQ),
                formula(r"100^{2}", "=", r"10{,}000", size=EQ),
                formula(r"100^{10}", "=", r"10^{20}", size=EQ)]
        for m in k_lbl:
            m.move_to(RIGHT * 2.6 + UP * 1.9)
        for m in cost:
            m.move_to(RIGHT * 2.6 + UP * 0.75)
            m[2].set_color(RED)
        rate = formula(r"\text{at } 10^{9} \text{ per second:}", size=MATH).move_to(RIGHT * 2.6 + DOWN * 0.55)
        years = formula(r"\approx 3{,}200 \text{ years}", size=EQ, color=RED).next_to(rate, DOWN, buff=0.35)
        graph_grp = VGroup(ax, curve, h1, h3)
        with self.narrate("Add a second parameter, and the grid becomes a hundred by a "
                          "hundred: ten thousand evaluations. Every parameter multiplies the "
                          "cost by a hundred. Ten parameters need ten to the twentieth "
                          "evaluations. At a billion per second, that takes over three "
                          "thousand years. The grid fails because the total needs the height "
                          "everywhere.") as beat:
            self.play(ReplacementTransform(slices, row), FadeOut(graph_grp),
                      FadeOut(zres), ReplacementTransform(evals, cost[0]),
                      FadeIn(k_lbl[0]), run_time=1.4)
            beat.wait_until("hundred by", offset=-0.3)
            self.play(ReplacementTransform(row, vlines), Create(hlines, lag_ratio=0.02),
                      TransformMatchingTex(cost[0], cost[1]),
                      TransformMatchingTex(k_lbl[0], k_lbl[1]), run_time=1.8)
            self.play(FadeIn(mesh_lbl, shift=0.1 * UP), run_time=0.6)
            beat.wait_until("multiplies", offset=-0.1)
            self.play(Indicate(cost[1][0], color=YELLOW, scale_factor=1.15), run_time=1.0)
            beat.wait_until("Ten parameters", offset=-0.2)
            self.play(TransformMatchingTex(cost[1], cost[2]),
                      TransformMatchingTex(k_lbl[1], k_lbl[2]),
                      VGroup(vlines, hlines).animate.set_stroke(opacity=0.35), run_time=1.3)
            beat.wait_until("billion", offset=-0.2)
            self.play(Write(rate), run_time=1.0)
            self.play(Write(years), run_time=beat.until("years", end=True, offset=0.1))
            beat.wait_until("fails", offset=-0.2)
            self.play(LaggedStart(*[l.animate(rate_func=there_and_back).set_stroke(YELLOW, opacity=1)
                                    for l in hlines], lag_ratio=0.02),
                      run_time=beat.remaining(min_time=1.5))

        # ============================================================ 5. Z cancels
        XP = MR + 0.6476                                # H(XP) = 1.5, half the summit height
        self.walker.move_to(self.pt(MR))
        seg_old = Line(ax.c2p(MR, 0), self.pt(MR), color=BLUE, stroke_width=6).set_z_index(3)
        seg_new = Line(ax.c2p(XP, 0), self.pt(XP), color=BLUE, stroke_width=6).set_z_index(3)
        l_old = formula(r"3", color=BLUE).next_to(seg_old, LEFT, buff=0.2).shift(DOWN * 0.3)
        l_new = formula(r"1.5", color=BLUE).next_to(seg_new, RIGHT, buff=0.2).shift(DOWN * 0.3)
        ghost = Dot(self.pt(XP), radius=0.12, color=YELLOW, fill_opacity=0.35)
        parc = self.arc_to(MR, XP)
        pa = MathTex(r"P(\text{accept}) = \frac{1.5}{3}", font_size=EQ,
                     substrings_to_isolate=["1.5", "3"]).move_to(UP * 2.9 + RIGHT * 1.6)
        pa.get_part_by_tex("1.5").set_color(BLUE)
        pa.get_part_by_tex("3").set_color(BLUE)
        pz = MathTex(r"P(\text{accept}) = \frac{1.5 / Z}{3 / Z}", font_size=EQ,
                     substrings_to_isolate=["1.5", "3", "Z", "/"]).move_to(pa)
        pz.get_part_by_tex("1.5").set_color(BLUE)
        pz.get_part_by_tex("3").set_color(BLUE)
        for part in pz:
            if part.get_tex_string() == "Z":
                part.set_color(RED)
        pa2 = pa.copy()
        with self.narrate("The walker never asks for the total. Its downhill rule: propose a "
                          "step, and accept it with probability new height over old height. "
                          "Each true height carries the same unknown Z, so in the ratio, "
                          "Z cancels.") as beat:
            self.play(FadeOut(VGroup(vlines, hlines, mesh_lbl, cost[2], k_lbl[2], rate, years)),
                      run_time=0.6)
            self.play(FadeIn(graph_grp), FadeIn(self.walker), run_time=1.0)
            beat.wait_until("propose", offset=-0.1)
            self.play(Create(parc), FadeIn(ghost, scale=0.6), run_time=0.9)
            beat.wait_until("new height", offset=-0.2)
            self.play(Create(seg_new), FadeIn(l_new), run_time=0.7)
            beat.wait_until("old height", offset=-0.2)
            self.play(Create(seg_old), FadeIn(l_old), run_time=0.7)
            self.play(Write(pa[0]), run_time=0.6)
            self.play(TransformFromCopy(l_new, pa.get_part_by_tex("1.5")),
                      TransformFromCopy(l_old, pa.get_part_by_tex("3")),
                      FadeIn(VGroup(*[m for m in pa[1:] if m.get_tex_string() not in ("1.5", "3")])),
                      run_time=1.1)
            beat.wait_until("Each", offset=-0.1)
            self.play(TransformMatchingTex(pa, pz), run_time=1.3)
            beat.wait_until("cancels", offset=-0.5)
            zs = VGroup(*[p for p in pz if p.get_tex_string() in ("Z", "/")])
            self.play(Indicate(zs, color=RED), run_time=0.7)
            self.play(TransformMatchingTex(pz, pa2), run_time=1.0)

        # ============================================================ 6. two spots, balance
        rule = MathTex(r"P(\text{accept}) = \min\!\Big(1, \frac{h_{\text{new}}}{h_{\text{old}}}\Big)",
                       font_size=MATH).move_to(pa2).align_to(pa2, LEFT)
        SX, TX, BASE = -3.3, 3.3, -2.45
        bar_s = Rectangle(width=1.3, height=0.8, stroke_width=0, fill_color=BLUE, fill_opacity=0.85)
        bar_t = Rectangle(width=1.3, height=2.4, stroke_width=0, fill_color=BLUE, fill_opacity=0.85)
        bar_s.move_to([SX, BASE, 0], aligned_edge=DOWN)
        bar_t.move_to([TX, BASE, 0], aligned_edge=DOWN)
        hs = formula(r"h = 1", color=BLUE).next_to(bar_s, DOWN, buff=0.2)
        ht = formula(r"h = 3", color=BLUE).next_to(bar_t, DOWN, buff=0.2)
        seg_s = Line(ax.c2p(ML, 0), self.pt(ML), color=BLUE, stroke_width=6)
        seg_t = Line(ax.c2p(MR, 0), self.pt(MR), color=BLUE, stroke_width=6)

        def gpos(k, bar):
            return bar.get_top() + np.array([(k % 10 - 4.5) * 0.19, 0.2 + (k // 10) * 0.19, 0])

        dots_all = [Dot(radius=0.065, color=PURPLE) for _ in range(120)]
        pen_s, pen_t = dots_all[:60], dots_all[60:]
        for i, d in enumerate(pen_s):
            d.move_to(gpos(i, bar_s))
        for i, d in enumerate(pen_t):
            d.move_to(gpos(i, bar_t))
        n_s, n_t = DecimalNumber(60, 0, font_size=MATH, color=PURPLE), DecimalNumber(60, 0, font_size=MATH, color=PURPLE)
        n_s.move_to([SX, 0.05, 0])
        n_t.move_to([TX, 2.25, 0])
        arr_ts = Arrow([2.3, 0.55, 0], [-2.3, 0.55, 0], buff=0, color=YELLOW, stroke_width=5)
        arr_st = Arrow([-2.3, -0.75, 0], [2.3, -0.75, 0], buff=0, color=YELLOW, stroke_width=5)

        def flow_lbls(a, frac_val, b, c, approx=False):
            up = MathTex(str(a), r"\times", r"\tfrac{1}{3}", r"\approx" if approx else "=",
                         str(frac_val), font_size=MATH)
            lo = MathTex(str(b), r"\times", "1", "=", str(c), font_size=MATH)
            up[4].set_color(GREEN)
            lo[4].set_color(GREEN)
            up.next_to(arr_ts, UP, buff=0.2)
            lo.next_to(arr_st, DOWN, buff=0.2)
            return up, lo

        def do_round(k_ts, k_st, rt, new_lbls=None):
            nonlocal pen_s, pen_t
            mov_ts, mov_st = pen_t[len(pen_t) - k_ts:], pen_s[len(pen_s) - k_st:]
            new_t = pen_t[:len(pen_t) - k_ts] + mov_st
            new_s = pen_s[:len(pen_s) - k_st] + mov_ts
            self.play(*[d.animate.set_color(GREEN) for d in mov_ts + mov_st], run_time=0.4)
            anims = []
            for i, d in enumerate(new_t):
                anims.append(d.animate(path_arc=(PI / 3 if d in mov_st else 0)).move_to(gpos(i, bar_t)))
            for i, d in enumerate(new_s):
                anims.append(d.animate(path_arc=(PI / 3 if d in mov_ts else 0)).move_to(gpos(i, bar_s)))
            anims += [ChangeDecimalToValue(n_t, len(new_t)), ChangeDecimalToValue(n_s, len(new_s))]
            if new_lbls:
                anims += new_lbls
            self.play(*anims, run_time=rt)
            self.play(*[d.animate.set_color(PURPLE) for d in mov_ts + mov_st], run_time=0.4)
            pen_s, pen_t = new_s, new_t

        with self.narrate("Why would that give the right proportions? Shrink the hills to two "
                          "spots, three units high and one unit high.") as beat:
            self.play(FadeOut(VGroup(seg_old, seg_new, l_old, l_new, ghost, parc)),
                      TransformMatchingTex(pa2, rule), run_time=1.2)
            beat.wait_until("Shrink", offset=-0.1)
            self.play(Create(seg_s), Create(seg_t), run_time=0.8)
            self.play(FadeOut(VGroup(ax, curve, self.walker)),
                      ReplacementTransform(seg_s, bar_s), ReplacementTransform(seg_t, bar_t),
                      ReplacementTransform(h1, hs), ReplacementTransform(h3, ht),
                      run_time=beat.remaining(min_time=1.5))

        up1, lo1 = flow_lbls(60, 20, 60, 60)
        with self.narrate("Put sixty walkers on each, and every round, each one proposes a "
                          "jump to the other spot.") as beat:
            self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in dots_all], lag_ratio=0.01),
                      FadeIn(n_s), FadeIn(n_t), run_time=beat.until("every"))
            self.play(GrowArrow(arr_ts), GrowArrow(arr_st), run_time=beat.remaining(min_time=1.0))

        with self.narrate("Going down from the tall spot, a third accept: twenty walkers. "
                          "Going up from the short spot, all sixty move. So the tall spot "
                          "fills up.") as beat:
            self.play(arr_ts.animate.set_color(GREEN), Write(up1[:3]), run_time=beat.until("twenty", offset=-0.3))
            self.play(Write(up1[3:]), run_time=0.6)
            beat.wait_until("Going up", offset=-0.1)
            self.play(arr_st.animate.set_color(GREEN), Write(lo1), run_time=beat.until("move", end=True))
            do_round(20, 60, beat.remaining(min_time=1.6) - 0.8)

        with self.narrate("At what split does the traffic balance? [pause 1.5]") as beat:
            self.play(Indicate(n_t, color=YELLOW), Indicate(n_s, color=YELLOW), run_time=1.0)

        rounds = [(33, 20, flow_lbls(100, 33, 20, 20, approx=True)),
                  (29, 33, flow_lbls(87, 29, 33, 33, approx=True)),
                  (30, 29, flow_lbls(91, 30, 29, 29, approx=True)),
                  (30, 30, flow_lbls(90, 30, 30, 30))]
        cur_up, cur_lo = up1, lo1
        eq1 = MathTex("90", r"\times", r"\tfrac{1}{3}", "=", "30", r"\times", "1", font_size=EQ)
        eq1.move_to(UP * 2.95 + RIGHT * 0.3)
        with self.narrate("Let the rounds run. Ninety and thirty. A third of ninety is thirty, "
                          "and all thirty come back.") as beat:
            for k_ts, k_st, (u, l) in rounds:
                do_round(k_ts, k_st, 0.9, new_lbls=[ReplacementTransform(cur_up, u),
                                                    ReplacementTransform(cur_lo, l)])
                cur_up, cur_lo = u, l
            self.play(FadeOut(rule), Indicate(n_t, color=YELLOW), Indicate(n_s, color=YELLOW),
                      run_time=beat.until("A third", offset=-0.1, min_time=0.8))
            self.play(TransformFromCopy(cur_up[:3], eq1[:3]), run_time=1.0)
            self.play(Write(eq1[3]), TransformFromCopy(cur_lo[:3], eq1[4:]),
                      run_time=beat.remaining(min_time=1.0))

        eq2 = MathTex(r"\pi_{\text{tall}}", r"\times", r"\frac{h_{\text{short}}}{h_{\text{tall}}}", "=",
                      r"\pi_{\text{short}}", r"\times", "1", font_size=EQ).move_to(eq1)
        eq3 = MathTex(r"\frac{\pi_{\text{tall}}}{\pi_{\text{short}}}", "=",
                      r"\frac{h_{\text{tall}}}{h_{\text{short}}}", "=", "3", font_size=EQ).move_to(eq1)
        for e, pis, hs_ in ((eq2, (0, 4), (2,)), (eq3, (0,), (2,))):
            for i in pis:
                e[i].set_color(PURPLE)
            for i in hs_:
                e[i].set_color(BLUE)
        with self.narrate("The flows match when the walkers split three to one, exactly the "
                          "ratio of the heights.") as beat:
            self.play(*[ReplacementTransform(eq1[i], eq2[i]) for i in range(7)],
                      run_time=beat.until("three", offset=-0.2, min_time=1.2))
            self.play(Indicate(n_t, color=YELLOW), Indicate(n_s, color=YELLOW), run_time=0.8)
            beat.wait_until("ratio", offset=-0.3)
            self.play(ReplacementTransform(eq2, eq3), run_time=1.3)
            self.play(Indicate(VGroup(hs, ht), color=YELLOW), run_time=beat.remaining(min_time=0.8))

        law = MathTex(r"\pi(x)", r"\propto", r"h(x)", font_size=EQ).move_to(eq1)
        law[0].set_color(PURPLE)
        law[2].set_color(BLUE)
        with self.narrate("Every pair of points on the curve strikes this same balance, so "
                          "footprints pile up in proportion to height.") as beat:
            self.play(Indicate(VGroup(arr_ts, arr_st), color=YELLOW), run_time=1.0)
            beat.wait_until("footprints", offset=-0.2)
            self.play(ReplacementTransform(eq3, law), run_time=beat.remaining(min_time=1.2))

        # ============================================================ 7. answer
        two_spot = VGroup(bar_s, bar_t, hs, ht, n_s, n_t, arr_ts, arr_st, cur_up, cur_lo, *dots_all)
        law_small = law.copy().scale(0.8).move_to(UP * 3.05 + LEFT * 4.6)
        bars = VGroup(*[Rectangle(width=BW * ax.x_axis.unit_size * 0.9, height=0.01, stroke_width=0,
                                  fill_color=PURPLE, fill_opacity=0.6) for _ in range(40)])
        for i, b in enumerate(bars):
            b.move_to(ax.c2p(EDGES[i] + BW / 2, 0), aligned_edge=DOWN)
        t_tr = ValueTracker(0.0)
        LOGN = np.log10(50000)

        def n_now():
            return int(np.clip(round(10 ** (t_tr.get_value() * LOGN)), 1, 50000))

        def upd_bars(g):
            n = n_now()
            c = np.bincount(idx[:n], minlength=40)
            hts = np.minimum(c / (n * BW) * Z_TRUE, 3.45)
            for i, b in enumerate(g):
                b.stretch_to_fit_height(max(hts[i] * ax.y_axis.unit_size, 0.01))
                b.move_to(ax.c2p(EDGES[i] + BW / 2, 0), aligned_edge=DOWN)

        steps_num = DecimalNumber(1, 0, font_size=MATH, group_with_commas=True)
        steps_lbl = formula(r"\text{steps} =")
        steps_num.add_updater(lambda m: m.set_value(n_now()))
        steps = VGroup(steps_lbl, steps_num).arrange(RIGHT, buff=0.2).move_to(UP * 3.05 + RIGHT * 1.6)
        steps_num.add_updater(lambda m: m.next_to(steps_lbl, RIGHT, buff=0.2))
        simlab = text("simulated", size=SMALL, color=GRAY).next_to(steps, RIGHT, buff=0.5)
        share_num = DecimalNumber(0, 1, font_size=MATH, color=PURPLE)
        share_num.add_updater(lambda m: m.set_value(100 * small[n_now() - 1] / n_now()))
        share_pct = formula(r"\%", color=PURPLE)
        share = VGroup(share_num, share_pct).arrange(RIGHT, buff=0.08)
        share_pct.add_updater(lambda m: m.next_to(share_num, RIGHT, buff=0.08))
        share.move_to(ax.c2p(ML, 2.15))
        area_lbl = formula(r"\text{area: } 25.0\%", color=BLUE, size=MATH_SMALL + 6)
        area_lbl.next_to(share, DOWN, buff=0.25)
        divider = DashedLine(ax.c2p(VALLEY, 0), ax.c2p(VALLEY, 3.3), color=GRAY, stroke_width=2,
                             dash_length=0.08)
        self.walker.move_to(self.pt(MR))
        with self.narrate("Back on the two hills, fifty thousand simulated steps. The small "
                          "hill collects twenty-five percent of the footprints, its exact share "
                          "of the area. The histogram traces the curve, and nobody ever "
                          "computed Z.") as beat:
            self.play(FadeOut(two_spot), ReplacementTransform(law, law_small), run_time=0.9)
            self.play(FadeIn(VGroup(ax, curve)), FadeIn(self.walker), FadeIn(bars),
                      FadeIn(steps), FadeIn(simlab), run_time=0.9)
            bars.add_updater(upd_bars)
            self.walker.add_updater(lambda m: m.move_to(self.pt(chain[n_now() - 1])))
            self.play(Create(divider), FadeIn(share), run_time=0.6)
            self.play(t_tr.animate.set_value(1.0), run_time=beat.until("twenty", offset=-0.2),
                      rate_func=linear)
            bars.clear_updaters()
            self.walker.clear_updaters()
            share_num.clear_updaters()
            steps_num.clear_updaters()
            self.play(Indicate(share, color=YELLOW), run_time=0.9)
            beat.wait_until("area", offset=-0.2)
            self.play(FadeIn(area_lbl, shift=0.1 * DOWN), run_time=0.7)
            beat.wait_until("histogram", offset=-0.1)
            self.play(LaggedStart(*[Indicate(b, color=PURPLE, scale_factor=1.0) for b in bars],
                                  lag_ratio=0.05),
                      ShowPassingFlash(curve.copy().set_stroke(YELLOW, 7), time_width=0.4),
                      run_time=2.0)
            self.play(Indicate(law_small, color=YELLOW), run_time=beat.remaining(min_time=0.8))

        # ============================================================ 8. payoff
        hist_scene = VGroup(ax, curve, bars, self.walker, divider, share, area_lbl, steps, simlab,
                            law_small)
        BOX = 3.9
        box_sq = Square(BOX, color=GRAY, stroke_width=2.5).move_to(LEFT * 3.7 + UP * 0.35)
        disks = VGroup()
        dx, dy = BOX / 14, BOX / 16
        for r in range(16):
            for c in range(14):
                off = 0.25 if r % 2 else -0.25
                p = box_sq.get_corner(DL) + np.array([(c + 0.5 + off) * dx, (r + 0.5) * dy, 0])
                disks.add(Circle(radius=0.095, stroke_color=INK, stroke_width=1.2,
                                 fill_color=GRAY, fill_opacity=0.45).move_to(p))
        jig = np.random.default_rng(11)
        disk_lbl = formula(r"224 \text{ disks}", size=MATH).next_to(box_sq, UP, buff=0.25)
        coords = formula(r"224 \times 2 = 448 \text{ coordinates}", size=MATH).move_to(RIGHT * 2.9 + UP * 1.9)
        gridpts = formula(r"\text{grid: } 100^{448} \text{ points}", size=EQ).move_to(RIGHT * 2.9 + UP * 0.75)
        gridpts[0][5:11].set_color(RED)
        maniac = text("MANIAC: 4–5 hours per pressure value", size=LABEL).move_to(RIGHT * 2.9 + DOWN * 0.45)
        cite1 = citation("Metropolis, A. Rosenbluth, M. Rosenbluth, A. Teller & E. Teller, 1953 · "
                         "J. Chem. Phys.")
        cite2 = citation("Hastings, 1970 · Biometrika").next_to(cite1, UP, buff=0.15, aligned_edge=LEFT)

        def jiggle(amount):
            return [d.animate.shift(np.array([*jig.uniform(-amount, amount, 2), 0])) for d in disks]

        with self.narrate("This rule is from a nineteen fifty-three paper by Nicholas "
                          "Metropolis, Arianna and Marshall Rosenbluth, and Augusta and Edward "
                          "Teller. At Los Alamos, they simulated two hundred twenty-four hard "
                          "disks: four hundred forty-eight coordinates.") as beat:
            self.play(FadeOut(hist_scene), run_time=0.8)
            self.play(FadeIn(cite1), run_time=0.8)
            beat.wait_until("Los Alamos", offset=-0.3)
            self.play(Create(box_sq), LaggedStart(*[FadeIn(d, scale=0.5) for d in disks],
                                                  lag_ratio=0.004),
                      run_time=beat.until("disks", offset=-0.1))
            self.play(Write(disk_lbl), *jiggle(0.025), run_time=0.9)
            self.play(Write(coords), *jiggle(0.025), run_time=beat.remaining(min_time=1.2))

        with self.narrate("A grid would need a hundred to the four hundred forty-eighth power "
                          "points. Arianna Rosenbluth implemented the walker on the Maniac "
                          "computer, and each pressure value took four to five hours. In "
                          "nineteen seventy, W. K. Hastings generalized it.") as beat:
            self.play(Write(gridpts), run_time=beat.until("points", end=True, min_time=1.0))
            beat.wait_until("Arianna", offset=-0.2)
            for _ in range(3):
                d = disks[int(jig.integers(0, 224))]
                self.play(d.animate.set_fill(YELLOW, 0.9).set_stroke(YELLOW), run_time=0.4)
                self.play(d.animate.shift(np.array([*jig.uniform(-0.04, 0.04, 2), 0]))
                          .set_fill(GRAY, 0.45).set_stroke(INK), run_time=0.6)
            self.play(FadeIn(maniac, shift=0.1 * UP), run_time=beat.until("four to", offset=-0.2, min_time=0.6))
            self.play(*jiggle(0.02), run_time=1.0)
            beat.wait_until("nineteen seventy", offset=-0.2)
            self.play(FadeIn(cite2, shift=0.1 * UP), *jiggle(0.02), run_time=beat.remaining(min_time=1.0))

        # ============================================================ 9. honest limit
        def panel(series, cx):
            a = axes((0, 2000), (-4, 4), x_ticks=[0, 1000, 2000], y_ticks=[-4, 0, 4],
                     x_length=4.8, y_length=2.7, x_label="step", y_label="position")
            a.move_to([cx, -0.55, 0])
            vline = DashedLine(a.c2p(0, VALLEY), a.c2p(2000, VALLEY), color=GRAY, stroke_width=2,
                               dash_length=0.08)
            tr = VMobject(stroke_color=PURPLE, stroke_width=2.2)
            tr.set_points_as_corners([a.c2p(i, v) for i, v in enumerate(series)])
            return a, vline, tr

        ha, hv, htr = panel(huge, -3.3)
        ta, tv, ttr = panel(tiny, 3.3)
        h_tit = formula(r"\text{step size } 25", size=MATH).next_to(ha, UP, buff=0.3)
        t_tit = formula(r"\text{step size } 0.05", size=MATH).next_to(ta, UP, buff=0.3)
        h_acc = formula(r"%d\%%\ \text{accepted}" % round(100 * acc_huge), size=MATH, color=GREEN)
        t_acc = formula(r"%d\%%\ \text{accepted}" % round(100 * acc_tiny), size=MATH, color=GREEN)
        h_acc.next_to(h_tit, UP, buff=0.2)
        t_acc.next_to(t_tit, UP, buff=0.2)
        small_tag = text("small hill", size=SMALL, color=GRAY).next_to(tv, DOWN, buff=0.15).align_to(tv, RIGHT)
        sim2 = text("simulated", size=SMALL, color=GRAY).move_to([0, -3.0, 0])
        ess = formula(r"50{,}000 \text{ steps} \approx 3{,}500 \text{ independent draws}",
                      size=MATH, color=PURPLE).move_to(UP * 3.15)
        with self.narrate("The paper also named the catch. With huge steps, most moves are "
                          "refused. With tiny steps, the walker barely moves: this one never "
                          "leaves the big hill.") as beat:
            self.play(FadeOut(VGroup(box_sq, disks, disk_lbl, coords, gridpts, maniac, cite1, cite2)),
                      run_time=0.8)
            self.play(FadeIn(VGroup(ha, hv, ta, tv)), FadeIn(sim2), run_time=0.8)
            beat.wait_until("huge", offset=-0.2)
            self.play(Write(h_tit), run_time=0.6)
            self.play(Create(htr), FadeIn(h_acc), run_time=beat.until("With tiny", offset=-0.1),
                      rate_func=linear)
            self.play(Write(t_tit), run_time=0.6)
            self.play(Create(ttr), FadeIn(t_acc), run_time=beat.until("never", offset=-0.1),
                      rate_func=linear)
            self.play(FadeIn(small_tag), Indicate(tv, color=YELLOW), run_time=beat.remaining(min_time=1.0))

        with self.narrate("And each footprint sits near the last, so fifty thousand steps are "
                          "worth only a few thousand independent draws.") as beat:
            self.play(Indicate(ttr, color=YELLOW, scale_factor=1.0), run_time=1.2)
            beat.wait_until("fifty", offset=-0.2)
            self.play(Write(ess), run_time=beat.remaining(min_time=1.5))

        # ============================================================ 10. landing
        q_ans = formula(r"25\%", size=EQ, color=PURPLE).move_to(q_mark, aligned_edge=LEFT)
        q_ans.align_to(q_txt, DOWN)
        self.stack = {}
        self.feet = VGroup()
        with self.narrate("So the small hill gets a quarter, not nearly zero. The walker never "
                          "learned how big the hills were. Comparing two heights at a time was "
                          "enough to map them.") as beat:
            self.play(FadeOut(VGroup(ha, hv, htr, h_tit, h_acc, ta, tv, ttr, t_tit, t_acc,
                                     small_tag, sim2, ess)), run_time=0.7)
            self.walker.move_to(self.pt(MR))
            self.play(FadeIn(VGroup(ax, curve, bars, self.walker, divider, share)),
                      FadeIn(question), run_time=0.9)
            self.play(ReplacementTransform(q_mark, q_ans), Indicate(share, color=YELLOW),
                      run_time=1.0)
            beat.wait_until("Comparing", offset=-0.3)
            x = MR
            x = self.step(x, 0.5, True, rt=1.4, foot=False)
            x = self.step(x, -1.4, False, rt=1.4, foot=False)
            self.hold(max(0.0, beat.remaining() - 0.05))

        self.end_card()
