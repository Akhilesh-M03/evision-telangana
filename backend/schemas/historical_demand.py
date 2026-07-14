from datetime import datetime

from pydantic import BaseModel


class HistoricalDemandBase(BaseModel):
    district_id: int
    reporting_month: str
    demand_kwh: float


class HistoricalDemandResponse(HistoricalDemandBase):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}
