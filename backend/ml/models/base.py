"""Abstract Base Class for Machine Learning Models.

This module defines the standard interface for all model wrappers in the
EVision Telangana ML package.
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, Optional, Tuple, Union

import numpy as np
import pandas as pd


class BaseModel(ABC):
    """Abstract Base Class representing a machine learning model wrapper."""

    def __init__(
        self,
        model_name: str,
        model_type: str,
        version: str = "1.0.0",
        hyperparameters: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Initialize the base model settings.

        Args:
            model_name: Descriptive name of the model.
            model_type: Identifier of the model type.
            version: Semantic version of the model.
            hyperparameters: Dict of hyperparameter configurations.
        """
        self.model_name = model_name
        self.model_type = model_type
        self.version = version
        self.hyperparameters = hyperparameters or {}
        self._is_fitted = False
        self._model: Any = None

    @property
    def is_fitted(self) -> bool:
        """Indicate whether the underlying model has been trained."""
        return self._is_fitted

    @property
    def model(self) -> Any:
        """Retrieve the raw underlying model object."""
        return self._model

    @abstractmethod
    def fit(
        self,
        X: Union[np.ndarray, pd.DataFrame],
        y: Union[np.ndarray, pd.Series, pd.DataFrame],
    ) -> "BaseModel":
        """Train the model on features X and targets y.

        Args:
            X: Training features.
            y: Training targets.

        Returns:
            The model instance itself.
        """
        pass

    @abstractmethod
    def predict(self, X: Union[np.ndarray, pd.DataFrame]) -> np.ndarray:
        """Generate predictions for features X.

        Args:
            X: Input features.

        Returns:
            An array of predictions.
        """
        pass

    @abstractmethod
    def predict_proba(self, X: Union[np.ndarray, pd.DataFrame]) -> np.ndarray:
        """Generate prediction probabilities for features X (for classifiers).

        Args:
            X: Input features.

        Returns:
            An array of prediction probabilities.
        """
        pass

    @abstractmethod
    def save(self, filepath: Path) -> None:
        """Serialize and save the model to a file.

        Args:
            filepath: Path where the model will be stored.
        """
        pass

    @abstractmethod
    def load(self, filepath: Path) -> "BaseModel":
        """Load and deserialize a model from a file.

        Args:
            filepath: Path from where the model will be loaded.

        Returns:
            The loaded model instance.
        """
        pass
