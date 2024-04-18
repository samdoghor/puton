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

from .coach_employ import CoachEmployModel
from .coach import CoachModel
from .country import CountryModel
from .game_event import GameEventModel
from .game_player import GamePlayerModel
from .game_team import GameTeamModel
from .game import GameModel
from .league import LeagueModel
from .player_transfer import PlayerTransferModel
from .player import PlayerModel
from .referee import RefereeModel
from .season import SeasonModel
from .team import TeamModel
from .venue import VenueModel
