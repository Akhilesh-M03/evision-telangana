"""Cluster analysis utilities for EVision Telangana ML Infrastructure.

This module provides tools to analyze clusters, including silhouette score computation,
inertia calculations for elbow method, and cluster distribution stats.
"""

from typing import Dict, Optional, Union

import numpy as np
import pandas as pd
from sklearn.metrics import silhouette_score


class ClusterAnalyzer:
    """Helper class to evaluate and profile cluster outputs."""

    @staticmethod
    def compute_silhouette_score(
        X: Union[np.ndarray, pd.DataFrame],
        labels: Union[np.ndarray, pd.Series],
        sample_size: Optional[int] = None,
        random_state: int = 42,
    ) -> float:
        """Calculate the silhouette width score for clusters.

        Args:
            X: Input dataset features.
            labels: Cluster label assignments.
            sample_size: Subsample size to speed up calculation on large datasets.
            random_state: Random state for subsampling.

        Returns:
            The average silhouette coefficient.
        """
        # Silhouette requires at least 2 clusters and less than N clusters
        unique_labels = np.unique(labels)
        if len(unique_labels) < 2 or len(unique_labels) >= len(X):
            return 0.0

        return float(
            silhouette_score(
                X,
                labels,
                sample_size=sample_size,
                random_state=random_state,
            )
        )

    @staticmethod
    def find_elbow_point(
        X: Union[np.ndarray, pd.DataFrame],
        max_k: int = 10,
        random_state: int = 42,
    ) -> Dict[int, float]:
        """Compute inertia for a range of cluster sizes (2 to max_k) to assist in the elbow method.

        Args:
            X: Input dataset features.
            max_k: Maximum number of clusters to test.
            random_state: Random seed for KMeans.

        Returns:
            A dictionary mapping k to inertia value.
        """
        from sklearn.cluster import KMeans

        inertias: Dict[int, float] = {}
        limit_k = min(max_k, len(X))

        for k in range(1, limit_k + 1):
            km = KMeans(n_clusters=k, random_state=random_state, n_init="auto")
            km.fit(X)
            inertias[k] = float(km.inertia_)

        return inertias

    @staticmethod
    def compute_cluster_stats(
        X: Union[np.ndarray, pd.DataFrame],
        labels: Union[np.ndarray, pd.Series]
    ) -> pd.DataFrame:
        """Generate statistical profiles (means, counts, ratios) for each cluster.

        Args:
            X: Features dataset.
            labels: Cluster label assignments.

        Returns:
            A pandas DataFrame compiling descriptive statistics per cluster.
        """
        df_feats = pd.DataFrame(X)
        df_feats["cluster"] = np.asarray(labels)

        # Basic counts and ratios
        group = df_feats.groupby("cluster")
        counts = group.size().to_frame(name="count")
        counts["ratio"] = counts["count"] / len(df_feats)

        # Means per feature
        means = group.mean()

        # Join stats
        stats = counts.join(means)
        return stats
