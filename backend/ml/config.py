"""Configuration schema and management for EVision Telangana ML Infrastructure.

This module defines configuration dataclasses to support model paths,
dataset paths, random seeds, logging configuration, and model versioning.
"""

import json
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Dict, Optional

from ml.constants import (
    DEFAULT_DATA_DIR,
    DEFAULT_EVALUATION_DIR,
    DEFAULT_LOG_FORMAT,
    DEFAULT_LOG_LEVEL,
    DEFAULT_RANDOM_SEED,
    DEFAULT_TRAINED_MODELS_DIR,
    PACKAGE_VERSION,
)


@dataclass
class DatasetConfig:
    """Configuration for dataset paths."""
    data_dir: Path = DEFAULT_DATA_DIR
    raw_dir: Path = field(default_factory=lambda: DEFAULT_DATA_DIR / "raw")
    processed_dir: Path = field(default_factory=lambda: DEFAULT_DATA_DIR / "processed")
    train_path: Optional[Path] = None
    test_path: Optional[Path] = None

    def __post_init__(self) -> None:
        # Convert strings to Path objects if necessary
        self.data_dir = Path(self.data_dir)
        self.raw_dir = Path(self.raw_dir)
        self.processed_dir = Path(self.processed_dir)
        if self.train_path is not None:
            self.train_path = Path(self.train_path)
        if self.test_path is not None:
            self.test_path = Path(self.test_path)


@dataclass
class ModelConfig:
    """Configuration for model paths, parameters, and metadata."""
    model_name: str
    model_version: str = "1.0.0"
    model_dir: Path = DEFAULT_TRAINED_MODELS_DIR
    hyperparameters: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.model_dir = Path(self.model_dir)


@dataclass
class LoggingConfig:
    """Configuration for logging."""
    level: str = DEFAULT_LOG_LEVEL
    format: str = DEFAULT_LOG_FORMAT
    log_file: Optional[Path] = None

    def __post_init__(self) -> None:
        if self.log_file is not None:
            self.log_file = Path(self.log_file)


@dataclass
class SystemConfig:
    """General system and environment configuration."""
    random_seed: int = DEFAULT_RANDOM_SEED
    package_version: str = PACKAGE_VERSION
    output_dir: Path = DEFAULT_EVALUATION_DIR

    def __post_init__(self) -> None:
        self.output_dir = Path(self.output_dir)


@dataclass
class MLConfig:
    """Unified configuration for the ML package."""
    model: ModelConfig
    dataset: DatasetConfig = field(default_factory=DatasetConfig)
    logging: LoggingConfig = field(default_factory=LoggingConfig)
    system: SystemConfig = field(default_factory=SystemConfig)

    def to_dict(self) -> Dict[str, Any]:
        """Convert the configuration to a dictionary, converting Path objects to strings."""
        def serialize_paths(obj: Any) -> Any:
            if isinstance(obj, dict):
                return {k: serialize_paths(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [serialize_paths(v) for v in obj]
            elif isinstance(obj, Path):
                return str(obj)
            return obj

        return serialize_paths(asdict(self))

    def save(self, filepath: Path) -> None:
        """Save configuration as a JSON file."""
        filepath = Path(filepath)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=4)

    @classmethod
    def load(cls, filepath: Path) -> "MLConfig":
        """Load configuration from a JSON file."""
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Deserialize paths and rebuild config hierarchy
        dataset_data = data.get("dataset", {})
        if "data_dir" in dataset_data:
            dataset_data["data_dir"] = Path(dataset_data["data_dir"])
        if "raw_dir" in dataset_data:
            dataset_data["raw_dir"] = Path(dataset_data["raw_dir"])
        if "processed_dir" in dataset_data:
            dataset_data["processed_dir"] = Path(dataset_data["processed_dir"])
        if dataset_data.get("train_path"):
            dataset_data["train_path"] = Path(dataset_data["train_path"])
        if dataset_data.get("test_path"):
            dataset_data["test_path"] = Path(dataset_data["test_path"])

        model_data = data.get("model", {})
        if "model_dir" in model_data:
            model_data["model_dir"] = Path(model_data["model_dir"])

        logging_data = data.get("logging", {})
        if logging_data.get("log_file"):
            logging_data["log_file"] = Path(logging_data["log_file"])

        system_data = data.get("system", {})
        if "output_dir" in system_data:
            system_data["output_dir"] = Path(system_data["output_dir"])

        return cls(
            model=ModelConfig(**model_data),
            dataset=DatasetConfig(**dataset_data),
            logging=LoggingConfig(**logging_data),
            system=SystemConfig(**system_data),
        )
