from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class District(SQLModel, table=True):
    """Represents a Telangana district."""

    __tablename__ = "districts"

    id: int | None = Field(default=None, primary_key=True)
    district_name: str = Field(index=True, unique=True, nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    # Relationships
    charging_stations: list["ChargingStation"] = Relationship(back_populates="district")
    historical_demand: list["HistoricalDemand"] = Relationship(back_populates="district")
    predictions: list["DistrictPrediction"] = Relationship(back_populates="district")
    analytics: Optional["DistrictAnalytics"] = Relationship(
        back_populates="district",
        sa_relationship_kwargs={"uselist": False}
    )
    recommendation: Optional["DistrictRecommendation"] = Relationship(
        back_populates="district",
        sa_relationship_kwargs={"uselist": False}
    )
