<<<<<<< HEAD
import src.requests as req
import logging
from flask import Blueprint, request, json
from .blueprint_utils import flask_construct_response
ALBUMS_API_BLUEPRINT = Blueprint(u'albums_api', __name__)




"""
As her name indicates, this method allow to get all albums in database
"""
@ALBUMS_API_BLUEPRINT.route(u'/', methods=[u'GET'])
def get_all_albums():
    items = req.getAllAlbums()
    return flask_construct_response({u'items':items})
=======
from flask import Blueprint, request, json, jsonify
from .utils_blueprint import flask_construct_response, flask_constructor_error
ALBUMS_API_BLUEPRINT = Blueprint(u"albums_api", __name__)


@ALBUMS_API_BLUEPRINT.route(u'/', methods = [u'GET'])
def get_album():
    pass
>>>>>>> 0c8fd7d074cd476b1ca43e0da6b751e020daffab
