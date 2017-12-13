#!/usr/bin/evn python
#-*- coding: utf-8 -*-
'''
Created on 2016年8月9日

@author: hstking hstking@hotmail.com
'''


import urllib.request
import BeautifulSoup4
from mylog import MyLog as mylog


class Item(object):
    title = None    #帖子標題
    firstAuthor = None  #帖子建立者
    firstTime = None   #帖子建立時間
    reNum = None    #總回覆數
    content = None  #最後回覆內容
    lastAuthor = None   #最後回覆者
    lastTime = None #最後回覆時間


class GetTiebaInfo(object):
    def __init__(self,url):
        self.url = url
        self.log = mylog()
        self.pageSum = 5
        self.urls = self.getUrls(self.pageSum)
        self.items = self.spider(self.urls)
        self.pipelines(self.items)

    def getUrls(self,pageSum):
        urls = []
        pns = [str(i*50) for i in range(pageSum)]
        ul = self.url.split('=')
        for pn in pns:
            ul[-1] = pn
            url = '='.join(ul)
            urls.append(url)
        self.log.info(u'取得URLS成功')
        return urls

    def spider(self, urls):
        items = []
        for url in urls:
            htmlContent = self.getResponseContent(url)
            soup = BeautifulSoup(htmlContent, 'lxml')
            tagsli = soup.find_all('li',attrs={'class':' j_thread_list clearfix'})
            for tag in tagsli:
                item = Item()
                item.title = tag.find('a', attrs={'class':'j_th_tit'}).get_text().strip()
                item.firstAuthor = tag.find('span', attrs={'class':'frs-author-name-wrap'}).a.get_text().strip()
                item.firstTime = tag.find('span', attrs={'title':u'建立時間'.encode('utf8')}).get_text().strip()
                item.reNum = tag.find('span', attrs={'title':u'回覆'.encode('utf8')}).get_text().strip()
                item.content = tag.find('div', attrs={'class':'threadlist_abs threadlist_abs_onlyline '}).get_text().strip()
                item.lastAuthor = tag.find('span', attrs={'class':'tb_icon_author_rely j_replyer'}).a.get_text().strip()
                item.lastTime = tag.find('span', attrs={'title':u'最後回覆時間'.encode('utf8')}).get_text().strip()
                items.append(item)
                self.log.info(u'取得標題為<<%s>>的項成功 ...' %item.title)
        return items

    def pipelines(self, items):
        fileName = u'百度貼吧_權利的遊戲.txt'.encode('GBK')
        with open(fileName, 'w') as fp:
            for item in items:
                fp.write('title:%s \t author:%s \t firstTime:%s \n content:%s \n return:%s \n lastAuthor:%s \t lastTime:%s \n\n\n\n'
                         %(item.title.encode('utf8'),item.firstAuthor.encode('utf8'),item.firstTime.encode('utf8'),item.content.encode('utf8'),item.reNum.encode('utf8'),item.lastAuthor.encode('utf8'),item.lastTime.encode('utf8')))
                self.log.info(u'標題為<<%s>>的項輸入到"%s"成功' %(item.title, fileName.decode('GBK')))

    def getResponseContent(self, url):
        '''這裡單獨使用一個函數返回頁面返回值，是為了後期方便的加入proxy和headers等
        '''
        try:
            response = urllib2.urlopen(url.encode('utf8'))
        except:
            self.log.error(u'Python 返回URL:%s  資料失敗' %url)
        else:
            self.log.info(u'Python 返回URUL:%s  資料成功' %url)
            return response.read()


if __name__ == '__main__':
    url = u'http://tieba.baidu.com/f?kw=權利的遊戲&ie=utf-8&pn=50'
    GTI = GetTiebaInfo(url)