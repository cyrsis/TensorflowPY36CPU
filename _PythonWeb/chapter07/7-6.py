#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import tornado.websocket

from tornado.options import define, options, parse_command_line

define("port", default=8888, help="run on the given port", type=int)

clients = dict()									# 用戶端Session字典

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render("index.html")

class MyWebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self, *args):							#有新連結是被呼叫
        self.id = self.get_argument("Id")
        self.stream.set_nodelay(True)
        clients[self.id] = {"id": self.id, "object": self}		#儲存Session到clients字典

    def on_message(self, message):        			#收到訊息時被呼叫
        print "Client %s received a message : %s" % (self.id, message)
        
    def on_close(self):							#關閉連線時被呼叫
        if self.id in clients:
            del clients[self.id]
            print "Client %s is closed" % (self.id)

    def check_origin(self, origin):
        return True

app = tornado.web.Application([
    (r'/', IndexHandler),
    (r'/websocket', MyWebSocketHandler),
])

import threading
import time

#啟動單獨的執行緒執行此函數，每隔1秒鍾向所有的用戶端推送目前時間
def sendTime():								
    import datetime
    while True:
        for key in clients.keys():
            msg = str(datetime.datetime.now())
            clients[key]["object"].write_message(msg)
            print "write to client %s: %s" % (key,msg)
        time.sleep(1)

  
if __name__ == '__main__':
    threading.Thread(target=sendTime).start()			#啟動推送時間執行緒
    parse_command_line()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()			#暫停執行
