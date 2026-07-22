import logging
from datetime import datetime
from pathlib import Path

from config import settings


def get_logger(name: str) -> logging.Logger:
    """
    Create or return a configured logger.

    Parameters
    ----------
    name : str
        Logger name (e.g. "Camera", "Calibration")

    Returns
    -------
    logging.Logger
    """

    logger = logging.getLogger(name)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    # Create log directory
    log_dir = Path(settings.logging.directory)
    log_dir.mkdir(parents=True, exist_ok=True)

    # Log filename
    logfile = log_dir / f"{datetime.now():%Y%m%d_%H%M%S}.log"

    # Logger configuration
    logger.setLevel(
        getattr(logging, settings.logging.level.upper(), logging.INFO)
    )

    logger.propagate = False

    # Formatter
    formatter = logging.Formatter(
        settings.logging.format
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File handler
    file_handler = logging.FileHandler(
        logfile,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    # Register handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    # Session header
    logger.info("=" * 60)
    logger.info("Logger initialized")
    logger.info("Log file : %s", logfile)
    logger.info("=" * 60)

    return logger