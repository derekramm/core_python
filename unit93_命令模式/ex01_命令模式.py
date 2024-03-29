#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_命令模式.py"""

from abc import ABCMeta, abstractmethod

class Receiver(object):
    @staticmethod
    def show_a(): print('show_a')
    @staticmethod
    def show_b(): print('show_b')

class Command(object, metaclass=ABCMeta):
    def __init__(self, r):
        self.receiver = r
    @abstractmethod
    def execute(self): pass

class CommandA(Command):
    def execute(self): self.receiver.show_a()

class CommandB(Command):
    def execute(self): self.receiver.show_b()

class Invoker(object):
    def __init__(self):
        self.commands = []
    def add(self, c): self.commands.append(c)
    def remove(self, c): self.commands.remove(c)
    def notify(self):
        for c in self.commands:
            c.execute()

if __name__ == '__main__':
    r = Receiver()
    a = Invoker()
    for _ in range(5):
        a.add(CommandA(r))
        a.add(CommandB(r))
    a.notify()
