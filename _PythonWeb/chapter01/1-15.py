#!/usr/bin/env python
# -*- coding: utf-8 -*-

myList = [ 4, 6, -1.1, 'English', 0, 'Python']			
sample2 = set(myList)							#起始化set
sample3 = frozenset([ 6, 'English', 9])				#起始化frozenset

print 6 in sample2							#判斷包括關系

print  sample2 >= sample3						#判斷子集關系

print  sample2 - sample3						#差運算

print sample2 & sample3						#交運算

sample3 |= sample2							#可以對frozenset執行 |= 重新給予值
print sample3
