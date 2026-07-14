"""Cross-validation framework for EVision Telangana ML Infrastructure.

This module provides cross-validation utilities to train and evaluate models
across multiple data folds using KFold or StratifiedKFold.
"""

from typing import Any, Dict, List, Type, Union

import numpy as np
import pandas as pd
from sklearn.model_selection import KFold, StratifiedKFold

from ml.constants import DEFAULT_RANDOM_SEED
from ml.evaluation.metrics import MetricEvaluator
from ml.models.base import BaseModel


class CrossValidator:
    """Helper class to run cross-validation on arbitrary registered models."""

    def __init__(
        self,
        n_splits: int = 5,
        shuffle: bool = True,
        random_state: int = DEFAULT_RANDOM_SEED,
        stratified: bool = False,
    ) -> None:
        """Initialize cross-validator.

        Args:
            n_splits: Number of cross-validation folds.
            shuffle: Whether to shuffle data before splitting.
            random_state: Random state for splitting reproducibility.
            stratified: Use StratifiedKFold if True (only for classification).
        """
        self.n_splits = n_splits
        self.shuffle = shuffle
        self.random_state = random_state
        self.stratified = stratified

    def validate(
        self,
        model_class: Type[BaseModel],
        X: Union[np.ndarray, pd.DataFrame],
        y: Union[np.ndarray, pd.Series],
        hyperparameters: Dict[str, Any],
        task: str = "regression",
    ) -> Dict[str, Any]:
        """Execute cross-validation.

        Args:
            model_class: The subclass of BaseModel to instantiate in each fold.
            X: Input dataset features.
            y: Ground truth targets.
            hyperparameters: Dict of hyperparams to instantiate the model wrappers with.
            task: Task type: 'regression' | 'classification'.

        Returns:
            A summary dictionary containing fold details, means, and std deviations of metrics.
        """
        # Convert X, y to numpy arrays for indexing if they are pandas DataFrames/Series
        X_arr = X.to_numpy() if isinstance(X, pd.DataFrame) else np.asarray(X)
        y_arr = y.to_numpy() if isinstance(y, pd.Series) else np.asarray(y)

        # Select split strategy
        if self.stratified and task == "classification":
            splitter = StratifiedKFold(
                n_splits=self.n_splits,
                shuffle=self.shuffle,
                random_state=self.random_state,
            )
        else:
            splitter = KFold(
                n_splits=self.n_splits,
                shuffle=self.shuffle,
                random_state=self.random_state,
            )

        fold_metrics: List[Dict[str, float]] = []

        # Run folds
        for fold, (train_idx, val_idx) in enumerate(splitter.split(X_arr, y_arr)):
            X_train, X_val = X_arr[train_idx], X_arr[val_idx]
            y_train, y_val = y_arr[train_idx], y_arr[val_idx]

            # Re-convert to DataFrame/Series if input was pandas to preserve interface compatibility
            if isinstance(X, pd.DataFrame):
                X_train = pd.DataFrame(X_train, columns=X.columns)
                X_val = pd.DataFrame(X_val, columns=X.columns)
            if isinstance(y, pd.Series):
                y_train = pd.Series(y_train, name=y.name)
                y_val = pd.Series(y_val, name=y.name)

            # Instantiate a fresh model instance for the fold
            model_inst = model_class(
                model_name=f"{model_class.__name__}_fold_{fold}",
                version="1.0.0",
                hyperparameters=hyperparameters,
            )

            # Fit and predict
            model_inst.fit(X_train, y_train)
            y_pred = model_inst.predict(X_val)

            y_prob = None
            if task == "classification":
                try:
                    y_prob = model_inst.predict_proba(X_val)
                except (NotImplementedError, AttributeError):
                    y_prob = None

            # Calculate fold metrics
            if task == "regression":
                metrics = MetricEvaluator.compute_regression_metrics(y_val, y_pred)
            else:
                metrics = MetricEvaluator.compute_classification_metrics(y_val, y_pred, y_prob)
                metrics.pop("confusion_matrix", None)  # Confusion matrix can't be averaged directly easily

            fold_metrics.append(metrics)

        # Aggregate metrics
        metric_keys = fold_metrics[0].keys()
        summary_mean: Dict[str, float] = {}
        summary_std: Dict[str, float] = {}

        for key in metric_keys:
            vals = [m[key] for m in fold_metrics if m[key] is not None]
            if vals:
                summary_mean[key] = float(np.mean(vals))
                summary_std[key] = float(np.std(vals))
            else:
                summary_mean[key] = None
                summary_std[key] = None

        return {
            "folds": fold_metrics,
            "mean": summary_mean,
            "std": summary_std,
        }
