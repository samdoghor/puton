""" Defines the Customer repository """

from models import Customer
from utils.errors import DataNotFound


class CustomerRepository:
    """ The repository for the customer model """

    def create(self, **args):
        """ Create a new customer """
        customer = Customer(username=args['username'], first_name=args['first_name'], last_name=args['last_name'], email=args['email'], phone=args['phone'], country=args['country'], state=args['state'], city=args['city'], street_name=args['street_name'], zipcode=args['zipcode'])
        customer.set_password('')

        return customer

    def read_one(self, customer_id):
        """ Query a customer by id """

        if customer_id is None:
             raise DataNotFound(f"Customer not found, no detail provided")
        
        try:
            customer = Customer.query.filter_by(id=customer_id).first()
            return customer
        except:
            raise DataNotFound(f"Customer with {customer_id} not found")

    def read_all(self):
        """ Query all customer """
        customers = Customer.query.all()

        return customers

    def update(self, customer_id, **args):
        """ Update a customer details """
        customer = Customer.query.filter_by(id=customer_id).first()

        return customer

    def delete(self, customer_id):
        """ Delete a customer """
        customer = Customer.query.filter_by(id=customer_id).first()

        return customer