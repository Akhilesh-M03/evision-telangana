from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel


class DistrictAnalytics(SQLModel, table=True):
    """Represents analytical output for a district."""

    __tablename__ = "district_analytics"

    id: int | None = Field(default=None, primary_key=True)
    district_id: int = Field(foreign_key="districts.id", index=True, nullable=False)
    cluster_id: int = Field(nullable=False)
    historical_average_demand: float | None = Field(default=None, nullable=True)
    trend_label: str | None = Field(default=None, nullable=True)
    generated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    # Relationships
    district: "District" = Relationship(back_populates="analytics")
