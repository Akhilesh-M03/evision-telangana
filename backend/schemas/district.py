from datetime import datetime

from pydantic import BaseModel


class DistrictBase(BaseModel):
    district_name: str


class DistrictResponse(DistrictBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
