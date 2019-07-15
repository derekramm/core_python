#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_格式化字符串中的命名.py"""

# % [(name)] [flags] [width] . [precision] typecode
# （name)：可选，用于选择指定的变量名

print("%(ln)s %(fn)s" % {'fn': 'ramm', 'ln': 'derek'})
