"""src/routes/game_team.py

Keyword arguments:
argument -- create, reall_all, read_one, update, delete
Return: create, reall_all, read_one, update, delete
"""

from flask import Blueprint
from flask_restful import Api

from resources import GameTeamResource

GameTeamBlueprint = Blueprint("game_team", __name__)
api = Api(GameTeamBlueprint)

GameTeamBlueprint.route(
    "/game-teams", methods=["POST"])(GameTeamResource.create)
GameTeamBlueprint.route(
    "/game-teams", methods=["GET"])(GameTeamResource.read_all)
GameTeamBlueprint.route("/game-teams/<uuid:id>",
                        methods=["GET"])(GameTeamResource.read_one)
GameTeamBlueprint.route("/game-teams/<uuid:id>",
                        methods=["PUT"])(GameTeamResource.update)
GameTeamBlueprint.route("/game-teams/<uuid:id>",
                        methods=["DELETE"])(GameTeamResource.delete)
