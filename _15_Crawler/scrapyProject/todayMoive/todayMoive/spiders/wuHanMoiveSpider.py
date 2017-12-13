# -*- coding: utf-8 -*-
import scrapy
from todayMoive.items import TodaymoiveItem


class WuhanmoiveSpider(scrapy.Spider):
    name = "wuHanMoiveSpider"
    allowed_domains = ["jycinema.com"]
    start_urls = (
        'http://www.jycinema.com/browsing/Cinemas/Details/1029',
    )

    def parse(self, response):
		subSelector = response.xpath('//div[@class="film-header"]')
		items = []
		for sub in subSelector:
			item = TodaymoiveItem()
			item['moiveName'] = sub.xpath('./a/h3/text()').extract()
			items.append(item)
		return items
