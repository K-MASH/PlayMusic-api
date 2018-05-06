import src.requests as req
import logging
from flask import Blueprint, request, json
from .blueprint_utils import flask_construct_response
USERS_API_BLUEPRINT = Blueprint(u'users_api', __name__)




"""
As her name indicates, this method allow to get all users in database
"""
@USERS_API_BLUEPRINT.route(u'/', methods=[u'GET'])
def get_all_users():
    items = req.getAllUsers()
    return flask_construct_response({u'items':items})