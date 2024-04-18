"""src/routes/referee.py

Keyword arguments:
argument -- create, reall_all, read_one, update, delete
Return: create, reall_all, read_one, update, delete
"""

from flask import Blueprint
from flask_restful import Api

from resources import RefereeResource

RefereeBlueprint = Blueprint("referee", __name__)
api = Api(RefereeBlueprint)

RefereeBlueprint.route("/referees", methods=["POST"])(RefereeResource.create)
RefereeBlueprint.route("/referees", methods=["GET"])(RefereeResource.read_all)
RefereeBlueprint.route("/referees/<uuid:id>",
                       methods=["GET"])(RefereeResource.read_one)
RefereeBlueprint.route("/referees/<uuid:id>",
                       methods=["PUT"])(RefereeResource.update)
RefereeBlueprint.route("/referees/<uuid:id>", methods=["DELETE"])(
    RefereeResource.delete
)
