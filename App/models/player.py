from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()
import datetime


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name= db.Column(db.String(80), nullable=False)
    second_name= db.Column(db.String(80), nullable=False)
    assists= db.Column(db.Integer, nullable=False)
    clean_sheets= db.Column(db.Integer, nullable=False)
    form= db.Column(db.Integer, nullable=False)
    goals_conceded= db.Column(db.Integer, nullable=False)
    goals_scored= db.Column(db.Integer, nullable=False)
    minutes= db.Column(db.Integer, nullable=False)
    penalties_saved= db.Column(db.Integer, nullable=False)
    red_cards= db.Column(db.Integer, nullable=False)
    saves= db.Column(db.Integer, nullable=True)
    yellow_cards= db.Column(db.Integer, nullable=False)


    def toDict(self):
      return {
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