from flask_login import UserMixin
from app import db


class User(db.Model, UserMixin):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=True)
    password = db.Column(db.String(30), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    phone = db.Column(db.String(11))

    def __init__(self, username, password, email, phone):
        self.username = username
        self.email = email
        self.password = password
        self.phone = phone

    def __repr__(self):
        return '<User %r>' % self.username
