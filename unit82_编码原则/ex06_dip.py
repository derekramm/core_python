#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex06_dip.py"""

class Paper(object):
    def set_paper(self): return '纸张'

class A4(Paper):
    def set_paper(self): return 'A4' + super(A4, self).set_paper()

class B5(Paper):
    def set_paper(self): return 'B5' + super(B5, self).set_paper()

class Box(object):
    def set_box(self): return '墨盒'

class Color(Box):
    def set_box(self): return '彩色' + super(Color, self).set_box()

class Gray(Box):
    def set_box(self): return '黑白' + super(Gray, self).set_box()

class Printer(object):
    @staticmethod
    def printing(paper, box):
        return f'使用{box.set_box()}在{paper.set_paper()}上打印'

print(Printer.printing(A4(), Color()))
print(Printer.printing(A4(), Gray()))
print(Printer.printing(B5(), Color()))
print(Printer.printing(B5(), Gray()))
