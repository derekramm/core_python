#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex11_读取excel文件.py"""

import xlrd

book = xlrd.open_workbook("products.xls")
sheet = book.sheets()[0]

for r in range(sheet.nrows):
    print(sheet.row_values(r, 0, sheet.ncols))

