#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex05_使用new实现单例.py"""
import random
import threading, time

class Singleton(object):
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance

def task():
    time.sleep(random.random())
    print(Singleton())

if __name__ == '__main__':
    for i in range(10):
        threading.Thread(target=task).start()
