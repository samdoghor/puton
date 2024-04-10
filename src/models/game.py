"""src/models/game.py

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


class GameModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """Game model"""

    __tablename__ = "games"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    created_at = db.Column(
        db.DateTime(), default=datetime.utcnow, nullable=False)
    updated_at = db.Column(
        db.DateTime(), onupdate=datetime.utcnow, default=datetime.utcnow,
        nullable=False
    )

    # foreign keys

    referee_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        "referees.id"), nullable=False)
