#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

import getpass

class FakeLogin(object):
	def __init__(self):
		self.name = 'king'
		self.password = 'haha,no pw'
		self.banner = 'hello, you have login system'
		self.run()

	def run(self):
		'''仿Linux終端登錄視窗'''
		print(u"不好意思，只有一個用戶king")
		print(u"偷偷的告訴你，密碼是6個8哦")
		while True:
			print(u"Login:king")
			pw = getpass.getpass("Password:")
			if pw == '88888888':
				print(u"%s" %self.banner)
				print(u"退出程式")
				exit()
			else:
				if len(pw) > 12:
					print(u"密碼長度應該小於12")
					continue
				elif len(pw) < 6:
					print(u"密碼長度大於6才對")
					continue
				else:
					print(u"可惜，密碼錯誤。繼續猜")
					continue


if __name__ == '__main__':
	fl = FakeLogin()
