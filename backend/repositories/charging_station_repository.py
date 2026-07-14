from sqlmodel import Session, select
from pydantic import BaseModel

from models.charging_stations import ChargingStation
from repositories.base import BaseRepository


class ChargingStationCreate(BaseModel):
    pass

class ChargingStationUpdate(BaseModel):
    pass


class ChargingStationRepository(BaseRepository[ChargingStation, ChargingStationCreate, ChargingStationUpdate]):
    def __init__(self):
        super().__init__(ChargingStation)

    def get_by_district(
        self, session: Session, district_id: int, skip: int = 0, limit: int = 100
    ) -> list[ChargingStation]:
        statement = (
            select(ChargingStation)
            .where(ChargingStation.district_id == district_id)
            .offset(skip)
            .limit(limit)
        )
        return session.exec(statement).all()
        
    def count_by_organization(self, session: Session) -> list[tuple[str, int]]:
        from sqlmodel import func
        statement = (
            select(ChargingStation.organization, func.count(ChargingStation.id))
            .where(ChargingStation.organization.is_not(None))
            .group_by(ChargingStation.organization)
        )
        return session.exec(statement).all() # type: ignore

charging_station_repository = ChargingStationRepository()
