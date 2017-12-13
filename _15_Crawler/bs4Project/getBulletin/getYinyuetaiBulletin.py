#!/usr/bin/evn python
#-*- coding: utf-8 -*-
'''
Created on 2016年9月1日

@author: hstking hstking@hotmail.com
'''

import mechanize
from bs4 import BeautifulSoup
from mylog import MyLog as mylog
from getHeadersFromFile import getHeaders
import codecs

class Item(object):
    title = None
    content = None


class GetBulletin(object):
    def __init__(self):
        self.url = 'http://i.yinyuetai.com/news/bulletin'
        self.log = mylog()
        self.headersFile = 'headersRaw.txt'
        self.outFile = 'bulletin.txt'

        self.spider()


    def getResponseContent(self, url):
        self.log.info('begin use mechanize module get response')
        br = mechanize.Browser()
        br.set_handle_equiv(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)

        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        headers = getHeaders(self.headersFile)
        br.addheaders = headers
        br.open(url)
        return br.response().read()


    def spider(self):
        self.log.info('beging run spider module')
        items = []
        responseContent = self.getResponseContent(self.url)
        soup = BeautifulSoup(responseContent, 'lxml')
        tags = soup.find_all('div', attrs={'class':'item_info'})
        for tag in tags:
            item = Item()
            item.title = tag.find('p', attrs={'class':'title'}).get_text().strip()
            item.content = tag.find('p', attrs={'class':'content'}).get_text().strip()
            items.append(item)
        self.pipelines(items)


    def pipelines(self, items):
        self.log.info('begin run pipeline function')
        with codecs.open(self.outFile, 'w', 'utf8') as fp:
            for item in items:
                fp.write(item.title + '\r\n')
                self.log.info(item.title)
                fp.write(item.content + '\r\n')
                self.log.info(item.content)
                fp.write('\r\n'*8)


if __name__ == '__main__':
    GB = GetBulletin()
