"""src/routes/coach.py

Keyword arguments:
argument -- create, reall_all, read_one, update, delete
Return: create, reall_all, read_one, update, delete
"""

from flask import Blueprint
from flask_restful import Api

from resources import CoachResource

CoachBlueprint = Blueprint("coach", __name__)
api = Api(CoachBlueprint)

CoachBlueprint.route("/coaches", methods=["POST"])(CoachResource.create)
CoachBlueprint.route("/coaches", methods=["GET"])(CoachResource.read_all)
CoachBlueprint.route("/coaches/<uuid:id>",
                     methods=["GET"])(CoachResource.read_one)
CoachBlueprint.route("/coaches/<uuid:id>",
                     methods=["PUT"])(CoachResource.update)
CoachBlueprint.route("/coaches/<uuid:id>",
                     methods=["DELETE"])(CoachResource.delete)
