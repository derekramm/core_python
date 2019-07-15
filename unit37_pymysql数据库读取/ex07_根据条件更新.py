#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex07_根据条件更新.py"""

import pymysql

db = pymysql.connect("localhost", "root", "781220", "mybookshopdb")
cursor = db.cursor()

sql = '''update book set price=%s where id=%s'''

try:
    cursor.execute(sql, (20, 1))
    db.commit()
except Exception as ex:
    print(ex)
    db.rollback()

db.close()