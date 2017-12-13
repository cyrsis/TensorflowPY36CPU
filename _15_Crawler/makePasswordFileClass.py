#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

import os
import platform
import itertools
import time

class MakePassword(object):
	def __init__(self):
		self.rawList = []
		self.denyList = ['',' ','@']
		self.pwList = []
		self.minLen = 6
		self.maxLen = 16
		self.timeout = 3
		self.flag = 0
		self.run = {
'0':exit,
'1':self.getRawList,
'2':self.addDenyList,
'3':self.clearRawList,
'4':self.setRawList,
'5':self.modifyPasswordLen,
'6':self.createPasswordList,
'7':self.showPassword,
'8':self.createPasswordFile
}
		self.main()

	def main(self):
		while True:
			self.mainMenu()
			op = raw_input('輸入選項:')
			if op in map(str,range(len(self.run))):
				self.run.get(op)()
			else:
				self.tipMainMenuInputError()
				continue

	def mainMenu(self):
		self.clear()
		print(u'||'),
		print(u'='*40),
		print(u'||')
		print(u'|| 0:退出程式')
		print(u'|| 1:輸入密碼原始字串')
		print(u'|| 2:新增非法字元到串列')
		print(u'|| 3:清空原始密碼串列')
		print(u'|| 4:整理原始密碼串列')
		print(u'|| 5:改變預設密碼長度(%d-%d)' %(self.minLen,self.maxLen))
		print(u'|| 6:建立密碼串列')
		print(u'|| 7:顯示所有密碼')
		print(u'|| 8:建立字典檔')
		print(u'||'),
		print(u'='*40),
		print(u'||')
		print(u'現在非法字元為：%s' %self.denyList)
		print(u'現在原始密碼元素為：%s' %self.rawList)
		print(u'共有密碼%d個' %len(self.pwList))
		if self.flag:
			print(u"已在目前的目錄建立密碼檔dic.txt")
		else:
			print(u"尚未建立密碼檔")

	def clear(self):
		OS = platform.system()
		if (OS == u'Windows'):
			os.system('cls')
		else:
			os.system('clear')

	def tipMainMenuInputError(self):
		self.clear()
		print(u"只能輸入0-7的整數,等待%d秒後重新輸入" %timeout)
		time.sleep(timeout)

	def getRawList(self):
		self.clear()
		print(u"輸入換行後直接退出")
		print(u"現在原始密碼列表為:%s" %self.rawList)
		st = None
		while not st == '':
			st = raw_input("請輸入密碼元素字表串:")
			if st in self.denyList:
				print(u"這個字表串是預先設定的非法字表串")
				continue
			else:
				self.rawList.append(st)
				self.clear()
				print(u"輸入換行後直接退出")
				print(u"現在原始密碼列表為:%s" %self.rawList)

	def addDenyList(self):
		self.clear()
		print(u"輸入換行後直接退出")
		print(u"現在非法字表為:%s" %self.denyList)
		st = None
		while not st == '':
			st = raw_input("請輸入需要新增的非法字表串:")
			self.denyList.append(st)
			self.clear()
			print(u"輸入換行後直接退出")
			print(u"現在非法字表列表為:%s" %self.denyList)

	def clearRawList(self):
		self.rawList = []

	def setRawList(self):
		a = set(self.rawList)
		b = set(self.denyList)
		self.rawList = []
		for str in set(a - b):
			self.rawList.append(str)

	def modifyPasswordLen(self):
		self.clear()
		while True:
			print(u"現在密碼長度為%d-%d" %(self.minLen,self.maxLen))
			min = raw_input("請輸入密碼最小長度:")
			max = raw_input("請輸入密碼最大長度:")
			try:
				self.minLen = int(min)
				self.maxLen = int(max)
			except ValueError:
				print(u"密碼長度只能輸入數字[6-18]")
				break
			if self.minLen not in xrange(6,19) or  self.maxLen not in xrange(6,19):
				print(u"密碼長度只能輸入數字[6-18]")
				self.minLen = 6
				self.maxLen = 16
				continue
			if self.minLen == self.maxLen:
				res = raw_input("確定將密碼長度設定為%d嗎?(Yy/Nn)" %self.minLen)
				if res not in list('yYnN'):
					print(u"輸入錯誤，請重新輸入")
					continue
				elif res in list('yY'):
					print(u"好吧，你確定就好")
					break
				else:
					print(u"給個機會，改一下吧")
					continue
			elif self.minLen > self.maxLen:
				print(u"最小長度比最大長度還大，可能嗎？請重新輸入")
				self.minLen = 6
				self.maxLen = 16
				continue
			else:
				print(u"設定完畢，等待%d秒後回主菜單" %self.timeout)
				time.sleep(self.timeout)
				break

	def createPasswordList(self):
		titleList = []
		swapcaseList = []
		for st in self.rawList:
			swapcaseList.append(st.swapcase())
			titleList.append(st.title())
		sub1 = []
		sub2 = []
		for st in set(self.rawList + titleList + swapcaseList):
			sub1.append(st)
		for i in xrange(2,len(sub1) + 1):
			sub2 += list(itertools.permutations(sub1,i))
		for tup in sub2:
			PW = ''
			for subPW in tup:
				PW += subPW
			if len(PW) in xrange(self.minLen,self.maxLen + 1):
				self.pwList.append(PW)
			else:
				pass

	def showPassword(self):
		for i in xrange(len(self.pwList)):
			if i%4 == 0:
				print("%s\n" %self.pwList[i])
			else:
				print("%s\t" %self.pwList[i]),
		print('\n')
		print(u"顯示%d秒，回到主菜單" %self.timeout)
		time.sleep(self.timeout)

	def createPasswordFile(self):
		print(u"現在目錄下建立字典檔案:dic.txt")
		time.sleep(self.timeout)
		with open('./dic.txt','w+') as fp:
			for PW in self.pwList:
				fp.write(PW)
				fp.write('\n')
		self.flag = 1


if __name__ == '__main__':
	mp = MakePassword()
