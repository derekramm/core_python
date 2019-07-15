#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex08_format函数对齐.py"""

print(
    '{:*<10}'.format(12),  # 12********
    '{:*>10}'.format(12),  # ********12
    '{:*^10}'.format(12),  # ****12****
    sep='\n'
)
