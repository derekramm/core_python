#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_建造者示例.py"""

from abc import abstractmethod, ABCMeta

class Building(object, metaclass=ABCMeta):
    def __init__(self):
        self.floor = None
        self.size = None
        self.build_floor()
        self.build_size()
    @abstractmethod
    def build_floor(self):
        raise NotImplementedError
    def build_size(self):
        raise NotImplementedError
    def __repr__(self):
        return 'Floor: {0.floor} | Size: {0.size}'.format(self)

class House(Building):
    def build_floor(self):
        self.floor = 'one'
    def build_size(self):
        self.size = 'big'

class Flat(Building):
    def build_floor(self):
        self.floor = 'more than one'
    def build_size(self):
        self.size = 'small'

class ComplexBuilding(object):
    def __init__(self):
        self.floor = None
        self.size = None
    def __repr__(self):
        return 'Floor: {0.floor} | Size: {0.size}'.format(self)

class ComplexHouse(ComplexBuilding):
    def build_floor(self):
        self.floor = 'more than one'
    def build_size(self):
        self.size = 'big and fancy'

def construct_building(cls):
    building = cls()
    building.build_floor()
    building.build_size()
    return building

if __name__ == '__main__':
    house = House()
    print(house)
    flat = Flat()
    print(flat)
    complex_house = construct_building(ComplexHouse)
    print(complex_house)
