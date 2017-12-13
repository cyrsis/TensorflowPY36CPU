#!/usr/bin/env python
# -*- coding: utf-8 -*-

dict1 = {'Language': 'English', 'Title': 'Python book', 'Pages': 450}

print dict1['Title']									#讀取元素

dict1['Date'] = '2002-10-30'							#直接透過索引新增字典內容
print dict1

dict1['Language'] = 'Chinese'						#直接透過索引更新字典內容
print dict1

dict2 = {'Language': 'English', 'Language':'Chinese'}		
print dict2
