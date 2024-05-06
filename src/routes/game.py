"""src/routes/game.py

Keyword arguments:
argument -- create, reall_all, read_one, update, delete
Return: create, reall_all, read_one, update, delete
"""

from flask import Blueprint
from flask_restful import Api

from resources import GameResource

GameBlueprint = Blueprint("game", __name__)
api = Api(GameBlueprint)

GameBlueprint.route(
    "/games", methods=["POST"])(GameResource.create)
GameBlueprint.route(
    "/games", methods=["GET"])(GameResource.read_all)
GameBlueprint.route("/games/<uuid:id>",
                    methods=["GET"])(GameResource.read_one)
GameBlueprint.route("/games/<uuid:id>",
                    methods=["PUT"])(GameResource.update)
GameBlueprint.route("/games/<uuid:id>",
                    methods=["DELETE"])(GameResource.delete)
