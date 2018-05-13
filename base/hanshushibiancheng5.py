#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-13 22:49:18
# @Author  : james.zhang


def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。


@log
def now():
    print '2013-12-25'


# now()


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    print '123'
    return decorator


@log('execute')
def now():
    print '2013-12-25'


now()
