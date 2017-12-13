#!/usr/bin/evn python
#-*- coding: utf-8 -*-
'''
Created on 2016��8��17��

@author: hstking hstking@hotmail.com
'''

import MySQLdb

class SavebooksData(object):
    def __init__(self,items):
        self.host = '192.168.2.90'
        self.port = 3306
        self.user = 'crawlUSER'
        self.passwd = 'crawl123'
        self.db = 'bs4DB'
        
        self.run(items)
        
    def run(self, items):
        conn = MySQLdb.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               passwd=self.passwd,
                               db=self.db,
                               charset='utf8')
        cur = conn.cursor()
        for item in items:
            cur.execute("INSERT INTO qiDianBooks(categoryName, bookName, wordsNum, updateTime, authorName) values(%s, %s, %s, %s, %s)", (item.categoryName, item.bookName, item.wordsNum, item.updateTime, item.authorName))
        cur.close()
        conn.commit()
        conn.close()


if __name__ == '__main__':
    pass
