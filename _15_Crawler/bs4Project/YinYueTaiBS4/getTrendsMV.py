#!/usr/bin/evn python
#-*- coding: utf-8 -*-
'''
Created on 2016��8��10��

@author: hstking hstking@hotmail.com
'''

from bs4 import BeautifulSoup
import urllib2
import codecs
import time
from mylog import MyLog as mylog
import resource
import random

class Item(object):
    top_num = None  #排名
    score = None  #打分
    mvName = None  #MV名字
    singer = None  #演唱者
    releasTime = None  #釋放時間


class GetMvList(object):
    '''The all data from www.yinyuetai.com
	所有資料都來自www.yinyuetai.com
    '''
    def __init__(self):
        self.urlBase = 'http://vchart.yinyuetai.com/vchart/trends?'
        self.areasDic = {'ML':'Mainland','HT':'Hongkong&Taiwan','US':'Americ','KR':'Korea','JP':'Japan'}
        self.log = mylog()
        self.getUrls()


    def getUrls(self):
		'''取得url池 '''
        areas = ['ML','HT','US','KR','JP']
        pages = [str(i) for i in range(1,4)]
        for area in areas:
            urls = []
            for page in pages:
                urlEnd = 'area=' + area + '&page=' + page
                url = self.urlBase + urlEnd
                urls.append(url)
                self.log.info(u'新增URL:%s 到URLS' %url)
            self.spider(area, urls)



    def getResponseContent(self, url):
		'''從頁面返回資料 '''
        fakeHeaders = {'User-Agent':self.getRandomHeaders()}
        request = urllib2.Request(url.encode('utf8'), headers=fakeHeaders)

        proxy = urllib2.ProxyHandler({'http':'http://'+self.getRandomProxy()})
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        try:
            response = urllib2.urlopen(request)
            time.sleep(1)
        except:
            self.log.error(u'Python 返回URL:%s  資料失敗' %url)
            return ''
        else:
            self.log.info(u'Python 返回URUL:%s  資料成功' %url)
            return response.read()

    def spider(self,area,urls):
        items = []
        for url in urls:
            responseContent = self.getResponseContent(url)
            if not responseContent:
                continue
            soup = BeautifulSoup(responseContent, 'lxml')
            tags = soup.find_all('li', attrs={'name':'dmvLi'})
            for tag in tags:
                item = Item()
                item.top_num = tag.find('div', attrs={'class':'top_num'}).get_text()
                if tag.find('h3', attrs={'class':'desc_score'}):
                    item.score = tag.find('h3', attrs={'class':'desc_score'}).get_text()
                else:
                    item.score = tag.find('h3', attrs={'class':'asc_score'}).get_text()

                item.mvName = tag.find('img').get('alt')
                item.singer = tag.find('a', attrs={'class':'special'}).get_text()
                item.releaseTime = tag.find('p', attrs={'class':'c9'}).get_text()
                items.append(item)
                self.log.info(u'新增mvName為<<%s>>的資料成功' %(item.mvName))
        self.pipelines(items, area)


    def getRandomProxy(self):  #隨機選取proxy代理
        return random.choice(resource.PROXIES)

    def getRandomHeaders(self):  #隨機選取檔案頭
        return random.choice(resource.UserAgents)


    def pipelines(self, items, area):  #處理取得的資料
        fileName = 'mvTopList.txt'
        nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        with codecs.open(fileName, 'a', 'utf8') as fp:
            fp.write('%s -------%s\r\n' %(self.areasDic.get(area), nowTime))
            for item in items:
                fp.write('%s %s \t %s \t %s \t %s \r\n'
                         %(item.top_num, item.score, item.releaseTime, item.singer, item.mvName))
                self.log.info(u'新增mvName為<<%s>>的MV到%s...' %(item.mvName, fileName))
            fp.write('\r\n'*4)


if __name__ == '__main__':
    GML = GetMvList()
