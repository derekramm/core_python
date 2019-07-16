#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex06_向单元格添加超链接.py"""

import xlwt
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')
worksheet.write(0, 0, xlwt.Formula('HYPERLINK("http://www.tedu.cn";"TEDU")'))
workbook.save('Excel_Workbook.xls')
