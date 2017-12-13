#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.internet.protocol import DatagramProtocol
from sys import stdout

host = "127.0.0.1"
port = 8007

class Echo(DatagramProtocol):							#定義DatagramProtocol子類別
    def startProtocol(self):							#連線成功後被呼叫
        self.transport.connect(host, port)					#指定對方位址/通訊埠
        print "Connection created!"
        
    def datagramReceived(self, data):					#收到資料時被呼叫
        print data.decode('utf8')

    def connectionRefused(self):						#每次通訊失敗後被呼叫
        print "sent failed!"

    def stopProtocol(self):
        print "Connection closed!"


protocol = Echo()

from twisted.internet import reactor
import threading, time, sys, datetime

bStop = False
def routine(factory):
while not bStop:
	   #傳送資料時只需傳入資料，而無需傳入對方位址/通訊埠
        protocol.transport.write("hello, I'm %s %s" % (sys.argv[1], datetime.datetime.now()))
        time.sleep(5)

threading.Thread(target=routine, args=(factory,)).start()
reactor.listenUDP(port, Echo())
reactor.run()
bStop = True
