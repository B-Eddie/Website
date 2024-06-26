from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, TextAreaField, RadioField, FileField
from wtforms.validators import DataRequired


class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(320), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)
    location = db.Column(db.String(200), nullable=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __init__(self, username, password, email, phone_number, location):
        self.username = username
        self.set_password(password)
        self.email = email
        self.phone_number = phone_number
        self.location = location


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    details = db.Column(db.String(1000), nullable=True)
    picture = db.Column(db.String(255), nullable=True)
    pickup_location = db.Column(db.String(200), nullable=False)
    contact_info = db.Column(db.String(300), nullable=False)
    rad_type = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    blue = db.Column(db.Integer, nullable=True)

class ProductsService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    details = db.Column(db.String(1000), nullable=True)
    picture = db.Column(db.String(255), nullable=True)
    pickup_location = db.Column(db.String(200), nullable=False)
    contact_info = db.Column(db.String(300), nullable=False)
    rad_type = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    blue = db.Column(db.Integer, nullable=True)


class lost_and_found(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    picture = db.Column(db.String(5000), nullable=False)
    details = db.Column(db.String(500), nullable=False)
    pickup_location = db.Column(db.String(200), nullable=False)
    contact_info = db.Column(db.String(300), nullable=False)
    bounty = db.Column(db.Integer, nullable=True)
