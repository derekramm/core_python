#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_命令模式_文件重命名.py"""

from __future__ import print_function
import os
from os.path import lexists

class MoveFileCommand(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def execute(self):
        self.rename(self.src, self.dest)
    def undo(self):
        self.rename(self.dest, self.src)
    @staticmethod
    def rename(src, dest):
        print(u"renaming %s to %s" % (src, dest))
        os.rename(src, dest)

command_stack = []

command_stack.append(MoveFileCommand('foo.txt', 'bar.txt'))
command_stack.append(MoveFileCommand('bar.txt', 'baz.txt'))

assert not lexists("foo.txt")
assert not lexists("bar.txt")
assert not lexists("baz.txt")

try:
    with open("foo.txt", "w"):
        pass

    for cmd in command_stack:
        cmd.execute()

    for cmd in reversed(command_stack):
        cmd.undo()

finally:
    os.unlink("foo.txt")
