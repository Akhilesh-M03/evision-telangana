"""Evaluation package initialization.

Exposes metrics calculations, report builders, and cross-validation utilities.
"""

from ml.evaluation.cross_validation import CrossValidator
from ml.evaluation.metrics import MetricEvaluator
from ml.evaluation.reports import EvaluationReport

__all__ = [
    "CrossValidator",
    "MetricEvaluator",
    "EvaluationReport",
]
