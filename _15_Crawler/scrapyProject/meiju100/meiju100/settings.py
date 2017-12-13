# -*- coding: utf-8 -*-

# Scrapy settings for meiju100 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'meiju100'

SPIDER_MODULES = ['meiju100.spiders']
NEWSPIDER_MODULE = 'meiju100.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'meiju100 (+http://www.yourdomain.com)'


### user define
ITEM_PIPELINES = {
'meiju100.pipelines.Meiju100Pipeline':10
}

DOWNLOADER_MIDDLEWARES = {
'meiju100.middlewares.customProxy.RandomProxy':10,
'meiju100.middlewares.customUserAgent.RandomUserAgent':30,
'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 20
}


