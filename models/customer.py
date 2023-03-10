"""
Define the Custommer model
"""
# imports
from datetime import datetime

from werkzeug.security import check_password_hash, generate_password_hash

from . import db


class Customer(db.Model):

    """ The Customer model """

    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    first_name = db.Column(db.String(300))
    last_name = db.Column(db.String(300))
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.Text(), nullable=False)
    phone = db.Column(db.String(15))
    country = db.Column(db.String(50))
    state = db.Column(db.String(70))
    city = db.Column(db.String(50))
    street_name = db.Column(db.String(50))
    zipcode = db.Column(db.String(50))
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)