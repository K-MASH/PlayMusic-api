import src.requests as req
import logging
from flask import Blueprint, request, json
from .blueprint_utils import flask_construct_response
PLAYLISTS_API_BLUEPRINT = Blueprint(u'playlists_api', __name__)




"""
As her name indicates, this method allow to get all playlists in database
"""
@PLAYLISTS_API_BLUEPRINT.route(u'/', methods=[u'GET'])
def get_all_playlists():
    items = req.getAllPlaylists()
    return flask_construct_response({u'items':items})