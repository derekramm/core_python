#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_官网案例.py"""

import xlwt
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('My Worksheet')
font = xlwt.Font()
font.name = 'Times New Roman'
font.bold = True
font.underline = True
font.italic = True
style = xlwt.XFStyle()
style.font = font
worksheet.write(0, 0, 'Unformatted value')
worksheet.write(1, 0, 'Formatted value', style)
workbook.save('Excel_Workbook.xls')
