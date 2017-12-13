#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

class ShowNumType(object):
	def __init__(self):
		self.showInt()
		self.showLong()
		self.showFloat()
		self.showComplex()

	def showInt(self):
		print(u"##########顯示整數型#############")
		print(u"十進位的整數型")
		print("%-20d,%-20d,%-20d" %(-10000,0,10000))
		print(u"二進位的整數型")
		print("%-20s,%-20s,%-20s" %(bin(-10000),bin(0),bin(10000)))
		print(u"八進位的整數型")
		print("%-20s,%-20s,%-20s" %(oct(-10000),oct(0),oct(10000)))
		print(u"十六進位的整數型")
		print("%-20s,%-20s,%-20s" %(hex(-10000),hex(0),hex(10000)))

	def showLong(self):
		print(u"##########顯示長整型#############")
		print(u"十進位的整數型")
		print("%-20Ld,%-20Ld,%-20Ld" %(-10000000000000000000,0,10000000000000000000))
		print(u"八進制的整數型")
		print("%-20s,%-20s,%-20s" %(oct(-10000000000000000000),oct(0),oct(10000000000000000000)))
		print(u"十六進位的整數型")
		print("%-20s,%-20s,%-20s" %(hex(-10000000000000000000),hex(0),hex(10000000000000000000)))

	def showFloat(self):
		print(u"##########顯示浮點數型#############")
		print("%-20.10f,%-20.10f,%-20.10f" %(-100.001,0,100.001))

	def showComplex(self):
		print(u"##########顯示複數型#############")
		print(u"變數儲存值複數 var = 3 + 4j")
		var = 3 + 4j
		print(u"var的實部是：%d\tvar的虛部是：%d" %(var.real,var.imag))


if __name__ == '__main__':
	showNum = ShowNumType()
