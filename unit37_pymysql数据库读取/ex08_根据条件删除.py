#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex08_根据条件删除.py"""

import pymysql

db = pymysql.connect("localhost", "root", "781220", "mybookshopdb")
cursor = db.cursor()

sql = '''delete from book where id=%s'''

try:
    cursor.execute(sql, 1)
    db.commit()
except Exception as ex:
    print(ex)
    db.rollback()

db.close()