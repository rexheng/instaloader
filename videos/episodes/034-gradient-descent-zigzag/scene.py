"""Episode 34 - Why Gradient Descent Zigzags.

    videos/toolkit/render.sh --preview videos/episodes/034-gradient-descent-zigzag/scene.py Episode /tmp/ep34.mp4
    videos/toolkit/render.sh videos/episodes/034-gradient-descent-zigzag/scene.py Episode \
        videos/episodes/034-gradient-descent-zigzag/final.mp4

Model (simulated, exact): f(x, y) = 1/2 (x^2 + 25 y^2), start (-5, 0.7).  Every number on
screen is recomputed in sim.py next to this file.
"""
import math

import numpy as np
from manim import *
from sample_space import *

K = 25.0
SQ5 = math.sqrt(5.0)
START = np.array([-5.0, 0.7])
UX = math.sqrt(START[0] ** 2 + K * START[1] ** 2)       # outer contour semi-axis (6.10)
LEVELS = [1.0, 0.8, 0.6, 0.4, 0.2]                       # contour radii as fractions
C0 = np.array([0.0, -0.1, 0.0])


def gd_path(k, eta, n, beta=0.0, start=START):
    """Plain (beta = 0) or heavy-ball gradient descent on 1/2 (x^2 + k y^2)."""
    h = np.array([1.0, k])
    x = start.astype(float).copy()
    prev = x.copy()
    pts = [x.copy()]
    for _ in range(n):
        xn = x - eta * h * x + beta * (x - prev)
        prev, x = x, xn
        pts.append(x.copy())
    return pts


def steps_needed(k):
    return math.ceil(math.log(1000) / math.log((k + 1) / (k - 1)))


def rot(deg):
    a = math.radians(deg)
    return np.array([[math.cos(a), -math.sin(a)], [math.sin(a), math.cos(a)]])


class Episode(NarratedScene):
    EPISODE = 34
    TITLE = "Why Gradient Descent Zigzags"
    SPEED = 0.82
    PRONUNCIATIONS = {
        "Cauchy's": "koh sheez",
        "LeCun": "luh kun",
        "Polyak": "pole yak",
        "eta": "ayta",
        "kappa": "kappa",
    }

    # ------------------------------------------------------------------ map helpers
    def P(self, uv):
        """Model coordinates -> screen point under the current map transform."""
        v = self.A @ np.asarray(uv, float)
        return self.c + np.array([v[0], v[1], 0.0])

    def warp(self, mobs, A_new, c_new):
        """Animations that carry every point of `mobs` from the current map transform to
        a new one (the picture is re-drawn, so this is a change of coordinates)."""
        M = A_new @ np.linalg.inv(self.A)
        c_old = self.c.copy()
        M3 = np.eye(3)
        M3[:2, :2] = M

        def f(p):
            return c_new + M3 @ (p - c_old)
        anims = [m.animate.apply_function(f) for m in mobs]
        self.A, self.c = A_new, np.array(c_new, float)
        return anims

    def contours(self):
        g = VGroup()
        for i, r in enumerate(LEVELS):
            e = Ellipse(width=2 * r * UX, height=2 * r * UX / SQ5 / SQ5,
                        stroke_color=GRAY, stroke_width=2.2,
                        stroke_opacity=0.95 - 0.12 * i)
            g.add(e)
        g.apply_matrix(np.pad(self.A, ((0, 1), (0, 1))) + np.diag([0, 0, 1]))
        g.shift(self.c)
        return g

    def descent_arrow(self, uv, length=1.7, to_center=False):
        p = self.P(uv)
        if to_center:
            d = self.c - p
        else:
            g = self.A @ (-np.array([1.0, self.k]) * np.asarray(uv))
            d = np.array([g[0], g[1], 0.0])
        d = d / np.linalg.norm(d)
        return Arrow(p, p + length * d, buff=0, color=PURPLE, stroke_width=6,
                     max_tip_length_to_length_ratio=0.18)

    def run(self, pts_uv, color, run_time, counter=None, rate=LINEAR, width=3.5):
        """Trace a descent path; the ball rides its end, the counter shows the step."""
        pts = [self.P(p) for p in pts_uv]
        path = VMobject(stroke_color=color, stroke_width=width)
        path.set_points_as_corners([pts[0], pts[0] + 1e-3 * RIGHT])
        k = ValueTracker(0)
        n = len(pts) - 1

        def upd(m):
            t = min(k.get_value(), n)
            i = int(t)
            fr = t - i
            cur = list(pts[:i + 1])
            if i < n:
                cur.append(pts[i] + fr * (pts[i + 1] - pts[i]))
            if len(cur) < 2:
                cur.append(cur[0] + 1e-3 * RIGHT)
            m.set_points_as_corners(cur)
        path.add_updater(upd)
        self.ball.add_updater(lambda b: b.move_to(path.get_end()))
        if counter is not None:
            counter.add_updater(lambda d: d.set_value(int(min(k.get_value(), n) + 1e-6)))
        self.add(path)
        self.bring_to_front(self.ball)
        self.play(k.animate.set_value(n), run_time=run_time, rate_func=rate)
        path.clear_updaters()
        self.ball.clear_updaters()
        if counter is not None:
            counter.clear_updaters()
            counter.set_value(n)
        return path

    # ------------------------------------------------------------------ counter
    def counter_value(self, mob):
        mob.next_to(self.cnt_label, RIGHT, buff=0.25)
        mob.align_to(self.cnt_label, DOWN) if not isinstance(mob, DecimalNumber) else None
        return mob

    def set_counter(self, mob, run_time=0.5):
        self.counter_value(mob)
        self.play(FadeTransform(self.cnt_val, mob), run_time=run_time)
        self.cnt_val = mob

    def number(self, v, color=YELLOW):
        d = DecimalNumber(v, num_decimal_places=0, font_size=EQ, color=color)
        return d

    # ------------------------------------------------------------------ the episode
    def construct(self):
        self.k = K
        self.A = np.diag([1 / SQ5, SQ5])            # round bowl
        self.c = C0.copy()

        # ============================================================ cold open
        rings = self.contours()
        bottom = VGroup(Line(LEFT * 0.09 + UP * 0.09, RIGHT * 0.09 + DOWN * 0.09),
                        Line(LEFT * 0.09 + DOWN * 0.09, RIGHT * 0.09 + UP * 0.09)
                        ).set_stroke(INK, 3).move_to(self.c)
        self.ball = Dot(self.P(START), radius=0.12, color=YELLOW).set_z_index(5)
        self.cnt_label = text("steps", size=LABEL, color=GRAY)
        self.cnt_label.move_to([3.9, 3.15, 0])
        self.cnt_val = self.number(0)
        self.counter_value(self.cnt_val)

        with self.narrate("This ball always steps the steepest way downhill. "
                          "In a round bowl, one step lands it on the bottom.") as beat:
            self.add(rings, bottom, self.ball)
            self.play(LaggedStart(*[Create(r) for r in rings], lag_ratio=0.15),
                      run_time=beat.until("steepest"))
            arrow = self.descent_arrow(START, length=1.6, to_center=True)
            self.play(GrowArrow(arrow), run_time=beat.until("downhill", end=True))
            beat.wait_until("one step", offset=-0.1)
            one = self.number(1)
            self.counter_value(one)
            self.play(self.ball.animate.move_to(self.c), FadeOut(arrow),
                      FadeIn(self.cnt_label), FadeIn(one), run_time=1.0)
            self.cnt_val = one

        q = text("?", size=TITLE, color=YELLOW)
        ratio = formula(r"5", r":", r"1", size=MATH, color=GRAY)
        with self.narrate("Stretch the bowl five times longer than it is wide. "
                          "How many steps now? [pause 1.5]") as beat:
            self.play(self.ball.animate.move_to(self.P(START)), run_time=0.6)
            self.k = K
            anims = self.warp([rings], np.eye(2), C0)
            self.play(*anims, self.ball.animate.move_to(self.P(START)),
                      run_time=beat.until("wide", end=True))
            ratio.next_to(rings, DOWN, buff=0.35)
            arrow = self.descent_arrow(START)
            self.play(FadeIn(ratio, shift=0.1 * UP), GrowArrow(arrow), run_time=0.9)
            beat.wait_until("How many", offset=-0.1)
            self.set_counter(q, run_time=0.6)
            self.play(flag(q), run_time=0.8)

        # ============================================================ stakes
        to_bottom = DashedLine(self.ball.get_center(), self.c, color=INK, stroke_width=2.5,
                               dash_length=0.12).set_z_index(1)
        goal = formula(r"\text{arrived: } d \div 1000", size=MATH_SMALL + 4, color=GRAY)
        goal.next_to(self.cnt_label, DOWN, buff=0.3, aligned_edge=LEFT)
        d_lab = formula(r"d", size=MATH, color=INK).next_to(to_bottom.get_center(), UP, buff=0.12)
        allow_overlap(d_lab.add_background_rectangle(color=BG, opacity=1, buff=0.05))
        cost = text("1 step = 1 pass over the data", size=SMALL + 2, color=GRAY)
        cost.next_to(goal, DOWN, buff=0.22, aligned_edge=LEFT)
        with self.narrate("Give it the best step size there is, and call it arrived once it is "
                          "a thousand times closer than at the start. Every step costs a full "
                          "pass over the data, and nearly every neural network trains on some "
                          "version of this rule, so that count is the bill.") as beat:
            beat.wait_until("arrived", offset=-0.2)
            self.play(Create(to_bottom), FadeIn(d_lab), run_time=0.8)
            beat.wait_until("thousand", offset=-0.2)
            self.play(Write(goal), run_time=0.9)
            beat.wait_until("full", offset=-0.2)
            self.play(FadeIn(cost, shift=0.1 * DOWN), run_time=0.8)
            beat.wait_until("count", offset=-0.1)
            self.play(flag(self.cnt_val), run_time=0.8)

        # ============================================================ naive build
        rule = formula(r"p", r"\;\leftarrow\;", r"p", r"-", r"\eta", r"\,", r"\nabla f", size=EQ)
        rule[6].set_color(PURPLE)
        rule.move_to([-2.2, 3.05, 0])
        eta_lab = formula(r"\eta", r"=", r"?", size=MATH)
        eta_lab.move_to([-4.0, 2.25, 0])
        cite_c = citation("Cauchy, 1847 · Comptes Rendus de l'Académie des Sciences")
        p_lab = formula(r"p", size=MATH, color=YELLOW).next_to(self.ball, UL, buff=0.1)
        tangent_dir = np.array([-START[1] * K, START[0], 0.0])        # perpendicular to grad
        tangent_dir /= np.linalg.norm(tangent_dir)
        tangent = Line(self.ball.get_center() - 0.9 * tangent_dir,
                       self.ball.get_center() + 0.9 * tangent_dir, color=INK, stroke_width=3)
        with self.narrate("The rule is Cauchy's, from eighteen forty seven: the steepest way "
                          "down is this arrow, square to the contour line. Step along it, "
                          "scaled by a step size, eta.") as beat:
            self.play(FadeOut(d_lab), FadeOut(to_bottom), FadeOut(cost), FadeIn(cite_c),
                      run_time=0.8)
            beat.wait_until("this arrow", offset=-0.15)
            self.play(flag(arrow, color=PURPLE), run_time=0.8)
            beat.wait_until("square", offset=-0.1)
            ra = RightAngle(tangent, Line(self.ball.get_center(), arrow.get_end()), length=0.25,
                            quadrant=(1, 1), color=INK, stroke_width=2.5)
            self.play(Create(tangent), Create(ra), run_time=0.9)
            beat.wait_until("Step", offset=-0.1)
            self.play(FadeIn(p_lab), Write(rule[0:4]), run_time=1.0)
            self.play(TransformFromCopy(arrow, rule[6]), FadeIn(rule[5]),
                      run_time=beat.until("step size"))
            self.play(Write(rule[4]), run_time=0.6)
            beat.wait_until("eta", offset=-0.1)
            self.play(TransformFromCopy(rule[4], eta_lab[0]), Write(eta_lab[1:]), run_time=0.9)

        # big step -> diverges
        def set_eta(s):
            new = formula(r"\eta", r"=", s, size=MATH).move_to(eta_lab, aligned_edge=LEFT)
            return Transform(eta_lab, new)

        big = gd_path(K, 0.1, 6)
        with self.narrate("Try a big step, point one. The ball ricochets from wall to wall, "
                          "each bounce higher than the last, and it is gone.") as beat:
            self.play(FadeOut(tangent), FadeOut(ra), FadeOut(p_lab), FadeOut(cite_c),
                      run_time=beat.until("point one", offset=-0.1))
            zero = self.number(0)
            self.counter_value(zero)
            self.play(set_eta("0.1"), FadeOut(self.cnt_val), FadeIn(zero), FadeOut(arrow),
                      run_time=0.7)
            self.cnt_val = zero
            beat.wait_until("ricochets", offset=-0.2)
            path_big = self.run(big, YELLOW, beat.until("gone"), counter=self.cnt_val,
                                rate=lambda t: t ** 1.3)
            inf = formula(r"\infty", size=EQ, color=YELLOW)
            self.set_counter(inf, run_time=0.6)

        # tiny step -> crawls
        crawl = gd_path(K, 0.005, 1377)
        with self.narrate("Shrink it to point oh oh five. Now it slides down the wall and "
                          "crawls along the floor, for thirteen hundred and seventy seven "
                          "steps.") as beat:
            self.ball.move_to(self.P(START))
            zero = self.number(0)
            self.counter_value(zero)
            self.play(FadeOut(path_big), FadeIn(self.ball), set_eta("0.005"),
                      FadeOut(self.cnt_val), FadeIn(zero), run_time=beat.until("slides", offset=-0.1))
            self.cnt_val = zero
            path_crawl = self.run(crawl, YELLOW, beat.until("thirteen", offset=0.2),
                                  counter=self.cnt_val, rate=lambda t: t ** 2.2)
            self.play(flag(self.cnt_val), run_time=0.8)

        # tuned step -> zigzag
        best = gd_path(K, 2 / (K + 1), 87)
        with self.narrate("The best step size sits in between, at point oh seven seven. The ball "
                          "zigzags across the valley and arrives after eighty seven "
                          "steps.") as beat:
            zero = self.number(0)
            self.counter_value(zero)
            self.play(path_crawl.animate.set_stroke(opacity=0.25),
                      self.ball.animate.move_to(self.P(START)),
                      FadeOut(self.cnt_val), FadeIn(zero), run_time=0.8)
            self.cnt_val = zero
            self.play(set_eta("0.077"), run_time=beat.until("zigzags", offset=-0.1))
            path_best = self.run(best, YELLOW, beat.until("eighty", offset=0.3),
                                 counter=self.cnt_val, rate=lambda t: t ** 1.6)
            self.play(flag(self.cnt_val), FadeOut(path_crawl), run_time=0.8)

        # ============================================================ fail: name the cause
        with self.narrate("Eighty seven, for a bottom in plain sight. Look at the arrow: it "
                          "points across the valley, not along it.") as beat:
            self.play(path_best.animate.set_stroke(opacity=0.3),
                      self.ball.animate.move_to(self.P(START)), run_time=0.9)
            to_bottom = DashedLine(self.ball.get_center(), self.c, color=INK, stroke_width=2.5,
                                   dash_length=0.12)
            beat.wait_until("plain sight", offset=-0.2)
            self.play(Create(to_bottom), run_time=0.8)
            arrow = self.descent_arrow(START)
            beat.wait_until("arrow", offset=-0.2)
            self.play(GrowArrow(arrow), run_time=0.8)
            ang = Angle(to_bottom, Line(self.ball.get_center(), arrow.get_end()), radius=0.75,
                        quadrant=(1, 1), other_angle=True, color=INK, stroke_width=2.5)
            deg = math.degrees(math.atan2(K * START[1], -START[0]) -
                               math.atan2(START[1], -START[0]))
            ang_lab = formula(rf"{deg:.0f}^\circ", size=MATH_SMALL + 4)
            ang_lab.move_to(self.ball.get_center() + 1.2 * np.array([0.62, -0.5, 0]))
            allow_overlap(ang_lab.add_background_rectangle(color=BG, opacity=1, buff=0.05))
            beat.wait_until("across", offset=-0.2)
            self.play(Create(ang), FadeIn(ang_lab), run_time=0.9)

        # ============================================================ insight: split the arrow
        bp = self.ball.get_center()
        tip = arrow.get_end()
        g_arr = Arrow(bp, [tip[0], bp[1], 0], buff=0, color=GREEN, stroke_width=6,
                      max_tip_length_to_length_ratio=0.45, max_stroke_width_to_length_ratio=20)
        r_arr = Arrow(bp, [bp[0], tip[1], 0], buff=0, color=RED, stroke_width=6,
                      max_tip_length_to_length_ratio=0.18)
        x_brace = BraceBetweenPoints([bp[0], 1.55, 0], [self.c[0], 1.55, 0], UP, color=GREEN)
        x_lab = formula(r"x", size=MATH, color=GREEN).next_to(x_brace, UP, buff=0.1)
        y_brace = BraceBetweenPoints([-5.45, self.c[1], 0], [-5.45, bp[1], 0], LEFT,
                                     color=RED, buff=0.05)
        y_lab = formula(r"y", size=MATH, color=RED).next_to(y_brace, LEFT, buff=0.1)
        allow_overlap(y_brace)
        g_lab = formula(r"1", r"\cdot", r"x", size=MATH, color=GREEN)
        g_lab.next_to(g_arr, UP, buff=0.35).shift(RIGHT * 0.35)
        r_lab = formula(r"25", r"\cdot", r"y", size=MATH, color=RED)
        r_lab.next_to(r_arr.get_end(), LEFT, buff=0.25)
        f_lab = formula(r"f", r"=", r"\tfrac12", r"(", r"x^2", r"+", r"25", r"y^2", r")",
                        size=MATH_SMALL + 4, color=GRAY)
        f_lab.move_to([3.7, -2.05, 0])
        sim_tag = text("simulated valley", size=SMALL, color=GRAY).next_to(f_lab, DOWN, buff=0.18)
        sq = formula(r"25", r"=", r"5^2", size=MATH_SMALL + 4, color=RED)
        sq.next_to(r_lab, DOWN, buff=0.3).align_to(r_lab, RIGHT)
        with self.narrate("Split the arrow in two. Along the valley, the slope is the distance "
                          "to the bottom, times one. Across, it is the distance times twenty "
                          "five: walls five times closer bend five squared times as "
                          "sharply.") as beat:
            self.play(FadeOut(ang), FadeOut(ang_lab), FadeOut(to_bottom), run_time=0.5)
            self.play(TransformFromCopy(arrow, g_arr), TransformFromCopy(arrow, r_arr),
                      arrow.animate.set_opacity(0.35), run_time=beat.until("Along", offset=-0.1))
            self.play(GrowFromCenter(x_brace), FadeIn(x_lab), run_time=beat.until("times one", offset=-0.2))
            self.play(TransformFromCopy(x_lab, g_lab[2]), FadeIn(g_lab[0:2]), run_time=0.9)
            beat.wait_until("Across", offset=-0.1)
            self.play(GrowFromCenter(y_brace), FadeIn(y_lab), run_time=0.8)
            self.play(TransformFromCopy(y_lab, r_lab[2]), FadeIn(r_lab[0:2]),
                      FadeIn(f_lab), FadeIn(sim_tag),
                      run_time=beat.until("walls", offset=-0.1))
            beat.wait_until("squared", offset=-0.3)
            self.play(TransformFromCopy(r_lab[0], sq[0]), FadeIn(sq[1:]), run_time=0.9)

        # per-step multipliers, built from the component labels
        g_mul = formula(r"x", r"\;\to\;", r"(1-\eta)", r"\,x", size=MATH, color=GREEN)
        r_mul = formula(r"y", r"\;\to\;", r"(1-25\eta)", r"\,y", size=MATH, color=RED)
        g_mul.move_to([-2.2, -2.0, 0])
        r_mul.move_to([2.6, -2.0, 0]).align_to(g_mul, DOWN)
        with self.narrate("So each step multiplies the distance along by one minus eta, and "
                          "the distance across by one minus twenty five eta.") as beat:
            self.play(FadeOut(sq), run_time=0.4)
            self.play(TransformFromCopy(g_lab, g_mul), run_time=beat.until("one minus", offset=-0.2))
            self.play(flag(g_mul[2], color=GREEN), run_time=0.8)
            beat.wait_until("across", offset=-0.2)
            self.play(TransformFromCopy(r_lab, r_mul), run_time=beat.until("one minus", 2, offset=-0.2))
            self.play(flag(r_mul[2], color=RED), run_time=0.8)

        # ---------------------------------------------------------------- the plot
        ax = axes((0, 0.1), (0, 1.5), x_ticks=[0, 0.02, 0.04, 0.06, 0.08, 0.1],
                  y_ticks=[0, 0.5, 1.0, 1.5], x_length=7.4, y_length=3.3,
                  x_label="step size η", y_label="fraction kept per step",
                  x_decimals=2, y_decimals=1)
        ax.move_to([-1.15, -1.05, 0])
        one_line = DashedLine(ax.c2p(0, 1), ax.c2p(0.1, 1), color=GRAY, stroke_width=2,
                              dash_length=0.1)
        kap = ValueTracker(K)

        def red_pts(k):
            e_end = min(0.1, 2.5 / k)
            return [ax.c2p(0, 1), ax.c2p(1 / k, 0), ax.c2p(e_end, k * e_end - 1)]

        def env_pts(k):
            es = 2 / (k + 1)
            e_end = min(0.1, 2.5 / k)
            return [ax.c2p(0, 1), ax.c2p(es, 1 - es), ax.c2p(e_end, k * e_end - 1)]

        green_ln = Line(ax.c2p(0, 1), ax.c2p(0.1, 0.9), color=GREEN, stroke_width=5)
        red_v = VMobject(stroke_color=RED, stroke_width=5).set_points_as_corners(red_pts(K))
        env = VMobject(stroke_color=YELLOW, stroke_width=9, stroke_opacity=0.9)
        env.set_points_as_corners(env_pts(K))
        A_ins, c_ins = 0.55 * np.eye(2), np.array([-1.6, 2.5, 0.0])
        g_leg = g_mul.copy().scale(0.85)
        r_leg = r_mul.copy().scale(0.85)
        g_leg.next_to(ax.c2p(0.1, 0.9), RIGHT, buff=0.3).shift(DOWN * 0.25)
        r_leg.next_to(ax.c2p(0.1, 1.5), RIGHT, buff=0.3)
        with self.narrate("Plot what survives of each distance after one step, against the "
                          "step size.") as beat:
            moving = [rings, path_best, arrow, g_arr, r_arr]
            fade = [x_brace, x_lab, y_brace, y_lab, g_lab, r_lab, f_lab, sim_tag]
            ball_target = None
            anims = self.warp(moving, A_ins, c_ins)
            ball_target = self.P(START)
            self.play(*anims, self.ball.animate.move_to(ball_target).scale(0.7),
                      bottom.animate.move_to(c_ins),
                      *[FadeOut(m) for m in fade], FadeOut(rule), FadeOut(eta_lab),
                      FadeOut(ratio), FadeOut(goal), run_time=1.3)
            self.play(Create(ax), run_time=1.0)
            self.play(Create(one_line), Transform(g_mul, g_leg), Transform(r_mul, r_leg),
                      run_time=0.9)
            self.play(Create(green_ln), Create(red_v), run_time=beat.remaining(1.0))

        big_dot = Dot(ax.c2p(0.1, 1.5), radius=0.09, color=RED)
        small_dot = Dot(ax.c2p(0.005, 0.995), radius=0.09, color=GREEN)
        big_tag = formula(r"\eta=0.1", size=MATH_SMALL, color=INK).next_to(big_dot, LEFT, buff=0.2)
        small_tag = formula(r"\eta=0.005", size=MATH_SMALL, color=INK)
        small_tag.next_to(small_dot, UP, buff=0.25).shift(RIGHT * 0.55)
        with self.narrate("Past point oh eight, the red V climbs above one. Our big step sat up "
                          "here, so the distance across grew every bounce. The green line "
                          "barely dips below one, and that is where our small step "
                          "crawled.") as beat:
            beat.wait_until("eight", offset=-0.2)
            mark = Dot(ax.c2p(0.08, 1), radius=0.07, color=INK)
            self.play(FadeIn(mark, scale=0.5), flag(red_v, color=RED), run_time=0.9)
            beat.wait_until("here", offset=-0.25)
            self.play(FadeIn(big_dot, scale=0.5), FadeIn(big_tag), run_time=0.8)
            beat.wait_until("green", offset=-0.2)
            self.play(flag(green_ln, color=GREEN), run_time=0.8)
            beat.wait_until("small", offset=-0.2)
            self.play(FadeIn(small_dot, scale=0.5), FadeIn(small_tag), run_time=0.8)

        cross = Dot(ax.c2p(2 / (K + 1), 1 - 2 / (K + 1)), radius=0.11, color=YELLOW).set_z_index(4)
        cross_val = DecimalNumber(1 - 2 / (K + 1), num_decimal_places=3, font_size=MATH_SMALL + 4,
                                  color=YELLOW)
        cross_val.next_to(cross, DOWN, buff=0.25).shift(RIGHT * 0.45)
        power = formula(r"0.923", r"^{87}", r"\approx", r"\tfrac{1}{1000}", size=MATH)
        power[0].set_color(YELLOW)
        power[1].set_color(YELLOW)
        power.move_to([4.3, -2.25, 0])
        with self.narrate("The ball is only as fast as its slower direction, this upper edge. "
                          "Its lowest point is the crossing: point nine two three per step, "
                          "which takes eighty seven steps to shrink a thousandfold.") as beat:
            self.play(FadeOut(mark), FadeOut(big_tag), FadeOut(small_tag), run_time=0.5)
            beat.wait_until("upper edge", offset=-0.3)
            self.play(Create(env), run_time=1.2)
            beat.wait_until("crossing", offset=-0.2)
            self.play(FadeIn(cross, scale=0.4), run_time=0.6)
            self.play(Write(cross_val), run_time=beat.until("per step", end=True))
            self.play(TransformFromCopy(cross_val, power[0]), run_time=0.9)
            beat.wait_until("eighty", offset=-0.2)
            self.play(TransformFromCopy(self.cnt_val, power[1]), Write(power[2:]), run_time=1.0)

        # kappa
        k_eq = formula(r"\kappa", r"=", size=MATH, color=RED)
        k_num = DecimalNumber(K, num_decimal_places=0, font_size=MATH, color=RED)
        frac = formula(r"\frac{\kappa-1}{\kappa+1}", r"\approx", size=MATH)
        frac_num = DecimalNumber(1 - 2 / (K + 1), num_decimal_places=3, font_size=MATH,
                                 color=YELLOW)
        k_eq.move_to([3.4, 2.05, 0])
        k_num.next_to(k_eq, RIGHT, buff=0.15)
        frac.next_to(k_eq, DOWN, buff=0.35, aligned_edge=LEFT)
        frac_num.next_to(frac, RIGHT, buff=0.15)
        with self.narrate("Call the steepness ratio kappa. The crossing always sits at kappa "
                          "minus one, over kappa plus one.") as beat:
            self.play(FadeOut(big_dot), FadeOut(small_dot), FadeIn(k_eq),
                      TransformFromCopy(r_mul[2][3:5], k_num), run_time=beat.until("crossing", offset=-0.1))
            self.play(flag(cross), run_time=0.7)
            self.play(Write(frac), run_time=beat.until("plus one", end=True, offset=-0.3))
            self.play(TransformFromCopy(cross_val, frac_num), run_time=0.9)

        # prediction: twice as narrow
        q2 = text("?", size=TITLE, color=YELLOW)
        with self.narrate("Now make the valley twice as narrow. Does the step count double? "
                          "[pause 1.5]") as beat:
            beat.wait_until("twice", offset=-0.2)
            squeeze = self.warp([rings, path_best, arrow, g_arr, r_arr],
                                0.55 * np.diag([1.0, 0.5]), c_ins)
            self.play(*squeeze, self.ball.animate.move_to(self.P(START)),
                      run_time=beat.until("narrow", end=True))
            beat.wait_until("double", offset=-0.3)
            self.set_counter(q2, run_time=0.6)
            self.play(flag(q2), run_time=0.8)

        cnt346 = self.number(87)
        self.counter_value(cnt346)
        times4 = formula(r"\times 4", size=MATH, color=YELLOW)
        r_leg2 = formula(r"y", r"\;\to\;", r"(1-100\eta)", r"\,y", size=MATH, color=RED)
        r_leg2.scale(0.85).move_to(r_mul, aligned_edge=LEFT)
        k_def = formula(r"\kappa", r"=", r"(\text{length}/\text{width})^2", size=MATH_SMALL + 4,
                        color=RED)
        k_def.move_to([-1.6, 1.35, 0])
        with self.narrate("Kappa becomes a hundred. The V steepens, the crossing climbs to point "
                          "nine eight, and the count jumps to three hundred and forty six: four "
                          "times. Cost grows with kappa, the narrowness squared.") as beat:
            red_v.add_updater(lambda m: m.set_points_as_corners(red_pts(kap.get_value())))
            env.add_updater(lambda m: m.set_points_as_corners(env_pts(kap.get_value())))
            cross.add_updater(lambda m: m.move_to(ax.c2p(2 / (kap.get_value() + 1),
                                                          1 - 2 / (kap.get_value() + 1))))
            k_num.add_updater(lambda m: m.set_value(kap.get_value()))
            frac_num.add_updater(lambda m: m.set_value(1 - 2 / (kap.get_value() + 1)))
            cross_val.add_updater(lambda m: m.set_value(1 - 2 / (kap.get_value() + 1)))
            cross_val.add_updater(lambda m: m.next_to(cross, DOWN, buff=0.25).shift(RIGHT * 0.45))
            cnt346.add_updater(lambda m: m.set_value(steps_needed(kap.get_value())))
            self.play(FadeOut(power), FadeTransform(self.cnt_val, cnt346), run_time=0.6)
            self.cnt_val = cnt346
            self.play(kap.animate.set_value(100), Transform(r_mul, r_leg2),
                      run_time=beat.until("three hundred", offset=-0.2), rate_func=SMOOTH)
            for m in (red_v, env, cross, k_num, frac_num, cross_val, cnt346):
                m.clear_updaters()
            times4.next_to(cnt346, RIGHT, buff=0.3)
            beat.wait_until("four", offset=-0.2)
            self.play(FadeIn(times4, shift=0.1 * LEFT), run_time=0.7)
            beat.wait_until("narrowness", offset=-0.3)
            self.play(Write(k_def), run_time=1.0)

        # ============================================================ payoff 1: rescale
        plot_stuff = [ax, one_line, green_ln, red_v, env, cross, cross_val, g_mul, r_mul,
                      k_eq, k_num, frac, frac_num, k_def, times4]
        cite_l = citation("LeCun, Bottou, Orr & Müller, 1998 · Neural Networks: Tricks of the Trade")
        lecun = formula(r"\text{convergence time}", r"\;\propto\;", r"\kappa", size=MATH)
        lecun[2].set_color(RED)
        lecun.move_to([-1.0, 3.1, 0])
        quote2 = text("scale inputs to similar variances", size=LABEL, color=INK)
        quote2.next_to(lecun, DOWN, buff=0.25)
        with self.narrate("LeCun and colleagues, nineteen ninety eight: convergence time is "
                          "proportional to kappa, so scale your inputs to similar variances. "
                          "Rescale the axes, and the valley is a bowl again: one step.") as beat:
            self.play(*[FadeOut(m) for m in plot_stuff + [arrow, g_arr, r_arr, path_best]],
                      FadeIn(cite_l), run_time=0.9)
            self.play(Write(lecun), run_time=beat.until("proportional", end=True, offset=0.2))
            beat.wait_until("scale", offset=-0.2)
            self.play(FadeIn(quote2, shift=0.1 * DOWN), run_time=0.8)
            beat.wait_until("Rescale", offset=-0.1)
            self.k = K
            anims = self.warp([rings], np.diag([1 / SQ5, SQ5]), C0)
            self.play(*anims, self.ball.animate.move_to(self.P(START)).scale(1 / 0.7),
                      bottom.animate.move_to(C0), run_time=beat.until("one step", offset=-0.1))
            one = self.number(1)
            self.counter_value(one)
            self.play(self.ball.animate.move_to(self.c), FadeTransform(self.cnt_val, one),
                      run_time=0.9)
            self.cnt_val = one

        # ============================================================ limit: tilt
        A_t = 0.62 * rot(45)
        k_tilt = formula(r"\kappa", r"=", r"25", size=MATH, color=RED)
        k_tilt.move_to([4.6, 1.6, 0])
        k_tilt2 = formula(r"\kappa", r"\approx", r"40", size=MATH, color=RED).move_to(k_tilt)
        with self.narrate("That needs the valley lined up with the inputs. Tilt it forty five "
                          "degrees, and squeezing either axis only makes it thinner.") as beat:
            self.play(FadeOut(lecun), FadeOut(quote2), FadeOut(cite_l),
                      self.ball.animate.move_to(self.P(START)), run_time=0.8)
            beat.wait_until("Tilt", offset=-0.1)
            anims = self.warp([rings], A_t, C0)
            self.play(*anims, self.ball.animate.move_to(self.P(START)), FadeIn(k_tilt),
                      run_time=beat.until("squeezing", offset=-0.1))
            sq_A = np.diag([0.5, 1.0]) @ A_t
            anims = self.warp([rings], sq_A, C0)
            self.play(*anims, self.ball.animate.move_to(self.P(START)),
                      Transform(k_tilt, k_tilt2), run_time=beat.until("thinner", end=True))
            anims = self.warp([rings], A_t, C0)
            self.play(*anims, self.ball.animate.move_to(self.P(START)),
                      Transform(k_tilt, formula(r"\kappa", r"=", r"25", size=MATH,
                                                color=RED).move_to(k_tilt)), run_time=1.0)

        # ============================================================ payoff 2: momentum
        hb = gd_path(K, 4 / 36, 23, beta=4 / 9)
        plain = gd_path(K, 2 / (K + 1), 87)
        cite_p = citation("Polyak, 1964 · USSR Computational Mathematics and Mathematical Physics")
        sim2 = text("simulated", size=SMALL, color=GRAY)
        mom = formula(r"p", r"\;\leftarrow\;", r"p", r"-", r"\eta", r"\,", r"\nabla f", r"+",
                      r"\beta", r"\,(\text{last step})", size=MATH)
        mom[6].set_color(PURPLE)
        mom[8:].set_color(BLUE)
        mom.move_to([-1.6, 3.1, 0])
        with self.narrate("Polyak's fix from nineteen sixty four does not care about the tilt. "
                          "Give the ball momentum. The back and forth cancels, the push along the "
                          "floor builds, and it arrives in twenty three steps.") as beat:
            self.play(FadeIn(cite_p), FadeOut(k_tilt), run_time=0.8)
            ghost = self.run(plain, YELLOW, 1.6, rate=lambda t: t ** 1.5, width=2.5)
            self.play(ghost.animate.set_stroke(opacity=0.3), run_time=0.5)
            self.ball.set_color(BLUE).move_to(self.P(START))
            zero = self.number(0, color=BLUE)
            self.counter_value(zero)
            self.play(FadeTransform(self.cnt_val, zero), FadeIn(self.ball),
                      run_time=beat.until("momentum", offset=-0.2))
            self.cnt_val = zero
            self.play(Write(mom), run_time=1.2)
            sim2.next_to(self.cnt_label, DOWN, buff=0.3, aligned_edge=LEFT)
            path_hb = self.run(hb, BLUE, beat.until("twenty three", offset=0.1),
                               counter=self.cnt_val, rate=lambda t: t ** 1.2, width=4.5)
            self.play(flag(self.cnt_val, color=BLUE), FadeIn(sim2), run_time=0.8)

        # ============================================================ landing
        with self.narrate("So in that first bowl, the ball never aimed at the bottom. It aimed "
                          "downhill, and only in a round bowl are those the same "
                          "direction.") as beat:
            self.play(FadeOut(path_hb), FadeOut(ghost), FadeOut(mom), FadeOut(cite_p),
                      FadeOut(sim2), self.ball.animate.set_color(YELLOW), run_time=0.8)
            anims = self.warp([rings], np.diag([1 / SQ5, SQ5]), C0)
            self.play(*anims, self.ball.animate.move_to(self.P(START)),
                      FadeOut(self.cnt_val), FadeOut(self.cnt_label),
                      run_time=beat.until("never", offset=-0.1))
            line_b = DashedLine(self.ball.get_center(), self.c, color=INK, stroke_width=2.5,
                                dash_length=0.12)
            self.play(Create(line_b), run_time=beat.until("downhill", offset=-0.2))
            arrow = self.descent_arrow(START, length=1.6, to_center=True)
            self.play(GrowArrow(arrow), run_time=0.9)
            beat.wait_until("same", offset=-0.2)
            self.play(flag(arrow, color=PURPLE), run_time=0.9)

        self.end_card()
