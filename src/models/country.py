"""src/models/country.py

Keyword arguments:
argument -- Base
Return: Country's uuid, name, code, created_at, updated_at
"""


from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID, Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Country(Base):
    """ State class """
    __tablename__ = 'countries'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(128), nullable=False)
    abbr = Column(String(128), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, onupdate=datetime.utcnow,
                        default=datetime.utcnow, nullable=False)
