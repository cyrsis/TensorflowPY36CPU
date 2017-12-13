#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'


from meiju100.middlewares.resource import PROXIES
import random

class RandomProxy(object):
	def process_request(self,request,spider):
		proxy = random.choice(PROXIES) 
		request.meta['proxy'] = 'http://%s' %proxy
