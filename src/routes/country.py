"""src/routes/country.py

Keyword arguments:
argument -- create, reall_all, read_one, update, delete
Return: create, reall_all, read_one, update, delete
"""

from flask import Blueprint
from flask_restful import Api

from resources import CountryResource

CountryBlueprint = Blueprint("country", __name__)
api = Api(CountryBlueprint)

CountryBlueprint.route("/countries", methods=["POST"])(CountryResource.create)
CountryBlueprint.route("/countries", methods=["GET"])(CountryResource.read_all)
CountryBlueprint.route("/countries/<uuid:id>", methods=["GET"])(
    CountryResource.read_one
)
CountryBlueprint.route("/countries/<uuid:id>",
                       methods=["PUT"])(CountryResource.update)
CountryBlueprint.route("/countries/<uuid:id>", methods=["DELETE"])(
    CountryResource.delete
)
