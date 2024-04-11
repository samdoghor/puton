"""src/models/referee.py

Keyword arguments:
argument -- db.Model, BaseModel, metaclass=MetaBaseModel
Return: Referee's id, first_name, last_name, middle_name, country_id, team_id,
created_at, updated_at
"""

from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID

from . import db
from .abc import BaseModel, MetaBaseModel


class RefereeModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """Referee model"""

    __tablename__ = "referees"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50), nullable=True)

    created_at = db.Column(
        db.DateTime(), default=datetime.utcnow, nullable=False)
    updated_at = db.Column(
        db.DateTime(), onupdate=datetime.utcnow, default=datetime.utcnow,
        nullable=False
    )

    # foreign keys

    country_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        "countries.id"), nullable=False)

    # relationships

    games = db.relationship("GameModel", backref="referees", lazy=True)
