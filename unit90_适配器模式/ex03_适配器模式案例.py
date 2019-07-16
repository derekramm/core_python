#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex03_适配器模式案例.py"""

class Dog(object):
    def __init__(self): self.name = "Dog"
    @staticmethod
    def bark(): return "woof!"

class Cat(object):
    def __init__(self): self.name = "Cat"
    @staticmethod
    def meow(): return "meow!"

class Human(object):
    def __init__(self): self.name = "Human"
    @staticmethod
    def speak(): return "'hello'"

class Car(object):
    def __init__(self): self.name = "Car"
    @staticmethod
    def make_noise(octane_level): return "vroom{0}".format("!" * octane_level)

class Adapter(object):
    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)
    def __getattr__(self, attr): return getattr(self.obj, attr)
    def original_dict(self): return self.obj.__dict__

if __name__ == '__main__':
    objects = []
    dog, cat, human, car = Dog(), Cat(), Human(), Car()
    objects.append(Adapter(dog, make_noise=dog.bark))
    objects.append(Adapter(cat, make_noise=cat.meow))
    objects.append(Adapter(human, make_noise=human.speak))
    objects.append(
        Adapter(car, make_noise=lambda: car.make_noise(3)))

    for obj in objects:
        print("A {0} goes {1}".format(obj.name, obj.make_noise()))
