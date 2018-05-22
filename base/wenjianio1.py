#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'james.zhang'


sfile = 'C:/Users/Administrator/Desktop/tablesDDL.txt'

tfile = 'C:/Users/Administrator/Desktop/tablesDDL2.txt'


with open(sfile, 'r') as sf:
    with open(tfile, 'w') as tf:
        tf.write(sf.read())
