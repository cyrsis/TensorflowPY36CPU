#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

class ShowTuple(object):
	def __init__(self):
		self.T1 = ()
		self.createTuple()
		self.subTuple(self.T1)
		self.tuple2List(self.T1)

	def createTuple(self):
		print(u"建立tuple：")
		print(u"T1 = (1,2,3,4,5,6,7,8,9,10)")
		self.T1 = (1,2,3,4,5,6,7,8,9,10)
		print(u"T1 = "),
		print(self.T1)
		print('\n')

	def subTuple(self,Tuple):
		print(u"tuple分片：")
		print(u"取tuple T1 的第4 個到最後一個tuple 組成的新tuple，執行指令T1[3:]")
		print(self.T1[3:])
		print(u"取tuple T1 的第2 個到倒數第2 個元素組成的新tuple，步長為2，執行指令T1[1:-1:2]")
		print(self.T1[1:-1:2])
		print('\n')

	def tuple2List(self,Tuple):
		print(u"tuple 轉換成串列：")
		print(u"顯示tuple")
		print(u"T1 = "),
		print(self.T1)
		print(u"執行指令 L2 = list(T1)")
		L2 = list(self.T1)
		print(u"顯示串列")
		print(u"L2 = "),
		print(L2)
		print(u"串列追加一個元素100 後，轉換成tuple。執行指令L2.append(100) tuple(L2)")
		L2.append(100)
		print(u"顯示新tuple")
		print(tuple(L2))


if __name__ == '__main__':
	st = ShowTuple()
