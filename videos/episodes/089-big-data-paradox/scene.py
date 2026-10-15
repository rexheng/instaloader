"""Episode 89 - Why 250,000 Survey Responses Were Worth Fewer Than 10.

    videos/toolkit/render.sh --preview videos/episodes/089-big-data-paradox/scene.py Episode /tmp/ep089.mp4
    videos/toolkit/render.sh videos/episodes/089-big-data-paradox/scene.py Episode \
        videos/episodes/089-big-data-paradox/final.mp4
"""
from manim import *
from sample_space import *

# ----------------------------------------------------------------------------- data
# Real numbers (Bradley et al. 2021, Nature 600:695-700): overshoot of first-dose uptake vs
# the CDC benchmark in May 2021, in percentage points; responses per week (Pulse: per wave).
REAL = [("Delphi–Facebook", "250,000 a week", 250_000, 17.0),
        ("Census Household Pulse", "75,000 a wave", 75_000, 14.0),
        ("Axios–Ipsos", "1,000 a week", 1_000, 4.2)]

# Simulated country: 32 x 32 tiles, exactly half vaccinated (BLUE), half not (PURPLE).
SIDE = 32
RNG = np.random.default_rng(7)
VACC = np.zeros(SIDE * SIDE, dtype=bool)
VACC[RNG.permutation(SIDE * SIDE)[: SIDE * SIDE // 2]] = True
SURVEY_TILE = 32 * 4 + 27          # the one tile that stands for all 250,000 responses

# Sampling distributions (simulated): 20 repeated polls per design.
N_DRAWS = 20
EST_SRS_1K = RNG.binomial(1_000, 0.5, N_DRAWS) / 10            # % vaccinated
EST_SRS_250K = RNG.binomial(250_000, 0.5, N_DRAWS) / 2_500
P_TILT = 2 / 3     # vaccinated twice as likely to answer, half the country vaccinated
EST_TILT_250K = RNG.binomial(250_000, P_TILT, N_DRAWS) / 2_500
EST_TILT_1M = RNG.binomial(1_000_000, P_TILT, N_DRAWS) / 10_000

# Meng's identity, with the episode's numbers
N_POP, N_RESP = 255e6, 250e3
F = N_RESP / N_POP
R0, R1 = 2 * F / 3, 4 * F / 3                                  # response rates
RHO = np.sqrt(0.25 / (F * (1 - F))) * (R1 - R0)                # 0.01044
QUANT = np.sqrt((N_POP - N_RESP) / N_RESP)                     # 31.9
N_EFF = 1 / (RHO ** 2 * (N_POP - N_RESP) / N_RESP)             # 9.0
assert abs(RHO * QUANT * 0.5 - 1 / 6) < 1e-9 and round(N_EFF) == 9

# number line (simulation panel)
NL_X0, NL_LEN, NL_LO, NL_HI = -0.9, 7.0, 40.0, 75.0
NL_Y = -1.45
BIN = 0.5            # dot-plot bin width, percentage points
DOT_R = 0.05
STACK = 0.118


def nl_x(v):
    return NL_X0 + (v - NL_LO) / (NL_HI - NL_LO) * NL_LEN


def stack_positions(values):
    counts, out = {}, []
    for v in values:
        b = np.floor(v / BIN) * BIN + BIN / 2
        k = counts.get(b, 0)
        counts[b] = k + 1
        out.append(np.array([nl_x(b), NL_Y + DOT_R + 0.04 + k * STACK, 0]))
    return out


# chart (cold open / payoff)
ZERO_X = -0.55
PT = 0.27                          # units per percentage point
BLOCK_RIGHT = -1.0
BIG_SIDE = 2.0                     # area of each block is proportional to responses


def block_side(n):
    return BIG_SIDE * np.sqrt(n / 250_000)


class Episode(NarratedScene):
    EPISODE = 89
    TITLE = "Why 250,000 Survey Responses Were Worth Fewer Than 10"
    PRONUNCIATIONS = {"Xiao-Li": "shyow lee", "Meng": "mung", "Ipsos": "ip sohss",
                      "rho": "row"}

    # ------------------------------------------------------------------ builders
    def chart_row(self, name, sub, n, err, y):
        side = max(block_side(n), 0.12)
        blk = Square(side, stroke_width=0, fill_color=INK, fill_opacity=0.85)
        blk.move_to([BLOCK_RIGHT - side / 2, y, 0])
        nm = label(name, size=27, color=INK)
        sb = label(sub, size=26, color=GRAY)
        txt = VGroup(nm, sb).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        txt.move_to([-SAFE_X + txt.width / 2, y, 0])
        bar = Rectangle(width=err * PT, height=0.34, stroke_width=0, fill_color=RED,
                        fill_opacity=0.9)
        bar.move_to([ZERO_X + err * PT / 2, y, 0])
        val = MathTex(rf"+{err:g}", font_size=MATH, color=RED).next_to(bar, RIGHT, buff=0.18)
        return VGroup(blk, txt, bar, val)

    def chart_axis(self, top, bottom):
        line = Line([ZERO_X, bottom, 0], [ZERO_X + 20 * PT, bottom, 0], color=GRAY,
                    stroke_width=2.5)
        ticks = VGroup(*[Line([ZERO_X + v * PT, bottom, 0], [ZERO_X + v * PT, bottom - 0.08, 0],
                              color=GRAY, stroke_width=2.5) for v in (0, 5, 10, 15, 20)])
        nums = VGroup(*[MathTex(str(v), font_size=MATH_SMALL, color=GRAY)
                        .next_to(t, DOWN, buff=0.1) for v, t in zip((0, 5, 10, 15, 20), ticks)])
        ttl = label("overshoot (percentage points)", size=26, color=GRAY)
        ttl.next_to(nums, DOWN, buff=0.15).align_to(line, RIGHT)
        truth = Line([ZERO_X, bottom, 0], [ZERO_X, top, 0], color=GREEN, stroke_width=4)
        tlab = label("true rate (CDC)", size=26, color=GREEN).next_to(truth, UP, buff=0.12)
        tlab.shift(RIGHT * (tlab.width / 2 - 0.1))
        return VGroup(line, ticks, nums, ttl), VGroup(truth, tlab)

    def mosaic(self):
        s = 4.0 / SIDE
        tiles = VGroup(*[
            Square(s * 0.86, stroke_width=0, fill_opacity=0.9,
                   fill_color=BLUE if VACC[i] else PURPLE)
            .move_to([(i % SIDE - (SIDE - 1) / 2) * s, ((SIDE - 1) / 2 - i // SIDE) * s, 0])
            for i in range(SIDE * SIDE)])
        tiles.move_to([-4.1, 0.6, 0])
        return tiles

    # ------------------------------------------------------------------ scene
    def construct(self):
        # ================================================================ COLD OPEN
        big = self.chart_row(*REAL[0], y=1.55)
        small = self.chart_row(*REAL[2], y=-0.75)
        spring = label("spring 2021 · share of US adults with a Covid shot", size=26,
                       color=GRAY).move_to([0, 3.3, 0])
        axis, truth = self.chart_axis(top=2.75, bottom=-1.55)

        with self.narrate("Two surveys ask American adults if they've had a Covid shot. "
                          "This one hears from a quarter of a million people a week. "
                          "This one, about a thousand. Which is closer to the truth? "
                          "[pause 1.5]") as beat:
            self.play(FadeIn(spring, shift=0.1 * DOWN), run_time=beat.until("This one"))
            self.play(GrowFromCenter(big[0]), FadeIn(big[1], shift=0.1 * RIGHT),
                      run_time=beat.until("This one,", occurrence=2, offset=-0.1))
            self.play(GrowFromCenter(small[0]), FadeIn(small[1], shift=0.1 * RIGHT),
                      run_time=beat.until("Which", offset=-0.1))
            self.play(Create(truth[0]), FadeIn(truth[1]), Create(axis[0]), FadeIn(axis[1:]),
                      run_time=beat.until("truth", offset=0.4))
            # prediction pause: the two blocks pulse once each, nothing else moves
            self.play(Indicate(big[0], color=INK, scale_factor=1.04),
                      run_time=1.0)
            self.play(Indicate(small[0], color=INK, scale_factor=1.6), run_time=1.0)

        cite_b = citation("Bradley et al., 2021 · Nature")
        with self.narrate("The big one overshot by seventeen percentage points. "
                          "The small one, by about four.") as beat:
            beat.wait_until("overshot", offset=-0.1)
            self.play(GrowFromEdge(big[2], LEFT), FadeIn(cite_b),
                      run_time=beat.until("seventeen", offset=-0.05))
            self.play(FadeIn(big[3], shift=0.1 * RIGHT), run_time=0.6)
            beat.wait_until("small", offset=-0.15)
            self.play(GrowFromEdge(small[2], LEFT), run_time=0.8)
            self.play(FadeIn(small[3], shift=0.1 * RIGHT), run_time=0.6)

        moe = MathTex(r"\text{its margin of error: } \pm 0.2", font_size=MATH, color=INK)
        moe.next_to(big[3], DOWN, buff=0.3).align_to(big[2], LEFT).shift(RIGHT * 0.1)
        with self.narrate("And the big survey came with a margin of error smaller than one "
                          "point. So how do a quarter of a million answers lose to a "
                          "thousand?") as beat:
            beat.wait_until("margin", offset=-0.2)
            self.play(Write(moe), run_time=1.2)
            beat.wait_until("quarter", offset=-0.1)
            self.play(Indicate(big[0], color=INK, scale_factor=1.04), run_time=0.9)
            beat.wait_until("thousand", offset=-0.1)
            self.play(Indicate(small[0], color=INK, scale_factor=1.6), run_time=0.9)

        chart = VGroup(big, small, axis, truth, spring, moe)
        self.play(FadeOut(chart), FadeOut(cite_b), run_time=0.6)

        # ================================================================ NAIVE BUILD
        tiles = self.mosaic()
        head = label("simulated country: half vaccinated", size=26, color=GRAY)
        head.next_to(tiles, UP, buff=0.22)
        sq_b = Square(0.22, stroke_width=0, fill_color=BLUE, fill_opacity=0.9)
        sq_p = Square(0.22, stroke_width=0, fill_color=PURPLE, fill_opacity=0.9)
        lg_b = label("vaccinated", size=26, color=BLUE)
        lg_p = label("not yet", size=26, color=PURPLE)
        leg1 = VGroup(sq_b, lg_b).arrange(RIGHT, buff=0.18)
        leg2 = VGroup(sq_p, lg_p).arrange(RIGHT, buff=0.18)
        legend = VGroup(leg1, leg2).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        legend.next_to(tiles, DOWN, buff=0.3).align_to(tiles, LEFT)

        nl = Line([nl_x(NL_LO), NL_Y, 0], [nl_x(NL_HI), NL_Y, 0], color=GRAY, stroke_width=2.5)
        nl_ticks = VGroup(*[Line([nl_x(v), NL_Y, 0], [nl_x(v), NL_Y - 0.08, 0], color=GRAY,
                                 stroke_width=2.5) for v in (40, 50, 60, 70)])
        nl_nums = VGroup(*[MathTex(rf"{v}\%", font_size=MATH_SMALL, color=GRAY)
                           .next_to(t, DOWN, buff=0.1) for v, t in zip((40, 50, 60, 70), nl_ticks)])
        nl_ttl = label("each dot: one poll's estimate", size=26, color=GRAY)
        nl_ttl.next_to(nl_nums, DOWN, buff=0.15).align_to(nl, RIGHT)
        numline = VGroup(nl, nl_ticks, nl_nums, nl_ttl)
        t_line = DashedLine([nl_x(50), NL_Y, 0], [nl_x(50), 2.35, 0], color=GREEN,
                            stroke_width=3, dash_length=0.08)
        t_lab = MathTex(r"\text{truth } 50\%", font_size=MATH, color=GREEN)
        t_lab.next_to(t_line, UP, buff=0.12)

        def readout(n_tex, m_tex):
            g = VGroup(MathTex(rf"n = {n_tex}", font_size=MATH, color=INK),
                       MathTex(rf"\text{{margin}} \pm {m_tex}", font_size=MATH, color=INK))
            g.arrange(RIGHT, buff=0.6).move_to([3.0, 3.25, 0])
            return g

        ro = readout(r"1{,}000", r"3.2")

        def specks(idx):
            return VGroup(*[Dot(tiles[i].get_center(), radius=0.04, color=INK)
                            for i in idx])

        rand_idx = RNG.choice(SIDE * SIDE, 40, replace=False)
        vacc_ids, novacc_ids = np.flatnonzero(VACC), np.flatnonzero(~VACC)
        tilt_idx = np.concatenate([RNG.choice(vacc_ids, 27, replace=False),
                                   RNG.choice(novacc_ids, 13, replace=False)])
        sp = specks(rand_idx)

        pos_1k = stack_positions(EST_SRS_1K)
        pos_250k = stack_positions(EST_SRS_250K)
        pos_tilt = stack_positions(EST_TILT_250K)
        pos_tilt1m = stack_positions(EST_TILT_1M)
        pts = VGroup(*[Dot(p, radius=DOT_R, color=INK) for p in pos_1k])

        with self.narrate("Here's the textbook picture, on a simulated country where exactly "
                          "half the adults are vaccinated. Poll a thousand people at random, "
                          "again and again, and the estimates scatter around fifty percent, "
                          "give or take about three points.") as beat:
            self.play(LaggedStart(*[FadeIn(t) for t in tiles], lag_ratio=0.002),
                      FadeIn(head), run_time=beat.until("half", offset=-0.1))
            self.play(FadeIn(legend), Create(numline), Create(t_line), FadeIn(t_lab),
                      run_time=beat.until("Poll", offset=-0.1))
            self.play(LaggedStart(*[GrowFromCenter(d) for d in sp], lag_ratio=0.05),
                      FadeIn(ro[0]), run_time=beat.until("again", offset=-0.1))
            self.play(LaggedStart(*[FadeIn(d, shift=0.6 * DOWN) for d in pts], lag_ratio=0.25),
                      Transform(sp, specks(RNG.choice(SIDE * SIDE, 40, replace=False))),
                      run_time=beat.until("give", offset=-0.1))
            self.play(FadeIn(ro[1], shift=0.1 * LEFT), run_time=0.8)

        with self.narrate("Poll a quarter of a million, and that spread collapses to a fifth "
                          "of a point. More answers, less error.") as beat:
            self.play(Transform(ro, readout(r"250{,}000", r"0.2")),
                      run_time=beat.until("spread", offset=-0.1))
            self.play(*[d.animate.move_to(p) for d, p in zip(pts, pos_250k)],
                      run_time=beat.until("More", offset=-0.1), rate_func=SMOOTH)
            self.play(Indicate(pts, color=INK, scale_factor=1.15), run_time=0.9)

        # ================================================================ FAIL
        rate_b = MathTex(r"\text{answer: } 13 \text{ in } 10{,}000", font_size=MATH, color=BLUE)
        rate_p = MathTex(r"\text{answer: } 6.5 \text{ in } 10{,}000", font_size=MATH,
                         color=PURPLE)
        rate_b.next_to(lg_b, RIGHT, buff=0.35)
        rate_p.next_to(lg_p, RIGHT, buff=0.35).align_to(rate_b, LEFT)
        with self.narrate("Now let people decide whether to answer. Say vaccinated adults "
                          "are twice as likely to respond: thirteen in every ten thousand, "
                          "against six and a half.") as beat:
            beat.wait_until("decide", offset=-0.1)
            self.play(Transform(sp, specks(tilt_idx)), run_time=beat.until("twice", offset=-0.1))
            beat.wait_until("thirteen", offset=-0.15)
            self.play(Write(rate_b), run_time=beat.until("against", offset=-0.1))
            self.play(Write(rate_p), run_time=beat.until("half", offset=0.2))

        miss_line = Line([nl_x(50), 1.55, 0], [nl_x(66.7), 1.55, 0], color=RED, stroke_width=5)
        miss_ends = VGroup(*[Line(miss_line.get_start() + 0.12 * d, miss_line.get_start() - 0.12 * d,
                                  color=RED, stroke_width=5).shift(s)
                             for d in (UP,) for s in (ORIGIN, miss_line.get_end() - miss_line.get_start())])
        miss_val = ValueTracker(16.7)
        miss_lab = live_number(miss_val, 1, size=MATH, color=RED, prefix=r"\text{miss} =",
                               suffix=r"\text{ points}")
        miss_lab.next_to(miss_line, UP, buff=0.15)
        with self.narrate("The estimates jump to sixty seven percent. A miss of almost "
                          "seventeen points, about the size of the real one.") as beat:
            self.play(*[d.animate.move_to(p) for d, p in zip(pts, pos_tilt)],
                      run_time=beat.until("sixty", offset=0.3), rate_func=SMOOTH)
            beat.wait_until("miss", offset=-0.1)
            self.play(Create(miss_line), Create(miss_ends), FadeIn(miss_lab, shift=0.1 * UP),
                      run_time=beat.until("about", offset=-0.1))

        with self.narrate("Quadruple the responses. The margin of error halves. The miss "
                          "doesn't move. More data only made the wrong answer more "
                          "confident.") as beat:
            new_sp = specks(np.concatenate([RNG.choice(vacc_ids, 27, replace=False),
                                            RNG.choice(novacc_ids, 13, replace=False)]))
            self.play(Transform(ro[0], readout(r"1{,}000{,}000", r"0.2")[0]), Transform(sp, new_sp),
                      run_time=beat.until("margin", offset=-0.1))
            self.play(Transform(ro[1], readout(r"1{,}000{,}000", r"0.1")[1]),
                      run_time=beat.until("miss", offset=-0.1))
            self.play(*[d.animate.move_to(p) for d, p in zip(pts, pos_tilt1m)],
                      flag(miss_lab, color=RED), run_time=beat.until("More", offset=-0.1))
            self.play(Indicate(pts, color=INK, scale_factor=1.15),
                      Indicate(ro[1], color=INK), run_time=beat.until("confident", offset=0.3))

        # ================================================================ INSIGHT
        # equation: miss = rho x sqrt((N-n)/n) x sigma, each term from its referent
        eq = MathTex(r"\text{miss}", "=", r"\rho", r"\times", r"\sqrt{\frac{N-n}{n}}",
                     r"\times", r"\sigma", font_size=EQ)
        eq.move_to([2.35, 2.1, 0])
        eq[0].set_color(RED)
        eq[2].set_color(YELLOW)
        vals = VGroup(MathTex(r"0.17", color=RED), MathTex("="), MathTex(r"0.0104", color=YELLOW),
                      MathTex(r"\times"), MathTex(r"32"), MathTex(r"\times"), MathTex(r"0.5"))
        for v, e in zip(vals, eq):
            v.set(font_size=EQ)
            v.move_to([e.get_center()[0], 0.55, 0])
        names = VGroup(label("quality", size=26, color=YELLOW),
                       label("quantity", size=26, color=GRAY),
                       label("difficulty", size=26, color=GRAY))
        for nm, idx in zip(names, (2, 4, 6)):
            nm.next_to(vals[idx], DOWN, buff=0.25)
        cite_m = citation("Meng, 2018 · Annals of Applied Statistics")
        cite_m.move_to([SAFE_X - cite_m.width / 2, cite_m.get_center()[1], 0])

        with self.narrate("The statistician Xiao-Li Meng showed that this miss is a product "
                          "of three numbers, all on screen.") as beat:
            self.play(FadeOut(pts), FadeOut(numline), FadeOut(t_line), FadeOut(t_lab),
                      FadeOut(ro), FadeOut(miss_line), FadeOut(miss_ends),
                      run_time=beat.until("Meng", offset=-0.2))
            miss_lab.clear_updaters()
            self.play(ReplacementTransform(miss_lab, eq[0]), FadeIn(cite_m),
                      run_time=beat.until("product", offset=-0.1))
            self.play(Write(eq[1]), run_time=0.6)
            beat.wait_until("three", offset=-0.1)
            self.play(Write(eq[2:]), run_time=beat.until("all", offset=-0.1))

        # sigma: from the two colours of the country
        half_b = VGroup(*[t for i, t in enumerate(tiles) if VACC[i]])
        with self.narrate("First, how varied the answers are. Half yes and half no gives a "
                          "standard deviation of one half.") as beat:
            self.play(FadeOut(sp), Indicate(eq[6], color=INK), run_time=beat.until("Half", offset=-0.1))
            self.play(half_b.animate.set_opacity(0.3), run_time=0.8)
            self.play(half_b.animate.set_opacity(0.9), run_time=beat.until("one half", offset=-0.2))
            self.play(TransformFromCopy(VGroup(sq_b, sq_p), vals[6]), FadeIn(names[2]),
                      run_time=1.0)

        # quantity: one tile = the whole survey; the side of the square
        stile = tiles[SURVEY_TILE]
        others = VGroup(*[t for i, t in enumerate(tiles) if i != SURVEY_TILE])
        brace = Brace(tiles, RIGHT, buff=0.12, color=GRAY)
        b_lab = MathTex("32", font_size=MATH, color=INK).next_to(brace, RIGHT, buff=0.12)
        with self.narrate("Second, how much of the country stayed silent. In this square, the "
                          "whole survey is one tile, out of a thousand and twenty four. The "
                          "factor is the square root of silent over heard: the side of the "
                          "square, about thirty two.") as beat:
            beat.wait_until("silent", offset=-0.1)
            self.play(Indicate(eq[4], color=INK), run_time=0.9)
            beat.wait_until("whole", offset=-0.1)
            self.play(stile.animate.set_fill(INK, 1).scale(1.6), others.animate.set_opacity(0.35),
                      run_time=beat.until("thousand", offset=-0.1))
            self.play(others.animate.set_opacity(0.9), run_time=beat.until("factor", offset=-0.1))
            beat.wait_until("side", offset=-0.1)
            self.play(GrowFromCenter(brace), FadeIn(b_lab), run_time=beat.until("thirty", offset=-0.2))
            self.play(TransformFromCopy(b_lab, vals[4]), FadeIn(names[1]), run_time=1.0)

        # rho: the response-rate tilt, measured over everyone
        with self.narrate("Third, data quality: across all two hundred and fifty five million "
                          "adults, the correlation between answering and being vaccinated. "
                          "Since almost nobody answers, twice as likely works out to a "
                          "correlation of just one hundredth.") as beat:
            beat.wait_until("quality", offset=-0.1)
            self.play(Indicate(eq[2], color=YELLOW), FadeIn(names[0]), run_time=0.9)
            beat.wait_until("Since", offset=-0.1)
            self.play(Indicate(VGroup(rate_b, rate_p), color=INK, scale_factor=1.05),
                      run_time=beat.until("twice", offset=-0.1))
            self.play(TransformFromCopy(VGroup(rate_b, rate_p), vals[2]),
                      run_time=beat.until("hundredth", offset=-0.2))

        with self.narrate("One hundredth, times thirty two, times one half: seventeen "
                          "points.") as beat:
            self.play(Write(vals[3]), Write(vals[5]), run_time=beat.until("times", occurrence=2))
            beat.wait_until("seventeen", offset=-0.3)
            self.play(Write(vals[1]), FadeIn(vals[0], shift=0.1 * RIGHT), run_time=0.7)
            self.play(flag(vals[0], color=RED), run_time=0.8)

        rnd_rho = MathTex(r"0.00006", font_size=EQ, color=YELLOW).move_to(vals[2])
        rnd_miss = MathTex(r"0.001", font_size=EQ, color=RED).move_to(vals[0])
        rnd_rho.align_to(vals[2], RIGHT)
        rnd_miss.align_to(vals[0], RIGHT)
        with self.narrate("A truly random sample keeps that correlation near zero, about one "
                          "in sixteen thousand. Then the same product is a tenth of a point, "
                          "the ordinary random error.") as beat:
            beat.wait_until("near", offset=-0.1)
            keep_rho, keep_miss = vals[2].copy(), vals[0].copy()
            self.play(Transform(vals[2], rnd_rho), run_time=beat.until("Then", offset=-0.1))
            beat.wait_until("tenth", offset=-0.3)
            self.play(Transform(vals[0], rnd_miss), run_time=0.8)
            beat.wait_until("ordinary", offset=0.2)
            self.play(Transform(vals[2], keep_rho), Transform(vals[0], keep_miss),
                      run_time=beat.remaining(min_time=0.8))

        dots9 = VGroup(*[Dot(radius=0.07, color=INK) for _ in range(9)]).arrange(RIGHT, buff=0.18)
        with self.narrate("So how many random people would be exactly as accurate as this "
                          "quarter of a million? [pause 1.5]") as beat:
            beat.wait_until("quarter", offset=-0.1)
            self.play(Indicate(stile, color=INK, scale_factor=2.0), run_time=1.0)
            self.play(Circumscribe(stile, color=INK, buff=0.08), run_time=beat.remaining(min_time=1.0))

        eq1 = MathTex(r"\frac{\sigma}{\sqrt{m}}", "=", r"\rho", r"\sqrt{\frac{N-n}{n}}",
                      r"\,\sigma", font_size=EQ).move_to([2.35, -1.25, 0])
        eq1[2].set_color(YELLOW)
        eq2 = MathTex("m", "=", r"\frac{1}{\rho^{2}}", r"\cdot", r"\frac{n}{N-n}", r"\approx",
                      "9", font_size=EQ).move_to([2.35, -1.25, 0])
        eq2[2].set_color(YELLOW)
        with self.narrate("Set a random sample's error equal to this miss, and solve. One over "
                          "rho squared, divided by a thousand and nineteen. About nine "
                          "people.") as beat:
            self.play(Write(eq1[0]), run_time=beat.until("equal", offset=-0.1))
            self.play(Write(eq1[1]), TransformFromCopy(eq[2:], eq1[2:]),
                      run_time=beat.until("solve", offset=0.2))
            beat.wait_until("One", offset=-0.1)
            self.play(ReplacementTransform(eq1[0], eq2[0]), ReplacementTransform(eq1[1], eq2[1]),
                      ReplacementTransform(eq1[2], eq2[2]), ReplacementTransform(eq1[3], eq2[4]),
                      FadeOut(eq1[4]), FadeIn(eq2[3]), run_time=beat.until("About", offset=-0.1))
            dots9.next_to(eq2, DOWN, buff=0.45)
            self.play(Write(eq2[5:]), TransformFromCopy(VGroup(stile), dots9),
                      run_time=beat.until("people", offset=0.3))

        # ================================================================ PAYOFF
        y_rows = (1.75, 0.05, -1.25)
        rows = [self.chart_row(*r, y=y) for r, y in zip(REAL, y_rows)]
        axis2, truth2 = self.chart_axis(top=2.85, bottom=-1.95)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.6)
        cite_b2 = citation("Bradley et al., 2021 · Nature")
        with self.narrate("Bradley and colleagues ran this audit on the real surveys, in "
                          "Nature. Delphi Facebook, a quarter million a week: seventeen points "
                          "high. The Census Household Pulse, seventy five thousand: fourteen. "
                          "Axios Ipsos, a thousand people recruited from random addresses: "
                          "about four.") as beat:
            self.play(FadeIn(cite_b2), Create(axis2[0]), FadeIn(axis2[1:]), Create(truth2[0]),
                      FadeIn(truth2[1]), run_time=beat.until("Delphi", offset=-0.1))
            for r, w, v in zip(rows, ("Delphi", "Census", "Axios"), ("seventeen", "fourteen", "four")):
                self.play(GrowFromCenter(r[0]), FadeIn(r[1], shift=0.1 * RIGHT),
                          run_time=beat.until(w, offset=0.5))
                self.play(GrowFromEdge(r[2], LEFT), run_time=beat.until(v, offset=-0.05))
                self.play(FadeIn(r[3], shift=0.1 * RIGHT), run_time=0.5)

        eff = MathTex(r"\text{worth} < 10 \text{ random people (April)}", font_size=MATH,
                      color=INK)
        eff.next_to(rows[0][2], DOWN, buff=0.22).align_to(rows[0][2], LEFT)
        with self.narrate("For April's estimate, the big survey was worth fewer than ten "
                          "random people.") as beat:
            self.play(Write(eff), run_time=beat.until("fewer", offset=0.3))
            self.play(Indicate(rows[0][0], color=INK, scale_factor=1.04),
                      run_time=beat.remaining(min_time=0.8))

        wtag = label("weighted for education and race", size=26, color=GRAY)
        wtag.next_to(rows[1][2], DOWN, buff=0.2).align_to(rows[1][2], LEFT)
        with self.narrate("Weighting didn't fix it: the Census survey adjusted for education "
                          "and race, and still overshot by more than ten points. And that "
                          "worth of ten belongs to this one question; another question has "
                          "its own correlation.") as beat:
            beat.wait_until("Census", offset=-0.1)
            self.play(FadeIn(wtag, shift=0.1 * UP), run_time=beat.until("still", offset=-0.1))
            self.play(flag(rows[1][2], color=RED), run_time=beat.until("And", offset=-0.1))
            beat.wait_until("this one", offset=-0.1)
            self.play(Circumscribe(eff, color=YELLOW, buff=0.1), run_time=beat.until("another", offset=-0.1))
            self.play(Indicate(eff, color=INK, scale_factor=1.03), run_time=1.0)

        # ================================================================ LANDING
        nine = VGroup(*[Dot(radius=0.035, color=INK) for _ in range(9)])
        nine.arrange_in_grid(3, 3, buff=0.04)
        nine.move_to([BLOCK_RIGHT - 0.1, y_rows[0], 0])
        with self.narrate("So here are the two surveys from the start, at their effective size. "
                          "A quarter of a million answers, and what they measured most "
                          "precisely was who chooses to answer.") as beat:
            self.play(FadeOut(rows[1]), FadeOut(wtag), run_time=beat.until("two", offset=-0.1))
            self.play(ReplacementTransform(rows[0][0], nine), run_time=beat.until("effective", offset=0.6))
            beat.wait_until("what", offset=-0.1)
            self.play(Indicate(rows[0][2], color=RED, scale_factor=1.04),
                      run_time=beat.until("who", offset=-0.1))
            self.play(Circumscribe(nine, color=INK, buff=0.1), run_time=beat.remaining(min_time=0.8))

        self.end_card()
