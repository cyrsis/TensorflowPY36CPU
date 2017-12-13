#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'


from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

class CustomUserAgent(UserAgentMiddleware):
	def process_request(self,request,spider):
		ua = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML,     like Gecko)"
		request.headers.setdefault('User-Agent', ua)
