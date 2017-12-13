#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'


import time
from myLog import MyLog
''' 這裡的myLog 是自建的模組，處於該檔案的同一目錄下'''

class TestTime(object):
	def __init__(self):
		self.log = MyLog()
		self.testTime()
		self.testLocaltime()
		self.testSleep()
		self.testStrftime()

	def testTime(self):
		self.log.info(u'開始測試time.time()函數')
		print(u'現在時間戳為：time.time() = %f' %time.time())
		print(u'這裡返回的是一個浮點型的數值，它是從1970紀元後經過的浮點秒數')
		print('\n')

	def testLocaltime(self):
		self.log.info(u'開始測試time.localtime()函數')
		print(u'現在本地時間為：time.localtime() = %s' %time.localtime())
		print(u'這裡返回的是一個struct_time結構的元組')
		print('\n')

	def testSleep(self):
		self.log.info(u'開始測試time.sleep()函數')
		print(u'這是個計時器：time.sleep(5)')
		print(u'閉上眼睛數上5秒就可以了')
		time.sleep(5)
		print('\n')

	def testStrftime(self):
		self.log.info(u'開始測試time.strftime()函數')
		print(u'這個函數返回的是一個格式化的時間')
		print('time.strftime("%%Y-%%m-%%d %%X",time.localtime()) = %s' %time.strftime("%Y-%m-%d %X",time.localtime()))
		print('\n')


if __name__ == '__main__':
	tt = TestTime()
