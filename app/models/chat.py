from .db import db, environment, SCHEMA


class Chat(db.Model):
    __tablename__='chats'

    if environment == "production":
        __table_args__ = { 'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key = True)
    friendId = db.Column(db.Integer, nullable = False)
