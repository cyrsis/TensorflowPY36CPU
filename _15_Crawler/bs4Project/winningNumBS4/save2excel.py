#!/usr/bin/evn python
#-*- coding: utf-8 -*-
'''
Created on 2016��8��17��

@author: hstking hstking@hotmail.com
'''

import xlwt


class SavaBallDate(object):
    def __init__(self, items):
        self.items = items
        self.run(self.items)
        
    def run(self,items):
        fileName = u'雙色球.xls'.encode('GBK')
        book = xlwt.Workbook(encoding='utf8')
        sheet=book.add_sheet('ball', cell_overwrite_ok=True)
        sheet.write(0, 0, u'開獎日期'.encode('utf8'))
        sheet.write(0, 1, u'期號'.encode('utf8'))
        sheet.write(0, 2, u'紅1'.encode('utf8'))
        sheet.write(0, 3, u'紅2'.encode('utf8'))
        sheet.write(0, 4, u'紅3'.encode('utf8'))
        sheet.write(0, 5, u'紅4'.encode('utf8'))
        sheet.write(0, 6, u'紅5'.encode('utf8'))
        sheet.write(0, 7, u'紅6'.encode('utf8'))
        sheet.write(0, 8, u'藍'.encode('utf8'))
        sheet.write(0, 9, u'銷售金額'.encode('utf8'))
        sheet.write(0, 10, u'一等獎'.encode('utf8'))
        sheet.write(0, 11, u'二等獎'.encode('utf8'))
        i = 1
        while i <= len(items):
            item = items[i-1]
            sheet.write(i, 0, item.date)
            sheet.write(i, 1, item.order)
            sheet.write(i, 2, item.red1)
            sheet.write(i, 3, item.red2)
            sheet.write(i, 4, item.red3)
            sheet.write(i, 5, item.red4)
            sheet.write(i, 6, item.red5)
            sheet.write(i, 7, item.red6)
            sheet.write(i, 8, item.blue)
            sheet.write(i, 9, item.money)
            sheet.write(i, 10, item.firstPrize)
            sheet.write(i, 11, item.secondPrize)
            i += 1
        book.save(fileName)
        


if __name__ == '__main__':
    pass
