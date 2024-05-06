"""src/routes/game_penalty.py

Keyword arguments:
argument -- create, reall_all, read_one, update, delete
Return: create, reall_all, read_one, update, delete
"""

from flask import Blueprint
from flask_restful import Api

from resources import GamePenaltyResource

GamePenaltyBlueprint = Blueprint("game_penalty", __name__)
api = Api(GamePenaltyBlueprint)

GamePenaltyBlueprint.route(
    "/game-penalties", methods=["POST"])(GamePenaltyResource.create)
GamePenaltyBlueprint.route(
    "/game-penalties", methods=["GET"])(GamePenaltyResource.read_all)
GamePenaltyBlueprint.route("/game-penalties/<uuid:id>",
                           methods=["GET"])(GamePenaltyResource.read_one)
GamePenaltyBlueprint.route("/game-penalties/<uuid:id>",
                           methods=["PUT"])(GamePenaltyResource.update)
GamePenaltyBlueprint.route("/game-penalties/<uuid:id>",
                           methods=["DELETE"])(GamePenaltyResource.delete)
