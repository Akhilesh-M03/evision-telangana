"""Inference pipeline for EVision Telangana ML Infrastructure.

This module implements a standard pipeline structure that chains optional preprocessing,
prediction, and optional postprocessing.
"""

from typing import Any, Callable, Optional

from ml.inference.predictor import Predictor


class InferencePipeline:
    """Orchestrator to run raw input data through preprocessing, inference, and postprocessing."""

    def __init__(
        self,
        predictor: Predictor,
        preprocessor: Optional[Callable[[Any], Any]] = None,
        postprocessor: Optional[Callable[[Any], Any]] = None,
    ) -> None:
        """Initialize the inference pipeline.

        Args:
            predictor: Instantiated Predictor.
            preprocessor: Optional function to transform/preprocess inputs before inference.
            postprocessor: Optional function to format/transform predictions after inference.
        """
        self.predictor = predictor
        self.preprocessor = preprocessor
        self.postprocessor = postprocessor

    def run(self, raw_input: Any) -> Any:
        """Run the end-to-end pipeline.

        Args:
            raw_input: Raw data payload.

        Returns:
            The processed model predictions.
        """
        # 1. Preprocessing (if defined)
        inputs = raw_input
        if self.preprocessor is not None:
            inputs = self.preprocessor(inputs)

        # 2. Model Prediction
        preds = self.predictor.predict(inputs)

        # 3. Postprocessing (if defined)
        outputs = preds
        if self.postprocessor is not None:
            outputs = self.postprocessor(outputs)

        return outputs
