"""KMeans Clustering Wrapper for EVision Telangana ML Infrastructure.

This module implements a BaseModel wrapper around scikit-learn's KMeans clustering model.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Union

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

from ml.constants import MODEL_TYPE_KMEANS
from ml.models.base import BaseModel
from ml.models.registry import ModelRegistry
from ml.training.persistence import ModelPersistence


@ModelRegistry.register(MODEL_TYPE_KMEANS)
class KMeansClustering(BaseModel):
    """Wrapper class for scikit-learn's KMeans clustering algorithm."""

    def __init__(
        self,
        model_name: str = "KMeans",
        version: str = "1.0.0",
        hyperparameters: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Initialize KMeans settings.

        Args:
            model_name: Human readable name.
            version: Model version.
            hyperparameters: Configurations. All keys are forwarded to sklearn's KMeans.
        """
        super().__init__(
            model_name=model_name,
            model_type=MODEL_TYPE_KMEANS,
            version=version,
            hyperparameters=hyperparameters,
        )
        self.kmeans_params = self.hyperparameters.copy()
        self.kmeans_params.setdefault("n_clusters", 5)
        self.kmeans_params.setdefault("random_state", 42)
        self.kmeans_params.setdefault("n_init", "auto")

        self._model = KMeans(**self.kmeans_params)

    def fit(
        self,
        X: Union[np.ndarray, pd.DataFrame],
        y: Optional[Union[np.ndarray, pd.Series, pd.DataFrame]] = None,
    ) -> "KMeansClustering":
        """Fit KMeans clustering on features X.

        Args:
            X: Clustering inputs.
            y: Ignored (here for signature compatibility).
        """
        self._model.fit(X)
        self._is_fitted = True
        return self

    def predict(self, X: Union[np.ndarray, pd.DataFrame]) -> np.ndarray:
        """Predict the closest cluster each sample in X belongs to.

        Args:
            X: Input features.
        """
        if not self._is_fitted:
            raise ValueError("KMeans model must be fitted before running predict.")
        return self._model.predict(X)

    def predict_proba(self, X: Union[np.ndarray, pd.DataFrame]) -> np.ndarray:
        """Predict probabilities (not supported for KMeans)."""
        raise NotImplementedError("predict_proba is not supported for clustering algorithms.")

    @property
    def cluster_centers(self) -> np.ndarray:
        """Retrieve the cluster centroids coordinates."""
        if not self._is_fitted:
            raise ValueError("Model not fitted.")
        return self._model.cluster_centers_

    @property
    def inertia(self) -> float:
        """Retrieve the inertia (sum of squared distances to closest centroid)."""
        if not self._is_fitted:
            raise ValueError("Model not fitted.")
        return float(self._model.inertia_)

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
            "is_fitted": self._is_fitted,
        }
        ModelPersistence.save_model(self._model, filepath, metadata)

    def load(self, filepath: Path) -> "KMeansClustering":
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
        self._is_fitted = metadata.get("is_fitted", True)
        return self
