"""Unit tests for the Machine Learning Infrastructure package.

This file tests all packages inside backend/ml:
- config and constants
- utils
- models base and registry
- training split, persistence, and estimators (Random Forest, XGBoost)
- evaluation metrics, reports, and cross-validation
- inference loader, predictor, pipeline, and batch predictions
- clustering kmeans, analysis, and utilities
"""

import sys
from pathlib import Path
import tempfile
import pytest
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator

# Ensure backend directory is in python path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))

from ml import (
    DatasetConfig,
    LoggingConfig,
    MLConfig,
    ModelConfig,
    SystemConfig,
    DEFAULT_RANDOM_SEED,
    MODEL_TYPE_RANDOM_FOREST,
    MODEL_TYPE_XGBOOST,
    MODEL_TYPE_KMEANS,
)
from ml.models.registry import ModelRegistry
from ml.training.split import DataSplitter
from ml.training.persistence import ModelPersistence
from ml.training.random_forest import RandomForestModel
from ml.training.xgboost import XGBoostModel
from ml.evaluation.metrics import MetricEvaluator
from ml.evaluation.reports import EvaluationReport
from ml.evaluation.cross_validation import CrossValidator
from ml.inference.loader import ModelLoader
from ml.inference.predictor import Predictor
from ml.inference.pipeline import InferencePipeline
from ml.inference.batch import BatchPredictor
from ml.clustering.kmeans import KMeansClustering
from ml.clustering.analysis import ClusterAnalyzer
from ml.clustering.utils import ClusteringUtils
from ml.utils import get_model_path, set_seed


@pytest.fixture
def regression_data():
    """Generate simple synthetic regression dataset."""
    np.random.seed(42)
    X = pd.DataFrame(np.random.randn(100, 4), columns=["f1", "f2", "f3", "f4"])
    y = pd.Series(X["f1"] * 2 + X["f2"] * 0.5 + np.random.randn(100) * 0.1, name="target")
    return X, y


@pytest.fixture
def classification_data():
    """Generate simple synthetic classification dataset."""
    np.random.seed(42)
    X = pd.DataFrame(np.random.randn(100, 4), columns=["f1", "f2", "f3", "f4"])
    y = pd.Series((X["f1"] + X["f2"] > 0).astype(int), name="target")
    return X, y


def test_constants_and_config():
    """Test package config creation, serialization, and deserialization."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        cfg_file = tmp_path / "config.json"

        model_cfg = ModelConfig(
            model_name="Random Forest",
            model_version="1.2.3",
            model_dir=tmp_path,
            hyperparameters={"n_estimators": 50, "task": "regression"},
        )
        dataset_cfg = DatasetConfig(
            data_dir=tmp_path,
            raw_dir=tmp_path / "raw",
            processed_dir=tmp_path / "processed",
            train_path=tmp_path / "train.csv",
        )
        logging_cfg = LoggingConfig(level="DEBUG", log_file=tmp_path / "ml.log")
        system_cfg = SystemConfig(random_seed=123, output_dir=tmp_path / "eval")

        ml_config = MLConfig(
            model=model_cfg,
            dataset=dataset_cfg,
            logging=logging_cfg,
            system=system_cfg,
        )

        # Check serialization
        cfg_dict = ml_config.to_dict()
        assert cfg_dict["model"]["model_version"] == "1.2.3"
        assert cfg_dict["system"]["random_seed"] == 123
        assert isinstance(cfg_dict["model"]["model_dir"], str)

        # Save config
        ml_config.save(cfg_file)
        assert cfg_file.exists()

        # Load config
        loaded_cfg = MLConfig.load(cfg_file)
        assert loaded_cfg.model.model_version == "1.2.3"
        assert loaded_cfg.system.random_seed == 123
        assert isinstance(loaded_cfg.model.model_dir, Path)
        assert loaded_cfg.dataset.train_path == tmp_path / "train.csv"


def test_splitter(regression_data):
    """Test train/test splitter functionality."""
    X, y = regression_data
    splitter = DataSplitter(test_size=0.3, random_state=42)
    X_train, X_test, y_train, y_test = splitter.split(X, y)

    assert len(X_train) == 70
    assert len(X_test) == 30
    assert len(y_train) == 70
    assert len(y_test) == 30
    assert isinstance(X_train, pd.DataFrame)
    assert isinstance(y_train, pd.Series)


class DummyEstimator:
    def __init__(self):
        self.value = 42


def test_persistence():
    """Test model and metadata saving and loading using a dummy estimator."""
    dummy = DummyEstimator()
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = Path(tmpdir) / "dummy_model.joblib"
        metadata = {"name": "dummy", "package_version": "0.1.0"}

        # Save
        ModelPersistence.save_model(dummy, filepath, metadata)
        assert filepath.exists()

        # Load
        loaded_model, loaded_meta = ModelPersistence.load_model(filepath)
        assert loaded_model.value == 42
        assert loaded_meta["name"] == "dummy"
        assert loaded_meta["package_version"] == "0.1.0"


def test_random_forest_regression(regression_data):
    """Test Random Forest Regressor wrapper fitting, predicting, and persistence."""
    X, y = regression_data
    rf = RandomForestModel(
        model_name="RF Regressor",
        version="1.0.0",
        hyperparameters={"task": "regression", "n_estimators": 10, "max_depth": 3},
    )

    assert not rf.is_fitted
    rf.fit(X, y)
    assert rf.is_fitted

    preds = rf.predict(X)
    assert len(preds) == 100
    assert isinstance(preds, np.ndarray)

    with pytest.raises(NotImplementedError):
        rf.predict_proba(X)

    # Test saving and loading via ModelLoader
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = Path(tmpdir) / "rf_model.joblib"
        rf.save(filepath)

        # Clear cache first to force reload from disk
        ModelLoader.clear_cache()
        rf_loaded = ModelLoader.load(filepath, use_cache=True)
        assert rf_loaded.is_fitted
        assert rf_loaded.model_type == MODEL_TYPE_RANDOM_FOREST
        assert rf_loaded.hyperparameters["n_estimators"] == 10

        loaded_preds = rf_loaded.predict(X)
        np.testing.assert_array_almost_equal(preds, loaded_preds)

        # Check caching
        rf_cached = ModelLoader.load(filepath, use_cache=True)
        assert rf_cached is rf_loaded


def test_random_forest_classification(classification_data):
    """Test Random Forest Classifier wrapper fitting, predicting, and predict_proba."""
    X, y = classification_data
    rf = RandomForestModel(
        model_name="RF Classifier",
        version="2.0.0",
        hyperparameters={"task": "classification", "n_estimators": 10, "max_depth": 3},
    )

    rf.fit(X, y)
    preds = rf.predict(X)
    probs = rf.predict_proba(X)

    assert len(preds) == 100
    assert probs.shape == (100, 2)


def test_xgboost_regression(regression_data):
    """Test XGBoost Regressor wrapper fitting and predicting."""
    X, y = regression_data
    xgb = XGBoostModel(
        model_name="XGB Regressor",
        version="1.0.0",
        hyperparameters={"task": "regression", "n_estimators": 5, "max_depth": 2},
    )

    xgb.fit(X, y)
    assert xgb.is_fitted
    preds = xgb.predict(X)
    assert len(preds) == 100


def test_xgboost_classification(classification_data):
    """Test XGBoost Classifier wrapper fitting and predict_proba."""
    X, y = classification_data
    xgb = XGBoostModel(
        model_name="XGB Classifier",
        version="1.0.0",
        hyperparameters={"task": "classification", "n_estimators": 5, "max_depth": 2},
    )

    xgb.fit(X, y)
    preds = xgb.predict(X)
    probs = xgb.predict_proba(X)

    assert len(preds) == 100
    assert probs.shape == (100, 2)


def test_metrics_evaluator():
    """Test regression and classification metric calculations."""
    y_true_reg = np.array([1.0, 2.0, 3.0])
    y_pred_reg = np.array([1.1, 1.9, 3.2])

    reg_metrics = MetricEvaluator.compute_regression_metrics(y_true_reg, y_pred_reg)
    assert "mean_squared_error" in reg_metrics
    assert "r2_score" in reg_metrics
    assert reg_metrics["mean_squared_error"] > 0.0

    y_true_clf = np.array([0, 1, 0, 1])
    y_pred_clf = np.array([0, 0, 0, 1])
    y_prob_clf = np.array([[0.9, 0.1], [0.8, 0.2], [0.7, 0.3], [0.1, 0.9]])

    clf_metrics = MetricEvaluator.compute_classification_metrics(y_true_clf, y_pred_clf, y_prob_clf)
    assert "accuracy" in clf_metrics
    assert "f1_score" in clf_metrics
    assert "roc_auc" in clf_metrics
    assert clf_metrics["accuracy"] == 0.75


def test_evaluation_reports(regression_data):
    """Test generation of evaluation reports in JSON and Markdown formats."""
    X, y = regression_data
    rf = RandomForestModel(
        model_name="RF Eval Report",
        hyperparameters={"task": "regression", "n_estimators": 5},
    )
    rf.fit(X, y)
    y_pred = rf.predict(X)

    report = EvaluationReport.generate(rf, X, y, y_pred, task="regression")
    assert report.model_metadata["model_name"] == "RF Eval Report"
    assert report.dataset_metadata["sample_count"] == 100

    report_dict = report.to_dict()
    assert "metrics" in report_dict
    assert "mean_squared_error" in report_dict["metrics"]

    md_str = report.to_markdown()
    assert "Model Evaluation Report" in md_str
    assert "Performance Metrics" in md_str

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        json_path = tmp_path / "report.json"
        md_path = tmp_path / "report.md"

        report.save_json(json_path)
        report.save_markdown(md_path)

        assert json_path.exists()
        assert md_path.exists()


def test_cross_validation(regression_data):
    """Test cross-validation runner executing on model wrappers."""
    X, y = regression_data
    validator = CrossValidator(n_splits=3, shuffle=True, random_state=42)

    cv_results = validator.validate(
        model_class=RandomForestModel,
        X=X,
        y=y,
        hyperparameters={"task": "regression", "n_estimators": 5, "max_depth": 2},
        task="regression",
    )

    assert "folds" in cv_results
    assert len(cv_results["folds"]) == 3
    assert "mean" in cv_results
    assert "std" in cv_results
    assert "mean_squared_error" in cv_results["mean"]


def test_predictor_and_batch_predictor(regression_data):
    """Test predictor interfaces including lists, dicts, and batched dataframes."""
    X, y = regression_data
    rf = RandomForestModel(
        model_name="RF Predict",
        hyperparameters={"task": "regression", "n_estimators": 5},
    )
    rf.fit(X, y)

    # 1. Standard Predictor
    predictor = Predictor(rf)

    # Test DataFrame input
    preds_df = predictor.predict(X)
    assert len(preds_df) == 100

    # Test single dict input
    dict_input = {"f1": 0.5, "f2": -0.2, "f3": 0.1, "f4": 0.0}
    preds_dict = predictor.predict(dict_input)
    assert len(preds_dict) == 1

    # Test list of dicts input
    list_input = [dict_input, dict_input]
    preds_list = predictor.predict(list_input)
    assert len(preds_list) == 2

    # 2. Batch Predictor
    batch_predictor = BatchPredictor(predictor, default_batch_size=30)
    batch_preds = batch_predictor.predict_batch(X)
    assert len(batch_preds) == 100
    assert isinstance(batch_preds, pd.Series)
    assert batch_preds.name == "prediction"
    pd.testing.assert_index_equal(batch_preds.index, X.index)

    # Test stream predictions generator
    stream_generator = batch_predictor.predict_stream(X.to_dict(orient="records"), batch_size=40)
    chunks = list(stream_generator)
    assert len(chunks) == 3  # 40, 40, 20
    assert len(chunks[0]) == 40
    assert len(chunks[2]) == 20


def test_inference_pipeline(regression_data):
    """Test InferencePipeline with pre- and post-processors."""
    X, y = regression_data
    rf = RandomForestModel(
        model_name="RF Pipeline",
        hyperparameters={"task": "regression", "n_estimators": 5},
    )
    rf.fit(X, y)
    predictor = Predictor(rf)

    # Mock preprocessor adding a offset, postprocessor multiplying predictions
    pre_fn = lambda data: data + 1.0
    post_fn = lambda preds: preds * 2.0

    pipeline = InferencePipeline(
        predictor=predictor,
        preprocessor=pre_fn,
        postprocessor=post_fn,
    )

    outputs = pipeline.run(X)
    assert len(outputs) == 100

    # Verification
    raw_preds = predictor.predict(X + 1.0)
    np.testing.assert_array_almost_equal(outputs, raw_preds * 2.0)


def test_clustering_and_analysis(regression_data):
    """Test KMeans wrapper, silhouette score finder, and elbow calculator."""
    X, _ = regression_data

    # Wrap KMeans
    km = KMeansClustering(
        model_name="KMeans Wrapper",
        hyperparameters={"n_clusters": 3, "random_state": 42},
    )

    assert not km.is_fitted
    km.fit(X)
    assert km.is_fitted

    labels = km.predict(X)
    assert len(labels) == 100
    assert len(np.unique(labels)) <= 3

    assert km.cluster_centers.shape == (3, 4)
    assert km.inertia > 0.0

    with pytest.raises(NotImplementedError):
        km.predict_proba(X)

    # Cluster Analyzer tests
    sil = ClusterAnalyzer.compute_silhouette_score(X, labels)
    assert -1.0 <= sil <= 1.0

    elbow = ClusterAnalyzer.find_elbow_point(X, max_k=4)
    assert len(elbow) == 4
    assert 1 in elbow
    assert 4 in elbow

    stats = ClusterAnalyzer.compute_cluster_stats(X, labels)
    assert isinstance(stats, pd.DataFrame)
    assert "count" in stats.columns
    assert "ratio" in stats.columns
    assert len(stats) <= 3

    # Clustering utilities
    centroids = ClusteringUtils.extract_centroids(km)
    np.testing.assert_array_equal(centroids, km.cluster_centers)

    df_centroids = ClusteringUtils.get_cluster_centroids_df(centroids, ["f1", "f2", "f3", "f4"])
    assert df_centroids.shape == (3, 4)

    df_clustered = ClusteringUtils.assign_clusters_to_df(X, labels, "assignment")
    assert "assignment" in df_clustered.columns
    np.testing.assert_array_equal(df_clustered["assignment"], labels)
