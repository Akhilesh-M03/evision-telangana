"""Metrics calculation helper for EVision Telangana ML Infrastructure.

This module provides functions to calculate common regression and classification metrics.
"""

from typing import Any, Dict, Optional, Union

import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    mean_absolute_error,
    mean_squared_error,
    precision_score,
    r2_score,
    recall_score,
    roc_auc_score,
)

from ml.constants import (
    METRIC_ACCURACY,
    METRIC_F1,
    METRIC_MAE,
    METRIC_MSE,
    METRIC_PRECISION,
    METRIC_R2,
    METRIC_RECALL,
    METRIC_RMSE,
    METRIC_ROC_AUC,
)


class MetricEvaluator:
    """Helper to calculate and format evaluation metrics for machine learning models."""

    @staticmethod
    def compute_regression_metrics(
        y_true: Union[np.ndarray, pd.Series],
        y_pred: Union[np.ndarray, pd.Series],
    ) -> Dict[str, float]:
        """Calculate standard regression metrics: MSE, RMSE, MAE, R2.

        Args:
            y_true: Ground truth values.
            y_pred: Predicted values.

        Returns:
            A dictionary containing the metrics.
        """
        mse = float(mean_squared_error(y_true, y_pred))
        rmse = float(np.sqrt(mse))
        mae = float(mean_absolute_error(y_true, y_pred))
        r2 = float(r2_score(y_true, y_pred))

        return {
            METRIC_MSE: mse,
            METRIC_RMSE: rmse,
            METRIC_MAE: mae,
            METRIC_R2: r2,
        }

    @staticmethod
    def compute_classification_metrics(
        y_true: Union[np.ndarray, pd.Series],
        y_pred: Union[np.ndarray, pd.Series],
        y_prob: Optional[Union[np.ndarray, pd.Series, pd.DataFrame]] = None,
        average: str = "binary",
    ) -> Dict[str, Any]:
        """Calculate standard classification metrics: Accuracy, Precision, Recall, F1, ROC-AUC.

        Args:
            y_true: Ground truth class labels.
            y_pred: Predicted class labels.
            y_prob: Predicted class probabilities (required for ROC-AUC).
            average: Type of averaging for multi-class metrics ('binary', 'macro', 'micro', 'weighted').

        Returns:
            A dictionary containing the metrics and confusion matrix.
        """
        metrics = {
            METRIC_ACCURACY: float(accuracy_score(y_true, y_pred)),
            METRIC_PRECISION: float(precision_score(y_true, y_pred, average=average, zero_division=0)),
            METRIC_RECALL: float(recall_score(y_true, y_pred, average=average, zero_division=0)),
            METRIC_F1: float(f1_score(y_true, y_pred, average=average, zero_division=0)),
        }

        # Calculate ROC-AUC if probabilities are provided
        if y_prob is not None:
            try:
                # Handle multi-class vs binary ROC AUC
                if isinstance(y_prob, (pd.DataFrame, np.ndarray)) and len(np.unique(y_true)) > 2:
                    metrics[METRIC_ROC_AUC] = float(
                        roc_auc_score(y_true, y_prob, multi_class="ovr", average=average)
                    )
                else:
                    # For binary classification, y_prob might be 1D or 2D (probabilities of the positive class)
                    if isinstance(y_prob, (np.ndarray, pd.DataFrame)) and len(y_prob.shape) > 1 and y_prob.shape[1] == 2:
                        y_prob_pos = y_prob[:, 1]
                    else:
                        y_prob_pos = y_prob
                    metrics[METRIC_ROC_AUC] = float(roc_auc_score(y_true, y_prob_pos))
            except Exception:
                metrics[METRIC_ROC_AUC] = None

        # Add confusion matrix representation
        cm = confusion_matrix(y_true, y_pred)
        metrics["confusion_matrix"] = cm.tolist()

        return metrics
