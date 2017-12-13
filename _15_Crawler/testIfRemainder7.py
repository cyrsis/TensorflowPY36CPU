#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'


def isEvenNum(num):
	if num%7 == 0:
		print(u"%d 可以被7整除" %num)
	else:
		print(u"%d 不可被7整除" %num)

if __name__ == '__main__':
	numStr = raw_input("請輸入一個整數：")
	try:
		num = int(numStr)
	except ValueError:
		print(u"輸入錯誤，要求輸入一個整數")
		exit()

	isEvenNum(num)
