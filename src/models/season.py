"""src/models/season.py

Keyword arguments:
argument -- Base
Return: Season's id, season, created_at, updated_at
"""


from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID

from . import db
from .abc import BaseModel, MetaBaseModel


class SeasonModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ Season model """

    __tablename__ = "seasons"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    season = db.Column(db.String(50), nullable=False)

    created_at = db.Column(
        db.DateTime(), default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime(), onupdate=datetime.utcnow,
                           default=datetime.utcnow, nullable=False)
