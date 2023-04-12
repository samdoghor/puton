"""
Define the resources for the Customer
"""
from flasgger import swag_from
from flask import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import CustomerRepository
from utils.parse_params import parse_params


class CustomerResource(Resource):
  """ methods relative to the customer """

  @staticmethod
  @parse_params(
      Argument("last_name", location="json", required=True, help="The last name of the customer."),
      Argument("first_name", location="json", required=True, help="The first name of the customer.")
  )
#   @swag_from("../swagger/customer/create.yml")
  def create(last_name, first_name):
      """ Create an customer based on the sent information """
      customer = CustomerRepository.create(last_name=last_name, first_name=first_name)

      return jsonify({"customer": customer.json})

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

      return jsonify({"Customer": customer_data.json})

  @staticmethod
#   @swag_from("../swagger/customer/read_all.yml")
  def read_all():
      """ Return customers key information based """
      customers = CustomerRepository.read_all()

      customers_data = []
      
      for  x in customers:
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

      return jsonify({"Customers": customers_data})


  @staticmethod
  @parse_params(
      Argument("age", location="json", required=True, help="The age of the user.")
  )
#   @swag_from("../swagger/customer/update.yml")
  def update(id, **args):
      """ Update an customer based on the sent information """
      repository = CustomerRepository()
      customer = repository.update(id=id)

      return jsonify({"customer": customer.json})
  
  @staticmethod
  @parse_params(
      Argument("age", location="json", required=True, help="The age of the user.")
  )
#   @swag_from("../swagger/customer/delete.yml")
  def delete(id):
      """ Update an customer based on the sent information """
      repository = CustomerRepository()
      customer = repository.delete(id=id)

      return jsonify({"customer": customer.json})