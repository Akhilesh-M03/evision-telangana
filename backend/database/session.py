from typing import Generator

from sqlmodel import Session

from database.engine import engine


def get_session() -> Generator[Session, None, None]:
    """Provide a database session dependency.

    Yields:
        Session: The active SQLModel session.
    """
    with Session(engine) as session:
        yield session
