"""Model persistence framework for EVision Telangana ML Infrastructure.

This module provides functionality to save and load models using joblib,
including checks for versions, metadata, and compatibility.
"""

import logging
from pathlib import Path
from typing import Any, Dict, Optional, Tuple, Union

import joblib

from ml.constants import LOGGER_NAME, PACKAGE_VERSION

logger = logging.getLogger(LOGGER_NAME)


class ModelPersistence:
    """Helper class to handle model serialization, deserialization, and metadata logging."""

    @staticmethod
    def save_model(
        model: Any,
        filepath: Path,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Path:
        """Serialize a model and its metadata and save to disk.

        Args:
            model: The underlying fitted model object or wrapper to save.
            filepath: Target Path to save the model.
            metadata: Optional dictionary of metadata parameters to persist.

        Returns:
            The resolved output filepath.
        """
        filepath = Path(filepath)
        filepath.parent.mkdir(parents=True, exist_ok=True)

        meta = metadata or {}
        # Ensure system package version is tracked
        meta.setdefault("package_version", PACKAGE_VERSION)

        payload = {
            "model": model,
            "metadata": meta,
        }

        joblib.dump(payload, filepath)
        logger.info(f"Successfully persisted model to {filepath} with metadata: {meta}")
        return filepath

    @staticmethod
    def load_model(filepath: Path) -> Tuple[Any, Dict[str, Any]]:
        """Load and deserialize a model and its metadata from disk.

        Args:
            filepath: Path to the serialized model file.

        Returns:
            A tuple of (model_object, metadata_dict).

        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file is not a valid model payload.
        """
        filepath = Path(filepath)
        if not filepath.exists():
            raise FileNotFoundError(f"Model file not found at {filepath}")

        payload = joblib.load(filepath)

        if not isinstance(payload, dict) or "model" not in payload:
            raise ValueError(f"Invalid model payload format loaded from {filepath}")

        model = payload["model"]
        metadata = payload.get("metadata", {})

        # Log warning if version mismatch occurs
        loaded_ver = metadata.get("package_version")
        if loaded_ver != PACKAGE_VERSION:
            logger.warning(
                f"Model package version mismatch. Loaded: {loaded_ver}, Current: {PACKAGE_VERSION}."
            )

        logger.info(f"Successfully loaded model from {filepath}")
        return model, metadata
