#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

class TryInput(object):
	def __init__(self):
		self.len = 10
		self.numList = self.createList()
		self.getNum()

	def createList(self):
		print(u"建立一個長度為%d的數字串列" %self.len)
		numL = []
		while len(numL) < 10:
			n = raw_input("請輸入一個整數：")
			try:
				num = int(n)
			except ValueError:
				print(u"輸入錯誤，要求是輸入一個整數")
				continue
			numL.append(num)
			print(u"現在的串列為："),
			print(numL)
		return numL

	def getNum(self):
		print(u"現在串列為"),
		print(self.numList)
		inStr = None
		while inStr != 'EXIT':
			print(u"輸入EXIT退出程式")
			inStr = raw_input("輸入串列下標[-10,9]：")
			try:
				index = int(inStr)
				num = self.numList[index]
				print(u"串列中下標為%d的值為%d" %(index,num))
			except ValueError:
				print(u"輸入錯誤，串列下標是一個整數")
				continue
			except IndexError:
				print(u"下標太大，存取串列超出範圍")
				continue


if __name__ == '__main__':
	ti = TryInput()
