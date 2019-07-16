#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_实例分析.py"""

import unit68_属性管理器.mysite as myshop

def run():
    inp = input("请输入您想访问的页面：").strip()
    if inp == "login":
        myshop.login()
    elif inp == "logout":
        myshop.logout()
    elif inp == "home":
        myshop.home()
    else:
        print("404")

if __name__ == '__main__':
    run()