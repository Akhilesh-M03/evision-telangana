from datetime import datetime

from sqlmodel import Field, SQLModel


class ApplicationMetadata(SQLModel, table=True):
    """Represents application metadata."""

    __tablename__ = "application_metadata"

    id: int | None = Field(default=None, primary_key=True)
    metadata_key: str = Field(index=True, unique=True, nullable=False)
    metadata_value: str = Field(nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
