"""Episode 15 - The Dead Fish That Lit Up an fMRI Scanner (multiple comparisons).

    videos/toolkit/render.sh videos/episodes/015-multiple-comparisons-dead-salmon/scene.py Episode \
        videos/episodes/015-multiple-comparisons-dead-salmon/final.mp4

Data: sim_data.npz written by sim.py (1000-voxel fish mask + one-sided p-values of pure noise, seed 8).
"""
from pathlib import Path

import numpy as np
from manim import *
from scipy.stats import norm

from sample_space import *

HERE = Path(__file__).resolve().parent
D = np.load(HERE / "sim_data.npz")
MASK, PVAL = D["mask"], D["p"]
ROWS, COLS = MASK.shape
CELLS = np.argwhere(MASK)                       # same order as PVAL
Z = norm.isf(PVAL)
M_FISH = len(CELLS)                             # 1000

PITCH, SIDE = 0.14, 0.118
FISH_C = np.array([0.0, 0.42, 0.0])
CLUSTER = [(13, 10), (13, 11), (14, 10), (14, 11), (14, 12), (15, 11)]   # schematic, head
CLUMPS = [[(11, 8), (12, 8)], [(6, 32), (7, 32), (8, 31)]]

BAR_L, BAR_W, BAR_Y, BAR_H = -5.0, 10.0, 0.45, 0.62


def noise_opacity(z):
    return 0.22 + 0.5 * float(np.clip((z + 2.0) / 4.5, 0, 1))


def tile_image(seed: int) -> ImageMobject:
    """A 1000-voxel fish as a tiny raster (one tile of the 130,000-voxel scan)."""
    rng = np.random.default_rng(seed)
    k = 3
    arr = np.zeros((ROWS * k, COLS * k, 4), dtype=np.uint8)
    g = np.array([0x8B, 0x93, 0x9E])
    for (r, c) in CELLS:
        a = int(255 * (0.3 + 0.5 * rng.random()))
        arr[r * k:(r + 1) * k - 1, c * k:(c + 1) * k - 1, :3] = g
        arr[r * k:(r + 1) * k - 1, c * k:(c + 1) * k - 1, 3] = a
    im = ImageMobject(arr)
    im.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
    return im


class Episode(NarratedScene):
    EPISODE = 15
    TITLE = "The Dead Fish That Lit Up an fMRI Scanner"
    PRONUNCIATIONS = {"NeuroImage": "neuro image"}

    # ------------------------------------------------------------------ helpers
    def build_fish(self):
        sq = []
        for (r, c) in CELLS:
            s = Square(SIDE, stroke_width=0, fill_color=GRAY, fill_opacity=0.45)
            s.move_to([(c - (COLS - 1) / 2) * PITCH, -(r - (ROWS - 1) / 2) * PITCH, 0])
            sq.append(s)
        vox = VGroup(*sq)
        index = {tuple(rc): i for i, rc in enumerate(map(tuple, CELLS))}
        # eye: a hollow ring in the head
        col = 5
        rows = [r for (r, c) in CELLS if c == col]
        er = int(min(rows) + 0.42 * (max(rows) - min(rows)))
        eye = Circle(radius=0.075, stroke_color=INK, stroke_width=2.5, fill_color=BG,
                     fill_opacity=1).move_to(vox[index[(er, col)]])
        fish = VGroup(vox, eye).move_to(FISH_C)
        return fish, vox, index

    def cells(self, rcs):
        return VGroup(*[self.vox[self.idx[rc]] for rc in rcs])

    # ------------------------------------------------------------------ scene
    def construct(self):
        fish, vox, idx = self.build_fish()
        self.fish, self.vox, self.idx = fish, vox, idx
        eye = fish[1]
        cols = {}
        for i, (r, c) in enumerate(CELLS):
            cols.setdefault(c, []).append(vox[i])
        col_groups = [VGroup(*cols[c]) for c in sorted(cols)]

        # ============================================================ COLD OPEN
        with self.narrate("This salmon was dead when it went into the brain scanner.") as beat:
            self.play(LaggedStart(*[FadeIn(g) for g in col_groups], lag_ratio=0.06),
                      run_time=beat.until("brain"))
            self.play(FadeIn(eye, scale=0.6), run_time=0.6)

        probe_rc = (14, 40)
        probe = vox[idx[probe_rc]]
        with self.narrate("Every tiny cube of it, every voxel, gets its own test, and each test "
                          "raises a false alarm one time in a thousand.") as beat:
            beat.wait_until("voxel", offset=-0.25)
            pbox = Square(SIDE + 0.12, color=YELLOW, stroke_width=3).move_to(probe)
            ptag = label("one voxel", color=YELLOW).move_to(probe.get_center() + UP * 2.05 + RIGHT * 0.9)
            pline = Line(ptag.get_bottom() + DOWN * 0.1, pbox.get_top(), color=YELLOW, stroke_width=2)
            self.play(Create(pbox), FadeIn(ptag, shift=DOWN * 0.1), Create(pline), run_time=0.8)
            rate = formula(r"\text{false alarm rate per test}", "=", r"\tfrac{1}{1000}")
            rate[2].set_color(YELLOW)
            rate.move_to(DOWN * 2.05)
            beat.wait_until("false", offset=-0.1)
            self.play(probe.animate.set_fill(RED, 1), Write(rate[0]), run_time=0.8)
            self.play(probe.animate.set_fill(GRAY, 0.45), Write(rate[1]), run_time=0.6)
            beat.wait_until("one time", offset=-0.1)
            self.play(Write(rate[2]), run_time=0.7)

        Q = formula(r"P(\text{at least one false alarm})", "=", "?", size=38)
        Q.to_edge(UP, buff=0.42).align_to(RIGHT * 6.3, RIGHT)
        with self.narrate("A typical scan has about a hundred and thirty thousand voxels. With "
                          "nothing alive in there, what are the odds of at least one false alarm? "
                          "Make a guess. [pause 1.5]") as beat:
            nvox = formula(r"\text{voxels per scan}", r"\approx", r"130{,}000")
            nvox.next_to(rate, DOWN, buff=0.35)
            beat.wait_until("hundred", offset=-0.2)
            self.play(Write(nvox), run_time=1.0)
            beat.wait_until("odds", offset=-0.2)
            self.play(Write(Q[0]), Write(Q[1]), run_time=1.3)
            self.play(Write(Q[2]), run_time=0.5)
            beat.wait_until("guess", offset=0.2)
            self.play(Indicate(Q[2], color=YELLOW, scale_factor=1.3), run_time=1.0)
            self.play(Circumscribe(Q, color=YELLOW, stroke_width=2), run_time=1.4)

        # ============================================================ STAKES
        cite = citation("Bennett, Baird, Miller & Wolford, 2010 · J. Serendipitous and "
                        "Unexpected Results · Ig Nobel 2012")
        photos = label("48 photos:  “What is this person feeling?”").move_to(DOWN * 2.1)
        clus = self.cells(CLUSTER)
        schem = label("schematic", size=22, color=GRAY)
        schem.move_to(clus.get_center() + UP * 1.75 + RIGHT * 0.2)
        sline = Line(schem.get_bottom() + DOWN * 0.08, clus.get_top() + UP * 0.08,
                     color=GRAY, stroke_width=1.5)
        with self.narrate("In two thousand nine, Craig Bennett's team did this for real. They "
                          "showed the dead fish forty-eight photos of people in social "
                          "situations, and asked what each person was feeling. A cluster in "
                          "its brain lit up.") as beat:
            self.play(FadeOut(VGroup(rate, nvox, pbox, ptag, pline), shift=DOWN * 0.2),
                      FadeIn(cite, shift=UP * 0.1), run_time=1.0)
            beat.wait_until("forty", offset=-0.2)
            self.play(Write(photos), run_time=1.4)
            beat.wait_until("cluster", offset=-0.15)
            self.play(LaggedStart(*[c.animate.set_fill(RED, 1) for c in clus], lag_ratio=0.2),
                      run_time=1.0)
            self.play(FadeIn(schem), Create(sline), run_time=0.6)

        with self.narrate("If noise can fool a scan of a dead fish, it can fool any brain map.") as beat:
            beat.wait_until("noise", offset=-0.1)
            others = [i for i, rc in enumerate(map(tuple, CELLS)) if rc not in CLUSTER]
            self.play(*[vox[i].animate.set_fill(GRAY, noise_opacity(Z[i])) for i in others],
                      FadeOut(photos), run_time=1.2)
            beat.wait_until("fool", 2, offset=-0.1)
            self.play(LaggedStart(*[Indicate(c, color=RED, scale_factor=1.3) for c in clus],
                                  lag_ratio=0.1), run_time=1.0)

        # ============================================================ NAIVE BUILD
        sim = label("simulated: 1,000 voxels of pure noise", color=GRAY)
        sim.to_edge(UP, buff=0.42).align_to(LEFT * 6.3, LEFT)
        if sim.get_right()[0] > Q.get_left()[0] - 0.3:
            sim.scale_to_fit_width(Q.get_left()[0] - 0.3 + 6.3)
            sim.align_to(LEFT * 6.3, LEFT)
        with self.narrate("So build the scanner yourself. Here is a simulated fish, a thousand "
                          "voxels of pure noise.") as beat:
            self.play(FadeOut(VGroup(cite, schem, sline)),
                      *[vox[idx[rc]].animate.set_fill(GRAY, noise_opacity(Z[idx[rc]])) for rc in CLUSTER],
                      run_time=1.0)
            beat.wait_until("simulated", offset=-0.2)
            self.play(Write(sim), run_time=1.2)
            beat.wait_until("thousand", offset=-0.1)
            self.play(Indicate(sim, color=INK, scale_factor=1.04), run_time=0.8)

        # bottom panel: version label (left) + live counter (right)
        ver = MathTex(r"\text{v1: }", "p", "<", "0.05", font_size=MATH)
        ver[3].set_color(YELLOW)
        ver.move_to([-3.6, -2.15, 0])
        count = ValueTracker(0)
        counter = live_number(count, 0, prefix=r"\text{false alarms} =", color=INK)
        counter.number.set_color(RED)
        counter.move_to([2.9, -2.15, 0])
        hits05 = [i for i in range(M_FISH) if PVAL[i] < 0.05]
        hits001 = [i for i in range(M_FISH) if PVAL[i] < 0.001]
        sweep = ValueTracker(fish.get_left()[0] - 0.2)
        scan_line = always_redraw(lambda: Line(
            [sweep.get_value(), fish.get_bottom()[1] - 0.1, 0],
            [sweep.get_value(), fish.get_top()[1] + 0.1, 0], color=YELLOW, stroke_width=3))
        hit_x = np.array([vox[i].get_center()[0] for i in hits05])

        def paint(m):
            x = sweep.get_value()
            for j, i in enumerate(hits05):
                if hit_x[j] <= x:
                    vox[i].set_fill(RED, 1)
            count.set_value(int((hit_x <= x).sum()))

        with self.narrate("Version one tests each voxel at the textbook threshold, p less than "
                          "point oh five.") as beat:
            self.play(Write(ver), FadeIn(counter), run_time=1.0)
            beat.wait_until("tests", offset=-0.1)
            painter = Mobject()
            painter.add_updater(paint)
            self.add(scan_line, painter)
            self.play(sweep.animate.set_value(fish.get_right()[0] + 0.2),
                      run_time=beat.remaining(min_time=2.5), rate_func=linear)
            painter.clear_updaters()
            self.remove(scan_line, painter)

        exp_ = MathTex("1000", r"\times", "0.05", "=", "50", r"\text{ expected}", font_size=MATH)
        exp_[2].set_color(YELLOW)
        exp_.next_to(counter, DOWN, buff=0.32).align_to(counter, LEFT)
        boxes = VGroup(*[SurroundingRectangle(self.cells(c), color=INK, buff=0.06,
                                              stroke_width=2.5) for c in CLUMPS])
        with self.narrate("Fifty-one voxels light up, some in little clumps. That's the "
                          "threshold doing its job: one false alarm per twenty tests.") as beat:
            self.play(Indicate(counter.number, color=RED, scale_factor=1.25), run_time=0.9)
            beat.wait_until("clumps", offset=-0.2)
            self.play(LaggedStart(*[Create(b) for b in boxes], lag_ratio=0.4), run_time=1.0)
            beat.wait_until("one false", offset=-0.1)
            self.play(FadeOut(boxes), Write(exp_[0:2]), TransformFromCopy(ver[3], exp_[2]),
                      run_time=1.0)
            self.play(Write(exp_[3:]), run_time=0.8)

        ver2 = MathTex(r"\text{v2: }", "p", "<", "0.001", font_size=MATH).move_to(ver, aligned_edge=LEFT)
        ver2[3].set_color(YELLOW)
        exp2 = MathTex("1000", r"\times", "0.001", "=", "1", r"\text{ expected}", font_size=MATH)
        exp2[2].set_color(YELLOW)
        exp2.move_to(exp_, aligned_edge=LEFT)
        drop = [i for i in hits05 if i not in hits001]
        surv = VGroup(*[vox[i] for i in hits001])
        with self.narrate("Version two uses the salmon study's threshold, p less than point oh "
                          "oh one. Two voxels survive.") as beat:
            beat.wait_until("point", offset=-0.2)
            self.play(TransformMatchingTex(ver, ver2), TransformMatchingTex(exp_, exp2), run_time=1.2)
            self.play(flag(ver2[3]), run_time=0.8)
            beat.wait_until("Two", offset=-0.5)
            self.play(*[vox[i].animate.set_fill(GRAY, noise_opacity(Z[i])) for i in drop],
                      count.animate.set_value(2), run_time=1.0)
            sboxes = VGroup(*[Square(SIDE + 0.14, color=INK, stroke_width=2.5).move_to(v) for v in surv])
            self.play(LaggedStart(*[Create(b) for b in sboxes], lag_ratio=0.3), run_time=0.8)

        # 130 tiles = 130,000 voxels
        TW = 0.80
        tiles = Group()
        grid_c = np.array([0.0, -0.35, 0.0])
        nx, ny, dx, dy = 13, 10, 0.93, 0.52
        positions = [grid_c + np.array([(i - (nx - 1) / 2) * dx, ((ny - 1) / 2 - j) * dy, 0])
                     for j in range(ny) for i in range(nx)]
        for k, pos in enumerate(positions[1:]):
            tiles.add(tile_image(100 + k).set_width(TW).move_to(pos))
        big = MathTex(r"130", r"\times", r"1{,}000", "=", r"130{,}000", r"\text{ voxels}",
                      font_size=MATH).to_edge(UP, buff=0.42).align_to(LEFT * 6.3, LEFT)
        panel = VGroup(ver2, counter, exp2)
        with self.narrate("Better. But the real scan had a hundred and thirty times more voxels.") as beat:
            self.play(FadeOut(sboxes), run_time=0.5)
            beat.wait_until("real", offset=-0.2)
            self.play(FadeOut(panel), FadeOut(sim),
                      fish.animate.scale(TW / fish.width).move_to(positions[0]), run_time=1.0)
            self.play(LaggedStart(*[FadeIn(t) for t in tiles], lag_ratio=0.02),
                      Write(big), run_time=beat.remaining(min_time=1.6))

        # ============================================================ INSIGHT: the bar
        alpha = ValueTracker(0.05)
        logm = ValueTracker(0.0)
        mode = {"bonf": False}

        def m_int():
            return int(round(10 ** logm.get_value()))

        def clean():
            m, a = m_int(), alpha.get_value()
            if mode["bonf"]:
                return (1 - a / m) ** m
            return (1 - a) ** m

        def blue_rect():
            w = max(BAR_W * clean(), 0.0)
            r = Rectangle(width=max(w, 1e-4), height=BAR_H, stroke_width=0, fill_color=BLUE,
                          fill_opacity=0.95 if w > 1e-3 else 0)
            return r.move_to([BAR_L + max(w, 1e-4) / 2, BAR_Y, 0])

        def red_rect():
            w = BAR_W * (1 - clean())
            r = Rectangle(width=max(w, 1e-4), height=BAR_H, stroke_width=0, fill_color=RED,
                          fill_opacity=0.95 if w > 1e-3 else 0)
            return r.move_to([BAR_L + BAR_W - max(w, 1e-4) / 2, BAR_Y, 0])

        blue = always_redraw(blue_rect)
        red = always_redraw(red_rect)
        frame_ = Rectangle(width=BAR_W, height=BAR_H, stroke_color=GRAY, stroke_width=1.5) \
            .move_to([BAR_L + BAR_W / 2, BAR_Y, 0])
        lab_clean = label("P(clean)", color=BLUE).next_to(frame_, UP, buff=0.22).align_to(frame_, LEFT)
        lab_red = label("at least one false alarm", color=RED).next_to(frame_, UP, buff=0.22) \
            .align_to(frame_, RIGHT)
        ticks = VGroup()
        for v, tex in ((0, "0"), (0.5, r"\tfrac{1}{2}"), (1, "1")):
            x = BAR_L + BAR_W * v
            t = Line([x, BAR_Y - BAR_H / 2 - 0.02, 0], [x, BAR_Y - BAR_H / 2 - 0.14, 0],
                     color=GRAY, stroke_width=2)
            n = MathTex(tex, font_size=MATH_SMALL, color=GRAY).next_to(t, DOWN, buff=0.1)
            ticks.add(VGroup(t, n))

        RO_Y = -2.45
        a_lab = MathTex(r"\alpha", "=", "0.05", font_size=MATH, color=YELLOW).move_to([-4.6, RO_Y, 0])
        m_num = DecimalNumber(1, num_decimal_places=0, font_size=MATH, color=INK)
        m_pre = MathTex("m", "=", font_size=MATH)
        m_num.add_updater(lambda d: d.set_value(m_int()).next_to(m_pre, RIGHT, buff=0.15))
        m_lab = VGroup(m_pre, m_num)
        m_pre.move_to([-1.75, RO_Y, 0])
        p_pre = MathTex(r"P(\text{clean})", "=", font_size=MATH, color=BLUE).move_to([1.7, RO_Y, 0])
        p_num = DecimalNumber(1, num_decimal_places=3, font_size=MATH, color=BLUE)
        p_num.add_updater(lambda d: d.set_value(clean()).next_to(p_pre, RIGHT, buff=0.15))
        p_lab = VGroup(p_pre, p_num)

        mini_c = np.array([-4.75, 2.55, 0])
        with self.narrate("To see why that matters, go back to one in twenty. This bar is the "
                          "chance that the whole scan stays clean.") as beat:
            self.play(FadeOut(tiles), FadeOut(big),
                      fish.animate.scale(3.0 / TW).move_to(mini_c), run_time=1.2)
            beat.wait_until("one in twenty", offset=-0.1)
            self.play(Write(a_lab), run_time=0.8)
            beat.wait_until("bar", offset=-0.2)
            logm.set_value(-20)                       # m rounds to 0 -> clean = 1
            self.add(red)
            self.play(GrowFromEdge(frame_, LEFT), FadeIn(blue), run_time=0.8)
            self.play(FadeIn(lab_clean, shift=UP * 0.1), FadeIn(ticks), run_time=0.8)

        f1 = MathTex(r"P(\text{clean})", "=", "0.95", font_size=EQ).move_to([0, -1.35, 0])
        f1[0].set_color(BLUE)
        f1[2].set_color(BLUE)
        with self.narrate("The first test keeps ninety-five percent of it, and loses the rest "
                          "to a false alarm.") as beat:
            self.play(FadeIn(m_lab), FadeIn(p_lab), run_time=0.6)
            beat.wait_until("ninety", offset=-0.2)
            self.play(logm.animate.set_value(0.0), run_time=1.0)
            self.play(TransformFromCopy(p_lab, f1), run_time=1.0)
            beat.wait_until("rest", offset=-0.1)
            self.play(FadeIn(lab_red, shift=UP * 0.1), Indicate(red, color=RED, scale_factor=1.15),
                      run_time=0.9)

        f2 = MathTex(r"P(\text{clean})", "=", "0.95", r"\times", "0.95", font_size=EQ).move_to(f1)
        f3 = MathTex(r"P(\text{clean})", "=", "0.95", "^{m}", font_size=EQ).move_to(f1)
        for f in (f2, f3):
            f[0].set_color(BLUE)
        f2[2].set_color(BLUE), f2[4].set_color(BLUE), f3[2].set_color(BLUE)
        f3[3].set_color(INK)
        indep = label("independent tests", size=24, color=GRAY)
        with self.narrate("The second keeps ninety-five percent of what's left. For independent "
                          "tests, after m of them, the clean part is point nine five to the m.") as beat:
            self.play(logm.animate.set_value(np.log10(2)), run_time=1.0)
            self.play(TransformMatchingTex(f1, f2), run_time=1.0)
            beat.wait_until("independent", offset=-0.1)
            indep.next_to(f2, RIGHT, buff=0.4)
            self.play(FadeIn(indep), run_time=0.6)
            beat.wait_until("point nine", offset=-0.2)
            self.play(TransformMatchingTex(f2, f3), indep.animate.next_to(f3, RIGHT, buff=0.4),
                      run_time=1.2)
            self.play(TransformFromCopy(m_pre[0], f3[3]), run_time=0.8)

        p_small = MathTex(r"5 \times 10^{-23}", font_size=MATH, color=BLUE)
        with self.narrate("Fourteen tests, and it's below a half. A thousand, and it's about "
                          "five times ten to the minus twenty-three.") as beat:
            self.play(logm.animate.set_value(np.log10(14)), run_time=beat.until("half", offset=-0.3),
                      rate_func=linear)
            self.play(Indicate(ticks[1], color=YELLOW), run_time=0.8)
            beat.wait_until("thousand", offset=-1.2)
            self.play(logm.animate.set_value(3.0), run_time=1.4, rate_func=smooth)
            p_num.clear_updaters()
            p_small.next_to(p_pre, RIGHT, buff=0.15)
            beat.wait_until("five", offset=-0.1)
            self.play(FadeTransform(p_num, p_small), run_time=0.8)

        a_new = MathTex(r"\alpha", "=", "0.001", font_size=MATH, color=YELLOW).move_to(a_lab, aligned_edge=LEFT)
        f4 = MathTex(r"P(\text{clean})", "=", "0.999", "^{m}", font_size=EQ).move_to(f3)
        f4[0].set_color(BLUE), f4[2].set_color(BLUE)
        p_num2 = DecimalNumber(0.368, num_decimal_places=3, font_size=MATH, color=BLUE)
        with self.narrate("Now set alpha to one in a thousand. Our thousand-voxel fish stays "
                          "clean only thirty-seven percent of the time.") as beat:
            beat.wait_until("one in", offset=-0.2)
            alpha.set_value(0.001)
            p_num2.next_to(p_pre, RIGHT, buff=0.15)
            self.play(TransformMatchingTex(a_lab, a_new), TransformMatchingTex(f3, f4),
                      FadeTransform(p_small, p_num2), indep.animate.next_to(f4, RIGHT, buff=0.4),
                      run_time=1.2)
            self.play(flag(a_new[2]), flag(f4[2]), run_time=0.8)
            beat.wait_until("fish", offset=-0.3)
            self.play(Indicate(fish, color=INK, scale_factor=1.06), run_time=0.9)
            beat.wait_until("thirty", offset=-0.1)
            self.play(Indicate(p_num2, color=BLUE, scale_factor=1.2), run_time=0.8)

        p_tiny = MathTex(r"3 \times 10^{-57}", font_size=MATH, color=BLUE)
        Q2 = MathTex(r"P(\text{at least one false alarm})", r"\approx", "1", font_size=38)
        Q2[2].set_color(RED)
        Q2.move_to(Q, aligned_edge=RIGHT)
        expc = MathTex(r"\text{expected}", "=", "m", r"\alpha", "=", "130", font_size=MATH)
        expc[3].set_color(YELLOW), expc[5].set_color(RED)
        expc.next_to(Q2, DOWN, buff=0.3).align_to(Q2, RIGHT)
        with self.narrate("At a hundred and thirty thousand voxels, it's three times ten to the "
                          "minus fifty-seven. So, your guess: a false alarm is certain, and about "
                          "a hundred and thirty are expected.") as beat:
            p_num2.add_updater(lambda d: d.set_value(clean()).next_to(p_pre, RIGHT, buff=0.15))
            self.play(logm.animate.set_value(np.log10(130000)), run_time=beat.until("three", offset=-0.1),
                      rate_func=smooth)
            p_num2.clear_updaters()
            p_tiny.next_to(p_pre, RIGHT, buff=0.15)
            self.play(FadeTransform(p_num2, p_tiny), run_time=0.8)
            beat.wait_until("guess", offset=-0.2)
            self.play(Indicate(Q, color=YELLOW, scale_factor=1.05), run_time=0.8)
            beat.wait_until("certain", offset=-0.2)
            self.play(TransformMatchingTex(Q, Q2), run_time=1.0)
            beat.wait_until("hundred", 2, offset=-0.6)
            self.play(Write(expc[0:2]), TransformFromCopy(m_pre[0], expc[2]),
                      TransformFromCopy(a_new[0], expc[3]), run_time=1.0)
            self.play(Write(expc[4:]), run_time=0.6)

        # ============================================================ FIX: alpha / m
        a_bon = MathTex(r"\alpha", "=", "0.05", font_size=MATH, color=YELLOW).move_to(a_lab, aligned_edge=LEFT)
        f5 = MathTex(r"P(\text{clean})", "=", r"\Big(1-", r"\frac{\alpha}{m}", r"\Big)", "^{m}",
                     font_size=EQ).move_to(f4)
        f5[0].set_color(BLUE), f5[3].set_color(GREEN)
        per = MathTex(r"\text{each test: }", r"\frac{\alpha}{m}", font_size=MATH)
        per[1].set_color(GREEN)
        with self.narrate("Fix it by dividing alpha by m, so each test gets stricter as the "
                          "tests pile up.") as beat:
            beat.wait_until("dividing", offset=-0.2)
            self.play(TransformMatchingTex(f4, f5), FadeOut(indep),
                      TransformMatchingTex(a_new, a_bon), run_time=1.4)
            self.play(flag(f5[3], color=GREEN), run_time=0.8)
            beat.wait_until("stricter", offset=-0.3)
            mode["bonf"] = True
            alpha.set_value(0.05)
            logm.set_value(0.0)
            p_tiny2 = p_tiny
            p_num3 = DecimalNumber(clean(), num_decimal_places=3, font_size=MATH, color=BLUE)
            p_num3.next_to(p_pre, RIGHT, buff=0.15)
            self.play(FadeTransform(p_tiny2, p_num3), run_time=0.8)
            p_num3.add_updater(lambda d: d.set_value(clean()).next_to(p_pre, RIGHT, buff=0.15))
            self.play(logm.animate.set_value(np.log10(130000)), run_time=beat.remaining(min_time=1.5),
                      rate_func=smooth)

        f6 = MathTex(r"P(\text{at least one false alarm})", r"\le", "m", r"\cdot", r"\frac{\alpha}{m}",
                     font_size=EQ).move_to(f5)
        f6[0].set_color(RED), f6[4].set_color(GREEN)
        f7 = MathTex(r"P(\text{at least one false alarm})", r"\le", r"\alpha", font_size=EQ).move_to(f5)
        f7[0].set_color(RED), f7[2].set_color(YELLOW)
        with self.narrate("Now each test can take at most alpha over m from the bar, so all m "
                          "tests together take at most alpha.") as beat:
            self.play(logm.animate.set_value(0.0), run_time=1.0)
            beat.wait_until("alpha over", offset=-0.2)
            self.play(Indicate(red, color=GREEN, scale_factor=1.1), flag(f5[3], color=GREEN), run_time=0.9)
            beat.wait_until("all", offset=-0.2)
            self.play(TransformMatchingTex(f5, f6), run_time=1.2)
            self.play(logm.animate.set_value(np.log10(130000)), run_time=1.6, rate_func=smooth)
            beat.wait_until("at most", 2, offset=-0.1)
            self.play(TransformMatchingTex(f6, f7), run_time=1.0)

        # back to the fish: v3
        ver3 = MathTex(r"\text{v3: }", "p", "<", r"\tfrac{0.05}{1000}", "=", "0.00005", font_size=MATH)
        ver3[3].set_color(GREEN), ver3[5].set_color(GREEN)
        ver3.move_to([-3.4, -2.15, 0])
        counter.move_to([3.4, -2.15, 0])
        insight = VGroup(frame_, lab_clean, lab_red, ticks, a_bon, m_lab, p_pre, p_num3, f7)
        with self.narrate("On our fish, that's p less than five in a hundred thousand, and the "
                          "last two voxels go dark.") as beat:
            m_num.clear_updaters()
            p_num3.clear_updaters()
            self.remove(blue, red)
            self.play(FadeOut(insight), FadeOut(blue.copy().clear_updaters()),
                      fish.animate.scale(1 / fish.width * 10.36 * fish.width / fish[0].width)
                      .move_to(FISH_C), run_time=1.2)
            self.play(Write(ver3), FadeIn(counter), run_time=1.2)
            beat.wait_until("dark", offset=-0.5)
            self.play(*[vox[i].animate.set_fill(GRAY, noise_opacity(Z[i])) for i in hits001],
                      count.animate.set_value(0), run_time=1.0)

        # power: a truly active voxel
        ax = axes((-1.5, 7.0, 1.0), (0, 0.45), x_ticks=[0, 2, 4, 6], y_ticks=[0, 0.2, 0.4],
                  x_length=9.6, y_length=2.6, x_label="voxel's test statistic z (signal / noise)",
                  y_label="probability density")
        ax.move_to([0.6, -0.85, 0])
        curve = ax.plot(lambda x: norm.pdf(x, 3), x_range=[-0.5, 7.0], color=PURPLE, stroke_width=4)
        z05, zb = norm.isf(0.05), norm.isf(0.00005)

        def thr(z, col, tex):
            ln = Line(ax.c2p(z, 0), ax.c2p(z, 0.47), color=col, stroke_width=3)
            t = MathTex(tex, font_size=MATH_SMALL, color=col).next_to(ln, UP, buff=0.12)
            return VGroup(ln, t)
        t05 = thr(z05, YELLOW, r"p<0.05")
        tb = thr(zb, GREEN, r"p<0.00005")
        area05 = ax.get_area(curve, x_range=[z05, 7.0], color=PURPLE, opacity=0.35)
        areab = ax.get_area(curve, x_range=[zb, 7.0], color=PURPLE, opacity=0.75)
        pw05 = MathTex(r"91\%", font_size=MATH, color=PURPLE).move_to(ax.c2p(2.55, 0.12))
        pwb = MathTex(r"19\%", font_size=MATH, color=PURPLE).move_to(ax.c2p(4.75, 0.09))
        act = label("truly active voxel", color=PURPLE)
        act.next_to(ax.c2p(3.0, 0.4), LEFT, buff=0.3).shift(LEFT * 0.4)
        with self.narrate("The price is power. A truly active voxel, with a signal three times "
                          "the noise, used to pass ninety-one percent of the time. Now, nineteen "
                          "percent.") as beat:
            self.play(FadeOut(VGroup(ver3, counter)), fish.animate.scale(3.0 / 10.36).move_to(mini_c),
                      run_time=1.0)
            self.play(Create(ax), run_time=beat.until("truly", offset=-0.2))
            self.play(Create(curve), FadeIn(act), run_time=1.2)
            beat.wait_until("ninety", offset=-0.6)
            self.play(FadeIn(t05), FadeIn(area05), run_time=0.8)
            self.play(Write(pw05), run_time=0.5)
            beat.wait_until("Now", offset=-0.2)
            self.play(FadeIn(tb), FadeIn(areab), pw05.animate.set_opacity(0.4), run_time=0.8)
            self.play(Write(pwb), run_time=0.5)

        fdr_brace = BraceBetweenPoints(ax.c2p(z05, 0.5), ax.c2p(zb, 0.5), direction=UP, color=GRAY)
        fdr_lab = label("false discovery rate cutoff", size=26, color=GRAY)
        bh = citation("Benjamini & Hochberg, 1995 · J. Royal Statistical Society B")
        with self.narrate("So brain imagers use gentler corrections, like the false discovery "
                          "rate, that still count the tests.") as beat:
            fdr_brace.shift(UP * 0.55)
            fdr_lab.next_to(fdr_brace, UP, buff=0.12)
            self.play(t05[1].animate.shift(LEFT * 0.0), run_time=0.3)
            beat.wait_until("false", offset=-0.3)
            self.play(GrowFromCenter(fdr_brace), FadeIn(fdr_lab, shift=UP * 0.1),
                      FadeIn(bh), run_time=1.0)

        # ============================================================ PAYOFF
        unc = MathTex(r"\text{uncorrected: }", "p<0.001", r",\ \ \text{clusters} \ge 3 \text{ voxels}",
                      font_size=MATH).move_to([0, -2.0, 0])
        unc[1].set_color(YELLOW)
        cor = MathTex(r"\text{FDR or family-wise, }", "0.05", r":\ \ 0 \text{ voxels}",
                      font_size=MATH).move_to([0, -2.0, 0])
        cor[1].set_color(GREEN)
        power_g = VGroup(ax, curve, t05, tb, area05, areab, pw05, pwb, act, fdr_brace, fdr_lab)
        with self.narrate("That's the salmon result. Uncorrected, at p less than point oh oh one "
                          "with clusters of at least three voxels, the fish showed a cluster in "
                          "its brain cavity. With false discovery rate or family-wise correction, "
                          "nothing.") as beat:
            self.play(FadeOut(power_g), FadeOut(bh), FadeOut(expc),
                      fish.animate.scale(10.36 / 3.0).move_to(FISH_C), FadeIn(cite), run_time=1.2)
            beat.wait_until("Uncorrected", offset=-0.2)
            self.play(Write(unc), run_time=1.4)
            beat.wait_until("cluster", 2, offset=-0.2)
            self.play(LaggedStart(*[c.animate.set_fill(RED, 1) for c in clus], lag_ratio=0.2),
                      FadeIn(schem), Create(sline), run_time=1.0)
            beat.wait_until("With", offset=-0.2)
            self.play(FadeOut(unc, shift=UP * 0.2), FadeIn(cor, shift=UP * 0.2), run_time=1.0)
            beat.wait_until("nothing", offset=-0.2)
            self.play(*[c.animate.set_fill(GRAY, 0.45) for c in clus], run_time=0.9)

        # NeuroImage 2008: 193 of 260 corrected
        PB_L, PB_W, PB_Y = -4.0, 8.0, -2.05
        w_c = PB_W * 193 / 260
        pb_c = Rectangle(width=w_c, height=0.34, stroke_width=0, fill_color=GRAY, fill_opacity=0.55) \
            .move_to([PB_L + w_c / 2, PB_Y, 0])
        pb_u = Rectangle(width=PB_W - w_c, height=0.34, stroke_width=0, fill_color=YELLOW,
                         fill_opacity=0.95).move_to([PB_L + w_c + (PB_W - w_c) / 2, PB_Y, 0])
        pb_lab = MathTex(r"67 \text{ of } 260 \text{ uncorrected}", font_size=MATH_SMALL + 6,
                         color=YELLOW).next_to(pb_u, DOWN, buff=0.18).align_to(pb_u, RIGHT)
        pb_name = label("NeuroImage fMRI studies, 2008", size=26, color=GRAY) \
            .next_to(pb_c, DOWN, buff=0.18).align_to(pb_c, LEFT)
        with self.narrate("Yet in two thousand eight, about one in four fMRI studies in the "
                          "journal NeuroImage skipped this correction.") as beat:
            self.play(FadeOut(cor), FadeOut(schem), FadeOut(sline), run_time=0.6)
            beat.wait_until("one in four", offset=-0.4)
            self.play(GrowFromEdge(pb_c, LEFT), GrowFromEdge(pb_u, LEFT), FadeIn(pb_name), run_time=1.2)
            self.play(Write(pb_lab), run_time=0.8)

        # ============================================================ LANDING
        with self.narrate("The salmon never saw a single face. It just gave a one in a thousand "
                          "fluke a hundred and thirty thousand tries.") as beat:
            self.play(FadeOut(VGroup(pb_c, pb_u, pb_lab, pb_name, cite)), run_time=0.8)
            beat.wait_until("fluke", offset=-0.3)
            self.play(LaggedStart(*[c.animate.set_fill(RED, 1) for c in clus], lag_ratio=0.15),
                      run_time=1.0)
            beat.wait_until("hundred", offset=-0.2)
            self.play(Indicate(Q2, color=RED, scale_factor=1.06), run_time=1.0)

        self.end_card()
