"""Episode 11: How Serial Numbers Counted Germany's Tanks.

    videos/toolkit/render.sh videos/episodes/011-german-tank-problem/scene.py Episode \
        videos/episodes/011-german-tank-problem/final.mp4
"""
from math import comb

import numpy as np
from manim import *
from sample_space import *

# --------------------------------------------------------------------------- data
SAMPLE = [8, 14, 22, 31, 89]          # one hand-picked simulated capture, k = 5
K = len(SAMPLE)
M = max(SAMPLE)                        # 89
MEAN = sum(SAMPLE) / K                 # 32.8
GAP = (M - K) / K                      # 16.8
EST = M + GAP                          # 105.8
TRUE_N = 100
GAPS = [(1, 7), (9, 13), (15, 21), (23, 30), (32, 88)]   # unseen runs below 89 (sum 84)

R = 10_000                             # simulated captures
_rng = np.random.default_rng(11)
_S = np.array([_rng.choice(np.arange(1, TRUE_N + 1), K, replace=False) for _ in range(R)])
_m = _S.max(1)
E_DOUBLE = 2 * _S.mean(1)
E_MAX = _m.astype(float)
E_GAP = _m + _m / K - 1
IMPOSSIBLE = E_DOUBLE < _m             # doubling the average guessed below a serial in hand

H_LO, H_HI, BIN = 20, 200, 4
EDGES = np.arange(H_LO + 0.5, H_HI + 0.5 + 1e-9, BIN)       # 20.5 ... 200.5
NB = len(EDGES) - 1
CHECK = 100                                                 # cumulative checkpoints


def cum_hist(values, mask=None):
    v = np.clip(values, EDGES[0] + 1e-6, EDGES[-1] - 1e-6)
    idx = np.digitize(v, EDGES) - 1
    out = np.zeros((CHECK + 1, NB))
    step = R // CHECK
    for j in range(1, CHECK + 1):
        sel = idx[:j * step] if mask is None else idx[:j * step][mask[:j * step]]
        out[j] = np.bincount(sel, minlength=NB)[:NB]
    return out


# --------------------------------------------------------------------------- geometry
NL_LEN = 11.2
NL_X0 = -5.6


def X(s):                               # serial number -> scene x on the number line
    return NL_X0 + s * NL_LEN / 120


HX0, HX1 = -3.9, 6.0                    # histogram estimate axis: 20..200


def HXp(v):
    return HX0 + (v - H_LO) * (HX1 - HX0) / (H_HI - H_LO)


class Episode(NarratedScene):
    EPISODE = 11
    TITLE = "How Serial Numbers Counted Germany's Tanks"

    # ------------------------------------------------------------------ helpers
    def build_line(self, y):
        line = Line([X(0), y, 0], [X(120), y, 0], color=GRAY, stroke_width=3)
        minor = VGroup(*[Line([X(s), y - 0.07, 0], [X(s), y + 0.07, 0], color=GRAY,
                              stroke_width=2) for s in range(0, 121, 10)])
        nums = VGroup(*[MathTex(str(s), font_size=MATH_SMALL, color=GRAY)
                        .move_to([X(s), y - 0.36, 0]) for s in (0, 30, 60, 90, 120)])
        name = label("gearbox serial number", size=SMALL + 2, color=GRAY)
        name.next_to(nums, DOWN, buff=0.18).align_to(line, RIGHT)
        return VGroup(line, minor, nums, name)

    def capture_tick(self, s, y):
        tick = Line([X(s), y, 0], [X(s), y + 0.42, 0], color=BLUE, stroke_width=6)
        num = MathTex(str(s), font_size=MATH, color=BLUE).next_to(tick, UP, buff=0.12)
        return VGroup(tick, num)

    def construct(self):
        y0 = 0.5
        nl = self.build_line(y0)
        caps = VGroup(*[self.capture_tick(s, y0) for s in SAMPLE])
        sim_tag = label("simulated", size=SMALL, color=GRAY).move_to([5.6, 3.35, 0], aligned_edge=RIGHT)
        n_q = formula(r"N", r"=", r"?", size=MATH, color=GREEN).move_to([X(116), y0 + 0.9, 0])

        # ============================================================ 1 cold open
        with self.narrate("Five captured tanks have gearboxes stamped eight, fourteen, twenty two, "
                          "thirty one and eighty nine. The factory numbers them in order, starting "
                          "from one. How many tanks has it built? [pause 1.5]") as beat:
            self.play(Create(nl[0]), FadeIn(nl[1]), FadeIn(sim_tag), run_time=beat.until("eight", offset=-0.15))
            for i, w in enumerate(["eight", "fourteen", "twenty two", "thirty one", "eighty nine"]):
                if i:
                    beat.wait_until(w, offset=-0.15)
                self.play(FadeIn(caps[i], shift=0.35 * DOWN), run_time=0.45)
            beat.wait_until("order", offset=-0.2)
            self.play(FadeIn(nl[2]), FadeIn(nl[3]), run_time=0.8)
            arrow1 = Arrow([X(1), y0 - 1.05, 0], [X(40), y0 - 1.05, 0], color=GRAY, buff=0,
                           stroke_width=3, max_tip_length_to_length_ratio=0.08)
            one = MathTex("1, 2, 3, \\dots", font_size=MATH_SMALL, color=GRAY).next_to(arrow1, DOWN, buff=0.12).align_to(arrow1, LEFT)
            self.play(GrowArrow(arrow1), FadeIn(one), run_time=beat.until("How", offset=-0.3))
            self.play(FadeOut(arrow1), FadeOut(one), Write(n_q), run_time=1.0)

        # ============================================================ 2 stakes
        spy_head = label("Allied intelligence, August 1942", size=LABEL, color=GRAY)
        spy_num = formula(r"1550", r"\text{ tanks / month}", size=EQ, color=PURPLE)
        spy = VGroup(spy_head, spy_num).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        spy.move_to([0, -1.75, 0])
        cite = citation("Ruggles & Brodie, 1947 · Journal of the American Statistical Association")
        with self.narrate("In the summer of nineteen forty two, this was a real question. Allied "
                          "intelligence put German tank production at one thousand five hundred and "
                          "fifty a month. The serial numbers told a different story.") as beat:
            self.play(FadeIn(spy_head, shift=0.2 * UP), run_time=beat.until("intelligence", offset=-0.2))
            beat.wait_until("one thousand", offset=-0.2)
            self.play(Write(spy_num), FadeIn(cite), run_time=1.2)
            beat.wait_until("serial", offset=-0.2)
            self.play(LaggedStart(*[Indicate(c[0], color=BLUE, scale_factor=1.15) for c in caps],
                                  lag_ratio=0.15), run_time=1.6)
        self.play(FadeOut(spy), FadeOut(cite), run_time=0.5)

        # ============================================================ 3 naive 1: double the mean
        yb = y0 - 1.25
        mean_dot = Triangle(color=INK, fill_opacity=1, stroke_width=0).scale(0.11).move_to([X(MEAN), yb, 0])
        mean_lbl = formula(r"\bar{x}", r"=", r"32.8", size=MATH).next_to(mean_dot, DOWN, buff=0.15)
        seg = Line([X(0), yb, 0], [X(MEAN), yb, 0], color=INK, stroke_width=5)
        seg2 = seg.copy()
        dbl_dot = mean_dot.copy().move_to([X(2 * MEAN), yb, 0])
        dbl_lbl = formula(r"2\bar{x}", r"\approx", r"66", size=MATH).next_to(dbl_dot, DOWN, buff=0.15)
        with self.narrate("Start with the obvious idea. Serial numbers spread evenly, so their average "
                          "should sit near the middle. These five average thirty two point eight. "
                          "Double it, and you get about sixty six tanks.") as beat:
            beat.wait_until("average", offset=-0.2)
            ghosts = VGroup(*[c[0].copy() for c in caps])
            self.play(LaggedStart(*[g.animate.move_to([X(MEAN), yb + 0.21, 0]).set_opacity(0.6) for g in ghosts],
                                  lag_ratio=0.1), run_time=beat.until("thirty two", offset=-0.2))
            self.play(ReplacementTransform(ghosts, mean_dot), Write(mean_lbl), run_time=1.0)
            beat.wait_until("Double", offset=-0.25)
            self.play(Create(seg), run_time=0.6)
            self.play(seg2.animate.shift(RIGHT * (X(MEAN) - X(0))), run_time=1.0)
            self.play(FadeIn(dbl_dot), Write(dbl_lbl), run_time=beat.remaining(0.8))

        # ============================================================ 4 fail 1
        band = Rectangle(width=X(M) - X(2 * MEAN), height=0.32, stroke_width=0, fill_color=RED,
                         fill_opacity=0.45).move_to([(X(M) + X(2 * MEAN)) / 2, yb, 0])
        imp = label("impossible", size=LABEL, color=RED).next_to(band, DOWN, buff=0.2)
        with self.narrate("But you are holding tank eighty nine. Doubling the average just guessed "
                          "fewer tanks than you have already seen.") as beat:
            self.play(Indicate(caps[4], color=BLUE, scale_factor=1.2), run_time=beat.until("Doubling", offset=-0.2))
            self.play(GrowFromEdge(band, LEFT), run_time=1.2)
            self.play(FadeIn(imp, shift=0.1 * DOWN), run_time=0.6)

        # ============================================================ 5 naive 2: maximum likelihood
        y1 = 2.45
        lik_ax = axes((0, 120), (0, 1), x_length=NL_LEN, y_length=2.7, x_ticks=[0, 30, 60, 90, 120],
                      y_ticks=[0, 1], x_label="factory size N", y_label="likelihood (relative)")
        lik_ax.shift([X(0) - lik_ax.c2p(0, 0)[0], -2.55 - lik_ax.c2p(0, 0)[1], 0])
        naive_bits = VGroup(mean_dot, mean_lbl, seg, seg2, dbl_dot, dbl_lbl, band, imp)
        zero_line = Line(lik_ax.c2p(K, 0), lik_ax.c2p(M - 1, 0), color=RED, stroke_width=7)
        zero_lbl = label("zero: impossible", size=LABEL, color=RED).next_to(zero_line, UP, buff=0.2)
        Ns = np.arange(M, 121)
        L = np.array([comb(M, K) / comb(int(n), K) for n in Ns])
        lik_dots = VGroup(*[Dot(lik_ax.c2p(n, l), radius=0.055, color=INK) for n, l in zip(Ns, L)])
        peak = Dot(lik_ax.c2p(M, 1), radius=0.09, color=BLUE)
        with self.narrate("Second try. Ask which factory size makes these five numbers most probable. "
                          "Any size below eighty nine is impossible, so its likelihood is zero. Above "
                          "that, every extra tank makes your five a little less likely. So the "
                          "likelihood peaks exactly at the largest serial you hold. That is the "
                          "maximum likelihood estimate, eighty nine.") as beat:
            self.play(FadeOut(naive_bits), run_time=0.6)
            grp = VGroup(nl, caps, n_q)
            self.play(grp.animate.shift(UP * (y1 - y0)), run_time=1.0)
            self.play(Create(lik_ax), run_time=beat.until("Any", offset=-0.2))
            self.play(Create(zero_line), run_time=beat.until("zero", offset=-0.3))
            self.play(FadeIn(zero_lbl), run_time=0.6)
            beat.wait_until("Above", offset=-0.1)
            self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in lik_dots], lag_ratio=0.08),
                      run_time=beat.until("So the", offset=-0.1))
            drop = DashedLine(caps[4][0].get_bottom(), peak.get_center(), color=BLUE, stroke_width=3,
                              dash_length=0.1)
            self.play(Create(drop), run_time=beat.until("peaks", offset=-0.1))
            self.play(FadeIn(peak, scale=1.6), run_time=0.6)
            mle = formula(r"\hat{N}_{\text{MLE}}", r"=", r"89", size=MATH, color=BLUE)
            mle.next_to(peak, RIGHT, buff=0.35).shift(DOWN * 0.15)
            beat.wait_until("maximum", offset=-0.2)
            self.play(Write(mle), run_time=1.0)

        # ============================================================ 6 fail 2: simulate
        lik_grp = VGroup(lik_ax, zero_line, zero_lbl, lik_dots, peak, drop, mle)
        rows_y = [0.25, -1.05, -2.35]
        bases = VGroup(*[Line([HXp(H_LO), y, 0], [HXp(H_HI), y, 0], color=GRAY, stroke_width=2)
                         for y in rows_y])
        hnums = VGroup(*[MathTex(str(v), font_size=MATH_SMALL, color=GRAY).move_to([HXp(v), rows_y[2] - 0.32, 0])
                         for v in (20, 60, 140, 180)])
        hname = label("estimate of N", size=SMALL + 2, color=GRAY).next_to(hnums[-1], LEFT, buff=0.35)
        truth = DashedLine([HXp(TRUE_N), rows_y[2], 0], [HXp(TRUE_N), rows_y[0] + 1.15, 0], color=GREEN,
                           stroke_width=3, dash_length=0.12)
        truth_lbl = formula(r"N = 100", size=MATH_SMALL + 6, color=GREEN).next_to(truth, DOWN, buff=0.12)
        rlabels = VGroup(formula(r"2\bar{x}", size=MATH), formula(r"m", size=MATH, color=BLUE),
                         formula(r"m+\tfrac{m-k}{k}", size=MATH, color=YELLOW))
        for lbl, y in zip(rlabels, rows_y):
            lbl.move_to([-5.2, y + 0.35, 0])

        n_t = ValueTracker(0)
        HMAX = 0.95

        def make_bars(cum, color, norm, under=None):
            bw = HXp(H_LO + BIN) - HXp(H_LO)
            bars = VGroup(*[Rectangle(width=bw * 0.86, height=0.001, stroke_width=0, fill_color=color,
                                      fill_opacity=0.9) for _ in range(NB)])
            bars.cum, bars.norm, bars.under = cum, norm, under

            def upd(g):
                j = int(round(n_t.get_value() / (R / CHECK)))
                for b, h0, x in zip(g, g.cum[j], range(NB)):
                    base = 0.0 if g.under is None else g.under.cum[j][x] / g.under.norm * HMAX
                    h = max(h0 / g.norm * HMAX, 0.001)
                    b.stretch_to_fit_height(h)
                    b.move_to([HXp(EDGES[x] + BIN / 2 - 0.5), g.y + base + h / 2, 0])
            bars.upd = upd
            return bars

        cD, cDimp, cM, cG = cum_hist(E_DOUBLE), cum_hist(E_DOUBLE, IMPOSSIBLE), cum_hist(E_MAX), cum_hist(E_GAP)
        nD, nM, nG = cD[-1].max(), cM[-1].max(), cG[-1].max()
        barsD_imp = make_bars(cDimp, RED, nD)
        barsD_ok = make_bars(cD - cDimp, GRAY, nD, under=barsD_imp)
        barsM = make_bars(cM, BLUE, nM)
        barsG = make_bars(cG, YELLOW, nG)
        for b, y in ((barsD_imp, rows_y[0]), (barsD_ok, rows_y[0]), (barsM, rows_y[1]), (barsG, rows_y[2])):
            b.y = y
            b.upd(b)

        counter = live_number(n_t, 0, size=MATH, prefix=r"\text{captures}=", color=INK)
        counter.number.group_with_commas = True
        counter.move_to([-3.3, 1.7, 0])
        pct = label("19%", size=LABEL, color=RED)
        short = Arrow([HXp(E_MAX.mean()), rows_y[1] + 1.05, 0], [HXp(TRUE_N), rows_y[1] + 1.05, 0], buff=0,
                      color=RED, stroke_width=4, max_tip_length_to_length_ratio=0.25)
        short_lbl = formula(r"84", r"\;\;-16", size=MATH_SMALL + 6, color=RED)
        short_lbl[0].set_color(BLUE)
        short_lbl.next_to(short, LEFT, buff=0.15)

        with self.narrate("Test both on a pretend factory of one hundred tanks. Capture five at random, "
                          "ten thousand times. Doubling the average centers near a hundred, but this "
                          "red slice, about one capture in five, lands below a serial already in hand. "
                          "The largest serial never overshoots, and that is its flaw. It averages "
                          "eighty four, sixteen tanks short.") as beat:
            self.play(FadeOut(lik_grp), nl.animate.set_opacity(0.3), caps.animate.set_opacity(0.3),
                      FadeOut(n_q), run_time=0.8)
            self.play(Create(bases), FadeIn(hnums), FadeIn(hname), Create(truth), FadeIn(truth_lbl),
                      FadeIn(rlabels[:2]), run_time=beat.until("Capture", offset=-0.1))
            for b in (barsD_imp, barsD_ok, barsM):
                b.add_updater(b.upd)
            self.add(barsD_imp, barsD_ok, barsM, counter)
            self.play(n_t.animate.set_value(R), run_time=beat.until("Doubling", offset=-0.1),
                      rate_func=rate_functions.ease_in_quad)
            for b in (barsD_imp, barsD_ok, barsM):
                b.clear_updaters()
            beat.wait_until("red slice", offset=-0.2)
            pct.next_to(barsD_imp, RIGHT, buff=0.2).align_to(barsD_imp, DOWN).shift(UP * 0.05)
            pct.move_to([HXp(40), rows_y[0] + 0.55, 0])
            self.play(flag(barsD_imp, color=RED), FadeIn(pct), run_time=1.0)
            beat.wait_until("largest", offset=-0.2)
            self.play(Indicate(barsM, color=BLUE, scale_factor=1.04), Indicate(truth, color=GREEN),
                      run_time=1.0)
            beat.wait_until("averages", offset=-0.2)
            self.play(GrowArrow(short), FadeIn(short_lbl), run_time=beat.remaining(0.8))

        # ============================================================ 7 prediction pause
        sim_grp = VGroup(bases, hnums, hname, truth, truth_lbl, rlabels[:2], barsD_imp, barsD_ok,
                         barsM, counter, pct, short, short_lbl)
        above = Rectangle(width=X(120) - X(M), height=0.42, stroke_width=0, fill_color=YELLOW,
                          fill_opacity=0.18).move_to([(X(M) + X(120)) / 2, y1 + 0.21, 0])
        qmark = MathTex("?", font_size=EQ, color=YELLOW).move_to(above).shift(RIGHT * 0.2)
        with self.narrate("The tanks above it are never seen, so it can only undercount. How far past "
                          "eighty nine should you reach? [pause 1.5]") as beat:
            self.play(FadeOut(sim_grp), nl.animate.set_opacity(1), caps.animate.set_opacity(1),
                      run_time=beat.until("never", offset=-0.2))
            self.play(FadeIn(above), FadeIn(qmark), run_time=0.8)

        # ============================================================ 8 the gaps
        gap_segs = VGroup(*[Line([X(a - 0.5), y1, 0], [X(b + 0.5), y1, 0], color=YELLOW, stroke_width=9)
                            for a, b in GAPS])
        ys = 1.05
        stack = VGroup()
        acc = 0
        for a, b in GAPS:
            n = b - a + 1
            stack.add(Line([X(acc), ys, 0], [X(acc + n), ys, 0], color=YELLOW, stroke_width=14))
            acc += n
        stack_lbl = formula(r"84", r"\text{ unseen}", size=MATH, color=YELLOW).next_to(stack, RIGHT, buff=0.3)
        divs = VGroup(*[Line([X(GAP * i), ys - 0.22, 0], [X(GAP * i), ys + 0.22, 0], color=BG, stroke_width=6)
                        for i in range(1, K)])
        pieces = VGroup(*[Line([X(GAP * i), ys, 0], [X(GAP * (i + 1)), ys, 0], color=YELLOW, stroke_width=14)
                          for i in range(K)])
        split_lbl = formula(r"\div 5", size=MATH, color=INK).next_to(stack_lbl, RIGHT, buff=0.3)
        piece_lbl = formula(r"16.8", size=MATH, color=YELLOW).next_to(pieces[0], DOWN, buff=0.25)
        with self.narrate("Look at the gaps. Five captures cut the line into stretches of tanks nobody "
                          "saw. Below eighty nine, those stretches hold eighty four unseen tanks, shared "
                          "across five gaps. That is about seventeen per gap.") as beat:
            self.play(FadeOut(qmark), above.animate.set_fill(opacity=0.1), run_time=0.5)
            beat.wait_until("cut", offset=-0.2)
            self.play(LaggedStart(*[Create(g) for g in gap_segs], lag_ratio=0.25),
                      run_time=beat.until("Below", offset=-0.1))
            self.play(LaggedStart(*[TransformFromCopy(g, s) for g, s in zip(gap_segs, stack)], lag_ratio=0.15),
                      run_time=beat.until("eighty four", offset=-0.1))
            self.play(Write(stack_lbl), run_time=0.8)
            beat.wait_until("five gaps", offset=-0.2)
            self.remove(stack)
            self.add(pieces, divs)
            self.play(LaggedStart(*[p.animate.shift(RIGHT * 0.12 * i) for i, p in enumerate(pieces)], lag_ratio=0.1),
                      FadeIn(split_lbl), run_time=1.0)
            beat.wait_until("seventeen", offset=-0.25)
            self.play(VGroup(*pieces[1:]).animate.set_opacity(0.3), Write(piece_lbl), run_time=0.8)

        # ============================================================ 9 one more gap on top
        top_gap = Line([X(M + 0.5), y1, 0], [X(EST + 0.5), y1, 0], color=YELLOW, stroke_width=9)
        est_tick = Line([X(EST), y1, 0], [X(EST), y1 + 0.42, 0], color=YELLOW, stroke_width=6)
        est_lbl = formula(r"\approx 106", size=MATH, color=YELLOW).next_to(est_tick, UP, buff=0.12)
        with self.narrate("Nothing makes the stretch above eighty nine any different, so add one more "
                          "average gap on top. Eighty nine plus seventeen is about a hundred and six.") as beat:
            self.play(Indicate(above, color=YELLOW, scale_factor=1.0), run_time=beat.until("add", offset=-0.2))
            self.play(TransformFromCopy(pieces[0], top_gap), FadeOut(above), run_time=1.4)
            beat.wait_until("about", offset=-0.2)
            self.play(Create(est_tick), Write(est_lbl), run_time=0.9)

        # ============================================================ 10 formula from the picture
        f1 = formula(r"\hat{N}", "=", "89", "+", r"\frac{84}{5}", size=EQ)
        f2 = formula(r"\hat{N}", "=", "m", "+", r"\frac{m-k}{k}", size=EQ)
        f3 = formula(r"\hat{N}", "=", "m", r"\left(1+\frac{1}{k}\right)", "-1", size=EQ)
        for f in (f1, f2, f3):
            f.move_to([0, -1.35, 0])
            f[2].set_color(BLUE)
        f1[4].set_color(YELLOW)
        f2[4].set_color(YELLOW)
        lbl_m = formula(r"m", size=MATH, color=BLUE)
        lbl_k = formula(r"k = 5", size=MATH, color=INK)
        with self.narrate("In symbols, m is the largest serial and k is the number captured. The estimate "
                          "is m, plus the average gap, m minus k over k. That tidies up to m times one "
                          "plus one over k, minus one.") as beat:
            self.play(Write(f1[0:2]), TransformFromCopy(caps[4][1], f1[2]), run_time=1.0)
            self.play(FadeIn(f1[3]), TransformFromCopy(VGroup(stack_lbl[0], split_lbl), f1[4]), run_time=1.2)
            beat.wait_until("m", offset=-0.15)
            lbl_m.next_to(caps[4][1], RIGHT, buff=0.12)
            self.play(FadeIn(lbl_m, shift=0.1 * LEFT), run_time=0.5)
            beat.wait_until("k", offset=-0.15)
            lbl_k.next_to(split_lbl, DOWN, buff=0.25)
            self.play(FadeIn(lbl_k, shift=0.1 * UP), run_time=0.5)
            beat.wait_until("estimate", offset=-0.2)
            # numbers -> symbols, term by term
            self.play(*[ReplacementTransform(a, b) for a, b in zip(f1, f2)],
                      run_time=beat.until("tidies", offset=-0.2))
            self.play(TransformMatchingTex(f2, f3), run_time=1.5)
            self.play(Circumscribe(f3, color=YELLOW, buff=0.15), run_time=beat.remaining(0.8))

        # ============================================================ 11 measured win
        insight_bits = VGroup(pieces, divs, piece_lbl, stack_lbl, split_lbl, lbl_m, lbl_k)
        with self.narrate("On the same ten thousand captures, it centers on one hundred, with about a "
                          "third less spread than doubling the average.") as beat:
            self.play(FadeOut(insight_bits), ReplacementTransform(f3, rlabels[2]),
                      nl.animate.set_opacity(0.3), caps.animate.set_opacity(0.3),
                      gap_segs.animate.set_opacity(0.3), top_gap.animate.set_opacity(0.3),
                      est_tick.animate.set_opacity(0.3), est_lbl.animate.set_opacity(0.3), run_time=1.0)
            n_t.set_value(R)
            for b in (barsD_imp, barsD_ok, barsM):
                b.upd(b)
            n_t.set_value(0)
            barsG.upd(barsG)
            back = VGroup(bases, hnums, hname, truth, truth_lbl, rlabels[:2], barsD_imp, barsD_ok, barsM)
            self.play(FadeIn(back), run_time=0.8)
            barsG.add_updater(barsG.upd)
            self.add(barsG)
            self.play(n_t.animate.set_value(R), run_time=beat.until("centers", offset=-0.1),
                      rate_func=rate_functions.ease_in_quad)
            barsG.clear_updaters()
            self.play(Indicate(truth, color=GREEN), run_time=beat.until("third", offset=-0.2))
            sdD, sdG = E_DOUBLE.std(), E_GAP.std()
            brD = Line([HXp(E_DOUBLE.mean() - sdD), rows_y[0] - 0.22, 0],
                       [HXp(E_DOUBLE.mean() + sdD), rows_y[0] - 0.22, 0], color=INK, stroke_width=4)
            brG = Line([HXp(E_GAP.mean() - sdG), rows_y[2] - 0.22, 0],
                       [HXp(E_GAP.mean() + sdG), rows_y[2] - 0.22, 0], color=INK, stroke_width=4)
            sdD_l = formula(r"\pm 25", size=MATH_SMALL + 6).next_to(brD, RIGHT, buff=0.2)
            sdG_l = formula(r"\pm 17", size=MATH_SMALL + 6).next_to(brG, RIGHT, buff=0.2).shift(UP * 0.12)
            self.play(Create(brD), FadeIn(sdD_l), run_time=0.7)
            self.play(TransformFromCopy(brD, brG), FadeIn(sdG_l), run_time=beat.remaining(0.8))

        # ============================================================ 12 payoff (real data)
        self.fade_out_all(run_time=0.6)
        sc = 7.0 / 1600
        bx = -1.9
        rows = [("intelligence estimate", 1550, PURPLE), ("serial numbers", 327, YELLOW),
                ("German records", 342, GREEN)]
        head = label("August 1942 · German tanks per month", size=LABEL + 4, color=INK)
        head.move_to([0, 2.85, 0])
        bars, names, vals = VGroup(), VGroup(), VGroup()
        for i, (name, v, col) in enumerate(rows):
            y = 1.75 - 0.95 * i
            r = Rectangle(width=v * sc, height=0.55, stroke_width=0, fill_color=col, fill_opacity=0.9)
            r.move_to([bx, y, 0], aligned_edge=LEFT)
            bars.add(r)
            names.add(label(name, size=LABEL, color=col).next_to([bx, y, 0], LEFT, buff=0.3))
            vals.add(formula(f"{v:,}".replace(",", "{,}"), size=MATH, color=col).next_to(r, RIGHT, buff=0.2))
        cite = citation("Ruggles & Brodie, 1947 · Journal of the American Statistical Association")
        with self.narrate("Allied economists ran this kind of serial number analysis on captured "
                          "gearboxes. For August nineteen forty two, it gave three hundred and twenty "
                          "seven tanks a month. German records, found after the war, said three hundred "
                          "and forty two.") as beat:
            self.play(FadeIn(head), FadeIn(cite), FadeIn(names[0]), GrowFromEdge(bars[0], LEFT),
                      FadeIn(vals[0]), run_time=beat.until("August", offset=-0.2))
            beat.wait_until("three hundred", offset=-0.2)
            self.play(FadeIn(names[1]), GrowFromEdge(bars[1], LEFT), run_time=0.8)
            self.play(FadeIn(vals[1]), run_time=0.4)
            beat.wait_until("three hundred", occurrence=2, offset=-0.2)
            self.play(FadeIn(names[2]), GrowFromEdge(bars[2], LEFT), run_time=0.8)
            self.play(FadeIn(vals[2]), run_time=beat.remaining(0.4))

        # ============================================================ 13 other months
        def month_row(name, est, rec, pct_txt):
            t = label(name, size=LABEL, color=INK)
            e = formula(str(est), size=MATH, color=YELLOW)
            vs = label("vs", size=LABEL - 2, color=GRAY)
            r = formula(str(rec), size=MATH, color=GREEN)
            p = formula(pct_txt, size=MATH, color=RED if pct_txt.startswith("+") else GRAY)
            g = VGroup(t, e, vs, r, p).arrange(RIGHT, buff=0.3)
            return g
        m41 = month_row("June 1941", 244, 271, r"-10\%")
        m40 = month_row("June 1940", 169, 122, r"+39\%")
        months = VGroup(m41, m40).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to([0.6, -1.7, 0])
        with self.narrate("Other months missed by more, by up to forty percent, but never by a factor "
                          "of four.") as beat:
            self.play(LaggedStart(FadeIn(m41, shift=0.2 * UP), FadeIn(m40, shift=0.2 * UP), lag_ratio=0.4),
                      run_time=beat.until("forty", offset=-0.1))
            self.play(flag(m40[4], color=RED), run_time=0.8)
            beat.wait_until("four", offset=-0.3)
            self.play(Indicate(bars[0], color=PURPLE, scale_factor=1.03), run_time=beat.remaining(0.8))

        # ============================================================ 14 limits: unbroken sequence
        self.fade_out_all(run_time=0.6)
        nl.set_opacity(1)
        caps.set_opacity(1)
        for m in (gap_segs, top_gap, est_tick, est_lbl):
            m.set_opacity(1)
        line_grp = VGroup(nl, caps, gap_segs, top_gap, est_tick, est_lbl)
        line_grp.shift(DOWN * (y1 - 1.3))
        yc = -1.6
        blocks = [(0, 30), (52, 70), (95, 120)]
        chassis = VGroup(*[Line([X(a), yc, 0], [X(b), yc, 0], color=GRAY, stroke_width=3) for a, b in blocks])
        ch_ticks = VGroup(*[Line([X(s), yc, 0], [X(s), yc + 0.42, 0], color=BLUE, stroke_width=6)
                            for s in (6, 19, 57, 66, 101)])
        ch_name = label("chassis serial number", size=SMALL + 2, color=GRAY).next_to(chassis, DOWN, buff=0.25)
        ch_name.align_to(chassis, RIGHT)
        with self.narrate("And it only works when numbers run in one unbroken sequence, as the gearbox "
                          "numbers did. Chassis numbers came in separate blocks, and those were much "
                          "harder to use.") as beat:
            self.play(FadeIn(line_grp), run_time=beat.until("unbroken", offset=-0.2))
            self.play(Indicate(nl[0], color=INK, scale_factor=1.0), run_time=1.0)
            beat.wait_until("Chassis", offset=-0.2)
            self.play(LaggedStart(*[Create(c) for c in chassis], lag_ratio=0.3), FadeIn(ch_name),
                      run_time=beat.until("blocks", offset=0.2))
            self.play(LaggedStart(*[FadeIn(t, shift=0.3 * DOWN) for t in ch_ticks], lag_ratio=0.15),
                      run_time=beat.remaining(0.8))

        # ============================================================ 15 landing
        y2 = 1.3
        true_tick = Line([X(TRUE_N), y2, 0], [X(TRUE_N), y2 - 0.5, 0], color=GREEN, stroke_width=6)
        nl_nums = nl[2]
        true_lbl = formula(r"N = 100", size=MATH, color=GREEN).move_to([X(TRUE_N), y2 - 1.05, 0])
        most = label("most likely", size=LABEL, color=BLUE)
        with self.narrate("Back to your five tanks. This simulated factory built exactly one hundred. If "
                          "you guessed near ninety, you picked the most likely answer, and it was still "
                          "too small. The missing tanks were hiding in the gaps.") as beat:
            self.play(FadeOut(chassis), FadeOut(ch_ticks), FadeOut(ch_name),
                      line_grp.animate.shift(DOWN * 0.6), run_time=beat.until("simulated", offset=-0.2))
            true_tick.shift(DOWN * 0.6)
            true_lbl.shift(DOWN * 0.6)
            self.play(FadeOut(nl_nums), FadeOut(nl[3]), run_time=0.4)
            self.play(Create(true_tick), Write(true_lbl), run_time=beat.until("If", offset=-0.2))
            most.move_to([X(M) - 1.6, true_lbl.get_y(), 0])
            self.play(Indicate(caps[4], color=BLUE, scale_factor=1.2), FadeIn(most),
                      run_time=beat.until("too small", offset=-0.1))
            short2 = Arrow([X(M), true_lbl.get_y() + 0.45, 0], [X(TRUE_N), true_lbl.get_y() + 0.45, 0],
                           buff=0, color=RED, stroke_width=4, max_tip_length_to_length_ratio=0.3)
            self.play(GrowArrow(short2), run_time=0.6)
            beat.wait_until("hiding", offset=-0.3)
            self.play(LaggedStart(*[g.animate.set_stroke(width=16) for g in [*gap_segs, top_gap]], lag_ratio=0.12),
                      run_time=beat.remaining(0.8))

        self.end_card()
