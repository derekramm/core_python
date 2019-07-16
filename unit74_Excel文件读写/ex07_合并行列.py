#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex07_合并行列.py"""

import xlwt
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')

worksheet.write_merge(0, 0, 0, 3, 'First Merge')
font = xlwt.Font()
font.bold = True
style = xlwt.XFStyle()
style.font = font

worksheet.write_merge(1, 2, 0, 3, 'Second Merge', style)
workbook.save('Excel_Workbook.xls')
