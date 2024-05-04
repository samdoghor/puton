"""src/routes/game_Palyer.py

Keyword arguments:
argument -- create, reall_all, read_one, update, delete
Return: create, reall_all, read_one, update, delete
"""

from flask import Blueprint
from flask_restful import Api

from resources import GamePlayerResource

GamePlayerBlueprint = Blueprint("game_player", __name__)
api = Api(GamePlayerBlueprint)

GamePlayerBlueprint.route(
    "/game-players", methods=["POST"])(GamePlayerResource.create)
GamePlayerBlueprint.route(
    "/game-players", methods=["GET"])(GamePlayerResource.read_all)
GamePlayerBlueprint.route("/game-players/<uuid:id>",
                          methods=["GET"])(GamePlayerResource.read_one)
GamePlayerBlueprint.route("/game-players/<uuid:id>",
                          methods=["PUT"])(GamePlayerResource.update)
GamePlayerBlueprint.route("/game-players/<uuid:id>",
                          methods=["DELETE"])(GamePlayerResource.delete)
