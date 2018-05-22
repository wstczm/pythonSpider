#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-11
# @Author  : james.zhang


def trim(s):
    if len(s) == 0:
        return s
    while len(s) > 0 and s[0] == ' ':
        s = s[1:]
    while len(s) > 0 and s[-1] == ' ':
        s = s[:-1]
    return s


if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
