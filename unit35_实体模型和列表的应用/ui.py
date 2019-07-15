#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ui.py"""

import unit35_实体模型和列表的应用.bll
flag = input('你今天吃饭了吗？（y=吃过了，n=没吃）：')
if flag == 'y':
    flag = True
else:
    flag = False

print(unit35_实体模型和列表的应用.bll.choose(flag))
