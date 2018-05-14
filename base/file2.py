#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-14 22:08:37
# @Author  : james.zhang

import os
# import time

# os.mkdir('C:/Users/Administrator/Desktop/test')
# time.sleep(3)
# os.rmdir('C:/Users/Administrator/Desktop/test')

# print os.path.split('/Users/michael/testdir/file.txt')
# print os.path.splitext('/path/to/file.txt')
# print[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']

# 编写一个search(s)的函数，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出完整路径：


def printFile(key, root='C:/Users/Administrator/Desktop/test'):
    for path in os.listdir(root):
        if os.path.isdir(os.path.join(root, path)):
            printFile(key, os.path.join(root, path))
        elif key in os.path.split(path)[1]:
            print os.path.abspath(path)


printFile('p')
