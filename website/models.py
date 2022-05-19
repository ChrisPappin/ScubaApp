from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Summary(db.Model):
    id = db.Columnn(db.Integer, primary_key=True)
    totalDives = db.Column(db.String(150))
    uniqueLoc = db.Column(db.String(150))
    totalTime = db.Column(db.String(150))
    

    #Auto add datetime:
    #date = db.Column(db.DateTime(timezone=True), default=)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
