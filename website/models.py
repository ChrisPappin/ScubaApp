from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

#class Summary(db.Model):
    #userID = db.Column(db.Integer, db.ForeignKey('user.id')) #One to one relationship, needed?
    #totalDives = db.Column(db.String(150))
    #uniqueLoc = db.Column(db.String(150))
    #totalTime = db.Column(db.String(150))

    #Auto add datetime:
    #date = db.Column(db.DateTime(timezone=True), default=)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    #summary = db.relationship('Summary')
    totalDives = db.Column(db.String(150))
    uniqueLoc = db.Column(db.String(150))
    totalTime = db.Column(db.String(150))
