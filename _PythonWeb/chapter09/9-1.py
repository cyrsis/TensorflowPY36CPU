#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.internet.protocol import Protocol

clients = []

class Spreader(Protocol):

    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.numProtocols = self.factory.numProtocols + 1
        self.transport.write(
            (u"歡迎來到Spread Site, 您是第%d個用戶端使用者！\n" %
            (self.factory.numProtocols,)).encode('utf8'))
        print("new connect: %d" % self.factory.numProtocols)
        clients.append(self)

    def connectionLost(self, reason):
        self.factory.numProtocols = self.factory.numProtocols - 1
        clients.remove(self)
        print("lost connect: %d" % self.factory.numProtocols)


def dataReceived(self, data):
    if data == "close":
        self.transport.loseConnection()
        for client in clients:
            if client != self:
                client.transport.write(data)



from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

class SpreadFactory(Factory):
    def __init__(self):
        self.numProtocols = 0

    def buildProtocol(self, addr):
        return Spreader(self)

# 8007是本伺服器的監聽通訊埠，建議選取大於1024的通訊埠
endpoint = TCP4ServerEndpoint(reactor, 8007)
endpoint.listen(SpreadFactory())
reactor.run()									#暫停執行
