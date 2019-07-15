#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_连接数据库.py"""

import pymysql
db = pymysql.connect("localhost", "guest", "", "test")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print(f"database version : {data}")
db.close()
