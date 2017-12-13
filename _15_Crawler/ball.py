#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

import random

class SelectBall(object):
	def __init__(self):
		self.run()

	def run(self):
		while True:
			numStr = raw_input('輸入測試的次數：')
			try:
				num = int(numStr)
			except ValueError:
				print(u'要求輸入一個整數')
				continue
			else:
				break
		ball = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		for i in xrange(num):
			n = random.randint(1,10)
			ball[n-1] += 1
		for i in xrange(1,11):
			print(u'取得第%d號球的概率為%f' %(i, ball[i-1]*1.0/num))


if __name__ == '__main__':
	SB = SelectBall()
