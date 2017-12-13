#!/usr/bin/env python
# -*- coding: utf-8 -*-

dict1 = {'Language': 'English', 'Title': 'Python book', 'Pages': 450}

print(dict1.get('Title', 'Todo'))  # 讀取元素

print(dict1.get('Author', 'Anonymous'))  # 讀取不存在的鍵

print(dict1.pop('Language'))  # pop

print(dict1)  # 檢查pop後的字典內容

dict2={'Author':'David', 'Price':32.00, 'Pages':409 }	
dict1.update(dict2)								#合並字典
print(dict1)

print(dict1.values())  # 取得值清單
