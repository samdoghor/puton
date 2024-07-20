"""src/models/team.py

Keyword arguments:
argument -- db.Model, BaseModel, metaclass=MetaBaseModel
Return: Team's id, name, abbr, flag, founded, country_id, league_id, games,
venues, created_at, updated_at
"""

from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID

from . import db
from .abc import BaseModel, MetaBaseModel


class TeamModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """Team model"""

    __tablename__ = "teams"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = db.Column(db.String(), nullable=False)
    abbr = db.Column(db.String(), nullable=False)
    flag = db.Column(db.String(), nullable=True)
    founded = db.Column(db.Integer, nullable=False)

    created_at = db.Column(
        db.DateTime(), default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime(), onupdate=datetime.utcnow,
                           default=datetime.utcnow, nullable=False)

    # foreign keys

    country_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        "countries.id"), nullable=False)

    # relationships

    coaches_employment = db.relationship(
        "CoachEmployModel", backref="teams", lazy=True)
    game_teams = db.relationship("GameTeamModel", backref="teams", lazy=True)
    players = db.relationship("PlayerModel", backref="teams", lazy=True)
    players_tranfers = db.relationship(
        "PlayerTransferModel", backref="teams", lazy=True)
    venues = db.relationship("VenueModel", backref="teams", lazy=True)
