#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-11
# @Author  : james.zhang


def triangles():
    result = [1]
    while True:
        yield result
        result = [1] + [result[x] + result[x + 1] for x in range(len(result) - 1)] + [1]


t = triangles()

print next(t)
print next(t)
print next(t)
print next(t)
print next(t)
