#!/usr/bin/env python
# -*- coding: utf-8 -*-



def demoIterator():						#定義一個迭代器函數
    print("I'm in the first call of next()")
    yield 1
    print("I'm in the second call of next()")
    yield 3
    print("I'm in the third call of next()")
    yield 9

for i in demoIterator():
    print(i)
