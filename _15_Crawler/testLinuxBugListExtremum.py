#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

import cls
import time

def getList():
	#構建一個純數字串列
	numList = []
	num = 'q'
	while num:
		cls.clear()
		print numList
		print(u'結束構建串列，請按換行')
		num = raw_input('請輸入一個整數：')
		if num == '':
			break
		try:
			num = int(num)
		except ValueError:
			print(u'要求輸入整數，請重新輸入')
			time.sleep(1)
			continue
		numList.append(num)
	return numList

def getMaxNum(List):
	#取得串列中最大值
	#import pdb
	#pdb.set_trace()
	num = List[0]
	for i in List[1:]:
		if num <= i:
			num = i
	return num

def getMinNum(List):
	#取得串列中最小值
	num = List[0]
	for i in List[1:]:
		if num >= i:
			num = i
	return num


if __name__ == '__main__':
	numList = getList()
	maxNum = getMaxNum(numList)
	print(u'串列中最大值為:%d' %maxNum)
	minNum = getMinNum(numList)
	print(u'串列中最小值為:%d' %minNum)
