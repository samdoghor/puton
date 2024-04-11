"""src/routes/season.py

Keyword arguments:
argument -- create, reall_all, read_one, update, delete
Return: create, reall_all, read_one, update, delete
"""

from flask import Blueprint
from flask_restful import Api

from resources import SeasonResource

SeasonBlueprint = Blueprint("season", __name__)
api = Api(SeasonBlueprint)

SeasonBlueprint.route("/seasons", methods=["POST"])(SeasonResource.create)
SeasonBlueprint.route("/seasons", methods=["GET"])(SeasonResource.read_all)
SeasonBlueprint.route("/seasons/<uuid:id>",
                      methods=["GET"])(SeasonResource.read_one)
SeasonBlueprint.route("/seasons/<uuid:id>",
                      methods=["PUT"])(SeasonResource.update)
SeasonBlueprint.route("/seasons/<uuid:id>",
                      methods=["DELETE"])(SeasonResource.delete)
