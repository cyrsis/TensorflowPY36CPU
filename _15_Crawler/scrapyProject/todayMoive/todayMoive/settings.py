# -*- coding: utf-8 -*-

# Scrapy settings for todayMoive project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'todayMoive'

SPIDER_MODULES = ['todayMoive.spiders']
NEWSPIDER_MODULE = 'todayMoive.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'todayMoive (+http://www.yourdomain.com)'

### user define
ITEM_PIPELINES = {'todayMoive.pipelines.TodaymoivePipeline':300}
