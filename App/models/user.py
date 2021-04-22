from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()
import datetime


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    #todos = db.relationship('Todo', backref='user', lazy=True) # sets up a relationship to todos which references User

    def toDict(self):
      return {
        "id": self.id,
        "username": self.username,
        "email": self.email,
        "password": self.password
      }
    
    #hashes the password parameter and stores it in the object
    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    #Returns true if the parameter is equal to the object's password property
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
    
    #To String method
    def __repr__(self):
        return '<User {}>'.format(self.username) 

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name= db.Column(db.String(80), nullable=False)
    second_name= db.Column(db.String(80), nullable=False)
    assists= db.Column(db.Integer, nullable=False)
    clean_sheets= db.Column(db.Integer, nullable=False)
    form= db.Column(db.Integer, nullable=True)
    goals_conceded= db.Column(db.Integer, nullable=False)
    goals_scored= db.Column(db.Integer, nullable=False)
    minutes= db.Column(db.Integer, nullable=False)
    penalties_saved= db.Column(db.Integer, nullable=False)
    red_cards= db.Column(db.Integer, nullable=False)
    saves= db.Column(db.Integer, nullable=True)
    yellow_cards= db.Column(db.Integer, nullable=False)


    def toDict(self):
      return {
        "id": self.id,
        "first_name": self.first_name,
        "second_name": self.second_name,
        "assists": self.assists,
        "clean_sheets": self.clean_sheets,
        "form": self.form,
        "goals_conceded": self.goals_conceded,
        "goals_scored": self.goals_scored,
        "minutes": self.minutes,
        "penalties_saved": self.penalties_saved,
        "red_cards": self.red_cards,
        "yellow_cards": self.yellow_cards
      }