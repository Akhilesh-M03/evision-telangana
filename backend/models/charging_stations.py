from datetime import datetime

from sqlalchemy import CheckConstraint
from sqlmodel import Field, Relationship, SQLModel


class ChargingStation(SQLModel, table=True):
    """Represents a charging station in Telangana."""

    __tablename__ = "charging_stations"

    id: int | None = Field(default=None, primary_key=True)
    district_id: int = Field(foreign_key="districts.id", index=True, nullable=False)
    station_name: str | None = Field(default=None, nullable=True)
    organization: str | None = Field(default=None, nullable=True)
    address: str | None = Field(default=None, nullable=True)
    latitude: float | None = Field(default=None, nullable=True)
    longitude: float | None = Field(default=None, nullable=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    # Relationships
    district: "District" = Relationship(back_populates="charging_stations")

    __table_args__ = (
        CheckConstraint("latitude BETWEEN -90 AND 90", name="chk_charging_stations_latitude"),
        CheckConstraint("longitude BETWEEN -180 AND 180", name="chk_charging_stations_longitude"),
    )
