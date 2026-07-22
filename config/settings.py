from dataclasses import dataclass

@dataclass(slots=True)
class CameraConfig:
    index: int
    width: int
    height: int
    fps: int


@dataclass(slots=True)
class WindowConfig:
    title: str
    fullscreen: bool


@dataclass(slots=True)
class LoggingConfig:
    directory: str
    level: str
    format: str


@dataclass(slots=True)
class ResultConfig:
    directory: str


@dataclass(slots=True)
class ExperimentConfig:
    screenshot_key: str
    exit_key: str


@dataclass(slots=True)
class Settings:
    camera: CameraConfig
    window: WindowConfig
    logging: LoggingConfig
    results: ResultConfig
    experiment: ExperimentConfig

@dataclass(slots=True)
class UIConfig:
    font_scale: float
    font_thickness: int

@dataclass(slots=True)
class Settings:
    camera: CameraConfig
    window: WindowConfig
    logging: LoggingConfig
    results: ResultConfig
    experiment: ExperimentConfig
    ui: UIConfig