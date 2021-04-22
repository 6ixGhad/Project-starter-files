from flask import Blueprint, redirect, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, EqualTo, Email
from wtforms.fields.html5 import EmailField
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, login_user, login_required
import logging

api_views = Blueprint('api_views', __name__, template_folder='../templates')
from App.controllers import ( create_user, SignUp, signupAction, LogIn, loginAction, logout, AddPlayer, addplayerAction, get_players, add_to_action, get_collection )


@api_views.route('/status', methods=['GET'])
@login_required
def get_api_docs():
    return render_template('index.html')

@api_views.route('/signup', methods=['GET'])
def signup():
  form = SignUp() # create form object
  return render_template('signup.html',  form=form) # pass form object to template

#@api_views.route('/')
#def index():
#  return render_template('login.html')

@api_views.route('/', methods=['GET'])
def index():
  form = LogIn()
  return render_template('login.html', form=form)

@api_views.route('/login', methods=['POST'])
def loginAction1():
  result = loginAction()
  return result

@api_views.route('/signup', methods=['POST'])
def signupAction1():
  result = signupAction()
  return result

@api_views.route('/logout', methods=['GET'])
@login_required
def logout1():
  result = logout()
  return result 

@api_views.route('/addplayer', methods=['GET'])
@login_required
def addplayer():
  form = AddPlayer() # get the addToDo form
  return render_template('addplayer.html', form=form) # pass the form to the template

@api_views.route('/addplayer', methods=['POST'])
@login_required
def addplayerAction1():
  result = addplayerAction()
  return result # redirect

@api_views.route('/players', methods=['GET', 'POST'])
@login_required
def get_players1():
   result = get_players()
   return result

@api_views.route('/addtocollection/<id>')
@login_required
def add_to_action1(id):
  search = id
  result = add_to_action(search)
  return result

@api_views.route('/mycollection', methods=['GET', 'POST'])
@login_required
def get_collection1():
   result = get_collection()
   return result