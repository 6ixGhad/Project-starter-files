import os
from flask import Flask
from flask_jwt import JWT
from datetime import timedelta 
from flask_uploads import UploadSet, configure_uploads, IMAGES, TEXT, DOCUMENTS
from flask_login import LoginManager, current_user, login_user, login_required
from App.models import ( User )
from App.models import db

from App.views import (
    api_views,
    user_views
)

''' Begin Flask Login Functions '''
login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

''' End Flask Login Functions '''

def initDB():
    #db.drop_all(app=app)
    db.create_all(app=app)
    print('database initialized!')

def get_db_uri(scheme='sqlite://', user='', password='', host='//demo.db', port='', name=''):
    return scheme+'://'+user+':'+password+'@'+host+':'+port+'/'+name 

def loadConfig(app):
    #try to load config from file, if fails then try to load from environment
    try:
        app.config.from_object('App.config')
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://kosnujrrfaxywn:57eace331afddfae8f69fc0f27c255ef46c4d7cd6a6401d1634236cff693d22a@ec2-34-206-8-52.compute-1.amazonaws.com:5432/de4ru3u11bk7qo' if app.config['SQLITEDB'] else app.config['DBURI']
    except:
        print("config file not present using environment variables")
        # DBUSER = os.environ.get("DBUSER")
        # DBPASSWORD = os.environ.get("DBPASSWORD")
        # DBHOST = os.environ.get("DBHOST")
        # DBPORT = os.environ.get("DBPORT")
        # DBNAME = os.environ.get("DBNAME")
        DBURI = os.environ.get("DBURI")
        SQLITEDB = os.environ.get("SQLITEDB", default="true")
        app.config['ENV'] = os.environ.get("ENV")
        app.config['SQLALCHEMY_DATABASE_URI'] = get_db_uri() if SQLITEDB in {'True', 'true', 'TRUE'} else DBURI
        app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

def create_app():
    app = Flask(__name__, static_url_path='/static')
    loadConfig(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['PREFERRED_URL_SCHEME'] = 'https'
    app.config['UPLOADED_PHOTOS_DEST'] = "App/uploads"
    photos = UploadSet('photos', TEXT + DOCUMENTS + IMAGES)
    configure_uploads(app, photos)
    db.init_app(app)
    login_manager.init_app(app)
    return app

app = create_app()

app.app_context().push()

app.register_blueprint(api_views)
app.register_blueprint(user_views)
initDB()

''' Set up JWT here (if using flask JWT)'''
# def authenticate(uname, password):
#   pass

# #Payload is a dictionary which is passed to the function by Flask JWT
# def identity(payload):
#   pass

# jwt = JWT(app, authenticate, identity)
''' End JWT Setup '''