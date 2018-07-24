from flask import Blueprint, request, json, jsonify
from .utils_blueprint import flask_construct_response, flask_constructor_error
ALBUMS_API_BLUEPRINT = Blueprint(u"albums_api", __name__)


@ALBUMS_API_BLUEPRINT.route(u'/', methods = [u'GET'])
def get_album():
    pass