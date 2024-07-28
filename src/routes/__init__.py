"""src/routes/__init__.py

Keyword arguments:
argument -- None
Return: all routes
"""

from .coach import CoachBlueprint
from .coach_employ import CoachEmployBlueprint
from .country import CountryBlueprint
from .game import GameBlueprint
from .game_event import GameEventBlueprint
from .game_penalty import GamePenaltyBlueprint
from .game_player import GamePlayerBlueprint
from .game_team import GameTeamBlueprint
from .index import IndexBlueprint
from .league import LeagueBlueprint
from .player import PlayerBlueprint
from .player_transfer import PlayerTransferBlueprint
from .referee import RefereeBlueprint
from .season import SeasonBlueprint
from .team import TeamBlueprint
from .venue import VenueBlueprint
