"""src/models/league.py

Keyword arguments:
argument -- db.Model, BaseModel, metaclass=MetaBaseModel
Return: League's id, name, league_type, logo, country_id, teams, created_at,
updated_at
"""

from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy import UUID

from . import db
from .abc import BaseModel, MetaBaseModel


class LeagueModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """League model"""

    __tablename__ = "leagues"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = db.Column(db.String(50), nullable=False)
    abbr = db.Column(db.String(50), nullable=False)
    league_type = db.Column(db.String(50), nullable=False)
    logo = db.Column(db.String(), nullable=True)

    created_at = db.Column(
        db.DateTime(), default=datetime.now(timezone.utc), nullable=False)
    updated_at = db.Column(db.DateTime(), onupdate=datetime.now(timezone.utc),
                           default=datetime.now(timezone.utc), nullable=False)

    # foreign keys

    country_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("countries.id"), nullable=False
    )

    # relationships

    games = db.relationship("GameModel", backref="leagues", lazy=True)
