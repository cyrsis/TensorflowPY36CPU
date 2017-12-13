#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

import logging
import getpass
import sys


# 定義MyLog類別
class MyLog(object):
	'''這個類別用於建立一個自用的log '''
	def __init__(self): #類別MyLog的構造函數
		user = getpass.getuser()
		self.logger = logging.getLogger(user)
		self.logger.setLevel(logging.DEBUG)
		logFile = './' + sys.argv[0][0:-3] + '.log' #日誌檔案名
		formatter = logging.Formatter('%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s')

		'''日誌顯示到螢幕上並輸出到日誌檔案內'''
		logHand = logging.FileHandler(logFile)
		logHand.setFormatter(formatter)
		logHand.setLevel(logging.ERROR) #只有錯誤才會被記錄到logfile中

		logHandSt = logging.StreamHandler()
		logHandSt.setFormatter(formatter)

		self.logger.addHandler(logHand)
		self.logger.addHandler(logHandSt)

	''' 日誌的5個級別對應以下的5個函數 '''
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
	mylog.debug("I'm debug")
	mylog.info("I'm info")
	mylog.warn("I'm warn")
	mylog.error("I'm error")
	mylog.critical("I'm critical")
