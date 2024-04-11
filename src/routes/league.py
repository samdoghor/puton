"""src/routes/league.py

Keyword arguments:
argument -- create, reall_all, read_one, update, delete
Return: create, reall_all, read_one, update, delete
"""

from flask import Blueprint
from flask_restful import Api

from resources import LeagueResource

LeagueBlueprint = Blueprint("league", __name__)
api = Api(LeagueBlueprint)

LeagueBlueprint.route("/leagues", methods=["POST"])(LeagueResource.create)
LeagueBlueprint.route("/leagues", methods=["GET"])(LeagueResource.read_all)
LeagueBlueprint.route("/leagues/<uuid:id>",
                      methods=["GET"])(LeagueResource.read_one)
LeagueBlueprint.route("/leagues/<uuid:id>",
                      methods=["PUT"])(LeagueResource.update)
LeagueBlueprint.route("/leagues/<uuid:id>",
                      methods=["DELETE"])(LeagueResource.delete)
