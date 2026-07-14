from sqlmodel import Session, select
from pydantic import BaseModel

from models.historical_demand import HistoricalDemand
from repositories.base import BaseRepository


class HistoricalDemandCreate(BaseModel):
    pass

class HistoricalDemandUpdate(BaseModel):
    pass


class HistoricalDemandRepository(BaseRepository[HistoricalDemand, HistoricalDemandCreate, HistoricalDemandUpdate]):
    def __init__(self):
        super().__init__(HistoricalDemand)

    def get_by_district(
        self, session: Session, district_id: int, skip: int = 0, limit: int = 100
    ) -> list[HistoricalDemand]:
        statement = (
            select(HistoricalDemand)
            .where(HistoricalDemand.district_id == district_id)
            .order_by(HistoricalDemand.reporting_month) # type: ignore
            .offset(skip)
            .limit(limit)
        )
        return session.exec(statement).all()

    def get_total_demand(self, session: Session) -> float:
        from sqlmodel import func
        statement = select(func.sum(HistoricalDemand.demand_kwh))
        result = session.exec(statement).one_or_none()
        return float(result) if result else 0.0

    def get_total_demand_by_district(self, session: Session, district_id: int) -> float:
        from sqlmodel import func
        statement = select(func.sum(HistoricalDemand.demand_kwh)).where(
            HistoricalDemand.district_id == district_id
        )
        result = session.exec(statement).one_or_none()
        return float(result) if result else 0.0
        
    def get_monthly_trend(self, session: Session) -> list[tuple[str, float]]:
        from sqlmodel import func
        statement = (
            select(HistoricalDemand.reporting_month, func.sum(HistoricalDemand.demand_kwh))
            .group_by(HistoricalDemand.reporting_month)
            .order_by(HistoricalDemand.reporting_month) # type: ignore
        )
        return session.exec(statement).all() # type: ignore

historical_demand_repository = HistoricalDemandRepository()
