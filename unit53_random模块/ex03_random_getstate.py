#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex03_random_getstate.py"""

import pickle
import random

state = random.getstate()
with open('state', 'wb') as f:
    pickle.dump(state, f)

for _ in range(3):
    print(random.random())

print('*' * 80)

with open('state', 'rb') as f:
    state = pickle.load(f)
random.setstate(state)

for _ in range(3):
    print(random.random())
