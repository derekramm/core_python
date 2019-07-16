#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex08_装饰器的应用.py"""

import logging, sys

logging.basicConfig(
    level=logging.DEBUG,
    stream=sys.stderr,
    format='%(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def decorator(func):
    def log(*args):
        for _ in args:
            logger.debug(_)
        return func(*args)

    return log


@decorator
def show(*args):
    print('hello', *args)


show('xiaoming', 'leguan')
