import time
from pathlib import Path

import cv2

from config import settings
from tracker.camera import Camera
from core.logger import get_logger

logger = get_logger("App")


Path(settings.results.directory).mkdir(parents=True, exist_ok=True)

camera = Camera()
camera.open()

logger.info("EyeTrax Prototype started.")
print("=" * 50)
print("EyeTrax Prototype")
print("=" * 50)
print("Resolution :", camera.resolution())
print()

while True:

    frame = camera.read()

    if frame is None:
        break

    fps = camera.fps()

    cv2.putText(
        frame,
        f"FPS : {fps:.1f}",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        settings.ui.font_scale,
        (0, 255, 0),
        settings.ui.font_thickness,
    )

    cv2.putText(
        frame,
        f"Frame : {camera.frame_count}",
        (20, 65),
        cv2.FONT_HERSHEY_SIMPLEX,
        settings.ui.font_scale,
        (0, 255, 255),
        settings.ui.font_thickness,
    )

    cv2.imshow(settings.window.title, frame)

    key = cv2.waitKey(1) & 0xFF

    # Save screenshot
    if key == ord("s"):

        filename = (
            Path(settings.results.directory)
            / f"frame_{int(time.time())}.png"
        )

        cv2.imwrite(str(filename), frame)

        logger.info(f"Screenshot saved : {filename}")
        print("Saved :", filename)

    # Exit
    elif key == 27:
        logger.info("Application closed.")
        break

camera.release()