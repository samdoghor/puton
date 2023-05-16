from datetime import datetime
from models import db


class Session(db.Model):
    """ The model defines the sessions of the user """
    __tablename__ = "sessions"

    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.DateTime, default=datetime.now())
    started_session_at = db.Column(db.DateTime, default=datetime.now())
    closed_session_at = db.Column(db.DateTime, default=datetime.now())

    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(
        db.DateTime, default=datetime.now(), onupdate=datetime.now())
