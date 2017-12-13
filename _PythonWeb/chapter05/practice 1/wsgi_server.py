#!/usr/bin/env python
# -*- coding: utf-8 -*-

#引入Python的WSGI包
from wsgiref.simple_server import make_server
#引入伺服器端程式程式碼
from webapp import application

#案例化一個監聽8080通訊埠的伺服器
server = make_server('', 8080, application)
# 開始監聽HTTP請求:
server.serve_forever()
