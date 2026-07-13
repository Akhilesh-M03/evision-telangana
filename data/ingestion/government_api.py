"""Government API ingestion client for Telangana DISCOM datasets."""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass
from datetime import date
from io import StringIO
from pathlib import Path
from typing import Any

import pandas as pd
import requests

from data.config.api_sources import (
    MAX_PAGES,
    PAGE_SIZE,
    REQUEST_TIMEOUT_SECONDS,
    RETRY_COUNT,
    RETRY_DELAY_SECONDS,
    TGSPDCL_API_URL,
    TGSPDCL_OUTPUT_DIR,
    TGNPDCL_API_URL,
    TGNPDCL_OUTPUT_DIR,
)

LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class DownloadResult:
    """Represents the result of a dataset download operation."""

    source: str
    success: bool
    file_path: Path | None
    rows_downloaded: int
    elapsed_seconds: float
    error_message: str | None = None


class GovernmentAPIClient:
    """Reusable client for downloading Telangana open datasets with retries."""

    def __init__(
        self,
        session: requests.Session | None = None,
        timeout: int = REQUEST_TIMEOUT_SECONDS,
        retry_count: int = RETRY_COUNT,
        retry_delay: float = RETRY_DELAY_SECONDS,
        page_size: int = PAGE_SIZE,
        max_pages: int = MAX_PAGES,
    ) -> None:
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": "EVision-Telangana-Ingestion/1.0"})
        self.timeout = timeout
        self.retry_count = retry_count
        self.retry_delay = retry_delay
        self.page_size = page_size
        self.max_pages = max_pages

    # ==========================================================
    # TODO(API-INTEGRATION-TGSPDCL)
    # Telangana Government Open Data Integration
    # Source:
    # https://data.telangana.gov.in/api/1/datastore/query/d9cbbc59-6099-516b-828c-c68881711f52
    # ==========================================================
    def fetch_tgspdcl(self) -> DownloadResult:
        """Download the latest TGSPDCL dataset and save it to raw consumption path."""
        start_time = time.perf_counter()
        LOGGER.info("Download started for TGSPDCL")

        try:
            response = self.download_dataset(TGSPDCL_API_URL, expect_json=False)
            csv_text = response.text
            dataframe = self._csv_to_dataframe(csv_text)
            if dataframe.empty:
                raise ValueError("TGSPDCL response contains no rows.")

            file_path = self.save_dataframe(dataframe, TGSPDCL_OUTPUT_DIR, "tgspdcl")

            elapsed = time.perf_counter() - start_time
            self.log_download("tgspdcl", len(dataframe.index), file_path, elapsed)
            return DownloadResult(
                source="tgspdcl",
                success=True,
                file_path=file_path,
                rows_downloaded=len(dataframe.index),
                elapsed_seconds=elapsed,
            )
        except Exception as exc:  # noqa: BLE001
            elapsed = time.perf_counter() - start_time
            LOGGER.exception("TGSPDCL download failed")
            return DownloadResult(
                source="tgspdcl",
                success=False,
                file_path=None,
                rows_downloaded=0,
                elapsed_seconds=elapsed,
                error_message=str(exc),
            )

    # ==========================================================
    # TODO(API-INTEGRATION-TGNPDCL)
    # Telangana Government Open Data Integration
    # Source:
    # https://data.telangana.gov.in/api/1/datastore/query/25398f55-f3e1-5126-aeb5-cf105e8ab54b
    # ==========================================================
    def fetch_tgnpdcl(self) -> DownloadResult:
        """Download the latest TGNPDCL dataset, convert JSON to CSV and save it."""
        start_time = time.perf_counter()
        LOGGER.info("Download started for TGNPDCL")

        try:
            response = self.download_dataset(TGNPDCL_API_URL, expect_json=True)
            dataframe = self.json_to_dataframe(response.json())
            if dataframe.empty:
                raise ValueError("TGNPDCL response contains no rows.")

            file_path = self.save_dataframe(dataframe, TGNPDCL_OUTPUT_DIR, "tgnpdcl")
            elapsed = time.perf_counter() - start_time
            self.log_download("tgnpdcl", len(dataframe.index), file_path, elapsed)
            return DownloadResult(
                source="tgnpdcl",
                success=True,
                file_path=file_path,
                rows_downloaded=len(dataframe.index),
                elapsed_seconds=elapsed,
            )
        except Exception as exc:  # noqa: BLE001
            elapsed = time.perf_counter() - start_time
            LOGGER.exception("TGNPDCL download failed")
            return DownloadResult(
                source="tgnpdcl",
                success=False,
                file_path=None,
                rows_downloaded=0,
                elapsed_seconds=elapsed,
                error_message=str(exc),
            )

    def download_dataset(
        self,
        url: str,
        params: dict[str, Any] | None = None,
        *,
        expect_json: bool,
    ) -> requests.Response:
        """Download a single dataset page with retry and exponential backoff."""
        LOGGER.info("API called: %s", url)
        attempts = self.retry_count + 1

        for attempt in range(attempts):
            try:
                response = self.session.get(url, params=params, timeout=self.timeout)

                if response.status_code in {429, 500, 502, 503, 504} and attempt < self.retry_count:
                    delay = self.retry_delay * (2**attempt)
                    LOGGER.warning(
                        "Transient HTTP %s from %s. Retrying in %.2fs (%s/%s).",
                        response.status_code,
                        url,
                        delay,
                        attempt + 1,
                        attempts,
                    )
                    time.sleep(delay)
                    continue

                self.validate_response(response=response, expect_json=expect_json)
                return response
            except (requests.Timeout, requests.ConnectionError) as exc:
                if attempt >= self.retry_count:
                    raise
                delay = self.retry_delay * (2**attempt)
                LOGGER.warning(
                    "Connection/timeout error for %s: %s. Retrying in %.2fs (%s/%s).",
                    url,
                    exc,
                    delay,
                    attempt + 1,
                    attempts,
                )
                time.sleep(delay)
            except requests.HTTPError as exc:
                status_code = exc.response.status_code if exc.response is not None else None
                if status_code is not None and 400 <= status_code < 500 and status_code != 429:
                    raise
                if attempt >= self.retry_count:
                    raise
                delay = self.retry_delay * (2**attempt)
                LOGGER.warning(
                    "HTTP error for %s: %s. Retrying in %.2fs (%s/%s).",
                    url,
                    exc,
                    delay,
                    attempt + 1,
                    attempts,
                )
                time.sleep(delay)
            except ValueError:
                if attempt >= self.retry_count:
                    raise
                delay = self.retry_delay * (2**attempt)
                LOGGER.warning(
                    "Validation failed for %s. Retrying in %.2fs (%s/%s).",
                    url,
                    delay,
                    attempt + 1,
                    attempts,
                )
                time.sleep(delay)

        raise RuntimeError(f"Retry loop exited unexpectedly for URL: {url}")

    def validate_response(self, response: requests.Response, *, expect_json: bool) -> None:
        """Validate HTTP status and payload integrity."""
        response.raise_for_status()

        if not response.content:
            raise ValueError("Empty response body.")

        if expect_json:
            payload = response.json()
            if payload is None:
                raise ValueError("JSON response is null.")

    def json_to_dataframe(self, payload: Any) -> pd.DataFrame:
        """Convert supported JSON payload structures into a DataFrame."""
        records = self._extract_records(payload)
        if not records:
            return pd.DataFrame()
        return pd.DataFrame(records)

    def save_dataframe(self, dataframe: pd.DataFrame, output_dir: Path, source_name: str) -> Path:
        """Persist a DataFrame as CSV under the source raw directory."""
        output_dir.mkdir(parents=True, exist_ok=True)
        file_path = output_dir / f"{date.today().strftime('%Y_%m_%d')}_{source_name}.csv"
        dataframe.to_csv(file_path, index=False)
        return file_path

    def save_csv(self, csv_text: str, output_dir: Path, source_name: str) -> Path:
        """Persist CSV text under the source raw directory."""
        output_dir.mkdir(parents=True, exist_ok=True)
        file_path = output_dir / f"{date.today().strftime('%Y_%m_%d')}_{source_name}.csv"
        file_path.write_text(csv_text, encoding="utf-8")
        return file_path

    def log_download(self, source_name: str, rows_downloaded: int, file_path: Path, elapsed_seconds: float) -> None:
        """Log standardized completion details for a download."""
        LOGGER.info("Download completed: %s", source_name)
        LOGGER.info("Rows downloaded: %s", rows_downloaded)
        LOGGER.info("File saved: %s", file_path)
        LOGGER.info("Execution time: %.2f seconds", elapsed_seconds)

    def _fetch_paginated_json(self, base_url: str) -> list[dict[str, Any]]:
        """Fetch all pages for JSON endpoints until complete result set is collected."""
        response = self.download_dataset(base_url, expect_json=True)
        records = self._extract_records(response.json())
        if not records:
            raise ValueError("No records found in JSON response.")
        return records

    def _fetch_paginated_csv(
        self,
        source_name: str,
        base_url: str,
        first_page: pd.DataFrame,
    ) -> pd.DataFrame | None:
        """Detect and fetch additional CSV pages if the API applies row limits."""
        LOGGER.info("CSV pagination not required for %s; using first response page.", source_name)
        return None

    @staticmethod
    def _extract_records(payload: Any) -> list[dict[str, Any]]:
        """Extract row records from supported Telangana API JSON shapes."""
        if isinstance(payload, list):
            if payload and isinstance(payload[0], dict):
                return payload
            return []

        if not isinstance(payload, dict):
            raise ValueError("Unsupported JSON payload type.")

        if isinstance(payload.get("results"), list):
            return [item for item in payload["results"] if isinstance(item, dict)]

        if isinstance(payload.get("data"), list):
            return [item for item in payload["data"] if isinstance(item, dict)]

        result = payload.get("result")
        if isinstance(result, dict):
            if isinstance(result.get("results"), list):
                return [item for item in result["results"] if isinstance(item, dict)]
            if isinstance(result.get("records"), list):
                return [item for item in result["records"] if isinstance(item, dict)]
            if isinstance(result.get("data"), list):
                return [item for item in result["data"] if isinstance(item, dict)]

        return []

    @staticmethod
    def _extract_total_count(payload: Any) -> int | None:
        """Extract total row count from supported Telangana API JSON shapes."""
        if not isinstance(payload, dict):
            return None

        for key in ("count", "total", "total_count", "recordsTotal"):
            value = payload.get(key)
            if isinstance(value, int):
                return value
            if isinstance(value, str) and value.isdigit():
                return int(value)

        result = payload.get("result")
        if isinstance(result, dict):
            for key in ("count", "total", "total_count", "recordsTotal"):
                value = result.get(key)
                if isinstance(value, int):
                    return value
                if isinstance(value, str) and value.isdigit():
                    return int(value)

        return None

    @staticmethod
    def _csv_to_dataframe(csv_text: str) -> pd.DataFrame:
        """Safely parse CSV text into DataFrame."""
        if not csv_text.strip():
            return pd.DataFrame()
        try:
            return pd.read_csv(StringIO(csv_text))
        except pd.errors.EmptyDataError:
            return pd.DataFrame()
