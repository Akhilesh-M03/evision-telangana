"""Entry-point script to fetch latest Telangana government datasets."""

from __future__ import annotations

import logging
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from data.ingestion.government_api import GovernmentAPIClient

LOGGER = logging.getLogger(__name__)


def main() -> int:
    """Run TGSPDCL and TGNPDCL ingestion and return process exit code."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    client = GovernmentAPIClient()

    tgspdcl_result = client.fetch_tgspdcl()
    tgnpdcl_result = client.fetch_tgnpdcl()

    if tgspdcl_result.success and tgnpdcl_result.success:
        LOGGER.info("Government API ingestion completed successfully.")
        return 0

    if not tgspdcl_result.success:
        LOGGER.error("TGSPDCL ingestion failed: %s", tgspdcl_result.error_message)
    if not tgnpdcl_result.success:
        LOGGER.error("TGNPDCL ingestion failed: %s", tgnpdcl_result.error_message)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
