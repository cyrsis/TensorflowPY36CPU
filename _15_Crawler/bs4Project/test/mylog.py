#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author  :hstking
#E-mail  :hstking@hotmail.com
#Ctime   :2015/09/15
#Mtime   :
#Version :

import logging
import getpass
import sys


#### 定義MyLog類別別
class MyLog(object):
#### 類別別MyLog的構造函數
	def __init__(self):
		self.user = getpass.getuser()
		self.logger = logging.getLogger(self.user)
		self.logger.setLevel(logging.DEBUG)

####  日誌檔案名
		self.logFile = sys.argv[0][0:-3] + '.log'
		self.formatter = logging.Formatter('%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s')

####  日誌顯示到螢幕上並輸出到日誌檔案內
		self.logHand = logging.FileHandler(self.logFile, encoding='utf8')
		self.logHand.setFormatter(self.formatter)
		self.logHand.setLevel(logging.DEBUG)

		self.logHandSt = logging.StreamHandler()
		self.logHandSt.setFormatter(self.formatter)
		self.logHandSt.setLevel(logging.DEBUG)

		self.logger.addHandler(self.logHand)
		self.logger.addHandler(self.logHandSt)

####  日誌的5個級別對應以下的5個函數
	def debug(self,msg):
		self.logger.debug(msg)

	def info(self,msg):
		self.logger.info(msg)

	def warn(self,msg):
		self.logger.warn(msg)

	def error(self,msg):
		self.logger.error(msg)

	def critical(self,msg):
		self.logger.critical(msg)

if __name__ == '__main__':
	mylog = MyLog()
	mylog.debug(u"I'm debug 測試中文")
	mylog.info("I'm info")
	mylog.warn("I'm warn")
	mylog.error(u"I'm error 測試中文")
	mylog.critical("I'm critical")
