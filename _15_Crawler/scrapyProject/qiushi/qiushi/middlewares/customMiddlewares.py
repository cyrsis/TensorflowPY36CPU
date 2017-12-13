#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'


from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

class CustomUserAgent(UserAgentMiddleware):
	def process_request(self,request,spider):
		ua = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3"
		request.headers.setdefault('User-Agent', ua)

class CustomProxy(object):
	def process_request(self,request,spider):
		request.meta['proxy'] = 'http://192.168.2.99:1080'
		
