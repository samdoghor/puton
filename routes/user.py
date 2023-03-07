"""
Defines the blueprint for the user
"""
# imports
from flask import Blueprint
from resources import UserResource

UserBlueprint = Blueprint('users', __name__)

UserBlueprint.route("/users", methods=['POST'])(UserResource.create)
UserBlueprint.route("/users", methods=['GET'])(UserResource.get_all)
UserBlueprint.route("/users/<int:user_id>", methods=['GET'])(UserResource.get_one)
UserBlueprint.route("/users/<int:user_id>", methods=["PUT"])(UserResource.update)
UserBlueprint.route("/users/<int:user_id>", methods=["DELETE"])(UserResource.delete)