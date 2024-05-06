"""src/models/game_penalty.py

Keyword arguments:
argument -- db.Model, BaseModel, metaclass=MetaBaseModel
Return: Game Penalty's id, last_name, middle_name, country_id, team_id,
created_at, updated_at
"""

from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID

from . import db
from .abc import BaseModel, MetaBaseModel


class GamePenaltyModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """Game Penalty model"""

    __tablename__ = "game_penalties"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    is_penalty_shootout = db.Column(db.Boolean, nullable=False)
    is_goal = db.Column(db.Boolean, nullable=False)

    created_at = db.Column(
        db.DateTime(), default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime(), onupdate=datetime.utcnow,
                           default=datetime.utcnow, nullable=False)

    # foreign keys

    game_event_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        "game_events.id"), nullable=False)
