#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_类型检查.py"""

class Animal: pass

class Dog(Animal): pass

class Cat(Animal): pass

class Bird: pass

class Duck(Animal, Bird): pass

print(issubclass(Dog, Animal))
print(issubclass(Cat, Animal))
print(issubclass(Bird, Animal))
print(issubclass(Duck, Animal))
print(issubclass(Duck, (Bird, Animal)))

print(isinstance(Dog(), Animal))
print(isinstance(Cat(), Animal))
print(isinstance(Bird(), Animal))
print(isinstance(Duck(), Animal))
print(isinstance(Duck(), (Bird, Animal)))

print(Animal.__subclasses__())
