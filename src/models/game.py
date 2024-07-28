"""src/models/game.py

Keyword arguments:
argument -- db.Model, BaseModel, metaclass=MetaBaseModel
Return: Game's id, first_name, last_name, middle_name, country_id, team_id,
created_at, updated_at
"""

from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy import UUID

from . import db
from .abc import BaseModel, MetaBaseModel


class GameModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """Game model"""

    __tablename__ = "games"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    game_time = db.Column(db.Time(), nullable=False)
    game_date = db.Column(db.Date(), nullable=False)
    game_week = db.Column(db.Integer, nullable=False)
    weather = db.Column(db.String(50), nullable=False)

    created_at = db.Column(
        db.DateTime(), default=datetime.now(timezone.utc), nullable=False)
    updated_at = db.Column(db.DateTime(), onupdate=datetime.now(timezone.utc),
                           default=datetime.now(timezone.utc), nullable=False)

    # foreign keys

    league_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        "leagues.id"), nullable=False)
    referee_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        "referees.id"), nullable=False)
    season_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        "seasons.id"), nullable=False)
    venue_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        "venues.id"), nullable=False)

    # relationships

    game_events = db.relationship("GameEventModel", backref="games", lazy=True)
    game_players = db.relationship(
        "GamePlayerModel", backref="games", lazy=True)
    game_teams = db.relationship("GameTeamModel", backref="games", lazy=True)
