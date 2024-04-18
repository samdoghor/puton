"""src/routes/index.py

Keyword arguments:
argument -- none
Return: homepage endpoint
"""

from flask.blueprints import Blueprint
from flask_restful import Api

from resources import IndexResource

IndexBlueprint = Blueprint("index", __name__)
api = Api(IndexBlueprint)

IndexBlueprint.route("/", methods=["GET"])(IndexResource.home)
