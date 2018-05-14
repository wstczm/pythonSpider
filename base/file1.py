#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-14 21:50:02
# @Author  : james.zhang


sfile = 'C:/Users/Administrator/Desktop/test.txt'
tfile = 'C:/Users/Administrator/Desktop/test2.txt'

with open(sfile, 'r') as sf:
    with open(tfile, 'w') as tf:
        tf.write(sf.read())
