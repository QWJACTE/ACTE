#!/usr/bin/python
# -*- encoding=utf-8 -*-

from flask import Flask, request, jsonify, render_template
import socket
from handle import *
app = Flask(__name__)

HOST = '121.42.145.248'
PORT = 8080

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/readme')
def readme():
    return render_template('readme.txt',abc='helloworld')

# @app.route('/post', method=['POST'])
# def post():
#     # todo....

# @app.route('/get', method=['GET'])
# def get():
#     # todo....

@app.route('/signup')
def signup():
#    uid = 'hello'#request.form['uid']
#    password = 'bb'request.form['password']
#    if uid != '' and password != '':
#        return "get it"
#    else: return "get nothing"
    return 'hello'

def main():
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.bind((HOST, PORT))
    ss.listen(5)

    while True:
        print 'begin accept'
        conn, addr = ss.accept()
        # record Client address
        log.get_log('Client addr', str(addr))

        try:
            conn.settimeout(50)
            buf = conn.recv(2048)
            back_msg = handle.handle(buf)
            if back_msg[0] == const.ILLEGAL_REQUEST:
                raise ILLEGAL_REQUEST_EXCEPTION
            else:
                conn.sendall(back_msg[1])
        except socket.timeout:
            print 'time out'
        except ILLEGAL_REQUEST_EXCEPTION:
            conn.sendall(const.ILLEGAL_REQUEST)
        conn.close()

    ss.close()

if __name__ == '__main__':
    app.run()
