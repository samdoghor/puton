"""src/models/team.py

Keyword arguments:
argument -- db.Model, BaseModel, metaclass=MetaBaseModel
Return: Team's id, name, abbr, flag, founded, country_id, league_id, games,
venues, created_at, updated_at
"""

from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID

from . import db
from .abc import BaseModel, MetaBaseModel


class TeamModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ Team model """

    __tablename__ = 'teams'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = db.Column(db.String(50), nullable=False)
    abbr = db.Column(db.String(10), nullable=False)
    flag = db.Column(db.String(), nullable=True)
    founded = db.Column(db.Integer, nullable=False)

    created_at = db.Column(
        db.DateTime(), default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime(), onupdate=datetime.utcnow,
                           default=datetime.utcnow, nullable=False)

    # foreign keys

    country_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        'countries.id'), nullable=False)
    league_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        'leagues.id'), nullable=False)

    # relationships

    venues = db.relationship('VenueModel', backref='teams', lazy=True)
