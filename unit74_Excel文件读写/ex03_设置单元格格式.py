#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_设置单元格格式.py"""

import xlwt
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')
worksheet.write(0, 0, 'My Cell Contents')
# 设置单元格宽度
worksheet.col(0).width = 8000
worksheet.col(0).height = 40

workbook.save('Excel_Workbook.xls')
