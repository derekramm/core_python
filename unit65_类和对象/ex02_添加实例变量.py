#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_添加实例变量.py"""

class Dog:
    pass

dog1 = Dog()
dog1.kinds = '京巴'
dog1.color = '白色'
dog1.color = '黄色'

dog2 = Dog()
dog2.kinds = '拉布拉多'
dog2.color = '棕色'

print(dog1.__dict__)
print(dog2.__dict__)