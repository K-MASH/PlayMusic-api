from flask import Blueprint, request, json, jsonify, abort
from .utils_blueprint import flask_construct_response, flask_constructor_error
import MySQLdb
from ..api_db import users_db
USERS_API_BLUEPRINT = Blueprint(u'users_api', __name__)


@USERS_API_BLUEPRINT.route(u'/<string:username>', methods = [u'GET'])
def get_basic_information_user(username):
    result = users_db.get_basic_information(username)
    print "user passed on url: {}".format(result)

"""
Help to retrieve all user's playlists
""" 
@USERS_API_BLUEPRINT.route(u'/<string:username>/playlists', methods = [u'GET'])
def get_user_playlists(username):
    print "user passed on url: {}".format(username)