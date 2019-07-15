#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_pymongo_查询.py"""

import pymongo
conn = pymongo.MongoClient('localhost', 27017)
db = conn.northwind

col_products = db.products
col_categories = db.categories
col_suppliers = db.suppliers

col_products.delete_one({'ProductId': 27})

for p in col_products.find({}, {'_id': 0}):
    print(p)

conn.close()
