#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex10_读取JSON生层excel.py"""

import json, xlwt
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('Product Info')

with open('northwind.json', 'rb+') as f:
    products = json.loads(f.read(), encoding='utf-8')

alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
alignment.vert = xlwt.Alignment.VERT_CENTER

font = xlwt.Font()
font.bold = True

pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = 5

style = xlwt.XFStyle()

style.alignment = alignment
style.font = font
style.pattern = pattern

for col, key in enumerate(products[0].keys()):
    worksheet.write(0, col, key, style)

for row, product in enumerate(products):
    for col,value in enumerate(product.values()):
        worksheet.write(row+1, col, value)

workbook.save('products.xls')
