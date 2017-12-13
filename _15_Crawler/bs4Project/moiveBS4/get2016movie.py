#!/usr/bin/evn python
#-*- coding: utf-8 -*-
'''
Created on 2016��8��13��

@author: hstking hstking@hotmail.com
'''

from bs4 import BeautifulSoup
import urllib2
import codecs
from mylog import MyLog as mylog


class MovieItem(object):
    movieName = None
    movieScore = None
    movieStarring = None

class GetMovie(object):
	'''取得電影訊息 '''
    def __init__(self):
        self.urlBase = 'http://dianying.2345.com/list/----2016---1.html'
        self.log = mylog()
        self.pages = self.getPages()
        self.urls = []  #url池
        self.items = []
        self.getUrls(self.pages) #取得抓取頁面的url
        self.spider(self.urls)
        self.pipelines(self.items)

    def getPages(self):
		'''取得總頁數 '''
        self.log.info(u'開始取得頁數')
        htmlContent = self.getResponseContent(self.urlBase)
        soup = BeautifulSoup(htmlContent, 'lxml')
        tag = soup.find('div', attrs={'class':'video_page'})
        subTags = tag.find_all('a')
        self.log.info(u'取得頁數成功')
        return int(subTags[-2].get_text())

    def getResponseContent(self, url):
		'''取得頁面返回的資料 '''
        fakeHeaders= {'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0'}
        request = urllib2.Request(url.encode('utf8'), headers=fakeHeaders)

        proxy = urllib2.ProxyHandler({'http':'http://192.168.2.99:1080'})
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        try:
            response = urllib2.urlopen(request)
        except:
            self.log.error(u'Python 返回URL:%s  資料失敗' %url)
        else:
            self.log.info(u'Python 返回URUL:%s  資料成功' %url)
            return response.read()

    def getUrls(self, pages):
        urlHead = 'http://dianying.2345.com/list/----2016---'
        urlEnd = '.html'
        for i in xrange(1,pages + 1):
            url = urlHead + str(i) + urlEnd
            self.urls.append(url)
            self.log.info(u'新增URL:%s 到URLS列表' %url)

    def spider(self, urls):
        for url in urls:
            htmlContent = self.getResponseContent(url)
            soup = BeautifulSoup(htmlContent, 'lxml')
            anchorTag = soup.find('ul', attrs={'class':'globalPicTxt pic140 clearfix'})
            tags = anchorTag.find_all('li')
            for tag in tags:
                item = MovieItem()
                item.movieName = tag.find('span', attrs={'class':'sTit'}).get_text()
                item.movieScore = tag.find('span', attrs={'class':'pRightBottom'}).em.get_text().replace(u'分', '')
                item.movieStarring = tag.find('span', attrs={'class':'sDes'}).get_text().replace(u'主演：', '')
                self.items.append(item)
                self.log.info(u'取得電影名為：<<%s>>成功' %(item.movieName))

    def pipelines(self, items):
        fileName = u'2016熱門電影.txt'.encode('GBK')
        with codecs.open(fileName, 'w', 'utf8') as fp:
            for item in items:
                fp.write('%s \t %s \t %s \r\n' %(item.movieName, item.movieScore, item.movieStarring))
                self.log.info(u'電影名為：<<%s>>已成功存入檔案"%s"...' %(item.movieName, fileName.decode('GBK')))



if __name__ == '__main__':
    GM = GetMovie()
