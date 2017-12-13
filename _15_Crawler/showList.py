#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

class ShowList(object):
	def __init__(self):
		self.L1 = []
		self.L2 = []

		self.createList()
		self.insertData()
		self.appendData()
		self.deleteData()
		self.subList()

	def createList(self):
		print(u"建立串列")
		print("L1 = list('abcdefg')")
		self.L1 = list('abcdefg')
		print("L2 = []")
		print("for i in xrange(0,10):")
		print("\tL2.append(i)")
		for i in xrange(0,10):
			self.L2.append(i)
		print("L1 = "),
		print(self.L1)
		print("L2 = "),
		print(self.L2)
		print('\n')

	def insertData(self):
		print(u"插入資料")
		print(u"L1串列中第3 個位置插入數字100，執行指令：L1.insert(3,100)")
		self.L1.insert(3,100)
		print("L1 = "),
		print(self.L1)
		print(u"L2串列中第10 個位置插入字串'python'，執行指令：L2.insert(10,'python')")
		self.L2.insert(10,'python')
		print("L2 = "),
		print(self.L2)
		print('\n')

	def appendData(self):
		print(u"追加資料")
		print(u"L1串列尾追加一個串列[1,2,3]，執行指令L1.append([1,2,3]")
		self.L1.append([1,2,3])
		print("L1 = "),
		print(self.L1)
		print(u"L2串列尾追加一個tuple('a','b','c')，執行指令L1.append(('a','b','c')")
		self.L2.append(('a','b','c'))
		print("L2 = "),
		print(self.L2)
		print('\n')

	def deleteData(self):
		print(u"刪除資料")
		print(u"刪除L1 的最後一個元素，執行指令L1.pop()")
		self.L1.pop()
		print("L1 = "),
		print(self.L1)
		print(u"刪除L1 的第1 個元素，執行指令L1.pop(0)")
		self.L1.pop(0)
		print("L1 = "),
		print(self.L1)
		print(u"刪除L2 的第4 個元素，執行指令L1.pop(3)")
		self.L2.pop(3)
		print("L2 = "),
		print(self.L2)
		print('\n')

	def subList(self):
		print(u"串列切片")
		print(u"取串列L1 的第3 到最後一個元素組成的新串列，執行指令L1[2:]")
		print(self.L1[2:])
		print(u"取串列L2 的第2 個到倒數第2 個元素組成的新串列，步長為2，執行指令L2[1:-1:2]")
		print(self.L2[1:-1:2])
		print('\n')


if __name__ == '__main__':
	print(u"示範串列操作：\n")
	sl = ShowList()
