"""Model loading framework with caching for EVision Telangana ML Infrastructure.

This module provides a ModelLoader that loads persisted models, resolves their
wrapper classes using the ModelRegistry, and caches loaded instances in memory.
"""

import logging
from pathlib import Path
from typing import Dict, Type, Union

from ml.models.base import BaseModel
from ml.models.registry import ModelRegistry
from ml.training.persistence import ModelPersistence
from ml.constants import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class ModelLoader:
    """Caching model loader to retrieve and instantiate persisted model wrappers."""

    _cache: Dict[str, BaseModel] = {}

    @classmethod
    def load(cls, filepath: Union[str, Path], use_cache: bool = True) -> BaseModel:
        """Load, wrap, and cache a persisted model from disk.

        Args:
            filepath: Path to the serialized model file.
            use_cache: If True, retrieve from cache or store in cache after load.

        Returns:
            An instantiated and fitted BaseModel subclass.
        """
        path_str = str(Path(filepath).resolve())

        if use_cache and path_str in cls._cache:
            logger.info(f"Retrieving cached model instance for: {path_str}")
            return cls._cache[path_str]

        # 1. Load raw model object and metadata
        model_obj, metadata = ModelPersistence.load_model(Path(filepath))

        model_type = metadata.get("model_type")
        if not model_type:
            raise ValueError(f"Metadata loaded from {filepath} does not contain 'model_type'.")

        # 2. Lookup corresponding wrapper class in the registry
        wrapper_class = ModelRegistry.get_model_class(model_type)

        # 3. Instantiate wrapper class and set internal states
        model_name = metadata.get("model_name", wrapper_class.__name__)
        version = metadata.get("version", "1.0.0")
        hyperparameters = metadata.get("hyperparameters", {})

        wrapper = wrapper_class(
            model_name=model_name,
            version=version,
            hyperparameters=hyperparameters,
        )
        wrapper._model = model_obj
        wrapper._is_fitted = metadata.get("is_fitted", True)

        # 4. Cache model
        if use_cache:
            cls._cache[path_str] = wrapper

        return wrapper

    @classmethod
    def clear_cache(cls) -> None:
        """Clear all cached model instances from memory."""
        cls._cache.clear()
        logger.info("Cleared model cache.")
