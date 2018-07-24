#coding: utf8

from flask import Flask
from src.utils import init_logger
from src.blueprint import USERS_API_BLUEPRINT, ALBUMS_API_BLUEPRINT
from config import CONFIG_DEV, CONFIG_PROG

CONFIG = CONFIG_DEV
logging_config = CONFIG[u"logging"]
init_logger(logging_config[u'pattern'], logging_config[u'pattern_debug'], logging_config[u"level"])

#create flask server
APP = Flask(__name__)
APP.register_blueprint(USERS_API_BLUEPRINT, url_prefix = u'/api/users')

if __name__ == "__main__":
    APP.run(threaded=True, port=5000, debug=True)
