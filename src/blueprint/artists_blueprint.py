import src.requests as req
import logging
from flask import Blueprint, request, json
from .blueprint_utils import flask_construct_response
ARTISTS_API_BLUEPRINT = Blueprint(u'artists_api', __name__)




"""
As her name indicates, this method allow to get all artists in database
"""
@ARTISTS_API_BLUEPRINT.route(u'/', methods=[u'GET'])
def get_all_artists():
    items = req.getAllArtists()
    return flask_construct_response({u'items':items})