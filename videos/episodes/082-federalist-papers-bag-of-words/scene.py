"""Episode 82 - The Boring Words That Unmasked an Author.

    videos/toolkit/render.sh videos/episodes/082-federalist-papers-bag-of-words/scene.py Episode \
        videos/episodes/082-federalist-papers-bag-of-words/final.mp4

All data: data.json, written by data_prep.py from the Project Gutenberg text (real counts).
Palette: RED = Hamilton, BLUE = Madison (and odds for Madison), INK = disputed essays,
YELLOW = focus (counted word, dividing line, error counter), GRAY/DIM = axes / context.
"""
import json
from math import log10
from pathlib import Path

import numpy as np
from manim import *
from sample_space import *

DATA = json.loads((Path(__file__).parent / "data.json").read_text())
H_IDS = sorted(int(k) for k in DATA["H"])
M_IDS = sorted(int(k) for k in DATA["M"])
D_IDS = [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 62, 63]
RATE = {**{int(k): v for k, v in DATA["H"].items()}, **{int(k): v for k, v in DATA["M"].items()},
        **{int(k): v for k, v in DATA["D"].items()}}
LOG_ODDS = {int(k): v for k, v in DATA["log10_odds"].items()}
W54 = DATA["odds54_words"]
PMF_H, PMF_M = DATA["pmf54"]["H"], DATA["pmf54"]["M"]

# strip-plot geometry ---------------------------------------------------------------
X0, UNIT = -3.55, 1.2            # x of rate 0, units per (use per 1,000 words)
ROW_Y = {"H": 1.45, "M": 0.05, "D": -1.3}
AXIS_Y = -2.15
DOT_R, STEP = 0.055, 0.125


def rx(r):
    return X0 + UNIT * r


def swarm(ids, word, row):
    """Beeswarm positions (exact x, y offsets only); zeros pile in 3 columns at x=0."""
    pos = {}
    zeros = [n for n in ids if RATE[n][word] == 0]
    for i, n in enumerate(zeros):
        col, lvl = i % 3, i // 3
        off = ((lvl + 1) // 2) * STEP * (1 if lvl % 2 else -1) if lvl else 0.0
        pos[n] = np.array([rx(0) + (col - 1) * STEP, ROW_Y[row] + off, 0])
    placed = []
    for n in sorted((n for n in ids if RATE[n][word] > 0), key=lambda n: RATE[n][word]):
        x = rx(RATE[n][word])
        for j in range(40):
            off = ((j + 1) // 2) * STEP * (1 if j % 2 else -1)
            if all(abs(x - px) >= STEP or abs(off - po) >= STEP for px, po in placed):
                break
        if zeros and x - rx(0) < 1.5 * STEP:   # keep clear of the zero pile
            x = max(x, rx(0) + 1.5 * STEP)
        placed.append((x, off))
        pos[n] = np.array([x, ROW_Y[row] + off, 0])
    return pos


def errors(word, cut):
    """Rule: rate > cut -> Hamilton.  Errors on the 65 known essays."""
    return (sum(RATE[n][word] <= cut for n in H_IDS) + sum(RATE[n][word] > cut for n in M_IDS))


def card(n):
    r = RoundedRectangle(width=0.84, height=1.08, corner_radius=0.08, stroke_color=INK,
                         stroke_width=2, fill_color=BG, fill_opacity=1)
    num = text(str(n), size=LABEL).move_to(r)
    return VGroup(r, num)


def chip(word):
    t = text(word, size=HEADING, color=YELLOW)
    b = RoundedRectangle(width=t.width + 0.6, height=0.85, corner_radius=0.12,
                         stroke_color=YELLOW, stroke_width=2.5)
    return VGroup(b, t.move_to(b))


class Episode(NarratedScene):
    EPISODE = 82
    TITLE = "The Boring Words That Unmasked an Author"
    PRONUNCIATIONS = {"Mosteller": "most eller", "Adair": "uh dair"}

    def construct(self):
        rng = np.random.default_rng(82)

        # ================================================================ 1 cold open
        ham = text("Hamilton", size=HEADING, color=RED).move_to([-4.5, 3.05, 0])
        mad = text("Madison", size=HEADING, color=BLUE).move_to([4.5, 3.05, 0])
        orq = text("or", size=BODY, color=GRAY).move_to([0, 3.05, 0])
        cards = VGroup(*[card(n) for n in D_IDS]).arrange(RIGHT, buff=0.2).move_to([0, 1.15, 0])
        chips = VGroup(chip("war"), chip("liberty"), chip("upon")).arrange(RIGHT, buff=0.9)
        chips.move_to([0, -1.55, 0])
        with self.narrate("Twelve of the Federalist Papers are disputed between Alexander "
                          "Hamilton and James Madison. You may count one word to settle it. "
                          "War, liberty, or upon. Pick one. [pause 1.5]") as beat:
            self.play(LaggedStart(*[FadeIn(c, shift=0.25 * DOWN) for c in cards], lag_ratio=0.12),
                      run_time=beat.until("Hamilton", offset=-0.1))
            self.play(FadeIn(ham, shift=0.2 * RIGHT), run_time=beat.until("Madison", offset=-0.1))
            self.play(FadeIn(orq), FadeIn(mad, shift=0.2 * LEFT), run_time=0.7)
            beat.wait_until("count", offset=-0.1)
            self.play(LaggedStart(*[c[0].animate.set_stroke(YELLOW, opacity=0.9) for c in cards],
                                  lag_ratio=0.05), run_time=1.0)
            self.play(*[c[0].animate.set_stroke(INK) for c in cards], run_time=0.5)
            for i, w in enumerate(["War", "liberty", "upon"]):
                beat.wait_until(w, offset=-0.12)
                self.play(FadeIn(chips[i], shift=0.2 * UP), run_time=0.45)
            beat.wait_until("Pick", offset=0.3)
            self.play(LaggedStart(*[flag(c) for c in chips], lag_ratio=0.35), run_time=1.6)

        # ================================================================ 2 stakes
        c51 = cards[2]
        quote_words = "If men were angels, no government would be necessary.".split()
        q1 = VGroup(*[text(w, size=BODY, slant=ITALIC) for w in quote_words[:4]]).arrange(RIGHT, buff=0.17)
        q2 = VGroup(*[text(w, size=BODY, slant=ITALIC) for w in quote_words[4:]]).arrange(RIGHT, buff=0.17)
        for line in (q1, q2):
            for w in line:
                w.align_to(line, DOWN)
        quote = VGroup(q1, q2).arrange(DOWN, buff=0.22).move_to([0, -0.85, 0])
        words = VGroup(*q1, *q2)
        y1804 = text("list made public 1804", size=SMALL + 2, color=RED).next_to(ham, DOWN, buff=0.15)
        y1818 = text("list of 1818", size=SMALL + 2, color=BLUE).next_to(mad, DOWN, buff=0.15)
        lh = Line(y1804.get_bottom() + DOWN * 0.08, c51.get_top() + UP * 0.08, color=RED, stroke_width=3)
        lm = Line(y1818.get_bottom() + DOWN * 0.08 + LEFT * 0.4, c51.get_top() + UP * 0.08 + RIGHT * 0.15,
                  color=BLUE, stroke_width=3)
        cite_adair = citation("Adair, 1944 · William and Mary Quarterly")
        with self.narrate("Essay fifty-one is one of them: if men were angels, no government "
                          "would be necessary. Hamilton's list, made public after his death in "
                          "eighteen oh four, claimed it. Madison's list, in eighteen eighteen, "
                          "claimed it too.") as beat:
            others = [c for c in cards if c is not c51]
            self.play(FadeOut(chips, shift=0.2 * DOWN), dim(*others),
                      c51[0].animate.set_stroke(YELLOW, width=3), run_time=beat.until("if", offset=-0.1))
            self.play(LaggedStart(*[FadeIn(w, shift=0.1 * UP) for w in words], lag_ratio=0.25),
                      run_time=beat.until("Hamilton's", offset=-0.1))
            self.play(FadeIn(y1804), Create(lh), FadeIn(cite_adair), run_time=beat.until("claimed"))
            beat.wait_until("Madison's", offset=-0.1)
            self.play(FadeIn(y1818), Create(lm), run_time=beat.until("claimed", 2))
            self.play(flag(c51), run_time=0.8)

        # ================================================================ 3 bag of words
        heap_pos = [np.array([rng.uniform(-2.8, 2.8), rng.uniform(-1.9, 0.6), 0]) for _ in words]
        # spread the heap so no two words overlap: simple rejection on a grid of slots
        slots = [np.array([x, y, 0]) for y in (0.55, -0.25, -1.05, -1.85) for x in (-2.6, -0.9, 0.9, 2.6)]
        order = rng.permutation(len(slots))[:len(words)]
        heap_pos = [slots[i] + np.array([rng.uniform(-0.3, 0.3), rng.uniform(-0.12, 0.12), 0]) for i in order]
        wlen = text("No. 51: 1,914 words", size=LABEL, color=GRAY).move_to([0, -2.75, 0])
        rate_eq = formula(r"\text{rate}", "=", r"{\text{uses}", r"\over", r"\text{words}}",
                          r"\times 1000", size=EQ)
        rate_eq.move_to([3.3, 2.2, 0])
        with self.narrate("Start the obvious way. Shred each essay into a bag of words: forget "
                          "the order, keep the counts, and divide by the length.") as beat:
            self.play(FadeOut(VGroup(*others, c51, lh, lm, y1804, y1818, orq, cite_adair)),
                      ham.animate.move_to([-4.5, 3.05, 0]), run_time=beat.until("Shred", offset=-0.1))
            self.play(*[w.animate.move_to(p).rotate(rng.uniform(-0.35, 0.35)).shift(LEFT * 1.6)
                        for w, p in zip(words, heap_pos)],
                      run_time=beat.until("keep", offset=-0.1), rate_func=SMOOTH)
            self.play(FadeIn(wlen.shift(LEFT * 1.6), shift=0.1 * UP), run_time=beat.until("divide", offset=-0.2))
            self.play(Write(rate_eq[0:2]), TransformFromCopy(words, rate_eq[2]), run_time=1.0)
            self.play(Write(rate_eq[3]), TransformFromCopy(wlen, rate_eq[4]), run_time=1.0)
            self.play(Write(rate_eq[5]), run_time=0.6)
        heap = VGroup(*words)

        # ================================================================ 4 strip plot (war)
        axis = NumberLine(x_range=[0, 8, 1], length=8 * UNIT, color=GRAY, stroke_width=2.5,
                          include_numbers=False, tick_size=0.06)
        axis.move_to([rx(4), AXIS_Y, 0])
        ticks = VGroup(*[MathTex(str(v), font_size=MATH_SMALL, color=GRAY).next_to(axis.n2p(v), DOWN, buff=0.18)
                         for v in range(0, 9, 2)])
        x_title = text("uses per 1,000 words", size=LABEL, color=GRAY)
        x_title.next_to(ticks, DOWN, buff=0.12).align_to(axis, RIGHT)
        src = citation("counts: Project Gutenberg text of The Federalist")
        rowlab_h = VGroup(text("Hamilton", size=LABEL, color=RED), text("51 essays", size=SMALL, color=GRAY)
                          ).arrange(DOWN, buff=0.08, aligned_edge=RIGHT)
        rowlab_m = VGroup(text("Madison", size=LABEL, color=BLUE), text("14 essays", size=SMALL, color=GRAY)
                          ).arrange(DOWN, buff=0.08, aligned_edge=RIGHT)
        rowlab_h.move_to([-4.6, ROW_Y["H"], 0], aligned_edge=RIGHT).shift(RIGHT * 0)
        rowlab_m.move_to([-4.6, ROW_Y["M"], 0], aligned_edge=RIGHT)
        rowlab_h.align_to(np.array([-4.3, 0, 0]), RIGHT)
        rowlab_m.align_to(np.array([-4.3, 0, 0]), RIGHT)
        pos = {w: {**swarm(H_IDS, w, "H"), **swarm(M_IDS, w, "M"), **swarm(D_IDS, w, "D")}
               for w in ("war", "liberty", "upon")}
        hd = {n: Dot(pos["war"][n], radius=DOT_R, color=RED) for n in H_IDS}
        md = {n: Dot(pos["war"][n], radius=DOT_R, color=BLUE) for n in M_IDS}
        counting = text("counting", size=BODY, color=GRAY)
        word_chip = chip("war")
        header = VGroup(counting, word_chip).arrange(RIGHT, buff=0.3).move_to([-3.2, 3.05, 0])
        with self.narrate("Sixty-five other essays have known authors: fifty-one by Hamilton, "
                          "fourteen by Madison. Each dot is one essay, placed by how often it "
                          "says war.") as beat:
            self.play(FadeOut(heap, shift=0.2 * DOWN), FadeOut(wlen), FadeOut(rate_eq),
                      FadeOut(mad), ReplacementTransform(ham, rowlab_h[0]),
                      run_time=beat.until("fifty-one", offset=-0.1))
            self.add(rowlab_h)
            self.play(FadeIn(rowlab_h[1]),
                      LaggedStart(*[GrowFromCenter(hd[n]) for n in H_IDS], lag_ratio=0.03),
                      run_time=beat.until("fourteen", offset=-0.1))
            self.play(FadeIn(rowlab_m),
                      LaggedStart(*[GrowFromCenter(md[n]) for n in M_IDS], lag_ratio=0.08),
                      run_time=beat.until("Each", offset=-0.1))
            self.play(Create(axis), FadeIn(ticks), FadeIn(x_title), FadeIn(src),
                      run_time=beat.until("war", offset=-0.15))
            self.play(FadeIn(header, shift=0.15 * DOWN), run_time=0.6)

        # ================================================================ 5 the dividing line
        cut = ValueTracker(3.0)
        state = {"word": "war"}
        top_y = 2.35
        line = always_redraw(lambda: DashedLine([rx(cut.get_value()), AXIS_Y, 0],
                                                [rx(cut.get_value()), top_y, 0],
                                                color=YELLOW, stroke_width=3, dash_length=0.12))
        to_h = text("Hamilton →", size=SMALL + 4, color=RED)
        to_m = text("← Madison", size=SMALL + 4, color=BLUE)
        to_h.add_updater(lambda m: m.next_to([rx(cut.get_value()), top_y, 0], RIGHT, buff=0.15))
        to_m.add_updater(lambda m: m.next_to([rx(cut.get_value()), top_y, 0], LEFT, buff=0.15))
        err_t = ValueTracker(errors("war", 3.0))
        err_lab = text("wrong:", size=BODY, color=YELLOW)
        err_num = DecimalNumber(err_t.get_value(), num_decimal_places=0, font_size=EQ, color=YELLOW)
        err_of = text("of 65", size=BODY, color=YELLOW)
        err_grp = VGroup(err_lab, err_num, err_of).arrange(RIGHT, buff=0.2).move_to([4.2, 3.05, 0])
        err_num.add_updater(lambda m: m.set_value(errors(state["word"], cut.get_value())))
        with self.narrate("Now slide a line to split them. Its best spot is the far edge, "
                          "calling every essay Hamilton's, and that still gets fourteen wrong.") as beat:
            self.play(Create(line), FadeIn(to_h), FadeIn(to_m), FadeIn(err_grp),
                      run_time=beat.until("Its", offset=-0.3))
            self.play(cut.animate.set_value(5.8), run_time=1.4, rate_func=SMOOTH)
            self.play(cut.animate.set_value(-0.35), run_time=beat.until("calling", offset=-0.1),
                      rate_func=SMOOTH)
            beat.wait_until("fourteen", offset=-0.1)
            self.play(flag(err_grp), run_time=0.9)

        # ================================================================ 6 cause: topic words
        ring8 = Circle(radius=0.16, color=YELLOW, stroke_width=3).move_to(hd[8])
        lab8 = text("No. 8: 11 uses", size=SMALL + 4, color=YELLOW).next_to(ring8, UP, buff=0.12)
        courts = [78, 79, 80, 81, 82, 83]
        court_rings = VGroup(*[Circle(radius=0.12, color=YELLOW, stroke_width=2.5).move_to(hd[n]) for n in courts])
        court_lab = text("courts: 0 or 1 use", size=SMALL + 4, color=YELLOW)
        with self.narrate("War follows the topic. Essay eight, on hostilities between the "
                          "states, says it eleven times; the essays on the courts, once at most. "
                          "Liberty does no better.") as beat:
            beat.wait_until("eight", offset=-0.15)
            self.play(Create(ring8), FadeIn(lab8), run_time=0.8)
            beat.wait_until("courts", offset=-0.3)
            court_lab.next_to(court_rings, DOWN, buff=0.12)
            court_lab.set_x(max(court_lab.get_x(), -2.2))
            court_lab.move_to([-1.2, ROW_Y["H"] - 0.78, 0])
            self.play(Create(court_rings), FadeIn(court_lab), run_time=0.9)
            beat.wait_until("Liberty", offset=-0.25)
            new_chip = chip("liberty").move_to(word_chip, aligned_edge=LEFT)
            state["word"] = "liberty"
            self.play(FadeOut(ring8), FadeOut(lab8), FadeOut(court_rings), FadeOut(court_lab),
                      Transform(word_chip, new_chip),
                      *[hd[n].animate.move_to(pos["liberty"][n]) for n in H_IDS],
                      *[md[n].animate.move_to(pos["liberty"][n]) for n in M_IDS],
                      run_time=1.6, rate_func=SMOOTH)
            self.play(cut.animate.set_value(2.0), run_time=1.0, rate_func=SMOOTH)
            self.play(cut.animate.set_value(-0.35), run_time=1.0, rate_func=SMOOTH)

        # ================================================================ 7 upon
        mis38 = Circle(radius=0.15, color=YELLOW, stroke_width=3)
        lab38 = text("No. 38", size=SMALL + 4, color=YELLOW)
        with self.narrate("Now count upon. Every one of Hamilton's fifty-one essays uses it. "
                          "Eleven of Madison's fourteen never do. The same line now makes one "
                          "mistake. Upon carries no topic, so it follows the writer.") as beat:
            new_chip = chip("upon").move_to(word_chip, aligned_edge=LEFT)
            self.play(Transform(word_chip, new_chip), run_time=beat.until("upon", offset=-0.1))
            state["word"] = "upon"
            self.play(*[hd[n].animate.move_to(pos["upon"][n]) for n in H_IDS],
                      *[md[n].animate.move_to(pos["upon"][n]) for n in M_IDS],
                      run_time=1.8, rate_func=SMOOTH)
            beat.wait_until("Every", offset=-0.1)
            self.play(LaggedStart(*[Indicate(hd[n], color=RED, scale_factor=1.6) for n in H_IDS],
                                  lag_ratio=0.02), run_time=beat.until("Eleven", offset=-0.2))
            zm = [n for n in M_IDS if RATE[n]["upon"] == 0]
            self.play(LaggedStart(*[Indicate(md[n], color=BLUE, scale_factor=1.6) for n in zm],
                                  lag_ratio=0.08), run_time=beat.until("same", offset=-0.2))
            self.play(cut.animate.set_value(0.86), run_time=beat.until("one", 2, offset=-0.1),
                      rate_func=SMOOTH)
            mis38.move_to(md[38])
            lab38.next_to(mis38, RIGHT, buff=0.12)
            self.play(Create(mis38), FadeIn(lab38), flag(err_grp), run_time=0.9)

        # ================================================================ 8 disputed essays
        dd = {n: Dot(pos["upon"][n], radius=DOT_R, color=INK) for n in D_IDS}
        rowlab_d = VGroup(text("Disputed", size=LABEL, color=INK), text("12 essays", size=SMALL, color=GRAY)
                          ).arrange(DOWN, buff=0.08, aligned_edge=RIGHT)
        rowlab_d.move_to([-4.6, ROW_Y["D"], 0]).align_to(np.array([-4.3, 0, 0]), RIGHT)
        lab5054 = text("No. 50 and No. 54", size=SMALL + 4, color=INK)
        with self.narrate("Drop in the twelve disputed essays. Ten land at zero. But fifty and "
                          "fifty-four, with one and two uses, fall on Hamilton's side of the line.") as beat:
            self.play(FadeOut(mis38), FadeOut(lab38), FadeIn(rowlab_d), run_time=0.6)
            starts = {n: rowlab_d.get_right() + RIGHT * 0.2 for n in D_IDS}
            for n in D_IDS:
                dd[n].move_to(starts[n]).set_opacity(0)
            self.play(LaggedStart(*[dd[n].animate.set_opacity(1).move_to(pos["upon"][n]) for n in D_IDS],
                                  lag_ratio=0.1), run_time=beat.until("Ten", offset=0.2))
            zd = [n for n in D_IDS if RATE[n]["upon"] == 0]
            self.play(LaggedStart(*[flag(dd[n], color=INK) for n in zd], lag_ratio=0.05), run_time=0.9)
            beat.wait_until("fifty", offset=-0.15)
            lab5054.next_to(VGroup(dd[50], dd[54]), RIGHT, buff=0.35)
            self.play(Indicate(dd[50], color=YELLOW, scale_factor=2), Indicate(dd[54], color=YELLOW, scale_factor=2),
                      FadeIn(lab5054, shift=0.1 * LEFT), run_time=1.0)
            beat.wait_until("Hamilton's", offset=-0.1)
            self.play(flag(to_h), run_time=0.8)

        # ================================================================ 9 likelihood, not sides
        lam_h = formula(r"\lambda_H", "=", r"3.3", r"\times", r"1.996", r"\approx", r"6.7", size=MATH)
        lam_m = formula(r"\lambda_M", "=", r"0.18", r"\times", r"1.996", r"\approx", r"0.36", size=MATH)
        for f, c in ((lam_h, RED), (lam_m, BLUE)):
            f[0].set_color(c)
            f[2].set_color(c)
            f[6].set_color(c)
        lam_h.move_to([3.4, 2.15, 0], aligned_edge=LEFT).shift(LEFT * 1.2)
        lam_m.next_to(lam_h, DOWN, buff=0.45, aligned_edge=LEFT)
        lam_note = text("rate per 1,000 × thousands of words", size=SMALL + 2, color=GRAY)
        lam_note.next_to(lam_m, DOWN, buff=0.3, aligned_edge=LEFT)
        tag54 = VGroup(text("No. 54", size=LABEL, color=INK),
                       text("1,996 words · upon × 2", size=SMALL + 4, color=GRAY)).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        tag54.move_to([-6.2, 2.75, 0], aligned_edge=LEFT)
        strip_stuff = VGroup(*hd.values(), *md.values(), *[dd[n] for n in D_IDS if n != 54], axis, ticks,
                             x_title, rowlab_h, rowlab_m, rowlab_d, lab5054, err_grp, header)
        dot54 = dd[54]
        with self.narrate("A line only asks which side. Ask instead how likely this exact count "
                          "is for each writer. Fifty-four runs about two thousand words. At "
                          "Hamilton's rate, three point three per thousand, he'd average six "
                          "point seven uses. Madison would average point three six.") as beat:
            self.play(cut.animate.set_value(1.6), run_time=0.8, rate_func=there_and_back)
            beat.wait_until("Ask", offset=-0.1)
            line.clear_updaters()
            to_h.clear_updaters()
            to_m.clear_updaters()
            self.play(FadeOut(strip_stuff), FadeOut(line), FadeOut(to_h), FadeOut(to_m), FadeOut(src),
                      dot54.animate.scale(1.6).move_to([-6.05, 2.75, 0]),
                      run_time=beat.until("Fifty-four", offset=-0.2))
            dot54.next_to(tag54, LEFT, buff=0.15)
            self.play(FadeIn(tag54, shift=0.1 * RIGHT), dot54.animate.next_to(tag54[0], LEFT, buff=0.15),
                      run_time=0.7)
            beat.wait_until("rate", offset=-0.2)
            self.play(Write(lam_h[0:2]), run_time=0.5)
            self.play(Write(lam_h[2:5]), run_time=beat.until("average", offset=-0.1))
            self.play(Write(lam_h[5:]), run_time=0.8)
            beat.wait_until("Madison", offset=-0.1)
            self.play(Write(lam_m), run_time=beat.until("six", 2, offset=-0.1))
            self.play(FadeIn(lam_note), run_time=0.6)

        # ================================================================ 10 Poisson picture
        ax = axes((-0.6, 12.6), (0, 0.8), x_ticks=[0, 2, 4, 6, 8, 10, 12], y_ticks=[0, 0.2, 0.4, 0.6, 0.8],
                  x_length=7.6, y_length=4.1, x_label="uses of “upon” in No. 54",
                  y_label="probability")
        ax.move_to([-2.05, -0.75, 0])
        bw = 0.28 * ax.x_axis.unit_size

        def bar(k, p, color, side):
            h = max(p * ax.y_axis.unit_size, 0.004)
            return Rectangle(width=bw, height=h, stroke_width=0, fill_color=color, fill_opacity=0.9
                             ).move_to(ax.c2p(k, 0) + RIGHT * side * bw / 2, aligned_edge=DOWN)
        bars_h = VGroup(*[bar(k, PMF_H[k], RED, -1) for k in range(13)])
        bars_m = VGroup(*[bar(k, PMF_M[k], BLUE, 1) for k in range(13)])
        pois = formula(r"P(k)", "=", r"{e^{-\lambda}", r"\lambda^k", r"\over", r"k!}", size=EQ)
        pois.move_to([3.6, -0.35, 0])
        lab_h = text("Hamilton", size=LABEL, color=RED).next_to(ax.c2p(7.6, 0.17), UR, buff=0.1)
        lab_m = text("Madison", size=LABEL, color=BLUE).next_to(bars_m[0], RIGHT, buff=0.35).shift(UP * 1.0)
        mark2 = Line(ax.c2p(2, 0), ax.c2p(2, 0.78), color=YELLOW, stroke_width=3)
        with self.narrate("Counts of a rare word follow a Poisson distribution, set by that "
                          "average. Here are both writers' chances for every count, and here is "
                          "two. Which writer does two favor? [pause 1.5]") as beat:
            self.play(Create(ax), FadeOut(lam_note), run_time=beat.until("Poisson", offset=-0.1))
            self.play(Write(pois[0:2]), TransformFromCopy(lam_h[0], pois[2]),
                      TransformFromCopy(lam_m[0], pois[3]), Write(pois[4:]),
                      run_time=beat.until("Here", offset=-0.1))
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars_h], lag_ratio=0.06),
                      LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars_m], lag_ratio=0.06),
                      FadeIn(lab_h), FadeIn(lab_m), run_time=beat.until("two", offset=-0.1))
            self.play(Create(mark2), dot54.animate.move_to(ax.c2p(2, 0.8) + UP * 0.12), run_time=0.8)
            beat.wait_until("Which", offset=-0.1)
            self.play(bars_h[2].animate.set_fill(opacity=1), bars_m[2].animate.set_fill(opacity=1),
                      *[b.animate.set_fill(opacity=0.3) for i, b in enumerate(bars_h) if i != 2],
                      *[b.animate.set_fill(opacity=0.3) for i, b in enumerate(bars_m) if i != 2],
                      run_time=1.2)

        # ================================================================ 11 ratio from the bars
        k = 30.0                                       # same magnification for both bars
        big_h = Rectangle(width=0.7, height=PMF_H[2] * ax.y_axis.unit_size * k, stroke_width=0,
                          fill_color=RED, fill_opacity=0.95)
        big_m = Rectangle(width=0.7, height=PMF_M[2] * ax.y_axis.unit_size * k, stroke_width=0,
                          fill_color=BLUE, fill_opacity=0.95)
        base = np.array([3.3, -2.05, 0])
        big_m.move_to(base, aligned_edge=DOWN)
        big_h.move_to(base + RIGHT * 1.6, aligned_edge=DOWN)
        floor = Line(base + LEFT * 0.7, base + RIGHT * 2.3, color=GRAY, stroke_width=2)
        pm = MathTex(r"4.5\%", font_size=MATH, color=BLUE).next_to(big_m, UP, buff=0.15)
        ph = MathTex(r"2.8\%", font_size=MATH, color=RED).next_to(big_h, UP, buff=0.15)
        zoom = text("at k = 2, both × 30", size=SMALL + 2, color=GRAY).next_to(floor, DOWN, buff=0.18)
        ratio = MathTex(r"{4.5", r"\over", r"2.8}", r"\approx", r"1.6", font_size=EQ)
        ratio[0].set_color(BLUE)
        ratio[2].set_color(RED)
        ratio[4].set_color(BLUE)
        ratio.move_to([4.0, 2.1, 0])
        ratio_lab = text("odds for Madison", size=LABEL, color=BLUE).next_to(ratio, DOWN, buff=0.2)
        with self.narrate("Madison, barely. Two is high for him but low for Hamilton. The bars "
                          "stand at four point five percent and two point eight percent. Their "
                          "ratio, one point six to one, is the evidence, and here it is weak.") as beat:
            self.play(FadeOut(pois), FadeOut(lam_h), FadeOut(lam_m), run_time=beat.until("The", offset=-0.4))
            self.play(Create(floor), TransformFromCopy(bars_m[2], big_m), TransformFromCopy(bars_h[2], big_h),
                      FadeIn(zoom), run_time=beat.until("four", offset=-0.1))
            self.play(FadeIn(pm, shift=0.1 * UP), run_time=beat.until("two", 2, offset=-0.1))
            self.play(FadeIn(ph, shift=0.1 * UP), run_time=beat.until("Their", offset=-0.1))
            self.play(TransformFromCopy(pm, ratio[0]), Write(ratio[1]), TransformFromCopy(ph, ratio[2]),
                      run_time=beat.until("one", offset=-0.1))
            self.play(Write(ratio[3:]), FadeIn(ratio_lab), run_time=beat.until("evidence"))

        # ================================================================ 12 multiply = add on log scale
        DEC = 0.86                                       # units per decade
        LX0 = -4.0
        lx = lambda d: LX0 + DEC * d
        lax = NumberLine(x_range=[0, 11, 1], length=11 * DEC, color=GRAY, stroke_width=2.5,
                         include_numbers=False, tick_size=0.06)
        lax.move_to([lx(5.5), -2.25, 0])
        lticks = VGroup(*[MathTex("1" if d == 0 else rf"10^{{{d}}}", font_size=MATH_SMALL, color=GRAY)
                          .next_to(lax.n2p(d), DOWN, buff=0.18) for d in range(0, 11, 2)])
        ltitle = text("odds for Madison (log scale)", size=LABEL, color=GRAY)
        ltitle.next_to(lticks, DOWN, buff=0.1).align_to(lax, RIGHT)
        seg_words = ["upon", "by", "on", "to", "there"]
        seg_y, seg_h = 1.0, 0.5
        segs, edges, acc = VGroup(), [], 0.0
        for w in seg_words:
            a, b = acc, acc + W54[w]
            segs.add(Rectangle(width=DEC * (b - a), height=seg_h, stroke_color=BG, stroke_width=2,
                               fill_color=BLUE, fill_opacity=0.9).move_to([lx((a + b) / 2), seg_y, 0]))
            edges.append((a, b))
            acc = b
        seg_labs = VGroup()
        for i, (w, s) in enumerate(zip(seg_words, segs)):
            t = text(w, size=LABEL, color=INK)
            if w == "upon":
                t.next_to(s, DOWN, buff=0.15).align_to(s, LEFT)
            else:
                t.next_to(s, UP, buff=0.15)
            seg_labs.add(t)
        total = MathTex(r"\approx 2.2\times 10^{7}", font_size=MATH, color=BLUE).next_to(segs, RIGHT, buff=0.25)
        assume = text("if the words are independent", size=SMALL + 4, color=GRAY).move_to([lx(3.3), 2.6, 0])
        tag54b = text("No. 54", size=LABEL, color=INK).next_to(segs, LEFT, buff=0.25)
        with self.narrate("So ask more words. By, on, to and there each give a ratio. If words "
                          "are independent, the ratios multiply, so on a log scale their lengths "
                          "add. For essay fifty-four, the product passes twenty million to one.") as beat:
            self.play(FadeOut(VGroup(ax, bars_h, bars_m, lab_h, lab_m, mark2, big_h, floor, pm, ph, zoom,
                                     ratio[0:4], ratio_lab, tag54, dot54)),
                      Create(lax), FadeIn(lticks), FadeIn(ltitle), run_time=beat.until("By", offset=-0.2))
            self.play(ReplacementTransform(VGroup(ratio[4], big_m), segs[0]), FadeIn(seg_labs[0]),
                      FadeIn(tag54b), run_time=0.8)
            for i, w in enumerate(["By", "on", "to", "there"], start=1):
                self.play(FadeIn(seg_labs[i], shift=0.1 * DOWN), GrowFromEdge(segs[i], LEFT),
                          run_time=max(0.5, beat.until(["on", "to", "there", "each"][i - 1], offset=-0.1)))
            beat.wait_until("independent", offset=-0.2)
            self.play(FadeIn(assume), run_time=0.6)
            beat.wait_until("lengths", offset=-0.1)
            self.play(LaggedStart(*[flag(s, color=BLUE) for s in segs], lag_ratio=0.2), run_time=1.2)
            beat.wait_until("passes", offset=-0.2)
            self.play(Write(total), run_time=0.9)

        # ================================================================ 13 all twelve
        ROW0, RSTEP, BH = 2.45, 0.4, 0.26
        ry = {n: ROW0 - i * RSTEP for i, n in enumerate(D_IDS)}
        rows = {n: Rectangle(width=max(DEC * LOG_ODDS[n], 0.02), height=BH, stroke_width=0, fill_color=BLUE,
                             fill_opacity=0.9).move_to([LX0, ry[n], 0], aligned_edge=LEFT) for n in D_IDS}
        rlabs = VGroup(*[MathTex(str(n), font_size=MATH_SMALL, color=INK).next_to([LX0, ry[n], 0], LEFT, buff=0.25)
                         for n in D_IDS])
        zero_line = Line([LX0, ry[49] + 0.3, 0], [LX0, -2.25, 0], color=GRAY, stroke_width=2)
        loo = text("known essays, each held out: 1 of 65 wrong", size=SMALL + 4, color=GRAY)
        loo.move_to([2.6, 3.2, 0])
        hdr2 = text("Poisson · 5 words · my counts", size=SMALL + 2, color=GRAY).move_to([-3.5, 3.2, 0])
        with self.narrate("Do it for every essay. Tested on the sixty-five known essays, each held "
                          "out in turn, it makes one mistake. All twelve disputed essays point to "
                          "Madison, though fifty-five barely leans.") as beat:
            target = VGroup(rows[54]).copy()
            self.play(FadeOut(seg_labs), FadeOut(total), FadeOut(assume), FadeOut(tag54b),
                      ReplacementTransform(segs, rows[54]), Create(zero_line), FadeIn(rlabs),
                      run_time=beat.until("Tested", offset=-0.2))
            self.play(FadeIn(loo), FadeIn(hdr2), run_time=beat.until("All", offset=-0.2))
            self.play(LaggedStart(*[GrowFromEdge(rows[n], LEFT) for n in D_IDS if n != 54], lag_ratio=0.12),
                      run_time=beat.until("fifty-five", offset=-0.2))
            box55 = SurroundingRectangle(VGroup(rlabs[6], rows[55]), color=YELLOW, buff=0.07, stroke_width=2.5)
            self.play(Create(box55), run_time=0.7)

        # ================================================================ 14 Mosteller & Wallace
        def diamond(n, odds):
            d = Square(0.17, color=YELLOW, fill_color=YELLOW, fill_opacity=1, stroke_width=0).rotate(PI / 4)
            return d.move_to([lx(log10(odds)), ry[n], 0])
        dm55, dm56 = diamond(55, 80), diamond(56, 800)
        mw55 = text("M&W: 80 to 1", size=SMALL + 4, color=YELLOW).next_to(dm55, RIGHT, buff=0.2)
        mw56 = text("M&W: 800 to 1", size=SMALL + 4, color=YELLOW).next_to(rows[56], RIGHT, buff=0.3)
        mw_c = citation("Mosteller & Wallace, 1963 · JASA 58(302)")
        with self.narrate("Frederick Mosteller and David Wallace did this carefully in nineteen "
                          "sixty-three: thirty words, and a model that lets words clump, which "
                          "shrinks the odds. They gave all twelve to Madison. Their weakest case "
                          "was also fifty-five, at about eighty to one. Next came fifty-six, at "
                          "eight hundred.") as beat:
            self.play(FadeIn(mw_c), run_time=beat.until("thirty", offset=-0.2))
            self.play(LaggedStart(*[flag(rows[n], color=BLUE) for n in D_IDS], lag_ratio=0.08),
                      run_time=beat.until("Their", offset=-0.2))
            beat.wait_until("eighty", offset=-0.25)
            self.play(FadeIn(dm55, scale=0.5), FadeIn(mw55), run_time=0.7)
            beat.wait_until("eight hundred", offset=-0.25)
            self.play(FadeIn(dm56, scale=0.5), FadeIn(mw56), FadeOut(box55), run_time=0.7)

        # ================================================================ 15 honest limit
        heap2 = heap.copy().set_opacity(1).move_to([1.2, 0.0, 0])
        ad_c = citation("Adair, 1944 · William and Mary Quarterly")
        chart = VGroup(*rows.values(), rlabs, zero_line, lax, lticks, ltitle, loo, hdr2, dm55, dm56, mw55, mw56)
        with self.narrate("Historians, led by Douglass Adair in nineteen forty-four, already "
                          "leaned toward Madison. The counts added evidence that ignores meaning "
                          "completely, which is why it hears habit and not argument.") as beat:
            self.play(FadeOut(mw_c), FadeIn(ad_c), dim(chart, opacity=0.25), run_time=beat.until("leaned"))
            beat.wait_until("ignores", offset=-0.2)
            self.play(FadeOut(chart), FadeIn(heap2, shift=0.2 * UP), run_time=1.0)
            beat.wait_until("habit", offset=-0.2)
            self.play(LaggedStart(*[w.animate.rotate(rng.uniform(-0.25, 0.25)).shift(
                rng.uniform(-0.2, 0.2) * RIGHT + rng.uniform(-0.15, 0.15) * UP) for w in heap2],
                lag_ratio=0.05), run_time=1.2)

        # ================================================================ 16 landing
        cards2 = VGroup(*[card(n) for n in D_IDS]).arrange(RIGHT, buff=0.2).move_to([0, 1.15, 0])
        chips2 = VGroup(chip("war"), chip("liberty"), chip("upon")).arrange(RIGHT, buff=0.9).move_to([0, -1.55, 0])
        ham2 = text("Hamilton: upon in 51 of 51 essays", size=LABEL, color=RED).move_to([0, 3.05, 0])
        zero51 = MathTex(r"\text{upon}\times 0", font_size=MATH, color=YELLOW).next_to(cards2[2], DOWN, buff=0.2)
        with self.narrate("In fifty-one essays, Hamilton never once went without upon. The essay "
                          "about angels never uses it at all.") as beat:
            self.play(FadeOut(ad_c), ReplacementTransform(heap2, cards2[2]),
                      LaggedStart(*[FadeIn(c) for i, c in enumerate(cards2) if i != 2], lag_ratio=0.05),
                      FadeIn(chips2), run_time=beat.until("Hamilton", offset=-0.1))
            self.play(FadeIn(ham2), dim(chips2[0], chips2[1], opacity=0.3), run_time=beat.until("upon", offset=-0.1))
            self.play(flag(chips2[2]), run_time=0.8)
            beat.wait_until("angels", offset=-0.3)
            self.play(cards2[2][0].animate.set_stroke(YELLOW, width=3),
                      dim(*[c for i, c in enumerate(cards2) if i != 2], opacity=0.3),
                      TransformFromCopy(chips2[2][1], zero51), run_time=1.0)
        self.hold(0.6)
        self.end_card()
