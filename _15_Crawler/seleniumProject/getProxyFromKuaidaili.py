#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'


from selenium import webdriver
from myLog import MyLog as mylog


class Item(object):
	ip = None
	port = None
	anonymous = None
	type = None
	support = None
	local = None
	speed = None

class GetProxy(object):
	def __init__(self):
		self.startUrl = 'http://www.kuaidaili.com/proxylist/'
		self.log = mylog()
		self.urls = self.getUrls()
		self.proxyList = self.getProxyList(self.urls)
		self.fileName = 'proxy.txt'
		self.saveFile(self.fileName, self.proxyList)

	def getUrls(self):
		urls = []
		for i in xrange(1,11):
			url = self.startUrl + str(i)
			urls.append(url)
			self.log.info('get url %s to urls' %url)
		return urls

	def getProxyList(self, urls):
		browser = webdriver.PhantomJS()
		proxyList = []
		item = Item()
		for url in urls:
			browser.get(url)
			browser.implicitly_wait(5)
			elements = browser.find_elements_by_xpath('//tbody/tr')
			for element in elements:
				item.ip = element.find_element_by_xpath('./td[1]').text.encode('utf8')
				item.port = element.find_element_by_xpath('./td[2]').text.encode('utf8')
				item.anonymous = element.find_element_by_xpath('./td[3]').text.encode('utf8')
				item.type = element.find_element_by_xpath('./td[4]').text.encode('utf8')
				item.support = element.find_element_by_xpath('./td[5]').text.encode('utf8')
				item.local = element.find_element_by_xpath('./td[6]').text.encode('utf8')
				item.speed = element.find_element_by_xpath('./td[7]').text.encode('utf8')
				proxyList.append(item)
				self.log.info('add proxy %s:%s to list' %(item.ip, item.port))
		browser.quit()
		return proxyList

	def saveFile(self, fileName, proxyList):
		self.log.info('add all proxy to %s' %fileName)
		with open(fileName, 'w') as fp:
			for item in proxyList:
				fp.write(item.ip + '\t')
				fp.write(item.port + '\t')
				fp.write(item.anonymous + '\t')
				fp.write(item.type + '\t')
				fp.write(item.support + '\t')
				fp.write(item.local + '\t')
				fp.write(item.speed + '\n')
				

if __name__ == '__main__':
	GP = GetProxy()
