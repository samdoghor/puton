"""src/routes/venue.py

Keyword arguments:
argument -- create, reall_all, read_one, update, delete
Return: create, reall_all, read_one, update, delete
"""

from flask import Blueprint
from flask_restful import Api

from resources import VenueResource

VenueBlueprint = Blueprint("venue", __name__)
api = Api(VenueBlueprint)

VenueBlueprint.route("/venues", methods=["POST"])(VenueResource.create)
VenueBlueprint.route("/venues", methods=["GET"])(VenueResource.read_all)
VenueBlueprint.route("/venues/<uuid:id>",
                     methods=["GET"])(VenueResource.read_one)
VenueBlueprint.route("/venues/<uuid:id>",
                     methods=["PUT"])(VenueResource.update)
VenueBlueprint.route("/venues/<uuid:id>",
                     methods=["DELETE"])(VenueResource.delete)
