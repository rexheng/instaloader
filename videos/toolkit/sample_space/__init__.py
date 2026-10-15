"""Sample Space production toolkit.

    from manim import *
    from sample_space import *        # NarratedScene, style constants/helpers, synth

See videos/toolkit/PRODUCTION_GUIDE.md.
"""
from .style import *                     # noqa: F401,F403  (sets the series background)
from .style import __all__ as _style_all
from .voice import synth, synthesize, estimate_duration, PRONUNCIATIONS  # noqa: F401
from .narrated import (NarratedScene, NarratedMovingCameraScene, NarrationMixin,  # noqa: F401
                       Beat, layout_issues, allow_overlap)

__all__ = list(_style_all) + [
    "synth", "synthesize", "estimate_duration", "PRONUNCIATIONS",
    "NarratedScene", "NarratedMovingCameraScene", "NarrationMixin", "Beat",
    "layout_issues", "allow_overlap",
]
