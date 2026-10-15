"""Sample Space visual identity + a few helpers every episode needs.

Follows videos/BAR.md §5.  Import with ``from sample_space.style import *`` (or use the
re-exports in ``sample_space``).  Importing this module sets the series background.

Colour = meaning.  Use the semantic names, never raw hex:
    BLUE    primary quantity / the thing being studied
    YELLOW  focus, highlight, "look here", the changing term
    GREEN   positive / correct / signal       (never alone vs RED: add a label/shape)
    RED     negative / error / noise
    PURPLE  a second data series, only if needed
    INK     text;  GRAY  axes, secondary text;  DIM  grid lines, de-emphasised context
"""
from __future__ import annotations

import logging
import math
import re

import numpy as np
from manim import (DOWN, LEFT, ORIGIN, RIGHT, UP, UL, Axes, Create, DecimalNumber, FadeIn,
                   FadeOut, Indicate, Line, MathTex, SurroundingRectangle, Tex, Text,
                   AnimationGroup, VGroup, VMobject, config, rate_functions)

log = logging.getLogger("sample_space.style")

# --------------------------------------------------------------------------- colour
BG = "#14161B"          # one flat, very dark slate for the whole series (not pure black)
INK = "#ECE9E2"         # warm off-white text, 14.9:1 on BG
GRAY = "#8B939E"        # axes, secondary labels, 5.8:1
DIM = "#4A5059"         # grid lines, dimmed context (not for text)
BLUE = "#5AA9E6"        # primary                       7.1:1
YELLOW = "#F5C451"      # accent / focus               11.1:1
GREEN = "#6CC58B"       # positive                      8.6:1
RED = "#EF6F61"         # negative                      6.1:1
PURPLE = "#B394E8"      # spare second series           7.2:1
PALETTE = {"BLUE": BLUE, "YELLOW": YELLOW, "GREEN": GREEN, "RED": RED, "PURPLE": PURPLE,
           "INK": INK, "GRAY": GRAY, "DIM": DIM}
DIM_OPACITY = 0.3       # BAR: de-emphasised context at 25-40 % opacity, not deleted

# --------------------------------------------------------------------------- type
SERIF = "CMU Serif"     # matches LaTeX Computer Modern: all prose, titles, labels
SANS = "Inter"          # optional: tables / code-ish UI labels only. Don't mix casually.

# Text (Pango) font sizes. BAR §5 minimums: primary >= 26, ticks/citations >= 18.
TITLE = 46
HEADING = 38
BODY = 32
LABEL = 28
SMALL = 22              # tick labels, citations, footnotes (never below 18)
# MathTex font sizes. BAR §5: main equation 40-60, primary >= 36, ticks >= 26.
EQ = 52
MATH = 40
MATH_SMALL = 30

# --------------------------------------------------------------------------- layout
FRAME_W, FRAME_H = 14.222, 8.0
SAFE_X = 6.4            # all text within x in [-6.4, 6.4]
SAFE_TOP = 3.6          # ... and y <= 3.6
SAFE_BOTTOM = -3.6      # absolute floor for any text
CONTENT_BOTTOM = -3.2   # nothing essential below this (captions / player bar)
SAFE_WIDTH = 2 * SAFE_X
CONTENT_HEIGHT = SAFE_TOP - CONTENT_BOTTOM
MIN_GAP = 0.15          # >= 0.15 units between text and any other object

# --------------------------------------------------------------------------- motion
QUICK = 0.5             # minor moves 0.5-1 s; nothing tracked moves faster than 0.4 s
MOVE = 0.8
TRANSFORM = 1.5         # transforms 1-2.5 s
SLOW = 2.2
SMOOTH = rate_functions.smooth
EASE = rate_functions.ease_in_out_sine
LINEAR = rate_functions.linear          # only for time-like processes


def reading_time(text: str) -> float:
    """BAR hold time after text finishes drawing: max(1.5, 0.8 + 0.3 s/word)."""
    return max(1.5, 0.8 + 0.3 * len(re.findall(r"[\w'’-]+", text)))


def equation_hold(n_terms: int) -> float:
    """BAR hold time for an equation before it changes: 2 s + 0.4 s/term."""
    return 2.0 + 0.4 * n_terms


# --------------------------------------------------------------------------- defaults
def apply_defaults() -> None:
    """Series-wide Manim defaults. Called on import and again by NarratedScene.setup."""
    config.background_color = BG
    Text.set_default(font=SERIF, color=INK, font_size=BODY)
    MathTex.set_default(color=INK, font_size=MATH)
    Tex.set_default(color=INK, font_size=MATH)


apply_defaults()


# --------------------------------------------------------------------------- text
def text(s: str, size: float = BODY, color=INK, **kw) -> Text:
    """Serif prose/label text. kwargs pass through to Text (t2c, weight, slant...)."""
    kw.setdefault("font", SERIF)
    return Text(s, font_size=size, color=color, **kw)


def label(s: str, size: float = LABEL, color=INK, **kw) -> Text:
    return text(s, size=size, color=color, **kw)


def formula(*tex: str, size: float = MATH, color=INK, **kw) -> MathTex:
    """MathTex in series style. Pass terms separately to colour/transform them:
        formula(r"\\bar{x}", "=", r"\\frac{1}{n}\\sum x_i", size=EQ)"""
    return MathTex(*tex, font_size=size, color=color, **kw)


def wrap(s: str, max_width: float = SAFE_WIDTH, size: float = BODY, color=INK,
         align: str = "center", line_spacing: float = 0.25, max_words_per_line: int = 7,
         **kw) -> VGroup:
    """Greedy word-wrap into a VGroup of Text lines that never exceeds max_width.
    BAR: at most 7 words per block and 12 words of prose on screen - keep it short."""
    words = s.split()
    lines, cur = [], []
    for w in words:
        cand = " ".join(cur + [w])
        if cur and (len(cur) >= max_words_per_line or
                    Text(cand, font_size=size, font=kw.get("font", SERIF)).width > max_width):
            lines.append(" ".join(cur))
            cur = [w]
        else:
            cur.append(w)
    if cur:
        lines.append(" ".join(cur))
    g = VGroup(*[text(line, size=size, color=color, **kw) for line in lines])
    edge = {"center": ORIGIN, "left": LEFT, "right": RIGHT}[align]
    g.arrange(DOWN, buff=line_spacing * size / 32, aligned_edge=edge)
    return fit(g, width=max_width)


def fit(m: VMobject, width: float = SAFE_WIDTH, height: float = CONTENT_HEIGHT) -> VMobject:
    """Scale m down (never up) so it fits inside width x height."""
    s = min(1.0, width / max(m.width, 1e-6), height / max(m.height, 1e-6))
    if s < 1.0:
        m.scale(s)
    return m


def keep_in_safe(m: VMobject, bottom: float = CONTENT_BOTTOM) -> VMobject:
    """Shift m (after fitting) so its bounding box lies in the safe area."""
    fit(m, SAFE_WIDTH, SAFE_TOP - bottom)
    dx = max(0, -SAFE_X - m.get_left()[0]) - max(0, m.get_right()[0] - SAFE_X)
    dy = max(0, bottom - m.get_bottom()[1]) - max(0, m.get_top()[1] - SAFE_TOP)
    return m.shift(dx * RIGHT + dy * UP)


def title(s: str, size: float = TITLE, color=INK, **kw) -> VMobject:
    """Short heading at the top of the safe area. Use sparingly (no title+bullets!)."""
    m = wrap(s, size=size, color=color, **kw)
    return m.move_to(UP * (SAFE_TOP - 0.1 - m.height / 2))


def caption(s: str, size: float = BODY, color=INK, **kw) -> VMobject:
    """A short line near the bottom, kept above y = -3.2 (CONTENT_BOTTOM)."""
    m = wrap(s, size=size, color=color, **kw)
    return m.move_to(UP * (CONTENT_BOTTOM + 0.15 + m.height / 2))


def citation(s: str | None = None, *, author: str | None = None, year: int | str | None = None,
             venue: str | None = None, size: float = SMALL, color=GRAY) -> Text:
    """On-screen source, bottom-left above y = -3.2: "Author et al., Year · Venue".
    BAR: hold >= 3 s; every empirical claim needs one.
        citation("Muller et al., 2008 · J. Computer Assisted Learning")
        citation(author="Muller et al.", year=2008, venue="JCAL")"""
    if s is None:
        s = f"{author}, {year}" + (f" · {venue}" if venue else "")
    m = Text(s, font=SERIF, font_size=size, color=color)
    fit(m, width=SAFE_WIDTH * 0.75)
    return m.move_to([-SAFE_X + m.width / 2, CONTENT_BOTTOM + 0.08 + m.height / 2, 0])


# --------------------------------------------------------------------------- numbers
def live_number(tracker, decimals: int = 2, size: float = MATH, color=INK,
                prefix: str | None = None, suffix: str | None = None, **kw) -> VGroup:
    """A DecimalNumber that follows a ValueTracker, optionally with MathTex prefix/suffix:
        err = ValueTracker(0.31); lbl = live_number(err, 2, prefix=r"\\text{error} =")
        self.play(err.animate.set_value(0.12))"""
    num = DecimalNumber(tracker.get_value(), num_decimal_places=decimals, font_size=size,
                        color=color, **kw)
    parts = []
    if prefix:
        parts.append(MathTex(prefix, font_size=size, color=color))
    parts.append(num)
    if suffix:
        parts.append(MathTex(suffix, font_size=size, color=color))
    g = VGroup(*parts).arrange(RIGHT, buff=0.15)
    pre = parts[0] if prefix else None
    post = parts[-1] if suffix else None

    def upd(m):
        m.set_value(tracker.get_value())
        if pre is not None:
            m.next_to(pre, RIGHT, buff=0.15)
        if post is not None:
            post.next_to(m, RIGHT, buff=0.15)
    num.add_updater(upd)
    g.number = num
    return g


def nice_ticks(lo: float, hi: float, max_ticks: int = 6) -> tuple[float, float, float]:
    """A 1-2-5 step giving <= max_ticks labelled ticks between lo and hi."""
    span = max(hi - lo, 1e-9)
    raw = span / max(1, max_ticks - 1)
    mag = 10 ** math.floor(math.log10(raw))
    for m in (1, 2, 2.5, 5, 10):
        step = m * mag
        if span / step <= max_ticks - 1 + 1e-9:
            break
    return (math.floor(lo / step + 1e-9) * step, math.ceil(hi / step - 1e-9) * step, step)


# --------------------------------------------------------------------------- charts
def axes(x_range=(0, 10), y_range=(0, 1), x_length: float = 9.0, y_length: float = 5.0,
         x_label: str | None = None, y_label: str | None = None, numbers: bool = True,
         x_ticks=None, y_ticks=None, x_decimals: int | None = None, y_decimals: int | None = None,
         tips: bool = False, grid: bool = False, **kw) -> Axes:
    """Series-styled Axes.
    x_range/y_range: (lo, hi) -> a <=6-tick 1-2-5 step is chosen; or (lo, hi, step).
    x_ticks/y_ticks: explicit tick values (e.g. bar charts: x_range=(-0.6, 10.6),
        x_ticks=[0, 2, 4, 6, 8, 10] so the first/last bar doesn't cross the axis).
    Labels must carry quantity + unit, e.g. "height (cm)".  Returns Axes with
    .x_title / .y_title (added as submobjects) and .grid."""
    def resolve(r, ticks):
        if ticks is not None:
            return (r[0], r[1], 1.0), list(ticks)
        r = tuple(r) if len(r) == 3 else nice_ticks(*r)
        return r, None
    xr, xt = resolve(x_range, x_ticks)
    yr, yt = resolve(y_range, y_ticks)
    for name, r, t in (("x", xr, xt), ("y", yr, yt)):
        n = len(t) if t is not None else round((r[1] - r[0]) / r[2]) + 1
        if n > 7:
            log.warning("%s axis has %d ticks; BAR allows at most 6", name, n)

    def dec(r, t, d):
        if d is not None:
            return d
        step = r[2] if t is None else (min(np.diff(sorted(t))) if len(t) > 1 else 1.0)
        return max(0, -int(math.floor(math.log10(abs(step)) + 1e-9)))
    common = dict(color=GRAY, stroke_width=2.5, include_tip=tips, tick_size=0.06,
                  font_size=MATH_SMALL, line_to_number_buff=0.18)
    ax = Axes(x_range=xr, y_range=yr, x_length=x_length, y_length=y_length,
              axis_config=common,
              x_axis_config={"include_ticks": xt is None,
                             "decimal_number_config": {"num_decimal_places": dec(xr, xt, x_decimals),
                                                       "color": GRAY}},
              y_axis_config={"include_ticks": yt is None,
                             "decimal_number_config": {"num_decimal_places": dec(yr, yt, y_decimals),
                                                       "color": GRAY}},
              **kw)
    for axis, t in ((ax.x_axis, xt), (ax.y_axis, yt)):
        if t is not None:
            axis.ticks = VGroup(*[axis.get_tick(v) for v in t])
            axis.add(axis.ticks)
        if numbers:
            axis.add_numbers(x_values=t, font_size=MATH_SMALL, color=GRAY,
                             **({"excluding": []} if t is not None else {}))
    ax.grid = VGroup()
    if grid:
        ys = yt if yt is not None else np.arange(yr[0] + yr[2], yr[1] + 1e-9, yr[2])
        for y in ys:
            ax.grid.add(Line(ax.c2p(xr[0], y), ax.c2p(xr[1], y), stroke_width=1, color=DIM))
        ax.add_to_back(ax.grid)
    ax.x_title = ax.y_title = None
    if x_label:
        ax.x_title = Text(x_label, font=SERIF, font_size=LABEL, color=GRAY)
        ax.x_title.next_to(ax.x_axis.numbers if numbers else ax.x_axis, DOWN, buff=0.18)
        ax.x_title.align_to(ax.x_axis.get_right(), RIGHT)
        ax.add(ax.x_title)
    if y_label:
        ax.y_title = Text(y_label, font=SERIF, font_size=LABEL, color=GRAY)
        ax.y_title.next_to(ax.y_axis.get_top(), UP, buff=0.22)
        ax.y_title.align_to(ax.y_axis.numbers if numbers else ax.y_axis, LEFT)
        ax.add(ax.y_title)
    return ax


def dots(ax: Axes, xs, ys, color=BLUE, radius: float = 0.06, opacity: float = 1.0) -> VGroup:
    """Scatter points on axes (radius >= 0.05 per BAR). Fine up to ~2000 points."""
    from manim import Dot
    return VGroup(*[Dot(ax.c2p(x, y), radius=radius, color=color, fill_opacity=opacity)
                    for x, y in zip(xs, ys)])


# --------------------------------------------------------------------------- emphasis
def underline(m: VMobject, color=YELLOW, buff: float = 0.1, stroke_width: float = 4) -> Line:
    """Line under m; animate with Create(underline(m))."""
    return Line(m.get_corner(DOWN + LEFT) + DOWN * buff, m.get_corner(DOWN + RIGHT) + DOWN * buff,
                color=color, stroke_width=stroke_width)


def box(m: VMobject, color=YELLOW, buff: float = 0.15, stroke_width: float = 3) -> SurroundingRectangle:
    """Rounded highlight rectangle around m; animate with Create(box(m))."""
    return SurroundingRectangle(m, color=color, buff=buff, corner_radius=0.08,
                                stroke_width=stroke_width)


def flag(m: VMobject, color=YELLOW, run_time: float = 0.8):
    """Briefly flag a changed term (BAR: <= 1 s). Returns an animation."""
    return Indicate(m, color=color, scale_factor=1.08, run_time=min(run_time, 1.0))


def dim(*ms: VMobject, opacity: float = DIM_OPACITY, run_time: float = MOVE):
    """De-emphasise context (fade to 30 %) instead of deleting it. Returns an animation."""
    return AnimationGroup(*[m.animate.set_opacity(opacity) for m in ms], run_time=run_time)


def undim(*ms: VMobject, run_time: float = MOVE):
    return AnimationGroup(*[m.animate.set_opacity(1.0) for m in ms], run_time=run_time)


# --------------------------------------------------------------------------- brand
def wordmark(scale: float = 1.0) -> VGroup:
    """Ω  Sample Space  (Ω = the sample space of a probability model)."""
    omega = MathTex(r"\Omega", font_size=72 * scale, color=BLUE)
    name = Text("Sample Space", font=SERIF, font_size=44 * scale, color=INK)
    g = VGroup(omega, name).arrange(RIGHT, buff=0.3 * scale)
    omega.align_to(name[0], DOWN)          # sit on the baseline of "S", not the descender
    return g


def end_card(episode: int | None = None, title_text: str | None = None) -> VGroup:
    """Quiet closing card: wordmark plus "Episode N · Title" in gray."""
    wm = wordmark()
    parts = [wm]
    sub = []
    if episode is not None:
        sub.append(f"Episode {episode}")
    if title_text:
        sub.append(title_text)
    if sub:
        s = Text("  ·  ".join(sub), font=SERIF, font_size=SMALL + 2, color=GRAY)
        parts.append(fit(s, width=SAFE_WIDTH * 0.8))
    return VGroup(*parts).arrange(DOWN, buff=0.35).move_to(ORIGIN)


__all__ = [
    # colours
    "BG", "INK", "GRAY", "DIM", "BLUE", "YELLOW", "GREEN", "RED", "PURPLE", "PALETTE",
    "DIM_OPACITY",
    # type
    "SERIF", "SANS", "TITLE", "HEADING", "BODY", "LABEL", "SMALL", "EQ", "MATH", "MATH_SMALL",
    # layout
    "FRAME_W", "FRAME_H", "SAFE_X", "SAFE_TOP", "SAFE_BOTTOM", "CONTENT_BOTTOM", "SAFE_WIDTH",
    "CONTENT_HEIGHT", "MIN_GAP",
    # motion
    "QUICK", "MOVE", "TRANSFORM", "SLOW", "SMOOTH", "EASE", "LINEAR", "reading_time",
    "equation_hold",
    # helpers
    "apply_defaults", "text", "label", "formula", "wrap", "fit", "keep_in_safe", "title",
    "caption", "citation", "live_number", "nice_ticks", "axes", "dots", "underline", "box",
    "flag", "dim", "undim", "wordmark", "end_card",
]
