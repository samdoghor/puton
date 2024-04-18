"""src/models/venue.py

Keyword arguments:
argument -- db.Model, BaseModel, metaclass=MetaBaseModel
Return: Venue's id, name, address, city, capacity, team_id, created_at,
updated_at
"""

from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID

from . import db
from .abc import BaseModel, MetaBaseModel


class VenueModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """Venue model"""

    __tablename__ = "venues"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.Text(), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

    created_at = db.Column(
        db.DateTime(), default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime(), onupdate=datetime.utcnow,
                           default=datetime.utcnow, nullable=False)

    # foreign keys

    team_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        "teams.id"), nullable=False)

    # relationships

    games = db.relationship("GameModel", backref="venues", lazy=True)
