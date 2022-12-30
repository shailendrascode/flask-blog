# apps.members.models
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Contact(db.Model):
    # sno,name,email,phone_num,message
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    phone_num = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(20), nullable=False)
    message = db.Column(db.String(120), nullable=False)


class Posts(db.Model):
    # sno,name,email,phone_num,message
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    content = db.Column(db.String(150), unique=True, nullable=False)
    date = db.Column(db.String(20), nullable=False)
    slug = db.Column(db.String(120), nullable=False)
    image_file = db.Column(db.String(120), nullable=False)
    subtitle = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)

