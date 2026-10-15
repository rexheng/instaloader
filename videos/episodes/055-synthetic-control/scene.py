"""Episode 55 - Building a Fake California to Measure a Real Law (synthetic control).

Data: per-capita cigarette sales, 39 US states, 1970-2000 (Abadie, Diamond & Hainmueller 2010,
via the synthdid package's california_prop99.csv).  Synthetic-California weights are the
paper's Table 2.  Placebo gaps: our own outcome-only re-fit (data/placebo_fit.py).
"""
import csv
from pathlib import Path

import numpy as np
from manim import *
from sample_space import *

HERE = Path(__file__).resolve().parent
YEARS = np.arange(1970, 2001)
PRE = YEARS <= 1988


def load():
    rows = list(csv.DictReader(open(HERE / "data" / "prop99.csv"), delimiter=";"))
    states = {}
    for r in rows:
        states.setdefault(r["State"], {})[int(r["Year"])] = float(r["PacksPerCapita"])
    return {s: np.array([v[y] for y in YEARS]) for s, v in states.items()}


DATA = load()
CA = DATA["California"]
DONORS = {s: v for s, v in DATA.items() if s != "California"}
AVG = np.mean(np.array(list(DONORS.values())), axis=0)          # unweighted, 38 states
MT = DONORS["Montana"]
WEIGHTS = [("Utah", 0.334), ("Nevada", 0.234), ("Montana", 0.199), ("Colorado", 0.164),
           ("Connecticut", 0.069)]                               # ADH 2010, Table 2
SYN = sum(w * DONORS[s] for s, w in WEIGHTS)
GAP = CA - SYN


def rmspe(a):
    return float(np.sqrt(np.mean((CA[PRE] - a[PRE]) ** 2)))


MISS_AVG, MISS_MT, MISS_SYN = rmspe(AVG), rmspe(MT), rmspe(SYN)   # 16.0, 4.5, 1.8

PZ = np.load(HERE / "data" / "placebos.npz", allow_pickle=True)
_names = list(PZ["gap_names"])
_ca_mspe = float(np.mean(GAP[PRE] ** 2))                          # ~3.1 (paper: "about 3")
PLACEBOS = [PZ["gaps"][i] for i, n in enumerate(_names)
            if n != "California" and PZ["prerm"][i] ** 2 <= 2 * _ca_mspe]

assert abs(GAP[-1] + 25.7) < 0.1 and abs(MISS_AVG - 16.0) < 0.1 and len(PLACEBOS) == 22
assert min(p[-1] for p in PLACEBOS) > GAP[-1]

X0, Y_LO, Y_HI = 1970, 30, 150


def chart(y_range, y_step, y_title, x_length=7.2, y_length=4.8):
    ax = Axes(x_range=(1970, 2000, 10), y_range=(y_range[0], y_range[1], y_step),
              x_length=x_length, y_length=y_length,
              axis_config=dict(color=GRAY, stroke_width=2.5, include_tip=False, tick_size=0.06))
    ax.move_to([-5.95 + x_length / 2, 0.2, 0])
    xl = VGroup(*[MathTex(str(v), font_size=MATH_SMALL, color=GRAY)
                  .next_to(ax.c2p(v, y_range[0]), DOWN, buff=0.2) for v in (1970, 1980, 1990, 2000)])
    ys = np.arange(y_range[0], y_range[1] + 1e-9, y_step)
    yl = VGroup(*[MathTex(f"{int(v)}".replace("-", "-"), font_size=MATH_SMALL, color=GRAY)
                  .next_to(ax.c2p(1970, v), LEFT, buff=0.18) for v in ys])
    yt = text(y_title, size=LABEL, color=GRAY).next_to(ax.c2p(1970, y_range[1]), UP, buff=0.25)
    yt.align_to(yl, LEFT)
    xt = text("year", size=LABEL, color=GRAY).next_to(xl[-1], RIGHT, buff=0.25)
    ax.labels = VGroup(xl, yl, yt, xt)
    ax.ylo, ax.yhi = y_range
    return ax


def polyline(ax, years, ys, color, width=4.0, opacity=1.0):
    """Polyline in data coords, clipped to the axes' y range (pieces kept as subpaths)."""
    lo, hi = ax.ylo, ax.yhi
    m = VMobject(stroke_color=color, stroke_width=width, stroke_opacity=opacity)
    seg = []

    def flush():
        if len(seg) >= 2:
            m.start_new_path(seg[0])
            m.add_points_as_corners(seg[1:])
        seg.clear()

    for i in range(len(years)):
        x, y = years[i], ys[i]
        inside = lo <= y <= hi
        if i > 0:
            px, py = years[i - 1], ys[i - 1]
            pin = lo <= py <= hi
            if pin != inside:
                edge = hi if (y > hi or py > hi) else lo
                t = (edge - py) / (y - py)
                seg.append(ax.c2p(px + t * (x - px), edge))
                if not inside:
                    flush()
        if inside:
            seg.append(ax.c2p(x, y))
    flush()
    return m


def segment(ax, ys, y0, y1, color, width=4.0, opacity=1.0):
    k = (YEARS >= y0) & (YEARS <= y1)
    return polyline(ax, YEARS[k], ys[k], color, width, opacity)


def dashed(m, n=None):
    n = n or max(8, int(m.get_arc_length() / 0.16))
    return DashedVMobject(m, num_dashes=n, dashed_ratio=0.55)


def band(ax, a, b, y0, y1, color, opacity=0.28):
    k = (YEARS >= y0) & (YEARS <= y1)
    pts = [ax.c2p(x, y) for x, y in zip(YEARS[k], a[k])] + \
          [ax.c2p(x, y) for x, y in zip(YEARS[k][::-1], b[k][::-1])]
    return Polygon(*pts, stroke_width=0, fill_color=color, fill_opacity=opacity)


def vbrace(ax, x, y_top, y_bot, color, label_tex, side=RIGHT, size=MATH):
    p0, p1 = ax.c2p(x, y_top), ax.c2p(x, y_bot)
    ln = Line(p0, p1)
    br = Brace(ln, direction=side, buff=0.08, color=color, sharpness=1.2)
    lab = MathTex(label_tex, font_size=size, color=color).next_to(br, side, buff=0.12)
    return VGroup(br, lab)


class Episode(NarratedScene):
    EPISODE = 55
    TITLE = "Building a Fake California to Measure a Real Law"
    PRONUNCIATIONS = {"Hainmueller": "hine myoo ler", "Abadie": "ah bah dee"}

    def construct(self):
        ax = chart((Y_LO, Y_HI), 30, "packs per person")
        ca_pre = segment(ax, CA, 1970, 1988, BLUE, 5)
        ca_post = segment(ax, CA, 1988, 2000, BLUE, 5)
        ca_line = VGroup(ca_pre, ca_post)
        ca_tag = text("California", size=LABEL, color=BLUE).next_to(ax.c2p(1980, CA[10]), DOWN, buff=0.25)
        law_x = ax.c2p(1988, 0)[0]
        law = DashedLine([law_x, ax.c2p(0, Y_LO)[1], 0], [law_x, ax.c2p(0, Y_HI)[1], 0],
                         color=GRAY, stroke_width=2, dash_length=0.08)
        law_tag = text("Prop 99", size=LABEL, color=GRAY).next_to(law, UP, buff=0.12)
        d88 = Dot(ax.c2p(1988, CA[18]), radius=0.07, color=BLUE)
        d00 = Dot(ax.c2p(2000, CA[-1]), radius=0.07, color=BLUE)
        v88 = MathTex("90.1", font_size=MATH_SMALL + 4, color=BLUE).next_to(d88, UR, buff=0.08)
        v00 = MathTex("41.6", font_size=MATH_SMALL + 4, color=BLUE).next_to(d00, DOWN, buff=0.15)
        guide = DashedLine(ax.c2p(1988, CA[18]), ax.c2p(2001.2, CA[18]), color=GRAY,
                           stroke_width=1.5, dash_length=0.06)
        drop = vbrace(ax, 2001.2, CA[18], CA[-1], INK, r"48.5", size=MATH)
        q = MathTex(r"\text{law?}", font_size=MATH, color=YELLOW).next_to(drop, DOWN, buff=0.2)

        # ---------------------------------------------------------------- 1 cold open
        with self.narrate("This blue line is cigarette sales in California, in packs per person "
                          "per year. In nineteen eighty-eight, voters passed Proposition ninety-nine: "
                          "a twenty-five cent tax on every pack, plus anti-smoking campaigns. By two "
                          "thousand, sales had fallen from ninety packs to about forty-two. That's a "
                          "drop of almost forty-nine packs. How many of them did the law cause? "
                          "[pause 1.5]") as beat:
            self.play(Create(ax), FadeIn(ax.labels), run_time=0.9)
            self.play(Create(ca_pre), FadeIn(ca_tag, shift=0.1 * UP),
                      run_time=beat.until("In nineteen", offset=-0.1), rate_func=LINEAR)
            self.play(Create(law), FadeIn(law_tag), FadeIn(d88), run_time=beat.until("twenty-five"))
            self.play(Create(ca_post), run_time=beat.until("ninety packs", offset=-0.1), rate_func=LINEAR)
            self.play(FadeIn(v88, scale=0.8), flag(d88), run_time=0.7)
            self.play(FadeIn(d00), FadeIn(v00, scale=0.8), run_time=beat.until("That's", offset=-0.2))
            self.play(Create(guide), GrowFromEdge(drop[0], UP), run_time=0.8)
            self.play(Write(drop[1]), run_time=0.5)
            beat.wait_until("How many", offset=-0.1)
            self.play(FadeIn(q, shift=0.1 * DOWN), run_time=0.6)

        # ---------------------------------------------------------------- 2 stakes
        stub = dashed(Line(ax.c2p(1988, CA[18]), ax.c2p(1992, 84)), 6).set_color(YELLOW).set_stroke(width=4)
        stub_q = MathTex("?", font_size=EQ, color=YELLOW).next_to(stub, RIGHT, buff=0.1).shift(UP * 0.1)
        hi76 = segment(ax, CA, 1976, 1988, YELLOW, 7)
        with self.narrate("Sales were already falling before the law, so part of that drop would have "
                          "happened anyway. To split it, you need a California that never passed the "
                          "law. Nobody can observe that one, so we have to build it.") as beat:
            beat.wait_until("already", offset=-0.2)
            self.play(Create(hi76), run_time=1.2)
            self.play(FadeOut(hi76), run_time=0.6)
            beat.wait_until("you need", offset=-0.1)
            self.play(Create(stub), FadeIn(stub_q), run_time=1.0)
            beat.wait_until("Nobody", offset=-0.1)
            self.play(stub.animate.set_stroke(opacity=0.3), stub_q.animate.set_opacity(0.3), run_time=0.8)
            beat.wait_until("build", offset=-0.2)
            self.play(FadeOut(stub), FadeOut(stub_q), FadeOut(q), FadeOut(drop), FadeOut(guide),
                      FadeOut(v00), run_time=0.8)

        # ---------------------------------------------------------------- 3 naive v1
        avg_line = polyline(ax, YEARS, AVG, PURPLE, 4)
        avg_tag = text("average of 38", size=LABEL, color=PURPLE).next_to(ax.c2p(1981, AVG[11]), UP, buff=0.15)
        gap_avg = vbrace(ax, 2000.4, AVG[-1], CA[-1], GREEN, r"50.5")
        with self.narrate("First try: the average of thirty-eight states with no big tobacco program. "
                          "By two thousand, this purple line sits fifty packs above California, more "
                          "than the whole drop.") as beat:
            self.play(Create(avg_line), FadeIn(avg_tag), run_time=beat.until("By two", offset=-0.2),
                      rate_func=LINEAR)
            beat.wait_until("this purple", offset=-0.1)
            self.play(flag(avg_line, color=PURPLE), run_time=0.8)
            beat.wait_until("fifty", offset=-0.3)
            self.play(GrowFromEdge(gap_avg[0], UP), FadeIn(gap_avg[1]), run_time=0.8)

        # ---------------------------------------------------------------- 4 fail
        red_avg = band(ax, AVG, CA, 1970, 1988, RED)
        tick70 = Line(ax.c2p(1970, CA[0]), ax.c2p(1970, AVG[0]), color=RED, stroke_width=5)
        tick88 = Line(ax.c2p(1988, CA[18]), ax.c2p(1988, AVG[18]), color=RED, stroke_width=5)
        t70 = MathTex("2.9", font_size=MATH_SMALL + 4, color=RED).next_to(ax.c2p(1970, AVG[0]), UR, buff=0.12)
        t88 = MathTex("23.7", font_size=MATH_SMALL + 4, color=RED).next_to(tick88, RIGHT, buff=0.12)
        shift = (AVG[18] - CA[18]) * ax.y_axis.unit_size
        avg_shift = segment(ax, AVG, 1970, 1988, PURPLE, 4).shift(DOWN * shift)
        miss70 = Line(ax.c2p(1970.4, CA[0]), ax.c2p(1970.4, AVG[0] - (AVG[18] - CA[18])),
                      color=RED, stroke_width=5)
        m70 = MathTex("26.6", font_size=MATH_SMALL + 4, color=RED).next_to(miss70, RIGHT, buff=0.12)
        with self.narrate("But look before the law. In nineteen seventy, the two lines nearly touch. By "
                          "nineteen eighty-eight, they're twenty-four packs apart. They were drifting "
                          "apart before the law existed. Shift the purple line down to match in "
                          "eighty-eight, and it misses nineteen seventy by twenty-seven.") as beat:
            self.play(FadeOut(v88), gap_avg.animate.set_opacity(0.35), run_time=0.6)
            beat.wait_until("In nineteen", offset=-0.1)
            self.play(Create(tick70), FadeIn(t70), run_time=0.8)
            beat.wait_until("By", offset=-0.1)
            self.play(Create(tick88), FadeIn(t88), run_time=0.8)
            beat.wait_until("drifting", offset=-0.2)
            self.play(FadeIn(red_avg), run_time=1.0)
            beat.wait_until("Shift", offset=-0.1)
            self.play(FadeOut(tick70), FadeOut(t70), FadeOut(tick88), FadeOut(t88), run_time=0.4)
            self.play(TransformFromCopy(segment(ax, AVG, 1970, 1988, PURPLE, 4), avg_shift),
                      run_time=beat.until("and it misses", offset=-0.1))
            self.play(Create(miss70), FadeIn(m70), run_time=0.8)

        # ---------------------------------------------------------------- 5 metric / scoreboard
        hx = [2.0, 4.75, 5.85]
        h_miss = text("miss", size=LABEL, color=RED).move_to([hx[1], 3.3, 0])
        h_eff = text("effect", size=LABEL, color=GREEN).move_to([hx[2], 3.3, 0])
        h_rule = Line([hx[0], 3.02, 0], [6.35, 3.02, 0], color=DIM, stroke_width=1.5)
        row_y = [2.6, 2.05, 1.5]

        def row_name(i, s, color, dash=False):
            sw = Line(ORIGIN, RIGHT * 0.38, color=color, stroke_width=5)
            if dash:
                sw = dashed(sw, 3).set_color(color)
            nm = text(s, size=LABEL, color=INK)
            g = VGroup(sw, nm).arrange(RIGHT, buff=0.15)
            return g.move_to([hx[0], row_y[i], 0], aligned_edge=LEFT)

        def num(v, color, i, col, dec=1):
            m = DecimalNumber(v, num_decimal_places=dec, font_size=MATH, color=color)
            return m.move_to([hx[col], row_y[i], 0])

        r1 = row_name(0, "average", PURPLE)
        miss1 = num(0, RED, 0, 1)
        eff1 = num(50.5, GREEN, 0, 2, 0)
        with self.narrate("So score every comparison by its typical miss before the law. The average "
                          "misses by sixteen packs, before anything happened.") as beat:
            self.play(FadeOut(avg_shift), FadeOut(miss70), FadeOut(m70),
                      FadeIn(h_miss), FadeIn(h_eff), Create(h_rule), FadeIn(r1), run_time=1.0)
            beat.wait_until("typical", offset=-0.2)
            self.play(Indicate(red_avg, color=RED, scale_factor=1.0), FadeIn(miss1), run_time=0.8)
            beat.wait_until("sixteen", offset=-0.9)
            self.play(ChangeDecimalToValue(miss1, MISS_AVG), run_time=0.9)
            self.play(ReplacementTransform(gap_avg[1].copy().set_opacity(1), eff1),
                      FadeOut(gap_avg), run_time=0.9)

        # ---------------------------------------------------------------- 6 naive v2: Montana
        mt_line = polyline(ax, YEARS, MT, PURPLE, 4)
        mt_tag = text("Montana", size=LABEL, color=PURPLE).next_to(ax.c2p(1971, MT[1]), DOWN, buff=0.2)
        red_mt = band(ax, MT, CA, 1970, 1988, RED)
        r2 = row_name(1, "Montana", PURPLE)
        miss2 = num(0, RED, 1, 1)
        gap_mt = vbrace(ax, 2000.4, MT[-1], CA[-1], GREEN, r"33.9")
        eff2 = num(33.9, GREEN, 1, 2, 0)
        lo70 = Line(ax.c2p(1970, CA[0]), ax.c2p(1970, MT[0]), color=RED, stroke_width=5)
        hi82 = Line(ax.c2p(1982, CA[12]), ax.c2p(1982, MT[12]), color=RED, stroke_width=5)
        with self.narrate("Second try: the one state closest to California before the law, Montana. "
                          "The miss drops to four and a half packs. But Montana runs twelve packs low in "
                          "nineteen seventy and seven high in eighty-two, and it would credit the law "
                          "with thirty-four packs.") as beat:
            self.play(FadeOut(red_avg), FadeOut(avg_tag), avg_line.animate.set_stroke(opacity=0.25),
                      FadeIn(r2), run_time=0.8)
            self.play(Create(mt_line), FadeIn(mt_tag), run_time=beat.until("Montana", offset=-0.2),
                      rate_func=LINEAR)
            beat.wait_until("The miss", offset=-0.1)
            self.play(FadeIn(red_mt), FadeIn(miss2), run_time=0.6)
            self.play(ChangeDecimalToValue(miss2, MISS_MT), run_time=beat.until("packs", offset=0.2))
            beat.wait_until("twelve", offset=-0.2)
            self.play(Create(lo70), run_time=0.6)
            beat.wait_until("seven", offset=-0.2)
            self.play(Create(hi82), run_time=0.6)
            beat.wait_until("credit", offset=-0.2)
            self.play(GrowFromEdge(gap_mt[0], UP), FadeIn(gap_mt[1]), run_time=0.8)
            self.play(ReplacementTransform(gap_mt[1].copy(), eff2), FadeOut(gap_mt),
                      run_time=beat.remaining(0.8))

        # ---------------------------------------------------------------- 7 blend: weights
        donor_lines = {s: polyline(ax, YEARS[PRE], v[PRE], GRAY, 1.2, 0.45) for s, v in DONORS.items()}
        donors = allow_overlap(VGroup(*donor_lines.values()))
        wy0, wdy = 0.75, 0.46
        wrows = VGroup()
        for i, (s, w) in enumerate(WEIGHTS):
            nm = text(s, size=LABEL, color=INK).move_to([hx[0], wy0 - i * wdy, 0], aligned_edge=LEFT)
            bar = Rectangle(width=w * 5.0, height=0.24, stroke_width=0, fill_color=YELLOW, fill_opacity=0.9)
            bar.move_to([3.85, wy0 - i * wdy, 0], aligned_edge=LEFT)
            val = MathTex(f"{w:.3f}"[1:], font_size=MATH_SMALL,
                          color=YELLOW).next_to(bar, RIGHT, buff=0.1)
            wrows.add(VGroup(nm, bar, val))
        chosen = VGroup(*[donor_lines[s] for s, _ in WEIGHTS])
        with self.narrate("So blend states instead. Give each state a weight, none below zero, all "
                          "adding up to one. Then pick the weights that make the blend track California "
                          "before the law, in sales, and in price, income, age and beer drinking. Five "
                          "states get weight: Utah a third, Nevada and Montana about a fifth each, "
                          "Colorado and Connecticut the rest.") as beat:
            self.play(FadeOut(red_mt), FadeOut(lo70), FadeOut(hi82), FadeOut(mt_line), FadeOut(mt_tag),
                      FadeOut(avg_line), FadeOut(ca_post), FadeOut(d00), run_time=0.8)
            self.play(LaggedStart(*[Create(m) for m in donors], lag_ratio=0.04),
                      run_time=beat.until("Give", offset=-0.1))
            beat.wait_until("weight", offset=-0.2)
            for r in wrows:
                r[1].stretch(0.001, 0, about_edge=LEFT)
            self.play(LaggedStart(*[FadeIn(r[0]) for r in wrows], lag_ratio=0.15), run_time=1.2)
            beat.wait_until("pick", offset=-0.2)
            self.play(LaggedStart(*[r[1].animate.stretch(1000, 0, about_edge=LEFT) for r in wrows],
                                  lag_ratio=0.1),
                      LaggedStart(*[m.animate.set_stroke(color=INK, width=2.6, opacity=0.9) for m in chosen],
                                  lag_ratio=0.1),
                      *[m.animate.set_stroke(opacity=0.18) for s, m in donor_lines.items()
                        if s not in dict(WEIGHTS)],
                      run_time=beat.until("Five", offset=-0.2))
            for i, (s, w) in enumerate(WEIGHTS):
                cue = {0: "Utah", 1: "Nevada", 2: "Montana", 3: "Colorado", 4: "Connecticut"}[i]
                beat.wait_until(cue, offset=-0.15)
                self.play(FadeIn(wrows[i][2]), flag(wrows[i][0]),
                          donor_lines[s].animate.set_stroke(width=2 + 10 * w), run_time=0.5)

        # ---------------------------------------------------------------- 8 formula
        syn_pre = dashed(segment(ax, SYN, 1970, 1988, YELLOW, 5)).set_color(YELLOW)
        f = MathTex(r"\hat{Y}_t", "=", r"\sum_j", "w_j", r"\,Y_{j,t}", font_size=EQ)
        f.move_to([4.15, -1.75, 0])
        f[0].set_color(YELLOW)
        f[3].set_color(YELLOW)
        cons = MathTex(r"w_j \ge 0,\quad \textstyle\sum_j w_j = 1", font_size=MATH, color=GRAY)
        cons.next_to(f, DOWN, buff=0.3)
        d88s = Dot(ax.c2p(1988, SYN[18]), radius=0.07, color=YELLOW)
        v88s = MathTex("91.7", font_size=MATH_SMALL + 4, color=YELLOW).next_to(d88s, UP, buff=0.12).shift(LEFT * 0.4)
        v88c = MathTex("90.1", font_size=MATH_SMALL + 4, color=BLUE).next_to(d88, DOWN, buff=0.12).shift(LEFT * 0.4)
        r3 = row_name(2, "blend", YELLOW, dash=True)
        miss3 = num(0, RED, 2, 1)
        with self.narrate("For each year, the blend is every state's sales times its weight, added up. "
                          "In nineteen eighty-eight, that gives ninety-one point seven, against "
                          "California's ninety point one. Across all nineteen years before the law, the "
                          "miss is under two packs.") as beat:
            self.play(Write(f[0:2]), run_time=0.6)
            beat.wait_until("sales", offset=-0.2)
            self.play(TransformFromCopy(chosen, f[4]), Write(f[2]), run_time=1.0)
            beat.wait_until("weight", offset=-0.2)
            self.play(TransformFromCopy(VGroup(*[r[2] for r in wrows]), f[3]), run_time=1.0)
            beat.wait_until("added", offset=-0.2)
            self.play(TransformFromCopy(chosen, syn_pre), FadeIn(cons, shift=0.1 * UP),
                      donors.animate.set_stroke(opacity=0.12), run_time=1.3)
            beat.wait_until("ninety-one", offset=-0.3)
            self.play(FadeIn(d88s), FadeIn(v88s), run_time=0.6)
            beat.wait_until("California's", offset=-0.2)
            self.play(FadeIn(v88c), flag(d88), run_time=0.6)
            beat.wait_until("Across", offset=-0.2)
            self.play(FadeOut(donors), FadeIn(r3), FadeIn(miss3), run_time=0.8)
            self.play(ChangeDecimalToValue(miss3, MISS_SYN), run_time=beat.until("packs", offset=0.1))
            self.play(flag(miss3, color=RED), run_time=0.8)

        # ---------------------------------------------------------------- 9 prediction + reveal
        syn_post = dashed(segment(ax, SYN, 1988, 2000, YELLOW, 5)).set_color(YELLOW)
        green = band(ax, SYN, CA, 1988, 2000, GREEN, 0.3)
        gap_syn = vbrace(ax, 2000.4, SYN[-1], CA[-1], GREEN, r"25.7")
        eff3 = num(25.7, GREEN, 2, 2, 0)
        e = MathTex(r"\text{effect}_t", "=", r"Y_{\text{CA},t}", "-", r"\hat{Y}_t", font_size=EQ)
        e[0].set_color(GREEN)
        e[2].set_color(BLUE)
        e[4].set_color(YELLOW)
        with self.narrate("Those weights only ever saw the years before the law. Now run the blend "
                          "forward. [pause 1.5] The blend keeps sliding slowly. California falls away "
                          "from it. By two thousand, the gap is twenty-six packs.") as beat:
            self.play(FadeOut(v88s), FadeOut(v88c), FadeOut(d88s), wrows.animate.set_opacity(0.0),
                      Indicate(law, color=YELLOW, scale_factor=1.0), run_time=0.9)
            self.remove(wrows)
            self.play(VGroup(f, cons).animate.shift(UP * 1.9), run_time=0.8)
            e.next_to(cons, DOWN, buff=0.45).align_to(f, LEFT)
            beat.wait_until("forward", offset=0.3)
            self.play(Flash(d88, color=YELLOW, line_length=0.15, flash_radius=0.25), run_time=0.8)
            beat.wait_until("The blend keeps", offset=-0.1)
            self.play(Create(syn_post), run_time=beat.until("California", offset=-0.1), rate_func=LINEAR)
            self.play(Create(ca_post), run_time=beat.until("By two", offset=-0.1), rate_func=LINEAR)
            self.play(FadeIn(green), GrowFromEdge(gap_syn[0], UP), FadeIn(gap_syn[1]), FadeIn(d00),
                      run_time=0.9)
            self.play(TransformFromCopy(gap_syn[1], eff3), run_time=0.9)
            self.play(Write(e[1]), Write(e[3]), TransformFromCopy(green, e[0]),
                      TransformFromCopy(ca_post, e[2]), TransformFromCopy(f[0], e[4]),
                      run_time=beat.remaining(1.2))

        # ---------------------------------------------------------------- 10 placebos
        self.hold(0.4)
        gx = chart((-30, 30), 15, "gap from own blend (packs)")
        zero = polyline(gx, YEARS, np.zeros_like(GAP), YELLOW, 3)
        zero_d = dashed(zero).set_color(YELLOW)
        gap_line = polyline(gx, YEARS, GAP, BLUE, 5)
        law2 = DashedLine(gx.c2p(1988, -30), gx.c2p(1988, 30), color=GRAY, stroke_width=2, dash_length=0.08)
        law2_tag = text("Prop 99", size=LABEL, color=GRAY).next_to(law2, UP, buff=0.12)
        plac = VGroup(*[polyline(gx, YEARS, p, GRAY, 1.6, 0.6) for p in PLACEBOS])
        ca_end = Dot(gx.c2p(2000, GAP[-1]), radius=0.07, color=BLUE)
        ca_lab = text("California", size=LABEL, color=BLUE).next_to(ca_end, RIGHT, buff=0.15)
        note = VGroup(text("gray: 22 other states", size=LABEL, color=GRAY),
                      text("each vs its own blend", size=LABEL, color=GRAY),
                      text("(our re-fit, sales only)", size=SMALL, color=GRAY)).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        note.move_to([4.25, 2.3, 0])
        with self.narrate("Could any state drift twenty-six packs from its blend by chance? Give each of "
                          "the other states its own blend, and pretend it passed a law in nineteen "
                          "eighty-eight. Of the twenty-two states fit about as well as California, none "
                          "ends as low.") as beat:
            self.play(FadeOut(VGroup(h_miss, h_eff, h_rule, r1, r2, r3, miss1, miss2, miss3, eff1, eff2,
                                     eff3, f, cons, e, green, gap_syn, d00, d88, ca_tag)),
                      run_time=0.8)
            self.play(ReplacementTransform(ax, gx), ReplacementTransform(ax.labels, gx.labels),
                      ReplacementTransform(VGroup(syn_pre, syn_post), zero_d),
                      ReplacementTransform(ca_line, gap_line),
                      ReplacementTransform(law, law2), ReplacementTransform(law_tag, law2_tag),
                      run_time=beat.until("Give", offset=-0.2))
            self.play(FadeIn(note[:2]), run_time=0.6)
            self.play(LaggedStart(*[Create(p) for p in plac], lag_ratio=0.06),
                      FadeIn(note[2]), run_time=beat.until("Of the", offset=-0.1))
            self.bring_to_front(gap_line)
            self.play(FadeIn(ca_end), FadeIn(ca_lab), flag(gap_line, color=BLUE), run_time=1.0)
            beat.wait_until("none", offset=-0.2)
            low = min(p[-1] for p in PLACEBOS)
            mark = DashedLine(gx.c2p(1996, low), gx.c2p(2000, low), color=GRAY, stroke_width=2,
                              dash_length=0.06)
            self.play(Create(mark), run_time=0.7)

        # ---------------------------------------------------------------- 11 payoff + limit
        cite = citation("Abadie, Diamond & Hainmueller, 2010 · JASA")
        stat = MathTex(r"\tfrac{1}{39}", r"\approx 0.026", font_size=EQ, color=INK)
        stat.move_to([4.2, 1.2, 0])
        stat_lab = text("if the law did nothing", size=LABEL, color=GRAY).next_to(stat, DOWN, buff=0.25)
        post_zone = Rectangle(width=gx.c2p(2000, 0)[0] - gx.c2p(1988, 0)[0],
                              height=gx.y_axis.get_length(), stroke_width=0, fill_color=GRAY,
                              fill_opacity=0.12).move_to(gx.c2p(1994, 0))
        shock = VGroup(text("or a shock that", size=LABEL, color=INK),
                       text("hit only California?", size=LABEL, color=INK)).arrange(DOWN, buff=0.1)
        shock.move_to([4.2, -1.3, 0])
        with self.narrate("Abadie, Diamond and Hainmueller ran this test in twenty ten. Measured against "
                          "how well each state fit before the law, California's gap was the largest of "
                          "thirty-nine: a one in thirty-nine chance if the law did nothing. A good fit to "
                          "the past can't rule out some other shock that hit only California after "
                          "nineteen eighty-eight.") as beat:
            self.play(FadeOut(note), FadeOut(mark), FadeIn(cite), run_time=0.8)
            beat.wait_until("largest", offset=-0.2)
            self.play(flag(gap_line, color=BLUE), run_time=0.8)
            beat.wait_until("one in", offset=-0.2)
            self.play(Write(stat[0]), run_time=0.8)
            self.play(Write(stat[1]), FadeIn(stat_lab), run_time=0.8)
            beat.wait_until("A good", offset=-0.1)
            self.play(plac.animate.set_stroke(opacity=0.3), FadeIn(post_zone), run_time=0.8)
            beat.wait_until("other shock", offset=-0.1)
            self.play(FadeIn(shock, shift=0.1 * UP), run_time=0.8)

        # ---------------------------------------------------------------- 12 landing
        ax2 = chart((Y_LO, Y_HI), 30, "packs per person")
        ca2 = polyline(ax2, YEARS, CA, BLUE, 5)
        syn2 = dashed(polyline(ax2, YEARS, SYN, YELLOW, 5)).set_color(YELLOW)
        law3 = DashedLine([law_x, ax2.c2p(0, Y_LO)[1], 0], [law_x, ax2.c2p(0, Y_HI)[1], 0],
                          color=GRAY, stroke_width=2, dash_length=0.08)
        law3_tag = text("Prop 99", size=LABEL, color=GRAY).next_to(law3, UP, buff=0.12)
        guide2 = DashedLine(ax2.c2p(1988, CA[18]), ax2.c2p(2001.2, CA[18]), color=GRAY,
                            stroke_width=1.5, dash_length=0.06)
        drop2 = vbrace(ax2, 2001.2, CA[18], CA[-1], INK, r"48.5")
        part_a = vbrace(ax2, 2001.2, CA[18], SYN[-1], YELLOW, r"22.8")
        part_b = vbrace(ax2, 2001.2, SYN[-1], CA[-1], GREEN, r"25.7")
        lab_a = text("anyway", size=LABEL, color=YELLOW).next_to(part_a[1], RIGHT, buff=0.2)
        lab_b = text("the law", size=LABEL, color=GREEN).next_to(part_b[1], RIGHT, buff=0.2)
        green2 = band(ax2, SYN, CA, 1988, 2000, GREEN, 0.3)
        with self.narrate("So, the forty-nine packs from the start. About twenty-three would have gone "
                          "anyway: that's where the blend ends up. The other twenty-six belong to the "
                          "law, and you can only see them against a California that never voted for "
                          "it.") as beat:
            self.play(FadeOut(VGroup(plac, ca_end, ca_lab, stat, stat_lab, shock, post_zone, cite)),
                      ReplacementTransform(gx, ax2), ReplacementTransform(gx.labels, ax2.labels),
                      ReplacementTransform(gap_line, ca2), ReplacementTransform(zero_d, syn2),
                      ReplacementTransform(law2, law3), ReplacementTransform(law2_tag, law3_tag),
                      run_time=1.6)
            self.play(Create(guide2), GrowFromEdge(drop2[0], UP), Write(drop2[1]),
                      run_time=beat.until("About", offset=-0.2))
            self.play(ReplacementTransform(drop2, part_a), FadeIn(part_b), run_time=1.0)
            self.play(FadeIn(lab_a), run_time=0.5)
            beat.wait_until("ends", offset=-0.3)
            self.play(Indicate(syn2, color=YELLOW, scale_factor=1.0), run_time=0.8)
            beat.wait_until("twenty-six", offset=-0.2)
            self.play(FadeIn(green2), FadeIn(lab_b), run_time=0.8)
            beat.wait_until("never", offset=-0.2)
            self.play(syn2.animate.set_stroke(width=7), run_time=0.8)

        self.end_card()
