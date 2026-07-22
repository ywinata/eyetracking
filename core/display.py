import cv2

from config import settings


class Display:
    """Utilities for drawing overlays and handling display."""

    FONT = cv2.FONT_HERSHEY_SIMPLEX

    KEY_ESC = 27

    OVERLAY = {
        "fps": {
            "position": (20, 35),
            "color": (0, 255, 0),
        },
        "frame": {
            "position": (20, 65),
            "color": (0, 255, 255),
        },
        "blink": {
            "position": (20, 95),
            "color": (0, 0, 255),
        },
        "landmark": {
            "color": (255,0,255),
            "radius": 2,
            "thickness": -1,
        },
        "recording": {
            "position": (20, 95),
            "color": (0, 0, 255),
        },
        "status": {
            "position": (20, 125),
            "color": (255, 255, 255),
        },
        "gaze": {
            "position": (20, 155),
            "color": (255, 255, 0),
        },
        "timestamp": {
            "position": (20, 185),
            "color": (200, 200, 200),
        },
    }

    # ------------------------------------------------------------------
    # Window
    # ------------------------------------------------------------------

    @classmethod
    def show(cls, frame) -> None:
        """Display frame."""
        cv2.imshow(settings.window.title, frame)

    @classmethod
    def close(cls) -> None:
        """Close all OpenCV windows."""
        cv2.destroyAllWindows()

    @classmethod
    def wait_key(cls) -> int:
        """Wait for keyboard input."""
        return cv2.waitKey(1) & 0xFF

    # ------------------------------------------------------------------
    # Keyboard
    # ------------------------------------------------------------------

    @classmethod
    def is_exit_key(cls, key: int) -> bool:
        """Return True if Exit key is pressed."""
        return key == cls.KEY_ESC

    @classmethod
    def is_screenshot_key(cls, key: int) -> bool:
        """Return True if Screenshot key is pressed."""
        return key == ord(settings.experiment.screenshot_key)

    # ------------------------------------------------------------------
    # Drawing
    # ------------------------------------------------------------------

    @classmethod
    def draw_text(
        cls,
        frame,
        text: str,
        position: tuple[int, int],
        color: tuple[int, int, int],
    ) -> None:
        """Draw text on frame."""
        cv2.putText(
            frame,
            text,
            position,
            cls.FONT,
            settings.ui.font_scale,
            color,
            settings.ui.font_thickness,
        )

    @classmethod
    def draw_item(
        cls,
        frame,
        item: str,
        text: str,
    ) -> None:
        """Draw overlay item."""
        overlay = cls.OVERLAY[item]

        cls.draw_text(
            frame,
            text,
            overlay["position"],
            overlay["color"],
        )

    # ------------------------------------------------------------------
    # Overlay Components
    # ------------------------------------------------------------------

    @classmethod
    def draw_fps(cls, frame, fps: float) -> None:
        cls.draw_item(
            frame,
            "fps",
            f"FPS : {fps:.1f}",
        )

    @classmethod
    def draw_frame_count(cls, frame, frame_count: int) -> None:
        cls.draw_item(
            frame,
            "frame",
            f"Frame : {frame_count}",
        )

    @classmethod
    def draw_blink(cls, frame, blink):
        text = "Blink : YES" if blink else "Blink : NO"
        cls.draw_text(
            frame,
            text,
            cls.OVERLAY["blink"]["position"],
            cls.OVERLAY["blink"]["color"],
        )
    
    @classmethod
    def draw_landmarks(cls, frame, landmarks):
        """Draw facial landmarks."""

        if landmarks is None:
            return

        height, width = frame.shape[:2]

        for x, y, _ in landmarks:

            px = int((x + 0.5) * width)
            py = int((y + 0.5) * height)

            cv2.circle(
                frame,
                (px, py),
                cls.OVERLAY["landmark"]["radius"],
                cls.OVERLAY["landmark"]["color"],
                cls.OVERLAY["landmark"]["thickness"],
            )
    
    @classmethod
    def draw_recording(cls, frame) -> None:
        cls.draw_item(
            frame,
            "recording",
            "REC",
        )

    @classmethod
    def draw_status(cls, frame, status: str) -> None:
        cls.draw_item(
            frame,
            "status",
            status,
        )

    @classmethod
    def draw_gaze(cls, frame, gaze: str) -> None:
        cls.draw_item(
            frame,
            "gaze",
            gaze,
        )

    @classmethod
    def draw_timestamp(cls, frame, timestamp: str) -> None:
        cls.draw_item(
            frame,
            "timestamp",
            timestamp,
        )

    # ------------------------------------------------------------------
    # Overlay
    # ------------------------------------------------------------------

    @classmethod
    def draw_overlay(
        cls,
        frame,
        fps: float,
        frame_count: int,
        blink: bool = False,
        landmarks = None,
    ) -> None:
        """Draw default overlay."""
        cls.draw_fps(frame, fps)
        cls.draw_frame_count(frame, frame_count)
        cls.draw_blink(frame, blink)
        cls.draw_landmarks(frame, landmarks)