# Machine Learning Infrastructure Architecture Review

**Project:** EVision Telangana  
**Epic:** Machine Learning Infrastructure  
**Author:** AI Coding Assistant  
**Date:** July 2026  

---

## 1. Compliance with Machine Learning Design Document

The implemented `ml/` package matches the approved Machine Learning Design specifications. Below is the mapping and status of every implemented component:

| Component Path | Class / Function / Script | Purpose | Category / Status |
| :--- | :--- | :--- | :--- |
| `backend/ml/constants.py` | Package Constants | Holds global seeds, path locations, and metrics identifiers. | **Required** |
| `backend/ml/config.py` | `DatasetConfig`, `ModelConfig`, `LoggingConfig`, `SystemConfig`, `MLConfig` | Standardizes configuration parsing, versioning, serialization. | **Required** |
| `backend/ml/utils.py` | `setup_logging`, `set_seed`, `ensure_dir`, `get_model_path` | Manages random seed initialization, directory creation, and logger configuration. | **Required** |
| `backend/ml/models/base.py` | `BaseModel` (Abstract Base Class) | Enforces unified interface (`fit`, `predict`, `predict_proba`, `save`, `load`) for all estimators. | **Required** |
| `backend/ml/models/registry.py` | `ModelRegistry` | Decentralized registration mapping model keys to wrapper classes. | **Required** |
| `backend/ml/training/split.py` | `DataSplitter` | Implements train/test data splitting (e.g. 80/20 train/test split). | **Required** |
| `backend/ml/training/persistence.py`| `ModelPersistence` | Serializes and loads models and metadata package versions using `joblib`. | **Required** |
| `backend/ml/training/random_forest.py`| `RandomForestModel` | Wraps scikit-learn's Random Forest for regression. | **Required** |
| `backend/ml/training/random_forest.py`| `RandomForestModel` (Classifier mode) | Wraps scikit-learn's Random Forest for classification. | **Future-proofing** |
| `backend/ml/training/xgboost.py` | `XGBoostModel` | Wraps xgboost's `XGBRegressor`. | **Required** |
| `backend/ml/training/xgboost.py` | `XGBoostModel` (Classifier mode) | Wraps xgboost's `XGBClassifier`. | **Future-proofing** |
| `backend/ml/evaluation/metrics.py` | `MetricEvaluator` (Regression) | Calculates MSE, RMSE, MAE, R² score. | **Required** |
| `backend/ml/evaluation/metrics.py` | `MetricEvaluator` (Classification) | Calculates Accuracy, Precision, Recall, F1, ROC-AUC, and Confusion Matrix. | **Future-proofing** |
| `backend/ml/evaluation/reports.py` | `EvaluationReport` | Compiles performance metadata into JSON and Markdown reports. | **Required** |
| `backend/ml/evaluation/cross_validation.py`| `CrossValidator` | Implements K-Fold and Stratified K-Fold. | **Optional / Future-proofing** |
| `backend/ml/inference/loader.py` | `ModelLoader` | Handles deserialization, registry mapping, and caching of loaded models. | **Required** |
| `backend/ml/inference/predictor.py` | `Predictor` | Handles format validation and single-predict commands. | **Required** |
| `backend/ml/inference/pipeline.py` | `InferencePipeline` | Chains preprocessors, predictors, and postprocessors. | **Required** |
| `backend/ml/inference/batch.py` | `BatchPredictor` | Implements chunked batch and stream prediction interfaces, preserving indices. | **Required** |
| `backend/ml/clustering/kmeans.py` | `KMeansClustering` | Wraps scikit-learn's `KMeans` clustering. | **Required** |
| `backend/ml/clustering/analysis.py` | `ClusterAnalyzer` | Computes silhouette coefficients, elbow-method inertias, and cluster means. | **Required** |
| `backend/ml/clustering/utils.py` | `ClusteringUtils` | Centroid extraction and cluster assignments formatting. | **Required** |
| `backend/ml/train.py` | CLI Script | Command-line entrypoint to train, evaluate, and save models. | **Required** |
| `backend/ml/predict.py` | CLI Script | Command-line entrypoint to load model checkpoints and write predictions. | **Required** |

---

## 2. Rationale for Classification Wrappers

- **Why Implemented:** The classification wrappers (e.g. `XGBClassifier` and `RandomForestClassifier` modes, and classification metrics under `MetricEvaluator`) were implemented to ensure the ML package infrastructure is general-purpose. This covers potential requirements in the epic, such as predicting suitability class labels, charging priority categories, or recommendations.
- **Are they required for this project?** No. The core machine learning objective for EVision Telangana is to predict `predicted_demand` (a continuous regression target representing estimated future EV charging demand per district). The classification tasks (such as `Priority Level` or suitability `Recommendation`) are explicitly defined as rule-based operations inside the **Decision Engine** (combining predicted demand, registrations, and area), rather than direct ML classification models.
- **Should they remain?** Yes. They occupy minimal, clean code paths, are fully tested, and future-proof the package. If the project team decides to transition rule-based priority levels into direct machine learning classifiers in subsequent phases, the infrastructure is already set up and validated.

---

## 3. Inference Pipeline Analysis & Boundary of Feature Engineering

- **No Preprocessing Duplication:** The `InferencePipeline` class acts as a clean orchestrator. It does not contain hardcoded preprocessing rules or feature engineering steps (like calculating rolling averages or computing densities). Instead, it accepts optional preprocessing functions/callables as arguments, ensuring zero duplication of code.
- **Boundary of Feature Engineering vs. Inference:**
  - **Feature Engineering Ends:** When raw data is cleaned, imputed, and transformed (e.g., mapping spatial coordinates, computing density ratios, and calculating rolling averages) to construct a structured dataset with feature columns matching the model's schema.
  - **Inference Begins:** When the feature dataframe or record list (containing already-calculated numeric features) is passed to the prediction pipeline. The `ModelLoader` retrieves the model, the `Predictor` validates the dimensions, and the estimator performs the forward pass (`predict`) to output the `predicted_demand`.

---

## 4. KMeans Dynamic Cluster Configuration

- **Centroid Configuration:** The implementation of `KMeansClustering` in `backend/ml/clustering/kmeans.py` does not hardcode the number of clusters ($K$).
- **Support for Dynamic Selection:**
  - The wrapper extracts `n_clusters` from the configuration `hyperparameters` dictionary during instantiation (defaulting to `5` if none is supplied):
    ```python
    self.kmeans_params.setdefault("n_clusters", 5)
    self.kmeans_params.setdefault("random_state", 42)
    self._model = KMeans(**self.kmeans_params)
    ```
  - The `ClusterAnalyzer` helper in `backend/ml/clustering/analysis.py` provides the `find_elbow_point(X, max_k)` method, which dynamically trains KMeans models from $K=1$ to `max_k` and returns the inertia map. This allows developers or the Decision Engine to run grid analyses to choose the optimal cluster size dynamically.

---

## 5. Independence of train.py from Synthetic Data

- **CSV Path Resolution:** The script `backend/ml/train.py` does not depend on synthetic data.
- **Configurable Dataset Loading:**
  - It parses the dataset filepath via the `--dataset-path` CLI argument:
    ```python
    parser.add_argument("--dataset-path", type=str, help="Path to the training CSV file")
    ```
  - It loads the target column via the `--target-col` CLI argument:
    ```python
    parser.add_argument("--target-col", type=str, default="target", help="Target label/value column name")
    ```
  - Once Worker 7 generates `data/processed/ml_training_dataset.csv`, `train.py` can be executed directly as follows:
    ```bash
    uv run python -m ml.train --dataset-path ../data/processed/ml_training_dataset.csv --target-col predicted_demand
    ```

---

## 6. Documented Assumptions

The following assumptions were made during development that are not explicitly defined in the project sources:
1. **Feature Integrity:** Assumed the processed training dataset will be passed as a clean CSV with a header row, and all categorical values will have been encoded beforehand.
2. **Missing Values:** Assumed that the input dataset has already been cleaned and imputed by the feature engineering pipeline, so no imputation is performed before splitting.
3. **RAM Scale:** Assumed the entire dataset (Telangana districts-level features, consisting of 33 records) fits entirely in memory during training and prediction.
4. **Target Names:** Assumed target columns are custom-defined via CLI arguments, enabling support for multiple variables.
