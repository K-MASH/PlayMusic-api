#coding: utf8
from flask import abort
from google.appengine.api import users
import MySQLdb
import logging
from . import connect_db

def get_basic_information(username):
    return "great"

