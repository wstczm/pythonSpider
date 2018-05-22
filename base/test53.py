#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-11
# @Author  : james.zhang

import os

print [x * x for x in range(1, 11) if x % 2 == 0]

print [m + n for m in 'ABC' for n in 'XYZ']

print [d for d in os.listdir('.')]

L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [s.lower() for s in L1 if isinstance(s, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
