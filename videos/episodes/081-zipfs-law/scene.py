"""Episode 81: Why "The" Is Twice as Common as "Of" (Zipf's law vs a typing monkey).

    videos/toolkit/render.sh videos/episodes/081-zipfs-law/scene.py Episode videos/episodes/081-zipfs-law/final.mp4

Data: data.json, built by make_data.py (Brown Corpus counts + seeded random-typing simulation).
Palette: BLUE English counts, PURPLE monkey counts (simulated), RED the flat-line guess,
GREEN x26 more possible words per letter, YELLOW /32.5 rarer per letter and the slope it makes.
"""
import json
from pathlib import Path

import numpy as np
from manim import *
from sample_space import *

DATA = json.loads((Path(__file__).resolve().parent / "data.json").read_text())
TOP = DATA["top"]                                   # [[word, count], ...] English
ENG = np.array(DATA["eng"], dtype=float)            # [[rank, count], ...] sampled
MON = np.array(DATA["mon"], dtype=float)
FIT_E = DATA["fit_eng"][0]                          # -0.979
FIT_M, ICPT_M = DATA["fit_mon"]                     # -1.072, 4.81
Q = 0.2
EXP1 = DATA["N"] * Q / 26                           # expected count of a 1-letter word
EXP2 = DATA["N"] * Q * (1 - Q) / 26 ** 2
EXP3 = DATA["N"] * Q * (1 - Q) ** 2 / 26 ** 3
L26, L32 = np.log10(26), np.log10(26 / (1 - Q))

MONO = "CMU Typewriter Text"
BAR_BASE = -2.0
BAR_SCALE = 4.6 / 69971
BAR_X0, BAR_DX, BAR_W = -5.2, 0.95, 0.6


def lg(v):
    return float(np.log10(v))


class Episode(NarratedScene):
    EPISODE = 81
    TITLE = "Why “The” Is Twice as Common as “Of”"
    PRONUNCIATIONS = {"Elvevåg": "elveh vog", "Cancho": "kancho", "Li": "lee",
                      "Zipf": "zipf"}

    # ------------------------------------------------------------------ builders
    def word_bar(self, k, word, count):
        x = BAR_X0 + BAR_DX * k
        bar = Rectangle(width=BAR_W, height=count * BAR_SCALE, stroke_width=0,
                        fill_color=BLUE, fill_opacity=0.9)
        bar.move_to([x, BAR_BASE, 0], aligned_edge=DOWN)
        name = text(word, size=LABEL, color=BLUE).next_to([x, BAR_BASE, 0], DOWN, buff=0.18)
        name.align_to([0, BAR_BASE - 0.18, 0], UP)
        return bar, name

    def build_axes(self):
        ax = axes((0, 5, 1), (0, 5, 1), x_length=7.0, y_length=5.2, numbers=False)
        ax.shift(np.array([-5.5, -2.0, 0]) - ax.c2p(0, 0))
        tex = ["1", "10", "10^{2}", "10^{3}", "10^{4}", "10^{5}"]
        xl = VGroup(*[MathTex(t, font_size=MATH_SMALL, color=GRAY)
                      .next_to(ax.c2p(i, 0), DOWN, buff=0.18) for i, t in enumerate(tex)])
        yl = VGroup(*[MathTex(t, font_size=MATH_SMALL, color=GRAY)
                      .next_to(ax.c2p(0, i), LEFT, buff=0.18) for i, t in enumerate(tex)])
        xt = text("rank", size=LABEL, color=GRAY).next_to(ax.c2p(5, 0), RIGHT, buff=0.25)
        yt = text("times seen", size=LABEL, color=GRAY)
        yt.next_to(ax.c2p(0, 5), RIGHT, buff=0.3).shift(UP * 0.12)
        return ax, xl, yl, xt, yt

    def curve(self, ax, data, color, width=4):
        pts = [ax.c2p(lg(r), lg(c)) for r, c in data if c >= 1]
        m = VMobject(stroke_color=color, stroke_width=width)
        m.set_points_as_corners(pts)
        return m

    # ------------------------------------------------------------------ scene
    def construct(self):
        # ============================================================ cold open
        bars, names = VGroup(), VGroup()
        for k, (w, c) in enumerate(TOP[:6]):
            b, n = self.word_bar(k, w, c)
            bars.add(b)
            names.add(n)
        cnt_the = formula(r"69{,}971", size=MATH_SMALL, color=BLUE).next_to(bars[0], UP, buff=0.15)
        cnt_of = formula(r"36{,}412", size=MATH_SMALL, color=BLUE).next_to(bars[1], UP, buff=0.15)
        base = Line([-5.7, BAR_BASE, 0], [-0.1, BAR_BASE, 0], color=GRAY, stroke_width=2)

        with self.narrate("In a million words of American English, the appears seventy "
                          "thousand times, and of, the runner-up, about half as often.") as beat:
            self.play(Create(base), FadeIn(names[0]), GrowFromEdge(bars[0], DOWN),
                      run_time=beat.until("seventy", offset=-0.2))
            self.play(FadeIn(cnt_the, shift=0.15 * UP), run_time=0.6)
            beat.wait_until("of", 2, offset=-0.3)
            self.play(FadeIn(names[1]), GrowFromEdge(bars[1], DOWN), run_time=1.0)
            beat.wait_until("half", offset=-0.3)
            half = DashedLine(bars[0].get_top() + LEFT * 0.3 + DOWN * bars[0].height / 2,
                              bars[1].get_top() + RIGHT * 0.3, color=GRAY, stroke_width=2,
                              dash_length=0.08)
            self.play(FadeIn(cnt_of, shift=0.15 * UP), Create(half), run_time=0.9)

        # the monkey: a stream of random letters, and the two candidate shapes
        words = DATA["stream"].split()
        lines, cur = [], ""
        for w in words:
            if len(cur) + len(w) + 1 > 24:
                lines.append(cur)
                cur = w
            else:
                cur = (cur + " " + w).strip()
            if len(lines) == 4:
                break
        stream = VGroup(*[Text(s, font=MONO, font_size=30, color=PURPLE) for s in lines])
        stream.arrange(DOWN, aligned_edge=LEFT, buff=0.22).move_to([3.5, 1.75, 0])
        stream_tag = text("random keys · simulated", size=SMALL + 4, color=GRAY)
        stream_tag.next_to(stream, UP, buff=0.3).align_to(stream, LEFT)

        def sketch(kind, x):
            frame = RoundedRectangle(width=1.9, height=1.25, corner_radius=0.1,
                                     stroke_color=GRAY, stroke_width=2).move_to([x, -1.0, 0])
            l, r = frame.get_left()[0] + 0.25, frame.get_right()[0] - 0.25
            b, t = frame.get_bottom()[1] + 0.22, frame.get_top()[1] - 0.22
            if kind == "falls":
                g = FunctionGraph(lambda u: b + (t - b) * 0.12 / (u - l + 0.12) * 1.0,
                                  x_range=[l, r], color=INK, stroke_width=3)
            else:
                g = Line([l, (b + t) / 2, 0], [r, (b + t) / 2, 0], color=INK, stroke_width=3)
            lab = text(kind, size=LABEL, color=INK).next_to(frame, DOWN, buff=0.18)
            return VGroup(frame, g, lab)

        sk_fall, sk_flat = sketch("falls", 2.3), sketch("flat", 4.7)
        orq = text("or", size=LABEL, color=GRAY).move_to([3.5, -1.0, 0])

        with self.narrate("Now a monkey hits random keys until it has typed a million words. "
                          "Do its counts fall off like this, or stay flat? [pause 1.5]") as beat:
            self.play(FadeIn(stream_tag), run_time=0.5)
            for i, ln in enumerate(stream):
                self.play(AddTextLetterByLetter(ln, rate_func=LINEAR),
                          run_time=beat.until("Do", offset=-0.1) / (4 - i) if i < 3 else
                          beat.until("Do", offset=-0.1))
            self.play(FadeIn(sk_fall, shift=0.1 * UP),
                      Indicate(VGroup(bars[0], bars[1]), color=BLUE, scale_factor=1.04),
                      run_time=beat.until("or", offset=-0.1))
            self.play(FadeIn(orq), FadeIn(sk_flat, shift=0.1 * UP), run_time=0.8)

        # ============================================================ stakes
        ref_curve = ParametricFunction(
            lambda u: np.array([BAR_X0 + BAR_DX * u, BAR_BASE + 69971 * BAR_SCALE / (u + 1), 0]),
            t_range=[0, 5.3], color=GRAY, stroke_width=3)
        ref_curve = DashedVMobject(ref_curve, num_dashes=40)
        ref_lab = formula(r"\propto \frac{1}{\text{rank}}", size=MATH, color=GRAY)
        ref_lab.move_to([-1.3, 0.6, 0])
        with self.narrate("Further down the English list, the counts keep falling, roughly "
                          "as one over the rank.") as beat:
            self.play(FadeOut(VGroup(sk_fall, sk_flat, orq)), FadeOut(half),
                      LaggedStart(*[AnimationGroup(GrowFromEdge(bars[k], DOWN), FadeIn(names[k]))
                                    for k in range(2, 6)], lag_ratio=0.35),
                      run_time=beat.until("one over", offset=-0.2))
            self.play(Create(ref_curve), FadeIn(ref_lab), run_time=beat.remaining(1.2))

        zipf_lab = VGroup(text("Zipf:", size=LABEL, color=INK),
                          text("principle of least effort", size=LABEL, color=INK, slant=ITALIC))
        zipf_lab.arrange(DOWN, aligned_edge=LEFT, buff=0.15).move_to([3.4, -0.6, 0])
        cit_zipf = citation("Zipf, 1949 · Human Behavior and the Principle of Least Effort")
        with self.narrate("In nineteen forty nine, George Zipf read this curve as a law of human "
                          "behaviour, the principle of least effort. If random typing draws it "
                          "too, the curve can't be his evidence.") as beat:
            self.play(dim(stream, stream_tag), run_time=0.6)
            beat.wait_until("George", offset=-0.2)
            self.play(FadeIn(cit_zipf), FadeIn(zipf_lab[0]), run_time=0.8)
            beat.wait_until("principle", offset=-0.2)
            self.play(Write(zipf_lab[1]), run_time=1.0)
            beat.wait_until("random", offset=-0.2)
            self.play(undim(stream, stream_tag), Circumscribe(stream, color=PURPLE, buff=0.15),
                      run_time=1.2)
            beat.wait_until("evidence", offset=-0.3)
            cross = Line(zipf_lab[1].get_left(), zipf_lab[1].get_right(), color=GRAY,
                         stroke_width=3)
            self.play(zipf_lab.animate.set_opacity(0.45), Create(cross), run_time=0.8)

        # ============================================================ naive build
        ax, xl, yl, xt, yt = self.build_axes()
        eng = self.curve(ax, ENG, BLUE)
        top_dots = VGroup(*[Dot(ax.c2p(lg(k + 1), lg(c)), radius=0.07, color=BLUE)
                            for k, (w, c) in enumerate(TOP[:6])])
        cit_brown = citation("Kučera & Francis, 1967 · Brown Corpus, American English")
        with self.narrate("So here is the whole English list: nearly fifty thousand different "
                          "words, ranked by count. Stretch both axes so each tick is ten times "
                          "the last.") as beat:
            self.play(FadeOut(VGroup(stream, stream_tag, zipf_lab, cross, ref_curve, ref_lab,
                                     cnt_the, cnt_of, names, base)),
                      FadeOut(cit_zipf), run_time=0.7)
            self.play(Create(ax), ReplacementTransform(bars, top_dots), FadeIn(xt), FadeIn(yt),
                      run_time=beat.until("fifty", offset=-0.3))
            self.play(Create(eng, rate_func=LINEAR), FadeIn(cit_brown),
                      run_time=beat.until("Stretch", offset=-0.1))
            self.play(LaggedStart(*[FadeIn(m, shift=0.1 * UP) for m in xl], lag_ratio=0.25),
                      LaggedStart(*[FadeIn(m, shift=0.1 * RIGHT) for m in yl], lag_ratio=0.25),
                      run_time=beat.until("ten times", offset=0.2))
            self.play(LaggedStart(*[flag(m) for m in list(xl[1:4])], lag_ratio=0.3),
                      run_time=beat.remaining(1.0))

        # panel: legends + slope readouts
        PX = 2.55
        sw_e = Line(ORIGIN, RIGHT * 0.5, color=BLUE, stroke_width=6)
        leg_e = VGroup(sw_e, text("English", size=LABEL, color=BLUE)).arrange(RIGHT, buff=0.2)
        leg_e.move_to([PX, 2.95, 0], aligned_edge=LEFT)
        s_e = ValueTracker(0.0)
        rd_e = live_number(s_e, 2, size=MATH, color=BLUE, prefix=r"\text{slope} =")
        rd_e.next_to(leg_e, DOWN, buff=0.25, aligned_edge=LEFT)
        ref = DashedLine(ax.c2p(0, lg(69971)), ax.c2p(lg(69971), 0), color=GRAY, stroke_width=3,
                         dash_length=0.12)
        ref_tag = formula(r"\text{slope } {-1}", size=MATH_SMALL, color=GRAY)
        ref_tag.move_to(ax.c2p(4.15, 1.25))
        band = Rectangle(width=ax.c2p(3, 0)[0] - ax.c2p(0, 0)[0], height=ax.c2p(0, 5)[1] - ax.c2p(0, 0)[1],
                         stroke_width=0, fill_color=DIM, fill_opacity=0.28)
        band.move_to(ax.c2p(0, 0), aligned_edge=DL).set_z_index(-2)
        band_tag = text("top 1,000", size=SMALL + 2, color=GRAY).move_to(ax.c2p(1.5, 0.35))
        with self.narrate("On these axes, one over rank is a straight line with slope minus one. "
                          "English hugs it. Fit the top thousand words, and the slope comes out "
                          "minus point nine eight.") as beat:
            self.play(Create(ref), run_time=beat.until("slope", offset=-0.2))
            self.play(FadeIn(ref_tag), run_time=0.6)
            beat.wait_until("English", offset=-0.2)
            self.play(FadeIn(leg_e), eng.animate.set_stroke(width=6), run_time=0.7)
            self.play(eng.animate.set_stroke(width=4), run_time=0.5)
            beat.wait_until("Fit", offset=-0.2)
            self.play(FadeIn(band), FadeIn(band_tag), run_time=0.8)
            beat.wait_until("slope", 2, offset=-0.3)
            self.add(rd_e)
            self.play(s_e.animate.set_value(FIT_E), run_time=beat.remaining(1.2))

        # the monkey's rules and the flat guess
        sw_m = Line(ORIGIN, RIGHT * 0.5, color=PURPLE, stroke_width=6)
        leg_m = VGroup(sw_m, text("monkey (simulated)", size=LABEL, color=PURPLE)).arrange(RIGHT, buff=0.2)
        leg_m.move_to([PX, 1.45, 0], aligned_edge=LEFT)
        rules = VGroup(
            VGroup(text("space bar:", size=LABEL, color=GRAY), formula(r"1 \text{ press in } 5", size=MATH)),
            VGroup(text("letters:", size=LABEL, color=GRAY), formula(r"26, \text{ all equal}", size=MATH)),
        )
        for r in rules:
            r.arrange(RIGHT, buff=0.2)
        rules.arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to([PX, -0.95, 0], aligned_edge=LEFT)
        guess = DashedLine(ax.c2p(0, 3.205), ax.c2p(5, 3.205), color=RED, stroke_width=4,
                           dash_length=0.14)
        guess_tag = text("guess: flat", size=LABEL, color=RED).move_to(ax.c2p(4.0, 3.65))
        with self.narrate("Our monkey hits the space bar one press in five, and otherwise any of "
                          "twenty six letters, all equally likely. No letter is favoured, so the "
                          "natural guess is that no word is either: a flat line, slope zero.") as beat:
            self.play(FadeIn(leg_m), FadeOut(cit_brown), run_time=0.7)
            beat.wait_until("space", offset=-0.2)
            self.play(FadeIn(rules[0], shift=0.1 * UP), run_time=0.8)
            beat.wait_until("twenty", offset=-0.2)
            self.play(FadeIn(rules[1], shift=0.1 * UP), run_time=0.8)
            beat.wait_until("flat", offset=-0.4)
            self.play(Create(guess), FadeIn(guess_tag), run_time=1.2)

        # ============================================================ fail
        mon = self.curve(ax, MON, PURPLE)
        s_m = ValueTracker(0.0)
        PIV = (1.5, ICPT_M + FIT_M * 1.5)
        fitm = always_redraw(lambda: Line(
            ax.c2p(0, PIV[1] - 1.5 * s_m.get_value()), ax.c2p(3, PIV[1] + 1.5 * s_m.get_value()),
            color=PURPLE, stroke_width=4))
        rd_m = live_number(s_m, 2, size=MATH, color=PURPLE, prefix=r"\text{slope} =")
        rd_m.next_to(leg_m, DOWN, buff=0.25, aligned_edge=LEFT)
        with self.narrate("Here is what it actually typed. Its counts fall too. Fit the same top "
                          "thousand ranks, and the slope is minus one point oh seven.") as beat:
            self.play(Create(mon, rate_func=LINEAR), run_time=beat.until("Fit", offset=-0.2))
            self.add(fitm, rd_m)
            self.play(s_m.animate.set_value(FIT_M), run_time=beat.until("minus", offset=0.4))
            self.play(flag(rd_m), run_time=0.8)

        gap = DoubleArrow(ax.c2p(3.25, 3.205), ax.c2p(3.25, PIV[1] + 1.5 * FIT_M + 0.02),
                          color=RED, stroke_width=4, buff=0, tip_length=0.2)
        gap_tag = formula(r"1.07", size=MATH_SMALL, color=RED).next_to(gap, RIGHT, buff=0.15)
        diff = formula(r"\Delta = 0.09", size=MATH, color=INK)
        with self.narrate("The flat guess misses by the entire slope, and random noise lands "
                          "within a tenth of English.") as beat:
            self.play(GrowFromCenter(gap), FadeIn(gap_tag), run_time=beat.until("and", offset=-0.2))
            both = VGroup(rd_e, rd_m)
            brk = Brace(both, RIGHT, color=INK, buff=0.15)
            diff.next_to(brk, RIGHT, buff=0.15)
            fit(diff)
            self.play(GrowFromCenter(brk), FadeIn(diff), run_time=1.0)
            beat.wait_until("English", offset=-0.2)
            self.play(Indicate(eng, color=BLUE, scale_factor=1.0), run_time=0.9)

        # ============================================================ insight
        plateau1 = Line(ax.c2p(0, lg(EXP1)), ax.c2p(lg(26), lg(EXP1)))
        plateau2 = Line(ax.c2p(lg(27), lg(202)), ax.c2p(lg(702), lg(202)))
        br1 = Brace(plateau1, DOWN, color=INK, buff=0.12)
        br2 = Brace(plateau2, DOWN, color=INK, buff=0.12)
        lab1 = VGroup(formula("26", size=MATH, color=INK), text("one-letter words", size=LABEL - 2))
        lab1.arrange(DOWN, buff=0.12).next_to(br1, DOWN, buff=0.12)
        lab1.align_to([ax.c2p(0, 0)[0] + 0.2, 0, 0], LEFT)
        lab2 = VGroup(formula("676", size=MATH, color=INK), text("two-letter words", size=LABEL - 2))
        lab2.arrange(DOWN, buff=0.12).next_to(br2, DOWN, buff=0.12)
        with self.narrate("Look closely at the monkey's curve. It's a staircase. The top step is "
                          "the twenty six one-letter words, all tied. The next holds six hundred "
                          "and seventy six two-letter words.") as beat:
            self.play(FadeOut(VGroup(eng, ref, ref_tag, guess, guess_tag, band, band_tag, gap,
                                     gap_tag, brk, diff, leg_e, rd_e, top_dots)),
                      fitm.animate.set_stroke(opacity=0), run_time=1.0)
            self.remove(fitm)
            self.play(mon.animate.set_stroke(width=6), run_time=beat.until("top", offset=-0.2))
            self.play(GrowFromCenter(br1), run_time=0.6)
            beat.wait_until("twenty", offset=-0.2)
            self.play(FadeIn(lab1, shift=0.1 * UP), run_time=0.8)
            beat.wait_until("six hundred", offset=-0.2)
            self.play(GrowFromCenter(br2), FadeIn(lab2, shift=0.1 * UP), run_time=1.0)

        # triangle between the midpoints of step 2 and step 3
        A = ax.c2p((lg(27) + lg(702)) / 2, lg(EXP2))
        B = ax.c2p((lg(703) + lg(18278)) / 2, lg(EXP2))
        C = ax.c2p((lg(703) + lg(18278)) / 2, lg(EXP3))
        dA, dC = Dot(A, radius=0.08, color=INK), Dot(C, radius=0.08, color=INK)
        h_leg = Arrow(A, B, buff=0, color=GREEN, stroke_width=5, tip_length=0.22)
        x26 = formula(r"\times 26", size=MATH, color=GREEN).next_to(h_leg, UP, buff=0.15)
        with self.narrate("Each extra letter multiplies the possible words by twenty six, so "
                          "each step sits twenty six times further along.") as beat:
            self.play(FadeOut(VGroup(br1, br2, lab1, lab2)), FadeIn(dA),
                      run_time=beat.until("twenty", offset=-0.3))
            self.play(GrowArrow(h_leg), run_time=1.0)
            self.play(FadeIn(x26, shift=0.1 * UP), run_time=0.6)

        rare = MathTex(r"\tfrac{4}{5}", r"\times", r"\tfrac{1}{26}", "=", r"\tfrac{1}{32.5}",
                       font_size=EQ, color=INK)
        rare[4].set_color(YELLOW)
        rare.move_to([PX, -2.45, 0], aligned_edge=LEFT)
        v_leg = Arrow(B, C, buff=0, color=YELLOW, stroke_width=5, tip_length=0.22)
        d32 = formula(r"\div 32.5", size=MATH, color=YELLOW).next_to(v_leg, RIGHT, buff=0.15)
        with self.narrate("Each extra letter also makes any single word rarer. The monkey must skip "
                          "the space bar, four times in five, and then hit the right letter, one "
                          "time in twenty six. Together, thirty two and a half times rarer.") as beat:
            beat.wait_until("skip", offset=-0.2)
            self.play(Indicate(rules[0], color=PURPLE, scale_factor=1.05), run_time=0.9)
            beat.wait_until("four", offset=-0.2)
            self.play(Write(rare[0]), run_time=0.7)
            beat.wait_until("one time", offset=-0.2)
            self.play(Indicate(rules[1], color=PURPLE, scale_factor=1.05), Write(rare[1:3]),
                      run_time=0.9)
            beat.wait_until("thirty", offset=-0.2)
            self.play(Write(rare[3]), FadeIn(rare[4]), run_time=0.8)
            self.play(GrowArrow(v_leg), TransformFromCopy(rare[4], d32),
                      run_time=beat.remaining(1.0))
            self.add(dC)

        hyp = DashedLine(A, C, color=YELLOW, stroke_width=4, dash_length=0.12)
        with self.narrate("Twenty six times further, thirty two and a half times lower, at every "
                          "step. What slope does that make? [pause 1.5]") as beat:
            self.play(flag(x26), run_time=0.8)
            beat.wait_until("thirty", offset=-0.2)
            self.play(flag(d32), run_time=0.8)
            beat.wait_until("What", offset=-0.2)
            self.play(Create(hyp), run_time=1.2)

        slope = MathTex(r"\text{slope}", "=", "-", r"{\log 32.5", r"\over", r"\log 26}",
                        r"\approx", "-1.07", font_size=EQ, color=INK)
        slope[3].set_color(YELLOW)
        slope[5].set_color(GREEN)
        slope[7].set_color(YELLOW)
        fit(slope, width=6.4 - PX)
        slope.move_to([PX, -1.0, 0], aligned_edge=LEFT)
        with self.narrate("Minus log thirty two and a half, over log twenty six. Minus one point oh "
                          "seven, the slope we measured.") as beat:
            self.play(FadeOut(rules), rare.animate.move_to([PX, 0.2, 0], aligned_edge=LEFT).scale(0.8),
                      Write(slope[0:3]), run_time=beat.until("log", offset=-0.1))
            self.play(TransformFromCopy(d32, slope[3]), run_time=beat.until("over", offset=-0.1))
            self.play(Write(slope[4]), TransformFromCopy(x26, slope[5]),
                      run_time=beat.until("Minus", 2, offset=-0.2))
            self.play(Write(slope[6:]), run_time=0.9)
            beat.wait_until("measured", offset=-0.3)
            mbox = box(rd_m, color=INK)
            self.play(Create(mbox), flag(slope[7]), run_time=0.9)

        law = VGroup(
            MathTex(r"\text{rank}", r"\propto", r"26^{L}", font_size=MATH, color=INK),
            MathTex(r"\text{count}", r"\propto", r"32.5^{-L}", font_size=MATH, color=INK),
            MathTex(r"\text{count}", r"\propto", r"\text{rank}^{-1.07}", font_size=MATH, color=INK),
        )
        law[0][2].set_color(GREEN)
        law[1][2].set_color(YELLOW)
        law[2][2].set_color(YELLOW)
        law.arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        law.move_to([PX, -1.15, 0], aligned_edge=LEFT)
        arrow_eq = MathTex(r"\Rightarrow", font_size=MATH, color=GRAY).next_to(law[2], LEFT, buff=0.15)
        k = (lg(EXP3) - lg(EXP2)) / ((lg(703) + lg(18278)) / 2 - (lg(27) + lg(702)) / 2)
        xa = (lg(27) + lg(702)) / 2
        line_all = DashedLine(ax.c2p(0, lg(EXP2) - k * xa), ax.c2p(4.6, lg(EXP2) + k * (4.6 - xa)),
                              color=YELLOW, stroke_width=4, dash_length=0.12)
        with self.narrate("The number of possible words grows exponentially with length. Each "
                          "word's count shrinks exponentially. Put together, they make a power "
                          "law, with no mind required.") as beat:
            self.play(FadeOut(rare), FadeOut(mbox),
                      slope.animate.move_to([PX, 0.25, 0], aligned_edge=LEFT),
                      run_time=beat.until("grows", offset=-0.4))
            self.play(TransformFromCopy(x26, law[0]), run_time=1.2)
            beat.wait_until("shrinks", offset=-0.4)
            self.play(TransformFromCopy(d32, law[1]), run_time=1.2)
            beat.wait_until("Put", offset=-0.2)
            self.play(FadeIn(arrow_eq), TransformMatchingTex(VGroup(law[1].copy()), law[2]),
                      run_time=1.0)
            self.play(ReplacementTransform(hyp, line_all), run_time=beat.remaining(1.0))

        # ============================================================ payoff
        cit_miller = citation("Miller, 1957 · American Journal of Psychology")
        cit_li = citation("Li, 1992 · IEEE Transactions on Information Theory")
        with self.narrate("George Miller made this point with random typing in nineteen fifty "
                          "seven. Wentian Li worked out the slope in nineteen ninety two.") as beat:
            self.play(FadeOut(VGroup(h_leg, v_leg, x26, d32, dA, dC)), run_time=0.8)
            beat.wait_until("George", offset=-0.2)
            self.play(FadeIn(cit_miller), run_time=0.6)
            beat.wait_until("Wentian", offset=-0.2)
            self.play(FadeOut(cit_miller), FadeIn(cit_li), run_time=0.6)
            self.play(flag(slope), run_time=0.9)

        eng.set_stroke(width=4)
        top_dot = Dot(ax.c2p(0, lg(69971)), radius=0.08, color=BLUE)
        the_tag = text("the", size=LABEL, color=BLUE).next_to(top_dot, RIGHT, buff=0.2)
        tie_box = SurroundingRectangle(Line(ax.c2p(0, lg(EXP1)), ax.c2p(lg(26), lg(EXP1))),
                                       color=INK, buff=0.14, corner_radius=0.06, stroke_width=3)
        tie_tag = text("26-way tie", size=LABEL, color=PURPLE).next_to(tie_box, DOWN, buff=0.15)
        tie_tag.align_to(tie_box, LEFT)
        cit_fe = citation("Ferrer-i-Cancho & Elvevåg, 2010 · PLoS ONE")
        with self.narrate("The staircase is also where the monkey gives itself away. In twenty "
                          "ten, Ferrer i Cancho and Elvevåg tested random texts statistically, and "
                          "they did not match the rank curves of real ones.") as beat:
            self.play(FadeIn(eng), FadeIn(leg_e), FadeOut(line_all), mon.animate.set_stroke(width=4),
                      FadeOut(law), FadeOut(arrow_eq), FadeOut(slope), run_time=1.0)
            self.play(Create(tie_box), FadeIn(tie_tag), run_time=beat.until("In", offset=-0.2))
            self.play(FadeOut(cit_li), FadeIn(cit_fe), FadeIn(top_dot), FadeIn(the_tag),
                      run_time=0.8)
            beat.wait_until("did not", offset=-0.2)
            self.play(Indicate(mon, color=PURPLE, scale_factor=1.0),
                      Indicate(eng, color=BLUE, scale_factor=1.0), run_time=1.2)

        with self.narrate("A straight line on log axes is a test that both can pass.") as beat:
            self.play(Create(ref), FadeIn(ref_tag), run_time=beat.until("test", offset=-0.2))
            self.play(Indicate(rd_m, color=PURPLE), run_time=0.9)

        # ============================================================ landing
        bar_the, nm_the = self.word_bar(0, "the", 69971)
        bar_of, nm_of = self.word_bar(1, "of", 36412)
        base2 = Line([-5.7, BAR_BASE, 0], [5.9, BAR_BASE, 0], color=GRAY, stroke_width=2)
        mon_top = DATA["mon_top"][:26]
        mbars = VGroup(*[Rectangle(width=0.13, height=c * BAR_SCALE, stroke_width=0,
                                   fill_color=PURPLE, fill_opacity=0.9)
                         .move_to([0.6 + 0.2 * i, BAR_BASE, 0], aligned_edge=DOWN)
                         for i, (w, c) in enumerate(mon_top)])
        mnames = text("one-letter words", size=LABEL, color=PURPLE).next_to(mbars, DOWN, buff=0.2)
        mnames.align_to([0, BAR_BASE - 0.18, 0], UP)
        mcount = formula(r"\approx 7{,}800 \text{ each}", size=MATH_SMALL, color=PURPLE)
        mcount.next_to(mbars, UP, buff=0.2)
        mhead = text("monkey: 26-way tie", size=LABEL, color=PURPLE).next_to(mcount, UP, buff=0.25)
        c_the = formula(r"69{,}971", size=MATH_SMALL, color=BLUE).next_to(bar_the, UP, buff=0.15)
        c_of = formula(r"36{,}412", size=MATH_SMALL, color=BLUE).next_to(bar_of, UP, buff=0.15)
        with self.narrate("So, back to the top of the list. The monkey's most common word is tied "
                          "with twenty five others. English has one word alone at the top, the, "
                          "nearly twice as common as of. Chance drew the straight line for free. "
                          "It did not draw that.") as beat:
            keep = VGroup(top_dot, tie_box)
            self.play(FadeOut(VGroup(ax, xl, yl, xt, yt, eng, mon, ref, ref_tag, leg_e, leg_m, rd_m,
                                     the_tag, tie_tag, cit_fe)),
                      run_time=0.8)
            self.play(ReplacementTransform(top_dot, bar_the), ReplacementTransform(tie_box, mbars),
                      Create(base2), run_time=beat.until("monkey", offset=-0.2))
            self.play(FadeIn(mcount), FadeIn(mhead), FadeIn(mnames),
                      run_time=beat.until("English", offset=-0.2))
            self.play(FadeIn(nm_the), FadeIn(c_the), run_time=0.7)
            beat.wait_until("of", 2, offset=-0.3)
            self.play(GrowFromEdge(bar_of, DOWN), FadeIn(nm_of), FadeIn(c_of), run_time=0.9)
            beat.wait_until("Chance", offset=-0.2)
            line_end = DashedLine(bar_the.get_top() + RIGHT * 0.1,
                                  mbars[-1].get_top() + RIGHT * 0.3, color=YELLOW,
                                  stroke_width=3, dash_length=0.1)
            self.play(Indicate(mbars, color=PURPLE, scale_factor=1.0), run_time=1.0)
            beat.wait_until("did not", offset=-0.2)
            self.play(Create(box(VGroup(bar_the, bar_of, c_the, nm_the, nm_of), color=INK)),
                      run_time=0.9)

        self.end_card()
