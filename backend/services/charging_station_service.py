from fastapi import HTTPException
from sqlmodel import Session

from repositories.charging_station_repository import charging_station_repository
from repositories.district_repository import district_repository
from schemas.charging_station import ChargingStationResponse
from schemas.pagination import PaginatedResponse


class ChargingStationService:
    def get_station_by_id(self, session: Session, station_id: int) -> ChargingStationResponse:
        station = charging_station_repository.get(session, station_id)
        if not station:
            raise HTTPException(status_code=404, detail=f"Charging station {station_id} not found")
        return ChargingStationResponse.model_validate(station)

    def get_all_stations(
        self, session: Session, district_id: int | None = None, skip: int = 0, limit: int = 100
    ) -> PaginatedResponse[ChargingStationResponse]:
        if district_id:
            # Check if district exists
            district = district_repository.get(session, district_id)
            if not district:
                raise HTTPException(status_code=404, detail=f"District {district_id} not found")
            stations = charging_station_repository.get_by_district(session, district_id, skip=skip, limit=limit)
            total = len(stations) # Ideally count_by_district
        else:
            stations = charging_station_repository.get_all(session, skip=skip, limit=limit)
            total = charging_station_repository.count(session)
            
        return PaginatedResponse(
            items=[ChargingStationResponse.model_validate(s) for s in stations],
            total=total,
            page=skip // limit + 1 if limit > 0 else 1,
            size=limit,
            pages=(total + limit - 1) // limit if limit > 0 else 1
        )

charging_station_service = ChargingStationService()
