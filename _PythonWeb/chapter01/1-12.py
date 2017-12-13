#!/usr/bin/env python
# -*- coding: utf-8 -*-

myList = ['you', 456, 'English', 9.34]				#定義

print myList[2]								#讀取元素

print myList[1:]								#截取子清單

myList[2]='France'							#可以修改內容
print myList

print len(myList)								#用函數len()獲得清單長度

numList = [2, 8, 16, 1, -6, 52, -1]					#定義
print sorted(myList)							#排序

print myList								#sorted後myList本身並不改變

print sum(numList)							#求和
