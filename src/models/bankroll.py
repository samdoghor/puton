from datetime import datetime
from models import db


class BankRoll(db.Model):
    """ The model defines the financial management of the user """
    __tablename__ = "bankrolls"

    id = db.Column(db.Integer, primary_key=True)
    capital = db.Column(db.Float)
    profits = db.Column(db.Float)
    losses = db.Column(db.Float)
    balance = db.Column(db.Float)
    loss_limit = db.Column(db.Float)

    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(
        db.DateTime, default=datetime.now(), onupdate=datetime.now())
