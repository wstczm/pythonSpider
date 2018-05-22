#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'james.zhang'

try:
    print 'try...'
    r = 10 / 0
    print 'result:', r
except ZeroDivisionError, e:
    print 'except:', e
finally:
    print 'finally...'
print 'END'
