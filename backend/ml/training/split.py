"""Train/Test split framework for EVision Telangana ML Infrastructure.

This module provides data splitting utilities wrapping scikit-learn's split options.
"""

from typing import Optional, Tuple, Union

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from ml.constants import DEFAULT_RANDOM_SEED, DEFAULT_TEST_SPLIT_SIZE


class DataSplitter:
    """Utility class to perform standard train/test/validation splits on datasets."""

    def __init__(
        self,
        test_size: float = DEFAULT_TEST_SPLIT_SIZE,
        random_state: int = DEFAULT_RANDOM_SEED,
        shuffle: bool = True,
        stratify: Optional[Union[np.ndarray, pd.Series]] = None,
    ) -> None:
        """Initialize split parameters.

        Args:
            test_size: Proportion of dataset to include in the test split.
            random_state: Random seed for reproducibility.
            shuffle: Whether to shuffle data before splitting.
            stratify: If not None, data is split in a stratified fashion.
        """
        self.test_size = test_size
        self.random_state = random_state
        self.shuffle = shuffle
        self.stratify = stratify

    def split(
        self,
        X: Union[np.ndarray, pd.DataFrame],
        y: Union[np.ndarray, pd.Series, pd.DataFrame],
        test_size: Optional[float] = None,
    ) -> Tuple[
        Union[np.ndarray, pd.DataFrame],  # X_train
        Union[np.ndarray, pd.DataFrame],  # X_test
        Union[np.ndarray, pd.Series, pd.DataFrame],  # y_train
        Union[np.ndarray, pd.Series, pd.DataFrame],  # y_test
    ]:
        """Perform train/test split on X and y.

        Args:
            X: Dataset features.
            y: Dataset target/labels.
            test_size: Optional override for the test split size.

        Returns:
            A tuple containing (X_train, X_test, y_train, y_test).
        """
        split_test_size = test_size if test_size is not None else self.test_size
        strat = self.stratify if self.shuffle else None

        return train_test_split(
            X,
            y,
            test_size=split_test_size,
            random_state=self.random_state,
            shuffle=self.shuffle,
            stratify=strat,
        )
