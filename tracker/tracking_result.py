from dataclasses import dataclass

import numpy as np


@dataclass(slots=True)
class TrackingResult:
    """Result returned by EyeTracker.process()."""

    face_detected: bool
    blink: bool
    features: np.ndarray | None
    landmarks: np.ndarray | None