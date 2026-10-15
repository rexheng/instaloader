"""Episode 84 - An Algorithm That Finds Topics Without Reading.

    videos/toolkit/render.sh videos/episodes/084-topic-models-lda/scene.py Episode \
        videos/episodes/084-topic-models-lda/final.mp4

Toy data comes from sim.json (written by sim.py; all simulated, labelled on screen).
"""
import json
from pathlib import Path

from manim import *
from sample_space import *

SIM = json.loads((Path(__file__).with_name("sim.json")).read_text())
VOCAB = SIM["vocab"]
THEME = SIM["theme"]
D, W = SIM["D"], SIM["W"]
STATES = SIM["states"]
WRONG = SIM["wrong"]
KM = SIM["kmeans_labels"]
PROBE = SIM["probe"]
N = len(D)

COLX = [-3.55, -2.25, -0.95, 0.35, 1.65, 2.95]
ROWY = [1.75, 1.1, 0.45, -0.2, -0.85, -1.5]
HEAD_Y = 2.45
BAR_X, BAR_W, BAR_H = 5.15, 1.9, 0.34
TOPIC = [BLUE, PURPLE]


def token_positions():
    seen = {}
    pos = []
    counts = SIM["counts"]
    for i in range(N):
        d, w = D[i], W[i]
        j = seen.get((d, w), 0)
        seen[(d, w)] = j + 1
        n = counts[d][w]
        pos.append(np.array([COLX[w] + (j - (n - 1) / 2) * 0.3, ROWY[d], 0]))
    return pos


POS = token_positions()


def mix_bar(d, frac_blue, solid=None):
    """Stacked bar for speech d: blue share on the left, purple on the right."""
    left = BAR_X - BAR_W / 2
    wb = max(BAR_W * frac_blue, 0.001)
    wp = max(BAR_W * (1 - frac_blue), 0.001)
    b = Rectangle(width=wb, height=BAR_H, stroke_width=0, fill_color=BLUE,
                  fill_opacity=0.9 if frac_blue > 0.001 else 0)
    p = Rectangle(width=wp, height=BAR_H, stroke_width=0, fill_color=PURPLE,
                  fill_opacity=0.9 if frac_blue < 0.999 else 0)
    b.move_to([left + wb / 2, ROWY[d], 0])
    p.move_to([left + BAR_W - wp / 2, ROWY[d], 0])
    if solid is not None:          # an unfilled bar
        b.set_fill(opacity=0); p.set_fill(opacity=0)
    return VGroup(b, p)


def bar_frame(d):
    return Rectangle(width=BAR_W, height=BAR_H, stroke_color=DIM, stroke_width=1.5).move_to(
        [BAR_X, ROWY[d], 0])


def frac_blue(state, d):
    toks = [i for i in range(N) if D[i] == d]
    return sum(1 for i in toks if state[i] == 0) / len(toks)


class Episode(NarratedScene):
    EPISODE = 84
    TITLE = "An Algorithm That Finds Topics Without Reading"
    PRONUNCIATIONS = {"Dirichlet": "dee ree klay", "Ng": "ing", "Blei": "bly",
                      "CTM": "C T M", "LDA": "L D A"}

    # ------------------------------------------------------------------ helpers
    def page_grid(self, cols, rows, w, h, gap, center):
        g = VGroup(*[Rectangle(width=w, height=h, stroke_color=GRAY, stroke_width=1.2,
                               fill_color=GRAY, fill_opacity=0.12)
                     for _ in range(cols * rows)])
        g.arrange_in_grid(rows=rows, cols=cols, buff=gap).move_to(center)
        return g

    def ineq_rows(self, sign1=">", sign2="?"):
        lab1 = label("predicts unseen articles", color=GRAY).move_to([-3.4, 0.55, 0])
        lab2 = label("makes sense to readers", color=GRAY).move_to([-3.4, -0.95, 0])
        lab2.align_to(lab1, LEFT)
        m1 = formula(r"\text{CTM}", sign1, r"\text{LDA}", size=64).move_to([2.6, 0.55, 0])
        m2 = formula(r"\text{CTM}", sign2, r"\text{LDA}", size=64).move_to([2.6, -0.95, 0])
        m1[1].set_color(YELLOW); m2[1].set_color(YELLOW)
        return lab1, m1, lab2, m2

    # ------------------------------------------------------------------ scene
    def construct(self):
        # ============================================================ 0 cold open
        pages = self.page_grid(16, 3, 0.3, 0.38, 0.1, [0, 2.75, 0])
        pages_lab = label("8,447 New York Times articles", size=26, color=GRAY).next_to(
            pages, DOWN, buff=0.22)
        lab1, m1, lab2, m2 = self.ineq_rows()
        cite_chang = citation("Chang, Gerrish, Wang, Boyd-Graber & Blei, 2009 · NIPS")
        with self.narrate("Two programs were fed the same eight thousand New York Times "
                          "articles, and each sorted the words into topics. This one, CTM, "
                          "predicts unseen articles better than this one, LDA. Will its topics "
                          "also make more sense to people? [pause 1.5]") as beat:
            self.play(LaggedStart(*[FadeIn(p, shift=0.15 * DOWN) for p in pages],
                                  lag_ratio=0.03), run_time=beat.until("New York", offset=-0.3))
            self.play(FadeIn(pages_lab, shift=0.1 * UP), run_time=0.6)
            beat.wait_until("each", offset=-0.2)
            # the two model names emerge from the pile of pages
            self.play(TransformFromCopy(pages[:8], m1[0]), TransformFromCopy(pages[8:], m1[2]),
                      run_time=beat.until("This one", offset=-0.1))
            self.play(FadeIn(lab1, shift=0.1 * RIGHT), Indicate(m1[0], color=YELLOW,
                                                                  scale_factor=1.1),
                      FadeIn(cite_chang), run_time=beat.until("predicts", offset=-0.05))
            self.play(GrowFromCenter(m1[1]), run_time=beat.until("this one", occurrence=2))
            self.play(Indicate(m1[2], color=YELLOW, scale_factor=1.1), run_time=0.8)
            beat.wait_until("Will", offset=-0.15)
            self.play(TransformFromCopy(m1[0], m2[0]), TransformFromCopy(m1[2], m2[2]),
                      FadeIn(lab2, shift=0.1 * RIGHT), run_time=beat.until("people", offset=-0.2))
            self.play(Write(m2[1]), run_time=0.6)
            self.play(Circumscribe(m2[1], color=YELLOW, shape=Circle, buff=0.15),
                      run_time=1.4)

        # ============================================================ 1 stakes
        senate = self.page_grid(30, 7, 0.16, 0.2, 0.05, [0, 1.9, 0])
        senate_lab = label("118,065 Senate speeches · 1997–2004", color=GRAY).next_to(
            senate, DOWN, buff=0.25)
        topics42 = formula(r"K = 42", r"\text{ topics}", size=MATH).next_to(senate_lab, DOWN,
                                                                        buff=0.3)
        topics42[0].set_color(YELLOW)
        cite_quinn = citation("Quinn, Monroe, Colaresi, Crespin & Radev, 2010 · Am. J. Political Science")
        with self.narrate("Political scientists use topic models to track what the Senate talks "
                          "about, across more than a hundred and eighteen thousand speeches. If "
                          "the topics mean nothing, so does the measurement.") as beat:
            self.play(FadeOut(VGroup(lab1, m1, lab2, m2), shift=0.3 * DOWN), FadeOut(cite_chang),
                      ReplacementTransform(pages, senate), FadeOut(pages_lab),
                      run_time=beat.until("hundred", offset=-0.4))
            self.play(FadeIn(senate_lab, shift=0.1 * UP), FadeIn(cite_quinn),
                      run_time=0.8)
            beat.wait_until("If", offset=-0.1)
            self.play(Write(topics42), run_time=1.0)
            self.play(senate.animate.set_fill(opacity=0.04).set_stroke(opacity=0.35),
                      run_time=beat.remaining(0.8))

        # ============================================================ 2 the toy corpus
        sim_tag = text("simulated · 6 speeches · 48 words", size=22, color=GRAY).move_to(
            [0, 3.3, 0]).align_to([-6.3, 0, 0], LEFT)
        heads = VGroup(*[label(w, size=28).move_to([COLX[j], HEAD_Y, 0])
                         for j, w in enumerate(VOCAB)])
        rowlabs = VGroup(*[text(f"speech {d + 1}", size=26, color=GRAY).move_to([-5.1, y, 0])
                           for d, y in enumerate(ROWY)])
        seps = VGroup(*[Line([-6.0, y - 0.325, 0], [3.65, y - 0.325, 0], stroke_width=1,
                             color=DIM) for y in ROWY[:-1]])
        dots_ = VGroup(*[Dot(POS[i], radius=0.11, color=GRAY) for i in range(N)])
        frames = VGroup(*[bar_frame(d) for d in range(6)])
        rows_src = VGroup(*[senate[k * 35:(k + 1) * 35] for k in range(6)])
        with self.narrate("So shrink the problem: six simulated speeches, eight words each, "
                          "from a six-word vocabulary. Every dot is one word. A program that "
                          "cannot read sees only this: which words share a speech.") as beat:
            self.play(FadeOut(senate_lab), FadeOut(topics42), FadeOut(cite_quinn),
                      *[ReplacementTransform(rows_src[d], rowlabs[d]) for d in range(6)],
                      run_time=beat.until("six", offset=-0.1))
            self.play(FadeIn(sim_tag), Create(seps), run_time=beat.until("vocabulary", offset=-0.2))
            self.play(LaggedStart(*[FadeIn(h, shift=0.1 * DOWN) for h in heads], lag_ratio=0.12),
                      run_time=beat.until("Every", offset=-0.1))
            self.play(LaggedStart(*[FadeIn(dd, scale=0.4) for dd in dots_], lag_ratio=0.03),
                      run_time=beat.until("program", offset=-0.1))
            beat.wait_until("which", offset=-0.1)
            # co-occurrence: the dots of speech 5 pulse together, row by row
            self.play(LaggedStart(*[Indicate(VGroup(*[dots_[i] for i in range(N) if D[i] == d]),
                                             color=YELLOW, scale_factor=1.25)
                                    for d in range(6)], lag_ratio=0.35),
                      run_time=beat.remaining(1.4))

        # ============================================================ 3 naive k-means
        group_lab = label("group", size=26, color=GRAY).move_to([BAR_X, HEAD_Y, 0])
        km_bars = [mix_bar(d, 1.0 if KM[d] == 0 else 0.0) for d in range(6)]
        empty = [mix_bar(d, 1.0 if KM[d] == 0 else 0.0, solid=False) for d in range(6)]
        bars = VGroup(*empty)

        def color_row(d, k):
            return [dots_[i].animate.set_color(TOPIC[k]) for i in range(N) if D[i] == d]

        with self.narrate("The obvious first try is k-means: cluster whole speeches into two "
                          "groups. Speeches one and two land together, and so do three and "
                          "four.") as beat:
            self.add(bars)
            self.play(Create(frames), FadeIn(group_lab), run_time=beat.until("Speeches", offset=-0.2))
            self.play(*[Transform(bars[d], km_bars[d]) for d in (0, 1)],
                      *color_row(0, 0), *color_row(1, 0),
                      run_time=beat.until("three", offset=-0.1))
            self.play(*[Transform(bars[d], km_bars[d]) for d in (2, 3)],
                      *color_row(2, 1), *color_row(3, 1), run_time=beat.remaining(0.8))

        # ============================================================ 4 fail
        truth = [THEME[W[i]] for i in range(N)]
        wrong_km = [i for i in range(N) if KM[D[i]] != truth[i]]
        rings = VGroup(*[Circle(radius=0.19, color=RED, stroke_width=3.5).move_to(POS[i])
                         for i in wrong_km])
        wrong_t = ValueTracker(0)
        metric = live_number(wrong_t, 0, size=36, prefix=r"\text{words in wrong group} =",
                             suffix=r"/\,48")
        metric.move_to([0, 3.28, 0]).align_to([6.3, 0, 0], RIGHT)
        with self.narrate("Speech five is half money words and half war words, but k-means "
                          "has to give it a single group. So does speech six. Seven of the "
                          "forty-eight words land in the wrong group, because the label belongs "
                          "to the whole speech.") as beat:
            row5 = VGroup(*[dots_[i] for i in range(N) if D[i] == 4])
            self.play(Indicate(rowlabs[4], color=YELLOW), Indicate(row5, color=YELLOW,
                                                                    scale_factor=1.2),
                      run_time=beat.until("single", offset=-0.3))
            self.play(Transform(bars[4], km_bars[4]), *color_row(4, 1),
                      run_time=beat.until("speech six", offset=-0.1))
            self.play(Transform(bars[5], km_bars[5]), *color_row(5, 1), Indicate(rowlabs[5],
                                                                               color=YELLOW),
                      run_time=beat.until("Seven", offset=-0.25))
            self.play(LaggedStart(*[Create(r) for r in rings], lag_ratio=0.12),
                      FadeIn(metric), wrong_t.animate.set_value(len(wrong_km)),
                      run_time=beat.until("because", offset=-0.1))
            self.play(Indicate(VGroup(bars[4], bars[5]), color=YELLOW, scale_factor=1.06),
                      run_time=beat.remaining(1.0))

        # ============================================================ 5 LDA: random start
        mix_lab = label("mix", size=26, color=GRAY).move_to(group_lab)
        s0 = STATES[0]
        cite_blei = citation("Blei, Ng & Jordan, 2003 · J. Machine Learning Research")
        with self.narrate("Latent Dirichlet Allocation, from Blei, Ng and Jordan in two "
                          "thousand and three, moves the label onto each word, so a speech can "
                          "be a mix. Start by coloring every word at random.") as beat:
            self.play(FadeIn(cite_blei), run_time=beat.until("moves", offset=-0.3))
            self.play(FadeOut(rings), *[dd.animate.set_color(GRAY) for dd in dots_],
                      *[Transform(bars[d], mix_bar(d, 0.5, solid=False)) for d in range(6)],
                      wrong_t.animate.set_value(0),
                      run_time=beat.until("mix", offset=-0.2))
            self.play(ReplacementTransform(group_lab, mix_lab), run_time=0.6)
            beat.wait_until("random", offset=-0.3)
            self.play(LaggedStart(*[dots_[i].animate.set_color(TOPIC[s0[i]]) for i in range(N)],
                                  lag_ratio=0.02),
                      *[Transform(bars[d], mix_bar(d, frac_blue(s0, d))) for d in range(6)],
                      wrong_t.animate.set_value(WRONG[0]), run_time=beat.remaining(1.6))

        # ============================================================ 6 the probe word
        pi = PROBE["i"]
        pd, pw = D[pi], W[pi]
        probe_ring = Circle(radius=0.2, color=YELLOW, stroke_width=4).move_to(POS[pi])
        row_box = SurroundingRectangle(VGroup(rowlabs[pd], *[dots_[i] for i in range(N)
                                                             if D[i] == pd]),
                                       color=YELLOW, buff=0.12, corner_radius=0.08,
                                       stroke_width=2.5)
        col_box = Rectangle(width=1.15, height=4.6, color=YELLOW,
                            stroke_width=2.5).move_to([COLX[pw], 0.5, 0])
        row_purple = [i for i in range(N) if D[i] == pd and i != pi and s0[i] == 1]
        col_purple = [i for i in range(N) if W[i] == pw and i != pi and s0[i] == 1]
        all_purple = [i for i in range(N) if i != pi and s0[i] == 1]
        assert len(row_purple) == PROBE["ndk"][1] and len(col_purple) == PROBE["nkw"][1]
        assert len(all_purple) == PROBE["nk"][1]
        with self.narrate("Now recolor one word: this war, in speech five. Look along its "
                          "row: of the other seven words, two are purple. Look down its column: "
                          "of the twenty purple words, three are war.") as beat:
            self.play(FadeOut(cite_blei), run_time=0.5)
            beat.wait_until("this war", offset=-0.2)
            self.play(Create(probe_ring), Indicate(heads[pw], color=YELLOW),
                      run_time=beat.until("row", offset=-0.2))
            self.play(Create(row_box), run_time=beat.until("two", offset=-0.15))
            self.play(LaggedStart(*[Indicate(dots_[i], color=YELLOW, scale_factor=1.6)
                                    for i in row_purple], lag_ratio=0.3),
                      run_time=beat.until("Look down", offset=-0.1))
            self.play(Create(col_box), row_box.animate.set_stroke(opacity=0.35),
                      run_time=beat.until("twenty", offset=-0.15))
            self.play(LaggedStart(*[Indicate(dots_[i], color=YELLOW, scale_factor=1.5)
                                    for i in all_purple], lag_ratio=0.04),
                      run_time=beat.until("three", offset=-0.15))
            self.play(LaggedStart(*[Indicate(dots_[i], color=YELLOW, scale_factor=1.6)
                                    for i in col_purple], lag_ratio=0.25),
                      run_time=beat.remaining(1.0))

        # ============================================================ 7 the recolour rule
        conc = formula(r"p(\text{purple})", r"\propto", r"(", r"2", r"+\alpha)", r"\cdot",
                       r"(", r"3", r"+\beta)", r"\,/\,", r"(", r"20", r"+6\beta)", size=44)
        conc.move_to([-1.6, -2.3, 0])
        conc[0][2:-1].set_color(PURPLE)
        for k in (3, 7, 11):
            conc[k].set_color(YELLOW)
        odds_b = Rectangle(width=2.6 * PROBE["p"][0], height=0.42, stroke_width=0,
                           fill_color=BLUE, fill_opacity=0.9)
        odds_p = Rectangle(width=2.6 * PROBE["p"][1], height=0.42, stroke_width=0,
                           fill_color=PURPLE, fill_opacity=0.9)
        odds = VGroup(odds_b, odds_p).arrange(RIGHT, buff=0).move_to([4.75, -2.3, 0])
        pct_b = formula(rf"{round(100 * PROBE['p'][0])}\%", size=MATH_SMALL + 4, color=BLUE)
        pct_p = formula(rf"{round(100 * PROBE['p'][1])}\%", size=MATH_SMALL + 4, color=PURPLE)
        pct_b.next_to(odds_b, DOWN, buff=0.15)
        pct_p.next_to(odds_p, DOWN, buff=0.15)
        cite_gs = citation("Griffiths & Steyvers, 2004 · PNAS (Gibbs sampling for LDA)")
        with self.narrate("Multiply those shares, with a small alpha and beta so no count is "
                          "ever zero. Do the same for blue, and redraw the color with those "
                          "odds. Purple gets only twenty four percent, because the colors are "
                          "still noise.") as beat:
            self.play(Write(conc[0:2]), run_time=0.7)
            self.play(TransformFromCopy(VGroup(*[dots_[i] for i in row_purple]), conc[3]),
                      FadeIn(conc[2]), row_box.animate.set_stroke(opacity=1),
                      run_time=0.9)
            self.play(TransformFromCopy(VGroup(*[dots_[i] for i in col_purple]), conc[7]),
                      FadeIn(conc[5:7]), run_time=0.9)
            self.play(TransformFromCopy(VGroup(*[dots_[i] for i in all_purple]), conc[11]),
                      FadeIn(conc[9:11]), run_time=beat.until("alpha", offset=-0.2))
            self.play(Write(conc[4]), Write(conc[8]), Write(conc[12]),
                      run_time=beat.until("Do the same", offset=-0.1))
            self.play(GrowFromEdge(odds_b, LEFT), FadeIn(pct_b), FadeIn(cite_gs),
                      run_time=beat.until("redraw", offset=-0.1))
            self.play(GrowFromEdge(odds_p, RIGHT), FadeIn(pct_p),
                      run_time=beat.until("Purple", offset=-0.1))
            self.play(flag(pct_p, color=PURPLE), Indicate(odds_p, color=YELLOW),
                      run_time=beat.until("noise", offset=-0.3))
            self.play(Indicate(VGroup(*[dots_[i] for i in all_purple]), color=YELLOW,
                               scale_factor=1.15), run_time=beat.remaining(0.8))

        # ============================================================ 8 in symbols
        gen = formula(r"p(z = k)", r"\propto", r"(", r"n_{dk}", r"+\alpha)", r"\cdot",
                      r"(", r"n_{kw}", r"+\beta)", r"\,/\,", r"(", r"n_{k}", r"+V\beta)", size=44)
        gen.move_to(conc).align_to(conc, LEFT)
        for k in (3, 7, 11):
            gen[k].set_color(YELLOW)
        with self.narrate("In symbols: how much speech d uses topic k, times how much topic k "
                          "uses word w.") as beat:
            self.play(*[ReplacementTransform(conc[k], gen[k]) for k in range(13)],
                      FadeOut(cite_gs), run_time=beat.until("how much", offset=-0.1))
            self.play(Indicate(gen[3], color=YELLOW, scale_factor=1.25),
                      Indicate(row_box, color=YELLOW, scale_factor=1.0),
                      run_time=beat.until("times", offset=-0.1))
            self.play(Indicate(VGroup(gen[7], gen[11]), color=YELLOW, scale_factor=1.2),
                      Indicate(col_box, color=YELLOW, scale_factor=1.0),
                      run_time=beat.remaining(1.0))

        # ============================================================ 9 prediction
        sweep_t = ValueTracker(0)
        sweep = live_number(sweep_t, 0, size=36, prefix=r"\text{sweep}")
        sweep.move_to([4.75, -2.3, 0])
        row5_box = SurroundingRectangle(VGroup(rowlabs[4], bars[4], frames[4]), color=YELLOW,
                                        buff=0.12, corner_radius=0.08, stroke_width=3)
        q = formula(r"?", size=44, color=YELLOW).move_to([BAR_X, ROWY[4], 0])
        with self.narrate("Now do that to every word, sweep after sweep. Before it runs, "
                          "predict speech five: one color, or a split. [pause 1.5]") as beat:
            self.play(FadeOut(probe_ring), FadeOut(col_box), FadeOut(odds), FadeOut(pct_b),
                      FadeOut(pct_p), ReplacementTransform(row_box, row5_box),
                      gen.animate.set_opacity(0.45),
                      run_time=beat.until("sweep", offset=-0.1))
            self.play(FadeIn(sweep), run_time=0.6)
            beat.wait_until("predict", offset=-0.2)
            self.play(bars[4].animate.set_opacity(0.15), FadeIn(q, scale=0.6),
                      run_time=beat.until("one color", offset=-0.1))
            self.play(Indicate(q, color=YELLOW, scale_factor=1.3), run_time=1.0)
            self.play(Circumscribe(row5_box, color=YELLOW, buff=0.05),
                      run_time=beat.remaining(1.2))

        # ============================================================ 10 run the sampler
        def to_state(s):
            st = STATES[s]
            return ([dots_[i].animate.set_color(TOPIC[st[i]]) for i in range(N)
                     if STATES[s - 1][i] != st[i]] +
                    [Transform(bars[d], mix_bar(d, frac_blue(st, d))) for d in range(6)] +
                    [wrong_t.animate.set_value(WRONG[s]), sweep_t.animate.set_value(s)])

        with self.narrate("Each recoloring makes the rows and columns a little less random, "
                          "which sharpens the next one. Twenty four wrong words become "
                          "thirteen, eight, three, two, then none. Speech five settles at "
                          "exactly half and half, which k-means could never say.") as beat:
            self.play(FadeOut(q), bars[4].animate.set_opacity(1), run_time=0.6)
            self.play(Indicate(metric, color=RED, scale_factor=1.06),
                      run_time=beat.until("thirteen", offset=-0.65))
            for s, word in zip(range(1, 6), ["thirteen", "eight", "three", "two", "none"]):
                self.play(*to_state(s), run_time=0.6, rate_func=SMOOTH)
                if s < 5:
                    nxt = ["eight", "three", "two", "none"][s - 1]
                    beat.wait_until(nxt, offset=-0.65)
            self.play(sweep_t.animate.set_value(20), run_time=beat.until("half and half",
                                                                         offset=-0.3),
                      rate_func=LINEAR)
            self.play(flag(VGroup(bars[4], frames[4]), color=YELLOW), run_time=0.9)
            self.play(Indicate(rowlabs[4], color=YELLOW), run_time=beat.remaining(0.8))

        # ============================================================ 11 meaning is ours
        fin = STATES[-1]
        blue_words = formula(r"\text{tax}\;\;\text{budget}\;\;\text{deficit}", size=40,
                             color=BLUE)
        purp_words = formula(r"\text{troops}\;\;\text{war}\;\;\text{army}", size=40,
                             color=PURPLE)
        name_b = text("“money”?", size=28, color=GRAY, slant=ITALIC)
        name_p = text("“war”?", size=28, color=GRAY, slant=ITALIC)
        kmark = formula(r"K = 2", size=40, color=YELLOW)
        bottom = VGroup(VGroup(blue_words, name_b).arrange(RIGHT, buff=0.25),
                        VGroup(purp_words, name_p).arrange(RIGHT, buff=0.25),
                        kmark).arrange(RIGHT, buff=0.8).move_to([0, -2.35, 0])
        fit(bottom, width=12.5)
        with self.narrate("Notice what the program never used: what any word means. Blue is "
                          "only words that keep turning up together. Calling it money is our "
                          "reading, and so is the choice of two topics. On real text, another "
                          "random start can split the words differently, and so can another "
                          "K.") as beat:
            self.play(FadeOut(gen), FadeOut(sweep), FadeOut(row5_box),
                      run_time=beat.until("Blue", offset=-0.3))
            self.play(TransformFromCopy(heads[0:3], blue_words),
                      Indicate(VGroup(*[dots_[i] for i in range(N) if fin[i] == 0]),
                               color=BLUE, scale_factor=1.25),
                      run_time=beat.until("Calling", offset=-0.2))
            self.play(TransformFromCopy(heads[3:6], purp_words), FadeIn(name_b, shift=0.1 * LEFT),
                      run_time=beat.until("so is", offset=-0.2))
            self.play(FadeIn(name_p, shift=0.1 * LEFT), FadeIn(kmark, shift=0.1 * DOWN),
                      run_time=beat.until("On real", offset=-0.1))
            self.play(flag(kmark), run_time=0.8)
            beat.wait_until("another", occurrence=2, offset=-0.2)
            self.play(Indicate(kmark, color=YELLOW, scale_factor=1.2),
                      run_time=beat.remaining(0.8))

        # ============================================================ 12 held-out likelihood
        self.fade_out_all(run_time=0.6)
        pages2 = self.page_grid(10, 5, 0.42, 0.54, 0.12, [-1.2, 0.9, 0])
        held = pages2[40:]
        held_lab = label("held out", color=YELLOW)
        pred_lab = formula(r"\text{score} = p(\text{their words}\mid\text{model})", size=40)
        with self.narrate("So how do you choose? The usual score is held-out likelihood: hide "
                          "some articles, and check how well the model predicts their words. "
                          "Chang and colleagues added a test with human readers.") as beat:
            self.play(LaggedStart(*[FadeIn(p, shift=0.1 * DOWN) for p in pages2],
                                  lag_ratio=0.02), run_time=beat.until("hide", offset=-0.2))
            self.play(held.animate.shift(RIGHT * 1.6).set_stroke(YELLOW).set_fill(YELLOW, 0.15),
                      run_time=beat.until("check", offset=-0.2))
            held_lab.next_to(held, DOWN, buff=0.25)
            self.play(FadeIn(held_lab), run_time=0.6)
            pred_lab.next_to(pages2, DOWN, buff=0.9).set_x(0)
            self.play(Write(pred_lab), run_time=beat.until("Chang", offset=-0.2))
            cite_chang2 = citation("Chang, Gerrish, Wang, Boyd-Graber & Blei, 2009 · NIPS")
            self.play(FadeIn(cite_chang2), run_time=beat.remaining(0.8))

        # ============================================================ 13 word intrusion
        words5 = ["committee", "legislation", "proposal", "republican", "taxis"]
        chips = VGroup()
        for w in words5:
            t = text(w, size=30)
            chips.add(VGroup(RoundedRectangle(width=t.width + 0.4, height=0.7, corner_radius=0.12,
                                              stroke_color=GRAY, stroke_width=2), t))
        plant_t = text("planted", size=26, color=GRAY, slant=ITALIC)
        plant = VGroup(DashedVMobject(RoundedRectangle(width=plant_t.width + 0.4, height=0.7,
                                                       corner_radius=0.12, stroke_color=GRAY,
                                                       stroke_width=2), num_dashes=24), plant_t)
        row = VGroup(*chips, plant).arrange(RIGHT, buff=0.25).move_to([0, 0.2, 0])
        fit(row, width=12.4)
        src = label("one topic's top words · NYT, 50-topic LDA", size=26, color=GRAY).next_to(
            row, UP, buff=0.4)
        readers = VGroup(*[Dot(radius=0.12, color=INK) for _ in range(8)]).arrange(RIGHT, buff=0.3)
        readers.move_to([0, 2.6, 0])
        readers_lab = label("8 readers", size=26, color=GRAY).next_to(readers, LEFT, buff=0.3)
        taxis = chips[4]
        seven = formula(r"7/8", r"\text{ picked taxis}", size=40).next_to(row, DOWN, buff=0.55)
        seven[0].set_color(YELLOW)
        own = label("the model's own top word", size=26, color=PURPLE)
        at_most = formula(r"\le 1/8", r"\text{ found the planted word}", size=40)
        at_most[0].set_color(RED)
        with self.narrate("Show people a topic's top words with one planted intruder, and see "
                          "if they can find it. For this New York Times topic, seven of eight "
                          "readers picked taxis. But taxis was the model's own word, so at most "
                          "one in eight found the plant.") as beat:
            self.play(FadeOut(VGroup(pages2, held_lab, pred_lab)),
                      LaggedStart(*[FadeIn(c, shift=0.1 * UP) for c in row], lag_ratio=0.12),
                      run_time=beat.until("planted", offset=-0.1))
            self.play(Indicate(plant, color=YELLOW, scale_factor=1.1),
                      run_time=beat.until("see", offset=-0.1))
            self.play(FadeIn(readers, lag_ratio=0.1), FadeIn(readers_lab),
                      run_time=beat.until("For this", offset=-0.2))
            self.play(FadeIn(src, shift=0.1 * DOWN), run_time=beat.until("seven", offset=-0.2))
            # seven readers drop onto "taxis", one does not
            targets = [taxis.get_top() + UP * 0.35 + RIGHT * (k - 3) * 0.26 for k in range(7)]
            self.play(*[readers[k].animate.move_to(targets[k]).set_color(YELLOW)
                        for k in range(7)], readers[7].animate.set_opacity(0.35),
                      taxis[0].animate.set_stroke(YELLOW, width=3),
                      run_time=beat.until("taxis", offset=-0.2))
            self.play(Write(seven), run_time=beat.until("But", offset=-0.1))
            own.next_to(seven, DOWN, buff=0.35)
            self.play(Create(underline(taxis, color=PURPLE)), FadeIn(own, shift=0.1 * UP),
                      run_time=beat.until("so at most", offset=-0.1))
            at_most.move_to(own)
            self.play(FadeOut(own, shift=0.1 * UP), FadeIn(at_most, shift=0.1 * UP),
                      Indicate(plant, color=RED, scale_factor=1.1),
                      run_time=beat.remaining(1.0))

        # ============================================================ 14 the verdict
        lab1b, m1b, lab2b, m2b = self.ineq_rows(">", "?")
        lt = formula(r"<", size=64, color=YELLOW).move_to(m2b[1])
        usually = text("usually, across their tests", size=22, color=GRAY).next_to(
            VGroup(m1b, m2b), DOWN, buff=0.45)
        with self.narrate("Across their tests, the correlated topic model usually beat LDA at "
                          "predicting held-out text, and usually lost to it with readers.") as beat:
            self.play(FadeOut(VGroup(*[m for m in self.mobjects if m is not cite_chang2])),
                      run_time=0.6)
            self.play(FadeIn(lab1b), FadeIn(m1b), FadeIn(lab2b), FadeIn(m2b),
                      run_time=beat.until("beat", offset=-0.2))
            self.play(Indicate(m1b[1], color=YELLOW, scale_factor=1.3),
                      run_time=beat.until("lost", offset=-0.3))
            self.play(ReplacementTransform(m2b[1], lt), run_time=0.9)
            self.play(FadeIn(usually), run_time=beat.remaining(0.8))

        # ============================================================ 15 landing
        with self.narrate("So the answer to the opening question is no. A topic model finds "
                          "words that travel together; deciding which of those patterns is a "
                          "topic still takes a reader.") as beat:
            self.play(flag(lt), run_time=beat.until("no", offset=-0.1, min_time=0.6))
            self.play(Indicate(lab2b, color=YELLOW, scale_factor=1.05),
                      run_time=beat.until("deciding", offset=-0.1))
            self.play(Circumscribe(VGroup(lab2b, m2b), color=YELLOW, buff=0.15),
                      run_time=beat.remaining(1.0))
        self.end_card()
