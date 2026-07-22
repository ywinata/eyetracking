from pathlib import Path

import yaml

from .settings import (
    CameraConfig,
    WindowConfig,
    LoggingConfig,
    ResultConfig,
    ExperimentConfig,
    UIConfig,
    Settings,
)


def load_settings():

    config_file = Path(__file__).parent / "default.yaml"

    with open(config_file, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    return Settings(
        camera=CameraConfig(**cfg["camera"]),
        window=WindowConfig(**cfg["window"]),
        logging=LoggingConfig(**cfg["logging"]),
        results=ResultConfig(**cfg["results"]),
        experiment=ExperimentConfig(**cfg["experiment"]),
        ui=UIConfig(**cfg["ui"]),
    )

settings = load_settings()