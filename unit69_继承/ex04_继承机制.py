#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_继承机制.py"""

class D:
    def show(self): print("i am D")

class C(D): pass

class B(C): pass

class G: pass

class F(G): pass

class E(F):
    def show(self): print("i am E")

class A(B, E): pass

a = A()
a.show()
