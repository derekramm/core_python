#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex08_purepath.py"""

from pathlib import *
pp = PurePath('/', 'usr', 'local', 'python', 'hello_world.py')
print(pp)  # /usr/local/python/hello_world.py

print(pp.as_posix())  # /usr/local/python/hello_world.py
print(pp.as_uri())  # file:///usr/local/python/hello_world.py

print(pp.relative_to('/'))  # usr/local/python/hello_world.py
print(pp.relative_to('/usr'))  # local/python/hello_world.py
print(pp.relative_to('/usr/local'))  # python/hello_world.py
