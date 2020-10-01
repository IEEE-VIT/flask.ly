from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

class User(db.Model):
    # Create the User model which stores their email ID and password
    id = db.Column(db.Integer , primary_key = True)
    email_id  = db.Column(db.String(200), nullable = False , unique = True)
    password =  db.Column(db.String(50), nullable = False)

class Url:
    # Create the url model which stores the original url as well as the shortened url
    pass
