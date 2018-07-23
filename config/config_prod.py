#coding: utf8
"""
production file configuration
"""

import logging

CONFIG = {
    u"db":{
        u"host": u"",
        u"database": u"zik_prod",
        u"password": u"",
        u"user": u"root"
    },
    u"logging": {
        u"level": logging.INFO,
        u"pattern": u'%(levelname)s - %(asctime)s : %(message)s',
        u"pattern_debug": u'[%(filename)15s::%(funcName)15s]-[l.%(lineno)3s] %(message)s'
    },
    u"app": {
        u"env": u"prod",
        u"debug": True
    }
}