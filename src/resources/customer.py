"""
Define the resources for the Customer
"""
from flask import jsonify, request
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import CustomerRepository
from utils.parse_params import parse_params


class CustomerResource(Resource):
    """ methods relative to the customer """

    @staticmethod
#   @swag_from("../swagger/customer/create.yml")
    def create(username, first_name, last_name, email, phone, country, state, city, street_name, zipcode):
        """ Create an customer based on the sent information """
        customer = CustomerRepository
        customer.create(username=username, first_name=first_name, last_name=last_name, email=email, phone=phone, country=country, state=state, city=city, street_name=street_name, zipcode=zipcode)

        return jsonify({"Message": f"Customer was created successfully",
                        
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

    @staticmethod
#   @swag_from("../swagger/customer/read_one.yml")
    def read_one(customer_id):
        """ Return a customer key information based on their id """
        customer = CustomerRepository.read_one(customer_id=customer_id)

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
            })

    @staticmethod
#   @swag_from("../swagger/customer/read_all.yml")
    def read_all():
        """ Return customers key information based """
        customers = CustomerRepository.read_all()

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
            })

    @staticmethod
#   @swag_from("../swagger/customer/update.yml")
    def update(customer_id, **args):
        """ Update an customer based on the sent information """
        customer = CustomerRepository
        customer.update(customer_id=customer_id)

        return jsonify({"Message": f"Customer with user id {customer_id} was updated successfully"})

    @staticmethod
#   @swag_from("../swagger/customer/delete.yml")
    def delete(customer_id):
        """ Delete an customer based on the sent information """
        customer = CustomerRepository
        customer.delete(customer_id=customer_id)

        return jsonify({"Message": f"Customer with id {customer_id} was deleted successfully"})
