from datetime import datetime

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel


class HistoricalDemand(SQLModel, table=True):
    """Represents historical EV charging demand for a district in a specific month."""

    __tablename__ = "historical_demand"

    id: int | None = Field(default=None, primary_key=True)
    district_id: int = Field(foreign_key="districts.id", index=True, nullable=False)
    reporting_month: str = Field(index=True, nullable=False)
    demand_kwh: float = Field(nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    # Relationships
    district: "District" = Relationship(back_populates="historical_demand")

    __table_args__ = (
        UniqueConstraint("district_id", "reporting_month", name="uq_historical_demand_district_month"),
    )
