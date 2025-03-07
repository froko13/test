from runner import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, unique = True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique = True)
    password = db.Column(db.String(100), nullable=False)
    balance = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, nullable=False)
    is_confirmed =  db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Project {self.name}>'