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
from .coach_employ import CoachEmployModel
from .country import CountryModel
from .game import GameModel
from .game_event import GameEventModel
from .game_player import GamePlayerModel
from .game_team import GameTeamModel
from .league import LeagueModel
from .player import PlayerModel
from .player_transfer import PlayerTransferModel
from .referee import RefereeModel
from .season import SeasonModel
from .team import TeamModel
from .venue import VenueModel
