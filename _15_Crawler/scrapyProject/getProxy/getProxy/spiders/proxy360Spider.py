# -*- coding: utf-8 -*-
import scrapy
from getProxy.items import GetproxyItem

class Proxy360Spider(scrapy.Spider):
	name = "proxy360Spider"
	allowed_domains = ["proxy360.com"]
	nations = ['Brazil','China','America','Taiwan','Japan','Thailand','Vietnam','bahrein']
	start_urls = []
	for nation in nations:
		start_urls.append('http://www.proxy360.cn/Region/' + nation)
		

	def parse(self, response):
		subSelector = response.xpath('//div[@class="proxylistitem" and @name="list_proxy_ip"]')
		items = []
		for sub in subSelector:
			item = GetproxyItem()
			item['ip'] = sub.xpath('.//span[1]/text()').extract()[0]
			item['port'] = sub.xpath('.//span[2]/text()').extract()[0]
			item['type'] = sub.xpath('.//span[3]/text()').extract()[0]
			item['loction'] = sub.xpath('.//span[4]/text()').extract()[0]
			item['protocol'] = 'HTTP'
			item['source'] = 'proxy360'
			items.append(item)
		return items
