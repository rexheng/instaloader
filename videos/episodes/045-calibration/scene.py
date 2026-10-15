"""Episode 45 - When 90% Confident Isn't 90% Right (calibration + temperature scaling).

    videos/toolkit/render.sh --preview videos/episodes/045-calibration/scene.py Episode /tmp/e45.mp4
"""
import sys
from pathlib import Path

import numpy as np
from manim import *
from sample_space import *

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sim  # noqa: E402  (simulated data, seed 45 - see facts.md)

# ---------------------------------------------------------------- real numbers (Guo et al. 2017)
LENET_ACC, RESNET_ACC = 0.551, 0.694          # Fig. 1: error 44.9 / 30.6 on CIFAR-100
LENET_ECE, RESNET_ECE, RESNET_ECE_T = 4.85, 16.53, 1.26   # Table 1, ECE %, M = 15


def card(name, year, acc, color):
    nm = text(name, size=HEADING, color=color)
    yr = text(year, size=LABEL, color=GRAY)
    head = VGroup(nm, yr).arrange(RIGHT, buff=0.3, aligned_edge=DOWN)
    track = Rectangle(width=4.4, height=0.36, stroke_color=GRAY, stroke_width=2, fill_opacity=0)
    fill = Rectangle(width=4.4 * acc, height=0.36, stroke_width=0, fill_color=color,
                     fill_opacity=0.9).align_to(track, LEFT)
    bar = VGroup(track, fill)
    acc_lbl = text("right", size=LABEL, color=GRAY)
    pct = formula(rf"{round(acc * 100)}\%", color=color)
    row = VGroup(acc_lbl, bar, pct).arrange(RIGHT, buff=0.25)
    conf_lbl = text("confidence", size=LABEL, color=GRAY)
    q = formula(r"?", color=YELLOW)
    row2 = VGroup(conf_lbl, q).arrange(RIGHT, buff=0.3)
    g = VGroup(head, row, row2).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
    g.nm, g.yr, g.track, g.fill, g.pct, g.row, g.conf_lbl, g.q = nm, yr, track, fill, pct, row, conf_lbl, q
    return g


def soft_eq(with_T):
    lhs = MathTex(r"p_k", r"=", font_size=MATH)
    lhs[0].set_color(BLUE)
    num = MathTex(r"e^{z_k/T}" if with_T else r"e^{z_k}", font_size=MATH)
    den = MathTex(r"\sum_j e^{z_j/T}" if with_T else r"\sum_j e^{z_j}", font_size=MATH)
    if with_T:
        num[0][3:5].set_color(YELLOW)
        den[0][5:7].set_color(YELLOW)
    bar = Line(LEFT, RIGHT, stroke_width=2.5, color=INK)
    bar.set_width(max(num.width, den.width) + 0.15)
    frac = VGroup(num, bar, den).arrange(DOWN, buff=0.1)
    g = VGroup(lhs, frac).arrange(RIGHT, buff=0.2)
    g.lhs, g.num, g.bar, g.den = lhs, num, bar, den
    return g


class Episode(NarratedScene):
    EPISODE = 45
    TITLE = "When 90% Confident Isn't 90% Right"
    PRONUNCIATIONS = {
        "logits": "low jits",
        "Guo": "gwoh",
        "Pleiss": "plice",
        "Weinberger": "wine berger",
        "Ovadia": "oh vah dee uh",
        "ICML": "I C M L",
    }

    # ------------------------------------------------------------ helpers (reliability diagram)
    def col_rects(self, ax, accs, ns, confs, color, show_gap=True):
        g = VGroup()
        w = ax.x_axis.unit_size * 0.086
        for b in range(10):
            n = ns[b]
            if n == 0 or accs[b] is None or np.isnan(accs[b]):
                acc, conf, alpha = 0.0, 0.0, 0.0
            else:
                acc, conf, alpha = float(accs[b]), float(confs[b]), min(1.0, n / 150)
            x = (b + 0.5) / 10
            h = max(acc * ax.y_axis.unit_size, 0.001)
            col = Rectangle(width=w, height=h, stroke_width=0, fill_color=color,
                            fill_opacity=0.9 * alpha).move_to(ax.c2p(x, 0), aligned_edge=DOWN)
            lo, hi = min(acc, conf), max(acc, conf)
            gh = max((hi - lo) * ax.y_axis.unit_size, 0.001)
            gap = Rectangle(width=w, height=gh, stroke_color=RED, stroke_width=2 * alpha if show_gap else 0,
                            fill_color=RED, fill_opacity=(0.35 * alpha) if show_gap else 0)
            gap.move_to(ax.c2p(x, lo), aligned_edge=DOWN)
            g.add(VGroup(col, gap))
        return g

    def construct(self):
        D = sim.episode_data()
        SW = D["sweep"]
        T_STAR = D["T_star"]
        z = D["z"]

        def sweep_at(T):
            T = float(np.clip(np.round(T, 2), 1.0, 2.5))
            return SW[T]

        # ============================================================ 1 · cold open
        old = card("LeNet", "design of 1998", LENET_ACC, PURPLE)
        new = card("ResNet-110", "design of 2016", RESNET_ACC, BLUE)
        cards = VGroup(old, new).arrange(RIGHT, buff=1.0).move_to(UP * 0.5)
        fit(cards, width=SAFE_WIDTH)
        for c in (old, new):
            c.fill.save_state()
            c.fill.stretch(0.001, 0, about_edge=LEFT)
        task = text("same test: small photos, 100 categories", size=LABEL, color=GRAY)
        task.next_to(cards, UP, buff=0.6)
        cite = citation("Guo et al., 2017 · ICML · CIFAR-100")
        with self.narrate("Two networks take the same test: small photos in a hundred categories. "
                          "A design from nineteen ninety-eight gets fifty-five percent right. "
                          "A design from twenty sixteen gets sixty-nine percent.") as beat:
            self.play(FadeIn(old.nm), FadeIn(new.nm), FadeIn(old.yr), FadeIn(new.yr), run_time=0.5)
            self.play(FadeIn(task, shift=0.1 * DOWN), FadeIn(cite), run_time=beat.until("design"))
            self.play(FadeIn(VGroup(old.row[0], old.track)), run_time=0.4)
            beat.wait_until("fifty", offset=-0.5)
            self.play(Restore(old.fill), FadeIn(old.pct, shift=0.1 * LEFT), run_time=1.2)
            self.play(FadeIn(VGroup(new.row[0], new.track)), run_time=beat.until("twenty", offset=-0.1))
            beat.wait_until("sixty", offset=-0.5)
            self.play(Restore(new.fill), FadeIn(new.pct, shift=0.1 * LEFT), run_time=1.2)

        with self.narrate("Each one also tells you how sure it is. "
                          "Whose confidence would you trust? [pause 1.5]") as beat:
            self.play(FadeIn(old.row2, shift=0.1 * UP), FadeIn(new.row2, shift=0.1 * UP),
                      run_time=beat.until("Whose"))
            self.play(Circumscribe(old.q, color=YELLOW, fade_out=True),
                      Circumscribe(new.q, color=YELLOW, fade_out=True), run_time=1.6)
            self.play(Indicate(old.q, color=YELLOW, scale_factor=1.25),
                      Indicate(new.q, color=YELLOW, scale_factor=1.25), run_time=1.0)

        # ============================================================ 2 · stakes
        self.play(FadeOut(cards), FadeOut(task), FadeOut(cite), run_time=QUICK)
        line = NumberLine(x_range=[0, 1, 0.1], length=10, color=GRAY, stroke_width=3,
                          include_numbers=False, tick_size=0.06).move_to(UP * 0.9)
        nums = VGroup(*[formula(s, size=MATH_SMALL, color=GRAY).next_to(line.n2p(v), DOWN, buff=0.25)
                        for v, s in ((0, "0"), (0.5, "0.5"), (1, "1"))])
        thr = Line(line.n2p(0.9) + DOWN * 0.35, line.n2p(0.9) + UP * 0.35, color=YELLOW, stroke_width=4)
        human = text("hand to a human", size=LABEL, color=GRAY).next_to(line.n2p(0.45), UP, buff=0.55)
        alone = text("act", size=LABEL, color=GRAY).next_to(line.n2p(0.95), UP, buff=0.55)
        conf_t = ValueTracker(0.97)
        marker = always_redraw(lambda: Triangle(fill_color=BLUE, fill_opacity=1, stroke_width=0)
                               .scale(0.14).rotate(PI).next_to(line.n2p(conf_t.get_value()), UP, buff=0.04))
        says = always_redraw(lambda: VGroup(
            text("says", size=LABEL, color=BLUE),
            DecimalNumber(conf_t.get_value(), num_decimal_places=2, font_size=MATH, color=BLUE)
        ).arrange(RIGHT, buff=0.2).next_to(line.n2p(conf_t.get_value()), DOWN, buff=0.75))
        with self.narrate("That number decides when a car stops trusting its camera, or when a "
                          "diagnosis goes to a human doctor.") as beat:
            self.play(Create(line), FadeIn(nums), run_time=1.0)
            self.play(FadeIn(marker), FadeIn(says), Create(thr), FadeIn(alone), FadeIn(human),
                      run_time=1.0)
            beat.wait_until("stops", offset=-0.3)
            self.play(conf_t.animate.set_value(0.62), run_time=1.6, rate_func=SMOOTH)
            self.play(Indicate(human, color=YELLOW, scale_factor=1.1), run_time=0.9)
            beat.wait_until("diagnosis", offset=-0.2)
            self.play(conf_t.animate.set_value(0.95), run_time=1.2, rate_func=SMOOTH)
            self.play(conf_t.animate.set_value(0.8), run_time=beat.remaining(), rate_func=SMOOTH)

        question = MathTex(r"P(\text{right}\mid\text{says}\,", r"0.9", r")", r"\overset{?}{=}", r"0.9",
                           font_size=EQ).move_to(DOWN * 1.9)
        question[1].set_color(BLUE)
        question[4].set_color(BLUE)
        with self.narrate("So the precise question is this. When a network says ninety percent, "
                          "is it right ninety percent of the time?") as beat:
            beat.wait_until("says", offset=-0.4)
            self.play(conf_t.animate.set_value(0.9), run_time=1.0, rate_func=SMOOTH)
            marker.clear_updaters(); says.clear_updaters()
            self.play(FadeIn(question[0]), FadeIn(question[2]),
                      TransformFromCopy(says[1], question[1]), run_time=beat.until("right", offset=-0.2))
            self.play(Write(question[3]), TransformFromCopy(says[1], question[4]),
                      run_time=1.2)
            self.play(Indicate(question[4], color=YELLOW, scale_factor=1.1), run_time=0.9)

        # ============================================================ 3 · naive build: one prediction
        P1 = sim.softmax(z)
        ax1 = axes((-0.6, 9.6), (0, 1), x_ticks=[0, 2, 4, 6, 8], y_ticks=[0, 0.5, 1],
                   x_length=5.2, y_length=3.9, x_label="class", y_label="probability")
        ax1.move_to([-3.45, -0.3, 0])
        bw = ax1.x_axis.unit_size * 0.7
        Tt = ValueTracker(1.0)

        def prob_bars():
            p = sim.softmax(z, Tt.get_value())
            return VGroup(*[Rectangle(width=bw, height=max(p[k] * ax1.y_axis.unit_size, 0.002),
                                      stroke_width=0, fill_color=BLUE, fill_opacity=0.9)
                            .move_to(ax1.c2p(k, 0), aligned_edge=DOWN) for k in range(10)])
        bars = prob_bars()
        top_lbl = DecimalNumber(P1[7], num_decimal_places=2, font_size=MATH, color=YELLOW)
        top_lbl.next_to(bars[7], UP, buff=0.15)
        sim_tag = citation("simulated: 10 classes, 10,000 test cases")
        small_q = question.copy().scale(0.75).to_edge(UP, buff=0.45)
        with self.narrate("To check, we simulated a stand-in network: ten classes, ten thousand "
                          "test cases. For one case it outputs these ten probabilities. "
                          "The tallest bar, point eight four, is its confidence.") as beat:
            self.play(FadeOut(VGroup(line, nums, thr, human, alone, marker, says)),
                      Transform(question, small_q), run_time=1.0)
            self.play(Create(ax1), FadeIn(sim_tag), run_time=beat.until("these", offset=-0.2))
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.1),
                      run_time=beat.until("tallest", offset=-0.1))
            beat.wait_until("point", offset=-0.2)
            self.play(bars[7].animate.set_fill(YELLOW), FadeIn(top_lbl, shift=0.1 * UP), run_time=0.8)
        self.add(bars)

        # ============================================================ 4 · a whole bin as tiles
        n_right = 63
        tile = 0.34
        tiles = VGroup(*[Square(tile, stroke_width=2,
                                stroke_color=BLUE if i < n_right else RED,
                                fill_color=BLUE if i < n_right else RED,
                                fill_opacity=0.9 if i < n_right else 0.0)
                         for i in range(100)])
        tiles.arrange_in_grid(10, 10, buff=0.07).move_to([3.4, -0.55, 0])
        # wrong tiles get a small cross so right/wrong never relies on colour alone
        crosses = VGroup(*[VGroup(Line(t.get_corner(UL), t.get_corner(DR)), Line(t.get_corner(UR), t.get_corner(DL)))
                           .scale(0.55).set_stroke(RED, 2) for t in tiles[n_right:]])
        bin_lbl = VGroup(text("said", size=LABEL, color=GRAY),
                         formula(r"0.8\text{ to }0.9", color=BLUE),
                         text("· 1,317 cases", size=LABEL, color=GRAY)).arrange(RIGHT, buff=0.2)
        bin_lbl.next_to(tiles, UP, buff=0.35)
        cnt_t = ValueTracker(0)
        count = always_redraw(lambda: VGroup(
            DecimalNumber(cnt_t.get_value(), num_decimal_places=0, font_size=EQ, color=BLUE),
            text("right per 100", size=LABEL, color=GRAY)).arrange(RIGHT, buff=0.2)
            .next_to(tiles, DOWN, buff=0.3))
        with self.narrate("One answer can't show whether that is honest. So gather every case "
                          "where it said between eighty and ninety percent, about thirteen hundred "
                          "of them. Out of every hundred, sixty-three are right.") as beat:
            self.play(Indicate(top_lbl, color=YELLOW), run_time=0.9)
            beat.wait_until("gather", offset=-0.2)
            self.play(FadeIn(bin_lbl, shift=0.1 * DOWN), run_time=0.8)
            self.play(LaggedStart(*[FadeIn(t) for t in tiles], lag_ratio=0.02),
                      FadeIn(crosses), run_time=beat.until("Out", offset=-0.1))
            self.add(count)
            self.play(cnt_t.animate.set_value(n_right),
                      LaggedStart(*[Indicate(t, color=YELLOW, scale_factor=1.15) for t in tiles[:n_right]],
                                  lag_ratio=0.03),
                      run_time=beat.until_end_of("right", occurrence=1), rate_func=LINEAR)
        count.clear_updaters()

        # ============================================================ 5 · tiles become a column
        ax2 = axes((0, 1), (0, 1), x_ticks=[0, 0.2, 0.4, 0.6, 0.8, 1.0], y_ticks=[0, 0.2, 0.4, 0.6, 0.8, 1.0],
                   x_length=3.9, y_length=3.9, x_label="stated confidence", y_label="fraction right")
        ax2.move_to([3.55, -0.3, 0])
        acc1, ece1, accs1, ns1, confs1 = sweep_at(1.0)
        cols = self.col_rects(ax2, accs1, ns1, confs1, BLUE)
        col8 = cols[8][0]
        diag = DashedLine(ax2.c2p(0, 0), ax2.c2p(1, 1), color=INK, stroke_width=2.5, dash_length=0.12)
        diag_lbl = MathTex(r"P(\text{right}\mid p) = p", font_size=MATH, color=INK)
        diag_lbl.move_to(ax2.c2p(0.33, 0.86))
        # readouts (top right)
        acc_t = ValueTracker(acc1 * 100)
        ece_t = ValueTracker(ece1)
        acc_read = live_number(acc_t, 1, size=MATH, color=BLUE, prefix=r"\text{accuracy}=", suffix=r"\%")
        ece_read = live_number(ece_t, 2, size=MATH, color=RED, prefix=r"\text{calibration error}=")
        reads = VGroup(acc_read, ece_read).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        reads.move_to([3.1, 2.9, 0])
        keep_in_safe(reads)

        with self.narrate("Stack that sixty-three percent as a column above its confidence. "
                          "An honest network would reach this diagonal. Now do every confidence range.") as beat:
            self.play(FadeOut(question), FadeOut(bin_lbl), FadeOut(count), run_time=0.6)
            self.play(Create(ax2), FadeOut(crosses), FadeOut(tiles[n_right:]),
                      ReplacementTransform(tiles[:n_right], col8), run_time=beat.until("honest", offset=-0.3))
            self.play(Create(diag), run_time=1.0)
            self.play(FadeIn(diag_lbl, shift=0.1 * DOWN), run_time=0.7)
            beat.wait_until("every", offset=-0.2)
            others = [cols[b][0] for b in range(10) if b != 8]
            self.play(LaggedStart(*[GrowFromEdge(c, DOWN) for c in others], lag_ratio=0.12),
                      run_time=beat.remaining())

        # ============================================================ 6 · measured failure
        gaps = VGroup(*[cols[b][1] for b in range(10)])
        with self.narrate("Every column falls short. Weight each red gap by how many cases it holds, "
                          "average them, and you get the calibration error: point one five. "
                          "On average, it claims fifteen points more than it delivers.") as beat:
            beat.wait_until("red", offset=-0.3)
            self.play(LaggedStart(*[GrowFromEdge(g, DOWN) for g in gaps], lag_ratio=0.1),
                      run_time=beat.until("average", offset=-0.1))
            self.play(TransformFromCopy(gaps, ece_read), run_time=beat.until("point", offset=-0.2))
            self.play(flag(ece_read, color=RED), FadeIn(acc_read), run_time=1.0)
            self.play(Indicate(gaps[9], color=YELLOW), run_time=beat.remaining())

        # ============================================================ 7 · naive fix: smaller network
        s_acc, s_ece, s_rows = D["small"]
        scols = self.col_rects(ax2, [r[3] for r in s_rows], [r[2] for r in s_rows],
                               [r[4] for r in s_rows], PURPLE, show_gap=False)
        with self.narrate("The obvious fix is a smaller network. Its columns sit on the diagonal, "
                          "with an error of point oh one. But its accuracy drops from sixty-nine "
                          "percent to fifty-four. That is the nineteen ninety-eight trade.") as beat:
            self.play(cols.animate.set_opacity(0.0), bars.animate.set_opacity(0.3),
                      top_lbl.animate.set_opacity(0.3), run_time=0.8)
            self.play(LaggedStart(*[GrowFromEdge(c[0], DOWN) for c in scols], lag_ratio=0.08),
                      ece_t.animate.set_value(s_ece), run_time=beat.until("error", offset=-0.1))
            self.play(flag(ece_read, color=RED), run_time=0.8)
            beat.wait_until("drops", offset=-0.3)
            self.play(acc_t.animate.set_value(s_acc * 100), acc_read.animate.set_color(PURPLE),
                      run_time=1.8)
            beat.wait_until("trade", offset=-0.6)
            self.play(flag(acc_read, color=PURPLE), run_time=0.9)

        # bring the big network back
        cols_live = self.col_rects(ax2, accs1, ns1, confs1, BLUE)
        self.play(FadeOut(scols), FadeIn(cols_live), acc_t.animate.set_value(acc1 * 100),
                  acc_read.animate.set_color(BLUE), ece_t.animate.set_value(ece1),
                  bars.animate.set_opacity(1), top_lbl.animate.set_opacity(1), run_time=1.0)
        self.remove(cols)

        # ============================================================ 8 · insight: where the bars come from
        zmax = 7.0
        axz = axes((-0.6, 9.6), (-9, 7), x_ticks=[], y_ticks=[-8, -4, 0, 4],
                   x_length=5.2, y_length=3.9, y_label="score (logit)")
        axz.move_to(ax1.get_center())
        zbars = VGroup(*[Rectangle(width=bw, height=max(abs(z[k]) * axz.y_axis.unit_size, 0.002),
                                   stroke_width=0, fill_color=BLUE, fill_opacity=0.9)
                         .move_to(axz.c2p(k, 0), aligned_edge=DOWN if z[k] >= 0 else UP)
                         for k in range(10)])
        zbars[7].set_fill(YELLOW)
        soft = soft_eq(False).next_to(ax1, UP, buff=0.25).align_to(ax1, LEFT).shift(RIGHT * 0.9)
        with self.narrate("Go back to the big network's one answer. Its tallest bar is the right class; "
                          "it is just too tall. These probabilities come from raw scores called logits. "
                          "Raise e to each score, then divide by the total.") as beat:
            self.play(dim(ax2, cols_live, diag, diag_lbl, reads), run_time=0.8)
            beat.wait_until("tallest", offset=-0.2)
            self.play(Indicate(bars[7], color=YELLOW, scale_factor=1.05), run_time=1.0)
            beat.wait_until("too", offset=-0.2)
            self.play(Circumscribe(top_lbl, color=YELLOW), run_time=1.0)
            beat.wait_until("scores", offset=-0.3)
            a1c = ax1.copy()
            self.remove(ax1)
            self.add(a1c)
            self.play(ReplacementTransform(a1c, axz), FadeOut(top_lbl),
                      ReplacementTransform(bars, zbars), run_time=1.6)
            beat.wait_until("Raise", offset=-0.2)
            self.play(TransformFromCopy(zbars[7], soft.num), run_time=1.0)
            beat.wait_until("divide", offset=-0.2)
            self.play(Create(soft.bar), TransformFromCopy(zbars, soft.den), run_time=1.0)
            bars = prob_bars()
            bars[7].set_fill(YELLOW)
            self.play(Write(soft.lhs), ReplacementTransform(axz, ax1), ReplacementTransform(zbars, bars),
                      run_time=beat.remaining(min_time=1.0))
        top_lbl = DecimalNumber(P1[7], num_decimal_places=2, font_size=MATH, color=YELLOW).next_to(bars[7], UP, buff=0.15)
        self.play(FadeIn(top_lbl), run_time=0.4)

        # ============================================================ 9 · temperature + prediction
        softT = soft_eq(True).move_to(soft, aligned_edge=LEFT)
        T_read = live_number(Tt, 2, size=MATH, color=YELLOW, prefix=r"T=")
        T_read.move_to(ax1.c2p(2.6, 0.8))
        with self.narrate("Now divide every score by one number, T, the temperature. Turn T up. "
                          "What happens to the accuracy? [pause 1.5]") as beat:
            beat.wait_until("T", offset=-0.2)
            self.play(TransformMatchingShapes(soft, softT), run_time=1.4)
            self.play(FadeIn(T_read, shift=0.1 * DOWN), run_time=0.6)
            beat.wait_until("accuracy", offset=-0.4)
            self.play(undim(reads, ax2, diag, diag_lbl), run_time=0.6)
            self.play(Circumscribe(acc_read, color=YELLOW, fade_out=True), run_time=1.5)
            self.play(Indicate(T_read, color=YELLOW), run_time=1.0)

        # ============================================================ 10 · turning T: bars flatten, accuracy fixed
        def upd_bars(m):
            p = sim.softmax(z, Tt.get_value())
            for k, r in enumerate(m):
                h = max(p[k] * ax1.y_axis.unit_size, 0.002)
                r.stretch_to_fit_height(h)
                r.move_to(ax1.c2p(k, 0), aligned_edge=DOWN)
        bars.add_updater(upd_bars)
        top_lbl.add_updater(lambda m: m.set_value(sim.softmax(z, Tt.get_value())[7]).next_to(bars[7], UP, buff=0.15))

        def upd_cols(m):
            _, e, a, n, c = sweep_at(Tt.get_value())
            new = self.col_rects(ax2, a, n, c, BLUE)
            for old_c, new_c in zip(m, new):
                old_c.become(new_c)
            if m.dimmed:
                for c in m:
                    c[0].set_fill(opacity=c[0].get_fill_opacity() * 0.3)
                    c[1].set_fill(opacity=c[1].get_fill_opacity() * 0.3).set_stroke(opacity=0.3)
        cols_live.dimmed = False
        cols_live.add_updater(upd_cols)
        ece_t.add_updater(lambda m: m.set_value(sweep_at(Tt.get_value())[1]))

        with self.narrate("Nothing. Dividing by T pulls every score toward zero, so the bars flatten, "
                          "but the tallest bar stays tallest. Every prediction is unchanged. "
                          "Only the confidence drops.") as beat:
            self.play(flag(acc_read, color=BLUE), run_time=0.9)
            beat.wait_until("pulls", offset=-0.2)
            self.play(Tt.animate.set_value(1.6), run_time=beat.until("tallest", offset=-0.2), rate_func=SMOOTH)
            self.play(Indicate(bars[7], color=YELLOW, scale_factor=1.05), run_time=1.0)
            beat.wait_until("Only", offset=-0.2)
            self.play(Circumscribe(top_lbl, color=YELLOW, fade_out=True), run_time=beat.remaining(min_time=1.0))

        # ============================================================ 11 · the diagram fixes itself
        with self.narrate("On the diagram, the columns climb toward the diagonal. Fit T on held-out cases, "
                          "and a temperature of about two takes the error from point one five "
                          "to point oh one.") as beat:
            self.play(dim(ax1, bars, softT, top_lbl, T_read),
                      run_time=0.8)
            self.play(Tt.animate.set_value(1.6), run_time=beat.until("Fit", offset=-0.2), rate_func=SMOOTH)
            self.play(Tt.animate.set_value(T_STAR), run_time=beat.until("point", occurrence=2, offset=-0.2),
                      rate_func=SMOOTH)
            self.play(flag(ece_read, color=RED), run_time=beat.remaining(min_time=0.8))
        bars.clear_updaters(); top_lbl.clear_updaters(); cols_live.clear_updaters(); ece_t.clear_updaters()

        # ============================================================ 12 · payoff: the real numbers
        self.play(FadeOut(VGroup(ax1, bars, softT, top_lbl, T_read, sim_tag)), run_time=0.6)
        axr = axes((0, 18), (-0.6, 1.6), x_ticks=[0, 5, 10, 15], y_ticks=[], x_length=4.6, y_length=2.4,
                   x_label="calibration error (%)", numbers=True)
        axr.y_axis.set_opacity(0)
        axr.move_to([-3.4, -0.6, 0])
        bh = 0.55
        r_raw = Rectangle(width=RESNET_ECE * axr.x_axis.unit_size, height=bh, stroke_width=0,
                          fill_color=RED, fill_opacity=0.85).move_to(axr.c2p(0, 1), aligned_edge=LEFT)
        r_T = Rectangle(width=RESNET_ECE_T * axr.x_axis.unit_size, height=bh, stroke_width=0,
                        fill_color=RED, fill_opacity=0.85).move_to(axr.c2p(0, 0), aligned_edge=LEFT)
        v_raw = formula(r"16.5\%", color=RED).next_to(r_raw, RIGHT, buff=0.15)
        v_T = formula(r"1.3\%", color=RED).next_to(r_T, RIGHT, buff=0.15)
        l_raw = text("as trained", size=LABEL, color=GRAY).next_to(r_raw, UP, buff=0.12).align_to(r_raw, LEFT)
        l_T = text("after one temperature", size=LABEL, color=YELLOW).next_to(r_T, UP, buff=0.12).align_to(r_T, LEFT)
        rhead = VGroup(text("ResNet-110", size=HEADING, color=BLUE),
                       text("on the 100-category test", size=LABEL, color=GRAY)).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        rhead.next_to(axr, UP, buff=1.25).align_to(axr, LEFT)
        racc = formula(r"\text{accuracy } 69.4\% \to 69.4\%", color=BLUE).next_to(axr, DOWN, buff=0.35).align_to(axr, LEFT)
        gcite = citation("Guo, Pleiss, Sun & Weinberger, 2017 · ICML · Table 1")
        with self.narrate("Guo, Pleiss, Sun and Weinberger reported this at ICML in twenty seventeen. "
                          "Their hundred-and-ten-layer network, the twenty sixteen design, had a calibration "
                          "error of sixteen and a half percent. One temperature cut it to one point three, "
                          "with accuracy untouched.") as beat:
            self.play(FadeIn(gcite), FadeIn(rhead, shift=0.1 * DOWN), run_time=beat.until("Their", offset=-0.2))
            self.play(Create(axr), FadeIn(l_raw), run_time=beat.until("sixteen", occurrence=2, offset=-0.6))
            self.play(GrowFromEdge(r_raw, LEFT), FadeIn(v_raw), run_time=1.0)
            beat.wait_until("One", offset=-0.2)
            self.play(FadeIn(l_T), TransformFromCopy(r_raw, r_T), run_time=1.2)
            self.play(FadeIn(v_T), run_time=0.5)
            beat.wait_until("accuracy", offset=-0.3)
            self.play(FadeIn(racc, shift=0.1 * UP), run_time=beat.remaining(min_time=0.8))

        # ============================================================ 13 · honest limit: shift
        sh_acc, sh_ece, sh_rows = D["shift"]
        shift_cols = self.col_rects(ax2, [r[3] for r in sh_rows], [r[2] for r in sh_rows],
                                    [r[4] for r in sh_rows], BLUE)
        shift_tag = text("simulated shift: noisier inputs", size=LABEL, color=GRAY)
        shift_tag.next_to(ax2, LEFT, buff=0.6).align_to(ax2, UP)
        ocite = citation("Ovadia et al., 2019 · NeurIPS")
        with self.narrate("The temperature is fit on data like the training data. When the inputs shift, "
                          "Ovadia and colleagues found that this calibration does not hold.") as beat:
            self.play(FadeOut(VGroup(axr, r_raw, r_T, v_raw, v_T, l_raw, l_T, rhead, racc)),
                      FadeOut(gcite), run_time=0.8)
            beat.wait_until("shift", offset=-0.3)
            self.play(FadeIn(shift_tag), FadeIn(ocite), run_time=0.6)
            self.play(*[Transform(a, b) for a, b in zip(cols_live, shift_cols)],
                      ece_t.animate.set_value(sh_ece), acc_t.animate.set_value(sh_acc * 100),
                      run_time=beat.until("not", offset=-0.2))
            self.play(flag(ece_read, color=RED), run_time=beat.remaining(min_time=0.8))

        # ============================================================ 14 · landing
        self.fade_out_all(run_time=0.6)
        old2 = card("LeNet", "design of 1998", LENET_ACC, PURPLE)
        new2 = card("ResNet-110", "design of 2016", RESNET_ACC, BLUE)
        for c, val in ((old2, LENET_ECE), (new2, RESNET_ECE)):
            c.conf_lbl.become(text("calibration error", size=LABEL, color=GRAY).move_to(c.conf_lbl, aligned_edge=LEFT))
            c.q.become(formula(rf"{val:.1f}\%", color=RED).next_to(c.conf_lbl, RIGHT, buff=0.3))
        cards2 = VGroup(old2, new2).arrange(RIGHT, buff=1.0).move_to(UP * 0.5)
        fit(cards2, width=SAFE_WIDTH)
        fixed = formula(r"1.3\%", color=RED).move_to(new2.q, aligned_edge=LEFT)
        tlbl = formula(r"\div T", color=YELLOW).next_to(new2.q, UP, buff=0.3)
        cite2 = citation("Guo et al., 2017 · ICML · CIFAR-100")
        with self.narrate("So, the two networks. The old one's confidence was honest; the new one's "
                          "was inflated. Divide the new one's scores by a single number, and it keeps "
                          "its sixty-nine percent, and its ninety percent means close to ninety.") as beat:
            self.play(FadeIn(cards2), FadeIn(cite2), run_time=beat.until("old", offset=-0.2))
            self.play(Circumscribe(old2.q, color=YELLOW, fade_out=True), run_time=1.2)
            beat.wait_until("inflated", offset=-0.3)
            self.play(Circumscribe(new2.q, color=YELLOW, fade_out=True), run_time=1.2)
            beat.wait_until("Divide", offset=-0.2)
            self.play(FadeIn(tlbl, shift=0.1 * DOWN), run_time=0.6)
            self.play(Transform(new2.q, fixed), run_time=1.2)
            beat.wait_until("keeps", offset=-0.1)
            self.play(Indicate(new2.pct, color=YELLOW), run_time=0.9)
            self.play(Indicate(new2.q, color=YELLOW), run_time=beat.remaining(min_time=0.8))

        self.end_card()
