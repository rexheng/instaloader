"""Episode 48: Storks Deliver Babies (p = 0.008).

Real data: Matthews (2000), Teaching Statistics 22(2), Table 1 (17 European countries).
Numbers are recomputed in check_numbers.py.

    videos/toolkit/render.sh --preview videos/episodes/048-confounding-dags/scene.py Episode /tmp/ep48.mp4
"""
from manim import *
from sample_space import *

# ---------------------------------------------------------------- data (Matthews 2000, Table 1)
TABLE = [
    ("Albania", 28750, 100, 83), ("Austria", 83860, 300, 87), ("Belgium", 30520, 1, 118),
    ("Bulgaria", 111000, 5000, 117), ("Denmark", 43100, 9, 59), ("France", 544000, 140, 774),
    ("Germany", 357000, 3300, 901), ("Greece", 132000, 2500, 106), ("Holland", 41900, 4, 188),
    ("Hungary", 93000, 5000, 124), ("Italy", 301280, 5, 551), ("Poland", 312680, 30000, 610),
    ("Portugal", 92390, 1500, 120), ("Romania", 237500, 5000, 367), ("Spain", 504750, 8000, 439),
    ("Switzerland", 41290, 150, 82), ("Turkey", 779450, 25000, 1576),
]
NAMES = [r[0] for r in TABLE]
AREA = np.array([r[1] for r in TABLE], float)
STORK = np.array([r[2] for r in TABLE], float) / 1000.0      # thousands of pairs
BIRTH = np.array([r[3] for r in TABLE], float)               # thousands per year
T = NAMES.index("Turkey")
# what land area alone predicts (simple linear fits on area)
PRED_S = np.polyval(np.polyfit(AREA, STORK, 1), AREA)
PRED_B = np.polyval(np.polyfit(AREA, BIRTH, 1), AREA)
NAIVE = np.polyfit(STORK, BIRTH, 1)                           # slope 28.79 thousand / thousand

STORKS_C, BIRTHS_C, AREA_C, SPUR_C = BLUE, PURPLE, YELLOW, RED


def plot_frame(xr, yr, xt, yt, x0, y0, w, h, xlab, ylab):
    """Hand-built axes so the box stays put while the data range changes.
    Returns (VGroup(lines, ticks, nums, titles, zero-lines), c2p)."""
    (xlo, xhi), (ylo, yhi) = xr, yr

    def c2p(x, y):
        return np.array([x0 + (x - xlo) / (xhi - xlo) * w, y0 + (y - ylo) / (yhi - ylo) * h, 0.0])

    lines = VGroup(Line(c2p(xlo, ylo), c2p(xhi, ylo)), Line(c2p(xlo, ylo), c2p(xlo, yhi)))
    lines.set_stroke(GRAY, 2.5)
    ticks, nums = VGroup(), VGroup()
    for v in xt:
        p = c2p(v, ylo)
        ticks.add(Line(p, p + DOWN * 0.1, stroke_color=GRAY, stroke_width=2.5))
        nums.add(MathTex(f"{v:g}", font_size=MATH_SMALL, color=GRAY).next_to(p, DOWN, buff=0.18))
    for v in yt:
        p = c2p(xlo, v)
        ticks.add(Line(p, p + LEFT * 0.1, stroke_color=GRAY, stroke_width=2.5))
        nums.add(MathTex(f"{v:g}", font_size=MATH_SMALL, color=GRAY).next_to(p, LEFT, buff=0.18))
    zero = VGroup()
    if xlo < 0 < xhi:
        zero.add(DashedLine(c2p(0, ylo), c2p(0, yhi), dash_length=0.08, stroke_width=1.5, color=DIM))
    if ylo < 0 < yhi:
        zero.add(DashedLine(c2p(xlo, 0), c2p(xhi, 0), dash_length=0.08, stroke_width=1.5, color=DIM))
    xt_ = label(xlab, color=STORKS_C).next_to(nums[:len(xt)], DOWN, buff=0.15)
    xt_.align_to(lines[0], RIGHT)
    yt_ = label(ylab, color=BIRTHS_C).next_to(lines[1].get_end(), UP, buff=0.25)
    yt_.align_to(nums[len(xt):], LEFT)
    g = VGroup(zero, lines, ticks, nums, xt_, yt_)
    g.zero, g.lines, g.ticks, g.nums, g.xt, g.yt = zero, lines, ticks, nums, xt_, yt_
    return g, c2p


def node(s, color, size=LABEL + 2):
    t = text(s, size=size, color=color)
    frame = RoundedRectangle(width=t.width + 0.45, height=t.height + 0.36, corner_radius=0.14,
                             stroke_color=color, stroke_width=2.5, fill_color=BG, fill_opacity=1)
    g = VGroup(frame, t)
    g.frame, g.label = frame, t
    return g


def edge(a, b, gap=0.1):
    """Point on the border of node a (a rectangle) in the direction of b's centre."""
    c, d = a.get_center(), b.get_center() - a.get_center()
    hw, hh = a.frame.width / 2, a.frame.height / 2
    t = min(hw / max(abs(d[0]), 1e-6), hh / max(abs(d[1]), 1e-6))
    u = d / np.linalg.norm(d)
    return c + t * d + gap * u


def arrow(a, b, color, dashed=False):
    s, e = edge(a, b), edge(b, a)
    if dashed:
        m = DashedLine(s, e, dash_length=0.13, stroke_width=4, color=color)
        m.add_tip(tip_length=0.22, tip_width=0.2)
        return m
    return Arrow(s, e, buff=0, stroke_width=4, color=color, tip_length=0.22,
                 max_tip_length_to_length_ratio=0.3)


class Episode(NarratedScene):
    EPISODE = 48
    TITLE = "Storks Deliver Babies (p = 0.008)"
    PRONUNCIATIONS = {"Matthews": "math yooz"}

    def construct(self):
        r_big = np.maximum(0.075, 0.34 * np.sqrt(AREA / AREA.max()))

        # ============================================================ phase A: big raw scatter
        A, c2a = plot_frame((0, 32), (0, 1700), [0, 10, 20, 30], [0, 500, 1000, 1500],
                            -5.4, -2.0, 7.7, 4.75, "stork pairs (thousands)",
                            "births (thousands / yr)")
        dts = VGroup(*[Dot(c2a(s, b), radius=0.085, color=INK, fill_opacity=0.9)
                       for s, b in zip(STORK, BIRTH)])
        for d in dts:
            d.set_z_index(2)
        line = Line(c2a(0, NAIVE[1]), c2a(31, np.polyval(NAIVE, 31)), color=SPUR_C, stroke_width=4)
        r_tex = formula("r", "=", "0.62", size=48, color=SPUR_C)
        p_tex = formula("p", "=", "0.008", size=48, color=SPUR_C)
        stats = VGroup(r_tex, p_tex).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        stats.move_to([4.6, 1.9, 0])

        self.add(A.lines, A.ticks)
        with self.narrate("Seventeen European countries, one dot each. Across, pairs of breeding "
                          "storks. Up, babies born per year. The line climbs. The correlation, r, "
                          "is point six two, and p is point oh oh eight. Is this a fluke? "
                          "Commit to an answer. [pause 1.5]") as beat:
            self.play(LaggedStart(*[GrowFromCenter(d) for d in dts], lag_ratio=0.12),
                      FadeIn(A.nums), run_time=beat.until("Across", offset=-0.1))
            self.play(FadeIn(A.xt, shift=0.1 * UP), A.lines[0].animate.set_color(STORKS_C),
                      run_time=0.8)
            self.play(A.lines[0].animate.set_color(GRAY), run_time=beat.until("Up", offset=-0.1))
            self.play(FadeIn(A.yt, shift=0.1 * DOWN), A.lines[1].animate.set_color(BIRTHS_C),
                      run_time=0.8)
            self.play(A.lines[1].animate.set_color(GRAY), run_time=beat.until("line", offset=-0.1))
            self.play(Create(line), run_time=beat.until("correlation", offset=-0.1))
            beat.wait_until("r", offset=-0.15)
            self.play(TransformFromCopy(line, r_tex), run_time=1.0)
            beat.wait_until("p", offset=-0.15)
            self.play(TransformFromCopy(line, p_tex), run_time=1.0)
            beat.wait_until("fluke", offset=-0.1)
            self.play(Indicate(p_tex, color=SPUR_C, scale_factor=1.12), run_time=1.0)
            beat.wait_until("Commit", offset=0.2)
            ring = box(p_tex, color=INK, buff=0.18)
            self.play(Create(ring), run_time=0.8)
            self.play(Uncreate(ring), run_time=beat.remaining(), rate_func=lambda t: max(0, (t - 0.6) / 0.4))

        cite_m = citation("Matthews, 2000 · Teaching Statistics 22(2)")
        with self.narrate("It's not a fluke. These are real counts, published in two thousand by "
                          "Robert Matthews in the journal Teaching Statistics. His point: suspected "
                          "links, like diet and cancer, often get their first test exactly this way."
                          ) as beat:
            beat.wait_until("real", offset=-0.1)
            self.play(LaggedStart(*[Indicate(d, color=INK, scale_factor=1.5) for d in dts],
                                  lag_ratio=0.08), run_time=beat.until("published"))
            self.play(FadeIn(cite_m, shift=0.1 * UP), run_time=0.8)
            beat.wait_until("this way", offset=-0.5)
            self.play(Indicate(VGroup(line, stats), color=SPUR_C, scale_factor=1.04), run_time=1.0)

        # ---- naive build: slope triangle
        x1, x2 = 10, 20
        y1, y2 = np.polyval(NAIVE, x1), np.polyval(NAIVE, x2)
        run = Line(c2a(x1, y1), c2a(x2, y1), color=STORKS_C, stroke_width=5)
        rise = Line(c2a(x2, y1), c2a(x2, y2), color=BIRTHS_C, stroke_width=5)
        run_l = formula(r"+10{,}000", size=36, color=STORKS_C).next_to(run, DOWN, buff=0.15)
        rise_l = formula(r"+288{,}000", size=36, color=BIRTHS_C).next_to(rise, RIGHT, buff=0.15)
        frac = MathTex(r"{288{,}000", r"\over", r"10{,}000}", r"\approx", "29", font_size=52)
        frac[0].set_color(BIRTHS_C)
        frac[2].set_color(STORKS_C)
        frac.move_to([4.6, -0.3, 0])
        per = label("babies per pair, per year").next_to(frac, DOWN, buff=0.3)
        with self.narrate("So take the line at its word. Ten thousand more stork pairs, and births "
                          "rise by two hundred and eighty-eight thousand. That's twenty-nine babies "
                          "per stork pair, per year. And if storks and births were unrelated, a "
                          "correlation this strong would turn up only about once in a hundred and "
                          "twenty-five tries.") as beat:
            self.play(FadeOut(cite_m), dts.animate.set_opacity(0.45), run_time=0.8)
            beat.wait_until("Ten", offset=-0.1)
            self.play(Create(run), FadeIn(run_l, shift=0.1 * DOWN), run_time=beat.until("births"))
            self.play(Create(rise), FadeIn(rise_l, shift=0.1 * LEFT), run_time=1.0)
            beat.wait_until("twenty-nine", offset=-1.2)
            self.play(TransformFromCopy(rise_l, frac[0]), TransformFromCopy(run_l, frac[2]),
                      FadeIn(frac[1]), run_time=1.0)
            self.play(Write(frac[3:]), run_time=0.6)
            self.play(FadeIn(per, shift=0.1 * UP), run_time=0.6)
            beat.wait_until("unrelated", offset=-0.2)
            self.play(Indicate(p_tex, color=SPUR_C, scale_factor=1.12), run_time=1.0)
            once = formula(r"\approx \tfrac{1}{125}", size=40, color=SPUR_C).next_to(p_tex, RIGHT, buff=0.3)
            beat.wait_until("once", offset=-0.1)
            self.play(FadeIn(once, shift=0.1 * LEFT), run_time=0.8)

        # ---- the test: dot size = land area
        test_l = label("same size?", color=AREA_C)
        with self.narrate("A causal claim should survive one test: compare countries of the same "
                          "size. So let each dot's area show its country's land area.") as beat:
            self.play(FadeOut(VGroup(run, rise, run_l, rise_l)), FadeOut(VGroup(frac, per)),
                      FadeOut(once), dts.animate.set_opacity(0.9), run_time=1.0)
            beat.wait_until("land area", offset=-0.3)
            self.play(*[d.animate.scale(r / 0.085).set_fill(AREA_C, 0.3).set_stroke(AREA_C, 2.5, 1)
                        for d, r in zip(dts, r_big)], run_time=beat.remaining(min_time=1.5))

        big_names = {}
        for n, direc in (("Turkey", LEFT), ("Germany", RIGHT), ("France", DR)):
            i = NAMES.index(n)
            big_names[n] = label(n, size=26, color=GRAY).next_to(dts[i], direc, buff=0.12)
        small_ring = Ellipse(width=0.95, height=0.95, color=GRAY, stroke_width=2).move_to(c2a(0.6, 110))
        cor_ab = VGroup(text("land area & births", size=26, t2c={"land area": AREA_C, "births": BIRTHS_C}),
                        formula("r", "=", "0.92", size=40))
        cor_as = VGroup(text("land area & storks", size=26, t2c={"land area": AREA_C, "storks": STORKS_C}),
                        formula("r", "=", "0.58", size=40))
        for g in (cor_ab, cor_as):
            g.arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        cors = VGroup(cor_ab, cor_as).arrange(DOWN, buff=0.45, aligned_edge=LEFT).move_to([4.6, -0.5, 0])
        with self.narrate("The biggest dots ride high: Turkey, Germany, France. The small ones huddle "
                          "near zero. Land area alone tracks births with a correlation of point nine "
                          "two. It tracks storks too, at point five eight. Size is doing the work."
                          ) as beat:
            for n in ("Turkey", "Germany", "France"):
                beat.wait_until(n, offset=-0.15)
                self.play(FadeIn(big_names[n], shift=0.08 * RIGHT),
                          flag(dts[NAMES.index(n)], color=AREA_C), run_time=0.6)
            beat.wait_until("small", offset=-0.1)
            self.play(Create(small_ring), run_time=0.9)
            beat.wait_until("births", offset=-0.2)
            self.play(FadeIn(cor_ab, shift=0.1 * UP), run_time=0.9)
            beat.wait_until("storks", offset=-0.2)
            self.play(FadeIn(cor_as, shift=0.1 * UP), run_time=0.9)
            beat.wait_until("Size", offset=-0.1)
            self.play(Indicate(VGroup(cor_ab[1], cor_as[1]), color=AREA_C, scale_factor=1.1), run_time=1.0)

        # ============================================================ phase B: DAG beside scatter
        X0, Y0, W, H = -5.3, -1.55, 5.0, 3.65
        B1, c2b = plot_frame((0, 32), (0, 1700), [0, 10, 20, 30], [0, 500, 1000, 1500],
                             X0, Y0, W, H, "stork pairs (thousands)", "births (thousands / yr)")
        r_small = np.maximum(0.06, 0.26 * np.sqrt(AREA / AREA.max()))
        n_area = node("land area", AREA_C).move_to([3.45, 2.75, 0])
        n_st = node("storks", STORKS_C).move_to([1.35, 1.05, 0])
        n_bi = node("births", BIRTHS_C).move_to([5.55, 1.05, 0])
        a_ab = arrow(n_area, n_bi, AREA_C)
        a_as = arrow(n_area, n_st, AREA_C)
        a_sb = arrow(n_st, n_bi, STORKS_C, dashed=True)
        p_small = formula("p", "=", "0.008", size=40, color=SPUR_C).move_to([3.45, -2.15, 0])
        line_b = Line(c2b(0, NAIVE[1]), c2b(31, np.polyval(NAIVE, 31)), color=SPUR_C, stroke_width=4)
        with self.narrate("Draw that as arrows. Area points to births: more land, more people. Area "
                          "points to storks: more land, more nests. The claim on trial is this dashed "
                          "arrow, from storks to births.") as beat:
            self.play(FadeOut(VGroup(*big_names.values(), small_ring, cors, r_tex)),
                      ReplacementTransform(p_tex, p_small),
                      ReplacementTransform(VGroup(A.lines, A.ticks), VGroup(B1.lines, B1.ticks)),
                      FadeTransform(A.nums, B1.nums), FadeTransform(A.xt, B1.xt),
                      FadeTransform(A.yt, B1.yt), Transform(line, line_b),
                      *[d.animate.scale(rs / rb).move_to(c2b(s, b))
                        for d, rs, rb, s, b in zip(dts, r_small, r_big, STORK, BIRTH)],
                      run_time=1.4)
            self.play(FadeIn(n_area, shift=0.1 * DOWN), TransformFromCopy(B1.xt, n_st),
                      TransformFromCopy(B1.yt, n_bi), run_time=beat.until("Area", offset=-0.1))
            self.play(GrowArrow(a_ab), run_time=1.0)
            beat.wait_until("Area", 2, offset=-0.1)
            self.play(GrowArrow(a_as), run_time=1.0)
            beat.wait_until("dashed", offset=-0.2)
            self.play(Create(a_sb), run_time=1.0)
            self.play(flag(a_sb, color=STORKS_C), run_time=0.8)

        # ---- the back door
        p1 = n_st.get_top() + RIGHT * 0.55 + UP * 0.12
        p2 = n_area.get_bottom() + DOWN * 0.22
        p3 = n_bi.get_top() + LEFT * 0.55 + UP * 0.12
        door1 = Line(p1, p2, color=SPUR_C, stroke_width=6)
        door2 = Line(p2, p3, color=SPUR_C, stroke_width=6).add_tip(tip_length=0.2, tip_width=0.2)
        with self.narrate("Even if that arrow were missing, a path would still connect them: from "
                          "storks, back through area, to births. That's a back door. It carries "
                          "correlation, but no causation.") as beat:
            beat.wait_until("missing", offset=-0.2)
            self.play(a_sb.animate.set_opacity(0.25), run_time=0.8)
            beat.wait_until("storks", offset=-0.1)
            self.play(flag(n_st, color=STORKS_C), run_time=0.7)
            self.play(Create(door1), run_time=beat.until("births", offset=-0.1))
            self.play(Create(door2), run_time=1.0)
            beat.wait_until("correlation", offset=-0.2)
            self.play(Indicate(line, color=SPUR_C, scale_factor=1.05),
                      Indicate(VGroup(door1, door2), color=SPUR_C, scale_factor=1.05), run_time=1.0)
            beat.wait_until("no causation", offset=-0.1)
            self.play(a_sb.animate.set_opacity(1), run_time=0.8)

        # ---- formula from the arrows into births
        eq = formula(r"\text{births}", "=", "a", "+", "b", r"\,\text{storks}", "+", "c",
                     r"\,\text{area}", size=40)
        eq[0].set_color(BIRTHS_C)
        eq[5].set_color(STORKS_C)
        eq[8].set_color(AREA_C)
        eq.move_to([3.45, -0.25, 0])
        with self.narrate("Every arrow into births becomes a term. Births equals a, plus b times "
                          "storks, plus c times area. The number on trial is b.") as beat:
            self.play(Indicate(a_sb, color=STORKS_C, scale_factor=1.05),
                      Indicate(a_ab, color=AREA_C, scale_factor=1.05), run_time=1.0)
            beat.wait_until("Births", offset=-0.2)
            self.play(TransformFromCopy(n_bi.label, eq[0]), run_time=1.0)
            self.play(Write(eq[1:4]), run_time=beat.until("b", offset=-0.1))
            self.play(TransformFromCopy(a_sb, eq[4:6]), run_time=1.0)
            beat.wait_until("c", offset=-0.1)
            self.play(Write(eq[6]), TransformFromCopy(a_ab, eq[7:9]), run_time=1.0)
            beat.wait_until("trial", offset=-0.1)
            self.play(Create(ub := underline(eq[4], color=INK)), run_time=0.6)

        # b readout, live from the dots
        lam = ValueTracker(0.0)
        lamT = ValueTracker(0.0)

        def data_pos(i, L):
            return STORK[i] - L * PRED_S[i], BIRTH[i] - L * PRED_B[i]

        def cur_fit():
            L = lam.get_value()
            xs = STORK - L * PRED_S
            ys = BIRTH - L * PRED_B
            return np.polyfit(xs, ys, 1)

        b_val = ValueTracker(NAIVE[0])
        b_num = DecimalNumber(NAIVE[0], num_decimal_places=0, font_size=44, color=SPUR_C)
        b_lhs = formula("b", r"\approx", size=44)
        b_unit = label("babies per pair")
        b_row = VGroup(b_lhs, b_num, b_unit).arrange(RIGHT, buff=0.2)
        b_unit.align_to(b_lhs, DOWN)
        b_row.move_to([3.45, -1.2, 0])
        b_num.add_updater(lambda m: m.set_value(b_val.get_value()))

        # ---- close the door for one country
        X2 = plot_frame((-15, 32), (-500, 1700), [-10, 0, 10, 20, 30], [-500, 0, 500, 1000, 1500],
                        X0, Y0, W, H, "stork pairs (thousands)", "births (thousands / yr)")
        B2, c2c = X2
        r_c = np.maximum(0.055, 0.22 * np.sqrt(AREA / AREA.max()))
        gate = SurroundingRectangle(n_area, color=INK, buff=0.1, stroke_width=3.5)
        line_c = Line(c2c(-14, np.polyval(NAIVE, -14)), c2c(31, np.polyval(NAIVE, 31)),
                      color=SPUR_C, stroke_width=4)
        tx, ty = STORK[T], BIRTH[T]
        h_arr = Arrow(c2c(tx, ty), c2c(tx - PRED_S[T], ty), buff=0, color=STORKS_C, stroke_width=4,
                      tip_length=0.2, max_tip_length_to_length_ratio=0.2)
        v_arr = Arrow(c2c(tx - PRED_S[T], ty), c2c(tx - PRED_S[T], ty - PRED_B[T]), buff=0,
                      color=BIRTHS_C, stroke_width=4, tip_length=0.2, max_tip_length_to_length_ratio=0.2)
        h_lab = formula(r"-18{,}000", size=36, color=STORKS_C).next_to(h_arr, DOWN, buff=0.15)
        v_lab = formula(r"-1.3\text{ million}", size=36, color=BIRTHS_C).next_to(v_arr, LEFT, buff=0.15)
        with self.narrate("To estimate b, close the back door: hold area fixed by subtracting what "
                          "each country's size alone predicts. For Turkey, that's eighteen thousand "
                          "stork pairs and one point three million births. Take them away, and "
                          "Turkey slides down here.") as beat:
            self.play(FadeOut(ub), TransformFromCopy(eq[4], b_lhs[0]), FadeIn(b_lhs[1]),
                      FadeIn(b_num), FadeIn(b_unit), run_time=1.0)
            beat.wait_until("close", offset=-0.1)
            self.play(Create(gate), VGroup(door1, door2).animate.set_opacity(0.2), run_time=1.0)
            beat.wait_until("subtracting", offset=-0.2)
            self.play(ReplacementTransform(VGroup(B1.lines, B1.ticks), VGroup(B2.lines, B2.ticks)),
                      FadeTransform(B1.nums, B2.nums), FadeIn(B2.zero),
                      ReplacementTransform(B1.xt, B2.xt), ReplacementTransform(B1.yt, B2.yt),
                      Transform(line, line_c),
                      *[d.animate.scale(rc / rs).move_to(c2c(s, b))
                        for d, rc, rs, s, b in zip(dts, r_c, r_small, STORK, BIRTH)],
                      run_time=1.5)
            beat.wait_until("Turkey", offset=-0.15)
            self.play(flag(dts[T], color=AREA_C), run_time=0.7)
            beat.wait_until("eighteen", offset=-0.1)
            self.play(GrowArrow(h_arr), FadeIn(h_lab), run_time=1.0)
            beat.wait_until("one point three", offset=-0.1)
            self.play(GrowArrow(v_arr), FadeIn(v_lab), run_time=1.0)
            beat.wait_until("Take", offset=-0.1)
            dts[T].add_updater(lambda m: m.move_to(c2c(*data_pos(T, lamT.get_value()))))
            self.play(lamT.animate.set_value(1.0), run_time=beat.until("here", offset=0.1))
            self.play(flag(dts[T], color=AREA_C), run_time=0.8)

        with self.narrate("Now the other sixteen. Will the line stay steep? [pause 1.5]") as beat:
            self.play(FadeOut(VGroup(h_arr, v_arr, h_lab, v_lab)), run_time=0.8)
            others = VGroup(*[d for i, d in enumerate(dts) if i != T])
            self.play(Indicate(others, color=INK, scale_factor=1.2), run_time=1.0)
            beat.wait_until("steep", offset=0.2)
            self.play(Indicate(line, color=SPUR_C, scale_factor=1.04), run_time=1.0)

        # ---- the result: everyone slides, the line refits live
        ghost = line.copy().set_stroke(opacity=0.35)
        line.clear_updaters()
        self.add(ghost)
        self.bring_to_front(line)
        for i, d in enumerate(dts):
            if i != T:
                d.add_updater(lambda m, i=i: m.move_to(c2c(*data_pos(i, lam.get_value()))))

        def line_upd(m):
            k, c0 = cur_fit()
            m.put_start_and_end_on(c2c(-14, c0 + k * -14), c2c(31, c0 + k * 31))
            m.set_color(interpolate_color(ManimColor(SPUR_C), ManimColor(INK), lam.get_value()))
        line.add_updater(line_upd)
        b_num.add_updater(lambda m: m.set_color(interpolate_color(ManimColor(SPUR_C), ManimColor(INK),
                                                                  lam.get_value())))
        b_val.add_updater(lambda m: m.set_value(cur_fit()[0]))
        self.add(b_val)
        p_new = formula("p", "=", "0.31", size=40, color=INK).move_to(p_small)
        xt_new = label("storks, size removed (thousands)", color=STORKS_C)
        xt_new.next_to(B2.nums[:5], DOWN, buff=0.15).align_to(B2.lines[0], RIGHT)
        yt_new = label("births, size removed (thousands / yr)", color=BIRTHS_C)
        yt_new.move_to(B2.yt, aligned_edge=LEFT)
        cite_p = citation("Pearl, 2000 · Causality (Cambridge University Press)")
        with self.narrate("It nearly flattens. b falls from twenty-nine babies per pair to six, and p "
                          "climbs to point three one. With seventeen countries, six is "
                          "indistinguishable from zero.") as beat:
            self.play(lam.animate.set_value(1.0), run_time=beat.until("six", offset=0.1),
                      rate_func=SMOOTH)
            self.play(ReplacementTransform(B2.xt, xt_new), ReplacementTransform(B2.yt, yt_new),
                      run_time=0.9)
            beat.wait_until("p", offset=-0.2)
            self.play(TransformMatchingTex(p_small, p_new), run_time=1.0)
            beat.wait_until("indistinguishable", offset=-0.2)
            self.play(Indicate(B2.zero[1], color=INK, scale_factor=1.0), flag(line, color=INK),
                      run_time=1.0)

        with self.narrate("That's Judea Pearl's back-door rule: draw the diagram, then adjust for "
                          "whatever blocks every back-door path.") as beat:
            self.play(FadeIn(cite_p, shift=0.1 * UP), run_time=0.8)
            beat.wait_until("draw", offset=-0.1)
            self.play(Indicate(VGroup(n_area, n_st, n_bi, a_ab, a_as, a_sb), color=INK,
                               scale_factor=1.03), run_time=1.0)
            beat.wait_until("blocks", offset=-0.1)
            self.play(Indicate(gate, color=INK, scale_factor=1.08), run_time=1.0)

        # ---- honest limit: a collider
        n_col = node("common effect", GRAY).move_to([3.45, -0.75, 0])
        a_sc = arrow(n_st, n_col, GRAY)
        a_bc = arrow(n_bi, n_col, GRAY)
        q1 = n_st.get_bottom() + RIGHT * 0.45 + DOWN * 0.1
        q2 = n_col.get_top() + UP * 0.2
        q3 = n_bi.get_bottom() + LEFT * 0.45 + DOWN * 0.1
        col_path = VGroup(Line(q1, q2, color=SPUR_C, stroke_width=6),
                          Line(q2, q3, color=SPUR_C, stroke_width=6))
        col_box = SurroundingRectangle(n_col, color=INK, buff=0.1, stroke_width=3.5)
        with self.narrate("But the diagram is an assumption, and no regression can draw it for you. "
                          "Adjusting for everything isn't safe either: box a variable that two arrows "
                          "point into, and you open a path instead of closing one.") as beat:
            self.play(FadeOut(cite_p), run_time=0.6)
            beat.wait_until("regression", offset=-0.2)
            self.play(FadeOut(VGroup(eq, b_row, p_new), shift=0.2 * DOWN), run_time=1.0)
            beat.wait_until("two arrows", offset=-0.4)
            self.play(FadeIn(n_col), GrowArrow(a_sc), GrowArrow(a_bc), run_time=1.2)
            beat.wait_until("open", offset=-0.6)
            self.play(Create(col_box), run_time=0.6)
            self.play(Create(col_path), run_time=beat.until("instead", offset=0.2))

        with self.narrate("So look at the opening plot again. The p-value was right: something real "
                          "links storks and babies. It just has an arrow pointing at both.") as beat:
            self.play(FadeOut(VGroup(n_col, a_sc, a_bc, col_box, col_path)), run_time=0.8)
            self.play(lam.animate.set_value(0.0), lamT.animate.set_value(0.0),
                      ReplacementTransform(xt_new, B2.xt), ReplacementTransform(yt_new, B2.yt),
                      run_time=beat.until("right", offset=-0.2))
            self.play(Indicate(line, color=SPUR_C, scale_factor=1.04), run_time=1.0)
            beat.wait_until("arrow", offset=-0.2)
            self.play(VGroup(door1, door2).animate.set_opacity(1),
                      Indicate(VGroup(a_as, a_ab, n_area), color=AREA_C, scale_factor=1.06),
                      run_time=1.2)

        for d in dts:
            d.clear_updaters()
        line.clear_updaters()
        self.end_card()
