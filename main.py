# coding: utf-8
from flask import Flask

from config import CONFIG
from src.utils import init_logger


import MySQLdb
import src.requests as req

logging_config = CONFIG[u"logging"]
init_logger(logging_config[u'pattern'], logging_config[u'pattern_debug'], logging_config[u"level"])


# create flask server
APP = Flask(__name__)
APP.debug = CONFIG[u"app"][u"debug"]
APP.register_blueprint(USERS_API_BLUEPRINT, url_prefix = u'/api/users')
APP.register_blueprint(ARTISTS_API_BLUEPRINT, url_prefix = u'/api/artists')
APP.register_blueprint(TRACKS_API_BLUEPRINT, url_prefix = u'/api/tracks')
APP.register_blueprint(ALBUMS_API_BLUEPRINT, url_prefix = u'/api/albums')
APP.register_blueprint(PLAYLISTS_API_BLUEPRINT, url_prefix = u'/api/playlists')


if __name__ == u"__main__":
    APP.run(threaded=True, port=5000, debug=True)