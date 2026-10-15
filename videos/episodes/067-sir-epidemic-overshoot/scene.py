"""Episode 67: Why Epidemics Overshoot Herd Immunity.

    videos/toolkit/render.sh videos/episodes/067-sir-epidemic-overshoot/scene.py Episode \
        videos/episodes/067-sir-epidemic-overshoot/final.mp4
"""
from manim import *
from sample_space import *
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

# ----------------------------------------------------------------------------- data
N = 400
R0 = 2.5
I0 = 1e-4                                   # seed (shown as one red dot)


def _rhs(t, y):
    s, i = y
    return [-R0 * s * i, R0 * s * i - i]


_sol = solve_ivp(_rhs, [0, 30], [1 - I0, I0], dense_output=True, rtol=1e-10, atol=1e-13,
                 max_step=0.01)
T_GRID = np.linspace(0, 30, 6001)
S_T, I_T = _sol.sol(T_GRID)
R_T = 1 - S_T - I_T
K_PEAK = int(np.argmax(I_T))
T_PEAK = T_GRID[K_PEAK]
T_END = float(T_GRID[np.argmax((T_GRID > T_PEAK) & (N * I_T < 0.3))])
X_T = 100 * (1 - S_T)                       # caught it so far (%)
Y_T = 100 * I_T                             # sick right now (%)
FINAL = 100 * (1 - S_T[-1])                 # 89.3


def final_size(r0):
    if r0 <= 1.0001:
        return 0.0
    return brentq(lambda z: 1 - z - np.exp(-r0 * z), 1e-9, 1 - 1e-12)


def state_at(t):
    """(ever infected, recovered) head counts at model time t."""
    s, i = _sol.sol(min(t, 30))
    e = max(1, int(round(N * (1 - s))))
    r = int(round(N * (1 - s - i)))
    return e, min(r, e)


# infection order: random (well-mixed), seed dot near the centre of the grid
_rng = np.random.default_rng(67)
ORDER = list(_rng.permutation(N))
SEED = 10 * 20 + 9
ORDER.remove(SEED)
ORDER = [SEED] + ORDER
RANK = np.empty(N, dtype=int)
RANK[ORDER] = np.arange(N)                  # RANK[dot] = position in infection order

E_PEAK, R_PEAK = state_at(T_PEAK)           # 240, 147 -> 93 sick
E_END, _ = state_at(30)                     # 357
REC_OPACITY = 0.38


class Episode(NarratedScene):
    EPISODE = 67
    TITLE = "Why Epidemics Overshoot Herd Immunity"
    SPEED = 0.82
    PRONUNCIATIONS = {"Kermack": "ker mack", "McKendrick": "mac kendrick",
                      "Trapman": "trap man"}

    # ------------------------------------------------------------------ grid helpers
    def make_grid(self):
        g = VGroup(*[Dot(radius=0.075, color=BLUE) for _ in range(N)])
        g.arrange_in_grid(rows=20, cols=20, buff=0.125)
        g.move_to([-4.2, 0.45, 0])
        return g

    @staticmethod
    def paint(dot, state):
        if state == "S":
            dot.set_fill(BLUE, opacity=1)
        elif state == "I":
            dot.set_fill(RED, opacity=1)
        elif state == "R":
            dot.set_fill(GRAY, opacity=REC_OPACITY)
        elif state == "O":
            dot.set_fill(PURPLE, opacity=1)
        dot.set_stroke(width=0)

    def paint_state(self, grid, e, r):
        for d in range(N):
            k = RANK[d]
            self.paint(grid[d], "R" if k < r else ("I" if k < e else "S"))

    def state_target(self, grid, e, r):
        tgt = grid.copy()
        self.paint_state(tgt, e, r)
        return tgt

    # ------------------------------------------------------------------ construct
    def construct(self):
        grid = self.make_grid()
        ax = axes((0, 100), (0, 30), x_length=6.0, y_length=3.7,
                  x_ticks=[0, 20, 40, 60, 80, 100], y_ticks=[0, 10, 20, 30],
                  x_label="caught it so far (%)", y_label="sick right now (%)")
        ax.move_to([2.95, -0.35, 0], aligned_edge=ORIGIN)
        ax.shift(np.array([2.95, -0.2, 0]) - ax.c2p(50, 15))

        def P(x, y):
            return ax.c2p(x, y)

        # ============================================================ 1. cold open
        r0_lbl = formula(r"R_0", "=", r"2.5", size=MATH).next_to(grid, UP, buff=0.3)
        r0_lbl[0].set_color(INK)
        hit_word = text("herd immunity threshold", size=BODY, color=INK)
        hit_num = formula(r"60\%", size=72, color=YELLOW)
        q_word = text("caught it by the end:", size=BODY, color=INK)
        q_mark = formula(r"?", size=72, color=INK)
        right = VGroup(VGroup(hit_word, hit_num).arrange(DOWN, buff=0.3),
                       VGroup(q_word, q_mark).arrange(DOWN, buff=0.3)).arrange(DOWN, buff=0.8)
        right.move_to([2.95, 0.3, 0])

        with self.narrate("Four hundred people, and nobody is immune. Each case of a new "
                          "virus passes it to two and a half others, so the textbook herd "
                          "immunity threshold is sixty percent. Leave the outbreak alone. "
                          "When it burns out, how many of the four hundred will have caught "
                          "it? [pause 1.6]") as beat:
            self.play(LaggedStart(*[FadeIn(row, scale=0.6) for row in
                                    [grid[i * 20:(i + 1) * 20] for i in range(20)]],
                                  lag_ratio=0.12), run_time=beat.until("Each"))
            self.play(grid[SEED].animate.set_fill(RED).scale(1.6), run_time=0.6)
            self.play(grid[SEED].animate.scale(1 / 1.6), run_time=0.4)
            beat.wait_until("two and a half", offset=-0.15)
            self.play(Write(r0_lbl), run_time=0.9)
            beat.wait_until("herd", offset=-0.1)
            self.play(FadeIn(hit_word, shift=0.15 * UP), run_time=0.7)
            beat.wait_until("sixty", offset=-0.1)
            self.play(Write(hit_num), run_time=0.7)
            beat.wait_until("how many", offset=-0.1)
            self.play(FadeIn(q_word, shift=0.15 * UP), run_time=0.7)
            self.play(Write(q_mark), run_time=0.6)
            self.play(flag(q_mark, color=YELLOW), run_time=0.9)

        # ============================================================ 2. stakes
        per = text("1 dot = 1 person", size=LABEL, color=GRAY).next_to(grid, DOWN, buff=0.3)
        per2 = text("country of 60 million: 1 dot = 150,000", size=LABEL, color=GRAY)
        per2.next_to(grid, DOWN, buff=0.3)
        fit(per2, width=4.6)
        per2.move_to([grid.get_center()[0], per2.get_center()[1], 0])
        with self.narrate("Each dot is a person. In a country of sixty million, each dot "
                          "would be a hundred and fifty thousand.") as beat:
            self.play(FadeIn(per, shift=0.1 * UP), run_time=0.8)
            beat.wait_until("country", offset=-0.1)
            self.play(ReplacementTransform(per, per2), run_time=1.0)
            self.play(Indicate(grid, color=BLUE, scale_factor=1.03), run_time=1.0)

        # ============================================================ 3. axes
        hit_line = DashedLine(P(60, 0), P(60, 30), color=YELLOW, stroke_width=3,
                              dash_length=0.12)
        hit_tag = formula(r"60\%", size=MATH_SMALL + 6, color=YELLOW).next_to(hit_line, UP, buff=0.12)
        answer = formula(r"\text{caught it by the end: }", r"?", size=MATH, color=INK)
        answer.next_to(grid, DOWN, buff=0.3)
        with self.narrate("Track two numbers. Across, the share who have ever caught it. "
                          "Up, the share who are sick right now.") as beat:
            self.play(FadeOut(hit_word), FadeOut(q_word), FadeOut(per2),
                      ReplacementTransform(q_mark, answer[1]),
                      FadeIn(answer[0]), run_time=1.0)
            self.play(Create(VGroup(ax.x_axis, ax.y_axis)), FadeIn(ax.x_title, ax.y_title),
                      run_time=beat.until("Across", offset=-0.1))
            self.play(flag(ax.x_title), run_time=0.8)
            beat.wait_until("Up", offset=-0.1)
            self.play(flag(ax.y_title), run_time=0.8)
            self.play(ReplacementTransform(hit_num, hit_tag), Create(hit_line),
                      run_time=beat.remaining(min_time=1.0))

        # ============================================================ 4. naive model
        # step diagram (per new case), schematic scale
        u = 1.0
        p0 = np.array([4.05, -1.45, 0])
        step_title = text("per new case", size=LABEL, color=GRAY)
        a_right = Arrow(p0, p0 + u * RIGHT, buff=0, color=INK, stroke_width=5,
                        max_tip_length_to_length_ratio=0.22)
        a_up = Arrow(p0 + u * RIGHT, p0 + u * RIGHT + u * UP, buff=0, color=RED, stroke_width=5,
                     max_tip_length_to_length_ratio=0.22)
        S_tr = ValueTracker(1.0)

        def down_len():
            return u / (R0 * S_tr.get_value())

        a_down = always_redraw(lambda: Arrow(
            p0 + u * RIGHT + u * UP + 0.22 * RIGHT,
            p0 + u * RIGHT + u * UP + 0.22 * RIGHT + down_len() * DOWN, buff=0,
            color=GRAY, stroke_width=5, max_tip_length_to_length_ratio=min(0.22, 0.09 / down_len())))
        l_right = formula(r"+1", size=36, color=INK).next_to(a_right, DOWN, buff=0.12)
        l_up = formula(r"+1", size=36, color=RED).next_to(a_up, LEFT, buff=0.12)
        l_down = formula(r"-0.4", size=36, color=GRAY)
        l_down.add_updater(lambda m: m.next_to(a_down, RIGHT, buff=0.12))
        step_title.next_to(VGroup(a_right, a_up), UP, buff=0.35).align_to(a_right, LEFT)
        step_title.shift(0.0 * LEFT)
        net = always_redraw(lambda: DashedLine(
            p0, p0 + u * RIGHT + (u - down_len()) * UP, color=INK, stroke_width=3,
            dash_length=0.08))
        naive_line = Line(P(0, 0), P(50, 30), color=INK, stroke_width=4)
        naive_tip = Triangle(color=INK, fill_opacity=1, stroke_width=0).scale(0.09)
        naive_tip.rotate(naive_line.get_angle() - PI / 2).move_to(P(50, 30))
        naive_tag = formula(r"\text{never stops: }100\%", size=36, color=INK)
        naive_tag.next_to(P(41, 25), LEFT, buff=0.3)

        with self.narrate("The simplest model never asks who is left. Each new case is one "
                          "step right, and one step up. Every case recovers after infecting "
                          "two and a half others, so each new case brings zero point four "
                          "of a recovery.") as beat:
            beat.wait_until("one step right", offset=-0.15)
            self.play(FadeIn(step_title), GrowArrow(a_right), FadeIn(l_right), run_time=0.8)
            beat.wait_until("one step up", offset=-0.15)
            self.play(GrowArrow(a_up), FadeIn(l_up), run_time=0.8)
            beat.wait_until("zero point four", offset=-0.2)
            self.play(FadeIn(a_down), FadeIn(l_down), run_time=0.8)
        with self.narrate("Up one, down point four: a straight line that climbs forever. It "
                          "predicts everyone catches it, because it never runs out of "
                          "people.") as beat:
            self.play(Create(net), run_time=beat.until("straight", offset=-0.1))
            self.play(Create(naive_line), run_time=beat.until("forever", offset=0.2))
            self.play(FadeIn(naive_tip, scale=0.5), run_time=0.4)
            beat.wait_until("everyone", offset=-0.1)
            self.play(Write(naive_tag), run_time=1.0)
            beat.wait_until("runs out", offset=-0.1)
            self.play(flag(grid, color=BLUE), run_time=1.0)

        # ============================================================ 5. depletion
        mid = self.state_target(grid, E_PEAK, R_PEAK)
        # two sick dots, five contacts: two susceptible, three immune
        def kind(d):
            k = RANK[d]
            return "R" if k < R_PEAK else ("I" if k < E_PEAK else "S")

        def nbrs(d, rad=3):
            r, c = divmod(d, 20)
            out = []
            for dr in range(-rad, rad + 1):
                for dc in range(-rad, rad + 1):
                    rr, cc = r + dr, c + dc
                    if (dr or dc) and 0 <= rr < 20 and 0 <= cc < 20:
                        out.append((dr * dr + dc * dc, rr * 20 + cc))
            return [d2 for _, d2 in sorted(out)]

        sick_mid = [d for d in range(N) if kind(d) == "I"]
        best = None
        for a in sick_mid:
            r, c = divmod(a, 20)
            if not (5 <= r <= 14 and 4 <= c <= 15):
                continue
            for b in sick_mid:
                if b <= a or abs(divmod(b, 20)[0] - r) > 4 or abs(divmod(b, 20)[1] - c) > 5 \
                        or abs(divmod(b, 20)[1] - c) < 3:
                    continue
                na = nbrs(a)
                nb = nbrs(b)
                sa = [d for d in na if kind(d) == "S"][:1]
                ra = [d for d in na if kind(d) == "R"][:2]
                sb = [d for d in nb if kind(d) == "S" and d not in sa][:1]
                rb = [d for d in nb if kind(d) == "R" and d not in ra][:1]
                if len(sa) == 1 and len(ra) == 2 and len(sb) == 1 and len(rb) == 1:
                    best = (a, b, sa + ra, sb + rb)
                    break
            if best:
                break
        a, b, ca, cb = best
        contacts = VGroup()
        targets = []
        for src, lst in ((a, ca), (b, cb)):
            for d in lst:
                ln = Line(mid[src].get_center(), mid[d].get_center(), color=INK, stroke_width=3,
                          buff=0.09)
                contacts.add(ln)
                targets.append((src, d, ln))
        ring = VGroup(*[Circle(radius=0.16, color=INK, stroke_width=3).move_to(mid[s].get_center())
                        for s in (a, b)])
        s_lbl = formula(r"S", "=", r"40\%", size=MATH, color=BLUE)
        s_lbl.next_to(grid, DOWN, buff=0.3)
        cnt = formula(r"2", r"\text{ sick} \to ", r"5", r"\text{ contacts} \to ", r"2",
                      r"\text{ new}", size=36)
        cnt[0].set_color(RED)
        cnt[4].set_color(BLUE)
        cnt.next_to(grid, UP, buff=0.3)
        fit(cnt, width=4.4)
        cnt.move_to([grid.get_center()[0], cnt.get_center()[1], 0])
        with self.narrate("Later, only forty percent are still susceptible. These two sick "
                          "people have five contacts. Two land on someone blue. The other "
                          "three are wasted on people already immune.") as beat:
            self.play(Transform(grid, mid), FadeOut(answer), run_time=1.6)
            self.play(FadeIn(s_lbl, shift=0.1 * UP), run_time=0.6)
            beat.wait_until("These", offset=-0.1)
            self.play(Create(ring), FadeOut(r0_lbl), FadeIn(cnt[0:2]), run_time=0.8)
            beat.wait_until("five", offset=-0.1)
            self.play(LaggedStart(*[Create(ln) for ln in contacts], lag_ratio=0.15),
                      FadeIn(cnt[2:4]), run_time=1.0)
            beat.wait_until("Two land", offset=-0.1)
            blue_t = [ln for (_, d, ln) in targets if kind(d) == "S"]
            self.play(*[ln.animate.set_color(BLUE).set_stroke(width=5) for ln in blue_t],
                      FadeIn(cnt[4:]), run_time=0.8)
            beat.wait_until("three", offset=-0.1)
            gray_t = [ln for (_, d, ln) in targets if kind(d) == "R"]
            self.play(*[ln.animate.set_stroke(color=GRAY, opacity=0.35) for ln in gray_t],
                      run_time=0.8)

        # cases per case = R0 * S  ->  recoveries per new case = 1 / (R0 S)
        eq1 = formula(r"\text{cases per case}", "=", r"R_0", r"S", size=EQ)
        eq1.move_to([2.95, 2.85, 0])
        eq1[3].set_color(BLUE)
        eq1b = formula(r"\text{cases per case}", "=", r"R_0", r"S", "=", r"2.5", r"\times",
                       r"0.4", "=", "1", size=EQ)
        eq1b.move_to(eq1)
        fit(eq1b, width=6.4)
        eq1b.move_to([2.95, 2.85, 0])
        eq1b[3].set_color(BLUE)
        eq1b[7].set_color(BLUE)
        l_down2 = formula(r"-\frac{1}{R_0 S}", size=36, color=GRAY)
        with self.narrate("So each case makes two point five times S new cases, and the "
                          "step down becomes one over that.") as beat:
            self.play(Write(eq1[0:2]), run_time=0.8)
            self.play(TransformFromCopy(cnt[2], eq1[2]), run_time=0.9)
            beat.wait_until("times S", offset=0.1)
            self.play(TransformFromCopy(s_lbl[0], eq1[3]), run_time=0.9)
            beat.wait_until("step down", offset=-0.1)
            l_down.clear_updaters()
            l_down2.next_to(a_down, RIGHT, buff=0.12)
            self.play(TransformFromCopy(eq1[2:4], l_down2), FadeOut(l_down), run_time=1.2)
            l_down2.add_updater(lambda m: m.next_to(a_down, RIGHT, buff=0.12))

        s_read = always_redraw(lambda: VGroup(
            MathTex(r"S =", font_size=36, color=BLUE),
            DecimalNumber(100 * S_tr.get_value(), num_decimal_places=0, font_size=36,
                          color=BLUE, unit=r"\%")).arrange(RIGHT, buff=0.15)
            .next_to(step_title, RIGHT, buff=0.35).align_to(step_title, DOWN))
        eq2 = formula(r"S", "=", r"\frac{1}{R_0}", size=EQ).move_to(eq1)
        eq2[0].set_color(BLUE)
        eq3 = formula(r"1-", r"\frac{1}{R_0}", "=", r"60\%", size=EQ, color=YELLOW).move_to(eq1)
        with self.narrate("As S shrinks, the step down grows. At forty percent it matches "
                          "the step up, and the curve goes flat, with sixty percent infected. "
                          "That is the herd immunity threshold, one minus one over R "
                          "nought.") as beat:
            self.play(FadeIn(s_read), FadeOut(contacts), FadeOut(ring), run_time=0.6)
            self.play(S_tr.animate.set_value(0.4), run_time=beat.until("matches", offset=0.3),
                      rate_func=SMOOTH)
            self.play(TransformMatchingTex(eq1, eq1b), run_time=1.2)
            beat.wait_until("flat", offset=-0.1)
            self.play(flag(net, color=YELLOW), run_time=0.8)
            beat.wait_until("sixty", offset=-0.1)
            self.play(flag(hit_tag), flag(hit_line), run_time=0.8)
            beat.wait_until("one minus", offset=-0.3)
            self.play(FadeOut(eq1b[4:]), TransformMatchingShapes(eq1b[:4], eq2), run_time=0.9)
            self.play(TransformMatchingTex(eq2, eq3), run_time=1.0)

        # ============================================================ 6. run it
        start = self.state_target(grid, 1, 0)
        t_tr = ValueTracker(0.0)
        n_pts = len(T_GRID)

        def tip_index():
            return max(2, int(np.searchsorted(T_GRID, t_tr.get_value())))

        pts_all = np.array([P(x, y) for x, y in zip(X_T, Y_T)])
        curve = VMobject(color=INK, stroke_width=5)

        def upd_curve(m):
            k = tip_index()
            m.set_points_as_corners(pts_all[:k:4] if k > 8 else pts_all[:k])
        curve.add_updater(upd_curve)
        head = Dot(radius=0.09, color=INK)
        head.add_updater(lambda m: m.move_to(pts_all[min(tip_index(), n_pts - 1)]))

        def upd_grid(m):
            e, r = state_at(t_tr.get_value())
            for d in range(N):
                k = RANK[d]
                st = "R" if k < r else ("I" if k < e else "S")
                col = {"S": BLUE, "I": RED, "R": GRAY}[st]
                op = REC_OPACITY if st == "R" else 1.0
                m[d].set_fill(col, opacity=op)

        caught = ValueTracker(0.0)
        cnt_lbl = live_number(caught, 0, size=MATH, prefix=r"\text{caught it: }", suffix=r"\%")
        cnt_lbl.next_to(grid, DOWN, buff=0.3)
        with self.narrate("Flat sounds like finished. Run it.") as beat:
            self.play(FadeOut(VGroup(step_title, a_right, a_up, l_right, l_up)),
                      FadeOut(s_read), FadeOut(net), FadeOut(a_down), FadeOut(l_down2),
                      FadeOut(cnt), FadeOut(s_lbl), dim(naive_line, naive_tip, naive_tag),
                      run_time=0.9)
            eq3s = eq3.copy().scale(0.75).move_to([4.6, 2.95, 0])
            self.play(Transform(grid, start), Transform(eq3, eq3s), FadeIn(cnt_lbl),
                      FadeIn(r0_lbl), run_time=beat.remaining(min_time=0.9))
        self.add(curve, head)
        grid.add_updater(upd_grid)
        caught.add_updater(lambda m: m.set_value(X_T[min(tip_index(), n_pts - 1)]))
        self.add(caught)
        land = Dot(P(FINAL, 0), radius=0.09, color=INK)
        land_tag = formula(r"89\%", size=36, color=INK).next_to(land, UP, buff=0.18)
        with self.narrate("The curve turns exactly at the sixty percent line, then keeps "
                          "going, and lands at eighty nine.") as beat:
            self.play(t_tr.animate.set_value(T_PEAK), run_time=beat.until("turns", offset=0.1),
                      rate_func=LINEAR)
            self.play(flag(hit_line), t_tr.animate.set_value(T_PEAK + 0.6), run_time=0.9,
                      rate_func=LINEAR)
            self.play(t_tr.animate.set_value(T_END), run_time=beat.until("eighty", offset=-0.2),
                      rate_func=rate_functions.ease_out_sine)
            self.play(FadeIn(land, scale=0.5), Write(land_tag), run_time=0.8)
        grid.clear_updaters()
        caught.clear_updaters()
        head.clear_updaters()
        curve.clear_updaters()
        self.remove(caught)
        cnt_final = formula(r"\text{caught it: }", r"89\%", size=MATH).move_to(cnt_lbl)
        self.remove(cnt_lbl)
        self.add(cnt_final)

        # overshoot: the part of the curve past the threshold
        post = VMobject(color=PURPLE, stroke_width=6)
        post.set_points_as_corners(pts_all[K_PEAK:np.searchsorted(T_GRID, T_END):4])
        over_bar = Line(P(60, 0), P(FINAL, 0), color=PURPLE, stroke_width=8)
        over_tag = formula(r"+29\text{ points}", size=36, color=PURPLE)
        over_tag.next_to(Line(P(60, 0), P(FINAL, 0)), UP, buff=0.2).shift(0.15 * LEFT)
        third = formula(r"\tfrac13", r"\text{ of all cases come after}", size=36, color=PURPLE)
        third.move_to([2.95, 2.1, 0])
        with self.narrate("The guess missed by twenty nine points. A third of all "
                          "infections come after the threshold.") as beat:
            self.play(Create(over_bar), FadeIn(over_tag, shift=0.1 * UP),
                      run_time=beat.until("twenty", offset=0.3))
            beat.wait_until("A third", offset=-0.1)
            self.play(Create(post), FadeIn(third, shift=0.1 * DOWN), run_time=1.2)

        # ============================================================ 7. why: momentum
        peak_pt = P(X_T[K_PEAK], Y_T[K_PEAK])
        peak_dot = Dot(peak_pt, radius=0.1, color=RED)
        sick_tag = formula(r"93\text{ sick now}", size=36, color=RED)
        sick_tag.next_to(peak_pt, LEFT, buff=0.35).shift(0.3 * UP)
        lt1 = formula(r"R_0", r"S", "<", "1", size=36, color=INK)
        lt1[1].set_color(BLUE)
        lt1.next_to(sick_tag, DOWN, buff=0.2).align_to(sick_tag, RIGHT)
        with self.narrate("At the peak, ninety three people are still sick. Each passes it on "
                          "to fewer than one person, but fewer than one is not zero.") as beat:
            self.play(FadeOut(third), head.animate.move_to(peak_pt), run_time=1.0)
            beat.wait_until("ninety", offset=-0.2)
            self.play(FadeIn(peak_dot, scale=0.5), Write(sick_tag),
                      Indicate(VGroup(*[grid[d] for d in range(N)
                                        if E_END > RANK[d] >= E_END]), scale_factor=1.0),
                      run_time=0.9)
            beat.wait_until("fewer", offset=-0.1)
            self.play(Write(lt1), run_time=0.9)
            beat.wait_until("not zero", offset=-0.1)
            self.play(flag(lt1[2:]), run_time=0.8)

        glide_arrow = Arrow(ORIGIN, 0.7 * RIGHT, buff=0, color=INK, stroke_width=5,
                            max_tip_length_to_length_ratio=0.3)
        glide_arrow.add_updater(lambda m: m.next_to(head, UP, buff=0.12))
        k_end = int(np.searchsorted(T_GRID, T_END))
        glide = ValueTracker(K_PEAK)
        with self.narrate("Every new case still moves the curve right. The threshold only "
                          "turns up into down. Only the floor stops it.") as beat:
            self.play(FadeIn(glide_arrow), run_time=0.5)
            head.add_updater(lambda m: m.move_to(pts_all[int(glide.get_value())]))
            self.play(glide.animate.set_value(k_end), run_time=beat.until("threshold", offset=0.3),
                      rate_func=SMOOTH)
            self.play(flag(hit_line), flag(hit_tag), run_time=0.9)
            beat.wait_until("floor", offset=-0.1)
            self.play(Indicate(land, color=YELLOW, scale_factor=1.6),
                      Indicate(ax.x_axis, color=INK, scale_factor=1.0), run_time=1.0)
            head.clear_updaters()
            glide_arrow.clear_updaters()
            self.play(FadeOut(glide_arrow), FadeOut(head), run_time=0.5)

        # ============================================================ 8. vary R0
        r_tr = ValueTracker(R0)

        def curve_pts(r0):
            z = final_size(r0)
            if z <= 0:
                return np.array([P(0, 0), P(0.6, 0)])
            xs = np.linspace(0, z, 160)
            ys = np.clip(xs + np.log(1 - xs) / r0, 0, None)
            return np.array([P(100 * x, 100 * y) for x, y in zip(xs, ys)])

        dyn_curve = always_redraw(lambda: VMobject(color=INK, stroke_width=5)
                                  .set_points_smoothly(curve_pts(r_tr.get_value())))

        def thr():
            return 100 * max(0.0, 1 - 1 / r_tr.get_value())

        dyn_line = always_redraw(lambda: DashedLine(P(thr(), 0), P(thr(), 30), color=YELLOW,
                                                    stroke_width=3, dash_length=0.12)
                                 .set_opacity(1 if r_tr.get_value() > 1.02 else 0))
        thr_num = DecimalNumber(60, num_decimal_places=0, font_size=36, color=YELLOW, unit=r"\%")
        thr_num.add_updater(lambda m: m.set_value(thr()).next_to(P(thr(), 30), UP, buff=0.12)
                            .set_opacity(1 if r_tr.get_value() > 1.02 else 0))
        land_dyn = always_redraw(lambda: Dot(P(100 * final_size(r_tr.get_value()), 0), radius=0.09,
                                             color=INK))
        land_num = DecimalNumber(89, num_decimal_places=0, font_size=36, color=INK, unit=r"\%")
        land_num.add_updater(lambda m: m.set_value(100 * final_size(r_tr.get_value()))
                             .next_to(P(100 * final_size(r_tr.get_value()), 0), UP, buff=0.18)
                             .set_opacity(1 if r_tr.get_value() > 1.02 else 0))
        r_read = VGroup(MathTex(r"R_0 =", font_size=EQ, color=INK),
                        DecimalNumber(2.5, num_decimal_places=1, font_size=EQ, color=INK))
        r_read.arrange(RIGHT, buff=0.18).move_to([1.6, 2.95, 0])
        r_read[1].add_updater(lambda m: m.set_value(r_tr.get_value())
                              .next_to(r_read[0], RIGHT, buff=0.18))
        with self.narrate("At R nought of one point five, it turns at thirty three percent "
                          "and lands at fifty eight. At four: seventy five, and ninety eight. "
                          "Below one, it never leaves the floor.") as beat:
            self.remove(curve, post, hit_line, hit_tag, land, land_tag)
            self.add(dyn_curve, dyn_line, thr_num, land_dyn, land_num)
            self.play(FadeOut(over_bar), FadeOut(over_tag), FadeOut(peak_dot), FadeOut(sick_tag),
                      FadeOut(lt1), FadeIn(r_read), dim(grid), run_time=0.8)
            self.play(r_tr.animate.set_value(1.5), run_time=beat.until("thirty", offset=-0.2),
                      rate_func=SMOOTH)
            beat.wait_until("four", offset=-0.2)
            self.play(r_tr.animate.set_value(4.0), run_time=beat.until("seventy", offset=-0.1),
                      rate_func=SMOOTH)
            beat.wait_until("Below", offset=-0.1)
            self.play(r_tr.animate.set_value(0.8), run_time=beat.until("floor", offset=0.2),
                      rate_func=SMOOTH)
            self.play(r_tr.animate.set_value(R0), run_time=beat.remaining(min_time=1.2),
                      rate_func=SMOOTH)
        for m in (thr_num, land_num, r_read[1]):
            m.clear_updaters()
        static_curve = dyn_curve.copy().clear_updaters()
        static_line = dyn_line.copy().clear_updaters()
        static_land = land_dyn.copy().clear_updaters()
        self.remove(dyn_curve, dyn_line, land_dyn)
        self.add(static_curve, static_line, static_land)

        # ============================================================ 9. payoff
        cite1 = citation("Kermack & McKendrick, 1927 · Proc. R. Soc. A")
        with self.narrate("This is the simplest form of Kermack and McKendrick's nineteen "
                          "twenty seven model, where everyone mixes evenly.") as beat:
            self.play(FadeOut(r_read), undim(grid), FadeOut(cnt_final), FadeIn(cite1),
                      run_time=1.0)
            beat.wait_until("everyone", offset=-0.1)
            self.play(Indicate(grid, color=INK, scale_factor=1.02), run_time=1.0)

        # contact heterogeneity: dot size = contacts (1/2x, 1x, 2x)
        act = np.array([1.0] * N)
        perm = np.random.default_rng(2020).permutation(N)
        act[perm[:100]] = 2.0
        act[perm[100:200]] = 0.5
        het = grid.copy()
        for d in range(N):
            het[d].scale(np.sqrt(act[d]) if act[d] != 1 else 1.0)
        key = VGroup(*[VGroup(Dot(radius=0.075 * np.sqrt(s), color=GRAY),
                              formula(lbl, size=36, color=GRAY)).arrange(RIGHT, buff=0.12)
                       for s, lbl in ((0.5, r"\tfrac12\times"), (1, r"1\times"), (2, r"2\times"))])
        key.arrange(RIGHT, buff=0.45)
        key_t = text("contacts", size=LABEL, color=GRAY)
        keyg = VGroup(key_t, key).arrange(RIGHT, buff=0.35).next_to(grid, DOWN, buff=0.3)
        keyg.move_to([grid.get_center()[0], keyg.get_center()[1], 0])
        line43 = DashedLine(P(43, 0), P(43, 30), color=YELLOW, stroke_width=3, dash_length=0.12)
        tag43 = formula(r"\approx 43\%", size=36, color=YELLOW).next_to(line43, UP, buff=0.12)
        cite2 = citation("Britton, Ball & Trapman, 2020 · Science")
        with self.narrate("In twenty twenty, Britton, Ball and Trapman gave R nought of two and "
                          "a half to a population where some people have four times the "
                          "contacts of others. The busiest catch it first, and the threshold "
                          "fell to about forty three percent. They call it an illustration, "
                          "not a forecast.") as beat:
            self.play(FadeOut(cite1), FadeIn(cite2), run_time=0.8)
            beat.wait_until("four times", offset=-0.2)
            self.play(Transform(grid, het), FadeIn(keyg), run_time=1.4)
            beat.wait_until("busiest", offset=-0.1)
            big = VGroup(*[grid[d] for d in perm[:100]])
            self.play(Indicate(big, color=RED, scale_factor=1.15), run_time=1.0)
            beat.wait_until("fell", offset=-0.1)
            ghost = static_line.copy()
            self.play(ReplacementTransform(ghost, line43), static_line.animate.set_opacity(0.3),
                      thr_num.animate.set_opacity(0.3), FadeIn(tag43),
                      run_time=1.4)
            beat.wait_until("illustration", offset=-0.1)
            self.play(Circumscribe(tag43, color=YELLOW, buff=0.1), run_time=1.2)

        # ============================================================ 10. landing
        # sort the 400: caught before the turn (240), after (117), never (43)
        end_grid = self.make_grid()
        pos = [end_grid[i].get_center() for i in range(N)]
        sorted_grid = grid.copy()
        for d in range(N):
            k = RANK[d]
            sorted_grid[d].become(Dot(pos[k], radius=0.075))
            if k < E_PEAK:
                self.paint(sorted_grid[d], "R")
            elif k < E_END:
                self.paint(sorted_grid[d], "O")
            else:
                self.paint(sorted_grid[d], "S")
        row_line = DashedLine(end_grid.get_left() + LEFT * 0.12, end_grid.get_right() + RIGHT * 0.12,
                              color=YELLOW, stroke_width=3, dash_length=0.1)
        row_line.move_to([end_grid.get_center()[0],
                          (pos[11 * 20][1] + pos[12 * 20][1]) / 2, 0])
        b240 = Brace(VGroup(*[sorted_grid[d] for d in range(N) if RANK[d] < E_PEAK]), RIGHT,
                     color=GRAY, buff=0.12)
        t240 = formula(r"240", size=36, color=INK).next_to(b240, RIGHT, buff=0.12)
        b117 = Brace(VGroup(*[sorted_grid[d] for d in range(N) if E_PEAK <= RANK[d] < E_END]),
                     RIGHT, color=PURPLE, buff=0.12)
        t117 = formula(r"117", size=36, color=PURPLE).next_to(b117, RIGHT, buff=0.12)
        with self.narrate("Back to the four hundred. These two hundred and forty caught it "
                          "before the turn. These hundred and seventeen caught it after herd "
                          "immunity had arrived. The threshold is where an epidemic starts to "
                          "shrink, not where it ends.") as beat:
            self.play(FadeOut(cite2), FadeOut(keyg), FadeOut(line43), FadeOut(tag43),
                      static_line.animate.set_opacity(1), thr_num.animate.set_opacity(1),
                      run_time=0.8)
            self.play(Transform(grid, sorted_grid), run_time=beat.until("These", offset=-0.1))
            self.play(GrowFromCenter(b240), FadeIn(t240), Create(row_line), run_time=0.8)
            beat.wait_until("hundred and seventeen", offset=-0.2)
            self.play(GrowFromCenter(b117), FadeIn(t117),
                      Indicate(VGroup(*[grid[d] for d in range(N) if E_PEAK <= RANK[d] < E_END]),
                               color=PURPLE, scale_factor=1.15), run_time=1.0)
            beat.wait_until("starts", offset=-0.1)
            self.play(flag(row_line), flag(static_line), run_time=0.9)
            beat.wait_until("ends", offset=-0.1)
            self.play(Indicate(static_land, color=PURPLE, scale_factor=1.6), run_time=0.9)

        self.end_card()
