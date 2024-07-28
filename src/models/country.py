"""src/models/country.py

Keyword arguments:
argument -- db.Model, BaseModel, metaclass=MetaBaseModel
Return: Country's id, name, abbr, flag, teams, leauges, created_at, updated_at
"""

from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy import UUID

from . import db
from .abc import BaseModel, MetaBaseModel


class CountryModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """Country model"""

    __tablename__ = "countries"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = db.Column(db.String(50), nullable=False)
    abbr = db.Column(db.String(10), nullable=False)
    flag = db.Column(db.String(), nullable=True)

    created_at = db.Column(
        db.DateTime(), default=datetime.now(timezone.utc), nullable=False)
    updated_at = db.Column(db.DateTime(), onupdate=datetime.now(timezone.utc),
                           default=datetime.now(timezone.utc), nullable=False)

    # relationships

    coaches = db.relationship("CoachModel", backref="countries", lazy=True)
    leauges = db.relationship("LeagueModel", backref="countries", lazy=True)
    players = db.relationship("PlayerModel", backref="countries", lazy=True)
    teams = db.relationship("TeamModel", backref="countries", lazy=True)
