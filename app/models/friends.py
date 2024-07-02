from .db import db, environment, SCHEMA


class Friend(db.Model):
    __tablename__='friends'

    if environment == "production":
        __table_args__ = { 'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key = True)
    friendId = db.Column(db.Integer, nullable = False)
    status = db.Column(db.String(100))
    name = db.Column(db.String(40))

    def to_dict(self):
        friend = {
            "id": self.id,
            "friendId": self.friendId,
            "status": self.status,
            "name": self.name
        }

        return friend
