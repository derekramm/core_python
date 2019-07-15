#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_创建数据库表.py"""

import pymysql
db = pymysql.connect("localhost", "root", "781220", "mybookshopdb")
cursor = db.cursor()

cursor.execute('drop table if exists book')

sql = '''create table book(
id int primary key,
title nvarchar(50) not null unique,
author nvarchar(255) not null,
price decimal(18,2) check(price>=0),
pubdate date)'''

cursor.execute(sql)

db.close()