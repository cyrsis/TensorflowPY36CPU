# -*- coding: utf-8 -*-

# Scrapy settings for weather project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'weather'

SPIDER_MODULES = ['weather.spiders']
NEWSPIDER_MODULE = 'weather.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'weather (+http://www.yourdomain.com)'

#### user add
ITEM_PIPELINES = {
'weather.pipelines.WeatherPipeline':1,
'weather.pipelines2json.WeatherPipeline':2,
'weather.pipelines2mysql.WeatherPipeline':3
}


