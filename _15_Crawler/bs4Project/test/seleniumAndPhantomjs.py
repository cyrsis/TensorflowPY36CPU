#!/usr/bin/evn python
#-*- coding: utf-8 -*-
'''
Created on 2016年9月6日

@author: hstking hstking@hotmail.com
'''

from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS()
driver.get('http://comic.kukudm.com/comiclist/2110/49749/1.htm')
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
#print soup.current_data
print type(soup.prettify())
#print soup.contents

#print html
with open('1.html', 'w') as fp:
    fp.write(soup.prettify(encoding='utf8'))
print('aaaa')
#    for co in soup.contents:
#        print type(co)
#        fp.write(c)

#data = driver.find_element_by_xpath('//div[@class="main" and @id="mainView"]/ul')
#print data.text
#data.screenshot('1.png')
#driver.get_screenshot_as_file('2.png')

#xx = data.screenshot_as_png

driver.close()

#if __name__ == '__main__':
#    pass
