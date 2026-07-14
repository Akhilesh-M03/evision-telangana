"""Clustering utilities for EVision Telangana ML Infrastructure.

This module provides helper utilities to format cluster assignments, extract centroids,
and map clusters to descriptive DataFrames.
"""

from typing import Any, List, Union

import numpy as np
import pandas as pd


class ClusteringUtils:
    """Helper utilities for clustering data prep and mapping."""

    @staticmethod
    def extract_centroids(model: Any) -> np.ndarray:
        """Extract centroids coordinates from a fitted clustering model.

        Args:
            model: A fitted KMeans instance or KMeansClustering wrapper.

        Returns:
            Numpy array of centroid coordinates.
        """
        # Handle both raw scikit-learn and our wrapper
        if hasattr(model, "cluster_centers"):
            return model.cluster_centers
        elif hasattr(model, "_model") and hasattr(model._model, "cluster_centers_"):
            return model._model.cluster_centers_
        else:
            raise AttributeError("Provided model does not contain cluster centroids.")

    @staticmethod
    def assign_clusters_to_df(
        df: pd.DataFrame,
        labels: Union[np.ndarray, List[int]],
        col_name: str = "cluster"
    ) -> pd.DataFrame:
        """Append cluster assignments to a copy of the input DataFrame.

        Args:
            df: Input DataFrame.
            labels: Cluster label assignments.
            col_name: Name of the column to store labels.

        Returns:
            A new DataFrame containing the cluster labels.
        """
        df_copy = df.copy()
        df_copy[col_name] = np.asarray(labels)
        return df_copy

    @staticmethod
    def get_cluster_centroids_df(
        centroids: np.ndarray,
        feature_names: List[str]
    ) -> pd.DataFrame:
        """Format centroids coordinates array into a descriptive pandas DataFrame.

        Args:
            centroids: Coordinates of cluster centroids.
            feature_names: List of feature names matching coordinates dimensions.

        Returns:
            A DataFrame representing centroids.
        """
        df_centroids = pd.DataFrame(centroids, columns=feature_names)
        df_centroids.index.name = "cluster"
        return df_centroids
