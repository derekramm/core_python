#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_创建数据库.py"""

import pymysql
db = pymysql.connect("localhost", "root", "781220", "mysql")
cursor = db.cursor()
cursor.execute("create database mybookshopdb")
db.close()