#!/usr/bin/env python
# -*- coding: utf-8 -*-

sample1 = set('understand')					#用string起始化set
print sample1								

myList = [ 4, 6, -1.1, 'English', 0, 'Python']			
sample2 = set(myList)							#用list起始化set
print sample2

sample3 = frozenset(myList)					#起始化frozenset
print sample3
