#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_pymongo_查询.py"""


import pymongo
conn = pymongo.MongoClient('localhost', 27017)
db = conn.northwind

col_products = db.products
col_categories = db.categories
col_suppliers = db.suppliers

product = col_products.find({'ProductId': 27}, {'_id': 0}).next()
product['UnitPrice'] = 99.99
col_products.update_one({'ProductId': 27}, {'$set': product})

product = col_products.find({'ProductId': 27}, {'_id': 0})
print(product.next())


conn.close()


