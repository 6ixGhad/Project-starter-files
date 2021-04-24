from flask import redirect, render_template, request, flash, session, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, EqualTo, Email
from wtforms.fields.html5 import EmailField
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
db=SQLAlchemy()


from App.models import ( User, Player, Collection )


def create_user(firstname, lastname, uwi_id, email, gender, dob):
    # newuser = use()
    return 'new user'


class SignUp(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    email = EmailField('email', validators=[Email(), InputRequired()])
    password = PasswordField('New Password', validators=[InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password')
    submit = SubmitField('Sign Up', render_kw={'class': 'btn waves-effect waves-light white-text'})

class LogIn(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login', render_kw={'class': 'btn waves-effect waves-light white-text'})

class AddPlayer(FlaskForm):
  id = TextAreaField('Player ID', validators =[InputRequired()])
  first_name = TextAreaField('First Name', validators =[InputRequired()])
  second_name = TextAreaField('Last Name', validators =[InputRequired()])
  assists = TextAreaField('Assists', validators =[InputRequired()])
  clean_sheets = TextAreaField('Clean Sheets', validators =[InputRequired()])
  form = TextAreaField('Form', validators =[InputRequired()])
  goals_conceded = TextAreaField('Goals Conceded', validators =[InputRequired()])
  goals_scored = TextAreaField('Goals Scored', validators =[InputRequired()])
  minutes = TextAreaField('Minutes', validators =[InputRequired()])
  penalties_saved = TextAreaField('Penalties Saved', validators =[InputRequired()])
  red_cards = TextAreaField('Red Cards', validators =[InputRequired()])
  saves = TextAreaField('Saves', validators =[InputRequired()])
  yellow_cards = TextAreaField('Yellow Cards', validators =[InputRequired()])

  submit = SubmitField('Add Player', render_kw={'class': 'btn waves-effect waves-light white-text'})

class edit(FlaskForm):
  assists = TextAreaField('Assists', validators =[InputRequired()])
  clean_sheets = TextAreaField('Clean Sheets', validators =[InputRequired()])
  form = TextAreaField('Form', validators =[InputRequired()])
  goals_conceded = TextAreaField('Goals Conceded', validators =[InputRequired()])
  goals_scored = TextAreaField('Goals Scored', validators =[InputRequired()])
  minutes = TextAreaField('Minutes', validators =[InputRequired()])
  penalties_saved = TextAreaField('Penalties Saved', validators =[InputRequired()])
  red_cards = TextAreaField('Red Cards', validators =[InputRequired()])
  saves = TextAreaField('Saves', validators =[InputRequired()])
  yellow_cards = TextAreaField('Yellow Cards', validators =[InputRequired()])

  submit = SubmitField('Update', render_kw={'class': 'btn waves-effect waves-light white-text'})

def signupAction():
  form = SignUp() # create form object
  if form.validate_on_submit():
    data = request.form # get data from form submission
    newuser = User(username=data['username'], email=data['email']) # create user object
    newuser.set_password(data['password']) # set password
    db.session.add(newuser) # save new user
    db.session.commit()
    flash('Account Created!')# send message
    return redirect(url_for('api_views.index'))# redirect to login page
  flash('Error invalid input!')
  return redirect(url_for('api_views.signup')) 

def loginAction():
  form = LogIn()
  if form.validate_on_submit(): # respond to form submission
      data = request.form
      user = User.query.filter_by(username = data['username']).first()
      if user and user.check_password(data['password']): # check credentials
        flash('Logged in successfully.') # send message to next page
        login_user(user) # login the user
        return redirect(url_for('api_views.get_api_docs')) # redirect to main page if login successful
  flash('Invalid credentials')
  return redirect(url_for('api_views.index'))

def logout():
  logout_user()
  flash('Logged Out!')
  return redirect(url_for('api_views.index'))

def addplayerAction():
  form = AddPlayer()
  if form.validate_on_submit():
    data = request.form # get request data
    allPlayers= Player(id=data['id'], first_name=data['first_name'], second_name=data['second_name'], assists=data['assists'], clean_sheets=data['clean_sheets'], form=data['form'], goals_conceded=data['goals_conceded'], goals_scored=data['goals_scored'] ,minutes=data['minutes'],penalties_saved=data['penalties_saved'],red_cards=data['red_cards'],yellow_cards=data['yellow_cards'])
    db.session.add(allPlayers)
    db.session.commit()
    flash('Player Created!') # send message
    return redirect(url_for('api_views.get_players1')) # redirect
  flash('Invalid data!')
  return redirect(url_for('api_views.get_players1')) # redirect

def get_players():
   players = Player.query.all()
   if players is None:
       players = []
   form = AddPlayer()
   return render_template('players.html', form=form, players=players) # pass the form and the user's todo objects to the template

def add_to_action(id):
  count = 1
  search = id
  row = Player.query.filter_by(id=search).first() # query  players
  #myCollection= Collection(id=count, first_name=row.first_name, second_name=row.second_name)
  myCollection= Collection(id=id, collectionid= current_user.id, first_name=row.first_name, second_name=row.second_name, assists=row.assists, clean_sheets=row.clean_sheets, form=row.form, goals_conceded=row.goals_conceded, goals_scored=row.goals_scored ,minutes=row.minutes,penalties_saved=row.penalties_saved,red_cards=row.red_cards,yellow_cards=row.yellow_cards)
  db.session.add(myCollection)
  db.session.commit()
  count += 1
  flash('Collection Updated!')
  return redirect(url_for('api_views.get_collection1'))

def get_collection():
  collections = Collection.query.filter_by(collectionid=current_user.id).all()
  if collections is None:
      collections = []
  form = AddPlayer()
  return render_template('collection.html', players=collections) 

def edit_action(id):
  form = edit()
  if form.validate_on_submit():
    data = request.form
    collection = Collection.query.filter_by(id=id).first() 
    collection.assists = data['assists'] # update text
    #player.assists = '0' # update text
    collection.clean_sheets = data['clean_sheets'] # update text
    collection.form = data['form'] # update text
    collection.goals_conceded = data['goals_conceded'] # update text
    collection.goals_scored = data['goals_scored'] # update text
    collection.minutes = data['minutes'] # update text
    collection.penalties_saved = data['penalties_saved'] # update text
    collection.red_cards = data['red_cards'] # update text
    collection.saves = data['saves'] # update text
    collection.yellow_cards = data['yellow_cards'] # update text
    local_object = db.session.merge(collection)
    db.session.add(local_object) 
    db.session.commit()
    flash('Player Updated!')
    return redirect(url_for('api_views.get_players1'))
  flash('Invalid data')
  return redirect(url_for('api_views.get_players1'))

def delete_item(id):
  collection = Collection.query.filter_by(id=id).first() # query  todo
  if collection:
    local_object = db.session.merge(collection)
    db.session.delete(local_object)
    db.session.commit()
    flash('Player removed from collection!')
    return redirect(url_for('api_views.get_collection1'))
  flash('Unauthorized or player not found')
  return redirect(url_for('api_views.get_collection1')) 