"""src/models/coach_employ.py

Keyword arguments:
argument -- db.Model, BaseModel, metaclass=MetaBaseModel
Return: Season's id, season, year, start_date, end_date, current, created_at,
updated_at
"""

from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID

from . import db
from .abc import BaseModel, MetaBaseModel


class CoachEmployModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """Coach Employ model"""

    __tablename__ = "coaches_employment"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    employment_type = db.Column(db.String(), nullable=False)

    created_at = db.Column(
        db.DateTime(), default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime(), onupdate=datetime.utcnow,
                           default=datetime.utcnow, nullable=False)

    # foreign keys

    coach_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("coaches.id"), nullable=False
    )
    season_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("seasons.id"), nullable=False
    )
    team_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        "teams.id"), nullable=False)
