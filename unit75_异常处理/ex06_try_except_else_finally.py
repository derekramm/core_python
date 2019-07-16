#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex06_try_except_else_finally.py"""

inp = input("请输⼊入你的年年龄: ")
numa = input("请输⼊入被除数: ")
numb = input("请输⼊入除数: ")

try:
    age = int(inp)
    print('成年' if age >= 18 else '未成年')
    print('{}/{}={}'.format(numa, numb, int(numa) / int(numb)))
except ValueError as exp:
    print(exp)
except ZeroDivisionError as exp:
    print(exp)
except Exception as exp:
    print(exp)
else:
    print('成功执行完毕')
finally:
    print('程序结束')
