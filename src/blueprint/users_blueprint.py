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