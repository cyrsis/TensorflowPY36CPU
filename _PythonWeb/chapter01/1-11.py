#!/usr/bin/env python
# -*- coding: utf-8 -*-

tuple1 = ('you', 456, 'English', 9.34)				#定義

print tuple1[2]								#讀取元素

print tuple1[1:]								#截取子元群組

tuple1[2]='France'							#錯誤！不能修改元群組內容

tuple2 = (3, 'you and me')					
tuple1 = tuple1 + tuple2						#可以對元群組變數重新給予值

print tuple1

print len(tuple2)								#用函數len()獲得元群組長度
