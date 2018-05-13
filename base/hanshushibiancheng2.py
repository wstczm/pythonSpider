#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-13
# @Author  : james.zhang


def is_odd(n):
    return n % 2 == 1


print filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])


def not_empty(s):
    return s and s.strip()


print filter(not_empty, ['A', '', 'B', None, 'C', '  '])


# 请尝试用filter()删除1~100的素数。

def is_prime(n):
    if n == 1:
        return False
    else:
        i = 2
        while n > i:
            if n % i == 0:
                return False
            i = i + 1
        return True


print filter(is_prime, range(1, 101))

