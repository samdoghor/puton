"""src/routes/team.py

Keyword arguments:
argument -- create, reall_all, read_one, update, delete
Return: create, reall_all, read_one, update, delete
"""

from flask import Blueprint
from flask_restful import Api

from resources import TeamResource

TeamBlueprint = Blueprint("team", __name__)
api = Api(TeamBlueprint)

TeamBlueprint.route("/teams", methods=["POST"])(TeamResource.create)
TeamBlueprint.route("/teams", methods=["GET"])(TeamResource.read_all)
TeamBlueprint.route("/teams/<uuid:id>", methods=["GET"])(TeamResource.read_one)
TeamBlueprint.route("/teams/<uuid:id>", methods=["PUT"])(TeamResource.update)
TeamBlueprint.route("/teams/<uuid:id>",
                    methods=["DELETE"])(TeamResource.delete)
