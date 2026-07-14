from typing import Generic, TypeVar
from sqlmodel import Session, select
from pydantic import BaseModel

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: type[ModelType]):
        self.model = model

    def get(self, session: Session, id: int) -> ModelType | None:
        return session.get(self.model, id)

    def get_all(
        self, session: Session, *, skip: int = 0, limit: int = 100
    ) -> list[ModelType]:
        statement = select(self.model).offset(skip).limit(limit)
        return session.exec(statement).all()

    def count(self, session: Session) -> int:
        from sqlmodel import func
        statement = select(func.count()).select_from(self.model)
        return session.exec(statement).one()
