"""
EVision Telangana – Feature Engineering Package (Epic 8).

This package transforms the master district-level dataset into rich feature sets
suitable for machine learning and analytics.  It is intentionally modular so that
future data sources (population, EV registrations, roads, economy, etc.) can be
added without touching existing modules.

Modules
-------
temporal_features       Quarter, season, time-index, and calendar flags.
infrastructure_features Density and per-station ratios.
utilization_features    Service efficiency ratios.
rolling_features        Lag and rolling-window statistics (no data leakage).
growth_features         Month-on-month growth and cumulative sums.
validation              Post-generation quality checks.
feature_dictionary      Structured metadata for every engineered feature.
feature_pipeline        Orchestration entry-point for the full pipeline.

Usage
-----
    python -m scripts.preprocessing.feature_engineering.feature_pipeline
    python scripts/preprocessing/feature_engineering/feature_pipeline.py
"""

from .feature_pipeline import run_pipeline

__all__ = ["run_pipeline"]
