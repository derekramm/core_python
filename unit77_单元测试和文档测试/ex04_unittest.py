#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_unittest.py"""

import unittest

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

class MyTest(unittest.TestCase):
    def test_method(self):
        self.assertEqual(add(12, 3), 15)
        self.assertEqual(sub(12, 3), 9)

if __name__ == "__main__":
    unittest.main()