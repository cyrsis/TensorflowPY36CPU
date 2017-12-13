# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time

class Meiju100Pipeline(object):
	def process_item(self, item, spider):
		today = time.strftime('%Y%m%d', time.localtime())
		fileName = today + 'meiju.txt'
		with open(fileName, 'a') as fp:
			fp.write("%s \t" %(item['storyName'].encode('utf8')))
			fp.write("%s \t" %(item['storyState'].encode('utf8')))
			if len(item['tvStation']) == 0:
				fp.write("unknow \t")
			else:
				fp.write("%s \t" %(item['tvStation'][0]).encode('utf8'))
			fp.write("%s \n" %(item['updateTime'].encode('utf8')))
		return item
