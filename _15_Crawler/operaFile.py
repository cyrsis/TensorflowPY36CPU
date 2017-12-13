#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

import os

def operaFile():
	print(u'建立一個名字為test.txt的檔案，並在其中寫入Hello Python')
	print(u'先得保證test.txt不存在')
	os.system('rm test.txt')
	os.system('ls -l test.txt')
	print(u'現在再來建立檔案並寫入內容\n')
	fp = open('test.txt', 'w')
	fp.write('Hello Python')
	fp.close()
	print(u'不要忘記用close關閉檔案哦')
	print(u'再來看看test.txt是否存在，和內容\n')
	os.system('ls -l test.txt')
	os.system('cat test.txt')
	print('\n')

	print(u'如何避免open檔案失敗的問題呢？')
	print(u'使用with as就可以了')
	with open('test.txt', 'r') as fp:
		st = fp.read()
	print('test.txt的內容為:%s' %st)

if __name__ == '__main__':
	operaFile()
