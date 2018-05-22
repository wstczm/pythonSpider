#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'james.zhang'


class Animal(object):
    def run(self):
        print 'Animal is running...'


class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog = Dog()
dog.run()

cat = Cat()
cat.run()

print dir('ABC')
