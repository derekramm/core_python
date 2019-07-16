#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_pytest.py"""
#
# # 编写测试脚本
# 测试文件以test_开头（以_test结尾也可以）
#
# 测试类以Test开头，并且不能带有init方法
#
# 测试函数以test_开头
#
# 断言使用基本的assert即可
# pytest 被测试文件.py --html=report.html​​​

import pytest

def func(x):
    return x + 1

def test_func():
    assert func(3) == 4
