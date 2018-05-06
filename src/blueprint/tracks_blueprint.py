import src.requests as req
import logging
from flask import Blueprint, request, json
from .blueprint_utils import flask_construct_response
TRACKS_API_BLUEPRINT = Blueprint(u'tracks_api', __name__)




"""
As her name indicates, this method allow to get all tracks in database
"""
@TRACKS_API_BLUEPRINT.route(u'/', methods=[u'GET'])
def get_all_tracks():
    items = req.getAllTracks()
    return flask_construct_response({u'items':items})