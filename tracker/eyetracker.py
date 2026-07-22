from typing import Optional

import numpy as np
from eyetrax import GazeEstimator

from core.logger import get_logger
from tracker.tracking_result import TrackingResult

logger = get_logger("EyeTracker")


class EyeTracker:
    """Wrapper around EyeTrax GazeEstimator."""

    def __init__(self):
        self.estimator: Optional[GazeEstimator] = None

    def initialize(self) -> None:
        """Initialize EyeTrax."""

        logger.info("Loading EyeTrax...")

        self.estimator = GazeEstimator()

        logger.info("EyeTrax initialized.")

    def is_initialized(self) -> bool:
        """Return True if EyeTrax is initialized."""
        return self.estimator is not None

    def extract(self, frame):
        """Extract gaze features and blink status from a frame."""

        if not self.is_initialized():
            raise RuntimeError("EyeTracker is not initialized.")

        return self.estimator.extract_features(frame)

    def landmarks(self, features: Optional[np.ndarray]) -> Optional[np.ndarray]:
        """Convert feature vector into (N, 3) landmarks."""

        if features is None:
            return None

        return features.reshape(-1, 3)

    def process(self, frame) -> TrackingResult:
        """Process a frame and return tracking result."""

        features, blink = self.extract(frame)
        landmarks = self.landmarks(features)

        return TrackingResult(
            face_detected=features is not None,
            blink=blink,
            features=features,
            landmarks=landmarks,
        )

    def close(self) -> None:
        """Release EyeTrax resources."""

        if self.estimator is not None:
            self.estimator.close()
            self.estimator = None

        logger.info("EyeTrax released.")