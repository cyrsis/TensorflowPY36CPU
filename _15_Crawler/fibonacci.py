#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'


import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

print(sys.getdefaultencoding())


class Fibonacci(object):
	'''返回一個fibonacci數列 '''
	def __init__(self):
		self.fList = [0,1] #設定初始列表
		self.main()

	def main(self):
		listLen = raw_input("請輸入 fibonacci 數列的長度(3-50):")

		self.checkLen(listLen)
		while len(self.fList) < int(listLen):
			self.fList.append(self.fList[-1] + self.fList[-2])
		print(u'得到的 fibonacci 數列為:\n %s ' %self.fList)

	def checkLen(self,lenth):
		lenList = map(str,xrange(3,51))
		if lenth in lenList:
			print(u'輸入的長度表合標準，繼續執行')
		else:
			print(u'只能輸入3-50，太長了不是算不出，只是沒必要')
			exit()


if __name__ == '__main__':
	f = Fibonacci()
