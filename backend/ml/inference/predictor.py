"""Predictor module for EVision Telangana ML Infrastructure.

This module provides a unified Predictor interface to execute predictions and
handle input data conversion.
"""

from typing import Any, Dict, List, Union

import numpy as np
import pandas as pd

from ml.models.base import BaseModel


class Predictor:
    """Predictor class wrapping a BaseModel to standardize inference executions."""

    def __init__(self, model: BaseModel) -> None:
        """Initialize the predictor.

        Args:
            model: An instantiated and fitted BaseModel wrapper.
        """
        if not model.is_fitted:
            raise ValueError("Model passed to Predictor must be fitted.")
        self.model = model

    def _convert_input(
        self,
        data: Union[np.ndarray, pd.DataFrame, List[Any], Dict[str, Any]]
    ) -> Union[np.ndarray, pd.DataFrame]:
        """Convert input structures (dicts, lists) into pandas DataFrame or numpy arrays.

        Args:
            data: Raw input data.

        Returns:
            Sanitized numpy array or pandas DataFrame.
        """
        if isinstance(data, (np.ndarray, pd.DataFrame)):
            return data

        if isinstance(data, pd.Series):
            return data.to_frame().T

        if isinstance(data, dict):
            # Single sample representation as key-value pairs
            # If values are not lists, treat as a single sample
            first_val = next(iter(data.values()))
            if not isinstance(first_val, list):
                return pd.DataFrame([data])
            return pd.DataFrame(data)

        if isinstance(data, list):
            # List of samples (each can be dict, list, etc.)
            if len(data) > 0 and isinstance(data[0], dict):
                return pd.DataFrame(data)
            return np.asarray(data)

        raise TypeError(
            f"Unsupported input type '{type(data)}'. "
            "Must be numpy array, pandas DataFrame/Series, list of features, or dictionary."
        )

    def predict(
        self,
        data: Union[np.ndarray, pd.DataFrame, List[Any], Dict[str, Any]]
    ) -> np.ndarray:
        """Execute model prediction.

        Args:
            data: Raw feature inputs.

        Returns:
            A numpy array of prediction values.
        """
        converted = self._convert_input(data)
        return self.model.predict(converted)

    def predict_proba(
        self,
        data: Union[np.ndarray, pd.DataFrame, List[Any], Dict[str, Any]]
    ) -> np.ndarray:
        """Execute prediction probabilities (only for classification).

        Args:
            data: Raw feature inputs.

        Returns:
            A numpy array of prediction probabilities.
        """
        converted = self._convert_input(data)
        return self.model.predict_proba(converted)
