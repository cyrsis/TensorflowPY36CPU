#!/usr/bin/evn python
#-*- coding: utf-8 -*-
'''
Created on 2016��8��17��

@author: hstking hstking@hotmail.com
'''

import MySQLdb

conn = MySQLdb.connect(host='192.168.2.90',
                        port=3306,
                       user='crawlUSER',
                       passwd='crawl123',
                       db='bs4DB',
                       charset='utf8')
cur = conn.cursor()
print('link mysql success')

conn.commit()
conn.close()


