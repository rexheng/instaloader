"""Episode 73 - How Open-Minded People Split Into Camps (bounded-confidence opinion dynamics).

    videos/toolkit/render.sh videos/episodes/073-opinion-dynamics-bounded-confidence/scene.py Episode \
        videos/episodes/073-opinion-dynamics-bounded-confidence/final.mp4

All opinion data is simulated by sim.py (-> data.json) and labelled "simulated" on screen.
"""
import json
from pathlib import Path

import numpy as np
from manim import *
from sample_space import *

HERE = Path(__file__).resolve().parent
D = json.loads((HERE / "data.json").read_text())
X0 = np.array(D["x0"])
HK = np.array(D["hk"])              # 11 x 100 (rounds 0..10)
DG = np.array(D["degroot"])         # 11 x 100
LAB = np.array(D["labels"])
CAMPS = [c for c, _ in D["camps"]]
CATCH = D["catchments"]
SWEEP = D["sweep"]
SP_HK = np.array(D["spread_hk"])
SP_DG = np.array(D["spread_dg"])
TRUST = D["trust"]
N = len(X0)
EPS = 0.1
ROUNDS = 10
DEMO = 61                            # the cold-open person (0.644, shifts down by 0.026)
TRUSTER = 70                         # the DeGroot person whose trust links are drawn


def interp_rows(traj, t):
    """Opinions at fractional round t (straight lines between rounds)."""
    k = int(np.floor(t))
    if k >= len(traj) - 1:
        return traj[-1]
    a = t - k
    return (1 - a) * traj[k] + a * traj[k + 1]


def spread_at(sp, t):
    k = int(np.floor(t))
    if k >= len(sp) - 1:
        return sp[-1]
    a = t - k
    return (1 - a) * sp[k] + a * sp[k + 1]


def stack_positions(xs, x_of, base_y, step=0.135, min_dx=0.125):
    """Dot-plot stacking: each person sits at their opinion, piled up where crowded."""
    order = np.argsort(xs)
    levels = []                                  # list of lists of screen-x per level
    pos = np.zeros((len(xs), 3))
    for i in order:
        sx = x_of(xs[i])
        lv = 0
        while lv < len(levels) and any(abs(sx - o) < min_dx for o in levels[lv]):
            lv += 1
        if lv == len(levels):
            levels.append([])
        levels[lv].append(sx)
        pos[i] = [sx, base_y + 0.16 + step * lv, 0]
    return pos


def panel_axes(cx, x_len, y_bottom, y_len, label_y=True):
    ax = axes((0, ROUNDS), (0, 1), x_length=x_len, y_length=y_len,
              x_ticks=[0, 5, 10], y_ticks=[0, 0.5, 1], x_label="round",
              y_label="opinion" if label_y else None)
    shift = np.array([cx, y_bottom, 0]) - ax.c2p(0, 0)
    shift[0] = cx - (ax.c2p(0, 0)[0] + ax.c2p(ROUNDS, 0)[0]) / 2
    ax.shift(shift)
    return ax


class Braid(VGroup):
    """100 threads (one per person) drawn up to round t, plus a dot at each head."""

    def __init__(self, ax, traj, color, t=0.0, width=1.6, opacity=0.55):
        super().__init__()
        self.ax, self.traj, self.color = ax, traj, color
        self.threads = VGroup(*[VMobject(stroke_color=color, stroke_width=width,
                                         stroke_opacity=opacity) for _ in range(N)])
        self.heads = VGroup(*[Dot(radius=0.05, color=color) for _ in range(N)])
        self.add(self.threads, self.heads)
        self.set_t(t)

    def path(self, i, t):
        k = int(np.floor(t))
        pts = [self.ax.c2p(r, self.traj[r][i]) for r in range(min(k, ROUNDS) + 1)]
        if t > k and k < ROUNDS:
            y = interp_rows(self.traj, t)[i]
            pts.append(self.ax.c2p(t, y))
        if len(pts) == 1:
            pts.append(pts[0])
        # pad to a fixed number of corners so Transform between braids is smooth
        while len(pts) < ROUNDS + 1:
            pts.append(pts[-1])
        return pts

    def set_t(self, t):
        for i in range(N):
            p = self.path(i, t)
            self.threads[i].set_points_as_corners(p)
            self.heads[i].move_to(p[-1])
        return self


class Episode(NarratedScene):
    EPISODE = 73
    TITLE = "How Open-Minded People Split Into Camps"
    PRONUNCIATIONS = {
        "DeGroot": "duh groat",
        "DeGroot's": "duh groats",
        "Hegselmann": "heg zel mun",
        "Krause": "krow zuh",
        "Krause's": "krow zuhs",
        "modelers": "modelers",
    }

    # ------------------------------------------------------------------ helpers
    def run_braid(self, braid, tracker, run_time, rate=LINEAR):
        braid.add_updater(lambda m: m.set_t(tracker.get_value()))
        self.play(tracker.animate.set_value(ROUNDS), run_time=run_time, rate_func=rate)
        braid.clear_updaters()

    def construct(self):
        # ============================================================ 1. cold open
        L_LEFT, L_RIGHT, LINE_Y = -5.5, 5.5, -1.7

        def ox(v):
            return L_LEFT + (L_RIGHT - L_LEFT) * v

        line = NumberLine(x_range=[0, 1, 0.5], length=L_RIGHT - L_LEFT, color=GRAY,
                          stroke_width=2.5, include_numbers=False).move_to([0, LINE_Y, 0])
        line_nums = VGroup(*[MathTex(s, font_size=MATH_SMALL, color=GRAY)
                             .next_to(line.n2p(v), DOWN, buff=0.2)
                             for s, v in (("0", 0), ("0.5", 0.5), ("1", 1))])
        line_lab = label("opinion", color=GRAY).next_to(line_nums[2], DOWN, buff=0.15)
        line_lab.align_to(line.get_right(), RIGHT)
        pos0 = stack_positions(X0, ox, LINE_Y)
        people = VGroup(*[Dot(p, radius=0.06, color=BLUE) for p in pos0])
        sim_tag = label("simulated", size=SMALL + 2, color=GRAY).to_corner(UR, buff=0.0)
        sim_tag.move_to([SAFE_X - sim_tag.width / 2, SAFE_TOP - 0.1 - sim_tag.height / 2, 0])

        me = people[DEMO]
        ring = Circle(radius=0.14, color=INK, stroke_width=3).move_to(me)
        win_lo, win_hi = X0[DEMO] - EPS, X0[DEMO] + EPS
        inside = [i for i in range(N) if abs(X0[i] - X0[DEMO]) <= EPS]
        top_y = max(pos0[i][1] for i in inside) + 0.25
        window = Rectangle(width=ox(win_hi) - ox(win_lo), height=top_y - LINE_Y,
                           stroke_width=0, fill_color=YELLOW, fill_opacity=0.16)
        window.move_to([(ox(win_lo) + ox(win_hi)) / 2, (top_y + LINE_Y) / 2, 0])
        w_edges = VGroup(*[Line([ox(v), LINE_Y, 0], [ox(v), top_y, 0], color=YELLOW,
                                stroke_width=2.5) for v in (win_lo, win_hi)])
        b_left = BraceBetweenPoints([ox(win_lo), top_y + 0.1, 0], [ox(X0[DEMO]), top_y + 0.1, 0],
                                    direction=UP, color=YELLOW)
        b_right = BraceBetweenPoints([ox(X0[DEMO]), top_y + 0.1, 0], [ox(win_hi), top_y + 0.1, 0],
                                     direction=UP, color=YELLOW)
        bl_lab = MathTex("0.1", font_size=MATH, color=YELLOW).next_to(b_left, UP, buff=0.12)
        br_lab = MathTex("0.1", font_size=MATH, color=YELLOW).next_to(b_right, UP, buff=0.12)
        avg = float(np.mean(X0[inside]))
        target = Triangle(color=YELLOW, fill_opacity=1, stroke_width=0).scale(0.11)
        target.move_to([ox(avg), LINE_Y - 0.0, 0]).rotate(PI)
        target.next_to([ox(avg), LINE_Y, 0], UP, buff=0.02)
        arrow = CurvedArrow(me.get_center() + UP * 0.12, [ox(avg), LINE_Y + 0.22, 0],
                            angle=-1.4, color=YELLOW, stroke_width=3, tip_length=0.14)
        question = text("How many opinions survive?", size=HEADING)
        question.move_to([0, 2.75, 0])

        with self.narrate("A hundred people, with opinions from zero to one. Each round, "
                          "everyone moves to the average of everyone within point one of them. "
                          "Repeat until nobody moves. How many different opinions survive? "
                          "[pause 1.5]") as beat:
            self.play(Create(line), FadeIn(line_nums), FadeIn(line_lab),
                      LaggedStart(*[FadeIn(d, scale=0.5) for d in people], lag_ratio=0.02),
                      FadeIn(sim_tag), run_time=beat.until("Each round"))
            self.play(Create(ring), people.animate.set_opacity(0.45),
                      me.animate.set_opacity(1), run_time=beat.until("average"))
            self.play(Create(arrow), FadeIn(target), run_time=beat.until("everyone", 2))
            self.play(FadeIn(window), Create(w_edges),
                      *[people[i].animate.set_opacity(1) for i in inside],
                      run_time=beat.until("within"))
            self.play(GrowFromCenter(b_left), GrowFromCenter(b_right), run_time=0.6)
            self.play(Write(bl_lab), Write(br_lab), run_time=beat.until("Repeat", offset=-0.1))
            # everyone does it at once: one real round, then rewound
            pos1 = stack_positions(HK[1], ox, LINE_Y)
            rule_group = VGroup(window, w_edges, b_left, b_right, bl_lab, br_lab, arrow, target, ring)
            self.play(FadeOut(rule_group), people.animate.set_opacity(1),
                      run_time=beat.until("nobody", offset=-0.1))
            self.play(*[people[i].animate.move_to(pos1[i]) for i in range(N)],
                      run_time=beat.until("How many", offset=-0.1))
            self.play(Write(question), run_time=1.0)
            self.play(*[people[i].animate.move_to(pos0[i]) for i in range(N)],
                      run_time=beat.remaining(), rate_func=SMOOTH)

        # ============================================================ 2. stakes -> two panels
        axL = panel_axes(-3.15, 4.4, -1.55, 3.75)
        axR = panel_axes(3.35, 4.4, -1.55, 3.75)
        headL = text("everyone you trust", size=LABEL, color=PURPLE)
        headR = text("only within 0.1", size=LABEL, color=BLUE)
        headL.move_to([axL.c2p(5, 0)[0], 3.25, 0])
        headR.move_to([axR.c2p(5, 0)[0], 3.25, 0])
        dg = Braid(axL, DG, PURPLE)
        hk = Braid(axR, HK, BLUE)
        with self.narrate("Nobody here is stubborn, and nobody is extreme. Rules like this are how "
                          "modelers ask when a group that keeps compromising reaches consensus, "
                          "and when it splits into camps.") as beat:
            self.play(FadeOut(question), run_time=0.6)
            self.play(ReplacementTransform(VGroup(line, line_nums, line_lab), axL),
                      *[ReplacementTransform(people[i], dg.heads[i]) for i in range(N)],
                      run_time=2.0)
            self.add(dg)
            self.play(TransformFromCopy(axL, axR), TransformFromCopy(dg.heads, hk.heads),
                      run_time=beat.until("consensus", offset=-0.2))
            self.add(hk)
            self.play(FadeIn(headL, shift=0.1 * DOWN), run_time=0.8)
            self.play(FadeIn(headR, shift=0.1 * DOWN), run_time=beat.until("camps"))

        # ============================================================ 3. naive build: DeGroot
        tL = ValueTracker(0)
        spL = live_number(ValueTracker(SP_DG[0]), 2, size=MATH, color=PURPLE,
                          prefix=r"\text{spread} =")
        spL_tr = spL.number.updaters and None
        spL_val = ValueTracker(SP_DG[0])
        spL = live_number(spL_val, 2, size=MATH, color=PURPLE, prefix=r"\text{spread} =")
        spL.move_to([axL.c2p(5, 0)[0], -2.85, 0])
        span_L = Line(axL.c2p(0, X0.min()), axL.c2p(0, X0.max()), color=PURPLE, stroke_width=6)
        span_L.shift(LEFT * 0.0)
        p_tr = dg.heads[TRUSTER].get_center()
        arcs = VGroup(*[ArcBetweenPoints(p_tr, dg.heads[j].get_center(),
                                         angle=-1.2 if X0[j] > X0[TRUSTER] else 1.2,
                                         color=PURPLE, stroke_width=2.5)
                        for j in TRUST[TRUSTER]])
        cite_dg = citation("DeGroot, 1974 · J. American Statistical Association")
        with self.narrate("The obvious answer is one. In nineteen seventy four, Morris DeGroot "
                          "proved that people who keep averaging over a fixed web of trust that "
                          "links everyone always reach consensus. Here it is, simulated: each "
                          "person trusts five random others, plus themselves. The spread, from "
                          "the highest opinion to the lowest, shrinks every round to almost "
                          "nothing.") as beat:
            self.play(dim(axR, hk, headR, opacity=0.3), run_time=beat.until("nineteen"))
            self.play(FadeIn(cite_dg), run_time=0.8)
            beat.wait_until("five random", offset=-0.2)
            self.play(LaggedStart(*[Create(a) for a in arcs], lag_ratio=0.2),
                      flag(dg.heads[TRUSTER], color=PURPLE), run_time=beat.until("spread"))
            self.play(FadeOut(arcs), FadeOut(cite_dg), FadeIn(spL), Create(span_L),
                      run_time=beat.until("shrinks", offset=-0.1))
            span_L.add_updater(lambda m: m.put_start_and_end_on(
                axL.c2p(tL.get_value(), interp_rows(DG, tL.get_value()).min()),
                axL.c2p(tL.get_value(), interp_rows(DG, tL.get_value()).max() + 1e-4)))
            spL_val.add_updater(lambda m: m.set_value(spread_at(SP_DG, tL.get_value())))
            self.run_braid(dg, tL, beat.remaining(min_time=3.5))
            span_L.clear_updaters()
            spL_val.clear_updaters()
            self.add(spL_val)
        one_lab = MathTex("1", font_size=MATH, color=PURPLE).next_to(axL.c2p(ROUNDS, DG[-1].mean()),
                                                                      RIGHT, buff=0.2)

        # ============================================================ 4. fail: bounded confidence
        tR = ValueTracker(0)
        spR_val = ValueTracker(SP_HK[0])
        spR = live_number(spR_val, 2, size=MATH, color=BLUE, prefix=r"\text{spread} =")
        spR.move_to([axR.c2p(5, 0)[0], -2.85, 0])
        span_R = Line(axR.c2p(0, X0.min()), axR.c2p(0, X0.max()), color=BLUE, stroke_width=6)
        camp_nums = VGroup(*[MathTex(str(k + 1), font_size=MATH, color=BLUE)
                             .next_to(axR.c2p(ROUNDS, c), RIGHT, buff=0.2)
                             for k, c in enumerate(CAMPS)])
        with self.narrate("Now run our rule on the same hundred starting opinions. The spread "
                          "falls from point nine nine to point seven four, and freezes. Four "
                          "camps, and they never move again. We predicted one. We got four.") as beat:
            self.play(Write(one_lab), undim(axR, hk, headR), dim(dg, span_L, opacity=0.35),
                      run_time=beat.until("same"))
            self.play(FadeIn(spR), Create(span_R), flag(hk.heads), run_time=beat.until("falls"))
            span_R.add_updater(lambda m: m.put_start_and_end_on(
                axR.c2p(tR.get_value(), interp_rows(HK, tR.get_value()).min()),
                axR.c2p(tR.get_value(), interp_rows(HK, tR.get_value()).max())))
            spR_val.add_updater(lambda m: m.set_value(spread_at(SP_HK, tR.get_value())))
            self.run_braid(hk, tR, beat.until("freezes", offset=0.3), rate=LINEAR)
            span_R.clear_updaters()
            spR_val.clear_updaters()
            self.play(flag(spR), run_time=0.8)
            beat.wait_until("Four", offset=-0.15)
            self.play(LaggedStart(*[FadeIn(n, shift=0.15 * LEFT) for n in camp_nums],
                                  lag_ratio=0.3), run_time=beat.until("never"))
            self.play(Indicate(hk.threads, color=BLUE, scale_factor=1.0),
                      run_time=beat.until("predicted", offset=-0.1))
            self.play(flag(one_lab, color=PURPLE), run_time=beat.until("got", offset=-0.1))
            self.play(flag(camp_nums), run_time=0.8)

        # ============================================================ 5. cause: the web tears
        axB = panel_axes(-0.3, 5.6, -2.2, 4.7)
        hkB = Braid(axB, HK, BLUE, t=ROUNDS)
        numsB = VGroup(*[MathTex(str(k + 1), font_size=MATH, color=BLUE)
                         .next_to(axB.c2p(ROUNDS, c), RIGHT, buff=0.2)
                         for k, c in enumerate(CAMPS)])
        gx = axB.c2p(ROUNDS, 0)[0] + 0.75
        gaps = VGroup()
        gap_labs = VGroup()
        for k in range(len(CAMPS) - 1):
            a, b = axB.c2p(ROUNDS, CAMPS[k]), axB.c2p(ROUNDS, CAMPS[k + 1])
            seg = Line([gx, a[1] + 0.12, 0], [gx, b[1] - 0.12, 0], color=RED, stroke_width=4)
            ends = VGroup(*[Line([gx - 0.09, y, 0], [gx + 0.09, y, 0], color=RED, stroke_width=4)
                            for y in (a[1] + 0.12, b[1] - 0.12)])
            gaps.add(VGroup(seg, ends))
            g = CAMPS[k + 1] - CAMPS[k]
            gap_labs.add(MathTex(f"{g:.2f}", font_size=MATH, color=RED).next_to(seg, RIGHT, buff=0.2))
        # a yellow listening window around camp 2 (index 1)
        cy = CAMPS[1]

        def band(lo, hi, opacity=0.16):
            r = Rectangle(width=axB.c2p(ROUNDS, 0)[0] - axB.c2p(0, 0)[0],
                          height=axB.c2p(0, hi)[1] - axB.c2p(0, lo)[1],
                          stroke_width=0, fill_color=YELLOW, fill_opacity=opacity)
            return r.move_to([(axB.c2p(0, 0)[0] + axB.c2p(ROUNDS, 0)[0]) / 2,
                              (axB.c2p(0, lo)[1] + axB.c2p(0, hi)[1]) / 2, 0])
        lwin = band(cy - EPS, cy + EPS)
        with self.narrate("The difference is the web. DeGroot's is fixed. Here, who you listen to "
                          "depends on where you stand. Every gap between these final camps is "
                          "wider than point one, so no one in one camp can hear anyone in the "
                          "next. If any gap were narrower, those two camps would still be pulling "
                          "on each other.") as beat:
            self.play(FadeOut(VGroup(axL, dg, span_L, one_lab, headL, spL)),
                      FadeOut(VGroup(spR, span_R, headR)),
                      ReplacementTransform(axR, axB),
                      ReplacementTransform(hk, hkB),
                      ReplacementTransform(camp_nums, numsB), run_time=beat.until("fixed"))
            self.play(FadeIn(lwin), run_time=beat.until("where you stand", offset=-0.1))
            self.play(lwin.animate.move_to(band(CAMPS[2] - EPS, CAMPS[2] + EPS)),
                      run_time=beat.until("Every gap"))
            self.play(LaggedStart(*[Create(g) for g in gaps], lag_ratio=0.3),
                      run_time=beat.until("wider"))
            self.play(LaggedStart(*[Write(g) for g in gap_labs], lag_ratio=0.3),
                      run_time=beat.until("so no one", offset=-0.1))
            self.play(lwin.animate.move_to(band(CAMPS[1] - EPS, CAMPS[1] + EPS)),
                      run_time=beat.until("If any", offset=-0.1))
            # what "narrower" would mean: the window would reach the next camp
            wide = band(CAMPS[1] - EPS, CAMPS[2] + 0.01)
            self.play(Transform(lwin, wide), run_time=beat.until("pulling", offset=-0.1))
            self.play(Transform(lwin, band(CAMPS[1] - EPS, CAMPS[1] + EPS)), run_time=beat.remaining(min_time=1.0))

        # ============================================================ 6. insight: 1/(2 eps)
        eps_br = BraceBetweenPoints(axB.c2p(ROUNDS, cy), axB.c2p(ROUNDS, cy + EPS), direction=RIGHT,
                                    color=YELLOW)
        eps_br.shift(LEFT * 0.0)
        eps_lab = MathTex(r"\varepsilon", font_size=EQ, color=YELLOW)
        bx = axB.c2p(0, 0)[0] - 0.95                 # starting-band column, left of tick labels
        bands = VGroup()
        band_labs = VGroup()
        for k, (lo, hi) in enumerate(CATCH):
            seg = Line([bx, axB.c2p(0, lo)[1], 0], [bx, axB.c2p(0, hi)[1], 0], color=YELLOW,
                       stroke_width=7)
            bands.add(seg)
            band_labs.add(MathTex(f"{hi - lo:.2f}", font_size=MATH_SMALL, color=YELLOW)
                          .next_to(seg, LEFT, buff=0.2))
        cuts = VGroup(*[Line([bx, axB.c2p(0, 0.2 * k)[1] + 0.03, 0],
                             [bx, axB.c2p(0, 0.2 * (k + 1))[1] - 0.03, 0], color=YELLOW,
                             stroke_width=7) for k in range(5)])
        cut_labs = VGroup(*[MathTex(r"2\varepsilon", font_size=MATH_SMALL, color=YELLOW)
                            .next_to(c, LEFT, buff=0.2) for c in cuts])
        # formula, right side
        fx = 4.75
        f1 = MathTex(r"\text{camps}", r"\approx", r"{1", r"\over", r"2\varepsilon}", font_size=EQ)
        f1[4].set_color(YELLOW)
        f1.move_to([fx, 1.2, 0])
        f2 = MathTex(r"=", r"{1", r"\over", r"2 \times 0.1}", r"=", r"5", font_size=EQ)
        f2[3].set_color(YELLOW)
        f2[5].set_color(YELLOW)
        f2.next_to(f1, DOWN, buff=0.45).align_to(f1[1], LEFT)
        counted = MathTex(r"\text{counted: }", r"4", font_size=EQ, color=BLUE)
        counted.next_to(f2, DOWN, buff=0.5).align_to(f1, LEFT)
        cite_df = citation("rule of thumb: Deffuant et al., 2000 · Advances in Complex Systems")
        axis_line = Line(axB.c2p(0, 0), axB.c2p(0, 1))
        with self.narrate("So how many camps should you expect? Call the listening range epsilon. "
                          "Trace each camp back to where its members started. Each one gathered "
                          "a band about two epsilon wide: roughly everyone within epsilon of its "
                          "centre, on either side. Cut the line from zero to one into bands of "
                          "width two epsilon, and you get one over two epsilon camps. Here, that "
                          "predicts five. [pause 0.8] We counted four.") as beat:
            self.play(FadeOut(gap_labs), gaps.animate.set_opacity(0.35),
                      run_time=beat.until("epsilon", offset=-0.6))
            eps_br.next_to(axB.c2p(ROUNDS, cy + EPS / 2), RIGHT, buff=0.05)
            eps_br.stretch_to_fit_height(axB.c2p(0, EPS)[1] - axB.c2p(0, 0)[1])
            eps_br.move_to([gaps[0][0].get_center()[0] - 0.05, axB.c2p(0, cy + EPS / 2)[1], 0])
            eps_lab.next_to(eps_br, RIGHT, buff=0.12)
            self.play(GrowFromCenter(eps_br), Write(eps_lab), FadeOut(gaps),
                      numsB.animate.set_opacity(0.0), run_time=beat.until("Trace", offset=-0.1))
            # trace camps back one at a time
            t_end = beat.time_of("centre", end=True) - beat.elapsed()
            per = max(0.9, (beat.time_of("Each one") - beat.elapsed()) / 4)
            for k in range(4):
                members = [i for i in range(N) if LAB[i] == k]
                others = [i for i in range(N) if LAB[i] != k]
                self.play(*[hkB.threads[i].animate.set_stroke(opacity=0.12) for i in others],
                          *[hkB.heads[i].animate.set_opacity(0.2) for i in others],
                          *[hkB.threads[i].animate.set_stroke(opacity=0.9) for i in members],
                          *[hkB.heads[i].animate.set_opacity(1) for i in members],
                          Create(bands[k]), FadeIn(band_labs[k], shift=0.1 * LEFT),
                          run_time=per)
            self.play(*[t.animate.set_stroke(opacity=0.55) for t in hkB.threads],
                      *[h.animate.set_opacity(1) for h in hkB.heads],
                      run_time=beat.until("Cut", offset=-0.1, min_time=0.6))
            self.play(ReplacementTransform(VGroup(*bands), cuts[:4]), FadeIn(cuts[4]),
                      ReplacementTransform(band_labs, cut_labs[:4]), FadeIn(cut_labs[4]),
                      run_time=beat.until("and you get"))
            self.play(Write(f1[0:2]), TransformFromCopy(axis_line, f1[2]), Create(f1[3]),
                      TransformFromCopy(cut_labs[2], f1[4]), FadeIn(cite_df),
                      run_time=beat.until("Here", offset=-0.1))
            self.play(TransformFromCopy(f1[1:5], f2[0:4]), run_time=beat.until("five", offset=-0.2))
            self.play(Write(f2[4:]), run_time=0.7)
            beat.wait_until("We counted", offset=-0.15)
            self.play(numsB.animate.set_opacity(1), TransformFromCopy(numsB[3], counted[1]),
                      Write(counted[0]), run_time=beat.remaining(min_time=1.0))

        # ============================================================ 7. measure: log-log sweep
        lx = np.log10
        ax2 = axes((lx(0.0085), lx(0.36)), (lx(0.85), lx(60)), x_length=8.4, y_length=4.9,
                   x_ticks=[lx(v) for v in (0.01, 0.03, 0.1, 0.3)],
                   y_ticks=[lx(v) for v in (1, 2, 5, 10, 20, 50)], numbers=False,
                   x_label="listening range ε", y_label="camps (count)")
        ax2.move_to([-1.2, -0.05, 0])
        xt = VGroup(*[MathTex(s, font_size=MATH_SMALL, color=GRAY).next_to(ax2.c2p(lx(v), lx(0.85)),
                                                                           DOWN, buff=0.2)
                      for s, v in (("0.01", 0.01), ("0.03", 0.03), ("0.1", 0.1), ("0.3", 0.3))])
        yt = VGroup(*[MathTex(str(v), font_size=MATH_SMALL, color=GRAY).next_to(ax2.c2p(lx(0.0085), lx(v)),
                                                                               LEFT, buff=0.2)
                      for v in (1, 2, 5, 10, 20, 50)])
        ax2.x_title.next_to(xt, DOWN, buff=0.15).align_to(ax2.x_axis.get_right(), RIGHT)
        ax2.y_title.next_to(ax2.y_axis.get_top(), UP, buff=0.2).align_to(yt, LEFT)
        rule_line = ax2.plot(lambda u: lx(1 / (2 * 10 ** u)), x_range=[lx(0.01), lx(0.3)],
                             color=YELLOW, stroke_width=4)
        whisk = VGroup(*[Line(ax2.c2p(lx(s["eps"]), lx(s["min"])), ax2.c2p(lx(s["eps"]), lx(s["max"])),
                              color=BLUE, stroke_width=3) for s in SWEEP])
        mdots = VGroup(*[Dot(ax2.c2p(lx(s["eps"]), lx(s["mean"])), radius=0.08, color=BLUE)
                         for s in SWEEP])
        sim2 = label("simulated · 625 people · 20 runs each", size=SMALL + 2, color=GRAY)
        sim2.move_to([SAFE_X - sim2.width / 2, SAFE_TOP - 0.1 - sim2.height / 2, 0])
        f_small = MathTex(r"{1", r"\over", r"2\varepsilon}", font_size=MATH, color=YELLOW)
        f_small.next_to(ax2.c2p(lx(0.05), lx(10)), UR, buff=0.25)
        s25 = SWEEP[8]
        hi_rule = Circle(radius=0.16, color=YELLOW, stroke_width=3).move_to(ax2.c2p(lx(0.25), lx(2)))
        hi_meas = Circle(radius=0.16, color=BLUE, stroke_width=3).move_to(mdots[8])
        drop = Arrow(ax2.c2p(lx(0.25), lx(2)) + DOWN * 0.16, mdots[8].get_center() + UP * 0.14,
                     buff=0, color=INK, stroke_width=3, tip_length=0.15, max_tip_length_to_length_ratio=0.5)
        with self.narrate("Is that close enough? Here are listening ranges from point oh one to "
                          "point three, each run twenty times with six hundred and twenty five "
                          "simulated people. Both axes are logarithmic, so the rule is this "
                          "straight yellow line. The real counts run parallel, at about three "
                          "quarters of the rule, because most camps gather a bit more than two "
                          "epsilon. And at point two five, the rule still promises two camps, "
                          "while almost every run ends in one.") as beat:
            keep = VGroup(f1)
            self.play(*[FadeOut(m) for m in self.mobjects if m not in (f1, sim_tag)],
                      f1.animate.scale(0.8).move_to([4.6, 2.2, 0]), FadeOut(sim_tag),
                      run_time=1.0)
            self.play(Create(ax2), FadeIn(xt), FadeIn(yt), FadeIn(sim2),
                      run_time=beat.until("each run", offset=-0.1))
            self.play(LaggedStart(*[AnimationGroup(Create(w), FadeIn(d, scale=0.5))
                                    for w, d in zip(whisk, mdots)], lag_ratio=0.25),
                      run_time=beat.until("Both axes"))
            beat.wait_until("straight", offset=-0.3)
            self.play(Create(rule_line), TransformFromCopy(f1[2:5], f_small),
                      FadeOut(f1), run_time=beat.until("The real", offset=-0.1))
            ghost = rule_line.copy().set_stroke(color=BLUE, width=3, opacity=0.8)
            ghost_target = ax2.plot(lambda u: lx(0.775 / (2 * 10 ** u)), x_range=[lx(0.01), lx(0.15)],
                                    color=BLUE, stroke_width=3).set_stroke(opacity=0.8)
            dashed = DashedVMobject(ghost_target, num_dashes=40)
            self.play(Transform(ghost, ghost_target), run_time=beat.until("three quarters"))
            q = MathTex(r"\times\,0.78", font_size=MATH, color=BLUE)
            q.next_to(ax2.c2p(lx(0.022), lx(0.775 / 0.044)), DL, buff=0.15)
            self.play(Write(q), run_time=beat.until("because", offset=-0.1))
            self.play(ReplacementTransform(ghost, dashed), run_time=beat.until("And at", offset=-0.1))
            self.play(Create(hi_rule), run_time=beat.until("while", offset=-0.1))
            self.play(GrowArrow(drop), Create(hi_meas), run_time=beat.remaining(min_time=1.0))

        # ============================================================ 8. payoff: HK 2002
        hk_pts = [(0.01, 38), (0.15, 2), (0.25, 1)]
        rings = VGroup(*[Circle(radius=0.2, color=INK, stroke_width=3).move_to(ax2.c2p(lx(e), lx(c)))
                         for e, c in hk_pts])
        ring_labs = VGroup(
            MathTex("38", font_size=MATH, color=INK).next_to(rings[0], RIGHT, buff=0.15),
            MathTex("2", font_size=MATH, color=INK).next_to(rings[1], UP, buff=0.15),
            MathTex("1", font_size=MATH, color=INK).next_to(rings[2], LEFT, buff=0.12).shift(DOWN * 0.3),
        )
        legend_ring = Circle(radius=0.14, color=INK, stroke_width=3)
        legend_txt = label("one published run each", size=LABEL)
        legend = VGroup(legend_ring, legend_txt).arrange(RIGHT, buff=0.2)
        legend.move_to([SAFE_X - legend.width / 2, 1.25, 0])
        cite_hk = citation("Hegselmann & Krause, 2002 · J. Artificial Societies and Social Simulation")
        with self.narrate("That set-up is Hegselmann and Krause's, from two thousand two: six "
                          "hundred and twenty five random opinions. With a range of point oh one, "
                          "thirty eight opinions survived. At point one five, two camps. At point "
                          "two five, consensus. Each of their single runs falls inside what our "
                          "twenty runs produced. These are models, and how closely real people "
                          "update this way is still thinly tested.") as beat:
            self.play(FadeOut(hi_rule), FadeOut(drop), FadeOut(hi_meas), FadeIn(cite_hk),
                      FadeIn(legend), run_time=beat.until("With", offset=-0.1))
            self.play(Create(rings[0]), run_time=beat.until("thirty", offset=-0.1))
            self.play(Write(ring_labs[0]), run_time=beat.until("At point one", offset=-0.1))
            self.play(Create(rings[1]), Write(ring_labs[1]), run_time=beat.until("At point two", offset=-0.1))
            self.play(Create(rings[2]), Write(ring_labs[2]), run_time=beat.until("Each of", offset=-0.1))
            self.play(*[flag(m) for m in (mdots[0], mdots[6], mdots[8])],
                      *[Indicate(w, color=INK, scale_factor=1.0) for w in (whisk[0], whisk[6], whisk[8])],
                      run_time=beat.until("These are", offset=-0.3))
            rest = [m for m in self.mobjects if m is not cite_hk]
            self.play(*[m.animate.set_opacity(0.3) for m in rest], run_time=beat.remaining(min_time=1.0))

        # ============================================================ 9. landing
        line2 = line.copy()
        nums2 = line_nums.copy()
        lab2 = line_lab.copy()
        posF = stack_positions(HK[-1], ox, LINE_Y, min_dx=0.0)
        people2 = VGroup(*[Dot(p, radius=0.06, color=BLUE) for p in pos0])
        # final camps: stack each camp in a neat column
        for k, c in enumerate(CAMPS):
            members = [i for i in range(N) if LAB[i] == k]
            for j, i in enumerate(members):
                col = j % 2
                posF[i] = [ox(c) + (col - 0.5) * 0.14, LINE_Y + 0.16 + 0.135 * (j // 2), 0]
        wins = VGroup()
        for c in CAMPS:
            h = 0.16 + 0.135 * 18
            r = Rectangle(width=ox(c + EPS) - ox(c - EPS), height=h, stroke_width=0,
                          fill_color=YELLOW, fill_opacity=0.14).move_to([ox(c), LINE_Y + h / 2, 0])
            wins.add(r)
        with self.narrate("Back to the first picture. Every one of these hundred people "
                          "compromised, every round. The four camps were settled the moment we "
                          "chose how far they would listen.") as beat:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)
            self.play(Create(line2), FadeIn(nums2), FadeIn(lab2), FadeIn(people2),
                      run_time=beat.until("Every one", offset=-0.1))
            self.play(*[people2[i].animate.move_to(posF[i]) for i in range(N)],
                      run_time=beat.until("The four", offset=-0.1), rate_func=SMOOTH)
            beat.wait_until("listen", offset=-0.9)
            self.play(LaggedStart(*[FadeIn(w) for w in wins], lag_ratio=0.2),
                      run_time=beat.remaining(min_time=1.2))
        self.end_card()
