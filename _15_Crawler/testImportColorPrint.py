#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

import sys

class ColorPrint(object):
	def __init__(self,color,msg):
		self.color = color
		self.msg = msg
		self.cPrint(self.color,self.msg)

	def cPrint(self,color,msg):
		colors = {
'black'	:	'\033[1;30;47m',
'red'	:	'\033[1;31;47m',
'green'	:	'\033[1;32;47m',
'yellow':	'\033[1;33;47m',
'blue'	:	'\033[1;34;47m',
'white'	:	'\033[1;37;47m'}
		if color not in colors.keys():
			print(u"輸入的顏色暫時沒有，按系統預設設定的顏色列印")
		else:
			print(u"輸入的顏色有效,開始彩色列印")
			print(u"%s" %colors[color])
			print(msg)
			print(u"\033[0m")


if __name__ == '__main__':
	cp = ColorPrint(sys.argv[1],sys.argv[2])
