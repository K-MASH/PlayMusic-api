#coding: utf8
from flask import abort
from google.appengine.api import users
import MySQLdb
import logging
from . import connect_db



def is_user_in_db(source, email, password):
    print "password: {}".format(password)
    if password is None:
        #User connect via classic form method
        cursor, con = connect_db.connect()
        cursor.execute(u"SELECT email FROM user WHERE email = '{}'".format(email))
        if cursor.fetchone():
            return True 
    else:
        #User connect via google auth method
        cursor, con = connect_db.connect()
        cursor.execute(u"SELECT email FROM user WHERE email = '{}' AND password = '{}'".format(email, password))
        if cursor.fetchone():
            return True
        
def get_user_informations(email):
    all_informations = {}
    cursor, con = connect_db.connect()
    cursor.execute("SELECT * FROM user WHERE email = '{}'".format(email))
    row = cursor.fetchone()
    if row:
        all_informations[u"id"] = row[0]
        all_informations[u"email"] = row[1]
        all_informations[u"first_name"] = row[4]
        all_informations[u"birthdate"] = row[5]
        all_informations[u"country"] = row[6]
        all_informations[u"town"] = row[7]
        all_informations[u"gender"] = row[8]
        all_informations[u"status"] = "simple user" if row[9] == 0 else ("artist" if row[9] == 1 else "admin")
        all_informations[u"language"] = row[10]
        all_informations[u"image"] = row[12]
        all_informations[u"phone"] = row[13]
    con.commit()
    if all_informations[u"status"] == 1:
        all_informations = get_artist_information(all_informations)
    else:
        all_informations = get_user_boughts(all_informations)
    return all_informations   


def get_artist_information(infos):
    return None


def get_user_boughts(infos):
    items = []
    print infos.get(u"id")
    try:
        if infos.get(u"id"):
            cursor, con = connect_db.connect()
            query = u"SELECT bought.date_bought, track.title, track.duration, track.track_position, track.music_genre, track.explicit_content, track.track_url, track.contributors_name, price_tag.type, price_tag.price FROM bought, track, price_tag WHERE bought.user_buying_id = '{}' AND bought.track_id = track.id AND bought.price_id = price_tag.id".format(infos.get(u"id"))
            cursor.execute(query)
            for row in cursor.fetchall():
                items.append({
                    u"date_bought": row[0],
                    u"title": row[1],
                    u"duration": row[2],
                    u"track_position": row[3],
                    u"music_genre": row[4],
                    u"explicit_content": True if row[5] == 1 else False,
                    u"track_url": row[6],
                    u"contributors_name": row[7],
                    u"payment_type": row[8],
                    u"price": row[9]
                })
        con.commit()
        infos[u"Boughts"] = items
    except BaseException as e:
        logging.error(u'Error: {}'.format(unicode(e).encode(u'utf-8')))

    return infos
