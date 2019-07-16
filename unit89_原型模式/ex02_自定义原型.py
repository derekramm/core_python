#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_自定义原型.py"""

class Prototype(object):
    value = 'default'  # 类属性
    def clone(self, **attrs):
        obj = self.__class__()  # 根据Prototype类型创建对象实例
        obj.__dict__.update(attrs)
        return obj  # 返回对象实例

class PrototypeDispatcher(object):
    def __init__(self): self._objects = {}
    def get_objects(self): return self._objects
    def register_object(self, name, obj): self._objects[name] = obj
    def unregister_object(self, name): del self._objects[name]

if __name__ == '__main__':
    dispatcher = PrototypeDispatcher()  # 创建调度对象
    prototype = Prototype()  # 创建原型对象
    d = prototype.clone()  # 默认克隆
    a = prototype.clone(value='a-value', category='a')
    b = prototype.clone(value='b-value', is_checked=True)
    # 将克隆出来的对象实例注册到调度对象中
    dispatcher.register_object('objecta', a)
    dispatcher.register_object('objectb', b)
    dispatcher.register_object('default', d)

    # 遍历调度对象中所有的实例，并输出
    print([{n: p.value} for n, p in dispatcher.get_objects().items()])
