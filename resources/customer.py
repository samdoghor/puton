"""
Define the resources for the Customer
"""
# imports
from flask import Blueprint, Response, jsonify
from flask_restful import Resource

from repositories import CustomerRepository


class CustomerResource(Resource):
  def create():
    pass
    return 
  
  def get_all():
    customers = CustomerRepository.get_all()
    return jsonify({"data": customers})

  def get_one():
    pass
    return
 
  def update():
    pass
    return

  def delete():
    pass
    return