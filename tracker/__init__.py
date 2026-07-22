from typing import Optional

from eyetrax import GazeEstimator


class EyeTracker:
    """Wrapper around EyeTrax GazeEstimator."""

    def __init__(self):
        self.estimator: Optional[GazeEstimator] = None
        self.initialized = False