#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

import sys

class ShowSysModule(object):
	'''這個類別用於展示python標準庫中的sys模組 '''
	def __init__(self):
		print(u'sys模組最常用的功能就是取得程式的參數')
		self.getArg()
		print(u'其次就是取得現在的系統平臺')
		self.getOs()

	def getArg(self):
		print(u'開始取得參數的個數')
		print(u'現在參數有 %d 個' %len(sys.argv))
		print(u'這些參數分別是 %s' %sys.argv)

	def getOs(self):
		print(u'sys.platform返回值對應的平臺：')
		print('System\t\t\tPlatform')
		print('Linux\t\t\tlinux2')
		print('Windows\t\t\twin32')
		print('Cygwin\t\t\tcygwin')
		print('Mac OS X\t\tdarwin')
		print('OS/2\t\t\tos2')
		print('OS/2 EMX\t\tos2emx')
		print('RiscOS\t\t\triscos')
		print('AtheOS\t\t\tatheos')
		print('\n')
		print(u'現在的系統為 %s' %sys.platform)

if __name__ == '__main__':
	ssm = ShowSysModule()
