"""
Define the resources for the Customer
"""
from flasgger import swag_from
from flask import jsonify, request
from flask_restful import Resource, abort
from flask_restful.reqparse import Argument

from repositories import CustomerRepository
from utils.errors import DataNotFound
from utils.parse_params import parse_params


class CustomerResource(Resource):
    """ methods relative to the customer """

    @staticmethod
    @parse_params(
        Argument("username", location="json",
                 help="The username of the customer."),
        Argument("first_name", location="json",
                 help="The first_name of the customer."),
        Argument("last_name", location="json",
                 help="The last_name of the customer."),
        Argument("email", location="json",
                 help="The email of the customer."),
        Argument("phone", location="json",
                 help="The phone number of the customer."),
        Argument("country", location="json",
                 help="The country of the customer."),
        Argument("state", location="json",
                 help="The state of the customer."),
        Argument("city", location="json",
                 help="The city of the customer."),
        Argument("street_name", location="json",
                 help="The street_name of the customer."),
        Argument("zipcode", location="json",
                 help="The zipcode of the customer.")
    )
    @swag_from("../swagger/customer/create.yml")
    def create(**args):
        """ Create an customer based on the sent information """

        customer = CustomerRepository().create(**args)

        data = request.get_json()

        if not data:
            return jsonify({"error": "No data provided."}), 400

        if 'username' in data:
            customer.username = data['username']

        if 'first_name' in data:
            customer.first_name = data['first_name']

        if 'last_name' in data:
            customer.last_name = data['last_name']

        if 'email' in data:
            customer.email = data['email']
        
        if 'phone' in data:
            customer.phone = data['phone']

        if 'country' in data:
            customer.country = data['country']

        if 'state' in data:
            customer.state = data['state']

        if 'city' in data:
            customer.city = data['city']
        
        if 'street_name' in data:
            customer.street_name = data['street_name']

        if 'zipcode' in data:
            customer.zipcode = data['zipcode']

        customer.save()

        return jsonify({"Message": f"Customer was created successfully"})

    @staticmethod
    @swag_from("../swagger/customer/read_one.yml")
    def read_one(customer_id):
        """ Return a customer key information based on their id """

        try:
            customer = CustomerRepository().read_one(customer_id=customer_id)

            if not customer:
                return jsonify({"Message": f"Customer with the id {customer_id} not found"}), 404

            customer_data = jsonify({
                "Username": customer.username,
                "First Name": customer.first_name,
                "Last Name": customer.last_name,
                "Email Address": customer.email,
                "Phone Number": customer.phone,
                "Country": customer.country,
                "State": customer.state,
                "City": customer.city,
                "Street Name": customer.street_name,
                "Zipcode": customer.zipcode
            })

            return jsonify({
                "Message": f"Customer with id {customer_id} was retrieved successfully",

                "Customer": customer_data.json
                }), 200
        except DataNotFound as e:
            abort(404, e.message)
        except Exception:
            abort(500)

    @staticmethod
    @swag_from("../swagger/customer/read_all.yml")
    def read_all():
        """ Return customers key information based """
        customers = CustomerRepository().read_all()

        customers_data = []

        for x in customers:
            customers_data.append({
                "Username": x.username,
                "First Name": x.first_name,
                "Last Name": x.last_name,
                "Email Address": x.email,
                "Phone Number": x.phone,
                "Country": x.country,
                "State": x.state,
                "City": x.city,
                "Street Name": x.street_name,
                "Zipcode": x.zipcode
            })

        return jsonify({
            "Message": f"Customers list was succesfully retrieved",

            "Customers": customers_data
            }), 200

    @staticmethod
    @parse_params(
        Argument("first_name", location="json",
                 help="The first_name of the customer."),
        Argument("last_name", location="json",
                 help="The last_name of the customer."),
        Argument("email", location="json",
                 help="The email of the customer.")
    )
    @swag_from("../swagger/customer/update.yml")
    def update(customer_id, **args):
        """ Update an customer based on the sent information """
        customer = CustomerRepository().update(customer_id=customer_id, **args)

        if not customer:
            return jsonify({f"Customer with id {customer_id} not found"}), 404

        data = request.get_json()

        if not data:
            return jsonify({"error": "No data provided."}), 400

        if 'first_name' in data:
            customer.first_name = data['first_name']

        if 'last_name' in data:
            customer.last_name = data['last_name']

        if 'email' in data:
            customer.email = data['email']

        customer.save()

        return jsonify({"Message": f"Customer with user id {customer_id} was updated successfully"}), 200

    @staticmethod
    @swag_from("../swagger/customer/delete.yml")
    def delete(customer_id):
        """ Delete an customer based on the sent information """
        customer = CustomerRepository().delete(customer_id=customer_id)
        customer.delete()

        return jsonify({"Message": f"Customer with id {customer_id} was deleted successfully"}), 200
