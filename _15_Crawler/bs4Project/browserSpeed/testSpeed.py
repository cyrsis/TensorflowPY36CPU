#!/usr/bin/evn python
#-*- coding: utf-8 -*-
'''
Created on 2016��9��7��

@author: hstking hstking@hotmail.com
'''

from selenium import webdriver
import time

class TestBrowserSpeed(object):
    def __init__(self, num):
        self.browsers = ['PhantomJS', 'Chrome', 'Firefox', 'Ie', 'Edge']
        self.url = 'https://www.baidu.com'
        self.num = num
        self.testBrowser(self.num)
        
    def testBrowser(self, num):
        for browser in self.browsers:
            eval('self.run_browser_%s'%browser)
        
    def run_browser_PhantomJS(self):
        driver = webdriver.PhantomJS()
        self.linkUrl(driver)
    
    def run_browser_Chrome(self):
        driver = webdriver.Chrome(executable_path='')
        pass
    
    def run_browser_Firefox(self):
        pass
    
    def run_browser_Ie(self):
        pass
    
    def run_browser_Edge(self):
        pass
    
    def linkUrl(self, driver):
        pass
        
        

if __name__ == '__main__':
    TBS = TestBrowserSpeed(5)
