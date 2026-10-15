"""Episode 18 - How Bayes Found a Plane at the Bottom of the Ocean.

    videos/toolkit/render.sh --preview videos/episodes/018-bayesian-search-af447/scene.py Episode /tmp/ep18.mp4
"""
import math

import numpy as np
from manim import *
from sample_space import *

# ----------------------------------------------------------------------------- data
# Simulated prior on a 40 NM circle (see facts.md): 0.5 uniform + 0.5 circular normal
# (sd 8 NM) about the last known position; rescaled so the listening zone holds 0.50.
R_NM, SD_NM, CELL_NM, HALF_W_NM = 40.0, 8.0, 40.0 / 15, 9.0
ROUTE_DEG = 60.0                      # bearing 30 deg true = 60 deg from east
D_EST = 0.77                          # Stone et al. 2014, sec. 4.3
WRECK_NM = (1.70, 5.15)               # east, north of LKP (BEA coordinates; facts.md #22)

_c = np.arange(-R_NM + CELL_NM / 2, R_NM, CELL_NM)
_X, _Y = np.meshgrid(_c, _c)
_IN = _X ** 2 + _Y ** 2 <= R_NM ** 2
CX, CY = _X[_IN], _Y[_IN]
_u = np.ones_like(CX) / len(CX)
_g = np.exp(-(CX ** 2 + CY ** 2) / (2 * SD_NM ** 2))
_g /= _g.sum()
PRIOR = 0.5 * _u + 0.5 * _g
_n = np.array([-math.sin(math.radians(ROUTE_DEG)), math.cos(math.radians(ROUTE_DEG))])
ZONE = np.abs(CX * _n[0] + CY * _n[1]) <= HALF_W_NM
_s = PRIOR[ZONE].sum()
PRIOR = np.where(ZONE, PRIOR * 0.5 / _s, PRIOR * 0.5 / (1 - _s))
P0 = float(PRIOR[ZONE].sum())         # = 0.50
PMAX = float(PRIOR.max())
POST = P0 * (1 - D_EST) / (1 - P0 * D_EST)   # 0.187
assert abs(P0 - 0.5) < 1e-9 and abs(POST - 0.187) < 0.001

# ----------------------------------------------------------------------------- layout
MC = np.array([-3.55, -0.05, 0.0])    # map centre (last known position)
RM = 2.55                             # map radius in units (40 NM)
K = RM / R_NM                         # units per NM
PX = 3.35                             # right-panel centre x


def nm(x, y):
    return MC + K * np.array([x, y, 0.0])


def p_zone(f):
    """Normalised zone probability when zone cells are multiplied by f."""
    return P0 * f / (P0 * f + 1 - P0)


class Episode(NarratedScene):
    EPISODE = 18
    TITLE = "How Bayes Found a Plane at the Bottom of the Ocean"
    PRONUNCIATIONS = {"Metron": "met tron"}

    # ------------------------------------------------------------------ map pieces
    def build_map(self):
        side = CELL_NM * K * 0.9
        self.cells = VGroup(*[
            Square(side, stroke_width=0, fill_color=BLUE, fill_opacity=0).move_to(nm(x, y))
            for x, y in zip(CX, CY)])
        self.f = ValueTracker(1.0)        # multiplier applied to zone cells
        self.a = ValueTracker(1.0)        # 0 = not yet rescaled, 1 = rescaled to sum 1
        self.paint()
        rim = Circle(RM, color=GRAY, stroke_width=2.5).move_to(MC)
        u = np.array([math.cos(math.radians(ROUTE_DEG)), math.sin(math.radians(ROUTE_DEG)), 0])
        route = DashedLine(MC - u * (RM + 0.35), MC + u * (RM + 0.35), color=GRAY,
                           stroke_width=2.5, dash_length=0.12)
        lkp = VGroup(Line(UL * 0.09, DR * 0.09), Line(UR * 0.09, DL * 0.09)).set_stroke(INK, 4)
        lkp.move_to(MC).set_z_index(3)
        route_lbl = label("route", size=26, color=GRAY).next_to(route.get_end(), RIGHT, buff=0.15)
        ang = math.radians(-45)
        edge = MC + RM * np.array([math.cos(ang), math.sin(ang), 0])
        radius = Line(MC, edge, color=GRAY, stroke_width=2)
        r_lbl = MathTex(r"40\ \text{NM}", font_size=36, color=GRAY).next_to(edge, DR, buff=0.12)
        rect = Rectangle(width=2 * (RM + 0.2), height=2 * HALF_W_NM * K).rotate(
            math.radians(ROUTE_DEG)).move_to(MC)
        zone = Intersection(rect, Circle(RM).move_to(MC), color=YELLOW, stroke_width=4,
                            fill_opacity=0)
        self.zone = zone
        self.rim, self.route, self.lkp, self.route_lbl = rim, route, lkp, route_lbl
        self.radius, self.r_lbl = radius, r_lbl
        key_cross = lkp.copy().set_z_index(0).move_to(ORIGIN)
        self.legend = VGroup(key_cross, label("last known position", size=26)).arrange(
            RIGHT, buff=0.2)
        self.legend.move_to([-6.3 + self.legend.width / 2, 3.25, 0])

    def paint(self):
        f, a = self.f.get_value(), self.a.get_value()
        mult = np.where(ZONE, f, 1.0)
        z = (PRIOR * mult).sum()
        p = PRIOR * mult / (a * z + (1 - a))
        op = np.clip(p / PMAX, 0, 1) ** 0.5
        for c, o in zip(self.cells, op):
            c.set_fill(opacity=float(o))

    def heat_updater(self):
        self.cells.add_updater(lambda m: self.paint())

    # ------------------------------------------------------------------ episode
    def construct(self):
        self.build_map()
        cells, zone = self.cells, self.zone

        # ============================== 1 cold open: the circle, the silent zone
        title = VGroup(MathTex(r"\text{AF}\,447", font_size=44),
                       label("· June 2009", size=30, color=GRAY)).arrange(RIGHT, buff=0.2)
        title.move_to([PX, 2.75, 0])
        day = ValueTracker(1)
        day_num = live_number(day, 0, size=48, color=YELLOW, prefix=r"\text{day}")
        day_num.move_to([PX, 1.2, 0])
        heard = MathTex(r"\text{beacons heard: } 0", font_size=40, color=YELLOW)
        heard.next_to(day_num, DOWN, buff=0.45)
        u = np.array([math.cos(math.radians(ROUTE_DEG)), math.sin(math.radians(ROUTE_DEG)), 0])
        nvec = np.array([-u[1], u[0], 0])
        ships = VGroup(*[Dot(MC - u * (RM - 0.05) + s * nvec * 0.35, radius=0.08, color=YELLOW)
                         for s in (-1, 1)]).set_z_index(4)
        with self.narrate("In June two thousand nine, Air France four four seven vanished "
                          "inside this circle of ocean. For thirty-one days, ships listened "
                          "along its route and heard nothing.") as beat:
            self.add(cells)
            self.play(FadeIn(cells), Create(self.rim), FadeIn(self.lkp), FadeIn(self.legend),
                      FadeIn(title), run_time=1.0)
            self.play(Create(self.route), FadeIn(self.route_lbl), run_time=beat.until("inside", offset=-0.1))
            self.play(Create(self.radius), FadeIn(self.r_lbl), self.rim.animate.set_stroke(INK, 4),
                      run_time=beat.until("For", offset=-0.1))
            self.play(self.rim.animate.set_stroke(GRAY, 2.5), Create(zone), FadeIn(ships),
                      FadeIn(day_num), run_time=beat.until("listened"))
            self.play(*[MoveAlongPath(s, Line(s.get_center(), s.get_center() + u * 2 * (RM - 0.05)))
                        for s in ships],
                      day.animate.set_value(31), run_time=beat.until("heard"), rate_func=LINEAR)
            self.play(FadeIn(heard, shift=0.1 * UP), FadeOut(ships), run_time=0.6)

        # ============================== 2 the prediction
        q = label("sonar next?", size=34).move_to([PX, 1.95, 0])
        opt_a = VGroup(Square(0.32, color=YELLOW, stroke_width=3), label("back into the zone", size=30))
        opt_b = VGroup(Square(0.32, color=GRAY, stroke_width=3), label("somewhere new", size=30))
        for o in (opt_a, opt_b):
            o.arrange(RIGHT, buff=0.25)
        opts = VGroup(opt_a, opt_b).arrange(DOWN, buff=0.45, aligned_edge=LEFT).move_to([PX, 0.35, 0])
        with self.narrate("Your next search uses sonar. Do you send it back into this zone, "
                          "or out where nobody has listened yet? [pause 1.5]") as beat:
            self.play(FadeOut(day_num), FadeOut(heard), FadeIn(q, shift=0.1 * DOWN), run_time=0.8)
            beat.wait_until("back", offset=-0.15)
            self.play(FadeIn(opt_a, shift=0.1 * RIGHT), zone.animate.set_stroke(width=7), run_time=0.7)
            self.play(zone.animate.set_stroke(width=4), run_time=0.5)
            beat.wait_until("out", offset=-0.15)
            self.play(FadeIn(opt_b, shift=0.1 * RIGHT), run_time=0.7)

        # ============================== 3 stakes + what the search actually did
        aboard = MathTex(r"228\ \text{aboard}", font_size=44).move_to([PX, 2.0, 0])
        # approximate sonar patches outside the zone (illustrative positions, facts.md)
        p09 = Rectangle(width=12 * K, height=9 * K, color=GRAY, stroke_width=3).move_to(nm(9, -20))
        p10 = Rectangle(width=16 * K, height=13 * K, color=GRAY, stroke_width=3).move_to(nm(-17, 12))
        nothing = VGroup(Square(0.3, color=GRAY, stroke_width=3),
                         label("sonar, 2009 and 2010: nothing", size=28, color=INK)).arrange(RIGHT, buff=0.25)
        nothing.move_to([PX, -1.65, 0])
        with self.narrate("Two hundred and twenty eight people were aboard, and the black boxes "
                          "held the only record of why. Most people pick somewhere new. In August, "
                          "the sonar went to a patch the ships had not covered, and found nothing. "
                          "A bigger sonar search the next spring found nothing either.") as beat:
            self.play(FadeOut(q), FadeIn(aboard, shift=0.1 * DOWN), run_time=0.8)
            beat.wait_until("Most", offset=-0.1)
            tick = Line(LEFT * 0.1 + UP * 0.02, ORIGIN + DOWN * 0.1, color=INK, stroke_width=4)
            tick2 = Line(ORIGIN + DOWN * 0.1, RIGHT * 0.16 + UP * 0.14, color=INK, stroke_width=4)
            check = VGroup(tick, tick2).move_to(opt_b[0])
            self.play(Create(check), opt_a.animate.set_opacity(0.3), run_time=0.8)
            beat.wait_until("August", offset=-0.1)
            self.play(Create(p09), run_time=beat.until("found nothing", offset=-0.1))
            self.play(FadeIn(nothing, shift=0.1 * UP), run_time=0.7)
            beat.wait_until("bigger", offset=-0.1)
            self.play(Create(p10), run_time=beat.until("found nothing", occurrence=2))
            self.play(flag(nothing), run_time=0.8)

        # ============================== 4 naive: treat the zone as cleared
        key = label("simulated · brighter = likelier", size=26, color=GRAY)
        key.next_to(self.legend, RIGHT, buff=0.6)
        readout_lbl = MathTex(r"P(\text{zone})", "=", font_size=48)
        zt = ValueTracker(P0)
        zval = DecimalNumber(P0, num_decimal_places=2, font_size=48, color=BLUE)
        readout = VGroup(readout_lbl, zval).arrange(RIGHT, buff=0.2).move_to([PX, 0.9, 0])
        zval.add_updater(lambda m: m.set_value(zt.get_value()))
        zval.add_updater(lambda m: m.next_to(readout_lbl, RIGHT, buff=0.2))
        with self.narrate("Picking somewhere new treats the zone as cleared. On this simulated map, "
                          "brighter cells are likelier places for the wreck, and the zone starts "
                          "with half of all the probability.") as beat:
            self.play(FadeOut(VGroup(opts, check, aboard, nothing, title)), FadeOut(p09), FadeOut(p10),
                      run_time=0.8)
            beat.wait_until("simulated", offset=-0.1)
            self.play(FadeIn(key), run_time=0.7)
            beat.wait_until("brighter", offset=-0.1)
            bright = sorted(range(len(cells)), key=lambda i: -PRIOR[i])[:40]
            self.play(LaggedStart(*[Indicate(cells[i], color=BLUE, scale_factor=1.25) for i in bright],
                                  lag_ratio=0.02), run_time=1.2)
            beat.wait_until("half", offset=-0.2)
            self.play(Write(readout_lbl), FadeIn(zval), flag(zone, color=YELLOW), run_time=1.0)

        # ============================== 5 wipe and rescale
        cleared = label("cleared", size=30, color=RED)
        cleared.next_to(self.route_lbl, DOWN, buff=0.25).align_to(self.route_lbl, LEFT)
        self.heat_updater()
        with self.narrate("Cleared means zero. Wipe every cell in the zone, then rescale the rest "
                          "so it adds up to one.") as beat:
            self.a.set_value(0)
            self.play(zone.animate.set_stroke(RED), FadeIn(cleared), run_time=beat.until("Wipe"))
            self.play(self.f.animate.set_value(0), zt.animate.set_value(0),
                      run_time=beat.until("rescale", offset=-0.1))
            self.play(self.a.animate.set_value(1), zval.animate.set_color(RED),
                      run_time=min(1.8, beat.remaining()))

        # ============================== 6 the failure, measured
        zero_rule = MathTex(r"0", r"\times", r"\text{any evidence}", "=", "0", font_size=44)
        zero_rule[0].set_color(RED)
        zero_rule[4].set_color(RED)
        zero_rule.move_to([PX, -0.3, 0])
        hear_lbl = label("chance the ships hear it", size=30).move_to([PX, -1.35, 0])
        hear = MathTex(r"100\%", font_size=52, color=RED).next_to(hear_lbl, DOWN, buff=0.3)
        hear77 = MathTex(r"77\%", font_size=52, color=PURPLE).move_to(hear)
        cite = citation(author="Stone, Keller, Kratzke & Strumpfer", year=2014,
                        venue="Statistical Science")
        with self.narrate("The zone now reads exactly zero, and zero can never come back: no "
                          "later evidence can multiply it up. Zeroing assumes the listening was "
                          "perfect. The analysts who later studied it put the chance of hearing "
                          "the beacons at seventy-seven percent.") as beat:
            self.play(flag(zval, color=RED), run_time=0.9)
            beat.wait_until("no later", offset=-0.2)
            self.play(Write(zero_rule), run_time=1.4)
            beat.wait_until("assumes", offset=-0.1)
            self.play(FadeIn(hear_lbl), FadeIn(hear, shift=0.1 * UP), run_time=beat.until("perfect", end=True))
            beat.wait_until("analysts", offset=-0.1)
            self.play(FadeIn(cite), run_time=0.6)
            beat.wait_until("seventy", offset=-0.15)
            self.play(TransformMatchingShapes(hear, hear77), run_time=1.0)

        # ============================== 7 the bar: p, and the slice p*d
        W, H, X0, BY = 5.4, 0.6, PX - 2.7, 1.25
        zone_bar = Rectangle(width=W * P0, height=H, stroke_width=0, fill_color=BLUE, fill_opacity=0.9)
        zone_bar.move_to([X0, BY, 0], aligned_edge=LEFT)
        out_bar = Rectangle(width=W * (1 - P0), height=H, stroke_width=0, fill_color=BLUE,
                            fill_opacity=0.35).next_to(zone_bar, RIGHT, buff=0)
        zone_tag = label("zone", size=28, color=YELLOW).next_to(zone_bar, UP, buff=0.2)
        out_tag = label("outside", size=28, color=GRAY).next_to(out_bar, UP, buff=0.2)
        p_lbl = MathTex(r"p", "=", r"0.5", font_size=40).next_to(zone_bar, DOWN, buff=0.25)
        p_lbl[0].set_color(BLUE)
        p_lbl[2].set_color(BLUE)
        d_lbl = MathTex(r"d", "=", r"0.77", font_size=48).move_to([PX, -1.0, 0])
        d_lbl.set_color(PURPLE)
        slice_bar = Rectangle(width=W * P0 * D_EST, height=H, stroke_width=0, fill_color=PURPLE,
                              fill_opacity=0.95).move_to(zone_bar.get_left(), aligned_edge=LEFT)
        keep_bar = Rectangle(width=W * P0 * (1 - D_EST), height=H, stroke_width=0, fill_color=BLUE,
                             fill_opacity=0.9).move_to(zone_bar.get_right(), aligned_edge=RIGHT)
        pd_lbl = MathTex(r"p\,d", font_size=40, color=PURPLE).next_to(slice_bar, DOWN, buff=0.25)
        self.cells.clear_updaters()
        with self.narrate("So draw the zone's share as this bar: p, one half. If the wreck is in "
                          "the zone, the ships hear it with chance d. That makes this slice, p "
                          "times d, the part a search could catch.") as beat:
            self.play(FadeOut(zero_rule), FadeOut(hear_lbl), FadeOut(readout), FadeOut(cleared),
                      zone.animate.set_stroke(YELLOW), self.f.animate.set_value(1),
                      UpdateFromFunc(cells, lambda m: self.paint()), run_time=1.0)
            self.play(TransformFromCopy(zone, zone_bar), FadeIn(out_bar), FadeIn(zone_tag),
                      FadeIn(out_tag), run_time=beat.until("p", offset=-0.1))
            self.play(Write(p_lbl), run_time=0.8)
            beat.wait_until("chance d", offset=-0.1)
            self.play(ReplacementTransform(hear77, d_lbl), run_time=1.0)
            beat.wait_until("this slice", offset=-0.1)
            self.add(keep_bar)
            self.remove(zone_bar)
            self.play(TransformFromCopy(d_lbl, slice_bar), run_time=1.0)
            self.play(FadeTransform(p_lbl, pd_lbl), run_time=0.8)

        # ============================== 8 silence removes the slice
        ghost = DashedVMobject(Rectangle(width=W * P0 * D_EST, height=H, color=PURPLE,
                                         stroke_width=2), num_dashes=30).move_to(slice_bar)
        keep_lbl = MathTex(r"p(1-d)", font_size=36, color=BLUE)
        out_lbl = MathTex(r"1-p", font_size=36, color=GRAY)
        self.cells.add_updater(lambda m: self.paint())
        with self.narrate("Silence rules out that slice, and only that slice. What's left adds up "
                          "to one minus p d.") as beat:
            self.a.set_value(0)
            self.play(FadeOut(slice_bar, shift=0.6 * DOWN), FadeOut(pd_lbl, shift=0.6 * DOWN),
                      FadeIn(ghost), self.f.animate.set_value(1 - D_EST),
                      run_time=beat.until("only", offset=-0.1))
            self.play(flag(keep_bar, color=BLUE), run_time=0.8)
            beat.wait_until("What's left", offset=-0.2)
            shift = (X0 - keep_bar.get_left()[0]) * RIGHT
            self.play(FadeOut(ghost), keep_bar.animate.shift(shift), out_bar.animate.shift(shift),
                      zone_tag.animate.shift(shift), out_tag.animate.shift(shift), run_time=1.0)
            keep_lbl.next_to(keep_bar, DOWN, buff=0.25)
            out_lbl.next_to(out_bar, DOWN, buff=0.25)
            total = VGroup(keep_bar, out_bar)
            brace = Brace(total, DOWN, buff=0.75, color=GRAY)
            brace_lbl = MathTex(r"1-p\,d", font_size=40).next_to(brace, DOWN, buff=0.15)
            self.play(FadeIn(keep_lbl), FadeIn(out_lbl), GrowFromCenter(brace), Write(brace_lbl),
                      run_time=min(1.2, beat.remaining()))

        # ============================== 9 rescale -> the formula
        eq = MathTex(r"p_{\text{after}}", "=", r"\frac{p(1-d)}{1-p\,d}", font_size=EQ,
                     substrings_to_isolate=["p(1-d)", r"1-p\,d"]).move_to([PX, -2.0, 0])
        num = eq.get_part_by_tex("p(1-d)")
        den = eq.get_part_by_tex(r"1-p\,d")
        fbar = VGroup(*[g for g in eq[2:] if g is not num and g is not den])
        eq[0].set_color(BLUE)
        num.set_color(BLUE)
        val = MathTex(r"\approx", r"0.19", font_size=EQ)
        val[1].set_color(BLUE)
        lhs = VGroup(eq[0], eq[1])
        with self.narrate("Rescale it back to one. The zone keeps p times one minus d, over one "
                          "minus p d. With these numbers, about nineteen percent: dimmer, but "
                          "alive.") as beat:
            new_keep = W * POST
            self.play(FadeOut(brace), FadeOut(out_lbl),
                      keep_bar.animate.stretch_to_fit_width(new_keep).move_to([X0, BY, 0], aligned_edge=LEFT),
                      out_bar.animate.stretch_to_fit_width(W - new_keep).move_to([X0 + W, BY, 0], aligned_edge=RIGHT),
                      keep_lbl.animate.move_to([X0 + new_keep / 2, keep_lbl.get_y(), 0]),
                      zone_tag.animate.move_to([X0 + new_keep / 2, zone_tag.get_y(), 0]),
                      out_tag.animate.move_to([X0 + new_keep + (W - new_keep) / 2, out_tag.get_y(), 0]),
                      self.a.animate.set_value(1), run_time=beat.until("The zone", offset=-0.1))
            self.play(Write(lhs), run_time=beat.until("p times", offset=-0.1))
            self.play(TransformFromCopy(keep_lbl, num), run_time=beat.until("over", offset=-0.1))
            self.play(Create(fbar), ReplacementTransform(brace_lbl, den), run_time=1.2)
            val.next_to(eq, RIGHT, buff=0.25)
            off = LEFT * (val.width + 0.25) / 2
            val.shift(off)
            beat.wait_until("nineteen", offset=-0.4)
            self.play(eq.animate.shift(off), FadeIn(val), run_time=0.8)
            keep_val = MathTex(r"0.19", font_size=36, color=BLUE).move_to(keep_lbl)
            self.play(TransformFromCopy(val[1], keep_val), FadeOut(keep_lbl), run_time=0.8)

        # ============================== 10 d is a guess too -> prediction pause
        tag1 = label("0.9 if a beacon works", size=26, color=GRAY)
        tag2 = label("minus beacons lost in the crash", size=26, color=GRAY)
        tags = VGroup(tag1, tag2).arrange(DOWN, buff=0.15).move_to([PX, -0.75, 0])
        dq = MathTex(r"d", "=", r"?", font_size=48 * 0.85, color=PURPLE).move_to([PX, 0.05, 0])
        with self.narrate("And d is a guess too: a ninety percent chance of hearing a working "
                          "beacon, discounted for beacons the crash might have destroyed. Suppose "
                          "both beacons died on impact. [pause 1.2]") as beat:
            self.play(eq.animate.set_opacity(0.3), val.animate.set_opacity(0.3),
                      d_lbl.animate.scale(0.85).move_to([PX, 0.05, 0]), run_time=0.8)
            self.play(flag(d_lbl, color=PURPLE), run_time=0.8)
            beat.wait_until("ninety", offset=-0.1)
            self.play(FadeIn(tag1, shift=0.1 * DOWN), run_time=0.7)
            beat.wait_until("discounted", offset=-0.1)
            self.play(FadeIn(tag2, shift=0.1 * DOWN), run_time=0.7)
            beat.wait_until("Suppose", offset=-0.1)
            self.play(FadeOut(tags), TransformMatchingTex(d_lbl, dq), run_time=1.0)

        # ============================== 11 d = 0: the silence moves nothing
        dt = ValueTracker(D_EST)
        d_live = VGroup(MathTex(r"d", "=", font_size=48 * 0.85, color=PURPLE),
                        DecimalNumber(D_EST, 2, font_size=48 * 0.85, color=PURPLE)).arrange(RIGHT, buff=0.15)
        d_live.move_to(dq)
        d_live[1].add_updater(lambda m: m.set_value(dt.get_value()))

        def post(d):
            return P0 * (1 - d) / (1 - P0 * d)
        keep_bar.add_updater(lambda m: m.stretch_to_fit_width(max(W * post(dt.get_value()), 1e-3))
                             .move_to([X0, BY, 0], aligned_edge=LEFT))
        out_bar.add_updater(lambda m: m.stretch_to_fit_width(W - W * post(dt.get_value()))
                            .move_to([X0 + W, BY, 0], aligned_edge=RIGHT))
        zone_tag.add_updater(lambda m: m.move_to([X0 + W * post(dt.get_value()) / 2,
                                                  zone_tag.get_y(), 0]))
        out_tag.add_updater(lambda m: m.move_to([X0 + W * post(dt.get_value())
                                                 + W * (1 - post(dt.get_value())) / 2,
                                                 out_tag.get_y(), 0]))
        kv = DecimalNumber(POST, 2, font_size=36, color=BLUE).move_to(keep_val)
        kv.add_updater(lambda m: m.set_value(post(dt.get_value())).next_to(keep_bar, DOWN, buff=0.25))
        val_live = DecimalNumber(POST, 2, font_size=EQ, color=BLUE).move_to(val[1])
        val_live.add_updater(lambda m: m.set_value(post(dt.get_value())))
        self.cells.clear_updaters()

        def follow_d(m):
            self.f.set_value(1 - dt.get_value())
            self.paint()
        self.cells.add_updater(follow_d)
        with self.narrate("Then d is zero, the slice is empty, and a month of silence moves "
                          "nothing. The zone is back to one half.") as beat:
            self.remove(keep_val)
            self.add(kv)
            self.play(FadeTransform(dq, d_live), run_time=0.6)
            self.play(dt.animate.set_value(0), run_time=beat.until("The zone", offset=-0.1))
            self.remove(val[1])
            self.add(val_live)
            self.play(eq.animate.set_opacity(1), val[0].animate.set_opacity(1), dim(),
                      flag(zone, color=YELLOW), run_time=min(1.2, beat.remaining()))
        for m in (keep_bar, out_bar, zone_tag, out_tag, kv, val_live, d_live[1]):
            m.clear_updaters()
        self.cells.clear_updaters()

        # ============================== 12 the real analysis
        right = VGroup(keep_bar, out_bar, zone_tag, out_tag, kv, d_live, eq, val[0], val_live, key)
        small_eq = VGroup(eq, val[0], val_live)
        team = label("BEA asks Metron, 2010", size=30).move_to([PX, 2.6, 0])
        maps = VGroup(label("map 1: beacons might work", size=28),
                      label("map 2: beacons failed", size=28, color=INK)).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        maps.move_to([PX, 0.9, 0])
        key2 = label("simulated · beacons failed, d = 0", size=26, color=GRAY).move_to(key, aligned_edge=LEFT)
        with self.narrate("In twenty ten, French investigators asked Lawrence Stone's team at "
                          "Metron to rebuild the map with Bayes, counting every failed search. "
                          "Unsure of the beacons, they also computed a map that assumed the "
                          "beacons had failed.") as beat:
            self.play(FadeOut(VGroup(keep_bar, out_bar, zone_tag, out_tag, kv, d_live)),
                      small_eq.animate.move_to([PX, -2.0, 0]), run_time=1.0)
            self.play(FadeIn(team, shift=0.1 * DOWN), flag(cite, color=INK), run_time=1.0)
            beat.wait_until("counting", offset=-0.1)
            self.play(FadeIn(maps[0], shift=0.1 * DOWN), run_time=0.8)
            beat.wait_until("Unsure", offset=-0.1)
            self.play(FadeIn(maps[1], shift=0.1 * DOWN), run_time=0.8)
            beat.wait_until("assumed", offset=-0.1)
            self.play(ReplacementTransform(key, key2), flag(maps[1]), run_time=1.0)

        # ============================== 13 found
        w_pt = nm(*WRECK_NM)
        ring = Circle(0.13, color=GREEN, stroke_width=5).move_to(w_pt).set_z_index(5)
        sweep = Circle(0.05, color=GRAY, stroke_width=2.5).move_to(MC).set_z_index(4)
        found = label("wreck, April 2011", size=30, color=GREEN).move_to([PX, 0.9, 0])
        leader = DashedLine(w_pt + RIGHT * 0.15, found.get_left() + LEFT * 0.15, color=GREEN,
                            stroke_width=2, dash_length=0.08)
        silent = MathTex(r"\text{recovered beacon: no signal}", font_size=38).move_to([PX, -0.1, 0])
        with self.narrate("In April twenty eleven, the search began near the centre. Within a week, "
                          "sonar robots found the wreck, inside the zone the ships had listened to. "
                          "The recovered beacon, tested with a fully charged battery, made no "
                          "sound.") as beat:
            self.play(FadeOut(maps), FadeOut(team), run_time=0.6)
            beat.wait_until("centre", offset=-0.2)
            self.play(sweep.animate.scale(14), run_time=beat.until("found", offset=-0.1), rate_func=LINEAR)
            self.play(FadeOut(sweep), Create(ring), Create(leader), FadeIn(found), run_time=1.0)
            beat.wait_until("inside", offset=-0.1)
            self.play(flag(zone, color=YELLOW), run_time=1.0)
            beat.wait_until("recovered", offset=-0.1)
            self.play(Write(silent), run_time=1.2)

        # ============================== 14 honest limits
        with self.narrate("The map didn't find the plane; the robots did. It told them where to "
                          "start, and it was only as good as its guess for d.") as beat:
            self.play(flag(ring, color=GREEN), run_time=1.0)
            beat.wait_until("where to", offset=-0.1)
            self.play(Indicate(self.lkp, color=YELLOW, scale_factor=1.6), run_time=1.0)
            beat.wait_until("guess", offset=-0.1)
            self.play(flag(num, color=PURPLE), flag(den, color=PURPLE), run_time=0.9)

        # ============================== 15 landing: the cold-open frame, re-seen
        day31 = MathTex(r"\text{day }31", font_size=48, color=YELLOW).move_to([PX, 2.6, 0])
        heard2 = MathTex(r"\text{beacons heard: } 0", font_size=40, color=YELLOW).next_to(day31, DOWN, buff=0.35)
        with self.narrate("Those thirty-one days of silence said less about the ocean than about "
                          "the beacons.") as beat:
            self.play(FadeOut(silent), FadeIn(day31), FadeIn(heard2), run_time=beat.until("ocean", offset=-0.1))
            self.play(Indicate(self.rim, color=INK, scale_factor=1.0), run_time=0.8)
            beat.wait_until("beacons", offset=-0.1)
            self.play(heard2.animate.set_color(PURPLE), flag(heard2, color=PURPLE), run_time=0.9)
        self.end_card()
