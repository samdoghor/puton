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

from .country import CountryModel
from .game import GameModel
from .game_draw import GameDrawModel
from .game_lose import GameLoseModel
from .game_played import GamePlayedModel
from .game_win import GameWinModel
from .league import LeagueModel
from .season import SeasonModel
from .team import TeamModel
from .venue import VenueModel
