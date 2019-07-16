#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex11_pure.py"""

from pathlib import *
p = Path('./about.txt')  # 获取当前目录
print(p)

length = p.write_text('''hello
my name is xiaoming
his name is daxiyi''', encoding='utf-8')

print(length)

content = p.read_text(encoding='utf-8')
print(content)

b_content = p.read_bytes()
print(b_content)
