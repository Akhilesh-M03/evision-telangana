import logging
from pathlib import Path

from sqlmodel import SQLModel

from core.settings import settings
from database.base import *  # Ensure all models are registered on metadata
from database.engine import engine

logger = logging.getLogger(__name__)


def ensure_database_directory() -> None:
    """Ensure that the parent directory for the SQLite database file exists."""
    db_url = settings.database_url
    if db_url.startswith("sqlite:") and ":memory:" not in db_url:
        # Extract path. Handle both sqlite:///path and sqlite://path
        if db_url.startswith("sqlite:///"):
            db_path_str = db_url[10:]  # strip 'sqlite:///'
        else:
            db_path_str = db_url[9:]  # strip 'sqlite://'
        
        # In case query parameters are appended, strip them
        if "?" in db_path_str:
            db_path_str = db_path_str.split("?")[0]
            
        db_path = Path(db_path_str)
        if db_path.parent and not db_path.parent.exists():
            logger.info(f"Creating database directory: {db_path.parent}")
            db_path.parent.mkdir(parents=True, exist_ok=True)


def initialize_database() -> None:
    """Initialize the database by creating all defined tables."""
    logger.info("Initializing database...")
    ensure_database_directory()
    try:
        SQLModel.metadata.create_all(engine)
        logger.info("Database tables created successfully.")
    except Exception as e:
        logger.error(f"Failed to initialize database tables: {e}")
        raise e
