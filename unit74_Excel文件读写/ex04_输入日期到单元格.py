#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_输入日期到单元格.py"""

import xlwt
import datetime

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')
style = xlwt.XFStyle()
style.num_format_str = 'YYYY-MM-DD hh:mm:ss'
worksheet.write(0, 0, datetime.datetime.now(), style)
workbook.save('Excel_Workbook.xls')

