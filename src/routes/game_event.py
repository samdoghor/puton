"""src/routes/game_event.py

Keyword arguments:
argument -- create, reall_all, read_one, update, delete
Return: create, reall_all, read_one, update, delete
"""

from flask import Blueprint
from flask_restful import Api

from resources import GameEventResource

GameEventBlueprint = Blueprint("game_event", __name__)
api = Api(GameEventBlueprint)

GameEventBlueprint.route(
    "/game-events", methods=["POST"])(GameEventResource.create)
GameEventBlueprint.route(
    "/game-events", methods=["GET"])(GameEventResource.read_all)
GameEventBlueprint.route("/game-events/<uuid:id>",
                         methods=["GET"])(GameEventResource.read_one)
GameEventBlueprint.route("/game-events/<uuid:id>",
                         methods=["PUT"])(GameEventResource.update)
GameEventBlueprint.route("/game-events/<uuid:id>",
                         methods=["DELETE"])(GameEventResource.delete)
