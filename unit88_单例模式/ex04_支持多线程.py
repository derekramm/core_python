#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex04_支持多线程.py"""
import random
import time, threading

class Singleton(object):
    _instance_lock = threading.Lock()
    def __init__(self):
        time.sleep(random.random())
    @classmethod
    def instance(cls):
        with Singleton._instance_lock:
            if not hasattr(Singleton, "_instance"):
                Singleton._instance = Singleton()
        return Singleton._instance

def task(): print(Singleton.instance())

if __name__ == '__main__':
    for i in range(10):
        threading.Thread(target=task).start()
