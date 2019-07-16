#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_工厂方法示例.py"""

class ChineseGetter(object):
    def __init__(self):
        self.trans = dict(dog="小狗", cat="小猫")
    def get(self, message_id):
        return self.trans.get(message_id, str(message_id))

class GreekGetter(object):
    def __init__(self):
        self.trans = dict(dog="σκύλος", cat="γάτα")
    def get(self, message_id):
        return self.trans.get(message_id, str(message_id))

class EnglishGetter(object):
    @staticmethod
    def get(message_id):
        return str(message_id)

def get_localizer(language='English'):
    languages = dict(English=EnglishGetter, Greek=GreekGetter, Chinese=ChineseGetter)
    return languages[language]()

if __name__ == '__main__':
    e, g, c = get_localizer(language='English'), get_localizer(language='Greek'), get_localizer('Chinese')
    for msgid in 'dog parrot cat bear'.split():
        print(e.get(msgid), g.get(msgid), c.get(msgid))
