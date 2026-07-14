"""Utility functions for EVision Telangana ML Infrastructure.

This module provides utility functions for logging setup, setting random seeds,
and managing directories and file paths.
"""

import logging
import os
import random
from pathlib import Path
from typing import Optional

import numpy as np

from ml.config import LoggingConfig
from ml.constants import LOGGER_NAME


def setup_logging(config: LoggingConfig) -> logging.Logger:
    """Configure the global logger according to LoggingConfig.

    Args:
        config: A LoggingConfig instance.

    Returns:
        The configured Logger instance.
    """
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(config.level)

    # Prevent duplicating handlers if they are already added
    if not logger.handlers:
        formatter = logging.Formatter(config.format)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # File handler (if specified)
        if config.log_file is not None:
            config.log_file.parent.mkdir(parents=True, exist_ok=True)
            file_handler = logging.FileHandler(config.log_file, encoding="utf-8")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

    return logger


def set_seed(seed: int) -> None:
    """Initialize random seeds across all libraries for reproducibility.

    Args:
        seed: The integer random seed to use.
    """
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    np.random.seed(seed)


def ensure_dir(path: Path) -> Path:
    """Ensure that the parent directory of a path (or the path itself if directory) exists.

    Args:
        path: Path object to create.

    Returns:
        The verified Path object.
    """
    path = Path(path)
    if path.suffix:  # It's a file path
        path.parent.mkdir(parents=True, exist_ok=True)
    else:  # It's a directory path
        path.mkdir(parents=True, exist_ok=True)
    return path


def get_model_path(
    model_dir: Path,
    model_name: str,
    model_version: str,
    extension: str = ".joblib"
) -> Path:
    """Generate a standardized model file path based on name, version, and directory.

    Args:
        model_dir: Base directory where models are stored.
        model_name: Name of the model.
        model_version: Version of the model.
        extension: File extension including the leading dot.

    Returns:
        The standardized Path for the model file.
    """
    sanitized_name = model_name.replace(" ", "_").lower()
    sanitized_version = model_version.replace(".", "_")
    filename = f"{sanitized_name}_v{sanitized_version}{extension}"
    return Path(model_dir) / filename
