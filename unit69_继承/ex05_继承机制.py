#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_继承机制.py"""

class H:
    def show(self): print('i am H')

class D(H): pass

class C(D): pass

class B(C): pass

class G(H): pass

class F(G): pass

class E(F):
    def show(self): print("i am E")

class A(B, E): pass

a = A()
a.show()
