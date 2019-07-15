#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex02_使用偏函数打印关键字.py"""

import functools
import keyword

println = functools.partial(print, sep='\n', end='\n')

println(*(range(5)))
println(*keyword.kwlist)
