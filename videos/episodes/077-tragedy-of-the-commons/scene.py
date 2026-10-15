"""Episode 077 - The Tragedy of the Commons Isn't Inevitable.

    videos/toolkit/render.sh --preview videos/episodes/077-tragedy-of-the-commons/scene.py Episode /tmp/e77.mp4
"""
import numpy as np
from manim import *
from sample_space import *

# ---------------------------------------------------------------- simulated model
# milk per cow = 20 L/day x grass left, grass left = 1 - cows/100 (see model_check.py)
def milk_per_cow(c):
    return max(0.0, 20 - 0.2 * c)


def village_milk(c):
    return c * milk_per_cow(c)


R = 2.0                      # pasture radius at scale 1
HOME = np.array([-3.7, 0.25, 0])
S_UNIT = 0.2                 # bar height per litre
BASE_Y = -1.3                # bar baseline
X_GAIN, X_HIS, X_DMG = 0.9, 2.15, 4.6
BAR_W = 0.85


def pool_positions(n=100):
    golden = np.pi * (3 - np.sqrt(5))
    pts = []
    for i in range(n):
        r = 0.88 * R * np.sqrt((i + 0.5) / n)
        th = i * golden
        pts.append([r * np.cos(th), r * np.sin(th), 0])
    order = np.random.default_rng(7).permutation(n)
    return np.array(pts)[order]


def herder_of(i):
    return i % 10


def bar(x, litres, color, width=BAR_W):
    h = max(litres * S_UNIT, 0.01)
    return Rectangle(width=width, height=h, stroke_width=0, fill_color=color,
                     fill_opacity=0.9).move_to([x, BASE_Y + h / 2, 0])


def sliced_bar(x, litres, color=RED, gap=0.0):
    h = litres * S_UNIT / 10
    g = VGroup()
    for k in range(10):
        r = Rectangle(width=BAR_W, height=h, stroke_width=0, fill_color=color, fill_opacity=0.9)
        r.move_to([x, BASE_Y + h / 2 + k * (h + gap), 0])
        g.add(r)
    return g


class Episode(NarratedScene):
    EPISODE = 77
    TITLE = "The Tragedy of the Commons Isn't Inevitable"
    PRONUNCIATIONS = {"Fehr": "fair", "Gächter": "gek ter"}

    # ------------------------------------------------------------ helpers
    def cows_to(self, n, recolor=None):
        """Animations that make cows [0, n) visible and the rest invisible."""
        anims = []
        for i, d in enumerate(self.cows):
            want = 1.0 if i < n else 0.0
            if abs(d.get_fill_opacity() - want) > 0.01 or (recolor and i in recolor):
                tgt = d.animate.set_fill(opacity=want)
                if recolor and i in recolor:
                    tgt = d.animate.set_fill(recolor[i], opacity=want)
                anims.append(tgt)
        return anims

    def construct(self):
        herd = ValueTracker(50)
        grass = ValueTracker(0.5)

        # ---------------------------------------------------------- pasture
        disc = Circle(radius=R, stroke_color=GREEN, stroke_width=4)
        disc.set_fill(GREEN, opacity=0.1 + 0.7 * grass.get_value())
        disc.add_updater(lambda m: m.set_fill(GREEN, opacity=0.1 + 0.7 * grass.get_value()))
        pos = pool_positions()
        self.cows = VGroup(*[Dot(p, radius=0.07, color=INK, fill_opacity=1.0 if i < 50 else 0.0)
                             for i, p in enumerate(pos)])
        pasture = VGroup(disc, self.cows).scale(1.2).move_to(DOWN * 0.15)

        place = text("Törbel, Swiss Alps", size=BODY).next_to(pasture, UP, buff=0.3)
        since = text("shared for 500+ years", size=LABEL, color=GRAY).next_to(pasture, DOWN, buff=0.3)

        # ================================================== 0 cold open
        with self.narrate("This pasture above Törbel, in the Swiss Alps, has been shared by a "
                          "whole village for more than five hundred years. A famous argument says "
                          "it should be bare dirt by now. What kept it green? Make a guess. "
                          "[pause 1.5]") as beat:
            self.add(disc)
            self.play(GrowFromCenter(disc), LaggedStart(*[FadeIn(c, scale=0.5) for c in self.cows[:50]],
                                                     lag_ratio=0.03), run_time=1.6)
            self.play(Write(place), run_time=beat.until("whole", offset=-0.6))
            self.play(FadeIn(since, shift=0.15 * UP), run_time=0.8)
            beat.wait_until("bare", offset=-0.3)
            self.play(grass.animate.set_value(0.0), run_time=1.2)
            beat.wait_until("green", offset=-0.5)
            self.play(grass.animate.set_value(0.5), run_time=0.9)
            beat.wait_until("guess", offset=0.4)
            ring = Circle(radius=R * 1.2 + 0.18, stroke_color=GRAY, stroke_width=3).move_to(disc)
            ring.rotate(PI / 2)
            self.play(Create(ring), run_time=beat.remaining() - 0.1, rate_func=LINEAR)
        self.remove(ring)

        # ================================================== 1 stakes: Hardin
        quote = VGroup(text("“Freedom in a commons", size=HEADING, slant=ITALIC),
                       text("brings ruin to all.”", size=HEADING, slant=ITALIC)).arrange(DOWN, buff=0.2)
        quote.move_to([2.9, 0.7, 0])
        who = text("Garrett Hardin, 1968", size=LABEL, color=GRAY).next_to(quote, DOWN, buff=0.4)
        cite_h = citation("Hardin, 1968 · Science 162:1243")
        with self.narrate("In nineteen sixty eight, Garrett Hardin argued in Science that anything "
                          "shared, from pastures to fisheries, gets used up. Freedom in a commons, "
                          "he wrote, brings ruin to all.") as beat:
            self.play(pasture.animate.scale(1 / 1.2).move_to(HOME), FadeOut(since),
                      place.animate.move_to(HOME + UP * (R + 0.5)), run_time=1.2)
            self.play(FadeIn(who, shift=0.1 * UP), FadeIn(cite_h), run_time=beat.until("Freedom", offset=-0.2))
            self.play(Write(quote[0]), run_time=beat.until("he wrote", offset=-0.1))
            self.play(Write(quote[1]), run_time=beat.until("ruin", offset=0.1))
            self.play(grass.animate.set_value(0.05), run_time=beat.remaining(0.6))
        # (grass returns when the model starts: it is a simulated pasture from here)

        # ================================================== 2 naive build
        sim_tag = text("simulated", size=SMALL, color=GRAY).move_to([-SAFE_X, SAFE_TOP, 0], aligned_edge=UL)
        herders = formula(r"10\ \text{herders}", r"\times", r"5\ \text{cows}", size=MATH)
        herders.move_to(place)
        rule = formula(r"\text{milk per cow}", "=", r"20", "-", r"0.2", r"\times", r"\text{cows}",
                       size=MATH)
        rule[0].set_color(BLUE)
        rule.move_to([2.9, 2.85, 0])
        with self.narrate("So build his pasture. Ten herders, five cows each. On fresh grass a cow "
                          "gives twenty litres of milk a day, but cows eat grass, so every added cow "
                          "cuts every cow's milk by a fifth of a litre.") as beat:
            self.play(FadeOut(quote), FadeOut(who), FadeOut(cite_h), FadeIn(sim_tag),
                      grass.animate.set_value(0.5), run_time=1.0)
            beat.wait_until("Ten", offset=-0.2)
            self.play(FadeTransform(place, herders), run_time=0.9)
            beat.wait_until("five", offset=-0.1)
            self.play(LaggedStart(*[Indicate(self.cows[i], color=YELLOW, scale_factor=1.6)
                                    for i in range(0, 50, 10)], lag_ratio=0.15), run_time=1.0)
            beat.wait_until("twenty", offset=-0.3)
            self.play(Write(rule[0:3]), run_time=beat.until("but", offset=-0.1))
            beat.wait_until("fifth", offset=-0.3)
            self.play(Write(rule[3:]), run_time=1.2)
            self.play(flag(rule[4]), run_time=0.8)

        # readouts under the pasture
        cows_ro = VGroup(formula(r"\text{cows} =", size=MATH),
                         DecimalNumber(50, num_decimal_places=0, font_size=MATH, color=INK))
        cows_ro.arrange(RIGHT, buff=0.15)
        cows_ro[1].add_updater(lambda m: m.set_value(herd.get_value()))
        grass_ro = VGroup(formula(r"\text{grass} =", size=MATH, color=GREEN),
                          DecimalNumber(50, num_decimal_places=0, font_size=MATH, color=GREEN),
                          formula(r"\%", size=MATH, color=GREEN))
        grass_ro.arrange(RIGHT, buff=0.12)

        def grass_upd(m):
            m.set_value(100 * grass.get_value())
            m.next_to(grass_ro[0], RIGHT, buff=0.12)
            grass_ro[2].next_to(m, RIGHT, buff=0.08)
        grass_ro[1].add_updater(grass_upd)
        readouts = VGroup(cows_ro, grass_ro).arrange(RIGHT, buff=0.7).move_to(HOME + DOWN * (R + 0.6))

        # chart
        ax = axes((0, 100), (0, 600), x_length=5.2, y_length=3.3, x_ticks=[0, 20, 40, 60, 80, 100],
                  y_ticks=[0, 200, 400, 600], x_label="cows on the pasture",
                  y_label="village milk (L/day)", x_decimals=0, y_decimals=0)
        ax.move_to([3.3, -0.55, 0])
        curve = ax.plot(village_milk, x_range=[0, 100, 0.5], color=BLUE, stroke_width=4)
        mdot = Dot(ax.c2p(50, 500), radius=0.1, color=BLUE, stroke_color=INK, stroke_width=2)
        mdot.add_updater(lambda m: m.move_to(ax.c2p(herd.get_value(), village_milk(herd.get_value()))))
        mval = DecimalNumber(500, num_decimal_places=0, font_size=MATH, color=BLUE)
        munit = formula(r"\text{L}", size=MATH, color=BLUE)
        mtag = VGroup(mval, munit)

        def mtag_upd(m):
            mval.set_value(village_milk(herd.get_value()))
            munit.next_to(mval, RIGHT, buff=0.1)
            m.next_to(mdot, UR, buff=0.1)
        mtag.add_updater(mtag_upd)

        # ================================================== 3 the curve
        with self.narrate("Plot the whole village's milk against the size of the herd. It peaks "
                          "right here: fifty cows, five hundred litres a day.") as beat:
            self.play(FadeIn(readouts, shift=0.1 * UP), Create(ax), run_time=1.6)
            self.play(Create(curve), run_time=beat.until("peaks", offset=-0.1))
            self.play(FadeIn(mdot, scale=0.5), run_time=0.5)
            beat.wait_until("fifty", offset=-0.2)
            vline = DashedLine(ax.c2p(50, 0), ax.c2p(50, 500), color=GRAY, stroke_width=2)
            self.play(Create(vline), FadeIn(mtag), run_time=1.0)
            self.play(flag(mtag), run_time=0.8)

        # ================================================== 4 fail: no rules
        with self.narrate("Now let each herder add a cow whenever it pays him. They stop at ninety "
                          "cows. The grass is down to a tenth, and the village gets a hundred and "
                          "eighty litres instead of five hundred.") as beat:
            self.play(FadeOut(vline), run_time=0.5)
            run = beat.until("ninety", offset=-0.1)
            self.play(herd.animate.set_value(90), grass.animate.set_value(0.1),
                      LaggedStart(*self.cows_to(90), lag_ratio=0.5), run_time=run, rate_func=SMOOTH)
            self.play(flag(cows_ro), run_time=0.8)
            beat.wait_until("tenth", offset=-0.3)
            self.play(flag(grass_ro), run_time=0.8)
            beat.wait_until("hundred", offset=-0.3)
            gap = DashedLine(ax.c2p(90, 180), ax.c2p(90, 500), color=RED, stroke_width=3)
            peak_mark = DashedLine(ax.c2p(50, 500), ax.c2p(90, 500), color=GRAY, stroke_width=2)
            self.play(Create(peak_mark), run_time=0.6)
            self.play(Create(gap), flag(mtag), run_time=1.0)
        lost = formula(r"-320\ \text{L}", size=MATH, color=RED).next_to(gap, LEFT, buff=0.15)

        # ================================================== 5 fix 1: goodwill
        saints = {i: PURPLE for i in range(50) if herder_of(i) in (1, 2, 3)}
        saint_lbl = formula(r"3\ \text{saints}", size=MATH, color=PURPLE).move_to(herders)
        saint_pay = formula(r"\text{saints: } 11\ \text{L}", size=MATH, color=PURPLE)
        other_pay = formula(r"\text{others: } 22\text{--}24\ \text{L}", size=MATH)
        pays = VGroup(saint_pay, other_pay).arrange(RIGHT, buff=0.6).move_to(readouts)
        with self.narrate("If you guessed trust, try it. Make three herders saints who never go past "
                          "five cows. The other seven fill the gap, and the herd settles at eighty "
                          "nine. The saints just earn half as much milk.") as beat:
            self.play(FadeOut(gap), FadeOut(peak_mark), herd.animate.set_value(50),
                      grass.animate.set_value(0.5), *self.cows_to(50), run_time=1.4)
            beat.wait_until("saints", offset=-0.3)
            self.play(FadeTransform(herders, saint_lbl), *self.cows_to(50, recolor=saints), run_time=1.0)
            beat.wait_until("seven", offset=-0.2)
            run = beat.until("eighty", offset=-0.1)
            self.play(herd.animate.set_value(89), grass.animate.set_value(0.11),
                      LaggedStart(*self.cows_to(89), lag_ratio=0.5), run_time=run, rate_func=SMOOTH)
            self.play(flag(cows_ro), run_time=0.8)
            beat.wait_until("saints", occurrence=2, offset=-0.3)
            self.play(FadeOut(readouts, shift=0.1 * DOWN), FadeIn(pays, shift=0.1 * UP), run_time=0.8)
            self.play(flag(saint_pay, color=PURPLE), run_time=0.8)

        # ================================================== 6 insight: one decision
        mine = [i for i in range(100) if herder_of(i) == 0]       # his cows: 0,10,...,90
        his_lbl = formula(r"\text{one herder: } 5 \text{ of } 50", size=MATH, color=YELLOW).move_to(herders)
        with self.narrate("Why does nobody stop? Rewind to fifty cows and watch this herder add "
                          "one more.") as beat:
            uncolor = {i: INK for i in saints}
            self.play(FadeOut(ax), FadeOut(curve), FadeOut(mdot), FadeOut(mtag), FadeOut(rule),
                      FadeOut(pays), FadeIn(readouts), run_time=0.8)
            self.play(herd.animate.set_value(50), grass.animate.set_value(0.5),
                      *self.cows_to(50, recolor=uncolor), FadeOut(saint_lbl),
                      run_time=beat.until("this", offset=-0.3))
            self.play(*[self.cows[i].animate.set_color(YELLOW).scale(1.3) for i in mine[:5]],
                      FadeIn(his_lbl), run_time=0.8)
            self.cows[50].set_fill(YELLOW).scale(1.3)
            self.play(herd.animate.set_value(51), self.cows[50].animate.set_fill(opacity=1),
                      Flash(self.cows[50], color=YELLOW, line_length=0.15), run_time=beat.remaining(0.8))

        # ================================================== 7 gain vs damage
        gain = bar(X_GAIN, 9.8, BLUE)
        dmg = sliced_bar(X_DMG, 10.0)
        gain_v = formula(r"9.8\ \text{L}", size=MATH, color=BLUE).next_to(gain, UP, buff=0.15)
        dmg_v = formula(r"10\ \text{L}", size=MATH, color=RED).next_to(dmg, UP, buff=0.15)
        gain_n = text("his gain", size=LABEL, color=BLUE).next_to(gain, DOWN, buff=0.2)
        dmg_n = text("damage to all", size=LABEL, color=RED).next_to(dmg, DOWN, buff=0.2)
        base = Line([X_GAIN - 0.8, BASE_Y, 0], [X_DMG + 0.8, BASE_Y, 0], color=GRAY, stroke_width=2)
        with self.narrate("The new cow gives him nine point eight litres. It also costs each of the "
                          "fifty cows a fifth of a litre, ten litres of damage. For the village, "
                          "this cow is a loss.") as beat:
            self.play(Create(base), run_time=0.6)
            self.play(TransformFromCopy(self.cows[50], gain), run_time=beat.until("nine", offset=-0.2))
            self.play(FadeIn(gain_v, shift=0.1 * UP), FadeIn(gain_n), run_time=0.8)
            beat.wait_until("costs", offset=-0.1)
            visible = [self.cows[i].copy() for i in range(50)]
            self.play(LaggedStart(*[ReplacementTransform(v, dmg[k // 5]) for k, v in enumerate(visible)],
                                  lag_ratio=0.03), run_time=beat.until("ten", offset=-0.1))
            self.play(FadeIn(dmg_v, shift=0.1 * UP), FadeIn(dmg_n), run_time=0.8)
            beat.wait_until("loss", offset=-0.4)
            cmp = formula(r"9.8 < 10", size=MATH, color=INK).move_to([(X_GAIN + X_DMG) / 2, 1.6, 0])
            self.play(TransformFromCopy(VGroup(gain_v, dmg_v), cmp), run_time=1.0)

        # ================================================== 8 his slice -> the formula
        eq = formula(r"\text{gain}", ">", r"\text{damage}", r"/", r"N", size=EQ)
        eq[0].set_color(BLUE)
        eq[2].set_color(RED)
        eq[4].set_color(YELLOW)
        eq.move_to([(X_GAIN + X_DMG) / 2 + 0.1, -2.25, 0])
        nums = formula(r"9.8", ">", r"10", r"/", r"10", size=MATH)
        nums[0].set_color(BLUE); nums[2].set_color(RED); nums[4].set_color(YELLOW)
        nums.next_to(eq, DOWN, buff=0.25)
        his_v = formula(r"1\ \text{L}", size=MATH, color=YELLOW)
        his_n = text("his share", size=LABEL, color=YELLOW)
        with self.narrate("But the damage is shared by ten herds, and only this one slice lands on "
                          "him. One litre. So he adds the cow whenever the gain beats the damage "
                          "over N.") as beat:
            self.play(FadeOut(cmp), run_time=0.5)
            spread = sliced_bar(X_DMG, 10.0, gap=0.06)
            self.play(Transform(dmg, spread), dmg_v.animate.next_to(spread, UP, buff=0.15),
                      run_time=beat.until("this", offset=-0.2))
            tgt = dmg[0].copy().set_fill(YELLOW).move_to([X_HIS, BASE_Y + dmg[0].height / 2, 0])
            self.play(dmg[0].animate.set_fill(YELLOW), run_time=0.4)
            self.play(Transform(dmg[0], tgt), run_time=beat.until("One", offset=-0.1))
            his_v.next_to(dmg[0], UP, buff=0.15)
            his_n.next_to(dmg[0], DOWN, buff=0.2)
            gain_n.next_to(gain, DOWN, buff=0.2)
            self.play(FadeIn(his_v, shift=0.1 * UP), FadeIn(his_n), run_time=0.7)
            beat.wait_until("gain", offset=-0.2)
            self.play(TransformFromCopy(gain_n, eq[0]), Write(eq[1]), run_time=beat.until("damage", offset=-0.1))
            self.play(TransformFromCopy(dmg_n, eq[2]), run_time=beat.until("over", offset=-0.1))
            self.play(Write(eq[3]), TransformFromCopy(dmg[0], eq[4]), run_time=0.9)
            self.play(TransformFromCopy(gain_v[0], nums[0]), Write(nums[1]),
                      TransformFromCopy(dmg_v[0], nums[2]), Write(nums[3]), Write(nums[4]),
                      run_time=1.0)

        # ================================================== 9 prediction pause
        gain90 = bar(X_GAIN, 1.8, BLUE)
        dmg90 = sliced_bar(X_DMG, 18.0, gap=0.06)
        his90 = dmg90[0].copy().set_fill(YELLOW).move_to([X_HIS, BASE_Y + dmg90[0].height / 2, 0])
        gain_v90 = formula(r"1.8\ \text{L}", size=MATH, color=BLUE).next_to(gain90, UP, buff=0.15)
        dmg_v90 = formula(r"18\ \text{L}", size=MATH, color=RED).next_to(dmg90, UP, buff=0.15)
        his_v90 = formula(r"1.8\ \text{L}", size=MATH, color=YELLOW).next_to(his90, UP, buff=0.15)
        nums90 = formula(r"1.8", "=", r"18", r"/", r"10", size=MATH).move_to(nums)
        nums90[0].set_color(BLUE); nums90[2].set_color(RED); nums90[4].set_color(YELLOW)
        his_lbl90 = formula(r"\text{one herder: } 9 \text{ of } 90", size=MATH, color=YELLOW).move_to(herders)
        with self.narrate("How big must the damage get before he stops? [pause 1.2] Ten times the "
                          "gain. At ninety cows, the next one gives one point eight litres and does "
                          "eighteen litres of damage.") as beat:
            self.play(flag(eq[2], color=RED), run_time=beat.until("stops", offset=-0.2))
            # planned prediction pause: the herd keeps creeping while the viewer thinks
            beat.wait_until("Ten", offset=-0.2)
            self.play(Indicate(eq[4], color=YELLOW), run_time=beat.until("ninety", offset=-0.2))
            for i in mine[5:9]:
                self.cows[i].set_fill(YELLOW).scale(1.3)
            self.play(herd.animate.set_value(90), grass.animate.set_value(0.1),
                      LaggedStart(*self.cows_to(90), lag_ratio=0.4),
                      FadeTransform(his_lbl, his_lbl90),
                      Transform(gain, gain90), Transform(gain_v, gain_v90),
                      Transform(dmg[1:], dmg90[1:]), Transform(dmg[0], his90),
                      Transform(dmg_v, dmg_v90), Transform(his_v, his_v90),
                      his_n.animate.next_to(his90, DOWN, buff=0.2),
                      gain_n.animate.next_to(gain90, DOWN, buff=0.2),
                      dmg_n.animate.next_to(dmg90, DOWN, buff=0.2),
                      run_time=beat.until("eighteen", offset=-0.2))
            self.play(TransformMatchingTex(nums, nums90), run_time=1.0)
        nums = nums90

        # ================================================== 10 fix 2: the fine
        gain50 = bar(X_GAIN, 9.8, BLUE)
        dmg50 = sliced_bar(X_DMG, 10.0, gap=0.06)
        h = dmg50[0].height
        his50 = dmg50[0].copy().set_fill(YELLOW).move_to([X_HIS, BASE_Y + h / 2, 0])
        stack = VGroup(*[dmg50[k].copy().set_fill(YELLOW).move_to([X_HIS, BASE_Y + h / 2 + k * (h + 0.06), 0])
                         for k in range(1, 10)])
        gain_v50 = formula(r"9.8\ \text{L}", size=MATH, color=BLUE).next_to(gain50, UP, buff=0.15)
        dmg_v50 = formula(r"10\ \text{L}", size=MATH, color=RED).next_to(dmg50, UP, buff=0.15)
        his_v50 = formula(r"1\ \text{L}", size=MATH, color=YELLOW).next_to(his50, UP, buff=0.15)
        nums50 = formula(r"9.8", ">", r"10", r"/", r"10", size=MATH).move_to(nums)
        nums50[0].set_color(BLUE); nums50[2].set_color(RED); nums50[4].set_color(YELLOW)
        eqf = formula(r"\text{gain}", ">", r"\text{damage}", r"/", r"N", "+", r"\text{fine}", size=EQ)
        eqf[0].set_color(BLUE); eqf[2].set_color(RED); eqf[4].set_color(YELLOW); eqf[6].set_color(YELLOW)
        eqf.move_to(eq)
        eqw = formula(r"\text{gain}", ">", r"\text{damage}", size=EQ).move_to(eq)
        eqw[0].set_color(BLUE); eqw[2].set_color(RED)
        his_tot = formula(r"1 + 9 = 10\ \text{L}", size=MATH, color=YELLOW)
        lose = formula(r"9.8", "<", r"10", size=MATH).move_to(nums)
        lose[0].set_color(BLUE); lose[2].set_color(YELLOW)
        fine_lbl = text("fine", size=LABEL, color=YELLOW)
        with self.narrate("So hand him back the other nine slices. Fine every cow over five by nine "
                          "litres. Now his rule is gain against the whole damage, and the fifty first "
                          "cow costs him money.") as beat:
            for i in mine[5:9]:
                self.cows[i].set_fill(INK).scale(1 / 1.3)
            self.play(herd.animate.set_value(51), grass.animate.set_value(0.49),
                      *self.cows_to(51), FadeTransform(his_lbl90, his_lbl),
                      Transform(gain, gain50), Transform(gain_v, gain_v50),
                      Transform(dmg[1:], dmg50[1:]), Transform(dmg[0], his50),
                      Transform(dmg_v, dmg_v50), Transform(his_v, his_v50),
                      his_n.animate.next_to(his50, DOWN, buff=0.2),
                      gain_n.animate.next_to(gain50, DOWN, buff=0.2),
                      dmg_n.animate.next_to(dmg50, DOWN, buff=0.2),
                      TransformMatchingTex(nums, nums50),
                      run_time=beat.until("nine", offset=-0.2))
            self.play(*[dmg[k].animate.set_fill(YELLOW) for k in range(1, 10)], run_time=0.5)
            self.play(LaggedStart(*[Transform(dmg[k], stack[k - 1]) for k in range(1, 10)], lag_ratio=0.12),
                      his_v.animate.next_to(stack, UP, buff=0.15).set_opacity(0),
                      FadeOut(dmg_v), run_time=beat.until("Fine", offset=-0.1))
            his_tot.next_to(stack, UP, buff=0.15)
            fine_lbl.next_to(stack[4], RIGHT, buff=0.2)
            self.play(FadeIn(his_tot, shift=0.1 * UP), FadeIn(fine_lbl), run_time=0.8)
            self.play(TransformMatchingTex(eq, eqf), run_time=beat.until("Now", offset=-0.1))
            self.play(flag(eqf[6]), run_time=0.8)
            beat.wait_until("whole", offset=-0.2)
            self.play(TransformMatchingTex(eqf, eqw), run_time=1.2)
            beat.wait_until("fifty first", offset=-0.2)
            self.play(TransformMatchingTex(nums50, lose), run_time=1.0)
            self.play(herd.animate.set_value(50), grass.animate.set_value(0.5),
                      self.cows[50].animate.set_fill(opacity=0), run_time=beat.remaining(0.8))
        eq = eqw

        # ================================================== 11 run again with the fine
        insight = VGroup(gain, gain_v, gain_n, dmg, his_n, his_tot, fine_lbl, base, lose)
        with self.narrate("Run the herders again from ninety cows, with the fine. They drop back to "
                          "fifty, the grass returns to half, and the village milk is back to five "
                          "hundred.") as beat:
            self.play(FadeOut(insight), eq.animate.scale(0.75).move_to([2.9, 2.85, 0]),
                      *[self.cows[i].animate.set_color(INK).scale(1 / 1.3) for i in mine[:5]],
                      FadeOut(his_lbl), run_time=0.9)
            fine_on = formula(r"10\ \text{herders} + \text{fine}", size=MATH)
            fine_on[0][-4:].set_color(YELLOW)
            fine_on.move_to(herders)
            self.play(FadeIn(ax), FadeIn(curve), FadeIn(fine_on), herd.animate.set_value(90),
                      grass.animate.set_value(0.1), *self.cows_to(90), run_time=1.0)
            self.add(mdot, mtag)
            self.play(FadeIn(mdot), FadeIn(mtag), run_time=beat.until("drop", offset=-0.2))
            self.play(herd.animate.set_value(50), *self.cows_to(50),
                      run_time=beat.until("grass", offset=-0.1), rate_func=SMOOTH)
            self.play(grass.animate.set_value(0.5), flag(grass_ro), run_time=beat.until("village", offset=-0.1))
            self.play(flag(mtag), run_time=0.9)

        # ================================================== 12 payoff: Törbel and Ostrom
        rule_q = VGroup(text("“No more cows on the alp", size=HEADING, slant=ITALIC),
                        text("than you can feed through winter.”", size=HEADING, slant=ITALIC))
        rule_q.arrange(DOWN, buff=0.2).move_to([2.9, 1.0, 0])
        fit(rule_q, width=6.4)
        fine_eq = formula(r"\text{gain}", ">", r"\text{damage}", r"/", r"N", "+", r"\text{fine}", size=MATH)
        fine_eq[0].set_color(BLUE); fine_eq[2].set_color(RED); fine_eq[4].set_color(YELLOW)
        fine_eq[6].set_color(YELLOW)
        fine_eq.next_to(rule_q, DOWN, buff=0.6)
        official = text("+ fines from an elected official", size=LABEL, color=YELLOW).next_to(rule_q, DOWN, buff=0.45)
        cite_n = citation("Netting, 1981 · Balancing on an Alp, p. 61")
        torbel = text("Törbel, Swiss Alps", size=BODY).move_to(herders)
        ostrom = text("Elinor Ostrom", size=TITLE).move_to([2.9, 0.9, 0])
        nobel = text("Nobel Prize in economics, 2009", size=LABEL, color=GRAY).next_to(ostrom, DOWN, buff=0.3)
        book = text("Governing the Commons, 1990", size=LABEL, slant=ITALIC).next_to(nobel, DOWN, buff=0.3)
        cite_o = citation("Ostrom, 1990 · Governing the Commons · Cambridge UP")
        with self.narrate("That is Törbel's rule. No one may send more cows to the alp than he can "
                          "feed through the winter, and an elected official fines anyone who does. "
                          "Elinor Ostrom built Governing the Commons on cases like this, and in two "
                          "thousand nine became the first woman to win the Nobel Prize in "
                          "economics.") as beat:
            self.play(FadeOut(ax), FadeOut(curve), FadeOut(mdot), FadeOut(mtag), FadeOut(eq),
                      FadeOut(sim_tag), FadeOut(readouts), FadeTransform(fine_on, torbel), run_time=1.0)
            self.play(Write(rule_q[0]), FadeIn(cite_n), run_time=beat.until("than", offset=-0.1))
            self.play(Write(rule_q[1]), run_time=beat.until("elected", offset=-0.2))
            self.play(FadeIn(official, shift=0.1 * UP), run_time=0.8)
            beat.wait_until("Elinor", offset=-0.4)
            self.play(FadeOut(rule_q, shift=0.2 * UP), FadeOut(official, shift=0.2 * UP),
                      FadeOut(cite_n), FadeIn(ostrom, shift=0.2 * UP), FadeIn(cite_o), run_time=0.9)
            self.play(FadeIn(book, shift=0.1 * UP), run_time=beat.until("two", offset=-0.2))
            self.play(FadeIn(nobel, shift=0.1 * UP), run_time=beat.until("first", offset=-0.1))
            self.play(flag(nobel, color=INK), run_time=0.9)

        # ================================================== 13 payoff: Fehr & Gächter
        fg_ax = axes((-0.6, 1.6), (0, 20), x_length=4.2, y_length=3.6, x_ticks=[], y_ticks=[0, 10, 20],
                     y_label="tokens given (of 20)", y_decimals=0, numbers=True)
        fg_ax.move_to([3.0, -0.2, 0])
        b_no = Rectangle(width=1.2, height=3.2 / 20 * 3.6, stroke_width=0, fill_color=GRAY,
                         fill_opacity=0.9).move_to(fg_ax.c2p(0.1, 0), aligned_edge=DOWN)
        b_yes = Rectangle(width=1.2, height=18.2 / 20 * 3.6, stroke_width=0, fill_color=YELLOW,
                          fill_opacity=0.9).move_to(fg_ax.c2p(0.95, 0), aligned_edge=DOWN)
        v_no = formula(r"3.2", size=MATH, color=GRAY).next_to(b_no, UP, buff=0.15)
        v_yes = formula(r"18.2", size=MATH, color=YELLOW).next_to(b_yes, UP, buff=0.15)
        n_no = text("no fines", size=LABEL, color=GRAY).next_to(b_no, DOWN, buff=0.25)
        n_yes = text("fines allowed", size=LABEL, color=YELLOW).next_to(b_yes, DOWN, buff=0.25)
        groups = text("groups of 4, last round", size=LABEL, color=GRAY).next_to(fg_ax, UP, buff=0.25)
        groups.align_to(fg_ax, RIGHT)
        cite_f = citation("Fehr & Gächter, 2000 · American Economic Review 90:980")
        with self.narrate("Will ordinary people pay to fine a neighbour? Fehr and Gächter gave groups "
                          "of four a shared pot. By the last round, without fines, people put in "
                          "about three tokens out of twenty. With fines allowed, about "
                          "eighteen.") as beat:
            self.play(FadeOut(ostrom), FadeOut(book), FadeOut(nobel), FadeOut(cite_o),
                      pasture.animate.set_opacity(0.3), torbel.animate.set_opacity(0.3), run_time=0.9)
            self.play(Create(fg_ax), FadeIn(cite_f), run_time=beat.until("groups", offset=-0.2))
            self.play(FadeIn(groups), run_time=beat.until("without", offset=-0.2))
            self.play(GrowFromEdge(b_no, DOWN), FadeIn(n_no), run_time=beat.until("about", offset=-0.1))
            self.play(FadeIn(v_no, shift=0.1 * UP), run_time=0.6)
            beat.wait_until("With", offset=-0.2)
            self.play(GrowFromEdge(b_yes, DOWN), FadeIn(n_yes), run_time=beat.until("eighteen", offset=-0.1))
            self.play(FadeIn(v_yes, shift=0.1 * UP), run_time=0.7)
        # disc fill is driven by an updater; restore its opacity via the grass tracker
        # ================================================== 14 honest limit
        count = ValueTracker(0)
        cnt = VGroup(formula(r"\text{counted} =", size=MATH),
                     DecimalNumber(0, num_decimal_places=0, font_size=MATH))
        cnt.arrange(RIGHT, buff=0.15).move_to(readouts)
        cnt[1].add_updater(lambda m: m.set_value(count.get_value()))
        unknown = formula(r"\text{counted} = \ ?", size=MATH).move_to(cnt)
        with self.narrate("A fine only works if someone counts. Törbel counts every cow the day the "
                          "herd goes up the mountain. Where nobody can count, Hardin's arithmetic "
                          "comes back.") as beat:
            self.play(FadeOut(VGroup(fg_ax, b_no, b_yes, v_no, v_yes, n_no, n_yes, groups, cite_f)),
                      self.cows.animate.set_opacity(1), disc.animate.set_stroke(opacity=1),
                      torbel.animate.set_opacity(1), run_time=0.9)
            for i in range(50, 100):
                self.cows[i].set_fill(opacity=0)
            self.play(pasture.animate.move_to(ORIGIN + UP * 0.25), torbel.animate.move_to(UP * (R + 0.75)),
                      run_time=beat.until("counts", offset=-0.2))
            cnt.move_to(DOWN * (R + 0.35) + DOWN * 0.15)
            self.add(cnt)
            run = beat.until("Where", offset=-0.3)
            self.play(count.animate.set_value(50),
                      LaggedStart(*[Indicate(c, color=YELLOW, scale_factor=1.6) for c in self.cows[:50]],
                                  lag_ratio=0.2), run_time=run, rate_func=LINEAR)
            self.play(FadeTransform(cnt, unknown), run_time=0.6)
            self.play(grass.animate.set_value(0.08), *self.cows_to(90), run_time=beat.remaining(1.0))

        # ================================================== 15 landing
        land = formula(r"\text{gain}", ">", r"\text{damage}", r"/", r"N", "+", r"\text{fine}", size=EQ)
        land[0].set_color(BLUE); land[2].set_color(RED); land[4].set_color(YELLOW); land[6].set_color(YELLOW)
        land.move_to(DOWN * (R + 0.55))
        with self.narrate("So the guess that trust kept Törbel green is the one the model rules out. "
                          "What keeps it green is a counted herd, and a fine that hands each herder "
                          "back the nine slices the commons takes away.") as beat:
            self.play(grass.animate.set_value(0.5), *self.cows_to(50), FadeOut(unknown),
                      run_time=beat.until("What", offset=-0.2))
            self.play(Write(land), run_time=beat.until("fine", offset=-0.1))
            self.play(flag(land[6]), run_time=0.9)
            beat.wait_until("nine", offset=-0.2)
            self.play(Indicate(land[4], color=YELLOW), run_time=beat.remaining(0.9))
        self.end_card()
