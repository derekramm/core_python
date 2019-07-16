#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_继承机制.py"""

class D: pass

class C(D): pass

class B(C):
    def show(self): print("i am B")

class G: pass

class F(G): pass

class E(F):
    def show(self): print("i am E")

class A(B, E): pass

a = A()
a.show()
