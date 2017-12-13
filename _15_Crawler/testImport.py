#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

from testImportColorPrint import ColorPrint
#這裡的testImportColorPrint模組就是從現在目錄下導入的testImportColorPrint.py程式

if __name__ == '__main__':
	p_black = ColorPrint('black','I am black print')
	p_black = ColorPrint('red','I am red print')
	p_black = ColorPrint('green','I am green print')
	p_black = ColorPrint('yellow','I am yellow print')
	p_black = ColorPrint('blue','I am blue print')
	p_black = ColorPrint('white','I am white print')
