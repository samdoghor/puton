"""src/models/game_player.py

Keyword arguments:
argument -- db.Model, BaseModel, metaclass=MetaBaseModel
Return: Game's id, first_name, last_name, middle_name, country_id, team_id,
created_at, updated_at
"""

from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID

from . import db
from .abc import BaseModel, MetaBaseModel


class GamePlayerModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """Game Player model"""

    __tablename__ = "game_players"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    starting_lineup = db.Column(db.Boolean, nullable=False, default=False)
    substitute = db.Column(db.Boolean, nullable=False, default=False)
    minutes_played = db.Column(db.Integer, nullable=False)

    created_at = db.Column(
        db.DateTime(), default=datetime.utcnow, nullable=False)
    updated_at = db.Column(
        db.DateTime(), onupdate=datetime.utcnow, default=datetime.utcnow,
        nullable=False
    )

    # foreign keys

    game_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        "games.id"), nullable=False)
    game_team_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        "game_teams.id"), nullable=False)
    player_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        "players.id"), nullable=False)

    # relationships

    game_events = db.relationship(
        "GameEventModel", backref="game_players", lazy=True)
