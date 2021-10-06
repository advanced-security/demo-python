
from server.webapp import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=False, nullable=False)
    author = db.Column(db.String(128), unique=False, nullable=False)

    read = db.Column(db.Boolean(), unique=False, nullable=False)
