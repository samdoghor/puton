""" Defines the Customer repository """

import os
from flask import jsonify
from models import Customer


class CustomerRepository:
    """ The repository for the customer model """

    def create(username, first_name, last_name, email, phone, country, state, city, street_name, zipcode):
        """ Create a new customer """
        customer = Customer(username=username, first_name=first_name, last_name=last_name, email=email, phone=phone, country=country, state=state, city=city, street_name=street_name, zipcode=zipcode)
        customer.set_password('')

        return customer.save()

    @staticmethod
    def read_one(customer_id):
        """ Query a customer by id """
        customer = Customer.query.filter_by(id=customer_id).first()

        return customer

    @staticmethod
    def read_all():
        """ Query all customer """
        customers = Customer.query.all()

        return customers

    def update(customer_id, **args):
        """ Update a customer details """
        customer = Customer.query.filter_by(id=customer_id).first()

        return customer.update()

    def delete(customer_id):
        """ Delete a customer """
        customer = Customer.query.filter_by(id=customer_id).first()

        return customer.delete()