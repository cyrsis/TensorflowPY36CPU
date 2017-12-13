#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

from myLog import MyLog

if __name__ == '__main__':
	ml = MyLog()
	ml.debug('I am debug message')
	ml.info('I am info message')
	ml.warn('I am warn message')
	ml.error('I am error message')
	ml.critical('I am critical message')
