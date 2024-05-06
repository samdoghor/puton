"""src/routes/player_transfer.py

Keyword arguments:
argument -- create, reall_all, read_one, update, delete
Return: create, reall_all, read_one, update, delete
"""

from flask import Blueprint
from flask_restful import Api

from resources import PlayerTransferResource

PlayerTransferBlueprint = Blueprint("player_transfer", __name__)
api = Api(PlayerTransferBlueprint)

PlayerTransferBlueprint.route(
    "/players-transfers", methods=["POST"])(PlayerTransferResource.create)
PlayerTransferBlueprint.route(
    "/players-transfers", methods=["GET"])(PlayerTransferResource.read_all)
PlayerTransferBlueprint.route("/players-transfers/<uuid:id>",
                              methods=["GET"])(PlayerTransferResource.read_one)
PlayerTransferBlueprint.route("/players-transfers/<uuid:id>",
                              methods=["PUT"])(PlayerTransferResource.update)
PlayerTransferBlueprint.route(
    "/players-transfers/<uuid:id>",
    methods=["DELETE"])(PlayerTransferResource.delete)
