from fastapi import APIRouter, Depends, Query, status
from sqlmodel import Session

from database.session import get_session
from schemas.charging_station import ChargingStationResponse
from schemas.pagination import PaginatedResponse
from services.charging_station_service import charging_station_service

router = APIRouter(
    prefix="/charging-stations",
    tags=["Charging Stations"],
)

@router.get(
    "",
    response_model=PaginatedResponse[ChargingStationResponse],
    summary="Get all charging stations",
    status_code=status.HTTP_200_OK
)
async def get_all_charging_stations(
    district_id: int | None = Query(None, description="Filter by district ID"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    session: Session = Depends(get_session)
):
    return charging_station_service.get_all_stations(
        session, district_id=district_id, skip=skip, limit=limit
    )

@router.get(
    "/{id}",
    response_model=ChargingStationResponse,
    summary="Get charging station by ID",
    status_code=status.HTTP_200_OK
)
async def get_charging_station(
    id: int,
    session: Session = Depends(get_session)
):
    return charging_station_service.get_station_by_id(session, station_id=id)
