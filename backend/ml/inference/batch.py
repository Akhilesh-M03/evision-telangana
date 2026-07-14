"""Batch prediction interface for EVision Telangana ML Infrastructure.

This module provides a BatchPredictor that handles chunking and batch predictions
for large pandas DataFrames or lists, preserving input indices.
"""

from typing import Any, Iterable, Iterator, List, Optional, Union

import numpy as np
import pandas as pd

from ml.inference.predictor import Predictor


class BatchPredictor:
    """Batch prediction runner to process large datasets in configurable chunks."""

    def __init__(self, predictor: Predictor, default_batch_size: int = 1000) -> None:
        """Initialize the batch predictor.

        Args:
            predictor: The underlying Predictor instance.
            default_batch_size: Chunk size to process large datasets in.
        """
        self.predictor = predictor
        self.default_batch_size = default_batch_size

    def predict_batch(
        self,
        data: Union[pd.DataFrame, np.ndarray, List[Any]],
        batch_size: Optional[int] = None
    ) -> Union[pd.Series, np.ndarray]:
        """Perform predictions on the full dataset in chunks, matching indices if pandas.

        Args:
            data: Fully populated input dataset.
            batch_size: Override size of chunks.

        Returns:
            A pandas Series (if input is DataFrame) or numpy array matching index alignment.
        """
        chunk_size = batch_size if batch_size is not None else self.default_batch_size
        n_samples = len(data)

        if n_samples == 0:
            return np.array([])

        predictions: List[np.ndarray] = []

        # Process in chunks
        for start_idx in range(0, n_samples, chunk_size):
            end_idx = min(start_idx + chunk_size, n_samples)
            if isinstance(data, pd.DataFrame):
                chunk = data.iloc[start_idx:end_idx]
            else:
                chunk = data[start_idx:end_idx]

            chunk_preds = self.predictor.predict(chunk)
            predictions.append(chunk_preds)

        flat_preds = np.concatenate(predictions)

        # Preserve indices for Pandas input
        if isinstance(data, pd.DataFrame):
            return pd.Series(flat_preds, index=data.index, name="prediction")

        return flat_preds

    def predict_stream(
        self,
        stream: Iterable[Any],
        batch_size: Optional[int] = None
    ) -> Iterator[np.ndarray]:
        """Generate predictions for a stream of records.

        Args:
            stream: Iterable supplying records sequentially.
            batch_size: Chunk size to bundle stream records before executing predictions.

        Yields:
            Numpy arrays of predictions for each batched chunk.
        """
        chunk_size = batch_size if batch_size is not None else self.default_batch_size
        batch: List[Any] = []

        for record in stream:
            batch.append(record)
            if len(batch) >= chunk_size:
                yield self.predictor.predict(batch)
                batch = []

        # Process final partial batch
        if batch:
            yield self.predictor.predict(batch)
