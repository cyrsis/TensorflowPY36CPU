#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

import random

class GuessNum(object):
	'''這個類用於猜亂數 '''
	def __init__(self):
		print(u"隨機產生一個0-100 的亂數")
		self.num = random.randint(0,101)
		self.guess()

	def guess(self):
		i = 0
		while True:
			print(u"猜這個亂數，0-100")
			strNum = raw_input("輸入你猜的數字:")
			i += 1
			try:
				print("****************")
				if int(strNum) < self.num:
					print(u"你猜得太小了")
					continue
				elif int(strNum) > self.num:
					print(u"你猜得太大了")
					continue
				else:
					print(u"你總算是猜對了")
					print(u"你總共猜了%d次" %i)
					break
			except ValueError:
				print(u"只能輸入數字，繼續猜吧")
				continue
			print(u"如果沒有continue或break，就會顯示這個，要不要試試？")


if __name__ == '__main__':
	gn = GuessNum()
