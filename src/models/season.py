"""src/models/season.py

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


class SeasonModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """Season model"""

    __tablename__ = "seasons"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    start_date = db.Column(db.Date(), nullable=False)
    end_date = db.Column(db.Date(), nullable=False)
    current_season = db.Column(db.Boolean, nullable=False, default=False)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow, nullable=False)
    updated_at = db.Column(
        db.DateTime(), onupdate=datetime.utcnow, default=datetime.utcnow, nullable=False
    )

    # relationships

    coaches_employment = db.relationship(
        "CoachEmployModel", backref="seasons", lazy=True
    )
    games = db.relationship("GameModel", backref="seasons", lazy=True)
    transfer = db.relationship("TransferModel", backref="seaons", lazy=True)
