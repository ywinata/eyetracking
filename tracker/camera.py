import cv2
import time

from config import settings
from core.logger import get_logger

logger = get_logger("Camera")

class Camera:

    def __init__(self):

        self.cap = None
        self.frame_count = 0
        self.start_time = None

    def open(self):
        logger.info("Opening webcam...")
        self.cap = cv2.VideoCapture(settings.camera.index)

        if not self.cap.isOpened():
            logger.error("Cannot open webcam.")
            raise RuntimeError("Cannot open webcam.")

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, settings.camera.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, settings.camera.height)
        logger.info("Camera opened.")
        logger.info(f"Resolution : {self.resolution()}")

        self.start_time = time.time()

    def read(self):

        ok, frame = self.cap.read()

        if not ok:
            return None

        self.frame_count += 1

        return frame

    def fps(self):

        elapsed = time.time() - self.start_time

        return self.frame_count / elapsed

    def resolution(self):

        return (
            int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        )

    def release(self):

        if self.cap:
            self.cap.release()

        cv2.destroyAllWindows()
        
        logger.info("Camera released.")