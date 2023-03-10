"""
Define the resources for the Customer
"""
# imports
from flask import abort, jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import CustomerRepository
from utils.errors import DataNotFound


class CustomerResource(Resource):
  """ methods relative to the customer """

  def create(first_name, last_name):
    """ Create a customer based on the provided information """
    # Check duplicates
    customer = CustomerRepository.create(first_name=first_name, last_name=last_name)
    return jsonify({"data": customer.json})
  
  @staticmethod
  def get_all():
    customers = CustomerRepository.get_all()
    return jsonify({"data": customers})

  @staticmethod
  def get_one(customer_id):
      """ Return a customer key information based on customer_id """

      try:
          customer = CustomerRepository.get_one(customer_id=customer_id)
          if not customer:
              return jsonify({"message": f" customer with the id {customer_id} not found"})
          data = {
              "id": customer.id,
              "username": customer.username,
              "first_name": customer.first_name,
              "last_name": customer.last_name,
              "email": customer.email,
              "phone": customer.phone,
              "country": customer.country,
              "state": customer.state,
              "city": customer.city,
              "street_name": customer.street_name,
              "zipcode": customer.zipcode,
          }
          return jsonify({"data": data})
      except DataNotFound as e:
          abort(404, e.message)
      except Exception:
          abort(500)
 
  def update(customer_id, last_name, first_name, age):
    """ Update a customer based on the provided information """
    repository = CustomerRepository()
    customer = repository.update(customer_id=customer_id, last_name=last_name, first_name=first_name, age=age)
    return jsonify({"data": customer.json})

  def delete(customer_id):
    """ delete a Customer via the provided id """
    CustomerRepository.delete(customer_id=customer_id)
    return jsonify({"message": "Customer was successfully deleted"})