"""src/routes/player.py

Keyword arguments:
argument -- create, reall_all, read_one, update, delete
Return: create, reall_all, read_one, update, delete
"""

from flask import Blueprint
from flask_restful import Api

from resources import PlayerResource

PlayerBlueprint = Blueprint("player", __name__)
api = Api(PlayerBlueprint)

PlayerBlueprint.route("/players", methods=["POST"])(PlayerResource.create)
PlayerBlueprint.route("/players", methods=["GET"])(PlayerResource.read_all)
PlayerBlueprint.route("/players/<uuid:id>",
                      methods=["GET"])(PlayerResource.read_one)
PlayerBlueprint.route("/players/<uuid:id>",
                      methods=["PUT"])(PlayerResource.update)
PlayerBlueprint.route("/players/<uuid:id>",
                      methods=["DELETE"])(PlayerResource.delete)
