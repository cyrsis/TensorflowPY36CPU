#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

import urllib2

def clear():
	'''該函數用於清屏 '''
	print(u'內容較多，顯示3秒後翻頁')
	time.sleep(3)
	OS = platform.system()
	if (OS == u'Windows'):
		os.system('cls')
	else:
		os.system('clear')

def linkBaidu():
	url = 'http://www.baidu.com'
	try:
		response = urllib2.urlopen(url,timeout=3)
	except urllib2.URLError:
		print(u"網路位址錯誤")
		exit()
	with open('./baidu.txt','w') as fp:
		fp.write(response.read())
	print(u"取得url訊息，response.geturl() \n: %s" %response.geturl())
	print(u"取得返回程式碼，response.getcode() \n: %s" %response.getcode())
	print(u"取得返回訊息，response.info() \n: %s" %response.info())
	print(u"取得的網頁內容已存入現在目錄的baidu.txt中，請自行查看")


if __name__ == '__main__':
	linkBaidu()
