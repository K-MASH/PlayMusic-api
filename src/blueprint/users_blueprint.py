<<<<<<< HEAD
import src.requests as req
import logging
from flask import Blueprint, request, json
from .blueprint_utils import flask_construct_response
USERS_API_BLUEPRINT = Blueprint(u'users_api', __name__)

Users = [
	{
        "id" : 1,
        "name":"Names",
        "lastname": "Geo",
        "pseudo": "namesgeo",
        "email": "andressegeofried@gmail.com",
        "password": "qloif5fd!d",
        "status": 1,
        "birthday": "12/12/2012",
        "inscription_date": "14/10/2015",
        "gender": "M",
        "picture": "http://www.store.pic/001",
        "lang": "French",
        "country": "South-Africa",
        "city": "Le Cap",
        "address":"1, rue bloufontaine, 4521, Le cap"
    },
    {
        "id" : 2,
        "name":"Dimitry",
        "lastname": "Tatior",
        "pseudo": "dimtatiores",
        "email": "dimtatiores@gmail.com",
        "password": "qlqsoif5fd!d",
        "status": 2,
        "birthday": "12/12/2012",
        "inscription_date": "14/10/2015",
        "gender": "M",
        "picture": "http://www.store.pic/002",
        "lang": "French",
        "country": "South-Africa",
        "city": "Le Cap",
        "address":"1, rue bloufontaine, 4521, Le cap"
    }
 ]


"""
As her name indicates, this method allow to get all users in database
"""
@USERS_API_BLUEPRINT.route(u'/', methods=[u'GET'])
def get_all_users():
    #items = req.getAllUsers()
    return flask_construct_response({u'items':Users})


"""
As her name indicates, this method allow to get all users in database
"""
@USERS_API_BLUEPRINT.route(u'/me', methods=[u'GET'])
def get_me_as_user():
    #items = req.getAllUsers()
    return flask_construct_response({u'items':Users[0]})
=======
#coding: utf8
from flask import Blueprint, request, json, jsonify, abort, render_template
from .utils_blueprint import flask_construct_response, flask_constructor_error
import json
import logging
import MySQLdb
from ..api_db import users_db
USERS_API_BLUEPRINT = Blueprint(u'users_api', __name__)

@USERS_API_BLUEPRINT.route(u'/signup', methods = [u'GET'])
def signup_goolgeauth_user():
    print "great"
    return flask_construct_response({u'response': 'Update points and score successfull'}, 201   )
    #result = users_db.signup_goolgeauth()


@USERS_API_BLUEPRINT.route(u'/signin', methods = [u'POST'])
def signin_user():
    payload = json.loads(request.data)
    try:
        if set((u"source", u"email", u"password")) <= set(payload.keys()):
            """Retrieve all informations about user
            (basic information, boughts, rents, playlist, whislist) 
            and send to the front""" 
            check_user_in_db = users_db.is_user_in_db(payload[u"source"], payload[u"email"], payload[u"password"])
            print check_user_in_db
            if check_user_in_db is True:
                print payload[u"email"]
                all_user_informations = users_db.get_user_informations(payload[u"email"])
                return flask_construct_response(all_user_informations, 200)
            else: 
                return flask_constructor_error(u"Not Found", 404, 404)
            
        else:
            return flask_constructor_error(u"Bad Request", 400, 400)
    except BaseException as e:
        logging.error(u'Error: {}'.format(unicode(e).encode(u'utf-8')))
        return flask_constructor_error(u"Not Found", 404, 404)

"""
Help to retrieve all user's playlists
""" 
@USERS_API_BLUEPRINT.route(u'/<string:username>/playlists', methods = [u'GET'])
def get_user_playlists(username):
    print "user passed on url: {}".format(username)
>>>>>>> 0c8fd7d074cd476b1ca43e0da6b751e020daffab
