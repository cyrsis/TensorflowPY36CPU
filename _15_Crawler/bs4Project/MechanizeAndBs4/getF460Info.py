#!/usr/bin/evn python
#-*- coding: utf-8 -*-
'''
Created on 2016年8月25日

@author: hstking hstking@hotmail.com
'''

import mechanize
from bs4 import BeautifulSoup
from mylog import MyLog as mylog


class F460Info(object):
    '''取得光貓f460的訊息 '''
    def __init__(self):
        self.url = 'http://192.168.1.125/'
        self.log = mylog()
        self.username = 'admin'
        self.password = '******'
        self.spider()


    def spider(self):
        responseContent = self.getResponseContent(self.url)
        if not responseContent:
            self.log.error('the response is null')
            exit()
        soup = BeautifulSoup(responseContent, 'lxml')
        modemInfo = {}
        modemInfo['CarrierName'] = soup.find('td', attrs={'id':'Frm_CarrierName'}).get_text().strip()
        modemInfo['modelName'] = soup.find('td', attrs={'id':'Frm_ModelName'}).get_text().strip()
        modemInfo['SerialNumber'] = soup.find('td', attrs={'id':'Frm_SerialNumber'}).get_text().strip()
        modemInfo['HardwareVer'] = soup.find('td', attrs={'id':'Frm_HardwareVer'}).get_text().strip()
        modemInfo['SoftwareVer'] = soup.find('td', attrs={'id':'Frm_SoftwareVer'}).get_text().strip()
        modemInfo['BootVer'] = soup.find('td', attrs={'id':'Frm_BootVer'}).get_text().strip()
        modemInfo['VerDate'] = soup.find('td', attrs={'id':'Frm_VerDate'}).get_text().strip()

        self.pipeline(modemInfo)


    def getResponseContent(self, url):
        self.log.info(u'begin create mechanize browser')
        br = mechanize.Browser()
        br.set_handle_equiv(True)
        br.set_handle_gzip(False)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36')]

        self.log.info(u'open url on mechanize browser')
        try:
            br.open(url)
        except:
            self.log.error(u'open %s failed' %url)
            return ''
        br.select_form(nr=0)
        br.form['Username'] = self.username
        br.form['Password'] = self.password
        br.submit()

        newUrl = url + 'template.gch'
        try:
            br.open(newUrl)
        except:
            self.log.error(u'open %s failed' %newUrl)
            return ''
        else:
            return br.response().read()


    def pipeline(self, info):
        fileName = u'f460ModemInfo.txt'.encode('gbk')
        with open(fileName, 'w') as fp:
            for key in info.keys():
                print('%s \t %s \n' %(key.encode('utf8'), info.get(key).encode('utf8')))
                fp.write('%s \t %s \n' %(key.encode('utf8'), info.get(key).encode('utf8')))


if __name__ == '__main__':
    fi = F460Info()
