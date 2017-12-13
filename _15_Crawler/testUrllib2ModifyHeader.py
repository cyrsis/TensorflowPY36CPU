#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

import urllib2
import userAgents
'''userAgents.py是個自定義的模組，位置處於現在目錄下 '''

class Urllib2ModifyHeader(object):
	'''使用urllib2模組修改header '''
	def __init__(self):
		#這個是PC + IE 的User-Agent
		PIUA = userAgents.pcUserAgent.get('IE 9.0')
		#這個是Mobile + UC的User-Agent
		MUUA = userAgents.mobileUserAgent.get('UC standard')
		#測試用的網站選擇的是有道翻譯
		self.url = 'http://fanyi.youdao.com'

		self.useUserAgent(PIUA,1)
		self.useUserAgent(MUUA,2)

	def useUserAgent(self,userAgent,name):
		request = urllib2.Request(self.url)
		request.add_header(userAgent.split(':')[0],userAgent.split(':')[1])
		response = urllib2.urlopen(request)
		fileName = str(name) + '.html'
		with open(fileName,'a') as fp:
			fp.write("%s\n\n" %userAgent)
			fp.write(response.read())

if __name__ == '__main__':
	umh = Urllib2ModifyHeader()
