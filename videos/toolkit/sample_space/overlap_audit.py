"""Geometric overlap audit (BAR §5): text keeps >= 0.15 units from every other object and
stays inside the safe area.

NarratedScene runs it automatically after every play() and every wait()/hold(), merges
repeated findings into time ranges, prints ``[sample_space] WARNING overlap ...`` lines and
stores them in narration.json["layout_audit"].  It can also be called directly:

    from sample_space.overlap_audit import audit
    for issue in audit(scene.mobjects):
        print(issue.kind, issue.describe())

For every visible text-like object (Text, MarkupText, each Paragraph line, each part of a
MathTex/Tex, SingleStringMathTex, DecimalNumber/Integer) it measures:
  * other text: box-to-box distance (refined to glyph boxes, then to the real glyph
    outlines, before two texts are called touching);
  * every other visible VMobject (lines, axes, curves, arrows, graph edges, ellipses, dots,
    bars, panels): the distance from its real path (Bezier curves flattened into short
    chords) to the text's bounding box, minus half the stroke width (a touch is re-checked
    against each glyph's box);
  * the safe area x in [-6.4, 6.4], y in [-3.6, 3.6], and the caption zone below y = -3.2.
Kinds: "overlap" (gap < 0.02: touching or crossing, a critic's cap 7), "clearance"
(closer than 0.15 - 0.02 tolerance), "safe-area", "caption-zone".
With sizes=True (NarratedScene passes it) it also measures every readable text's cap height
in 1080p pixels (style.cap_height_px, x camera zoom): "text-size" = under BAR's 24 px floor
for any text (ticks and citations included); "small-label" (advisory) = 24-26 px text that
is not an axis number or a citation (BAR: labels >= 34 px).  Critics measured and docked
20-26 px labels in 8 of the 12 episodes in review rounds 5-6.

Held only to "must not touch" (instead of 0.15), to keep false positives near zero:
  * a closed shape that fully contains the text (a label in its box, a digit in its token,
    a name inside an ellipse) - a panel;
  * the text's own small group (a fraction's bar, a token's square), an axis' numbers vs
    its ticks, style.underline()/style.box() of that text;
  * axis lines and ticks (NumberLine), short tick marks and fraction bars drawn as Lines;
  * text beside text on the same line (fragments of one formula), stray formula glyphs;
  * context fainter than 20 %.
Ignored: objects below 5 % opacity, faint fills without a stroke, text parked fully
off-frame, exact duplicates stacked on themselves, anything drawn beneath an opaque panel
(fill >= 75 %) that holds the text (a graph edge running under a token), mobjects marked
allow_overlap(m), and pairs given to scene.allow_overlap(a, b, reason) (reported as allowed).

Pure numpy on the current state; it never modifies a mobject.  Callers wrap it in
try/except so that it can never break a render.
"""
from __future__ import annotations

import math
import weakref
from dataclasses import dataclass

import numpy as np
from manim import (BackgroundRectangle, DecimalNumber, MarkupText, NumberLine, Paragraph,
                   SingleStringMathTex, Text, VMobject, config)
from manim.mobject.svg.svg_mobject import VMobjectFromSVGPath

try:                                         # Manim >= 0.19: MathTex parts are MathTexPart
    from manim.mobject.text.tex_mobject import MathTexPart
except ImportError:                          # pragma: no cover
    MathTexPart = None

from . import style

CLEARANCE = style.MIN_GAP        # BAR §5: >= 0.15 units between text and anything else
TOUCH = 0.02                     # panels and the text's own group: flag only when touching
MIN_OPACITY = 0.05               # below this an object is invisible
FAINT = 0.2                      # fainter context only counts when it actually touches text
OPAQUE = 0.75                    # a panel at least this opaque hides what is beneath it
LOCAL_PAD = 1.0                  # an "own group" must fit in the text box grown by this
SAFE_TOL = 0.02
TOL = 0.02                       # measurement tolerance: buff=0.15 minus half a stroke is fine
CURVE_STEPS = 8                  # chords per curved Bezier segment (error < 0.5 % of radius)
TEXT_FLOOR_PX = 24.0             # BAR §5: ticks and citations >= 24 px cap height
SMALL_LABEL_PX = 26.0            # labels the critics flagged were 20-26 px (BAR: >= 34 px)
READABLE = 0.5                   # size checks apply to text at least this opaque
SIZE_KINDS = ("text-size", "small-label")

TEXT_TYPES = (Text, MarkupText, Paragraph, SingleStringMathTex, DecimalNumber) + \
    ((MathTexPart,) if MathTexPart is not None else ())

# decoration -> the mobject it decorates (style.underline / style.box register here)
_DECORATES: "weakref.WeakKeyDictionary" = weakref.WeakKeyDictionary()


def mark_decoration(deco, target):
    """Register `deco` (an underline, a highlight box ...) as part of `target`: the audit
    then only requires that it does not touch target's text, not the full clearance."""
    try:
        _DECORATES[deco] = target
    except TypeError:
        pass
    return deco


# ---------------------------------------------------------------------------- issues
@dataclass
class Issue:
    kind: str                 # "overlap" | "clearance" | "safe-area" | "caption-zone" |
                              # "text-size" | "small-label" (gap = cap height in px)
    a: str                    # the text
    b: str                    # the other object ("" for safe-area / caption-zone)
    gap: float                # units; negative = overlapping by that much
    need: float               # the clearance that applied
    a_pos: tuple
    b_pos: tuple | None = None
    detail: str = ""
    allowed: str | None = None    # reason, when suppressed by scene.allow_overlap(a, b, reason)

    @property
    def key(self) -> tuple:
        """Identity used to merge the same finding across consecutive checks."""
        return (self.kind if self.kind in ("safe-area", "caption-zone") + SIZE_KINDS else "pair",
                self.a, self.b)

    def describe(self) -> str:
        if self.kind in ("safe-area", "caption-zone") + SIZE_KINDS:
            return f"{self.a} @{_fmt_pos(self.a_pos)} {self.detail}"
        rel = (f"overlapping by {-self.gap:.2f}" if self.gap < -0.005 else
               "touching" if self.gap < TOUCH else f"gap {self.gap:.2f}")
        need = "must not touch" if self.need <= TOUCH else f"need >= {self.need:.2f}"
        return (f"{self.a} @{_fmt_pos(self.a_pos)} vs {self.b} @{_fmt_pos(self.b_pos)}: "
                f"{rel} ({need})")


def _fmt_pos(p) -> str:
    return "(?)" if p is None else f"({p[0]:+.2f}, {p[1]:+.2f})"


# ---------------------------------------------------------------------------- naming
def _short(s: str, n: int = 28) -> str:
    s = " ".join(str(s).split())
    return s if len(s) <= n else s[: n - 1] + "…"


def text_content(m) -> str | None:
    try:
        if isinstance(m, (Text, MarkupText)):
            return getattr(m, "original_text", None) or getattr(m, "text", "")
        if isinstance(m, Paragraph):
            return " / ".join(m.lines_text.text.split("\n"))
        if isinstance(m, DecimalNumber):
            return f"{m.get_value():.{getattr(m, 'num_decimal_places', 2)}f}"
        return getattr(m, "tex_string", None)
    except Exception:
        return None


def _text_name(root, part, i) -> str:
    content = None
    if part is not root:
        content = text_content(part)
        if content is None:
            try:
                content = (root.tex_strings[i] if hasattr(root, "tex_strings")
                           else root.lines_text.text.split("\n")[i])
            except Exception:
                content = None
    if content is None:
        content = text_content(root) or ""
    cls = "MathTex" if MathTexPart is not None and isinstance(root, MathTexPart) else type(root).__name__
    return f"{cls} '{_short(content)}'"


def _axis_tag(nl, anc) -> str:
    for a in anc:
        if getattr(a, "x_axis", None) is nl:
            return " (x-axis)"
        if getattr(a, "y_axis", None) is nl:
            return " (y-axis)"
    return ""


# ---------------------------------------------------------------------------- geometry
def _alpha(rgbas) -> float:
    try:
        n = len(rgbas)
        if n == 1:
            return float(rgbas[0, 3])
        return float(rgbas[:, 3].max()) if n else 0.0
    except Exception:
        return 0.0


def _opacity(m) -> tuple[float, float, float]:
    """(fill alpha, stroke alpha, stroke width) of m's own path."""
    d = m.__dict__
    fa = _alpha(d.get("fill_rgbas", ()))
    w = d.get("stroke_width", 0.0)
    if type(w) not in (int, float):
        try:
            w = float(np.max(w))
        except Exception:
            w = 0.0
    sa = _alpha(d.get("stroke_rgbas", ())) if w > 0 else 0.0
    return fa, sa, w


_KIND: dict[type, int] = {}


def _kind(tp) -> int:
    """1 = text-like, 2 = other VMobject, 0 = anything else (cached per class)."""
    k = _KIND.get(tp)
    if k is None:
        k = 1 if issubclass(tp, TEXT_TYPES) else 2 if issubclass(tp, VMobject) else 0
        _KIND[tp] = k
    return k


_B_CACHE: dict[int, np.ndarray] = {}


def _bernstein(n: int) -> np.ndarray:
    b = _B_CACHE.get(n)
    if b is None:
        t = np.linspace(0.0, 1.0, n + 1)[:, None]
        b = np.hstack([(1 - t) ** 3, 3 * (1 - t) ** 2 * t, 3 * (1 - t) * t ** 2, t ** 3])
        _B_CACHE[n] = b
    return b


def flatten_many(pts_list: list[np.ndarray]):
    """Bezier control points (4k x 2 each, Manim layout) -> chords.
    Returns (p0, p1, offsets): segments of shape i are p0[offsets[i]:offsets[i+1]].
    Straight Beziers stay one chord; curved ones get CURVE_STEPS chords."""
    ks = np.fromiter((len(p) // 4 for p in pts_list), dtype=np.int64, count=len(pts_list))
    if ks.sum() == 0:
        z = np.zeros((0, 2))
        return z, z, np.zeros(len(pts_list) + 1, dtype=np.int64)
    P = np.concatenate([p[: 4 * k] for p, k in zip(pts_list, ks) if k]).reshape(-1, 4, 2)
    owner = np.repeat(np.arange(len(pts_list)), ks)
    c = P[:, 3] - P[:, 0]
    clen = np.maximum(np.hypot(c[:, 0], c[:, 1]), 1e-9)
    r1, r2 = P[:, 1] - P[:, 0], P[:, 2] - P[:, 0]
    dev = np.maximum(np.abs(r1[:, 0] * c[:, 1] - r1[:, 1] * c[:, 0]),
                     np.abs(r2[:, 0] * c[:, 1] - r2[:, 1] * c[:, 0])) / clen
    # handles beyond the chord's ends also bend the curve (overshoot)
    t1 = (r1[:, 0] * c[:, 0] + r1[:, 1] * c[:, 1]) / clen ** 2
    t2 = (r2[:, 0] * c[:, 0] + r2[:, 1] * c[:, 1]) / clen ** 2
    bent = (dev > 0.003) | (t1 < -1e-3) | (t2 > 1 + 1e-3) | (clen < 1e-8)
    st = ~bent
    p0 = [P[st, 0]]
    p1 = [P[st, 3]]
    own = [owner[st]]
    if bent.any():
        S = np.einsum("tc,kcd->ktd", _bernstein(CURVE_STEPS), P[bent])
        p0.append(S[:, :-1].reshape(-1, 2))
        p1.append(S[:, 1:].reshape(-1, 2))
        own.append(np.repeat(owner[bent], CURVE_STEPS))
    p0, p1, own = np.concatenate(p0), np.concatenate(p1), np.concatenate(own)
    order = np.argsort(own, kind="stable")
    offsets = np.searchsorted(own[order], np.arange(len(pts_list) + 1))
    return p0[order], p1[order], offsets


def close_subpaths(points2: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Closing chords (end -> start) of every subpath, for inside/outside tests."""
    k = len(points2) // 4
    if k == 0:
        z = np.zeros((0, 2))
        return z, z
    P = points2[: 4 * k].reshape(k, 4, 2)
    new = np.r_[True, np.any(np.abs(P[1:, 0] - P[:-1, 3]) > 1e-6, axis=1)]
    starts = np.flatnonzero(new)
    ends = np.r_[starts[1:] - 1, k - 1]
    return P[ends, 3], P[starts, 0]


def is_closed(points2: np.ndarray) -> bool:
    a, b = close_subpaths(points2)
    return len(a) > 0 and bool(np.all(np.hypot(*(a - b).T) < 1e-3)) and len(points2) >= 8


def seg_box_gaps(p0: np.ndarray, p1: np.ndarray, box) -> np.ndarray:
    """Per segment: distance to the axis-aligned box (x0, y0, x1, y1), or minus the depth of
    its deepest point inside the box when it enters it.  `box` may also be an (n, 4) array
    of boxes: the result is then (n, segments)."""
    B = np.asarray(box, dtype=float)
    single = B.ndim == 1
    B = B.reshape(-1, 4)
    x0, y0, x1, y1 = (B[:, k:k + 1] for k in range(4))         # (nb, 1) each
    d = p1 - p0
    px, py, dx_, dy_ = p0[None, :, 0], p0[None, :, 1], d[None, :, 0], d[None, :, 1]
    tmin = np.zeros((len(B), len(p0)))
    tmax = np.ones((len(B), len(p0)))
    with np.errstate(divide="ignore", invalid="ignore"):
        for pa, da, lo, hi in ((px, dx_, x0, x1), (py, dy_, y0, y1)):
            flat = np.abs(da) < 1e-12
            inside = (pa >= lo) & (pa <= hi)
            ta, tb = (lo - pa) / da, (hi - pa) / da
            tmin = np.maximum(tmin, np.where(flat, np.where(inside, -np.inf, np.inf), np.minimum(ta, tb)))
            tmax = np.minimum(tmax, np.where(flat, np.where(inside, np.inf, -np.inf), np.maximum(ta, tb)))
    hit = tmin <= tmax

    def pt_box(qx, qy):
        ex = np.maximum(np.maximum(x0 - qx, qx - x1), 0.0)
        ey = np.maximum(np.maximum(y0 - qy, qy - y1), 0.0)
        return np.hypot(ex, ey)
    best = np.minimum(pt_box(px, py), pt_box(px + dx_, py + dy_))
    dd = dx_ * dx_ + dy_ * dy_
    dd = np.where(dd < 1e-18, 1e-18, dd)
    for cx, cy in ((x0, y0), (x0, y1), (x1, y0), (x1, y1)):
        t = np.clip(((cx - px) * dx_ + (cy - py) * dy_) / dd, 0.0, 1.0)
        best = np.minimum(best, np.hypot(px + dx_ * t - cx, py + dy_ * t - cy))
    if hit.any():
        tm = 0.5 * (tmin + tmax)
        mx, my = px + dx_ * tm, py + dy_ * tm
        depth = np.minimum(np.minimum(mx - x0, x1 - mx), np.minimum(my - y0, y1 - my))
        best = np.where(hit, -np.maximum(depth, 0.0), best)
    return best[0] if single else best


def clip_to_box(p0, p1, box):
    """Clip segments to box (Liang-Barsky); returns (p0, p1, kept-mask)."""
    x0, y0, x1, y1 = box
    d = p1 - p0
    tmin = np.zeros(len(p0))
    tmax = np.ones(len(p0))
    with np.errstate(divide="ignore", invalid="ignore"):
        for ax, lo, hi in ((0, x0, x1), (1, y0, y1)):
            da, pa = d[:, ax], p0[:, ax]
            flat = np.abs(da) < 1e-12
            inside = (pa >= lo) & (pa <= hi)
            ta, tb = (lo - pa) / da, (hi - pa) / da
            tmin = np.maximum(tmin, np.where(flat, np.where(inside, -np.inf, np.inf), np.minimum(ta, tb)))
            tmax = np.minimum(tmax, np.where(flat, np.where(inside, np.inf, -np.inf), np.maximum(ta, tb)))
    keep = tmin <= tmax
    return p0[keep] + d[keep] * tmin[keep, None], p0[keep] + d[keep] * tmax[keep, None], keep


def points_inside(p0, p1, pts) -> np.ndarray:
    """Even-odd test of pts (m x 2) against closed polygon(s) given as segments."""
    y0, y1 = p0[None, :, 1], p1[None, :, 1]
    x0, x1 = p0[None, :, 0], p1[None, :, 0]
    py, px = pts[:, 1:2], pts[:, 0:1]
    straddle = (y0 > py) != (y1 > py)
    with np.errstate(divide="ignore", invalid="ignore"):
        xc = x0 + (py - y0) * (x1 - x0) / (y1 - y0)
    return ((straddle & (px < xc)).sum(axis=1) % 2) == 1


def _pt_seg_dist(P, s0, s1) -> float:
    """Min distance from points P (m x 2) to segments (n)."""
    d = s1 - s0
    dd = np.einsum("ij,ij->i", d, d)
    dd = np.where(dd < 1e-18, 1e-18, dd)
    t = ((P[:, None, 0] - s0[None, :, 0]) * d[None, :, 0] +
         (P[:, None, 1] - s0[None, :, 1]) * d[None, :, 1]) / dd[None, :]
    np.clip(t, 0.0, 1.0, out=t)
    qx = s0[None, :, 0] + d[None, :, 0] * t - P[:, None, 0]
    qy = s0[None, :, 1] + d[None, :, 1] * t - P[:, None, 1]
    return float(np.sqrt((qx * qx + qy * qy).min()))


def ink_gap(A: np.ndarray, B: np.ndarray) -> float:
    """Distance between the outlines of two glyphs (2-D Bezier control points), or a
    negative number when one's ink lies inside the other's."""
    a0, a1, _ = flatten_many([A])
    b0, b1, _ = flatten_many([B])
    if not len(a0) or not len(b0):
        return math.inf
    ac0, ac1 = close_subpaths(A)
    bc0, bc1 = close_subpaths(B)
    pa = np.concatenate([a0, a1[-1:]])
    pb = np.concatenate([b0, b1[-1:]])
    if points_inside(np.concatenate([b0, bc0]), np.concatenate([b1, bc1]), pa).any() or \
            points_inside(np.concatenate([a0, ac0]), np.concatenate([a1, ac1]), pb).any():
        return -0.01
    return min(_pt_seg_dist(pa, b0, b1), _pt_seg_dist(pb, a0, a1))


def box_gap(a, b) -> float:
    """Distance between two boxes; negative = overlapping by the smaller penetration."""
    dx = max(a[0] - b[2], b[0] - a[2])
    dy = max(a[1] - b[3], b[1] - a[3])
    if dx >= 0 and dy >= 0:
        return math.hypot(dx, dy)
    return max(dx, dy)


def _inside(box, outer, tol=1e-3) -> bool:
    return (box[0] >= outer[0] - tol and box[1] >= outer[1] - tol and
            box[2] <= outer[2] + tol and box[3] <= outer[3] + tol)


# ---------------------------------------------------------------------------- collection
class _Scan:
    """Visible texts and shapes of the current frame, in screen coordinates."""

    def __init__(self, mobjects, tf):
        self.tf = tf
        self.zoom = 1.0 if tf is None else float(tf[3])
        self.fw, self.fh = config.frame_width / 2, config.frame_height / 2
        self.t_root, self.t_part, self.t_idx, self.t_anc, self.t_box, self.t_rank = [], [], [], [], [], []
        self.t_bg, self.t_alpha, self.t_glyphs = [], [], []
        self.s_mob, self.s_anc, self.s_pts, self.s_fa, self.s_sa, self.s_half, self.s_rank = \
            [], [], [], [], [], [], []
        self.shape_anc_ids: set[int] = set()
        visited: set[int] = set()
        order = 0
        stack = [(m, ()) for m in reversed(list(mobjects))]
        while stack:
            m, anc = stack.pop()
            mid = id(m)
            if mid in visited:
                continue
            visited.add(mid)
            order += 1
            md = m.__dict__
            if md.get("ss_allow_overlap"):
                continue
            kind = _kind(type(m))
            if kind == 1:
                self._add_text(m, anc, order)
                continue
            if kind == 2:
                pts = md.get("points")
                if pts is not None and len(pts) >= 4:
                    fa, sa, w = _opacity(m)
                    if sa >= MIN_OPACITY or fa >= FAINT:
                        self.s_mob.append(m)
                        self.s_anc.append(anc)
                        self.s_pts.append(self._screen(pts))
                        self.s_fa.append(fa)
                        self.s_sa.append(sa)
                        self.s_half.append(0.005 * w if sa >= MIN_OPACITY else 0.0)
                        self.s_rank.append(md.get("z_index", 0) * 1e7 + order)
                        if anc:
                            self.shape_anc_ids.update(map(id, anc))
            subs = md.get("submobjects")
            if subs:
                anc2 = anc + (m,)
                stack.extend((s, anc2) for s in reversed(subs))

    def _screen(self, points3):
        if self.tf is None:
            return points3[:, :2]
        cx, cy, sx, sy = self.tf
        return np.column_stack([(points3[:, 0] - cx) * sx, (points3[:, 1] - cy) * sy])

    def _add_text(self, root, anc, order):
        subs = root.submobjects
        if isinstance(root, SingleStringMathTex) and len(subs) > 1 and \
                len(getattr(root, "tex_strings", ())) > 1:
            parts = list(subs)
        elif isinstance(root, Paragraph) and len(subs) > 1:
            parts = list(subs)
        else:
            parts = [root]
        bg = None
        for x in subs:
            if isinstance(x, BackgroundRectangle) and len(x.points):
                fa, _, _ = _opacity(x)
                if fa >= OPAQUE:
                    p = self._screen(x.points)
                    bg = (p[:, 0].min(), p[:, 1].min(), p[:, 0].max(), p[:, 1].max())
        z = getattr(root, "z_index", 0)
        for i, part in enumerate(parts):
            if isinstance(part, BackgroundRectangle):
                continue
            vis = []
            alpha = 0.0
            for g in part.get_family():
                if len(g.points) and not isinstance(g, BackgroundRectangle):
                    fa, sa, _ = _opacity(g)
                    if fa >= MIN_OPACITY or sa >= MIN_OPACITY:
                        vis.append(g.points)
                        alpha = max(alpha, fa, sa)
            if not vis:
                continue
            p = self._screen(np.concatenate(vis))
            lo, hi = p.min(axis=0), p.max(axis=0)
            if hi[0] - lo[0] < 1e-4 and hi[1] - lo[1] < 1e-4:
                continue
            if lo[0] > self.fw or hi[0] < -self.fw or lo[1] > self.fh or hi[1] < -self.fh:
                continue                           # parked entirely off-frame: not seen
            self.t_root.append(root)
            self.t_part.append(part)
            self.t_idx.append(i)
            self.t_anc.append(anc + ((root,) if part is not root else ()))
            self.t_box.append((float(lo[0]), float(lo[1]), float(hi[0]), float(hi[1])))
            self.t_rank.append(z * 1e7 + order + 0.5)
            self.t_bg.append(bg)
            self.t_alpha.append(alpha)
            self.t_glyphs.append(vis)


# ---------------------------------------------------------------------------- the audit
def _camera_transform(camera):
    """Scene -> screen coordinates (14.22 x 8 frame) for a moved or zoomed camera."""
    frame = getattr(camera, "frame", None)
    if frame is None:
        return None
    try:
        c = frame.get_center()
        w, h = frame.width, frame.height
        fw, fh = config.frame_width, config.frame_height
        if abs(c[0]) < 1e-9 and abs(c[1]) < 1e-9 and abs(w - fw) < 1e-6 and abs(h - fh) < 1e-6:
            return None
        return (float(c[0]), float(c[1]), fw / w, fh / h)
    except Exception:
        return None


def audit(mobjects, camera=None, allowed_pairs=(), clearance: float = CLEARANCE,
          safe_x: float = style.SAFE_X, safe_top: float = style.SAFE_TOP,
          safe_bottom: float = style.SAFE_BOTTOM,
          content_bottom: float = style.CONTENT_BOTTOM, sizes: bool = False) -> list[Issue]:
    """Check the given top-level mobjects (e.g. scene.mobjects) as they are now.

    allowed_pairs: iterable of (mob_a, mob_b, reason); issues between a's family and b's
    family are still returned, with .allowed set to the reason.
    sizes: also report "text-size" / "small-label" (cap height in px, see module doc)."""
    S = _Scan(mobjects, _camera_transform(camera) if camera is not None else None)
    nT, nS = len(S.t_box), len(S.s_mob)
    if not nT:
        return []
    TB = np.array(S.t_box)
    t_ids = [{id(p), id(r), *map(id, a)} for p, r, a in zip(S.t_part, S.t_root, S.t_anc)]
    names = [_text_name(r, p, i) for r, p, i in zip(S.t_root, S.t_part, S.t_idx)]

    def centre(b):
        return (round((b[0] + b[2]) / 2, 2), round((b[1] + b[3]) / 2, 2))

    allowed = []
    for a, b, reason in allowed_pairs:
        try:
            allowed.append(({id(x) for x in a.get_family()}, {id(x) for x in b.get_family()},
                            reason or "allowed"))
        except Exception:
            pass

    def allowed_reason(ids1, ids2):
        for fa, fb, reason in allowed:
            if (ids1 & fa and ids2 & fb) or (ids1 & fb and ids2 & fa):
                return reason
        return None

    issues: list[Issue] = []

    # ---------------------------------------------------------------- text size
    if sizes:
        issues.extend(_size_issues(S, names, centre))

    # ---------------------------------------------------------------- safe area
    for i, (x0, y0, x1, y1) in enumerate(S.t_box):
        out = []
        if x0 < -safe_x - SAFE_TOL:
            out.append(f"x={x0:.2f}")
        if x1 > safe_x + SAFE_TOL:
            out.append(f"x={x1:.2f}")
        if y1 > safe_top + SAFE_TOL:
            out.append(f"y={y1:.2f}")
        if y0 < safe_bottom - SAFE_TOL:
            out.append(f"y={y0:.2f}")
        if out:
            issues.append(Issue("safe-area", names[i], "", 0.0, 0.0, centre(S.t_box[i]),
                                detail=f"reaches {', '.join(out)} (safe: |x| <= {safe_x:g}, "
                                       f"{safe_bottom:g} <= y <= {safe_top:g})"))
        elif y0 < content_bottom - SAFE_TOL and not any(
                getattr(x, "ss_caption_zone", False)
                for x in (S.t_part[i], S.t_root[i], *S.t_anc[i])):
            issues.append(Issue("caption-zone", names[i], "", 0.0, 0.0, centre(S.t_box[i]),
                                detail=f"reaches y={y0:.2f}, below y={content_bottom:g} "
                                       f"(caption/player zone)"))

    # ---------------------------------------------------------------- relatedness helpers
    gbox_cache: dict[int, tuple | None] = {}

    def group_box(g):
        k = id(g)
        if k not in gbox_cache:
            try:
                pts = [x.points for x in g.get_family() if len(x.points)]
                p = S._screen(np.concatenate(pts)) if pts else None
                gbox_cache[k] = None if p is None else (*p.min(axis=0), *p.max(axis=0))
            except Exception:
                gbox_cache[k] = None
        return gbox_cache[k]

    owners = []                      # (nearest NumberLine id, own small group id)
    pure_anc = []                    # ids of pure-text groups holding the text
    for i in range(nT):
        nl = own = None
        own_done = False
        root = S.t_root[i]
        x0, y0, x1, y1 = S.t_box[i]
        for a in reversed(S.t_anc[i]):
            if a is root:
                continue
            if nl is None and isinstance(a, NumberLine):
                nl = id(a)
            if not own_done and id(a) in S.shape_anc_ids:
                own_done = True
                gb = group_box(a)
                if gb is not None and (gb[0] >= x0 - LOCAL_PAD and gb[1] >= y0 - LOCAL_PAD and
                                       gb[2] <= x1 + LOCAL_PAD and gb[3] <= y1 + LOCAL_PAD):
                    own = id(a)
            if nl is not None and own_done:
                break
        owners.append((nl, own))
        pure_anc.append({id(a) for a in S.t_anc[i] if a is not root and id(a) not in S.shape_anc_ids})

    # ---------------------------------------------------------------- glyph boxes (lazy)
    gbox: dict[int, np.ndarray] = {}

    def glyph_boxes(i):
        if i not in gbox:
            b = np.array([(*g[:, :2].min(axis=0), *g[:, :2].max(axis=0)) for g in S.t_glyphs[i]])
            if S.tf is not None:
                cx, cy, sx, sy = S.tf
                b = np.column_stack([(b[:, 0] - cx) * sx, (b[:, 1] - cy) * sy,
                                     (b[:, 2] - cx) * sx, (b[:, 3] - cy) * sy])
            gbox[i] = b
        return gbox[i]

    # ---------------------------------------------------------------- text vs shapes
    # opaque panel behind each text: (draw rank, box, is a separate shape)
    panel_of = [((S.t_rank[i] - 0.25, S.t_bg[i], False) if S.t_bg[i] is not None else None)
                for i in range(nT)]
    if nS:
        lens = np.fromiter((len(p) for p in S.s_pts), dtype=np.int64, count=nS)
        starts = np.r_[0, np.cumsum(lens)[:-1]]
        allp = np.concatenate(S.s_pts)
        half = np.array(S.s_half)
        SB = np.column_stack([np.minimum.reduceat(allp, starts, axis=0) - half[:, None],
                              np.maximum.reduceat(allp, starts, axis=0) + half[:, None]])
        m = clearance + 0.06
        cand = ((SB[None, :, 0] <= TB[:, None, 2] + m) & (SB[None, :, 2] >= TB[:, None, 0] - m) &
                (SB[None, :, 1] <= TB[:, None, 3] + m) & (SB[None, :, 3] >= TB[:, None, 1] - m))
        used = np.flatnonzero(cand.any(axis=0))
    else:
        cand = np.zeros((nT, 0), dtype=bool)
        used = np.zeros(0, dtype=np.int64)

    if len(used):
        local = {int(j): k for k, j in enumerate(used)}
        P0, P1, OFF = flatten_many([S.s_pts[j] for j in used])
        seg_owner = np.repeat(np.arange(len(used)), np.diff(OFF))
        s_rank = np.array(S.s_rank)
        s_ids_cache: dict[int, set] = {}
        closed_cache: dict[int, bool] = {}
        deco_cache: dict[int, set] = {}
        text_by_group = {}
        for i in range(nT):
            par = [a for a in S.t_anc[i] if a is not S.t_root[i]]
            if par:
                text_by_group.setdefault(id(par[-1]), names[i])

        def mark_like(j, box):
            """A short straight stroke: a tick mark, or a fraction bar (horizontal, <= 2.5
            long, spanning the text above/below it).  Typesetting puts these ~0.1 from
            their numbers."""
            pts = S.s_pts[j]            # (a straight line has no area, so ignore its fill)
            if len(pts) > 8:
                return False
            a, b = pts[0], pts[-1]
            L = math.hypot(b[0] - a[0], b[1] - a[1])
            if L < 1e-6:
                return False
            # straight: every control point on the chord
            d = np.abs((pts[:, 0] - a[0]) * (b[1] - a[1]) - (pts[:, 1] - a[1]) * (b[0] - a[0])) / L
            if d.max() > 0.003:
                return False
            if L <= 0.35:
                return True
            if abs(b[1] - a[1]) >= 0.02 or L > 2.5:
                return False
            lo, hi = min(a[0], b[0]), max(a[0], b[0])
            return L <= box[2] - box[0] + 0.6 or (box[0] >= lo - 0.1 and box[2] <= hi + 0.1)

        def is_axis(j):
            if isinstance(S.s_mob[j], NumberLine):
                return True
            return any(isinstance(a, NumberLine) for a in S.s_anc[j])

        def s_ids(j):
            if j not in s_ids_cache:
                s_ids_cache[j] = {id(S.s_mob[j]), *map(id, S.s_anc[j])}
            return s_ids_cache[j]

        def deco_of(j):
            if j not in deco_cache:
                ids = set()
                if len(_DECORATES):
                    for x in (S.s_mob[j], *S.s_anc[j]):
                        try:
                            tgt = _DECORATES.get(x)
                        except TypeError:
                            tgt = None
                        if tgt is not None:
                            ids.update(id(y) for y in tgt.get_family())
                deco_cache[j] = ids
            return deco_cache[j]

        def shape_name(j):
            mob, anc = S.s_mob[j], S.s_anc[j]
            name = type(mob).__name__
            if isinstance(mob, NumberLine):
                name += _axis_tag(mob, anc)
            for a in reversed(anc):
                if type(a).__name__ not in ("VGroup", "Group", "VDict"):
                    oname = type(a).__name__
                    if isinstance(a, NumberLine):
                        oname += _axis_tag(a, anc)
                    name = f"{name} of {oname}"
                    break
            if anc and id(anc[-1]) in text_by_group and len(anc[-1].submobjects) <= 3:
                name += f" [with {text_by_group[id(anc[-1])]}]"
            op = max(S.s_fa[j], S.s_sa[j])
            if op < 0.95:
                name += f" ({round(100 * op)}% opacity)"
            return name

        for i in range(nT):
            js = np.flatnonzero(cand[i])
            if not len(js):
                continue
            box = S.t_box[i]
            x0, y0, x1, y1 = box
            # panels: closed or filled shapes that fully contain the text box
            panels = set()
            wraps = js[(SB[js, 0] <= x0) & (SB[js, 1] <= y0) & (SB[js, 2] >= x1) & (SB[js, 3] >= y1)]
            if len(wraps):
                corners = np.array([[x0, y0], [x0, y1], [x1, y0], [x1, y1], [(x0 + x1) / 2, (y0 + y1) / 2]])
                for j in wraps.tolist():
                    if j not in closed_cache:
                        closed_cache[j] = is_closed(S.s_pts[j])
                    if not (closed_cache[j] or S.s_fa[j] >= MIN_OPACITY):
                        continue
                    k = local[j]
                    a0, a1 = P0[OFF[k]:OFF[k + 1]], P1[OFF[k]:OFF[k + 1]]
                    c0, c1 = close_subpaths(S.s_pts[j])
                    if points_inside(np.concatenate([a0, c0]), np.concatenate([a1, c1]), corners).all():
                        panels.add(j)
                        if S.s_fa[j] >= OPAQUE and S.s_rank[j] < S.t_rank[i] and \
                                (panel_of[i] is None or S.s_rank[j] > panel_of[i][0]):
                            panel_of[i] = (S.s_rank[j], tuple(SB[j]), True)
            occl = panel_of[i]
            ks = np.array([local[j] for j in js.tolist()])
            if occl is not None:     # beneath the text's opaque panel = hidden
                keep = np.array([(s_rank[j] > occl[0]) or (j in panels) for j in js.tolist()])
                js, ks = js[keep], ks[keep]
                if not len(js):
                    continue
            mask = np.zeros(len(used), dtype=bool)
            mask[ks] = True
            sel = mask[seg_owner]
            p0, p1, own_k = P0[sel], P1[sel], seg_owner[sel]
            if occl is not None:     # above the panel: only what lies on the panel counts
                above = np.isin(own_k, [local[j] for j in js.tolist() if j not in panels])
                if above.any():
                    c0, c1, kept = clip_to_box(p0[above], p1[above], occl[1])
                    p0 = np.concatenate([p0[~above], c0])
                    p1 = np.concatenate([p1[~above], c1])
                    own_k = np.concatenate([own_k[~above], own_k[above][kept]])
                    order = np.argsort(own_k, kind="stable")
                    p0, p1, own_k = p0[order], p1[order], own_k[order]
            if not len(p0):
                continue
            g = seg_box_gaps(p0, p1, box)
            brk = np.r_[0, np.flatnonzero(np.diff(own_k)) + 1]
            gmin = np.minimum.reduceat(g, brk)
            gk = own_k[brk]
            nl, own = owners[i]
            ends = np.r_[brk[1:], len(own_k)]
            for k, gv, b0, b1 in zip(gk.tolist(), gmin.tolist(), brk.tolist(), ends.tolist()):
                j = int(used[k])
                gap = gv - S.s_half[j]
                if gap < TOUCH and len(S.t_glyphs[i]) > 1:
                    # the text box is coarse (a superscript raises a corner): re-measure
                    # against each glyph's box before calling it a touch
                    gap = float(seg_box_gaps(p0[b0:b1], p1[b0:b1], glyph_boxes(i)).min()) - S.s_half[j]
                if gap >= clearance - TOL:
                    continue
                ids = s_ids(j)
                related = (j in panels or (own is not None and own in ids) or
                           (nl is not None and nl in ids) or bool(deco_of(j) & t_ids[i]) or
                           # axes: tick labels and titles hug the axis by design, so an
                           # axis line or tick only counts when it touches the text
                           is_axis(j) or
                           max(S.s_fa[j], S.s_sa[j]) < FAINT or S.t_alpha[i] < FAINT)
                if not related and mark_like(j, box):
                    related = True
                if not related and type(S.s_mob[j]) is VMobjectFromSVGPath:
                    # a stray glyph (a formula piece moved by a transform) beside the text on
                    # the same line reads as part of that line
                    sb = SB[j]
                    vo = min(sb[3], y1) - max(sb[1], y0)
                    related = vo >= 0.5 * min(sb[3] - sb[1], y1 - y0)
                need = TOUCH if related else clearance
                if gap >= need - (TOL if need > TOUCH else 1e-3):
                    continue
                issues.append(Issue("overlap" if gap < TOUCH else "clearance", names[i],
                                    shape_name(j), round(gap, 3), need, centre(box),
                                    centre(SB[j]), allowed=allowed_reason(t_ids[i], ids)))

    # ---------------------------------------------------------------- text vs text
    def glyph_gap(i, j) -> float:
        """Glyph-box distance; where two glyph boxes touch, the real ink distance decides
        (a radical's box covers its radicand, italic overhangs touch neighbours)."""
        A, B = glyph_boxes(i), glyph_boxes(j)
        dx = np.maximum(A[:, None, 0] - B[None, :, 2], B[None, :, 0] - A[:, None, 2])
        dy = np.maximum(A[:, None, 1] - B[None, :, 3], B[None, :, 1] - A[:, None, 3])
        both = (dx >= 0) & (dy >= 0)
        g = np.where(both, np.hypot(np.maximum(dx, 0), np.maximum(dy, 0)), np.maximum(dx, dy))
        if g.min() >= TOUCH:
            return float(g.min())
        for n, (ga, gb) in enumerate(zip(*np.nonzero(g < TOUCH))):
            if n >= 16:
                break                       # many touching glyphs: they really overlap
            pa, pb = S.t_glyphs[i][ga], S.t_glyphs[j][gb]
            if S.tf is not None:
                pa, pb = S._screen(pa), S._screen(pb)
            ink = ink_gap(pa[:, :2], pb[:, :2])
            if ink < 0:
                return float(g[ga, gb])     # ink inside ink: keep the box penetration
            g[ga, gb] = max(g[ga, gb], ink)
        return float(g.min())

    if nT > 1:
        m2 = clearance + 0.01
        close = ((TB[None, :, 0] <= TB[:, None, 2] + m2) & (TB[None, :, 2] >= TB[:, None, 0] - m2) &
                 (TB[None, :, 1] <= TB[:, None, 3] + m2) & (TB[None, :, 3] >= TB[:, None, 1] - m2))
        for i, j in zip(*map(np.ndarray.tolist, np.nonzero(np.triu(close, 1)))):
            if S.t_root[i] is S.t_root[j]:
                continue
            a, b = S.t_box[i], S.t_box[j]
            if names[i] == names[j] and max(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]),
                                            abs(a[3] - b[3])) < 0.02:
                continue          # an exact duplicate stacked on itself (a transform's copy)
            pa, pb = panel_of[i], panel_of[j]
            # a label on an opaque panel shape: that shape-vs-text check covers this pair
            if (pa is not None and pa[2] and not _inside(b, pa[1])) or \
                    (pb is not None and pb[2] and not _inside(a, pb[1])):
                continue
            nla, owna = owners[i]
            nlb, ownb = owners[j]
            related = (bool(pure_anc[i] & t_ids[j]) or bool(pure_anc[j] & t_ids[i]) or
                       (nla is not None and nla == nlb) or
                       (owna is not None and owna in t_ids[j]) or (ownb is not None and ownb in t_ids[i]))
            if not related:
                # side by side on one line (fragments of one formula, "unhappy 238"): they
                # read as one line of text, so they only have to keep from touching
                vo = min(a[3], b[3]) - max(a[1], b[1])
                related = vo >= 0.5 * min(a[3] - a[1], b[3] - b[1])
            if S.t_alpha[i] < FAINT or S.t_alpha[j] < FAINT:
                related = True
            need = TOUCH if related else clearance
            lim = need - (TOL if need > TOUCH else 1e-3)
            gap = box_gap(a, b)
            if gap >= lim:
                continue
            # boxes are coarse (a radical's box covers its radicand, a fraction bar widens
            # its part): measure glyph to glyph before reporting
            gap = glyph_gap(i, j)
            if gap >= lim:
                continue
            na, nb, ca, cb = names[i], names[j], centre(a), centre(b)
            if (na, ca) > (nb, cb):
                na, nb, ca, cb = nb, na, cb, ca
            issues.append(Issue("overlap" if gap < TOUCH else "clearance", na, nb, round(gap, 3),
                                need, ca, cb, allowed=allowed_reason(t_ids[i], t_ids[j])))
    return _dedupe(issues)


def _size_issues(S: "_Scan", names: list[str], centre) -> list[Issue]:
    """Cap height of each readable text (BAR §5 floors), measured from its font size."""
    out: list[Issue] = []
    px_cache: dict[int, float | None] = {}
    for i, root in enumerate(S.t_root):
        if S.t_alpha[i] < READABLE:
            continue
        k = id(root)
        if k not in px_cache:
            px = style.cap_height_px(root)
            px_cache[k] = None if px is None else px * S.zoom
        px = px_cache[k]
        if px is None or px >= SMALL_LABEL_PX:
            continue
        anc = (S.t_part[i], root, *S.t_anc[i])
        role = next((getattr(x, "ss_role", None) for x in anc if getattr(x, "ss_role", None)), None)
        tick = role in ("tick", "citation") or any(isinstance(x, NumberLine) for x in anc)
        if px < TEXT_FLOOR_PX - 0.05:
            out.append(Issue("text-size", names[i], "", round(px, 1), TEXT_FLOOR_PX,
                             centre(S.t_box[i]),
                             detail=f"cap height ≈ {px:.0f} px < {TEXT_FLOOR_PX:.0f} px (BAR floor for "
                                    f"ticks/citations; labels need 34 px: Text >= "
                                    f"{style.TEXT_LABEL_MIN}, MathTex >= {style.MATH_LABEL})"))
        elif not tick:
            out.append(Issue("small-label", names[i], "", round(px, 1), SMALL_LABEL_PX,
                             centre(S.t_box[i]),
                             detail=f"cap height ≈ {px:.0f} px: reads as a footnote; a label the "
                                    f"viewer must read needs 34 px (Text >= {style.TEXT_LABEL_MIN}, "
                                    f"MathTex >= {style.MATH_LABEL})"))
    return out


def _dedupe(issues: list[Issue]) -> list[Issue]:
    """One issue per key (same text, same other object): keep the worst gap."""
    best: dict[tuple, Issue] = {}
    for it in issues:
        k = it.key
        if k not in best or it.gap < best[k].gap:
            best[k] = it
    return list(best.values())


# ---------------------------------------------------------------------------- time ranges
@dataclass
class Finding:
    issue: Issue                # the worst instance seen
    start: float
    end: float
    checks: int = 1

    @property
    def held(self) -> float:
        return self.end - self.start


class AuditLog:
    """Merges the issues found by consecutive checks into time ranges."""

    def __init__(self):
        self.open: dict[tuple, Finding] = {}
        self.closed: list[Finding] = []
        self.checks = 0
        self.seconds = 0.0
        self.errors = 0

    def update(self, issues: list[Issue], t0: float, t1: float, held: bool) -> None:
        """Record a check at time t1.  held=True: the frame was unchanged over [t0, t1]."""
        self.checks += 1
        seen = set()
        for it in issues:
            k = it.key
            seen.add(k)
            f = self.open.get(k)
            if f is None:
                self.open[k] = Finding(it, t0 if held else t1, t1)
            else:
                f.end = t1
                f.checks += 1
                if it.gap < f.issue.gap:
                    f.issue = it
        for k in [k for k in self.open if k not in seen]:
            f = self.open.pop(k)
            f.end = max(f.end, t0)          # the state lasted until this animation began
            self.closed.append(f)

    def close_all(self, t: float) -> None:
        for f in self.open.values():
            f.end = max(f.end, t)
            self.closed.append(f)
        self.open.clear()

    def findings(self) -> list[Finding]:
        return sorted(self.closed + list(self.open.values()), key=lambda f: (f.start, f.issue.key))


def fmt_time(t: float) -> str:
    m, s = divmod(max(t, 0.0), 60)
    return f"{int(m)}:{s:04.1f}"


def finding_line(f: Finding) -> str:
    if f.held < 0.05:
        span = f"{fmt_time(f.start)} (end of an animation, not held)"
    else:
        span = f"{fmt_time(f.start)}-{fmt_time(f.end)} (held {f.held:.1f}s)"
    return f"{span} {f.issue.describe()}"


SEVERITY = {"overlap": 0, "safe-area": 1, "caption-zone": 2, "text-size": 3, "clearance": 4,
            "small-label": 5}


def rank_findings(findings: list[Finding]) -> list[Finding]:
    """Most important first: overlaps, frame problems, then tight gaps.  Overlaps and frame
    problems: longest held first; tight gaps: smallest gap first (held >= 1 s before
    momentary ones)."""
    def key(f):
        k = SEVERITY.get(f.issue.kind, 9)
        if f.issue.kind == "clearance":
            return (k, f.held < 1.0, round(f.issue.gap, 2), -f.held, f.start)
        return (k, -f.held, f.issue.gap, 0, f.start)
    return sorted(findings, key=key)


def finding_dict(f: Finding) -> dict:
    it = f.issue
    d = {"kind": it.kind, "start": round(f.start, 2), "end": round(f.end, 2),
         "held": round(f.held, 2), "text": it.a, "text_pos": list(it.a_pos)}
    if it.kind in ("overlap", "clearance"):
        d.update({"other": it.b, "other_pos": list(it.b_pos) if it.b_pos else None,
                  "gap": round(it.gap, 3), "need": it.need})
    else:
        d["detail"] = it.detail
    if it.allowed:
        d["allowed"] = it.allowed
    d["msg"] = f"{it.kind} {finding_line(f)}"
    return d
