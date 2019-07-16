#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex08_设置单元格对齐.py"""

import xlwt
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')

alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
alignment.vert = xlwt.Alignment.VERT_CENTER

style = xlwt.XFStyle()
style.alignment = alignment

poem = '''静夜思
床前明月光，疑是地上霜。
举头望明月，低头思故乡。'''

worksheet.write(0, 0, 'Cell Contents', style)
worksheet.write(0, 1, poem, style)

workbook.save('Excel_Workbook.xls')
