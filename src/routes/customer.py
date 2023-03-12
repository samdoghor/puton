"""
Defines the blueprint for the customer
"""
# imports
from flask import Blueprint

from resources import CustomerResource

CustomerBlueprint = Blueprint('customers', __name__)

CustomerBlueprint.route(
    "/customers", methods=['POST'])(CustomerResource.create)
CustomerBlueprint.route(
    "/customers", methods=['GET'])(CustomerResource.read_all)
CustomerBlueprint.route("/customers/<int:customer_id>",
                        methods=['GET'])(CustomerResource.read_one)
CustomerBlueprint.route("/customers/<int:id>",
                        methods=["PUT"])(CustomerResource.update)
CustomerBlueprint.route("/customers/<int:id>",
                        methods=["DELETE"])(CustomerResource.delete)
