#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

import platform
import os

def clear():
	OS = platform.system()
	if OS == u'Windows':
		os.system('cls')
	else:
		os.system('clear')



if __name__ == '__main__':
	pass
