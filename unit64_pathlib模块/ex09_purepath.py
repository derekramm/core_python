#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex09_purepath.py"""

from pathlib import *

pp = PurePath('/', 'usr', 'local', 'python', 'hello_world.py')
print(pp)  # /usr/local/python/hello_world.py

print(pp.with_name('hello_xm.py'))
print(pp.with_suffix('.pyc'))