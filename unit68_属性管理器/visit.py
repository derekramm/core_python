#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""visit.py"""

import unit68_属性管理器.mysite

def run():
    inp = input("请输入您想访问页面的url：  ").strip()
    modules, func = inp.split("/")
    obj = __import__("lib." + modules, fromlist=True)  # 注意fromlist参数
    if hasattr(obj, func):
        func = getattr(obj, func)
        func()
    else:
        print("404")

if __name__ == '__main__':
    run()

if __name__ == '__main__':
    run()
