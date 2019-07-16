#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex09_设置单元格背景.py"""

import xlwt
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')

pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = 5

style = xlwt.XFStyle()
style.pattern = pattern

worksheet.write(0, 0, 'Cell Contents', style)
workbook.save('Excel_Workbook.xls')
