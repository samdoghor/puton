"""src/models/game_draw.py

Keyword arguments:
argument -- db.Model, BaseModel, metaclass=MetaBaseModel
Return: Game Draw's id, game_id, created_at, updated_at
"""


from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID

from . import db
from .abc import BaseModel, MetaBaseModel


class GameDrawModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ Game Draw model """

    __tablename__ = 'games_drew'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    created_at = db.Column(
        db.DateTime(), default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime(), onupdate=datetime.utcnow,
                           default=datetime.utcnow, nullable=False)

    # foreign keys

    game_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        'games.id'), nullable=False)
