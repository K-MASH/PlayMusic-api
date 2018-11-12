<<<<<<< HEAD
# coding: utf-8
"""
Configuration file.
"""
import logging


CONFIG = {
    u"db": {
        u"unix_socket": u"/cloudsql/",
        u"user": u"root",
        u"host" : u"",
        u"password": u"",
        u"database": u"",
        u"charset": u"utf-8"
=======
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
>>>>>>> 0c8fd7d074cd476b1ca43e0da6b751e020daffab
    },
    u"logging": {
        u"level": logging.INFO,
        u"pattern": u'%(levelname)s - %(asctime)s : %(message)s',
        u"pattern_debug": u'[%(filename)15s::%(funcName)15s]-[l.%(lineno)3s] %(message)s'
    },
    u"app": {
<<<<<<< HEAD
        u"env": u"dev",
        u"debug": True
    }
}
=======
        u"env": u"prod",
        u"debug": False
    }
}
>>>>>>> 0c8fd7d074cd476b1ca43e0da6b751e020daffab
