#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex06_根据条件查询数据.py"""

import pymysql
db = pymysql.connect("localhost", "root", "781220", "mybookshopdb")
cursor = db.cursor()

sql = '''select * from book where title like %s'''

cursor.execute(sql,'%c%')
books = cursor.fetchall()

db.close()

for book in books:
    print(book)
