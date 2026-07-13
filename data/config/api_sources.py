"""Government API source configuration for EVision Telangana."""

from pathlib import Path

TGSPDCL_API_URL = (
    "https://data.telangana.gov.in/api/1/datastore/query/"
    "d9cbbc59-6099-516b-828c-c68881711f52"
    "?count=true&results=true&schema=true&keys=true&format=csv"
)

TGNPDCL_API_URL = (
    "https://data.telangana.gov.in/api/1/datastore/query/"
    "25398f55-f3e1-5126-aeb5-cf105e8ab54b"
    "?count=true&results=true&schema=true&keys=true&format=json&rowIds=true"
)

REQUEST_TIMEOUT_SECONDS = 60
RETRY_COUNT = 3
RETRY_DELAY_SECONDS = 1.5
PAGE_SIZE = 1000
MAX_PAGES = 500

RAW_CONSUMPTION_DIR = Path("data/raw/consumption")
TGSPDCL_OUTPUT_DIR = RAW_CONSUMPTION_DIR / "tgspdcl"
TGNPDCL_OUTPUT_DIR = RAW_CONSUMPTION_DIR / "tgnpdcl"
