#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_职责链扩展.py"""
from abc import ABCMeta, abstractmethod

class Position(object, metaclass=ABCMeta):
    def __init__(self, name, message=''):
        self.name = name
        self.superior = None
        self.info = message
    def handle_request(self, message):
        print(f'{self.name} 收到了 {message}')
        result = input(f'请输入审核意见（y：通过，n：不通过）：')
        if result == 'y':
            self._approve(message)
            if self.superior:
                self.superior.handle_request(message)
        else:
            self._refuse(message)
    @abstractmethod
    def _approve(self, message):
        pass
    def _refuse(self, message):
        print(f'{self.name} 拒绝了 {message}')

class TeamLeader(Position):
    def _approve(self, message):
        print(f'{self.name} 通过了 {message}')

class Manager(Position):
    def _approve(self, message):
        print(f'{self.name} 通过了 {message}')

class Boss(Position):
    def _approve(self, message):
        print(f'{self.name} 通过了 {message}')

if __name__ == '__main__':
    tl = TeamLeader('组长')
    mgr = Manager('经理')
    boss = Boss('老板')
    tl.superior = mgr
    mgr.superior = boss
    tl.handle_request('来自小铭的请假')

    tl.superior = boss
    tl.handle_request('来自大蜥蜴的请假')
