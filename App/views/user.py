from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory

user_views = Blueprint('user_views', __name__, template_folder='../templates')

from App.models import User
from App.controllers import ( create_user, SignUp, signupAction )

@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = User.query.all()
    return render_template('users.html', users=users)

@user_views.route('/register', methods=['GET'])
def signupp():
  #form = SignUp() # create form object
  return render_template('signup.html') # pass form object to template

@user_views.route('/register', methods=['POST'])
def signupAction2():
  signupAction()
  return 'Created'

@user_views.route('/api/users')
def client_app():
    users = User.query.all()
    if not users:
        return jsonify([])
    users = [user.toDict() for user in users]
    return jsonify(users)

@user_views.route('/static/users')
def static_user_page():
  return send_from_directory('static', 'static-user.html')