"""src/models/player_transfer.py

Keyword arguments:
argument -- db.Model, BaseModel, metaclass=MetaBaseModel
Return: Season's id, season, year, start_date, end_date, current, created_at,
updated_at
"""

from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID

from . import db
from .abc import BaseModel, MetaBaseModel


class PlayerTransferModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """Player Transfer model"""

    __tablename__ = "player_transfers"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    amount = db.Column(db.Integer, nullable=False)
    transfer_window = db.Column(db.String(), nullable=False)  # noqa | jan or aug
    transfer_type = db.Column(db.String(), nullable=False)  # noqa | buy or sell

    created_at = db.Column(
        db.DateTime(), default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime(), onupdate=datetime.utcnow,
                           default=datetime.utcnow, nullable=False)

    # foreign keys

    player_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        "players.id"), nullable=False)
    season_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        "seasons.id"), nullable=False)
    team_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        "teams.id"), nullable=False)
