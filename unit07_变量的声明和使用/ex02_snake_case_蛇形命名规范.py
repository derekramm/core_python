#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex02_snake_case_蛇形命名规范.py
蛇形命名规范"""

PI = 3.14  # 常量全部大写
circle_radius = 10  # 变量使用全部小写的snake_case


class Shape:  # 类名首字母大写
    @staticmethod
    def get_circle_area():  # 方法名使用全部小写的snake_case
        try:
            return PI * circle_radius * circle_radius
        except Exception as ex:  # 异常首字母大写
            print(ex)
