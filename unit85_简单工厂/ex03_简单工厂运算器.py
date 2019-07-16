#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_简单工厂运算器.py"""

class Calculator(object):
    def __init__(self):
        self.numa = None
        self.numb = None
    def get_result(self): pass

class Add(Calculator):
    def get_result(self): return self.numa + self.numb

class Sub(Calculator):
    def get_result(self): return self.numa - self.numb

class Mul(Calculator):
    def get_result(self): return self.numa * self.numb

class Div(Calculator):
    def get_result(self): return self.numa / self.numb

class CalculatorFactory(object):
    @staticmethod
    def get_calculator(operator):
        if operator == '+':
            return Add()
        elif operator == '-':
            return Sub()
        elif operator == '*':
            return Mul()
        elif operator == '/':
            return Div()
        else:
            return None

if __name__ == '__main__':
    op = input('please enter an operator: ')
    cal = CalculatorFactory.get_calculator(op)
    cal.numa = float(input('please enter numa:'))
    cal.numb = float(input('please enter numb:'))
    print(f'{cal.numa} {op} {cal.numb} = {cal.get_result()}')
