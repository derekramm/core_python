#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_聚合关系.py"""

class PetShop(object):
    def __init__(self):
        self.pets = []
    def add_pet(self, pet): self.pets.append(pet)

shop = PetShop()
shop.add_pet('cat')
shop.add_pet('dog')
shop.add_pet('turtle')
shop.add_pet('snake')

print(shop.pets)
