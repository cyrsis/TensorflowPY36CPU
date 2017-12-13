#!/usr/bin/evn python
#-*- coding: utf-8 -*-
'''
Created on 2016年9月10日

@author: hstking hstking@hotmail.com
'''

from selenium import webdriver
from mylog import MyLog as mylog
import os
import time

class GetCartoon(object):
    def __init__(self):
        self.startUrl = u'http://www.1kkk.com/ch1-406302/'
        self.log = mylog()
        self.browser = self.getBrowser()
        self.saveCartoon(self.browser)
        self.browser.quit()


    def getBrowser(self):
        browser = webdriver.PhantomJS()
        try:
            browser.get(self.startUrl)
        except:
            mylog.error('open the %s failed' %self.startUrl)
        browser.implicitly_wait(20)
        return browser

    def saveCartoon(self, browser):
        cartoonTitle = browser.title.split('_')[0]
        self.createDir(cartoonTitle)
        os.chdir(cartoonTitle)
        sumPage = int(self.browser.find_element_by_xpath('//font[@class="zf40"]/span[2]').text)
        i = 1
        while i<=sumPage:
            imgName = str(i) + '.png'
            browser.get_screenshot_as_file(imgName)
            self.log.info('save img %s' %imgName)
            i += 1
            NextTag = browser.find_element_by_id('next')
            NextTag.click()
#            browser.implicitly_wait(20)
            time.sleep(5)
        self.log.info('save img sccess')

    def createDir(self, dirName):
        if os.path.exists(dirName):
            self.log.error('create directory %s failed, hava a same name file or directory' %dirName)
        else:
            try:
                os.makedirs(dirName)
            except:
                self.log.error('create directory %s failed' %dirName)
            else:
                self.log.info('create directory %s success' %dirName)


if __name__ == '__main__':
    GC = GetCartoon()
