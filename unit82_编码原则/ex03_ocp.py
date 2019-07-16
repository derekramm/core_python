#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_ocp.py"""

# 改造后

import pymysql

class Account(object):
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

def connect(account, database):
    db = pymysql.connect(account.host, account.username, account.password, database)
    cursor = db.cursor()
    cursor.execute('select version()')
    result = cursor.fetchone()
    db.close()
    return result

acc = Account('localhost', 'guest', '')
print(connect(acc, 'test'))
