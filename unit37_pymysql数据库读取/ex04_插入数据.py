#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_插入数据.py"""

import pymysql
db = pymysql.connect("localhost", "root", "781220", "mybookshopdb")
cursor = db.cursor()

sql = '''insert into book(id,title,author,price,pubdate) 
values 
(1,'python','Guido van Rossum',10,'2010-1-1'),
(2,'java','James Gosling',20,'2010-2-1'),
(3,'c#','Anders Hejlsberg',30,'2010-3-1'),
(4,'c','Dennis Ritchie',40,'2010-4-1')'''

try:
    cursor.execute(sql)
    db.commit()
except Exception as ex:
    db.rollback()
    print(ex)

db.close()