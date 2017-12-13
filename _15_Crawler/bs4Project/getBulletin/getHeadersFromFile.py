#!/usr/bin/evn python
#-*- coding: utf-8 -*-
'''
Created on 2016��9��1��

@author: hstking hstking@hotmail.com
'''


def getHeaders(fileName):
    headers = []
    headerList = ['User-Agent', 'Cookie']
    with open(fileName, 'r') as fp:
        for line in fp.readlines():
            name, value = line.split(':', 1)
            if name in headerList:
                headers.append((name.strip(), value.strip()))
    return headers

if __name__ == '__main__':
    headers = getHeaders('headersRaw.txt')
    print headers