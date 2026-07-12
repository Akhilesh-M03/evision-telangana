from sqlmodel import create_engine

from core.settings import settings

engine = create_engine(
    settings.database_url,
    echo=settings.debug,
)
