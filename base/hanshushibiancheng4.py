#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-13 22:41:53
# @Author  : james.zhang


def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
