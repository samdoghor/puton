"""src/models/__init__.py

Keyword arguments:
argument -- None
Return: all models
"""

# external import
from flask_sqlalchemy import SQLAlchemy

# database initialisation

db = SQLAlchemy()

# internal import

from .coach import CoachModel
from .country import CountryModel
from .game import GameModel
from .league import LeagueModel
from .player import PlayerModel
from .season import SeasonModel
from .team import TeamModel
from .venue import VenueModel
