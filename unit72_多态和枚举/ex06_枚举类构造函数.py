#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex06_枚举类构造函数.py"""

from enum import Enum

class Gender(Enum):
    MALE = '男', '阳刚之力'
    FEMALE = '女', '柔顺之美'
    def __init__(self, name, desc):
        self._name = name
        self._desc = desc
    @property
    def desc(self):
        return self._desc
    @property
    def name(self):
        return self._name

print(Gender.MALE.name, Gender.MALE.desc)
print(Gender.FEMALE.name, Gender.FEMALE.desc)
