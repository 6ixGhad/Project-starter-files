from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory

user_views = Blueprint('user_views', __name__, template_folder='../templates')

from App.models import User, Player, Collection
from App.controllers import ( create_user,  )

@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = User.query.all()
    return render_template('users.html', users=users)

@user_views.route('/api/users')
def client_app():
    users = User.query.all()
    if not users:
        return jsonify([])
    users = [user.toDict() for user in users]
    return jsonify(users)

@user_views.route('/api/players')
def get_players():
    players = Collection.query.all()
    if not players:
        return jsonify([])
    players = [player.toDict() for player in players]
    return jsonify(players)

@user_views.route('/static/users')
def static_user_page():
  return send_from_directory('static', 'static-user.html')