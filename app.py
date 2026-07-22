import time
from pathlib import Path

import cv2

from config import settings
from tracker.camera import Camera
from core.logger import get_logger
from core.display import Display
from core.utils import save_frame
from tracker.eyetracker import EyeTracker

def main():
    """Main application."""
    Path(settings.results.directory).mkdir(
        parents=True,
        exist_ok=True
    )
    
    logger = get_logger("App")
    tracker = EyeTracker()

    camera = Camera()
    tracker.initialize()
    
    if not tracker.is_initialized():
        logger.error("EyeTrax initialization failed.")
        return
    
    try:
        camera.open()
        
        if not camera.is_opened():
            logger.error("Unable to open camera.")
            return

        logger.info("EyeTrax Prototype started.")

        while True:

            frame = camera.read()
            
            if frame is None:
                logger.warning("No frame received.")
                break
            
            result = tracker.process(frame)
            
            Display.draw_overlay(
                frame,
                fps=camera.fps(),
                frame_count=camera.frame_count,
                blink=result.blink
            )
            
            Display.show(frame)
            
            key = Display.wait_key()

            if Display.is_screenshot_key(key):

                filename = save_frame(frame)

                logger.info(f"Screenshot saved: {filename}")

            elif Display.is_exit_key(key):
                logger.info("Application closed.")
                break

    except KeyboardInterrupt:
        logger.info("Interrupted by user (Ctrl+C).")

    except Exception:
        logger.exception("Unexpected error.")
        
    finally:
        tracker.close()
        camera.release()
        Display.close()
        logger.info("Application terminated.")


if __name__ == "__main__":
    main()