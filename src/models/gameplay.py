from datetime import datetime
from models import db


class GamePlay(db.Model):
    """ The model defines the financial management of the user """
    __tablename__ = "gameplays"

    id = db.Column(db.Integer, primary_key=True)
    stake = db.Column(db.Float)
    target = db.Column(db.Float)
    odd = db.Column(db.Float)
    status = db.Column(db.String())

    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(
        db.DateTime, default=datetime.now(), onupdate=datetime.now())
