""" Defines the Customer repository """
import sys

from flask import jsonify
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError

from models import Customer
from utils.errors import DataNotFound, DuplicateData, InternalServerError


class CustomerRepository:
    """ The repository for the customer model """

    @staticmethod
    def create(username, first_name, last_name, email, password, phone=None, country=None,
               state=None, city=None, street_name=None, zipcode=None):
        """ Create a new customer """
        try:
            new_customer = Customer(username=username, first_name=first_name, last_name=last_name, email=email, phone=phone, country=country, state=state, city=city, street_name=street_name, zipcode=zipcode)
            new_customer.set_password(password)

            customer = new_customer.save() 

            return jsonify({
                "First Name": customer.first_name,
                "Last Name": customer.last_name,
            })
        
        except IntegrityError as e:
            message = e.orig.diag.message_detail
            raise DuplicateData(message)
        except Exception:
            raise InternalServerError
    
    @staticmethod
    def get_all():
        """ Query all customers"""
        customers = Customer.query.all()
        if not customers:
            return []
        data = []
        for cus in customers:
            data.append({
                "id": cus.id,
                "username": cus.username,
                "first_name": cus.first_name,
                "last_name": cus.last_name,
                "email": cus.email,
                "phone": cus.phone,
                "country": cus.country,
                "state": cus.state,
                "city": cus.city,
                "street_name": cus.street_name,
                "zipcode": cus.zipcode,
            })

        return data

    @staticmethod
    def get_one(customer_id=None, username=None, email=None):
        """ Query a customer by customer_id """

        # make sure one of the parameters was passed
        if not customer_id and not username and not email:
            raise DataNotFound(f"Customer not found, no detail provided")

        try:
            query = Customer.query
            if customer_id:
                query = query.filter(Customer.id == customer_id)
            if username:
                query = query.filter(or_(Customer.username == username, Customer.email == username))
            if email:
                query = query.filter(or_(Customer.email == email, Customer.username == email))

            customer = query.first()
            return customer
        except:
            print(sys.exc_info())
            raise DataNotFound(f"Customer with {customer_id} not found")

    def update(self, customer_id, **args):
        """ Update a customer's age """
        customer = self.get(customer_id)
        if 'phone' in args and args['phone'] is not None:
            customer.phone = args['phone']

        if 'last_name' in args and args['last_name'] is not None:
            customer.last_name = args['last_name']

        if 'first_name' in args and args['first_name'] is not None:
            customer.first_name = args['first_name']

        return customer.save()
    
    @staticmethod
    def delete(customer_id):
        """ Delete a customer by id """
        if not customer_id:
            raise DataNotFound(f"Store not found")
        try:
            query = Customer.query.filter(Customer.id == customer_id).first()
            if not query:
                raise DataNotFound(f"Customer Detail with {customer_id} not found")
            return query.delete()
        except DataNotFound as e:
            print(sys.exc_info())
            raise DataNotFound(f"Customer with {customer_id} not found")
