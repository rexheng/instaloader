"""Episode 76 - The Winning Strategy That Never Won a Single Game.

    videos/toolkit/render.sh --preview videos/episodes/076-axelrod-tournament/scene.py Episode /tmp/ep76.mp4
"""
from manim import *
from sample_space import *

# --------------------------------------------------------------------------- the game
PAY = {("C", "C"): (3, 3), ("C", "D"): (0, 5), ("D", "C"): (5, 0), ("D", "D"): (1, 1)}
ROUNDS = 200


def s_alld(me, op):
    return "D"


def s_tft(me, op):
    return op[-1] if op else "C"


def s_grudger(me, op):
    return "D" if "D" in op else "C"


def s_stft(me, op):
    return op[-1] if op else "D"


FIELD = [("Always Defect", s_alld), ("Tit for Tat", s_tft), ("Grudger", s_grudger),
         ("Suspicious TFT", s_stft)]
HEADERS = [("Always", "Defect"), ("Tit for", "Tat"), ("Grudger",), ("Suspicious", "TFT")]


def play_match(a, b, n=ROUNDS):
    ma, mb, sa, sb = [], [], 0, 0
    for _ in range(n):
        x, y = a(ma, mb), b(mb, ma)
        pa, pb = PAY[(x, y)]
        sa, sb = sa + pa, sb + pb
        ma.append(x)
        mb.append(y)
    return sa, sb


SCORES = [[play_match(fa, fb) for _, fb in FIELD] for _, fa in FIELD]
TOTALS = [sum(c[0] for c in row) for row in SCORES]
assert SCORES[0][1] == (204, 199) and TOTALS[0] == 808 and TOTALS[1] == 1899

# --------------------------------------------------------------------------- layout
COL_X = [-2.4, -0.6, 1.2, 3.0]
TOT_X = 5.15
ROW_Y = [2.0, 0.95, -0.1, -1.15]
HEAD_Y = 3.05
LABEL_RIGHT = -3.45
BAR_W = 0.62
K = 0.2                      # units per (point per round)


def sq(m, s=0.42):
    """One move: green C (cooperate) or red D (defect). Letter + colour, never colour alone."""
    box_ = Square(s, stroke_width=0, fill_color=GREEN if m == "C" else RED, fill_opacity=0.92)
    let = Text(m, font=SERIF, font_size=22, color=BG, weight=BOLD).move_to(box_)
    return VGroup(box_, let)


def strip(moves, x0, y, s=0.42, step=0.52):
    return VGroup(*[sq(m, s).move_to([x0 + i * step, y, 0]) for i, m in enumerate(moves)])


def row_label(s, y, size=LABEL, color=INK):
    t = text(s, size=size, color=color)
    return t.move_to([LABEL_RIGHT - t.width / 2, y, 0])


class Episode(NarratedScene):
    EPISODE = 76
    TITLE = "The Winning Strategy That Never Won a Single Game"
    PRONUNCIATIONS = {"Axelrod": "axle rod", "Grudger": "grudger"}

    # ------------------------------------------------------------------ build helpers
    def ladder(self, n=15, x=3.9, top=2.8, bottom=-2.8, length=1.3, labels=("1st", "15th")):
        ys = np.linspace(top, bottom, n)
        slots = VGroup(*[Line([x - length / 2, y, 0], [x + length / 2, y, 0], color=GRAY,
                              stroke_width=4) for y in ys])
        lo = label(labels[0], size=26, color=GRAY).next_to(slots[0], LEFT, buff=0.25)
        hi = label(labels[1], size=26, color=GRAY).next_to(slots[-1], LEFT, buff=0.25)
        return VGroup(slots, lo, hi)

    def payoff_grid(self):
        cw, ch = 2.3, 1.25
        cells, nums = VGroup(), {}
        for i, me in enumerate("CD"):
            for j, op in enumerate("CD"):
                r = Rectangle(width=cw, height=ch, stroke_color=DIM, stroke_width=2)
                r.move_to([j * cw, -i * ch, 0])
                a, b = PAY[(me, op)]
                na = MathTex(str(a), font_size=52, color=BLUE)
                nb = MathTex(str(b), font_size=52, color=GRAY)
                pair = VGroup(na, nb).arrange(RIGHT, buff=0.7).move_to(r)
                cells.add(r)
                nums[(me, op)] = pair
        row_heads = VGroup(*[sq(m, 0.5).next_to(cells[2 * i], LEFT, buff=0.3)
                             for i, m in enumerate("CD")])
        col_heads = VGroup(*[sq(m, 0.5).next_to(cells[j], UP, buff=0.3)
                             for j, m in enumerate("CD")])
        you = text("you", size=32, color=BLUE).next_to(row_heads, LEFT, buff=0.3)
        them = text("them", size=32, color=GRAY).next_to(col_heads, UP, buff=0.25)
        g = VGroup(cells, row_heads, col_heads, you, them, *nums.values())
        g.nums, g.cells, g.row_heads, g.col_heads, g.you, g.them = nums, cells, row_heads, col_heads, you, them
        return g

    # ------------------------------------------------------------------ the episode
    def construct(self):
        # ============ 1. cold open: the card and the ladder =======================
        lad = self.ladder()
        card_lbl = text("opponents it outscored", size=32).move_to([-3.0, 1.55, 0])
        zero = MathTex("0", font_size=120, color=YELLOW).next_to(card_lbl, DOWN, buff=0.35)
        qmark = MathTex("?", font_size=60, color=YELLOW)
        arrow = Triangle(color=YELLOW, fill_color=YELLOW, fill_opacity=1, stroke_width=0)
        arrow.scale(0.16).rotate(PI / 2)
        marker = VGroup(arrow, qmark).arrange(RIGHT, buff=0.15)
        marker.next_to(lad[0][7], RIGHT, buff=0.2)
        with self.narrate("In nineteen eighty, Robert Axelrod pitted fifteen computer programs "
                          "against each other. One of them never outscored a single opponent. "
                          "Where did it finish? [pause 1.5]") as beat:
            self.play(LaggedStart(*[Create(s) for s in lad[0]], lag_ratio=0.12),
                      FadeIn(lad[1:]), run_time=beat.until_end_of("programs"))
            beat.wait_until("One of them", offset=-0.1)
            self.play(FadeIn(card_lbl, shift=0.2 * UP), run_time=0.8)
            self.play(FadeIn(zero, scale=0.6), run_time=beat.until("Where", offset=-0.1))
            self.play(FadeIn(marker, shift=0.3 * LEFT), run_time=0.7)

        # ============ 2. first: Tit for Tat, cooperate then copy =================
        name = text("Tit for Tat", size=HEADING, color=YELLOW).next_to(card_lbl, UP, buff=0.5)
        them_moves = "CDDCCC"
        tft_moves = "C" + them_moves[:-1]
        x0 = -3.6
        top = strip(them_moves, x0, -1.35, step=0.62)
        bot = strip(tft_moves, x0, -2.35, step=0.62)
        l_top = row_label("them", -1.35, color=GRAY).shift(RIGHT * 0.25 + LEFT * 0.0)
        l_bot = row_label("Tit for Tat", -2.35)
        l_top.next_to(top, LEFT, buff=0.35)
        l_bot.next_to(bot, LEFT, buff=0.35)
        copies = VGroup(*[Arrow(top[i].get_bottom() + 0.05 * RIGHT, bot[i + 1].get_top() + 0.05 * LEFT,
                                buff=0.06, stroke_width=3, color=YELLOW,
                                max_tip_length_to_length_ratio=0.25)
                          for i in range(len(them_moves) - 1)])
        first_tag = text("1st", size=32, color=YELLOW)
        with self.narrate("First. It was Tit for Tat, the simplest entry: cooperate on the first "
                          "move, then copy whatever the other side did last.") as beat:
            first_tag.next_to(lad[0][0], RIGHT, buff=0.55)
            self.play(marker.animate.next_to(lad[0][0], RIGHT, buff=0.2),
                      lad[0][0].animate.set_color(YELLOW), run_time=0.9)
            self.play(Transform(marker[1], first_tag.move_to(marker[1], aligned_edge=LEFT)),
                      run_time=0.5)
            self.play(Write(name), run_time=beat.until("cooperate", offset=-0.1))
            self.play(FadeIn(l_bot), FadeIn(bot[0], scale=0.6), run_time=0.6)
            self.play(FadeIn(l_top), LaggedStart(*[FadeIn(s, scale=0.6) for s in top], lag_ratio=0.15),
                      run_time=beat.until("copy", offset=-0.1))
            self.play(LaggedStart(*[AnimationGroup(GrowArrow(copies[i]), FadeIn(bot[i + 1], scale=0.6))
                                    for i in range(len(copies))], lag_ratio=0.35),
                      run_time=beat.remaining() - 0.1)
        card = VGroup(name, card_lbl, zero)
        rule = VGroup(top, bot, l_top, l_bot, copies)

        # ============ 3. the payoff grid ==========================================
        grid = self.payoff_grid()
        grid.move_to([0.4, -0.35, 0])
        frame_parts = VGroup(grid.cells, grid.row_heads, grid.col_heads, grid.you, grid.them)
        with self.narrate("Every match was two hundred rounds of the prisoner's dilemma. Both "
                          "cooperate: three points each. Both defect: one each. Defect on a "
                          "cooperator, and you take five while they get zero.") as beat:
            self.play(FadeOut(rule), FadeOut(card), FadeOut(lad), FadeOut(marker), run_time=0.7)
            self.play(FadeIn(frame_parts), run_time=beat.until("Both", offset=-0.1))
            self.play(Indicate(grid.cells[0], color=YELLOW, scale_factor=1.0),
                      FadeIn(grid.nums[("C", "C")], scale=0.7), run_time=1.0)
            beat.wait_until("Both", occurrence=2, offset=-0.1)
            self.play(FadeIn(grid.nums[("D", "D")], scale=0.7), run_time=0.9)
            beat.wait_until("Defect", offset=-0.1)
            self.play(Indicate(grid.row_heads[1], color=YELLOW), Indicate(grid.col_heads[0], color=YELLOW),
                      run_time=0.9)
            self.play(FadeIn(grid.nums[("D", "C")][0], scale=0.7), run_time=beat.until("they", offset=-0.1))
            self.play(FadeIn(grid.nums[("D", "C")][1], scale=0.7), FadeIn(grid.nums[("C", "D")], scale=0.7),
                      run_time=0.9)

        # ============ 4. stakes and the question ==================================
        times = MathTex(r"\times\,200", r"\text{ rounds}", font_size=40, color=GRAY)
        with self.narrate("Price wars and arms races have this shape, played over and over. So how "
                          "do you win a tournament without winning a match?") as beat:
            self.play(grid.animate.scale(0.62).to_corner(UR, buff=0.0).shift(LEFT * 0.75 + DOWN * 0.42),
                      run_time=1.2)
            times.next_to(grid, LEFT, buff=0.4).shift(DOWN * 0.15)
            self.play(Write(times), run_time=beat.until("So", offset=-0.1))
            card.scale(0.85).move_to([-2.6, 0.2, 0])
            place = text("finished 1st", size=32, color=YELLOW).next_to(card, DOWN, buff=0.35)
            self.play(FadeIn(card, shift=0.2 * UP), run_time=0.9)
            self.play(FadeIn(place, shift=0.2 * UP), run_time=0.8)

        # ============ 5. naive build: Always Defect ===============================
        lab_tft = row_label("Tit for Tat", -0.05)
        lab_ad = row_label("Always Defect", -1.05)
        with self.narrate("Build the opposite: a program that can never lose. Always Defect never "
                          "takes a zero, so no one can outscore it.") as beat:
            self.play(FadeOut(card), FadeOut(place), run_time=0.6)
            self.play(Write(lab_ad), run_time=beat.until("never", offset=-0.1))
            # it never plays C, so the whole "you cooperate" row (the only zero) is gone
            c_row = VGroup(grid.cells[0], grid.cells[1], grid.row_heads[0],
                           grid.nums[("C", "C")], grid.nums[("C", "D")])
            zero_num = grid.nums[("C", "D")][0]
            self.play(Indicate(zero_num, color=YELLOW, scale_factor=1.3),
                      run_time=beat.until("so", offset=-0.1))
            self.play(c_row.animate.set_opacity(0.25), run_time=0.9)

        # ============ 6. the match vs Tit for Tat ===============================
        n_vis = 11
        xs0 = -3.0
        tft_row = strip("C" + "D" * (n_vis - 1), xs0, -0.05)
        ad_row = strip("D" * n_vis, xs0, -1.05)
        dots_ = MathTex(r"\cdots", font_size=48, color=GRAY).next_to(VGroup(tft_row, ad_row), RIGHT, buff=0.3)
        rnd1 = label("round 1", size=24, color=GRAY).next_to(tft_row[0], UP, buff=0.25)
        rnd1.shift(RIGHT * (rnd1.width / 2 - 0.21))
        t_ad, t_tft = ValueTracker(0), ValueTracker(0)
        sc_ad = live_number(t_ad, 0, size=52, color=BLUE)
        sc_tft = live_number(t_tft, 0, size=52, color=GRAY)
        sc_tft.move_to([5.2, -0.05, 0])
        sc_ad.move_to([5.2, -1.05, 0])
        for s_ in (sc_ad, sc_tft):
            s_.number.add_updater(lambda m, x=5.2: m.move_to([x, m.get_y(), 0]))
        copy_arrow = Arrow(ad_row[0].get_top() + 0.05 * RIGHT, tft_row[1].get_bottom(), buff=0.05,
                           stroke_width=3, color=YELLOW, max_tip_length_to_length_ratio=0.25)
        with self.narrate("Against Tit for Tat, it grabs five in round one. After that, Tit for Tat "
                          "copies the defection, and both earn one point a round. Final score: two "
                          "hundred and four to one ninety nine. A win.") as beat:
            self.play(Write(lab_tft), FadeIn(sc_ad), FadeIn(sc_tft), run_time=beat.until("five", offset=-0.5))
            self.play(FadeIn(tft_row[0], scale=0.6), FadeIn(ad_row[0], scale=0.6), FadeIn(rnd1),
                      Indicate(grid.nums[("D", "C")], color=YELLOW),
                      t_ad.animate.set_value(5), run_time=1.0)
            beat.wait_until("copies", offset=-0.2)
            self.play(GrowArrow(copy_arrow), FadeIn(tft_row[1], scale=0.6), FadeIn(ad_row[1], scale=0.6),
                      run_time=0.8)
            self.play(Indicate(grid.nums[("D", "D")], color=YELLOW),
                      LaggedStart(*[AnimationGroup(FadeIn(tft_row[i], scale=0.6), FadeIn(ad_row[i], scale=0.6))
                                    for i in range(2, n_vis)], lag_ratio=0.3),
                      t_ad.animate(rate_func=linear).set_value(5 + n_vis - 1),
                      t_tft.animate(rate_func=linear).set_value(n_vis - 1),
                      run_time=beat.until("Final", offset=-0.1))
            self.play(FadeIn(dots_),
                      t_ad.animate(rate_func=linear).set_value(204),
                      t_tft.animate(rate_func=linear).set_value(199),
                      run_time=beat.until("A win", offset=-0.1))
            self.play(Circumscribe(sc_ad, color=YELLOW, buff=0.12), run_time=1.0)

        # ============ 7. the mini tournament =====================================
        heads = VGroup()
        for x, h in zip(COL_X, HEADERS):
            g = VGroup(*[text(w, size=26, color=INK) for w in h]).arrange(DOWN, buff=0.08)
            g.move_to([x, HEAD_Y, 0])
            heads.add(g)
        rlabels = VGroup(*[row_label(nm, y) for (nm, _), y in zip(FIELD, ROW_Y)])
        tot_head = text("total", size=26, color=INK).move_to([TOT_X, HEAD_Y, 0])
        sim = label("simulated · 200 rounds per match · Axelrod's scoring", size=22, color=GRAY)
        sim.move_to([-SAFE_X + sim.width / 2, CONTENT_BOTTOM + 0.1 + sim.height / 2, 0])
        cells = []
        for i, row in enumerate(SCORES):
            crow = []
            for j, (a, b) in enumerate(row):
                sc = MathTex(str(a), font_size=40, color=BLUE).move_to([COL_X[j], ROW_Y[i] + 0.14, 0])
                d = a - b
                mg = MathTex(("+" if d > 0 else ("-" if d < 0 else r"\pm")) + str(abs(d)),
                             font_size=28, color=GRAY).next_to(sc, DOWN, buff=0.12)
                crow.append(VGroup(sc, mg))
            cells.append(crow)
        diag = VGroup(*[RoundedRectangle(corner_radius=0.08, width=1.6, height=0.95, stroke_color=YELLOW,
                                         stroke_width=2.5).move_to([COL_X[i], ROW_Y[i], 0])
                        for i in range(4)])
        with self.narrate("Now a small simulated tournament with Axelrod's scoring. Four entries; "
                          "everyone plays everyone, including its own twin. Grudger cooperates until "
                          "you defect once, then never forgives. Suspicious Tit for Tat copies too, "
                          "but opens with a defection.") as beat:
            sc_ad.number.clear_updaters()
            sc_tft.number.clear_updaters()
            self.play(FadeOut(VGroup(tft_row, ad_row, dots_, rnd1, copy_arrow, grid, times)),
                      ReplacementTransform(lab_ad, rlabels[0]), ReplacementTransform(lab_tft, rlabels[1]),
                      sc_ad.animate.move_to(cells[0][1][0]), sc_tft.animate.move_to(cells[1][0][0]),
                      run_time=1.4)
            self.remove(sc_ad, sc_tft)
            self.add(cells[0][1][0], cells[1][0][0])
            self.play(FadeIn(sim), FadeIn(cells[0][1][1]), FadeIn(cells[1][0][1]),
                      run_time=beat.until("Four", offset=-0.1))
            self.play(FadeIn(rlabels[2:]), LaggedStart(*[FadeIn(h, shift=0.15 * DOWN) for h in heads],
                                                        lag_ratio=0.2),
                      run_time=beat.until("own twin", offset=-0.2))
            self.play(LaggedStart(*[Create(d) for d in diag], lag_ratio=0.2), run_time=1.0)
            beat.wait_until("Grudger", offset=-0.15)
            self.play(FadeOut(diag), Indicate(rlabels[2], color=YELLOW), Indicate(heads[2], color=YELLOW),
                      run_time=1.0)
            beat.wait_until("Suspicious", offset=-0.15)
            self.play(Indicate(rlabels[3], color=YELLOW), Indicate(heads[3], color=YELLOW), run_time=1.0)

        # ============ 8. fill the grid ===========================================
        rest = [cells[i][j] for i in range(4) for j in range(4) if (i, j) not in ((0, 1), (1, 0))]
        with self.narrate("Each cell is the row program's score, with its margin over the opponent "
                          "underneath.") as beat:
            self.play(LaggedStart(*[FadeIn(c[0], scale=0.8) for c in rest], lag_ratio=0.12),
                      run_time=beat.until("margin", offset=-0.1))
            self.play(LaggedStart(*[FadeIn(c[1]) for c in rest], lag_ratio=0.08),
                      Indicate(cells[0][1][1], color=YELLOW), run_time=beat.remaining())

        # ============ 9. fail: wins don't add up ==================================
        trackers = [ValueTracker(0) for _ in range(4)]
        tots = VGroup(*[live_number(t, 0, size=40, color=INK) for t in trackers])
        for tn, y in zip(tots, ROW_Y):
            tn.move_to([TOT_X - 0.25, y + 0.05, 0])
        order = sorted(range(4), key=lambda i: -TOTALS[i])
        ranks = {i: ["1st", "2nd", "3rd", "4th"][order.index(i)] for i in range(4)}
        rank_lbls = VGroup(*[label(ranks[i], size=26, color=GRAY).move_to([TOT_X + 0.85, ROW_Y[i] + 0.05, 0])
                             for i in range(4)])
        row_box = lambda i: SurroundingRectangle(VGroup(*cells[i]), color=YELLOW, buff=0.12,
                                                 corner_radius=0.08, stroke_width=3)
        b0, b1 = row_box(0), row_box(1)
        with self.narrate("Always Defect's row: two wins, two ties, no losses. Tit for Tat's row: no "
                          "wins at all. Now total the points. Always Defect, eight hundred and eight: "
                          "last place. Tit for Tat, eighteen ninety nine: more than double.") as beat:
            self.play(Create(b0), run_time=0.8)
            self.play(LaggedStart(*[flag(c[1]) for c in cells[0]], lag_ratio=0.25),
                      run_time=beat.until("Tit for Tat", offset=-0.2))
            self.play(ReplacementTransform(b0, b1), run_time=0.8)
            self.play(LaggedStart(*[flag(c[1]) for c in cells[1]], lag_ratio=0.25),
                      run_time=beat.until("Now", offset=-0.1))
            self.play(FadeOut(b1), FadeIn(tot_head), FadeIn(tots), run_time=0.6)
            self.play(*[t.animate.set_value(v) for t, v in zip(trackers, TOTALS)],
                      run_time=beat.until("eight hundred", offset=-0.4))
            self.play(FadeIn(rank_lbls), rank_lbls[0].animate.set_color(YELLOW), flag(tots[0]),
                      run_time=beat.until("last", offset=0.0))
            self.play(Circumscribe(VGroup(tots[0], rank_lbls[0]), color=YELLOW, buff=0.1), run_time=1.0)
            beat.wait_until("eighteen", offset=-0.2)
            self.play(rank_lbls[1].animate.set_color(YELLOW), flag(tots[1]), run_time=0.9)
            self.play(Circumscribe(VGroup(tots[1], rank_lbls[1]), color=YELLOW, buff=0.1),
                      run_time=beat.remaining(0.6))

        # ============ 10. insight: every match is a pot ===========================
        base = {0: 1.45, 1: -0.55}
        bars = {}
        pot_lbls = {}
        for i in (0, 1):
            for j in range(4):
                a, b = SCORES[i][j]
                ya, yb = a / ROUNDS * K * 5, b / ROUNDS * K * 5
                x = COL_X[j]
                blue = Rectangle(width=BAR_W, height=ya, stroke_width=0, fill_color=BLUE, fill_opacity=0.95)
                blue.move_to([x, base[i], 0], aligned_edge=DOWN)
                gray = Rectangle(width=BAR_W, height=yb, stroke_width=0, fill_color=GRAY, fill_opacity=0.55)
                gray.next_to(blue, UP, buff=0)
                bars[(i, j)] = VGroup(blue, gray)
                pot = (a + b) / ROUNDS
                pl = MathTex(f"{pot:.0f}", font_size=34, color=INK).next_to(gray, UP, buff=0.12)
                pot_lbls[(i, j)] = pl
        pot_head = text("pot per round", size=26, color=GRAY).move_to([LABEL_RIGHT - 1.25, HEAD_Y, 0])
        with self.narrate("So redraw each match as a pot: everything both programs scored, with the "
                          "row program's piece in blue. Always Defect holds at least half of every pot, "
                          "but its pots are tiny, about two points a round. Tit for Tat's reach "
                          "six.") as beat:
            self.play(FadeOut(VGroup(*[c for c in cells[2] + cells[3]], rlabels[2:], tots, rank_lbls,
                                     tot_head)), run_time=0.8)
            self.play(rlabels[0].animate.move_to([rlabels[0].get_x(), base[0] + 0.5, 0]),
                      rlabels[1].animate.move_to([rlabels[1].get_x(), base[1] + 0.6, 0]),
                      *[ReplacementTransform(cells[i][j][0], bars[(i, j)][0]) for i in (0, 1) for j in range(4)],
                      *[FadeOut(cells[i][j][1]) for i in (0, 1) for j in range(4)],
                      run_time=beat.until("everything", offset=-0.1))
            self.play(*[GrowFromEdge(bars[(i, j)][1], DOWN) for i in (0, 1) for j in range(4)],
                      FadeIn(pot_head), run_time=beat.until("Always", offset=-0.1))
            halves0 = VGroup(*[Line(bars[(0, j)].get_left() + LEFT * 0.08, bars[(0, j)].get_right() + RIGHT * 0.08,
                                    color=YELLOW, stroke_width=3).move_to(bars[(0, j)].get_center())
                               for j in range(4)])
            self.play(LaggedStart(*[Indicate(bars[(0, j)][0], color=BLUE, scale_factor=1.15) for j in range(4)],
                                  lag_ratio=0.2), run_time=beat.until("tiny", offset=-0.1))
            self.play(LaggedStart(*[FadeIn(pot_lbls[(0, j)], shift=0.1 * UP) for j in range(4)], lag_ratio=0.15),
                      run_time=beat.until("Tit for Tat", offset=-0.1))
            self.play(LaggedStart(*[FadeIn(pot_lbls[(1, j)], shift=0.1 * UP) for j in range(4)], lag_ratio=0.15),
                      run_time=beat.until("six", offset=-0.2))
            self.play(flag(pot_lbls[(1, 1)]), flag(pot_lbls[(1, 2)]), run_time=0.8)

        # ============ 11. score = share x pot =====================================
        f1 = formula(r"\text{score}", "=", r"\text{share}", r"\times", r"\text{pot}", size=EQ)
        f1.move_to([0, -1.55, 0])
        f1[0].set_color(BLUE)
        f1[2].set_color(BLUE)
        ref = bars[(1, 2)]
        with self.narrate("Your score is your share, times the pot.") as beat:
            self.play(TransformFromCopy(ref[0], f1[0]), run_time=beat.until("is", offset=-0.05))
            self.play(Write(f1[1]), TransformFromCopy(ref[0], f1[2]), run_time=beat.until("times", offset=-0.1))
            self.play(Write(f1[3]), TransformFromCopy(ref, f1[4]), run_time=beat.remaining(0.9))

        # ============ 12. prediction: what bounds Tit for Tat's share =============
        halves1 = VGroup(*[Line(bars[(1, j)].get_left() + LEFT * 0.08, bars[(1, j)].get_right() + RIGHT * 0.08,
                                color=YELLOW, stroke_width=3).move_to(bars[(1, j)].get_center())
                           for j in range(4)])
        ge = MathTex(r"\text{share}", r"\geq", r"\tfrac{1}{2}", font_size=40)
        ge[0].set_color(BLUE)
        ge[2].set_color(YELLOW)
        ge.move_to([TOT_X, base[0] + 0.3, 0])
        le = MathTex(r"\text{share}", r"\leq", r"?", font_size=40)
        le[0].set_color(BLUE)
        le[2].set_color(YELLOW)
        le.move_to([TOT_X, base[1] + 0.6, 0])
        with self.narrate("Always Defect's share never drops below one half. Tit for Tat never defects "
                          "first, so what can its share never rise above? [pause 1.5]") as beat:
            self.play(LaggedStart(*[Create(h) for h in halves0], lag_ratio=0.15),
                      run_time=beat.until("one half", offset=-0.2))
            self.play(TransformFromCopy(f1[2], ge[0]), Write(ge[1:]), run_time=1.0)
            beat.wait_until("rise", offset=-0.4)
            self.play(LaggedStart(*[Create(h) for h in halves1], lag_ratio=0.15),
                      TransformFromCopy(f1[2], le[0]), Write(le[1:]), run_time=1.2)

        # ============ 13. the answer, and two instances ===========================
        half = MathTex(r"\tfrac{1}{2}", font_size=40, color=YELLOW).move_to(le[2], aligned_edge=LEFT)
        inst_t = formula(r"\tfrac{1}{2}", r"\times", "6", "=", "3", size=MATH)
        inst_a = formula(r"\tfrac{1}{2}", r"\times", "2", r"\approx", "1", size=MATH)
        for f in (inst_t, inst_a):
            f[0].set_color(BLUE)
            f[4].set_color(BLUE)
        nm_t = label("Tit for Tat", size=26, color=GRAY)
        nm_a = label("Always Defect", size=26, color=GRAY)
        VGroup(nm_t, inst_t).arrange(RIGHT, buff=0.35).move_to([-3.1, -2.55, 0])
        VGroup(nm_a, inst_a).arrange(RIGHT, buff=0.35).move_to([3.1, -2.55, 0])
        with self.narrate("One half. It cannot win a match. But half of six is three points a round, "
                          "while Always Defect's half of two is about one.") as beat:
            self.play(Transform(le[2], half), run_time=0.7)
            self.play(Circumscribe(le, color=YELLOW, buff=0.1), run_time=beat.until("But", offset=-0.1))
            self.play(FadeIn(nm_t), TransformFromCopy(half, inst_t[0]), Write(inst_t[1]),
                      TransformFromCopy(pot_lbls[(1, 2)], inst_t[2]), run_time=beat.until("is three", offset=-0.1))
            self.play(Write(inst_t[3:]), run_time=0.8)
            beat.wait_until("while", offset=-0.1)
            self.play(FadeIn(nm_a), TransformFromCopy(ge[2], inst_a[0]), Write(inst_a[1]),
                      TransformFromCopy(pot_lbls[(0, 1)], inst_a[2]), run_time=beat.until("about", offset=-0.1))
            self.play(Write(inst_a[3:]), run_time=0.8)

        # ============ 14. the tournament sums share x pot =========================
        f2 = MathTex(r"\text{total}", "=", r"\sum_{\text{opponents}}", r"\text{share}", r"\times",
                     r"\text{pot}", font_size=EQ)
        f2[0].set_color(BLUE)
        f2[3].set_color(BLUE)
        f2.move_to([0, -1.85, 0])
        with self.narrate("A tournament adds share times pot over every opponent. Winning a match "
                          "only maximizes the first factor.") as beat:
            self.play(FadeOut(VGroup(nm_t, inst_t, nm_a, inst_a)), run_time=0.6)
            self.play(TransformMatchingTex(f1, f2), run_time=beat.until("Winning", offset=-0.2))
            self.play(Create(box(f2[3])), flag(f2[3]), run_time=beat.until("first", offset=0.0))
            self.play(Indicate(ge, color=YELLOW, scale_factor=1.1), run_time=beat.remaining(0.8))

        # ============ 15. payoff: the real tournaments ============================
        self.fade_out_all(run_time=0.7)
        lad1 = self.ladder(15, x=-3.6, top=2.8, bottom=-2.5, length=1.3, labels=("1st", "15th"))
        lad1[0][0].set_color(YELLOW)
        tft_tag = MathTex(r"\text{Tit for Tat}", font_size=36, color=YELLOW)
        tft_tag.next_to(lad1[0][0], RIGHT, buff=0.3)
        avg = MathTex(r"504", r"\text{ points per match}", font_size=36)
        avg[0].set_color(BLUE)
        avg.next_to(tft_tag, DOWN, aligned_edge=LEFT, buff=0.18)
        top8 = lad1[0][:8]
        brace = Brace(top8, RIGHT, color=GREEN, buff=0.25).shift(RIGHT * 2.7)
        nice = VGroup(text("never", size=26, color=GREEN), text("defected first", size=26, color=GREEN))
        nice.arrange(DOWN, buff=0.08, aligned_edge=LEFT).next_to(brace, RIGHT, buff=0.15)
        lad2 = self.ladder(63, x=4.7, top=2.8, bottom=-2.5, length=1.3, labels=("1st", "63rd"))
        for s_ in lad2[0]:
            s_.set_stroke(width=2)
        lad2[0][0].set_color(YELLOW).set_stroke(width=5)
        again = text("1st again", size=28, color=YELLOW).next_to(lad2[0][0], UP, buff=0.12)
        cite1 = citation("Axelrod, 1980a, 1980b · Journal of Conflict Resolution")
        with self.narrate("Axelrod's real tournament agreed. Tit for Tat averaged five hundred and four "
                          "points per match, about two and a half a round, and the top eight finishers "
                          "never defected first. In a second tournament with over sixty entries, it won "
                          "again.") as beat:
            self.play(LaggedStart(*[Create(s) for s in lad1[0]], lag_ratio=0.06), FadeIn(lad1[1:]),
                      FadeIn(cite1), run_time=beat.until("Tit for Tat", offset=-0.1))
            self.play(Write(tft_tag), run_time=beat.until("five", offset=-0.1))
            self.play(FadeIn(avg, shift=0.1 * UP), run_time=beat.until("top eight", offset=-0.2))
            self.play(top8.animate.set_color(GREEN), GrowFromCenter(brace), run_time=0.9)
            self.play(FadeIn(nice), lad1[0][0].animate.set_color(YELLOW), run_time=beat.until("In a", offset=-0.1))
            self.play(LaggedStart(*[Create(s) for s in lad2[0]], lag_ratio=0.02), FadeIn(lad2[1:]),
                      run_time=beat.until("won", offset=-0.2))
            self.play(FadeIn(again, shift=0.1 * DOWN), flag(lad2[0][0]), run_time=beat.remaining(0.8))

        # ============ 16. honest limit: noise, and generosity =====================
        n = 13
        a_moves = "CCCD" + "CDCDCDCDC"
        b_moves = "CCCC" + "DCDCDCDCD"
        g_tft = "CCCD" + "CDCCCCCCC"
        g_gen = "CCCC" + "DCCCCCCCC"
        sx = -2.55
        ra = strip(a_moves, sx, 2.2)
        rb = strip(b_moves, sx, 1.6)
        rc = strip(g_tft, sx, -0.75)
        rd = strip(g_gen, sx, -1.35)
        la = row_label("Tit for Tat", 2.2, size=26).shift(RIGHT * 0.3)
        lb = row_label("Tit for Tat", 1.6, size=26).shift(RIGHT * 0.3)
        lc = row_label("Tit for Tat", -0.75, size=26).shift(RIGHT * 0.3)
        ld = row_label("Generous TFT", -1.35, size=26).shift(RIGHT * 0.3)
        slip = SurroundingRectangle(ra[3], color=YELLOW, buff=0.06, stroke_width=4)
        slip_t = label("slip", size=26, color=YELLOW).next_to(slip, UP, buff=0.12)
        slip2 = SurroundingRectangle(rc[3], color=YELLOW, buff=0.06, stroke_width=4)
        forgive = SurroundingRectangle(rd[6], color=YELLOW, buff=0.06, stroke_width=4)
        forgive_t = label("forgives", size=26, color=YELLOW).next_to(rd[6], DOWN, buff=0.18)
        pot_t = ValueTracker(6.0)
        pot_num = live_number(pot_t, 1, size=52, color=INK)
        pot_cap = VGroup(text("pot per round", size=26, color=GRAY),
                         text("long noisy match", size=22, color=GRAY))
        pot_cap.arrange(DOWN, buff=0.08)
        pot_box = VGroup(pot_num, pot_cap).arrange(DOWN, buff=0.2).move_to([5.0, 1.9, 0])
        pot_num.number.add_updater(lambda m: m.move_to([5.0, m.get_y(), 0]))
        cite2 = citation("Axelrod, 2012 · J. Theoretical Biology (Molander, 1985)")
        cite3 = citation("Nowak & Sigmund, 1992 · Nature")
        with self.narrate("Its win depends on the field, and its weakness is mistakes. One slip, and two "
                          "Tit for Tats echo it back and forth. Over a long, noisy match their pot falls "
                          "from six a round to about four and a half. Generous Tit for Tat, which "
                          "forgives about one defection in three, breaks the echo.") as beat:
            self.play(FadeOut(VGroup(lad2, again, brace, nice, avg, cite1)),
                      FadeOut(lad1), FadeOut(tft_tag), run_time=0.8)
            self.play(FadeIn(la), FadeIn(lb), LaggedStart(*[AnimationGroup(FadeIn(ra[i], scale=0.6),
                                                                          FadeIn(rb[i], scale=0.6))
                                                            for i in range(3)], lag_ratio=0.3),
                      run_time=beat.until("One slip", offset=-0.1))
            self.play(FadeIn(ra[3], scale=0.6), FadeIn(rb[3], scale=0.6), Create(slip), FadeIn(slip_t),
                      run_time=0.9)
            self.play(LaggedStart(*[AnimationGroup(FadeIn(ra[i], scale=0.6), FadeIn(rb[i], scale=0.6))
                                    for i in range(4, n)], lag_ratio=0.35), FadeIn(cite2),
                      run_time=beat.until("Over", offset=-0.1))
            self.play(FadeIn(pot_box), run_time=0.6)
            self.play(pot_t.animate.set_value(4.5), run_time=beat.until("Generous", offset=-0.1))
            self.play(FadeIn(lc), FadeIn(ld), FadeOut(cite2), FadeIn(cite3),
                      LaggedStart(*[AnimationGroup(FadeIn(rc[i], scale=0.6), FadeIn(rd[i], scale=0.6))
                                    for i in range(6)], lag_ratio=0.25), Create(slip2),
                      run_time=beat.until("forgives", offset=-0.1))
            self.play(FadeIn(rc[6], scale=0.6), FadeIn(rd[6], scale=0.6), Create(forgive), FadeIn(forgive_t),
                      run_time=0.9)
            self.play(LaggedStart(*[AnimationGroup(FadeIn(rc[i], scale=0.6), FadeIn(rd[i], scale=0.6))
                                    for i in range(7, n)], lag_ratio=0.3),
                      run_time=beat.remaining(1.0))

        # ============ 17. landing ===============================================
        pot_num.number.clear_updaters()
        card.scale(1 / 0.85).move_to([-3.0, 1.6, 0])
        lad.move_to([3.9 - lad.get_center()[0] + lad.get_center()[0], lad.get_y(), 0])
        land_bars = VGroup(*[bars[(1, j)].copy() for j in range(4)])
        land_bars.arrange(RIGHT, buff=0.4, aligned_edge=DOWN).move_to([-3.0, -1.9, 0])
        tft_pots = VGroup(*[pot_lbls[(1, j)].copy().next_to(land_bars[j], UP, buff=0.12) for j in range(4)])
        first2 = text("1st", size=32, color=YELLOW).next_to(lad[0][0], RIGHT, buff=0.3)
        lad[0][0].set_color(YELLOW)
        with self.narrate("Zero matches won, first place. Tit for Tat never took the bigger share of a "
                          "match. It won by making the matches bigger.") as beat:
            self.play(FadeOut(VGroup(ra, rb, rc, rd, la, lb, lc, ld, slip, slip_t, slip2, forgive, forgive_t,
                                     pot_box, cite3)), run_time=0.7)
            self.play(FadeIn(card), FadeIn(lad), run_time=beat.until("first", offset=-0.3))
            self.play(FadeIn(first2, shift=0.2 * LEFT), flag(card[2]), run_time=beat.until("never", offset=-0.1))
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in land_bars], lag_ratio=0.2),
                      run_time=beat.until("It won", offset=-0.1))
            self.play(LaggedStart(*[FadeIn(p, shift=0.1 * UP) for p in tft_pots], lag_ratio=0.2),
                      *[b.animate.set_opacity(1.0) for b in land_bars], run_time=beat.remaining(0.8))

        self.end_card()
