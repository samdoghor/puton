"""src/models/game_team.py

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


class GameTeamModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """Game Team model"""

    __tablename__ = "game_teams"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    is_home = db.Column(db.Boolean, nullable=False, default=False)

    created_at = db.Column(
        db.DateTime(), default=datetime.now(timezone.utc), nullable=False)
    updated_at = db.Column(db.DateTime(), onupdate=datetime.now(timezone.utc),
                           default=datetime.now(timezone.utc), nullable=False)

    # foreign keys

    game_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        "games.id"), nullable=False)
    team_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        "teams.id"), nullable=False)

    # relationships

    game_events = db.relationship(
        "GameEventModel", backref="game_teams", lazy=True)
    game_players = db.relationship(
        "GamePlayerModel", backref="game_teams", lazy=True)
