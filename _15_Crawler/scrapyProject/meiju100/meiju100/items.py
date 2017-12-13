# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Meiju100Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
     storyName = scrapy.Field()
     storyState = scrapy.Field()
     tvStation = scrapy.Field()
     updateTime = scrapy.Field()
