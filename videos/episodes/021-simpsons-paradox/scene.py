"""Episode 21 - When Every Part Says Yes but the Whole Says No (Simpson's paradox, Berkeley 1973).

    videos/toolkit/render.sh --preview videos/episodes/021-simpsons-paradox/scene.py Episode /tmp/ep21.mp4
"""
from manim import *
from sample_space import *

# ---------------------------------------------------------------- real data (no simulation)
# Berkeley graduate admissions, fall 1973, six largest departments (R: UCBAdmissions;
# Bickel, Hammel & O'Connell 1975, Science 187:398).  (applicants, admitted)
DEPTS = "ABCDEF"
M_N = [825, 560, 325, 417, 191, 373]
M_A = [512, 353, 120, 138, 53, 22]
W_N = [108, 25, 593, 375, 393, 341]
W_A = [89, 17, 202, 131, 94, 24]
M_R = [a / n for a, n in zip(M_A, M_N)]
W_R = [a / n for a, n in zip(W_A, W_N)]
M_TOT = sum(M_A) / sum(M_N)          # 0.445
W_TOT = sum(W_A) / sum(W_N)          # 0.304
SWAP = sum(n / sum(M_N) * r for n, r in zip(M_N, W_R))   # 0.516

MEN, WOMEN, MIX, VERDICT = BLUE, PURPLE, YELLOW, RED


def pct(v, size=MATH_SMALL, color=INK):
    return MathTex(f"{round(100 * v)}", font_size=size, color=color)


def morph(src, dst, pairs, run_time=1.5):
    """Equation algebra: matched parts glide to their new place, the rest cross-fades."""
    anims, used_s, used_d = [], set(), set()
    for a, b in pairs:
        pa = src.get_part_by_tex(a) if isinstance(a, str) else a
        pb = dst.get_part_by_tex(b) if isinstance(b, str) else b
        anims.append(ReplacementTransform(pa, pb))
        used_s |= {id(x) for x in pa.get_family()}
        used_d |= {id(x) for x in pb.get_family()}
    rest_s = [m for m in src.family_members_with_points() if id(m) not in used_s]
    rest_d = [m for m in dst.family_members_with_points() if id(m) not in used_d]
    if rest_s or rest_d:
        anims.append(FadeTransform(VGroup(*rest_s), VGroup(*rest_d)))
    return AnimationGroup(*anims, run_time=run_time)


class Episode(NarratedScene):
    EPISODE = 21
    TITLE = "When Every Part Says Yes but the Whole Says No"
    PRONUNCIATIONS = {"Bickel": "bick ul", "Hammel": "ham ul"}

    # ------------------------------------------------------------------ cold-open bars
    def cold_bars(self):
        base, h = -1.75, 6.0
        g = VGroup()
        for i, (v, col, name, n) in enumerate([(0.44, MEN, "men", "8,442"),
                                                (0.35, WOMEN, "women", "4,321")]):
            x = -5.0 + 1.45 * i
            bar = Rectangle(width=0.95, height=v * h, stroke_width=0, fill_color=col,
                            fill_opacity=0.9).move_to([x, base, 0], aligned_edge=DOWN)
            val = MathTex(f"{round(100 * v)}\\%", font_size=MATH, color=col).next_to(bar, UP, buff=0.15)
            nm = label(name, color=col).next_to([x, base, 0], DOWN, buff=0.22)
            cnt = MathTex(n.replace(",", "{,}"), font_size=MATH_SMALL, color=GRAY).next_to(nm, DOWN, buff=0.12)
            g.add(VGroup(bar, val, nm, cnt))
        g.base = base
        return g

    def construct(self):
        # ============================================================ 1. cold open
        head = label("UC Berkeley graduate admissions, fall 1973", size=26, color=GRAY)
        head.to_corner(UL, buff=0).shift(RIGHT * 0.35 + DOWN * 0.45)
        head.align_to([-6.3, 0, 0], LEFT)
        bars = self.cold_bars()
        men_bar, women_bar = bars
        with self.narrate("Berkeley, fall nineteen seventy three. Forty four percent of the "
                          "men who applied to graduate school got in. Thirty five percent of "
                          "the women did.") as beat:
            self.play(FadeIn(head, shift=0.1 * DOWN), run_time=0.6)
            self.play(FadeIn(men_bar[2]), FadeIn(women_bar[2]), FadeIn(men_bar[3]),
                      FadeIn(women_bar[3]), run_time=beat.until("Forty", offset=-0.3))
            self.play(GrowFromEdge(men_bar[0], DOWN), FadeIn(men_bar[1], shift=0.2 * UP),
                      run_time=1.0)
            beat.wait_until("Thirty", offset=-0.2)
            self.play(GrowFromEdge(women_bar[0], DOWN), FadeIn(women_bar[1], shift=0.2 * UP),
                      run_time=1.0)

        # department chart scaffolding
        base, hs = -1.75, 4.0
        xs = [-0.55 + 1.0 * i for i in range(6)]
        xpool = 5.75
        letters = VGroup(*[text(d, size=30, color=INK).move_to([x, base - 0.35, 0])
                           for d, x in zip(DEPTS, xs)])
        baseline = Line([xs[0] - 0.45, base, 0], [xs[-1] + 0.45, base, 0], color=GRAY,
                        stroke_width=2)
        qmarks = VGroup(*[MathTex("?", font_size=MATH, color=MIX).move_to([x, base + 0.5, 0])
                          for x in xs])
        tally = MathTex(r"\text{men higher in }", "?", r"\text{ of 6}", font_size=MATH)
        tally[1].set_color(MIX)
        tally.move_to([2.4, 2.75, 0])
        sub = label("% admitted, six largest departments", size=22, color=GRAY)
        sub.next_to(tally, DOWN, buff=0.22)
        with self.narrate("Now split out the six largest departments. In how many of the six "
                          "did men get in at the higher rate? [pause 1.5]") as beat:
            self.play(Create(baseline), LaggedStart(*[FadeIn(l, shift=0.15 * UP) for l in letters],
                                                    lag_ratio=0.12),
                      run_time=beat.until("In how", offset=-0.2))
            self.play(Write(tally), FadeIn(sub), run_time=1.2)
            self.play(LaggedStart(*[FadeIn(q, scale=0.8) for q in qmarks], lag_ratio=0.15),
                      run_time=1.4)
            # planned prediction pause: the question marks breathe in turn (cue to answer)
            self.play(LaggedStart(*[Indicate(q, color=MIX, scale_factor=1.15) for q in qmarks],
                                  lag_ratio=0.25), run_time=beat.remaining())

        # ============================================================ 2. naive verdict
        top_m = men_bar[0].get_top()[1]
        top_w = women_bar[0].get_top()[1]
        gx = women_bar[0].get_right()[0] + 0.3
        gap = BraceBetweenPoints([gx, top_m, 0], [gx, top_w, 0], direction=RIGHT, color=VERDICT)
        gap_lbl = MathTex(r"9\text{ points}", font_size=MATH, color=VERDICT).next_to(gap, RIGHT, buff=0.12)
        se_lbl = MathTex(r"\approx 10\text{ SE}", font_size=MATH_SMALL + 4, color=VERDICT)
        se_lbl.next_to(gap_lbl, DOWN, buff=0.18).align_to(gap_lbl, LEFT)
        ref = DashedLine([men_bar[0].get_left()[0], top_m, 0], [gx, top_m, 0], color=GRAY,
                         stroke_width=2, dash_length=0.08)
        verdict = label("bias against women?", size=LABEL, color=VERDICT)
        verdict.next_to(head, DOWN, buff=0.35).align_to(head, LEFT)
        with self.narrate("The obvious reading is bias against women. With twelve thousand seven "
                          "hundred applicants, a nine point gap is about ten standard errors "
                          "wide. Luck doesn't do that.") as beat:
            self.play(FadeIn(verdict, shift=0.1 * DOWN), run_time=beat.until("With", offset=-0.1))
            self.play(Create(ref), run_time=beat.until("nine", offset=-0.5))
            self.play(GrowFromCenter(gap), FadeIn(gap_lbl, shift=0.1 * LEFT), run_time=0.8)
            beat.wait_until("ten", offset=-0.2)
            self.play(FadeIn(se_lbl, shift=0.1 * UP), run_time=0.7)
            self.play(Indicate(verdict, color=VERDICT, scale_factor=1.06),
                      run_time=min(1.0, beat.remaining()))

        # ============================================================ 3. the reveal
        mbars, wbars, mlbl, wlbl = VGroup(), VGroup(), VGroup(), VGroup()
        for x, rm, rw in zip(xs, M_R, W_R):
            bm = Rectangle(width=0.36, height=rm * hs, stroke_width=0, fill_color=MEN,
                           fill_opacity=0.9).move_to([x - 0.2, base, 0], aligned_edge=DOWN)
            bw = Rectangle(width=0.36, height=rw * hs, stroke_width=0, fill_color=WOMEN,
                           fill_opacity=0.9).move_to([x + 0.2, base, 0], aligned_edge=DOWN)
            mbars.add(bm)
            wbars.add(bw)
            mlbl.add(pct(rm, 26, MEN).next_to(bm, UP, buff=0.1))
            wlbl.add(pct(rw, 26, WOMEN).next_to(bw, UP, buff=0.1))
        # lift a label pair apart if they would touch (A: 62 vs 82 fine; small gaps elsewhere)
        for a, b in zip(mlbl, wlbl):
            if abs(a.get_center()[1] - b.get_center()[1]) < 0.3:
                hi, lo = (a, b) if a.get_center()[1] >= b.get_center()[1] else (b, a)
                hi.shift(UP * (0.32 - (hi.get_center()[1] - lo.get_center()[1])))
        two = MathTex("2", font_size=MATH, color=MIX).move_to(tally[1])
        with self.narrate("Here are the six. Department A admitted eighty two percent of its "
                          "women and sixty two percent of its men. Women had the higher rate in "
                          "four departments. Men led in only two, C and E, by three and four "
                          "points.") as beat:
            self.play(FadeOut(qmarks), dim(verdict, opacity=0.35),
                      LaggedStart(*[AnimationGroup(GrowFromEdge(m, DOWN), GrowFromEdge(w, DOWN))
                                    for m, w in zip(mbars, wbars)], lag_ratio=0.15),
                      run_time=beat.until("Department", offset=-0.1))
            self.play(FadeIn(wlbl[0], shift=0.1 * UP), Indicate(wbars[0], color=WOMEN),
                      run_time=beat.until("sixty", offset=-0.1))
            self.play(FadeIn(mlbl[0], shift=0.1 * UP), Indicate(mbars[0], color=MEN),
                      run_time=beat.until("Women had", offset=-0.1))
            self.play(LaggedStart(*[FadeIn(VGroup(mlbl[i], wlbl[i]), shift=0.1 * UP)
                                    for i in range(1, 6)], lag_ratio=0.2),
                      run_time=beat.until("Men led", offset=-0.1))
            ce = VGroup(box(VGroup(mbars[2], wbars[2], mlbl[2], wlbl[2], letters[2]), buff=0.1),
                        box(VGroup(mbars[4], wbars[4], mlbl[4], wlbl[4], letters[4]), buff=0.1))
            self.play(Transform(tally[1], two), run_time=beat.until("C and", offset=-0.15))
            self.play(Create(ce[0]), run_time=0.5)
            self.play(Create(ce[1]), run_time=0.5)
            self.hold(max(0, beat.remaining() - 0.6))
            self.play(FadeOut(ce), run_time=0.5)

        # ============================================================ 4. the fail: pool them
        sep = DashedLine([xpool - 0.72, base, 0], [xpool - 0.72, base + 2.6, 0], color=DIM,
                         stroke_width=2, dash_length=0.1)
        pm = Rectangle(width=0.36, height=M_TOT * hs, stroke_width=0, fill_color=MEN,
                       fill_opacity=0.9).move_to([xpool - 0.2, base, 0], aligned_edge=DOWN)
        pw = Rectangle(width=0.36, height=W_TOT * hs, stroke_width=0, fill_color=WOMEN,
                       fill_opacity=0.9).move_to([xpool + 0.2, base, 0], aligned_edge=DOWN)
        pml = pct(M_TOT, 26, MEN).next_to(pm, UP, buff=0.1)
        pwl = pct(W_TOT, 26, WOMEN).next_to(pw, UP, buff=0.1)
        pbase = Line([xpool - 0.45, base, 0], [xpool + 0.45, base, 0], color=GRAY, stroke_width=2)
        plab = label("all six", size=24, color=INK).move_to([xpool, base - 0.35, 0])
        with self.narrate("Now pool these same six back together, and the gap gets wider: "
                          "forty five percent of men, thirty percent of women. Same decisions, "
                          "opposite story.") as beat:
            srcs_m = VGroup(*[m.copy() for m in mbars])
            srcs_w = VGroup(*[w.copy() for w in wbars])
            self.play(Create(sep), Create(pbase), FadeIn(plab), run_time=beat.until("forty", offset=-1.0))
            self.play(ReplacementTransform(srcs_m, pm), run_time=1.0)
            self.play(FadeIn(pml, shift=0.1 * UP), run_time=0.4)
            beat.wait_until("thirty", offset=-0.5)
            self.play(ReplacementTransform(srcs_w, pw), run_time=1.0)
            self.play(FadeIn(pwl, shift=0.1 * UP), run_time=0.4)
            beat.wait_until("Same", offset=-0.1)
            self.play(undim(verdict), Indicate(VGroup(pm, pw, pml, pwl), color=VERDICT,
                                               scale_factor=1.05), run_time=1.0)

        # ============================================================ 5. the picture
        # department chart shrinks into a legend strip; chains of steps take the stage
        chart = VGroup(baseline, letters, mbars, wbars)
        strip_target = chart.copy().scale(0.5).move_to([4.85, 2.25, 0])
        ax = axes((0, 2800), (0, 1400), x_ticks=[0, 1000, 2000], y_ticks=[0, 500, 1000],
                  x_length=8.0, y_length=4.0, x_label="applicants", y_label="admitted")
        ax.shift(np.array([-5.55, -2.15, 0]) - ax.c2p(0, 0))
        O = ax.c2p(0, 0)

        def chain(ns, as_, color, width=6):
            pts = [ax.c2p(0, 0)]
            cx = cy = 0
            for n, a in zip(ns, as_):
                cx += n
                cy += a
                pts.append(ax.c2p(cx, cy))
            segs = VGroup(*[Line(p, q, color=color, stroke_width=width) for p, q in zip(pts, pts[1:])])
            joints = VGroup(*[Dot(p, radius=0.045, color=color) for p in pts[1:]])
            segs.pts = pts
            return segs, joints

        mseg, mj = chain(M_N, M_A, MEN)
        wseg, wj = chain(W_N, W_A, WOMEN)

        def seg_label(seg, d, side, color):
            v = seg.get_end() - seg.get_start()
            nrm = np.array([-v[1], v[0], 0]) / max(np.linalg.norm(v), 1e-6)
            return text(d, size=24, color=color).move_to(seg.get_center() + side * 0.28 * nrm)

        mletters = VGroup(*[seg_label(s, d, 1, MEN) for s, d in zip(mseg, DEPTS)])
        wletters = VGroup(*[seg_label(s, d, -1, WOMEN) for s, d in zip(wseg, DEPTS)][2:])

        legend = VGroup(
            VGroup(Line(ORIGIN, RIGHT * 0.5, color=MEN, stroke_width=6), label("men", size=24, color=MEN)).arrange(RIGHT, buff=0.15),
            VGroup(Line(ORIGIN, RIGHT * 0.5, color=WOMEN, stroke_width=6), label("women", size=24, color=WOMEN)).arrange(RIGHT, buff=0.15),
        ).arrange(RIGHT, buff=0.4)

        with self.narrate("To see how, draw each department as a step. It runs right by the "
                          "number who applied and rises by the number admitted, so its slope is "
                          "the admission rate. Here are the men. Their biggest steps are A and "
                          "B, the steep ones.") as beat:
            self.play(FadeOut(VGroup(head, verdict, men_bar, women_bar, gap, gap_lbl, se_lbl, ref,
                                     tally, sub, mlbl, wlbl, sep, pm, pw, pml, pwl, pbase, plab)),
                      Transform(chart, strip_target), run_time=1.0)
            self.play(Create(ax), run_time=beat.until("runs", offset=-0.1))
            # one example step (men, dept A) with its run and rise drawn out
            a0, a1 = mseg.pts[0], mseg.pts[1]
            run_leg = Line(a0, [a1[0], a0[1], 0], color=GRAY, stroke_width=3)
            rise_leg = Line([a1[0], a0[1], 0], a1, color=GRAY, stroke_width=3)
            run_t = MathTex("825", font_size=MATH_SMALL, color=GRAY).next_to(run_leg, UP, buff=0.12)
            rise_t = MathTex("512", font_size=MATH_SMALL, color=GRAY).next_to(rise_leg, RIGHT, buff=0.12)
            self.play(Create(run_leg), FadeIn(run_t), run_time=beat.until("rises", offset=-0.1))
            self.play(Create(rise_leg), FadeIn(rise_t), run_time=beat.until("so its", offset=-0.1))
            self.play(Create(mseg[0]), FadeIn(mj[0]), run_time=beat.until("slope", offset=-0.1))
            rate_t = MathTex(r"\tfrac{512}{825} = 62\%", font_size=MATH_SMALL + 4, color=MEN)
            rate_t.next_to(mseg[0].get_center(), UL, buff=0.25)
            self.play(Indicate(mseg[0], color=MEN), FadeIn(rate_t, shift=0.1 * UP),
                      Indicate(chart[2][0], color=MEN), run_time=beat.until("Here", offset=-0.2))
            self.play(FadeOut(VGroup(run_leg, rise_leg, run_t, rise_t, rate_t)),
                      FadeIn(mletters[0]), FadeIn(legend.move_to([-1.6, 2.95, 0])), run_time=0.6)
            for i in range(1, 6):
                self.play(Create(mseg[i]), FadeIn(mj[i]), FadeIn(mletters[i]),
                          Indicate(chart[2][i], color=MEN, scale_factor=1.1), run_time=0.55)
            beat.wait_until("A and", offset=-0.1)
            self.play(mseg[0].animate.set_stroke(width=10), mseg[1].animate.set_stroke(width=10),
                      run_time=0.6)
            self.play(mseg[0].animate.set_stroke(width=6), mseg[1].animate.set_stroke(width=6),
                      run_time=0.6)

        # women
        wab_lbl = text("A, B", size=24, color=WOMEN).next_to(wseg.pts[2], DOWN + RIGHT, buff=0.1)
        cef = VGroup(wseg[2], wseg[4], wseg[5])
        share = MathTex(r"72\%", r"\text{ of women's}", font_size=MATH_SMALL + 4, color=MIX)
        share2 = label("applications", size=24, color=MIX)
        with self.narrate("Now the women. In A and B their steps are steeper, but tiny. Almost "
                          "three quarters of their run goes into C, E and F, where few got "
                          "in.") as beat:
            self.play(Create(wseg[0]), Create(wseg[1]), FadeIn(wj[:2]),
                      Indicate(chart[3][0], color=WOMEN), Indicate(chart[3][1], color=WOMEN),
                      run_time=beat.until("steeper", offset=-0.1))
            zoom = Circle(radius=0.38, color=WOMEN, stroke_width=3).move_to(wseg.pts[1])
            self.play(Create(zoom), FadeIn(wab_lbl), run_time=beat.until("Almost", offset=-0.2))
            self.play(FadeOut(zoom), LaggedStart(*[AnimationGroup(Create(wseg[i]), FadeIn(wj[i]),
                                                                  FadeIn(wletters[i - 2]))
                                                   for i in range(2, 6)], lag_ratio=0.35),
                      run_time=beat.until("C,", offset=-0.1))
            self.play(*[s.animate.set_color(MIX) for s in cef], run_time=0.8)
            g = VGroup(share, share2).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            g.move_to([2.0, -1.55, 0])
            self.play(FadeIn(g, shift=0.1 * UP), run_time=min(0.8, beat.remaining()))

        # ============================================================ 6. the formula
        m_end, w_end = mseg.pts[-1], wseg.pts[-1]
        mdash = DashedLine(O, m_end, color=MEN, stroke_width=3, dash_length=0.12)
        wdash = DashedLine(O, w_end, color=WOMEN, stroke_width=3, dash_length=0.12)
        mtot = MathTex(r"45\%", font_size=MATH, color=MEN).next_to(m_end, RIGHT, buff=0.15)
        wtot = MathTex(r"30\%", font_size=MATH, color=WOMEN).next_to(w_end, RIGHT, buff=0.15)
        rise = DashedLine([w_end[0], O[1], 0], w_end, color=INK, stroke_width=3, dash_length=0.08)
        run = Line(O, [w_end[0], O[1], 0], color=INK, stroke_width=5)
        f1 = MathTex(r"\text{rate} = \frac{\text{admitted}}{\text{applied}}", font_size=MATH,
                     substrings_to_isolate=[r"\text{admitted}", r"\text{applied}", r"\text{rate}", "="])
        f1.move_to([-1.4, 2.95, 0])
        f2 = MathTex(r"\text{rate} = \frac{\sum_d \text{applied}_d \times \text{rate}_d}{\text{applied}}",
                     font_size=MATH, substrings_to_isolate=[r"\text{applied}_d", r"\text{rate}_d", r"\sum_d",
                                                            r"\times", r"\text{applied}", r"\text{rate}", "="])
        f2.move_to(f1, aligned_edge=LEFT)
        f3 = MathTex(r"\text{rate} = \sum_d \frac{\text{applied}_d}{\text{applied}} \times \text{rate}_d",
                     font_size=MATH, substrings_to_isolate=[r"\frac{\text{applied}_d}{\text{applied}}",
                                                            r"\text{rate}_d", r"\sum_d", r"\times",
                                                            r"\text{rate}", "="])
        f3.move_to(f1, aligned_edge=LEFT)
        wfrac = f3.get_part_by_tex(r"\frac{\text{applied}_d}{\text{applied}}")
        wfrac.set_color(MIX)
        with self.narrate("The overall rate is the slope of this dashed line. Its rise is every "
                          "admission, and its run is every application. Each department adds its "
                          "applicants times its rate. So the overall rate is an average of "
                          "department rates, weighted by where people applied.") as beat:
            self.play(FadeOut(g), FadeOut(legend), *[s.animate.set_color(WOMEN) for s in cef],
                      run_time=beat.until("this", offset=-0.3))
            self.play(Create(wdash), Create(mdash), run_time=0.9)
            self.play(FadeIn(wtot, shift=0.1 * LEFT), FadeIn(mtot, shift=0.1 * LEFT),
                      run_time=beat.until("rise", offset=-0.2))
            self.play(Create(rise), Write(f1.get_part_by_tex(r"\text{rate}")),
                      Write(f1.get_part_by_tex("=")), run_time=beat.until("every", offset=-0.1))
            self.play(TransformFromCopy(rise, f1.get_part_by_tex(r"\text{admitted}")),
                      run_time=beat.until("run is", offset=-0.1))
            rest = VGroup(*[m for m in f1.family_members_with_points()
                            if m not in f1.get_part_by_tex(r"\text{admitted}").get_family()
                            and m not in f1.get_part_by_tex(r"\text{applied}").get_family()
                            and m not in f1.get_part_by_tex(r"\text{rate}").get_family()
                            and m not in f1.get_part_by_tex("=").get_family()])
            self.play(Create(run), run_time=0.6)
            self.play(TransformFromCopy(run, f1.get_part_by_tex(r"\text{applied}")), FadeIn(rest),
                      run_time=beat.until("Each", offset=-0.1))
            self.play(LaggedStart(*[Indicate(s, color=WOMEN, scale_factor=1.0) for s in wseg],
                                  lag_ratio=0.15),
                      morph(f1, f2, [(r"\text{rate}", r"\text{rate}"), ("=", "="),
                                     (r"\text{applied}", r"\text{applied}"),
                                     (f1.get_part_by_tex(r"\text{admitted}"),
                                      VGroup(f2.get_part_by_tex(r"\sum_d"),
                                             f2.get_part_by_tex(r"\text{applied}_d"),
                                             f2.get_part_by_tex(r"\times"),
                                             f2.get_part_by_tex(r"\text{rate}_d")))]),
                      run_time=beat.until("So the", offset=-0.1))
            self.play(FadeOut(rise), FadeOut(run), run_time=0.5)
            self.play(morph(f2, f3, [(r"\text{rate}", r"\text{rate}"), ("=", "="),
                                     (r"\sum_d", r"\sum_d"), (r"\times", r"\times"),
                                     (r"\text{rate}_d", r"\text{rate}_d"),
                                     (VGroup(f2.get_part_by_tex(r"\text{applied}_d"),
                                             f2.get_part_by_tex(r"\text{applied}", substring=False)
                                             if False else f2.get_parts_by_tex(r"\text{applied}")[-1]),
                                      wfrac)]),
                      run_time=beat.until("weighted", offset=-0.1))
            wtag = label("where they applied", size=24, color=MIX).next_to(wfrac, DOWN, buff=0.2)
            rtag = label("dept. rate", size=24, color=GRAY).next_to(f3.get_part_by_tex(r"\text{rate}_d"), DOWN, buff=0.2)
            rtag.align_to(wtag, UP)
            self.play(FadeIn(wtag, shift=0.1 * UP), FadeIn(rtag, shift=0.1 * UP),
                      *[s.animate.set_color(MIX) for s in cef], run_time=0.8)
            self.play(*[s.animate.set_color(WOMEN) for s in cef], run_time=min(0.8, beat.remaining()))

        # ============================================================ 7. the swap
        t = ValueTracker(0.0)

        def ns_now():
            a = t.get_value()
            return [(1 - a) * w + a * m * sum(W_N) / sum(M_N) * (1 + a * (sum(M_N) / sum(W_N) - 1))
                    / (1 + 0 * a) for w, m in zip(W_N, M_N)]

        def runs_now():
            a = t.get_value()
            return [(1 - a) * w + a * m for w, m in zip(W_N, M_N)]

        def build_chain():
            ns = runs_now()
            pts = [ax.c2p(0, 0)]
            cx = cy = 0
            for n, r in zip(ns, W_R):
                cx += n
                cy += n * r
                pts.append(ax.c2p(cx, cy))
            return pts

        def rate_now():
            ns = runs_now()
            return sum(n * r for n, r in zip(ns, W_R)) / sum(ns)

        def live_chain():
            pts = build_chain()
            g = VGroup(*[Line(p, q, color=WOMEN, stroke_width=6) for p, q in zip(pts, pts[1:])])
            g.add(*[Dot(p, radius=0.045, color=WOMEN) for p in pts[1:]])
            g.add(DashedLine(pts[0], pts[-1], color=WOMEN, stroke_width=3, dash_length=0.12))
            return g

        rate_tr = ValueTracker(W_TOT * 100)
        readout = live_number(rate_tr, 0, size=EQ, color=WOMEN, prefix=r"\text{women}",
                              suffix=r"\%")
        readout.move_to([4.6, -0.2, 0])
        mread = MathTex(r"\text{men}", r"\;45", r"\%", font_size=EQ, color=MEN)
        mread.next_to(readout, UP, buff=0.35).align_to(readout, LEFT)

        f4 = MathTex(r"\text{rate} = \sum_d \frac{\text{applied}_d}{\text{applied}} \times \text{rate}_d",
                     font_size=MATH, substrings_to_isolate=[r"\frac{\text{applied}_d}{\text{applied}}",
                                                            r"\text{rate}_d", r"\sum_d", r"\times",
                                                            r"\text{rate}", "="])
        f4.move_to(f3)
        f4.get_part_by_tex(r"\frac{\text{applied}_d}{\text{applied}}").set_color(MEN)
        f4.get_part_by_tex(r"\text{rate}_d").set_color(WOMEN)
        wtag2 = label("men's mix", size=24, color=MEN).move_to(wtag)
        rtag2 = label("women's rates", size=24, color=WOMEN).move_to(rtag).align_to(rtag, LEFT)
        with self.narrate("So run the test the pooled number skipped. Keep the women's own rate "
                          "in every department, but give them the men's mix of applications. "
                          "Where does their overall rate land? [pause 1.5]") as beat:
            self.play(FadeIn(mread, shift=0.1 * LEFT), FadeIn(readout, shift=0.1 * LEFT),
                      run_time=beat.until("Keep", offset=-0.2))
            self.play(ReplacementTransform(rtag, rtag2),
                      f3.get_part_by_tex(r"\text{rate}_d").animate.set_color(WOMEN),
                      run_time=beat.until("give", offset=-0.1))
            self.play(ReplacementTransform(wtag, wtag2), wfrac.animate.set_color(MEN),
                      Indicate(chart[2], color=MEN, scale_factor=1.05),
                      run_time=beat.until("Where", offset=-0.1))
            # prediction pause: the women's chain and readout wait, the question hangs
            self.play(Indicate(readout, color=MIX, scale_factor=1.08),
                      run_time=min(1.0, beat.remaining()))
            self.hold(max(0, beat.remaining()))

        swap_chain = always_redraw(live_chain)
        with self.narrate("Fifty two percent. Seven points above the men, from the same "
                          "committee decisions.") as beat:
            self.remove(wseg, wj, wdash, wletters)
            self.add(swap_chain)
            rate_tr.add_updater(lambda m: m.set_value(rate_now() * 100))
            self.add(rate_tr)
            self.play(t.animate.set_value(1.0), FadeOut(wtot), run_time=beat.until("Seven", offset=-0.2),
                      rate_func=SMOOTH)
            rate_tr.clear_updaters()
            final = build_chain()
            stot = MathTex(r"52\%", font_size=MATH, color=WOMEN).next_to(final[-1], UP, buff=0.15)
            stot.shift(LEFT * 0.4)
            gapb = BraceBetweenPoints(m_end + RIGHT * 0.05, final[-1] + RIGHT * 0.05, direction=RIGHT,
                                      color=MIX)
            self.play(FadeIn(stot), Indicate(readout, color=MIX, scale_factor=1.08), run_time=0.8)
            self.hold(max(0, beat.remaining() - 0.1))

        # ============================================================ 8. payoff: the paper + the arrows
        self.play(FadeOut(VGroup(*[m for m in self.mobjects])), run_time=0.6)
        self.remove(swap_chain)
        sex = text("applicant's sex", size=HEADING)
        dep = text("department", size=HEADING)
        adm = text("admitted", size=HEADING)
        sex.move_to([-4.3, -0.9, 0])
        dep.move_to([0, 1.6, 0])
        adm.move_to([4.3, -0.9, 0])
        a_sd = Arrow(sex.get_top() + UP * 0.1 + RIGHT * 0.3, dep.get_left() + LEFT * 0.15, color=MIX,
                     stroke_width=5, buff=0.1, max_tip_length_to_length_ratio=0.08)
        a_da = Arrow(dep.get_right() + RIGHT * 0.15, adm.get_top() + UP * 0.1 + LEFT * 0.3, color=GRAY,
                     stroke_width=5, buff=0.1, max_tip_length_to_length_ratio=0.08)
        a_sa = Arrow(sex.get_right() + RIGHT * 0.15, adm.get_left() + LEFT * 0.15, color=INK,
                     stroke_width=5, buff=0.1, max_tip_length_to_length_ratio=0.06)
        l_sd = label("where people applied", size=LABEL, color=MIX)
        l_sd.next_to(a_sd.get_center(), UL, buff=0.2)
        l_sa = label("committee decisions", size=LABEL, color=INK).next_to(a_sa, UP, buff=0.18)
        l_res = label("no bias against women", size=LABEL, color=GRAY).next_to(a_sa, DOWN, buff=0.22)
        l_res2 = label("(small tilt toward them)", size=24, color=GRAY).next_to(l_res, DOWN, buff=0.12)
        cite = citation("Bickel, Hammel & O'Connell, 1975 · Science 187:398")
        with self.narrate("Bickel, Hammel and O'Connell made this argument in Science in "
                          "nineteen seventy five, using the full campus data. They found no "
                          "pattern of discrimination by the admissions committees, and if "
                          "anything, a small tilt in favour of women.") as beat:
            self.play(FadeIn(cite), FadeIn(sex), FadeIn(adm), run_time=beat.until("using", offset=-0.3))
            self.play(GrowArrow(a_sa), FadeIn(l_sa), run_time=beat.until("They", offset=-0.1))
            self.play(Indicate(l_sa, color=INK), run_time=beat.until("no pattern", offset=-0.1))
            self.play(FadeIn(l_res, shift=0.1 * DOWN), run_time=beat.until("a small", offset=-0.2))
            self.play(FadeIn(l_res2, shift=0.1 * DOWN), run_time=min(0.8, beat.remaining()))

        with self.narrate("Splitting by department holds this other path fixed: which fields "
                          "people applied to. That's the right comparison for judging committees. "
                          "Ask whether the whole system admitted women less, and the pooled gap "
                          "is the answer, with its cause upstream, on this yellow arrow.") as beat:
            self.play(FadeIn(dep, shift=0.1 * DOWN), run_time=beat.until("this other", offset=-0.5))
            self.play(GrowArrow(a_sd), GrowArrow(a_da), run_time=beat.until("which", offset=-0.1))
            self.play(FadeIn(l_sd, shift=0.1 * UP), run_time=beat.until("That's", offset=-0.1))
            self.play(Indicate(VGroup(a_sa, l_sa), color=INK, scale_factor=1.04),
                      run_time=beat.until("Ask", offset=-0.1))
            self.play(dim(l_res, l_res2, a_sa, l_sa, opacity=0.35), run_time=beat.until("yellow", offset=-0.6))
            self.play(Indicate(VGroup(a_sd, l_sd), color=MIX, scale_factor=1.06), run_time=0.9)
            self.hold(max(0, beat.remaining()))

        # ============================================================ 9. landing
        bars2 = self.cold_bars()
        m2, w2 = bars2
        top_m = m2[0].get_top()[1]
        top_w = w2[0].get_top()[1]
        gx = w2[0].get_right()[0] + 0.3
        gap2 = BraceBetweenPoints([gx, top_m, 0], [gx, top_w, 0], direction=RIGHT, color=MIX)
        ref2 = DashedLine([m2[0].get_left()[0], top_m, 0], [gx, top_m, 0], color=GRAY,
                          stroke_width=2, dash_length=0.08)
        why = label("where women applied", size=LABEL, color=MIX).next_to(gap2, RIGHT, buff=0.15)
        with self.narrate("So look again at forty four and thirty five. The arithmetic was right "
                          "all along. It was measuring where women applied, not how committees "
                          "judged them.") as beat:
            diag = VGroup(sex, dep, adm, a_sd, a_da, a_sa, l_sa, l_res, l_res2, cite)
            self.play(diag.animate.set_opacity(0.15).shift(RIGHT * 1.6), FadeOut(l_sd),
                      FadeIn(bars2), run_time=beat.until("The arithmetic", offset=-0.2))
            self.play(Create(ref2), GrowFromCenter(gap2), run_time=beat.until("where", offset=-0.2))
            self.play(TransformFromCopy(VGroup(a_sd), why) if False else FadeIn(why, shift=0.2 * LEFT),
                      run_time=0.8)
            self.hold(max(0, beat.remaining()))
        self.end_card()
