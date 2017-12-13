#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.internet.protocol import DatagramProtocol


class Echo(DatagramProtocol):  # 定義DatagramProtocol子類別
    def datagramReceived(self, data, host, port):
        print("Got data from: %s:%d" % (host, port))
        print(data.decode('utf8'))


protocol = Echo()  # 案例化Protocol子類別

from twisted.internet import reactor
import threading
import time
import sys
import datetime

host = "127.0.0.1"
port = 8007

bStop = False


def routine():  # 每隔5秒向伺服器傳送訊息
    while not bStop:
        protocol.transport.write("hello, I'm %s %s" %
                                 (sys.argv[1], datetime.datetime.now()), (host, port))
        time.sleep(5)


threading.Thread(target=routine).start()
reactor.listenUDP(port, protocol)
reactor.run()  # 暫停執行
bStop = True
