from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel


class DistrictPrediction(SQLModel, table=True):
    """Represents predicted charging demand for a district."""

    __tablename__ = "district_predictions"

    id: int | None = Field(default=None, primary_key=True)
    district_id: int = Field(foreign_key="districts.id", index=True, nullable=False)
    forecast_period: str = Field(nullable=False)
    predicted_demand: float = Field(nullable=False)
    model_version: str | None = Field(default=None, nullable=True)
    generated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    # Relationships
    district: "District" = Relationship(back_populates="predictions")
