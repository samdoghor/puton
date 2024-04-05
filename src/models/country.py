"""src/models/country.py

Keyword arguments:
argument -- db.Model, BaseModel, metaclass=MetaBaseModel
Return: Country's id, name, abbr, flag, teams, leauges, created_at, updated_at
"""

from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID

from . import db
from .abc import BaseModel, MetaBaseModel


class CountryModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ Country model """

    __tablename__ = 'countries'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = db.Column(db.String(50), nullable=False)
    abbr = db.Column(db.String(10), nullable=False)
    flag = db.Column(db.String(), nullable=True)

    created_at = db.Column(
        db.DateTime(), default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime(), onupdate=datetime.utcnow,
                           default=datetime.utcnow, nullable=False)

    # relationships

    teams = db.relationship('TeamModel', backref='countries', lazy=True)
    leauges = db.relationship('LeagueModel', backref='countries', lazy=True)
