#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

import os
import platform
import itertools
import time

def main():
	'''主程式 '''
	global rawList #原始資料列表
	rawList = []
	global denyList #非法單詞列表
	denyList = [' ','','@']
	global pwList #最終的密碼列表
	pwList = []
	global minLen #密碼的最小長度
	minLen = 6
	global maxLen #密碼的最大長度
	maxLen = 16
	global timeout
	timeout = 3
	global flag
	flag = 0
	run = {
'0':exit,
'1':getRawList,
'2':addDenyList,
'3':clearRawList,
'4':setRawList,
'5':modifyPasswordLen,
'6':createPasswordList,
'7':showPassword,
'8':createPasswordFile
}

	while True:
		mainMenu()
		op = raw_input('輸入選項:')
		if op in map(str,range(len(run))):
			run.get(op)()
		else:
			tipMainMenuInputError()
			continue

def mainMenu():
	'''主菜單 '''
	global denyList
	global rawList
	global pwList
	global flag
	clear()
	print(u'||'),
	print(u'='*40),
	print(u'||')
	print(u'|| 0:退出程式')
	print(u'|| 1:輸入密碼原始字串')
	print(u'|| 2:新增非法字元到串列')
	print(u'|| 3:清空原始密碼串列')
	print(u'|| 4:整理原始密碼串列')
	print(u'|| 5:改變預設密碼長度(%d-%d)' %(minLen,maxLen))
	print(u'|| 6:建立密碼串列')
	print(u'|| 7:顯示所有密碼')
	print(u'|| 8:建立字典檔')
	print(u'||'),
	print(u'='*40),
	print(u'||')
	print(u'現在非法字元為：%s' %denyList)
	print(u'現在原始密碼元素為：%s' %rawList)
	print(u'共有密碼%d個' %len(pwList))
	if flag:
		print(u"已在目前的目錄建立密碼檔dic.txt")
	else:
		print(u"尚未建立密碼檔")

def clear():
	'''清屏函數 '''
	OS = platform.system()
	if (OS == u'Windows'):
		os.system('cls')
	else:
		os.system('clear')

def tipMainMenuInputError():
	'''錯誤提示 '''
	clear()
	print(u"只能輸入0-7的整數,等待%d秒後重新輸入" %timeout)
	time.sleep(timeout)

def getRawList():
	'''取得原始資料列表 '''
	clear()
	global denyList
	global rawList
	print(u"輸入換行後直接退出")
	print(u"現在原始密碼列表為:%s" %rawList)
	st = None
	while not st == '':
		st = raw_input("請輸入密碼元素字表串:")
		if st in denyList:
			print(u"這個字表串是預先設定的非法字表串")
			continue
		else:
			rawList.append(st)
			clear()
			print(u"輸入換行後直接退出")
			print(u"現在原始密碼列表為:%s" %rawList)

def addDenyList():
	'''新增非法詞 '''
	clear()
	global denyList
	print(u"輸入換行後直接退出")
	print(u"現在非法字表為:%s" %denyList)
	st = None
	while not st == '':
		st = raw_input("請輸入需要新增的非法字表串:")
		denyList.append(st)
		clear()
		print(u"輸入換行後直接退出")
		print(u"現在非法字表列表為:%s" %denyList)

def clearRawList():
	'''清空原始資料列表 '''
	global rawList
	rawList = []

def setRawList():
	'''整理原始資料列表 '''
	global rawList
	global denyList
	a = set(rawList)
	b = set(denyList)
	rawList = []
	for str in set(a - b):
		rawList.append(str)

def modifyPasswordLen():
	'''修改預設密碼的長度 '''
	clear()
	global maxLen
	global minLen
	while True:
		print(u"現在密碼長度為%d-%d" %(minLen,maxLen))
		min = raw_input("請輸入密碼最小長度:")
		max = raw_input("請輸入密碼最大長度:")
		try:
			minLen = int(min)
			maxLen = int(max)
		except ValueError:
			print(u"密碼長度只能輸入數字[6-18]")
			break
		if minLen not in xrange(6,19) or  maxLen not in xrange(6,19):
			print(u"密碼長度只能輸入數字[6-18]")
			minLen = 6
			maxLen = 16
			continue
		if minLen == maxLen:
			res = raw_input("確定將密碼長度設定為%d嗎?(Yy/Nn)" %minLen)
			if res not in list('yYnN'):
				print(u"輸入錯誤，請重新輸入")
				continue
			elif res in list('yY'):
				print(u"好吧，你確定就好")
				break
			else:
				print(u"給個機會，改一下吧")
				continue
		elif minLen > maxLen:
			print(u"最小長度比最大長度還大，可能嗎？請重新輸入")
			minLen = 6
			maxLen = 16
			continue
		else:
			print(u"設定完畢，等待%d秒後回主菜單" %timeout)
			time.sleep(timeout)
			break

def createPasswordList():
	'''建立密碼列表 '''
	global rawList
	global pwList
	global maxLen
	global minLen
	titleList = []
	swapcaseList = []
	for st in rawList:
		swapcaseList.append(st.swapcase())
		titleList.append(st.title())
	sub1 = []
	sub2 = []
	for st in set(rawList + titleList + swapcaseList):
		sub1.append(st)
	for i in xrange(2,len(sub1) + 1):
		sub2 += list(itertools.permutations(sub1,i))
	for tup in sub2:
		PW = ''
		for subPW in tup:
			PW += subPW
		if len(PW) in xrange(minLen,maxLen + 1):
			pwList.append(PW)
		else:
			pass

def showPassword():
	'''顯示建立的密碼 '''
	global pwList
	global timeout
	for i in xrange(len(pwList)):
		if i%4 == 0:
			print("%s\n" %pwList[i])
		else:
			print("%s\t" %pwList[i]),
	print('\n')
	print(u"顯示%d秒，回到主菜單" %timeout)
	time.sleep(timeout)

def createPasswordFile():
	'''建立密碼字典檔案 '''
	global flag
	global pwList
	print(u"現在目錄下建立字典檔案:dic.txt")
	time.sleep(timeout)
	with open('./dic.txt','w+') as fp:
		for PW in pwList:
			fp.write(PW)
			fp.write('\n')
	flag = 1


if __name__ == '__main__':
	main()
