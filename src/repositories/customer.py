""" Defines the Customer repository """
import sys

from flask import jsonify
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError

from models import Customer


class CustomerRepository:
    """ The repository for the customer model """

    @staticmethod
    def create(username, first_name, last_name, email, password, phone, country, state, city, street_name, zipcode):
        """ Create a new customer """
        customer = Customer(username=username, first_name=first_name, last_name=last_name, email=email, phone=phone, country=country, state=state, city=city, street_name=street_name, zipcode=zipcode)
        customer.set_password(password)

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

    def update(self, id, **args):
        """ Update a user's details """
        customer = self.get(id)
        customer.age = args

        return customer.update()

    def delete(self, id):
        """ Delete a user """
        customer = self.get(id)

        return customer.delete()


