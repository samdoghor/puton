"""src/models/game.py

Keyword arguments:
argument -- db.Model, BaseModel, metaclass=MetaBaseModel
Return: Game's id, created_at, updated_at
"""

from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID

from . import db
from .abc import BaseModel, MetaBaseModel


class GameModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ Game model """

    __tablename__ = 'games'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    game_date_time = db.Column(db.DateTime(), nullable=False)

    created_at = db.Column(
        db.DateTime(), default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime(), onupdate=datetime.utcnow,
                           default=datetime.utcnow, nullable=False)

    # foreign keys

    away_team_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        'teams.id'), nullable=False)
    home_team_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        'teams.id'), nullable=False)
    league_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        'leagues.id'), nullable=False)
    season_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        'seasons.id'), nullable=False)

    # relationships

    games_drew = db.relationship('GameDrawModel', backref='games', lazy=True)
    games_loss = db.relationship('GameLoseModel', backref='games', lazy=True)
    games_played = db.relationship(
        'GamePlayedModel', backref='games', lazy=True)
    games_won = db.relationship('GameWinModel', backref='games', lazy=True)
