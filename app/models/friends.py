from .db import db, environment, SCHEMA


class Friend(db.Model):
    __tablename__='friends'

    if environment == "production":
        __table_args__ = { 'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key = True)
    profilePic = db.Column(db.String)
