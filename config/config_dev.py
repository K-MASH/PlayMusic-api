<<<<<<< HEAD
# coding: utf-8
"""
Configuration file.
"""
import logging

=======
#coding: utf8
"""
dev configuration file
"""

import logging
>>>>>>> 0c8fd7d074cd476b1ca43e0da6b751e020daffab

CONFIG = {
    u"db": {
        u"user": u"root",
<<<<<<< HEAD
        u"host" : u"127.0.0.1",
        u"password": u"localroot1234",
        u"database": u"playMusic",
        u"charset": u"utf-8"
=======
        u"host": u"127.0.0.1",
        u"database": u"zik_dev",
        u"password": u"localroot1234"
>>>>>>> 0c8fd7d074cd476b1ca43e0da6b751e020daffab
    },
    u"logging": {
        u"level": logging.INFO,
        u"pattern": u'%(levelname)s - %(asctime)s : %(message)s',
<<<<<<< HEAD
        u"pattern_debug": u'[%(filename)15s::%(funcName)15s]-[l.%(lineno)3s] %(message)s'
=======
        u"pattern_debug": u'[%(filename)15s::%(funcName)15s]-[l.%(lineno)3s] %(message)s'      
>>>>>>> 0c8fd7d074cd476b1ca43e0da6b751e020daffab
    },
    u"app": {
        u"env": u"dev",
        u"debug": True
    }
<<<<<<< HEAD
}
=======

}
>>>>>>> 0c8fd7d074cd476b1ca43e0da6b751e020daffab
