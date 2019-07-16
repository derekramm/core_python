#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex01_模块的基本概念.py"""

# petstore.py

petstore_name = 'xiaoming\'s pet store'


class Pet(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


def show_pet_info(pet):
    print('name:{}, age:{}'.format(pet.name, pet.age))
