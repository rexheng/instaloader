"""Episode 40 - What a t-SNE Plot Can't Tell You.

Data: tsne_data.npz, made by tsne_sim.py (exact t-SNE in numpy, seed 7; simulated).
    videos/toolkit/render.sh videos/episodes/040-tsne-umap-pitfalls/scene.py Episode \
        videos/episodes/040-tsne-umap-pitfalls/final.mp4
"""
from pathlib import Path

import numpy as np
from manim import *
from sample_space import *

HERE = Path(__file__).resolve().parent
D = np.load(HERE / "tsne_data.npz")
LAB = D["lab"]
YMAP = D["Y"]
TRAJ = D["traj"]                 # (201, 450, 2) snapshots every 5 iterations
SNAP_IT = D["snap_iters"]

# palette (script.md): BLUE points · PURPLE original-data truth · RED read off the map
#                      YELLOW sigma / perplexity (the neighbourhood knob) · GREEN kept neighbours
TRUTH = PURPLE
MAPC = RED
KNOB = YELLOW
KEPT = GREEN

MAP_CENTER = np.array([-3.4, -0.15, 0])
MAP_SCALE = 0.1
_MID = (YMAP.max(0) + YMAP.min(0)) / 2


def map_xy(Y, center=MAP_CENTER, scale=MAP_SCALE):
    P = (Y - _MID) * scale
    return np.c_[P, np.zeros(len(P))] + center


def spread(Z):
    return float(np.sqrt(((Z - Z.mean(0)) ** 2).sum(1).mean()))


def make_dots(P, color=BLUE, r=0.05, opacity=0.9):
    return VGroup(*[Dot(p, radius=r, color=color, fill_opacity=opacity) for p in P])


def pts_of(g):
    return np.array([d.get_center() for d in g])


class Episode(NarratedScene):
    EPISODE = 40
    TITLE = "What a t-SNE Plot Can't Tell You"
    PRONUNCIATIONS = {"Pachter": "pack ter", "Chari": "char ee"}

    # ------------------------------------------------------------------ helpers
    def island(self, k):
        return VGroup(*[d for d, l in zip(self.dots, LAB) if l == k])

    def centroid(self, k):
        return pts_of(self.island(k)).mean(0)

    def construct(self):
        X = D["X"]
        true_spread = [spread(X[LAB == k]) for k in range(3)]
        map_spread = [spread(YMAP[LAB == k]) for k in range(3)]
        cen = [X[LAB == k].mean(0) for k in range(3)]
        mcen = [YMAP[LAB == k].mean(0) for k in range(3)]
        t_ratio = true_spread[1] / true_spread[0]                       # 10.1
        m_ratio = map_spread[1] / map_spread[0]                         # 0.99
        t_gap = np.linalg.norm(cen[2] - cen[0]) / np.linalg.norm(cen[1] - cen[0])    # 4.99
        m_gap = np.linalg.norm(mcen[2] - mcen[0]) / np.linalg.norm(mcen[1] - mcen[0])  # 0.98

        # ============================================================ 1. cold open
        self.dots = make_dots(map_xy(YMAP))
        names = VGroup()
        dirs = {0: RIGHT, 1: DOWN, 2: DOWN}
        for k, n in enumerate("ABC"):
            t = text(n, size=HEADING).next_to(self.island(k), dirs[k], buff=0.25)
            names.add(t)
        tag = text("t-SNE map · simulated", size=SMALL, color=GRAY)
        tag.move_to(MAP_CENTER + UP * 3.35)
        q1 = VGroup(text("one group is", size=BODY), formula(r"10\times", color=TRUTH, size=MATH),
                    text("wider", size=BODY), formula(r"?", color=KNOB, size=EQ)).arrange(RIGHT, buff=0.2)
        q2 = VGroup(text("one group is", size=BODY), formula(r"5\times", color=TRUTH, size=MATH),
                    text("farther", size=BODY), formula(r"?", color=KNOB, size=EQ)).arrange(RIGHT, buff=0.2)
        for q in (q1, q2):
            q[1].align_to(q[0], DOWN)
        qs = VGroup(q1, q2).arrange(DOWN, buff=0.7, aligned_edge=LEFT).move_to([3.2, 0.3, 0])

        with self.narrate("This is a t-SNE map of three groups of points. In the real data, one "
                          "group is ten times more spread out than the others, and one sits five "
                          "times farther away. Which is which? [pause 1.5]") as beat:
            self.play(LaggedStart(*[FadeIn(self.island(k), scale=0.6) for k in range(3)],
                                  lag_ratio=0.35), FadeIn(tag), run_time=beat.until("three"))
            self.play(LaggedStart(*[FadeIn(n, shift=0.1 * UP) for n in names], lag_ratio=0.3),
                      run_time=beat.until("real"))
            beat.wait_until("ten", offset=-0.15)
            self.play(FadeIn(q1, shift=0.15 * LEFT), run_time=0.8)
            beat.wait_until("five", offset=-0.15)
            self.play(FadeIn(q2, shift=0.15 * LEFT), run_time=0.8)
            beat.wait_until("which", offset=-0.1)
            # prediction pause: a yellow ring visits each island in turn
            ring = Circle(radius=0.85, color=KNOB, stroke_width=4).move_to(self.centroid(0))
            self.play(Create(ring), run_time=0.6)
            for k in (1, 2, 0):
                self.play(ring.animate.move_to(self.centroid(k)), run_time=0.9)
            self.play(FadeOut(ring), run_time=beat.remaining(0.4))

        # ============================================================ 2. stakes
        ruler = Line(self.centroid(0), self.centroid(1), color=MAPC, stroke_width=5)
        ruler_q = formula(r"?", color=MAPC, size=EQ).next_to(ruler.get_center(), RIGHT, buff=0.25)
        q3 = VGroup(text("what does this length", size=BODY),
                    text("measure in the data?", size=BODY)).arrange(DOWN, buff=0.18)
        q3.move_to([3.2, 0.3, 0])
        cite1 = citation("Chari & Pachter, 2023 · PLoS Computational Biology")
        with self.narrate("In single-cell biology, maps like this get read for exactly that: how "
                          "varied a cell type is, and which types are close relatives. So the "
                          "real question is what a length on this map measures.") as beat:
            self.play(FadeIn(cite1), run_time=0.8)
            beat.wait_until("varied", offset=-0.2)
            self.play(flag(self.island(1), color=KNOB), run_time=1.0)
            beat.wait_until("relatives", offset=-0.4)
            self.play(flag(VGroup(self.island(0), self.island(2)), color=KNOB), run_time=1.0)
            beat.wait_until("length", offset=-0.3)
            self.play(FadeOut(qs, shift=0.2 * RIGHT), Create(ruler), run_time=0.9)
            self.play(FadeIn(ruler_q), FadeIn(q3, shift=0.1 * UP), run_time=0.8)

        # ============================================================ 3. the truth we built
        head = text("original data · 50 dimensions", size=LABEL, color=GRAY).move_to([3.3, 3.25, 0])
        base_y = 0.55
        H = 2.0
        sp_bars, sp_vals, sp_names = VGroup(), VGroup(), VGroup()
        for i, (k, n) in enumerate(zip(range(3), "ABC")):
            h = max(H * true_spread[k] / max(true_spread), 0.06)
            b = Rectangle(width=0.5, height=h, stroke_width=0, fill_color=TRUTH, fill_opacity=0.9)
            b.move_to([0.95 + 0.85 * i, base_y, 0], aligned_edge=DOWN)
            sp_bars.add(b)
            sp_vals.add(formula(f"{true_spread[k]:.1f}", size=MATH_SMALL, color=TRUTH).next_to(b, UP, buff=0.12))
            sp_names.add(text(n, size=LABEL).next_to(b, DOWN, buff=0.15).set_y(base_y - 0.3))
        sp_title = text("spread", size=LABEL, color=GRAY).next_to(sp_names, DOWN, buff=0.2)
        gaps_true = [np.linalg.norm(cen[1] - cen[0]), np.linalg.norm(cen[2] - cen[0])]
        gp_bars, gp_vals, gp_names = VGroup(), VGroup(), VGroup()
        for i, (g, n) in enumerate(zip(gaps_true, ["A–B", "A–C"])):
            b = Rectangle(width=0.5, height=H * g / max(gaps_true), stroke_width=0,
                          fill_color=TRUTH, fill_opacity=0.9)
            b.move_to([4.45 + 1.15 * i, base_y, 0], aligned_edge=DOWN)
            gp_bars.add(b)
            gp_vals.add(formula(f"{g:.0f}", size=MATH_SMALL, color=TRUTH).next_to(b, UP, buff=0.12))
            gp_names.add(text(n, size=LABEL).next_to(b, DOWN, buff=0.15).set_y(base_y - 0.3))
        gp_title = text("gap", size=LABEL, color=GRAY).next_to(gp_names, DOWN, buff=0.2)
        gp_title.set_y(sp_title.get_y())
        baseline = Line([0.55, base_y, 0], [6.15, base_y, 0], color=GRAY, stroke_width=2)

        with self.narrate("We can check, because this data is simulated. Three blobs, a hundred "
                          "and fifty points each, in fifty dimensions. Blob B is ten times wider "
                          "than A and C. And C sits five times farther from A than B does.") as beat:
            self.play(FadeOut(q3), FadeOut(ruler_q), FadeOut(ruler), FadeOut(cite1), run_time=0.6)
            beat.wait_until("fifty dimensions", offset=-0.3)
            self.play(FadeIn(head, shift=0.1 * DOWN), Create(baseline), FadeIn(sp_names),
                      FadeIn(gp_names), FadeIn(sp_title), FadeIn(gp_title), run_time=1.0)
            beat.wait_until("ten", offset=-0.3)
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in sp_bars], lag_ratio=0.2),
                      run_time=1.2)
            self.play(LaggedStart(*[FadeIn(v, shift=0.1 * UP) for v in sp_vals], lag_ratio=0.2),
                      run_time=0.8)
            beat.wait_until("five", offset=-0.3)
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in gp_bars], lag_ratio=0.3),
                      run_time=1.2)
            self.play(LaggedStart(*[FadeIn(v, shift=0.1 * UP) for v in gp_vals], lag_ratio=0.2),
                      run_time=0.8)

        # ============================================================ 4. run t-SNE
        frames = [map_xy(self._norm(T)) for T in TRAJ]
        it = ValueTracker(0)
        it_lbl = live_number(it, 0, size=MATH_SMALL, color=GRAY, prefix=r"\text{iteration}")
        it_lbl.move_to(MAP_CENTER + DOWN * 2.85)
        start_pos = frames[0]

        def follow(group):
            v = it.get_value()
            i = int(np.clip(np.floor(v), 0, len(frames) - 2))
            a = v - i
            P = (1 - a) * frames[i] + a * frames[i + 1]
            for d, p in zip(group, P):
                d.move_to(p)

        it_num = ValueTracker(0)
        with self.narrate("Now run t-SNE on it from scratch, with a standard perplexity of "
                          "thirty.") as beat:
            perp = formula(r"\text{perplexity}=", r"30", size=MATH_SMALL).move_to(MAP_CENTER + UP * 2.95)
            perp[1].set_color(KNOB)
            self.play(FadeOut(names), FadeOut(tag),
                      *[d.animate.move_to(p) for d, p in zip(self.dots, start_pos)],
                      run_time=1.0)
            self.play(FadeIn(perp), FadeIn(it_lbl), run_time=0.5)
            # iteration label follows the snapshot index
            it_lbl.number.clear_updaters()
            it_lbl.number.add_updater(lambda m: m.set_value(
                float(np.interp(it.get_value(), np.arange(len(SNAP_IT)), SNAP_IT))))
            self.dots.add_updater(follow)
            self.play(it.animate.set_value(len(frames) - 1), run_time=max(beat.remaining(), 5.5),
                      rate_func=LINEAR)
            self.dots.clear_updaters()
            it_lbl.number.clear_updaters()
        names2 = VGroup()
        for k, n in enumerate("ABC"):
            names2.add(text(n, size=HEADING).next_to(self.island(k), dirs[k], buff=0.25))
        self.play(FadeIn(names2), FadeOut(it_lbl), run_time=0.6)
        names = names2

        # ============================================================ 5. measure: fail
        rings = VGroup(*[Circle(radius=MAP_SCALE * map_spread[k], color=MAPC, stroke_width=4)
                         .move_to(self.centroid(k)) for k in range(3)])
        gA = Line(self.centroid(0), self.centroid(1), color=MAPC, stroke_width=4)
        gC = Line(self.centroid(0), self.centroid(2), color=MAPC, stroke_width=4)
        for m in (gA, gC):
            m.set_z_index(-1)
        hdr = VGroup(text("data", size=LABEL, color=TRUTH), text("map", size=LABEL, color=MAPC))
        hdr[0].move_to([3.75, -0.95, 0])
        hdr[1].move_to([5.45, -0.95, 0])
        r1 = formula(r"\text{spread } B \div A", size=MATH_SMALL + 4).move_to([1.6, -1.65, 0])
        r2 = formula(r"\text{gap } AC \div AB", size=MATH_SMALL + 4).move_to([1.6, -2.5, 0])
        v11 = formula(f"{t_ratio:.1f}", size=MATH, color=TRUTH).move_to([3.75, -1.65, 0])
        v12 = formula(f"{m_ratio:.2f}", size=MATH, color=MAPC).move_to([5.45, -1.65, 0])
        v21 = formula(f"{t_gap:.1f}", size=MATH, color=TRUTH).move_to([3.75, -2.5, 0])
        v22 = formula(f"{m_gap:.2f}", size=MATH, color=MAPC).move_to([5.45, -2.5, 0])
        with self.narrate("Then measure the map. B's spread divided by A's: the truth is ten "
                          "point one, and the map says point nine nine. C's gap divided by B's "
                          "gap: the truth is five, and the map says point nine eight. Both ratios "
                          "got flattened to one.") as beat:
            self.play(FadeIn(hdr), run_time=0.6)
            self.play(LaggedStart(*[Create(r) for r in rings], lag_ratio=0.3),
                      run_time=beat.until("spread", offset=-0.2))
            self.play(FadeIn(r1), run_time=0.6)
            beat.wait_until("truth", offset=-0.2)
            self.play(TransformFromCopy(VGroup(sp_bars[1], sp_bars[0]), v11), run_time=1.0)
            beat.wait_until("map says", offset=-0.2)
            self.play(TransformFromCopy(VGroup(rings[1], rings[0]), v12), run_time=1.0)
            beat.wait_until("gap", offset=-0.3)
            self.play(Create(gA), Create(gC), FadeIn(r2), run_time=0.9)
            beat.wait_until("truth", occurrence=2, offset=-0.2)
            self.play(TransformFromCopy(gp_bars, v21), run_time=1.0)
            beat.wait_until("map says", occurrence=2, offset=-0.2)
            self.play(TransformFromCopy(VGroup(gC, gA), v22), run_time=1.0)
            beat.wait_until("flattened", offset=-0.2)
            self.play(flag(v12), flag(v22), run_time=1.0)

        # ============================================================ 6. sigma per point
        rng = np.random.default_rng(3)
        sk_n = 40
        ca, cb = np.array([-3.6, -0.55, 0]), np.array([2.4, -0.55, 0])
        ZA = rng.normal(0, 1, (sk_n, 2)); ZB = rng.normal(0, 1, (sk_n, 2))
        ZA = np.clip(ZA, -2.1, 2.1); ZB = np.clip(ZB, -2.1, 2.1)
        sa, sb = 0.1, 1.0
        PA = np.c_[ZA * sa, np.zeros(sk_n)] + ca
        PB = np.c_[ZB * sb, np.zeros(sk_n)] + cb
        skA, skB = make_dots(PA), make_dots(PB)
        iA = int(np.argmin(np.linalg.norm(ZA, axis=1)))
        iB = int(np.argmin(np.linalg.norm(ZB, axis=1)))
        # neighbour j at ~1.4 sd from i
        jB = int(np.argmin(np.abs(np.linalg.norm(ZB - ZB[iB], axis=1) - 1.6)))
        ringA = Circle(radius=1.0 * sa, color=KNOB, stroke_width=4).move_to(PA[iA]).set_z_index(3)
        ringB = Circle(radius=1.0 * sb, color=KNOB, stroke_width=4).move_to(PB[iB]).set_z_index(3)
        for g, i in ((skA, iA), (skB, iB)):
            g[i].set_color(KNOB).set_z_index(4)
        sigA = formula(r"\sigma \approx 1.9", size=MATH, color=KNOB).next_to(skA, DOWN, buff=0.5)
        sigB = formula(r"\sigma \approx 19", size=MATH, color=KNOB).move_to([5.3, -0.55, 0])
        rad = Line(PB[iB], PB[iB] + RIGHT * sb, color=KNOB, stroke_width=3).set_z_index(3)
        lblA = text("A", size=HEADING).next_to(skA, UP, buff=0.45)
        lblB = text("B", size=HEADING).move_to([cb[0] - 2.75, 1.4, 0])
        sk_note = text("sketch · numbers from the 50-D data", size=SMALL, color=GRAY)
        sk_note.move_to([3.2, -3.0, 0])
        with self.narrate("t-SNE threw sizes away in its very first step. Around each point, it "
                          "picks a Gaussian width, sigma, tuned so the point has about thirty "
                          "effective neighbours. That number is the perplexity. In tight blob A, "
                          "sigma comes out near one point nine. In wide blob B, near "
                          "nineteen.") as beat:
            keep = [self.island(0), self.island(1)]
            others = [m for m in self.mobjects if m not in (self.dots, perp)]
            self.play(*[FadeOut(m) for m in others], FadeOut(self.island(2)), run_time=0.8)
            self.play(ReplacementTransform(self.island(0), skA),
                      ReplacementTransform(self.island(1), skB),
                      perp.animate.move_to([0, 3.0, 0]),
                      FadeIn(lblA), FadeIn(lblB), FadeIn(sk_note), run_time=1.8)
            beat.wait_until("Gaussian", offset=-0.2)
            self.play(Create(ringB), Create(rad), run_time=1.0)
            self.play(Create(ringA), run_time=0.6)
            beat.wait_until("thirty", offset=-0.2)
            self.play(flag(perp[1]), run_time=0.9)
            beat.wait_until("perplexity", offset=-0.2)
            self.play(Circumscribe(perp, color=KNOB, buff=0.12), run_time=1.0)
            beat.wait_until("one point nine", offset=-0.25)
            self.play(FadeIn(sigA, shift=0.1 * UP), flag(ringA), run_time=0.8)
            beat.wait_until("nineteen", offset=-0.25)
            self.play(FadeIn(sigB, shift=0.1 * LEFT), run_time=0.8)

        # ============================================================ 7. the kernel
        jdot = skB[jB]
        darr = Line(PB[iB], PB[jB], color=TRUTH, stroke_width=5).set_z_index(3)
        dlab = formula(r"d", size=MATH, color=TRUTH).next_to(darr.get_center(), UP + LEFT, buff=0.12)
        eq = MathTex(r"p_{j|i}", r"\propto", r"e^{-", r"d_{ij}", r"^2", r"/", r"2", r"\sigma_i", r"^2", r"}",
                     font_size=EQ)
        eq.move_to([0, 2.95, 0])
        eq[3].set_color(TRUTH); eq[7].set_color(KNOB)
        eq2 = MathTex(r"p_{j|i}", r"\propto", r"e^{-", r"\frac{1}{2}", r"\left(", r"{d_{ij}", r"\over",
                      r"\sigma_i}", r"\right)", r"^2", r"}", font_size=EQ)
        eq2.move_to([0, 2.85, 0])
        eq2[5].set_color(TRUTH); eq2[7].set_color(KNOB)
        with self.narrate("The similarity of a neighbour j to point i is e to the minus distance "
                          "squared, over two sigma i squared. So distance only ever appears "
                          "divided by that point's own sigma.") as beat:
            self.play(FadeOut(perp), Create(darr), jdot.animate.set_color(TRUTH), run_time=0.8)
            self.play(FadeIn(dlab), run_time=0.5)
            self.play(Write(eq[0:2]), run_time=beat.until("e to", offset=-0.1))
            self.play(Write(eq[2]), run_time=0.5)
            self.play(TransformFromCopy(dlab, eq[3]), run_time=beat.until("squared", offset=-0.05))
            self.play(Write(eq[4:7]), run_time=0.6)
            self.play(TransformFromCopy(sigB, eq[7]), Write(eq[8:]), run_time=beat.until("So", offset=-0.1))
            beat.wait_until("divided", offset=-0.3)
            self.play(TransformMatchingTex(eq, eq2), run_time=1.4)
            self.play(Circumscribe(VGroup(eq2[5], eq2[6], eq2[7]), color=INK, buff=0.1), run_time=1.0)
        eq = eq2

        # ============================================================ 8. sigmas cancel
        fA = MathTex(r"{9.8", r"\over", r"1.9}", r"\approx", r"5.2", font_size=MATH)
        fB = MathTex(r"{99", r"\over", r"19}", r"\approx", r"5.2", font_size=MATH)
        for f in (fA, fB):
            f[0].set_color(TRUTH); f[2].set_color(KNOB)
        fA.next_to(sigA, DOWN, buff=0.35)
        fB.next_to(sigB, DOWN, buff=0.45)
        dA = formula(r"d \approx 9.8", size=MATH, color=TRUTH).next_to(lblA, LEFT, buff=0.6)
        dB = formula(r"d \approx 99", size=MATH, color=TRUTH).next_to(sigB, UP, buff=0.45)
        with self.narrate("A typical distance inside A is about ten, and inside B about a "
                          "hundred. Divide each by its own sigma, and what's left? [pause 1.5] "
                          "About five sigmas, in both. Measured in sigmas, B looks just like A, "
                          "so the map draws them the same size.") as beat:
            beat.wait_until("ten", offset=-0.25)
            self.play(FadeIn(dA, shift=0.1 * UP), run_time=0.7)
            beat.wait_until("hundred", offset=-0.25)
            self.play(TransformFromCopy(dlab, dB), run_time=0.8)
            beat.wait_until("Divide", offset=-0.1)
            self.play(TransformFromCopy(dA, fA[0]), TransformFromCopy(sigA, fA[2]),
                      Create(fA[1]), TransformFromCopy(dB, fB[0]), TransformFromCopy(sigB, fB[2]),
                      Create(fB[1]), run_time=1.4)
            # prediction pause: the kernel's fraction pulses toward each blob in turn
            self.play(Indicate(fA[0:3], color=INK, scale_factor=1.08), run_time=1.0)
            self.play(Indicate(fB[0:3], color=INK, scale_factor=1.08), run_time=1.0)
            beat.wait_until("About", offset=-0.2)
            self.play(Write(fA[3:]), Write(fB[3:]), run_time=0.8)
            beat.wait_until("Measured", offset=-0.1)
            # zoom A by sigma_B / sigma_A = 10: it becomes indistinguishable from B
            zoom = sb / sa
            self.play(FadeOut(sigA), FadeOut(fA), FadeOut(fB), FadeOut(sigB), FadeOut(dA), FadeOut(dB),
                      run_time=0.5)
            self.play(VGroup(skA, ringA).animate.scale(zoom, about_point=ca).shift(RIGHT * 0.9 + UP * 0.25),
                      lblA.animate.shift(DOWN * 0.0), run_time=beat.until("so the map", offset=-0.1))
            mapA = make_dots(map_xy(YMAP[LAB == 0]))
            mapB = make_dots(map_xy(YMAP[LAB == 1]))
            mapC = make_dots(map_xy(YMAP[LAB == 2]))
            self.play(FadeOut(ringA), FadeOut(ringB), FadeOut(rad), FadeOut(darr), FadeOut(dlab),
                      FadeOut(lblA), FadeOut(lblB), FadeOut(sk_note),
                      ReplacementTransform(skA, mapA), ReplacementTransform(skB, mapB),
                      eq.animate.scale(0.8).move_to([3.3, 2.9, 0]),
                      run_time=beat.remaining(1.2))
        self.dots = VGroup()
        ordered = []
        ia = ib = ic = 0
        mA, mB, mC = list(mapA), list(mapB), list(mapC)
        for l in LAB:
            if l == 0:
                ordered.append(mA[ia]); ia += 1
            elif l == 1:
                ordered.append(mB[ib]); ib += 1
            else:
                ordered.append(mC[ic]); ic += 1
        names = VGroup(*[text(n, size=HEADING) for n in "ABC"])

        # ============================================================ 9. gaps -> zero
        gAB = Line(mapA.get_center(), mapB.get_center(), color=MAPC, stroke_width=4).set_z_index(-1)
        gAC = Line(mapA.get_center(), mapC.get_center(), color=MAPC, stroke_width=4).set_z_index(-1)
        gBC = Line(mapB.get_center(), mapC.get_center(), color=MAPC, stroke_width=4).set_z_index(-1)
        l300 = formula(r"300", size=MATH, color=TRUTH).next_to(gAB.get_center(), RIGHT, buff=0.3)
        l1500 = formula(r"1500", size=MATH, color=TRUTH).next_to(gAC.get_center(), LEFT, buff=0.3)
        z1 = MathTex(r"{d", r"\over", r"\sigma}", r"\geq", r"12.4", font_size=MATH)
        z1[0].set_color(TRUTH); z1[2].set_color(KNOB)
        z2 = MathTex(r"e^{-\frac{1}{2}(12.4)^2}", r"\approx", r"e^{-77}", font_size=MATH)
        z3 = MathTex(r"=", r"0.\underbrace{000\cdots000}_{33\text{ zeros}}36", font_size=MATH)
        zs = VGroup(z1, z2, z3).arrange(DOWN, buff=0.45, aligned_edge=LEFT).move_to([3.3, 0.2, 0])
        z3.align_to(z2[1], LEFT)
        z1.set_x(3.3)
        with self.narrate("Gaps go the same way. Between blobs, every distance is at least "
                          "twelve sigmas, so that exponential is at most e to the minus seventy "
                          "seven: thirty three zeros after the decimal point. Three hundred or "
                          "fifteen hundred, both round to zero. With nothing pulling any pair "
                          "together, all three settle the same distance apart.") as beat:
            self.play(FadeIn(mapC, scale=0.6), run_time=0.7)
            beat.wait_until("twelve", offset=-0.3)
            self.play(Create(gAB), Create(gAC), run_time=0.7)
            self.play(TransformFromCopy(VGroup(eq[5], eq[6], eq[7]), z1[0:3]), Write(z1[3:]), run_time=1.0)
            beat.wait_until("e to", offset=-0.2)
            self.play(TransformFromCopy(VGroup(eq[2], z1[4]), z2[0]), run_time=1.0)
            self.play(Write(z2[1:]), run_time=0.6)
            beat.wait_until("thirty three", offset=-0.2)
            self.play(Write(z3), run_time=1.2)
            beat.wait_until("Three hundred", offset=-0.2)
            self.play(FadeIn(l300, shift=0.1 * LEFT), run_time=0.6)
            beat.wait_until("fifteen", offset=-0.2)
            self.play(FadeIn(l1500, shift=0.1 * RIGHT), run_time=0.6)
            beat.wait_until("both", offset=-0.1)
            zero_a = formula(r"\approx 0", size=MATH, color=INK).next_to(l300, DOWN, buff=0.2)
            zero_b = formula(r"\approx 0", size=MATH, color=INK).next_to(l1500, DOWN, buff=0.2)
            self.play(FadeIn(zero_a), FadeIn(zero_b), flag(z3[1]), run_time=0.9)
            beat.wait_until("all three", offset=-0.2)
            self.play(FadeOut(zero_a), FadeOut(zero_b), FadeOut(l300), FadeOut(l1500), Create(gBC),
                      run_time=0.8)
            self.play(flag(VGroup(gAB, gAC, gBC), color=MAPC), run_time=1.0)

        # ============================================================ 10. the knob
        self.fade_out_all(run_time=0.6)
        def panel(Y, cx):
            P = Y - Y.mean(0)
            s = 2.3 / np.abs(P).max()
            return np.c_[P * s, np.zeros(len(P))] + np.array([cx, -0.35, 0])
        n30 = make_dots(panel(D["noise30"], -3.3), r=0.05)
        n2 = make_dots(panel(D["noise2"], 3.3), r=0.05)
        h30 = MathTex(r"\text{perplexity}=", r"30", font_size=MATH).move_to([-3.3, 2.8, 0])
        h2 = MathTex(r"\text{perplexity}=", r"2", font_size=MATH).move_to([3.3, 2.8, 0])
        h30[1].set_color(KNOB); h2[1].set_color(KNOB)
        ntag = text("50-D noise, no clusters · simulated", size=SMALL, color=GRAY).move_to([0, 3.35, 0])
        cite2 = citation("Wattenberg, Viégas & Johnson, 2016 · Distill")
        P2 = pts_of(n2)
        # a clump to circle: point with the most neighbours within a small radius
        dd = np.linalg.norm(P2[:, None] - P2[None], axis=2)
        cnt = (dd < 0.22).sum(1)
        ci = int(np.argmax(cnt))
        members = np.where(dd[ci] < 0.22)[0]
        clump = Circle(radius=0.38, color=KNOB, stroke_width=4).move_to(P2[members].mean(0))
        with self.narrate("That thirty is a knob you choose. Here is fifty-dimensional noise, no "
                          "clusters at all, at perplexity thirty. Turn it down to two, and each "
                          "point hunts for just two neighbours. The same noise shatters into "
                          "tight little islands.") as beat:
            self.play(FadeIn(h30), run_time=0.6)
            beat.wait_until("noise", offset=-0.2)
            self.play(FadeIn(ntag), LaggedStart(*[FadeIn(d, scale=0.5) for d in n30], lag_ratio=0.01),
                      run_time=1.6)
            self.play(FadeIn(cite2), run_time=0.6)
            beat.wait_until("two", offset=-0.2)
            self.play(TransformFromCopy(h30, h2), run_time=0.9)
            self.play(TransformFromCopy(n30, n2), run_time=beat.until("shatters", offset=-0.1))
            self.play(Create(clump), run_time=0.8)
            self.play(clump.animate.scale(1.15), rate_func=there_and_back, run_time=1.0)

        # ============================================================ 11. real data payoff
        self.fade_out_all(run_time=0.6)
        xs = np.linspace(-3.2, 5.6, 30)
        row1 = VGroup(*[Dot([x, 1.3, 0], radius=0.11, color=BLUE) for x in xs])
        row2 = VGroup(*[Dot([x, 0.0, 0], radius=0.11, color=KEPT if i < 13 else GRAY,
                            fill_opacity=1.0 if i < 13 else 0.5) for i, x in enumerate(xs)])
        rl1 = text("gene data", size=LABEL).next_to(row1, LEFT, buff=0.4)
        rl2 = text("2-D map", size=LABEL).next_to(row2, LEFT, buff=0.4)
        rl2.align_to(rl1, RIGHT)
        cap = text("one cell's 30 nearest neighbours", size=LABEL, color=GRAY).move_to([1.2, 2.5, 0])
        br = Brace(VGroup(*row2[:13]), DOWN, color=KEPT)
        br_t = formula(r"13 \text{ shared}", size=MATH_SMALL + 4, color=KEPT).next_to(br, DOWN, buff=0.15)
        jac = MathTex(r"1-", r"{13", r"\over", r"30+30-13}", r"\approx", r"0.72", font_size=MATH)
        jac[1].set_color(KEPT)
        jac.move_to([-1.6, -2.1, 0])
        rep = MathTex(r"\text{reported average: }", r"> 0.7", font_size=MATH_SMALL + 4).move_to([3.6, -2.1, 0])
        cite3 = citation("Chari & Pachter, 2023 · PLoS Computational Biology")
        jl = text("Jaccard distance", size=SMALL, color=GRAY).next_to(jac, UP, buff=0.2)
        with self.narrate("On real data, Tara Chari and Lior Pachter compared each cell's thirty "
                          "nearest neighbours in the original gene data with its thirty nearest on "
                          "t-SNE and UMAP maps. On average, fewer than half matched. Even "
                          "neighbourhoods, the one thing these maps are built to keep, survive "
                          "only in part.") as beat:
            self.play(FadeIn(cite3), FadeIn(cap), run_time=0.8)
            beat.wait_until("thirty", offset=-0.2)
            self.play(FadeIn(rl1), LaggedStart(*[GrowFromCenter(d) for d in row1], lag_ratio=0.04),
                      run_time=1.4)
            beat.wait_until("thirty nearest on", offset=-0.2)
            self.play(FadeIn(rl2), TransformFromCopy(row1, row2), run_time=1.4)
            beat.wait_until("fewer", offset=-0.3)
            self.play(row1[13:].animate.set_opacity(0.3), GrowFromCenter(br), FadeIn(br_t), run_time=0.9)
            self.play(FadeIn(jl), Write(jac[0]), TransformFromCopy(br_t[0][0:2], jac[1]), Write(jac[2]),
                      run_time=1.0)
            self.play(Write(jac[3]), run_time=0.7)
            self.play(Write(jac[4:]), run_time=0.6)
            self.play(FadeIn(rep, shift=0.1 * LEFT), run_time=0.7)
            beat.wait_until("survive", offset=-0.2)
            self.play(flag(rep[1]), flag(VGroup(*row2[:13]), color=KEPT), run_time=1.0)

        # ============================================================ 12. landing
        self.fade_out_all(run_time=0.6)
        final = make_dots(map_xy(YMAP))
        self.dots = final
        names = VGroup()
        for k, n in enumerate("ABC"):
            names.add(text(n, size=HEADING).next_to(self.island(k), dirs[k], buff=0.25))
        # 3 nearest neighbours on the map, drawn as one VMobject
        P = pts_of(final)
        dd = np.linalg.norm(P[:, None] - P[None], axis=2)
        np.fill_diagonal(dd, np.inf)
        nn = np.argsort(dd, axis=1)[:, :3]
        edges = VMobject(stroke_color=KEPT, stroke_width=1.6, stroke_opacity=0.85)
        for i in range(len(P)):
            for j in nn[i]:
                if i < j or i not in nn[j]:
                    edges.start_new_path(P[i]); edges.add_line_to(P[j])
        edges.set_z_index(-1)
        wB = formula(r"10\times \text{ wider}", size=MATH, color=TRUTH).next_to(names[1], RIGHT, buff=0.3)
        wC = formula(r"5\times \text{ farther}", size=MATH, color=TRUTH).next_to(names[2], RIGHT, buff=0.3)
        kept = text("neighbours: kept", size=LABEL, color=KEPT)
        lost = text("sizes and gaps: gone", size=LABEL, color=MAPC)
        legend = VGroup(kept, lost).arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to([3.4, -0.3, 0])
        with self.narrate("So measure sizes and gaps back in the original fifty dimensions, and "
                          "read the map for who sits near whom. Back to our three islands. B was "
                          "the wide one, and C the far one. They look identical because t-SNE gave "
                          "every point room for the same thirty neighbours.") as beat:
            self.play(LaggedStart(*[FadeIn(self.island(k), scale=0.6) for k in range(3)],
                                  lag_ratio=0.3), FadeIn(names), run_time=1.2)
            beat.wait_until("sizes", offset=-0.2)
            self.play(FadeIn(lost, shift=0.1 * LEFT), run_time=0.7)
            beat.wait_until("who sits", offset=-0.3)
            self.play(Create(edges), FadeIn(kept, shift=0.1 * LEFT), run_time=1.4)
            beat.wait_until("wide one", offset=-0.3)
            self.play(FadeIn(wB, shift=0.1 * LEFT), run_time=0.7)
            beat.wait_until("far one", offset=-0.3)
            self.play(FadeIn(wC, shift=0.1 * LEFT), run_time=0.7)
            beat.wait_until("thirty", offset=-0.4)
            rings = VGroup(*[Circle(radius=0.75, color=KNOB, stroke_width=4).move_to(self.centroid(k))
                             for k in range(3)])
            self.play(LaggedStart(*[Create(r) for r in rings], lag_ratio=0.2),
                      run_time=beat.remaining(0.9))
        self.end_card()

    @staticmethod
    def _norm(T):
        """Centre a snapshot and scale it to the final map's extent (a steady 'camera')."""
        P = T - T.mean(0)
        F = YMAP - YMAP.mean(0)
        s = np.abs(F).max() / max(np.abs(P).max(), 1e-9)
        return P * s + YMAP.mean(0)
