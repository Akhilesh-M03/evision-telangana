from datetime import datetime

from sqlalchemy import CheckConstraint
from sqlmodel import Field, Relationship, SQLModel


class DistrictRecommendation(SQLModel, table=True):
    """Represents decision engine recommendation output for a district."""

    __tablename__ = "district_recommendations"

    id: int | None = Field(default=None, primary_key=True)
    district_id: int = Field(foreign_key="districts.id", index=True, nullable=False)
    priority_score: float = Field(nullable=False)
    priority_level: str = Field(nullable=False)
    district_rank: int = Field(nullable=False)
    generated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    # Relationships
    district: "District" = Relationship(back_populates="recommendation")

    __table_args__ = (
        CheckConstraint("priority_score >= 0", name="chk_district_recommendations_priority_score"),
        CheckConstraint("district_rank > 0", name="chk_district_recommendations_district_rank"),
    )
