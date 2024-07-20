"""src/models/player.py

Keyword arguments:
argument -- db.Model, BaseModel, metaclass=MetaBaseModel
Return: Player's id, first_name, last_name, middle_name, date_of_birth,
height, weight, rating, postion, injury, country_id, team_id, created_at,
updated_at
"""

from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID

from . import db
from .abc import BaseModel, MetaBaseModel


class PlayerModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """Player model"""

    __tablename__ = "players"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50), nullable=True)
    date_of_birth = db.Column(db.Date(), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    postion = db.Column(db.String(50), nullable=False)
    injury = db.Column(db.Boolean, nullable=False, default=False)
    footed = db.Column(db.String(50), nullable=False)
    retired = db.Column(db.Boolean, nullable=False, default=False)

    created_at = db.Column(
        db.DateTime(), default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime(), onupdate=datetime.utcnow,
                           default=datetime.utcnow, nullable=False)

    # foreign keys

    country_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        "countries.id"), nullable=False)
    team_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        "teams.id"), nullable=False)

    # relationships

    game_players = db.relationship(
        "GamePlayerModel", backref="players", lazy=True)
    transfer = db.relationship(
        "PlayerTransferModel", backref="players", lazy=True)
