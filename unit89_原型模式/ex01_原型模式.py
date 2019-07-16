#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_原型模式.py"""

from copy import copy, deepcopy

class Prototype(object):
    __slots__ = ('name', 'nums')
    def __init__(self, name, nums):
        self.name = name
        self.nums = nums
    def clone(self): return copy(self)
    def deep_clone(self): return deepcopy(self)

if __name__ == '__main__':
    p1 = Prototype('xm', [1, 2, 6, 8])
    p2 = p1.clone()
    p3 = p1.deep_clone()
    p1.name = 'dxy'
    p1.nums[0] = 0
    print(p1.name, p1.nums)
    print(p2.name, p2.nums)
    print(p3.name, p3.nums)
