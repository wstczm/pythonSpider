#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-13
# @Author  : james.zhang

# map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。

# reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算。
# print map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']


list = ['adam', 'LISA', 'barT']


def test1(str):
    # print str.capitalize()
    return str[0:1].upper() + str[1:].lower()


print map(test1, list)


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积。
list = [1, 2, 3, 4, 5]


def prod(l):
    def test2(x, y):
        return x * y
    return reduce(test2, l)


print prod(list)
