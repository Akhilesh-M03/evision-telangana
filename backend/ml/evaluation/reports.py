"""Evaluation report generation for EVision Telangana ML Infrastructure.

This module provides tools to compile evaluation statistics and output them
to JSON or Markdown files.
"""

from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any, Dict, Optional, Union

import numpy as np
import pandas as pd

from ml.evaluation.metrics import MetricEvaluator
from ml.models.base import BaseModel


class EvaluationReport:
    """Wrapper class holding and presenting evaluation metrics, metadata, and artifacts."""

    def __init__(
        self,
        model_metadata: Dict[str, Any],
        dataset_metadata: Dict[str, Any],
        metrics: Dict[str, Any],
        timestamp: Optional[str] = None,
    ) -> None:
        """Initialize the evaluation report.

        Args:
            model_metadata: Dict describing the evaluated model.
            dataset_metadata: Dict describing the test/evaluation dataset.
            metrics: Dict containing performance metrics.
            timestamp: Iso-formatted timestamp. Defaults to now.
        """
        self.model_metadata = model_metadata
        self.dataset_metadata = dataset_metadata
        self.metrics = metrics
        self.timestamp = timestamp or datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    @classmethod
    def generate(
        cls,
        model: BaseModel,
        X: Union[np.ndarray, pd.DataFrame],
        y: Union[np.ndarray, pd.Series],
        y_pred: np.ndarray,
        y_prob: Optional[np.ndarray] = None,
        task: str = "regression",
    ) -> "EvaluationReport":
        """Factory method to generate a report from a model and predictions.

        Args:
            model: The wrapper model used for predictions.
            X: Input dataset features.
            y: Ground truth targets.
            y_pred: Model predictions.
            y_prob: Model class probabilities (if classification).
            task: Task type: 'regression' | 'classification'.

        Returns:
            An instantiated EvaluationReport.
        """
        model_metadata = {
            "model_name": model.model_name,
            "model_type": model.model_type,
            "version": model.version,
            "hyperparameters": model.hyperparameters,
        }

        # Dataset dimensions and properties
        dataset_metadata = {
            "sample_count": len(X),
            "feature_count": X.shape[1] if len(X.shape) > 1 else 1,
            "features": list(X.columns) if isinstance(X, pd.DataFrame) else None,
        }

        if task == "regression":
            metrics = MetricEvaluator.compute_regression_metrics(y, y_pred)
        else:
            metrics = MetricEvaluator.compute_classification_metrics(y, y_pred, y_prob)

        return cls(
            model_metadata=model_metadata,
            dataset_metadata=dataset_metadata,
            metrics=metrics,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert the report to a dictionary representation."""
        return {
            "timestamp": self.timestamp,
            "model": self.model_metadata,
            "dataset": self.dataset_metadata,
            "metrics": self.metrics,
        }

    def save_json(self, filepath: Path) -> Path:
        """Save the report as a JSON file.

        Args:
            filepath: Destination Path.
        """
        filepath = Path(filepath)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=4)
        return filepath

    def to_markdown(self) -> str:
        """Generate a formatted markdown string representing the report."""
        md = []
        md.append(f"# Model Evaluation Report ({self.model_metadata['model_name']})")
        md.append(f"**Timestamp:** {self.timestamp}  ")
        md.append(f"**Model Version:** {self.model_metadata['version']}  ")
        md.append(f"**Model Type:** {self.model_metadata['model_type']}  \n")

        md.append("## Dataset Summary")
        md.append(f"- **Sample Count:** {self.dataset_metadata['sample_count']}")
        md.append(f"- **Feature Count:** {self.dataset_metadata['feature_count']}")
        if self.dataset_metadata["features"]:
            feats = ", ".join(self.dataset_metadata["features"])
            md.append(f"- **Features:** {feats}")
        md.append("\n")

        md.append("## Performance Metrics")
        for metric, value in self.metrics.items():
            if metric == "confusion_matrix":
                continue
            if value is None:
                md.append(f"- **{metric.replace('_', ' ').title()}:** N/A")
            else:
                md.append(f"- **{metric.replace('_', ' ').title()}:** {value:.6f}")

        if "confusion_matrix" in self.metrics:
            md.append("\n## Confusion Matrix")
            md.append("```")
            md.append(str(np.array(self.metrics["confusion_matrix"])))
            md.append("```")

        md.append("\n## Hyperparameters")
        md.append("```json")
        md.append(json.dumps(self.model_metadata["hyperparameters"], indent=2))
        md.append("```")

        return "\n".join(md)

    def save_markdown(self, filepath: Path) -> Path:
        """Save the report as a Markdown file.

        Args:
            filepath: Destination Path.
        """
        filepath = Path(filepath)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(self.to_markdown())
        return filepath
