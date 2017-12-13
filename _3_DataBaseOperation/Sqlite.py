#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import MySQLdb				#引入Python引擎包

# 連線本機資料庫testDB
#conn = MySQLdb.connect(database="testDB", user="user1", password="password123",
#                         host="127.0.0.1", port=3306)

import os
if os.path.exists('test.db'):
    os.remove('test.db')

import sqlite3
conn = sqlite3.connect('test.db')

#取得游標物件
cur = conn.cursor()

#執行一系列SQL敘述
#建立一個表
cur.execute("CREATE TABLE demo(num int,str varchar(20));")
# 插入一些記錄
cur.execute("INSERT INTO demo VALUES (%d, '%s')" % (1, 'aaa'))
cur.execute("INSERT INTO demo VALUES (%d, '%s')" % (2, 'bbb'))
cur.execute("INSERT INTO demo VALUES (%d, '%s')" % (3, 'ccc'))

#更新一條記錄
cur.execute("UPDATE demo SET str='%s' WHERE num = %d" % ('ddd', 3))

#查詢
cur.execute("SELECT * FROM demo;")
rows = cur.fetchall()
print("number of records: ", len(rows))
for i in rows:
    print(i)

#傳送交易
conn.commit()

#關閉游標物件
cur.close()

#關閉資料庫連線
conn.close()
