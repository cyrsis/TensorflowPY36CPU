#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

import re
import urllib2

class TodayMoive(object):
	'''取得金逸影院當日影視 '''
	def __init__(self):
		self.url = 'http://www.jycinema.com/browsing/Cinemas/Details/1029'
		self.timeout = 5
		self.fileName = './todayMoive.txt'
		'''內部變數定義完畢 '''
		self.getMoiveInfo()

	def getMoiveInfo(self):
		response = urllib2.urlopen(self.url,timeout=self.timeout)
		moiveList = re.findall('film-title.*',response.read())
		with open(self.fileName,'w') as fp:
			for moive in moiveList:
				moive = self.subStr(moive)
				print(moive.decode('utf8'))
				fp.write(moive + '\n')

	def subStr(self,st):
		st = st.replace('film-title">','')
		st = st.replace('</h3>','')
		return st


if __name__ == '__main__':
	tm = TodayMoive()
