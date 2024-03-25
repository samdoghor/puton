"""src/resource/season.py

Keyword arguments:
argument -- season
Return: Country's uuid, name, code, created_at, updated_at
"""

from flask.json import jsonify
from flask_restful.reqparse import Argument
from sqlalchemy.exc import DataError

from models import SeasonModel
from utils import (Conflict, DataNotFound, Forbidden, InternalServerError,
                   parse_params)


class SeasonRoute:
    """ This class CRUD Season Operation """

    def create_season():
        """ creates a new season """
