"""src/models/game_event.py

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


class GameEventModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """Game Event model"""

    __tablename__ = "game_events"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    event_type = db.Column(db.String(), nullable=False)  # noqa | goals, yellow card etc
    event_time = db.Column(db.Integer, nullable=False)
    game_half = db.Column(db.Integer, nullable=False)

    created_at = db.Column(
        db.DateTime(), default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime(), onupdate=datetime.utcnow,
                           default=datetime.utcnow, nullable=False)

    # foreign keys

    game_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        "games.id"), nullable=False)
    game_player_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("game_players.id"), nullable=False
    )
    game_team_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("game_teams.id"), nullable=False
    )

    # relationships

    game_penalties = db.relationship(
        'GamePenaltyModel', backref='game_events', lazy=True)
