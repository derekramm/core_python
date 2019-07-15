#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_pymongo_连接.py"""

import pymongo
conn = pymongo.MongoClient('localhost', 27017)
db = conn.northwind

col_products = db.products
col_categories = db.categories
col_suppliers = db.suppliers

conn.close()
