#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-23 16:23:35
# @Author  : james.zhang

import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
print cursor.rowcount
conn.commit()
cursor.execute('select * from user where id=?', ('1',))
values = cursor.fetchall()
print values
cursor.close()
conn.close()