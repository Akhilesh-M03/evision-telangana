"""Training script entrypoint for EVision Telangana ML Infrastructure.

This script parses arguments, initializes config, instantiates the chosen model,
runs the data split, trains the model, evaluates performance, and saves artifacts.
"""

import argparse
import logging
import sys
from pathlib import Path
from typing import Optional

import pandas as pd

from ml.config import DatasetConfig, LoggingConfig, MLConfig, ModelConfig, SystemConfig
from ml.constants import LOGGER_NAME, MODEL_TYPE_RANDOM_FOREST, MODEL_TYPE_XGBOOST
from ml.evaluation.reports import EvaluationReport
from ml.models.registry import ModelRegistry
from ml.training.split import DataSplitter
from ml.utils import get_model_path, setup_logging


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Train an EVision ML model wrapper.")
    parser.add_argument(
        "--model-type",
        type=str,
        default=MODEL_TYPE_RANDOM_FOREST,
        choices=[MODEL_TYPE_RANDOM_FOREST, MODEL_TYPE_XGBOOST],
        help="Type of model wrapper to train",
    )
    parser.add_argument(
        "--dataset-path",
        type=str,
        help="Path to the training CSV file",
    )
    parser.add_argument(
        "--target-col",
        type=str,
        default="target",
        help="Target label/value column name",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        help="Directory to save model checkpoint and evaluation reports",
    )
    parser.add_argument(
        "--model-version",
        type=str,
        default="1.0.0",
        help="Model semantic version",
    )
    parser.add_argument(
        "--task",
        type=str,
        default="regression",
        choices=["regression", "classification"],
        help="The machine learning task type",
    )
    parser.add_argument(
        "--config-path",
        type=str,
        help="Path to a JSON configuration file (overrides other command line params)",
    )
    return parser.parse_args()


def run_training(args: argparse.Namespace) -> int:
    """Execute training workflow.

    Returns:
        Exit code (0 for success, non-zero for failure).
    """
    # 1. Initialize configuration
    if args.config_path:
        config = MLConfig.load(Path(args.config_path))
    else:
        # Construct config from arguments
        dataset_cfg = DatasetConfig()
        if args.dataset_path:
            dataset_cfg.train_path = Path(args.dataset_path)

        model_cfg = ModelConfig(
            model_name=args.model_type.replace("_", " ").title(),
            model_version=args.model_version,
            hyperparameters={"task": args.task},
        )
        if args.output_dir:
            model_cfg.model_dir = Path(args.output_dir)

        logging_cfg = LoggingConfig()
        system_cfg = SystemConfig()
        if args.output_dir:
            system_cfg.output_dir = Path(args.output_dir)

        config = MLConfig(
            model=model_cfg,
            dataset=dataset_cfg,
            logging=logging_cfg,
            system=system_cfg,
        )

    # 2. Setup logging
    logger = setup_logging(config.logging)
    logger.info("Initializing EVision Telangana training pipeline...")
    logger.info(f"Configuration: {config.to_dict()}")

    # 3. Load dataset
    if not config.dataset.train_path or not config.dataset.train_path.exists():
        logger.error(f"Dataset path not found or invalid: {config.dataset.train_path}")
        return 1

    try:
        df = pd.read_csv(config.dataset.train_path)
    except Exception as e:
        logger.error(f"Failed to read dataset from {config.dataset.train_path}: {e}")
        return 1

    target_col = args.target_col
    if target_col not in df.columns:
        logger.error(f"Target column '{target_col}' not found in dataset. Columns: {list(df.columns)}")
        return 1

    X = df.drop(columns=[target_col])
    y = df[target_col]

    logger.info(f"Loaded dataset of shape: {df.shape}")

    # 4. Train/Test split
    splitter = DataSplitter(random_state=config.system.random_seed)
    X_train, X_test, y_train, y_test = splitter.split(X, y)
    logger.info(f"Split data into train size {X_train.shape} and test size {X_test.shape}")

    # 5. Instantiate model from registry
    try:
        model_class = ModelRegistry.get_model_class(config.model.model_name.replace(" ", "_").lower())
    except KeyError:
        # Fallback resolve using args.model_type key directly
        try:
            model_class = ModelRegistry.get_model_class(args.model_type)
        except KeyError as e:
            logger.error(f"Unregistered model type: {e}")
            return 1

    model_wrapper = model_class(
        model_name=config.model.model_name,
        version=config.model.model_version,
        hyperparameters=config.model.hyperparameters,
    )

    # 6. Fit model wrapper
    logger.info(f"Fitting model wrapper {model_wrapper.model_name}...")
    model_wrapper.fit(X_train, y_train)

    # 7. Evaluate performance
    logger.info("Generating predictions and computing performance evaluation metrics...")
    y_pred = model_wrapper.predict(X_test)
    y_prob = None
    if args.task == "classification":
        try:
            y_prob = model_wrapper.predict_proba(X_test)
        except (NotImplementedError, AttributeError):
            y_prob = None

    report = EvaluationReport.generate(
        model=model_wrapper,
        X=X_test,
        y=y_test,
        y_pred=y_pred,
        y_prob=y_prob,
        task=args.task,
    )

    # 8. Persist model and reports
    model_filepath = get_model_path(
        model_dir=config.model.model_dir,
        model_name=model_wrapper.model_name,
        model_version=model_wrapper.version,
    )
    logger.info(f"Persisting trained model wrapper checkpoint to {model_filepath}...")
    model_wrapper.save(model_filepath)

    eval_json_path = config.system.output_dir / "evaluation_report.json"
    eval_md_path = config.system.output_dir / "evaluation_report.md"
    logger.info(f"Saving evaluation reports to {config.system.output_dir}...")
    report.save_json(eval_json_path)
    report.save_markdown(eval_md_path)

    logger.info("Training pipeline complete.")
    return 0


if __name__ == "__main__":
    sys.exit(run_training(parse_args()))
