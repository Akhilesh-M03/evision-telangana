from datetime import datetime

from pydantic import BaseModel


class ChargingStationBase(BaseModel):
    district_id: int
    station_name: str | None = None
    organization: str | None = None
    address: str | None = None
    latitude: float | None = None
    longitude: float | None = None


class ChargingStationResponse(ChargingStationBase):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}
