from flask import redirect, render_template, request, session, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, EqualTo, Email
from wtforms.fields.html5 import EmailField
from flask_sqlalchemy import SQLAlchemy
#db=SQLAlchemy()
from App.models import db


from App.models import ( User )

def create_user(firstname, lastname, uwi_id, email, gender, dob):
    # newuser = use()
    return 'new user'




def signupAction():
  form = SignUp() # create form object
  if form.validate_on_submit():
   data = request.json # get data from form submission
   newuser = User(first_name=data['username'], last_name=data['username']) # create user object
    #newuser.set_password(data['password']) # set password
   db.session.add(newuser) # save new user
   db.session.commit()
    #flash('Account Created!')# send message
    #return redirect(url_for('index'))# redirect to login page
  #flash('Error invalid input!')
  #return redirect(url_for('signup')) 