"""XGBoost Model Wrapper for EVision Telangana ML Infrastructure.

This module implements a BaseModel wrapper around xgboost's scikit-learn API.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Union

import numpy as np
import pandas as pd
from xgboost import XGBClassifier, XGBRegressor

from ml.constants import MODEL_TYPE_XGBOOST
from ml.models.base import BaseModel
from ml.models.registry import ModelRegistry
from ml.training.persistence import ModelPersistence


@ModelRegistry.register(MODEL_TYPE_XGBOOST)
class XGBoostModel(BaseModel):
    """Wrapper class for xgboost's XGBClassifier and XGBRegressor."""

    def __init__(
        self,
        model_name: str = "XGBoost",
        version: str = "1.0.0",
        hyperparameters: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Initialize XGBoost model settings.

        Args:
            model_name: Human readable name.
            version: Model version.
            hyperparameters: Configurations. Supported key 'task': 'regression' | 'classification'.
                All other keys are forwarded to xgboost's wrappers.
        """
        super().__init__(
            model_name=model_name,
            model_type=MODEL_TYPE_XGBOOST,
            version=version,
            hyperparameters=hyperparameters,
        )
        self.task = self.hyperparameters.get("task", "regression")

        # Extract underlying hyperparameters to pass to XGBoost constructor
        self.xgb_params = self.hyperparameters.copy()
        self.xgb_params.pop("task", None)

        # Set default random state if not provided
        self.xgb_params.setdefault("random_state", 42)

        if self.task == "regression":
            self._model = XGBRegressor(**self.xgb_params)
        elif self.task == "classification":
            self._model = XGBClassifier(**self.xgb_params)
        else:
            raise ValueError(f"Invalid task type '{self.task}'. Must be 'regression' or 'classification'.")

    def fit(
        self,
        X: Union[np.ndarray, pd.DataFrame],
        y: Union[np.ndarray, pd.Series, pd.DataFrame],
    ) -> "XGBoostModel":
        """Fit the XGBoost model.

        Args:
            X: Training features.
            y: Training labels.
        """
        if isinstance(y, (pd.Series, pd.DataFrame)):
            if isinstance(y, pd.DataFrame) and y.shape[1] == 1:
                y = y.iloc[:, 0]

        self._model.fit(X, y)
        self._is_fitted = True
        return self

    def predict(self, X: Union[np.ndarray, pd.DataFrame]) -> np.ndarray:
        """Predict target values.

        Args:
            X: Input features.
        """
        if not self._is_fitted:
            raise ValueError("Model must be fitted before running predict.")
        return self._model.predict(X)

    def predict_proba(self, X: Union[np.ndarray, pd.DataFrame]) -> np.ndarray:
        """Predict class probabilities (only supported for classification task).

        Args:
            X: Input features.
        """
        if not self._is_fitted:
            raise ValueError("Model must be fitted before running predict_proba.")
        if self.task != "classification":
            raise NotImplementedError("predict_proba is only supported for classification tasks.")
        return self._model.predict_proba(X)

    def save(self, filepath: Path) -> None:
        """Save model checkpoint to disk.

        Args:
            filepath: Path to write the serialized file.
        """
        metadata = {
            "model_name": self.model_name,
            "model_type": self.model_type,
            "version": self.version,
            "hyperparameters": self.hyperparameters,
            "task": self.task,
            "is_fitted": self._is_fitted,
        }
        ModelPersistence.save_model(self._model, filepath, metadata)

    def load(self, filepath: Path) -> "XGBoostModel":
        """Load model checkpoint from disk.

        Args:
            filepath: Path to the serialized file.
        """
        model_obj, metadata = ModelPersistence.load_model(filepath)
        self._model = model_obj
        self.model_name = metadata.get("model_name", self.model_name)
        self.model_type = metadata.get("model_type", self.model_type)
        self.version = metadata.get("version", self.version)
        self.hyperparameters = metadata.get("hyperparameters", self.hyperparameters)
        self.task = metadata.get("task", "regression")
        self._is_fitted = metadata.get("is_fitted", True)
        return self
