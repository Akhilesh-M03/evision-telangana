"""EVision Telangana Machine Learning Infrastructure package.

This package provides a production-grade machine learning architecture, including
configuration management, model registries, data splitting, training wrappers,
metrics evaluation, reports, cross-validation, and batch/stream inference pipelines.
"""

from ml.config import (
    DatasetConfig,
    LoggingConfig,
    MLConfig,
    ModelConfig,
    SystemConfig,
)
from ml.constants import (
    DEFAULT_RANDOM_SEED,
    MODEL_TYPE_KMEANS,
    MODEL_TYPE_RANDOM_FOREST,
    MODEL_TYPE_XGBOOST,
    PACKAGE_VERSION,
)
from ml.models.base import BaseModel
from ml.models.registry import ModelRegistry

# Trigger registrations of models
import ml.training.random_forest
import ml.training.xgboost
import ml.clustering.kmeans

__all__ = [
    # Configs
    "MLConfig",
    "ModelConfig",
    "DatasetConfig",
    "LoggingConfig",
    "SystemConfig",
    # Constants
    "PACKAGE_VERSION",
    "DEFAULT_RANDOM_SEED",
    "MODEL_TYPE_RANDOM_FOREST",
    "MODEL_TYPE_XGBOOST",
    "MODEL_TYPE_KMEANS",
    # Models
    "BaseModel",
    "ModelRegistry",
]
