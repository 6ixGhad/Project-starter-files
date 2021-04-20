from flask import Blueprint, redirect, render_template, request

api_views = Blueprint('api_views', __name__, template_folder='../templates')
from App.controllers import ( create_user, SignUp )
@api_views.route('/', methods=['GET'])
def get_api_docs():
    return render_template('index.html')

@app_views.route('/signup', methods=['GET'])
def signup():
  form = SignUp() # create form object
  return render_template('signup.html', form=form) # pass form object to template