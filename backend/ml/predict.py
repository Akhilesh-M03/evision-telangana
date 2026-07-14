"""Prediction script entrypoint for EVision Telangana ML Infrastructure.

This script parses arguments, loads a persisted model wrapper, loads input features,
runs predictions, and writes output files.
"""

import argparse
import logging
import sys
from pathlib import Path

import pandas as pd

from ml.config import LoggingConfig
from ml.constants import LOGGER_NAME
from ml.inference.batch import BatchPredictor
from ml.inference.loader import ModelLoader
from ml.inference.predictor import Predictor
from ml.utils import setup_logging


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Run predictions using a trained EVision model.")
    parser.add_argument(
        "--model-path",
        type=str,
        required=True,
        help="Path to the persisted model checkpoint file",
    )
    parser.add_argument(
        "--input-path",
        type=str,
        required=True,
        help="Path to input features CSV file",
    )
    parser.add_argument(
        "--output-path",
        type=str,
        required=True,
        help="Path to write the CSV predictions output file",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=1000,
        help="Batch size for predictions",
    )
    return parser.parse_args()


def run_prediction(args: argparse.Namespace) -> int:
    """Execute prediction workflow.

    Returns:
        Exit code (0 for success, non-zero for failure).
    """
    logging_cfg = LoggingConfig()
    logger = setup_logging(logging_cfg)
    logger.info("Initializing EVision Telangana prediction pipeline...")

    # 1. Verify file paths
    model_path = Path(args.model_path)
    if not model_path.exists():
        logger.error(f"Persisted model file not found at {model_path}")
        return 1

    input_path = Path(args.input_path)
    if not input_path.exists():
        logger.error(f"Input features file not found at {input_path}")
        return 1

    # 2. Load persisted model wrapper
    try:
        logger.info(f"Loading model checkpoint from {model_path}...")
        model_wrapper = ModelLoader.load(model_path)
    except Exception as e:
        logger.error(f"Failed to load model from {model_path}: {e}")
        return 1

    # 3. Load input data
    try:
        logger.info(f"Reading input features from {input_path}...")
        df_inputs = pd.read_csv(input_path)
    except Exception as e:
        logger.error(f"Failed to read input features from {input_path}: {e}")
        return 1

    logger.info(f"Loaded {len(df_inputs)} samples for prediction.")

    # 4. Initialize Predictors
    predictor = Predictor(model_wrapper)
    batch_predictor = BatchPredictor(predictor, default_batch_size=args.batch_size)

    # 5. Run Batch Prediction
    logger.info("Executing batch predictions...")
    try:
        preds = batch_predictor.predict_batch(df_inputs)
    except Exception as e:
        logger.error(f"Prediction execution failed: {e}")
        return 1

    # 6. Save results
    output_path = Path(args.output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        # Create output DataFrame: preserve indices and combine
        df_outputs = df_inputs.copy()
        df_outputs["prediction"] = preds

        logger.info(f"Saving predictions to {output_path}...")
        df_outputs.to_csv(output_path, index=False)
    except Exception as e:
        logger.error(f"Failed to save predictions to {output_path}: {e}")
        return 1

    logger.info("Prediction pipeline complete.")
    return 0


if __name__ == "__main__":
    sys.exit(run_prediction(parse_args()))
