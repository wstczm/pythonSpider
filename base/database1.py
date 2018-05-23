#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-23 15:49:00
# @Author  : james.zhang

import mysql.connector
conn = mysql.connector.connect(user='root', password='root', database='mysql', use_unicode=True)
cursor = conn.cursor()
cursor.execute('select * from help_category')
values = cursor.fetchall()
print values
cursor.close()
conn.close()