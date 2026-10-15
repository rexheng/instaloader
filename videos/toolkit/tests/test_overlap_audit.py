"""Unit tests for sample_space.overlap_audit: known overlaps and known-clean layouts,
checked on mobjects directly (no rendering; ~30 s, mostly LaTeX).  Run:

    PYTHONPATH=videos/toolkit python3 videos/toolkit/tests/test_overlap_audit.py

Render-level check (time ranges, warnings, narration.json):
    videos/toolkit/render.sh --preview videos/toolkit/tests/audit_synthetic_scene.py \
        AuditSynthetic /tmp/audit_synth/out.mp4
"""
import os
import sys
import tempfile
import time

os.chdir(tempfile.mkdtemp(prefix="ss_audit_test_"))      # manim writes media/Tex here
from manim import *                                     # noqa
from sample_space import *                              # noqa
from sample_space.overlap_audit import audit, flatten_many, seg_box_gaps

def seg_box_gap(p0, p1, box):
    return float(seg_box_gaps(p0, p1, box).min())

def flatten(p):
    a, b, _ = flatten_many([p])
    return a, b


FAILS = []


def check(name, mobs, expect_kinds=(), allowed_pairs=(), show=False):
    issues = [i for i in audit(mobs, allowed_pairs=allowed_pairs) if not i.allowed]
    kinds = sorted(i.kind for i in issues)
    ok = sorted(expect_kinds) == kinds
    status = "ok " if ok else "FAIL"
    print(f"[{status}] {name}: {kinds or 'clean'}")
    if not ok or show:
        for i in issues:
            print("       ", i.kind, i.describe())
    if not ok:
        FAILS.append(name)
    return issues


# ---------------------------------------------------------------- geometry primitives
p0 = np.array([[-1.0, 0.0]]); p1 = np.array([[1.0, 0.0]])
assert abs(seg_box_gap(p0, p1, (-0.1, 0.2, 0.1, 0.4)) - 0.2) < 1e-9
assert seg_box_gap(p0, p1, (-0.1, -0.1, 0.1, 0.1)) < 0
assert abs(seg_box_gap(p0, p1, (1.3, 0.4, 2, 1)) - 0.5) < 1e-9          # corner distance
c = Circle(radius=1)
a, b = flatten(c.points[:, :2])
assert len(a) > 16 and abs(np.hypot(*a.T).mean() - 1) < 0.01

# ---------------------------------------------------------------- clean layouts
lab = Text("label", font_size=28)
check("label inside its own box", [lab, SurroundingRectangle(lab, buff=0.15)])
check("label inside a tight highlight box (buff 0.06)", [lab, SurroundingRectangle(lab, buff=0.06)])
panel = RoundedRectangle(width=3, height=1.2, corner_radius=0.2, fill_color=BG, fill_opacity=1,
                         stroke_color=GRAY)
check("label centred in a filled panel", [VGroup(panel, Text("legend", font_size=26))])

edge = Line(LEFT * 2, RIGHT * 2, color=GRAY, stroke_width=3)
sq = Square(0.26, stroke_width=0, fill_color=YELLOW, fill_opacity=1)
tok = VGroup(sq, MathTex("4", font_size=26, color=BG).move_to(sq))
check("token (opaque square + digit) on a graph edge", [edge, tok])
tok2 = tok.copy().shift(RIGHT * 0.9)
check("two tokens on one edge", [edge, tok, tok2])

ax = axes((0, 10), (0, 1), x_label="heads (count)", y_label="probability")
check("style.axes, default placement (title in caption zone)", [ax], ["caption-zone"])
check("style.axes with numbers and titles", [ax.copy().shift(UP * 0.3)])
ax2 = axes((-0.6, 10.6), (0, 0.25), x_ticks=[0, 2, 4, 6, 8, 10], x_length=8.6, y_length=4.0,
           x_label="heads (count)", y_label="probability").move_to(LEFT * 1.6 + DOWN * 0.15)
bars = VGroup(*[Rectangle(width=0.4, height=0.5 + 0.2 * k, stroke_width=0, fill_color=BLUE,
                          fill_opacity=0.9).move_to(ax2.c2p(k, 0), aligned_edge=DOWN) for k in range(11)])
tag = MathTex("0.117", font_size=30, color=YELLOW).next_to(bars[7], UP, buff=0.15)
check("demo-style bar chart + tag at buff 0.15", [ax2, bars, tag])
plain_ax = Axes(x_range=[0, 5, 1], y_range=[0, 3, 1], x_length=6, y_length=4).add_coordinates()
check("manim Axes.add_coordinates()", [plain_ax])
nl = NumberLine(x_range=[0, 10, 1], include_numbers=True)
check("manim NumberLine with numbers", [nl])

d = Dot(ORIGIN, radius=0.06)
check("label next_to dot (buff 0.2)", [d, Text("A", font_size=28).next_to(d, UP, buff=0.2)])
num, den = MathTex("2", font_size=48), MathTex("7", font_size=48)
bar = Line(LEFT * 0.26, RIGHT * 0.26, stroke_width=3.2)
frac = VGroup(num, bar, den).arrange(DOWN, buff=0.09)
check("fraction from MathTex + Line bar (buff 0.09)", [frac])
lbl = Text("on the line", font_size=26)
lbl.add_background_rectangle(color=BG, opacity=1, buff=0.05)
check("text with opaque background rectangle on a line", [Line(LEFT * 3, RIGHT * 3), lbl])
disk = Circle(radius=0.42, stroke_color=YELLOW, stroke_width=3, fill_color=YELLOW, fill_opacity=0.18)
check("coin: letter inside a translucent disk", [VGroup(disk, Text("H", font_size=28).move_to(disk))])
row = VGroup(MathTex("2^{10}"), MathTex("="), MathTex("1024")).arrange(RIGHT, buff=0.1)
check("equation row of separate MathTex (buff 0.1)", [row])
w = wrap("a wrapped caption that runs over two lines easily", max_width=4)
check("wrap() paragraph", [w])
t = Text("underlined", font_size=32)
check("style.underline(t)", [t, underline(t)])
check("style.box(t)", [t, box(t)])
check("live_number group", [live_number(ValueTracker(0.31), 2, prefix=r"\text{error} =")])
ghost = Line(LEFT, RIGHT).set_opacity(0)
check("invisible line through text", [Text("ghost", font_size=28), ghost])
faint = Line(LEFT, RIGHT).set_stroke(opacity=0.03)
check("3% opacity line through text", [Text("ghost", font_size=28), faint])
hidden = Text("off", font_size=28).set_opacity(0)
check("invisible text on a line", [hidden, Line(LEFT, RIGHT)])
wm = wordmark()
check("wordmark / end card", [end_card(3, "Some title")])
cit = citation("Muller et al., 2008 · JCAL")
check("citation()", [cit])
cap = caption("A short caption line")
check("caption()", [cap])
eq = MathTex(r"P(7)", "=", r"\frac{120}{1024}", r"\approx", r"0.117", font_size=52)
check("multi-part MathTex", [eq])
br = Brace(eq, DOWN)
check("Brace + get_text label", [eq, br, br.get_text("sum")])
arrow = Arrow(LEFT * 3, LEFT * 0.4, buff=0)
check("arrow ending 0.2 from a label", [arrow, Text("here", font_size=28).next_to(LEFT * 0.4, RIGHT, buff=0.2)])
ell = Ellipse(width=4, height=2.4, color=BLUE)
check("label well inside an ellipse", [ell, Text("A", font_size=30)])

# ---------------------------------------------------------------- known defects
sue = Text("Sue", font_size=26).move_to(UP * 0.5)
tokd = tok.copy().move_to(sue.get_corner(DR) + DOWN * 0.05 + LEFT * 0.04)
check("token covering the 'e' of 'Sue'", [sue, tokd], ["overlap"])
axis_line = Line(LEFT * 4, RIGHT * 4, color=GRAY)
l27 = MathTex(r"\frac{2}{7}", font_size=32).move_to(RIGHT * 0.5 + DOWN * 0.1)
check("rung label '2/7' crossing an x-axis line", [axis_line, l27], ["overlap"])
ax3 = axes((0, 60), (40, 100), x_length=8, y_length=4)
l14 = MathTex(r"\frac{1}{4}", font_size=32).next_to(ax3.c2p(25, 40), UP, buff=0.0)
check("label resting on an axes x-axis", [ax3, l14], ["overlap"])
on_ell = Text("B", font_size=30).move_to(ell.point_from_proportion(0.1))
check("label sitting on an ellipse's stroke", [ell, on_ell], ["overlap"])
check("label next_to dot buff 0.08", [d, Text("A", font_size=28).next_to(d, UP, buff=0.08)], ["clearance"])
t1 = Text("first", font_size=30); t2 = Text("second", font_size=30).next_to(t1, RIGHT, buff=-0.1)
check("two texts overlapping", [t1, t2], ["overlap"])
t3 = Text("second", font_size=30).next_to(t1, RIGHT, buff=0.08)
check("two texts side by side 0.08 apart (one line)", [t1, t3])
t5 = Text("below", font_size=30).next_to(t1, DOWN, buff=0.08)
check("two labels stacked 0.08 apart", [t1, t5], ["clearance"])
t6 = Text("diag", font_size=30).next_to(t1, DR, buff=0.06)
check("two labels diagonal 0.06 apart", [t1, t6], ["clearance"])
frag = VGroup(*[MathTex(x, font_size=40) for x in ["(", "0.44", "/", "1.14", ")^2"]]).arrange(RIGHT, buff=0.04)
check("formula fragments as separate MathTex in a row", list(frag))
check("text outside safe area", [Text("far right", font_size=30).move_to(RIGHT * 6.5)], ["safe-area"])
check("text in caption zone", [Text("low", font_size=30).move_to(DOWN * 3.35)], ["caption-zone"])
near = Text("near", font_size=28)
check("line 0.1 below text", [near, Line(LEFT * 2, RIGHT * 2).next_to(near, DOWN, buff=0.1)], ["clearance"])
lab2 = Text("crossed", font_size=28)
box_thru = Rectangle(width=lab2.width + 0.4, height=lab2.height * 0.5)
check("box whose stroke passes through its label", [lab2, box_thru], ["overlap"])
g_edge = Line(LEFT * 2 + DOWN, RIGHT * 2 + UP)
check("graph edge through a node label", [g_edge, Text("Pam", font_size=26)], ["overlap"])
curve = FunctionGraph(lambda x: 0.3 * x ** 2, x_range=[-3, 3])
check("curve through a label", [curve, Text("peak", font_size=26).move_to([1, 0.3, 0])], ["overlap"])
own_group = VGroup(Line(LEFT, RIGHT), Text("on it", font_size=26))
check("line through a label in the label's own group", [own_group], ["overlap"])
tok3 = tok.copy().move_to(ORIGIN); tok4 = tok.copy().move_to(RIGHT * 0.2)
check("two tokens overlapping each other", [tok3, tok4], ["overlap"])
dots = VGroup(*[Dot([x, 0.05, 0], radius=0.06) for x in np.linspace(-0.5, 0.5, 5)])
check("dots under a label", [dots, Text("cloud", font_size=28)], ["overlap"])

lbg = Text("bg label", font_size=26); lbg.add_background_rectangle(color=BG, opacity=1, buff=0.05)
other = Text("neighbour", font_size=26).next_to(lbg, RIGHT, buff=-0.05)
check("bg-rect label overlapping another label", [lbg, other], ["overlap"])

hand_ax = NumberLine(x_range=[0, 10, 2], length=6, include_numbers=False).shift(DOWN)
hand_lbls = VGroup(*[MathTex(str(v), font_size=30).next_to(hand_ax.n2p(v), DOWN, buff=0.17) for v in range(0, 11, 2)])
check("hand-placed tick labels 0.11 under a NumberLine's ticks", [hand_ax, hand_lbls])
check("rung label crossing a NumberLine", [hand_ax, MathTex(r"\frac{2}{7}", font_size=32).move_to(hand_ax.n2p(5))], ["overlap"])
faint_curve = FunctionGraph(lambda x: 0.1 * x, x_range=[-2, 2]).set_stroke(opacity=0.09)
check("label 0.08 from a 9%-opacity curve", [faint_curve, Text("w", font_size=28).move_to([0, 0.3, 0])])
check("label crossing a 9%-opacity curve", [faint_curve, Text("w", font_size=28).move_to([0, 0.05, 0])], ["overlap"])

check("text parked fully off-frame", [Text("parked", font_size=28).move_to(RIGHT * 9)])
check("text half off the right edge", [Text("clipped", font_size=28).move_to(RIGHT * 7.1)], ["safe-area"])

n16 = DecimalNumber(16, num_decimal_places=0, font_size=40); fbar = Line(LEFT * 0.4, RIGHT * 0.4, stroke_width=3)
n16.next_to(fbar, UP, buff=0.1)
check("ungrouped fraction: number 0.1 over a Line bar", [n16, fbar])
tick = Line(UP * 0.07, DOWN * 0.07, stroke_width=2).shift(RIGHT * 2)
check("hand-made tick 0.08 from its label", [tick, MathTex("3", font_size=30).next_to(tick, DOWN, buff=0.08)])
longl = Line(LEFT * 3, RIGHT * 3)
check("label 0.08 above a long line", [longl, Text("tight", font_size=28).next_to(longl, UP, buff=0.08)], ["clearance"])
check("label crossing a short tick", [tick, MathTex("3", font_size=30).move_to(tick)], ["overlap"])

dup = MathTex("3", font_size=40)
check("exact duplicate stacked on itself (TransformFromCopy leftover)", [dup, dup.copy()])

rad = MathTex(r"\sqrt{N}", font_size=48); nn = rad.copy()
rad[0][2].set_opacity(0)                    # rad shows only the radical, nn only the N
nn[0][0].set_opacity(0); nn[0][1].set_opacity(0)
check("radicand N under a separate radical (formula split by a transform)", [rad, nn])
tint = Rectangle(width=3, height=1, stroke_width=0, fill_color=GRAY, fill_opacity=0.12)
check("label half over a 12% tint band", [tint, Text("on tint", font_size=28).move_to(tint.get_top())])

dimmed_tick = Line(UP * 0.07, DOWN * 0.07, stroke_width=2).shift(LEFT * 2).set_opacity(0.35)
check("dimmed (set_opacity) tick 0.08 from its label", [dimmed_tick, MathTex("0", font_size=30).next_to(dimmed_tick, DOWN, buff=0.08)])

wbar = Line(LEFT * 0.9, RIGHT * 0.9, stroke_width=3)
check("small numerator 0.085 under a wide fraction bar", [wbar, MathTex(r"\sum k", font_size=36).next_to(wbar, DOWN, buff=0.085).shift(LEFT * 0.4)])
beam = Line(LEFT * 1.9, RIGHT * 1.9, stroke_width=3)
check("label 0.08 under a 3.8-long beam", [beam, MathTex("2.5", font_size=36).next_to(beam, DOWN, buff=0.08)], ["clearance"])

sup = MathTex(r"3.7\ \text{hits/km}^2", font_size=36)
corner_dot = Dot(sup.get_corner(UL) + RIGHT * 0.12 + UP * 0.03, radius=0.06)
check("dot at a box corner raised by a superscript (ink 0.1 away)", [sup, corner_dot], ["clearance"])

# ---------------------------------------------------------------- exemptions
lab_a = Text("allowed", font_size=28); line_a = Line(LEFT * 2, RIGHT * 2)
check("allow_overlap(m)", [allow_overlap(Text("allowed", font_size=28)), line_a])
iss = audit([lab_a, line_a], allowed_pairs=[(lab_a, line_a, "strikethrough on purpose")])
assert iss and all(i.allowed == "strikethrough on purpose" for i in iss), iss
print("[ok ] allow pair returns the issue marked allowed")

# ---------------------------------------------------------------- moving camera
from sample_space.overlap_audit import _camera_transform  # noqa
class FakeFrame:
    def __init__(s, c, w, h): s._c, s.width, s.height = np.array(c), w, h
    def get_center(s): return s._c
class FakeCam:
    frame = FakeFrame([2, 0, 0], config.frame_width / 2, config.frame_height / 2)
txt = Text("zoomed", font_size=20).move_to([2 + 3.4, 0, 0])   # 3.4 units right of centre -> 6.8 on screen
iss = audit([txt], camera=FakeCam())
assert any(i.kind == "safe-area" for i in iss), iss
print("[ok ] zoomed camera maps text to screen space")

# ---------------------------------------------------------------- speed
big = VGroup(*[Dot([x, y, 0], radius=0.06) for x in np.linspace(-6, 6, 50) for y in np.linspace(-3, 3, 40)])
labels = VGroup(*[Text(f"L{i}", font_size=24).move_to([-6 + i * 0.6, 3.3, 0]) for i in range(20)])
scene_mobs = [big, labels, ax2, bars, tag, eq.copy().to_edge(DOWN)]
audit(scene_mobs)
t0 = time.perf_counter()
for _ in range(10):
    audit(scene_mobs)
dt = (time.perf_counter() - t0) / 10
print(f"[info] audit of 2000 dots + 40 texts + axes: {1000 * dt:.1f} ms")
t0 = time.perf_counter()
small = [ax2, bars, tag, eq.copy().to_edge(DOWN), tok, edge]
for _ in range(50):
    audit(small)
print(f"[info] audit of a typical frame: {1000 * (time.perf_counter() - t0) / 50:.1f} ms")

print("FAILS:", FAILS or "none")
sys.exit(1 if FAILS else 0)
