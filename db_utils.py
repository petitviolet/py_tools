# -*- encoding:utf-8 -*-
import MySQLdb
db_info = {
    'HOST': 'HOST',
    'DB': 'DB',
    'USER': 'USER',
    'PASSWD': 'PASSWD',
    'CHARSET': 'utf8'
}


class DbUtil(object):
    def __init__(self, db_name=''):
        self.con = MySQLdb.connect(**db_info)
        self.con.cursorclass = MySQLdb.cursors.DictCursor
        self.cur = self.con.cursor()

    def __del__(self):
        self.cur.close()
        self.con.close()

