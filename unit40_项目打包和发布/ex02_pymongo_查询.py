#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_pymongo_查询.py"""


import pymongo
conn = pymongo.MongoClient('localhost', 27017)
db = conn.northwind

col_products = db.products
col_categories = db.categories
col_suppliers = db.suppliers

for c in col_categories.find({}, {'_id': 0}):
    print(c['CategoryId'], c['CategoryName'])

conn.close()


