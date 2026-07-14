from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    apiVersion: str


class HealthLiveResponse(BaseModel):
    status: str


class HealthReadyResponse(BaseModel):
    status: str
    database: str
