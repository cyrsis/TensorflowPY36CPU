# -*- coding: utf-8 -*-

# Scrapy settings for qiushi project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'qiushi'

SPIDER_MODULES = ['qiushi.spiders']
NEWSPIDER_MODULE = 'qiushi.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'qiushi (+http://www.yourdomain.com)'



### user define
DOWNLOADER_MIDDLEWARES = {
    'qiushi.middlewares.customMiddlewares.CustomProxy': 10,
    'qiushi.middlewares.customMiddlewares.CustomUserAgent': 30,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 20
}

ITEM_PIPELINES = {
'qiushi.pipelines.QiushiPipeline':10,
}
