#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask
app = Flask(__name__)

from flask import abort, redirect

@app.route('/')
def index():
    return redirect('/check')					#重導至/login頁面

@app.route('/check')
def f_check():
    abort(401)								#立即向用戶端傳回401錯誤
#    dont_coding_here()						#這裡的程式碼不會被執行

if __name__ == '__main__':
    app.run()
