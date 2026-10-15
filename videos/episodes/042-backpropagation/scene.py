"""Episode 42: How a Network Learns: Passing the Blame Backward.

    videos/toolkit/render.sh videos/episodes/042-backpropagation/scene.py Episode \
        videos/episodes/042-backpropagation/final.mp4
"""
import numpy as np
from manim import *
from sample_space import *

# ----------------------------------------------------------------------------- toy network
# x1=2, x2=1, w1=1, w2=0.5 -> z=2.5 -> h=ReLU(z)=2.5 -> y=v*h=5 (v=2) -> L=(y-3)^2=4
# blame: dL/dy=4, dL/dh=8, dL/dv=10, dL/dz=8, dL/dw1=16, dL/dw2=8
GY = 0.6                      # centre line of the toy graph
Y1, Y2 = GY + 1.25, GY - 1.25
X_IN, X_MUL, X_PLUS, X_RELU, X_V, X_LOSS = -6.0, -3.8, -1.7, 0.45, 2.6, 5.1
R = 0.38
VAL = 36                      # MathTex size of edge values / blames


def op_node(sym, x, y):
    c = Circle(R, stroke_color=GRAY, stroke_width=3, fill_color=BG, fill_opacity=1).move_to([x, y, 0])
    s = MathTex(sym, font_size=40, color=INK).move_to(c)
    return VGroup(c, s)


def relu_node(x, y):
    c = Circle(R, stroke_color=GRAY, stroke_width=3, fill_color=BG, fill_opacity=1).move_to([x, y, 0])
    ramp = VMobject(stroke_color=INK, stroke_width=3).set_points_as_corners(
        [[-0.22, -0.1, 0], [0, -0.1, 0], [0.2, 0.14, 0]]).move_to(c)
    return VGroup(c, ramp)


def edge(a, b):
    return Line(a, b, stroke_color=GRAY, stroke_width=3)


def side_pos(line, side, d=0.36):
    """Point beside the middle of `line`; side=+1 above, -1 below."""
    p, q = line.get_start(), line.get_end()
    t = (q - p) / np.linalg.norm(q - p)
    n = np.array([-t[1], t[0], 0])
    if n[1] < 0:
        n = -n
    return (p + q) / 2 + side * d * n


def path_line(points):
    return VMobject().set_points_as_corners([np.array(p, dtype=float) for p in points])


class Episode(NarratedScene):
    EPISODE = 42
    TITLE = "How a Network Learns: Passing the Blame Backward"
    PRONUNCIATIONS = {"ReLU": "ray loo", "Linnainmaa": "linn eye mah", "Werbos": "wer boss",
                      "Rumelhart": "roomel hart"}

    # ------------------------------------------------------------------ big network
    def build_big(self):
        sizes = [5, 7, 7, 7, 4]
        xs = np.linspace(-5.7, 0.3, len(sizes))
        layers = []
        for x, n in zip(xs, sizes):
            ys = (np.arange(n) - (n - 1) / 2) * 0.6 + 0.5
            layers.append(VGroup(*[Circle(0.12, stroke_color=GRAY, stroke_width=2, fill_color=BG,
                                          fill_opacity=1).move_to([x, y, 0]) for y in ys]))
        err = Circle(0.36, stroke_color=GRAY, stroke_width=3, fill_color=BG, fill_opacity=1).move_to([1.75, 0.5, 0])
        err_l = MathTex("L", font_size=40).move_to(err)
        err_t = label("error", size=26, color=GRAY).next_to(err, DOWN, buff=0.2)
        gaps = []
        for a, b in zip(layers[:-1], layers[1:]):
            gaps.append(VGroup(*[Line(p.get_center(), q.get_center(), stroke_width=1.4, color=DIM)
                                 for p in a for q in b]))
        gaps.append(VGroup(*[Line(p.get_center(), err.get_center(), stroke_width=1.4, color=DIM)
                             for p in layers[-1]]))
        net = VGroup(*gaps, *layers, err, err_l, err_t)
        net.gaps, net.layers, net.err = gaps, layers, VGroup(err, err_l, err_t)
        return net

    # ------------------------------------------------------------------ construct
    def construct(self):
        net = self.build_big()
        header = MathTex("N", "=", r"10^6", r"\text{ weights}", font_size=40)
        header_s = label("(schematic)", size=26, color=GRAY)
        head = VGroup(header, header_s).arrange(RIGHT, buff=0.25).move_to([-2.0, 3.2, 0])
        focus_edge = net.gaps[1][17]

        slope = MathTex(r"\frac{\partial L}{\partial w}", font_size=44, color=RED)
        slope_n = MathTex(r"\times\,10^6", font_size=40, color=RED)
        runs_l = MathTex(r"\text{runs}", "=", font_size=44, color=PURPLE)
        runs_q = MathTex("?", font_size=52, color=PURPLE)
        slope.move_to([4.3, 1.5, 0])
        slope_n.next_to(slope, RIGHT, buff=0.2)
        runs_l.move_to([3.95, -0.2, 0])
        runs_q.next_to(runs_l, RIGHT, buff=0.2)

        # 1 ---------------------------------------------------------------- cold open
        with self.narrate("This network has a million weights. Training needs the same number "
                          "from each one: how fast the error changes when that weight moves.") as beat:
            self.play(LaggedStart(*[Create(g) for g in net.gaps], lag_ratio=0.25),
                      LaggedStart(*[FadeIn(l) for l in net.layers], lag_ratio=0.25),
                      FadeIn(net.err), run_time=beat.until("million", offset=-0.2))
            self.play(Write(head), run_time=beat.until("Training", offset=-0.1, min_time=0.8))
            beat.wait_until("error", offset=-0.2)
            self.play(Indicate(net.err, color=YELLOW, scale_factor=1.1), run_time=0.8)
            beat.wait_until("that weight", offset=-0.2)
            self.play(focus_edge.animate.set_stroke(YELLOW, width=6), run_time=0.6)
            self.play(TransformFromCopy(VGroup(net.err[1], focus_edge), slope), run_time=beat.remaining(0.9))

        with self.narrate("That's a million slopes. How many runs of the network does it take "
                          "to get them all? Make a guess. [pause 1.5]") as beat:
            self.play(LaggedStart(*[g.animate.set_stroke(RED, width=1.6, opacity=0.6) for g in net.gaps],
                                  lag_ratio=0.15),
                      Write(slope_n), run_time=beat.until("How", offset=-0.1))
            self.play(Write(runs_l), run_time=beat.until("Make", offset=-0.2))
            self.play(FadeIn(runs_q, scale=1.4), run_time=0.6)

        # 3 ---------------------------------------------------------------- stakes
        steps = MathTex(r"\text{per step}", r"\;\times\;", r"\text{thousands of steps}",
                        font_size=36, color=GRAY).next_to(VGroup(runs_l, runs_q), DOWN, buff=0.4)
        steps.align_to(runs_l, LEFT)
        keep_in_safe(steps)
        with self.narrate("Training repeats this step thousands of times, so this one count "
                          "decides whether big networks can be trained at all.") as beat:
            self.play(FadeIn(steps[0]), run_time=0.8)
            beat.wait_until("thousands", offset=-0.2)
            self.play(FadeIn(steps[1:], shift=0.1 * RIGHT), run_time=0.9)
            for _ in range(2):
                if beat.remaining() > 1.6:
                    self.play(LaggedStart(*[g.animate.set_stroke(opacity=0.25) for g in net.gaps],
                                          lag_ratio=0.12), run_time=0.7)
                    self.play(LaggedStart(*[g.animate.set_stroke(opacity=0.6) for g in net.gaps],
                                          lag_ratio=0.12), run_time=0.7)

        # 4 ---------------------------------------------------------------- toy network
        in1 = MathTex("x_1", font_size=40).move_to([X_IN, Y1, 0])
        in2 = MathTex("x_2", font_size=40).move_to([X_IN, Y2, 0])
        mul1, mul2 = op_node(r"\times", X_MUL, Y1), op_node(r"\times", X_MUL, Y2)
        plus = op_node("+", X_PLUS, GY)
        relu = relu_node(X_RELU, GY)
        mulv = op_node(r"\times", X_V, GY)
        loss_box = RoundedRectangle(corner_radius=0.15, width=1.75, height=0.8, stroke_color=GRAY,
                                    stroke_width=3, fill_color=BG, fill_opacity=1).move_to([X_LOSS, GY, 0])
        loss_tex = MathTex("(", "y", "-3)^2", font_size=40).move_to(loss_box)
        lossn = VGroup(loss_box, loss_tex)

        e_in1 = edge(in1.get_right() + RIGHT * 0.15, mul1.get_left())
        e_in2 = edge(in2.get_right() + RIGHT * 0.15, mul2.get_left())
        d1 = plus.get_center() - mul1.get_center()
        d1 /= np.linalg.norm(d1)
        d2 = plus.get_center() - mul2.get_center()
        d2 /= np.linalg.norm(d2)
        e_m1 = edge(mul1.get_center() + d1 * R, plus.get_center() - d1 * R)
        e_m2 = edge(mul2.get_center() + d2 * R, plus.get_center() - d2 * R)
        e_z = edge(plus.get_right(), relu.get_left())
        e_h = edge(relu.get_right(), mulv.get_left())
        e_y = edge(mulv.get_right(), loss_box.get_left())
        edges = VGroup(e_in1, e_in2, e_m1, e_m2, e_z, e_h, e_y)

        w1 = MathTex("w_1", "=", "1", font_size=VAL).next_to(mul1, UP, buff=0.22)
        w2 = MathTex("w_2", "=", "0.5", font_size=VAL).next_to(mul2, DOWN, buff=0.22)
        wv = MathTex("v", "=", "2", font_size=VAL).next_to(mulv, UP, buff=0.22)

        def val(name, v, line, side=1, d=0.36):
            parts = ([name, "="] if name else []) + [v]
            m = MathTex(*parts, font_size=VAL)
            m[-1].set_color(BLUE)
            return m.move_to(side_pos(line, side, d))

        v_x1 = val(None, "2", e_in1)
        v_x2 = val(None, "1", e_in2)
        v_m1 = val(None, "2", e_m1, 1, 0.34)
        v_m2 = val(None, "0.5", e_m2, -1, 0.38)
        v_z = val("z", "2.5", e_z)
        v_h = val("h", "2.5", e_h)
        v_y = val("y", "5", e_y)
        v_L = MathTex("L", "=", "4", font_size=VAL)
        v_L[-1].set_color(BLUE)
        v_L.next_to(loss_box, UP, buff=0.22)
        values = VGroup(v_x1, v_x2, v_m1, v_m2, v_z, v_h, v_y, v_L)
        toy_tag = label("toy network", size=22, color=GRAY).move_to([-5.5, 3.35, 0])
        leg_val = MathTex(r"\text{values}\;\rightarrow", font_size=36, color=BLUE)
        leg_val.next_to(toy_tag, DOWN, buff=0.18).align_to(toy_tag, LEFT)

        runs_t = ValueTracker(0)
        runs_top = MathTex(r"\text{runs}", "=", font_size=40, color=PURPLE).move_to([3.7, 3.25, 0])
        runs_num = DecimalNumber(0, num_decimal_places=0, group_with_commas=True, font_size=40,
                                 color=PURPLE)
        runs_num.add_updater(lambda m: m.set_value(runs_t.get_value()).next_to(runs_top, RIGHT, buff=0.2))

        with self.narrate("Shrink it to three weights. Two inputs, two and one, each times a weight, "
                          "then summed, passed through a ReLU, and scaled by a third weight.") as beat:
            self.play(FadeOut(net, scale=0.6), FadeOut(head), FadeOut(slope), FadeOut(slope_n),
                      FadeOut(steps), FadeOut(runs_q),
                      ReplacementTransform(runs_l, runs_top), run_time=1.0)
            runs_num.update()
            self.play(FadeIn(toy_tag), FadeIn(runs_num), run_time=beat.until("Two", offset=-0.1, min_time=0.5))
            self.play(FadeIn(in1), FadeIn(in2), Create(e_in1), Create(e_in2),
                      FadeIn(leg_val), FadeIn(v_x1), FadeIn(v_x2),
                      run_time=beat.until("each", offset=-0.1))
            self.play(GrowFromCenter(mul1), GrowFromCenter(mul2), FadeIn(w1), FadeIn(w2),
                      run_time=beat.until("summed", offset=-0.1))
            self.play(Create(e_m1), Create(e_m2), GrowFromCenter(plus), run_time=beat.until("passed", offset=-0.1))
            self.play(Create(e_z), GrowFromCenter(relu), run_time=beat.until("scaled", offset=-0.1))
            self.play(Create(e_h), GrowFromCenter(mulv), FadeIn(wv), run_time=beat.until("third", offset=0.3))
            self.play(Create(e_y), FadeIn(lossn), run_time=beat.remaining(0.6))

        # forward pass, values appear left to right
        fwd_path = path_line([e_in1.get_start(), mul1.get_center(), plus.get_center(),
                              relu.get_center(), mulv.get_center(), loss_box.get_center()])
        with self.narrate("The output is five, the target is three, and the loss, the squared miss, is four.") as beat:
            pulse = Dot(radius=0.09, color=BLUE).move_to(fwd_path.get_start())
            self.add(pulse)
            self.play(MoveAlongPath(pulse, fwd_path, rate_func=LINEAR),
                      LaggedStart(FadeIn(v_m1), FadeIn(v_m2), FadeIn(v_z), FadeIn(v_h), lag_ratio=0.4),
                      run_time=beat.until("five", offset=-0.1))
            self.play(FadeIn(v_y), runs_t.animate.set_value(1), run_time=0.5)
            beat.wait_until("three", offset=-0.1)
            self.play(flag(loss_tex[2]), run_time=0.7)
            beat.wait_until("four", offset=-0.2)
            self.play(FadeOut(pulse), FadeIn(v_L, shift=0.1 * UP), run_time=0.6)

        # 6 ---------------------------------------------------------------- naive nudge
        fd = MathTex(r"\frac{4.1616 - 4}{0.01}", r"\approx", "16.16", font_size=44,
                     substrings_to_isolate=["4.1616", "0.01"]).move_to([0.6, -2.35, 0])
        fd.get_part_by_tex("4.1616").set_color(BLUE)
        fd.get_part_by_tex("0.01").set_color(YELLOW)
        new_vals = {
            "w1": MathTex("w_1", "=", "1.01", font_size=VAL).move_to(w1, aligned_edge=LEFT),
            "m1": val(None, "2.02", e_m1, 1, 0.34), "z": val("z", "2.52", e_z),
            "h": val("h", "2.52", e_h), "y": val("y", "5.04", e_y),
        }
        new_vals["w1"][2].set_color(YELLOW)
        new_L = MathTex("L", "=", "4.1616", font_size=VAL).next_to(loss_box, UP, buff=0.22)
        new_L[-1].set_color(BLUE)
        olds = [w1.copy(), v_m1.copy(), v_z.copy(), v_h.copy(), v_y.copy(), v_L.copy()]
        est1 = MathTex(r"\approx 16.16", font_size=VAL, color=GRAY).next_to(w1, RIGHT, buff=0.3)
        with self.narrate("The obvious way to get a slope is to nudge. Raise w one by one hundredth "
                          "and run everything again. The loss rises to four point one six one six, "
                          "so the slope is about sixteen point one six.") as beat:
            beat.wait_until("Raise", offset=-0.1)
            self.play(Transform(w1, new_vals["w1"]), run_time=beat.until("and", offset=-0.1, min_time=0.6))
            pulse = Dot(radius=0.09, color=BLUE).move_to(mul1)
            self.add(pulse)
            p2 = path_line([mul1.get_center(), plus.get_center(), relu.get_center(),
                            mulv.get_center(), loss_box.get_center()])
            t_run = beat.until("rises", offset=-0.1, min_time=1.5)
            self.play(MoveAlongPath(pulse, p2, rate_func=LINEAR),
                      LaggedStart(Transform(v_m1, new_vals["m1"]), Transform(v_z, new_vals["z"]),
                                  Transform(v_h, new_vals["h"]), Transform(v_y, new_vals["y"]),
                                  lag_ratio=0.5),
                      runs_t.animate.set_value(2), run_time=t_run)
            self.play(FadeOut(pulse), Transform(v_L, new_L), run_time=beat.until("so the", offset=-0.1, min_time=0.6))
            self.play(TransformFromCopy(v_L[2], fd.get_part_by_tex("4.1616")),
                      FadeIn(VGroup(*[p for p in fd[0] if p is not fd.get_part_by_tex("4.1616")
                                      and p is not fd.get_part_by_tex("0.01")])),
                      TransformFromCopy(w1[2], fd.get_part_by_tex("0.01")),
                      run_time=beat.until("sixteen", offset=-0.2, min_time=1.0))
            self.play(Write(fd[-2:]), run_time=0.8)
            self.play(TransformFromCopy(fd[-1], est1), run_time=beat.remaining(0.8))

        # 7 ---------------------------------------------------------------- the other weights
        est2 = MathTex(r"\approx 8.04", font_size=VAL, color=GRAY).next_to(w2, RIGHT, buff=0.3)
        est3 = MathTex(r"\approx 10.06", font_size=VAL, color=GRAY).next_to(wv, RIGHT, buff=0.3)
        with self.narrate("Repeat for each weight. Three weights cost four runs.") as beat:
            self.play(FadeOut(fd), Transform(w1, olds[0]), Transform(v_m1, olds[1]),
                      Transform(v_z, olds[2]), Transform(v_h, olds[3]), Transform(v_y, olds[4]),
                      Transform(v_L, olds[5]), run_time=0.6)
            for wl, est, start in ((w2, est2, mul2), (wv, est3, mulv)):
                pts = [start.get_center()] + [m.get_center() for m in (plus, relu, mulv)
                                              if m.get_center()[0] > start.get_center()[0]] + [loss_box.get_center()]
                pd = Dot(radius=0.09, color=BLUE).move_to(pts[0])
                self.add(pd)
                self.play(wl.animate.set_color(YELLOW), MoveAlongPath(pd, path_line(pts), rate_func=LINEAR),
                          runs_t.animate.set_value(runs_t.get_value() + 1), run_time=1.0)
                self.play(FadeOut(pd), wl.animate.set_color(INK), FadeIn(est, shift=0.1 * RIGHT), run_time=0.5)
            beat.wait_until("four", offset=-0.2)
            self.play(flag(runs_num), run_time=0.7)

        # 8 ---------------------------------------------------------------- fail: scale up
        wts_t = ValueTracker(3)
        wts_top = MathTex(r"\text{weights}", "=", font_size=40).next_to(runs_top, DOWN, buff=0.3).align_to(runs_top, RIGHT)
        wts_num = DecimalNumber(3, num_decimal_places=0, group_with_commas=True, font_size=40)
        wts_num.add_updater(lambda m: m.set_value(wts_t.get_value()).next_to(wts_top, RIGHT, buff=0.2))
        runs_num.clear_updaters()
        runs_num.add_updater(lambda m: m.set_value(wts_t.get_value() + 1).next_to(runs_top, RIGHT, buff=0.2))
        per = MathTex(r"\text{per step}", font_size=30, color=GRAY)
        with self.narrate("Now scale back up. A million weights cost a million and one runs, for a "
                          "single step. And sixteen point one six is not even the true slope.") as beat:
            wts_num.update()
            self.play(FadeIn(wts_top), FadeIn(wts_num), run_time=0.6)
            beat.wait_until("million", offset=-0.3)
            u = ValueTracker(0)
            wts_t.add_updater(lambda m: m.set_value(round(3 * (1e6 / 3) ** u.get_value())))
            self.add(wts_t)
            self.play(u.animate.set_value(1), run_time=beat.until("runs", offset=0.2, min_time=1.5), rate_func=SMOOTH)
            wts_t.clear_updaters()
            wts_t.set_value(1_000_000)
            per.next_to(VGroup(runs_top, runs_num), LEFT, buff=0.3)
            beat.wait_until("single", offset=-0.2)
            self.play(FadeIn(per), flag(runs_num, color=PURPLE), run_time=0.8)
            beat.wait_until("sixteen", offset=-0.1)
            self.play(Indicate(est1, color=YELLOW, scale_factor=1.15), run_time=0.9)

        # 9 ---------------------------------------------------------------- the waste
        stretch = [plus, relu, mulv, lossn]
        with self.narrate("Here is the waste. Every rerun recomputed this same stretch: the sum, "
                          "the ReLU, the output, the loss.") as beat:
            beat.wait_until("this", offset=-0.1)
            self.play(VGroup(e_z, e_h, e_y).animate.set_stroke(YELLOW, width=5), run_time=0.8)
            for word, node in zip(("sum", "ReLU", "output", "loss"), stretch):
                beat.wait_until(word, offset=-0.15)
                self.play(node[0].animate.set_stroke(YELLOW, width=5), run_time=0.45)

        # 10 --------------------------------------------------------------- backward: the loss
        leg_bl = MathTex(r"\leftarrow\;\text{blame}", font_size=36, color=RED)
        leg_bl.next_to(leg_val, DOWN, buff=0.12).align_to(leg_val, LEFT)
        lslope = MathTex("2(", "y", "-3)", "=", "4", font_size=VAL)
        lslope[-1].set_color(RED)
        lslope.next_to(loss_box, DOWN, buff=0.25)
        b_y = MathTex("4", font_size=VAL, color=RED).move_to(side_pos(e_y, -1))
        with self.narrate("So ask once, from the far end, and walk backward. The loss is y minus three, "
                          "squared, so its slope in y is two times y minus three, which is four. "
                          "Call that y's blame.") as beat:
            self.play(VGroup(e_z, e_h, e_y).animate.set_stroke(GRAY, width=3),
                      *[n[0].animate.set_stroke(GRAY, width=3) for n in stretch],
                      dim(est1, est2, est3, opacity=0.45), run_time=0.8)
            self.play(Indicate(loss_box, color=RED, scale_factor=1.06), FadeIn(leg_bl, shift=0.2 * LEFT),
                      run_time=beat.until("two times", offset=-0.1, min_time=0.8))
            self.play(TransformFromCopy(loss_tex, lslope[:3]), run_time=beat.until("which", offset=-0.1, min_time=0.8))
            self.play(Write(lslope[3:]), run_time=0.6)
            beat.wait_until("Call", offset=-0.1)
            self.play(TransformFromCopy(lslope[-1], b_y), run_time=beat.remaining(0.8))

        # 11 --------------------------------------------------------------- multiply node
        tag_v = MathTex(r"\times 2", font_size=VAL).next_to(mulv, DOWN, buff=0.22)
        b_h = MathTex("8", font_size=VAL, color=RED).move_to(side_pos(e_h, -1))
        b_v = MathTex("10", font_size=VAL, color=RED)
        b_v.add_background_rectangle(color=BG, opacity=1, buff=0.05)
        b_v.next_to(est3, RIGHT, buff=0.3)
        with self.narrate("At this multiply, y is v times h. Nudge h, and y moves twice as much, so "
                          "h's blame is four times two, eight. And v's blame is four times h, ten.") as beat:
            beat.wait_until("this", offset=-0.1)
            self.play(Indicate(mulv, color=YELLOW, scale_factor=1.15), FadeOut(lslope), run_time=0.8)
            beat.wait_until("twice", offset=-0.2)
            self.play(TransformFromCopy(wv[2], tag_v), run_time=0.8)
            beat.wait_until("four times", offset=-0.1)
            self.play(TransformFromCopy(VGroup(b_y, tag_v), b_h), run_time=beat.until("And", offset=-0.1, min_time=0.9))
            self.play(TransformFromCopy(VGroup(b_y, v_h[2]), b_v), run_time=beat.remaining(0.9))

        # 12 --------------------------------------------------------------- relu + plus
        tag_r = MathTex(r"\times 1", font_size=VAL).next_to(relu, DOWN, buff=0.22)
        b_z = MathTex("8", font_size=VAL, color=RED).move_to(side_pos(e_z, -1))
        b_m1 = MathTex("8", font_size=VAL, color=RED).move_to(side_pos(e_m1, -1, 0.34))
        b_m2 = MathTex("8", font_size=VAL, color=RED).move_to(side_pos(e_m2, 1, 0.34))
        with self.narrate("The ReLU is on, so its slope is one, and the eight passes straight through. "
                          "The plus node hands that same eight to both branches.") as beat:
            beat.wait_until("slope", offset=-0.1)
            self.play(FadeIn(tag_r, shift=0.1 * UP), run_time=0.6)
            beat.wait_until("passes", offset=-0.1)
            self.play(TransformFromCopy(b_h, b_z), run_time=0.9)
            beat.wait_until("both", offset=-0.2)
            self.play(TransformFromCopy(b_z, b_m1), TransformFromCopy(b_z, b_m2), run_time=beat.remaining(0.9))

        # 13 --------------------------------------------------------------- prediction pause
        b_w2 = MathTex("8", font_size=VAL, color=RED)
        b_w2.next_to(est2, RIGHT, buff=0.3)
        b_w1 = MathTex("16", font_size=VAL, color=RED)
        b_w1.next_to(est1, RIGHT, buff=0.3)
        with self.narrate("w two's input is one. What blame does it get? [pause 1.5]") as beat:
            self.play(Indicate(v_x2, color=YELLOW, scale_factor=1.3), run_time=beat.until("What", offset=-0.1, min_time=0.8))
            self.play(Indicate(w2[0], color=YELLOW, scale_factor=1.2), run_time=0.9)

        with self.narrate("Eight times one, eight. And w one gets eight times two: sixteen exactly, "
                          "the value the nudging only approximated.") as beat:
            self.play(TransformFromCopy(VGroup(b_m2, v_x2), b_w2), run_time=beat.until("And", offset=-0.1, min_time=0.9))
            self.play(TransformFromCopy(VGroup(b_m1, v_x1), b_w1), run_time=beat.until("sixteen", offset=-0.1, min_time=0.9))
            beat.wait_until("approximated", offset=-0.5)
            self.play(est1.animate.set_opacity(1), est2.animate.set_opacity(1), est3.animate.set_opacity(1),
                      run_time=0.6)
            self.play(est1.animate.set_opacity(0.45), est2.animate.set_opacity(0.45),
                      est3.animate.set_opacity(0.45), run_time=beat.remaining(0.6))

        # 15 --------------------------------------------------------------- chain rule
        sym = MathTex(r"\frac{\partial L}{\partial w_1}", "=", r"\frac{\partial L}{\partial y}",
                      r"\frac{\partial y}{\partial h}", r"\frac{\partial h}{\partial z}",
                      r"\frac{\partial z}{\partial w_1}", font_size=40)
        sym.arrange(RIGHT, buff=0.42)
        sym.move_to([1.2, -2.0, 0])
        sym[0].set_color(RED)
        sym[2].set_color(RED)
        nums = [MathTex(s, font_size=40, color=c) for s, c in
                (("16", RED), ("=", INK), ("4", RED), ("2", INK), ("1", INK), ("2", BLUE))]
        for n, s in zip(nums, sym):
            n.move_to([s.get_center()[0], -2.95, 0])
        dots_ = VGroup(*[MathTex(r"\times", font_size=36, color=GRAY).move_to(
            [(sym[i].get_right()[0] + sym[i + 1].get_left()[0]) / 2, -2.95, 0]) for i in (2, 3, 4)])
        numrow = VGroup(*nums)
        path_hl = VGroup(e_in1, e_m1, e_z, e_h, e_y)
        with self.narrate("Line up the factors along w one's path: four, two, one, two. Each is one "
                          "node's local slope, and their product is the chain rule, read from the "
                          "loss backward.") as beat:
            self.play(path_hl.animate.set_stroke(YELLOW, width=5), run_time=beat.until("four", offset=-0.1, min_time=0.6))
            self.play(TransformFromCopy(b_y, nums[2]), run_time=0.5)
            beat.wait_until("two", offset=-0.1)
            self.play(TransformFromCopy(tag_v, nums[3]), FadeIn(dots_[0]), run_time=0.5)
            beat.wait_until("one", offset=-0.1)
            self.play(TransformFromCopy(tag_r, nums[4]), FadeIn(dots_[1]), run_time=0.5)
            beat.wait_until("two", 2, offset=-0.1)
            self.play(TransformFromCopy(v_x1, nums[5]), FadeIn(dots_[2]), run_time=0.5)
            self.play(TransformFromCopy(b_w1, nums[0]), FadeIn(nums[1]), run_time=0.7)
            beat.wait_until("chain", offset=-0.6)
            self.play(LaggedStart(*[FadeIn(sym[i], shift=0.2 * UP) for i in (2, 3, 4, 5)], lag_ratio=0.35),
                      run_time=1.4)
            self.play(FadeIn(sym[0], shift=0.2 * UP), FadeIn(sym[1]), run_time=beat.remaining(0.6))

        # 16 --------------------------------------------------------------- shared part
        shared = SurroundingRectangle(VGroup(sym[2:5], *nums[2:5]), color=YELLOW, buff=0.12,
                                      corner_radius=0.08, stroke_width=3)
        eq8 = MathTex("=", "8", font_size=40)
        eq8[1].set_color(RED)
        eq8.next_to(shared, RIGHT, buff=0.2).align_to(sym[0], DOWN)
        eq8.move_to([sym[5].get_center()[0] + 1.25, -2.95, 0])
        with self.narrate("The first three factors make the eight, and every weight feeding this sum "
                          "shares them. Going backward, that shared part is computed once.") as beat:
            self.play(path_hl.animate.set_stroke(GRAY, width=3), Create(shared),
                      run_time=beat.until("eight", offset=-0.1, min_time=0.8))
            self.play(flag(b_z, color=RED), run_time=0.8)
            beat.wait_until("every", offset=-0.1)
            self.play(Indicate(b_m1, color=YELLOW, scale_factor=1.3), Indicate(b_m2, color=YELLOW, scale_factor=1.3),
                      run_time=0.9)
            beat.wait_until("once", offset=-0.3)
            self.play(Indicate(b_z, color=YELLOW, scale_factor=1.4), run_time=beat.remaining(0.8))

        # 17 --------------------------------------------------------------- memory
        boxes = VGroup(*[SurroundingRectangle(v[-1], color=BLUE, buff=0.07, stroke_width=2.5)
                         for v in (v_x1, v_x2, v_m1, v_m2, v_z, v_h, v_y)])
        mem = label("kept until the blame returns", size=26, color=BLUE).move_to([0.6, -2.4, 0])
        with self.narrate("The price is memory. v's blame needed h, a value from the forward run, so "
                          "training must keep every forward value until the blame comes back for it.") as beat:
            self.play(FadeOut(VGroup(sym, numrow, dots_, shared)), run_time=0.6)
            beat.wait_until("needed", offset=-0.2)
            self.play(Indicate(b_v, color=YELLOW, scale_factor=1.25), run_time=0.7)
            self.play(Create(boxes[5]), Indicate(v_h, color=BLUE, scale_factor=1.15), run_time=0.8)
            beat.wait_until("every", offset=-0.1)
            self.play(LaggedStart(*[Create(b) for i, b in enumerate(boxes) if i != 5], lag_ratio=0.15),
                      FadeIn(mem), run_time=beat.remaining(1.2))

        # 18 --------------------------------------------------------------- back to the big network
        net2 = self.build_big()
        head2 = VGroup(header.copy(), header_s.copy())
        toy = VGroup(in1, in2, mul1, mul2, plus, relu, mulv, lossn, edges, w1, w2, wv, values,
                     est1, est2, est3, b_y, b_h, b_v, b_z, b_m1, b_m2, b_w1, b_w2, tag_v, tag_r,
                     boxes, mem, toy_tag, leg_val, leg_bl)
        runs_num.clear_updaters()
        cmp_n = MathTex(r"\text{nudging:}", r"1{,}000{,}001", font_size=40, color=PURPLE)
        cmp_b = MathTex(r"\text{backprop:}", "1", "+", "2", r"\approx 3", font_size=40, color=PURPLE)
        cmp_b[1].set_color(BLUE)
        cmp_b[3].set_color(RED)
        cmp_runs = MathTex(r"\text{runs per step}", font_size=36, color=GRAY)
        panel = VGroup(cmp_runs, cmp_n, cmp_b).arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to([4.5, 1.0, 0])
        cmp_b.align_to(cmp_n, LEFT)
        with self.narrate("In the big network, one backward sweep hands every weight its blame. That "
                          "sweep costs about two forward runs, so all million slopes cost about three "
                          "runs, not a million and one.") as beat:
            self.play(FadeOut(toy), FadeOut(VGroup(wts_top, wts_num, per)),
                      FadeIn(net2), FadeIn(head2),
                      ReplacementTransform(VGroup(runs_top, runs_num), cmp_n), FadeIn(cmp_runs),
                      run_time=beat.until("backward", offset=-0.2, min_time=1.0))
            self.play(Indicate(net2.err, color=RED, scale_factor=1.15), run_time=0.6)
            self.play(LaggedStart(*[g.animate.set_stroke(RED, width=1.8, opacity=0.75)
                                    for g in reversed(net2.gaps)], lag_ratio=0.35),
                      run_time=beat.until("That", offset=-0.1, min_time=1.4))
            beat.wait_until("two", offset=-0.1)
            self.play(FadeIn(cmp_b[0]), FadeIn(cmp_b[1:4]), run_time=0.8)
            beat.wait_until("three", offset=-0.2)
            self.play(Write(cmp_b[4]), run_time=0.6)
            beat.wait_until("not", offset=-0.1)
            self.play(flag(cmp_n[1], color=PURPLE), run_time=0.8)

        # 19 --------------------------------------------------------------- history
        tl = Line([-5.6, -2.05, 0], [5.6, -2.05, 0], stroke_color=GRAY, stroke_width=2.5)
        years = [(1970, "Linnainmaa", "1970 · MSc thesis"), (1974, "Werbos", "1974 · PhD thesis"),
                 (1986, "Rumelhart, Hinton & Williams", "1986 · Nature")]
        xs_ = [-4.4, -1.4, 3.1]
        ticks = VGroup(*[Dot([x, -2.05, 0], radius=0.07, color=INK) for x in xs_])
        names = VGroup(*[label(n, size=26).next_to(t, UP, buff=0.18) for (_, n, _), t in zip(years, ticks)])
        subs = VGroup(*[label(s, size=22, color=GRAY).next_to(t, DOWN, buff=0.2) for (_, _, s), t in zip(years, ticks)])
        with self.narrate("The method was first published by Linnainmaa in nineteen seventy, applied to "
                          "networks by Werbos, and made famous by Rumelhart, Hinton and Williams in "
                          "nineteen eighty six.") as beat:
            self.play(Create(tl), run_time=beat.until("Linnainmaa", offset=-0.2, min_time=0.6))
            for i, word in enumerate(("Linnainmaa", "Werbos", "Rumelhart")):
                beat.wait_until(word, offset=-0.15)
                self.play(FadeIn(ticks[i], scale=1.5), FadeIn(names[i], shift=0.1 * UP),
                          FadeIn(subs[i]), run_time=0.7)
            beat.wait_until("eighty", offset=-0.2)
            self.play(flag(names[2]), run_time=0.8)

        # 20 --------------------------------------------------------------- Kaplan
        kap = MathTex(r"\text{compute per token}", r"\approx", "2N", "+", "4N", "=", "6N", font_size=44)
        kap[2].set_color(BLUE)
        kap[4].set_color(RED)
        kap.move_to([0.0, -2.2, 0])
        cite = citation("Kaplan et al., 2020 · Scaling Laws for Neural Language Models · arXiv")
        with self.narrate("Today, the standard compute budget for a large language model counts six "
                          "operations per weight per token: two forward, four backward.") as beat:
            self.play(FadeOut(VGroup(tl, ticks, names, subs)), run_time=0.6)
            self.play(Write(kap[0:2]), FadeIn(cite), run_time=beat.until("six", offset=-0.2, min_time=0.8))
            self.play(TransformFromCopy(head2[0][0], kap[6]), FadeIn(kap[5]), run_time=0.9)
            beat.wait_until("two forward", offset=-0.2)
            self.play(TransformFromCopy(cmp_b[1], kap[2]), FadeIn(kap[3]), run_time=0.8)
            beat.wait_until("four", offset=-0.2)
            self.play(TransformFromCopy(cmp_b[3], kap[4]), run_time=beat.remaining(0.8))

        # 21 --------------------------------------------------------------- landing
        ratio = MathTex(r"\frac{1{,}000{,}001}{3}", r"\approx", r"333{,}000", font_size=44)
        ratio[0].set_color(PURPLE)
        ratio.move_to([0.0, -2.35, 0])
        with self.narrate("So if you guessed a million, you were off by about three hundred thousand "
                          "times. The loss can tell every weight its share of the blame in one trip back.") as beat:
            self.play(FadeOut(kap), FadeOut(cite),
                      *[g.animate.set_stroke(DIM, width=1.4, opacity=1) for g in net2.gaps],
                      run_time=beat.until("million", offset=-0.2, min_time=0.8))
            self.play(TransformFromCopy(VGroup(cmp_n[1], cmp_b[4]), ratio[0]), run_time=beat.until("off", offset=-0.1, min_time=0.9))
            self.play(Write(ratio[1:]), run_time=beat.until("The loss", offset=-0.2, min_time=0.8))
            self.play(Indicate(net2.err, color=RED, scale_factor=1.15), run_time=0.6)
            self.play(LaggedStart(*[g.animate.set_stroke(RED, width=1.8, opacity=0.75)
                                    for g in reversed(net2.gaps)], lag_ratio=0.3),
                      run_time=beat.remaining(1.5), rate_func=LINEAR)
        self.end_card()
