import time
from pathlib import Path

import cv2

from config import settings


def save_frame(frame) -> Path:
    """
    Save current frame to the results directory.

    Returns
    -------
    Path
        Saved image path.
    """

    result_dir = Path(settings.results.directory)
    result_dir.mkdir(parents=True, exist_ok=True)

    filename = (
        result_dir
        / f"frame_{int(time.time())}.png"
    )

    cv2.imwrite(str(filename), frame)

    return filename