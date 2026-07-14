from sqlmodel import Session, select
from pydantic import BaseModel

from models.district import District
from repositories.base import BaseRepository


class DistrictCreate(BaseModel):
    pass

class DistrictUpdate(BaseModel):
    pass


class DistrictRepository(BaseRepository[District, DistrictCreate, DistrictUpdate]):
    def __init__(self):
        super().__init__(District)

    def search(
        self, session: Session, query: str, skip: int = 0, limit: int = 100
    ) -> list[District]:
        statement = (
            select(District)
            .where(District.district_name.ilike(f"%{query}%"))
            .offset(skip)
            .limit(limit)
        )
        return session.exec(statement).all()

    def get_by_name(self, session: Session, district_name: str) -> District | None:
        statement = select(District).where(District.district_name == district_name)
        return session.exec(statement).first()

district_repository = DistrictRepository()
