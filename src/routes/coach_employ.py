"""src/routes/coach_employ.py

Keyword arguments:
argument -- create, reall_all, read_one, update, delete
Return: create, reall_all, read_one, update, delete
"""

from flask import Blueprint
from flask_restful import Api

from resources import CoachEmployResource

CoachEmployBlueprint = Blueprint("coach_employ", __name__)
api = Api(CoachEmployBlueprint)

CoachEmployBlueprint.route(
    "/coaches-employ", methods=["POST"])(CoachEmployResource.create)
CoachEmployBlueprint.route(
    "/coaches-employ", methods=["GET"])(CoachEmployResource.read_all)
CoachEmployBlueprint.route("/coaches-employ/<uuid:id>",
                           methods=["GET"])(CoachEmployResource.read_one)
CoachEmployBlueprint.route("/coaches-employ/<uuid:id>",
                           methods=["PUT"])(CoachEmployResource.update)
CoachEmployBlueprint.route("/coaches-employ/<uuid:id>",
                           methods=["DELETE"])(CoachEmployResource.delete)
