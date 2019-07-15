#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_查询数据库.py"""

import pymysql
db = pymysql.connect("localhost", "root", "781220", "mybookshopdb")
cursor = db.cursor()

sql = '''select * from book'''

cursor.execute(sql)
books = cursor.fetchall()

db.close()

for book in books:
    print(book)
