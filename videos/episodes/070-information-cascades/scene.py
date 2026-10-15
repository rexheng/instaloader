"""Episode 70: How Rational People Join the Wrong Crowd (information cascades).

    videos/toolkit/render.sh --preview videos/episodes/070-information-cascades/scene.py Episode /tmp/ep70.mp4
"""
from pathlib import Path

import numpy as np
from manim import *
from sample_space import *

HERE = Path(__file__).resolve().parent
N = 100
P_RIGHT = 2 / 3

# one simulated line (seeded, see sim.py): True = blue ball. Draws 1-2 red, 3-4 blue, 67 blue.
LINE = np.load(HERE / "line.npy")


def simulate_lines(lines=100_000, n=N, seed=70):
    """BHW/Anderson-Holt line, true urn B, tie -> own ball. Returns per-line 'hundredth wrong'."""
    rng = np.random.default_rng(seed)
    draws = rng.random((lines, n)) < P_RIGHT
    d = np.zeros(lines, int)
    guess_blue = np.zeros(lines, bool)
    for i in range(n):
        free = np.abs(d) < 2
        guess_blue = np.where(free, draws[:, i], d > 0)
        d = np.where(free, d + np.where(draws[:, i], 1, -1), d)
    return ~guess_blue


def ball(color, r=0.26):
    return Circle(radius=r, stroke_width=0, fill_color=color, fill_opacity=1)


def urn(contents, name, color):
    body = VMobject(stroke_color=GRAY, stroke_width=5)
    body.set_points_as_corners([[-0.85, 0.75, 0], [-0.85, -0.6, 0], [0.85, -0.6, 0], [0.85, 0.75, 0]])
    spots = [[-0.34, -0.3, 0], [0.34, -0.3, 0], [0, 0.24, 0]]
    balls = VGroup(*[ball(c).move_to(s) for c, s in zip(contents, spots)])
    lab = text(f"urn {name}", size=LABEL, color=color).next_to(body, DOWN, buff=0.22)
    g = VGroup(body, balls, lab)
    g.body, g.balls, g.lab = body, balls, lab
    return g


class Episode(NarratedScene):
    EPISODE = 70
    TITLE = "How Rational People Join the Wrong Crowd"

    def construct(self):
        wrong = simulate_lines()
        # ------------------------------------------------------------ tape (persists all episode)
        xs = np.linspace(-6.0, 6.0, N)
        people = VGroup(*[Dot([x, 0, 0], radius=0.05, color=INK) for x in xs])
        balls = VGroup(*[Circle(radius=0.05, stroke_color=GRAY, stroke_width=1.5, fill_color=DIM,
                                fill_opacity=1).move_to([x, 0, 0]) for x in xs])
        PY, BY = -0.75, -1.3
        people.set_y(PY)
        balls.set_y(BY)
        pub = text("guesses: public", size=26, color=GRAY)
        priv = text("balls: private", size=26, color=GRAY)

        def place_tape_labels():
            pub.next_to(people, UP, buff=0.22).align_to(people, LEFT)
            priv.next_to(balls, DOWN, buff=0.22).align_to(balls, LEFT)
        place_tape_labels()

        # ------------------------------------------------------------ 0. cold open
        uA = urn([RED, RED, BLUE], "A", RED).move_to([-3.4, 1.75, 0])
        uB = urn([BLUE, BLUE, RED], "B", BLUE).move_to([3.4, 1.75, 0])
        for u in (uA, uB):
            u.balls.set_opacity(0)
        qmark = formula("?", size=96, color=YELLOW).move_to([0, 1.9, 0])
        last_lab = text("person 100", size=26, color=YELLOW)
        with self.narrate("One of these two urns was picked in secret. A hundred people guess "
                          "which, one at a time, out loud. How often is the hundredth guess wrong? "
                          "[pause 1.5]") as beat:
            self.play(Create(uA.body), Create(uB.body), FadeIn(uA.lab), FadeIn(uB.lab),
                      run_time=beat.until("secret", offset=-0.2))
            self.play(FadeIn(qmark, scale=0.6), run_time=0.6)
            self.play(LaggedStart(*[GrowFromCenter(d) for d in people], lag_ratio=0.02),
                      run_time=beat.until("one at a time", end=True))
            self.play(LaggedStart(*[Indicate(d, color=INK, scale_factor=1.8) for d in people],
                                  lag_ratio=0.03), run_time=beat.until("hundredth", offset=-0.15))
            last_lab.next_to(people[-1], UP, buff=0.25).align_to(people[-1], RIGHT)
            self.play(people[-1].animate.set_color(YELLOW).scale(1.6), FadeIn(last_lab, shift=0.1 * DOWN),
                      run_time=0.7)
            beat.wait_until("wrong", offset=0.3)
            self.play(Wiggle(qmark, scale_value=1.15, rotation_angle=0.03 * TAU), run_time=1.2)

        # ------------------------------------------------------------ 1. contents and 2/3
        frac = formula(r"\frac{2}{3}", size=EQ + 8, color=BLUE).move_to([0, 2.05, 0])
        frac_lab = text("ball matches its urn", size=26, color=GRAY).next_to(frac, DOWN, buff=0.25)
        with self.narrate("Urn A holds two red balls and one blue. Urn B holds two blue and one red. "
                          "Each person draws one ball in private, puts it back, and hears every "
                          "guess before theirs. So a single ball matches its urn two times in three.") as beat:
            beat.wait_until("two red", offset=-0.1)
            self.play(LaggedStart(*[b.animate.set_opacity(1) for b in uA.balls[:2]], lag_ratio=0.4),
                      run_time=0.8)
            beat.wait_until("one blue", offset=-0.1)
            self.play(uA.balls[2].animate.set_opacity(1), run_time=0.5)
            beat.wait_until("two blue", offset=-0.1)
            self.play(LaggedStart(*[b.animate.set_opacity(1) for b in uB.balls[:2]], lag_ratio=0.4),
                      run_time=0.8)
            beat.wait_until("one red", offset=-0.1)
            self.play(uB.balls[2].animate.set_opacity(1), run_time=0.5)
            beat.wait_until("draws", offset=-0.1)
            self.play(LaggedStart(*[FadeIn(b, shift=0.15 * DOWN) for b in balls], lag_ratio=0.02),
                      FadeIn(priv), run_time=beat.until("puts", offset=-0.1))
            beat.wait_until("hears", offset=-0.1)
            self.play(FadeIn(pub, shift=0.1 * UP), FadeOut(last_lab),
                      LaggedStart(*[Indicate(d, color=INK, scale_factor=1.6) for d in people[:-1]],
                                  lag_ratio=0.02), run_time=beat.until("So a", offset=-0.1))
            self.play(qmark.animate.scale(0.55).move_to([0, 3.15, 0]), run_time=0.6)
            beat.wait_until("two times", offset=-0.2)
            self.play(TransformFromCopy(uB.balls[:2], frac[0][0]), run_time=1.0)
            self.play(Create(frac[0][1]), TransformFromCopy(uB.balls, frac[0][2]), run_time=1.0)
            self.play(FadeIn(frac_lab, shift=0.1 * UP), run_time=0.5)

        # ------------------------------------------------------------ 2. what pooling would give
        sim_tag = text("simulated", size=22, color=GRAY)
        sim_tag.move_to([SAFE_X - sim_tag.width / 2, CONTENT_BOTTOM + 0.1 + sim_tag.height / 2, 0])
        pooled = formula(r"\text{majority of all 100 balls: wrong }", r"0.03\%", size=36)
        pooled[1].set_color(RED)
        pooled.move_to([0, -2.4, 0])
        with self.narrate("With all hundred balls in view, a simple majority would be wrong three "
                          "times in ten thousand. The last person can't see the balls, only the "
                          "ninety-nine guesses. Restaurants and bestseller lists work this way: "
                          "you see the choice, not the reason.") as beat:
            self.play(LaggedStart(*[b.animate.set_fill(BLUE if LINE[i] else RED).set_stroke(BLUE if LINE[i] else RED)
                                    for i, b in enumerate(balls)], lag_ratio=0.02),
                      FadeIn(sim_tag), run_time=beat.until("majority", offset=-0.1))
            self.play(Write(pooled[0]), run_time=1.0)
            self.play(TransformFromCopy(balls, pooled[1]), run_time=beat.until("three", offset=0.1, min_time=0.8))
            beat.wait_until("can't", offset=-0.1)
            self.play(*[b.animate.set_fill(DIM).set_stroke(GRAY) for b in balls], FadeOut(sim_tag),
                      run_time=1.0)
            beat.wait_until("ninety", offset=-0.1)
            self.play(LaggedStart(*[Indicate(d, color=YELLOW, scale_factor=1.6) for d in people[:-1]],
                                  lag_ratio=0.02), run_time=1.6)
            beat.wait_until("choice", offset=-0.15)
            self.play(flag(pub), run_time=0.8)
            beat.wait_until("reason", offset=-0.15)
            self.play(flag(priv), run_time=0.8)

        # ------------------------------------------------------------ 3. run the line
        TOP_P, TOP_B = 2.85, 2.45
        true_tag = formula(r"\text{true urn: }", "B", size=36)
        true_tag[1].set_color(BLUE)
        true_tag.move_to([-SAFE_X + true_tag.width / 2, -2.9, 0])
        XS = [-4.8, -1.6, 1.6, 4.8]
        heads = VGroup(*[Circle(radius=0.42, stroke_color=INK, stroke_width=3).move_to([x, 0.05, 0]) for x in XS])
        nums = VGroup(*[formula(str(i + 1), size=36).move_to(h) for i, h in enumerate(heads)])
        bubbles = VGroup(*[DashedVMobject(RoundedRectangle(width=0.85, height=0.85, corner_radius=0.15,
                                                           stroke_color=GRAY, stroke_width=2.5), num_dashes=24)
                           .move_to([x, 1.2, 0]) for x in XS])
        priv_balls = VGroup(*[ball(BLUE if LINE[i] else RED, r=0.24).move_to(bubbles[i]) for i in range(4)])
        gboxes = VGroup(*[VGroup(RoundedRectangle(width=0.8, height=0.72, corner_radius=0.12, stroke_color=RED,
                                                  stroke_width=3),
                                 formula("A", size=40, color=RED)).move_to([x, -1.05, 0]) for x in XS])
        for g in gboxes:
            g[1].move_to(g[0])

        def to_tape(i):
            tgt = Dot(people[i].get_center(), radius=0.05, color=RED)
            return TransformFromCopy(gboxes[i], tgt), tgt

        with self.narrate("Let's run it. Secretly, the urn is B. Person one draws red and says A. "
                          "Person two draws red too, and says A.") as beat:
            self.play(FadeOut(pooled), FadeOut(frac), FadeOut(frac_lab),
                      people.animate.set_y(TOP_P), balls.animate.set_y(TOP_B),
                      pub.animate.next_to(people.copy().set_y(TOP_P), UP, buff=0.22).align_to(people, LEFT),
                      priv.animate.next_to(balls.copy().set_y(TOP_B), DOWN, buff=0.22).align_to(balls, LEFT),
                      FadeOut(qmark), run_time=1.0)
            people[-1].set_color(INK)
            beat.wait_until("B", offset=-0.1)
            self.play(Create(box(uB)), run_time=0.5)
            bx = self.mobjects[-1]
            self.play(FadeOut(uA), FadeOut(bx), ReplacementTransform(uB, true_tag), run_time=1.0)
            self.play(Create(heads[0]), Write(nums[0]), Create(bubbles[0]), run_time=beat.until("draws", offset=-0.1))
            self.play(GrowFromCenter(priv_balls[0]), run_time=0.5)
            beat.wait_until("says", offset=-0.1)
            self.play(TransformFromCopy(priv_balls[0], gboxes[0]), run_time=0.6)
            a, t0 = to_tape(0)
            self.play(a, run_time=0.6)
            self.remove(t0)
            people[0].set_color(RED)
            self.play(Create(heads[1]), Write(nums[1]), Create(bubbles[1]), run_time=0.7)
            beat.wait_until("draws", occurrence=2, offset=-0.1)
            self.play(GrowFromCenter(priv_balls[1]), run_time=0.5)
            beat.wait_until("says", occurrence=2, offset=-0.1)
            self.play(TransformFromCopy(priv_balls[1], gboxes[1]), run_time=0.6)
            a, t1 = to_tape(1)
            self.play(a, run_time=0.6)
            self.remove(t1)
            people[1].set_color(RED)

        # ------------------------------------------------------------ 4. person three flips
        rb1, rb2 = ball(RED, 0.2), ball(RED, 0.2)
        gt = formula(">", size=40)
        bb = ball(BLUE, 0.2)
        imp = formula(r"\Rightarrow", size=40)
        resA = formula("A", size=40, color=RED)
        reason = VGroup(rb1, rb2, gt, bb, imp, resA).arrange(RIGHT, buff=0.22).move_to([XS[2], -2.3, 0])
        with self.narrate("Person three draws blue. But those two A's each stand for a red ball, and "
                          "two reds against one blue favour urn A. So she says A, and her blue ball "
                          "never reaches the record.") as beat:
            self.play(Create(heads[2]), Write(nums[2]), Create(bubbles[2]), heads[2].animate.set_stroke(YELLOW),
                      run_time=beat.until("blue", offset=-0.1))
            self.play(GrowFromCenter(priv_balls[2]), run_time=0.5)
            beat.wait_until("two A", offset=-0.1)
            self.play(Indicate(gboxes[0]), Indicate(gboxes[1]), run_time=0.8)
            beat.wait_until("red ball", offset=-0.1)
            self.play(TransformFromCopy(gboxes[0], rb1), TransformFromCopy(gboxes[1], rb2), run_time=1.0)
            beat.wait_until("against", offset=-0.1)
            self.play(FadeIn(gt), TransformFromCopy(priv_balls[2], bb), run_time=0.9)
            beat.wait_until("favour", offset=-0.1)
            self.play(Write(imp), FadeIn(resA, shift=0.1 * RIGHT), run_time=0.8)
            beat.wait_until("says", offset=-0.1)
            self.play(TransformFromCopy(resA, gboxes[2]), run_time=0.7)
            a, t2 = to_tape(2)
            self.play(a, run_time=0.6)
            self.remove(t2)
            people[2].set_color(RED)
            beat.wait_until("never", offset=-0.1)
            self.play(priv_balls[2].animate.set_fill(GRAY, opacity=0.35), bubbles[2].animate.set_opacity(0.35),
                      run_time=1.0)

        # ------------------------------------------------------------ 5. everyone copies
        with self.narrate("Person four sees the same two A's and does the same arithmetic. "
                          "So does everyone after her.") as beat:
            self.play(heads[2].animate.set_stroke(INK), Create(heads[3]), Write(nums[3]), Create(bubbles[3]),
                      heads[3].animate.set_stroke(YELLOW), GrowFromCenter(priv_balls[3]),
                      run_time=beat.until("same two", offset=-0.1))
            self.play(Indicate(gboxes[0]), Indicate(gboxes[1]), run_time=0.7)
            self.play(reason.animate.move_to([XS[3] - 0.6, -2.3, 0]), run_time=beat.until("arithmetic", end=True))
            self.play(TransformFromCopy(reason[-1], gboxes[3]),
                      priv_balls[3].animate.set_fill(GRAY, opacity=0.35), bubbles[3].animate.set_opacity(0.35),
                      run_time=0.7)
            a, t3 = to_tape(3)
            self.play(a, run_time=0.5)
            self.remove(t3)
            people[3].set_color(RED)
            beat.wait_until("everyone", offset=-0.2)
            self.play(LaggedStart(*[d.animate.set_color(RED) for d in people[4:]], lag_ratio=0.04,
                                  rate_func=LINEAR), run_time=max(2.5, beat.remaining() - 0.1))

        # ------------------------------------------------------------ 6. the line
        big = VGroup(heads, nums, bubbles, priv_balls, gboxes, reason)
        count = formula("67", r"\text{ blue,\ }", "33", r"\text{ red}", size=36)
        count[0].set_color(BLUE)
        count[2].set_color(RED)
        count.next_to(balls, DOWN, buff=0.22).align_to(balls, RIGHT)
        sim_tag2 = sim_tag.copy()
        with self.narrate("A hundred guesses of A, sitting on sixty-seven blue balls.") as beat:
            self.play(FadeOut(big), LaggedStart(*[Indicate(d, color=RED, scale_factor=1.6) for d in people],
                                                lag_ratio=0.015), run_time=beat.until("sitting", offset=-0.1))
            self.play(LaggedStart(*[b.animate.set_fill(BLUE if LINE[i] else RED).set_stroke(BLUE if LINE[i] else RED)
                                    for i, b in enumerate(balls)], lag_ratio=0.015),
                      FadeIn(count), FadeIn(sim_tag2), run_time=max(1.2, beat.remaining()))

        # ------------------------------------------------------------ 7. the measured failure
        L0, LEN = -2.6, 8.4                     # bar origin x, length for 25 %
        def px(v):
            return L0 + LEN * v / 25
        nl = NumberLine(x_range=[0, 25, 5], length=LEN, color=GRAY, stroke_width=2.5, include_numbers=True,
                        font_size=MATH_SMALL, numbers_to_include=[0, 5, 10, 15, 20, 25],
                        decimal_number_config={"num_decimal_places": 0, "color": GRAY})
        nl.move_to([L0 + LEN / 2, -1.15, 0])
        nl_title = text("hundredth person wrong (%)", size=26, color=GRAY).next_to(nl, DOWN, buff=0.15)
        nl_title.align_to(nl, RIGHT).shift(DOWN * 0.38)
        lab1 = text("guesses only", size=LABEL).move_to([0, 0.75, 0]).align_to([-6.2, 0, 0], LEFT)
        lab2 = text("balls pooled", size=LABEL).move_to([0, -0.35, 0]).align_to([-6.2, 0, 0], LEFT)
        rate = ValueTracker(0.0)
        bar1 = Rectangle(width=0.01, height=0.6, stroke_width=0, fill_color=RED, fill_opacity=0.9)
        bar1.move_to([L0, 0.75, 0], aligned_edge=LEFT)

        def upd_bar(m):
            w = max(0.01, LEN * rate.get_value() / 25)
            m.stretch_to_fit_width(w).move_to([L0, 0.75, 0], aligned_edge=LEFT)
        bar1.add_updater(upd_bar)
        pct1 = live_number(rate, 1, size=36, color=RED, suffix=r"\%")
        pct1.add_updater(lambda m: m.next_to(bar1, RIGHT, buff=0.2))
        bar2 = Rectangle(width=max(0.02, LEN * 0.0309 / 25), height=0.6, stroke_width=0, fill_color=RED,
                         fill_opacity=0.9).move_to([L0, -0.35, 0], aligned_edge=LEFT)
        pct2 = formula(r"0.03\%", size=36, color=RED).next_to(bar2, RIGHT, buff=0.2)
        nlines = ValueTracker(2.0)
        cm = np.cumsum(wrong) / np.arange(1, len(wrong) + 1)

        def lines_now():
            return int(round(10 ** nlines.get_value()))
        counter_t = ValueTracker(100)
        counter = live_number(counter_t, 0, size=36, color=INK, prefix=r"\text{lines simulated:}")
        counter.move_to([0, 0, 0]).align_to([-6.2, 0, 0], LEFT).set_y(-2.65)

        def drive(m):
            n = lines_now()
            counter_t.set_value(n)
            rate.set_value(100 * cm[n - 1])
        driver = Mobject()
        driver.add_updater(drive)
        with self.narrate("Simulate a hundred thousand lines, and the hundredth person is wrong twenty "
                          "percent of the time, more than six hundred times worse than the pooled balls. "
                          "The cause is everyone after person two: each guess just repeats the record.") as beat:
            self.play(FadeOut(true_tag), Create(nl), FadeIn(nl_title), FadeIn(lab1), FadeIn(lab2),
                      FadeIn(bar1), run_time=0.9)
            self.add(driver, counter, pct1)
            self.play(nlines.animate.set_value(5.0), rate_func=LINEAR,
                      run_time=beat.until("twenty", offset=0.2, min_time=2.0))
            driver.clear_updaters()
            self.remove(driver)
            rate.set_value(100 * cm[-1])
            counter_t.set_value(100_000)
            self.play(flag(pct1), run_time=0.8)
            beat.wait_until("six hundred", offset=-0.1)
            self.play(GrowFromEdge(bar2, LEFT), FadeIn(pct2, shift=0.1 * RIGHT), run_time=0.8)
            self.play(flag(pct2), run_time=0.8)
            beat.wait_until("everyone after", offset=-0.15)
            first2 = box(VGroup(people[:2], balls[:2]), buff=0.1)
            self.play(*[d.animate.set_opacity(DIM_OPACITY) for d in people[2:]], run_time=1.0)
            self.play(Create(first2), run_time=0.6)
            beat.wait_until("repeats", offset=-0.1)
            self.play(LaggedStart(*[Indicate(d, color=RED, scale_factor=1.5) for d in people[2:30]],
                                  lag_ratio=0.05), run_time=max(1.0, beat.remaining() - 0.1))
        bar1.clear_updaters()
        pct1.clear_updaters()
        pct1.number.clear_updaters()

        # ------------------------------------------------------------ 8. the token
        Y0 = -0.25
        NX = [-3.2, -1.6, 0.0, 1.6, 3.2]
        track = Line([NX[0], Y0, 0], [NX[-1], Y0, 0], color=GRAY, stroke_width=3)
        nodes = VGroup(*[Dot([x, Y0, 0], radius=0.07, color=GRAY) for x in NX])
        wallA = Rectangle(width=0.14, height=1.3, stroke_width=0, fill_color=RED, fill_opacity=1).move_to([-3.55, Y0, 0])
        wallB = Rectangle(width=0.14, height=1.3, stroke_width=0, fill_color=BLUE, fill_opacity=1).move_to([3.55, Y0, 0])
        wlabA = text("locked on A", size=LABEL, color=RED).next_to(wallA, DOWN, buff=0.25)
        wlabB = text("locked on B", size=LABEL, color=BLUE).next_to(wallB, DOWN, buff=0.25)
        wlabA.align_to(wallA, LEFT).shift(LEFT * 0.4)
        wlabB.align_to(wallB, RIGHT).shift(RIGHT * 0.4)
        token = Dot([0, Y0, 0], radius=0.17, color=YELLOW).set_z_index(3)
        sl_ball = ball(RED, 0.13).move_to([-0.45, Y0 + 0.55, 0])
        sl_arr = Arrow([-0.7, Y0 + 0.55, 0], [-1.55, Y0 + 0.55, 0], buff=0, color=RED, stroke_width=4,
                       max_tip_length_to_length_ratio=0.3)
        sr_ball = ball(BLUE, 0.13).move_to([0.45, Y0 + 0.55, 0])
        sr_arr = Arrow([0.7, Y0 + 0.55, 0], [1.55, Y0 + 0.55, 0], buff=0, color=BLUE, stroke_width=4,
                       max_tip_length_to_length_ratio=0.3)
        steps = VGroup(sl_ball, sl_arr, sr_ball, sr_arr)
        chart = VGroup(nl, nl_title, lab1, lab2, bar1, bar2, pct1, pct2, counter)

        def step(k, rt=0.55):
            return token.animate(rate_func=SMOOTH).shift(RIGHT * 1.6 * k)

        with self.narrate("So track the record as one token. Each guess that still reveals a ball moves "
                          "it a step: left for red, right for blue, and a tie goes to your own ball. Two "
                          "steps out, no single ball can outweigh it, and the token locks.") as beat:
            self.play(FadeOut(chart), FadeOut(first2), Create(track), FadeIn(nodes), run_time=1.0)
            self.play(GrowFromCenter(token), run_time=beat.until("moves", offset=-0.1))
            self.play(step(1), run_time=0.6)
            self.play(step(-1), run_time=0.6)
            beat.wait_until("left", offset=-0.1)
            self.play(FadeIn(sl_ball, scale=0.5), GrowArrow(sl_arr), step(-1), run_time=0.8)
            beat.wait_until("right", offset=-0.1)
            self.play(FadeIn(sr_ball, scale=0.5), GrowArrow(sr_arr), step(1), run_time=0.8)
            beat.wait_until("tie", offset=-0.1)
            self.play(step(1), run_time=0.6)
            self.play(Indicate(token, color=YELLOW, scale_factor=1.4), step(-1), run_time=0.8)
            beat.wait_until("Two steps", offset=-0.1)
            self.play(FadeIn(wallA), FadeIn(wallB), FadeIn(wlabA), FadeIn(wlabB), run_time=0.8)
            self.play(step(1), run_time=0.55)
            self.play(step(1), run_time=0.55)
            beat.wait_until("locks", offset=-0.15)
            self.play(flag(wallB), token.animate.set_color(BLUE).set_color(YELLOW), run_time=0.8)
            probe = ball(RED, 0.13).move_to([1.6, Y0 + 0.55, 0])
            self.play(FadeIn(probe, shift=0.4 * RIGHT), run_time=0.5)
            self.play(probe.animate.move_to(token.get_center() + 0.55 * UP), run_time=0.5)
            self.play(FadeOut(probe, scale=0.4), run_time=0.5)

        # ------------------------------------------------------------ 9. replay + 2/3 per step
        pA = formula(r"\tfrac{1}{3}", size=36, color=RED).next_to(sl_arr, UP, buff=0.15)
        pB = formula(r"\tfrac{2}{3}", size=36, color=BLUE).next_to(sr_arr, UP, buff=0.15)
        with self.narrate("Here, two reds locked it on A. Start over from the middle. Each step goes "
                          "right two times in three. Take two steps.") as beat:
            self.play(token.animate.move_to([0, Y0, 0]), *[d.animate.set_opacity(1) for d in people[:2]],
                      run_time=beat.until("two reds", offset=-0.1))
            self.play(Indicate(people[0], color=YELLOW, scale_factor=2.5), step(-1), run_time=0.7)
            self.play(Indicate(people[1], color=YELLOW, scale_factor=2.5), step(-1), run_time=0.7)
            self.play(flag(wallA), run_time=0.8)
            beat.wait_until("Start", offset=-0.1)
            self.play(token.animate.move_to([0, Y0, 0]), run_time=0.9)
            beat.wait_until("two times", offset=-0.1)
            self.play(FadeIn(pB, shift=0.1 * UP), FadeIn(pA, shift=0.1 * UP), run_time=0.8)
            beat.wait_until("Take", offset=-0.1)
            self.play(Indicate(token, color=YELLOW, scale_factor=1.4), run_time=0.8)

        # ------------------------------------------------------------ 10. three two-step paths
        def curved(a, b, ang, color):
            return CurvedArrow(np.array(a), np.array(b), angle=ang, color=color, stroke_width=4,
                               tip_length=0.2)
        arcB = curved([0.15, Y0 + 0.2, 0], [3.05, Y0 + 0.2, 0], -PI / 2, BLUE)
        arcA = curved([-0.15, Y0 + 0.2, 0], [-3.05, Y0 + 0.2, 0], PI / 2, RED)
        loop = Arc(radius=0.36, start_angle=PI / 2 + 0.55, angle=-(2 * PI - 1.1), arc_center=[0, Y0 - 0.5, 0],
                   color=INK, stroke_width=4)
        loop.add_tip(tip_length=0.18)

        def pair_label(c1, c2, tex, color):
            g = VGroup(ball(c1, 0.11), ball(c2, 0.11), formula(tex, size=40, color=color))
            g.arrange(RIGHT, buff=0.12)
            return g
        labB = pair_label(BLUE, BLUE, r"\tfrac{4}{9}", BLUE).next_to(arcB, UP, buff=0.12)
        labA = pair_label(RED, RED, r"\tfrac{1}{9}", RED).next_to(arcA, UP, buff=0.12)
        labM = pair_label(RED, BLUE, r"\tfrac{4}{9}", INK).next_to(loop, DOWN, buff=0.15)
        with self.narrate("Blue, blue, four ninths: locked on B. Red, red, one ninth: locked on A. One of "
                          "each, four ninths: back to the middle, and the race restarts. Does a longer "
                          "line rescue her? [pause 1.2]") as beat:
            self.play(FadeOut(steps), run_time=0.4)
            self.play(Create(arcB), MoveAlongPath(token.copy(), arcB.copy()), run_time=0.9)
            self.remove(*[m for m in self.mobjects if isinstance(m, Dot) and m is not token and m.color == token.color
                          and m not in people])
            self.play(TransformFromCopy(VGroup(pB, pB.copy()), labB), run_time=beat.until("locked on B", offset=-0.1))
            self.play(flag(wallB), run_time=0.6)
            beat.wait_until("Red, red", offset=-0.1)
            self.play(Create(arcA), run_time=0.8)
            self.play(TransformFromCopy(VGroup(pA, pA.copy()), labA), run_time=beat.until("locked on A", offset=-0.1))
            self.play(flag(wallA), run_time=0.6)
            beat.wait_until("One of", offset=-0.1)
            self.play(Create(loop), run_time=0.8)
            self.play(TransformFromCopy(VGroup(pA, pB), labM), run_time=beat.until("back", offset=-0.1))
            self.play(FadeOut(pA), FadeOut(pB), Rotate(loop, angle=-TAU, about_point=[0, Y0 - 0.5, 0]),
                      run_time=1.2)
            beat.wait_until("Does", offset=-0.1)
            self.play(token.animate.scale(1.3), run_time=0.6)
            self.play(token.animate.scale(1 / 1.3), run_time=0.6)

        # ------------------------------------------------------------ 11. the formula from the paths
        F = formula(r"P(\text{wrong})", "=", r"\tfrac{1}{9}", r"\div", r"\Big(", r"\tfrac{1}{9}", "+",
                    r"\tfrac{4}{9}", r"\Big)", "=", r"\tfrac{1}{5}", size=EQ)
        F.move_to([0, -2.45, 0])
        for k in (2, 5, 10):
            F[k].set_color(RED)
        F[7].set_color(BLUE)
        with self.narrate("No. Only the first two paths ever end the race, so the wrong lock wins one "
                          "ninth out of five ninths: one in five. For a line of ten people or ten "
                          "million.") as beat:
            beat.wait_until("Only", offset=-0.1)
            self.play(dim(loop, labM), run_time=0.8)
            beat.wait_until("wrong lock", offset=-0.1)
            self.play(Write(F[0:2]), run_time=0.7)
            self.play(TransformFromCopy(labA[2], F[2]), run_time=beat.until("out of", offset=-0.1))
            self.play(Write(F[3]), Write(F[4]), TransformFromCopy(labA[2], F[5]), Write(F[6]),
                      TransformFromCopy(labB[2], F[7]), Write(F[8]), run_time=beat.until("one in five", offset=-0.1))
            self.play(Write(F[9]), FadeIn(F[10], shift=0.1 * RIGHT), run_time=0.8)
            self.play(flag(F[10]), run_time=0.8)
            beat.wait_until("ten people", offset=-0.1)
            self.play(Indicate(wallA, color=YELLOW), Indicate(wallB, color=YELLOW), run_time=1.0)

        # ------------------------------------------------------------ 12. general p
        G = formula(r"P(\text{wrong})", "=", r"q^2", r"\div", r"\Big(", r"q^2", "+", r"p^2", r"\Big)", size=EQ)
        G[2].set_color(RED)
        G[5].set_color(RED)
        G[7].set_color(BLUE)
        qn = formula(r"q = 1 - p", size=40, color=GRAY)
        VGroup(G, qn).arrange(RIGHT, buff=0.9).move_to([0, -2.45, 0])
        with self.narrate("For any ball accuracy p, the wrong share is q squared over q squared plus p "
                          "squared, with q equal to one minus p.") as beat:
            beat.wait_until("q squared", offset=-0.15)
            self.play(FadeOut(F[9:]), *[ReplacementTransform(F[k], G[k]) for k in range(9)],
                      run_time=beat.until("with", offset=-0.1, min_time=1.5))
            self.play(Write(qn), run_time=0.8)
            self.play(flag(G[7]), run_time=0.8)

        # ------------------------------------------------------------ 13. the fix
        err = ValueTracker(np.log10(20.0))
        fixnum = live_number(err, 2, size=EQ, color=RED, prefix=r"\text{hundredth person wrong:}", suffix=r"\%")
        fixnum.number.clear_updaters()
        fixnum.number.set_value(20.0)
        pre, post = fixnum[0], fixnum[2]

        def upd_fix(m):
            m.set_value(10 ** err.get_value())
            m.next_to(pre, RIGHT, buff=0.15)
            post.next_to(m, RIGHT, buff=0.15)
        fixnum.number.add_updater(upd_fix)
        fixnum.move_to([0, -2.45, 0])
        with self.narrate("The fix is one rule: announce your ball, not your guess. Every step counts again, "
                          "the token never locks, and the hundredth person is back to three mistakes in ten "
                          "thousand.") as beat:
            self.play(FadeOut(G), FadeOut(qn), FadeOut(VGroup(arcA, arcB, loop, labA, labB, labM)),
                      run_time=beat.until("announce", offset=-0.1))
            self.play(*[b.animate.set_opacity(1) for b in balls], *[d.animate.set_opacity(1) for d in people],
                      run_time=1.0)
            self.play(LaggedStart(*[d.animate.set_color(BLUE if LINE[i] else RED) for i, d in enumerate(people)],
                                  lag_ratio=0.02), run_time=beat.until("never", offset=-0.1))
            self.play(FadeOut(wallA), FadeOut(wallB), FadeOut(wlabA), FadeOut(wlabB), step(1), run_time=0.8)
            self.play(step(1), run_time=0.5)
            self.play(step(-1), run_time=0.5)
            self.add(fixnum)
            self.play(FadeIn(fixnum), step(1), run_time=beat.until("back", offset=-0.1, min_time=0.6))
            self.play(err.animate.set_value(np.log10(0.0309)), step(-1), run_time=1.6)
            self.play(flag(fixnum.number), run_time=0.8)

        # ------------------------------------------------------------ 14. Anderson & Holt
        self.play(FadeOut(VGroup(track, nodes, token, fixnum, count, sim_tag2, pub, priv)),
                  *[d.animate.set_color(RED).set_opacity(DIM_OPACITY) for d in people],
                  *[b.animate.set_opacity(DIM_OPACITY) for b in balls], run_time=0.8)
        cells = VGroup(*[Square(0.42, stroke_color=GRAY, stroke_width=2, fill_opacity=0) for _ in range(56)])
        cells.arrange_in_grid(rows=7, cols=8, buff=0.1).move_to([-2.7, -0.45, 0])
        head = text("rounds where a cascade could form", size=LABEL).next_to(cells, UP, buff=0.3)
        cite = citation("Anderson & Holt, 1997 · American Economic Review")

        def leg(color, n, words, filled=True):
            sw = Square(0.42, stroke_color=GRAY if not filled else color, stroke_width=2,
                        fill_color=color, fill_opacity=1 if filled else 0)
            return VGroup(sw, formula(str(n), size=40, color=color if filled else INK),
                          text(words, size=LABEL, color=color if filled else INK)).arrange(RIGHT, buff=0.3)
        lg1 = leg(BLUE, 28, "right urn")
        lg2 = leg(RED, 13, "wrong urn")
        lg3 = leg(GRAY, 15, "no cascade", filled=False)
        legend = VGroup(lg1, lg2, lg3).arrange(DOWN, buff=0.45, aligned_edge=LEFT).move_to([3.4, 0.35, 0])
        with self.narrate("Anderson and Holt ran this game with real urns and cash prizes, six people a "
                          "round. Where a cascade could form, one did in forty-one of fifty-six rounds, and "
                          "thirteen of those locked onto the wrong urn.") as beat:
            self.play(FadeIn(cite, shift=0.1 * UP), run_time=0.8)
            beat.wait_until("Where", offset=-0.1)
            self.play(FadeIn(head), LaggedStart(*[Create(c) for c in cells], lag_ratio=0.03),
                      run_time=beat.until("forty", offset=-0.1))
            self.play(LaggedStart(*[c.animate.set_fill(BLUE if i < 28 else RED, 1).set_stroke(BLUE if i < 28 else RED)
                                    for i, c in enumerate(cells[:41])], lag_ratio=0.03),
                      FadeIn(lg1), FadeIn(lg2), FadeIn(lg3), run_time=beat.until("thirteen", offset=-0.1, min_time=1.2))
            self.play(LaggedStart(*[Indicate(c, color=RED, scale_factor=1.25) for c in cells[28:41]], lag_ratio=0.08),
                      flag(lg2), run_time=max(1.2, beat.remaining()))

        # ------------------------------------------------------------ 15. honest limit
        dev = VGroup(formula(r"26\%", size=EQ, color=YELLOW),
                     text("followed own ball", size=LABEL)).arrange(RIGHT, buff=0.3)
        dev.next_to(legend, DOWN, buff=0.6).align_to(legend, LEFT)
        with self.narrate("Their subjects weren't perfect copiers: in about a quarter of the cases where "
                          "copying paid, they followed their own ball, and each deviation put a real ball "
                          "back into the record.") as beat:
            beat.wait_until("quarter", offset=-0.1)
            self.play(FadeIn(dev, shift=0.1 * UP), run_time=0.8)
            beat.wait_until("deviation", offset=-0.1)
            self.play(LaggedStart(*[c.animate.set_stroke(YELLOW, width=4) for c in cells[41:]], lag_ratio=0.06),
                      flag(lg3), run_time=1.4)
            self.play(LaggedStart(*[c.animate.set_stroke(GRAY, width=2) for c in cells[41:]], lag_ratio=0.06),
                      run_time=max(0.8, beat.remaining()))

        # ------------------------------------------------------------ 16. landing
        pub2 = text("guesses", size=26, color=GRAY)
        priv2 = text("balls", size=26, color=GRAY)
        with self.narrate("So look again at this row of a hundred A's. It sounds like a hundred votes. "
                          "It holds two balls of evidence.") as beat:
            self.play(FadeOut(VGroup(cells, head, legend, dev, cite)), run_time=0.7)
            self.play(people.animate.set_y(0.45).set_opacity(1), balls.animate.set_y(-0.35).set_opacity(1),
                      run_time=beat.until("sounds", offset=-0.2, min_time=1.0))
            pub2.next_to(people, UP, buff=0.25).align_to(people, LEFT)
            priv2.next_to(balls, DOWN, buff=0.25).align_to(balls, LEFT)
            self.play(FadeIn(pub2), FadeIn(priv2),
                      LaggedStart(*[Indicate(d, color=RED, scale_factor=1.8) for d in people], lag_ratio=0.02),
                      run_time=beat.until("holds", offset=-0.1, min_time=1.2))
            frame2 = box(VGroup(people[:2], balls[:2]), buff=0.12)
            self.play(*[m.animate.set_opacity(DIM_OPACITY) for m in list(people[2:]) + list(balls[2:])],
                      Create(frame2), run_time=beat.until("evidence", end=True, min_time=0.8))
            self.hold(1.0)
        self.end_card()
