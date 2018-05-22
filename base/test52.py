#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-11
# @Author  : james.zhang

from collections import Iterable

list = [1, 2, 3, 4, 5]

tuple = (1, 2, 3, 4, 5)

dict = {'a': 1, 'b': 2, 'c': 3}

set = {1, 2, 3, 4, 5}

str = "abcde"

for l in list:
    print l

for t in tuple:
    print t

for d in dict:
    print d

for s in set:
    print s

for s in str:
    print s


print isinstance('abc', Iterable)  # str是否可迭代

print isinstance([1, 2, 3], Iterable)  # list是否可迭代

print isinstance(123, Iterable)  # 整数是否可迭代


for i, value in enumerate(list):
    print i, value


def findMinAndMax(L):
    min = None
    max = None
    if isinstance(L, Iterable):
        for i, v in enumerate(L):
            if i == 0:
                min = max = v
            else:
                if min > v:
                    min = v
                if max < v:
                    max = v
    return (min, max)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败1!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败2!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败3!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败4!')
else:
    print('测试成功!')
