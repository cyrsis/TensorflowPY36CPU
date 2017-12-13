#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket   #socket模組

HOST='0.0.0.0'
PORT=3434

s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   #AF_INET說明使用
s.bind((HOST,PORT))   #綁定IP與通訊埠

while True:
    data, addr = s.recvfrom(1024)
    print("Received: %s from %s" % (data, str(addr)))

s.close()
