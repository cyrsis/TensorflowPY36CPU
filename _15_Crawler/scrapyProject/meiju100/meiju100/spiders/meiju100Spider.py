# -*- coding: utf-8 -*-
import scrapy

from meiju100.items import Meiju100Item

class Meiju100spiderSpider(scrapy.Spider):
	name = "meiju100Spider"
	allowed_domains = ["meijutt.com"]
	start_urls = (
		'http://www.meijutt.com/new100.html',
	)

	def parse(self, response):
		subSelector = response.xpath('//li/div[@class="lasted-num fn-left"]')
		items = []
		for sub in subSelector:
			item = Meiju100Item()
			item['storyName'] = sub.xpath('../h5/a/text()').extract()[0]
			item['storyState'] = sub.xpath('../span[@class="state1 new100state1"]/text()').extract()[0]
			item['tvStation'] = sub.xpath('../span[@class="mjtv"]/a/text()').extract()
			item['updateTime'] = sub.xpath('../div[@class="lasted-time new100time fn-right"]/text()').extract()[0]
			items.append(item)
		return items
