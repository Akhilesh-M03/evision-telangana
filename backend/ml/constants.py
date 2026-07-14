"""Constants for the EVision Telangana Machine Learning Infrastructure.

This module contains package-wide constants, including defaults for paths,
seeds, logging configurations, and model identifiers.
"""

from pathlib import Path

# Package info
PACKAGE_VERSION = "0.1.0"
DEFAULT_RANDOM_SEED = 42

# Paths (resolved relative to this file's location to project root)
# This file is at backend/ml/constants.py, so its parent's parent's parent is the project root.
PROJECT_ROOT = Path(__file__).resolve().parents[2]

DEFAULT_DATA_DIR = PROJECT_ROOT / "data"
DEFAULT_MODELS_DIR = PROJECT_ROOT / "models"

DEFAULT_TRAINED_MODELS_DIR = DEFAULT_MODELS_DIR / "trained"
DEFAULT_EVALUATION_DIR = DEFAULT_MODELS_DIR / "evaluation"

# Logging defaults
DEFAULT_LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
DEFAULT_LOG_LEVEL = "INFO"
LOGGER_NAME = "evision_ml"

# Model types
MODEL_TYPE_RANDOM_FOREST = "random_forest"
MODEL_TYPE_XGBOOST = "xgboost"
MODEL_TYPE_KMEANS = "kmeans"

# Dataset splits
DEFAULT_TEST_SPLIT_SIZE = 0.2
DEFAULT_VALIDATION_SPLIT_SIZE = 0.1

# Metrics
METRIC_MSE = "mean_squared_error"
METRIC_RMSE = "root_mean_squared_error"
METRIC_MAE = "mean_absolute_error"
METRIC_R2 = "r2_score"
METRIC_ACCURACY = "accuracy"
METRIC_PRECISION = "precision"
METRIC_RECALL = "recall"
METRIC_F1 = "f1_score"
METRIC_ROC_AUC = "roc_auc"
